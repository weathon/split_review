Now I'll write the final consolidated review.

## Summary

ShEPhERD introduces an SE(3)-equivariant diffusion model that jointly learns the distribution over 3D molecular structures and their interaction profiles — shapes, electrostatic potential surfaces, and directional pharmacophores. By enabling conditional generation via inpainting, the method is demonstrated on three ligand-based drug design tasks: natural product ligand hopping, protein-blind bioactive hit diversification, and bioisosteric fragment merging.

## Strengths

1. **Joint diffusion of directional pharmacophores with vector representations**: ShEPhERD models pharmacophore directionality (HBA, HBD, aromatic rings, halogen bonds) by diffusing/denoising vectors on the unit sphere (Section 3.1, lines 117–119; Section 3.3, line 145), going substantially beyond prior work like MolSnapper (Section 2, line 79) which treated only N/O atoms as HBD/HBA and ignored all other interaction types.

2. **Joint denoising architecture with explicit cross-modal interaction**: The denoising network (Section 3.3, lines 182–208) uses a three-component design (embedding → joint local+global interaction → denoising) where the joint module first runs SE(3)-equivariant message passing on a heterogeneous graph collating all four modalities, then applies sum-pooling and equivariant tensor products to obtain a global code. This goes beyond prior 3D molecular DDPMs (e.g., MIDI, MolDiff) that model only the molecule itself.

3. **OOD generalization on bioisosteric fragment merging**: ShEPhERD successfully merges 13 experimentally identified fragments (27 pharmacophores) into drug-like ligands with up to 89 atoms (Section 4, lines 251–260), where both molecule size and pharmacophore count are "significantly out-of-distribution" from the MOSES-aq training set (line 260). This demonstrates that the joint model generalizes far beyond its training distribution.

4. **Self-consistency evaluation protocol with xTB relaxation**: The unconditional joint generation evaluation (Section 4, lines 235–236) computes the true interaction profiles of generated molecules *after* semi-empirical DFT (xTB) relaxation and realignment, avoiding optimistically scoring strained geometries. The average RMSD upon relaxation is <0.1 Å for all unconditional models on ShEPhERD-GDB17.

5. **Surface-based shape similarity calibrated to volumetric scoring**: The paper defines a new surface similarity function (Section 3.2, lines 126–127) with a calibration function Ψ that maps the Gaussian width to match a volumetric gold standard, a principled design choice absent from prior surface-based methods.

## Weaknesses

### Major

1. **No ablation studies of architectural choices.** ShEPhERD's architecture is complex: four separate EquiformerV2 embedding modules, a joint module with both local (heterogeneous graph message-passing) and global (sum-pooled vector) interaction components, multiple denoising heads, and symmetry-breaking noise injection. None of these design choices are ablated. It is unclear whether the joint module (with both local and global interaction) improves over simpler cross-attention, whether jointly modeling all modalities together outperforms training separate single-modality models, or whether the expensive EquiformerV2 backbone is needed versus more efficient alternatives (e.g., simpler E3NN variants). Since the paper positions itself partly as a methodological contribution, the absence of ablations is a significant gap.

2. **Evaluation lacks direct comparisons to relevant prior interaction-conditioned 3D generative models.** The paper situates itself as an advance over shape-conditioned 3D generation (Chen et al. 2023, Lin et al. 2024, Le et al. 2024) and pharmacophore-conditioned generation (Ziv et al. 2024), yet never compares against any of these methods under a shared evaluation protocol. The only quantitative baselines used are randomly sampled dataset molecules and REINVENT (the latter confined to the appendix). While the paper's primary contribution is the *joint* modeling framework (all three modalities together), the absence of even single-modality comparisons (e.g., comparing ShEPhERD's shape-conditioned generation against Chen et al. 2023 on the same shape similarity metric) makes it difficult to assess whether the unified approach adds value beyond existing dedicated methods.

### Minor

3. **Evaluation relies exclusively on self-defined scoring functions that operate on the same representations ShEPhERD generates.** The shape, ESP, and pharmacophore similarity scores (Section 3.2, lines 123–133) are custom-designed for the point-cloud representations used by the model. While the scoring functions are well-motivated (Gaussian overlap, physically-motivated parameters) and evaluation is performed after xTB relaxation to avoid scoring strained geometries directly, the absence of validation against established external tools (e.g., ROCS for shape, EON or Forge for electrostatics, Phase/Pharao for pharmacophores) leaves open the possibility of representation-metric alignment inflating apparent performance.

4. **Need to pre-specify n₁ and n₄ per sample is a practical limitation.** As acknowledged (line 216), the method requires users to specify the number of heavy atoms and pharmacophores for each generated sample. For real drug design use cases where the target molecule size is unknown, this is a nontrivial constraint. The paper does not discuss how sensitive results are to the choice of these parameters, or provide guidance on how a practitioner would set them in a discovery setting.

5. **The Vina-based hit diversification experiment, while suggestive, uses a single surrogate endpoint.** The paper honestly reports 5/7 enrichment and acknowledges Vina scores as a "weak surrogate for bioactivity" (line 250). However, the 2/7 cases where ShEPhERD underperformed random sampling are not discussed as a limitation or analyzed for patterns (e.g., was the ligand's interaction profile poorly captured by a single conformer?). Comparisons to the original PDB ligands' Vina scores would also help calibrate expectations.

### Trivial

6. None.

## Nice-to-Haves

- Comparing to prior shape-conditioned 3D generative models (Chen et al. 2023, Lin et al. 2024) on a shared single-modality task would strengthen claims of advantage.
- Validating the custom scoring functions against standard tools like ROCS (shape) and Phase (pharmacophores) would address potential circularity concerns.
- Reporting validity rates, novelty, and uniqueness in the main text (rather than only the appendix) would improve readability.
- Discussing conformational flexibility — molecules occupy an ensemble of conformations, but the paper uses single-conformer interaction profiles — would strengthen the limitations section.
- Reporting computational cost (training and inference time) would help assess practical utility.

## Removed Points

*"The Vina evaluation is too weakly controlled"* — REMOVED. The paper explicitly acknowledges Vina as a "weak surrogate for bioactivity" (line 250), the 5/7 result is honestly reported including failures, and random molecules from the training set is a standard baseline for enrichment. The critic's framing that the paper doesn't acknowledge limitations is factually incorrect.

*"Quantitative results are largely deferred to figures and the appendix"* — REMOVED. Key numbers (RMSD <0.1 Å, ≥94% graph similarity <0.2, 5/7 Vina enrichment) are reported in the main text. Distribution plots are a standard presentation format in this field. Deferring validity/novelty/uniqueness tables to the appendix is standard practice.

*"The paper should discuss computational cost"* and *"Should discuss conformational flexibility"* — MOVED to Nice-to-Haves. These are suggestions that improve completeness but are not weaknesses — the paper's scope is well-defined.

*"the assertion depends on information not present in the paper"* — The critic's claim about "circularity" being a fatal flaw is downgraded to Minor because the scoring functions are physically grounded and the paper uses xTB-relaxed geometries.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observations about missing ablations and limited baselines are standard methodological critiques that any experienced reviewer would raise, not novel insights.

## Suggestions

1. Add ablation studies comparing: (a) full joint module vs. removing local or global interaction, (b) joint training vs. separately trained single-modality models, and (c) EquiformerV2 backbones vs. simpler E3NN alternatives.
2. Include at least one direct comparison to a prior 3D shape-conditioned generative model (e.g., the method of Chen et al. 2023 or Lin et al. 2024) under a shared evaluation protocol using the same scoring functions.
3. Validate the custom scoring functions against established tools (ROCS, EON, or Phase) on a subset of generated molecules to demonstrate they correlate with accepted metrics.
4. Report the sensitivity of conditional generation quality to the choice of n₁ and n₄, and provide practical guidance for setting these parameters.

## Score and Decision

The paper introduces a genuinely novel and well-designed framework for interaction-aware molecular generation. The joint diffusion of molecular graphs with explicit shape, ESP, and directional pharmacophore representations is a clear advance in scope over prior work. The three application demonstrations are ambitious and practically motivated. However, the evaluation has significant gaps: the absence of ablations makes it difficult to attribute performance to specific architectural choices, and the lack of direct comparisons to prior interaction-conditioned 3D generative methods limits the paper's ability to substantiate its positioning as an advance. The method is promising but the evidence as presented does not fully establish its advantages over existing approaches.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Borderline</decision>