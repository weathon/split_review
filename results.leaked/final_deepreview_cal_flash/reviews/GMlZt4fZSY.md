Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

## Summary

This paper investigates how to build strong sub-billion-parameter reasoning models through principled data curation rather than massive data scaling. The authors propose two main techniques: (i) a cross-capability influence-based pre-training data mixing method (Datamix) that optimizes token allocation across code, math, and knowledge domains using influence scores, and (ii) an iterative data-model co-evolution strategy for mid-training that progressively filters and re-weights data based on sample influence. The resulting MobileLLM-R1 models (140M–950M) are trained on 4.2T tokens (11.7% of Qwen3's 36T) and match or surpass Qwen3-0.6B on reasoning benchmarks while outperforming comparably sized fully open-source models (OLMo, SmolLM) by large margins. All models, code, and data recipes are open-sourced.

## Strengths

- **Strong empirical results with substantially fewer tokens.** MobileLLM-R1-950M achieves 74.6% MATH (vs Qwen3-0.6B's 73.0%), 15.5 AIME'24 (vs 11.3), and 46.3% HumanEval (vs 30.5) using only 4.2T tokens—11.7% of Qwen3's 36T. These results place the model on the Pareto frontier of accuracy vs. training FLOPs (Figure 1) and directly substantiate the claim that strong reasoning in small models does not require massive data.

- **Principled benchmark-free data mixing via cross-capability influence.** The extension of influence-based mixture optimization to simultaneously target code, math, and knowledge capabilities (Section 2.2) is methodologically novel. The resulting Datamix consistently lowers perplexity on all three capability axes compared to uniform sampling (Figure 4), without ever accessing the final evaluation benchmarks—demonstrating a training-agnostic, benchmark-free approach to data curation.

- **Self-converging mid-training data compression.** The iterative data-model co-evolution (Section 3) provides a clean demonstration of convergence: influence scores concentrate near zero as informative content in the data is exhausted (Figure 5), and the subsampled dataset substantially outperforms the original mid-training set on MMLU (Figure 6). This is a well-motivated and empirically grounded technique.

- **Comprehensive open-source release.** The paper provides complete training recipes, all data sources and mixing ratios, trained model weights, and code (Abstract, Reproducibility Statement). This enables full reproducibility and serves as a valuable resource for the sub-billion-parameter reasoning community.

- **Systematic disentanglement of data source contributions.** The leave-one-out ablations (Section 2.1.2, Figure 3) yield non-trivial insights: FineWeb-Edu acts as a cross-domain "glue," StarCoder benefits math more than OpenWebMath benefits code, and Wikipedia contributes little to non-knowledge capabilities. These findings offer actionable guidance for data curation beyond this work.

## Weaknesses

### Major

- **End-to-end ablation of the influence-based contributions is incomplete.** The paper does not provide a full-pipeline controlled experiment that isolates the proposed influence-based methods from start to finish. Specifically:
  - For pre-training, Datamix is evaluated only via perplexity on benchmarks (Figure 4), not final downstream accuracy after the complete training pipeline. Perplexity improvement does not guarantee accuracy gains, especially for reasoning tasks.
  - For mid-training, the compression effect is shown only on MMLU (Figure 6), not on the reasoning benchmarks (MATH, HumanEval, LiveCodeBench) that headline the paper's claims.
  - No experiment takes the same 950M architecture through the full pipeline (pre-training + mid-training + post-training) comparing influence-based mixing vs. uniform or heuristic mixing on final reasoning accuracy. Since the final model comparisons (Figures 8-9) confound data curation with architecture, tokenizer, and training hyperparameters, the reader cannot isolate how much the proposed techniques contribute to the reported gains versus other pipeline choices.

- **The "2T unique tokens are sufficient" claim is asserted but not directly tested.** The abstract states "only ~2T tokens of high-quality data are sufficient," yet the paper trains on 4.2T tokens (approximately 2T unique tokens repeated). There is no experiment training on exactly 2T unique tokens without repetition to verify sufficiency. A stronger claim would require directly testing the lower bound, or at minimum acknowledging this as an extrapolation.

### Minor

- **Table 2's "identical reasoning SFT" comparison has a baseline asymmetry.** Baseline models use fully instruction-tuned checkpoints (e.g., SmolLM2-1.7B-Instruct, OLMo-2-0425-1B-SFT), while MobileLLM-R1 uses an intermediate Tulu3-SFT checkpoint (denoted *). These baselines have undergone different instruction-tuning regimens, which could either help or hinder further reasoning SFT. A cleaner control would start from publicly available base models for all families if available.

- **Ask-LLM model not specified.** The curation of capability-probing datasets (Section 2.1.1) uses Ask-LLM scoring but never states which model was used (GPT-4? LLaMA? A smaller model?). This omission directly affects reproducibility and introduces a hidden dependency.

- **Mid-training compression effect on reasoning benchmarks not reported.** While Figure 6 shows MMLU improvement from the compression procedure, the effect on MATH, HumanEval, and LiveCodeBench—the paper's primary reasoning metrics—is not shown. This is a noticeable gap given the mid-training corpus includes extra math and code data.

- **Leave-one-out analysis model size not reported.** Section 2.1.2 trains models for 500k steps under leave-one-out settings but does not state the model size. If the model is much smaller than the 950M target, conclusions about which datasets matter most may not transfer.

- **No analysis of influence-computation cost or robustness.** The paper does not discuss the GPU-hours required to train the three domain-specialized models for influence computation, nor whether cheaper heuristics might achieve similar results. Additionally, there is no sensitivity analysis of how the choice/quality of the capability-probing datasets affects the resulting mixture.

### Trivial

- The FLOPs estimate in Figure 1 uses the ×6 constant common in the field but treats all forward/backward costs as equal. A brief caveat would be appropriate.

## Nice-to-Haves

- A full-pipeline ablation (from scratch to final accuracy at 950M scale) comparing (a) uniform sampling, (b) domain-proportional sampling, and (c) the proposed Datamix would substantially strengthen the paper's core causal claim.
- Reporting mid-training compression results on MATH, GSM8K, and HumanEval (not just MMLU) would fill a clear evaluation gap.
- Table 2 would be cleaner if all models started from non-instruction-tuned base checkpoints.
- A brief discussion of potential overfitting risks in the mid-training compression (influence-based filtering could overfit to the small probing datasets) and evidence on held-out tasks not used for probing would be beneficial.

## Removed Points

These points from the reviewers were evaluated and removed for the reasons below:

- **Qwen3 token count "taken at face value":** It is standard practice in the field to cite reported training tokens from baselines. The paper cites Qwen3 (Yang et al., 2025); the 36T figure is their reported number. This is a valid comparison, not a weakness. [Removed (Hard Rule: factually wrong concern about a cited baseline)]
- **"The comparison numbers [in figures] are poorly rendered":** This is a parser artifact from PDF extraction. The original paper's figures are clean and the data is additionally provided in appendix tables. [Removed (Hard Rule: formatting/parser artifact)]
- **"No variance or number of runs reported":** Single-run evaluation is standard practice in large-scale LM pretraining at this scale. [Removed (Soft Rule: requesting practices not standard in the field)]
- **Claim about domain models being trained on full vs. representative sets is unclear:** The paper explicitly states domain models are trained "on the full training sets of domains C, M, K." The critic missed this passage. [Removed (Hard Rule: factually wrong / strawman)]
- **Section-by-section notes about missing appendix content, undisclosed hyperparameters, and formatting:** The appendix is stripped by the PDF parser; these details exist in the original submission. Hyperparameters and training details are described in Appendix A (which was stripped). [Removed (Hard Rule: parser artifact / standard practices)]
- **Various minor presentation/style nitpicks:** These are parser artifacts, not author errors. [Removed (Hard Rules: formatting, trivial reproducibility nits)]

## Novel Insights

Beyond the paper's own contributions, the reviewer integration surfaces a key tension: the paper's strongest asset (delivering SOTA-performing models with full open-source release) is also where its causal evidence is weakest. The influence-based mixing and compression procedures are well-motivated and individually supported (Figures 4 and 6), but the *incremental benefit* of these specific techniques over simpler alternatives in the *full pipeline* is not quantified. This is a recurring pattern in "recipe" papers that combine multiple techniques—the community gets a strong system and valuable insights (e.g., FineWeb-Edu's cross-domain role, the convergence phenomenon in influence compression), but the evidence for each claimed innovation remains at the proxy-metric level. The paper would be strengthened by acknowledging this gap explicitly and framing the work as a demonstrated recipe with hypothesized mechanisms, rather than a validated causal framework.

## Suggestions

- Add a controlled 950M-scale ablation comparing Datamix vs. uniform/heuristic mixing through the full pipeline to final accuracy on reasoning benchmarks. Even a single well-designed experiment would substantially clarify the contribution of the data mixing method.
- Report the Ask-LLM model used for probing dataset curation, and include the model size for the leave-one-out analyses.
- Directly test (or caveat) the "2T tokens are sufficient" claim by training a model on exactly 2T unique tokens (no repetition) or by acknowledging this is an extrapolation from the 4.2T regime.
- Add mid-training compression results on MATH, GSM8K, and HumanEval to Figure 6 or the appendix.
- Include a brief robustness/overfitting discussion for the influence-based filtering procedure.

## Score and Decision

I calibrate the score through two rounds of retrieval against human-reviewed anchors.

**Round 1 (bracketing):** Three queries covering the topic space — (i) "sub-billion language model reasoning small model data efficiency" with high_score=3.5 returned anchors averaging 2.0–3.0 (weak papers, all Reject), (ii) "data curation influence-based data mixing pre-training mixture optimization" with low_score=3.5 and high_score=7.5 returned anchors at 4.2–7.2 (Gradient-based Optimization at 4.20, Aioli at 6.25, RegMix at 7.20), and (iii) "small language model reasoning training token efficiency open source" with low_score=7.5 returned anchors at 8.0–8.67 (OLMoE, WizardMath-level papers). This places the paper solidly in the 5–7.5 range.

**Round 1 bracket:** [5.5, 7.5]

**Round 2 (narrowing):** Two queries inside the bracket — "small language model reasoning open source training recipe" (low=5.5, high=7.5) returned "Training Mice to Compete with Elephants" (6.00) and "Smaller, Weaker, Yet Better" (7.00); "data curation influence scores language model pre-training mixture" (low=5.5, high=7.5) returned RegMix (7.20), Aioli (6.25), and a data curation paper at 5.75.

**Comparative assessment:** The paper is stronger than "Training Mice to Compete with Elephants" (6.00) — more novelty, stronger final results, open-source release. It is weaker than "Smaller, Weaker, Yet Better" (7.00) on experimental isolation but has broader scope (pre-training + mid-training + post-training) and releases full assets. It is comparable to Aioli (6.25) in overall quality but has more practical impact. RegMix (7.20) has cleaner ablations but less methodological breadth. The missing end-to-end ablations and the baseline asymmetry in Table 2 prevent the paper from reaching the 7+ level, while the novel methodology, strong empirical results, and comprehensive release clearly lift it above the 5.5–6.0 range.

**Final score: 6.5 / Decision: Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>