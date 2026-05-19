- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review, carefully cross-checking each claim against the actual paper text.

## Summary

This paper proposes that neural network solution sets reachable via SGD form a *star domain* (modulo permutation symmetries) rather than a convex set — a relaxation of the convexity conjecture. It introduces the Starlight algorithm to find a candidate "star model" that is linearly mode-connected to multiple source solutions, and provides empirical evidence across several architectures (ResNet-18, VGG, DenseNet) and datasets (CIFAR-10/100, ImageNet-1k). The paper also explores practical benefits of star models for Bayesian model averaging and model fusion.

## Strengths

1. **Novel relaxation of the convexity conjecture.** The star domain conjecture (Conjecture 2) is a principled weakening of full convexity that better matches documented empirical failure cases of the convexity conjecture (Section 3.1). The paper directly demonstrates that convexity fails for standard-width networks (blue regular–regular curves in Figure 3 show high barriers) while star-shaped connectivity holds to a meaningful degree (red star–regular curves). This is a genuine conceptual contribution to understanding solution-set geometry.

2. **Systematic empirical evaluation across architectures and datasets.** Table 1 reports star–regular vs. regular–regular loss barriers for five architectures (ResNet-18, VGG11, VGG19, DenseNet) on CIFAR-10, CIFAR-100, and ImageNet-1k. Star–regular barriers are consistently and substantially lower — e.g., CIFAR-10 ResNet-18 (SGD): 0.078 vs. 0.383, a ~4.9× reduction. This breadth of evidence supports the existence of models with markedly improved linear connectivity.

3. **Principled algorithm design.** The Starlight algorithm (Algorithm 1) incorporates periodic weight matching to handle permutation invariances (Step 1) and a Monte-Carlo sampling scheme (Steps 2–5) to avoid the intractable integral in Equation 3. The design is specifically tailored to the star-domain setup and goes beyond trivial adaptation of prior curve-fitting methods.

4. **Analysis of how starness scales with architecture.** Figure 4 shows that star–regular barriers are consistently about one-third of regular–regular barriers across WideResNet widths (1× to 8×) and depths (22 to 40 layers). This demonstrates the phenomenon is robust and not a narrow-network artifact.

## Weaknesses

### Fatal
None.

### Major

1. **Mismatch between the conjecture's formal statement and the empirical evidence.** Conjecture 2 requires that the star model be linearly mode-connected to other solutions, i.e., $\text{barrier}(\tilde{\theta}, \theta^\star) \approx 0$. However, every reported star–regular barrier is clearly positive and often far from zero: 0.078 (CIFAR-10 ResNet-18), 0.336 (VGG19), 0.756 (CIFAR-100 ResNet-18), and 3.735 (CIFAR-100 DenseNet). The paper's own Caveats paragraph (lines 391–394) states that "loss barriers between the star model and other solutions often yield values that are significantly greater than zero." The evidence strongly supports the claim that star models have *substantially lower* barriers than typical pairs (e.g., 4.9× lower), but it does not support the stated condition of "≈ 0." This is a significant overclaim. The framing should be adjusted to match what the data actually show — e.g., "substantially reduced barriers" — or the evidence must be strengthened to approach near-zero values.

### Minor

2. **Limited held-out evaluation sample.** Connectivity to arbitrary solutions is tested against only 5 held-out models in most experiments (explicitly stated in lines 315, 363, 376, 389). While any finite sample is necessarily incomplete, 5 models provides a narrow basis for claiming connection to the entire solution set. This is especially relevant given the conjecture is a universal statement ("for any other solution $\theta \in S$").

3. **Missing baseline: simple averaging of aligned source models.** The paper compares star–regular barriers against regular–regular barriers, but does not compare against the simplest alternative for obtaining a centrally located model: weight-averaging the (permutation-aligned) source models. Without this baseline, it is unclear whether the Starlight algorithm's low barriers are a unique property of the star model, or whether any model near the centroid of the source set would exhibit similar connectivity. The paper would be strengthened by showing that Starlight significantly outperforms such a baseline.

4. **Star model's training loss is sometimes far from zero.** The solution set is defined as $S := \{\theta \mid \mathcal{L}(\theta) \approx 0\}$ (line 84). However, in several cases the star model's loss is notably higher than regular models: e.g., CIFAR-10 VGG19 (0.059 vs. 0.001), CIFAR-10 DenseNet (0.157 vs. 0.001), and CIFAR-100 DenseNet (0.635 vs. 0.006) (Table 1). These values are not "approximately zero" in any standard sense, raising the question of whether the star model is truly in the solution set or is a compromise point with moderately higher loss. The paper acknowledges this implicitly in the Caveats section but does not discuss it explicitly.

### Trivial
None.

## Nice-to-Haves

- **Comparison with concurrently obtained star models (Lin et al., 2024).** The paper already cites this work (line 66). A direct comparison of barrier values or accuracy would help contextualize the results.
- **Computational complexity analysis.** The Starlight algorithm requires periodic permutation matching (every $m$ steps) and Monte-Carlo sampling. A brief complexity discussion (e.g., overhead relative to standard training) would help readers assess practicality.
- **Larger held-out sets in selected settings.** Running one experiment with, say, 50+ held-out models would provide stronger evidence that connectivity generalizes beyond the small test set.

## Removed Points

These points were flagged by reviewers but are removed from the main weaknesses per the filtering rules:

- **"Practical applications are orthogonal to the conjecture."** Removed — The paper never claims the practical applications (Section 5) support the conjecture. They are presented as separate benefits of star models. This criticism misreads the paper's structure.
- **Questions about model/dataset existence or release status.** Removed per hard rules — all cited models, datasets, and benchmarks are assumed to exist.
- **Formatting and presentation nitpicks.** Removed per hard rules.
- **"Missing related works" (any formulation).** Removed per hard rules — I cannot confirm what works exist in the literature beyond the paper's citations.
- **"Missing appendix / proofs / supplementary."** Removed per hard rules — the parser strips these sections.
- **Generic criticisms without specific evidence anchors (e.g., "the evaluation lacks rigor" without pointing to a specific table/figure/claim).** Removed.

### Criticisms about specific claims that are already addressed by the paper

- **"The paper claims 'strong evidence' but the barriers are non-zero."** The paper *does* acknowledge this explicitly in the Caveats (lines 391–394): "loss barriers between the star model and other solutions often yield values that are significantly greater than zero." While I retain the mismatch between the conjecture's strict condition and the evidence as a **Major** weakness (point 1 above), the accusation that the paper is *unaware* of or *hides* this fact is incorrect.

## Novel Insights

The merger of the two reviews surfaces a tension that neither review fully articulates: the paper makes two distinct claims — (a) the star domain *conjecture* (a universal geometric claim about the solution set requiring ≈0 barriers), and (b) the *existence* of Starlight-found models with substantially lower barriers. The evidence strongly supports (b) but not (a). The interesting observation is that if the conjecture were reframed as "the solution set is approximately a star domain where the star point enjoys barriers that are a fraction (e.g., 1/3 to 1/5) of typical pair barriers," the paper's evidence would be cleanly supportive. This suggests the paper's conceptual contribution is more robust than its formal framing would suggest. The community would benefit from a clearer delineation of what quantitative condition constitutes "star-shaped connectivity" in practice.

## Suggestions

1. **Reframe the conjecture** to match the evidence. Replace "$\barrier \approx 0$" with a precise quantitative condition such as "$\barrier \leq \epsilon$ for a task-dependent small $\epsilon$" or "barriers are substantially lower than typical regular–regular barriers, with a reduction factor measurable empirically." The evidence then directly supports the claim.
2. **Add a weight-averaging baseline.** After permutation alignment, compute the simple average of source models and report its barriers against held-out models. If Starlight significantly outperforms this baseline, the algorithm's value is much clearer.
3. **Explicitly discuss** the star model's higher training loss in cases where it deviates from ≈0 (e.g., DenseNet on CIFAR-100). Acknowledge whether this means the star model lies outside the strict solution set and discuss the implications.
4. **Expand the held-out evaluation** in at least one key setting (e.g., CIFAR-10 ResNet-18) to 50+ held-out models to demonstrate that the low barriers are not an artifact of a small test set.
