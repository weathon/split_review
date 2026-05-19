- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have thoroughly verified all claims against the paper. Let me write the consolidated review.

## Summary

FlickerFusion proposes a simple, parameter-free input-space augmentation for zero-shot out-of-domain (OOD) generalization in MARL under intra-trajectory entity count changes. At each inference step, entities are stochastically dropped from each agent's observation to match the in-domain input size, relying on temporal aggregation to recover information. The method is evaluated across 12 new benchmarks (MPEv2) against 11 baselines, achieving top mean reward in 10 of 12 and showing improved robustness.

## Strengths

- **Strong empirical results across diverse benchmarks**: Table 1 shows FlickerFusion ranks first in 10 of 12 benchmarks and second in another, with improvements in 22 of 24 comparisons against the backbone (QMIX-MLP or QMIX-Attention). This is the paper's strongest evidence and is clearly presented.

- **Clean theoretical guarantee for decentralized dropout**: Proposition 3.1 (lines 171–177) provides an in-expectation bound on the L1 distance between empirical and expected drop ratios across agents, showing that random independent dropping achieves well-dispersed coverage with minimal overlap. This formal guarantee for the decentralized scheme is a genuine contribution.

- **Domain-aware entity dropout ablation is well-conducted**: Table 2 systematically demonstrates that using the in-domain entity count to determine how many entities to drop (DAED) significantly improves over naive uniform dropping, especially for the MLP backbone (e.g., -1127.2 vs -1447.6 in Guard OOD1). This cleanly validates the design choice in Section 3.2.

- **Low computational overhead**: The paper reports only 4.1% (MLP) and 9.1% (attention) additional training runtime on an RTX 3090, with reduced memory cost since no extra parameters \(\theta_Q'\) are needed. This directly supports the claimed practical applicability.

- **Standardized 12-benchmark suite (MPEv2)**: Section 4 introduces six environments with two OOD splits each, designed specifically for intra-trajectory entity addition/deletion. This addresses the standardization gap noted by Papoudakis et al. (2021) and is a valuable community resource.

## Weaknesses

### Fatal
None.

### Major

- **Uncertainty metric is never defined.** The paper repeatedly highlights "uncertainty reduction" as a key advantage — in the abstract, introduction (lines 4, 23), Section 5 results (line 229), and Discussion (line 241). Figure 5 (top-left) is described as a "box-and-whisker plot uncertainty distributions across methods" (line 224), and the caption mentions "standard deviation statistics." However, the paper never explicitly states what "uncertainty" refers to. Is it the standard deviation of final episode returns across seeds? The variance of Q-values? Prediction intervals? Something else? Because the metric is undefined, the central claim that FlickerFusion "uniquely reduces uncertainty" (abstract, line 4) is unverifiable. The box plot cannot be interpreted or reproduced without this definition.

### Minor

- **Temporal fusion mechanism is asserted as intuition but not rigorously analyzed.** The paper states that "aggregating these views along the temporal axis gives us a virtually full view" (line 191) and uses the flicker fusion analogy as an explanatory narrative. However, no analysis — theoretical or empirical — is provided to support this claim. Proposition 3.1 bounds dispersion across agents at a single time step but says nothing about information accumulation over time for a single agent. No experiment measures how many entities each agent observes within a time window, whether critical events in dropped entities are missed, or how many steps are needed to reach a given coverage probability. The empirical results (Table 1) demonstrate that the combined method works, which is valuable, but the paper does not separately validate the temporal fusion mechanism that it presents as the core intuition.

- **No discussion of limitations or failure cases.** The paper does not address when FlickerFusion might degrade. For example, if the inference entity count is far larger than the training count (e.g., 10×), the method would drop most entities, losing nearly all information at each step. The experiments test only moderate OOD shifts. A brief limitations discussion would substantially strengthen the paper.

- **"Universal" claim is only tested with QMIX backbones.** The method is described as a "universally applicable augmentation technique" (abstract) but is only evaluated with QMIX-MLP and QMIX-Attention. While the method's architecture-agnostic design is plausible, substantiating the universality claim would require at least one additional backbone (e.g., VDN, COMA).

- **Hyperparameter sensitivity is not analyzed.** The method depends on knowing the in-domain entity count. If this is misestimated, the dropout could drop too many or too few entities. The paper does not analyze sensitivity to this assumption.

### Trivial
None that are not parser artifacts.

## Nice-to-Haves

- A temporal covering analysis (theoretical or empirical) quantifying the probability that each entity is observed at least once within a window of T steps would directly support the "fusing" narrative and turn an intuition into a verified property.
- An explicit definition of the uncertainty metric would make the results reproducible and the claimed advantage verifiable — a single sentence stating whether uncertainty refers to the standard deviation of episode returns across seeds, the variance of Q-values, or something else.

## Removed Points

- **"Irrelevant baselines" criticism** — Removed. The paper explicitly categorizes model-agnostic methods separately (red in Table 1), acknowledges they "were not created with MARL tasks in mind" (line 242), and includes them transparently. Demonstrating that these methods fail in this setting is itself informative. The comparison against MARL-specific baselines (7 methods) is the primary evidence, and those comparisons are unaffected.

- **Proposition 3.1 relevance criticism** — Removed. The proposition correctly supports the decentralized dropout scheme's dispersion guarantee across agents, which is its stated purpose. The reviewer's concern (that it doesn't address temporal coverage) is factually correct but does not constitute a weakness of the proposition itself, which is appropriately scoped.

- **Missing appendix/content removed by parser** — Removed per instructions; the parser strips these from all submissions.

- **All formatting/typographical nitpicks** — Removed per instructions (parser artifacts, not author errors).

## Novel Insights

The reviews surface one observation that the paper itself does not emphasize: the method's success with an MLP backbone (often beating attention-based methods with fewer parameters) raises an interesting question about whether complex inductive biases in attention mechanisms are actually detrimental under OOD shifts in entity count. The paper notes this briefly in the Discussion (line 241) but the reviewers' convergence on this as a noteworthy finding suggests it deserves more attention. This could motivate future work on simpler architectures for OOD MARL.

## Suggestions

1. **Define the uncertainty metric explicitly in the main text** (not just in a figure caption). A single sentence such as "Uncertainty is measured as the standard deviation of final episode returns across 5 seeds for each benchmark" would resolve the main weakness.

2. **Add a short limitations paragraph** discussing the method's degradation under extreme OOD shifts (e.g., inference entity count >> training count) and potential sensitivity to misestimated in-domain entity counts.

3. **Either add a temporal covering analysis** (even a simple bound or an empirical measure of how many entities each agent observes over a window) or **downgrade the "virtual full view" language** from a claimed property to a motivating intuition. The paper's empirical results stand on their own; the temporal fusion narrative does not need to be a verified theorem, but it should be clearly scoped.

4. **Consider evaluating on one additional backbone** (e.g., VDN) to substantiate the "universal" claim, or qualify the claim to say "universal across MLP and attention architectures tested."
