- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8
Now I have everything I need. Let me compose the final consolidated review.

## Summary

This paper proposes a framework for evaluating sparse autoencoders (SAEs) by constructing supervised feature dictionaries from task-relevant attribute labels, then using these dictionaries as "skyline" benchmarks to assess unsupervised dictionaries on three axes: (1) sufficiency/necessity of reconstructions for task performance, (2) sparse controllability of attributes via feature editing (agnostic to feature interpretations), and (3) interpretability including causal validation. Applied to the IOI task in GPT-2 Small, the framework shows that supervised dictionaries achieve near-perfect performance (e.g., >80% edit accuracy with just two features), while both task-specific and full-distribution SAEs fall significantly short. The work also identifies qualitative phenomena—feature occlusion and over-splitting—in SAE training.

## Strengths

- **Principled evaluation framework with supervised dictionary skyline (Section 4):** The paper introduces a concrete methodology for computing supervised feature dictionaries (mean feature vectors per attribute value) and validates that they achieve high scores on all three tests (Figures 2 and 3). This provides a grounded "skyline" to contextualize unsupervised SAE performance—directly addressing the lack of ground-truth features that has hampered evaluation in this area.

- **Interpretation-agnostic sparse controllability test (Section 3.3):** Test 2 measures how sparsely a dictionary can edit attribute information using a greedy combinatorial optimization over features, without requiring any human interpretation of what features mean. This overcomes a key limitation of prior evaluation methods that implicitly rely on feature interpretability.

- **Causal evaluation of interpretability beyond correlational metrics (Section 3.5):** The paper verifies that highly interpretable features (F₁ ≥ 0.6) are causally relevant by testing their sufficiency/necessity and using them for attribute editing (Figure 5). This moves beyond the auto-interpretability proxies common in prior work.

- **Controlled baseline with frozen decoder directions (Section 5.2):** The comparison to SAEs with decoder directions frozen at initialization cleanly demonstrates that learned decoder directions provide non-trivial controllability, while random directions perform on par with full-distribution SAEs.

- **Comprehensive comparison of task-specific vs. full-distribution SAEs (Section 5):** The paper evaluates both SAE types on the same three tests and documents nuanced differences—task-specific SAEs enable modest control with fewer features, full-distribution SAEs require many more, and neither matches supervised dictionaries. This highlights concrete gaps for future work.

## Weaknesses

### Fatal
None.

### Major
- **Lack of statistical rigor for core SAE comparisons:** The paper does not report variance, confidence intervals, or mention running multiple random seeds for the main SAE training and evaluation results (Figures 2–4, Section 5.2). SAE training is stochastic, and the paper's central empirical claims—that task-specific SAEs outperform full-distribution SAEs on controllability, that both fall short of supervised dictionaries, and that frozen-decoder SAEs perform on par with full-distribution SAEs—rest on point estimates. Without error bars or replication, it is unclear whether the observed gaps are reliable or could be driven by a single unlucky seed. (Note: multiple seeds are used only for the over-splitting qualitative analysis in Section 6.2, which makes their absence from the main results more conspicuous.)

### Minor
- **Supervised skyline construction relies on an independence assumption validated for this specific task:** The mean feature dictionaries (Section 4.1) work well because the IOI attributes (IO, S, Pos) are probabilistically independent in the IOI distribution. The paper recommends MSE regression as a more general alternative and is transparent about this limitation. However, the comparative claims about how SAEs "fall short" are contextualized against this skyline, so any gap between the mean dictionary and a more expressive learned linear dictionary (with the same sparsity pattern) would affect those conclusions. The paper's core contribution—the *ability to rank* SAE variants—is largely independent of this, but the absolute claims about SAE performance relative to the skyline are somewhat contingent on the skyline being a fair upper bound.

- **Qualitative phenomena (occlusion and over-splitting) are supported by preliminary evidence (Section 6):** Feature occlusion is demonstrated at a single circuit location (queries of L10H0) via a hyperparameter sweep and a surgical manipulation. The over-splitting analysis observes the Pos attribute splitting into many features, but lacks a quantitative similarity metric (e.g., feature overlap or cosine similarity) for the cross-seed/cross-dataset comparison, relying instead on a qualitative "similar above chance levels" assessment. The toy models for both phenomena are simplified (isotropic independent random features, a two-component Gaussian mixture) and the over-splitting toy result is a known property of overparameterized models rather than a phenomenon specific to SAEs. The paper's framing is appropriately cautious, but the evidence does not yet support strong claims about generality.

### Trivial
None.

## Nice-to-Haves
- **Ground-truth intervention target for the controllability test:** The sparse control experiment minimizes ℓ₂ distance in activation space to a counterfactual activation. Using logit difference as the target (as in the sufficiency/necessity test) would be more directly aligned with behavioral control and would connect the two evaluation axes more tightly. The current choice is reasonable but the paper could discuss this design trade-off.
- **Global interpretability statistics for full-distribution SAEs:** The paper reports per-node distributions of interpretable features but does not state the overall fraction of SAE features (that fire on IOI prompts) that receive any interpretation at a given F₁ threshold. Reporting this globally would better characterize how much of the SAE's representational capacity is accounted for.
- **Comparing the mean dictionary to a learned linear dictionary:** Validating that the mean dictionary is near-optimal under the same sparsity pattern (e.g., via sparse linear regression with attribute indicators) would strengthen the claim that it is a meaningful upper bound rather than just one plausible baseline.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Criticism that "the paper should note the S attribute seems less causally separable"** — The paper already notes this on lines 571–575 ("not performing any intervention often already mostly agrees with the ground-truth edit, effectively reducing the resolution of our evaluation results for this attribute"). Already addressed.
- **Criticism about non-exhaustive hyperparameter tuning for SAEs** — The paper explicitly states (lines 605–610): "Importantly, we did not perform exhaustive hyperparameter tuning to train these SAEs, as our main goal was to evaluate the methodology and how it can distinguish between different classes of feature dictionaries, rather than to achieve state-of-the-art performance." This is a conscious design choice, not an oversight.
- **Claim that the interpretability test is "somewhat subjective"** — The paper acknowledges this limitation extensively (lines 419–428, 1019–1032). This is a recognized limitation, not an undiscussed weakness.
- **Pure speculation about results being "idiosyncratic" due to a single random seed** — While the lack of reported variance is a real concern (retained as a Major weakness), the framing that results "may be idiosyncratic" without evidence is speculation.

## Novel Insights
The review process surfaces one insight that goes beyond the paper's own claims: the tension between the paper's stated goal of being "agnostic" to feature interpretations and its reliance on human-chosen attributes for the supervised skyline is more fundamental than the paper fully explores. The three evaluation tests are presented as complementary, but they are implicitly ordered in terms of how much they depend on the chosen attribute ontology: Test 1 (sufficiency/necessity) is fully agnostic, Test 2 (sparse controllability) is agnostic about feature *meanings* but evaluates control over the predefined attributes, and Test 3 (interpretability) is fully dependent on the attribute set. Recognizing this hierarchy clarifies that the framework's strength lies in the layered approach—each test provides a different kind of evidence, and the value of the framework is in combining them, not in any single test.

## Suggestions
- Report results from at least 3 random seeds for the main SAE comparisons (sufficiency/necessity scores, edit accuracy, Pareto trade-offs) with error bars or confidence intervals. This is the single highest-leverage improvement for the empirical contribution.
- For the over-splitting analysis, provide a quantitative similarity metric (e.g., average pairwise cosine similarity or feature overlap Jaccard index) to substantiate the "similar above chance levels" claim across seeds and datasets.
- Consider comparing the mean feature dictionaries against a learned linear dictionary (MSE regression with attribute indicators) to validate that the mean skyline is near-optimal under the same sparsity pattern, as suggested in the paper's own discussion.
