## Summary

This paper presents a systematic zero-shot evaluation of 31 open-weight LLMs on five-class sentiment polarity detection using two canonical benchmarks (SemEval-2017 Task 4C and SST-5). The evaluation jointly measures classification accuracy (and Macro-Average MAE) against inference throughput (instances/second), surfacing Pareto-optimal models. The main empirical finding is that several contemporary open-weight LLMs, without any fine-tuning or specialized prompting, exceed the previously reported best Accuracy and Macro-Average MAE on SemEval while approaching the SST-5 state-of-the-art.

---

## Strengths

- **Breadth of evaluation:** Testing 31 open-weight models across diverse families (Llama, Gemma, Qwen, Mistral, Phi, OLMo, DeepSeek, etc.), parameter scales (2B–32B), and architecture variants (dense, MoE, GQA, SWA, MLA) provides a genuinely comprehensive snapshot of the current open-weight LLM landscape for this task.
- **Cost-performance framing:** The Pareto frontier approach simultaneously considering throughput and accuracy is a practically useful way to present results for the deployment decision-making of practitioners. The per-class ordinal metric (Macro-Average MAE) is well motivated for the imbalanced, ordinal nature of both datasets.
- **Reproducibility:** The paper discloses the exact prompts (Appendix A and B), hardware specifications, discard policy for unparseable outputs, and full per-model tables, enabling replication.

---

## Weaknesses

### Fatal
None that completely invalidate the results.

### Major

1. **Questionable SOTA baseline for Accuracy on SemEval.** The primary accuracy SOTA comparison (0.542) is attributed to Das & Pedersen (2024), explicitly noted as "yet unpublished." Competing against an unpublished, un-peer-reviewed preprint to claim new state-of-the-art is methodologically weak. Moreover, SemEval-2017 Task 4C had many published competition entrants in 2017; the paper does not situate its accuracy claim against those. The jump from 0.542 to 0.619 is striking, but without a robust published baseline the claim is hard to assess.

2. **Single-prompt, no sensitivity analysis.** All 31 models are evaluated with a single fixed zero-shot prompt (Appendices A/B). LLM performance on classification tasks is known to be sensitive to prompt wording and label verbalization. Without at least two or three prompt variants, it is unclear whether the observed model rankings reflect genuine capability differences or prompt-specific artifacts. This is particularly relevant for models that score poorly.

3. **Hardware-constrained throughput comparison.** All throughput measurements are taken on a single NVIDIA RTX A5500 (24GB VRAM). Larger models (e.g., 27B–32B) that exceed available VRAM must be quantized or offloaded, while smaller ones (2B–8B) run natively. The paper does not disclose quantization levels or memory footprints, making the "instances per second" metric incomparable across parameter scales and potentially misleading for cost analysis.

4. **No statistical significance or variance estimates.** The paper reports single-run point estimates. Without confidence intervals, bootstrapped significance tests, or multiple runs, there is no way to determine whether performance differences between closely ranked models (e.g., Accuracy 0.619 vs. 0.610) are meaningful or within random variation.

### Minor

1. The paper does not discuss the possibility of test-set contamination: several evaluated models (Gemma3, Qwen2.5, etc.) were trained on large crawls that plausibly include SST-5 or SemEval-2017 data, which could inflate zero-shot scores.
2. The "instances per second" metric captures end-to-end wall-clock throughput but conflates generation length, batching behavior, and hardware utilization. A per-token throughput or FLOPs estimate would allow fairer cross-architecture comparisons.
3. Both datasets are English-only. The conclusion that "specialized fine-tuned models may not always be necessary" is an overgeneralization beyond this narrow scope.

### Trivial
The tables in Figure 2 contain what appear to be duplicate rows (e.g., gemma3_27b, gemma3_12b, gemma2_9b each appear twice), likely a parser artifact.

---

## Nice-to-Haves

- A brief ablation over 2–3 prompt variants to quantify prompt sensitivity.
- Reporting memory footprint and/or quantization level alongside throughput, to make the Pareto analysis actionable for hardware-constrained practitioners.
- Evaluating at least one few-shot (k=5) setting to bound the gap with fine-tuning more tightly.
- Statistical significance tests (e.g., McNemar's test) between top-ranked models.

---

## Novel Insights

The most interesting finding is the asymmetric generalization pattern: modern open-weight LLMs excel on the informal, topic-anchored SemEval tweets (achieving clear SOTA-level accuracy) but still fall ~3–4 points short of SOTA on SST-5's syntactically complex movie reviews. This suggests that zero-shot LLMs handle pragmatic, contextual sentiment more fluently than fine-grained compositional sentiment (negation, contrastive syntax), which would be worth investigating further. The Pareto analysis also reveals that mid-sized models (gemma2-27b, qwen2.5-32b) dominate the frontier — larger-than-expected models relative to the task difficulty — suggesting that accuracy improvements from scale are not yet saturated for ordinal sentiment. Beyond these observations, the paper's novel content lies primarily in its breadth of coverage rather than conceptual novelty.

---

## Suggestions

- Clarify the SemEval accuracy SOTA claim by either citing published competition results or explicitly acknowledging that the chosen baseline is a preprint and framing the finding more cautiously.
- Add a paragraph discussing the hardware/quantization setup for each model tested, especially models near the 24GB VRAM limit.
- Run each model with at least two prompt formulations and report the variance in rankings to establish robustness.
- Include a contamination analysis or at minimum a discussion of the risk.

---

## Score and Decision

This is a competently executed empirical benchmarking study with clear practical value, but it has significant methodological gaps: the SOTA comparison rests on an unpublished baseline, there is no prompt sensitivity analysis, quantization details are absent, and there are no significance tests. The contribution is primarily "we ran many models on two well-known benchmarks" — an observation that is useful but lacks the depth in methodology, analysis, or novel findings typically expected at ICLR. The paper would be a strong fit for a workshop or empirical tracks of lower-tier NLP venues.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>