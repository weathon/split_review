Here is the consolidated final review.

---

## Summary

This paper proposes a fine-tuning framework for Multi-Source Unsupervised Domain Adaptation (MUDA) that integrates learnable category-specific prompts (shared across domains to capture domain-invariant features) with domain-specific multimodal Low-Rank Adaptation (LoRA) adapters applied to CLIP. The prompts are trained in a first stage, after which LoRA adapters (with a cross-modal shared projection layer) are trained per source domain and combined via an unspecified coefficient-based amalgamation for target inference. Experiments on Office-31, Office-Home, and DomainNet show improvements over prior MUDA methods including the CLIP-based MPA baseline.

## Strengths

- **Novel and well-motivated integration of prompts and multimodal LoRA for MUDA.** The paper makes a principled design choice: shared class-specific prompts avoid the overfitting risk of domain-specific prompts (motivated by Li et al., 2023), while separate multimodal LoRA matrices capture domain-specific features. This two-component architecture is a clean decomposition of domain-invariant vs. domain-specific knowledge. The approach yields consistent improvements over prior MUDA methods on all three benchmarks (Office-31: 85.7%, Office-Home: 77.7% (+2.3% over MPA), DomainNet: 54.8%).

- **Cross-modal interaction mechanism via a shared projection layer.** The multimodal LoRA design bridges visual and textual branches through a shared projection layer (Eqs. 13–17, Fig. 2), allowing gradient propagation between modalities during training. This is a concrete structural innovation over prior approaches that treat modalities independently. The paper reports (qualitatively in Section 4.3) that this configuration outperforms single-modality and independent multimodal LoRA.

- **Evaluation on challenging large-scale benchmarks.** The method is tested on DomainNet (~600k images, 345 categories, 6 domains), demonstrating scalability well beyond the small-scale datasets common in MUDA literature. The paper acknowledges the specific difficulties of this dataset (large category count, extreme shifts like Quickdraw vs. others), which adds credibility to the results.

## Weaknesses

### Fatal
None.

### Major

1. **Ablation analysis presented without any numerical evidence (Section 4.3).** The paper discusses three critical design decisions — (i) manual vs. learnable prompts for pseudo-labeling, (ii) LoRA added to one vs. both modalities with vs. without the shared projection layer, and (iii) which transformer layers to insert LoRA — and states conclusions in every case (e.g., "manual prompts outperformed learnable prompts," "multimodal LoRA with a shared projection layer... yielded the best results," "higher layers... resulted in better performance"). Yet **not a single accuracy number, table, or figure** is provided to support these claims. The hyperparameter analysis (threshold τ_label in {0.4,0.5,0.6,0.7,0.8}; prompt length b in {8,12,16,20}) similarly states only the final choices without showing the corresponding accuracy curves or tables. Because these analyses are central to justifying why the method is designed the way it is, the paper's supporting evidence is incomplete. The reader cannot assess the magnitude of each design choice's effect or whether alternative settings would work equally well.

2. **Domain-adapter integration mechanism is underspecified to the point of irreproducibility (Section 3.2.3 and Abstract).** The paper states it will "combine all source domain-specific LoRA modules into an integrated module using a set of coefficients and adapt this integrated module to learn on the target domain" (Abstract) and "amalgamate the multimodal LoRA matrix modules that were trained across different domains" at inference (Section 3.2.3). However, no detail is given on: (a) how these coefficients are initialized, optimized, or selected; (b) whether they are learned per target domain or fixed; (c) whether "adapt this integrated module to learn on the target domain" involves additional training or is simply a weighted combination at inference. No equation for the integration is provided. This is not a minor implementation detail — it is the core mechanism for how multi-source knowledge is transferred to the target domain. Without it, the method cannot be independently implemented or evaluated.

### Minor

3. **Ambiguous two-stage training procedure (Section 3.2.3).** Step 1 trains prompts using "all data, including data from all source domains and the target domain" — but target data is unlabeled. The paper does not specify whether pseudo-labels are used in Step 1, and if so, what model generates them (zero-shot CLIP? some other initialization?). The pseudo-label loss (Eq. 20) and total loss (Eq. 21) are presented only after both steps are described, making it unclear whether the total loss applies to Step 1, Step 2, or both. This ambiguity undermines confidence that the training procedure is correctly described.

4. **Baseline comparison fairness is not discussed.** The paper compares against DAN, D-CORAL, DCTN, MDDA, MFSAN, and MPA. Only MPA is known to use CLIP; the older methods typically use different backbones (e.g., ResNet). The paper does not state whether these baselines were re-run under the same CLIP backbone or whether numbers are taken from original papers with different architectures. If the latter, the comparison may conflate method quality with backbone choice. This should at minimum be acknowledged.

5. **No variance/confidence reporting.** Results are reported as single accuracy numbers without standard deviations or multiple-seed runs. Office-31 and Office-Home are small enough that random seed variation could affect rankings. Modern VLM fine-tuning papers routinely report at least 3 runs.

6. **Connection between stated challenges and method components is asserted rather than demonstrated (Section 1).** The introduction lists three challenges (overfitting from prompt tuning, cross-domain invariance, cross-modal misalignment) and claims the method addresses all three, but no analysis or ablation is provided to isolate which component addresses which challenge. For example, how exactly does the multimodal LoRA shared projection solve cross-modal misalignment beyond providing additional trainable parameters? The paper would benefit from a mapping between challenges, design choices, and evidence.

7. **DomainNet improvement is not quantified in text.** The paper states the method achieved "an average accuracy of 54.8%, which represents an improvement over previous methods" without saying by how much. While Table 3 presumably contains this information, the text should state the margin.

8. **No limitations discussion.** The paper does not discuss limitations such as sensitivity to the number of source domains, failure cases when classes are not well separable, the assumption that all domains share the same label set, or scenarios where pseudo-labels are unreliable.

### Trivial
- The CLIP review (Section 3.1) is standard and could be condensed, though this does not affect the paper's contribution.
- The paper uses "L" to denote both the layer where LoRA is inserted and the transformer layer index, which causes minor confusion in Section 3.2.2.

## Nice-to-Haves
- An efficiency analysis (training time, parameter counts, memory usage) comparing prompt+LoRA to full fine-tuning and to MPA would strengthen the practical motivation.
- An analysis of pseudo-label quality (accuracy of generated labels, fraction of target samples retained at the chosen threshold) would help readers understand how much unlabeled data is leveraged.
- An ablation over LoRA rank (e.g., r ∈ {1, 2, 4, 8}) to justify the choice of r=2.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The CLIP review is too long; it could be condensed."* — This is a presentation-style preference, not a substantive weakness. The section provides necessary background for the method.
- *"The paper does not report whether these baselines were re-run under the same backbone (CLIP) or taken from existing papers."* — This is partially retained above as a Minor weakness (fair comparison). The removed component is the speculation that "older methods likely use different backbones" without evidence; however, the core concern (unclear whether numbers are comparable) is valid and kept.
- *Criticism about garbled tables in extraction.* — Parser artifact, not an author error. The relevant concern (no variance reported) is retained as a Minor weakness.
- *The Strength Finder's claim that "The ablation study (Section 4.3) shows that multimodal LoRA with the shared projection outperforms..."* — This conflicts with the verified weakness that Section 4.3 provides **no numerical evidence**. The strength about the mechanism being a genuine design contribution is retained, but the inflated evidential claim is dropped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a complete ablation table** to Section 4.3 reporting accuracy numbers for each design choice: prompt type (manual vs. learnable) with resulting pseudo-labeled sample count; LoRA configuration (visual-only, text-only, both independent, both with shared projection); layer insertion point; rank r ∈ {1,2,4,8}; threshold τ_label vs. accuracy; prompt length b vs. accuracy.
2. **Specify the domain-adapter integration mechanism in full.** Provide the equation for combining LoRA updates (e.g., ΔW_combined = Σ_i β_i ΔW_i) and describe how β_i are obtained — are they learned via a separate optimization on target data, or fixed (e.g., uniform)? If learned, describe the loss and procedure. If fixed, state that and show an ablation.
3. **Clarify the two-stage training procedure.** Separate the loss for Step 1 and Step 2 explicitly. State whether pseudo-labels are used in Step 1 and, if so, how they are obtained. If Step 1 uses only source labels, state that clearly.
4. **Report standard deviations** from at least 3 runs with different seeds.
5. **Clarify baseline numbers.** State whether baselines were re-implemented with the same CLIP backbone or taken from prior papers with different backbones, and discuss how this affects comparability.
6. **Add a limitations paragraph** acknowledging the method's assumptions and potential failure modes.

## Score and Decision

This paper proposes a plausible and well-motivated integration of two PEFT techniques (prompt tuning and multimodal LoRA) for the MUDA setting with VLMs, and reports strong results on standard benchmarks. However, the paper has two structural weaknesses that prevent acceptance in its current form: (1) the ablation analysis central to justifying the method's design is presented without any numerical support, and (2) the domain-adapter integration mechanism — the core mechanism for transferring multi-source knowledge to the target — is underspecified to the point of irreproducibility. These are not minor presentation issues; they directly affect the paper's credibility and reproducibility. The training procedure is also ambiguously described. The ideas have genuine potential, but the evidence and specification are insufficient as-is.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>