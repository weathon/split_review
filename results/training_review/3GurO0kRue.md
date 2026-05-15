Now I have all the information I need. Let me synthesize the final consolidated review.

---

## Summary

This paper studies the problem of implicit subpopulation imbalance, where classes are balanced but hidden subpopulations are skewed. The authors propose SHE (Scatter and HarmonizE), which jointly learns to partition training data into subpopulations via an objective grounded in interaction information (Def. 3.1, Thm. 3.3) and produces subpopulation-balanced predictions via LogSumExp aggregation (Thm. 3.4). Extensive experiments on COCO, CIFAR-100, tieredImageNet, CelebA, and Waterbirds show consistent improvements over 11 baselines.

## Strengths

- **Consistent and substantial accuracy gains across diverse benchmarks.** Table 2 shows SHE outperforms all 11 baselines on COCO (+1.72%), CIFAR-100 at three imbalance ratios (+1.35–1.53%), and tieredImageNet (+1.42%). These gains are statistically meaningful given the small reported standard deviations.

- **Significant improvement on minority subpopulations without sacrificing majority performance.** Table 3 shows SHE achieves a 4.42% gain over the best baseline on the Few split of COCO while also attaining the best results on Many and Medium splits — directly supporting the claim of subpopulation rebalancing.

- **Principled theoretical motivation.** The paper defines optimal data partition via interaction information (Def. 3.1), proves that minimizing the proposed empirical risk asymptotically aligns with maximizing interaction information (Thm. 3.3), and shows LogSumExp aggregation yields subpopulation-balanced predictions (Thm. 3.4). These results provide a principled foundation for the method.

- **Evidence of meaningful subpopulation discovery.** Figure 3 shows NMI between learned subpopulations and true annotations increasing during training on the toy dataset. Figure 4(d) shows SHE achieves higher NMI than EIIL, ARL, and GRASP on Waterbirds. Visualizations on COCO (Fig. 5, referenced) show interpretable subpopulations (e.g., "cut-up" vs. "whole" produce).

- **Comprehensive ablations validate each component.** Table 5 shows removing the entropy term degrades performance, and using learned subpopulations in the EIIL way (SHE_EIIL) is inferior to SHE's LogSumExp aggregation. Figure 4(a–c) ablates K, β, and the direct-vs-model-based optimization of V, respectively.

- **Broad experimental coverage.** The paper evaluates on subpopulation imbalance, class+subpopulation imbalance (Table 4 left), spurious correlations via SHE+GDRO (Table 4 right), and fine-tuning from CLIP/ALIGN/AltCLIP (Table 6), demonstrating versatility.

## Weaknesses

### Fatal
None.

### Major

1. **Per-sample optimization of the subpopulation-weight matrix V risks overfitting and is not analyzed for generalization.** The N×K matrix V is directly optimized per training sample (Eq. 2) with no explicit regularization on the assignments themselves. While the entropy term Ĥ(Y|V) and diversity term Div(x) provide some structure, the paper does not analyze train-test consistency of the learned assignments, stability to initialization, or performance as a function of training set size. The ablation comparing direct optimization to a model-based V (Fig. 4c) shows direct optimization wins, but this is expected given vastly higher capacity. Without further analysis, it is unclear whether V is discovering meaningful structure or fitting noise, and whether its benefit would persist on larger or noisier datasets.

2. **No evaluation on a real-world dataset where subpopulations are natural and unlabeled.** Despite motivating the problem with CheXpert (Fig. 1, age subpopulations in medical diagnosis), all experiments use datasets where subpopulation structure is explicitly defined by the experimenter (subclasses in CIFAR-100/tieredImageNet, attributes in COCO, predefined groups in Waterbirds/CelebA). These are valid benchmarks, but the central claim of handling *implicit* subpopulations in realistic settings would be substantially strengthened by at least one experiment on a dataset with naturally occurring demographic or environmental subgroups (e.g., CheXpert with age/sex, or MultiNLI with genre).

### Minor

1. **Theory-practice gap in joint optimization.** Theorem 3.3 shows that minimizing the empirical risk asymptotically approximates maximizing interaction information *for a fixed ν*. However, in the actual algorithm, V (which encodes ν) is jointly optimized with f. The bound's Rademacher complexity term scales with K, and the global lower bound m on log f^y(x) is unrealistic for deep networks. The theory provides useful intuition but does not certify the joint optimization procedure or guarantee that the learned V approximates the optimal data partition.

2. **Label-dependence of ν(X,Y) is not discussed.** Definition 3.1 allows the data partition to depend on both input X and label Y. The paper does not discuss whether this could lead to partitions that memorize label-predictable patterns rather than discovering meaningful subpopulation structure. While the empirical results suggest this does not happen in practice, an explicit discussion would strengthen the paper.

3. **Number of random seeds/experimental runs not reported.** Results are reported as Mean ± Std (e.g., Table 2, Table 4) but the number of seeds is not stated. This makes it difficult to assess the statistical reliability of the reported improvements, especially for the fine-tuning experiments (Table 6) where gains are 0.3–0.8 percentage points.

4. **NMI comparison on Waterbirds (Fig. 4d) is ambiguous.** The text claims a comparative analysis between SHE and EIIL/ARL/GRASP, but the description of Fig. 4(d) only states it "presents the NMI scores... on Waterbird" without clarifying whether the comparison is actually plotted or only SHE is shown.

5. **No limitations discussed.** The conclusion does not acknowledge limitations (e.g., needing to pre-specify K, risk of V overfitting, reliance on synthetic benchmarks), which would help readers assess the method's applicability.

### Trivial

- The number of subpopulations K must be specified in advance; while Fig. 4(a) shows robustness to K across 2–8, no guidance is provided for choosing K on a new dataset.
- The diversity term ablation (Fig. 4b) lacks error bars.

## Nice-to-Haves

- Evaluate on a dataset with naturally occurring implicit subpopulations (e.g., CheXpert with demographic subgroups) to directly support the claim of handling implicit subpopulations in realistic settings.
- Add explicit regularization on V (e.g., entropy penalty on assignments, feature-based constraints) to reduce overfitting risk.
- Provide a principled method for selecting K (e.g., validation-based selection, automatic relevance determination).
- Report the number of seeds and/or confidence intervals for main tables.
- Analyze the generalization of V (e.g., fraction of samples with confident assignments at convergence, distribution of assignments on test set).
- Scale to a larger dataset (e.g., ImageNet-scale) to assess the practicality of the N×K assignment matrix.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the comparison to methods using true annotations (SD, CIM) is unfair.** The paper presents these methods "for reference" (line 178) and does not claim to beat them. The core comparison to methods without group labels (EIIL, ARL, GRASP, JTT, etc.) is fair. *Reason: The paper is transparent about this, and the asymmetry favors the baseline, not the author's method (per Hard Rule 3).*

- **Claim that the paper does not show superiority of subpopulation discovery because NMI comparisons are only mentioned.** The paper states "Fig. 4(d) presents the NMI scores on Waterbird between the recovered subpopulations and the ground truth annotations" and the figure caption says "(d) NMI score." Whether the comparison is plotted depends on the actual figure (not visible in text extraction). *Reason: Cannot verify from text alone; partial information.*

- **Criticism that "the key lies in effective subpopulation discovery with proper rebalancing" is stated as a finding but is essentially the premise.** This is standard rhetorical framing in ML papers. *Reason: Not a substantive weakness.*

- **Request for theoretical guarantees on joint optimization or a certificate that V approximates optimal partition.** The theorem provides asymptotic consistency, which is the standard form of theoretical support in this literature. *Reason: Overly demanding for an empirical systems paper.*

- **Criticism that the multi-head strategy "divides the feature dimension by K, reducing per-subpopulation capacity."** The paper explicitly states this "does not introduce any additional parameters" and is a design choice. The capacity trade-off is acknowledged implicitly. *Reason: Not a flaw — this is a deliberate architectural choice.*

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core empirical results but surface a meaningful gap between the claim of handling "implicit" subpopulations and the synthetic nature of the benchmarks, and raise a legitimate concern about the unregularized per-sample optimization of V that the paper does not adequately analyze.

## Suggestions

1. **Address the overfitting concern for V directly.** Add an experiment studying train-test consistency of V assignments, or at minimum, analyze the distribution of v_is at convergence (e.g., what fraction of training samples receive near-deterministic assignments?).
2. **Add at least one experiment on a dataset with naturally occurring implicit subpopulations.** CheXpert is the obvious choice given the motivation in Fig. 1. Even a small experiment would substantially strengthen the paper's central claim.
3. **State the number of experimental seeds** for all reported Mean ± Std results, and consider bootstrapped confidence intervals for the fine-tuning experiments where gains are small.
4. **Add a limitations section** discussing the need to pre-specify K, the risk of V overfitting, and the scope of the current evaluation.
5. **Clarify what is plotted in Fig. 4(d)** — if only SHE is shown, the comparative analysis claimed in the text is not supported by that figure.

## Score and Decision

The paper tackles a genuine problem with a creative, theoretically motivated method and delivers consistent empirical improvements across multiple benchmarks and settings. However, two concerns prevent a stronger recommendation: (1) the per-sample optimization of V is not analyzed for overfitting, which is critical because the method's capacity to fit noise could undermine generalization claims; and (2) despite motivating with a real-world medical example, all evaluations use synthetic benchmarks where subpopulation structure is explicitly designed by the experimenter. These issues are addressable but are not merely presentational — they affect how strongly the paper's central claims are supported. The paper would benefit from a revision cycle to address these points. I recommend rejection in its current form but note the paper has clear potential for a strong resubmission.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>