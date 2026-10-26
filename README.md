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
| index.html | index-en.html | Bienvenida, grados y materias |
| grados.html | grados-en.html | Todo, ordenado por grado (anclas `#prek`, `#k`, `#g1` … `#g6`) |
| materias.html | materias-en.html | Todo, ordenado por materia (anclas `#matematicas`, `#lectura`, `#ciencias`, `#sociales`) |

Las anclas son iguales en los dos idiomas, así que al cambiar de idioma
el estudiante se queda en la misma sección.

## Cómo agregar material

1. **Interactivos y juegos:** añadir una serie en `catalogo.js`
   (grado, materia, título y dirección en cada idioma, y sus lecciones).
2. **Cuentos:** no hay que tocar nada aquí. El portal lee el catálogo
   de `cuentos-educativos` y cada cuento nuevo aparece solo.
3. **Libros de cuentos terminados:** añadir una línea en `libros`
   dentro de `catalogo.js`.

## Archivos

- `catalogo.js`: la lista de series (lo único que se edita a menudo).
- `lumi.js`: arma las páginas a partir del catálogo.
- `lumi.css`: colores y estilos del Manual de identidad v1.2.
- Logo, favicon e ilustraciones de Lumi.

Autor: José M. Fernández · Licencia: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es).
