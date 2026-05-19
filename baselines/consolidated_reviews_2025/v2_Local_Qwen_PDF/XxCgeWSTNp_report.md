## Summary
This paper addresses a critical limitation in Lévy-Itô diffusion models (LIMs): the original stochastic sampling algorithm relies on an approximate reverse SDE that neglects a finite-variation term, leading to significant degradation at low function evaluation (NFE) counts. The authors derive a parametric family of exact reverse SDEs that preserve forward marginal densities while allowing precise control over reverse noise injection via a tunable parameter $\eta_t$. Empirical evaluations on CIFAR-10 demonstrate substantial FID improvements (up to 3.5 points at N=20) over the approximate baseline without sacrificing sample diversity. Additionally, the paper extends LIMs to text-to-speech synthesis, showing that $\alpha$-stable noise consistently outperforms Gaussian baselines in speaker similarity on highly imbalanced multi-speaker datasets. The theoretical derivation is rigorous, and the empirical validation effectively supports the core claims.

## Strengths
1. **Theoretical Rigor & Exact Marginal Preservation:** The derivation of a parametric family of exact reverse SDEs (Theorem 1) is mathematically sound and directly addresses the approximation error in prior LIM sampling. The proof correctly leverages fractional Fokker-Planck equations and fractional Laplacian properties.
2. **Strong Empirical Validation at Low NFE:** The CIFAR-10 experiments provide compelling evidence that the proposed SDE-E significantly outperforms the approximate SDE-A at low solver steps (N=20, 50), particularly with Euler-Maruyama. The gains are consistent across different $\alpha$ values.
3. **Novel Application to Imbalanced TTS:** Extending LIMs to text-to-speech synthesis on highly imbalanced datasets (1000 min vs 10 min) is a creative and practically relevant demonstration. The consistent speaker similarity improvements for rare speakers highlight the utility of heavy-tailed noise in data-scarce regimes.
4. **Clear Noise Control Mechanism:** The introduction of $\eta_t$ as a tunable noise schedule provides practitioners with a flexible tool to balance stochasticity and numerical stability, analogous to variance scheduling in standard diffusion models.

## Weaknesses
1. **Missing Variance Reporting in Image Generation:** Tables 1 and 2 report point estimates for FID and coverage without standard deviations or confidence intervals. Given the stochastic nature of diffusion sampling, multi-seed variance is essential to assess statistical reliability and stability.
2. **Incomplete TTS Evaluation Metrics:** The speech synthesis experiments rely solely on CAM++ speaker similarity. Standard TTS evaluations require Word Error Rate (WER) or Mean Opinion Score (MOS) to verify that improved speaker similarity does not compromise linguistic accuracy or perceptual naturalness.
3. **Heuristic Noise Schedule Tuning:** The parameter $\eta_t$ requires manual tuning (Eq. 22), which is acknowledged as a limitation. The paper lacks a systematic analysis of how $\eta_t$ interacts with solver step sizes or $\alpha$ values, leaving practitioners without clear guidelines for schedule design.
4. **Narrative Disconnect in Introduction:** The introduction initially focuses on fast-sampling methods for Gaussian diffusions before abruptly pivoting to dataset imbalance. This creates a disjointed motivation that does not immediately connect the efficiency challenge to the LIM framework.

## Key Issues
1. **Statistical Reliability of Image Results:** The absence of variance reporting for CIFAR-10 FID/coverage metrics prevents readers from assessing whether the observed gains (e.g., 144.7 → 8.79 FID at N=20) are stable across random seeds. This is a standard requirement for diffusion model evaluations.
2. **TTS Intelligibility Verification:** Relying exclusively on speaker similarity for TTS evaluation risks overlooking potential degradation in linguistic accuracy. Without WER or MOS, the practical utility of the proposed method for speech synthesis remains partially unverified.
3. **Lack of Systematic $\eta_t$ Analysis:** The heuristic tuning of $\eta_t$ is a practical bottleneck. The paper does not provide a sensitivity analysis or theoretical guidance on how $\eta_t$ should scale with solver step size or $\alpha$, limiting reproducibility and ease of adoption.

## Actionable Suggestions
1. **Add Multi-Seed Variance for Image Generation:** Report mean ± std over at least 3 random seeds for FID and coverage in Tables 1 and 2, particularly for low-NFE configurations (N=20, 50). If space is limited, move variance data to Appendix Table B1 and reference it in the main text.
2. **Include WER for TTS Evaluation:** Compute Word Error Rate using a standard ASR model (e.g., Whisper) for the synthesized speech. Add a sentence confirming that linguistic accuracy remains comparable across Gaussian and $\alpha$-stable noise types, or include WER results in Appendix Table C1.
3. **Provide $\eta_t$ Sensitivity Analysis:** Add a supplementary figure or table showing how FID varies with different constant $\eta$ values across solver steps. This will help practitioners understand the robustness of the noise schedule and reduce tuning burden.
4. **Refine Introduction Narrative:** Reorder the opening paragraph to establish the efficiency/low-NFE challenge first, then introduce LIMs as a promising but under-optimized framework for this regime. Explicitly link the skipped finite-variation term to low-NFE degradation to foreshadow the theoretical contribution.

## Storyline Options + Writing Outlines
**Abstract Outline (S1-S5):**
- S1 (Problem/Domain): Lévy-Itô diffusion models (LIMs) improve image generation on imbalanced datasets using heavy-tailed $\alpha$-stable noise.
- S2 (Challenge): Their original stochastic sampler solves an approximate reverse SDE, neglecting a finite-variation term that causes significant errors at low NFE.
- S3 (Method): We derive a parametric family of exact reverse SDEs preserving forward marginals, enabling precise control over reverse noise injection via a tunable schedule $\eta_t$.
- S4 (Results): On CIFAR-10, our method reduces FID by up to 3.5 points at N=20 compared to the approximate baseline, maintaining high sample diversity.
- S5 (Extension): We extend LIMs to text-to-speech, demonstrating consistent speaker similarity gains for rare speakers on highly imbalanced datasets.

**Introduction Outline (P1-P4):**
- P1 (Motivation & Gap): Diffusion models face efficiency and imbalance challenges. While fast solvers exist for Gaussian diffusions, LIMs lack exact, noise-controllable reverse dynamics, limiting their low-NFE performance.
- P2 (Prior Work & Limitation): Yoon et al. established LIMs but relied on an approximate reverse SDE due to an intractable term. This approximation fails at coarse solver steps because the neglected finite-variation component becomes non-negligible.
- P3 (Proposed Solution): We bridge this gap by deriving a parametric family of exact reverse SDEs. The noise parameter $\eta_t$ unifies deterministic and stochastic sampling, allowing practitioners to balance trajectory stochasticity and numerical stability.
- P4 (Contributions): (1) Theoretical derivation of exact parametric reverse SDEs. (2) Empirical validation showing substantial FID/coverage gains at low NFE on CIFAR-10. (3) Successful application to imbalanced TTS, outperforming Gaussian baselines in speaker similarity.

## Priority Revision Plan
**P0 (Critical - Must Fix):**
- Add multi-seed variance reporting for CIFAR-10 FID/coverage (Tables 1 & 2). Compute mean ± std over 3 seeds and include in main text or Appendix B1.
- Include WER evaluation for TTS experiments to verify linguistic accuracy is preserved alongside speaker similarity gains.

**P1 (Major - Strongly Recommended):**
- Refine Introduction narrative to explicitly connect low-NFE efficiency challenges to the LIM approximation error, foreshadowing the parametric SDE contribution.
- Add a sensitivity analysis or guideline for tuning $\eta_t$ across solver steps and $\alpha$ values to reduce heuristic burden.

**P2 (Minor - Nice to Have):**
- Strengthen Conclusion with a forward-looking statement on integrating exact reverse dynamics with consistency models or adaptive solvers.
- Clarify regularity assumptions in Appendix A proof regarding fractional Laplacian commutativity with spatial derivatives.

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|---|---|---|---|---|---|---|
| E1 | Exact SDE improves low-NFE image quality | CIFAR-10, $\alpha \in \{1.8, 1.5, 1.2\}$, N=20/50/500 | FID, Coverage | SDE-E outperforms SDE-A at N=20/50 | C2 | No variance reported |
| E2 | Exact SDE maintains diversity on imbalanced data | Imbalanced CIFAR-10, N=20 | FID, Coverage (per-class) | SDE-E improves FID & coverage without rare-class drop | C2 | Single $\alpha=1.8$ tested |
| E3 | $\alpha$-stable noise benefits imbalanced TTS | 1000min female vs 10min male, N=30/50/100 | Speaker Similarity (CAM++) | $\alpha$-stable > Gaussian, especially at low N | C3 | No WER/MOS reported |

**Research-Theme Gap Diagnosis:**
- Statistical reliability of image generation gains is unverified due to missing multi-seed variance.
- TTS linguistic accuracy and perceptual quality are unassessed, leaving practical utility partially open.
- $\eta_t$ tuning lacks systematic guidance, limiting reproducibility.

**Proposed Research Experiments:**
1. **Multi-Seed Stability Test (P0):** Run E1 over 3 seeds. Report mean ± std FID/Coverage. *Success:* Std < 0.5 FID at N=20.
2. **TTS WER Evaluation (P0):** Compute WER using Whisper on E3 samples. *Success:* WER difference between Gaussian and $\alpha$-stable < 1%.
3. **$\eta_t$ Sensitivity Sweep (P1):** Test constant $\eta \in \{0.0, 0.2, 0.5, 1.0\}$ across N=20/50. *Success:* Identify robust $\eta$ range insensitive to small perturbations.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 7.5/10

The paper presents a theoretically rigorous and empirically validated improvement to Lévy-Itô diffusion sampling. The derivation of exact parametric reverse SDEs is a solid contribution that directly addresses a known approximation error, with compelling low-NFE gains on CIFAR-10. The extension to imbalanced TTS is creative and practically relevant. The score is moderated by the lack of multi-seed variance reporting for image results and incomplete TTS evaluation metrics (missing WER/MOS), which are standard requirements for statistical reliability and practical utility verification.

Post-Revision Target: [8.5, 9.0]/10

Adding multi-seed variance, WER evaluation, and a brief $\eta_t$ sensitivity analysis will fully close the evidence gaps, strengthening statistical confidence and practical reproducibility. The theoretical core is already strong, and these empirical refinements will elevate the paper to a clear acceptance standard.