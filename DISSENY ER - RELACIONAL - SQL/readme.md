# Distribució de la base de dades
## Les taules de la base de dades
\n
Personal:
Aquesta taula conte la informació global de cada treballador de l’hospital. Aquesta informació, per exemple, podria ser el DNI, nom, cognoms, ... Informació que tota persona te en comú.

Metges:
Amb el ID del personal podem escollir inserir-lo en aquesta taula, que fa com referencia a que aquest treballador es metge. També pots dir l seva especialitat (aquesta es una altra taula) i inserir el seu currículum.

Infermers:
Com metges, aquesta taula serveix per identificar el ofici del treballador, amb la diferencia de metges, en aquesta taula, te una columna “Experiència”. On es pot inserir tota informació sobre les seves habilitats.

Altres:
Tant mateix com metges o infermers, serveix per identificar si es un treball diferent a aquests dos. Però per saber l’ofici “real” del treballador, existeix una columna anomenada “Tipus de treball”. 

Especialitat:
Com hem dit abans en metges, tenim aquesta taula que te com finalitat, dir la especialització del mèdic.

Especialitat / Estudis mèdics:
Es l’extensió de la anterior taula, on es dona informació especifica de tota la vida laboral o estudis específics del metge per tenir una informació detallada per a futures operacions o visites no generals.

Metge / Infermer:
Aquesta taula fa la funció de relacionar si una infermer esta enllaçada a un metge. Si aquest infermer no esta enllaçada a un metge, s’identifica que aquest es un infermer de planta.

Infermer / Planta:
Com hem dit abans, si el infermer no esta enllaçat a cap metge, aquest passa a ser un infermer de planta, amb aquesta taula podem identificar l’ID de l’infermer i el numero de planta on es troba l’infermer.
Planta:
En aquesta taula només ira l’ID / número de planta.
Planta / Habitacions:
Com diu el nom de la taula serveix per identificar quin número d’habitació hi es en la planta.
Habitacions:
En aquesta taula es com la de planta, només es guarda l’ID / número d’habitació.
Quiròfan:
Taula on es guarda el ID / número del quiròfan amb l’ID / número de planta on es troba.
Quiròfan / Aparells mèdics:
Aquesta es la taula on relacionem l’ID / número de quiròfan amb el identificador de l’aparell mèdic.
Pacients:
La taula pacients conte la informació principal que es necessita per identificar-ho i per saber les seves dificultats sanitàries. Tenim informació com per exemple la seva TSI  (Targeta Sanitaria Individual), nom, cognoms, numero de contacte i el contacte de emergència, ... Amb aquestes dades podem fer diagnòstics més precisos.
Diagnòstics:
Amb aquesta taula fem un barreig de visites i les seves conclusions, es a dir, el diagnòstic final del metge al pacient. Tenim com l’hora d’entrada i sortida al mateix temps que informació que identifiqui als protagonistes d’aquesta (metge i pacient).
Reserves:
Amb aquesta taula podem veure les reserves d’habitacions que tenen els pacients.
Operació:
Taula on es pot veure les operacions dels pacients, tant si es fa una operació com si només s’utilitza el quiròfan per altra intervenció. 
