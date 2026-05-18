Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper introduces Context Steering (CoS), a training-free inference-time method that modulates an LLM's reliance on contextual information by contrasting log-likelihoods of token predictions with and without context, scaled by a tunable parameter λ. The method is applied to three tasks — personalization, bias mitigation, and hate speech quantification — and demonstrated on open-source LLMs (Llama2-7b, Mistral-7b, T0pp, GPT-J).

## Strengths

- **Clean, intuitive formulation.** The core idea — computing a "contextual influence function" as the logit difference between conditioned and unconditioned LLM forward passes, then scaling it by λ — is simple, well-motivated, and trivially implementable at inference time without weight access or fine-tuning (Eqs. 1–3, Section 3.1). This makes it broadly applicable, including to API-gated models that return log probabilities.

- **Qualitative demonstration of controllability.** The examples in Tables 1 and 2 show a clear, interpretable progression of output tone/personalization as λ varies from −3 to +3. The "Blade Runner 2049 with comedy context" case is particularly striking — CoS finds humor in a non-comedy film and tailors the description accordingly, demonstrating the method can handle cross-genre personalization.

- **Unified treatment of diverse problems.** Applying the same λ-modulated contrast to personalization (amplify context), bias mitigation (suppress context via an equalizing prompt), and hate quantification (infer λ via posterior scoring) demonstrates the framing's breadth. The hate quantification idea — using CoS's inverse model to assign a continuous hate severity score — is creative.

## Weaknesses

### Major

1. **BBQ equalizing context is mismatched to several demographic categories.** The paper states it uses $\mathcal{C}_{\text{equal}} =$ "All people should be treated equally regardless of age" (Section 4.2), but Figure 4 reports accuracy and bias across all BBQ subjects — age, gender, race, religion, etc. Applying an age-specific equalizing context to gender or race questions is conceptually mismatched: the model is told to ignore age, but the stereotypes for other categories operate through different mechanisms. The results may still show improvement (any equality-themed prompt might help), but the reader cannot tell whether a properly matched context would work better, worse, or the same. This needs clarification: either report the exact contexts used per category, or justify why the age-specific phrasing was chosen as a single generic intervention.

2. **Insufficient baseline comparisons across all experiments.** For bias mitigation (BBQ), the only comparison is the λ-varying CoS trend itself — no comparison to simpler alternatives (e.g., prepending the equalizing context without CoS, direct instruction like "ignore stereotypes," or standard prompt-only BBQ scores). For hate classification, the only baseline is an unspecified "LLM-based" method (no standard zero-shot classifier, no RoBERTa-based detector, no reference to the dataset's published benchmarks). Without baselines, the reader cannot judge whether CoS adds value over trivial alternatives. The BBQ λ-trend does implicitly include λ=0, but this is not highlighted or discussed as a baseline.

3. **Personalization user study tests only two λ values, weakly supporting the controllability claim.** The user study (Section 4.1) compares λ = −1 and λ = 3. With only two points, the Spearman correlation (ρ = 0.67) simply measures separation between two groups — there is no evidence that intermediate λ values (e.g., 0, 1) produce intermediate personalization. The claim that CoS enables "controllable" levels of contextual influence requires demonstrating monotonicity across at least three values. The qualitative examples (Tables 1–2) partially address this, but the quantitative study does not.

4. **Bayesian inference framing is oversold and underspecified.** Sections 3.3 and 4.3 present Bayesian inversion of the CoS forward model, but the implementation reduces to computing MAP over a discrete candidate set because the normalizing constant is intractable. This is not Bayesian inference in any substantive sense — it is likelihood-based scoring. More problematically, the hate quantification experiment never specifies: (a) the candidate set of λ values used, (b) the prior over λ, (c) whether λ was treated as discrete or continuous, or (d) how the integral in Eq. (16) was approximated. The correlation p-value (p = 0.0295) is reported without describing the Monte Carlo or integration procedure. This level of underspecification prevents reproducibility.

### Minor

5. **IAT experiment is too thin to be persuasive.** The Implicit Association Test experiment (Section 4.2) is described in a single paragraph with incomplete sentences and vague conclusions ("higher λ results in an increased rate of the model rejecting to answer the request" without specifying the rate, and "reduced levels of bias in topics where the original bias level is high" without systematic results, error bars, or per-topic breakdowns). This experiment should either be expanded with full quantitative results or removed.

6. **Inference cost not acknowledged.** CoS requires two forward passes per token (with and without context), doubling inference time. The paper discusses composability and long-sequence limitations in the Discussion but does not mention the 2× inference cost, which is a practical concern for deployment.

7. **Sensitivity to context phrasing not discussed.** CoS prepends the context as a textual prefix; its effect depends entirely on how the context is phrased. The paper does not discuss or experiment with wording variations, which is relevant for both personalization (where context phrasing matters) and bias mitigation (where different equalizing phrasings might yield different results).

### Trivial

- None beyond presentation issues attributable to the PDF extraction process.

## Nice-to-Haves

- For the BBQ experiment, testing with category-specific equalizing contexts (or a truly generic one like "regardless of identity") and reporting results broken down by demographic category.
- Adding at least one more λ value to the personalization user study, or supplementing with an automated evaluation at multiple λ values.
- Reporting the exact candidate set, prior, and discretization for the hate quantification λ-inference procedure.
- Including qualitative examples from the hate classification task (similar to Tables 1–2) to help readers understand how CoS operates on implicit hate.

## Removed Points

- **Criticism about missing DExperts (Liu et al., 2021) connection**: Removed per the rule against mentioning missing related works — I cannot verify the existence or relevance of this reference with the information available.
- **Criticism about the method being "effectively a contrastive decoding approach" with low technical novelty**: The paper already cites Li et al. (2023) for contrastive decoding and discusses the relationship. The critic's framing overstates this as a weakness when the paper's contribution is in the framing and application breadth, which the critic themselves acknowledges is "fine."
- **Criticism about the IAT experiment being "too thin... should either be expanded or removed"**: This is preserved as a Minor weakness (point 5) but the harsh language is softened to match its severity — it does not invalidate the paper's core claims.
- **Criticism about the p=0.0295 correlation without details**: Preserved as part of Major weakness 4, which already covers the underspecification.

## Novel Insights

None beyond the paper's own contributions. The core observation — that LLM token log-likelihood differences between conditioned and unconditioned passes can serve as a tunable "context influence knob" — is the paper's own contribution and does not require additional synthesis from the reviews.

## Suggestions

1. **[Essential] Clarify the BBQ context(s):** Report exactly what context strings were used for each demographic category. If a single context was used, justify why it is appropriate for all categories, or re-run with category-matched contexts.
2. **[Essential] Add baselines:** For BBQ, compare against the plain model without CoS, and against simple prompt-based debiasing. For hate classification, include standard baselines from the Implicit Hate dataset literature.
3. **[Important] Expand the personalization user study** to at least 3 λ values (e.g., −1, 1, 3) to demonstrate monotonicity, or supplement with an automated evaluation.
4. **[Important] Specify the hate quantification procedure:** Report the candidate λ set, the prior, and how the posterior/MAP was computed.
5. **[Good practice] Acknowledge the 2× inference cost** in the Discussion.
6. **[Good practice] Include a brief sensitivity analysis** for context phrasing.

## Score and Decision

The paper presents a clean, well-motivated method with compelling qualitative demonstrations. However, the quantitative evaluation across all three claimed applications has significant gaps — mismatched experimental setup (BBQ context), insufficient baselines, underspecified procedures (hate quantification), thin experiments (IAT), and an underpowered user study (personalization). These issues collectively prevent the paper from substantiating its claims with the rigor expected for publication. The core idea is promising, and most weaknesses are addressable with additional experiments, but the paper in its current form is not ready.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>