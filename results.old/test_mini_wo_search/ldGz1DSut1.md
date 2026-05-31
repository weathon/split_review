Now I have all the information I need. Let me synthesize the reviews against the actual paper.

## Summary

This paper presents the first systematic study of whether deep image watermarking methods can coexist in the same image. Using eight open-source methods applied pairwise in both orders over 1020 images, it demonstrates that contrary to the intuitive expectation that the second watermark would overwrite the first, many method pairs can be sequentially embedded and independently decoded with non-zero accuracy. Building on this finding, the paper proposes watermark ensembling (combined with strength clipping and error-correcting codes) as a post-training tool to modify the capacity-accuracy-robustness-quality trade-offs of existing methods without retraining. The paper is honest about limitations, including cases where ECC+clipping on a single strong method outperforms ensembling.

---

## Strengths

- **Systematic empirical demonstration of watermark coexistence across diverse methods.** Table 1 reports pairwise accuracy for 8 watermarking methods applied in both orders over 1020 images. For many off-diagonal pairs (e.g., DwtDct with DwtDctSvd, HiDDeN followed by SSL), the first method's accuracy remains near its solo baseline while the second method also maintains high accuracy. This directly supports the paper's core claim that coexistence occurs to a much greater degree than expected.

- **Controlled analysis showing coexistence is not merely an artifact of quality degradation.** Figure 3 repeats the pairwise experiment after clipping watermark strength so that final PSNR approximates the mean of the individual methods. Even under this control, multiple pairs exhibit non-zero accuracy for both watermarks (≥25% highlighted), providing evidence that coexistence is not simply a consequence of reduced quality or robustness.

- **Demonstration that ensembling can boost capacity without retraining.** Figure 5D shows that ensembling HiDDeN (48 bits) with RoSteALS (series, clip 1.0, LC[148, 102, 14]) yields an effective capacity of 102 bits while modestly improving accuracy, robustness, and quality compared to HiDDeN alone. This directly supports the claim that ensembling increases capacity and modifies trade-offs without model retraining.

- **Honest assessment of limitations relative to simpler alternatives.** Figure 8 compares ensembles of RivaGAN+TrustMark Q against TrustMark Q alone with strength clipping and ECC (LC[100, 32, 25]) and shows the latter dominates on accuracy–quality space. The paper acknowledges cases where ensembling is not beneficial rather than overselling the approach.

- **Practical comparison of series vs. parallel ensembling.** Figure 7 shows PSNR distributions for RoSteALS+HiDDeN ensembles: series ensembling keeps all images under 40 dB, while parallel ensembling yields 5.6% of images above 40 dB. This provides a data-backed design insight for choosing ensemble order based on quality requirements.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Single dataset limits empirical generalizability.** All experiments use 1020 images from a single (anonymous) dataset. Robustness augmentations tested are limited to those used for training the considered methods. Coexistence patterns could differ across image domains (e.g., medical vs. natural images) or under unseen augmentations. The paper does not test this, so the breadth of the empirical conclusions is unconfirmed. The paper does not overclaim (it presents a first study), but this is the most significant limitation.

2. **No variance or statistical significance reported.** All results (Table 1, Figures 2–3) are point estimates over 1020 images. Confidence intervals or variance measures would help assess whether observed differences (e.g., the "improvement" of the first method in pairs like DwtDct→DwtDctSvd) are meaningful or within noise range.

3. **No perceptual quality metric beyond PSNR.** The paper acknowledges this limitation (Sec. 5: "We used PSNR as a proxy for image quality despite it not tracking human quality perception well") but does not address it. For practical use cases like the super-watermark scenario, imperceptibility is paramount. Adding a metric like LPIPS or a brief user study would substantially strengthen the real-world claims.

4. **Anonymous dataset properties are not described.** The paper references "Anon. dataset" without stating image resolution, diversity (e.g., number of classes, scene types), or whether it is a standard benchmark. This information is needed for reproducibility and for assessing how representative the testbed is.

5. **Computational cost of ensembling acknowledged but not measured.** The paper notes (Sec. 5) that ensembling requires inference through both watermarking models, but does not report wall-clock time or throughput. For practitioners evaluating whether ensembling is practical, this cost is relevant.

6. **ECC code selection lacks systematic justification.** Codes are taken from Grassl's tables, but there is no systematic search or stated criterion for choosing a specific code given a capacity target and desired robustness. Different codes would yield different trade-off curves. This makes the specific trade-off points shown in Figure 5 and Figure 6 less reproducible as optimal configurations.

### Trivial
None.

---

## Nice-to-Haves

- **Test the super-watermark scenario explicitly.** The introduction motivates coexistence via super watermarks (a second watermark indicating which decoder to use) and multi-actor provenance chains. Directly evaluating this pipeline—applying a "super" watermark, then a main watermark, then decoding both in sequence—would directly operationalize the motivating use case and strengthen the paper beyond "coexistence is possible in the abstract."

- **Deeper analysis of *why* coexistence occurs.** The paper notes that different methods likely encode in quasi-orthogonal subspaces but provides no direct evidence. A simple analysis measuring correlation between watermark residuals or checking whether the second watermark's residual lies in the nullspace of the first decoder would add significant explanatory power.

- **Systematize the ECC selection procedure.** Instead of picking codes ad-hoc from Grassl's tables, define a procedure: given a capacity budget and target accuracy, choose the code that maximizes robustness. This would make the ensembling tool more principled and reproducible.

---

## Removed Points

- **"The introduction presents scenarios as if the paper will evaluate them directly"** — The paper presents super-watermark and multi-actor scenarios as motivation, then explicitly states "That is why we conducted a comprehensive analysis demonstrating they can indeed effectively coexist." It does not promise to evaluate full pipelines. This criticism misreads the paper's scope.

- **"The 'improvement' of the first method in some pairs is likely a statistical artifact of small sample size"** — The sample size is 1020 images, which is not small. The paper already offers its own explanation ("possibly because these methods find it easier to encode noisier images"). This criticism is speculative and the paper already addresses the phenomenon.

- **"The examples in Figure 5 are somewhat cherry-picked"** — The paper presents these as illustrative examples of what ensembling *can* do and explicitly acknowledges cases where ensembling is not beneficial (Fig. 8). Showing positive examples when demonstrating capability is standard practice; the paper does not claim these are typical or universal.

- **Strength Finder strengths about "importance of the problem"** — These are generic/superficial and not kept. The remaining strengths (listed above) are concrete and evidence-grounded.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers correctly identify the paper's core empirical finding as novel and its limitations as bounded, but do not contribute a fundamentally different perspective.

---

## Suggestions

1. Report confidence intervals or bootstrapped variance for the pairwise coexistence results in Table 1.
2. Add at least one perceptual metric (LPIPS, DISTS, or a small user study) to support the claim that coexistence costs "only minor impacts on image quality."
3. Describe the dataset's properties (resolution, class diversity, source) in the main paper or appendix.
4. Measure and report the computational overhead (wall-clock time per image) of series vs. parallel ensembling.
5. In the camera-ready version, reveal the dataset name if anonymization was only for review.

---

## Score and Decision

The paper is a well-executed empirical study answering a timely and non-obvious question. The core finding (deep watermarks from different methods can coexist) is convincingly demonstrated, and the paper is honest about the limits of ensembling relative to simpler alternatives. Weaknesses are bounded and minor—no flaw threatens the core claims. The paper is publishable as it stands.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>