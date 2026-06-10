Now I have a solid understanding. Let me write the final consolidated review.

## Summary
This paper decomposes CLIP-ViT's image representation into contributions from individual layers, attention heads, and image tokens, then uses CLIP's shared text-image space to label these components with text descriptions via a proposed algorithm, TextSpan. Key findings are that the last 4 MSA layers dominate the representation, many heads have coherent property-specific roles, and the token decomposition yields SOTA zero-shot segmentation on ImageNet-segmentation (54.50% mIoU). The identified head roles also enable targeted removal of spurious features, improving Waterbirds worst-group accuracy from 47.7% to 72.9% on ViT-L.

## Strengths

1. **Systematic mean-ablation establishes that the final 4 MSA layers dominate CLIP-ViT's representation with quantitative evidence.** Table 1 shows mean-ablating all MLPs reduces accuracy by only 1–3% across ViT-B/L/H, and Figure 1 shows ablating MSA layers up to the last 4 leaves accuracy nearly unchanged while ablating those last 4 causes a drastic drop. This evidence-based justification for focusing on late attention layers is a concrete methodological contribution that prior interpretability work has not provided.

2. **TextSpan recovers 96.7% of CLIP's zero-shot accuracy using only 60 text-interpretable directions per head, with the ChatGPT pool consistently outperforming baselines.** Figure 3 shows 60 descriptions per head reach 72.77% ImageNet accuracy (vs. 75.25% baseline), and the ChatGPT pool outperforms both common-word and random-vector baselines across all output sizes. This validates that the text directions capture meaningful variation in head outputs — a stronger quantitative check than prior neuron-level interpretability work has provided.

3. **The token decomposition yields zero-shot semantic segmentation that outperforms six prior methods on every metric.** Table 3 reports 75.21% pixel accuracy, 54.50% mIoU, and 81.61% mAP — each higher than LRP, GradCAM, rollout, raw attention, partial-LRP, and Chefer et al. (2021). The mIoU improvement over the best prior method is 7.03 percentage points, a substantial and clean margin.

4. **The joint decomposition (heads × tokens) provides compelling spatial verification of text labels.** Figure 5 shows that for a geolocation head (L22H13), the image tokens contributing most to the "Paris" direction correspond precisely to the Eiffel Tower region — cross-modal alignment that validates the TextSpan basis directions spatially.

## Weaknesses

### Major

1. **The Waterbirds experiment conflates TextSpan's contribution with human domain knowledge, weakening the causal claim.** The paper states: "we manually annotated the role of each head using the text descriptions from TextSpan" (line 294) and then selectively ablated "geolocation" and "image-location" heads. The abstract's headline claim — "we can reduce spurious correlations by removing heads associated with the spurious cue" (line 25) — omits the manual annotation dependency. The "best-of-5 random draws of 10 heads" baseline does not control for the human selection, because the manual annotation leverages knowledge of the dataset bias and the specific head identities in a way a blind ablation cannot. The experiment demonstrates that *a human with TextSpan outputs and knowledge of the Waterbirds spurious cue* can improve worst-group accuracy, but it does not cleanly demonstrate that TextSpan *alone* enables this. A controlled protocol (e.g., automating head selection using a fixed keyword-based criterion derived purely from TextSpan outputs) would support the causal claim.

2. **The number of heads ablated in the Waterbirds experiment is never reported.** The random baseline ablates 10 heads, but the paper never states how many "geolocation + image-location" heads were ablated in the targeted condition. Without this number, the comparison to random ablation is incomplete. The large variance across model sizes (ViT-B: 45.6→57.5; ViT-L: 47.7→72.9; ViT-H: 37.2→43.3) also goes unexplained — if the method is sound, the wide variability warrants discussion.

### Minor

1. **The TextSpan candidate description pool was manually expanded based on patterns found in the heads being analyzed, introducing circularity for the qualitative interpretability claims.** The paper states: "After obtaining an initial set, we manually prompt ChatGPT to generate more examples of specific patterns we found (e.g. texts that describe more colors)" (lines 270–271). Because TextSpan's output is constrained by whether the right descriptions are in the pool, expanding the pool to cover patterns observed in the data inflates the apparent semantic coherence of the discovered bases. The baselines (common words, random vectors) do not test whether the pool construction is fair — they test different hypotheses (text semantics matter, directions are non-random). This primarily affects the qualitative head-role claims rather than the core quantitative results (segmentation is independent of this pool; Figure 3's recovery accuracy would catch severe overfitting), but it is a methodological concern worth addressing.

2. **The segmentation comparison lacks a baseline that isolates the decomposition from using CLIP's text-aligned space.** The method computes inner products between token-level contributions and CLIP text representations — leveraging CLIP's own joint embedding space as the similarity metric, an advantage that compared methods (LRP, GradCAM, rollout, Chefer et al. 2021) do not have. While "raw attention" (65.67% pixel acc) is a partial control, a matched baseline — e.g., directly computing cosine similarity between the class-text embedding and each image patch's final-layer embedding — would isolate whether the improvement comes from the decomposition framework or from simply using CLIP's text-aligned space as the comparison metric.

3. **The phrase "uncover an emergent spatial localization within CLIP" (line 7) overstates novelty.** Extensive prior work (DINO, Chefer et al., Caron et al. 2021) has established that ViT attention maps encode spatial information; CLIP-ViT inherits this from the ViT architecture. The paper's contribution is in quantifying and leveraging this property using CLIP's text-aligned space for segmentation, which is valuable — but the phrasing implies discovery of a new phenomenon rather than characterization of a known one.

4. **The joint decomposition (heads × tokens) is evaluated only qualitatively.** Figure 5 is visually compelling, but some quantitative measure (e.g., fraction of heatmap mass within the described region, or alignment with ground-truth masks where available) would strengthen the claim that "it validates our text labels" (line 33).

### Trivial

- The paper uses "direct effect" to describe mean-ablation experiments, but because residual connections pass the ablated output to downstream layers, the ablation measures a mix of direct and indirect effects. The finding itself is robust and interesting — the terminology is imprecise but does not affect the conclusions.

## Nice-to-Haves
- Automating the Waterbirds head-selection process (e.g., using keyword-based criteria on TextSpan outputs) would turn a human-dependent demonstration into a clean validation.
- Adding the suggested segmentation baseline (cosine similarity of patch embeddings to class text) would strengthen the ablation.
- Reporting the number of ablated heads in the Waterbirds experiment and discussing variability across model sizes would improve clarity.

## Removed Points

- **Criticism about TextSpan being "standard greedy orthogonal matching pursuit":** The paper does not claim algorithmic novelty; the contribution is the application domain and text-interpretable framing.
- **Criticism about missing statistical significance / confidence intervals:** Single-run evaluation on fixed benchmarks is the norm in this subfield.
- **Criticism that compared segmentation methods "operate under a different informational advantage" as fatal:** The paper already includes "raw attention" as a CLIP-native baseline in the table, partially addressing this. The criticism is valid as a missing control (now in Minor) but not a fatal flaw.
- **Criticism about unfair comparison favoring the author's method:** The asymmetry (if any) favors baselines, not the proposed method — the paper is evaluating its method against established approaches, not stacking the deck.
- **Criticism about "fatal indirect effects" in mean-ablation:** The paper acknowledges indirect effects in its Limitations section. The finding that MLP mean-ablation barely affects accuracy is robust even with the terminology imprecision.
- **Strength Finder strengths about the problem being "important":** Generic; removed.
- **Strength Finder claiming TextSpan provides "stronger downstream validation than prior neuron-level interpretability work":** Subjective and unverifiable; removed.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on identifying a gap between the Waterbirds causal claims and the evidence provided, but this gap is apparent from reading the paper directly.

## Suggestions
1. For the Waterbirds experiment, automate head selection: define "geolocation heads" using a fixed set of location-related keywords and measure overlap with TextSpan basis directions, then ablate those. Report the exact count of ablated heads.
2. Fix the candidate pool to an independently-sourced caption dataset (e.g., COCO captions) before running TextSpan analysis, eliminating the circularity concern.
3. Add a segmentation baseline computing cosine similarity between class-text embeddings and per-patch embeddings from the final ViT layer (without the proposed decomposition), to isolate the decomposition's contribution.
4. Discuss the large variability in Waterbirds improvement across ViT-B/L/H models.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>