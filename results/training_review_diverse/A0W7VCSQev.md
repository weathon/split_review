Now I have all the evidence I need. Let me produce the consolidated review.

## Summary

This paper identifies *select-and-copy* attention heads in LLMs that process multiple-choice QA by semantically aligning the question with answer options, and proposes two new scoring methods (QK-score and Attention-score) extracted from these heads that outperform standard logit-based evaluation. The method yields up to 16% improvement on real MCQA benchmarks and near-perfect accuracy on a synthetic task where the baseline fails (~10%), with supporting causal ablation, universality analysis, and an unsupervised head-selection heuristic.

## Strengths

- **Novel score extraction from interpretable heads yields large, consistent gains.** The QK-score and Attention-score exploit the query–key interactions of select-and-copy heads, achieving up to 16% absolute improvement on real MCQA datasets (Figure 3, LLaMA2-7B zero-shot) and ~60% gain on the synthetic SSD task, where the baseline achieves only ~10% while QK-score approaches perfect accuracy (Figure 5b). This directly validates the central claim that internal heads capture knowledge the model's final output does not reliably express.

- **Causal validation of universal select-and-copy heads across models.** The paper shows that specific heads (e.g., (14,24), (14,20) in LLaMA2-7B) rank among the top 5% across all four real datasets and shot counts (Figure 5a). Zero-ablation of these heads produces dramatic accuracy drops, often below random (Figure 4), establishing a causal mechanistic link—stronger than typical correlational studies.

- **Practical unsupervised head selection.** The paper proposes a scoring heuristic based on attention-weight concentration and variability that ranks the key heads in the top 10–20 without any labeled validation data (Figure 6). This reduces dependence on labeled sets and extends applicability to low-resource scenarios.

- **Robustness to option permutation and distractor options.** The QK-score method maintains higher Permutation Accuracy (PA) than the baseline across all datasets (Figure 3, Table 1), and handles the addition of "None of the above" and "I don't know" options without performance collapse—a limitation of the PriDe baseline.

- **Thorough token-representativity analysis.** The paper systematically compares option-representative tokens (label, period, end-of-line, etc.) in Figure 2, showing that end-of-line tokens work best while label-based heads behave differently in few-shot settings. This granularity grounds the mechanistic interpretation and provides actionable design choices.

- **Scale and model diversity.** Experiments span LLaMA2 (7B, 13B, 70B) and LLaMA3 (8B, 70B), including base and chat/instruct variants (Table 1). Consistent gains (e.g., 27% on HellaSwag with LLaMA3-8B) demonstrate the phenomenon is not confined to a single architecture or size.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **QK-score implementation detail underspecified regarding RoPE.** The paper states that QK-score does not apply positional transformation (lines 88, 117) but does not specify whether query and key vectors are extracted **before** RoPE (i.e., immediately after the linear projections \(W_q, W_k\)) or **after** RoPE with the rotation discarded. This matters for reproducibility: the two choices produce different vectors with different semantic properties. The paper's intent is clear—avoid positional bias—and a practitioner would likely infer the correct interpretation, but the specification should be made explicit (one sentence would suffice).

- **Main results table could benefit from a universal-head column.** The headline results (Table 1, Figure 3) use dataset-specific heads selected from a 5% validation subset, while the standard baseline uses no validation data. The paper does compare against PriDe (which also uses 5% data), partially addressing the asymmetry. The analysis section already identifies universal heads (e.g., (14,24)) and an unsupervised selection method that avoids labels altogether. Adding a column with universal-head results (or the unsupervised selection method) to the main tables would make the advantage of the scoring itself transparent and fully address this concern.

- **Limitations section is too sparse.** The three-sentence limitations section (lines 327–330) mentions resource scarcity and MCQA criticism but omits two important caveats: (1) the method's reliance on a labeled validation set for best performance, and (2) its weaker results on knowledge-oriented tasks (MMLU for 70B models). Both are already mentioned in the body of the paper but should be collected in the limitations section for completeness.

- **Ablation study could be more granular.** The paper ablates sets of 10 heads collectively vs. random heads, which is a sensible design. However, ablating the single best head alone would provide a stronger individual causal test. The current analysis is still informative but would benefit from this additional condition.

### Trivial

- The synthetic dataset (SSD) is described in sufficient detail for reproduction (2,500 examples, format specified), but the paper does not mention plans for code or data release. Making these available would strengthen reproducibility.
- No confidence intervals or significance tests are reported; this is common in large-scale LLM evaluations but would strengthen the ablation conclusions.

## Nice-to-Haves

- **Impact of added E/F options on baseline accuracy**: The paper adds "None of the above" and "I don't know" to all datasets. While both methods are evaluated on the same modified data (so the comparison is fair), an ablation showing how much the extra options affect the baseline's accuracy would strengthen the claim that the method is more robust to distractors.
- **Comparison to a linear probe on hidden states**: While the paper focuses on attention heads (a different level of analysis), a linear-probe baseline on the last-token hidden state would help position the method relative to existing internal-representation approaches.
- **Statistical quantification**: Confidence intervals for the ablation study would further strengthen the causal conclusions.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **MMLU inconsistency as a hidden weakness**: The reviewer claims the paper "does not grapple with the implication that the method does not universally improve performance." This is factually inaccurate—the paper explicitly states (line 193) "MMLU is the most difficult benchmark for our method, likely because questions from it are oriented on general knowledge while our method by design focuses more on the semantic relations between the question and the possible answers." The paper also presents the full results transparently (Table 1) and qualifies the abstract claims ("up to 16%" is correct). The criticism overstates a limitation the paper already addresses.

2. **"The Y-axis scale is not explicitly labeled with numbers"**: This is a parser artifact complaint about a figure; the original submission would have clear figures. Removed as a formatting nitpick.

3. **"The paper does not report whether the baseline is also run on this modified format or on the original format"**: The paper's experimental setup (adding E/F to all datasets "in all five datasets") clearly implies both methods are evaluated on the same modified data. The baseline is described using the standard logit approach applied to the same inputs. No ambiguity exists beyond what a parser artifact might create.

## Novel Insights

The most insightful finding from the reviews is the complementarity pattern between the two best universal heads: (14,20) is biased toward options A/D while (14,24) is biased toward B/C (Section 6, "Selection bias"). This observation, noted briefly in the paper, suggests that an ensemble of these heads could cancel out selection bias—a concrete and testable extension that the authors could implement without any additional data. The reviews also highlight that the paper's unsupervised head-finding heuristic (attention concentration × variability) is potentially its most practically valuable contribution, since it bypasses the labeled-validation requirement entirely, yet this is relegated to the analysis section rather than featured in the main results.

## Suggestions

1. **Clarify the QK-score extraction point**: Add one sentence: "We extract the query and key vectors immediately after the linear projections \(W_q, W_k\) and before the RoPE rotation is applied, so that the dot product captures semantic similarity independent of position."

2. **Add a universal-head column to the main results**: Include results from head (14,24) (or the best universal head for each model) as a separate row in Table 1, alongside the dataset-specific best-head results. This provides a clean comparison showing the scoring method's contribution independent of validation-set head selection.

3. **Expand the Limitations section**: Add two bullet points covering (a) the method's weaker performance on knowledge-heavy tasks like MMLU for large models, and (b) the reliance on a validation set for optimal head selection (with a pointer to the unsupervised heuristic as a partial remedy).

## Score and Decision

The paper makes a genuine contribution: it identifies a novel mechanistic phenomenon (select-and-copy heads), proposes a practical extraction method (QK-score), and provides solid causal validation across model scales. The remaining weaknesses are minor and addressable in a revision—they do not threaten the core claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>