## Summary

ProteinVista introduces a full-atom 3D CNN that voxelizes protein heavy atoms at 1.0 Å resolution, uses adaptive boxing (64³–160³ voxels) to handle variable protein sizes, and is pre-trained on ~500K AlphaFold-2 structures. On three protein–ligand interaction benchmarks (enzyme-substrate, transporter-substrate, and IC50 regression), it matches or outperforms ESM-2_650M despite having 5× fewer parameters (123M vs. 650M) and orders of magnitude less pre-training data. An ensemble with ESM-2 further improves classification accuracy, confirming complementarity between sequence and structure signals. The model also demonstrates a large practical speed advantage (~20s vs. ~426s per 1K proteins on an A100).

## Strengths

- **Strong downstream results with statistical rigor.** On IC50 regression, ProteinVista achieves R²=0.69 vs. ESM-2_650M's 0.61 (Wilcoxon p<10⁻³⁰⁴). On transporter-substrate prediction, it reaches MCC=0.77 vs. 0.74 (McNemar p<10⁻¹³). These aren't marginal gains; they are large, statistically significant improvements on biologically meaningful tasks.

- **IC50 result is the paper's strongest evidence for structure-dominance.** ProteinVista alone (R²=0.69) outperforms the ESM–ProteinVista ensemble (R²=0.68), demonstrating that for binding affinity, the structural encoder captures essentially all the relevant signal and the sequence encoder adds no residual value. This directly supports the claim that atom-level 3D geometry matters for tasks requiring precise pocket geometry.

- **Compute efficiency is genuinely impressive.** Pre-training on 4 A100s for 48 hours vs. ESM-2_650M's ~7 days on 128 H100s (~1% of GPU-hours). Inference speed of 20s per 1K proteins vs. 426s for ESM-2_650M. These comparisons are meaningful even with caveats about benchmarking methodology.

- **Comprehensive ablations.** The paper isolates the contribution of key design choices: contrastive vs. Rosetta pre-training (+1.0% R²), 5 vs. 1 views (+6.4%), 1.0 Å vs. 1.5 Å resolution (+1.1%), and training data augmentation (~0% effect). These controlled experiments validate the architecture's design.

- **Stratified analysis provides honest characterization.** The breakdown by sequence identity, TM-score, and pLDDT shows when structure helps (high similarity, high confidence) and when it doesn't, giving readers a clear picture of the method's适用范围.

- **Practical architectural contributions.** The adaptive boxing scheme (64³–160³) and continuous-density voxelization (Gaussian rather than one-hot) are well-motivated design decisions that make full-atom 3D CNNs tractable.

## Weaknesses

### Major

- **Contrastive pre-training with ESM-2 muddies the headline comparisons.** ProteinVista is pre-trained to align its embeddings with ESM-2 via an InfoNCE loss (Section 2.3), and all main-table results (Tables 1, 2) use these contrastively pre-trained weights. Comparing this model against ESM-2 and claiming "outperforms sequence transformers" conflates the structure encoder's contribution with information absorbed from ESM-2 during pre-training. The Rosetta-only ablation (Figure 2e) shows only a ~1% R² drop, which partially mitigates the concern, but this ablation is relegated to a small panel rather than presented as a primary baseline. The paper would be substantially cleaner if the Rosetta-only variant appeared as a main-table row alongside the contrastive variant, so readers can see structure-only performance directly.

### Minor

- **Inference speedup vs. FLOPs is under-documented.** ProteinVista requires 415 GFLOPs vs. ESM-2_650M's 520 GFLOPs (~25% less), yet runs 21× faster (20s vs. 426s per 1K proteins). The paper attributes this to better parallelization of shallow 3D CNNs vs. deep transformers, which is plausible, but the exact benchmarking conditions (batch size, precision, input-size distribution, whether ESM-2 was run with or without mixed precision, kernel compilation settings) are not reported. A detailed methodology table would allow others to reproduce and trust this claim.

- **SOTA comparison pipeline lacks a controlled ESM-2 variant.** In Table 1, the ESM-ProteinVista_OP pipeline involves joint fine-tuning of MolFormer plus a contrastive classifier, and outperforms SPOT/ProSmith-ESP/Fusion_ESP. But there is no ESM-2_OP row showing what the same optimized pipeline achieves with ESM-2 alone. This makes it impossible to isolate whether the improvement comes from ProteinVista's encoder or from the more elaborate pipeline. The paper's transparency about the pipeline helps, but the missing control weakens the attribution.

- **GO term prediction significance is not assessed.** ProteinVista's F_max=0.57 vs. ESM-2's 0.62 is reported as a negative result ("structure encoders add limited value"), but no confidence intervals or significance test are provided. The gap may be real, but it could also be within noise; reporting this honestly would strengthen the paper.

- **No explicit limitations section.** The Discussion mentions the single-snapshot limitation but does not explicitly list: (a) reliance on AlphaFold-2 predicted structures, (b) contrastive pre-training dependence on ESM-2, (c) the storage cost of 3D inputs (~75 GB for 5.8K proteins), and (d) that the model processes a static conformation only.

### Trivial

- The caption for Figure 3c describes it as "Inference Time" but the text describes the same numbers as "during training" — this should be clarified.

- Figure 2e's ablation values in the text (1.0% for Rosetta vs. CL) differ slightly from the figure values (~1.2%); these should be consistent.

## Nice-to-Haves

- An occupancy-fraction histogram showing how empty the voxel grids are across the training set. The paper motivates 3D CNNs by noting atomic sparsity but never quantifies it.
- A discussion of on-the-fly voxelization from PDB files as a way to avoid the ~75 GB storage cost, which the paper honestly reports.
- An ablation comparing the adaptive boxing scheme against a fixed 160³ grid for all proteins, to quantify the memory/compute savings.

## Removed Points

The following points were removed from the harsh critic's report as they do not constitute valid weaknesses:

- **"Missing comparison to GearNet/ESM-GearNet/GPS-Fun"** — These methods were evaluated on different benchmarks (GO term prediction, fold classification) and the paper already discusses them in the Introduction. The binding tasks in ProteinVista are not the standard evaluation benchmarks for those methods, and the paper does compare on GO term prediction where ProteinVista underperforms. Adding these baselines is outside the paper's stated scope.
- **"IC50 dataset construction details not provided"** — The paper references Table S3 (in the appendix) for dataset details. The appendix was stripped by the parser, so this criticism cannot be verified from the available text.
- **"Voxel sparsity analysis"** — This is a nice-to-have analysis, not a weakness. The paper's adaptive boxing already addresses the sparsity concern.
- **"Storage requirement (75 GB) is a practical obstacle"** — The paper already acknowledges this trade-off explicitly. The critic's suggestion (on-the-fly voxelization) is a reasonable future direction but not a flaw in the presented work.
- **"Missing related works"** — The paper adequately cites relevant prior work. The critic's suggestions are not verifiable as missing works I can confirm exist.

## Novel Insights

None beyond the paper's own contributions. The key insight — that a well-designed 3D CNN operating on full-atom voxel grids can match or exceed large protein language models on structure-sensitive tasks while using far less compute — is the paper's original contribution, not something that emerges from the reviews.

## Suggestions

1. **Present the Rosetta-only pre-trained variant as a co-primary model.** Add a row to Tables 1 and 2 for "ProteinVista (Rosetta pretraining)" so readers can directly compare structure-only performance against ESM-2. This single change would address the most serious weakness without requiring new experiments (the data already exists in the ablation).

2. **Provide a detailed benchmarking methodology table for the speed comparison.** Report batch size, precision (FP16/FP32/bf16), input-size distribution for the 1K proteins, and whether any kernel-level optimizations were applied to either model. This would make the 21× speedup claim verifiable.

3. **Add an ESM-2_OP row to Table 1** applying the same optimized pipeline (joint fine-tuning of MolFormer + contrastive classifier) to ESM-2_650M, to isolate ProteinVista's contribution from the pipeline improvement.

4. **Move the limitations discussion to a dedicated section** and explicitly list: reliance on predicted structures, ESM-2 dependency in contrastive pretraining, storage cost, and single-conformation limitation.

## Score and Decision

**Calibration summary:**

| Round | Anchor ID | Avg Score | Comparison |
|-------|-----------|-----------|------------|
| R1 | 1EGfgGkHFY (MotifScreen) | 2.50 | Weaker — flawed validation; ProteinVista's evaluation is much more rigorous |
| R1 | DuWU9aflmc (SSProNet) | 2.50 | Weaker — limited secondary structure contribution vs. ProteinVista's full-atom approach |
| R1 | vbc5JyzNE0 (Geometric SSL) | 2.80 | Weaker — narrow graph-based pretraining vs. ProteinVista's comprehensive benchmark suite |
| R1 | tYLCkzHAM2 (ProteinAE) | 5.00 | Similar — both structure encoders with solid results, but ProteinVista has stronger downstream validation |
| R1 | EgPqKZHfVY (SLAE) | 4.00 | Weaker — rejected for missing baselines; ProteinVista's baseline selection is more complete |
| R1 | rQePuOpesU (AutoFold) | 5.20 | Similar topic (protein structure) but different task (generation vs. representation) |
| R2 | qgk2F6jxH4 (SAIR) | 5.50 | Weaker — dataset contribution with modest modeling results; ProteinVista has stronger algorithmic novelty |
| R2 | 9ZogcRkhoG (MLFF local env) | 5.00 | Similar — repurposing embeddings for protein tasks, but ProteinVista's architecture is more end-to-end |
| R2 | kIxAQxUZHq (Bento) | 5.00 | Weaker — benchmarking study, not a new method |
| R2 | 55e5f3GVFc (GeoBPE) | 7.50 | Different topic (structure tokenization); higher score reflects cleaner methodology without the contrastive pre-training concern |

**Round 1 bracket:** [4.5, 7.5] — clearly above reject-level papers (2.5–3.3) and below the top-tier papers on different problems.

**Round 2 narrowing:** The paper is stronger than the 5.0–5.5 anchors (SAIR, ProteinAE, MLFF) due to its combination of architectural novelty, strong downstream results with statistical tests, compute efficiency analysis, and thorough ablations. However, the contrastive pre-training concern prevents it from reaching the 6.5+ band where papers have cleaner methodology. The paper sits near the top of the 5.0–6.0 range.

**Final score: 6.0**

The paper makes a clear and practically valuable contribution: it demonstrates that a well-designed full-atom 3D CNN, pre-trained on modest data, can compete with and complement much larger protein language models on structure-sensitive tasks. The major weakness (contrastive pre-training conflating the comparison) is real but addressable, and largely mitigated by the existing Rosetta ablation. With the suggested presentation changes, this would be a strong paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>