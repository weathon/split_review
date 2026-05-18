Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes Learning to Low-Rank Compress (LLRC), a gradient-based method that learns per-layer masks over singular values using Gumbel-Sigmoid relaxation, enabling differentiable rank selection for low-rank compression of LLMs without post-compression fine-tuning. The method trains only lightweight mask parameters on a small calibration set (3K documents) using a multi-objective loss combining compression, distillation, and total variation regularization. Experiments on Llama-2-7B/13B, Llama-3-8B, and Gemma-7B show improvements over fixed-rate baselines, STRS, and ARS on several downstream tasks, and competitive results against fine-tuned structural pruning (LLM-Pruner) on Llama-2-7B.

## Strengths

- **Differentiable any‑\(k\) singular value selection is a novel and principled approach to a real problem.** The Gumbel-Sigmoid mask over singular values allows the method to learn which subset of singular values to retain (not just top‑\(k\)), addressing the limitation of discrete heuristic rank search. The any‑\(k\) vs. top‑\(k\) ablation (Figure 3) provides empirical evidence that flexibility matters, especially at higher compression rates (e.g., +4% on NQ-Open at 80% parameter ratio).

- **Fine-tuning-free LLRC is competitive with or surpasses fine-tuned structural pruning on Llama-2-7B.** Table 2 shows that LLRC (no fine-tuning) outperforms LLM-Pruner *with* fine-tuning on 4 out of 5 datasets at 80% parameter ratio. This is a noteworthy result because structural pruning methods typically require substantial post-compression training to recover performance.

- **Efficient training with lightweight learnable parameters.** Only one learnable vector per layer (\(W_{\text{learnable}} \in \mathbb{R}^{1\times\text{rank}}\)) is trained while the rest of the model is frozen. The calibration set of just 3,000 documents suffices, keeping the training cost low compared to ARS (which requires 576 GPU hours).

- **Evaluation across four model families.** Results span Llama-2-7B, Llama-3-8B, Gemma-7B, and Llama-2-13B, demonstrating the method is not tailored to a single architecture.

## Weaknesses

### Major

- **Comparison to STRS is confounded by the distillation loss — the source of gains is not isolated.** STRS selects ranks by perplexity search after ASVD and does not use distillation. LLRC uses both the Gumbel-Sigmoid mask *and* a distillation loss (Eq. 7) that minimizes activation divergence from the original model. Since distillation is a well-known technique that independently improves compressed model performance, the reported gains over STRS (e.g., +12% on MMLU for Llama-2-13B at 80% param ratio) cannot be cleanly attributed to the rank selection mechanism itself. An ablation that applies LLRC's distillation loss to the ranks selected by STRS (or to a fixed-rank baseline) is needed to separate the contribution of the mask learning from the distillation objective. Without this, the paper's central claim about the superiority of the gradient-based rank selection is partially undersupported.

### Minor

- **No perplexity evaluation despite it being the standard metric for language model compression.** Compressed LLMs are conventionally evaluated on perplexity (e.g., WikiText-2) to measure language modeling degradation in a task-agnostic way. The paper evaluates only on downstream tasks (MMLU, BoolQ, PIQA, OpenbookQA, NQ-Open), which are noisier and less sensitive to subtle compression damage. Reporting perplexity would strengthen the evidence that LLRC preserves language modeling quality, not just task-specific accuracy.

- **No variance or reproducibility statistics reported.** No standard deviations, confidence intervals, or multi-seed runs are reported for any result. Given that the calibration set is only 3,000 documents and mask training involves stochastic optimization (Gumbel-Sigmoid with temperature), the variance could be nontrivial. The headline numbers (Tables 1–2, Figure 2) are presented as point estimates without any measure of reliability, which limits the evidentiary weight of the comparisons.

- **Hyperparameter sensitivity is unexplored.** Several key hyperparameters are set without ablation: the mask initialization range ([3, 6]), Gumbel temperature (0.1), the oscillating \(\alpha\) schedule bounds, and the early-stopping threshold (750 steps after target ratio). While many of these follow prior work, their sensitivity is uncharacterized. This makes it harder for practitioners to reproduce the method on new models.

- **The claim about outperforming fine-tuned LLM-Pruner is asymmetrically presented.** The paper highlights that LLRC outperforms LLM-Pruner (with fine-tuning) on Llama-2-7B at 80%, but relegates to a single sentence the fact that on Llama-3-8B at higher compression rates LLM-Pruner (with fine-tuning) performs better. While the paper acknowledges this, the overall narrative leans heavily on the favorable case.

### Trivial

- **The oscillating \(\alpha\) schedule and the fixed \(\beta\) schedule are described but not analyzed** for sensitivity or convergence impact. The early-stopping rule of 750 steps after target ratio is stated without motivation.

## Nice-to-Haves

- A controlled comparison: STRS + distillation loss applied to its selected ranks vs. LLRC, to isolate the rank selection contribution.
- Perplexity evaluation on WikiText-2 (held-out) for all compression rates and models.
- Multi-seed results (mean ± std) for main tables.
- Visualization of learned mask profiles across layers (e.g., attention vs. FFN at different depths) to illustrate how the method distributes rank budgets.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Unfair comparison to ARS — stripping fine-tuning breaks the intended pipeline."** The paper explicitly states (line 201) that it compares fine-tuning-free rank selection approaches and uses only ARS's rank selection without fine-tuning. The paper's scope is fine-tuning-free rank selection, so this comparison is appropriate and transparent. The critic's concern is a scope mismatch, not a methodological flaw.

2. **"Inaccurate description of STRS in the abstract"** — the paper describes STRS as using a discrete set of 10 rates and performing binary search, which is consistent with the original method. The critic's description does not contradict the paper's. No factual error exists.

3. **"Oscillating α lacks reference (likely missing citation)"** — the paper explicitly cites Fu et al. (2019) for this choice (line 185). The claim is factually wrong.

4. **"Distillation vs. pretraining inconsistency in usage"** — both yield similar results yet distillation is used"** — the paper explains (Section 7.3) that distillation leads to better generalization on the majority of datasets, especially at 20% compression where it outperforms pretraining on all datasets. This is a valid justification.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine methodological concern (the distillation confound in the STRS comparison) but do not produce a new insight about the paper or the problem that the paper itself does not articulate.

## Suggestions

1. **Add a controlled ablation** that applies LLRC's distillation loss to STRS-selected ranks (or to fixed rank assignments) to isolate whether the gains come from the mask learning or from the distillation objective. This would substantially strengthen the central claim.

2. **Report perplexity on WikiText-2** for all compression rates and models. This is the standard evaluation for LLM compression and would provide a task-agnostic measure of quality degradation.

3. **Report multi-seed mean ± std** for at least the main results (Tables 1, 2). The community needs to know the variance of the method.

4. **A sensitivity study** of the Gumbel temperature and mask initialization range would help practitioners reproduce the method and clarify how robust the approach is.

5. **Visualize learned masks** for representative layers to illustrate how LLRC distributes rank budgets across different layer types and depths — this would validate the claim that different layers receive different compression rates.

## Score and Decision

**Calibration anchors** (all from the same topic area — LLM compression via low-rank/SVD/pruning):

| Anchor Path | Avg Score | Comparison to LLRC |
|---|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AutoTrunc (3KEwJGYNzH)` | 4.00 | Weaker: tested on fewer model families (only Llama-2), fewer downstream tasks, but does report perplexity. LLRC is stronger in breadth and novelty. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TensorGPT (FVgizbs3o2)` | 3.75 | Weaker: narrower scope, fewer experiments. LLRC is clearly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Low-Rank Correction for Quantized LLMs (FA3iYp1y6z)` | 5.00 | Comparable overall: both have clear contributions but notable experimental gaps. LLRC has stronger novelty (differentiable rank selection). |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ASVD (HyPofygOCT)` | 6.25 | Stronger: seminal paper with cleaner evaluation (perplexity, more baselines). LLRC has a narrower experimental validation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OATS (DLDuVbxORA)` | 6.25 | Stronger: more thorough experiments, speed measurements, broader model scope. LLRC is comparable in novelty but weaker in experimental rigor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DSF (DwiwOcK1B7)` | 6.33 | Stronger: more rigorous experimental validation, clearer methodological contribution. LLRC has a cleaner idea but weaker empirical support. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Rank-adaptive spectral pruning (6aRMQVlPVE)` | 4.33 | Weaker: focuses on CNNs, less relevant. LLRC addresses a more timely problem (LLMs). |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Structured Mixture-of-Experts LLMs Compression (ho7ZUS1z8A)` | 5.00 | Comparable: both have interesting ideas but incomplete experimental validation. LLRC's contribution is more clearly differentiated from prior work. |

The paper introduces a novel and well-motivated approach to rank selection for low-rank LLM compression. The Gumbel-Sigmoid masking with any‑\(k\) selection and the multi-objective training signal are genuine technical contributions. However, the experimental evaluation has substantive gaps: the comparison to STRS is confounded by the distillation loss (making it unclear whether the gains come from the rank selection or the distillation), perplexity is not reported, and no variance statistics are provided. These issues prevent the paper from being a strong accept at the current stage. Compared to the calibration anchors, the paper sits slightly below the caliber of ASVD/OATS/DSF (~6.25) but above weaker papers like AutoTrunc (4.00). The core idea has promise, but the evidence presented is insufficient to fully validate the claimed advantages.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>