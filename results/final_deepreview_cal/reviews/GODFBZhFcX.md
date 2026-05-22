## Summary

This paper introduces PCE (Planner-Composer-Evaluator), a framework that extracts implicit assumptions from LLM reasoning traces, structures them into a decision tree, and scores each path by likelihood, gain, and execution cost to guide uncertainty-aware action selection in decentralized multi-agent embodied environments. The core idea — that LLM planners already generate assumptions in their reasoning, and that explicitly structuring these assumptions into a decision tree enables better planning than heavy inter-agent communication — is well-motivated and novel. Experiments across two benchmarks (C-WAH, TDW-MAT) and three LLM backbones (GPT-4o mini, GPT-OSS:20B, Gemma3:4B) show PCE consistently outperforms four communication-centric baselines in task efficiency and success rate while maintaining comparable token usage.

## Strengths

- **Novel and well-motivated mechanism.** The idea of extracting assumptions latent in LLM reasoning traces and structuring them into a decision tree for systematic evaluation is genuinely novel. Unlike prior work that relies on iterative communication (CoELA, REVECA, CaPo) or cognitive-step trees (ToT), PCE treats environmental assumptions as first-class decision variables. This is a clean conceptual shift from communication-centric to reasoning-centric uncertainty handling.

- **Consistent improvements across backbones and environments.** Tables 1 and 2 show PCE achieves the best total steps in C-WAH (e.g., 42.76 vs. 46.80 for REVECA with GPT-4o mini) and highest success rate in TDW-MAT (87.50% vs. 81.25%) across all three diverse LLM backbones. The consistency — PCE wins every backbone/benchmark combination — is strong evidence that the benefit comes from the framework structure, not from a particular model's quirks.

- **Component ablation validates all three modules.** Table 3 shows removing the Planner (+13.7 steps), Composer (+4.06 steps), or Evaluator (+4.58 steps) all degrade performance, and the *w/o Planner* ablation reveals a 3× token-cost increase, confirming the Planner's reasoning trace is a crucial source of relevant assumptions.

- **User study with human participants.** The within-subjects study (12 participants, 7-point Likert) shows PCE scoring highest on Appropriateness, Usefulness, Efficiency, and Trust, providing qualitative evidence that selective communication is perceived as more cooperative than both no-communication and always-communication baselines.

- **Rigorous problem formulation.** Section 3 formalizes the setting as a DEC-POMDP with one-step message delay and a cost equation (Eq. 2) separating movement and communication via indicator functions, grounding the work in a well-defined theoretical model.

## Weaknesses

### Major

- **No statistical reporting on any comparative results.** Tables 1, 2, and 3 report only point estimates with no standard deviations, confidence intervals, or significance tests. C-WAH has only 10 episodes per condition and TDW-MAT has 24. Without variance information, the observed differences between PCE and the second-best baseline (e.g., 42.76 vs. 46.80 steps in C-WAH, GPT-4o mini) could fall within the noise of environment stochasticity or LLM output variability. This is the most significant weakness — the claims are likely correct, but the evidence as presented is less rigorous than the field's standards demand.

- **Scaling ablation (Figure 3) lacks error bars and has few observations per cell.** The paper argues that scaling alone yields "limited performance improvements relative to its computational cost" and that PCE's gains are additive. The data consists of three model sizes and three reasoning depths with 10 episodes per cell and no variance information. While the consistent gap between PCE and Planner-only lines is suggestive, the claim about the *limits* of scaling is a claim about effect size, and the experimental design is underpowered to support it decisively. The additive-benefit claim (PCE helps at every scale) is better supported than the scaling-ceiling claim.

### Minor

- **Scoring components (ℒ, 𝒢, 𝒞) rely on LLM judgments without main-paper validation.** The paper mentions human-expert correlation studies in Appendix A.10 and A.11, but the main text includes no summary statistics (e.g., correlation coefficients). A reader cannot assess whether the evaluator's likelihood and gain estimates are meaningfully accurate or just noisy approximations. Adding even one summary statistic (e.g., "Evaluator likelihood scores correlate with human judgments at ρ = 0.82") to the main paper would substantially improve credibility.

- **Composer's local ranking policy is underspecified.** The paper states the policy is "approximated using LLMs' commonsense reasoning" (Section 4.3), but it is unclear whether this involves an additional LLM call per node or is embedded in the same prompt that generates the tree. The total number of LLM calls per planning step is not quantified, making it difficult to assess computational cost precisely.

- **User study has limited statistical robustness.** 12 participants is a moderate sample, and the paper does not report inter-rater reliability or individual-level variance (only bar-chart averages in Figure 4). The study is useful as qualitative evidence but is not powered for strong quantitative conclusions.

- **The *w/o Planner* ablation's massive token increase is unexplained.** Token usage jumps from ~44k to ~140k when the Planner is removed. The paper notes this but does not explain *why* — is the Composer generating many irrelevant assumptions from scratch without the Planner's guidance? This would be a valuable analysis to include.

- **Only two environments tested, both simulated household tasks.** The paper acknowledges this in the conclusion, but the limited diversity means generalizability to other domains (e.g., outdoor navigation, search-and-rescue, dynamic environments) remains unaddressed.

### Trivial

- None.

## Nice-to-Haves

- A concrete case study (beyond the abstract example in the introduction) showing a specific planning step where the Planner's initial action was suboptimal, the Composer exposed a better alternative, and the Evaluator correctly identified it. This would make the mechanism transparent.
- Hyperparameter sensitivity analysis (α, β, λ, D) in the main paper rather than only in the appendix.
- Comparison with a reasoning-only baseline (e.g., self-consistency over multiple CoT samples) more clearly separated in the main paper.

## Removed Points

These points were raised in the input reviews but removed per the synthesis guidelines:

- **Figure 4 caption typo (PCE listed twice):** Removed per formatting-artifact rule — this is a PDF-parser duplication, not an author error.
- **"Hyperparameter sensitivity is relegated to an appendix":** Removed per the rule against criticisms of missing appendix content — the appendix exists in the original submission.
- **"CoTS includes MCTS and the comparison is not in the main paper":** The paper references Appendix A.8 for this comparison. While it would be nice to have in the main paper, the appendix exists in the original submission.
- **"The paper should report per-episode variance" framing as a fatal flaw:** Downgraded from "fatal" to "major" because the method itself is sound and the evidence is directionally consistent; the weakness is in the rigor of reporting, not in the validity of the approach.
- **Strength Finder's "principled problem formulation" was kept as it is specific and grounded in Section 3.**

## Novel Insights

None beyond the paper's own contributions. The key insight — that implicit assumptions in LLM reasoning traces can be extracted, structured into a decision tree, and scored for uncertainty-aware planning — is the paper's own contribution, not something synthesized from the reviews.

## Suggestions

1. **Add variance reporting to all main results.** The single most impactful improvement: report standard deviations or 95% confidence intervals for Tables 1, 2, and 3, and add error bars to Figure 3. Given the small episode counts, a paired bootstrap or simple standard error would suffice and would dramatically increase the credibility of the comparative claims.

2. **Add a summary of the evaluator correlation study to the main paper.** Even a single sentence (e.g., "Evaluator likelihood scores correlate with human expert judgments at ρ = 0.82, N = 50") would bridge the current credibility gap in the scoring mechanism.

3. **Clarify the LLM call budget per planning step.** Specify exactly how many LLM calls the Planner, Composer, and Evaluator each make per step, and how the Composer's local ranking relates to the tree depth D.

4. **Explain the *w/o Planner* token explosion.** A brief analysis of why removing the Planner causes token usage to triple would be informative (e.g., does the Composer generate many irrelevant branches without the Planner's trace as a seed?).

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| CaPo (KRv9NubipP) | 6.00 | R2 | Weaker — CaPo is a baseline in PCE's paper and was criticized as "minimal innovation"; PCE has a genuinely novel mechanism and better cross-backbone validation |
| CoELA (EnXJfQqy0K) | 6.50 | R2 | Comparable — CoELA was pioneering work in the same line; PCE has a more novel technical contribution (assumption extraction vs. LLM communication) and component ablation, but CoELA was first |
| COMBO (YXRyYkb1im) | 6.67 | R2 | Slightly weaker — COMBO's compositional video diffusion model is technically more complex; PCE's contribution is cleaner conceptually |
| Tree-Planner (Glcsog6zOe) | 5.25 | R1 | Stronger — similar tree-based approach but single-agent, single-backbone, single-benchmark; PCE operates in more challenging multi-agent partially-observable setting |
| Generative World Explorer (8NlUL0Cv1L) | 6.25 | R1 | Comparable — different approach (video generation vs. reasoning structuring) to partial observability; both are strong |
| DeLLMa (Acvo2RGSCy) | 7.33 | R2 | Weaker — DeLLMa has a more formal decision-theoretic framing and more varied experimental settings, pulling ahead of PCE |
| HAZARD (n6mLhaBahJ) | 6.75 | R2 | Different type — benchmark paper with LLM evaluation; not directly comparable |

**Round 1 bracket:** [6.0, 7.0]. PCE is clearly stronger than CaPo (6.00) and Tree-Planner (5.25), comparable to CoELA (6.50) and Genex (6.25), and weaker than DeLLMa (7.33).

**Round 2 narrowing:** Compared against CaPo (6.00), CoELA (6.50), and COMBO (6.67), PCE sits between CoELA and COMBO. It has a cleaner conceptual contribution than CaPo (which was criticized as prompt engineering), comparable novelty to CoELA, and slightly less technical machinery than COMBO.

**Final score: 6.5.** The paper has a genuine contribution and a well-executed experimental campaign across multiple backbones and environments, but the systematic lack of variance reporting keeps it from the 7+ tier. This weakness is common in the area (CaPo and Tree-Planner had the same issue and were accepted), and PCE's contribution is strong enough to warrant acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>