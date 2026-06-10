## Summary

This paper identifies two limitations of the interventional fairness notion K-Fair (threshold sensitivity and first-moment insufficiency), proposes a new metric called **ICRD** that compares full CDFs of post-intervention predictions rather than evaluating at a single threshold, and presents **ICCFL**, a learning framework that regularizes a model to minimize ICRD via a differentiable approximation using temperature-scaled sigmoids. The core diagnostic claim — that K-Fair=0 is insufficient for causal fairness because it only captures the first moment — is well-motivated and theoretically supported.

## Strengths

1. **ICRD satisfies the sufficiency condition that K-Fair lacks**: Theorem 1 (Property 1, line 162) establishes that ICRD=0 *if and only if* predictions are causally independent of the sensitive attribute given context. This is a provable improvement over K-Fair, which the paper correctly identifies as only a necessary condition (Limitation 2, Section 4.1).

2. **ICRD generalizes K-Fair as a special case**: The discussion in Section 4.2 (line 170) explicitly shows that K-Fair evaluated at a threshold α is equivalent to ICRD evaluated at a single point, establishing a clean theoretical relationship and explaining why ICRD subsumes K-Fair's capabilities.

3. **Empirical demonstration that K-Fair=0 does not imply causal fairness**: Table 3 shows ICCFL-KF (which minimizes K-Fair) achieves low K-Fair values (e.g., 0.033 on Adult) but has large MMD values (0.291), while ICCFL simultaneously achieves low K-Fair and low MMD. Figure 2 visualizes this: ICCFL-KF's predicted densities differ visibly across groups despite low K-Fair, whereas ICCFL aligns them. This directly validates the paper's central insufficiency claim.

4. **Consistency between ICRD and an independent distributional metric (MMD)**: Figure 3 shows that as λ varies, ICRD and MMD exhibit similar monotonic trends — decreasing ICRD corresponds to decreasing MMD. This empirical link strengthens the claim that minimizing ICRD genuinely reduces distributional unfairness between sensitive groups, not just the specific metric itself.

## Weaknesses

### Fatal
None.

### Major

1. **The method's dependence on a known causal graph is never discussed as a limitation, let alone tested for robustness.** The entire pipeline — generating interventional samples via Causal VAE, computing post-intervention CDFs, and training ICCFL — assumes access to a correct causal graph. The paper treats graphs from prior work as "ground truth" (line 227: *"We consider the causal graph introduced by Wu et al. (2019) as the ground truth"*) without acknowledging that in real-world settings causal graphs are almost never known with certainty. No sensitivity analysis (e.g., varying edges, testing with misspecified graphs) is provided. Since the method's practical viability hinges on this assumption, and the paper advertises the method as deployable, this is a significant gap that limits the paper's contribution.

### Minor

1. **The choice of context variable C is stated for each dataset but no principled criterion is given** for why, e.g., "education" is chosen as context for Adult versus "country birth" for Dutch versus "entrance exam scores" for Law School (lines 221-227). The paper does not discuss how to select C or what happens with a misspecified choice (e.g., a collider or mediator). Since the entire ICRD definition conditions on C, this choice matters and should be principled.

2. **The primary evaluation metric (ICRD) is what ICCFL is trained to minimize** (Eq. 11, line 177: ℓ(ŷ,y) + λ|ICRD(ŷ)|). While Property 1 justifies ICRD itself as the target fairness notion (so this is not circular in a strict sense), the experiments would be stronger if they also showed fairness improvements on independently measured real-world outcomes (e.g., loan denial rates by group) rather than exclusively on synthetic interventional samples. The MMD analysis in Section 5.3 partially addresses this concern by using an independent distributional metric, but MMD is also computed on the same interventional samples.

3. **The claim that ICCFL achieves "higher (or similar) accuracy" while also being fairer** (Section 5.2(i), line 245) is stated without discussion of why this simultaneous improvement is possible. Given that the λ-sweep in Figure 3 shows the expected accuracy-fairness trade-off *within* ICCFL, the cross-method dominance claim (better on both dimensions vs. baselines) is not contradictory but merits a brief explanation, especially since strict accuracy-fairness trade-offs are the norm in fair ML benchmarks.

4. **No uncertainty quantification is provided for the MMD comparisons** in Section 5.3. While the numerical differences (e.g., 0.291 vs. 0.064) appear large, confidence intervals or a permutation test would strengthen the evidence.

5. **The Causal VAE architecture and training procedure are not described.** The paper mentions using a Causal VAE to infer exogenous variables (line 192) and Pyro to construct causal models (line 239), but provides no details on architecture, training objective, convergence criteria, or whether it is retrained during ICCFL optimization or trained once and fixed.

### Trivial
None.

## Nice-to-Haves

- **Ablation isolating the causal component**: Compare ICCFL against a version that minimizes the same CDF discrepancy but on observational (non-interventional) predictions. This would isolate whether the value comes from the *causal* aspect or from using a distributional (rather than point) discrepancy measure.
- **Synthetic experiment with known ground truth**: A controlled experiment where K-Fair=0 but ICRD>0, showing ICCFL detects the disparity that K-Fair-based methods miss, would crystallize the paper's contribution in the most compelling way possible.
- **Computational cost comparison**: Training time of ICCFL vs. baselines would help practitioners evaluate the practical trade-off.

## Removed Points
These points were removed from the input reviews per filtering rules; treat them with caution:

1. **Criticism that the CDF-based approach is a "straightforward extension" of K-Fair**: Subjective assessment of novelty, not a specific verifiable weakness.
2. **Criticism that ICRD is interventional, not counterfactual**: The paper explicitly frames ICRD as an interventional notion; this reflects a reviewer misreading.
3. **Request for missing related works on non-causal CDF-based fairness metrics**: Per hard rules, missing related works are not a valid criticism.
4. **Criticism that Table 2 is an image (parser artifact)**: This is a PDF parsing issue, not a paper problem.
5. **Claim that the accuracy+fairness dominance claim is contradicted by Figure 3**: Figure 3 shows a within-method λ sweep (accuracy-fairness trade-off within ICCFL); Table 2 shows cross-method comparisons. These are distinct and not contradictory.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Add a discussion of the causal graph assumption** and a robustness experiment with misspecified graphs (e.g., adding/removing edges, testing sensitivity). This is the single most important improvement for the paper's practical relevance.
2. **Provide a principled criterion for context variable selection** and discuss what happens with misspecified choices.
3. **Add confidence intervals or bootstrap estimates** for MMD comparisons in Table 3.
4. **Include a brief explanation** of why ICCFL can simultaneously match or exceed baseline accuracy while improving fairness (beyond the usual trade-off).
5. **Specify Causal VAE training details** (architecture, objective, whether it is updated during ICCFL optimization or fixed).

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>