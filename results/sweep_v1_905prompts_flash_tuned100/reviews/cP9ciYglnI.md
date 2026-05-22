Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

This paper proposes a shape-adaptive guidance signal (WGDT) for interactive cortical sulcal labeling on the sphere. The key idea is to encode user clicks using a curvature-weighted geodesic distance transform (solving the eikonal equation with speed governed by mean curvature), so the signal propagates faster along sulcal valleys and slower along gyri. The method uses SPHARM-Net as backbone with per-sulcus binary models. Experiments on 72 HCP subjects with 17 LPFC sulci show that WGDT significantly outperforms equidistance-based signals (ADT, Disk) on small/variable sulci with a single click, and the interactive framework also surpasses fully automatic baselines.

## Strengths

- **Curvature-aware guidance signal is novel and well-motivated.** The WGDT formulation (Eq. 3–5) explicitly incorporates cortical curvature into the click encoding via the eikonal equation, moving beyond simple angular or binary disk schemes. This is the first interactive segmentation method for cortical surfaces that uses surface geometry to guide the signal, and the intuition—faster propagation in sulcal valleys—is clearly explained and visually demonstrated (Figure 3).

- **Controlled comparison among guidance signals (Section 4.1) convincingly validates the core contribution.** With all other factors fixed (same backbone, same per-sulcus models), WGDT consistently outperforms ADT and Disk on all 9 small/variable sulci (adjusted p < 0.05) after a single click. This is the cleanest part of the evaluation and directly supports the paper's central thesis even without reference to automatic methods.

- **Significant practical benefit for small, anatomically variable sulci.** These sulci (e.g., pmfs-a, half, lfms) are precisely the ones that automatic methods and equidistance signals struggle with. The paper shows that one click with WGDT brings these difficult targets to near-perfect accuracy after 2–3 clicks, which has clear practical value for neuroscience studies that currently rely on manual correction.

- **Real-time efficiency.** The pipeline (WGDT encoding + re-tessellation + forward pass) averages under 0.5 seconds per click (Table 2), making iterative refinement practical for real use.

## Weaknesses

### Major
None.

### Minor

- **Comparison to automatic baselines mixes two sources of advantage.** The proposed method uses per-sulcus binary models (17 separate models, each specialized for one sulcus), while the automatic baselines (Lyu et al. 2021; Lee et al. 2025a,b) are multi-sulcus models that label all 17 sulci in a single pass. This means the interactive method benefits from both (a) the click prior and WGDT signal *and* (b) dedicated per-sulcus optimization. The paper does not disentangle these factors. While the per-sulcus design is a standard and justifiable choice for interactive segmentation (the paper cites precedent in Diaz-Pinto et al., Wang et al., Luo et al.), the headline "single click outperforms fully automatic methods" conflates two distinct advantages. The paper would be stronger if it either: (i) acknowledged this asymmetry explicitly and discussed how much of the gain comes from the per-sulcus specialization vs. the guidance signal, or (ii) retrained the automatic baselines under a per-sulcus binary setup to isolate the pure effect of the interactive signal.

- **Click simulation is not validated with real human annotators.** The simulation (Section 2.2) selects the largest mislabeled component and samples near its center—a reasonable protocol that follows Mahadevan et al. and Sofiuk et al. However, the paper does not include any human-annotation experiment or even a sensitivity analysis with alternative click strategies. Without validation that the simulated clicks reflect real expert behavior, it is unclear whether the reported accuracy gains would transfer to practice. A small human study (e.g., 1–2 raters on a subset) or an alternative simulation (e.g., boundary clicks, random clicks) would substantially strengthen the evaluation of practical utility.

- **Evaluation is limited to LPFC.** The paper acknowledges this as future work (Section 5), which is appropriate, but some discussion of which properties of the method are region-specific (curvature-based propagation relying on LPFC folding patterns) vs. transferable would help readers judge generalizability.

- **Missing backbone ablation.** The paper uses SPHARM-Net and argues that its limited expressivity is compensated by the WGDT signal (Section 2.5). This is a plausible design rationale, but no experiment compares WGDT's benefit on SPHARM-Net vs. a more expressive spherical CNN. Such an ablation would clarify whether WGDT's gains are specific to this backbone or represent a general advantage.

### Trivial
- The hyperparameter \(k\) in Eq. 4 is described as modulating the influence of \(H\), but its effective range is constrained by the clamping \([0.05, 10]\). A brief note on how \(k\) interacts with clamping in practice would improve reproducibility.

- It is stated that mean curvature \(H\) is a "spherical function" but not explicitly clarified whether it is computed on the native white-matter surface and resampled to the sphere, or computed directly on the sphere (Section 3.1 suggests the former via FreeSurfer's *curv* feature, which is native-surface curvature mapped to the sphere—this could be stated more directly).

## Nice-to-Haves

- A human-annotation validation of the click simulation (even with a single rater on a subset of subjects).
- An ablation comparing SPHARM-Net with a more expressive spherical CNN (e.g., graph-based spherical network) with and without WGDT.
- A direct metric for guidance signal "spillover" (e.g., overlap of the guidance signal with the target sulcus vs. adjacent sulci) to support the qualitative claim that WGDT minimizes spillover.

## Removed Points

These points were raised by reviewers but are removed after verification against the paper:

- **"Unfair comparison invalidates central headline claim"** (Harsh Critic, Fatal tier): The critic claims the per-sulcus vs. multi-sulcus asymmetry is a "structural flaw" that invalidates the core claim. This is overblown. The comparison is between an interactive method (with click input) and fully automatic methods (without click input)—this is a standard evaluation paradigm in the interactive segmentation literature. The per-sulcus modeling is a design choice justified by the paper (Section 2.1) and consistent with medical image interactive segmentation practices. The controlled experiment in Section 4.1 (WGDT vs. ADT/Disk with identical per-sulcus setup) already isolates the WGDT signal's benefit. The automatic comparison is supplementary evidence showing that interactive methods broadly outperform automatic ones, which is the expected and intended claim. Demoting to Minor per the rules: the criticism has some validity as a precision point but does not threaten the core claim.

- **"Click simulation realism is unvalidated—this is an evidential gap"** (Harsh Critic): Kept as Minor (not removed entirely) but downgraded from the critic's framing as a major gap. The simulation follows established protocols in the field (Mahadevan et al., Sofiuk et al.). A human study would strengthen the paper but is not standardly required for acceptance.

- **"Mean curvature computation location unclear"**: Kept as Trivial since the paper uses FreeSurfer's standard *curv* feature which is computed on the native white-matter surface and then mapped to the sphere (standard in the field), though this could be stated more explicitly.

- **"No backbone ablation"**: Kept as Minor.

- **"Re-tessellation may affect fine-grained boundaries"**: Not included—this is a standard operation in spherical CNN pipelines and the paper already addresses artifacts with a masking strategy (Section 3.3).

- **"Limited to LPFC"**: Kept as Minor, appropriately acknowledged by the paper.

## Novel Insights

The most interesting meta-point emerging from the reviews is that the paper's strongest evidence (the controlled guidance-signal comparison in Section 4.1) is somewhat disconnected from its most eye-catching claim (outperforming automatic methods). The reviews collectively highlight that the paper would be stronger if it leaned into its actual technical contribution (curvature-aware encoding) rather than foregrounding the comparison to automatic methods, which inevitably raises design-paradigm confounds. The reviewer discussion also surfaces an important question for the field: at what point does per-sulcus specialization become a modeling advantage that should itself be compared, vs. a natural design choice inherent to interactive paradigms?

## Suggestions

1. **Clarify the automatic baseline comparison.** Explicitly state whether the automatic baselines were trained as multi-sulcus models or per-sulcus binary models. If they are multi-sulcus, briefly note this asymmetry in the comparison and discuss how it relates to the interpretation of results (e.g., the automatic methods are solving a harder multi-class problem, but the interactive method also has click information). This single sentence would address the most serious concern raised in review.

2. **Add a small human-annotation validation or alternative click simulation.** Even a limited experiment with one rater on a few subjects, or an ablation comparing the paper's simulation strategy against alternatives (e.g., random clicks, boundary clicks), would substantially increase confidence that the reported gains transfer to real use.

3. **Consider adding a backbone ablation.** A comparison between SPHARM-Net and a more expressive spherical network (e.g., a spherical CNN with anisotropic filters, or a graph-based network) would help determine whether the WGDT signal provides a general benefit or primarily compensates for SPHARM-Net's isotropic filter limitations.

## Score and Decision

**Round 1 (Bracketing):** Weak anchors ~3.0 (scores 2.50–3.00); middle anchors ~4.4–5.5 (scores 4.40–5.50); strong anchors ~8.0 (scores 8.00). Initial bracket: this paper clearly belongs in the middle band—it has a real, well-motivated contribution but does not have the exceptional novelty or exhaustive evaluation of the ~8.0 papers. It is clearly above the ~3.0 papers which had fundamental methodological issues or severely limited evaluations.

**Round 2 (Narrowing):** Compared against mid-range anchors. AGILE3D (5.50, interactive 3D segmentation) has user studies and broader evaluation but its technical novelty (click attention module for multi-object) drew mixed reviews. The current paper has a clearer methodological contribution (WGDT signal) but fewer evaluation dimensions (no user study, one brain region). The Neuron Segmentation anchor (6.25) is a stronger paper with better evaluation. The current paper is comparable to but slightly weaker than AGILE3D due to the lack of real-user validation and backbone ablation.

**Final calibration:** The paper sits between the 5.33–5.50 anchors and the 4.40–4.75 anchors. It has a clear, novel technical contribution that is well-supported by a controlled experiment, but has notable evaluation gaps (no user validation of click simulation, limited to one brain region, no backbone ablation). These gaps are bounded and addressable rather than fatal.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>