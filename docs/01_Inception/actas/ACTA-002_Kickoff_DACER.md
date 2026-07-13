# ACTA DE REUNIÓN KICKOFF — DACER S.A.C.
**Código:** ACTA-002
**Fecha:** 08 de abril de 2026
**Lugar:** Oficinas de DACER S.A.C., Miraflores, Lima / Modalidad Mixta
**Fase RUP:** Inicio

## Asistentes
- Brayan Delgado Oblitas (Practicante / Desarrollador)
- [Nombre del Ingeniero AV / Supervisor en DACER S.A.C.]

## Orden del Día
1. Presentación de la propuesta técnica del practicante.
2. Análisis del flujo actual de maquetación (AS-IS).
3. Definición y confirmación de alcance del proyecto.
4. Acuerdos y compromisos.

## Puntos Tratados
- **Flujo actual de maquetación (AS-IS):** El ingeniero detalló que, para cada sala de reuniones, debe abrir Crestron Construct, arrastrar manualmente componentes como botones y sliders, alinearlos mediante clics, configurar sus propiedades (colores, tamaños, estados) y finalmente asociar IDs. Este proceso iterativo no es fácilmente replicable entre proyectos.
- **Tiempo promedio:** Se determinó que la maquetación visual inicial de una pantalla táctil típica toma aproximadamente 45 minutos antes de empezar la programación lógica de procesadores.
- **Pain points:** Repetitividad, falta de un sistema robusto de templates y el alto consumo de tiempo frente a la pantalla solo para definir geometría espacial, restando tiempo valioso a la configuración real de equipos AV y lógicas de control.

## Acuerdos
- **Alcance acordado:** El sistema AV-MCP Automator intervendrá exclusivamente en la generación de archivos para interfaces gráficas (Frontend CH5). La programación de procesadores físicos y lógica (SIMPL Windows, C#) queda descartada.
- **Restricciones confirmadas:** DACER S.A.C. no financiará licencias de software privativas para este proyecto universitario. El sistema debe operar con un presupuesto de S/. 0 y alojarse localmente. La información comercial confidencial de clientes finales no se procesará en las peticiones.
- **Recursos disponibles:** El desarrollador utilizará su equipo personal (Lenovo IdeaPad, 16GB RAM) para el desarrollo y las pruebas, y se otorgarán los accesos documentales necesarios para entender el estándar CH5.

## Compromisos
- **Del practicante:** Entregar una solución de software funcional validada con pruebas de compatibilidad, y manuales operativos (usuario y despliegue) antes del 29/06/2026.
- **De DACER S.A.C.:** Proveer retroalimentación oportuna, facilitar pruebas de los archivos `.cuig` en escenarios controlados (IDE Crestron Construct) y participar en la sesión de capacitación al cierre del ciclo.

## Próximos Pasos
- Levantar y documentar formalmente los requerimientos y casos de uso del sistema.
- Iniciar la Fase de Elaboración explorando el formato `.cuig`.

## Firmas

_________________________     _________________________
Brayan Delgado Oblitas        [Nombre del Supervisor]
Practicante                   Supervisor DACER S.A.C.
