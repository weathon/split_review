Here is the final consolidated review.

## Summary
U3D proposes a framework for sparse novel view synthesis that extracts geometrical priors from a frozen video diffusion model (SV3D) and integrates them into a sparse-view generation network via a lightweight residual temporal adapter. The paper also introduces a temporal-enhanced sparse view network finetuned from video diffusion weights, preserving deep temporal attention layers that capture global structure. The key observations—that decoder temporal features encode geometry even from noisy inputs, and that deep temporal layers capture long-range structure—are well-motivated and supported by visualizations.

## Strengths
1. **Novel and well-demonstrated empirical observation (Section 3.1, Figure 3):** The paper identifies that temporal features in the decoder of a video diffusion U-Net encode rich geometrical priors, even when the input is pure Gaussian noise. This observation is supported by clear visualizations and is non-trivial—it directly motivates the core methodological contribution.
2. **Clean and efficient architectural design:** The residual temporal adapter is a lightweight cross-attention module inserted between the frozen video diffusion model and the frozen sparse-view network, training only its own parameters (~6k steps). The adaptive control module (two MLP layers) dynamically modulates control strength based on denoising step. This design is well-motivated and practical.
3. **Insightful analysis of temporal attention layers (Section 3.2, Figure 4):** The paper analyzes receptive fields and mean attention distances across temporal layers, showing that shallow layers attend locally (adjacent frames) while deep layers capture global structure across distant views. This observation directly motivates preserving deep temporal layers during finetuning for sparse-view generation.
4. **Strong qualitative results on challenging inputs (Figures 5, 6):** The qualitative comparisons show U3D producing more 3D-consistent and detailed novel views than EscherNet, Wonder3D, SV3D(p), and Era3D, particularly on inputs where 2D-diffusion baselines produce collapsed structures.
5. **Ablation studies validating both components (Figure 7, Table 1):** The paper ablates the geometrical reference network (w/o GR) and the temporal enhanced network (w/o TE), showing visible degradation when either component is removed. The ablation on denoising steps (N=0, 8, 20) also empirically justifies the design choice.

## Weaknesses

### Fatal
None.

### Major
1. **Quantitative evaluation is insufficient to support the SOTA claims.** The paper claims "state-of-the-art performance compared to existing methods" (line 24) and "outperforms other baselines across all metrics" (line 143), yet the quantitative evaluation is limited to a single in-distribution dataset (Google Scanned Objects, 200 objects for NVS, 50 for 3D reconstruction). No error bars, confidence intervals, or per-sample variance are reported. The central claim of "strong generalization ability" (abstract) is supported only by qualitative examples—there is no quantitative evaluation on any out-of-distribution or in-the-wild dataset. For a top-venue paper making explicit SOTA claims, this gap between the strength of the assertions and the breadth of evidence is significant.

2. **Which baselines are in the quantitative comparison is unclear.** The qualitative section (line 132) compares against EscherNet, Wonder3D, SV3D(p), and Era3D. The quantitative section (line 143) merely states "our model outperforms other baselines across all metrics" without explicitly enumerating which methods appear in Tables 1 and 2. A reader cannot determine from the prose whether all qualitatively compared methods were evaluated quantitatively, or whether the comparison is against a different subset. This undermines verifiability of the core quantitative claim.

3. **No runtime or efficiency measurements despite emphasis on efficiency.** The paper repeatedly claims computational efficiency over video diffusion methods ("accelerates the overall generation process" line 24; "lower computational costs and faster inference speeds" line 12). However, no runtime (seconds per view), FLOPs, parameter count, or any other efficiency metric is reported anywhere. These advantages are asserted but never substantiated.

### Minor
1. **No standalone comparison of the temporal-enhanced network against existing sparse-view methods.** The paper introduces the temporal enhanced sparse view network as "a new baseline sparse novel view synthesis network" (line 23). The ablation (Figure 7) compares U3D with and without the temporal enhanced network, but does not directly compare the standalone temporal enhanced network (without GR) against existing methods like EscherNet or Era3D in the quantitative tables. It is unclear whether this component alone already matches or exceeds prior SOTA.

2. **Reproduced SV3D uses different camera conditioning without matched-performance evidence.** The paper states the reproduced SV3D "adopts the pluckier ray embedding... which achieves similar performance" (line 125) but provides no evidence (e.g., a comparison table) to confirm that the reproduced model performs comparably to the official SV3D checkpoint used in the SV3D(p) comparisons. If the reproduced model underperforms, the video-diffusion baseline in comparisons may not reflect true SV3D performance.

3. **Actual metric values not reported in prose.** While numbers exist in the image tables, not a single numeric value (e.g., "PSNR: 24.5") appears anywhere in the main text. Reporting 2-3 key values in prose would help readers immediately assess the magnitude of claimed improvements.

### Trivial
- The limitations section (lines 162-164) is brief and generic; it does not discuss the evaluation scope limitations or show concrete failure cases.

## Nice-to-Haves
- Evaluate on an out-of-distribution or in-the-wild dataset (e.g., RealEstate10K) to substantiate the generalization claim.
- Provide a user study or pairwise preference judgments, given that qualitative results are the main evidence for the generalization advantage.
- Report variance/error bars for quantitative metrics.
- Include a failure case analysis.

## Removed Points
These points from the harsh critic are flagged for removal—use with caution:
- **"Comparison against SV3D is structurally unfair"**: The paper's thesis is that sparse-view generation with video priors outperforms direct video generation. Comparing against SV3D is standard and appropriate; the paper frames the different output formats as an advantage, not a flaw.
- **"Which specific layer(s) of the decoder?"**: Specified as "the third upsample block in the decoder" (Figure 3 caption) and "the temporal attention layer in the decoder block" (line 88).
- **"How is dimensional mismatch handled?"**: Explicitly addressed in lines 68-76 with feature shapes and the cross-attention equation.
- **"Shifted denoise schedule (8 steps) is unmotivated"**: Ablation in Figure 7 compares N=0, 8, 20, motivating the choice.
- **"No user study"**: A nice-to-have, not a weakness.
- **"Tables are unreadable"**: Parser artifact; tables exist as images in the original paper.
- **Missing related works, appendix content, formatting/style nitpicks**: Removed per instructions.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Tone down the SOTA claim or substantially broaden the quantitative evaluation (multiple datasets, error bars, explicit baseline enumeration).
2. State 2-3 key metric values in the prose for immediate reader assessment.
3. Report runtime/efficiency numbers to substantiate the computational advantage claims.
4. Add a clearer description of which baselines appear in Tables 1 and 2, either in the caption or the prose.
5. Compare the standalone temporal enhanced network (without GR) against prior sparse-view methods in the quantitative tables.
6. Include a failure case or discuss scenarios where U3D underperforms.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>