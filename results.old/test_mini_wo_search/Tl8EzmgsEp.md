Now I have a thorough understanding of the paper. Let me construct the final consolidated review, carefully verifying each claim against the paper text.

---

## Summary

This paper investigates the look-ahead capabilities of the Leela Chess Zero policy network, extending prior work by Jenner et al. (2024). It introduces a puzzle set notation for disentangling different board-square configurations, provides probing and activation patching evidence that the model encodes and causally relies on information about board states up to seven moves ahead, shows that this behavior is highly context-dependent across puzzle types, and presents evidence that the model considers alternative move sequences. The central contributions are the extension to longer-term (5th and 7th move) look-ahead, the context-dependence characterization, and the alternative-move analysis.

## Strengths

1. **Demonstration of look-ahead beyond the immediately subsequent moves.** Section 3 and Figure 3 show probing accuracy for the model's residual stream on puzzle set 1123456, with accuracy degrading across distant moves but remaining non-negligible for the 7th move compared to a random model. This provides direct evidence that information about board states several moves ahead is encoded in the model's internal representations.

2. **Context-dependent behavior across puzzle sets.** Section 3 systematically shows that patching and ablation effects vary strongly by puzzle set (e.g., attention head L12H12 is most important for set 112 but weaker in other sets; checkmate vs. non-checkmate positions produce distinct patterns, Figures 4 and 5). This suggests the model does not apply a uniform look-ahead strategy but tailors its processing to the tactical structure of the position.

3. **Evidence of considering alternative move sequences.** Section 3 and Figure 6 show that patching alternative first or third move squares (i.e., board squares from a secondary branch of play) consistently improves the model's odds of choosing the correct branch. This provides a novel behavioral signature of multi-branch evaluation beyond the principal variation.

4. **Time-insensitive pattern mechanisms in attention head L12H12.** Section 3 reports that the patterns AAC, ABC, and ACC that L12H12 responds to appear to generalize across move triples (1-2-3, 3-4-5, 5-6-7), suggesting the head has learned pattern-matching mechanisms that are not timing-specific. This is a concrete mechanistic finding.

5. **Novel puzzle set notation (Section 2.4).** The sequential labeling scheme (e.g., 1123456) provides a systematic way to categorize puzzles by the geometry of their move squares, enabling analysis of longer-range look-ahead without conflating different scenarios. This is a practical methodological contribution.

## Weaknesses

### Fatal
None.

### Major

1. **Lack of statistical quantification for several key results.** Probing accuracy for the 7th move is described only as "considerably low, but still non-negligible" with no exact accuracy numbers, confidence intervals, or baselines beyond "a random model" (Figure 3 caption, lines 80–83). The 7th-move patching results that would parallel the 5th-move analysis of Figure 2 are not shown in the main text at all — they are deferred to the appendix. For the 5th-move patching, effect sizes are described qualitatively ("most salient for set 11223, while not being very significant for set 11233") without reporting the actual log-odds values or the number of puzzles per set beyond the threshold of "more than 50" (line 84). This makes it difficult to assess the reliability and magnitude of the reported effects.

2. **Planning vs. pattern matching is not meaningfully distinguished.** The paper acknowledges pattern matching as a possibility (line 104: "the model has learned some general pattern-matching mechanisms across time"), and the introduction frames planning vs. pattern matching as an open question, but the paper never attempts to distinguish whether its observations reflect the model evaluating future contingencies versus recognizing forced continuation patterns from its training data. The puzzles are selected sequences where the optimal move leads to a deterministic continuation; a model that has learned statistical correlations between current position and typical future squares in such puzzles would also encode and be causally dependent on those future squares. Since the paper's core claim is about "look-ahead behavior," a term that blurs this distinction, the lack of any experimental design to separate these explanations is a significant gap.

3. **Use of a finetuned model without adequate justification.** The paper states only: "Due to peculiarities of this particular model, previously discussed in Jenner et al. (2024), we use a finetuned version of the model, trained and used by Jenner et al. (2024)" (line 35). No explanation of what these peculiarities are, how finetuning addresses them, or how finetuning changes the model's behavior is provided in the paper. Since all subsequent results are obtained on this finetuned variant, it is unclear whether the findings generalize to the original Leela model or to chess neural networks more broadly. A brief summary of the relevant peculiarities and a validation check (e.g., reproducing a subset of results on the original model) would substantially strengthen the paper.

### Minor

1. **The "backward in time" information flow claim relies heavily on prior work for the core interpretation.** The paper inherits the claim that L12H12 "moves information backward in time" from Jenner et al. (2024) and extends it to 5th/7th moves. The evidence in this paper for the backward-in-time direction is ablation-based (Figure 5 and referenced appendices), which establishes causal importance but not direction of information flow. No attention pattern visualizations or quantitative attention analyses are shown in the main text — these are deferred entirely to appendices. While the paper uses appropriately cautious language ("appears to," "we hypothesize that"), the main text's conclusions are presented with more confidence than the evidence shown in it supports.

2. **The alternative moves analysis lacks detail on branch selection and corrupted board construction.** The paper states that puzzles are selected where "the Leela model assigns a probability around 1/2 of choosing each of the two move branches" and that corrupted boards are "compatible with both branches A and B" (lines 119–121), but it does not specify the threshold for "around 1/2," how the two branches are identified, or what constitutes a "compatible" corrupted board. The effect sizes in Figure 6 appear modest relative to the displayed standard deviations, and no significance testing is reported.

3. **The evidence that 7th-move processing uses "similar concrete internal mechanisms" as 3rd and 5th moves is extrapolated from pattern matching on 5th-move data.** The paper shows AAC/ABC/ACC patterns for 5th-move patching (Figure 2) and hypothesizes they apply to 7th moves based on Appendix results, but the strong claim of "similar concrete internal mechanisms" in the conclusion (line 143) is not directly evidenced for 7th moves in the main text.

### Trivial

None.

## Nice-to-Haves

- A dedicated limitations section acknowledging: the analysis is restricted to Lichess puzzles (not general chess positions); the finetuned model may differ from the standard Leela; the causal importance of future-move squares is consistent with look-ahead but also with learned correlations; the 2.2k 7-move dataset is small once subdivided into puzzle-set categories.
- More probing baselines: comparing against a model with permuted labels or a shallow classifier on raw board input, rather than only against a random-weight model.
- Reporting per-puzzle-set sample sizes for all analyses, especially given the "more than 50 puzzles" threshold and the many categories.
- Explicit statistical tests (e.g., permutation tests or paired comparisons) for the alternative-move patching results.

## Removed Points

These points from the input reviews were checked against the paper and removed for the following reasons:

- **"Starting squares could carry information about piece identity... ignoring them limits the analysis."** — The paper explicitly addresses this (lines 77–78), citing its own results and prior work showing that starting move squares "do not seem to play a significant direct role in the look-ahead behavior." Removed because the paper has already justified this choice.
- **"Missing attention pattern analysis in the main text" framed as a structural issue.** — Kept in Minor (point 1) but softened: the paper references appendices for this analysis, and appendices exist in the original submission (the parser strips them). The weakness is that the main text presents conclusions that depend on deferred evidence, not that the analysis is missing entirely.
- **"The paper lacks a Limitations section"** — Moved to Nice-to-Haves. Many papers do not have explicit limitations sections; this is a presentation preference, not a substantive weakness.
- **"The paper does not report sample sizes per set"** — Partially addressed by the "more than 50 puzzles" threshold (line 84). Kept as a note in Nice-to-Haves rather than a standalone weakness.
- **Generic criticisms about "lack of rigor" and "fails to discuss important limitations"** — Removed as they are one-size-fits-all statements without specific anchors. Specific instantiations (statistical quantification, finetuned model justification) are retained as Major/Minor weaknesses above.
- **Strength Finder strengths about the problem being "important" or the paper "addressing an important question"** — Removed as generic/superficial. Concrete strengths (1–5 above) are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews identify important limitations but do not introduce a novel interpretation of the paper's findings beyond what the authors themselves present.

## Suggestions

1. **Report exact probing accuracy numbers for each future move (1st through 7th) with confidence intervals**, and compare against a meaningful baseline (e.g., a model with permuted labels or a board-state-only classifier) rather than only a random-weight model.
2. **Include 7th-move patching results (analogous to Figure 2 for 5th moves) in the main text**, or if the effects are too weak, explicitly state the non-result and its implications for the model's look-ahead horizon.
3. **Address the planning vs. pattern matching confound**: analyze whether the model's sensitivity to future-move squares differs between forced sequences (e.g., checkmate puzzles with deterministic continuations) versus positions where the opponent has plausible alternatives. If the model's "look-ahead" breaks down when the continuation is not forced, this favors the pattern-matching interpretation.
4. **Provide a brief explanation of the finetuning peculiarities** (or at minimum a summary) in the current paper, and validate that a subset of key results replicates on the original unfinetuned model.
5. **Report per-puzzle-set sample sizes** for all analyses, and consider excluding sets with too few examples from strong conclusions.
6. **Add statistical significance tests** (e.g., permutation tests) for the alternative-move patching results in Figure 6, given the modest effect sizes and visible variance.

## Score and Decision

**Originality**: The paper makes incremental but useful extensions to Jenner et al. (2024) — the puzzle set notation, alternative-move analysis, and extension to 5th/7th moves are novel, though the core approach is inherited from prior work.

**Importance of research question**: Understanding whether neural networks learn genuine look-ahead or pattern matching is an important question for mechanistic interpretability and AI safety.

**Claims supported**: The central claims are partially supported. The evidence for 5th-move look-ahead is reasonable; the 7th-move evidence is thin and qualitatively described; the context-dependence claim is well-supported; the alternative-move analysis is interesting but underspecified.

**Soundness of experiments**: The methodology (probing, patching, ablation) is standard and appropriate. The main weakness is the lack of statistical quantification and the reliance on a finetuned model without adequate validation.

**Clarity of writing**: Generally clear, though the Results section jumps between claims and figure references without always giving precise numbers. The puzzle set notation, once explained, is effective.

**Value to the research community**: Moderately valuable as an extension of prior work; the notation and alternative-move methodology may be reusable.

<score>4.5</score>
<decision>Reject</decision>