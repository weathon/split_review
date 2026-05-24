Now I have a thorough understanding of both the paper and the calibration anchors. Let me compile my final review.

---

## Summary

This paper systematically decomposes the GRPO loss function to identify which components are essential for post-training LLMs on math reasoning. Through controlled ablations on small models (Qwen2.5 0.5B/1.5B, Llama3.2 1B) trained on GSM8K, the authors find that (1) negative feedback is essential — positive-only methods collapse, (2) group-relative advantage estimation is critical for stability, and (3) PPO-style clipping and policy ratios are unnecessary. They propose RGR, a simplified REINFORCE variant that retains group-relative advantages but drops PPO-style constraints, and show it matches or modestly exceeds GRPO across 9 benchmarks.

## Strengths

- **Compelling evidence that negative feedback is essential.** The training curves in Figure 1 are the paper's strongest result: GRPO-pos and RAFT show clear reward and response-length collapse (especially for Qwen2.5-0.5B, where both drop to near zero within 20 steps), while GRPO and RGR maintain stable trajectories. This is a clean, interpretable finding backed by all three model sizes.

- **Systematic, well-structured ablation design.** The paper tests five variants (GRPO, GRPO-pos, RGR, REINFORCE, RAFT) in a principled decomposition: first removing negative feedback, then removing clipping/ratios, then removing advantage estimation entirely. This isolates each component's role and makes the causal story clear.

- **Multi-model, multi-benchmark validation.** Results are reported across three model families (Qwen2.5-0.5B, Qwen2.5-1.5B, Llama3.2-1B) and nine benchmarks spanning English math, Chinese math, and STEM subjects (Tables 1–3). The pattern — RGR matching or exceeding GRPO while positive-only methods degrade — holds broadly, strengthening the generalizability claim.

- **Timely and practically relevant research question.** GRPO has become a de facto standard for reasoning post-training (DeepSeek-R1, etc.), yet its loss function combines several components whose individual contributions were not well understood. The finding that PPO-style clipping can be dropped simplifies future implementations and aligns with Ahmadian et al. (2024)'s argument that pre-trained LLMs may not need PPO's variance-reduction machinery.

## Weaknesses

### Fatal

None.

### Major

- **No quantification of statistical reliability — single training runs throughout.** All training curves (Figure 1) and benchmark results (Tables 1–3) come from a single training run per method per model. With differences between RGR and GRPO frequently in the 1–3 percentage point range (e.g., Qwen2.5-0.5B on GSM8K: 53.1 vs. 50.9; Qwen2.5-1.5B on MATH: 46.7 vs. 44.2), the reader cannot distinguish genuine improvement from between-run noise. The claim that RGR "surpasses GRPO on 17 over 27 tasks" overstates the evidence without error bars or multiple seeds. The core finding that RGR *matches* GRPO is better supported by the training curves (Figure 1), which show comparable trajectories, but the "surpasses" framing is not.

### Minor

- **KL regularization is retained without ablation or theoretical justification.** RGR keeps the KL penalty but the paper never explains why it is kept, what role it plays, or what would happen without it. Given the paper's stated goal of identifying which components are "essential," testing a variant without KL (pure REINFORCE + group-relative advantage) would directly answer this question. As written, RGR is "GRPO minus clipping" rather than a minimal REINFORCE variant, which slightly overstates the simplicity claim relative to the experimental evidence.

- **Training setup is narrow (1,800 GSM8K instances, ~65 steps, 0.5B–1.5B models).** The paper acknowledges hardware constraints, and the effects shown (collapse vs. stability) are clear at this scale, but the practical relevance to realistic GRPO training (typically longer horizons, larger models, and larger datasets) remains an open question. The generalization of stability claims to those settings is not demonstrated.

- **RAFT baseline details are sparse.** The paper describes RAFT's mechanism at a high level but does not specify the number of top responses used, learning rate, or whether the process is iterative. While RAFT's collapse is only one piece of evidence for the negative-feedback claim (GRPO-pos and REINFORCE provide independent corroboration), more detail would aid reproducibility.

### Trivial

- The abstract and introduction use "more efficient" to describe RGR, but RGR uses the same group sampling and KL computation as GRPO, offering no demonstrated computational efficiency gain. "Simpler" or "more transparent" would be more precise.

- The training curves (Figure 1) use a 10-step running average smoothing, which is noted in the caption but could benefit from raw-point overlays to convey variance within each window.

## Nice-to-Haves

- Run each method with at least 3 different seeds and report mean ± std on benchmark scores. Even a modest number of repeats would substantially strengthen the comparative claims.
- Ablate the KL penalty from RGR (i.e., test pure REINFORCE + group-relative advantage) to fully answer the question posed by the title.
- Include a hyperparameter sensitivity analysis (learning rate, KL coefficient, group size) to assess whether RGR's simplicity translates to robustness.
- Extend training beyond 65 steps or use a larger training set (e.g., MATH training split) to test whether the stability and relative ranking of methods holds over realistic training horizons.
- Report reasoning-process metrics (e.g., average trace length on benchmarks, diversity of reasoning paths, rubric-based scoring) rather than relying on a single qualitative example (Figure 2) for claims about emergent reasoning behaviors.

## Removed Points

*These points were flagged by reviewers but are not included as weaknesses above.*

- **"Equation 1 overloads r_{i,t} as both reward and policy ratio."** This is incorrect — r_{i,t} in Equation 1 is explicitly defined as the policy ratio π_θ/π_θ_old (line 89), which is standard notation in the PPO/GRPO literature. The harsh critic misread this. **Removed.**

- **"The text refers to Table 4 but no such table exists."** No reference to "Table 4" appears in the paper. **Removed.**

- **"The KL gradient in Equation 2 is written in a nonstandard way."** Equation 2 writes ∇_θ D_KL inside the sum over timesteps, consistent with how GRPO's loss (Equation 1) places the KL term inside the per-token summation. The notation is reasonable. **Removed.**

- **"The paper lacks discussion of hyperparameter sensitivity."** This is a nice-to-have for a small-scale study; standard practice in this subfield does not require comprehensive sensitivity analysis. Moved to Nice-to-Haves.

- **"Implementation details for KL term are absent, hampering reproducibility."** The paper provides code and Appendix A with hyperparameters. KL estimation details (e.g., estimator type) would help but are not a substantive weakness given the code release. **Removed as a standalone criticism.**

- **"The claim that RAFT fails because it lacks negative feedback is not fairly substantiated — the failure may reflect poor tuning."** The evidence for negative feedback being essential does not rest primarily on RAFT. GRPO-pos (which uses the same GRPO infrastructure minus negative advantages) also collapses, and REINFORCE (no advantage estimation at all) collapses even harder. RAFT's failure is corroborative, not load-bearing. **Removed.**

- **"RAFT baseline poorly specified; how many top responses, is it iterative, what learning rate?"** RAFT by definition uses top-1 per prompt. Additional detail would help but this does not affect the paper's core claims. Moved to Minor.

## Novel Insights

The paper's most novel empirical insight is that PPO-style clipping — long considered essential for stable RL training — appears genuinely unnecessary when fine-tuning LLMs from strong initial policies with group-relative advantage estimation. While Ahmadian et al. (2024) argued this for standard REINFORCE vs. PPO (with a value-function baseline), this paper extends that finding to the GRPO setting (with group-relative baselines), showing that the advantage normalization alone provides sufficient stability. The sharp contrast between RGR (stable) and plain REINFORCE (collapses) in Figure 1 isolates advantage estimation — not clipping — as the true stabilizer, which is a clean and instructive result.

## Suggestions

- Tone down the "surpasses" language in the abstract and conclusion to "matches or modestly exceeds," and explicitly note that the comparisons are from single runs. The paper's strongest contribution is that clipping can be *removed without loss*, not that RGR is reliably *better*.
- Add a sentence or short paragraph explaining why KL regularization is retained in RGR (e.g., it prevents the policy from drifting too far from the reference, which is standard practice in RLHF). This closes an obvious reader question.
- Consider renaming RGR to something like "Simplified GRPO" to avoid implying it is a pure REINFORCE variant — it still uses group-relative advantages and KL, which are meaningful complexity.

---

## Score and Decision

**Calibration anchors considered across both rounds:**

| Anchor ID | Paper | Avg Score | Round | Comparison |
|-----------|-------|-----------|-------|------------|
| ZK1NnjpjEs | LLM NLU with RL | 3.00 | R1 (low) | Clearly weaker — smaller scope, less systematic |
| jOuHjFw71C | Planning in Strawberry Fields | 3.00 | R1 (low) | Different topic, weaker contribution |
| 28TLorTMnP | Soft Alignment for LLMs | 2.50 | R1 (low) | Clearly weaker |
| JNZ3Om6NPS | Inherent limitations of GPT | 2.00 | R1 (low) | Not comparable, weaker |
| F0GNv13ojF | Effective RL Reward for LLM Reasoning | 5.17 | R1 (mid) | Similar topic; our paper has clearer ablation but smaller scale |
| BGnm7Lo8oW | Learning to Reason at Pre-Training Scale | 5.50 | R1 (mid) | Different focus; our paper more focused and cleaner story |
| gdzpnRBP4F | RLSF: RL from Self-feedback | 4.50 | R1 (mid) | Our paper stronger — more systematic, clearer results |
| fWRBheSJth | GReaTer: Gradient-based Prompt Optimization | 6.67 | R1 (mid) | Stronger than our paper — more novel method |
| mMPMHWOdOy | WizardMath | 8.00 | R1 (high) | Much stronger — major contribution, extensive experiments |
| FIXk0RP960 | Does RLHF Scale? | 5.50 | R2 | Our paper has clearer contribution |
| ZRDa2IT1sQ | Step-Controlled DPO | 6.00 | R2 | Comparable quality; our paper more systematic but smaller scale |
| cijO0f8u35 | Scaling Relationship Math Reasoning | 5.25 | R2 | Our paper stronger — more actionable findings |
| fsX9nFwMNj | BNF: Bidirectional Negative Feedback Loss | 6.00 | R2 | Most comparable — both propose loss simplifications with systematic ablations; similar quality and contribution level |

**Bracketing:** Round 1 placed the paper between roughly 5.0 (above weak RL reward-design papers like F0GNv13ojF at 5.17) and 8.0 (below major contributions like WizardMath). Round 2 narrowed this to approximately 5.5–6.5, with the closest anchors being fsX9nFwMNj (BNF, 6.00, Accept — loss simplification paper with similar strengths/weaknesses profile) and ZRDa2IT1sQ (SCDPO, 6.00, Reject — math reasoning improvement with execution gaps). Our paper is slightly weaker than BNF in experimental thoroughness but comparable in contribution clarity and ablation design. It is stronger than ZRDa2IT1sQ in systematicity and honesty about limitations.

**Final score:** 6.0 — a solid, well-structured contribution with a clear ablation story and practically relevant findings, held back by single-run evaluation (no statistical reliability) and limited training scale. Comparable to other accepted papers at this level.

**Originality:** Good — the systematic decomposition of GRPO is novel and directly addresses a gap in the rapidly growing GRPO literature.

**Importance:** The question is timely and practically relevant, given GRPO's central role in reasoning post-training. The finding that clipping can be dropped will simplify future implementations.

**Claim support:** Strong for the negative-feedback and advantage-estimation findings (Figure 1); adequate but not fully rigorous for the "RGR surpasses GRPO" claim (no error bars, single runs).

**Soundness:** The experimental design (controlled ablations, multiple models and benchmarks) is sound. The main weakness is lack of statistical quantification.

**Clarity:** The paper is well-structured, the ablations are clearly motivated, and the figures/tables are informative. Minor imprecision in wording ("efficient").

**Value to community:** The paper provides actionable guidance (drop clipping, keep negative feedback and advantage estimation) that can directly inform GRPO implementations and future research.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>