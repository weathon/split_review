Now I have enough information to write my final review. Let me compile it.

**Round 1 Bracket:** Based on the calibration search, this paper sits between the lower anchors (4.67-6.00) and the higher anchors (7.00-8.00). The most relevant comparisons are the TTA-for-VLM papers at 6.20-6.67 and the long-tailed+VLMs paper at 7.00.

**Round 2 Narrowing:** Comparing against the 6.67 anchor (RLCF: TTA for VLMs, accepted), the 6.25 anchor (L2C: Few-shot test-time domain adaptation, accepted), and the 6.20 anchor (PROGRAM: prototype-based TTA, accepted): this paper has stronger novelty (first to tackle LT-TTA for VLMs), more extensive evaluation (15 datasets vs. fewer), and theoretical propositions. However, it has more presentation/clarity issues (CRA loss specification not fully clarified, no variance reported). The paper is stronger than the 6.20-6.25 anchors but has more significant clarity gaps than the 6.67 anchor. I place it at **6.5**.

Here is my final review:

## Summary
This paper introduces L-TTA, the first test-time adaptation method designed for Vision-Language Models (VLMs) under long-tailed test distributions, identifying two failure modes (text-induced tail erosion and modality-bias amplification) and proposing three co-designed components: Synergistic Prototypes (DPs + EPs), Rebalancing Shortcuts (RSs) with a class re-allocation loss, and Balanced Entropy Minimization (BEM).

## Strengths
- Exclusionary Prototypes (EPs) provide a principled solution to tail-class under-representation by updating all class prototypes on every view weighted by prediction confidence (Eq. 5). Ablation (Table 6) confirms EPs contribute independently, with macro-F1 dropping 3.22% when removed.
- Comprehensive evaluation: 15 datasets across 3 benchmarks (OOD, Cross-Domain, Corruption) at imbalance ratios {10, 20, 50} with 11 baselines. L-TTA achieves best or runner-up in 41/48 metric-by-dataset cells, with gains typically widening at higher imbalance ratios.
- BEM is accompanied by theoretical propositions (Props. 1-2) that formalize head-class bias in standard EM and show BEM reduces the head-tail gradient gap. The (1-P̃)^β penalty term is well-motivated and ablation (Fig. 4d) confirms β=1 as optimal.
- Efficiency analysis shows favorable trade-off: L-TTA runs in 1.45h (ImageNet, imb=10) vs. 18.30h (RLCF) and 27.70h (WATT), while outperforming all baselines on HM scores.
- Generalization across four CLIP-family backbones (ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG) with consistent improvements (~1.5% Acc. / ~1.8% Mac.).
- Ablation on dynamic head/tail-class ordering (Table 7) tests a realistic stress case and shows stability across different sampling orders.

## Weaknesses
### Major
None.

### Minor
1. **CRA loss optimization not specified.** The class re-allocation loss (Eq. 7) uses c_{c,j}(v) = 𝟙(j = Argmax(...)), which is non-differentiable. The paper does not state how gradients are handled. The standard approach (detaching the argmax, consistent with the cited MoE load balancing loss) should be explicitly stated. This is an incomplete specification rather than a structural flaw, but readers cannot reproduce the method without this clarification.

2. **No statistical variability reported.** The paper states "5 runs for each experiment" (Tables 1–3) but only reports point estimates. TTA methods can have meaningful run-to-run variance under long-tailed streams where sample order matters, and L-TTA's improvements over strong baselines are often modest (1–3%). Without standard deviations or confidence intervals, it is difficult to assess whether the reported gains are statistically reliable.

3. **BEM's class prior estimation has a potential circular dependency.** The class priors π are "continually updated based on the current predicted pseudo-labels" (Sec. 3.2). If the model misclassifies tail-class samples as head classes (a common failure mode), the estimated tail-class prior becomes too low, weakening the BEM penalty where it is most needed. Proposition 2 assumes correct priors and does not account for this feedback loop. The paper should discuss this limitation or provide evidence that it does not arise in practice.

4. **Test-stream ordering not specified.** The paper describes how long-tailed test sets are constructed by subsampling but does not specify the order in which samples arrive during TTA. In continual adaptation, the arrival order can significantly affect outcomes (e.g., all head samples arriving first could induce head bias before tail samples appear). This is a reproducibility concern.

5. **Propositions 1 and 2 use informal language.** "Split C into C_head and C_tail with certain measurements" is vague. The partitioning criterion (top-20% vs. bottom-80%) is defined in the experiments section (line 206) but should be stated alongside the propositions in the main text for clarity.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment directly quantifying modality-bias amplification (e.g., comparing SAR on CLIP vs. on a pure vision backbone under identical long-tailed conditions) would strengthen the central motivation.
- Testing whether a simple combination of an existing TTA method with standard LT techniques (e.g., logit adjustment) closes the gap would sharpen the claim that a co-designed solution is necessary.
- An analysis of BEM's sensitivity to pseudo-label quality under simulated bias scenarios would address the circular-dependency concern directly.

## Removed Points
- "CRA loss is a structural flaw" — The argmax non-differentiability is standard in MoE load balancing losses with well-known solutions (detached assignments). The issue is incomplete specification, not a structural flaw. Downgraded to Minor.
- "EP update mechanism is misleading" — The reviewer's analysis confirms the EMA dynamics implement the intended exclusionary logic. This is a presentation preference, not a substantive weakness.
- "Modality-bias amplification evidence is thin" — The paper provides qualitative evidence and this is a claimed failure mode, not a central experimental result. Moved to Nice-to-Have.
- "HM metric not clearly motivated" — Harmonic mean of accuracy and macro-F1 is a standard combined metric. Presentation nitpick.
- "Props. 1-2 deferred to appendix" — This is normal paper structure; proofs in appendix are standard.
- "Table 7 formatting garbled" — PDF extraction artifact.
- Parallelism concern about single A100 — "Parallel" refers to independent computation, not multi-GPU.
- "Missing combined approaches comparison" — Paper already compares with 11 baselines; this is augmentation, not omission.
- Strengths removed: generic statements about "addressing an important problem" and superficial characterizations without concrete content.

## Novel Insights
None beyond the paper's own contributions. The reviews surface no novel perspective that the paper itself does not already articulate.

## Suggestions
1. Clarify the CRA loss optimization: explicitly state that the argmax assignments are detached during gradient computation (standard MoE practice).
2. Report standard deviations or confidence intervals for the 5-run main results (Tables 1–3).
3. Specify the test-stream ordering protocol for reproducibility.
4. Tighten Propositions 1-2 by specifying the head/tail split criterion in the main text.
5. Add a brief discussion of the potential circular dependency in BEM's prior estimation.

## Score and Decision
Score: 6.5
Decision: Accept

**Calibration anchors used:**

Round 1 (bracketing):
- Low band (<3.5): pdzHpQbGrn (2.50), HfJxXbXlYJ (3.00), ZaudLwn0Hm (2.50), FwkYeLovHk (3.33), gNoqEdT2wO (2.33), WM5G2NWSYC (2.00) — all rejected, generally weak TTA/VLM papers with fundamental flaws.
- Middle band (3.5-7.5): b20VK2GnSs (7.00, concept drift+VLMs, accepted), NW2s5XXwXU (6.00, long-tailed diffusion, accepted), PxL35zAxvT (4.67, TTA auxiliary tasks, rejected), xqxG5WogN6 (5.67, TTA+label shift, rejected), u1yvEwYfK9 (5.67, long-tailed recognition, rejected), 7iuFxx9Ccx (6.00, resource-efficient TTT, rejected).
- High band (>7.5): TPZRq4FALB (8.00, multi-modal TTA reliability, accepted), WyEdX2R4er (8.00, VLM data-type understanding), uAFHCZRmXk (8.00, modality gap analysis) — all accepted but not TTA method papers.

Round 2 (narrowing within 5.5-7.5):
- kIP0duasBb (6.67, TTA with CLIP Reward RLCF, accepted) — Closest anchor. RLCF has weaker novelty (similar to prior work) but applies to 3 tasks and has clearer writing. Our paper has stronger novelty and broader evaluation but more presentation gaps. Slightly weaker than this anchor.
- x5LvBK43wg (6.20, PROGRAM prototype-based TTA, accepted) — Our paper has clearer novelty and more extensive evaluation. Stronger than this anchor.
- TD3SGJfBC7 (6.25, Few-shot TTA for CLIP, accepted) — Our paper has stronger novelty (not incremental like L2C was criticized for). Stronger than this anchor.
- NW2s5XXwXU (6.00, Long-tailed diffusion, accepted) — Different domain (generation vs. classification) but similar long-tail focus. Our evaluation is more extensive.

**Final score positioned at 6.5**, reflecting that the paper has stronger novelty and broader evaluation than the 6.20-6.25 anchors but more presentation clarity gaps than the 6.67 anchor. The weaknesses are all minor (specification gaps, missing variance, discussion gaps) and addressable in a rebuttal, not fatal.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>