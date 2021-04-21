# Spike Challenge

## Pregunta 1

Para crear el MVP se necesitan los siguientes artefactos:

- Aplicación movil
- API y API Gateway
- Aplicación web
- Proceso CI/CD
- Proceso de recoleccion de analytics

En un inicio sería una API monolitica y escalable, tendriamos una web simple para la construcción del branding o marca. Es necesario que la aplicación para los usuarios finales sean en dispositivos móviles. Además al ser un prototipo es necesario tener métricas que nos indiquen que problemas o mejoras se han detectado relacionado con las actividades de los usuarios, para esta parte necesitaria de la ayuda de un Data Scientist.

## Pregunta 2

Al ser un MVP y que debe ser diseñado de forma rápida y eficiente, consideraría utilizar una arquitectura monolítica que en un inicio esté delimitada en contextos para en un futuro poder llevarlo a microservicios. Mis razones son las siguientes:

- Crear una arquitectura de microservicios para un MVP no genera impacto en el negocio a menos que sepamos que desde el primer día tendremos grandes cantidades de usuarios.

- Crear una arquitectura de microservicios es complejo, un MVP debe ser desarrollado de forma rápida porque no sabemos si el producto finalmente será aceptado. Cada microservicio requeriría su propia pipeline CI/CD, su propio mantenimiento y sus propias pruebas, generando complejidad innecesaria al inicio.

- Un microservicio debe estar bien definido y delimitado, debe cumplir con el principio de Responsabilidad Unica. Crear microservicios desde el inicio es riesgoso. Al desconocer la magnitud de los posibles contextos o dominios de nuestra aplicación podriamos crear microservicios que en un futuro pueden volverse muy complejos y abarcar demasiados contextos.

## Pregunta 3

En mi experiencia me ha funcionado el SCRUM. Podriamos iniciar con la creacion de historias de usuario y rapidamente definir requerimientos. Considero que los sprints son relevantes para llevar a cabo el desarrollo de este MVP ya que se necesita tener siempre un producto funcional en cada iteración.

## Pregunta 4

Considero que deberiamos seguir el proceso de [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). Tendriamos una rama master para aplicaciones listas para produccion. Una rama de desarrollo donde estaría integrado un pipeline CI/CD para desarrollar y deployar continuamente. Además contariamos con multiples ramas feature para cada requerimiento que se quiera construir en la aplicación.

Cada commit a la rama feature se debe validar con test unitarios, los commits a la rama develop deben de deployarse en un entorno de desarrollo continuo.

Además para mejores prácticas deberiamos seguir lineamientos para los commits usando [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

## Pregunta 5

Los roles propuestos son suficientes para el desarrollo del prototipo. Sin embargo consideraría agregar algunos Ing. de Software que puedan *llevar varios sombreros* para desarrollar más rápido el primer prototipo. Posteriormente podríamos crear roles especializados necesarios en todo equipo de desarrollo: ingenieros QA, ingenieros DevOps, UX Designers, frontend Developers, mobile Developers, backend developers. Después se podría hacer los analytics con Ing. de Machine Learning o Data Scientist para incorporar features inteligentes a la aplicación. Además se requeriría de un Product Manager para dirigir el futuro del producto.