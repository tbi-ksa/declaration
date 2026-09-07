# Build the standalone GitHub Pages index.html from declaration.html (artifact source).
import sys,re
src=open(__import__('os').path.join(__import__('os').path.dirname(__file__),'declaration.html')).read(); t=src
def rep(old,new):
    global t
    assert t.count(old)==1,old[:60]; t=t.replace(old,new)
rep("""    if(!dl){flash('err','Saving files is not available in this view. Open the page in the Claude app or browser and try again.');btn.disabled=false;return;}""",
"""    if(!dl){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([bytes],{type:'application/pdf'}));a.download=fname;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove();},2000);flash('ok','Saved as '+fname+'. Send it to TBI admissions with your application.');btn.disabled=false;return;}""")
rep("const PAGE_URL=ARTIFACT_URL;","const PAGE_URL='https://tbi-ksa.github.io/declaration/';")
ff="""/* self-hosted brand faces (same set as tbi-ksa/insights) */
@font-face{font-family:"Avenir Next";src:url("fonts/Avenir_Next_Regular.otf") format("opentype");font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:"Avenir Next";src:url("fonts/Avenir_Next_Italic.otf") format("opentype");font-weight:400;font-style:italic;font-display:swap}
@font-face{font-family:"Avenir Next";src:url("fonts/Avenir_Next_Medium.otf") format("opentype");font-weight:500;font-style:normal;font-display:swap}
@font-face{font-family:"Avenir Next";src:url("fonts/Avenir_Next_Demi.otf") format("opentype");font-weight:600;font-style:normal;font-display:swap}
@font-face{font-family:"Avenir Next";src:url("fonts/Avenir_Next_Bold.otf") format("opentype");font-weight:700;font-style:normal;font-display:swap}
@font-face{font-family:"Segoe UI";src:url("fonts/SegoeUI.woff2") format("woff2");font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:"Segoe UI";src:url("fonts/SegoeUI-Italic.woff2") format("woff2");font-weight:400;font-style:italic;font-display:swap}
@font-face{font-family:"Segoe UI";src:url("fonts/SegoeUI-SemiBold.woff2") format("woff2");font-weight:600;font-style:normal;font-display:swap}
@font-face{font-family:"Segoe UI";src:url("fonts/SegoeUI-Bold.woff2") format("woff2");font-weight:700;font-style:normal;font-display:swap}
@font-face{font-family:"TBI Label";src:url("fonts/Klein-Bold.otf") format("opentype");font-weight:400 900;font-style:normal;font-display:swap}
:root{"""
rep('<style>\n:root{','<style>\n'+ff)
rep('--font-label:"Avenir Next","Segoe UI",system-ui,sans-serif;','--font-label:"TBI Label","Avenir Next","Segoe UI",system-ui,sans-serif;')
t=t.replace('<meta charset="utf-8">\n','')
head="""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Fill, sign and stamp the TBI Executive PGDBM entrepreneur declaration of experience on your company letterhead and save it as a PDF.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="TBI Saudi Executive Education">
<meta property="og:title" content="Entrepreneur declaration of experience · TBI Executive PGDBM">
<meta property="og:description" content="Fill, sign and stamp your declaration on company letterhead and save a signed PDF in minutes. Pearson UK Level 7 applicant form.">
<meta property="og:url" content="https://tbi-ksa.github.io/declaration/">
<meta property="og:image" content="https://tbi-ksa.github.io/declaration/assets/og-card.png">
<meta property="og:image:secure_url" content="https://tbi-ksa.github.io/declaration/assets/og-card.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="TBI Saudi Executive Education - Entrepreneur declaration of experience">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Entrepreneur declaration of experience · TBI Executive PGDBM">
<meta name="twitter:description" content="Fill, sign and stamp your declaration on company letterhead and save a signed PDF in minutes.">
<meta name="twitter:image" content="https://tbi-ksa.github.io/declaration/assets/og-card.png">
<meta name="theme-color" content="#091E3D">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
"""
i=t.index('</style>')+len('</style>')
out=head+t[:i]+'\n</head>\n<body>\n'+t[i:]+'\n</body>\n</html>\n'
open(sys.argv[1],'w').write(out); print('built',sys.argv[1],len(out))
