- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 1, 8
Now I have thoroughly read the paper and verified all claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes Channel-dimension Fourier Transform Learning (CFTL) for image enhancement. The core idea is to apply a 1D Fourier transform along the *channel* dimension of a global-pooled feature vector, learn channel-wise modulations of the amplitude and phase components, then invert the transform. Three variants are introduced (high-order moments, grouped channels, spatial-Fourier combination). The method is evaluated by plugging it into several existing backbones (DRBN, Restormer, LCDPNet, CSRNet, UIEC²-Net) across four enhancement tasks (low-light, exposure correction, SDR2HDR, underwater).

---

## Strengths

1. **Novel application of channel-dimension Fourier transform.** Prior Fourier-based works in image enhancement operate along the spatial dimension (e.g., FECNet modulates spatial amplitude). Applying FFT along the channel dimension of a global-pooled vector to modulate amplitude and phase in that space is a genuinely new idea. The toy experiment (Fig. 4, Section 4.1) directly validates that channel-dimension FFT features achieve higher distribution distance between under- and over-exposed samples than spatial FFT or global pooling, supporting the discriminability claim.

2. **Broad experimental scope.** The method is tested on four distinct enhancement tasks (low-light, exposure correction, SDR2HDR, underwater) with multiple backbones (DRBN, Restormer, LCDPNet, CSRNet, UIEC²-Net) and across multiple datasets per task (LOL, MIT-FiveK, SICE, MSEC, HDRTV, UIEB). This breadth demonstrates the plug-and-play nature of the module.

3. **Systematic ablation studies.** Table 5 ablates key design choices (removing global pooling, omitting IFFT, processing only amplitude or only phase) across two datasets, confirming that each component contributes. Figure 7 shows the effect of varying the number of CFTL blocks. These ablations give confidence that the design is empirically grounded.

4. **Multiple efficiency-oriented variants.** The paper offers three implementation formats (High-order, Group, Spatial-Fourier) that provide performance-efficiency trade-offs, with the Group variant reducing parameters while maintaining competitive results.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing control experiment: FFT vs. learned linear projection.** The paper never compares CFTL to a version where the 1D FFT/IFFT is replaced by a learned linear transformation (e.g., an MLP or two fully-connected layers with activation) of the same output dimension applied to the same pooled vector. Without this control, it is impossible to attribute the reported gains to the Fourier operation itself rather than to the extra parameters, the channel-wise modulation structure, or simply the attention mechanism. This is the single most critical missing experiment for the paper's central claim. *(Verified from paper: no such comparison appears in the main text or ablations.)*

2. **No error bars, variance, or multiple-run statistics.** The paper reports only single numbers for each configuration. Given the small magnitude of improvements typically reported in this domain, it is impossible to assess whether the 0.1–0.3 dB gains are systematic or within the noise of random initialization and training variance. Running each configuration at least 3 times with different seeds and reporting mean±std is standard practice for this community. *(Verified: no mention of multiple runs, seeds, standard deviation, or statistical tests anywhere in the paper.)*

### Minor

3. **Underspecified baseline definitions.** The "Pooling Attention" and "Spatial Fourier" comparison operators are named but not defined in the body — the reference reads "as illustrated in Sec." (line 218) with an incomplete section number. The reader cannot assess whether these baselines are fairly configured or whether "Spatial Fourier" corresponds to a simple amplitude modulation (à la FECNet) or something different. *(Verified: line 218 is truncated.)*

4. **Minimal training details.** The paper states "We train all baselines and their integrated formats using their original settings until they are converged" (line 225) with no information about learning rate schedules, data splits, number of epochs, or whether hyperparameters were re-tuned for each CFTL-integrated variant. This makes independent reproduction difficult and fairness across comparisons hard to assess. *(Verified: no further training details provided.)*

5. **No computational cost numbers.** The abstract and contributions claim "negligible computation costs," but no FLOPs, parameters, or latency figures are reported in the main text. The only parameter comparison appears in a table image (Table 2), which the reviewer could not fully verify. A module paper claiming low overhead should present this data explicitly. *(Verified: grep for FLOPs/latency/MACs returns no matches in main text.)*

6. **Incomplete connection between toy experiment and end-to-end improvement.** The toy experiment (Section 4.1, Fig. 4) shows that channel-FFT features better separate under- vs. over-exposed samples. However, the paper does not demonstrate that this improved discriminability in a *pooled global vector* causally translates to better *pixel-level* enhancement in an end-to-end network. The connection is intuitive but not empirically supported. *(Verified: the paper asserts this connection via Fig. 1c but does not provide causal evidence linking discriminability to final PSNR.)*

### Trivial

None.

---

## Nice-to-Haves

- A direct comparison to a full, recent SOTA method (e.g., Retinexformer for low-light) showing that CFTL can improve a top-performing model, not just mid-range backbones.
- An analysis of which moment orders (k values) matter in the High-order variant, to justify the choice.
- Ablation comparing CFTL-Net against the backbone alone to quantify its standalone performance vs. the plug-in variants.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Spatial-Fourier CFTL variant is underspecified (refers to Fig. 10/Eq. 10 which are not in the body)"** — Removed per rule: the parser strips appendix sections from all papers; these references exist in the original submission and are not missing.
- **"The motivation claim that previous works 'operate only in the spatial dimension' is inaccurate because SENet/CBAM do channel attention"** — Removed: the paper specifically refers to Fourier-transform-based works operating in the spatial dimension, not all attention mechanisms. The reviewer misread the text.
- **"No comparison to FECNet as a full method"** — Removed: the paper's contribution is a plug-in module, not a full method; FECNet is discussed as prior spatial-Fourier work and the paper's baselines are the base networks, not full competing methods. The reviewer's concern about comparing CFTL-module vs. FECNet-module on the same backbone is reasonable but belongs in Nice-to-Haves.
- **"Limited architecture diversity / no diffusion-based methods"** — Removed: the paper already tests on CNN and transformer (Restormer) backbones across four tasks. Demanding diffusion-based enhancement models extends beyond the paper's stated scope.
- **Multiple nitpicks about formatting, missing related works, and speculative concerns about table image readability** — removed per filtering rules.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add the critical control experiment**: Replace the 1D FFT/IFFT in CFTL with a learned linear projection (e.g., two FC layers with LeakyReLU) of the same output dimension on the same pooled vector. If CFTL outperforms this control, the Fourier operation itself adds value. If not, the gains come from the channel-wise modulation structure, not the Fourier transform.
2. **Report mean and standard deviation** across at least 3 random seeds for all main results.
3. **Complete the broken reference** defining "Pooling Attention" and "Spatial Fourier" baselines.
4. **Provide FLOPs/parameter/latency comparisons** in a main-table format to substantiate the "negligible computational cost" claim.
5. **Add more training details** (learning rate schedule, epochs, data splits) to improve reproducibility.

---
