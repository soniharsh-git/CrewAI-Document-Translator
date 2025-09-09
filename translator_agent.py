import yaml

def translator_agent(structured_data, config_path="config.yaml"):
    """
    Translator Agent:
    Translates paragraphs and table text into target language.

    Args:
        structured_data (list): Structured data from breakdown agent.
        config_path (str): Path to config.yaml file.

    Returns:
        list: Translated structured data.
    """
    # Load config.yaml
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    target_language = config.get("target_language", "French")

    translated_data = []

    for element in structured_data:
        if element['type'] == 'paragraph':
            # Simulated translation
            translated_text = f"[Translated to {target_language}] {element['text']}"
            translated_data.append({
                "type": "paragraph",
                "text": translated_text,
                "bold": element["bold"],
                "italic": element["italic"],
                "alignment": element["alignment"]
            })

        elif element['type'] == 'table':
            translated_rows = []
            for row in element['rows']:
                translated_row = [f"[Translated to {target_language}] {cell}" for cell in row]
                translated_rows.append(translated_row)

            translated_data.append({
                "type": "table",
                "rows": translated_rows
            })

    print("[Translator Agent] Translation simulation completed.")
    return translated_data
