Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

VICtoR introduces a hierarchical reward model for long-horizon robotic manipulation that decomposes tasks into stages, motions, and within-motion progress. The model uses GPT-4 for task decomposition, a stage detector based on object-state classification, and a motion progress evaluator trained with three complementary contrastive losses on short-horizon action-free videos. Experiments in a custom simulated environment show consistent improvements over prior VIC methods (up to 43% on harder tasks), with qualitative real-world validation on XSkill data and ablation studies confirming each hierarchical component's importance.

## Strengths

- **Novel hierarchical decomposition for VIC reward modeling.** The paper correctly identifies three specific deficiencies of prior VIC methods for long-horizon tasks (no sub-stage awareness, confusion from variable difficulty, lack of object-state reasoning) and designs a three-tier architecture — stage, motion, progress — that directly addresses each one. This goes beyond simply applying CLIP or LIV to longer tasks.

- **The three contrastive losses (time, motion, language-frame) are principled and individually ablated.** Each objective targets a distinct capability needed for the motion progress evaluator. Table 3 (referenced in the paper) shows that removing any one degrades performance, with the progress signal having the largest impact. This provides strong internal validation of the design.

- **Generalization to unseen compositions from short-horizon training data.** VICtoR is trained only on single-motion videos yet can compose rewards for arbitrary sequences of those motions. The VICtoR(task) baseline, trained on full-task videos without decomposition, performs worse — demonstrating that the hierarchical structure is responsible for this compositional generalization, not just more data.

- **Consistent improvement over multiple baselines across 10 tasks of varying horizon.** The paper reports a 25% average improvement and 43% on harder tasks. While the environment is custom, all methods are evaluated under identical conditions, making the relative comparison credible.

- **Qualitative real-world validation and embedding visualizations** provide additional evidence that the learned representations capture motion identity and task progress in a structured way, consistent with the method's design.

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses listed below are addressable and do not invalidate the paper's core claims.

### Minor

- **Evaluation relies solely on a custom environment without validation on any standard long-horizon benchmark.** The paper justifies the custom environment by noting that Calvin is too challenging for VIC methods and that other benchmarks lack conditional dependencies between steps. However, this means the reported 43% improvement has been demonstrated only on one specific testbed whose difficulty relative to established benchmarks is uncalibrated. At minimum, reporting the environment's design parameters (number of objects, motion set, observation space dimensions) in sufficient detail for reproduction would help, as would attempting evaluation on a subset of Calvin or MetaWorld long-horizon tasks — even with low absolute success rates, relative comparisons remain informative.

- **Real-world experiments are purely qualitative.** The paper claims validation "in both simulated and real-world environments" (abstract), but the real-world component (Section 4.4) only visualizes potential curves for correct/incorrect task executions on the XSkill dataset. No policy learning is conducted in the real world, no success rates are reported, and no quantitative comparison with baselines is provided. While qualitative analysis can be a useful sanity check, it does not demonstrate that the rewards enable an agent to learn a task in the real world. The claim of real-world validation is thus overextended.

- **The application of potential-based shaping to LOReL and LIV baselines is underspecified.** The paper states "We apply the same reward shaping method for LIV and LOReL as discussed in Section 4.3" (line 179). However, Section 4.3 defines a potential function φ (Equation 5) that depends on stage, motion number, and progress — outputs that LOReL (a classifier score) and LIV (a similarity score) do not produce. Without explaining how these baselines' outputs are converted into a potential suitable for shaping, the fairness of the comparison cannot be fully assessed. If a different conversion was used, the paper should describe it; if the same formula was naively applied, it may be mismatched.

- **Key implementation details are missing, hurting reproducibility.** (a) The GPT-4 prompt for task knowledge generation is not provided, despite this being a critical component. (b) The object state classifier P in the Stage Detector is mentioned but its architecture, training data, and training procedure are not described. (c) The custom simulation environment is described in only one short paragraph and a figure; the number of objects, set of possible motions, observation space (image resolution, camera viewpoint), and exact task generation method should be specified.

- **No analysis of reward model errors or failure modes.** The paper does not report the accuracy of the Stage Detector (how often it picks the wrong stage) or the motion classifier. Since both are intermediate components that feed into the reward, understanding where errors occur would (a) reveal failure modes and (b) strengthen the connection between design and performance. Similarly, sensitivity to the confidence threshold λ_c is not analyzed.

- **Inference time and computational cost are not reported.** The method uses GPT-4 (via API, with latency) and an object detector at each timestep, which raises practical questions about whether the reward model can run at a frequency useful for real-time RL training. Reporting wall-clock time per reward computation would help.

### Trivial

- The claim of being "the first to explore the potential of VIC rewards for long-horizon manipulation tasks" is a minor overstatement that does not affect the paper's value — the contribution stands on its technical merits regardless of priority.

## Nice-to-Haves

- A simple "CLIP-reward" baseline (using raw CLIP similarity between observation and instruction without fine-tuning) would help calibrate the improvement over a zero-shot lower bound.
- Reporting mean and variance across multiple seeds in the main text (the tables exist in the original but were not visible in the review copy due to parser handling of `\input`).
- A sensitivity analysis of reward-model performance to the confidence threshold λ_c.

## Removed Points

*These points are flagged to be removed due to hard-rule conflicts; treat them with caution.*

1. **"Ground-truth object detector may give VICtoR an indirect advantage."** — The paper states the ground-truth detector is used for *policy training* (shared across all methods), not for the reward model (which uses MDETR). All baselines use the same policy setup, so there is no asymmetric advantage. Removed because the criticism is factually misaligned with the paper's description.

2. **"The LaTeX `\input` commands prevent numerical results from being visible."** — The tables exist in the original submission; this is a parser limitation, not an author omission. Removed per the rule on parser artifacts.

3. **"The paper should report mean and variance across multiple seeds in the main text, not only in the tables."** — The tables (which exist in the original) presumably contain these statistics. Without confirming they are absent, this is speculative. Removed.

4. **"No comparison with a simple CLIP-based zero-shot reward."** — This is a wishlist item, not a weakness in the existing experiments. Moved to Nice-to-Haves.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's strong internal validity (well-controlled ablation, consistent relative improvements) and its limited external validity (custom environment, qualitative real-world results). The hierarchical decomposition approach — separating stage detection (object-state based) from motion identification and progress (embedding-similarity based) — is a genuinely principled way to address the three challenges identified in Figure 1. What is less clear is whether the gap between VICtoR and LOReL/LIV would persist on standardized benchmarks or in real policy learning on a physical robot. The reviews do not surface any flaw in the method itself, only in the completeness of its empirical demonstration.

## Suggestions

1. **Provide the GPT-4 prompt and object state classifier details** (possibly in supplementary material) to enable reproduction.
2. **Clarify how the LOReL and LIV baselines' outputs are mapped to the potential-based shaping framework.** A single sentence per baseline would resolve the ambiguity.
3. **Add a quantitative real-robot evaluation** or, at minimum, temper the claim of "real-world validation" to reflect the qualitative nature of the current evidence.
4. **Document the custom environment** with a table listing objects, motions, observation space, and task-generation procedure.
5. **Report Stage Detector and motion classifier accuracy** to validate the intermediate modules that the reward depends on.

## Score and Decision

This paper presents a novel, well-motivated hierarchical approach to VIC reward modeling for long-horizon manipulation. The method is principled, the ablation studies support the design choices, and the simulated experiments show consistent and substantial improvements over existing VIC methods. The weaknesses — reliance on a custom environment, qualitative-only real-world experiments, underspecified baseline comparison, and missing implementation details — are real but addressable and do not undermine the core contribution. The paper would benefit from additional validation on a standard benchmark and a more complete real-world evaluation, but in its current form it makes a solid contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>