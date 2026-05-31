## Summary

ATF (Autoformalizer with Tool Feedback) integrates Lean 4 compiler feedback and a multi-LLMs-as-judge consistency checker into the autoformalization training pipeline via three stages: cold-start on synthetic tool-calling trajectories, expert iteration, and DPO for efficiency. ATF-32B substantially outperforms all existing 32B formalizers across FormalMath-Lite, ProverBench, and CombiBench on both syntactic validity and semantic consistency, and an open-source 750K formal statement dataset (Numina-ATF) is released to support downstream ATP research.

## Strengths

- **Strong and consistent empirical gains:** ATF-32B surpasses the best baseline (Goedel-V2-Formalizer-32B) by +9.1%, +10.08%, and +29.13% CC Pass@1 on the three benchmarks. The improvements are systematic and hold across all metrics and sample sizes.
- **Human evaluation as gold standard:** 3-annotator majority-vote human evaluation on 100 instances per benchmark confirms the automated metrics are reliable and that ATF substantially outperforms all baselines (e.g., 49% vs. 22% on CombiBench CC).
- **Well-designed ablation study:** Table 4 cleanly isolates contributions of each tool and each training stage, showing that both the consistency check and expert iteration each provide substantial additive gains.
- **Practical multi-LLMs-as-judge benchmarking:** The authors construct a purpose-built 800-sample benchmark with character-similar positive/negative pairs, systematically evaluate candidate judges, and select the ensemble based on measured FPR reduction (from ~9% to ~5.8%), which is careful empirical methodology.
- **Grouped Lean 4 execution for efficiency:** The namespace-batching approach for amortizing compilation cost is a non-trivial engineering contribution that makes large-scale training practical.
- **Inference scaling analysis:** Both revision-count scaling and Pass@K scaling are demonstrated, and performance continues to improve beyond the training limit of 8 revisions, indicating learned generalizable revision strategies.

## Weaknesses

### Fatal
None.

### Major

1. **Comparison fairness at inference time:** ATF's Pass@1 is measured with up to 4 sequential revision attempts (each calling Lean 4 and two LLM judges), while baseline Pass@1 is a single forward pass. The authors justify this by arguing output lengths are "roughly equivalent," but this is a compute-wall-equivalence argument rather than a controlled comparison. Baselines with equivalent inference compute (e.g., repeated sampling with majority vote) are not reported. Given that ATF's Pass@1 ≈ baselines' Pass@8 in some settings, the effective "inference compute" advantage may partly explain the gains.

2. **High false-negative rate (FNR) of the consistency check:** The ensemble judge achieves FNR = 0.4033, meaning ~40% of semantically inconsistent statements are incorrectly labeled as consistent. This noisy label is used both as a training signal (expert iteration accepts these) and as the primary evaluation metric. The Pearson correlation of 0.746 with human judgments provides partial reassurance, but the magnitude of FNR means a non-trivial fraction of ATF's "consistent" outputs may not actually be consistent. This creates a ceiling question for the true quality of the Numina-ATF dataset.

3. **Circular training and evaluation signal:** The consistency check (QWQ-32B + Qwen3-32B ensemble) is used to (a) generate training rewards during expert iteration and (b) evaluate all models in Table 3 (including baselines). If the judge systematically favors the style of outputs produced by ATF (which was trained against this exact judge), the evaluation metric may overstate ATF's advantage. Human evaluation alleviates this but covers only Pass@1 on 100 samples each.

### Minor

1. **Cold-start data requires Claude-4-Sonnet (not publicly available):** The cold-start phase depends on proprietary model trajectories, which limits full reproducibility for external researchers.

2. **DPO contribution is marginal:** The DPO phase provides only +0.36%–+1.5% CC improvement across benchmarks (Table 4), suggesting the 10K DPO pairs add limited signal. The analysis of why consecutive identical errors persist after expert iteration, and whether DPO truly resolves them, is shallow.

3. **Declining consistency success rate at higher revisions:** Figure 5(c) shows CC success rate dropping from 69.5% to 8.8% across 8 attempts, but the paper only notes this trend without investigating its cause—whether it reflects diminishing model diversity, judge saturation, or problem hardness.

### Trivial
None worth noting.

## Nice-to-Haves

- Report baselines with repeated sampling (e.g., best-of-K without revision) to establish a true compute-controlled baseline.
- Analyze the composition of the 40% FNR cases to characterize what types of subtle inconsistencies the ensemble judge systematically misses.
- Include a breakdown of ATF failure cases on CombiBench (which still fails 35% CC at Pass@1) to characterize remaining open challenges.

## Novel Insights

The most genuinely novel insight is the demonstration that multi-LLMs-as-judge ensemble with a purpose-built similarity-constrained benchmark effectively reduces FPR in detecting subtle semantic misalignments (from ~9% individually to ~5.8%), making LLM-based consistency validation practically viable as a training signal. Combining this with a three-stage training pipeline (cold-start tool familiarity → expert iteration for capability → DPO for efficiency) and compiler-batching for scale is an original synthesis that advances the state of autoformalization.

## Suggestions

- Provide compute-controlled baselines (same inference FLOPs as ATF but used as repeated single-pass sampling) to disentangle model quality from inference-time search.
- Quantify what fraction of the 750K Numina-ATF statements are affected by the 40% FNR, and offer a re-filtered, higher-precision subset for users who prioritize quality over quantity.
- Investigate whether DPO with online RL (e.g., GRPO) would be stronger than offline DPO for reducing redundant revisions, or provide empirical evidence that DPO is preferred for reasons beyond the practical argument given.

## Score and Decision

The paper presents a well-executed, empirically strong system contribution to an important problem (autoformalization for ATP). The improvements are large and validated by human evaluation. The main concerns—inference compute fairness, FNR of the consistency tool, and evaluation circularity—are real but do not invalidate the core findings; human evaluation provides a partial but meaningful independent check. The dataset contribution and scaling analysis add further value.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>