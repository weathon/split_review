## Summary
The paper investigates the "auto-consistency" of Large Language Models (LLMs) by evaluating whether the tokens they identify as important for a classification decision (self-explanations) are functionally aligned with their predictive behavior. The authors propose a framework using three metrics—Sufficiency, Comprehensiveness, and Counterfactuality—adapted for scalar review scores (1-10) to measure how isolating, removing, or inverting these tokens affects model output. Experiments across five LLM families (GPT-4o, Gemma, Granite, DeepSeek) on sentiment analysis datasets reveal that while some models (GPT-4o) show high functional consistency, others (DeepSeek) exhibit structural contradictions or over-sensitivity to their own highlighted features.

## Strengths
- The paper addresses a critical gap in LLM interpretability: the distinction between "plausible" explanations (narrative) and "faithful" explanations (functional).
- The experimental design is rigorous, utilizing a diverse set of models (closed-source vs. open-source, varying parameter scales) and two distinct datasets (IMDB and Steam).
- The adaptation of ERASER-style metrics (Sufficiency/Comprehensiveness) to a scalar "review score" (1-10) rather than just class probabilities is a practical contribution that bypasses the lack of logit access in proprietary APIs.
- The inclusion of a Counterfactuality metric via semantic inversion (WordNet/negation) provides a more robust test of feature importance than simple erasure, which can often introduce out-of-distribution artifacts.

## Weaknesses
### Fatal
None.

### Major
- **Lack of Baseline Comparison:** The paper evaluates the "auto-consistency" of the model's *self-identified* features but does not compare these results against standard feature attribution methods (e.g., Leave-One-Out, or Gradient-based methods for open-source models). Without a baseline, it is difficult to determine if the observed "inconsistency" is a failure of the model's self-explanation capability specifically, or a general property of how these models handle text perturbations.
- **Potential for Prompt Sensitivity:** The "top features" are extracted via a specific prompt. The paper does not explore how sensitive the results are to the phrasing of the explanation request. If a different prompt yielded different tokens, would the "auto-consistency" scores change significantly? This limits the generalizability of the findings regarding specific model "families."

### Minor
- **Semantic Inversion Limitations:** The counterfactuality method relies on WordNet or "not" prefixes. This can result in ungrammatical or semantically awkward sentences (e.g., "not pay to win" vs "free to play"), which might trigger model sensitivity due to the change in fluency rather than the change in sentiment.
- **Ambiguity in Token Selection:** The paper mentions models identify "most relevant" tokens but does not specify a fixed number or a threshold. If one model selects 2 tokens and another selects 10, the Comprehensiveness and Sufficiency scores are not directly comparable across models.

### Trivial
- The distinction between "auto-consistency" and "self-consistency" is slightly semantic, as the latter is already used in literature to describe various forms of internal logic, though the authors' definition is clear within their context.

## Nice-to-Haves
- A comparison between the LLM-selected features and human-annotated rationales (e.g., from the original ERASER benchmark) to see if "auto-consistent" models are also more "human-aligned."
- Analysis of whether Chain-of-Thought (CoT) improves or degrades these functional consistency metrics compared to direct feature extraction.

## Novel Insights
The most significant insight is the identification of distinct "failure profiles" in LLM explanations: the "Contradiction Profile" (seen in DeepSeek-1.5B), where tokens are neither sufficient to hold a prediction nor comprehensive enough to explain its loss, and the "Over-sensitivity Profile" (DeepSeek-14B), where the model's prediction hinges so brittlely on specific tokens that any perturbation causes a total collapse. This suggests that model scaling does not linearly improve explanation faithfulness; instead, it may transition a model from being incoherent to being over-reliant on a narrow set of features.

## Suggestions
- Include a "Random Token" baseline for the interventions. If removing random tokens produces similar $\Delta R$ to removing "important" tokens, the model's self-explanation is effectively meaningless.
- Clarify the average number of tokens extracted per model in Table 1 to ensure the "Sufficiency" and "Comprehensiveness" metrics are being compared on a level playing field.

## Score and Decision
The paper presents a well-executed empirical study on a timely topic. The methodology is sound, and the findings regarding the varying reliability of self-explanations across different model architectures provide valuable cautionary evidence for the community. While it lacks a comparison to traditional attribution methods, its focus on "behavioral" consistency via the model's own interface is a valid and useful perspective for the ICLR audience.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>