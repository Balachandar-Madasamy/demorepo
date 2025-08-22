import pandas as pd
import json
import re


def extract2table(out):
    if isinstance(out,str):
        try:
            print('Here is original str',out)

            match = re.search(r"\{.*\}", out, re.DOTALL)
            clean = match.group(0)
            dct = json.loads(clean)
            print(dct)

        except Exception as e:
            print('Exception error : ',e)



    return pd.DataFrame(dct.items(), columns=["Fields", "Value"])