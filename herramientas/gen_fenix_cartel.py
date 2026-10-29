"""
Cartel imprimible de «El Fénix sobre el Lago», de José M. Fernández (español e inglés).
La ilustración (fenix-cartel.jpg) trae dos espacios en blanco: arriba va el título
y abajo los datos de la función, que se escriben en la propia página antes de imprimir.
Produce obra-fenix-lago-cartel-es.html y obra-fenix-lago-cartel-en.html.
Uso: python3 gen_fenix_cartel.py
"""
import os

AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTOR = "José M. Fernández"

T = {
 "es": dict(otro="obra-fenix-lago-cartel-en.html", volver="obra-fenix-lago-produccion-es.html", volver_txt="← Guía de producción",
   titulo_pag="El Fénix sobre el Lago · Cartel", inicio="index-es.html", saltar="Saltar al contenido", idioma_lbl="Idioma",
   instr="Escriba en los espacios punteados (haga clic sobre ellos) el nombre de la escuela, la fecha, la hora, el lugar y la ciudad. Después pulse «Imprimir». Se imprime en una hoja carta, en vertical.",
   imprimir="🖨️ Imprimir el cartel",
   escuela="Nombre de la escuela", presenta="presenta", titulo="El Fénix sobre el Lago",
   sub="La historia del Gran Incendio de Chicago", obra=f"Obra de {AUTOR}",
   elenco="Con todos los alumnos, de prekínder a 6.º grado",
   lbl_fecha="Día", lbl_hora="Hora", lbl_lugar="Lugar", fecha="Día y fecha", hora="Hora", lugar="Lugar",
   ciudad="Ciudad, estado", entrada="Entrada libre",
   alt="Al amanecer, un fénix dorado vuela sobre el lago Michigan junto a la Torre de Agua de Chicago. En la orilla, niños disfrazados con los papeles de la obra lo miran felices: un niño vestido de vaca, llamitas con capas rojas y naranjas, niños que sostienen la tela azul del río y agitan cintas como el viento, vecinos de 1871 con maletas, un bombero con una linterna y un arquitecto con planos.",
   pie=f"«El Fénix sobre el Lago» · Obra de {AUTOR} · Lumi, www.lumi-educa.com · CC BY-NC-SA 4.0"),
 "en": dict(otro="obra-fenix-lago-cartel-es.html", volver="obra-fenix-lago-produccion-en.html", volver_txt="← Production guide",
   titulo_pag="The Phoenix on the Lake · Poster", inicio="index.html", saltar="Skip to content", idioma_lbl="Language",
   instr="Type in the dotted spaces (click on them) the name of the school, the date, the time, the place and the city. Then press “Print”. It prints on one letter-size sheet, portrait.",
   imprimir="🖨️ Print the poster",
   escuela="School name", presenta="presents", titulo="The Phoenix on the Lake",
   sub="The Story of the Great Chicago Fire", obra=f"A play by {AUTOR}",
   elenco="With all our students, from Pre-K to 6th grade",
   lbl_fecha="Date", lbl_hora="Time", lbl_lugar="Place", fecha="Day and date", hora="Time", lugar="Place",
   ciudad="City, State", entrada="Free admission",
   alt="At dawn, a golden phoenix flies over Lake Michigan next to the Chicago Water Tower. On the shore, children dressed as the characters of the play look up happily: a child dressed as a cow, little flames in red and orange capes, children holding the blue river cloth and waving ribbons as the wind, 1871 residents with suitcases, a firefighter with a lantern and an architect with blueprints.",
   pie=f"“The Phoenix on the Lake” · A play by {AUTOR} · Lumi, www.lumi-educa.com · CC BY-NC-SA 4.0"),
}

def pagina(L):
    t = T[L]
    idioma = (f'<span aria-current="true">Español</span><a href="{t["otro"]}" lang="en" hreflang="en">English</a>' if L == "es"
              else f'<a href="{t["otro"]}" lang="es" hreflang="es">Español</a><span aria-current="true">English</span>')
    campo = lambda cls, ph: f'<span class="campo {cls}" contenteditable="true" role="textbox" aria-label="{ph}" data-ph="{ph}"></span>'
    return f'''<!doctype html>
<!-- Cartel de «El Fénix sobre el Lago» · Obra de {AUTOR} · Lumi · CC BY-NC-SA 4.0 · generado con herramientas/gen_fenix_cartel.py -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["titulo_pag"]} · Lumi</title>
<meta name="author" content="{AUTOR}">
<link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="lumi.css?v=6">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;700&display=swap" rel="stylesheet">
<style>
 .ayuda{{max-width:820px;margin:1rem auto;padding:0 16px}}
 .ayuda button{{display:inline-flex;align-items:center;min-height:44px;padding:0 1rem;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);font:inherit;font-weight:700;cursor:pointer}}
 .cartel{{position:relative;width:min(640px,100%);margin:0 auto 2rem;aspect-ratio:848/1264;container-type:inline-size;border-radius:14px;overflow:hidden;box-shadow:0 6px 24px rgba(0,0,0,.18);background:#fbf3e6}}
 .cartel img{{position:absolute;inset:0;width:100%;height:100%;display:block}}
 .c-arriba{{position:absolute;left:7%;right:7%;top:3.2%;height:11.6%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#5a2410}}
 .c-esc{{margin:0;font-size:2.9cqw;font-weight:700;color:#7a3a16}}
 .c-tit{{font-family:Fredoka,system-ui,sans-serif;font-weight:700;font-size:7cqw;line-height:1;margin:.1em 0 .08em;color:#b23a0e}}
 .c-sub{{margin:0;font-size:2.6cqw;color:#5a2410}}
 .c-obra{{margin:.15em 0 0;font-size:2.6cqw;font-weight:700;color:#194F5A}}
 .c-abajo{{position:absolute;left:5%;right:5%;top:85.2%;bottom:1.6%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#3b2a1e}}
 .c-elenco{{margin:0;font-size:3cqw;font-weight:700;color:#194F5A}}
 .c-datos{{display:flex;flex-wrap:wrap;justify-content:center;gap:.2em 1.2em;margin:.45em 0 .3em;font-size:3.1cqw;font-weight:700}}
 .c-datos .lbl{{color:#b23a0e;margin-right:.25em}}
 .c-lugar{{margin:0;font-size:2.6cqw}}
 .campo{{display:inline-block;min-width:5.5em;border-bottom:2px dotted #b23a0e;outline:none;padding:0 .15em}}
 .campo:empty::before{{content:attr(data-ph);color:#8a7a6a;font-weight:400;font-style:italic}}
 .campo:focus{{background:rgba(178,58,14,.08)}}
 @media print{{
  @page{{size:letter portrait;margin:0}}
  html,body{{background:#fbf3e6}} .cabecera,.ayuda,.pie,.saltar{{display:none!important}}
  main{{display:flex;align-items:center;justify-content:center;height:100vh}}
  .cartel{{width:auto;height:100vh;margin:0;border-radius:0;box-shadow:none;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
  .campo,.campo:focus{{border-bottom:0;background:none}} .campo:empty::before{{content:""}}
 }}
</style>
</head>
<body>
<a class="saltar" href="#contenido">{t["saltar"]}</a>
<header class="cabecera">
 <div class="envoltura">
  <a class="marca" href="{t["inicio"]}"><img src="lumi-logo-horizontal.svg" alt="Lumi" width="560" height="240"></a>
  <div class="idioma" role="group" aria-label="{t["idioma_lbl"]}">{idioma}</div>
 </div>
</header>
<div class="ayuda">
 <p style="margin:.4rem 0"><a href="{t["volver"]}">{t["volver_txt"]}</a></p>
 <p>{t["instr"]}</p>
 <p><button type="button" onclick="window.print()">{t["imprimir"]}</button></p>
</div>
<main id="contenido" tabindex="-1">
<article class="cartel" aria-label="{t["titulo_pag"]}">
 <img src="fenix-cartel.jpg" alt="{t["alt"]}" width="1696" height="2528">
 <div class="c-arriba">
  <p class="c-esc">{campo("escuela", t["escuela"])} {t["presenta"]}</p>
  <h1 class="c-tit">{t["titulo"]}</h1>
  <p class="c-sub">{t["sub"]}</p>
  <p class="c-obra">{t["obra"]}</p>
 </div>
 <div class="c-abajo">
  <p class="c-elenco">{t["elenco"]}</p>
  <div class="c-datos">
   <span><span class="lbl">{t["lbl_fecha"]}:</span>{campo("fecha", t["fecha"])}</span>
   <span><span class="lbl">{t["lbl_hora"]}:</span>{campo("hora", t["hora"])}</span>
   <span><span class="lbl">{t["lbl_lugar"]}:</span>{campo("lugar", t["lugar"])}</span>
  </div>
  <p class="c-lugar">{campo("ciudad", t["ciudad"])} · {t["entrada"]}</p>
 </div>
</article>
</main>
<footer class="pie"><div class="envoltura"><p>{t["pie"]}</p></div></footer>
<script>
(function(){{
  var K="fenix-cartel-"+document.documentElement.lang, cs=document.querySelectorAll(".campo");
  function clave(c){{ return c.className.split(" ")[1]; }}
  try{{ var g=JSON.parse(localStorage.getItem(K)||"{{}}"); cs.forEach(function(c){{ if(g[clave(c)]) c.textContent=g[clave(c)]; }}); }}catch(e){{}}
  window.addEventListener("beforeprint",function(){{ if(document.activeElement) document.activeElement.blur(); var s=window.getSelection&&window.getSelection(); if(s) s.removeAllRanges(); }});
  cs.forEach(function(c){{
    c.addEventListener("keydown",function(ev){{ if(ev.key==="Enter"){{ ev.preventDefault(); c.blur(); }} }});
    c.addEventListener("input",function(){{ try{{ var g={{}}; cs.forEach(function(x){{ g[clave(x)]=x.textContent; }}); localStorage.setItem(K,JSON.stringify(g)); }}catch(e){{}} }});
  }});
}})();
</script>
</body>
</html>
'''

if __name__ == "__main__":
    for L in ("es", "en"):
        with open(os.path.join(AQUI, f"obra-fenix-lago-cartel-{L}.html"), "w", encoding="utf-8") as f:
            f.write(pagina(L))
    print("ok")
