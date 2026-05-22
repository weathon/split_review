Now I have all the information I need. Let me write the final consolidated review.

## Summary

ProteinVista introduces a full-atom 3D CNN that voxelizes protein structures at 1.0 Å resolution and is pre-trained on ~500K AlphaFold2 structures via contrastive alignment with ESM-2 embeddings. Despite having only 123M parameters and using >200× less pre-training data than large PLMs, it matches or outperforms ESM-2 variants on transporter-substrate classification, enzyme-substrate classification, and drug-target IC₅₀ regression (R² 0.69 vs. ESM-2₆₅₀ₘ's 0.61). A simple ensemble with ESM-2 further boosts accuracy on classification tasks, demonstrating complementary signals between structure and sequence.

## Strengths

1. **Substantial empirical advantage on structure-sensitive tasks with far fewer resources**: On IC₅₀ regression (Table 2), ProteinVista (R²=0.69, 123M params, ~500K pre-training examples) clearly surpasses ESM-2₆₅₀ₘ (R²=0.61, 650M params, ~250M sequences). This 0.08 R² improvement on a biologically meaningful regression task is a genuine and practically relevant result, supported by a Wilcoxon test (p < 10⁻³⁰⁴).

2. **Complementarity with sequence models is convincingly demonstrated**: On TSP and ESP classification, the ESM-ProteinVista ensemble outperforms both individual models across all metrics (Table 1), with McNemar's test p-values < 10⁻¹³ and < 10⁻¹⁷. This pattern holds across multiple similarity bins (Figure 2a-b), providing robust evidence that 3D structure and sequence signals are at least partly complementary.

3. **Thoughtful analysis of when structure helps**: The stratification by sequence identity, TM-score, and pLDDT confidence (Figure 2a-d) provides actionable insights: ProteinVista gains are largest on high-confidence structures and familiar folds, but the ensemble still helps on low-similarity proteins. The GO term failure case (ProteinVista 0.57 vs. ESM-2 0.62) honestly shows the boundary of the approach.

4. **Compute-efficient architecture**: Pre-training completed in 48 hours on 4 A100 GPUs (~1% of ESM-2₆₅₀ₘ's GPU-hours). The adaptive boxing (64³–160³ voxels) and compact 5-block design make the approach accessible. Inference processes 1,000 proteins in ~20s on an A100 (vs. 215–426s for ESM-2 variants), a meaningful practical advantage.

5. **Ablation studies isolate key design choices**: The Rosetta-based pre-training (no ESM-2 signal) only drops R² by ~1%, showing the contrastive objective is not the sole source of performance. Resolution (1.0 vs. 1.5 Å) and ensembling (1 vs. 5 views) are properly quantified.

## Weaknesses

### Major

- **No filtering of pre-training data against downstream test sets**: ProteinVista is pre-trained on ~500K Swiss-Prot structures. The downstream TSP, ESP, and BindingDB datasets almost certainly contain proteins with high sequence/structure similarity to those in the pre-training set. The stratification in §4.1 bins by similarity to the *fine-tuning* training set, not the pre-training set. This is a standard concern in protein ML (also affecting the ESM-2 baselines), but quantifying the overlap and reporting results after filtering would substantially strengthen the paper. Without it, the absolute generalisation claims are supported only by indirect evidence.

### Minor

- **Contrastive pre-training against ESM-2 complicates the complementarity claim**: Pre-training with ESM-2 embeddings as targets means the structural encoder is explicitly aligned to sequence-derived representations. This weakens the claim that the ESM-ProteinVista ensemble's gains reflect genuinely complementary information—the structural encoder has already "seen" ESM-2's representation space. The Rosetta-only ablation (§4.2, only ~1% worse) partly mitigates this concern, but it would be stronger to demonstrate complementarity using a version of ProteinVista pre-trained without any sequence-derived signal.

- **Rotation robustness via discrete augmentations only**: The augmentation set (90° rotations, mirror reflections) covers a finite subgroup of SO(3). ProteinVista may not be robust to arbitrary continuous rotations. The strong dependence on the 5-view ensemble (Table 2e: single view reduces R² by 5.5–6.4%) suggests the model has not fully internalised rotation invariance. The paper would benefit from evaluating on randomly rotated test structures and reporting variance across orientations.

- **Numerical inconsistencies between text and figure**: The ablation values in the text (§4.2) and Figure 2e's table disagree on several points: (i) Rosetta vs. CL: text says ~1.0%, table says ~1.2%; (ii) 1.5Å vs. 1.0Å: text says ~1.1%, table says ~0.8%; (iii) disabling training augmentation: text says -0.1%, table says ~0.4%. These need harmonization. Also, the Discussion (§5) mentions "33 Rosetta scores" while §2.3 and §4.2 say "23"—a copy-editing error.

- **FLOPs vs. wall-clock time comparison is plausible but under-explained**: ProteinVista has 415 GFLOPs (vs. ESM-2₁₅₀ₘ's 140) yet runs ~10× faster. The paper attributes this to better parallelism of shallow CNNs vs. deep transformers. This is physically plausible (CNNs have higher arithmetic intensity), but the lack of a breakdown (e.g., memory bandwidth utilisation, batch size, CUDA kernel profiling) leaves the reader guessing.

### Trivial

- Storage comparison (75 GB float32 NumPy arrays for 5,800 proteins) is a bit overdrawn — half-precision or compression would reduce this — but it's an honest comparison of raw formats.

## Nice-to-Haves

- **Comparison to equivariant architectures**: The paper claims to address the limitation of GNN-based protein encoders but does not compare to equivariant atom-level methods (e.g., EGNN, SE(3)-Transformers, or the all-atom GNN from 4S2L519nIX). These would contextualize the 3D CNN design choice relative to equivariant alternatives.
- **Continuous rotation stress test**: Adding a properly randomized rotation test (not just the 5-ensemble average) would strengthen the rotation robustness claims.

## Removed Points

These points were raised by reviewers but are removed from the main review with justification:

1. **"FLOPs/runtime discrepancy is physically implausible"** — REMOVED. This misunderstands the relationship between FLOPs and wall-clock time. CNNs have substantially higher arithmetic intensity than transformers; their operations are more regular and better utilize GPU tensor cores. The paper's explanation (better parallelization of shallow CNNs vs. deep transformers) is standard and correct.

2. **"Ensemble underperformance on IC50 not discussed"** — REMOVED. The paper explicitly discusses this (§3.2, line 123): "the ESM–ProteinVista ensemble performs worse (Table 2)." It also offers a reasoned explanation (affinity prediction needs fine geometry, leaving little for the sequence model to contribute).

3. **"ProteinVista equals ESM-2₁₅₀ₘ on ESP (91.8%) so superiority claim is wrong"** — REMOVED. This cherry-picks one column while ignoring that ProteinVista outperforms ESM-2 on TSP (90.8% vs. 88.5%) and substantially on IC50 (R² 0.69 vs. 0.61), and the overall trend across all benchmarks is clear.

4. **"Pre-training data scale is modest"** — REMOVED. Relative to PLMs (250M sequences), 500K is >2 orders of magnitude less data. The paper's claim about data efficiency is correctly scoped.

5. **"Missing related works (EGNN, SE(3)-Transformers)"** — MOVED to Nice-to-Haves. These are relevant but the paper's main comparison is against ESM-2, the dominant approach in practice. Not including them is a gap but does not invalidate the paper's claims.

6. **"Storage comparison using float32 is wasteful"** — REMOVED. The comparison honestly reports raw storage. Half-precision is standard practice but does not affect the paper's main conclusions about compute efficiency.

7. **Paper claims about novelty are overstated** — REMOVED. The paper acknowledges prior 3D CNN work (Derevyanko et al., Kulikova et al.) and correctly identifies its novelty as large-scale pre-training, which is a legitimate distinction.

## Novel Insights

The most interesting finding across the reviews — one that emerges clearly from the paper but is not explicitly stated by any reviewer — is the *asymmetric complementarity* pattern: on classification tasks (TSP, ESP), sequence and structure signals combine constructively (ensemble > either alone), whereas on the regression task (IC₅₀), the structure-only model already dominates and adding sequence signal *hurts*. This suggests a task-dependent hierarchy: coarse-grained functional classification benefits from the broad evolutionary context in sequence embeddings, while precise affinity regression is dominated by the fine geometric detail that the 3D CNN captures. The failure on GO term prediction (0.57 vs. 0.62) further reinforces this: when the task is essentially homology-based nearest-neighbor retrieval, structure adds noise rather than signal. These boundary conditions are more informative than the headline numbers.

## Suggestions

1. **(If pursued for publication)** Perform and report sequence-identity filtering between the pre-training set (Swiss-Prot) and each downstream test set. If even moderate overlap exists, rerun the main comparisons on a filtered subset. This single addition would substantially increase confidence in the results.

2. **(If pursuing revision)** Resolve the ablation numerical inconsistencies and the 23 vs. 33 Rosetta scores discrepancy. These are small fixes but suggest haste.

3. Add a controlled experiment comparing ProteinVista pre-trained with the Rosetta-only objective (no ESM-2 signal) to ESM-2 on the ensemble complementarity analysis. This would cleanly address the confound concern.

4. Report variance across the 5 augmented views (or across random seeds) for the main results, not just the ensemble average.

## Score and Decision

**Anchor comparison** (all paths from calibration search):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/.../iBAWiEjogY.md` (ProteiNexus) | 3.67 | Rejected; data leakage concerns dominated. ProteinVista has better-controlled experiments and stronger results. |
| `/home/.../BEH4mGo7zP.md` (ProteinINR) | 5.75 | Accepted; marginal improvements over ESM-GearNet. ProteinVista shows larger, clearer gains. |
| `/home/.../sTYuRVrdK3.md` (ProteinWorkshop) | 6.25 | Accepted; benchmark paper, different contribution type. Comparable quality. |
| `/home/.../4S2L519nIX.md` (All-Atom Geom-GNN) | 6.50 | Accepted; explores pretraining/scaling of Geom-GNNs. Comparable rigour, though ProteinVista has stronger empirical wins. |
| `/home/.../O0dW800ukz.md` (ProteinSSA) | 5.67 | Rejected; unclear motivation, missing baselines. ProteinVista is better-motivated and more clearly presented. |
| `/home/.../i6jYK0hd0B.md` (3D Interaction Pre-training) | 4.00 | Rejected; limited novelty. ProteinVista has clearer practical relevance. |
| `/home/.../0ctvBgKFgc.md` (ProtComposer) | 8.00 | Accepted; protein generation, different task. Higher innovation bar met. |
| `/home/.../IEZjjDX0iC.md` (Comparing pLMs) | 3.00 | Rejected; narrow scope. |
| `/home/.../ifK9NFyrhn.md` (Leakage-Free Datasets) | 3.50 | Rejected; addresses data leakage specifically, not comparable contribution. |

Relative to the anchors, ProteinVista sits above the 5.75–6.25 accepted papers in terms of result clarity and practical significance, but the unresolved data leakage question and numerical inconsistencies prevent it from reaching the 7+ range.

**Originality**: Moderate — 3D CNNs for proteins have been explored before, but large-scale pre-training with this architecture is new.
**Importance of question**: High — structure-aware protein models are an active and important area.
**Claims supported**: Mostly yes, with caveats about data leakage and the contrastive confound.
**Soundness**: Good — experiments are well-designed, ablations informative, limitations discussed.
**Clarity**: Good overall, marred by a few numerical inconsistencies.
**Value to community**: High — the model is compact, compute-efficient, and the code is promised open-source.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>