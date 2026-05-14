## Summary
ProteinVista is a 123 M-parameter 3D CNN that voxelizes full-atom protein structures at 1 Å resolution and is pre-trained via contrastive alignment to ESM-2 embeddings on ~500 k AlphaFold-2 structures. The paper reports that ProteinVista matches or exceeds ESM-2 (150 M / 650 M) on enzyme-substrate (ESP), transporter-substrate (TSP), and BindingDB IC50 prediction under a controlled fine-tuning protocol, with a notable IC50 gain (R² 0.69 vs 0.61) and substantial inference-time savings; an optimized ensemble with ESM-2 attains SOTA on TSP/ESP.

## Strengths
- **Genuine, non-trivial IC50 signal.** ProteinVista alone reaches R² = 0.69 vs 0.61 for ESM-2-650M on BindingDB IC50, with a Wilcoxon signed-rank p < 10⁻³⁰⁴ on paired squared errors (Table 2, §3.2). This is the strongest standalone evidence that atom-level voxelization helps affinity regression.
- **Controlled within-paper comparison to ESM-2.** All models use the same MolFormer ligand embeddings and the same two-layer head, with a uniform learning-rate search (§3.1). This makes the head-to-head encoder comparison interpretable.
- **Useful, rarely reported compute/runtime accounting.** Pre-training in 48 h on 4× A100 (~1 % of ESM-2-650M's GPU-hours) and 1 000-protein inference in 20 s vs 426 s for ESM-2-650M (§4.3, Fig. 3) is concrete and the disk-space trade-off is honestly disclosed.
- **Honest negative result on GO-MF.** ProteinVista underperforms ESM-2-650M on GO-MF (Fmax 0.57 vs 0.62, §3.4) and the asymmetry in ensembling between classification and IC50 is reported without cherry-picking.
- **Targeted ablation on augmentation and pretraining objective.** Multi-view test-time averaging is shown to be the dominant driver of robustness (–5.5 % R² with single view), while training-time augmentation contributes little, supporting the claim that rotational robustness is established in pretraining (§4.2, Fig. 2e).

## Weaknesses

### Fatal
None.

### Major
- **No structure-aware baselines, despite a motivation built explicitly on them.** §1 frames the contribution against GearNet, ESM-GearNet (called out by name, line ~27), GPS-Fun and the general residue-graph family, arguing they "only slightly outperformed sequence-only ESM-2." But Tables 1–2 only compare to ESM-2-150M/650M. Without any residue-level structure-aware encoder on the same TSP/ESP/IC50 splits, the headline that "full-atom 3D CNNs are … superior to protein transformers for structure-dependent tasks" (abstract) is not actually tested against the family of methods most directly threatened by the contribution. This is the central experimental gap.
- **"Two orders of magnitude less data" obscures an ESM-2 dependence in the chosen pipeline.** The selected pretraining objective is contrastive alignment of ProteinVista embeddings to ESM-2 sequence embeddings (§2.3); the ablation (§4.2) confirms this objective was chosen over Rosetta-only because it gives +1 % R². The data-efficiency framing in the abstract and §3.2 omits that the deployed model inherits signal from ESM-2's 250 M-sequence pretraining via the teacher. To the paper's credit, a Rosetta-only alternative is reported and is only ~1 % worse, which partially defuses the criticism — but the abstract should explicitly acknowledge ESM-2-in-the-loop for the headline configuration.
- **SOTA comparison in §3.3 is not apples-to-apples.** ESM-ProteinVista_OP adds joint ligand-encoder fine-tuning, a separately trained contrastive head, *and* ensembling with ESM-2-650M. SPOT, ProSmith-ESP, and Fusion-ESP did not receive these pipeline components. The 0.1–0.9 pp accuracy / 0.01 MCC margins (Table 1) cannot be attributed to the protein encoder under this design.
- **Pattern in Figure 2a is consistent with similarity leakage and the paper does not rule it out.** The largest ProteinVista–ESM gap is in the 80–100 % sequence-identity-to-training bin, the gap narrows monotonically with identity, and the lowest-identity bin is near parity. The paper interprets this as evidence that 3D structure captures mutation effects; a similarity-controlled split (e.g., MMseqs2 ≤30 %) is the standard way to distinguish that hypothesis from memorization, and is not reported. Crucially, the §4.1 stratification is a property of the test set against the training set; how the train/test partition itself was generated for TSP/ESP/IC50 is not described in the main text. This matters because the analysis is the paper's main internal validation that structure is providing the gain.

### Minor
- **IC50 lacks domain-standard baselines.** The most interesting result is benchmarked only against in-house ESM-2 with a 2-layer head; conventional drug-target baselines (e.g., DeepDTA-style) are absent. This is not fatal — the paper's stated scope is encoder comparison — but for a result this striking, an additional external reference point would substantially strengthen the claim.
- **Rotational invariance is overstated.** Augmentation covers octahedral rotations and mirror reflections (24 + reflections), not SO(3); the paper repeatedly uses "rotation-robust" / "rotational invariance" language, and equivariant baselines (SE(3)-Transformer, EGNN, GVP) are not benchmarked. The ablation already shows that the dominant contribution is multi-view test-time averaging rather than learned invariance, which is informative but means the terminology should be tightened.
- **No variance / multiple seeds.** Margins like 0.951 vs 0.955 AUC on ESP (Table 1) are small enough that single-seed numbers cannot support directional claims. McNemar testing is reported for the ensemble-vs-ESM-2 comparison, but the ablation deltas (~1 %) lack any run-to-run baseline.
- **160 Å crop unanalyzed.** The paper crops proteins exceeding the 160³ box (§2.1) but never reports the fraction cropped per benchmark, nor performance on cropped vs uncropped subsets. For multidomain enzymes / transporters this could matter.
- **GO-MF post-hoc framing.** Labeling GO-MF as "homology-reliant" after observing the loss is a reasonable hypothesis but is not tested (e.g., by stratifying GO performance by homology to training set, as is done for TSP in §4.1).

### Trivial
- The density-formula rendering in §2.1 line 61 looks malformed (likely a parser issue from the equation extraction); confirm the appendix presentation in the camera-ready.

## Nice-to-Haves
- Add at least one residue-level structure-aware encoder (GearNet/ESM-GearNet, GVP-GNN, or SaProt) on the same TSP/ESP/IC50 splits.
- Re-run benchmarks under similarity-controlled splits (≤30 % sequence identity; ≤0.5 TM-score for IC50 targets).
- Run the Grad-CAM-style binding-pocket visualization that §5 promises; this is the natural mechanistic check on the "ProteinVista learns pocket geometry" thesis.
- Multiple seeds + variance / CIs on Tables 1–2 and on ablation deltas.
- Explicitly reframe the data-efficiency statement to acknowledge ESM-2-as-teacher in the deployed configuration, and lean on the Rosetta-only ablation to argue that ProteinVista is *also* competitive without it.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- **Harsh critic: "Strawman or under-discussed objective choice" (§2.3 / §5 alternatives).** The paper does run a head-to-head ablation against Rosetta-only pretraining (§4.2). The complaint that masked-voxel/jigsaw objectives weren't tried is a reasonable extension but is scope creep, not a flaw — §5 explicitly flags these as future work.
- **Harsh critic: §4.1 confound with protein class.** The pLDDT confound mentioned is speculative; the paper shows the high-confidence bin contains most test proteins (Fig. 2d) and acknowledges the pattern as a hypothesis about experimental-structure benefit. Not strong enough to keep as a weakness.
- **Strength: "addresses a highly relevant problem" / "important research question" framings.** Generic.
- **Strength: McNemar significance for ensemble.** Significance under McNemar can be inflated by ensembling alone and does not by itself establish encoder complementarity; folded into the more general ensemble-gain strength.

## Novel Insights
The most informative empirical observation is the *task-asymmetric* behavior of structure vs sequence: ensembling helps classification (TSP/ESP) but *hurts* IC50, where ProteinVista alone is strictly better. Combined with the GO-MF result, this is consistent with a coherent picture — sequence dominates when the prediction is homology-transferable, while atom-level geometry dominates when the prediction depends on fine-grained pocket complementarity (continuous affinity regression). The ablation finding that nearly all of the rotation-robustness benefit comes from multi-view *inference-time* averaging, not from training-time augmentation, is also a non-obvious and useful observation. Both insights are the paper's own, but they are substantive.

## Suggestions
- Add at minimum GearNet and either GVP-GNN or SaProt to Tables 1–2 on the same splits.
- Report whether TSP/ESP/IC50 splits are sequence-identity- and (for IC50) TM-score-controlled; if not, re-evaluate with controlled splits.
- Move the Rosetta-only ablation result forward to disarm the "but you used ESM-2" objection; rewrite the abstract's data-efficiency claim around that.
- Either drop the SOTA-beating framing of §3.3 or apply the same OP pipeline (joint ligand fine-tuning + contrastive head + ESM-2 ensembling) to SPOT/ProSmith-ESP/Fusion-ESP.
- Report cropping statistics per benchmark and cropped-vs-uncropped subset accuracy.
- Run multiple seeds; report CIs on at least Tables 1–2 and the ablation panel.

## Axis evaluation
- **Originality:** Moderate. Voxelized 3D CNNs for proteins are not new (DeepSite, 3DCNN_MQA, EnzyNet), but the scale (500 k AF2 structures), the contrastive-to-ESM-2 pretraining objective, and the engineering choices (adaptive boxing, multi-view inference) are a sensible modern instantiation.
- **Importance of research question:** Real — whether atom-level structure adds signal beyond sequence transformers for binding tasks is an open empirical question.
- **Claim support:** Mixed. The IC50 claim is well-supported on its own. The headline "outperforms sequence transformers" is supported only against ESM-2; the data-efficiency claim glosses over ESM-2 distillation; the SOTA claim mixes pipeline components.
- **Soundness of experiments:** Mediocre. No similarity-controlled splits, no multi-seed variance, no structure-aware baselines despite the motivation explicitly targeting them.
- **Clarity:** Generally clear and honestly presented; negative results are reported.
- **Value to community:** Real — the compute/runtime data point, the IC50 result, and an open-source 3D-CNN baseline are useful even if the comparative claims need tightening.

## Score and Decision

Anchors retrieved (paths, avg human score, comparison to paper under review):
- `iBAWiEjogY` — ProteiNexus (3.67, Reject). **Read.** Very close analogue: structural pretraining for proteins, leakage concerns, train/test split unclear, weak experimental discipline. ProteinVista has stronger IC50 evidence and better engineering reporting than ProteiNexus, but shares the missing-structure-baseline and split-transparency issues.
- `BEH4mGo7zP` — ProteinINR (5.75, Accept). **Read.** Comparable scope (multimodal protein pretraining) but compares fairly against ESM-GearNet family on standard benchmarks. ProteinVista's missing structure-aware baselines make it weaker on this dimension.
- `sTYuRVrdK3` — ProteinWorkshop (6.25, Accept). **Read.** A benchmark paper, different scope; demonstrates the standard the field expects for fair multi-method comparison, which ProteinVista does not meet.
- `ARQIJXFcTH` — AtomSurf (6.75, Accept). Not read in full; concerns fair surface-vs-graph comparison within Atom3D — sets the bar for the kind of controlled comparison ProteinVista does not provide.
- `OzUNDnpQyd` — Structure Language Models (7.00, Accept). Not read; different problem (conformation generation), weaker analogue.
- `IEZjjDX0iC` — Comparing PLMs for phages (3.00, Reject). Not read; benchmarking paper with weak conclusions.
- `Et0SIGDpP5` — Long-context PLM (4.25, Reject). Not read; weak experimental design.
- `AXbN2qMNiW` — Protein-ligand binding from fine-grained interactions (5.67, Accept). Not read; closest topical analogue — accepted with concrete binding-task improvements and a clear novel objective.
- `xNDydjYBmC` — PPB affinity prediction (4.60, Reject). Not read; rejected for limited methodology.
- `gB2ZeqDpl6` — DTI benchmark (4.00, Reject). Not read; relevant DTI baseline literature ProteinVista should have engaged with.
- `O0dW800ukz` — Multimodal distillation (5.67, Reject). Not read; similar distillation flavor.
- `K3tHTPjFBM` — Equivariant protein multi-task (4.00, Reject). Not read.
- `Dr4qD9bzZd` — Functional geometry guided design (4.00, Reject). Not read.
- `fM432E7l5w` — Conditional diffusion for protein generation (3.60, Reject). Not read; weak experimental design analogue.
- `U5gNAmN3h1` — AMP benchmarking (3.50, Reject). Not read.
- `1S8ndwxMts` — Protein generative metrics (3.00, Reject). Not read.

Positioning: ProteinVista is clearly stronger than the 3.5–4.0 rejects (more substantive engineering, a real standalone IC50 result, honest negative GO-MF reporting) but weaker than the 5.75 / 6.25 accepts (which run the structure-aware baselines ProteinVista names but does not include, and which describe their splits cleanly). It sits closest to ProteiNexus (3.67) on experimental discipline but with a genuine IC50 contribution that ProteiNexus lacks. Net: a borderline-reject — material contribution, but the central comparative claim is under-tested for an ICLR-level publication.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>