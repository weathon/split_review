Below is the final consolidated review.

---

## Summary

TimeRAG proposes a retrieval-augmented generation framework for time-series forecasting, applied to stock movement prediction. The key idea: use the LLM's generation probability of the correct token as a teacher signal to train a text embedder (BGE backbone) via contrastive learning with soft labels, addressing the absence of explicit retrieval ground truths in time-series data. Sequences are converted to JSON text, retrieved via the trained embedder, and fed as context to LLaMA3-8B for binary (rise/fall) prediction.

---

## Strengths

- **Principled response to a genuine bottleneck.** The paper identifies a real problem: time-series data lack explicit retrieval ground truths (unlike text QA pairs), making standard RAG training inapplicable. Using the LLM's own generation probability P(c) as a teacher signal for retriever training (Section 3.3, Eq. 1) is a specific, reproducible mechanism that directly targets this gap. This is the paper's strongest contribution.

- **Systematic prompt optimization.** Section 4.4.1 (Table 5) tests 8 prompt configurations scored using mean top-3 P(c) of correct predictions, providing an objective basis for prompt design. This goes beyond ad-hoc prompt engineering common in prior work.

- **New benchmark covering recent conditions.** Stock23 (51 stocks, 2022–2023 data) extends evaluation beyond the 2014–2020 window of existing datasets, improving temporal diversity of the evaluation.

---

## Weaknesses

### Fatal
None.

### Major

1. **No fine-tuning baselines for retrieval models.** All retrieval baselines (Instructor, BGE, LLM-Embedder, E5-mistral-7b-instruct) are used off-the-shelf without fine-tuning on stock data. TimeRAG is fine-tuned on the same stock data using LLM feedback. The experiment cannot distinguish whether TimeRAG's advantage comes from its specific LLM-feedback training signal or simply from any task-specific fine-tuning. The critical missing comparison: BGE fine-tuned on stock data with a simpler objective (e.g., supervised contrastive learning on next-day movement). Even LLM-Embedder (fine-tuned with LLM feedback on *text* tasks) is not fine-tuned on stock data. This is the single largest weakness in the empirical evaluation.

2. **No statistical rigor.** The paper reports single-point ACC and MCC values (Table 3) without standard deviations, confidence intervals, or significance tests. Stock movement prediction has notoriously high variance across stocks and time periods. Without uncertainty quantification, the observed differences between TimeRAG and baselines cannot be assessed for meaningfulness.

3. **Ablation study does not ablate the proposed method's core components.** Section 4.4 examines prompt design (order, feature naming, feature inclusion). It does not ablate: (a) the LLM-feedback-based candidate selection, (b) the knowledge distillation / soft-label training, (c) the contrastive loss function, or (d) the choice of embedding backbone. The key ablation — "what happens if we train the same BGE backbone on stock data without the LLM-feedback signal?" — is absent. This makes it impossible to attribute performance to the claimed mechanism.

4. **No comparison against non-LLM time-series or stock prediction models.** The paper restricts to LLM-based retrieval baselines. There are no comparisons against standard models (LSTM, Transformer, TimesNet, PatchTST) or specialized stock prediction models. This would provide a crucial sanity check on whether the RAG+LLM pipeline is competitive with simpler, established approaches.

### Minor

1. **Overstated "first" claim.** Contribution 1 claims "the first retrieval-augmented generation approach specifically tailored for time-series forecasting." The pipeline converts time-series to JSON text and applies standard text-RAG machinery (text embedder → contrastive learning → LLM). The core training technique (LLM-feedback-based distillation via soft labels) is directly inspired by Zhang et al. (2023)/LLM-Embedder (cited in the paper). The time-series-specific adaptation is the data-formatting step and the use of P(c) as the teacher score — an incremental contribution, not a first-of-its-kind framework.

2. **Framing mismatch: "forecasting" vs. binary classification.** The title, abstract, and introduction frame the contribution broadly as time-series *forecasting*, but the evaluation is on binary stock *direction* prediction (rise/fall) using ACC and MCC. While directional prediction is a form of forecasting, the paper implies general forecasting capability (e.g., "our method uniquely applies to continuous and complex temporal sequences") that is not demonstrated. No continuous forecasting metrics (MAE, RMSE, sMAPE) are reported.

3. **Temporal ordering of candidates not clarified.** Section 3.2 states the candidate pool is "all sequences from the past year of query stock" but does not specify whether candidates are guaranteed to be temporally prior to the query date. If a candidate from after the query date is used during training, this introduces data leakage.

4. **No ablation of the soft-label vs. hard-label training.** A comparison between the proposed soft-label training (using P(c) as weights) and a hard-label variant (uniform weighting of top-1 positive vs. negatives) would isolate whether the soft weighting contributes meaningfully. This is the most directly informative ablation for the claimed contribution.

5. **Absolute performance is low and not contextualized.** MCC values of 0.140–0.219 are positive but modest. The freeze-day filtering (movements between -0.5% and +0.55%) follows prior work conventions but removes an undisclosed fraction of data; results on unfiltered data are not reported.

### Trivial
- Equation (1) is described as "KL divergence" but is cross-entropy loss with soft labels. The two are equivalent up to an additive constant (the entropy of the target distribution) when minimizing, so this is a minor technical imprecision.
- GPT-4 is mentioned in the results discussion (Section 4.2) but not listed in experimental settings (Section 4.1), making the comparison protocol unclear.

---

## Nice-to-Haves
- Comparing against the same embedding models fine-tuned on stock data with a simpler objective would be the most informative ablation.
- Reporting results on unfiltered data (including "freeze" days) would provide a more complete picture of real-world performance.
- A discussion of computational cost (the method requires running LLaMA3-8B to score all candidates during training) would help assess practical trade-offs.

---

## Removed Points
These points were raised by reviewers but are removed as noise or based on verified misunderstanding:

- **"This paper does not evaluate time-series forecasting"** — Removed. Stock price direction prediction is a valid form of time-series forecasting. The paper transparently defines the task in Section 2. The overclaim about general forecasting capability is handled in Minor weakness 2.
- **"Top-1 positive / bottom-15 negative selection is arbitrary"** — Removed. This is a standard design choice in contrastive learning; no detailed justification is required beyond what is given.
- **"Prompt optimization on 10 examples risks overfitting"** — Removed. This is a prompt *exploration* step on a held-out toy set; the selected prompt is evaluated on a separate test set, which is standard methodology.
- **Missing appendix/proofs/related works** — Removed per instructions (parser strips these; they exist in the original submission).

---

## Novel Insights
None beyond the paper's own contributions. The synthetic reviews do not surface an observation about the method not already contained in the paper itself.

---

## Suggestions
1. Add fine-tuned versions of baseline embedders (particularly BGE and LLM-Embedder trained on stock data) to isolate whether the LLM-feedback signal adds value over generic task-specific fine-tuning.
2. Report standard deviations or confidence intervals across stocks/time periods for all metrics.
3. Ablate the core components: (a) hard labels vs. soft labels (P(c) weighting), (b) contrastive loss vs. alternative objectives, (c) the same BGE backbone fine-tuned with a simple supervised objective.
4. Clarify temporal ordering: specify whether all candidate sequences are guaranteed to be temporally prior to the query date.
5. Add at least one non-LLM time-series forecasting baseline (e.g., LSTM, Transformer) for context.
6. Re-frame the title and claims to match what is actually evaluated (stock movement prediction) rather than the broader "time-series forecasting."
7. Report the fraction of data removed by the freeze filter and provide metrics on unfiltered data.

---

## Score and Decision
MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>