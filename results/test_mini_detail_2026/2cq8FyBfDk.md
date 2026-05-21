Now I have a solid calibration. Let me write the final consolidated review.

## Summary

This paper introduces ProteinVista, a compute-efficient 3D CNN that processes full-atom protein structures via voxelization, pre-trained on ~500K AlphaFold2 structures using contrastive alignment with ESM-2 embeddings. It achieves strong results on three protein-ligand prediction tasks (enzyme-substrate classification, transporter-substrate classification, and drug-target IC50 regression) while using 5× fewer parameters and ~1% of the GPU-hours compared to ESM-2. The authors demonstrate complementarity between sequence and structure representations through ensemble experiments and provide ablation studies and stratified analyses.

## Strengths

- **Outperforms sequence transformers on three structure-dependent benchmarks**: ProteinVista achieves higher accuracy than ESM-2₆₅₀M on transporter-substrate prediction (90.8% vs 89.3%, Table 1) and a substantially higher R² on IC50 regression (0.69 vs 0.61, Table 2), directly supporting the claim that a full-atom 3D CNN can exceed a much larger sequence model on tasks requiring fine structural resolution.

- **Clear evidence of complementarity with sequence models**: The ESM-ProteinVista ensemble surpasses both individual models on transporter- and enzyme-substrate benchmarks (91.5% vs 90.8% and 89.3%). McNemar's test confirms highly significant error reduction (p < 10⁻¹³ for TSP, p < 10⁻¹⁷ for ESP), supporting the claim that 3D and sequence information are partly complementary.

- **Compute and data efficiency demonstrated with concrete numbers**: ProteinVista has 123 M parameters vs ESM-2₆₅₀M's 650 M, pre-trains on 0.5 M structures (vs 250 M sequences) in 48 hours on four A100s (vs 7 days on 128 H100s) — roughly 1% of the GPU-hours (Section 4.3). Figure 3c shows 1,000 proteins processed in 20s vs 426s for ESM-2₆₅₀M.

- **Stratified analysis pinpoints when structure helps most**: Figure 2a–c bins test proteins by sequence identity, TM-score, and pLDDT, showing ProteinVista outperforms ESM-2 on high-confidence and structurally similar proteins while the ensemble remains superior across all ranges. This directly ties the model's gains to explicit 3D geometry.

- **Systematic ablation studies isolate design choices**: Section 4.2 and Figure 2e quantify the contribution of augmentations, pretraining objective, and voxel resolution; e.g., reducing ensemble views from five to one lowers R² by 6.4%, while removing training augmentations has almost no effect, confirming robustness is learned during pretraining.

- **State-of-the-art results under an optimized pipeline**: After joint fine-tuning and a contrastive prediction head, ESM-ProteinVistaOP surpasses published SOTA on TSP (93.2% vs SPOT's 92.4%) and ESP (94.4% vs 94.2%) in Table 1.

## Weaknesses

### Major

- **No error bars or standard deviations reported**: All results are reported as point estimates without standard deviation over multiple random seeds. While p-values are provided for ensemble comparisons, the lack of variance estimates makes it unclear whether the reported improvements are robust to initialization. This is a standard experimental hygiene issue that should be addressed by reporting mean ± std over at least 3 seeds.

- **Missing structure-aware baselines on the IC50 task**: On the BindingDB IC50 regression task, only ESM-2 variants are compared. No other structure-aware models (e.g., 3D-CNNs without large-scale pre-training, equivariant GNNs, or graph-based methods with structural features) are included. The substrate prediction tasks do include SOTA models, making the inconsistent coverage noticeable. The paper's central claim about the value of structure is weakened by the absence of structural baselines on this task.

- **No contamination/decontamination analysis**: The pre-training corpus consists of AlphaFold2 structures from Swiss-Prot proteins. The fine-tuning benchmarks (TSP, ESP, BindingDB) also draw from Swiss-Prot or related protein families. The paper does not state whether protein-level or homology-level overlap between pre-training and fine-tuning sets was removed. This should be clarified with a decontamination analysis reporting maximum sequence identity and TM-score between test and pre-training proteins.

### Minor

- **Rotation robustness claim is overstated relative to evidence**: The paper claims "rotation-robust" (abstract) and "enforce rotational invariance" (Figure 1c), but the augmentation scheme is limited to discrete 90° rotations and mirror reflections. While the ablation showing that removing fine-tuning augmentations barely hurts (-0.1% R²) suggests the model learns robustness during pre-training, there is no experiment testing performance on continuously rotated inputs. The claim should be tempered, and a continuous-rotation test would verify whether the discrete augmentation generalizes.

- **Figure 2e numerical discrepancy**: The prose (line 480) states "Expanding to ten instead of five views yields a small 0.9% gain," but the figure table in Figure 2e lists "10 vs. 5 predictions: ~1.8%." This inconsistency needs correction.

### Trivial

- **ESM-2 encoder status during pre-training**: The paper should clarify whether the ESM-2 encoders used to generate projection targets during contrastive pre-training were frozen or fine-tuned.

## Nice-to-Haves

- **Discussion of equivariant GNNs** (e.g., SchNet, DimeNet, NequIP) would contextualize the design choice of a non-equivariant CNN with augmentation.

- **Hyperparameter details**: The learning rate search range and final selected values would aid reproducibility.

## Removed Points

These points were raised by reviewers but are not included as weaknesses for the reasons noted:

1. **"Contrastive pre-training to ESM-2 raises a fundamental question about what is learned"** — This misinterprets contrastive learning. The InfoNCE loss aligns embeddings in a shared space while allowing the 3D CNN to learn complementary structural information; it does not force identity mapping. Moreover, the Rosetta regression ablation yields nearly identical performance (-1.0% R²), proving the model's value does not depend on ESM-2 alignment.

2. **"Full-atom is misleading"** — The paper uses the five most common heavy-atom types (C, N, O, S, P), which is standard for "full-atom" in the protein-structure literature where hydrogens are routinely omitted.

3. **"GNNs 'omit atom-level details' is an oversimplification"** — The paper specifically discusses residue-level protein graph networks (GearNet, ESM-GearNet). Equivariant GNNs operate on different scales (small molecules) and are not the standard for protein-level representation.

4. **"Storage concern about 75GB"** — The paper explicitly discusses this storage/GPU trade-off as a limitation (Section 4.3). This is acknowledged, not hidden.

5. **"The optimized pipeline asymmetry is unexplained"** — The paper explicitly explains that the simple pipeline is used for fair comparison and the OP pipeline shows what is achievable with optimization. This is clearly stated.

6. **"Missing related works"** — Cannot be verified from available information. Referenced works exist as cited.

7. **"ESM-2 projections may involve leakage"** — The reviewer speculates about whether ESM-2 encoders were frozen. This is an unknown without further evidence.

8. Various formatting/typo nitpicks — These are parser artifacts, not author errors.

## Novel Insights

The reviews surface one genuinely insightful tension: the paper pre-trains ProteinVista by aligning its embeddings with ESM-2 (a sequence model) via contrastive learning, yet claims the resulting model outperforms ESM-2 by virtue of structural information. While this is not actually contradictory (the 3D CNN processes different input and the contrastive loss only loosely aligns embedding spaces), the paper would benefit from a direct experiment clarifying what structural signal is captured beyond what ESM-2 already encodes — for example, comparing ProteinVista pre-trained with contrastive vs. a purely structural objective (masked voxel prediction). The ablation with Rosetta regression partially addresses this (similar performance), but the conceptual question remains underexplored.

## Suggestions

1. Report all metrics as mean ± std over at least 3 random seeds.
2. Add a contamination analysis showing maximum sequence identity and TM-score overlap between pre-training and test sets.
3. Add at least one structure-aware baseline on the IC50 task (e.g., a 3D CNN trained from scratch, or a published structure-based method on BindingDB).
4. Test rotation robustness explicitly by evaluating on test data rotated by continuous random angles and reporting performance degradation (if any).
5. Correct the Figure 2e numerical discrepancy (0.9% vs 1.8%).

## Score and Decision

**Calibration protocol**:

**Round 1 (bracketing)**: Searched for "3D CNN protein structure prediction" in three score bands.
- Weak band (<3.5): Anchors included GCP-VQVAE (2.00, Reject), SSProNet (2.50, Reject), and a geometrically-contrastive pretraining paper (2.80, Reject). Compared to these, ProteinVista has far stronger evaluation, ablation studies, compute analysis, and clear downstream improvements.
- Middle band (3.5–7.5): Anchors included ProteinAE (5.00, Accept Poster), DynaProt (5.00, Accept Poster), AutoFold (5.20, Reject), and an inverse folding paper (4.00, Reject). ProteinVista is clearly stronger than the 4.00 paper (more tasks, better ablation, clearer problem framing) and comparable to ProteinAE/DynaProt.
- Strong band (>7.5): Anchors were on visual geometry, text-to-3D, and rotation estimation — topically different and much higher-scored. Initial bracket: [4.5, 6.5].

**Round 2 (narrowing)**: Searched for "protein-ligand interaction prediction 3D structure CNN" (4.5–6.5) and "protein structure representation learning downstream tasks" (3.5–5.5).
- SAIR (5.50, Accept Poster): Dataset paper — strong contribution, but methodologically different. ProteinVista is comparable in overall quality.
- Pallatom-Ligand (6.00, Accept Poster): All scores of 6 — generative model with minor weaknesses. ProteinVista has comparable evaluation breadth.
- SLAE (4.00, Reject): Missing baselines, unclear novelty, weaker downstream evaluation. ProteinVista is clearly stronger.
- Local protein environments MLFF paper (5.00, Accept Poster): Good approach, accepted.
- Structure-aligned PLM (4.00, Reject): Weak comparisons and missing baselines.

**Final placement**: ProteinVista is stronger than the rejected SLAE (4.0) and comparable to the accepted ProteinAE (5.0) and DynaProt (5.0). It has broader downstream evaluation than ProteinAE and stronger ablation studies than both. However, the missing error bars, missing contamination analysis, and missing structure-aware IC50 baselines prevent it from reaching the 6.0 level of Pallatom-Ligand, which had cleaner methodology. The paper sits between 5.0 and 6.0, closer to the SAIR (5.5) anchor.

**MY FINAL SCORE**: <score>5.5</score>
**MY FINAL DECISION**: <decision>Accept</decision>