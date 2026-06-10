## Summary

This paper introduces Geometric Bayesian Flow Networks (GeoBFN), which adapts Bayesian Flow Networks—a recently developed generative modeling framework operating in parameter space rather than sample space—to 3D molecule generation. The method models continuous coordinates, discretized atom charges, and discrete atom types within a unified probabilistic framework with proven SE(3) invariance. Empirically, GeoBFN achieves SOTA or competitive results on QM9 and GEOM-DRUG unconditional and conditional generation benchmarks, and its continuous-time training objective enables any-step sampling (e.g., 20× speedup with 50 steps at competitive quality).

## Strengths

- **First principled adaptation of BFN to 3D molecular geometry with proven SE(3) invariance.** The paper derives concrete conditions (Theorem 3.1) under which the BFN likelihood and ELBO become SE(3) invariant, and implements these conditions via an EGNN parameterization of the inter-dependency network Φ (Eq. 12). This is a non-trivial extension—prior molecule generation models (EDM, GeoLDM) are diffusion-based, and the BFN parameter-space formulation requires different equivariance reasoning than sample-space diffusion.

- **Strong quantitative results across both benchmarks.** GeoBFN reports 90.87% molecule stability on QM9 and 85.6% atom stability on GEOM-DRUG at 1k sampling steps (Table 1), with improvement to 94.25% at 4000 steps (Fig. 4). On conditional generation (Table 2), GeoBFN improves over baselines across all six QM9 properties (α, εHOMO, εLUMO, Δε, μ, Cv), a consistent improvement pattern that is more compelling than selective metric wins.

- **Any-step sampling with demonstrable speed-quality trade-off.** Because the continuous-time loss (Eq. 19) decouples training from the number of sampling steps, GeoBFN can generate with as few as 50 steps while remaining competitive with baselines requiring hundreds of steps. The paper quantifies this: 20× speedup with 50 steps while matching or exceeding EDM-level performance (Table 1, Fig. 4). This is a concrete operational advantage over EDM (1000 steps) and GeoLDM.

- **Identifies and empirically resolves a discrete-variable sampling pathology.** Section 3.4 pinpoints a genuine mode-redundancy failure in BFN sampling for discretized variables (boundary clamping in the CDF causes probability mass to concentrate on edge bins). The proposed NEAREST_CENTER fix (Eq. 20) is validated empirically in Fig. 5 and the ablation study (Table 3). While the theoretical analysis is thin (see Weaknesses), the problem identification and practical solution are valuable contributions.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Chemically inaccurate claim about charge-type mapping.** The paper states (Section 3.4) that "h_t and h_c variables have a one-to-one mapping, e.g., the charge value 4 could be uniquely determined as the Carbon atom." This is not a one-to-one mapping; it only shows one direction. Multiple atom types in QM9 (H, C, N, O, F) can carry the same formal charge (e.g., all neutral atoms have charge 0). The example given does not suffice to establish a one-to-one mapping, and the paper provides no analysis of the actual mapping in the datasets used. This claim is used as justification for discarding atom types, though the empirical ablation (Table 3) provides independent evidence that the approach works. The text should be corrected to remove the inaccurate claim and instead rely on the empirical results.

- **The NEAREST_CENTER fix is empirically validated but lacks theoretical analysis.** The paper asserts that the fix is "unbiased towards the training objective" (line 245) without providing any justification, proof, or analysis of bias. The approach—deterministically snapping a weighted average to the nearest bucket center during sampling—mixes probabilistic training with a deterministic post-processing step. While the empirical results (Fig. 5, Table 3) suggest the fix works, the paper does not analyze whether it introduces its own biases, affects diversity, or could fail in edge cases. A brief formal characterization would strengthen the paper significantly.

- **The modality configuration for main results is not explicitly stated.** The evaluation protocol (Section 4.1) says bond types are predicted "based on pair-wise atomic distance and atom types," which requires knowing atom types. Section 3.4 shows GeoBFN *can* operate without atom types (x + h_c only), but the paper never states which configuration was used for the headline results in Tables 1 and 2. If the main results use all three modalities (x + h_c + h_t), this is a simple reporting gap. If they use only x + h_c, the evaluation pipeline for bond prediction would need clarification. The authors should state this explicitly.

- **The variance reduction claim for parameter space lacks direct evidence for molecule data.** The paper argues that operating in BFN's parameter space yields "considerably lower" variance than diffusion's sample space (Section 3.3), citing Graves et al. (2023) and showing qualitative trajectories (Fig. 3). However, no quantitative comparison of variance between BFN and diffusion coordinate trajectories on the same molecular data is provided. This would substantially strengthen the central conceptual argument.

- **Training hyperparameters and model architecture details are absent.** The paper does not report EGNN depth, hidden dimension, number of parameters, learning rate, batch size, training steps, or compute budget. For a paper presenting new architectural work, this information is essential for reproducibility and fair comparison.

- **No confidence intervals or run-to-run variance reported.** For generative models on datasets as small as QM9 (~130K molecules), single-run results can be misleading. While this is standard practice in the subfield (EDM, GeoLDM also omit CIs), reporting them would substantially strengthen reliability.

### Trivial

None.

## Nice-to-Haves

- Provide a direct empirical comparison of variance between the BFN parameter trajectory and a diffusion sample trajectory (e.g., EDM) on the same QM9 molecule during generation, measured quantitatively rather than only qualitatively in Fig. 3.
- Report confidence intervals or standard deviations for all main metrics across multiple random seeds.
- Add training details (architecture, hyperparameters, compute) to improve reproducibility.

## Removed Points

- **Criticism about baseline numbers appearing only in images (Tables 1, 2)**: This is standard formatting in ML papers where tables are rendered as figures. Not a scientific weakness. Removed as a formatting/style nitpick.
- **Criticism about proofs being deferred to appendix**: Standard practice. Removed.
- **Criticism about "comparing with methods that do not correspond to currently available systems"**: All cited baselines (EDM, EDM-Bridge, GeoLDM) are published and/or have code available. Removed per Hard Rules.
- **"The paper inherits a large amount of formalism from prior work"**: This is how methodology papers work. Removed.
- **Strength about addressing "an important problem"**: Generic. Removed.
- **Strength about "paper is well-written"**: Generic. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Correct the chemically inaccurate "one-to-one mapping" claim in Section 3.4. Instead of asserting this, simply state that the ablation empirically shows discarding h_t can work with the discretized charge representation.
2. Explicitly state which modality configuration (x+h_c+h_t or x+h_c) was used for the headline results in Tables 1 and 2, and clarify how bond prediction is handled without atom types if that setting was used.
3. Add a brief formal analysis of the NEAREST_CENTER fix—at minimum, characterize whether it introduces bias relative to the training objective, or replace the unsupported "unbiased" claim with a more measured description.
4. Include direct quantitative evidence (a plot or table) comparing parameter-space variance vs. sample-space variance for molecular coordinate trajectories.
5. Add a reproducibility section with training hyperparameters, model architecture details, and compute budget.

## Score and Decision

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>