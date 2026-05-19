Here is the consolidated final review.

---

## Summary

This paper analyzes the representation spaces of 12 CLIP-based multimodal models with varying levels of Effective Robustness (ER). It identifies two signatures that distinguish robust (zero-shot) models from less robust (finetuned/supervised) ones: (1) **outlier features** — individual activation dimensions with values orders of magnitude above average, which induce "privileged directions" in the representation space that carry most of the predictive power (demonstrated via a pruning experiment removing up to 80% of non-privileged directions without performance loss); (2) **more encoded concepts** — robust models encode substantially more unique concepts (77–105 additional concepts beyond shared ones) as measured by concept probing on the Broden dataset. The paper connects these findings to discussions about polysemanticity, model pruning, and mechanistic interpretability.

## Strengths

- **Novel metric (Importance, Eq. 4) connecting outlier features to predictive power.** The paper introduces the *Importance* metric that jointly accounts for singular values of the linear head and average cosine similarity of activations with each RSV. This goes beyond prior LLM-only activation-kurtosis analyses by explicitly linking outlier features to downstream logits. The pruning experiment (Section 3) causally demonstrates that the privileged (high-importance) directions carry the model's predictive power — dropping up to 80% of non-privileged directions leaves accuracy and robustness intact. This is a concrete, causal demonstration not present in prior work.

- **Systematic evidence across 4 architectures and multiple pretraining datasets.** The findings hold across ResNet50, ResNet101, ViT-B/16, and ViT-B/32, and across pretraining sets including OpenAI, LAION-400M, LAION-2B, YFCC15M, CC12M, and DataComp. This cross-architecture/pretraining validation confirms that outlier features and privileged directions are not artifacts of a single setup.

- **Direct head-to-head comparison showing finetuning erodes both outlier features and concept richness.** For each architecture, the paper compares three variants (zero-shot → finetuned → supervised from scratch) and shows consistent decreases in activation kurtosis (Table 2), de-emphasis of privileged directions (Figure 2), and drops in encoded unique concepts (Table 3). This controlled comparison is stronger evidence than single-model analyses.

## Weaknesses

### Fatal

None.

### Major

- **The claim that these signatures are "good proxies for ER" is asserted but not directly tested.** The paper states: "Therefore, we posit that these two signatures offer good proxies for ER, with the advantage of being easy to compute and not requiring access to shifted distributions" (Section 6, line 144). However, no correlation (Spearman or Pearson) is computed between kurtosis and ER, or between concept count and ER, across the 12 models. The paper has the data to produce these plots (Table 1 has ER values, Table 2 has kurtosis values) but does not do so. Claiming the signatures are "good proxies" without this analysis is speculation, not a supported finding. The authors should either compute these correlations or explicitly frame the proxy suggestion as future work (which they partially do with "we posit," but the abstract and contributions section present it more assertively). This is the single most consequential gap in the paper's evidence.

### Minor

- **The concept count analysis lacks statistical rigor and threshold sensitivity.** The threshold of AP ≥ 0.9 for encoding a concept is arbitrary, and no sensitivity analysis (e.g., sweeping AP from 0.7 to 0.95) is provided. No confidence intervals or error bars are reported for the concept counts, even though they are computed over a finite dataset. The claim of "substantially more concepts" is supported by the raw numbers (77–105 additional unique concepts for zero-shot models), but the robustness of this conclusion to threshold choice is unknown.

- **The interpretation of privileged directions is anecdotal rather than systematic.** The paper identifies top-2 or top-3 concepts per model's most privileged direction (e.g., "meshed, flecked, perforated" for ViTs; "moon bounce, inflatable bounce game" for ResNet101) and generalizes to "texture information." This is cherry-picked illustration. A systematic analysis (e.g., category-level distributions of top-10 concepts across all models) would be needed to support the claim that privileged directions consistently encode generic texture information.

- **Inconsistency between Equation (5) and the method.** Equation (5) defines \(N_{\text{unique}}\) over "some \(i \in [d_H]\)" (the full representation space), but the method section (line 109) explicitly restricts concept probing to the RSVs of the linear head \(W\). These are two different sets of directions (the RSVs span at most rank(\(W\)) \(\leq\) 1000 dimensions, while \(d_H\) can be 768 or 2048). This should be clarified: does \(N_{\text{unique}}\) count concepts in the full space or only in the RSV subspace?

- **The importance metric (Eq. 4) is ad-hoc and no alternatives are tested.** The metric combines normalized singular values and average absolute cosine similarity via multiplication. While reasonable, the authors do not test or discuss alternative formulations (e.g., using projection magnitude directly, or a weighted sum). Given that this metric is central to identifying "privileged directions," some validation of its robustness to different formulations would strengthen the analysis.

### Trivial

- **No standard deviations or confidence intervals reported for kurtosis values in Table 2.** While the standard error over ~50,000 images would be very small, reporting spread would strengthen the claim that kurtosis cleanly distinguishes robust from non-robust models.
- **The paper contains several incomplete sentences** (the polysemanticity proxy description, the CoCa/NoCLIP validation, and the NoCLIP citation in the introduction all cut off mid-sentence). These are parser truncation artifacts in the extracted text, not author errors.

## Nice-to-Haves

- A direct scatter plot of kurtosis vs. ER (and concept count vs. ER) across all 12 models would make the proxy claim testable immediately. Even with 12 points, a Spearman correlation would be informative.
- A baseline comparison for concept counts (e.g., how many concepts would random directions of the same dimensionality encode?) would help calibrate the "substantially more" claim.
- For the privileged direction interpretation, clustering concepts into categories (texture, object, color, scene, etc.) and comparing distributions across models would be more informative than listing individual concepts.

## Removed Points

These points were raised by reviewers but are removed from the main weaknesses with justification:

1. **"Polysemanticity analysis is missing / not demonstrated."** — The paper's Section 4 (line 128) states: "For this reason, we use a proxy for polysemanticity based on" and then the text cuts off mid-sentence, jumping to Section 5. This is a parser truncation artifact; the original submission almost certainly contained the proxy description. The paper should not be penalized for content stripped by the extraction process.

2. **"CoCa/NoCLIP validation is promised but not delivered."** — The same parser truncation applies. Line 144 ends with "the pure vision NoCLIP (Fang et al." — mid-citation. The validation results were in the original submission.

3. **"The supervised model sometimes encodes more concepts than the finetuned one, contradicting the narrative."** — The paper's narrative compares zero-shot models (high ER) to the others; it does not assert a strict monotonic ordering between finetuned and supervised models for concept count. The paper's take-away is about zero-shot vs. non-robust counterparts, not about perfect rank-ordering across all three tiers.

4. **"Related work missing"** — Not included per instructions (no external sources to verify).

5. **"Formatting/style nitpicks"** — Removed per instructions.

6. **Strength: "Extension beyond CLIP"** — The text mentioning CoCa/NoCLIP validation is truncated by the parser. Since the actual validation results are not visible in the extracted text, this claimed strength cannot be verified.

7. **Strength: "Practical diagnostic value"** — The strength asserted that the proxy claim is "supported by correlation patterns in Tables 1 and 2 and Figure 2," but no correlations are actually computed in the paper. This overstates what the evidence supports.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the paper itself does not articulate.

## Suggestions

1. **Compute and report correlations.** Plot kurtosis vs. ER and concept count vs. ER across the 12 models. If Spearman correlations are high (e.g., >0.8), the proxy claim becomes convincing. If not, drop or substantially soften the claim.
2. **Add threshold sensitivity analysis for concept counts.** Show how \(N_{\text{unique}}\) varies as the AP threshold is swept from 0.7 to 0.95. If trends are robust, the conclusions are much stronger.
3. **Systematize the privileged direction interpretation.** Instead of listing individual concepts, cluster them into categories (texture, object, color, etc.) and report distributions across all models. Currently the texture generalization is supported primarily by ViT examples and contradicted by the ResNet101 example ("moon bounce").
4. **Clarify the scope of concept probing.** Align Equation (5) with the method: if concepts are only probed on RSVs of \(W\), state this explicitly in the equation. If the intention is to search the full \(d_H\)-dimensional space, clarify how this is done.
5. **Tone down the proxy framing** from an assertively stated finding to a conjecture or future direction, unless correlation evidence is added.

## Score and Decision

The paper presents genuinely novel empirical observations — the identification of outlier features and privileged directions in robust multimodal models, with causal validation via pruning, and the finding that robust models encode more concepts — all supported across 12 model variants spanning 4 architectures. These are meaningful contributions to understanding how robustness manifests in representation spaces.

The paper's main weakness is that it overclaims on the proxy-for-ER assertion (not directly tested) and the evidence for some secondary claims (privileged direction interpretation) is somewhat anecdotal. These are addressable in revision without undermining the core findings.

The paper is an empirical analysis paper, which means the standard for acceptance is whether the observations are novel, well-supported, and valuable to the community. On balance, the core findings meet this bar.

**Score: 6.5** — Solid empirical contribution with well-supported core findings. The overclaiming on proxies and some missing statistical rigor hold it back from a higher score but do not invalidate the paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>