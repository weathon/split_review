Now I have a thorough understanding of the paper and can verify reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes Inductive Gradient Adjustment (IGA), a method that mitigates spectral bias in Implicit Neural Representations (INRs) by transforming gradients using the eigendecomposition of an empirical Neural Tangent Kernel (eNTK) matrix computed on a sampled subset of training points. The authors provide theoretical analysis (Theorems 1 and 2) showing that eNTK-based adjustments converge to NTK-based adjustments as width increases, and that training dynamics can be estimated via inductive generalization from sampled points. Empirically, IGA is evaluated on 2D image fitting, 3D shape representation, and NeRF, showing consistent improvements over vanilla training, Fourier reparameterization (FR), and batch normalization (BN) across ReLU, positional encoding (PE), and SIREN architectures.

## Strengths

1. **Principled theoretical grounding for eNTK-based spectral adjustment.** Theorem 1 provides explicit error bounds showing that eNTK-based gradient adjustments (eigenvalues, eigenvectors, training dynamics) converge to NTK-based adjustments as network width increases. This is the first work to formally establish the eNTK as a tractable surrogate for NTK-based spectral bias control, moving beyond the intractable full NTK that prior work relied on.

2. **Inductive generalization that scales to practical INR sizes.** Theorem 2 provides an error analysis showing that training dynamics can be estimated from sampled points via inductive generalization. The method is demonstrated on 768×512 images using less than 0.1% of total points for the transformation matrix, yet achieves consistent gains — e.g., PE+IGA reaches 32.46 PSNR vs 31.65 for PE+BN on Kodak images (Table 1).

3. **Tailored control of spectral bias via balanced eigenvalues.** Experiment 2 (Figures 3–4) shows that increasing the number of balanced eigenvalues (parameter *end*) progressively amplifies impacts on spectral bias for both ReLU and SIREN, with relative error curves decreasing more rapidly. This demonstrates purposeful, tunable improvement rather than a black-box modification.

4. **Consistent gains across diverse architectures and tasks.** Tables 1–3 show IGA improves PSNR, SSIM, LPIPS, and IOU for ReLU, PE, and SIREN on 2D image fitting, 3D shape representation, and NeRF, outperforming +FR and +BN in nearly every case. Fourier-domain heatmaps (Figure 5) further show IGA's improvements are uniformly distributed across frequency bands, unlike FR and BN which concentrate near low frequencies.

## Weaknesses

### Fatal
None.

### Major

1. **Training time and memory overhead not reported.** The method requires computing Jacobians for sampled points, forming an *n*×*n* Gram matrix, and performing eigendecomposition at each training step (the paper does not specify how often the eNTK is recomputed). For the 2D image experiments with *n*=384 (one point per 32×32 patch) through a 4-layer 256-width network, this is non-trivial. The paper does not report wall-clock time, memory usage, or iteration cost compared to baselines. Since the method is described as "practical," the absence of efficiency data makes it impossible to assess whether the improvement (e.g., +0.83 dB PSNR for SIREN, Table 1) justifies the additional overhead. This is a significant gap in evaluating the method's practical viability.

2. **Theory-practice gap is not adequately addressed.** The theoretical results (Theorems 1 and 2) are derived for a specific two-layer network with fixed last layer under assumptions of large width, data similarity within groups, and Lipschitz conditions. Yet the method is applied to four-layer networks with ReLU/Sine activations, trained with Adam (not SGD). The extension to Adam is justified only by intuition ("momentum has similar direction," "adaptive learning rates typically result in larger update steps") with no formal analysis (Section 3, line 106). The paper does not verify whether the assumptions of Theorem 2 (residual and gradient similarity within groups) hold for real image patches or NeRF rays. While such theory-practice gaps are common and acknowledged by the authors ("remains an open problem"), the paper presents the method as being "guided by theoretical derivation" without demonstrating that the theory's conditions are met in practice.

3. **Hyperparameter sensitivity is under-analyzed on real tasks.** The method introduces several interacting hyperparameters: group size (determining eNTK matrix dimension), number of balanced eigenvalues (*end*), sampling strategy, and (implicitly) recomputation frequency. Sensitivity analysis is limited to a 1D synthetic function (Experiment 2) with group sizes 4 and 8 and *end* from 2 to 8. For the main experiments (2D images, 3D shapes, NeRF), only single settings are reported with no ablation or guidance on how to select parameters based on signal properties. This limits reproducibility and understanding of the method's robustness across different settings.

### Minor

1. **Improvements in 3D shape and NeRF are marginal.** In the 3D shape experiment (Table 2), baseline IOU values are already very high (e.g., 0.9942 for PE), and IGA's improvement to 0.9970 is tiny on this saturating metric. In the NeRF experiment (Table 3), IGA achieves only +0.12 dB over NeRF+FR. While consistent improvements are commendable, the practical significance in these settings is unclear.

2. **FR and BN degrade SIREN performance under the reported settings.** In Table 1, FR and BN slightly *decrease* PSNR for SIREN (32.65 → 32.61 and 32.35), while IGA improves to 33.48. The paper states "we make every effort to achieve optimal performance" for baselines, but this asymmetry suggests the baselines may not be universally well-configured, making IGA's relative advantage partially an artifact of suboptimal baseline tuning for certain architectures.

3. **No statistical significance or variance reporting for main experiments.** The 2D image and 3D shape experiments report only average metrics without confidence intervals, standard deviations, or paired significance tests across the 8 images or 5 shapes. The 1D synthetic experiments (Experiment 1 and 2) do report runs with 10 seeds and shaded variance; this practice should extend to the main results to establish reliability.

### Trivial
None.

## Nice-to-Haves

- A sensitivity study for *end* and group size on at least one real task (e.g., Kodak image fitting), with guidance on selection based on signal spectrum.
- Reporting training time per iteration and total wall-clock time for IGA vs. baselines for a standard setting.
- Verifying the core theoretical assumptions (residual/gradient similarity within groups) on real data to strengthen the theory-practice connection.

## Removed Points

- **Criticism about "the frequency of recomputing the transformation matrix" being an unanalyzed hyperparameter**: The paper does not explicitly identify this as a hyperparameter or discuss its setting. While the omission is real, this point was introduced by the reviewer rather than being grounded in the paper's stated exposition.
- **Criticism about LPIPS=0.050 for BN in NeRF being "suspicious"**: The paper clearly notes these values are from the original BN paper (line 302: "Use values reported in the paper"). This is a transparency footnote, not an inconsistency in the paper's own experiments.
- **Strength about "addressing an important problem" / generic framing**: These are too generic and lack specific content.
- **Criticism about "cannot be independently verified"**: This type of criticism was removed per the hard rules; the paper cites existing models/tools.

## Novel Insights

The harsh critic and strength finder largely converge on the paper's profile: a theoretically motivated method with real but modest empirical gains, whose primary weakness is in evaluation completeness rather than soundness. The most insightful observation cutting across both reviews is that the paper's core tension lies between the rigorous but narrow theory (2-layer networks, SGD, specific assumptions) and the heuristic but effective practice (4-layer networks, Adam, real data). Neither reviewer fully captures that this gap is partly a feature of the literature — the NTK theory it builds on has similar limitations — but also a weakness the paper could mitigate by validating its assumptions on real data rather than deferring to empirical results alone. Another cross-cutting insight: the paper's strongest evidence is the Fourier-domain heatmap analysis (Figure 5) showing IGA's improvements are spectrally uniform, but this analysis is only qualitative. Quantitative frequency-domain metrics would substantially strengthen the core claim.

## Suggestions

1. **Report training time and memory** for IGA vs. baselines on at least the Kodak image setting. This is essential to support the "practical" claim and to let readers assess the efficiency-accuracy trade-off.
2. **Add statistical significance or per-sample results** to the main tables (e.g., standard deviations or confidence intervals across the 8 Kodak images and random seeds), consistent with what is already done for the 1D synthetic experiments.
3. **Validate key theoretical assumptions** — specifically the residual and gradient similarity within groups (Theorem 2's condition) — on real image patches or NeRF rays to bridge the theory-practice gap.
4. **Provide hyperparameter guidance** for selecting *end* and group size based on signal characteristics, and add at least one ablation on a real task showing sensitivity to these choices.

## Score and Decision

**Originality:** The paper is novel in showing that the eNTK can serve as a tractable surrogate for NTK-based spectral bias adjustment and in proposing inductive generalization to scale this to practical INR tasks.  
**Importance of Research Question:** Spectral bias in INRs is a well-recognized problem; principled training-dynamics methods that go beyond architecture search are valuable.  
**Claims Support:** The core claim — that IGA improves spectral bias and representation quality — is supported by consistent experimental evidence. However, the evidence is weakened by lack of timing data, limited hyperparameter analysis, and a gap between theoretical assumptions and practical implementation.  
**Soundness of Experiments:** Experiments cover diverse architectures and tasks with appropriate baselines. The main gaps are the absence of efficiency metrics, variance reporting, and hyperparameter sensitivity on real tasks.  
**Clarity:** The paper is clearly written, with a logical flow from theory to method to experiments.  
**Value to Community:** Moderate. The idea is principled and the inductive approach is potentially useful, but the evaluation gaps limit immediate practical impact.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>