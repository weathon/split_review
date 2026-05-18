Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces two linked algorithms for goal-conditioned RL: NCII (Null Counterfactual Interaction Inference), which infers object-object interactions using a "null counterfactual" assumption (comparing observed transitions against a counterfactual where a cause factor is absent), and HInt (Hindsight Relabeling using Interactions), which uses these inferred interactions to filter hindsight relabeling trajectories. The core insight is that vanilla hindsight relabeling can hurt sample efficiency in object-centric domains by rewarding trajectories where the target object was never actually controlled. The paper evaluates on Random DAG, Spriteworld, Robosuite, Robot Air Hockey, and Franka Kitchen domains, reporting significant improvements in both interaction inference accuracy and downstream RL sample efficiency.

## Strengths

1. **NCII achieves substantially lower misprediction rates across all evaluated domains.** Table 1 reports near-zero misprediction rates (e.g., 0.003 on Robosuite-default) that are orders of magnitude lower than prior methods like JACI, gradient-based, and attention-based approaches. This directly supports the claim that the null counterfactual approach provides a significant improvement in interaction inference accuracy.

2. **HInt improves sample efficiency by up to 4× across diverse goal-conditioned tasks.** Figure 4 shows consistent improvement over vanilla HER, prioritized replay, f-divergence policy gradients, and ELDEN across Spriteworld, Robosuite, Air Hockey, and Franka Kitchen — spanning quasistatic pushing, dynamic striking, and articulated manipulation. HInt with NCII-inferred interactions matches or exceeds HInt with ground-truth interactions, demonstrating robustness to inference imperfections.

3. **Clear, concrete motivation of the hindsight distribution mismatch problem.** Section 1's block-pushing example (hindsight rewarding trajectories where the block does not move, which are irrelevant when the block is far from the goal) precisely identifies a real and underappreciated failure mode of hindsight relabeling in object-centric domains.

4. **The null counterfactual definition (Definition 3.1) provides a principled, domain-general formalization of interactions.** Unlike domain-specific heuristics (distance thresholds, contact detection), the definition applies across different dynamics (quasistatic pushing, dynamic collision, articulated manipulation) as demonstrated by the diverse evaluation suite.

5. **Figure 5 provides direct empirical evidence for the mechanism behind HInt's improvement.** The heatmaps show that HInt filtering removes hindsight goals where the target object was already at the goal (a common spurious case) and retains goals that better match the desired goal distribution, validating the claimed mechanism.

## Weaknesses

### Fatal

None.

### Major

1. **Missing comparison against other hindsight-distribution-improvement methods.** The paper cites Curriculum HER (Fang et al. 2019), curiosity-based hindsight (Zhao & Tresp 2019), maximum-entropy hindsight (Zhao et al. 2019), and Hindsight Goal Generation (Li et al. 2021) in the related work but does not compare against any of them. Since the core contribution is a new filtering strategy for hindsight relabeling, it is unclear whether the benefit comes from the interaction-based filter specifically or from any non-uniform hindsight sampling strategy. The f-policy gradient baseline partially addresses this but is not a hindsight-filtering method. This gap weakens the claim that interactions are the right inductive bias, as opposed to simply modifying the hindsight distribution non-uniformly in any principled way.

2. **The null-state assumption is a structural limitation that is insufficiently discussed as such.** The method requires data containing trajectories with varying subsets of factors (i.e., where objects are sometimes absent) to train the masked forward model (Section 4.1, line 75: "only possible in settings where each trajectory can contain a different subset of the state factors"). In many real-world and standard simulation settings — e.g., the robot arm itself is always present — there is no natural "arm absent" state, and collecting data with absent objects may be impractical. The paper does not discuss this requirement as a limitation or offer workarounds. While the assumption is clearly stated in Definition 3.1, its practical implications for deployment are not addressed; the brief Limitations paragraph (Section 6) focuses on domains where interactions are less critical rather than on this more fundamental structural requirement.

### Minor

3. **No sensitivity analysis or default value provided for $\epsilon_{\text{null}}$.** The threshold $\epsilon_{\text{null}}$ appears in Equation 3 to decide whether the log-likelihood difference between observed and nulled predictions constitutes an interaction. It is never discussed, given a default value, or ablated. The performance of NCII depends on this choice, and without any sensitivity study, it is unclear how robust the method is or how to apply it in a new domain.

4. **The two filtering strategies ("action graph" vs. "control-target") are not clearly defined or justified.** Section 4.2 defines the general path-based filtering criterion. Line 114 introduces "control-target interaction" as limiting the chain length. However, line 169 then states: "we applied HInt using the action graph filtering strategy in all the domains except the obstacles variants, where we found the control-target graph filtering strategy was more stable." The "action graph filtering strategy" is never defined, and the choice between strategies appears ad-hoc without analysis.

5. **No analysis of NCII's iterative training convergence or error propagation.** The NCII algorithm alternates between training the forward model $f$ and the interaction model $h$, where $h$'s targets come from the current $f$'s null tests, and $f$ is then retrained using $h$'s predictions. Early inaccuracies in either model could compound, but no analysis of the number of iterations needed, convergence behavior, or sensitivity to initialization is provided.

### Trivial

None.

## Nice-to-Haves

- A comparison against a simpler interaction detector (e.g., checking whether the target object's position/velocity changes by a threshold after an action). If NCII significantly outperforms this, the paper's more complex machinery is further justified.
- Reporting training times and inference speeds for NCII, since the iterative training of two models has practical computational cost.
- Explicitly stating the default value of $\epsilon_{\text{null}}$ used in experiments.

## Removed Points

- **"Image-based results claimed but not shown":** The paper's introduction claims NCII "scales gracefully to segmented image inputs in Spriteworld." Without access to the embedded table images (parser artifact), it cannot be verified whether these results exist in the original submission. Removed per the rule that parser artifacts do not reflect author errors.
- **"Reproducibility statement is cut off":** The text is truncated, but this is a PDF extraction artifact. The original submission contains the full statement. Removed per the rule about parser artifacts.
- **"'up to 4× improvement' lacks final performance numbers":** The claim is supported by training curves in Figure 4 (5 seeds, standard error shading). The exact numerical values are visually conveyed; this is a formatting preference, not a substantive gap.
- **"No statistical significance bars at convergence":** RL evaluations with 5 seeds and standard error shading are standard practice. This is a field-norm nitpick; removed.
- **Several generic suggestions from the Strengthening section** (e.g., "ablating the null assumption against simple heuristics") are moved to Nice-to-Haves since they represent scope extensions, not core flaws.

## Novel Insights

The two reviews together surface an important tension: the paper's strongest empirical evidence (NCII's near-zero misprediction rates and HInt's consistent 4× gains) is in tension with the weakest point in the evaluation design — the absence of comparisons against other hindsight-distribution-modifying methods. The strength finder rightly points to the concrete, mechanistic evidence in Figure 5 (the heatmap showing distribution shift), which the harsh critic underweights. The harsh critic correctly identifies that the null-state requirement is a real-world deployment concern, but overstates its impact: the domains tested (robotics with varying object sets, Spriteworld) are precisely those where the assumption holds, and the paper's transparency about the assumption is adequate. The most actionable insight is that adding even one comparison against a modern hindsight-sampling method (e.g., Curriculum HER) and a simple ablation of $\epsilon_{\text{null}}$ would substantially strengthen the core claim without requiring new algorithm development.

## Suggestions

1. Add at least one comparison against a non-uniform hindsight sampling method (e.g., Curriculum HER) on a domain where such methods are known to work, to isolate whether the benefit is specific to interaction filtering.
2. Provide a default value for $\epsilon_{\text{null}}$ and show sensitivity across a range (e.g., as a percentile of the log-likelihood difference distribution on held-out non-interaction states).
3. Explicitly define the "action graph filtering strategy" in Section 4.2 and state the rationale for choosing between the two strategies.
4. Expand the Limitations paragraph to explicitly discuss the requirement for data with varying subsets of factors and the implications for domains where all factors are always present.
5. Report the number of NCII training iterations used in experiments and briefly comment on convergence.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>