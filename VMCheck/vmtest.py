import unittest
from VMChecker import VMChecker

class Test_vmtest(unittest.TestCase):
    
    #Isolated tests
    def test_loadDats(self):
        comparedict = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': 50, 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': 50, 'CU': 1, 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': 50, 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': 50, 'CU': 2, 'Mandant': 'Testit'}}
        mychecker = VMChecker()                        
        self.assertDictEqual(comparedict, mychecker.loadData('mock_data.txt'))

    def test_newVMs(self):
        oldvms = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.2CU', 'Mandant': 'Testit'}}
        newvms = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.2CU', 'Mandant': 'Testit'}, 'abcd1347': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}}
        diff = {'abcd1347': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}}
        mychecker = VMChecker()
        self.assertDictEqual(diff, mychecker.newVMs(oldvms, newvms))        

    def test_missinglockedVMs(self):
        newvms = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.2CU', 'Mandant': 'Testit'}}
        oldvms = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.2CU', 'Mandant': 'Testit'}, 'abcd1347': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}}
        diff = oldvms.copy()
        mychecker = VMChecker()
        mychecker.missingLockedVMs(oldvms, newvms)
        self.assertDictEqual(diff, oldvms)

    def test_missingunlockedVMs(self):
        oldvms = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.2CU', 'Mandant': 'Testit'}, 'abcd1347': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '201-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': False, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}}
        newvms = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.2CU', 'Mandant': 'Testit'}}        
        diff = newvms.copy()
        mychecker = VMChecker()
        mychecker.missingLockedVMs(oldvms, newvms)
        self.assertEqual(diff, newvms)

    def test_changingParametersLockedReduce(self):        
        oldvms = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '60GB', 'CU': 'cloud.2CU', 'Mandant': 'Testit'}}
        newvms = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.2CU', 'Mandant': 'Testit'}, 'abcd1347': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}}        
        diff = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '60GB', 'CU': 'cloud.2CU', 'Mandant': 'Testit'}, 'abcd1347': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': '50GB', 'CU': 'cloud.1CU', 'Mandant': 'Testit'}}        
        mychecker = VMChecker()
        mychecker.changingParameters(oldvms, newvms)
        self.assertDictEqual(diff, newvms)

    def test_compareNewValueNewMonth(self):
        first = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '100GB', 'Backup': '200GB'}
        second = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '150GB', 'Backup': '200GB'}
        diff = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '150GB', 'Backup': '200GB'}
        mychecker = VMChecker()        
        mychecker.compare(first, second)
        self.assertDictEqual(diff, second)

    def test_compareNewValueOldMonth(self):
        first = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '150GB', 'Backup': '200GB'}
        second = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '100GB', 'Backup': '200GB'}
        diff = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '150GB', 'Backup': '200GB'}
        mychecker = VMChecker()        
        mychecker.compare(first, second)
        self.assertDictEqual(diff, second)

    def test_compareNewValueOldMonthandNewMonth(self):
        first = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '150GB', 'Backup': '200GB'}
        second = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '170GB', 'Backup': '200GB'}
        diff = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '170GB', 'Backup': '200GB'}
        mychecker = VMChecker()        
        mychecker.compare(first, second)
        self.assertDictEqual(diff, second)

    def test_compareTwoNewValueOldMonth(self):
        first = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '170GB', 'Backup': '250GB'}
        second = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '150GB', 'Backup': '200GB'}
        diff = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'Disk': '170GB', 'Backup': '250GB'}
        mychecker = VMChecker()        
        mychecker.compare(first, second)
        self.assertDictEqual(diff, second)
    
    def test_smoothValues(self):
            mydict = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'AP Storage': '170GB', 'Backup GVS inkl KR': '250GB', 'CU': 'cloud.1CU'}
            diff = {'ID': 'abcdefg100', 'Server' : 'foobar', 'Typ' : 'Windows', 'AP Storage': 170, 'Backup GVS inkl KR': 250, 'CU': 1}
            mychecker = VMChecker()  
            mychecker.smoothValues(mydict)            
            self.assertDictEqual(diff, mydict)
    
    #combined tests
    def test_loadDataAndProceed(self):
        mychecker = VMChecker()
        oldmonth = mychecker.loadData('mock_data.txt')
        newmonth = mychecker.loadData('mock_data2.txt')
        mychecker.newVMs(oldmonth, newmonth)          
        mychecker.missingLockedVMs(oldmonth, newmonth)      
        mychecker.changingParameters(oldmonth, newmonth)
        diff = comparedict = {'abcd1346': {'Verfuegbarkeit': '100', 'ID': 'abcd1346', 'Server': 'mighty-turkey-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-03-23T07:32:56Z', 'Applikation': 'APP B', 'Backup GVS inkl KR': 50, 'DisplayName': 'Niceview b', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': 50, 'CU': 1, 'Mandant': 'Testit'}, 'abcd1345': {'Verfuegbarkeit': '100', 'ID': 'abcd1345', 'Server': 'evil-stingray-38.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2016-11-28T12:48:59Z', 'Applikation': 'APP A', 'Backup GVS inkl KR': 50, 'DisplayName': 'Niceview a', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': 50, 'CU': 2, 'Mandant': 'Testit'}, 'abcd1347': {'Verfuegbarkeit': '100', 'ID': 'abcd1347', 'Server': 'mighty-mother-18.cloud.test.ch', 'Typ': 'Windows', 'Commision Date': '2017-01-23T07:32:56Z', 'Applikation': 'APP C', 'Backup GVS inkl KR': 6000, 'DisplayName': 'Niceview c', 'Umgebung': 'Prod', 'Lock': True, 'AP Storage': 100, 'CU': 4, 'Mandant': 'Testit'}}
        self.assertDictEqual(diff, newmonth)

if __name__ == '__main__':
    unittest.main()