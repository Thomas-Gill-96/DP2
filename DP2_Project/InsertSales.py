import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sreps"
)
print(mydb)

mycursor = mydb.cursor()

def InsertSales (aSalesDate, aItemID, aItemQuant, aTotalCost):
    sale_date = aSalesDate
    item_id = aItemID
    item_quantity = aItemQuant
    total_cost = aTotalCost

    if (aSalesDate == "") or (aItemID == "") or (aItemQuant == "") or (aTotalCost == ""):
        print("Error, an item must have a Name and Price")
    else:
        sql = "INSERT INTO Sales (sale_date, item_id, item_quantity, total_cost) VALUES (%s, %s, %s, %s)"
        val = (sale_date, item_id, item_quantity, total_cost)
        mycursor.execute (sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")
