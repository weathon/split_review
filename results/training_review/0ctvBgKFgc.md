I now have sufficient evidence from the paper. Let me compose the final consolidated review.

---

## Summary

ProtComposer introduces a two-stage paradigm for controllable protein structure generation: users specify spatial layouts via 3D ellipsoids annotated with secondary structure, and a fine-tuned flow-matching model (Multiflow) fills in the backbone conditioned on these ellipsoids. The paper contributes a novel Invariant Cross Attention mechanism for injecting ellipsoid conditioning, a statistical model for generating synthetic ellipsoid layouts, and demonstrates improved Pareto frontiers for designability vs. diversity/novelty as well as improved compositional complexity (helicity closer to PDB statistics). The problem framing—bringing spatial layout control from image generation to protein design—is well-motivated and timely.

## Strengths

- **Novel representation for controllable protein generation**: The 3D ellipsoid representation provides an intermediate level of abstraction between coarse text prompts and fine-grained voxel/mesh constraints. The paper validates that this representation is expressive enough to control generation (Table 1, Figure 3) while being easy to construct and manipulate (Section 3.1, Figure 2). This is a genuinely novel contribution among protein generative models.

- **Expanded Pareto frontiers for designability vs. diversity/novelty**: By conditioning on synthetic ellipsoid layouts from a simple statistical model, ProtComposer significantly outperforms Multiflow, Chroma, and RFDiffusion in achieving higher diversity and novelty at comparable designability levels. This is evidenced by a systematic sweep across 1,750 settings with Pareto frontiers shown in Figure 4. The result that ellipsoid conditioning can shift the distribution away from oversampled helix bundles is practically valuable.

- **Improved helicity and compositionality**: Table 2 and Figure 5 demonstrate that ellipsoid conditioning reduces helicity from ~73% (Multiflow) to ~50% (closer to PDB's ~42%) and increases compositional complexity. This addresses a genuine limitation of existing unconditional generative models.

- **Well-designed adherence metrics**: The six metrics in Section 4.1 (Coverage, Misplacement, Accuracy, Likelihood, Soft Accuracy, Resegment JSD) thoughtfully capture different aspects of shape and semantic consistency between generated proteins and input layouts. This methodological contribution goes beyond what prior work provides.

- **Careful architectural design for minimal perturbation**: The Invariant Cross Attention is explicitly designed to be zero-initialized, preserving unconditional model outputs when no ellipsoids are provided (Section 3.2, Algorithms 1 and 2). This follows established principles from GLIGEN/ControlNet.

## Weaknesses

### Fatal
None.

### Major

- **The conditioning mechanism discards ellipsoid orientation, contradicting claims of orientation control.** The paper repeatedly claims control over "orientation" of substructures (abstract line 4: "control the location, size, orientation..."; Figure 6B: "Rotating the rightmost α-helix"). However, the conditioning mechanism (Section 3.2, line 60) initializes ellipsoid tokens with only SE(3)-invariant quantities—size *nₖ*, squared radius of gyration tr Σ, and secondary structure type *fₖ*—explicitly discarding the eigenvectors of the full covariance matrix Σₖ. The Invariant Cross Attention (Algorithm 1, detailed in line 312) only uses relative positions **t**ᵢ − μₖ between residue positions and ellipsoid *means*, not the ellipsoid's shape or orientation. Therefore, the model cannot distinguish between an ellipsoid elongated along the x-axis vs. the y-axis. The "rotated" generations in Figure 6B cannot be attributed to orientation conditioning from the ellipsoid covariance as described. This is not a missing ablation—the architectural choice as described does not support the claimed capability. This materially weakens one of the paper's headline contributions ("control over ... orientation").

### Minor

- **The Chroma baseline in Table 1 is insufficiently described.** The paper reports adherence metrics for "Chroma" in Table 1 but never specifies *how* Chroma was conditioned on ellipsoid layouts. Chroma uses inference-time conditioning via differentiable energy functions (Section 2, line 26); it is unclear whether the authors used unconditioned Chroma (which would be a meaningless comparison for adherence), used an ellipsoid-based energy function, or used some other procedure. While the table's main comparison is ProtComposer at different λ values (vs. oracle), the Chroma column cannot be interpreted without this information. The authors should clarify this in any revision.

- **Unbalanced comparison in the Pareto frontier analysis.** ProtComposer sweeps four free parameters (σ, γ, ν, λ) to construct its Pareto frontier, whereas Multiflow sweeps only rotational annealing (1 parameter) and Chroma/RFDiffusion sweep sampling temperature (1 parameter each). With more degrees of freedom, a better frontier is expected. The authors should at minimum fix the ellipsoid model parameters (σ, γ, ν) and vary only λ to isolate the effect of conditioning strength, demonstrating that the improvement is not simply an artifact of having more knobs to turn.

- **No quantitative diversity evaluation of synthetic ellipsoid layouts.** The paper evaluates protein-level diversity via Vendi score (Figure 4) but does not directly measure whether the synthetic ellipsoid layouts are diverse relative to PDB ellipsoid layouts (e.g., using Vendi score on ellipsoid parameters). Without this, it is unclear whether the protein diversity gains stem from the conditioning mechanism or simply from the ellipsoid model's built-in spread.

### Trivial

- Section 4.4.4.2.1 is referenced (line 235) but appears to be a formatting artifact from PDF extraction, making the sweep parameters impossible to verify from the text alone.
- Some cross-references to algorithms (Algorithm 1, Algorithm 2) refer to images rather than text, limiting verifiability.

## Nice-to-Haves

- **Comparison to alternative conditioning representations (e.g., block contact maps, coordinate constraints):** The paper motivates ellipsoids as striking an optimal tradeoff but provides no direct comparison to simpler alternatives. If the orientation issue is fixed, demonstrating that ellipsoids provide meaningfully better control than simpler alternatives (e.g., spherical constraints, secondary structure strings) would substantially strengthen the contribution.

- **Per-ellipsoid adherence metrics:** The current analysis averages over all ellipsoids. Per-ellipsoid metrics (e.g., what fraction of residues assigned to each ellipsoid fall within its Mahalanobis boundary) would reveal whether the model respects individual placements or produces globally plausible arrangements.

- **Compositionality for synthetic ellipsoids:** Adding a row to Table 2 for ProtComposer with synthetic ellipsoids (e.g., a high-designability setting from the Pareto frontier) would complete the story.

## Removed Points

- "Compositionality claim for synthetic ellipsoids is not supported": The paper explicitly shows compositionality for data ellipsoids in Table 2. The synthetic pipeline's headline benefits are diversity and novelty (Figure 4), not compositionality. The abstract promises "expanded Pareto frontiers" from synthetic ellipsoids, not specifically compositionality gains. This criticism overstates the claim.
- "Self-conditioning interpolation is unjustified": The paper already addresses this design choice (line 80-81) and explains why λX_E + (1−λ)X is used for both models. This is a reasonable explanation.
- "No comparison to alternative conditioning representations" (moved to Nice-to-Haves): Requesting comparisons to all possible conditioning methods is scope creep for a paper introducing a new representation.
- "Formatting/style nitpicks about missing appendix sections, section numbering artifacts, broken references": These are PDF extraction artifacts.
- "Missing hyperparameters": The paper states it follows Multiflow's setup (line 109). The hyperparameters are inherited from Multiflow's public checkpoint and the fine-tuning details are standard.

## Novel Insights

None beyond the paper's own contributions. The two reviews are largely aligned on the paper's strengths (novel representation, improved Pareto frontiers, good metric design) but disagree on severity of weaknesses. The key novel synthesis is recognizing that the orientation criticism, while valid and significant, does not fully invalidate the paper: location control, secondary structure control, size/shape control, and the diversity/novelty improvements are supported by the method as described and by the experiments. The compositionality criticism from the harsh reviewer is overblown—the paper's compositionality claim is supported for data ellipsoids, and the synthetic pipeline's benefits are primarily in diversity/novelty. The harsh reviewer's "unfixable" characterization of the orientation issue is too severe given that the paper has multiple other contributions that survive without orientation control. However, the paper should not claim orientation control without fixing the architectural gap.

## Suggestions

1. **Fix the orientation conditioning**: Provide the full covariance information (e.g., by encoding the three ellipsoid axes as additional token features, or by using Mahalanobis distance rather than Euclidean distance in the cross-attention). Then verify that rotating an ellipsoid's covariance actually changes the generated structure.
2. **Describe the Chroma baseline**: State explicitly how Chroma was conditioned on ellipsoids (or if it was used unconditionally, remove it from Table 1).
3. **Add an ablation fixing σ, γ, ν and varying only λ**: This would demonstrate that the improved Pareto frontier is not an artifact of having more free parameters.
4. **Add per-ellipsoid adherence analysis**: Report what fraction of residues assigned to each ellipsoid actually fall within its Mahalanobis boundary.
5. **Tone down orientation claims** or, if fixed, provide explicit quantitative evidence that orientation conditioning works.

## Score and Decision

The paper makes genuine contributions—a novel control representation for protein generation, improved diversity/novelty Pareto frontiers, and better compositional statistics—but has a significant gap between claimed capabilities (orientation control) and what the described architecture actually supports. The orientation issue is serious but not fatal to the whole paper: the remaining contributions (location control, secondary structure control, diversity/novelty improvements, compositionality improvements) are still valuable and supported by evidence. The Chroma baseline description is incomplete. These issues are addressable with architectural modifications and clarifications, but in their current form, the overclaimed orientation control weakens the paper substantially.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>