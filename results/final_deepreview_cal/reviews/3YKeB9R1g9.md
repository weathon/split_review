## Summary

This paper identifies the key conditions under which training loss curves (TLCs) *collapse* (align after normalization) across model scales during LLM pre-training: matching the AdamW timescale τ, the tokens-per-parameter ratio (TPP), and the LR schedule. It shows that when τ is set optimally for a given TPP, collapse emerges naturally as a signature of compute-efficient training. The paper introduces **Celerity**, an LLM family trained in this regime (up to 3.9B parameters), and demonstrates two applications: (1) collapse residuals as an early diagnostic for training anomalies, and (2) a parametric surrogate for normalized TLCs that enables early stopping in hyperparameter tuning (predicting final loss after 10–30% of training).

## Strengths

- **Identifies the three controls governing TLC shape at LLM scale and demonstrates their sufficiency for collapse.**  
  Section 3 and Figures 3–4 systematically vary η, λ, B, TPP, and model size (111M–3.3B), showing that normalized TLCs align when τ and TPP are matched and the LR schedule is fixed. This extends prior work (Qiu et al., 2025) from small μP models with vanilla Adam to practical LLM families with co-scaled width, depth, batch size, and weight decay — a non-trivial advance the prior work explicitly called for.

- **Provides a mechanistic explanation for τ's effect via a bias–variance decomposition (Eq. 3, Appendix B.3).**  
  The noisy quadratic model shows why smaller τ gives faster initial decay but a higher floor, while larger τ gives slower progress but better variance suppression — and why, after normalization, the curve depends only on τ and ̂t. This gives the paper's core empirical findings a clean theoretical anchor.

- **Introduces Celerity, a practically useful LLM family trained with demonstrated collapse.**  
  The paper trains and releases models at 20, 80, and 234 TPP across 300M–3.9B, showing tight collapse (Fig. 6). The 234-TPP models sit on the accuracy/compute Pareto frontier relative to published open models (Fig. 2). Training with fixed TPP bands enables cross-scale comparisons and diagnostics that are not possible with variable-TPP families like Llama-2.

- **Proposes a parametric surrogate for normalized TLCs (Eq. 4–5) and validates that it enables early stopping.**  
  The surrogate is fit on 111M-scale data (1000× fewer FLOPs than the 3.3B target) and predicts final loss accurately enough to identify the best λ setting after 10–30% of training (Fig. 9). This significantly outperforms the naive "current best" baseline and demonstrates a concrete practical payoff from the collapse understanding.

- **Collapse residuals serve as an early diagnostic in a genuine production-scale incident.**  
  The 1.8B numerical instability was detected by collapse residuals at ~60% of training, well before the raw loss showed an upward blip at ~90% (Fig. 1 right vs. Fig. 6 right). This is a real, not synthetic, example.

## Weaknesses

### Major

None. The core claims are supported by the evidence presented.

### Minor

- **The diagnostic application rests on a single incident.**  
  The paper shows one case (1.8B numerical instability) where collapse residuals detected an issue earlier than raw loss. While this example is compelling and genuine, the paper generalizes to "deviations from collapse allow precise identification…of numerics issues" without systematic validation across multiple runs or injected perturbations. A synthetic study (e.g., injecting known anomalies at small scale and measuring detection latency) would substantiate the claim. As written, this is a promising demonstration rather than a validated method.

- **The collapse phenomenon lacks a quantitative quality metric.**  
  The paper defines collapse by visual inspection — "curves align" — and does not provide a quantitative measure (e.g., mean absolute deviation between normalized curves across scales, compared to inter-run noise). Such a metric would strengthen the diagnostic and early stopping applications and enable principled comparisons across TPP bands. (The surrogate model evaluation uses MAE, but not for collapse itself.)

- **The compute-efficiency claim is framed more strongly than the evidence.**  
  "Celerity is at the compute-efficiency frontier" (Fig. 2) is supported by comparison against published results from other model families, but these comparisons are heterogeneous in data mixture, training procedures, evaluation protocols, and tuning effort. The paper acknowledges some of these issues (Philosophy paragraph) but the "Pareto frontier" framing invites a level of precision that the cross-family comparison does not provide. The honest and still-interesting claim is: "Celerity achieves competitive accuracy for its training FLOPs when compared to published open models." The empirical evidence supports this weaker claim directly.

- **The early stopping evaluation uses a simple "current best" baseline but not standard HPO methods.**  
  The paper shows that its method outperforms naive "current best" and random choice, which is a reasonable first demonstration. However, the setting (predicting final loss from partial curves to select hyperparameters) is related to, but not directly comparable with, pruning methods like ASHA or successive halving — these address a different problem (multi-trial stopping). The paper should state this distinction clearly so readers can assess where the method fits in the broader HPO toolkit.

- **Hyperparameter transfer via fixed-TPP bands is claimed as an advantage but not experimentally validated.**  
  The paper states that fixed TPP enables tuning τ at small scale and zero-shot transferring to larger models. While τ was indeed tuned on a proxy and transferred via scaling rules in Celerity's training, no explicit experiment demonstrates that τ tuned at, say, 300M yields near-optimal final loss at 3.9B. This claim would be strengthened by an explicit transfer experiment.

### Trivial

- Figure 8 shows only one example (3.3B). A table of MAE across multiple model sizes (provided in Appendix Table 11) is mentioned but not shown in the main text. Moving this into the main paper would help.
- The surrogate model (Eq. 4) is described as fitting 5 parameters on 111M data; a brief note on overfitting risk (and why the fit is stable) would be helpful.

## Nice-to-Haves

- Compare the early stopping method to a trial-pruning baseline if one can be adapted to this setting (e.g., predict final loss from early checkpoints using existing parametric forms from the loss-curve-prediction literature — Schaipp et al., Hong & Wang 2025 — which the paper already cites).
- Quantify collapse tightness with a metric such as the mean absolute deviation between normalized curves across scales, and show it is smaller than inter-run noise.
- Add a synthetic diagnostic study: inject known anomalies (e.g., data corruption, LR spike) at small scale and measure whether residuals detect them earlier than raw loss.
- Include an explicit τ-transfer experiment across model sizes at fixed TPP.

## Removed Points

These points were raised but are removed or downgraded after verification against the paper:

1. **"Extra FLOPs not accounted for in Figure 2"** — Removed. Figure 2 plots actual FLOPs on the x-axis; the 67% extra FLOPs for 234-TPP models is *already reflected* in their x-coordinate. The critic confused the trade-off analysis (Fig. 5) with the empirical comparison (Fig. 2).

2. **"Controlled compute-efficiency experiment needed"** — Removed as a required weakness. The paper's Figure 2 is a standard cross-family comparison in the open-LLM literature. A controlled experiment (holding data/compute constant) would be stronger but is not the norm for positioning a model family, and the paper already provides transparent trade-off analysis (Fig. 5).

3. **"Ablation of architecture choices (Squared ReLU, ALiBi, etc.)"** — Removed. This is speculative and unsupported; the paper shows collapse under two distinct architectures (GPT2-like in Section 3, Celerity in Section 4), suggesting robustness. No evidence suggests collapse depends on these specific choices.

4. **"Theoretical derivation is only sketched"** — Removed. The paper explicitly points to Appendix B.3 for the full derivation of Eq. 3. The main text provides the intuition; full formalization in an appendix is standard practice.

5. **"ASHA/HPO methods as required baselines"** — Downgraded to nice-to-have. The paper's setting (predicting final loss from partial curves) differs from trial-pruning methods. The "current best" baseline is a reasonable first comparison; the paper does not claim to outperform established HPO methods.

## Novel Insights

The anonymous review process did not surface genuinely novel observations beyond the paper's own contributions. However, one synthesized insight is worth noting: the paper shows that the *same* normalized timescale τ that controls the bias–variance trade-off in a noisy quadratic model also determines whether TLCs collapse across model scales — unifying the practical goal of loss-curve alignment with a classical optimization concept. This connection between the AdamW EMA viewpoint (Wang & Aitchison 2024) and the collapse phenomenon (Qiu et al. 2025) is the paper's cleanest conceptual contribution.

## Suggestions

- **Narrow the compute-efficiency claim.** Replace "Pareto frontier" phrasing with "competitive accuracy for its training FLOPs vs. published open models." The empirical evidence supports this directly.
- **Quantify collapse tightness.** Add a metric (e.g., mean absolute deviation between normalized curves across scales) and report it for each TPP band, ideally relative to inter-run noise.
- **Validate diagnostics systematically.** Add a small-scale synthetic study injecting known anomalies (e.g., altered LR, data corruption, numerical perturbation) and measuring whether residuals detect them earlier than raw loss.
- **Acknowledge scope explicitly.** Add a Limitations section noting that the diagnostic method was tested on one incident, and the early stopping method has not been compared to existing HPO approaches.

## Score and Decision

**Calibration anchors used:**

| Round | Anchor ID | Score | Comparison |
|-------|-----------|-------|------------|
| R1 | o9YC0B6P2m | 6.75 | LR-annealing scaling law; cleaner claim, but less novel than this paper |
| R1 | WYL4eFLcxG | 6.00 | LR scaling across token horizons; narrower scope, less ambitious |
| R1 | xGM5shdGJD | 5.20 | Scaling law estimation methodology; less novel |
| R1 | d8w0pmvXbZ | 8.00 | Training instabilities at scale; stronger experimental rigor |
| R2 | KnoS9XxIlK | 6.00 | Multi-power loss curve prediction; similar topic, less novel |
| R2 | iZeQBqJamf | 6.50 | Over-training scaling laws; comparable rigor, less original insight |
| R2 | P7KRIiLM8T | 7.33 | μP improvement; cleaner execution, narrower contribution |

**Round 1 bracket:** [5.5, 7.5]  
**Round 2 narrowing:** Comparisons to anchors at 6.00, 6.50, 6.75 place this paper above the 6.00 papers (more novel, broader scope, larger scale) and comparable to the 6.50–6.75 range. The overclaims and limited validation of the diagnostic application keep it below the 6.75 anchor's level of experimental rigor.  
**Final score:** 6.5

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>