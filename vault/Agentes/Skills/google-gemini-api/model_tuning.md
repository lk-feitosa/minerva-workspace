---
tags:
  - ai/skill/doc
  - skill/google-gemini-api
skill: "google-gemini-api"
source: "references\model_tuning.md"
updated_at: "2026-11-08T06:43:45.390Z"
---

# Documento: model_tuning (Skill: google-gemini-api)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-gemini-api]]**.  
> **Caminho de origem:** `references\model_tuning.md`

---

# Model Tuning

Supervised Fine-Tuning using your own datasets.

Note: Not all models support tuning. Refer to https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning.md.txt for the list of supported models.

```python
import time
from google import genai
from google.genai import types

client = genai.Client()

training_dataset = types.TuningDataset(
    gcs_uri="gs://your-bucket/sft_train_data.jsonl",
)

tuning_job = client.tunings.tune(
    base_model="gemini-3.1-flash-lite",
    training_dataset=training_dataset,
    config=types.CreateTuningJobConfig(
        tuned_model_display_name="Example tuning job",
    ),
)

running_states = {"JOB_STATE_PENDING", "JOB_STATE_RUNNING"}
while tuning_job.state in running_states:
    time.sleep(60)
    tuning_job = client.tunings.get(name=tuning_job.name)

print("Tuned Model Endpoint:", tuning_job.tuned_model.endpoint)

# Predict with the tuned endpoint
response = client.models.generate_content(
    model=tuning_job.tuned_model.endpoint,
    contents="Why is the sky blue?",
)
print(response.text)
```

