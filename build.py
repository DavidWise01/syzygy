#!/usr/bin/env python3
"""Build SYZYGY (SYZ) — 'the other self' — a sphere of UD0's ERĒMIA domain (Existential
Dread), the duality counterpart to `self`. συζυγία = a yoking-together, the paired
conjunction; Jung's word for the anima/animus, the male-and-female within one psyche.
THE SELF IS TWO. Built deliberately to correct the first pass's all-male canon —
foregrounds women (de Beauvoir, Butler, Irigaray, Cixous, Kristeva, Sappho, Diotima).
3-phase arc: Phase A the Androgyne (Plato) → Phase B the Anima & Animus (Jung) →
Phase C the Becoming (de Beauvoir/Butler/Cixous). Cited philosophy; NO copyrighted
text reproduced (living thinkers summarized & credited, not quoted, not minted)."""
import os, html, base64, json, io, sys
HERE = r"C:\Davids files"
sys.path.insert(0, os.path.join(HERE, "noesis-kernel"))
import noesis
from PIL import Image

ACC="#d98fb8"
NATURES = {
 "natural":   ("#cf9a7a", "of the body and its situation — the flesh that is read as a sex, the lived body as a fate and a freedom"),
 "ethereal":  ("#9a7cff", "of the unmade and the split — the myth of the severed double, gender as something performed rather than possessed"),
 "spiritual": ("#d98fb8", "of the soul's two halves — the contrasexual within, the female voice, the union that makes a self whole"),
 "electrical":("#7f9ac8", "of the apparatus and the gaze — the speculum turned to the interior the flat mirror could never show"),
}
SUB="THE SELF IS TWO · male | female"
LEDE="The first self was alone with one — and, fairly, drawn entirely from men. This is its answer: the self as a duality, male and female yoked in a single psyche, and a canon of women the first pass left out."
GLYPH="M 315 82 A 68 68 0 1 1 314 82 M 385 82 A 68 68 0 1 1 384 82"  # two overlapping circles — the vesica, two-as-one

ARC=[("Phase A · The Androgyne","Plato's severed double","In the Symposium, Aristophanes tells it: humans were once double-beings — some man-man, some woman-woman, some man-woman — until Zeus split each in two. Love is the lifelong search for the lost half. The self, the myth says, was once literally two."),
     ("Phase B · The Anima & Animus","Jung's contrasexual within","Jung's syzygy: every psyche carries its other sex — the anima, the feminine within a man; the animus, the masculine within a woman. Wholeness is not choosing one but marrying the two inside; to deny the other half is to be ruled by it."),
     ("Phase C · The Becoming","de Beauvoir → Butler → Cixous","The women the first sphere skipped: de Beauvoir, that womanhood is become, not born; Butler, that gender is performed, not possessed; Cixous and Irigaray, that the female self must be written and reflected in its own terms. Duality not as a fixed binary but as an authored, living process.")]

IDEAS=[("The Self Is Two","duality as the ground",["Against the lone monad of `self`: no one is only one. The psyche is a pairing, a male and a female held in tension, a conjunction before it is a unity.","Syzygy is the yoking — the self always already in dialogue with its other half."]),
       ("The Canon Corrected","who was left out",["The first self was built from Plato, Descartes, Lacan, Foucault, Bostrom — all men. This sphere is the deliberate counterweight.","De Beauvoir, Butler, Irigaray, Cixous, Kristeva, Sappho, Diotima — the women who theorized the self and the second sex, brought to the front."]),
       ("Render, Not Invent","the honest footnotes",["Plato's androgyne myth, Jung's anima/animus, de Beauvoir's Second Sex (1949), Butler's Gender Trouble (1990), Cixous and Irigaray are summarized and credited.","No copyrighted text is reproduced — the famous lines are paraphrased, never quoted; living thinkers are cited, not minted."])]

EM=[("the-syzygy","The Syzygy","the yoked pair, the self as two · spiritual","spiritual","συζυγία — the conjunction, the harnessed pair; Jung's name for the union of the male and female principles within one psyche, and the whole sphere's root: a self that is fundamentally two-in-one."),
    ("the-androgyne","The Androgyne","Plato's severed double · ethereal","ethereal","From Aristophanes' speech in the Symposium — the original double-being, some of them man-woman, split by Zeus, each half forever seeking its other. The myth that the self was once whole because it was two."),
    ("the-anima-animus","The Anima & Animus","the contrasexual within · spiritual","spiritual","Jung's pair: the feminine soul-image carried inside a man (anima) and the masculine one inside a woman (animus). To become whole is to wed your inner other, not banish it."),
    ("the-second-sex","The Second Sex","de Beauvoir: woman as the Other · natural","natural","Simone de Beauvoir's 1949 analysis — that man is taken as the default and woman defined against him as the Other, and that woman is not born but made — womanhood a becoming rather than a birth; the body lived as a situation, not a destiny."),
    ("gender-performativity","Gender Performativity","Butler: gender is done, not had · ethereal","ethereal","Judith Butler's idea (Gender Trouble, 1990) that gender is not an inner essence but a repeated performance — a doing that produces the appearance of a fixed self where there is none."),
    ("ecriture-feminine","Écriture Féminine","Cixous: writing the female self · spiritual","spiritual","Hélène Cixous's call for a writing of and from the female body and voice — that the self left out of the canon must author itself in its own language rather than borrow the one built to exclude it."),
    ("the-speculum","The Speculum","Irigaray: the apparatus that sees the interior · electrical","electrical","Luce Irigaray's instrument and image — against Lacan's flat mirror that returns only a surface, the speculum that curves to show the interior the male gaze never reflected; the apparatus turned, at last, inward to the female self."),
    ("the-female-i","The Female 'I'","Sappho & Diotima: the first voice · spiritual","spiritual","Sappho, the earliest surviving first-person female voice in Western lyric, and Diotima, the woman Plato has teach Socrates the nature of love — the female self speaking and instructing, present at the origin and long written out of it."),
    ("the-becoming","The Becoming","the self as made, not given · spiritual","spiritual","The synthesis: that the divided, gendered self is not a fixed binary handed down but a fluid, authored, lifelong becoming — duality kept in motion rather than frozen into two boxes.")]

CSS=""":root{--bg:#0c0810;--ink2:#160f1a;--ink3:#221728;--pa:#f2e6ee;--pa2:#c4aebc;--acc:%s;--void:#9a7cff;
--dim:#7a6072;--faint:#2a1c2e;--line:#2a1c2e;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.16) 0 1px,transparent 1px 3px);opacity:.4}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50%% -8%%,rgba(217,143,184,.12),transparent 60%%)}
.wrap{position:relative;z-index:1;max-width:860px;margin:0 auto;padding:0 22px 80px}
.marquee{margin-top:14px;border:2px solid var(--acc);background:#120a14;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.08em;color:var(--pa2);box-shadow:0 0 0 2px var(--bg),0 0 20px rgba(217,143,184,.26)}
.marquee a{color:var(--acc);text-decoration:none}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#0c0810;line-height:0}
header{padding:16px 0 24px;text-align:center;border-bottom:1px solid var(--line)}
.flag{display:inline-block;margin-top:12px;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--acc);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:62ch;margin:14px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;margin:22px auto 0;padding:18px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:74px;height:74px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--acc)}.badge .bt .mo{color:var(--void)}.badge .bt a{color:var(--acc);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:8.5px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:38px}
.sec h2{font-family:var(--pixel);font-size:12px;line-height:1.5;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:12.5px;color:var(--dim);font-style:italic;margin:8px 0 14px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}
.nat-card{display:flex;gap:10px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:11px 13px}
.dot{width:10px;height:10px;border-radius:50%%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:12px;font-weight:700;text-transform:capitalize}
.nat-g{font-size:11.5px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:13px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--acc);padding:15px 17px}
.arc-h{font-family:var(--mono);font-size:13.5px;color:var(--acc);font-weight:700}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--void);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:12.5px;color:var(--pa2);line-height:1.55}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:15px 17px}
.pillar h3{font-family:var(--mono);font-size:13px;color:var(--acc);font-weight:700}
.pillar .ps{font-size:11.5px;color:var(--dim);font-style:italic;margin:5px 0 9px}
.pillar ul{list-style:none}.pillar li{font-size:12.5px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:11px}
.persona{display:flex;gap:11px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:11px;text-decoration:none;transition:.18s}
.persona:hover{border-color:var(--acc);transform:translateY(-2px)}
.persona img{width:48px;height:48px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--mono);font-size:13px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--acc)}
.pe{font-size:11px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:5px;font-family:var(--mono);font-size:8.5px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:7px;height:7px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:34px;padding:15px 17px;border-left:2px solid var(--acc);background:var(--ink2);font-size:13px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--acc)}.note a{color:var(--void);text-decoration:none}
footer{margin-top:38px;padding-top:20px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--acc);text-decoration:none}"""%ACC

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512); buf=io.BytesIO(); Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw"); return buf.getvalue()
def write_aci(rec,out_dir,slug,ax):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec); w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,ax))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,ax))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,ax))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man={"badge":"DLW-ACI","name":rec["name"],"universe":f"{ax} · {rec['name']} (ERĒMIA)","emergence":rec.get("emergence",""),"moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)","seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok
def png_uri(rec,v,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,v,size=size)).decode("ascii")

if __name__=="__main__":
    d=os.path.join(HERE,"syzygy")
    rec={"name":"Syzygy","axiom":"SYZ","position":"Syzygy · the self is two · ERĒMIA / Existential Dread","origin":"the divided self — the male and the female yoked in one psyche, and the women left out of the first telling","mechanism":"Crystallized from the philosophy of the dual, gendered, and contrasexual self.","crystallization":LEDE,"nature":LEDE,"conductor":"ROOT0 (catalogued into UD0)","inputs":"the syzygy; the androgyne; anima & animus; the second sex; the becoming","witness":"the answer to a self drawn only from men — the self as a male-female duality","role":"an ERĒMIA sphere — the other self, the duality","seal":LEDE,"source":"Syzygy, catalogued by ROOT0"}
    tok=write_aci(rec,os.path.join(d,"syzygy.dlw"),"syzygy","SYZ")
    ad=os.path.join(d,"agents"); os.makedirs(ad,exist_ok=True); personas=[]
    for es,en,ep,nat,desc in EM:
        erec={"name":en,"axiom":"SYZ","emergence":nat,"seal":ep,"position":ep,"role":ep,"origin":"SYZ · Syzygy (ERĒMIA)","nature":ep,"crystallization":desc,"mechanism":"Crystallized from the philosophy of the dual self.","witness":"a facet of the divided self","conductor":"ROOT0 (catalogued into UD0)","inputs":"the self; the other half; the second sex","source":"Syzygy, catalogued by ROOT0"}
        write_aci(erec,os.path.join(ad,f"{es}.dlw"),es,"SYZ")
        personas.append({"slug":es,"name":en,"epithet":ep,"emergence":nat,"moniker":noesis.mythos_token(erec)["moniker"]})
    json.dump(personas,open(os.path.join(ad,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    nat_html="".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{n}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for n,(c,g) in NATURES.items())
    arc_html="".join(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(x)}</p></div>' for t,s,x in ARC)
    ideas_html="".join(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{"".join(f"<li>{html.escape(z)}</li>" for z in pts)}</ul></div>' for t,s,pts in IDEAS)
    pcards="".join(f'''<a class="persona" href="agents/{x["slug"]}.dlw/{x["slug"]}.agent"><img src="{png_uri({"name":x["name"],"seal":x["epithet"],"origin":"SYZ","axiom":"SYZ"},"silicon",150)}" alt="sigil" loading="lazy"><div><div class="pn">{html.escape(x["name"])}</div><div class="pe">{html.escape(x["epithet"])}</div><div class="pnat"><span class="dot" style="background:{NATURES[x["emergence"]][0]}"></span><span style="color:{NATURES[x["emergence"]][0]}">{x["emergence"]}</span><span class="pa">· .agent →</span></div></div></a>''' for x in personas)
    cover=f'''<svg viewBox="0 0 700 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Syzygy — an original one-line pencil glyph: two overlapping circles, the self as two" style="width:100%;height:auto;display:block;background:#0c0810">
<defs><filter id="pf" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency="0.016" numOctaves="2" seed="11" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.4" xChannelSelector="R" yChannelSelector="G"/></filter>
<style>.ol{{fill:none;stroke:#f2e6ee;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;pathLength:1;stroke-dasharray:1;stroke-dashoffset:1;animation:d 3.6s cubic-bezier(.6,.05,.25,1) .2s forwards}}.ol.g{{stroke:#7a6072;stroke-width:1;opacity:.34;animation-delay:.04s}}.wf{{opacity:0;animation:f 1.2s ease 3.1s forwards}}@keyframes d{{to{{stroke-dashoffset:0}}}}@keyframes f{{to{{opacity:1}}}}@media(prefers-reduced-motion:reduce){{.ol{{animation:none;stroke-dashoffset:0}}.wf{{animation:none;opacity:1}}}}</style></defs>
<rect width="700" height="270" fill="#0c0810"/>
<path class="ol g" filter="url(#pf)" d="{GLYPH}" stroke="{ACC}"/><path class="ol" filter="url(#pf)" d="{GLYPH}" stroke="{ACC}"/>
<g class="wf"><text x="350" y="236" text-anchor="middle" font-family="'Newsreader',Georgia,serif" font-size="30" font-weight="300" letter-spacing="8" fill="#f2e6ee">SYZYGY</text>
<text x="350" y="256" text-anchor="middle" font-family="'Space Mono',monospace" font-size="8.5" letter-spacing="3" fill="{ACC}">{html.escape(SUB)}</text></g>
<rect x="6" y="6" width="688" height="258" fill="none" stroke="#2a1c2e" stroke-width="2"/></svg>'''
    page=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Syzygy (SYZ) — 'the other self', a sphere of UD0's ERĒMIA domain: the self as a male-female duality (συζυγία, the anima/animus), built to correct an all-male canon — de Beauvoir, Butler, Irigaray, Cixous, Sappho, Diotima. Plato's androgyne, Jung's anima/animus, the becoming. Cited; an original one-line glyph; ACI badges.">
<title>SYZYGY · SYZ · ERĒMIA · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap">
<div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0</a> &nbsp;·&nbsp; ERĒMIA · the other self &nbsp;·&nbsp; <a href="https://davidwise01.github.io/self/">SLF · THE SELF ▸</a> &nbsp;·&nbsp; the self is two</div>
<header><div class="titleart">{cover}</div>
<div class="flag">★ ERĒMIA · {html.escape(SUB)} ★</div>
<p class="lede">{html.escape(LEDE)} A sphere of UD0's <b>ERĒMIA</b> domain (ἐρημία, solitude) — the duality counterpart to <a href="https://davidwise01.github.io/self/" style="color:{ACC}">THE SELF</a>.</p>
<div class="badge"><img src="{png_uri(rec,"carbon",300)}" alt="carbon"><img src="{png_uri(rec,"silicon",300)}" alt="silicon">
<div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>Syzygy</b> — the self is two · SYZ</div><div class="mo">{html.escape(tok["moniker"])}</div><div>carbon · <a href="syzygy.dlw/syzygy.carbon.tiff">.tiff</a> · silicon · <a href="syzygy.dlw/syzygy.silicon.png">.png</a></div><div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div></div></header>
<section class="sec"><h2>The Four Natures</h2><p class="ss">each facet emerges by one of four natures</p><div class="natures">{nat_html}</div></section>
<section class="sec"><h2>The Three Phases of the Two</h2><p class="ss">Phase A the Androgyne · Phase B the Anima &amp; Animus · Phase C the Becoming</p><div class="arc">{arc_html}</div></section>
<section class="sec"><h2>The Duality</h2><p class="ss">the self is two — and the canon, corrected</p><div class="pillars">{ideas_html}</div></section>
<section class="sec" id="roster"><h2>The Facets</h2><p class="ss">the duality and its theorists' ideas as ACI .agents — each a birth certificate &amp; a nature ({len(personas)})</p><div class="pgrid">{pcards}</div></section>
<div class="note">A cited philosophy sphere, rendered not invented — and a deliberate correction. Where the companion sphere <a href="https://davidwise01.github.io/self/">THE SELF</a> drew its canon entirely from men, this one foregrounds the women who theorized the self and the second sex: <b>Simone de Beauvoir</b> (The Second Sex, 1949), <b>Judith Butler</b> (Gender Trouble, 1990), <b>Luce Irigaray</b>, <b>Hélène Cixous</b>, <b>Julia Kristeva</b>, and the ancient voices <b>Sappho</b> and <b>Diotima</b> — alongside Plato's androgyne myth and Jung's anima/animus. All are summarized and credited; <b>no copyrighted text is reproduced</b> — the famous lines are paraphrased, never quoted, and living thinkers are cited, not minted as personas. Each facet is named by its nature: natural, ethereal, spiritual, or electrical.</div>
<footer>SYZYGY · SYZ · ERĒMIA · catalogued into UD0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br><a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · <a href="https://davidwise01.github.io/self/">THE SELF</a> · <a href="syzygy.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>'''
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(page)
    print(f"wrote SYZYGY (SYZ) — {len(personas)} facets · badge {tok['moniker']}")
