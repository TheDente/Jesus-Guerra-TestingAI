from playwright.sync_api import sync_playwright
import time
from datetime import datetime

casos = [
    (5, 3, 12),
    (2, 4, 8),
    (0, 12, 0),
    (10, 10, 10),
    (1, 15, "error"),   # Error esperado por lógica
    (4, 2, 99)          # Error esperado por comparación
]

def log_error(caso, error_msg):
    with open("errores_playwright.txt", "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}] ERROR en caso {caso}: {error_msg}\n")

def ejecutar_prueba(agregar, quitar, esperado):
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False, slow_mo=300)
        pagina = navegador.new_page()
        pagina.goto("http://localhost:8000/inventario.html")

        # Reiniciar stock a 10 desde JavaScript
        pagina.evaluate("cantidad = 10; actualizarVista();")

        # Agregar stock
        for _ in range(agregar):
            pagina.click("text=Agregar 1")

        try:
            if esperado == "error":
                # Esperamos una alerta al intentar quitar más stock del disponible
                with pagina.expect_event("dialog") as dialog_info:
                    for _ in range(quitar):
                        pagina.click("text=Quitar 1")
                    dialog = dialog_info.value
                    dialog.dismiss()
                stock_actual = pagina.inner_text("#cantidad")
                print(f"🧪 Agregado: {agregar}, Quitado: {quitar} → Stock final: {stock_actual} (alerta OK)")
            else:
                # Quitar stock
                for _ in range(quitar):
                    pagina.click("text=Quitar 1")

                stock_actual = pagina.inner_text("#cantidad")
                print(f"🧪 Agregado: {agregar}, Quitado: {quitar} → Stock final: {stock_actual}")
                assert int(stock_actual) == esperado, f"Esperado {esperado}, obtenido {stock_actual}"

        except Exception as e:
            log_error((agregar, quitar, esperado), str(e))

        time.sleep(1)
        navegador.close()

# Ejecutar todas las pruebas
for caso in casos:
    ejecutar_prueba(*caso)