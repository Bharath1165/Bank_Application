class Bank_Form:
    Bank_name = 'union bank'
    IFSC_code = 'UBIN4532'
    Branch_name = 'Tirupati'
    Rate_of_interest = 1.6
    
    def __init__(self,name,mobile,accno,balance,pin):
        self.name = name
        self.mobile = mobile
        self.accno = accno
        self.balance = balance
        self.pin = pin
    
    def check_balance(self):
        if self.validpin() == self.pin :
            print(f'{self.balance} is your balance')
        else:
            print('wrong pin entered')
    
    def Deposit(self):
        if self.validpin() == self.pin :
            self.balance += int(input('enter amount:'))
            print(f'{self.balance} is your amount')
        else:
            print('wrong pin entered')
    
    def Withdraw(self):
        if self.validpin() == self.pin :
            amount = int(input('enter amount :'))
            if self.balance >= amount :
                self.balance -= amount
                print(f'{self.balance} is remaining amount')
            else:
                print('insufficient funds')
        else:
            print('wrong pin entered')
    
    def Change_pin(self):
        if self.validpin() == self.pin :
            pin = int(input('enter new pin :'))
            if pin == self.validpin():
                print(f'{pin} pin is updated')
            else:
                print('Reentered pin is not matched')
        else:
            print('wrong pin entered')
        
    
    @classmethod
    def Change_ROI(cls):
        cls.ROI = float(input('enter ROI :'))
        print(f'This is your rate of interest {cls.ROI}')
        
    @staticmethod
    def validpin():
        return int(input('enter 4 digit pin :'))
        
B1 = Bank_Form('kumar',9640287757,10321053421,10000,1234)
B2 = Bank_Form('Reddy',9347053213,10324232415,30000,5678)
#print(B1.mobile)
B1.check_balance()
#B1.Withdraw()
#B1.Change_pin()
#B1.Change_ROI()

#B2.check_balance()
#B2.Withdraw()
#B2.Change_pin()
#B1.Change_ROI()

#Application is Based on Python and OOP's
