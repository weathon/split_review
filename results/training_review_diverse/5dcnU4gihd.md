Now I have thoroughly verified all claims. Here is my final consolidated review.

---

## Summary

This paper proposes "Attention Head Purification" for domain generalization with CLIP, built on the observation that not all attention heads in CLIP's image encoder are equally generalizable. The method decouples two levels of purification: (1) **task-level purification** via head-aware LoRA (HA-LoRA), which gives each attention head its own independent LoRA parameters to avoid cross-head interference during task adaptation; and (2) **domain-level purification** via learnable gating with MMD regularization (DIG), which emphasizes domain-invariant heads and suppresses domain-sensitive ones. The two components are decoupled by not backpropagating the MMD loss into HA-LoRA. The method achieves strong results on five DG benchmarks and is shown to be complementary to prompt-learning methods.

## Strengths

1. **Novel and well-motivated perspective.** The paper identifies that different attention heads in CLIP encode different properties, and that some heads encode domain-specific or background-focused information that harms generalization. Figure 1 provides supporting evidence, and the purification framing (task-level vs. domain-level) is intuitive and clearly communicated. This goes beyond the standard "avoid knowledge forgetting" paradigm of prior CLIP-based DG work.

2. **Head-aware LoRA is convincingly justified.** The analysis in Eq. 4–5 shows that conventional LoRA shares the B matrix across heads, creating interference during head-specific adaptation. Table 1 (Right) shows that HA-LoRA and conventional LoRA perform nearly identically without DIG (+0.1–0.2%), but HA-LoRA yields a meaningful +1.0–1.4% gain when DIG is added. This directly supports the interference-elimination story.

3. **Ablation studies cleanly validate each design choice.** Table tab-mmd shows that using MMD to update HA-LoRA (alone or jointly with DIG) degrades performance, while using MMD only for the gates yields the best result (87.0% on OH). Table tab-strate (Left) shows that joint training outperforms alternative or two-stage pipelines. These ablations make the method's architecture credible.

4. **Orthogonal and consistent improvement over prompt-learning methods.** Table 3 demonstrates that attention head purification provides consistent gains of 2.1–5.5% when combined with six different prompt-learning methods (CoOp, CoCoOp, DPL, DUPRG, STYLIP, PromptStyler). This is strong evidence that the contribution is complementary and robust.

5. **Training efficiency.** The method trains in 1h 30min on DomainNet, substantially faster than MIRO (5h 24min) and CLIPood (4h 46min), while achieving competitive or better accuracy.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Comparison table mixes cited and reproduced numbers without full consistency.** Table 4 (main comparison) cites original reported numbers for some methods and reproduces numbers for others (marked with \textsuperscript{\dag}). While the paper is transparent about which is which, the lack of a single unified evaluation protocol means some baselines are evaluated under different conditions (e.g., data splits, backbone details, optimization settings). This makes it harder to precisely isolate the method's improvement. The concern is partially mitigated because: (a) the paper's headline result (79.0% with PromptStyler+purification) exceeds even the *cited* CLIPood number (78.6%), so the comparison is not misleading even under the most favorable baseline interpretation; and (b) the ablation tables and combine table provide controlled internal comparisons. Nonetheless, the paper would be stronger with a fully controlled reproduction of all baselines.

2. **Figure 1 motivation experiment does not isolate head dropping from adaptation.** The "adapt & drop" curve in Figure 1 jointly applies LoRA adaptation and head dropping, so the jump from ~82% (zero-shot) to ~86% conflates both interventions. The "drop by cross-validation" curve (which uses frozen CLIP) is cleaner but is not the one showing the largest gains. The paper frames this as a motivation observation (not a main result), and the actual ablations in Table 1 properly isolate the contributions. Still, a controlled experiment that drops heads without adaptation would strengthen the motivating claim that head selection itself, not just adaptation, drives improvement.

3. **Standard deviations are not reported.** The paper states results are averaged over three runs (Section 4.2) but no standard deviations appear in any table. Given that DG benchmarks have non-negligible variance, reporting variance estimates would improve reproducibility assessment.

4. **MMD kernel bandwidth is unspecified.** The paper uses a Gaussian kernel for MMD (Eq. 5) but does not report the bandwidth parameter, which can affect the MMD loss. The authors should either fix this value across all experiments or show robustness to its choice.

5. **The "Ours" entry in Table 4 requires cross-referencing to understand what it includes.** The caption states that "Ours" uses attention head purification combined with prompt learning, but the reader must cross-reference Table 3 to identify PromptStyler as the specific prompt method used. An explicit statement (e.g., "Ours = HA-LoRA + DIG + PromptStyler prompts") would improve clarity.

### Trivial

1. **Design choice of r=8 for last two layers and r=2 for others is not ablated.** This is a reasonable design (more capacity in deeper layers), but an ablation showing its near-optimality would strengthen the paper.

## Nice-to-Haves

- A controlled experiment isolating head dropping from adaptation (e.g., dropping heads on the frozen zero-shot model) to sharpen the motivational claim in Figure 1.
- An ablation doubling the rank of conventional LoRA to match HA-LoRA's parameter count, to verify that the improvement comes from interference elimination rather than extra capacity.
- A quantitative correlation analysis between the cross-validation importance scores (used in Figure 1) and the learned DIG gate weights.

## Removed Points

- **Criticism about "confusing" marking of CLIPood numbers in Table 4.** The paper clearly states that \textsuperscript{\dag} marks reproduced numbers and "Others are cited from the original paper." The double-listing of CLIPood (first row cited, second row reproduced) is transparent, not confusing. The reviewer's confusion reflects a misreading, not an error in the paper.
- **Criticism that the comparison table is "structurally flawed" and "makes it impossible to assess whether the reported improvements are genuine."** This is an overstatement. The paper's own numbers at 79.0% exceed CLIPood's cited 78.6%, so the improvement is genuine even under the most favorable reading of the baselines. The double-listing of CLIPood (cited 87.0 vs. reproduced 85.3) is a mark of transparency, not opacity.
- **Criticism about MMD loss implementation clarity ("whether multiple MMD terms are summed or only the final [CLS] token feature").** The paper states "impose the MMD loss on each layer" (Section 4.2), which is reasonably clear.
- **Generic strengths from Strength Finder that are superficial or unspecific:** None were identified after filtering — all listed strengths are backed by specific evidence.

## Novel Insights

The decoupling insight — that task-level adaptation (LoRA) and domain-level invariance (gating + MMD) should be treated as separate optimization problems with separate parameter sets and distinct gradient flows — is the paper's most novel contribution beyond the specific technique. The ablation showing that applying MMD to HA-LoRA *hurts* performance (Table tab-mmd, lines: 85.8% vs. 87.0%) is a useful negative result: it suggests that forcing domain-invariance constraints onto the feature extraction parameters themselves is counterproductive, and that a gating/selection mechanism operating on top of adapted features is a more effective architecture. This has implications beyond the specific CLIP/DG setting.

## Suggestions

- **For the camera-ready version:** Either reproduce all baselines under identical conditions (same data splits, CLIP backbone version, optimization details) in a single unified table, or clarify in the caption exactly which conditions differ and why. At minimum, report the three-run standard deviations for all results.
- **Clarify the MMD kernel bandwidth** and whether it was tuned or fixed across datasets.
- **Explicitly state** in the Table 4 caption that "Ours" uses PromptStyler prompts, to remove the need for cross-referencing.
- **Add a small controlled experiment** in the supplement that drops heads (by the cross-validation ranking) on top of the frozen zero-shot model, to decouple head selection from adaptation in the motivation.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>