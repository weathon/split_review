## Summary

This paper proposes a "Sparse Causal Model" framework for causal discovery and variable attribution on sparse datasets. The method identifies confounder-treatment pairs via pairwise Pearson correlations, constructs a DAG using CATE-estimated edge directions, selects among 27 model combinations (Linear/XGBoost/GAM for treatment/outcome/residual models) using a composite R²-based Model Score with shuffling-based sensitivity diagnostics, and attributes outcomes through a baseline-scaled decomposition. The paper claims a 53% R² improvement over traditional methods.

## Strengths

- **Systematic model search across three model families.** The framework explicitly enumerates 27 model combinations (three architectures for treatment, outcome, and residual models) evaluated through a structured selection criterion, going beyond ad-hoc single-model approaches common in applied causal inference work.

- **Composite Model Score with sensitivity diagnostics.** The weighted R² score (Eq. 188) combining outcome fit, confounder-shuffled stability, and treatment-shuffled stability is a principled idea for selecting models robust to distribution shift, even if the current formulation and validation are incomplete.

## Weaknesses

### Fatal

- **The headline 53% R² improvement is completely unsubstantiated.** The abstract and conclusion both claim a "53% increase in the R² score" / "53% improvement in causal inference accuracy," yet the experiments section (Section 5) provides no traceable support for this number. Table 1 ("Performance comparison with other models") and Table 2 ("Best model selection") are unreadable images with no numerical values given in text. No baselines are named — "traditional methods" and "single-stage model" are never identified. There are no error bars, confidence intervals, or statistical tests. A quantitative claim of this magnitude that cannot be verified against the paper's own experimental section is a fatal evidential gap that invalidates the paper's central result.

- **Correlation-based "causal discovery" has no principled justification for identifying causal structure.** Section 4.0.2 identifies confounder-treatment pairs by computing pairwise Pearson correlations and selecting the top *k* pairs. The paper offers no theoretical argument or identification condition for why marginal association coefficients would identify confounding relationships specifically. The entire causal inference literature is built on the understanding that correlation does not imply causation, and confounding is a structural property that cannot be read off a correlation matrix. Since the subsequent DAG construction (Section 4.1) inherits these pairs, the entire causal discovery pipeline rests on an unsound foundation. The paper does not even address obvious problems such as spurious correlation, unobserved confounding, or collider bias.

### Major

- **The attribution method is conceptually incoherent.** The baseline prediction is defined as $B_0 = f(\varnothing \cup \varnothing \cup \varnothing)$ — evaluating a model on the empty set, which is not a meaningful quantity. The scaling factor $Scl = B_0/(B_0 + B_1)$ (Eq. 268) is presented without any principled justification, theoretical derivation, or connection to established attribution frameworks (Shapley values, SHAP, integrated gradients, mediation analysis). The distinction between "primary" and "secondary" variables, and between "direct" and "indirect" effects, is asserted but never formally defined or validated.

- **The method is critically under-specified, preventing reproduction or verification.** Key design choices are left unspecified: (1) how the threshold *k* for correlation-based pair selection is chosen; (2) how the Model Score weights $w_o, w_{rc}, w_{rt}$ are determined (Eq. 188); (3) how CATE (defined between a treatment and outcome) determines edge direction between arbitrary feature pairs $(X_k, Y_l)$ where neither is a designated treatment or outcome; (4) how the orthogonality condition (Eq. 198 — a non-standard formulation) connects to or enforces Neyman orthogonality. Without these details, neither the validity nor the reproducibility of the method can be assessed.

### Minor

- **"Sparse" is never formally defined.** The paper's central motivating concept — sparsity — is used throughout the title and body but never operationalized. The dataset has 43,000 SKUs, which is not obviously sparse by any standard definition. It is unclear whether "sparse" refers to observation count, feature dimensionality, or the density of causal relationships.

- **No named baselines in the experiments.** The evaluation compares against "traditional methods" and "single-stage model" without identifying any specific existing causal discovery or attribution method. This makes it impossible to interpret the claimed improvements.

### Trivial

- None major enough to list; the above issues dominate any presentational concerns.

## Nice-to-Haves

- If the method were properly validated and the attribution framework grounded in established theory, a synthetic data experiment with known ground-truth DAGs would be essential for evaluating causal discovery precision/recall.

## Removed Points

*These are points from the inputs that were filtered per the review guidelines; they are listed here for transparency but were not included as weaknesses in the main review.*

- **"Related work is too brief / doesn't engage with causal discovery literature."** Removed per hard rule: missing related works should not be mentioned, as I cannot confirm which methods exist or should have been cited.
- **"No code or pseudocode."** Removed: requesting full training logs or code as a reproducibility complaint about missing large artifacts is outside the scope of a paper review.
- **"Sparsity not formally defined"** was kept as a minor weakness above — it's verifiable from the paper.
- **"Reviewer speculation about what might be in the appendix"** — removed as speculative.
- **"Formatting/style nitpicks"** — removed per hard rules on parser artifacts.
- **Strength finder's "data-driven confounder-treatment pair selection" as a strength.** Removed because this is actually a weakness (correlation-based selection without causal justification), and a strength conflicting with a verified weakness should not stand.
- **Strength finder's "attribution methodology with scaling factor" as a strength.** Removed because the method is conceptually incoherent (empty-set baseline, arbitrary scaling), as verified from the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any unexpected connection, subtle pattern, or non-obvious synthesis that extends beyond the paper's stated claims or the obvious flaws therein.

## Suggestions

1. **Abandon the 53% claim** unless it can be traced to a specific experimental comparison with a named baseline, with error bars and statistical significance reported.
2. **Replace the correlation-based confounder-treatment identification** with a principled approach (e.g., conditional independence tests, score-based search with sparsity constraints, or domain-knowledge-only selection with clear assumptions stated).
3. **Re-think the attribution framework** from the ground up: grounding in Shapley values, SHAP, or mediation analysis would give it theoretical legitimacy, and the empty-set baseline must be replaced with something well-defined.
4. **Fully specify all design choices**: the pair-selection threshold *k*, the Model Score weights, the CATE-based edge direction procedure for arbitrary feature pairs, and the connection to Neyman orthogonality.
5. **Validate on synthetic data with known ground-truth DAGs** to establish that the method recovers true causal structure rather than spurious associations.

## Score and Decision

This paper has multiple fatal weaknesses: its headline quantitative claim is entirely unsubstantiated, its core "causal discovery" mechanism uses marginal correlations without causal justification, its attribution method is conceptually incoherent, and the methodological description is too under-specified to permit verification. These issues cannot be fixed through minor revision — the experimental evidence would need to be rebuilt from scratch, the causal discovery pipeline rethought, and the claims substantially downgraded. Reject.

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>