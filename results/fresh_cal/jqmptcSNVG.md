Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces PepHAR, a three-stage autoregressive generative model for peptide binder design that explicitly separates "hot-spot" residues (functionally critical) from "scaffold" residues (structural). The pipeline consists of: (1) sampling hot-spot residues via an energy-based model with Langevin MCMC, (2) autoregressively extending fragments using von Mises-distributed dihedral angles to enforce peptide bond geometry, and (3) a correction stage that refines fragment assembly via gradient-based optimization. The paper also proposes a scaffold generation task where known hot spots are fixed and the model must complete the peptide. Experiments on peptide design and scaffold generation show competitive performance against RFDiffusion, PepFlow, and PepGLAD.

## Strengths

1. **Hot-spot-driven generation is biologically motivated and methodologically novel.** The paper identifies that existing generative models (PepFlow, RFDiffusion) treat all residues equally, whereas PepHAR separates hot-spot and scaffold residues into distinct generation stages (Section 4, Algorithm 1). This distinction explicitly addresses the challenge that "not all residues contribute equally" to binding, which is grounded in the protein design literature.

2. **Correction stage uses learned distributions rather than hand-crafted energy functions for fragment assembly.** The optimization objective (Eq. 13–15) combines a backbone consistency term and a dihedral likelihood term, both parameterized by learned networks from the first two stages. The ablation study (Table 3) shows this stage substantially improves affinity and stability, demonstrating a practical refinement method that goes beyond traditional empirical force fields.

3. **Introduction of a scaffold generation task that mirrors real drug-discovery workflows.** The paper describes a new experimental setting (Section 5.2) where known hot-spot residues are fixed and the model must scaffold them into a complete peptide. This is more realistic than unconditional de novo design and is a genuine practical contribution — PepHAR achieves the best SSR and BSR scores on this task (Table 2), and the paper demonstrates that baseline methods like RFDiffusion and PepFlow benefit little from the same conditioning.

4. **Autoregressive extension via von Mises distributions explicitly enforces peptide bond geometry.** By modeling dihedral angles as a product of von Mises distributions (Eq. 7–9), PepHAR naturally respects the circular nature of angles and the planar constraint of peptide bonds. The ablation confirms that removing this modeling degrades all metrics, validating the design choice.

5. **Competitive quantitative performance with strong novelty and diversity.** The reported metrics (Table 1) show PepHAR achieving a high valid rate, competitive RMSD, SSR, and affinity, while producing the highest novelty and diversity scores. The scaffold task results (Table 2) show PepHAR significantly outperforming baselines on SSR and BSR.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline adaptation for scaffold generation is insufficiently described, making comparisons potentially unfair.** For RFDiffusion and ProteinGenerator, the paper states only that "the known hot spot residues are provided as an additional condition, along with the target" (line 236). RFDiffusion's native conditioning mechanism is via a target protein structure, not arbitrary residue-level conditioning. How this was implemented — and whether the adaptation was validated to work correctly — is not described. For PepFlow, the ODE sampling is modified to fix hot spots, but re-initialization details are omitted. If RFDiffusion was inadequately adapted to the conditioning, the comparison may be misleading (PepHAR's apparent advantage in SSR and BSR may partly reflect the baseline's inability to incorporate the condition rather than PepHAR's scaffolding skill). This is a **methodological gap** that must be addressed.

2. **The ablation study covers only the de novo design task, not the scaffold generation task.** The paper's claimed practical contribution is the scaffold generation setting, yet the ablation (Table 3) examines the effects of removing hot spots, von Mises modeling, and the correction stage only for de novo design. It is unknown whether these components are equally essential when hot spots are given a priori. Since the scaffold task is the paper's distinguishing contribution, this is an **evidential gap** that weakens the claim that these components are crucial for realistic scenarios.

### Minor

1. **No statistical uncertainty quantification.** Results in Tables 1 and 2 are reported as single point estimates without standard deviations, confidence intervals, or evidence of multiple runs. Generative models exhibit variance across random seeds, extension orders, and hot-spot initialization. Without any measure of variability, it is difficult to assess whether reported advantages are reliable.

2. **NCE objective formulation is unconventional and insufficiently justified.** Equation 2 combines a softmax normalization over residue types with a noise density term in the denominator, and treats the noise distribution as a fixed constant class. This is not the standard binary NCE formulation (which uses logistic regression to discriminate data vs. noise). The paper refers to this as "NCE" but the presented equation is a hybrid softmax-with-noise-class objective. The formulation may be valid, but its relationship to standard NCE and its theoretical justification are not explained. This needs clarification.

3. **No convergence analysis or step count for Langevin MCMC sampling.** The founding stage (Section 5.1) uses Langevin MCMC "starting from an initial guessed position and orientation" (line 119). How many steps are used, what constitutes a good initial guess, and whether the chain converges are not specified. Since the EBM is trained via NCE (which can produce poorly calibrated densities far from data), basic diagnostics would help establish that sampled hot spots are realistic.

4. **Missing implementation details for the correction stage.** The hyperparameters λ_bb and λ_ang (Eq. 13) are declared but their values are never given. The stopping criterion for iterative refinement is not stated. This makes the correction stage difficult to reproduce.

5. **Fragment merging after extension is underspecified.** Algorithm 1 states "Merge fragments into the peptide" but does not specify how overlaps, gaps, or ordering conflicts between independently grown fragments are resolved. While the correction stage later adjusts structures, the initial merge strategy should be defined precisely for reproducibility.

6. **Directional masking in the extension network is described only at a high level.** The paper states that "if direction is Left, residues can only attend to their neighbors on the right" (line 151), but the implementation of these masks within IPA attention is not detailed. Since data leakage could occur if the model attends to residues in other fragments that are far in sequence but structurally nearby, the masking scheme needs explicit specification.

7. **Many training hyperparameters are omitted.** Learning rate, batch size, number of NCE noise samples, Langevin step count, number of correction iterations, and optimization details for the correction stage are not reported. The number of hot spots is given as K=1–3 but without explaining how this is chosen per target.

### Trivial
None.

## Nice-to-Haves
- Reporting per-cluster performance for the 10 test clusters to demonstrate that results are not driven by a single cluster.
- Visualizing the distribution of Cα distances between consecutive residues for generated peptides, to directly show that peptide bond geometry is satisfied.
- Including a Ramachandran plot analysis for generated peptides.
- Reporting computational cost (runtime per stage).

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"PepHAR's valid rate (54.8%) is far below RFDiffusion (99.1%) and PepFlow (67.1%)" + associated claim that this contradicts the method's design.** These specific numbers (54.8%, 79.5%, 49.4%, 67.1%, 99.1%) do not appear in the parsed paper text and cannot be verified. They also directly contradict the strength finder's reading (98.1% Valid for PepHAR on the design task) and the paper's own textual claim that PepHAR "ensures the production of valid peptides." The related criticism that a 5.4Å RMSD is high is similarly unverifiable from the parsed text. — *Removed because the numerical claims are unverifiable from the paper text and contradict the paper's descriptive narrative.*

2. **"Missing related works" (autoregressive protein generation methods).** This criticism speculates about missing references that the reviewer cannot confirm. — *Removed per hard rule.*

3. **"The ablation conflates two effects" (random hot spots vs. no hot-spot stage).** The ablation replaces sampled hot spots with random residues, which is a perfectly reasonable design to test whether learned hot-spot sampling matters. The paper does not claim this ablates the entire hot-spot stage concept; it tests the quality of sampled hot spots. — *Removed as misunderstanding of the ablation design.*

4. **"No Ramachandran plot or bond geometry analysis."** This demands more extensive structural analysis than is standard for a submission; the "Valid" metric already measures Cα distances. — *Downgraded to nice-to-have.*

5. **"Generating all residues in one step may be inefficient — unsupported claim."** This is stated as a motivation/intuition in the Introduction, not as a rigorous experimental claim. Evaluating efficiency is outside scope. — *Removed as scope creep.*

6. **"The paper does not discuss prior work on autoregressive protein generation."** This is a related-work criticism that is unverifiable and would require knowledge of all papers in the field. — *Removed per hard rule.*

7. **Various reproducibility nitpicks (complete training logs, large artifacts).** These are trivial or impractical to include. — *Removed per hard rule.*

## Novel Insights
The reviews do not surface a genuinely novel observation beyond the paper's own contributions. The core insight — that hot-spot and scaffold residues should be treated via separate generation stages, with autoregressive extension using von Mises-distributed dihedral angles — remains the paper's original contribution, and the reviewers' analyses do not add a new lens or reframe this contribution in a way not already in the paper.

## Suggestions
1. **Describe the RFDiffusion/PepFlow baseline adaptation in detail.** Provide the exact procedure for conditioning RFDiffusion on hot-spot residues, and validate that the adapted baseline works correctly on a simple test case.
2. **Add error bars.** Run at least 3 seeds for each configuration and report means ± std for all metrics.
3. **Extend the ablation to the scaffold generation task.** Show whether the correction stage, von Mises modeling, and learned hot-spot sampling still matter when hot spots are given as ground truth.
4. **Clarify the NCE formulation.** Explain why the softmax-over-types is combined with a noise class, and how this relates to standard NCE. Provide the exact equation for negative samples as well.
5. **Report hyperparameters.** Include λ_bb, λ_ang, Langevin step count, correction iterations, learning rate, batch size, and how K (number of hot spots) is selected per target.

## Score and Decision

The paper presents a well-motivated, technically sound approach with a novel pipeline architecture that separates hot-spot and scaffold residue generation. The scaffold generation task is a practical contribution. The main weaknesses are: incomplete description of how baselines were adapted for the scaffold task (which could affect the fairness of comparisons), ablation limited to the de novo task, and the absence of error bars for any metric. These issues are fixable but nontrivial. The core methodology remains promising, and the results appear competitive.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>