import pandas as pd
import os

class Inventory:
    
    def __init__(self):
        self.init_db()
        
    def init_db(self):
        if os.path.exists("InventoryDB.xlsx"):
            self.db = pd.read_excel("InventoryDB.xlsx")
        else:    
            df = pd.DataFrame({"Minimum":[50]}) # Minimum value of cloth that should be inventory
            self.db = pd.ExcelWriter("InventoryDB.xlsx", engine="xlsxwriter")
            df.to_excel(self.db, index=False)
            self.db.save()
            self.db = pd.read_excel("InventoryDB.xlsx")
            
    def autoSave(self):
        temp = pd.ExcelWriter("InventoryDB.xlsx", engine="xlsxwriter")
        self.db.to_excel(temp, index=False)
        temp.save()
        self.db = pd.read_excel("InventoryDB.xlsx")
        
    def modMinimum(self, quantity):
        self.enterCloth("Minimum", quantity) 
        self.autoSave()
        
        
    def enterCloth(self, material, quantity):
        self.db[material] = quantity
        self.autoSave()
        
    # ONLY SUPPOSE TO BE USED FOR ADDITIVE OR SUBTRACTIVE PROCESSES
    def modCloth(self, material, quantity):
        self.db[material] = self.db[material][0] + quantity
        self.autoSave()
        
    def deleteCloth(self, material):
        self.db = self.db.drop(material, axis=1)
        self.autoSave()
        
    def lowOnCloth(self):
        if len(self.db.columns) == 0:
            return {}
        else:
            data = {}
            for m in self.db.columns:
                if self.db[m][0] < self.db["Minimum"][0]:
                    data[m]= self.db[m][0]
            return data
        
    def dictInventory(self):
        return self.db.to_dict()