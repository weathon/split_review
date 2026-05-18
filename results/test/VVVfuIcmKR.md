Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper identifies and demonstrates a core limitation of off-the-shelf CLIP-style models: their intra-modal (image-image, text-text) similarity comparisons are inherently suboptimal because the contrastive pre-training objective focuses exclusively on inter-modal alignment and leaves intra-modal relationships uncalibrated. The authors show that converting intra-modal retrieval tasks into inter-modal ones via optimization-based modality inversion (OTI for images→text, OVI for text→images) consistently improves performance across 15+ datasets and five model variants, while a control experiment confirms the improvement stems from exploiting CLIP's inter-modal alignment rather than from inversion per se.

## Strengths

- **Broad empirical validation across multiple datasets and models**: Table 1 reports image-to-image retrieval mAP on 15 datasets for five CLIP/SigLIP variants. In every case, OTI-inverted (inter-modal) features outperform native intra-modal features with consistent gains (e.g., 67.8→70.2 for CLIP ViT-B/32 on Birds, 58.5→61.3 on Food). This directly supports the core claim.

- **Control experiment confirms the effect is due to inter-modal nature, not inversion itself**: Table 2 (right) shows that the *same* OTI-inverted features applied to zero-shot classification (an inter-modal task) *decrease* accuracy (e.g., 72.8→63.8 on ImageNet). The asymmetry — improvement on retrieval but degradation on classification — cleanly isolates the cause: converting task modality type, not the inversion process, drives the gains.

- **Mechanistic analysis linking inversion behavior to inter-modal alignment**: Figure 3(a-b) shows that peak retrieval performance occurs when the inversion loss is still far from zero (i.e., before features drift back toward the image manifold), and Figure 3(c) demonstrates that OTI-image similarity distributions are closer to text-image than to image-image distributions. This evidence chain supports the causal mechanism.

- **Demonstration that intra-modal loss during pre-training mitigates misalignment**: Table 3 shows that SLIP (which adds a SimCLR-style intra-modal loss) nearly eliminates the OTI advantage on CIFAR-100 (intra-modal 89.8 vs. OTI 90.4, compared to the large gap on vanilla CLIP). This corroborates the root-cause analysis.

- **Link between modality gap and intra-modal misalignment**: Table 4 shows that fine-tuning CLIP with a high temperature (τ=1.0) — which closes the modality gap — eliminates the performance advantage of OTI (on CIFAR-10, intra-modal 93.7 vs. OTI 93.5). This directly ties the modality gap phenomenon to the observed misalignment.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Language about the "text embedding manifold" is slightly stronger than the evidence supports**: The paper claims that OTI-inverted features "still lie in the text manifold" (Sec. 6.4), but the supporting evidence (Fig. 3(c)) shows substantial overlap among all three similarity distributions (image-image, text-image, OTI-image) in the 0.7–0.9 range. The paper's own caption describes OTI similarities as "closer to those related to texts than images" — a relative claim — while the body text makes a categorical one. The empirical evidence (improved retrieval + degraded classification + performance peak before convergence) is sufficient for the paper's overall argument, but the "text manifold" framing implies a sharper separation than the data unambiguously show. Tightening this language would improve precision without weakening the contribution.

### Trivial
None.

## Nice-to-Haves

- **Systematic quantification of the modality gap → misalignment relationship**: Section 6.6 demonstrates the effect with two fine-tuned models on three datasets. A more systematic sweep across multiple models/datasets plotting modality gap magnitude (e.g., centroid distance) versus OTI gain would strengthen the causal narrative beyond the current correlational evidence.

- **OVI analysis parallel to Figure 3**: The paper briefly notes that "the same considerations apply to OVI" (Sec. 6.4) but provides no analogous figure for the text→image direction. Given that OVI requires more patches and can approach zero loss, a corresponding analysis would be helpful.

- **Per-query computational cost**: The limitations section notes computational expense and gives step counts (150 for OTI, 1000 for OVI) but does not quantify seconds per query or compare against native feature extraction overhead, which would help practitioners contextualize the trade-off.

- **Additional retrieval metrics**: mAP is used throughout the main tables; R-Precision or recall@k (more commonly used in practical retrieval systems) are reported only in the Section 2 toy experiment. Adding them to the main tables would strengthen practical relevance.

## Removed Points
None. All criticisms from the reviewers are factually grounded and verified against the paper.

## Novel Insights

The reviews do not surface an observation about this paper that goes beyond the paper's own analysis. The contribution — that intra-modal CLIP representations are suboptimal because of the inter-modal contrastive training objective, and that modality inversion recovers the gap — is clearly stated and supported by the paper's own experiments.

## Suggestions

1. **Tighten the language in Sec. 6.4** regarding the "text manifold" claim. Rephrase to something like "OTI-inverted features exhibit similarity distributions that are more characteristic of the text embedding region than the image embedding region" to more precisely match what Figure 3(c) shows.

2. If space permits, add an OVI analysis figure to the appendix parallel to Figure 3 to confirm the symmetry of the phenomenon.

## Score and Decision

This paper makes a clean, well-supported empirical contribution. The core finding — that intra-modal CLIP representations are suboptimal for intra-modal tasks and that inter-modal inversion fixes this — is convincingly demonstrated across extensive experiments with appropriate controls. The minor overclaim about the "text manifold" does not threaten the main argument. The paper is clearly written, honestly discusses limitations, and is likely to influence how practitioners use CLIP for retrieval.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>