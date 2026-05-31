## Summary

SIGMADOCK is an SE(3) Riemannian diffusion model for molecular docking that decomposes ligands into rigid-body fragments rather than employing torsional diffusion. The central insight is that breaking rotatable bonds yields rigid substructures whose poses can be independently parametrised as SE(3) transformations, producing a factorised product-space diffusion process that is better-conditioned than torsional models. Three key contributions drive performance: (1) a fragment-reduction scheme FR3D that merges adjacent fragments to reduce degrees of freedom, (2) soft triangulation constraints that enforce bond-angle priors across fragment boundaries without restricting dihedral freedom, and (3) an SO(3)-equivariant EquiformerV2-based architecture with virtual nodes and smooth edge decay. Experimentally, SIGMADOCK achieves 79.9% Top-1 PB-valid success on PoseBusters, compared to 12.7–32.8% for recent deep learning approaches, and is claimed to be the first DL method to surpass classical physics-based docking on the intended temporal split.

---

## Strengths

- **Dramatic empirical advance**: 79.9% Top-1 PB-valid on PoseBusters represents a 2.4–6.3× absolute improvement over competing DL approaches (12.7–32.8%), and surpasses physics-based Vina (~56%) for the first time among DL methods under the intended train-test split. The result holds across sequence similarity bins (72% for <30% identity), directly countering the memorisation critique.

- **Sound theoretical motivation**: Theorem 1 formalises precisely why torsional models are poorly conditioned—torsion-to-Cartesian mappings break the product structure of the noise kernel, coupling degrees of freedom and creating gauge ambiguities. The fragment formulation restores factorised Haar measures on SE(3)^m, yielding a theoretically cleaner SDE. This is more than a post-hoc rationalisation; it predicts and explains the empirical gap.

- **Careful justification of the conformational manifold assumption**: Section 2.2.1 empirically shows that Kabsch + torsional alignment of RDKit conformers to bound poses yields RMSD well below 2 Å, providing a necessary and non-trivial validation that fragment sampling from M_c does not fall out of distribution.

- **Comprehensive ablations**: Table 1 isolates the contribution of each component—triangulation conditioning (+8.8%), protein-ligand interactions (+3.6%), fragment merging (+6.1%), energy-based ranking (+13.3%)—with re-training for the architecture ablations (A–C), making the claims credible.

- **Competitive with co-folding models at negligible cost**: Achieving 79.9% vs. AF3's 80.2% PB-valid with 19k training points, 50× faster sampling, and lower train-test leakage is a compelling data-efficiency argument for principled geometric inductive biases over scale.

- **Invariance/equivariance theorem**: Theorem 2 proves the training objective and sampler are invariant to the choice of local coordinate axes for fragment orientation, resolving a fundamental ambiguity in the SE(3)^m parametrisation, and ensuring the score model is SO(3)-equivariant.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Energy-scoring heuristic contributes ~13% absolute performance**: Ablation Row D shows that removing energy/physicochemical scoring drops Top-1 from 80.5% to 67.2% (RMSD) and from 79.9% to 66.1% (PB-valid). This is the largest single ablation gap in Table 1—larger than any architectural component. The paper describes this heuristic only vaguely in the main text ("pseudo binding energy … physicochemical checks") and delegates the full procedure to the appendix. Because the headline claim pivots on 79.9% and the heuristic contributes a disproportionate share, the main text should fully specify the scoring pipeline so readers can assess whether the gain is attributable to the diffusion model or the downstream ranker. Competing methods should also be evaluated with a similar re-ranking budget for a fair comparison.

2. **Sparse baseline comparison for the stated claims**: The paper compares against DiffDock and variants, but the "state-of-the-art among DL methods" claim at the time of writing could be contested by more recent non-torsional approaches (e.g., Uni-Mol2, FABind+, PLANTAIN, RoseTTAFold-AA docking). The paper should either include these or explicitly justify why the selected baselines bound the state-of-the-art. The current framing risks overstating novelty if peer methods already outperform the 12.7–32.8% baseline band.

### Minor

1. **FR3D stochastic search not ablated for fragmentation variance**: FR3D performs a stochastic search producing different fragmentation realisations. While the paper notes this as a data-augmentation avenue, it does not report variance over fragmentation choices or quantify how much of the improvement comes from augmentation vs. merging per se.

2. **AF3 comparison framing**: Table 4 compares SIGMADOCK and AF3 on the PB set but these models operate under fundamentally different paradigms (re-docking with known pocket vs. co-folding from sequence), trained on different data, evaluated under different leakage conditions. While the paper qualifies this, the direct numeric juxtaposition in the same table could mislead readers into concluding the models are interchangeable for practical use.

3. **Pocket definition sensitivity vs. Vina**: Table 3 shows SIGMADOCK performance drops to 69.8% at d_0 = 7Å pocket cutoff. The analysis notes Vina's Top-1 does not improve with tighter pockets, but no Vina numbers at matching d_0 values are shown, leaving the relative performance gap at larger pockets uncharacterised.

### Trivial
None worth noting.

---

## Nice-to-Haves

- Providing the full pseudo-code (or compact formula) for the energy/physicochemical ranking heuristic in the main text would substantially aid reproducibility and allow readers to fairly attribute performance to the generative model vs. the ranker.
- A brief quantitative comparison of inference wall-clock time vs. baselines (not just "50× faster than AF3") would be useful for practitioners evaluating HTVS applicability.
- Including results for DiffDock-L and any non-torsional contemporary DL baselines would strengthen the "state-of-the-art" claim.

---

## Novel Insights

The key novel insight is the formal identification of torsional diffusion's conditioning pathology: torsion-to-Cartesian maps induce non-product, entangled measures in the observation space that break score factorisation and introduce gauge ambiguity, whereas rigid-body fragmentation restores a product of Haar measures on SE(3)^m, yielding a cleaner and better-conditioned learning problem. This reframing—from "torsional models as low-DoF approximations" to "torsional models as ill-conditioned mappings"—provides a principled explanation for the persistent empirical gap between the theoretical promise and practical performance of torsional methods, and offers a concrete path forward via fragment-level SE(3) diffusion. The triangulation conditioning scheme is a particularly elegant mechanism that re-introduces bond-angle priors without restricting dihedral freedom, effectively recovering some of the DoF savings of torsional models while retaining the product structure of the fragment diffusion.

---

## Suggestions

1. Provide full specification of the energy-ranking heuristic in the main text and apply it consistently to baseline comparisons, or explicitly report SIGMADOCK's performance without ranking (Row D) alongside ranked results to allow isolated evaluation of the generative model.
2. Add a wall-clock timing table comparing SIGMADOCK to DiffDock-L and Vina under matched hardware to substantiate HTVS applicability claims.
3. Report inter-run variance of FR3D to clarify how much performance depends on fragmentation choice vs. architecture.
4. Consider including a forward pass analysis (score function conditioning numbers or loss curves) to empirically demonstrate the claimed improved conditioning over torsional baselines.

---

## Score and Decision

SIGMADOCK represents a genuine and substantial advance. The theoretical grounding of its fragment-space SE(3) diffusion, the empirical scale of the improvement over prior DL methods (nearly 2.5–6× improvement in PB-valid success), the first DL surpassing of classical physics-based docking, and the competitive positioning against vastly larger co-folding models—all under principled, reproducible experimental conditions—qualify this as a high-quality contribution to the ML and computational chemistry communities. The weaknesses are real but not fatal: the energy-ranking heuristic warrants more explicit treatment, and the baseline comparison could be broadened. These are straightforward issues that do not undermine the core contribution.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>