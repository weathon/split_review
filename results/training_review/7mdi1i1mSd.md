Now I have thoroughly read and analyzed the paper. Let me produce the final consolidated review.

## Summary

This paper proposes NoisyTraj, a noise-agnostic framework for trajectory prediction with noisy observations. It introduces a Trajectory Denoise Model (TDM) trained with three losses: a mutual information loss (minimizing information between noisy and denoised observations while maximizing information between denoised observations and clean future trajectories), a reconstruction loss to preserve trajectory structure, and a ranking loss ensuring predictions from denoised observations outperform those from noisy ones. The method is plug-and-play with existing trajectory prediction backbones and is evaluated on ETH/UCY and SDD across Gaussian, Poisson, mixed, and multiplicative noise.

## Strengths

- **Identifies and quantifies a practically important problem**: The paper demonstrates concretely (Figure 1) that adding Gaussian noise (σ=0.4) degrades FDE on ETH/UCY from ~0.35–0.45 m to ~0.60–0.75 m across multiple SOTA methods (GraphTern, EqMotion, SocialVAE, MID). This provides clear motivation for the new problem setting of noisy-observation trajectory prediction.

- **Noise-agnostic design validated across multiple noise types**: The method is explicitly designed not to assume a specific noise distribution, and experiments test it on Gaussian noise (Tables 1–2), Poisson noise (Table 4a), mixed Gaussian+Poisson (Table 4b), multiplicative noise (Table 4c), and cross-distribution generalization (Table 5, train on Gaussian σ=0.4, test on σ=0.2 and Poisson). In every setting NoisyTraj+backbone outperforms both the backbone alone and Wavelet/EMA denoising baselines, supporting the claim of noise-agnostic capability.

- **Plug-and-play integration with consistent gains**: NoisyTraj is applied to two different backbones (GraphTern, EqMotion). On ETH/UCY (σ=0.4), NoisyTraj+GraphTern reduces FDE from 0.67 to 0.48 and NoisyTraj+EqMotion from 0.62 to 0.47 (Table 1). The same pattern holds on SDD (Table 2), demonstrating architecture-agnostic utility.

- **Ablation study confirms each component contributes**: Table 3 isolates the three loss terms. The text reports that removing any one degrades performance, providing evidence that the three-loss design works as intended.

## Weaknesses

### Fatal
None.

### Major

- **Design tension in the reconstruction loss is not adequately justified**: The reconstruction loss (Eq. 15) targets the *noisy* observations at masked locations: $\mathcal{L}_{\text{rec}} = \mathcal{I}(\hat{X}_{\text{obs}}^{\text{mask}} \odot (1-\mathcal{M}_{\text{obs}}),\, X_{\text{obs}} \odot (1-\mathcal{M}_{\text{obs}}))$, where $X_{\text{obs}}$ is noisy. The paper states this "preserves structure information" while the MI loss handles denoising, but never explains why reconstructing noisy values is a sound way to preserve structure that doesn't also counteract the denoising objective. The two losses pull in opposite directions (one toward clean patterns, the other toward reproducing noise). While the ablation shows the combination improves over MI alone, the paper offers no theoretical or empirical analysis of this trade-off, how it is resolved, or why reconstructing noisy targets doesn't harm denoising.

### Minor

- **Missing a learned denoising baseline**: The paper compares against signal-processing denoisers (Wavelet, EMA) and standard prediction models fed noisy inputs. Since clean trajectories $S_{\text{obs}}$ are available during training (synthetic noise), a natural baseline is a learned denoising autoencoder trained with L2 loss to reconstruct $S_{\text{obs}}$ from $X_{\text{obs}}$, then plugged into the same prediction backbones. Without this, it is unclear whether the mutual information and ranking losses provide an advantage over straightforward supervised denoising.

- **No uncertainty quantification or standard deviations**: All reported results in Tables 1–5 lack standard deviations or confidence intervals. Given the modest margins (e.g., ADE 0.45 vs. 0.49 on ETH/UCY at σ=0.4), it is impossible to assess whether differences are statistically significant.

- **No direct denoising quality metrics**: The paper evaluates only prediction metrics (ADE/FDE), which are an indirect measure of denoising. Reporting RMSE or MAE between denoised observations $\hat{X}_{\text{obs}}$ and clean observations $S_{\text{obs}}$ would directly verify that the method actually removes noise rather than merely producing representations that happen to help prediction.

- **Auxiliary network architectures unreported**: The variational approximation $q_\phi(\hat{X}_{\text{obs}}|X_{\text{obs}})$ and the network $T_\psi$ used for mutual information estimation are not described architecturally (layers, hidden dimensions, training schedule). This impedes reproducibility.

- **No hyperparameter sensitivity analysis**: The total loss has four weighting hyperparameters ($\alpha, \beta, \delta, \gamma$). No ablation or sensitivity study is provided, so it is unclear whether performance depends on careful tuning.

### Trivial
None.

## Nice-to-Haves

- An analysis of the estimated mutual information bounds ($I_\mu$ and $I_\psi$) during training would help verify that the optimization is actually achieving the intended information bottleneck behavior.
- Testing on real-world noisy data (beyond synthetic noise) would strengthen claims about practical applicability.
- Replacing the reconstruction loss target with clean $S_{\text{obs}}$ at masked locations (during training, where clean data is available) would be a cleaner design and could be compared to the current formulation via ablation.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Ranking loss can be cheated without true denoising"** (Harsh Critic, Critical Issue #2) — REMOVED: The prediction loss $\mathcal{L}_{\text{pred}}$ (Eq. 16) directly minimizes the prediction error from *both* the denoised and noisy branches. The TPB cannot "deliberately perform worse on noisy inputs" because doing so would increase $\mathcal{L}_{\text{pred}}$. The ranking loss is an additional constraint on top of this joint supervision. The criticism ignores the explicit prediction loss term.

2. **Abstract overstates contribution** — REMOVED (as a distinct weakness): The method is tested on Gaussian, Poisson, mixed, and multiplicative noise with consistent gains, and the design is indeed not tied to any specific noise distribution. Claiming "noise-agnostic" is reasonable given the evidence presented; requiring proof against "truly arbitrary" noise is scope creep.

3. **Best-of-K conflates multi-modality with accuracy** — REMOVED: The reviewer themselves says this is "not necessarily a problem." Using best-of-K for evaluation is standard in trajectory prediction (Salzmann et al., 2020; Xu et al., 2022a), and using it in the loss is a design choice, not a flaw.

4. **Gains over baselines are small** — WEAKENED and merged into the "no uncertainty quantification" point above. The gains are consistent across multiple settings, backbones, and noise types, which strengthens the evidence beyond any single comparison.

## Novel Insights

The key design question raised by these reviews that goes beyond the paper's own framing is whether the reconstruction loss's noisy-target formulation is actually beneficial or whether it represents an unnecessary compromise. The paper's ablation shows L_rec helps over MI alone, but does not disentangle whether this is because the reconstruction loss genuinely preserves useful structure or simply because it acts as a regularizer that prevents representation collapse. Comparing the current L_rec (noisy targets) against a variant that reconstructs clean targets (available during training due to synthetic noise) would cleanly resolve this. This tension is the central unresolved issue in the paper.

## Suggestions

1. Add a learned denoising baseline (e.g., an MLP or transformer autoencoder trained with L2 loss to reconstruct clean $S_{\text{obs}}$ from noisy $X_{\text{obs}}$) and compare to NoisyTraj.
2. Report standard deviations across multiple runs for all main results.
3. Report direct denoising quality (RMSE between $\hat{X}_{\text{obs}}$ and $S_{\text{obs}}$) for NoisyTraj, Wavelet, and EMA.
4. Provide architecture details for $q_\phi$ and $T_\psi$, and include a hyperparameter sensitivity study for $\alpha, \beta, \delta, \gamma$.
5. Address the reconstruction loss tension more explicitly: discuss why reconstructing noisy targets does not harm denoising, or consider ablating with clean targets.

## Score and Decision

The paper addresses a genuinely underexplored problem, proposes a novel approach that is architecture-agnostic, and provides consistent empirical evidence across multiple noise types. The main weakness is a design tension in the reconstruction loss that is not adequately justified, combined with several missing analyses (learned denoising baseline, uncertainty quantification, hyperparameter sensitivity). These are addressable concerns that do not invalidate the core contribution but do limit the strength of the claims in the current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>