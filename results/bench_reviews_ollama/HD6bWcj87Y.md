## Summary
The paper proposes In-Run Data Shapley, which redefines the cooperative-game utility as a per-iteration loss change along a single training trajectory, then uses first- and second-order Taylor expansions to derive closed-form Shapley values that reduce to gradient dot-products and gradient–Hessian–gradient products. A "ghost dot-product" technique (extending ghost clipping from DP literature) computes all per-sample dot-products in one backward pass, making first-order attribution nearly free and enabling case studies on GPT-2/Pile pretraining (copyright/paraphrase ranking, stage-dependent contributions, and data curation).

## Strengths
- **Ghost dot-product / ghost vector-Hessian-vector product (Section 4.2, Eqs. linear-decompose-main and non-seq).** Reusing the per-sample output gradients already produced during backpropagation to compute all pairwise gradient dot-products in a single backward pass is a concrete, non-trivial systems contribution; Figure 1 shows >30× speedup over naive per-sample gradients and near-zero overhead vs. regular training on GPT2-small.
- **Closed-form second-order Shapley (Theorem 2).** The decomposition into a first-order TracIn-Ideal term plus a Hessian-mediated interaction term has a clean interpretation (penalizing redundancy/duplicates inside the batch) and avoids combinatorial enumeration — a genuine methodological contribution beyond TracIn.
- **Per-iteration linearization with linearity-of-Shapley aggregation (Section 3).** Embedding the realized batch/randomness into a local utility, then using the linearity axiom (Theorem 1) to legitimately sum per-step Shapley values, provides a principled and scalable alternative to retraining-based Data Shapley and lets the method expose stage-dependent contributions that retraining methods cannot show (Figure 2).

## Weaknesses

### Fatal
None.

### Major
- **Framing vs. what is actually computed (Section 3).** The introduction sells the method on the *uniqueness* of Shapley under the four axioms applied to $U(S)=\mathrm{metric}(\mathcal{A}(S))$, but the algorithm computes Shapley values of a *different* game: per-iteration linearized utilities along a fixed trajectory $\{w_t\}$. The summation across $t$ is valid by linearity, but the resulting score only attributes one-step counterfactuals around the realized $w_t$ — it cannot represent how an earlier data point would have changed which later batches are useful, and points never sampled in any batch get zero by construction. The paper's repeated claim of "fair, axiomatically unique attribution to the specific trained model" is therefore stronger than what the construction supports; a more accurate framing would be "Shapley-decomposed TracIn with batch-interaction terms."
- **SGD-as-proxy-for-Adam undercuts the foundation-model pitch (Section 6 / Conclusion).** The ghost techniques are explicitly SGD-only ("using SGD as a proxy for Adam … is the approach adopted in practice"), but GPT-2/foundation-model pretraining uses Adam/AdamW. The "attribution to *the* specific training run" claim is hard to sustain when the trajectory the attribution is computed along is not the trajectory that produced the model the user cares about. No experiment validates that SGD-proxy attribution correlates with Adam-trajectory attribution.
- **Data-curation experiment lacks controls (Section 5.2.3, Figure 4).** Shapley values are computed against the Pile *validation set* and then negatively valued points are removed; convergence is reported on a related test loss. The headline "≈16% of the Pile is noise" cannot be separated from validation-aligned filtering without (i) random-removal of an equal token budget, (ii) removal of an equal fraction of bottom-by-loss points (a standard cheap baseline), and (iii) evaluation on distributions disjoint from the scoring validation set. Only an influence-function comparison is shown.

### Minor
- **Taylor-approximation error is asserted, not measured in context (Section 4.1).** The "<10% / <4% relative error" claim is stated without showing whether this is per-step or cumulative, and the ranking conclusions depend on summing over $T$ steps where errors may drift.
- **Empirical scope is narrow.** All experiments are GPT2-small on uncopyrighted Pile. Table 1's "Similar topic" rank gap (145 vs. 292) is reported without variance, on what appears to be a small number of paraphrase tuples, and the copyright argument in Section 5.2.1 rests on one Wikipedia-musician/violinist example. The stage-dependence claim in Section 5.2.2 likewise rests on one math-validation corpus and one figure.
- **Second-order ghost technique is presented but key derivation deferred (Section 4.2, "derivation is omitted").** Since the central efficiency claim for the second-order method depends on it, the main text leaves the reader unable to assess correctness without the appendix.
- **Points never sampled get exactly zero attribution.** For single-epoch pretraining where most points are seen at most once, this is a substantive design choice that should be discussed explicitly rather than handled as a notation footnote (Section 3, "augmented utility function").
- **Runtime claim is qualified only in the limitations.** "As fast as regular training" holds for GPT2-small batches that fit in 80GB; the per-sample activation memory requirement scales with batch size, which constrains the applicability claim to larger models.

### Trivial
- IF vs. In-Run Shapley rank gap (Section 5.2.1) is interpreted as IF being "noisy," but the two methods use different signals (final-model gradient vs. summed trajectory gradients); the interpretation would be more defensible with a controlled comparison.

## Nice-to-Haves
- A small-model experiment computing attributions on both an SGD and an Adam trajectory of the same setup, to defend the SGD-as-proxy claim.
- Random and high-loss-removal baselines for Section 5.2.3, plus held-out evaluation distributions.
- A run-to-run variance study showing how stable In-Run Shapley rankings are across seeds, to substantiate the "targeted to the specific run" framing.
- A larger paraphrase benchmark (hundreds of tuples, reported variance) replacing the single anecdote in Table 1.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "Reproducibility hinges on the appendix" for the second-order ghost derivation — appendix material is stripped by the parser and standardly available in submissions; the main-text presentation-gap concern is kept under Minor instead.
- Generic Strength Finder claims such as "rigorous integration of stochastic training into the utility" and "revealing dynamics of data contribution" — these are largely restatements of the contribution rather than independent evidence. Kept only the specific, evidence-backed strengths.
- Harsh-critic claim that the "16% noise" conclusion is methodologically circular *in itself* — the more precise issue (kept above) is missing controls, not circularity, since the validation set is a legitimate target.

## Novel Insights
None beyond the paper's own contributions. The genuinely novel ideas — viewing TracIn-Ideal as a first-order Shapley decomposition and adding a Hessian-mediated batch-interaction term that handles redundancy analytically — are the paper's own.

## Suggestions
- Reframe the contribution as "scalable Shapley-decomposed per-step attribution with batch interactions"; reserve the uniqueness/axioms argument for the local utility only.
- Add the missing controls in Section 5.2.3 (random removal, bottom-by-loss removal, held-out evaluation) before claiming a fixed percentage of Pile is harmful.
- Run at least a small-scale SGD-vs-Adam attribution-correlation study to defend the foundation-model use case.
- Measure cumulative Taylor error over training and report first- vs. second-order ranking agreement as $T$ grows.
- Discuss explicitly the implication that points unseen in any batch receive zero attribution under single-epoch pretraining.

## Assessment
- Originality: The ghost dot-product extension and the closed-form second-order Shapley with interaction term are original and useful.
- Importance: Data attribution at pretraining scale is a high-value question.
- Soundness of claims: The technical math is correct, but the "axiomatic uniqueness" framing and the "specific trained model" claim are stronger than the construction (SGD-proxy + per-step linearization) supports.
- Soundness of experiments: One small model, limited controls in the curation experiment, anecdotal evidence for headline copyright and stage-dependence claims.
- Clarity: Generally clear; the second-order ghost derivation is the main presentation gap.
- Value to community: The ghost dot-product technique alone is likely to be reused; the framing and curation claims would benefit from more rigor.

Net: a real engineering and methodological contribution with overclaimed framing and under-controlled empirical claims, but not fatally flawed.

## Score and Decision
MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>