from ember_nlp import EmberNLP

# Initialize EmberNLP
ember_nlp = EmberNLP()

# Text to analyze
text = 'I love pizza'

# Perform entity extraction
entities = ember_nlp.extract_entities(text)

# Print the entities
for entity in entities:
    print(entity)
