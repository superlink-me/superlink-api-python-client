# coding: utf-8

"""
    Superlink

    API for Superlink

    The version of the OpenAPI document: v0.3.26
    Contact: support@superlink.me
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ApiCoin(str, Enum):
    """
    ApiCoin
    """

    """
    allowed enum values
    """
    BTC = 'BTC'
    LTC = 'LTC'
    DOGE = 'DOGE'
    RDD = 'RDD'
    DASH = 'DASH'
    PPC = 'PPC'
    NMC = 'NMC'
    FTC = 'FTC'
    XCP = 'XCP'
    BLK = 'BLK'
    NSR = 'NSR'
    NBT = 'NBT'
    MZC = 'MZC'
    VIA = 'VIA'
    RBY = 'RBY'
    GRS = 'GRS'
    DGC = 'DGC'
    DGB = 'DGB'
    MONA = 'MONA'
    CLAM = 'CLAM'
    XPM = 'XPM'
    NEOS = 'NEOS'
    JBS = 'JBS'
    ZRC = 'ZRC'
    VTC = 'VTC'
    NXT = 'NXT'
    BURST = 'BURST'
    MUE = 'MUE'
    ZOOM = 'ZOOM'
    SDC = 'SDC'
    PKB = 'PKB'
    PND = 'PND'
    START = 'START'
    MOIN = 'MOIN'
    EXP = 'EXP'
    DCR = 'DCR'
    XEM = 'XEM'
    PART = 'PART'
    SHR = 'SHR'
    NVC = 'NVC'
    AC = 'AC'
    BTCD = 'BTCD'
    DOPE = 'DOPE'
    TPC = 'TPC'
    AIB = 'AIB'
    EDRC = 'EDRC'
    SYS = 'SYS'
    SLR = 'SLR'
    SMLY = 'SMLY'
    ETH = 'ETH'
    PSB = 'PSB'
    XBC = 'XBC'
    NXS = 'NXS'
    INSN = 'INSN'
    OK = 'OK'
    BRIT = 'BRIT'
    CMP = 'CMP'
    CRW = 'CRW'
    BELA = 'BELA'
    ICX = 'ICX'
    FJC = 'FJC'
    MIX = 'MIX'
    CLUB = 'CLUB'
    RICHX = 'RICHX'
    POT = 'POT'
    QRK = 'QRK'
    TRC = 'TRC'
    GRC = 'GRC'
    AUR = 'AUR'
    IXC = 'IXC'
    NLG = 'NLG'
    BITB = 'BITB'
    XMY = 'XMY'
    BSD = 'BSD'
    UNO = 'UNO'
    GB = 'GB'
    SHM = 'SHM'
    CRX = 'CRX'
    BIQ = 'BIQ'
    EVO = 'EVO'
    STO = 'STO'
    BIGUP = 'BIGUP'
    GAME = 'GAME'
    DLC = 'DLC'
    ZYD = 'ZYD'
    DBIC = 'DBIC'
    STRAT = 'STRAT'
    SH = 'SH'
    MARS = 'MARS'
    UBQ = 'UBQ'
    PTC = 'PTC'
    NRO = 'NRO'
    ARK = 'ARK'
    USC = 'USC'
    THC = 'THC'
    LINX = 'LINX'
    ECN = 'ECN'
    DNR = 'DNR'
    PINK = 'PINK'
    ATOM = 'ATOM'
    PIVX = 'PIVX'
    FLASH = 'FLASH'
    ZEN = 'ZEN'
    PUT = 'PUT'
    ZNY = 'ZNY'
    UNIFY = 'UNIFY'
    XST = 'XST'
    VC = 'VC'
    XMR = 'XMR'
    VOX = 'VOX'
    NAV = 'NAV'
    ZEC = 'ZEC'
    LSK = 'LSK'
    STEEM = 'STEEM'
    XZC = 'XZC'
    RBTC = 'RBTC'
    RPT = 'RPT'
    KMD = 'KMD'
    RIC = 'RIC'
    XRP = 'XRP'
    NEBL = 'NEBL'
    ZCL = 'ZCL'
    WHL = 'WHL'
    ERC = 'ERC'
    DMD = 'DMD'
    BTM = 'BTM'
    BIO = 'BIO'
    SSN = 'SSN'
    TOA = 'TOA'
    BTX = 'BTX'
    ACC = 'ACC'
    ELLA = 'ELLA'
    PIRL = 'PIRL'
    XNO = 'XNO'
    VIVO = 'VIVO'
    FRST = 'FRST'
    HNC = 'HNC'
    BUZZ = 'BUZZ'
    MBRS = 'MBRS'
    HC = 'HC'
    HTML = 'HTML'
    ODN = 'ODN'
    ONX = 'ONX'
    RVN = 'RVN'
    GBX = 'GBX'
    BTCZ = 'BTCZ'
    POA = 'POA'
    NYC = 'NYC'
    MXT = 'MXT'
    WC = 'WC'
    MNX = 'MNX'
    MUSIC = 'MUSIC'
    CRAVE = 'CRAVE'
    STAK = 'STAK'
    LCH = 'LCH'
    EXCL = 'EXCL'
    LCC = 'LCC'
    XFE = 'XFE'
    EOS = 'EOS'
    TRX = 'TRX'
    KOBO = 'KOBO'
    HUSH = 'HUSH'
    BAN = 'BAN'
    ETF = 'ETF'
    OMNI = 'OMNI'
    BIFI = 'BIFI'
    CNMC = 'CNMC'
    BCN = 'BCN'
    RIN = 'RIN'
    ATP = 'ATP'
    EVT = 'EVT'
    ATN = 'ATN'
    BIS = 'BIS'
    NEET = 'NEET'
    BOPO = 'BOPO'
    OOT = 'OOT'
    ALIAS = 'ALIAS'
    BOXY = 'BOXY'
    FLO = 'FLO'
    MEC = 'MEC'
    BTDX = 'BTDX'
    XAX = 'XAX'
    ANON = 'ANON'
    LTZ = 'LTZ'
    SMART = 'SMART'
    XUEZ = 'XUEZ'
    HLM = 'HLM'
    WEB = 'WEB'
    ACM = 'ACM'
    BITC = 'BITC'
    TZC = 'TZC'
    VAR = 'VAR'
    IOV = 'IOV'
    FIO = 'FIO'
    BSV = 'BSV'
    DXN = 'DXN'
    PCX = 'PCX'
    LOKI = 'LOKI'
    NIM = 'NIM'
    EXOS = 'EXOS'
    ECA = 'ECA'
    SOOM = 'SOOM'
    FREE = 'FREE'
    NPW = 'NPW'
    BST = 'BST'
    ZEST = 'ZEST'
    ABT = 'ABT'
    PION = 'PION'
    ZBUX = 'ZBUX'
    KPL = 'KPL'
    TPAY = 'TPAY'
    ZILLA = 'ZILLA'
    ANK = 'ANK'
    BCC = 'BCC'
    HPB = 'HPB'
    ONE = 'ONE'
    SBC = 'SBC'
    IPC = 'IPC'
    DMTC = 'DMTC'
    OGC = 'OGC'
    SHIT = 'SHIT'
    ANDES = 'ANDES'
    AREPA = 'AREPA'
    BOLI = 'BOLI'
    RIL = 'RIL'
    BRAVO = 'BRAVO'
    ALGO = 'ALGO'
    BZX = 'BZX'
    GXX = 'GXX'
    HEAT = 'HEAT'
    XDN = 'XDN'
    FSN = 'FSN'
    BOLD = 'BOLD'
    IOST = 'IOST'
    TKEY = 'TKEY'
    USE = 'USE'
    BCZ = 'BCZ'
    IOC = 'IOC'
    ASF = 'ASF'
    MASS = 'MASS'
    FAIR = 'FAIR'
    NUKO = 'NUKO'
    CMT = 'CMT'
    EUNO = 'EUNO'
    IOTX = 'IOTX'
    ONION = 'ONION'
    BTS = 'BTS'
    UGAS = 'UGAS'
    ADS = 'ADS'
    ARA = 'ARA'
    ZIL = 'ZIL'
    MOAC = 'MOAC'
    SWTC = 'SWTC'
    VNSC = 'VNSC'
    ECC = 'ECC'
    RPD = 'RPD'
    RAP = 'RAP'
    GARD = 'GARD'
    ZER = 'ZER'
    EBST = 'EBST'
    SHARD = 'SHARD'
    CMM = 'CMM'
    BLOCK = 'BLOCK'
    AUDAX = 'AUDAX'
    LUNA = 'LUNA'
    ZPM = 'ZPM'
    MEM = 'MEM'
    SWIFT = 'SWIFT'
    FIX = 'FIX'
    CPC = 'CPC'
    VGO = 'VGO'
    DVT = 'DVT'
    MTNS = 'MTNS'
    BLAST = 'BLAST'
    DCT = 'DCT'
    AUX = 'AUX'
    USDP = 'USDP'
    HTDF = 'HTDF'
    YEC = 'YEC'
    ARW = 'ARW'
    MDM = 'MDM'
    CYB = 'CYB'
    DOT = 'DOT'
    AEON = 'AEON'
    RES = 'RES'
    AYA = 'AYA'
    DAPS = 'DAPS'
    CSC = 'CSC'
    NOLLAR = 'NOLLAR'
    XNOS = 'XNOS'
    CPU = 'CPU'
    VCT = 'VCT'
    CZR = 'CZR'
    ABBC = 'ABBC'
    HET = 'HET'
    XAS = 'XAS'
    VDL = 'VDL'
    MED = 'MED'
    ZVC = 'ZVC'
    VESTX = 'VESTX'
    DBT = 'DBT'
    SEOS = 'SEOS'
    MXW = 'MXW'
    ZNZ = 'ZNZ'
    XCX = 'XCX'
    SOX = 'SOX'
    NYZO = 'NYZO'
    ULC = 'ULC'
    KAL = 'KAL'
    XSN = 'XSN'
    DOGEC = 'DOGEC'
    QBC = 'QBC'
    IMG = 'IMG'
    QOS = 'QOS'
    PKT = 'PKT'
    LHD = 'LHD'
    CENNZ = 'CENNZ'
    UMBRU = 'UMBRU'
    EVER = 'EVER'
    XPC = 'XPC'
    NIX = 'NIX'
    UC = 'UC'
    GALI = 'GALI'
    OLT = 'OLT'
    XBI = 'XBI'
    DONU = 'DONU'
    EARTHS = 'EARTHS'
    HDD = 'HDD'
    SUGAR = 'SUGAR'
    AILE = 'AILE'
    TENT = 'TENT'
    AIN = 'AIN'
    MSR = 'MSR'
    SUMO = 'SUMO'
    ETN = 'ETN'
    BYTZ = 'BYTZ'
    WOW = 'WOW'
    XTNC = 'XTNC'
    LTHN = 'LTHN'
    NODE = 'NODE'
    AGM = 'AGM'
    TELOS = 'TELOS'
    AION = 'AION'
    KTV = 'KTV'
    ZCR = 'ZCR'
    ERG = 'ERG'
    PESO = 'PESO'
    XRPHD = 'XRPHD'
    KSM = 'KSM'
    PCN = 'PCN'
    NCH = 'NCH'
    ICU = 'ICU'
    FNSA = 'FNSA'
    AERGO = 'AERGO'
    XTH = 'XTH'
    LV = 'LV'
    PHR = 'PHR'
    VITAE = 'VITAE'
    DIN = 'DIN'
    SPL = 'SPL'
    YCE = 'YCE'
    XLR = 'XLR'
    DGLD = 'DGLD'
    XNS = 'XNS'
    EM = 'EM'
    SHN = 'SHN'
    SEELE = 'SEELE'
    AE = 'AE'
    ODX = 'ODX'
    KAVA = 'KAVA'
    GLEEC = 'GLEEC'
    FIL = 'FIL'
    RUTA = 'RUTA'
    CSDT = 'CSDT'
    ETI = 'ETI'
    ERE = 'ERE'
    BTH = 'BTH'
    MESG = 'MESG'
    FIMK = 'FIMK'
    AR = 'AR'
    OGO = 'OGO'
    RNG = 'RNG'
    PEXA = 'PEXA'
    MOON = 'MOON'
    FCH = 'FCH'
    LAT = 'LAT'
    VEO = 'VEO'
    GFN = 'GFN'
    BAND = 'BAND'
    DROP = 'DROP'
    LYRA = 'LYRA'
    CS = 'CS'
    RUPX = 'RUPX'
    THETA = 'THETA'
    SOL = 'SOL'
    THT = 'THT'
    CFX = 'CFX'
    KUMA = 'KUMA'
    HASH = 'HASH'
    CSPR = 'CSPR'
    EARTH = 'EARTH'
    EGLD = 'EGLD'
    CHI = 'CHI'
    KOTO = 'KOTO'
    XRD = 'XRD'
    AETH = 'AETH'
    DNA = 'DNA'
    SIERRA = 'SIERRA'
    LET = 'LET'
    BTCV = 'BTCV'
    ABA = 'ABA'
    SCC = 'SCC'
    EDG = 'EDG'
    AMS = 'AMS'
    BU = 'BU'
    GRAM = 'GRAM'
    YAP = 'YAP'
    NOVO = 'NOVO'
    GHOST = 'GHOST'
    HST = 'HST'
    PRJ = 'PRJ'
    YOU = 'YOU'
    BYND = 'BYND'
    FLOW = 'FLOW'
    SCDO = 'SCDO'
    BIND = 'BIND'
    COINEVO = 'COINEVO'
    SCRIBE = 'SCRIBE'
    HYN = 'HYN'
    BHP = 'BHP'
    MKF = 'MKF'
    XDC = 'XDC'
    STR = 'STR'
    HBC = 'HBC'
    KTS = 'KTS'
    LKR = 'LKR'
    XWC = 'XWC'
    DEAL = 'DEAL'
    NTY = 'NTY'
    AG = 'AG'
    CICO = 'CICO'
    IRIS = 'IRIS'
    BDX = 'BDX'
    SLS = 'SLS'
    SRM = 'SRM'
    BPS = 'BPS'
    NKN = 'NKN'
    ICL = 'ICL'
    BONO = 'BONO'
    PLC = 'PLC'
    DUN = 'DUN'
    DMCH = 'DMCH'
    CTC = 'CTC'
    GBCR = 'GBCR'
    XDAG = 'XDAG'
    SCAP = 'SCAP'
    GTM = 'GTM'
    RNL = 'RNL'
    GRIN = 'GRIN'
    MWC = 'MWC'
    DOCK = 'DOCK'
    POLYX = 'POLYX'
    DIVER = 'DIVER'
    APN = 'APN'
    MTC = 'MTC'
    NC = 'NC'
    XINY = 'XINY'
    BUFS = 'BUFS'
    STOS = 'STOS'
    TON = 'TON'
    TAFT = 'TAFT'
    HYDRA = 'HYDRA'
    NOR = 'NOR'
    WCN = 'WCN'
    PSWAP = 'PSWAP'
    XOR = 'XOR'
    SSP = 'SSP'
    DEI = 'DEI'
    ZERO = 'ZERO'
    ALPHA = 'ALPHA'
    NOBL = 'NOBL'
    EAST = 'EAST'
    KDA = 'KDA'
    SOUL = 'SOUL'
    LORE = 'LORE'
    FNR = 'FNR'
    NEXUS = 'NEXUS'
    QTZ = 'QTZ'
    XMA = 'XMA'
    CALL = 'CALL'
    VAL = 'VAL'
    EMIT = 'EMIT'
    APTOS = 'APTOS'
    ADON = 'ADON'
    BTSG = 'BTSG'
    LFC = 'LFC'
    TREE = 'TREE'
    LX = 'LX'
    XLN = 'XLN'
    ZRB = 'ZRB'
    UCO = 'UCO'
    WMP = 'WMP'
    KOIN = 'KOIN'
    PIRATE = 'PIRATE'
    ACT = 'ACT'
    PRKL = 'PRKL'
    SSC = 'SSC'
    GC = 'GC'
    PLGR = 'PLGR'
    MPLGR = 'MPLGR'
    KNOX = 'KNOX'
    ZED = 'ZED'
    CNDL = 'CNDL'
    WLKRR = 'WLKRR'
    YUNGE = 'YUNGE'
    VOKEN = 'VOKEN'
    APL = 'APL'
    EVRYNET = 'EVRYNET'
    NENG = 'NENG'
    CHTA = 'CHTA'
    OAS = 'OAS'
    KLV = 'KLV'
    VEIL = 'VEIL'
    GTB = 'GTB'
    XDAI = 'XDAI'
    COM = 'COM'
    CHC = 'CHC'
    SERF = 'SERF'
    BNB = 'BNB'
    SIN = 'SIN'
    DLN = 'DLN'
    BONTE = 'BONTE'
    PEER = 'PEER'
    ZET = 'ZET'
    ABY = 'ABY'
    XVC = 'XVC'
    MCX = 'MCX'
    HEALIOS = 'HEALIOS'
    BMK = 'BMK'
    DENTX = 'DENTX'
    CFG = 'CFG'
    XPRT = 'XPRT'
    HONEY = 'HONEY'
    BALLZ = 'BALLZ'
    COSA = 'COSA'
    BR = 'BR'
    SUI = 'SUI'
    UIDD = 'UIDD'
    ACA = 'ACA'
    BNC = 'BNC'
    TAU = 'TAU'
    PDEX = 'PDEX'
    ZKS = 'ZKS'
    QVT = 'QVT'
    MEER = 'MEER'
    REEF = 'REEF'
    CLO = 'CLO'
    BDB = 'BDB'
    ACE = 'ACE'
    CCN = 'CCN'
    BBA = 'BBA'
    CRUZ = 'CRUZ'
    SAPP = 'SAPP'
    KYAN = 'KYAN'
    AZR = 'AZR'
    CFL = 'CFL'
    TRTT = 'TRTT'
    PNY = 'PNY'
    BECN = 'BECN'
    MONK = 'MONK'
    SAGA = 'SAGA'
    SUV = 'SUV'
    ESK = 'ESK'
    BIR = 'BIR'
    MOBIC = 'MOBIC'
    FLS = 'FLS'
    DSM = 'DSM'
    HVH = 'HVH'
    MOB = 'MOB'
    IF = 'IF'
    NAM = 'NAM'
    ZBC = 'ZBC'
    NEO = 'NEO'
    TOMO = 'TOMO'
    XSEL = 'XSEL'
    LKSC = 'LKSC'
    AS = 'AS'
    XEC = 'XEC'
    LMO = 'LMO'
    HNT = 'HNT'
    FIS = 'FIS'
    SGE = 'SGE'
    GERT = 'GERT'
    META = 'META'
    FRA = 'FRA'
    CCD = 'CCD'
    GHM = 'GHM'
    LTP = 'LTP'
    VKAX = 'VKAX'
    MATIC = 'MATIC'
    UNW = 'UNW'
    TWINS = 'TWINS'
    TLOS = 'TLOS'
    AU = 'AU'
    VCG = 'VCG'
    AIOZ = 'AIOZ'
    CORE = 'CORE'
    PEC = 'PEC'
    UNT = 'UNT'
    CAPS = 'CAPS'
    SUM = 'SUM'
    TT = 'TT'
    BKT = 'BKT'
    NODL = 'NODL'
    PCOIN = 'PCOIN'
    TAO = 'TAO'
    FTM = 'FTM'
    RPG = 'RPG'
    LAKE = 'LAKE'
    ELV = 'ELV'
    BIC = 'BIC'
    EVC = 'EVC'
    ONT = 'ONT'
    CZZ = 'CZZ'
    MCM = 'MCM'
    BTCR = 'BTCR'
    RISE = 'RISE'
    DFI = 'DFI'
    EFI = 'EFI'
    ALPH = 'ALPH'
    GLMR = 'GLMR'
    MOVR = 'MOVR'
    WPC = 'WPC'
    WEI = 'WEI'
    DFC = 'DFC'
    HYC = 'HYC'
    BEAM = 'BEAM'
    ELF = 'ELF'
    AUDL = 'AUDL'
    ATH = 'ATH'
    NEW = 'NEW'
    BTA = 'BTA'
    NEOX = 'NEOX'
    MEWC = 'MEWC'
    BCX = 'BCX'
    XTZ = 'XTZ'
    BBP = 'BBP'
    ADA = 'ADA'
    TES = 'TES'
    ZTX = 'ZTX'
    CLC = 'CLC'
    VIPS = 'VIPS'
    XMX = 'XMX'
    TRTL = 'TRTL'
    EGEM = 'EGEM'
    HODL = 'HODL'
    PHL = 'PHL'
    SC = 'SC'
    MYT = 'MYT'
    POLIS = 'POLIS'
    XMCC = 'XMCC'
    COLX = 'COLX'
    GIN = 'GIN'
    MNP = 'MNP'
    MLN = 'MLN'
    KIN = 'KIN'
    EOSC = 'EOSC'
    PKC = 'PKC'
    SKT = 'SKT'
    ANY = 'ANY'
    MCASH = 'MCASH'
    TRUE = 'TRUE'
    IOTE = 'IOTE'
    BAY = 'BAY'
    XRG = 'XRG'
    CHZ = 'CHZ'
    ASK = 'ASK'
    QTUM = 'QTUM'
    ETP = 'ETP'
    GXC = 'GXC'
    CRP = 'CRP'
    ELA = 'ELA'
    SNOW = 'SNOW'
    XIN = 'XIN'
    NEXI = 'NEXI'
    AOA = 'AOA'
    NAS = 'NAS'
    BND = 'BND'
    LUX = 'LUX'
    COS = 'COS'
    CCC = 'CCC'
    SXP = 'SXP'
    ROI = 'ROI'
    DYN = 'DYN'
    SEQ = 'SEQ'
    DEO = 'DEO'
    DST = 'DST'
    CY = 'CY'
    YEE = 'YEE'
    IOTA = 'IOTA'
    SMR = 'SMR'
    AXE = 'AXE'
    XYM = 'XYM'
    XVM = 'XVM'
    FIC = 'FIC'
    HNS = 'HNS'
    ISK = 'ISK'
    ALTME = 'ALTME'
    FUND = 'FUND'
    STX = 'STX'
    SLU = 'SLU'
    COTI = 'COTI'
    ROGER = 'ROGER'
    TOPL = 'TOPL'
    KLY = 'KLY'
    SHFT = 'SHFT'
    BTV = 'BTV'
    SKY = 'SKY'
    KLAY = 'KLAY'
    BTQ = 'BTQ'
    XCH = 'XCH'
    PLMNT = 'PLMNT'
    NULS = 'NULS'
    BBC = 'BBC'
    JGC = 'JGC'
    AVAX = 'AVAX'
    BOBA = 'BOBA'
    LOOP = 'LOOP'
    STRK = 'STRK'
    NRG = 'NRG'
    FO = 'FO'
    RTM = 'RTM'
    XRC = 'XRC'
    XPI = 'XPI'
    VARCH = 'VARCH'
    TNKR = 'TNKR'
    IPOS = 'IPOS'
    MINA = 'MINA'
    BTY = 'BTY'
    SDGO = 'SDGO'
    ARDR = 'ARDR'
    MTR = 'MTR'
    SAFE = 'SAFE'
    FLUX = 'FLUX'
    RITO = 'RITO'
    XND = 'XND'
    PAC = 'PAC'
    PWR = 'PWR'
    BELL = 'BELL'
    CHX = 'CHX'
    NEXA = 'NEXA'
    BTT = 'BTT'
    FXTC = 'FXTC'
    AMA = 'AMA'
    AXIV = 'AXIV'
    EVE = 'EVE'
    STASH = 'STASH'
    CELO = 'CELO'
    TH = 'TH'
    GRLC = 'GRLC'
    GWL = 'GWL'
    ZYN = 'ZYN'
    WICC = 'WICC'
    HOME = 'HOME'
    STC = 'STC'
    STRAX = 'STRAX'
    KAS = 'KAS'
    AKA = 'AKA'
    GENOM = 'GENOM'
    ZAMA = 'ZAMA'
    SCR = 'SCR'
    VITE = 'VITE'
    WTC = 'WTC'
    ILT = 'ILT'
    XERO = 'XERO'
    LAX = 'LAX'
    BCO = 'BCO'
    BHD = 'BHD'
    PTN = 'PTN'
    VLX = 'VLX'
    WAN = 'WAN'
    WAVES = 'WAVES'
    ABC = 'ABC'
    CRM = 'CRM'
    SEM = 'SEM'
    ION = 'ION'
    FCT = 'FCT'
    WGR = 'WGR'
    OBSR = 'OBSR'
    AFS = 'AFS'
    XDS = 'XDS'
    AQUA = 'AQUA'
    HATCH = 'HATCH'
    KUSD = 'KUSD'
    GENS = 'GENS'
    EQ = 'EQ'
    QKC = 'QKC'
    FVDC = 'FVDC'
    USDC = 'USDC'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApiCoin from a JSON string"""
        return cls(json.loads(json_str))


