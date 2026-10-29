"""
Materiales de «Inoka: El aliento de la pradera y la gente de Illinois», obra de José M. Fernández:
guía de producción, guía histórica para el docente, cartel y programa de mano, en español e inglés.

Produce:
  obra-inoka-produccion-es.html / -en.html
  obra-inoka-historia-es.html   / -en.html
  obra-inoka-cartel-es.html     / -en.html
  obra-inoka-programa-es.html   / -en.html
Uso: python3 gen_inoka_materiales.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_bosque_produccion import CSS as CSS_GUIA, JS as JS_GUIA, casillas

AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTOR = "José M. Fernández"
LIC = '<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license">CC BY-NC-SA 4.0</a>'
PEORIA = "https://peoriatribe.com/"

COM = {
 "es": dict(inicio="index-es.html", teatro="teatro-es.html", logo_alt="Lumi — página de inicio", saltar="Saltar al contenido", menu_lbl="Menú principal",
   menu=[("index-es.html","Inicio"),("grados-es.html","Por grado"),("materias-es.html","Por materia"),("teatro-es.html","Teatro")],
   idioma_lbl="Idioma", arriba="↑ Cerrar y volver arriba", partes="Partes de la guía",
   titulo="Inoka: El aliento de la pradera y la gente de Illinois", obra=f"Obra de {AUTOR}", guion="obra-inoka-es.html", guion_txt="← El guion",
   pie=f"«Inoka: El aliento de la pradera y la gente de Illinois» · Obra de {AUTOR} · Lumi · {LIC}"),
 "en": dict(inicio="index.html", teatro="teatro.html", logo_alt="Lumi — home page", saltar="Skip to content", menu_lbl="Main menu",
   menu=[("index.html","Home"),("grados.html","By grade"),("materias.html","By subject"),("teatro.html","Theater")],
   idioma_lbl="Language", arriba="↑ Close and back to top", partes="Parts of the guide",
   titulo="Inoka: The Breath of the Prairie and the People of Illinois", obra=f"A play by {AUTOR}", guion="obra-inoka-en.html", guion_txt="← The script",
   pie=f"“Inoka: The Breath of the Prairie and the People of Illinois” · A play by {AUTOR} · Lumi · {LIC}"),
}

def cabecera(L, archivo_otro, actual_teatro=True):
    c = COM[L]
    menu = "\n".join(f'   <a href="{h}"{" aria-current=\"page\"" if (h == c["teatro"] and actual_teatro) else ""}>{x}</a>' for h, x in c["menu"])
    idioma = (f'<span aria-current="true">Español</span><a href="{archivo_otro}" lang="en" hreflang="en">English</a>' if L == "es"
              else f'<a href="{archivo_otro}" lang="es" hreflang="es">Español</a><span aria-current="true">English</span>')
    return f'''<a class="saltar" href="#contenido">{c["saltar"]}</a>
<header class="cabecera">
 <div class="envoltura">
  <a class="marca" href="{c["inicio"]}"><img src="lumi-logo-horizontal.svg" alt="{c["logo_alt"]}" width="560" height="240"></a>
  <nav aria-label="{c["menu_lbl"]}" class="menu">
{menu}
  </nav>
  <div class="idioma" role="group" aria-label="{c["idioma_lbl"]}">{idioma}</div>
 </div>
</header>'''

def head(L, titulo, desc, otro, extra_css=""):
    return f'''<!doctype html>
<!-- «Inoka: El aliento de la pradera y la gente de Illinois» · Obra de {AUTOR} · Lumi · CC BY-NC-SA 4.0 · generado con herramientas/gen_inoka_materiales.py -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · Lumi</title>
<meta name="description" content="{desc}">
<meta name="author" content="{AUTOR}">
<meta name="dcterms.license" content="CC BY-NC-SA 4.0">
<link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="alternate" hreflang="{"en" if L=="es" else "es"}" href="{otro}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="lumi.css?v=6">
<style>{CSS_GUIA}{extra_css}</style>
</head>'''

def guia(L, archivo, otro, titulo_pag, h1, intro, herr, nav, secciones, desc):
    c = COM[L]
    secs = "\n".join(f''' <details class="seccion acord" id="{sid}" name="partes">
  <summary><h2 id="t-{sid}">{tit}</h2></summary>
  <div class="cuerpo">{cuerpo}
  <p class="arriba"><a href="#contenido" class="cerrar">{c["arriba"]}</a></p>
 </div>
 </details>''' for sid, tit, cuerpo in secciones)
    navh = "\n".join(f'  <li><a href="#{a}">{x}</a></li>' for a, x in nav)
    return f'''{head(L, titulo_pag, desc, otro, ".autor-caja{background:#F3EEFA;border-left:6px solid #5B3F8F;border-radius:10px;padding:.8rem 1rem;margin:1rem 0} .cancion-v{border:2px solid var(--borde);border-radius:14px;padding:.8rem 1rem;margin:1rem 0;scroll-margin-top:120px} .cancion-v video{display:block;width:100%;max-width:460px;border-radius:12px;background:#000} .linea{list-style:none;padding:0;margin:.5rem 0;border-left:4px solid var(--pet)} .linea li{position:relative;padding:.35rem 0 .7rem 1.2rem} .linea li::before{content:\"\";position:absolute;left:-10px;top:.7rem;width:16px;height:16px;border-radius:50%;background:#fff;border:4px solid var(--pet)} .linea b{display:block} .mito{margin:.2rem 0;font-weight:700} .hecho{margin:.2rem 0 1rem}")}
<body>
{cabecera(L, otro)}

<section class="obra-cab" aria-labelledby="titulo">
 <div class="envoltura">
  <p style="margin:0"><a href="{c["guion"]}">{c["guion_txt"]}</a></p>
  <h1 id="titulo">{h1}</h1>
  <p class="autor">{c["obra"]}</p>
  <p style="margin:.3rem 0 0">{intro}</p>
  <div class="herr solo-pantalla">{herr}</div>
 </div>
</section>

<main id="contenido" tabindex="-1"><div class="envoltura">
 <nav aria-label="{c["partes"]}"><ul class="anclas">
{navh}
 </ul></nav>

{secs}
</div></main>
<footer class="pie"><div class="envoltura"><p>{c["pie"]}</p></div></footer>
<script>{JS_GUIA}</script>
</body>
</html>
'''

def video_cancion(L, vid, titulo, sub_titulo, portada, letra_html, sentido_en=""):
    if L == "es":
        aviso = "Su navegador no puede mostrar el video."; desc = "Descargar la canción"; lt = "Letra"
    else:
        aviso = "Your browser cannot play this video."; desc = "Download the song"; lt = "Lyrics (sung in Spanish)"
    sentido = f'<p style="font-style:italic;margin:.5rem 0 0">{sentido_en}</p>' if sentido_en else ""
    return f'''
  <div class="cancion-v" id="{vid}">
   <h3>🎵 «{titulo}»</h3>
   <p style="margin:.2rem 0 .6rem">{sub_titulo}</p>
   <video controls preload="none" poster="{portada}" width="1024" height="1024" lang="es"><source src="{vid}.mp4" type="video/mp4"><track kind="captions" src="{vid}.vtt" srclang="es" label="Español" default>{aviso} <a href="{vid}.mp4">{desc}</a>.</video>
   <details style="margin:.6rem 0 0"><summary><strong>{lt}</strong></summary><p lang="es" style="font-size:1.1rem;line-height:1.7">{letra_html}</p>{sentido}</details>
  </div>'''

LETRA_RAIZ = "Raíz con raíz, hojita con hoja,<br>la tierra florece cuando el pueblo trabaja.<br>Maíz, calabaza y tierno frijol<br>protegen el hogar bajo el mismo sol."
SENT_RAIZ = "Root by root, little leaf by leaf, / the land blooms when the people work together. / Corn, squash and tender beans / protect the home under the same sun."
LETRA_LEGADO = ("Bajo el cielo abierto creció la hierba alta,<br>el bisonte, el viento y el agua que no falta.<br>Maíz, frijol, calabaza, juntitos bajo el sol:<br>la tierra da sus frutos cuando hay unión.<br><br>"
 "<strong>Estribillo:</strong><br>Pradera dorada, río sin final,<br>la gente de Illinois vuelve a cantar.<br>Lo que fue sembrado no se perderá:<br>¡el aliento sigue, sigue y seguirá!<br><br>"
 "Por el río bajan canoas de un tronco,<br>llevan pieles, conchas y un saludo hondo.<br>En el consejo escuchan, palabra por palabra,<br>y así nace un acuerdo que a todos ampara.<br><br>(Estribillo)<br><br>"
 "Pasaron los años, el camino fue largo;<br>dejaron su tierra, pero no su legado.<br>Hoy en Oklahoma su nación sigue en pie,<br>y vuelve su lengua: los niños la aprenden también.<br><br>(Estribillo, dos veces)<br><br>"
 "¡Somos el presente y el legado de la gente de Illinois!")
SENT_LEGADO = ("What it means: Under the open sky the tall grass grew, the bison, the wind and the water that never runs out. Corn, beans and squash, close together under the sun: the land gives its fruit when there is unity. "
 "Chorus: Golden prairie, endless river, the people of Illinois sing again. What was planted will not be lost: the breath goes on and on! "
 "Canoes carved from a single trunk come down the river, carrying pelts, shells and a heartfelt greeting. In the council they listen, word by word, and so an agreement is born that protects everyone. "
 "The years went by, the road was long; they left their land, but not their legacy. Today their nation still stands in Oklahoma, and their language is coming back: the children are learning it too. "
 "We are the present and the legacy of the people of Illinois!")

# =========================================================================== PRODUCCIÓN
def produccion(L):
    es = L == "es"
    if es:
        sec = [
("respeto", "Respeto cultural: lo primero", f"""
  <div class="autor-caja"><p style="margin:0"><strong>Esta obra habla de un pueblo que sigue vivo.</strong> Los descendientes de los Inoka forman hoy la <span lang="en">Peoria Tribe of Indians of Oklahoma</span>, una nación reconocida por el gobierno de Estados Unidos. La obra los presenta con respeto, sin estereotipos de película.</p></div>
  <h3>Cinco reglas para todo el montaje</h3>
  <ol>
   <li><strong>Nadie se disfraza de indígena.</strong> Nada de plumas, tocados, flecos, collares «de estilo indígena» ni pintura en la cara. Cada personaje se reconoce por lo que hace y por lo que lleva en las manos (ver <a href="#vestuario">vestuario</a>).</li>
   <li><strong>Los objetos sagrados no se fabrican ni se usan en escena.</strong> El calumet se nombra en el acto IV, pero no aparece. No se usan tambores de agua ni otros objetos ceremoniales.</li>
   <li><strong>No se imitan cantos, gritos ni maneras de hablar.</strong> Los niños hablan con su voz de siempre. La música usa tambor de mano, palos de lluvia, sonajas y flauta, sin copiar cantos de ningún pueblo. El tambor marca un pulso parejo, como un latido, no el ritmo de «tom-tom» de las películas; la flauta es dulce o traversa, no una «flauta nativa». En el baile final, pasos sencillos, sin imitar danzas indígenas.</li>
   <li><strong>Se habla en presente cuando toca.</strong> Los Inoka no «desaparecieron»: el acto V lo dice con claridad, y conviene repetirlo en clase.</li>
   <li><strong>Los nombres, bien dichos.</strong> Inoka, Kaskaskia, Peoria, Tamaroa, Cahokia, Michigamea, miami-illinois. Ver la <a href="obra-inoka-historia-es.html">guía histórica</a>.</li>
  </ol>
  <div class="nota"><strong>Antes de representarla en público</strong>, es una buena cortesía escribir a la tribu Peoria para contarles el proyecto y ofrecerles el guion. Su información de contacto está en <a href="{PEORIA}" target="_blank" rel="noopener noreferrer">peoriatribe.com</a>. Pregúnteles también si están de acuerdo con que los niños hablen en primera persona como líderes Peoria y Kaskaskia.</div>"""),
("resumen", "En breve", """
  <ul>
   <li><strong>De qué trata:</strong> la pradera y los ríos de Illinois, las aldeas Inoka y su forma de vivir: el cultivo del maíz, el frijol y la calabaza, las casas de esteras, el comercio por los ríos y el consejo que decide por acuerdo. Termina en el presente, con la tribu Peoria de Oklahoma y su lengua, que vuelve.</li>
   <li><strong>Duración:</strong> de 20 a 25 minutos, con las dos canciones.</li>
   <li><strong>Elenco:</strong> toda la escuela. Cada acto es de dos grados; el acto V reúne a todos.</li>
   <li><strong>Idiomas:</strong> el guion está en <a href="obra-inoka-es.html">español</a> y en <a href="obra-inoka-en.html" lang="en">inglés</a>, con las mismas líneas. Las dos canciones se cantan en español.</li>
  </ul>"""),
("imagenes", "La obra en imágenes", """
  <figure class="info"><img src="inoka-acto1.jpg" alt="Infografía «Configuración del Acto I: El latido de la pradera». Ambientación: tambor de mano y palos de lluvia en penumbra, y un fondo de pastizales dorados con telas ligeras. Elenco: narradores de sexto grado; niños de prekínder y kínder como flores, bisontes, ciervos y el viento; y el concepto central: el pueblo Inoka, que vivía en armonía con la tierra." loading="lazy" width="1376" height="768"><figcaption>Acto I: el latido de la pradera. Infografía orientativa: manda el guion (en el guion tocan 1.º y 2.º, y no hay ciervos).</figcaption></figure>"""),
("reparto", "Reparto por grados y cantidades", """
  <p>Las cantidades son orientativas. Los papeles con texto propio pueden ser de un niño o de un grupo pequeño; los grupos sin texto crecen según la escuela.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Cantidad de niños por papel</caption>
   <thead><tr><th scope="col">Grado</th><th scope="col">Papel</th><th scope="col">Mínimo</th><th scope="col">Recomendado</th><th scope="col">Máximo</th></tr></thead>
   <tbody>
    <tr><th scope="row">Prekínder y kínder</th><td>La naturaleza: viento, flores, aves y bisontes (sin texto)</td><td>8</td><td>20</td><td>40</td></tr>
    <tr><th scope="row" rowspan="3">1.º y 2.º</th><td>Niño Maíz, Niña Frijol, Niña Calabaza, Agricultora, Tejedora, estudiante de 1.º del acto V</td><td>5</td><td>5</td><td>10</td></tr>
    <tr><td>Músicos: palos de lluvia y sonajas (acto I)</td><td>2</td><td>4</td><td>8</td></tr>
    <tr><td>Coro «Raíz con raíz»</td><td>6</td><td>20</td><td>todo el grado</td></tr>
    <tr><th scope="row" rowspan="2">3.º y 4.º</th><td>Mensajero, Navegante Peoria, Comerciante Kaskaskia, estudiantes de 3.º y 4.º del acto V</td><td>5</td><td>5</td><td>10</td></tr>
    <tr><td>Los ríos (telas) y los remeros de las canoas, sin texto</td><td>4</td><td>8</td><td>16</td></tr>
    <tr><th scope="row" rowspan="3">5.º y 6.º</th><td>Narradores 1 y 2</td><td>2</td><td>2</td><td>4</td></tr>
    <tr><td>Guardiana de la Memoria, líderes del consejo Kaskaskia y Peoria, estudiantes de 5.º y 6.º del acto V</td><td>5</td><td>5</td><td>10</td></tr>
    <tr><td>Círculo del consejo (sin texto) y equipo técnico</td><td>4</td><td>12</td><td>30</td></tr>
    <tr><th scope="row">Todos</th><td>El coro final</td><td colspan="3">toda la escuela</td></tr>
   </tbody>
  </table>
  </div>"""),
("trabajos", "Trabajos para no actores", """
  <ul class="tarjetas">
   <li><h3>🎤 Presentadores</h3><span class="chip">5.º o 6.º · 1 o 2</span><p>Dan la bienvenida, presentan la obra y a su autor, y recuerdan que habla de un pueblo que sigue vivo.</p></li>
   <li><h3>🔊 Sonido</h3><span class="chip">4.º a 6.º · 2</span><p>Ponen las dos canciones en su momento, siguiendo la <a href="#entradas">hoja de entradas</a>.</p></li>
   <li><h3>💡 Luces</h3><span class="chip">5.º y 6.º · 1 o 2</span><p>Penumbra al empezar, luz cálida de día y luz dorada para el final.</p></li>
   <li><h3>🌾 Escenografía</h3><span class="chip">Cualquier grado</span><p>Pintan la pradera, preparan la casa de esteras y las canoas de cartón.</p></li>
   <li><h3>🧺 Utilería</h3><span class="chip">3.º a 6.º · 2 a 4</span><p>Canastos, tallos, esteras, remos, telas del río, pieles de fieltro, conchas y cuencos.</p></li>
   <li><h3>📖 Apuntador</h3><span class="chip">5.º o 6.º · 1 o 2</span><p>Siguen el guion entre bastidores.</p></li>
   <li><h3>🤝 Guías de bambalinas</h3><span class="chip">5.º · 1 por cada 2 o 3 pequeños</span><p>Acompañan a prekínder y kínder en el acto I y en el final.</p></li>
   <li><h3>📰 Programa y cartel</h3><span class="chip">3.º a 6.º · 2 a 4</span><p>Completan el <a href="obra-inoka-programa-es.html">programa de mano</a> y el <a href="obra-inoka-cartel-es.html">cartel</a>.</p></li>
  </ul>"""),
("musica", "Música y canciones", f"""
  <p><strong>Instrumentos:</strong> tambor de mano, palos de lluvia, sonajas de semillas y flauta. Pueden tocarlos los propios alumnos. No se usan grabaciones de cantos ceremoniales indígenas.</p>
  {video_cancion("es", "inoka-raiz-con-raiz", "Raíz con raíz", "Acto II · Coro de 1.º y 2.º grado, después de la Tejedora.", "inoka-raiz-portada.jpg", LETRA_RAIZ)}
  {video_cancion("es", "inoka-legado-de-la-pradera", "Legado de la pradera", "Canción final · Todo el elenco, después del coro «¡Somos la memoria de la pradera!».", "inoka-legado-portada.jpg", LETRA_LEGADO)}
  <p>Las dos canciones se crearon para esta obra. Cada verso se canta dos veces, para que los más pequeños lo repitan.</p>"""),
("entradas", "Hoja de entradas (sonido y luces)", """
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Entradas de sonido y luces</caption>
   <thead><tr><th scope="col">N.º</th><th scope="col">Acto</th><th scope="col">Señal</th><th scope="col">Sonido</th><th scope="col">Luces</th></tr></thead>
   <tbody>
    <tr><td>1</td><td>I</td><td>Se abre el telón</td><td>Tambor de mano, lento; palos de lluvia</td><td>Penumbra</td></tr>
    <tr><td>2</td><td>I</td><td>Entra la naturaleza</td><td>Sigue el tambor</td><td>Sube poco a poco a luz de amanecer</td></tr>
    <tr><td>3</td><td>I</td><td>Habla el Narrador 1</td><td>El tambor baja hasta callar</td><td>Luz de día</td></tr>
    <tr><td>4</td><td>II</td><td>Termina la Tejedora</td><td>«Raíz con raíz»</td><td>Luz cálida</td></tr>
    <tr><td>5</td><td>III</td><td>Entran las canoas</td><td>Sonajas suaves, como agua</td><td>Luz azulada sobre el río</td></tr>
    <tr><td>6</td><td>IV</td><td>Se forma el círculo del consejo</td><td>Silencio</td><td>Luz cálida en el centro</td></tr>
    <tr><td>7</td><td>V</td><td>Todo el elenco da un paso al frente</td><td>—</td><td>Luz general</td></tr>
    <tr><td>8</td><td>V</td><td>Termina el coro «¡Somos el presente…!»</td><td>«Legado de la pradera»</td><td>Luz dorada</td></tr>
    <tr><td>9</td><td>V</td><td>Termina la canción</td><td>Tambores de mano</td><td>Reverencia; se cierra el telón</td></tr>
   </tbody>
  </table>
  </div>"""),
("vestuario", "Vestuario respetuoso", """
  <p>Los niños <strong>no</strong> se visten «de indígenas». Usan ropa sencilla y llevan la utilería de su personaje.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Vestuario por papel</caption>
   <thead><tr><th scope="col">Papel</th><th scope="col">Ropa de casa</th><th scope="col">Lo que lo distingue</th></tr></thead>
   <tbody>
    <tr><td>Personajes humanos (agricultora, tejedora, navegante, comerciante, mensajero, consejo, narradores, estudiantes)</td><td>Camiseta o túnica lisa y pantalón en tonos tierra: beige, ocre, marrón, verde oliva.</td><td>La utilería: canasto, estera a medio tejer, remo, pieles de fieltro, conchas, cuencos de barro, bastón de cañas.</td></tr>
    <tr><td>La naturaleza (prekínder y kínder)</td><td>Camiseta lisa: dorado para la hierba, azul claro para el viento, marrón para los bisontes, colores vivos para flores y aves.</td><td>Un distintivo sencillo de fieltro: una flor, un ala, unos cuernos pequeños.</td></tr>
    <tr><td>Maíz, Frijol y Calabaza</td><td>Verde, verde claro y naranja.</td><td>Mazorca de fieltro, enredadera de papel, hojas grandes de fieltro.</td></tr>
    <tr><td>Los ríos</td><td>Azul.</td><td>Las telas del río.</td></tr>
   </tbody>
  </table>
  </div>
  <div class="nota"><strong>Nunca:</strong> plumas, tocados, cintas en la frente, flecos, collares de imitación, pintura en la cara, «trajes de indio» de tienda.</div>"""),
("cotejo", "Lista de cotejo", f"""
  <p>Salón: <span class="hueco">&nbsp;</span> Docente: <span class="hueco">&nbsp;</span> Papel del grupo: <span class="hueco">&nbsp;</span></p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Lista de cotejo por niño</caption>
   <thead><tr><th scope="col">Nombre</th><th scope="col">Ropa de casa</th><th scope="col">Utilería o distintivo</th><th scope="col">Marcado con su nombre</th><th scope="col">Listo para el ensayo general</th></tr></thead>
   <tbody>
{casillas(4)}
   </tbody>
  </table>
  </div>
  <h3>Utilería y escenografía</h3>
  <ul class="lista-casillas">
   <li><span class="casilla"></span>Fondo de la pradera pintado</li>
   <li><span class="casilla"></span>Casa larga de arcos con esteras</li>
   <li><span class="casilla"></span>Tallos de maíz, frijol y calabaza; canastos</li>
   <li><span class="casilla"></span>Dos telas azules de 6 a 8 metros</li>
   <li><span class="casilla"></span>Dos canoas de cartón con tirantes; remos</li>
   <li><span class="casilla"></span>Pieles de fieltro, conchas, cuencos de barro, bastón de cañas</li>
   <li><span class="casilla"></span>Fogón simbólico de papel o tela (sin fuego real)</li>
   <li><span class="casilla"></span>Tambores de mano, palos de lluvia, sonajas</li>
   <li><span class="casilla"></span>Las dos canciones probadas en el equipo de sonido</li>
  </ul>"""),
("escenografia", "Escenografía y utilería", """
  <ul>
   <li><strong>La pradera (fondo fijo):</strong> papel kraft o lienzo con pastizales dorados altos, flores silvestres y cielo abierto.</li>
   <li><strong>Los ríos:</strong> dos telas ligeras, azul rey y turquesa, de 6 a 8 metros, que los alumnos ondulan suavemente.</li>
   <li><strong>Las canoas:</strong> siluetas de cartón reforzado, pintadas como madera tallada y quemada, con tirantes para llevarlas a la altura de la cintura. Las canoas de los Inoka se tallaban en un solo tronco.</li>
   <li><strong>La casa larga:</strong> arcos flexibles (tubos de PVC o varas) cubiertos con esteras de petate, yute o caña. En verano, los Inoka vivían en casas largas para varias familias; en invierno, en wigwams más pequeños. Las dos se cubrían con esteras de junco.</li>
   <li><strong>El fogón del consejo:</strong> simbólico, de papel o tela naranja. Nunca fuego real.</li>
  </ul>"""),
("plano", "Plano del escenario", """
  <p>Visto desde el público.</p>
  <h3>Actos I y II</h3>
  <div class="plano" role="img" aria-label="Actos I y II: al fondo, la pradera y la casa larga de esteras; a los lados, los músicos; en el centro, la naturaleza (acto I) y las Tres Hermanas con las agricultoras (acto II).">
   <div><b>Fondo izquierda</b>Pradera</div><div><b>Fondo centro</b>Casa larga de esteras</div><div><b>Fondo derecha</b>Pradera</div>
   <div><b>Frente izquierda</b>Músicos (acto I)</div><div><b>Frente centro</b>La naturaleza · las Tres Hermanas</div><div><b>Frente derecha</b>Músicos (acto I)</div>
  </div><p class="publico">Público</p>
  <h3>Acto III</h3>
  <div class="plano" role="img" aria-label="Acto III: las telas del río cruzan el escenario de lado a lado; las canoas avanzan sobre el río; la orilla de los Kaskaskia a la derecha.">
   <div><b>Fondo izquierda</b>Entrada de las canoas</div><div><b>Fondo centro</b>Pradera</div><div><b>Fondo derecha</b>Entrada del mensajero</div>
   <div><b>Frente izquierda</b>Río (telas)</div><div><b>Frente centro</b>Río y canoas</div><div><b>Frente derecha</b>Orilla Kaskaskia</div>
  </div><p class="publico">Público</p>
  <h3>Actos IV y V</h3>
  <div class="plano" role="img" aria-label="Actos IV y V: en el centro, el círculo del consejo alrededor del fogón; alrededor, en semicírculo, los demás grados. En el acto V todos dan un paso al frente.">
   <div><b>Fondo izquierda</b>Semicírculo: 1.º a 4.º</div><div><b>Fondo centro</b>Semicírculo: 1.º a 4.º</div><div><b>Fondo derecha</b>Semicírculo: 1.º a 4.º</div>
   <div><b>Frente izquierda</b>Prekínder y kínder, sentados</div><div><b>Frente centro</b>Círculo del consejo (5.º y 6.º) y fogón</div><div><b>Frente derecha</b>Prekínder y kínder, sentados</div>
  </div><p class="publico">Público</p>"""),
("ensayos", "Ensayos", """
  <h3>Semanas 1 a 3: cada grupo en su salón</h3>
  <ul>
   <li><strong>Prekínder y kínder (15 min):</strong> entrar con la música imitando el viento, los animales y las flores, y «congelarse» en semicírculo.</li>
   <li><strong>1.º y 2.º (20 min):</strong> sus líneas, «Raíz con raíz» y el movimiento de los tallos y las esteras; los músicos, el pulso del acto I.</li>
   <li><strong>3.º y 4.º (25 min):</strong> el movimiento de las telas y el paso de las canoas; las líneas del mensajero, el navegante y el comerciante.</li>
   <li><strong>5.º y 6.º (30 min):</strong> proyección de la voz, las pausas del consejo y la narración.</li>
   <li><strong>Todos:</strong> «Legado de la pradera».</li>
  </ul>
  <h3>Semanas 4 y 5: por actos</h3>
  <p>Cada acto con su música y sus entradas y salidas por los lados. El acto V, con todos, al final de la semana 5.</p>
  <h3>Última semana</h3>
  <p>Dos o tres pasadas completas con utilería y canciones.</p>
  <div class="nota">Nadie tiene que memorizar si no puede. Los narradores pueden leer con el guion en una carpeta negra. En el <a href="obra-inoka-es.html">guion interactivo</a>, cada niño puede elegir su papel, ver solo sus líneas y escucharlas.</div>"""),
("carta", "Carta a las familias", """
  <p class="solo-pantalla">Lista para imprimir. Complete los espacios a mano.</p>
  <div class="carta">
   <p><strong>Obra de teatro de la escuela: <em>Inoka: El aliento de la pradera y la gente de Illinois</em></strong></p>
   <p>Fecha: <span class="hueco">&nbsp;</span></p>
   <p>Estimada familia:</p>
   <p>Este año, toda la escuela, de prekínder a 6.º grado, presentará <em>Inoka</em>, una obra sobre los pueblos que vivían en las praderas y los ríos de Illinois antes de la llegada de los franceses, y sobre sus descendientes de hoy, la tribu Peoria de Oklahoma. Mientras ensayan, los niños aprenderán historia de nuestro estado, ciencias (cómo crecen juntos el maíz, el frijol y la calabaza) y el valor de decidir escuchándonos unos a otros.</p>
   <p><strong>Su hijo o hija</strong> <span class="hueco">&nbsp;</span> <strong>será:</strong> <span class="hueco">&nbsp;</span></p>
   <p><strong>Ropa que le pedimos, si la tiene en casa</strong> (no hace falta comprar nada): <span class="hueco" style="min-width:60%">&nbsp;</span></p>
   <p><strong>Importante:</strong> por respeto a los pueblos indígenas, les pedimos que <strong>no</strong> envíen disfraces «de indio», plumas, tocados ni pintura para la cara. La escuela preparará la utilería de cada personaje.</p>
   <ul>
    <li>Entregar la ropa, en una bolsa con el nombre y el grado: <span class="hueco">&nbsp;</span></li>
    <li>Ensayo general: <span class="hueco">&nbsp;</span></li>
    <li>Función: día <span class="hueco">&nbsp;</span>, hora <span class="hueco">&nbsp;</span>, lugar <span class="hueco">&nbsp;</span></li>
   </ul>
   <p><strong>Cómo puede ayudar en casa:</strong> el guion está en Lumi (www.lumi-educa.com), en español y en inglés, con un botón para escuchar cada línea. Las dos canciones también están allí.</p>
   <p>¡Gracias por acompañarnos!</p>
   <p>Atentamente,<br><span class="hueco">&nbsp;</span></p>
   <div class="talon">
    <p><strong>Devuelva este talón firmado antes del</strong> <span class="hueco">&nbsp;</span></p>
    <p>Nombre del niño o la niña: <span class="hueco">&nbsp;</span> Grado: <span class="hueco">&nbsp;</span></p>
    <p><span class="casilla"></span>Doy permiso para que mi hijo o hija participe en la obra.</p>
    <p><span class="casilla"></span>Doy permiso para que la escuela publique fotos o videos de la obra en los que aparezca mi hijo o hija.</p>
    <p><span class="casilla"></span><strong>No</strong> doy permiso para publicar fotos ni videos en los que aparezca mi hijo o hija.</p>
    <p>Firma: <span class="hueco" style="min-width:14em">&nbsp;</span> Teléfono: <span class="hueco">&nbsp;</span></p>
   </div>
  </div>"""),
        ]
        nav = [("respeto","Respeto cultural"),("resumen","En breve"),("imagenes","Imágenes"),("reparto","Reparto"),("trabajos","Trabajos para no actores"),("musica","Música y canciones"),("entradas","Hoja de entradas"),("vestuario","Vestuario"),("cotejo","Lista de cotejo"),("escenografia","Escenografía"),("plano","Plano"),("ensayos","Ensayos"),("carta","Carta a las familias")]
        herr = '<button type="button" onclick="window.print()">🖨️ Imprimir o guardar en PDF</button><a href="#carta">✉️ Carta a las familias</a><a href="obra-inoka-programa-es.html">📄 Programa de mano</a><a href="obra-inoka-cartel-es.html">🖼️ Cartel</a><a href="obra-inoka-historia-es.html">📜 Guía histórica</a>'
        return guia(L, "obra-inoka-produccion-es.html", "obra-inoka-produccion-en.html", "Inoka · Producción", "Inoka · Producción",
                    "Todo lo que hace falta para montarla con toda la escuela, con respeto por el pueblo que representa.", herr, nav, sec,
                    "Guía de producción de «Inoka», de José M. Fernández: respeto cultural, reparto por grados, canciones, hoja de entradas, vestuario, escenografía, ensayos y carta a las familias.")
    # ------------------------------------------------------------------ inglés
    sec = [
("respeto", "Cultural respect comes first", f"""
  <div class="autor-caja"><p style="margin:0"><strong>This play is about a people who are still here today.</strong> The descendants of the Inoka are today the Peoria Tribe of Indians of Oklahoma, a nation recognized by the United States government. The play presents them with respect, without movie stereotypes.</p></div>
  <h3>Five rules for the whole production</h3>
  <ol>
   <li><strong>No one dresses up as a Native person.</strong> No feathers, headdresses, fringe, “Native-style” necklaces or face paint. Each character is recognized by what they do and what they carry (see <a href="#vestuario">costumes</a>).</li>
   <li><strong>Sacred objects are not made or used on stage.</strong> The calumet is mentioned in Act IV, but it does not appear. No water drums or other ceremonial objects are used.</li>
   <li><strong>No imitation of chants, war cries or ways of speaking.</strong> The children speak in their own voices. The music uses hand drums, rain sticks, rattles and flute, without copying any people's songs. The drum keeps an even pulse, like a heartbeat, not the movie “tom-tom” rhythm; use a recorder or concert flute, not a “Native flute.” In the final dance, simple steps, not imitating Native dances.</li>
   <li><strong>Use the present tense when it applies.</strong> The Inoka did not “disappear”: Act V says so clearly, and it is worth repeating in class.</li>
   <li><strong>Say the names correctly.</strong> Inoka, Kaskaskia, Peoria, Tamaroa, Cahokia, Michigamea, Miami-Illinois. See the <a href="obra-inoka-historia-en.html">historical guide</a>.</li>
  </ol>
  <div class="nota"><strong>Before a public performance</strong>, it is a good courtesy to write to the Peoria Tribe to tell them about the project and offer them the script. Their contact information is at <a href="{PEORIA}" target="_blank" rel="noopener noreferrer">peoriatribe.com</a>. Also ask whether they are comfortable with children speaking in the first person as Peoria and Kaskaskia leaders.</div>"""),
("resumen", "At a glance", """
  <ul>
   <li><strong>What it's about:</strong> the prairie and rivers of Illinois, the Inoka villages and their way of life: growing corn, beans and squash, houses covered with mats, trade along the rivers, and the council that decides by agreement. It ends in the present, with the Peoria Tribe of Oklahoma and their language, which is coming back.</li>
   <li><strong>Running time:</strong> 20 to 25 minutes, with the two songs.</li>
   <li><strong>Cast:</strong> the whole school. Each act belongs to two grades; Act V brings everyone together.</li>
   <li><strong>Languages:</strong> the script is in <a href="obra-inoka-es.html" lang="es">Spanish</a> and <a href="obra-inoka-en.html">English</a>, with the same lines. Both songs are sung in Spanish.</li>
  </ul>"""),
("imagenes", "The play in pictures", """
  <p>This infographic is in Spanish.</p>
  <figure class="info"><img src="inoka-acto1.jpg" alt="Infographic “Setting up Act I: The Heartbeat of the Prairie.” Setting: a hand drum and rain sticks in dim light, and a backdrop of golden grasses with light cloths. Cast: 6th grade narrators; Pre-K and K children as flowers, bison, deer and the wind; and the central idea: the Inoka people, who lived in harmony with the land." loading="lazy" width="1376" height="768"><figcaption>Act I: the heartbeat of the prairie. The infographic is a general guide; the script comes first (in the script, 1st and 2nd graders play, and there are no deer).</figcaption></figure>"""),
("reparto", "Cast by grade and numbers", """
  <p>The numbers are a guide. Parts with their own lines can be played by one child or a small group; groups without lines grow with the school.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Number of children per part</caption>
   <thead><tr><th scope="col">Grade</th><th scope="col">Part</th><th scope="col">Minimum</th><th scope="col">Suggested</th><th scope="col">Maximum</th></tr></thead>
   <tbody>
    <tr><th scope="row">Pre-K &amp; K</th><td>Nature: wind, flowers, birds and bison (no lines)</td><td>8</td><td>20</td><td>40</td></tr>
    <tr><th scope="row" rowspan="3">1st &amp; 2nd</th><td>Corn, Bean, Squash, Farmer, Weaver, 1st grader in Act V</td><td>5</td><td>5</td><td>10</td></tr>
    <tr><td>Musicians: rain sticks and rattles (Act I)</td><td>2</td><td>4</td><td>8</td></tr>
    <tr><td>“Raíz con raíz” chorus</td><td>6</td><td>20</td><td>the whole grade</td></tr>
    <tr><th scope="row" rowspan="2">3rd &amp; 4th</th><td>Messenger, Peoria Paddler, Kaskaskia Trader, 3rd and 4th graders in Act V</td><td>5</td><td>5</td><td>10</td></tr>
    <tr><td>The rivers (cloths) and canoe paddlers, no lines</td><td>4</td><td>8</td><td>16</td></tr>
    <tr><th scope="row" rowspan="3">5th &amp; 6th</th><td>Narrators 1 and 2</td><td>2</td><td>2</td><td>4</td></tr>
    <tr><td>Keeper of Memory, Kaskaskia and Peoria council leaders, 5th and 6th graders in Act V</td><td>5</td><td>5</td><td>10</td></tr>
    <tr><td>Council circle (no lines) and tech crew</td><td>4</td><td>12</td><td>30</td></tr>
    <tr><th scope="row">All</th><td>The final chorus</td><td colspan="3">the whole school</td></tr>
   </tbody>
  </table>
  </div>"""),
("trabajos", "Jobs for non-actors", """
  <ul class="tarjetas">
   <li><h3>🎤 Presenters</h3><span class="chip">5th or 6th · 1 or 2</span><p>Welcome the audience, introduce the play and its author, and remind everyone that it is about a people who are still here today.</p></li>
   <li><h3>🔊 Sound</h3><span class="chip">4th to 6th · 2</span><p>Play the two songs at the right moment, following the <a href="#entradas">cue sheet</a>.</p></li>
   <li><h3>💡 Lights</h3><span class="chip">5th &amp; 6th · 1 or 2</span><p>Dim light at the start, warm daylight, and golden light for the ending.</p></li>
   <li><h3>🌾 Sets</h3><span class="chip">Any grade</span><p>Paint the prairie, build the mat-covered house and the cardboard canoes.</p></li>
   <li><h3>🧺 Props</h3><span class="chip">3rd to 6th · 2 to 4</span><p>Baskets, stalks, mats, paddles, river cloths, felt pelts, shells and bowls.</p></li>
   <li><h3>📖 Prompter</h3><span class="chip">5th or 6th · 1 or 2</span><p>Follow the script backstage.</p></li>
   <li><h3>🤝 Backstage buddies</h3><span class="chip">5th · 1 for every 2 or 3 little ones</span><p>Go with Pre-K and K in Act I and in the ending.</p></li>
   <li><h3>📰 Program and poster</h3><span class="chip">3rd to 6th · 2 to 4</span><p>Fill in the <a href="obra-inoka-programa-en.html">program</a> and the <a href="obra-inoka-cartel-en.html">poster</a>.</p></li>
  </ul>"""),
("musica", "Music and songs", f"""
  <p><strong>Instruments:</strong> hand drum, rain sticks, seed rattles and flute. Students can play them. No recordings of Native ceremonial songs are used.</p>
  {video_cancion("en", "inoka-raiz-con-raiz", "Raíz con raíz", "Act II · 1st and 2nd grade chorus, after the Weaver.", "inoka-raiz-portada.jpg", LETRA_RAIZ, SENT_RAIZ)}
  {video_cancion("en", "inoka-legado-de-la-pradera", "Legado de la pradera", "Closing song · The whole cast, after the chorus “We are the memory of the prairie!”.", "inoka-legado-portada.jpg", LETRA_LEGADO, SENT_LEGADO)}
  <p>Both songs were written for this play and are sung in Spanish. Each line is sung twice, so the little ones can repeat it.</p>"""),
("entradas", "Cue sheet (sound and lights)", """
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Sound and light cues</caption>
   <thead><tr><th scope="col">No.</th><th scope="col">Act</th><th scope="col">Signal</th><th scope="col">Sound</th><th scope="col">Lights</th></tr></thead>
   <tbody>
    <tr><td>1</td><td>I</td><td>The curtain opens</td><td>Slow hand drum; rain sticks</td><td>Dim light</td></tr>
    <tr><td>2</td><td>I</td><td>Nature comes in</td><td>The drum continues</td><td>Slowly up to dawn light</td></tr>
    <tr><td>3</td><td>I</td><td>Narrator 1 speaks</td><td>The drum fades out</td><td>Daylight</td></tr>
    <tr><td>4</td><td>II</td><td>The Weaver finishes</td><td>“Raíz con raíz”</td><td>Warm light</td></tr>
    <tr><td>5</td><td>III</td><td>The canoes come in</td><td>Soft rattles, like water</td><td>Bluish light on the river</td></tr>
    <tr><td>6</td><td>IV</td><td>The council circle forms</td><td>Silence</td><td>Warm light in the center</td></tr>
    <tr><td>7</td><td>V</td><td>The whole cast steps forward</td><td>—</td><td>Full light</td></tr>
    <tr><td>8</td><td>V</td><td>The chorus “We are the present…!” ends</td><td>“Legado de la pradera”</td><td>Golden light</td></tr>
    <tr><td>9</td><td>V</td><td>The song ends</td><td>Hand drums</td><td>Bows; the curtain closes</td></tr>
   </tbody>
  </table>
  </div>"""),
("vestuario", "Respectful costumes", """
  <p>The children do <strong>not</strong> dress up “as Native people.” They wear simple clothes and carry their character's props.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Costumes by part</caption>
   <thead><tr><th scope="col">Part</th><th scope="col">Clothes from home</th><th scope="col">What makes them stand out</th></tr></thead>
   <tbody>
    <tr><td>Human characters (farmer, weaver, paddler, trader, messenger, council, narrators, students)</td><td>A plain T-shirt or tunic and pants in earth tones: beige, ochre, brown, olive green.</td><td>Props: a basket, a half-woven mat, a paddle, felt pelts, shells, clay bowls, a reed staff.</td></tr>
    <tr><td>Nature (Pre-K and K)</td><td>A plain T-shirt: gold for the grass, light blue for the wind, brown for the bison, bright colors for flowers and birds.</td><td>A simple felt badge: a flower, a wing, small horns.</td></tr>
    <tr><td>Corn, Bean and Squash</td><td>Green, light green and orange.</td><td>A felt corn cob, a paper vine, large felt leaves.</td></tr>
    <tr><td>The rivers</td><td>Blue.</td><td>The river cloths.</td></tr>
   </tbody>
  </table>
  </div>
  <div class="nota"><strong>Never:</strong> feathers, headdresses, headbands, fringe, imitation necklaces, face paint, store-bought “Indian costumes.”</div>"""),
("cotejo", "Checklist", f"""
  <p>Classroom: <span class="hueco">&nbsp;</span> Teacher: <span class="hueco">&nbsp;</span> Group's part: <span class="hueco">&nbsp;</span></p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Checklist by child</caption>
   <thead><tr><th scope="col">Name</th><th scope="col">Clothes from home</th><th scope="col">Prop or badge</th><th scope="col">Labeled with name</th><th scope="col">Ready for dress rehearsal</th></tr></thead>
   <tbody>
{casillas(4)}
   </tbody>
  </table>
  </div>
  <h3>Props and sets</h3>
  <ul class="lista-casillas">
   <li><span class="casilla"></span>Painted prairie backdrop</li>
   <li><span class="casilla"></span>Longhouse of bent poles covered with mats</li>
   <li><span class="casilla"></span>Corn, bean and squash stalks; baskets</li>
   <li><span class="casilla"></span>Two blue cloths, 20 to 26 feet long</li>
   <li><span class="casilla"></span>Two cardboard canoes with straps; paddles</li>
   <li><span class="casilla"></span>Felt pelts, shells, clay bowls, reed staff</li>
   <li><span class="casilla"></span>Symbolic fire made of paper or cloth (no real fire)</li>
   <li><span class="casilla"></span>Hand drums, rain sticks, rattles</li>
   <li><span class="casilla"></span>Both songs tested on the sound system</li>
  </ul>"""),
("escenografia", "Sets and props", """
  <ul>
   <li><strong>The prairie (fixed backdrop):</strong> kraft paper or canvas with tall golden grasses, wildflowers and open sky.</li>
   <li><strong>The rivers:</strong> two light cloths, royal blue and turquoise, 20 to 26 feet long, gently waved by students.</li>
   <li><strong>The canoes:</strong> reinforced cardboard cutouts, painted like carved and burned wood, with straps to carry them at waist height. Inoka canoes were carved from a single tree trunk.</li>
   <li><strong>The longhouse:</strong> flexible arches (PVC pipes or poles) covered with straw, jute or reed mats. In summer the Inoka lived in longhouses shared by several families; in winter, in smaller wigwams. Both were covered with rush mats.</li>
   <li><strong>The council fire:</strong> symbolic, made of orange paper or cloth. Never real fire.</li>
  </ul>"""),
("plano", "Stage plan", """
  <p>Seen from the audience.</p>
  <h3>Acts I and II</h3>
  <div class="plano" role="img" aria-label="Acts I and II: upstage, the prairie and the mat-covered longhouse; at the sides, the musicians; in the center, nature (Act I) and the Three Sisters with the farmers (Act II).">
   <div><b>Upstage left</b>Prairie</div><div><b>Upstage center</b>Mat-covered longhouse</div><div><b>Upstage right</b>Prairie</div>
   <div><b>Downstage left</b>Musicians (Act I)</div><div><b>Downstage center</b>Nature · the Three Sisters</div><div><b>Downstage right</b>Musicians (Act I)</div>
  </div><p class="publico">Audience</p>
  <h3>Act III</h3>
  <div class="plano" role="img" aria-label="Act III: the river cloths cross the stage; the canoes move along the river; the Kaskaskia riverbank on the right.">
   <div><b>Upstage left</b>Canoes come in</div><div><b>Upstage center</b>Prairie</div><div><b>Upstage right</b>Messenger comes in</div>
   <div><b>Downstage left</b>River (cloths)</div><div><b>Downstage center</b>River and canoes</div><div><b>Downstage right</b>Kaskaskia riverbank</div>
  </div><p class="publico">Audience</p>
  <h3>Acts IV and V</h3>
  <div class="plano" role="img" aria-label="Acts IV and V: in the center, the council circle around the fire; around it, in a half circle, the other grades. In Act V everyone steps forward.">
   <div><b>Upstage left</b>Half circle: 1st to 4th</div><div><b>Upstage center</b>Half circle: 1st to 4th</div><div><b>Upstage right</b>Half circle: 1st to 4th</div>
   <div><b>Downstage left</b>Pre-K and K, seated</div><div><b>Downstage center</b>Council circle (5th and 6th) and fire</div><div><b>Downstage right</b>Pre-K and K, seated</div>
  </div><p class="publico">Audience</p>"""),
("ensayos", "Rehearsals", """
  <h3>Weeks 1 to 3: each group in its classroom</h3>
  <ul>
   <li><strong>Pre-K and K (15 min):</strong> come in with the music, moving like the wind, the animals and the flowers, and “freeze” in a half circle.</li>
   <li><strong>1st and 2nd (20 min):</strong> their lines, “Raíz con raíz,” and moving the stalks and mats; the musicians, the beat of Act I.</li>
   <li><strong>3rd and 4th (25 min):</strong> moving the cloths and the canoes; the messenger's, paddler's and trader's lines.</li>
   <li><strong>5th and 6th (30 min):</strong> projecting their voices, the pauses of the council, and the narration.</li>
   <li><strong>Everyone:</strong> “Legado de la pradera.”</li>
  </ul>
  <h3>Weeks 4 and 5: act by act</h3>
  <p>Each act with its music, entrances and exits from the sides. Act V, with everyone, at the end of week 5.</p>
  <h3>Last week</h3>
  <p>Two or three full run-throughs with props and songs.</p>
  <div class="nota">No one has to memorize if they can't. Narrators can read from a script in a black folder. In the <a href="obra-inoka-en.html">interactive script</a>, each child can choose a part, see only their own lines and listen to them.</div>"""),
("carta", "Family letter", """
  <p class="solo-pantalla">Ready to print. Fill in the blanks by hand.</p>
  <div class="carta">
   <p><strong>School play: <em>Inoka: The Breath of the Prairie and the People of Illinois</em></strong></p>
   <p>Date: <span class="hueco">&nbsp;</span></p>
   <p>Dear family,</p>
   <p>This year, the whole school, from Pre-K to 6th grade, will perform <em>Inoka</em>, a play about the peoples who lived on the prairies and rivers of Illinois before the French arrived, and about their descendants today, the Peoria Tribe of Oklahoma. As they rehearse, the children will learn the history of our state, some science (how corn, beans and squash grow together) and the value of making decisions by listening to one another.</p>
   <p><strong>Your child</strong> <span class="hueco">&nbsp;</span> <strong>will be:</strong> <span class="hueco">&nbsp;</span></p>
   <p><strong>Clothes we ask for, if you have them at home</strong> (no need to buy anything): <span class="hueco" style="min-width:60%">&nbsp;</span></p>
   <p><strong>Important:</strong> out of respect for Native peoples, please do <strong>not</strong> send “Indian costumes,” feathers, headdresses or face paint. The school will prepare each character's props.</p>
   <ul>
    <li>Bring the clothes, in a bag labeled with your child's name and grade: <span class="hueco">&nbsp;</span></li>
    <li>Dress rehearsal: <span class="hueco">&nbsp;</span></li>
    <li>Performance: date <span class="hueco">&nbsp;</span>, time <span class="hueco">&nbsp;</span>, place <span class="hueco">&nbsp;</span></li>
   </ul>
   <p><strong>How you can help at home:</strong> the script is on Lumi (www.lumi-educa.com), in English and Spanish, with a button to listen to each line. The two songs are there too.</p>
   <p>Thank you for joining us!</p>
   <p>Sincerely,<br><span class="hueco">&nbsp;</span></p>
   <div class="talon">
    <p><strong>Please sign and return this slip by</strong> <span class="hueco">&nbsp;</span></p>
    <p>Child's name: <span class="hueco">&nbsp;</span> Grade: <span class="hueco">&nbsp;</span></p>
    <p><span class="casilla"></span>I give permission for my child to take part in the play.</p>
    <p><span class="casilla"></span>I give permission for the school to post photos or videos of the play that show my child.</p>
    <p><span class="casilla"></span>I do <strong>not</strong> give permission to post photos or videos that show my child.</p>
    <p>Signature: <span class="hueco" style="min-width:14em">&nbsp;</span> Phone: <span class="hueco">&nbsp;</span></p>
   </div>
  </div>"""),
    ]
    nav = [("respeto","Cultural respect"),("resumen","At a glance"),("imagenes","Pictures"),("reparto","Cast"),("trabajos","Jobs for non-actors"),("musica","Music and songs"),("entradas","Cue sheet"),("vestuario","Costumes"),("cotejo","Checklist"),("escenografia","Sets"),("plano","Stage plan"),("ensayos","Rehearsals"),("carta","Family letter")]
    herr = '<button type="button" onclick="window.print()">🖨️ Print or save as PDF</button><a href="#carta">✉️ Family letter</a><a href="obra-inoka-programa-en.html">📄 Program</a><a href="obra-inoka-cartel-en.html">🖼️ Poster</a><a href="obra-inoka-historia-en.html">📜 Historical guide</a>'
    return guia(L, "obra-inoka-produccion-en.html", "obra-inoka-produccion-es.html", "Inoka · Production", "Inoka · Production",
                "Everything you need to stage it with the whole school, with respect for the people it portrays.", herr, nav, sec,
                "Production guide for “Inoka,” a play by José M. Fernández: cultural respect, cast by grade, songs, cue sheet, costumes, sets, rehearsals and family letter.")

# =========================================================================== HISTORIA
def historia(L):
    if L == "es":
        sec = [
("breve", "En breve", """
  <ul>
   <li><strong>Quiénes:</strong> los Inoka, que los franceses llamaron «Illinois». Eran una confederación de unas doce tribus o aldeas aliadas, entre ellas los Kaskaskia, los Peoria, los Cahokia, los Tamaroa y, desde hacia 1700, parte de los Michigamea.</li>
   <li><strong>Dónde:</strong> las praderas y los valles de los ríos Illinois y Mississippi, en lo que hoy es Illinois y en zonas vecinas.</li>
   <li><strong>Cómo vivían:</strong> en primavera y verano, en grandes aldeas junto a los ríos, donde las mujeres cultivaban maíz, frijol y calabaza; en invierno, en campamentos de caza más pequeños. Los hombres cazaban bisontes en la pradera.</li>
   <li><strong>Hoy:</strong> sus descendientes forman la <span lang="en">Peoria Tribe of Indians of Oklahoma</span>, con sede en Miami, Oklahoma.</li>
  </ul>"""),
("nombre", "El nombre: Inoka e Illinois", """
  <p><strong>Inoka</strong> es el nombre que el pueblo se daba a sí mismo, según anotaron los misioneros franceses. Su significado se desconoce.</p>
  <p><strong>Illinois</strong> viene de una palabra de su propia lengua, el miami-illinois, que significa más o menos «el que habla de la manera común». Los franceses la oyeron primero a otros pueblos de la región de los Grandes Lagos, que llamaban así a los Inoka, y la escribieron «Illinois».</p>
  <p>El padre Marquette creyó que «Illinois» significaba «los hombres», y más tarde otros autores añadieron «los hombres completos» o «la gente completa». Son hermosas, pero no se sostienen. En la obra, «los hombres» aparece como lo que fue: una interpretación de Marquette.</p>"""),
("linea", "Línea de tiempo", """
  <ul class="linea">
   <li><b>Hacia 1050–1350</b>Florece Cahokia, la gran ciudad de los montículos de la cultura misisipiana, cerca del actual San Luis. Después de 1200 empezó a despoblarse; hacia 1350 estaba casi vacía.</li>
   <li><b>Siglo XVII</b>Los Inoka viven en aldeas en el valle del río Illinois y a ambos lados del Mississippi.</li>
   <li><b>1673</b>Jacques Marquette y Louis Jolliet bajan por el Mississippi. En una aldea Peoria los reciben con el calumet de la paz. Al volver, pasan por la Gran Aldea de los Kaskaskia, junto a Starved Rock.</li>
   <li><b>1675</b>Marquette funda una misión en la Gran Aldea de los Kaskaskia.</li>
   <li><b>Hacia 1700</b>Parte de los Michigamea, que vivían en el noreste de Arkansas, se une a los Kaskaskia.</li>
   <li><b>Después de 1763</b>Parte del pueblo se traslada a Missouri.</li>
   <li><b>1832</b>Por un tratado, los Peoria y los Kaskaskia ceden sus últimas tierras y reciben tierras en Kansas, cerca de los Piankashaw y los Wea.</li>
   <li><b>1854</b>Los Peoria, Kaskaskia, Piankashaw y Wea se unen formalmente en una sola tribu.</li>
   <li><b>1867</b>Se trasladan al Territorio Indio, hoy Oklahoma.</li>
   <li><b>1959</b>El gobierno federal pone fin a su relación con la tribu, como hizo con muchas otras en esa época.</li>
   <li><b>1978</b>El Congreso restituye el reconocimiento federal a la tribu Peoria.</li>
   <li><b>Hoy</b>La <span lang="en">Peoria Tribe of Indians of Oklahoma</span> es una nación soberana con su propio gobierno, y trabaja para recuperar su lengua.</li>
  </ul>"""),
("vida", "La vida en las aldeas", """
  <h3>Las casas</h3>
  <p>En las aldeas de verano, las familias vivían en <strong>casas largas</strong>: estructuras de varas curvadas, de hasta unos 18 metros, donde podían vivir varias familias alrededor de fogones compartidos. En invierno usaban <strong>wigwams</strong>, más pequeños y en forma de cúpula. Las dos se cubrían con <strong>esteras de junco</strong> que tejían las mujeres; una doble capa protegía de la lluvia y la nieve. No vivían en tipis.</p>
  <h3>El cultivo y la caza</h3>
  <p>Las mujeres cultivaban <strong>maíz</strong>, el alimento principal, junto con <strong>frijol</strong> y <strong>calabaza</strong>, y recogían plantas silvestres, nueces, bayas y miel. Las tres plantas se ayudan: el maíz sirve de apoyo al frijol, el frijol enriquece el suelo y las hojas de la calabaza lo mantienen húmedo. Hoy muchos pueblos las llaman las «Tres Hermanas», un nombre que viene de la tradición haudenosaunee (iroquesa).</p>
  <p>Los hombres cazaban, sobre todo <strong>bisontes</strong> en la pradera, y se encargaban de la guerra. A fines del verano y en invierno, las aldeas se dividían en grupos más pequeños que iban a los campamentos de caza.</p>
  <h3>Los ríos y el comercio</h3>
  <p>Los ríos eran caminos. Los Inoka viajaban en <strong>canoas talladas en un solo tronco</strong> (piraguas), no en canoas de corteza, e intercambiaban pieles, carne seca, herramientas de piedra, conchas y cerámica con otras aldeas y pueblos.</p>"""),
("gobierno", "El gobierno y el calumet", """
  <p>No había un rey ni un gobierno central. Cada aldea tenía sus jefes: <strong>jefes de paz</strong>, que organizaban la caza y las relaciones con otros pueblos, y <strong>jefes de guerra</strong>. Los cargos no se heredaban sin más: dependían del respeto ganado, y los jefes guiaban con la persuasión, no con la fuerza. Las decisiones importantes se tomaban en gran parte <strong>por consenso</strong>, escuchando a los ancianos y a los clanes.</p>
  <p>El <strong>calumet</strong> era una pipa ceremonial. Ofrecerlo era una forma solemne de recibir a los visitantes y de sellar la paz; quien lo llevaba podía viajar seguro. Por ser un objeto sagrado, en la obra se nombra pero no aparece en escena.</p>"""),
("mitos", "Mitos, hechos y preguntas abiertas", """
  <p class="mito">Mito: «Illinois (o Illiniwek) significa “los hombres completos”.»</p>
  <p class="hecho">Hecho: fue una interpretación posterior a Marquette. La palabra significa más o menos «el que habla de la manera común». Y el nombre propio del pueblo, <em>Inoka</em>, tiene un significado desconocido.</p>
  <p class="mito">Mito: «Vivían en tipis y llevaban grandes penachos de plumas.»</p>
  <p class="hecho">Hecho: vivían en casas largas y wigwams cubiertos de esteras de junco. Los penachos de las películas vienen de algunos pueblos de las Grandes Llanuras, y en esos pueblos tienen un significado ceremonial.</p>
  <p class="mito">Pregunta abierta: «¿Construyeron los Inoka la ciudad de Cahokia?»</p>
  <p class="hecho">Lo que sabemos: Cahokia es de la cultura misisipiana y floreció siglos antes de 1673. El sitio tomó su nombre de los Cahokia, una tribu de la Confederación que vivía cerca en la época colonial. La tribu Peoria se considera descendiente de los pueblos que construyeron los grandes montículos; los arqueólogos siguen estudiando esa relación.</p>
  <p class="mito">Mito: «Tenían un rey o un gran jefe que mandaba sobre todos.»</p>
  <p class="hecho">Hecho: eran aldeas aliadas y autónomas, con jefes de paz y de guerra, que decidían en gran parte por consenso.</p>
  <p class="mito">Mito: «Los indígenas de Illinois desaparecieron.»</p>
  <p class="hecho">Hecho: sus descendientes forman hoy la tribu Peoria de Oklahoma, una nación reconocida por el gobierno federal.</p>"""),
("hoy", "La tribu Peoria hoy", f"""
  <p>La <span lang="en">Peoria Tribe of Indians of Oklahoma</span> reúne a descendientes de los Peoria, Kaskaskia, Piankashaw y Wea. Tiene su propio gobierno, elegido por sus ciudadanos, y su sede en Miami, Oklahoma.</p>
  <p>Su lengua, el <strong>miami-illinois</strong>, ya no tiene hablantes nativos, pero las naciones Peoria y Miami trabajan para recuperarla, y hoy niños y jóvenes la están aprendiendo de nuevo.</p>
  <p>Su página oficial: <a href="{PEORIA}" target="_blank" rel="noopener noreferrer">peoriatribe.com</a>.</p>"""),
("vocabulario", "Vocabulario", """
  <div class="envoltura-tabla"><table class="tabla">
   <caption class="sr">Vocabulario</caption>
   <thead><tr><th scope="col">Palabra</th><th scope="col">Qué significa</th></tr></thead>
   <tbody>
    <tr><th scope="row">Confederación</th><td>Unión de varios pueblos que se ayudan, pero que siguen siendo libres.</td></tr>
    <tr><th scope="row">Aldea</th><td>Pueblo pequeño. Las aldeas Inoka estaban junto a los ríos.</td></tr>
    <tr><th scope="row">Consenso</th><td>Acuerdo al que se llega escuchando a todos.</td></tr>
    <tr><th scope="row">Calumet</th><td>Pipa ceremonial que se ofrecía para recibir a los visitantes y sellar la paz.</td></tr>
    <tr><th scope="row">Estera</th><td>Tejido de juncos o cañas. Cubría las casas.</td></tr>
    <tr><th scope="row">Pradera</th><td>Llanura de hierbas altas y pocos árboles.</td></tr>
    <tr><th scope="row">Piragua</th><td>Canoa tallada en un solo tronco.</td></tr>
    <tr><th scope="row">Reciprocidad</th><td>Dar y recibir: ayudarse unos a otros.</td></tr>
    <tr><th scope="row">Nación soberana</th><td>Pueblo que tiene su propio gobierno. Las tribus reconocidas en EE. UU. lo son.</td></tr>
   </tbody>
  </table></div>"""),
("actividades", "Actividades por grado", """
  <ul class="tarjetas">
   <li><h3>Prekínder y kínder</h3><p><strong>La pradera se mueve.</strong> Escuchar el tambor y moverse como el viento, las flores, las aves y los bisontes; despacio, rápido, quietos.</p><p>Contar cuántos animales y plantas de la pradera conocen.</p></li>
   <li><h3>1.º y 2.º</h3><p><strong>Las tres hermanas en un vaso.</strong> Sembrar una semilla de maíz, una de frijol y una de calabaza en un vaso transparente y observar cómo crecen.</p><p><strong>Tejer una estera</strong> con tiras de papel, y comprobar que tejida resiste más que una sola tira.</p></li>
   <li><h3>3.º y 4.º</h3><p><strong>Los ríos son caminos.</strong> En un mapa de Illinois, encontrar los ríos Illinois y Mississippi, Starved Rock y el lago Peoria.</p><p><strong>Trueque:</strong> intercambiar objetos de clase sin dinero y hablar de qué hace justo un intercambio.</p></li>
   <li><h3>5.º y 6.º</h3><p><strong>Decidir por consenso.</strong> Tomar una decisión de la clase escuchando a todos hasta llegar a un acuerdo, y compararla con una votación.</p><p><strong>Fuentes:</strong> comparar lo que escribieron los franceses en 1673 con lo que dice hoy la tribu Peoria en su página. ¿Quién cuenta la historia?</p></li>
  </ul>"""),
("respeto", "Cómo hablar del tema con respeto", """
  <ul>
   <li>Hablar de <strong>pueblos concretos</strong> (Inoka, Peoria, Kaskaskia) en lugar de «los indios» en general.</li>
   <li>Usar el <strong>presente</strong> cuando corresponde: la tribu Peoria existe hoy.</li>
   <li>No pedir a los niños que se disfracen, que imiten gritos de guerra ni que hagan objetos sagrados como «manualidad».</li>
   <li>Si hay en la clase niños de origen indígena, de cualquier pueblo, dejar que compartan solo si ellos quieren.</li>
  </ul>"""),
("fuentes", "Fuentes y para saber más", f"""
  <ul>
   <li><a href="https://peoriatribe.com/welcome/history/" target="_blank" rel="noopener noreferrer">Peoria Tribe of Indians of Oklahoma: su historia</a></li>
   <li><a href="https://museum.state.il.us/muslink/nat_amer/post/htmls/te_houses.html" target="_blank" rel="noopener noreferrer">Illinois State Museum: las casas de los Illinois</a></li>
   <li><a href="https://dnrhistoric.illinois.gov/content/dam/soi/en/web/dnrhistoric/research/documents/illinivol1n1.pdf" target="_blank" rel="noopener noreferrer">Illinois Department of Natural Resources: los Illiniwek</a></li>
   <li><a href="https://www.okhistory.org/publications/enc/entry?entry=PE013" target="_blank" rel="noopener noreferrer">Oklahoma Historical Society: Peoria</a></li>
   <li><a href="{PEORIA}" target="_blank" rel="noopener noreferrer">Peoria Tribe of Indians of Oklahoma</a></li>
   <li><a href="https://wikiwand.com/en/articles/Illinois_Confederacy" target="_blank" rel="noopener noreferrer">Illinois Confederation (resumen enciclopédico)</a></li>
  </ul>"""),
        ]
        nav = [("breve","En breve"),("nombre","El nombre"),("linea","Línea de tiempo"),("vida","La vida en las aldeas"),("gobierno","Gobierno y calumet"),("mitos","Mitos y hechos"),("hoy","La tribu Peoria hoy"),("vocabulario","Vocabulario"),("actividades","Actividades por grado"),("respeto","Hablar con respeto"),("fuentes","Fuentes")]
        herr = '<button type="button" onclick="window.print()">🖨️ Imprimir o guardar en PDF</button><a href="obra-inoka-produccion-es.html">🎬 Guía de producción</a>'
        return guia(L, "obra-inoka-historia-es.html", "obra-inoka-historia-en.html", "Inoka · Guía histórica", "Inoka · Guía histórica para el docente",
                    "Quiénes eran los Inoka, cómo vivían, qué pasó después y quiénes son hoy, con mitos y hechos y actividades por grado.", herr, nav, sec,
                    "Guía histórica para el docente de «Inoka», de José M. Fernández: los Inoka o Illinois, el nombre, la vida en las aldeas, el gobierno, la tribu Peoria hoy, mitos y hechos y actividades por grado.")
    sec = [
("breve", "At a glance", """
  <ul>
   <li><strong>Who:</strong> the Inoka, whom the French called “Illinois.” They were a confederation of about twelve allied tribes or villages, including the Kaskaskia, Peoria, Cahokia, Tamaroa and, from around 1700, part of the Michigamea.</li>
   <li><strong>Where:</strong> the prairies and river valleys of the Illinois and Mississippi rivers, in what is now Illinois and nearby areas.</li>
   <li><strong>How they lived:</strong> in spring and summer, in large villages by the rivers, where women grew corn, beans and squash; in winter, in smaller hunting camps. Men hunted bison on the prairie.</li>
   <li><strong>Today:</strong> their descendants are the Peoria Tribe of Indians of Oklahoma, headquartered in Miami, Oklahoma.</li>
  </ul>"""),
("nombre", "The name: Inoka and Illinois", """
  <p><strong>Inoka</strong> is the name the people called themselves, as French missionaries wrote down. Its meaning is unknown.</p>
  <p><strong>Illinois</strong> comes from a word in their own language, Miami-Illinois, meaning roughly “one who speaks in the ordinary way.” The French first heard it from other peoples of the Great Lakes region, who used it for the Inoka, and wrote it as “Illinois.”</p>
  <p>Father Marquette believed “Illinois” meant “the men,” and later writers added “the complete men” or “the complete people.” They are beautiful, but they do not hold up. In the play, “the men” appears as what it was: Marquette's interpretation.</p>"""),
("linea", "Timeline", """
  <ul class="linea">
   <li><b>About 1050–1350</b>Cahokia, the great city of mounds of the Mississippian culture, flourishes near present-day St. Louis. It began to empty after 1200 and was nearly abandoned by about 1350.</li>
   <li><b>1600s</b>The Inoka live in villages in the Illinois River valley and on both sides of the Mississippi.</li>
   <li><b>1673</b>Jacques Marquette and Louis Jolliet travel down the Mississippi. In a Peoria village, they are welcomed with the peace calumet. On their way back, they pass the Grand Village of the Kaskaskia, near Starved Rock.</li>
   <li><b>1675</b>Marquette founds a mission at the Grand Village of the Kaskaskia.</li>
   <li><b>Around 1700</b>Part of the Michigamea, who lived in northeastern Arkansas, join the Kaskaskia.</li>
   <li><b>After 1763</b>Part of the people move to Missouri.</li>
   <li><b>1832</b>By treaty, the Peoria and Kaskaskia give up their last lands and receive land in Kansas, near the Piankashaw and Wea.</li>
   <li><b>1854</b>The Peoria, Kaskaskia, Piankashaw and Wea formally unite as one tribe.</li>
   <li><b>1867</b>They move to Indian Territory, today Oklahoma.</li>
   <li><b>1959</b>The federal government ends its relationship with the tribe, as it did with many others at that time.</li>
   <li><b>1978</b>Congress restores federal recognition to the Peoria Tribe.</li>
   <li><b>Today</b>The Peoria Tribe of Indians of Oklahoma is a sovereign nation with its own government, and it is working to bring its language back.</li>
  </ul>"""),
("vida", "Life in the villages", """
  <h3>Houses</h3>
  <p>In the summer villages, families lived in <strong>longhouses</strong>: frames of bent poles, up to about 58 feet long, where several families lived around shared hearths. In winter they used smaller, dome-shaped <strong>wigwams</strong>. Both were covered with <strong>rush mats</strong> woven by the women; a double layer kept out rain and snow. They did not live in tipis.</p>
  <h3>Farming and hunting</h3>
  <p>Women grew <strong>corn</strong>, the main food, along with <strong>beans</strong> and <strong>squash</strong>, and gathered wild plants, nuts, berries and honey. The three plants help one another: corn supports the beans, beans enrich the soil, and squash leaves keep it moist. Many peoples today call them the “Three Sisters,” a name that comes from Haudenosaunee (Iroquois) tradition.</p>
  <p>Men hunted, above all <strong>bison</strong> on the prairie, and took care of warfare. In late summer and winter, the villages split into smaller groups that went to hunting camps.</p>
  <h3>Rivers and trade</h3>
  <p>Rivers were roads. The Inoka traveled in <strong>canoes carved from a single tree trunk</strong> (dugouts), not bark canoes, and traded pelts, dried meat, stone tools, shells and pottery with other villages and peoples.</p>"""),
("gobierno", "Government and the calumet", """
  <p>There was no king and no central government. Each village had its own chiefs: <strong>peace chiefs</strong>, who organized hunts and relations with other peoples, and <strong>war chiefs</strong>. These positions were not simply inherited: they depended on earned respect, and chiefs led by persuasion, not force. Important decisions were largely made <strong>by consensus</strong>, listening to elders and clans.</p>
  <p>The <strong>calumet</strong> was a ceremonial pipe. Offering it was a solemn way to welcome visitors and seal peace; whoever carried it could travel safely. Because it is a sacred object, the play mentions it but does not show it on stage.</p>"""),
("mitos", "Myths, facts and open questions", """
  <p class="mito">Myth: “Illinois (or Illiniwek) means ‘the complete men.’”</p>
  <p class="hecho">Fact: that came from later interpretations of Marquette. The word means roughly “one who speaks in the ordinary way.” The people's own name, <em>Inoka</em>, has an unknown meaning.</p>
  <p class="mito">Myth: “They lived in tipis and wore big feather headdresses.”</p>
  <p class="hecho">Fact: they lived in longhouses and wigwams covered with rush mats. The headdresses in movies come from some peoples of the Great Plains, where they have a ceremonial meaning.</p>
  <p class="mito">Open question: “Did the Inoka build the city of Cahokia?”</p>
  <p class="hecho">What we know: Cahokia belongs to the Mississippian culture and flourished centuries before 1673. The site was named after the Cahokia, a tribe of the Confederation that lived nearby in colonial times. The Peoria Tribe sees itself as descended from the peoples who built the great mounds; archaeologists are still studying that connection.</p>
  <p class="mito">Myth: “They had a king or a great chief who ruled everyone.”</p>
  <p class="hecho">Fact: they were allied, independent villages with peace and war chiefs, which largely decided by consensus.</p>
  <p class="mito">Myth: “The Native peoples of Illinois disappeared.”</p>
  <p class="hecho">Fact: their descendants are today the Peoria Tribe of Oklahoma, a federally recognized nation.</p>"""),
("hoy", "The Peoria Tribe today", f"""
  <p>The Peoria Tribe of Indians of Oklahoma brings together descendants of the Peoria, Kaskaskia, Piankashaw and Wea. It has its own government, elected by its citizens, and its headquarters in Miami, Oklahoma.</p>
  <p>Their language, <strong>Miami-Illinois</strong>, no longer has native speakers, but the Peoria and Miami nations are working to bring it back, and today children and young people are learning it again.</p>
  <p>Official website: <a href="{PEORIA}" target="_blank" rel="noopener noreferrer">peoriatribe.com</a>.</p>"""),
("vocabulario", "Vocabulary", """
  <div class="envoltura-tabla"><table class="tabla">
   <caption class="sr">Vocabulary</caption>
   <thead><tr><th scope="col">Word</th><th scope="col">What it means</th></tr></thead>
   <tbody>
    <tr><th scope="row">Confederation</th><td>A union of several peoples who help one another but stay free.</td></tr>
    <tr><th scope="row">Village</th><td>A small town. The Inoka villages were by the rivers.</td></tr>
    <tr><th scope="row">Consensus</th><td>An agreement reached by listening to everyone.</td></tr>
    <tr><th scope="row">Calumet</th><td>A ceremonial pipe offered to welcome visitors and seal peace.</td></tr>
    <tr><th scope="row">Mat</th><td>Woven rushes or reeds. Mats covered the houses.</td></tr>
    <tr><th scope="row">Prairie</th><td>Flat land with tall grasses and few trees.</td></tr>
    <tr><th scope="row">Dugout canoe</th><td>A canoe carved from a single tree trunk.</td></tr>
    <tr><th scope="row">Reciprocity</th><td>Giving and receiving: helping one another.</td></tr>
    <tr><th scope="row">Sovereign nation</th><td>A people with its own government. Federally recognized tribes in the U.S. are sovereign nations.</td></tr>
   </tbody>
  </table></div>"""),
("actividades", "Activities by grade", """
  <ul class="tarjetas">
   <li><h3>Pre-K and K</h3><p><strong>The prairie moves.</strong> Listen to the drum and move like the wind, the flowers, the birds and the bison: slowly, quickly, frozen.</p><p>Count how many prairie animals and plants they know.</p></li>
   <li><h3>1st and 2nd</h3><p><strong>Three sisters in a cup.</strong> Plant a corn seed, a bean seed and a squash seed in a clear cup and watch them grow.</p><p><strong>Weave a mat</strong> with paper strips, and test that the woven mat is stronger than a single strip.</p></li>
   <li><h3>3rd and 4th</h3><p><strong>Rivers are roads.</strong> On a map of Illinois, find the Illinois and Mississippi rivers, Starved Rock and Peoria Lake.</p><p><strong>Barter:</strong> trade classroom objects without money and talk about what makes a trade fair.</p></li>
   <li><h3>5th and 6th</h3><p><strong>Decide by consensus.</strong> Make a class decision by listening to everyone until there is agreement, and compare it with a vote.</p><p><strong>Sources:</strong> compare what the French wrote in 1673 with what the Peoria Tribe says today on its website. Who tells the story?</p></li>
  </ul>"""),
("respeto", "Talking about this topic with respect", """
  <ul>
   <li>Talk about <strong>specific peoples</strong> (Inoka, Peoria, Kaskaskia) rather than “Indians” in general.</li>
   <li>Use the <strong>present tense</strong> when it applies: the Peoria Tribe exists today.</li>
   <li>Do not ask children to dress up, imitate war cries or make sacred objects as a “craft.”</li>
   <li>If there are children of Native heritage in the class, from any people, let them share only if they want to.</li>
  </ul>"""),
("fuentes", "Sources and further reading", f"""
  <ul>
   <li><a href="https://peoriatribe.com/welcome/history/" target="_blank" rel="noopener noreferrer">Peoria Tribe of Indians of Oklahoma: history</a></li>
   <li><a href="https://museum.state.il.us/muslink/nat_amer/post/htmls/te_houses.html" target="_blank" rel="noopener noreferrer">Illinois State Museum: Illinois houses</a></li>
   <li><a href="https://dnrhistoric.illinois.gov/content/dam/soi/en/web/dnrhistoric/research/documents/illinivol1n1.pdf" target="_blank" rel="noopener noreferrer">Illinois Department of Natural Resources: the Illiniwek</a></li>
   <li><a href="https://www.okhistory.org/publications/enc/entry?entry=PE013" target="_blank" rel="noopener noreferrer">Oklahoma Historical Society: Peoria</a></li>
   <li><a href="{PEORIA}" target="_blank" rel="noopener noreferrer">Peoria Tribe of Indians of Oklahoma</a></li>
   <li><a href="https://wikiwand.com/en/articles/Illinois_Confederacy" target="_blank" rel="noopener noreferrer">Illinois Confederation (encyclopedia summary)</a></li>
  </ul>"""),
    ]
    nav = [("breve","At a glance"),("nombre","The name"),("linea","Timeline"),("vida","Village life"),("gobierno","Government and calumet"),("mitos","Myths and facts"),("hoy","The Peoria Tribe today"),("vocabulario","Vocabulary"),("actividades","Activities by grade"),("respeto","Talking with respect"),("fuentes","Sources")]
    herr = '<button type="button" onclick="window.print()">🖨️ Print or save as PDF</button><a href="obra-inoka-produccion-en.html">🎬 Production guide</a>'
    return guia(L, "obra-inoka-historia-en.html", "obra-inoka-historia-es.html", "Inoka · Historical guide", "Inoka · Historical guide for teachers",
                "Who the Inoka were, how they lived, what happened next and who they are today, with myths and facts and activities by grade.", herr, nav, sec,
                "Historical guide for teachers for “Inoka,” a play by José M. Fernández: the Inoka or Illinois, the name, village life, government, the Peoria Tribe today, myths and facts and activities by grade.")

# =========================================================================== CARTEL
CAR = {
 "es": dict(otro="obra-inoka-cartel-en.html", volver="obra-inoka-produccion-es.html", volver_txt="← Guía de producción", titulo_pag="Inoka · Cartel",
   instr="Escriba en los espacios punteados (haga clic sobre ellos) el nombre de la escuela, la fecha, la hora, el lugar y la ciudad. Después pulse «Imprimir». Se imprime en una hoja carta, en vertical.",
   imprimir="🖨️ Imprimir el cartel", escuela="Nombre de la escuela", presenta="presenta", sub="El aliento de la pradera y la gente de Illinois",
   obra=f"Obra de {AUTOR}", elenco="Con todos los alumnos, de prekínder a 6.º grado", lema="La tierra · El río · El consejo · El pueblo que sigue vivo",
   lf="Día", lh="Hora", ll="Lugar", f="Día y fecha", h="Hora", l="Lugar", ciudad="Ciudad, estado", entrada="Entrada libre",
   alt="Una planta de maíz con su mazorca en una pradera dorada; al fondo, colinas suaves, el sol del atardecer y una bandada de aves.",
   pie=f"«Inoka: El aliento de la pradera y la gente de Illinois» · Obra de {AUTOR} · Lumi, www.lumi-educa.com"),
 "en": dict(otro="obra-inoka-cartel-es.html", volver="obra-inoka-produccion-en.html", volver_txt="← Production guide", titulo_pag="Inoka · Poster",
   instr="Click the dotted spaces and type the school's name, date, time, place and city. Then press “Print”. It prints on one letter-size sheet, portrait.",
   imprimir="🖨️ Print the poster", escuela="School name", presenta="presents", sub="The Breath of the Prairie and the People of Illinois",
   obra=f"A play by {AUTOR}", elenco="With all our students, from Pre-K to 6th grade", lema="The land · The river · The council · A people still here today",
   lf="Date", lh="Time", ll="Place", f="Day and date", h="Time", l="Place", ciudad="City, State", entrada="Free admission",
   alt="A corn plant with its ear on a golden prairie; behind it, gentle hills, the evening sun and a flock of birds.",
   pie=f"“Inoka: The Breath of the Prairie and the People of Illinois” · A play by {AUTOR} · Lumi, www.lumi-educa.com"),
}

def cartel(L):
    c = CAR[L]; cm = COM[L]
    campo = lambda cls, ph: f'<span class="campo {cls}" contenteditable="true" role="textbox" aria-label="{ph}" data-ph="{ph}"></span>'
    idioma = (f'<span aria-current="true">Español</span><a href="{c["otro"]}" lang="en" hreflang="en">English</a>' if L == "es"
              else f'<a href="{c["otro"]}" lang="es" hreflang="es">Español</a><span aria-current="true">English</span>')
    return f'''<!doctype html>
<!-- Cartel de «Inoka», obra de {AUTOR} · Lumi · CC BY-NC-SA 4.0 · generado con herramientas/gen_inoka_materiales.py -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c["titulo_pag"]} · Lumi</title>
<meta name="author" content="{AUTOR}">
<link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="lumi.css?v=6">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;700&display=swap" rel="stylesheet">
<style>
 .ayuda{{max-width:820px;margin:1rem auto;padding:0 16px}}
 .ayuda button{{display:inline-flex;align-items:center;min-height:44px;padding:0 1rem;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);font:inherit;font-weight:700;cursor:pointer}}
 .cartel{{width:min(640px,100%);margin:0 auto 2rem;aspect-ratio:8.5/11;container-type:inline-size;background:#3b2410;color:#fff4dc;border-radius:14px;overflow:hidden;box-shadow:0 6px 24px rgba(0,0,0,.18);display:flex;flex-direction:column}}
 .c-arriba{{padding:5% 6% 3%;text-align:center}}
 .c-esc{{margin:0;font-size:3.4cqw;color:#f2c26b;font-weight:700}}
 .c-tit{{font-family:Fredoka,system-ui,sans-serif;font-weight:700;font-size:13cqw;line-height:1;margin:.12em 0 0;color:#fff4dc;letter-spacing:.04em}}
 .c-sub{{margin:.25em 0 0;font-size:3.8cqw;color:#f6dfb0}}
 .c-obra{{margin:.35em 0 0;font-size:3.2cqw;font-weight:700;color:#f2c26b}}
 .c-img{{flex:1;min-height:0;display:flex;justify-content:center;align-items:center;padding:0 9%}}
 .c-img img{{height:100%;max-width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:10px;box-shadow:0 4px 18px rgba(0,0,0,.35)}}
 .c-abajo{{padding:3% 6% 5%;text-align:center}}
 .c-elenco{{margin:0;font-size:3.3cqw;font-weight:700}}
 .c-lema{{margin:.3em 0 .5em;font-size:2.6cqw;color:#f6dfb0;letter-spacing:.04em}}
 .c-datos{{display:flex;flex-wrap:wrap;justify-content:center;gap:.2em 1.2em;font-size:3.3cqw;font-weight:700}}
 .c-datos .lbl{{color:#f2c26b;margin-right:.25em}}
 .c-lugar{{margin:.4em 0 0;font-size:2.8cqw}}
 .c-cred{{margin:.6em 0 0;font-size:2cqw;opacity:.85}}
 .campo{{display:inline-block;min-width:5.5em;border-bottom:2px dotted #f2c26b;outline:none;padding:0 .15em}}
 .campo:empty::before{{content:attr(data-ph);color:#cdb48a;font-weight:400;font-style:italic}}
 .campo:focus{{background:rgba(242,194,107,.12)}}
 @media print{{
  @page{{size:letter portrait;margin:0}}
  html,body{{background:#3b2410;margin:0;padding:0}} .cabecera,.ayuda,.pie,.saltar{{display:none!important}}
  main{{margin:0;padding:0}}
  .cartel{{width:100vw;height:100vh;aspect-ratio:auto;margin:0;border-radius:0;box-shadow:none;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
  .campo,.campo:focus{{border-bottom:0;background:none}} .campo:empty::before{{content:""}}
 }}
</style>
</head>
<body>
<a class="saltar" href="#contenido">{cm["saltar"]}</a>
<header class="cabecera">
 <div class="envoltura">
  <a class="marca" href="{cm["inicio"]}"><img src="lumi-logo-horizontal.svg" alt="Lumi" width="560" height="240"></a>
  <div class="idioma" role="group" aria-label="{cm["idioma_lbl"]}">{idioma}</div>
 </div>
</header>
<div class="ayuda">
 <p style="margin:.4rem 0"><a href="{c["volver"]}">{c["volver_txt"]}</a></p>
 <p>{c["instr"]}</p>
 <p><button type="button" onclick="window.print()">{c["imprimir"]}</button></p>
</div>
<main id="contenido" tabindex="-1">
<article class="cartel" aria-label="{c["titulo_pag"]}">
 <div class="c-arriba">
  <p class="c-esc">{campo("escuela", c["escuela"])} {c["presenta"]}</p>
  <h1 class="c-tit">INOKA</h1>
  <p class="c-sub">{c["sub"]}</p>
  <p class="c-obra">{c["obra"]}</p>
 </div>
 <div class="c-img"><img src="inoka-cartel.jpg" alt="{c["alt"]}" width="1200" height="1200"></div>
 <div class="c-abajo">
  <p class="c-elenco">{c["elenco"]}</p>
  <p class="c-lema">{c["lema"]}</p>
  <div class="c-datos">
   <span><span class="lbl">{c["lf"]}:</span>{campo("fecha", c["f"])}</span>
   <span><span class="lbl">{c["lh"]}:</span>{campo("hora", c["h"])}</span>
   <span><span class="lbl">{c["ll"]}:</span>{campo("lugar", c["l"])}</span>
  </div>
  <p class="c-lugar">{campo("ciudad", c["ciudad"])} · {c["entrada"]}</p>
  <p class="c-cred">{c["pie"]}</p>
 </div>
</article>
</main>
<footer class="pie"><div class="envoltura"><p>{c["pie"]}</p></div></footer>
<script>
(function(){{
  var K="inoka-cartel-"+document.documentElement.lang, cs=document.querySelectorAll(".campo");
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

# =========================================================================== PROGRAMA DE MANO
PRO = {
 "es": dict(otro="obra-inoka-programa-en.html", volver="obra-inoka-produccion-es.html", volver_txt="← Guía de producción", titulo_pag="Inoka · Programa de mano",
   instr="Escriba en los espacios punteados el nombre de la escuela, la fecha y los nombres del elenco. Después pulse «Imprimir». Ocupa dos páginas: se puede imprimir a doble cara y doblar.",
   imprimir="🖨️ Imprimir el programa", cab="Programa de mano", escuela="Nombre de la escuela", fecha="Fecha y lugar de la función",
   sub="El aliento de la pradera y la gente de Illinois", obra=f"Obra de {AUTOR}",
   bienv_t="Bienvenidos",
   bienv="Gracias por acompañarnos. Esta obra, en la que participa toda la escuela, cuenta la historia de los Inoka, los pueblos de las praderas y los ríos de Illinois, y la de sus descendientes de hoy, la tribu Peoria de Oklahoma. Habla de la tierra que alimenta cuando se trabaja en común, de los ríos que unen a las aldeas y de un consejo que decide escuchando a todos.",
   actos_t="La obra",
   actos=[("Acto I · El latido de la pradera y el río", "Prekínder y kínder", "La pradera, el río y sus seres vivos, con tambor de mano y palos de lluvia."),
          ("Acto II · Las tres hermanas y el hogar de esteras", "1.º y 2.º", "El cultivo del maíz, el frijol y la calabaza y las casas cubiertas de esteras. Canción: «Raíz con raíz»."),
          ("Acto III · Las rutas del río y el comercio entre aldeas", "3.º y 4.º", "Canoas talladas en un solo tronco y el intercambio entre aldeas."),
          ("Acto IV · La asamblea de las aldeas y la sabiduría del consejo", "5.º y 6.º", "Las decisiones por consenso, el calumet de la paz y la llegada de los franceses en 1673."),
          ("Acto V · El legado vivo de los Inoka", "Toda la escuela", "La tribu Peoria de Oklahoma hoy y su lengua, que vuelve. Canción final: «Legado de la pradera».")],
   rep_t="Reparto", th=("Papel", "Grado", "Interpretado por"),
   reparto=[("Narradores 1 y 2","6.º"),("La naturaleza: viento, flores, aves y bisontes","Prekínder y kínder"),("Músicos","1.º y 2.º"),("Niño Maíz · Niña Frijol · Niña Calabaza","1.º y 2.º"),("Agricultora · Tejedora","2.º"),("Coro «Raíz con raíz»","1.º y 2.º"),("Los ríos","3.º y 4.º"),("Mensajero de la aldea","3.º"),("Navegante Peoria · Comerciante Kaskaskia","4.º"),("Guardiana de la Memoria","6.º"),("Líderes del consejo Kaskaskia y Peoria","5.º y 6.º"),("Estudiantes del acto V","1.º a 6.º"),("Equipo técnico, apuntadores y guías","3.º a 6.º")],
   notas_t="Para saber más",
   notas=["<strong>Inoka</strong> es el nombre que el pueblo se daba a sí mismo; su significado se desconoce. «Illinois» viene de una palabra de su lengua que significa «el que habla de la manera común».",
          "Vivían en <strong>casas largas y wigwams cubiertos de esteras de junco</strong>, no en tipis, y viajaban por los ríos en <strong>canoas talladas en un solo tronco</strong>.",
          "Las aldeas eran autónomas y decidían en gran parte <strong>por consenso</strong>.",
          "Sus descendientes forman hoy la <strong><span lang=\"en\">Peoria Tribe of Indians of Oklahoma</span></strong>, una nación soberana. Su lengua, el miami-illinois, se está recuperando: niños y jóvenes de las naciones Peoria y Miami la están aprendiendo de nuevo."],
   respeto="Por respeto a un pueblo que sigue vivo, en esta obra nadie se disfraza de indígena ni se usan objetos ceremoniales: cada personaje se reconoce por lo que hace.",
   agr_t="Agradecimientos",
   agr="A la <span lang=\"en\">Peoria Tribe of Indians of Oklahoma</span>, por mantener viva la historia y la lengua de los Inoka. A las familias, los docentes y todo el personal de la escuela.",
   cred=f"«Inoka: El aliento de la pradera y la gente de Illinois» · Obra de {AUTOR} · Canciones «Raíz con raíz» y «Legado de la pradera», creadas para la obra · Lumi, www.lumi-educa.com · CC BY-NC-SA 4.0"),
 "en": dict(otro="obra-inoka-programa-es.html", volver="obra-inoka-produccion-en.html", volver_txt="← Production guide", titulo_pag="Inoka · Program",
   instr="Type the school's name, the date and the cast names in the dotted spaces. Then press “Print”. It takes two pages: it can be printed double-sided and folded.",
   imprimir="🖨️ Print the program", cab="Program", escuela="School name", fecha="Date and place of the performance",
   sub="The Breath of the Prairie and the People of Illinois", obra=f"A play by {AUTOR}",
   bienv_t="Welcome",
   bienv="Thank you for joining us. This play, with the whole school taking part, tells the story of the Inoka, the peoples of the prairies and rivers of Illinois, and of their descendants today, the Peoria Tribe of Oklahoma. It is about the land that feeds us when we work together, the rivers that connect the villages, and a council that decides by listening to everyone.",
   actos_t="The play",
   actos=[("Act I · The Heartbeat of the Prairie and the River", "Pre-K & K", "The prairie, the river and their living things, with hand drum and rain sticks."),
          ("Act II · The Three Sisters and the Home of Mats", "1st & 2nd", "Growing corn, beans and squash, and houses covered with mats. Song: “Raíz con raíz.”"),
          ("Act III · The River Routes and Trade Between Villages", "3rd & 4th", "Canoes carved from a single trunk and trade between villages."),
          ("Act IV · The Village Assembly and the Wisdom of the Council", "5th & 6th", "Decisions by consensus, the peace calumet and the arrival of the French in 1673."),
          ("Act V · The Living Legacy of the Inoka", "The whole school", "The Peoria Tribe of Oklahoma today and their language, which is coming back. Closing song: “Legado de la pradera.”")],
   rep_t="Cast", th=("Part", "Grade", "Played by"),
   reparto=[("Narrators 1 and 2","6th"),("Nature: wind, flowers, birds and bison","Pre-K & K"),("Musicians","1st & 2nd"),("Corn · Bean · Squash","1st & 2nd"),("Farmer · Weaver","2nd"),("“Raíz con raíz” chorus","1st & 2nd"),("The rivers","3rd & 4th"),("Village Messenger","3rd"),("Peoria Paddler · Kaskaskia Trader","4th"),("Keeper of Memory","6th"),("Kaskaskia and Peoria council leaders","5th & 6th"),("Students in Act V","1st to 6th"),("Tech crew, prompters and buddies","3rd to 6th")],
   notas_t="Did you know?",
   notas=["<strong>Inoka</strong> is the name the people called themselves; its meaning is unknown. “Illinois” comes from a word in their language meaning “one who speaks in the ordinary way.”",
          "They lived in <strong>longhouses and wigwams covered with rush mats</strong>, not tipis, and traveled the rivers in <strong>canoes carved from a single trunk</strong>.",
          "The villages were independent and largely decided <strong>by consensus</strong>.",
          "Their descendants are today the <strong>Peoria Tribe of Indians of Oklahoma</strong>, a sovereign nation. Their language, Miami-Illinois, is coming back: children and young people of the Peoria and Miami nations are learning it again."],
   respeto="Out of respect for a people who are still here today, no one in this play dresses up as a Native person or uses ceremonial objects: each character is recognized by what they do.",
   agr_t="Thank you",
   agr="To the Peoria Tribe of Indians of Oklahoma, for keeping the history and language of the Inoka alive. To the families, teachers and the whole school staff.",
   cred=f"“Inoka: The Breath of the Prairie and the People of Illinois” · A play by {AUTOR} · Songs “Raíz con raíz” and “Legado de la pradera,” written for the play · Lumi, www.lumi-educa.com · CC BY-NC-SA 4.0"),
}

def programa(L):
    c = PRO[L]; cm = COM[L]
    campo = lambda cls, ph, ancho="": f'<span class="campo {cls}" contenteditable="true" role="textbox" aria-label="{ph}" data-ph="{ph}"{ancho}></span>'
    idioma = (f'<span aria-current="true">Español</span><a href="{c["otro"]}" lang="en" hreflang="en">English</a>' if L == "es"
              else f'<a href="{c["otro"]}" lang="es" hreflang="es">Español</a><span aria-current="true">English</span>')
    actos = "\n".join(f'   <li><strong>{a}</strong> <span class="g">· {g}</span><br>{d}</li>' for a, g, d in c["actos"])
    filas = "\n".join(f'    <tr><td>{p}</td><td>{g}</td><td>{campo("n"+str(i), "…")}</td></tr>' for i, (p, g) in enumerate(c["reparto"]))
    notas = "\n".join(f"   <li>{n}</li>" for n in c["notas"])
    return f'''<!doctype html>
<!-- Programa de mano de «Inoka», obra de {AUTOR} · Lumi · CC BY-NC-SA 4.0 · generado con herramientas/gen_inoka_materiales.py -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c["titulo_pag"]} · Lumi</title>
<meta name="author" content="{AUTOR}">
<link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="lumi.css?v=6">
<style>
 .ayuda{{max-width:820px;margin:1rem auto;padding:0 16px}}
 .ayuda button{{display:inline-flex;align-items:center;min-height:44px;padding:0 1rem;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);font:inherit;font-weight:700;cursor:pointer}}
 .hoja{{max-width:820px;margin:0 auto 1.5rem;background:#fffaf0;border:1px solid #e3d3b4;border-radius:12px;padding:2rem 2.2rem;box-shadow:0 4px 18px rgba(0,0,0,.08);color:#2b1d10}}
 .hoja h1{{font-size:2.6rem;letter-spacing:.06em;margin:.2rem 0 0;color:#5a3412;text-align:center}}
 .hoja h2{{font-size:1.25rem;color:#5a3412;border-bottom:2px solid #e3c88f;padding-bottom:.15rem;margin:1.4rem 0 .5rem}}
 .hoja .centro{{text-align:center}}
 .hoja .sub{{font-size:1.2rem;margin:.2rem 0 0}}
 .hoja .obra{{font-weight:700;margin:.3rem 0 0}}
 .hoja .escuela{{font-weight:700;font-size:1.15rem;margin:0}}
 .hoja ol{{padding-left:1.3rem}} .hoja li{{margin:.45rem 0}}
 .hoja .g{{color:#7a5428}}
 .hoja table{{width:100%;border-collapse:collapse}}
 .hoja th,.hoja td{{border-bottom:1px solid #e3d3b4;padding:.4rem .4rem;text-align:left;vertical-align:top}}
 .hoja thead th{{color:#5a3412}}
 .hoja .respeto{{background:#f6ead0;border-left:5px solid #b07a2a;border-radius:8px;padding:.6rem .9rem;margin:1rem 0}}
 .hoja .cred{{font-size:.85rem;margin-top:1.4rem;text-align:center;color:#5c4630}}
 .campo{{display:inline-block;min-width:8em;border-bottom:2px dotted #b07a2a;outline:none;padding:0 .15em}}
 .campo:empty::before{{content:attr(data-ph);color:#9c8a74;font-style:italic}}
 @media print{{
  @page{{size:letter portrait;margin:12mm}}
  html,body{{background:#fff;margin:0;padding:0;font-size:10.5pt;line-height:1.35}} .cabecera,.ayuda,.pie,.saltar{{display:none!important}}
  main{{margin:0;padding:0}}
  .hoja{{border:0;box-shadow:none;padding:0;margin:0;max-width:none;background:#fff}}
  .hoja h1{{font-size:24pt}} .hoja h2{{font-size:13pt;margin:.8rem 0 .3rem}} .hoja li{{margin:.25rem 0}} .hoja th,.hoja td{{padding:.2rem .3rem}} .hoja .cred{{margin-top:.8rem}}
  .hoja.p2{{break-before:page}}
  .campo{{border-bottom:0}} .campo:empty::before{{content:""}}
 }}
</style>
</head>
<body>
<a class="saltar" href="#contenido">{cm["saltar"]}</a>
<header class="cabecera">
 <div class="envoltura">
  <a class="marca" href="{cm["inicio"]}"><img src="lumi-logo-horizontal.svg" alt="Lumi" width="560" height="240"></a>
  <div class="idioma" role="group" aria-label="{cm["idioma_lbl"]}">{idioma}</div>
 </div>
</header>
<div class="ayuda">
 <p style="margin:.4rem 0"><a href="{c["volver"]}">{c["volver_txt"]}</a></p>
 <p>{c["instr"]}</p>
 <p><button type="button" onclick="window.print()">{c["imprimir"]}</button></p>
</div>
<main id="contenido" tabindex="-1">
<section class="hoja" aria-label="{c["cab"]}">
 <p class="centro escuela">{campo("escuela", c["escuela"])}</p>
 <p class="centro" style="margin:.2rem 0 0;letter-spacing:.12em;text-transform:uppercase;font-size:.9rem;color:#7a5428">{c["cab"]}</p>
 <h1>INOKA</h1>
 <p class="centro sub">{c["sub"]}</p>
 <p class="centro obra">{c["obra"]}</p>
 <p class="centro">{campo("fecha", c["fecha"])}</p>
 <h2>{c["bienv_t"]}</h2>
 <p>{c["bienv"]}</p>
 <h2>{c["actos_t"]}</h2>
 <ol>
{actos}
 </ol>
 <p class="respeto">{c["respeto"]}</p>
</section>
<section class="hoja p2" aria-label="{c["rep_t"]}">
 <h2 style="margin-top:0">{c["rep_t"]}</h2>
 <table>
  <caption class="sr">{c["rep_t"]}</caption>
  <thead><tr><th scope="col">{c["th"][0]}</th><th scope="col">{c["th"][1]}</th><th scope="col">{c["th"][2]}</th></tr></thead>
  <tbody>
{filas}
  </tbody>
 </table>
 <h2>{c["notas_t"]}</h2>
 <ul>
{notas}
 </ul>
 <h2>{c["agr_t"]}</h2>
 <p>{c["agr"]}</p>
 <p class="cred">{c["cred"]}</p>
</section>
</main>
<footer class="pie"><div class="envoltura"><p>{cm["pie"]}</p></div></footer>
<script>
(function(){{
  var K="inoka-programa-"+document.documentElement.lang, cs=document.querySelectorAll(".campo");
  function clave(c){{ return c.className.split(" ")[1]; }}
  try{{ var g=JSON.parse(localStorage.getItem(K)||"{{}}"); cs.forEach(function(c){{ if(g[clave(c)]) c.textContent=g[clave(c)]; }}); }}catch(e){{}}
  window.addEventListener("beforeprint",function(){{ if(document.activeElement) document.activeElement.blur(); }});
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
        for nombre, fn in (("produccion", produccion), ("historia", historia), ("cartel", cartel), ("programa", programa)):
            with open(os.path.join(AQUI, f"obra-inoka-{nombre}-{L}.html"), "w", encoding="utf-8") as f:
                f.write(fn(L))
    print("ok")
