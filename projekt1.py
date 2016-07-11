import itertools
from tkinter import *
from tkinter import ttk

raam = Tk()
raam.title("Geneetika")

silt=ttk.Label(raam, text=("Mendeli seadused on organismide tunnuste pärandumise seadused geneetikas.\n Mendeli seadused avastas 1860. aastatel loodusseadustest huvituv augustiini munk Gregor Mendel,\n kes tegi ristamiskatseid hernetaimedega,\nning sõnastas need 1865. aastal Brunni (praegu Brno) Looduslooseltsi toimetistes ilmunud artiklis.\nMendeli seadused:\n1.Ristates kahte homosügootset (AABB, aabb) isendit on esimese põlvkonna järglased geneetiliselt identsed.\n2.Ristates erinevaid heterosügoote(AaBB, AaBb),\ntekib järglaspõlvkonnas tunnuse avaldumisel genotüübiline ja fenotüübiline lahknemine.\nKaks tunnust (geeni) päranduvad üksteisest sõltumatult.\nMeie toome näitena herned, kuna need olid algsed katsetaimed. \nProgrammiga on võimalik lahendada dihübriidset dominatsuse (a=herne värv ja b=tekstuur)\nja monohübriidset kodominatsuse ülesannet(a=õie värv)\nProgrammi peab sisestama mõlema vanema geeni lookused.\n Ühes lookuses on 2 alleeli (aa). Kirjutage enda valikul kas suured või väikesed 2 a-d ja 2 b-d \nvõi kodominatsuse lahendamiseks ainult a-d.\n Seejärel programm väljastab järglaste feno- ja genotüübid.\n"))    
silt.grid(row=0, column=0, rowspan=8, columnspan=12, sticky=W+E+N+S)
      
silt = ttk.Label(raam, text="Ema genotüüp: ")
silt.grid(column=0, row=9, sticky=W)

ema_genotüüp = ttk.Entry(raam)
ema_genotüüp.grid(column=1, row=9, sticky=W)

silt = ttk.Label(raam, text="Isa genotüüp: ")
silt.grid(column=0, row=10, sticky=W)

isa_genotüüp = ttk.Entry(raam)
isa_genotüüp.grid(column=1, row=10, sticky=W)

def järglased(ema,isa):    
    järglaste_ajutine_list = []

    for ema_alleel in ema:
        for isa_alleel in isa:
            järglane=ema_alleel,isa_alleel
            if järglane[0].upper() == järglane[1].upper():
                järglane = ''.join(sorted(järglane))
                järglaste_ajutine_list.append(järglane)

    list_a = []
    list_b = []
    i = 0
    for lookus in järglaste_ajutine_list:
        if i < 4:
            list_a.append(lookus)
        else:
            list_b.append(lookus)
        i += 1

    return list_a, list_b

def genotüübid(ema,isa):
    list_a, list_b = järglased(ema,isa)
    järglaste_genotüübid = list(itertools.product(list_a, list_b))
    järglaste_list = []
    for paar in järglaste_genotüübid:
        järglaste_list.append(''.join(paar))

    järglaste_sagedus = {}
    for el in järglaste_list:
        if el in järglaste_sagedus:
            continue
        else:
            järglaste_sagedus[el] = järglaste_list.count(el)

    return järglaste_sagedus
    
def fenotüübid(järglaste_sagedus):
    fenotüüp = {}
    AB = 0
    aB = 0
    Ab = 0
    ab = 0
    for el in järglaste_sagedus:
        if 'A' in el and 'B' in el:
            AB += järglaste_sagedus[el]  	 
        elif 'aa' in el and 'bb' in el:
            ab += järglaste_sagedus[el]
        elif 'aa' in el and 'B' in el:
            aB += järglaste_sagedus[el]
        elif 'A' in el and 'bb' in el:
            Ab += järglaste_sagedus[el]
             
    fenotüüp['kollane ja sile'] = AB
    fenotüüp['roheline ja krobeline'] = ab
    fenotüüp['roheline ja sile'] = aB
    fenotüüp['kollane ja krobeline'] = Ab

    return fenotüüp

def lahenda():
    ema=ema_genotüüp.get()
    isa=isa_genotüüp.get()

    järglaste_sagedus = genotüübid(ema,isa)
    järglaste_list = set(järglaste_sagedus)
    fenotüüp = fenotüübid(järglaste_sagedus)
    
    if järglaste_sagedus=={}:
        silt=ttk.Label(raam, text=('Vigane sisend. Sisend peab olema kujul aabb, näiteks AaBb.'))
        silt.grid(row=12, column=0, columnspan=8)
    else:
        silt=ttk.Label(raam, text=('Järglaste genotüübid:',järglaste_sagedus), wraplength = 1000)
        silt.grid(row=12, column=0, columnspan=8)

    if fenotüüp=={}:
        silt=ttk.Label(raam, text=(''))
        silt.grid(row=13, column=0)
    else:  
        silt=ttk.Label(raam, text=('Järglaste fenotüübid:', fenotüüp), wraplength=1000)
        silt.grid(row=13, column=0, columnspan=8)

    silt=ttk.Label(raam, text=('Vanemad:'), wraplength=1000)
    silt.grid(row=14, column=0)

    if 'A' in ema and 'B' in ema:
        kol_sile = PhotoImage(file="kollane-ja-sile.gif")
        silt = ttk.Label(raam, image=kol_sile)
        silt.image = kol_sile
        silt.grid(row = 14, column = 1) 	 
    elif 'aa' in ema and 'bb' in ema:
        roh_krobe = PhotoImage(file="roheline-ja-krobeline.gif")
        silt=ttk.Label(raam, image=roh_krobe)
        silt.image = roh_krobe
        silt.grid(row=14, column=1)
    elif 'aa' in ema and 'B' in ema:
        roh_sile = PhotoImage(file="roheline-ja-sile.gif")
        silt=ttk.Label(raam, image=roh_sile)
        silt.image = roh_sile
        silt.grid(row=14, column=1)
    elif 'A' in ema and 'bb' in ema:
        kol_krobe = PhotoImage(file="kollane-ja-krobeline.gif")
        silt=ttk.Label(raam, image=kol_krobe)
        silt.image = kol_krobe
        silt.grid(row=14, column=1)

    silt=ttk.Label(raam, text=('X'))
    silt.grid(row=14, column=2)

    if 'A' in isa and 'B' in isa:
        kol_sile = PhotoImage(file="kollane-ja-sile.gif")
        silt = ttk.Label(raam, image=kol_sile)
        silt.image = kol_sile
        silt.grid(row = 14, column = 3) 	 
    elif 'aa' in isa and 'bb' in isa:
        roh_krobe = PhotoImage(file="roheline-ja-krobeline.gif")
        silt=ttk.Label(raam, image=roh_krobe)
        silt.image = roh_krobe
        silt.grid(row=14, column=3)
    elif 'aa' in isa and 'B' in isa:
        roh_sile = PhotoImage(file="roheline-ja-sile.gif")
        silt=ttk.Label(raam, image=roh_sile)
        silt.image = roh_sile
        silt.grid(row=14, column=3)
    elif 'A' in isa and 'bb' in isa:
        kol_krobe = PhotoImage(file="kollane-ja-krobeline.gif")
        silt=ttk.Label(raam, image=kol_krobe)
        silt.image = kol_krobe
        silt.grid(row=14, column=3)
        
    silt=ttk.Label(raam, text=('Järglased:'), wraplength=1000)
    silt.grid(row=15, column=0)

    kol_sile = PhotoImage(file="kollane-ja-sile.gif")
    silt = ttk.Label(raam, text=('A_B_:', fenotüüp['kollane ja sile']), image=kol_sile)
    silt.image = kol_sile
    silt.grid(row = 15, column = 1)

    kol_krobe = PhotoImage(file="kollane-ja-krobeline.gif")
    silt=ttk.Label(raam, text=('A_bb:', fenotüüp['kollane ja krobeline']), image=kol_krobe)
    silt.image = kol_krobe
    silt.grid(row = 15, column = 2)

    roh_sile = PhotoImage(file="roheline-ja-sile.gif")
    silt=ttk.Label(raam, text=('aaB_:', fenotüüp['roheline ja sile']), image=roh_sile)
    silt.image = roh_sile
    silt.grid(row = 15, column = 3)

    roh_krobe = PhotoImage(file="roheline-ja-krobeline.gif")
    silt=ttk.Label(raam, text=('aabb:', fenotüüp['roheline ja krobeline']), image=roh_krobe)
    silt.image = roh_krobe
    silt.grid(row = 15, column = 4)

    silt = ttk.Label(raam, text=('A_B_:', fenotüüp['kollane ja sile']))
    silt.grid(row = 16, column = 1)

    silt=ttk.Label(raam, text=('A_bb:', fenotüüp['kollane ja krobeline']))
    silt.grid(row = 16, column = 2)

    silt=ttk.Label(raam, text=('aaB_:', fenotüüp['roheline ja sile']))
    silt.grid(row = 16, column = 3)

    silt=ttk.Label(raam, text=('aabb:', fenotüüp['roheline ja krobeline']))
    silt.grid(row = 16, column = 4)
    

def ko_genotüübid(ema,isa):
    järglaste_list = []

    for ema_alleel in ema:
        for isa_alleel in isa:
            järglane=ema_alleel,isa_alleel
            if järglane[0].upper() == järglane[1].upper():
                järglane = ''.join(sorted(järglane))
                järglaste_list.append(järglane)

    järglaste_sagedus = {}
    for el in järglaste_list:
        if el in järglaste_sagedus:
            continue
        else:
            järglaste_sagedus[el] = järglaste_list.count(el)

    return järglaste_sagedus
    
def ko_fenotüübid(järglaste_sagedus):
    fenotüüp = {}
    AA = 0
    Aa = 0
    aa = 0
    for el in järglaste_sagedus:
        if 'AA' in el:
            AA += järglaste_sagedus[el]  	 
        elif 'aa' in el:
            aa += järglaste_sagedus[el]
        elif 'Aa' in el:
            Aa += järglaste_sagedus[el]
             
    fenotüüp['punane'] = AA
    fenotüüp['roosa'] = Aa
    fenotüüp['valge'] = aa

    return fenotüüp

def kodominantsus():
    ema=ema_genotüüp.get()
    isa=isa_genotüüp.get()

    järglaste_sagedus = ko_genotüübid(ema,isa)
    järglaste_list = set(järglaste_sagedus)
    fenotüüp = ko_fenotüübid(järglaste_sagedus)
    
    if ema.upper()!='AA' or isa.upper()!='AA':
        silt=ttk.Label(raam, text=('Vigane sisend. Sisend peab olema kujul aa, näiteks Aa.'))
        silt.grid(row=12, column=0, columnspan=8)
    else:
        silt=ttk.Label(raam, text=('Järglaste genotüübid:',järglaste_sagedus), wraplength = 1000)
        silt.grid(row=12, column=0, columnspan=8)

    if fenotüüp=={}:
        silt=ttk.Label(raam, text=(''))
        silt.grid(row=13, column=0)
    else:  
        silt=ttk.Label(raam, text=('Järglaste fenotüübid:', fenotüüp), wraplength=1000)
        silt.grid(row=13, column=0, columnspan=8)

    silt=ttk.Label(raam, text=('Vanemad:'), wraplength=1000)
    silt.grid(row=14, column=0)

    if 'AA' in ema:
        punane = PhotoImage(file="punane.gif")
        silt = ttk.Label(raam, image=punane)
        silt.image = punane
        silt.grid(row = 14, column = 1) 	 
    elif 'aa' in ema:
        valge = PhotoImage(file="valge.gif")
        silt=ttk.Label(raam, image=valge)
        silt.image = valge
        silt.grid(row=14, column=1)
    elif 'Aa' in ema:
        roosa = PhotoImage(file="roosa.gif")
        silt=ttk.Label(raam, image=roosa)
        silt.image = roosa
        silt.grid(row=14, column=1)

    silt=ttk.Label(raam, text=('X'))
    silt.grid(row=14, column=2)

    if 'AA' in isa:
        punane = PhotoImage(file="punane.gif")
        silt = ttk.Label(raam, image=punane)
        silt.image = punane
        silt.grid(row = 14, column = 3) 	 
    elif 'aa' in isa:
        valge = PhotoImage(file="valge.gif")
        silt=ttk.Label(raam, image=valge)
        silt.image = valge
        silt.grid(row=14, column=3)
    elif 'Aa' in isa:
        roosa = PhotoImage(file="roosa.gif")
        silt=ttk.Label(raam, image=roosa)
        silt.image = roosa
        silt.grid(row=14, column=3)
        
    silt=ttk.Label(raam, text=('Järglased:'), wraplength=1000)
    silt.grid(row=15, column=0)

    punane = PhotoImage(file="punane.gif")
    silt = ttk.Label(raam, text=('AA:', fenotüüp['punane']), image=punane)
    silt.image = punane
    silt.grid(row = 15, column = 1)

    valge = PhotoImage(file="valge.gif")
    silt=ttk.Label(raam, text=('aa:', fenotüüp['valge']), image=valge)
    silt.image = valge
    silt.grid(row = 15, column = 3)

    roosa = PhotoImage(file="roosa.gif")
    silt=ttk.Label(raam, text=('Aa:', fenotüüp['roosa']), image=roosa)
    silt.image = roosa
    silt.grid(row = 15, column = 2)

    silt = ttk.Label(raam, text=('AA:', fenotüüp['punane']))
    silt.grid(row = 16, column = 1)

    silt=ttk.Label(raam, text=('Aa:', fenotüüp['roosa']))
    silt.grid(row = 16, column = 2)

    silt=ttk.Label(raam, text=('aa:', fenotüüp['valge']))
    silt.grid(row = 16, column = 3)

nupp = ttk.Button(raam, text="Lahenda:dominantsus", command=lahenda)
nupp.grid(column=1, row=11, sticky=W)

nupp = ttk.Button(raam, text="Lahenda:kodominantsus", command=kodominantsus)
nupp.grid(column=2, row=11,  sticky=(E))


raam.mainloop()


    


