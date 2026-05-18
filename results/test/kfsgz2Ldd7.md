Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes Reverse Mean Propagation (RMP), a framework for solving inverse problems using diffusion models that targets the posterior mean directly rather than generating posterior samples. The authors prove (Proposition 2) that reverse conditional distributions are Gaussian in the continuous limit with tractable mean/covariance involving the posterior mean, and show (Theorem 1) that propagating the mean through the reverse chain converges to the posterior mean. They implement RMP via a variational inference approach using natural gradient descent with score function approximations, and demonstrate strong empirical results on FFHQ image reconstruction tasks with improved computational efficiency.

## Strengths

1. **Novel problem framing and theoretical foundation** — The idea of targeting the posterior mean directly via reverse mean propagation (rather than generating posterior samples) is a meaningful contribution to diffusion-based inverse problems. Proposition 2 and Theorem 1 provide a principled theoretical framework connecting the reverse diffusion chain to the posterior mean, and the Gaussian mixture toy experiment (Figures 1–2) validates that the chain indeed converges to the true MMSE estimate.

2. **Strong empirical results across diverse tasks** — Tables 1 and 2 show that VE/VP-RMP achieves the best or second-best scores on nearly all metrics across 5 linear and 2 nonlinear inverse problems on FFHQ. The gains are substantial; e.g., VP-RMP achieves FID 22.41 on random inpainting vs. 57.74 for DPS, and LPIPS 0.0771 vs. 0.1887.

3. **Computational efficiency** — Figure 6 demonstrates that VP-RMP with only 50 NFEs achieves higher PSNR than DPS with 1000 NFEs on super-resolution, directly supporting the claim of lower computational complexity for posterior mean estimation.

4. **Practical algorithmic design** — The fixed precision approximation (Section 4.4) avoids expensive Hessian computation, making the algorithm scalable to high-dimensional images while remaining grounded in the theoretical covariance expressions from Proposition 2.

## Weaknesses

### Major

1. **Limited baseline comparison fails to support "state-of-the-art" claims** — The paper compares only against DPS and MCG. MCG performs pathologically poorly (PSNR 11–18 vs. RMP's 25–35 on most tasks), making it a weak baseline that inflates relative gains. Methods cited in the introduction—DDRM, SNIPS, RED-Diff—are absent from experiments. While some of these (e.g., DDRM/SNIPS with spectral SVD) require different operators, the claim of outperforming "state-of-the-art algorithms" is not adequately supported with only one credible competitor.

2. **Gap between the variational inference theory and the practical algorithm** — The paper frames RMP as solving a variational inference problem (minimizing KL(q_k||p_k) at each step via natural gradient descent). However, in practice (Algorithm 2): (i) the precision Λ_k is fixed to *a priori* approximations rather than learned from the KL objective, (ii) for VP-RMP, T_in=1 meaning the mean is updated exactly once per reverse step with no verification of convergence, and (iii) the claim that minimizing KL(q||p) is "equivalent to" minimizing each KL(q_k||p_k) ignores the marginal weighting by q(x_{k+1}|y). These deviations do not invalidate the method, but the theoretical framing overstates the rigor of the connection.

### Minor

3. **Missing comparison with multi-run DPS** — The paper motivates RMP as avoiding the need to average multiple posterior samples to obtain the posterior mean. The most direct test of this claim would compare RMP (single run) against DPS averaged over multiple runs at comparable NFE cost. While RMP's single-run advantage over single-sample DPS is already useful, this experiment would strengthen the central claim.

4. **Different architectural choices between VE-RMP and VP-RMP are not explained** — VE-RMP uses T=30 and T_in=20, while VP-RMP uses T=400 and T_in=1. These are radically different configurations (total inner steps: 600 vs. 400). The paper provides no ablation or justification for why each variant requires such different settings, making it unclear whether the results are robust or the method requires task-specific tuning.

5. **Hyperparameter ζ not analyzed** — The likelihood score balancing parameter ζ appears critical to performance (it controls the weight of the likelihood gradient relative to the prior score), yet it is not ablated or its sensitivity discussed.

### Trivial

- None.

## Nice-to-Haves

- An ablation study showing how performance depends on the fixed precision approximation (e.g., comparing against the full Hessian-based update on small-scale problems).
- Comparison against RED-Diff (another variational approach) to contextualize the VI framing.
- A clearer explanation of why VE-RMP and VP-RMP use such different T and T_in settings.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Proposition 2 is stated without derivation"** — The derivation may exist in a stripped appendix. The main text provides a justification referencing the reverse SDE formulation. Removed per the rule about missing appendix content.

2. **"The algorithm is not a variational inference procedure in any standard sense"** — Overstated. Fixing some variational parameters while optimizing others and using natural gradient descent are standard VI techniques, even if the particular approximations are coarse. The algorithm does derive its update from the KL objective.

3. **"Comparing single-run RMP to single-run DPS is unfair"** — This misunderstands the paper's claim. The paper argues that targeting the posterior mean is better than sampling, so comparing RMP (mean estimate) to DPS (single sample) is the direct test of this premise. However, comparing to multi-run DPS would strengthen the claim.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add at least one additional credible baseline (e.g., RED-Diff or a multi-run DPS average) to support the "state-of-the-art" claim.
- Clarify the gap between the variational inference theory and the practical algorithm, perhaps by reframing the fixed precision as a design choice rather than a consequence of the VI derivation.
- Ablate the hyperparameter ζ and explain the T/T_in discrepancy between VE and VP variants.
- Include error bars or multiple-seed results where feasible.

## Score and Decision

**Overall assessment**: The paper presents a novel approach to posterior mean estimation in diffusion-based inverse problems, with a clean theoretical motivation and strong empirical results. However, the experimental evaluation is weakened by comparing against only two baselines (one of which is clearly broken), and the theoretical framing overclaims the rigor of the connection between the variational inference theory and the practical algorithm. The core contribution is solid and the results are compelling, but the paper would benefit from broader comparisons and more honest characterization of its approximations.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>