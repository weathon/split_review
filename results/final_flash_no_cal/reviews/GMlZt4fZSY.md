Now I have all the information needed. Let me compose the final review.

## Summary

This paper presents a data-centric training recipe for sub-billion-parameter reasoning language models. The key methodological contributions are (1) a benchmark-free, influence-based data mixing strategy for pre-training that uses cross-capability influence scores to weight datasets, and (2) a data-model co-evolution approach for mid-training that iteratively filters samples and adjusts mixing ratios as the model evolves. The authors train MobileLLM-R1 models (140M–950M parameters) on ~4.2T tokens of curated open-source data and demonstrate that the 950M variant matches or surpasses Qwen3-0.6B on several reasoning benchmarks despite using only 11.7% of Qwen3's 36T-token training budget, while substantially outperforming all prior fully open-source sub-billion models.

## Strengths

1. **Impressive token efficiency.** MobileLLM-R1-950M achieves strong reasoning performance with 4.2T pre-training tokens — only 11.7% of Qwen3-0.6B's 36T tokens — while matching or exceeding it on key benchmarks (HumanEval base: 46.3% vs. 30.5%; MATH: 74.6 vs. 73.0). The Pareto-frontier plot (Figure 1) cleanly illustrates this efficiency advantage.

2. **Principled, benchmark-free data mixture optimization.** The paper formalizes a dataset-level weighting method via influence scores computed on *capability-probing datasets* (Eqs. 2–5), never exposing actual evaluation benchmarks during training or mixture construction. Figure 4 provides direct evidence that the resulting Datamix consistently yields lower perplexity than uniform sampling across Code, Math, and Knowledge probing benchmarks.

3. **Data-model co-evolution for mid-training with convergence evidence.** Section 3 describes an iterative compression procedure where the model itself is used to identify and retain only positively-influential samples. Figure 5 shows influence scores converging to near-zero after two stages, and Figure 6 demonstrates that the subsampled data produces higher and more stable MMLU scores than the original mid-training set, both with and without knowledge distillation.

4. **State-of-the-art results among fully open-source sub-billion models.** Table 2 shows that after identical reasoning SFT, MobileLLM-R1-950M* outperforms OLMo-2-1.48B-SFT (57.8% vs. 53.0% MATH) and SmolLM2-1.7B-Instruct (57.8% vs. 41.4% MATH), despite being significantly smaller. Figures 8–9 confirm these advantages across multiple benchmarks and model scales.

5. **Insightful leave-one-out analysis of data sources.** Section 2.1.2 (Figure 3) disentangles which corpora contribute to each reasoning capability, revealing that FineWeb-Edu is the most cross-domain impactful source and that StarCoder benefits math more than OpenWebMath benefits code — a reversal of common assumptions.

6. **Rigorous post-training ablation.** Table 1 systematically ablates the order and composition of fine-tuning stages, providing actionable findings (e.g., instruction SFT before reasoning SFT is crucial; staged decoupling of alignment and reasoning outperforms joint training).

## Weaknesses

### Fatal
None.

### Major

- **Missing end-to-end controlled ablation isolating the proposed methods' contribution to final reasoning performance.** The paper validates the influence-based data mixing via perplexity on probing sets (Figure 4) and the mid-training compression via MMLU (Figure 6). But it never runs a controlled experiment that compares the *full pipeline* (Datamix + mid-training compression) against a simpler alternative (e.g., uniform data mixing without mid-training compression) on *final reasoning benchmarks* such as MATH, GSM8K, HumanEval, or LiveCodeBench, while keeping all other factors (architecture, token budget, post-training) identical. Table 2 validates that pre-training+mid-training *as a whole* produces a stronger base, but it does not isolate which component drives the gains. Without this, the central claim — that the specific data optimization procedures (rather than careful dataset selection, the particular set of training corpora, or the post-training recipe) are responsible for the strong results — rests on proxy metrics rather than direct reasoning-benchmark evidence. This is a structural gap, though partially mitigated by the presence of component-level evidence.

### Minor

- **Qwen3-0.6B comparison could be clearer.** The headline claim that MobileLLM-R1-950M matches or surpasses Qwen3-0.6B is supported by numbers reported across figures and text, but the presentation is scattered. Figure 9 is labeled as showing "post-trained models" yet includes entries labeled "Qwen3-0.6B-base," creating ambiguity about which model variant is being compared. A single clean numerical table covering all benchmarks with explicit indication of model state (base vs. post-trained) and post-training protocol would substantially improve verifiability. (Note: Tables 8–9 referenced in the main text were stripped by the parser; if they provide this clean comparison in the appendix, this weakness is reduced.)

- **LOO analysis conducted at substantially smaller scale (~500K steps) than final training (4.2T tokens).** The paper uses leave-one-out proxy runs to identify informative datasets, which is a reasonable screening strategy, but does not discuss how well these short-horizon dynamics reflect full-training behavior. The gap between proxy scale and production scale is worth acknowledging.

- **Mid-training compression evaluated only on MMLU.** Figure 6 demonstrates that subsampled mid-training data outperforms the original on MMLU, but MMLU measures factual knowledge, not reasoning per se. Evaluating on reasoning benchmarks (MATH, GSM8K, HumanEval) would more directly support the claim that the compression benefits reasoning-specific capabilities.

- **No variance or significance estimates reported.** For small models where performance can be sensitive to initialization and hyperparameters, stating the number of runs or providing error bars would strengthen confidence. (This is noted as a minor concern since single-run evaluation is standard practice in large-scale LM training papers.)

### Trivial
None.

## Nice-to-Haves

- **Run a controlled end-to-end ablation:** Train the full pipeline with uniform pre-training data mixing and no mid-training compression, then compare final reasoning benchmark performance against the full recipe. This would directly quantify the benefit attributable to the proposed methods.
- **Add reasoning benchmarks to mid-training evaluation** (MATH, GSM8K, HumanEval) alongside MMLU in Figure 6.
- **Provide a single consolidated comparison table** for Qwen3-0.6B across all evaluated benchmarks with clear model-state annotations.
- **Specify the exact Ask-LLM model used** for capability-probing dataset construction (if not already in the appendix).

## Removed Points

These points were flagged by reviewers but are removed from the main weaknesses for the following reasons:

- **"Paper doesn't provide a clean comparison table for Qwen3"** — The paper reports key numbers in text (Section 4.1) and figures, and references Tables 8–9 in the appendix for comprehensive comparisons. The parser strips the appendix; these tables likely exist in the original submission.
- **"Qwen3 comparison cannot be verified"** — The numbers are reported in the paper (HumanEval 46.3 vs 30.5, MATH 74.6 vs 73.0, LiveCodeBench gains). The claim is verifiable from what is on the page.
- **"Missing hyperparameters / training details"** — Appendix A likely contains these details; the parser strips the appendix.
- **"Missing Ask-LLM model specification"** — Likely detailed in the appendix; the main text references the Ask-LLM paradigm (Sachdeva et al., 2024) which defines the approach.
- **"Fairness of baseline comparisons"** — Table 2 gives baselines the same SFT data; the comparison favors baselines (MobileLLM-R1* uses only Tulu-SFT while baselines use their instruct checkpoints), so any asymmetry favors the baselines, not the proposed method.

## Novel Insights

The most striking finding beyond the paper's own contributions is the convergence behavior documented in the mid-training compression: influence scores for most samples collapse to near-zero after two stages (Figure 5), and this "compression" yields *better* downstream performance than training on the full uncorpus, with the full data even showing a performance dip around 30K steps (Figure 6). This suggests that mid-training data for small models follows a pattern of diminishing returns where continued training on uninformative samples actively harms performance — an observation that could inform data scheduling strategies more broadly. Additionally, the LOO finding that StarCoder benefits math more than OpenWebMath benefits code (Figure 3) is a non-obvious empirical result that challenges the common intuition about domain transfer between code and mathematics.

## Suggestions

1. Add a controlled end-to-end ablation comparing the full pipeline (Datamix + mid-training compression) against a simpler baseline (uniform mixing, no compression) on the final reasoning benchmarks used in the paper. This is the single most impactful experiment to validate the methodological claims.
2. Consolidate the Qwen3-0.6B comparison into one clean table, explicitly noting which model variant (base vs. post-trained, SFT vs. RL vs. base) is being compared on each benchmark.
3. Report how many random seeds or training runs were used for the main results, or state that single-run evaluation is used and discuss sensitivity.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>