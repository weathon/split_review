Now I have a thorough understanding of the paper and can verify all claims. Let me produce the final consolidated review.

## Summary

This paper proposes SITD, a method that uses Double Machine Learning (DoubleML) to test Granger causality for time-series causal feature selection. The key idea is to frame Granger non-causality as equality of linear moment functionals and test it via doubly robust estimators, avoiding the faithfulness assumption and allowing cycles and confounding among covariates. The method provides √n-consistent estimates and uses a zero-masking trick to avoid retraining nuisance functions for each candidate cause.

## Strengths

- **Generalization of the Granger–causality equivalence without faithfulness** (Theorem 1, §4.2): The paper proves that under axioms (A1)–(D), Granger causality coincides with true direct causation, extending prior results (Peters et al., 2013; Löwe et al., 2022) beyond fully autoregressive models to settings with cycles among covariates and hidden confounding among them. This is a true theoretical step forward.

- **Doubly robust estimation with √n-consistency** (§4.1): The construction of an orthogonal score using the Riesz Representer, and the validation that it satisfies the Mixed Bias Property, gives the estimator a genuine statistical advantage: convergence at √n-rate even when nuisance functions converge slowly, provided their product rate beats √n. The paper correctly links this to the DoubleML literature.

- **Computationally efficient algorithm design** (Algorithm 1): Training the full model (g⁰, α⁰) once and reusing it across candidate causes via zero-masking yields O(mdk) total time where d is the regression cost. Even setting aside the zero-masking validity question (see Weaknesses), the overall framework of using a single trained model to generate per-cause test statistics is a practical improvement over methods requiring per-cause model retraining.

- **Clear theoretical positioning against related work** (§2): The paper systematically explains why existing methods require faithfulness, causal sufficiency, or restrictive functional forms, and why CI-testing-based approaches face known hardness results. This motivates the contribution clearly.

- **Rigorous treatment of identifiability conditions**: The paper explicitly states its four axioms, discusses the necessity of (C) (no instantaneous effects) for observational causal discovery, and notes the special case where it can be relaxed (linear Gaussian instantaneous effects), citing prior work.

## Weaknesses

### Fatal
None.

### Major

- **The zero-masking trick lacks justification in the main text and raises a legitimate mathematical concern.** The algorithm avoids training separate regression models for each candidate cause by zero-masking the nuisance functions g⁰ⱼ and α⁰ⱼ for feature Xⁱ, yielding surrogate models that are then used to compute θⁱⱼ. The claim is that this produces the correct reduced conditional expectations. However, for a nonlinear function, setting a variable to zero is not equivalent to marginalization. The paper states (line 292) "Please refer to app:zero-mask on why zero-masking is not hurting the estimations," but the main text provides zero justification or intuition. Since the appendix is not accessible in the review process, the reader cannot verify that this central algorithmic step is sound. If the trick is invalid, the per-cause test statistics would be incorrect. This is the most consequential issue in the paper and must be addressed — either with a justification in the main text or by abandoning the trick. **(Note:** the paper does cite an appendix for justification; the criticism is that the main text's presentation gap is significant for such a non-obvious claim.)

- **Experimental claims modestly outpace the evidence.** The paper asserts that SITD is "significantly more performative than state-of-the-art baselines" (line 26). On the Dream3 benchmark (Table 1), SITD wins on 2/5 tasks (E.Coli 1, E.Coli 2), ties on 1/5 (Yeast 2), and is slightly behind on 2/5 (Yeast 1, Yeast 3). The margin of victory is small (e.g., 0.704 vs. 0.686 on E.Coli 1; 0.680 vs. 0.666 on E.Coli 2), and no error bars are reported for any baseline method. For the reproduced Rhino/Rhino+g baselines, a single fixed hyperparameter configuration (taken from the E.Coli 1 setting) was used across all five tasks, while the authors' own method implicitly benefits from the choice of kernel ridge regression and the overall framework. The missing uncertainty quantification and uneven tuning makes it impossible to judge whether the reported differences are statistically significant.

### Minor

- **The handling of hidden confounders is narrower than an unsuspecting reader might infer.** The paper states it "allow[s] for the presence of hidden confounders among the covariates" (line 25) and "hidden common confounders between the potential causes" (line 186). This is explicitly limited to confounding among the candidate causes. The structural equation (A1) assumes ε_T is exogenous and independent of the history, which rules out hidden confounders that directly affect both Y and a covariate — i.e., the classic treatment–outcome confounding scenario. Most of the paper's high-level descriptions (abstract, introduction, discussion) use the unqualified phrase "hidden confounding," which could mislead readers. The paper should explicitly contrast what it handles with what it does not.

- **The i.i.d.-trajectories assumption is stated but not discussed.** The paper assumes (line 169) i.i.d. copies of entire time-series trajectories. In many real applications (climate, finance, healthcare), one observes a single long time series. The restrictiveness of this assumption and whether it can be relaxed to stationarity and mixing is not addressed. This should be acknowledged.

- **Statistical significance of the core test is not validated in finite samples.** The paper uses a paired Student's t-test on the cross-fit estimates θ⁰ⱼ and θⁱⱼ, but the number of folds k is typically small (k ≥ 2). With a small number of partitions, the t-test may have low power or poor calibration. The paper does not discuss this or provide empirical validation (e.g., a null-95% quantile table or a permutation test alternative).

- **Missing error bars for all baselines** (Table 1): Only SITD's standard errors are reported. For the reproduced Rhino/Rhino+g results, multiple runs with different seeds could provide error bars. Without them, the reader cannot assess whether SITD's advantages are reliable.

### Trivial

- The runtime analysis (Algorithm 1, O(dk)) omits the cost of the t-test across m candidate causes. This is negligible but the accounting is slightly incomplete.

## Nice-to-Haves

- A proof sketch of Theorem 1 in the main text, explaining how the argument differs from Peters et al. (2013), would help readers who cannot access the appendix.
- An empirical runtime comparison (wall-clock time vs. baselines) would strengthen the "significantly faster" claim.
- A synthetic-data experiment with known ground truth, where the type of hidden confounding is varied, would clarify the scope of what the method can and cannot tolerate.

## Removed Points

- **"Full causal discovery discussion assumes acyclic system, contradicting claims about cycles"** — Removed. The paper explicitly states (line 297) "for fully-observed acyclic auto-regressive models." This is a separate, restricted setting from the paper's main (feature-selection) claims and is not a contradiction.
- **"Runtime analysis is superficial"** — Downgraded to Trivial. The complexity accounting is slightly incomplete but not misleading.
- **"Proof of Theorem 1 relegated to appendix with no sketch"** — Removed per rule about missing appendix content. The parser strips appendix sections; this exists in the original submission.
- **Strength Finder's "state-of-the-art empirical performance"** — Weakened to reflect that SITD wins on 2/5, ties on 1/5, and is behind on 2/5 tasks. The factual table is kept; the overclaim is noted in Weaknesses.

## Novel Insights

The most interesting observation from this review process is that the DoubleML + Riesz Representer framework, originally designed for average treatment effect estimation, can be repurposed to test Granger non-causality by framing it as an equality of moment functionals. This is a genuinely creative application that opens a new methodological bridge between the debiased ML and time-series causality communities. The zero-masking trick, if it can be justified, would be the practical enabler that makes this approach computationally viable for high-dimensional settings.

## Suggestions

1. **Clarify the zero-masking justification in the main text.** Either provide the mathematical condition under which it is valid (e.g., if the regression model is additive in the features, or if the RR belongs to a known family), or state that the current empirical evidence suggests it works in practice (with supporting experiments), or acknowledge the limitation and use the slower per-cause procedure.
2. **Add error bars for all baselines** in Table 1, especially the reproduced Rhino/Rhino+g results, and clarify whether the reported numbers are single-run or averaged.
3. **Tone down the performance claim** from "significantly more performative" to "competitive" or "state-of-the-art on several tasks," which better matches the evidence.
4. **Discuss the i.i.d.-trajectories assumption** and whether the results extend to single-long-trajectory settings under stationarity and mixing conditions.
5. **Explicitly state the limits of the hidden-confounding claim** in the introduction: SITD handles confounding among potential causes but does not handle hidden confounders that directly affect both Y and a covariate.

## Score and Decision

The paper's core idea — using DoubleML to test Granger causality without faithfulness — is genuinely novel and well-motivated. The theoretical framework (Theorem 1, the MBP-based √n-consistency) is sound and extends prior work in meaningful ways. However, the paper has two significant problems: (1) the zero-masking trick, central to the algorithm's efficiency, lacks a clear justification in the main text for a non-obvious operation, and (2) the empirical claims modestly outpace the evidence, with no error bars for baselines and uneven hyperparameter treatment. These are addressable but serious in the current form. The paper makes a real theoretical contribution and the approach is worth developing, but the presentation gap on the algorithmic core and the overstated empirical claims prevent acceptance in the current state.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>