/* ==================================================================
   Lumi · Catálogo de actividades
   ------------------------------------------------------------------
   Una entrada por SERIE (un conjunto de actividades con su página
   de inicio). Cada serie tiene un grado, una materia y, dentro,
   sus lecciones.

   Grados:   "prek", "k", "1", "2", "3", "4", "5", "6"
   Materias: "matematicas", "lectura", "ciencias", "sociales"

   Para cada idioma ("es", "en") se da el título y la dirección.
   Si una serie existe en un solo idioma, se deja el otro vacío
   (null); el portal lo indica al estudiante.

   Los CUENTOS no se escriben aquí: el portal los lee directamente
   del catálogo del repositorio cuentos-educativos, así que cada
   cuento nuevo aparece solo. Aquí solo se anotan sus LIBROS.

   Licencia CC BY-NC-SA 4.0 · José M. Fernández
   ================================================================== */

var P = "https://zhemaria.github.io/primaria/";
var C = "https://zhemaria.github.io/cuentos-educativos/";

window.LUMI = {

  /* Catálogo de cuentos (se carga desde el otro repositorio) */
  cuentos_catalogo: C + "catalogo.js",
  cuentos_base: C,

  /* Libros de cuentos ya terminados: grado + área → archivos */
  libros: [
    { grado: "k", area: "ciencias", es: "libro-kinder-ciencias.html", en: "book-kindergarten-science.html" },
    { grado: "k", area: "sociales", es: "libro-kinder-sociales.html", en: "book-kindergarten-social-studies.html" },
    { grado: "2", area: "ciencias", es: "libro-2do-ciencias.html",   en: "book-grade2-science.html" },
    { grado: "2", area: "sociales", es: "libro-2do-sociales.html",   en: "book-grade2-social-studies.html" }
  ],

  series: [

    /* ---------------- PREKÍNDER ---------------- */
    {
      grado: "prek", materia: "matematicas", tipo: "interactivo",
      es: { titulo: "Matemáticas para prekínder", url: P + "prekinder/?lang=es" },
      en: { titulo: "Pre-K mathematics",          url: P + "prekinder/?lang=en" },
      lecciones: [
        { es: "Números y conteo",       en: "Numbers and counting",    archivo: "prekinder/prek-01-numeros-conteo.html" },
        { es: "Figuras y posición",     en: "Shapes and position",     archivo: "prekinder/prek-02-figuras-posicion.html" },
        { es: "Comparar cantidades",    en: "Comparing amounts",       archivo: "prekinder/prek-03-comparar.html" },
        { es: "Medir y comparar",       en: "Measuring and comparing", archivo: "prekinder/prek-04-medir.html" },
        { es: "Patrones y clasificar",  en: "Patterns and sorting",    archivo: "prekinder/prek-05-patrones.html" },
        { es: "Datos y predicciones",   en: "Data and predictions",    archivo: "prekinder/prek-06-datos.html" }
      ]
    },
    {
      grado: "prek", materia: "lectura", tipo: "interactivo",
      es: { titulo: "Las letras: trazos y caminos", url: P + "letras/" },
      en: { titulo: "Letters: tracing paths",       url: P + "letters/" },
      lecciones: [
        { es: "Líneas y formas",          en: "Lines and shapes",
          es_url: P + "letras/prek-trazos-01-lineas-y-formas.html",       en_url: P + "letters/prek-letters-01-lines-and-shapes.html" },
        { es: "Mayúsculas paso a paso",   en: "Capital letters step by step",
          es_url: P + "letras/prek-trazos-02-mayusculas.html",            en_url: P + "letters/prek-letters-02-capital-letters.html" },
        { es: "Conocer las letras",       en: "Knowing the letters",
          es_url: P + "letras/prek-trazos-03-conocer-las-letras.html",    en_url: P + "letters/prek-letters-03-knowing-letters.html" }
      ]
    },

    /* ---------------- KINDERGARTEN ---------------- */
    {
      grado: "k", materia: "matematicas", tipo: "interactivo",
      es: { titulo: "Matemáticas de kindergarten", url: P + "kindergarten/?lang=es" },
      en: { titulo: "Kindergarten math",           url: P + "kindergarten/" },
      lecciones: [
        { es: "Contar hasta 100",           en: "Counting to 100",         archivo: "kindergarten/k-01-counting.html" },
        { es: "Comparar números",           en: "Comparing numbers",       archivo: "kindergarten/k-02-comparing.html" },
        { es: "Sumar y restar",             en: "Adding and taking away",  archivo: "kindergarten/k-03-add-subtract.html" },
        { es: "Parejas de números",         en: "Number partners",         archivo: "kindergarten/k-04-number-partners.html" },
        { es: "Del 11 al 19",               en: "Teen numbers",            archivo: "kindergarten/k-05-teen-numbers.html" },
        { es: "Medir, clasificar y contar", en: "Measure, sort and count", archivo: "kindergarten/k-06-measure-sort.html" },
        { es: "Figuras",                    en: "Shapes",                  archivo: "kindergarten/k-07-shapes.html" }
      ]
    },
    {
      grado: "k", materia: "lectura", tipo: "interactivo", solo: "es",
      es: { titulo: "Lectura en español", url: P + "kindergarten/lectura.html" },
      en: { titulo: "Reading in Spanish",  url: P + "kindergarten/lectura.html" },
      lecciones: [
        { es: "Así funciona un libro",    en: "How a book works (in Spanish)",   url: P + "kindergarten/k-lectura-01-asi-funciona-un-libro.html" },
        { es: "Las vocales",              en: "The vowels (in Spanish)",         url: P + "kindergarten/k-lectura-02-las-vocales.html" },
        { es: "Sílabas y rimas",          en: "Syllables and rhymes (in Spanish)", url: P + "kindergarten/k-lectura-03-silabas-y-rimas.html" },
        { es: "Sílabas directas",         en: "Simple syllables (in Spanish)",   url: P + "kindergarten/k-lectura-04-silabas-directas.html" },
        { es: "Leo palabras y el acento", en: "Words and accents (in Spanish)",  url: P + "kindergarten/k-lectura-05-palabras-y-acento.html" },
        { es: "Leo mi primera oración",   en: "My first sentence (in Spanish)",  url: P + "kindergarten/k-lectura-06-mi-primera-oracion.html" }
      ]
    },
    {
      grado: "k", materia: "lectura", tipo: "interactivo", solo: "en",
      es: { titulo: "Lectura en inglés",   url: P + "kindergarten/reading.html" },
      en: { titulo: "Kindergarten reading", url: P + "kindergarten/reading.html" },
      lecciones: [
        { es: "Así funciona un libro",    en: "How books work",        url: P + "kindergarten/k-reading-01-how-books-work.html" },
        { es: "Rimas y sílabas",          en: "Rhymes and syllables",  url: P + "kindergarten/k-reading-02-rhymes-and-syllables.html" },
        { es: "El primer sonido",         en: "First sounds",          url: P + "kindergarten/k-reading-03-first-sounds.html" },
        { es: "Palabras de tres sonidos", en: "Three-sound words",     url: P + "kindergarten/k-reading-04-three-sound-words.html" },
        { es: "Palabras de vista",        en: "Sight words",           url: P + "kindergarten/k-reading-05-sight-words.html" },
        { es: "Mis primeras oraciones",   en: "My first sentences",    url: P + "kindergarten/k-reading-06-first-sentences.html" }
      ]
    },

    /* ---------------- SEGUNDO GRADO ---------------- */
    {
      grado: "2", materia: "matematicas", tipo: "interactivo",
      es: { titulo: "Matemáticas interactivas de 2.º grado", url: P + "2do_grado/" },
      en: { titulo: "Grade 2 math interactives",             url: P + "2nd_grade/" },
      lecciones: [
        { es: "Valor posicional y operaciones",       en: "Place value & operations",
          es_url: P + "2do_grado/valor-posicional.html",     en_url: P + "2nd_grade/place-value.html" },
        { es: "Números hasta 1000",                   en: "Numbers to 1,000",
          es_url: P + "2do_grado/numeros.html",              en_url: P + "2nd_grade/numbers.html" },
        { es: "Operaciones y pensamiento algebraico", en: "Operations & algebraic thinking",
          es_url: P + "2do_grado/operaciones.html",          en_url: P + "2nd_grade/operations.html" },
        { es: "Medición y recta numérica",            en: "Measurement & number line",
          es_url: P + "2do_grado/medicion.html",             en_url: P + "2nd_grade/measurement.html" },
        { es: "Tiempo y dinero",                      en: "Time & money",
          es_url: P + "2do_grado/tiempo-dinero.html",        en_url: P + "2nd_grade/time-money.html" },
        { es: "Datos",                                en: "Data",
          es_url: P + "2do_grado/datos.html",                en_url: P + "2nd_grade/data.html" },
        { es: "Geometría y fracciones",               en: "Geometry & fractions",
          es_url: P + "2do_grado/geometria-fracciones.html", en_url: P + "2nd_grade/geometry-fractions.html" }
      ]
    },
    {
      grado: "2", materia: "matematicas", tipo: "juego",
      es: { titulo: "Detective de operaciones", url: P + "mate_detective/" },
      en: { titulo: "Math Word Detective",      url: P + "math_word_detective/" }
    },
    {
      grado: "2", materia: "matematicas", tipo: "juego",
      es: { titulo: "Tablas galácticas",     url: P + "galactica_tablas/" },
      en: { titulo: "Galactic Times Tables", url: P + "galactic_tables/" }
    },
    {
      grado: "2", materia: "matematicas", tipo: "juego",
      es: { titulo: "Sudoku para niños", url: P + "sudoku-segundo-grado.html" },
      en: { titulo: "Sudoku for Kids",   url: P + "sudoku-for-kids.html" }
    },
    {
      grado: "2", materia: "lectura", tipo: "juego",
      es: null,
      en: { titulo: "Grow a Sentence", url: P + "grow-a-sentence/" }
    },
    {
      grado: "2", materia: "ciencias", tipo: "juego",
      es: null,
      en: { titulo: "Ecosystem Adventure", url: P + "ecosystem-adventure/" }
    }
  ]
};
