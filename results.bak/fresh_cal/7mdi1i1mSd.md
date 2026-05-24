Now I have a comprehensive understanding of the paper. Let me compose the final review.

## Summary

This paper proposes NoisyTraj, a plug-and-play framework for trajectory prediction under noisy observations. The method has three components: (1) a mutual information-based loss that encourages denoised trajectories to share information with clean future trajectories while discarding noise-related information from noisy observations, (2) a masked reconstruction loss to preserve trajectory structure, and (3) a ranking loss that ensures predictions from denoised observations outperform those from noisy observations. The framework is evaluated on ETH/UCY and SDD datasets with multiple backbones (GraphTern, EqMotion) under Gaussian, Poisson, mixed, and multiplicative noise, showing substantial improvements over both raw backbones and traditional denoising baselines.

## Strengths

- **Well-motivated problem with quantified severity**: Figure 1 explicitly demonstrates that adding Gaussian noise (σ=0.4) causes FDE to rise from 0.35–0.45 m to 0.60–0.75 m on ETH/UCY and from 13–15 px to 18–20 px on SDD across four SOTA methods, establishing a clear need for robust prediction under noise.

- **Novel MI-based denoising with tractable bounds**: The paper derives a practical objective (Eq. 10) combining CLUB upper bound for \(I(X_{obs};\hat{X}_{obs})\) and MINE lower bound for \(I(\hat{X}_{obs};Y_{fut})\), providing a principled mechanism to suppress noise while retaining predictive signal. Ablation (Table 3) confirms this alone reduces ADE from 0.57 to 0.42 on ETH/UCY (σ=0.4).

- **Consistent large-margin improvements across diverse settings**: NoisyTraj+GraphTern reduces ADE from 0.57 (GraphTern) to 0.39 on ETH/UCY under Gaussian noise (σ=0.4), and from 23.15 (GraphTern) to 14.05 on SDD under Poisson noise. These gains hold across four distinct noise types (Table 4a–d) and two prediction backbones (Tables 1–2).

- **Generalization to unseen noise at test time**: Table 5 shows that when trained on Gaussian noise (σ=0.4) and tested on Poisson noise (λ=0.4), NoisyTraj+GraphTern achieves ADE 16.80 vs. GraphTern's 23.15 and Wavelet+GraphTern's 20.62 (SDD), confirming the approach does not overfit to a specific noise distribution.

- **Plug-and-play compatibility**: The framework integrates with both GraphTern and EqMotion, consistently improving performance — e.g., on SDD with σ=0.4, NoisyTraj+EqMotion achieves ADE 19.71 vs. EqMotion alone at 28.43 — showing the approach is not tied to a single architecture.

## Weaknesses

### Fatal
None.

### Major

- **The Trajectory Denoise Model (TDM) architecture is not specified.** The paper repeatedly refers to \(\Phi_{\mathbf{TDM}}\) as the core module that takes noisy trajectories and outputs denoised trajectories, but never describes its architecture — not even whether it is an MLP, transformer, RNN, or graph network, let alone layer counts, hidden dimensions, or input/output shapes. Figure 2 shows a framework diagram but does not expose TDM internals. Since the entire method hinges on this module being able to learn effective denoising, a reader cannot assess whether its capacity is appropriate, nor reproduce the work. This is a structural omission that must be addressed for publication.

- **The mutual-information optimization procedure is underspecified.** The loss \(\mathcal{L}_{MI}\) involves two auxiliary networks: a variational network \(q_\phi\) (for the CLUB upper bound on \(I(X_{obs};\hat{X}_{obs})\)) and a critic network \(T_\psi\) (for the MINE lower bound on \(I(\hat{X}_{obs};Y_{fut})\)). The paper presents only the final loss (Eq. 19) and states "By minimizing the upper bound \(\mathcal{L}_{MI}\)" (line 136), but never describes how \(q_\phi\) and \(T_\psi\) are trained — whether jointly with the main model, in alternating steps, with separate optimizers, with gradient clipping, or with any stability measures. Min-max optimization of MI bounds is known to be delicate; without methodological specifics, the reported results cannot be fully trusted to be stable or reproducible.

### Minor

- **The reconstruction loss targets noisy observations without sufficient analysis.** Equation (12) defines \(\mathcal{L}_{rec}\) as the L2 distance between the produced masked trajectory and the **original noisy** \(X_{obs}\) at masked positions. The paper states this "preserves structure information" but does not explain why training a model to reproduce noisy positions is beneficial for denoising, nor analyze the tension between \(\mathcal{L}_{rec}\) (which rewards fidelity to noise) and \(\mathcal{L}_{MI}\) (which penalizes noise-related information). The ablation shows this combination works empirically (Table 3), but the mechanism remains unexplained. A controlled experiment comparing against reconstructing clean targets (if available) or a noise-agnostic variant would strengthen the paper.

- **No statistical variance or significance is reported.** All tables report single numbers without error bars, confidence intervals, or multiple-seed experiments. While the improvements are large, the reader has no way to assess the stability of results. This is a standard expectation for empirical papers.

- **The clean-future assumption is acknowledged but not discussed as a limitation.** The paper states (Sec. 3.1) "we simplify the problem by assuming \(Y_{fut}\) are clean" but never returns to discuss how realistic this is in practice or what would happen if future observations were also noisy. Since the method uses future trajectories as a clean signal to guide denoising of the past, this assumption is consequential and should be explicitly examined as a limitation.

### Trivial
None.

## Nice-to-Haves

- A denoising autoencoder (DAE) baseline, trained to map noisy observations to clean observations, would be a natural additional comparison point beyond the current Wavelet and EMA baselines.
- A brief discussion of why simple denoising methods (e.g., Kalman smoothing, DCT-based smoothing) are insufficient would help position the contribution.
- The conclusion is very brief and would benefit from a discussion of limitations and future work.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about not discussing existing denoising trajectory works** (Kalman smoothing, DCT): This is a missing-related-works criticism, which per policy is removed since I cannot confirm what works exist beyond what is cited.
- **"The reconstruction loss is conceptually inconsistent with denoising"** framed as a fatal issue: The paper provides ablation evidence that this combination works, and the self-supervised masked-reconstruction + MI-discrimination setup is a known paradigm. The criticism is retained in Minor form (insufficient analysis), but the stronger "fundamentally inconsistent" framing was removed as it overstates the issue given the empirical support.
- **Criticism about generalizability experiment (σ=0.4→σ=0.2 being "within-distribution")**: Table 5 also tests Poisson noise (cross-distribution generalization), so this criticism is partially inaccurate.
- **"The paper cannot be accepted in its current form" is a conclusion, not a weakness to include.** It is reflected in the overall score and decision.

## Novel Insights

None beyond the paper's own contributions. Both reviews largely recapitulate the paper's claims and noted missing details; no synthesis yielded a fundamentally new observation about the method or its implications.

## Suggestions

1. **Specify the TDM architecture** — describe the number of layers, hidden dimensions, activation functions, and whether it is an MLP, transformer, or other architecture. Include this in the main paper or supplement.
2. **Describe the MI optimization procedure** — explain how \(q_\phi\) and \(T_\psi\) are trained (jointly or alternating; optimizer and learning rate; whether gradient clipping or warm-up is used) and how the min-max is implemented in practice.
3. **Add error bars or multiple-seed results** for the main tables (at least 3–5 seeds) to establish statistical reliability.
4. **Provide a more thorough analysis of the reconstruction loss** — e.g., compare against a variant that reconstructs *clean* observations (where available as ground truth during training) to isolate the effect of the noisy reconstruction target.
5. **Expand the limitations discussion** — address the clean-future assumption, potential failure cases, and the scope of noise types for which the method is theoretically guaranteed to work.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>