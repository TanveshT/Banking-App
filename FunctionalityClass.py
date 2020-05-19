import mysql.connector as con
import csv

mydb = con.connect(host = 'localhost',user = 'root',passwd = 'noname@123', database ='tanvesh')
mycursor = mydb.cursor()

class Account:


    username = ""
    password = ""

    #constructor
    def __init__(self,user,passwd):

        self.username = user
        self.password = passwd

    def depositOperation(self,amount):

        total = self.checkBalance() + int(amount)

        query = "UPDATE user SET Balance = %s WHERE username = %s and password =%s"
        val = [str(total),(self.username).upper(),self.password]
        try:
            mycursor.execute(query,val)
            mydb.commit()
        except con.IntegrityError:
            return False   #USE First As Flag and Second as Amount
            #tkMessageBox.showinfo("CANNOT DEPOSITED", "DEPOSIT OPERATION WAS UNSUCCESSFUL",parent = Deposit)
        finally:
            query = "INSERT INTO Transaction_table(To_User, From_User, Amount, Type) values(%s, %s, %s, %s)"
            val = ["to SELF", self.username.upper(), str(amount), "DEPOSIT"]
            mycursor.execute(query,val)
            mydb.commit()
            return True  #USE First As Flag and Second as Amount
            #labelCurrentB.configure(text="CURRENT BALANCE: " + str(total))
            #tkMessageBox.showinfo("DEPOSIT SUCCESSFUL", "AMOUNT DEPOSITED",parent = Deposit )

    def checkBalance(self):

        query = "SELECT Balance FROM user WHERE username = %s and password = %s"
        val = [self.username.upper(), self.password]
        mycursor.execute(query, val)
        records = mycursor.fetchall()
        amount = 0
        if records[0][0] is None:
            amount = 0
        else:
            amount = int(records[0][0])

        return amount

        #labelCurrentB.configure(text="CURRENT BALANCE: " + str(records[0][0]))

    def withdrawalOperation(self,amount):

        total = self.checkBalance() - int(amount)

        query = "UPDATE user SET Balance = %s WHERE username = %s and password =%s"
        val = [str(total), self.username.upper(), self.password]
        try:
            mycursor.execute(query, val)
            mydb.commit()
        except con.IntegrityError:
            return 0
            #tkMessageBox.showinfo("CANNOT WITHDRAWAL", "WITHDRAWAL OPERATION WAS UNSUCCESSFUL", parent=Withdrawal)
        finally:
            query = "INSERT INTO Transaction_table(To_User, From_User, Amount, Type) values(%s, %s, %s, %s)"
            val = ["to SELF", self.username.upper(), str(amount), "WITHDRAWN"]
            mycursor.execute(query,val)
            mydb.commit()
            return 1
            #labelCurrentB.configure(text="CURRENT BALANCE: " + str(total))
            #tkMessageBox.showinfo("WITHDRAWAL SUCCESSFUL", "AMOUNT WITHDRAWN", parent=Withdrawal)


    # retuns 0 - insufficient funds , 1 - no to_user found, 2- Successful transaction
    def transferOperation(self, tousername,amount,type):

        query = "SELECT Balance FROM user WHERE username = %s"
        val = [tousername.upper()]
        mycursor.execute(query,val)
        recordOfToUser = mycursor.fetchall()

        # if recordOfToUser[0][0] == "None":
        #     balanceOfToUser = 0
        # else:
        #     balanceOfToUser = recordOfToUser[0][0]

        if self.checkBalance() > int(amount):

            if recordOfToUser > 0:

                if recordOfToUser[0][0] is None:
                    balanceOfToUser = 0
                else:
                    balanceOfToUser = recordOfToUser[0][0]


                transactionInsertQuery = "INSERT into Transaction_table(To_User,From_User,Amount,Type) values(%s,%s,%s,%s)"
                updateUserBalanceQuery = "UPDATE user SET Balance = %s where username = %s"

                valForTransactionQuery = [tousername.upper(), self.username.upper(), str(amount), type]
                valForUpdatingCurrentUserBalance = [str(self.checkBalance() - int(amount)),
                                                    self.username.upper()]
                valForUpdatingToUserBalance = [str(int(balanceOfToUser) + int(amount)),
                                               tousername.upper()]


                mycursor.execute(transactionInsertQuery, valForTransactionQuery)
                mydb.commit()

                mycursor.execute(updateUserBalanceQuery, valForUpdatingCurrentUserBalance)
                mydb.commit()

                mycursor.execute(updateUserBalanceQuery, valForUpdatingToUserBalance)
                mydb.commit()

               # tkMessageBox.showinfo("TRANSACTION SUCCESFULL","TRANSACTION HAS BEEN MADE")
                return 2
            else:
                return 1
              #  tkMessageBox.showinfo("NO SUCH USER", "CHECK USERNAME OF THE USER TO WHOM YOU ARE SENDING MONEY", parent=Transfer)
        else:
            return 0
           # tkMessageBox.showinfo("INSUFFICIENT FUNDS", "FUNDS ARE NOT SUFFICIENT FOR THIS TRANSFER")

    @staticmethod
    def registerUser(username, password, email, type):
        query = "INSERT INTO user(username,password,email,TypeOfAccount) values(%s,%s,%s,%s)"
        val = [str(username.upper()),str(password),str(email),str(type)]
        mycursor.execute(query, val)
        mydb.commit()

    def checkLogin(self):

        query = "SELECT * FROM user WHERE username = %s and password = %s"
        values = [self.username.upper(), self.password]

        mycursor.execute(query, values)
        records = mycursor.fetchall()

        if len(records) > 0:
            return True
        else:
            return False
            #tkMessageBox.showinfo("NO DATA FOUND", "USERNAME OR PASSWORD IS WRONG")

    def fetchPassbook(self):

        query = "SELECT * FROM Transaction_table WHERE From_User= %s or To_User = %s"
        values = [self.username.upper(),self.username.upper()]

        mycursor.execute(query, values)
        records = mycursor.fetchall()

        if records > 0:
            return records
        else:
            return 0

    def fetchType(self):

        query = "SELECT TypeOfAccount FROM user WHERE username = %s"
        value = [self.username.upper()]

        mycursor.execute(query,value)
        records = mycursor.fetchall()

        if records > 0:
            return records[0]
        else:
            return 0

    def getAccountID(self):

        query = "SELECT Account_id FROM user WHERE username = %s"
        val = [self.username]

        mycursor.execute(query, val)
        records = mycursor.fetchall()

        return records[0]

    def writeCSV(self):

        query = "SELECT * FROM Transaction_table WHERE From_User = %s or To_User = %s"
        val = [self.username,self.username]

        mycursor.execute(query,val)

        records = mycursor.fetchall()
        filename = self.username + "_" + str(self.getAccountID()[0])
        with open(filename + ".csv", "w+") as TransactionCSV:
            fields = ["ID","To_USER","From_USER","Amount","Type","DATE"]
            TransactionCSV.seek(0)
            csvWriter = csv.DictWriter(TransactionCSV, delimiter=',', fieldnames=fields )
            csvWriter.writeheader()
            for record in records:

                csvWriter.writerow({"ID":str(record[0]),"To_USER":str(record[1]),"From_USER":str(record[2]),"Amount":str(record[3]),"Type":str(record[4]),"DATE":str(record[5])})

            return 1  # AFTER OPERATION IS DONE


class SavingsAccount(Account):

    type = "Savings"
    minimum_balance = 5000

class CurrentAccount(Account):

    type = "Current"
