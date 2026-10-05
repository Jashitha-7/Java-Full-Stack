from ollama import chat
prompt = """
Write Python code to display the following image-analysis result
as a simple structured report:
Objects: Laptop, keyboard, mouse
Text: Computer Laboratory
Main purpose: Educational computer laboratory
Use headings for Objects, Text, and Main Purpose.
"""
response = chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}]
)
print(response["message"]["content"])