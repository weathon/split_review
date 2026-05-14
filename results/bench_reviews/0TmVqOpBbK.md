Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper introduces a conditional scaling law that extends the Chinchilla framework to incorporate architectural factors—hidden size, mlp-to-attention ratio, and grouped-query attention (GQA)—enabling architecture-aware loss prediction. The authors train over 200 models (80M–3B parameters) to fit their scaling law and propose a search framework that identifies architectures jointly optimizing inference throughput and accuracy. The resulting Surefire models achieve up to 42% higher inference throughput than comparably-sized LLaMA-3.2 models while maintaining or improving downstream accuracy.

## Strengths

- **Novel conditional scaling law for architecture-aware loss prediction.** The two-step calibration approach (multiplicative/additive on top of Chinchilla) provides a practical way to incorporate hidden size and mlp-to-attention ratio into scaling laws. The scaling law achieves strong predictive performance on held-out architectures (Spearman 0.75–0.89 across three progressively harder tasks, Figure 6), and the separable formulation is validated against more complex non-separable alternatives (Appendix J).

- **Extensive and systematic empirical characterization.** Training 200+ models across scales (80M–3B) with controlled architectural variations produces convincing U-shaped loss curves for both hidden size and mlp-to-attention ratio (Figures 4–5). These provide genuinely new quantitative insights into optimal parameter allocation, beyond prior work that only examined aspect ratio (d_model / n_layers).

- **Robust and transferable inference-throughput gains.** The throughput improvements (up to 42% on A100/vLLM, up to 47% on H200/SGLang) are validated across multiple serving frameworks and GPU types (Appendix G). The throughput analysis convincingly isolates the effects of hidden size, mlp-to-attention ratio, and GQA (Figure 3, Appendix F). These gains are the most solid part of the contribution.

- **Practical search framework.** Algorithm 1 provides a lightweight, implementable recipe: fit the conditional scaling law on small models, solve the constrained optimization for d_model and r, then enumerate GQA values. The framework is well-motivated by the empirical finding that GQA affects throughput but not loss in a consistently modelable way (Appendix I).

## Weaknesses

### Major

- **Uncontrolled LLaMA-3.2 comparison and overclaiming in the abstract.** The abstract states "Under the same training budget, optimized architectures achieve up to 2.1% higher accuracy... compared to LLaMA-3.2." However, the LLaMA-3.2-1B and -3B results in Table 1 appear to come from publicly available checkpoints trained on a different data mixture and for a different (likely much larger) number of tokens. The Panda/Surefire models were trained on 100B tokens of Dolma-v1.7. Training data distribution and token count are confounded with architecture, so the accuracy delta cannot be cleanly attributed to architectural choices. The paper's internal validation (Figure 7 left, showing Panda-1B achieves lowest loss among all 1B variants trained under the same setup) is the more rigorous comparison, and the paper should foreground that instead. The abstract and conclusion need to be revised to accurately reflect what the comparison shows and does not show. This does not invalidate the scaling law methodology itself, but it weakens the headline accuracy claim.

### Minor

- **Scaling-law extrapolation is limited, not demonstrated across wide scale gaps.** Figure 8 shows that fitting on models from 80M–1B and predicting 3B yields only Spearman 0.50. The paper honestly acknowledges this and recommends fitting on models ~1/3 the target scale (1B→3B), which yields perfect correlation on the tested 3B architectures. However, the number of 3B test architectures is not reported; if only a handful were evaluated, the perfect Spearman of 1.0 is less informative. The practical takeaway—that coefficients shift with scale and close-range fitting is preferable—is useful, but the paper should state the number of test points and temper claims about extrapolation.

- **Small absolute accuracy margins without statistical characterization.** The downstream accuracy advantage of Surefire-3B over LLaMA-3.2-3B is 0.6–0.7 percentage points averaged across nine tasks (62.5% vs. 61.9%, Table 1). No confidence intervals, standard deviations, or training seeds are reported. While single-run reporting is common in scaling-law papers, given the small margin, some characterization of variance (even via bootstrap over tasks) would strengthen the claim.

- **L_opt fitting procedure is underspecified.** The paper states it "empirically searched over architecture variants to find the optimal loss L_opt(N,D)" for fitting the conditional law. How many architectures were searched, and how was the optimum determined? Using the minimum observed loss as the reference could inject noise, particularly at smaller scales where fewer variants were trained.

### Trivial

- The abstract should clarify whether LLaMA-3.2 loss values in Table 1 are obtained by evaluating public checkpoints on the authors' validation data or are the original reported training losses.

## Nice-to-Haves

- Training a LLaMA-3.2-architecture model from scratch under the same 100B-token Dolma-v1.7 budget would cleanly isolate the architectural effect and strengthen the accuracy claim considerably. This would address the major weakness above.
- Characterizing how the conditional-law coefficients shift with scale (e.g., by fitting at 500M, 700M, 1B, 2B) could provide insight into whether a meta-scaling law for the coefficients is feasible, which would broaden the extrapolation range.
- Reporting per-task downstream accuracy with variance estimates (at minimum, standard deviation across the nine tasks) would help readers assess the reliability of the small accuracy margins.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Invalid baseline comparison invalidates the headline contribution on accuracy" (Harsh Critic, Critical Issue 1, claimed as Fatal).** The core contribution is the conditional scaling law and search framework, both of which are validated through internal held-out evaluation (Figure 6, Figure 7 left). The LLaMA-3.2 comparison is a secondary anchoring point, not the primary validation. The overclaiming in the abstract is a presentation issue, not a methodological one. The paper would stand without this comparison. Retained as Major (presentation overclaim) but not Fatal.

- **"Scaling-law extrapolation breaks at 3B scale" (Harsh Critic, Critical Issue 2).** The paper is honest about this limitation and proposes a practical solution. This is not a hidden flaw—it is an explicit finding. Retained as Minor.

- **"Accuracy improvements are tiny and lack statistical support" (Harsh Critic, Critical Issue 3).** Valid concern but single-run reporting with nine diverse tasks is standard practice in the scaling-law literature (cf. Chinchilla, Kaplan et al.). Retained as Minor.

- **"The conditional scaling law assumes separability of d_model and r effects" (Harsh Critic, Section-by-Section Notes).** The paper explicitly acknowledges this assumption and ablates non-separable formulations in Appendix J, finding they do not improve predictive performance. The assumption is validated, not hidden. Removed as a weakness.

- **"The 'fitting strategy' for finding L_opt is underspecified" (Harsh Critic).** Retained as Minor—this is a real documentation gap but does not threaten the core claims.

- **Strength Finder generic strengths removed:** The strength finder's "well-written" equivalent was not present, so none needed removal on that basis. All strength finder points kept are substantive and evidence-backed.

## Novel Insights

The paper's finding that hidden size and mlp-to-attention ratio exhibit consistent U-shaped loss curves with nearly identical optimal d_model/√N across model scales (80M–297M) is a genuinely novel empirical observation that goes beyond prior architecture-scaling work. Additionally, the discovery that larger hidden sizes and higher mlp-to-attention ratios improve inference throughput (via reduced FLOPs and smaller KV caches) while simultaneously having non-monotonic effects on loss creates a non-trivial Pareto frontier—the paper is the first to characterize and operationalize this trade-off systematically.

## Suggestions

- Revise the abstract to remove the implication that LLaMA-3.2 was trained under the same budget. Instead, foreground the internal validation (Figure 7 left) and frame the LLaMA-3.2 comparison as an external reference point with explicit caveats about differing training regimes.
- Report the number of 3B test architectures used for the Spearman 1.0 result in Figure 8 (right), and consider adding a few more 3B variants if the current set is small.
- Clarify in Table 1 how LLaMA-3.2 loss values were obtained (public checkpoint evaluated on Dolma-v1.7 validation data, or original reported training loss).

## Score and Decision

**Anchor comparison:**

| Path | Avg Score | Decision | Comparison to current paper |
|------|-----------|----------|-----------------------------|
| 2FZC0c06jP | 6.50 | Accept (Poster) | Stronger theoretical grounding and a clearer, more impactful finding with direct practical implications. Current paper is below this. |
| YnJ2s4WeNF | 6.00 | Accept (Poster) | Similar empirical scale, somewhat cleaner contribution. Current paper has more novelty but worse presentation issues. Below this. |
| utSqpxQHXq | 6.00 | Accept (Poster) | Theory paper with different contribution type. Not directly comparable. |
| T985gm4sDA | 5.50 | Accept (Poster) | First-of-its-kind scaling law for a new domain, well-executed but incremental. Current paper has comparable novelty with more substantial empirical scale. Similar tier. |
| 57D4Uaiiyi | 5.50 | Reject | Theory paper; different contribution type. |
| 7r2lkhDGUj | 5.33 | Accept (Poster) | Strong empirical contribution (300+ models, up to 28B) with definitional clarity issues. Current paper's empirical scale is slightly smaller (200+ models, up to 3B) but its methodological contribution (conditional scaling law) is comparably novel. Similar tier. |
| 0Iw52EDu82 | 4.50 | Reject | Scaling laws for sparse models; narrower contribution. Current paper is stronger. |
| iQG6CObQ7E | 4.00 | Reject | Theory paper with significant theory-experiment gaps. Current paper is well above this. |
| pJcHaD3mvn | 4.00 | Reject | Extrapolation from small models with different focus. Current paper is stronger. |
| dnuIoVjeGR | 3.00 | Reject | Overly expressive, insufficiently justified scaling law. Current paper's simpler, better-validated approach is clearly stronger. |
| jZcWBV3Pis | 3.00 | Reject | Re-analysis paper with limited significance. Current paper is well above this. |

**Scoring rationale:** The conditional scaling law is a novel methodological contribution, the 200+ model training sweep provides substantial empirical grounding, and the inference-throughput gains are robust and transferable. These strengths place the paper solidly above the low-band anchors (which suffered from fundamental gaps or limited significance) and in the neighborhood of the medium-band anchors like 7r2lkhDGUj (5.33) and T985gm4sDA (5.50).

The major weakness—overclaiming in the abstract about the LLaMA-3.2 comparison—is a presentation issue, not a methodological flaw. The core contribution (scaling law + search framework) is validated through internal held-out evaluation. However, the weakness does reduce confidence in the headline accuracy claims and drags the score below the high-band anchors (6.0+), which had cleaner presentations of their core findings. The minor weaknesses (limited extrapolation range, small accuracy margins without variance) are addressable and typical for papers in this space.

**Score:** 5.0. The paper makes a genuine contribution with a practical framework that the community can build on, but the presentation overclaim and limited extrapolation evidence prevent a higher score. The strengths outweigh the weaknesses.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>