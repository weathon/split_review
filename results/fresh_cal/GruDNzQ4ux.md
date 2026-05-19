## Summary

This paper identifies reward prediction as a performance bottleneck in model-based reinforcement learning (MBRL), particularly for sparse-reward tasks. It proposes DreamSmooth, which applies temporal smoothing (Gaussian, uniform, or EMA) to reward targets before training the reward model, making it easier to predict when rewards occur without needing exact timestep alignment. The method is extremely simple—one additional line of code—and yields substantial improvements over DreamerV3 on three long-horizon sparse-reward tasks (RoboDesk, Hand, Earthmoving) while matching baseline performance on dense-reward benchmarks (DMC, Atari). Ablations convincingly isolate temporal smoothing as the effective ingredient, ruling out data imbalance, model capacity, and loss function alternatives.

## Strengths

- **Clear identification and empirical demonstration of the reward prediction bottleneck.** Section 3.2 and Figure 2 show that DreamerV3's reward model systematically misses sparse rewards across four environments. Figure 3 links these prediction failures to concrete policy failures (e.g., the agent getting stuck after the first subtask in RoboDesk). This provides direct evidence for the paper's central claim and is a genuinely underexplored issue in the MBRL literature.

- **Substantial performance improvements on multiple sparse-reward tasks.** Figure 5 shows DreamSmooth (Gaussian) dramatically improves DreamerV3 on RoboDesk, Hand, and Earthmoving in both sample efficiency and final return. On Hand, median reward rises from near zero to over 100; improvements are sustained across training. These results directly support the claim that better reward prediction via smoothing leads to better task completion.

- **Well-designed ablations that rule out alternative explanations.** Section 4.4 tests oversampling (data imbalance), increased reward model size, and alternative loss functions (L1, L2, 2-Hot). In each case, smoothing either outperforms or complements the alternative. For example, Figure 7 shows oversampling helps but underperforms DreamSmooth; Figure 8 shows larger reward models provide negligible gain. This isolates temporal smoothing as the effective ingredient.

- **Generalization to multiple MBRL algorithms.** Figure 6 demonstrates that DreamSmooth also improves TD-MPC (pixel and state) and MBPO (state) on the Hand task, where vanilla algorithms fail to solve even the first subtask. This supports the claim that the method benefits MBRL broadly, not just DreamerV3.

- **No performance degradation on dense-reward benchmarks.** Figure 5e,f shows DreamSmooth achieves comparable aggregate performance to DreamerV3 on 7 DMC tasks and 6 Atari tasks (100K steps). This supports the claim that the method can be applied universally without harming performance where reward prediction is not a bottleneck.

- **Extremely minimal implementation cost.** Algorithm 1 shows DreamSmooth requires only a single additional line of code per rollout, with time complexity O(T·L). This makes the contribution practically useful for existing MBRL codebases.

## Weaknesses

### Fatal

None.

### Major

- **The reward-prediction accuracy metric is biased and conflates methods.** Section 4.2 (line 288) measures whether the predicted reward exceeds half the target reward value. For the baseline, the target is the original sparse reward (e.g., 1), so the threshold is 0.5. For DreamSmooth, the target is a smoothed value (e.g., 0.2–0.3), so the threshold is 0.1–0.15. The two methods are therefore evaluated against different thresholds on different targets. This does not measure whether DreamSmooth better detects reward events on the *original* signal; it only confirms that predicting a smoothed target is easier. The comparison should be redesigned to evaluate both methods against the common ground-truth reward (e.g., via precision/recall for detecting reward events within a temporal window).

- **The "state-of-the-art" claim is unsupported by the comparison set.** The abstract claims "state-of-the-art performance on long-horizon sparse-reward tasks," but the experiments compare only against DreamerV3 (the main baseline), TD-MPC, and MBPO (both on a single task). No comparison is made to any method designed for sparse rewards—such as hindsight experience replay (HER), curiosity-driven exploration (ICM, RND), or even simple reward-shaping baselines. Since DreamerV3 is itself not specialized for sparse rewards, beating it does not establish state-of-the-art among methods that address this difficulty. The paper's core contribution stands without this claim, and the claim should be removed or qualified.

- **The Crafter failure is under-analyzed in the main text.** DreamSmooth-Gaussian and Uniform perform worse than the baseline on Crafter, despite improving reward prediction accuracy. The paper offers a hypothesis ("false positives from anticipating future rewards," line 345) and references an appendix section, but provides no controlled analysis in the main text—no false-positive rate measurements, no ablation of smoothing width on this specific environment, and no evidence linking the hypothesized mechanism to the performance drop. Given that Crafter is the only environment where smoothing hurts, a proper analysis of why would substantially strengthen the claimed universal applicability.

### Minor

- **Limited cross-algorithm evidence.** DreamSmooth improves TD-MPC and MBPO on only the Hand task. The paper acknowledges that these algorithms "fail on other sparse-reward tasks," but this means the claim that DreamSmooth is "useful in a broad range of MBRL algorithms" rests on a single additional task. Demonstrating improvement on at least one more task for TD-MPC or MBPO would substantiate this claim.

- **Individual DMC and Atari task results are not shown.** Only aggregate learning curves (Figure 5e,f) are provided for the dense-reward benchmarks. While no degradation is visible in aggregate, individual task breakdowns would increase confidence that no single task is substantially degraded. This is especially important since the paper claims the method "can be universally applied."

- **The theory does not cover the best-performing variant.** The optimality guarantee (which is in the appendix, stripped by the parser) applies only to EMA smoothing with full state history, but the best empirical results use Gaussian smoothing (which has no guarantee). The paper is transparent about this limitation (lines 158–160 explicitly state "there is no theoretical guarantee" for Gaussian smoothing), but the framing in the abstract and introduction could still give readers the impression the method is theoretically grounded when its strongest results are not.

### Trivial

None.

## Nice-to-Haves

- A comparison to a classification-based reward loss (predicting whether a reward occurs within the next N steps) would directly test the hypothesis that MSE loss is the root cause of poor reward prediction, complementing the L1/L2/2-Hot ablations already performed.
- The smoothing window length L is not independently ablated from the kernel parameters (σ, δ, α). While σ controls effective width for Gaussian smoothing, a direct sweep of L would clarify its role.
- Statistical reporting (confidence intervals or effect sizes) would strengthen the 3-seed results.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

- *Harsh Critic Critical Issue #4 (theoretical guarantee is misleading):* The paper is actually quite transparent. It explicitly states: "when future rewards are used for smoothing (e.g. Gaussian smoothing)... there is no theoretical guarantee" and "under the assumption that a state includes the history of past states." The theoretical limitations are clearly caveated in the paper itself. Removed because the criticism misreads the paper's own careful framing.

- *"No discussion of prior work on reward function transformation, HER, ICM, RND, potential-based shaping":* The related work section is admittedly brief, but the instruction forbids mentioning missing related works since I cannot confirm what exists externally and may invent nonexistent ones. Removed per hard rules.

- *"Only 3 seeds are used":* This is standard practice in DreamerV3 papers and the broader MBRL literature. Three seeds with min-max shading (as the paper uses) is the norm. Removed as a generic nitpick.

- *"The hypothesis that MSE loss causes the model to predict zero everywhere is not directly tested":* The paper tests alternative loss functions (L1, L2, 2-Hot) in Figure 8 and shows they also fail to solve the problem. This indirectly tests the MSE hypothesis. Removed because the paper already addresses the concern.

- *"Crafter subfigure only shows EMA":* The paper shows Gaussian, Uniform, EMA, and DreamerV3 in Figure 6d with proper labels. The reviewer misread the figure. Removed as factually wrong.

- *Strength: "This paper addressed an important problem"* — removed as generic/superficial.
- *Strength: "The paper identifies that reward prediction is a critical but overlooked bottleneck"* — already captured in the main strengths as "clear identification."

## Novel Insights

The synthesis surfaces a tension worth noting: DreamSmooth's primary experimental success comes from symmetric smoothing (Gaussian), which the paper correctly notes has no theoretical optimality guarantee, while its backward-only variant (EMA) does have a guarantee but produces weaker empirical results. This mirrors a broader pattern in deep RL where the methods that work best empirically often have the weakest theoretical grounding, and it points toward a concrete open question: can the empirical success of symmetric smoothing be theoretically justified, or is its advantage fundamentally tied to a non-stationary reward signal that breaks the POMDP equivalence? Additionally, the Crafter failure suggests a deeper trade-off: in environments with many diverse sparse rewards, smoothing may cause the reward model to fire too frequently, washing out the signal-to-noise ratio—an effect that deserves dedicated study.

## Suggestions

1. **Remove or qualify the "state-of-the-art" claim** in the abstract and introduction unless new baselines are added. The paper's contribution is strong enough without this framing.
2. **Redesign the reward-prediction accuracy metric** to compare both methods on the same ground-truth reward signal, for example by thresholding predictions to detect reward events within a small temporal window and reporting precision/recall.
3. **Add at least one standard sparse-reward baseline** (e.g., HER-style replay labeling or a count-based exploration bonus) on one of the three improved tasks to contextualize the magnitude of improvement.
4. **Provide a more detailed analysis of the Crafter failure** in the main text—quantify false-positive rates for each smoothing variant, correlate them with policy failures, and ablate the smoothing width on this environment.
5. **Report individual task scores for DMC and Atari** in a table or per-task learning curves, ideally in the main paper or at minimum in the appendix with a note confirming no task degrades.
6. **Consider showing improvement on at least one additional task for TD-MPC or MBPO** to strengthen the cross-algorithm generality claim.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>