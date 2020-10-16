# sec_scrape.py
# Description: scrapes SEC filing data from the SEC website and processes
# Authors: Anthony Stone
#          Alexander Talbott
#          Jim Wang


import requests
import pandas as pd
import eq_utilities
import zipfile
import os
import numpy as np
from pathlib import Path

# Open sec_fsds.csv and verify which files have been downloaded


def get_next_sec_fsds():
    path = Path(__file__).parent.absolute().parent
    df = pd.read_csv(path / "data" / "sec_fsds.csv")
    for x in df["downloaded_data_distribution"]:
        most_recent_sec_fsds = x
    if int(most_recent_sec_fsds[5:6]) == 4:
        get_file_url = (
            "https://www.sec.gov/files/dera/data/financial-statement-data-sets/"
            + str(int(most_recent_sec_fsds[0:4]) + 1)
            + "q1.zip"
        )
    else:
        get_file_url = (
            "https://www.sec.gov/files/dera/data/financial-statement-data-sets/"
            + most_recent_sec_fsds[0:4]
            + "q"
            + str(int(most_recent_sec_fsds[5:6]) + 1)
            + ".zip"
        )
    return get_file_url



def add_file_to_sec_fsds(url):
    path = Path(__file__).parent.absolute().parent
    df = pd.read_csv(path / "data" / "sec_fsds.csv", sep=",", encoding="utf-8")
    new_data = df.append(
        pd.DataFrame([[url[66:72] + ".zip", False, False, False, False, False, False]], columns=df.columns)
    )
    new_data.to_csv(path / "data" / "sec_fsds.csv", index=False)

def check_sec_menu(url):
    while True:
        print(
            "Would you like to check if the SEC has published Filing Data for "
            + url[66:72]
            + "?"
        )
        print("You will need a minimum of 500MB of diskspace to process!")
        print("Y/N")
        response = input()
        try:
            response = str(response)
        except:
            eq_utilities.screen_clear()
            print("Not a valid response. Try again!")
            continue
        if response != "Y" and response != "N":
            eq_utilities.screen_clear()
            print("Not a valid response. Try again!")
            continue
        if response == "Y":
            eq_utilities.screen_clear()
            if check_new_sec_exist(url) == True:
                print("The SEC has published " + url[66:72] + "!")
                will_download_file = True
            else:
                print("There is no file")
                will_download_file = False
            break
        else:
            will_download_file = False
            eq_utilities.screen_clear()
            break
    del response
    return will_download_file


def check_new_sec_exist(url):
    req = requests.get(url)
    if req.status_code == 200:
        file_found = True
    else:
        file_found = False
    return file_found


def download_new_sec_file(url):
    print(
        "Downloading "
        + url[66:72]
        + ".zip from the SEC. This may take several minutes..."
    )
    req = requests.get(url, stream=True)
    path = Path(__file__).parent.absolute().parent
    data_loc = open(path / "data" / "sec_data_temp/" / (url[66:72] + ".zip"), "wb")
    for chunk in req.iter_content(chunk_size=512):
        if chunk:
            data_loc.write(chunk)
    data_loc.close()
    print("The latest package has been downloaded!")


def process_data_file(process_new_data, url):
    path = Path(__file__).parent.absolute().parent
    #Read sec_fsds_data, so we can determine which files have been processed
    #and control flow
    sec_fsds_data = pd.read_csv(
        path / "data" / "sec_fsds.csv",
        dtype={
            "downloaded_data_distribution": str,
            "num_proc": np.bool_,
            "pre_proc": np.bool_,
            "sub_proc": np.bool_,
            "tag_proc": np.bool_,
            "final_proc": np.bool_,
            "flag": np.bool_,
        },
    )
    sec_fsds_array = np.array(sec_fsds_data)
    url= sec_fsds_array[-1,0][0:6]
    print(url)
    
    #Read company_list, so we can determine which companies are needed from SEC
    company_list_data = pd.read_csv(
        path / "data" / "company_list.csv",
        dtype={
            "Company ID": np.int16,
            "Company Name": str,
            "Stock Code": str,
            "ALT_Company_Name": str
        }
    )
    #Create list of our companies
    sec_company_list = company_list_data["ALT_Company_Name"].unique()
    #remove nulls
    sec_company_list = sec_company_list[~pd.isna(sec_company_list)]
    print(sec_company_list[0:10])
    
    
    for row in sec_fsds_data:
        for item in row:
            if item == True:
                #print("True")
                x=1
            else:
                x=2
                #print("False")
    #print(sec_fsds_array[0:, :1])
    process_new_data =True
    if process_new_data == True:
        """
        Process SUB.TXT Data
        This files must be processes first due to size and since it is the only
        file that will relate back to the COMPANY_LIST.CSV.
        """
        print("processing SUB.TXT")
        sub_txt = pd.read_csv(
            path / "data" / "sec_data_temp"/url/"sub.txt",
            sep="\t",
            dtype={
                "adsh":str,
                "cik":np.int16,
                "name":str, #FK to COMANY_LIST.CSV
                "sic":np.single,
                "countryba":str,
                "stprba":str,
                "cityba":str,
                "zipba":str,
                "bas1":str,
                "bas2":str,
                "baph":str,
                "countryma":str,
                "stprma":str,
                "cityma":str,
                "zipma":str,
                "mas1":str,
                "mas2":str,
                "countryinc":str,
                "stprinc":str,
                "ein":np.int32,
                "former":str,
                "changed":np.double,
                "afs":str,
                "wksi":np.single,
                "fye":np.double,
                "form":str,
                "period":np.double,
                "fy":np.double,
                "fp":str,
                "filed":np.int32,
                "accepted":str,
                "prevrpt":np.int8,
                "detail":np.int8,
                "instance":str,
                "nciks":np.int8,
                "aciks":str
                }
            )
        #Get all records in sub_txt where name is in company_list
        sub_txt_comp_name = sub_txt[sub_txt["name"].isin(sec_company_list)]
        #create list of all adsh value used, in order to reduce other tables
        adsh_list = list(sub_txt_comp_name["adsh"])

        # Process num.txt
        print("Processing NUM.TXT")
        num_txt = pd.read_csv(
            path / "data" / "sec_data_temp"/url/"num.txt",
            sep="\t",
            dtype={
                "adsh":str,
                "tag":str,
                "version":str,
                "coreg":str,
                "ddate":np.double,
                "qtrs":np.int8,
                "uom":str,
                "value":np.double,
                "footnote":str
                }
            )
        #Get all records in num_txt where adsh is in adsh_list
        num_txt_adsh_match = num_txt[num_txt["adsh"].isin(adsh_list)]
        tag_list_num = list(num_txt_adsh_match["tag"])
        # Process pre.txt
        print("Processing PRE.TXT")
        pre_txt = pd.read_csv(
            path / "data" / "sec_data_temp"/url/"pre.txt",
            sep="\t",
            dtype={
                "adsh":str,
                "report":np.int8,
                "line":np.int16,
                "stmt":str,
                "inpth":np.int8,
                "rfile":str,
                "tag":str,
                "version":str,
                "plabel":str,
                "negating":np.int8                
                }
            )
        
        #Get all records in pre_txt where adsh is in adsh_list
        pre_txt_adsh_match = pre_txt[pre_txt["adsh"].isin(adsh_list)]
        tag_list_pre = list(pre_txt_adsh_match["tag"])
        # Process tag.txt
        print("Processing TAG.TXT")
        tag_txt = pd.read_csv(
            path / "data" / "sec_data_temp"/url/"tag.txt",
            sep="\t",
            dtype={
                "tag": str,
                "version":str,
                "custom":np.int16,
                "abstract":np.int16,
                "datatype":str,
                "iord":str,
                "crdr":str,
                "tlabel":str,
                "doc":str
            }
            )
        tag_num_match = tag_txt[tag_txt["tag"].isin(tag_list_num)]
        tag_pre_match = tag_txt[tag_txt["tag"].isin(tag_list_pre)]
        #merge data
        print("...")
        pre_merge_tag = pre_txt_adsh_match.merge(tag_pre_match, on = "tag")
        pre_merge_tag.drop_duplicates()
        print("...")
        num_merge_tag = num_txt_adsh_match.merge(tag_num_match, on = "tag")
        num_merge_tag.drop_duplicates()
        print("...")
        num_merge_pre = pre_merge_tag.merge(num_merge_tag, on = "adsh")
        num_merge_pre.drop_duplicates()
        print("...")
        sec_merge_data = sub_txt_comp_name.merge(num_merge_pre, left_on = "adsh")
        print("...")
        sec_merge_data.drop_duplicates()
        print("...")
        sec_merge_data.to_csv(path / "data" / "SEC_data_table.csv")

        """
        #remove zip file
        os.remove("../data/sec_data_temp/"
        + url[66:72]
        + ".zip")
        """
    else:
        pass


def update_data():
    path = Path(__file__).parent.absolute().parent
    # Check to see what file needs to be downloaded next from SEC
    next_sec_url = str(get_next_sec_fsds())
    # Go to function and see if url exist to get new SEC data package
    if check_sec_menu(next_sec_url) == True:
        # download new package with function and unpack
        download_new_sec_file(next_sec_url)
        with zipfile.ZipFile(
            path / "data" / "sec_data_temp/" / (next_sec_url[66:72] + ".zip"), "r",
        ) as zip_ref:
            zip_ref.extractall(path / "data" / "sec_data_temp/" / next_sec_url[66:72])
        add_file_to_sec_fsds(next_sec_url)
        check_new_file = True
        print("Processing lastest SEC data package...")
    else:
        print("SEC will not be checked for new data")
        check_new_file = False
    print("Verifying data integrity")
    process_data_file(check_new_file, next_sec_url)


"""
TESTING
"""
if __name__ == "__main__":
    update_data()
