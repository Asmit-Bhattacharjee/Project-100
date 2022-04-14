class Atm:
    def __init__(self, pinNumber, cardNumber, balance, bankName, cardHolderName):
        self.pinNumber = pinNumber
        self.cardNumber = cardNumber
        self.balance = balance
        self.bankName = bankName
        self.cardHolderName = cardHolderName

    def cashDeposit(self, amountDeposited):
        balance = self.balance
        newBalance = balance+amountDeposited
        print("Your new balance is :", newBalance)

    def cashWithdrawal(self, amountWithdrawal):
        balance = self.balance
        newBalance = balance-amountWithdrawal
        print("Your new balance is :", newBalance)

    def balanceEnquiry(self):
        print(self.balance)

customer1 = Atm("1234", "8302973932777382", 10000, "StandardChartered", "Asmit")
customer1.cashWithdrawal(1500)