## Summary

The paper introduces a two-stage voting architecture for suicide risk detection on social media. Stage 1 uses a fine-tuned BERT classifier with length–confidence routing to resolve high-confidence explicit cases cheaply; Stage 2 escalates ambiguous (implicit) posts to either an LLM voting ensemble (pathway a) or a combination of BERT with ML classifiers trained on LLM-extracted psychological features (pathway b). On an explicit-dominant Reddit dataset and a synthetic implicit-only dataset (DeepSuiMind), the framework achieves high F1 scores (98–99%) with small cross-domain gaps while reducing LLM calls by routing many inputs away from the expensive models.

## Strengths

- **Well-motivated problem and design** – The paper clearly identifies the efficiency–accuracy trade-off in detecting implicit suicidal ideation and proposes a cascaded architecture that is both intuitive and practically appealing.
- **Multifaceted stage‑2 pathways** – Offering two distinct strategies (LLM voting for maximum recall and ML voting for balanced efficiency/interpretability) provides useful flexibility for different deployment constraints.
- **Psychologically grounded feature extraction** – Converting LLM‑derived indicators (intent, distress, metaphor, etc.) into structured vectors is a clean way to inject clinical domain knowledge into classical classifiers, enhancing interpretability.
- **Strong empirical results on the presented data** – The two-stage variants consistently outperform single models on the metrics reported, especially in cross-domain gaps, and the convex‑optimised weight selection is a principled way to build the ML ensemble.

## Weaknesses

### Fatal

None.

### Major

1. **Synthetic implicit dataset** – DeepSuiMind is entirely generated (not real user content). All posts are artificially constructed using cognitive frameworks (D/S‑IAT, ANT). The paper treats it as the exclusive implicit benchmark, so the claimed “99.7% F1 on implicit cases” and the generalisation conclusions may not transfer to real‑world implicit expressions. This severely limits the external validity of the empirical evaluation.

2. **Misleading cost analysis** – The paper claims LLM cost is lowered because Stage 1 resolves ~67.6% of inputs, but this ignores the fact that **the fundamental‑feature extraction itself requires an LLM call for every sample** (including Stage 1 and train/val data). Pathway (b) may avoid per‑post LLM voting, but the one‑time extraction still incurs substantial cost that is not accounted for. The “reduction” is not properly quantified, and the overall cost picture is incomplete.

3. **Reddit dataset is not a pure implicit test** – Reddit is described as explicit-dominant; the paper does not provide evidence that its Stage 2 subset actually contains meaningful implicit cases. Combined with the synthetic nature of DeepSuiMind, the “cross‑domain” gap essentially compares a real explicit dataset against a synthetic implicit one, which weakens the claim of robustness.

### Minor

- **No evaluation on a real implicit corpus** – The paper would be stronger with at least one naturalistic implicit dataset (e.g., posts flagged by moderators as concerning but lacking explicit keywords).
- **LLM variant details are sparse** – No temperature, top‑p, or exact version strings are reported for GPT‑5 and GPT‑4o‑mini, making reproduction harder.
- **Ablation of feature extraction** – The effectiveness of the six extracted psychological dimensions is shown only via distribution plots and a simple feature‑importance chart; no controlled comparison (e.g., using only BERT embeddings, or removing one feature at a time) is conducted.

### Trivial

- The text length as a “reasoning complexity” proxy is very coarse; the paper acknowledges this but provides no alternative analysis (e.g., using a BERT‑based complexity score).

## Nice-to-Haves

- Validate on a real implicit benchmark (e.g., CLPsych shared tasks or manually annotated ambiguous posts) before deployment.
- Include a complete cost model (dollars or tokens) that accounts for the fundamental‑feature extraction across the whole pipeline.
- Run a controlled ablation that removes each psychological feature to measure its marginal contribution.

## Novel Insights

The observation that implicit suicidal ideation is characterised by very high metaphor usage (0.955 vs. 0.076 for explicit), 100% high emotional distress, and longer narrative reasoning offers a concrete, clinically interpretable distinction. This finding could guide future data collection and feature engineering, even though it is derived partly from synthetic data.

## Suggestions

- Replace or supplement DeepSuiMind with a real implicit dataset (e.g., from crisis helpline logs or moderated social media forums) to ground the claims in authentic language.
- Clearly separate the cost of LLM‑based feature extraction from the cost of per‑post LLM decision calls, and report both. A fair comparison should include the extraction overhead.
- Provide a more thorough analysis of the false negatives and false positives on both explicit and implicit subsets to understand where the two‑stage system still fails.

## Score and Decision

The paper addresses an important problem with a pragmatically designed architecture and introduces a useful technique for extracting structured psychological features. However, the empirical evaluation rests on a synthetic implicit dataset, and the cost analysis omits the significant overhead of LLM‑based feature extraction. These weaknesses substantially weaken the support for the core claims. Therefore the paper is below the acceptance threshold in its current form.

**Score:** 4  
**Decision:** Reject

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>