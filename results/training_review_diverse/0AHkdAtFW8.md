Now I have a thorough understanding of the paper. Let me write the final consolidated review after careful cross-verification of every claim.

---

## Summary

This paper introduces a computational framework — the first of its kind — that uses sum-of-squares (SOS) programming to certify or falsify the Ma–Trudinger–Wang (MTW) non-negativity condition for optimal transport ground costs. It addresses two problems: the *forward* problem of globally certifying the MTW(0) or NNCC conditions, and the *inverse* problem of computing an inner semialgebraic approximation of the region where these conditions hold locally. Numerical examples recover known analytic thresholds and extend to costs where analytic verification is prohibitive.

## Strengths

- **First computational approach to OT regularity certification.** The paper explicitly claims novelty as "the first work on computational certification of OT regularity" (Sec. 1), and this claim is supported: prior work on MTW verification is entirely analytic and problem-specific (Ma et al., 2005; Lee & McCann, 2011; Khan & Zhang, 2020). The SOS-based approach opens a new methodological direction.

- **Successful recovery of known analytic results.** Example 1 for n=1 recovers the exact analytic threshold ε_max = 2/3 for the perturbed Euclidean cost (Table 2, first column). For n=2, the SOS residual is 1.25×10⁻¹¹, providing a clean numerical certificate that matches known theory. This validates the correctness of the SOS reformulation.

- **Extension to cases where analytic verification is infeasible.** The method certifies MTW(0) for the isotropic multivariate normal log-partition cost for n≥3 (Example 2), where "analytic verification of non-negativity of poly is significantly challenging" (Sec. 4.1). The approach also handles non-rational cost functions (the log-partition cost in Example 2, the surface metric in Example 4) provided the MTW tensor elements become rational after a suitable transformation.

- **Novel inverse problem formulation.** The paper formulates and solves the inverse problem of finding inner semialgebraic approximations of regions where MTW(0) holds (Sec. 3.2, Examples 3 and 4). This goes beyond simple certification and addresses the practical scenario where global MTW(0) fails but local regularity is sufficient. CPU times (0.97s for Example 3, 19.6s for Example 4) confirm practical tractability.

- **Use of standard, reproducible tools.** All experiments use widely available SOS toolboxes (SOSTOOLS, YALMIP) on a standard laptop, making the method immediately accessible.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Numerical residuals in some results undermine the "certificate" claim for those cases.** The residual is defined as the largest coefficient in 𝔖 − sᵀs (Sec. 4.1). While the n=1 and n=2 results in Example 1 are clean (residual ~10⁻¹¹ or zero), the residuals in Example 2 (Table 3) are substantially larger — 2.09×10⁻⁴ for n=3 and 0.2 for n=4. A residual of 0.2 means the SOS decomposition found by the solver is not an exact representation of the polynomial, so the result does **not** constitute a provable certificate of non-negativity. The paper reports these values transparently, which is good, but it continues to call the results "certificates" and claims the approach is "provably correct" in the abstract without sufficiently discussing when numerical certificates are valid vs. when they are merely suggestive. The paper should either (a) qualify the strength of the evidence for cases with large residuals, or (b) add a verification step (e.g., evaluating the remainder's sign on a dense grid or using rational arithmetic).

- **The inverse problem objective is an acknowledged heuristic, not a rigorous volume maximization.** The derivation in Sec. 3.2 replaces vol(𝒰×𝒱) maximization with minimization of ∫_Λ V(x,y) dx dy, attributed to "the heuristic used in Theorem 2 of Jones (2024)." The paper is transparent about this being a heuristic, but the consequences are not discussed: the computed region is guaranteed to be a valid inner approximation (by the SOS constraints), but it is **not** guaranteed to be the largest possible such region. The claims about the inverse problem should more clearly distinguish between the validity guarantee (the region satisfies MTW(0)) and the optimality claim (which is heuristic). As a minor note, the notation in Theorem 7 (e.g., "V_+⁻", unsubscripted "±" constraints) is unclear and should be cleaned up.

- **Inverse problem results lack independent validation.** The computed regions in Examples 3 and 4 (Figures 1, 2) are shown but never independently verified — e.g., by evaluating the MTW tensor at sampled points inside the region to confirm non-negativity, or by checking points just outside the region to see if the condition indeed fails. Such validation would substantially strengthen confidence in the method, especially since the volume-reduction step is a heuristic.

- **Missing implementation details hinder reproducibility.** The specific SDP solver used (e.g., SeDuMi, Mosek, SDPT3) and key solver options (e.g., tolerance settings) are not reported. The problem size for the forward SOS programs (number of variables, polynomial degree, number of SOS multipliers) is also not given. These details are standard to report in the SOS literature.

### Trivial
- The notation in Theorem 7 is sloppy: the "±" signs appear without explanation, and the subscript "+−" in V₊⁻ is not defined in the text.

## Nice-to-Haves

- A discussion of the practical limitations of SOS scaling with ambient dimension n would help readers assess applicability. The current paper reports results up to n=8 but does not analyze how the SDP size grows.
- A comparison against brute-force random sampling (as a sanity check on small problems) would provide context for the SOS certificates.
- For the inverse problem, a simpler baseline (e.g., fixing the region as a ball/cube and optimizing its radius under SOS constraints) would clarify the value added by the general polynomial parameterization of V.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about missing Section 3.1 (Forward Problem):** The paper's organization section (line 36) clearly states "Sec. 3 details the SOS formulation for the forward problem (Sec. 3.1)." The forward problem section was stripped by the text extraction parser; it exists in the original submission. Per instructions, this criticism is removed.
- **"The derivation of the inverse problem is not supported":** The paper explicitly says "utilizing the heuristic used in Theorem 2 of Jones (2024)" (line 138). Calling it a heuristic is transparent; the paper does not claim a rigorous proof of the volume-equivalence identity. The reviewer's characterization as "not supported" ignores the paper's own qualifying language.
- **Accusation that non-zero residuals "directly contradict" the provably-correct claim:** The abstract's "provably correct" refers to the SOS approach (if an exact SOS decomposition exists, non-negativity follows), not to the numerical solver's ability to always find exact decompositions. Numerical residuals are standard in all SOS/SDP literature. The paper reports residuals transparently. This is a standard practice, not a contradiction.
- **Generic strengths from Strength Finder** (e.g., "Rigorous motivation") that are superficial or lack specific evidence are dropped.
- **Complaints about fairness of comparison:** Not applicable — the paper does not perform comparative benchmarking.
- **Formatting nitpicks** (typos, broken characters, garbled text): These are parser artifacts, not author errors.

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the framework's theoretical appeal (provably correct SOS reformulations) and the messy reality of floating-point SDP solvers (large residuals that undermine the certificate interpretation). This tension is not unique to this paper — it pervades the entire SOS literature — but it is particularly salient here because the paper stakes its contribution on "provably correct" certificates. The inverse problem heuristic also raises a deeper question: how much of the difficulty in OT regularity certification is genuinely structural (the MTW condition is a pointwise inequality of a biquadratic form) versus algorithmic (the volume maximization objective resists convexification)? The paper makes a reasonable start on both fronts, but neither problem is fully resolved, pointing toward clear research directions in exact rational SOS methods and certified inner-approximation techniques for OT.

## Suggestions

1. **Add a verification step for the larger-residual cases.** For Example 2 (n=3,4,8), evaluate the polynomial 𝔖 at a dense set of random points within the domain and report the minimum value. This would confirm whether the polynomial is indeed non-negative despite the inexact SOS decomposition.
2. **Qualify the language around "certificates" and "provably correct."** In the abstract and conclusions, distinguish between cases where exact (or numerically negligible) residuals provide valid certificates and cases where the residuals are larger and the evidence is only suggestive.
3. **For the inverse problem, clearly separate the validity guarantee from the optimality heuristic.** The region found is a valid inner approximation; the claim that it is "largest" is heuristic. Add a sentence to this effect.
4. **Report the SDP solver name and key parameters.** Even a brief sentence ("We used Mosek with default tolerances via YALMIP's 'solvesos' command with the 'sedumi' backend") would substantially improve reproducibility.
5. **Validate the inverse regions with spot-checks.** For Examples 3 and 4, evaluate the MTW tensor on a 50×50 grid inside the computed region and report the minimum eigenvalue of F(x,y). This would confirm the computed region genuinely satisfies MTW(0).

## Score and Decision

The paper introduces a genuinely novel cross-pollination of SOS programming and OT regularity theory. The forward problem formulation is technically sound (standard SOS with a correct mapping from MTW non-negativity to polynomial non-negativity). The inverse problem is more tentative but still interesting. The numerical evidence is mixed — clean for some cases, noisy for others — and the paper would benefit from more careful discussion of what constitutes a certificate versus numerical evidence. The core contribution is real but modest: this is an application of well-understood SOS tools to a new domain, not a new algorithmic or theoretical result in either SOS or OT. The paper is publishable but needs revisions focused on honest qualification of its numerical results and better documentation of its experimental setup.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>