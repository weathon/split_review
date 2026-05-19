- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 3, 5
Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper studies learning in flow-based generative models for high-dimensional two-mode Gaussian mixtures. It identifies that the phase where the mode probability is learned collapses as dimension grows (speciation time ∼ 1/√d → 0), proposes a time-dilation schedule that stretches the early-time interval to prevent this collapse, and provides a heuristic (replica-style) asymptotic characterization of the learned velocity field parameters. The key results show a two-phase learning structure: the first phase captures the mode probability, the second captures the within-mode variance. The authors validate the dilation idea on a Gaussian mixture simulation (Figure 1) and propose a practical oversampling method for real data tested on MNIST.

## Strengths

- **Well-motivated problem and clean theoretical setup.** The paper clearly identifies a genuine issue: the phase where high-level structure (mode probability) is learned vanishes as d → ∞ under standard linear schedules. The proposed time dilation (piecewise-linear τ(t) stretching [0, κ/√d] to [0,1]) is a principled fix, and Proposition 1 formally shows it restores two distinct phases in the generative process. This is a clean, non-obvious theoretical insight.

- **Asymptotic characterization of the learned parameters in each phase.** Results 1 and 2 (though heuristic) provide concrete closed-form equations for the overlap parameters of the two-layer autoencoder in the d→∞ limit. Corollaries 1 and 3 cleanly show that the first phase's learned parameters depend only on p (not σ²) and the second phase's depend only on σ² (not p), demonstrating the autoencoder's ability to "simplify" by feature-relevant estimation per phase.

- **Well-designed Gaussian mixture simulation (Figure 1).** The experiment directly tests the central claim: it trains the actual two-layer autoencoder from Eq. 7 on a high-dimensional Gaussian mixture (d=5000, p=0.8, n=128), compares the dilated vs. non-dilated schedules, and shows that the dilated schedule correctly estimates p ≈ 0.8 while the non-dilated schedule collapses to a value near 0.5. This is direct, within-model validation of the core theoretical idea.

- **MSE-based phase transition detection insight.** Corollary 5 shows that the test MSE takes distinct constant values at different phases with a smooth transition across the dilated interval, suggesting a general method for identifying phase transitions in arbitrary data — an insight that is well-grounded in the theoretical analysis.

## Weaknesses

### Fatal

None.

### Major

- **Heuristic theoretical results are presented as more definitive than warranted.** Results 1 and 2 are explicitly derived using non-rigorous replica calculations ("at the level of rigor of theoretical physics"), noted only in their captions. Yet the abstract ("we give an asymptotic characterization," "we show that the neural network learns to simplify"), introduction, and subsequent claims (Corollaries 1–6, Result 3's O(1/n) error bound, Corollary 6's conclusion about correct parameter estimation) are all framed as settled characterizations without accompanying caveats. A reader unfamiliar with replica theory would reasonably believe these are mathematically proven. For a machine learning venue, the heuristic status should be clearly stated in the abstract and introduction, and conclusions drawn from heuristic calculations should be appropriately qualified. This is a framing/rigor gap, not a fatal flaw, but it needs to be addressed for publication.

- **Disconnect between the theoretical dilation and the practical method.** The theory proposes changing the *generative process itself* (a specific τ(t) dilation in α_t, β_t) to make the first phase non-vanishing. The practical MNIST method, however, does not use this dilation — it keeps the standard schedule and instead *oversamples training times* near the critical interval identified by U-Turn. These are different interventions (changing the generative schedule vs. changing the training-time distribution), and the paper does not explain how one translates to the other or why oversampling training times should be equivalent to dilating the generative process. The paper simply states "the insight of our analysis is that... we can sample more times near the phase transition" (line 356), but this leap is not justified. Either a formal connection should be provided, or the practical method should be framed as a separate (independently motivated) heuristic.

- **MNIST experiment lacks statistical rigor and baselines.** The MNIST validation reports single numbers (e.g., 88.2% 0s for uniform, 81.0% for oversampling [0.3,0.5]) with no error bars, no mention of multiple seeds or runs, and no assessment of statistical significance. Additionally:
  - No comparison with alternative schedules (cosine, learned, or simply training the uniform schedule for more epochs).
  - No comparison with simple post-hoc corrections (e.g., reweighting generated samples by class probability).
  - Only one feature (digit identity 0 vs. 1) is tested, on one dataset, with one asymmetry ratio (80/20).
  - No evaluation of whether oversampling degrades other quality metrics (e.g., FID, sample diversity, accuracy on other digits).
  The improvement from 88.2% to ~81% is suggestive but, as presented, does not provide strong evidence that the method reliably corrects class probabilities.

### Minor

- **No direct test of the dilated generative schedule on real data.** The theory's proposed τ(t) dilation (Eq. 12) is tested only on the Gaussian mixture simulation (Figure 1). The MNIST experiment tests a different procedure (oversampling training times). Testing the exact dilated schedule on a real dataset (or even on the GM with a more complex architecture) would substantially strengthen the claim that the theory translates to practice.

- **Order of limits in Corollary 6 is stated but not justified.** Corollary 6 takes lim_{κ→∞} lim_{n→∞} lim_{d→∞} for the p-recovery result but lim_{n→∞} lim_{d→∞} for the σ²-recovery result. The order of limits matters (especially d→∞ before n→∞), and the paper does not discuss why this specific order is appropriate or what it means physically. This is a clarity gap.

- **Sensitivity of U-Turn not explored.** The U-Turn method identifies the critical interval using a pre-trained model. The paper does not discuss how sensitive the identified interval is to the quality of this pre-trained model, the number of U-Turn samples, or the choice of threshold. If the identified interval depends heavily on the initial model, the practical pipeline may be fragile.

### Trivial

None.

## Nice-to-Haves

- Comparison with the cosine schedule on MNIST (which also weights early times more heavily).
- Reporting FID or diversity metrics alongside class-proportion accuracy to verify that oversampling does not degrade sample quality.
- Sensitivity analysis for the U-Turn method parameters.
- A formal connection (or at least a clear discussion) linking the theoretical time dilation to the practical oversampling approach.

## Removed Points

- **Criticism about formatting issues in Eq. 12 (missing bracket):** Removed — this is a PDF extraction artifact, not an author error.
- **Criticism about missing appendix/proofs:** Removed — the parser strips these; they exist in the original submission.
- **Criticism's suggestion #1 ("Provide a direct test of the theoretical model itself"):** Removed — Figure 1 *already does exactly this*: it trains the two-layer autoencoder on a high-dimensional GM (d=5000, p=0.8, n=128) with dilated vs. non-dilated schedules and measures recovered p. The critic appears to have missed or undervalued this experiment.
- **Generic one-size-fits-all criticisms** (requesting larger dataset, more model variants): Removed — the current experimental scope is adequate for a theory-driven paper; the issues that remain (error bars, baselines, disconnect) are specific and substantive.
- **Strength about MNIST as "practical validation":** Demoted/removed from Strengths as listed — the MNIST experiment is too thin to count as a strong point, and keeping it as a strength would conflict with the verified weaknesses about its lack of rigor.

## Novel Insights

The most interesting meta-insight across the reviews is that the harsh critic's primary concrete suggestion (test the theoretical dilation on the GM) is *already present in the paper* as Figure 1, yet the critic still found the paper's evidence insufficient. This suggests that the paper's *central piece of validating evidence* (the GM simulation) is being inadvertently de-emphasized by the surrounding framing — the heuristic-laden theoretical results and the thin MNIST experiment distract from what is actually a clean, well-executed simulation that directly confirms the paper's core claim. The real gap is not missing evidence but poor rhetorical packaging: the paper would be stronger if it positioned Figure 1 as its primary empirical contribution and explicitly scoped the MNIST experiment as a preliminary qualitative demonstration of the *general insight* (not as a validation of the specific theoretical model). Beyond this, no genuinely novel insight emerges from the reviews beyond the paper's own contributions.

## Suggestions

1. **Reframe the paper around the known limitations.** State clearly in the abstract and introduction that the theoretical results are derived via non-rigorous replica methods and should be treated as conjectures or scaling laws. Qualify conclusions drawn from heuristic calculations (Corollaries 5 and 6, Result 3) with appropriate caveats.

2. **Bridge the theory-practice gap.** Either (a) formally show how the time dilation in the generative process relates to oversampling in training time distribution, or (b) test the actual τ(t) dilation on a real dataset, or (c) explicitly frame the oversampling method as a separate heuristic inspired by (but not derived from) the theory.

3. **Strengthen the MNIST experiment.** Add multiple seeds with error bars, compare against at least one alternative schedule (cosine, or uniform with more epochs), and evaluate whether oversampling degrades other quality metrics. Report the proportion of 0s from the trained model under the standard uniform schedule as a baseline.

4. **Emphasize the GM experiment.** Figure 1 is the cleanest evidence in the paper. Make it the centerpiece of the empirical validation and consider additional GM experiments (e.g., varying p, varying κ, varying n) to reinforce the sample complexity and limit-taking claims.
