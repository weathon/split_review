Now I have a good understanding of the calibration landscape. Let me produce the final review.

## Summary

This paper investigates the look-ahead behavior of the Leela Chess Zero policy network, extending the work of Jenner et al. (2024). Using activation patching, probing, and ablation, the authors analyze whether the model encodes information about future board states beyond the immediate next move. They present evidence that the model can process information about board states up to seven moves ahead (with decreasing accuracy), that this behavior is highly context-dependent based on the specific chess position type, that similar internal mechanisms (particularly attention head L12H12) handle look-ahead across different time horizons, and that the model considers multiple alternative move sequences rather than a single line of play.

## Strengths

- **Complementary interpretability methodology**: The paper triangulates findings using three techniques—activation patching (causal necessity), probing (encoded information), and ablation (fine-grained head roles). This is a principled approach, and the paper explicitly discusses cases where these techniques provide different information (e.g., probing reveals opponent-move encoding not captured by patching).

- **Novel puzzle-set notation**: The introduction of the labeling scheme (e.g., 112XY) that disentangles move-square relationships is a practical methodological contribution. It enables the fine-grained comparisons that underpin the core results and is likely reusable by future work building on this line of research.

- **Evidence of alternative-move consideration**: Figure 6 provides concrete causal evidence that corrupting the alternative first-move square increases the log odds of the model choosing the main branch's first move, and vice versa. This goes beyond prior work and directly supports the claim that the model weighs multiple sequences.

- **Identification of time-insensitive pattern matching in L12H12**: The demonstration that attention head L12H12 responds to patterns AAC, ABC, and ACC regardless of whether these patterns apply to moves 1-2-3, 3-4-5, or 5-6-7 is a specific and interesting mechanistic finding.

- **Clear writing and organization**: The paper is well-structured, the puzzle-set notation is clearly explained, and the connection between experimental results and conclusions is generally transparent.

## Weaknesses

### Fatal

None.

### Major

- **Weak evidence for 7-move look-ahead**: The paper's strongest claim—that the model looks ahead to the 7th move—rests primarily on probing results described as having "considerably low" accuracy that is "still non-negligible when compared with the probe's accuracy for a random model." No actual accuracy numbers, no confidence intervals for the probe accuracy, and no rigorous baseline comparison are provided in the main text. Given that this is a headline contribution, the lack of quantitative detail is a significant gap. Activation-patching results for the 7th move are also relegated to appendices (which are not present in the submitted paper text), so the main paper does not provide sufficient evidence for this claim standing alone.

- **Limited scope of the alternative-move analysis**: The alternative-move results are based on only 609 puzzles selected for a very specific condition (50/50 probability split between two branches). This is acknowledged but remains a limitation. More importantly, the analysis shows that corrupting alternative branch squares affects the model's confidence, but this is consistent with the model having learned which branches are correlated with the optimal move through training patterns, not necessarily with the model *simultaneously simulating* multiple lines. The paper does not design experiments to distinguish these interpretations.

- **No statistical rigor**: The paper does not report statistical significance tests for any of its key comparisons. The reported confidence intervals (50% and 90%) are described but their computation is not explained, and many figures (Figure 4 heatmap, Figure 6) lack error bars or statistical tests. Given that the results rely on sometimes small differences between conditions, this is a methodological shortcoming.

- **Incremental contribution relative to Jenner et al. (2024)**: The paper directly extends Jenner et al. (2024) by analyzing longer move horizons and adding an alternative-move experiment. While extension work is valuable, the core techniques, the model, and many of the puzzle sets are inherited without substantial methodological novelty. The paper's contribution is primarily empirical—showing these phenomena exist at longer horizons—rather than providing new mechanistic understanding or new methods.

### Minor

- **Probing results lack quantitative baselines**: The probing accuracy for future moves is described qualitatively ("non-negligible") without reporting the actual accuracy values or the random-baseline accuracy. A reader cannot assess how meaningful the 7th-move decoding is without these numbers.

- **Attention head analysis is post-hoc and descriptive**: The identified roles of L12H17, L13H3, L11H10, and L11H13 are described qualitatively (e.g., "appears to move information 'backward in time'"), without hypothesis testing or controls for multiple comparisons across the many attention heads examined. This limits the reliability of the specific functional attributions.

- **No code release**: The reproducibility statement says code "will be made available upon publication" but is not provided now, making independent verification of the results impossible during review.

### Trivial

- Figures referenced in the text (e.g., "see Fig. 2" in line 84, "see Figs." in line 98) appear to reference subfigures or panels that are not labeled in the text as they appear in the provided file.

## Nice-to-Haves

- A comparison of the model's behavior to a simpler baseline (e.g., whether a linear heuristic based on board features could produce similar probing/patching results) would strengthen the claim that the observed effects are nontrivial.
- An analysis of whether the identified attention heads actually implement sequential processing (e.g., through path patching or circuit analysis) rather than just correlational evidence via ablation.
- Testing the alternative-move analysis on a broader range of positions beyond the 50/50 split condition.

## Removed Points

*The harsh critic's claim that "the paper consistently uses language implying genuine planning" and that experiments do not distinguish pattern-matching from sequential simulation* — The paper repeatedly uses the measured term "look-ahead behavior" rather than "planning" or "simulation," and explicitly discusses pattern-matching mechanisms (e.g., "the model has learned some general pattern-matching mechanisms across time rather than timing-specific heuristics"). This criticism overreads the paper's claims.

*The harsh critic's criticism that the L12H12 analysis "lacks statistical controls for multiple comparisons"* — While the analysis is descriptive, this is standard for mechanistic interpretability studies at this level of granularity. The paper does not claim statistical significance for the specific head attributions but presents them as observations. I demoted this from the harsh critic's framing to a minor weakness above.

*The harsh critic's statement that "the 7th move look-ahead is supported only by low-accuracy probing (no rigorous baseline comparison provided)"* — This is a valid concern and is kept as a major weakness above, but the claim that results are "relegated to appendices" is likely a parser issue (appendices stripped). I kept the core concern.

*Strength Finder's generic strengths about "addressing an important problem" and "value to the research community"* — These are generic and do not provide specific evidence; removed.

*Strength Finder's claim about "context-dependence demonstrated through puzzle-set-specific patching"* — This is merged into the third Strength (kept but reworded). The core evidence is valid.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report quantitative probing results**: Provide the actual accuracy values for probing at each move horizon (1st through 7th), along with random-baseline accuracy and confidence intervals. This is essential for the reader to assess the strength of the 7th-move evidence.

2. **Add statistical significance testing**: For key comparisons (e.g., the varying importance of 5th-move patching across puzzle sets, or the effect of alternative-move patching), report p-values or effect sizes to distinguish signal from noise.

3. **Expand the alternative-move analysis**: Test a broader range of positions beyond the 50/50 split condition, or at minimum discuss whether the results are expected to generalize.

4. **Tighten claims about "look-ahead"**: The paper's evidence primarily shows that future-move *squares* are encoded and causally relevant. This is consistent with pattern-matching as well as sequential planning. A brief discussion of this distinction would strengthen the paper's intellectual honesty.

## Score and Decision

My bracket after the initial pass was 4.5–5.5. After narrowing against calibration anchors:

- **"Interpreting Emergent Planning" (8.0)**: Much stronger—has a clear hypothesis-testing framework, stronger causal evidence, and a novel methodological approach. Our paper is substantially weaker.
- **"Human-Aligned Chess" (6.8)**: A larger, more complete contribution with user studies and a novel model. Our paper is somewhat weaker.
- **"Fine-Tuning Enhances Existing Mechanisms" (5.67)**: Comparable rigor and presentation, but has a novel method (CMAP). Our paper is slightly weaker.
- **"Discovering Influential Neuron Path" (6.0)**: Stronger novelty and more thorough experiments. Our paper is weaker.
- **"Mechanistic Unlearning" (5.25)**: Mixed-quality paper with strong empirical results but poor presentation. Our paper is better-presented but has weaker results. Roughly comparable.
- **"Decompose the model" (5.0)**: Comparable—both are solid empirical contributions with clear methodology but incremental novelty. Similar overall quality.
- **"Disentangling the QiGan" (4.25)**: Similar domain (game AI interpretability), but our paper is clearer and better executed. Our paper is stronger.

The paper under review is a well-written, competent empirical extension of prior work. It makes incremental but real contributions. The main factors constraining the score are: (1) the weak quantitative evidence for the headline claim about 7-move look-ahead, (2) the limited scope of the alternative-move analysis, and (3) the lack of statistical rigor. The paper does not have fatal flaws, and its claims are appropriately scoped. It sits alongside papers in the 5.0 range.

**Final score: 5.0**

**Decision: Reject**

(Note: In this scoring convention, a score of 5.0 corresponds to a borderline paper—solid contribution but with clear limitations that make acceptance without major revision difficult. The paper would benefit from addressing the major weaknesses above, particularly providing quantitative probing results and expanding the alternative-move analysis.)

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>