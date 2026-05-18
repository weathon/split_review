Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces HStat-Net, a three-component architecture (pre-trained feature extractor ϕ, statistical net s, task net h) that bridges large pre-trained models with Generalized Linear Models (GLMs) in federated learning. The authors argue that CLIP's feature space is not sufficiently linearly separable for GLM-based statistical tools, so HStat-Net refines representations via triplet training on s. Building on HStat-Net, they propose FedRACE, a poisoning attack detector that uses deviance residuals from the GLM-based task net to identify malicious clients. A Chebyshev bound on the total misclassification rate is provided. Experiments on CIFAR-100, Food-101, and Tiny ImageNet under five attack types show FedRACE achieving substantially lower attack success rates (e.g., ASR 0.07% vs. 0.61% for the next-best baseline on CIFAR-100) while maintaining high benign accuracy.

## Strengths

1. **Novel integration of GLMs with large pre-trained models in FL.** HStat-Net is the first FL architecture designed to make GLM-based statistical tools (deviance residuals, Chebyshev bounding) work on top of frozen large feature extractors. The two-step training (first h, then s) is a sensible strategy to avoid gradient conflicts between cross-entropy and triplet loss (Section 3.1).

2. **Strong and consistent empirical performance.** In Table 4, FedRACE achieves the lowest ASR and BA across all five attack types on all three datasets, often by wide margins (e.g., 0.07% ASR vs. 0.61% for FLAIR on CIFAR-100 under TLFA; 0.06% BA vs. 1.30% for FLAIR under ECBA). These gaps are large — orders of magnitude — suggesting a genuine advantage rather than a tuning artifact.

3. **Comprehensive robustness evaluation.** The paper evaluates FedRACE under extreme non-IID (α=0.1), near-IID (α=0.9), varying numbers of malicious clients (M=8, M=24), and a different feature extractor (ResNet-152). TPR remains >0.97 and FPR remains low across all these conditions (Figures 5–7).

4. **Validation of the representation refinement.** Table 2 shows that HStat-Net improves Fisher's Criterion by 3.34× and Mutual Information by 2.02× over raw CLIP features, providing concrete evidence that the refined space is more linearly separable — which is the prerequisite for GLM-based detection.

5. **Cutoff estimation is empirically validated.** Table 5 measures the gap between the estimated cutoff $\hat{p}$ and the true $p^*$, showing small errors (e.g., 0.02 on Tiny ImageNet under ECBA), which supports the practical utility of the heuristic even if the theoretical guarantee does not perfectly match the algorithm.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 is overclaimed relative to the implemented algorithm.** The theorem (Appendix A.2) proves a Chebyshev bound on TMR under the assumption of *known* distribution parameters $\mu_\mathcal{B}, \mu_\mathcal{M}, \sigma^2$ and a *fixed* threshold at their midpoint. However, the actual algorithm (Section 4.3) says: "For each value between 1 and n, we calculate an upper bound and select the point that minimizes the bound as the final $\hat{p}$." This requires estimating the parameters from the same residuals used to determine the cutoff, making the bound data-dependent — the Chebyshev guarantee no longer holds as a true frequentist bound. The paper does not clarify whether plug-in estimates are used, nor does it discuss the validity gap. The empirical success of the cutoff heuristic (Table 5) is real, but the paper's claim to "provide a theorem to support FedRACE's detection" is misleading as currently presented. This does not invalidate the empirical results but needs to be honestly scoped.

2. **Baseline comparison fairness is not sufficiently justified.** The paper states that "we use the same HStat-Net architecture across all defense methods" (Section 5.1). For FedRoLA, which was designed for per-layer analysis of deep networks, reducing the trainable component to two layers (h and s) may fundamentally alter how its mechanism operates. For FLAIR, which uses a reputation decay parameter, it is unclear whether this was tuned per baseline or simply given a single default value. Trimmed-mean and Multi-Krum are architecture-agnostic and should transfer cleanly, but FLShield's validation set composition and size are not reported as matched across methods. The paper should clarify exactly what was shared across methods and what adaptations (if any) were made to each baseline for the HStat-Net setting. The large performance gaps mitigate this concern but do not eliminate it.

3. **No analysis of adaptive attacks against the statistical net.** Since s is trained locally by all clients, a malicious client aware of FedRACE could deliberately train s to produce representations that evade detection while still poisoning h. The threat model (Section 4.1) assumes the adversary has limited knowledge (unaware of the aggregation rule or benign updates), but an adversary who knows FedRACE exists could still manipulate their local s. This scenario is not discussed or tested. Adaptive attacks are a standard consideration in the FL defense literature (FLAIR explicitly evaluates against them), and their absence here weakens the security claim.

### Minor

4. **No-attack baseline is missing from the defense comparison table.** Table 4 reports ACC, ASR, and BA under attacks but has no row showing model accuracy when no attacker is present. The paper has clean accuracy of 75.99% from Table 1 (partially fine-tuned CLIP), but it is not placed alongside the defense results for direct comparison of whether FedRACE degrades benign accuracy. This should be added.

5. **Two-step training is not ablated against alternatives.** The paper motivates two-step training as a way to avoid gradient conflicts between triplet loss and cross-entropy (Section 3.1), but provides no experiment comparing it to joint training with a weighted loss. Similarly, the triplet loss on s is not compared to simpler alternatives (e.g., a linear projection trained with only cross-entropy, or a fixed random projection) to isolate whether the triplet loss is driving the detection improvement or merely dimensionality reduction. These ablations would strengthen the attribution of gains to specific design choices.

6. **HStat-Net's classification accuracy gain over CLIP is modest (1.19%) given the dramatic separability improvements.** While this does not undermine the paper's core claim (which is about enabling *detection*, not classification), the introduction motivates HStat-Net partly by saying GLMs "struggle with the complex feature representation spaces from pre-trained models." The modest accuracy gain weakens this motivation somewhat — the main benefit of HStat-Net is clearly the statistical detection capability, and the paper should frame this more clearly rather than leaning on the classification improvement as supporting evidence.

7. **Communication overhead of per-class mean representations is not discussed.** Each client sends per-class mean representations (for CIFAR-100 with d=256, that is 25,600 floats per round) in addition to model parameters. The paper claims "enhanced scalability and efficiency" (Section 1) but provides no analysis of this overhead relative to baselines like FLShield (which requires a validation server). This is a practical consideration that should be quantified.

### Trivial

8. **"Does not require pre-defined parameters" (Section 1) is slightly overstated.** The detection algorithm uses K, subset size, and a voting threshold — all derived from n rather than pre-defined constants. This is still qualitatively different from FLAIR's reputation decay parameter, but the claim could be refined.

## Nice-to-Haves

- Ablation of the subset size K in majority voting to show sensitivity.
- Comparison of the deviance residual aggregation (weighted by log) against simpler alternatives (e.g., max class residual or sum).
- Evaluation under a stronger adaptive adversary who can manipulate s representations.

## Removed Points

These points are flagged to be removed — treat them with caution if referenced.

- **Harsh Critic's weakness about "The paper should have included a 'no-defense' baseline" being entirely missing:** The paper does reference clean accuracy (75.99%) in Table 1 and attacked accuracy (64.24%) without defense in Section 4.1. The information exists in the paper, just not in the main comparison table. Moved to Minor (#4).
- **Harsh Critic's observation about "fixed Dirichlet α=0.5" as a weakness:** The paper evaluates α=0.1 and α=0.9 in Figure 6, so this is partially addressed. The baselines are not re-run under extreme non-IID, which is a scope limitation rather than a flaw in FedRACE.
- **Strength Finder's "theoretical guarantee for detection" as a strength:** Overclaimed given the theorem-algorithm mismatch. Kept as a claimed strength but the weakness in the Major section addresses the gap.

## Novel Insights

The most interesting insight from the reviews is that the separation between what Theorem 1 actually proves (a bound under known parameters and a fixed threshold) and what the algorithm does (data-dependent cutoff selection via bound minimization) mirrors a common tension in ML security papers: a theoretically neat bound is presented as grounding, but the practical heuristic succeeds for reasons (the residuals are well-separated) that the theorem does not actually guarantee. The empirical results in Table 5 are what really validate the cutoff selection, not the theorem. A stronger paper would either develop a data-adaptive concentration bound or present the theorem as a conceptual motivation rather than a guarantee.

## Suggestions

1. **Revise the theoretical claim.** Either: (a) clearly state that Theorem 1 provides conceptual motivation (the bound under known parameters), and that the algorithm uses empirical plug-in estimates as a heuristic whose validity is empirically validated (Table 5); or (b) develop a data-dependent bound using concentration inequalities that holds with high probability. The first option is far simpler and honest about the limitation.

2. **Clarify baseline comparison setup.** State explicitly: (a) whether all baselines used the full HStat-Net architecture (including s) or just CLIP+linear head; (b) what hyperparameter tuning was performed for each baseline; (c) how FedRoLA was adapted for the two-layer case.

3. **Add a no-attack row to Table 4** showing ACC for each defense method (or just FedRACE) under clean conditions, so readers can verify that the defense does not degrade normal performance.

4. **Add a simple ablation** comparing the full HStat-Net (s with triplet loss) against: (i) CLIP features with no s (just h), and (ii) s trained with only cross-entropy (no triplet loss), for detection performance. This would isolate the contribution of triplet training.

5. **Add a brief discussion** of why the adaptive attack scenario (malicious client spoofing s) is not covered by the current threat model and whether FedRACE could be extended to handle it.

## Score and Decision

**Score:** 5.5  
**Decision:** Accept

The paper makes genuine contributions — a novel architecture for integrating GLMs with large models in FL, and a detection mechanism with empirically strong results across multiple datasets and attack scenarios. The weaknesses are real (overclaimed theorem, baseline justification, missing ablations, no adaptive attack analysis) but addressable in a revision. No weakness is fatal: the empirical results are robust enough to stand on their own even with the theoretical claim scaled back, and the baseline fairness concern is partially mitigated by the sheer size of the performance gaps (9–22× improvement over the next-best baseline). With revisions to scope the theoretical claim honestly, clarify the experimental setup, and add the recommended ablations, this would be a solid paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>