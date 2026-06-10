## Summary

STL-Drive proposes using Signal Temporal Logic (STL) robustness scores computed from Responsibility-Sensitive Safety (RSS) minimum-safe-distance constraints as an auxiliary loss during imitation learning for waypoint prediction in automated driving. Evaluated on the NAVSIM benchmark using Transfuser as the base model, the paper reports that STL-Drive variants outperform the baseline and that the RSS-based safety envelope outperforms a constant-distance envelope. The idea is sensible, but the paper has significant specification and evidential gaps that prevent acceptance at a top venue.

## Strengths

- **Novel framing of RSS as an offline training regularizer rather than a runtime safety monitor.** Prior work used RSS for reactive monitoring and falsification; this paper repurposes it as a differentiable loss signal during imitation learning (Section 1, lines 22–26). This is clearly differentiated from the prior work surveyed.

- **All STL-Drive variants reportedly outperform the baseline Transfuser (α=0) on aggregate NAVSIM score.** Section 3.2 (line 102) states that the baseline achieves 0.7409 and every STL-based variant scores higher, providing direct quantitative evidence that adding the STL robustness loss improves the learned policy.

- **Controlled ablation showing the RSS spatial envelope outperforms a constant-distance envelope.** Section 3.2 (line 108) reports that as α increases, performance degrades significantly for a constant 0.5m envelope but remains stronger for the RSS-based envelope. This isolates the benefit of the RSS formalization over a naive fixed-distance alternative.

- **Systematic comparison of three robustness aggregation strategies.** Type-0 (minimum over vehicles within 50m), Type-1 (closest vehicle only), and Type-2 (inverse-distance-weighted average) are defined and compared, with Type-1 identified as the best performer (Section 2.2, Section 3.2). This provides actionable design guidance.

- **Large-scale, real-world training data.** 103,288 scenarios from the nuPlan/OpenScene dataset are used for training (Section 3.1), grounding the evaluation in realistic data.

## Weaknesses

### Fatal

None.

### Major

- **The combined loss function is never specified.** The paper's core mechanism is a weighted combination of the imitation learning task loss $\mathcal{L}_{tpp}$ and the STL robustness score, parameterized by $\alpha$. Yet the actual total loss equation never appears in the paper. The text says "use the robustness score as an additional loss term" (line 33), and experiments sweep $\alpha \in \{0.2, 0.5, 0.8, 1.0\}$, but the reader cannot determine whether the combination is $\mathcal{L}_\text{total} = \mathcal{L}_{tpp} + \alpha\rho$, $(1-\alpha)\mathcal{L}_{tpp} + \alpha\rho$, or some other form. This is not a minor oversight: the central equation of the claimed contribution is absent, making the method incompletely specified and unreproducible without inference.

- **Evidence for improved safety is thin — no disaggregated safety metrics reported.** NAVSIM produces multiple sub-metrics (safety, comfort, navigation progress), but only a single aggregate score is discussed. The paper's central claim is "improved safety and robustness," yet no collision counts, minimum-distance histograms, near-miss rates, or scenario-difficulty breakdowns are provided. No variance, confidence intervals, or multi-seed training results are reported. Because the aggregate score conflates safety with comfort and navigation progress, it is impossible to verify that *safety specifically* improved — the aggregate gain could be driven by comfort or progress while safety remained flat or degraded. This is an evidential gap that strikes at the paper's core claim.

### Minor

- **Open-loop evaluation limits the safety conclusions that can be drawn.** NAVSIM uses non-reactive open-loop simulation: predicted waypoints are compared against ground-truth trajectories but never influence the environment. Safety is inherently a closed-loop property — a policy that predicts safe-looking waypoints in a static log may behave unsafely when its predictions close the loop. The paper acknowledges this in passing (line 80: "non-reactive open-loop simulation approach") but does not discuss what this limitation means for the validity of its safety claims. Three qualitative closed-loop examples (Figure 3) mitigate this slightly but do not replace systematic closed-loop testing.

- **Type-2 robustness formula is specified only verbally.** Type-0 is given as a formal equation (Eq., line 68). Type-1 and Type-2 are described only textually ("robustness score of only the closest vehicle," "inverse weighted distance average"). A precise equation for the Type-2 aggregation is needed for reproducibility.

- **Differentiability of the STL robustness computation is not addressed.** The paper uses RTAMT to compute robustness scores but never discusses how gradients flow from the robustness loss back through the waypoint predictor to the model parameters. RTAMT-based monitoring is not inherently differentiable in the deep learning sense, and this gap is non-trivial for the claimed training procedure.

- **Conclusion (Section 5) is disconnected from the paper's content.** It discusses "spatial intelligence," "generative models," and "large language models" — concepts that appear nowhere in the technical sections. This reads as templated boilerplate rather than a conclusion synthesized from the work presented.

- **Limitations section (Section 6) contains extensively garbled/unreadable text.** Multiple sentences are corrupted (e.g., "Our tmheo ddeel fhinaesd bteeemnp odreasli glongeidc tcoo uhladn dclhea lvlearnigoeu st hsei tfuraatimeonws..."), making the section partially unintelligible. This undermines the professionalism of the submission.

### Trivial

None.

## Nice-to-Haves

- Reporting NAVSIM's sub-metrics (safety, comfort, progress) separately would directly strengthen the paper's core safety-improvement claim.
- A brief discussion of how the RTAMT robustness gradient is obtained (or a differentiable proxy used) would address a non-trivial methodological question.
- A comparison to a simple safety-filtering baseline (e.g., weighting training examples by safety scores) would contextualize the benefit of the full STL+RSS formulation.

## Removed Points

*These points were flagged as potential weaknesses but were removed after verification against the paper; they are retained here for transparency in case they are useful.*

- **"Inadequate baselines" (harsh critic point 4):** The criticism demands comparisons to Safe DAgger, MPC shielding, barrier-function methods, etc. This asks the paper to address problems outside its stated scope. The paper compares against its own baseline (α=0) and a constant-distance envelope ablation, which is appropriate for an initial investigation of the proposed technique. These alternative methods address a different research question (STL-Drive vs. other safe-IL paradigms) that the paper does not claim to answer.
- **"0.5m constant envelope is unrealistically small":** This is an opinion about threshold selection, not a verifiable weakness. The comparison of RSS vs. constant envelope under identical α values is a reasonable ablation.
- **"Missing related works":** Removed per instructions (cannot verify without external sources).
- **"Typos/formatting/style nitpicks":** Removed per instructions (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The reviews surface well-known methodological standards (reporting disaggregated metrics, specifying loss functions fully) but do not uncover unexpected findings about the paper's content.

## Suggestions

1. Provide the explicit total loss function in Section 2 (e.g., $\mathcal{L}_\text{total} = \mathcal{L}_{tpp} + \alpha\rho$ or $(1-\alpha)\mathcal{L}_{tpp} + \alpha\rho$).
2. Report disaggregated NAVSIM sub-metrics (safety, comfort, progress) alongside the aggregate score.
3. Add a brief discussion of how gradients flow through the RTAMT-based STL robustness computation, or specify a differentiable alternative.
4. Replace the templated conclusion (Section 5) with a summary of findings, concrete limitations, and future work specific to this paper.
5. Clean up the garbled text in Section 6.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>