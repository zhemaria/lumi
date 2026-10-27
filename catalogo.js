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

   Una serie puede traer su propio aviso por idioma: aviso: { es: "...", en: "" }.

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
    { grado: "1", area: "ciencias", es: "libro-1ro-ciencias.html",   en: "book-grade1-science.html" },
    { grado: "1", area: "sociales", es: "libro-1ro-sociales.html",   en: "book-grade1-social-studies.html" },
    { grado: "2", area: "ciencias", es: "libro-2do-ciencias.html",   en: "book-grade2-science.html" },
    { grado: "2", area: "sociales", es: "libro-2do-sociales.html",   en: "book-grade2-social-studies.html" },
    { grado: "3", area: "ciencias", es: "libro-3ro-ciencias.html",   en: "book-grade3-science.html" },
    { grado: "3", area: "sociales", es: "libro-3ro-sociales.html",   en: "book-grade3-social-studies.html" },
    { grado: "4", area: "ciencias", es: "libro-4to-ciencias.html",   en: "book-grade4-science.html" },
    { grado: "4", area: "sociales", es: "libro-4to-sociales.html",   en: "book-grade4-social-studies.html" },
    { grado: "5", area: "ciencias", es: "book-grade5-science.html",  en: "book-grade5-science.html" },
    { grado: "5", area: "sociales", es: "book-grade5-social-studies.html", en: "book-grade5-social-studies.html" }
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

    /* ---------------- PRIMER GRADO ---------------- */
    {
      grado: "1", materia: "matematicas", tipo: "interactivo",
      es: { titulo: "Matemáticas de 1.er grado", url: P + "1er_grado/?lang=es" },
      en: { titulo: "Grade 1 math",              url: P + "1er_grado/" },
      lecciones: [
        { es: "Contar hasta 120",            en: "Counting to 120",              archivo: "1er_grado/g1-01-counting-120.html" },
        { es: "Decenas y unidades",          en: "Tens and ones",                archivo: "1er_grado/g1-02-tens-and-ones.html" },
        { es: "Sumar y restar hasta 20",     en: "Adding and subtracting to 20", archivo: "1er_grado/g1-03-facts-to-20.html" },
        { es: "Problemas de sumar y restar", en: "Word problems",                archivo: "1er_grado/g1-04-word-problems.html" },
        { es: "El signo igual",              en: "The equal sign",               archivo: "1er_grado/g1-05-equal-sign.html" },
        { es: "Sumar hasta 100",             en: "Adding within 100",            archivo: "1er_grado/g1-06-add-within-100.html" },
        { es: "Medir y decir la hora",       en: "Length and time",              archivo: "1er_grado/g1-07-length-and-time.html" },
        { es: "Datos y gráficas",            en: "Data and graphs",              archivo: "1er_grado/g1-08-data.html" },
        { es: "Figuras, mitades y cuartos",  en: "Shapes, halves and fourths",   archivo: "1er_grado/g1-09-shapes-and-halves.html" }
      ]
    },
    {
      grado: "1", materia: "lectura", tipo: "interactivo", solo: "es",
      es: { titulo: "Lectura en español", url: P + "1er_grado/lectura.html" },
      en: { titulo: "Reading in Spanish",  url: P + "1er_grado/lectura.html" },
      lecciones: [
        { es: "Sílabas con todas las letras", en: "Syllables with every letter (in Spanish)", url: P + "1er_grado/g1-lectura-01-todas-las-letras.html" },
        { es: "Sílabas trabadas",             en: "Consonant blends (in Spanish)",            url: P + "1er_grado/g1-lectura-02-silabas-trabadas.html" },
        { es: "Sílabas inversas y mixtas",    en: "Closed syllables (in Spanish)",            url: P + "1er_grado/g1-lectura-03-inversas-y-mixtas.html" },
        { es: "Letras con truco",             en: "Tricky spellings (in Spanish)",            url: P + "1er_grado/g1-lectura-04-letras-con-truco.html" },
        { es: "Acento y palabras largas",     en: "Stress and long words (in Spanish)",       url: P + "1er_grado/g1-lectura-05-acento-y-palabras-largas.html" },
        { es: "Oraciones y cuentitos",        en: "Sentences and little stories (in Spanish)", url: P + "1er_grado/g1-lectura-06-oraciones-y-cuentitos.html" }
      ]
    },
    {
      grado: "1", materia: "lectura", tipo: "interactivo", solo: "en",
      es: { titulo: "Lectura en inglés", url: P + "1er_grado/reading.html?lang=es" },
      en: { titulo: "Grade 1 reading",   url: P + "1er_grado/reading.html" },
      lecciones: [
        { es: "Oraciones",                             en: "Sentences",
          es_url: P + "1er_grado/g1-reading-01-sentences.html?lang=es",           en_url: P + "1er_grado/g1-reading-01-sentences.html" },
        { es: "Vocales y grupos de consonantes",       en: "Vowels and blends",
          es_url: P + "1er_grado/g1-reading-02-vowels-and-blends.html?lang=es",   en_url: P + "1er_grado/g1-reading-02-vowels-and-blends.html" },
        { es: "Dígrafos",                              en: "Digraphs",
          es_url: P + "1er_grado/g1-reading-03-digraphs.html?lang=es",            en_url: P + "1er_grado/g1-reading-03-digraphs.html" },
        { es: "La e mágica",                           en: "Magic e",
          es_url: P + "1er_grado/g1-reading-04-magic-e.html?lang=es",             en_url: P + "1er_grado/g1-reading-04-magic-e.html" },
        { es: "Parejas de vocales y terminaciones",    en: "Vowel teams and endings",
          es_url: P + "1er_grado/g1-reading-05-vowel-teams-endings.html?lang=es", en_url: P + "1er_grado/g1-reading-05-vowel-teams-endings.html" },
        { es: "Palabras frecuentes y lecturas cortas", en: "Sight words and short stories",
          es_url: P + "1er_grado/g1-reading-06-sight-words-stories.html?lang=es", en_url: P + "1er_grado/g1-reading-06-sight-words-stories.html" }
      ]
    },

    /* ---------------- QUINTO GRADO ----------------
       Desde 5.º todo va en inglés, con el botón opcional «Ayuda en español».
       La versión «es» abre la misma página con la ayuda ya activada (?ayuda=es). */
    {
      grado: "5", materia: "matematicas", tipo: "interactivo", solo: "en",
      aviso: { es: "En inglés, con ayuda en español: ya viene activada desde aquí.", en: "" },
      es: { titulo: "Matemáticas de 5.º grado", url: P + "5to_grado/?ayuda=es" },
      en: { titulo: "Grade 5 math",            url: P + "5to_grado/" },
      lecciones: [
        { es: "Valor posicional y potencias de diez", en: "Place value and powers of ten", es_url: P + "5to_grado/g5-01-place-value-powers-of-ten.html?ayuda=es", en_url: P + "5to_grado/g5-01-place-value-powers-of-ten.html" },
        { es: "Leer, comparar y redondear decimales", en: "Read, compare and round decimals", es_url: P + "5to_grado/g5-02-decimals.html?ayuda=es", en_url: P + "5to_grado/g5-02-decimals.html" },
        { es: "Multiplicar números de varias cifras", en: "Multi-digit multiplication", es_url: P + "5to_grado/g5-03-multiplication.html?ayuda=es", en_url: P + "5to_grado/g5-03-multiplication.html" },
        { es: "Dividir entre números de dos cifras", en: "Division with two-digit divisors", es_url: P + "5to_grado/g5-04-division.html?ayuda=es", en_url: P + "5to_grado/g5-04-division.html" },
        { es: "Operaciones con decimales", en: "Operations with decimals", es_url: P + "5to_grado/g5-05-decimal-operations.html?ayuda=es", en_url: P + "5to_grado/g5-05-decimal-operations.html" },
        { es: "Expresiones y patrones", en: "Expressions and patterns", es_url: P + "5to_grado/g5-06-expressions-patterns.html?ayuda=es", en_url: P + "5to_grado/g5-06-expressions-patterns.html" },
        { es: "Sumar y restar fracciones", en: "Adding and subtracting fractions", es_url: P + "5to_grado/g5-07-adding-fractions.html?ayuda=es", en_url: P + "5to_grado/g5-07-adding-fractions.html" },
        { es: "La fracción como división", en: "Fractions as division", es_url: P + "5to_grado/g5-08-fractions-division.html?ayuda=es", en_url: P + "5to_grado/g5-08-fractions-division.html" },
        { es: "Multiplicar fracciones", en: "Multiplying fractions", es_url: P + "5to_grado/g5-09-multiplying-fractions.html?ayuda=es", en_url: P + "5to_grado/g5-09-multiplying-fractions.html" },
        { es: "Dividir con fracciones unitarias", en: "Dividing with unit fractions", es_url: P + "5to_grado/g5-10-dividing-fractions.html?ayuda=es", en_url: P + "5to_grado/g5-10-dividing-fractions.html" },
        { es: "Medidas y volumen", en: "Measurement and volume", es_url: P + "5to_grado/g5-11-measurement-volume.html?ayuda=es", en_url: P + "5to_grado/g5-11-measurement-volume.html" },
        { es: "El plano de coordenadas y las figuras", en: "The coordinate plane and shapes", es_url: P + "5to_grado/g5-12-coordinate-plane-shapes.html?ayuda=es", en_url: P + "5to_grado/g5-12-coordinate-plane-shapes.html" }
      ]
    },
    {
      grado: "5", materia: "lectura", tipo: "interactivo", solo: "en",
      aviso: { es: "Esta serie enseña a leer en inglés. La ayuda en español traduce solo las instrucciones y las preguntas.", en: "" },
      es: { titulo: "Lectura en inglés", url: P + "5to_grado/reading.html?ayuda=es" },
      en: { titulo: "Grade 5 reading",   url: P + "5to_grado/reading.html" },
      lecciones: [
        { es: "Raíces griegas y latinas", en: "Greek and Latin roots", es_url: P + "5to_grado/g5-reading-01-greek-latin-roots.html?ayuda=es", en_url: P + "5to_grado/g5-reading-01-greek-latin-roots.html" },
        { es: "Significados y lenguaje figurado", en: "Word meanings and figurative language", es_url: P + "5to_grado/g5-reading-02-word-meanings.html?ayuda=es", en_url: P + "5to_grado/g5-reading-02-word-meanings.html" },
        { es: "Gramática y puntuación", en: "Grammar and punctuation", es_url: P + "5to_grado/g5-reading-03-grammar.html?ayuda=es", en_url: P + "5to_grado/g5-reading-03-grammar.html" },
        { es: "Cuentos, poemas y obras de teatro", en: "Stories, poems and plays", es_url: P + "5to_grado/g5-reading-04-stories.html?ayuda=es", en_url: P + "5to_grado/g5-reading-04-stories.html" },
        { es: "Textos informativos", en: "Informational texts", es_url: P + "5to_grado/g5-reading-05-informational-texts.html?ayuda=es", en_url: P + "5to_grado/g5-reading-05-informational-texts.html" },
        { es: "Puntos de vista y comparar textos", en: "Points of view and comparing texts", es_url: P + "5to_grado/g5-reading-06-comparing-texts.html?ayuda=es", en_url: P + "5to_grado/g5-reading-06-comparing-texts.html" }
      ]
    },

    /* ---------------- CUARTO GRADO ---------------- */
    {
      grado: "4", materia: "matematicas", tipo: "interactivo",
      es: { titulo: "Matemáticas de 4.º grado", url: P + "4to_grado/?lang=es" },
      en: { titulo: "Grade 4 math",            url: P + "4to_grado/" },
      lecciones: [
        { es: "Valor posicional hasta un millón", en: "Place value to one million", es_url: P + "4to_grado/g4-01-place-value-million.html?lang=es", en_url: P + "4to_grado/g4-01-place-value-million.html" },
        { es: "Sumar y restar números grandes", en: "Adding and subtracting large numbers", es_url: P + "4to_grado/g4-02-add-subtract.html?lang=es", en_url: P + "4to_grado/g4-02-add-subtract.html" },
        { es: "Multiplicar números de varios dígitos", en: "Multi-digit multiplication", es_url: P + "4to_grado/g4-03-multiplication.html?lang=es", en_url: P + "4to_grado/g4-03-multiplication.html" },
        { es: "Dividir con residuo", en: "Division with remainders", es_url: P + "4to_grado/g4-04-division.html?lang=es", en_url: P + "4to_grado/g4-04-division.html" },
        { es: "Problemas de varios pasos", en: "Multi-step word problems", es_url: P + "4to_grado/g4-05-word-problems.html?lang=es", en_url: P + "4to_grado/g4-05-word-problems.html" },
        { es: "Factores, múltiplos y patrones", en: "Factors, multiples and patterns", es_url: P + "4to_grado/g4-06-factors-patterns.html?lang=es", en_url: P + "4to_grado/g4-06-factors-patterns.html" },
        { es: "Fracciones equivalentes y comparar", en: "Equivalent fractions and comparing", es_url: P + "4to_grado/g4-07-equivalent-fractions.html?lang=es", en_url: P + "4to_grado/g4-07-equivalent-fractions.html" },
        { es: "Sumar, restar y multiplicar fracciones", en: "Adding, subtracting and multiplying fractions", es_url: P + "4to_grado/g4-08-fraction-operations.html?lang=es", en_url: P + "4to_grado/g4-08-fraction-operations.html" },
        { es: "Décimos, centésimos y decimales", en: "Tenths, hundredths and decimals", es_url: P + "4to_grado/g4-09-decimals.html?lang=es", en_url: P + "4to_grado/g4-09-decimals.html" },
        { es: "Medidas, área y perímetro", en: "Measurement, area and perimeter", es_url: P + "4to_grado/g4-10-measurement.html?lang=es", en_url: P + "4to_grado/g4-10-measurement.html" },
        { es: "Ángulos", en: "Angles", es_url: P + "4to_grado/g4-11-angles.html?lang=es", en_url: P + "4to_grado/g4-11-angles.html" },
        { es: "Rectas, figuras y simetría", en: "Lines, shapes and symmetry", es_url: P + "4to_grado/g4-12-geometry.html?lang=es", en_url: P + "4to_grado/g4-12-geometry.html" }
      ]
    },
    {
      grado: "4", materia: "lectura", tipo: "interactivo", solo: "en",
      es: { titulo: "Lectura en inglés", url: P + "4to_grado/reading.html?lang=es" },
      en: { titulo: "Grade 4 reading",   url: P + "4to_grado/reading.html" },
      lecciones: [
        { es: "Raíces griegas y latinas", en: "Greek and Latin roots", es_url: P + "4to_grado/g4-reading-01-roots-affixes.html?lang=es", en_url: P + "4to_grado/g4-reading-01-roots-affixes.html" },
        { es: "Palabras largas y fluidez", en: "Long words and fluency", es_url: P + "4to_grado/g4-reading-02-multisyllable-words.html?lang=es", en_url: P + "4to_grado/g4-reading-02-multisyllable-words.html" },
        { es: "Significados y lenguaje figurado", en: "Word meanings and figurative language", es_url: P + "4to_grado/g4-reading-03-word-meanings.html?lang=es", en_url: P + "4to_grado/g4-reading-03-word-meanings.html" },
        { es: "Gramática y puntuación", en: "Grammar and punctuation", es_url: P + "4to_grado/g4-reading-04-grammar.html?lang=es", en_url: P + "4to_grado/g4-reading-04-grammar.html" },
        { es: "Cuentos: tema, personajes y punto de vista", en: "Stories: theme, characters and point of view", es_url: P + "4to_grado/g4-reading-05-stories.html?lang=es", en_url: P + "4to_grado/g4-reading-05-stories.html" },
        { es: "Textos informativos", en: "Informational texts", es_url: P + "4to_grado/g4-reading-06-informational-texts.html?lang=es", en_url: P + "4to_grado/g4-reading-06-informational-texts.html" }
      ]
    },
    {
      grado: "4", materia: "lectura", tipo: "interactivo", solo: "es",
      es: { titulo: "Lectura en español", url: P + "4to_grado/lectura.html" },
      en: { titulo: "Reading in Spanish",  url: P + "4to_grado/lectura.html" },
      lecciones: [
        { es: "Acentuación: diptongos, hiatos y tildes", en: "Accents: diphthongs, hiatus and accent marks (in Spanish)", url: P + "4to_grado/g4-lectura-01-acentuacion.html" },
        { es: "Ortografía y puntuación", en: "Spelling and punctuation (in Spanish)", url: P + "4to_grado/g4-lectura-02-ortografia.html" },
        { es: "Raíces, prefijos y sufijos", en: "Roots, prefixes and suffixes (in Spanish)", url: P + "4to_grado/g4-lectura-03-partes-de-palabras.html" },
        { es: "Gramática: verbos, pronombres y oraciones", en: "Grammar (in Spanish)", url: P + "4to_grado/g4-lectura-04-gramatica.html" },
        { es: "Significados, refranes y lenguaje figurado", en: "Word meanings and sayings (in Spanish)", url: P + "4to_grado/g4-lectura-05-significados.html" },
        { es: "Leer y comprender", en: "Reading comprehension (in Spanish)", url: P + "4to_grado/g4-lectura-06-leer-y-comprender.html" }
      ]
    },

    /* ---------------- TERCER GRADO ---------------- */
    {
      grado: "3", materia: "matematicas", tipo: "interactivo",
      es: { titulo: "Matemáticas de 3.er grado", url: P + "3er_grado/?lang=es" },
      en: { titulo: "Grade 3 math",              url: P + "3er_grado/" },
      lecciones: [
        { es: "Multiplicar: grupos iguales y arreglos", en: "Multiplication: equal groups and arrays", es_url: P + "3er_grado/g3-01-multiplication.html?lang=es", en_url: P + "3er_grado/g3-01-multiplication.html" },
        { es: "Dividir y repartir", en: "Division", es_url: P + "3er_grado/g3-02-division.html?lang=es", en_url: P + "3er_grado/g3-02-division.html" },
        { es: "Las tablas de multiplicar", en: "Multiplication facts", es_url: P + "3er_grado/g3-03-facts.html?lang=es", en_url: P + "3er_grado/g3-03-facts.html" },
        { es: "Problemas de dos pasos", en: "Two-step problems", es_url: P + "3er_grado/g3-04-two-step.html?lang=es", en_url: P + "3er_grado/g3-04-two-step.html" },
        { es: "Valor posicional hasta 1000", en: "Place value to 1,000", es_url: P + "3er_grado/g3-05-place-value-1000.html?lang=es", en_url: P + "3er_grado/g3-05-place-value-1000.html" },
        { es: "Fracciones", en: "Fractions", es_url: P + "3er_grado/g3-06-fractions.html?lang=es", en_url: P + "3er_grado/g3-06-fractions.html" },
        { es: "La hora, el volumen y la masa", en: "Time, volume and mass", es_url: P + "3er_grado/g3-07-time-volume-mass.html?lang=es", en_url: P + "3er_grado/g3-07-time-volume-mass.html" },
        { es: "Gráficas y diagramas de puntos", en: "Graphs and line plots", es_url: P + "3er_grado/g3-08-data.html?lang=es", en_url: P + "3er_grado/g3-08-data.html" },
        { es: "Área y perímetro", en: "Area and perimeter", es_url: P + "3er_grado/g3-09-area-perimeter.html?lang=es", en_url: P + "3er_grado/g3-09-area-perimeter.html" },
        { es: "Cuadriláteros y partes iguales", en: "Quadrilaterals and equal parts", es_url: P + "3er_grado/g3-10-shapes.html?lang=es", en_url: P + "3er_grado/g3-10-shapes.html" }
      ]
    },
    {
      grado: "3", materia: "lectura", tipo: "interactivo", solo: "es",
      es: { titulo: "Lectura en español", url: P + "3er_grado/lectura.html" },
      en: { titulo: "Reading in Spanish",  url: P + "3er_grado/lectura.html" },
      lecciones: [
        { es: "Acento y tilde", en: "Accents (in Spanish)", url: P + "3er_grado/g3-lectura-01-acento-y-tilde.html" },
        { es: "Ortografía con truco", en: "Tricky spelling (in Spanish)", url: P + "3er_grado/g3-lectura-02-ortografia.html" },
        { es: "Las partes de las palabras", en: "Word parts (in Spanish)", url: P + "3er_grado/g3-lectura-03-partes-de-palabras.html" },
        { es: "Gramática", en: "Grammar (in Spanish)", url: P + "3er_grado/g3-lectura-04-gramatica.html" },
        { es: "El significado de las palabras", en: "Word meanings (in Spanish)", url: P + "3er_grado/g3-lectura-05-significados.html" },
        { es: "Leer y comprender", en: "Reading comprehension (in Spanish)", url: P + "3er_grado/g3-lectura-06-leer-y-comprender.html" }
      ]
    },
    {
      grado: "3", materia: "lectura", tipo: "interactivo", solo: "en",
      es: { titulo: "Lectura en inglés", url: P + "3er_grado/reading.html?lang=es" },
      en: { titulo: "Grade 3 reading",   url: P + "3er_grado/reading.html" },
      lecciones: [
        { es: "Prefijos y sufijos", en: "Prefixes and suffixes", es_url: P + "3er_grado/g3-reading-01-prefixes-suffixes.html?lang=es", en_url: P + "3er_grado/g3-reading-01-prefixes-suffixes.html" },
        { es: "Palabras largas y con truco", en: "Long and tricky words", es_url: P + "3er_grado/g3-reading-02-multisyllable-words.html?lang=es", en_url: P + "3er_grado/g3-reading-02-multisyllable-words.html" },
        { es: "El significado de las palabras", en: "Word meanings", es_url: P + "3er_grado/g3-reading-03-word-meanings.html?lang=es", en_url: P + "3er_grado/g3-reading-03-word-meanings.html" },
        { es: "Gramática en acción", en: "Grammar at work", es_url: P + "3er_grado/g3-reading-04-grammar.html?lang=es", en_url: P + "3er_grado/g3-reading-04-grammar.html" },
        { es: "Cuentos con Israel", en: "Stories with Israel", es_url: P + "3er_grado/g3-reading-05-stories.html?lang=es", en_url: P + "3er_grado/g3-reading-05-stories.html" },
        { es: "Leer para aprender", en: "Reading to learn", es_url: P + "3er_grado/g3-reading-06-informational-texts.html?lang=es", en_url: P + "3er_grado/g3-reading-06-informational-texts.html" }
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
