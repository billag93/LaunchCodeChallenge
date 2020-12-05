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
# The api route that will connect my front end to flask which will communicate with mariadb (database).
@app.route('/api/quotes', methods = ["GET","POST", "PATCH", "DELETE"])
def quotesendpoint():
    # this get endpoint will recieve all the quotes or it will get an individual quote when sending the quote Id
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

# This endpint will post a quote to the database and will create a new quote Id. The Id is autoincremented.
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

# This endpoint will update an existing quote by passing down a quote Id in the front end using props from the parent component. We use the WHERE clause in our SQL statements.
    elif request.method == "PATCH":
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
        quoteId = request.json.get("quoteId")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if quotes_departure != "" and quotes_departure != None:
                cursor.execute("UPDATE quotes q SET q.departure=? WHERE Id=?",[quotes_departure,quoteId,])
            if quotes_arrival != "" and quotes_arrival != None:
                cursor.execute("UPDATE quotes q SET q.arrival=? WHERE Id=?",[quotes_arrival,quoteId,])
            if quotes_destination  != "" and quotes_destination != None:
                cursor.execute("UPDATE quotes q SET q.destination=? WHERE Id=?",[quotes_destination,quoteId,])
            if quotes_travellers != "" and quotes_travellers != None:
                cursor.execute("UPDATE quotes q SET q.travellers=? WHERE Id=?",[quotes_travellers,quoteId,])
            if quotes_transportation != "" and quotes_transportation != None:
                cursor.execute("UPDATE quotes q SET q.transportation=? WHERE Id=?",[quotes_transportation,quoteId,])
            if quotes_name != "" and quotes_name != None:
                cursor.execute("UPDATE quotes q SET q.name=? WHERE Id=?",[quotes_name,quoteId,])
            if quotes_email  != "" and quotes_email != None:
                cursor.execute("UPDATE quotes q SET q.email=? WHERE Id=?",[quotes_email,quoteId,])
            if quotes_phonenumber  != "" and quotes_phonenumber != None:
                cursor.execute("UPDATE quotes q SET q.phoneNumber=? WHERE Id=?",[quotes_phonenumber,quoteId,])
            if quotes_finalprice  != "" and quotes_finalprice != None:
                cursor.execute("UPDATE quotes q SET q.finalprice=? WHERE Id=?",[quotes_finalprice,quoteId,])
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
                    "departure": quote[0],
                    "arrival": quote[1],
                    "destination": quote[2],
                    "travellers": quote[3],
                    "transportation": quote[4],
                    "name": quote[5],
                    "email": quote[6],
                    "phoneNumber": quote[7],
                    "finalprice": quote[8],
                
                }
                return Response(json.dumps(this_quote, default = str), mimetype = "application/json", status = 200)
            else: 
                return Response("Updated Failed", mimetype="text/html", status=404)
# This endpoint will delete a quote using the same method as updating a quote. 
    elif request.method == "DELETE":
        conn = None
        cursor = None
        quoteId = request.json.get("quoteId")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM quotes WHERE Id=?",[quoteId])
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
            
# A table of airports was created in the DB and this endpoint will grab all the available airports from the DB. 
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

# A table of rental companies was created in the DB and this endpoint will grab all the available airports from the DB.
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