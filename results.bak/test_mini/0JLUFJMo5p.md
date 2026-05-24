Now I have all the information I need. Let me write the consolidated review.

**Round 1 bracket:** Based on the calibration search, the paper clearly belongs in the weak band. The closest comparable paper is Compositional HyperModules (avg 2.00) which shares the same fundamental flaw (missing training procedure for the hypernetwork). Strong anchors at 8.00 are in a completely different tier. **Initial bracket: 1.5 - 3.5.**

**Round 2 narrowing:** Compared to the 2.00 anchors (Compositional HyperModules, ARRS), this paper has more content (explicit architectural equations, an ablation study, cross-task experiments, learned reward analysis) but the same fatal flaw. Compared to the 3.00 anchors (Surprise-Modulated Meta-Advantages, Posterior-GRPO), it is less well-specified and has a more severe missing-procedure problem. The paper sits between these — closer to the 2.00 end.

**Final score: 2.5** — clearly below the acceptance threshold.

---

## Summary

This paper proposes DTERM, a hypernetwork-based framework for dynamically weighting multiple reward components (syntactic correctness, functional correctness, code style, efficiency) in reinforcement learning for code generation tasks. The hypernetwork takes a task embedding (from CodeBERT) and produces per-task weights for each sub-reward, replacing the standard static or uniformly weighted reward composition. Experiments on code summarization, translation, completion, repair, and competitive programming show consistent improvements over Uniform, Expert-Tuned, and GradNorm baselines.

## Strengths

1. **Well-specified architecture with explicit equations.** Sections 4.1–4.5 formally define the hypernetwork weight generation (Eq. 5–6), FiLM conditioning (Eq. 7), prototype-based attention (Eq. 8–9), multi-modal fusion (Eq. 10), and compiler feedback (Eq. 11). The design is clearly laid out and easy to follow.

2. **Consistent improvements over static baselines across five benchmarks.** Table 1 shows DTERM outperforming Uniform, Expert-Tuned, and GradNorm on all tasks — e.g., BLEU-4 gains of +4.4 on translation and +3.4 fix rate on repair over the best static baseline.

3. **Ablation study isolating components.** Table 2 reports Pass@1 dropping from 22.7 (full DTERM) to 18.1 (w/o Hypernetwork), 19.3 (w/o Task Embedding), and 20.8 (w/o FiLM), suggesting each module contributes to overall performance.

4. **Analysis of learned reward weightings.** Figure 3 shows how DTERM assigns different sub-reward proportions per task type (e.g., style and efficiency dominate in translation; compilation success matters more in repair), confirming task-sensitive behavior.

## Weaknesses

### Fatal

None. The paper's core claims (dynamic reward weighting is beneficial) are plausible and the experimental results are directionally consistent. However, the weaknesses below are collectively severe enough to prevent acceptance.

### Major

1. **Training procedure for the hypernetwork and prototypes is never specified — this is the single biggest gap.** The paper states "We train using PPO" (Section 5.1), but PPO trains the policy network, not the hypernetwork \(H_\phi\) or the reward prototypes. How are these trained? Jointly through the RL objective? With a separate meta-objective? On a held-out set of tasks? Figure 4 shows a "meta-training loss" curve, but the loss function is never defined. Without knowing how the central architectural component is optimized, the method cannot be reproduced or assessed for generalizability. This is a structural omission, not a minor presentation issue.

2. **The evaluation compares only against static reward weightings, which does not test the paper's core claim about dynamic weighting.** The baselines (Uniform, Expert-Tuned, GradNorm) are all static or effectively static in terms of reward composition. The paper itself cites reward machines (Icarte et al., 2022), meta-learning for reward adjustment (Yang et al., ), and adaptive reward functions in Section 2.2 — yet none of these are compared against. The claimed benefit of *dynamic over static* weighting cannot be established when the only comparisons are static methods. The improvements in Table 1 could reflect any aspect of the framework (e.g., better sub-reward design, more expressive architecture) rather than the dynamic weighting itself.

3. **No statistical rigor.** Only 3 random seeds are used, and no variances, confidence intervals, or significance tests are reported for any result (Tables 1, 2; Figure 2). Given the high variance typical of RL for code generation, the numerical gaps could be noise. This weakens all experimental conclusions.

### Minor

4. **The cross-task generalization experiment (Figure 2) is underspecified.** The 10 "unseen tasks" are not described — what are they? Are they presented in a fixed order? Why do *all* methods improve across tasks (e.g., Uniform rises from 0.28 to 0.51)? If tasks are ordered by difficulty, the upward trend is trivial. If DTERM adapts per task (via online weight generation), it is not zero-shot in the claimed sense. The paper says "zero-shot adaptation" (Section 4.3 and Abstract) but does not verify that the hypernetwork operates without per-task gradient updates.

5. **The "Expert-Tuned" baseline cites Rame et al. (2023) — Rewarded Soups — which is about interpolating fine-tuned model weights, not about manually tuned reward weights for code generation.** This citation does not support the claim that "manually optimized weights from prior work" were used. The validity of this baseline is unclear.

6. **Multi-modal fusion (Section 4.4) and RLHF integration (Section 4.6) are described but never evaluated.** These are presented as capabilities of the framework but no experiments confirm they work. They should either be tested or deferred to future work.

7. **The ablation's "w/o Hypernetwork" (Pass@1 = 18.1) performs worse than the Expert-Tuned baseline (18.4).** This suggests that simply removing the hypernetwork yields performance below a manually tuned static baseline, and that the improvement in full DTERM may come from the combination of components rather than the hypernetwork specifically. This is not discussed in the paper.

### Trivial

8. Several references are missing or broken: CodeXGLUE citation appears as "(?)", and there are other placeholder citations in Sections 2.3 and 2.5.

## Nice-to-Haves

- Comparing against at least one adaptive/learned-reward baseline (e.g., a simple reward machine baseline or a meta-learned reward function) would directly test the paper's central claim.
- Reporting variances or confidence intervals for the main results would substantially improve confidence in the findings.
- Clarifying the cross-task experiment protocol (task identities, ordering, whether the hypernetwork weights are frozen or updated per task in the "zero-shot" setting) would resolve ambiguity about the claimed generalization capability.

## Removed Points

These points were flagged in the reviews but are removed per the filtering rules:

- **"The conclusion section is garbled"** — Removed as a parser/formatting artifact; the instructions note that such artifacts affect all papers uniformly.
- **"No comparison against state-of-the-art code LLMs (e.g., CodeLlama)"** — The paper's contribution is about reward weighting in an RL pipeline, not about achieving SOTA code generation scores. The evaluation compares within a controlled RL setup, which is an appropriate scope.
- **"No code release"** — Removed per the rule about not questioning availability of artifacts. The paper is under double-blind review.
- **"Missing appendix details"** — Removed per the instruction that appendices are stripped by the parser and present in the original submission.
- **Several generic strengths from the Strength Finder** (e.g., "principled modular architecture" as a standalone point without specific evidence, "diverse benchmarking" as a generic positive) — Removed as they duplicate points already captured in the Strengths section above or are too generic.

## Novel Insights

None beyond the paper's own contributions. The two reviews are largely convergent — the harsh critic identifies the real flaws (missing training procedure, weak baselines, no statistical rigor) and the strength finder identifies the real positives (architecture clarity, consistent gains, ablation). The core tension is that the paper has a plausible and potentially useful idea but fails to specify it completely enough to evaluate.

## Suggestions

1. **Specify the training procedure for the hypernetwork and prototypes.** This is essential. What is the loss function for the meta-training shown in Figure 4? Is the hypernetwork updated via the RL policy gradient, or via a separate supervised objective? What data is used for prototype learning? Without this, the paper is not reproducible.

2. **Add at least one adaptive/learned-reward baseline.** The simplest option would be a reward machine (Icarte et al., 2022) tailored to code tasks, or a meta-learned linear reward adjustment. This would directly support the claim that dynamic weighting outperforms static weighting.

3. **Report variances and use more seeds.** With only 3 seeds, reporting standard deviations or confidence intervals is necessary for any claim of improvement.

4. **Clarify the cross-task experiment.** Name the 10 unseen tasks, explain the evaluation protocol (fixed order? random order?), and verify that the hypernetwork weights are not updated per task during evaluation — or else do not call it "zero-shot."

5. **Either evaluate the multi-modal fusion and RLHF integration, or remove them from the paper.** Describing capabilities that are never tested inflates the claimed contribution without evidence.

## Score and Decision

**Score: 2.5**  
**Decision: Reject**

**Calibration anchors used:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Compositional HyperModules | 2.00 | R1/R2 | Very similar: hypernetwork for code RL, same missing training procedure flaw. Our paper has slightly more experimental content (ablation, cross-task data) but the same fundamental gap. |
| Adversarial Robust Reward Shaping | 2.00 | R1/R2 | Similar quality — underspecified method, weak evaluation. Our paper is marginally stronger in architectural clarity. |
| Thinking Before Coding | 2.50 | R1/R2 | Better experimental design but weaker novelty. Comparable overall quality. |
| Surprise-Modulated Meta-Advantages | 3.00 | R2 | Better-specified training procedure but presentation issues. Our paper is weaker — the missing training procedure is more severe than any single flaw in this anchor. |
| Posterior-GRPO | 3.00 | R2 | Well-specified method with clear training. Our paper is clearly worse — it lacks the basic specification of how its core component is trained. |
| RewardCode | 4.00 | R1 | Complete training pipeline with rigorous evaluation. Our paper is substantially less complete. |
| Process Supervision-Guided Policy Optimization | 5.50 | R1 | Thorough empirical study with clear methodology. Not comparable in rigor. |
| Efficient RL by Guiding World Models | 8.00 | R1 | Top-tier work. Not comparable. |

The paper proposes a plausible architecture for dynamic reward composition in code-generation RL, but the training procedure for its core component (the hypernetwork) is entirely unspecified, the evaluation compares only against static baselines (leaving the central claim about dynamic weighting untested), and results lack statistical rigor. These flaws are collectively fatal for the current submission. A substantially revised version with a clear training protocol, appropriate adaptive baselines, and rigorous evaluation could warrant reconsideration.

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>