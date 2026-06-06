## Summary

The paper proposes BDSB (Brain Disk Schrödinger Bridge), a pipeline for enhancing 3T BOLD fMRI signals toward 7T quality for retinotopic decoding. The method first projects cortical surface fMRI data onto a shared 2D parametric domain via conformal mapping (producing "brain disks"), then applies an unpaired Schrödinger Bridge diffusion model with PatchNCE and BD-SSIM structural regularization. Evaluation spans three settings: synthetic (downsampled NSD as pseudo-3T), cross-dataset real (NOD 3T → NSD 7T), and a small paired dataset (TDM). The headline claim is that enhanced 3T signals become "comparable to 7T quality" for population receptive field (pRF) retinotopic decoding.

---

## Strengths

- **Conformal parameterization is validated by a thorough ablation** (Table 3): SSIM improves from 0.237 (direct slice) to 0.849 (conformal without regularization), FID drops from 226.8 to 34.23, and R̄² rises from 6.1 to 22.0. Comparing conformal vs harmonic mapping shows a meaningful gap (R̄² 22.02 vs 16.97), establishing the parameterization choice as a substantive technical contribution rather than a packaging decision.

- **BDSB achieves consistent performance gains over all five baselines across three experimental settings** (Table 2): In the synthetic setting, BDSB achieves SSIM 0.855, PSNR 25.05, FID 42.88, R̄² 24.00—outperforming the next-best competitor (OTT-GAN: 0.803/23.39/72.70/18.01) on all metrics. In cross-dataset real, it leads in both FID (70.65 vs next-best 95.91) and R̄² (25.91 vs 19.99). This breadth of improvement across diverse scenarios is a genuine strength.

- **Downstream pRF analysis (Figure 7) concretely demonstrates functional improvement**: Scatter plots of R² and receptive center estimates c_v show that enhanced signals produce markedly more stable receptive field estimates than raw 3T, with substantially reduced variance in center localization across repeated random-stimulus pRF analyses. This goes beyond pixel-level metrics and connects to the paper's neuroscience motivation.

- **The three-setting experimental design is appropriate for the unpaired learning problem**: Using synthetic data (with ground truth), cross-dataset real data (practical scenario), and a small paired dataset (TDM, as a verification probe) covers the major use cases and limitations transparently.

- **Baseline comparisons are thorough**: Cycle-GAN, OTT-GAN, OTE-GAN, SCR-Net, and fast-DDPM all serve as competitive unpaired translation baselines adapted to the same pipeline, which isolates the contribution of the SB formulation with structural regularization.

---

## Weaknesses

### Fatal
None.

### Major

- **The primary downstream metric (R̄²) is potentially circular in the cross-dataset real setting.** The paper's headline real-world result—R̄² rises from 20.26 (raw NOD) to 25.91 (BDSB enhanced) with no ground truth 7T—cannot distinguish genuine neural signal recovery from hallucination of plausible-looking high-R² visual cortex responses. The BDSB model is trained on NSD 7T data, which by construction contains high-R² BOLD patterns for pRF stimuli; a model that learns to bias outputs toward this distribution will mechanically inflate R² (Eq. 6–7) without recovering subject-specific signals. The paper does not attempt to break this circular dependence. In the synthetic experiment, R̄² gains are corroborated by SSIM/PSNR against ground truth, which partially defuses this concern in that setting; but the cross-dataset real case—which the paper frames as the most practical scenario—relies entirely on FID (distributional, not subject-specific) and R̄² (potentially circular). An independent validation such as correlation of enhanced-vs-true pRF spatial parameters (eccentricity, polar angle, size) from the synthetic setting, or V1–V3 boundary consistency, would clarify this.

- **The TDM paired experiment—the only setting with real 3T and real 7T for the same subjects—is underpowered and shows a non-trivial SSIM shortfall.** Two subjects, three training and three test runs is genuinely limited. More critically, in Table 2 (TDM Real), BDSB achieves SSIM 0.718 compared to OTT-GAN's 0.727—the only metric where BDSB is not best in its row. BDSB leads on PSNR (19.24 vs 19.18) and clearly on FID (62.09 vs 84.45), but the SSIM gap is unexplained and unacknowledged in the text. Because SSIM directly measures structural similarity to the true 7T reference, this is the most directly interpretable metric in this setting; the paper does not discuss why the method whose stated goal is structural fidelity loses on structural similarity in the real paired benchmark.

### Minor

- **The synthetic experiment conditions are unusually favorable in a way the paper understates.** The model trains on NSD subjects 1–6 and tests on NSD subjects 7–8—same dataset, same scanner, same pRF stimuli, same protocol. The leap from SSIM 0.475 to 0.855 is impressive but reflects a regime with maximal inductive bias from same-dataset training. The drop from synthetic performance to TDM Real performance (SSIM 0.855 → 0.718, PSNR 25.05 → 19.24) reveals a meaningful generalization gap that deserves explicit discussion, not just a one-line limitation about scanner hardware variability.

- **The ablation's FID vs R̄² trade-off from regularization is not discussed.** Table 3 shows that adding both PatchNCE and BD-SSIM improves R̄² (22.02 → 24.00) and PSNR (24.26 → 25.05) but worsens FID (34.23 → 42.88). The model without any regularization achieves the best FID; the full model achieves the best R̄². This reveals a genuine tension: regularization pushes signals toward brain-structural priors helpful for pRF decoding, but at some cost to distributional similarity to 7T. The paper calls BD-SSIM "critical for maintaining structural integrity… leading to notable improvements in both BOLD signal quality and functional decoding accuracy"—this is accurate for PSNR and R̄² but omits the FID cost. The trade-off should be stated explicitly so readers can calibrate when to use the regularized model.

- **Unpaired training is used even in TDM (where paired data exists), with no comparison to supervised training.** Table 1 notes that training always uses a randomly selected target subject rather than the same subject, even in TDM. The motivation for this design choice is unstated. Comparing unpaired vs supervised TDM training would (a) validate that unpaired learning is not merely a workaround for data scarcity and (b) establish how much performance is left on the table by avoiding paired supervision.

### Trivial

- Figure 7(b) restricts the receptive center comparison to the top-40 highest-R² vertices across 50 independent pRF analyses—a favorable subset. Extending the receptive field parameter agreement analysis (at minimum eccentricity and polar angle) to the full vertex set would broaden the validation.

---

## Nice-to-Haves

- In the synthetic experiment, the authors have both enhanced and true 7T pRF maps. A correlation analysis of estimated eccentricity, polar angle, and pRF size between enhanced and ground-truth 7T—beyond R̄²—would provide metric-independent evidence that spatial organization is recovered rather than just signal smoothness improved.
- For cross-dataset real, reporting per-subject R̄² and FID for the two NOD test subjects (rather than a single pooled mean) would reveal whether gains are consistent across subjects or concentrated in one.
- A brief clarification in the methods of how BOLD signals from the two datasets (NSD: 164k fsaverage; NOD: 32k fsLR) are normalized prior to BDSB training, since the absolute intensity ranges visible in Figure 5 (550–950) differ across datasets and this normalization choice affects training dynamics.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **BD-SSIM definition absent from main text (removed)**: The harsh critic noted that BD-SSIM is defined only in Appendix B.1. Per review rules, appendix content is stripped from all parsed papers and assumed to exist; this is not an author error.

- **"First approach" claim insufficiently supported (removed)**: The paper explicitly hedges with "to the authors' knowledge" and the functional vs structural MRI distinction is real. This is standard scientific hedging, not a falsifiable overclaim.

- **BOLD signal normalization as a reproducibility concern (removed as standalone weakness)**: Likely covered in the stripped appendix; retained as a minor nice-to-have clarification rather than a methodological failure.

- **Generic strength "addresses an important problem" (from Strength Finder, removed)**: Not concrete enough to include.

---

## Novel Insights

The most genuinely novel structural insight in this work is the recognition that conformal mapping—rather than direct volumetric slicing or harmonic mapping—is the critical enabler for unpaired fMRI translation across subjects. The ablation shows that even replacing conformal with harmonic mapping drops R̄² by roughly 5 points (22.02 → 16.97) and worsens FID considerably, whereas the Schrödinger Bridge formulation contributes more incrementally on top. This suggests that **the geometric alignment step is the primary driver of performance**—a finding that has implications beyond this paper for any unpaired learning task on cortical surface data. The paper positions the SB model as the headline contribution, but the ablation reveals the conformal parameterization as the indispensable foundation.

---

## Suggestions

1. **Add a spatial pRF parameter agreement analysis** (eccentricity, polar angle, pRF size vs ground truth) in the synthetic experiment to provide evidence for genuine signal recovery rather than prior-matching, directly addressing the R² circularity concern.

2. **Discuss the TDM SSIM shortfall explicitly** — even a one-paragraph acknowledgment distinguishing the SSIM vs FID trade-off in TDM would significantly improve the credibility of the results section.

3. **Add a supervised vs unpaired training comparison in TDM** to quantify the cost of the unpaired design, which would make the unpaired framework's practical value clearer.

4. **Expand Figure 7(b) from top-40 to full vertex pRF maps** or add a separate full-vertex scatter plot of eccentricity estimates (enhanced vs GT 7T) for at least one synthetic test subject.

5. **Clearly state the FID vs R̄² trade-off from regularization** in the Results or Discussion, and recommend which model variant is appropriate for which downstream use case (image fidelity vs decoding performance).

---

**Axis Evaluations:**

- **Originality**: Moderate-to-good. The combination of conformal brain-disk parameterization with an SB diffusion model for fMRI enhancement is novel; the individual components draw on prior work but the integration is meaningful.
- **Importance of research question**: Clearly relevant — 7T scarcity is a real bottleneck in computational neuroscience and BCIs.
- **Claims well supported**: Partially. Synthetic results with ground truth are convincing; the cross-dataset real headline claim rests on a potentially circular metric; TDM is underpowered with a mixed result.
- **Soundness of experiments**: Moderate. Three-setting design is appropriate, baselines are fair, ablation is thorough. Main gaps are sample size in TDM and the metric-circularity issue in cross-dataset real.
- **Clarity of writing**: Generally clear; key methodological trade-offs (FID vs R̄², TDM SSIM gap) are glossed over.
- **Value to research community**: Moderate. The pipeline and brain-disk idea are reusable; but the evidential gaps mean practitioners should treat the cross-dataset claims with caution until stronger validation is provided.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>