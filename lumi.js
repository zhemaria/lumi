/* ==================================================================
   Lumi · Lógica del portal
   ------------------------------------------------------------------
   Lee catalogo.js (series de interactivos y juegos) y el catálogo
   de cuentos del repositorio cuentos-educativos, y arma:
     - inicio  (index-es.html / index.html, que es la portada en inglés)
     - grados  (grados.html / grados-en.html)   → una sección por grado
     - materias(materias.html / materias-en.html) → una sección por materia
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
      grados: "grados.html", materias: "materias.html",
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
      abrirLibro: "Abrir el libro completo",
      libroTit: { ciencias: "Cuentos de ciencias", sociales: "Cuentos de estudios sociales" },
      cuentosIndice: "index.html",
      errorCuentos: "No se pudieron cargar los cuentos en este momento.",
      cifras: ["actividades", "grados con material", "materias"]
    },
    en: {
      grados: "grados-en.html", materias: "materias-en.html",
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
      abrirLibro: "Open the whole book",
      libroTit: { ciencias: "Science stories", sociales: "Social studies stories" },
      cuentosIndice: "index-en.html",
      errorCuentos: "The stories could not be loaded right now.",
      cifras: ["activities", "grades with materials", "subjects"]
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
    var todas = DATOS.series.map(function (s) {
      var v = s[L], lang = L, aviso = "";
      if (!v) { v = s[OTRO]; lang = OTRO; aviso = T.soloOtro; }
      if (s.solo === "es" && L === "en") aviso = T.soloEsEnEn;
      if (s.solo === "en" && L === "es") aviso = T.soloEnEnEs;
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

  function paginaGrados(todas, cont) {
    var html = anclas(GRADOS.map(function (g) { return { ancla: g.ancla, texto: nombre(g) }; }));
    GRADOS.forEach(function (g) {
      var delGrado = todas.filter(function (s) { return s.grado === g.id; });
      html += '<section class="seccion" id="' + g.ancla + '" aria-labelledby="t-' + g.ancla + '">' +
              '<h2 id="t-' + g.ancla + '">' + esc(nombre(g)) +
              (g[L + "2"] ? ' <small style="font-weight:400;font-size:1rem">· ' + esc(g[L + "2"]) + "</small>" : "") + "</h2>";
      if (!delGrado.length) {
        /* Lumi crece con el niño: lápiz hasta 2.º, libreta de 3.º a 6.º */
        var foto = /^[3-6]$/.test(g.id) ? "lumi-explora.jpg" : "lumi-saluda.jpg";
        html += '<p class="vacio"><img src="' + foto + '" alt="">' + esc(T.vacio) + "</p>";
      } else {
        MATERIAS.forEach(function (m) {
          var s = delGrado.filter(function (x) { return x.materia === m.id; });
          if (!s.length) return;
          html += '<div class="sub"><h3>' + icono(m.id) + esc(nombre(m)) + '</h3><div class="series">' +
                  s.map(function (x) { return tarjeta(x, 4); }).join("") + "</div></div>";
        });
      }
      html += '<p class="arriba"><a href="#contenido">' + esc(T.arriba) + "</a></p></section>";
    });
    cont.innerHTML = html;
  }

  function paginaMaterias(todas, cont) {
    var html = anclas(MATERIAS.map(function (m) { return { ancla: m.id, texto: nombre(m) }; }));
    MATERIAS.forEach(function (m) {
      var deMateria = todas.filter(function (s) { return s.materia === m.id; });
      html += '<section class="seccion" id="' + m.id + '" aria-labelledby="t-' + m.id + '">' +
              '<h2 id="t-' + m.id + '">' + icono(m.id) + esc(nombre(m)) + "</h2>";
      var faltan = [];
      GRADOS.forEach(function (g) {
        var s = deMateria.filter(function (x) { return x.grado === g.id; });
        if (!s.length) { faltan.push(nombre(g)); return; }
        html += '<div class="sub" id="' + m.id + "-" + g.ancla + '"><h3>' + esc(nombre(g)) + '</h3><div class="series">' +
                s.map(function (x) { return tarjeta(x, 4); }).join("") + "</div></div>";
      });
      if (faltan.length) html += '<p class="vacio">' + esc(T.pronto + faltan.join(", ")) + ".</p>";
      html += '<p class="arriba"><a href="#contenido">' + esc(T.arriba) + "</a></p></section>";
    });
    cont.innerHTML = html;
  }

  /* El cambio de idioma conserva la sección en la que está el niño,
     tanto si llegó por un enlace (#ancla) como si bajó con la rueda */
  function seccionVisible() {
    var cab = document.querySelector(".cabecera");
    var limite = (cab ? cab.getBoundingClientRect().bottom : 0) + 40;
    var actual = "";
    document.querySelectorAll(".seccion").forEach(function (s) {
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
    window.addEventListener("scroll", poner, { passive: true });
    a.addEventListener("focus", poner);
  }

  function armar() {
    var todas = normalizar();
    var pag = document.body.getAttribute("data-pagina");
    var cont = document.getElementById("catalogo");
    if (pag === "inicio") paginaInicio(todas);
    if (pag === "grados") paginaGrados(todas, cont);
    if (pag === "materias") paginaMaterias(todas, cont);
    if (!window.CATALOGO && cont) {
      cont.insertAdjacentHTML("afterbegin", '<p class="vacio" role="status">' + esc(T.errorCuentos) + "</p>");
    }
    /* Si se llegó con #ancla, ir a ella ya armada la página */
    if (location.hash) {
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
