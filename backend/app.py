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
                cursor.execute("SELECT q.departure, q.arrival, q.destination, q.travellers, q.transportation, q.name, q.email, q.phoneNumber, q.finalprice,q.Id FROM quotes q WHERE Id=?",[quoteId,])
            else:
                cursor.execute("SELECT  q.departure, q.arrival, q.destination, q.travellers, q.transportation, q.name, q.email, q.phoneNumber, q.finalprice,q.Id FROM quotes q")
            quotes = cursor.fetchall()
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
                allQuotes = []
                for quote in quotes:
                    quotes_info = {
                        "departure": quote[0],
                        "arrival": quote[1],
                        "destination": quote[2],
                        "travellers": quote[3],
                        "transportation": quote[4],
                        "name": quote[5],
                        "email": quote[6],
                        "phoneNumber": quote[7],
                        "finalprice": quote[8],
                        "quoteId": quote[9],
                    }
                    allQuotes.append(quotes_info)
                return Response(json.dumps(allQuotes, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)


    elif request.method == "POST":
        conn = None
        cursor = None
        quotes_departure = request.json.get("departure")
        quotes_arrival = request.json.get("arrival") 
        quotes_destination = request.json.get("destination")
        quotes_travellers = request.json.get("travellers")
        quotes_transportation = request.json.get("transportation")
        quotes_name = request.json.get("name")
        quotes_email = request.json.get("email")
        quotes_phonenumber = request.json.get("phonenumber")
        quotes_finalprice = request.json.get("finalprice")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO quotes(departure,arrival,destination,travellers,transportation,name,email,phonenumber,finalprice) VALUES(?,?,?,?,?,?,?,?,?)",[quotes_departure,quotes_arrival,quotes_destination,quotes_travellers,quotes_transportation,quotes_name,quotes_email,quotes_phonenumber,quotes_finalprice])
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
            print("There was a coding error by wetBat: ")
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
            

@app.route('/api/airports', methods = ["GET"])
def destinationendpoint():
    if request.method == "GET":
        conn = None
        cursor = None
        destinations = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM airport")
            destinations = cursor.fetchall()
            print(destinations)
        except mariadb.ProgrammingError as error:
            print("There was a coding error by wetBat: ")
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
            if(destinations != None):
                all_destinations = []
                for destination in destinations:
                    destination_info = {
                        "Id" : destination[0],
                        "name" : destination[1]
                    }
                    all_destinations.append(destination_info)

                return Response(json.dumps(all_destinations, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)


@app.route('/api/transportation', methods = ["GET"])
def transportationendpoint():
    if request.method == "GET":
        conn = None
        cursor = None
        transportations = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM transportation")
            transportations = cursor.fetchall()
            print(transportations)
        except mariadb.ProgrammingError as error:
            print("There was a coding error by wetBat: ")
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
            if(transportations != None):
                all_transportation = []
                for transportation in transportations:
                    transportation_info = {
                        "Id" : transportation[0],
                        "name" : transportation[1]
                    }
                    all_transportation.append(transportation_info)

                return Response(json.dumps(all_transportation, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)