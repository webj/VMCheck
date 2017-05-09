import unittest
from VMChecker import VMChecker

class Test_vmtest(unittest.TestCase):
    
    def test_loadData(self):
        comparedict = {'e1c8a44d-31f0-408c-92bd-4044f7bec080': {'Verfuegbarkeit': '100', 'CU': 'becloud.1CU', 'Commision Date': '2017-03-23T07:32:56Z', 'Server': 'mighty-turkey-18.cloud.kb-bedag.ch', 'Applikation': 'JGK Infrastruktur Management', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'JGK-ABA-C-ADM-P-001', 'Mandant': 'KAIO', 'Umgebung': 'Prod', 'ID': 'e1c8a44d-31f0-408c-92bd-4044f7bec080', 'Typ': 'Windows', 'Lock': True, 'AP Storage': '50GB'}, '5e96ccee-3098-4e29-9c34-f407ff4abac8': {'Verfuegbarkeit': '100', 'CU': 'becloud.2CU', 'Commision Date': '2016-11-28T12:48:59Z', 'Server': 'evil-stingray-38.cloud.kb-bedag.ch', 'Applikation': 'BE-Print EveryonePrint', 'Backup GVS inkl KR': '50GB', 'DisplayName': 'KAIO-BEPRINT-EOP-C-001', 'Mandant': 'KAIO', 'Umgebung': 'Prod', 'ID': '5e96ccee-3098-4e29-9c34-f407ff4abac8', 'Typ': 'Windows', 'Lock': True, 'AP Storage': '50GB'}}        
        mychecker = VMChecker()                        
        testdict = mychecker.loadData('mock_data.txt')
        self.assertEqual(comparedict, testdict)
        

if __name__ == '__main__':
    unittest.main()
