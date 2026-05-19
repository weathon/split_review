- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 8, 5, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes Learned Proximal Networks (LPNs), a class of neural networks that *exactly* implement proximal operators of (potentially nonconvex) regularizers, by parameterizing them as gradients of input-convex neural networks (ICNNs). It introduces a *proximal matching* loss that provably recovers the MAP denoiser (i.e., the proximal of the log-prior) in the limit \(\gamma\to0\) using only i.i.d. clean samples. The trained LPN can be plugged into iterative solvers (ADMM, PGD) with convergence guarantees under minimal and actionable assumptions, and the implicitly learned regularizer can be recovered via convex optimization. Experiments on synthetic data, MNIST, CelebA deblurring, and Mayo-CT (tomography and compressed sensing) demonstrate competitive performance while enabling explicit characterization of the learned prior.

## Strengths

1. **Exact proximal parameterization via ICNN gradients (Proposition 1)**. The paper provides a formal construction guaranteeing that \(f_\theta = \nabla\psi_\theta\) is exactly a proximal operator of some function \(R_\theta\). This is a stronger theoretical guarantee than prior PnP methods, which only approximate proximal behavior, and it is the foundation for all downstream convergence and interpretability claims.

2. **Proximal matching loss with recovery guarantee (Theorem 1)**. Theorem 1 proves that minimizing \(\mathcal{L}_{PM}\) yields the MAP denoiser \(\prox_{-\sigma^2\log p_x}\) in the limit \(\gamma\searrow 0\), using only i.i.d. samples from \(p_x\). The Laplacian experiment (Figure 1) verifies this empirically: \(\ell_2\) and \(\ell_1\) losses recover the posterior mean and median (not the prox of the log-prior), while proximal matching recovers the correct soft-thresholding function.

3. **Convergence guarantees for PnP without restrictive denoiser assumptions (Theorem 2)**. Because LPNs are provably proximal operators, PnP-ADMM with a trained LPN converges to a fixed point under assumptions that are all actionable (\(\rho > \|A^\top A\|\), softplus activations, \(0<\alpha<1\)). This contrasts with prior PnP convergence results that require contractivity, nonexpansivity, or Lipschitz constraints that are hard to verify or enforce.

4. **Recovery and explicit evaluation of the learned regularizer (Section 3.2)**. The paper provides a tractable method (convex optimization, Eq. 8) to invert the LPN and evaluate \(R_\theta\) at arbitrary points. This enables explicit characterization of the data-driven prior — demonstrated on MNIST (Figure 2) — which is impossible with black-box denoisers.

5. **Competitive performance on challenging inverse problems with added interpretability**. On CelebA deblurring (Table 1), LPN matches or closely approaches the best PnP baselines. On Mayo-CT tomography and compressed sensing (Table 2), LPN substantially outperforms the AR baseline and is competitive with task-specific UAR, while providing interpretability that neither offers.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Ambiguous convergence notion in Theorem 2.** The theorem states that the iterate sequence "converges to a limit point... which is a fixed point of the PnP-ADMM iteration." The phrasing is ambiguous between full sequence convergence (a strong claim) and subsequential convergence (every cluster point is a fixed point, the typical result under nonconvex ADMM analyses such as Themelis et al. 2020, which the paper cites). Since the proof is relegated to the appendix, the main text should disambiguate this. The paper's key selling point — that LPNs enable convergence guarantees "absent any additional assumptions" — is not invalidated by this ambiguity, but the claim should be precisely stated.

2. **Unclear whether the AR baseline on Mayo-CT was retrained or numbers are imported.** The paper reports large margins over AR (e.g., 38.03 dB vs. 29.71 dB for compressed sensing at 1/16 rate). The text states "Following Lunz et al., we simulate CT sinograms using a parallel-beam geometry with 200 angles and 400 detectors," which describes the forward measurement setup but does not clarify whether the AR model was retrained on the same Mayo-CT data or whether numbers are taken from the original publication (which evaluated on different datasets and configurations). The authors should specify this; if AR results are from a different dataset/task configuration, the comparison is invalid.

3. **Gap between asymptotic theory (\(\gamma\to 0\)) and finite-\(\gamma\) practice.** Theorem 1 is asymptotic (\(\gamma\searrow 0\)), while training uses a finite annealing schedule. The paper does not analyze the approximation error for finite \(\gamma\) or provide principled guidance on the schedule. The Laplacian experiment provides some empirical validation for specific \(\gamma\) values, but a systematic study connecting the theory to practice (e.g., how the learned prior degrades as \(\gamma\) increases) would strengthen the evidence.

4. **Slight overstatement of CelebA results.** The text claims LPN "achieves state-of-the-art result across multiple blur degrees, noise levels and metrics considered." In Table 1, PnP-GS strictly outperforms LPN on PSNR in 2 of 4 settings (\(\sigma_{blur}=1,\sigma_{noise}=0.04\): 31.4 vs. 31.3; \(\sigma_{blur}=2,\sigma_{noise}=0.04\): 29.3 vs. 29.1). LPN ties PnP-GS in the other two settings. The results are competitive and the paper's contribution is not primarily about beating every baseline, so the claim should be tempered to reflect that LPN is at or near state-of-the-art.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment varying the final \(\gamma\) value to quantify its effect on the learned prior (for the Laplacian case) or reconstruction quality (for image tasks) would directly connect the asymptotic theory to practice.
- A discussion of limitations (e.g., computational cost of inverting \(f_\theta\) via convex optimization, potential expressivity limitations of softplus vs. ReLU, finite-\(\gamma\) bias) would strengthen the paper's self-assessment.
- Quantifying the recovered MNIST prior against a nonparametric estimate of the true log-density (if feasible) would make the interpretability claim more concrete.
- Reporting wall-clock training/inference times would be useful for practitioners.

## Removed Points

- **"Missing semicolon in Eq. 8":** This is a PDF-parser formatting artifact; the actual submission does not have this issue.
- **"Wrapfigure layout issues":** Pure formatting nitpick with no substantive content.
- **"Proof in appendix not available to me":** The appendix is legitimately deferred; this is not an author error and the critic acknowledged this limitation. The retained point above (ambiguity in the main text) is the substantive concern.

## Novel Insights

None beyond the paper's own contributions. The key synthesis emerging from the reviews is that the paper's three-part contribution (proximal-guaranteed parameterization, provably correct training loss, convergence guarantees with minimal assumptions) is unusually principled for the PnP literature. The remaining concerns are about clarity and documentation, not about the soundness of the core ideas.

## Suggestions

1. **Clarify Theorem 2.** Replace "converges to a limit point" with precise language: either "the sequence has a convergent subsequence whose limit is a fixed point" (subsequential convergence) or "the sequence converges to a fixed point" (full convergence), and state which reference/lemma provides that conclusion.
2. **Specify AR baseline sources in Table 2.** Add a footnote or sentence stating whether AR was retrained on Mayo-CT data and, if so, with what hyperparameters. If numbers are from the original publication, flag the comparison as cross-dataset.
3. **Add a finite-\(\gamma\) ablation.** Show the effect of the final \(\gamma\) value on the learned proximal operator / regularizer for the Laplacian case (extending Figure 1).
4. **Temper the "state-of-the-art" claim in Section 5.** Replace with "competitive with state-of-the-art" or "at or near state-of-the-art."
