# Ustedes deberán realizar los cambios en caso de ser necesarios
# para quitar los errores y obtener la ejecución del agente inteligente

class GuessingAgent:
    def __init__(self, min_range, max_range):
        self.min_range = min_range
        self.max_range = max_range

    def guess(self):
        return (self.min_range + self.max_range) // 2  # Devuelve el punto medio del rango.

def main():
    print("Bienvenido al juego 'Adivina el número 1-100'!")
    min_range = 1
    max_range = 100
    agent = GuessingAgent(min_range, max_range)

    while True:
        agent_guess = agent.guess()
        print(f"El agente adivina: {agent_guess}")
        # Verificación del rango minimo y maximo
        if agent_guess == 1 or agent_guess == 100:
            print("El agente ha adivinado el número correctamente!")
            break

        user_response = input("Es demasiado alto (A), demasiado bajo (B) o correcto (C)?").upper()
        if user_response == "A":
            agent.max_range = agent_guess - 1
        elif user_response == "B":
            agent.min_range = agent_guess + 1
        elif user_response == "C":
            print("El agente ha adivinado el número correctamente!")
            break
        else:
            print("Respuesta no válida. Por favor, responde con A, B o C.")

if __name__ == "__main__":
    main()
