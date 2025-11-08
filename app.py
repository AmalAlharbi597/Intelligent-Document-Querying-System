from bedrock import valid_prompt, query_knowledge_base, generate_response
import json

def prepare_context(user_input, retrieved_docs):
    base_prompt = """You are an assistant that answers questions based on the provided context.
If the answer is not found in the context, respond with "I don't know."

<context>
{context}
</context>

<question>
{question}
</question>

Answer:"""

    context_text = ""
    for i, doc in enumerate(retrieved_docs):
        text = doc.get('content', {}).get('text', '')
        context_text += f"[{i+1}] {text}\n"

    full_prompt = base_prompt.format(context=context_text, question=user_input)
    return full_prompt


def generate_rag_answer(user_input):
    if not valid_prompt(user_input):
        return "This question is not within the allowed topic."

    retrieved_docs = query_knowledge_base(user_input)

    if not retrieved_docs:
        return "No relevant information found in the knowledge base."

    final_prompt = prepare_context(user_input, retrieved_docs)
    answer = generate_response(final_prompt)

    sources = []
    for doc in retrieved_docs:
        try:
            s3_uri = doc['location']['s3Location']['uri']
            file_name = s3_uri.split('/')[-1]
            if file_name not in sources:
                sources.append(file_name)
        except KeyError:
            continue

    result = answer + "\n\nSources:\n"
    for i, name in enumerate(sources, 1):
        result += f"[{i}] {name}\n"

    return result


def main():
    print("AWS Bedrock Knowledge Base Chatbot")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Chat ended.")
            break

        response = generate_rag_answer(user_input)
        print(f"\nBot: {response}\n")


if __name__ == "__main__":
    main()
