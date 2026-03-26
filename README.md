# 📮 Gestor de Colas CLI - Farmacia

Aplicación de terminal interactiva desarrollada en Python para gestionar los turnos de atención de una farmacia multipuesto (Perfumería, Farmacia y Cosmética). El proyecto destaca por una arquitectura modular que separa la interfaz de usuario de la lógica de negocio, priorizando la eficiencia de memoria y la robustez frente a errores de *input*.

## 🧰 Inventario de Arquitectura y Tecnologías

En este desarrollo se han aplicado patrones de diseño orientados a la optimización de recursos y al blindaje del flujo de ejecución:

### 1. Generadores (`yield`) y Evaluación Perezosa (Lazy Evaluation)
* El motor de turnos (`numeros.py`) no pre-calcula ni almacena listas infinitas de números en la memoria RAM. En su lugar, utiliza **Generadores** con la palabra reservada `yield`.
* Cada vez que un usuario solicita un ticket, el programa genera dinámicamente el siguiente número en la secuencia (`next()`), manteniendo un consumo de memoria mínimo (O(1)) sin importar cuántos turnos se expidan en el día.

### 2. Control de Flujo Defensivo (`try/except/else`)
* El menú interactivo (`main.py`) implementa validaciones estrictas interceptando excepciones `ValueError`.
* Mediante el uso estratégico de `.index()` sobre listas de opciones válidas (ej. `["P", "F", "C"]`), la aplicación bloquea cualquier entrada incorrecta por parte del usuario sin detener la ejecución (Crash), manteniendo el bucle activo hasta recibir un dato procesable.

### 3. Modularidad y Separación de Responsabilidades
* **`numeros.py`:** Módulo encapsulado que actúa como "Backend", manejando exclusivamente el estado de los turnos y el formateo estético de salida (función envolvente `decorador`).
* **`main.py`:** Script principal que actúa como "Frontend/Controlador", gestionando exclusivamente el enrutamiento del usuario y los bucles de interacción.

---

## ⚙️ Cómo ejecutar el proyecto

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado en tu sistema.
3. Ejecuta el archivo principal desde tu terminal:
   ```bash
   python main.py
