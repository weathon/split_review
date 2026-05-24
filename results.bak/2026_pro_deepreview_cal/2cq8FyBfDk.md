Now I have sufficient information. Let me write the final review.

---

## Summary
ProteinVista introduces a full-atom 3D convolutional neural network that voxelizes protein heavy atoms into 3D grids, pre-trains using contrastive alignment to ESM-2 embeddings on ~500K AlphaFold-2 structures, and fine-tunes on protein-ligand binding tasks. The model (123M parameters) outperforms the much larger ESM-2 650M sequence transformer on drug-target affinity prediction (R² 0.69 vs 0.61) and transporter-substrate classification, while requiring ~1% of the pre-training GPU-hours. Ensemble averaging with ESM-2 yields further gains, demonstrating complementary sequence-structure signals.

## Strengths
- **Strong, well-documented performance on structure-sensitive binding tasks**: ProteinVista achieves R² 0.69 vs. ESM-2 650M's 0.61 on IC₅₀ regression (p < 10⁻³⁰⁴, Table 2), and 90.8% vs. 89.3% accuracy on TSP (Table 1), despite pre-training on >500× fewer data points. The statistical significance testing adds credibility.
- **Genuine compute efficiency**: Processes 1,000 proteins in 20s vs. 426s for ESM-2 650M on an A100, with pre-training using ~1% of ESM-2's GPU-hours (Fig. 3, Sec 4.3). This counters the common belief that full-atom 3D CNNs are prohibitively expensive.
- **Complementary signals validated through ensemble**: ESM-ProteinVista averages beat both single models across all metrics on TSP and ESP (Table 1), and the optimized pipeline (ESM-ProteinVista_OP) achieves state-of-the-art on both benchmarks (93.2% TSP accuracy, 94.4% ESP accuracy). The complementary nature is a genuinely useful finding.
- **Honest, well-stratified analysis**: Partitioning test data by sequence identity, TM-score, and pLDDT (Fig. 2a–d) reveals *when* structure matters — ProteinVista's edge is largest with structural homologs present and high-confidence AlphaFold structures, and models perform similarly in the lowest-identity bin. This is unusually transparent for the field.
- **Informative ablations**: Quantifying the effect of 5-view vs. single-view inference (-6.4% relative R²), contrastive vs. Rosetta pre-training (-1.0%), voxel resolution (1.0Å → 1.5Å: -1.1%), and training augmentation removal (-0.1%) provides actionable design insights (Fig. 2e, Sec 4.2).
- **Open-source release** and honest negative result on GO annotation (Sec 3.4: F_max 0.57 vs. ESM-2's 0.62) where structure adds little value.

## Weaknesses

### Fatal
None.

### Major
- **No structure-aware baselines**: The paper argues at length that residue-level protein GNNs (GearNet, ESM-GearNet) omit atom-level detail and therefore underperform (lines 21–29), but never compares ProteinVista against any structure-aware GNN. The demonstrated gains over ESM-2 could stem from *any* structural information rather than the specific atom-level voxelization. Without comparing against a residue-graph GNN pre-trained under the same contrastive protocol, the paper cannot distinguish whether the advantage comes from atom-level resolution or simply from encoding 3D structure at all. This limits the strength of the central architectural claim.

- **Pre-training relies on the ESM-2 teacher it is compared against**: The contrastive objective aligns ProteinVista embeddings to ESM-2 embeddings, meaning the structure encoder is partially distilling from the sequence model. While the Rosetta regression ablation (-1.0% relative R²) suggests the architecture can learn without this teacher, a pure self-supervised structure objective (e.g., masked voxel prediction) would provide cleaner evidence that the 3D CNN independently extracts function-relevant features.

### Minor
- **Rotation robustness claims are partially validated**: The paper uses only 90° rotations and axis mirrors during training and 5-view averaging at test time. The ablation showing -0.1% change when disabling fine-tuning augmentation is encouraging, but claims of "rotation-robust representations" (abstract, line 35, 85) are not tested against arbitrary continuous rotations. A direct test on randomly rotated test proteins would substantiate the claim.

- **No pre-training ablation (random-init baseline)**: The paper does not report performance of the 3D CNN fine-tuned from scratch on each task, which would quantify the contribution of the pre-training phase versus the architecture alone.

- **Data split construction not described**: The paper references standard benchmarks (TSP, ESP, BindingDB) but does not describe how train/validation/test splits were constructed or what measures were taken against homology/ligand leakage. While the stratified analysis (Sec 4.1) partially addresses this indirectly, explicit split protocols are needed for full reproducibility.

### Trivial
- The GO annotation experiment (Sec 3.4) only evaluates molecular-function terms; biological process and cellular component ontologies are not tested, though this is acknowledged implicitly.

## Nice-to-Haves
- A 3D Grad-CAM visualization (mentioned in the discussion, line 512) would strengthen the claim that ProteinVista autonomously identifies binding-relevant regions.
- Exploring deeper or wider 3D CNN architectures to test scaling behavior.
- Including dynamic conformations beyond single rigid snapshots (acknowledged by the authors as future work).

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"The 3D CNN is very shallow (five blocks) and lacks residual connections"** — The downstream results are strong, so this is not a demonstrated weakness. The architecture's adequacy is proven by its performance.
- **"InfoNCE loss copied from vision-language models without justification in the protein domain"** — InfoNCE is standard practice across domains; demanding domain-specific justification for a well-established loss function is unreasonable.
- **"The figure would benefit from error bars or confidence intervals"** — Presentation nitpick; the statistical tests and binning analyses already provide rigor.
- **"Training throughput numbers should clarify whether they measure forward pass only or full training steps"** — The paper states "processes 1,000 proteins... in 20 seconds during training" (line 486), which is clear. Demanding batch-size and precision details is a reproducibility nitpick beyond what a main paper typically provides.
- **"The parity with SPOT/ProSmith-ESP would be more meaningful if the comparison included structure-aware competitors"** — Merged into the major weakness about missing structure-aware baselines above.

## Novel Insights
The stratified analysis (Fig. 2a–c) is genuinely revealing: it shows that ProteinVista's advantage over ESM-2 is largest when structural homologs are present in the training set, and that the two models perform similarly in the lowest sequence-identity bin — yet their average still improves performance. This pattern suggests a useful rule of thumb for practitioners: structure encoders add value when folds are known, while sequence models generalize better to novel folds. The paper also makes a concrete empirical case that full-atom 3D CNNs are not just viable but practical at scale, which challenges a standing assumption in the field.

## Suggestions
- Add at least one structure-aware GNN baseline (e.g., GearNet or ESM-GearNet) pre-trained with the same contrastive alignment protocol and fine-tuned identically. This would directly test whether atom-level resolution matters over residue-level graphs.
- Report performance under random continuous test-time rotations (beyond the 90° grid) to validate the rotation-robustness claim.
- Include a "no pre-training" baseline (3D CNN fine-tuned from scratch) to quantify the value of the contrastive pre-training phase.
- Describe the train/validation/test split protocol for each benchmark, including any homology or ligand-similarity filtering.

## Score and Decision

**Calibration anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| SaProt (6MRm3G4NiU) | 7.33 | R1 | Stronger: broader eval (10 tasks), cleaner structure integration, no teacher confound |
| Structure Language Models (OzUNDnpQyd) | 7.00 | R1 | Stronger: more novel framework, better evaluated |
| ProteinWorkshop (sTYuRVrdK3) | 6.25 | R2 | Similar quality, ProteinVista more novel but narrower evaluation |
| ProteinINR (BEH4mGo7zP) | 5.75 | R2 | Weaker: marginal gains, missing baselines; ProteinVista has larger empirical gains |
| BindNet (AXbN2qMNiW) | 5.67 | R2 | Weaker: data leakage concerns, missing ESM-2 baselines |
| ProteiNexus (iBAWiEjogY) | 3.67 | R1 | Much weaker: data leakage, missing baselines, low novelty |

**Round 1 bracket:** 5.0–7.0. **Round 2 narrowing:** ProteinVista is clearly above the ~5.7 anchors (more significant gains, cleaner experiments, better ablations) but below SaProt at 7.33 (fewer tasks, ESM-2 teacher confound, missing structure baselines). It sits comparably to ProteinWorkshop at 6.25 but with more novel contribution and less comprehensive evaluation. Final placement: **6.0**.

The paper makes a real contribution — a practical full-atom 3D CNN that challenges the assumption that such models are too expensive, with strong results on binding tasks. The missing structure-aware baselines and ESM-2 teacher confound are genuine gaps but do not invalidate the demonstrated gains over sequence transformers. The efficiency story and complementarity findings are independently valuable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>