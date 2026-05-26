from locust import HttpUser, task, between
import random

class UsuarioExtremo(HttpUser):
    # Espera mínima entre tareas para generar carga real
    wait_time = between(0.05, 0.2)

    @task(5)
    def visitar_home(self):
        # Solo la raíz "/" que sí existe
        self.client.get("/?rand=" + str(random.randint(1, 10000)))

    @task(1)
    def visitar_home_lento(self):
        # Simula usuarios que esperan un poco más
        self.client.get("/?rand=" + str(random.randint(1, 10000)))