from agents.identification_agent import identification_agent
from agents.breakdown_agent import breakdown_agent
from agents.translator_agent import translator_agent
from agents.formatting_agent import formatting_agent

if __name__ == "__main__":
    input_path = "input_document.docx"
    
    prompt = identification_agent(input_path)
    print("\nGenerated Prompt:\n", prompt)
    
    structured_data = breakdown_agent(input_path)
    print("\nStructured Data Sample (First 2 elements):\n", structured_data[:2])
    
    translated_data = translator_agent(structured_data)
    print("\nTranslated Data Sample (First 2 elements):\n", translated_data[:2])
    
    formatting_agent(translated_data)
    print("\nTranslation process completed successfully!")
