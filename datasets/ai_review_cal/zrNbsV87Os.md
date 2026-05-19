- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6
I now have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes SSIF (Spatial-Spectral Implicit Function), a neural implicit model that represents an image as a continuous function of both spatial coordinates and wavelengths. The key innovations are: (1) extending implicit neural representations from the spatial domain alone to the joint spatial-spectral domain, (2) incorporating the physical principle of sensor response functions as an integral over wavelength, and (3) removing the equal-spaced spectral interval requirement that constrained prior work (LISSF). The model uses an image encoder, a pixel-feature decoder, a spectral encoder, and a spectral decoder to jointly handle arbitrary spatial and spectral upsampling with a single model. Experiments on the CAVE and Pavia Centre datasets show SSIF variants consistently outperforming a range of baselines (including per-resolution-trained models like RCAN, SSJSR, SSFIN, and NIF-based models like LIIF, CiaoSR, and LISSF) across multiple spatial scales and spectral resolutions, with demonstrated generalization to unseen resolutions.

## Strengths

- **Novel architectural design for continuous spectral representation.** SSIF is the first NIF-based SSSR model that represents images as a continuous function of wavelength, enabling joint spatial-spectral super-resolution. The decomposition into a pixel feature decoder (F^x), spectral encoder (E^λ), and spectral decoder (D^{x,λ}) with response-function-weighted integration is a principled and well-motivated design. The paper clearly articulates how this differs from LISSF's 3D-CNN-based approach that requires equally-spaced spectral bands (Section 4, Figure 2).

- **Strong and consistent empirical results.** On both CAVE (31 bands) and Pavia Centre (102 bands), SSIF variants (especially SSIF-RF-GS) achieve the best or second-best PSNR, SSIM, and SAM across all tested spatial scales (p=2–16), outperforming all 10 baselines including per-resolution-trained models. Critically, SSIF does this with a single model, while the first 7 baselines are trained separately for each spatial/spectral resolution (Tables 1, 2). The paper also demonstrates generalization to out-of-distribution spatial scales (p=10,12,14) and spectral scales (C>31 on CAVE, C>102 on Pavia Centre) (Figures 3, 4).

- **Systematic ablation and analysis of design choices.** The paper evaluates four response-function/wavelength-sampling variants (RF-GS, RF-GF, RF-US, RF-UF) plus a midpoint-only variant (SSIF-M). Appendix ablations (referenced in Section 5.4) systematically test image encoders (SwinIR, EDSR, RDN), pixel decoders (CiaoSR, LIIF, ITSRN), and spectral decoders (dot product, MLP). The effect of K (number of wavelength samples per band) is ablated, showing larger K improves generalization to unseen spectral resolutions (Appendix A.9.3).

- **Data and training efficiency.** Figure 8 demonstrates that SSIF-RF-GS outperforms CiaoSR and SSIF-M at reduced data regimes (25%, 50%, 75% training data) and converges faster in early training, supporting the claim that the physics-inspired design provides practical benefits beyond raw performance.

## Weaknesses

### Fatal

None.

### Major

1. **The claimed advantage of handling irregular/non-uniform spectral intervals is not empirically tested.** The paper repeatedly emphasizes that unlike LISSF, SSIF "does not have the equally spaced spectral band requirement" (Abstract, Section 1, Section 3) and can handle "irregularly spaced wavelength intervals" (Section 2). This is presented as a primary motivation and key differentiator. Yet every experiment uses equally-spaced hyperspectral data (CAVE: 31 bands, 400–700 nm; Pavia Centre: 102 bands, 430–860 nm). The conclusion explicitly states this is "future work" (Section 6). This means the paper's claimed central advantage over LISSF is validated only in a setting where LISSF's limitation does not apply. The architectural flexibility exists on paper, but the experimental evaluation does not test the scenario that motivates it. The paper should either: (a) add a simple experiment with non-uniform intervals (e.g., constructing synthetic irregular bands from a hyperspectral image, or simulating RGB-like response functions), or (b) honestly reframe the contribution to acknowledge that the irregular-interval capability is a theoretical property not yet empirically validated.

2. **Quantitative results for spectral SR comparisons are missing from the main paper.** Section 5.4 mentions comparisons against three specialized spectral SR models (HDNet, MST++, SSRNet) and states SSIF "either outperforms or is on par" — but provides no table, figure, or numerical results in the main text, only references to appendix figures (Figure 11, 12, 13). A reader of the main paper cannot verify this claim. This weakens the otherwise strong experimental section.

### Minor

1. **The large performance gap over LISSF is not explained.** SSIF-RF-GS achieves PSNR 39.65 vs. 34.24 for LISSF at p=4 on CAVE — a 5.4 dB gap. Similar gaps appear across scales and on Pavia Centre. The table caption (Table 1) states that LISSF results are not from Ma et al. (2022) but does not clarify whether LISSF was re-implemented with the same training configuration or numbers were taken from the original paper. Since SSIF shares architectural components (SwinIR encoder, CiaoSR decoder) with the NIF family that LISSF belongs to, explaining this gap would strengthen the comparison's credibility.

2. **The data efficiency advantage (Figure 8) is confounded with supervision count.** SSIF-RF-GS uses K spectral samples per band (multiple wavelengths with response function weights), giving it many more training targets per pixel than CiaoSR (spatial-only, single value per band) or SSIF-M (single midpoint per band). The "physics-inspired design" claim for data/training efficiency cannot be separated from the fact that SSIF-RF-GS simply receives more supervisory signal per pixel. A controlled comparison that holds supervision count constant (e.g., SSIF with K=1 but using response-function-weighted sampling) would isolate the benefit of the physics-inspired inductive bias.

3. **Spectral encoder analysis (Figure 7) is illustrative but not systematic.** The observation that learned spectral embeddings resemble PL/PK basis functions is interesting, but only two cases are shown (d=5, d=10). This does not constitute a general analysis of what the spectral encoder learns. The paper would benefit from examining how these embeddings change with different training data or comparing against fixed basis functions.

### Trivial

- The ethics statement is perfunctory and the paper acknowledges this.

## Nice-to-Haves

- Testing on input images with different numbers of spectral bands at inference time (the paper tests varying output spectral resolution but input spectral resolution is fixed in each experiment).
- Error bars or variance estimates for the main tables, since SSIF-RF-GS uses random wavelength sampling.
- An ablation using a weaker image encoder (e.g., EDSR instead of SwinIR) to clarify how much of SSIF's performance comes from the backbone vs. the SSIF-specific components.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"Performance gap over LISSF is suspicious and weakens comparison credibility"** (harsh critic, framed as critical issue #2) — Demoted from "critical issue" to Minor weakness. The paper does specify that LISSF results are reported separately (not from Ma et al. 2022). The critic's assertion that the gap is "too large to be taken at face value" is speculation; such gaps are not inherently impossible and the paper's methodological differences (continuous spectral representation, response function integration) could plausibly explain them. The weakness is that the comparison setup isn't fully documented, not that the results are suspect.

- **"Missing error bars"** — Removed as a field-standard practice; single-run evaluation is common in SR benchmarking. But noted as a nice-to-have since SSIF uses random sampling.

- **"Missing related works"** — Removed per instructions; I cannot confirm what related works exist.

- **"The appendix should detail this but the reader cannot check"** — Removed per instructions; appendix sections are stripped by the parser.

- **Generic criticisms about missing reproducibility details** (hyperparameters, complete training logs) — Removed per instructions as trivial implementation details.

- **"Fatal structural flaw" framing** — The untested irregular-interval claim is a genuine gap but not fatal: the paper still demonstrates strong SSSR performance on standard benchmarks, and the architectural design is a real contribution. Demoted to Major.

- **Light source principle "dropped as redundant"** — The paper uses the dot product decoder which is presented as satisfying the spectral signature principle (Section 4.3). The harsh critic's claim that it's "never used or evaluated" is incorrect; Appendix A.9.2 (referenced in Section 5.4) evaluates the dot product vs. MLP decoder. Removed.

## Novel Insights

The most valuable insight from synthesizing the reviews is the tension between SSIF's architectural ambition and its empirical scope. The paper builds a model that, by design, handles arbitrary spectral intervals and response functions — this is a genuine step beyond LISSF. But it evaluates this model only in the standard equally-spaced setting where the distinguishing feature is irrelevant, and then acknowledges the gap as future work. This pattern — overclaiming what is empirically validated while punting the key differentiating experiment — recurs across ML papers and SSIF is a clear case study. The response-function integration (K spectral samples per band) is simultaneously the paper's most elegant physics-inspired design choice and the source of a confound in the data-efficiency claims. Separating the inductive-bias benefit from the supervision-count benefit would strengthen not just this paper but the broader line of physics-inspired neural representation work.

## Suggestions

1. **Add an experiment with non-uniform spectral intervals.** This is the single action that would most strengthen the paper. Even a simple synthetic setup — e.g., grouping the 31 CAVE bands into 8 unequal-width intervals with varying widths and overlaps — would directly validate the claimed advantage over LISSF. Without this, the paper's central differentiating claim remains untested.

2. **Clarify the LISSF comparison setup in the main text.** State explicitly whether LISSF results come from the original paper or a re-implementation, and if re-implemented, confirm that training configurations (encoder, data splits, loss) were matched.

3. **Add a controlled data-efficiency experiment.** Compare SSIF-RF-GS against a version of SSIF that uses K=1 (a single weighted sample per band) to isolate the benefit of the physics-inspired integration from the benefit of having more training targets.

4. **Move the spectral SR comparison numbers into the main paper.** At minimum, include a supplementary table reference with clear numbers in the main text, or add a compact table.

5. **Reframe claims about irregular-interval handling.** Either add the experiment or honestly state in the abstract/introduction that SSIF's architecture supports irregular intervals (unlike LISSF) but empirical validation on such intervals is left to future work.
