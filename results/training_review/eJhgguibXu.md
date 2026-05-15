The paper references A.1 and A.2 only for architecture/hyperparameter details — not for results. The results section (5.4) is genuinely empty in the main body. This is a fatal flaw. Let me now produce the final consolidated review.

---

## Summary

This paper proposes using learned, task-agnostic GNN dynamics models (with per-edge update functions per object pair, dynamic edge activations, and relative coordinate frames) to guide exploration in reinforcement learning for intuitive physics tasks. The core idea is to use approximate models solely to identify rewarding action clusters (via short-horizon random rollouts and K-means clustering) and then sample from these clusters within an epsilon-greedy strategy, decoupling model use from policy learning to avoid compounding model error. **However, the paper contains no experimental results whatsoever — Section 5.4 ("RESULTS") is empty — making it impossible to evaluate any of its central claims.**

## Strengths

- **Principled decoupling of approximate models from policy learning.** The paper proposes using learned dynamics models *only* to guide exploration (via action distributions), not to generate training data for policy updates. This mitigates the well-documented problem of compounding model error corrupting policy learning (Janner et al., 2019; Abbas et al., 2021), and is a sensible design choice clearly motivated in Sections 1 and 4.2.

- **Well-motivated GNN architecture for physics prediction.** The technical design choices — distinct per-edge update functions for each object-pair type, dynamic edge activations via distance cutoffs, and relative coordinate frames — are appropriate for capturing structural invariances in physics domains. The argument for how these enable generalization to unseen object configurations and variable object counts (Section 4.1) is cogent.

- **Compelling cognitive-science framing.** The connection to human intuitive physics (Piloto et al., 2022; Allen et al., 2020) and the analogy to action priors provides genuine motivation for why *imperfect* models might still be useful for exploration, a perspective that is less explored in the model-based RL literature compared to the dominant focus on model accuracy.

## Weaknesses

### Fatal

- **Section 5.4 ("RESULTS") is entirely empty.** The section contains only the heading and the sentence fragment "Our experiments aim to answer the following questions:" — with no data, figures, tables, learning curves, quantitative comparisons, or analysis of any kind. The paper then jumps directly to Section 6 ("CONCLUSIONS"). The abstract, introduction, and conclusions repeatedly claim that the method "significantly improves the frequency of reward signals," "demonstrates accelerated convergence to optimal policies," and "can flexibly generalise to unseen tasks" (lines 4–5, 16–18, 155–159), but **not a single piece of empirical evidence is provided**. This is not a minor omission; it means the paper's core contributions are entirely unsubstantiated. A paper that makes empirical claims without any experimental results cannot be accepted in any venue.

### Major

- **The paper's claims directly assert results that do not appear in the submission.** The contributions list (lines 16–18) says the paper will "show that sampling from [model-identified] distributions significantly improves the frequency of reward signals" and "demonstrates accelerated convergence." The conclusions (lines 155–159) insist "We demonstrate that these learned models can flexibly generalise to unseen tasks and, despite being imperfect, can improve the sample efficiency of policy learning" and "We show that these learned approximate dynamics models... can reliably identify rewarding regions of the action space across tasks." These are stated as *accomplished findings*, not proposed future work, yet the empirical backing is absent. This is not a formatting artifact — it is a missing central component.

### Minor

- **The described experimental design is thin even if results were present.** The paper commits to comparing only DDPG-MGE against a single baseline (standard DDPG), with no ablation studies, no comparison to other exploration methods (e.g., curiosity-driven exploration, count-based exploration), and no model-based RL baselines (e.g., MBPO, PETS). The reliance on hand-specified subgoals (explicitly acknowledged as a limitation in line 161) limits the claimed generality. These issues would need to be addressed in any complete submission, though they are entirely secondary to the missing-results problem.

- **The paper does not evaluate the learned dynamics models' prediction accuracy.** It acknowledges that model error compounds over longer rollouts (lines 82–83) and uses subgoals to mitigate this, but provides no quantitative assessment of model quality (e.g., prediction MSE, rollout error accumulation). Such analysis would be critical for understanding when and why the guidance helps or hurts.

### Trivial

None that warrant remark given the fatal issue.

## Nice-to-Haves

- Analysis of sensitivity to key hyperparameters (rollout horizon, number of random rollouts, number of K-means clusters, epsilon threshold, distance cutoff) would strengthen any future submission.
- Automatic subgoal discovery (mentioned by the authors as future work in line 161) would improve the method's generality.
- Qualitative visualizations of the identified action clusters and failure-mode analysis would be helpful for understanding the approach.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper does not situate itself against recent work on exploration in continuous control (curiosity-driven exploration, random network distillation, Go-Explore)."* — **Removed per hard rule: DO NOT mention missing related works, as I cannot independently verify what the paper does or does not cite relative to the full literature.**

- *"Key details are missing: How many model rollouts? How many clusters? How are subgoals defined?"* — **Removed per hard rule about nitpicks on reproducibility/implementation details. These would be in the appendix (referenced as A.1 and A.2), which was stripped by the parser.**

- *"Results section may have been stripped by the parser."* — **This cannot explain the empty Section 5.4. The parser strips figure placeholders but leaves textual content. Section 5.4 contains no results text beyond a sentence fragment.**

- *"Empirical demonstration that model-guided exploration accelerates convergence."* (claimed by Strength Finder) — **Removed because no such demonstration exists in the paper. The strength is fabricated; the paper has no results.**

- *"The method requires subgoals to be specified per task, yet the paper claims the models themselves generalize."* — **This is acknowledged by the authors as a limitation (line 161) and is more appropriately classified as a nice-to-have or minor weakness, not a central flaw. Weakened and moved accordingly.**

- *Criticisms about missing proofs or theoretical analysis.* — **Not present in the reviews; included here for completeness.**

## Novel Insights

None beyond the paper's own (unsupported) contributions. The cognitive-science framing and architectural design choices are interesting ideas, but without experimental validation they remain untested proposals rather than established insights.

## Suggestions

1. **Complete the experiments.** The paper needs a full results section with learning curves comparing DDPG-MGE to standard DDPG across multiple CREATE tasks, including statistical significance measures.
2. **Add stronger baselines.** Compare against at least one model-based RL method (e.g., MBPO or a planning-based approach) and one modern exploration method (e.g., RND or ICM) to support the claim that model-guided exploration offers distinct advantages.
3. **Include ablation studies.** Isolate the contributions of the GNN architecture choices, the K-means clustering, and the epsilon-greedy schedule.
4. **Report dynamics model accuracy.** Quantify prediction error on held-out trajectories and analyze how it compounds over rollout horizons. This is essential for understanding when the guidance is reliable.
5. **Acknowledge the current state of the work honestly.** If this is a preliminary or ongoing project, the framing should match that, and claims of "demonstrating" results should be removed until evidence exists.

## Score and Decision

**Originality:** The core idea (using approximate models for exploration guidance, decoupled from policy learning, with cognitive inspiration) has merit and is reasonably novel. However, novelty without evidence carries no weight.

**Importance of research question:** The question of efficient exploration in sparse-reward continuous control is important, and the approach of leveraging imperfect models for exploration rather than planning is a sensible direction.

**Claims support:** **None whatsoever.** The paper makes strong empirical claims but provides zero experimental evidence. This is the single most critical failing.

**Soundness of experiments:** Cannot be evaluated — no experiments are reported.

**Clarity of writing:** Generally clear in the sections that are present, though the conclusions section reads as an extended abstract that restates claims as if they were already demonstrated.

**Value to the research community:** The proposed approach could be valuable if validated, but in its current form the paper provides no actionable or citable result.

The paper presents a well-motivated method and clear writing, but it is **missing the entire evidentiary component required for a scientific contribution**. The claimed empirical findings do not exist in the submission. This is a fatal flaw that cannot be addressed by minor revisions. The paper must be rejected.

**MY FINAL SCORE:** <pineapple>2.0</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>