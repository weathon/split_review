Now I have thoroughly verified all claims against the paper. Let me compose the final consolidated review.

---

## Summary

This paper establishes a Neural Network–Gaussian Process (NNGP) correspondence for Neural ODEs, covering both the standard autonomous (shared-weight) and non-autonomous (independent-weight) cases. The central idea is to approximate the Neural ODE with a finite-depth ResNet, prove the ResNet converges to a Gaussian process at large width, and then use a double-limit argument (depth and width) to extend the result to the infinite-depth (ODE) limit. The paper additionally proves strict positive definiteness of the limiting kernel for non-polynomial activations and provides a dynamic programming algorithm for computing the covariance matrix.

## Strengths

1. **First NNGP analysis for Neural ODEs with shared weights.** The paper tackles a significant theoretical gap: extending NNGP theory to the practically important autonomous (shared-weight) ODE setting, which has resisted prior SDE-based approaches that require independent weights across layers. The problem is timely and well-motivated.

2. **Rigorous distinction from prior physics-based MFT analyses.** Section 2 clearly separates the paper's fixed-\(T\), nonzero-diagonal-weight setting from the dynamical mean-field theory literature (Sompolinsky et al., Engelken & Goedeke) that studies \(T\to\infty\) dynamics with zero-diagonal weights. This correctly situates the contribution as complementary and relevant to practical Neural ODE training.

3. **Strict positive definiteness of the limiting NNGP kernel (Theorem 4.8).** The paper proves that even under the nontrivial shared-weights ODE limit, the limiting kernel \(\Sigma^*\) is strictly positive definite for non-polynomial activations — a property essential for global convergence guarantees and generalization bounds. The proof leverages stationarity on the sphere (Lemma 4.2) and Hermitian expansions of the dual activation.

4. **Experimental validation that supports the theoretical claims.** Figures 1–3 provide empirical evidence for Gaussian behavior of wide Neural ODEs, convergence of empirical covariances with depth and width, positivity of smallest eigenvalues, and the practical utility of the NNGP kernel for Bayesian inference on MNIST. The experiments directly compare shared-weight, independent-weight, and Neural ODE cases, confirming distinct behaviors predicted by the theory.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient justification of distributional convergence for the ODE limit (Theorem 4.5).** The paper's argument proceeds by: (i) showing the finite-depth ResNet \(f_\theta^L\) converges to a GP for each fixed \(L\) (Theorem 4.2); (ii) showing the double limit of the **empirical covariance** \(\hat\Sigma_n^L\) commutes (Lemma 4.1); and then (iii) asserting the Neural ODE converges to a GP with kernel \(\Sigma^* = \lim \Sigma^\ell\). The leap from (ii) to (iii) is not adequately justified in the main text. Lemma 4.1 concerns a scalar quantity (the empirical covariance of hidden features), not the distribution of the network output. To conclude that the output of the ODE is a GP, one must argue that the finite-dimensional distributions converge to Gaussian with covariances determined by \(\Sigma^*\), and that the GP structure is preserved when taking \(L\to\infty\). The paper mentions that "the convergence of depth is uniform in width" as a key insight, but this uniformity is established for the empirical covariance, not for the distributional convergence. Additional arguments (e.g., tightness of the sequence of processes, convergence of characteristic functions, or an appropriate Moore–Osgood argument applied at the distributional level) would be needed to close this gap. As the central claim of the paper (Theorem 4.5) rests on this reasoning, the authors should provide a clearer proof sketch or reference to a detailed argument in the appendix.

2. **Inadequate justification for applying the Tensor Program to shared-weights ResNets (Theorem 4.2, shared case).** The paper invokes Yang (2019)'s Tensor Program framework and says "With similar arguments, we establish that the ResNet \(f_\theta^L\) converges to a Gaussian process," covering both the independent-weights and shared-weights cases. However, Yang's master theorem in its basic form assumes weight independence across layers. Extending it to the setting where \(W^\ell = W\) for all \(\ell\) — so that the G-vars \(g^\ell(x) = W\phi(h^{\ell-1}(x))\) at different layers are linear functions of the **same random matrix** — is nontrivial because the pre-activations become correlated across layers through the shared weight, violating standard independence assumptions. While Yang (2019) does cover some forms of weight tying (e.g., recurrent networks), the paper does not explain how this extends to the ResNet architecture with skip connections and shared weights. The recursive covariance formulas in Theorem 4.2(i) suggest the authors understand the correct limiting structure, but the justification that the Tensor Program guarantees Gaussianity in this correlated setting needs to be spelled out.

### Minor

1. **Algorithm 1 is unclear and uses undefined notation.** The pseudocode uses \(V_\phi\) without definition — this likely refers to the dual activation (a standard object in NNGP theory), but it is never defined in the main text. The loop indexing is unconventional (e.g., \(\bigcup_{\mathbf{\theta}}\)), and the pseudocode as written is not reproducible. The surrounding mathematical description (Eq. 19) is clearer but still relies on \(V_\phi\) without definition. This does not affect the theory but undermines a claimed contribution (the DP algorithm).

### Trivial
None.

## Nice-to-Haves

- A brief discussion or explicit verification that the limit \(\lim_{\ell\to\infty} \Sigma^\ell\) exists (which follows implicitly from Lemma 4.1 plus the convergence of \(\hat\Sigma_n^L\) to \(\Sigma^{L+1}\)) would clarify the logical flow and preempt reader confusion.
- Derivation or explanation of the integral expression in Proposition 4.6(ii) (Eq. 16) would improve readability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Convergence of the deterministic kernel sequence \(\Sigma^\ell\) is not addressed."** — This is factually incorrect. The existence of \(\lim \Sigma^\ell\) follows from Lemma 4.1 (which establishes the double limit of the empirical covariance) combined with the standard result that \(\lim_{n\to\infty} \hat\Sigma_n^L = \Sigma^{L+1}\) (convergence of the empirical covariance to the NNGP kernel for each fixed depth). Specifically, \(\lim_{L\to\infty} \Sigma^{L+1} = \lim_{L\to\infty} (\lim_{n\to\infty} \hat\Sigma_n^L) = \Sigma^*\) by Lemma 4.1. The critic overlooked this connection.
- **"Proposition 4.1's bound depends on random matrices through A and B."** — A and B are deterministic constants composed of hyperparameters (\(\sigma_v, \sigma_w, \sigma_u\)) and the input norm \(\|x\|\). The critic misread the notation.
- **"z^ℓ and u^ℓ are introduced without explicit definition as Gaussian variables."** — Theorem 4.2 explicitly states "(z^ℓ(x), z^k(x')) are centered Gaussian random variables" and defines u^ℓ as a linear combination of these variables.
- **Criticisms about missing appendix, formatting/style, and similar artificial parser artifacts.** — These are not present in the original submission.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface additional novel insights. The tension between the paper's ambitious theoretical claims and the gaps in the main-text justification is a structural observation about presentation, not a new research finding.

## Suggestions

1. **Provide a self-contained proof sketch for Theorem 4.5** that explicitly addresses the three steps: (a) distributional convergence of the finite-depth approximation to a GP, (b) closeness of the ODE and its finite-depth approximation in a sense that preserves weak convergence, and (c) convergence of the resulting GP sequence to a limiting GP with kernel \(\Sigma^*\). Clarify what additional properties (e.g., uniform tightness) are needed and how Lemma 4.1 supports them.

2. **Explain how the Tensor Program handles the shared-weights case.** Provide a brief justification or reference showing that the G-vars \(g^\ell(x) = W\phi(h^{\ell-1}(x))\) still satisfy the conditions of the Tensor Program master theorem despite weight sharing. A note on how this differs from or extends Yang (2019)'s treatment of recurrent networks would suffice.

3. **Clean up Algorithm 1:** define \(V_\phi\) (the dual activation function), use standard pseudocode notation, and ensure the recurrence is self-contained.

## Score and Decision

This paper addresses a significant and timely problem. The strengths — first NNGP correspondence for Neural ODEs, strict positive definiteness of the limiting kernel, clear experimental validation, and proper contextualization against prior physics-based work — are real and valuable. However, the main text leaves two significant gaps in the justification of its core theoretical claims: the link between the empirical covariance double-limit and distributional convergence of the ODE output (Theorem 4.5) is not adequately explained, and the application of the Tensor Program framework to the shared-weights ResNet is asserted without sufficient justification. These gaps affect the paper's central contribution and prevent acceptance in the current form. The work is promising and the gaps are addressable, but the theoretical presentation needs substantial strengthening.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>