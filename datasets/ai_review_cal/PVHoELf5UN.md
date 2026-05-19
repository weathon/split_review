- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6
Now I have all the information needed to produce an authoritative consolidated review. Let me synthesize.

---

## Summary

The paper proposes a zero-reference (unsupervised) framework for joint low-light image enhancement and denoising. The key idea is to generate paired sub-images from a single low-light input via neighboring pixel masking (sampling adjacent pixels from 2×2 patches) and gamma correction, then train a retinex decomposition network with cross-attention to an implicit degradation representation (extracted via DCT-based frequency filters and an illumination prior) to produce consistent reflectance maps. Evaluations on LOLv1/v2, SICE, and SIDD show improvements over several unsupervised baselines.

## Strengths

1. **Novel integration of sub-image masking with gamma correction for joint denoising+enhancement.** The idea of pairing neighboring-pixel-masked sub-images with gamma-corrected versions to create a self-supervised training signal for both denoising and enhancement simultaneously is genuinely novel. Prior zero-reference methods (Zero-DCE, SCI, RUAS) do not provide this kind of paired supervision that simultaneously addresses both degradations at the feature level.

2. **Frequency-domain decomposition with interpretable physical priors in sRGB space.** The FIcoder applies channel-wise 2D DCT to extract four explicit frequency bands (low-1, low-2, high-1, high-2) plus an illumination prior, each corresponding to interpretable physical attributes (chromaticity, semantics, edges, noise). The ablation study (Table 3) confirms that each prior contributes positively, validating the design choice.

3. **Cross-attention mechanism for degradation-guided reflectance decomposition.** REFnet uses multi-head cross-attention to inject the FIcoder's implicit degradation representations into feature tokens (Section 3.2, Figure 3). This provides feature-level guidance for separating noise from reflectance distinct from prior architectures that treat denoising as a separate post-processing module or rely purely on loss function engineering.

4. **Comprehensive ablation study validating individual components.** Section 4.3 presents controlled experiments isolating: (a) the denoising design (masking + regularization, Table 4), (b) the hybrid priors (Table 3), (c) the LCnet adaptivity (Figure 8), and (d) the gamma factor sensitivity (Figure 9). The ablations consistently attribute performance gains to the specific design choices.

5. **Strong quantitative results on multiple real-world benchmarks.** The method achieves top-ranking PSNR/SSIM/LPIPS on LOLv1, LOLv2, and SICE (Table 1-2), and best no-reference scores on SIDD, outperforming several recent unsupervised methods including PairLIE on LOL datasets.

## Weaknesses

### Fatal
None.

### Major

1. **The Taylor expansion approximation grounding the self-supervised training strategy is not valid for the chosen parameter range.** The paper's core theoretical justification (Eq. 7-8, Section 3.2) relies on the approximation \(R^{\lambda-1}\approx 1\) when \(\lambda\) is "close to 1." However, the actual gamma values used during training are \(\lambda = 1/\sigma\), with \(\sigma\) sampled from (1.3, 1.7), giving \(\lambda \in (0.59, 0.77)\) — substantially *below* 1, not close to 1. For a dark pixel with reflectance \(R \approx 0.2\), \(R^{\lambda-1}\) evaluates to ~1.45–1.93, far from 1. The paper itself acknowledges at line 259 that "at higher values, the enhancement does not conform to the assumption \(R^{\lambda-1}=1\)," yet still uses the range where the assumption is violated. This does not invalidate the *empirical* method — the framework may still work as a heuristic — but it undermines the paper's claim of a "physically sound" derivation grounded in imaging principles (Contributions, line 25). The authors should either provide a valid approximation (e.g., working in log space), present empirical evidence that the approximation error is negligible in practice, or reframe the contribution as empirical without claiming physical grounding.

2. **Missing citation for the neighboring pixel masking strategy.** The core denoising mechanism — generating two sub-images with independent noise by randomly selecting adjacent pixels from 2×2 blocks (Section 3.1.2) — is identical to the **Neighbor2Neighbor** framework (Huang et al., 2021, "Neighbor2Neighbor: Self-Supervised Denoising from Single Noisy Images"). The paper cites N2N (Lehtinen et al., 2018) for the point-estimation principle but omits Neighbor2Neighbor, which introduced the exact subsampling scheme used here, including a regularizer for consistency. The paper lists "self-supervised image denoising method based on neighboring pixel masking" as a contribution (line 21), which is misleading without proper attribution. The actual novelty lies in combining this masking with gamma correction and retinex decomposition for *joint* denoising and enhancement — this should be clearly differentiated.

### Minor

3. **Ambiguity in the gamma enhancement factor notation and range.** Section 4.3 defines \(\lambda = 1/\sigma\), tests \(\sigma\) from 1.2 to 1.9, then states "we randomly sample enhancement factors within the range of (1.3, 1.7)." It is unclear whether "enhancement factors" refers to \(\lambda\) or \(\sigma\). The figure axes and text are inconsistent, making the paper's reported experimental conditions ambiguous. This matters because it directly relates to the validity of the theoretical derivation (Weakness 1).

4. **"Dynamic Discrete Sequence Fusion Transformer" appears only in the conclusion, not in the method.** The conclusion (line 266) introduces this component, but the method section (Section 3) describes only the FIcoder (a convolutional encoder combining DCT priors and illumination). This terminological inconsistency makes it unclear whether this is a renamed component or an error. The authors should align the terminology or remove the phrase.

5. **The DCT bandwidth hyperparameter \(t\) is never specified, and no sensitivity analysis is provided.** The four DCT masks (Eq. 11, line 136) are defined with threshold \(t\), described as a "manually set bandwidth hyperparameter," but its numeric value is never given in the main text. The ablation (Table 3) tests removal of entire frequency bands but not the sensitivity to \(t\). Since the high-pass and low-pass priors contribute only ~0.2 dB each, the sensitivity to this parameter matters.

6. **SIDD evaluation uses only no-reference metrics for a method claiming joint denoising.** SIDD provides ground-truth clean images, yet only BRISQUE and CLIPIQA (no-reference metrics) are reported in Table 2. Since SIDD is primarily a denoising benchmark, reporting PSNR/SSIM against the ground truth would directly validate the denoising capability. The absence weakens the evidence for the denoising component of the joint claim.

7. **The regularization term \(\mathcal{L}_{reg}\) (Eq. 14/15) is unclearly explained.** The notation \(\mathcal{D}_1(REF(I,P))\) is confusing: FIcoder is described as processing sub-images, but here \(P\) is the degradation representation for the full image \(I\). The intended meaning (mask the full-image reflectance to get sub-image reflectances, then compare differences) can be inferred but is not clearly stated.

### Trivial
- Various typos ("Denoiseing" in section title, line 243; "retinal" appears where "retinex" is meant).
- No limitations section is included.

## Nice-to-Haves
- Reporting runtime, parameter count, and FLOPs would help assess practical applicability, though not required for a method paper.
- An ablation where masking is applied but gamma enhancement is held constant (both sub-images have the same illumination) would more directly isolate the enhancement signal from the denoising signal.
- The paper promises code release, which is appreciated.

## Removed Points

Points flagged for removal; treat with caution:

- **"The method is not interpretable"** (Harsh Critic): The retinex decomposition, explicit DCT frequency bands with physical interpretations, and illumination priors do provide a level of interpretability beyond pure black-box methods. The claim is reasonable and not a weakness.
- **"Architecture details deferred to supplementary"** (Harsh Critic): The parser strips supplementary sections from all submissions. Hard rule prohibits penalizing for this.
- **"No statistical significance / variance reported"** (Harsh Critic): Single-run evaluation on standard benchmarks is the norm in this field; not a weakness.
- **"Dataset splits not described in main text"** (Harsh Critic): Deferred to supplementary; parser strips these sections. Hard rule prohibits penalizing.
- **"Missing related works"** (Harsh Critic): Hard rule prohibits mentioning missing related works. The paper already includes PairLIE (2023) and NeRCo (2023), which are recent.
- **"Comparison with more recent unsupervised methods needed"** (Harsh Critic): Related to missing related works rule. The paper includes recent baselines.
- **"The masking ablation (set1) removes masking + gamma together, not isolating gamma"** (Harsh Critic): Set1 removes masking entirely (training on full-resolution images), which necessarily removes the sub-image framework. This is a reasonable ablation design for the denoising mechanism, not a flaw.
- **"No denoising evaluation — assertion but not measured"** (Harsh Critic): Partially addressed by Weakness 6; toned down from "asserted but not measured" to a specific evaluation gap on SIDD.
- **Strength Finder claim about "principled self-supervised sub-image generation grounded in physical imaging principles"**: Conflicts with verified Weakness 1 (the Taylor expansion justification is invalid). The approach concept is novel, but the "principled/grounded" framing is not supported. This strength is modified in the Strengths section above to remove the unsupported framing.

## Novel Insights

The reviews surface a tension that the paper itself does not confront: the method's empirical success (competitive PSNR on LOL benchmarks) appears to be at odds with its claimed theoretical foundation. The Taylor expansion approximation that is supposed to justify the self-supervised training strategy is numerically invalid for the chosen gamma range. This suggests either (a) the method works for reasons different from those claimed (e.g., the network learns to handle the noise through the retinex decomposition and cross-attention mechanism even without valid zero-mean noise guarantees), or (b) the approximation is less critical than the paper asserts. The paper would be stronger if it acknowledged this gap and reframed its contribution as an empirically validated heuristic with an intuitive (rather than theoretically rigorous) motivation — similar to how many successful zero-reference methods (Zero-DCE, SCI) are presented without strong formal guarantees.

## Suggestions

1. **Fix or reframe the theoretical derivation.** The simplest path: work in the logarithmic domain where gamma correction becomes scaling and noise becomes additive, making the zero-mean property tractable. Alternatively, explicitly acknowledge that the Taylor expansion is heuristic (not rigorous) and remove claims of "physical soundness."

2. **Cite Neighbor2Neighbor** and clearly state that the masking strategy follows that prior work; the novelty is in the combination with gamma correction and retinex decomposition for joint tasks.

3. **Resolve the gamma range ambiguity** — specify whether (1.3, 1.7) refers to \(\lambda\) or \(\sigma\), and ensure notation is consistent throughout.

4. **Report PSNR/SSIM on SIDD** to directly validate the denoising capability.

5. **Align the conclusion terminology** with the method section, or remove the phrase "Dynamic Discrete Sequence Fusion Transformer" if it is not used in the method description.

6. **Specify the DCT bandwidth hyperparameter \(t\)** and include a brief sensitivity analysis.
