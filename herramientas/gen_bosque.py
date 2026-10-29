"""
Generador del guion interactivo de «El bosque mágico», de Vicente Cañón Verdasco
(© 2019, www.obrasteatro.com), en español y en su traducción al inglés.

Publicado en Lumi con autorización escrita del autor (29 de octubre de 2026):
guion interactivo, traducción al inglés y reparto ampliado, siempre con su nombre
como autor y con el título original. El texto de la obra es del autor; este
generador y el diseño de las páginas son de Lumi.

Produce:
  obra-bosque-magico-es.html   guion en español
  obra-bosque-magico-en.html   guion en inglés
  (y, con --traduccion, El-bosque-magico-traduccion-ingles.html: el texto
   bilingüe lado a lado, para enviar al autor; no se publica en Lumi)
Uso: python3 gen_bosque.py [--traduccion]
"""
import html, os, sys

AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = lambda s: html.escape(s, quote=False)

AUTOR = "Vicente Cañón Verdasco"
WEB_AUTOR = "https://www.obrasteatro.com/"

# ------------------------------------------------------------------ papeles
# clave: (color, grado_es, grado_en, nombre_es, nombre_en, descripción_es, descripción_en, miembros)
# Los papeles compuestos (BB, HD, PUEBLOS, ...) no aparecen en el selector: sus líneas
# se resaltan cuando el niño elige cualquiera de sus miembros.
PAPELES = {
 "NAR":     ("#5B3F8F", "5.º y 6.º", "5th & 6th", "Narradora", "Narrator",
             "Cuenta la historia en verso, entre escena y escena. Pueden ser de una a cuatro voces, narradoras o narradores.",
             "Tells the story in verse between the scenes. The part can be shared by two to four voices.", None),
 "BRUJAS":  ("#6A2C70", "3.º y 4.º", "3rd & 4th", "Brujas", "Witches",
             "Envidiosas y cómicas: preparan el conjuro y se esconden en los matorrales.",
             "Envious and funny: they brew the spell and hide behind the bushes.", None),
 "BRUJOS":  ("#3B3A6E", "3.º y 4.º", "3rd & 4th", "Brujos", "Wizards",
             "Igual de envidiosos y cómicos que las brujas; al final, piden ser amigos.",
             "Just as envious and funny as the witches; at the end, they ask to be friends.", None),
 "HADAS":   ("#A02C6B", "1.º y 2.º", "1st & 2nd", "Hadas", "Fairies",
             "Llegan del bosque con música alegre y traen el plan para romper el maleficio.",
             "They arrive from the forest to cheerful music and bring the plan to break the curse.", None),
 "DUENDES": ("#2F6B2F", "1.º y 2.º", "1st & 2nd", "Duendes", "Elves",
             "Compañeros de las hadas: guían el gran baile en círculo de la noche.",
             "The fairies' partners: they lead the big nighttime circle dance.", None),
 "SABIAS":  ("#3F5560", "3.º y 4.º", "3rd & 4th", "Personas sabias", "Wise People",
             "Las personas más sabias de los pueblos: buscan una solución y se la explican a todos.",
             "The wisest people of the villages: they look for a solution and explain it to everyone.", None),
 "ALE":     ("#8A4B00", "Prekínder y kínder", "Pre-K & K", "Pueblo de la Alegría", "Village of Joy",
             "Bailan todo el día, hasta que el maleficio los pone tristes. Camisetas amarillas.",
             "They dance all day, until the curse makes them sad. Yellow T-shirts.", None),
 "AMI":     ("#1E5AA0", "Prekínder y kínder", "Pre-K & K", "Pueblo de la Amistad", "Village of Friendship",
             "Juegan juntos, hasta que el maleficio los hace pelear. Camisetas azules.",
             "They play together, until the curse makes them quarrel. Blue T-shirts.", None),
 "GEN":     ("#A32420", "Prekínder y kínder", "Pre-K & K", "Pueblo de la Generosidad", "Village of Generosity",
             "Comparten sus helados, hasta que el maleficio los vuelve egoístas. Camisetas rojas.",
             "They share their ice cream, until the curse makes them selfish. Red T-shirts.", None),
 # compuestos
 "BB":      ("#4E2A5E", "3.º y 4.º", "3rd & 4th", "Brujas y brujos", "Witches and Wizards", "", "", ["BRUJAS", "BRUJOS"]),
 "HD":      ("#6B3A5A", "1.º y 2.º", "1st & 2nd", "Hadas y duendes", "Fairies and Elves", "", "", ["HADAS", "DUENDES"]),
 "PUEBLOS": ("#194F5A", "Prekínder y kínder", "Pre-K & K", "Todos los habitantes", "All the villagers", "", "", ["ALE", "AMI", "GEN"]),
 "PHD":     ("#194F5A", "Prek. a 2.º", "Pre-K to 2nd", "Habitantes, hadas y duendes", "Villagers, Fairies and Elves", "", "", ["ALE", "AMI", "GEN", "HADAS", "DUENDES"]),
}
BASE = [k for k, v in PAPELES.items() if v[7] is None]
def miembros(p): return PAPELES[p][7] or [p]

# ------------------------------------------------------------------ música
# Lista (opcional) que propone el autor al final de la obra.
PISTAS = {
 1: ("The New Order", "Aaron Kenny", "cinematográfico oscuro", "dark cinematic"),
 2: ("Sand Castle", "Quincas Moreira", "infantil, positivo", "children's, upbeat"),
 3: ("St. Francis", "Josh Lippi & The Overtimers", "rock, triste", "rock, sad"),
 4: ("Rainbow Forest", "Quincas Moreira", "infantil, feliz", "children's, happy"),
 5: ("Goat", "Wayne Jones", "infantil, feliz", "children's, happy"),
 6: ("Sleeping Sheep", "The Green Orbs", "infantil, serena", "children's, calm"),
 7: ("Kinderszenen, op. 15, n.º 1: «De países y gentes lejanos»", "Robert Schumann", "piano", "piano"),
 8: ("Canción de cuna", "Johannes Brahms", "nana", "lullaby"),
 9: ("Twirly Tops", "The Green Orbs", "infantil, feliz", "children's, happy"),
 10: ("Dancing on Green Grass", "The Green Orbs", "infantil, positiva", "children's, upbeat"),
}
PISTA_EN = {7: "Kinderszenen, Op. 15, No. 1: “Of Foreign Lands and Peoples”", 8: "Lullaby (Wiegenlied)"}

# ------------------------------------------------------------------ guion
# Cada escena: (id, título_es, título_en, [elementos])
# Elementos:
#   ("AC", es, en)                 acotación (no se dice en voz alta)
#   ("MUS", n)                     indicación del autor: MÚSICA: TRACK n
#   ("LUGAR", es, en)              rótulo del autor: «(PUEBLO DE LA ALEGRÍA)»
#   ("FIN", es, en)                «Telón»
#   (papel, etiqueta_es, etiqueta_en, es, en)   línea; etiqueta None = nombre del papel
# El texto en español es EXACTAMENTE el del autor (PDF «El-bosque-magico-DEFINITIVA-
# version-para-24-alumnos-2026»), con su puntuación y sus mayúsculas. Solo se corrigieron
# las erratas de NOTAS_ERRATAS. «\n» = salto de verso del original.
ESCENAS = [
("escena-1", "Escena 1", "Scene 1", [
 ("AC", "Al abrirse el telón, podemos ver una escenografía compuesta por cuatro matorrales, donde ya estarán escondidos las BRUJAS y BRUJOS. Al salir a escena la NARRADORA, los HABITANTES de los pueblos estarán sentados, ante el escenario y cara al público, colocados en tres grupos, muy diferenciados, por los colores muy vistosos de sus camisetas. Cuando la NARRADORA vaya nombrando, uno por uno, a cada pueblo, estos se levantarán y saludarán, durante unos segundos al público, para volverse a sentar",
        "When the curtain opens, we see a set made up of four bushes, with the WITCHES and WIZARDS already hiding behind them. As the NARRATOR comes on stage, the VILLAGERS of the three villages are sitting in front of the stage, facing the audience, in three clearly separate groups that are easy to tell apart by the bright colors of their T-shirts. As the NARRATOR names each village, one by one, its villagers stand up and wave to the audience for a few seconds, then sit back down"),
 ("NAR", None, None, "Había una vez tres pueblos que vivían, cerca de un bosque mágico, en perfecta armonía:",
                     "Once upon a time, there were three villages that lived near a magical forest in perfect harmony:"),
 ("NAR", None, None, "-El pueblo de la alegría, donde bailaban todo el día.",
                     "-The Village of Joy, where they danced all day, every girl and every boy."),
 ("AC", "Los HABITANTES del pueblo de la ALEGRIA, saludan al público", "The VILLAGERS of the Village of JOY wave to the audience"),
 ("NAR", None, None, "-El pueblo de la amistad, trabajando siempre en solidaridad.",
                     "-The Village of Friendship, where they always worked hand in hand, the friendliest village in all the land."),
 ("AC", "Los HABITANTES del pueblo de la AMISTAD, saludan al público", "The VILLAGERS of the Village of FRIENDSHIP wave to the audience"),
 ("NAR", None, None, "Y por último, el pueblo de la generosidad, lleno de simpatía y bondad.",
                     "And last of all, the Village of Generosity, full of warmth and goodness, as kind as can be."),
 ("AC", "Los HABITANTES del pueblo de la GENEROSIDAD, saludan al público", "The VILLAGERS of the Village of GENEROSITY wave to the audience"),
 ("NAR", None, None, "Todos sus habitantes vivían alegres, felices\ny cómo no… comían perdices.\nPero las brujas y brujos que vivían en el bosque,\nhicieron una visita a los pueblos, en plena noche.",
                     "Everyone who lived there was cheerful and glad,\nand, of course... they lived the happiest life anyone had.\nBut the witches and wizards who lived in the wood\ncame to the villages at night, up to no good."),
 ("AC", "Las BRUJAS Y BRUJOS, sacan la cabeza de su escondrijo", "The WITCHES and WIZARDS pop their heads out from their hiding place"),
 ("NAR", None, None, "Llenos de envidia, malas energías y crueldad,\nlanzaron un maleficio, para que los pueblos vivieran sin felicidad.",
                     "Full of envy, bad energy and spite,\nthey cast a curse so the villages would be unhappy, day and night."),
 ("AC", "Las BRUJAS Y BRUJOS van hacia el proscenio y hablan, desafiantes, al público", "The WITCHES and WIZARDS move to the front of the stage and speak defiantly to the audience"),
 ("MUS", 1),
 ("BRUJAS", None, None, "(Enfadadas) ¡No puede ser... estos pueblos son demasiado felices!", "(Angry) This can't be... these villages are far too happy!"),
 ("BRUJOS", None, None, "(Enfadados) Hagamos un conjuro para que estén enfadados y tristes.", "(Angry) Let's cast a spell to make them angry and sad."),
 ("BRUJAS", None, None, "¡Sí!", "Yes!"),
 ("BB", None, None, "(Riendo maliciosamente) Ja, ja, ja...", "(Laughing wickedly) Ha, ha, ha..."),
 ("MUS", 1),
 ("AC", "Empiezan a preparar el conjuro. Una BRUJA y un BRUJO, entran en escena una gran olla o caldero y todos harán la mímica de ir introduciendo cosas",
        "They start to brew the spell. One WITCH and one WIZARD bring a big pot or cauldron on stage, and everyone mimes dropping things into it"),
 ("BB", None, None, "Babas de ranas, ojos de babosa y... humos de ciudad,\nque desaparezca… la felicidad.",
                    "Frog drool, slug eyes and... city smog,\nlet happiness vanish... into the fog!"),
 ("BRUJOS", None, None, "¡Ya está!", "There! It's done!"),
 ("BRUJAS", None, None, "¡El hechizo, está listo! (Riendo) ja, ja, ja…", "The spell is ready! (Laughing) Ha, ha, ha..."),
 ("BB", None, None, "Vamos a esparcirlo… ¡ya!", "Let's go spread it... now!"),
 ("MUS", 1),
 ("AC", "La misma BRUJA y BRUJO, se encargan de sacar la olla fuera de escena. Una vez vuelven, todos harán como un “trenecito” para ir a esconderse, en varios grupos, detrás de los matorrales del bosque",
        "The same WITCH and WIZARD carry the pot offstage. When they come back, they all form a little “choo-choo train” and go hide, in several groups, behind the bushes of the forest"),
]),
("escena-2", "Escena 2", "Scene 2", [
 ("NAR", None, None, "Las brujas y los brujos esperaron que llegaran al bosque los habitantes del pueblo de la alegría y desde su escondrijo lanzarles su maleficio, ese mismo día.",
                     "The witches and wizards waited, hidden away, for the Village of Joy to come to the forest, so they could cast their curse on them that very same day."),
 ("LUGAR", "Pueblo de la Alegría", "Village of Joy"),
 ("MUS", 2),
 ("AC", "Acompañados de la música del track 2, entran a escena los HABITANTES del pueblo de la ALEGRIA que bailarán una coreografía donde se represente la alegría",
        "To the music of track 2, the VILLAGERS of the Village of JOY come on stage and dance a routine that shows joy"),
 ("AC", "Al acabarse la música, Las BRUJAS Y BRUJOS salen de su escondrijo y lanzan su maleficio a los HABITANTES del pueblo de la alegría",
        "When the music ends, the WITCHES and WIZARDS come out of hiding and cast their curse on the VILLAGERS of the Village of Joy"),
 ("BB", None, None, "Tris, tras... tris, tras... ¡la alegría desaparecerá!", "Zip, zap... zip, zap... joy will disappear!"),
 ("AC", "Las BRUJAS Y BRUJOS, vuelven a esconderse, rápidamente, en su escondrijo", "The WITCHES and WIZARDS quickly hide again"),
 ("AC", "LOS HABITANTES del pueblo de la ALEGRÍA, muy tristes se miran entre ellos", "The VILLAGERS of the Village of JOY look at one another, very sad"),
 ("ALE", "Habitantes 1 y 2", "Villagers 1 and 2", "¿Qué nos ha pasado?", "What happened to us?"),
 ("ALE", "Habitantes 3 y 4", "Villagers 3 and 4", "¡Estamos muy tristes!", "We're so sad!"),
 ("ALE", "Todos los habitantes", "All the villagers", "(Muy tristes) ¡Oh! ¡Oh!", "(Very sad) Oh! Oh!"),
 ("AC", "Acompañados de una música, un poco triste, los HABITANTES del pueblo de la ALEGRIA salen de escena muy despacio, para volver a su lugar de inicio. Todos van mirando al suelo, muy tristes",
        "To some slightly sad music, the VILLAGERS of the Village of JOY leave the stage very slowly and go back to where they started. They all walk looking down at the floor, very sad"),
 ("MUS", 3),
]),
("escena-3", "Escena 3", "Scene 3", [
 ("NAR", None, None, "El segundo pueblo en llegar al bosque, para jugar, fue el pueblo de la amistad y las brujas y los brujos, para lanzarle su conjuro... preparados están.",
                     "The second village to come to the forest to play was the Village of Friendship... and the witches and wizards were ready to cast their spell on them that day."),
 ("BB", None, None, "(Saliendo de su escondrijo. Ríen con mucha malicia) ¡Ja, ja, ja! Ahora vendrá el pueblo de la amistad. Ja, ja, ja…",
                    "(Coming out of their hiding place. They laugh very wickedly) Ha, ha, ha! Here comes the Village of Friendship. Ha, ha, ha..."),
 ("AC", "Las BRUJAS Y los BRUJOS harán el gesto, cómplice, de pedir silencio al público para volver a esconderse detrás de los matorrales",
        "The WITCHES and WIZARDS make a sly “shh” gesture to the audience and hide behind the bushes again"),
 ("LUGAR", "Pueblo de la Amistad", "Village of Friendship"),
 ("MUS", 4),
 ("AC", "Acompañados de la música del track, entran en escena, los HABITANTES del Pueblo de la AMISTAD que juegan y bailan muy contentos una coreografía que represente la amistad",
        "To the music, the VILLAGERS of the Village of FRIENDSHIP come on stage, playing and dancing very happily to a routine that shows friendship"),
 ("AC", "Al acabarse la música, las BRUJAS Y BRUJOS salen de su escondrijo y lanzan su maleficio al pueblo de la amistad",
        "When the music ends, the WITCHES and WIZARDS come out of hiding and cast their curse on the Village of Friendship"),
 ("BB", None, None, "Tris, tras... tris, tras... ¡la amistad desaparecerá!", "Zip, zap... zip, zap... friendship will disappear!"),
 ("AC", "Las BRUJAS Y BRUJOS, vuelven a esconderse rápidamente en su escondrijo", "The WITCHES and WIZARDS quickly hide again"),
 ("AC", "Los HABITANTES del PUEBLO de La AMISTAD, muy tristes se miran entre ellos", "The VILLAGERS of the Village of FRIENDSHIP look at one another, very sad"),
 ("AMI", "Habitantes", "Villagers", "¿Qué nos ha pasado?", "What happened to us?"),
 ("AMI", "Habitante 1", "Villager 1", "(Al HABITANTE 2) Ya no quiero ser tu amigo.", "(To VILLAGER 2) I don't want to be your friend anymore."),
 ("AMI", "Habitante 2", "Villager 2", "(Al HABITANTE 1) Ni yo... tampoco.", "(To VILLAGER 1) Well... me neither."),
 ("AC", "Los NIÑOS 1 y 2 enseñan sus lenguas, en señal de burla o enfado", "CHILDREN 1 and 2 stick their tongues out at each other, teasing or angry"),
 ("AMI", "Habitante 3", "Villager 3", "(Al HABITANTE 4) Ya no quiero ser tu amigo.", "(To VILLAGER 4) I don't want to be your friend anymore."),
 ("AMI", "Habitante 4", "Villager 4", "(Al HABITANTE 3) Ni yo... tampoco.", "(To VILLAGER 3) Well... me neither."),
 ("AC", "Los HABITANTES 3 y 4 enseñan sus lenguas, en señal de burla y enfado", "VILLAGERS 3 and 4 stick their tongues out at each other, teasing and angry"),
 ("AC", "Acompañados de una música, un poco triste, los HABITANTES del pueblo de la AMISTAD salen de escena muy despacio, para volver a su lugar de inicio. Todos van mirando al suelo, muy tristes",
        "To some slightly sad music, the VILLAGERS of the Village of FRIENDSHIP leave the stage very slowly and go back to where they started. They all walk looking down at the floor, very sad"),
 ("MUS", 3),
]),
("escena-4", "Escena 4", "Scene 4", [
 ("NAR", None, None, "El último pueblo en llegar al bosque repartiendo bondad fueron los habitantes del pueblo de la generosidad.",
                     "The last to come to the forest, spreading kindness all around, was the Village of Generosity, the kindest village to be found."),
 ("BB", None, None, "(Ríen con mucha malicia) ¡Ja, ja, ja! Ahora vendrá el pueblo de la generosidad.", "(They laugh very wickedly) Ha, ha, ha! Here comes the Village of Generosity."),
 ("AC", "Las BRUJAS Y los BRUJOS harán el gesto, cómplice, de pedir silencio al público para esconderse, por última vez, detrás de los matorrales",
        "The WITCHES and WIZARDS make a sly “shh” gesture to the audience and hide behind the bushes, for the very last time"),
 ("LUGAR", "Pueblo de la Generosidad", "Village of Generosity"),
 ("MUS", 5),
 ("AC", "Acompañados de la música del track 5, entran en escena los HABITANTES del Pueblo de la GENEROSIDAD, que comen y comparten un helado, muy contentos, al ritmo de la música representando una pequeña coreografía",
        "To the music of track 5, the VILLAGERS of the Village of GENEROSITY come on stage, very happily eating and sharing ice cream to the beat of the music, in a little dance routine"),
 ("AC", "Al acabarse la música, las BRUJAS Y BRUJOS salen de su escondrijo y lanzan su maleficio al Pueblo de la Generosidad",
        "When the music ends, the WITCHES and WIZARDS come out of hiding and cast their curse on the Village of Generosity"),
 ("BB", None, None, "Tris, tras... tris, tras... ¡la generosidad desaparecerá!", "Zip, zap... zip, zap... generosity will disappear!"),
 ("AC", "Las BRUJAS Y BRUJOS vuelven a esconderse, rápidamente, en su escondrijo", "The WITCHES and WIZARDS quickly hide again"),
 ("GEN", "Habitantes", "Villagers", "(Muy tristes se miran entre ellos) ¿Qué nos ha pasado?", "(Looking at one another, very sad) What happened to us?"),
 ("GEN", "Habitante 1", "Villager 1", "(Al HABITANTE 2) Ya no te quiero dar helado.", "(To VILLAGER 2) I don't want to give you any ice cream anymore."),
 ("GEN", "Habitante 2", "Villager 2", "(Al HABITANTE 1) Ni yo a ti... tampoco.", "(To VILLAGER 1) Well... I won't give you any either."),
 ("GEN", "Habitante 3", "Villager 3", "(Al HABITANTE 4) Ya no te quiero dar helado.", "(To VILLAGER 4) I don't want to give you any ice cream anymore."),
 ("GEN", "Habitante 4", "Villager 4", "(Al HABITANTE 3) Ni yo a ti... tampoco.", "(To VILLAGER 3) Well... I won't give you any either."),
 ("AC", "Todos los HABITANTES del pueblo de la GENEROSIDAD sacan sus lenguas, en señal de burla y enfado", "All the VILLAGERS of the Village of GENEROSITY stick their tongues out, teasing and angry"),
 ("AC", "Acompañados de una música, un poco triste, salen de escena los HABITANTES del pueblo de GENEROSIDAD, muy despacio, para volver a su lugar de inicio. Todos van mirando al suelo, muy tristes",
        "To some slightly sad music, the VILLAGERS of the Village of GENEROSITY leave the stage very slowly and go back to where they started. They all walk looking down at the floor, very sad"),
 ("MUS", 3),
 ("NAR", None, None, "Las brujas y brujos, de su escondrijo salieron, y desde allí celebraron que la victoria, por fin, consiguieron.",
                     "The witches and wizards came out from where they hid, and they cheered for the victory they had finally won... yes, they did!"),
 ("AC", "Las BRUJAS y BRUJOS, salen de su escondrijo y vuelven a hacer el “trenecito” de antes para colocarse en el proscenio y volver a mirar desafiantes al público, riendo muy fuerte, confiados en su victoria. Después saldrán de escena por el lado derecho",
        "The WITCHES and WIZARDS come out of hiding and form the same “choo-choo train” as before to line up at the front of the stage, where once again they look defiantly at the audience, laughing very loudly, sure of their victory. Then they leave on the right side"),
 ("BB", None, None, "(Ríen con mucha malicia) ¡Ja, ja, ja!", "(They laugh very wickedly) Ha, ha, ha!"),
 ("BRUJAS", None, None, "A nuestra cueva volvamos… ¡ya!", "Back to our cave we go... right now!"),
 ("BRUJOS", None, None, "(Eufóricos) ¡Hemos acabado con la felicidad!", "(Overjoyed) We've put an end to happiness!"),
 ("BB", None, None, "(Ríen con mucha malicia) ¡Ja, ja, ja!", "(They laugh very wickedly) Ha, ha, ha!"),
 ("MUS", 1),
]),
("escena-5", "Escena 5", "Scene 5", [
 ("NAR", None, None, "Los pueblos de la alegría, la amistad y la generosidad estaban tristes y desesperados porque habían perdido la felicidad que era, para ellos, su tesoro más preciado. Para buscar una solución, las personas más sabias, en el bosque se reunieron y esto que ahora veréis, fue lo que concluyeron.",
                     "The Villages of Joy, Friendship and Generosity were sad and full of despair, because they had lost their happiness, which was, for them, their most precious treasure. To find a solution, the wisest people met in the forest that day, and now you will see what they had to say."),
 ("MUS", 6),
 ("AC", "Las PERSONAS SABIAS, entran en escena y caminan preocupadas, buscando una solución para su problema; que no es fácil de encontrar. Desesperados se colocan en el centro de la escena",
        "The WISE PEOPLE come on stage and walk around, worried, looking for a solution to their problem, which is not easy to find. In despair, they gather in the center of the stage"),
 ("SABIAS", "Personas sabias 1 y 2", "Wise People 1 and 2", "¿Qué nos ha pasado?", "What happened to us?"),
 ("SABIAS", "Personas sabias 3 y 4", "Wise People 3 and 4", "¿Cómo podemos recuperar la felicidad de nuestros pueblos?", "How can we bring happiness back to our villages?"),
 ("AC", "Las PERSONAS SABIAS, se encogen de hombros para dar a entender que no encuentran ninguna solución para su gran problema",
        "The WISE PEOPLE shrug their shoulders to show that they cannot find any solution to their big problem"),
]),
("escena-6", "Escena 6", "Scene 6", [
 ("NAR", None, None, "Cuando de repente aparecieron del bosque mágico, unas hadas y unos duendes y acercándose a la gente sabia de cada pueblo, esto les dijeron, impacientes…",
                     "Then suddenly, from the magical forest, some fairies and elves came near; they hurried up to the wise people of each village and said, for all to hear..."),
 ("MUS", 7),
 ("AC", "Acompañados de una música alegre entran, por un lado, un grupo de HADAS que rodean a las PERSONAS SABIAS y se colocan a un lado en la escena. Poco después y por el otro lado, entrarán un grupo de DUENDES que también rodean a las PERSONAS SABIAS y se sitúan al lado contrario al de las HADAS",
        "To cheerful music, a group of FAIRIES comes in from one side, circles around the WISE PEOPLE and stands on one side of the stage. A little later, a group of ELVES comes in from the other side, also circles around the WISE PEOPLE and stands on the side opposite the FAIRIES"),
 ("HD", "Duendes y hadas", "Elves and Fairies", "Hemos venido a ayudaros.", "We have come to help you."),
 ("SABIAS", "Personas sabias 1 y 2", "Wise People 1 and 2", "(Con gran sorpresa) ¡Oh, unas hadas!", "(Very surprised) Oh, fairies!"),
 ("SABIAS", "Personas sabias 3 y 4", "Wise People 3 and 4", "(Con gran sorpresa) ¡Oh, unos duendes!", "(Very surprised) Oh, elves!"),
 ("SABIAS", "Todas las personas sabias", "All the Wise People", "¡¡¡Gualaaaa!!!", "Wooooow!!!"),
 ("HADAS", None, None, "Estáis bajo el hechizo de unas brujas y brujos malos.", "You are under the spell of some wicked witches and wizards."),
 ("SABIAS", "Todas las personas sabias", "All the Wise People", "¿Y qué podemos hacer?", "So what can we do?"),
 ("DUENDES", None, None, "Esta noche iremos a la cueva de las brujas y brujos...", "Tonight we will go to the cave where the witches and wizards live..."),
 ("HADAS", None, None, "Cuando estén dormidos, juntos bailaremos.", "And while they're asleep, we'll all dance as one."),
 ("HD", "Duendes y hadas", "Elves and Fairies", "Y el maleficio romperemos.", "And the curse will be undone!"),
 ("SABIAS", "Personas sabias 1 y 2", "Wise People 1 and 2", "¡Muchas gracias!", "Thank you so much!"),
 ("SABIAS", "Personas sabias 3 y 4", "Wise People 3 and 4", "¡Así lo haremos!", "That's just what we'll do!"),
 ("AC", "Las HADAS y los DUENDES salen de escena, cada cual por dónde han entrado en escena y siempre acompañados de la misma música que se ha usado para su entrada",
        "The FAIRIES and the ELVES leave the stage, each group the way it came in, always to the same music that played when they entered"),
 ("MUS", 7),
 ("NAR", None, None, "Las personas sabias de cada pueblo, al oír a las hadas y a los duendes, llenos de esperanza, fueron corriendo a explicarlo todo a sus vecinos, sin tardanza.",
                     "When the wise people of each village heard the fairies and the elves, they were filled with hope, you see, and they ran to tell their neighbors everything, as fast as can be."),
 ("AC", "Los HABITANTES de los pueblos se levantan, de espaldas al público, para escuchar a sus personas sabias, que se han colocado en el proscenio para hablar con ellos",
        "The VILLAGERS stand up, with their backs to the audience, to listen to their wise people, who have moved to the front of the stage to speak to them"),
]),
("escena-7", "Escena 7", "Scene 7", [
 ("SABIAS", "Personas sabias 1 y 2", "Wise People 1 and 2", "¡Escuchad, escuchad! ¡Unas hadas y unos duendes nos vendrán a ayudar!", "Listen, listen! Some fairies and elves are coming to help us!"),
 ("PUEBLOS", None, None, "¡Fantástico!", "Fantastic!"),
 ("SABIAS", "Personas sabias 3 y 4", "Wise People 3 and 4", "Bailaremos, bailaremos y el maleficio romperemos.", "We will dance, we will dance, and the curse won't stand a chance!"),
 ("PUEBLOS", None, None, "Bailaremos, bailaremos y el maleficio romperemos. ¡Viva!", "We will dance, we will dance, and the curse won't stand a chance! Hooray!"),
 ("SABIAS", "Todas las personas sabias", "All the Wise People", "Ahora todo el mundo a esconderse. (Hacen el gesto, típico, para pedir silencio, con el dedo en la boca) ¡Spppp!",
                                                       "Now, everybody, go and hide! (They make the usual “shh” gesture, with a finger to their lips) Shhhh!"),
 ("AC", "Los HABITANTES de los pueblos se agachan y guardan silencio. Las PERSONAS SABIAS, de cada pueblo, salen de escena y se reparten en dos grupos: el grupo primero irá junto a las HADAS y el segundo, con los DUENDES",
        "The VILLAGERS crouch down and keep quiet. The WISE PEOPLE of each village leave the stage and split into two groups: the first group goes with the FAIRIES, and the second, with the ELVES"),
 ("NAR", None, None, "Aquella noche los habitantes, a la cueva subieron tranquilamente. Mientras las brujas y los brujos, dormían plácidamente. ¡Silencio! porque en el interior del bosque, impacientes, les esperaban, para romper el maleficio, las hadas y los duendes.",
                     "That night the villagers climbed up to the cave, as quiet as could be, while the witches and the wizards slept so peacefully. Quiet! Because deep inside the forest, eager to break the spell, the fairies and the elves were waiting for them as well."),
 ("MUS", 8),
 ("AC", "Entran en escena las BRUJAS Y Los BRUJOS, que se colocan en el centro de la escena a dormir. Poco después, de puntillas, lo harán las HADAS y los DUENDES, que harán una señal de aviso para que entren las PERSONAS SABIAS acompañadas de todos los HABITANTES de los tres pueblos, que han subido al escenario, también sin hacer ruido. Todos juntos formarán un gran corro alrededor de las BRUJAS y BRUJOS que siguen durmiendo",
        "The WITCHES and WIZARDS come on stage and lie down to sleep in the center. A little later, the FAIRIES and ELVES tiptoe in and give a signal for the WISE PEOPLE to come in, together with all the VILLAGERS of the three villages, who have also come up onto the stage without making a sound. Together, they all form a big circle around the WITCHES and WIZARDS, who are still asleep"),
]),
("escena-8", "Escena 8", "Scene 8", [
 ("DUENDES", None, None, "(Pidiendo silencio) ¡Spppp! No hagáis ruido.", "(Asking for silence) Shhhh! Don't make a sound."),
 ("HADAS", None, None, "A la de tres, empezaremos a bailar.", "On the count of three, we'll start to dance."),
 ("DUENDES", None, None, "Y el maleficio así se romperá.", "And that's how the curse will break."),
 ("HD", None, None, "¿Estáis preparados?", "Are you ready?"),
 ("PUEBLOS", "Pueblos", "All the villagers", "¡¡¡Sí!!!", "Yes!!!"),
 ("HD", None, None, "A la una, a las dos y a las… ¡tres!", "One, two and... three!"),
 ("AC", "Todos los HABITANTES de los tres pueblos, las PERSONAS SABIAS, las HADAS y los DUENDES, empezarán a dar vueltas y bailar para romper el maleficio",
        "All the VILLAGERS of the three villages, the WISE PEOPLE, the FAIRIES and the ELVES start to circle around and dance to break the curse"),
 ("MUS", 9),
 ("AC", "Al acabar la música, todos los HABITANTES, las PERSONAS SABIAS, las HADAS y los DUENDES, se abrirán hacia los lados de la escena, convirtiendo el corro en un semicírculo, dejando a la vista del público a las BRUJAS y BRUJOS, que empiezan a despertar",
        "When the music ends, all the VILLAGERS, the WISE PEOPLE, the FAIRIES and the ELVES spread out toward the sides of the stage, turning the circle into a half circle, so the audience can see the WITCHES and WIZARDS, who are starting to wake up"),
 ("BB", None, None, "(Despertando. Furiosos) ¿Qué hacéis aquí?", "(Waking up. Furious) What are you doing here?"),
 ("AC", "Las BRUJAS Y BRUJOS intentan lanzar, con sus manos, un hechizo", "The WITCHES and WIZARDS try to cast a spell with their hands"),
 ("BB", None, None, "(Lanzando su hechizo maligno) ¡¡¡Chasss!!!", "(Casting their wicked spell) Zaaap!!!"),
 ("AC", "Las BRUJAS Y BRUJOS, miran sus manos y se dan cuenta de que ya no tienen poderes malignos", "The WITCHES and WIZARDS look at their hands and realize that they have no wicked powers anymore"),
 ("BRUJAS", None, None, "(Preocupadas) ¿Qué nos ha pasado?", "(Worried) What happened to us?"),
 ("BRUJOS", None, None, "(Preocupados) ¿Ya no somos malos?", "(Worried) So we're not bad anymore?"),
 ("DUENDES", None, None, "¡No! Hemos roto el maleficio.", "No! We have broken the curse."),
 ("HADAS", None, None, "A partir de ahora, seréis buenos.", "From now on, you will be good."),
 ("BB", None, None, "(Mimosos a los HABITANTES) ¿Y podremos ser vuestros amigos?", "(Sweetly, to the VILLAGERS) And can we be your friends?"),
 ("PHD", "Todos los habitantes, hadas y duendes", "All the villagers, fairies and elves", "¡Claro que sí!", "Of course you can!"),
 ("BB", None, None, "¡Viva!", "Hooray!"),
 ("SABIAS", "Sabios y sabias", "Wise People", "¡Viva!", "Hooray!"),
 ("PUEBLOS", None, None, "¡A bailar para celebrar nuestra felicidad!", "Let's dance to celebrate our happiness!"),
 ("NAR", None, None, "Y así fue como, con la suma de la energía positiva, que juntos consiguieron los tres pueblos, con la ayuda de las hadas y los duendes, pudieron vencer a la negatividad y la maldad de las brujas y brujos… insolentes.\nY vivieron muy felices y comieron perdices.\nY colorín, colorado esta obra de teatro… se ha acabado.",
                     "And that is how, with all the positive energy the three villages gathered together, and with the help of the fairies and the elves, they defeated the negativity and the wickedness of those rude, boastful witches and wizards.\nAnd they all lived happily ever after.\nAnd snip, snap, snout... our play is all played out."),
 ("MUS", 10),
 ("FIN", "Telón", "Curtain"),
]),
]

# Erratas corregidas en el texto en español. Nada más se cambió.
NOTAS_ERRATAS = [
 ("Escena 1, acotación", "«para ir esconderse» → «para ir a esconderse»"),
 ("Escena 2, acotaciones", "«que bailaran un coreografía» → «que bailarán una coreografía»; «y lazan su maleficio a los HABITANTES pueblo de la alegría» → «y lanzan su maleficio a los HABITANTES del pueblo de la alegría»"),
 ("Escenas 3 y 4, acotaciones", "«detrás los matorrales» → «detrás de los matorrales» (dos veces)"),
 ("Escena 3, acotación", "«Los NIÑOS 1 y 2 4 enseñan sus lenguas» → «Los NIÑOS 1 y 2 enseñan sus lenguas»"),
 ("Escena 4", "acotación: «representado» → «representando»; diálogo: «la generosidad desaparecerá!» → «¡la generosidad desaparecerá!» y «Hemos acabado con la felicidad!» → «¡Hemos acabado con la felicidad!» (faltaba el signo de apertura)"),
 ("Escena 6, acotación", "«por habla con ellos» → «para hablar con ellos»"),
 ("Nombres de los personajes", "el original alterna «BRUJAS y BRUJOS» y «BRUJAS Y BRUJOS», «HADAS y DUENDES» y «HADAS Y DUENDES»; aquí se escribe siempre «y», en minúscula"),
 ("Escena 7", "faltaban los dos puntos tras «PERSONAS SABIAS 1 y 2»; diálogo: «¡Unas hadas y unos duendes nos vendrán a ayudar.» → «…nos vendrán a ayudar!»; acotaciones: «y el segundo, - con los DUENDES» → «y el segundo, con los DUENDES»; «lo harán- las HADAS» → «lo harán las HADAS»; «formaran» → «formarán»"),
 ("Escena 8", "acotaciones: «empezaran» → «empezarán»; «las BRUJAS i BRUJOS» → «las BRUJAS y BRUJOS»; diálogo: «Chasss!!!» → «¡¡¡Chasss!!!»"),
]

# Notas del traductor: (título_en, nota_en, título_es, nota_es)
NOTAS_TRAD = [
 ("Rhyme",
  "Where the original rhymes (the Narrator's verses, the spell, “bailaremos… romperemos”), the English also rhymes, so the lines are just as easy for children to remember. In a few verses the rhyme needed a few extra words: “every girl and every boy” (Village of Joy), “the friendliest village in all the land” (Village of Friendship), “up to no good” (the night visit), “yes, they did!” (the witches' victory) and “into the fog” (the spell). In Scene 7, “and the curse won't stand a chance!” replaces the image of breaking the curse with one that rhymes with “dance”; the meaning is kept. In Scene 7 the narrator's “maleficio” is translated as “spell” (“eager to break the spell”) for the rhyme; everywhere else it is “curse”.",
  "Rima",
  "Donde el original rima (los versos de la narradora, el conjuro, «bailaremos… romperemos»), el inglés también rima, para que a los niños les resulte igual de fácil recordarlo. En algunos versos la rima pidió unas pocas palabras más: «every girl and every boy» (cada niña y cada niño, en el pueblo de la alegría), «the friendliest village in all the land» (el pueblo más amistoso del mundo, en el de la amistad), «up to no good» (con malas intenciones, en la visita nocturna), «yes, they did!» (¡sí, señor!, en la victoria de las brujas y brujos) e «into the fog» (en la niebla, en el conjuro). En la escena 7, «and the curse won't stand a chance!» (y el maleficio no tendrá ninguna oportunidad) sustituye la imagen de romper el maleficio por otra que rima con «dance» (bailar); el sentido se conserva. En la narración de la escena 7, «maleficio» se traduce «spell» para la rima; en el resto de la obra es «curse»."),
 ("«Tris, tras» → “Zip, zap”",
  "Short magic words with the same rhythm, easy for English-speaking children to say together. “¡¡¡Chasss!!!”, the witches' and wizards' failed spell in Scene 8, becomes “Zaaap!!!”, so the two sounds match.",
  "«Tris, tras» → «Zip, zap»",
  "Palabras mágicas cortas, con el mismo ritmo, fáciles de decir a coro para niños que hablan inglés. «¡¡¡Chasss!!!», el hechizo fallido de la escena 8, pasa a «Zaaap!!!», para que los dos sonidos vayan juntos."),
 ("The spell",
  "“Babas de ranas, ojos de babosa y... humos de ciudad, / que desaparezca… la felicidad” becomes “Frog drool, slug eyes and... city smog, / let happiness vanish... into the fog!”: the three ingredients are kept, and the spell rhymes, as it does in Spanish.",
  "El conjuro",
  "«Babas de ranas, ojos de babosa y... humos de ciudad, / que desaparezca… la felicidad» pasa a «Frog drool, slug eyes and... city smog, / let happiness vanish... into the fog!» (babas de rana, ojos de babosa y… humo de ciudad, / ¡que la felicidad desaparezca… en la niebla!): se mantienen los tres ingredientes y el conjuro rima, como en español."),
 ("«Comían perdices» and «colorín, colorado»",
  "These traditional Spanish story formulas have no literal English equivalent. In Scene 1, “y cómo no… comían perdices” becomes “and, of course... they lived the happiest life anyone had”, which keeps the comic pause and the rhyme. At the end, “y vivieron muy felices y comieron perdices” becomes the traditional “and they all lived happily ever after”, and “colorín, colorado” becomes “snip, snap, snout... our play is all played out”, adapted from the folktale ending “snip, snap, snout, this tale's told out”, known in English from translations of Norwegian folktales.",
  "«Comían perdices» y «colorín, colorado»",
  "Estas fórmulas tradicionales no tienen equivalente literal en inglés. En la escena 1, «y cómo no… comían perdices» pasa a «and, of course... they lived the happiest life anyone had» (y, cómo no…, vivían la vida más feliz del mundo), que conserva la pausa cómica y la rima. Al final, «y vivieron muy felices y comieron perdices» pasa a la fórmula inglesa tradicional «and they all lived happily ever after» (y vivieron felices para siempre), y «colorín, colorado» pasa a «snip, snap, snout... our play is all played out», adaptado del final de cuento «snip, snap, snout, this tale's told out», conocido en inglés por las traducciones de los cuentos populares noruegos."),
 ("Other sounds",
  "“¡¡¡Gualaaaa!!!” becomes “Wooooow!!!” and “¡Spppp!” becomes “Shhhh!”: the sounds English-speaking children use for surprise and for silence.",
  "Otros sonidos",
  "«¡¡¡Gualaaaa!!!» pasa a «Wooooow!!!» y «¡Spppp!» a «Shhhh!»: los sonidos que usan los niños en inglés para la sorpresa y para pedir silencio."),
 ("Vosotros (plural “you”)",
  "The plural “you” used in Spain (“Hemos venido a ayudaros”, “¿Estáis preparados?”) becomes the ordinary English “you”.",
  "Vosotros",
  "El «vosotros» («Hemos venido a ayudaros», «¿Estáis preparados?») se traduce con el «you» normal del inglés."),
 ("Characters",
  "NARRADORA → NARRATOR; BRUJAS → WITCHES; BRUJOS → WIZARDS; HADAS → FAIRIES; DUENDES → ELVES; PERSONAS SABIAS → WISE PEOPLE; HABITANTES → VILLAGERS; NIÑOS (Scene 3) → CHILDREN; PUEBLOS (Scene 8) → ALL THE VILLAGERS; pueblo de la alegría, de la amistad, de la generosidad → Village of Joy, of Friendship, of Generosity. Music cues keep the author's “TRACK” numbering.",
  "Personajes",
  "NARRADORA → NARRATOR; BRUJAS → WITCHES; BRUJOS → WIZARDS; HADAS → FAIRIES; DUENDES → ELVES; PERSONAS SABIAS → WISE PEOPLE; HABITANTES → VILLAGERS; NIÑOS (escena 3) → CHILDREN; PUEBLOS (escena 8) → ALL THE VILLAGERS; pueblo de la alegría, de la amistad, de la generosidad → Village of Joy, of Friendship, of Generosity. Las indicaciones de música conservan la numeración «TRACK» del autor."),
]

T = {
 "es": dict(lang="es", titulo="El bosque mágico", sub="Teatro infantil para toda la escuela",
   autor=f"Obra de {AUTOR}", trad="",
   otro="obra-bosque-magico-en.html", otro_lang="en",
   intro="Tres pueblos felices, unas brujas y unos brujos envidiosos, y unas hadas y unos duendes que saben cómo romper un maleficio: bailando todos juntos. Una obra para toda la escuela, de prekínder a 6.º grado.",
   permiso=f"Publicada en Lumi con autorización de {AUTOR} (octubre de 2026). El texto de la obra pertenece a su autor.",
   reparto="Reparto", mipapel="Mi papel:", todos_op="Todos los papeles", solo="Mostrar solo mis líneas",
   oir="Escuchar", oir_esc="🔊 Escuchar la escena", parar="⏹ Parar", menor="Letra más pequeña", mayor="Letra más grande", imprimir="🖨️ Imprimir",
   th=["Papel", "Grado", "Cómo es", "Líneas"], acot="Acotación", musica="Música", pista="Pista", arriba="↑ Cerrar y volver arriba", ir="Ir a",
   nota="Las acotaciones (en cursiva) indican lo que pasa en el escenario: no se dicen en voz alta. Las tarjetas 🎵 marcan cuándo entra cada pista de música.",
   reparto_nota="Las cantidades son las del autor; todos los grupos pueden crecer para que participe toda la escuela, sin cambiar el texto. Cuando un papel tiene número (Habitante 1, Persona sabia 3…), esa línea la puede decir un niño o un pequeño grupo.",
   pie=f"«El bosque mágico» · Obra de {AUTOR} © 2019 · Publicada en Lumi con autorización del autor · Uso gratuito y sin fines de lucro",
   prod="🎬 Guía de producción: reparto por grados, música, vestuario, escenografía, ensayos y carta a las familias",
   cartel="🖼️ Cartel de la función", web="Página del autor", voz="es-ES", lumi="index-es.html", teatro="teatro-es.html", teatro_txt="← Teatro de Lumi",
   guia="obra-bosque-magico-produccion-es.html", cartel_url="obra-bosque-magico-cartel-es.html",
   menu=[("index-es.html","Inicio"),("grados-es.html","Por grado"),("materias-es.html","Por materia"),("teatro-es.html","Teatro")]),
 "en": dict(lang="en", titulo="El bosque mágico", sub="The Magical Forest · A children's play for the whole school",
   autor=f"A play by {AUTOR}", trad="English translation: José M. Fernández, with the author's permission",
   otro="obra-bosque-magico-es.html", otro_lang="es",
   intro="Three happy villages, some envious witches and wizards, and some fairies and elves who know how to break a curse: by dancing all together. A play for the whole school, from Pre-K to 6th grade.",
   permiso=f"Published on Lumi with the permission of {AUTOR} (October 2026). The text of the play belongs to its author.",
   reparto="Cast", mipapel="My part:", todos_op="All parts", solo="Show only my lines",
   oir="Listen", oir_esc="🔊 Listen to the scene", parar="⏹ Stop", menor="Smaller text", mayor="Bigger text", imprimir="🖨️ Print",
   th=["Part", "Grade", "What they are like", "Lines"], acot="Stage direction", musica="Music", pista="Track", arriba="↑ Close and back to top", ir="Go to",
   nota="Stage directions (in italics) tell what happens on stage: they are not read aloud. The 🎵 cards show when each music track starts.",
   reparto_nota="These are the author's numbers; every group can grow so the whole school takes part, without changing the text. When a part has a number (Villager 1, Wise Person 3...), that line can be said by one child or by a small group.",
   pie=f"“El bosque mágico” (The Magical Forest) · A play by {AUTOR} © 2019 · English translation published on Lumi with the author's permission · Free, non-commercial use",
   prod="🎬 Production guide: cast by grade, music, costumes, sets, rehearsals and family letter",
   cartel="🖼️ Show poster", web="Author's website", voz="en-US", lumi="index.html", teatro="teatro.html", teatro_txt="← Lumi Theater",
   guia="obra-bosque-magico-produccion-en.html", cartel_url="obra-bosque-magico-cartel-en.html",
   menu=[("index.html","Home"),("grados.html","By grade"),("materias.html","By subject"),("teatro.html","Theater")]),
}

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
    try{ localStorage.setItem("bosque-papel", p); }catch(e){}
  }
  try{ var g = localStorage.getItem("bosque-papel"); if(g && sel.querySelector('option[value="'+g+'"]')) sel.value = g; }catch(e){}
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
    var ls = [].slice.call(b.closest("details").querySelectorAll(".linea")).filter(function(l){ return getComputedStyle(l).display !== "none"; });
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

def nombre(p, L): return PAPELES[p][3 if L == "es" else 4]
def grado(p, L): return PAPELES[p][1 if L == "es" else 2]
def verso(s): return "<br> ".join(e(x) for x in s.split("\n"))
def pista_txt(n, L):
    tit, aut, gen_es, gen_en = PISTAS[n]
    if L == "en": tit = PISTA_EN.get(n, tit)
    return f"{tit} · {aut}", (gen_es if L == "es" else gen_en)

def cuenta_lineas():
    c = {p: 0 for p in BASE}
    for _, _, _, items in ESCENAS:
        for it in items:
            if it[0] in ("AC", "MUS", "LUGAR", "FIN"): continue
            for m in miembros(it[0]): c[m] += 1
    return c

def pagina(L):
    t = T[L]; c = cuenta_lineas()
    filas = "\n".join(
        f'<tr><td><span class="punto" style="background:{PAPELES[p][0]}" aria-hidden="true"></span>{e(nombre(p,L))}</td><td>{e(grado(p,L))}</td><td>{e(PAPELES[p][5 if L=="es" else 6])}</td><td>{c[p]}</td></tr>'
        for p in BASE)
    opciones = "".join(f'<option value="{p}">{e(nombre(p,L))} · {e(grado(p,L))}</option>' for p in BASE)
    escenas = []
    for eid, tes, ten, items in ESCENAS:
        cuerpo = []
        for it in items:
            k = it[0]
            if k == "AC":
                cuerpo.append(f'  <p class="acot"><span class="sr">{e(t["acot"])}: </span>({e(it[1 if L=="es" else 2])})</p>')
            elif k == "FIN":
                cuerpo.append(f'  <p class="lugar">{e(it[1 if L=="es" else 2])}</p>')
            elif k == "MUS":
                tit, gen = pista_txt(it[1], L)
                cuerpo.append(f'  <p class="mus"><span aria-hidden="true">🎵 </span>{e(t["musica"])}: {e(t["pista"])} {it[1]} <small>· {e(tit)} ({e(gen)})</small></p>')
            elif k == "LUGAR":
                cuerpo.append(f'  <p class="lugar">({e(it[1 if L=="es" else 2])})</p>')
            else:
                p, et_es, et_en, tx_es, tx_en = it
                et = (et_es if L == "es" else et_en) or nombre(p, L)
                tx = tx_es if L == "es" else tx_en
                cuerpo.append(f'''  <div class="linea" data-papeles="{" ".join(miembros(p))}" style="--c:{PAPELES[p][0]}">
   <div><span class="quien">{e(et)}</span><span class="grado">{e(grado(p,L))}</span><p class="txt">{verso(tx)}</p></div>
   <button type="button" class="oir" aria-label="{e(t["oir"])}: {e(et)}">🔊</button>
  </div>''')
        tit = tes if L == "es" else ten
        escenas.append(f'''<details class="seccion acord" id="{eid}">
 <summary><h2 id="t-{eid}">{e(tit)}</h2></summary>
 <div class="cuerpo">
 <div class="acto-h"><span><button type="button" class="oir-esc">{e(t["oir_esc"])}</button> <button type="button" class="parar">{e(t["parar"])}</button></span></div>
{chr(10).join(cuerpo)}
 <p class="arriba"><a href="#contenido" class="cerrar">{e(t["arriba"])}</a></p>
 </div>
</details>''')
    anclas = [("reparto", t["reparto"])] + [(a[0], (a[1] if L == "es" else a[2]).split(" · ")[0]) for a in ESCENAS]
    nav = "".join(f'<li><a href="#{a}">{e(x)}</a></li>' for a, x in anclas)
    menu = "\n".join(f'   <a href="{h}"{" aria-current=\"page\"" if h == t["teatro"] else ""}>{e(x)}</a>' for h, x in t["menu"])
    idioma = (f'<span aria-current="true">Español</span><a href="{t["otro"]}" lang="en" hreflang="en">English</a>' if L == "es"
              else f'<a href="{t["otro"]}" lang="es" hreflang="es">Español</a><span aria-current="true">English</span>')
    trad = f'\n  <p style="margin:.2rem 0 0">{e(t["trad"])}</p>' if t["trad"] else ""
    titulo_html = e(t["titulo"]) if L == "es" else f'<span lang="es">{e(t["titulo"])}</span>'
    return f'''<!doctype html>
<!-- «El bosque mágico» · Obra de {AUTOR} © 2019 (www.obrasteatro.com) · Publicada en Lumi con autorización del autor.
     El texto de la obra pertenece a su autor. Diseño de la página: Lumi (José M. Fernández). Generado con herramientas/gen_bosque.py -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["titulo"])}{" (The Magical Forest)" if L=="en" else ""} · Lumi</title>
<meta name="description" content="{e(t["intro"])}">
<meta name="author" content="{AUTOR}">
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
  <h1 id="titulo">{titulo_html}</h1>
  <p class="sub">{e(t["sub"])}</p>
  <p class="autor">{e(t["autor"])}</p>{trad}
  <p>{e(t["intro"])}</p>
  <ul class="enlaces-obra">
   <li><a href="{t["guia"]}">{e(t["prod"])}</a></li>
   <li><a href="{t["cartel_url"]}">{e(t["cartel"])}</a></li>
   <li><a href="{WEB_AUTOR}" target="_blank" rel="noopener noreferrer">{e(t["web"])}: obrasteatro.com</a></li>
  </ul>
  <p class="permiso">{e(t["permiso"])}</p>
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
{chr(10).join(escenas)}
</div></main>
<footer class="pie"><div class="envoltura"><p>{e(t["pie"])}</p><p><a href="{WEB_AUTOR}" target="_blank" rel="noopener noreferrer">www.obrasteatro.com</a></p></div></footer>
<script>{JS}</script>
</body>
</html>
'''

# ------------------------------------------------------------------ texto bilingüe para el autor
def traduccion():
    filas = []
    for eid, tes, ten, items in ESCENAS:
        filas.append(f'<tr class="esc"><th scope="colgroup" colspan="2"><span lang="es">{e(tes)}</span> · <span lang="en">{e(ten)}</span></th></tr>')
        for it in items:
            k = it[0]
            if k == "AC":
                filas.append(f'<tr class="ac"><td lang="es">({e(it[1])})</td><td lang="en">({e(it[2])})</td></tr>')
            elif k == "MUS":
                filas.append(f'<tr class="mu"><td lang="es">MÚSICA: TRACK {it[1]}</td><td lang="en">MUSIC: TRACK {it[1]}</td></tr>')
            elif k == "FIN":
                filas.append(f'<tr class="lu"><td lang="es">{e(it[1])}</td><td lang="en">{e(it[2])}</td></tr>')
            elif k == "LUGAR":
                filas.append(f'<tr class="lu"><td lang="es">({e(it[1].upper())})</td><td lang="en">({e(it[2].upper())})</td></tr>')
            else:
                p, ees, een, tx_es, tx_en = it
                q_es = (ees or nombre(p, "es")).upper().replace(" Y ", " y "); q_en = (een or nombre(p, "en")).upper()
                filas.append(f'<tr><td lang="es"><b>{e(q_es)}:</b> {verso(tx_es)}</td><td lang="en"><b>{e(q_en)}:</b> {verso(tx_en)}</td></tr>')
    notas = "\n".join(f'<li><b>{e(a)}.</b> {e(en)}</li>' for a, en, b, es in NOTAS_TRAD)
    notas_es = "\n".join(f'<li><b>{e(b)}.</b> {e(es)}</li>' for a, en, b, es in NOTAS_TRAD)
    erratas = "\n".join(f'<li><b>{e(a)}:</b> {e(b)}</li>' for a, b in NOTAS_ERRATAS)
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>El bosque mágico · The Magical Forest · Traducción al inglés</title>
<meta name="author" content="{AUTOR}">
<style>
 :root{{--tinta:#1d2a2e;--borde:#c9d6d9;--suave:#f3f7f8;--acento:#194F5A}}
 body{{font-family:Georgia,"Times New Roman",serif;color:var(--tinta);background:#fff;margin:0;line-height:1.5}}
 .hoja{{max-width:1050px;margin:0 auto;padding:2rem 1rem 3rem}}
 h1{{font-size:2rem;margin:0}} h2{{font-size:1.3rem;margin:2rem 0 .5rem;color:var(--acento)}}
 .sub{{font-size:1.15rem;margin:.3rem 0 1rem}}
 table{{width:100%;border-collapse:collapse;table-layout:fixed}}
 th,td{{border-bottom:1px solid var(--borde);padding:.45rem .6rem;vertical-align:top;text-align:left}}
 thead th{{background:var(--suave);font-family:Arial,sans-serif;font-size:.9rem;text-transform:uppercase;letter-spacing:.04em}}
 tr.esc th{{background:var(--acento);color:#fff;font-family:Arial,sans-serif;font-size:1rem;padding:.55rem .6rem}}
 tr.ac td{{font-style:italic;color:#3c5257}}
 tr.mu td,tr.lu td{{font-family:Arial,sans-serif;font-size:.85rem;letter-spacing:.03em;color:#4c3a6e}}
 td b{{font-family:Arial,sans-serif;font-size:.82rem;letter-spacing:.03em}}
 ul{{padding-left:1.2rem}} li{{margin:.3rem 0}}
 .pie{{margin-top:2rem;font-size:.9rem;border-top:1px solid var(--borde);padding-top:.8rem}}
 @media print{{.hoja{{padding:0}} tr{{break-inside:avoid}} h2{{break-after:avoid}}}}
</style>
</head>
<body>
<div class="hoja">
 <h1>El bosque mágico</h1>
 <p class="sub"><span lang="en">The Magical Forest</span> · Teatro infantil · {AUTOR} © 2019</p>
 <p>Texto original en español y traducción al inglés, línea por línea, para la revisión del autor.<br>
 <span lang="en">Original Spanish text and English translation, line by line, for the author's review.</span></p>
 <p>Traducción al inglés: José M. Fernández (Lumi, www.lumi-educa.com), octubre de 2026, sujeta a la aprobación del autor.<br>
 <span lang="en">English translation: José M. Fernández (Lumi, www.lumi-educa.com), October 2026, subject to the author's approval.</span></p>

 <h2>Notas del traductor · <span lang="en">Translator's notes</span></h2>
 <ul lang="es">
{notas_es}
 </ul>
 <ul lang="en">
{notas}
 </ul>

 <h2>Texto · <span lang="en">Text</span></h2>
 <table>
  <caption style="text-align:left;margin-bottom:.4rem">El bosque mágico — español / <span lang="en">English</span></caption>
  <thead><tr><th scope="col">Español</th><th scope="col" lang="en">English</th></tr></thead>
  <tbody>
{chr(10).join(filas)}
  </tbody>
 </table>

 <h2>Erratas corregidas en la versión de Lumi</h2>
 <p>El texto en español es el de la obra, con su puntuación, sus mayúsculas y sus saltos de verso. Solo se corrigieron estas erratas; no se cambió ninguna palabra de los diálogos.</p>
 <ul>
{erratas}
 </ul>
 <h2>Cómo se ve en Lumi</h2>
 <p>En la página interactiva de Lumi, el texto es el mismo. Además, cada personaje tiene un color; las acotaciones aparecen en cursiva; cada «MÚSICA: TRACK» se muestra como una tarjeta con el nombre de la pieza que usted propone; cada línea se puede escuchar en voz alta; y cada niño puede elegir su personaje para ver solo sus líneas. Su nombre figura como autor al principio y al final de cada página, con un enlace a www.obrasteatro.com.</p>
 <p class="pie">«El bosque mágico» · Obra de {AUTOR} © 2019 · www.obrasteatro.com</p>
</div>
</body>
</html>
'''

# Mientras el autor revisa la traducción, obra-bosque-magico-en.html es un aviso
# de «próximamente». Cuando la apruebe, cambiar a True y volver a generar.
EN_PUBLICADO = False

def aviso_en():
    return f'''<!doctype html>
<!-- «El bosque mágico» · Obra de {AUTOR} © 2019 · El guion en inglés se publicará cuando el autor apruebe la traducción. -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>El bosque mágico (The Magical Forest) · Lumi</title>
<meta name="author" content="{AUTOR}">
<link rel="alternate" hreflang="es" href="obra-bosque-magico-es.html">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="lumi.css?v=6">
<style>
.obra-cab{{background:var(--cie);padding:1.4rem 0}}
.obra-cab h1{{font-size:clamp(1.8rem,4.5vw,2.6rem)}}
.aviso-en{{background:#FFF6DF;border-left:6px solid var(--ama);border-radius:10px;padding:1rem 1.2rem;margin:1.2rem 0}}
.enlaces-obra{{display:flex;flex-wrap:wrap;gap:.5rem;margin:.6rem 0 0;padding:0;list-style:none}}
.enlaces-obra a{{display:inline-flex;align-items:center;min-height:44px;padding:.3rem 1rem;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);font-weight:700;text-decoration:none}}
</style>
</head>
<body>
<a class="saltar" href="#contenido">Skip to content</a>
<header class="cabecera">
 <div class="envoltura">
  <a class="marca" href="index.html"><img src="lumi-logo-horizontal.svg" alt="Lumi — home page" width="560" height="240"></a>
  <nav aria-label="Main menu" class="menu">
   <a href="index.html">Home</a>
   <a href="grados.html">By grade</a>
   <a href="materias.html">By subject</a>
   <a href="teatro.html" aria-current="page">Theater</a>
  </nav>
  <div class="idioma" role="group" aria-label="Language"><a href="obra-bosque-magico-es.html" lang="es" hreflang="es">Español</a><span aria-current="true">English</span></div>
 </div>
</header>
<section class="obra-cab" aria-labelledby="titulo">
 <div class="envoltura">
  <p style="margin:0"><a href="teatro.html">← Lumi Theater</a></p>
  <h1 id="titulo"><span lang="es">El bosque mágico</span> (The Magical Forest)</h1>
  <p style="font-weight:700;font-size:1.15rem;margin:.3rem 0 0">A play by {AUTOR}</p>
 </div>
</section>
<main id="contenido" tabindex="-1"><div class="envoltura">
 <div class="aviso-en">
  <p style="margin:0"><strong>English script: coming soon.</strong> The English translation is being reviewed by the author, {AUTOR}. It will be published here as soon as he approves it.</p>
 </div>
 <p>Meanwhile, you can already use:</p>
 <ul class="enlaces-obra">
  <li><a href="obra-bosque-magico-es.html" lang="es" hreflang="es">Script in Spanish</a></li>
  <li><a href="obra-bosque-magico-produccion-en.html">🎬 Production guide</a></li>
  <li><a href="obra-bosque-magico-cartel-en.html">🖼️ Show poster</a></li>
  <li><a href="{WEB_AUTOR}" target="_blank" rel="noopener noreferrer">Author's website: obrasteatro.com</a></li>
 </ul>
</div></main>
<footer class="pie"><div class="envoltura"><p>“El bosque mágico” (The Magical Forest) · A play by {AUTOR} © 2019 · Published on Lumi with the author's permission</p><p><a href="{WEB_AUTOR}" target="_blank" rel="noopener noreferrer">www.obrasteatro.com</a></p></div></footer>
</body>
</html>
'''

if __name__ == "__main__":
    for L in ("es", "en"):
        with open(os.path.join(AQUI, f"obra-bosque-magico-{L}.html"), "w", encoding="utf-8") as f:
            f.write(pagina(L) if (L == "es" or EN_PUBLICADO or "--completo" in sys.argv) else aviso_en())
    if "--traduccion" in sys.argv:
        destino = sys.argv[sys.argv.index("--traduccion") + 1] if len(sys.argv) > sys.argv.index("--traduccion") + 1 else AQUI
        with open(os.path.join(destino, "El-bosque-magico-traduccion-ingles.html"), "w", encoding="utf-8") as f:
            f.write(traduccion())
    print("ok")
