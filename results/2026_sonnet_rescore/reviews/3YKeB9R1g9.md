Now I have a thorough read of the paper. Let me compose the final consolidated review.

---

## Summary

This paper demonstrates that LLM training loss curves (TLCs) collapse onto a universal normalized trajectory across model scales when three controls are matched: the AdamW timescale τ, the tokens-per-parameter ratio (TPP), and the learning-rate schedule. The authors show this collapse holds at practical LLM scales (300M–3.9B parameters) under realistic joint scaling of width, depth, batch size, and weight decay—directly answering the open challenge posed by Qiu et al. (2025). The Celerity model family is trained in this collapse regime and demonstrated to sit on the compute-efficiency Pareto frontier, while two concrete applications of collapse are validated: (1) deviation-from-collapse as an early diagnostic of training anomalies, and (2) collapse-guided early stopping for hyperparameter tuning using only 10–30% of large-scale training.

---

## Strengths

- **Systematic empirical identification of τ and TPP as scale-invariant TLC controls (Fig. 3, 4, Eq. 3):** The paper sweeps η, λ, and B independently (Fig. 3) at 610M/80TPP to show normalized TLC shape is controlled by τ alone, and separately shows TPP further modulates shape in a scale-invariant way (Fig. 4, spanning 111M–3.3B, a 1000× compute range). This provides mechanistic grounding via the noisy-quadratic bias–variance decomposition (Eq. 3), giving the results theoretical coherence beyond raw empiricism.

- **Extension of collapse to full-scale practical LLM pretraining:** Qiu et al. (2025) demonstrated collapse only on small-scale, specialized tasks under vanilla Adam without weight decay. This paper extends collapse to a realistic scaling ladder—co-scaling width, depth, batch size, weight decay, and LR under CompleteP—across 300M–3.9B models, directly answering their stated challenge. The 80 TPP band achieves tight collapse (N(r=0.087)) and the 20 TPP band also collapses (N(r=0.175)).

- **Concrete real-world diagnostic case study (Fig. 1 right, Fig. 6 right):** The 1.8B/234-TPP training anomaly—detected via collapse residuals starting at ~60% of training, whereas the raw loss curve only shows a visible blip after ~90%—is a compelling existence proof. The paper documents that the anomaly was traced to a numerical kernel issue triggered at specific microbatch sizes, and that restarting from before the divergence caused the repaired run to track the reference closely.

- **Principled early stopping with near-zero optimality gap at 10–30% of training (Fig. 9):** The predicted-best method achieves negligible loss gaps for λ sweeps at both 1.7B and 3.3B, while the current-best baseline fails at 1.7B. The surrogate fit on 111M-scale data transferring to 3.3B (Fig. 8) is clean evidence that the predictive model generalizes across scales.

- **Celerity on compute-efficiency frontier (Fig. 2):** Celerity models form the accuracy/compute Pareto frontier among comparable open models without task-specific annealing, achieving comparable accuracy to BTLm with ~75% fewer training FLOPs.

---

## Weaknesses

### Fatal
None.

### Major

- **The CompleteP–µP theoretical gap is unaddressed.** The collapse theory throughout Section 3 is derived under µP (using results from Qiu et al. 2025; Noci et al. 2024). Celerity, however, uses "CompleteP, which enables hyperparameter transfer over width *and* depth" (Section 4). The paper notes CompleteP outperforms µP empirically (Fig. 15), but never addresses whether the theoretical properties that underpin collapse (scale-consistent curvature under µP, per Noci et al. 2024; EMA timescale behavior) carry over to CompleteP without modification. This is a genuine gap: the collapse phenomena being demonstrated empirically uses a different parameterization than the one the theory is built for, and the authors leave this as an implicit assumption. At minimum, this should be acknowledged as a limitation or justified by an argument that CompleteP preserves the relevant µP scaling properties.

### Minor

- **The collapse quality metric N(r=...) is used but not defined in the main text.** Fig. 6 captions report "N(r=0.175)" and "N(r=0.087)" for the 20 TPP and 80 TPP bands respectively, without explaining what this notation means (RMSE of normalized residuals? proportion of curves within radius r? normalized by what?). This prevents the reader from calibrating how tight the collapses are relative to each other or to non-collapsed families. The definition may exist in the stripped appendix, but the reader of the main paper cannot evaluate the central quantitative claim about collapse quality.

- **Incomplete collapse at 234 TPP is acknowledged but incompletely analyzed.** The paper states (Section 4): "At 234 TPP, divergences appear late in training for larger models (Fig. 1, middle). Investigating, we find loss improves disproportionately on training data, while held-out data remains aligned with projections." This is the critical band for Celerity's efficiency claims. The distinction between expected scale-dependent divergence (overfitting on training data) and genuine training pathology is important for the diagnostic application—the reader cannot tell from the main text analysis how to make this call in a production setting.

- **Early stopping experiments test only λ sweeps.** Section 5 and Fig. 9 demonstrate early stopping for λ (weight decay) sweeps at 1.7B and 3.3B. Learning-rate and batch-size sweeps are at least as common in practice and are discussed as motivating use cases. The principle should generalize, but the evidence would be stronger with even one additional HP type.

### Trivial

- **Theoretical model for LR decay case is qualitative.** Eq. 3 is derived under constant LR. The extension to decaying schedules (Section 3, last paragraph) is a plausible qualitative argument ("With LR decay, η_t λ decreases and the instantaneous timescale τ_t increases, enhancing late-stage variance suppression") appended to a constant-LR result rather than derived from it. The paper acknowledges the theory is in the appendix, but the main-text framing oversells the theoretical derivation's coverage of the decay case.

---

## Nice-to-Haves

- A rigorous analysis of when and why collapse degrades at 234 TPP for larger models would substantially strengthen the paper. Specifically: showing the held-out loss curves alongside the training loss curves, characterizing the scale at which divergence begins as a function of model size, and providing guidance on when collapse residuals remain reliable as a diagnostic despite imperfect training-loss collapse.
- Extending the collapse quality metric (the r values) to a comparison with a non-collapsed baseline (e.g., Llama-2 spread) would let readers calibrate how much collapse improves beyond naive normalization.
- Adding even one early stopping experiment for a learning rate or batch size sweep would substantially broaden the generalizability of the HPO application.
- The introduction's frontier-scale motivation (where "direct experimentation disappears") should be scoped honestly to the 300M–3.9B validation range; the frontier applicability remains an open empirical question, though the µP/CompleteP framework does provide theoretical basis for cautious extrapolation.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **Harsh Critic: "Frontier-scale motivation not matched by experimental scope" as a structural flaw.** This is real but overstated as a serious weakness. The 3.9B validation range is genuine and the extrapolation is theoretically grounded; this is better handled as a scoping note in nice-to-haves. A paper validating at 3.9B is not "evidentially deficient" merely because frontier models are larger.

- **Harsh Critic: "TPP=234 and TPP=294 appear at the same point in Fig. 5."** Looking at the figure caption, both points have the same coordinates (k_N=0.38, C/C_opt=1.67), suggesting the trade-off curve is essentially flat between these TPPs—not a presentation error. Removed as a nitpick.

- **Harsh Critic: "The bias-variance model is analyzed at constant LR and only qualitatively extended to decaying schedules."** This is real but trivial—it is normal for theoretical analyses to be derived for the simplified case and qualitatively extended. Retained only as trivial.

- **Strength Finder: "Celerity serves as a clean baseline for models trained without task-specific annealing."** This is meaningful context but generic as a *strength*; it is a positioning claim rather than an evidenced contribution. Removed from strengths.

---

## Novel Insights

The paper's most generative observation—not explicit but latent in the results—is that collapse is not merely a post-hoc alignment phenomenon but a *signature of compute-efficient and correctly-calibrated training*: it emerges exactly when τ is set optimally for the given TPP, meaning models that "accidentally" fail to collapse (like Llama-2, which varies τ across sizes) are simultaneously suboptimal in their hyperparameter choices. This reframes collapse from a mathematical curiosity into a *real-time training health indicator*, blurring the line between diagnostic tool and training criterion. The paper also demonstrates, via the 1.8B case study, that collapse residuals surface issues an order of magnitude earlier in fractional training time than raw loss monitoring—a practically significant signal that has no direct analog in existing monitoring practice.

---

## Suggestions

1. **Define N(r=...) in the main text** with a clear formula and unit (ideally as RMSE or similar), and report this metric consistently across all TPP bands including 234 TPP, alongside a baseline spread for a non-collapsed family (e.g., Llama-2) for calibration.

2. **Address the CompleteP–µP gap explicitly.** Either provide an argument that CompleteP preserves the relevant scaling properties (scale-consistent curvature, EMA timescale behavior), or include a sentence acknowledging this as an empirical assumption backed by Fig. 15.

3. **Expand the 234 TPP collapse analysis.** Show held-out loss curves alongside training loss curves for the 234 TPP band, characterize when divergence appears as a function of model size, and add one or two sentences explaining when a practitioner should treat divergence as "expected overfitting" versus "potential pathology."

4. **Add at least one early stopping experiment for a non-λ sweep** (e.g., LR sweep) to demonstrate generality of the procedure beyond weight decay tuning.

5. **Soften the frontier-scale framing in the introduction.** The experiments validate at 300M–3.9B; state this range explicitly when motivating the work, and frame the frontier-scale applicability as a motivated conjecture rather than an established result.

---

## Score and Decision

**Originality:** The work builds directly on Qiu et al. (2025) but extends substantially—co-scaling width, depth, batch size, and weight decay in a realistic LLM setting, identifying new controls (τ and TPP), and developing two practical applications. Solidly incremental-to-strong.

**Importance:** High. The diagnostic and HPO applications address real pain points in frontier model training, and the systematic characterization of collapse controls is practically actionable.

**Claims supported:** Well-supported. The core empirical claims (τ and TPP control TLC shape; collapse at 300M–3.9B; early stopping works at 10–30%) are all backed by clearly presented experiments. The CompleteP–µP gap and the 234 TPP imperfect collapse are real but bounded limitations.

**Soundness:** Good. The experiments are carefully constructed, the µP framework provides theoretical grounding, and the results are consistent. The CompleteP assumption and the qualitative treatment of LR decay are the main gaps.

**Clarity:** Good. The paper is well-organized and the narrative is clear. The undefined N(r=...) metric is the main clarity gap.

**Community value:** High. The practical diagnostic and HPO tools are immediately adoptable, and the Celerity family provides a clean compute-efficient open baseline without task-specific annealing.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>