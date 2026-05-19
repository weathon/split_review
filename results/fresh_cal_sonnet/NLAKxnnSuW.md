Now let me run the calibration search to find comparable papers.Based on Round 1, I bracket the paper between **5.5 and 7.5**. The closest anchor papers are Swift4D (6.5) and Lightweight Predictive 3DGS (7.0), both on Gaussian compression topics. Let me narrow with Round 2.Now I have enough information to write the final review. Let me synthesize all findings with the verified paper content.

---

## Summary

MEGA proposes a memory-efficient framework for 4D Gaussian Splatting (4DGS) of dynamic scenes. The core contributions are (1) a DC-AC color decomposition that replaces 144 per-Gaussian spherical harmonics coefficients with a 3-parameter per-Gaussian DC component and a shared lightweight MLP AC predictor, achieving ~8× per-Gaussian parameter reduction; and (2) an entropy-constrained Gaussian deformation technique that expands each Gaussian's temporal action range while pruning unnecessary Gaussians via an opacity entropy loss. Combined with FP16 and zip-delta compression, MEGA achieves 190× and 125× storage reduction on the Technicolor and Neu3DV datasets respectively, at comparable or better rendering quality and real-time frame rates.

---

## Strengths

- **Dramatic storage reduction with simultaneous quality improvement on Technicolor.** Table 1 shows MEGA reduces storage from 6107 MB to 32.45 MB (190×) while raising PSNR from 32.07 to 33.57 dB (+1.5 dB) and increasing rendering speed from 55.26 to 83.14 FPS relative to the 4DGS baseline. This refutes the common assumption that compression necessarily sacrifices quality.

- **DC-AC color decomposition outperforms the natural grid-based alternative.** Table 3 (both datasets) directly compares "w/ grid" (Lee et al. 2024) vs "w/ DAC": on *Birthday*, grid drops PSNR to 30.49 dB vs 4DGS's 31.00 dB, while DAC raises it to 31.60 dB. On *Flame Steak*, grid drops to 31.07 dB vs DAC's 33.34 dB (barely below 4DGS's 33.34 dB). The paper directly demonstrates its decomposition strategy is a superior compression mechanism.

- **Entropy-constrained deformation achieves very large Gaussian count reductions.** Table 3 (*Birthday*): the full method cuts Gaussians from 13M (4DGS) to 0.91M (14×) while raising PSNR from 31.00 to 32.02 dB. Figure 2(a) quantifies the mechanism: the participation ratio rises from <50% to ~75%. No prior 4DGS work achieves this combination of reduction and better utilization.

- **Comprehensive and honest ablation study.** The ablation (Table 3) systematically isolates each component across four scenes from both datasets, including intermediate variants ("w/ DAC+Deformation", "w/ DAC+L_opa") that reveal the failure mode of each component in isolation. The deformation predictor alone increases Gaussian count; the entropy loss alone limits action range; only the combination achieves massive reduction. This disclosure of intermediate failures strengthens credibility.

- **Real-time rendering maintained despite massive compression.** MEGA achieves 83 FPS on Technicolor and 77 FPS on Neu3DV (Tables 1 and 2), confirming the compression does not break the real-time interactive use case the method targets.

---

## Weaknesses

### Fatal
None.

### Major

- **View-dependent geometry deformation violates multi-view consistency.** Equation 2 (line 128) takes the normalized viewing direction `sg(d_v)` as input to the deformation predictor `F_θ`, which outputs deformations to position `m_{μ_{4D}}`, scale `m_{s_{4D}}`, and both rotation quaternions `m_{q_l}`, `m_{q_r}`. This means the *geometric shape and location* of each Gaussian varies with camera viewpoint at inference time. In multi-view capture setups like Neu3DV (18–21 cameras), the same physical object should occupy the same spatial position regardless of which camera renders it; view-dependent geometry violates this invariance. The stop-gradient on `d_v` (noted correctly in the method) prevents gradient flow back through the position input, but does not prevent the forward-pass inconsistency. The paper provides no justification for why geometry should be viewpoint-dependent, offers no analysis showing the predicted deformations are near-constant across views in practice, and does not acknowledge the consistency issue. While the method achieves good empirical PSNR (suggesting the MLP may learn near-view-invariant deformations in practice), this is an unacknowledged architectural choice that needs either justification or ablation. An experiment removing `d_v` from `F_θ` (leaving it only in the color predictor `F_φ`) would directly resolve this question.

### Minor

- **Scene-specific quality regression masked by aggregated reporting.** The ablation (Table 3b) shows the full method achieves only 32.27 dB on *Flame Steak* vs 33.19 dB for 4DGS, 33.34 for w/DAC, 33.47 for w/DAC+Deformation, and 33.45 for w/DAC+L_opa — the final method underperforms every intermediate ablation variant on this scene by 0.9–1.2 dB. The aggregate Neu3DV table (Table 2) shows MEGA at 31.49 dB vs 4DGS at 31.57 dB, which the paper characterizes as "similar visual quality." This is accurate on average, but the *Flame Steak* scene sustains a substantial degradation that is averaged away. The paper does not analyze what scene properties predict whether compression helps or hurts (Technicolor: quality improves; *Flame Steak*: quality degrades), leaving practitioners without guidance on when the method is reliable.

- **Multiplicative position deformation unexplained.** Equation 3 applies element-wise multiplication for position deformation: `μ_{4D}^{t,v} = μ_{4D} × m_{μ_{4D}}^{t,v}`. For positions and scales, additive residuals are the physically motivated convention (a Gaussian's position should shift by a translation, not scale relative to the origin). The multiplicative form biases deformation toward scaling away from or toward the scene origin, which is a strong implicit prior not acknowledged. For quaternions, the intended composition is also ambiguous (element-wise multiplication is not equivalent to the Hamilton product that represents rotation composition). The paper does not discuss this design choice.

- **Rendering speed characterization is slightly misleading.** MEGA runs at 77.42 FPS vs 4DGS's 96.69 FPS on Neu3DV (Table 2), a 20% slowdown. With 125× fewer Gaussians, rasterization should be faster; the overhead must come from MLP evaluation at render time. Calling this "comparable rendering speeds" in the abstract is defensible but imprecise. The paper does not profile or decompose where the rendering overhead originates.

### Trivial

- **MLP architecture not fully specified.** The AC color predictor is described as having "three linear layers" (Introduction) but no hidden unit widths are given. The deformation predictor architecture is not specified at all. For a compression paper where the MLP size directly contributes to storage overhead, the parameter counts of both shared MLPs should be stated.

---

## Nice-to-Haves

- A brief ablation removing view direction from the deformation predictor (leaving it only in the color predictor) would either clean up the method or justify the design choice.
- Per-scene breakdown in the main comparison tables (not just ablation) would let readers assess whether the "comparable quality" claim holds uniformly or concentrates in favorable scenes.
- Training time comparison with 4DGS would be helpful for practitioners, since two shared MLPs may increase training cost.
- Analysis of what scene properties (motion complexity, spatial frequency) predict whether MEGA improves or regresses quality would directly strengthen the compression claim.

---

## Removed Points

*These points are flagged for removal — treat with caution.*

- **"Setting a new standard" overclaim (harsh critic):** While slightly promotional, the abstract's language ("setting a new standard") is common in conference papers and not a substantive methodological flaw. Retained as a note on presentation but not included as a weakness.

- **Missing related work on 3DGS compression (harsh critic):** Removed per hard rule — cannot confirm the existence of unreferenced works.

- **MLP architecture reproducibility criticism:** The paper gives training hyperparameters (lines 241-242), Adam optimizer settings, and enough implementation detail for replication. The missing MLP widths are noted as Trivial, not a fundamental reproducibility flaw.

- **STG comparison asymmetry (6 models vs 1 model):** The harsh critic notes this as problematic. However, per hard rules, unfair comparisons that favor the baseline (STG) over the authors' method should be removed as weaknesses — the asymmetry here (STG uses 6 × 50-frame models summing to 175 MB vs MEGA's 25 MB for 300 frames) actually *favors* STG's storage efficiency per-model. The paper footnotes this ($^3$ in Table 2). No foul.

- **Strength Finder: "real-time rendering performance despite massive compression":** Kept, but as a partial strength — noted that there is a 20% slowdown on Neu3DV not fully acknowledged.

- **Participation ratio at 75% still leaving 25% waste (harsh critic):** This is an observation about the efficiency ceiling, not a genuine weakness of the method. The paper does not claim 100% utilization. Removed.

---

## Novel Insights

The combination of a stop-gradient on both position and view-direction inputs (to the color and deformation MLPs) is an underappreciated design choice: it means neither MLP can inadvertently learn to shift Gaussian geometry by abusing the position gradient, keeping the geometric optimization clean. The DC-AC decomposition, while conceptually simple, solves a problem the direct grid-based replacement fails on — it preserves the identity information that makes each Gaussian individual (DC component) while sharing the variation information (AC predictor), which is why it succeeds where grid approaches lose detail. The instability revealed in the ablation (deformation predictor alone *increases* Gaussian count) points to an interesting dynamic: the deformation predictor expands each Gaussian's action range but also creates a gradient incentive to densify more, which only the entropy loss reverses. This interaction is one of the more interesting mechanistic findings in the paper.

---

## Suggestions

1. Add a brief ablation (`F_θ` without `d_v`) to test whether view direction in the deformation predictor is necessary. If it is not, removing it would eliminate the multi-view consistency concern entirely.
2. Report per-scene PSNR in the main comparison tables (not just in the ablation) to give a complete picture of where compression gains and losses concentrate.
3. Report parameter counts of both shared MLPs (AC color predictor and deformation predictor) explicitly, so readers can verify the total storage accounting.
4. Provide training time figures relative to 4DGS to complete the efficiency profile.

---

## Score and Decision

**Round 1 bracket: 5.5 – 7.5**

Most similar anchor papers from Round 1:
- `PbheqxnO1e` (Lightweight Predictive 3DGS, avg 7.0, Accept): Compresses static 3DGS; similar area but static scenes, and reviewers cited limited novelty. MEGA addresses the harder dynamic case and is the first in its specific space.
- `c1RhJVTPwT` (Swift4D, avg 6.5, Accept): Compact dynamic 4DGS reconstruction with ~30MB storage; most directly comparable thematically.
- `DCandSZ2F1` (FCGS, avg 6.5, Accept): Optimization-free static 3DGS compression with 20× ratio; technically more sophisticated entropy model.

**Round 2 anchors:**
- `okD9dbifxa` (GaussianFlow, avg 5.83, Reject): Dynamic GS for 4D content creation; weaker than MEGA in experimental validation and clarity.
- `tMG6btjBfd` (SplineGS, avg 6.0, Accept): Deformable 3DGS with NURBS; similar area, slightly more principled deformation but narrower compression contribution.
- `dkrEoT68by` (GS-LK, avg 6.0, Accept): Analytical scene flow for dynamic GS; distinct approach but similar tier.
- `IcYDRzcccP` (4DGS from single landscape, avg 5.75, Accept): 4D Gaussians for different task; lower.

**Comparison against anchors:** MEGA is clearly stronger than the 5.75–6.0 tier (SplineGS, GS-LK): it has more dramatic empirical results (190× compression), a cleaner ablation, and addresses an important gap. Against Swift4D (6.5): MEGA achieves comparably impressive compression with a more elegant methodological design; however, MEGA has the unresolved view-dependent geometry architectural concern that Swift4D does not. Against FCGS (6.5): MEGA tackles the harder dynamic setting and achieves a much larger compression ratio, but FCGS's technical depth in the entropy model is stronger. Against Lightweight Predictive 3DGS (7.0): the level of novelty is similar (both fill specific gaps in GS compression), but Lightweight 3DGS has a reviewer citing limited novelty issues — MEGA has clearer novelty as the first in its space. MEGA is comparable to or slightly better than the 6.5 anchors, falling short of 7.0 due to the architectural concern about view-dependent geometry and the masked scene-specific quality regression. The paper is well above the 6.0 anchors.

**Final score: 6.5 | Decision: Accept**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Lightweight Predictive 3DGS | PbheqxnO1e | 7.0 | R1 | MEGA fills a harder gap but has one unresolved architectural concern; slightly below this anchor |
| Swift4D | c1RhJVTPwT | 6.5 | R1 | Most directly comparable; MEGA is slightly better in compression scale but has the view-dependent geometry concern |
| FCGS | DCandSZ2F1 | 6.5 | R1 | Comparable tier; MEGA is harder problem but less technically deep on the entropy side |
| HIWE | NLRo4qhg6t | 3.0 | R1 | Much weaker than MEGA |
| GaussianFlow | okD9dbifxa | 5.83 | R2 | Weaker; MEGA has cleaner results and stronger compression claim |
| SplineGS | tMG6btjBfd | 6.0 | R2 | Slightly weaker; MEGA has more dramatic quantitative impact |
| GS-LK | dkrEoT68by | 6.0 | R2 | Weaker in compression contribution; MEGA has stronger practical impact |
| 4DGS Single Landscape | IcYDRzcccP | 5.75 | R2 | Different task; lower tier than MEGA |

**Originality:** High — first systematic compression framework for 4DGS, novel DC-AC decomposition.  
**Importance:** High — 4DGS is practical only on server hardware; 125–190× compression opens AR/VR deployment.  
**Claim support:** Mostly strong — Technicolor claims well-supported; Neu3DV "comparable quality" claim slightly overstated given per-scene variance.  
**Experimental soundness:** Good — ablation is comprehensive, baseline evaluation is fair and disclosed.  
**Writing clarity:** Good — method is clearly presented; the view-dependent geometry choice is unexplained.  
**Value to community:** High — fills a clear and important gap; reproducibility is adequate for the area.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>