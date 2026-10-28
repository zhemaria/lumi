"""
Generador del guion interactivo de «El Fénix sobre el Lago» (español e inglés).
Obra de José M. Fernández. Produce obra-fenix-lago-es.html y obra-fenix-lago-en.html.
Uso: python3 gen_fenix.py
"""
import html, json, os

AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = lambda s: html.escape(s, quote=False)

# ------------------------------------------------------------------ papeles
# clave: (color, grado_es, grado_en, nombre_es, nombre_en, descripcion_es, descripcion_en)
PAPELES = {
 "NAR1":  ("#6B4FA0", "6.º", "6th", "Narrador 1", "Narrator 1", "Cuenta la historia con voz clara y serena.", "Tells the story in a clear, calm voice."),
 "NAR2":  ("#8A63C9", "6.º", "6th", "Narrador 2", "Narrator 2", "Cuenta la historia con voz clara y serena.", "Tells the story in a clear, calm voice."),
 "OLEARY":("#A0522D", "6.º", "6th", "Sra. Catherine O'Leary", "Mrs. Catherine O'Leary", "Vecina de la calle DeKoven que vendía leche. Al final cuenta la verdad sobre la leyenda.", "A DeKoven Street neighbor who sold milk. At the end, she tells the truth about the legend."),
 "JEFE":  ("#B22222", "6.º", "6th", "Bombero Jefe", "Fire Chief", "Habla al público con calma y autoridad: da las reglas de seguridad.", "Speaks to the audience with calm authority and gives the safety rules."),
 "ARQ":   ("#1F5F8B", "6.º", "6th", "Arquitecto", "Architect", "Lidera la reconstrucción con energía y esperanza.", "Leads the rebuilding with energy and hope."),
 "V1":    ("#2E7D4F", "4.º–5.º", "4th–5th", "Vecino 1", "Resident 1", "Vecino que guía a la gente hacia el lago.", "A neighbor who guides people to the lake."),
 "V2":    ("#3C8D5A", "4.º–5.º", "4th–5th", "Vecina 2", "Resident 2", "Quiere volver por sus cosas, pero la convencen de seguir.", "Wants to go back for her things, but is convinced to keep going."),
 "V3":    ("#4A9C67", "4.º–5.º", "4th–5th", "Vecino 3", "Resident 3", "Tranquilo y sensato: recuerda que la vida vale más que las cosas.", "Calm and wise: reminds others that lives matter more than things."),
 "V4":    ("#58AB74", "4.º–5.º", "4th–5th", "Vecina 4", "Resident 4", "Da ánimo al ver la Torre de Agua en pie.", "Gives hope when she sees the Water Tower still standing."),
 "AGENTE":("#7A5C1E", "4.º–5.º", "4th–5th", "Agente de bienes raíces", "Real estate agent", "Basado en William D. Kerfoot, que puso su famoso letrero entre las ruinas.", "Based on William D. Kerfoot, who put up his famous sign among the ruins."),
 "E4":    ("#2F6F73", "4.º", "4th", "Estudiante de 4.º", "4th grader", "Empieza la frase final.", "Starts the final line."),
 "E5":    ("#3D8A8F", "5.º", "5th", "Estudiante de 5.º", "5th grader", "Termina la frase final.", "Finishes the final line."),
 "VIENTOS":("#5D7B99", "2.º–3.º", "2nd–3rd", "Vientos y chispas (coro)", "Winds and embers (chorus)", "Bailan con cintas: el viento que empuja el fuego.", "Dance with ribbons: the wind that pushes the fire."),
 "RIO":   ("#1E6FB8", "1.º", "1st", "Río Chicago (coro)", "Chicago River (chorus)", "Mueven la larga tela azul del río.", "Move the long blue river cloth."),
 "LLAMAS":("#D35400", "Kínder", "K", "Llamitas (coro)", "Little Flames (chorus)", "Con capas de fieltro rojo y naranja, son el fuego.", "In red and orange felt capes, they are the fire."),
 "ANIMALES":("#8D6E63", "Prekínder", "Pre-K", "Animalitos del establo (coro)", "Barnyard animals (chorus)", "La vaca Daisy, pollitos, corderitos y terneros.", "Daisy the cow, chicks, lambs and calves."),
 "TODOS": ("#194F5A", "Todos", "All", "Todos los grados", "All grades", "Todo el elenco, en coro.", "The whole cast, together."),
}

# ------------------------------------------------------------------ guion
# Cada acto: (id, titulo_es, titulo_en, [ (papel o "AC", texto_es, texto_en) ])
ACTOS = [
("acto-1", "Acto I · La chispa en la calle DeKoven (8 de octubre de 1871)", "Act I · The Spark on DeKoven Street (October 8, 1871)", [
 ("AC", "Música animada de violín o banjo. Al fondo, a la derecha, alumnos de 4.º y 5.º pasean por una acera de tablones. A la izquierda, el establo: los niños de prekínder descansan como animalitos de granja junto a la vaca Daisy.",
        "A lively fiddle or banjo tune plays. Upstage right, 4th and 5th graders stroll along a wooden plank sidewalk. Stage left is the barn: the Pre-K students rest like barnyard animals around Daisy the cow."),
 ("NAR1", "Chicago, 8 de octubre de 1871. Era una de las ciudades que más rápido crecían en el mundo. Pero tenía un gran peligro: ¡casi todo estaba hecho de madera! Las casas, los puentes, las aceras y hasta muchas calles.",
          "Chicago. October 8, 1871. It was one of the fastest-growing cities in the world. But it had a big danger: almost everything was made of wood! Houses, bridges, sidewalks, and even many streets."),
 ("NAR2", "Hacía semanas que casi no llovía. La madera estaba seca como yesca, y un viento fuerte soplaba desde el sudoeste. Bastaba una chispa para desatar una tragedia.",
          "It had hardly rained for weeks. The wood was as dry as kindling, and a strong wind was blowing from the southwest. One spark was all it would take."),
 ("AC", "Los vientos de 2.º y 3.º cruzan el fondo una vez, agitando sus cintas, y salen.", "The 2nd and 3rd grade winds cross upstage once, waving their ribbons, and exit."),
 ("VIENTOS", "¡Fiuuu, fiuuu! ¡Somos el viento del sudoeste!", "Whoosh, whoosh! We are the southwest wind!"),
 ("NAR1", "Esa noche, en un pequeño establo de la calle DeKoven, empezó el fuego. Nadie sabe con certeza cómo. Pero hay una leyenda muy famosa... y así la cuenta la gente.",
          "That night, in a small barn on DeKoven Street, the fire began. No one knows for sure how. But there is a very famous legend... and this is how people tell it."),
 ("AC", "Entra la Sra. O'Leary con un cubo de hojalata y una linterna de utilería con luz LED.", "Mrs. O'Leary enters with a tin pail and a prop lantern with a safe LED light."),
 ("OLEARY", "(Acariciando a Daisy) Hola, bonita. Es hora de ordeñarte. Afuera el viento sopla muy fuerte... Dejaré la lámpara aquí, en el rincón, junto a la paja, para poder ver.",
            "(Patting Daisy) Hello, sweet girl. Time for your milking. The wind is so strong out there... I'll leave my lantern here in the corner, next to the hay, so I can see."),
 ("AC", "El Bombero Jefe da un paso al frente y congela la escena con la mano.", "The Fire Chief steps forward and freezes the scene with a raised hand."),
 ("JEFE", "(Al público) ¡Alto! Primera regla de seguridad: nunca pongas una llama ni algo caliente cerca de cosas que se queman fácilmente, como la paja, el papel o la tela. Las reglas de seguridad existen por una razón.",
          "(To the audience) Stop! Safety rule number one: never put a flame or anything hot near things that burn easily, like hay, paper or cloth. Safety rules exist for a reason."),
 ("AC", "La escena vuelve a moverse, en cámara lenta y cómica.", "The scene unfreezes in comic slow motion."),
 ("NAR2", "Según la leyenda, Daisy movió la pata...", "According to the legend, Daisy kicked her leg..."),
 ("AC", "Daisy sacude suavemente una pata trasera y tumba la linterna.", "Daisy gently kicks a hind leg and knocks over the lantern."),
 ("ANIMALES", "¡Muuu! ¡Pío, pío! ¡Cuidado con el fuego!", "Moo! Peep, peep! Watch out for the fire!"),
 ("AC", "Luz roja parpadeante. Entran las llamitas de kínder moviendo los brazos al ritmo.", "Red lights flicker. The kindergarten flames dance in, moving their arms to the beat."),
 ("LLAMAS", "¡Crac, crac, crac! ¡Somos las llamitas!", "Crackle, crackle, crack! We are the little flames!"),
 ("OLEARY", "(Asustada) ¡Fuego! ¡Fuego en el establo! ¡Ayuda!", "(Frightened) Fire! Fire in the barn! Help!"),
]),
("acto-2", "Acto II · La huida organizada (8 al 10 de octubre)", "Act II · The Orderly Escape (October 8–10)", [
 ("AC", "Los vientos de 2.º y 3.º cruzan el fondo en una fila ondulante con sus cintas, sin correr. Al frente, los niños de 1.º sostienen la larga tela azul del río Chicago y la mueven en ondas. Los animalitos de prekínder, con sus guías, se sientan a la derecha, en la orilla del lago.",
        "The 2nd and 3rd grade winds cross upstage in a wavy line with their ribbons, without running. Downstage, the 1st graders hold the long blue cloth of the Chicago River and move it in waves. The Pre-K animals, with their buddies, sit at stage right, on the lake shore."),
 ("NAR2", "El viento empujaba las llamas de cuadra en cuadra, saltando de techo en techo.", "The wind pushed the flames from block to block, leaping from roof to roof."),
 ("VIENTOS", "¡Fiuuu! ¡Más fuerte, más fuerte!", "Whoosh! Stronger, stronger!"),
 ("RIO", "¡Somos el río Chicago! ¡El fuego no puede cruzarnos!", "We are the Chicago River! The fire can't cross us!"),
 ("NAR1", "Pero el viento llevaba por el aire pedazos de madera encendida. El fuego cruzó el brazo sur del río... y después el río principal, hasta el lado norte de la ciudad.",
          "But the wind carried burning pieces of wood through the air. The fire jumped the South Branch of the river... and then the main river, all the way to the North Side."),
 ("AC", "Las llamitas pasan alrededor de la tela del río, guiadas por sus maestras, y se agachan al otro lado.", "The flames move around the river cloth, guided by their teachers, and crouch down on the other side."),
 ("LLAMAS", "¡Saltamos el río!", "We jumped the river!"),
 ("AC", "Los alumnos de 4.º y 5.º cruzan en diagonal con paso rápido pero ordenado, con carretillas, maletas, mantas y libros.", "The 4th and 5th graders cross diagonally at a quick but orderly pace, carrying wheelbarrows, suitcases, blankets and books."),
 ("V1", "¡El fuego llegó al lado norte! ¡Todos hacia la orilla del lago Michigan!", "The fire has reached the North Side! Everyone to the shore of Lake Michigan!"),
 ("V2", "(Se detiene con una maleta) ¡Quiero volver por mis muebles y mis cartas!", "(Stopping with a suitcase) I want to go back for my furniture and my letters!"),
 ("V3", "(La toma del brazo con calma) ¡No regreses! Las cosas se pueden reponer; las vidas, no. ¡Sigue la ruta hacia el lago!", "(Gently taking her arm) Don't go back! Things can be replaced; lives cannot. Follow the route to the lake!"),
 ("AC", "Un alumno de 6.º levanta al fondo un recorte de la Torre de Agua, de piedra caliza.", "A 6th grader raises a cutout of the limestone Water Tower upstage."),
 ("JEFE", "(Con voz clara, alzando su linterna) ¡Regla de evacuación: caminen, no corran; sigan la ruta y mantengan libres las salidas! ¡Los grandes, tomen de la mano a los pequeños!",
          "(Clearly, raising his lantern) Evacuation rule: walk, don't run; follow the route and keep the exits clear! Big kids, hold the little ones' hands!"),
 ("AC", "Alumnos de 5.º toman de la mano a los de prekínder y los llevan con el grupo.", "5th graders take the Pre-K students by the hand and bring them to the group."),
 ("V4", "(Señalando) ¡Miren la Torre de Agua! ¡Sus muros de piedra siguen en pie! ¡Si nos mantenemos unidos y tranquilos, saldremos adelante!",
        "(Pointing) Look at the Water Tower! Its stone walls are still standing! If we stay together and stay calm, we'll get through this!"),
 ("NAR2", "El fuego ardió más de un día. Por fin, en la noche del 9 de octubre, empezó a llover, y el 10 se apagaron las últimas llamas.",
          "The fire burned for more than a day. At last, on the night of October 9, it began to rain, and on October 10 the last flames went out."),
 ("NAR1", "Cientos de personas murieron, y unas cien mil se quedaron sin casa. Más de diecisiete mil edificios se quemaron.",
          "Hundreds of people died, and about one hundred thousand were left without a home. More than seventeen thousand buildings burned."),
 ("AC", "La luz roja baja poco a poco a un azul oscuro. Las llamitas se sientan, apagadas. Todos quedan a salvo en la orilla del lago.", "The red light slowly fades to dark blue. The flames sit down, put out. Everyone is safe on the lake shore."),
]),
("acto-3", "Acto III · El renacimiento", "Act III · Rising from the Ashes", [
 ("AC", "Los paneles del fondo giran y muestran el Chicago nuevo, de piedra y ladrillo. Entran comerciantes y constructores con martillos de madera, planos y carretillas.",
        "The backdrop panels turn to show the new Chicago of stone and brick. Shopkeepers and builders enter with wooden mallets, blueprints and wheelbarrows."),
 ("ARQ", "¿Rendirnos? ¡Jamás! Una ciudad no está hecha solo de madera y ladrillos. Una ciudad está hecha del valor y del corazón de su gente.",
         "Give up? Never! A city isn't made only of wood and bricks. A city is made of the courage and the heart of its people."),
 ("AC", "El agente de bienes raíces clava un letrero junto a una pequeña caseta de tablas.", "The real estate agent nails a sign next to a little wooden shack."),
 ("AGENTE", "Mi oficina se quemó, pero mi letrero dice la verdad: «Todo perdido, menos la esposa, los hijos y la energía». ¡Mañana empiezo otra vez!",
            "My office burned down, but my sign tells the truth: “All gone but wife, children and energy.” Tomorrow I start again!"),
 ("V1", "De todo el país y del mundo nos envían comida, ropa y mantas. ¡Y desde Inglaterra llegan miles de libros para la primera biblioteca pública gratuita de Chicago!",
        "People across the country and around the world are sending us food, clothes and blankets. And from England, thousands of books are arriving for Chicago's first free public library!"),
 ("ARQ", "Esta vez construiremos mejor. En el centro de la ciudad, ¡nada de casas de madera: solo piedra, ladrillo y hierro! ¡Y más bomberos, mejor preparados!",
         "This time we will build better. In the center of the city, no more wooden houses: only stone, brick and iron! And more firefighters, better prepared!"),
 ("NAR1", "Chicago se reconstruyó tan rápido que el mundo quedó asombrado. Años después, en 1885, aquí se construyó uno de los primeros rascacielos con esqueleto de metal.",
          "Chicago rebuilt so fast that the world was amazed. Years later, in 1885, one of the first skyscrapers with a metal skeleton was built here."),
 ("NAR2", "Y en 1893, apenas veintidós años después del incendio, Chicago recibió al mundo en la Exposición Mundial, con sus palacios blancos: la famosa «Ciudad Blanca».",
          "And in 1893, just twenty-two years after the fire, Chicago welcomed the world to the World's Fair, with its white palaces: the famous “White City.”"),
 ("AC", "Dos alumnos de 6.º despliegan una bandera de Chicago hecha en clase.", "Two 6th graders unfold a Chicago flag made in class."),
 ("NAR1", "Por eso la bandera de Chicago tiene cuatro estrellas rojas. La segunda recuerda el Gran Incendio de 1871, y la tercera, la Exposición Mundial de 1893.",
          "That's why the Chicago flag has four red stars. The second one remembers the Great Fire of 1871, and the third one, the World's Fair of 1893."),
]),
("acto-4", "Acto IV · Reflexión final", "Act IV · Closing Reflection", [
 ("AC", "Todos los grados se reúnen en orden: los pequeños adelante, sentados; los mayores atrás, de pie.", "All grades gather in order: the youngest in front, sitting; the oldest in back, standing."),
 ("JEFE", "El incendio nos dejó lecciones para toda la vida. Primera: respetar las reglas de seguridad, en casa y en la escuela. Segunda: estar preparados: conocer las salidas, no bloquear los pasillos y practicar los simulacros en serio.",
          "The fire left us lessons for a lifetime. First: respect safety rules, at home and at school. Second: be prepared: know the exits, keep the hallways clear and take fire drills seriously."),
 ("OLEARY", "Y ahora les cuento la verdad sobre mí. Durante muchos años, la gente nos culpó a mí y a mi vaca. Pero en 1893, el periodista que inventó la historia de la vaca confesó que no era cierta. Y en 1997, la ciudad de Chicago declaró que yo era inocente. Nadie sabe con certeza cómo empezó el fuego.",
            "And now let me tell you the truth about me. For many years, people blamed me and my cow. But in 1893, the reporter who made up the cow story admitted it wasn't true. And in 1997, the City of Chicago declared me innocent. No one knows for sure how the fire started."),
 ("NAR2", "Por eso, antes de creer una historia, hay que buscar las pruebas.", "So, before you believe a story, look for the evidence."),
 ("OLEARY", "Y la lección más grande que aprendió nuestra ciudad: ninguna caída es para siempre si nos mantenemos unidos.", "And the greatest lesson our city learned: no fall lasts forever if we stand together."),
 ("E4", "Porque del fuego...", "From the fire..."),
 ("E5", "...surgió un Chicago más fuerte, más seguro y más hermoso.", "...rose a Chicago that was stronger, safer and more beautiful."),
 ("TODOS", "(Dando un paso al frente) ¡Siempre alerta, siempre preparados! ¡Unidos superamos cualquier dificultad!", "(Stepping forward) Always alert, always prepared! Together we can overcome anything!"),
 ("AC", "Todos cantan el «Canto del Fénix» y hacen una reverencia por grados, de los más pequeños a los mayores.", "Everyone sings the “Phoenix Chant” and bows by grade, from the youngest to the oldest."),
]),
]

CANTO_ES = ["Si hay humo, no corras:", "camina y avisa;", "ayuda al pequeño", "y en fila, sin prisa.", "Chicago cayó,", "Chicago se alzó:", "¡como el Fénix,", "de nuevo voló!"]
CANTO_EN = ["If there's smoke, don't run,", "walk and tell a grown-up;", "help the little ones,", "and line up, line up!", "Chicago fell,", "Chicago rose:", "like the Phoenix,", "up it goes!"]

T = {
 "es": dict(lang="es", titulo="El Fénix sobre el Lago", sub="La historia del Gran Incendio de Chicago", autor="Obra de José M. Fernández",
   otro="obra-fenix-lago-en.html", otro_txt="English", otro_lang="en",
   intro="Una obra para toda la escuela, de prekínder a 6.º grado. Los mayores llevan los diálogos y la narración; los más pequeños son los animalitos, el fuego, el viento y el río.",
   reparto="Reparto", canto="Canto del Fénix", mipapel="Mi papel:", todos_op="Todos los papeles", solo="Mostrar solo mis líneas",
   oir="Escuchar", oir_acto="🔊 Escuchar el acto", parar="⏹ Parar", menor="Letra más pequeña", mayor="Letra más grande", imprimir="🖨️ Imprimir",
   th=["Papel", "Grado", "Cómo es", "Líneas"], acot="Acotación", arriba="↑ Cerrar y volver arriba", ir="Ir a",
   nota="Las acotaciones (en cursiva) indican lo que pasa en el escenario: no se dicen en voz alta.",
   pie="«El Fénix sobre el Lago» · Obra de José M. Fernández · Licencia CC BY-NC-SA 4.0",
   prod="🎬 Guía de producción: reparto, música, vestuario, escenografía y carta a las familias", voz="es-US", lumi="index-es.html", teatro="teatro-es.html", teatro_txt="← Teatro de Lumi",
   menu=[("index-es.html","Inicio"),("grados-es.html","Por grado"),("materias-es.html","Por materia"),("teatro-es.html","Teatro")]),
 "en": dict(lang="en", titulo="The Phoenix on the Lake", sub="The Story of the Great Chicago Fire", autor="A play by José M. Fernández",
   otro="obra-fenix-lago-es.html", otro_txt="Español", otro_lang="es",
   intro="A play for the whole school, from Pre-K to 6th grade. The older students carry the dialogue and narration; the youngest are the animals, the fire, the wind and the river.",
   reparto="Cast", canto="Phoenix Chant", mipapel="My part:", todos_op="All parts", solo="Show only my lines",
   oir="Listen", oir_acto="🔊 Listen to the act", parar="⏹ Stop", menor="Smaller text", mayor="Bigger text", imprimir="🖨️ Print",
   th=["Part", "Grade", "What they are like", "Lines"], acot="Stage direction", arriba="↑ Close and back to top", ir="Go to",
   nota="Stage directions (in italics) tell what happens on stage: they are not read aloud.",
   pie="“The Phoenix on the Lake” · A play by José M. Fernández · License CC BY-NC-SA 4.0",
   prod="🎬 Production guide (in Spanish for now): cast, music, costumes, sets and family letter", voz="en-US", lumi="index.html", teatro="teatro.html", teatro_txt="← Lumi Theater",
   menu=[("index.html","Home"),("grados.html","By grade"),("materias.html","By subject"),("teatro.html","Theater")]),
}

CSS = """
.obra-cab{background:var(--cie);padding:1.4rem 0}
.obra-cab h1{font-size:clamp(1.8rem,4.5vw,2.6rem)}
.obra-cab .sub{font-size:1.2rem;margin:.3rem 0 0}
.obra-cab .autor{margin:.3rem 0 0;font-weight:700}
.barra{position:sticky;top:76px;z-index:5;background:#fff;border:2px solid var(--borde);border-radius:14px;padding:.6rem .8rem;margin:1rem 0;display:flex;flex-wrap:wrap;gap:.5rem;align-items:center}
.barra label{font-weight:700}
.barra select,.barra button{min-height:44px;font:inherit;border-radius:999px;border:2px solid var(--pet);background:#fff;color:var(--pet);padding:0 .9rem;font-weight:700;cursor:pointer}
.barra button[aria-pressed="true"]{background:var(--pet);color:#fff}
.barra .chk{display:inline-flex;align-items:center;gap:.4rem;font-weight:700}
.barra .chk input{width:22px;height:22px}
.linea{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:.6rem;align-items:start;padding:.6rem .8rem;margin:.35rem 0;border-left:8px solid var(--c);border-radius:10px;background:#fff}
.linea .quien{display:inline-block;font-weight:700;color:#fff;background:var(--c);border-radius:999px;padding:.05rem .65rem;font-size:.9rem;margin-right:.4rem}
.linea .grado{font-size:.85rem;margin-right:.4rem}
.linea p{margin:.25rem 0 0}
.acot{font-style:italic;margin:.6rem 0;padding:.4rem .8rem;border-left:4px dashed var(--borde);color:#2d5f69}
.oir{min-width:44px;min-height:44px;border-radius:50%;border:2px solid var(--pet);background:#fff;cursor:pointer;font-size:1.1rem}
.oir:hover{background:var(--cie)}
body.filtrando .linea{opacity:.35}
body.filtrando .linea.mia{opacity:1;box-shadow:0 0 0 3px var(--c)}
body.solo .linea:not(.mia){display:none}
body.solo .acot{display:none}
.linea.hablando{outline:3px solid var(--ama)}
details.acord{border:2px solid var(--borde);border-radius:16px;margin:.8rem 0;padding:0;background:#fff}
details.acord > summary{padding:.8rem 1rem;min-height:56px;list-style:none;border:0}
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
.canto{font-size:1.25rem;line-height:1.7;background:var(--cie);border-radius:14px;padding:1rem 1.4rem}
body.grande{font-size:21px}
body.muygrande{font-size:24px}
main .seccion{scroll-margin-top:170px}
.barra select{max-width:100%}
@media (max-width:760px){.barra{position:static}.barra select{width:100%}main .seccion{scroll-margin-top:130px}}
@media print{.barra,.oir,.acto-h button,.cabecera,.anclas{display:none!important}.linea{break-inside:avoid;border-left-width:6px}body.filtrando .linea{opacity:1}}
"""

JS = r"""
(function(){
  "use strict";
  var LANG = document.documentElement.lang, VOZ = document.body.getAttribute("data-voz");
  var sel = document.getElementById("mi-papel"), solo = document.getElementById("solo");
  function aplicar(){
    var p = sel.value;
    document.querySelectorAll(".linea").forEach(function(l){ l.classList.toggle("mia", !!p && l.getAttribute("data-papel") === p); });
    document.body.classList.toggle("filtrando", !!p);
    document.body.classList.toggle("solo", !!p && solo.checked);
    if(p && solo.checked) document.querySelectorAll("details.acord").forEach(function(d){ if(d.querySelector(".linea.mia")) d.open = true; });
    try{ localStorage.setItem("fenix-papel", p); }catch(e){}
  }
  try{ var g = localStorage.getItem("fenix-papel"); if(g && sel.querySelector('option[value="'+g+'"]')) sel.value = g; }catch(e){}
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
  document.querySelectorAll(".oir-acto").forEach(function(b){ b.addEventListener("click", function(){
    var ls = [].slice.call(b.closest("details").querySelectorAll(".linea")).filter(function(l){ return getComputedStyle(l).display !== "none"; });
    decir(ls);
  }); });
  document.querySelectorAll(".parar").forEach(function(b){ b.addEventListener("click", function(){ cola = []; if(hay) speechSynthesis.cancel(); limpiar(); }); });
  if(!hay) document.querySelectorAll(".oir,.oir-acto,.parar").forEach(function(b){ b.hidden = true; });

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

def pagina(L):
    t = T[L]; i = 0 if L == "es" else 1
    cuenta = {}
    for _, _, _, lineas in ACTOS:
        for p, *_ in lineas:
            if p != "AC": cuenta[p] = cuenta.get(p, 0) + 1
    cuenta["TODOS"] = cuenta.get("TODOS", 0) + 1  # el canto
    filas = "\n".join(
        f'<tr><td><span class="punto" style="background:{PAPELES[p][0]}" aria-hidden="true"></span>{e(nombre(p,L))}</td><td>{e(grado(p,L))}</td><td>{e(PAPELES[p][5 if L=="es" else 6])}</td><td>{cuenta.get(p,0)}</td></tr>'
        for p in PAPELES)
    opciones = "".join(f'<option value="{p}">{e(nombre(p,L))} · {e(grado(p,L))}</option>' for p in PAPELES)
    actos = []
    for aid, tes, ten, lineas in ACTOS:
        cuerpo = []
        for p, tx_es, tx_en in lineas:
            tx = tx_es if L == "es" else tx_en
            if p == "AC":
                cuerpo.append(f'  <p class="acot"><span class="sr">{e(t["acot"])}: </span>{e(tx)}</p>')
            else:
                c = PAPELES[p][0]
                cuerpo.append(f'''  <div class="linea" data-papel="{p}" style="--c:{c}">
   <div><span class="quien">{e(nombre(p,L))}</span><span class="grado">{e(grado(p,L))}</span><p class="txt">{e(tx)}</p></div>
   <button type="button" class="oir" aria-label="{e(t["oir"])}: {e(nombre(p,L))}">🔊</button>
  </div>''')
        tit = tes if L == "es" else ten
        actos.append(f'''<details class="seccion acord" id="{aid}">
 <summary><h2 id="t-{aid}">{e(tit)}</h2></summary>
 <div class="cuerpo">
 <div class="acto-h"><span><button type="button" class="oir-acto">{e(t["oir_acto"])}</button> <button type="button" class="parar">{e(t["parar"])}</button></span></div>
{chr(10).join(cuerpo)}
 <p class="arriba"><a href="#contenido" class="cerrar">{e(t["arriba"])}</a></p>
 </div>
</details>''')
    canto = CANTO_ES if L == "es" else CANTO_EN
    canto_html = f'''<details class="seccion acord" id="canto">
 <summary><h2 id="t-canto">{e(t["canto"])}</h2></summary>
 <div class="cuerpo">
 <div class="acto-h"><span><button type="button" class="oir-acto">{e(t["oir_acto"])}</button> <button type="button" class="parar">{e(t["parar"])}</button></span></div>
 <div class="linea" data-papel="TODOS" style="--c:{PAPELES["TODOS"][0]}">
  <div><span class="quien">{e(nombre("TODOS",L))}</span><p class="txt canto">{"<br>".join(e(v) for v in canto)}</p></div>
  <button type="button" class="oir" aria-label="{e(t["oir"])}: {e(t["canto"])}">🔊</button>
 </div>
 <p class="arriba"><a href="#contenido" class="cerrar">{e(t["arriba"])}</a></p>
 </div>
</details>'''
    anclas = [("reparto", t["reparto"])] + [(a[0], (a[1] if L == "es" else a[2]).split(" · ")[0]) for a in ACTOS] + [("canto", t["canto"])]
    nav = "".join(f'<li><a href="#{a}">{e(x)}</a></li>' for a, x in anclas)
    menu = "\n".join(f'   <a href="{h}"{" aria-current=\"page\"" if h == t["teatro"] else ""}>{e(x)}</a>' for h, x in t["menu"])
    otro_lbl = "Language" if L == "en" else "Idioma"
    idioma = (f'<span aria-current="true">Español</span><a href="{t["otro"]}" lang="en" hreflang="en">English</a>' if L == "es"
              else f'<a href="{t["otro"]}" lang="es" hreflang="es">Español</a><span aria-current="true">English</span>')
    return f'''<!doctype html>
<!-- {t["titulo"]} · José M. Fernández · CC BY-NC-SA 4.0 · generado con gen_fenix.py -->
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["titulo"])} · Lumi</title>
<meta name="description" content="{e(t["intro"])}">
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
  <div class="idioma" role="group" aria-label="{otro_lbl}">{idioma}</div>
 </div>
</header>
<section class="obra-cab" aria-labelledby="titulo">
 <div class="envoltura">
  <p style="margin:0"><a href="{t["teatro"]}">{e(t["teatro_txt"])}</a></p>
  <h1 id="titulo">{e(t["titulo"])}</h1>
  <p class="sub">{e(t["sub"])}</p>
  <p class="autor">{e(t["autor"])}</p>
  <p>{e(t["intro"])}</p>
  <p><a href="obra-fenix-lago-produccion-es.html"{' lang="es" hreflang="es"' if L=="en" else ""}>{e(t["prod"])}</a></p>
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
  <div class="envoltura-tabla"><table class="tabla">
   <thead><tr>{"".join(f'<th scope="col">{e(h)}</th>' for h in t["th"])}</tr></thead>
   <tbody>
{filas}
   </tbody>
  </table></div>
  <p class="arriba"><a href="#contenido" class="cerrar">{e(t["arriba"])}</a></p>
  </div>
 </details>
{chr(10).join(actos)}
{canto_html}
</div></main>
<footer class="pie"><div class="envoltura"><p>{e(t["pie"])}</p></div></footer>
<script>{JS}</script>
</body>
</html>
'''

if __name__ == "__main__":
    for L in ("es", "en"):
        with open(os.path.join(AQUI, f"obra-fenix-lago-{L}.html"), "w", encoding="utf-8") as f:
            f.write(pagina(L))
    print("ok")
