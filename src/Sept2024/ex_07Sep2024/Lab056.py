class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")


class TC1: # no need to inherit since it's static methods
    def runTC(self):
        ExcelReader.readExcelFile() # ClassName.method_name,  not inherited so no need to use super()
        MYSQLDBConnection.readMySQLFile() # ClassName.method_name,  not inherited so no need to use super()


tc1 = TC1()
tc1.runTC()