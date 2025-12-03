import requests
import time
import base64
import argparse
import re

# ============== PAYLOAD ============== #
Main_payload = r"""
__/\\\\____________/\\\\_______________________________________________________________        
 _\/\\\\\\________/\\\\\\_______________________________________________________________       
  _\/\\\//\\\____/\\\//\\\_____________________________________/\\\______________________      
   _\/\\\\///\\\/\\\/_\/\\\___/\\\\\\\\\______/\\/\\\\\\_____/\\\\\\\\\\\___/\\\\\\\\\____     
    _\/\\\__\///\\\/___\/\\\__\////////\\\____\/\\\////\\\___\////\\\////___\////////\\\___    
     _\/\\\____\///_____\/\\\____/\\\\\\\\\\___\/\\\__\//\\\_____\/\\\_________/\\\\\\\\\\__   
      _\/\\\_____________\/\\\___/\\\/////\\\___\/\\\___\/\\\_____\/\\\_/\\____/\\\/////\\\__  
       _\/\\\_____________\/\\\__\//\\\\\\\\/\\__\/\\\___\/\\\_____\//\\\\\____\//\\\\\\\\/\\_ 
        _\///______________\///____\////////\//___\///____\///_______\/////______\////////\//__"""

Exit_payload = r"""
_____/\\\\\\\\\\\\_____________________________________/\\\_____________/\\\_____________________________________        
 ___/\\\//////////_____________________________________\/\\\____________\/\\\_____________________________________       
  __/\\\________________________________________________\/\\\____________\/\\\___________/\\\__/\\\________________      
   _\/\\\____/\\\\\\\_____/\\\\\________/\\\\\___________\/\\\____________\/\\\__________\//\\\/\\\______/\\\\\\\\__     
    _\/\\\___\/////\\\___/\\\///\\\____/\\\///\\\____/\\\\\\\\\____________\/\\\\\\\\\_____\//\\\\\_____/\\\/////\\\_    
     _\/\\\_______\/\\\__/\\\__\//\\\__/\\\__\//\\\__/\\\////\\\____________\/\\\////\\\_____\//\\\_____/\\\\\\\\\\\__   
      _\/\\\_______\/\\\_\//\\\__/\\\__\//\\\__/\\\__\/\\\__\/\\\____________\/\\\__\/\\\__/\\_/\\\_____\//\\///////___  
       _\//\\\\\\\\\\\\/___\///\\\\\/____\///\\\\\/___\//\\\\\\\/\\___________\/\\\\\\\\\__\//\\\\/_______\//\\\\\\\\\\_ 
        __\////////////_______\/////________\/////______\///////\//____________\/////////____\////__________\//////////__"""
# ============== PAYLOAD ============== #



parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', dest='url', default=None, help='Url to exploit')
parser.add_argument('-c', '--cookie', dest='cookie', default=None, help='Delicious cookie')
parser.add_argument('-H', '--header', dest='header', default=None, help='Header for the post request')
parser.add_argument('-b', '--body', dest='body', default=None, help='Body if needed')
args = parser.parse_args()

def extract_names(html):
    forms = re.findall(r"<form[\s\S]*?</form>", html, flags=re.IGNORECASE)
    for form in forms:
        names = []
        names += re.findall(r'name=["\']([^"\']+)["\']', form, flags=re.IGNORECASE)
        names += re.findall(r'name=([^"\'>\s]+)', form, flags=re.IGNORECASE)
    return names

def upload(url):
    html = requests.get(url).text
    var = extract_names(html)
    return var



if args.url:
    print(f"[+] Exploit {args.url}")
    response = upload(args.url)
    if len(response) >= 2:
        for idx, var in enum(response):
            print(f"[{idx}] {var}")
    elif len(response) == 0:
        print("[!] No variable  or form found, specify with (-v | --var)")

    import requests

def upload_files(url, files_dict, extra_params=None):

    files = {}
    
    for field, info in files_dict.items():
        content = info["content"]
        if isinstance(content, str):
            content = content.encode()

        files[field] = (info["file_name"], content, info["mime"])
    url = args.url
    r = requests.post(url, files=files, data=extra_params or {})
    return r
      
payloads = {
    "file1": {
        "file_name": "sample.txt",
        "mime": "text/plain",
        "content": "Ceci est un test."
    },
    "file2": {
        "file_name": "image.fake.jpg",
        "mime": "image/jpeg",
        "content": b"\xff\xd8\xff\xe0"  # header JPEG
    }
}

resp = upload_files(
    url="http://test.local/upload",
    files_dict=payloads,
    extra_params={"submit": "OK"}
)

print(resp.status_code)
print(resp.text[:500])

else:
    print("[!] You need to specify an url (-u | --url)")
