Now I have a thorough understanding of the paper and can verify reviewer claims against it. Let me produce the consolidated review.

## Summary

This paper studies whether a batch-normalized MLP can simultaneously maintain good forward signal propagation (avoid rank collapse) and avoid gradient explosion in depth. For an MLP with **orthogonal random weights**, a simplified batch normalization operator (row-wise L2 normalization without mean subtraction), and **linear activations**, the paper proves two non-asymptotic results: (1) the isometry gap (a measure of how far representations are from orthogonal) decays exponentially in depth; (2) the expected log-gradient-norm for each layer is bounded by a depth-independent constant (O(d⁵)). The technical machinery uses Weingarten calculus to obtain finite-width bounds, going beyond prior mean-field analyses. An empirical activation-shaping scheme is proposed to extend these properties to certain non-linear activations (tanh, sin), and training experiments on CIFAR-10 show depth-independent convergence.

## Strengths

1. **First non-asymptotic proof of bounded gradients in a BN network.** Theorem 2 (Theorem 3.2 in the paper) provides an explicit bound on the expected log-gradient norm that depends only on width (O(d⁵)) but **not on depth**, directly contradicting prior work (Yang et al., 2019, Theorem 3.9) that concluded gradient explosion in BN networks is unavoidable. This is a qualitative departure from the established mean-field theory.

2. **Non-asymptotic exponential decay of the isometry gap in depth.** Theorem 1 proves that ϕ decays as exp(−ℓ / (C d²(1+d ϕ(X₀)))), which is stronger than the O(width^{−1/2}) ball guaranteed by Daneshmand et al. (2021). The result is rigorous for finite width and does not rely on uncontrolled asymptotic assumptions.

3. **Rigorous link between orthogonalization and gradient norm of BN layers.** The proof of Theorem 2 explicitly bounds the log-Jacobian of the BN operator by the isometry gap, then uses the exponential decay of ϕ to show the sum over depths is geometrically bounded. This mechanistic explanation — that the very same orthogonalization that enables good signal propagation also prevents gradient explosion — is conceptually new.

4. **Honest scoping of limitations.** The paper explicitly states that the theory applies to a simplified BN variant (no mean reduction), requires n = d, and uses linear activations. The title includes "Towards" and the abstract is careful to describe "a particular construction." This transparency is a strength, not a weakness.

5. **Empirical demonstration of depth-independent training.** Figure 2 shows that training accuracy of 100-layer MLPs with orthogonal weights, BN, and shaped activations remains stable across depths with vanilla SGD, confirming that the theoretical properties translate to practice.

## Weaknesses

### Major

1. **The n = d restriction (batch size must equal width) is a significant architectural constraint that limits practical applicability.** The paper states this as a requirement (line 71) but does not discuss whether or how the theory might extend to rectangular settings (n ≠ d). Since batch size and width are independent hyperparameters in practice, forcing them equal is a genuine restriction. The non-degenerate assumption becomes impossible when n > d (rank at most d), and for n < d the batch is rank-deficient by dimension, so the bound becomes vacuous. A paragraph discussing possible extensions (e.g., padding, thin QR, or why the square case captures the essential regime) would substantially strengthen the paper.

2. **The simplified BN operator omits mean reduction, and the theory does not cover standard BN.** The paper defines BN(X) = diag(XXᵀ)^(−1/2) X (line 66), leaving out the mean-centering step that is a core component of standard batch normalization. The authors acknowledge this (line 69) and reference an experimental figure (Fig. mean_reduction) showing the results hold with standard BN, but that figure is in the appendix (which is stripped by the parser). More importantly, the theoretical analysis — the isometry gap as a Lyapunov function, the eigenvalue bounds in (0,1], the Weingarten calculus calculations — all rely on the specific form diag(XXᵀ)^(−1/2) X. With mean subtraction, XXᵀ becomes a covariance matrix rather than a Gram matrix, and it is not obvious that the same analysis applies. The paper would benefit from either a theoretical discussion of why mean subtraction does not fundamentally change the dynamics, or an explicit statement that the theory covers a BN *variant* (not standard BN) and the title/abstract should be adjusted accordingly.

### Minor

3. **The gradient bound is on the expected log-norm, not on the norm itself.** Theorem 2 bounds E[log ||∇||] ≤ O(d⁵). The paper correctly interprets this as "bits of precision needed" (line 192), and the bound being depth-independent is the substantive result. However, some prose phrases like "gradients remain bounded by a constant" (Figure 3 caption, line 188) could be read as a bound on E[||∇||] rather than E[log ||∇||]. These are different statements — the log-norm bound does not rule out heavy-tailed gradient distributions with occasional large values, though in practice this is a minor concern given the exponential decay mechanism. The d⁵ dependence is large (10¹⁰ for width 100), but the key point is depth-independence. The paper should tighten the prose to consistently say "bounded log-gradient norm."

4. **The activation shaping extension is entirely empirical, and the paper does not claim otherwise.** The paper is transparent that the theory covers only the linear-activation case (line 37) and describes the non-linear extension as experimental. This is a limitation of scope, not a flaw. However, the framing in Section 5 ("Activation shaping **based on the theoretical analysis**") could suggest a tighter theoretical connection than actually exists. The shaping strategy amounts to tuning per-layer gains so that the empirical slope of log-gradient-norm vs. depth decays fast enough — a heuristic motivated by, but not proven by, the theory. A clearer separation between theory and experiment (e.g., a subsection titled "Extension to non-linear activations (empirical)") would sharpen the exposition.

### Trivial

5. **The implicit orthogonality bias observation (Figure 7) is interesting but not explained.** The paper notes that middle layers remain near-orthogonal during training despite non-negligible gradients, and calls this a "striking empirical observation." This is a genuine finding but the paper offers no mechanism. This is fine for an observation, but the claim that this is a "strength" of the paper's contribution is overblown — it is a suggestion for future work.

## Nice-to-Haves

- Include a heuristic discussion of the n ≠ d case — e.g., whether thin QR or padding could extend the results, or why the square case is already informative.
- Show gradient behavior on at least one additional dataset (e.g., Fashion-MNIST) and for a range of widths to strengthen the empirical evidence.
- Visualize the mean-reduction experiment (Fig. mean_reduction) in the main text rather than only in the appendix, since it directly addresses the most significant theoretical simplification.

## Removed Points

The following points from the harsh critic have been removed or downgraded per the filtering rules:

- **"No such experiments are shown in the main text [for mean reduction]"** — The paper references Figure~\ref{fig:mean_reduction} in the appendix. The appendix is stripped by the parser, not missing from the original submission. **Removed.**

- **"Missing appendix / proofs of Lemma 2"** — The parser strips appendices from all papers. These exist in the original submission. **Removed per hard rules.**

- **"Lipschitz assumption not verified"** — The paper refers to Lemma~\ref{lem:lipschitz} in the appendix (stripped). **Removed.**

- **"Empirical validation is limited to MLPs on CIFAR10"** — The paper is primarily a theoretical contribution; the experiments are demonstrative. Asking for more datasets is scope creep for a theory paper. **Removed.**

- **"Non-linear activation extension lacks theoretical grounding"** — The paper explicitly states this is empirical (line 37: "The limitation of our theory is that it holds for... linear activations"). The criticism conflates a clearly stated limitation with a weakness. **Downgraded to Minor and reframed as a presentation suggestion.**

- **"Proof of Lemma 2 is missing"** — See above; appendix is stripped. **Removed.**

## Novel Insights

The key insight that emerges from this paper and the reviews is that **the very property that makes BN good for signal propagation (orthogonalization) can, under the right weight initialization (orthogonal), also prevent gradient explosion.** Prior work had concluded that these two properties are in tension — that the orthogonalization that avoids rank collapse necessarily causes exploding gradients. The paper shows this tension is not fundamental; it arises specifically under Gaussian initialization. By using orthogonal weights, the Jacobian of the linear layers is isometric (eigenvalues = 1), so the only gradient amplification comes from the BN layers, and this amplification can be controlled because the isometry gap (which bounds it) decays exponentially. This reframes the problem: the culprit was never BN per se, but the interaction of BN with unconstrained spectra from Gaussian weights.

## Suggestions

1. Add a paragraph in Section 3 explicitly discussing the n = d restriction and possible ways to relax it (or why it is the natural regime for this analysis).
2. Tighten prose throughout to consistently say "bounded log-gradient norm" rather than "bounded gradients" when discussing the Theorem 2 bound.
3. Move the mean-reduction experiment (Fig. mean_reduction) into the main text or, at minimum, add a sentence summarizing its findings.
4. In Section 5, add a subsection header like "Extension to non-linear activations (empirical)" to visually separate the heuristic exploration from the theory.
5. Add a brief comment on why the d⁵ constant, while large, is still meaningful: it shows depth-independence, and for any fixed width the bound is a finite constant.

## Score and Decision

**Originality:** 7/10 — Novel combination of orthogonal initialization + Weingarten calculus for BN networks; the insight that orthogonal weights resolve the tension between signal propagation and gradient explosion is genuinely new.

**Importance of research question:** 8/10 — Resolving whether BN can avoid gradient explosion is a central theoretical question in deep learning.

**Claims well-supported:** 6/10 — The theoretical claims (Theorems 1, 2) are well-supported within their stated assumptions. However, the gap between the simplified setting (no mean reduction, n=d, linear activations) and the full BN setting is significant enough that the title/abstract slightly overreach.

**Soundness of experiments:** 7/10 — The experiments are clean and validate the theory, but are limited in scope (one dataset, one width). They serve their purpose as proof-of-concept but do not constitute a thorough empirical study.

**Clarity of writing:** 7/10 — The paper is generally well-written and transparent about limitations. The proof sketches are clear. Some prose overclaims slightly.

**Value to the research community:** 7/10 — The theoretical machinery (isometry gap as Lyapunov function for BN, Weingarten calculus bounds) is likely to be reused in future analyses of normalization layers. The paper opens a new direction (orthogonal weights + BN) for further study.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>