Now I have a thorough understanding of the paper and the reviews. Let me write the consolidated review.

## Summary

This paper develops a sequential Monte Carlo (SMC) framework for controlled LLM generation that integrates both syntactic (grammar) constraints and semantic constraints that cannot be evaluated per-token. The method correctly targets the intractable global product-of-experts distribution, using importance weight correction to mitigate the greediness of locally-constrained decoding and adaptive resampling to focus computation on promising partial sequences. Experiments on four challenging domains (goal inference, Python data science code generation, text-to-SQL, and molecule synthesis) show consistent improvements over baselines, with ablation studies isolating the contribution of each algorithmic component and validation experiments linking improved posterior approximation to downstream gains.

## Strengths

1. **Consistent and substantial downstream accuracy gains across four diverse domains** — Table 2 shows Full SMC outperforms all baselines in every domain, e.g., Goal Inference: 67.9% vs. base LM 14.6%; Data Science: 47.3% vs. 42.5%; Text-to-SQL: 82.4% vs. 77.0%; Molecule QED: 0.569 vs. 0.530. The improvements are large and clean.

2. **Direct validation that better posterior approximation drives performance** — Figure 2 estimates KL divergence to the global product-of-experts target and finds Full SMC achieves the lowest KL in three of four domains (e.g., Goal Inference: ~0.25 vs. Sample-Rerank ~0.66, p<0.001). Table 3 shows that Full SMC's particle weights have the highest correlation with accuracy in those same domains. This provides direct evidence that accuracy gains stem from better probabilistic inference, not ad-hoc heuristics.

3. **Principled integration of heterogeneous constraints beyond logit masking** — Section 2 and Table 1 formalize how the method incorporates semantic potentials that cannot be evaluated per-token (e.g., running partial code on a test case, plan validation via VAL, SMILES prefix validation). This is a clear advance over prior grammar-only constrained decoding, which is limited to constraints that permit incremental per-token masking.

4. **Clean ablation isolating each algorithmic component** — Table 2 systematically adds grammar constraints, semantic potentials, weight correction, and resampling. Each component produces measurable gains in at least some domains: e.g., in Goal Inference, grammar-only gets 13.4%, adding the semantic potential jumps to 64.7%, weight correction adds 1.6%, and resampling adds another 1.6%. This provides strong evidence that the full SMC pipeline is responsible for the improvements.

5. **Avoids costly contrastive fine-tuning** — Section 4 explicitly notes the contrast with Zhao et al. (2024): the proposed method uses incremental static and dynamic analysis rather than a costly contrastive fine-tuning procedure for twist functions. This is a practical advantage for real-world deployment.

6. **Practical design extensions** — Section 2 describes stochastic approximations to expensive token-masking distributions and line-level SMC steps (over Python statements), making the approach feasible in real-world code generation settings beyond token-by-token SMC.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Numerical discrepancy between Sample-Rerank and Full IS in the Data Science domain** — In the Data Science domain, the grammar potential is set to φ_CFG(x)=1 (trivial). Under this setting, the importance weight for Full IS (Equation 3) simplifies to φ_sem(x), which is identical to Sample-Rerank's weight w(x)=φ_sem(x). The proposal distribution is p_LM for both. Therefore, in principle, both methods should produce identical weighted particles and identical posterior-weighted accuracy. Table 2 reports 48.8 for Full IS versus 47.9 for Sample-Rerank. The difference (~1 point) is small and likely within the confidence intervals, but the mathematical equivalence means the paper should clarify either (a) that this is random variation, or (b) whether the evaluation protocol differs between the two methods (e.g., how posterior-weighted accuracy is computed). This does not undermine the overall findings — the gains in other domains are clean — but it is important for internal consistency.

### Trivial

1. **"Grammar-only" labeling in the Data Science domain is somewhat misleading** — In Data Science, φ_CFG=1 is explicitly trivial. Methods labeled "Grammar-only IS" and "Grammar-only SMC" therefore operate with no actual grammar constraint. The paper explains this clearly at line 148, but the labeling could confuse readers and the "grammar-only" methods are essentially re-runs of the base LM baseline. This is a minor presentational concern.

2. **Molecule synthesis diversity metric needs clarification** — Figure 3 reports a "Diversity" metric but the paper does not explicitly state whether this is computed across all generated molecules or across multiple runs. This is a small missing detail.

## Nice-to-Haves

- **Add a best-of-N baseline**: An even simpler baseline than Sample-Rerank would be to generate N samples and select the one with the highest φ_sem score (best-of-N). This would directly test whether the SMC weighting and resampling provide benefits beyond simple rejection with the best sample. If best-of-N matches Full SMC in some domains, the contribution narrative could be sharpened. The paper does not need this for acceptance, but it would strengthen the empirical story.

- **Report computational cost**: The paper does not report wall-clock time or total LM calls for each method. SMC with resampling involves overhead relative to simple sampling. A brief runtime comparison (even as a simple table) would help practitioners assess trade-offs. This is a practical concern, not a validity concern.

- **Diagnose why resampling does not help in Text-to-SQL**: The paper notes this honestly but does not analyze it. Reporting the effective sample size over generation steps for Text-to-SQL could add insight without requiring new experiments.

## Removed Points

These points are flagged to be removed; treat them with caution.

*(No points from the inputs required removal — all criticisms raised by the harsh critic are factually grounded and merit consideration. The "naming concern" about "grammar-only" in Data Science was kept but downgraded to Trivial since the paper already explains φ_CFG=1. No strawman, factual error, or formatting-nitpick points were found. The strength finder's outputs were all concrete and specific, so none were removed.)*

## Novel Insights

The harsh critic's observation about the Data Science discrepancy is the most insightful cross-cutting point: it reveals an internal consistency check that the authors should verify. The fact that with φ_CFG=1, Sample-Rerank and Full IS are mathematically equivalent but produce slightly different numbers suggests either an implementation-level difference in how posterior-weighted accuracy is computed or ordinary Monte Carlo noise. Resolving this would tighten the paper's internal validity. Beyond this, the reviews do not surface a fundamentally novel perspective beyond what the paper itself contributes — the connection between posterior approximation quality (measured via KL divergence, Figure 2) and downstream performance (Table 2) is already the paper's own strongest analytical contribution.

## Suggestions

1. **Clarify the Data Science discrepancy**: In the final version, explain why Sample-Rerank (47.9) and Full IS (48.8) differ in the Data Science domain despite being mathematically equivalent when φ_CFG=1. If this is random variation, state it explicitly. If the evaluation protocol differs, describe how.
2. **Rename "Grammar-only" baselines in the Data Science domain**: Since φ_CFG=1, consider clear labeling such as "LM + Weight Correction" or "LM + Resampling" to avoid confusion.
3. **Add a best-of-N baseline** as a simple additional comparison in the main results table or appendix.
4. **Report wall-clock time or total LM forward passes** for the main methods to help practitioners understand the computational overhead.
5. **Clarify the molecule synthesis diversity metric** in the caption of Figure 3 or in the main text.

## Score and Decision

This is a well-executed paper with a principled methodology, strong empirical support across four diverse domains, clean ablations, and direct validation of the probabilistic mechanism behind the improvements. The issues identified are minor and addressable. The core contribution — that SMC improves over locally-constrained decoding by integrating heterogeneous constraints and reallocating computation via resampling — is well-supported.

**Originality**: High — SMC with heterogeneous semantic potentials for LLM-controlled generation is novel.  
**Importance of research question**: High — controlled generation is central to deploying LLMs reliably.  
**Claims well-supported**: Yes — ablations, KL divergence analysis, and correlation studies all back the claims.  
**Soundness of experiments**: Strong — four domains, seven methods, appropriate statistical reporting.  
**Clarity**: Good — the method is clearly explained, though the Data Science discrepancy needs clarification.  
**Value to community**: Significant — the modular framework can be applied to many controlled generation problems.

MY FINAL SCORE: <score>8.5</score>
MY FINAL DECISION: <decision>Accept</decision>