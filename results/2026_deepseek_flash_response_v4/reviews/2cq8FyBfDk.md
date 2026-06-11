Now let me write the final consolidated review.

## Summary

ProteinVista introduces a 3D CNN that voxelizes protein structures at 1.0 Å resolution into a 5-channel grid (C, N, O, S, P heavy atoms), pre-trained via contrastive alignment to ESM-2 embeddings on ~500K AlphaFold-2 predicted structures. Fine-tuned on protein-ligand prediction tasks, ProteinVista (123M parameters) matches or exceeds ESM-2 (150M/650M) on enzyme-substrate classification, transporter-substrate classification, and drug-target IC50 regression while using ~1% of the pre-training GPU-hours and ~500× less pre-training data. An ensemble with ESM-2 further improves accuracy on classification tasks, demonstrating complementary signals between sequence and structure.

## Strengths

1. **Demonstrated complementarity between 3D structure and sequence via rigorous statistical tests**: Ensemble predictions from ProteinVista + ESM-2 consistently outperform either model alone across multiple benchmarks (Table 1: TSP Acc 91.5% vs 89.3% and 90.8%; ESP Acc 93.0% vs 91.9% and 91.8%). McNemar's tests confirm significance (p < 10^−13 for TSP, p < 10^−17 for ESP). The stratified analysis (Figure 2a–b) further shows the ensemble outperforms both single models across all bins of sequence identity and structural similarity.

2. **Dramatic compute and data efficiency with competitive or superior task performance**: ProteinVista matches or exceeds ESM-2_{650M} on three structure-dependent benchmarks while using ~1% of the GPU-hours for pre-training (48 hours on 4 A100s vs. ~7 days on 128 H100s), ~500× less pre-training data (~0.5M vs. ~250M sequences), and 5× fewer parameters (123M vs. 650M). On IC50 regression (Table 2), ProteinVista achieves R²=0.69 vs. ESM-2_{650M}'s 0.61.

3. **Systematic ablation study**: Section 4.2 quantifies the contribution of each design component on IC50 prediction. Reducing from 5 to 1 augmented inference views drops R² by 6.4%; contrastive vs. Rosetta pre-training changes R² by only 1.0%; 1.5Å vs. 1.0Å voxel resolution reduces R² by 1.1%. These controlled perturbations allow readers to assess which design decisions are critical vs. incidental.

4. **Honest reporting of failure modes**: In Section 3.4, the authors test ProteinVista on GO molecular function annotation, where it underperforms ESM-2_{650M} (Fmax 0.57 vs. 0.62). Reporting this clear negative result strengthens credibility and helps delineate the scope where the method is beneficial.

5. **Stratified analysis by pLDDT confidence**: Section 4.1 and Figure 2c show ProteinVista's advantage is largest for high-confidence structures (pLDDT > 90) and drops to parity for low-confidence structures, providing practical guidance on when predicted vs. experimental structures are needed.

## Weaknesses

### Fatal

None.

### Major

1. **Missing no-pretraining baseline for the 3D CNN**: The contrastive pre-training explicitly aligns ProteinVista's embeddings with ESM-2 sequence embeddings (Section 2.3). This creates a confound: is the downstream performance driven by the 3D CNN's structural processing, or by inheriting ESM-2-like representations through the pre-training alignment? The ablation comparing contrastive vs. Rosetta-regression pre-training (1.0% R² difference) only swaps one pre-training objective for another — it does not include a randomly initialized 3D CNN fine-tuned from scratch. Without this baseline, the reader cannot assess how much of the gain comes from pre-training vs. the architecture itself. This is a standard control in representation learning papers.

2. **No direct comparison against graph-based structure encoders**: The introduction motivates the approach by arguing that graph-based methods like GearNet and ESM-GearNet "omit atom-level details and therefore struggle to encode the detailed chemistry of binding sites" (lines 15–19). Yet the experiments compare ProteinVista against ESM-2 (sequence-only) and against specialized downstream methods (SPOT, ProSmith-ESP, Fusion_ESP) that use different pipelines. There is no experiment where ProteinVista and any graph-based structure encoder are evaluated under identical conditions (same downstream head, same training protocol). While the paper's headline claim targets sequence transformers, the motivation for why atom-level detail matters is framed against graph-based methods, making this omission significant.

### Minor

3. **No variance or confidence intervals alongside main results**: Tables 1 and 2 report point estimates only. Given that the performance differences between ProteinVista and ESM-2 are modest on classification tasks (e.g., 90.8% vs. 89.3% on TSP, effectively tied on ESP at 91.8%), it is unclear whether these gaps are outside the noise range of a single training run. Reporting standard deviations across multiple seeds would strengthen confidence.

4. **Imprecise language on rotation invariance**: The paper states "rotation-invariant predictions" (line 31) and "enforce rotational invariance" (Figure 1 caption), but the augmentation is limited to 90° rotations and mirror flips, producing at most 24 discrete orientations from the cube's symmetry group. This provides robustness to cubic-group rotations, not continuous rotation invariance. The language should match what the system actually delivers.

### Trivial

5. **Extreme p-value for IC50 comparison**: The paper reports p < 10^{-304} (line 119). While the qualitative finding is robust, reporting a p-value at the limits of floating-point precision is unconventional. Standard practice would report p < 10^{-16} or a similarly bounded value.

6. **Dataset statistics deferred to appendix**: Per-task dataset sizes, splits, and class balance are referenced only in Table S3 (removed by the parser). A brief summary in the main text would improve self-contained readability.

## Removed Points

These points were raised in reviews but are not included as weaknesses in the main review; they are flagged here for completeness and should be treated with caution.

- **"Atom-level framing is overstated" (Harsh Critic, point 3)**: The paper encodes 5 heavy-atom types at 1.0Å resolution with Gaussian smearing (σ=1Å). This is standard practice in structural biology for atom-level encoding; the smearing avoids discretization artifacts and preserves sub-voxel positional information. The framing is appropriate for the field.
- **"Rotation augmentation analysis raises concerns about learned invariance" (Harsh Critic, point 4)**: The reviewer's alternative interpretation (model is "insensitive" rather than "robust" to rotations) is speculative. The ablation showing 0.1% change when dropping augmentation during fine-tuning is consistent with the paper's interpretation (model learns stable representations during pre-training). The 24-discrete-orientation scheme is standard for 3D CNNs and provides meaningful robustness.
- **"Complementarity claim contradicted by IC50 ensemble"**: The paper directly addresses this (lines 119–125), explicitly noting that fine-grained affinity prediction leaves little room for sequence information to contribute. The paper discusses this nuance.
- **"SOTA comparison uses an optimized pipeline, creating unfair comparison"**: The paper is fully transparent about this (lines 137–142), clearly labeling the optimized pipeline (OP) and distinguishing it from the controlled comparison.
- **Strength Finder claim that "problem is important"**: Generic claim, not specific to this paper's technical contributions.

## Novel Insights

None beyond the paper's own contributions. The key observation — that a 3D CNN at 1.0Å voxel resolution with contrastive pre-training can match or exceed sequence models on structure-sensitive tasks while being orders of magnitude more efficient — is well-articulated by the paper itself.

## Suggestions

1. Add a no-pretraining baseline (randomly initialized 3D CNN fine-tuned from scratch) to disentangle architectural from pre-training contributions.
2. Include a comparison against at least one graph-based structure encoder (e.g., GearNet or ESM-GearNet) under the same controlled pipeline.
3. Report results across multiple random seeds with standard deviations, especially for classification benchmarks where margins are small.
4. Tighten language from "rotation-invariant" to "rotation-robust" to match the discrete augmentation scheme.
5. Replace p < 10^{-304} with a conventionally bounded p-value.
6. Include a brief summary of dataset statistics in the main text.

## Score and Decision

**Calibration evidence:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| 3D Molecular Pretraining via LEGO | rEQ8OiBxbZ.md | 3.00 | 1 (low) | Much weaker methodology, no protein-specific contribution |
| ProteiNexus | iBAWiEjogY.md | 3.67 | 1 (low) | Had data leakage and missing baselines; ProteinVista is clearly stronger |
| RNA Contrastive Learning | wRkfniZIBl.md | 4.33 | 1 (mid) | Different domain (RNA); less relevant comparison |
| EquiPocket | umUIYdLtvh.md | 5.50 | 2 (mid) | E(3)-equivariant GNN for binding sites; rejected due to missing SOTA comparisons; ProteinVista has cleaner experiments |
| Protein-ligand binding rep learning | AXbN2qMNiW.md | 5.67 | 2 (mid) | Self-supervised binding learning; had data leakage and missing ESM-2 baseline; ProteinVista is methodologically cleaner |
| Pre-training Seq/Struct/Surface | BEH4mGo7zP.md | 5.75 | 2 (mid) | Multi-modal pre-training with surface modality; comparable rigor, different approach |
| ProteinWorkshop benchmark | sTYuRVrdK3.md | 6.25 | 2 (mid) | Benchmark paper, different contribution type |
| GroupBind docking | zDC3iCBxJb.md | 6.75 | 2 (mid) | Docking-specific, not directly comparable |
| FoldFlow / ProtComposer | Various | 8.00 | 1 (high) | Protein generation papers; ProteinVista is clearly below this tier |

**Round 1 bracket:** 4.5 – 6.5  
**Round 2 narrowing:** Anchors at 5.50–6.25; ProteinVista is stronger than EquiPocket (5.50, Reject) and comparable to or slightly stronger than the accepted papers at 5.67–5.75.  
**Final score:** 6.0 — a solid Accept. The paper makes a genuine contribution (demonstrating that 3D CNNs at scale are compute-efficient and competitive with sequence models on structure-sensitive tasks) with a clean experimental design and honest reporting. The two missing baselines (no-pretraining, graph comparison) are significant but fixable gaps, not fatal flaws.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>