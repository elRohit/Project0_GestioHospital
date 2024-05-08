# Servidor de Base de Datos:
**Procesador:** Opta por un procesador potente con múltiples núcleos y altas frecuencias. Los procesadores Intel Xeon o AMD EPYC son excelentes opciones.

**Memoria RAM:** Cuanta más RAM, mejor. Al menos 64 GB, pero preferiblemente 128 GB o más.

**Discos Duros:** Utilizaremos discos duros de estado sólido (SSD) para un rendimiento óptimo. También puedes considerar una combinación de SSD para datos activos y discos duros tradicionales para almacenamiento a largo plazo.

**Controlador RAID:** Implementaremos un controlador RAID para la redundancia y la protección de datos en caso de pérdida de datos o fallo de discos de almacenamiento.

**Red:** Es recomendable que el servidor tenga múltiples interfaces de red para la segregación de tráfico y la redundancia.

**Sistema Operativo:** Utiliza un sistema operativo libre Server de Linux.

# Hardware elegido

[Lenovo ThinkSystem SR630 V2 Servidor en Bastidor 1U Intel Xeon Silver 4309Y/32GB](https://www.pccomponentes.com/lenovo-thinksystem-sr630-v2-servidor-en-bastidor-1u-intel-xeon-silver-4309y-32gb)

| Componente      | Descripción                                                              |
|----------------|--------------------------------------------------------------------------|
| Procesador    | Intel Xeon Silver 4309Y                                                  |
| Memoria RAM    | 64 GB RAM                                                                |
| Disco duro     | Disc SAS                                                                 |
| Red            | Tipo Ethernet                                                            |
| Sistema Operativo | Debian server 12                                                      |

`Procesador:`

Procesador Intel Xeon serie 5100: Estos procesadores ofrecen una velocidad de hasta 2,33 GHz y una cantidad de núcleos de hasta 4.

`Memoria RAM:` 

64 GB debería ser suficiente, aunque es un poco justo considerando los requisitos solicitados. Dependiendo de la concurrencia de la aplicación, puede ser necesario ampliar la cantidad de memoria RAM.

`Discos duros:` 

Son discos que consumen menos recursos y tienen una interfaz totalmente compatible con SATA, y también son capaces de alcanzar altas velocidades de lectura y escritura. Para más almacenamiento se podria montar un servidor SAS que no será mas que un servidor de almacenamiento interno dentro de la red.

`Red:`

Principalmente es 1 red Ethernet, La idea es implementar un Etherchannel ya que con eso ganaremos más velocidad.

`Sistema Operativo:`

El más apto en este caso seria Linux, en mi caso Debian Server o Ubuntu server ya que són muy buenos para la seguridad, administración remota entre otras cosas.