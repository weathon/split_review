Now I have thoroughly read and verified the paper against all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes LMSP (Local Model Space Projection), an orthogonal-projection-based continual learning method that replaces the expensive global SVD on task representation matrices with a set of local low-rank decompositions defined via anchor points (adapting Local Low-Rank Matrix Approximation from recommendation systems). This reduces the per-layer complexity from O(n³) to O(n²) and expands the candidate pool of old-task correlations from t to t×m local subspaces. The paper provides convergence analysis (Theorem 1) and backward transfer analysis (Theorem 2), plus experiments on four CL benchmarks comparing against eight baselines.

## Strengths

1. **Novel application of local low-rank models to continual learning.** The paper correctly identifies the computational bottleneck of SVD in orthogonal-projection CL and adapts LLRA (Lee et al., 2013) — previously used in recommendation systems — to construct cheap local task subspaces. This is explicitly claimed as the first such application (Section 2) and is a genuinely new transfer of ideas.

2. **Theoretical complexity reduction is clearly motivated.** Section 4.1 walks through the complexity chain: AltMin on an M×Nʲ matrix costs O(M Nʲ r) = O(n²), and with m anchor points (m ≪ n), total cost stays O(n²). The contrast with standard SVD's O(n³) is clear and well-motivated, even if the bound is not empirically validated.

3. **Competitive accuracy and backward transfer on multiple benchmarks.** Table 1 reports that LMSP matches or exceeds all baselines on ACC and achieves the highest BWT on all four datasets (e.g., CIFAR-100 Split BWT = 0.157 vs. CUBER's 0.119). This provides meaningful evidence that the local approximation does not sacrifice task performance.

## Weaknesses

### Major

1. **Convergence claim is not supported by the stated bound.** The paper claims an "O(1/K) convergence rate" (Introduction) and that the method "converges to the first order stationary point" (Theorem 1, part 2). However, the bound in Theorem 1, part 2 contains non-vanishing constant terms involving initial gradient norms: [2+γ²(25−λ₁²)]‖ḡ₁(W^(0))‖² + 4‖g₁(W^(0))‖² + 4‖g₂(W^(0))‖². These do **not** vanish as K→∞, so the right-hand side does not go to zero. The bound therefore shows convergence to a neighborhood determined by initialization, not convergence to a stationary point. The convex-case statement ("converges to the optimal model") is similarly asserted without a supporting bound or rate. This overclaiming undermines the theoretical contribution.

2. **Central efficiency claim lacks empirical validation.** The paper's core practical selling point is reducing complexity from O(n³) to O(n²). Yet Table 1 reports only ACC and BWT — no wall-clock time, FLOP counts, memory usage, or any runtime measurement is provided anywhere. The ablation study (Figure 1) varies rank r and anchor count m for accuracy but never measures actual speed. Given that the method solves m separate AltMin optimization problems (each requiring iterative optimization), performs QR on A and B, plus an SVD on r×r matrices, the practical efficiency gain is not a foregone conclusion and must be measured. Without this data, the main practical claim is unsubstantiated.

3. **Algorithm description is incomplete — how multiple local subspaces are aggregated is unspecified.** Section 4.1 states that "we treat all m local model spaces as m old tasks" and "find the top-k correlated ones," but never specifies: (a) how correlation between the new task and a local subspace is measured, (b) how k is chosen, or (c) how update rules from different selected local models are combined (e.g., averaging, sequential application, weighted sum, most restrictive projection). Section 4.3 defines the three regimes only for a single pair (t, j^(q)). Since the entire framework depends on selecting and aggregating information from multiple local subspaces, this gap makes the reported results effectively irreproducible from the description.

4. **Experimental results lack statistical rigor.** All results in Table 1 are point estimates with no standard deviations, confidence intervals, or indication of how many random seeds were used. Given that LMSP outperforms strong baselines (including CUBER, which shares the same high-level structure) on nearly every metric, variance reporting is essential to assess whether improvements are meaningful. The hyperparameter selection protocol (learning rate, λ₁, λ₂, kernel bandwidth h, regularization coefficients) is also not described, nor is it stated whether the same protocol was used for all baselines.

### Minor

1. **Theorem 2's backward transfer claim is weaker than suggested.** The first part of Theorem 2 shows that under local relative orthogonality, the local projection update achieves a lower joint loss than the global projection update (ℱ(Wˢ) ≤ ℱ(Wᶜ)). This is a comparative bound (local vs. global), not a proof that performance on old tasks improves in absolute terms. The paper's text ("enables backward knowledge transfer") implies the latter but the theorem supports only the former.

2. **No sensitivity analysis for kernel bandwidth h.** The kernel bandwidth h (mentioned in Section 4.1 as a Gaussian kernel parameter) critically controls the locality of the low-rank approximation, yet it is never varied or discussed in the ablation study — only rank r and anchor count m are examined.

3. **Theoretical analysis considers only a single local subspace.** Theorems 1 and 2 analyze the case of one local subspace j^(q), but the practical algorithm uses m local subspaces per old task. Whether the convergence and backward-transfer guarantees extend to the multi-local-subspace setting is not addressed.

4. **The conditions in Theorems 1 and 2 depend on initial quantities (‖ḡ₁(W^(0))‖, ‖ḡ₂(W^(0))‖) that are not interpretable or checkable in practice.** It is unclear whether the required condition on λ₁ (stated in terms of these initial gradient norms) holds generically.

### Trivial

- None that survive filtering (potential acronym inconsistency LSMP/LMSP is a minor author error but carries no weight in evaluation).

## Nice-to-Haves

- A clear pseudocode block showing how the top-k correlated local spaces are identified and how their update rules are aggregated (sequential, weighted, or min-norm selection) would resolve the algorithm ambiguity.
- Wall-clock time per task (or total training time) for the full benchmark, ideally with a breakdown showing the AltMin/QR/SVD phases, would substantiate the O(n²) complexity claim.
- Multi-seed experiments with means ± std reported for all entries in Table 1.
- An ablation varying kernel bandwidth h to show sensitivity.

## Removed Points

The following points from the reviews were removed per the filtering guidelines:

- **Criticism about Eq. (3) being self-referential and typo complaints (LSMP vs. LMSP):** These are formatting/parser artifacts and author typos. The hard rules instruct removal of such nitpicks.
- **Missing baseline methods (OPG, CCL):** Per guidelines, missing-related-work criticisms are removed because we cannot independently verify their existence or relevance.
- **Missing appendix/proof details and "inequality appears truncated":** The parser strips appendices; these exist in the original submission. Truncation is a parser artifact.
- **Generic strengths from Strength Finder (e.g., "this paper addressed an important problem") without specific citation or concrete content:** Dropped per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the paper's claimed O(1/K) convergence rate and the actual bound (which has non-vanishing constants) — a point the paper's own discussion does not acknowledge — but this is a critique rather than a novel insight.

## Suggestions

1. **Fix the convergence analysis.** Either provide a bound where the constant terms vanish with K (re-establishing the O(1/K) claim), or explicitly revise the text to state a finite-time guarantee that depends on initialization quality. The current text claims "converges to the first order stationary point" but the bound does not support this.

2. **Add runtime measurements.** Include wall-clock time per task, or total training time, across all methods. This is the single most important missing piece for a paper whose main contribution is computational efficiency.

3. **Specify the multi-local-model aggregation procedure.** Write explicit pseudocode showing: (a) how correlation is scored for each local subspace, (b) how k is determined, and (c) the combination rule when multiple local subspaces from different anchor points and different old tasks are selected.

4. **Report standard deviations.** Repeat experiments with at least 3 seeds and report means ± std for both ACC and BWT.

5. **Clarify what Theorem 2 actually proves.** Distinguish between "local outperforms global" (which the theorem supports) and "backward transfer improves" (which is a stronger claim). Adjust the language accordingly.

## Score and Decision

The paper introduces a genuinely interesting idea — applying local low-rank approximation to orthogonal-projection continual learning — and achieves competitive accuracy results on four benchmarks. However, three major weaknesses prevent acceptance: the claimed convergence rate is contradicted by the paper's own bound, the central efficiency claim (O(n²) complexity) has zero empirical validation, and the algorithm's multi-local-model aggregation mechanism is underspecified to the point of irreproducibility. These are not minor gaps; they undercut the theoretical contribution, the practical contribution, and the reproducibility of the experimental results. A substantial revision addressing all three is needed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>