Now I have sufficient anchors to calibrate. Let me finalize my assessment.

**Bracket:** Round 1 placed the paper between ~5.5 and 7.5. Round 2 narrows: comparing against "Detecting Pretraining Data" (6.25), "How much can we Forget" (6.75), "To the Cutoff... and Beyond?" (6.75), "Proving Test Set Contamination" (7.50), and "LiveBench" (7.33). Our paper has broader empirical scope and cleaner ablations than the 6.25-6.75 anchors, with important practical implications. It's below the 7.33-7.50 anchors in conceptual novelty (no new method/benchmark) but compensates with thoroughness. **Final score: 7.0.**

---

## Summary
This paper presents the first systematic study of benchmark contamination detection in Large Reasoning Models (LRMs), revealing that existing detection methods are fragile in two realistic scenarios: (I) RL training (GRPO) can conceal SFT contamination evidence that was previously detectable, and (II) final-stage CoT contamination on advanced LRMs leaves almost no detectable trace, with detectors performing near random. Through controlled experiments, theoretical analysis, and ablation studies, the authors trace the concealment in Stage I to PPO-style importance sampling and clipping objectives, and argue that LRMs' generalization ability—rather than memorization—explains the Stage II detection failures.

## Strengths
- **Strong empirical demonstration across two contamination stages.** The paper shows that after GRPO training, AUROC drops consistently across 10 detection methods and 6 benchmarks (e.g., Loss detector falls from 75.48% to 61.26% AUROC; Table 2), and that extensive CoT contamination on advanced LRMs yields large pass@1 gains (up to ~10 points, Table 4) while detectors hover near random (Table 5). The scope and consistency of these results are compelling.

- **Clean ablation isolating the concealment mechanism.** Table 3 is the paper's strongest single result: removing clipping from GRPO and RAFT++ restores Loss-detector AUROC to near-baseline (73.28% and 74.39% vs. 75.48% no-RL), while RAFT (no clipping, no importance sampling) shows no concealment at all. This directly pins the concealment on the PPO-style objective, not on additional training or forgetting.

- **Well-controlled experiments ruling out alternative explanations.** The paper shows that further clean SFT does not degrade detection (Figure 2, Table 23), while RL with identical data does—confirming the RL optimization dynamic, not just extra training, is responsible. The pass@1 results (Table 1) also confirm that contaminated models do not forget the contamination, ruling out the forgetting hypothesis.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The theoretical exposition in Section 3.2 is compressed and relies on a simplified tabular model with a small natural-gradient step.** The derivation sketches the intuition that clipping dampens non-member trajectories more heavily, but the mapping from the abstract Δ_x expression to per-algorithm instantiations could be clearer. The empirical ablation (Table 3) provides strong independent support, so this does not undermine the core findings, but the claim that "a broad class of RL methods" inherently conceals contamination would benefit from a more complete and qualified theoretical presentation in the main text.

- **Stage II non-members are drawn from the same benchmark distribution as members.** The paper splits each benchmark 50/50 into member/non-member sets, which is standard practice. However, the "barely leaves evidence" conclusion is therefore a statement about within-distribution separability. In practice, a detector might compare the contaminated benchmark against an entirely different out-of-distribution reference set. The paper's Discussion section (lines 337-338) argues that LRMs generalize to distributionally similar questions, which is a plausible explanation, but acknowledging the within-distribution scope of the claim would strengthen the paper.

- **No variance estimates for AUROC values.** Detection scores are averaged over 8 rollouts per question, but standard deviations or confidence intervals are not reported. Given that some AUROCs are close to 50%, reporting variability would help readers assess statistical robustness. The drops are large and consistent enough that this does not threaten the conclusions.

- **Models are limited to 7-14B parameters on reasoning benchmarks.** The paper does not include a limitations paragraph discussing whether findings scale to larger models or different domains (e.g., coding benchmarks). This does not weaken the presented results but bounds the generality claims.

### Trivial
- The abstract's "alarmingly easy" and "brief GRPO training" language is slightly imprecise: the results show a monotonic decline across steps rather than immediate failure, and 156 steps—while modest compared to full-scale RL—may not qualify as "brief" to all readers. The framing is acceptable but could be tightened.

## Nice-to-Haves
- A step-wise AUROC analysis for the ablation variants (GRPO without clipping, RAFT++ without clipping) at multiple training steps, mirroring Figure 2, would further characterize how clipping drives concealment over time.
- An auxiliary experiment or qualitative discussion of how Stage II detection would change if non-members came from a different distribution would clarify the scope of the conclusion.
- Testing one additional clipping-based RL algorithm (e.g., standard PPO) would harden the "broad class of RL methods" claim, though the ablation on clipping already provides strong evidence.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Concern about the appendix proof being stripped and therefore unverifiable.** Removed per policy: the parser strips appendix sections from all papers; the proof exists in the original submission. The theoretical exposition in the main text was evaluated on its own terms.

- **Demand for confidence intervals as a fatal or major concern.** Downgraded to minor. Single-run evaluation without CIs is standard in large-scale LLM benchmarking; the AUROC drops are large and consistent across methods and benchmarks.

- **Request for additional related work citations.** Removed per policy: we do not suggest missing related works without external confirmation.

## Novel Insights
The paper's most interesting insight is the mechanistic link between PPO-style clipping and contamination concealment. The theoretical decomposition into μ (mean push) and β (covariance reweighting) terms, combined with the ablation showing that removing clipping alone restores detection, provides a clean explanation for *why* RL training obscures contamination signals. This goes beyond the common observation that "more training helps models generalize" and identifies a specific algorithmic feature—the clipping gate that dampens off-policy trajectories—as the root cause. This has implications beyond contamination detection: it suggests that the same clipping mechanism that stabilizes RL training may systematically erode other distributional signals that practitioners rely on.

## Suggestions
- Make the theoretical section more self-contained by presenting a concise proof sketch of the key inequality (why Δ_N − Δ_M < 0 under clipping) in the main text, with clearly stated assumptions. The ablation already carries the empirical argument; the theory should be framed as an explanatory mechanism rather than a standalone rigorous proof.
- Add a brief limitations paragraph acknowledging model size (7-14B) and domain (reasoning benchmarks) scope.
- Report standard deviations for key AUROC results, at minimum in the appendix.
- Contextualize the Stage II results by noting that the within-benchmark split may represent a best-case scenario for detectors and briefly discussing out-of-distribution implications.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Evading Data Contamination Detection... (Nk1MegaPuG) | 4.25 | R1 | Our paper has far more thorough experiments, theory, and ablations; clearly stronger |
| Detecting Pretraining Data from LLMs (zWqr3MQuNs) | 6.25 | R2 | Our paper has broader scope (10 detectors, 6 benchmarks, 2 stages, multiple models) and cleaner ablations; stronger |
| LiveCodeBench (chfJJYC3iL) | 6.25 | R2 | Different type of contribution (benchmark); our paper's analytical depth is comparable or stronger |
| Infilling Score (9QPH1YQCMn) | 6.25 | R2 | Our paper has broader scope and more practical implications |
| How much can we Forget about Data Contamination? (Nsms7NeU2x) | 6.75 | R2 | Both combine theory + experiments; our paper has broader validation across detection methods and clearer practical takeaways; comparable or slightly stronger |
| To the Cutoff... and Beyond? (m2NVG4Htxs) | 6.75 | R1/R2 | Both are well-executed contamination studies; our paper has broader scope and mechanistic insights; comparable or slightly stronger |
| LiveBench (sKYHBTAxVa) | 7.33 | R1/R2 | Major benchmark contribution with lasting community value; our paper is an analysis/exposure paper with less lasting infrastructure; slightly below |
| Proving Test Set Contamination (KS8mIvetg2) | 7.50 | R2 | Novel method with theoretical guarantees; higher conceptual novelty than our paper; slightly below |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowed to:** 6.5–7.5. The paper is stronger than the 6.25 anchors (more comprehensive, cleaner ablations, broader validation) and comparable to or slightly stronger than the 6.75 anchors. It sits below the 7.33–7.50 anchors, which propose novel methods or benchmarks with lasting infrastructure value. **Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>