def identification_agent(input_doc_path):
    """
    Identification Agent:
    Reads the document and generates an initial prompt.

    Args:
        input_doc_path (str): Path to the input .docx file.

    Returns:
        str: Auto-generated prompt for further steps.
    """

    # For now, we keep it simple
    prompt = "You are an expert academic translator. Translate this academic paper from its original language to the target language specified in config.yaml, while maintaining structure (tables, footnotes, alignment, bold/italic, etc.)."
    
    print("[Identification Agent] Prompt generated successfully.")
    return prompt
