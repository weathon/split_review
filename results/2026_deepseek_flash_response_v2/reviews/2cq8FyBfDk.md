Now I have all the information I need to produce the final review. Let me write it.

## Summary

ProteinVista introduces a 3D CNN that operates on voxelized full-atom protein structures at 1.0Å resolution, pretrained on ~500K AlphaFold-2 structures via contrastive alignment to ESM-2 embeddings. It is evaluated on protein-ligand interaction tasks (transporter-substrate prediction, enzyme-substrate prediction, IC50 regression) and GO annotation. Key results show ProteinVista outperforms ESM-2_650M on IC50 regression (R²=0.69 vs 0.61) and TSP (90.8% vs 89.3% accuracy), while the ensemble with ESM-2 yields further improvements on classification tasks, all with substantially fewer parameters and pretraining data.

## Strengths

1. **Competitive performance on structure-sensitive tasks with a fraction of the parameters and pretraining data of ESM-2.** On IC50 regression (Table 2), ProteinVista (123M params, ~500K AF2 structures) achieves R²=0.69 vs ESM-2_650M's 0.61 (650M params, ~250M sequences). On TSP (Table 1), it reaches 90.8% vs 89.3%. The Wilcoxon signed-rank test gives p < 10⁻³⁰⁴ for IC50 (Section 3.2), confirming the gap is significant. This directly validates the claim that full-atom 3D CNNs are tractable and informative for structure-dependent tasks.

2. **Sequence and structure signals are quantitatively shown to be complementary.** The ESM-ProteinVista ensemble exceeds either model alone on TSP (91.5% vs 89.3%) and ESP (93.0% vs 91.9%) (Table 1). McNemar's tests confirm significance (p < 10⁻¹³, p < 10⁻¹⁷). The stratification by sequence identity and TM-score (Figure 2a-b) characterizes *when* each modality contributes, showing ProteinVista excels on high-similarity test examples while ESM-2 performs better on low-similarity cases — a nuanced finding that strengthens the complementarity claim.

3. **Dramatic practical compute savings demonstrated quantitatively.** ProteinVista processes 1,000 proteins on an A100 in 20 seconds vs 426 seconds for ESM-2_650M (Figure 3c). Pretraining used ~1% of the GPU-hours: 48 hours on 4 A100s vs ~7 days on 128 H100s (Section 4.3). These numbers make a concrete case for practical deployability.

4. **Honest characterization of failure modes and boundary conditions.** The GO term prediction experiment (Section 3.4) shows ProteinVista (Fmax=0.57) trails ESM-2_650M (0.62), and the paper explicitly acknowledges where structure encoders add limited value. The stratification by pLDDT (Figure 2c) further establishes how performance degrades on low-confidence predicted structures — setting clear boundary conditions rather than hiding weaknesses.

5. **Continuous Gaussian density voxelization with adaptive boxing is a well-motivated design.** Instead of one-hot voxel encoding, atoms contribute continuous density (exp(-‖v⃗−r⃗‖/σ²)), preserving sub-voxel geometry. Adaptive boxing (four sizes from 64³ to 160³) minimizes empty voxels for smaller proteins. The ablation (Section 4.2) shows even 1.5Å resolution drops R² by only 1.1%, indicating robustness.

## Weaknesses

### Fatal

None.

### Major

1. **The best-performing variant's pretraining uses cross-modal alignment to the very model it is compared against.** ProteinVista is pretrained via contrastive alignment to ESM-2 embeddings (Section 2.3): the structure encoder is trained to produce embeddings similar to what ESM-2 would produce from the sequence. The paper's primary results, released weights, and abstract's strongest claim ("outperforms sequence transformers") all rest on this ESM-guided variant. While the ablation (Section 4.2) shows that replacing the contrastive objective with Rosetta-score regression decreases R² by only 1.0% (relative), meaning an independently-trained structure model would still be competitive, the paper presents the ESM-aligned model as the main result. A reader evaluating "ProteinVista outperforms ESM-2" is not comparing an independent structure model to a sequence model; the structure model was taught by ESM-2 during pretraining. The Rosetta-pretrained variant should be reported alongside the contrastive variant in the main tables to clarify what the independent structure model achieves.

2. **No comparison against residue-level graph methods that the paper motivates against.** The introduction motivates ProteinVista by arguing that GearNet, ESM-GearNet, and GPS-Fun "omit atom-level details" and "treat proteins as topological networks with no direct mapping to 3D space" (Section 1). Yet none of these methods appear in any experimental comparison — the baselines are exclusively sequence-only ESM-2 and task-specific methods (SPOT, ProSmith-ESP, Fusion_ESP). Without comparing against a residue-level graph method on the same benchmarks, the paper cannot support its claim that moving from residue-level graphs to full-atom voxel grids is what drives performance. The gains over ESM-2 could plausibly come from using *any* structural signal, not from atom-level detail specifically.

3. **The "outperforms" claim is not supported on all three benchmarks.** The abstract states ProteinVista "outperforms sequence transformers on three benchmarks." On the enzyme-substrate prediction (ESP) task, ProteinVista achieves 91.8% accuracy — essentially tying with ESM-2_650M's 91.9% (Table 1). The outperformance claim is accurate for IC50 regression (R²=0.69 vs 0.61) and TSP (90.8% vs 89.3%), but not for ESP. This overreach weakens the paper's central claim.

### Minor

1. **Unclear whether ESM-2 is frozen or fine-tuned during contrastive pretraining.** Section 2.3 states that "a similar projection head maps the ESM-2 embedding to z^(ESM)" but does not specify whether the ESM-2 backbone weights are frozen or updated during this stage. This matters for reproducibility and for interpreting how much of the downstream performance comes from the structure encoder vs. from adapting ESM-2's representations.

2. **ESM-2 embedding aggregation method for downstream tasks is unspecified.** ESM-2 produces per-token embeddings, while ProteinVista produces a single global vector via global average pooling. The paper does not specify how ESM-2's per-token embeddings are pooled (e.g., averaging, [CLS] token, or other) into a protein-level representation for the simple prediction head. If the pooling methods differ in quality, this asymmetry could systematically favor one model.

3. **Rotation augmentation uses only discrete 90° rotations, not continuous rotations.** The paper acknowledges this, but the ablation (Section 4.2) shows that reducing from 5 to 1 random view at inference drops R² by 6.4% — confirming the model is not truly invariant and relies on ensembling over a discrete set. A 45° rotation would produce a substantially different voxelization not covered by the augmentation.

4. **The 20× runtime speedup over ESM-2_650M is not adequately explained relative to the raw FLOPs gap.** ProteinVista requires 415 GFLOPs vs ESM-2_650M's 520 GFLOPs (a ~25% difference), yet processes 1,000 proteins in 20 seconds vs 426 seconds (~20× faster). The paper attributes this to better parallelization of shallow CNNs over deep transformer stacks, but the extreme discrepancy (25% vs 2000%) suggests implementation-level factors (batch sizes, CUDA kernel efficiency, memory bandwidth) are the primary drivers rather than any fundamental algorithmic property. The reader cannot assess how much of this advantage would transfer to other settings.

5. **No "no pretraining" baseline.** The ablation compares two pretraining objectives (contrastive vs. Rosetta), but neither experiment trains ProteinVista from scratch without any pretraining. This would help separate the benefit of the architecture from the benefit of large-scale pretraining.

6. **Test set sizes are deferred to the appendix.** The main text refers to Table S3 for dataset details but does not state how many proteins/ligand pairs are in each test set. Without this information in the main text, the reader cannot gauge the reliability of the reported metrics.

### Trivial

None.

## Nice-to-Haves

- Compare against at least one residue-level graph method (e.g., GearNet) on one shared benchmark to directly test whether atom-level detail drives improvement over residue-level structure.
- Report the Rosetta-pretrained variant's performance alongside the contrastive variant in the main results tables so readers can directly see what the independent structure model achieves.
- Clarify the ESM-2 pooling strategy and whether ESM-2 is frozen during pretraining.
- Add a no-pretraining baseline for ProteinVista to separate architecture benefits from pretraining benefits.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"First" claim in introduction.** The critic objected to the phrase "first compute-efficient full-atom 3D CNN pretrained on large-scale AF2 structures." Previous 3D CNNs for proteins (DeepSite, EnzyNet, 3DCNN_MQA) were neither pretrained at scale nor full-atom. The claim is specific enough to be defensible; removed as not a substantive weakness.
- **Astronomical p-values.** The critic objected to p < 10⁻³⁰⁴ as suspicious. With large test sets, such extreme values are expected for real effects. The paper also reports effect sizes. Removed as not a meaningful weakness.
- **Storage cost "dismissed too quickly."** The paper explicitly acknowledges the storage trade-off in Figure 3d. The paper's scope defines compute efficiency as the main focus. Removed as scope creep.
- **Parallelizability explanation insufficient (overstated version).** The core concern (runtime vs FLOPs discrepancy) is kept as Minor #4 above, but the stronger claim that the paper's explanation is invalid is weakened — architectural differences in parallelism can produce large runtime gaps at similar FLOP counts.
- **Criticism about whether 45° rotations would produce different voxelizations.** This is subsumed into Minor #3 (discrete rotation limitation), which already captures the substantive concern.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the pretraining story.** Present the Rosetta-pretrained variant's performance alongside the contrastive variant in the main results, and reframe the abstract to accurately reflect that the best variant uses cross-modal alignment to ESM-2, not purely structure-based pretraining. This would resolve the tension between the claimed "structure model outperforms sequence model" framing and the actual experimental design.

2. **Add at least one comparison against a residue-level graph method** (e.g., GearNet or ESM-GearNet) on a shared benchmark to directly test whether atom-level detail is the source of improvement over residue-level structure representations.

3. **Tone down the "outperforms" claim** for the ESP benchmark where ProteinVista ties with ESM-2, and qualify the claim as task-dependent.

4. **Specify the ESM-2 pooling strategy** and whether ESM-2 is frozen during pretraining in Section 2.3.

5. **Include test set sizes** in the main text rather than deferring entirely to the appendix table.

## Calibration Anchors

### Round 1 — Bracketing (score ranges from retrieved anchors)
- **Weak band (< 3.5):** 4 papers at 3.0 (rejected — molecular docking benchmark, ligand conformation generation). ProteinVista is clearly stronger.
- **Middle band (3.5–7.5):** EquiPocket (5.50, rejected — binding site prediction with missing baselines), GroupBind (6.75, accepted — novel docking framework), "Deep Learning for Protein-Ligand Docking" (4.38, rejected — benchmark paper), "Enhancing PPB Affinity" (4.60, rejected).
- **Strong band (> 7.5):** 4 papers at 8.0 (accepted — protein backbone/structure generation). These are different types of contributions (generative models).

**Initial bracket:** 5.0–7.0

### Round 2 — Narrowing
- **ProteinINR** (5.75, accepted — multi-modal pretraining, marginal improvements): Similar pretraining+finetuning paradigm to ProteinVista. Weaker performance gains but cleaner comparison setup. ProteinVista is slightly stronger in scope and practical contributions.
- **ProteinWorkshop** (6.25, accepted — benchmark suite): Different contribution type (benchmark vs. method). Not directly comparable.
- **PPIformer** (5.80, accepted — PPI pretraining, scores 6,8,6,6,3): Comparable scope and rigor. Similar strengths (pretraining dataset, novel architecture) and weaknesses (generalization concerns).
- **AtomSurf** (6.75, accepted — surface representation learning): Stronger SOTA claims on established benchmark. More rigorous evaluation protocol. ProteinVista is somewhat weaker in execution clarity.
- **BindNet** (5.67, accepted — protein-ligand representation learning): Comparable in scope and contribution level, with similar concerns about missing baselines.

**Final score:** 6.0. ProteinVista has genuine novelty (3D CNN at full-atom scale with practical compute efficiency), a well-designed evaluation that honestly characterizes failure modes, and clear practical value. However, the pretraining confound and overstated framing prevent it from reaching the level of the 6.75–7.0 anchors. It sits slightly above ProteinINR (5.75) and PPIformer (5.80) due to its more substantial performance gaps and practical compute analysis, but its framing issues are more central than those papers' weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>