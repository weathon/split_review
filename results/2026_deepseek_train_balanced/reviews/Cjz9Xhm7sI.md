## Summary

This paper proposes a two-component framework for 3D radar sequence prediction: **STC-GS** (SpatioTemporal Coherent Gaussian Splatting) compresses volumetric radar data into spatiotemporally tracked 3D Gaussian primitives, and **GauMamba** (a memory-augmented Mamba network) predicts the evolution of these Gaussians across time. The approach is evaluated on MOSAIC and NEXRAD radar datasets and aims to enable 512×512 resolution 3D nowcasting where raw-3D methods are limited to 128×128.

---

## Strengths

- **Memory-efficient representation enabling higher-resolution 3D nowcasting**: Fig. 5 and Sec. 4.2 provide concrete measurements showing that the Gaussian representation's memory usage scales linearly with the number of primitives (independent of spatial resolution), whereas raw-3D baselines (ConvGRU, PhyDNet, SimVP, DiffCast) scale quadratically with resolution. On 4×A100 80G GPUs, those baselines cannot be trained at 512×512 horizontal resolution, while GauMamba operates natively at this resolution. This is a genuine practical advantage that directly supports the paper's core thesis about making high-resolution 3D nowcasting feasible.

- **Systematic ablations isolate each component's contribution**: Both the reconstruction ablation (Table 4) and prediction ablation (Table 5) cleanly quantify the impact of each proposed design choice. Removing the local detail constraint increases reconstruction MAE by 32.6%; removing the memory mechanism increases prediction MAE by 20.2%; removing only the GRU gates (retaining raw memory) increases MAE by 4.1%. This provides grounded evidence that the bidirectional pipeline, dual-scale constraints, and memory-augmented architecture each contribute measurably.

- **Bidirectional reconstruction tailored to non-rigid radar dynamics**: The backward-then-forward reconstruction scheme (Sec. 3.3.2) is well-motivated. Unlike prior dynamic 3DGS methods designed for mostly-static scenes with localized motion, radar clouds exhibit continuous growth, dissipation, and deformation without rigid-body constraints. The backward pre-reconstruction propagates information about emerging regions back to the initial frame, and the ablation confirms its removal substantially degrades accuracy.

- **New dataset contributions**: The MOSAIC dataset (storms in Guangdong, China) and the reorganized NEXRAD benchmark provide two real-world 3D radar nowcasting datasets with different characteristics (7 features vs. 1 intensity channel), supporting future work in this under-resourced area.

---

## Weaknesses

### Fatal
None.

### Major

- **The headline prediction comparison is asymmetric, confounding method quality with resolution advantage**. The paper trains baselines at 128×128 horizontal resolution and GauMamba at 512×512 (a 16× pixel-count difference), then upsamples baseline predictions to 512×512 for comparison (Sec. 4.2). The stated rationale — raw-3D methods cannot train at 512×512 on the available hardware — is valid as a practical constraint, but the resulting comparison cannot cleanly attribute the reported gains (e.g., 69.0% CSI-30 improvement on MOSAIC, 101.1% on NEXRAD) to the prediction method versus the large resolution gap. A matched-resolution experiment (e.g., all methods at 128×128, or GauMamba at 128×128 vs baselines at 128×128) is needed to isolate the benefit of the Gaussian representation and GauMamba architecture from the resolution advantage. Without this, the paper's central performance claims are confounded. This is the paper's most significant weakness.

- **The "16× higher spatial resolution" claim overstates what is demonstrated**. The claim (abstract and line 21) compares the resolution at which GauMamba is evaluated (512×512) against the resolution at which baselines are evaluated (128×128). This conflates an evaluation-design choice with an intrinsic property of the method. The memory-efficiency advantage of the Gaussian representation is real and well-documented (Fig. 5), but the "16×" framing should be presented as an enabled capability ("our framework can operate at 512×512 where raw-3D methods hit memory limits") rather than a direct resolution comparison between methods.

### Minor

- **The 3D flow constraint relies on RAFT pre-trained on RGB images applied to radar data, with uncharacterized bias**. The paper acknowledges this concern (Sec. 3.3.2): "employing an optical flow model pre-trained on real-world image sequences to estimate the flow of radar sequences could introduce inductive bias, which may accumulate over iterations." The ablation (32.6% MAE increase without this constraint) shows the constraint provides useful signal, but the paper does not analyze whether the pseudo-3D flow estimates are actually correct for radar reflectivity patterns, or whether the benefit comes from a regularization-like effect rather than accurate motion guidance. This does not invalidate the results, but it weakens the claim that the reconstruction captures "physical cloud motion."

- **No uncertainty quantification or statistical significance reported**. For a weather prediction task where stochasticity is inherent, the paper reports only single-run point estimates without standard deviations or confidence intervals. While this is common in large-scale benchmark evaluations, it is worth noting given that several baselines (e.g., DiffCast) are stochastic by design.

### Trivial
None.

---

## Nice-to-Haves

- Run GauMamba at 128×128 against baselines at 128×128 for a clean matched-resolution comparison.
- Validate the RAFT-based 3D flow accuracy on radar data against a radar-specific flow baseline or a simpler temporal smoothness prior.
- Quantify the reconstruction fidelity loss of the Gaussian representation relative to raw voxels at matched resolution to substantiate the "nearly lossless" claim.
- Report inference speed and total pipeline cost including the STC-GS reconstruction preprocessing step.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Weaknesses about missing appendix content / implementation details (number of Gaussians, hyperparameters, etc.)*: Removed per hard rule — the parser strips appendices and supplementary materials from all papers; they exist in the original submission.
- *"First work for 3D-based weather nowcasting" is too broad*: Removed — the paper's scope is specifically radar nowcasting, not global weather models like FourCastNet/GraphCast. The comparison mixes different problem settings.
- *Loss function discrepancy in Eq. 9*: Removed — teacher forcing for observed steps and autoregressive rollout for later steps (both supervised against ground truth) is standard practice. No discrepancy exists.
- *Formatting artifacts ("interestTang", garbled numbers in Fig. 1)*: Removed as parser artifacts per hard rules.
- *Generic "could be" speculation without paper anchor*: Removed per filtering discipline.
- *Criticism that baselines "could" operate at 512×512 with more memory*: Removed as speculative — the paper demonstrates they cannot with the provided resources, which is the relevant practical finding.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

- **Most impactful**: Add a matched-resolution experiment — run GauMamba at 128×128 against all baselines at 128×128. This would decouple the prediction-method advantage from the resolution advantage and substantially strengthen the paper's evidential foundation.
- Reframe the "16× higher spatial resolution" claim as an enabled capability rather than an inherent method property.
- Analyze the accuracy of the pseudo-3D flow estimates on radar data, or validate the local detail constraint against an alternative (e.g., a temporal difference prior).

---

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>