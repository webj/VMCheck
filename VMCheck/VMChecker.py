import csv
import sys
import datetime
import itertools

class VMChecker():
        
    __debug = False

    def __init__(self):
        pass
        
    def run(self):    
        self.printLog("\nStart VMCheck: %s" %datetime.datetime.now())
        oldmonth = self.loadData('becloud_maerz17.txt')
        newmonth = self.loadData('becloud_april17.txt')        
        if self.changes(oldmonth, newmonth):
            self.printLog("Yeeha, there were some changes!!!")            
            self.newVMs(oldmonth, newmonth)
            print(len(newmonth))
            self.missingVMs(oldmonth, newmonth)
            print(len(newmonth))
            self.changingParameters(oldmonth, newmonth)                        
            self.createCSV(newmonth)
        else:
            self.printLog("There were no changes since last month.") 
            self.createCSV(newmonth)        
        
    #load csv
    def loadData(self, datafile):
        csvreader = csv.reader(open(datafile), delimiter='\t')        
        mydict = {}       
        headerrow = next(csvreader, None)                       
        for row in csvreader:
            key = row[3]            
            if key in mydict:
                if self.__debug:
                    self.printLog("Server %s is already in, check double value in csv." % key)
                sys.exit
            else:
                if self.__debug:
                    self.printLog("Add Server %s to Dict" % key)
                mydict[key] = dict(zip(headerrow, row))   
                self.addLockDate(mydict[key])                                     
        return mydict       

    def changes(self, oldmonth, newmonth):
        return oldmonth != newmonth
       
    #checks if there are new VM's in town
    def newVMs(self, oldmonth, newmonth):        
        for key in newmonth:
            if not key in oldmonth:
               self.printLog("New VM: %s" %key)               
    
    #Checks if there are some VM' were deleted
    def missingVMs(self, oldmonth, newmonth):        
        for key in oldmonth:
            if not key in newmonth:
                if oldmonth[key]["Lock"]:
                    self.printLog("Add deleted VM: %s, since it is still locked." %key)
                    newmonth[key] = oldmonth[key]
                else:
                    self.printLog("VM deleted (unlocked): %s" %key)
            
    
    def changingParameters(self, oldmonth, newmonth):        
        for key in oldmonth:                        
            if oldmonth[key]["Lock"] and not oldmonth[key] == newmonth[key]:                               
                self.compare(oldmonth[key], newmonth[key])

    def compare(self, first, second):        
        sharedKeys = set(first.keys()).intersection(second.keys())
        for key in sharedKeys:
            if first[key] != second[key]:            
                self.printLog('Value Changed => Server: {}, Column: {}, Value Old: {}, Value New: {}'.format(first['ID'], key, first[key], second[key]))
                if first[key] > second[key] and second['Lock']:
                    second[key] = first[key]
                    self.printLog('Decreasment due lock not allowed: ID %s' %second['ID'])

    def addLockDate(self, mydict):
        mydate = str(mydict['Commision Date'])[:10]
        mydatetime = datetime.datetime.strptime(mydate, '%Y-%m-%d')
        mydict['Lock'] =  mydatetime > (datetime.datetime.now() - datetime.timedelta(days=365))
    
    def createCSV(self, datadict):
        with open('test.csv', 'w', newline='') as f:
            first= True
            w = csv.writer(f, delimiter=';')             
            for key in datadict.keys():
                if first:
                    w.writerow(datadict[key].keys())
                    first = False
                w.writerow(datadict[key].values())

    def printLog(self, text):
        print(text, file=open('log.txt', 'a'))

def main():   
    vmchecker = VMChecker()
    vmchecker.run()
         

if __name__ == '__main__':
    main()