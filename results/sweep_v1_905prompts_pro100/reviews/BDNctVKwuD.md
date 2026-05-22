Now I have sufficient calibration data. Let me synthesize everything into the final review.

**Round 1 bracket**: The paper sits between the middle band (3.5–7.5) and strong band (>7.5). Compared to 6.0-level anchors (bkdWThqE6q, ozZG5FXuTV), this paper has richer theoretical and empirical contributions. Compared to the 7.33 anchor (GjfIZan5jN), the contribution scope and quality are comparable, though some evaluation concerns persist. **Initial bracket: 6.0–7.5**.

**Round 2 narrowing**: Anchors at 6.25 (57NfyYxh5f — limited to one backbone, narrower scope) and 6.50 (WBUVagRgsd — incremental Shapley method) are clearly weaker. The paper is closer to GjfIZan5jN (7.33) in contribution depth but falls slightly short due to the circularity concern in the IoU metric and some appendix-deferred details.

Final score: **7.0**.

---

## Summary
This paper identifies a theoretical limitation of HiResCAM explanations — they are not uniquely determined under softmax invariance, admitting an arbitrary matrix shift while producing the same prediction. The authors propose ContrastiveCAM, an M-invariant explanation that provides class-versus-class granularity, and use it to diagnose feature misalignment where models rely on spurious non-core image regions. They then derive Core-Focused Cross-Entropy (CFCE), a loss that penalizes non-core contributions while encouraging core-region contrast, and demonstrate across Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC that CFCE-trained models rely substantially more on core regions (e.g., accuracy under core-region ablation drops from 76.5% to 41.8%), work with approximate masks, and improve downstream segmentation.

## Strengths
- **Rigorous theoretical identification of HiResCAM non-uniqueness**: Theorems 3.2 and 3.5 cleanly prove that HiResCAM explanations are ambiguous up to an additive matrix M, and that ContrastiveCAM eliminates this redundancy. This is a genuine theoretical contribution to the CAM interpretability literature.
- **Strong ablation-based evidence for core reliance**: Under core-region ablation (Gray Mask), CFCE accuracy drops to 41.78% vs. 76.53% for CE w/ Arch — a dramatic 35-point gap that directly and independently demonstrates the model now depends on core regions. This metric requires no explanation method and is therefore immune to any circularity concern.
- **Practicality with approximate masks**: Table 3 shows CFCE trained with auto-generated SAM masks achieves ~84% IoU, close to ground-truth mask performance (~83–93%). Bounding-box supervision also yields competitive results. This substantially broadens the method's applicability.
- **Consistency guarantee**: Theorem 4.6 establishes that minimizing CFCE risk converges to the Bayes-optimal risk of the core-constrained formulation, providing theoretical backing that the loss is well-founded.
- **Downstream segmentation improvements**: Figure 4 shows CFCE+KL-trained backbones yield consistently higher per-class IoU when fine-tuned or used end-to-end for segmentation, indicating the learned representations transfer beneficially.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **ContrastiveCAM IoU partially circular as an evaluation metric**: The CFCE loss (Eq. 15) directly optimizes ContrastiveCAM activations to align with core masks, so measuring alignment via ContrastiveCAM IoU reflects optimization success as well as genuine feature alignment. This is mitigated by three facts: (a) CE w/ Arch achieves only 30.27 ContrastiveCAM IoU vs. CFCE's 89.22 — a 3× gap on the same metric; (b) the ablation metrics (Gray Mask, BBOX, Tile, RFS) are independent of any explanation method and strongly corroborate core reliance; and (c) GradCAM IoU also improves (16.25 → 51.52 for CFCE+KL). The concern reduces confidence in the exact IoU numbers but does not undermine the core claim.
- **Accuracy-alignment trade-off underdiscussed**: Hard-ImageNet accuracy drops from 93.69% (CE w/ Arch) to ~90.5% (CFCE). The paper presents this as acceptable but does not analyze when or why this trade-off is warranted. A brief discussion of scenarios where core reliance justifies the accuracy cost would strengthen the narrative.
- **IoU metric source ambiguous for Oxford-IIIT Pets and PASCAL VOC tables**: Tables 3 and 4 do not explicitly state which explanation method (GradCAM, ContrastiveCAM, or reconstructed CAM) was used to compute the reported IoU values. Given the Hard-ImageNet setup, ContrastiveCAM is likely, but this should be stated clearly.

### Trivial
- The KL regularizer (Eq. 18) introduces parameters λ₁, λ₂, λ₃ whose values and selection protocol are not described in the main text, though they presumably appear in the appendix.

## Nice-to-Haves
- Reporting ContrastiveCAM IoU for the non-architectural baselines (CORM, DFR, standard CE) would provide additional context and strengthen the comparison, though CE w/ Arch already serves as the relevant baseline.
- An ablation isolating the effect of the KL regularizer (CFCE vs. CFCE+KL) with analysis of when the divergence term helps vs. hurts would deepen understanding.
- A discussion of the method's limitations — dependence on core-mask availability, sensitivity to mask quality, and scenarios where the accuracy cost may be prohibitive — would round out the contribution.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "The paper never computes ContrastiveCAM-IoU for the baselines"** — Factually incorrect. Table 2 shows CE w/ Arch has ContrastiveCAM IoU = 30.27, providing a direct within-metric comparison. The harsh critic apparently missed this entry.
- **Harsh critic: "Opaque architectural modifications ... prevent disentangling the effect of the loss from the effect of the architecture"** — The architectural modifications are detailed in Appendix C (stripped by the parser but present in the original submission). The paper provides CE w/ Arch as the architecture-matched baseline, so the CFCE vs. CE w/ Arch comparison is on equal architectural footing. The criticism that CORM/DFR are not evaluated on the modified architecture ignores that CE w/ Arch is the primary baseline for isolating the loss effect.
- **Harsh critic: "Theorem 4.6 ('Consistency') is stated but the proof is in the appendix"** — Standard practice; the parser strips appendices from all papers.
- **Harsh critic: "The table introduces 'CFBCE' ... without defining the adaptation to multilabel classification"** — Defined in Appendix B; appendix-stripped content.
- **Harsh critic: "The paper mentions parameters λ₁,λ₂,λ₃ but never states their values"** — Likely in the appendix; hyperparameter reporting is standard in appendices.
- **Harsh critic: "The paper does not discuss the assumption that core masks are accurately known"** — Section 5.2 directly addresses this by experimenting with approximate SAM masks and bounding boxes, demonstrating robustness to imperfect masks.
- **Strength Finder: "The introduction's claim that HiResCAMs may not explain true factors would benefit from a more precise link"** — This is a framing preference, not a substantive weakness. Theorem 3.2 provides the precise link.

## Novel Insights
The paper's most genuinely novel insight is the mathematical connection between softmax shift-invariance and CAM non-uniqueness (Theorem 3.2). While the softmax invariance property itself is trivial, its amplification to a full spatial matrix M in the HiResCAM decomposition, and the demonstration that this can completely corrupt explanations (Figure 1), has not been articulated in prior CAM literature. The further insight that class-versus-class CAM differences are M-invariant (Theorem 3.5) provides a clean theoretical justification for pairwise explanations that goes beyond the usual "contrastive explanations are more informative" intuition.

## Suggestions
- State explicitly in Tables 3 and 4 which explanation method was used to compute IoU (presumably ContrastiveCAM or CAM^Recon). This is a one-line clarification that would eliminate ambiguity.
- Add a brief paragraph discussing when the ~3% accuracy drop on Hard-ImageNet is a reasonable price for core reliance (e.g., safety-critical applications where spurious-correlation failures are unacceptable) versus when it might not be.
- Consider computing ContrastiveCAM IoU for CORM and DFR baselines — even a single forward pass would provide a useful reference point for the community, though its absence does not weaken the paper's core comparisons.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| bkdWThqE6q | INTR interpretable transformer | 6.00 | R1 | Weaker: mostly qualitative, no theoretical backing, narrower scope |
| ozZG5FXuTV | Causal alignment diagnosis | 6.00 | R1/R2 | Weaker: domain-specific, less theoretical novelty |
| 57NfyYxh5f | Probing for post-hoc explanations | 6.25 | R2 | Weaker: single backbone, narrower finding, less methodology |
| WBUVagRgsd | Salvage Shapley explainability | 6.50 | R2 | Weaker: incremental over ViT-Shapley, less theoretical depth |
| GjfIZan5jN | IIS representation interpretability | 7.33 | R1 | Comparable: similar breadth, stronger multi-architecture validation; our paper has richer theory but slightly weaker metric independence |

The paper under review provides a coherent and well-supported contribution: a theoretical finding about HiResCAM, a new explanation method, a derived training loss with consistency guarantees, and strong empirical validation across multiple datasets. The evaluation concerns (partial circularity of ContrastiveCAM IoU) are real but minor — the independent ablation metrics and the 3× ContrastiveCAM IoU gap against the architecture-matched baseline provide sufficient evidence for the core claims. The paper is clearly stronger than the 6.0–6.5 anchors and comparable to, though slightly below, the 7.33 anchor.

**Originality**: The HiResCAM non-uniqueness finding and M-invariant ContrastiveCAM are genuinely novel contributions to the CAM literature. The CFCE loss is a natural but effective derivation.

**Importance**: Feature alignment and shortcut learning are significant problems in robust ML. The paper addresses them through an interpretability-guided training approach that could influence how the community thinks about the relationship between explanation methods and training objectives.

**Claim support**: Core claims are well-supported by both theory and experiments. The ablation metrics provide strong, explanation-method-independent evidence.

**Soundness**: The methodology is sound. The theoretical derivations are correct. The evaluation design is appropriate, with the minor caveat about ContrastiveCAM IoU noted above.

**Clarity**: Well-written, well-structured, with clear notation and effective figures.

**Value**: The paper bridges interpretability and training in a principled way, with practical benefits demonstrated through approximate-mask experiments and downstream segmentation improvements.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>