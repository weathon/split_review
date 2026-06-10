Good. I've verified everything. Let me now write the final review.

---

## Summary

The paper proposes Contra+, a method for explaining recommendations by applying contrapositive logic. Instead of asking which historical items, when removed, would change a recommendation (counterfactual), it perturbs the user embedding so the recommended item is no longer recommended (¬B), then identifies which historical items' scores drop most under this perturbation (¬A), yielding explanations of the form "because you interacted with item j, we recommended item i." The method is applied to SVD (via vector perturbation) and MLP models (via gradient steps). A custom evaluation metric is introduced, and experiments on MovieLens-100k, MovieLens-1M, and Netflix are presented.

## Strengths

1. **Computational efficiency is a genuine practical advantage**: For SVD, Contra+ requires only a vector subtraction and dot-product comparison (Equation 3: `p'_u = γp_u − εq_i`), avoiding Hessian computation and model retraining entirely. For MLP, it requires a few gradient steps on a single data point rather than full influence-function inversion (Section 3.2, noting it "takes less than 1 second" vs "at least 5 times longer" for influence functions). This efficiency claim is directly supported by the method's design.

2. **Novel evaluation metric explicitly designed for the contrapositive framing**: The paper introduces M_contra (Equation 2) with a clear conceptual distinction from the standard counterfactual metric via Figure 1's 2×2 contingency table (ratio ①/(①+③) vs ①/(①+②)). The metric asks: "Given a change in recommendation, how many removals instigating this change align with our explanations?" (line 173) — a purpose-built measure absent from the prior work reviewed in Section 2.3.

3. **Bridges theoretical counterfactual backtracking to a practical algorithm**: Section 3.3 draws a thoughtful connection to the theoretical framework of counterfactual backtracking (von Kügelgen et al., 2022), noting that prior work "ha[s] not actually proposed a practical algorithm but rather set up a new theoretical framework." Contra+ provides one of the first practical instantiations of this logically related concept, which is a legitimate conceptual contribution.

## Weaknesses

### Major

1. **SVD method with γ=1 is mathematically identical to the Item Similarity baseline, and the actual γ used in experiments is not reported.**  
   With γ=1, the score change for a historical item h is Δ_h = s(u,h) − s'(u,h) = ε⟨q_i, q_h⟩ (derivable from lines 110–126). The items with highest Δ_h are those with the highest dot product with the recommended item's embedding q_i — i.e., items most similar to the recommended item. The Item Similarity baseline (line 187) "selects historical items most similar to the recommended item as explanations." These are mathematically identical selection criteria.  
   The paper states "For simplicity of exposition, we fix γ=1 for now" (line 120) but **never specifies what γ value was actually used in the experiments** (Sections 4.2, 4.2.1, 4.3). Without this information, the claimed outperformance of Contra+ over Item Similarity in Figures 2–3 cannot be interpreted. If γ=1, the methods are identical and any differences must arise from unspecified implementation details (e.g., the "score of at least 4" filtering criterion in line 126, or a different similarity metric for the baseline). This is a fundamental ambiguity that undermines the paper's central technical claim for the SVD case.

2. **Core hyperparameters of the explanation method are not reported, making the method irreproducible.**  
   The following parameters are defined in Section 3 but never specified for the experiments: (a) ε (the perturbation magnitude, line 111), (b) S (the score threshold below which item i is "no longer recommended," lines 120–123), (c) γ (whether expositional γ=1 carries over to experiments), (d) k (number of gradient iterations for the MLP perturbation, line 139), and (e) η (learning rate for the MLP perturbation, line 139 — the learning rates reported in [0.01, 0.001, 0.0001] in Section 4.3 are for *training* the MLP model, not for the explanation perturbation). The method's sensitivity to these parameters cannot be assessed, and the experiments cannot be independently reproduced.

3. **The logical framing systematically oversells what the method actually delivers.**  
   The paper builds its motivation on the logical equivalence A→B ≡ ¬B→¬A and presents the method as directly implementing ¬B→¬A (abstract, introduction, Section 3). However, the method identifies items via embedding-space proximity: Δ_h measures dot-product similarity between historical items and the recommended item's embedding. This is an associational relationship, not a logical or causal implication. The paper acknowledges this in Section 5 ("we are only approximating the negation of the 'did not interact with item j' statement") but the qualification is buried in limitations, while the main text presents the equivalence as if the method directly operationalizes it. The Godfather example (lines 130–131) illustrates this vividly: the "explanation" that "If The Godfather II was not recommended, the user would not have interacted with The Godfather" relies on the fact that sequels have similar embeddings — this is embedding similarity, not counterfactual causation.

### Minor

4. **No numerical results reporting.** All experimental results are presented only as bar charts (Figures 2–4). No tables report means, standard deviations, confidence intervals, or statistical significance test values. The paper claims "statistically significant improvements" (line 219) but provides no supporting statistics. This makes it impossible to assess the magnitude or reliability of the claimed improvements.

5. **Netflix dataset description is incomplete.** The paper describes the Netflix dataset as containing "approximately 600k data points" (line 219). The full Netflix Prize dataset contains ~100M ratings. If a subsample was used (which it must have been given the cited size), the sampling procedure should be described. Dataset scale directly affects the practical relevance of efficiency claims.

6. **Runtime comparison is not systematic.** The paper claims Contra+ for MLP "takes less than 1 second" and influence functions "can take at least 5 times longer" (Section 3.2) but provides no wall-clock comparison table, no hardware specification, no breakdown by model size, and no comparison for the SVD case. Given that computational efficiency is a central motivation, this is insufficiently quantified.

### Trivial

- The paper uses "statistically significant" (line 219) without providing any p-values or confidence intervals — the asserted significance is unsupported.
- Line 120: "For simplicity of exposition, we fix γ=1 for now" leaves unresolved whether experiments use γ=1 or some other value. This should be stated explicitly.

## Nice-to-Haves

- An ablation varying γ and ε to show how the method transitions from item-similarity behavior (γ=1) to a distinct regime would directly address the core concern about what Contra+ contributes beyond item similarity.
- The evaluation metric requires training 10,000 models (100 users × 100 subsets × factor). While the paper notes this is for evaluation only, an analysis of metric stability with fewer retraining runs would strengthen claims of practical applicability.

## Removed Points

The following criticisms from the reviewers were assessed and removed:

- *Critique that the metric does not test ¬B→¬A but instead ¬A→¬B*: The metric (sample 10% subsets, retrain, identify change-causing subsets, check overlap with explanations) tests: "Given that removing these items changed the recommendation (¬B), are my explanations among them (¬A)?" This is a reasonable operationalization of ¬B→¬A as described in Figure 1's left column. The implementation is indirect but valid. The harsh critic's strict reading is not supported by the paper's own description of the metric (line 173: "Given a change in recommendation, how many removals instigating this change align with our explanations?"). **Removed as unsupported by the paper text.**

- *Critique about 10,000 retraining runs making the method unscalable for practitioners*: The paper explicitly states "this retraining is purely for evaluation's sake, the actual explanation method does not require retraining of models" (line 191). The evaluation procedure is separate from the method's deployment cost. **Removed as the paper already addresses this.**

- *Formatting/style nitpicks and parser artifacts*: **Removed per instructions.** These are PDF extraction artifacts, not author errors.

- *"Not yet released" or reproducibility concerns about cited works*: **Removed per hard rules** — all cited entities are assumed to exist.

- *Strength Finder generic strengths* (e.g., "addressed an important problem"): **Removed as generic/superficial.** Strengths without specific citations or concrete content were dropped per instructions.

- *Critique about missing appendix content or proofs*: **Removed per instructions** — the parser strips these sections; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that Δ_h = ε⟨q_i, q_h⟩ under γ=1 makes Contra+ equivalent to item similarity is the most important analytical insight, but it follows directly from the paper's own equations in Section 3.1.

## Suggestions

1. Report the actual γ, ε, and S values used in the experiments. If γ≠1, state this explicitly. If γ=1, explain how Contra+ differs from the Item Similarity baseline (e.g., is the "score ≥ 4" filter applied asymmetrically, or does the baseline use a different similarity space?).
2. Include a table of numerical results with means and standard deviations for the key experiments (Figures 2–4). Without this, the claimed improvements cannot be assessed.
3. Report k and η for the MLP perturbation method separately from the training hyperparameters.
4. Clarify whether the Netflix dataset is a subsample, and if so, describe the sampling procedure and the original dataset size.
5. Provide a proper runtime comparison table across methods, datasets, and model sizes.
6. Either downplay the logical framing to match what the method actually does (embedding-space perturbation), or add experiments that directly validate the contrapositive interpretation (e.g., intervening on the recommendation output directly and measuring the effect on inferred user interactions, without training-data manipulation).

## Score and Decision

The paper introduces a genuinely interesting idea — using contrapositive logic to frame recommendation explanations — and has the practical advantage of computational efficiency. The evaluation metric is novel and well-motivated. However, the core technical contribution for the SVD case collapses to item similarity under the expositional setting (γ=1), and the paper never clarifies whether the experiments diverge from this setting. This ambiguity, combined with unreported hyperparameters that prevent reproducibility, an inflated logical framing that overstates what the method actually demonstrates, and the absence of numerical results, leaves the paper's central claims unsubstantiated. The idea has merit, but the execution and presentation do not meet the standards required for a top venue.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>