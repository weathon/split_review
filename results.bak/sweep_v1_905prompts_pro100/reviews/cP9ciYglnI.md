Now I have all the information needed to write the final review. Let me present it.

---

## Summary

This paper proposes a shape-adaptive guidance signal (Weighted Geodesic Distance Transform, WGDT) for interactive cortical sulcal labeling on spherical representations. The key idea is to encode user clicks by solving the eikonal equation with a propagation speed function derived from mean curvature, so that the guidance signal spreads faster along sulcal valleys and slower on gyri — unlike conventional equidistance-based encodings (angular distance transform, binary disk) that ignore cortical anatomy. Using a spherical CNN backbone (SPHARM-Net), the method supports iterative refinement with multiple clicks. Experiments on 72 HCP subjects with 17 LPFC sulci demonstrate that WGDT significantly outperforms equidistance signals, particularly on small and variable sulci.

## Strengths

- **Novel, well-motivated guidance signal**: The WGDT encoding (Section 2.3.3, Equations 3–5) solves the eikonal equation with a curvature-driven speed function, producing guidance signals that adaptively elongate along sulcal folds rather than expanding as isotropic disks. Figure 3 visually demonstrates this shape-adaptive behavior and convincingly shows how ADT/Disk signals spill over into adjacent unrelated sulci while WGDT remains aligned to the targeted fold.

- **Rigorous within-method evaluation**: The comparison of WGDT vs. ADT vs. Disk (Figure 4) is well-controlled — same backbone, same features, same click simulation protocol — isolating the effect of the guidance signal design. All 9 small/variable sulci show statistically significant gains (adjusted p < 0.05 under FDR correction) for WGDT with a single click. This evidence directly supports the paper's core contribution.

- **Iterative refinement with weighted loss**: The click simulation protocol (Section 2.2) iteratively samples clicks from the largest mislabeled component with weighted random sampling, and the training loss (Section 2.4, Equation 7) weights later clicks more heavily. Figure 4 shows progressive Dice improvement across clicks, and Figure 6 provides qualitative convergence examples.

- **Practical runtime**: Table 2 reports < 0.5 s total per click (signal encoding + re-tessellation + forward pass), supporting real-time interactivity claims.

## Weaknesses

### Fatal

None. The core contribution — the WGDT guidance signal design and its superiority over equidistance encodings — stands on solid evidence.

### Major

- **Unfair comparison with automatic baselines weakens a headline claim.** The paper claims that "even a single click using the proposed encoding scheme outperforms fully automatic methods" (abstract, Section 4.2, Figure 5). This comparison has two confounds:

  *Masking differential:* The interactive model's predictions are post-processed by retaining only vertices with `curv ≥ 0` (Section 3.3), which removes false positives outside sulcal regions. The automatic baselines (Lyu et al., Lee et al.) are evaluated without this anatomical prior. This masking is described as addressing "re-tessellation artifacts," but it functions as a strong spatial prior that will inflate Dice scores relative to unmasked baselines.

  *Task asymmetry:* The interactive model is trained as a per-sulcus binary classifier, while the automatic baselines perform multi-label classification across all 17 sulci simultaneously. Binary classification is inherently simpler, particularly for small sulci that are easily confused with neighboring structures in a multi-label setting.

  These issues do not invalidate the within-encoding experiments (WGDT vs. ADT vs. Disk), which remain clean and convincing. But they substantially weaken the claim that the interactive method "outperforms" automatic methods. The claim should be either removed or heavily qualified, with the confounds transparently disclosed. The discussion already gestures toward complementarity ("automatic model provides stable predictions for large and consistent sulci, while our proposed interactive model effectively resolves the errors in small and variable sulci"), which is a more defensible framing.

### Minor

- **Optimized initial click placement inflates single-click performance estimates.** Initial clicks are selected to "maximize both their distance from the label boundary and mutual separation" (Section 3.3), yielding unrealistically favorable click positions deep inside the sulcus. A real user may click closer to the boundary. This means reported single-click Dice scores are upper-bound estimates. The relative comparison across guidance signals is unaffected (all use the same clicks), but the absolute performance claims and the framing of single-click efficiency would be strengthened by including random click sampling with variance reporting.

- **First-click model input unspecified.** The model receives a "current prediction" as input (Figure 2, described as "optional" in the caption), but the paper does not specify what is fed at the first click when no prediction exists (zeros, a blank channel, or omission). Section 2.2 handles click simulation for training (extracting from the manual label when no prediction is available), but the model input itself is not clarified. This is a minor reproducibility gap.

### Trivial

None.

## Nice-to-Haves

- An ablation showing the contribution of the `curv ≥ 0` masking step to Dice scores (with vs. without masking) would help readers understand how much of the interactive method's advantage comes from the anatomical prior vs. the guidance signal.
- A brief sensitivity analysis or discussion of criteria for choosing hyperparameters `k` and `σ` on a new dataset would improve practical adoption. The paper acknowledges this as future work.
- Clarifying the practical deployment workflow (does the user specify which sulcus they are labeling before clicking?) would help readers understand the interactive experience.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic: "The reliability of the manual annotations is not reported; an inter-rater Dice would strengthen confidence."** This is a nice-to-have, not a weakness. The paper uses standard HCP data with published annotation protocols. Demanding inter-rater reliability for a methods paper on guidance signals is scope creep and a generic one-size-fits-all criticism.

- **Harsh critic: "The choice of loss weights β_i = [1/6, 1/3, 1/2] is given without justification."** The paper adapts ICL from Sun et al. (2024), which is a cited prior work. The weighting pattern (emphasizing later clicks) follows directly from that framework. Requiring additional justification for a standard adaptation is a nitpick.

- **Strength finder: "Spherical CNN foundation preserves geometry."** This is true but the paper uses an existing backbone (SPHARM-Net); the spherical mapping is standard practice in this subfield. The strength of the paper is the guidance signal, not the backbone choice.

- **Strength finder: "Iterative refinement mechanism."** The click simulation and iterative training are sound but follow established practices (Mahadevan et al., Sofiuk et al.). Not a novel contribution of this paper.

## Novel Insights

The core insight — that an eikonal-equation-based guidance signal with curvature-driven propagation speed can encode user clicks in a way that respects cortical folding patterns — is genuinely novel and well-executed. Figure 3 provides a compelling visual demonstration of why shape-adaptive encoding matters: equidistance signals spill over into adjacent sulci that are geodesically close but anatomically distinct, while WGDT stays confined to the intended fold. The use of the fast marching method on a re-tessellated spherical mesh to solve the eikonal equation in sub-200ms is a practical engineering contribution that makes the idea viable for real-time use.

## Suggestions

- **Reframe the automatic baseline comparison.** Instead of claiming superiority, present it as evidence that interactive refinement can recover the failures of automatic methods on small/variable sulci, and transparently note the masking and task-format differences. Better yet, run the automatic baselines with the same `curv ≥ 0` masking to isolate the effect of the interactive guidance.

- **Add random click sampling.** Replace or supplement the optimized initial click placement with random clicks sampled within the sulcus, and report mean ± std Dice. This would ground the single-click claims in a more realistic scenario without changing the core contribution.

- **Specify the first-click model input.** State explicitly what tensor (dimensions and values) is fed as the "current prediction" when none exists.

## Score and Decision

**Originality:** The WGDT signal design is novel — curvature-driven eikonal propagation for interactive guidance on spherical cortical surfaces has no direct precedent in the literature. **Importance:** Sulcal labeling of small/variable sulci is a real bottleneck in cognitive neuroscience, and the paper targets this bottleneck directly. **Claims supported:** The within-encoding comparison (WGDT vs. ADT/Disk) is rigorous and well-supported; the comparison to automatic methods overreaches due to confounds. **Soundness:** The core methodology is sound; the iterative click simulation, statistical testing, and cross-validation are appropriate. **Clarity:** Well-written and well-motivated throughout. **Value:** The WGDT signal could be adopted by other cortical surface analysis pipelines and the idea of shape-adaptive guidance could transfer to other surface-based interactive tasks.

### Calibration

Round 1 bracketing: low band (interactive medical segmentation, avg 2.33–3.00), middle band (cortical surface / spherical CNN, avg 3.67–7.00), high band (geometry/mesh segmentation, avg 7.60–8.00). The paper is clearly above the low band and below the high band. Initial bracket: **[5.0, 7.0]**.

Round 2 narrowing:
- **AGILE3D** (9cQtXpRshE, avg 5.50): Interactive 3D segmentation with attention-guided multi-object clicks. Similar domain (interactive segmentation), with user studies and multiple datasets but concerns about incremental novelty. Our paper has a more genuinely novel technical contribution (WGDT) but a narrower evaluation scope and the comparison fairness issue. **Comparable; our paper sits near 5.5.**
- **DeepSPF** (Dnc3paMqDE, avg 6.33): Spherical SO(3)-equivariant patches for 3D tasks. Novel representation, evaluated across three tasks, presentation issues. Stronger systematic contribution than our paper. **Our paper is somewhat weaker.**
- **Efficient Neuron Segmentation** (Y0QqruhqIa, avg 6.25): Query-based neuron segmentation in EM. Domain-specific contribution with strong evaluation.
- **Order-aware Interactive Segmentation** (8ZLzw5pIrc, avg 6.00): Interactive 2D segmentation with order encoding.

The paper under review has a novel, well-motivated contribution (WGDT signal) with solid within-method evaluation, but the headline claim about outperforming automatic methods has genuine confounds that weaken it. Relative to AGILE3D (5.50), which had similar mixed-review dynamics (genuine novelty plus evaluation concerns), our paper is comparable — the WGDT idea is more novel than AGILE3D's click attention module, but AGILE3D had broader evaluation including user studies. Compared to DeepSPF (6.33), our paper is weaker due to the narrower scope and comparison issues.

**Final score: 5.5**, between AGILE3D (5.50) and DeepSPF/Order-aware IS (6.00–6.33), leaning toward the lower end due to the comparison fairness issue that affects a headline claim.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>