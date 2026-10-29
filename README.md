# Lumi · Pequeñas luces, grandes ideas

Portal educativo gratuito, de prekínder a 6.º grado, en español y en inglés.
Se publica en **www.lumi-educa.com** (también responde lumi-educa.com y la dirección anterior, zhemaria.github.io/lumi, que redirige).

Este repositorio contiene solo el "cascarón" del portal. Las actividades
viven en sus propios repositorios:

- **primaria**: interactivos y juegos.
- **cuentos-educativos**: cuentos ilustrados y libros.

## Páginas

| Español | English | Qué muestra |
|---|---|---|
| index-es.html | index.html (portada por defecto) | Bienvenida, grados y materias |
| grados-es.html | grados.html | Todo, ordenado por grado (anclas `#prek`, `#k`, `#g1` … `#g6`) |
| materias-es.html | materias.html | Todo, ordenado por materia (anclas `#matematicas`, `#lectura`, `#ciencias`, `#sociales`) |

Las anclas son iguales en los dos idiomas, así que al cambiar de idioma
el estudiante se queda en la misma sección.

## Cómo agregar material

1. **Interactivos y juegos:** añadir una serie en `catalogo.js`
   (grado, materia, título y dirección en cada idioma, y sus lecciones).
2. **Cuentos:** no hay que tocar nada aquí. El portal lee el catálogo
   de `cuentos-educativos` y cada cuento nuevo aparece solo.
3. **Libros de cuentos terminados:** añadir una línea en `libros`
   dentro de `catalogo.js`.

## Teatro

Las obras se dan de alta en `obras`, dentro de `catalogo.js`; cada una tiene su guion
en español y en inglés y su guía de producción. Las páginas se generan con los
programas de `herramientas/`:

| Obra | Generador | Páginas |
|---|---|---|
| *El Fénix sobre el Lago*, de José M. Fernández | `gen_fenix.py` | `obra-fenix-lago-*.html` |
| *El bosque mágico*, de Vicente Cañón Verdasco | `gen_bosque_produccion.py` (guía y cartel); el generador del guion se agregará cuando el autor apruebe la traducción al inglés | `obra-bosque-magico-*.html` |

*El bosque mágico* es obra de **Vicente Cañón Verdasco** (© 2019, www.obrasteatro.com).
Se publica en Lumi con su autorización escrita (octubre de 2026): guion interactivo,
traducción al inglés y reparto ampliado, siempre con su nombre como autor y con el
título original. El texto de la obra pertenece a su autor; la licencia CC BY-NC-SA
de Lumi cubre solo la guía de producción, el cartel y el diseño de las páginas.

## Archivos

- `catalogo.js`: la lista de series (lo único que se edita a menudo).
- `lumi.js`: arma las páginas a partir del catálogo.
- `lumi.css`: colores y estilos del Manual de identidad v1.2.
- Logo, favicon e ilustraciones de Lumi.

Autor: José M. Fernández · Licencia: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es).
