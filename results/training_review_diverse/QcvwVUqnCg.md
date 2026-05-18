Now I have a thorough understanding of the paper and all the reviewer inputs. Let me compose the final consolidated review.

## Summary

This paper proposes a normative reinforcement learning model where TD-error-driven updates to place field parameters (amplitude, center, width) — alongside actor-critic weights — reproduce three canonical place field phenomena under a single reward-maximization objective: high field density at reward locations, backward field elongation against movement direction, and representational drift with stable behavior. The model is analyzed through perturbative approximations, ablations, comparisons with the successor representation, and drift experiments, and the authors show that noisy field updates improve new-target relearning.

## Strengths

- **Unification of three disparate phenomena under a single normative framework.** Prior work proposed separate mechanisms for reward-density emergence, field elongation, and representational drift. This paper demonstrates that all three arise from a single TD-error-driven reward maximization objective (Figs. 1–3), which is a genuinely novel synthesis.
- **Analytical perturbative approximation for field dynamics.** The paper derives closed-form approximations (Eqs. 6–7; App. B) showing that field center shifts scale with squared critic weights and amplitudes scale with value. This gives mechanistic insight beyond purely phenomenological models and is validated against simulations (Fig. 1E–F).
- **Testable distinction from successor representation dynamics.** The paper directly compares RM and SR agents and shows they diverge early (anti-correlated mean firing rates, Fig. 2C–D) before converging later (Fig. 2E), providing an experimentally testable prediction about the time course of field reorganization.
- **Demonstration of a functional role for representational drift.** Noisy field parameter updates degrade population vector correlation while keeping behavior stable (Fig. 3B–C), and importantly, an optimal noise magnitude improves new-target learning (Fig. 4C) — suggesting drift is not merely an epiphenomenon but may serve a computational role in preventing fixation on outdated reward locations.
- **Systematic ablation of field parameters.** The paper decomposes the contribution of each field parameter (width, amplitude, center) to policy convergence (Fig. 4A–B), finding that width optimization provides the largest benefit while center optimization contributes least in the single-target case — a nontrivial decomposition.

## Weaknesses

### Fatal
None.

### Major

- **The gradient-based learning rule for place field parameters is biologically implausible and the gap is not bridged.** The core mechanism — updating α, λ, σ by backpropagating the TD error through the actor and critic — requires each place field to have access to downstream weights and compute precise gradients. The authors explicitly acknowledge this in the Discussion and frame the model as normative rather than mechanistic. However, the value of a normative model depends on whether the proposed objective *could plausibly* be optimized by a neural circuit. The paper provides no sketch of how such gradients could be approximated by local, biologically plausible plasticity rules (e.g., eligibility traces, three-factor rules, feedback alignment). Since the paper's central contribution is to explain *why* place fields reorganize (reward maximization), the lack of a bridge to *how* this optimization could be implemented limits the model's claim to be a neuroscientific account of place field plasticity. The paper's experimental predictions (e.g., disrupting dopamine affects reorganizations) depend on the gradient mechanism holding, making this a structural gap rather than a mere simplification.

- **The functional role of field center reorganization is unresolved and creates a tension with the ablations.** The ablation results (Fig. 4A–B) show that center optimization does not improve single-target navigation performance and even harms it when combined with amplitude optimization. Yet center shifts toward reward locations are one of the hallmark phenomena the paper aims to explain (Fig. 1B, 1E, 2A–B). The paper does not resolve whether these center shifts are (a) causally beneficial for new-target learning (Fig. 4C tests noisy *all-parameter* updates, not center updates specifically) or (b) a non-functional byproduct of gradient descent. An ablation that disables center updates during new-target learning (while keeping width/amplitude updates) would resolve this, but is not provided. This undermines the claim that place field reorganization "improves policy convergence" as a unified advantage, since the most conspicuous experimentally observed feature (center shifts) appears functionally neutral or detrimental in the single-target setting the model studies most.

### Minor

- **The SR comparison compares different types of learned objects.** The paper compares learned *basis functions* (RM's place fields φ) against learned *weights on fixed basis functions* (SR's successor features ψ), following Stachenfeld et al. (2017). While this follows prior methodology, it conflates two different levels of representation. The finding that their dynamics differ (Fig. 2C–E) is interesting but does not directly inform whether a *true* SR with learnable nonlinear basis would behave differently from RM. The paper should clarify this distinction and temper the claim about the two algorithms being distinguishable by experiments.
  
- **The perturbative approximation fit is acknowledged as moderate but not systematically characterized.** The paper notes that "additional approximations are needed to model the agent's trajectory and improve the simulation-theory fit for place field centers" (App. B). However, no quantification of the approximation error is provided (e.g., R² values, error bars on theory vs. simulation across parameter regimes), which would help readers assess how reliable the analytical insights are.
  
- **The noise injection mechanism for drift is not learned or controlled.** Gaussian noise is injected directly into field parameter updates (Section 4.3). The paper acknowledges this is a phenomenological choice rather than a learned mechanism. While this is acceptable as a first step, the finding that noise helps new-target learning (Fig. 4C) is then less surprising — noise is a known regularizer in continual learning. The paper would benefit from discussing how this relates to other anti-forgetting mechanisms (e.g., elastic weight consolidation, replay).

### Trivial
- The paper uses a single set of place fields for both actor and critic, which simplifies the anatomy (separate pathways to dorsal/ventral striatum). The Discussion notes this, but the paper does not analyze potential conflicts where a change that benefits policy could harm value estimation.

## Nice-to-Haves
- **Quantitative comparison to experimental data.** The paper references Sup. Fig. 9 for comparisons to data, but a summary table of key measurements (e.g., peak density ratio near reward vs. start, average shift distance, drift rate) alongside published values would make the claim of recapitulation much stronger and more useful to experimentalists.
- **Test with binary (all-or-nothing) reward.** The Gaussian reward distribution simplifies boundary effects; testing whether the phenomena hold for a binary reward (which is common in experiments) would increase robustness.
- **Binary reward condition testing.** Testing whether the phenomena hold for a binary (reward/no-reward) schedule as used in many rodent experiments would increase ecological validity.
- **Center-specific ablation in new-target setting.** Running the new-target learning experiment (Fig. 4C) with center updates disabled while keeping width/amplitude/noise updates would directly test whether center shifts are causally responsible for improved relearning.

## Removed Points

These points were flagged by reviewers but are removed or downgraded after verification against the paper:

- **"The paper does not explain why the weak feature learning regime occurs."** — The paper does state: "This is because as the number of fields increase, the agent goes into a weak feature learning regime (Sup. Fig. 4) in which feature learning does not contribute to additional advantage." While the mechanistic explanation is brief, the paper identifies the regime and references the appendix. This is too minor to retain as a weakness.
- **"The paper should test binary reward."** — This is scope creep; the paper's Gaussian reward is a defensible design choice and testing binary reward would expand rather than strengthen the paper's existing self-contained narrative.
- **"The paper does not compare the model's predictions to any quantitative experimental data."** — The paper references Sup. Fig. 9 for data comparisons and provides qualitative matches to published phenomena throughout. A quantitative table would be a nice addition but its absence is not a core weakness.

## Novel Insights

The most penetrating observation to emerge from the reviews is the unresolved tension between center shifts as a hallmark experimental phenomenon and their minimal (or negative) contribution to single-target reward maximization in the model. This forces a sharp question about the model: either (i) center shifts serve a computational role that only manifests in dynamic, multi-target environments (which the new-target experiment hints at but does not causally verify for centers alone), or (ii) they are a non-functional byproduct of gradient-based optimization — which would itself be a noteworthy prediction (experimental manipulation of centers might not impair behavior on stationary reward tasks). The paper currently leans toward (i) but does not provide the ablation experiment needed to distinguish (i) from (ii). This is the single most important direction for strengthening the paper's claims.

## Suggestions

- Add an ablation experiment in the new-target setting (Fig. 4C) that disables center updates while keeping width, amplitude, and noise updates. If the no-center condition shows slower adaptation, center shifts are causally functional; if not, state explicitly that centers are a non-functional byproduct — either outcome is informative.
- Add a brief simulation or discussion showing how the gradient updates for place field parameters could be approximated by a biologically plausible rule (e.g., an eligibility trace combining d log π/dθ with the TD error, or a three-factor rule with TD error as a global neuromodulator). Even a noisy approximation that produces qualitatively similar dynamics would substantially address the biggest limitation.
- Provide quantitative bounds for the RM-vs-SR experimental predictions: estimate how many trials and neurons would be needed to detect a statistically significant difference in the correlation dynamics (Fig. 2D–E). Order-of-magnitude estimates would make the predictions actionable for experimentalists.
- Add a table comparing key experimental measurements (field density ratio at reward vs. start, mean shift distance, PV correlation decay rate) to published values from Gauthier & Tank (2018), Mehta et al. (1997), Ziv et al. (2013), and Geva et al. (2023).

## Score and Decision

This paper makes a genuine and nontrivial contribution: it is the first model to unify three well-known place field phenomena under a single reward-maximization framework, supported by thoughtful ablations, analytical approximations, and testable predictions. The weaknesses are real — particularly the biological implausibility of the gradient updates and the unresolved functional role of center shifts — but the paper is transparent about its limitations and frames itself honestly as a normative model. The work is likely to stimulate both theoretical and experimental follow-up. On balance, the strengths outweigh the weaknesses.

**Originality:** High — first normative unification of three phenomena. **Importance:** High — addresses fundamental questions about place field plasticity. **Claims supported:** Mostly, with gaps in center function and biological plausibility. **Soundness:** Solid simulations and analyses. **Clarity:** Well-written. **Value:** High for computational neuroscience.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>