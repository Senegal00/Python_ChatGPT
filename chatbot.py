import openai
# archivo de configuracion para la api-key que se genero en la pagina oficial de openai.
import config
# from rich import print


def main():
    """Es una pequeño ejemplo de uso de la api de OPENAI integrando Python"""
    openai.api_key = config.API_KEY
    # contexto del asistente
    messages = [
        {"role": "system", "content": "Eres un desarrollador muy avanzado."}]
    # ------------------------------------------------------------------------#
    client = openai
    # response = client.chat.completions.create(
    #     model="davinci-002", messages=[{"role": "system", "content": "You are a helpful assistant."}])
    # ------------------------------------------------------------------------#

    while True:  # para que pregunte de manera constante.
        # aqui se guarda la pregunta que se va a hacer a la api de OpenAi
        content = input("De que quieres hablar?. ")
        if content == "exit":  # para romper el ciclo.
            break
        # las preguntas que se hacen a la api
        messages.append({"role": "user", "content": content})
        response = client.chatcompletions.create(
            model="GPT-3.5", messages=[messages])

        # completion = openai.Completion.create(model="davinci-002", prompt="Hello world")
        # print(response.choices[0].message)
        response_content = response.choices[0].message.content
        # para que la api conosca el contexto, de las conversaciones.
        messages.append({"role": "assistant", "content": response_content})
        print(f"{response_content}")


# para usar a typer.
if __name__ == "__main__":
    main()
