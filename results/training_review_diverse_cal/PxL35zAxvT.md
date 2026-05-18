Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper addresses the problem of limited data in Test Time Adaptation (TTA) by proposing DISTA, a method that uses a *distillation-based auxiliary task* on unlabeled source-domain data during test-time adaptation. The key insight is that when the test stream reveals limited data per batch (preventing multiple adaptation steps without overfitting), the model can additionally optimize on clean unlabeled data from the training distribution. The authors provide a *lookahead analysis* to motivate why auxiliary tasks help, then show consistent gains across episodic (+1.5%), continual (+6%), and a newly proposed federated TTA evaluation (+6%) on ImageNet-C and ImageNet-3DCC.

## Strengths

1. **Consistent and significant improvements across multiple evaluation protocols.** DISTA outperforms prior state-of-the-art (EATA, SAR, Tent) on episodic, continual, and federated evaluations. The gains are particularly notable in continual evaluation (6% on ImageNet-C, 8% on ImageNet-3DCC) and the method recovers performance on clean validation data, demonstrating that the distillation auxiliary task provides stability against forgetting.

2. **Principled motivation via lookahead analysis.** Section 2.1 introduces a diagnostic (lookahead, Eq. 3) that empirically measures how much an auxiliary step on source data reduces entropy on corrupted data. Figure 1 shows positive lookahead over all observed batches for both the simple entropy auxiliary and the proposed distillation auxiliary. This grounds the method in a quantifiable phenomenon rather than intuition alone.

3. **Robustness to practical deployment conditions.** Figure 2b shows DISTA maintains gains across batch sizes 8–64 (with a 15% improvement over EATA at batch size 8). Figure 2c shows consistent gains across ResNet-18, ResNet-50, ResNet-50-GN, and ViT (7% over SAR on ViT). This demonstrates the method is not brittle to architecture or batch size choices.

4. **Computational trade-off analysis.** Figure 2a reports a smooth trade-off: with only 50% additional computation (auxiliary update on every other batch), DISTA still outperforms EATA by 1.4% on average. Section 4.4.1 also proposes a parallel update variant (Eq. 6) that reduces latency.

5. **Orthogonality of auxiliary tasks.** Table 6 shows that adding a simple entropy-based auxiliary task improves both Tent and SHOT (e.g., 3% reduction on motion blur for both, 4% average gain for SHOT), demonstrating the auxiliary-task principle is general and not specific to the distillation formulation.

## Weaknesses

### Fatal
None.

### Major
- **Federated evaluation conflates multiple sources of gain and lacks comparison to existing federated TTA methods.** In the federated setup (Table 5), clients within the same corruption category (e.g., Noise: Gaussian, Shot, Impulse) but observing *different* corruptions communicate via averaging. The improvements attributed to federated averaging could stem from increased effective batch size, from averaging across diverse shifts, or from the simple fact that each client sees a small subset of data. The paper does not isolate these factors. Moreover, although the paper cites Jiang & Lin (2023) in the introduction as prior work on federated TTA, it does not compare against any existing federated TTA method. A controlled ablation (e.g., varying client count, communication frequency, or heterogeneity of shifts) would be needed to make the federated results a robust contribution rather than an exploratory analysis.

### Minor
- **No error bars, confidence intervals, or multi-run variability reported.** All experimental results (Tables 1–6, Figure 2) are reported as single point estimates. TTA experiments are known to be sensitive to initialization, data ordering, and random batching. Without variability estimates, it is difficult to assess whether the reported 1.5% episodic or 6% continual improvements are statistically significant. While single-run evaluation is common practice in large-scale TTA benchmarks, reporting at least 3 seeds with standard deviations would substantially strengthen the credibility of the claimed improvements.

- **The requirement for source unlabeled data ($\mathcal{D}_s$) is acknowledged but not characterized.** The paper notes that "one could store few unlabeled data examples ... before deployment" but does not quantify how much source data is needed, how it should be selected, or how representative it must be. The ablation on $\mathcal{D}_s$ size is missing entirely — the paper states only that $\mathcal{D}_s$ is a "randomly selected subset of ImageNet training set" without specifying its size. For practitioners evaluating whether this method is viable, knowing the minimum data requirement is important.

- **Computational overhead is discussed but not quantified in terms of wall-clock time, memory footprint, or throughput.** Section 4.4.1 acknowledges that DISTA has "2× the cost" of standard TTA and analyzes sensitivity to auxiliary update frequency, but no runtime numbers are reported. Without knowing whether the 1.5–6% improvement costs 2× latency or can be made nearly free with the parallel variant, a reader cannot assess the practical trade-off for real-time deployments.

- **No discussion of failure cases or limitations.** The paper lacks a dedicated limitations section. Every method has regimes where it underperforms — e.g., when the source distribution is very different from the training distribution, or when the stored $\mathcal{D}_s$ is itself corrupted. A frank discussion of limitations would improve credibility.

### Trivial
- **Data selection thresholds ($E_0$, $\epsilon$) are taken from EATA without sensitivity analysis.** Since DISTA uses a different auxiliary task (distillation rather than entropy minimization), the optimal thresholds may differ. Reporting sensitivity to these would be straightforward.

- **No random seeds reported, making exact reproducibility difficult.**

## Nice-to-Haves
- **Per-batch/domain adaptation curves** (e.g., error rate or entropy over batches for specific corruptions like Gaussian Noise, Snow) would visually demonstrate the acceleration claim and complement the lookahead analysis.
- **Ablation on source data size and selection strategy** (e.g., fixed small set vs. large random subset, diversity of samples) would directly address the practical concern about $\mathcal{D}_s$ requirements.
- **Runtime comparison table** (seconds per batch or total adaptation time) for Tent, EATA, SAR, and DISTA (both sequential and parallel variants).
- **In the federated evaluation**, an experiment where all clients observe the *same* corruption (but non-overlapping data) would separate the benefit of larger aggregated data from the benefit of averaging across different shifts.

## Removed Points
- *"The orthogonality experiment uses the entropy-auxiliary task, not distillation — this weakens the claim that distillation is key."* — The paper's claim in Section 4.4.3 is specifically about the orthogonality/generality of *auxiliary tasks broadly*. The distillation claim is already validated by the main DISTA results (Tables 1–5). This criticism evaluates the wrong experiment against the wrong claim.
- *"No comparison to TTT (Test-Time Training) methods like TTT++, MT3."* — The paper explicitly scopes out TTT methods, noting (Section 3) that they "require control over the training process, and thus are not readily applicable to any pretrained model." Evaluating the paper against a setting it deliberately and justifiably excludes is scope creep.
- *"The paper does not share code."* — Code release is standard practice for camera-ready versions but is not a requirement for the submission itself. This is a generic reproducibility nitpick; the paper compares against baselines using official implementations with recommended hyperparameters, which is sufficient.

## Novel Insights

The review process surfaces that while DISTA's core idea — using distillation on source unlabeled data to accelerate TTA — is well-motivated via the lookahead diagnostic and validated across many settings, the paper's main methodological contribution (the auxiliary task) is orthogonal to several design choices that remain unablated. The most interesting tension is between the strength of the lookahead motivation (which elegantly isolates *why* auxiliary tasks work) and the uncertainty introduced by using an uncharacterized source data store ($\mathcal{D}_s$) whose size, selection strategy, and distributional alignment with the training data are all unspecified. The federated evaluation, while novel, needs tighter experimental controls before the federated gains can be attributed to the specific claims made rather than to confounding factors like increased effective batch size.

## Suggestions
1. **Add error bars** — run at least 3 seeds and report mean ± std for all main tables. This alone would dramatically increase confidence in the results.
2. **Characterize the $\mathcal{D}_s$ requirement** — state the size of the subset used, run an ablation on subset size (e.g., 1K, 5K, 10K, 50K samples), and discuss how representative the source samples need to be.
3. **Add wall-clock runtime** for the sequential and parallel DISTA variants vs. Tent, EATA, and SAR on a single GPU.
4. **For the federated setup**, add an ablation where all clients observe the same corruption (non-overlapping data) to isolate the effect of larger aggregated data from the effect of averaging across heterogeneous shifts, and compare against a non-federated version with equivalent batch size.

## Score and Decision

The paper presents a clean, well-motivated idea with consistently positive results across many settings. The weaknesses are mostly about incomplete validation (no error bars, no runtime numbers, uncharacterized source data requirement) rather than fundamental flaws in the method itself. The federated evaluation has the most significant gap (conflated sources of gain, no comparison to prior federated TTA), but this is an exploratory contribution rather than the paper's core claim. The main contributions — the distillation auxiliary task and the lookahead analysis — are solid. With the above issues addressed, this would be a strong paper.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>