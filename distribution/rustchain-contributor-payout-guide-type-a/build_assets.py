# SPDX-License-Identifier: MIT
from __future__ import annotations
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
VOICE=ROOT/"voiceover"
VIS=ROOT/"visuals"

def f(size,bold=False):
    for p in [
      "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
      "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"]:
        if Path(p).exists(): return ImageFont.truetype(p,size)
    return ImageFont.load_default()

def wrap(d,text,font,maxw):
    lines=[]; cur=""
    for w in text.split():
        trial=(cur+" "+w).strip()
        if d.textbbox((0,0),trial,font=font)[2] <= maxw: cur=trial
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def card(path,title,bullets,footer):
    im=Image.new("RGB",(1920,1080),(24,20,32)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((90,80,1830,1000),radius=44,outline=(133,111,153),width=4)
    d.text((150,145),title,font=f(64,True),fill=(244,240,248)); y=285
    for b in bullets:
        d.text((155,y),"•",font=f(40,True),fill=(218,198,235))
        for line in wrap(d,b,f(38),1450):
            d.text((215,y),line,font=f(38),fill=(235,230,240)); y+=55
        y+=24
    d.text((150,920),footer,font=f(28),fill=(188,176,199)); im.save(path,optimize=True)

def thumb(path,top,bottom,sub):
    im=Image.new("RGB",(1280,720),(24,20,32)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((55,55,1225,665),radius=38,outline=(133,111,153),width=4)
    d.text((95,150),top,font=f(70,True),fill=(244,240,248))
    d.text((95,255),bottom,font=f(70,True),fill=(244,240,248))
    d.text((100,500),sub,font=f(34),fill=(198,184,210)); im.save(path,optimize=True)

def main():
    VIS.mkdir(exist_ok=True)
    for src in sorted(VOICE.glob("[0-9][0-9]-*.txt")):
        subprocess.run(["espeak","-v","en-gb","-s","150","-f",str(src),"-w",str(src.with_suffix(".wav"))],check=True)
    cards=[
      ("01-path.png","CONTRIBUTION PATH",["Open issue → focused branch → test → PR → review → merge","Payment happens after acceptance, not before engineering starts"],"Source: RustChain CONTRIBUTING.md"),
      ("02-wallet.png","WALLET TIMING",["RTC wallet is not required before opening the PR","After merge: project asks for payout destination"],"Source: CONTRIBUTING.md + merged PR #8271"),
      ("03-quality.png","EVIDENCE > VOLUME",["Test the exact area changed","Use live read-only endpoints when relevant","No fake screenshots, placeholder data, or untested bulk PRs"],"Source: RustChain CONTRIBUTING.md"),
      ("04-bcos.png","BCOS CHECK",["BCOS-L1: normal features/refactors","BCOS-L2: wallet, transfer, consensus, rewards, auth, crypto, supply-chain","Docs-only PRs are exempt; new code needs SPDX"],"Source: RustChain CONTRIBUTING.md"),
      ("05-scope.png","KEEP IT SMALL",["One focused issue per PR","Run the closest relevant tests","Miner-file edits must refresh miners/checksums.sha256"],"Source: RustChain CONTRIBUTING.md"),
      ("06-payout.png","PAYOUT AUTHORITY",["Valid authority: @Scottcjn or clearly labeled project automation","Automation evidence requires matching project-issued pending ID + transaction hash"],"Source: RustChain CONTRIBUTING.md"),
      ("07-close.png","FASTEST PATH = AUDITABLE",["Small scope","Real test evidence","Clear merge","Clear payout handoff"],"Package author: @mdmcl-pixel"),
      ("08-sources.png","VERIFY BEFORE PUBLISH",["CONTRIBUTING.md","Rustchain PR #8271","github.com/Scottcjn/Rustchain"],"All claims mapped in SOURCES.md")]
    for x in cards: card(VIS/x[0],x[1],x[2],x[3])
    thumb(ROOT/"thumbnail.png","FIRST PR","TO RTC PAYOUT","RustChain contributor workflow")
    thumb(ROOT/"thumbnail-alt-1.png","DON'T LET","PAYOUT SETUP BLOCK","your RustChain PR")
    thumb(ROOT/"thumbnail-alt-2.png","PR → MERGE","WALLET → PAYOUT","A documented workflow")

if __name__=="__main__": main()
