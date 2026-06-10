Now I have verified the reviewer claims against the paper. Let me write the final consolidated review.

## Summary

This paper proposes FedNewton, a Newton-type federated learning algorithm that communicates the global gradient (first-order information) and uses locally precomputed Hessian inverses, reducing per-iteration communication from O(M²) to O(M). The central contribution is theoretical: the first generalization bounds (excess risk) for a second-order FL method under both data heterogeneity (covariate shift) and model heterogeneity (concept shift) in the kernel ridge regression setting. The analysis decomposes the excess risk into a federated error that converges exponentially (when local sample sizes are sufficient and heterogeneity is moderate) and a centralized excess risk that achieves minimax-optimal rates. The bounds explicitly quantify how local sample size, covariate shift Δ<sub>𝔇ⱼ</sub>, and concept shift Δ<sub>fⱼ</sub> affect performance.

## Strengths

- **First generalization bounds for Newton-type federated learning.** Prior Newton-type FL work (Ghosh et al., 2020; Safaryan et al., 2022; Qian et al., 2022) provided only convergence (optimization) analysis. This paper bridges optimization and generalization by deriving excess risk bounds that simultaneously guarantee fast convergence and good generalization — a genuinely novel contribution clearly substantiated in Section 5 (lines 243–244).

- **Quantifies both covariate shift and concept shift in generalization bounds.** The paper introduces explicit measures Δ<sub>𝔇ⱼ</sub> (covariate shift) and Δ<sub>fⱼ</sub> (concept shift) in Definitions 1 (lines 122–136) and analytically characterizes their impact on the excess risk in Theorems 2 and 4 (lines 183–186, 220–228). This goes substantially beyond the DKRR literature (Guo et al., 2017; Lin & Cevher, 2020), which assumes i.i.d. local data (Δ<sub>𝔇ⱼ</sub> = Δ<sub>fⱼ</sub> = 0).

- **Communication-efficient design.** The algorithm's key innovation — using the global gradient with local Hessian inverses — reduces per-iteration communication from O(M²) to O(M) (line 100), matching first-order methods in total communication complexity O(Mt) while retaining Newton-type convergence benefits. This is directly compared against prior Newton-type FL methods (Safaryan et al., 2022; Qian et al., 2022) that communicated Hessian shifts at O(M²) cost.

- **Richer theoretical characterization than DKRR literature in four specific aspects.** Section 5 (lines 245–246) enumerates: (1) relaxing the source condition from r∈[1/2,1] to r>0 with 2r+γ≥1; (2) handling non-IID data with covariate + concept shift; (3) novel error decompositions for the federated error under heterogeneity; (4) covering both optimal and sub-optimal rates (four regimes of ℵⱼ in Theorem 3), whereas DKRR only studied optimal rates with restrictions on the number of partitions.

- **Shows sufficient local examples benefit both optimization AND generalization simultaneously.** Remark 7 (lines 234–235) provides a non-trivial insight: a large number of local examples can guarantee both linear convergence (for the federated error) and the optimal learning rate (from the centralized excess risk), rather than forcing a tradeoff between them.

## Weaknesses

### Fatal
None.

### Major

- **Convergence comparison with first-order methods conflates different quantities.** Remark 3 (line 104) states FedNewton achieves linear convergence t = Ω(log(1/ε)) while "first-order federated algorithms requires a large number of communication rounds t = Ω(1/ε)" (citing Su et al., 2021). Here ε is the *federated error* — the gap between the FedNewton iterate and the centralized KRR solution. The cited first-order rate t = Ω(1/ε) from Su et al. (2021) targets convergence to the optimal *population risk* under different assumptions (i.i.d. data, specific kernels). These are different objectives under different conditions, making the comparison uninformative and potentially misleading. The paper needs to either compare like with like or explicitly clarify the discrepancy.

- **Framing overclaims the scope of the theory.** The title "Efficient Newton-type Federated Learning with Non-IID Data" and the introduction (line 16: "similar computational and communication costs as the first-order methods") suggest a general FL method. However, the core theory relies critically on Proposition 1 (line 74), which holds only for the squared loss (Hessian independent of weights). Remark 4 (line 106) attempts to extend beyond squared loss but concedes that for weight-dependent Hessians (e.g., cross-entropy), the computational advantage disappears ("causing huge computational burdens"), effectively restricting the practical scope to losses where the Hessian is weight-independent (essentially squared loss and ReLU-type activations). The abstract does mention the KRR setting, but the gap between the general framing and the narrow guarantees remains too wide.

### Minor

- **Missing experiments section.** The abstract (line 4) promises "Extensive experimental results further validate our theoretical findings," the introduction (line 14) states "We conclude with experiments on simulated data and publicly available tasks," and Remark 3 (line 104) references "Section 7." However, the extracted text ends at Section 6 (Conclusion) with no experiments visible. While the paper's primary contribution is theoretical and can be evaluated on that basis, the empirical validation promised in the paper is absent from the reviewed material. The authors should ensure experiments are included in any future submission.

- **Claim of "similar computational costs" as first-order methods is imprecise.** The paper claims FedNewton requires "similar computational and communication costs as the first-order methods" (line 16). While per-iteration communication is O(M), the pre-iteration computation of each local Hessian inverse costs O(|𝔇ⱼ|M² + M³) (Remark 1, line 76), which is substantially more expensive than a first-order method's O(|𝔇ⱼ|M) per iteration. Remark 1 acknowledges this and suggests approximation schemes (BFGS, L-BFGS, etc.) but without analyzing their effect on the theoretical guarantees. The cost claim is therefore accurate only for the approximate variant, which is unanalyzed.

- **Remark 4 on extending beyond squared loss is underdeveloped.** The remark (line 106) contains a grammatical corruption ("is not applies") and an internal tension: it asserts applicability to broad loss functions while simultaneously noting that weight-dependent Hessians "cause huge computational burdens." The remark lacks a concrete characterization of which loss functions admit the precomputation that makes FedNewton efficient, leaving the practical scope unclear.

### Trivial
- The reference to "Section 7" in Remark 3 (line 104) without the section being present creates a dangling reference in the extracted text.
- The text in line 62 has minor parser corruption ("H_{\mathfrak{D}_{j},\lambda}^{-1} and H" appears duplicated/garbled), though this is likely an extraction artifact.

## Nice-to-Haves

- The bounds (Theorems 2–4) involve ≲ notation throughout, hiding constants. A more explicit characterization of the constants would strengthen the practical interpretability.
- A simplified bound or remark giving guidance in terms of *observable* quantities (e.g., empirical covariances) would increase practical value, though this is not standard for this type of theory paper.

## Removed Points

These points were flagged by the harsh critic but removed through the filtering process:

**"Υ depends on unobservable population-level parameters, reducing its informativeness"** — Removed. The quantities 𝒫<sub>𝔇ⱼ,λ</sub>, ℛ<sub>𝔇ⱼ,λ</sub>, and Δ<sub>𝔇ⱼ</sub> in Υ (Theorem 1, line 173) involve population operators, but this is standard practice in statistical learning theory. Bounds in this literature routinely involve population-level quantities that are subsequently controlled via concentration inequalities. The bound is a high-probability statement (with probability 1−δ), and the paper explains (line 136) how these quantities decrease with local sample size. This criticism is a generic area sweep that would apply to most theory papers in this tradition, not a specific problem with this paper's results.

**"The theoretical guarantees are narrower than the paper's framing suggests"** (full version) — Partially kept as a Major weakness but filtered of the harsh critic's overstatement. The critic claimed the paper "broadly claims" applicability to a broad range of loss functions, but the paper's abstract explicitly says "In general kernel ridge regression setting" and Remark 4 includes substantial caveats. The framing gap is real but narrower than the critic asserted.

**"Section-by-section notes on Introduction and Problem Setup"** — Removed as editorial commentary rather than concrete weaknesses. The note about overlooking related work violates the "missing related works" rule.

## Novel Insights

Beyond the paper's own contributions, two review-level insights emerge: (1) The paper's four-regime analysis of ℵⱼ in Theorem 3 reveals an interesting phase transition where the federated error's dependence on local sample size shifts across regimes — this is a richer characterization than typical DKRR work and could inform practical resource allocation decisions (how many local samples per client are "enough"). (2) The tension between Remark 4 (extension to general losses) and Proposition 1 (reliance on weight-independent Hessians) is not fully resolved in the paper; this points to a genuine open problem about whether second-order FL methods can be made efficient for general convex losses without sacrificing the communication savings that make FedNewton attractive.

## Suggestions

1. **Converge the framing with the actual scope.** Revise the title and introduction to state explicitly that the analysis is for the KRR / squared-loss setting. The paper's contribution — first generalization bounds for Newton-type FL under heterogeneity — is meaningful even within this scope. Overclaiming weakens rather than strengthens the paper.

2. **Fix the convergence comparison in Remark 3.** Either (a) compare FedNewton's federated error convergence rate with first-order methods' convergence to the *same* quantity (the centralized KRR solution) under the same assumptions, or (b) clearly state that the cited rates address different objectives and explain why the comparison is still informative.

3. **Either include experiments or adjust the text.** If experiments exist in the original submission, ensure they are accessible. If they do not exist, remove or substantially qualify the claims in the abstract and introduction about experimental validation.

4. **Acknowledge the limitations more explicitly in the conclusion.** Section 6 (lines 256–259) presents only positive results without discussing the narrow setting (squared loss, KRR, precomputable Hessians) or the gap between the general framing and the specific guarantees.

## Score and Decision

This paper makes a genuine theoretical contribution — the first generalization bounds for Newton-type FL methods under data and model heterogeneity — and the analysis is technically solid, with a clean error decomposition and systematic treatment of multiple factors. The phase-transition analysis (Theorem 3) and the quantification of covariate/concept shift (Theorem 4) are non-trivial advances over the DKRR literature. However, the paper is weakened by (a) a convergence comparison that conflates different quantities, (b) a framing that overclaims the scope of the theory, and (c) the absence of visible experiments that the paper itself promises. The theoretical contribution is real but narrow, and the paper would benefit from scoping adjustments before it meets the bar for a top venue. 

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>