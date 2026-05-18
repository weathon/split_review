Now I have a clear picture of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper addresses hierarchical classification by proposing two interconnected contributions: (1) Hierarchical Multi-Modal Contrastive Fine-Tuning (HMCF), which uses a CLIP-based text encoder to compute contrastive losses at multiple levels of a taxonomy, and (2) graph diffusion-based inference, which refines prediction scores over the taxonomy graph as a post-processing step. The paper motivates both from a "hierarchical manifolds" perspective—the claim that data lie in nested manifolds corresponding to taxonomic levels, and that diffusion can navigate these manifolds. Experiments on iNat18 (with claims about iNat21) show that HMCF + diffusion outperforms prior hierarchical classification methods across multiple metrics.

## Strengths

- **Consistent and sizable empirical gains over prior methods.** Table 4 shows HMCF + diffusion outperforms eleven prior methods (flat softmax, conditional softmax, descendant softmax, Deep RTC, soft-margin, etc.) on iNat18 across all reported metrics, under a unified CLIP ResNet-50 backbone. This is the strongest piece of evidence in the paper.

- **Diffusion inference is model-agnostic and broadly beneficial.** Table 2 demonstrates that both general diffusion and differentiable diffusion improve the bottom-up baseline across six different fine-tuned models (trained with HMCF, cross-entropy, descendant softmax, at different label levels, different backbones). The gains hold for all metrics and all models, establishing generality.

- **Convergence proof for the diffusion process.** Section 3.2 provides a clean convergence analysis, showing the iterative process converges to a closed-form solution \(f^* = (1-\alpha)(I-\alpha\bar{W})^{-1}f^0\), connecting the method to established graph diffusion theory.

- **Identification of misalignment between leaf-level Top-1 and hierarchical metrics.** The paper notes (Section 4.2) that L-Top1 does not consistently align with hierarchical metrics like AP, underscoring the need to evaluate hierarchical classification with appropriate metrics rather than relying solely on leaf-level accuracy.

## Weaknesses

### Fatal
None.

### Major

**1. The text encoder is a confound that prevents clean attribution of gains to hierarchical supervision.** This is the paper's most significant weakness. Table 3 shows that switching from cross-entropy to multi-modal contrastive loss **at the leaf level only** (CE7 → MCL7) yields a ~6.6% AP improvement. Adding hierarchical labels on top of the text encoder (MCL7 → HMCF L1-7) gives only ~1.6% additional AP improvement. Meanwhile, Table 4 compares HMCF against baselines that use the CLIP **visual** encoder only—no text encoder. This means the claimed contribution of "explicitly leveraging the hierarchical taxonomy" via HMCF is conflated with the use of the text encoder and contrastive loss. A proper ablation would compare methods that also use the text encoder (with leaf-only supervision) or visual-only hierarchical losses, to isolate what the hierarchy itself contributes. The paper acknowledges this setup in Section 4.2 but does not resolve it, and the narrative in Sections 4.3 and 5 presents the combined gain as evidence for hierarchical supervision.

**2. No quantitative analysis of when or why graph diffusion helps.** The paper motivates diffusion with a "hierarchical manifolds" hypothesis (Section 3.1) and a Chihuahua example, but provides no empirical analysis of what errors diffusion actually fixes. Does it primarily correct parent-level errors, child-level errors, or sibling confusions? What fraction of test examples change after diffusion, and how many are corrected vs. newly misclassified? Without this, the manifold argument remains an unsubstantiated metaphor, and the mechanism by which diffusion improves accuracy is opaque. Given that the paper frames diffusion as a central contribution, this analysis is necessary.

**3. Missing results for iNat21.** The abstract and introduction claim evaluation on "two large-scale datasets, iNat18 and iNat21," the datasets section describes iNat21 in detail, and the conclusion repeats the claim. However, all results tables (Tables 1–4) present iNat18 only. No iNat21 results appear in the paper, and there is no reference to an appendix or supplementary where they might reside. For a paper that stakes its claims on comprehensive validation, this is a significant gap.

### Minor

**1. Differentiable diffusion is under-validated.** The paper introduces differentiable diffusion (Section 3.2) as a learned linear transform that could replace the fixed connection matrix, but the experimental support is thin: one row in Table 1 (AP 69.2 → 69.5, marginal) and one row in Table 2. There are no training details, no analysis of what the learned transform captures, no convergence curves, and no comparison of learned weights to the fixed taxonomy matrix. This is presented as a contribution but is essentially untested.

**2. Computational cost of diffusion is not discussed.** The closed-form diffusion requires inverting an \(n \times n\) matrix, which is prohibitive for taxonomies with thousands of nodes (iNat18 has ~14k nodes). The paper shows an ablation of \(t\) iterations (Figure 3) but does not discuss whether the iterative approximation is used in practice for large taxonomies, nor report wall-clock time or memory requirements. For a method that operates at inference time, this is a practical concern.

**3. Metrics are defined only by reference to prior work.** The paper states it follows Valmadre (2022) for metrics (AP, AC, R@X, M-F1, L-F1) but does not define what AP and AC mean in a hierarchical output space. While citing the source is standard practice for a camera-ready paper, the main text's lack of definitions makes it hard to evaluate whether reported improvements are meaningful or numerically small, especially since AP and AC are the key metrics for the paper's claims.

### Trivial

- The "hierarchical manifolds" concept is presented as intuition (Figure 1) without formal definition or measurement, but this is a framing device rather than a mathematical claim; the paper's technical contributions do not depend on a rigorous manifold formulation.
- No confidence intervals or multiple-run statistics are reported. This is common for large-scale benchmark evaluations in this field, so it is a minor concern, but several claimed improvements are small enough that variance is relevant.

## Nice-to-Haves

- Add a controlled ablation: compare HMCF against a variant that uses the text encoder with contrastive loss but leaf-only labels (MCL7 in the paper already exists) after applying diffusion, to fully disentangle text encoder from hierarchical supervision.
- Compare HMCF against a visual-only hierarchical contrastive loss (e.g., supervised contrastive learning with hierarchical labels, Khosla et al. 2020) to isolate the hierarchy contribution without the text encoder.
- Analyze diffusion behavior quantitatively: what fraction of predictions change, categorized by error type (parent-level, child-level, sibling).
- Report computational cost (runtime, memory) for diffusion at inference time.
- Train differentiable diffusion more rigorously and analyze its learned weights.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"First attempt to apply graph diffusion to hierarchical classification" claim is questionable.** Removed because this is a defensible claim when situated specifically in the deep learning / VLM-based hierarchical classification context. The paper cites Zhou et al. (2003a/b) and distinguishes its setting from semi-supervised label propagation. Whether this is truly the "first" is a matter of scope definition, not a factual error that undermines the paper.

- **"Multi-modal" term is inflated.** Removed as a semantic nitpick. Using CLIP's text encoder with category names as text inputs is a standard multi-modal (vision + language) setup. The term is appropriate.

- **"The manifold argument remains a metaphor" — this is already covered by the verified quantitative analysis weakness (Major #2).** The core concern (lack of analysis) is kept there; the phrasing about metaphor is redundant.

- **"Missing related works" comments about label propagation.** Removed per instruction: the paper cites relevant prior work (Zhou et al. 2003a/b, Page et al. 1998, Iscen et al. 2017) and the critic does not provide a specific missing reference that is clearly relevant and omitted. The rule states not to mention missing related works without external confirmation.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a well-known tension: when a method has multiple novel components (text encoder + hierarchical loss + diffusion), and one component (the text encoder) dominates the performance gains, it is difficult to claim that the other components are individually responsible for the observed improvements. This is a general lesson for multi-component systems papers but not a novel insight specific to this work.

## Suggestions

- **Disentangle the text encoder from hierarchical supervision.** Add an ablation that trains HMCF with the text encoder but only leaf-level labels (Table 3's MCL7 is already this), and compare against HMCF L1-7 with the same post-diffusion inference. Report both in a single table so readers can see the marginal contribution of hierarchical labels beyond the text encoder.
- **Provide a diffusion behavior analysis.** Report the fraction of test examples where diffusion changes the top prediction, and break down whether the change corrects parent-level errors, child-level errors, sibling confusions, or introduces new errors. This would directly test the manifold hypothesis and make the method interpretable.
- **Add iNat21 results** to the main paper (or explicitly reference an appendix containing them), and discuss how the balanced vs. long-tailed distribution affects the relative gains.
- **Validate differentiable diffusion more rigorously** with training curves, analysis of learned weights, and a comparison against the fixed taxonomy matrix to show what the learned transform captures.
- **Define AP and AC for the hierarchical setting** briefly in the main paper, or at least provide the key formula, so readers can interpret the main experimental results without cross-referencing Valmadre (2022).

## Score and Decision

The paper proposes a sensible combination of ideas (hierarchical contrastive learning + graph diffusion inference) and demonstrates strong results on iNat18. However, the core claim about hierarchical supervision driving the improvements is not cleanly isolated from the text encoder confound, which undermines the paper's main narrative. The missing iNat21 results and under-explored differentiable diffusion further weaken the submission. The contributions are real but incompletely supported by the experimental design as presented.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>