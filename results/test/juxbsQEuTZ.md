Now I have a thorough understanding of both the paper and the reviews. Let me produce the consolidated review.

## Summary

This paper studies how training data characteristics—specifically syntactic complexity (center-embedding vs. right-branching) and syntactic diversity (number of unique syntax trees)—determine whether decoder-only Transformers learn hierarchical grammatical rules or surface-level linear heuristics in two synthetic grammar tasks (question formation and tense inflection). It then connects these data properties to training stability, showing that models only stabilize when they commit to a rule (linear or hierarchical), and that intermediate data diversity/heterogeneity produces unstable training dynamics and bimodal seed-level outcomes.

## Strengths

1. **Causal isolation of center embeddings through direct ablation.** The QF experiment (Figure 3 left) compares training on *only* center-embedded declarations (median OOD accuracy near 100%) vs. *only* right-branching declarations (near 0%), holding the question-formation samples fixed. This clean contrast—where both conditions contain modifying clauses but differ in embedding position—directly attributes hierarchical generalization to center embedding rather than to structural complexity in general.

2. **Two-task validation of the core findings.** Both the data-complexity results (Section 4) and the stability analysis (Section 5) are replicated across question formation and tense inflection tasks using the same methodology and 50 seeds per condition, strengthening generality beyond a single synthetic grammar.

3. **Establishing stability as a consequence of rule commitment with a quantitative measure.** The total variation (TV) metric across 2K-step checkpoints reveals that low-TV (stable) runs always converge to either 0% or 100% OOD accuracy, while unstable runs occupy intermediate values. The systematic variation of data mixes in Figure 4 shows that heterogeneous data increases the proportion of unstable runs, providing a mechanistic explanation for previously observed seed inconsistency (Figure 5).

4. **Inverse U-shaped relationship between data diversity and stability.** By varying the number of unique syntax trees (measured via tree-edit distance), the paper identifies three distinct regimes: low-diversity → stable memorization, mid-diversity → high instability, high-diversity → stable rule commitment. This finding is replicated for both hierarchy-inducing and linearity-inducing data (Figure 6), and it connects structural grokking (rule transition) with classic grokking (memorization-to-generalization) under a unified framework.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The secondary past-tense copying task in TI is not described.** The paper mentions in a footnote (Section 4.3) that the original TI dataset contains a secondary past-tense copying task held constant across data mixes, but never specifies whether this secondary task contains center-embedded sentences. If it does, then the "0% center-embedded" condition on the x-axis of Figure 3 (right) is misleading—the model still receives center-embedded exposure through the secondary task, which would explain the near-perfect OOD accuracy on center-embedded test items even at that data point. The red line's flatness would then partly reflect a constant background of center embeddings rather than "model consistently treats center embeddings as hierarchical regardless of data mix." The graded effect on right-branching OOD (green line) would remain valid, but the claim about the red line needs qualification. The paper should either characterize the secondary task's composition or show that removing it does not change the qualitative pattern.

2. **The stability–commitment relationship is correlational, but presented with causal language.** The paper's title for Section 5 is "Training Stabilizes if a Model Commits to a Rule," and the text treats rule commitment as a precondition for stability. However, the evidence—that stable runs have 0% or 100% accuracy and unstable runs occupy intermediate values—is equally compatible with the reverse direction: models that happen to converge to a clean rule are rewarded by low loss and therefore stabilize, while models stuck between attractors never settle. The paper's descriptive finding is valuable either way, but the causal framing is stronger than the evidence warrants. This can be addressed by softening the language (e.g., "stability and rule commitment are tightly coupled").

3. **No direct verification of memorization vs. pattern-specific learning in the low-diversity regime.** The paper claims that low-diversity models "memorize individual syntactic patterns rather than committing to a rule" (Section 6), but does not test whether these models generalize to *unseen vocabulary* within *seen syntax trees*. If a low-diversity model achieves high accuracy on held-out examples with the same tree structure but new words, then it has learned something rule-like (just a tree-specific rather than global rule), which is importantly different from token-sequence memorization. This distinction matters for the paper's overarching narrative about rule commitment vs. memorization, and could be resolved with a simple additional analysis.

4. **The total variation measure is sensitive to the 2K-step checkpoint frequency.** A model oscillating at a faster rate than 2K steps (e.g., switching every 500 steps) would appear as stable under the current TV definition. The paper should acknowledge this limitation or provide a sanity check with finer-grained checkpoints for a subset of runs.

### Trivial

- The abstract states that "models stabilize in their OOD behavior only when they fully commit to either a surface-level linear rule or a hierarchical rule" and then immediately notes "an exception" (memorization with low diversity). The "only" is technically contradicted by the exception. Clarify that the "only" applies to cases where the model is not in the memorization regime, or rephrase for precision.

## Nice-to-Haves

- Add a limitations paragraph explicitly discussing how the findings might (or might not) transfer to natural language, larger models, and other syntactic phenomena. (The Discussion touches on this informally but a dedicated limitations paragraph would strengthen the paper.)
- Include confidence intervals or variability estimates (e.g., standard deviation across seeds) for bar-plot comparisons such as the TV box plots in Figure 4 and the rule commitment ratios in Figure 6.
- The poverty-of-the-stimulus discussion (Section 7) makes claims about "degree 1" vs. "degree 2" data that are not directly tested. An experiment systematically varying embedding depth would substantiate these claims, or the claims should be softened.

## Removed Points

- **Criticism about the QF "Quest Only" condition not isolating center embedding:** The reviewer argues that removing all declaration-copying examples does not isolate center embedding specifically. However, the paper never claims the Quest Only condition isolates center embedding—it uses this condition only to show that declaration-copying examples (of any kind) are *necessary* for hierarchical generalization. The causal evidence about center embedding specifically comes from the separate Center Embed vs. Right Branch comparison, which the reviewer acknowledges is "cleaner." The Quest Only condition serves a different logical role, so this criticism misreads the experimental design.

- **Criticism about the abstract's "only" being severely contradictory:** The exception (memorization) is stated in the very next sentence. The reviewer acknowledges this ("the authors may the exception in the next sentence") but still calls it a flaw. This is a minor imprecision in wording, not a substantive weakness, and has been moved to Trivial above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Characterize the secondary past-tense copying task in TI: describe its sentence types, whether it contains center embeddings, and ideally run a control condition where the secondary task is removed entirely to confirm the graded effect holds.
2. Add a control experiment for the low-diversity regime: test models on held-out examples that share the same syntax tree as training examples but use different vocabulary. This will distinguish token memorization from tree-specific pattern learning.
3. Soften the causal language in Section 5: frame the stability–rule-commitment relationship as a tight coupling rather than assuming directionality.
4. Acknowledge the checkpoint-frequency limitation of the TV measure in the main text.

## Score and Decision

The paper's controlled experiments, careful metrics, and cross-task validation make a genuine contribution to understanding how data composition drives OOD generalization and training stability in grammar learning. The weaknesses are limited to missing details and framing overreach—none threaten the core findings. With straightforward clarifications (characterizing the TI secondary task, softening causal claims, verifying memorization vs. tree-specific learning), the paper would be very strong.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>