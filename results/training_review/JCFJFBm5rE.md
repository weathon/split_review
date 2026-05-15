Now I have sufficient information. Let me carefully construct the consolidated review.

---

## Summary

The paper proposes SurfDesign, a surface-conditioned protein design framework that combines geometric features from molecular surfaces (normal vectors, pseudo-curvatures) with knowledge from pretrained protein language models via a proposed "surface-based equivariant message passing" (SEMP) and "hybrid parameter-efficient fine-tuning" (PEFT). The method is evaluated on CATH 4.2/4.3, TS50, TS500, and PDB benchmarks, reporting average recovery rates exceeding 70% and substantially outperforming prior methods.

## Strengths

- **Timely and well-motivated problem direction**: Surface-conditioned protein design is genuinely under-explored compared to backbone-conditioned inverse folding, and the paper provides a clear motivation for why surface geometry (beyond backbone coordinates) matters for functional protein design. The introduction builds a coherent case that molecular surfaces carry information about biochemical properties (charge, hydrophobicity) that backbone-only methods miss.

- **Extensive empirical scope**: The paper evaluates across five benchmarks (CATH 4.2, CATH 4.3, TS50, TS500, PDB multi-chain) with comparisons to a broad set of baselines including both GNN-based (ProteinMPNN, PiFold, GVP) and PLM-based (ESM-IF, LM-Design, VFN-IF-ESM, InstructPLM) methods. The ablation study (Section 3.4) quantifies the contribution of surface geometry features and PLM knowledge.

- **Analysis by structural context provides useful insight**: Figure 4's breakdown by SASA and interaction interface shows where SurfDesign improves over structure-based LM-Design—particularly on surface-exposed and loop regions where backbone-only methods struggle. This directly supports the paper's motivating claim that surface conditioning helps where sequential/backbone information is weakest.

- **Self-consistent structure recovery evaluation**: The use of scTM and scRMSD (Table 6) goes beyond simple sequence recovery to verify that designed sequences actually fold into the target structure, providing a meaningful quality check.

## Weaknesses

### Fatal
None.

### Major

1. **Core technical contributions (SEMP and hybrid PEFT) are named but not technically described.** The paper's two claimed innovations—surface-based equivariant message passing and a hybrid PEFT technique—are mentioned in the abstract, introduction, and figure captions, but the method section (Sections 2.1–2.2) contains no equations, update rules, or architectural details for either. SEMP is not defined: there are no message update equations, no aggregation scheme, no specification of whether the equivariance is SE(3) or E(3), and no proof or citation establishing the equivariant property. The hybrid PEFT technique is never explained: no adapter architecture, no description of which PLM layers are frozen vs. tuned, and no details on how surface encoder features are integrated with PLM representations. Figure 2 shows a "structural adapter" in a diagram, but the text never describes it. Because the claimed contributions are underspecified, the paper cannot be evaluated as a technical work—the reader cannot assess novelty, correctness, or reproducibility. This is the most consequential weakness.

2. **Reported results substantially exceed prior work without sufficient verification.** SurfDesign reports 74.13% recovery on CATH 4.2 and 82.16% on TS50—levels dramatically above prior methods (e.g., VFN-IF-ESM at ~53–55% on CATH 4.2). An improvement of 20–30 absolute percentage points over strong baselines trained on the same data is extraordinary and would require: (a) error bars or variance metrics across multiple runs (none reported), (b) direct verification that training splits and evaluation protocols match the baselines exactly (only stated, not demonstrated), and (c) an explanation for how a surface-conditioned model so dramatically outperforms structure-conditioned models on tasks that are traditionally structure-conditioned. The zero-shot generalization numbers on TS50/TS500 (82.16%, 84.70%) are so far above prior art that data leakage is a plausible concern that is not addressed.

3. **The PLM integration component is a black box.** The ablation study attributes a 13.43% recovery improvement to "PLM knowledge" (Table 1), but the mechanism is never described. The baseline without PLM already achieves 65.35% recovery—itself far above any prior method—which is never explained. The scaling experiments (Figure 5) show marginal gains despite a 375× increase in parameters (8M to 3B), which is not discussed in terms of efficiency or diminishing returns. Without knowing what the PEFT technique is, how the PLM is interfaced with the surface encoder, or what information the PLM contributes beyond what the surface encoder already captures, this component cannot be assessed.

### Minor

- **Gap between theoretical framing and implementation.** The paper motivates its approach by arguing that molecular surfaces are continuous manifolds with infinite resolution, and that prior point-cloud methods fail to account for smoothness. However, the actual implementation uses standard point-cloud processing: PyMol-generated surfaces, Gaussian kernel smoothing (borrowed from prior work), k-NN graphs, and eigenvalues from a local covariance matrix as "pseudo curvatures." The paper never demonstrates that this pipeline actually respects manifold structure or differs meaningfully from existing surface-based methods (e.g., dMaSIF, SurfPro). The Darboux frame discussion (Section 2.2) is mathematically detailed, but the connection to the actual implementation (eigenvalues → pseudo curvatures) is asserted without validation that these quantities approximate the claimed geometric quantities.

- **No evaluation on functional design tasks.** The paper motivates surface-conditioned design by arguing that it enables functional protein design (binding affinity, enzyme redesign), but all evaluations are on inverse-folding-style sequence recovery—predicting the wild-type sequence from surface features. Whether SurfDesign can actually design functional proteins with novel functions is not tested. This limits the paper's contribution relative to its stated motivation.

- **No error bars or confidence metrics.** All reported metrics are point estimates without variance. While single-run evaluation is common in this field, the gap between reported results and prior art is large enough that confidence intervals would substantially strengthen the analysis.

- **"SurfDock" typo (line 92).** The text reads "SurfDock is the foremost to exceed 70% recovery" where context clearly indicates "SurfDesign." (Note: per instructions, this is flagged as a parser artifact / minor author error.)

- **Multi-chain evaluation on PDB.** The multi-chain experiment (Table 3) trains and tests on the entire PDB (clustered at 30% identity). Recovery >80% on this dataset may partly reflect that the model is tested on structures similar to its training data, making the comparison to CATH-trained baselines difficult to interpret.

### Trivial

- The conclusion is generic and does not discuss limitations or failure cases.

## Nice-to-Haves

- A controlled experiment comparing SurfDesign to a structure-based method that uses the **same PLM** (e.g., ESM-IF with the same adapter technique) would isolate the contribution of surface conditioning vs. the PLM.
- An ablation showing recovery with and without individual surface features (normals only, curvatures only, both) would clarify what each geometric component contributes.
- Concrete case studies (visualized) showing where SurfDesign recovers native residues correctly vs. where it fails, especially in binding interfaces.
- The paper would benefit from a clear section or paragraph stating limitations and potential failure modes.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about the "SurfDock" typo undermining confidence**: Per hard rules, pure typographical errors are removed as they are likely parser artifacts or minor author errors and do not affect the paper's substantive evaluation.
- **Criticism about missing appendix content or absent references**: Per hard rules, the parser strips appendix sections from all papers; their absence in the extracted text does not imply they were absent in the original submission.
- **Criticism that the method is "not a paper" because contributions are missing**: While the underspecification is a major weakness, the paper does present a coherent method pipeline (surface generation, geometry computation, graph construction, PLM integration at the system level) and extensive empirical results, so it qualifies as a complete paper submission.
- **Strength Finder's claimed strengths about SEMP and PEFT being "principled improvements"**: These strengths conflict with the verified weakness that neither SEMP nor PEFT is technically described. Per instructions, when a strength and verified weakness disagree, the weakness wins. The strengths are therefore moved here rather than included in the main Strengths section.

## Novel Insights

The most interesting observation across the reviews is the tension between the paper's ambitious theoretical framing (continuous manifolds, Darboux frames, equivariant message passing) and the much more conventional point-cloud toolkit actually deployed (PyMol surfaces, Gaussian smoothing, k-NN, eigenvalue decomposition). Several findings reported—particularly the >80% recovery on TS50/TS500 and the 65.35% ablation baseline without any PLM—are striking enough to warrant follow-up investigation even if the current manuscript does not provide the technical detail needed to fully trust them. The structural-context analysis (Figure 4) is a genuinely useful diagnostic that shows where surface conditioning helps over backbone conditioning (surface-exposed residues), and this kind of analysis could inform future work regardless of whether SurfDesign's specific numbers hold up under closer scrutiny.

## Suggestions

1. **Provide full technical specification of SEMP and hybrid PEFT.** The paper needs equations for the message update mechanism, an explicit statement of the equivariance group (SE(3) or E(3)) and how it is achieved, and a complete description of the adapter architecture used for PLM integration. Without this, the paper's core contributions cannot be evaluated.

2. **Add error bars and protocol verification.** Report results across multiple random seeds. Directly verify that evaluation splits match those of prior work (or re-run baselines in the same environment) to rule out evaluation discrepancies as an explanation for the large performance gap.

3. **Validate the pseudo-curvature approximation.** The paper should demonstrate (e.g., via a toy experiment or visual comparison) that the eigenvalues computed from the local covariance matrix actually approximate the Darboux frame quantities (normal curvature, geodesic curvature, geodesic torsion) as claimed.

4. **Isolate the contribution of surface conditioning.** A clean comparison: the same architecture with vs. without surface features (using backbone coordinates only) would directly measure what surface conditioning adds over standard inverse folding.

## Score and Decision

This paper addresses a genuinely important and under-explored problem, and the empirical scope is impressive. However, the two claimed technical contributions (SEMP and hybrid PEFT) are not technically described anywhere in the paper—no equations, no architectural details, no equivariance derivation—making evaluation of novelty, correctness, and reproducibility impossible. The reported results, while interesting, are dramatically above prior art with no error bars and no verification that evaluation protocols are matched. The paper needs major revision to provide sufficient technical description of its method before it can be properly evaluated.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>