Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper extends the theory of benign overfitting from in-distribution to out-of-distribution (OOD) settings under covariate shift for over-parameterized linear models. The core contribution is Theorem 2, which provides an instance-dependent, multiplicative excess risk bound for ridge regression that decomposes OOD error into interpretable factors governing shift in major and minor covariance directions. The paper further provides a lower bound (Theorem 4) showing ridge regression can be fundamentally limited under large minor-direction shift, and argues that Principal Component Regression (PCR) achieves the fast rate in such regimes.

## Strengths

- **First vanishing non-asymptotic bound for OOD benign overfitting in ridge regression (Theorem 2).** The multiplicative decomposition of the excess risk into factors capturing major-direction shift (\(\mathcal{T}\)) and minor-direction shift (\(\mathcal{U}, \mathcal{V}\)) is clean and interpretable. Prior work (Tripuraneni et al., 2021; Hao et al., 2024; Mallinar et al., 2024) either obtained non-vanishing constants or imposed restrictive alignment conditions between source and target covariances.

- **Identification of key quantities governing OOD generalization.** Theorem 2 isolates four quantities — \(\|\mathcal{T}\|\), \(\mathrm{tr}[\mathcal{T}]/k\), \(\mathrm{tr}[\mathcal{U}]/\mathrm{tr}[\mathcal{V}]\), and \(n r_k^{-1}\|\Sigma_{T,-k}\|/\|\Sigma_{S,-k}\|\) — that multiplicatively control the OOD excess risk. This framework provides actionable conditions for when benign overfitting survives distribution shift.

- **Target distribution requires only magnitude control, not spectral alignment.** A novel and practically important insight: the target minor components need only have bounded overall magnitude relative to the source (e.g., \(\mathrm{tr}[\mathcal{U}]/\mathrm{tr}[\mathcal{V}] = O(1)\)), with no constraints on their internal eigenvalue ordering. This is strictly weaker than prior work requiring eigenvalue-wise alignment (Mallinar et al., 2024).

- **Lower bound demonstrating ridge regression's fundamental limitation (Theorem 4).** For a concrete instance with \(\Sigma_T = I_d\) and \(\sqrt{n}\) minor eigenvalues at \(C/\sqrt{n}\) scale, ridge regression is lower bounded by \(\Omega(1/\sqrt{n})\) regardless of \(\lambda\) — proving the deterioration is inherent, not an artifact of loose upper bounds.

- **Empirical validation matches theoretical predictions.** Figure 1(a,b) confirms \(\mathcal{O}(1/n)\) rates for minimum-norm interpolation under controlled covariate shifts; Figure 1(c) confirms the \(\mathcal{O}(1/\sqrt{n})\) slow rate for ridge and \(\mathcal{O}(1/n)\) fast rate for PCR under the Theorem 4 instance.

- **Sample complexity analysis reflects degree of covariate shift (Remark 2).** Required sample size ranges from \(\Omega(k)\) to \(\tilde{\Omega}(k^3)\) depending on shift severity in major directions, paralleling and extending the under-parameterized analysis of Ge et al. (2024).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **"Sharpness" claim is imprecise.** The abstract and introduction state "Our result is sharp," but the paper does not provide a general matching lower bound for Theorem 2. The conclusion (Section 5) candidly acknowledges: "a key challenge remains in deriving a general lower bound that matches our upper bounds." The paper demonstrates sharpness only in the sense of recovering known sharp bounds as special cases (Tsigler & Bartlett, 2023; Ge et al., 2024). The language should be qualified — e.g., "recovers known sharp bounds in special cases" — to avoid overclaiming. This does not undermine the mathematical content of Theorem 2 but creates an expectation the paper does not fulfill.

### Trivial

- **Operator norm vs. "overall magnitude" in the bias bound.** The bias factor in Theorem 2 uses \(\|\Sigma_{T,-k}\|\) (operator norm), while the surrounding discussion (Section 3.2, point 2) speaks of "overall magnitude" of the target minor components. The variance factor uses \(\mathrm{tr}[\mathcal{U}]/\mathrm{tr}[\mathcal{V}]\) which relates to Frobenius norms (as the paper notes, \(\leq \|\Sigma_{T,-k}\|_F / \|\Sigma_{S,-k}\|_F\)). The bias condition via operator norm is stricter than a trace-based notion would be: a single large eigenvalue in \(\Sigma_{T,-k}\) would inflate the operator norm while leaving the trace relatively small. The narrative could be sharpened to distinguish these two measures. This is a presentation nuance that does not affect correctness.

## Nice-to-Haves

- **Simulations use diagonal target covariances.** The experiments in Appendix A.1 use \(\Sigma_T = \mathrm{diag}(\Sigma_{T,k}, \Sigma_{T,-k})\) with randomly generated but diagonal blocks. The theory does not require diagonal \(\Sigma_{T,-k}\) — the claims about "only overall magnitude matters" would be more convincingly illustrated with a non-diagonal (rotated) target covariance.

- **Varying effective rank \(r_k, R_k\) in simulations.** The experiments fix the source covariance structure; systematically varying \(r_k\) and \(R_k\) while controlling OOD factors would further test the predictive power of Theorem 2.

- **The PCR guarantee (Theorem 5) is referenced but its formal statement is not visible in the provided manuscript text.** Section 4.2 contains only a brief conceptual motivation before jumping to the conclusion. Presumably the theorem statement and proof reside in the full appendix, but having the theorem statement in the main body — even without full proof — would substantially strengthen the readability of Section 4.2.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing Theorem 5 — PCR guarantee is unsubstantiated" (Harsh Critic).** The paper references Theorem 5 in the abstract and contributions; Section 4.2 exists and motivates the PCR result. The formal theorem statement and proof are stripped by the parser along with appendix material. Per review guidelines, missing appendix/proof content is a parser artifact and does not reflect an author error.

- **"In-distribution recovery is not exact — bound does not match Tsigler & Bartlett (2023)" (Harsh Critic).** When specializing to \(\Sigma_S = \Sigma_T\), the bias bound becomes \(B/c \leq B_{\mathrm{ID}} \cdot (1 + n/r_k)\). The paper explicitly states the condition \(n < r_k\) (line 154 of Theorem 2, and line 162 in discussion), which implies \(n/r_k < 1\), making the factor at most 2 — absorbable into the constant \(c\). The paper does address this, so the criticism misunderstands the paper's stated conditions.

- **"Simulation uses diagonal target covariance matrices — a limitation."** Moved to Nice-to-Haves. The theory covers non-diagonal cases; the simulation limitation is minor.

- **"Effect of varying effective rank not tested."** Moved to Nice-to-Haves as a suggestion for strengthening empirical evidence.

- **Strength Finder: "PCR achieves fast rate O(1/n) where ridge fails (Theorem 5)."** Removed because Theorem 5's formal statement is not present in the provided manuscript text and cannot be independently verified. The empirical validation (Figure 1c) does support the claim directionally.

- **Strength Finder: "Sharpness: recovery of prior in-distribution and under-parameterized OOD results."** Partially retained — the recovery of special cases is genuine. But the claim of general sharpness is overstated (see Minor Weakness above).

## Novel Insights

The paper's most conceptually interesting observation is the asymmetry between source and target requirements for benign overfitting: the source needs high effective rank in minor directions (to dampen noise via implicit regularization), but the target needs only bounded overall magnitude in those same directions — its internal spectral structure is irrelevant. This decoupling is not obvious a priori and has practical implications for assessing OOD robustness: one can check target suitability by measuring aggregate quantities like \(\mathrm{tr}[\mathcal{U}]/\mathrm{tr}[\mathcal{V}]\) rather than requiring detailed spectral alignment.

## Suggestions

- Qualify the "sharpness" language throughout the paper. Replace "Our result is sharp" with "Our result recovers known sharp bounds as special cases" or "Our bound is tight in the sense that it reduces to existing sharp bounds when specialized to in-distribution or under-parameterized settings."
- Bring the statement of Theorem 5 (even without full proof) into the main body of Section 4.2 so the section is self-contained.
- In the discussion around the bias bound, clarify the distinction between operator norm and trace/Frobenius norm for the minor-direction shift factor.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Score | Comparison |
|--------|-------|------------|
| `eoTCKKOgIs.md` — Ge et al. (2024), "MLE is All You Need for Well-Specified Covariate Shift" | 6.25 (Accept) | Strong theoretical paper on covariate shift with matching upper/lower bounds. Our paper builds on this work but addresses the over-parameterized regime. Slightly less complete due to imprecise sharpness claim and the PCR theorem being appendix-deferred. |
| `AnuHbhwv9Q.md` — "Out of the Ordinary: Spectrally Adapting Regression for Covariate Shift" | 6.25 (Reject, but scores 6,6,5,8) | Another OOD regression paper with spectral analysis. Comparable rigor; our paper is more theoretical while that one is more applied. |
| `AcoXPIPh4A.md` — "Risk Bounds of Accelerated SGD for Overparameterized Linear Regression" | 6.00 (Accept) | Instance-dependent risk bounds for overparameterized linear regression. Similar contribution level and theoretical depth. |
| `5T46w5X3Go.md` — "Theoretical Analysis on the Generalization Power of Overfitted Transfer Learning" | 4.75 (Reject) | Similar topic (transfer/benign overfitting in linear models) but more restrictive model and limited insights. Our paper is clearly stronger. |
| `uVDwunWsLz.md` — "Benign Overfitting in Single-Head Attention" | 5.25 (Reject) | Benign overfitting analysis with novelty concerns. Our paper has a clearer, more novel contribution. |
| `x8jxf3byli.md` — "Two Stages Domain Invariant Representation Learners..." | 2.80 (Reject) | Poor quality, irrelevant. Our paper is far stronger. |

The paper under review extends benign overfitting theory to OOD in a rigorous, well-structured way. Theorem 2 is a genuine contribution that advances the state of the art. The paper's weaknesses are limited to imprecise language about sharpness and some presentation nuances — none threaten the core claims. Compared to anchors, it sits comfortably at the 6.0 level: above the 4.75–5.25 range of papers with limited novelty, comparable to the 6.0 benchmark of instance-dependent bounds for overparameterized models, and slightly below the 6.25 benchmark of a fully complete (matching upper/lower bound) covariate shift theory paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>