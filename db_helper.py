#import psycopg2
#from psycopg2 import Error
#import os
#import json
#from urllib.parse import urlparse
#from settings import config
#
#
##Connect to an existing database
##db_url = os.environ.get("DATABASE_URL")
#db_url = config.DATABASE_URL
#result = urlparse(db_url)
#username = result.username
#password = result.password
#database = result.path[1:]
#hostname = result.hostname
#port = result.port
#def conn():
#    connection = psycopg2.connect(
#                                    database = database,
#                                    user = username,
#                                    password = password,
#                                    host = hostname,
#                                    port = port
#                                )
#    return connection
#
#def jsing(dic):
#    """convert dict variable to json object"""
#    json_object = json.dumps(dic, indent = 4) 
#    return json_object
#
#def create_table():
#    created = False
#    con = conn()
#    cur = con.cursor()
#    create_table = """
#                    CREATE TABLE fairco
#                    (name    TEXT    PRIMARY KEY    NOT NULL,
#                    value    JSONB    NOT NULL);
#                    """
#    try:
#        cur.execute(create_table)
#        con.commit()
#    except psycopg2.Error as error:
#        print(f'error occured\n{error}')
#    else:
#        created = True
#        cur.close()
#        con.close()
#    finally:
#        return created
#
#
#def insert(element_name,element_value):
#    inserted = False
#    con = conn()
#    cur = con.cursor()
#    insert_query =  """ 
#                    INSERT INTO fairco (name,value) 
#                    VALUES (%s,%s)
#                    """
#    try:
#        cur.execute(insert_query,(element_name,element_value,))
#        con.commit()
#    except psycopg2.Error as error:
#        print(f'error occured\n{error}')
#    else:
#        inserted = True
#        cur.close()
#        con.close()
#    finally:
#        return inserted
#
#def update(element_name,element_value):
#    updated = False
#    con = conn()
#    cur = con.cursor()
#    update_query =   """Update fairco 
#                        set value = %s 
#                        where name = %s """
#    try:
#        cur.execute(update_query,(element_value,element_name,))
#        con.commit()
#    except psycopg2.Error as error:
#        print(f'error occured\n{error}')
#    else:
#        updated = True
#        cur.close()
#        con.close()
#    finally:
#        return updated
#
#def retrieve(element_name):
#    con = conn()
#    cur = con.cursor()
#    retrieve_query= """
#                    SELECT value 
#                    FROM fairco
#                    WHERE name = %s 
#                    """
#    cur.execute(retrieve_query,(element_name,))
#    row = cur.fetchone()
#    while row is not None:
#        log = row
#        row = cur.fetchone()
#    con.commit()
#    cur.close()
#    con.close()
#    return dict(log[0])
#
