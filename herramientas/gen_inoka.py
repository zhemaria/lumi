"""
Guion interactivo de «Inoka: El aliento de la pradera y la gente de Illinois»,
obra de José M. Fernández (español e inglés). Texto revisado y aprobado por el autor
el 29 de octubre de 2026.

Produce obra-inoka-es.html y obra-inoka-en.html.
Uso: python3 gen_inoka.py
"""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from teatro_base import CSS, js_guion

AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = lambda s: html.escape(s, quote=False)
AUTOR = "José M. Fernández"

# ------------------------------------------------------------------ papeles
# clave: (color, grado_es, grado_en, nombre_es, nombre_en, descripción_es, descripción_en, habla)
PAPELES = {
 "NAR1":   ("#5B3F8F", "6.º", "6th", "Narrador 1", "Narrator 1", "Cuenta la historia con voz clara y pausada.", "Tells the story in a clear, calm voice.", True),
 "NAR2":   ("#6A3F86", "6.º", "6th", "Narrador 2", "Narrator 2", "Cuenta la historia con voz clara y pausada.", "Tells the story in a clear, calm voice.", True),
 "NATURA": ("#4D6B12", "Prekínder y kínder", "Pre-K & K", "La naturaleza (sin texto)", "Nature (no lines)", "El viento, las flores de la pradera, las aves y los bisontes: se expresan con el cuerpo.", "The wind, the prairie flowers, the birds and the bison: they express themselves through movement.", False),
 "MUSICOS":("#5A5A1E", "1.º y 2.º", "1st & 2nd", "Músicos (sin texto)", "Musicians (no lines)", "Palos de lluvia y sonajas de semillas en el acto I.", "Rain sticks and seed rattles in Act I.", False),
 "MAIZ":   ("#2F6B2F", "1.º", "1st", "Niño Maíz", "Corn", "Alto y firme: el apoyo de sus hermanas.", "Tall and strong: the support for its sisters.", True),
 "FRIJOL": ("#3C6E1E", "1.º", "1st", "Niña Frijol", "Bean", "Se enreda en el maíz y le devuelve la fuerza al suelo.", "Winds around the corn and gives strength back to the soil.", True),
 "CALAB":  ("#A0461A", "2.º", "2nd", "Niña Calabaza", "Squash", "Cubre la tierra con sus hojas anchas.", "Covers the ground with its wide leaves.", True),
 "AGRI":   ("#7A4E12", "2.º", "2nd", "Agricultora", "Farmer", "Entre los Inoka, las mujeres cultivaban los huertos.", "Among the Inoka, women tended the gardens.", True),
 "TEJ":    ("#8A3B5C", "2.º", "2nd", "Tejedora", "Weaver", "Teje las esteras de junco que cubren las casas.", "Weaves the rush mats that cover the houses.", True),
 "CORO12": ("#1F5F6B", "1.º y 2.º", "1st & 2nd", "Coro", "Chorus", "Canta «Raíz con raíz».", "Sings “Raíz con raíz”.", True),
 "RIOS":   ("#1E5AA0", "3.º y 4.º", "3rd & 4th", "Los ríos (sin texto)", "The rivers (no lines)", "Mueven las telas azules del río Illinois y del Mississippi.", "Move the blue cloths of the Illinois and Mississippi rivers.", False),
 "MENS":   ("#6B5212", "3.º", "3rd", "Mensajero de la aldea", "Village Messenger", "Anuncia la asamblea de la temporada.", "Announces the seasonal assembly.", True),
 "NAVEG":  ("#1A5276", "4.º", "4th", "Navegante Peoria", "Peoria Paddler", "Llega en canoa con carne de bisonte y pieles.", "Arrives by canoe with bison meat and pelts.", True),
 "COMER":  ("#8A4B00", "4.º", "4th", "Comerciante Kaskaskia", "Kaskaskia Trader", "Recibe a los visitantes e intercambia herramientas y cerámica.", "Welcomes the visitors and trades tools and pottery.", True),
 "LKAS":   ("#3F5560", "5.º", "5th", "Líder del consejo Kaskaskia", "Kaskaskia Council Leader", "Habla de la verdadera fuerza de una comunidad.", "Speaks about the true strength of a community.", True),
 "GUARD":  ("#7A2E2E", "6.º", "6th", "Guardiana de la Memoria", "Keeper of Memory", "Explica cómo se gobernaban las aldeas y de dónde viene el nombre «Illinois».", "Explains how the villages governed themselves and where the name “Illinois” comes from.", True),
 "LPEO":   ("#2E4D6B", "6.º", "6th", "Líder del consejo Peoria", "Peoria Council Leader", "Cuenta qué significaba ofrecer el calumet.", "Tells what offering the calumet meant.", True),
 "E1":     ("#2F6F73", "1.º", "1st", "Estudiante de 1.º", "1st grader", "Una frase del cierre.", "One line in the closing scene.", True),
 "E3":     ("#2B6680", "3.º", "3rd", "Estudiante de 3.º", "3rd grader", "Habla de la lengua que vuelve.", "Speaks about the language coming back.", True),
 "E4":     ("#355E8C", "4.º", "4th", "Estudiante de 4.º", "4th grader", "Una frase del cierre.", "One line in the closing scene.", True),
 "E5":     ("#4A4E8F", "5.º", "5th", "Estudiante de 5.º", "5th grader", "Presenta a la tribu Peoria de hoy.", "Introduces today's Peoria Tribe.", True),
 "E6":     ("#5B3F8F", "6.º", "6th", "Estudiante de 6.º", "6th grader", "Dice la última frase antes del coro final.", "Says the last line before the final chorus.", True),
 "TODOS":  ("#194F5A", "Todos", "All", "Todos los grados", "All grades", "Todo el elenco, a la vez.", "The whole cast, together.", True),
}

LETRA_RAIZ = "Raíz con raíz, hojita con hoja,\nla tierra florece cuando el pueblo trabaja.\nMaíz, calabaza y tierno frijol\nprotegen el hogar bajo el mismo sol."
SENTIDO_RAIZ = "Root by root, little leaf by leaf, / the land blooms when the people work together. / Corn, squash and tender beans / protect the home under the same sun."
LETRA_LEGADO = ("Bajo el cielo abierto creció la hierba alta,\nel bisonte, el viento y el agua que no falta.\nMaíz, frijol, calabaza, juntitos bajo el sol:\nla tierra da sus frutos cuando hay unión.\n\n"
 "Pradera dorada, río sin final,\nla gente de Illinois vuelve a cantar.\nLo que fue sembrado no se perderá:\n¡el aliento sigue, sigue y seguirá!\n\n"
 "Por el río bajan canoas de un tronco,\nllevan pieles, conchas y un saludo hondo.\nEn el consejo escuchan, palabra por palabra,\ny así nace un acuerdo que a todos ampara.\n\n"
 "(Estribillo)\n\n"
 "Pasaron los años, el camino fue largo;\ndejaron su tierra, pero no su legado.\nHoy en Oklahoma su nación sigue en pie,\ny vuelve su lengua: los niños la aprenden también.\n\n"
 "(Estribillo, dos veces)\n\n¡Somos el presente y el legado de la gente de Illinois!")
SENTIDO_LEGADO = ("Under the open sky the tall grass grew, the bison, the wind and the water that never runs out. Corn, beans and squash, close together under the sun: the land gives its fruit when there is unity. "
 "Chorus: Golden prairie, endless river, the people of Illinois sing again. What was planted will not be lost: the breath goes on and on! "
 "Canoes carved from a single trunk come down the river, carrying pelts, shells and a heartfelt greeting. In the council they listen, word by word, and so an agreement is born that protects everyone. "
 "The years went by, the road was long; they left their land, but not their legacy. Today their nation still stands in Oklahoma, and their language is coming back: the children are learning it too. "
 "We are the present and the legacy of the people of Illinois!")

# ------------------------------------------------------------------ guion aprobado
# ("AC", es, en) acotación · ("CANCION", papel, título, letra, sentido_en, video) · (papel, es, en)
ACTOS = [
("acto-1", "Acto I · El latido de la pradera y el río", "Act I · The Heartbeat of the Prairie and the River", [
 ("AC", "Participan prekínder y kínder: la naturaleza de Illinois.", "Pre-K and K take part: the natural world of Illinois."),
 ("AC", "El escenario empieza en penumbra. Se oye el pulso lento y constante de un tambor de mano. A los lados del escenario, alumnos de 1.º y 2.º hacen sonar palos de lluvia y sonajas de semillas. Entran despacio los alumnos de prekínder y kínder: son el viento, las flores de la pradera, las aves y los bisontes.",
        "The stage begins in dim light. We hear the slow, steady beat of a hand drum. At the sides of the stage, 1st and 2nd graders play rain sticks and seed rattles. The Pre-K and K students slowly come in: they are the wind, the prairie flowers, the birds and the bison."),
 ("NAR1", "Mucho antes de las autopistas de asfalto y las grandes ciudades de ladrillo, esta amplia cuenca de ríos pertenecía al cielo abierto, a los pastizales altos de la pradera y al cauce generoso del gran río Mississippi.",
          "Long before asphalt highways and great brick cities, this wide land of rivers belonged to the open sky, to the tall prairie grasses and to the generous waters of the great Mississippi River."),
 ("NAR2", "Aquí la vida fluía en equilibrio. Los árboles daban cobijo a las aves, las hierbas alimentaban al bisonte y el río traía agua fresca a los bosques y a los valles. Cada ser vivo formaba parte de una red de respeto y reciprocidad.",
          "Here, life flowed in balance. The trees sheltered the birds, the grasses fed the bison, and the river brought fresh water to the forests and the valleys. Every living thing was part of a web of respect and reciprocity."),
 ("NAR1", "En el corazón de estas tierras vivían familias agrupadas en muchas aldeas. Los misioneros franceses anotaron que se llamaban a sí mismos «Inoka».",
          "In the heart of this land lived families gathered in many villages. French missionaries wrote down that they called themselves “Inoka.”"),
 ("NAR2", "El significado de la palabra Inoka se perdió en el tiempo, pero en las historias de la pradera quedó grabada como el recuerdo de un pueblo que vivía en armonía con la tierra y con sus semejantes.",
          "The meaning of the word Inoka was lost in time, but in the stories of the prairie it remains as the memory of a people who lived in harmony with the land and with one another."),
]),
("acto-2", "Acto II · Las tres hermanas y el hogar de esteras", "Act II · The Three Sisters and the Home of Mats", [
 ("AC", "Participan 1.º y 2.º grado: el cultivo, las casas y el trabajo en común.", "1st and 2nd grades take part: farming, houses and working together."),
 ("AC", "Entran los alumnos de 1.º y 2.º con canastos y con los tallos del maíz, el frijol y la calabaza. Al fondo, una casa larga de arcos cubierta con esteras de junco.",
        "The 1st and 2nd graders come in with baskets and with the stalks of the corn, the beans and the squash. Upstage, a longhouse of bent poles covered with rush mats."),
 ("NAR1", "En la primavera y el verano, las mujeres de las aldeas Inoka cultivaban fértiles huertos en los valles. Su alimento principal nacía de tres plantas que crecían juntas, ayudándose unas a otras, a las que hoy muchos pueblos llaman las Tres Hermanas.",
          "In spring and summer, the women of the Inoka villages tended rich gardens in the valleys. Their main food came from three plants that grew together, helping one another, which many peoples today call the Three Sisters."),
 ("MAIZ", "Yo soy el Maíz. Crezco alto, recto y firme hacia el sol del verano. Con mi cuerpo fuerte sirvo de columna y de apoyo para mis hermanas.",
          "I am Corn. I grow tall, straight and steady toward the summer sun. With my strong stalk, I hold up my sisters."),
 ("FRIJOL", "Yo soy el Frijol. Sola en la tierra no puedo alcanzar la altura; pero me enredo suavemente en el tallo del Maíz, subo hacia la luz y le devuelvo la fuerza al suelo.",
            "I am Bean. Alone on the ground, I cannot reach up high; but I gently wind around Corn's stalk, climb toward the light and give strength back to the soil."),
 ("CALAB", "Yo soy la Calabaza. Extiendo mis hojas anchas sobre la tierra. Mantengo el suelo fresco y húmedo para que la sequía no marchite a mis hermanas.",
           "I am Squash. I spread my wide leaves over the ground. I keep the soil cool and moist so dry weather does not wilt my sisters."),
 ("AGRI", "Nuestras abuelas comprendieron que la tierra da abundancia no por la fuerza, sino por la unión. Si sembramos juntas, la cosecha alimenta a toda la aldea.",
          "Our grandmothers understood that the land gives plenty not through force, but through working together. If we plant together, the harvest feeds the whole village."),
 ("TEJ", "Y con los juncos de los pantanos tejemos las esteras que cubren nuestras casas. Una sola caña se quiebra al doblarla, pero trenzadas todas juntas protegen a nuestras familias del viento y de la lluvia.",
         "And with the rushes from the marshes we weave the mats that cover our houses. One reed alone breaks when you bend it, but woven all together they protect our families from the wind and the rain."),
 ("CANCION", "CORO12", ("Raíz con raíz", "Root by Root"), LETRA_RAIZ, SENTIDO_RAIZ, "inoka-raiz-con-raiz"),
]),
("acto-3", "Acto III · Las rutas del río y el comercio entre aldeas", "Act III · The River Routes and Trade Between Villages", [
 ("AC", "Participan 3.º y 4.º grado: la navegación, el comercio y las alianzas entre aldeas.", "3rd and 4th grades take part: river travel, trade and alliances between villages."),
 ("AC", "Cuatro alumnos ondean las telas azules como las aguas del río Illinois. Dos navegantes avanzan dentro de las siluetas de las canoas de tronco ahuecado, con remos de madera ligera.",
        "Four students wave the blue cloths like the waters of the Illinois River. Two paddlers move forward inside the cutouts of the dugout canoes, with light wooden paddles."),
 ("NAR2", "Los ríos de Illinois no eran fronteras, sino anchos caminos de intercambio. Por ellos se comunicaban las aldeas de la Confederación: los Kaskaskia, los Peoria, los Tamaroa, los Cahokia y, más tarde, aliados como los Michigamea.",
          "The rivers of Illinois were not borders, but wide roads for trade. Along them, the villages of the Confederation stayed in touch: the Kaskaskia, the Peoria, the Tamaroa, the Cahokia and, later, allies such as the Michigamea."),
 ("NAVEG", "¡Saludos, hermanos de la aldea vecina! Navegamos por el río en nuestra canoa, tallada en un solo tronco. Traemos carne seca de bisonte y valiosas pieles de castor.",
           "Greetings, friends from the neighboring village! We travel the river in our canoe, carved from a single tree trunk. We bring dried bison meat and valuable beaver pelts."),
 ("COMER", "¡Bienvenidos a nuestra orilla! Por los ríos y los caminos antiguos intercambiamos herramientas de pedernal, conchas de río y cuencos de barro. El comercio une a nuestras familias y fortalece la paz.",
           "Welcome to our riverbank! Along the rivers and the old trails we trade flint tools, river shells and clay bowls. Trade brings our families together and makes peace stronger."),
 ("NAR1", "Cerca de estos ríos, siglos atrás, había florecido la gran ciudad de los montículos de Cahokia, de la cultura misisipiana. Cuando los Inoka recorrían estos ríos, aquella ciudad ya estaba vacía. La relación entre aquella ciudad y los pueblos que vinieron después todavía la estudian los arqueólogos.",
          "Centuries earlier, near these rivers, the great mound city of Cahokia had flourished. It belonged to the Mississippian culture. By the time the Inoka traveled these rivers, that city was already empty. Archaeologists are still studying how that city was related to the peoples who came after."),
 ("MENS", "(Entra con paso firme, con un bastón de cañas trenzadas.) ¡Noticias de la asamblea! Los jefes y los ancianos de cada aldea nos llaman a la reunión de la temporada. Es hora de compartir lo que dio el verano y de escuchar los relatos de los mayores.",
          "(Enters with firm steps, holding a staff of woven reeds.) News from the assembly! The chiefs and the elders of each village are calling us to the meeting of the season. It is time to share what the summer gave us and to listen to the stories of our elders."),
]),
("acto-4", "Acto IV · La asamblea de las aldeas y la sabiduría del consejo", "Act IV · The Village Assembly and the Wisdom of the Council", [
 ("AC", "Participan 5.º y 6.º grado: las decisiones por consenso, la tradición oral y la llegada de los franceses.", "5th and 6th grades take part: decisions by consensus, oral tradition and the arrival of the French."),
 ("AC", "Los alumnos de 5.º y 6.º forman un círculo de consejo alrededor de un fogón simbólico. Los grupos de los otros grados se sientan en un semicírculo exterior: es la gran asamblea de la comunidad.",
        "The 5th and 6th graders form a council circle around a symbolic fire. The groups from the other grades sit in an outer half circle: this is the great assembly of the community."),
 ("GUARD", "En nuestras aldeas no había un rey ni un gobierno central. Cada aldea tenía sus jefes: uno para la paz y otro para la guerra, y nadie heredaba el cargo. Pero cuando había que tomar grandes decisiones, nos escuchábamos unos a otros hasta llegar a un acuerdo.",
           "In our villages there was no king and no central government. Each village had its own chiefs: one for peace and one for war, and no one inherited the position. But when big decisions had to be made, we listened to one another until we reached an agreement."),
 ("LKAS", "La verdadera fuerza de una comunidad no se mide por sus armas, sino por su capacidad de proteger a los niños, cuidar a los mayores y pensar en los que vendrán después de nosotros.",
          "The true strength of a community is not measured by its weapons, but by how well it protects its children, cares for its elders and thinks of those who will come after us."),
 ("LPEO", "Cuando llegaban visitantes en son de paz, les ofrecíamos el calumet, una pipa ceremonial adornada con plumas. Era nuestra manera más solemne de decir: aquí hay paz, diálogo y hospitalidad.",
          "When visitors came in peace, we offered them the calumet, a ceremonial pipe decorated with feathers. It was our most solemn way of saying: here there is peace, dialogue and hospitality."),
 ("AC", "El calumet se nombra, pero no aparece en escena.", "The calumet is mentioned, but it does not appear on stage."),
 ("NAR2", "En 1673 llegaron por el río los exploradores franceses Jacques Marquette y Louis Jolliet. Ya habían oído hablar de este pueblo a otros pueblos vecinos, que lo llamaban con una palabra parecida a «ilinwe». De ella viene el nombre «Illinois». Y en una aldea Peoria, los recibieron con el calumet de la paz.",
          "In 1673, the French explorers Jacques Marquette and Louis Jolliet arrived by river. They had already heard about these people from other nations of the Great Lakes, who called them by a word that sounded like “ilinwe.” That is where the name “Illinois” comes from. And in a Peoria village, they were welcomed with the peace calumet."),
 ("GUARD", "Marquette creyó que «Illinois» quería decir «los hombres». Hoy los estudiosos piensan que la palabra significaba «los que hablan de la manera común». Pero el nombre que ellos mismos se daban era otro: Inoka. Y ser parte de esta tierra pide madurez, valor para cuidar la paz y sabiduría para compartir el fuego.",
           "Marquette believed that “Illinois” meant “the men.” Today, scholars think the word meant “those who speak in the ordinary way.” But the name they gave themselves was a different one: Inoka. And being part of this land calls for maturity, courage to protect the peace and wisdom to share the fire."),
]),
("acto-5", "Acto V · Escena final: el legado vivo de los Inoka", "Act V · Final Scene: The Living Legacy of the Inoka", [
 ("AC", "Participa toda la escuela: del pasado al presente de la tribu Peoria de Oklahoma.", "The whole school takes part: the Peoria Tribe of Oklahoma, from the past to today."),
 ("AC", "Todo el elenco se va uniendo poco a poco y da un paso al frente, a la vez.", "The whole cast gradually joins in and takes one step forward, all together."),
 ("NAR1", "Pasaron los siglos. Las praderas cambiaron de manto, sobre los ríos nacieron puentes y las aldeas de esteras dieron paso a los mapas del moderno estado de Illinois.",
          "Centuries went by. The prairies changed their colors, bridges rose over the rivers, and the villages of mats gave way to the maps of the modern state of Illinois."),
 ("NAR2", "Pero la historia de los Inoka no terminó en el pasado. Tuvieron que dejar Illinois: primero hacia Missouri, después a Kansas y, en 1867, a lo que hoy es Oklahoma. Y allí siguieron adelante.",
          "But the story of the Inoka did not end in the past. They had to leave Illinois: first for Missouri, then for Kansas and, in 1867, for what is now Oklahoma. And there, they carried on."),
 ("E5", "Hoy sus descendientes forman la Peoria Tribe of Indians of Oklahoma, una nación reconocida por el gobierno de Estados Unidos, que conserva con orgullo su historia y su identidad.",
        "Today their descendants form the Peoria Tribe of Indians of Oklahoma, a nation recognized by the United States government, which proudly keeps its history and its identity."),
 ("E3", "Ya no quedan hablantes nativos de su lengua, el miami-illinois. Pero niños y jóvenes de las naciones Peoria y Miami la están aprendiendo de nuevo, y así vuelven a sonar las palabras de sus abuelos.",
        "Their language, Miami-Illinois, no longer has any native speakers. But children and young people of the Peoria and Miami nations are learning it again, and so the words of their grandparents are heard once more."),
 ("E1", "Nos enseñan a cuidar los ríos, las plantas y los bosques.", "They teach us to care for the rivers, the plants and the forests."),
 ("E4", "Nos enseñan que los caminos sirven para tender la mano y comerciar en paz.", "They teach us that paths are for helping one another and trading in peace."),
 ("E6", "Y nos recuerdan que, para ser dignos del nombre de Illinois, debemos gobernarnos escuchando, con justicia y con respeto a la naturaleza.",
        "And they remind us that, to be worthy of the name Illinois, we must govern ourselves by listening, with fairness and with respect for nature."),
 ("TODOS", "¡Somos la memoria de la pradera!\n¡Somos el aliento del gran río!\n¡Somos el presente y el legado de la gente de Illinois!",
           "We are the memory of the prairie!\nWe are the breath of the great river!\nWe are the present and the legacy of the people of Illinois!"),
 ("AC", "Suenan los tambores de mano y empieza la canción final. Todo el elenco canta y baila tomado de las manos, con pasos sencillos, sin imitar danzas indígenas.", "The hand drums play and the final song begins. The whole cast sings and dances, holding hands, with simple steps, not imitating Native dances."),
 ("CANCION", "TODOS", ("Legado de la pradera", "Legacy of the Prairie"), LETRA_LEGADO, SENTIDO_LEGADO, "inoka-legado-de-la-pradera"),
 ("AC", "Todo el elenco hace una reverencia tomados de las manos mientras se cierra el telón.", "The whole cast takes a bow, holding hands, as the curtain closes."),
]),
]

T = {
 "es": dict(titulo="Inoka", titulo_largo="Inoka: El aliento de la pradera y la gente de Illinois", sub="El aliento de la pradera y la gente de Illinois",
   autor=f"Obra de {AUTOR}", otro="obra-inoka-en.html", otro_lang="en",
   intro="Antes de las autopistas y las ciudades de ladrillo, en las praderas y los ríos de Illinois vivía el pueblo Inoka. Una obra para toda la escuela, de prekínder a 6.º grado, sobre la tierra, el trabajo en común, el consejo y un pueblo que sigue vivo: la tribu Peoria de Oklahoma.",
   reparto="Reparto", mipapel="Mi papel:", todos_op="Todos los papeles", solo="Mostrar solo mis líneas",
   oir="Escuchar", oir_esc="🔊 Escuchar el acto", parar="⏹ Parar", menor="Letra más pequeña", mayor="Letra más grande", imprimir="🖨️ Imprimir",
   th=["Papel", "Grado", "Cómo es", "Líneas"], acot="Acotación", arriba="↑ Cerrar y volver arriba", ir="Ir a", cancion="Canción",
   ver_cancion="Ver la canción con su letra", letra="Letra", sentido="",
   nota="Las acotaciones (en cursiva) indican lo que pasa en el escenario: no se dicen en voz alta. Las canciones se cantan con la grabación de la guía de producción.",
   reparto_nota="Todos los grupos pueden crecer o achicarse sin cambiar el texto. Cuando un papel tiene un solo niño (Niño Maíz, Agricultora…), la línea también la puede decir un grupo pequeño.",
   prod="🎬 Guía de producción: reparto, canciones, vestuario respetuoso, escenografía y carta a las familias",
   hist="📜 Guía histórica para el docente: quiénes eran los Inoka, mitos y hechos, y actividades por grado",
   prog="📄 Programa de mano", cartel="🖼️ Cartel de la función",
   respeto="Esta obra habla de un pueblo que sigue vivo. Los niños no se disfrazan de indígenas ni usan objetos ceremoniales: cada personaje se reconoce por lo que hace. Más detalles en la guía de producción.",
   pie=f"«Inoka: El aliento de la pradera y la gente de Illinois» · Obra de {AUTOR} · Licencia CC BY-NC-SA 4.0",
   voz="es-US", lumi="index-es.html", teatro="teatro-es.html", teatro_txt="← Teatro de Lumi",
   guia="obra-inoka-produccion-es.html", historia="obra-inoka-historia-es.html", programa="obra-inoka-programa-es.html", cartel_url="obra-inoka-cartel-es.html",
   menu=[("index-es.html","Inicio"),("grados-es.html","Por grado"),("materias-es.html","Por materia"),("teatro-es.html","Teatro")]),
 "en": dict(titulo="Inoka", titulo_largo="Inoka: The Breath of the Prairie and the People of Illinois", sub="The Breath of the Prairie and the People of Illinois",
   autor=f"A play by {AUTOR}", otro="obra-inoka-es.html", otro_lang="es",
   intro="Before the highways and the brick cities, the Inoka people lived on the prairies and rivers of Illinois. A play for the whole school, from Pre-K to 6th grade, about the land, working together, the council and a people who are still here today: the Peoria Tribe of Oklahoma.",
   reparto="Cast", mipapel="My part:", todos_op="All parts", solo="Show only my lines",
   oir="Listen", oir_esc="🔊 Listen to the act", parar="⏹ Stop", menor="Smaller text", mayor="Bigger text", imprimir="🖨️ Print",
   th=["Part", "Grade", "What they are like", "Lines"], acot="Stage direction", arriba="↑ Close and back to top", ir="Go to", cancion="Song",
   ver_cancion="Watch the song with its lyrics", letra="Lyrics (sung in Spanish)", sentido="What it means:",
   nota="Stage directions (in italics) tell what happens on stage: they are not read aloud. The songs are sung in Spanish, with the recordings in the production guide.",
   reparto_nota="Every group can grow or shrink without changing the text. When a part has one child (Corn, Farmer...), the line can also be said by a small group.",
   prod="🎬 Production guide: cast, songs, respectful costumes, sets and family letter",
   hist="📜 Historical guide for teachers: who the Inoka were, myths and facts, and activities by grade",
   prog="📄 Program", cartel="🖼️ Show poster",
   respeto="This play is about a people who are still here today. Children do not dress up as Native people or use ceremonial objects: each character is recognized by what they do. More details in the production guide.",
   pie=f"“Inoka: The Breath of the Prairie and the People of Illinois” · A play by {AUTOR} · License CC BY-NC-SA 4.0",
   voz="en-US", lumi="index.html", teatro="teatro.html", teatro_txt="← Lumi Theater",
   guia="obra-inoka-produccion-en.html", historia="obra-inoka-historia-en.html", programa="obra-inoka-programa-en.html", cartel_url="obra-inoka-cartel-en.html",
   menu=[("index.html","Home"),("grados.html","By grade"),("materias.html","By subject"),("teatro.html","Theater")]),
}

def nombre(p, L): return PAPELES[p][3 if L == "es" else 4]
def grado(p, L): return PAPELES[p][1 if L == "es" else 2]
def verso(s): return "<br>".join(e(x) for x in s.split("\n"))

def cuenta():
    c = {p: 0 for p in PAPELES}
    for _, _, _, items in ACTOS:
        for it in items:
            if it[0] == "AC": continue
            if it[0] == "CANCION": c[it[1]] += 1
            else: c[it[0]] += 1
    return c

def pagina(L):
    t = T[L]; c = cuenta()
    filas = "\n".join(
        f'<tr><td><span class="punto" style="background:{PAPELES[p][0]}" aria-hidden="true"></span>{e(nombre(p,L))}</td><td>{e(grado(p,L))}</td><td>{e(PAPELES[p][5 if L=="es" else 6])}</td><td>{c[p]}</td></tr>'
        for p in PAPELES)
    opciones = "".join(f'<option value="{p}">{e(nombre(p,L))} · {e(grado(p,L))}</option>' for p in PAPELES if PAPELES[p][7])
    actos = []
    for aid, tes, ten, items in ACTOS:
        cuerpo = []
        for it in items:
            if it[0] == "AC":
                cuerpo.append(f'  <p class="acot"><span class="sr">{e(t["acot"])}: </span>({e(it[1 if L=="es" else 2])})</p>')
            elif it[0] == "CANCION":
                _, p, tit, letra, sentido, vid = it
                titulo_txt = f"«{tit[0]}»" if L == "es" else f"“{tit[0]}” (“{tit[1]}”)"
                extra = f'<p class="sentido"><strong>{e(t["sentido"])}</strong> {e(sentido)}</p>' if L == "en" else ""
                cuerpo.append(f'''  <div class="linea cancion" data-papeles="{p}" style="--c:{PAPELES[p][0]}">
   <div><span class="quien">{e(nombre(p,L))}</span><span class="grado">{e(grado(p,L))}</span>
   <p class="txt"><strong>🎵 {e(t["cancion"])}: {e(titulo_txt)}</strong></p>
   <p class="letra" lang="es"{' aria-label="'+e(t["letra"])+'"' if L=="en" else ""}>{verso(letra)}</p>{extra}
   <p style="margin:.4rem 0 0"><a href="{t["guia"]}#{vid}">▶ {e(t["ver_cancion"])}</a></p></div>
  </div>''')
            else:
                p, tx_es, tx_en = it
                tx = tx_es if L == "es" else tx_en
                cuerpo.append(f'''  <div class="linea" data-papeles="{p}" style="--c:{PAPELES[p][0]}">
   <div><span class="quien">{e(nombre(p,L))}</span><span class="grado">{e(grado(p,L))}</span><p class="txt">{verso(tx)}</p></div>
   <button type="button" class="oir" aria-label="{e(t["oir"])}: {e(nombre(p,L))}">🔊</button>
  </div>''')
        tit = tes if L == "es" else ten
        actos.append(f'''<details class="seccion acord" id="{aid}">
 <summary><h2 id="t-{aid}">{e(tit)}</h2></summary>
 <div class="cuerpo">
 <div class="acto-h"><span><button type="button" class="oir-esc">{e(t["oir_esc"])}</button> <button type="button" class="parar">{e(t["parar"])}</button></span></div>
{chr(10).join(cuerpo)}
 <p class="arriba"><a href="#contenido" class="cerrar">{e(t["arriba"])}</a></p>
 </div>
</details>''')
    anclas = [("reparto", t["reparto"])] + [(a[0], (a[1] if L == "es" else a[2]).split(" · ")[0]) for a in ACTOS]
    nav = "".join(f'<li><a href="#{a}">{e(x)}</a></li>' for a, x in anclas)
    menu = "\n".join(f'   <a href="{h}"{" aria-current=\"page\"" if h == t["teatro"] else ""}>{e(x)}</a>' for h, x in t["menu"])
    idioma = (f'<span aria-current="true">Español</span><a href="{t["otro"]}" lang="en" hreflang="en">English</a>' if L == "es"
              else f'<a href="{t["otro"]}" lang="es" hreflang="es">Español</a><span aria-current="true">English</span>')
    return f'''<!doctype html>
<!-- {t["titulo_largo"]} · {AUTOR} · CC BY-NC-SA 4.0 · generado con herramientas/gen_inoka.py -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["titulo_largo"])} · Lumi</title>
<meta name="description" content="{e(t["intro"])}">
<meta name="author" content="{AUTOR}">
<link rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<link rel="alternate" hreflang="{t["otro_lang"]}" href="{t["otro"]}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="lumi.css?v=6">
<style>{CSS}</style>
</head>
<body data-voz="{t["voz"]}">
<a class="saltar" href="#contenido">{"Saltar al contenido" if L=="es" else "Skip to content"}</a>
<header class="cabecera">
 <div class="envoltura">
  <a class="marca" href="{t["lumi"]}"><img src="lumi-logo-horizontal.svg" alt="{"Lumi — página de inicio" if L=="es" else "Lumi — home page"}" width="560" height="240"></a>
  <nav aria-label="{"Menú principal" if L=="es" else "Main menu"}" class="menu">
{menu}
  </nav>
  <div class="idioma" role="group" aria-label="{"Idioma" if L=="es" else "Language"}">{idioma}</div>
 </div>
</header>
<section class="obra-cab" aria-labelledby="titulo">
 <div class="envoltura">
  <p style="margin:0"><a href="{t["teatro"]}">{e(t["teatro_txt"])}</a></p>
  <h1 id="titulo">{e(t["titulo"])}</h1>
  <p class="sub">{e(t["sub"])}</p>
  <p class="autor">{e(t["autor"])}</p>
  <p>{e(t["intro"])}</p>
  <p><a href="{t["guia"]}">{e(t["prod"])}</a></p>
  <p><a href="{t["historia"]}">{e(t["hist"])}</a></p>
  <p><a href="{t["programa"]}">{e(t["prog"])}</a> · <a href="{t["cartel_url"]}">{e(t["cartel"])}</a></p>
  <p class="permiso">{e(t["respeto"])}</p>
 </div>
</section>
<main id="contenido" tabindex="-1"><div class="envoltura">
 <nav aria-label="{e(t["ir"])}"><ul class="anclas">{nav}</ul></nav>
 <div class="barra" role="group" aria-label="{e(t["mipapel"])}">
  <label for="mi-papel">{e(t["mipapel"])}</label>
  <select id="mi-papel"><option value="">{e(t["todos_op"])}</option>{opciones}</select>
  <label class="chk"><input type="checkbox" id="solo"> {e(t["solo"])}</label>
  <button type="button" id="menor" aria-label="{e(t["menor"])}">A−</button>
  <button type="button" id="mayor" aria-label="{e(t["mayor"])}">A+</button>
  <button type="button" id="imprimir">{e(t["imprimir"])}</button>
 </div>
 <p>{e(t["nota"])}</p>
 <details class="seccion acord" id="reparto">
  <summary><h2 id="t-reparto">{e(t["reparto"])}</h2></summary>
  <div class="cuerpo">
  <p>{e(t["reparto_nota"])}</p>
  <div class="envoltura-tabla"><table class="tabla">
   <caption class="sr">{e(t["reparto"])}</caption>
   <thead><tr>{"".join(f'<th scope="col">{e(h)}</th>' for h in t["th"])}</tr></thead>
   <tbody>
{filas}
   </tbody>
  </table></div>
  <p class="arriba"><a href="#contenido" class="cerrar">{e(t["arriba"])}</a></p>
  </div>
 </details>
{chr(10).join(actos)}
</div></main>
<footer class="pie"><div class="envoltura"><p>{e(t["pie"])}</p></div></footer>
<script>{js_guion("inoka-papel")}</script>
</body>
</html>
'''

if __name__ == "__main__":
    for L in ("es", "en"):
        with open(os.path.join(AQUI, f"obra-inoka-{L}.html"), "w", encoding="utf-8") as f:
            f.write(pagina(L))
    print("ok")
