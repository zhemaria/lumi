/* ==================================================================
   Lumi · Lógica del portal
   ------------------------------------------------------------------
   Lee catalogo.js (series de interactivos y juegos) y el catálogo
   de cuentos del repositorio cuentos-educativos, y arma:
     - inicio  (index-es.html / index.html, que es la portada en inglés)
     - grados  (grados-es.html / grados.html, en inglés por defecto) → una sección por grado
     - materias(materias-es.html / materias.html, en inglés por defecto) → una sección por materia
   El idioma se toma del atributo lang de la página.
   No guarda nada ni usa cookies.
   ================================================================== */
(function () {
  "use strict";

  var L = (document.documentElement.lang || "es").slice(0, 2) === "en" ? "en" : "es";
  var OTRO = L === "es" ? "en" : "es";
  var DATOS = window.LUMI;

  /* ---------------- textos ---------------- */
  var T = {
    es: {
      grados: "grados-es.html", materias: "materias-es.html",
      lecciones: function (n) { return n === 1 ? "1 actividad" : n + " actividades"; },
      cuentos: function (n) { return n === 1 ? "1 cuento" : n + " cuentos"; },
      verTodo: "Ver todo",
      tipo: { interactivo: "Interactivos", juego: "Juego", cuentos: "Cuentos ilustrados" },
      soloOtro: "Disponible por ahora solo en inglés.",
      soloEsEnEn: "",
      soloEnEnEs: "Esta serie está en inglés: enseña a leer en inglés.",
      vacio: "Lumi está preparando este grado. ¡Pronto habrá actividades!",
      proximamente: "Próximamente",
      pronto: "Próximamente también en: ",
      arriba: "↑ Volver arriba",
      cerrar: "↑ Cerrar y volver a la lista",
      abrirLibro: "Abrir el libro completo",
      guiaTit: "Para el docente",
      guia: "Guía para el docente de los cuentos (en inglés, con ayuda en español): consejos de uso y actividades de Ciencias y de Estudios Sociales",
      libroTit: { ciencias: "Cuentos de ciencias", sociales: "Cuentos de estudios sociales" },
      cuentosIndice: "index.html",
      errorCuentos: "No se pudieron cargar los cuentos en este momento.",
      cifras: ["actividades", "grados con material", "materias"],
      teatro: { cartel: "Ver el cartel de la obra: ", pronto: "En preparación", listo: "Lista", idiomas: "En español y en inglés",
                guionEs: "Guion en español", guionEn: "Guion en inglés", guia: "Guía de producción", historia: "Guía histórica para el docente", soloEs: "",
                traera: "Lo que traerá: guion, tarjetas de personajes, vestuario, escenarios y guía para el docente." }
    },
    en: {
      grados: "grados.html", materias: "materias.html",
      lecciones: function (n) { return n === 1 ? "1 activity" : n + " activities"; },
      cuentos: function (n) { return n === 1 ? "1 story" : n + " stories"; },
      verTodo: "See all",
      tipo: { interactivo: "Interactives", juego: "Game", cuentos: "Illustrated stories" },
      soloOtro: "For now, available only in Spanish.",
      soloEsEnEn: "This series is in Spanish: it teaches reading in Spanish.",
      soloEnEnEs: "",
      vacio: "Lumi is getting this grade ready. Activities are coming soon!",
      proximamente: "Coming soon",
      pronto: "Coming soon for: ",
      arriba: "↑ Back to top",
      cerrar: "↑ Close and go back to the list",
      abrirLibro: "Open the whole book",
      guiaTit: "For teachers",
      guia: "Teacher guide for the stories: tips for using them, and activities for Science and Social Studies",
      libroTit: { ciencias: "Science stories", sociales: "Social studies stories" },
      cuentosIndice: "index-en.html",
      errorCuentos: "The stories could not be loaded right now.",
      cifras: ["activities", "grades with materials", "subjects"],
      teatro: { cartel: "See the poster for the play: ", pronto: "In preparation", listo: "Ready", idiomas: "In English and Spanish",
                guionEs: "Script in Spanish", guionEn: "Script in English", guia: "Production guide", historia: "Historical guide for teachers", soloEs: " (in Spanish)",
                traera: "Coming: script, character cards, costumes, sets and a teacher guide." }
    }
  }[L];

  var GRADOS = [
    { id: "prek", ancla: "prek", es: "Prekínder",    en: "Pre-K",        es2: "4 a 5 años", en2: "Ages 4–5" },
    { id: "k",    ancla: "k",    es: "Kindergarten", en: "Kindergarten", es2: "5 a 6 años", en2: "Ages 5–6" },
    { id: "1",    ancla: "g1",   es: "1.er grado",   en: "Grade 1" },
    { id: "2",    ancla: "g2",   es: "2.º grado",    en: "Grade 2" },
    { id: "3",    ancla: "g3",   es: "3.er grado",   en: "Grade 3" },
    { id: "4",    ancla: "g4",   es: "4.º grado",    en: "Grade 4" },
    { id: "5",    ancla: "g5",   es: "5.º grado",    en: "Grade 5" },
    { id: "6",    ancla: "g6",   es: "6.º grado",    en: "Grade 6" }
  ];
  var MATERIAS = [
    { id: "matematicas", es: "Matemáticas",        en: "Math",
      es2: "Números, figuras y problemas", en2: "Numbers, shapes and problems" },
    { id: "lectura",     es: "Lectura y escritura", en: "Reading & writing",
      es2: "Letras, sonidos y palabras",   en2: "Letters, sounds and words" },
    { id: "ciencias",    es: "Ciencias",           en: "Science",
      es2: "Explorar el mundo natural",    en2: "Exploring the natural world" },
    { id: "sociales",    es: "Estudios sociales",  en: "Social studies",
      es2: "Comunidad, historia y lugares", en2: "Community, history and places" }
  ];

  /* Íconos decorativos: el texto de al lado ya dice la materia */
  var ICONOS = {
    matematicas: '<circle cx="26" cy="26" r="25" fill="#F8C85F"/><path d="M14 17h10M19 12v10M30 14l8 8M38 14l-8 8M13 35h11M30 32h9M30 38h9" stroke="#194F5A" stroke-width="3.2" stroke-linecap="round" fill="none"/>',
    lectura: '<circle cx="26" cy="26" r="25" fill="#EF9275"/><path d="M26 17c-4-3-9-3-14-2v20c5-1 10-1 14 2 4-3 9-3 14-2V15c-5-1-10-1-14 2zM26 17v20" stroke="#194F5A" stroke-width="3" stroke-linejoin="round" fill="#fff"/>',
    ciencias: '<circle cx="26" cy="26" r="25" fill="#6DCEC5"/><path d="M21 12h10M23 12v10l-8 14a3 3 0 0 0 3 4h16a3 3 0 0 0 3-4l-8-14V12" stroke="#194F5A" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" fill="#fff"/><circle cx="24" cy="33" r="2.4" fill="#45A6AD"/><circle cx="30" cy="30" r="1.8" fill="#45A6AD"/>',
    sociales: '<circle cx="26" cy="26" r="25" fill="#A9D3D6"/><path d="M12 25 26 14l14 11M16 22v16h20V22" stroke="#194F5A" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" fill="#fff"/><path d="M23 38v-8h6v8" stroke="#194F5A" stroke-width="3" fill="#F8C85F"/>'
  };
  function icono(m) {
    return '<svg class="icono" viewBox="0 0 52 52" aria-hidden="true" focusable="false">' + ICONOS[m] + "</svg>";
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function nombre(o) { return o[L]; }
  function gradoPorId(id) { for (var i = 0; i < GRADOS.length; i++) if (GRADOS[i].id === id) return GRADOS[i]; }

  /* ---------------- armar la lista completa de series ---------------- */
  function urlLeccion(l) {
    if (l.url) return l.url;
    if (l.es_url || l.en_url) return l[L + "_url"] || l[OTRO + "_url"];
    return P + l.archivo + "?lang=" + L;
  }

  function seriesDeCuentos() {
    var cat = window.CATALOGO || [];
    var grupos = {};
    cat.forEach(function (c) {
      var g = c.grado === 0 ? "k" : String(c.grado);
      var k = g + "|" + c.area;
      (grupos[k] = grupos[k] || []).push(c);
    });
    return Object.keys(grupos).map(function (k) {
      var g = k.split("|")[0], area = k.split("|")[1];
      var lista = grupos[k].sort(function (a, b) { return a.orden - b.orden; });
      var libro = (DATOS.libros || []).filter(function (b) { return b.grado === g && b.area === area; })[0];
      var base = DATOS.cuentos_base;
      var s = {
        grado: g, materia: area, tipo: "cuentos", lang: L,
        url: libro ? base + libro[L] : base + T.cuentosIndice,
        titulo: T.libroTit[area] || area,
        lecciones: lista.map(function (c) {
          var v = c[L] || c[OTRO];
          return { titulo: v.titulo, url: base + v.archivo, lang: c[L] ? L : OTRO };
        })
      };
      return s;
    });
  }

  function normalizar() {
    /* En la versión en inglés no se muestran las series que son solo en español
       (la lectura en español); en la versión en español se muestran todas */
    var todas = DATOS.series.filter(function (s) {
      return !(s.solo === "es" && L === "en");
    }).map(function (s) {
      var v = s[L], lang = L, aviso = "";
      if (!v) { v = s[OTRO]; lang = OTRO; aviso = T.soloOtro; }
      if (s.solo === "es" && L === "en") aviso = T.soloEsEnEn;
      if (s.solo === "en" && L === "es") aviso = T.soloEnEnEs;
      if (s.aviso && s.aviso[L] !== undefined) aviso = s.aviso[L];   // aviso propio de la serie
      return {
        grado: s.grado, materia: s.materia, tipo: s.tipo,
        titulo: v.titulo, url: v.url, lang: lang, aviso: aviso,
        lecciones: (s.lecciones || []).map(function (l) {
          return { titulo: l[L] || l[OTRO], url: urlLeccion(l) };
        })
      };
    });
    return todas.concat(seriesDeCuentos());
  }

  /* ---------------- tarjetas ---------------- */
  function tarjeta(s, nivel) {
    var h = "h" + nivel;
    var langAttr = s.lang !== L ? ' lang="' + s.lang + '"' : "";
    var html = '<article class="serie">' +
      '<span class="tipo">' + esc(T.tipo[s.tipo] || s.tipo) + "</span>" +
      "<" + h + '><a href="' + esc(s.url) + '"' + langAttr + ">" + esc(s.titulo) + "</a></" + h + ">";
    if (s.aviso) html += '<p class="aviso">' + esc(s.aviso) + "</p>";
    if (s.lecciones.length) {
      var n = s.tipo === "cuentos" ? T.cuentos(s.lecciones.length) : T.lecciones(s.lecciones.length);
      html += "<details><summary>" + esc(n) + "</summary><ol>";
      s.lecciones.forEach(function (l) {
        var la = l.lang && l.lang !== L ? ' lang="' + l.lang + '"' : "";
        html += '<li><a href="' + esc(l.url) + '"' + la + ">" + esc(l.titulo) + "</a></li>";
      });
      html += "</ol></details>";
      if (s.tipo === "cuentos" && /libro|book/.test(s.url)) {
        html += '<p class="arriba"><a href="' + esc(s.url) + '">' + esc(T.abrirLibro) + "</a></p>";
      }
    }
    return html + "</article>";
  }

  function cuenta(series) {
    return series.reduce(function (t, s) { return t + Math.max(1, s.lecciones.length); }, 0);
  }

  /* ---------------- páginas ---------------- */
  function paginaInicio(todas) {
    var gradosCon = GRADOS.filter(function (g) { return todas.some(function (s) { return s.grado === g.id; }); });
    var ul = document.getElementById("lista-grados");
    if (ul) {
      ul.innerHTML = GRADOS.map(function (g) {
        var n = cuenta(todas.filter(function (s) { return s.grado === g.id; }));
        if (!n) return "<li><span>" + esc(nombre(g)) + "<small>" + esc(T.proximamente) + "</small></span></li>";
        return '<li><a href="' + T.grados + "#" + g.ancla + '">' + esc(nombre(g)) +
               "<small>" + esc(T.lecciones(n)) + "</small></a></li>";
      }).join("");
    }
    var um = document.getElementById("lista-materias");
    if (um) {
      um.innerHTML = MATERIAS.map(function (m) {
        return '<li><a href="' + T.materias + "#" + m.id + '">' + icono(m.id) +
               "<span>" + esc(nombre(m)) + "<small>" + esc(m[L + "2"]) + "</small></span></a></li>";
      }).join("");
    }
    var c = document.getElementById("cifras");
    if (c) {
      c.innerHTML = "<li><b>" + cuenta(todas) + "</b> " + T.cifras[0] + "</li>" +
                    "<li><b>" + gradosCon.length + "</b> " + T.cifras[1] + "</li>" +
                    "<li><b>" + MATERIAS.length + "</b> " + T.cifras[2] + "</li>";
    }
  }

  function anclas(items) {
    return '<nav aria-label="' + (L === "es" ? "Ir a" : "Go to") + '"><ul class="anclas">' +
      items.map(function (i) { return '<li><a href="#' + i.ancla + '">' + esc(i.texto) + "</a></li>"; }).join("") +
      "</ul></nav>";
  }

  /* ---------- Acordeón de «Por grado» y «Por materia» ----------
     Cada grado (o materia) es una tarjeta cerrada con su Lumi. Al abrir una,
     se cierra la que estaba abierta: la página nunca se hace larga.
     Lumi de cada tarjeta: lumi-grado-<id>.png o lumi-materia-<id>.png; si
     todavía no existe, se usa el Lumi de siempre (lápiz hasta 2.º, libreta
     de 3.º a 6.º). */
  function lumiDe(tipo, id) {
    var respaldo = (tipo === "grado" && /^[3-6]$/.test(id)) ? "lumi-explora.jpg" : "lumi-saluda.jpg";
    return '<span class="lumi-mini" aria-hidden="true"><img src="lumi-' + tipo + "-" + id + '.png" alt="" ' +
           'onerror="this.onerror=null;this.src=\'' + respaldo + '\'"></span>';
  }
  function tarjetaAcordeon(id, tipo, idLumi, titulo, detalle, color, cuerpo) {
    return '<details class="seccion acordeon" id="' + id + '" name="' + tipo + 's" style="--anillo:' + color + '">' +
      '<summary><span class="lumi-anillo">' + lumiDe(tipo, idLumi) + '</span>' +
      '<span class="acordeon-texto"><h2 id="t-' + id + '">' + esc(titulo) + '</h2>' +
      (detalle ? '<small>' + esc(detalle) + '</small>' : "") + '</span>' +
      '<span class="acordeon-flecha" aria-hidden="true"></span></summary>' +
      '<div class="acordeon-cuerpo">' + cuerpo +
      '<p class="arriba"><a href="#' + id + '" class="cerrar-acordeon">' + esc(T.cerrar) + "</a></p></div></details>";
  }
  var COLORES = ["var(--men)", "var(--ama)", "var(--cor)", "var(--tur)"];

  function paginaGrados(todas, cont) {
    var html = "";
    GRADOS.forEach(function (g, k) {
      var delGrado = todas.filter(function (s) { return s.grado === g.id; });
      var n = cuenta(delGrado);
      var detalle = [g[L + "2"], n ? T.lecciones(n) : T.proximamente].filter(Boolean).join(" · ");
      var cuerpo = "";
      if (!delGrado.length) {
        var foto = /^[3-6]$/.test(g.id) ? "lumi-explora.jpg" : "lumi-saluda.jpg";
        cuerpo += '<p class="vacio"><img src="' + foto + '" alt="">' + esc(T.vacio) + "</p>";
      } else {
        MATERIAS.forEach(function (m) {
          var s = delGrado.filter(function (x) { return x.materia === m.id; });
          if (!s.length) return;
          cuerpo += '<div class="sub"><h3>' + icono(m.id) + esc(nombre(m)) + '</h3><div class="series">' +
                    s.map(function (x) { return tarjeta(x, 4); }).join("") + "</div></div>";
        });
        (DATOS.guias || []).filter(function (x) { return x.grado === g.id; }).forEach(function (x) {
          cuerpo += '<div class="sub guia-grado"><h3>' + esc(T.guiaTit) + '</h3><p><a href="' + esc(x.url) + '" hreflang="en">' +
                    '<span aria-hidden="true">🍎 </span>' + esc(T.guia) + "</a></p></div>";
        });
      }
      html += tarjetaAcordeon(g.ancla, "grado", g.id, nombre(g), detalle, COLORES[k % 4], cuerpo);
    });
    cont.innerHTML = html;
  }

  function paginaMaterias(todas, cont) {
    var html = "";
    MATERIAS.forEach(function (m, k) {
      var deMateria = todas.filter(function (s) { return s.materia === m.id; });
      var cuerpo = "", faltan = [];
      GRADOS.forEach(function (g) {
        var s = deMateria.filter(function (x) { return x.grado === g.id; });
        /* Prekínder no tiene ciencias ni estudios sociales: no es algo que falte */
        if (!s.length) { if (!(g.id === "prek" && (m.id === "ciencias" || m.id === "sociales"))) faltan.push(nombre(g)); return; }
        var guiaM = (m.id === "ciencias" || m.id === "sociales") ?
          (DATOS.guias || []).filter(function (x) { return x.grado === g.id; }) : [];
        cuerpo += '<div class="sub" id="' + m.id + "-" + g.ancla + '"><h3>' + esc(nombre(g)) + '</h3><div class="series">' +
                  s.map(function (x) { return tarjeta(x, 4); }).join("") + "</div>" +
                  guiaM.map(function (x) {
                    return '<p class="guia-grado"><a href="' + esc(x.url) + '" hreflang="en"><span aria-hidden="true">🍎 </span>' + esc(T.guia) + "</a></p>";
                  }).join("") + "</div>";
      });
      if (faltan.length) cuerpo += '<p class="vacio">' + esc(T.pronto + faltan.join(", ")) + ".</p>";
      var detalle = m[L + "2"] + " · " + T.lecciones(cuenta(deMateria));
      html += tarjetaAcordeon(m.id, "materia", m.id, nombre(m), detalle, COLORES[(k + 1) % 4], cuerpo);
    });
    cont.innerHTML = html;
  }

  /* Abrir la tarjeta que pide el # (#g3, #ciencias, #ciencias-g5…) y llevar al niño a ella */
  function abrirPorAncla() {
    if (!location.hash) return;
    var dest = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (!dest) return;
    var det = dest.matches && dest.matches("details.acordeon") ? dest : (dest.closest && dest.closest("details.acordeon"));
    if (det) det.open = true;
    setTimeout(function () { dest.scrollIntoView({ block: "start" }); }, 30);
  }
  function activarAcordeon(cont) {
    var tarjetas = Array.prototype.slice.call(cont.querySelectorAll("details.acordeon"));
    tarjetas.forEach(function (d) {
      d.addEventListener("toggle", function () {
        if (!d.open) return;
        /* una sola abierta (por si el navegador no admite name="") */
        tarjetas.forEach(function (o) { if (o !== d && o.open) o.open = false; });
        /* que se vea el título de la tarjeta que se abrió */
        requestAnimationFrame(function () {
          var r = d.getBoundingClientRect(), cab = document.querySelector(".cabecera");
          var tope = cab ? cab.getBoundingClientRect().bottom : 0;
          if (r.top < tope || r.top > window.innerHeight * 0.7) d.scrollIntoView({ block: "start" });
        });
        if (history.replaceState) history.replaceState(null, "", "#" + d.id);
      });
    });
    cont.addEventListener("click", function (e) {
      var a = e.target.closest && e.target.closest(".cerrar-acordeon");
      if (!a) return;
      e.preventDefault();
      var d = a.closest("details.acordeon");
      d.open = false;
      d.scrollIntoView({ block: "start" });
      d.querySelector("summary").focus({ preventScroll: true });
    });
    window.addEventListener("hashchange", abrirPorAncla);
  }

  /* Teatro: tarjetas de las obras (catalogo.js → obras) */
  function paginaTeatro(cont) {
    var t = T.teatro;
    cont.innerHTML = (DATOS.obras || []).map(function (o) {
      var v = o[L] || o[OTRO], lista = o.estado !== "pronto";
      var html = '<article class="serie obra" id="obra-' + esc(o.id) + '">';
      if (o.img) {
        var foto = '<img src="' + esc(o.img) + '" alt="' + esc(t.cartel + v.titulo) + '" width="640" height="480" loading="lazy">';
        html += o.cartel ? '<a class="miniatura" href="' + esc(o.cartel + "-" + L + ".html") + '">' + foto + "</a>"
                         : '<span class="miniatura">' + foto.replace(/alt="[^"]*"/, 'alt=""') + "</span>";
      }
      html +=
        '<span class="tipo">' + esc(lista ? t.listo : t.pronto) + "</span>" +
        "<h3" + (o[L] ? "" : ' lang="' + OTRO + '"') + ">" + esc(v.titulo) + "</h3>" +
        '<p class="otro-titulo" lang="' + OTRO + '">' + esc(o[OTRO].titulo) + "</p>" +
        "<p>" + esc(v.desc) + "</p>" +
        '<p class="aviso">' + esc(v.nota || t.idiomas) + "</p>";
      if (lista) {
        var enl = [];
        if (o.es_url) enl.push('<li><a href="' + esc(o.es_url) + '" lang="es">' + esc(t.guionEs) + "</a></li>");
        if (o.en_url) enl.push('<li><a href="' + esc(o.en_url) + '" lang="en">' + esc(t.guionEn) + "</a></li>");
        [["guia", "guia_en"], ["historia", "historia_en"]].forEach(function (k) {
          if (!o[k[0]]) return;
          var enIngles = L === "en" && o[k[1]];
          var url = enIngles ? o[k[1]] : o[k[0]];
          var soloEs = L === "en" && !o[k[1]];
          enl.push('<li><a href="' + esc(url) + '"' + (soloEs ? ' lang="es"' : "") + ">" + esc(t[k[0]] + (soloEs ? t.soloEs : "")) + "</a></li>");
        });
        html += "<ul>" + enl.join("") + "</ul>";
      } else {
        html += '<p class="nota-obra">' + esc(t.traera) + "</p>";
      }
      return html + "</article>";
    }).join("");
  }

  /* El cambio de idioma conserva la sección en la que está el niño,
     tanto si llegó por un enlace (#ancla) como si bajó con la rueda */
  function seccionVisible() {
    var cab = document.querySelector(".cabecera");
    var limite = (cab ? cab.getBoundingClientRect().bottom : 0) + 40;
    var abierta = document.querySelector("details.acordeon[open]");
    if (abierta) return abierta.id;
    var actual = "";
    document.querySelectorAll(".seccion:not(.acordeon)").forEach(function (s) {
      if (s.getBoundingClientRect().top <= limite) actual = s.id;
    });
    return actual;
  }
  function enlaceIdioma() {
    var a = document.querySelector(".idioma a");
    if (!a) return;
    var base = a.getAttribute("href").split("#")[0];
    function poner() {
      var id = seccionVisible();
      a.setAttribute("href", base + (id ? "#" + id : location.hash));
    }
    poner();
    window.addEventListener("hashchange", poner);
    document.addEventListener("toggle", poner, true);
    window.addEventListener("scroll", poner, { passive: true });
    a.addEventListener("focus", poner);
  }

  function armar() {
    var todas = normalizar();
    var pag = document.body.getAttribute("data-pagina");
    var cont = document.getElementById("catalogo");
    if (pag === "teatro") paginaTeatro(document.getElementById("lista-obras"));
    if (pag === "inicio") paginaInicio(todas);
    if (pag === "grados") paginaGrados(todas, cont);
    if (pag === "materias") paginaMaterias(todas, cont);
    if (!window.CATALOGO && cont) {
      cont.insertAdjacentHTML("afterbegin", '<p class="vacio" role="status">' + esc(T.errorCuentos) + "</p>");
    }
    /* Si se llegó con #ancla, ir a ella ya armada la página */
    if (cont && (pag === "grados" || pag === "materias")) { activarAcordeon(cont); abrirPorAncla(); }
    else if (location.hash) {
      var dest = document.getElementById(location.hash.slice(1));
      if (dest) dest.scrollIntoView();
    }
  }

  enlaceIdioma();
  var sc = document.createElement("script");
  sc.src = DATOS.cuentos_catalogo;
  sc.onload = armar;
  sc.onerror = armar;
  document.head.appendChild(sc);
})();
