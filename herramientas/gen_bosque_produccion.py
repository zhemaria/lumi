"""
Guía de producción y cartel de «El bosque mágico», de Vicente Cañón Verdasco
(© 2019, www.obrasteatro.com), en español y en inglés.

La obra es del autor y se publica en Lumi con su autorización (octubre de 2026).
La guía (reparto por grados, ensayos, carta, cartel) es material de Lumi.

Produce:
  obra-bosque-magico-produccion-es.html / -en.html   guía de producción
  obra-bosque-magico-cartel-es.html / -en.html       cartel imprimible
Uso: python3 gen_bosque_produccion.py
"""
import os

AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTOR = "Vicente Cañón Verdasco"
CORREO = "tente.ca2017@gmail.com"
WEB = "https://www.obrasteatro.com/"

CSS = """
  .obra-cab{background:var(--cie);padding:1.4rem 0}
  .obra-cab h1{font-size:clamp(1.8rem,4.5vw,2.5rem)}
  .obra-cab .autor{margin:.3rem 0 0;font-weight:700;font-size:1.15rem}
  .herr{display:flex;gap:.5rem;flex-wrap:wrap;margin:1rem 0 0}
  .herr button,.herr a{display:inline-flex;align-items:center;min-height:44px;padding:0 1rem;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);font:inherit;font-weight:700;text-decoration:none;cursor:pointer}
  .tabla{width:100%;border-collapse:collapse;margin:.5rem 0 1rem}
  .tabla th,.tabla td{border:1px solid var(--borde);padding:.5rem .65rem;text-align:left;vertical-align:top}
  .tabla thead th{background:var(--cie)}
  .tabla tbody th{background:#F6FBFB;font-weight:700}
  .envoltura-tabla{overflow-x:auto}
  .nota{background:#FFF6DF;border-left:6px solid var(--ama);border-radius:10px;padding:.8rem 1rem;margin:1rem 0}
  .autor-caja{background:#F3EEFA;border-left:6px solid #5B3F8F;border-radius:10px;padding:.8rem 1rem;margin:1rem 0}
  .tarjetas{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1rem;list-style:none;padding:0;margin:0}
  .tarjetas li{border:2px solid var(--borde);border-radius:16px;padding:.9rem 1.1rem;background:#fff}
  .tarjetas h3{font-size:1.1rem;margin-bottom:.3rem}
  .tarjetas p{margin:.3rem 0}
  .chip{display:inline-block;font-size:.85rem;font-weight:700;background:var(--cie);border-radius:999px;padding:.05rem .6rem}
  .plano{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4px;margin:.6rem 0 .3rem;font-size:.92rem}
  .plano div{background:#F6FBFB;border:1px solid var(--borde);border-radius:8px;padding:.45rem .55rem;min-height:70px}
  .plano b{display:block;font-size:.8rem;text-transform:uppercase;letter-spacing:.03em;color:#2d5f69}
  .publico{text-align:center;font-weight:700;border-top:3px solid var(--pet);padding-top:.2rem;margin-bottom:1rem}
  .carta{border:2px dashed var(--pet);border-radius:14px;padding:1.2rem 1.4rem;background:#fff;margin:1rem 0}
  .hueco{display:inline-block;min-width:9em;border-bottom:2px solid var(--pet)}
  .talon{border-top:2px dashed var(--pet);margin-top:1rem;padding-top:.8rem}
  .casilla{display:inline-block;width:1em;height:1em;border:2px solid var(--pet);vertical-align:-2px;margin-right:.3rem}
  .lista-casillas{list-style:none;padding-left:0}
  figure.info{margin:1rem 0 1.6rem}
  figure.info img,video.guia{display:block;width:100%;height:auto;border-radius:14px;border:1px solid var(--borde);background:#000}
  figure.info figcaption{font-size:.95rem;margin-top:.4rem}
  .muestra{display:inline-block;width:1.1em;height:1.1em;border-radius:4px;border:1px solid #555;vertical-align:-3px;margin-right:.35rem}
  details.acord{border:2px solid var(--borde);border-radius:16px;margin:.8rem 0;padding:0;background:#fff}
  details.acord > summary{padding:.8rem 1rem;min-height:56px;list-style:none;cursor:pointer}
  details.acord > summary::-webkit-details-marker{display:none}
  details.acord > summary::before{content:"▸";font-size:1.4rem;margin-right:.5rem}
  details.acord[open] > summary::before{content:"▾"}
  details.acord > summary h2{display:inline;font-size:1.35rem}
  details.acord > summary:hover{background:var(--cie);border-radius:14px}
  details.acord .cuerpo{padding:0 1rem 1rem}
  main .seccion{scroll-margin-top:120px}
  @media print{#cotejo{break-before:page}.cabecera,.anclas,.herr,.solo-pantalla,video{display:none!important}.carta{break-before:page;border-style:solid}.tarjetas li,.tabla tr{break-inside:avoid}}
"""

JS = """
(function(){
  function abrir(id){ var d=document.getElementById(id); if(d && d.tagName==="DETAILS"){ d.open=true; setTimeout(function(){ d.scrollIntoView({block:"start"}); },30); return true; } return false; }
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener("click",function(ev){
      var id=a.getAttribute("href").slice(1);
      if(a.classList.contains("cerrar")){ var d=a.closest("details"); if(d) d.open=false; return; }
      if(abrir(id)) { ev.preventDefault(); history.replaceState(null,"","#"+id); }
    });
  });
  if(location.hash) abrir(location.hash.slice(1));
  document.querySelectorAll("details.acord").forEach(function(d){
    d.addEventListener("toggle", function(){
      if(!d.open){ var v=d.querySelector("video"); if(v) v.pause(); }
      if(d.open && !window.__imprimiendo) setTimeout(function(){ var c=document.querySelector(".cabecera"); var h=(c && getComputedStyle(c).position==="sticky") ? c.getBoundingClientRect().height : 0; window.scrollTo({top: window.scrollY + d.getBoundingClientRect().top - h - 10, behavior: "instant"}); }, 60);
    });
  });
  window.addEventListener("beforeprint",function(){ window.__imprimiendo=true; document.querySelectorAll("details.acord").forEach(function(d){ d.setAttribute("data-estaba",d.open?"1":""); d.open=true; }); });
  window.addEventListener("afterprint",function(){ setTimeout(function(){ window.__imprimiendo=false; },500); document.querySelectorAll("details.acord").forEach(function(d){ d.open=d.getAttribute("data-estaba")==="1"; }); });
})();
"""

def casillas(n_cols, filas=6):
    fila = "<tr><td>&nbsp;</td>" + "".join('<td><span class="casilla"></span></td>' for _ in range(n_cols)) + "</tr>"
    return "\n".join("    " + fila for _ in range(filas))

# ======================================================================= ESPAÑOL
ES = dict(
 lang="es", otro="obra-bosque-magico-produccion-en.html",
 titulo="El bosque mágico · Producción",
 desc=f"Guía de producción de «El bosque mágico», de {AUTOR}: reparto por grados de prekínder a 6.º, escena por escena, música y hoja de entradas, vestuario, escenografía, plano, ensayos, actividades de clase y carta a las familias.",
 menu=[("index-es.html","Inicio"),("grados-es.html","Por grado"),("materias-es.html","Por materia"),("teatro-es.html","Teatro")],
 inicio="index-es.html", teatro="teatro-es.html", logo_alt="Lumi — página de inicio", saltar="Saltar al contenido", menu_lbl="Menú principal",
 idioma='<div class="idioma" role="group" aria-label="Idioma"><span aria-current="true">Español</span><a href="obra-bosque-magico-produccion-en.html" lang="en" hreflang="en">English</a></div>',
 volver='<a href="obra-bosque-magico-es.html">← El guion</a>',
 autor=f"Obra de {AUTOR}",
 intro="Todo lo que hace falta para montarla con toda la escuela, de prekínder a 6.º grado: quién sale, cuántos, qué se necesita y cuándo.",
 herr='<button type="button" onclick="window.print()">🖨️ Imprimir o guardar en PDF</button><a href="#carta">✉️ Carta a las familias</a><a href="obra-bosque-magico-cartel-es.html">🖼️ Cartel de la función</a>',
 partes="Partes de la guía", arriba="↑ Cerrar y volver arriba",
 pie=f"«El bosque mágico» · Obra de {AUTOR} © 2019 · <a href=\"{WEB}\" target=\"_blank\" rel=\"noopener noreferrer\">www.obrasteatro.com</a> · Publicada en Lumi con autorización del autor · Guía de producción: Lumi (José M. Fernández), CC BY-NC-SA 4.0",
 secciones=[
("autor", "El autor y sus condiciones", f"""
  <div class="autor-caja">
   <p><strong><em>El bosque mágico</em> es una obra de {AUTOR}</strong> (© 2019), autor teatral de Tarragona, España. Sus obras para niños y jóvenes están en <a href="{WEB}" target="_blank" rel="noopener noreferrer">www.obrasteatro.com</a>.</p>
   <p>En octubre de 2026, el autor autorizó a Lumi a publicar el guion interactivo, a traducirlo al inglés y a ampliar el número de habitantes, hadas y duendes para que participe toda la escuela, siempre respetando el texto original.</p>
  </div>
  <p>El autor cede la obra gratis para representarla, con estas condiciones, que se aceptan al usarla:</p>
  <ul>
   <li><strong>Su nombre, Vicente Cañón, debe figurar siempre como autor</strong>: antes de cada función y en todo lo que se publique: carteles, programas, redes sociales, páginas web y videos.</li>
   <li><strong>No se puede cambiar el título</strong> de la obra: <em>El bosque mágico</em>. En inglés se presenta como <em>El bosque mágico (The Magical Forest)</em>.</li>
   <li>El autor agradece mucho que le envíen <strong>fotos, enlaces a videos, recortes de prensa o críticas</strong> de cada montaje, a su correo: <a href="mailto:{CORREO}">{CORREO}</a>. Le gustaría recibir también un cartel donde aparezcan el título, su nombre, la escuela y el país.</li>
  </ul>
  <h3>Lista para cumplir con el autor</h3>
  <ul class="lista-casillas">
   <li><span class="casilla"></span>El cartel y el programa dicen «<em>El bosque mágico</em>, de Vicente Cañón». Use el <a href="obra-bosque-magico-cartel-es.html">cartel de Lumi</a>.</li>
   <li><span class="casilla"></span>Los presentadores dicen el nombre del autor antes de empezar (ver <a href="#trabajos">trabajos para no actores</a>).</li>
   <li><span class="casilla"></span>Cada publicación en redes, en la página de la escuela o en video lleva el título y el nombre del autor.</li>
   <li><span class="casilla"></span>Las familias firmaron el permiso para las fotos (ver la <a href="#carta">carta</a>).</li>
   <li><span class="casilla"></span>Después de la función, se envían al autor fotos, enlaces a los videos y el cartel.</li>
  </ul>"""),
("resumen", "De un vistazo", """
  <ul>
   <li><strong>De qué trata:</strong> cerca de un bosque mágico viven tres pueblos felices: el de la Alegría, el de la Amistad y el de la Generosidad. Las brujas y los brujos, envidiosos, les lanzan un maleficio y les quitan la felicidad. Las personas sabias no saben qué hacer, hasta que unas hadas y unos duendes traen un plan: de noche, mientras las brujas y los brujos duermen, todos bailarán juntos en círculo a su alrededor. El baile rompe el maleficio, y las brujas y los brujos piden ser amigos de todos.</li>
   <li><strong>Valores:</strong> la alegría, la amistad y la generosidad, y sus contrarios: la tristeza, la enemistad y el egoísmo. Que los problemas se resuelven juntos, y que quien se equivoca puede cambiar.</li>
   <li><strong>Duración:</strong> de 20 a 25 minutos, según la música y los bailes. El texto es corto: casi todo es movimiento, baile y música.</li>
   <li><strong>Elenco:</strong> el autor la escribió para unos 25 niños de 5 y 6 años, y dice que todos los grupos pueden crecer. En Lumi la proponemos para toda la escuela, de prekínder a 6.º, con el <a href="#reparto">reparto por grados</a>.</li>
   <li><strong>Idiomas:</strong> el guion está en <a href="obra-bosque-magico-es.html">español</a> y en <a href="obra-bosque-magico-en.html" lang="en">inglés</a>, con las mismas líneas y el mismo orden: se puede representar en un idioma o en el otro.</li>
  </ul>"""),
("imagenes", "La obra en imágenes", """
  <figure class="info"><img src="bm-escena5.jpg" alt="Infografía de la escena 5, «La reunión de las personas sabias». A la izquierda, los tres pueblos grises y tristes; a la derecha, cuatro personas sabias con bata blanca y gafas, en el bosque, se preguntan cómo recuperar la felicidad y se encogen de hombros." loading="lazy" width="1600" height="893"><figcaption>Escena 5: la reunión de las personas sabias.</figcaption></figure>
  <figure class="info"><img src="bm-magia.jpg" alt="Infografía de las escenas 6 y 7, «La llegada de la magia». Las hadas y los duendes llegan con música ante las personas sabias y proponen ir de noche a la cueva y bailar en círculo; las personas sabias se lo explican a los pueblos, que caminan en silencio hacia la cueva." loading="lazy" width="1600" height="893"><figcaption>Escenas 6 y 7: el plan para romper el maleficio.</figcaption></figure>
  <figure class="info"><img src="bm-escena8.jpg" alt="Infografía de la escena 8, «El baile y la reconciliación». Fase 1: hadas, duendes, personas sabias y habitantes bailan en un gran círculo alrededor de las brujas y los brujos dormidos. Fase 2: las brujas y los brujos despiertan sin poderes, piden ser amigos y todos celebran." loading="lazy" width="1600" height="893"><figcaption>Escena 8: el baile y la reconciliación.</figcaption></figure>
  <figure class="info"><img src="bm-escenografia.jpg" alt="Infografía «Escenografía de bajo costo»: matorrales de cartón pintados en varios tonos de verde, con brujas y brujos asomados detrás, y un caldero de cartón negro con llamas y piedras pintadas; los dos llevan un soporte trasero de cartón doblado en triángulo." loading="lazy" width="1600" height="893"><figcaption>Escenografía de bajo costo: los matorrales y el caldero.</figcaption></figure>
  <figure class="info"><img src="bm-atrezo.jpg" alt="Infografía «Guía de escenografía y atrezo»: matorrales del bosque, caldero de conjuros y murales de fondo con árboles y montañas; helados de utilería de goma eva o cartón y un reproductor de música." loading="lazy" width="1600" height="893"><figcaption>Escenografía y utilería.</figcaption></figure>
  <h3>Video: guía de la obra</h3>
  <video class="guia" controls preload="none" poster="bm-guia-portada.jpg" width="1280" height="720"><source src="bm-guia.mp4" type="video/mp4">Su navegador no puede mostrar el video. <a href="bm-guia.mp4">Descargar el video</a>.</video>
  <p style="font-size:.95rem">Video en español, de unos 6 minutos: la obra, el reparto por grados, las escenas y el vestuario.</p>"""),
("reparto", "Reparto por grados y cantidades", """
  <p>El autor pensó la obra para unos 25 niños y escribió que <strong>casi todos los personajes se pueden doblar</strong>: en lugar de cuatro habitantes por pueblo pueden ser cinco, seis o más, y lo mismo con las brujas, los brujos, las hadas y los duendes. Así participa toda la escuela <strong>sin cambiar el texto</strong>.</p>
  <ul>
   <li>Cuando una línea es de un grupo («Brujas», «Hadas y duendes», «Todos los habitantes»), la dice todo el grupo, en coro.</li>
   <li>Cuando una línea tiene número («Habitante 1», «Personas sabias 3 y 4»), la puede decir un niño o un pequeño grupo.</li>
  </ul>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Cantidad de niños por papel</caption>
   <thead><tr><th scope="col">Grado</th><th scope="col">Papel</th><th scope="col">Original</th><th scope="col">Recomendado</th><th scope="col">Máximo</th><th scope="col">Cómo crece</th></tr></thead>
   <tbody>
    <tr><th scope="row" rowspan="3">5.º y 6.º</th><td>Narradora o narrador</td><td>1 a 4</td><td>4</td><td>8</td><td>Una voz por cada dos escenas, o dos voces que se alternan los versos.</td></tr>
    <tr><td>Equipo técnico (ver <a href="#trabajos">trabajos</a>)</td><td>—</td><td>8</td><td>15</td><td>Sonido, luces, telón, matorrales, utilería, apuntador.</td></tr>
    <tr><td>Guías de bambalinas</td><td>—</td><td>1 por cada 3 pequeños</td><td>1 por cada 2</td><td>Llevan a prekínder y kínder a su lugar y entran con ellos.</td></tr>
    <tr><th scope="row" rowspan="3">3.º y 4.º</th><td>Brujas</td><td>3</td><td>6</td><td>12</td><td>Todas dicen sus líneas en coro; se esconden en grupos detrás de los cuatro matorrales.</td></tr>
    <tr><td>Brujos</td><td>3</td><td>6</td><td>12</td><td>Igual que las brujas. Una bruja y un brujo llevan el caldero.</td></tr>
    <tr><td>Personas sabias</td><td>4</td><td>8</td><td>12</td><td>Dos grupos: «1 y 2» y «3 y 4». Puede haber personas sabias de cada pueblo.</td></tr>
    <tr><th scope="row" rowspan="2">1.º y 2.º</th><td>Hadas</td><td>2</td><td>10</td><td>25</td><td>Todas dicen sus líneas en coro y guían el baile final.</td></tr>
    <tr><td>Duendes</td><td>2</td><td>10</td><td>25</td><td>Igual que las hadas: entran por el lado contrario.</td></tr>
    <tr><th scope="row" rowspan="3">Prekínder y kínder</th><td>Pueblo de la Alegría (amarillo)</td><td>4</td><td>10</td><td>30</td><td>Kínder dice las líneas con número; prekínder, las de todo el pueblo («¡Oh! ¡Oh!»), los bailes y los gestos.</td></tr>
    <tr><td>Pueblo de la Amistad (azul)</td><td>4</td><td>10</td><td>30</td><td>Igual: los habitantes 1 a 4 pueden ser cuatro parejas o cuatro grupitos.</td></tr>
    <tr><td>Pueblo de la Generosidad (rojo)</td><td>4</td><td>10</td><td>30</td><td>Igual: todos comparten un helado de utilería.</td></tr>
    <tr><th scope="row">Total</th><td></td><td><strong>≈ 26</strong></td><td><strong>≈ 100</strong></td><td><strong>200 o más</strong></td><td></td></tr>
   </tbody>
  </table>
  </div>
  <div class="nota"><strong>Por qué este reparto:</strong> los más pequeños hacen lo que mejor se les da, que es bailar, moverse y hacer gestos; 1.º y 2.º tienen frases cortas en coro; 3.º y 4.º llevan los papeles con más actuación, las brujas, los brujos y las personas sabias; 5.º y 6.º narran en verso y llevan el escenario. Es una propuesta: cada escuela la adapta a sus grupos.</div>"""),
("escenas", "Escena por escena", """
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Resumen de las escenas</caption>
   <thead><tr><th scope="col">Escena</th><th scope="col">Qué pasa</th><th scope="col">Quién sale</th><th scope="col">Música</th></tr></thead>
   <tbody>
    <tr><th scope="row"><a href="obra-bosque-magico-es.html#escena-1">1</a></th><td>La narradora presenta los tres pueblos, que saludan al público. Las brujas y los brujos, envidiosos, preparan el conjuro en el caldero.</td><td>Narración, los tres pueblos (sentados), brujas y brujos</td><td>Pista 1</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-es.html#escena-2">2</a></th><td>El pueblo de la Alegría baila en el bosque; el maleficio lo pone triste.</td><td>Narración, Alegría, brujas y brujos</td><td>Pistas 2 y 3</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-es.html#escena-3">3</a></th><td>El pueblo de la Amistad juega; el maleficio hace que se peleen y se saquen la lengua.</td><td>Narración, Amistad, brujas y brujos</td><td>Pistas 4 y 3</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-es.html#escena-4">4</a></th><td>El pueblo de la Generosidad comparte helados; el maleficio los vuelve egoístas. Las brujas y los brujos celebran y vuelven a su cueva.</td><td>Narración, Generosidad, brujas y brujos</td><td>Pistas 5, 3 y 1</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-es.html#escena-5">5</a></th><td>Las personas sabias se reúnen en el bosque, pero no encuentran solución.</td><td>Narración, personas sabias</td><td>Pista 6</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-es.html#escena-6">6</a></th><td>Llegan las hadas y los duendes con el plan: bailar de noche alrededor de las brujas y los brujos dormidos.</td><td>Narración, personas sabias, hadas y duendes</td><td>Pista 7</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-es.html#escena-7">7</a></th><td>Las personas sabias explican el plan a los pueblos. De noche, todos suben en silencio a la cueva.</td><td>Narración, personas sabias, los tres pueblos, y después todos</td><td>Pista 8</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-es.html#escena-8">8</a></th><td>A la de tres, todos bailan en círculo y rompen el maleficio. Las brujas y los brujos se quedan sin poderes, piden ser amigos y todos celebran.</td><td>Todo el elenco</td><td>Pistas 9 y 10</td></tr>
   </tbody>
  </table>
  </div>"""),
("trabajos", "Trabajos para no actores", """
  <p>No todos quieren o pueden hablar en escena, y la obra no sale sin estos trabajos. Son papeles de verdad: aparecen en el programa con su nombre.</p>
  <ul class="tarjetas">
   <li><h3>🎤 Presentadores</h3><span class="chip">5.º o 6.º · 1 o 2 niños</span><p>Dan la bienvenida y <strong>anuncian la obra y a su autor</strong>: «Les presentamos <em>El bosque mágico</em>, de Vicente Cañón». El autor pide que su nombre se diga antes de cada función.</p></li>
   <li><h3>🔊 Sonido</h3><span class="chip">4.º a 6.º · 2 niños</span><p>Ponen cada pista en el momento justo, siguiendo la <a href="#entradas">hoja de entradas</a>.</p></li>
   <li><h3>💡 Luces</h3><span class="chip">5.º y 6.º · 1 o 2 niños</span><p>Luz de día para las escenas 1 a 6 y luz de noche, azul, para la cueva.</p></li>
   <li><h3>🌳 Telón y matorrales</h3><span class="chip">5.º y 6.º · 2 a 4 niños</span><p>Abren y cierran el telón y revisan que los cuatro matorrales estén firmes.</p></li>
   <li><h3>🧺 Utilería</h3><span class="chip">4.º a 6.º · 2 niños</span><p>Preparan el caldero y los helados en una mesa, entre bastidores, y los recogen después.</p></li>
   <li><h3>📖 Apuntador</h3><span class="chip">5.º o 6.º · 1 o 2 niños</span><p>Siguen el guion entre bastidores y, si alguien olvida su línea, se la susurran.</p></li>
   <li><h3>🤝 Guías de bambalinas</h3><span class="chip">5.º · 1 por cada 2 o 3 pequeños</span><p>Llevan a prekínder y kínder a su lugar, los acompañan en el baile final y los traen de vuelta.</p></li>
   <li><h3>🎨 Escenografía</h3><span class="chip">Cualquier grado</span><p>Pintan los matorrales, el caldero y el fondo de árboles y montañas.</p></li>
   <li><h3>👒 Vestuario</h3><span class="chip">4.º a 6.º, con un adulto</span><p>Ayudan a vestir a los pequeños: alas, coronas de flores, gorros y sombreros.</p></li>
   <li><h3>📰 Cartel y programa</h3><span class="chip">3.º a 6.º · 2 a 4 niños</span><p>Preparan el <a href="obra-bosque-magico-cartel-es.html">cartel</a> y el programa, con el título, el autor y los nombres de todo el elenco.</p></li>
   <li><h3>🎟️ Recepción</h3><span class="chip">4.º a 6.º · 2 a 4 niños</span><p>Reciben a las familias, reparten programas y ayudan a encontrar asiento.</p></li>
   <li><h3>📸 Fotografía y video</h3><span class="chip">6.º, con un adulto</span><p>Graban solo a los niños cuyas familias dieron permiso. Esas fotos y videos son los que se envían al autor.</p></li>
  </ul>"""),
("musica", "Música y canción final", """
  <p>El autor propone esta lista, que es opcional. Casi todas las piezas son de la <strong>Biblioteca de audio de YouTube</strong>, de uso libre (música infantil y alegre). <strong>El autor ofrece enviarlas en mp3</strong> a quien se lo pida, por correo: ver <a href="#autor">el autor</a>.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Lista de música</caption>
   <thead><tr><th scope="col">Pista</th><th scope="col">Pieza</th><th scope="col">Carácter</th><th scope="col">Cuándo suena</th></tr></thead>
   <tbody>
    <tr><td>1</td><td><em>The New Order</em>, Aaron Kenny</td><td>Cinematográfico, oscuro</td><td>Brujas y brujos (escenas 1 y 4)</td></tr>
    <tr><td>2</td><td><em>Sand Castle</em>, Quincas Moreira</td><td>Infantil, positivo</td><td>Baile del pueblo de la Alegría</td></tr>
    <tr><td>3</td><td><em>St. Francis</em>, Josh Lippi &amp; The Overtimers</td><td>Rock, triste</td><td>Salida triste de cada pueblo</td></tr>
    <tr><td>4</td><td><em>Rainbow Forest</em>, Quincas Moreira</td><td>Infantil, feliz</td><td>Baile del pueblo de la Amistad</td></tr>
    <tr><td>5</td><td><em>Goat</em>, Wayne Jones</td><td>Infantil, feliz</td><td>Baile de los helados, pueblo de la Generosidad</td></tr>
    <tr><td>6</td><td><em>Sleeping Sheep</em>, The Green Orbs</td><td>Infantil, serena</td><td>Las personas sabias, preocupadas</td></tr>
    <tr><td>7</td><td>Robert Schumann, <em>Escenas infantiles</em>, op. 15, n.º 1, «De países y gentes lejanos»</td><td>Piano</td><td>Entrada y salida de las hadas y los duendes</td></tr>
    <tr><td>8</td><td>Johannes Brahms, <em>Canción de cuna</em></td><td>Nana</td><td>La noche: las brujas y los brujos se duermen</td></tr>
    <tr><td>9</td><td><em>Twirly Tops</em>, The Green Orbs</td><td>Infantil, feliz</td><td>El gran baile en círculo</td></tr>
    <tr><td>10</td><td><em>Dancing on Green Grass</em>, The Green Orbs</td><td>Infantil, positiva</td><td>Final y reverencia</td></tr>
   </tbody>
  </table>
  </div>
  <div class="nota"><strong>Pistas 7 y 8:</strong> Schumann y Brahms son de dominio público, pero no todas las grabaciones lo son. El autor sugiere la versión de Vladimir Horowitz; para publicar videos de la función, conviene usar grabaciones libres, como las de <a href="https://musopen.org/" target="_blank" rel="noopener noreferrer">Musopen</a>, o pedirle las pistas al autor.</div>
  <h3>Canción final: «A bailar en el bosque»</h3>
  <p>Una canción de Lumi para cerrar la obra, compuesta a partir de sus ideas: la alegría, la amistad, la generosidad, el helado compartido y el hechizo roto. <strong>No forma parte del texto del autor</strong>; Vicente Cañón la conoce y le pareció «una genial idea para darle un colofón final a la obra». Va después de la última narración, con todo el elenco en corro. Cada verso se canta dos veces, para que los más pequeños lo repitan.</p>
  <video class="guia" controls preload="none" poster="bm-cancion-portada.jpg" width="1024" height="1024" style="max-width:520px"><source src="bm-cancion.mp4" type="video/mp4"><track kind="captions" src="bm-cancion-es.vtt" srclang="es" label="Español" default>Su navegador no puede mostrar el video. <a href="bm-cancion.mp4">Descargar la canción</a>.</video>
  <details style="margin:.6rem 0"><summary><strong>Letra</strong></summary><p style="font-size:1.1rem;line-height:1.7">En el bosque de la magia,<br>todos juntos a bailar.<br>La tristeza se marchó,<br>¡la alegría ya llegó!<br><br>Compartimos el helado,<br>damos saltos de ilusión;<br>si jugamos como amigos,<br>se ilumina el corazón.<br><br>En el bosque de la magia,<br>hadas, duendes y los sabios<br>el hechizo rompen ya;<br>brujas y brujos sonrientes<br>¡cantan con nosotros hoy!<br><br>¿Quién comparte su bondad?<br>¡Generosidad!<br>¿Quién nos une de verdad?<br>¡La amistad!<br>¿Y qué canta el bosque entero?<br>¡Felicidad!<br>¡Uno, dos y tres: a sonreír!</p></details>"""),
("entradas", "Hoja de entradas (sonido y luces)", """
  <p>Para el equipo técnico. Cada «entrada» es un cambio: se hace cuando ocurre lo que dice la columna «Señal». Las luces son una sugerencia de Lumi; la obra se puede hacer con la luz del salón.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Entradas de sonido y luces</caption>
   <thead><tr><th scope="col">N.º</th><th scope="col">Escena</th><th scope="col">Señal</th><th scope="col">Sonido</th><th scope="col">Luces</th></tr></thead>
   <tbody>
    <tr><td>1</td><td>1</td><td>Se abre el telón</td><td>Silencio</td><td>Luz de día, cálida</td></tr>
    <tr><td>2</td><td>1</td><td>Las brujas y los brujos van al frente del escenario</td><td>Pista 1; baja cuando hablan</td><td>—</td></tr>
    <tr><td>3</td><td>1</td><td>«Ja, ja, ja...», después de «¡Sí!»</td><td>Pista 1 mientras traen el caldero</td><td>—</td></tr>
    <tr><td>4</td><td>1</td><td>«Vamos a esparcirlo… ¡ya!»</td><td>Pista 1 mientras sacan el caldero y hacen el trenecito</td><td>—</td></tr>
    <tr><td>5</td><td>2</td><td>Termina la narración</td><td>Pista 2: baile de la Alegría; se apaga cuando terminan</td><td>—</td></tr>
    <tr><td>6</td><td>2</td><td>«¡Oh! ¡Oh!»</td><td>Pista 3: salida triste</td><td>—</td></tr>
    <tr><td>7</td><td>3</td><td>Las brujas y los brujos se esconden</td><td>Pista 4: baile de la Amistad</td><td>—</td></tr>
    <tr><td>8</td><td>3</td><td>Los habitantes 3 y 4 sacan la lengua</td><td>Pista 3: salida triste</td><td>—</td></tr>
    <tr><td>9</td><td>4</td><td>Las brujas y los brujos se esconden por última vez</td><td>Pista 5: baile de los helados</td><td>—</td></tr>
    <tr><td>10</td><td>4</td><td>Todos los habitantes sacan la lengua</td><td>Pista 3: salida triste</td><td>—</td></tr>
    <tr><td>11</td><td>4</td><td>«¡Hemos acabado con la felicidad!» · «¡Ja, ja, ja!»</td><td>Pista 1: salen por la derecha</td><td>—</td></tr>
    <tr><td>12</td><td>5</td><td>Termina la narración</td><td>Pista 6: las personas sabias caminan preocupadas</td><td>—</td></tr>
    <tr><td>13</td><td>6</td><td>Termina la narración («…impacientes»)</td><td>Pista 7: entran las hadas y los duendes</td><td>—</td></tr>
    <tr><td>14</td><td>6</td><td>«¡Así lo haremos!»</td><td>Pista 7: salen las hadas y los duendes</td><td>—</td></tr>
    <tr><td>15</td><td>7</td><td>La narración dice «Aquella noche…»</td><td>Silencio</td><td>Baja a luz de noche, azul suave</td></tr>
    <tr><td>16</td><td>7</td><td>Termina la narración</td><td>Pista 8: la nana, mientras todos entran de puntillas</td><td>Noche</td></tr>
    <tr><td>17</td><td>8</td><td>«A la una, a las dos y a las… ¡tres!»</td><td>Pista 9: el gran baile en círculo</td><td>Noche, con luz en el centro</td></tr>
    <tr><td>18</td><td>8</td><td>«¡Claro que sí!»</td><td>—</td><td>Vuelve la luz de día</td></tr>
    <tr><td>19</td><td>8</td><td>«…esta obra de teatro se ha acabado»</td><td>Pista 10: baile final y reverencia</td><td>Luz general</td></tr>
    <tr><td>20</td><td>Final</td><td>Termina la reverencia; todos en corro</td><td>Canción «A bailar en el bosque»: todos cantan y bailan</td><td>Luz general; al final, se cierra el telón</td></tr>
   </tbody>
  </table>
  </div>"""),
("vestuario", "Vestuario", """
  <p>El vestuario es el que propone el autor. Casi todo se arma con ropa de casa; lo demás se hace en clase.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Vestuario por papel</caption>
   <thead><tr><th scope="col">Papel</th><th scope="col">Ropa de casa</th><th scope="col">Lo hace la escuela</th></tr></thead>
   <tbody>
    <tr><td><span class="muestra" style="background:#F2C200" aria-hidden="true"></span>Pueblo de la Alegría</td><td>Pantalón de mezclilla y camiseta amarilla.</td><td>—</td></tr>
    <tr><td><span class="muestra" style="background:#2F6FC0" aria-hidden="true"></span>Pueblo de la Amistad</td><td>Pantalón de mezclilla y camiseta azul.</td><td>—</td></tr>
    <tr><td><span class="muestra" style="background:#C8302B" aria-hidden="true"></span>Pueblo de la Generosidad</td><td>Pantalón de mezclilla y camiseta roja.</td><td>Helados de utilería.</td></tr>
    <tr><td>Hadas</td><td>Medias de color y camiseta.</td><td>Falda de tul, alas y corona de flores.</td></tr>
    <tr><td>Duendes</td><td>Camiseta y medias o pantalón verdes.</td><td>Gorro verde; orejas de duende, si se quiere.</td></tr>
    <tr><td>Brujas</td><td>Vestido o ropa negra.</td><td>Sombrero negro puntiagudo de cartulina.</td></tr>
    <tr><td>Brujos</td><td>Ropa oscura.</td><td>Capa negra y sombrero negro.</td></tr>
    <tr><td>Personas sabias</td><td>Ropa clara.</td><td>Bata blanca (una camisa grande de adulto sirve) y gafas redondas sin cristales.</td></tr>
    <tr><td>Narradores</td><td>Ropa escolar arreglada.</td><td>—</td></tr>
    <tr><td>Equipo técnico</td><td>Ropa negra u oscura, para no llamar la atención.</td><td>—</td></tr>
   </tbody>
  </table>
  </div>
  <div class="nota"><strong>Por qué estos colores:</strong> el autor pide un color distinto para cada pueblo. Como los duendes van de verde, el pueblo de la Generosidad va de rojo, para que en el baile final se distingan todos los grupos.</div>"""),
("cotejo", "Lista de cotejo de vestuario y utilería", f"""
  <p>Para el docente de cada grupo: marque cada casilla cuando el niño tenga todo listo. Se imprime una por salón.</p>
  <p>Salón: <span class="hueco">&nbsp;</span> Docente: <span class="hueco">&nbsp;</span> Papel del grupo: <span class="hueco">&nbsp;</span></p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Lista de cotejo por niño</caption>
   <thead><tr><th scope="col">Nombre</th><th scope="col">Ropa de casa</th><th scope="col">Pieza hecha en clase (alas, gorro, sombrero…)</th><th scope="col">Marcado con su nombre</th><th scope="col">Listo para el ensayo general</th></tr></thead>
   <tbody>
{casillas(4)}
   </tbody>
  </table>
  </div>
  <h3>Utilería</h3>
  <ul class="lista-casillas">
   <li><span class="casilla"></span>Cuatro matorrales de cartón, firmes y con su soporte</li>
   <li><span class="casilla"></span>Caldero u olla grande de cartón</li>
   <li><span class="casilla"></span>Helados de utilería para el pueblo de la Generosidad</li>
   <li><span class="casilla"></span>Fondo pintado con árboles y montañas</li>
   <li><span class="casilla"></span>Las diez pistas ordenadas y probadas en el equipo de sonido</li>
   <li><span class="casilla"></span>Cinta de colores en el suelo: amarilla, azul y roja para los pueblos</li>
  </ul>"""),
("escenografia", "Escenografía y utilería", """
  <ul>
   <li><strong>Fondo:</strong> montañas y árboles pintados en papel o cartón, separados del telón.</li>
   <li><strong>Cuatro matorrales</strong> de cartón recortado, pintados en varios tonos de verde, con un soporte trasero de cartón doblado en triángulo para que se sostengan solos. Detrás se esconden las brujas y los brujos, así que deben ser altos y anchos.</li>
   <li><strong>Caldero u olla grande</strong> de cartón pintado de negro, con fuego y piedras pintadas en la base, también con soporte trasero. Una bruja y un brujo lo entran y lo sacan.</li>
   <li><strong>Helados de utilería</strong> de goma eva, cartón o plástico, para el pueblo de la Generosidad.</li>
   <li><strong>La cueva</strong> (escenas 7 y 8): no hace falta decorado. Basta con la luz de noche y con que las brujas y los brujos se acuesten en el centro.</li>
  </ul>
  <p>Al final de su obra, el autor incluye fotos de los matorrales y del caldero que se hicieron en el montaje original, todos de cartón. Las infografías de <a href="#imagenes">la obra en imágenes</a> muestran cómo hacerlos.</p>"""),
("plano", "Plano del escenario", """
  <p>Visto desde el público. «Fondo» es lo más lejano al público; «Frente», lo más cercano. Los tres pueblos se sientan en el suelo, delante del escenario y de cara al público, y suben al escenario cuando les toca.</p>
  <h3>Escenas 1 a 4</h3>
  <div class="plano" role="img" aria-label="Escenas 1 a 4: al fondo, cuatro matorrales con las brujas y los brujos escondidos detrás; al frente en el centro, la narración y, más tarde, el pueblo que baila; delante del escenario, los tres pueblos sentados de cara al público: Alegría a la izquierda, Amistad al centro, Generosidad a la derecha.">
   <div><b>Fondo izquierda</b>Matorrales 1 y 2 · brujas y brujos</div><div><b>Fondo centro</b>Fondo de árboles y montañas</div><div><b>Fondo derecha</b>Matorrales 3 y 4 · brujas y brujos</div>
   <div><b>Frente izquierda</b>Narración</div><div><b>Frente centro</b>Caldero (escena 1) · el pueblo que baila (escenas 2 a 4)</div><div><b>Frente derecha</b>Salida de las brujas y los brujos (escena 4)</div>
  </div>
  <div class="plano" role="img" aria-label="Delante del escenario: los tres pueblos sentados.">
   <div><b>Delante, izquierda</b>Pueblo de la Alegría (amarillo)</div><div><b>Delante, centro</b>Pueblo de la Amistad (azul)</div><div><b>Delante, derecha</b>Pueblo de la Generosidad (rojo)</div>
  </div><p class="publico">Público</p>
  <h3>Escenas 5 y 6</h3>
  <div class="plano" role="img" aria-label="Escenas 5 y 6: las personas sabias en el centro; las hadas entran por la izquierda y los duendes por la derecha.">
   <div><b>Fondo izquierda</b>Matorrales</div><div><b>Fondo centro</b>—</div><div><b>Fondo derecha</b>Matorrales</div>
   <div><b>Frente izquierda</b>Hadas</div><div><b>Frente centro</b>Personas sabias</div><div><b>Frente derecha</b>Duendes</div>
  </div><p class="publico">Público</p>
  <h3>Escenas 7 y 8</h3>
  <div class="plano" role="img" aria-label="Escenas 7 y 8: las brujas y los brujos duermen en el centro; alrededor, un gran corro con hadas, duendes, personas sabias y los tres pueblos. Después del baile, el corro se abre en un semicírculo.">
   <div><b>Fondo izquierda</b>Corro</div><div><b>Fondo centro</b>Corro</div><div><b>Fondo derecha</b>Corro</div>
   <div><b>Frente izquierda</b>Corro</div><div><b>Frente centro</b>Brujas y brujos, dormidos</div><div><b>Frente derecha</b>Corro</div>
  </div><p class="publico">Público</p>
  <div class="nota">Después del baile, el corro <strong>se abre en un semicírculo hacia los lados</strong>, para que el público vea a las brujas y los brujos cuando despiertan. Si el escenario es pequeño, el corro puede ser doble: los pequeños por dentro, con sus guías, y los mayores por fuera.</div>"""),
("ensayos", "Ensayos", """
  <h3>Semanas 1 a 3: cada grupo en su salón</h3>
  <ul>
   <li><strong>Prekínder y kínder:</strong> sesiones de 15 minutos. Saludar al público cuando la narración nombra a su pueblo, el baile de su pueblo y los gestos del maleficio: cara triste, sacar la lengua, no querer compartir.</li>
   <li><strong>1.º y 2.º:</strong> la entrada con música, las frases en coro («Hemos venido a ayudaros», «A la de tres, empezaremos a bailar») y el baile en corro.</li>
   <li><strong>3.º y 4.º:</strong> las brujas y los brujos, la mímica del caldero, el conjuro y el «trenecito»; las personas sabias, la caminata preocupada y su diálogo.</li>
   <li><strong>5.º y 6.º:</strong> los versos de la narración, con calma y voz clara, y el equipo técnico con la hoja de entradas.</li>
   <li><strong>Todos:</strong> la canción final, «A bailar en el bosque», en corro.</li>
  </ul>
  <h3>Semanas 4 y 5: por bloques</h3>
  <ul>
   <li><strong>Bloque A, el maleficio (escenas 1 a 4):</strong> brujas y brujos con un pueblo cada vez.</li>
   <li><strong>Bloque B, la solución (escenas 5 y 6):</strong> personas sabias con hadas y duendes.</li>
   <li><strong>Bloque C, la noche y el baile (escenas 7 y 8):</strong> todos los grupos, con los guías de bambalinas.</li>
   <li><strong>Narración:</strong> se une a cada bloque para ajustar los tiempos con la música.</li>
  </ul>
  <h3>Última semana: ensayos generales</h3>
  <ol>
   <li>Marcar con cinta de colores en el suelo dónde se sienta cada pueblo; entradas y salidas con música.</li>
   <li>Obra completa con vestuario, matorrales, caldero y helados, y la reverencia final.</li>
  </ol>
  <div class="nota">Nadie tiene que memorizar si no puede. Los narradores pueden leer en escena, con el guion en una carpeta negra. Los pequeños dicen sus frases en coro, y un guía puede decírselas en voz baja justo antes. En el <a href="obra-bosque-magico-es.html">guion</a>, cada niño puede elegir su papel, ver solo sus líneas y escucharlas en voz alta.</div>"""),
("clase", "En clase", """
  <p>El autor recomienda que, <strong>antes de empezar los ensayos</strong>, se trabajen en clase los valores de la obra y sus contrarios: alegría y tristeza, amistad y enemistad, generosidad y egoísmo.</p>
  <ul class="tarjetas">
   <li><h3>Prekínder y kínder</h3><p><strong>Caras y gestos.</strong> Mostrar con la cara y el cuerpo «alegre» y «triste», «amigos» y «enfadados», «compartir» y «no compartir». Es justo lo que harán en escena.</p><p>Repartir algo entre todos, como unos helados de papel, y hablar de cómo se siente compartir.</p></li>
   <li><h3>1.º y 2.º</h3><p><strong>¿Cómo ayudamos?</strong> Las hadas y los duendes no pelean: proponen un plan. ¿Qué podemos hacer cuando un compañero está triste o enfadado?</p><p>Ensayar el corro y contar «a la una, a las dos y a las tres» todos a la vez.</p></li>
   <li><h3>3.º y 4.º</h3><p><strong>Envidia y segunda oportunidad.</strong> ¿Por qué las brujas y los brujos sienten envidia? Al final piden ser amigos y los aceptan: ¿por qué es importante perdonar?</p><p>Las personas sabias no encuentran la respuesta solas: ¿cuándo es bueno pedir ayuda?</p></li>
   <li><h3>5.º y 6.º</h3><p><strong>Verso y rima.</strong> Buscar las rimas de la narración («alegría» y «día», «amistad» y «solidaridad») y leerlas marcando el ritmo.</p><p>Comparar el español con <a href="obra-bosque-magico-en.html" lang="en">la traducción al inglés</a>: ¿cómo se tradujo «colorín, colorado»?</p></li>
  </ul>"""),
("carta", "Carta a las familias", f"""
  <p class="solo-pantalla">Lista para imprimir. Complete los espacios a mano. Al final hay un talón para devolver firmado.</p>
  <div class="carta">
   <p><strong>Obra de teatro de la escuela: <em>El bosque mágico</em>, de Vicente Cañón</strong></p>
   <p>Fecha: <span class="hueco">&nbsp;</span></p>
   <p>Estimada familia:</p>
   <p>Este año, toda la escuela, de prekínder a 6.º grado, presentará <em>El bosque mágico</em>, una obra de teatro infantil de Vicente Cañón. Cuenta la historia de tres pueblos, el de la Alegría, el de la Amistad y el de la Generosidad, que pierden su felicidad por un maleficio y la recuperan bailando todos juntos. Mientras ensayan, los niños hablarán en clase de la alegría, la amistad y la generosidad.</p>
   <p><strong>Su hijo o hija</strong> <span class="hueco">&nbsp;</span> <strong>será:</strong> <span class="hueco">&nbsp;</span></p>
   <p><strong>Ropa que le pedimos, si la tiene en casa</strong> (no hace falta comprar nada):</p>
   <p><span class="hueco" style="min-width:100%">&nbsp;</span></p>
   <p>La escuela hará en clase las alas, las coronas de flores, los gorros, los sombreros y las capas. Si no tiene alguna prenda, avísenos: tendremos ropa de préstamo.</p>
   <p><strong>Fechas importantes</strong></p>
   <ul>
    <li>Entregar la ropa, en una bolsa con el nombre y el grado: <span class="hueco">&nbsp;</span></li>
    <li>Ensayo general: <span class="hueco">&nbsp;</span></li>
    <li>Función: día <span class="hueco">&nbsp;</span>, hora <span class="hueco">&nbsp;</span>, lugar <span class="hueco">&nbsp;</span></li>
   </ul>
   <p><strong>Cómo puede ayudar en casa:</strong> si su hijo o hija tiene líneas, ensáyenlas juntos. El guion está en Lumi (www.lumi-educa.com), en español y en inglés, con un botón para escuchar cada línea y otro para ver solo las de su personaje.</p>
   <p><strong>Sobre las fotos y los videos:</strong> el autor de la obra pide que le enviemos fotos y videos de las funciones. Solo enviaremos imágenes de los niños cuyas familias lo autoricen en el talón.</p>
   <p>¡Gracias por acompañarnos!</p>
   <p>Atentamente,<br><span class="hueco">&nbsp;</span></p>
   <div class="talon">
    <p><strong>Devuelva este talón firmado antes del</strong> <span class="hueco">&nbsp;</span></p>
    <p>Nombre del niño o la niña: <span class="hueco">&nbsp;</span> Grado: <span class="hueco">&nbsp;</span></p>
    <p><span class="casilla"></span>Doy permiso para que mi hijo o hija participe en la obra.</p>
    <p><span class="casilla"></span>Doy permiso para que la escuela publique fotos o videos de la obra en los que aparezca mi hijo o hija, y para que se los envíe al autor de la obra.</p>
    <p><span class="casilla"></span><strong>No</strong> doy permiso para publicar ni enviar fotos o videos en los que aparezca mi hijo o hija.</p>
    <p><span class="casilla"></span>Puedo ayudar con: <span class="casilla" style="margin-left:.4rem"></span>vestuario <span class="casilla" style="margin-left:.4rem"></span>escenografía <span class="casilla" style="margin-left:.4rem"></span>el día de la función</p>
    <p>Firma: <span class="hueco" style="min-width:14em">&nbsp;</span> Teléfono: <span class="hueco">&nbsp;</span></p>
   </div>
  </div>"""),
 ],
)
ES_NAV = [("autor","El autor"),("resumen","De un vistazo"),("imagenes","Imágenes y video"),("reparto","Reparto por grados"),("escenas","Escena por escena"),("trabajos","Trabajos para no actores"),("musica","Música y canción"),("entradas","Hoja de entradas"),("vestuario","Vestuario"),("cotejo","Lista de cotejo"),("escenografia","Escenografía"),("plano","Plano del escenario"),("ensayos","Ensayos"),("clase","En clase"),("carta","Carta a las familias")]

# ======================================================================= ENGLISH
EN = dict(
 lang="en", otro="obra-bosque-magico-produccion-es.html",
 titulo="El bosque mágico (The Magical Forest) · Production",
 desc=f"Production guide for “El bosque mágico” (The Magical Forest), a play by {AUTOR}: cast by grade from Pre-K to 6th, scene by scene, music and cue sheet, costumes, sets, stage plan, rehearsals, classroom activities and family letter.",
 menu=[("index.html","Home"),("grados.html","By grade"),("materias.html","By subject"),("teatro.html","Theater")],
 inicio="index.html", teatro="teatro.html", logo_alt="Lumi — home page", saltar="Skip to content", menu_lbl="Main menu",
 idioma='<div class="idioma" role="group" aria-label="Language"><a href="obra-bosque-magico-produccion-es.html" lang="es" hreflang="es">Español</a><span aria-current="true">English</span></div>',
 volver='<a href="obra-bosque-magico-en.html">← The script</a>',
 autor=f"A play by {AUTOR}",
 intro="Everything you need to stage it with the whole school, from Pre-K to 6th grade: who is in it, how many, what you need and when.",
 herr='<button type="button" onclick="window.print()">🖨️ Print or save as PDF</button><a href="#carta">✉️ Family letter</a><a href="obra-bosque-magico-cartel-en.html">🖼️ Show poster</a>',
 partes="Parts of the guide", arriba="↑ Close and back to top",
 pie=f"“El bosque mágico” (The Magical Forest) · A play by {AUTOR} © 2019 · <a href=\"{WEB}\" target=\"_blank\" rel=\"noopener noreferrer\">www.obrasteatro.com</a> · Published on Lumi with the author's permission · Production guide: Lumi (José M. Fernández), CC BY-NC-SA 4.0",
 secciones=[
("autor", "The author and his conditions", f"""
  <div class="autor-caja">
   <p><strong><em lang="es">El bosque mágico</em> is a play by {AUTOR}</strong> (© 2019), a playwright from Tarragona, Spain. His plays for children and young people are at <a href="{WEB}" target="_blank" rel="noopener noreferrer">www.obrasteatro.com</a>.</p>
   <p>In October 2026, the author gave Lumi permission to publish the interactive script, to translate it into English, and to add more villagers, fairies and elves so the whole school can take part, always keeping the original text.</p>
  </div>
  <p>The author offers the play free of charge for performance, on these conditions, which are accepted by using it:</p>
  <ul>
   <li><strong>His name, Vicente Cañón, must always appear as the author</strong>: before every performance and in everything that is published: posters, programs, social media, websites and videos.</li>
   <li><strong>The title of the play must not be changed</strong>: <em lang="es">El bosque mágico</em>. In English, it is presented as <em><span lang="es">El bosque mágico</span> (The Magical Forest)</em>.</li>
   <li>The author would be very grateful to receive <strong>photos, links to videos, press clippings or reviews</strong> of each production, at his email: <a href="mailto:{CORREO}">{CORREO}</a>. He would also like to receive a poster showing the title, his name, the school and the country.</li>
  </ul>
  <h3>Checklist for the author's conditions</h3>
  <ul class="lista-casillas">
   <li><span class="casilla"></span>The poster and the program say “<em lang="es">El bosque mágico</em> (The Magical Forest), by Vicente Cañón”. Use the <a href="obra-bosque-magico-cartel-en.html">Lumi poster</a>.</li>
   <li><span class="casilla"></span>The presenters say the author's name before the show begins (see <a href="#trabajos">jobs for non-actors</a>).</li>
   <li><span class="casilla"></span>Every post on social media, on the school website or in a video includes the title and the author's name.</li>
   <li><span class="casilla"></span>Families have signed the photo permission (see the <a href="#carta">letter</a>).</li>
   <li><span class="casilla"></span>After the show, photos, video links and the poster are sent to the author.</li>
  </ul>"""),
("resumen", "At a glance", """
  <ul>
   <li><strong>What it's about:</strong> near a magical forest there are three happy villages: the Village of Joy, the Village of Friendship and the Village of Generosity. The envious witches and wizards cast a curse on them and take away their happiness. The wise people don't know what to do, until some fairies and elves bring a plan: at night, while the witches and wizards are asleep, everyone will dance together in a circle around them. The dance breaks the curse, and the witches and wizards ask to be everyone's friends.</li>
   <li><strong>Values:</strong> joy, friendship and generosity, and their opposites: sadness, unfriendliness and selfishness. Problems are solved together, and someone who makes a mistake can change.</li>
   <li><strong>Running time:</strong> 20 to 25 minutes, depending on the music and the dances. The text is short: most of the play is movement, dancing and music.</li>
   <li><strong>Cast:</strong> the author wrote it for about 25 children aged 5 and 6, and says every group can grow. On Lumi we suggest it for the whole school, Pre-K to 6th grade, with the <a href="#reparto">cast by grade</a>.</li>
   <li><strong>Languages:</strong> the script is in <a href="obra-bosque-magico-es.html" lang="es">Spanish</a> and in <a href="obra-bosque-magico-en.html">English</a>, with the same lines in the same order, so it can be performed in either language.</li>
  </ul>"""),
("imagenes", "The play in pictures", """
  <p>These infographics are in Spanish.</p>
  <figure class="info"><img src="bm-escena5.jpg" alt="Infographic for scene 5, the meeting of the wise people. On the left, the three villages, gray and sad; on the right, four wise people in white coats and glasses, in the forest, wondering how to bring happiness back and shrugging their shoulders." loading="lazy" width="1600" height="893"><figcaption>Scene 5: the wise people meet.</figcaption></figure>
  <figure class="info"><img src="bm-magia.jpg" alt="Infographic for scenes 6 and 7, the arrival of magic. The fairies and elves arrive with music before the wise people and suggest going to the cave at night to dance in a circle; the wise people explain the plan to the villages, who walk quietly to the cave." loading="lazy" width="1600" height="893"><figcaption>Scenes 6 and 7: the plan to break the curse.</figcaption></figure>
  <figure class="info"><img src="bm-escena8.jpg" alt="Infographic for scene 8, the dance and the reconciliation. Phase 1: fairies, elves, wise people and villagers dance in a big circle around the sleeping witches and wizards. Phase 2: the witches and wizards wake up without their powers, ask to be friends and everyone celebrates." loading="lazy" width="1600" height="893"><figcaption>Scene 8: the dance and making friends.</figcaption></figure>
  <figure class="info"><img src="bm-escenografia.jpg" alt="Infographic on low-cost sets: cardboard bushes painted in several shades of green, with witches and wizards peeking out from behind, and a black cardboard cauldron with painted flames and stones; both have a cardboard back support folded into a triangle." loading="lazy" width="1600" height="893"><figcaption>Low-cost sets: the bushes and the cauldron.</figcaption></figure>
  <figure class="info"><img src="bm-atrezo.jpg" alt="Infographic on sets and props: forest bushes, a spell cauldron and backdrop murals with trees and mountains; prop ice creams made of foam sheets or cardboard, and a music player." loading="lazy" width="1600" height="893"><figcaption>Sets and props.</figcaption></figure>
  <h3>Video: a guide to the play</h3>
  <video class="guia" controls preload="none" poster="bm-guia-portada.jpg" width="1280" height="720" lang="es"><source src="bm-guia.mp4" type="video/mp4">Your browser cannot play this video. <a href="bm-guia.mp4">Download the video</a>.</video>
  <p style="font-size:.95rem">A video in Spanish, about 6 minutes long: the play, the cast by grade, the scenes and the costumes.</p>"""),
("reparto", "Cast by grade and numbers", """
  <p>The author wrote the play for about 25 children and noted that <strong>almost every part can be doubled</strong>: instead of four villagers per village there can be five, six or more, and the same goes for the witches, wizards, fairies and elves. That way the whole school takes part <strong>without changing the text</strong>.</p>
  <ul>
   <li>When a line belongs to a group (“Witches”, “Fairies and Elves”, “All the villagers”), the whole group says it together.</li>
   <li>When a line has a number (“Villager 1”, “Wise People 3 and 4”), it can be said by one child or by a small group.</li>
  </ul>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Number of children per part</caption>
   <thead><tr><th scope="col">Grade</th><th scope="col">Part</th><th scope="col">Original</th><th scope="col">Suggested</th><th scope="col">Maximum</th><th scope="col">How it grows</th></tr></thead>
   <tbody>
    <tr><th scope="row" rowspan="3">5th &amp; 6th</th><td>Narrator</td><td>1 to 4</td><td>4</td><td>8</td><td>One voice for every two scenes, or two voices taking turns with the verses.</td></tr>
    <tr><td>Tech crew (see <a href="#trabajos">jobs</a>)</td><td>—</td><td>8</td><td>15</td><td>Sound, lights, curtain, bushes, props, prompter.</td></tr>
    <tr><td>Backstage buddies</td><td>—</td><td>1 for every 3 little ones</td><td>1 for every 2</td><td>They take Pre-K and K children to their places and go on stage with them.</td></tr>
    <tr><th scope="row" rowspan="3">3rd &amp; 4th</th><td>Witches</td><td>3</td><td>6</td><td>12</td><td>They all say their lines together and hide in groups behind the four bushes.</td></tr>
    <tr><td>Wizards</td><td>3</td><td>6</td><td>12</td><td>Same as the witches. One witch and one wizard carry the cauldron.</td></tr>
    <tr><td>Wise People</td><td>4</td><td>8</td><td>12</td><td>Two groups: “1 and 2” and “3 and 4”. There can be wise people from each village.</td></tr>
    <tr><th scope="row" rowspan="2">1st &amp; 2nd</th><td>Fairies</td><td>2</td><td>10</td><td>25</td><td>They all say their lines together and lead the final dance.</td></tr>
    <tr><td>Elves</td><td>2</td><td>10</td><td>25</td><td>Same as the fairies; they come in from the opposite side.</td></tr>
    <tr><th scope="row" rowspan="3">Pre-K &amp; K</th><td>Village of Joy (yellow)</td><td>4</td><td>10</td><td>30</td><td>Kindergarten says the numbered lines; Pre-K says the whole-village lines (“Oh! Oh!”), and does the dances and gestures.</td></tr>
    <tr><td>Village of Friendship (blue)</td><td>4</td><td>10</td><td>30</td><td>Same: villagers 1 to 4 can be four pairs or four small groups.</td></tr>
    <tr><td>Village of Generosity (red)</td><td>4</td><td>10</td><td>30</td><td>Same: they all share a prop ice cream.</td></tr>
    <tr><th scope="row">Total</th><td></td><td><strong>≈ 26</strong></td><td><strong>≈ 100</strong></td><td><strong>200 or more</strong></td><td></td></tr>
   </tbody>
  </table>
  </div>
  <div class="nota"><strong>Why this casting:</strong> the youngest children do what they do best, which is dancing, moving and making faces; 1st and 2nd graders have short lines said together; 3rd and 4th graders play the parts with the most acting, the witches, wizards and wise people; 5th and 6th graders narrate in verse and run the stage. It is a suggestion: each school can adapt it to its own groups.</div>"""),
("escenas", "Scene by scene", """
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Summary of the scenes</caption>
   <thead><tr><th scope="col">Scene</th><th scope="col">What happens</th><th scope="col">Who is on stage</th><th scope="col">Music</th></tr></thead>
   <tbody>
    <tr><th scope="row"><a href="obra-bosque-magico-en.html#escena-1">1</a></th><td>The narrator introduces the three villages, who wave to the audience. The envious witches and wizards brew the spell in the cauldron.</td><td>Narrator, the three villages (seated), witches and wizards</td><td>Track 1</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-en.html#escena-2">2</a></th><td>The Village of Joy dances in the forest; the curse makes them sad.</td><td>Narrator, Joy, witches and wizards</td><td>Tracks 2 and 3</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-en.html#escena-3">3</a></th><td>The Village of Friendship plays; the curse makes them quarrel and stick their tongues out.</td><td>Narrator, Friendship, witches and wizards</td><td>Tracks 4 and 3</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-en.html#escena-4">4</a></th><td>The Village of Generosity shares ice cream; the curse makes them selfish. The witches and wizards celebrate and go back to their cave.</td><td>Narrator, Generosity, witches and wizards</td><td>Tracks 5, 3 and 1</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-en.html#escena-5">5</a></th><td>The wise people meet in the forest, but they cannot find a solution.</td><td>Narrator, wise people</td><td>Track 6</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-en.html#escena-6">6</a></th><td>The fairies and elves arrive with the plan: to dance at night around the sleeping witches and wizards.</td><td>Narrator, wise people, fairies and elves</td><td>Track 7</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-en.html#escena-7">7</a></th><td>The wise people explain the plan to the villages. At night, everyone climbs quietly up to the cave.</td><td>Narrator, wise people, the three villages, and then everyone</td><td>Track 8</td></tr>
    <tr><th scope="row"><a href="obra-bosque-magico-en.html#escena-8">8</a></th><td>On the count of three, everyone dances in a circle and breaks the curse. The witches and wizards lose their powers, ask to be friends, and everyone celebrates.</td><td>The whole cast</td><td>Tracks 9 and 10</td></tr>
   </tbody>
  </table>
  </div>"""),
("trabajos", "Jobs for non-actors", """
  <p>Not everyone wants to or can speak on stage, and the show can't go on without these jobs. They are real parts: they appear in the program with each child's name.</p>
  <ul class="tarjetas">
   <li><h3>🎤 Presenters</h3><span class="chip">5th or 6th · 1 or 2 children</span><p>They welcome the audience and <strong>announce the play and its author</strong>: “We present <span lang="es">El bosque mágico</span>, The Magical Forest, by Vicente Cañón.” The author asks for his name to be said before every performance.</p></li>
   <li><h3>🔊 Sound</h3><span class="chip">4th to 6th · 2 children</span><p>They play each track at the right moment, following the <a href="#entradas">cue sheet</a>.</p></li>
   <li><h3>💡 Lights</h3><span class="chip">5th &amp; 6th · 1 or 2 children</span><p>Daylight for scenes 1 to 6, and blue nighttime light for the cave.</p></li>
   <li><h3>🌳 Curtain and bushes</h3><span class="chip">5th &amp; 6th · 2 to 4 children</span><p>They open and close the curtain and check that the four bushes stand firmly.</p></li>
   <li><h3>🧺 Props</h3><span class="chip">4th to 6th · 2 children</span><p>They set out the cauldron and the ice creams on a table backstage and put them away afterward.</p></li>
   <li><h3>📖 Prompter</h3><span class="chip">5th or 6th · 1 or 2 children</span><p>They follow the script backstage and whisper a line to anyone who forgets it.</p></li>
   <li><h3>🤝 Backstage buddies</h3><span class="chip">5th · 1 for every 2 or 3 little ones</span><p>They take Pre-K and K children to their places, join them in the final dance and bring them back.</p></li>
   <li><h3>🎨 Sets</h3><span class="chip">Any grade</span><p>They paint the bushes, the cauldron and the backdrop of trees and mountains.</p></li>
   <li><h3>👒 Costumes</h3><span class="chip">4th to 6th, with an adult</span><p>They help the little ones put on wings, flower crowns, caps and hats.</p></li>
   <li><h3>📰 Poster and program</h3><span class="chip">3rd to 6th · 2 to 4 children</span><p>They prepare the <a href="obra-bosque-magico-cartel-en.html">poster</a> and the program, with the title, the author and the names of the whole cast.</p></li>
   <li><h3>🎟️ Front of house</h3><span class="chip">4th to 6th · 2 to 4 children</span><p>They greet families, hand out programs and help people find a seat.</p></li>
   <li><h3>📸 Photos and video</h3><span class="chip">6th, with an adult</span><p>They film only the children whose families gave permission. These are the photos and videos sent to the author.</p></li>
  </ul>"""),
("musica", "Music and closing song", """
  <p>The author suggests this list, which is optional. Almost all the pieces come from the <strong>YouTube Audio Library</strong> and are free to use (happy music for children). <strong>The author offers to send them as mp3 files</strong> to anyone who asks, by email: see <a href="#autor">the author</a>.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Music list</caption>
   <thead><tr><th scope="col">Track</th><th scope="col">Piece</th><th scope="col">Mood</th><th scope="col">When it plays</th></tr></thead>
   <tbody>
    <tr><td>1</td><td><em>The New Order</em>, Aaron Kenny</td><td>Dark, cinematic</td><td>Witches and wizards (scenes 1 and 4)</td></tr>
    <tr><td>2</td><td><em>Sand Castle</em>, Quincas Moreira</td><td>Children's, upbeat</td><td>Dance of the Village of Joy</td></tr>
    <tr><td>3</td><td><em>St. Francis</em>, Josh Lippi &amp; The Overtimers</td><td>Rock, sad</td><td>Each village's sad exit</td></tr>
    <tr><td>4</td><td><em>Rainbow Forest</em>, Quincas Moreira</td><td>Children's, happy</td><td>Dance of the Village of Friendship</td></tr>
    <tr><td>5</td><td><em>Goat</em>, Wayne Jones</td><td>Children's, happy</td><td>Ice cream dance, Village of Generosity</td></tr>
    <tr><td>6</td><td><em>Sleeping Sheep</em>, The Green Orbs</td><td>Children's, calm</td><td>The worried wise people</td></tr>
    <tr><td>7</td><td>Robert Schumann, <em>Kinderszenen</em>, Op. 15, No. 1, “Of Foreign Lands and Peoples”</td><td>Piano</td><td>Fairies and elves come in and go out</td></tr>
    <tr><td>8</td><td>Johannes Brahms, <em>Lullaby</em> (Wiegenlied)</td><td>Lullaby</td><td>Night: the witches and wizards fall asleep</td></tr>
    <tr><td>9</td><td><em>Twirly Tops</em>, The Green Orbs</td><td>Children's, happy</td><td>The big circle dance</td></tr>
    <tr><td>10</td><td><em>Dancing on Green Grass</em>, The Green Orbs</td><td>Children's, upbeat</td><td>Ending and bows</td></tr>
   </tbody>
  </table>
  </div>
  <div class="nota"><strong>Tracks 7 and 8:</strong> Schumann's and Brahms's music is in the public domain, but not every recording is. The author suggests Vladimir Horowitz's recording; if you plan to post videos of the show, use free recordings, such as those from <a href="https://musopen.org/" target="_blank" rel="noopener noreferrer">Musopen</a>, or ask the author for the tracks.</div>
  <h3>Closing song: “A bailar en el bosque” (Let's Dance in the Forest)</h3>
  <p>A Lumi song to close the play, written from its ideas: joy, friendship, generosity, the shared ice cream and the broken spell. <strong>It is not part of the author's text</strong>; Vicente Cañón has heard it and called it “a great idea to give the play a final flourish”. It comes after the last narration, with the whole cast in a circle. Each line is sung twice, so the little ones can repeat it. The song is in Spanish.</p>
  <video class="guia" controls preload="none" poster="bm-cancion-portada.jpg" width="1024" height="1024" style="max-width:520px" lang="es"><source src="bm-cancion.mp4" type="video/mp4"><track kind="captions" src="bm-cancion-es.vtt" srclang="es" label="Español" default>Your browser cannot play this video. <a href="bm-cancion.mp4">Download the song</a>.</video>
  <details style="margin:.6rem 0"><summary><strong>Lyrics (in Spanish)</strong></summary><p lang="es" style="font-size:1.1rem;line-height:1.7">En el bosque de la magia,<br>todos juntos a bailar.<br>La tristeza se marchó,<br>¡la alegría ya llegó!<br><br>Compartimos el helado,<br>damos saltos de ilusión;<br>si jugamos como amigos,<br>se ilumina el corazón.<br><br>En el bosque de la magia,<br>hadas, duendes y los sabios<br>el hechizo rompen ya;<br>brujas y brujos sonrientes<br>¡cantan con nosotros hoy!<br><br>¿Quién comparte su bondad?<br>¡Generosidad!<br>¿Quién nos une de verdad?<br>¡La amistad!<br>¿Y qué canta el bosque entero?<br>¡Felicidad!<br>¡Uno, dos y tres: a sonreír!</p></details>"""),
("entradas", "Cue sheet (sound and lights)", """
  <p>For the tech crew. Each “cue” is a change: it happens when the event in the “Signal” column takes place. The lights are Lumi's suggestion; the play also works with ordinary room lighting.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Sound and light cues</caption>
   <thead><tr><th scope="col">No.</th><th scope="col">Scene</th><th scope="col">Signal</th><th scope="col">Sound</th><th scope="col">Lights</th></tr></thead>
   <tbody>
    <tr><td>1</td><td>1</td><td>The curtain opens</td><td>Silence</td><td>Warm daylight</td></tr>
    <tr><td>2</td><td>1</td><td>The witches and wizards move to the front of the stage</td><td>Track 1; fades down when they speak</td><td>—</td></tr>
    <tr><td>3</td><td>1</td><td>“Ha, ha, ha...”, after “Yes!”</td><td>Track 1 while the cauldron comes in</td><td>—</td></tr>
    <tr><td>4</td><td>1</td><td>“Let's go spread it... now!”</td><td>Track 1 while they carry out the cauldron and form the train</td><td>—</td></tr>
    <tr><td>5</td><td>2</td><td>The narration ends</td><td>Track 2: dance of Joy; stops when they finish</td><td>—</td></tr>
    <tr><td>6</td><td>2</td><td>“Oh! Oh!”</td><td>Track 3: sad exit</td><td>—</td></tr>
    <tr><td>7</td><td>3</td><td>The witches and wizards hide</td><td>Track 4: dance of Friendship</td><td>—</td></tr>
    <tr><td>8</td><td>3</td><td>Villagers 3 and 4 stick out their tongues</td><td>Track 3: sad exit</td><td>—</td></tr>
    <tr><td>9</td><td>4</td><td>The witches and wizards hide for the last time</td><td>Track 5: ice cream dance</td><td>—</td></tr>
    <tr><td>10</td><td>4</td><td>All the villagers stick out their tongues</td><td>Track 3: sad exit</td><td>—</td></tr>
    <tr><td>11</td><td>4</td><td>“We have done away with happiness!” · “Ha, ha, ha!”</td><td>Track 1: they exit stage right</td><td>—</td></tr>
    <tr><td>12</td><td>5</td><td>The narration ends</td><td>Track 6: the wise people walk around, worried</td><td>—</td></tr>
    <tr><td>13</td><td>6</td><td>The narration ends (“...eager to be heard”)</td><td>Track 7: the fairies and elves come in</td><td>—</td></tr>
    <tr><td>14</td><td>6</td><td>“That's just what we'll do!”</td><td>Track 7: the fairies and elves leave</td><td>—</td></tr>
    <tr><td>15</td><td>7</td><td>The narrator says “That night...”</td><td>Silence</td><td>Fade to soft blue night</td></tr>
    <tr><td>16</td><td>7</td><td>The narration ends</td><td>Track 8: the lullaby, while everyone tiptoes in</td><td>Night</td></tr>
    <tr><td>17</td><td>8</td><td>“One, two and... three!”</td><td>Track 9: the big circle dance</td><td>Night, with a light in the center</td></tr>
    <tr><td>18</td><td>8</td><td>“Of course you can!”</td><td>—</td><td>Daylight returns</td></tr>
    <tr><td>19</td><td>8</td><td>“...our play is all played out.”</td><td>Track 10: final dance and bows</td><td>Full light</td></tr>
    <tr><td>20</td><td>End</td><td>The bows end; everyone in a circle</td><td>Song “A bailar en el bosque”: everyone sings and dances</td><td>Full light; at the end, the curtain closes</td></tr>
   </tbody>
  </table>
  </div>"""),
("vestuario", "Costumes", """
  <p>These are the costumes the author suggests. Most can be put together from clothes at home; the rest are made in class.</p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Costumes by part</caption>
   <thead><tr><th scope="col">Part</th><th scope="col">Clothes from home</th><th scope="col">Made at school</th></tr></thead>
   <tbody>
    <tr><td><span class="muestra" style="background:#F2C200" aria-hidden="true"></span>Village of Joy</td><td>Jeans and a yellow T-shirt.</td><td>—</td></tr>
    <tr><td><span class="muestra" style="background:#2F6FC0" aria-hidden="true"></span>Village of Friendship</td><td>Jeans and a blue T-shirt.</td><td>—</td></tr>
    <tr><td><span class="muestra" style="background:#C8302B" aria-hidden="true"></span>Village of Generosity</td><td>Jeans and a red T-shirt.</td><td>Prop ice creams.</td></tr>
    <tr><td>Fairies</td><td>Colored tights and a T-shirt.</td><td>Tulle skirt, wings and a flower crown.</td></tr>
    <tr><td>Elves</td><td>Green T-shirt and green tights or pants.</td><td>Green cap; elf ears, if you like.</td></tr>
    <tr><td>Witches</td><td>Black dress or black clothes.</td><td>Pointed black hat made of construction paper.</td></tr>
    <tr><td>Wizards</td><td>Dark clothes.</td><td>Black cape and black hat.</td></tr>
    <tr><td>Wise People</td><td>Light-colored clothes.</td><td>White coat (a large adult shirt works) and round glasses without lenses.</td></tr>
    <tr><td>Narrators</td><td>Neat school clothes.</td><td>—</td></tr>
    <tr><td>Tech crew</td><td>Black or dark clothes, so they don't stand out.</td><td>—</td></tr>
   </tbody>
  </table>
  </div>
  <div class="nota"><strong>Why these colors:</strong> the author asks for a different color for each village. Since the elves wear green, the Village of Generosity wears red, so every group stands out in the final dance.</div>"""),
("cotejo", "Costume and prop checklist", f"""
  <p>For each group's teacher: check each box when the child is all set. Print one per classroom.</p>
  <p>Classroom: <span class="hueco">&nbsp;</span> Teacher: <span class="hueco">&nbsp;</span> Group's part: <span class="hueco">&nbsp;</span></p>
  <div class="envoltura-tabla">
  <table class="tabla">
   <caption class="sr">Checklist by child</caption>
   <thead><tr><th scope="col">Name</th><th scope="col">Clothes from home</th><th scope="col">Piece made in class (wings, cap, hat...)</th><th scope="col">Labeled with name</th><th scope="col">Ready for dress rehearsal</th></tr></thead>
   <tbody>
{casillas(4)}
   </tbody>
  </table>
  </div>
  <h3>Props</h3>
  <ul class="lista-casillas">
   <li><span class="casilla"></span>Four cardboard bushes, sturdy and with their supports</li>
   <li><span class="casilla"></span>Big cardboard pot or cauldron</li>
   <li><span class="casilla"></span>Prop ice creams for the Village of Generosity</li>
   <li><span class="casilla"></span>Painted backdrop with trees and mountains</li>
   <li><span class="casilla"></span>All ten tracks in order and tested on the sound system</li>
   <li><span class="casilla"></span>Colored tape on the floor: yellow, blue and red for the villages</li>
  </ul>"""),
("escenografia", "Sets and props", """
  <ul>
   <li><strong>Backdrop:</strong> mountains and trees painted on paper or cardboard, set apart from the curtain.</li>
   <li><strong>Four bushes</strong> cut out of cardboard and painted in several shades of green, with a cardboard back support folded into a triangle so they stand on their own. The witches and wizards hide behind them, so they need to be tall and wide.</li>
   <li><strong>A big pot or cauldron</strong> made of cardboard painted black, with fire and stones painted at the base, also with a back support. One witch and one wizard carry it in and out.</li>
   <li><strong>Prop ice creams</strong> made of foam sheets, cardboard or plastic, for the Village of Generosity.</li>
   <li><strong>The cave</strong> (scenes 7 and 8): no set is needed. The nighttime light and the witches and wizards lying down in the center are enough.</li>
  </ul>
  <p>At the end of his play, the author includes photos of the bushes and the cauldron made for the original production, all of cardboard. The infographics in <a href="#imagenes">the play in pictures</a> show how to make them.</p>"""),
("plano", "Stage plan", """
  <p>Seen from the audience. “Upstage” is farthest from the audience; “downstage” is closest. The three villages sit on the floor in front of the stage, facing the audience, and go up on stage when it's their turn.</p>
  <h3>Scenes 1 to 4</h3>
  <div class="plano" role="img" aria-label="Scenes 1 to 4: upstage, four bushes with the witches and wizards hiding behind them; downstage center, the narrator and, later, the village that dances; in front of the stage, the three villages sitting and facing the audience: Joy on the left, Friendship in the center, Generosity on the right.">
   <div><b>Upstage left</b>Bushes 1 and 2 · witches and wizards</div><div><b>Upstage center</b>Backdrop of trees and mountains</div><div><b>Upstage right</b>Bushes 3 and 4 · witches and wizards</div>
   <div><b>Downstage left</b>Narrator</div><div><b>Downstage center</b>Cauldron (scene 1) · the village that dances (scenes 2 to 4)</div><div><b>Downstage right</b>Witches and wizards exit (scene 4)</div>
  </div>
  <div class="plano" role="img" aria-label="In front of the stage: the three villages, seated.">
   <div><b>In front, left</b>Village of Joy (yellow)</div><div><b>In front, center</b>Village of Friendship (blue)</div><div><b>In front, right</b>Village of Generosity (red)</div>
  </div><p class="publico">Audience</p>
  <h3>Scenes 5 and 6</h3>
  <div class="plano" role="img" aria-label="Scenes 5 and 6: the wise people in the center; the fairies come in from the left and the elves from the right.">
   <div><b>Upstage left</b>Bushes</div><div><b>Upstage center</b>—</div><div><b>Upstage right</b>Bushes</div>
   <div><b>Downstage left</b>Fairies</div><div><b>Downstage center</b>Wise People</div><div><b>Downstage right</b>Elves</div>
  </div><p class="publico">Audience</p>
  <h3>Scenes 7 and 8</h3>
  <div class="plano" role="img" aria-label="Scenes 7 and 8: the witches and wizards sleep in the center; around them, a big circle of fairies, elves, wise people and the three villages. After the dance, the circle opens into a half circle.">
   <div><b>Upstage left</b>Circle</div><div><b>Upstage center</b>Circle</div><div><b>Upstage right</b>Circle</div>
   <div><b>Downstage left</b>Circle</div><div><b>Downstage center</b>Witches and wizards, asleep</div><div><b>Downstage right</b>Circle</div>
  </div><p class="publico">Audience</p>
  <div class="nota">After the dance, the circle <strong>opens into a half circle toward the sides</strong>, so the audience can see the witches and wizards as they wake up. On a small stage, make a double circle: the little ones inside, with their buddies, and the older children outside.</div>"""),
("ensayos", "Rehearsals", """
  <h3>Weeks 1 to 3: each group in its classroom</h3>
  <ul>
   <li><strong>Pre-K and K:</strong> 15-minute sessions. Waving to the audience when the narrator names their village, their village's dance, and the curse gestures: sad faces, sticking out tongues, not wanting to share.</li>
   <li><strong>1st and 2nd:</strong> the entrance with music, the lines said together (“We have come to help you”, “On the count of three, we'll start to dance”) and the circle dance.</li>
   <li><strong>3rd and 4th:</strong> the witches and wizards: the cauldron mime, the spell and the “choo-choo train”; the wise people: the worried walk and their dialogue.</li>
   <li><strong>5th and 6th:</strong> the narrator's verses, calmly and in a clear voice, and the tech crew with the cue sheet.</li>
   <li><strong>Everyone:</strong> the closing song, “A bailar en el bosque”, in a circle.</li>
  </ul>
  <h3>Weeks 4 and 5: in blocks</h3>
  <ul>
   <li><strong>Block A, the curse (scenes 1 to 4):</strong> witches and wizards with one village at a time.</li>
   <li><strong>Block B, the solution (scenes 5 and 6):</strong> wise people with fairies and elves.</li>
   <li><strong>Block C, the night and the dance (scenes 7 and 8):</strong> all the groups, with the backstage buddies.</li>
   <li><strong>Narrators:</strong> join each block to match their timing with the music.</li>
  </ul>
  <h3>Last week: dress rehearsals</h3>
  <ol>
   <li>Mark with colored tape on the floor where each village sits; entrances and exits with music.</li>
   <li>The whole play with costumes, bushes, cauldron and ice creams, and the final bows.</li>
  </ol>
  <div class="nota">No one has to memorize if they can't. Narrators can read on stage, with the script in a black folder. The little ones say their lines together, and a buddy can whisper the line to them just before. In the <a href="obra-bosque-magico-en.html">script</a>, each child can choose a part, see only their own lines and listen to them read aloud.</div>"""),
("clase", "In the classroom", """
  <p>The author recommends that, <strong>before rehearsals begin</strong>, classes explore the play's values and their opposites: joy and sadness, friendship and unfriendliness, generosity and selfishness.</p>
  <ul class="tarjetas">
   <li><h3>Pre-K and K</h3><p><strong>Faces and gestures.</strong> Show “happy” and “sad”, “friends” and “cross”, “sharing” and “not sharing” with face and body. That is exactly what they will do on stage.</p><p>Share something among everyone, such as paper ice creams, and talk about how sharing feels.</p></li>
   <li><h3>1st and 2nd</h3><p><strong>How can we help?</strong> The fairies and elves don't fight: they come up with a plan. What can we do when a classmate is sad or angry?</p><p>Practice the circle and count “one, two and three” all together.</p></li>
   <li><h3>3rd and 4th</h3><p><strong>Envy and second chances.</strong> Why are the witches and wizards envious? At the end they ask to be friends and everyone says yes: why is forgiving important?</p><p>The wise people can't find the answer on their own: when is it good to ask for help?</p></li>
   <li><h3>5th and 6th</h3><p><strong>Verse and rhyme.</strong> Find the rhymes in the narration (“wood” and “good”, “dance” and “chance”) and read them aloud, keeping the beat.</p><p>Compare the English with <a href="obra-bosque-magico-es.html" lang="es">the original Spanish</a>: how was “<span lang="es">colorín, colorado</span>” translated?</p></li>
  </ul>"""),
("carta", "Family letter", f"""
  <p class="solo-pantalla">Ready to print. Fill in the blanks by hand. At the end there is a slip to sign and return.</p>
  <div class="carta">
   <p><strong>School play: <em><span lang="es">El bosque mágico</span> (The Magical Forest)</em>, by Vicente Cañón</strong></p>
   <p>Date: <span class="hueco">&nbsp;</span></p>
   <p>Dear family,</p>
   <p>This year, the whole school, from Pre-K to 6th grade, will perform <em><span lang="es">El bosque mágico</span> (The Magical Forest)</em>, a children's play by Vicente Cañón. It tells the story of three villages, the Village of Joy, the Village of Friendship and the Village of Generosity, who lose their happiness because of a curse and get it back by dancing all together. While they rehearse, the children will talk in class about joy, friendship and generosity.</p>
   <p><strong>Your child</strong> <span class="hueco">&nbsp;</span> <strong>will be:</strong> <span class="hueco">&nbsp;</span></p>
   <p><strong>Clothes we ask for, if you have them at home</strong> (there's no need to buy anything):</p>
   <p><span class="hueco" style="min-width:100%">&nbsp;</span></p>
   <p>The school will make the wings, flower crowns, caps, hats and capes in class. If you don't have an item, let us know: we will have clothes to lend.</p>
   <p><strong>Important dates</strong></p>
   <ul>
    <li>Bring the clothes, in a bag labeled with your child's name and grade: <span class="hueco">&nbsp;</span></li>
    <li>Dress rehearsal: <span class="hueco">&nbsp;</span></li>
    <li>Performance: date <span class="hueco">&nbsp;</span>, time <span class="hueco">&nbsp;</span>, place <span class="hueco">&nbsp;</span></li>
   </ul>
   <p><strong>How you can help at home:</strong> if your child has lines, practice them together. The script is on Lumi (www.lumi-educa.com), in English and Spanish, with a button to listen to each line and another to show only your child's lines.</p>
   <p><strong>About photos and videos:</strong> the author of the play asks schools to send him photos and videos of their performances. We will only send pictures of children whose families give permission on the slip below.</p>
   <p>Thank you for joining us!</p>
   <p>Sincerely,<br><span class="hueco">&nbsp;</span></p>
   <div class="talon">
    <p><strong>Please sign and return this slip by</strong> <span class="hueco">&nbsp;</span></p>
    <p>Child's name: <span class="hueco">&nbsp;</span> Grade: <span class="hueco">&nbsp;</span></p>
    <p><span class="casilla"></span>I give permission for my child to take part in the play.</p>
    <p><span class="casilla"></span>I give permission for the school to post photos or videos of the play that show my child, and to send them to the author of the play.</p>
    <p><span class="casilla"></span>I do <strong>not</strong> give permission to post or send photos or videos that show my child.</p>
    <p><span class="casilla"></span>I can help with: <span class="casilla" style="margin-left:.4rem"></span>costumes <span class="casilla" style="margin-left:.4rem"></span>sets <span class="casilla" style="margin-left:.4rem"></span>the day of the show</p>
    <p>Signature: <span class="hueco" style="min-width:14em">&nbsp;</span> Phone: <span class="hueco">&nbsp;</span></p>
   </div>
  </div>"""),
 ],
)
EN_NAV = [("autor","The author"),("resumen","At a glance"),("imagenes","Pictures and video"),("reparto","Cast by grade"),("escenas","Scene by scene"),("trabajos","Jobs for non-actors"),("musica","Music and song"),("entradas","Cue sheet"),("vestuario","Costumes"),("cotejo","Checklist"),("escenografia","Sets"),("plano","Stage plan"),("ensayos","Rehearsals"),("clase","In the classroom"),("carta","Family letter")]


def guia(D, NAV):
    L = D["lang"]
    menu = "\n".join(f'   <a href="{h}"{" aria-current=\"page\"" if h == D["teatro"] else ""}>{x}</a>' for h, x in D["menu"])
    nav = "\n".join(f'  <li><a href="#{a}">{x}</a></li>' for a, x in NAV)
    secs = []
    for sid, tit, cuerpo in D["secciones"]:
        secs.append(f''' <!-- ================= {sid.upper()} ================= -->
 <details class="seccion acord" id="{sid}" name="partes">
  <summary><h2 id="t-{sid}">{tit}</h2></summary>
  <div class="cuerpo">{cuerpo}
  <p class="arriba"><a href="#contenido" class="cerrar">{D["arriba"]}</a></p>
 </div>
 </details>''')
    h1 = D["titulo"] if L == "es" else '<span lang="es">El bosque mágico</span> (The Magical Forest) · Production'
    return f'''<!doctype html>
<!-- «El bosque mágico» · Obra de {AUTOR} © 2019 (www.obrasteatro.com) · Publicada en Lumi con autorización del autor.
     Guía de producción: Lumi (José M. Fernández) · CC BY-NC-SA 4.0 · Generado con herramientas/gen_bosque_produccion.py -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{D["titulo"]} · Lumi</title>
<meta name="description" content="{D["desc"]}">
<meta name="author" content="{AUTOR}">
<link rel="alternate" hreflang="{"en" if L=="es" else "es"}" href="{D["otro"]}">
<link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="lumi.css?v=6">
<style>{CSS}</style>
</head>
<body>
<a class="saltar" href="#contenido">{D["saltar"]}</a>
<header class="cabecera">
 <div class="envoltura">
  <a class="marca" href="{D["inicio"]}"><img src="lumi-logo-horizontal.svg" alt="{D["logo_alt"]}" width="560" height="240"></a>
  <nav aria-label="{D["menu_lbl"]}" class="menu">
{menu}
  </nav>
  {D["idioma"]}
 </div>
</header>

<section class="obra-cab" aria-labelledby="titulo">
 <div class="envoltura">
  <p style="margin:0">{D["volver"]}</p>
  <h1 id="titulo">{h1}</h1>
  <p class="autor">{D["autor"]}</p>
  <p style="margin:.3rem 0 0">{D["intro"]}</p>
  <div class="herr solo-pantalla">{D["herr"]}</div>
 </div>
</section>

<main id="contenido" tabindex="-1"><div class="envoltura">
 <nav aria-label="{D["partes"]}"><ul class="anclas">
{nav}
 </ul></nav>

{chr(10).join(secs)}
</div></main>
<footer class="pie"><div class="envoltura"><p>{D["pie"]}</p></div></footer>
<script>{JS}</script>
</body>
</html>
'''

# ======================================================================= CARTEL
CARTEL = {
 "es": dict(lang="es", otro="obra-bosque-magico-cartel-en.html", volver="obra-bosque-magico-produccion-es.html", volver_txt="← Guía de producción",
   titulo_pag="El bosque mágico · Cartel", inicio="index-es.html", saltar="Saltar al contenido",
   instr="Escriba en los espacios punteados (haga clic sobre ellos) el nombre de la escuela, la ciudad, la fecha, la hora y el lugar. Después pulse «Imprimir». Se imprime en una hoja carta o A4, en vertical.",
   imprimir="🖨️ Imprimir el cartel", nota_autor="El autor pide que su nombre figure siempre en los carteles y que le envíen uno. Envíelo con las fotos a",
   antetitulo="La escuela presenta", titulo="El bosque mágico", subtitulo="", obra="Una obra de teatro de", elenco="Con todos los alumnos, de prekínder a 6.º grado",
   escuela="Nombre de la escuela", ciudad="Ciudad, estado", pais="Estados Unidos", fecha="Día y fecha", hora="Hora", lugar="Lugar",
   lbl_fecha="Día", lbl_hora="Hora", lbl_lugar="Lugar", lema="Alegría · Amistad · Generosidad",
   alt="Todo el elenco baila en un gran círculo en el bosque alrededor de las brujas y los brujos dormidos.",
   pie=f"«El bosque mágico» · Vicente Cañón © 2019 · www.obrasteatro.com", entrada="Entrada libre"),
 "en": dict(lang="en", otro="obra-bosque-magico-cartel-es.html", volver="obra-bosque-magico-produccion-en.html", volver_txt="← Production guide",
   titulo_pag="El bosque mágico (The Magical Forest) · Poster", inicio="index.html", saltar="Skip to content",
   instr="Type in the dotted spaces (click on them) the name of the school, the city, the date, the time and the place. Then press “Print”. It prints on one letter or A4 sheet, portrait.",
   imprimir="🖨️ Print the poster", nota_autor="The author asks for his name to always appear on posters, and to be sent one. Send it with the photos to",
   antetitulo="The school presents", titulo="El bosque mágico", subtitulo="The Magical Forest", obra="A play by", elenco="With all our students, from Pre-K to 6th grade",
   escuela="School name", ciudad="City, State", pais="United States", fecha="Day and date", hora="Time", lugar="Place",
   lbl_fecha="Date", lbl_hora="Time", lbl_lugar="Place", lema="Joy · Friendship · Generosity",
   alt="The whole cast dances in a big circle in the forest around the sleeping witches and wizards.",
   pie=f"“El bosque mágico” (The Magical Forest) · Vicente Cañón © 2019 · www.obrasteatro.com", entrada="Free admission"),
}

def cartel(L):
    c = CARTEL[L]
    idioma = (f'<span aria-current="true">Español</span><a href="{c["otro"]}" lang="en" hreflang="en">English</a>' if L == "es"
              else f'<a href="{c["otro"]}" lang="es" hreflang="es">Español</a><span aria-current="true">English</span>')
    sub = f'<p class="c-sub">{c["subtitulo"]}</p>' if c["subtitulo"] else ""
    tit = c["titulo"] if L == "es" else f'<span lang="es">{c["titulo"]}</span>'
    campo = lambda cls, ph: f'<span class="campo {cls}" contenteditable="true" role="textbox" aria-label="{ph}" data-ph="{ph}"></span>'
    return f'''<!doctype html>
<!-- Cartel de «El bosque mágico», obra de {AUTOR} © 2019 · Plantilla de Lumi (José M. Fernández) · CC BY-NC-SA 4.0 -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c["titulo_pag"]} · Lumi</title>
<meta name="author" content="{AUTOR}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="lumi.css?v=6">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;700&display=swap" rel="stylesheet">
<style>
 .ayuda{{max-width:820px;margin:1rem auto;padding:0 16px}}
 .ayuda .herr{{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;margin:.6rem 0}}
 .ayuda button,.ayuda a.b{{display:inline-flex;align-items:center;min-height:44px;padding:0 1rem;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);font:inherit;font-weight:700;text-decoration:none;cursor:pointer}}
 .cartel{{max-width:820px;margin:0 auto 2rem;aspect-ratio:8.5/11;background:#0f2a24;color:#fff;border-radius:18px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 6px 24px rgba(0,0,0,.18)}}
 .c-top{{padding:4% 6% 2%;text-align:center;background:linear-gradient(#0f2a24,#173d33)}}
 .c-ante{{font-size:clamp(.9rem,2.4vw,1.25rem);letter-spacing:.12em;text-transform:uppercase;margin:0;color:#ffe08a}}
 .c-esc{{font-size:clamp(1.1rem,3.4vw,1.8rem);font-weight:700;margin:.3rem 0 0}}
 .c-tit{{font-family:Fredoka,system-ui,sans-serif;font-weight:700;font-size:clamp(2.4rem,9vw,5rem);line-height:1;margin:.25em 0 0;color:#fff;text-shadow:0 3px 0 #0a1c18}}
 .c-sub{{font-family:Fredoka,system-ui,sans-serif;font-size:clamp(1.2rem,4vw,2.1rem);margin:.15em 0 0;color:#bfeccd}}
 .c-autor{{font-size:clamp(1rem,3vw,1.5rem);margin:.5em 0 0}}
 .c-autor strong{{color:#ffe08a}}
 .c-img{{flex:1;min-height:0;background:#000}}
 .c-img img{{width:100%;height:100%;object-fit:cover;display:block}}
 .c-pie{{padding:3% 6% 4%;text-align:center;background:#173d33}}
 .c-elenco{{margin:0;font-size:clamp(.95rem,2.6vw,1.3rem)}}
 .c-lema{{margin:.3rem 0 .6rem;font-weight:700;letter-spacing:.06em;color:#bfeccd}}
 .c-datos{{display:flex;flex-wrap:wrap;justify-content:center;gap:.4rem 1.4rem;font-size:clamp(1rem,2.8vw,1.35rem);font-weight:700}}
 .c-datos span.lbl{{color:#ffe08a;margin-right:.3rem}}
 .c-entrada{{margin:.5rem 0 0;font-size:clamp(.9rem,2.4vw,1.1rem)}}
 .c-cred{{margin:.6rem 0 0;font-size:clamp(.7rem,1.8vw,.85rem);opacity:.9}}
 .campo{{display:inline-block;min-width:6em;border-bottom:2px dotted #ffe08a;outline:none;padding:0 .15em}}
 .campo:empty::before{{content:attr(data-ph);color:#c9d8d2;font-weight:400;font-style:italic}}
 .campo:focus{{background:rgba(255,224,138,.15)}}
 @media print{{
  @page{{size:letter portrait;margin:0}}
  body{{background:#fff}} .cabecera,.ayuda,.pie,.saltar{{display:none!important}}
  .cartel{{max-width:none;width:100vw;height:100vh;aspect-ratio:auto;margin:0;border-radius:0;box-shadow:none;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
  .campo{{border-bottom:0}} .campo:empty::before{{content:"";}}
 }}
</style>
</head>
<body>
<a class="saltar" href="#contenido">{c["saltar"]}</a>
<header class="cabecera">
 <div class="envoltura">
  <a class="marca" href="{c["inicio"]}"><img src="lumi-logo-horizontal.svg" alt="Lumi" width="560" height="240"></a>
  <div class="idioma" role="group" aria-label="{"Idioma" if L=="es" else "Language"}">{idioma}</div>
 </div>
</header>
<div class="ayuda">
 <p style="margin:.4rem 0"><a href="{c["volver"]}">{c["volver_txt"]}</a></p>
 <p>{c["instr"]}</p>
 <div class="herr"><button type="button" onclick="window.print()">{c["imprimir"]}</button></div>
 <p style="font-size:.95rem">{c["nota_autor"]} <a href="mailto:{CORREO}">{CORREO}</a>.</p>
</div>
<main id="contenido" tabindex="-1">
<article class="cartel" aria-label="{c["titulo_pag"]}">
 <div class="c-top">
  <p class="c-ante">{c["antetitulo"]}</p>
  <p class="c-esc">{campo("escuela", c["escuela"])}</p>
  <h1 class="c-tit">{tit}</h1>
  {sub}
  <p class="c-autor">{c["obra"]} <strong>Vicente Cañón</strong></p>
 </div>
 <div class="c-img"><img src="bm-cartel.jpg" alt="{c["alt"]}" width="1200" height="831"></div>
 <div class="c-pie">
  <p class="c-elenco">{c["elenco"]}</p>
  <p class="c-lema">{c["lema"]}</p>
  <div class="c-datos">
   <span><span class="lbl">{c["lbl_fecha"]}:</span>{campo("fecha", c["fecha"])}</span>
   <span><span class="lbl">{c["lbl_hora"]}:</span>{campo("hora", c["hora"])}</span>
   <span><span class="lbl">{c["lbl_lugar"]}:</span>{campo("lugar", c["lugar"])}</span>
  </div>
  <p class="c-entrada">{campo("ciudad", c["ciudad"])} · {campo("pais", c["pais"]) .replace('></span>', '>' + c["pais"] + '</span>')} · {c["entrada"]}</p>
  <p class="c-cred">{c["pie"]}</p>
 </div>
</article>
</main>
<footer class="pie"><div class="envoltura"><p>{c["pie"]}</p></div></footer>
<script>
(function(){{
  var K="bosque-cartel-"+document.documentElement.lang;
  var cs=document.querySelectorAll(".campo");
  try{{ var g=JSON.parse(localStorage.getItem(K)||"{{}}"); cs.forEach(function(c){{ var k=c.className.split(" ")[1]; if(g[k]!=null) c.textContent=g[k]; }}); }}catch(e){{}}
  cs.forEach(function(c){{
    c.addEventListener("keydown",function(ev){{ if(ev.key==="Enter"){{ ev.preventDefault(); c.blur(); }} }});
    c.addEventListener("input",function(){{
      try{{ var g={{}}; cs.forEach(function(x){{ g[x.className.split(" ")[1]]=x.textContent; }}); localStorage.setItem(K,JSON.stringify(g)); }}catch(e){{}}
    }});
  }});
}})();
</script>
</body>
</html>
'''

if __name__ == "__main__":
    for D, NAV in ((ES, ES_NAV), (EN, EN_NAV)):
        with open(os.path.join(AQUI, f"obra-bosque-magico-produccion-{D['lang']}.html"), "w", encoding="utf-8") as f:
            f.write(guia(D, NAV))
    for L in ("es", "en"):
        with open(os.path.join(AQUI, f"obra-bosque-magico-cartel-{L}.html"), "w", encoding="utf-8") as f:
            f.write(cartel(L))
    print("ok")
