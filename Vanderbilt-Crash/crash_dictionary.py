import pandas as pd

class CrashDict:
    def __init__(self, dict_csv):
        self.df = pd.read_csv(dict_csv)
        self.df.set_index('Name', inplace=True)
        # print(self.df)
    
    def _prep_var_name(self, var_names) -> list:
        if isinstance(var_names, list):
            # print(f"var_names is {type(var_names)}")
            for v in var_names:
                if isinstance(v,str) == False:
                    raise ValueError(f"'var_names' is an unexpected type: {type(var_names)}")
            return var_names
        elif isinstance(var_names, str):
            # print(f"var_names is {type(var_names)}")
            return [var_names]
        else:
            raise ValueError(f"'var_names' is an unexpected type: {type(var_names)}")

    def get_details(self, var_names:str|list[str]) -> pd.DataFrame:
        """return all columns of the data dictionary for a specified variable name or list of names"""
        var_names = self._prep_var_name(var_names)
        return self.df.loc[var_names]

    def get_labels(self, var_names):
        """return the 'Labels' column of the data dictionary for a specified variable name or list of names"""
        var_names = self._prep_var_name(var_names)
        return self.df.loc[var_names,['Labels']]

    def get_df(self):
        """return a DataFrame of the full data dictionary"""
        return self.df


if __name__ == '__main__':
    import os
    print(os.getcwd())
    crash_dict = CrashDict('./Vanderbilt-Crash/data/crash_dictionary.csv')

    print(crash_dict.get_details(['cause']))
    print(crash_dict.get_details('cause'))
    print("--------")
    print(crash_dict.get_labels(['cause']))
    print(crash_dict.get_labels('cause'))


