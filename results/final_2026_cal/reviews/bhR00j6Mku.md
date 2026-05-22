Now I have enough calibration context. Let me compile the final review.

**Calibration Summary:**
- **Round 1 bracket:** [(3.0, 5.33), 8.0]. Contamination detection papers in the weak-to-middle band (3.0–5.33) are substantially less thorough. The 7.5+ band returned no topically similar papers; those existing are at 6.5–7.33 on tangentially related topics. The paper sits above the middle anchors.
- **Round 2 narrowing:** Found "Preference Leakage" (6.50, accepted poster) — a comparably thorough contamination study with similar empirical breadth but less theoretical depth. Our paper has stronger mechanistic analysis (Theorem 3.1, ablation isolating clipping) and addresses a more practically urgent problem. This places it above 6.5.
- **Final score: 7.0.** Better than the 6.5-level anchors due to its theoretical contribution and controlled experiments, but not at the 7.5+ level of exceptionally novel or comprehensive contributions.

Now the review:

## Summary
This paper systematically investigates benchmark contamination detection in large reasoning models (LRMs) across two realistic scenarios: (I) contamination during SFT that is subsequently obscured by RL training, and (II) final-stage SFT contamination with chain-of-thought data on already-capable LRMs. The paper demonstrates that GRPO training can conceal SFT contamination evidence through PPO-style importance sampling and clipping (supported by theoretical analysis and controlled ablations), and that CoT contamination on advanced LRMs evades nearly all existing detection methods near random-guess levels. The findings reveal a critical vulnerability in LRM evaluation.

## Strengths

**First systematic study of benchmark contamination in LRMs.** The paper identifies a genuinely new problem — contamination in the multi-stage LRM training pipeline — and provides the first comprehensive evaluation across 10 detection methods, 6 benchmarks, and multiple model families (Qwen, Llama, DeepSeek-R1-Distill). The framing around two contamination stages (pre-LRM and post-LRM) is well-motivated and cleanly structures the contribution.

**Mechanistic explanation with theoretical backing.** Theorem 3.1 and the subsequent analysis establish that PPO-style importance sampling and clipping drive the contraction of the member/non-member NLL gap. Table 3 provides a clean causal validation: GRPO and RAFT++ (with clipping) produce sharp AUROC drops, while removing clipping restores detection to near-baseline levels. This theory-experiment alignment is the paper's strongest evidence and goes beyond what prior contamination detection papers provide.

**Rigorous controlled experiments ruling out alternative explanations.** The paper explicitly tests and rejects the "forgetting" hypothesis through two controlled experiments: (i) training GRPO on mixed clean-and-contaminated data still conceals contamination (Table 2), and (ii) continuing SFT on clean data does not reduce detectability (Figure 2). This careful isolation of the RL objective itself as the causal mechanism is methodologically sound.

**Stage II findings are striking and practically important.** Table 4 shows pass@1 gains of up to 12 percentage points, while Table 5 shows all 10 detection methods hovering near 50-60% AUROC. The log-prob density overlap (Figure 4) provides clear visual evidence. The practical implication — model developers could inflate benchmark performance while leaving minimal traces — has immediate relevance to leaderboard integrity.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

**1. The "broad class of RL methods" claim rests on two algorithms sharing the same mechanism.** The paper tests GRPO and RAFT++ (both with importance sampling/clipping) and shows concealment, while RAFT (without) does not. The theory correctly attributes concealment to the clipping mechanism. However, directly testing a standard PPO implementation (or REINFORCE/RLOO) under the same conditions would strengthen the generality claim from a plausible inference to a directly validated finding. As it stands, the evidence supports the mechanism claim but extrapolates to "a broad class" primarily by reasoning from the mechanism.

**2. Stage I concealment is incomplete for some detection methods at 64 steps.** LiRA retains 80.14% AUROC after GRPO (down from 89.13%), which the paper acknowledges. The paper argues correctly that more steps produce monotonic decline (Figure 2) and that typical LRM training uses far more steps, making the trend the relevant signal. However, the headline numbers in Table 2 show reduction, not elimination, for the strongest detectors. This nuance should be kept in mind when interpreting claims about "concealment."

**3. The theoretical analysis is informal.** Theorem 3.1 is derived under simplifying assumptions (tabular setting, small step size, correct trajectories only). The analysis is useful as a conceptual explanation and aligns cleanly with the empirical ablation, but it is not a rigorous proof in the formal sense. The authors acknowledge this, but the presentation (with "Theorem 3.1") may overstate the formality. This is a minor presentation concern, not a substantive flaw.

**4. Stage II generalization explanation is qualitative.** The paper argues that LRMs "internalize the underlying knowledge and reasoning process" leading to generalization to non-members. This is plausible and consistent with the evidence, but a direct memorization metric (e.g., exact match of answer strings or CoT segments between members and non-members) would strengthen the claim. Without it, the root cause remains partly inferred rather than directly observed.

### Trivial
- The paper would benefit from confidence intervals or variance estimates for AUROC values in Tables 2 and 5, particularly for methods near the 50% threshold where small fluctuations matter.
- Figure 2 could list numerical AUROC values on the bars for easier cross-referencing with Table 2.

## Nice-to-Haves
- Testing a standard PPO implementation under identical Stage I conditions would directly validate the "broad class of RL methods" claim.
- A memorization quantification analysis in Stage II (e.g., comparing exact-match rates on members vs. non-members) would improve confidence in the generalization explanation.
- Reporting main results at a higher GRPO step count (e.g., 156 steps where reference-free methods hit near-random) would better illustrate the full concealment trajectory.

## Removed Points
- *Criticism about incomplete concealment being overstated:* The paper explicitly acknowledges the partial concealment and hedges appropriately ("may inherently exhibit similar concealment," "we expect that extensive GRPO training would render..."). The harsh critic's framing overstates the evidential gap — the trend and prediction are clear. Demoted to Minor.
- *Criticism about no PPO/REINFORCE testing:* Retained as Minor because the test is a natural extension, but softened — the paper's mechanism-level validation (RAFT vs. RAFT++) already provides strong causal evidence, and the claim is appropriately hedged ("suggests that a broad class may inherently exhibit").
- *Criticism about missing confidence intervals:* Demoted to Trivial — single-run evaluations are standard for large-scale benchmark experiments; confidence intervals would be nice but not standard methodology in this setting.
- *Strength about "first systematic study":* Retained — the paper explicitly claims this and supports it with evidence across two stages, 10 methods, 6 benchmarks.
- *Strength about "theoretical identification of root cause":* Retained — verified by Table 3 ablation.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- In the revision, add a clear statement at the end of Section 3 noting that for reference-based methods like LiRA, concealment is partial at 64 steps and requires more training steps to approach random, while reference-free methods reach near-random at 156 steps. This manages reader expectations about the current results.
- Consider adding error bars to figures showing AUROC trends, particularly for methods whose values fluctuate near 50%.

## Score and Decision

**Score: 7.0**
**Decision: Accept**

The paper makes a timely, well-executed, and significant contribution to an important problem. It identifies a real vulnerability in LRM evaluation that has direct implications for leaderboard integrity, supports its claims with diverse experiments, provides a mechanistic explanation with theoretical backing, and carefully rules out alternative explanations. The weaknesses are minor and addressable — they do not undermine the core claims. The paper is clearly stronger than comparable contamination detection papers in the 4-6 range and deserves acceptance.