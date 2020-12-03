import Client
import Employee
import Inventory
import Product
import Transaction

class Main:
    
    def __init__(self):
        self.client = Client()
        self.employee = Employee()
        self.inventory = Inventory()
        self.product = Product()
        self.transaction = Transaction()
        #self.calender = Calender()
        
        self.status = 0
        self.admin = 0
        self.employeelog = ""
        
    def login(self, code):
        if code == "BR%CKPoNBR%CK":
            self.admin = 1
            return True
        return False
            
    def securityLogin(self, code):
        if code == "S@veM3plZ":
            self.admin = 1
            return True
        return False
            
    def employeeLogin(self, ID):
        if ID in self.employee.dictEmployee().keys():
            self.status = 1
            self.employeelog = ID
            return True
        return False
            
    def createClient(self, name, neck, arm, bust, waist, hip, thigh, knee, calf, ankle, shoulder, wrist, outseam, back, sleeve, inseam):
        self.client.createClient(name, neck, arm, bust, waist, hip, thigh, knee, calf, ankle, shoulder, wrist, outseam, back, sleeve, inseam)
        
    def modClient(self, clientNumber, query, data):
        self.client.modClient(clientNumber, query, data)
        
    def deleteClient(self, clientNumber):
        self.client.deleteClient(clientNumber)
        
    def clientData(self, clientNumber):
        return self.client.callClientdata()
    
    def dictClient(self):
        self.client.dictClient()
        
    def createEmployee(self, name, dob, age, startDate):
        self.employee.createEmployee(name, dob, age, startDate)
        
    def modEmployee(self, ID, query, data):
        self.employee.modEmployee(ID, query, data)
        
    def deleteEmployee(self, ID):
        self.employee.deleteEmployee(ID)
        
    def dictEmployee(self):
        return self.employee.dictEmployee()
    
    def enterNewCloth(self, material, quantity):
        self.inventory.enterCloth(material, quantity)
    
    #ONLY ADDITIVE AND SUBTRACTIVE PROCESSES
    def updateInventory(self, material, quantity):
        self.inventory.modCloth(material, quantity)
    
    def deleteCloth(self, material):
        self.inventory.deleteCloth(material)
        
    def lowOnCloth(self):
        return self.inventory.lowOnCloth()
    
    def dictInventory(self):
        return self.inventory.dictInventory()
    
    #size_type = "Fitted" | "Mid" | "Loose"
    #choice_clothing ranges from 0-15
    def makeProduct(self, clientNumber, size_type, choice_clothing):
        return self.product.makeProduct(self.client.callClientData(clientNumber), size_type, choice_clothing)

    def makeTransaction(self, clientNumber, choice_clothing, quantity, tom, dot):
        self.transaction.makeTransaction(clientNumber, self.employeelog, choice_clothing, quantity, tom, dot)
        
    def deletTransaction(self, invoice):
        self.transaction.deleteTransaction(invoice)
    
    