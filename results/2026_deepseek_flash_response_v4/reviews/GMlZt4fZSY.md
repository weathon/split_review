## Summary

This paper introduces a data-centric training pipeline for sub-billion-parameter reasoning language models, using only ~2T unique tokens (4.2T total with resampling) to match or exceed models trained on 36T tokens. The methodology includes: (1) leave-one-out analysis of data-source contributions via NLL on capability-probing datasets, (2) cross-capability self-influence scoring for data mixture optimization, and (3) iterative data-model co-evolution for mid-training data compression. The paper releases models, code, and datasets.

## Strengths

1. **Principled leave-one-out analysis isolates data-source contributions (Figure 3)**: The LOO ablation measures NLL degradation when individual datasets are removed, providing quantitative evidence that FineWeb-Edu provides the broadest cross-domain benefit and that StarCoder benefits math more than math-focused data benefits code — a non-obvious finding backed by data.

2. **Influence-based data mixing improves perplexity on held-out benchmarks (Figure 4)**: The Datamix strategy consistently achieves lower perplexity than uniform sampling on Code, Math, and Knowledge benchmarks, despite these benchmarks never being accessed during mixture construction. This demonstrates benchmark-free, self-adaptive data optimization.

3. **Controlled ablation isolates pre-training quality from SFT effects (Table 2)**: When all models are fine-tuned on the identical reasoning SFT corpus, MobileLLM-R1-950M (949M params) achieves 57.8% MATH vs 53.0% for OLMo-2-1.48B and 41.4% for SmolLM2-1.7B — directly attributing gains to pre-training/mid-training quality rather than better SFT data. This is the strongest evidence in the paper.

4. **Post-training ablation reveals non-obvious trade-offs (Table 1)**: Systematic comparison of staged vs. joint training, and individual vs. combined domain data, showing that scientific reasoning data improves MMLU more than math/code data, and that decoupling alignment from reasoning is beneficial.

5. **Token efficiency is demonstrated through direct comparison**: MobileLLM-R1-950M (4.2T tokens) matches or surpasses Qwen3-0.6B (36T tokens) on multiple reasoning benchmarks, placing it on the Pareto frontier of accuracy vs. training FLOPs (Figure 1).

## Weaknesses

### Fatal
None.

### Major

1. **Abstract AIME claim (15.5) contradicts the AIME24 table (0.9/1.1)**. The abstract states "MobileLLM-R1-950M achieves an AIME score of 15.5, compared to just 0.6 for OLMo-2-1.48B and 0.3 for SmolLM-2-1.7B." In the AIME24 table (Figure 9), the value 15.5 belongs to **SmolLM2-135M-base**, while MobileLLM-R1-950M-base shows **0.9/1.1**. Furthermore, OLMo-2-1.48B and SmolLM-2-1.7B do not appear in the AIME24 table at all. The paper's headline quantitative claim — featured prominently in the abstract — is inconsistent with the paper's own tables.

2. **950M base model severely underperforms smaller variants without explanation**. In Figure 8 (base models), MobileLLM-R1-950M-base achieves GSM8k: 5.0, HumanEval: 0.0, MMLU: 26.5, while the 350M variant achieves 39.4, 32.9, and 50.0 respectively. The 950M model is outperformed by both smaller siblings on every benchmark, contradicting basic scaling expectations. The paper offers no discussion of this anomaly — a serious omission for a paper whose central claim involves model scaling.

3. **Claimed HumanEval score (46.3%) for MobileLLM-R1-950M is not supported by any table**. Line 384 states "MobileLLM-R1-950M attains the highest HumanEval score (46.3%) among all sub-1B models, significantly outperforming Qwen3-0.6B (30.5%)." However, the HumanEval table (Figure 8) shows MobileLLM-R1-950M-base at 0.0 and Qwen3-0.6B-base at 46.3. Figure 9 (post-trained models) does not include HumanEval. No table in the paper substantiates this claim.

### Minor

4. **Model naming inconsistency across tables**. Table 2 uses "MobileLLM-R1-140M\*" (140M params) and "MobileLLM-R1-360M\*" (359M params), while Figure 8 uses "MobileLLM-R1-150M-base" and "MobileLLM-R1-350M-base." The parameter count differences (140M vs 150M, 359M vs 350M) are unexplained — these could be different checkpoints, rounding, or naming errors.

5. **No error bars or multiple seeds**. Key comparisons (LOO analysis, mixture strategies, mid-training subsampling) are presented as single runs without variance estimates. While single-run evaluation is common in large-scale pre-training, the absence is notable for a paper whose main evidence is empirical and where some trends (Figure 6 dip around 30K steps) need disambiguation.

6. **Computational cost of the influence pipeline is not reported**. The method requires training domain-specialized models and computing Hessian approximations at 10 checkpoints. This overhead is relevant for practitioners evaluating whether the method is worth adopting.

7. **No discussion of data repetition**. The paper uses 4.2T total tokens from ~2T unique tokens (~2× repetition). Qwen3's 36T tokens may or may not use repetition. This confound is not addressed, making the token-efficiency comparison less precise.

8. **Missing direct baseline: training on the same raw data with uniform sampling**. The paper compares against OLMo/SmolLM baselines but does not include a "train on the same raw datasets with uniform sampling" baseline, which would directly isolate the value of the curation pipeline from architectural or other confounds.

### Trivial
None.

## Nice-to-Haves

- Validate that NLL reductions on the capability-probing datasets correlate with downstream benchmark gains (currently assumed rather than demonstrated).
- Report mid-training results on benchmarks beyond MMLU to show generality of the compression effect.
- Clarify the relationship between "representative datasets" used for influence computation and the full datasets.

## Removed Points

- **Criticism that NLL proxy is not validated as correlated with downstream performance**: Using NLL on capability-probing datasets is a standard approach in data curation research. This is a reasonable methodology choice, not a flaw. The paper also validates indirectly through downstream benchmarks.
- **"Staged vs joint training contradicted by joint winning on LCBv6"**: The paper's claim is about "math and general reasoning" (line 241). LCBv6 is a code benchmark. There is no contradiction.
- **Strength about "full open-source release"**: This is commendable but generic; many papers make similar commitments. Not a core methodological strength.
- **Various formatting/table layout concerns**: These are PDF parser artifacts, not author errors.
- **"Missing related works"**: Cannot verify without external sources.
- **Concerns about missing appendix content**: The parser strips appendices; these exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the abstract's AIME claim** to match the table data (or vice versa) and clarify which model variant (base vs. post-trained) and evaluation setting the scores refer to.
2. **Investigate and explain the 950M base model's anomalous underperformance** relative to the 350M variant. If it's a genuine result, discuss why (e.g., undertraining, data mixture not transferring to larger capacity). If it's an error, correct it.
3. **Provide a table or figure** that supports the claimed 46.3% HumanEval score for MobileLLM-R1-950M, with clear indication of which training stage this corresponds to.
4. Add a **uniform-sampling baseline trained on the same raw data** to directly isolate the curation pipeline's contribution.
5. Report **computational costs** for the influence scoring pipeline and clarify the **data repetition** schedule.

## Score and Decision

**Calibration Anchors (from human-review corpus):**

*Round 1 — Bracketing:*
- **Weak band** — Paramanu-Ganita (2.33), FreeLM (2.00), LogicJitter (2.50): Papers with thin methodology or limited contributions. MobileLLM-R1 is clearly stronger.
- **Middle band** — RegMix (7.20, Accept), Aioli (6.25, Accept), MiniPLM (6.40, Accept), Domain2Vec (6.25), AutoScale (5.50, Reject): Papers on data mixture optimization and small-model training, comparable in scope.
- **Strong band** — Synthetic continued pretraining (8.00), Combatting Dimensional Collapse (8.00): Clean execution, comprehensive evaluation, no data issues. MobileLLM-R1 is clearly weaker.

*Round 2 — Narrowing:*
- **RegMix (7.20, Accept)**: Cleaner execution, narrower scope. MobileLLM-R1 has broader scope and more impressive end results but the data consistency issues make it substantially weaker.
- **Aioli (6.25, Accept)**: Clean conceptual contribution with limited experiments. MobileLLM-R1 has more extensive empirical validation but messier presentation. Roughly comparable, with MobileLLM-R1 slightly weaker due to data issues.
- **AutoScale (5.50, Reject)**: Similar data presentation/validation issues, weaker experiments. MobileLLM-R1 has stronger experiments but similar data consistency concerns. Roughly comparable.

**Final Score: 5.5**

The paper's methodological contributions (LOO analysis, influence-based mixing, data-model co-evolution) are genuine and the controlled ablation in Table 2 is compelling evidence for the value of the curation pipeline. The post-training results on MATH (57.8%) and GSM8K (68.5%) at only 4.2T tokens are legitimately impressive. However, the paper has multiple data consistency issues — the abstract's headline AIME claim contradicts the main table, the 950M base model underperformance is completely unexplained, and the claimed HumanEval score lacks tabular support — that undermine the paper's credibility and prevent acceptance in the current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>