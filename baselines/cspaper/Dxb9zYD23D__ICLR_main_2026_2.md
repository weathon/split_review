---
job_id: 7d3b5806-e3a7-4eba-bb6f-4110a26175be
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Dxb9zYD23D.pdf
paper: Time Series as Videos: Spectro-Temporal Generative Diffusion
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on generative modeling and representation learning for multivariate time series via diffusion models and spatiotemporal architectures.

## Minimum Quality
Pass ✅. The submission includes the expected core components, namely Abstract, Introduction, Related Work, Method, Experiments, Results analysis, and Conclusion; despite several methodological and clarity issues, it clears the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes ST-Diff, a diffusion framework for unconditional multivariate time-series generation that converts each sequence into a spectro-temporal "video" using an STFT-based representation, then applies a custom video diffusion transformer over the resulting time-frequency tensor, followed by inverse STFT to recover the generated signal. The method combines trend-residual decomposition, a real/imaginary/trend tensor representation, anisotropic patching, and factorized attention across temporal, frequency, and covariate axes. Experiments on six benchmark datasets and additional longer-context ETTh settings report improved performance over prior GAN, VAE, time-domain diffusion, and image-based diffusion baselines.

## Strengths
1. The central representation choice is interesting and well motivated. Recasting multivariate time series as a spectro-temporal video is a clean way to preserve explicit temporal evolution while also exposing spectral structure. This is more compelling than simply converting the whole sequence into one static image, because the model can use temporal inductive bias at the representation level rather than hoping the architecture rediscovers it.

2. The paper does a good job illustrating the pipeline. **Figure 1** gives a concise overview of training and sampling, and **Figure 2(a,b,c)** makes the intended decomposition of the method fairly easy to follow: data transformation, backbone, and the tri-axial attention block are separated cleanly. In particular, **Figure 2(c)** helps clarify that the model is not using generic full 3D attention, but a factorized sequence of temporal, frequency, and covariate attentions, which is an important architectural choice.

3. The empirical results are broadly strong. In **Table 1**, ST-Diff is competitive or better on most dataset-metric combinations, and on several real datasets the gains over Diffusion-TS are sizeable, especially in discriminative score and Context-FID. The long-sequence ETTh results in **Table 2** are also notable, especially the predictive and discriminative scores, which suggest the approach does not immediately collapse as context length increases.

4. The method appears especially suitable for domains where spectral evolution matters, and the paper consistently argues for that inductive bias rather than selling the model as a universal black-box sequence generator. This framing is more credible than many submissions that claim broad superiority without any representation-level rationale.

5. The qualitative diagnostics are useful. **Figure 4** goes beyond t-SNE and shows ACF/PSD comparisons, which are better aligned with the claimed spectro-temporal advantages of the method. The PSD plots in particular are relevant here, since the core pitch of the paper is that spectral dynamics should be modeled explicitly.

## Weaknesses
1. **The paper is missing the most important ablations, so it is hard to tell what actually drives the gains.**  
   The main method includes several nontrivial ingredients: trend-residual decomposition with EMA (Section 4.1, Page 4), STFT video representation itself, the third trend channel, anisotropic patching and unit covariate granularity (Section 4.3, Page 5), factorized tri-axial attention, bias matrices \(B_C\) and \(B_F\), and an additional cross-covariance STFT-magnitude loss introduced only in the implementation details on **Page 7**. Yet there is no ablation table isolating any of these choices. This matters a lot scientifically. Right now, the empirical story bundles representation, architecture, and auxiliary loss into one package, so the paper does not establish whether the gains come from the "time series as videos" idea, from the custom transformer biases, from the trend handling, or simply from extra regularization. A strong paper here would at minimum report variants such as: raw STFT without trend split, 2-channel vs 3-channel input, isotropic vs anisotropic patching, no \(B_C/B_F\) initialization, no cross-covariance loss, and a generic video transformer baseline on the same representation.

2. **The comparison set is not sufficiently aligned with the paper's core claim, especially given the related-work positioning.**  
   On **Page 2**, the paper explicitly contrasts itself with frequency-domain diffusion methods and cites *Crabbé et al. (2024)* as performing generation in the frequency domain. However, this method does not appear in **Table 1** or **Table 2**. If the core claim is that modeling the joint time-frequency plane as a video is better than operating in the time domain or in a collapsed image representation, then a direct comparison to a strong frequency-domain baseline is not optional, it is precisely the nearest conceptual alternative. Without that experiment, the current evidence mainly shows ST-Diff is better than a selected set of baselines, not that explicit spectro-temporal evolution is the key missing ingredient.

3. **Several mathematical and signal-processing parts are underspecified or imprecise, and this weakens reproducibility and confidence in the inversion story.**  
   There are multiple issues here:
   - In the STFT definition on **Page 3**, the formula  
     \[
     X[m,k]=\sum_{n=0}^{L-1}x[n]w[n-mH]e^{-j\frac{2\pi k n}{L}}
     \]
     uses \(L\) in the complex exponential denominator, whereas the text separately introduces a window length \(N\). For a standard STFT, one would expect the local Fourier transform length or FFT size, not the full sequence length \(L\), to control the frequency indexing. As written, the notation mixes the global signal length and local transform parameters in a way that is at best confusing.
   - The dimensions around frequency bins are inconsistent. Section 4.1 says STFT yields \(S_k \in \mathbb{C}^{F \times T}\), while Section 4.3 introduces \(F'\) as the number of frequency patches for the frequency bias matrix \(B_F \in \mathbb{R}^{F' \times F'}\). That part is reasonable, but the paper never explicitly defines the mapping from \(F\) to \(F'\) given the anisotropic patch size. This should be spelled out.
   - The trend channel is described on **Page 4** as being "broadcasted across the frequency dimension and resampled to match the temporal dimension \(T\)." This is a delicate operation, because the trend originally lives in the time domain of length \(L\), while the STFT frames live on overlapping windows. The exact resampling/alignment rule is not stated. Is it window-averaged, sampled at frame centers, linearly interpolated, or something else? This is not a cosmetic detail, because the generated trend is later added back in the time domain.
   - Most importantly, the generative output is an unconstrained real-valued tensor containing generated \(\operatorname{Re}(S_k)\) and \(\operatorname{Im}(S_k)\). The paper assumes that applying iSTFT to these generated coefficients yields sensible residual signals, but says nothing about consistency constraints between overlapping frames, Hermitian symmetry conditions if real-signal conventions are used, or whether the generated complex STFT is guaranteed to correspond to a valid time-domain signal under the chosen STFT parameterization. The text on **Pages 3-5** treats invertibility of the STFT as if it transfers directly to arbitrary generated tensors, which is not generally true unless the coefficients are in the range of the analysis operator or the synthesis handles inconsistency robustly. At minimum, the paper should discuss this distinction explicitly.

4. **A crucial training component is introduced too late and too vaguely.**  
   On **Page 7**, the authors add "a cross-covariance loss applied directly to the Short-Time Fourier Transform (STFT) magnitudes," but this loss is nowhere formally defined. This is a major omission. If the total objective is something like
   \[
   \mathcal{L}_{\text{total}} = \mathcal{L}_{\text{DDPM}} + \lambda \mathcal{L}_{\text{ccov}},
   \]
   then the paper should specify \(\mathcal{L}_{\text{ccov}}\), how covariance is computed over batch/time/frequency/covariate indices, what normalization is used, and what \(\lambda\) is. The current wording is too loose for reproduction, and it also muddles attribution of gains. If this auxiliary loss is important, it belongs in the method section, not hidden in implementation details.

5. **The strongest empirical table is less decisive than the narrative suggests.**  
   The text claims state-of-the-art on 21 out of 24 metric-dataset combinations for **Table 1**. Even setting that aside, the table is more mixed than the prose implies:
   - In the **Correlational Score** row of **Table 1**, ST-Diff is actually slightly worse than DiffusionTs on MuJoCo (\(0.199\) vs \(0.193\)) and fMRI (\(1.661\) vs \(1.411\)).
   - In the **Predictive Score** row of **Table 1**, ST-Diff is substantially worse on Sines (\(0.186\) vs \(0.093\) for DiffusionTs and TimeGAN), and ties DiffusionTs on ETTh and MuJoCo.
   These are not fatal, but they matter because the paper's conclusion is that spectro-temporal modeling better preserves dynamics and cross-channel structure. The Sines predictive result is especially awkward, since this is the one dataset where periodic structure should favor the proposed inductive bias. The paper should not flatten these exceptions into a blanket SOTA claim without discussing why they happen.

6. **The qualitative analysis is somewhat selective and occasionally over-claimed.**  
   **Figure 4** is a useful diagnostic, but it only shows ETTh, and even there the text concedes slight mismatch at high frequencies. The statement that the plots demonstrate "near-perfect overlap" is stronger than what the figure visibly supports, especially in the PSD panels where there are noticeable deviations. Likewise, **Figure 3** uses t-SNE and KDE as evidence of distributional fidelity across all datasets, but t-SNE is notoriously projection-sensitive, and the KDE plots seem to summarize marginal density in a way that can conceal temporal and multivariate failures. These visuals are acceptable as complements, but they should not be leaned on as strong evidence. A more convincing qualitative section would include actual generated trajectories, cross-covariate joint behaviors, or failure cases.

7. **The computational cost tradeoff is acknowledged but not quantified at all.**  
   The conclusion on **Page 9** admits higher computational and memory costs due to spatiotemporal architectures, but there is no actual accounting anywhere: no parameter counts, no training wall-clock, no sampling throughput, no memory usage, and no cost comparison against Diffusion-TS or ImagenTime. This matters because the paper's architecture seems materially heavier than the baselines, and the long-sequence benefits in **Table 2** should be weighed against efficiency. If the price of the gain is a large increase in cost, the practical contribution changes substantially.

8. **The fairness of the baseline comparison is somewhat unclear because performance is taken from original papers rather than re-run under a unified protocol.**  
   On **Page 6**, the paper says, "For all baselines, we report performance from the original publications to ensure fair comparison." That is not obviously fair. Different codebases, preprocessing, splits, metric implementations, and random seeds can materially affect time-series generation results. This concern is amplified by the fact that ImagenTime has many missing entries in **Table 1**, shown as "-". If baselines cannot be evaluated under the same protocol, the strength of the comparative claim should be toned down.

9. **Novelty is decent at the representation-and-architecture combination level, but the paper overstates how unprecedented the general idea is.**  
   The paper repeatedly frames the representation shift as a new paradigm. I agree the adaptation to multivariate time-series generation is interesting, but treating spectral representations as image-like or video-like objects is already common in adjacent areas, especially audio and spectrogram-based generation. The genuinely useful contribution here is not "discovering" that STFT tensors have spatiotemporal structure, but packaging that observation into a tailored generative model for multivariate non-audio time series and showing competitive results. The positioning would be stronger if the claims were calibrated more tightly.

10. **Presentation quality is uneven despite a generally readable high-level narrative.**  
   There are numerous typos and wording issues that add friction: "taht" on **Page 4**, "spectogram" on **Page 5**, duplicated phrase "Following standard evaluation protocols" on **Page 6**, and several notation slips such as \(V_{T_{\text{ant}}}\) on **Page 3** and \(V_{T_{\mathrm{det}}}\) on **Page 4**. These look minor, but in a method paper with several tensors and transforms, notation drift makes it harder to verify exactly what is being optimized and generated.

## Questions
1. Please provide a proper ablation study. At minimum, I would want:  
   (i) no EMA trend decomposition,  
   (ii) 2-channel \((\Re,\Im)\) input vs 3-channel \((\Re,\Im,\text{trend})\),  
   (iii) generic isotropic patching vs your anisotropic patching,  
   (iv) removal of \(B_C\) and \(B_F\),  
   (v) removal of the STFT cross-covariance loss,  
   (vi) a generic video diffusion backbone on the same representation.  
   If the gains mostly survive these removals, my confidence in the core idea would increase substantially.

2. Can you formally define the additional STFT cross-covariance loss introduced on Page 7? Please give the exact formula, normalization, weighting coefficient, and which axes are used when computing the covariance matrices. Right now this part is too vague to reproduce.

3. Please clarify the STFT/iSTFT pipeline more carefully. What is the exact transform convention, what FFT size is used in the exponent in the STFT formula, how is the trend channel aligned to STFT frames, and how do you ensure that generated complex coefficients are sufficiently consistent for stable inversion? A concise algorithm box would help.

4. Did you compare against the cited frequency-domain diffusion approach of Crabbé et al.? If not, can you explain why that comparison is absent, given that it is one of the most natural baselines relative to your central claim?

5. For the long-sequence ETTh results in **Table 2**, can you provide compute and model-size comparisons versus DiffusionTs and ImagenTime? Even rough numbers, such as parameter count, GPU memory, training time per epoch, and sampling time, would materially improve the paper.

6. How should I interpret the poor **Sines predictive score** in **Table 1** relative to your thesis that spectral-temporal structure is the key advantage? Is this due to trend handling, the evaluation protocol, overfitting to richer datasets, or something else?

7. Are the baseline numbers in **Table 1** and **Table 2** produced under the same preprocessing, sequence extraction, and metric implementation as ST-Diff, or are they copied from published reports? If the latter, please discuss protocol mismatch more explicitly.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work focuses on unconditional generation benchmarks on public datasets and does not present an immediate fairness, privacy, or safety issue beyond the standard caution that synthetic time-series generation can be used in sensitive domains such as finance or healthcare.

## Soundness Rating
2: fair. The core idea is plausible and the empirical signal is promising, but important methodological details are underspecified, key ablations are missing, and some claims are stronger than the evidence currently supports.

## Presentation Rating
2: fair. The high-level story is readable and the figures help, but there are notable notation inconsistencies, missing mathematical definitions, and several writing issues that reduce clarity.

## Contribution Rating
2: fair. The representation-and-architecture combination is interesting and potentially useful, but the paper does not yet isolate the source of improvement well enough, and the experimental positioning against the closest alternatives is incomplete.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a genuinely interesting idea and promising results, but in its current form it feels under-validated for ICLR main track. The biggest issue is not that the approach is implausible, it is that too many critical ingredients are bundled together without ablation or precise specification, so the scientific takeaway remains fuzzier than the headline suggests.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. The paper is in an area I know well, and I checked the methodological claims and quantitative evidence carefully, but some implementation details are missing from the main text.