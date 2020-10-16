# sec_scrape.py
# Description: scrapes SEC filing data from the SEC website
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
    df.close()


def add_file_to_sec_fsds(url):
    path = Path(__file__).parent.absolute().parent
    df = pd.read_csv(path / "data" / "sec_fsds.csv", sep=",", encoding="utf-8")
    new_data = df.append(
        pd.DataFrame([[url[66:72] + ".zip", False, False, False, False, False, False]], columns=df.columns)
    )
    new_data.to_csv(path / "data" / "sec_fsds.csv", index=False)
    df.close()


def check_sec_menu(url):
    while True:
        print(
            "Would you like to check if the SEC has published Filing Data for "
            + url[66:72]
            + "?"
        )
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
    sec_fsds_data.close()
    company_list = pd.read_csv(
        path / "data" / "company_list.csv",
        dtype={
            "Company ID": np.int16,
            "Company Name": str,
            "Stock Code": str,
            "ALT_Company_Name": str,
        },
    )
    company_list()
    for row in sec_fsds_data:
        for item in row:
            if item == True:
                print("True")
            else:
                print("False")
    print(sec_fsds_array[0:, :1])
    if process_new_data == True:
        # Process num.txt
        num_txt = pd.read_csv(
            path / "data" / "sec_data_temp"/(url[66:72]/"num.txt"),
            sep="\t",
            dtype={
                "adsh":str,
                "tag":str,
                "version":str,
                "coreg":str,
                "ddate":np.int32,
                "qtrs":np.int8,
                "uom":str,
                "value":np.int32,
                "footnote":str
                }
            )
        # Process pre.txt
        pre_txt = pd.read_csv(
            path / "data" / "sec_data_temp"/(url[66:72]/"pre.txt"),
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
        # Process sub.txt
        sub_txt = pd.read_csv(
            path / "data" / "sec_data_temp"/(url[66:72]/"sub.txt"),
            sep="\t",
            dtype={
                "adsh":str,
                "cik":np.int16,
                "name":str,
                "sic":np.int16,
                "countryba":str,
                "stprba":str,
                "cityba":str,
                "zipba":np.int32,
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
                "changed":np.int32,
                "afs":str,
                "wksi":np.int8
                "fye":np.int16,
                "form":str,
                "period":np.int32,
                "fy":np.int16,
                "fp":str,
                "filed":np.int32
                "accepted":str,
                "prevrpt":np.int8,
                "detail":np.int8,
                "instance":str,
                "nciks":np.int8,
                "aciks":str
                }
            )
        # Process tag.txt
        tag_txt = pd.read_csv(
            path / "data" / "sec_data_temp"/(url[66:72]/"tag.txt"),
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
