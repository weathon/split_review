Now I have enough calibration anchors. Let me write the final consolidated review.

## Summary

This paper studies how training data composition—specifically syntactic complexity (center-embedded vs. right-branching sentences) and syntactic diversity (number of unique syntax trees)—determines whether language models learn hierarchical syntactic rules or fall back on linear heuristics, and how these properties govern training stability and seed-to-seed variation. Using controlled experiments on question formation and tense inflection tasks with synthetic CFG-generated data, the authors find that (1) center-embedded sentences causally drive hierarchical generalization, (2) OOD behavior stabilizes only when a model commits to either a linear or hierarchical rule, and (3) data diversity exhibits an inverse U-shaped relationship with training stability, revealing three regimes: memorization (low diversity), instability (mid diversity), and rule commitment (high diversity).

## Strengths

- **Causal identification of center-embedded sentences as drivers of hierarchical generalization (Section 4.2, Figure 3 left).** The controlled comparison between training only on center-embedded declarations vs. only on right-branching declarations, while keeping the question-formation samples identical, cleanly isolates the data property that induces hierarchical generalization. This finding is replicated across two distinct grammatical tasks (QF and TI, Sections 4.2–4.3), demonstrating it is not task-specific.

- **Demonstration that heterogeneous data mixtures produce bimodal OOD outcomes linked to training stability (Section 5.2, Figure 4).** The paper shows that mixing hierarchy-inducing and linearity-inducing data leads to unstable training dynamics, and that the runs that do stabilize cluster at extreme OOD accuracies (0% or 100%). This ties seed-to-seed variation to rule competition in the data, a concrete mechanism for observed inconsistency across random seeds that prior work noted but did not explain.

- **Two-task validation across distinct grammatical phenomena.** The key finding (center embeddings → hierarchical rule) is established in both the question formation task and the tense inflection task, strengthening the claim that this reflects a general property of grammar learning rather than a quirk of one task design.

- **Conceptual framework organizing three training regimes along two data axes.** The paper's framing of data composition in terms of complexity (center-embedded vs. right-branching) and diversity (unique syntax trees) provides a coherent picture of when a model memorizes, competes between rules, or commits to a rule—unifying phenomena from classic grokking and structural grokking under a single perspective.

## Weaknesses

### Major

- **The claim that "stable models always achieve exactly 0% or 100% OOD accuracy" lacks statistical support (Section 5.2).** This is a strong, central claim in the paper, but it is supported only by a visual reference to Figure 4. The paper provides no histogram, kernel density plot, or table of OOD accuracy values for stable runs; no threshold is given for categorizing runs as "stable" (total variation is introduced as a continuous measure in Section 5.1, but the binary stable/unstable split is never operationalized); and no statistical test for bimodality (e.g., Hartigan's dip test) is reported. Without this, the claim risks being a qualitative observation rather than an established result. The authors should report the complete distribution (e.g., a table of mean, min, max accuracy across data mixes along with the proportion of runs in each mode) and demonstrate robustness to the choice of TV threshold.

### Minor

- **The stable/unstable categorization is not operationalized with a threshold.** Total variation (TV) is defined as a continuous measure (Section 5.1), but the paper then makes categorical claims about "stable models." No cutoff, clustering method, or sensitivity analysis is provided. This makes it unclear how runs are partitioned and whether the conclusions would shift under a different threshold choice.

- **The data diversity experiments (Section 6) conflate diversity (number of unique syntax trees) with repetition frequency.** Total dataset size is fixed, so varying the number of unique trees necessarily changes how many times each tree appears. The observed inverse U-shaped pattern could be partly driven by repetition effects (memorization under many repeats) rather than syntactic diversity per se. While this does not invalidate the finding—the repetition mechanism is closely related—the paper's interpretation that "insufficient diversity prevents rule commitment" would be strengthened by an experiment that holds the number of unique trees constant while varying repetition, or adds filler sentences to control for this confound.

- **The number of unique syntax trees per diversity level is not specified (Section 6).** The paper describes diversity levels as "low," "mid," and "high" but does not report the actual number of unique trees used (e.g., 1, 5, 10, 50, ...). This hampers reproducibility and makes it impossible for readers to assess whether the diversity labels are justified or to compare across conditions.

- **The inverse U-shaped relationship is presented only as a qualitative description of Figure 5.** No tabular means/variances of total variation across diversity levels are reported, and no statistical test for a quadratic trend is performed. The "rule commitment ratio" uses arbitrary thresholds (>95% or <5%) without a sensitivity analysis.

### Trivial

- None.

## Nice-to-Haves

- A histogram or density plot of OOD accuracy for stable runs across all data mixes, with a dip test or similar bimodality test.
- An additional control in the QF experiments that adds filler sentences to match the total number of examples in the Quest Only condition, to fully rule out the dataset-size confound.
- Explicit quantification of diversity levels (number of unique syntax trees per condition) in Section 6.

## Removed Points

- **Abstract "contradiction" about memorization exception**: The reviewer claimed the abstract's claim that models stabilize only when committing to a rule is contradicted by the later finding about memorization. In fact, the abstract explicitly acknowledges this exception (line 10: "We also identify an exception to the relationship between stability and generalization: models which memorize... can overfit stably"). The criticism is based on a misreading.
- **Quest Only dataset size confound as a central flaw**: The reviewer notes that Quest Only has fewer examples than Center embed/Right branch. The paper's key comparison is Center embed vs. Right branch, which is size-controlled. Quest Only is an ablation to show declarations are necessary—the size confound does not threaten the main result. Mentioned in Nice-to-Haves above.
- **Discussion speculation about poverty of the stimulus**: The reviewer criticizes the Discussion for speculation beyond what experiments demonstrate. Discussion sections are the standard place for interpretation and speculation; this is scope creep.
- **Missing hyperparameters/reproducibility details**: The paper states hyperparameters in Section 3.3 (12M/4-layer transformer, Adam, LR 1e-4, 300K steps, 50 seeds). This is standard and sufficient.

## Novel Insights

None beyond the paper's own contributions. The reviews surface that the paper's secondary claims (bimodality of stable runs, inverse U-shaped diversity-stability relationship) are less well-supported than the core causal finding about center embeddings, but this is a gap in evidence strength rather than a novel observation.

## Suggestions

1. **Provide statistical evidence for the bimodality claim.** Report a histogram or density plot of OOD accuracy for stable runs (with a clear TV threshold stated), and run a dip test or similar. Show that the result is robust across reasonable TV thresholds.
2. **Specify the number of unique syntax trees used for each diversity level** in Section 6. Report a table of mean/median TV and rule commitment ratios per level, not just a qualitative figure description.
3. **Disentangle diversity from repetition** by running an additional experiment that holds the number of unique trees constant and varies repetition (or vice versa), with filler sentences to keep total size fixed.
4. **Define the stable/unstable threshold** explicitly. State the TV cutoff used and show sensitivity analysis across a range of cutoffs.

## Score and Decision

I calibrate this score against the following anchor papers (all from the deepreview_13k_calibration directory):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `TvfkSyHZRA.md` (Grokking at the Edge) | 7.0 | Stronger: has a well-supported mechanism + proposed solutions; more rigorous evidence for its central claims |
| `H98CVcX1eh.md` (Discovering modular solutions) | 6.5 | Comparable contribution level: both have theoretical/empirical contributions but clarity issues; similar pattern of interesting claims with some evidential gaps |
| `aWLQTbfFgV.md` (Training NNs as Recognizers) | 6.25 | Stronger empirical rigor: thorough methodology, clear evidence for claims; our paper is weaker on evidence support for secondary claims |
| `d8w0pmvXbZ.md` (Small-scale proxies) | 8.0 | Much stronger: thorough, well-executed experiments, clear practical implications |
| `79ZkWgY2FI.md` (Small-to-Large Generalization) | 5.25 | Similar pattern: interesting findings but some claims have weak evidential support; our paper has stronger causal identification for its main claim |
| `eRkNNQRppH.md` (FOL scaling) | 3.5 | Weaker: vague phase definitions, insufficient evidence for claims, post-hoc interpretation of noisy curves; our paper has cleaner experimental design |
| `xlxDTVAbNM.md` (Lowering Data Diversity) | 3.5 | Weaker: synthetic-only experiments, unconvincing claims about practical utility, no real-world validation |

The paper makes a genuine and well-supported contribution (center embeddings causally drive hierarchical generalization) through controlled experiments validated across two tasks. However, the paper's strongest secondary claims—that stable models always cluster at exactly 0%/100% OOD accuracy and that diversity has an inverse U-shaped relationship with stability—are presented with insufficient statistical evidence and rely on qualitative figure descriptions without tabular support, thresholds, or statistical tests. The diversity experiments also conflate syntactic diversity with repetition frequency. The paper's overall contribution is meaningful but its evidential footing for several central claims is incomplete, placing it between the more rigorous accepted papers (6–7 range) and the weakly-supported rejected papers (3–4 range).

MY FINAL SCORE: 5.5
MY FINAL DECISION: Reject