import argparse

class StressTest:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Optional app description')
        self.parser.add_argument('--generate-leads', dest='generate-leads', action='store_const',
             const=gen, default=1000000, help='Generate the test data')
        self.parser.add_argument('--test-lead-import', dest='test-load-import', action='store_const',
                                 const=test_lead_import, default="leads.txt", help='Generate the test data')

    def importLeads(self):
        lead = mc.execute(
                method='import_lead', 
                file='../folder/test.csv', 
                format='csv', 
                lookupField='email', 
                listId=None, 
                partitionName='Default')

    def main(self):
        args = self.parser.parse_args()


if __name__ == '__main__':
    StressTest().main()

