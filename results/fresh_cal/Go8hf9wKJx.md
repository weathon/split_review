Now I'll synthesize the final review.

## Summary

This paper proposes DOG, a framework that uses a pre-trained text-to-image diffusion model (Stable Diffusion v1.5) to synthesize near-OOD surrogate images from only in-distribution (ID) data, then fine-tunes an OOD detector via outlier exposure. The key innovation is a two-step anchor selection: first, textual inversion captures visual semantics per class into pseudo-words; second, candidate words are selected in text space and filtered by visual similarity to find anchors whose generated images lie near the ID boundary. Table 1 reports strong performance gains over existing methods on CIFAR-10, CIFAR-100, and ImageNet.

---

## Strengths

- **Multi-modal outlier generation outperforms single-modality baselines.** The ablation in Table 2 shows that DOG (combining visual semantics through textual inversion with textual category information) outperforms all five single-modality alternatives (e.g., using only text synonyms, only visual interpolation, only noise perturbation) on both CIFAR benchmarks. This directly supports the paper's core claim that fusing both modalities improves detection.

- **State-of-the-art results without external OOD data.** On CIFAR-10, CIFAR-100, and ImageNet, DOG achieves the best FPR95 and AUROC among all compared methods (Table 1), including strong outlier-exposure baselines (OE, POEM) and generation-based methods (VOS, NPOS). For CIFAR-100, it reduces FPR95 by 20.27 points over standard OE.

- **Converts outlier generation to interpretable text space, enabling explicit anchoring.** DOG transforms the problem from sampling low-likelihood latent features (VOS/NPOS) to finding candidate words in text space via cosine similarity (Eq. 5) and filtering by visual proximity to ID data (Eq. 6). This text-space approach is a clear departure from prior work and is supported by better performance than VOS and NPOS in Table 1.

- **Empirical guidance on the number of synthesis outliers.** Figure 3(a,b) systematically varies the number of generated outliers M and shows performance saturating when M roughly matches the number of ID samples per class — a useful, principled rule for practitioners.

---

## Weaknesses

### Major

- **Unsubstantiated claim of "dynamic adjustment" of surrogate outliers.** The abstract states that DOG "allows dynamic adjustment of surrogate outlier data based on the results," and the conclusion repeats that DOG "enables dynamically adjusting the surrogate outlier data based on the OOD detection results." However, the method description (Algorithm 1, lines 1–16) contains no such mechanism: surrogate outliers are generated once from a fixed set of anchor words, followed by a single fine-tuning phase. There is no iterative refinement, no feedback loop from the detector to the generator, and no experiment demonstrating adjustment based on results. This claim directly contradicts what is implemented and overstates the demonstrated contribution. The authors should either remove this claim from abstract and conclusion or, minimally, clarify precisely what is meant by "dynamic adjustment" and provide evidence for it.

- **Ambiguous evaluation protocol regarding the scoring function.** Line 193 states: "And we adopt the ASH scoring (Djurisic et al., 2023) in OOD detection." It is not made explicit whether ASH is used as the scoring function for *all* methods in Table 1 or only for DOG. ASH is also listed as a separate post-hoc baseline in the same table, creating confusion. If only DOG uses ASH while baselines use their default scoring (e.g., MSP for OE, energy for Energy-OE), the comparison is invalid because ASH is known to boost OOD detection performance across many models. If all methods use ASH, the paper should state this explicitly and acknowledge that the baseline methods were not originally tuned for ASH scoring. This ambiguity threatens the validity of the headline results in Table 1.

### Minor

- **Key filtering step (Eq. 6) is under-specified and not reproducible as written.** The formula is:
  ```
  C_λ = {c ∈ C : min_{(x,y) ∈ D^{Train}_ID} percentile_η[ sim( T(prompt(c)), E'(x) ) ] ≤ λ}
  ```
  It is unclear what `percentile_η` is computed over. If `E'(x)` is a single image embedding per sample, then `sim(...)` returns a single scalar, and taking a percentile of a single value is ill-defined. The text explains that the percentile is used "to alleviate noises interference" but does not clarify the actual computation (e.g., whether it runs over patch-level features, over multiple crops, or over the set of all training samples). The choice of λ and η is also not ablated. Given that this step determines which text anchors are ultimately used for generation, the lack of clarity is a reproducibility concern.

- **Ablation does not isolate the effect of textual inversion vs. using raw class names.** The ablation in Table 2 compares DOG against strategy (e) which uses "synonyms based on the current classes." This tests a different baseline (synonyms rather than the class name itself) and does not directly compare using (i) the raw class name as anchor, (ii) the learned pseudo-word `s_y` from textual inversion, and (iii) both. Without this comparison, it is unclear whether the complexity of textual inversion (Eq. 4) is justified, or whether simply using the class name directly in the same multi-modal pipeline would achieve comparable results.

### Trivial

- None beyond standard formatting artifacts introduced by the PDF extraction process (which are not the authors' fault).

---

## Nice-to-Haves

- **Computational cost discussion.** The paper does not report the cost of textual inversion or diffusion-based image generation (e.g., total GPU hours, number of Stable Diffusion calls). A brief discussion would help practitioners assess the practical trade-offs.
- **Error bars / confidence intervals for Table 1 results.** The reported gains are large enough that statistical variance from a single run is a concern. Reporting results over multiple seeds would strengthen confidence.
- **Ablation of parameters `λ` and `η`** from the filtering step (Eq. 6) would improve understanding of the method's sensitivity.

---

## Removed Points

*These points were flagged by one or both input reviews but are removed here with brief justification:*

- **"Number of generated outliers M not well-justified"** — The paper already provides an ablation on M in Figure 3(a,b) with a clear saturation pattern and a principled rule (match M to samples per class). This criticism is not valid as stated.
- **"t-SNE visualization not quantitative"** — The t-SNE in Figure 3(c) is acknowledged as qualitative evidence; the paper does not overclaim on it. This is a generic criticism that does not undermine any specific claim.
- **"No comparison against methods using different scoring functions"** — This is subsumed by the ASH-scoring-ambiguity weakness above; the real issue is the lack of clarity about *which* scoring function was used for *which* method.
- **"Missing related work"** — Not verifiable without external sources; per instructions, excluded.
- **"Typos / formatting"** — These are parser artifacts, not author errors.
- **The Strength Finder's generic phrasing about "this paper addressed an important problem"** — All retained strengths are concrete and evidence-grounded; no generic strengths were kept.

---

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is that the paper's evaluation might conflate two separate axes of improvement: (1) the quality of generated near-OOD outliers (the genuine methodological contribution) and (2) the choice of scoring function for evaluation (ASH). If ASH is uniformly applied, the actual contribution of the generation pipeline vs. the scoring function is not disentangled. This is a challenge the paper needs to address but does not appear to recognize.

---

## Suggestions

1. **Remove or substantiate the "dynamic adjustment" claim.** If no feedback loop exists, delete the claim from abstract and conclusion.
2. **Clarify the scoring protocol unambiguously.** State for each method in Table 1 which scoring function was used. If ASH was used for all methods, state this explicitly, add a note about tuning, and explain why ASH as a separate baseline is still meaningful.
3. **Reformulate Eq. 6** to make the percentile computation unambiguous (e.g., over which set of values is the percentile taken), and consider adding an ablation for λ and η.
4. **Add an ablation** that compares using the raw class name vs. the learned pseudo-word `s_y` (from textual inversion) as the anchor in the full pipeline, to justify the textual inversion step.
5. Add error bars or multiple-seed results for the main experiments.

---

## Score and Decision

**Originality:** The idea of using text-to-image diffusion to generate near-OOD outliers anchored in text space is novel and a clear departure from prior feature-space sampling methods (VOS, NPOS). However, the textual inversion component is adopted from prior work (Gal et al., 2022).

**Importance of research question:** OOD detection is a practically important problem, and the challenge of obtaining suitable surrogate outliers is well-recognized.

**Claims supported:** The main claim (that DOG generates useful near-OOD outliers and improves detection) has experimental support, but is weakened by the ASH scoring ambiguity and the unsubstantiated dynamic-adjustment claim.

**Soundness of experiments:** The experimental scope (three ID datasets, multiple OOD test sets) is appropriate, but the ambiguity about scoring functions is a significant concern that needs resolution.

**Clarity of writing:** The method is generally clearly described except for Eq. 6 which is underspecified.

**Value to community:** If the evaluation concerns are resolved, the framework could offer a practical approach for generating surrogate outliers using only ID data, which would be valuable.

The paper has a genuine contribution (text-space anchored outlier generation via diffusion) but has two major issues: (1) an unsubstantiated claim about dynamic adjustment that should be removed, and (2) an ambiguously specified evaluation protocol that could affect the validity of the headline results. The latter is the more serious concern — the paper must clarify the scoring protocol to make its contribution credible. With these resolved, this could be a strong paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>