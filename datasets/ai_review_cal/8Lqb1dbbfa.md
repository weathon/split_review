- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3
Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes FusionDTI, a drug-target interaction (DTI) model that uses frozen pre-trained language models (SaProt for proteins with structure-aware vocabulary, SELFormer for drugs with SELFIES) to encode drugs and proteins at the token level, then applies a token-level fusion module (Cross Attention Network or Bilinear Attention Network) to capture fine-grained binding information. The model achieves state-of-the-art results on BindingDB, BioSNAP, and Human benchmarks.

## Strengths

1. **State-of-the-art empirical performance.** FusionDTI-CAN achieves an AUROC of 0.989, AUPRC of 0.990, and accuracy of 96.1% on BindingDB in-domain (Table 1), outperforming all eight baselines including BioT5 (0.963 AUROC). These gains are substantial and consistent across multiple datasets.

2. **Ablation study isolates the fusion module's contribution.** Table 3 shows that removing the CAN fusion module (while keeping the same SaProt + SELFormer encoders) drops AUC from 0.989 to 0.954 on BindingDB — a 3.5-point decrease that directly attributes meaningful gains to the fusion mechanism rather than purely to the PLM encoders.

3. **Fusion scales analysis supports the core thesis.** Figure 5 demonstrates a clear monotonic relationship: finer-grained fusion (smaller group sizes) consistently yields better performance, which directly corroborates the claim that token-level interaction matters for DTI prediction.

4. **Cross-domain evaluation and generalization.** The model is evaluated under realistic cross-domain splits where test drugs and targets are unseen during training. FusionDTI-CAN achieves top results on BindingDB cross-domain (0.675 AUROC) and BioSNAP cross-domain (0.748 AUROC), demonstrating practical value for novel DTI discovery.

5. **Explainability via attention visualization.** The case study on three PDB-validated drug-target pairs shows that CAN attention weights highlight known binding sites (e.g., Gln92–benzothiazole in EZL–6QL2) that DrugBAN missed, providing biologically meaningful fine-grained explanations for predictions.

6. **Well-motivated design choices.** Using SELFIES (which always generates valid molecular graphs) instead of SMILES, and incorporating structure-aware (SA) protein vocabulary to capture 3D geometric features, are principled improvements over prior approaches.

7. **Efficiency through pre-encoding.** Storing pre-encoded representations eliminates redundant encoder forward passes, enabling faster training — a practical advantage for large-scale drug screening.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **BAN equation has a dimensional inconsistency.** In Eq. 1, the paper defines \(\mathbf{P} \in \mathbb{R}^{N \times \rho}\), \(\mathbf{D} \in \mathbb{R}^{M \times \phi}\), \(\mathbf{U} \in \mathbb{R}^{N \times K}\), \(\mathbf{V} \in \mathbb{R}^{M \times K}\). Then \(\sigma(\mathbf{P}^\top\mathbf{U})\) is \(\rho \times K\) and \(Att\) is \(\rho \times \phi\), but their product in \(\sigma(\mathbf{P}^\top\mathbf{U}) \cdot Att \cdot \sigma(\mathbf{D}^\top\mathbf{V})\) requires \(K = \rho\) which is not stated or justified. This needs correction for mathematical coherence. While this does not affect the CAN-based main results (CAN equations are dimensionally consistent), it is an error that should be fixed.

2. **The "without CAN" ablation baseline (Table 3) is critically under-described.** The paper states "when the fusion module is omitted" without specifying the architecture used in its place. The reader cannot tell whether this baseline uses mean pooling + concatenation, a simple linear layer, or some other aggregation. This matters because the 3.5-point AUC drop (0.989 → 0.954) is the paper's best evidence isolating the fusion module's contribution — but its interpretability depends on knowing what "no fusion" actually means architecturally. The ablation is also only on BindingDB.

3. **Human cross-domain underperformance is not discussed.** In the cross-domain Human setting (Table 2), FusionDTI-CAN achieves only 0.801 AUROC, substantially underperforming SiamDTI (0.863) and BioT5 (0.856). This is a nontrivial gap that the paper does not acknowledge or attempt to explain, limiting the generality of the claimed advantage.

4. **Efficiency analysis contains an internal contradiction.** The text states "FusionDTI-CAN and FusionDTI-BAN… approximately 45 minutes and 220 minutes, respectively" (CAN=45min, BAN=220min), yet later claims "FusionDTI-BAN runs faster than FusionDTI-CAN." These statements are inconsistent and need clarification.

5. **Missing training details.** The paper does not report the optimizer, learning rate, batch size, number of epochs, GPU hardware, or the number of random seeds used to compute the reported standard deviations. These omissions make reproduction unnecessarily difficult.

### Trivial
None.

## Nice-to-Haves

- The main comparison tables (Tables 1 and 2) compare FusionDTI (PLM encoders + fusion) against methods with substantially weaker encoders. Adding a baseline that uses the same SaProt + SELFormer encoders but with simple pooling + concatenation (i.e., the ablation condition from Table 3) into the main tables would more cleanly separate the fusion module's contribution from the encoder advantage.
- Including the "without CAN" ablation on all three datasets (not just BindingDB) would strengthen the isolation of the fusion module's effect.
- Explicitly stating the encoder output dimensions (the actual \(h\) in CAN, \(\phi\) and \(\rho\) in BAN) would improve clarity.

## Removed Points

- **"Evaluation fundamentally conflates encoder benefit with fusion benefit."** The ablation study (Table 3) already provides a controlled comparison keeping encoders fixed, showing a 3.5-point AUC gain from the CAN module. The concern is partially addressed by the paper itself and is therefore softened to the description gap in point #2 above.
- **The harsh critic's observation that the 6% accuracy improvement is only against BioT5 and not "stronger non-PLM baselines."** BioT5 is the strongest baseline across all metrics; comparing against it is appropriate. Removed as it misreads the comparison structure.
- **"Request for head-to-head with BioT5 using the same encoders."** This asks for experiments outside the paper's stated scope and would require retraining a different model architecture, not a controlled ablation. Demoted to Nice-to-Have.
- **Strength Finder's claim about efficiency (45 min vs 220 min for pre-coded vs non-pre-coded).** The strength finder misinterprets which numbers correspond to which setting. Kept the efficiency point but with corrected framing.

## Novel Insights

The most noteworthy observation emerging from the review is the asymmetric strength of the FusionDTI approach: token-level fusion appears to work very well when the test distribution contains some familiar drugs or targets (in-domain) or when the data is large (BindingDB, BioSNAP), but its advantage substantially erodes on the smaller Human dataset in the cross-domain setting, where SiamDTI — which uses a completely different architectural philosophy (dual-channel local/global protein information) — outperforms it. This suggests that the value of token-level fusion may depend on dataset characteristics (size, diversity, homology patterns) that are not explored in the paper. Understanding when token-level fusion helps versus when simpler strategies suffice would be a valuable direction for future work.

## Suggestions

- Fix the dimensional inconsistency in the BAN equation (Eq. 1). Ensure all matrix products are dimensionally coherent, or clarify if a transposition is intended differently.
- Explicitly describe the "without CAN" ablation architecture: specify whether it uses mean pooling + concatenation or some other aggregation, and ideally extend this ablation to all three datasets.
- Acknowledge and briefly discuss the Human cross-domain gap relative to SiamDTI and BioT5.
- Resolve the efficiency timing inconsistency (45 min vs 220 min vs "BAN runs faster").
- Add a reproducibility paragraph with optimizer, learning rate, batch size, number of epochs, GPU details, and number of random seeds.
