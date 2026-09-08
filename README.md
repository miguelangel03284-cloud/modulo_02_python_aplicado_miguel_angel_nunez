PREGUNTA DE	RAZONAMIENTO
1. ¿Por qué diagnosticar el dataset completo (forma, nulos) antes	de	limpiar	nada,	en	vez	de	empezar	a limpiar directamente	desde la primera columna que veas?

Primero se necesita saber lo que contiene el dataset para conocer el tamaño tanto de filas y columnas y de cuales estan vacias o con informacion no relevante para asi poder modificando y organizando los datos 

2. ¿Qué pasaría si	rellenaras	Budget	con	0	en	vez	de	eliminar esas filas?	¿Cómo afectaría	eso	a la columna Ganancia que vas a	crear	en	la próxima	etapa?

La ganancia aumentaria incorrectamente ya que se le estaria restando 0 y no seria una informacion certera 

3. Ganancia se	calcula	restando (WorldGross -	Budget).	¿Qué representaría,	en	cambio,	una	columna	que	dividiera	WorldGross	entre
Budget?	¿En	qué	caso preferirías esa versión en	vez	de	la	resta?

Representa cuántas veces se recuperó el presupuesto. Es útil para medir la rentabilidad

4. ¿Qué habría	pasado	si	hubieras intentado	ordenar	por	Ganancia antes	de	limpiar	los	nulos de WorldGross	y Budget en	la	Etapa 2?	¿Por qué el	orden en que se	hacen las etapas importa aquí?

El resultado podría ser incorrecto porque habría datos incompletos
Porque el codigo se ejecuta de arriba hacia abajo y si no se cumple la condicion salta o da error puede no mostrar la informacion deseada

5. De los géneros con más películas	en	el	dataset	(Comedia,	Acción,	Drama),	¿cuál tiene	el	promedio de	calificación de	crítica	más	alto?	¿Te sorprende, o era lo	que	esperabas?

Segun el resultado me reflejo que Drama tiene el promdio mas alto en cuanto a las criticas, no me sorprende al ser un genero mas vistos por feminas las cuales son mas sensibles a dar criticas

Comedy       44.8
Action       44.9
Drama        57.4

6. ¿Por	qué	guardar	el	resultado en un	archivo	nuevo (hollywood_limpio.csv), en vez de	sobrescribir el	archivo	original hollywood.csv	que descargaste?

Para tener una copia mejorada sin afectar el documento original 

ESCENARIO	1

Si	el	dataset	tuviera	una	columna	de	fechas	completas (día,	mes	y año) en	vez	de	solo el	año, ¿qué tendrías que	verificar antes	de	poder	ordenar el	dataset	cronológicamente por esa columna?

verificar que la columna tenga formato de fecha para poder ordenarla segun el requerimiento

ESCENARIO	2

Si	quisieras aplicar este mismo pipeline a	un	dataset	completamente distinto	(por ejemplo, canciones	con	su	artista, género	y número de reproducciones), ¿qué partes de	tu	código	cambiarían,	y cuáles seguirían	exactamente	igual?

Cambiarían los nombres y las columnas específicas, pero el proceso de limpiar, transformar y analizar sería similar ya que se busca optimizar el dataset

ESCENARIO	3

Si una columna	nueva	tuviera	95%	de	sus	valores	nulos (mucho peor que Genre, que tenía	cerca	del	29%), ¿seguirías rellenándola de la	misma forma?	¿Qué harías	distinto, y	por	qué?

Consideraría eliminar la columna o buscar otra forma de obtener esos datos, porque tiene demasiados valores vacíos y puede generar informacion incorrecta en los resultados
