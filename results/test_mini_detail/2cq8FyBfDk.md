Now I have a good set of calibration anchors. Let me write the final review.

## Summary

ProteinVista introduces a full-atom 3D CNN that voxelizes protein structures at 1.0Å resolution across five heavy-atom channels, pre-trained on ~500K AlphaFold2 structures via contrastive alignment with ESM-2 embeddings. On three protein-ligand prediction tasks (transporter-substrate, enzyme-substrate, IC50 regression), it matches or outperforms ESM-2 models 5x its size while requiring ~1% of the pre-training compute. Ensemble with ESM-2 shows complementary signals are partly orthogonal.

## Strengths

- **Compute efficiency is convincingly demonstrated**: ProteinVista (123M params, ~500K pre-training structures, 20s/1K samples) achieves higher accuracy than ESM-2_650M (650M params, 250M pre-training sequences, 426s/1K samples) on TSP (90.8% vs 89.3% accuracy) and substantially higher R² on IC50 regression (0.69 vs 0.61, Section 3.2, Tables 1-2). Pre-training used ~1% of the GPU-hours (48 hrs on 4 A100s vs ~7 days on 128 H100s, Section 4.3). This is a concrete, well-documented advantage.

- **Controlled comparison against ESM-2 ensures fair assessment**: All models were fine-tuned under identical conditions: same prediction head architecture (256 hidden units, batch norm, ReLU), same fixed MolFormer small-molecule embeddings, same hyperparameter search protocol (Section 3.1). This isolates the effect of the protein encoder and is a methodological strength often missing in comparisons.

- **Complementarity analysis is informative and statistically grounded**: The ESM-ProteinVista ensemble improves over either model alone (TSP: 91.5% vs 90.8% / 89.3%; ESP: 93.0% vs 91.8% / 91.9%). McNemar's test yields p<10⁻¹³ (TSP) and p<10⁻¹⁷ (ESP), Section 3.2. Stratification by sequence identity, TM-score, and pLDDT (Figure 2a-c) further characterizes *where* structure adds value — an analysis that goes beyond simple leaderboard reporting.

- **Ablations support key design choices**: The paper compares two pre-training objectives (contrastive vs. Rosetta score regression), showing contrastive yields a modest +1.0% R² advantage (Figure 2e). Inference with 1 vs 5 augmented views costs 6.4% R², confirming multi-view inference is essential. Disabling augmentation during fine-tuning has negligible effect (−0.1%), suggesting robustness is built during pre-training (Section 4.2). Voxel resolution ablation (1.0Å vs 1.5Å, −1.1% R²) validates the atom-resolution design.

- **Honest limitation reporting**: The paper explicitly tests on GO prediction and shows ProteinVista underperforms ESM-2 (Fmax 0.57 vs 0.62, Section 3.4), discusses the single-snapshot limitation (Section 5), and acknowledges the storage overhead (75GB vs 3MB for the TSP dataset, Section 4.3).

## Weaknesses

### Major

- **No controlled comparison against structure-aware models (GearNet, equivariant nets, etc.)**: The paper's narrative positions ProteinVista as superior to *all* protein transformers for structure-dependent tasks and argues that residue-level GNNs like GearNet omit atom-level details (Introduction, lines 23-28). Yet the experiments compare only against *sequence* transformers (ESM-2). Missing baselines include GearNet, ESM-GearNet, or any equivariant architecture on the same benchmarks under identical conditions. Without this, the reader cannot distinguish whether gains come from *any* explicit 3D representation or from the specific atomic-resolution volumetric CNN. The claim that "full-atom 3D CNNs are both tractable and superior" is incompletely supported. The paper acknowledges GearNet/ESM-GearNet in the introduction but never benchmarks against them.

### Minor

- **Rotation robustness is tested only on a discrete 90° set**: Training augmentations are limited to 90° rotations and mirroring around Cartesian axes (Section 2.4). This yields at most 24 orientations. The paper does not evaluate performance under arbitrary continuous rotations. While the language is appropriately cautious ("rotation-robust" not "rotation-invariant"), the practical claim that the model "learns rotation-robust representations" (Abstract) is only validated on this discrete subset.

- **SOTA comparison (OP pipeline) lacks methodological rigor**: The optimized pipeline (ESM-ProteinVista_OP) is compared against published numbers from SPOT, ProSmith-ESP, and Fusion_ESP (Table 1) without specifying whether those baselines used the same data splits, training protocols, or were re-run at all. The paper also does not report what ESM-2_650M alone achieves with the same OP pipeline, making it impossible to isolate the structure encoder's contribution in the optimized setting.

- **Contrastive pretraining with ESM-2 partially confounds signal source**: Training ProteinVista to align with ESM-2 embeddings means the structure encoder is explicitly taught to reproduce sequence-derived representations. The Rosetta-score pretraining ablation (+1.0% vs contrastive) partially addresses this concern by showing a purely structural objective also works well, but it is not a self-supervised structural task (e.g., masked voxel reconstruction) that would fully isolate independent structure learning.

### Trivial

- **Abstract slightly overstates**: "Outperforms sequence transformers on three benchmarks" — on the ESP task ProteinVista matches ESM-2_650M (91.8% vs 91.9% accuracy, Table 1), it does not clearly outperform on this benchmark.
- **Gaussian density formula**: The formula reads `exp(-∥v - r∥/σ²)` (line 61); if this is intended as a Gaussian kernel, the numerator should be squared (`∥v - r∥²`). This may be a parser artifact but should be checked.

## Nice-to-Haves

- Comparison to a structure-aware GNN (e.g., GearNet) on the same benchmarks using the same prediction head would strengthen the claim that atom-level 3D CNNs add value beyond residue-level graph methods.
- Testing performance under arbitrary continuous rotations (e.g., random Euler angles) would clarify the practical limits of the augmentation strategy.
- A purely structural self-supervised pre-training baseline (e.g., masked voxel reconstruction) would better isolate whether the learned representations are genuinely structural or inherited from the ESM-2 alignment.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a controlled comparison against GearNet (or ESM-GearNet) on the TSP/ESP/IC50 benchmarks using the same prediction head and training protocol. This directly addresses the main concern about structural baseline comparisons.
2. Report performance of the OP pipeline on ESM-2_650M alone alongside the ProteinVista results to isolate the structure encoder's contribution in the optimized setting.
3. Test robustness under arbitrary continuous rotations (not just 90° increments) and report degradation if any.
4. Qualify the "outperforms" claim in the abstract for the ESP task where the result is effectively tied.

---

## Score and Decision

I bracketed the paper by comparing against human-reviewed anchors. **Round 1 (bracketing)**: Weak anchors <3.5 (ProteinAdapter ~3.4, CrysFormer ~3.75) — ProteinVista is clearly stronger due to cleaner experiments and compute analysis. Middle anchors 3.5-7.5 (Pocket Pretraining 6.0, AtomSurf 6.75) — ProteinVista is somewhat weaker than AtomSurf (which has thorough structural baselines) but comparable to Pocket Pretraining (similar contribution level). Strong anchors >7.5 (SaProt 7.33, ProtComposer 8.0) — ProteinVista is not at this level; these papers have much more extensive evaluation.

**Round 2 (narrowing)**: Inside bracket 4.5-6.5: Distilling Structural Representations (5.0) — ProteinVista has clearer contributions and better compute analysis, placing it higher. PPBind (4.6) — missing baselines make it clearly weaker. Inside bracket 6.0-7.5: AtomSurf (6.75) has more thorough structural baselines. Pocket Pretraining (6.0) has comparable novelty.

ProteinVista sits between the ~5.0 of Distilling Structural Representations (which had marginal gains and unclear contributions) and the ~6.0 of Pocket Pretraining (solid results with a novel data pipeline). The missing structural baselines pull it down from the 6.0+ range, but the compute efficiency story, controlled comparison against ESM-2, and informative stratification analysis are genuine strengths that lift it above the reject-level papers.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>