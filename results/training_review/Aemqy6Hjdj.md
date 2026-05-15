Now I have all the information I need. Let me compose the consolidated review.

## Summary

This paper tackles compositional generalization (CG) — generalizing to unseen domain-class combinations — and makes two main contributions: (1) CG-Bench, a benchmark suite derived from four real-world image datasets that isolates the CG challenge, and (2) Compositional Feature Alignment (CFA), a two-stage fine-tuning method that learns two orthogonal linear heads (class and domain) via linear probing (Stage 1), then fine-tunes the encoder with those heads frozen (Stage 2). Experiments on CLIP and DINOv2 show consistent OOD accuracy improvements over standard fine-tuning, LP-FT, and reweighting baselines.

## Strengths

- **Consistent OOD improvement across multiple models, datasets, and metrics**: Table 1 shows CFA (often combined with WiSE-FT) achieves the highest OOD accuracy on 4 of 5 dataset×metric combinations for CLIP (OfficeHome OOD: 56.9% vs 53.1% best baseline; DomainNet OOD: 9.2% vs 8.7%; iWildCam OOD F1: 32.5 vs 30.0) and on all combinations for DINOv2 (e.g., iWildCam OOD Acc: 23.8% vs 19.6% best baseline). These gains hold across two fundamentally different foundation models (vision-language CLIP and self-supervised DINOv2), demonstrating the method is not model-specific.

- **Feature visualization directly confirms the claimed compositional structure**: Figure 3 visualizes CLIP features on DomainNet (2 domains, 3 classes). Before CFA the features show no clear separation; after CFA, features for each domain–class combination cleanly separate into a grid with class variation along one direction and domain variation along the orthogonal direction. This provides direct empirical evidence for the compositional feature structure defined in Definition 1.

- **A principled new benchmark for an understudied problem**: CG-Bench is built from four real-world datasets (OfficeHome, DomainNet, iWildCam, FMoW) with a masking procedure that isolates the CG challenge. The benchmark reveals that standard fine-tuning methods struggle on OOD domain–class combinations, providing a standardized evaluation platform for future work.

- **Practical robustness to partial domain labels**: Table 2 shows CFA retains most of its OOD benefit even with only 10% of domain labels (53.4% OOD vs 54.3% with 100%) or with zero-shot predicted domain labels (52.0% OOD), supporting real-world applicability where domain annotations may be scarce.

## Weaknesses

### Fatal
None.

### Major

- **Discrepancy between theoretical analysis and implementation**: The method description (Section 2.2, Eq. 4) and the theoretical guarantee (Theorem 1, Eq. 6) both assume both class and domain losses are active during Stage 2 (λ > 0). However, the implementation (Section 3.2) states "we deploy λ = 0 in Stage-2 to reduce compute cost," removing the domain loss entirely. This means Theorem 1 — which proves that optimal features decompose as W₁ᵀa_y + W₂ᵀb_e under the dual-loss objective — does not directly apply to the evaluated method. The paper acknowledges this choice but does not reconcile why the theory is presented as justification for the exact procedure. While the empirical results stand independently and an ablation on λ is referenced in the appendix, the theoretical support as presented is mismatched with the actual implementation, weakening one of the paper's key claimed contributions. The authors should clarify what guarantee holds at λ=0 and whether the domain head serves any active role during Stage 2 fine-tuning beyond the initialization it provides from Stage 1.

### Minor

- **Improvements are modest on several datasets and absent on one**: On DomainNet-CLIP without WiSE-FT, CFA's OOD accuracy (7.3) is actually slightly below full fine-tuning (7.5). On FMoW, CFA's OOD accuracy (41.6) ties or barely trails Reweight-E (41.8). On DINOv2, improvements on OfficeHome and DomainNet are within 1–2 percentage points. While the overall pattern favors CFA, the gains are not uniformly large, and the paper's framing ("outperforms common finetuning techniques") would benefit from more measured language that acknowledges these edge cases.

- **No comparison to domain-adversarial methods**: The paper explicitly notes (line 31) that the two-head architecture "has been widely used in domain adversarial neural networks" but does not include DANN or gradient-reversal methods as baselines. While DANN pursues domain-invariant features (a different goal from CFA's compositional structure), a comparison would help establish whether CFA's specific design choices (frozen orthogonal heads) offer advantages over the standard adversarial two-head framework in the compositional generalization setting. This omission limits the reader's ability to assess the relative value of CFA's design.

- **OOD combination selection is heuristic**: The benchmark curation selects the lowest 20% of zero-shot CLIP accuracies as OOD combinations. This conflates "hard for zero-shot CLIP" with "compositionally novel" and may introduce confounds related to inherent class difficulty rather than compositionality per se. A random masking strategy or one that controls for per-class difficulty would provide a cleaner test of compositional generalization.

### Trivial
None.

## Nice-to-Haves
- An analysis of why λ=0 still works: the paper could explain that even without an active domain loss, features are pulled toward the frozen class head W₁, and since W₁ and W₂ were trained to be orthogonal in Stage 1, the resulting features naturally live in the W₁ subspace — but the domain-dependent component (in the W₂ subspace) that Theorem 1 predicts may be partially lost. An analysis of what feature structure the λ=0 optimum actually produces would clarify the method's true mechanism.
- A direct comparison with a variant that uses only a single orthogonalized class head (no domain head at all) in Stage 1, to isolate whether the domain head contributes beyond providing orthogonal initialization.

## Removed Points
These points are flagged to be removed, treat them with caution:

- *Critic's claim that Stage 2 implementation "contradicts the described algorithm" to the point of invalidating the paper's central claim* — This is softened because the paper acknowledges the λ=0 choice explicitly, cites the ablation on λ in the appendix (which the parser strips but exists in the original submission), and the method still uses the two-head frozen-head mechanism from Stage 1 even without an active domain loss in Stage 2. The gap is real but not a contradiction that invalidates the empirical contribution.

- *Critic's claim that "the mechanism claimed for CFA—alignment of features with both class and domain subspaces—cannot operate if the domain head is not active in the loss"* — This is factually incorrect in its strong form: even without an active domain loss gradient, the frozen domain head W₂, which was learned orthogonal to W₁, constrains the feature space because features are being pulled toward W₁ directions (which are orthogonal to W₂). The domain head's influence is indirect but present through the orthogonality constraint learned in Stage 1.

- *Critic's claim that Section 3.4 "undercuts the stated motivation for the two-head design"* — The paper explicitly explains why domain labels are easy to predict (few domains, visually distinctive features) and supports this with an ablation (Table 3) showing 82-86% domain prediction accuracy even with few labels. This is a thoughtful discussion, not an undercutting.

- *Strength Finder's claim about "Theoretical guarantee for compositional feature alignment" as a core strength* — This is retained but weakened by the λ=0 discrepancy discussed above. The theory is presented as justification for the general framework, even if the exact implementation differs.

## Novel Insights
The reviews collectively surface a subtle but important observation: the gap between the method's theoretical framing (dual-loss optimization) and its practical instantiation (λ=0) invites deeper scrutiny of what CFA is actually doing. The most interesting scientific question — whether the domain head actively shapes features during fine-tuning or merely provides a beneficial orthogonal initialization in Stage 1 — remains unanswered. If the latter is true, the two-stage CFA reduces to a sophisticated initialization scheme for the class head, and the domain head could be replaced by any mechanism that enforces orthogonality. The paper's own evidence (robustness to missing domain labels, λ=0 working well) leans toward this interpretation, but the paper does not explicitly draw this conclusion.

## Suggestions

1. **Reconcile theory with implementation**: Either adjust Theorem 1 to cover the λ=0 case (showing what feature structure emerges under single-loss training with a frozen orthogonal head), or run Stage 2 with λ>0 and report results, or explicitly state that the theory covers the general framework while the λ=0 simplification is an empirically justified approximation. The current framing leaves an unnecessary credibility gap.

2. **Add DANN as a baseline**: Even a single-dataset comparison would help establish whether CFA's design choices (frozen heads, orthogonality) matter relative to adversarial domain alignment.

3. **Tone down absolute superiority claims**: The improvements are real but modest on some datasets. Rephrase "outperforms" to "consistently improves OOD accuracy across most settings, with gains ranging from modest (1–2 pts) to substantial (5+ pts)."

4. **Clarify the OOD selection procedure**: Add a control experiment using random masking (instead of lowest 20% zero-shot accuracy) to validate that the benchmark isolates compositionality rather than inherent difficulty.

5. **Ablate the domain head entirely**: Test a variant with only a single orthogonalized class head (no domain head at all) to measure the domain head's marginal contribution.

## Score and Decision

The paper addresses an important and genuinely understudied problem (compositional generalization under domain-class sparsity), contributes a useful benchmark, and proposes a method that empirically improves OOD accuracy across multiple settings. The main weakness — the λ=0 discrepancy between theory and implementation — is real and should be addressed, but it does not invalidate the empirical contribution. The improvements are consistent if sometimes modest, and the method's simplicity and robustness to missing domain labels are practical virtues. The paper is a solid contribution that can be strengthened with clarifications rather than requiring a fundamentally new approach.

**Score**: 6.5

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>