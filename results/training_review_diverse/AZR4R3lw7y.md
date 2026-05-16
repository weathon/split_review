Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated final review.

## Summary

This paper proposes BoostCL, a pretrained-based continual learning method. It provides a theoretical analysis showing that random projection (RP) onto higher dimensions increases the Bayes margin at a rate of O(√d'), offers a Multi-View RP scheme where K atomic-view linear classifiers are combined via a huge-view decomposition (Theorem 4.3, Corollary 4.4), and adapts AdaBoost principles to encourage diversity among views in a CL setting without a memory buffer. The method also introduces a self-improvement process for prompt selection during inference.

## Strengths

- **First formal bound on RP margin improvement for CL (Theorem 4.2).** The theorem provides a probabilistic bound showing that the Bayes margin increases at O(√d') with high probability under an invertible expansive nonlinearity. This directly addresses an unproven hypothesis in RanPAC and offers a rigorous justification for why RP benefits CL — a question the prior work left open.

- **Decomposition theorem makes multi-view ensembles computationally practical (Theorem 4.3, Corollary 4.4).** The paper proves that under a block-diagonal approximation of the Gram matrix, the optimal linear classifier on a huge view (concatenation of atomic views) decomposes into optimal classifiers on each atomic view, and the huge-view prediction equals the sum of atomic-view predictions. This is a clean theoretical result that directly enables the multi-view ensemble without the O((k·d'_a)³) cost of inverting a full huge-view Gram matrix.

- **Empirical evidence isolates the contribution of the multi-view ensemble.** The paper reports results for multiple variants: with high-dimensional RP (d'=10K, K=15), with matched RP dimension (d'=768, K=13), and without RP entirely (K=13). The variant without RP still outperforms RanPAC and other baselines, which — if the empirical results hold — convincingly shows that the multi-view boosting strategy, not just higher-dimensional projection, drives performance gains.

- **The self-improvement process addresses a practical failure mode.** The idea of correcting mispredicted task prompts during inference with a small number of improvement rounds is a simple but sensible mitigation for feature shifts caused by incorrect prompt selection.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical analysis (Theorem 4.2) addresses the Bayes margin but the paper trains a specific linear ridge-regression classifier, creating a gap.** Theorem 4.2 bounds the Bayes margin — the supremum over *all measurable classifiers* — but the actual method solves a regularized least-squares problem yielding a specific linear classifier. The paper provides no argument that this specific ridge-regression solution achieves a margin anywhere close to the Bayes margin. The subsequent implications ("generalization error for each task will be smaller," "task separability increases") implicitly assume the trained classifier inherits the Bayes margin improvement, which is not justified. The theory provides intuition about why RP *could* help but does not formally support the particular algorithm used.

- **The adaptation of AdaBoost to buffer-free CL is not convincingly justified.** In task-incremental CL without a memory buffer, old tasks' data is not retained. The paper trains atomic views sequentially using sample weights Λᵏₜ computed from the error of the (k−1)-th view on the current task's data. The Gram matrices for each view are accumulated incrementally, but sample weights from task t can only affect the contribution of task t's data during the Gram matrix update. Past tasks have already been incorporated without those weights, so the "boosting" effect does not propagate backward. The paper acknowledges that "directly applying AdaBoost/SAMME to CL poses a significant challenge" (Section 3.3) but does not explain how its per-task reweighting scheme overcomes this challenge. A detailed algorithmic description is needed to assess whether this is a genuine adaptation of boosting or merely per-task reweighting without the boosting guarantee.

### Minor

- **The voting strategy for huge views is referenced but the description is unavailable in the extracted text.** The paper states "we then use these responses in a voting strategy, which will be discussed in the next subsection" (line 109), but the relevant subsection was stripped by the parser. The actual voting mechanism (e.g., majority vote, weighted sum, confidence averaging) cannot be evaluated from the available content.

- **The computational implications of "up to 2^K − 1" huge-view responses are unclear.** For K=15, this is 32,767 possible huge views. The paper does not clarify whether all subsets are used, a fixed subset is selected, or some other strategy is employed. While the decomposition theorem avoids separate training for each huge view, the cost of generating and combining 32K predictions at inference time is nontrivial and unaddressed.

- **The block-diagonal Gram approximation (Theorem 4.3) is justified only qualitatively.** The paper states that (Ḡ + λI)⁻¹ approximates (G + λI)⁻¹ "when λ is sufficiently large" but provides no quantitative guidance on selecting λ to balance approximation quality and regularization strength. An operator-norm bound on the approximation error as a function of λ would allow practitioners to assess when the approximation is safe.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing per-task reweighting (the proposed approach) against full AdaBoost with a memory buffer would directly quantify how much of the boosting effect is lost without access to past data.
- Reporting sensitivity of results to hyperparameters (d', K, λ, activation function choice) would strengthen practical guidance.
- If the empirical section (stripped by the parser) already contains a comparison to RanPAC with matching projection dimension (d'=768), that isolates the multi-view benefit. This is a good design that should be highlighted.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The nonlinear activation used in practice (ReLU) is not invertible, so the theorem does not apply."** — The extracted paper text does not specify which activation function is used in practice. The critic assumes ReLU without evidence. Since the activation choice is unstated in the available text, this criticism cannot be verified against the paper. Removed per the rule against unverifiable claims.

- **Criticisms about missing implementation details (voting mechanism, sample weight computation formula, weighted closed-form solution).** — The parser stripped Sections 4.2.2 (continuation), 4.3, 5, and the appendix from this paper. Details of the voting mechanism, the AdaBoost weight update formula, the weighted Gram matrix update, and the self-improvement process exist in the original submission. Per the rules on parser-stripped content, these criticisms cannot be included.

- **"The paper never states this formula [weighted closed-form]" regarding weighted ridge regression.** — This detail would appear in the continuation of Section 4.2.2, which is missing from the extracted text. Removed as a parser artifact.

- **Generic formatting/style nitpicks and concerns about reproducibility requiring trivial implementation details.** — Removed per the corresponding hard rules.

- **Strength Finder claims about "comprehensive empirical validation."** — While the paper's introduction reports results, the full experimental section (tables, baselines, datasets) is in the stripped Section 5. Claims about empirical strength cannot be fully verified from the available text, so I have softened this to refer only to the experimental design (matching-dimension and no-RP variants) visible in the introduction.

## Novel Insights

The key insight that emerges across the reviews is a theory-practice tension: the paper presents a formal margin analysis that applies to the Bayes-optimal classifier in an expanded hypothesis space, but the actual method uses a simple closed-form ridge regression solution on random projections. The decomposition theorem (Theorem 4.3/Corollary 4.4) is a genuinely useful technical contribution that stands independently of this tension — it shows that a large ensemble of random projections can be decomposed into independent atomic-view classifiers, making multi-view RP computationally feasible. The more fundamental question is whether the AdaBoost-inspired training actually induces meaningful diversity among views in a buffer-free CL setting, or whether the empirical gains stem primarily from ensembling many random projections (which Theorem 4.3 enables) with a simpler per-task weighting scheme that does not truly approximate boosting. The paper's own "no-RP" variant suggests the ensemble structure itself carries substantial weight.

## Suggestions

1. **Bridge the theory-practice gap.** Either (a) reframe Theorem 4.2 as providing intuition and a formal bound on data separability (rather than a guarantee about the trained classifier), or (b) extend the analysis to bound the margin of the specific ridge-regression solution after RP (e.g., using concentration inequalities for the empirical Gram matrix).

2. **Specify the AdaBoost adaptation precisely.** Provide a step-by-step algorithm showing: (a) how Λᵏₜ is computed from the error rate (e.g., AdaBoost exponentiation), (b) how the Gram matrix update incorporates these weights, (c) whether weights affect only the current task's contribution or whether some mechanism propagates their effect. Acknowledge the limitation that past tasks' data cannot be reweighted and discuss why per-task reweighting still yields diversity.

3. **Describe the voting mechanism concretely.** State how many huge views are actually used (a fixed subset? all 2^K−1?), how their predictions are combined, and the inference-time computational cost.

4. **Provide guidance on the block-diagonal approximation error.** Give a bound on ‖(G+λI)⁻¹ − (Ḡ+λI)⁻¹‖ as a function of λ and the off-diagonal blocks, so readers can assess when the approximation is safe.

## Score and Decision

The paper proposes interesting ideas (theoretical justification of RP, decomposition theorem for multi-view ensembles, adaptation of boosting to CL) and the empirical design with controlled variants is principled. However, the core theoretical result (Theorem 4.2) has a gap — it addresses the Bayes margin rather than the margin of the specific trained classifier — and the claimed adaptation of AdaBoost to buffer-free CL is not convincingly specified or justified. These are significant issues that prevent the paper from being accepted in its current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>