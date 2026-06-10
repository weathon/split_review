## Summary

GeoRDe proposes a hybrid architecture for RNA inverse folding (predicting a 1D sequence from a 3D backbone structure) that combines three existing component types: a triangle-attention-based SeqFormer module adapted from protein structure prediction, a Geometric Vector Perception (GVP) graph neural network for geometric features, a secondary structure auxiliary loss, and BiRNA-BERT embeddings. The method is evaluated on the gRNAde and RDesign datasets and shows generalization on held-out CASP15 and RNA-Puzzle structures.

## Strengths

- **Hybrid architecture combining triangle attention (SeqFormer) with GVP-GNN for complementary geometric reasoning**: the SeqFormer captures structured (covalent-bond-connected) information while the GVP module handles unstructured geometric features via SO(3)-equivariant message passing. The ablation study confirms that adding the GVP module to the SeqFormer baseline substantially improves performance, validating that this combination is more effective than triangle attention alone.

- **Demonstrated generalization to held-out CASP15 and RNA-Puzzle datasets** (Section 4.2): GeoRDe trained on the gRNAde dataset maintains competitive performance on CASP15 structures not accessible during training and on diverse RNA-Puzzle targets — a more rigorous generalization evaluation than many prior RNA design papers provide.

- **Multi-task learning of secondary structure constraints**: the pair constraint module (Section 3.4.3) predicts base-pairing probabilities (AU, CG, UG) as a separate supervised task with its own cross-entropy loss, which the ablation confirms contributes to final performance.

## Weaknesses

### Fatal

None.

### Major

- **Severely underspecified method prevents reproducibility assessment.** The paper omits almost all training and architectural details: number of layers and hidden dimensions for SeqFormer, GVP, and Transformer components; the value of N for recycling iterations (line 119: "N recycle iterations" with no number given); training hyperparameters (optimizer, learning rate, batch size, epochs, gradient clipping, schedule); loss weighting coefficients α and β (line 207); dataset splitting procedure (how training/validation/test were partitioned, what clustering thresholds were used, whether splits match gRNAde/RDesign); whether BiRNA-BERT is frozen or fine-tuned; hardware and framework details. For a methods paper at a top venue, this level of omission prevents assessing the method's soundness or reproducing the results.

### Minor

- **Textual error on line 168**: the paper states the GVP module provides "a comprehensive understanding of **protein** structures" in a paper about *RNA* design — a clear copy-paste error from prior protein work.

- **Ablation description is too sparse**: the ablation results (Table 4) are described in only two sentences (lines 258–259) with no numerical values in the text — "significantly enhanced" and "marginally refines" are not precise enough to convey what drives performance or by how much.

- **"Five distinct methodologies" (line 217) are never enumerated.** The paper states it compared five methods but does not name them in the experimental section, leaving ambiguity about the exact baseline set.

- **Related work catalogs rather than critically differentiates.** gRNAde already uses multi-state GNNs for 3D RNA design. The paper does not articulate what specific deficiency in existing methods GeoRDe addresses or how its triangle attention + GVP architecture differs from gRNAde's approach in concrete terms.

- **Limitations paragraph (lines 275–279) is generic.** It notes that metrics "only partially reflect the accuracy of computational design" without identifying a single concrete limitation of GeoRDe itself (e.g., performance on long RNAs, handling of pseudoknots, sensitivity to input noise, computational cost).

### Trivial

- Contributions list formatting: item 1 begins with a bare "." (line 20).
- Conclusion grammatical issue (lines 273–274): "positions it as a powerful tool" grammar is broken.

## Nice-to-Haves

- A systematic tertiary-structure evaluation comparing self-consistency RMSD of GeoRDe-designed sequences against those from gRNAde and RDesign using the same folding predictor, instead of purely qualitative "low RMSD" examples in Figure 2.
- Per-position recovery analysis (loops vs. stems) and failure analysis for specific structural motifs (pseudoknots, multi-helix junctions).
- Runtime or parameter count comparison across methods, since GeoRDe is a multi-component architecture.

## Removed Points

These points are flagged as removed; treat them with caution.

- **Tables invisible due to placeholder images.** The extracted text shows `![](images/xxx.jpg)` for Tables 1–4 and Figure 2. This is a parser/extraction artifact — the original PDF submission would contain the embedded tables/figures as rendered images. The blank image tags in the extracted text do not reflect the actual submission.
- **"Minimal novelty" / contribution framing.** The harsh critic argued the architecture is an assembly of existing components. While the paper could frame its contributions more carefully (see "Related work" weakness above), the paper openly acknowledges its inspirations (lines 119, 130), and combining existing components in a new domain with demonstrated empirical gains is a legitimate contribution. Removed to avoid overstating the issue.
- **Section numbering and formatting nitpicks** (bare "2.2" heading, mixed `\section` usage). These are likely artifacts of PDF-to-text extraction, not author errors.
- **Missing appendix / supplementary content.** The review guidelines explicitly exclude criticisms about missing appendix sections, as the parser strips these from all papers.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide a complete specification of all architecture dimensions, training hyperparameters, loss weights, data splits, and the number of recycling iterations — ideally in both the main text and a reproducibility checklist.
2. Add numerical values from the ablation to the main text (percentages or relative improvements), not just qualitative adjectives.
3. Fix the copy-paste error on line 168 ("protein" → "RNA").
4. Explicitly enumerate the five comparative methods in Section 4 and clarify which were retrained vs. cited from published numbers.
5. Frame contributions as a combination-and-application to RNA rather than architectural invention, and position GeoRDe concretely against gRNAde: what specific gap does the hybrid design fill?

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>