import twitter
import pandas as pd


api = twitter.Api(
    "xjBcMPKQDKtmS9YOxRjDs2v4T",
    "8sK4L0kYM0VT8UecMu8IPZgd54O8d20uaSnFwiAQvcDz0AWVRB",
    "1309554738543943684-jD3glTsDlofSFWX5DPVFSguZsBRaMp",
    "UbHoxvZky0ZcJQwQ0hpb6oIlDu01Dd3IuMslv0nzVmg2A",
)

# TODO
def retrieve_handle_from_ticker(ticker):
    if ticker.upper() == "AAPL":
        handle = "Apple"
    elif ticker.upper() == "ADBE":
        handle = "Adobe"
    elif ticker.upper() == "ADI":
        handle = "ADI_News"
    elif ticker.upper() == "ADSK":
        handle = "autodesk"
    elif ticker.upper() == "AMAT":
        handle = "Applied4Tech"
    elif ticker.upper() == "AMD":
        handle = "AMD"
    elif ticker.upper() == "ANSS":
        handle = "ANSYS"
    elif ticker.upper() == "ASML":
        handle = "ASMLcompany"
    elif ticker.upper() == "AVGO":
        handle = "Broadcom"
    elif ticker.upper() == "BIDU":
        handle = "Baidu_Inc"
    elif ticker.upper() == "CDNS":
        handle = "Cadence"
    elif ticker.upper() == "CDW":
        handle = "CDWCorp"
    elif ticker.upper() == "CERN":
        handle = "Cerner"
    elif ticker.upper() == "CHKP":
        handle = "CheckPointSW"
    elif ticker.upper() == "CSCO":
        handle = "Cisco"
    elif ticker.upper() == "CTSH":
        handle = "Cognizant"
    elif ticker.upper() == "CTXS":
        handle = "citrix"
    elif ticker.upper() == "DOCU":
        handle = "DocuSign"
    elif ticker.upper() == "FB":
        handle = "Facebook"
    elif ticker.upper() == "GOOG":
        handle = "Google"
    elif ticker.upper() == "GOOGL":
        handle = "Google"
    elif ticker.upper() == "INTC":
        handle = "intel"
    elif ticker.upper() == "INTU":
        handle = "Intuit"
    elif ticker.upper() == "KLAC":
        handle = "KLAcorp"
    elif ticker.upper() == "LRCX":
        handle = "LamResearch"
    elif ticker.upper() == "MCHP":
        handle = "MicrochipTech"
    elif ticker.upper() == "MSFT":
        handle = "Microsoft"
    elif ticker.upper() == "MU":
        handle = "MicronTech"
    elif ticker.upper() == "MXIM":
        handle = "maximintegrated"
    elif ticker.upper() == "NTES":
        handle = "NetEase_Global"
    elif ticker.upper() == "NVDA":
        handle = "nvidia"
    elif ticker.upper() == "NXPI":
        handle = "NXP"
    elif ticker.upper() == "QCOM":
        handle = "Qualcomm"
    elif ticker.upper() == "SNPS":
        handle = "Synopsis"
    elif ticker.upper() == "SPLK":
        handle = "splunk"
    elif ticker.upper() == "SWKS":
        handle = "SkyworksGlobal"
    elif ticker.upper() == "TXN":
        handle = "TXInstruments"
    elif ticker.upper() == "VRSN":
        handle = "VERISIGN"
    elif ticker.upper() == "WDAY":
        handle = "Workday"
    elif ticker.upper() == "WDC":
        handle = "WDCreators"
    elif ticker.upper() == "XLNX":
        handle = "XilinxInc"
    elif ticker.upper() == "BABA":
        handle = "AlibabaGroup"
    elif ticker.upper() == "TSLA":
        handle = "Tesla"
    elif ticker.upper() == "CRM":
        handle = "salesforce"
    elif ticker.upper() == "PYPL":
        handle = "PayPal"
    elif ticker.upper() == "ATVI":
        handle = "Activision"
    elif ticker.upper() == "EA":
        handle = "EA"
    elif ticker.upper() == "MTCH":
        handle = "Match"
    elif ticker.upper() == "ZG":
        handle = "zillow"
    elif ticker.upper() == "TTD":
        handle = "TheTradeDesk"
    elif ticker.upper() == "AMZN":
        handle = "Amazon"
    elif ticker.upper() == "TSM":
        handle = None
    elif ticker.upper() == "ORCL":
        handle = "Oracle"
    elif ticker.upper() == "SAP":
        handle = "SAP"
    elif ticker.upper() == "IBM":
        handle = "IBM"
    elif ticker.upper() == "VMW":
        handle = "VMware"
    elif ticker.upper() == "HPQ":
        handle = "HP"
    elif ticker.upper() == "DDD":
        handle = "3dsystems"
    elif ticker.upper() == "ACIW":
        handle = "Apple"
    elif ticker.upper() == "ADTN":
        handle = "Apple"
    elif ticker.upper() == "AKAM":
        handle = "Apple"
    elif ticker.upper() == "MDRX":
        handle = "Apple"
    elif ticker.upper() == "ALTR":
        handle = "Apple"
    elif ticker.upper() == "DOX":
        handle = "Apple"
    elif ticker.upper() == "AZPN":
        handle = "Apple"
    elif ticker.upper() == "CACI":
        handle = "Apple"
    elif ticker.upper() == "CIEN":
        handle = "Apple"
    elif ticker.upper() == "CRUS":
        handle = "Apple"
    elif ticker.upper() == "CVLT":
        handle = "Apple"
    elif ticker.upper() == "GLW":
        handle = "Apple"
    elif ticker.upper() == "CREE":
        handle = "Apple"
    elif ticker.upper() == "DBD":
        handle = "Apple"
    elif ticker.upper() == "EQIX":
        handle = "Equinix"
    elif ticker.upper() == "FFIV":
        handle = "F5Networks"
    elif ticker.upper() == "FICO":
        handle = "FICO"
    elif ticker.upper() == "GRMN":
        handle = "Apple"
    elif ticker.upper() == "IT":
        handle = "Apple"
    elif ticker.upper() == "GWRE":
        handle = "Apple"
    elif ticker.upper() == "IDCC":
        handle = "Apple"
    elif ticker.upper() == "JCOM":
        handle = "Apple"
    elif ticker.upper() == "JNPR":
        handle = "Apple"
    elif ticker.upper() == "LHX":
        handle = "Apple"
    elif ticker.upper() == "LDOS":
        handle = "Apple"
    elif ticker.upper() == "MRVL":
        handle = "Apple"
    elif ticker.upper() == "MSI":
        handle = "Apple"
    elif ticker.upper() == "NCR":
        handle = "Apple"
    elif ticker.upper() == "NTAP":
        handle = "Apple"
    elif ticker.upper() == "NLOK":
        handle = "Apple"
    elif ticker.upper() == "NUAN":
        handle = "Apple"
    elif ticker.upper() == "ON":
        handle = "onsemi"
    elif ticker.upper() == "PANW":
        handle = "Apple"
    elif ticker.upper() == "PBI":
        handle = "Apple"
    elif ticker.upper() == "PLT":
        handle = "Apple"
    elif ticker.upper() == "PRGS":
        handle = "Apple"
    elif ticker.upper() == "PTC":
        handle = "Apple"
    elif ticker.upper() == "SAIC":
        handle = "Apple"
    elif ticker.upper() == "STX":
        handle = "Apple"
    elif ticker.upper() == "SMTC":
        handle = "Apple"
    elif ticker.upper() == "NOW":
        handle = "Apple"
    elif ticker.upper() == "SLAB":
        handle = "Apple"
    elif ticker.upper() == "SSNC":
        handle = "Apple"
    elif ticker.upper() == "SYNA":
        handle = "Apple"
    elif ticker.upper() == "TDC":
        handle = "Teradata"
    elif ticker.upper() == "TER":
        handle = "Teradyneinc"
    elif ticker.upper() == "TWTR":
        handle = "Twitter"
    elif ticker.upper() == "TYL":
        handle = "tylertech"
    elif ticker.upper() == "VSAT":
        handle = "ViasatInc"
    elif ticker.upper() == "VIAV":
        handle = "ViaviSolutions"

    return handle


def scrape_timeline(handle):
    timeline = api.GetUserTimeline(screen_name=handle, count=200)

    l = []
    for tweet in timeline:
        tweet = tweet.AsDict()
        if "in_reply_to_screen_name" not in tweet:
            l.append(tweet["text"])

    return l


if __name__ == "__main__":
    pass
