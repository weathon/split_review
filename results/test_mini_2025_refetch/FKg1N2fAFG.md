Here is my final consolidated review:

---

## Summary

This paper addresses architecture overfitting in dataset distillation — the phenomenon where distilled data synthesized by a shallow training network performs poorly when used to train deeper networks of different architectures. The authors propose a collection of techniques applied during test-network training: a DropPath variant extended to single-branch networks with a three-phase keep-rate scheduler, improved shortcut connections, knowledge distillation from the smaller training network (used as teacher), periodical learning rate scheduling, the Lion optimizer, and multi-fold data augmentation. Experiments on CIFAR-10 with FRePo and MTT distillation across four architectures and three IPC settings show substantial accuracy gains (e.g., +35.7% on ResNet50 with MTT IPC=10), often closing the gap to the training network's performance.

## Strengths

1. **Well-motivated problem with clear framing.** The paper identifies a real bottleneck in dataset distillation — architecture overfitting — and demonstrates its severity quantitatively (e.g., ResNet50 drops 35.5% below the 3-layer CNN on MTT IPC=10). This provides a strong motivation for the proposed techniques.

2. **DropPath variant generalizes to single-branch networks.** Section 3.1 introduces a principled adaptation of DropPath (Larsson et al., 2016) to architectures like VGG that lack residual branches, using a virtual shortcut active only when the main path is dropped (Figure 2b). This extends ensemble-style depth regularization beyond ResNet-like architectures.

3. **Demonstrated synergy between DropPath and knowledge distillation.** Table 2 consistently shows that the Full method (DropPath + KD) outperforms either component alone across architectures and IPC settings. For example, on FRePo IPC=10 ResNet18: Full 66.6% vs. w/o DP (KD only) 64.0% and w/o KD (DP only) 63.9%. The paper provides a plausible explanation: DropPath creates an ensemble of shallow sub-networks, and KD regularizes them toward the small teacher's output.

4. **Thorough ablation structure.** The paper abates each component systematically: Table 3 separates the final-phase keep rate from improved shortcut connections; Table 4 isolates periodical LR, Lion optimizer, and stronger augmentation; Figure 4 tests sensitivity of the three-phase scheduler's hyperparameters. This allows readers to attribute gains to individual changes.

5. **Extension beyond distilled data to limited real data.** Section 4.2 and Figure 3 show that DropPath+KD enables ResNet18 and ResNet50 to outperform a 3-layer CNN even with as few as 100 training samples (fraction 0.002), whereas baseline ResNets underperform. This demonstrates generality beyond the distilled setting.

## Weaknesses

### Fatal

None.

### Major

1. **Incremental contribution from combination of well-known techniques.** Each component — DropPath, knowledge distillation, Lion optimizer, cosine annealing with warm restarts, data augmentation — is an established technique. The novel elements (single-branch DropPath adaptation, three-phase scheduler, improved shortcut) are relatively minor architectural modifications. The paper reads as an effective engineering combination rather than a conceptual advance or unified principle explaining *why* the combination works. This limits the paper's significance as a methodological contribution. The strong empirical results are real, but the paper provides little insight beyond "these heuristics work when combined."

2. **No comparison to factorization-based cross-architecture methods at comparable IPC.** The paper explicitly scopes out factorization methods (IDC, DSA, CAFE, HINT) because they operate at larger IPCs. However, the paper itself tests IPC=50, and at least some of these methods have been evaluated at IPC=50. A comparison at this IPC would directly inform whether the proposed approach is competitive with methods that also target cross-architecture transfer. Without such comparisons, the reader cannot assess whether the paper's approach is genuinely state-of-the-art for cross-architecture distillation or merely a well-tuned improvement over vanilla FRePo/MTT baselines.

### Minor

3. **Baseline tuning asymmetry is not fully ruled out.** The baseline uses "standard" settings (AdamW, cosine LR, 1-fold augmentation), while the proposed method adds Lion, periodical LR resets, and multi-fold augmentation. Table 4 shows the optimization/augmentation components each contribute, but the combined gain from these components over the baseline is large (e.g., baseline 61.6% → with all optimizations 66.6%). Without evidence that the baseline hyperparameters were tuned per architecture, some of the reported gains may reflect suboptimal default choices rather than the core DropPath+KD mechanism.

4. **Main results table is CIFAR-10 only.** Table 2 reports comprehensive results for CIFAR-10; CIFAR-100 and Tiny-ImageNet results are relegated to the appendix. For a paper claiming generality, a summary of those results (even one row per dataset) should appear in the main text to establish that findings transfer beyond a single dataset.

5. **Missing empirical comparisons to simpler DropPath schedules and DropOut.** The three-phase schedule is compared against "no final phase" (Table 3), but not against a constant keep rate (e.g., p=0.5 throughout). Similarly, the paper argues DropPath is preferred over DropOut because it reduces depth, but provides no direct comparison. These would strengthen the justification for the proposed design choices.

### Trivial

6. **No wall-clock or GPU-memory efficiency analysis** despite claiming "negligible overhead." Adding multi-fold augmentation and knowledge distillation inference on the teacher may increase training time measurably.

7. **Practical guidance for setting the three-phase scheduler hyperparameters** (decay period, minimum keep rate) is not provided beyond the specific values used. Figure 4 shows sensitivity to these choices, making tuning guidance valuable for practitioners.

## Nice-to-Haves

- Comparison to SGD with momentum (in addition to AdamW) would strengthen the optimizer ablation (Table 4).
- The paper's observation that a stronger teacher helps at larger data fractions (Appendix Figure 7) is important enough for the main text, as it clarifies when the method saturates and how it can be extended.
- Reporting standard deviations in the main table (currently in Appendix Table 8) would improve interpretability.

## Removed Points

- **"Absence of comparison to existing cross-architecture methods" (framed as Fatal):** Moved from Major to Minor. The paper explicitly justifies the exclusion of factorization methods based on IPC regime (Section 2, line 43: "the IPC used in these methods is at least 5 times larger"). This is a principled scoping decision, not an omission. The criticism is downgraded to Minor (point 2 above) because a comparison at IPC=50 with some factorization methods would still strengthen the paper.

- **"Definition of 'almost overcome' is missing":** Removed. The paper shows specific accuracy numbers with gaps in parentheses (Table 2); readers can assess whether gaps are "almost overcome" quantitatively. This is a framing preference, not a factual gap.

- **"Comparison to standard regularization techniques (weight decay, dropout, label smoothing)":** Removed. The paper's motivation is architecture overfitting specific to distilled data, not general regularization. Scope creep.

- **"Strong-teacher analysis should be in the main text":** Moved to Nice-to-Haves. The paper references it in Section 4.2 and points to Appendix B.5. Important but not a flaw.

- **"Missing related work":** Removed per guidelines — I cannot verify whether these references exist.

- **"Loss landscape flatness comparison (Figure 9) in appendix":** Removed. This is a parser artifact; the content exists in the original submission.

- **Strengths removed from Strength Finder:** Generic/superficial strengths (e.g., "this paper addressed an important problem") removed. Only concrete, evidence-backed strengths retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension between the paper's strong empirical results and its limited conceptual novelty, but do not add new observations about the method or problem beyond what the paper itself provides.

## Suggestions

1. Add a comparison against at least one factorization-based method (e.g., IDC or DSA) at IPC=50 on CIFAR-10 to benchmark against the cross-architecture literature directly.
2. Run a small hyperparameter sweep for each baseline architecture on one setting (e.g., MTT IPC=10) to demonstrate the baseline is not significantly under-optimized.
3. Move a summary of CIFAR-100 and Tiny-ImageNet results to the main text (even as a small table or a sentence with key numbers).
4. Add an efficiency table reporting wall-clock time and GPU memory for each configuration tier.
5. Provide a simple heuristic for setting the three-phase scheduler hyperparameters (e.g., "decay period = number of training epochs / 2, minimum keep rate = 0.5").
6. Compare the three-phase DropPath schedule against a constant low keep rate (e.g., p=0.5) and against DropOut under otherwise identical settings.

## Score and Decision

**Round 1 bracket (4–7):** The paper comfortably exceeds weak <3.5 anchors (flawed papers withdrawn/rejected at scores 2–3) and is clearly below the >7.5 anchors (oral/spotlight papers with high novelty). The relevant band is the middle.

**Round 2 narrowing:** Compared to:
- *Dataset Distillation via Adversarial Prediction Matching* (5.0, Reject): The current paper has a clearer problem framing, stronger and more controlled ablations, and more dramatic empirical gains. **→ Current paper is stronger.**
- *Enhancing Dataset Distillation with Concurrent Learning* (5.33, Reject): Similar level of empirical rigor, but the current paper's problem (architecture overfitting) is better motivated and the evaluation is more comprehensive (more architectures × IPC combinations). **→ Current paper is slightly stronger.**
- *Prioritize Alignment in Dataset Distillation* (5.0, Reject): The current paper has stronger evidence and more systematic ablation, but PAD has a simpler, cleaner idea (alignment). **→ Comparable, current paper slightly stronger on evidence.**
- *Towards Lossless Dataset Distillation via Difficulty-Aligned Trajectory Matching* (7.0, Accept Poster): That paper introduces a novel algorithmic insight (difficulty-aligned trajectories) and demonstrates lossless distillation at large IPCs. The current paper's combination of existing techniques is a weaker conceptual contribution. The current paper has more thorough cross-architecture evaluation. **→ Current paper is weaker.**
- *Dataset Distillation via Knowledge Distillation for SSL* (7.0, Accept Poster): That paper pioneers a new setting (SSL for DD) with theoretical grounding. The current paper addresses a known problem without comparable theoretical analysis. **→ Current paper is weaker.**

**Final score: 5.5.** The paper tackles a real problem with well-executed experiments and strong empirical results, but is held back by (i) limited conceptual novelty (combination of existing techniques with minor modifications), (ii) missing comparisons to relevant factorization-based methods at comparable IPC, and (iii) primary evidence concentrated on CIFAR-10 in the main text. The paper is borderline — a resubmission that addresses the comparison gap and provides a more unified insight would be a stronger contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>