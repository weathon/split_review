Now I have all the evidence I need. Let me compose the final consolidated review.

## Summary

This paper proposes a framework for evaluating sparse autoencoders (SAEs) on LLM tasks using **supervised feature dictionaries** as an empirical "skyline." The authors demonstrate on the IOI task with GPT-2 Small that supervised dictionaries (constructed by averaging activations conditioned on attribute values) achieve near-perfect scores on three tests: reconstruction sufficiency/necessity, sparse controllability, and interpretability. They then evaluate task-specific and full-distribution SAEs against this skyline, finding that SAEs capture interpretable features but fall short on controllability. The paper also identifies two qualitative phenomena — feature occlusion and over-splitting — and reproduces them in toy models.

## Strengths

1. **Principled supervised benchmarking framework.** The paper introduces a concrete method for constructing supervised feature dictionaries that serve as an empirical skyline, filling a gap where prior SAE evaluation relied on indirect proxies. On the IOI task, supervised dictionaries achieve near-perfect sufficiency/necessity scores (Figure 2) and >80% editing accuracy (Figure 3), demonstrating that the framework's reference point is meaningful.

2. **Agnostic three-axis evaluation suite.** The framework defines three explicit, well-motivated tests — sufficiency/necessity of reconstructions (agnostic to feature semantics), sparse controllability (formulated as combinatorial optimization with no human-chosen feature-attribute alignment), and interpretability with causal validation. The sparse controllability test in particular addresses a key limitation of auto-interpretability and MMCS metrics.

3. **Identification and partial explanation of qualitative SAE pitfalls.** The paper discovers feature occlusion (higher-magnitude attributes dominating learned features) and feature over-splitting (binary attributes fragmented into many features) in the IOI circuit, and reproduces both in toy models (Section 6). These provide concrete failure modes to guide future SAE design.

4. **Discriminative evaluation across SAE types.** The framework successfully distinguishes task-specific SAEs from full-distribution SAEs: task SAEs achieve higher controllability with fewer feature edits (Figure 3, Figure 5), while full-distribution SAEs require significantly more features (often 32+) with edit magnitudes approaching total reconstruction weight (Section 5.2). The frozen-decoder baseline confirms that observed controllability is non-trivial.

5. **Causal validation of interpretability beyond correlation.** The paper goes beyond correlational F₁ scores by testing whether high-F₁ features are necessary/sufficient for task performance (Section 5.2) and whether they can be used for interpretation-aware sparse control (Figure 5), strengthening confidence in the assignment methodology.

## Weaknesses

### Fatal
None.

### Major
None that rise to the level of undermining the paper's core contribution. The framework itself is well-motivated and the experiments are competently executed. The weaknesses below are significant but addressable.

### Minor

1. **No uncertainty quantification in key results.** Throughout Section 5, results are presented as point estimates without error bars, confidence intervals, or standard deviations (Figures 2, 3, 5). Given that logit differences, editing accuracies, and F₁ scores can vary across prompts, seeds, and cross-sections, the absence of variance reporting makes it difficult to assess whether observed differences between dictionary types are statistically significant. This is a standard expectation for empirical ML work.

2. **ℓ₂ optimization proxy in sparse controllability not validated against behavioral objectives.** The greedy algorithm (Section 5.1) minimizes ℓ₂ distance to a counterfactual activation, but the evaluation metric is next-token prediction accuracy. The paper does not check whether the ℓ₂ minimizer actually corresponds to the edit that maximizes behavioral change for a given number of features. While the same optimization is applied to all dictionaries (so relative comparisons are fair), the absolute performance gap between SAEs and supervised dictionaries could partly reflect optimization misalignment rather than feature quality per se. The paper would benefit from measuring the correlation between ℓ₂ reduction and behavioral change on a held-out set.

3. **SAE hyperparameters not systematically tuned.** The paper explicitly acknowledges (Section 5, footnote) that SAEs were not exhaustively tuned and that better performance may be achievable. This is honest but weakens the headline claim that SAEs "fall short" of supervised dictionaries, since the comparison is between a well-tuned oracle and untuned unsupervised methods. The paper's value as an evaluation framework survives this caveat, but the empirical conclusions about SAE quality should be read as preliminary.

4. **Necessity metric normalization may compress differences.** The normalized necessity metric (Test 1) uses mean ablation as a lower bound for rescaling. Mean ablation can already preserve some task performance (e.g., if the circuit has redundancy), so the rescaling may hide differences between dictionaries, especially when the mean activation already captures task-relevant signal. Reporting raw logit differences alongside the normalized values would improve interpretability.

5. **Single task and model limit generality.** The paper evaluates only on IOI with GPT-2 Small. While acknowledged as a limitation (Section 8), this restricts confidence that the framework's conclusions (or the qualitative phenomena) transfer to other tasks, models, or architectural families. A second, contrasting task — even at smaller scale — would significantly strengthen the contribution.

6. **Over-splitting phenomenon not fully characterized as a problem.** The paper shows that SAEs split binary attributes into many features and that this is not due to overfitting, but does not establish whether over-splitting causally harms downstream use (e.g., controllability or interpretability). The paper's own framing notes "it does not necessarily mean that the SAE failed" (Section 6.2). The phenomenon is intriguing but its status as a "failure mode" rather than a neutral property of the loss landscape needs stronger evidence.

### Trivial

1. **The "first time" claim for disentanglement.** The claim that supervised dictionaries demonstrate "the first time such a disentanglement has been achieved in a realistic LLM task" (Introduction footnote) is slightly overstated given prior work finding linear subspaces for concepts in LLMs (Nanda et al. 2023, Tigges et al. 2023). The paper's related work section appropriately contrasts with these, so the footnote claim would benefit from more measured phrasing.

## Nice-to-Haves

- **Replicate on a second task** (e.g., the greater-than task or a gender-bias task with a smaller model) to demonstrate transferability of the framework. The paper acknowledges this as a limitation, and addressing it would substantially increase impact.
- **Add error bars or bootstrapped confidence intervals** to all quantitative results where variability is expected (editing accuracy, sufficiency/necessity scores, F₁ distributions).
- **Check correlation across the three evaluation axes** for different SAE configurations. If the tests are correlated, a single measure may suffice; if they diverge, the framework provides richer diagnostic value.
- **Compare the framework's outputs to existing proxy metrics** (e.g., MMCS, auto-interpretability scores) to show when the grounded metrics add information beyond existing practices.
- **Brief analysis of computational cost** of the sparse controllability test, which requires per-prompt greedy optimization.

## Removed Points

These points are flagged for removal per the meta-review rules; treat them with caution:

- **Criticism about supervised dictionaries being an inherently uneven comparison (Harsh Critic #1):** The paper explicitly acknowledges this asymmetry (Section 5, footnote) and frames the supervised dictionaries as a "skyline" benchmark, not as a claim that SAEs are fundamentally limited. The comparison is intentional by design — a skyline should be favorable. The paper's core contribution is the evaluation framework itself, not a definitive verdict on SAE quality. This criticism largely misreads the paper's goals.

- **Criticism about missing auto-interpretability contrast in Related Work (Harsh Critic, Section-by-Section):** The paper **does** discuss auto-interpretability (lines 942–966) and its limitations ("the use of maximum activating examples has been criticized as potentially giving an illusory and subjective sense of interpretability"). This criticism is factually incorrect.

- **Criticism about the "first time" claim rendering the contribution merely "incremental rather than foundational":** This is a matter of degree. The paper's related work (Section 7) explicitly contrasts individual-subspace approaches with full decomposition, establishing that the paper provides something prior work did not. The "first time" footnote is slightly overstated (moved to Trivial) but not inaccurate enough to weaken the contribution.

- **Criticism about the paper not using the framework to improve SAEs (Harsh Critic, "Strengthening" #1):** This asks the paper to be a different paper. The framework's purpose is evaluation, not SAE improvement. Using it to guide tuning is future work, not a current flaw.

- **Criticism about occlusion being purely correlational:** The paper performs a **causal intervention** — surgically subtracting supervised IO features and observing monotonic increase in S feature discovery (Figure 6, right). The toy model further isolates magnitude as a causal factor. The critic's concern about confounding is partially valid but does not make the evidence merely correlational.

- **Criticism that the paper does not explain why F₁-based interpretation is preferred over auto-interpretability:** The paper does discuss this (lines 942–949), noting that auto-interpretability can give "an illusory and subjective sense of interpretability."

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a synthesized insight that the paper itself does not already articulate.

## Suggestions

1. **Add uncertainty quantification** (error bars, confidence intervals, or bootstrapped estimates) to all quantitative comparisons between dictionary types. This is the single most impactful improvement for the paper's evidential strength.
2. **Validate the ℓ₂ optimization proxy** by measuring whether ℓ₂ reduction correlates with behavioral change on a held-out subset, or alternatively implement a logit-difference-based feature selection.
3. **Frame the empirical conclusions about SAE quality more cautiously** (e.g., "under the hyperparameter configurations tested, SAEs fall short..."), since the SAEs are not exhaustively tuned.
4. **Add raw logit difference values** alongside the normalized necessity metric so readers can assess the absolute effect sizes.
5. **Provide at least a small-scale second task** (e.g., Pythia-160M on a synthetic task) to demonstrate the framework's generality beyond IOI.
6. Soften the "first time" footnote language to acknowledge prior subspace-finding work more directly.

## Score and Decision

The paper proposes a thoughtful, well-motivated evaluation framework for a timely problem. The experiments are competently executed and the qualitative phenomena are genuine contributions. The weaknesses are real but minor — no uncertainty quantification, one-task scope, undertuned SAEs — and none threaten the paper's core contribution. The paper clearly identifies what it contributes and what its limitations are. It is a solid methodological contribution that the community will find useful.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>