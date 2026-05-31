## Summary

MolMiner is a fragment-based, geometry-aware, order-agnostic autoregressive generative model for inverse molecular design. The model assembles molecules from ring and bond fragments via a transformer architecture augmented with Gaussian-decay spatial attention biases and dynamic forcefield-based geometry relaxation during generation. A GMM-based marginal prior enables probabilistic completion of unspecified conditioning properties, allowing users to control any subset of twelve physicochemical targets (logP, QED, SAS, MW, TPSA, MR, HBD, HBA, ring count, rotatable bonds, chiral centers, FractionCSP3). The paper also proposes Wasserstein-based distributional metrics and calibration plots as improved evaluation protocols.

---

## Strengths

- **12-property simultaneous conditioning** is the paper's most distinctive contribution. No prior fragment-based autoregressive model controls this breadth of properties at once; the probabilistic GMM-based partial-conditioning mechanism is simple, practical, and well-motivated.
- **Symmetry-aware fragment attachment** is a genuine methodological contribution. The cyclic-permutation standardization via Morgan/Tanimoto similarities addresses a concrete correctness gap that prior work (e.g., MoLeR) left unresolved; it is carefully described and properly motivated.
- **Dynamic forcefield relaxation** during generation (not just initialization) is meaningfully different from the frozen-geometry approach of G-SchNet and is a sensible design choice that keeps intermediate conditional predictions geometrically realistic.
- **Improved evaluation protocol**. Proposing Wasserstein distances for property-distribution comparison and calibration plots (target vs. predicted) as standard conditional-generation metrics is a useful contribution to the community beyond the model itself.
- **Order-agnostic rollouts as regularization** is empirically confirmed via ablation (Sec. 4.1 and Appendix A.3), lending support to a design choice that could otherwise seem arbitrary.

---

## Weaknesses

### Fatal
None. The core claim (calibrated multi-property conditional generation) is substantiated by the calibration plots in Figure 2.

### Major

1. **Severely limited baseline comparison.** The only competitive baseline in the main quantitative table is HierVAE (2020). MolMiner underperforms it across the majority of properties (10 of 12 Wasserstein distances are larger for MolMinerD, and the gap for molecular weight — 47 vs. 15 — is large). No newer models (MolGPT, REINVENT, recent diffusion-based models) are compared. For conditional generation — the central claim — there is *no comparison* to any other model at all; the evaluation is purely self-referential calibration plots. This makes it impossible to assess whether the claimed advance over the state of the art is real.

2. **QED and molecular weight control failures.** QED is explicitly acknowledged as a failure case, and molecular weight exhibits systematic bias (hypothesized as premature termination). These are arguably the two most practically important molecular design targets (drug-likeness and size control). Failures here undermine the headline claim of calibrated 12-property control without a clear resolution or quantification of the failure extent.

3. **Single dataset, small scale.** All experiments are conducted on the ~200k ZINC subset from ChemicalVAE. No evaluation on GuacaMol, MOSES, or ChEMBL benchmarks is performed, making generalization claims speculative. 200k molecules is also modest by current standards, raising questions about whether conclusions transfer to realistic industrial-scale settings.

4. **No multi-property simultaneous conditioning experiment.** The calibration plots in Figure 2 evaluate each property individually — i.e., one property is swept while the remaining eleven are drawn from the GMM. No experiment demonstrates that two or more properties can be jointly controlled simultaneously (e.g., constraining both MW and logP at once), which is the core use case advertised for HTS pipelines. This is a significant omission given the paper's primary claim.

### Minor

1. **Starting fragment predictor design is underexplained.** The auxiliary fragment predictor is a multi-label BCE classifier, but it is unclear how this interacts with conditioning at test time, how sensitive generation quality is to the seed fragment choice, and what happens when the predictor selects a fragment inconsistent with the conditioning vector.

2. **Termination bias is identified but not resolved.** The early-termination hypothesis for MW/TPSA/MR bias is reasonable, but the paper proposes remedies (termination rebalancing, RL fine-tuning) without testing them. Reporting an unresolved systematic bias in the most important physical-size properties weakens the paper.

3. **64 attention heads is unusually large** for an 8-layer transformer over fragment-level tokens. The ablation in Appendix A.3 is referenced but not shown in the main body; a brief discussion of why this configuration was chosen would be helpful.

4. **GMM quality for 12-dimensional distribution is not evaluated.** The GMM-based imputation of missing properties is a core component of the conditioning pipeline, yet its quality is only described in Appendix A.2 without a clear quantitative demonstration of calibration fidelity.

### Trivial

- The termination action imbalance in order-agnostic rollouts is a known issue in similar models (e.g., MADE/NADE). Connecting this to prior work would add perspective.

---

## Nice-to-Haves

- Add a joint two-property conditioning experiment (e.g., fix MW and logP simultaneously) to directly demonstrate multi-property control.
- Include a comparison against at least one recent conditional molecular generation method (e.g., LIMO, MolGPT, or a conditioned diffusion model).
- Evaluate on MOSES or GuacaMol to allow community benchmarking.
- Report generation time per molecule vs. baselines, especially since forcefield relaxation is applied at every step.

---

## Novel Insights

The most genuinely novel observation is the interaction between order-agnostic rollout and termination frequency: because any open attachment site can serve as a focal point, the fraction of termination actions in training data scales with the total number of open sites visited across all orderings, biasing the model toward early termination. This is a new architectural failure mode specific to order-agnostic fragment-based generation (distinct from atom-based or fixed-order models) and the paper is the first to clearly articulate it. The cyclic-permutation symmetry standardization via Morgan fingerprints is also a practically important and underappreciated contribution to fragment-based generation more broadly.

---

## Suggestions

- Run a controlled ablation in which two or three properties are simultaneously constrained and report the resulting Wasserstein distances for *all* twelve properties, to quantify multi-property crosstalk.
- Address the termination bias by reweighting termination actions during training (trivially implementable) and report the effect on MW/TPSA calibration.
- Add at least one recent conditional generative model as a baseline; if exact replication is infeasible, use published numbers from MOSES or GuacaMol leaderboards with caveats.
- Include generation speed (seconds/molecule) for MolMiner and HierVAE so practitioners can assess scalability to HTS scenarios.

---

## Score and Decision

MolMiner introduces a meaningful combination of ideas — symmetry-aware fragment attachment, dynamic 3D geometry, order-agnostic rollouts, and 12-property conditioning — and the calibration framework is a useful community contribution. However, the evaluation is substantially incomplete: only one outdated baseline is shown in the unconditional table (where MolMiner performs worse), conditional generation has no competing methods, the primary use case (simultaneous multi-property control) is not demonstrated, and results are confined to a single small dataset. The paper reads more like a system/engineering report than a rigorously validated scientific contribution. The ideas are sound and the implementation is careful, but the empirical case for the stated claims is too thin for acceptance at this stage.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>