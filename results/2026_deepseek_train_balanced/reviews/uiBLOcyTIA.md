## Summary

This paper proposes NextLocLLM, a model for next-location prediction that replaces discrete location IDs with normalized spatial coordinates and integrates a partially-frozen GPT-2 backbone. The method adds LLM-enhanced POI embeddings (using the embedding layer of an LLM to encode natural-language descriptions of POI categories) and a KD-tree retrieval module to convert predicted coordinates into structured top-k outputs. Experiments on three public datasets (Xi'an, Chengdu, Japan) and one private dataset (Singapore) show competitive results in both fully-supervised and zero-shot settings.

---

## Strengths

- **Spatial coordinates enable genuine cross-city generalization that ID-based methods cannot achieve.** The zero-shot experiment (Table 2) shows NextLocLLM trained on Chengdu → tested on Xi'an achieves 37.02% Hit@1 / 82.26% Hit@5 / 92.41% Hit@10 with a 449.79m average distance error, while prior ID-based prompt-only methods cannot transfer because identical IDs map to entirely different locations in different cities. This is a concrete and validated contribution.

- **The ablation study cleanly validates the design choices.** Table 4's 3-factor ablation (prompt prefix, LoRA vs. freezing, LLM-enhanced POI) shows the best configuration (freezing + prompt prefix + POI) reaches 58.14% Hit@1, while removing all components drops to 25.81%. The freezing strategy consistently outperforms LoRA (e.g., 58.14% vs. 38.11% in the closest LoRA variant), supporting the claim that preserving pre-trained knowledge in core LLM layers while adapting peripheral layers is more effective. Table 5 further verifies that each input feature (time, duration, POI) contributes positively.

- **The KD-tree retrieval module solves the LLM output-format inconsistency that plagues prompt-only approaches.** LLMMob with strict output format enforcement ("s" suffix) drops from 33.52% to 20.81% Hit@1 on Xi'an, while NextLocLLM's coordinate-regression + KD-tree approach avoids this entirely by design.

- **Three systematic ablation studies** (key components, input features, trajectory segmentation) independently verify the contribution of each design choice, providing clear evidence for the architecture's rationale.

---

## Weaknesses

### Fatal
None.

### Major
- **The "LLM-enhanced POI embeddings" do not meaningfully leverage LLM capabilities.** The method extracts token embeddings from the LLM's *embedding layer only*, applies frequency-weighted averaging, and passes through an MLP. There is no attention, no cross-POI interaction, no transformer processing of the POI descriptions — any pre-trained static embedding model (Word2Vec, GloVe, fastText) could be substituted with essentially the same effect. The paper's framing ("utilizes LLMs' ability to encode... leveraging the representational power of LLMs") is misleading: the embedding layer alone does not constitute reasoning or comprehension. This inflates the claimed novelty of a core contribution.

- **The claim about Llama2-7B and Llama3-8B backbone consistency is stated without any quantitative evidence.** Line 346: "We also utilized other LLMs (Llama2-7B and Llama3-8B) as the backbone for NextLocLLM and found that their prediction performances are relatively consistent compared to using GPT-2." No numbers, table, or figure support this claim. For a paper whose central contribution is integrating an LLM backbone, this is a significant empirical gap — especially since GPT-2 (124M parameters) and Llama3-8B differ by two orders of magnitude. The reader cannot assess whether the approach generalizes across architectures.

### Minor
- **No measure of variance or statistical reliability is reported for any result.** All values in Tables 1–5 are single percentages with no standard deviations, confidence intervals, or indication of the number of random seeds. Given the substantial variation in the ablation table (e.g., removing prompt prefix at fixed freezing+POI drops Hit@1 from 58.14% to 45.79%), the reader cannot distinguish reliable improvements from noise. This is a basic expectation for an empirical paper proposing a new method.

- **Baseline results in the zero-shot table (Table 2) are identical to the supervised table (Table 1) without explanation.** Every LLMMob and ZS-NL value for Xi'an is duplicated verbatim across both tables (e.g., LLMMob(wt): 33.52%/77.86%/78.00% in both). While this is *explainable* — LLMMob and ZS-NL are prompt-based methods that do not train on source-city data, so their outputs are naturally identical regardless of the table's label — the paper never states this. The reader is left to infer whether the baselines were actually run in a zero-shot protocol. This undermines trust in the experimental reporting.

- **Critical experimental details are missing, hindering reproducibility.** No hyperparameters are reported: no learning rate, batch size, optimizer, number of epochs, or embedding dimension values ($d_{llm}$, $d_{xy}$, $d_t$, $d_d$, $d_{dur}$, $d_{poi}$). Dataset statistics (number of users, locations, records, time span, grid resolution, POI category count) are absent — the paper only provides qualitative descriptions (e.g., "Xi'an and Chengdu datasets have more users, a longer time span, and shorter average sampling intervals").

- **The KD-tree retrieval module's error contribution is never analyzed.** Since the model predicts coordinates and retrieves the nearest locations, prediction errors could stem from either inaccurate coordinate regression or the KD-tree mapping selecting a wrong nearby location. No analysis separates these effects.

### Trivial
- No discussion of computational cost (training/inference time, parameter counts) is provided despite using an LLM backbone, which has very different resource requirements than the baselines.

---

## Nice-to-Haves
- Including a variant that replaces the LLM embedding layer with a standard static embedding (e.g., Word2Vec, GloVe) for the POI descriptions would clarify whether the LLM's embedding layer specifically is adding value over any pre-trained embedding.
- An ablation replacing GPT-2 with a randomly-initialized transformer of the same architecture would reveal whether pre-trained knowledge in the frozen LLM backbone matters or whether any transformer suffices.
- The geographic distance error limitation (mentioned in the conclusion as >200m) could be contextualized earlier in the paper to set expectations.

---

## Removed Points
- **Zero-shot evaluation "structurally unfair" claim (Harsh Critic).** The critic argues that comparing NextLocLLM trained on City A against prompt-only baselines that receive no training is unfair. This is incorrect: both methods have not seen Xi'an training data, making this a standard (and valid) zero-shot evaluation. The core issue (duplicate numbers) is retained as a Minor weakness.
- **Definition 2.2 incomplete (Harsh Critic).** This appears to be a parser artifact (the definition exists in the comment block at lines 163–167). The commenting-out of some definitions is a formatting issue, not a content problem.
- **Normalization being dataset-dependent (Harsh Critic).** The paper explicitly discusses and justifies this design choice (lines 240–242), including a figure reference. This is a deliberate design decision, not an oversight.
- **"First model" claim overstated (Harsh Critic).** The paper states "the first model to integrate LLM in next location prediction structure, without solely using prompts." This is accurate — prior work (LLMMob, ZS-NL) uses prompts to query LLMs without integrating them into the model structure.
- **Singapore dataset as a weakness (Harsh Critic).** The paper acknowledges the dataset limitations honestly and includes the failure case rather than cherry-picking only favorable results. This is good scientific practice.
- **LoRA degradation as a weakness (Harsh Critic).** The ablation shows that freezing outperforms LoRA — this is a *finding* that validates the paper's design choice, not a weakness. The paper discusses this on line 506.
- **Basic model achieving 97.54% Hit@10 as a weakness (Harsh Critic).** The baseline model without proposed components achieves strong Hit@10 but only 25.81% Hit@1. The proposed components substantially improve Hit@1 (to 58.14%), which is the harder and more meaningful metric. This pattern is standard for next-location prediction.

---

## Novel Insights

The most interesting observation from the synthesis of reviews is the tension between the paper's framing and its actual technical depth. The paper claims to "integrate LLMs" into the prediction structure, but the LLM is used in two shallow ways: (1) the POI embeddings access only the token embedding layer (no transformer processing), and (2) the backbone's self-attention and FFN layers are frozen, limiting adaptation to positional encoding and layer norm. The ablation actually shows that the larger gains come from freezing (vs. LoRA) rather than from the "LLM" nature of the backbone — a randomly initialized transformer of similar size might perform similarly. The paper's results are real, but the claimed "leveraging of LLM capabilities" is largely branding of fairly standard techniques. This gap between framing and implementation is broader than either individual review captured.

---

## Suggestions
1. **Provide evidence for the Llama backbone claim** — at minimum, a single row showing Hit@k results for Llama2-7B and Llama3-8B on one dataset.
2. **Report all results as mean ± std over multiple runs** (3–5 seeds) to establish statistical reliability.
3. **Explain in the text why the zero-shot baseline numbers match the supervised numbers** — a brief sentence clarifying that LLMMob and ZS-NL are prompt-only and thus produce identical outputs regardless of the table framing would resolve the concern.
4. **Add a table of dataset statistics** (number of users, locations, records, time span, grid size, POI categories) and **report all hyperparameters** used in experiments.
5. **Acknowledge the shallow use of the LLM for POI embeddings** and either (a) show that deeper LLM processing (e.g., passing descriptions through transformer layers) does not help, or (b) reframe the contribution more honestly as using pre-trained embeddings rather than "LLM capabilities."

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>