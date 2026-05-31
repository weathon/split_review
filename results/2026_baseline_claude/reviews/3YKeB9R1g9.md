## Summary
The paper extends the "training loss curve collapse" phenomenon (first shown by Qiu et al., 2025 on small-scale autoregressive tasks with vanilla Adam) to practical LLM training that co-scales width, depth, batch size, learning rate, and weight decay. The authors identify three scale-invariant controls governing the shape of normalized training loss curves (TLCs): the AdamW timescale τ, the tokens-per-parameter ratio (TPP), and the learning-rate schedule. They show collapse occurs precisely when τ is set optimally for the given TPP, and demonstrate this is a hallmark of compute-efficient training. They introduce **Celerity**, an LLM family (300M–3.9B parameters) that operates in the collapse regime, and demonstrate two practical applications: (1) collapse residuals as an early diagnostic of training pathologies, and (2) a small-scale surrogate model enabling early stopping in hyperparameter tuning at 10–30% of training.

---

## Strengths

- **Bridging theory and scale.** Qiu et al. (2025) explicitly requested validation at "larger scales with practical scaling ladders." This paper directly answers that call, demonstrating collapse across ∼100M–3.9B parameters with full co-scaling of depth, batch size, and weight decay. The experiments are methodical: three separate figures systematically ablate τ, TPP, and their interaction.

- **Conceptual clarity of τ as the master control.** The insight that τ = 1/(ηλT) unifies learning rate, weight decay, and batch size into a single bias-variance trade-off dial is clean and well-motivated. Fig. 3 compellingly shows that sweeping η, λ, or B independently produces the same TLC shape when τ is held constant—an elegant experimental design that makes the causal chain clear.

- **Concrete real-world debugging impact.** The 1.8B training run case study (Figs. 1 right and 6 right) is one of the paper's most compelling moments: collapse residuals revealed a numerical instability at 60% of training, 30 percentage-points earlier than the raw loss curve would have. This is not hypothetical—the authors explain the root cause (microbatch-size-specific loss kernel bug) and show the repaired run tracking the reference. This provides strong evidence of practical utility.

- **Early stopping validated on real sweeps.** Figure 9 demonstrates that the proposed procedure selects the correct winner (by final loss) after just 10–30% of training for both 1.7B and 3.3B sweeps, outperforming the naïve "current best" approach which fails at 1.7B. The parametric surrogate (Eq. 4–5) is fit on 111M-scale data and successfully extrapolates to 3.3B, offering a >1000× compute amortization.

- **Theoretical grounding.** The noisy quadratic model (Eq. 3) provides a principled derivation of why τ modulates the bias-variance trade-off and why TLCs obey consistent shape under normalization. The explanation for TPP via neural power laws (Appendix B.2) is also consistent with the standard scaling literature.

- **Competitive model.** Celerity achieves the compute-accuracy Pareto frontier among open models at its scale (Fig. 2), including a 75% compute saving over BTLm at comparable accuracy. This validates collapse as a practically useful training principle, not just a theoretical curiosity.

---

## Weaknesses

### Fatal
None.

### Major

1. **Imperfect collapse in the most inference-efficient regime (234 TPP).** The paper acknowledges that "At 234 TPP, divergences appear late in training for larger models" (Fig. 1, middle), attributing this to in-distribution overfitting while held-out data remains aligned. However, this is precisely the regime the authors designate as the practical operating point for Celerity (62% parameter reduction). Late-training divergence in the collapse residuals for larger models in this regime is non-trivial: it means the diagnostic signal is confounded. The paper does not characterize the frequency or severity of this phenomenon, nor does it provide a principled explanation. This weakens the claim that collapse is a reliable diagnostic in the 234 TPP setting.

2. **Scale ceiling at 3.9B leaves frontier applicability uncertain.** While the paper's framing targets "very large model" pre-training and mentions "billion-dollar runs," the empirical validation tops out at 3.9B parameters. The jump from 3.9B to the 70B–700B frontier represents 2–3 orders of magnitude more compute and qualitatively different engineering challenges (e.g., pipeline parallelism, data parallelism artifacts). It is plausible that collapse holds at larger scales, but this remains unverified. The practical claims about monitoring frontier runs rest on extrapolation.

### Minor

1. **LR warmup breaks collapse at 20 TPP.** Early deviations at 20 TPP (Fig. 6, left) are attributed to different warmup proportions across model sizes, but Table 2 shows warmup is not individually tuned per model. This means any real deployment of the diagnostic procedure requires either careful warmup equalization or ignoring the first 10%+ of training—a practical limitation that warrants more explicit treatment.

2. **The early-stopping procedure is not fully self-contained.** Steps 1–3 of the proposed HPO protocol require training small-scale reference models for each unique combination of TLC controls. For teams without existing collapse infrastructure, this adds a prerequisite cost. The paper does not estimate or discuss this overhead relative to the savings.

3. **Claim that collapse requires optimality of τ is not precisely characterized.** The paper states collapse "emerges as a signature of compute-efficient training" and requires τ to be "optimal." But collapse is demonstrated at τ values that are simply held constant across sizes, not necessarily globally optimal for each TPP. The relationship between τ-optimality and collapse tightness (as a quantitative function of the sub-optimality of τ) is left implicit.

### Trivial
None identified beyond parser artifacts.

---

## Nice-to-Haves
- A table quantifying the RMS residual of collapse at each TPP band (20, 80, 234) across model sizes would make the "tightness" claim precise and comparable across settings.
- A discussion of how often training instabilities realistically occur in well-managed runs, to contextualize the practical frequency with which the diagnostic application would be invoked.
- A sensitivity analysis on the power law parameters used in the iso-loss compute-vs-compression analysis (Fig. 5), since the choice of 234 TPP as the operating point depends on these fits.

---

## Novel Insights
The paper's most novel synthesis is the reframing of AdamW's (η, λ, B) triad as a single normalized scalar τ = B/(ηλD), which captures the optimizer's effective memory length relative to the training run. This view unifies seemingly unrelated hyperparameter choices under a single control variable and explains—with theoretical backing from a noisy quadratic model—why TLCs are shape-invariant across scales when τ is matched. The corollary that collapse is a *signature* (not just a consequence) of compute-efficient training—because optimal τ depends only on TPP and both are held constant in a well-designed recipe—is a particularly clean and actionable observation. The connection between collapse breakdown and training pathologies as a diagnostic tool extends this insight to a practical monitoring framework that quantifies deviations from expected trajectories, a significant advance over current practice which relies on subjective visual inspection of raw loss curves.

---

## Suggestions
- **Characterize 234 TPP collapse degradation quantitatively.** Provide collapse residuals as a function of training fraction for each model size at 234 TPP and analyze whether the late-training divergence correlates with data repetition metrics or gradient statistics.
- **Add an ablation where warmup is equalized.** Fix LR warmup as a constant proportion across all model sizes and show whether early-training collapse at 20 TPP tightens; this would clarify whether the observed deviations are fundamental or engineering artifacts.
- **Validate on one larger scale.** Even a single 7B experiment would substantially strengthen the frontier applicability claim. If computational constraints prohibit this, explicitly bound the claims to the validated range.
- **Discuss what happens when τ is suboptimal by a known factor.** A plot of collapse residual norm vs. τ sub-optimality would help practitioners know how carefully τ must be tuned for the diagnostic to remain reliable.

---

## Score and Decision

This is a solid empirical paper that makes a genuine and useful contribution: it extends an important regularity (TLC collapse) to practical LLM training and demonstrates two concrete applications with real evidence. The core claims are well-supported, the experiments are methodical, and the Celerity model validates the approach on downstream benchmarks. The main limitations—imperfect collapse at the highest-TPP regime and scale ceiling at 3.9B—are real but do not invalidate the core contribution. The work provides actionable insights for LLM practitioners and a principled framework for understanding why training loss curves behave as they do.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>