Now I have all the information needed. Here is the consolidated review:

---

## Summary

This paper tackles continual learning for vision-language models (CLIP), establishing a multimodal benchmark (VLCL) spanning 8 diverse image-caption datasets with three evaluation tracks (downstream retrieval, zero-shot retrieval, zero-shot classification). The authors propose C-CLIP, which combines Low-Rank Adaptation (LoRA) to mitigate forgetting with a novel Contrastive Knowledge Consolidation (CKC) loss that aligns new-task learning with CLIP's contrastive objective, rather than fighting it. Experiments show C-CLIP achieves strong downstream retrieval performance while preserving zero-shot generalization, substantially outperforming existing continual learning methods.

## Strengths

- **First comprehensive VLCL benchmark with three evaluation tracks.** The paper establishes a principled evaluation protocol for continual learning of vision-language models, covering downstream retrieval on 8 domain-diverse datasets, zero-shot retrieval on unseen domains, and zero-shot classification on 6 datasets (Tables 1-2). This is more complete than prior settings like Mod-X (fixed-distribution) or MTIL (classification-only), and will be useful to the community.

- **C-CLIP achieves strong downstream performance with little zero-shot forgetting.** On trained datasets, C-CLIP obtains average I2T R@1 of 76.49, surpassing sequential full fine-tuning (73.84) and all other CL methods (next best: 70.65), while maintaining ImageNet-1K zero-shot accuracy at 67.8% after 8 tasks compared to 26.7% for sequential fine-tuning (Tables 3-4). This combination of strong new-task learning and preserved generalization is the paper's central empirical contribution.

- **CKC loss is conceptually well-motivated and empirically effective.** Unlike prior regularization methods (EWC, LwF, Mod-X) whose losses conflict with CLIP's contrastive objective (Figure 3c-d), CKC performs contrastive learning between old and new projected features, aligning with CLIP's optimization direction. Table 5 shows CKC+LoRA (76.49 I2T R@1) dramatically outperforms LoRA alone (64.28) and LoRA+LwF/Mod-X (61.43/62.60), demonstrating the approach works as intended.

- **Systematic ablation and generalization verification.** The paper disentangles LoRA and CKC contributions (Table 5), examines LoRA rank sensitivity (Table 6), verifies across ViT-B/32, ViT-L/14, ViT-L/14@336 backbones (Table 7), and compares against prompt-tuning methods L2P and CPE-CLIP (Table 8), showing robustness.

## Weaknesses

### Fatal
None.

### Major

1. **Missing isolated single-task fine-tuning upper bounds.** The paper frames "outperforms full fine-tuning" as a headline result (abstract, Figure 1, conclusion). However, the reported "full fine-tuning" baseline is sequential fine-tuning on all 8 tasks — a standard lower bound in CL because it suffers catastrophic forgetting. The paper never reports what performance a model fine-tuned on *each dataset individually* (with no continual learning constraints) would achieve. Without this upper bound, the reader cannot tell whether C-CLIP genuinely enhances new-task learning relative to the non-continual optimum, or whether it merely recovers some of the loss incurred by sequential fine-tuning. If C-CLIP approaches or matches isolated fine-tuning, that is still highly impressive — but the paper should state this clearly rather than claiming to "exceed" fine-tuning. This is the single most impactful issue to address.

2. **The merge coefficient α=0.5 is used throughout with no ablation or justification.** After each task, the learned LoRA weights are merged into the backbone with α=0.5 (Eq. 2). The paper states "we simply use α = 0.5 for all experiments" (line 139), with no sensitivity analysis across different values or task orders. Since α directly controls the trade-off between retaining old knowledge and incorporating new information, this is a significant methodological gap. An ablation varying α from 0 to 1 on at least one task sequence would clarify whether 0.5 is near-optimal or simply a reasonable default.

### Minor

1. **No analysis of feature drift or error accumulation from repeated LoRA merges.** At each stage, the "old model" used by CKC has undergone multiple merge operations (each with α<1, introducing approximation). The paper does not examine whether the old model's features drift across stages or whether CKC's effectiveness degrades with task count. While the empirical results across 8 tasks suggest this is not catastrophic, some analysis would strengthen confidence for longer task sequences.

2. **The theoretical justification (Section 4.1) is not specific to LoRA.** The Lipschitz analysis shows that constraining weight changes bounds feature drift — but any method that keeps parameter changes small (early stopping, weight decay, low learning rates) would satisfy the same reasoning. The analysis does not establish that LoRA's low-rank structure provides a unique advantage. This does not detract from the method's empirical success, but the theoretical framing oversells the connection.

3. **Projector architecture h_ψ is unspecified.** The projector is a core component of CKC, yet its architecture (number of layers, hidden dimensions, activation) is not described. Its capacity controls how much the new model can diverge from old features. This information should be provided.

4. **Zero-shot retrieval results are presented only in a figure (Figure 5) without a dedicated table of numerical values.** Given that zero-shot retrieval is one of the three evaluation tracks, a table with key numbers (at least final performance) should be included alongside Figure 5.

5. **Task order is fixed across all experiments with no analysis of order sensitivity.** Continual learning results can be sensitive to task ordering (e.g., training on AI-generated data before vs. after real data). The paper does not discuss why the chosen order is representative or include any sensitivity analysis.

### Trivial
- The phrase "for the first time" (line 26) is mild hyperbole and could be removed.

## Nice-to-Haves
- A summary table of all 8 datasets with statistics (number of training/test samples, domain descriptions) would improve readability — currently this information is spread across the text.
- A comparison against a simple rehearsal-based baseline (e.g., storing a small number of samples per task) would broaden the empirical context, though the paper's rehearsal-free focus is a defensible scope choice.

## Removed Points

- **Criticism that the Mod-X comparison is unfair because Mod-X was designed for a different setting.** The paper explicitly acknowledges this on line 45: "each task shares the same data distribution, which differs from our goal of adapting CLIP to diverse domains." The reviewer's concern is already addressed by the authors.

- **"The paper should compare against more baselines from a broader literature."** The paper already compares against EWC, LwF, ZSCL, Mod-X, DKR, MOE-CL, L2P, and CPE-CLIP — a comprehensive set for the setting. This is scope creep.

- **Criticism that the Lipschitz theory should show LoRA is uniquely capable.** The paper's claim is that LoRA *naturally satisfies* the constraint, not that it is uniquely capable. The empirical comparison differentiates LoRA from alternatives. This is downgraded to Minor above.

## Novel Insights

The reviews independently converge on the same main issue: the "outperforms full fine-tuning" claim needs the isolated single-task upper bound to be properly contextualized. Beyond the paper's own contributions, the reviews surface a more general problem: in continual learning for foundation models, authors often compare against sequential fine-tuning (a weak baseline) without establishing the non-continual optimum, creating an inflated sense of improvement. For this paper, the core method (LoRA + CKC) is clearly effective — the missing baseline would strengthen, not weaken, the paper by showing precisely how close C-CLIP gets to the unconstrained ideal.

## Suggestions

1. **Provide isolated single-task fine-tuning upper bounds.** Train a separate model on each of the 8 datasets independently (no continual constraints) and report per-task performance. Compare C-CLIP's per-task results after the full sequence to these upper bounds. This directly addresses whether C-CLIP sacrifices plasticity — the results will likely still be impressive, and the claim becomes precise rather than overstated.

2. **Ablate α on at least one task sequence.** Vary α from 0 to 1 and report (a) performance on the current task, (b) performance on an earlier task, and (c) ImageNet zero-shot accuracy. This would show whether 0.5 is near-optimal and give practitioners guidance.

3. **Specify the projector architecture** (h_ψ) — number of layers, hidden dimensions, activation, and how it is trained across tasks.

4. **Include key numerical values** from the zero-shot retrieval track (Figure 5) in a table or caption.

5. **Include the isolated fine-tuning upper bound in the abstract/conclusion framing** rather than the current "outperforms full fine-tuning" phrasing.

## Score and Decision

This paper addresses a timely and underexplored problem, contributes a useful benchmark, and proposes a well-motivated method with strong empirical results. The two main weaknesses — the missing single-task upper bound and the unablated α — are consequential but do not invalidate the core contribution. Both are addressable in a revision. The paper demonstrates genuine technical contribution and clear value to the community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>