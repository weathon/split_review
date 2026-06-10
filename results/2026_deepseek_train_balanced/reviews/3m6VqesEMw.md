Here is my synthesized review.

---

## Summary

The paper proposes T³-S2S, a training-free triplet tuning method that enhances ControlNet+SDXL for multi-instance sketch-to-scene generation. It identifies two under-explored issues in cross-attention — imbalanced prompt energy and value homogeneity — and introduces three plug-in modules (Prompt Balance, Characteristics Prominence, and Dense Tuning) to address them without fine-tuning. The analysis in Section 3, particularly the demonstration of value homogeneity as a distinct failure mode, is the paper's strongest contribution.

## Strengths

- **Identifies and empirically demonstrates value homogeneity as a distinct failure mode beyond attention-map modulation** (Section 3.3, Figure 4). Prior training-free methods (Dense Diffusion, Attend-and-Excite) focus exclusively on attention maps. The paper isolates a separate bottleneck: tokens in the value matrices exhibit minimal numerical disparity, causing instance coupling. The diagnostic experiment — amplifying TopK values in value matrices recovers missing instances but introduces noise — honestly acknowledges the trade-off and motivates the more careful Characteristics Prominence design that operates at the feature-map level rather than directly on the value matrix.

- **Prompt Balance replaces ad-hoc weight tuning with principled energy scaling** (Section 3.2, Section 4.2). Instead of heuristic prompt-weight adjustments like "(houses:1.5)", the paper measures energy (L2 norm) imbalance in multi-instance prompts, replaces keyword embeddings with single-word embeddings, and scales them to match a reference energy level. This is a cleaner, analysis-grounded alternative to trial-and-error weighting.

- **Training-free operation on frozen models** removes data-collection barriers in copyright-sensitive domains (gaming, animation, film), which is a practical advantage over training-based approaches (GLIGEN, etc.) that require large scene-image datasets.

- **Ablation study demonstrates that each module addresses a distinct failure mode** (Figure 7, Section 5.3). Dense Tuning controls instance overlap, Prompt Balance recovers small objects, and Characteristics Prominence sharpens features. No single module solves all problems, justifying the triplet design.

## Weaknesses

### Fatal
None.

### Major

- **No quantitative comparison against the baselines listed in the paper.** Section 5.1 lists Dense Diffusion and T2I-Adapter as baselines. Section 5.2 states: "We compare CLIP-Scores for global image, instances, and background across different variants and the base ControlNet" (line 237). The quantitative evaluation (Table 1) only compares variants of the proposed method and the base ControlNet. T2I-Adapter never appears in any result. Dense Diffusion appears only in the qualitative Figure 6 (3 example scenes). The paper's central claim — that T³-S2S improves over existing sketch-to-image models — is not backed by any quantitative comparison against those models. This is the most significant weakness and undermines the paper's core contribution.

- **Small evaluation set with no statistical reporting.** The evaluation uses 20 custom-designed scenes (line 166). The paper does not report variance, confidence intervals, or statistical significance for either the CLIP-Score results or the user study. Without multiple seeds or runs, the reader cannot assess whether the reported improvements are genuine or within noise on a small, unvalidated evaluation set.

### Minor

- **Prompt Balance loses contextual information without discussion.** The module replaces keyword embeddings with single-word embeddings (Eq. 1). This means "old stone houses with a red roof" is reduced to just "houses" for that instance's embedding. The paper acknowledges no trade-off here and provides no analysis of cases where this substitution could hurt generation quality (e.g., when the descriptor carries critical semantics like "ruined stone castle").

- **Choice of energy target not justified.** The paper scales instance keywords to match the "end of text" token's energy (Eq. 2) because it "always has the maximum energy" (line 123), but provides no argument that this is the correct or optimal target. A simpler alternative like equalizing all instance keywords to their mean energy is not discussed.

- **Guidance scale of 9 not justified for SDXL.** The paper uses a guidance scale of 9 (line 164), which is unusually high for SDXL (typical range is 5–7.5). High guidance scales can produce more saturated, artificially "enhanced" images that could inflate CLIP-Scores. No sensitivity analysis is reported.

- **Heuristic grounding of TopK selection in value matrices is not analyzed.** The Characteristics Prominence module uses TopK indices from value matrices to identify which tokens to enhance (Eq. 3). The paper does not analyze what these TopK indices semantically represent across different layers and channels, or why values in V should correspond to tokens that need feature-map amplification rather than, e.g., attention-map amplification.

- **Dense Diffusion adaptation to SDXL is underspecified.** The paper applies Dense Diffusion (designed for SD 1.5) to SDXL "for a fair comparison" (Figure 6 caption) but provides no details on how the architecture adaptation was done.

### Trivial
None.

## Nice-to-Haves

- Release the 20 custom sketch scenes, prompts, and evaluation annotations so the community can build on this work.
- Test whether Prompt Balance's single-word substitution hurts generation for prompts where adjectives carry critical semantic weight (e.g., "a ruined stone castle").
- Include a discussion comparing against layout-to-image methods, even if only to formally argue why they are not applicable to sketch inputs.

## Removed Points

These points were raised in the input reviews but are removed as invalid or filtered:

- **User study insufficiently described**: The paper explicitly states "Details can be found in Appendices C and E" (line 167). Per hard rules, weaknesses about missing appendix content are removed — the parser strips appendices from all papers.
- **Triplet framing inflates novelty**: The paper is transparent that Dense Tuning is "adapted from Kim et al. (2023)" (line 106). The contribution is honestly scoped.
- **No code release or reproducibility checklist**: Per hard rules, reproducibility nitpicks about large artifacts impractical to include are removed.
- **No comparison to layout-to-image methods**: The paper already explains (line 37) that "these box-based approaches struggle with simple sketch inputs and fail to strictly follow the designer's sketch."
- **No quantitative ablation table**: Table 1 does provide quantitative CLIP-Score comparisons across variants. The point is factually incorrect.
- **Dense Diffusion adaptation may be unfair**: Speculative claim about a comparison the paper cannot control.
- **Various formatting/style nitpicks, hypothetical concerns about missing sections**: Removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves did not make.

## Suggestions

1. **Quantitatively compare against Dense Diffusion and T2I-Adapter** on the 20 scenes (or more). Without this, the central claim of improving over existing methods is unsubstantiated.
2. **Expand the evaluation set** to ≥100 scenes from an established benchmark adapted with sketch inputs, and report CLIP-Score variance across multiple seeds.
3. **Acknowledge and evaluate the context-loss trade-off** in Prompt Balance — e.g., compare single-word substitution against retaining full-phrase embeddings on a curated set of attribute-critical prompts.
4. **Justify the guidance scale of 9** or repeat key comparisons with a range of guidance scales to show the improvement is not an artifact of high guidance.
5. **Provide the TopK selection analysis**: what do the TopK indices in value matrices correspond to semantically across layers and channels? This would strengthen the theoretical grounding of Characteristics Prominence.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>