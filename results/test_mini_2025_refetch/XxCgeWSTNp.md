Now I have everything I need. Let me write the final consolidated review.

## Summary

This paper proposes a parametric family of reverse-time SDEs for Lévy-Itô diffusion models (LIMs) whose solutions exactly match the marginal densities of the forward diffusion process, unlike the prior approximate SDE (SDE-A) which omits an intractable finite-variation term. The parameter η_t controls the amount of α-stable noise added during reverse sampling, with η_t=0 recovering the deterministic ODE. The paper shows on CIFAR10 image generation that the proposed SDE-E provides large FID improvements over SDE-A when the number of function evaluations is small (e.g., 8.79 vs 144.7 for Euler–Maruyama N=20, α=1.8), without sacrificing sample diversity. It also demonstrates the first application of LIMs to text-to-speech, showing advantages over Gaussian baselines on imbalanced multi-speaker data.

## Strengths

- **Novel theoretical derivation (Theorem 1, Equation 11):** The paper derives the first parametric family of reverse SDEs for Lévy-Itô diffusion models whose solutions match the forward process marginals without requiring the intractable dZ̄_t term. This bridges a notable gap between conventional diffusion models (which have had such parametric families since Song et al. 2021a) and LIMs. The connection between η_t and the noise injection level is clearly explained, and the special cases (η_t=0 → ODE, η_t=1 → forward-matching noise) are correctly identified.

- **Large and consistent empirical gains for small NFE (Tables 1 & 2):** The proposed SDE-E dramatically outperforms SDE-A when the number of function evaluations is small. For Euler–Maruyama with N=20 and α=1.8, SDE-E achieves FID 8.79 versus 144.7 for SDE-A, while coverage jumps from 2.26% to 84.73%. These improvements are consistent across α ∈ {1.8, 1.5, 1.2} and both solvers (Euler–Maruyama, Exponential Integrator), and the diversity benefits hold across all settings.

- **Clear theoretical motivation for the small-NFE regime (Figure 3 and Section 4):** The paper provides an intuitive explanation — via a toy comparison of infinite-variation Lévy processes vs. finite-variation Gamma processes — for why the omitted finite-variation term dZ̄_t becomes non-negligible when the number of solver steps is small. This grounds the empirical findings in a concrete conceptual argument.

- **First application of LIMs to speech synthesis (Table 5):** Training TTS models with α-stable noise (α=1.5) yields speaker similarity scores of 0.782 vs 0.738 (Gaussian) for a rare male speaker at 30 ODE steps, demonstrating that the heavy-tailed noise benefit extends to a new domain beyond images. Confidence intervals are reported.

- **Per-class coverage analysis on imbalanced CIFAR10 (Table 4):** Shows that SDE-E's diversity advantage is not concentrated on majority classes. Class 8 (rarest, 50 images) has 91% coverage with SDE-E vs 80% with SDE-A, confirming the method does not sacrifice rare-class diversity.

## Weaknesses

### Fatal
None.

### Major

- **Hyperparameter η_t tuned on the test set (Section 5.1, line 229):** The paper states: "SDE-E … with the parameters η_t chosen as showing the best performance in terms of FID on CIFAR10 test set containing 10k images." The test set was used for both model selection (choosing η_t) and final evaluation. This violates standard experimental protocol — hyperparameters should be selected on a held-out validation set and the test set used only once. While the improvement magnitudes are so large (e.g., 144.7→8.79 FID) that the core finding (SDE-E helps for small NFE) is clearly robust, the exact reported FID numbers for SDE-E may be optimistically biased and cannot be taken at face value. The authors should re-run using a proper validation split.

### Minor

- **Speech experiments do not evaluate the proposed SDE-E (Section 5.2):** The speech experiments only compare ODE-based sampling with Gaussian noise vs. α-stable noise. The proposed SDE-E sampling algorithm is never tested on the TTS task. To be clear, this is not a flaw in the paper's stated scope — the third contribution is "LIMs applied to TTS," not "SDE-E on TTS" — but given the paper's title ("Improved Sampling Algorithms"), evaluating the sampling algorithm on a second modality would have substantially strengthened the claims of broad applicability.

- **No confidence intervals or multiple-seed runs for image FID (Tables 1 & 2):** The paper reports single-run FID and coverage numbers without variance estimates. Given that the small-NFE improvements are the paper's headline empirical result, multiple seeds with means and standard deviations would help assess statistical reliability. (The speech experiments do report confidence intervals.)

- **The η_t schedule used for each configuration is not fully specified in the main text:** The paper states that "explicit expression for functions η_t used for every model can be found in Appendix B" (which is stripped by the parser), but even the main text could benefit from stating the schedule form or typical optimal η values rather than deferring fully to the appendix.

- **No comparison with standard Gaussian diffusion model baselines on CIFAR10:** The paper compares SDE-E, SDE-A, and ODE within the LIM family, but does not report how these FID numbers stack up against conventional Gaussian-based diffusion models trained on the same data. While the main contribution is about improved sampling within LIMs, a reference point (e.g., DDPM FID on CIFAR10) would help readers contextualize the absolute quality levels.

### Trivial
- The Proof of Theorem 1 is deferred to the appendix without a sketch in the main body; a 2-3 sentence outline of the Fokker-Planck argument would help build confidence.
- The paper does not discuss existence/uniqueness conditions for the SDE (11) beyond briefly mentioning standard regularity assumptions.

## Nice-to-Haves
- Evaluate SDE-E on the speech task for at least one small-NFE setting to demonstrate the sampling algorithm's cross-domain applicability.
- Include a comparison with a conventional Gaussian diffusion model (e.g., DDPM/score-based) on CIFAR10 as an absolute performance reference point.
- Report computational cost comparison of solving SDE-E vs. SDE-A vs. ODE (e.g., wall-clock time per sample).

## Removed Points

- **Criticism about "unverified theoretical derivation" (proof in appendix):** The harsh critic characterized the deferred proof as a "methodological gap" requiring the reader to "take the theorem on faith." Per the removal rules: weaknesses about missing appendix content (proofs, appendices) that are stripped by the parser are not valid criticisms. The original submission contains the full proof in Appendix A. The main text states the proof strategy ("inspecting fractional Fokker-Planck PDEs"), which is standard practice.
- **Criticism about missing related works:** Per removal rules, I cannot comment on missing references as I lack external sources to confirm their existence.
- **Formatting/style nitpicks:** Removed per rules.
- **Criticism about speech experiments being unrelated to core contribution:** The paper explicitly scopes the speech experiments as its third contribution (demonstrating LIMs on TTS), not as an evaluation of SDE-E. The disconnect exists only if one misreads the paper's stated contributions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the evaluation protocol:** Hold out a validation set (e.g., 5k images from the CIFAR10 training set) for tuning η_t. Report final numbers on the test set only once. Re-compute Tables 1 and 2 under this protocol.
2. **Add multiple-seed runs** for the image experiments and report means ± std for FID and coverage.
3. **Evaluate SDE-E on the speech task** for at least one setting (e.g., 30 ODE/SDE-E steps) to demonstrate cross-domain applicability of the sampling method.
4. **Include a statement of the η_t schedule** used in the main text for reproducibility, e.g., η_t = η·(1 - exp(-t/T)) or whatever functional form was used.

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| kKXIYUi8ff (DynamicsDiffusion) | 3.00 | R1 | Weaker — no theoretical contribution comparable to this paper |
| W4djmqKZC6 (Pixel-Aware Diffusion) | 3.00 | R1 | Weaker — less rigorous theoretical grounding |
| WxLwXyBJLw (Flow Matching One-Step) | 3.25 | R1 | Weaker — less novel contribution |
| XeGSIr7z6u (Memorization→Generalization) | 3.40 | R1 | Weaker — smaller scope |
| yhmVrA8W0v (Second-Order Sampling) | 4.60 | R1→R2 | Weaker — stronger assumptions, less empirical support |
| UkLSvLqiO7 (Reproducibility/Consistency) | 5.50 | R2 | Comparable — interesting finding but no novel method |
| jIOBhZO1ax (Simulation-Free Differential Dynamics) | 5.50 | R1 | Comparable — novel method but limited experiments |
| 46mbA3vu25 (Does Diffusion Beat GAN?) | 5.75 | R2 | Slightly stronger — cleaner experimental methodology |
| BoMvv7ypDF (Recursive Score Estimation DMC) | 5.80 | R1→R2 | Comparable — strong theory, no experiments (this paper has both) |
| RiS2cxpENN (Diffusion Models as Cartoonists) | 6.25 | R2 | Stronger — cleaner experiments, accepted |
| 0FbzC7B9xI (Improved Sampling Fluid Dynamics) | 6.60 | R1→R2 | Stronger — sounder experimental methodology, accepted |
| 4EjdYiNRzE (O(d/T) Convergence Theory) | 6.67 | R1 | Stronger — rigorous theory, accepted |
| yVeNBxwL5W (MaRS Sampler) | 7.50 | R2 | Stronger — clean experiments, accepted Spotlight |
| OlzB6LnXcS (Shortcut Models) | 8.00 | R1 | Stronger — full evaluation suite, accepted Oral |
| zMoNrajk2X (CADS) | 8.00 | R1 | Stronger — thorough experiments, accepted Spotlight |

**Round 1 bracket**: 3.5–7.5. The paper is firmly above the weak band (~3.0–3.4) and well below top papers (8+).

**Round 2 narrowing**: Compared against anchors in the 4.5–6.5 range. The paper has a stronger theoretical contribution than yhmVrA8W0v (4.60) and is comparable to BoMvv7ypDF (5.80) and UkLSvLqiO7 (5.50). However, the test-set tuning issue makes it noticeably weaker than 0FbzC7B9xI (6.60) or RiS2cxpENN (6.25), both of which have sounder experimental methodology and were accepted. The paper sits just below the acceptance threshold — a marked paper with real contributions that is undermined by a fixable evaluation protocol flaw.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>