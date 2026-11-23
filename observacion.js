/* ==================================================================
   Lumi · Hoja de observación para el docente
   ------------------------------------------------------------------
   Arma, a partir de catalogo.js (y del catálogo de cuentos), una hoja
   para imprimir y anotar a mano cómo trabaja cada niño:
     - Para el grupo: una serie de actividades; filas = estudiantes,
       columnas = actividades.
     - Para un estudiante: todas las actividades del grado; una fila
       por actividad.
   Mentes curiosas no aparece a propósito: son juegos, no se registran.
   Los nombres que se escriban NO se guardan ni se envían: se borran al
   cerrar la página.
   Licencia CC BY-NC-SA 4.0 · José M. Fernández
   ================================================================== */
(function () {
  "use strict";

  var L = (document.documentElement.lang || "es").slice(0, 2) === "en" ? "en" : "es";
  var OTRO = L === "es" ? "en" : "es";
  var DATOS = window.LUMI;
  var $ = function (id) { return document.getElementById(id); };

  var T = {
    es: {
      grados: { prek: "Prekínder", k: "Kindergarten", 1: "1.er grado", 2: "2.º grado", 3: "3.er grado", 4: "4.º grado", 5: "5.º grado", 6: "6.º grado", 7: "7.º grado", 8: "8.º grado" },
      materias: { matematicas: "Matemáticas", lectura: "Lectura y escritura", ciencias: "Ciencias", sociales: "Estudios sociales" },
      libroTit: { ciencias: "Cuentos de ciencias", sociales: "Cuentos de estudios sociales" },
      soloEs: " (en español)", soloEn: " (en inglés)",
      estudiante: "Estudiante", actividad: "Actividad", fecha: "Fecha", logro: "¿Cómo lo hizo?",
      pista: "¿Qué pista le ayudó?", siguiente: "Próximo paso", notas: "Notas",
      cap1: function (g, s) { return "Hoja de observación del grupo · " + g + " · " + s; },
      cap2: function (g) { return "Hoja de observación de un estudiante · " + g; },
      nombre: "Nombre del estudiante:", docente: "Docente:", periodo: "Fechas:",
      sinSeries: "Este grado todavía no tiene actividades para observar.",
      error: "No se pudieron cargar los cuentos en este momento; la hoja muestra solo los interactivos.",
      unJuego: "(juego)"
    },
    en: {
      grados: { prek: "Pre-K", k: "Kindergarten", 1: "Grade 1", 2: "Grade 2", 3: "Grade 3", 4: "Grade 4", 5: "Grade 5", 6: "Grade 6", 7: "Grade 7", 8: "Grade 8" },
      materias: { matematicas: "Math", lectura: "Reading & writing", ciencias: "Science", sociales: "Social studies" },
      libroTit: { ciencias: "Science stories", sociales: "Social studies stories" },
      soloEs: " (in Spanish)", soloEn: " (in English)",
      estudiante: "Student", actividad: "Activity", fecha: "Date", logro: "How did it go?",
      pista: "Which hint helped?", siguiente: "Next step", notas: "Notes",
      cap1: function (g, s) { return "Class observation sheet · " + g + " · " + s; },
      cap2: function (g) { return "Student observation sheet · " + g; },
      nombre: "Student's name:", docente: "Teacher:", periodo: "Dates:",
      sinSeries: "This grade does not have activities to observe yet.",
      error: "The stories could not be loaded right now; the sheet shows only the interactives.",
      unJuego: "(game)"
    }
  }[L];

  var ORDEN_GRADOS = ["prek", "k", "1", "2", "3", "4", "5", "6", "7", "8"];
  var ORDEN_MATERIAS = ["matematicas", "lectura", "ciencias", "sociales"];

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  /* ---------- series del grado (sin Mentes curiosas) ---------- */
  function series() {
    var lista = DATOS.series.filter(function (s) { return s.materia !== "mentes"; }).map(function (s) {
      var v = s[L] || s[OTRO];
      var titulo = v.titulo;
      if (s.solo === "es" && L === "en" && !/spanish/i.test(titulo)) titulo += T.soloEs;
      if (s.solo === "en" && L === "es" && !/ingl/i.test(titulo)) titulo += T.soloEn;
      var lec = (s.lecciones || []).map(function (l) { return l[L] || l[OTRO]; });
      if (!lec.length) lec = [v.titulo + " " + T.unJuego];
      return { grado: s.grado, materia: s.materia, titulo: titulo, lecciones: lec };
    });
    /* Cuentos (catálogo del repositorio cuentos-educativos) */
    var grupos = {};
    (window.CATALOGO || []).forEach(function (c) {
      var g = c.grado === 0 ? "k" : String(c.grado);
      (grupos[g + "|" + c.area] = grupos[g + "|" + c.area] || []).push(c);
    });
    Object.keys(grupos).forEach(function (k) {
      var g = k.split("|")[0], area = k.split("|")[1];
      var cs = grupos[k].sort(function (a, b) { return a.orden - b.orden; });
      lista.push({
        grado: g, materia: area, titulo: T.libroTit[area] || area,
        lecciones: cs.map(function (c) { return (c[L] || c[OTRO]).titulo; })
      });
    });
    return lista.sort(function (a, b) {
      return ORDEN_MATERIAS.indexOf(a.materia) - ORDEN_MATERIAS.indexOf(b.materia);
    });
  }

  var TODAS = [];
  function delGrado(g) { return TODAS.filter(function (s) { return s.grado === g; }); }

  /* ---------- controles ---------- */
  function llenarGrados() {
    $("obs-grado").innerHTML = ORDEN_GRADOS.filter(function (g) { return delGrado(g).length; }).map(function (g) {
      return '<option value="' + g + '">' + esc(T.grados[g]) + "</option>";
    }).join("");
  }
  function llenarSeries() {
    var s = delGrado($("obs-grado").value);
    $("obs-serie").innerHTML = s.map(function (x, i) {
      return '<option value="' + i + '">' + esc(T.materias[x.materia] + " · " + x.titulo + " (" + x.lecciones.length + ")") + "</option>";
    }).join("");
  }
  function formato() { return $("obs-individual").checked ? "individual" : "grupo"; }

  function nombres() {
    return $("obs-nombres").value.split(/\n/).map(function (n) { return n.trim(); }).filter(Boolean);
  }

  /* ---------- la hoja ---------- */
  function cabeceraHoja() {
    return '<div class="hoja-datos"><span>' + esc(T.docente) + ' <span class="raya"></span></span>' +
           "<span>" + esc(T.periodo) + ' <span class="raya"></span></span></div>';
  }

  function hojaGrupo(g, s) {
    var ns = nombres();
    var filas = Math.max(ns.length, parseInt($("obs-filas").value, 10) || 0);
    var h = cabeceraHoja() + '<table class="hoja hoja-grupo"><caption>' + esc(T.cap1(T.grados[g], s.titulo)) + "</caption><thead><tr>" +
            '<th scope="col" class="col-nombre">' + esc(T.estudiante) + "</th>";
    s.lecciones.forEach(function (l, i) {
      h += '<th scope="col"><span class="num">' + (i + 1) + ".</span> " + esc(l) + "</th>";
    });
    h += '<th scope="col" class="col-notas">' + esc(T.notas) + "</th></tr></thead><tbody>";
    for (var i = 0; i < filas; i++) {
      h += '<tr><th scope="row">' + esc(ns[i] || "") + "</th>";
      for (var j = 0; j < s.lecciones.length; j++) h += "<td></td>";
      h += "<td></td></tr>";
    }
    return h + "</tbody></table>";
  }

  function hojaIndividual(g) {
    var ns = nombres();
    var quienes = ns.length ? ns : [""];
    return quienes.map(function (n) {
      var h = '<section class="hoja-alumno">' +
        '<p class="hoja-nombre">' + esc(T.nombre) + " " + (n ? "<strong>" + esc(n) + "</strong>" : '<span class="raya larga"></span>') + "</p>" +
        cabeceraHoja() +
        '<table class="hoja hoja-individual"><caption>' + esc(T.cap2(T.grados[g])) + "</caption><thead><tr>" +
        '<th scope="col">' + esc(T.actividad) + '</th><th scope="col" class="col-fecha">' + esc(T.fecha) + "</th>" +
        '<th scope="col" class="col-logro">' + esc(T.logro) + '</th><th scope="col">' + esc(T.pista) + "</th>" +
        '<th scope="col">' + esc(T.siguiente) + "</th></tr></thead>";
      delGrado(g).forEach(function (s) {
        h += '<tbody><tr class="fila-serie"><th scope="rowgroup" colspan="5">' + esc(T.materias[s.materia] + " · " + s.titulo) + "</th></tr>";
        s.lecciones.forEach(function (l) {
          h += '<tr><th scope="row">' + esc(l) + '</th><td></td><td class="simbolos" aria-hidden="true">★ &nbsp; ✓ &nbsp; ○</td><td></td><td></td></tr>';
        });
        h += "</tbody>";
      });
      return h + "</table></section>";
    }).join("");
  }

  function armarHoja() {
    var g = $("obs-grado").value;
    var cont = $("obs-hoja");
    if (!g) { cont.innerHTML = '<p class="vacio">' + esc(T.sinSeries) + "</p>"; return; }
    var ind = formato() === "individual";
    $("obs-serie-caja").hidden = ind;
    $("obs-filas-caja").hidden = ind;
    cont.innerHTML = ind ? hojaIndividual(g) : hojaGrupo(g, delGrado(g)[parseInt($("obs-serie").value, 10) || 0]);
    /* Impresión: el grupo va en horizontal; un estudiante, en vertical */
    $("obs-pagina").textContent = "@page{size:" + (ind ? "portrait" : "landscape") + ";margin:12mm}";
    /* Conservar grado y formato al cambiar de idioma */
    var a = document.querySelector(".idioma a");
    var q = "?grado=" + g + (ind ? "&formato=individual" : "");
    if (a) a.setAttribute("href", a.getAttribute("href").split("?")[0] + q);
    try { history.replaceState(null, "", q); } catch (e) {}
  }

  function iniciar() {
    TODAS = series();
    if (!window.CATALOGO) $("obs-aviso").textContent = T.error;
    llenarGrados();
    try {
      var q = new URLSearchParams(location.search);
      if (q.get("grado") && delGrado(q.get("grado")).length) $("obs-grado").value = q.get("grado");
      if (q.get("formato") === "individual") $("obs-individual").checked = true;
    } catch (e) {}
    llenarSeries();
    $("obs-grado").addEventListener("change", function () { llenarSeries(); armarHoja(); });
    ["obs-serie", "obs-filas", "obs-grupo", "obs-individual"].forEach(function (id) {
      $(id).addEventListener("change", armarHoja);
    });
    $("obs-nombres").addEventListener("input", armarHoja);
    $("obs-imprimir").addEventListener("click", function () { window.print(); });
    armarHoja();
  }

  var sc = document.createElement("script");
  sc.src = DATOS.cuentos_catalogo;
  sc.onload = iniciar;
  sc.onerror = iniciar;
  document.head.appendChild(sc);
})();
