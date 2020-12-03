import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import os

class Client:
    
    def __init__(self):
       self.init_db()
        

    def init_db(self):
        if os.path.exists("ClientDB.xlsx"):
            self.db = pd.read_excel("ClientDB.xlsx")
        else:
            df = pd.DataFrame({"Client Number":[], "Name":[], "Neck":[], \
                                    "Upper Arm":[], "Bust":[], "Waist":[], "Hip":[], \
                                    "Thigh":[], "Knee":[], "Calf":[], "Ankle":[], "Shoulder Width":[], \
                                    "Wrist":[], "Outseam":[], "Back Length":[], "Sleeve length":[], "Inseam":[] })
            
            self.db = pd.ExcelWriter("ClientDB.xlsx", engine="xlsxwriter")
            
            df.to_excel(self.db, index=False)
            self.db.save()
            self.db = pd.read_excel("ClientDB.xlsx")
            
    
    def autoSave(self):
        temp = pd.ExcelWriter("ClientDB.xlsx", engine="xlsxwriter")
        self.db.to_excel(temp, index=False)
        temp.save()
        self.db = pd.read_excel("ClientDB.xlsx")
            
    def createClient(self, name, neck, arm, bust, waist, hip, thigh, knee, calf, ankle, shoulder, wrist, outseam, back, sleeve, inseam):
        
        if self.db["Client Number"].max() != self.db["Client Number"].max():
            new = pd.DataFrame({"Client Number":["CRN0001"], "Name":[name], "Neck":[neck], \
                                "Upper Arm":[arm], "Bust":[bust], "Waist":[waist], "Hip":[hip], "Thigh":[thigh], \
                                "Knee":[knee], "Calf":[calf], "Ankle":[ankle], "Shoulder Width":[shoulder], "Wrist":[wrist],\
                                "Outseam":[outseam], "Back Length":[back], "Sleeve length":[sleeve], "Inseam":[inseam] })
        else:
            temp_num = int(self.db["Client Number"].max()[3:])
            temp_word = ""
            
            if len(self.db["Client Number"]) >= 999:
                temp_word = "CRN"
            elif len(self.db["Client Number"]) >= 99:
                temp_word = "CRN0"
            elif len(self.db["Client Number"]) >= 9:
                temp_word = "CRN00"
            else:
                temp_word = "CRN000"
            new = pd.DataFrame({"Client Number":[temp_word+str(temp_num+1)], "Name":[name], "Neck":[neck], \
                                "Upper Arm":[arm], "Bust":[bust], "Waist":[waist], "Hip":[hip], "Thigh":[thigh], \
                                "Knee":[knee], "Calf":[calf], "Ankle":[ankle], "Shoulder Width":[shoulder], "Wrist":[wrist],\
                                "Outseam":[outseam], "Back Length":[back], "Sleeve length":[sleeve], "Inseam":[inseam] })
    
        self.db = self.db.append(new, ignore_index=True)  
        self.autoSave()
        
    def modClient(self, clientNumber, query, data):
        for m in range(len(self.db["Client Number"])):
            if self.db["Client Number"][m] == clientNumber:
                self.db[query][m] = data
                self.autoSave()
                break
    
    def deleteClient(self, clientNumber):
        for m in range(len(self.db["Client Number"])):
            if self.db["Client Number"][m] == clientNumber:
                self.db = self.db.drop(m, axis=0)
                self.autoSave()
                break
    
    def callClientData(self, clientNumber):
        for m in range(len(self.db["Client Number"])):
            if self.db["Client Number"][m] == clientNumber:
                return [self.db["Name"][m], self.db["Neck"][m], self.db["Upper Arm"][m], self.db["Bust"][m], self.db["Waist"][m],\
                        self.db["Hip"][m], self.db["Thigh"][m], self.db["Knee"][m], self.db["Calf"][m], self.db["Ankle"][m],\
                        self.db["Shoulder Width"][m], self.db["Wrist"][m], self.db["Outseam"][m],\
                        self.db["Back Length"][m], self.db["Sleeve length"][m], self.db["Inseam"][m]]
    
    def dictClient(self):
        return self.db.to_dict()
