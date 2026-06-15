# Repo para EIEC - DevOps - UNIR

Este repositorio incluye un proyecto sencillo para demostrar los conceptos de pruebas unitarias, pruebas de servicio o de API y pruebas E2E o de GUI. El objetivo es que el alumno entienda estos conceptos, por lo que el código y la estructura del proyecto son especialmente sencillos.

El Makefile ofrece comandos para facilitar la creación de imágenes de Docker y la ejecución de las pruebas. El único requisito es tener Docker instalado. Los comandos funcionarán en MacOS y Linux. En caso de usar Windows, será necesario adaptarlos o ejecutarlos en una máquina virtual Linux con Docker instalado.

---

# Guía para Poner en Marcha el Proyecto: Calculadora con Pruebas CI/CD

## ¿Qué es este proyecto?

Una aplicación **Calculadora** construida con Python/Flask (API REST) y una interfaz web en HTML + Vue.js. Su propósito principal es demostrar los **4 niveles de pruebas** en un pipeline de CI/CD:

```
[Pruebas Unitarias] → [Pruebas de Comportamiento BDD] → [Pruebas de API REST] → [Pruebas E2E]
```

---

## Arquitectura del Proyecto

```
app/
├── calc.py      ← Lógica de negocio (Calculator class)
├── api.py       ← API REST con Flask (endpoints /calc/add, /calc/substract, etc.)
└── util.py      ← Utilidades (conversión de tipos, permisos)

web/
└── index.html   ← Frontend: HTML + Vue.js (consume la API)

test/
├── unit/        ← Pruebas unitarias (pytest)
├── behavior/    ← Pruebas BDD/comportamiento (behave + Gherkin)
├── rest/        ← Pruebas de API REST (pytest)
├── e2e/         ← Pruebas End-to-End (Cypress)
├── jmeter/      ← Pruebas de rendimiento (JMeter)
└── sec/         ← Pruebas de seguridad (OWASP ZAP)
```

---

## Prerrequisito ÚNICO: Docker

Todo el proyecto corre dentro de contenedores Docker. **No necesitas instalar Python, pip, ni ninguna dependencia** en tu máquina.

- **Windows**: Instala [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **macOS/Linux**: Instala Docker Engine

> **Importante para Windows**: El Makefile usa sintaxis bash (backtick `` `pwd` ``). Se recomienda ejecutar desde **WSL2** (Windows Subsystem for Linux) o **Git Bash**. En PowerShell nativo los comandos no funcionarán directamente.

---

## Paso a Paso para Ver la Aplicación en Ejecución

### Paso 1 — Clonar y entrar al proyecto

```bash
git clone <url-del-repo>
cd Act02_01
```

### Paso 2 — Crear la carpeta de resultados

```bash
mkdir results
```

> Los reportes de pruebas se guardan aquí. Sin esta carpeta, algunos comandos fallan.

### Paso 3 — Construir la imagen Docker de la aplicación

```bash
make build
```

Este comando ejecuta el Dockerfile que instala Python 3.6 y todas las dependencias del archivo requires:

- Flask, pytest, behave, pylint, pytest-cov, junit2html, python-owasp-zap

### Paso 4 — Levantar solo el servidor API

```bash
make server
```

Esto arranca Flask en el puerto **5000**. Verifica en tu navegador:

- `http://localhost:5000/` → responde `Hello from The Calculator!`
- `http://localhost:5000/calc/add/3/5` → responde `8`

### Paso 5 — Levantar la interfaz web

En otra terminal:

```bash
make run-web
```

Esto levanta Nginx en el puerto **80** sirviendo el frontend. Abre `http://localhost` en tu navegador para ver la calculadora con interfaz gráfica.

> Usa constants.local.js que apunta a `http://localhost:5000` — perfecto para desarrollo local.

### Paso 6 — Parar la web cuando termines

```bash
make stop-web
```

---

## Ejecutar los Diferentes Tipos de Pruebas

### Pruebas Unitarias

```bash
make test-unit
```

- Ejecuta calc_test.py con `pytest`
- Genera reporte de **cobertura de código** en `results/coverage/`
- Genera `results/unit_result.html` con el resumen

**¿Qué prueba?** La lógica pura de `Calculator`: suma, resta, multiplicación, división, manejo de errores con tipos inválidos y división por cero.

### Pruebas de Comportamiento (BDD)

```bash
make test-behavior
```

- Usa `behave` con archivos Gherkin (`.feature`)
- Lee los escenarios de calculator.feature

Ejemplo de escenario en Gherkin:

```gherkin
Scenario: Use the add operation
  Given I open the calculator
  When I type 2 + 2
  Then the result is 4
```

> **Concepto clave**: BDD permite escribir pruebas en lenguaje natural que entienden tanto técnicos como negocio.

### Pruebas de API REST

```bash
make test-api
```

- Levanta el servidor Flask en una red Docker aislada
- Ejecuta api_test.py contra los endpoints reales
- Para después

**¿Qué prueba?** Que los endpoints HTTP respondan correctamente: status codes, respuestas, etc.

### Pruebas E2E (End-to-End con Cypress)

```bash
make test-e2e
```

- Levanta Flask + Nginx en red Docker
- Ejecuta calc.spec.js con Cypress en Chrome
- Simula un usuario real: escribe operandos, hace clic en botones, verifica resultados

---

## Mapa Mental: ¿Qué contenedor hace qué?

| Servicio           | Imagen                      | Puerto | Propósito                         |
| ------------------ | --------------------------- | ------ | --------------------------------- |
| `calculator-app`   | Construida con `make build` | —      | Imagen base Python + dependencias |
| `apiserver`        | `calculator-app` + Flask    | 5000   | API REST                          |
| `calc-web`         | `nginx` oficial             | 80     | Sirve el frontend HTML            |
| `cypress/included` | Cypress oficial             | —      | Pruebas E2E                       |
| `sonarqube-server` | SonarQube                   | 9000   | Análisis de calidad de código     |

---

## Problemas Comunes en Windows

| Problema                              | Solución                                                       |
| ------------------------------------- | -------------------------------------------------------------- |
| `make: command not found`             | Instalar Make via Chocolatey: `choco install make` o usar WSL2 |
| `` `pwd` `` no funciona en PowerShell | Usar WSL2 o Git Bash                                           |
| `results/` no existe y falla el test  | Ejecutar `mkdir results` antes del primer `make test-*`        |
| Puerto 80 ocupado                     | Cambiar `-p 80:80` a `-p 8080:80` en el comando `run-web`      |
| Puerto 5000 ocupado                   | Verificar con `netstat -ano \                                  |

---

## Flujo Completo Resumido

```bash
# 1. Construir imagen
make build
# 2. Levantar API + Web
make server        # terminal 1
make run-web       # terminal 2

# 3. Abrir http://localhost en el navegador

# 4. Ejecutar pruebas (en orden de granularidad)
make test-unit
make test-behavior
make test-api
make test-e2e

# 5. Ver resultados en la carpeta results/
```

---

## Concepto Clave para Entender el Proyecto

El archivo Makefile es el **punto de entrada único**. Cada `make <comando>` orquesta contenedores Docker, redes, volúmenes y la secuencia correcta de pasos — esto simula exactamente lo que haría un pipeline de CI/CD en Jenkins, GitLab CI o GitHub Actions.
