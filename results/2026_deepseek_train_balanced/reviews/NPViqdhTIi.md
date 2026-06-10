Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper adapts the Gzip-based, parameter-free text classification method (Jiang et al., 2022) to molecular property prediction. It extends the original approach with support for regression, multimodal protein-ligand binding affinity prediction, and string-encoded numerical descriptors (MolZip-Vec). The core empirical finding is that compression-based kNN on SMILES strings yields competitive performance against baseline chemical transformers (ChemBERTa-1, GROVER) on several MoleculeNet benchmarks while requiring orders of magnitude less compute.

## Strengths

- **Parameter-free method shows non-trivial performance on molecular classification.** Table 1 demonstrates that MolZip outperforms ChemBERTa-1 on 3 out of 4 classification datasets (BBBP, BACE, HIV) and matches GROVER_large on BBBP and HIV. This is achieved with zero training and is verifiable from the table data.

- **MolZip-Vec systematically improves regression across all four tasks.** Table 2 shows MolZip-Vec outperforming MolZip on Delaney/ESOL (RMSE 1.510→1.097), Lipophilicity, BACE (regression), and Clearance. Figure A.2 further shows the benefit grows with training set size — a clean signal that the string-binning strategy works.

- **Multimodal binding affinity prediction outperforms multiple GNN-based methods on PDBbind.** Table 3 reports MolZip achieving RMSE 1.365 vs. GCN (1.543), GAT (1.486), GIN (1.477), and GNN-DTI (1.400), including methods that use 3D spatial information. This is a genuinely novel application of compression-based similarity to a biosequence+chemical string problem.

- **Dramatically lower computational requirements.** All benchmarks ran on a single consumer CPU (Intel i7-13700K) in under 44 hours total. Molformer-XL, by contrast, required 208 hours on 16 NVIDIA V100 GPUs for pre-training alone. This resource differential is a concrete, verifiable advantage.

- **Systematic ablation of molecular string encodings.** Table A.1 evaluates SMILES vs. DeepSMILES vs. SELFIES with quantitative results, giving practitioners actionable guidance on encoding choice.

## Weaknesses

### Fatal

None.

### Major

1. **The paper never specifies what data split MolZip uses, and all baseline numbers are taken from different publications without verification of split consistency.** The benchmarking section (line 124) states: "The benchmarking results and details of ChemBERTa-1, ChemBERTa-2, and MOLFORMER-XL were taken from the respective publications. For GROVER, the benchmark results based on scaffold splits have been taken from Zhou et al. (2023)." Nowhere does the paper state what data split MolZip itself used — whether scaffold splits, random splits, or another scheme. The only mention of "scaffold splits" is in the note about where GROVER's numbers come from. Since MoleculeNet results are known to be sensitive to the choice of split (scaffold vs. random vs. time-based) and to the random seed used for scaffold assignment, the head-to-head comparisons in Tables 1 and 2 conflate model performance with potentially different evaluation protocols. The claims that MolZip "performs better on 3 out of 4 data sets" against ChemBERTa-1 or is "on par" with GROVER_large are not supportable without controlled comparison under identical splits. This is the most consequential weakness — it undermines the paper's central comparative evidence. (Split-mismatch concern verified from the paper text: no split specification for MolZip anywhere in Sections 2-3.)

2. **No variance or statistical significance reporting.** All results in Tables 1-3 are reported as single point estimates with no error bars, confidence intervals, or standard deviations. For a kNN method with no stochasticity in training, variance across different train/test splits is the relevant quantity. Without it, the reader cannot assess whether reported advantages over baselines are within the noise of the evaluation. (Verified: no uncertainty quantification anywhere in the reported results.)

### Minor

3. **Inconsistent treatment of augmentation results.** The paper states (line 43) that augmentation-based regression results are suppressed "to be compatible with the results reported for the classification tasks." This is internally inconsistent: the binding affinity prediction benchmark (Table 3) is a regression task and explicitly uses augmentation ("*Augmented with an additional SMILES"). The suppression also hides a 28% RMSE improvement on Delaney/ESOL (from 1.510 to 1.097), which would materially change the assessment of MolZip's regression performance. The stated rationale does not justify this reporting decision.

4. **"Parameter-free" framing is somewhat overstated.** The method has no trained parameters but has several hyperparameters: k (5 for classification, 25 for regression — set arbitrarily), number of bins for MolZip-Vec (256, "empirically found" without supporting ablation), and the choice of molecular encoding (SMILES chosen over alternatives using Table A.1). These are not learned weights but are design choices that affect performance, and the paper provides no sensitivity analysis. The framing is not deceptive but lacks the rigor expected for this descriptor.

5. **No runtime breakdown or per-task compute comparison with baselines.** The paper reports a total benchmark runtime of 43h 55m but does not break this down by task or compare it to the training+inference time of the baselines. Since the paper claims to be a "low-resource" alternative, quantitative runtime comparison against even one baseline (e.g., time per fold for ChemBERTa-1 vs. MolZip) is the natural evidence for this claim and is missing.

6. **k hyperparameter is not analyzed.** Classification uses k=5, regression uses k=25, with only "to potentially smooth noise labels" as justification for the latter. No analysis of how performance varies with k is provided, leaving it unclear whether the method's reported results are driven primarily by the compression distance or by the choice of k.

### Trivial

None.

## Nice-to-Haves

- Ablation of the MolZip-Vec bin count (stated as 256 "empirically found" without supporting data).
- Comparison of MolZip's inference time against a forward pass of ChemBERTa-1 on the same hardware.
- Statistical characterization of the SELFIES outlier on BACE (0.720 vs. ~0.67-0.68) beyond labeling it an "outlier."

## Removed Points

*These points were raised by the reviewers but are removed after verification against the paper:*

- **"The split-mismatch is structural and cannot be fixed"** (Harsh Critic, Claim 1, overstated severity). It CAN be addressed by verifying splits or re-running baselines. It remains a Major weakness but is not unfixable.
- **"Modality asymmetry in binding affinity comparison"** (Harsh Critic, Claim 3, speculative). The paper explores multiple modality combinations in Table A.2 and is transparent about which worked best. The concern about GNNs using whole-protein vs. binding pocket is a reasonable question but not a verified weakness — the cited baselines (Nguyen et al., 2021) are described in the paper as using "protein sequence as inputs," which is consistent with what MolZip also uses.
- **"Class-weighted kNN formulation is a strength"** (Strength Finder). This is a straightforward application of standard weighted kNN with scikit-learn's class_weight function. It is adequately described but not a novel contribution.
- **"MolZip-Vec reduces performance on binding affinity"** (Harsh Critic, noted as "interesting but unexplained"). This is an empirical finding honestly reported, not a weakness.

## Novel Insights

The most interesting observation across the reviews is the structural asymmetry in what the paper demonstrates convincingly vs. what it claims to demonstrate. The paper convincingly shows that compression-based methods *work at all* for molecular property prediction — a non-trivial finding given that SMILES strings are shorter and less redundant than natural language text. This core result is robust even if the exact comparison numbers shift. What the paper claims, however, is specific competitiveness against particular models, and that claim is where the evaluation methodology falls short. This tension — between an interesting proof-of-concept and an over-ambitious comparative framing — is the fundamental issue the authors should address.

## Suggestions

1. **Specify the data split used for MolZip and verify it matches the baselines.** If the standard DeepChem scaffold split is used (as the paper's comparison to GROVER's scaffold-split numbers implies), state this explicitly and cite the implementation. If the splits cannot be verified, re-run a representative subset of baselines under identical conditions.

2. **Report regression results with augmentation as the primary configuration**, or at minimum present both augmented and non-augmented results and let the reader assess. The current suppression undermines the method's demonstrated capabilities.

3. **Add variance estimates.** Report results across multiple train/test splits or bootstrap resamples. This is essential for interpreting the comparative claims.

4. **Add a runtime comparison table** showing per-task inference time for MolZip vs. a forward pass through at least one baseline transformer (e.g., ChemBERTa-1 inference on the same hardware).

5. **Provide a k-sensitivity analysis** for at least one classification and one regression dataset to establish that the chosen values are reasonable.

## Score and Decision

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>