## Summary

This paper makes three interconnected contributions: (i) a unified Heterophilous Message-Passing (HTMP) framework that decomposes 12+ existing HTGNNs into shared components (neighborhood indicators, aggregation guidance, combine, and fuse functions); (ii) an empirical analysis revealing that message passing succeeds on heterophilous graphs because it implicitly enhances the discriminability of the compatibility matrix (CM); and (iii) CMGNN, a method that explicitly constructs supplementary neighborhoods from class prototypes and applies a discrimination loss to improve CM discriminability, validated on a cleaned benchmark of 10 datasets against 17 baselines.

## Strengths

- **Table 1 systematically unifies diverse HTGNNs into a common framework.** The paper decomposes MixHop, H2GCN, GPR-GNN, ACM-GCN, OrderedGNN, and others into the same HTMP components, providing a structured design space that was previously fragmented. This enables direct comparison and principled design of new methods.
- **Figure 2 provides direct empirical evidence that HTGNNs enhance CM discriminability.** The visualizations of CMs before and after applying ACM-GCN and GPR-GNN on Amazon-Ratings show that these methods produce more distinguishable rows compared to the raw graph's CM, directly supporting the paper's central theoretical explanation.
- **Table 4 demonstrates CMGNN's mechanism-based advantage on low-degree nodes.** By partitioning test nodes by degree quintiles, the paper shows CMGNN performs best on the lowest-degree 20% of nodes—directly validating the diagnosis that low-degree nodes suffer from incomplete/noisy semantic neighborhoods and that CMGNN's supplementary neighborhoods address this specific failure mode.
- **New benchmark systematically addresses known dataset flaws.** The paper explicitly identifies and avoids data leakage in Chameleon/Squirrel (Platonov et al., 2023) and newly discovered inconsistencies in Citeseer and Cora, creating a more reliable evaluation foundation.
- **Ablation study cleanly isolates the two design components.** Table 3 separately ablates supplementary messages (SM) and discrimination loss (DL), showing their contributions vary interpretably across datasets. This disciplined ablation strengthens confidence that both components serve their intended roles.

## Weaknesses

### Fatal
None.

### Major

- **"Theorem 1" is not a theorem and lacks formal grounding.** Line 97 states: "Theorem 1. The discriminability among the representations learned by the message-passing mechanism is positively correlated with the discriminability among classes in the compatibility matrix." However, the paper provides no formal definition of "discriminability," no mathematical proof, and no derivation—only qualitative visualizations and informal reasoning (lines 99–104). The paper also lists both "Observation 1" (line 93) and "Theorem 1" (line 97) in the same section, blurring the line between empirical observation and formal claim. Calling this a theorem is misleading; it should be presented as a conjecture or observation backed by the empirical evidence the paper actually has. This does not invalidate the paper's contributions, but it over-promises rigor that is not delivered.

- **The 48/32/20 train/val/test split lacks adequate justification.** Line 230 states the split is used "for consistency with existing methods," but this is ambiguous and not well-substantiated. 48% training nodes is substantially larger than the low-label regimes typically studied in heterophilous GNN literature. While all methods are compared under the *same* protocol (so internal comparisons are fair), the choice affects external validity: results in high-label regimes may not generalize to the low-label settings where heterophily is most challenging. The paper should either (a) justify why 48% training is the appropriate protocol for this new benchmark, or (b) show that relative rankings are robust to training ratio.

### Minor

- **Cold-start behavior of CM estimation is not analyzed.** The paper initializes predictions with uniform class probabilities (line 195: "nodes have the same probabilities belonging to each class"). At initialization, the supplementary aggregation guidance \(B^{sup} = \hat{C}\hat{M}\) with uniform \(\hat{C}\) collapses to a constant vector per node, providing no class-discriminative signal. The paper does not analyze how the method escapes this uniform fixed point or how sensitive results are to pseudo-label quality in early training. While the cross-entropy loss on training labels provides some gradient signal, a convergence analysis or sensitivity study would strengthen the paper.

- **Lack of quantitative measure for "discriminability."** The paper repeatedly invokes "discriminability among classes in the CM" as its core concept (Observations 1–2, Theorem 1, the CMGNN design), but never formalizes it with a concrete metric. A quantitative measure (e.g., row-wise cosine similarity, minimum margin between rows, or spectral gap) would allow the authors to directly measure CM enhancement and correlate it with accuracy—transforming the current qualitative visual argument into a rigorous one.

- **Potential negative effects of the discrimination loss are not discussed.** The discrimination loss (Eq. 11) penalizes similarity between different classes' desired neighborhood messages. If two classes genuinely have similar connection patterns in the graph (i.e., their rows in the true CM are similar), forcing their desired neighborhood messages apart could introduce spurious information. The paper does not discuss this scenario.

- **Degree weighting function thresholds are ad-hoc.** The weighting function (Eq. 8) uses fixed thresholds \(K\) and \(3K\) that are "empirically chosen" (line 153). Since \(K\) (number of classes) varies across datasets, the function's behavior changes across settings, and no sensitivity analysis is provided.

### Trivial

- **Notation inconsistency in Equation 14.** The equation uses \(\prod\) (product symbol) for what the text (line 187) defines as concatenation (denoted by \(\parallel\)). The equation should use \(\parallel\) to match the definition.

## Nice-to-Haves

- Sensitivity analysis for the training split ratio (e.g., compare results under 48/32/20 vs. a lower-label regime) would strengthen claims about generalizability.
- A formal discriminability measure (as noted above under Minor weaknesses) would substantially improve the paper's analytical rigor.
- Statistical significance testing (e.g., paired t-tests) across the 10-dataset × 18-method comparison matrix would help assess whether improvements are reliable.
- Complexity analysis (flops, memory, runtime) for the proposed method, which adds \(K\) virtual nodes and a pseudo-label estimation loop.
- Sensitivity analysis for key hyperparameters: the degree weighting thresholds (\(K\), \(3K\)), discrimination loss weight \(\lambda\), and the number of supplementary neighborhoods.

## Removed Points

These points from the input reviews are excluded with brief justification:

- **"Abstract framing promises causal explanation but evidence is correlational"**: The paper's evidence (Figure 2 visualizations, ablation, degree-based analysis) is both causal and correlational; this critique is too sweeping and not anchored to a specific failure.
- **"Section 3 should discuss methods that do not fit HTMP"**: Scope creep—the paper is not required to exhaustively enumerate what does not fit.
- **"Synthetic experiments not shown in main paper"**: The text mentioning synthetic experiments (line 89) is parser-garbled; results likely reside in the stripped appendix. Per instructions, parser artifacts are not author errors.
- **"No quantitative analysis of incomplete/noisy semantic neighborhoods in the benchmark datasets"**: This is a generic "area of concern" sweep, not a specific identified problem. The paper uses this concept as motivation and validates it via Table 4 (low-degree node performance).
- **"Brief limitations section (two sentences)"**: Minor but valid; folded into Minor weaknesses as part of broader set.
- **"No statistical significance testing"**: Generic request not standardly required for tabular benchmark comparisons of this scale; moved to Nice-to-Haves.
- **Strength Finder statements that are generic or conflict**: All five listed strengths are concrete and evidence-anchored; none removed.
- **Formatting nitpicks and claims about "non-standard datasets"**: Removed per formatting rule. All cited datasets exist and are released.

## Novel Insights

None beyond the paper's own contributions. However, a notable synthesis emerges from the two reviews read together: the paper's strongest evidence for its central claim (that message passing succeeds by enhancing CM discriminability) comes not from "Theorem 1" but from the convergence of two independent empirical results—Figure 2's CM visualizations showing that existing HTGNNs produce more separable CMs, and Table 4's degree-based analysis showing that CMGNN's advantage is concentrated on precisely the nodes the theory predicts (low-degree nodes with incomplete semantic neighborhoods). These two pieces of evidence, combined, constitute a stronger argument than either alone. The "Theorem 1" labeling is unnecessary and distracts from this genuinely compelling empirical chain.

## Suggestions

1. Rename "Theorem 1" to "Observation 3" or "Conjecture 1" to accurately reflect its status. Better yet, define a quantitative discriminability measure and compute it for the methods in Figure 2 to provide rigorous numerical support.
2. Add a brief discussion justifying the 48/32/20 split: either cite the protocol used in the source papers for the new datasets (e.g., Platonov et al., 2023), or acknowledge the difference from prior practice and argue why this split is appropriate.
3. Add an analysis (even brief) of how the CM estimate evolves during training, addressing the cold-start concern.
4. Fix the notation in Eq. 14: replace \(\prod\) with \(\parallel\) to match the text.
5. Include a sentence in the limitations section acknowledging the circular dependency between pseudo-labels and CM estimation, and noting that future work could analyze initialization sensitivity.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>