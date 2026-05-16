I have thoroughly reviewed the paper and all the reviewer inputs. Let me now construct the consolidated review.

## Summary

This paper adapts the Gzip-based text classification method (Jiang et al., 2022) to molecular property prediction. The authors extend the original approach with multiprocessing, class-weighting, kNN regression, and multimodal input support, and propose MolZip-Vec which converts numerical RDKit descriptors into Unicode strings concatenated with SMILES. The method is benchmarked against ChemBERTa-1, ChemBERTa-2, GROVER, and several GNN-based methods on MoleculeNet classification/regression tasks and PDBbind binding affinity prediction. The core thesis is that a training-free compression-based method can be surprisingly competitive with deep learning baselines, particularly on binding affinity where it outperforms multiple graph-based methods.

## Strengths

- **Competitive classification performance against transformer baselines**: On MoleculeNet classification (scaffold splits), MolZip outperforms ChemBERTa-1 on 3/4 datasets (BBBP, Tox21, HIV) and performs on par with GROVER_large on BBBP and HIV, all without any GPU training (Table 1). This provides concrete evidence that a simple compression-based approach can match early deep learning efforts.

- **Exceptional binding affinity prediction outperforming structure-aware GNNs**: On PDBbind, MolZip achieves lower RMSE than all GraphDTA methods and outperforms geometricdeep learning methods like GNN-DTI that use explicit 3D structural information (Table 3). This is a genuinely surprising and well-supported result for a method that only uses SMILES strings and amino acid sequences.

- **Novel and effective MolZip-Vec extension for regression**: The conversion of 200 RDKit descriptors into Unicode strings and concatenation with SMILES consistently improves regression RMSE across all four datasets (Table 2), with the improvement growing with training set size on FreeSolv (Figure A.2). This is a clean, domain-informed extension that integrates chemical knowledge without altering the core compression algorithm.

- **Practical engineering contributions**: The paper implements multiprocessing, class-weighted kNN for imbalanced datasets, multimodal data loading (SMILES + amino acid sequences), and releases the implementation as an open-source library. These extensions make the method applicable to realistic cheminformatics scenarios beyond the original text-classification setting.

- **Demonstrated qualitative similarity to fingerprint-based chemical space**: The TMAP visualization (Figure 1) shows that the NCD-based compression space produces similar clustering of blood-brain barrier penetrating molecules as the established ECFP fingerprint space, suggesting potential for structure-based similarity search in ultra-large databases.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Data split protocol not specified for all baselines, weakening comparability**: The paper does not explicitly state what data split (scaffold vs. random) was used for the MolZip experiments. The only clue is the note that GROVER numbers come from Zhou et al. (2023) "as the authors of the original GROVER paper did not include benchmark results for scaffold splits," implying MolZip uses scaffold splits. For the ChemBERTa-1 and ChemBERTa-2 baselines, results are simply "taken from the respective publications" without specifying the split protocol. Since different splits produce different difficulty levels, the paper should clearly state the split used for every method in Tables 1 and 2. If MolZip uses scaffold splits (harder) and ChemBERTa used random splits (easier), the comparison could be unfair to MolZip — but the paper never makes this transparent. This is a reporting gap that undermines confidence in the numerical comparisons.

- **Augmented regression results omitted from main tables without compelling justification**: In Section 2.2, the authors show that SMILES augmentation (concatenating multiple valid SMILES strings of the same molecule) reduces RMSE on Delaney/ESOL by 28% (from 1.510 to 1.097) and has a general positive effect on regression tasks (Figure A.1c,d). They then state: "However, we omit reporting augmentation-based results for the regression tasks to be compatible with the results reported for the classification tasks." Consistency with classification is not a scientifically compelling reason to suppress clearly better regression results — especially since the augmented RMSE of 1.097 on Delaney/ESOL would be competitive with ChemBERTa-2 MTR (1.058). The paper would be stronger by reporting both augmented and non-augmented results, or by presenting augmentation as the primary regression configuration and explaining the asymmetry.

- **PDBbind evaluation lacks critical details (version, exact split)**: The paper does not specify which version of PDBbind was used (e.g., v2016, v2019) or the exact train/test split. The baseline results are "taken from Li et al. (2021)," but the paper does not confirm that the same protocol was followed for MolZip. Since different PDBbind versions and splits yield very different absolute RMSE values, this omission makes the comparison less trustworthy than it should be. The authors should state the PDBbind version, split sizes, and how they ensured protocol parity with Li et al. (2021).

- **"Large-scale chemical language models" overclaim**: The abstract states the method "can reach the performance of large-scale chemical language models in a subset of tasks." The baselines used (ChemBERTa-1, ChemBERTa-2, GROVER) are not large-scale in the current sense of the field (e.g., Molformer-XL with 1.1B molecules, which was explicitly excluded). The comparison is against baseline/early transformers, not large-scale models. This phrasing should be adjusted.

- **Choice of hyperparameters (k for regression, number of bins) lacks sensitivity analysis**: The selection of k=25 for regression (vs. k=5 for classification) and 256 bins for MolZip-Vec are stated but not analyzed. The bin count is justified only as "empirically we found that 256 is a suitable number." A brief ablation (e.g., k=[5,15,25,35], bins=[64,128,256,512]) would strengthen the claim that these choices are not driving the results.

### Trivial

- The abstract says "Parameter-Free" in the title, but the method requires choosing k (5 for classification, 25 for regression), bins (256), and class-weighting. While "parameter-free" is conventionally used for methods without learned weights (kNN is a classic example), the title is slightly at odds with the need for these configurable hyperparameters.
- The PDBbind section refers to "PCBbind data set" (line 64) — a typo for PDBbind.
- The paper could benefit from a brief comparison of computational cost (CPU hours for MolZip vs. GPU hours for training deep learning baselines) to substantiate the "low-resource" advantage.

## Nice-to-Haves

- **Augmented regression as primary or co-reported results**: Reporting the augmented RMSE for Delaney/ESOL (1.097) would make the regression tables noticeably stronger. This is a cheap enhancement (data augmentation, no model retraining) and presenting it transparently would strengthen rather than weaken the paper.

- **PDBbind protocol confirmation**: Explicitly state the PDBbind version (e.g., v2016, v2019), the number of train/validation/test complexes, and confirm the split matches Li et al. (2021).

- **Qualitative ablation on MolZip-Vec ordering and bin sensitivity**: Does the ordering of SMILES + descriptor string vs. descriptor string + SMILES matter? Is performance sensitive to bin count? These are natural questions the authors could address briefly.

- **Time breakdown by dataset and comparison with GPU training costs**: Even a rough comparison (e.g., "training ChemBERTa-2 on 10M molecules requires ~X GPU-hours; our method uses no training and Y CPU-hours for inference on these benchmarks") would substantiate the low-resource advantage.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Parameter-free claim is overstated"** (from Harsh Critic #4): The reviewer claims the method is not parameter-free because it tunes k and bin count. However, "parameter-free" in machine learning conventionally refers to methods without learned/trained parameters (weights) — kNN is the canonical example. The method has configurable hyperparameters but no learned parameters, so the usage is standard. This criticism reflects a terminological disagreement rather than a genuine flaw.

- **"The claim that the method can reach the performance of large-scale chemical language models is slightly too strong"** (framed as a Critical Issue by the reviewer): The abstract qualifies this with "in a subset of tasks." The baselines are ChemBERTa-2 and GROVER (10M molecules each), which are not small models. While the phrasing could be more precise ("baseline transformers" vs. "large-scale"), this is a mild presentational choice rather than an error that affects the paper's contribution.

- **"Binding affinity comparison lacks details about which version of PDBbind"** (from Harsh Critic #3, downgraded from "methodological gap"): This is a valid concern but belongs in Minor — it does not invalidate the comparison (the baselines are from the same reference), it simply needs better documentation.

- **"Section 3.3 - compare CPU time with GPU training time of deep learning baselines"**: This is a nice-to-have, not a weakness. The paper already reports total runtime.

- **Various section-by-section notes** (e.g., "it would be useful to speculate why descriptors hurt classification," "a short paragraph explaining why these older baselines are a fair test would help"): These are editorial suggestions, not weaknesses.

## Novel Insights

The most striking finding that emerges clearly across the reviews is that a compression-based method with no training, no GPUs, and no learned representations can outperform graph neural networks that explicitly encode 3D geometric information on the PDBbind binding affinity task. This suggests that the statistical regularity captured by Gzip compression of SMILES strings and amino acid sequences encodes meaningful biophysical information about protein-ligand interactions — perhaps more than the community might expect. The fact that adding explicit RDKit descriptors (MolZip-Vec) actually *decreases* binding affinity performance while *improving* small-molecule regression further hints at a trade-off between representational specificity and generalizability that could inform future work on compression-based molecular representations. These observations are genuinely novel and go beyond simply transferring a known method to a new domain.

## Suggestions
1. **Clarify data splits for all methods in Tables 1 and 2**: State explicitly whether MolZip used scaffold or random splits, and note the split protocol used in the original ChemBERTa-1/ChemBERTa-2 papers. If the split types differ, either re-run baselines on the same splits or transparently discuss the expected effect on the comparison.
2. **Report augmented regression results alongside non-augmented**: The 28% RMSE improvement on Delaney/ESOL is too significant to relegate to an appendix note. Either make augmented results the primary regression configuration or report both with clear labeling.
3. **Add a brief hyperparameter sensitivity analysis**: A small ablation on k (for both classification and regression) and bin count for MolZip-Vec would address the natural concern that results are tuned to specific values.
4. **Specify the PDBbind version and split protocol** to match Li et al. (2021) and confirm protocol parity.

## Score and Decision

**Originality**: 6/10 — The core method (Gzip + NCD + kNN) is not novel, but the application to molecular property prediction, the MolZip-Vec extension, and the multimodal binding affinity extension are novel contributions.

**Importance of research question**: 7/10 — A low-resource, training-free alternative to deep learning is practically valuable for many real-world drug discovery scenarios.

**Claims well-supported**: 6/10 — The binding affinity results are strongly supported. The classification and regression comparisons are weakened by the lack of transparency about data splits for baselines.

**Soundness of experiments**: 6/10 — The experimental design is reasonable but has gaps in documentation (splits, PDBbind version, augmentation rationale).

**Clarity of writing**: 7/10 — Generally clear and well-structured. Minor issues with the overclaim in the abstract and some missing details.

**Value to research community**: 7/10 — A useful demonstration that simple methods can be competitive, with potential for chemical information retrieval applications.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>