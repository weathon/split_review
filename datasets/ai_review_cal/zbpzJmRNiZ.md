- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3
Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

The paper proposes NAMformer, which augments the FT-Transformer architecture with shallow single-layer networks on uncontextualized embeddings to produce interpretable marginal feature effects while retaining the full interaction-capturing transformer backbone. The approach is clean: additively combine per-feature shape functions (shallow nets on uncontextualized embeddings) with the transformer's contextualized output, and enforce identifiability via feature dropout. The paper provides a theoretical bound linking dropout-based risk to marginal-effect recovery error, an ablation showing strong marginal-effect recovery in simulated data (Table 1), a small comparison showing NAMformer closely matches FT-Transformer under fixed hyperparameters (Table 2), and a larger benchmark against interpretable models where NAMformer is competitive (Table 3).

## Strengths

1. **Theoretical identifiability bound (Section 2.1):** The paper derives an upper bound (Equation 9, leading to ≤2R under uniform-risk assumption) formalizing how feature dropout controls the error in recovering true marginal effects $\mathbb{E}[y|x_k]$. This goes beyond the heuristic dropout used in prior neural additive models (Agarwal et al., 2021) by showing, under distance-based losses, that the bound on marginal-effect error is a function of the overall risk and dropout probability. This is a genuine theoretical addition to the literature on identifiable additive neural networks.

2. **Empirical validation that uncontextualized embeddings preserve feature identity (Figure 3):** The paper demonstrates that decision trees trained on uncontextualized embeddings predict original feature values with $R^2 \geq 0.96$, confirming that token identifiability (Brunner et al., 2019) transfers to tabular data. This provides the empirical basis for why attaching shallow networks to uncontextualized embeddings (rather than contextualized ones) can faithfully capture marginal effects.

3. **Strong marginal effect recovery in the presence of strong interactions (Table 1):** The ablation study shows NAMformer (with PLE encodings) achieves high average $R^2$ for recovering true marginal effects (e.g., 0.99 vs 0.97 for NAMs on Dataset 1) with substantially lower variance across effects (0.00 vs 0.06). This advantage persists as interaction complexity increases, convincingly showing that the transformer backbone does not corrupt marginal-effect identification.

4. **Competitive performance among interpretable models (Table 3):** On a benchmark of 15 datasets with tuned hyperparameters, NAMformer performs (shared) best on 9 out of 15 datasets and achieves the best average rank among interpretable models (including NAMs, EBMs, EB²M, Hi-NAM, GAMs). This demonstrates real-world usefulness.

## Weaknesses

### Fatal
None.

### Major

1. **Central claim of "identical performance" to FT-Transformer is insufficiently supported.** The paper repeatedly states that NAMformer "perfectly maintains the predictive power" (contribution II), achieves "identical performance" (Section 2, conclusion), and performs "as good as FT-Transformer" (Table 2 caption). The sole direct evidence is Table 2: 8 datasets (4 regression, 4 classification) with 5-fold cross-validation under identical hyperparameters. The authors assert "no model achieves significantly different performances with respect to the cross validation results," but no statistical test supports this — no confidence intervals, no equivalence test (TOST), not even a paired t-test. With only 5 folds, "within standard deviations" is not a valid equivalence criterion. This is a serious mismatch between the strength of the claim and the evidence provided.

2. **Black-box comparison results are not presented in the main experiments (Section 4).** The paper states that NAMformer is compared to MLP, XGBoost, and FT-Transformer with tuned hyperparameters, but no table or figure shows these results. The text only says "FT-Transformer can outperform XGBoost on certain datasets" — it does not report how NAMformer compares to FT-Transformer (or MLP/XGBoost) in this tuned setting. For a paper whose headline claim is matching black-box performance, omitting these results is a significant gap. (Note: the paper does not reference a "Table 4"; the issue is not a missing table due to parsing, but that the comparison results are absent from the manuscript.)

### Minor

3. **Theoretical bound lacks empirical validation.** The identifiability bound (≤2R) is mathematically valid under stated assumptions, but no experiment measures the actual recovery error against this bound. The bound depends on the uniform-risk assumption which the authors concede "is unlikely in practice" (line 191). Without an empirical check (e.g., computing the bound vs. actual recovery error in the simulation study), the theoretical contribution remains a formal guarantee without demonstrated tightness.

4. **Feature dropout implementation is underspecified.** The theory models the transformer branch as a monolithic $f_{J+1}$ interaction network with a single dropout weight $w_{J+1}$, but in practice the transformer is more complex (multiple layers, attention heads, [CLS] token). How exactly is dropout applied to the transformer branch during training? The paper states "For NAMs and NAMformer we use identical feature dropout probability of 0.1" (line 198), which implies the transformer is treated as a single unit, but this should be explicitly stated.

### Trivial
None.

## Nice-to-Haves

- **Statistical testing for the equivalence claim:** Even a simple paired test with effect-size bounds would substantially strengthen the "no degradation" claim.
- **Computational cost profiling:** The paper reports the parameter increase ($J \times e < 5000$), but reporting training time or inference latency would help practitioners assess the overhead.
- **Extending the ablation to pairwise interactions:** The limitations section notes the identifiability constraint can extend to pairwise interactions — a small experiment demonstrating this would be a useful addition.

## Removed Points

- **"Table 4 is missing" / "black-box comparison table (Table 4)":** The paper never references a Table 4. The substantive concern (missing black-box results) is retained as Major weakness #2, but the specific "Table 4" framing is removed as factually inaccurate.
- **"No analysis of computational cost":** The paper reports the parameter count explicitly ($J \times e < 5000$). Training time/latency is moved to Nice-to-Haves.
- **"Hyperparameter sensitivity":** A generic concern applicable to any model; the paper tunes hyperparameters in Section 4. No specific evidence of instability is presented.
- **"Larger datasets and many features" / scalability speculation:** Not verified from the paper's content; the paper uses a reasonable benchmark of 15 datasets.
- **"Interpretation of trained model... user studies":** Scope creep; user studies are not standard for this type of algorithmic contribution.
- **"Missing related works":** Cannot be verified; do not have external sources to confirm omissions.
- **All formatting, typo, and grammar criticisms:** Parser artifacts, not author errors.
- **Strength Finder's generic strengths** (e.g., "addressed important problem"): Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Soften the "identical performance" claim to "comparable performance" or "no statistically significant degradation detected,"** and support it with a proper equivalence test (TOST) or at minimum report confidence intervals on the differences in Table 2. Alternatively, present a paired comparison plot with predefined equivalence bounds.

2. **Include the missing black-box comparison results** (NAMformer vs. MLP, XGBoost, FT-Transformer under tuned hyperparameters) — either in a new table or as part of an extended Table 3. If there is a small performance gap, report it honestly; the paper's value does not hinge on perfect parity.

3. **Empirically compute the theoretical bound** in the simulation setting: report the bound (2R) alongside the actual recovery error (MSE or $R^2$ of the marginal effect estimate) to show the bound is not vacuous.

4. **Clarify the dropout mechanism:** explicitly state how feature dropout applies to the transformer branch during training (e.g., "the entire transformer output is dropped with probability 0.1, and each shallow feature network $f_j^\epsilon$ is independently dropped with probability 0.1").
