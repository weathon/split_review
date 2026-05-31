## Summary

D²GS addresses sparse-view 3D Gaussian Splatting (3DGS) by diagnosing two distinct failure modes—overfitting in near-field, high-density regions and underfitting in far-field, low-coverage regions—then proposing two targeted modules: (1) Depth-and-Density Guided Dropout (DD-Drop), which assigns each Gaussian a probabilistic dropout score based on local k-NN density and camera distance with a dual local/global mechanism, and (2) Distance-Aware Fidelity Enhancement (DAFE), which uses monocular depth estimates to mask far-field regions and amplify their L1 supervision signal. The paper also introduces Inter-Model Robustness (IMR), a new evaluation metric grounded in 2-Wasserstein distance and Optimal Transport over Gaussian mixture models, to quantify the stability of independently trained 3DGS models.

---

## Strengths

- **Sharp, quantified problem diagnosis.** The paper goes beyond general claims of "overfitting" by counting Gaussian primitives in matched spatial regions: near-field dense clusters have 11,450 Gaussians (sparse) vs. 6,112 (dense); far-field has 3,082 (sparse) vs. 5,224 (dense). This concrete evidence strongly motivates the two-module design.

- **Complementary module design with principled formulations.** DD-Drop's dual local (continuous per-Gaussian score via Eq. 1–2) and global (depth-stratified attenuation λ_far, λ_mid) mechanism is coherent and addresses overfitting from both fine-grained and structural perspectives. DAFE's masked L1 loss (Eq. 5) directly targets the opposite failure mode.

- **Novel evaluation metric (IMR) filling a real gap.** Figure 3 demonstrates PSNR ranging from 14.62 to 18.63 over 10 repeated training runs—a striking 4 dB instability that image-space metrics alone do not capture. Grounding IMR in OT/Bures geometry over Gaussian mixtures (Eqs. 9–14) is mathematically principled and directly characterizes representation quality beyond rendering outcomes.

- **Consistent quantitative gains across datasets and ablation fidelity.** D²GS achieves 21.35/20.56 dB on LLFF (1/8 and 1/4 res.) and 20.09 dB on Mip-NeRF360, outperforming all prior 3DGS-based baselines including DropGaussian (+0.59/0.55 dB, +0.35 dB). Table 4 ablation cleanly isolates each component's contribution, and Table 6 shows DAFE works across MiDas, DPT, and DepthAnything V2.

---

## Weaknesses

### Fatal
None.

### Major

- **IMR metric design issues.** The IMR formula in Eq. 14, log(Σ S²_ij / Σ S_ij), is essentially a log of a self-weighted average—it amplifies the contribution of large pairwise distances, but the motivation for this specific form over simpler alternatives (mean pairwise distance, max pairwise distance, standard deviation) is not discussed or ablated. More importantly, the reported values in Table 3 exhibit a counterintuitive ordering: DropGaussian has *higher* IMR (less stable) than vanilla 3DGS in the 3-view setting (3.205 vs. 3.162), despite being explicitly designed to reduce overfitting. The paper does not address this anomaly.

- **Building on DropGaussian without clear boundary.** The paper explicitly states "Our implementation is built on DropGaussian." The key distinguishing contributions—adaptive dropout replacing uniform dropout, and DAFE augmenting supervision—are meaningful, but the paper's relationship to and departure from DropGaussian deserves sharper delineation. It is not entirely clear whether the +0.59 dB improvement on LLFF requires the full D²GS machinery or could be partially achieved by simpler modifications.

### Minor

- **Fixed hyperparameters without ablation.** λ_far = 0.3 and λ_middle = 0.7 are described as "based on experimental experience" (Section 3.2) without any supporting ablation, despite extensive ablation of other hyperparameters (Table 5). Similarly, the choice of tertile-based depth thresholds and the fixed depth-layer count (3) are not ablated.

- **Computational overhead of DD-Drop uncharacterized.** Computing k-NN density over all Gaussian primitives (20k–310k per scene) at each training step is potentially expensive. The paper provides no runtime analysis or comparison to the DropGaussian baseline.

- **IMR practical cost not addressed.** IMR requires training N=10 independent models per evaluation. This cost makes IMR impractical as a routine evaluation tool. The paper does not discuss this or propose cheaper approximations.

### Trivial

- The depth-based density oversampling for IMR (Section 3.4) over-samples far-field Gaussians, which happens to be the region D²GS most improves. This could bias the metric in favor of D²GS; no sensitivity analysis is provided.

---

## Nice-to-Haves

- Ablation of λ_far and λ_middle to substantiate the empirically chosen values.
- Analysis of what happens when monocular depth estimates are inaccurate (e.g., reflective surfaces, sky regions), since DAFE relies entirely on these estimates for its mask.
- Discussion of D²GS on datasets beyond LLFF/Mip-NeRF360 (e.g., Tanks & Temples, DTU) to test generalizability.
- Clarification of the counterintuitive IMR ordering for DropGaussian vs. 3DGS, and comparison of IMR against simpler statistics (mean, variance of pairwise distances).

---

## Novel Insights

The most genuinely novel observation is that sparse-view 3DGS fails in *spatially opposed* ways—near-field overpopulation and far-field underpopulation—and that a single uniform dropout strategy (DropGaussian) exacerbates the far-field problem while only partially helping the near-field. The IMR metric, while imperfect in its exact formulation, is a genuinely new idea: treating independently trained 3DGS models as draws from a distribution over Gaussian mixtures and measuring their agreement via OT offers a path to evaluating 3D representation quality rather than proxying it through 2D rendering.

---

## Suggestions

- Provide an ablation of λ_far and λ_middle alongside the other hyperparameter ablations in Table 5.
- Add a paragraph explicitly explaining why DropGaussian has higher IMR than 3DGS in Table 3—this is a legitimate puzzle that, if explained, would strengthen confidence in the IMR metric.
- Report wall-clock training time for D²GS vs. DropGaussian baseline to characterize the overhead of k-NN computation.
- Consider reporting IMR computed with simpler aggregators (mean, std) alongside the current formula to motivate the specific form chosen.

---

## Score and Decision

D²GS is a well-motivated and clearly written paper that diagnoses a real problem in sparse-view 3DGS, proposes two complementary and principled modules, and introduces a novel robustness metric. The experimental validation is thorough, gains are consistent across datasets, and ablations are disciplined. The main weaknesses are the underexplained IMR metric design (including a counterintuitive empirical result), the lack of ablation for two key hyperparameters, and the modest increment over the DropGaussian baseline it builds upon. These are not fatal but do limit the paper's impact. Overall this is a solid contribution warranting acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>