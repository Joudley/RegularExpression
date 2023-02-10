import re

fraz = "Lamour #Joudley aime le  #sport #"
pattern = "#\w+"

nfraz= re.sub(pattern, lambda x: f"<a href=''>{x.group()}</a>", fraz)
print(nfraz)