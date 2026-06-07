I now have enough calibration data. Let me write the final review.

## Summary

This paper introduces FedMPDD, a federated learning algorithm that encodes each client's gradient by computing its directional derivatives along *m* random Rademacher vectors, transmitting only the *m* scalar projections plus a seed per client per round, thus reducing uplink communication from O(*d*) to O(*m*). The core technical claim is that averaging *m* projections overcomes the dimension-dependent variance of single-projection methods and achieves O(1/√K) convergence (matching FedSGD) via the Johnson–Lindenstrauss lemma. Privacy is claimed to arise from the rank-deficiency of the projection operator.

## Strengths

1. **Clean theoretical result in Lemma 1.** The expected relative gradient reconstruction error of (*d*−1)/*m* for Rademacher projections (Equation 6) is correctly derived and provides a meaningful quantification of how many projections control estimator variance. This is the paper's most defensible theoretical contribution.

2. **Empirical demonstration of joint communication-privacy benefit.** Tables 1 and 2 show that FedMPDD achieves SSIM < 0.22 under gradient inversion attacks while maintaining competitive accuracy within a tight communication budget, whereas competing compression methods (lp-proj, Top-k, SA-FedLora) leak substantial information (SSIM 0.74–0.91). The communication reduction numbers (e.g., 356× vs. FedSGD on CIFAR-10) are genuinely impressive.

3. **Problem identification is well-motivated.** The paper correctly identifies that a single projected directional derivative suffers from √*d* norm scaling (lines 94–98), which would force impractically small step sizes. The multi-projection averaging idea is a natural and principled approach to this specific issue.

## Weaknesses

### Fatal

1. **Misapplication of the Johnson–Lindenstrauss lemma invalidates Theorem 2 (lines 108–112, Equation 4).** The paper claims that the operator $\frac{1}{m}U_{k,i}U_{k,i}^\top$ satisfies $\|\frac{1}{m}UU^\top g\| \leq (1+\varepsilon)\|g\|$ with $m = O(\ln(d/\delta)/\varepsilon^2)$, citing the JL lemma. This is mathematically incorrect. The JL lemma guarantees that the *sketch* $\frac{1}{\sqrt{m}}U^\top g$ preserves its norm in the low-dimensional space $\mathbb{R}^m$; it says nothing about the norm of the *reconstruction* $\frac{1}{m}UU^\top g$ in $\mathbb{R}^d$. A direct calculation (consistent with the paper's own Lemma 1) gives:

$$\mathbb{E}\!\left[\left\|\frac{1}{m}UU^\top g\right\|^2\right] = \|g\|^2\left(1 + \frac{d}{m}\right),$$

so the expected reconstruction norm is approximately $\sqrt{d/m}\,\|g\|$, *not* $(1+\varepsilon)\|g\|$. Achieving $(1+\varepsilon)\|g\|$ would require $m = \Omega(d)$. This is not a minor gap — the convergence bound in Theorem 2 depends on $\varepsilon$ as a distortion parameter that can only be made small with $m = O(\log d)$ under the paper's incorrect JL reasoning. With the correct variance scaling ($d/m$), the claimed $O(1/\sqrt{K})$ rate cannot be sustained with $m = O(\log d)$, and the central theoretical guarantee of the paper collapses.

### Major

1. **Theorem 2 is unverifiable from the available text.** Assumption 1 is referenced (line 114) but never stated in the main paper. The parameters $\sigma^2$ and $G$ in Equation (5) are not defined anywhere in the visible text. Without these, a reader cannot evaluate whether the theorem's conditions are reasonable or whether the stated bound is meaningful.

2. **The privacy analysis establishes gradient-level uncertainty, not formal data-level privacy.** Lemma 1 correctly quantifies gradient reconstruction error, but Lemma 2's jump from "gradient cannot be exactly recovered" to "private data cannot be reconstructed" depends on a Lipschitz constant $L_v(\mathbf{x})$ that is never quantified or bounded for the models tested. The bound in Lemma 2 could be vacuous. The multi-round bound (Remark 2: $T \times m < d$) is a necessary condition for non-uniqueness of a linear system, not a sufficient condition for data privacy — an adversary with prior information could do substantially better than solving the underdetermined system.

### Minor

1. **The evaluated implementation computes the full gradient before projecting (Algorithm 2, line 6), so per-round client computation is $O(dm)$, exceeding FedSGD's $O(d)$.** Remark 1 discusses avoiding this via Jacobian-vector products but states this is evaluated in a follow-up study, not in the current paper. The framing (e.g., "resource-constrained scenarios") thus overstates the computational savings of the evaluated method.

2. **The SSIM values for FedMPDD jump from $<0.03$ in Table 1 (MNIST/LeNet) to 0.14–0.22 in Table 2 (CIFAR-10/CNN) without discussion** of whether this reflects a model/dataset effect or a change in privacy protection. Relatedly, baselines like lp-proj, Top-k, and SA-FedLora are penalized on SSIM despite making no privacy claims, which is valid for showing FedMPDD's joint benefit but the framing as "outperforming" these methods on privacy is uneven.

3. **The claim that "smaller values of $m$ can actually achieve comparable or even faster convergence" (line 226) contradicts the paper's own theory** that smaller $m$ increases variance and slows convergence. If this is empirically true, it suggests a regularizing effect that merits analysis, but none is provided.

### Trivial

None.

## Nice-to-Haves

- An ablation on $m$ as a main-text figure (currently Appendix Table A.9) would strengthen the central empirical claim about logarithmic scaling.
- A DP-SGD baseline with formal $(\varepsilon,\delta)$ guarantees would calibrate what "privacy" means relative to the standard in the field.
- The convergence analysis should be rebuilt on the correct variance calculation (Lemma 1 already provides $\mathbb{E}[\|\hat{g}_i - g_i\|^2] = \frac{d-1}{m}\|g_i\|^2$) rather than the incorrect JL argument.

## Removed Points

- Criticisms about missing related works, formatting artifacts, and missing appendix/proof content (removed per protocol — these are parser issues or require external knowledge).
- "Fundamentally new multiplicative encoding paradigm" as an overstatement (removed as a subjective framing concern, not a technical weakness).
- The harsh critic's claim that the paper lacks baseline comparisons for privacy (removed — LDP comparisons are present; the absence of DP-SGD is noted in Nice-to-Haves, not a current weakness).
- Strength Finder's claim about the JL-based convergence guarantee being a core strength (removed — the JL argument is mathematically incorrect, so this is not a valid strength).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the theoretical analysis.** Replace the JL lemma argument with a direct variance calculation. The convergence rate should be derived from Lemma 1's variance expression. This will yield an honest scaling relationship between $m$, $d$, and $K$ that the experiments may or may not support.
2. **Quantify $L_v(\mathbf{x})$ in Lemma 2** for the specific models tested, or replace it with a more concrete privacy analysis.
3. **Move the $m$ ablation to the main text** as it directly addresses the paper's central empirical claim.

## Score and Decision

**Bracketing (Round 1):** I queried three bands of ICLR-calibration papers on similar topics (federated learning compression, random projection, privacy). Low-band anchors (< 3.5, avg scores 1.67–3.00) included papers with flawed theory or narrow scope (e.g., "Compressed Decentralized Learning with Error-Feedback under Data Heterogeneity" at 1.67; "FedComLoc" at 3.00). Middle-band anchors (3.5–7.5, avg scores 4.50–5.83) included papers with sound but incomplete theory or limited experiments (e.g., "Sketched Adaptive Federated Deep Learning" at 4.50; "Collaborative Compressors" at 5.25). High-band anchors (> 7.5, avg scores 7.60–8.00) were clearly accept-quality papers with strong, validated contributions.

**Initial bracket:** I placed this paper between 2.0 and 4.0 — the fatal JL error rules out the middle-to-high range, but the empirical results and Lemma 1 lift it above the worst-scoring papers.

**Narrowing (Round 2):** I further queried papers scoring 1.0–4.0 and 2.0–5.0. The 1.67 anchor ("Compressed Decentralized Learning") had a restricted convergence guarantee that limited its applicability without being a clear mathematical error — reviewers gave 1, 1, 3. The 3.0 anchor ("Vanishing Privacy: Fast Gradient Leakage") was an attack paper with clear empirical contributions but mixed reviews (5, 3, 1, 3). The 4.50 anchor ("Sketched Adaptive FL") had solid logarithmic-convergence theory with assumption concerns — scores 3, 6, 3, 6.

**Comparison:** Our paper has a *verifiable mathematical error* in its central theorem (not just a restrictive assumption or narrow scope, but a provably incorrect claim). This is more damaging than the limitations in any of the anchor papers. However, Lemma 1 is correct, and the empirical results in Tables 1–2 are stronger and cleaner than the 1.67–3.00 anchors. Balancing these factors, the paper sits below a 3.67 (where "Sketched Adaptive FL" sits with flawed-but-not-fatal theory) but above a 1.67 (where papers have multiple systemic issues).

**Final score: 3.0.** This reflects the reality that:
- The paper has a fatal, verifiable mathematical error that invalidates its main theoretical claim
- It has one clean theoretical result (Lemma 1) and genuinely interesting empirical results  
- These salvageable parts are not enough for the paper to be accepted at ICLR as-is

**Decision: Reject.** The paper cannot be accepted with an invalidated central theorem. The authors should correct the convergence analysis (deriving it from the correct variance, not the JL lemma) and resubmit.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>