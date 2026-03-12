import pandas as pd
class ComparableData:
 
    def __init__(self, data: pd.DataFrame):

        self.data = data

    def get_pe(self):

        return self.data["PE"]

    def get_ev_ebitda(self):

        return self.data["EV_EBITDA"]

    def get_ev_sales(self):

        return self.data["EV_Sales"]

    def get_pb(self):

        return self.data["PB"]

    def summary(self):

        return self.data.describe()
