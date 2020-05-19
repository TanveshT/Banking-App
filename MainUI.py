import Tkinter as tk
import tkMessageBox
import FunctionalityClass
import ttk


font10 = "-family {Abyssinica SIL} -size 14 -weight bold -slant roman -underline 0 -overstrike 0"
font9 = "-family FreeMono -size 15 -weight bold -slant roman -underline 0 -overstrike 0"

def DepositPage():
    def depositOperation():
        if(loginAccount.depositOperation(txtDeposit.get())):
            labelCurrentB.configure(text="CURRENT BALANCE: " + str(loginAccount.checkBalance()))
            tkMessageBox.showinfo("DEPOSIT SUCCESSFUL", "AMOUNT DEPOSITED",parent = Deposit)
        else:
            tkMessageBox.showinfo("CANNOT DEPOSITED", "DEPOSIT OPERATION WAS UNSUCCESSFUL", parent=Deposit)

    AfterLogin.destroy()
    Deposit = tk.Toplevel()

    Deposit.attributes('-fullscreen', True)
    Deposit.title("Deposit")
    Deposit.configure(background="#41d8d8")

    Label1 = tk.Label(Deposit)
    Label1.place(rely=0.044, height=100, width=1366)
    Label1.configure(background="#16d843")
    Label1.configure(text='''KONOHA SAHAKARI BANK - DEPOSIT PAGE''')
    Label1.configure(font = font9)
    Label1.configure(width=476)

    labelCurrentB = tk.Label(Deposit)
    labelCurrentB.place(relx=0.25, rely=0.267, height=58, width=271)
    labelCurrentB.configure(background="#279dd8")
    labelCurrentB.configure(cursor="fleur")
    labelCurrentB.configure(font=font10)
    labelCurrentB.configure(text='''CURRENT BALANCE:''')
    labelCurrentB.configure(width=271)

    Label3 = tk.Label(Deposit)
    Label3.place(relx=0.117, rely=0.489, height=58, width=196)
    Label3.configure(background="#279dd8")
    Label3.configure(font=font10)
    Label3.configure(text='''DEPOSIT AMOUNT:''')
    Label3.configure(width=196)

    txtDeposit = tk.Entry(Deposit)
    txtDeposit.place(relx=0.483, rely=0.489, height=60, relwidth=0.327)
    txtDeposit.configure(background="white")
    txtDeposit.configure(font=font9)
    txtDeposit.configure(width=196)

    btnDeposit = tk.Button(Deposit, command=depositOperation)
    btnDeposit.place(rely=0.65, height=170, width=1366)
    btnDeposit.configure(background="#09a8d8")
    btnDeposit.configure(text="DEPOSIT MONEY")

    btnCancel = tk.Button(Deposit, command=lambda:[Deposit.destroy(),AfterLoginPage()])
    btnCancel.place(rely=0.85, height=120, width=1366)
    btnCancel.configure(background="#09a8d8")
    btnCancel.configure(text="CANCEL")

    labelCurrentB.configure(text="CURRENT BALANCE: " + str(loginAccount.checkBalance()))
    Deposit.mainloop()

def Registration():

    def returnValue(value):
        global typeofAccount
        typeofAccount = str(value)

    def registerUser():
        FunctionalityClass.Account.registerUser(txtUsername.get(),txtPassword.get(),txtEmail.get(), str(tkvar.get()))
        RegisterPage.destroy()

    RegisterPage = tk.Toplevel()

    RegisterPage.title("Registration")
    RegisterPage.attributes('-fullscreen', True)
    RegisterPage.configure(background="#41d8d8")

    Label1 = tk.Label(RegisterPage)
    Label1.place(rely=0.022, height=100, width=1366)
    Label1.configure(background="#16d843")
    Label1.configure(text='''KONOHA REGISTRATION WINDOW''')
    Label1.configure(font=font9)
    Label1.configure(width=576)

    Label2 = tk.Label(RegisterPage)
    Label2.place(relx=0.167, rely=0.222, height=40, width=200)
    Label2.configure(background="#279dd8")
    Label2.configure(text='''USERNAME:''')
    Label2.configure(font = font9)
    Label2.configure(width=156)

    TypeOfAccount = tk.Label(RegisterPage)
    TypeOfAccount.place(relx=0.167, rely=0.589, height=40, width=200)
    TypeOfAccount.configure(background="#279dd8")
    TypeOfAccount.configure(text='''Type Of Account:''')
    TypeOfAccount.configure(font = font9)
    TypeOfAccount.configure(width=156)

    txtUsername = tk.Entry(RegisterPage)
    txtUsername.place(relx=0.55, rely=0.222, height=40, relwidth=0.4)
    txtUsername.configure(background="white")
    txtUsername.configure(font = font9)

    Label3 = tk.Label(RegisterPage)
    Label3.place(relx=0.167, rely=0.356, height=40, width=200)
    Label3.configure(background="#279dd8")
    Label3.configure(text='''PASSWORD:''')
    Label3.configure(font = font9)
    Label3.configure(width=157)

    Label4 = tk.Label(RegisterPage)
    Label4.place(relx=0.167, rely=0.489, height=40, width=200)
    Label4.configure(background="#279dd8")
    Label4.configure(text='''EMAIL ID:''')
    Label4.configure(font = font9)
    Label4.configure(width=162)

    tkvar = tk.StringVar(RegisterPage)
    choices = {'Savings', 'Current'}

    tkvar.set("CHOOSE ONE")
    dropdown = tk.OptionMenu(RegisterPage, tkvar, *choices, command = returnValue)
    dropdown.place(relx = 0.55, rely = 0.589, height = 58, width = 271)
    dropdown.configure(background = 'white')
    dropdown.configure(font = font9)

    txtPassword = tk.Entry(RegisterPage)
    txtPassword.place(relx=0.55, rely=0.356, height=40, relwidth=0.4)
    txtPassword.configure(background="white")
    txtPassword.configure(font = font9)

    txtEmail = tk.Entry(RegisterPage)
    txtEmail.place(relx=0.55, rely=0.489, height=40, relwidth=0.4)
    txtEmail.configure(background="white")
    txtEmail.configure(font = font9)

    Button1 = tk.Button(RegisterPage, command=registerUser)
    Button1.place(rely=0.7, height=220, width=683)
    Button1.configure(background="#09a8d8")
    Button1.configure(font = font9)
    Button1.configure(text='''Submit''')
    Button1.configure(width=122)

    Button2 = tk.Button(RegisterPage, command=RegisterPage.destroy)
    Button2.place(relx=0.5, rely=0.7, height=220, width=683)
    Button2.configure(font = font9)
    Button2.configure(background="#09a8d8")
    Button2.configure(text='''Exit''')
    Button2.configure(width=121)

    RegisterPage.mainloop()

def WithdrawalPage():

    def withdrawalOperation():
        if(loginAccount.withdrawalOperation(txtWithdrawal.get())):
            labelCurrentB.configure(text="CURRENT BALANCE: " + str(loginAccount.checkBalance()))
            tkMessageBox.showinfo("WITHDRAWAL SUCCESSFUL", "AMOUNT WITHDRAWN",parent = Withdrawal )
        else:
            tkMessageBox.showinfo("CANNOT WITHDRAW", "WITHDRAWAL OPERATION WAS UNSUCCESSFUL", parent=Withdrawal)

    AfterLogin.destroy()
    Withdrawal = tk.Toplevel()

    Withdrawal.attributes('-fullscreen', True)
    Withdrawal.title("WITHDRAW")
    Withdrawal.configure(background="#41d8d8")

    Label1 = tk.Label(Withdrawal)
    Label1.place(rely=0.044, height=100, width=1366)
    Label1.configure(background="#16d843")
    Label1.configure(text='''KONOHA SAHAKARI BANK - WITHDRAWAL PAGE''')
    Label1.configure(font=font9)
    Label1.configure(width=476)

    labelCurrentB = tk.Label(Withdrawal)
    labelCurrentB.place(relx=0.25, rely=0.267, height=58, width=271)
    labelCurrentB.configure(background="#279dd8")
    labelCurrentB.configure(cursor="fleur")
    labelCurrentB.configure(font=font10)
    labelCurrentB.configure(text='''CURRENT BALANCE:''')
    labelCurrentB.configure(width=271)

    Label3 = tk.Label(Withdrawal)
    Label3.place(relx=0.117, rely=0.489, height=58, width=210)
    Label3.configure(background="#279dd8")
    Label3.configure(font=font10)
    Label3.configure(text='''WITHDRAWAL AMOUNT:''')
    Label3.configure(width=196)

    txtWithdrawal = tk.Entry(Withdrawal)
    txtWithdrawal.place(relx=0.483, rely=0.489, height=60, relwidth=0.327)
    txtWithdrawal.configure(background="white")
    txtWithdrawal.configure(font=font9)
    txtWithdrawal.configure(width=196)

    btnWithdrawal = tk.Button(Withdrawal, command=withdrawalOperation)
    btnWithdrawal.place(rely=0.65, height=170, width=1366)
    btnWithdrawal.configure(background="#09a8d8")
    btnWithdrawal.configure(text="WITHDRAW MONEY")

    btnCancel = tk.Button(Withdrawal, command=lambda:[Withdrawal.destroy(),AfterLoginPage()])
    btnCancel.place(rely=0.85, height=120, width=1366)
    btnCancel.configure(background="#09a8d8")
    btnCancel.configure(text="CANCEL")

    labelCurrentB.configure(text="CURRENT BALANCE: " + str(loginAccount.checkBalance()))
    Withdrawal.mainloop()

def TransferPage():

    Transfer = tk.Toplevel()

    def returnValue(value):
        global x
        x = str(value)

    def transferOperation():
        returnValueofTransfer = loginAccount.transferOperation(txtToUser.get(),txtAmount.get(), x)
        if(returnValueofTransfer == 0):
            tkMessageBox.showinfo("INSUFFICIENT FUNDS", "FUNDS ARE NOT SUFFICIENT FOR THIS TRANSFER", parent = Transfer)
        elif(returnValueofTransfer == 1):
            tkMessageBox.showinfo("NO SUCH USER", "CHECK USERNAME OF THE USER TO WHOM YOU ARE SENDING MONEY", parent=Transfer)
        else:
            tkMessageBox.showinfo("TRANSACTION SUCCESFULL", "TRANSACTION HAS BEEN MADE", parent = Transfer)


    Transfer.attributes('-fullscreen',True)
    Transfer.title("Transfer")
    Transfer.configure(background="#41d8d8")

    labelCurrentUser = tk.Label(Transfer)
    labelCurrentUser.place(relx=0.25, rely=0.2, height=58, width=271)
    labelCurrentUser.configure(background="#279dd8")
    labelCurrentUser.configure(cursor="fleur")
    labelCurrentUser.configure(font =  font10)
    labelCurrentUser.configure(text = "CURRENT USER: ")
    labelCurrentUser.configure(width=271)

    labelCurrentDisplay = tk.Label(Transfer)
    labelCurrentDisplay.place(relx=0.5, rely=0.2, height=58, width=271)
    labelCurrentDisplay.configure(background="#279dd8")
    labelCurrentDisplay.configure(cursor="fleur")
    labelCurrentDisplay.configure(font =  font10)
    labelCurrentDisplay.configure(text = str(loginAccount.username))
    labelCurrentDisplay.configure(width=271)

    labelCurrentDisplay = tk.Label(Transfer)
    labelCurrentDisplay.place(relx=0.25, rely=0.3, height=58, width=271)
    labelCurrentDisplay.configure(background="#279dd8")
    labelCurrentDisplay.configure(cursor="fleur")
    labelCurrentDisplay.configure(font =  font10)
    labelCurrentDisplay.configure(text = "TO: ")
    labelCurrentDisplay.configure(width=271)

    labelCurrentDisplay = tk.Label(Transfer)
    labelCurrentDisplay.place(relx=0.25, rely=0.4, height=58, width=271)
    labelCurrentDisplay.configure(background="#279dd8")
    labelCurrentDisplay.configure(cursor="fleur")
    labelCurrentDisplay.configure(font =  font10)
    labelCurrentDisplay.configure(text = "AMOUNT: ")
    labelCurrentDisplay.configure(width=271)

    labelCurrentDisplay = tk.Label(Transfer)
    labelCurrentDisplay.place(relx=0.25, rely=0.5, height=58, width=271)
    labelCurrentDisplay.configure(background="#279dd8")
    labelCurrentDisplay.configure(cursor="fleur")
    labelCurrentDisplay.configure(font =  font10)
    labelCurrentDisplay.configure(text = "TYPE: ")
    labelCurrentDisplay.configure(width=271)

    txtAmount = tk.Entry(Transfer)
    txtAmount.place(relx=0.5, rely=0.4, height=58, width=271)
    txtAmount.configure(background='white')
    txtAmount.configure(cursor="fleur")
    txtAmount.configure(font =  font10)
    txtAmount.configure(width=271)

    txtToUser = tk.Entry(Transfer)
    txtToUser.place(relx=0.5, rely=0.3, height=58, width=271)
    txtToUser.configure(background='white')
    txtToUser.configure(cursor="fleur")
    txtToUser.configure(font =  font10)
    txtToUser.configure(width=271)

    Label1 = tk.Label(Transfer)
    Label1.place(rely=0.022, height=100, width=1366)
    Label1.configure(background="#16d843")
    Label1.configure(text='''KONOHA TRANSFER PAGE''')
    Label1.configure(font=font9)
    Label1.configure(width=576)

    tkvar = tk.StringVar(Transfer)
    choices = {'RTGS', 'NEFT', 'ICMP'}

    tkvar.set("CHOOSE ONE")
    dropdown = tk.OptionMenu(Transfer, tkvar, *choices, command = returnValue)
    dropdown.place(relx = 0.5, rely = 0.5, height = 58, width = 271)
    dropdown.configure(background = 'white')

    btnTransfer = tk.Button(Transfer, command=transferOperation)
    btnTransfer.place(rely=0.65, height=170, width=1366)
    btnTransfer.configure(background="#09a8d8")
    btnTransfer.configure(text="TRANSFER")

    btnCancel = tk.Button(Transfer, command=lambda:[Transfer.destroy(),AfterLoginPage()])
    btnCancel.place(rely=0.85, height=120, width=1366)
    btnCancel.configure(background="#09a8d8")
    btnCancel.configure(text="CANCEL")

def PassbookPage():

    def exportCSV():

        x = loginAccount.writeCSV()
        if(x == 0):

            tkMessageBox.showinfo("NO TRANSACTION AVAILABLE","NO TRANSACTIONS AVAILABLE", parent = Passbook)
        else:
            tkMessageBox.showinfo("CSV EXPORTED","CSV EXPORTED",parent = Passbook)


    records = loginAccount.fetchPassbook()

    if records == 0:
        flag = 0
    else:
        flag = 1

    Passbook = tk.Toplevel()

    Passbook.geometry("600x400")
    Passbook.title("PassBook")
    Passbook.configure(background="#41d8d8")

    btnExportCSV = tk.Button(Passbook)
    btnExportCSV.place(relx = 0.75, rely = 0.5, height = 50, width = 100)
    btnExportCSV.configure(text = "CONVERT \n  TO \n CSV")
    btnExportCSV.configure(font = font9)
    btnExportCSV.configure(command = exportCSV)

    PassbookTable = ttk.Treeview(Passbook)
    PassbookTable.place(relx = 0.)
    PassbookTable["columns"] = ("ID", "To USER", "From USER", "AMOUNT", "TYPE")

    PassbookTable.column("#0", width=0)
    PassbookTable.column("ID", width=20)
    PassbookTable.column("To USER", width=100)
    PassbookTable.column("From USER", width=100)
    PassbookTable.column("AMOUNT", width=100)
    PassbookTable.column("TYPE", width=100)

    PassbookTable.heading("ID", text="ID")
    PassbookTable.heading("To USER", text="To USER")
    PassbookTable.heading("From USER", text="From User")
    PassbookTable.heading("AMOUNT", text="AMOUNT")
    PassbookTable.heading("TYPE", text="TYPE")

    if flag == 0:
        tkMessageBox.showinfo("NO TRANSACTIONS MADE", "NO TRANSACTIONS MADE")
    else:
        for record in records:
            PassbookTable.insert("", 0, text="", values=record)

def AfterLoginPage():

    global AfterLogin
    AfterLogin = tk.Toplevel()

    AfterLogin.attributes('-fullscreen', True)
    AfterLogin.title("AfterLogin")
    AfterLogin.configure(background="#41d8d8")

    btnDeposit = tk.Button(AfterLogin, command=DepositPage)
    btnDeposit.place(relx=0.0, rely=0.178, height=250, width=683)
    btnDeposit.configure(background="#09a8d8")
    btnDeposit.configure(font = font9)
    btnDeposit.configure(text='''DEPOSIT''')

    MainLabel = tk.Label(AfterLogin)
    MainLabel.place(rely=0.022, height=100, width=1366)
    MainLabel.configure(background="#16d843")
    MainLabel.configure(text='''WELCOME TO KONOHA SAHAKARI BANK''')
    MainLabel.configure(font=font9)
    MainLabel.configure(width=576)

    TypeLabel = tk.Label(MainLabel)
    TypeLabel.place(relx= 0.75, height= 50, width = 300)
    TypeLabel.configure(text = "ACCOUNT TYPE: " + str(loginAccount.type))
    TypeLabel.configure(font = font9)

    BalanceLabel = tk.Label(MainLabel)
    BalanceLabel.place(relx= 0.1, height= 50, width = 300)
    BalanceLabel.configure(text = "Balance: " + str(loginAccount.checkBalance()))
    BalanceLabel.configure(font = font9)

    btnLogout = tk.Button(AfterLogin, command=AfterLogin.destroy)
    btnLogout.place(relx=0.0, rely=0.825, height=130, width=1366)
    btnLogout.configure(background="#09a8d8")
    btnLogout.configure(text='''LOGOUT''')
    btnLogout.configure(font = font9)
    btnLogout.configure(width=299)

    btnTransfer = tk.Button(AfterLogin, command=TransferPage)
    btnTransfer.place(relx=0.0, rely=0.498, height=250, width=683)
    btnTransfer.configure(background="#09a8d8")
    btnTransfer.configure(text='''TRANSFER''')
    btnTransfer.configure(font = font9)

    btnWithdrawal = tk.Button(AfterLogin, command=WithdrawalPage)
    btnWithdrawal.place(relx=0.5, rely=0.178, height=250, width=683)
    btnWithdrawal.configure(background="#09a8d8")
    btnWithdrawal.configure(text='''WITHDRAWAL''')
    btnWithdrawal.configure(font = font9)
    btnWithdrawal.configure(width=299)

    btnPassbook = tk.Button(AfterLogin, command = PassbookPage)
    btnPassbook.place(relx=0.5, rely=0.498, height=250, width=683)
    btnPassbook.configure(background="#09a8d8")
    btnPassbook.configure(font = font9)
    btnPassbook.configure(text='''PASSBOOK''')

    if (loginAccount.type == "Savings" and loginAccount.checkBalance() < loginAccount.minimum_balance):
        tkMessageBox.showinfo("MINIMUM BALANCE ERROR","DEPOSIT MONEY MINIMUM BALANCE SHOULD BE 5000", parent = AfterLogin)

    AfterLogin.mainloop()

def Login():

    top = tk.Tk()

    top.title("Login")
    top.attributes('-fullscreen', True)
    top.configure(background="#41d8d8")

    Label1 = tk.Label(top)
    Label1.place(rely=0.022, height=100, width=1366)
    Label1.configure(background="#16d843")
    Label1.configure(text='''KONOHA SAHAKARI BANK LOGIN''')
    Label1.configure(font=font9)
    Label1.configure(width=576)

    txtUsername = tk.Entry(top)
    txtUsername.place(relx=0.5, rely=0.289, height=30, relwidth=0.277)
    txtUsername.configure(background="white")
    txtUsername.configure(font="TkFixedFont")
    txtUsername.configure(width=166)
    txtUsername.configure(font = font9)

    Label2 = tk.Label(top)
    Label2.place(relx=0.2, rely=0.267, height=48, width=156)
    Label2.configure(activebackground="#ededed")
    Label2.configure(background="#279dd8")
    Label2.configure(text='''USERNAME''')
    Label2.configure(width=156)
    Label2.configure(font = font9)

    Label3 = tk.Label(top)
    Label3.place(relx=0.2, rely=0.444, height=48, width=156)
    Label3.configure(background="#279dd8")
    Label3.configure(text='''PASSWORD''')
    Label3.configure(font = font9)
    Label3.configure(width=156)

    txtPassword = tk.Entry(top, show = "*")
    txtPassword.place(relx=0.5, rely=0.467, height=30, relwidth=0.277)
    txtPassword.configure(background="white")
    txtPassword.configure(font="TkFixedFont")
    txtPassword.configure(width=166)
    txtPassword.configure(font = font9)


    def login():

        global loginAccount
        loginAccount = FunctionalityClass.Account(str(txtUsername.get().upper()),str(txtPassword.get()))
        if(loginAccount.fetchType()):
            if(loginAccount.fetchType()[0] == "Savings"):
                loginAccount = FunctionalityClass.SavingsAccount(str(txtUsername.get().upper()),str(txtPassword.get()))
            else:
                loginAccount = FunctionalityClass.CurrentAccount(str(txtUsername.get().upper()),str(txtPassword.get()))
        else:
            tkMessageBox.showinfo("INVALID USERNAME", "INVALID USERNAME", parent = top)
        if((loginAccount.checkLogin())):
            AfterLoginPage()
        else:
            tkMessageBox.showinfo("NO DATA FOUND", "USERNAME OR PASSWORD IS WRONG", parent = top)

    btnLogin = tk.Button(top,command = login)
    btnLogin.place(relx=0.0, rely=0.644, height=120, width=683)
    btnLogin.configure(activeforeground="#09a8d8")
    btnLogin.configure(background="#09a8d8")
    btnLogin.configure(text='''LOGIN''')
    btnLogin.configure(width=86)
    btnLogin.configure(font = font9)

    btnRegister = tk.Button(top)
    btnRegister.configure(command=Registration)
    btnRegister.place(relx=0.5, rely=0.644, height=120, width=683)
    btnRegister.configure(background="#09a8d8")
    btnRegister.configure(text='''REGISTER''')
    btnRegister.configure(font = font9)
    btnRegister.configure(width=98)

    btnExit = tk.Button(top, command=top.destroy)
    btnExit.place(relx=0, rely=0.8, height=150, width=1366)
    btnExit.configure(background="#09a8d8")
    btnExit.configure(text='''EXIT''')
    btnExit.configure(font = font9)
    btnExit.configure(width=75)

    top.mainloop()

if __name__ == '__main__':
    Login()