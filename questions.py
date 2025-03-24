import random
import sys
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
punt = 0 # Se inicializa el contador de puntos
# El usuario deberá contestar 3 preguntas
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
for q, a, c in questions_to_ask:
    print(q)
    for i, answer in enumerate(a):
        print(f"{i + 1}. {answer}")
    cont = 0 
    for intento in range(2):
        cont += 1
        user_answer = input("Respuesta: ")
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if (user_answer < 5) and (user_answer > 0):
                if user_answer == c + 1:
                    print("¡Correcto!")
                    punt += 1
                    break
                else:
                    if cont == 1:
                        punt -= 0.5
            else:
                print("Respuesta no válida.")
                sys.exit(1)
        else:
                print("Respuesta no válida.")
                sys.exit(1)
    else:
        print("Incorrecto. La respuesta correcta es:")
        print(c + 1)
        punt -= 0.5
print("El puntaje del jugador/a es: ", punt)