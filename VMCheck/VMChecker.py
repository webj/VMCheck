import csv
import sys
import datetime
import itertools
from itertools import chain

class VMChecker():
        
    __debug = False

    def __init__(self):
        pass
        
    def run(self):    
        self.printLog("\nStart VMCheck: %s" %datetime.datetime.now())
        oldmonth = self.loadData('mock_maerz17.txt')                
        print(len(oldmonth))
        newmonth = self.loadData('mock_april17.txt')        
        if self.changes(oldmonth, newmonth):            
            self.newVMs(oldmonth, newmonth)          
            self.missingLockedVMs(oldmonth, newmonth)      
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
            key = row[headerrow.index('ID')]            
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
        newVMs = {}        
        for key in newmonth:
            if not key in oldmonth:
               self.printLog("NEW VM: %s" %key)
               newVMs[key] = newmonth[key]
        return newVMs
    
    #Checks if there were some VMs deleted. Adds to newmonth the locked VMs from previous month
    def missingLockedVMs(self, oldmonth, newmonth):
        missingVMs = {}        
        for key in oldmonth:
            if not key in newmonth:
                if oldmonth[key]["Lock"]:
                    self.printLog("ADD deleted VM: %s, since it is still locked." %key)
                    newmonth[key] = oldmonth[key]
                else:
                    self.printLog("NOT ADDED: VM deleted (unlocked): %s" %key)

    #checks differences in shared keys, needs two dicts of dicts.        
    def changingParameters(self, oldmonth, newmonth):        
        sharedKeys = set(oldmonth.keys()).intersection(newmonth.keys())
        for key in sharedKeys:                        
            if oldmonth[key]["Lock"] and not oldmonth[key] == newmonth[key]:                               
                self.compare(oldmonth[key], newmonth[key])
    
    #Compares two dicts, to check wether two values are the same or not. If so, take the higher (if VM is still locked) otherwise take the newer.
    #return updatet second dict
    def compare(self, first, second):        
        sharedKeys = set(first.keys()).intersection(second.keys())
        for key in sharedKeys:
            if first[key] != second[key]:            
                self.printLog('Value Changed => Server: {}, Column: {}, Value Old: {}, Value New: {}'.format(first['ID'], key, first[key], second[key]))
                if first[key] > second[key]:
                    second[key] = first[key]
                    self.printLog('Move to previous month: ID %s' %second['ID'])
        return second
    
    #Adds/Update dict entry lock date => key=Lock value=True/False
    def addLockDate(self, mydict):
        mydate = str(mydict['Commision Date'])[:10]
        mydatetime = datetime.datetime.strptime(mydate, '%Y-%m-%d')
        mydict['Lock'] =  mydatetime > (datetime.datetime.now() - datetime.timedelta(days=365))
    
    #creates CSV for the new month
    def createCSV(self, datadict):
        with open('test.csv', 'w', newline='') as f:
            first= True
            w = csv.writer(f, delimiter=';')             
            for key in datadict.keys():
                if first:
                    w.writerow(datadict[key].keys())
                    first = False
                w.writerow(datadict[key].values())
    
    #Prints information into logfile
    def printLog(self, text):
        print(text, file=open('log.txt', 'a'))

def main():   
    vmchecker = VMChecker()
    vmchecker.run()

if __name__ == '__main__':
    main()