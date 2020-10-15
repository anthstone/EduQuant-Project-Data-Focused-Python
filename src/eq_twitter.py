# eq_twitter.py
# Description: module to interact with Twitter API
# Authors: Anthony Stone
#          Alexander Talbott
#          Jim Wang


import twitter
import pandas as pd
import eq_utilities

# this is not secure in any way shape or form
# but it is a dummy account that I don't use
# please don't abuse
api = twitter.Api(
    "xjBcMPKQDKtmS9YOxRjDs2v4T",
    "8sK4L0kYM0VT8UecMu8IPZgd54O8d20uaSnFwiAQvcDz0AWVRB",
    "1309554738543943684-jD3glTsDlofSFWX5DPVFSguZsBRaMp",
    "UbHoxvZky0ZcJQwQ0hpb6oIlDu01Dd3IuMslv0nzVmg2A",
)

# convert from ticker to company twitter handle
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
        handle = "ACI_Worldwide"
    elif ticker.upper() == "ADTN":
        handle = "ADTRAN"
    elif ticker.upper() == "AKAM":
        handle = "Akamai"
    elif ticker.upper() == "MDRX":
        handle = "Allscripts"
    elif ticker.upper() == "ALTR":
        handle = "Altair_Inc"
    elif ticker.upper() == "DOX":
        handle = "Amdocs"
    elif ticker.upper() == "AZPN":
        handle = "AspenTech"
    elif ticker.upper() == "CACI":
        handle = "CACIIntl"
    elif ticker.upper() == "CIEN":
        handle = "Ciena"
    elif ticker.upper() == "CRUS":
        handle = "CirrusLogic"
    elif ticker.upper() == "CVLT":
        handle = "Commvault"
    elif ticker.upper() == "GLW":
        handle = "Corning"
    elif ticker.upper() == "CREE":
        handle = "Cree"
    elif ticker.upper() == "DBD":
        handle = "DieboldNixdorf"
    elif ticker.upper() == "EQIX":
        handle = "Equinix"
    elif ticker.upper() == "FFIV":
        handle = "F5Networks"
    elif ticker.upper() == "FICO":
        handle = "FICO"
    elif ticker.upper() == "GRMN":
        handle = "Garmin"
    elif ticker.upper() == "IT":
        handle = "Gartner_inc"
    elif ticker.upper() == "GWRE":
        handle = "Guidewire_PandC"
    elif ticker.upper() == "IDCC":
        handle = "InterDigitalCom"
    elif ticker.upper() == "JCOM":
        handle = "j2global"
    elif ticker.upper() == "JNPR":
        handle = "JuniperNetworks"
    elif ticker.upper() == "LHX":
        handle = "L3HarrisTech"
    elif ticker.upper() == "LDOS":
        handle = "LeidosInc"
    elif ticker.upper() == "MRVL":
        handle = "marvellsemi"
    elif ticker.upper() == "MSI":
        handle = "MotorolaUS"
    elif ticker.upper() == "NCR":
        handle = "NCRCorporation"
    elif ticker.upper() == "NTAP":
        handle = "NetApp"
    elif ticker.upper() == "NLOK":
        handle = "NortonLifelock"
    elif ticker.upper() == "NUAN":
        handle = "NuanceInc"
    elif ticker.upper() == "ON":
        handle = "onsemi"
    elif ticker.upper() == "PANW":
        handle = "PaloAltoNtwks"
    elif ticker.upper() == "PBI":
        handle = "PitneyBowes"
    elif ticker.upper() == "PLT":
        handle = "Plantronics"
    elif ticker.upper() == "PRGS":
        handle = "ProgressSW"
    elif ticker.upper() == "PTC":
        handle = "PTC"
    elif ticker.upper() == "SAIC":
        handle = "SAICinc"
    elif ticker.upper() == "STX":
        handle = "Seagate"
    elif ticker.upper() == "SMTC":
        handle = "SMTCCorporation"
    elif ticker.upper() == "NOW":
        handle = "servicenow"
    elif ticker.upper() == "SLAB":
        handle = "siliconlabs"
    elif ticker.upper() == "SSNC":
        handle = "SSCTechnologies"
    elif ticker.upper() == "SYNA":
        handle = "SynaCorp"
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


# scrape the twitter timeline of a given handle
def scrape_timeline(handle):
    timeline = api.GetUserTimeline(screen_name=handle, count=200)

    l = []
    for tweet in timeline:
        tweet = tweet.AsDict()
        if "in_reply_to_screen_name" not in tweet:
            l.append(tweet["text"])

    return l
