Now I have all the information I need. Let me compile the consolidated review.

---

## Summary

ProteinVista introduces a full-atom 3D CNN that voxelizes protein heavy atoms into a 5-channel density grid, pretrains on ~500K AlphaFold-2 structures (two orders of magnitude less data than ESM-2), and is evaluated on three protein-ligand prediction tasks (transporter-substrate, enzyme-substrate, drug-target IC₅₀). It outperforms ESM-2 on structure-sensitive tasks while using 5× fewer parameters and dramatically less GPU time (~20s vs 426s per 1K samples vs ESM-2₆₅₀M), and a simple ensemble with ESM-2 further improves accuracy, demonstrating complementarity between sequence and structure signals.

## Strengths

- **Concrete compute-efficiency demonstration with measured runtime.** Figure 3 reports wall-clock times: ProteinVista processes 1K proteins in ~20s on a single A100 vs 426s for ESM-2₆₅₀M, and pretraining finishes in 48 hours on 4 A100s vs ~7 days on 128 H100s. These measurements directly refute the long-held assumption that full-atom 3D CNNs for proteins are computationally prohibitive.

- **Clear performance gains on structure-sensitive tasks despite far less data and parameters.** Table 1 shows ProteinVista achieving 90.8% accuracy (MCC 0.77) on TSP vs ESM-2₆₅₀M's 89.3% (MCC 0.74). Table 2 shows a more substantial gain on IC₅₀ regression (R² 0.69 vs 0.61). When coupled with an optimized pipeline, the ESM-ProteinVista ensemble surpasses specialized SOTA methods (SPOT, ProSmith-ESP, Fusion_ESP).

- **Systematic ensemble analysis establishing complementarity.** The ESM-ProteinVista ensemble consistently outperforms both individual models across all metrics (e.g., TSP accuracy 91.5% vs 89.3% for ESM-2₆₅₀M), with McNemar's tests confirming significance (p < 10⁻¹³). Figure 2 further demonstrates that complementarity holds across bins of sequence identity, structural similarity, and structure confidence (pLDDT).

- **Well-designed ablation studies.** Section 4.2 quantifies the impact of key design choices (single vs multi-view inference: −6.4% R²; Rosetta vs contrastive pretraining: −1.0%; 1.5Å vs 1.0Å resolution: −1.1%), providing evidence for why each design decision was made.

- **Stratified analysis by structural quality and similarity.** Figure 2 bins the test set by sequence identity, TM-score, and pLDDT, showing that gains are concentrated in the regimes where structural detail matters most and that the majority of test proteins fall in the high-confidence range.

## Weaknesses

### Fatal
None.

### Major

- **No direct comparison to structure-aware (graph-based) encoders.** The Introduction frames ProteinVista against GearNet, ESM-GearNet, and other graph-based methods, claiming they "omit atom-level details" (Section 1). Yet the controlled experiments compare only to sequence-based ESM-2. The specialized SOTA models in Table 1 (SPOT, ProSmith-ESP, Fusion_ESP) use task-specific pipelines, so they do not serve as baselines for evaluating the general-purpose encoder. Without comparing to GearNet or ESM-GearNet on the same three benchmarks with the same prediction head, it is impossible to attribute the reported gains to atom-level voxelization versus simply using *some* structural information. This gap directly weakens the paper's broader claim that atom-level detail provides a decisive advantage over existing structure-aware approaches.

### Minor

- **Rotation robustness is tested only with 90° axis-aligned augmentations.** Section 2.4 describes augmentations limited to 90° rotations and axis mirrorings. The paper never evaluates on arbitrary continuous rotations (e.g., 30° around a random axis), which would be common in real-world use. While the ablation shows multi-view inference recovers the 6.4% single-view R² drop, this does not demonstrate robustness to off-axis orientations. The paper's claims of "rotation-invariant predictions" (Section 1) and "rotation-robust representations" (abstract) are overstated relative to the evidence provided.

- **No multiple random seeds or variance estimates.** The paper reports all results as point estimates with no standard deviations or confidence intervals from multiple runs. This is standard practice for deep learning benchmarks and would improve confidence in the reported numbers, especially given the modest gaps on some classification tasks.

- **The contrastive pretraining objective anchors to ESM-2 embeddings.** ProteinVista is pretrained by aligning its embeddings with ESM-2 sequence embeddings via InfoNCE loss. This implicitly conditions the structure encoder on information already captured by a sequence model. While the Rosetta-regression ablation (Section 4.2) partially addresses this (showing only 1% difference), a purely structural self-supervised objective (e.g., masked voxel prediction) would better isolate the contribution of 3D geometry.

- **Minor numerical inconsistency in ablation results.** Section 4.2 states that replacing contrastive alignment with Rosetta regression decreased R² by "1.0%," but the table in Figure 2e reports "~1.2%" for the same comparison. While small, this inconsistency should be resolved.

- **The IC₅₀ dataset details are deferred to an inaccessible appendix.** Table S3 (dataset sizes, splits) is referred to but not available in the main text or accessible supplementary. This information should be summarized in the paper body.

### Trivial

- **The voxelization density function (Section 2.1, Eq. 1) is unclearly written.** The formula states "contribution to the c-channel of the voxel centered at v = exp(-||v - r||/σ²) with σ = 1." It is unclear whether this uses distance (||v-r||) as written or the standard squared distance (||v-r||²). This should be clarified for reproducibility.

## Nice-to-Haves

- Testing rotation robustness with arbitrary continuous rotations (e.g., 0–360° around a random axis) would validate the augmentation strategy.
- A self-supervised structural pretraining baseline (e.g., masked voxel reconstruction) would strengthen the evidence for genuine geometric learning independent of sequence alignment.
- Comparing to GearNet or ESM-GearNet under the same pipeline (same MolFormer embeddings, prediction head) would strengthen the paper's broader claims about atom-level detail.
- Discussing compression strategies for the 75GB storage footprint (e.g., sparse voxel representations) would improve practical applicability.

## Removed Points

*These points were flagged by reviewers but are removed because they are factually incorrect, already addressed by the paper, or reflect reviewer knowledge gaps.*

- **FLOPs vs. inference time discrepancy (Critic Point 4 under Section 4.3).** The reviewer claims that if ProteinVista has 415 GFLOPs vs ESM-2₁₅₀M's 140 GFLOPs, it should be *slower*, not faster. However, the paper explicitly addresses this in Section 4.3: "This suggests that computations for the ProteinVista CNN with only five ProteinVista blocks can be parallelized more efficiently than those required for the ESM-2 models that have many more encoder layers." FLOPs and wall-clock time are not linearly related due to parallelization efficiency, memory bandwidth, and model depth. The criticism ignores this explanation.

- **Storage cost as an unaddressed weakness.** The paper transparently acknowledges the storage trade-off in Section 4.3: "The trade-off is disk space… 75 GB as float32 coordinate NumPy arrays." This is presented as an acknowledged limitation, not an oversight.

- **Practical significance of small TSP/ESP gaps.** The reviewer calls the ≤1% accuracy gap "uncertain" in practical significance. However, the paper demonstrates statistically significant improvements via McNemar's test, and the IC₅₀ gap (R² 0.69 vs 0.61) is substantially larger and more compelling. The paper also shows the ensemble improves over both models consistently.

- **Strength Finder's generic/delusional strengths.** Removed generic strengths such as "addressed an important problem" that lacked specific evidence. All retained strengths are grounded in specific tables/figures.

## Novel Insights

None beyond the paper's own contributions. The interaction between the two reviews is largely additive rather than contradictory: the harsh critic correctly identifies missing baselines and methodological gaps, while the strength finder correctly identifies the core experimental evidence that does exist. The most interesting tension is around what the paper's central claim actually is — the title focuses on outperforming *sequence transformers* (which is well-supported), but the Introduction's framing against *graph-based structure-aware methods* (which is not benchmarked). This mismatch between framing and experimental evidence is the paper's most significant weakness.

## Suggestions

1. **Directly compare to GearNet or ESM-GearNet** on the same three benchmarks (TSP, ESP, IC₅₀) with the same MolFormer embeddings and prediction head. This is the single most important experiment to validate the paper's broader claims about atom-level detail.
2. **Test arbitrary continuous rotations** (e.g., random rotations sampled uniformly from SO(3)) on a held-out subset and report variance in predictions to substantiate the rotation-robustness claim.
3. **Report results across 3–5 random seeds with standard deviations** for all main metrics.
4. **Clarify the voxelization density function** — specify whether it uses distance or squared distance in the exponent.
5. **Resolve the 1.0% vs 1.2% numerical discrepancy** in the ablation values.

## Score and Decision

**Calibration anchors (retrieved from human-review corpus):**

| Path | Avg Score | Topic | Comparison to this paper |
|------|-----------|-------|-------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0ctvBgKFgc.md` | 8.00 | ProtComposer (protein generation) | Much stronger; flawless execution, no significant weaknesses. Not comparable in task. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ARQIJXFcTH.md` | 6.75 | AtomSurf (surface representation learning) | Slightly stronger; more comprehensive baseline comparisons and clearer contribution framing. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sTYuRVrdK3.md` | 6.25 | ProteinWorkshop (structure representation benchmark) | Comparable in rigor; ProteinWorkshop is a benchmark paper with broader scope but also had missing results. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AXbN2qMNiW.md` | 5.67 | Protein-ligand binding (self-supervised) | Similar area; this paper is stronger in experimental design and baseline fairness. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OzUNDnpQyd.md` | 7.00 | Structure Language Models (conformation generation) | Stronger; novel framework with thorough evaluation. Different sub-area. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Ocg3XIymmp.md` | 3.50 | Pharmacophore-based voxel design | Much weaker; limited novelty, insufficient experiments. Paper under review is clearly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jqx5XI4Yr3.md` | 3.40 | ProteinAdapter (adapter-based representation) | Much weaker; limited novelty, unclear improvements. Paper under review is stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iBAWiEjogY.md` | 3.67 | ProteiNexus (structural pre-training) | Much weaker; had data leakage, missing baselines, unclear contributions. Paper under review is substantially stronger. |

Relative to these anchors: this paper is clearly stronger than the low-scoring group (3.5–3.67) and comparable to or slightly weaker than the mid-range (5.67–6.75). It has a concrete, novel methodological contribution with solid experimental evidence for its core claim (outperforming sequence transformers). However, the missing comparison to structure-aware models limits the scope of the claimed contribution, and the absence of variance estimates and limited rotation-robustness evidence prevent it from reaching the level of the strongest papers in the 6.5+ range. I calibrate the score at **6.0**, reflecting a paper with genuine contributions and well-supported core claims, but with significant gaps that should be addressed.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>