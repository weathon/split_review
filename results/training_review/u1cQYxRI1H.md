Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

---

Let me now write the full review.

The paper proposes IC-Light, a method for scaling diffusion-based illumination editing by adding a light-transport consistency loss during training. It builds a large dataset (>10M images from light stages, 3D renders, and synthetic augmentations) and trains on backbones from SD1.5 to Flux. The core idea is to enforce that the diffusion noise predictions satisfy ε_{L1+L2} ≈ ε_{L1} + ε_{L2} (or a learned variant thereof), motivated by the physical linearity of light transport.

**Strengths** (filtering out generic/conflicting ones from Strength Finder):

1. Large-scale data unification across heterogeneous sources (in-the-wild, 3D renders, light stages) — this is a substantial engineering effort that enables scaling beyond prior work. ✅
2. Demonstrates training across multiple backbones (SD1.5, SDXL, Flux) with plausible qualitative results — shows the approach works at different scales. ✅
3. The consistency loss ablation (Fig 4, Table 1) provides some evidence that the constraint helps (LPIPS 0.134 vs 0.178 without it). ✅
4. The normal map generation from multiple inferences is a nice byproduct that validates the model's consistency. ✅ (But paper itself says it's "empirical")
5. Unified data format (appearance + env map + mask + optional background) allows mixing diverse sources — practical for practitioners. ✅

Drop from strengths: "Preservation of intrinsic image properties" — conflicts with verified weakness that this is only qualitatively shown. "Thorough ablations" — conflicts with weakness that ablation is qualitative with only 2 examples.

**Weaknesses:**

1. **Theoretical derivation is imprecise (Major).** The paper claims ε_{L1+L2} = ε_{L1} + ε_{L2} follows from Î_{L1+L2} = Î_{L1} + Î_{L2} given Î = (I_σt - ε)/σt. This is mathematically incorrect: substituting yields ε_{L1+L2} = ε_{L1} + ε_{L2} - I_σt (not ε_{L1} + ε_{L2}). The paper also doesn't clarify whether all three predictions use the same noisy latent or different ones — the expanded loss (Eq. 5) suggests different latents, which invalidates even the approximate derivation. The learned MLP φ can absorb these discrepancies, but the claimed "physical grounding" is overstated.

2. **Intrinsic property preservation is only qualitatively shown (Major).** The paper's central claim is that IC-Light preserves albedo and fine details. Yet the only evidence is two qualitative examples in Fig. 4. No quantitative metrics (albedo MSE, reflectance consistency) are reported, even for the 3D rendered data where ground-truth albedos are available.

3. **Evaluation protocol is biased and narrow (Major).** The quantitative test set (50K 3D renders) is from the same distribution as the training data. The paper acknowledges this bias (models trained only on 3D data achieve highest PSNR) but provides no quantitative evaluation on real-world images. Given the paper's emphasis on in-the-wild capability, this is a significant gap.

4. **Sub-illumination image generation is underspecified (Minor).** The paper describes splitting the environment map L into L1 and L2, but never explicitly states how the corresponding target images I_{L1} and I_{L2} are generated, especially for the in-the-wild augmentation pipeline. While a reader can infer the approach (re-render with sub-maps using the extracted albedo and normals), this should be spelled out for reproducibility.

5. **Learnable MLP φ weakens the physical grounding (Minor).** Using φ(ε_{L1}, ε_{L2}) instead of ε_{L1}+ε_{L2} means the constraint is a learned consistency loss, not a hard physical law. φ could learn a degenerate mapping. The paper doesn't analyze what φ actually learns or whether it generalizes.

6. **The "structure-guided random image generator" failure mode is never quantified (Minor).** The paper motivates the whole approach by warning about this failure mode but provides no metric or diagnostic for it.

**Trivial:** None worth mentioning beyond what's covered above.

**Nice-to-Haves:** 
- Reporting confidence intervals for the quantitative metrics
- Evaluating on a held-out real-world relighting benchmark
- Albedo-specific metrics on the 3D test set

Now let me figure out the score. The paper has real contributions (data pipeline, trained models, practical applicability) but significant weaknesses in theoretical grounding and evaluation. I'd say it's a borderline paper.

Score: 5.5 — borderline, leaning towards reject due to overstated claims and incomplete evaluation.

Wait, let me reconsider. The paper's core claims are:
1. IC-Light enables scaling to >10M images — Supported (engineering contribution).
2. IC-Light preserves intrinsic properties — Weakly supported (only qualitative).
3. IC-Light is physically grounded — Partially incorrect (derivation is imprecise).

The FUNDAMENTAL ISSUES rule says: "If any weakness is severe enough to undermine the paper's core claims... The overall assessment must reflect this severity."

The derivation issue is real but the practical approach (consistency loss with MLP) is still useful even if the theoretical justification is imperfect. The evaluation gap is significant but not fatal — the paper still provides some evidence.

I'd score this around 5.0-5.5.

Actually, let me think about what score to assign more carefully. Let me use the typical conference scale:

10: Top 1% of papers, groundbreaking
9: Excellent, very strong paper
8: Strong accept, solid paper with minor issues
7: Good paper, clear accept
6: Decent paper, borderline accept
5: Below acceptance threshold, borderline reject
4: Weak paper, clear reject
3: Very weak, major flaws
2-1: Trivial or incomprehensible

I think this paper is around 5.0-6.0. It has real contributions (data, trained models) but the core methodological claim is overstated and the evaluation is incomplete. I'll give 5.5.

Actually, looking at this more carefully, I think the appropriate score is around 5.0. The paper has a substantial engineering contribution but the scientific/methodological contribution is significantly weakened by:
1. The flawed theoretical derivation
2. The lack of quantitative evaluation for the core claim
3. The narrow, biased evaluation protocol

These are major weaknesses that undermine the paper's claims, but the engineering contribution (dataset, trained models) is real and practically valuable.

Let me go with 5.0 — borderline to weak reject. The paper could potentially be acceptable after major revisions (addressing the theoretical imprecision and adding proper evaluation).

Now let me write the final review.Now I have a thorough understanding of both the paper and the reviewer input. Let me produce the final consolidated review.

## Summary

This paper proposes IC-Light, a method for scaling diffusion-based illumination editing by adding a light-transport consistency loss during training. The authors assemble a large dataset (>10M images combining light-stage captures, 3D renders, and synthetic in-the-wild augmentations) and train models on backbones from SD1.5 through Flux. The core idea is to enforce that diffusion noise predictions satisfy a learned variant of ε_{L1+L2} ≈ ε_{L1} + ε_{L2}, motivated by the physical linearity of light transport.

## Strengths

- **Large-scale data unification across heterogeneous sources.** Combining in-the-wild augmentations, 3D renders (Objaverse), and light-stage OLAT data into a common format (appearance + 32×32 environment map + foreground mask + optional background) is a substantial engineering effort that goes well beyond prior work's structured datasets. This is the paper's most clear contribution.

- **Training demonstrated across multiple strong backbones.** Results are shown for SD1.5, SDXL, and Flux.1-dev with qualitatively plausible illumination editing (Figs. 5, 6). This shows the approach is not tied to a single architecture.

- **Ablation evidence that the consistency loss helps.** Removing the consistency loss degrades LPIPS from 0.134 to 0.178 on the 3D test set (Table 1), and qualitative comparisons (Fig. 4) show visible color-saturation artifacts without it. This provides prima facie evidence that the constraint has a regularizing effect.

- **Normal map generation as a byproduct.** Sec. 4.3 shows that multiple relighting inferences under known directional lights can be combined to produce detailed normal maps (Eqs. 7–10). While the paper candidly calls this "empirical," it validates that the model produces physically consistent appearances across different lighting conditions.

- **Unified input/output format for diverse data types.** The common representation (I_L, L, M, B, I_d) allows seamless mixing of data from real capture, synthetic rendering, and augmented in-the-wild images during training (Sec. 3.1, Fig. 2).

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated, though they are significantly weakened.

### Major

1. **The theoretical derivation of the consistency loss is mathematically imprecise, and the claimed "physical grounding" is overstated.** The paper states (Sec. 3.2, line 78) that from Î_L = (I_σt − ε_L)/σt and Î_{L1+L2} = Î_{L1} + Î_{L2} one obtains ε_{L1+L2} = ε_{L1} + ε_{L2}. This does not follow: substituting the definition yields ε_{L1+L2} = ε_{L1} + ε_{L2} − I_σt (the noisy image does not cancel). The expanded loss (Eq. 5, line 89) further uses ε(I_{L1})_t and ε(I_{L2})_t — different noisy latents — which invalidates the premise that all predictions share the same I_σt. The paper never clarifies this discrepancy. The practical method uses a learned MLP φ(·,·) (line 80–86) that can absorb any residual, turning what is advertised as a physically-grounded constraint into a generic learned consistency loss without guarantees of physical correspondence. The paper should either correct the derivation or reframe the contribution as a heuristic consistency regularization rather than a physics-derived constraint.

2. **The central claim — preservation of intrinsic properties (albedo, fine details) — is not quantitatively demonstrated.** The paper's motivation hinges on preventing the model from becoming a "structure-guided random image generator" and on keeping albedo/reflectance unchanged. Yet the only evidence is two qualitative examples in the ablation (Fig. 4) and a general LPIPS/PSNR/SSIM evaluation (Table 1) on a 3D test set. No metric specifically measures albedo consistency (e.g., albedo MSE or cosine similarity on the 3D rendered data where ground-truth albedos are available). Without this, the paper's core claim about intrinsic property preservation is unsupported by the submitted evidence.

3. **The quantitative evaluation protocol does not support the claimed in-the-wild generalization.** The test set (50K 3D renders from Objaverse) shares its distribution with a large fraction of the training data (4M Objaverse renders). The paper itself notes that the model trained *only* on 3D data achieves the highest PSNR — confirming evaluation bias. No quantitative evaluation on real-world images (light-stage captures, in-the-wild photographs, or established relighting benchmarks) is provided. Given the paper's emphasis on scaling to in-the-wild data, the absence of cross-distribution quantitative evaluation is a significant gap.

### Minor

4. **Sub-illumination target image generation is underspecified.** The paper describes splitting the environment map L into L1 and L2 by random masking (line 86) but never explicitly states how the corresponding ground-truth appearance images I_{L1} and I_{L2} are produced for the in-the-wild augmentation pipeline. While one can infer the approach (re-render using the extracted albedo and normals with the sub-map), this should be clearly documented for reproducibility.

5. **The learned MLP φ is not analyzed.** Since the consistency loss uses a learnable φ(ε_{L1}, ε_{L2}) instead of a hard-coded sum, it can learn any mapping. The paper provides no analysis of what φ actually learns, whether it converges to a sum-like behavior on in-distribution data, or whether it might degenerate. Without such analysis, the "physical grounding" of the constraint remains opaque.

6. **The "structure-guided random image generator" failure mode is never operationalized or quantified.** This evocative phrase motivates the entire approach (Abstract, Sec. 1), but the paper offers no metric, diagnostic, or quantitative characterization of this failure mode. The ablation removes the consistency loss and shows qualitative degradation, but does not measure whether the model actually drifts toward "random" behavior in any well-defined sense.

### Trivial
None that warrant separate listing beyond the points above.

## Nice-to-Haves

- Reporting confidence intervals or significance tests for the quantitative metrics in Table 1.
- Adding an evaluation on a held-out real-world relighting benchmark (e.g., Multi-Illumination dataset, light-stage captures with novel subjects) to support the in-the-wild generalization claims.
- Providing albedo-specific metrics (MSE, cosine similarity) on the 3D rendered test set where ground-truth intrinsic decompositions are available.
- Ablating the effect of the MLP φ by comparing against a hard-coded sum (ε_{L1} + ε_{L2}) with appropriate domain adaptation.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

- *Criticism about the "vague" framing of the core problem.* The reviewer called "structure-guided random image generator" undefined and not operationalized. This is a stylistic criticism of motivation language, not a substantive flaw. Many papers use evocative language to describe failure modes. → **Removed (style complaint, not a substantive weakness).**

- *Criticism about the data augmentation pipeline being "under-described" and "not validated."* The paper explicitly references the supplementary material for full details (line 39: "See also the supplemental materials for full details"). This is standard practice. → **Removed (standard paper structure; missing appendix is a parser artifact).**

- *Criticism about CLIP filtering being "ad hoc."* The filtering by CLIP similarity to illumination-related keywords is a methodological choice, not a flaw. → **Removed (methodological nitpick).**

- *Criticism about baselines being compared without "controlling for backbone or data scale."* These are different methods with different architectures; such cross-architecture comparisons are standard in systems papers and informative for practitioners. The asymmetry does not favor the author's method. → **Removed (unfair asymmetry claim; comparison format is standard).**

- *Criticism about "no confidence intervals or significance tests."* Single-run evaluation at this scale (8×H100, 100+ hours) is the norm in large-scale diffusion training. → **Moved to Nice-to-Haves (standard practice for the field).**

- *Strength Finder's claim about "preservation of intrinsic image properties" as an unqualified strength.* This conflicts with verified Weakness #2 (not quantitatively demonstrated). → **Dropped from Strengths per instructions (weakness prevails over conflicting strength).**

- *Strength Finder's claim about "thorough ablations and comparisons."* Conflicts with verified weaknesses about qualitative-only ablation and biased test set. → **Dropped.**

- *Strength Finder's claim about "Physically-grounded consistency loss enables stable large-scale training" —* The "physically-grounded" part conflicts with verified Weakness #1 (imprecise derivation). The claim of enabling stable training is partially supported but overstated. → **Absorbed into broader Strength #1 (data unification and empirical regularizer) rather than stated as a separate strength.**

## Novel Insights

The most interesting cross-perspective observation is that both the harsh critic and the paper's own framing overstate the "physical grounding" of the consistency loss, but for opposite reasons. The paper claims the physics transfers directly to diffusion noise predictions (a clean linear relationship), while the critic argues this is fundamentally impossible. The truth is somewhere in between: the linear structure of light transport provides a plausible *motivation* for a consistency regularizer, but the implementation's reliance on a learned MLP φ to absorb domain gaps means the constraint is a soft learned regularizer, not a hard physical law. The paper would be stronger if it reframed the contribution as "a consistency regularizer inspired by light transport linearity" rather than "imposing consistent light transport." Neither the paper nor the harsh critic fully acknowledges this middle ground.

## Suggestions

1. **Correct or reframe the derivation in Sec. 3.2.** Either provide a mathematically clean derivation (accounting for the I_σt term and clarifying whether the same or different noisy latents are used) or explicitly state that the consistency loss is a heuristic regularization inspired by — but not derived from — light transport linearity. The current text overclaims.

2. **Add quantitative albedo preservation metrics.** On the 3D rendered data (where ground-truth albedos are available), report albedo MSE or cosine similarity between the model's output and the input's albedo, comparing w/ and w/o the consistency loss. This directly tests the paper's central claim.

3. **Add a cross-distribution quantitative evaluation.** Evaluate on a real-world benchmark (e.g., a held-out light-stage dataset or the Multi-Illumination dataset) to support the claimed in-the-wild generalization rather than relying solely on a same-distribution 3D test set.

4. **Analyze the learned MLP φ.** Show whether φ's learned mapping approximates a sum operation or learns something else. A simple experiment: on synthetic 3D data where ground-truth linearity holds, compare φ(ε_{L1}, ε_{L2}) to ε_{L1} + ε_{L2}.

5. **Clarify how I_{L1} and I_{L2} are obtained** for the in-the-wild augmentation pipeline, or describe the alternative approach if the same noisy latent is used for all predictions.

## Score and Decision

This paper has real value: the large-scale data pipeline, the unified training format, and the empirical finding that a consistency regularizer helps stabilize illumination editing at scale are practically useful contributions. The demonstrations across SD1.5, SDXL, and Flux show genuine scalability.

However, the paper's core methodological claim is significantly overclaimed. The theoretical derivation of the consistency loss is imprecise, the central assertion about preserving intrinsic properties is only qualitatively supported, and the quantitative evaluation is too narrow to substantiate the claimed in-the-wild generalization. These are not fatal flaws — the practical approach can still work — but they substantially weaken the paper as a scientific contribution.

The paper is currently below the acceptance threshold for a top venue. With major revisions (correcting the derivation, adding quantitative albedo metrics, and cross-distribution evaluation), it could become acceptable.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>