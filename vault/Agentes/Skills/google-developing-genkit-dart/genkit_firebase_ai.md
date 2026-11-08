---
tags:
  - ai/skill/doc
  - skill/google-developing-genkit-dart
skill: "google-developing-genkit-dart"
source: "references\genkit_firebase_ai.md"
updated_at: "2026-11-08T20:55:34.661Z"
---

# Documento: genkit_firebase_ai (Skill: google-developing-genkit-dart)

> [!NOTE] Documentação de suporte da skill **[[Visão Geral|google-developing-genkit-dart]]**.  
> **Caminho de origem:** `references\genkit_firebase_ai.md`

---

# Genkit Firebase AI Plugin (`genkit_firebase_ai`)

The Firebase AI plugin for Genkit Dart, used for interacting with Gemini APIs through Firebase AI Logic.

## Usage

```dart
import 'package:genkit/genkit.dart';
import 'package:genkit_firebase_ai/genkit_firebase_ai.dart';

void main() async {
  // Initialize Genkit with the Firebase AI plugin
  final ai = Genkit(plugins: [firebaseAI()]);

  // Generate text
  final response = await ai.generate(
    model: firebaseAI.gemini('gemini-flash-latest'),
    prompt: 'Tell me a joke about a developer.',
  );

  print(response.text);
}
```

