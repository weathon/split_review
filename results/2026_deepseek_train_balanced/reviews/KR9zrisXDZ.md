## Summary

This paper introduces a framework for designing variance schedules in score-based diffusion models by interpreting the inverse of a variance schedule as a CDF and its derivative as a PDF induced by a "rationale" — a weighting function over variances. The formalism allows practitioners to construct schedules from principled criteria (separability metrics, prior beliefs) rather than ad-hoc empirical design, including cases where the schedule lacks a closed-form expression (requiring numerical inverse CDF computation). The paper also reframes loss weighting as an implicit change of rationale and demonstrates empirically that using different schedules for training and sampling can improve FID.

## Strengths

- **Clean mathematical formalism unifying variance schedule design under a CDF/PDF framework.** Section 3.1 (Definition 3.1, Equations 5–8) formalizes the connection between a variance schedule's inverse and a CDF, and its derivative and a PDF. This provides a unified lens that subsumes existing schedules (e.g., the VE schedule's PDF is recovered in Equation 14 of Section 3.3.1) and gives practitioners a principled vocabulary for schedule design rather than relying purely on empirical trial-and-error.

- **Derivation of the squared L2-norm schedule from a separability rationale.** Section 3.3.2 shows that a rationale derived from the squared L2-norm between class-conditional marginals yields a CDF (Equation 15) whose inverse lacks a closed form. The paper demonstrates that the generalized inverse CDF (Equation 9) can still produce a valid schedule, and this schedule is used successfully in both training and sampling (Section 4, Tables 1–2). This concretely illustrates how the framework enables schedules that would be difficult to arrive at through direct σ(t) design.

- **Loss weighting reframed as a change of rationale.** Section 3.4 (Equations 16–18) shows that loss weighting λ(σ) is equivalent to redefining the rationale to r_λ = λ·φ_r and then sampling from the new density without explicit weighting. This is a clean conceptual simplification that makes the interaction between loss weighting and variance schedules transparent.

- **Empirical demonstration that training and sampling schedules can differ to advantage.** The cross-condition experimental design (Section 4, Figures 3–4, Tables 1–2) tests all combinations of three rationales for training and sampling. The finding that the best FID scores are achieved by training with squared L2-norm and sampling with the Gaussian schedule — despite the Gaussian schedule performing poorly during training — is a non-trivial empirical result.

- **Controlled experimental setup isolating the effect of rationales.** Section 4.2 specifies identical architecture, optimizer, EMA rate, and sampler across all conditions, making comparisons fair and reproducible.

## Weaknesses

### Fatal
None.

### Major

- **Missing the most directly relevant baseline.** The paper extensively cites Karras et al. (2022) — which is the most closely related prior work on designing and analyzing variance schedules in driftless diffusion models — and even states it can "provide the underlying rationale" of the Karras et al. schedule (line 167). Yet the experiments compare only against VE (Song et al., 2020) and exclude the Karras et al. schedule as a baseline. The paper's justification — "no hyperparameter selection is required" for VE (line 167–168) — does not hold: the Karras schedule can be used with its default recommended hyperparameters, exactly as the paper does for other schedules. This omission means the experiments cannot answer the question a reader most wants answered: *does the rationale perspective produce schedules that outperform a standard modern alternative?* The paper's claims of "notable improvements" (abstract) are calibrated only against VE, which is not a state-of-the-art baseline.

### Minor

- **The evaluation scope is narrow.** Experiments are limited to two datasets at 32×32 resolution, a single sampler (Euler-Maruyama, 1000 steps), and three rationales. There is no evaluation at higher resolutions (e.g., ImageNet-64, LSUN), with modern fast samplers (DPM-Solver, DDIM, Heun), or against published SOTA numbers. While this is acceptable for a methods paper introducing a conceptual framework, it limits the generality of the conclusions — in particular, the finding about mixing training/sampling schedules may be an artifact of the SDE solver's discretization properties.

- **The "unattainable through conventional methods" claim (abstract, line 22) is inflated.** The squared L2-norm schedule requires numerical computation of its inverse CDF because the CDF lacks a closed-form inverse. However, one could equivalently define the same σ(t) values numerically without the CDF framework — the schedule is not mathematically new, only inconvenient to express in closed form. The framework's value lies in providing a principled *derivation path* (starting from a separability metric), not in enabling schedules that are mathematically impossible to define otherwise. The language should be calibrated to reflect this.

- **Tension between the abstract and the experimental framing.** The abstract claims "notable improvements in image generation performance, as measured by FID," while Section 4.2 states "the experiments was not to tweak a specific rationale to achieve state-of-the-art performance ... but rather comparing the baseline performance of rationales relative to another." If the evaluation is intentionally excluding the tweaks needed for competitive performance, the "notable improvements" claim should be explicitly scoped to the tested baselines rather than stated in absolute terms.

- **No sensitivity analysis for the Gaussian rationale's σ_N parameter.** The Gaussian rationale is presented as "of particular interest for a parameterized variance schedule that can be tuned to different data-domains" (line 193), yet σ_N is fixed to 5 throughout with no justification or sweep (line 248). A simple ablation showing how performance varies with σ_N would be informative.

- **The finding that training and sampling can use different schedules, while valid, is not analyzed.** The paper shows that training with squared L2-norm and sampling with N(0,5²) yields the best FID, but provides no investigation into *why* this combination works (e.g., whether the squared L2-norm oversamples intermediate variances during training, improving score estimation there, while the Gaussian avoids discretization error at high variances during sampling). Without analysis, the result remains a narrow empirical observation rather than a generalizable principle.

- **Loss weighting result is reframed, not discovered.** Section 3.4 correctly shows that loss weighting can be re-expressed as a change of rationale. However, Karras et al. (2022) already demonstrated that loss weighting changes the effective noise distribution during training. The paper's reformulation is internally consistent and pedagogically useful, but presenting it without explicit acknowledgment of this prior understanding overstates its novelty.

### Trivial

- The paper uses the term "Smirnov transform" (Section 3.1), which is more commonly known as inverse transform sampling or the probability integral transform in statistics. This may confuse readers.

## Nice-to-Haves

- An analysis of *why* mixing the squared L2-norm training schedule with the Gaussian sampling schedule works — e.g., ablating the interaction between sampler discretization and variance schedule, or testing ODE-based samplers to see if the finding transfers.
- A sensitivity sweep for the Gaussian rationale's σ_N parameter.
- A comparison against the Karras et al. (2022) schedule as an additional baseline.

## Removed Points

These points were removed from the inputs for the following reasons:

1. **Harsh Critic's Claim 1 (reparameterization = no new capability, "simply incorrect")** — Downgraded from fatal/structural to minor. The mathematical observation is indeed a reparameterization (inverse transform sampling), and any schedule expressible via the framework is expressible directly. However, the paper's value is in providing a principled *derivation path* (starting from meaningful criteria like separability), not in expanding the mathematical set. The "unattainable" claim is inflated but not "simply incorrect" — the squared L2-norm schedule cannot be expressed as a simple closed-form σ(t) function, which is what "conventional methods" typically produce.

2. **Harsh Critic's "the paper should not be accepted in its current form"** — This is an overall judgment call that I have factored into my own assessment rather than treating as a standalone weakness.

3. **Strength Finder's generic strengths** — Several strengths in the Strength Finder were generic ("addressed an important problem," "provides a unified approach"). I retained only strengths that are specific, concrete, and evidenced in the paper.

4. **Criticism about missing appendix content (derivations, proofs)** — The appendix is stripped by the parser; such criticisms are invalid per instructions.

5. **"The framework does not yield a new practical capability" (Harsh Critic, Claim 3)** — The paper does use the framework to derive the squared L2-norm schedule, which is used in experiments. This is a practical capability, even if modest.

6. **Criticism about conditioning on σ not being novel** — The paper attributes this to Karras et al. (line 287). It does not claim novelty here; it uses this technique as a tool for its experiments.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the Karras et al. (2022) schedule as an experimental baseline.** This is the single most important improvement. The paper cites Karras et al. as the most closely related prior work on schedule design, and a fair comparison is essential to establish whether the rationale framework produces practically superior schedules.

2. **Calibrate the language.** The claim that the squared L2-norm schedule is "unattainable through conventional methods" should be softened to clarify that it is unattainable *in closed form* via direct σ(t) design, but the schedule itself is not mathematically extraordinary. Similarly, "notable improvements" should be scoped to the baselines actually tested.

3. **Add a brief analysis or at least a hypothesis for why mixing training/sampling schedules works.** Even a short paragraph discussing possible mechanisms (e.g., differences in discretization error profiles) would transform the empirical observation into a more actionable finding.

4. **Sweep the Gaussian σ_N parameter.** Since the Gaussian rationale is presented as tunable, showing performance for at least 2–3 values of σ_N would demonstrate the utility of the tuning knob.

## Score and Decision

The paper introduces a clean and mathematically sound formalism for thinking about variance schedules in terms of their induced density over variances. The conceptual reframing has genuine pedagogical value and the squared L2-norm schedule demonstrates a useful application of the framework. However, the experimental evaluation has a decisive gap: the omission of the Karras et al. (2022) schedule as a baseline means the paper cannot substantiate its stronger claims relative to contemporary practice. Combined with the inflated language ("unattainable," "notable improvements" without proper scoping) and the narrow evaluation scope, the paper falls short of the standard for ICLR acceptance in its current form. A major revision addressing the baseline gap, calibrating claims, and broadening the evaluation would make it competitive.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>