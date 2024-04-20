from openai import OpenAI
client = OpenAI()
 
assistant = client.beta.assistants.create(
  name="Trata de personas",
  instructions="Eres un experto en derecho penal, delito de trata de personas",
  model="gpt-3.5-turbo-0125",
  tools=[{"type": "file_search"}],
  temperature=0
)

""" vector_store = client.beta.vector_stores.create(name="Financial Statements")
file_paths = [
  "trata_de_personas.pdf", 
  "Trata De Personas - Art. 129.A.docx", 
  "Trata De Personas - Convención de las Naciones Unidas contra la Delincuencia Organizada Transnacional.docx",
  "Trata De Personas - Decreto Supremo N° 088-2001-RE.docx"]
file_streams = [open(path, "rb") for path in file_paths]

file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id=vector_store.id, files=file_streams
)

print(file_batch.status)
print(file_batch.file_counts) """

assistant = client.beta.assistants.update(
  assistant_id=assistant.id,
  tool_resources={"file_search": {"vector_store_ids": ["vs_CkufhP0y04QuVQyB2uZtDm5v"]}},
)

print(assistant)

# Create a thread and attach the file to the message
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Explotar es un verbo rector del delito de trata de personas o es la finalidad perseguida, por tratarse de un delito de tendencia interna trascendente",
      # Attach the new file to the message.
    }
  ]
)

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id, assistant_id=assistant.id
)

messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

print(messages)

""" message_content = messages[0].content[0].text
annotations = message_content.annotations
citations = []
for index, annotation in enumerate(annotations):
    message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
    if file_citation := getattr(annotation, "file_citation", None):
        cited_file = client.files.retrieve(file_citation.file_id)
        citations.append(f"[{index}] {cited_file.filename}")

print(message_content.value)
print("\n".join(citations)) """