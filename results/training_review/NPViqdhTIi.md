Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper adapts Gzip-based Normalized Compression Distance (NCD) — originally proposed for text classification — to molecular property prediction. It introduces MolZip (k-NN with NCD on SMILES strings) and MolZip-Vec (which binned RDKit numerical descriptors are concatenated as non-ASCII characters to the SMILES before compression) and benchmarks them on MoleculeNet classification/regression tasks and PDBbind binding affinity prediction. The key claim is that this training-free, CPU-only approach can be competitive with baseline transformers and GNNs on a subset of tasks.

## Strengths

- **Novel adaptation of compression-based learning to molecular regression and multimodal binding affinity**: The paper extends the prior Gzip-NCD method (limited to text classification) to support regression, class weighting, and multimodal input (SMILES + amino acid sequences), demonstrating competitive RMSE on four regression tasks and strong results on PDBbind binding affinity (Table 3, outperforming all GraphDTA and most GNN baselines). This is a genuine extension beyond the existing literature.

- **MolZip-Vec's string-binning strategy for numerical descriptors consistently improves regression**: Adding 200 RDKit descriptors via Unicode binning (non-ASCII characters concatenated to SMILES) improves RMSE across all four regression tasks (e.g., ESOL: 1.509 → 1.129; LIPO: 0.759 → 0.721) as shown in Table 2. This provides a simple, principled way to inject domain knowledge into a compression-only pipeline without altering the core algorithm.

- **Competitive performance against deep learning baselines without GPU training**: On BBBP and HIV classification, MolZip matches GROVER_large (Table 1), and it outperforms ChemBERTa-1 on 3 of 4 classification tasks. This supports the paper's practical claim that a resource-lean, zero-training alternative can be surprisingly effective against larger models.

- **Open-source implementation with practical extensions**: The code supports multiprocessing, class weighting for imbalanced sets, distance-weighted k-NN regression, and multimodal data loading — making the method directly usable by practitioners.

## Weaknesses

### Fatal
None.

### Major

- **Missing the most obvious chemical similarity baseline: fingerprint + Tanimoto k-NN**: The paper's central claim — that Gzip compression distance is surprisingly effective for molecular tasks — cannot be properly evaluated without comparing against Morgan (ECFP) fingerprints with Tanimoto similarity in a k-NN classifier. This is the simplest, most widely used chemical similarity method, is itself nearly parameter-free, and requires no training. The paper compares MolZip against deep learning models (ChemBERTa, GROVER, GraphDTA) but never establishes whether the compression metric captures anything useful beyond what standard molecular fingerprints already provide. Without this comparison, the reader cannot judge whether NCD adds value over decades-old existing technology, or whether compression is merely rediscovering fingerprint-based similarity at higher computational cost. This is the single most important missing control in the paper.

- **No variance or statistical significance reporting**: All results in Tables 1, 2, and 3 are reported as single numbers with no standard deviations, confidence intervals, or multiple splits. Since the benchmark uses fixed scaffold splits, it is unknown whether observed differences (e.g., MolZip 0.694 vs. GROVER 0.728 on BBBP) are meaningful or within noise. For regression, RMSE differences of ~0.1–0.3 could easily result from a single split. This undermines the reliability of the claimed comparisons.

### Minor

- **Baselines for binding affinity prediction are dated and limited in scope**: Table 3 compares MolZip against GraphDTA and GNN-DTI methods from 2021. While this is acknowledged as a comparison to "basic GNNs," more recent and stronger methods for this task exist (e.g., those incorporating 3D structural information). The paper's claim that MolZip "performs exceptionally well" is relative to this dated baseline set. (Note: structure-based docking methods like DiffDock/EquiBind operate in a fundamentally different setting and are outside the paper's scope, but stronger sequence/structure baselines from 2022–2025 would strengthen the evaluation.)

- **"Parameter-free" is imprecise**: The title and framing call the method "parameter-free," but the system requires user-chosen hyperparameters: k (5 for classification, 25 for regression), bin count (256), encoding choice (SMILES vs. DeepSMILES vs. SELFIES), class-weighting scheme, and whether to use augmentation. While the method has no *trainable* parameters (which is the conventional meaning in the original Jiang et al. paper), the label is likely to mislead readers into thinking there are no tuning decisions at all. No sensitivity analysis for these choices is provided.

- **No ablation of the class-weighting and distance-weighting scheme**: Equation 2 combines class weights with a distance-weighting term `(1 − d̄_i)`. The contribution of this term is not isolated: a comparison to simple majority-vote k-NN and to inverse-distance-weighted k-NN (without the `C_i W_i` term) would clarify whether the proposed weighting actually helps.

- **Choice of `k=25` for regression is not validated**: The paper states this choice is "to potentially smooth noise labels" but provides no grid search, cross-validation, or analysis showing how performance varies with k on different datasets. With k=25 on small datasets like ESOL (1128 molecules), substantial oversmoothing is possible.

- **No sensitivity analysis for the bin count in MolZip-Vec**: The 256-bin choice is described as "empirically" suitable with reference to a single dataset (FreeSolv, Figure A.2). No analysis showing how performance varies with bin count on other regression tasks is provided.

- **Section 2.4 (Chemical Information Retrieval) is entirely qualitative**: The TMAP visualization in Figure 1 shows qualitative similarity between ECFP and compression spaces, but no quantitative neighborhood preservation, retrieval recall, or ranking metrics are provided. The claims about applicability to large-database search remain speculative.

### Trivial

- The paper notes augmentation on regression reduces RMSE by 28% on ESOL but omits these results from the main tables "to be compatible with the results reported for the classification tasks." This is a reasonable decision, but the justification is thin — the asymmetry between classification and regression augmentation behavior is interesting and could be discussed further.

- The paper does not specify whether canonical SMILES are used. Since the method is sensitive to string content (different SMILES for the same molecule yield different compressed lengths), this is needed for exact reproducibility (even though augmentation intentionally varies SMILES).

## Nice-to-Haves

- **Scatter plot of NCD vs. Tanimoto similarity** on a representative dataset would directly address whether compression captures chemical structure or merely correlates with fingerprint-based similarity.
- **Runtime scaling plot** showing wall-clock time vs. training set size, since time complexity is acknowledged as a limitation but no data is provided.
- **Concrete retrieval examples** showing the top-k retrieved molecules by NCD vs. Morgan + Tanimoto for a query molecule, to illustrate whether the methods capture complementary or redundant information.
- **Test on larger datasets (e.g., Tox21, ClinTox)** to assess scalability beyond the current small-to-medium datasets.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that the paper "hides" augmentation results**: The paper explicitly discusses augmentation's 28% RMSE improvement on ESOL (lines 43) and explains why it is omitted from main tables. The paper is transparent about this.
- **Criticism about missing appendix tables (Table A.1, A.2)**: Appendix sections are stripped by the PDF parser; they exist in the original submission.
- **Criticism that the method cannot be evaluated because the paper doesn't test what NCD captures chemically**: While this analysis would strengthen the paper, its absence does not invalidate the comparative benchmark results. Move to Nice-to-Haves.
- **Criticism that "no comparison to KarmaDock, DiffDock, EquiBind"**: These are 3D-structure-based docking methods operating in a fundamentally different setting (requires protein 3D structure, not just sequence). The paper's scope is SMILES + amino acid sequence, making this comparison inappropriate.
- **Criticism that the abstract overstates results**: The abstract says "reach the performance of large-scale chemical language models in a subset of tasks." The data supports this (e.g., MolZip matches GROVER on HIV and BBBP). The framing is accurate.
- **Complaint that SELFIES encoding improves BACE regression but this is "glossed over"**: The paper explicitly notes this as an outlier and provides a clear rationale for choosing SMILES as a balanced baseline.
- **Criticism that the "fuzzy representation" interpretation is speculation**: The paper phrases this as "hinting at" and does not claim it as proven — this is appropriate for a discussion section.

## Novel Insights

The harsh reviewer raises a genuinely important methodological question that the paper does not address: does the compression distance actually capture *chemical* structure, or is it rediscovering trivial string-level regularities? The paper's own Figure 1 shows that the compression space produces TMAP clusters qualitatively similar to ECFP fingerprints — but without a quantitative correlation analysis (NCD vs. Tanimoto similarity), the reader cannot tell whether the compression metric is a reformulation of fingerprint similarity at higher computational cost or a genuinely complementary signal. This question is not merely an ablation; it goes to the heart of what the paper claims to contribute. The fact that MolZip-Vec (which adds explicit chemical descriptors) helps regression but hurts binding affinity (Table 3) further suggests the interaction between compression and chemical information is nontrivial and deserves direct investigation.

## Suggestions

1. **Add the Morgan fingerprint + Tanimoto k-NN baseline** to all benchmark tables (classification, regression, and binding affinity). This single addition would allow readers to assess whether compression-based similarity adds value over standard chemical similarity methods.

2. **Report mean ± std over multiple scaffold splits** (or use repeated random splits) for all main results. Without variance, the comparisons in Tables 1–3 cannot be interpreted with confidence.

3. **Provide sensitivity analyses** for the key hyperparameters: (a) k in k-NN for both classification and regression, (b) bin count for MolZip-Vec across multiple datasets, and (c) ablation of the distance-weighting term in Equation 2 vs. simple majority vote.

4. **Add a quantitative analysis** relating NCD to known chemical similarity (e.g., scatter plot of NCD vs. Tanimoto on a representative dataset) to clarify what the compression metric captures.

5. **Specify whether canonical SMILES are used** for the non-augmented runs, and clarify the exact SMILES generation pipeline for reproducibility.

## Score and Decision

**Originality**: The adaptation of Gzip-NCD to molecular tasks is novel, though the core technique is inherited from Jiang et al. (2022).  
**Importance of research question**: Yes — low-resource alternatives to deep learning for molecular property prediction are practically relevant.  
**Claims well supported**: Partially. The comparisons against deep learning baselines are informative, but the missing fingerprint baseline and lack of variance reporting are significant gaps.  
**Soundness of experiments**: Adequate but incomplete. The experimental design covers multiple tasks but omits critical controls and statistical rigor.  
**Clarity of writing**: Good. The method and results are clearly described.  
**Value to the community**: Moderate — useful as a proof-of-concept and for practitioners with limited GPU access, but the contribution is weakened by the absence of the most basic chemical similarity baseline.

The paper presents an interesting idea and some genuinely surprising results (e.g., Gzip-based prediction working at all on molecules), but the evaluation is incomplete in ways that prevent the reader from assessing the method's true value. The missing fingerprint baseline is the most serious omission — it does not invalidate the paper's core claim (that compression works for molecules), but it does prevent the reader from knowing *how well* it works relative to the simplest existing alternative. The lack of variance reporting further weakens the quantitative claims. With these weaknesses addressed, the paper could be a solid contribution to the low-resource ML for chemistry literature.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>