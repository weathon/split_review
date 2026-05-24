Now I have enough context. Let me produce the final consolidated review.

## Summary

This paper addresses architecture overfitting in dataset distillation, where deep networks trained on distilled data perform poorly when their architecture differs from the shallow network used during distillation. The authors propose a combination of techniques — a DropPath variant for single-branch networks (with a three-phase keep-rate schedule and improved shortcut connections), knowledge distillation from a smaller teacher, periodical learning rates, the Lion optimizer, and stronger data augmentation — applied during training of the test network. The headline empirical findings are strong: e.g., on MTT CIFAR-10 IPC=10, ResNet50 accuracy jumps from 28.1% (baseline) to 63.8% (Full method), nearly matching the 63.6% of the 3-layer CNN that generated the distilled data. The pattern is consistent across architectures, distillation methods, and IPC settings on CIFAR-10, and the method also transfers to limited real data.

## Strengths

1. **Novel DropPath variant for single-branch networks (Section 3.1, Figure 3(b))**: The paper adapts DropPath by adding a virtual shortcut connection that is only activated during training when the main path is dropped. This makes DropPath applicable to architectures like VGG where standard DropPath would produce a zero output, and the authors clearly describe the training/inference asymmetry. This is a genuine (if incremental) architectural innovation.

2. **Large and consistent quantitative gains in cross-architecture generalization (Table 1)**: The empirical evidence is the paper's strongest contribution. On MTT IPC=10, ResNet50 goes from 28.1% to 63.8% (+35.7%), ResNet18 from 48.9% to 67.4% (+18.5%), AlexNet from 56.9% to 68.3%, and VGG11 from 52.6% to 67.1%. In many cases the Full method matches or exceeds the 3-layer CNN training network — directly demonstrating mitigation of architecture overfitting. The pattern holds across two distillation methods (FRePo and MTT) and three IPC settings (1, 10, 50).

3. **Component-wise ablation validates each innovation (Section 4.3, Tables on optimization/augmentation and DropPath components)**: The ablations quantify individual contributions: improved shortcut connection adds +1.4% (65.2→66.6), final high keep rate adds +0.4%, Lion optimizer adds +2.9% (61.9→64.8), and periodical LR + stronger augmentation add further gains. Hyperparameter sensitivity plots (Figure 3b,c) show the method is robust to KD weight and temperature within reasonable ranges.

4. **Generalization to limited real data (Section 4.2, Figure 2)**: With only 100 real training samples (CIFAR-10 fraction 0.002), the proposed DP+KD training lets ResNet18 and ResNet50 surpass the 3-layer CNN baseline, whereas the baseline training fails. This demonstrates the methods are not artifacts of the distillation process and have broader applicability to small-data regimes.

## Weaknesses

### Fatal

None.

### Major

1. **Only CIFAR-10 results are presented in the main paper, despite claims of generality across "different datasets."** The abstract and introduction assert the method is evaluated on "different datasets," and Section 4 states "we evaluate our method on different dataset distillation algorithms, different numbers of instances per class (IPCs), different datasets and different network architectures." Yet the only detailed empirical table (Table 1) and all figures in the main body report results exclusively on CIFAR-10. For a paper making strong empirical claims about generality, this is a significant evidential gap. (Note: Figure \ref{fig:app_4.2} references an appendix figure, and the stripped appendix may contain other-dataset results; but a conference paper's main text should be sufficiently self-contained to support its central claims.)

2. **Limited methodological novelty relative to the framing.** The paper's core contribution is an empirical demonstration that combining existing techniques — DropPath (modified for single-branch), KD, Lion optimizer, cosine annealing, k-fold augmentation — substantially mitigates architecture overfitting. The only technically new component is the virtual shortcut for single-branch DropPath, which is a minor architectural modification. The improved ResNet shortcut (max pooling + stride-1 conv) is also incremental. The paper is better understood as an empirical study / engineering recipe than as a new methodology. This does not invalidate the findings, but the paper overstates its novelty (e.g., "We propose a series of approaches in both architecture designs and training schemes") and would benefit from a more precise framing.

### Minor

1. **No error bars in the main results table (Table 1).** The paper acknowledges that "standard deviations increase when decreasing IPC" (Section 4.1) and Figure 2 does include standard deviation shadows for the real-data experiments, but the primary CIFAR-10 results table reports only point estimates. Without variance estimates, the reader cannot assess whether the improvements are statistically reliable, especially at IPC=1 where variance is acknowledged to be higher. This is a standard expectation for empirical papers.

2. **The headline performance gains conflate general training improvements with architecture-overfitting-specific effects.** The paper reports "performance gains of 18.5% and 35.7% for ResNet18 and ResNet50" (Section 4.1) comparing Full to Baseline. However, the ablation column "w/o DP & KD" (which applies the Misc. improvements: Lion optimizer, periodical LR, stronger augmentation, but no DropPath or KD) shows that ~2.4% of the 18.5% gain for ResNet18 on MTT IPC=10 comes from these general training improvements alone — not from the methods specifically aimed at architecture overfitting. The paper does provide the w/o DP & KD column in the table for readers to disentangle this, so it is not misleading, but the narrative repeatedly emphasizes the Full-vs-Baseline comparison without disambiguating the sources of improvement. A direct analysis showing that the *relative* improvement over baseline is larger on distilled data than on real data of the same size would strengthen the claim that the method specifically targets architecture overfitting.

3. **Three-phase keep rate schedule is incompletely specified.** The paper describes a three-phase schedule (keep rate p=1 initially, then decrease to a minimum, then increase to a large value in the final phase) and states "we shrink the keep rate every few epochs." However, the exact epoch counts per phase, the rate of decrease/increase, and the specific values of the final high keep rate are not provided in the main text. (The reference to Algorithm \ref{alg:droppath} suggests these details may be in the stripped appendix.) This hampers reproducibility.

### Trivial

None.

## Nice-to-Haves

- **Direct comparison of gain magnitude on distilled vs. real data per architecture.** The paper already shows real-data results (Section 4.2), but a side-by-side table comparing the *relative* improvement of Full over Baseline on distilled data vs. on same-size real data would more cleanly separate architecture-overfitting-specific gains from general training improvements.
- **Analysis of the implicit ensemble effect of DropPath.** The paper argues DropPath creates an ensemble of subnetworks. Measuring prediction diversity across dropout realizations and comparing to standard DropOut or stochastic depth would help validate the claimed mechanism.
- **Discussion of computational overhead** (training time, memory) of the proposed techniques, especially k-fold augmentation which increases the effective dataset size.
- **Comparison to simpler regularization baselines** (e.g., increased weight decay, label smoothing) to help isolate the unique value of the proposed combination.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"No comparison to existing approaches that also improve cross-architecture transfer in dataset distillation"** — The paper explicitly and reasonably explains why factorization methods are excluded (they use 5× larger IPC). The reviewer's suggestion of "training-network regularization during distillation, multi-architecture distillation, or ensemble distillation" addresses modifying the distillation process itself, which is outside the paper's stated scope (improving training of the test network post-distillation). Removed as scope creep.
- **"The improved shortcut connection contributes only ~0.4% improvement"** — This is a factual result honestly reported by the paper, not a weakness. It simply shows that this component's individual contribution is modest, which the paper's ablation table transparently conveys.
- **"The missing equation in Section 3.3"** — This is a PDF parsing artifact, not an error in the original submission. Removed per instructions.
- **"DropPath variant is a minor modification"** — This is a matter of perspective already covered under "limited methodological novelty" (Major weakness #2). Duplication removed.
- **"No results on other datasets in the main paper"** — This was merged into Major weakness #1 above.

## Novel Insights

The two reviewers converge on a key observation that goes beyond the paper's own framing: the paper's most significant contribution is not any single technique but the *empirical demonstration* that the gap between distilled-data performance and original-data performance for deep networks can be largely closed through careful training recipes, and that the "architecture overfitting" problem is substantially a *training* problem rather than a fundamental limitation of the distilled data. The ResNet50 result on MTT IPC=10 (28.1% → 63.8%) is striking precisely because it shows that the distilled data actually contains sufficient information to train a deep network — the bottleneck was entirely in how the test network was trained, not in the data quality. This reframes the problem from "how to distill data that generalizes across architectures" to "how to train deep networks on the already-distilled data," which is an important conceptual shift for the community.

## Suggestions

1. Add at least a summary table of results on CIFAR-100 and/or TinyImageNet to the main paper to support the claimed generality across datasets.
2. Add error bars (standard deviations over multiple runs) to the main results table.
3. Reframe the paper's contributions more precisely as an empirical study demonstrating that a combination of existing training techniques effectively overcomes architecture overfitting, rather than claiming novel methodology.
4. Provide the three-phase keep rate schedule with exact epoch counts and values (or ensure Algorithm \ref{alg:droppath} is included in the main text).
5. Include a direct comparison showing that the relative gains of the Full method over baseline are larger on distilled data than on same-size real data, to strengthen the claim that the method specifically addresses architecture overfitting.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>