Now I have all the information I need. Let me compose the consolidated review.

## Summary

This paper introduces C-CLIP, a method for multimodal continual learning of vision-language models that combines LoRA-based parameter-efficient fine-tuning with a novel contrastive knowledge consolidation (CKC) loss. The paper also establishes a Vision-Language Continual Learning (VLCL) benchmark spanning three evaluation tracks (downstream retrieval, zero-shot retrieval, and zero-shot classification forgetting). The core technical claim is that CKC, by performing contrastive learning between old and new feature projections rather than simply aligning them, simultaneously reduces forgetting and improves new-task learning — overcoming the typical stability-plasticity trade-off. The strongest evidence is Tables 3 and 4: C-CLIP achieves the highest average I2T R@1 (70.62) across eight datasets while losing less than 1.3% ImageNet zero-shot accuracy (66.42% vs. 67.73% original CLIP).

## Strengths

- **Novel VLCL benchmark with three-track evaluation**: The paper establishes a multimodal continual learning benchmark that goes beyond prior single-modal or single-metric evaluations. It jointly assesses downstream image-text retrieval, retrieval on unseen domains, and zero-shot classification forgetting (Section 3, Table 2). This fills a genuine gap: prior works like ZSCL and Mod-X do not evaluate forgetting of CLIP's original zero-shot performance.

- **C-CLIP achieves both strong downstream performance and near-zero zero-shot forgetting**: The method outperforms full fine-tuning on several downstream datasets (I2T R@1 on Flickr30K and COCO in Table 3) while maintaining 66.42% ImageNet zero-shot accuracy after all eight tasks, compared to ~25% for full fine-tuning and ~60% for best prior methods (Table 4, Figure 1). This directly supports the paper's central claim of "learning more and forgetting less."

- **Contrastive knowledge consolidation resolves the stability-plasticity trade-off**: Unlike prior regularization methods (EWC, ZSCL) whose losses conflict with the CLIP loss, CKC aligns the loss trends (Figure 3(c)–(d)) and improves performance on both new and old tasks as training progresses (Figure 5). Ablation results (Table 5) show adding CKC on top of LoRA dramatically boosts average I2T R@1 from 50.40 to 70.62, confirming its unique effectiveness.

- **Thorough evaluation across architectures and against prompt-based methods**: C-CLIP performs consistently on ViT-B/32, ViT-L/14, and ViT-L/14@336 (Table 7). The comparison with L2P and CPE-CLIP (Table 8) shows prompt-tuning forgets downstream tasks, while C-CLIP with LoRA+CKC retains both zero-shot and downstream performance.

## Weaknesses

### Major

- **Quantitative zero-shot retrieval results on HAVG are reported only qualitatively, not in a dedicated comparison table.** The paper defines a three-track benchmark (Section 3, Table 2) including "Zero-shot retrieval" on the held-out HAVG dataset, with I2T R@1 as the specified metric. However, the main results tables (Tables 3 and 4) cover only the other two tracks. Figure 5 is described as showing trends on unseen datasets, including HAVG, but the accompanying text provides only qualitative observations ("training improves performance," "previous methods are unstable," "our method exhibits impressive performance") without a dedicated table reporting final numeric results with baseline comparisons. This is a significant evaluation gap: one of the three defined benchmark axes lacks the quantitative treatment the other two receive. While the paper's primary contribution (the C-CLIP method) is not invalidated, the benchmark loses some of its claimed comprehensiveness.

### Minor

- **Task order is not explicitly stated, and no ordering robustness analysis is provided.** The paper uses eight datasets but never states which order they are trained in, beyond scattered clues (e.g., "after fine-tuning twice on Flickr30K and COCO" suggests these are first two tasks; "AI-generated datasets like Lexica in Task 4" places it fourth). Given that CL methods are known to be sensitive to task order, and the paper itself notes that fine-tuning on AI-generated datasets "causes the model to forget its performance in real-world domains," the absence of a clear task ordering or any ordering-robustness experiment (e.g., one alternative random order) is a gap that limits the generality claims. This is not fatal — many CL papers use a single fixed order — but the paper's claim that C-CLIP uniquely achieves both stability and plasticity would benefit from showing this is not order-dependent.

- **Zero-shot classification prompting protocol is underspecified.** The paper reports zero-shot accuracy on ImageNet, CIFAR-100, etc., but never states which text prompts are used. CLIP's zero-shot accuracy is known to vary by several points depending on prompt engineering. The paper uses "pre-trained CLIP" as a reference point (67.73% on ImageNet-1K) but does not clarify whether the same prompts are used during and after continual fine-tuning. This is easily fixable but impacts reproducibility.

- **Ablation study (Table 5) covers only Tasks 0 and 1, not the full 8-task sequence.** The paper presents the ablation of LoRA and CKC on the first two tasks as demonstrating the method's effectiveness. However, the interaction between LoRA and CKC may change as more tasks accumulate — LoRA integration and CKC's use of old model features both evolve over the full sequence. A full ablation across all 8 tasks (or at least 4–5) would substantially strengthen the claim that the benefits persist.

### Trivial

- **The "for the first time" claim (Section 1, contributions) is overstated.** The paper states "achieving the goal of learning more and forgetting less for the first time." Several recent CL methods (e.g., DER, BiC, Mod-X with rebalancing) also claim to improve new-task performance while preserving old knowledge. The authors should qualify this to their specific setting (multimodal VLMs with rehearsal-free constraint) or simply remove the phrase.

- **The theoretical proof in Appendix A.1 (Lipschitz continuity of a feedforward network) is standard** and does not provide specific insight into why LoRA's particular parameterization is effective for CL. It shows that network outputs are Lipschitz in parameters, which is true for any bounded-weight network, but does not compare LoRA to regularization-based methods or explain LoRA's advantage. This could be shortened to a citation without loss.

- **Two datasets (Simpsons, Kream) lack formal citations** in the main paper or appendix, making it harder to verify their provenance. The paper should cite these or note their sources.

## Nice-to-Haves

- Include a quantitative table reporting I2T R@1 on HAVG with full baseline comparisons.
- Provide t-SNE visualizations of the feature space before and after CKC, comparing old model projections with new model projections, to directly support the claim that CKC "keeps the new and old feature spaces connected but not identical."
- Ablate the CKC temperature and batch size sensitivity, as these can affect the consolidation vs. plasticity trade-off.
- Add a replay-based upper bound (e.g., storing 100 samples per task) to calibrate how much performance is lost under the rehearsal-free constraint.
- The concatenation of visual and text features in Eq. (5) (creating a 1024-dim vector) is a design choice that could be ablated against separate projectors for vision and text features.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **The critic's claim that the zero-shot retrieval results are "never quantitatively reported" is partially softened**: Figure 5 is described as showing these results with trends, but the paper lacks a dedicated comparison table. The underlying concern (missing quantitative table) is real and kept in Major; the claim that there are "no numeric results at all" is slightly overstated since Figure 5 presumably contains values, but without access to the figure, the strength of the criticism is appropriate. Kept in Major as stated.

- **The critic's point about the paper needing a "fairer comparison with replay-based methods"**: Removed. The paper scopes itself as rehearsal-free, and the harsh critic acknowledges this is a valid choice. Demanding a replay upper bound is a nice-to-have, not a weakness.

- **The critic's request for separate ablation of CKC's batch size and temperature**: Moved to Nice-to-Haves. This is a standard sensitivity analysis but does not threaten any core claim.

- **The critic's request for ablating the concatenation design (Eq. 5) vs. separate projectors**: Moved to Nice-to-Haves. Interesting design question but not central to the paper's validity.

## Novel Insights

The reviews surface an important tension not fully addressed in the paper: C-CLIP's CKC loss treats the old model's projected features as positives in a contrastive formulation. This is clever because it naturally scales the number of negative pairs (all other samples in the batch), unlike standard knowledge distillation that operates on individual sample alignment. The reviewer correctly notes this contrastive formulation inherits sensitivity to temperature and batch size — but this is actually a strength of the design, as it allows the consolidation strength to be modulated via a single scalar, unlike regularization-based methods that require per-layer coefficients. The paper could lean into this point more explicitly as a practical advantage.

## Suggestions

1. Add a dedicated table reporting I2T R@1 on the HAVG dataset for the zero-shot retrieval track, with all baseline methods compared.
2. State the task order explicitly and include at least one alternative random order (reporting mean/std).
3. Clarify which zero-shot classification prompts are used during and after continual fine-tuning.
4. Extend the ablation of LoRA+CKC to cover at least 4–5 tasks (or all 8).
5. Tone down or qualify the "for the first time" claim in Section 1.
6. Provide citations for the Simpsons and Kream datasets.
7. Consider shortening Appendix A.1 to a citation and adding a more targeted theoretical comment about why LoRA's rank-constrained parameterization is well-suited to the CL constraint in Eq. (4).

## Score and Decision

**Overall assessment**: The paper makes a solid contribution to an underexplored area (continual learning for multimodal VLMs). The C-CLIP method is technically sound, well-motivated, and shows clear and consistent improvements over rehearsal-free baselines on the two fully reported tracks. The main evaluation gap (missing quantitative zero-shot retrieval table) is significant given the paper's benchmark framing but does not invalidate the method — the paper's core claims about downstream performance and zero-shot classification preservation are well-supported. The other issues (task order, prompt specification, limited ablation) are fixable in revision. This is a clear accept at the borderline-to-solid range: the work is original, the experiments are mostly thorough, and the method is effective.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>