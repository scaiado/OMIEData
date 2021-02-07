import pandas as pd
import os
from .FileReader import FileReader

####################################################################################################################
class Reader:

    ####################################################################################################################
    def __init__(self, absolutePath: str, fileReader: FileReader):
        self.folder = absolutePath
        self.fileReader = fileReader
    ####################################################################################################################

    ####################################################################################################################
    def readToDataFrame(self, verbose=False) -> pd.DataFrame:

        # List all the files in the directory
        filenames = [f for f in os.listdir(self.folder) if os.path.isfile(os.path.join(self.folder, f))]

        reader = self.fileReader
        df = pd.DataFrame(columns=reader.getKeys())
        for f in filenames:
            try:
                for row in reader.dataGenerator(filename=os.path.join(self.folder, f)):
                    # df = df.append(row, ignore_index=True) # This is inefficient
                    df.loc[df.shape[0], :] = row
            except:
                print('There was error processing file: ' + f)
            else:
                if verbose:
                    print('File: ' + f + ' successfully processed')

        return df
    ####################################################################################################################

# End class
####################################################################################################################
