import mysql.connector

def InsertItem (itemName, itemPrice):
    if (itemName == "") or (itemPrice == ""):
        print("Error, an item must have a Name and Price")
    else:
        query = "INSERT INTO items(item_name, item_price) VALUES ('" + itemName + "', '" + itemPrice + "')"
        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")



def GetSalesRecord(startDate = "", endDate = "", saleID = ""):
    query = ""

    if (saleID != ""):
        query = "SELECT Sales.sale_id, Sales.sale_date, Items.item_name, Sales.item_quantity, Sales.total_cost FROM Sales INNER JOIN Items ON Sales.item_id = Items.item_id WHERE Sales.sale_id = " + saleID
    elif (startDate != "") and (endDate == ""):
        query = "SELECT Sales.sale_id, Sales.sale_date, Items.item_name, Sales.item_quantity, Sales.total_cost FROM Sales INNER JOIN Items ON Sales.item_id = Items.item_id WHERE Sales.sale_date >= '" + startDate + "'"
    elif (startDate != "") and (endDate != ""):
        query = "SELECT Sales.sale_id, Sales.sale_date, Items.item_name, Sales.item_quantity, Sales.total_cost FROM Sales INNER JOIN Items ON Sales.item_id = Items.item_id WHERE Sales.sale_date BETWEEN '" + startDate + "' AND '" + endDate + "'"
    else:
        print("Error, invalid search parameters.")
        return -1

    mycursor = mydb.cursor()
    mycursor.execute(query)
    records = mycursor.fetchall()

    return records







mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sreps"
)
print(mydb)
mycursor = mydb.cursor()