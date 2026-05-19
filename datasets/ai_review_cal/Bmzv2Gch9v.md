- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8
Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes SmartPretrain, a self-supervised learning framework for motion prediction that is designed to be both model-agnostic (works across GNN, transformer, and raster-based backbones) and dataset-agnostic (enables pre-training on multiple heterogeneous driving datasets). The method uses temporal sampling to create non-overlapping sub-scenarios from the same scene, then applies two trajectory-focused pretext tasks — trajectory contrastive learning (TCL) and trajectory reconstruction learning (TRL) — that avoid architectural constraints by operating only on trajectory embeddings. Experiments on Argoverse and Argoverse 2 with four backbone models (HiVT, HPNet, Forecast-MAE, QCNet) show consistent improvements, with the largest being a 10.6% Miss Rate reduction for Forecast-MAE.

## Strengths

1. **Model-agnostic design validated across diverse architectures.** Table 1 shows SmartPretrain improves all four backbones — HiVT (GNN), HPNet (point-cloud-based), Forecast-MAE (transformer-MAE), QCNet (transformer with query) — with positive gains on both validation and test sets across all metrics. This directly supports the core claim that trajectory-focused pretext tasks (Section 3.2.2) avoid architectural constraints.

2. **Multi-dataset pre-training yields clear and consistent scaling benefits.** Table 4 systematically compares single-dataset, transfer, and data-scaled pre-training. For both HiVT (Argoverse) and QCNet (Argoverse 2), pre-training on all three datasets (Argoverse + Argoverse 2 + WOMD) outperforms any single-dataset pre-training, with improvements growing as data diversity increases (e.g., HiVT minFDE: 0.940 single → 0.929 All, a -4.1% total gain vs -3.0% with single-dataset).

3. **Significant gains demonstrated on a strong baseline.** The comparison with Forecast-MAE's own pre-training (Table 2) shows SmartPretrain's improvement on the same backbone is more than double that of Forecast-MAE's method (4.5% vs 1.9% minFDE improvement), providing meaningful evidence of advantage over an existing SSL approach.

4. **Ablation validates the synergy of contrastive and reconstructive tasks.** Table 3 shows each pretext task alone improves minFDE (-1.1% for TCL, -1.8% for TRL), but combining both yields the largest gain (-3.0%), confirming the paper's design rationale for integrating generative and discriminative SSL.

5. **Methodologically careful design.** The temporal sampling strategy that ensures non-overlapping sub-scenarios avoids information leakage between the two branches (Section 3.2.1). The reconstruction target ablation (Table 5) systematically tests four variants and shows predictive targets (complementary/other sub-scenario trajectory) substantially outperform reconstructing historical information, providing evidence-informed design choices.

## Weaknesses

### Fatal
None.

### Major

1. **No WOMD downstream evaluation.** The paper lists WOMD as one of three core datasets and claims "dataset-agnostic" generalization, but all downstream fine-tuning and evaluation is conducted only on Argoverse 1 and Argoverse 2. WOMD is used exclusively as a pre-training source. While the transfer pre-training experiments (Table 4) show that pre-training on WOMD benefits downstream performance on the other two datasets, the absence of fine-tuning on WOMD itself — especially as WOMD is the largest and most diverse dataset (487k scenes, 8-second horizon) — leaves the "dataset-agnostic" claim partially unsupported. The paper would be substantially stronger with even a single backbone fine-tuned and evaluated on WOMD validation.

### Minor

2. **No variance or statistical significance reporting.** All results are single numbers without standard deviations, confidence intervals, or multiple seeds. For the smallest improvements (e.g., HPNet on Argoverse test: minADE -0.4%, minFDE -0.8%), it is impossible to determine whether these gains are within run-to-run variance. The overall pattern of consistent improvement across all models and datasets mitigates this concern for the paper's main claims, but the modest HPNet test improvements in particular would benefit from error bars.

3. **Limited comparison with alternative pre-training methods.** Only Forecast-MAE is used as a pre-training baseline (Table 2). The paper explains that "only Forecast-MAE was open-sourced at the time of this paper's submission," but published numbers from other methods (e.g., PreTraM on Argoverse 1) could provide additional context for the method's relative effectiveness. The claim of "stronger performance enhancements compared to existing pre-training methods" rests on a single comparison point.

4. **No ablation or reporting of the reconstruction loss weight λ.** The combined loss (Eq. 3) introduces λ as a balancing hyperparameter, but its value is never stated nor ablated. It is unclear how sensitive performance is to this choice and what value was used in experiments.

5. **No discussion of limitations or potential negative transfer.** The paper reports only positive results. There is no discussion of settings where SmartPretrain might underperform (e.g., if pre-training and downstream data distributions are highly dissimilar), nor analysis of failure cases. The transfer pre-training results in Table 4 show smaller but still positive gains — a discussion of when one might expect negative transfer would strengthen the paper's scientific rigor.

### Trivial

6. **Temporal sampling distribution not fully specified.** Section 3.2.1 states that sub-scenario start times t and t' are "temporally sampled" without information leakage, but does not specify the sampling distribution (uniform over feasible range? constrained by minimum gap?). This affects exact reproducibility.

## Nice-to-Haves

- An ablation of the λ hyperparameter would strengthen the methodological analysis.
- A discussion of compute cost trade-offs (32 A100 GPUs for 128 epochs) relative to training from scratch for more epochs would help practitioners assess practical value.
- Reporting the pre-training learning rate and optimizer hyperparameters would aid reproducibility beyond what is currently provided.

## Removed Points

The following points from the reviews are removed with justification:

1. **"The improvement from 'single' to 'All' could be due to simply more data rather than any special property of the method."** — This is not a weakness; the method's core purpose is to enable multi-dataset pre-training. Showing that more data helps is the method working as intended, not a confound. The paper makes no claim that the method provides gains beyond what data scaling would predict.

2. **"The paper does not prove the absence of partial attempts at model-agnostic or multi-dataset SSL."** — Generic literature-coverage criticism without a concrete missing reference or specific evidence. The paper's claim is about existing works being model-specific; this framing is supported by the cited literature.

3. **"Reproducibility details missing (learning rates, optimizer settings)"** — The paper specifies AdamW and notes that fine-tuning uses "the models' original training schedules" for each backbone. While more detail would help, this falls under the rule to remove nitpicks about hyperparameter disclosure. Minor formatting details like "trajectory" vs "trajectory" in the text are parser artifacts.

4. **Missing appendix content or proofs** — Removed per instructions; the parser strips appendix content from all papers.

## Novel Insights

None beyond the paper's own contributions. The reviews do not synthesize observations that the paper itself does not already articulate.

## Suggestions

1. **Highest priority: Add WOMD downstream results for at least one backbone** (e.g., QCNet or Forecast-MAE, which already have strong WOMD baselines in prior work). This directly validates the dataset-agnostic claim and closes the largest evidence gap.

2. **Report error bars** for at least the main results (Table 1), even if only for one representative backbone-dataset pair with 3 seeds, to establish that improvements are statistically reliable.

3. **Include a limitations paragraph** discussing potential negative transfer scenarios and when the method might not help.

4. **State the λ value used** and ideally provide a brief sensitivity analysis.

5. **Cite published results** from PreTraM or other SSL methods on the same benchmarks as additional context, even if exact reproduction is not possible.
