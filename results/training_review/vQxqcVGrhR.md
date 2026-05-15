Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

DisEnvisioner proposes a tuning-free, single-image customization method that disentangles subject-essential from subject-irrelevant features via an image tokenizer (DisVisioner), then enriches the subject tokens through separate cross-attention layers (EnVisioner) to improve ID consistency. The method achieves strong text-alignment (best C-T: 0.315) and the lowest internal variance (IV: 0.026), with competitive inference speed (~2s).

## Strengths

1. **Well-motivated problem framing and clean architecture.** The paper identifies the entanglement of subject-essential and irrelevant attributes as a core challenge in single-image customization, and the two-stage pipeline (DisVisioner for disentanglement + EnVisioner for enrichment) is architecturally clean and principled. The use of separate cross-attention layers for subject and irrelevant tokens is a sensible design for controlling information flow.

2. **Demonstrates the best text-alignment and lowest internal variance among compared methods.** In Table 1, DisEnvisioner achieves the highest C-T (0.315) and lowest IV (0.026), indicating that it responds better to textual instructions and is less affected by irrelevant factors (pose, background, etc.) than baselines. The mRank (2.0) beats all competitors, including IP-Adapter (3.3) and BLIP-Diffusion (2.9).

3. **Tuning-free, single-image inference with practical efficiency.** The method requires no test-time fine-tuning, uses a single reference image, and runs in 1.96s — competitive with the fastest baselines. This combination of properties is practically valuable.

4. **Attention map visualizations provide evidence of spatial disentanglement.** Figures 4/8 (attention maps showing subject tokens attending to the object region and irrelevant tokens attending to background) give direct qualitative evidence that DisVisioner separates features by spatial region, which supports the core claim.

## Weaknesses

### Fatal
None.

### Major
- **Ablation studies are almost entirely qualitative, limiting support for key design choices.** The token-number ablation (Fig. 8) and EnVisioner ablation (Fig. 6/9) are shown only as attention maps or single qualitative examples. No quantitative metrics (C-T, C-I, D-I, IV) are reported for these ablations, making it impossible to assess whether the chosen configurations are truly optimal or whether the qualitative patterns generalize. Given that these ablations justify core architectural decisions (why $n_s=n_i=1$, why EnVisioner is needed), the lack of quantitative support is a significant gap.

- **The mRank weighting of C-I/D-I at 0.5 vs. C-T/IV at 1.0 favors the authors' method.** While the paper transparently discloses this weighting (Table 1 footnote), the choice mathematically downweights the two ID-consistency metrics. DisEnvisioner's C-I (0.828) and D-I (0.802) lag behind IP-Adapter (0.883, 0.912) and DreamBooth (0.842, 0.849). The paper argues these methods "replicate large portions of the reference image" at the cost of editability, but this trade-off is never quantified via a Pareto-style analysis. Without an explicit trade-off visualization (e.g., C-T vs. C-I scatter plot) or a user study that directly measures real-world preferences, the claim of "superior comprehensive performance" rests partly on a debatable weighting choice. The user study does show DisEnvisioner leading in all criteria, but it's relegated to supplementary with limited methodological detail.

### Minor
- **The claim that SoftMax ensures "mutual independence and orthogonality" is overstated.** The paper (line 156) states that independence/orthogonality of the two token sets is "ensured by the SoftMax(·) function applied at spatial dimension." SoftMax normalizes attention weights spatially but does not mathematically guarantee orthogonality of the resulting feature vectors. The attention maps do show spatial separation (subject vs. background), which is valuable, but the paper would benefit from a direct quantitative measure of disentanglement (e.g., cosine similarity between subject and irrelevant tokens, or reconstruction from each token independently).

- **The Internal Variance (IV) metric's interpretation could be ambiguous.** Lower IV means generated images vary less across different reference images of the same subject. As the paper defines it, this is desirable. However, low variance could theoretically also arise if the method discards legitimate identity-relevant cues that happen to correlate with viewpoint/environment. The paper's C-I/D-I scores suggest this isn't happening severely, but the concern is not explicitly addressed.

- **Baseline selection has some gaps.** The paper states it covers "all available open-source methods" but excludes SubjectDiffusion, PhotoMaker, and InstantBooth from quantitative comparison. The justification (they "still rely on multiple reference images") is reasonable for PhotoMaker and InstantBooth, but SubjectDiffusion can operate in a single-image setting and might be a more directly comparable baseline. Including it would strengthen the evaluation.

- **User study lacks detail on score normalization and significance testing.** The supplementary mentions that scores are "normalized before being reported" but does not describe the normalization procedure. The paper acknowledges that "grading differences among methods are not particularly large," yet no significance tests are reported. A simple pairwise significance test would increase confidence.

### Trivial
- Typo: "Specificallt" → "Specifically" (line 157).

## Nice-to-Haves

- A scatter plot of C-T vs. C-I (or D-I) across methods to visualize the editability–ID-preservation Pareto frontier would better contextualize the trade-off than a single weighted ranking.
- Direct reconstruction experiments using only the subject token vs. only the irrelevant token to visually demonstrate the disentanglement quality.
- Reporting quantitative ablation results (C-T, C-I, D-I, IV) for different token counts ($n_s=n_i=1$ vs. $n_s=n_i=2$) and for the variant without EnVisioner.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"DisEnvisioner achieves the lowest C-I (0.828) and D-I (0.802) among tuning-free methods"** — Factually incorrect. Among the four tuning-free methods in Table 1, DisEnvisioner's C-I of 0.828 and D-I of 0.802 are the *second highest*, ahead of ELITE (0.792/0.770) and BLIP-Diffusion (0.785/0.765). Only IP-Adapter is higher.
- **"The initialization of irrelevant tokens using CLIP class name embeddings is not fully specified for the inference scenario where the class name may not be provided"** — Misunderstanding. The CLIP class name is used to initialize the *learnable queries* during training, not during inference. After training, the tokens are fixed and no class name is needed at test time.
- **"The separate cross-attention injection in EnVisioner (Eq. 4) is a straightforward extension of IP-Adapter's dual-attention"** — This describes what the method is, not a weakness. Many good papers build on existing components in novel ways.
- **"The comparison between two-stage and single-stage training is only qualitative... A quantitative metric would be needed"** — The single-stage ablation in supplementary Fig. 11 shows a complete failure (no subject captured at all). A quantitative metric is unnecessary when the failure is catastrophic and visually obvious.
- **"The paper does not discuss possible over-compression from representing a subject as a single token"** — This is exactly what EnVisioner addresses: it enriches the single token into 4 finer-grained tokens, acknowledging and fixing the potential over-compression issue.
- **"Inference time difference is marginal"** — The paper claims "efficiency" and shows 1.96s vs. 1.98s (IP-Adapter) and 1.10s (BLIP-Diffusion). This criticism doesn't undermine any core claim; the method is clearly competitive.

## Novel Insights

Beyond the paper's own contributions, the key insight that emerges from the review process is that *explicit spatial disentanglement via tokenization* (DisVisioner) is a practical alternative to implicit disentanglement methods (BLIP-Diffusion's BLIP-2 querying, ELITE's layer-wise separation). The attention maps confirm that two learned queries can indeed partition image content spatially with minimal supervision (only a reconstruction loss), which is a non-trivial finding. However, the paper does not deeply analyze *when* this spatial separation fails (e.g., subjects with similar color to background, transparent objects, or subjects that occupy most of the frame) — understanding failure modes would significantly strengthen future work.

## Suggestions

1. **Add quantitative ablation results for token counts and EnVisioner.** Report C-T, C-I, D-I, and IV for at least three configurations: (a) $n_s=n_i=1$ (final), (b) $n_s=n_i=2$, (c) without EnVisioner (i.e., using only the single subject token). This is the most impactful improvement for the paper.

2. **Include a C-T vs. C-I scatter plot** so readers can see the editability–ID-preservation trade-off across all methods, making the mRank weighting less critical for the paper's conclusions.

3. **Clarify the "orthogonality" claim.** Either (a) replace "orthogonality" with "spatial separation" to be accurate, or (b) compute a quantitative measure (e.g., cosine similarity between $\tau^s_d$ and $\tau^i_d$) to support the claim.

4. **Describe the user study normalization procedure** and add significance tests (even simple bootstrapped confidence intervals) for the main findings.

5. **Consider adding SubjectDiffusion** to the quantitative comparison if it can be run in the single-image setting, to address the baseline completeness concern.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>