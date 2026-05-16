Now I have all the information needed to write the consolidated review. Let me synthesize everything carefully.

## Summary

The paper proposes a method to refine pretrained flow-based posterior estimators for simulation-based inference by introducing a small control network that injects simulator feedback (gradients/cost or learned encoder outputs) during finetuning while the flow weights remain frozen. The approach is evaluated on standard SBI benchmarks and a challenging strong gravitational lensing inverse problem, where it matches or exceeds MCMC-based inference while being substantially faster.

## Strengths

- **Simulator feedback demonstrably outperforms scaling training data alone**: On the Lotka-Volterra task, increasing the training dataset from 10⁵ to 10⁷ samples yields no C2ST improvement, yet the proposed feedback method (using ~9×10⁶ simulator calls for finetuning, fewer total calls than the 10⁷ baseline) achieves clearly better C2ST scores (Section 5.4, Figure 4/5). This directly supports the claim that directed simulator feedback cannot be replaced by more data.

- **Competitive with MCMC on a challenging real-world inverse problem while being drastically faster**: On strong gravitational lensing, flow matching with gradient-based control achieves an average χ² of 1.48, surpassing both NUTS (1.83) and AIES (1.74), while requiring only 19s for 1000 posterior samples versus 564s–672s for MCMC (Table 2, Section 6.1). The method delivers on its central promise of combining high accuracy with fast amortized inference.

- **Isolates the effect of simulator feedback by testing related training variants**: Self-conditioning, independent couplings, and x-prediction all fail to improve upon vanilla flow matching on SBI benchmarks (Section 5.2, Figure 3). This careful ablation confirms that only explicit simulator feedback yields gains, not any architectural or loss modification.

- **Provides solutions for both differentiable and non-differentiable simulators**: Both gradient-based control (using cost and gradient) and learning-based control (using an encoder on simulator output) are evaluated on the LV task, with the learning-based version also improving C2ST (Section 5.3, Figure 4). This broadens applicability to realistic settings where simulators may not be differentiable.

- **Theoretical correctness preserved**: The paper argues that the controlled flow network uses the same conditional flow matching loss as vanilla flow matching, with the control signal being a deterministic function of θ_t, so all theoretical properties of flow matching are maintained (Section 4.2).

## Weaknesses

### Fatal
None.

### Major
None. The core contribution is sound and empirically supported.

### Minor

- **Ambiguous framing of the 53% improvement (Abstract, Section 6.1)**: The abstract states "improves the accuracy by 53%" without context. In the main text (line 311), the improvement is clarified as a 53% reduction of the gap between the model χ² and the noise floor (1.17), not a 53% absolute improvement in χ² (which would be a 1.83→1.48 = 19% relative decrease). The abstract's phrasing is imprecise and could mislead readers. This is a presentation issue, not a methodological flaw, and is easily corrected.

- **DPS baseline included without explanation (Table 2)**: Diffusion Posterior Sampling (DPS) is listed with χ²=9.98 — far worse than all other methods. The paper provides no description of how DPS was implemented, what architecture was used, or how it was adapted to this parameter inference problem. DPS is designed for image reconstruction with known forward operators, not scientific parameter inference, so its poor performance is unsurprising and its inclusion without explanation undermines rather than strengthens the evaluation. The main comparisons (NUTS, AIES) do not depend on DPS, so this is a minor presentation issue.

- **No error bars or measures of variability (Tables 1, 2; Figures 3, 4, 6)**: C2ST scores, χ² values, and computational efficiency metrics are reported as point estimates without confidence intervals, standard deviations, or any indication of variability across runs. Given that some reported differences are small (e.g., C2ST of 0.93 vs 0.88 for different control variants on LV), the reader cannot assess whether these improvements are stable or idiosyncratic to a particular training run. This is common in the SBI benchmark literature, but reporting standard errors over 3–5 seeds would substantially strengthen the paper.

- **Time-dependence threshold (t > 0.8) is not ablated (Section 4.2)**: The choice to train the control network only for t > 0.8 is intuitive but arbitrary. No sensitivity analysis is provided for this threshold. An ablation varying this cutoff (or training on all t) would help readers understand how critical this design choice is.

- **Simulation-based calibration shown for only one of 23 parameters (Section 6)**: SBC histograms are only visualized for the x_center parameter. While this parameter is illustrative, the paper would benefit from stating what fraction of the 23 parameters pass a uniformity test, or at minimum showing a few more representative parameters.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis on the t > 0.8 masking threshold to show how performance varies with this choice.
- A brief explanation (1-2 sentences) in the caption of Table 2 clarifying that DPS is adapted from image reconstruction and is not expected to be competitive on parameter inference, to avoid confusion.
- Reporting results over 3-5 random seeds with error bars for at least the main C2ST and χ² metrics.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No comparison to likelihood-guidance or other inference-time correction methods empirically"** — Scope creep. The paper proposes a specific method (control network finetuning with simulator feedback), not a comprehensive benchmark of all guidance approaches. The conceptual comparison with likelihood-guidance in Section 4 suffices for positioning.

- **"SBI results not contextualized against best known results from Lueckmann et al. 2021"** — Not supported by evidence. Table 1 shows flow matching is already best or tied for best on 2 of 4 tasks (LV, SLCP) and close to best on the remaining 2 (SIR, TM) against CNF, NSF, and FFJORD — standard NPE baselines.

- **"Computational efficiency comparison is not on equal footing"** — The opposite is true. The feedback method uses ~9.1×10⁶ total simulator calls (10⁵ for pretraining + 9×10⁶ for finetuning) versus 10⁷ for the scaling baseline. The comparison is conservative and actually favors the paper's case.

- **"Zero Controls baseline improvement not discussed enough"** — The paper explicitly addresses this (line 267): "The zero control signal improves only slightly, showing that the improvement can be directly attributed to the simulator."

- **"Missing hyperparameters and reproducibility details"** — The paper references Wildberger et al. for optimal hyperparameters, describes architecture sizes (~300K weights for small networks, control network = 11% of total parameters), and the overall budget. This meets the standard for the field.

## Novel Insights

The most significant insight across the reviews is that the paper's contribution is best understood as an **efficiency intervention for the data-compute frontier in SBI**: the strong lensing experiment shows that a modest finetuning step (11% additional parameters, ~9×10⁶ simulator calls) can close the gap between amortized neural posterior estimation and gold-standard MCMC — a gap that naive data scaling (increasing training data 100×) cannot close. The "Zero Controls" baseline revealing a small improvement (even without real control signals) is underexplored and hints that the finetuning procedure itself, not just the control signal, may contribute. Finally, the combination of differentiable simulator feedback with a frozen pretrained flow is conceptually clean and avoids the training instabilities that joint end-to-end training would introduce.

## Suggestions

- **Fix the 53% claim in the abstract.** Replace "improves the accuracy by 53%" with a precise description, e.g., "reducing the gap between the model χ² and the irreducible noise floor by 53%."
- **Either remove the DPS baseline or add 2–3 sentences describing how it was applied and why its poor performance is expected.** If the authors keep it, they should note that DPS is designed for a different problem class.
- **Add standard deviations or confidence intervals for the main results.** Even 3 seeds for the C2ST and χ² numbers would significantly improve the paper's credibility.
- **Add a brief ablation of the t > 0.8 threshold** (or at minimum a justification based on pilot experiments).
- **Expand the SBC analysis** to report pass rates on a uniformity test across all 23 parameters.

## Score and Decision

This paper presents a well-motivated, practically relevant method that demonstrably improves posterior inference accuracy on both benchmark and real-world scientific problems. The core contributions are sound, the experimental evidence supports the main claims, and the strong lensing application is compelling. The weaknesses are primarily presentation issues and missing statistical detail rather than methodological flaws. The paper would benefit from revision but its contribution is real.

**Score**: 6.5

**Decision**: Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>