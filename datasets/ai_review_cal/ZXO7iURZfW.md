- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes FEBP, an LLM-based automated feature engineering algorithm that leverages dataset semantic descriptions and iterative in-context learning. Features are represented in canonical Reverse Polish Notation (cRPN), and the LLM is prompted with dataset attribute descriptions, operator definitions, and ranked example features with scores to iteratively construct new features. Experiments on seven real-world datasets with three downstream models show FEBP outperforming state-of-the-art baselines (DIFER, OpenFE, CAAFE), with a statistically significant advantage.

## Strengths

1. **Consistent performance gains over strong baselines** — Table 2 shows FEBP achieves the highest mean performance score and lowest mean rank across seven datasets and three downstream models (linear models, Random Forests, LightGBM). The Friedman-Nemenyi test confirms significance at p=0.01 against DIFER and OpenFE.

2. **Semantic context demonstrably improves performance** — Table 3's ablation study compares FEBP with and without dataset attribute descriptions. The full version outperforms the blinded version across all three downstream models with statistical significance (p=0.01), and the paper provides a plausible explanation (non-semantic features cause overfitting in tree-based models).

3. **In-context learning drives iterative improvement** — Figure 5 plots cross-validation scores of candidate features against construction iterations, showing a clear upward trend (supported by one-tailed t-test results). This directly demonstrates that FEBP improves feature quality by learning from top-performing examples.

4. **Semantic explanations are generated alongside features** — Figure 4 shows an example LLM output containing both the constructed feature in cRPN and a natural-language explanation of its usefulness. The prompt template (Figure 3) explicitly instructs the LLM to provide such reasoning, making this the first AutoFE method to produce interpretable features with semantic explanations.

5. **Canonical RPN ensures compact representation** — Section 4 describes a canonicalization scheme that produces a one-to-one mapping between features and strings. This reduces the search space compared to free-form code (as in CAAFE) and helps the LLM parse and learn feature patterns reliably.

6. **Feature search dynamics are analyzed thoroughly** — Figures 6–8 examine feature order, tree-edit-distance divergence, and construction efficiency across iterations. These analyses confirm that the search explores then converges, consistent with the claimed in-context-learning-based optimization.

7. **Hyperparameter analysis justifies design choices** — Tables 4–5 examine temperature and number of example features, providing empirical grounding for the default configuration (temperature=1, k=10 examples).

## Weaknesses

### Major

- **Missing baseline that isolates the LLM's contribution** — The paper claims that the LLM's semantic reasoning and in-context learning are key to FEBP's performance, but it never compares against a simple baseline operating in the *same* cRPN search space with the *same* evaluation protocol (e.g., random generation of cRPN expressions, or a simple evolutionary search over the operator set). DIFER and OpenFE use different search spaces and strategies, and the blinded ablation (Table 3) removes semantic descriptions but keeps the LLM. Neither control answers the question: "Would a non-LLM search over the same cRPN space perform similarly?" Without this baseline, the paper's central claim — that LLM guidance adds value beyond the operator set and search protocol — is not fully validated. Adding a random or simple evolutionary baseline in the same space with the same number of feature evaluations would directly test this and either sharpen or weaken the paper's message. (Specific anchor: Section 5 compares FEBP vs. DIFER/OpenFE/CAAFE only; no same-space non-LLM baseline exists.)

- **Ambiguous specification of CAAFE's LLM version** — Section 5.1 states the authors use `gpt-3.5-turbo-0125` and `gpt-4-0613` in their experiments. Section 5.2 states "the performance of FEBP or CAAFE with GPT-4 is not significantly different from that with GPT-3.5," implying CAAFE was tested with both versions. However, Table 2 reports only a single "CAAFE" column without indicating which GPT version was used. If CAAFE was only run with one version while FEBP results are shown for both, the comparison is unfair and the claim about comparable GPT-3.5 vs. GPT-4 performance is unsubstantiated for CAAFE. The authors must specify which GPT version was used for CAAFE in each comparison or present both results. (Specific anchor: Table 2 shows one CAAFE column; Section 5.2 text says "FEBP or CAAFE with GPT-4 is not significantly different from that with GPT-3.5.")

### Minor

- **Statistical significance reporting is incomplete** — The paper states the Friedman-Nemenyi test shows significance at p=0.01 but does not report the actual test statistic, critical difference, or pairwise p-values. With only 7 datasets, the Friedman test has limited power. The analysis also does not break down significance per downstream model, despite substantial variation (large gains for linear models, small gains for RF/LightGBM). The observation that DIFER is not significantly different from FEBP receives no discussion. (Specific anchor: Section 5.2, last sentence.)

- **Average performance gain not computed with confidence intervals** — The abstract and introduction claim "over 5% performance gain on average across three downstream models," but Table 2 shows only per-dataset results. The average gain across datasets and models is not explicitly computed or accompanied by confidence intervals. (Specific anchor: Section 1, Table 2.)

- **Initial random feature generation process unspecified** — The algorithm initializes the prompt with "k random features from the constrained feature space X_T^(2)" but does not specify how these random features are generated (e.g., uniform random over operators and feature indices, or some other distribution). This affects reproducibility and the quality of early search. (Specific anchor: Section 4, line 89.)

- **Maximum operator constraint not specified** — The paper mentions "a constraint instruction to use no more than a certain number of operators" but never states the numerical value used in experiments. This is relevant for understanding the effective search space. (Specific anchor: Section 4, paragraph starting "Our prompt contains...")

- **Meta description usage unclear** — The prompt template includes "a meta description of the dataset (optional)" but the paper does not clarify whether this was used in the reported experiments. (Specific anchor: Section 4, item (1) in prompt components.)

- **Computational cost not discussed** — The paper evaluates performance and search behavior but does not discuss API call volume, approximate monetary cost, or wall-clock time. This is relevant for practitioners assessing practical feasibility, especially since the method requires iterative LLM calls. (Specific anchor: Section 5.)

- **Interpretability claim not evaluated** — The paper lists "providing semantic explanations" as a contribution but does not evaluate explanation quality (e.g., do explanations align with known domain relationships? are they useful to users?). At minimum, a qualitative analysis of example explanations would strengthen this claim. (Specific anchor: Section 1, contribution (1); Figure 4.)

### Trivial

- **Dataset full names and sources not listed** — Table 1 provides abbreviated dataset names (AF, BH, CD, etc.) but does not give full names, URLs, or citations for the seven datasets. (Specific anchor: Table 1.)

## Nice-to-Haves

- A random-cRPN baseline in the same search space (as described in Major Weakness 1) would most sharply test the LLM's value-add.
- Breaking down the statistical significance analysis per downstream model would clarify where the gains are robust.
- A brief discussion of API costs would help practitioners assess feasibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *CAAFE's related-work description is too brief* — Subjective opinion; the paper accurately describes CAAFE and explicitly notes the differences (code vs. cRPN, line 45). Removed as it lacks a specific factual anchor.
- *Why 200 candidate features?* — Partially justified by Figure 9 showing diminishing returns, making this a minor presentation choice rather than a weakness. Removed as already addressed.
- *Exact prompts should be provided in supplementary material* — The parser strips supplementary/appendix content from all papers; these likely exist in the original submission. Removed per hard rule.
- *Table formatting clarity* — Parser-induced artifact; original formatting is not assessable from the extracted text. Removed per hard rule.
- *Temperature tuned for FEBP but not baselines* — Minor fairness concern, but baseline parameters are "initialized per the corresponding papers," which is standard practice. Weakness is stretched; removed.
- *Missing hyperparameter details about baselines* — The paper states parameters are set per the corresponding papers, which is standard. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the method or results that the paper itself does not already provide.

## Suggestions

1. **Add a same-space non-LLM baseline**: Run random generation of cRPN expressions (or a simple evolutionary algorithm over the operator set) with the same evaluation protocol, iteration count, and feature selection procedure. Report whether FEBP outperforms this baseline. This will cleanly separate the contribution of the LLM from the contribution of the search space and protocol.
2. **Clarify CAAFE's GPT version**: Either state which GPT version was used for CAAFE in Table 2, or present both GPT-3.5 and GPT-4 results for CAAFE if both were tested.
3. **Provide fuller statistical reporting**: Report the Friedman test statistic, critical difference, and ideally pairwise p-values per downstream model.
4. **Specify the missing experimental details**: State the maximum operator constraint value, the random feature generation procedure, and whether the meta description was used.
5. **Compute and report the average gain explicitly**: Add a row showing the average performance gain across datasets with confidence intervals.
6. **Discuss computational cost**: Report approximate API call volume and cost, even if rough.
