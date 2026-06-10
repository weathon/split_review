Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes SafeConPhy, combining diffusion models with conformal prediction to generate control sequences for physical systems that satisfy safety constraints. The method pre-trains a diffusion model, computes a conformal prediction-based safety bound, then iteratively improves safety through guidance and fine-tuning using the bound. Experiments on 1D Burgers' equation and 2D incompressible fluid control tasks show that SafeConPhy achieves the safety constraint while outperforming prior safe methods on the control objective.

## Strengths

- **Empirically demonstrates safety-constrained control with strong performance simultaneously**: On both the 1D Burgers' equation and 2D incompressible fluid tasks (Tables 2 and 3, lines 222, 278), SafeConPhy is the only method that satisfies the safety constraint ($s_{\text{norm}} < 1$) while achieving the best control objective $\mathcal{I}$ among safe methods, sometimes matching methods that ignore safety entirely. This is a genuine empirical result.

- **Ablation confirms the fine-tuning component drives safety improvement**: The ablation study (Table 4, lines 280–284) shows that removing fine-tuning causes a significant decline in safety, confirming that the iterative safety improvement loop, not just the conformal bound or guidance, is responsible for the safety gains.

- **Tackles a practical and challenging experimental setup**: Both tasks involve high proportions of unsafe training data (89.7% unsafe in 1D, 53.1% unsafe in 2D), and the 2D task requires indirect control with 1,792 spatial control parameters. The method succeeds where many baselines (BC, CDT, TREBI, SL-Lag) either violate safety or sacrifice performance.

## Weaknesses

### Major

- **The conformal prediction guarantee is not verified empirically, which undermines the paper's central claim**: The paper's primary contribution is a "provable" and "certifiable" safety bound (abstract, line 7, Lemma 1). However, the experiments never verify the probabilistic guarantee. The standard way to validate a conformal prediction claim is to report empirical coverage — the fraction of test trajectories where the true safety score falls below the predicted bound $s_+$. Instead, only $s_{\text{norm}}$ and unsafe rates are reported (lines 244–258, 274). Without coverage verification, the "user-defined probability" claimed in the abstract is unsupported by evidence.

- **The confidence level $\alpha$ is never specified**: The conformal prediction guarantee depends on a user-defined $\alpha$ (the probability that the bound fails). The paper introduces $\alpha$ in the method (Eqs. 12–13, lines 167–181) but never reports what value is used in the experiments. This makes the central claim unfalsifiable — a guarantee of "at least $1-\alpha$ probability" is vacuous without stating $\alpha$. Multiple values of $\alpha$ should also be investigated to show the safety-performance trade-off.

- **The relationship between iterative fine-tuning and the conformal guarantee is not adequately explained**: The conformal prediction bound (Lemma 1) applies to a fixed model. The method then uses this bound in a loss function to fine-tune the model parameters (Eq. 15, line 202), which changes the model's error distribution. The paper states the bound is "progressively updated" (line 113) but provides no mechanism or theoretical argument for how the probabilistic guarantee survives after model updates. If the bound is recomputed from the calibration set at each iteration, this should be explicitly stated and its implications for the final guarantee explained; if it is not recomputed, the guarantee is invalidated. This gap leaves the paper's core theoretical claim incomplete.

- **Critical experimental details are missing, impairing reproducibility**: Several key hyperparameters are not reported: the guidance weight $\gamma$ (Eq. 14), fine-tuning weight $\beta$ (Eq. 15), step size $\eta$ (Eq. 4), diffusion loss weight $\lambda$ (Eq. 2), number of diffusion steps $K$, number of fine-tuning iterations, size of $D_{\text{sampled}}$, and calibration set size. Without these, the results cannot be reproduced or compared against in future work.

### Minor

- **The quantile is claimed to be differentiable without discussion**: The paper states that $Q(1-\alpha; \tilde{S})$ is "still a differentiable function with respect to $\theta$" (line 173). The quantile of a finite set is piecewise constant and not differentiable at jump points. While differentiable approximations or subgradients exist in practice, the paper provides no discussion of how this is handled, leaving a gap in the methodological description.

- **Typo in Eq. 11 (line 164)**: The score set definition writes $s(\mathbf{w}_i)$ where the correct term should be $s(\mathbf{u}_i)$ to match the definition in Eq. 7 (line 124). This appears to be a transcription error.

### Trivial

- **"D_cul" typo in Eq. 8 (line 158)**: The denominator writes $D_{\mathrm{cul}}$ where it should be $D_{\mathrm{cal}}$.

## Nice-to-Haves

- A cleaner ablation that isolates the effect of guidance vs. safety loss vs. diffusion loss during fine-tuning (as noted by one reviewer) would strengthen the analysis.
- Reporting error bars or variance across random seeds would help assess the reliability of the reported improvements.

## Removed Points

These points were raised by reviewers but are removed after verification:

- **"The weight approximation eliminates the distribution shift that conformal prediction is supposed to address"**: This criticism is factually incorrect. The weight derivation simplifies $\omega = C \cdot e^{-\mathcal{G}}$ under the reasonable assumption that $p_\theta \approx p$ (the diffusion model is well-trained on data). The distribution shift from the guidance $\mathcal{G}$ is preserved in the weights; the dropped ratio $p_\theta/p$ captures model approximation quality, not covariate shift. The criticism misunderstands the role of the approximation.

- **"Lemma 1 is not proved"**: Lemma 1 is a standard result from weighted conformal prediction (Tibshirani et al., 2019). A citation to the original proof satisfies the requirement for a conference paper.

- **"Algorithm 1 is not in the main text" / "No code or data release"**: The parser strips these from all papers. They exist in the original submission.

- **"The score set definition has a likely typo: Eq. 7 and Eq. 11 write s(w_i)"**: Eq. 7 (line 124) correctly writes $s(\mathbf{u}_i)$. Only Eq. 11 has the typo, which is already listed above.

- **"TREBI/FISOR comparison too vague"**: The paper explicitly states the distinction (line 17): these methods "fail to compute the probabilistic bound of safety costs concretely," which is a meaningful differentiation given the paper's focus.

- **"The method may not work under extreme distribution shift with few safe samples"**: This is speculative; the paper actually achieves safe control on the 1D task where 90% of calibration samples are unsafe, so the concern is not supported by evidence.

- **Generic strengths removed**: "Addresses an important problem" and similar generic statements are not substantive enough to retain.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the theoretical claim (provable bound via conformal prediction) and the empirical evaluation (which does not validate the bound), and the missing explanation of how iterative fine-tuning interacts with the conformal guarantee — but these are criticisms, not novel insights.

## Suggestions

1. **Report empirical coverage**: Compute and report the fraction of test trajectories where $s(\mathbf{u}(\mathbf{w})) \le s_+(\tilde{\mathbf{u}}_\theta(\mathbf{w}))$ and compare with the nominal $1-\alpha$ level. This is the minimal experiment needed to support the "certifiable" claim.
2. **State $\alpha$ explicitly** and show results for multiple values (e.g., $\alpha = 0.1, 0.05, 0.01$).
3. **Clarify the iterative procedure**: Describe explicitly whether the conformal bound is recomputed from scratch on the calibration set after each fine-tuning step, and explain how the guarantee applies to the final model.
4. **Report all hyperparameters**: $\gamma$, $\beta$, $\lambda$, $\eta$, $K$, calibration set size, number of fine-tuning iterations, and $|D_{\text{sampled}}|$.

## Score and Decision

The paper proposes a conceptually interesting combination of diffusion models and conformal prediction for safe physical system control and demonstrates empirical results that outperform prior methods. However, the central claim of a "provable," "certifiable" safety bound is not supported by the evaluation — the experiments never verify the conformal prediction coverage, the confidence level $\alpha$ is not specified, and the interaction between iterative fine-tuning and the conformal guarantee is not adequately explained. These are substantive gaps that prevent the paper from delivering on its stated contribution. The method may have value as an empirical heuristic, but the paper is framed around a theoretical guarantee it does not substantiate.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>