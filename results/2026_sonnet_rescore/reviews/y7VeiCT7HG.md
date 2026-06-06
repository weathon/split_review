## Summary

This paper proposes Probability of Matching (PM), a probabilistic acquisition framework for batch multi-objective Bayesian optimization (MOBO). The key idea is to factorize the event that an acquired batch exactly matches the true Pareto optimal set X* into two components: the probability that all batch points are Pareto optimal, and the probability that they collectively cover X*. This factorization motivates qEHVI-SF, which multiplies qEHVI by a minimum-pairwise-distance term to promote design-space diversity. The paper also introduces Expected Minimum Distance (EMD), a design-space coverage metric, and validates the method on synthetic benchmarks and a real-world six-objective alloy inverse design task.

---

## Strengths

- **Principled probabilistic framing with a clean decomposition.** Eq. 7 factors P(**X** = X*) into P(**X** ⊆ X*) · P(X* ⊆ **X** | **X** ⊆ X*), making both quality and coverage explicit targets. This cleanly diagnoses why qEHVI can concentrate near extreme Pareto front regions (it only optimizes the first factor) and motivates the space-filling augmentation without requiring a manually tuned trade-off hyperparameter—a genuine advantage over QSVGD.

- **Efficient, hyperparameter-free method.** The space-filling term adds O(q(n+q)d) cost per iteration (Section 3.3), which is negligible relative to the O(NmK(2^q − 1)) qEHVI term. The method has no η to tune, unlike QSVGD's decaying schedule. Table 1 confirms that practical runtimes are largely comparable across methods.

- **Strong empirical results, especially the alloy design case study.** Figure 2 shows qEHVI-SF consistently achieves the highest rediscovery ratio across 18 conditions (3 batch sizes × 6 objective-group settings), including the hardest six-objective case. The rediscovery metric is directly practically relevant for inverse design, and the results are robust across 20 trials with notably smaller variance than competing methods.

- **New metric EMD (Eq. 9) is well-motivated.** EMD evaluates coverage in design space rather than objective space, making it stricter than IGD for inverse design tasks where the practitioner wants to recover specific Pareto-optimal designs, not merely their objective-space images.

- **Consistent performance across batch sizes.** Both qEHVI and QSVGD show substantial sensitivity to batch size (Section 4.1); qEHVI-SF remains stable, which is a meaningful practical robustness property.

---

## Weaknesses

### Fatal
None.

### Major

- **The theoretical bridge from Eq. 7 to Eq. 8 is incomplete.** Section 3.2 states that "normalized qEHVI" approximates P(**X** ⊆ X*), but the paper does not define what normalization is applied, whether the normalized value lies in [0, 1], or whether normalization is well-posed as the Pareto front changes across iterations. Similarly, the minimum-distance term approximates P(X* ⊆ A_**X**^r | **X** ⊆ X*) via a ball-overlap geometric argument, but this is intuition, not a formal surrogate bound. Moreover, Eq. 8 places the expectation operator over the full product—the hypervolume improvement times the min-distance scalar—rather than separately estimating the two probability factors and multiplying them as Eq. 7 prescribes. The paper's Limitations section (Section 5) honestly acknowledges that "the precise relationship between pairwise distance and true coverage probability remains unclear," but this concession is understated relative to the theoretical weight placed on PM throughout the paper. The core contribution would be more credible if it were presented as a well-motivated heuristic augmentation of qEHVI rather than as an estimator of a formally defined probability. This does not undermine the method's empirical validity, but it overstates the theoretical grounding.

- **Baseline comparisons are limited.** The paper compares qEHVI-SF only against qEHVI (Daulton et al., 2020, five years old) and a MOBO extension of QSVGD that was originally a single-objective method and that the authors themselves adapted (Section 2.2). While the paper argues in Section 2.2 that "not many related works have taken into account the diversity of Pareto optimal solutions," this argument is incomplete: methods such as EMMI (Olofsson et al., 2018) and IGD-NS (Tian et al., 2016) are cited but then excluded because they operate in objective space—yet including them would still provide a more complete picture. Competing primarily against one's own adaptation of a single-objective method is insufficient to establish state-of-the-art performance for a 2025/2026 venue.

### Minor

- **EMD computation is unexplained for RE4-7-1.** Section 4.1 describes RE4-7-1 as having an "unknown Pareto optimal set," yet Figure 1 reports EMD (Eq. 9), which requires X*. The paper does not explain how X* is estimated or approximated for this benchmark. This is a methodological gap that needs to be addressed (e.g., via a large-reference-set approximation, which should be stated explicitly).

- **The EMD metric is partially circular as an evaluation criterion.** qEHVI-SF directly maximizes minimum intra-batch and batch-to-observations distances, and EMD measures the average distance from each point in X* to the nearest observed point. These are closely related quantities, making strong EMD performance partly tautological for qEHVI-SF. The hypervolume and rediscovery results are more independently informative; EMD results should be presented as corroborating rather than independent evidence.

- **High runtime variance in Table 1 weakens computational efficiency claims.** Several entries in Table 1 have standard deviations exceeding the mean (e.g., qEHVI at q=5 "All": 46.03 ± 52.18s; qEHVI-SF at q=10 "All": 52.01 ± 70.60s). The paper attributes this to early convergence of the optimizer (Section 4.3), which is plausible, but the claim of "minimal additional overhead" is not well-supported under these high-variance conditions for m=6.

### Trivial
- The paper asserts that qEHVI tends to oversample in extreme regions because those points are less likely to be dominated, which drives P(**X** ⊆ X*) up (Section 3.1). This is stated as an intuition without an empirical illustration. A 2D design-space visualization of qEHVI's concentration near extreme Pareto regions versus qEHVI-SF's dispersion on the GM problem would make the core argument immediate and compelling.

---

## Nice-to-Haves

- Clarify the normalization applied to qEHVI when using it as a proxy for P(**X** ⊆ X*)—even a simple statement (e.g., dividing by the maximum qEHVI value across the candidate set) would allow the method to be reproduced as described.

- Add a visualization for the GM problem (2D design space) showing that qEHVI concentrates near extreme Pareto regions while qEHVI-SF disperses—this would directly illustrate the failure mode diagnosed in Section 3.1.

- Analyze whether the alloy-design results (discrete pool of 1,000 candidates) generalize to continuous design spaces; the minimum-distance criterion may have different behavior in continuous vs. discrete settings.

- Evaluate the sensitivity of qEHVI-SF to the specific form of the space-filling term (e.g., average distance instead of minimum distance, or a kernel-based coverage criterion).

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Contemporary baselines like DGEMO, MESMO are absent"** (Harsh Critic): Removed per hard rule prohibiting criticism of missing related works that cannot be independently verified. The paper's own framing of the baseline choice is internally consistent with its design-space diversity motivation.

- **"The approach is fatally disconnected from the probability it claims to estimate"** (Harsh Critic framing as structural/fatal): Demoted to Major. The paper explicitly acknowledges the gap in Section 5 (Limitations), which makes it an honest approximation claim rather than a fabricated theoretical equivalence. The empirical evidence stands regardless.

- **"QSVGD comparison is unfair because it is the authors' own extension"** (Harsh Critic): Retained as part of the Major baseline weakness, but the framing of "unfairness" is removed since the authors disadvantage their baseline (not their own method) by adapting QSVGD suboptimally.

- **"The discrete pool limits generalizability"** (Harsh Critic, Section 4.2): Removed as speculative — the concern that qEHVI-SF benefits disproportionately from discreteness is not supported by any analysis in the paper. Moved to Nice-to-Haves.

- **"qEHVI's tendency to favor extreme solutions is stated without proof"** (Harsh Critic): Kept as a Trivial observation (visualization suggestion), but removed as a standalone weakness since this is a known property cited with references (Auger et al., 2009; Tian et al., 2016).

- **Generic strengths from Strength Finder** (e.g., "the paper addresses an important problem" and "the motivation for design-space diversity is well-argued"): Retained only in condensed form with specific textual grounding. The observation about design-space diversity arguments (Section 2.2) is substantive and kept.

---

## Novel Insights

The paper's most valuable insight is the decomposition of the acquisition objective into two probabilistic components with different failure modes: methods that maximize only P(**X** ⊆ X*) systematically under-explore the Pareto set because extreme-front points are less likely to be dominated (hence easier for a quality metric to identify), while a coverage term explicitly counteracts this bias. Operationalizing the coverage term as a simple min-distance scalar inside the qEHVI expectation is a lightweight and practically effective design decision. The EMD metric, operating in design space rather than objective space, is a genuinely useful diagnostic that separates front-coverage from design-recovery — an important distinction for inverse design tasks.

---

## Suggestions

1. **Reframe the theoretical contribution honestly**: Present qEHVI-SF as a well-motivated approximation whose two factors correspond to the two PM components, and show that Eq. 8 is a consistent (if informal) surrogate for Eq. 7. Explicitly state the normalization used for qEHVI. This would be more honest and still constitute a clear methodological contribution.

2. **Clarify the RE4-7-1 EMD computation**: State explicitly how X* is approximated for this benchmark (e.g., using a dense reference set from a long evolutionary run), and include a caveat on the resulting EMD values.

3. **Expand baseline comparisons**: Include at least one additional diversity-aware MOBO method (one operating in design space if available, or EMMI/IGD-NS in objective space as upper/lower bounds of coverage metrics) to contextualize qEHVI-SF within the broader landscape.

4. **Add a GM visualization**: Show design-space sample distributions for qEHVI vs. qEHVI-SF on the 2D GM benchmark across iterations to directly demonstrate the overclustering failure mode and how qEHVI-SF resolves it.

---

## Score and Decision

**Originality:** The decomposition idea is conceptually clear and the EMD metric is genuinely useful, but the technical novelty — adding a min-distance term to qEHVI — is incremental. The probabilistic framing provides motivation but is not fully derived. Solid but not breakthrough. (4/5)

**Importance of Research Question:** Design-space coverage in batch MOBO is practically significant, especially for inverse design. The alloy design application is well-chosen and illustrative. (4/5)

**Claims Supported:** Empirical claims (better hypervolume, rediscovery, EMD) are well supported by the alloy design study and synthetic benchmarks. The theoretical claim (Eq. 8 estimates Eq. 7) is not formally established, though honestly acknowledged. (3/5)

**Soundness of Experiments:** The alloy design task with 20 trials, 6 objective combinations, and 3 batch sizes is a solid experimental design. The RE4-7-1 EMD gap and the high runtime variance are genuine gaps. Discrete pool limitation reduces generality claims. (3/5)

**Clarity:** The paper is well-organized and clearly written. The geometric argument for space-filling (Section 3.2) is intuitive. Missing definition of normalization hurts reproducibility but this is a minor presentation issue. (4/5)

**Value to Community:** qEHVI-SF is simple to implement, hyperparameter-free, and empirically effective. The EMD metric is a useful contribution to the evaluation toolkit. Community adoption is plausible. (4/5)

The paper makes a genuine practical contribution — qEHVI-SF is a sensible, effective, and efficient augmentation of qEHVI — backed by compelling alloy design results. However, the theoretical framing overstates what has been derived, and the baseline comparison is thin for a 2025/2026 submission. These are addressable weaknesses rather than fatal flaws. The paper sits at a borderline weak-accept position: the empirical contributions justify publication but the theoretical and evaluation gaps require revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>