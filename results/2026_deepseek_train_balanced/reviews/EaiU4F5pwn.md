## Summary

PG-Diff proposes a diffusion model for reconstructing high-fidelity 2D turbulent flow fields from solver-generated (as opposed to artificially downsampled) low-fidelity data. The method combines a DWT-based importance weight integrated into the diffusion training loss to prioritize high-frequency details, and a training-free PDE residual correction applied at selected inference steps for physical consistency. Experiments on four 2D turbulent flow datasets show improvements over non-physics-guided baselines.

## Strengths

1. **Novel and well-motivated problem formulation**: The paper clearly identifies the distinction between "integrate then downsample" (artificially downsampled low-fidelity data used by prior work) and "downsample then integrate" (solver-generated low-fidelity data encountered in practice), illustrated in Figure 1 and discussed in Section 1 (lines 14–16). This is a genuine and underappreciated practical concern in CFD reconstruction.

2. **Well-specified DWT-based importance weighting**: The importance weight computation is mathematically complete (Eq. 3, Eq. 4, lines 96–113): DWT decomposition into HL, LH, HH subbands, sum-of-squares aggregation, and quantile-based linear mapping. This directly targets fine-grained high-frequency details that prior diffusion-based methods do not explicitly emphasize, and avoids the computational cost of attention-based approaches.

3. **Systematic study of residual correction scheduling**: Section 4.5 (lines 217–226, Table 2, Figure 4) compares four scheduling policies (Uniform, Start+End, Start+Space, End+Space) with varying numbers of correction steps, yielding the principled choice "Start 2, End 2" that optimally balances L2 error and PDE residual. This goes beyond ad-hoc choices in prior work and is a genuinely useful empirical contribution.

4. **Multi-scale evaluation via DWT**: The DWT-based evaluation (Section 4.2, lines 144–145) measures reconstruction quality separately in LL, LH, HL, HH subbands, directly testing the paper's central claim of recovering high-frequency details rather than only aggregate error.

5. **Ablations confirm both components contribute**: Two ablations (PG-Diff w/o IW and PG-Diff w/o Cor, Section 4.2, line 142) show that removing either Importance Weight or Residual Correction degrades performance, validating the modular design.

## Weaknesses

### Fatal
None.

### Major

1. **Missing physics-guided diffusion baselines undermine the SOTA claim.** The paper cites Chung et al. (2023), Huang et al. (2024), Zhu et al. (2023), and Shysheya et al. (2024) in Section 3.2 (line 120) as related diffusion guidance methods, noting that PG-Diff's Residual Correction "differs" from them. However, none of these are included as experimental baselines (Section 4.2, line 142). The comparison set consists of bicubic interpolation, a CNN (Fukami et al., 2019), a GAN (Li & McComb, 2022), and two diffusion variants from Shu et al. (2023). For a paper whose core contribution is a *physics-guided diffusion method* claiming state-of-the-art results, the absence of even a single physics-guided diffusion baseline is a significant gap. It is impossible to assess whether the reported improvements stem from the proposed components or from properties common to any physics-guided diffusion approach.

2. **Ambiguous experimental setup description for the paper's central claim.** The dataset generation description (line 138) reads: "The high-fidelity data are generated with 2048×2048 discretization grid and then uniformly downsampled to 256×256, while those on the lower-resolution grids are considered low-fidelity." This does not explicitly state whether the low-fidelity data (32×32, 64×64) comes from *separate coarse-grid numerical simulations* ("downsample then integrate," the paper's claimed setting) or from *downsampling the same 2048×2048 simulation* ("integrate then downsample," the setting the paper criticizes prior work for using). The paper's entire motivation hinges on this distinction — if the low-fidelity data is simply downsampled from the fine-grid solution, the experiments do not test the claimed problem. While the paper's narrative (abstract, introduction, method) consistently asserts the use of solver-generated data, suggesting this is a writing clarity issue rather than an experimental error, the ambiguity must be resolved for proper evaluation.

### Minor

3. **Theoretical connection for Importance Weight not established.** The paper weights the elementwise noise-prediction loss by DWT-derived importance scores, with the goal of improving reconstruction of high-frequency flow structures. The difficulty is that the model is trained to predict random Gaussian noise εₜ, which is spatially i.i.d. — weighting its prediction loss does not obviously translate to better reconstruction of structured, high-frequency vorticity features. The paper provides no analysis (theoretical or empirical) bridging this gap, e.g., showing that the model predicts noise more accurately in high-weight regions, or that denoised reconstructions have lower error specifically in those regions. The ablation shows IW helps empirically, but the mechanism is a black box.

4. **Residual Correction module is under-specified for reproducibility.** The description (Section 3.2, lines 118–127) leaves several details unclear: (a) how the PDE residual ℛ(·) is computed — the incompressible Navier-Stokes equations involve spatial derivatives (gradient of vorticity, Laplacian of vorticity) that could be evaluated via finite differences, spectral methods, or automatic differentiation, each affecting gradient quality and cost; (b) the exact objective function minimized by gradient descent (L2 norm of the residual? a different loss?); (c) after correcting the denoised prediction x₀^τ, how this corrected state feeds back into the DDIM reverse process to continue denoising is not explained. The body of Algorithm 1 is not fully visible in the extracted text.

5. **No computational cost comparison.** Diffusion models are already computationally expensive at inference (requiring many denoising steps), and PG-Diff adds gradient descent steps at selected timesteps. The paper reports no runtime, FLOPs, or wall-clock time comparison against baselines. This is important practical information for any real-world application.

6. **Inconsistent "training-free" claim.** Line 235 states "both our importance weight mechanism and residual correction modules are training-free," but Section 3.1 (lines 92–114) explicitly describes the importance weight as a training-time modification to the diffusion loss. Only the residual correction is training-free.

7. **Generalization results lack in-text numerical discussion.** Section 4.6 (lines 230–235) claims PG-Diff generalizes across time discretization, domain size, and Reynolds number "comparably to trained ones," but provides no summary numbers in the text — only a reference to Table 3 (which is present in the paper as an image). Key values should be stated in the text.

### Trivial

- Section numbering skips from 4.3 directly to 4.5 (no Section 4.4).
- The quantile threshold θ in Eq. 4 is a free hyperparameter with no discussion of how it was selected or any sensitivity analysis.
- The "3.5% to 7.7% performance gain" (line 148) does not specify whether this is relative or absolute improvement.

## Nice-to-Haves

- An explicit validation experiment showing that baseline models (e.g., Cond Diff from Shu et al.) trained on downsampled data indeed fail on solver-generated data, experimentally confirming the claimed distribution shift.
- Sensitivity analysis on the quantile threshold θ used in the importance weight (Eq. 4).
- Discussion of limitations: (a) all experiments are 2D — scaling to 3D is non-trivial; (b) the method requires access to the PDE residual at inference, which may not be available for all CFD solvers; (c) evaluation is on synthetic pseudo-spectral solver data, not experimental CFD data.

## Removed Points

- **Criticism about generalization results lacking support**: The harsh critic claimed generalization results were unsupported because no numbers were given in text. However, Table 3 (line 245) exists in the paper as an image — the claim is supported, just the textual discussion is sparse. Downgraded to Minor (lack of in-text numerical summary).
- **Criticism about Algorithm 1 missing**: The algorithm body was stripped by the text extraction parser. The paper clearly references Algorithm 1 and provides its "Require" block (lines 122–124). However, remaining underspecified procedural details are retained as Minor weakness #4.
- **Speculative criticisms about confounders and metric validity**: These were area-of-concern sweeps ("could the metric be measuring a proxy?", "are confounders controlled?") without concrete anchors in the paper. Removed as noise.
- **Strength about "diffusion models only require high-fidelity data during training" treated as generic**: This is an accurate, specific property of the Shu et al. conditioning approach adopted by PG-Diff. Retained in context of the problem formulation.

## Novel Insights

None beyond the paper's own contributions. The scheduling analysis for residual correction (Section 4.5) comparing Start+End, Uniform, End+Space policies with controlled N is practically useful and presented clearly by the paper itself.

## Suggestions

1. **Add at least one physics-guided diffusion baseline** (e.g., Chung et al. 2023 or Huang et al. 2024) to substantiate the SOTA claim. This is the single most impactful improvement.
2. **Unambiguously clarify the experimental setup**: explicitly state that low-fidelity data at 32×32 and 64×64 is generated by solving the PDE at those coarse resolutions (not by downsampling the fine-grid solution).
3. **Provide diagnostic analysis for the IW mechanism**: show per-region reconstruction error relative to importance weight values, or demonstrate that noise prediction accuracy correlates with importance scores.
4. **Specify the residual correction in full**: state how PDE residuals are discretized (finite differences / spectral / AD), the exact objective, and how the corrected x₀ feeds back into the DDIM loop.
5. **Report computational cost**: runtime or FLOPs comparison against baselines.
6. **Correct the "training-free" claim** and add a limitations section addressing 2D-only evaluation, reliance on PDE residual at inference, and synthetic data scope.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>