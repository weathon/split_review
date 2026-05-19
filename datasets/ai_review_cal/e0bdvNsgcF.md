- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 1, 5, 1
Now I have a thorough understanding of the paper and can verify claims against the actual text. Here is my consolidated review.

---

## Summary

This paper proposes a continuous optimization model for locating the largest/smallest elements of tensors given in low-rank (CP) format, by converting the problem to a spherical-constrained optimization over rank-one factor vectors. The authors develop an alternating iterative method with a maximum block improvement (MBI) strategy (Algorithm 1) that provably converges to a stationary point, and a block-search variant (Algorithm 2) that searches over multiple fibers per iteration to improve accuracy. The greedy shift-based extension handles k>1 elements. Experiments on synthetic and real-world tensors demonstrate substantial speedups over power iteration, star sampling, and MinCPD, with competitive accuracy.

---

## Strengths

- **Novel continuous optimization model with generality across tensor formats.** Theorem 1 reformulates element location as a spherical-constrained problem over rank-one vectors, and the paper explicitly notes (line 59) that this "also applies to other tensor formats such as Tucker, TT, and QTT." This generality goes beyond prior optimization-based approaches that are tailored to CP format (Sidiropoulos et al., 2022).

- **MBI-based alternating method with convergence theory.** Algorithm 1 is accompanied by Theorem 2 (global convergence to a stationary point) and Theorem 3 (R-linear local convergence under a closeness assumption). These guarantees are stronger than those available for sampling methods or for power iteration with recompression, which lacks formal convergence guarantees.

- **Block-search strategy yields measurable accuracy gains over MinCPD.** Table 1 reports accuracy improvements of up to 48.2% for largest-element and 266.7% for smallest-element detection over MinCPD across 50 random tensors. The block-search variant (Algorithm 2) consistently improves over plain alternating iteration, and the paper documents that results are stable across block sizes b=3,5,7.

- **Substantial and well-documented computational efficiency gains.** On large-scale multivariate-function tensors (d=10, grid size 4096), Table 2 reports speedups of 41.9×–176.0× over power iteration, 7.4×–27.7× over star sampling, and 11.0×–778.5× over MinCPD. On random tensors, Figure 2 shows 2.2×–86.4× speedups over star sampling. These efficiency benefits are the paper's strongest empirical contribution and are consistently observed across all experiments.

- **Parameter-free alternating updates.** Unlike MinCPD (which requires tuning a curvature parameter) or power iteration (which needs a recompression threshold), the core alternating update (Section 3, subproblem 3.1) reduces to finding the largest element of a vector and is parameter-free.

---

## Weaknesses

### Fatal

None.

### Major

- **The paper's narrative overclaims accuracy advantages, and some accuracy claims are contradicted by the paper's own data.** The abstract and introduction claim "significant improvements in both accuracy and efficiency over the existing works," yet multiple results show the proposed methods are *less* accurate than star sampling:

  * Table 1 (random tensors): the paper's own text (line 170) states "star sampling achieves higher accuracy than the iterative methods in this example" (star sampling 92% vs. proposed max 88%).
  * Table 2 (Rastrigin function): star sampling reports a max value of 11538.09 while Algorithm 2 reports 10918.32 — star sampling is 5.7% *better*. The paper's claim that "the accuracy of star sampling is broken due to the increase in the size of tensors" is contradicted by this very data.
  * The paper's claim (line 205) that Algorithm 2 "improves accuracy by at least 14.3% and 25% compared to star sampling and MinCPD, respectively" on real-world tensors appears to cherry-pick the most favorable case; the reviewer reports star sampling ties or exceeds Algo2 in 5 of 12 comparisons in Table 4. **(Note: Since Table 4 is an embedded image, I cannot independently verify the exact numbers — but the stated claim as written is absolute and conflicts with the reviewer's reading.)**

  The paper would be much stronger if it honestly characterized its accuracy as competitive but not universally superior, and acknowledged that star sampling remains more accurate on some problem instances.

- **The power iteration comparison is insufficiently justified.** The paper acknowledges (line 20) that power iteration "cannot directly obtain the corresponding location due to errors in the iterative process," yet includes it as a baseline and reports speedups of 41.9×–176.0× against it. For a paper whose core task is *locating* elements (not just estimating values), the baseline needs to be solving the same problem. The paper provides no explanation of how a location is extracted from the power iteration eigenvector. While the value-comparison in Table 2 is still meaningful, the paper should either (a) describe the extraction procedure and its limitations, or (b) clearly separate the value-finding and location-finding evaluations.

### Minor

- **Tensor order N is not specified for the random tensor experiments.** The random tensor setup (Section 5.1) states dimensions I_n ∈ [10, 50] and rank R ∈ [1, 10], but does not state N (the number of modes). Since the efficiency of alternating methods scales linearly with N, and the total tensor size is exponential in N, this omission makes the random tensor experiments difficult to fully interpret or reproduce.

- **Missing details on accuracy metric construction.** (a) For random tensors: ground-truth enumeration is non-trivial for tensors up to 50^N entries, but the paper does not describe how exact largest/smallest elements are determined. (b) For real-world tensors: the accuracy metric (#hit/k) does not specify how many candidates each algorithm returns — if star sampling returns many more than k candidates while the proposed method returns exactly k, the metric could be biased. These details should be clarified.

- **The greedy top-k extension has a practical limitation that is acknowledged but under-discussed.** The shift-transformation approach (Section 3.3) increases CP-rank by k, and the paper notes this is "only suitable for small k." The experiments test only k ≤ 15. This is a real restriction that limits the method's applicability, and the paper could be more upfront about it.

### Trivial

None.

---

## Nice-to-Haves

- A Pareto-style analysis (accuracy vs. time) for star sampling under varying sample budgets would provide a richer comparison than the single operating point (min(10⁵, 20% of parameters)) used in the paper. This would strengthen the efficiency claims by showing the proposed method's advantage across the accuracy–time curve.
- Error bars or variance estimates over multiple runs would strengthen the random tensor results (currently reported as single accuracy percentages over 50 tensors).
- An ablation study for block size b on real-world tensors (currently only shown for random tensors in Table 1).

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The star sampling baseline is not fairly configured"** (Harsh Critic Point 3) — The paper uses the default configuration recommended by Lu et al. (2017). Requesting a Pareto analysis is a nice-to-have, not a weakness. **Reason for removal:** The reviewer's criticism asks for an analysis beyond standard practice; the paper follows the baseline's own guidelines.

2. **"The restart strategy (100 restarts) is applied to MinCPD and the proposed method but not to star sampling or power iteration"** (part of Harsh Critic Point 4c) — Restarts are a standard practice for initialization-sensitive iterative methods. Star sampling is not iterative and power iteration does not conventionally use restarts. **Reason for removal:** The asymmetry is natural, not unfair.

3. **"Theoretical contribution is solid but limited"** (Harsh Critic Point 5) — This is a subjective assessment, not a factual weakness. The paper provides Theorems 2 and 3 (convergence to stationary point, local linear rate) which are meaningful guarantees absent from competing methods. **Reason for removal:** Subjective opinion, not an actionable flaw.

4. **Strength Finder Core Strength claim about Table 4 "at least 14.3% improvement over star sampling"** — The reviewer contests this claim and reports specific counterexamples. Since Table 4 is a parser-stripped image, neither I nor the paper text can resolve the dispute. The strength as stated reflects what the paper claims, but its accuracy requires independent verification against the original Table 4. **Treated with caution.**

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension: the paper's strong efficiency results are well-supported, but its accuracy narrative is over-inflated and occasionally contradicted by the reported data. The most productive observation from the reviews is that the proposed method's genuine competitive advantage is speed (often orders of magnitude), not universal accuracy — and the paper should be restructured around this honest trade-off rather than claiming simultaneous improvement on both axes.

---

## Suggestions

1. **Rewrite the accuracy narrative to be honest about the trade-off.** Acknowledge that star sampling achieves higher accuracy on some problem instances (random tensors, Rastrigin max), while the proposed method's strength is computational efficiency with competitive accuracy. Remove or soften "significant improvements in both accuracy and efficiency" from the abstract and conclusion.

2. **Clarify the power iteration comparison.** Either describe how locations are extracted from the power iteration eigenvector, or reframe the comparison as purely about value estimation speed (and move it to a supplementary role). If the location extraction cannot be justified, consider removing the power iteration baseline.

3. **Supply missing experimental details:** report N (tensor order) for all experiments, describe how ground-truth largest elements are computed, and specify how many candidates each algorithm returns for the accuracy metric.

4. **Verify the "at least 14.3% improvement over star sampling" claim** against Table 4. If the reviewer's counterexamples are correct, correct or remove this claim.

5. **Add an explicit limitations paragraph** covering: (a) star sampling can be more accurate on some problems, (b) the greedy k-extended method is limited to small k due to CP-rank growth, and (c) Algorithm 2 lacks convergence theory.

---
