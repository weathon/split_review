## Summary

This paper introduces DLPO (Diffusion model Loss-guided Policy Optimization), a method that fine-tunes diffusion-based text-to-speech models by combining a pretrained MOS predictor (UTMOS) as reward with the diffusion model's own denoising loss as a regularization penalty. The paper compares DLPO against four existing RL-for-diffusion methods (RWR, DDPO, DPOK, KLinR) on WaveGrad2, showing that DLPO achieves the best UTMOS (3.65) and NISQA (4.02) scores while RWR and DDPO actively degrade quality.

## Strengths

- **DLPO's design of incorporating the diffusion loss as a reward penalty produces clear improvements over the baseline.** Table 1 shows DLPO raises UTMOS from 2.90 (baseline) to 3.65 and NISQA from 3.74 to 4.02, both statistically significant (p < 10⁻²⁰), with a demo page confirming audible improvements.

- **The paper documents a non-obvious negative result: RWR and DDPO degrade TTS quality, unlike their success in text-to-image.** Table 1 shows RWR (UTMOS 2.18, NISQA 3.00) and DDPO (UTMOS 2.69, NISQA 2.96) fall below the baseline (UTMOS 2.90, NISQA 3.74), with generated audio becoming "acoustically noisy" (Section 5). This challenges the transferability assumption from prior image-domain work and motivates TTS-specific RL design.

- **A human listening experiment confirms that automatic-metric improvements translate to perceptual gains.** Across 20 audio pairs evaluated by 11 listeners, 67% preferred DLPO over the baseline versus 14% preferring the baseline (19% tie), providing direct evidence beyond proxy MOS scores.

- **The OnlyDL ablation cleanly isolates the contribution of the RL reward from the diffusion loss term.** OnlyDL (diffusion loss alone) achieves UTMOS 3.16 and NISQA 3.45, far below DLPO's 3.65/4.02 (Table 1), demonstrating the RL reward is the primary driver of improvement.

- **Use of NISQA as a held-out evaluation metric guards against reward overfitting.** The paper explicitly states this design choice (Section 5, "Evaluation Metrics" paragraph), and NISQA is an independently-trained model from a different corpus, so the consistent NISQA improvements cannot be explained by reward hacking alone.

## Weaknesses

### Fatal
None.

### Major
- **All methods are compared with identical hyperparameters (α=1, β=1) without tuning, undermining the central comparative claim.** Table 1 assigns α=1, β=1 to DLPO, DPOK, KLinR, and DDPO without any ablation or search. Different methods have fundamentally different sensitivities to these parameters: DPOK applies KL regularization at every timestep, KLinR shapes the reward with a KL penalty, and DLPO uses a single-timestep diffusion loss penalty. Without a hyperparameter sweep over β (e.g., {0.1, 0.5, 1.0, 5.0}), the claim that "DLPO outperforms DPOK and KLinR" cannot be separated from the possibility that β=1 happens to favor DLPO's particular formulation. This is the paper's central comparative claim, and the evidence is insufficient to support it robustly.

### Minor
- **UTMOS serves as both the RL reward and a primary evaluation metric, introducing circularity.** The paper's main quantitative evidence rests on two learned MOS predictors, one of which (UTMOS) is directly optimized during training. NISQA partially mitigates this (it was not used during training), and the human evaluation provides a partial check, but the core quantitative evidence for DLPO's improvement is partially confounded.

- **No statistical significance tests are reported between DLPO and the other successful methods (DPOK, KLinR).** The paper reports t-tests for DLPO vs. baseline (p < 10⁻²⁰), but the gaps between DLPO and DPOK/KLinR (e.g., UTMOS 3.65 vs. 3.18 vs. 3.02) are not tested for significance, leaving uncertainty about whether these differences are reliable given the variance visible in Figure 1.

- **The human evaluation is too small to carry substantial evidential weight.** 11 raters and 20 audio pairs (from a single speaker) yields at most 220 comparisons. No confidence intervals, inter-rater reliability metrics, or statistical significance analyses are reported. While 67% preference is directionally positive, the study is more suggestive than conclusive.

- **The paper tests on a single dataset (LJSpeech, one female speaker).** Generalizability to multi-speaker TTS or other domains is untested and not discussed as a limitation.

- **DPOK achieves slightly better WER (1.1%) than DLPO (1.2%), which is not discussed.** This suggests a quality-intelligibility trade-off that different methods navigate differently, and the paper should address what this means for DLPO's overall advantage.

### Trivial
- **The "RLHF" framing is imprecise.** UTMOS is a fixed pretrained predictor, not an iterative human feedback loop. While UTMOS was trained on human MOS ratings, calling the procedure "RLHF" conflates it with methods where human preferences directly shape the reward during fine-tuning.

- **The OnlyDL objective formulation is unusual and underexplained.** The loss `-log p_θ(x_{t-1}|x_t,c) * (-‖ε̃ - ε_θ‖₂)` equals `log p_θ * diff_loss`, which is not obviously a sensible objective. The paper does not justify why this specific form was chosen.

- **The gradient formulation in Eq. 11 places the diffusion loss gradient inside the REINFORCE term rather than as a separate additive term.** The paper should clarify whether this is theoretically motivated or a heuristic choice.

## Nice-to-Haves
- A hyperparameter sweep over β (and possibly α) for each method would substantially strengthen the comparative claim.
- A larger-scale human evaluation with more raters, confidence intervals, and inter-rater reliability metrics.
- Discussion of the WER result: why DPOK achieves the best WER and what this implies about the quality-intelligibility trade-off.
- Analysis of whether DLPO, DPOK, or KLinR exhibit subtler forms of reward over-optimization (e.g., unnatural prosody, artifacts) beyond the catastrophic collapse observed for RWR/DDPO.

## Removed Points
These points are flagged for removal; treat them with caution:
- **Weakness about missing code/reproducibility details (random seeds, checkpoints, code release):** Removed per hard rules — these are considered nitpicks about reproducibility artifacts impractical to include in a submission.
- **Weakness about no inference-time analysis:** Removed as a nice-to-have, not a core weakness.
- **Speculation that "DPOK or KLinR would match or exceed DLPO with a different β value":** The core concern about fixed hyperparameters is retained as Major, but the specific speculation about what would happen with different β values is removed — it is not verifiable from the paper.
- **Weakness about missing appendix or deferred proofs:** Removed per hard rules — the parser strips these from all papers.
- **Criticism that the "first to apply RL" novelty claim is thin vs. Nagaram et al. (2024):** The paper correctly distinguishes "speech quality" from "emotional expression" and cites Nagaram et al. The distinction is reasonable.

## Novel Insights
The reviews collectively surface a tension not fully articulated in the paper: the hyperparameter sensitivity issue interacts with the evaluation circularity concern in a way that compounds uncertainty about DLPO's claimed advantage. If β=1 happens to favor DLPO over DPOK/KLinR (which use the same β but structurally different regularization), and the evaluation relies partly on the same predictor used for training (UTMOS), then the magnitude of DLPO's reported advantage could reflect both a genuine improvement and favorable evaluation conditions. A hyperparameter sweep would disentangle these factors. Additionally, the negative result for RWR/DDPO is actually the paper's cleanest finding — these methods lack any regularization mechanism, and their failure is predictable from their design. The paper's framing of this as a domain-specific discovery overstates the finding.

## Suggestions
- Conduct a hyperparameter sweep over β (and possibly α) for each method, at minimum over {0.1, 0.5, 1.0, 5.0}, and report whether DLPO's advantage over DPOK/KLinR is robust across the range.
- Add statistical significance tests between DLPO and DPOK/KLinR for both UTMOS and NISQA.
- Report confidence intervals and inter-rater reliability for the human evaluation, or expand the study.
- Add a brief discussion of the WER results and the quality-intelligibility trade-off.
- Acknowledge the single-dataset limitation explicitly and discuss generalizability.
- Clarify whether the gradient formulation in Eq. 11 is theoretically motivated or a heuristic design choice.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>