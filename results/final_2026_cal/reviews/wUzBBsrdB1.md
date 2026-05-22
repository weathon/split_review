Now I have enough context. Let me write the final consolidated review.

## Summary

This paper studies the effect of the sparsity hyperparameter L0 on sparse autoencoders (SAEs) for LLM interpretability. The central claim is that L0 has a *correct* value (the number of true features active per token on average), and that deviating from it—whether too low or too high—causes the SAE to learn corrupted, polysemantic latents that mix correlated underlying features. The authors demonstrate this mechanism in toy models with known ground-truth features, then introduce a proxy metric (decoder pairwise cosine similarity, c_dec) that can indicate the correct L0. They validate c_dec on Gemma-2-2b and Llama-3.2-1b SAEs, showing that c_dec's "elbow" coincides with peak sparse probing performance. The paper further argues that sparsity-reconstruction tradeoff plots are misleading because incorrect but feature-mixing SAEs can achieve better reconstruction than the ground-truth dictionary at low L0.

## Strengths

1. **Clean toy-model demonstration that low-L0 SAEs actively depart from the ground-truth solution.** Section 3.1 initializes a BatchTopK SAE with L0 = 1.8 (below true L0 = 2) to the exact ground-truth decoder and then trains it; the SAE moves away from the correct features and mixes correlated ones (Figures 2, 3). This is stronger evidence than simply showing a poor final SAE—it proves gradient pressure forces feature mixing when sparsity is too tight. Section 3.3 quantifies the mechanism: the trained (incorrect) SAE achieves MSE 2.73 vs. 4.88 for the ground-truth SAE, directly confirming that MSE loss incentivizes mixing.

2. **Figure 4 directly exposes a failure mode in sparsity–reconstruction tradeoff plots.** At the *same* low L0, a trained SAE that mixes features achieves higher variance explained than the ground-truth SAE with correct but orthogonal features. This is a concrete counterexample showing that better reconstruction at a given sparsity does not imply better features—the very premise of sparsity-reconstruction tradeoff plots as an evaluation tool. The comparison is at the same L0, so this is not a misaligned comparison.

3. **Validation of c_dec on real LLM SAEs with sparse probing.** Figure 8 shows that on Gemma-2-2b and Llama-3.2-1b, the L0 at which c_dec has its low-L0 "jump" coincides with peak sparse probing F1 score. This provides a practical, unsupervised proxy that practitioners can compute without ground-truth features.

4. **Unified treatment of both BatchTopK and JumpReLU SAEs.** Section 3.6 replicates the toy-model findings on JumpReLU, and Section 4.1 reveals an architecturally meaningful difference: JumpReLU SAEs' c_dec does not rise at high L0, consistent with their per-latent adaptive thresholds. This is a nuanced architectural finding missed by prior work.

5. **The paper is honest about c_dec's limitations.** Section 6 explicitly states "we do not view this as a perfect guide" and acknowledges that the metric "can sometime remain nearly flat for a wide range of L0." This transparency strengthens the paper's credibility.

## Weaknesses

### Major

1. **The claim that "most commonly used SAEs have an L0 that is too low" is asserted without supporting evidence.** This claim appears in the abstract and the Discussion, supported only by a single sentence referencing "a cursory search of open source SAEs on Neuronpedia" and pointing to an appendix (A.13). No data, table, or systematic survey is provided in the main paper. The paper's core contribution does not depend on this claim, but making a sweeping empirical assertion about the state of the field without evidence weakens the paper's tone and invites skepticism. The authors should either provide a brief systematic survey (e.g., 5–10 widely-used SAEs with their L0) or soften the claim to a plausible implication.

2. **c_dec's "elbow" heuristic for L0 selection is defined post-hoc and not validated as a predictive tool.** The paper shows that on the layers and models tested, the L0 just before c_dec's low-L0 jump coincides with peak probing performance. But this is a qualitative observation, not a *rule* that could be applied to a new layer or model. (a) For Gemma-2-2b Layer 5, the c_dec curve is essentially flat from L0≈200–2000, with the global minimum in the flat region—the "elbow" is not a distinct point. (b) For JumpReLU SAEs (Figure 9), c_dec does not rise at high L0, so the "elbow" concept breaks down. The paper acknowledges these issues in the Discussion, but they mean the metric's practical utility as a *guide* is more limited than the presentation sometimes implies. Validating c_dec on held-out layers with a pre-defined selection rule would significantly strengthen the contribution.

### Minor

3. **LLM experiment plots lack visible error bars.** Figure 8's caption states "3 seeds per L0" but no error bars or shading are visible in the plots, unlike Figure 6 which clearly shows ±1 stdev shading. Showing the variance (even if small) would improve confidence in the results.

4. **The "both too low and too high simultaneously" analysis in Section 4.2 is suggestive but underdeveloped.** The bimodal decoder projection histogram at L0=750 is an interesting finding, but the paper does not test the hypothesis (e.g., by analyzing individual latent firing frequencies) that some latents are too high and others too low. This section reads more like a speculation than a confirmed result.

### Trivial

5. The justification for using absolute cosine similarity in c_dec (Equation 4) is deferred to Appendix A.6. A brief sentence in the main text explaining why absolute value is used (negative correlations also indicate mixing) would improve readability.

6. The paper states "most of the literature evaluates SAEs at a range of L0 values, referring to this as a 'sparsity-reconstruction tradeoff'" (p. 1) and then claims these plots "are not a sound method of evaluating SAEs" (p. 2). While the toy-model evidence supports this for the specific claim that better reconstruction implies better features, the framing should be more precise: sparsity-reconstruction plots are still useful for comparing architectures at the *same* L0; the paper's finding is that they are misleading for selecting the *correct* L0 or for comparing SAEs across different L0 values.

## Nice-to-Haves

- **Test c_dec predictively on held-out layers.** Pick a fixed rule (e.g., "the L0 where the derivative of c_dec exceeds a threshold") on one layer, then apply it to other layers/models and measure how often it matches peak sparse probing.
- **Evaluate whether fixing L0 via c_dec improves actual interpretability** (e.g., automated interpretability scores or a small human evaluation on SAEs at c_dec-recommended vs. lower L0).
- **A table of L0 values for widely-used open SAEs** (Gemma Scope, etc.) to support the "most SAEs have L0 too low" claim.

## Removed Points

These points are flagged to be removed per the filtering rules; treat them with caution.

- Harsh critic's claim that the sparsity-reconstruction comparison is between a trained SAE and a ground-truth SAE at "a lower L0" — this is incorrect; the comparison in Figure 4 is at the *same* L0, so the criticism is factually wrong.
- Harsh critic's claim about "missing error bars" on LLM plots — this is partially valid (no visible shading) but softened because the caption states 3 seeds were run.
- Strength Finder's claim about "Figure 4 directly falsifies the sparsity–reconstruction tradeoff as a model-selection criterion" — kept as a strength but noted it shows a *failure mode*, not a complete falsification.
- Strength Finder's generic "open-source reproducible pipeline" strength — kept briefly but it's standard practice.

## Novel Insights

The paper contributes a mechanistic explanation for why low-L0 SAEs perform poorly: MSE loss actively incentivizes the SAE to mix correlated and anti-correlated feature components into individual latents, and this phenomenon affects *all* latents (not just a subset). The observation that this happens for both too-low and too-high L0 through different mechanisms (resource pressure vs. degenerate solutions) is a useful conceptual distinction. The finding that JumpReLU SAEs naturally "stick" near the correct per-latent threshold (Section 3.6, Figure 7 left) while BatchTopK SAEs degrade symmetrically at high L0 offers practical guidance for architecture choice.

## Suggestions

- Add a small table or survey of L0 values in common open-source SAEs to substantiate the claim that most SAEs have L0 too low. If the data is in Appendix A.13, move a summary to the main text.
- Add visible error bars or shading to the LLM experiment plots (Figure 8).
- Define a specific rule for selecting L0 from the c_dec curve and test it on held-out layers (e.g., hold back Layer 12, define the rule on Layer 5, then apply to Layer 12).
- Qualify the "not a sound method" claim about sparsity-reconstruction plots with a precise statement: "Sparsity-reconstruction plots are misleading for selecting the correct L0 or for concluding that better reconstruction implies better features, though they remain useful for comparing architectures at a fixed L0."

## Score and Decision

**Calibration report:**

*Round 1 bracket:* 4.0–7.0
- "Enforcing Orderedness in SAEs" (avg 3.00, reject) — weaker: pure ordering method with limited validation. Paper under review is clearly stronger.
- "Taming Polysemanticity in LLMs" (avg 4.50, accept poster) — proposed method with weak experiments. Paper under review has cleaner experiments and stronger evidence.
- "The Price of Amortized Inference in SAEs" (avg 5.00, accept poster) — empirical/position paper. Comparable in type; paper under review has cleaner core demonstration.
- "On the Limits of Sparse Autoencoders" (avg 6.00, accept poster) — theoretical + method paper. Paper under review is less theoretical but has more tightly controlled experiments.

*Round 2 narrowing:* 
- "Sparse Autoencoders Trained on the Same Data Learn Different Features" (avg 5.50, accept poster) — empirical study of SAE instability. Paper under review is somewhat stronger (cleaner mechanism demonstration, practical diagnostic proposed).
- "Bimodality of SAE Features" (avg 5.00, reject) — identified phenomenon + fix. Paper under review is stronger (clearer experiments, better validated).
- "Temporal Sparse Autoencoders" (avg 6.50, accept oral) — new method paper. Paper under review is weaker in that it doesn't propose a complete solution.

*Final position:* The paper sits above the 5.0–5.5 range (cleaner than the "Same Data" and "Bimodality" papers) and is comparable to the 6.0 "Limits of SAEs" paper, though for different reasons (empirical clarity vs. theoretical depth). It falls short of the 6.5 "Temporal SAEs" paper which proposed a more complete architectural solution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>