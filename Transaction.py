import pandas as pd
import os
#import time


class Transaction:
    
    rate = 50
    
    def __init__(self):
       self.init_db()
        

    def init_db(self):
        if os.path.exists("TransactionDB.xlsx"):
            self.db = pd.read_excel("TransactionDB.xlsx")
        else:
            df = pd.DataFrame({"Invoice Number":[], "Client Number":[], "Employee ID":[], "product":[], "cost":[], "Terms of payment":[], "Date":[] })
            
            self.db = pd.ExcelWriter("TransactionDB.xlsx", engine="xlsxwriter")
            
            df.to_excel(self.db, index=False)
            self.db.save()
            self.db = pd.read_excel("TransactionDB.xlsx")
            
    
    def autoSave(self):
        temp = pd.ExcelWriter("TransactionDB.xlsx", engine="xlsxwriter")
        self.db.to_excel(temp, index=False)
        temp.save()
        self.db = pd.read_excel("TransactionDB.xlsx")
        
    def makeTransaction(self,clientNumber, ID, choice_clothing, quantity, tom, dot):
        
        if self.db["Invoice Number"].max() != self.db["Invoice Number"].max():
            new = pd.DataFrame({"Invoice Number":[1], "Client Number":[clientNumber], "Employee ID":[ID], "product":[choice_clothing], "cost":[quantity* Transaction.rate], "Terms of payment":[tom], "Date":[dot] })
        else:   
            new = pd.DataFrame({"Invoice Number":[self.db["Invoice Number"].max()+1], "Client Number":[clientNumber], "Employee ID":[ID], "product":[choice_clothing], "cost":[quantity* Transaction.rate], "Terms of payment":[tom], "Date":[dot] })
    
        self.db = self.db.append(new, ignore_index=True)  
        self.autoSave()
        
    def deleteTransaction(self, invoice):
        for m in range(len(self.db["Invoice Number"])):
            if self.db["Invoice Number"][m] == invoice:
                self.db = self.db.drop(m, axis=0)
                self.autoSave()
                break
            
    def dictTransaction(self):
        return self.db.to_dict()