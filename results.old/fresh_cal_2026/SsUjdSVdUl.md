Now I have sufficient calibration. Let me synthesize and write the final review.

## Summary

Critique-RL proposes a two-stage reinforcement learning approach for training critique language models without relying on stronger supervisors. In Stage I, it directly optimizes the critic's discriminability (whether it correctly judges response correctness) via a binary reward signal. In Stage II, it optimizes helpfulness (constructive feedback) using refinement-based rewards while preserving discriminability through explicit regularization. The key insight — that indirect reward signals from actor refinement fail to optimize discriminability — is well-diagnosed via training dynamics analysis (Figure 3). Experiments on math reasoning tasks with Qwen2.5-3B/7B show substantial improvements: e.g., 85.20% Acc@Dis vs. CTRL's 71.42% on MATH for the 7B model, and a 9.02% overall accuracy gain on in-domain tasks.

## Strengths

1. **Clear diagnosis of a concrete failure mode.** Section 4.1 and Figure 3 demonstrate that RL with only indirect rewards (r_refine, r_Δ, r_correction) fails to improve the critic's discriminability, causing the critic to become either overly conservative or overly aggressive. This finding is well-supported by training dynamics and novel — prior work (Retroformer, CTRL) did not identify this issue.

2. **Substantial and consistent empirical improvements.** Table 1 shows large gains across all metrics (Acc, Δ, Acc@Dis) for both 3B and 7B models, over all baselines. The improvements in discriminability are particularly striking — e.g., 82.80% vs. 69.29% (CTRL) on MATH-3B, and 85.20% vs. 71.42% (CTRL) on MATH-7B — and these directly translate into accuracy improvements.

3. **Well-designed ablations validate the two-stage design.** Table 3 shows that removing either Stage I or Stage II degrades performance, and removing the discrimination regularization in Stage II causes clear drops (82.8→77.7 Acc@Dis on MATH-3B, 69.9→61.6 on AQuA). This provides strong internal evidence for the method's design.

4. **Generalization across model scales and OOD tasks.** Consistent gains are demonstrated on 3B and 7B models, across in-domain (MATH, GSM8K, AQuA) and OOD tasks (SVAMP, TheoremQA). Additional results on Llama3.2 and DeepSeek-R1-Distill (in appendix) suggest the approach is architecture-agnostic.

5. **Iterative training shows further gains.** Table 2 shows that a second iteration of Critique-RL improves Acc@Dis from 82.8% to 86.5% and Acc from 48.6% to 51.0% on MATH-3B, suggesting the method can bootstrap its own improvement rather than plateauing.

## Weaknesses

### Major

1. **Confounded RL algorithm comparison with baselines.** Critique-RL uses RLOO while Retroformer uses PPO and CTRL uses GRPO (lines 258, 282). The paper does not control for the RL algorithm across methods, so the reported improvements over these primary baselines may partially reflect the choice of RLOO rather than the two-stage design. The ablations (w/o Stage I, w/o Stage II) are controlled because they share the same RL algorithm, but the comparison to Retroformer and CTRL — which establishes the contribution's advantage over prior work — is confounded. This does not invalidate the paper, but it weakens the headline claim that "Critique-RL outperforms other baselines" (Section 5.2). The authors should either run baselines with RLOO or run Critique-RL with PPO/GRPO to isolate the effect of the two-stage approach.

2. **No measures of variance or statistical significance.** All reported results are single runs without error bars, standard deviations, or any statement of variance. RL training is inherently noisy; without multiple seeds or significance tests, the reader cannot assess whether the large reported gains (e.g., the 9.02% improvement on MATH) are robust or could fall within the noise of a single run. This gap affects Table 1, Table 2, Table 3, and Table 4.

### Minor

1. **Stage II ablation does not disentangle the two discrimination-preserving components.** Table 3 removes both r_dis and the KL(π_Stage-I || π_Stage-II) regularization together ("Stage II w/o discrimination"). A cleaner ablation would compare Stage II with: (a) r_refine only, (b) r_refine + r_dis (no KL), and (c) r_refine + KL (no r_dis) to pinpoint which component matters more.

2. **Inference compute scaling comparison is unclearly presented.** Figure 1 (right) attempts to compare Critique-RL against sampling multiple responses without critique. While the caption explains "@2k and @3k" as sampling multipliers, the explanation of how compute budgets are matched between methods is insufficient. The paper states (line 341) that K× response-critique-refinement sampling is compared to 3K× parallel sampling, but the figure's legend contains unclear entries and the compute-matching protocol is not spelled out. This undermines a non-trivial efficiency claim.

3. **OOD gains on TheoremQA are modest.** Table 4 shows small improvements on TheoremQA (16.8 vs. 16.1 for 3B, 21.4 vs. 21.1 for 7B). While directionally consistent, this tempers the claim of "substantial" generalization to hard OOD tasks. The paper is honest about this but should acknowledge the limitation more explicitly.

4. **The binary r_dis reward in Stage I is a coarse signal.** The discriminability reward (Eq. 7) is 1 if the critic's final judgment matches the oracle, 0 otherwise. It does not capture step-level judgment accuracy. While pragmatically justified, the paper does not discuss whether finer-grained rewards could further improve performance or whether the binary signal might lead to reward hacking (e.g., the critic predicting the majority class). Some analysis of step-level accuracy would strengthen the paper.

5. **Preliminary analysis limited to one model and one task.** The motivating analysis (Section 4.1, Figure 3) is performed only on GSM8K with Qwen2.5-3B. While sufficient for motivation, the paper should note that failure modes could be task- or model-specific.

### Trivial

1. **Missing hyperparameter sensitivity analysis for β₁, β₂.** The Stage II objective has two reward terms with potentially different scales, but no ablation over β₁ values is provided.

2. **No analysis of the actor's refinement success rate given correct vs. incorrect critiques.** If the actor often fails to follow valid criticism, the RL signal for helpfulness will be noisy.

## Nice-to-Haves

- Running controlled experiments where Retroformer and CTRL are re-implemented with RLOO (or Critique-RL with PPO/GRPO) to isolate the two-stage contribution.
- Multi-seed reporting (even 3 seeds with mean/std) for at least the main results table.
- A cleaner inference compute scaling figure with unambiguous compute budgets and clearer legends.
- An analysis of the actor's refinement behavior (e.g., how often does the actor successfully follow correct critiques vs. incorrect ones?).

## Removed Points

- **"No stronger labeling" claim is imprecise** — The paper clearly states "without stronger labeling" meaning without a stronger model for critique annotation. The oracle reward is a rule-based verifier for math. The paper is sufficiently precise.
- **Duplicate legend entries in Figure 1** — This is a PDF parsing artifact, not an author error.
- **Missing appendix content** — The parser strips appendix sections; they exist in the original submission.
- **Generality of the preliminary analysis** — Already addressed as a minor weakness; the harsh critic's framing was overly strong.
- **Stage II reward ablation not re-tuning β₁, β₂** — This is a generic critique that could apply to any ablation; the drops are small and the finding is still informative as-is.
- **Reward hacking concern about binary r_dis** — The concern is speculative without evidence; the paper's training dynamics show the critic does improve discriminability.

## Novel Insights

The most interesting observation emerging from the reviews is that the two-stage design's success hinges on an asymmetry that the paper does not fully emphasize: discriminability is *easier to optimize directly* (via a simple binary reward on the original response) but *hard to maintain while optimizing helpfulness*. This suggests that discriminability and helpfulness are not merely competing objectives but operate at different levels of optimization fragility — discriminability is a necessary foundation that is easily disrupted by helpfulness-focused RL. The KL regularization toward Stage I essentially acts as an anti-catastrophic-forgetting mechanism for a specific capability, which is a framing that could be made more explicit and may generalize to other multi-objective RL settings for LLMs.

## Suggestions

1. **Address the RL algorithm confound.** This is the most impactful improvement. Either: (a) re-implement Retroformer and CTRL using RLOO (same base RL algorithm) and re-run comparisons, or (b) implement a version of Critique-RL using PPO or GRPO to show the two-stage design works regardless of the underlying RL algorithm. Even a single controlled comparison would substantially strengthen the paper.

2. **Add variance estimates.** Report mean and standard deviation over at least 3 random seeds for the main results (Table 1). If compute constraints prevent this, explicitly state that the reported numbers were verified to be stable across multiple runs with qualitative evidence.

3. **Clarify the inference compute scaling analysis.** Provide a cleaner version of Figure 1 (right) with unambiguous compute budgets. Explicitly state the total FLOPs or token counts for each method so readers can verify the compute-matching claim.

## Score and Decision

**Score bracket from Round 1 (Bracketing):** I compared Critique-RL against three bands of anchors. The low band (score ~3) contains withdrawn/rejected critique-model papers that are clearly weaker. The middle band (score 4–7) contains relevant papers like RefCritic (4.0), DeepCritic (4.67), Critique-Coder (5.50), and RLoT (6.0). The high band (score 8+) contains papers on different topics and is less relevant. My initial bracket was [5.0, 7.0].

**Round 2 (Narrowing):** I examined full reviews of RefCritic (4.0, Reject), DeepCritic (4.67, Reject), Critique-Coder (5.50, Accept Poster), Advancing LLM Reasoning (4.50, Reject), and RLoT (6.0, Accept Poster). Critique-RL is substantially stronger than RefCritic (which was rejected for novelty concerns and lack of comparison to prior work) and DeepCritic (which relies heavily on a strong teacher model). It is comparable to or slightly stronger than Critique-Coder (which uses a simpler single-stage approach with critique data augmentation). It is comparable in quality to RLoT (which was accepted as Poster).

**Anchors consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| he7BMZwm8t (Critique to Verify) | 3.00 | 1 | Weaker withdrawn paper on a related topic |
| y2P0h8Bxm8 (Critique-Post-Edit) | 3.00 | 1 | Weaker withdrawn paper |
| X2V46Zwcwi (From Faithfulness to Correctness) | 3.00 | 1 | Weaker withdrawn paper |
| aONZZA0oIQ (Taming LLMs) | 2.00 | 1 | Weaker withdrawn paper |
| qgMvotqkXd (RefCritic) | 4.00 | 1,2 | Similar topic but weaker: novelty concerns, no clear diagnosis of failure mode |
| wyCnT4BUsT (DeepCritic) | 4.67 | 1,2 | Similar topic but depends on strong teacher; Critique-RL is more principled |
| QpYBbBZHoF (LLaVA-Critic-R1) | 4.50 | 2 | Different domain (vision-language); comparable quality |
| 5FzN1nM20e (Advancing LLM Reasoning) | 4.50 | 1,2 | Related but different focus (self-critique in GRPO) |
| Dw034qKrP5 (RLoT) | 6.00 | 2 | Comparable quality tier; accepted as Poster |
| tsuxIeLUsz (Critique-Coder) | 5.50 | 2 | Similar topic; simpler approach; accepted as Poster |
| ebgsbC4x5W (Online Rubrics) | 6.50 | 2 | Different topic; not directly comparable |
| oBXfPyi47m (Efficient RL) | 8.00 | 1 | Different topic; higher quality tier |

Critique-RL sits comfortably above the 4.0–4.67 papers (RefCritic, DeepCritic) and is comparable to the 5.5–6.0 papers (Critique-Coder, RLoT). Considering its genuine contribution (diagnosis of the indirect reward failure mode) balanced against the RL algorithm confound and lack of variance reporting, a score of **6.0** is appropriate. This is a solid paper that makes a clear contribution and should be accepted, but the authors should address the RL algorithm confound.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>