## Summary

This paper proposes "support spectrums" for model explainability: given a test point classified into class *c*, the method finds training points in class *c* that geometrically "lie between" the test point and other classes in feature space (the support set), and ranks them along a global-to-local axis by decoupling representer points (or influence functions) into separate measures of prototypicality (global) and feature similarity (local). The spectrum is constructed by sweeping a locality parameter δ and, for each δ, selecting the maximally globally important point in the support set whose similarity to the test point exceeds δ.

## Strengths

1. **Clean geometric decoupling of representer points into interpretable components.** The derivation (Section 3.2, lines 148–172) shows that representer point contributions decompose into g(z_i) = -(Ŵ_c·f_i + b_c) (how prototypical the training point is for class c) and ℓ(z_i, z_t) = f_i^T f_t (feature similarity). The simplification to ordering-equivalent forms avoids computing full representer values and gives each component a clear geometric meaning — this is a non-trivial advance over treating influence/representer scores as monolithic.

2. **Principled definition of support sets using classifier discriminants.** The support set is defined by w_k·(f_t − f) > 0 (lines 62–72), which captures training points that "stand between" the test point and other classes in feature space. This is geometrically grounded and distinct from proximity-based heuristics in prior work.

3. **The California spurious correlation case study is genuinely compelling.** The paper shows (lines 388–418) that for GPT2-XL, the token "California" after "researchers from the University of" is consistently assigned ~0.54–0.59 probability regardless of the broader topical context, and the spectrum retrieves training sequences that are topically irrelevant to the generated text. A controlled experiment across four different contexts confirms the systematic bias. This demonstrates a concrete debugging capability.

4. **The method scales to large language models.** The approach is applied to GPT2-XL (1.6B) and Open-LLaMA-7B by treating autoregressive token prediction as sequential classification over vocabularies of ~50K / ~32K classes, using TF-IDF to select tokens for explanation (line 308). This shows feasibility beyond small classification datasets.

## Weaknesses

### Major

1. **The experimental evaluation is almost entirely qualitative and anecdotal, and does not support the paper's central claims with the rigor expected of a top-venue submission.**

   - **MNIST (Figure 3):** Only two test points (both predicted "5") are shown. The analysis is purely descriptive ("this fact is reflected by the spectrums," "notice also that…"). No quantitative metric is computed — not even the model's test accuracy, the size of the support sets, or a comparison of spectrum properties across a random sample of test points.
   - **Text generation:** A handful of hand-picked tokens are examined. The authors interpret each spectrum post-hoc to decide whether a token is "well supported" or "not well supported." There is no systematic protocol, no inter-rater reliability, no controlled test.
   - **No baseline comparisons on real tasks.** The synthetic 2D example (Figure 2) visually compares spectrums against representer points and influence functions, but no quantitative measure of "skew" or "staticness" is computed there either. Critically, the MNIST experiment and the text-generation experiments do **not** run representer points or influence functions as baselines on the same data, so there is no basis for the claimed improvement over these methods.
   - **No ablation** of the method's components (e.g., what happens if only the support set is used without the global-to-local ranking? What happens if only the local component is used?).
   
   For a new-method paper that asserts advantages over established techniques, the complete absence of any quantitative evaluation, any systematic comparison, and any measure of faithfulness or utility is a decisive weakness.

### Minor

2. **The spectrum construction algorithm is underspecified.** The paper defines the spectrum as {z_δ | −∞<δ<∞} where z_δ = argmax g(z) subject to z∈R(z_t;k) and ℓ(z,z_t) > δ (lines 77–84). However: (a) no discretization strategy for δ is given; (b) the optimization does not have a unique maximizer for a given δ when multiple points satisfy the constraints — how ties are broken is not stated; (c) in Figure 3, each row shows a grid of images — it is unclear whether these are the full spectrum or a sampled/truncated subset, and how many points each row contains is not specified. Without an explicit procedure the method is not reproducible as described.

3. **Edge case not discussed.** The support set condition w_k·(f_t − f) > 0 (line 64) means that if the test point is the most extreme training point of class c along direction w_k, the support set is empty. The paper does not discuss how this case is handled or what a spectrum means for such a test point.

4. **The claim that support set size indicates distinguishability is not validated.** The paper states "when the support set is large it tells us that it is easier for the model to distinguish z_t from the other classes" (line 73). This is a testable claim — e.g., by correlating support set size with prediction confidence or accuracy on held-out data — but no such validation is performed.

5. **The "global importance" g(z) derived from representer points measures prototypicality, not influence in the parameter-change sense.** g(z_i) = −(Ŵ_c·f_i + b_c) is the negative logit for class c, which assigns high value to points deep in the class region — i.e., the most prototypical points, not necessarily the most *influential* on model parameters. This is not a bug (the paper is transparent about the derivation), but the framing as "global importance" conflates two distinct concepts. The method should more accurately be described as ranking from prototypical to test-point-similar, rather than from globally influential to locally influential.

6. **No computational cost characterization.** The method searches over up to ~7M documents / ~24B tokens for each token-level explanation. The paper notes that "the sheer number of classes" makes relative spectrums impractical (line 308), but provides no runtime, scaling, or cost analysis for the absolute spectrums either.

## Nice-to-Haves

- A controlled experiment on MNIST where the spectrum's ability to retrieve style-specific training points is measured (e.g., by constructing a test set with known style variations and checking whether the spectrum correctly selects training points of matching style).
- A dropout-based or retraining-based faithfulness test: do the locally most important training points, when removed from training, actually change the prediction on the test point?

## Removed Points

These points were flagged by reviewers but removed during consolidation — treat with caution.

- **"The claim that existing methods 'often produce global attributions' is overstated"** — Removed. The paper's characterization of the limitation is a reasonable framing, not a factual error.
- **"Influence functions subsection feels tangential"** — Removed. The paper explicitly frames this as future work (line 190: "comparison … will be our main priority in future works").
- **"No discussion of broader explainability evaluation literature"** — Removed per the rule on not citing missing related works.
- **"No training details for MNIST"** — Removed per the rule on nitpicks about hyperparameters. The specific architecture choice is a minor detail in a qualitative demonstration.
- **"The synthetic comparison is purely visual"** — Subsumed under Weakness #1 (the overall evaluation gap), not kept as a standalone point.
- Several strengths from the Strength Finder that were generic or overclaimed (e.g., describing the evaluation as a strength despite it being qualitative) — removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. The most impactful change would be to add a quantitative evaluation on MNIST or a similar controlled dataset: compute the spectrum for many test points, measure properties (length, entropy, overlap across test points), and compare against representer points / influence functions on a simple faithfulness metric (e.g., does removing the top-k spectrum points change the prediction more than removing the top-k points from baselines?).

2. Provide a clear algorithmic description of how the spectrum is computed in practice: discretization of δ, tie-breaking, how many points are in a typical spectrum, and selection of which points to display in figures.

3. Validate the "support set size ↔ distinguishability" claim by computing the correlation with prediction confidence or accuracy on a held-out set.

4. Report computational cost (number of forward passes, wall-clock time) for the language model experiments.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>