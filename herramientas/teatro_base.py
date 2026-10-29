"""
Estilos y programa comunes de los guiones interactivos del Teatro de Lumi
(colores por personaje, «Mi papel», solo mis líneas, lectura en voz alta, letra ampliable).
Los usan gen_inoka.py y, en la rama del guion en inglés, gen_bosque.py.
"""

CSS = """
.obra-cab{background:var(--cie);padding:1.4rem 0}
.obra-cab h1{font-size:clamp(1.8rem,4.5vw,2.6rem)}
.obra-cab .sub{font-size:1.2rem;margin:.3rem 0 0}
.obra-cab .autor{margin:.3rem 0 0;font-weight:700;font-size:1.15rem}
.obra-cab .permiso{font-size:.95rem}
.enlaces-obra{display:flex;flex-wrap:wrap;gap:.5rem;margin:.6rem 0 0;padding:0;list-style:none}
.enlaces-obra a{display:inline-flex;align-items:center;min-height:44px;padding:.3rem 1rem;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);font-weight:700;text-decoration:none}
.enlaces-obra a:hover{background:var(--cie)}
.barra{position:sticky;top:76px;z-index:5;background:#fff;border:2px solid var(--borde);border-radius:14px;padding:.6rem .8rem;margin:1rem 0;display:flex;flex-wrap:wrap;gap:.5rem;align-items:center}
.barra label{font-weight:700}
.barra select,.barra button{min-height:44px;font:inherit;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);padding:0 .9rem;font-weight:700;cursor:pointer}
.barra .chk{display:inline-flex;align-items:center;gap:.4rem;font-weight:700}
.barra .chk input{width:22px;height:22px}
.linea{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:.6rem;align-items:start;padding:.6rem .8rem;margin:.35rem 0;border-left:8px solid var(--c);border-radius:10px;background:#fff}
.linea .quien{display:inline-block;font-weight:700;color:#fff;background:var(--c);border-radius:999px;padding:.05rem .65rem;font-size:.9rem;margin-right:.4rem}
.linea .grado{font-size:.85rem;margin-right:.4rem}
.linea p{margin:.25rem 0 0}
.acot{font-style:italic;margin:.6rem 0;padding:.4rem .8rem;border-left:4px dashed var(--borde);color:#2d5f69}
.mus{margin:.6rem 0;padding:.45rem .8rem;border-radius:10px;background:#F3EEFA;color:#3d2a63;font-weight:700}
.mus small{font-weight:400}
.lugar{margin:1rem 0 .4rem;text-align:center;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:#2d5f69}
.oir{min-width:44px;min-height:44px;border-radius:50%;border:2px solid var(--pet);background:#fff;cursor:pointer;font-size:1.1rem}
.oir:hover{background:var(--cie)}
body.filtrando .linea{opacity:.35}
body.filtrando .linea.mia{opacity:1;box-shadow:0 0 0 3px var(--c)}
body.solo .linea:not(.mia){display:none}
body.solo .acot,body.solo .mus,body.solo .lugar{display:none}
.linea.hablando{outline:3px solid var(--ama)}
.cancion .letra{font-size:1.1rem;line-height:1.75;margin:.3rem 0 0}
.cancion .sentido{font-size:.95rem;font-style:italic;margin:.5rem 0 0;color:#2d5f69}
.cancion video{display:block;width:100%;max-width:420px;border-radius:12px;margin:.6rem 0 0;background:#000}
details.acord{border:2px solid var(--borde);border-radius:16px;margin:.8rem 0;padding:0;background:#fff}
details.acord > summary{padding:.8rem 1rem;min-height:56px;list-style:none;border:0;cursor:pointer}
details.acord > summary::-webkit-details-marker{display:none}
details.acord > summary::before{content:"▸";font-size:1.4rem;margin-right:.5rem}
details.acord[open] > summary::before{content:"▾"}
details.acord > summary h2{display:inline;font-size:1.35rem}
details.acord > summary:hover{background:var(--cie);border-radius:14px}
details.acord .cuerpo{padding:0 1rem 1rem}
.acto-h{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;justify-content:space-between}
.acto-h button{min-height:44px;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);font:inherit;font-weight:700;padding:0 .9rem;cursor:pointer}
.tabla{width:100%;border-collapse:collapse;margin:.5rem 0 1rem}
.tabla th,.tabla td{border:1px solid var(--borde);padding:.5rem .65rem;text-align:left;vertical-align:top}
.tabla th{background:var(--cie)}
.punto{display:inline-block;width:14px;height:14px;border-radius:50%;margin-right:.4rem;vertical-align:-2px}
.envoltura-tabla{overflow-x:auto}
body.grande{font-size:21px}
body.muygrande{font-size:24px}
main .seccion{scroll-margin-top:170px}
.barra select{max-width:100%}
@media (max-width:760px){.barra{position:static}.barra select{width:100%}main .seccion{scroll-margin-top:130px}}
@media print{.barra,.oir,.acto-h button,.cabecera,.anclas,.enlaces-obra{display:none!important}.linea{break-inside:avoid;border-left-width:6px}body.filtrando .linea{opacity:1}}
"""

JS = r"""
(function(){
  "use strict";
  var LANG = document.documentElement.lang, VOZ = document.body.getAttribute("data-voz");
  var sel = document.getElementById("mi-papel"), solo = document.getElementById("solo");
  function aplicar(){
    var p = sel.value;
    document.querySelectorAll(".linea").forEach(function(l){
      var ms = (l.getAttribute("data-papeles") || "").split(" ");
      l.classList.toggle("mia", !!p && ms.indexOf(p) >= 0);
    });
    document.body.classList.toggle("filtrando", !!p);
    document.body.classList.toggle("solo", !!p && solo.checked);
    if(p && solo.checked) document.querySelectorAll("details.acord").forEach(function(d){ if(d.querySelector(".linea.mia")) d.open = true; });
    try{ localStorage.setItem(CLAVE_PAPEL, p); }catch(e){}
  }
  try{ var g = localStorage.getItem(CLAVE_PAPEL); if(g && sel.querySelector('option[value="'+g+'"]')) sel.value = g; }catch(e){}
  sel.addEventListener("change", aplicar); solo.addEventListener("change", aplicar); aplicar();

  var hay = "speechSynthesis" in window, cola = [];
  function vozIdioma(){
    var vs = hay ? speechSynthesis.getVoices() : [];
    return vs.filter(function(v){ return v.lang === VOZ; })[0] || vs.filter(function(v){ return v.lang.slice(0,2) === LANG; })[0] || null;
  }
  function limpiar(){ document.querySelectorAll(".hablando").forEach(function(x){ x.classList.remove("hablando"); }); }
  function decir(lineas){
    if(!hay) return;
    speechSynthesis.cancel(); limpiar(); cola = lineas.slice();
    (function sig(){
      var l = cola.shift(); limpiar(); if(!l) return;
      var txt = l.querySelector(".txt").textContent.replace(/\([^)]*\)/g, " ");
      var u = new SpeechSynthesisUtterance(txt); u.lang = VOZ; var v = vozIdioma(); if(v) u.voice = v; u.rate = .95;
      l.classList.add("hablando"); u.onend = sig; u.onerror = function(){ limpiar(); };
      speechSynthesis.speak(u);
    })();
  }
  document.querySelectorAll(".oir").forEach(function(b){ b.addEventListener("click", function(){ decir([b.closest(".linea")]); }); });
  document.querySelectorAll(".oir-esc").forEach(function(b){ b.addEventListener("click", function(){
    var ls = [].slice.call(b.closest("details").querySelectorAll(".linea")).filter(function(l){ return getComputedStyle(l).display !== "none" && !l.classList.contains("cancion"); });
    decir(ls);
  }); });
  document.querySelectorAll(".parar").forEach(function(b){ b.addEventListener("click", function(){ cola = []; if(hay) speechSynthesis.cancel(); limpiar(); }); });
  if(!hay) document.querySelectorAll(".oir,.oir-esc,.parar").forEach(function(b){ b.hidden = true; });

  var tam = 0, clases = ["", "grande", "muygrande"];
  function poner(){ document.body.classList.remove("grande","muygrande"); if(clases[tam]) document.body.classList.add(clases[tam]); }
  document.getElementById("menor").addEventListener("click", function(){ tam = Math.max(0, tam-1); poner(); });
  document.getElementById("mayor").addEventListener("click", function(){ tam = Math.min(2, tam+1); poner(); });
  document.getElementById("imprimir").addEventListener("click", function(){ window.print(); });
  function abrir(id){ var d=document.getElementById(id); if(d && d.tagName==="DETAILS"){ d.open=true; setTimeout(function(){ d.scrollIntoView({block:"start"}); },30); return true; } return false; }
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener("click", function(ev){
      if(a.classList.contains("cerrar")){ var d=a.closest("details"); if(d) d.open=false; return; }
      var id=a.getAttribute("href").slice(1); if(abrir(id)){ ev.preventDefault(); history.replaceState(null,"","#"+id); }
    });
  });
  if(location.hash) abrir(location.hash.slice(1));
  document.querySelectorAll("details.acord").forEach(function(d){
    d.addEventListener("toggle", function(){
      if(d.open && !window.__imprimiendo) setTimeout(function(){ var c=document.querySelector(".cabecera"); var h=(c && getComputedStyle(c).position==="sticky") ? c.getBoundingClientRect().height : 0; window.scrollTo({top: window.scrollY + d.getBoundingClientRect().top - h - 10, behavior: "instant"}); }, 60);
    });
  });
  window.addEventListener("beforeprint", function(){ window.__imprimiendo=true; document.querySelectorAll("details.acord").forEach(function(d){ d.setAttribute("data-estaba", d.open?"1":""); d.open=true; }); });
  window.addEventListener("afterprint", function(){ setTimeout(function(){ window.__imprimiendo=false; },500); document.querySelectorAll("details.acord").forEach(function(d){ d.open = d.getAttribute("data-estaba")==="1"; }); });
})();
"""

def js_guion(clave):
    return JS.replace('CLAVE_PAPEL', '"' + clave + '"')
