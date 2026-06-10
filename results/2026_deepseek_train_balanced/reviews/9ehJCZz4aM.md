## Summary

This paper proposes a two-module imitation learning framework: (1) an **Automatic Concept Discovery (ACD)** module that self-supervises extraction of K discrete manipulation concepts from robot proprioception using VQ-VAE with three auxiliary objectives (goal state detection, goal state evaluation, goal consolidation), and (2) a **Concept-Guided Policy Learning** module comprising a Concept Selection Transformer (CST) that predicts a distribution over concepts at each timestep and a Concept-Guided Policy (CGP) — a diffusion policy conditioned on the CST's output distribution. The key claim is that autonomously discovered concepts improve long-horizon task performance without human annotation.

## Strengths

- **Consistent empirical advantage across tasks and difficulty levels (Table 1):** The proposed method outperforms vanilla Diffusion Policy, InfoCon, XSkill, and AWE on a majority of the 6 evaluated task×difficulty combos, with the largest margins on the hardest variants (Coffee D2, Mug D1). This provides direct evidence that fusing the discovered concepts into the policy helps.

- **Ablation confirms all three ACD components contribute (Table 2):** Disabling Goal State Detection, Goal State Evaluation, or Goal Consolidation individually hurts performance across tasks. This validates that the three-strategy design is not redundant — each piece adds measurable value.

- **Qualitative concept consistency is genuinely informative:** Figure 4 shows that the discovered concepts align across different trajectories of the same task with far less variability than XSkill's concepts. Figure 5 demonstrates that the same concept index captures similar motion patterns (e.g., pulling, reaching) across entirely different tasks. These visualizations convincingly show that the method extracts something structurally meaningful.

- **Cross-task concept discovery without task-type supervision (Sec. 4.1):** ACD is trained on mixed demonstrations from all six tasks without task-type labels, yet discovers transferable concepts. This strengthens the claim of autonomous, general-purpose concept abstraction.

## Weaknesses

### Major

1. **No variance or confidence reporting for any quantitative result (Tables 1 and 2).** The paper reports success rates over 50 episodes with "fixed random seeds" but provides **no standard deviations, confidence intervals, or error bars** for any condition. With only 50 trials per entry and no measure of spread, the reader cannot determine whether the reported advantages over baselines are meaningful or within evaluation noise. This is a basic standard for empirical evaluation at a top conference and directly undermines the central quantitative contribution of the paper.

2. **Critical hyperparameters unreported: the number of concepts K and all loss weighting coefficients.** The paper defines K as the number of learnable embeddings (Eq. 1) and introduces three weighting hyperparameters λ_ent, λ_gc, and λ (Eqs. 9, 15), but **none of these values are given anywhere in the paper**. Without K, the reader cannot assess the granularity of the discovered concepts or whether the method is sensitive to this choice. Without the loss weights, the method is incompletely specified. This goes beyond a reproducibility concern — it prevents informed evaluation of the approach.

3. **Overclaim of scope:** The paper claims "state-of-the-art performance on various benchmarks" (Sec. 1, bullet 3), but the evaluation covers only **one simulator (Robosuite/MimicGen) with one robot morphology (single arm) on six tasks from a single dataset family**. There is no real-world validation, no cross-morphology testing, and no evaluation on any external benchmark. The claim is not supported by the evidence presented.

### Minor

4. **"Closed-loop" framing is oversold.** The CST is trained via cross-entropy (Eq. 11) to predict the **same labels** produced by the offline ACD encoder applied to training demonstrations. The joint training with CGP provides gradient feedback, but the CST's primary objective is to mimic the ACD encoder's offline assignments. The paper's language ("dynamic adjustment in response to environmental changes," "adapts to unforeseen situations") implies a capacity for online concept adaptation that the training procedure does not provide — the CST simply learns to reproduce the offline segmentation at inference time. The "closed-loop" claim would be better framed as *per-timestep concept reselection* rather than dynamic adaptation.

5. **XSkill baseline comparison is weakened by design.** The paper reimplements XSkill using "only robotic demonstrations" (Sec. 4.1). XSkill's core design premise is cross-embodiment transfer from human video to robot data; stripping away this modality removes its key advantage. The paper is transparent about this, but the comparison then tests a variant rather than the method as originally proposed, making the reported advantage less informative.

6. **Full-distribution conditioning partially undermines the "concept selection" narrative.** The paper passes the entire softmax distribution \(\mathcal{T}(o_t, s_t) = [p_{\text{CST}}(k|o_t, s_t)]_{k=1}^K\) to CGP rather than a single selected concept (Eqs. 13–14, lines 195–205). The paper explicitly motivates this for gradient flow, which is reasonable, but it muddies the claimed analogy to discrete manipulation skills. The rhetoric of "selecting" a concept is not well-aligned with the implementation, which feeds the policy a soft mixture over all K concepts simultaneously.

7. **Gradient-alignment assumption in Goal State Evaluation is undiscussed.** Equation 7 trains Π to map \((s_t^\tau, \nabla_{s_t^\tau} \mathcal{V})\) to the finite-difference state transition \(\nabla s_t^\tau\). This assumes that the gradient of the learned value function \(\mathcal{V}\) with respect to the proprioceptive state points in a direction aligned with the robot's actual dynamics — a strong condition that is neither discussed nor explicitly regularized. While the ablation (Table 2, w/o GE) provides empirical support that the component helps, the paper does not address this conceptual tension.

### Trivial

None.

## Nice-to-Haves

- Ablate CST vs. random concept selection, and full distribution vs. argmax selection, to isolate which aspect of the concept conditioning drives the improvement.
- Report results across multiple training seeds (not just evaluation episodes) to establish robustness.
- Add hierarchical imitation learning baselines (e.g., VQ-BeT, SPIRL) that also segment demonstrations into reusable sub-skills.

## Removed Points

The following criticisms from the input reviewers were filtered as not substantive or not verifiable from the paper:

- **Forcing baselines into DP backbone:** Using a common backbone to compare concept discovery methods is standard experimental practice; the claim that this "likely favors the proposed method" is speculative and unsupported. **Removed.**

- **AWE as a "category error":** AWE extracts minimal waypoints from demonstrations — this is a valid form of unsupervised structure discovery and a reasonable baseline for comparison. **Removed.**

- **Generic reproducibility nitpicks** about undisclosed implementation details that would normally be in the appendix (which the parser strips). **Removed.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report standard deviations or confidence intervals** for all success rates in Tables 1 and 2, computed across multiple training seeds (not just evaluation episodes). This is the single highest-leverage improvement.

2. **Disclose K and all λ values.** Without these, the method is incompletely specified and the reader cannot assess sensitivity to these choices.

3. **Tone down the "state-of-the-art" and "closed-loop adaptation" claims** to match what is actually demonstrated: per-timestep concept reselection evaluated on one simulator with six tasks.

4. **Add an ablation comparing full-distribution vs. argmax conditioning** to clarify whether the soft mixture or the concept structure drives the improvement.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>