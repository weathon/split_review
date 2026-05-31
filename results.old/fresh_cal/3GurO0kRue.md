Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

This paper studies implicit subpopulation imbalance — where class labels are balanced but hidden subpopulations within classes are skewed — and proposes SHE (Scatter and HarmonizE). SHE jointly learns a soft partition of training data into subpopulations and per-subpopulation classifiers, then aggregates them via LogSumExp to produce subpopulation-balanced predictions. The theoretical development connects the optimal partition to maximizing interaction information I(X;Y;ν), and Thm. 3.4 shows that LogSumExp over per-subpopulation logits yields the balanced distribution. Experiments across COCO, CIFAR-100, tieredImageNet, and spurious-correlation benchmarks show consistent gains over 12+ baselines, with the key finding that minority subpopulations improve substantially (e.g., +4.42% on the Few-split in COCO) without harming majority performance.

## Strengths

- **Principled formulation linking subpopulation discovery to interaction information.** Definition 3.1 casts optimal data partition as maximizing I(X;Y|ν) − I(X;Y), and Theorem 3.3 proves that minimizing the proposed empirical risk (Eq. 1) for a fixed ν asymptotically aligns with this objective, with a finite-sample Rademacher bound. This grounds subpopulation discovery in information theory rather than heuristic clustering.

- **Elegant LogSumExp aggregation for balanced predictions.** Theorem 3.4 shows that applying log-sum-exp to per-subpopulation logits directly yields the subpopulation-balanced distribution p_bal(x,y). This is a simple closed-form operation that replaces post-hoc weighting or resampling — a clean theoretical-to-practical bridge.

- **Consistent and significant gains across diverse benchmarks.** Table 2 reports SHE outperforming all 12+ baselines on COCO (+1.72%), CIFAR-100 at IR∈{20,50,100} (+1.35–1.53%), and tieredImageNet (+1.42%), with means and stds over multiple runs. Table 3 shows the per-split analysis: the Few-split improves by +4.42% over the best baseline while Many and Medium splits also improve, directly validating the claim that subpopulation rebalancing benefits all groups.

- **Empirical validation of subpopulation discovery.** Figure 3 shows NMI between learned subpopulations and ground-truth annotations rising to ~0.8 on the toy dataset during training. Figure 4(d) shows SHE achieves NMI ~0.5 on Waterbird, substantially above EIIL, ARL, and GRASP. The paper also describes qualitative visualizations (Fig. 5, appendix) showing SHE discovers distinct subpopulations (e.g., cut-up vs. whole fruit on COCO).

- **Multi-head strategy adds no parameters.** Section 3.4 splits feature channels and classifier weights into K groups, keeping total parameter count identical to a standard single-head classifier. This rules out the trivial explanation that performance gains come from increased capacity.

- **Robustness to hyperparameters.** Figure 4(a) shows SHE is stable across K=2–5 (best at K=4), and Figure 4(b) shows robustness to β from 0.5–2.0, with gains over ERM even at β=0.

## Weaknesses

### Fatal
None.

### Major

- **Theory–practice gap in the joint optimization.** Theorem 3.3 establishes consistency for minimizing Eq. (1) **given a fixed partition ν**. However, the actual algorithm (Eq. 2, Section 3.4) jointly optimizes both the per-sample assignment matrix *V* (N×K parameters) and the network parameters via gradient descent, adding a diversity regularization term that the theory does not cover. The abstract states "With theoretical guarantees" — this is misleading because the guarantees apply to an idealized version (oracle partition), not to the full algorithm executed. The paper does partially address this empirically (Fig. 3 shows NMI rising during training, Fig. 4d shows SHE outperforms baselines on subpopulation discovery), but the theoretical claim as written overstates what is proved. **Impact**: the paper's contributions remain empirically strong, but the "theoretically guaranteed" framing needs explicit qualification. The authors should either (a) extend the theory to the joint setting (e.g., variational bound) or (b) honestly delineate what is proved vs. what is heuristic.

### Minor

- **No discussion of limitations or failure modes.** The paper lacks a limitations section. Several issues go unaddressed: (1) the per-sample assignment matrix *V* is a transductive parameter (N×K values optimized directly, discarded at test time) — the paper does not discuss why this avoids overfitting, how the entropy and diversity terms regularize it, or why an inductive version (*V* predicted from *x*) underperforms (Fig. 4c); (2) no practical guidance is given for choosing *K* when no prior knowledge exists (the ablation shows robustness, but a heuristic or diagnostic would help practitioners); (3) sensitivity to the diversity term's interaction with the entropy term is not analyzed. Including a candid limitations paragraph would strengthen the paper significantly.

- **Non-standard sign of interaction information not clarified.** The paper defines I(X;Y;ν) = I(X;Y|ν) − I(X;Y), which is the negative of the conventional McGill interaction information (I(X;Y) − I(X;Y|ν)). While the argmax is unchanged (I(X;Y) is constant), the paper describes it as "the gain of correlation between X and Y given a data partition" — in the standard definition, a positive value of I(X;Y) − I(X;Y|ν) means ν *reduces* the correlation. Readers familiar with information theory will be confused. The paper should explicitly note this sign reversal and justify why their convention is appropriate for this setting.

### Trivial

- **Figure reference is broken.** Line 104 says "We also visualize the two subpopulations learned by our method in COCO in Fig." — the figure number is missing (it should be Fig. 5, referenced correctly in the next sentence). This appears to be a LaTeX compilation artifact but should be fixed.

## Nice-to-Haves

- **Computational cost comparison.** A brief note on training time and/or memory overhead (the N×K assignment matrix adds storage proportional to dataset size) relative to ERM would help practitioners assess deployment feasibility.
- **Move subpopulation visualizations to the main paper.** The paper references Fig. 5 (appendix) showing discovered subpopulations on COCO (cut-up vs. whole fruit). Including this in the main paper would strengthen the claim that SHE discovers *meaningful* structure.
- **Ablation on feature dimension per head.** The multi-head strategy splits the D-dimensional feature equally among K heads (each gets D/K channels). An analysis of whether this limits expressiveness for large K, or whether the choice of K interacts with D, would be informative.

## Removed Points

These points were removed from the main review with justification:

1. **"The paper does not discuss whether the multi-head architecture can achieve the necessary approximation for Theorem 3.3."** — This is speculative; Theorem 3.3 is stated in terms of a general hypothesis space with a Rademacher complexity bound, not tied to the specific multi-head realization. The gap between theory and practice is already addressed in the Major weakness above. **Removed.**

2. **"Fig. 5 in the appendix (not provided here) showing learned subpopulations."** — The appendix is stripped by the PDF parser but exists in the original submission. The paper's text already describes what Fig. 5 shows. **Removed per rule: parser artifacts do not constitute author errors.**

3. **"Missing proofs in the appendix" / "Appx. C.2 for the complete proof"** — The parser removes appendix content; these proofs exist in the original submission. **Removed per rule.**

4. **Generic concerns about "potential memorization" without evidence.** The critic's speculation that V might memorize training samples is not supported by any evidence in the paper (the per-split results in Tab. 3 show generalization, not overfitting). The paper's ablation (Fig. 4c) also addresses this by comparing with an inductive version. **Removed as speculative.**

## Novel Insights

The most interesting observation that emerges from the reviews is the **tension between per-sample transductive optimization of V and the method's strong generalization**. The paper shows that an inductive version (predicting V from x) underperforms (Fig. 4c), suggesting that the joint optimization of V with the entropy and diversity terms is doing something qualitatively different from learning a function ν(x). This is an underexplored design choice in the subpopulation-discovery literature, and a deeper analysis of *why* per-sample optimization works (e.g., does the entropy term act as a regularizer that prevents memorization? does the dependence on both x and y in Definition 3.1 make a difference?) could lead to insights about when transductive vs. inductive approaches are preferable for latent structure discovery.

## Suggestions

1. **Reframe the theoretical claims.** Replace "With theoretical guarantees" in the abstract with something like "Theoretically motivated by an information-theoretic optimal partition" or similar, and clearly delineate in Section 3 that Theorem 3.3 applies to minimizing Eq. (1) for a given ν, while the joint optimization (Eq. 2) is a practical heuristic validated empirically.
2. **Add a limitations paragraph** discussing the transductive nature of V, choice of K, and potential memory overhead.
3. **Clarify the sign convention** for interaction information (Section 3.1) with a brief footnote or explicit remark.
4. **Provide practical guidance on choosing K** (e.g., cross-validation, or monitoring entropy of learned assignments as a diagnostic).

## Score and Decision

**Originality.** The paper tackles an under-explored problem (subpopulation imbalance without annotations) and connects it to interaction information in a novel way. The LogSumExp aggregation is an elegant technical contribution. — High.

**Importance of research question.** Subpopulation imbalance is pervasive in real-world applications (medical diagnosis, autonomous driving) and existing class-level methods cannot address it. The question is timely and important. — High.

**Claims supported?** The empirical claims are well-supported by extensive experiments. The theoretical claims about "guarantees" are partially overstated (see Major weakness). With proper reframing, the remaining claims are adequately supported. — Moderate-to-high (discounted by the theory-practice framing gap).

**Soundness of experiments.** Strong. Multiple datasets, multiple imbalance ratios, comprehensive baselines (12+), per-split analysis, ablations for each component, and extension to spurious correlation and class+subpopulation combined settings. Statistics reported with means and stds. — High.

**Clarity of writing.** Generally clear. The notation is precise, the motivation is well-illustrated (Fig. 2), and the method section is logical. Minor issues: the broken figure reference, and the interaction information sign convention could confuse. — Moderate-to-high.

**Value to the community.** High. The method is simple, parameter-efficient, and consistently effective. Practitioners working with data where hidden subpopulations may exist can directly apply SHE. The theoretical framing (even if partially heuristic in practice) provides a new perspective on subpopulation discovery.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>