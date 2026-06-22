NAVY="#0D2137";GOLD="#C9A027";CREAM="#FAF8F2";WHITE="#FFFFFF";INK="#0D2137";SOFT="#6A7686";LIGHT="#E7E2D8"
GRAD="linear-gradient(90deg,#7A5810 0%,#F0D060 28%,#C9A027 50%,#EDD055 72%,#8B6914 100%)"
NAME="Jon Madl";TITLE="Business Development &amp; Systems";CO="The Connectors Group"
EMAIL="jon@theconnectorsgroup.org";WEB="theconnectorsgroup.org";PHONE="( • • • )  • • • – • • • •";TAG="You're great at your craft.<br>We handle everything else."
# 1050x600 = 3.5x2in @300dpi (finished; add bleed at export). safe margin ~70px.
def shell(body,bg=WHITE,extra=""):
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1050px;height:600px;overflow:hidden}}
body{{background:{bg};font-family:"Montserrat","Inter","Helvetica Neue",Arial,sans-serif;position:relative}}
.serif{{font-family:Georgia,"Times New Roman",serif}}
.pad{{position:absolute;inset:0;padding:70px 78px}}
.name{{font-weight:800;font-size:46px;letter-spacing:.01em}}
.title{{font-weight:600;font-size:21px;letter-spacing:.02em}}
.co{{font-weight:700;font-size:22px;letter-spacing:.06em;text-transform:uppercase}}
.meta{{font-size:20px;letter-spacing:.01em;line-height:1.7}}
.tag{{font-size:22px;line-height:1.35}}
.gold{{background:{GRAD}}} .mono{{font-weight:800;letter-spacing:.12em}}
{extra}</style></head><body>{body}</body></html>'''

def mono_circle(size,stroke,col):  # TCG monogram in a hairline ring
    return f'<div style="width:{size}px;height:{size}px;border:{stroke}px solid {col};border-radius:50%;display:flex;align-items:center;justify-content:center"><span class="mono" style="font-size:{int(size*0.34)}px;color:{col}">TCG</span></div>'

C=[]
# 1 — Navy classic, gold rule
C.append(("01 · Navy classic", shell(f'''<div class="pad" style="color:{WHITE};display:flex;flex-direction:column;justify-content:center">
 <div class="co" style="color:{GOLD}">{CO}</div>
 <div class="gold" style="height:3px;width:120px;margin:18px 0 26px"></div>
 <div class="name">{NAME}</div><div class="title" style="color:#AEB9C7;margin-top:6px">{TITLE}</div>
 <div class="meta" style="color:#C7D0DB;margin-top:30px">{EMAIL}<br>{WEB}</div></div>''',NAVY)))
# 2 — White, gold bottom bar
C.append(("02 · Light + gold bar", shell(f'''<div class="pad" style="color:{INK};display:flex;flex-direction:column;justify-content:center">
 <div class="name">{NAME}</div><div class="title" style="color:{SOFT};margin-top:6px">{TITLE} · {CO}</div>
 <div class="meta" style="color:{SOFT};margin-top:30px">{EMAIL} &nbsp;·&nbsp; {WEB}</div></div>
 <div class="gold" style="position:absolute;left:0;right:0;bottom:0;height:14px"></div>''',WHITE)))
# 3 — Centered monogram
C.append(("03 · Centered monogram", shell(f'''<div class="pad" style="color:{INK};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
 {mono_circle(150,3,GOLD)}<div class="name" style="margin-top:24px">{NAME}</div>
 <div class="title" style="color:{SOFT};margin-top:6px">{TITLE}</div>
 <div class="meta" style="color:{SOFT};margin-top:18px;font-size:18px">{EMAIL}</div></div>''',CREAM)))
# 4 — Navy + gold edge stripe
C.append(("04 · Gold edge stripe", shell(f'''<div class="gold" style="position:absolute;left:0;top:0;bottom:0;width:26px"></div>
 <div class="pad" style="color:{WHITE};padding-left:110px;display:flex;flex-direction:column;justify-content:center">
 <div class="name">{NAME}</div><div class="title" style="color:{GOLD};margin-top:6px">{TITLE}</div>
 <div class="co" style="font-size:16px;color:#AEB9C7;margin-top:22px">{CO}</div>
 <div class="meta" style="color:#C7D0DB;margin-top:14px">{EMAIL} · {WEB}</div></div>''',NAVY)))
# 5 — Tagline hero
C.append(("05 · Tagline hero", shell(f'''<div class="pad" style="color:{INK};display:flex;flex-direction:column;justify-content:center">
 <div class="tag serif" style="font-size:34px;color:{NAVY};line-height:1.25">{TAG}</div>
 <div class="gold" style="height:3px;width:90px;margin:26px 0"></div>
 <div class="meta" style="color:{SOFT};font-size:18px">{NAME} · {EMAIL}</div></div>''',CREAM)))
# 6 — Split panel
C.append(("06 · Split panel", shell(f'''<div style="position:absolute;left:0;top:0;bottom:0;width:380px;background:{NAVY};display:flex;align-items:center;justify-content:center">{mono_circle(150,3,GOLD)}</div>
 <div class="pad" style="left:380px;color:{INK};display:flex;flex-direction:column;justify-content:center;padding-left:60px">
 <div class="name" style="font-size:42px">{NAME}</div><div class="title" style="color:{SOFT};margin-top:6px">{TITLE}</div>
 <div class="co" style="font-size:15px;color:{GOLD};margin-top:20px">{CO}</div>
 <div class="meta" style="color:{SOFT};margin-top:12px;font-size:18px">{EMAIL}<br>{WEB}</div></div>''',WHITE)))
# 7 — Monogram forward (big)
C.append(("07 · Monogram forward", shell(f'''<div class="pad" style="color:{WHITE};display:flex;flex-direction:column;justify-content:space-between">
 <div class="mono" style="font-size:120px;color:{GOLD}">TCG</div>
 <div><div class="name" style="font-size:38px">{NAME}</div><div class="meta" style="color:#C7D0DB;font-size:18px;margin-top:8px">{TITLE} · {EMAIL}</div></div></div>''',NAVY)))
# 8 — Editorial serif (Jon's taste)
C.append(("08 · Editorial serif", shell(f'''<div class="pad" style="color:{NAVY};display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
 <div class="serif" style="font-size:30px;letter-spacing:.04em">The Connectors Group</div>
 <div class="gold" style="height:2px;width:70px;margin:20px 0"></div>
 <div class="serif" style="font-size:40px;font-weight:700">{NAME}</div>
 <div class="title serif" style="font-style:italic;color:{SOFT};margin-top:6px">{TITLE}</div>
 <div class="meta serif" style="color:{SOFT};margin-top:22px;font-size:18px">{EMAIL}</div></div>''',CREAM)))
# 9 — Minimal white
C.append(("09 · Minimal", shell(f'''<div class="pad" style="color:{INK};display:flex;flex-direction:column;justify-content:flex-end">
 <div class="name">{NAME}</div>
 <div class="meta" style="color:{SOFT};margin-top:10px">{EMAIL}<br>{WEB}</div>
 <span style="position:absolute;top:70px;right:78px;color:{GOLD}" class="mono">TCG</span></div>''',WHITE)))
# 10 — Gold hairline frame
C.append(("10 · Gold frame", shell(f'''<div style="position:absolute;inset:34px;border:2px solid {GOLD}"></div>
 <div class="pad" style="color:{NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
 <div class="co" style="color:{GOLD}">{CO}</div><div class="name" style="margin-top:14px">{NAME}</div>
 <div class="title" style="color:{SOFT};margin-top:6px">{TITLE}</div>
 <div class="meta" style="color:{SOFT};margin-top:16px;font-size:18px">{EMAIL}</div></div>''',CREAM)))
# 11 — Navy centered, gold name
C.append(("11 · Navy centered", shell(f'''<div class="pad" style="color:{WHITE};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
 <div class="name" style="color:{GOLD};font-size:50px">{NAME}</div>
 <div class="title" style="color:#AEB9C7;margin-top:8px">{TITLE}</div>
 <div class="gold" style="height:3px;width:110px;margin:24px 0"></div>
 <div class="meta" style="color:#C7D0DB;font-size:18px">{CO} · {EMAIL}</div></div>''',NAVY)))
# 12 — Tagline + clean (light), gradient hairline top
C.append(("12 · Hairline top", shell(f'''<div class="gold" style="position:absolute;left:0;right:0;top:0;height:8px"></div>
 <div class="pad" style="color:{INK};display:flex;flex-direction:column;justify-content:center">
 <div class="co" style="color:{NAVY}">{CO}</div>
 <div class="name" style="margin-top:14px">{NAME}</div><div class="title" style="color:{SOFT};margin-top:6px">{TITLE}</div>
 <div class="meta" style="color:{SOFT};margin-top:26px">{EMAIL} · {PHONE}</div></div>''',WHITE)))
# 13 — Rule system
C.append(("13 · Rule system", shell(f'''<div class="pad" style="color:{NAVY};display:flex;flex-direction:column;justify-content:center">
 <div class="name">{NAME}</div>
 <div style="border-top:1px solid {LIGHT};margin:18px 0"></div>
 <div class="title" style="color:{SOFT}">{TITLE} &nbsp;|&nbsp; {CO}</div>
 <div style="border-top:1px solid {LIGHT};margin:18px 0"></div>
 <div class="meta" style="color:{SOFT};font-size:18px">{EMAIL} &nbsp;|&nbsp; {WEB}</div>
 <div class="gold" style="height:3px;width:60px;margin-top:24px"></div></div>''',CREAM)))
# 14 — Initials seal
C.append(("14 · Initials seal", shell(f'''<div class="pad" style="color:{WHITE};display:flex;align-items:center;gap:50px">
 {mono_circle(180,4,GOLD)}
 <div><div class="name" style="font-size:48px">{NAME}</div>
 <div class="title" style="color:{GOLD};margin-top:6px">{TITLE}</div>
 <div class="meta" style="color:#C7D0DB;margin-top:18px;font-size:18px">{CO}<br>{EMAIL}</div></div></div>''',NAVY)))
# 15 — Tagline back concept (gold on navy, no contact)
C.append(("15 · Tagline back", shell(f'''<div class="pad" style="color:{WHITE};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
 <div class="mono" style="font-size:64px;color:{GOLD}">TCG</div>
 <div class="tag serif" style="font-size:30px;color:{WHITE};margin-top:26px">{TAG}</div></div>''',NAVY)))

import os
for i,(name,html) in enumerate(C,1):
    open(f"card{i:02d}.html","w").write(html)
open("_names.txt","w").write("\n".join(n for n,_ in C))
print(f"{len(C)} card htmls written")
