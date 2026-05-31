## Summary
GenCoGS proposes a unified few-shot novel view synthesis method based on 3D Gaussian Splatting that addresses the core problem of insufficient scene completion when only sparse input views are available. The paper introduces two complementary strategies: (1) a generative point cloud completion–based Gaussian initialization (GCGI), which generates complementary points via a Transformer-based network and filters hallucinated outliers with a kd-tree structure; and (2) a generative pseudo-view completion–based Gaussian optimization (GCGO), which uses an image-to-video diffusion model over a perturbed camera trajectory to synthesize pseudo views covering unobserved regions, guided by a generative consistency loss that attenuates hallucination artifacts. Experiments on LLFF, DTU, and Shiny show consistent state-of-the-art performance among 3DGS-based few-shot methods.

---

## Strengths

- **Consistent SOTA across three benchmarks.** GenCoGS outperforms all compared 3DGS-based methods on LLFF (3/6/9-view), DTU (3-view), and Shiny (3-view). On DTU it exceeds the second-best 3DGS method by 2.40 dB PSNR, which is a large margin in this domain; on Shiny it gains 1.47 dB over FSGS. On LLFF it beats BinoGS, the strongest prior 3DGS baseline, by 0.47–0.74 dB across view counts.

- **Well-designed generate-and-filter paradigm for point clouds.** The CPF module using kd-tree nearest-neighbor distances as an optimize-free outlier indicator is simple, interpretable, and avoids introducing additional trainable parameters that might destabilize the 3DGS optimization. Table 6 shows CPF alone contributes a clear gap in LPIPS (0.178 → 0.164), and the strategy is robust even when the initial SfM cloud is degraded to 25% of its points.

- **Meaningful ablations.** Table 4 isolates GCGI and GCGO contributions. The combination outperforms each individually by additional margins (PSNR 22.13 vs 21.65/21.45), validating that initialization and optimization improvements are complementary. Table 5 separately ablates the perturbed camera trajectory against random sampling and the effect of $\mathcal{L}_{GC}$, both showing clear quantitative benefit.

- **Practical hallucination mitigation.** The confidence mask $\hat{M}_r$ in the generative consistency loss—computed adaptively from pixel-level color deviation with Gaussian-blur–derived local statistics—is a concrete, lightweight mechanism to suppress diffusion hallucination without retraining the generative backbone. Figure 4 visualizes its effectiveness.

---

## Weaknesses

### Fatal
None.

### Major

1. **No runtime or efficiency analysis.** 3DGS is valued precisely for its training and rendering speed. GenCoGS adds: SfM → GCGI (DGCNN + Transformer encoder-decoder + FoldingNet) → CPF (kd-tree) → 3DGS optimization, with the I2V diffusion model invoked during the last 1,000 iterations of training per scene. No wall-clock training times or inference speeds are reported anywhere, making it impossible to judge the practical overhead relative to baselines like FSGS or BinoGS that run in minutes. For a venue where efficiency is a first-class concern this is a significant omission.

2. **CPG module training details are absent from the main paper.** Section 3.1.1 describes the architecture (DGCNN, Transformer, FoldingNet) but does not explain how the CPG module is trained, on what data (ShapeNet? ScanNet? Something else?), or whether it generalises zero-shot to the test scenes. This is a core design choice and the reproducibility statement's "source code upon acceptance" does not substitute for the explanation needed to evaluate the contribution.

3. **Multi-view evaluation limited to LLFF.** Tables 2 and 3 report only the 3-view setting for DTU and Shiny, while Table 1 covers 3/6/9 views for LLFF. Readers cannot tell whether the large DTU gains hold at 6 or 9 views, or whether GCGI/GCGO bring diminishing returns as more observations are available—a crucial practical question.

### Minor

1. **CAT3D comparison ambiguity.** CAT3D generates dozens of synthetic views using a large multi-view diffusion model trained on large-scale data before fitting a 3DGS, making it far more expensive and data-hungry than GenCoGS. The tables mix it with lightweight 3DGS methods without noting this difference. GenCoGS outperforms CAT3D on LLFF (3-view) but the comparison context is unclear for readers unfamiliar with CAT3D's cost profile.

2. **Perturbed trajectory amplitude A is scene-independent.** The amplitude A=2.0 is a fixed global hyperparameter applied to all scenes, whose physical scale depends on the normalisation of camera coordinates. Figure 8 shows A=3.0 causes severe hallucination, so the method is sensitive near this value. No analysis of robustness across scenes with very different depth/scale is provided.

3. **GCGO starts only at iteration 4,000 of 5,000.** The diffusion-guided optimization operates for only the last 20% of training. The motivation for this delay (warm-up to avoid optimization instability) is not explicitly discussed, and it is unclear how sensitive the final result is to the choice of m.

### Trivial
- Table 6 appears to have a redundant row (the first two rows both list "Full / ✓ / — / …"); this looks like a copy-paste error from the parsing.

---

## Nice-to-Haves

- A training-time and rendering-time comparison table relative to FSGS and BinoGS would be very helpful to practitioners.
- Reporting DTU/Shiny results at 6-view and 9-view would strengthen the universality claim.
- An explicit description of CPG training (dataset, loss, whether it is fine-tuned per-scene or purely feed-forward) is important for reproducibility and would be more transparent.

---

## Novel Insights

The paper makes a crisp observation that existing 3DGS few-shot methods fail in two distinct but related ways—sparse initialisation and observation-biased pseudo-view sampling—and proposes targeted generative fixes for each. The insight that outlier filtering can be performed purely geometrically via kd-tree distance (no learned discriminator, no additional Gaussian parameters) sidesteps the common failure mode of hallucination cascading into the 3DGS optimiser. The confidence-mask formulation for selectively suppressing hallucinated regions in pseudo views, rather than discarding them entirely, is a practical middle ground between fully trusting and fully ignoring diffusion output.

---

## Suggestions

- Add a table comparing per-scene or average wall-clock training time for GenCoGS versus FSGS and BinoGS.
- Describe CPG training explicitly in the main text (dataset, loss function, number of epochs, whether it runs per-scene or once globally).
- Report DTU and Shiny results for 6-view and 9-view to establish robustness beyond the single evaluation condition.
- Discuss how the perturbation amplitude A should be chosen in practice for scenes with different spatial scales; ideally provide a simple normalisation or sensitivity curve.

---

## Score and Decision

The paper addresses a clear limitation in 3DGS-based few-shot NVS and proposes two technically sound, complementary strategies with consistent state-of-the-art results across three benchmarks. The ablations are informative and the core ideas are novel within the 3DGS few-shot context. The major gaps are: missing efficiency analysis (critical for 3DGS work), incomplete CPG training description, and limited multi-view evaluation on DTU/Shiny. These weaken but do not invalidate the contribution.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>