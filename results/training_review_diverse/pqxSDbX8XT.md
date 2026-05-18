## Summary

This paper proposes CAPGen, an adversarial patch generator that constrains the patch to use a small set of base colors (extracted from the environment via K-means clustering) to improve visual stealthiness. The method optimizes a color probability matrix with a temperature-regularized softmax so each pixel maps to exactly one base color. The paper further decomposes adversarial patches into pattern (color-agnostic relative pixel magnitudes) and color components, finding that patterns dominate attack performance. Based on this, it proposes a fast generation strategy: swap colors of a pre-trained high-performance patch to match a new environment without retraining. Experiments on INRIA across six detectors in white-box and black-box settings show CAPGen-P1 (pattern from AdvPatch, colors swapped to arbitrary sets) achieves mean mAP₅₀ of 22.92, close to AdvPatch's 19.58 and far below color-only CAPGen-T1 (48.04).

---

## Strengths

- **Systematic decomposition of adversarial patches into pattern and color components.** To my knowledge, this is the first paper to formally separate these two factors and quantify their relative impact. The evidence is internally consistent across multiple comparisons: CAPGen-P1 (pattern preserved, colors swapped) achieves 22.92 mAP₅₀, CAPGen-T1 (color optimized from scratch) achieves 48.04, and CAPGen-R1/R2 (random pattern) ~82 — a clean monotonic ordering that supports the pattern-dominance claim.

- **Novel method design that decouples stealth from adversarial optimization.** The color probability matrix with temperature-regularized softmax (Eq. 3) is a neat technical contribution. It forces each pixel to a single base color end-to-end via differentiable optimization, so stealth (choosing environment-matching colors) and attack effectiveness (optimizing spatial allocation of those colors) are handled by separate components without interference. The regularization on m ensures exactly-one-color-per-pixel without post-processing.

- **Comprehensive evaluation across diverse detector architectures.** White-box results span Yolov2/3/4/5s/5m and Faster R-CNN; black-box transferability is tested with five different substitute models. The pattern-dominance finding holds consistently (every cell in Tables 1 and 3 shows CAPGen-P1 beating CAPGen-T1), and CAPGen-P1 is competitive with (and in some black-box settings essentially matches) the unrestricted AdvPatch baseline.

- **The fast generation strategy, though unvalidated, is conceptually well-motivated by the pattern-dominance finding.** If patterns dominate performance, then reusing a pre-optimized pattern and merely adapting its colors to a new environment is a principled way to avoid retraining. The idea is clearly presented and follows logically from the paper's own experimental evidence.

---

## Weaknesses

### Major

- **The color replacement procedure for converting AdvPatch (continuous pixels) into CAPGen-P1 is completely unspecified.** AdvPatch directly optimizes 640×640×3 pixel values — it has no color probability matrix \(m\) and no notion of "base colors." The paper states CAPGen-P1 is created by "replacing the colors of the AdvPatch with base colors Bc1 and Bc2" but never describes the algorithm that maps AdvPatch's continuous pixel values onto a discrete set of 3 base colors while preserving the pattern. Does it run K-means on AdvPatch's pixels to obtain a pseudo-color-probability matrix? Does it assign each pixel to the nearest base color? If the latter, the quantization error alone could fundamentally alter the pattern. Without this detail, CAPGen-P1 is not a well-defined object, the pattern-dominance claim is unverifiable, and the "fast generation strategy" (which relies on this same operation) cannot be reproduced or trusted. (Sec. 4.2, Sec. 3.3)

- **Stealthiness is claimed but never quantitatively evaluated.** The paper's headline motivation is that CAPGen patches "seamlessly blend with their background for superior visual stealthiness" (abstract) and are "visually concealed in the physical environment" (conclusion). Yet: (a) there is no human perception study, no stealthiness metric, and no quantitative measurement of visual match; (b) the base colors used in all experiments (Bc1, Bc2) are **arbitrarily chosen RGB triplets** (Sec. 4.2: "We randomly select two base color sets..."), *not* extracted from actual environment images via the K-means procedure described in Sec. 3.2. This means the experimental evaluation tests color-constrained patches, not environment-adaptive patches. The only evidence for stealthiness is a qualitative reference to a physical experiment (Fig. phy_b2, not visible in the extracted text) with no controlled measurements. The paper's central value proposition — environment-adaptive visual stealthiness — is assumed rather than demonstrated.

- **The pattern vs. color comparison is confounded by asymmetric starting points.** CAPGen-P1 derives its pattern from AdvPatch (a fully trained, unrestricted adversarial patch that was optimized for attack performance alone). CAPGen-T1 learns its pattern *from scratch* via 200 epochs of gradient optimization. The 25-point gap (22.92 vs. 48.04) is large, and the claim is corroborated by CAPGen-R1/R2 (~82), so this does *not* invalidate the finding. But it is a real confound: the pre-optimized pattern in CAPGen-P1 likely has higher "quality" than what 200 epochs from scratch can achieve under color constraints. A controlled experiment (e.g., starting the same m from AdvPatch's cluster assignments vs. random initialization, both with the same colors) would cleanly isolate the contribution of pattern quality from the pattern-vs-color dichotomy.

### Minor

- **The "fast generation" claim has no timing benchmarks.** The paper asserts that color-swapping "can significantly enhance the efficiency of the adversarial attack" but provides no measurement of generation time, no comparison to the 200-epoch CAPGen training pipeline, and no demonstration that the swapped patch actually works in a new environment (the experiments use fixed color sets, not environment-specific ones extracted from a new scene). The idea is plausible but entirely unsubstantiated. (Sec. 3.3)

- **No variance or confidence intervals reported.** All results in Tables 1 and 3 are single numbers. Given that differences between methods are sometimes small (e.g., CAPGen-P1 vs. AdvPatch in black-box settings differ by <1 point on several entries), it is impossible to assess whether observed differences are meaningful or statistical noise.

- **Ablation on number of base colors (Fig. 3) uses randomly chosen colors, not environment-extracted ones.** The paper says "first randomly choose 3 colors" and then incrementally adds more colors up to 93. Since the method's purpose is environment matching, using random colors tests capacity but not the environment-adaptation claim. The trend that more colors improve attack performance is expected (less constrained) and does not inform the design choice of 3 as the default.

- **Temperature parameter τ = 0.1 is given without sensitivity analysis.** The paper states τ ensures "each pixel belongs to one of the base colors" but a single value is unexamined. Since τ controls the hardness of the softmax color assignment, it directly affects both the pattern (sharper assignments = more binary spatial structure) and the effective number of colors used per pixel.

### Trivial

- **Phrasing of the attack performance comparison (Sec. 4.3).** The paper writes: "Even AdvPatch is only 3.34 points lower than CAPGen-P1, further illustrating our approach's advantage." Since lower mAP₅₀ is better, AdvPatch (19.58) outperforms CAPGen-P1 (22.92). The intended meaning ("CAPGen-P1 is competitive despite color constraints") is clear from context, but the phrasing reads as if CAPGen-P1 has an advantage over AdvPatch, which is not true for attack performance. This should be clarified.

---

## Nice-to-Haves

- A human perception study (e.g., two-alternative forced-choice detection task, or reaction-time measurement) to directly support the stealthiness claim.
- Timing benchmarks comparing the fast generation pipeline vs. full CAPGen training (200 epochs) vs. AdvPatch training, in terms of wall-clock time.
- An experiment where base colors are actually extracted from real environment images (e.g., snow, forest, brick wall) via the described K-means procedure, with both attack performance and visual match evaluated.
- A controlled experiment for the pattern vs. color analysis: start from the same optimized color probability matrix and compare (a) swapping colors while keeping m fixed vs. (b) randomizing m while keeping colors fixed — both starting from the same initialization.
- Sensitivity study for the temperature parameter τ and confidence intervals via multiple runs.

---

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Gray patch description omission** (Harsh Critic, Other Observations): The paper does not elaborate on how the Gray patch is applied (e.g., solid gray rectangle, its size, grayscale value). This is a trivial implementation detail common in adversarial patch papers and does not affect the paper's claims. → **Removed** (trivial implementation detail).

- **"First to comprehensively examine" framing** (Harsh Critic): The reviewer suggests more cautious framing. This is a stylistic opinion about self-claims, not an error or a valid weakness of the paper's technical content. → **Removed** (opinion).

- **"The paper should also cover Y" demands from Strength Finder**: Some of the Strength Finder's claimed strengths about "environment-adaptive stealthiness" are weakened by the fact that experiments use arbitrary base colors. The strength itself is retained (method design is conceptually sound) but the overclaim is noted in the Major weaknesses. No points to remove here.

- **Harsh Critic's claim that "CAPGen-T1 has no pattern optimization at all"** is factually inaccurate: CAPGen-T1 optimizes the color probability matrix m via gradient descent, which does create a pattern (spatial allocation of colors). The real difference is that CAPGen-P1 inherits a pre-optimized pattern while CAPGen-T1 learns one from scratch. The weakness text above reflects the corrected version. → **Corrected in Minor Weakness #1**.

---

## Novel Insights

None beyond the paper's own contributions. The most interesting observation — that patterns dominate colors by a large margin — is the paper's own finding and is well supported despite the confounds noted above.

---

## Suggestions

1. **Specify the AdvPatch-to-CAPGen-P1 conversion algorithm explicitly.** If the procedure is: (a) run K-means on AdvPatch's pixels to obtain cluster centroids and assignments, (b) treat cluster assignments as a hard color-probability matrix, (c) replace centroids with Bc1/Bc2 — then say so. If a different method is used, describe it in full. Without this, CAPGen-P1 is not a well-defined experimental condition.

2. **Either evaluate stealthiness quantitatively or temper the stealthiness claims.** If a human study is infeasible, consider a proxy metric (e.g., perceptual distance between patch and background in color space, or a user study on Amazon Mechanical Turk with a modest sample size). At minimum, perform the environment-color extraction experiment (K-means on real background images) that the method describes but the experiments omit.

3. **Add a controlled pattern-vs-color experiment within the CAPGen framework only** (no AdvPatch involvement): take a CAPGen-trained patch, then create two variants — (a) swap colors preserving pattern, and (b) randomize the color probability matrix m preserving colors. This avoids the AdvPatch confound entirely.

4. **Report timing for the fast generation strategy.** Even a single number (e.g., "color replacement takes 0.3s vs. 200 epochs of training") would substantiate the efficiency claim.

5. **Include variance estimates** by running experiments with at least 3 random seeds and reporting mean ± std.

---

## Score and Decision

The paper tackles a relevant problem and contributes a technically clean method (the color probability matrix with regularized softmax) plus a genuinely interesting finding about pattern vs. color dominance. The writing is clear and the evaluation is broad across detectors. However, the paper has three major weaknesses: (1) the core CAPGen-P1 experimental condition is underspecified to the point of being unreproducible, (2) the paper's main value proposition — environment-adaptive visual stealthiness — is asserted but never quantitatively evaluated, and the experiments use arbitrary (non-environmental) colors, and (3) the pattern-vs-color comparison has an uncontrolled asymmetry. These issues collectively undermine confidence in the central claims. The paper needs substantial revision — particularly specifying the color replacement procedure, adding a stealthiness evaluation, and running a controlled pattern experiment — before it can be accepted. I cannot recommend acceptance in the current form.

**MY FINAL SCORE:** <pineapple>4.5</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>