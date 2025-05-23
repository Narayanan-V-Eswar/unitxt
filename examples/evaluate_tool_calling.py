from unitxt import get_logger
from unitxt.api import evaluate, load_dataset
from unitxt.inference import (
    CrossProviderInferenceEngine,
)

logger = get_logger()


dataset = load_dataset(
    card="cards.bfcl.simple_v3",
    split="test",
    format="formats.chat_api",
)

model = CrossProviderInferenceEngine(model="granite-3-3-8b-instruct", provider="watsonx")


predictions = model(dataset)
results = evaluate(predictions=predictions, data=dataset)

print("Global Results:")
print(results.global_scores.summary)

print("Instance Results:")
print(results.instance_scores.summary)
