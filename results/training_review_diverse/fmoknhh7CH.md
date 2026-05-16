Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me compose the consolidated review.

## Summary

This paper presents HarmonicFlow, a flow-matching generative model for 3D protein-ligand docking that outperforms the state-of-the-art diffusion process (DiffDock) in accuracy (24.4% vs 16.3% RMSD < 2Å on PDBBind) while being simpler (direct Cartesian updates, no torsion-angle parameterization). It then extends this into FlowSite, the first deep learning solution for joint generation of ligand poses and pocket residue types for binding site design. FlowSite achieves 47.0% sequence recovery on PDBBind binding sites without ground-truth ligand structure, nearly closing the gap to an oracle (51.4%) that has access to it.

## Strengths

- **First deep learning solution for binding site design**: FlowSite is the first general DL method for designing protein pockets that bind (multi-)ligands without requiring ground-truth 3D ligand positions. Prior methods (Carbonara, FAIR) require the bound ligand structure as input. This is clearly scoped in Sections 1–2 and supported by Table 3.

- **HarmonicFlow outperforms the state-of-the-art generative docking process on pocket-level splits**: In Table 1 (PDBBind, Radius-Pocket, sequence split), HarmonicFlow achieves 24.4% of predictions with RMSD < 2Å vs. DiffDock's diffusion at 16.3%, while using simpler Cartesian coordinate updates. The paper also controls for architecture (same TFN layers) and does not use confidence model selection, so the comparison isolates the generative process.

- **First application of flow matching to real-world biomolecular tasks**: As stated in the contributions and related work (Section 2, line 44), this provides the first investigation of flow matching (vs. diffusion) for multi-ligand docking and binding site design, beyond the toy single-molecule setting of Klein et al. [2023].

- **Self-conditioned flow matching and refinement TFN layers improve performance**: Table 4 shows that self-conditioning raises best-of-5 %<2Å from 14.3% to 19.3%, and refinement TFN layers raise it from 13.0% to 19.3%. These are clean, well-controlled ablations.

- **Harmonic prior provides a useful inductive bias for multi-ligand docking**: The harmonic prior (Section 3.1, Figure 3) separates atoms of different molecules at t=0, which is especially important when multiple ligands must remain distinct. Table 4 shows Gaussian prior hurts performance (9.9% vs 11.2% top-1 <2Å).

- **Comprehensive ablations and analysis**: Table 4 systematically isolates the contributions of the harmonic prior, velocity vs. x₁ prediction, refinement TFN layers, self-conditioning, and σ=0, providing clear evidence for each design choice.

- **BLOSUM score as a more informative evaluation metric**: The paper introduces a BLOSUM-based metric (Section 4.3) that accounts for amino acid similarity, which is more meaningful than exact recovery for design tasks.

## Weaknesses

### Fatal
None.

### Major
None. The core claims (first DL binding site design, improved generative docking process, first flow matching for biomolecular tasks) are well-supported by the evidence presented.

### Minor

- **Weak baselines for multi-ligand docking (Table 2)**. The only comparison is "EigenFold Diffusion," which uses the same architecture as HarmonicFlow but predicts x₀ instead of x₁. This is essentially an ablation of the training objective rather than a competing method. While the paper acknowledges being "the first ML method for this task" (limiting baseline options), the 11.7% <2Å rate on Binding MOAD lacks external context for readers to evaluate whether the method is performing well in an absolute sense. A simple non-ML baseline (e.g., placing ligands at the pocket center with random rotations) would calibrate expectations. That said, this does not undermine the paper's central claims — the core docking contribution is validated on single-ligand data against DiffDock's diffusion.

- **Missing best-of-N results in Table 1**. Table 4 reports both average and "best of 5" performance, but Table 1 (the main comparison to DiffDock's diffusion) reports only average sample quality. Docking pipelines typically select the best pose from multiple candidates (e.g., via a confidence model). Reporting only average quality is not standard practice and makes the comparison less complete. Since both methods could benefit from best-of-N selection, this does not invalidate the comparison, but it is an omission that should be addressed.

- **Self-conditioning not compared to simpler recycling**. The paper frames self-conditioning as adapting AlphaFold2's recycling strategy (line 97: "bring AlphaFold2's successful recycling strategy to flow models"). However, the ablation (Table 4) compares only "no self-conditioning" vs. "with self-conditioning," without isolating whether the specific design choices (50% masking, gradient detachment) are necessary or whether simpler recycling (passing the previous output as input without masking or detachment) achieves similar gains. The claimed contribution is plausible but not explicitly demonstrated to be superior to simpler alternatives within the same budget.

- **Fake ligand augmentation is not ablated**. FlowSite uses fake-ligand data augmentation (Section 3.2), and the oracle baseline (GROUND TRUTH POS) also uses it. However, there is no ablation showing its individual impact on FlowSite's performance. This makes it unclear how much of the improvement comes from the augmentation vs. the flow model.

- **Euler solver step size not specified**. The paper states "We use an Euler solver" (line 86) but does not specify ∆t or the number of integration steps, which is needed for reproducibility and for comparing computational cost with DiffDock's diffusion.

- **No runtime or computational cost comparison**. The paper claims "simplicity" and "generality" for HarmonicFlow relative to DiffDock's diffusion but provides no wall-clock time or FLOPs comparison. A rough runtime comparison would substantiate this claim.

### Trivial

- The description of how the self-conditioning input x̃₁ᵗ is used to parameterize equivariant messages (Section 3.3) is somewhat terse. The paper states distances from x̃₁ᵗ are used to "parameterize the tensor products" but does not fully detail the mechanism — this could be clarified.
- The sensitivity of the pocket-definition noise parameters (σ=0.5 for distances, σ=0.2 for pocket center) is not analyzed.

## Nice-to-Haves

- **Confidence intervals or bootstrapped standard errors** for the main results (Tables 1–4) would strengthen confidence in the reported differences, given the stochastic nature of generative models.
- **Sensitivity analysis** of the noise magnitude in pocket definitions (σ parameters) and the impact of fake ligand augmentation would further strengthen the results.
- A comparison between the self-conditioning procedure and simpler recycling (without masking/detachment) would directly demonstrate the value of the specific design.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about missing architectural details (number of refinement layers K, GAT layers, feature dimensions not in main text)* — Removed because the paper's appendix (stripped by the parser) likely contains these details. The hard rule forbids penalizing missing appendix content.
- *Criticism about unclear description of how intermediate refined coordinates update node features* — The paper does describe (line 126-128) that the self-conditioning input x̃₁ᵗ provides interatomic distances used to parameterize tensor products for equivariant messages. While the description could be clearer, the mechanism is explained.
- *Criticism questioning DiffDock comparison fairness* — The paper explicitly states both methods use the same architecture and neither uses confidence model selection. The comparison is fair as a comparison of the generative processes.

## Novel Insights

The reviews surface one insight beyond the paper's own contributions: the observation that because FlowSite's self-conditioning is directly adapted from discrete-diffusion self-conditioning (Chen et al., 2023) to the flow-matching setting, a natural baseline would be to compare it against standard AlphaFold2-style recycling (without masking and gradient detachment). The reviews correctly identify that the current ablation does not isolate whether the *specific* self-conditioning procedure is necessary or whether the gains come from iterative refinement in general. This is a well-posed future ablation experiment.

## Suggestions

1. Add a "best of 5" or "best of 10" column to Table 1 to match the standard practice in docking evaluation.
2. Include at least one simple non-ML baseline for multi-ligand docking (e.g., random pose, or centroid placement with random rotation) to contextualize the 11.7% <2Å rate.
3. Specify the Euler solver step size / number of integration steps in the main text.
4. Provide a controlled ablation comparing self-conditioning to simpler recycling (without masking or detachment) to isolate the contribution of the specific design choices.
5. Add an ablation showing the impact of fake-ligand data augmentation on FlowSite's performance.

## Score and Decision

The paper presents a well-motivated method for an important problem. HarmonicFlow demonstrates a genuine improvement over DiffDock's diffusion for generative docking on pocket-level splits, and FlowSite provides the first deep learning solution for binding site design without requiring ground-truth ligand poses. The contributions are real, the experiments are well-designed, and the ablations are informative. The weaknesses are all minor and addressable — they do not threaten the core claims. The paper is a solid contribution to the field.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>