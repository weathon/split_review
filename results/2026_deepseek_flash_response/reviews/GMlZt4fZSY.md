## Summary

This paper presents a data-centric framework for training sub-billion-parameter reasoning models using ~4.2T tokens of curated open-source data. The multi-stage pipeline includes leave-one-out (LOO) analysis for dataset selection, influence-based cross-capability data mixing, and data-model co-evolution for mid-training compression. The trained MobileLLM-R1 models (140M–950M) achieve strong reasoning performance, notably outperforming larger fully-open baselines (OLMo-2-1.48B, SmolLM2-1.7B) under identical reasoning SFT (Table 2) and matching/surpassing Qwen3-0.6B on several benchmarks with ~11.7% of the training tokens.

## Strengths

1. **Clean controlled comparison isolating pretraining effects (Table 2)**: Under identical reasoning SFT data (OpenMathReasoning + OpenScienceReasoning-2 + OpenCodeReasoning-2, one epoch), MobileLLM-R1-950M (949M params) outperforms OLMo-2-1.48B (MATH: 57.8 vs 53.0), SmolLM2-1.7B (MATH: 57.8 vs 41.4), and others on MATH, GSM8K, and LiveCodeBench. This cleanly attributes the gains to pretraining/mid-training rather than post-training data differences.

2. **Non-obvious cross-domain data insights from LOO analysis**: Figure 3 shows that StarCoder benefits math performance more than OpenWebMath benefits code — a reversal of common assumptions. FineWeb-Edu shows the largest cross-domain degradation when removed, revealing its "glue" role across capabilities. These findings are concrete and reusable.

3. **Token efficiency against proprietary baselines is substantiated**: MobileLLM-R1-950M surpasses Qwen3-0.6B on HumanEval (46.3% vs 30.5%) and shows substantial gains on LiveCodeBench, while using 4.2T tokens (the paper is transparent that 4.2T is on ~2T unique tokens, explicitly stated in the abstract).

4. **Data-model co-evolution convergence criterion**: The observation that influence scores concentrate around zero as training progresses (Figure 5) provides a principled stopping criterion grounded in the data itself.

5. **Open-source release commitment**: The paper commits to releasing all datasets, model weights, and training code, enabling exact reproduction.

## Weaknesses

### Fatal
None.

### Major

1. **No end-to-end ablation isolating the proposed methodology from simpler alternatives (structural gap)**: The paper claims a novel "benchmark-free, self-evolving data optimization" framework (LOO + influence-based mixing + data-model co-evolution) but never trains a baseline that simply uses uniform sampling of the same high-quality data without the proposed components, at the final 4.2T training scale. The headline results could be driven entirely by (a) the selection of high-quality constituent datasets, (b) multi-epoch training on ~2T unique tokens, or (c) the post-training recipe (from prior work). Without this ablation, the central *methodological* claims are unsupported. This is not a minor omission — the paper claims a principled framework but does not demonstrate that the framework is responsible for the gains.

2. **Influence-based data mixing validated only at proxy scale**: Figure 4 compares "Datamix" vs uniform sampling only at 500K steps on perplexity of probing sets. There is no demonstration that this mixing strategy improves *final benchmark performance* at the actual 4.2T training scale. The connection between proxy-scale perplexity improvements and final-model benchmark gains is asserted, not shown.

3. **Mid-training compression validated only on MMLU, not reasoning benchmarks**: Figure 6 evaluates data compression on MMLU (a knowledge benchmark). The paper's stated focus is *reasoning* (code, math), yet the mid-training validation uses none of the paper's own key reasoning benchmarks (MATH, GSM8K, HumanEval, AIME). The unexplained performance dip in the "original" line around 30K steps on MMLU (Figure 6, going from 38.0→31.0 at step 40K) also warrants explanation — it may indicate a learning rate artifact rather than a property of the data.

4. **No decontamination or benchmark leakage analysis**: The reasoning SFT datasets (OpenMathReasoning, OpenCodeReasoning-2, OpenScienceReasoning-2) and Dolmino mid-training data likely contain examples similar to or overlapping with MATH, GSM8K, HumanEval, and AIME benchmarks. The paper reports no n-gram overlap or embedding-based contamination analysis. Given that the central results depend on these benchmarks, this is a significant omission.

### Minor

1. **Computational cost of the methodology not reported**: The paper reports FLOPs for final models but not the overhead of LOO analysis (7+ training runs), three domain-specialized models trained to convergence for influence computation, and iterative mid-training compression. A practitioner evaluating whether to adopt this methodology needs to know the total cost, not just the final run.

2. **Capability-probing datasets not validated against benchmarks**: The LOO analysis uses NLL on probing datasets as a proxy for final benchmark performance, but the paper never demonstrates that NLL reductions on these probing sets correlate with improvements on held-out reasoning benchmarks (MATH, GSM8K, HumanEval). The chain NLL → probing → benchmark is assumed.

3. **"Benchmark-free" framing is somewhat overstated**: While the paper avoids using traditional benchmarks during training, the capability-probing datasets are constructed via classifiers (FineWeb-Edu classifier) and LLM judges (Ask-LLM) that encode specific notions of reasoning quality — constituting a form of supervision that could introduce bias.

### Trivial

None.

## Nice-to-Haves

- Report total GPU-hours for the full development pipeline (LOO + influence models + mid-training), not just the final training run.
- Add scaling analysis: does the data curation methodology benefit 140M, 360M, and 950M models equally, or are gains concentrated at certain sizes?
- Validate mid-training compression on at least one reasoning benchmark (MATH or GSM8K).

## Removed Points

These points from reviewers were filtered out. Treat them with caution.

- **"AIME scores show roughly half performance vs Qwen3-0.6B"** — Removed. The comparison was derived from garbled PDF-extracted table columns. The paper's text characterizes the AIME comparison as "comparable" (line 386), not "matching," and the claim is "matches or surpasses *across multiple* reasoning benchmarks" (abstract), which is accurate (HumanEval 46.3 vs 30.5; LiveCodeBench gains). The specific Qwen3-0.6B AIME score for the post-trained model is not cleanly rendered in extraction.

- **"11.7% figure could mislead about unique vs total tokens"** — Removed. The abstract explicitly states "pre-training with 4.2T tokens on the dataset resampled from these ~2 T tokens." The paper is transparent about data repetition. Potential to mislead is speculative.

- **"Post-training data postdates Qwen3's training"** — Mostly removed. While this is a legitimate caveat for the Qwen3 comparison, the paper's Table 2 comparison against fully-open models (OLMo-2, SmolLM2) uses the same post-training data for all models and shows clear advantages, independently validating the pretraining contribution regardless of the Qwen3 comparison.

- **"Missing related work positioning"** — Removed as unverifiable without external sources; also, the paper cites and builds on relevant prior work.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add an end-to-end ablation**: Train a 950M model using uniform sampling of the same high-quality datasets (no influence-based mixing) and no mid-training compression, keeping post-training fixed. If performance drops substantially, the methodology is validated. If not, reframe the paper honestly as an empirical recipe paper documenting what is possible with careful data selection rather than as a novel method paper.

2. **Run decontamination analysis**: Report n-gram overlap and embedding-based similarity between training data (especially the SFT datasets) and evaluation benchmarks (MATH, GSM8K, HumanEval, AIME).

3. **Validate the probing datasets**: Show that NLL on the capability-probing datasets correlates with held-out benchmark performance, linking the LOO and influence analyses to the final results.

4. **Validate mid-training on reasoning benchmarks**: Reproduce Figure 6 using MATH or GSM8K instead of (or in addition to) MMLU.

---

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- *Lower band (<3.5)*: `Paramanu-Ganita` (2.33, Reject) — Small-domain math model with weak results and unsupported claims. Our paper is substantially stronger in scope, rigor, and results.
- *Middle band (3.5–7.5)*: 
  - `What Kind of Pretraining Data Do Large Language Models Rely on When Doing Reasoning?` (6.75, Accept) — Uses influence functions to analyze data for reasoning in 7B+ models. Cleaner methodological validation but narrower scope. Our paper has more practical impact but weaker component-level validation.
  - `At Which Training Stage Does Code Data Help LLMs Reasoning?` (7.25, Accept) — Systematic ablation study on code data impact. Cleaner experimental design but less impressive empirical results. Our paper is comparably scoped but with weaker methodological isolation.
  - `Textbooks Are All You Need` (Φ-1) (6.00, Reject) — Small model + curated data, similar spirit. Our paper has more methodological novelty but less rigorous validation of its methods.
  - `Small-to-Large Generalization` (5.25, Accept) — Study of training data influence across scale. Stronger in experimental design, weaker in empirical impact.
- *Upper band (>7.5)*: Various 8.0 papers — All unanimous accept papers with strong experimental methodology or theoretical contributions. Our paper does not reach this bar.

**Round 2 (Narrowing):** I placed the paper in the 4–7 range and retrieved anchors in (4.0, 6.5) and (5.5, 7.5):
- `Textbooks Are All You Need` (6.00, Reject) — Similar data-curation-motivation paper but with cleaner empirical demonstration and contamination analysis. Our paper is slightly weaker due to lack of ablations validating its methodology.
- `Small-to-Large Generalization` (5.25, Accept) — Clean experimental design, albeit narrower practical impact. Our paper has more practical significance but less rigorous validation.
- `Studying the Effects of Training Data on Small Language Models` (5.50, Reject) — More narrowly scoped. Our paper has broader scope and stronger results.

**Bracket:** Round 1 placed the paper between the weak anchor at ~2.3 and the strong anchor at ~7.25. Initial bracket: [4.0, 6.5].

**Narrowing:** After reading anchors, the paper sits below `Textbooks Are All You Need` (6.00) because its central methodological claims are not validated, and above `Paramanu-Ganita` (2.33) because its empirical contributions are genuine and well-supported. Among middle anchors, it is closest to `Small-to-Large Generalization` (5.25) but with more practical impact. The paper's primary weakness is the gap between claimed methodology and demonstrated evidence — a structural issue that prevents it from reaching the 6+ range.

**Final score: 5.0**

The paper has genuine empirical contributions (strong models, clean Table 2 comparison, useful LOO insights, open-source release). However, the central methodological claims about influence-based mixing and data-model co-evolution are not validated through proper ablations that isolate their contribution from simply using high-quality data and training longer. For a top venue like ICLR, this gap is significant. The paper would be stronger if reframed as an empirical recipe contribution rather than a novel method paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>