import sqlite3 as sq


# ADD TRY AND EXCEPT STATEMENTS TO ALL DATABASE CONNECTIONS AND QUERIES
class databaseAbstraction:
    connectionAddress = ""
    username = ""
    password = ""

    def __init__(self, connectionAddress, username, password):
        self.connectionAddress = connectionAddress
        self.username = username
        self.password = password

    # Connects to a database and ret
    # .urns a connection object
    def __connectToDB(self):
        connection = sq.connect(self.getDbLocation())
        return connection

    def getDbLocation(self):
        return self.connectionAddress

    def selectAllFromTable(self, Table):
        try:
            conn = self.__connectToDB()
            cursor = conn.cursor()
            queryString = ("SELECT * FROM %s" % Table)
            obj = cursor.execute(queryString)
            conn.commit()
            objList = obj.fetchall()  # 'Save' a copy as we close obj
        except Exception as err:
            print(err)
        finally:
            conn.close()
            return objList

    def selectFromTableWhereFieldEqualsValue(self, Table, Item, Value):
        conn = self.__connectToDB()
        try:
            cursor = conn.cursor()
            queryString = ('SELECT * FROM %s WHERE %s = %s' % (Table, Item, Value))
            returnObjList = []
            returnObjList = cursor.execute(queryString).fetchall()
            conn.commit()
        except Exception as err:
            print("EXCEPTION OCCURED AT sectfromtablewhereFieldequalsvalue")
            print(err)
        finally:
            conn.close()
            return returnObjList

    # This needs testing
    def deleteFromTableWhereFieldEqualsValue(self, Table, Item, Value):
        try:
            conn = self.__connectToDB()
            cursor = conn.cursor()
            if isinstance(Value, str):
                Value = "'%s'" % Value
            print(Value)
            queryString = ('DELETE FROM %s WHERE %s = %s' % (Table, Item, Value))
            print(queryString)
            cursor.execute(queryString)
            conn.commit()
        except Exception as err:
            print(err)
        finally:
            conn.close()

    def insertIntoTableWhereColNamesEqualWhereValuesEqual(self, Table=[], ColumnNames=[], Values=[]):
        conn = self.__connectToDB()  # Connect to database
        cursor = conn.cursor()

        # Check Types
        Table = self.__checkIsList(Table)
        ColumnNames = self.__checkIsList(ColumnNames)
        Values = self.__checkIsList(Values)

        # check correct array lengths
        if len(ColumnNames) != len(Values):
            print("ERROR - Lists not equal length")
            return

        try:
            queryString = 'INSERT INTO %s (%s) VALUES (%s)' % (
                Table.__str__()[2:-2], ColumnNames.__str__()[1:-1], Values.__str__()[1:-1])
            print(queryString)
            cursor.execute(queryString)
            conn.commit()
        except Exception as err:
            print("CUNT")
            print(err)
        finally:
            conn.close()

    def updateFromTableWhereFieldNameEqualsAndValueNameEqualsValue(self, tableName, fieldName, fieldEquals, valueName, valueEquals):
        try:
            conn = self.__connectToDB()
            cursor = conn.cursor()

            queryString = ('UPDATE %s set %s = %s WHERE %s = %s' % (tableName, valueName, valueEquals, fieldName, fieldEquals))
            print(queryString)
            cursor.execute(queryString)
            conn.commit()
        except Exception as err:
            print(err)
        finally:
            conn.close()

    # UPDATE
    # ITEM_LIST
    # set
    # TAG_STATUS = 1
    # WHERE
    # UUID = 67305985

    # Function checks if input is a list. If its not it will convert it to a List
    def __checkIsList(self, isList):
        if isinstance(isList, list):
            return isList
        else:
            return [isList]
