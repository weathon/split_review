Now I have thoroughly verified all claims against the paper. Here is the consolidated meta-review.

---

## Summary

This paper introduces VICtoR, a hierarchical Vision-Instruction Correlation (VIC) reward model for long-horizon robotic manipulation. It decomposes tasks into stages (via GPT-4), detects current stage through object state classification, and assesses in-motion progress through contrastive video-language embeddings. The reward model is trained on short, action-free motion videos and composed for unseen long-horizon tasks. Simulation experiments using PPO show 25% average improvement and 43% improvement on harder tasks over prior VIC methods (LOReL, LIV), with ablation studies confirming the importance of each hierarchical level.

## Strengths

- **Principled hierarchical decomposition of VIC rewards for long-horizon tasks.** The paper identifies three concrete limitations of flat VIC methods (no sub-stage awareness, variance in difficulty, ambiguous object state) and directly addresses each with stage detection, motion classification, and progress assessment. The ablation study confirms that removing any level degrades performance, validating the architecture's structure (Section 5.3).

- **Consistent and substantial improvements in simulation policy-learning experiments.** Across 10 tasks (3 single-stage, 7 multi-stage), VICtoR outperforms all baselines including LOReL, LIV, and a task-level variant of the same method. The 43% relative improvement on tasks with >3 motions is a meaningful gain that traces directly to the hierarchical design (Tables 1 & 2, discussed in Section 5.2).

- **Well-designed contrastive objectives that produce interpretable representations.** The three losses — time-contrastive, motion-contrastive, and language-frame contrastive — are each motivated by a specific capability needed in the reward model. The t-SNE visualization (Figure 5a) confirms motion embeddings cluster by motion class, and the dynamic motion-switching visualization (Figure 5b) shows the model tracks progress within motions, not just coarse classification.

- **Compositional generalization from short motion videos to unseen long-horizon tasks.** The design of training on modular motion-level videos and composing them at inference via GPT-4-generated task knowledge is a practical approach to generalization. This is demonstrated across 10 tasks with varying composition.

## Weaknesses

### Fatal
None. The core simulation results with policy learning are valid and support the paper's main claims.

### Major

- **Overclaiming real-world validation.** The paper's conclusion states VICtoR "successfully operates in ... real-world environments" (line 216). However, Section 5.4 only visualizes potential curves on the XSkill dataset — it does not perform policy learning, robot rollouts, or any manipulation in the real world. Showing that reward potentials increase on correct demos and decrease on incorrect ones is a useful sanity check, not evidence that the reward model enables successful real-world policy learning. This should be reframed as a qualitative analysis of the reward model's outputs, not operational validation. The simulation results are the paper's main evidence and are solid; the overclaim is unnecessary and weakens the paper's credibility.

- **GPT-4 task decomposition is a critical component that is entirely unevaluated.** The entire reward structure depends on GPT-4 correctly decomposing tasks into stages with accurate object-state conditions and motion lists (Section 4.1). The paper provides no analysis of decomposition quality — no accuracy metrics, no human evaluation, no error taxonomy, no robustness to prompt variations, no discussion of failure modes (e.g., non-linear task structure, ambiguous states). While LLM-based decomposition is common practice, the paper's claims about generalization would be stronger if this component's reliability were characterized. This is a missing experiment, not a framing issue.

### Minor

- **Object state label requirements are underspecified.** The paper states that motion-level videos are "autonomously annotated" with object state labels (Section 4, overview). No method for autonomous annotation is described. In simulation, a ground-truth detector is used (line 178). For real-world application, the practical mechanism for obtaining object state labels without manual effort is unclear. The paper correctly notes it is "action-free" (no action labels), but the claim of autonomous annotation needs elaboration or removal.

- **Hyperparameters λ₁, λ₂, λ₃ and confidence threshold λ_c are not specified, ablated, or justified.** The loss function (Eq. 4) weights three contrastive objectives, and the confidence threshold λ_c (Eq. 7–8) determines when the model trusts its motion prediction. Neither the chosen values nor sensitivity analysis are provided. Given that these hyperparameters control the balance of three training signals and a decision boundary at inference, this is a nontrivial gap.

- **The potential function constant λ_m is vaguely defined.** The paper says λ_m is "a constant near the maximum of progress" (line 162), but does not specify how it is determined, how sensitive performance is to its value, or whether it is tuned per task.

- **No variance or confidence intervals reported for main results.** The paper mentions running "multiple tasks with multiple seeds" (line 178) but only reports point estimates (e.g., "25% average improvement," "43% improvement"). Without variance information, the reliability of the reported improvements is difficult to assess. (If the tables — stripped by the PDF parser — include standard deviations, this point is partially addressed; the text should still discuss them explicitly.)

### Trivial

- The definition of the confidence ratio (Eq. 8) uses `confidence = S(m, l^{motion*}) / (S(m, l^{motion*}) + S(m, l^n))`, but `l^n` (embedding of "arbitrary agent movements") is not defined in the main text — only referenced in Section 4.3's training objectives. A brief definition at the inference point would improve clarity.

## Nice-to-Haves

- Evaluating on a standard long-horizon benchmark (e.g., a modified version of CALVIN with simplified action spaces) would increase comparability. The paper's justification for a custom environment is reasonable, but it limits external validation.
- A small human evaluation of GPT-4 decomposition quality (e.g., 20–50 tasks rated for stage completeness, motion accuracy, object state correctness) would substantially strengthen the paper's trustworthiness.
- Real-robot policy rollouts with VICtoR rewards (even a small number) would substantiate the conclusion's claim about real-world operation.

## Removed Points

These points were flagged by reviewers but are either factually incorrect, misunderstood, or do not survive verification against the paper:

1. **"Object state labels contradict the action-free framing."** — Removed. The paper claims "action-free" meaning no robot action labels, not no labels at all. This is standard terminology in the VIC literature. The paper never claims to be label-free. However, the related concern about unspecified *autonomous annotation* is kept in the Minor section above.

2. **"Baselines LOReL and LIV are unfairly modified."** — Removed. The paper transparently states the modifications (backbone replaced to CLIP for fair comparison, same reward shaping applied) and provides the rationale. This is a standard and appropriate experimental control.

3. **"The environment is custom and not standard."** — Removed as a standalone weakness. The paper provides a reasoned justification (existing benchmarks lack inter-step dependency or are too challenging for VIC methods). The concern about limited comparability is noted as a Nice-to-Have, not a weakness.

4. **"Potential-based shaping terminology could confuse."** — Removed. Pure presentational nitpick.

## Novel Insights

None beyond the paper's own contributions. The reviews surface important gaps (GPT-4 evaluation, real-world overclaim) but do not contribute new conceptual observations beyond what the paper already articulates about the benefits of hierarchical VIC rewards.

## Suggestions

1. **Reframe the real-world experiments.** Clearly label Section 5.4 as a qualitative analysis of reward model outputs, not operational validation. Remove or soften the claim of "successfully operates in real-world environments" from the conclusion. Replace with language about "promising qualitative results on real-world data suggesting reward quality."

2. **Add a GPT-4 decomposition quality study.** Even a small-scale human evaluation (20 tasks, rating stage completeness, motion accuracy, state correctness) would significantly strengthen the paper's methodological foundation.

3. **Specify hyperparameter values and add at least a brief sensitivity analysis** for λ₁, λ₂, λ₃, λ_c, and the potential constant λ_m. Report whether these were tuned per-task or fixed across all experiments.

4. **Elaborate or retract the "autonomously annotated" claim.** If object state labels come from a ground-truth simulator in the main experiments, say so. If there is a real autonomous annotation pipeline, describe it.

5. **Report variance** (standard deviations or confidence intervals) for the main success rate results, or at minimum note their absence and discuss the expected variability of the reported improvements.

## Score and Decision

The paper makes a genuine contribution — it is the first systematic exploration of hierarchical VIC rewards for long-horizon tasks, with well-designed contrastive objectives and consistent simulation results showing meaningful improvements over prior methods. The weaknesses are real but addressable: the GPT-4 evaluation and hyperparameter documentation are missing experiments that can be run, the real-world overclaim is a presentation fix, and the variance issue is a reporting gap. None invalidate the core simulation-based contribution. The paper should be accepted with a recommendation to address these points in the final version.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>