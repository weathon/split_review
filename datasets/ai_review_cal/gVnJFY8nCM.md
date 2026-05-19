- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6
Here is my synthesized final review.

---

## Summary

This paper proposes Residual-MPPI, an online planning algorithm for policy customization in continuous control. The key idea is to integrate Residual Q-learning (RQL) with Model Predictive Path Integral (MPPI): at execution time, MPPI evaluates action sequences using the add-on reward plus the log-likelihood of the prior policy (which substitutes for the unknown original reward), thereby customizing the policy without retraining. The method is evaluated on MuJoCo benchmarks (zero-shot setting) and on the Gran Turismo Sport (GTS) environment, where it successfully customizes the champion-level GT Sophy 1.0 racing agent to drive more safely while retaining speed, using orders of magnitude less data than the training-based Residual-SAC baseline.

## Strengths

- **Zero-shot online customization without retraining.** Residual-MPPI customizes a pre-trained policy at execution time, requiring only the prior's action distribution and a dynamics model. The MuJoCo results (Table 1) show it consistently improves over the prior policy and outperforms both Full-MPPI and Guided-MPPI across four environments, with no task-specific training.

- **Scalability to a real-time, champion-level agent.** The GTS experiments are the paper's standout contribution. Residual-MPPI successfully customizes GT Sophy 1.0 to reduce off-course steps from ~93 to ~37 (few-shot) while incurring only a ~3-second lap-time increase. This is achieved with ~2,000 laps of offline data (for dynamics learning) and ~100 laps of online fine-tuning, whereas the Residual-SAC baseline required 80,000 laps and produced an overly conservative policy (Table 2). The 60 Hz real-time constraint on PS5 makes this a nontrivial deployment.

- **Practical dynamics learning pipeline.** Section 3.2 describes a principled training pipeline with multi-step error, exploration noise, and online fine-tuning. These are standard techniques but are sensibly combined to enable the method to work with learned dynamics and improve with online data, as demonstrated in the GTS few-shot results.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theoretical connection between MPPI and maximum-entropy optimality is heuristic, not rigorous.** Theorem 1 shows that the action-sequence distribution from a maximum-entropy policy matches the MPPI target distribution *under the condition that the noise distribution has infinite variance (i.e., is uniform)*. The paper then states that "MPPI can well approximate the maximum-entropy optimal policy with a large noise variance" (line 148). The gap between infinite-variance (exact equivalence) and finite large variance (approximation quality) is never analyzed. The derivation of Residual-MPPI (replacing the MPPI evaluation function with the add-on reward plus log-prior) follows from this heuristic step. The algorithm works empirically, but the paper's framing ("establish the theoretical foundation," line 96) overstates what the theorem provides. The paper would be stronger if it acknowledged this limitation more clearly.

- **Missing Residual-SAC comparison in MuJoCo.** The paper includes Residual-SAC as a baseline in the GTS experiments but not in the MuJoCo experiments, where the baselines are only other planning methods (Prior Policy, Full-MPPI, Guided-MPPI). Since a core claim is that Residual-MPPI "eliminates the need for additional policy training," showing how its zero-shot performance compares to a trained Residual-SAC policy (the natural alternative from the RQL framework) would help assess whether the online approach sacrifices performance. The GTS experiments already demonstrate this comparison and strongly favor Residual-MPPI (better performance with ~800× less data), partially mitigating this gap. However, the absence in MuJoCo means the claim is not fully supported across the standard benchmark suite.

- **Explanation for outperforming Guided-MPPI is not tested via ablation.** The paper attributes Residual-MPPI's advantage over Guided-MPPI to the log-prior providing long-horizon information via the prior's Q-function (lines 246–247). This is a plausible story, but the two methods differ in *both* the evaluation function and the prior's role, so the cause is not isolated. An ablation (e.g., replacing the log-prior with a learned terminal value estimator based on the basic reward, or varying the planning horizon to test the explanation) would strengthen the analysis. Without it, the mechanism remains speculative.

- **No hyperparameter sensitivity analysis.** The method has tunable parameters (ω′ weighting the log-prior, λ temperature) whose impact on performance is not studied. A brief sensitivity analysis or a heuristic for setting these values would improve reproducibility and practical utility.

- **Dynamics model quality not characterized.** The paper relies heavily on a learned dynamics model for planning but does not report prediction error, multi-step rollout accuracy, or how degradation over the planning horizon affects performance. A quantitative characterization (even a single environment) would strengthen confidence in the results.

### Trivial

- The abstract text appears truncated after the URL (line 4 ends mid-sentence); this is a parser artifact. No actual paper issues.

## Nice-to-Haves

- A single MuJoCo environment with a comparison to Residual-SAC would make the zero-shot claim more complete (this is already a weakness above, listed as a nice-to-add suggestion).
- An ablation in one MuJoCo environment varying the planning horizon T and comparing Residual-MPPI to a version of Guided-MPPI with a learned terminal value estimator would isolate the log-prior's role.
- Clarify whether the 2,000 laps for GTS dynamics training were collected using the prior policy offline, and how they were allocated between training and validation.

## Removed Points

- **Criticism about no hypothesis tests / statistical rigor in MuJoCo** — Removed: 500 episodes per method with mean and std is a standard reporting format; the evaluation is sufficiently robust. This is a generic concern, not a specific identified problem.
- **Criticism about 30-lap GTS evaluation being "small sample"** — Removed: the standard errors on lap times are very tight (e.g., ±0.37s for few-shot MPPI, ±0.13s for Residual-SAC), indicating deterministic or near-deterministic evaluation in a consistent simulator setting. The sample size is adequate for the observed effect sizes.
- **Criticism about missing prior policy hyperparameters / characterization** — Removed per hard rules: these details would typically be in the appendix (which was stripped by the parser). The paper states that SAC-trained priors are used; further implementation details belong in the supplement.
- **Criticism that Theorem 1 is not labeled as "Theorem 1"** — Removed: the paper clearly contains `\begin{theorem}...\end{theorem}`; referring to it as Theorem 1 is standard. This is a formatting nitpick.
- **Strength about "theoretical grounding for integrating RQL and MPPI"** — Removed from strengths: as noted under Minor weaknesses, the theoretical connection is heuristic, and presenting it as a "principled advance" overstates the rigor. The method's value is empirical, not theoretical.
- **Strength about "effective initialization from prior policy"** — Removed: initializing the nominal sequence from the prior policy is a straightforward application of the method; calling it a separate strength is generic.

## Novel Insights

None beyond the paper's own contributions. The observation that the log-prior can serve as a stand-in for the unknown original reward in an MPPI planner, and that this empirically works better than using the ground-truth full reward (Guided-MPPI), is the paper's central insight. The reviewers do not contribute a new interpretation beyond what the paper already states.

## Suggestions

1. **Reframe the theoretical section.** Remove or qualify the claim that Theorem 1 provides a formal foundation for Residual-MPPI. Acknowledge that the connection between MPPI and the maximum-entropy policy is exact only under infinite-variance noise, and that for practical finite variance the method is a principled heuristic justified by empirical results.

2. **Add Residual-SAC to at least one MuJoCo environment** (e.g., HalfCheetah) to complete the comparison with the training-based alternative. Even a brief experiment would substantially strengthen the paper's main claim.

3. **Add a brief ablation in one environment** that tests the role of the log-prior — either by replacing it with a learned terminal value estimator or by varying the horizon to see if the advantage over Guided-MPPI grows with horizon as the theory suggests.

4. **Add a hyperparameter sensitivity study** for ω′ and/or λ in one environment, or provide a simple heuristic for setting them.
