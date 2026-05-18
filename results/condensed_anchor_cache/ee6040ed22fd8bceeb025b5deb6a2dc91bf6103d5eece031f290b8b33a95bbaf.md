- Decision: Reject
- Scores: 3, 3, 1, 1

## Merged Review

### Summary
The paper proposes Diffusion SigFormer, combining a diffusion-based denoising module (DSDM) and a transformer with 1D convolutional layers (SigFormer) for interference time-series signal recognition. It is evaluated on RML2016.10a, RML2016.10b, and a Bluetooth dataset. Two reviewers rate the paper 3 (positive leaning) and two rate it 1 (strongly negative), indicating substantial disagreement on novelty, clarity, and experimental sufficiency.

### Strengths
1. The application of diffusion models with a Transformer for interference signal recognition is novel and addresses a gap; using a diffusion-denoising model to separate noise in time-series data is conceptually sound. (R1, R2)
2. A signal interference mechanism is designed, and SigFormer combines Transformer with convolution for both local feature extraction and global context modeling. (R1)
3. Results are well-presented with thorough comparisons against existing models on relevant benchmarks. Visualizations (Figures 4,5) and Table 1 demonstrate feasibility. (R1, R2)
4. Comparisons with several basic architectures (LSTM, ViT, Mamba, CNN-based models) are included. (R4)
5. The topic of electromagnetic signal recognition with interference is interesting. (R3)

### Weaknesses
1. **Grammatical errors and readability** – The manuscript has numerous grammatical mistakes (e.g., missing articles, pronoun agreement) and sentences that are difficult to follow. Examples: Abstract and lines 45, 81 in Introduction. The writing quality needs significant improvement. (R1)
2. **Missing figure captions and unclear illustrations** – Figures lack captions; Figure 1 does not clearly show how different noise types are added, has overlapping legend, rough borders, missing/directionless arrows in the diffusion process. Figure 2 blocks need explanation. It is unclear if the diffusion process uses only four steps or if an ellipsis is missing. (R1)
3. **Undefined or erroneous mathematical notation** – Symbol \(\sigma_t z\) is not explained; the derivation from Formula 3 to Formula 4 appears incorrect and lacks detail. Full notation definitions and a correct, step-by-step derivation are needed. (R1)
4. **Limited novelty and integration** – Diffusion models and transformers are well-researched; the paper appears to be a straightforward patchwork of existing techniques without sufficient adaptation or innovation. SigFormer is just a simple combination of Transformer and convolution. The paper does not clearly differentiate which parts are novel versus off-the-shelf. (R1, R3, R4)
5. **Lack of ablation experiments** – No experiments verify the role of each component. Required ablations include: (a) constraining the diffusion step number \(t\) to 1 vs. using \(t\) as input vs. original diffusion, (b) the effect of the SIR noise constraint, (c) isolating DSDM from noise augmentation, (d) verifying SigFormer’s modifications (1D convolution) and the claim that the original Transformer causes training instability. (R1, R4)
6. **Unaddressed phase problem** – Applying DDPMs to time-series data causes phase mismatch between real and imaginary parts (visible in Figures 4,5). The paper does not explain how the model overcomes this or why it does not degrade performance in Table 1. (R2)
7. **Confusion about experimental setup** – In Table 3, it is unclear whether the CNN-based model, SigFormer, and ViT all include the DSDM process or only SigFormer does. Also, Gaussian, Rayleigh, and Periodic noises appear to have no significant performance difference, but the reason is not discussed. (R2)
8. **Mismatch between method description and appendix** – The DSDM description and formula in Section 2.3 do not match the algorithm in Appendix A.3, which seems to be the correct version. Placing the algorithm in the related work section confuses whether DSDM is the authors’ proposal or an existing method. (R4)
9. **Inability to attribute improvement** – Adding noise to training data is a long-established technique, so the experiments cannot distinguish whether gains come from DSDM’s denoising or from training with noisy data. (R4)
10. **Incomplete related-work positioning and missing citations** – The Introduction criticizes only traditional methods, not recent AI approaches; newer methods cited in A.1 and A.2 are not analyzed or compared. The paper should cite (e.g.) Eldele et al. (ICML 2024) for 1D conv in Transformers and Li et al. (ICLR 2024) for conditioned signal-side diffusion, and discuss how they relate to SigFormer. Each scientific claim should be backed by relevant prior work. (R3, R4)