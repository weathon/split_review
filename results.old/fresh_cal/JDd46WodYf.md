Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper proposes an "active" procedure planning framework that, during inference, selects *whether* to add an intermediate visual observation based on a thresholded uncertainty score. This score combines a task-variation entropy prior (computed from training data over the distribution of trajectories for a given start/goal action pair) and a calibrated prediction confidence score (temperature-scaled softmax, with sequence-level uncertainty = 1 − min step confidence). The method is plugged into two diffusion-based planners (PDPP, MDPP) and evaluated on CrossTask and COIN. Results show modest but consistent gains (∼5% SR on CrossTask T=3) over a controlled random-observation baseline, with the finding that performance peaks at intermediate thresholds (not at τ=1), confirming that uncertainty-driven selection is useful.

## Strengths

1. **Controlled evaluation that properly isolates the benefit of uncertainty-guided selection.** The authors explicitly acknowledge that adding observations provides more information, and address this by re-training passive baselines with random observation addition matched to the same budget (Section 5.1). Tables 1 and 2 show that uncertainty-guided sampling consistently beats both passive and random baselines at equivalent observation costs, e.g., on CrossTask T=3, MDPP with uncertainty-guided observation (τ=0.3) achieves a success rate of 45.77% vs. 40.18% for passive MDPP and 44.14% for random sampling (text near line 171). This controlled design makes the comparison fair and the results credible.

2. **Ablation of two complementary uncertainty metrics with clear differentiation.** Figures 4 and 5 systematically compare the task-variation score, the calibrated confidence score, and their weighted combinations against random sampling. The calibrated confidence score consistently outperforms the task-variation score, and combining both (with a small weight on task variation) yields further robustness. The finding that metrics differ in effectiveness and that random sampling barely helps until >70% of instances are augmented is a genuinely useful empirical result.

3. **Model-agnostic integration across two SoTA diffusion planners.** The active mechanism is applied to both PDPP and MDPP on two datasets (CrossTask and COIN) with consistent trends. This demonstrates that the approach is not tied to a specific architecture.

## Weaknesses

### Fatal
None.

### Major
- **Framing inflation ("paradigm shift") relative to actual mechanism.** The paper claims to "enable flexible visual observations to disambiguate the planning task" and that the method "represents a paradigm shift in procedure planning from passive reasoning to active/adaptive learning and reasoning" (line 21). In reality, the "active" component is a single binary threshold gate that decides *whether* to add an observation. The observation itself is always the center/center-right frame — a fixed heuristic. There is no sequential decision-making, no query selection dependent on the current state, and no interaction with the environment beyond a one-shot insertion. The method is better described as "selective observation" than "active planning." While the paper acknowledges limited interactivity in the conclusion (line 196), the abstract, introduction, and contributions section claim substantially more than what is delivered. This mismatch between framing and scope weakens the paper's credibility and would need to be corrected for publication.

### Minor
- **The selection of *which* observation to add is not uncertainty-driven, even for T≥4 where multiple candidates exist.** The paper acknowledges that for T≥4 there are multiple candidate intermediate observations, but picks the center/center-right frame by default and explicitly defers uncertainty-based selection to future work (line 115). This means the claimed connection between uncertainty estimation and observation *selection* is incomplete: uncertainty only decides *whether* to observe, not *what* to observe. The gap is acknowledged, but it limits the method's claim to being "active" in any substantive sense for longer horizons.

- **The task-variation metric (Eq. 1) depends on correct prediction of the first and last actions, making it brittle.** The uncertainty score u_v is retrieved from a memory indexed by (a₁, a_T). During inference, the model uses its *predicted* (â₁, â_T) to look up this score. If these predictions are incorrect, the retrieved uncertainty corresponds to a different action pair and may be uninformative or misleading. This is a genuine limitation, though partially mitigated by the fact that the calibrated confidence score (u_c) also contributes to the combined score and does not share this dependency.

- **The minimum-over-steps aggregation in Eq. 3 (u_c = 1 − min_i(̄p_i)) is stated without justification.** The paper does not discuss why the worst-case step drives overall uncertainty rather than the average or product of step confidences. This choice is reasonable but should be motivated or ablated.

- **Temperature scaling calibration details are underspecified.** The paper adopts temperature scaling but does not state what data is used to learn the temperature parameter (e.g., a held-out calibration set, whether it is task-specific or dataset-specific). This is a standard detail that should be reported for reproducibility.

### Trivial
- The paper's section numbering jumps from 4.1.2 directly to 4.3 (no section 4.2). The content that could belong to section 4.2 (observation selection strategy) is present within 4.1.2 (lines 115–117), so nothing is missing, but the numbering or section header may be misassigned.

## Nice-to-Haves
- **Uncertainty-driven observation selection for T≥4:** The single most impactful extension would be to use the calibrated confidence of individual steps (min_i(̄p_i) already available) to identify which intermediate step is most uncertain and select the corresponding observation, rather than always picking the center frame. This would make the "active" claim substantially stronger.
- **Failure analysis for cases where adding an observation hurts performance:** The paper notes that performance peaks at intermediate thresholds (τ=0.5–0.7) because adding observations can sometimes "disturb correct predictions" (line 159). A brief analysis of when this occurs (e.g., when the center frame is noisy or misaligned) would deepen the contribution.
- **Cost analysis:** Discussing how the threshold can be tuned given a specific budget for additional observations and quantifying the computational overhead of re-running the diffusion model would improve practical utility.

## Removed Points

These points from the inputs were removed with justification:

1. **"Missing section 4.2" (Harsh Critic):** The selection strategy content that would belong to a §4.2 is present in §4.1.2 (lines 115–117). The numbering gap from 4.1.2 to 4.3 appears to be a formatting artifact; no content is missing. Removed per the rule: "REMOVE pure formatting/style nitpicks."

2. **"The task variation metric ignores visual ambiguity — it is a prior" (Harsh Critic, part of Claim 2):** The paper explicitly states this is "prior knowledge of the data distribution" (line 77). It is intentionally a prior over action pairs, meant to capture task-level variation uncertainty. The calibrated confidence score (u_c) is the complementary metric that captures instance-level visual ambiguity through model predictions which *are* conditioned on the visual input. The critic's framing that this is a flaw misunderstands the two-metric design.

3. **Reproducibility concern about unspecified thresholds (Harsh Critic, end of "Missing Parts"):** The paper explicitly states threshold values: "we adopt three thresholds τ={0.3,0.4,0.5}" (line 159). The mapping of thresholds to percentages of augmented instances is given for T=3. This is adequately specified.

4. **Strength Finder strengths that are generic or conflict with verified weaknesses:** The strength about "novel active-planning formulation that demonstrably improves accuracy" is retained in modified form in the Strengths section. The strength about "Qualitative example illustrating interpretability and uncertainty reduction" is moved here because it is a single anecdotal example — illustrative but not a strength that carries weight.

## Novel Insights

The most interesting observation is the non-monotonic relationship between observation budget and accuracy: performance peaks at intermediate thresholds (τ≈0.5–0.7) and declines at τ=1 (all instances augmented). This reveals an important property of procedure planning — adding visual observations is not uniformly beneficial and can introduce noise that disrupts already-correct predictions. The fact that random sampling barely helps until >70% of instances are augmented, while uncertainty-guided sampling shows gains at just 17% augmentation, cleanly demonstrates that *which* instances get additional observations matters far more than *how many*. This is the paper's strongest empirical insight and provides a clear argument for uncertainty-based selective observation.

## Suggestions

1. **Rebalance the framing.** Replace "paradigm shift," "active planning," and "seeks additional information" with language that accurately describes the contribution: selective mid-inference observation based on uncertainty. A binary gating mechanism with fixed observation position is not an interactive agent; it is a selective-input extension. Accurate framing will strengthen rather than weaken reader trust.

2. **Make the observation selection uncertainty-driven for T≥4.** The step-level confidence (̄p_i) already exists from Eq. 2. Using it to pick the observation corresponding to the least-confident step (rather than the center frame) would directly connect uncertainty estimation to observation *content* selection, substantially closing the gap between framing and implementation.

3. **Report the temperature scaling calibration details** (calibration set size, whether task-specific or global) and add a brief ablation of the min-over-steps aggregation vs. alternatives (average or product).

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>