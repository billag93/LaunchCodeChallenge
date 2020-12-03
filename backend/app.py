from flask import Flask, request, Response
from flask_cors import CORS
import mariadb 
import random 
import json
import dbcreds
import secrets
import datetime

def generateToken():
    random_alphanumeric = secrets.token_urlsafe(20)
    return random_alphanumeric
def createDateTime():
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d")
    return currentdate

app = Flask(__name__)
CORS(app)

@app.route('/api/quotes', methods = ["GET","POST", "PATCH", "DELETE"])
def quotesendpoint():
    if request.method == "GET":
        conn = None
        cursor = None
        quotes = None
        quoteId = request.args.get("quoteId")
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if quoteId != "" and quoteId != None:
                cursor.execute("SELECT q.departure, q.arrival, q.destination, q.travellers, q.transportation, q.name, q.email, q.phoneNumber, q.finalprice FROM quotes q WHERE Id=?",[quoteId,])
            else:
                cursor.execute("SELECT  q.departure, q.arrival, q.destination, q.travellers, q.transportation, q.name, q.email, q.phoneNumber, q.finalprice FROM quotes q")
            quotes = cursor.fetchall()[0]
            print(quotes)
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(quotes != None):
                quotes_info = {
                    "departure": quotes[4],
                    "arrival": quotes[1],
                    "destination": quotes[0],
                    "travellers": quotes[2],
                    "transportation": quotes[3],
                    "name": quotes[0],
                    "email": quotes[2],
                    "phoneNumber": quotes[3],
                    "finalprice": quotes[3],
                    "quotenumber": quotes[3],
                }
                return Response(json.dumps(quotes_info, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)


    elif request.method == "POST":
        conn = None
        cursor = None
        quotes_departure = request.json.get("departure")
        quotes_arrival = request.json.get("arrival") 
        quotes_destination = request.json.get("destination")
        quotes_travellers = request.json.get("travellers")
        quotes_name = request.json.get("name")
        quotes_email = request.json.get("email")
        quotes_phonenumber = request.json.get("phonenumber")
        quotes_finalprice = request.json.get("finalprice")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO quotes(departure,arrival,destination,travellers,name,email,phonenumber,finalprice) VALUES(?,?,?,?,?,?,?,?)",[quotes_departure,quotes_arrival,quotes_destination,quotes_travellers,quotes_name,quotes_email,quotes_phonenumber,quotes_finalprice])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("quote inserted!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)


    elif request.method == "PATCH":
        conn = None
        cursor = None
        quotes_departure = request.json.get("departure")
        quotes_arrival = request.json.get("arrival") 
        quotes_destination = request.json.get("destination")
        quotes_travellers = request.json.get("travellers")
        quotes_name = request.json.get("name")
        quotes_email = request.json.get("email")
        quotes_phonenumber = request.json.get("phonenumber")
        quotes_finalprice = request.json.get("finalprice")
        quoteId = request.json.get("quoteId")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if quotes_departure != "" and quotes_departure != None:
                cursor.execute("UPDATE quotes q SET q.departure WHERE Id=?",[quotes_departure,quoteId,])
            if quotes_arrival != "" and quotes_arrival != None:
                cursor.execute("UPDATE quotes q SET q.arrival WHERE Id=?",[quotes_arrival,quoteId,])
            if quotes_destination  != "" and quotes_destination != None:
                cursor.execute("UPDATE quotes q SET q.destination WHERE Id=?",[quotes_destination,quoteId,])
            if quotes_travellers != "" and quotes_travellers != None:
                cursor.execute("UPDATE quotes q SET q.travellers WHERE Id=?",[quotes_travellers,quoteId,])
            if quotes_name != "" and quotes_name != None:
                cursor.execute("UPDATE quotes q SET q.name WHERE Id=?",[quotes_name,quoteId,])
            if quotes_email  != "" and quotes_email != None:
                cursor.execute("UPDATE quotes q SET q.email WHERE Id=?",[quotes_email,quoteId,])
            if quotes_phonenumber  != "" and quotes_phonenumber != None:
                cursor.execute("UPDATE quotes q SET q.phoneNumber WHERE Id=?",[quotes_phonenumber,quoteId,])
            if quotes_finalprice  != "" and quotes_finalprice != None:
                cursor.execute("UPDATE quotes q SET q.finalprice WHERE Id=?",[quotes_finalprice,quoteId,])
            conn.commit()
            cursor.execute("SELECT q.departure, q.arrival, q.destination, q.travellers, q.transportation, q.name, q.email, q.phoneNumber, q.finalprice FROM quotes q WHERE q.Id=?",[quoteId])
            quote = cursor.fetchall()[0]
            print(quote)
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                this_quote = {
                    "departure": quotes[4],
                    "arrival": quotes[1],
                    "destination": quotes[0],
                    "travellers": quotes[2],
                    "transportation": quotes[3],
                    "name": quotes[0],
                    "email": quotes[2],
                    "phoneNumber": quotes[3],
                    "finalprice": quotes[3],
                    "quotenumber": quotes[3],
                }
                return Response(json.dumps(this_quote, default = str), mimetype = "application/json", status = 200)
            else: 
                return Response("Updated Failed", mimetype="text/html", status=404)

    elif request.method == "DELETE":
        conn = None
        cursor = None
        quoteId = request.args.get("quoteId")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM quotes q WHERE q.Id=?",[quoteId])
            conn.commit()
            rows = cursor.rowcount
        except mariadb.ProgrammingError as error:
            print("There was a coding error by Twatter: ")
            print(error)
        except mariadb.DatabaseError as error:
            print("There has been a database error: ")
            print(error)
        except mariadb.OperationalError as error:
            print("Connection error, please check your dbcreds: ")
            print(error)
        except Exception as error:
            print("You should add an exception for htis error: ")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("DELETE Success", mimetype = "text/html", status = 204)
            else: 
                return Response("DELETE Failed", mimetype="text/html", status=404)