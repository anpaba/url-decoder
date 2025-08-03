import sys, base64, re, urllib.parse

try: import readline
except ImportError: pass

G="\033[92m";R="\033[91m";W="\033[97m";N="\033[0m"

def is_url(txt):
    return txt.startswith(('http://','https://'))

def decode(url):
    q = urllib.parse.parse_qs(urllib.parse.urlparse(url.strip()).query)
    cands=[re.sub(r'[\?\&#]+$','',v) for vals in q.values() for v in vals]
    cands+=re.findall(r'[A-Za-z0-9+/=_-]{8,}',url)
    for c in cands:
        try:
            d=base64.urlsafe_b64decode(c+'='*(-len(c)%4)).decode()
            if d.startswith(('http://','https://')):
                return d
        except:
            continue
    return None

def process(u):
    if not is_url(u):
        print(f"{R}URL tidak valid{N}\n"); return
    dec = decode(u)
    print(f"{G}{dec}{N}\n" if dec else f"{R}URL tidak didukung{N}\n")

if __name__=="__main__":
    if len(sys.argv)>1:
        for u in sys.argv[1:]:
            process(u)
    else:
        while True:
            try:
                u=input(f"{W}> {N}").strip()
            except (KeyboardInterrupt, EOFError):
                print(f"\n{R}Keluar...{N}"); break
            if not u: continue
            if u.lower()=="exit": break
            process(u)