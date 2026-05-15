Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper proposes NCL-SR, the first Non-Contrastive Learning (NCL) framework for Sequential Recommendation (SR). The method avoids the computational cost of negative samples required by contrastive learning (CL). The core technical novelty is a differential-privacy-inspired data augmentation designed to generate diverse positive samples that preserve user preferences, enabling effective non-contrastive training with alignment and uniformity losses adapted from Matrix Cross Entropy (Zhang et al., 2023). Empirical results on six datasets show consistent improvements (average 11.93% over second-best baselines).

## Strengths

- **First NCL framework for SR, addressing a clear limitation of CL-based methods.** The paper identifies a genuine problem — the computational overhead of negative samples in CL-based SR — and proposes a principled alternative. The consistent improvements across six datasets (Table 1, 11.93% average improvement; Table 2, 12.48% against CL methods) provide strong evidence that NCL can be effective for SR, which was previously unexplored.

- **Interesting new empirical insight on alignment vs. uniformity.** Through ablation (Table 3), the paper discovers that alignment is generally more important than uniformity in data-sparse SR settings (6.10% vs. 4.00% average Recall@10 drop when removing alignment vs. uniformity). This finding counters assumptions that may carry over from dense domains (CV/NLP) and has practical implications for designing SR-specific NCL methods.

- **Practical item-level efficiency design.** The paper explicitly identifies the exponential complexity of user-level DP augmentation (O(k^l)) and designs an item-level variant with linear complexity O(k·l) (Section 4.1, final paragraph). This makes the method feasible for real-world recommendation data.

- **Consistent and substantial empirical gains, especially on sparse data.** The method achieves particularly large gains on the sparsest dataset (Sports: 33.2% improvement in Recall@10), suggesting genuine robustness where CL methods typically struggle.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical guarantee for preference-preserving augmentation is not properly established.** This is the paper's most significant weakness. Theorem 1 is presented as the core guarantee but has several unresolved issues:

  (1) The term **"limited modification"** is never defined (line 72: "if there is only limited modification from x to x'"). Without a formal definition, the theorem's conclusion is not operational.

  (2) The **precondition cannot be met**: Theorem 1 assumes "a recommendation mechanism M satisfies differential privacy with the privacy parameter ϵ." The actual recommender is a standard neural network trained on the data — it does not satisfy ϵ-DP, and the paper never claims it does. This renders the theorem inapplicable to the actual system.

  (3) The paper switches from **user-level to item-level augmentation** (Section 4.1, final paragraph) due to exponential complexity, but does not re-derive the preference-preservation guarantee for the item-level procedure. The post-processing property and expected output stability cited (lines 109-110) are properties of differential privacy (about *privacy*), not about preserving the semantic meaning of user preferences. The gap remains unbridged.

  The paper's abstract and contribution bullets claim the approach is *provably* preference-preserving. As presented, this claim is unsupported.

- **Non-standard evaluation split raises questions about generalizability and fairness.** The 2:2:6 training/validation/test split (20% training) is highly unusual for SR, where standard protocols (leave-one-out, 80/10/10, etc.) are well-established. While the paper justifies this as testing cold-start/sparse regimes and cites related work (Wu et al., 2024; Qian et al., 2020; Wang et al., 2022a; Lin et al., 2025), the split introduces confounds:

  — Baselines may perform poorly simply because they require more training data, not because NCL-SR is genuinely superior.
  — The paper does not report whether baselines were re-tuned for this split.
  — No results under standard splits are provided, making it difficult to assess the method's general applicability.

  The paper claims to test "cold-start users" (line 159) but never separately analyzes cold-start vs. warm users, leaving this motivation unverified.

- **Missing efficiency measurements.** The paper motivates NCL by computational efficiency (lines 11-13: "CL-based methods inevitably suffer from high computational costs, because they heavily rely on negative samples"). Yet it provides zero runtime, memory, or throughput comparisons against CL baselines. This is a critical omission that leaves the primary motivation unsupported by evidence.

### Minor

- **Baseline fairness concerns.** Several CL baselines (CLS4Rec, CoSeRec, EC4Rec, SCL) were originally designed for ID-based recommenders and modified to text-based settings. Their augmentation strategies (random crop, swap, mask) were designed for categorical item IDs, not text embeddings. The paper does not clarify whether these baselines were re-tuned for the text-based setting, which may disadvantage them.

- **Ablation control for DP augmentation is weak.** When removing the DP augmentation (line 191, "Ours w/o DP Aug."), the paper replaces it with augmentations "randomly sampled from the CL-based baselines." A more informative control would compare against a structured, preference-aware non-DP augmentation (e.g., CoSeRec's correlation-based substitution) within the same NCL framework, to isolate the benefit of the DP mechanism.

- **Minor presentation issues.** (1) Notation inconsistency: the synonym set is introduced as S(x_i) in the text but defined as N_k(x_i) in Equation 4 (line 83-86). (2) Typo in the sampling probability formula (line 94): "u(t,t')" uses t instead of x.

- **Sensitivity analysis shows configuration-dependence.** Figure 2 shows that optimal λ₁ and λ₂ vary across datasets, weakening the paper's general claim about the relative importance of alignment vs. uniformity.

### Trivial
None.

## Nice-to-Haves

- Results under a standard SR split (e.g., leave-one-out or 80/10/10) to complement the sparse-data evaluation.
- Runtime/memory/throughput comparisons against CL baselines to validate the efficiency motivation.
- Separate analysis of cold-start vs. warm users, since the split is justified for this purpose.
- A case study or quantitative analysis showing that augmented profiles yield similar top-1 predictions as original profiles, to empirically validate preference preservation.

## Removed Points

- **Criticism about the paper "not reporting whether baselines were re-tuned":** Partially retained — the criticism is valid but softened to "not clarified" since the paper states baselines were "modified into the text-based setting for a fair comparison" (line 164) without explicit mention of re-tuning.
- **Criticism about incomplete citation "(Wang et al.":** Removed. This is almost certainly a parser artifact (reference section stripped); the original submission contains the full citation.
- **Claim that NCL losses are "taken verbatim from prior work" making novelty marginal:** The paper clearly attributes the losses to Zhang et al. (2023), which is standard practice. The novelty lies in the framework and the augmentation, not in inventing new loss functions. This criticism overstates the problem.
- **Claim about missing related work on prior NCL for recommendation:** Cannot verify without external sources; removed per instructions.
- **Generic formatting/style nitpicks:** Removed.

## Novel Insights

The most interesting observation not explicitly made by the paper but emerging from the cross-reviews is this: the paper simultaneously claims *provable* preference preservation (which requires a formal guarantee) and demonstrates the *practical necessity* of the item-level approximation (which abandons the formal guarantee). This tension is actually productive — it suggests that the community might benefit from a separate line of work on *empirically validated* preference-preserving augmentations for SR, rather than attempting to retrofit strong DP guarantees that are misaligned with the actual model architecture (a non-DP neural network). The paper's strong results on sparse data, combined with the collapse of its theoretical scaffolding, implicitly argue that preference preservation can be achieved *without* formal DP guarantees — an observation worth testing directly.

## Suggestions

1. **Fix the theoretical argument.** Either (a) correct Theorem 1 by defining "limited modification," dropping the unrealistic ϵ-DP precondition on M, and proving the guarantee for the item-level implementation, or (b) abandon the formal guarantee framing and present the augmentation as heuristic (DP-inspired) with strong empirical validation. Option (b) is likely more honest and would still constitute a contribution.
2. **Add results under a standard SR split** (e.g., leave-one-out) to demonstrate general applicability beyond the sparse-data regime.
3. **Add runtime and/or memory comparisons** against CL baselines to substantiate the efficiency motivation.
4. **Re-run or clarify baseline tuning** for the text-based setting and the 2:2:6 split. Report whether grid search or default hyperparameters were used.
5. **Improve the DP augmentation ablation:** compare against a structured non-DP augmentation (e.g., correlation-based substitution from CoSeRec) as a control, rather than random augmentations.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>