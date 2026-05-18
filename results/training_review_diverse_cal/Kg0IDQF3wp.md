Now I have verified all claims against the paper. Let me write the final consolidated review.

---

## Summary

This paper proposes LegoMT2, a framework for training massive multilingual machine translation models (435 languages) that combines three ideas: (1) a language grouping scheme that partitions 435 languages into 8 data-balanced groups, (2) a multi-way detachable architecture with one local encoder-decoder per group plus a shared global encoder-decoder (9 encoder-decoders at training time, 1.6B-param global-only at inference), and (3) a non-blocking (asynchronous) federated learning algorithm that pushes/pulls only the global parameters. The paper reports a 2.2 spBLEU improvement over a fine-tuned NLLB-200-1.3B baseline on Flores-101 and claims a 16.2× training speedup over distributed training of the same-size NLLB model.

## Strengths

- **Translation quality improvement is supported by controlled comparison.** Table 1 shows LegoMT2 outperforms Single-FT (fine-tuned NLLB-200-1.3B on the same training data) by 2.2 spBLEU on many-to-one and 2.5 spBLEU on one-to-many Flores-101 translations. The comparison is fair (same data, same inference-time parameter count). This provides empirical evidence that the proposed approach alleviates parameter interference relative to standard fine-tuning of a single model.

- **Scalability to 435 languages is demonstrated.** The paper constructs a 25B sentence-pair dataset covering 435 languages and trains a model on all of them, exceeding the language coverage of prior open-source MNMT systems. The evaluation acknowledges the inherent difficulty of evaluating 400+ languages and uses back-translation quality as a practical proxy.

- **Informative component-level analyses are provided.** Section 5 includes: (a) a comparison of similarity-based clustering vs. data-balanced vs. random language grouping (Table 5), showing that balanced data distribution matters; (b) an analysis of save/load interval effects (Figure 3), showing that too-infrequent parameter exchange hurts performance; and (c) an ablation showing that Dec-Flow (local decoder) improves low-resource translation (Table 4). These help justify specific design choices.

- **Practical initialization strategy.** Initializing both global and local modules from NLLB-200-1.3B and expanding the vocabulary from 256K to 490K via per-language BPE merging is a sensible way to leverage existing pretrained knowledge without training from scratch.

## Weaknesses

### Fatal

- **The 16.2× speedup claim is entirely unsubstantiated.** This is a headline contribution — stated in the abstract, listed as a contribution in the introduction (line 26: "achieves 16.2× speedups"), and repeated in the conclusion — yet the Experiments section (Section 4) reports **zero** training time measurements, wall-clock comparisons, throughput figures, or any data that would allow a reader to verify this claim. There is no definition of what "the distributed training method for the same-size NLLB" refers to (standard data-parallel training of NLLB-200-1.3B? A specific distributed configuration?), making the claim unfalsifiable even in principle. A core empirical contribution asserted without evidence is a fatal flaw that cannot be corrected in a rebuttal — it requires new experiments.

### Major

- **No ablation isolates the contribution of individual components.** The paper compares LegoMT2 to Single-FT, but these differ on **three** dimensions simultaneously: architecture (multi-way vs. single encoder-decoder), training procedure (federated vs. centralized), and data organization (grouped vs. single shard). Without ablations such as (a) training a single encoder-decoder under the same asynchronous FL scheme, or (b) training LegoMT2 in a centralized fashion, it is impossible to attribute the 2.2 BLEU gain to any specific component. The contribution structure is unclear.

- **Asynchronous training is not validated against a synchronous baseline.** Section 5's analysis (Figure 2) only shows that using stale global parameters from other clients for **inference** does not degrade quality — a substantially weaker claim than showing that asynchronous **training** converges to the same quality as synchronous training. Without a synchronous-FL baseline, the effect of staleness on convergence and the claimed advantage of asynchrony for training quality are unsubstantiated. (The speed advantage of asynchrony is separately unmeasured — see the fatal weakness above.)

- **Human evaluation claim is stated without supporting data.** Line 173 states "Human evaluation results show that the performance of LegoMT2 reaches commercial translators' performance" and describes a 0–5 rating protocol comparing Google/Baidu/LegoMT2/NLLB-200-1.3B on Chinese-centric translation, but provides **no** scores, sample sizes, inter-annotator agreement, or any tabulated results. This is a significant claim with zero empirical backing.

### Minor

- **Evaluation coverage for the 435 claimed languages is thin.** Flores-101 covers only 86 of the 435 languages. For the remaining languages, the paper relies on Back-spBLEU (Table 2), shown for only a handful of English-centric directions with no aggregated results across language families or resource tiers. The paper acknowledges the evaluation difficulty (line 144), but the gap between claiming support for "435 languages" and demonstrating it on a standard test set for <20% of them is substantial.

- **The speedup baseline is never defined.** The abstract refers to "the distributed training method for the same-size NLLB" without specifying which method, what hardware configuration, or what training setup this refers to. This is necessary context even if the speed data were reported.

- **Back-translation metric explanation is confusing.** The caption for Table 2 states "Lower S-T and higher S-S_b are better." While this follows from the logic of detecting source-copying, the paper does not provide concrete examples or a clear justification, making it hard for readers to interpret the results.

- **No per-language or per-group BLEU breakdown.** Table 1 only reports averages split into "H" (high-resource) and "L" (low-resource) categories. Without per-language or at least per-group results, it is not possible to assess whether gains are concentrated in a few languages or broadly distributed.

### Trivial

None.

## Nice-to-Haves

- A comparison to NLLB-200-54.5B on the overlapping Flores-101 languages would be informative to show how competitive a 1.6B-param inference model can be against a 54.5B MoE model.
- Convergence curves (BLEU or loss over training steps) for LegoMT2 vs. baselines would strengthen the claims.
- Analysis of communication overhead (parameters transferred per push/pull, frequency, comparison to standard all-reduce) would contextualize the claimed efficiency.

## Removed Points

- *"Algorithm 1 is referenced but not shown"* — The core text describes the PUSH/MERGE/PULL operations; the pseudocode was in an appendix stripped by the parser. This is a known artifact, not an author error.
- *"Missing comparison to NLLB-200-54.5B as a weakness"* — Comparing to a 54.5B MoE model trained on different data is a defensible scope choice. The paper's comparisons to models of comparable/smaller inference-time size are appropriate.
- *"Vocabulary expansion (256K→490K) overhead not evaluated"* — The parameter counts are explicitly broken down (line 151: #embedding = 0.5B). The initialization strategy is clearly described.
- *Strength about "significant training speedup"* — This strength conflicts with the verified fatal weakness (no evidence), so it is removed rather than listed as a strength.

## Novel Insights

The reviews converge on identifying a clear disconnect between the paper's ambitious claims and the empirical support provided. The most important structural observation is that the paper attempts three interconnected contributions (grouping, architecture, algorithm) but evaluates them only as a monolithic package against a single baseline that differs on all dimensions simultaneously. A second insight worth highlighting: the non-blocking FL algorithm's validation conflates two different claims — that stale parameters are harmless for *inference* (which Figure 2 tests) and that asynchronous training converges as well as synchronous training (which is untested). These are not the same thing.

None beyond the paper's own contributions.

## Suggestions

1. **Provide training time measurements.** Report wall-clock time, GPU-hours, or convergence steps for LegoMT2 and a well-specified distributed training baseline (e.g., standard data-parallel training of NLLB-200-1.3B on the same data with the same hardware). This is non-negotiable given the prominence of the speedup claim.

2. **Add controlled ablations.** At minimum: (a) a single global encoder-decoder trained under the same asynchronous FL scheme (removing the multi-way architecture), and (b) LegoMT2 trained with synchronous parameter aggregation (removing asynchrony). This would clarify which component drives the BLEU gains.

3. **Either report full human evaluation data or remove the claim.** A statement about reaching "commercial translators' performance" without scores, sample sizes, or statistical tests cannot be evaluated.

4. **Provide a per-language or per-group breakdown** of Flores-101 results, and expand Back-spBLEU evaluation to cover a stratified sample across all 8 language groups.

5. **Define the speedup baseline explicitly** ("distributed training method for the same-size NLLB → standard data-parallel training of NLLB-200-1.3B on $N$ GPUs with configuration $X$").

6. **Clarify the Back-spBLEU metric** with a concrete example showing why lower S-T is desirable (e.g., a degenerate model that copies the source would have high S-T but low utility).

## Score and Decision

**Score: 4.0** — A clear reject in its current form. The paper presents a creative combination of ideas for massive multilingual MT, and the BLEU improvements on Flores-101 are promising. However, the headline speedup claim — one of two core contributions — has zero experimental support. The ablation gap prevents attribution of the BLEU gains. The unsubstantiated human evaluation claim weakens credibility. These issues are too fundamental to address in a rebuttal; they require new experiments. With proper speed measurements, ablations, and evaluation coverage, this could become a strong contribution.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>