Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper demonstrates that current evaluation datasets for membership inference (MI) attacks on foundation models suffer from systematic distribution shifts between members and non-members across all eight examined benchmarks (spanning LLMs and diffusion models). The authors design simple "blind" attacks (date thresholding, bag-of-words classifiers, greedy n-gram selection) that completely ignore the target model yet outperform all reported state-of-the-art MI attacks on every dataset — often by dramatic margins (e.g., 94.4% vs. 43.2% TPR@5%FPR on WikiMIA). The paper concludes that existing evaluations measure distribution differences rather than actual membership leakage, and proposes using datasets with proper random train-test splits (the Pile, DataComp, DataComp-LM) as a path forward.

## Strengths

- **Systematic evidence across 8 diverse MI datasets**: The paper analyzes all major published MI evaluation benchmarks for foundation models (text and vision) and finds distribution shifts in every one. This breadth — temporal shifts, replication biases, distinguishable tails — makes the critique definitive rather than anecdotal.

- **Blind attacks dramatically outperform SOTA MI attacks on 6 of 8 datasets**: The margins are enormous on WikiMIA (94.4% vs. 43.2% TPR@5%FPR), Multi-Webdata (83.5% vs. 40.3% TPR@1%FPR), Gutenberg (59.6% vs. 18.8% TPR@1%FPR), BookMIA, LAION-MI, and ArXiv-1 month. This directly proves that current evaluations cannot measure true membership leakage.

- **Simplicity of blind attacks underscores the severity of the flaw**: The attacks use trivial features — regex date extraction, bag-of-words classifiers, character-level n-grams — and still beat sophisticated model-based attacks. This makes the point concrete and hard to dismiss as a methodological edge case.

- **Per-dataset case studies with detailed root-cause analysis**: For each dataset, the paper explains the specific source of distribution shift (e.g., temporal cutoff, non-English translation artifacts, metadata formatting changes) and designs a tailored blind attack. The ablation on Gutenberg (removing formatting still yields 16.6% TPR@1%FPR) is particularly thorough.

- **Constructive path forward**: Section 5 identifies concrete alternatives (the Pile, DataComp, DataComp-LM) with available pool sizes and pretrained models, giving the community a clear direction for fixing the evaluation methodology rather than just critiquing it.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Marginal margins on two temporal datasets with no confidence intervals**: On Temporal Wiki (AUC 79.9% vs. 79.6%, +0.3pp) and Temporal arXiv (AUC 75.6% vs. 74.5%, +1.1pp), the blind attack's advantage is small. The paper reports no confidence intervals, standard deviations, or significance tests despite averaging over cross-validation runs. For these two datasets, the "outperform" claim would be more honest as "essentially ties." The central claim of the paper (evaluation is flawed) is not harmed — a near-tie on a temporally controlled dataset where the shift has been minimized is still problematic for the evaluation — but the presentational inflation of these two results should be corrected.

- **Inconsistency between Table 1 and Table 2 for Temporal arXiv AUC values**: Table 1 reports the best prior attack as 72.3% (ours: 73.1%), while Table 2 reports the best prior attack as 74.5% (ours: 75.6%) for the same metric and dataset. This discrepancy is not explained and could confuse readers about which baseline is being compared against.

- **Greedy n-gram FPR stopping criterion not fully explicit**: Section 3.2 describes selecting n-grams sorted by TPR-to-FPR ratio on "part of the data" and evaluating on a "held-out set," but does not state that the 1% FPR threshold is calibrated on the training split. This detail is clear in the LAION-MI case study (line 272) but should be stated in the general methodology section.

### Trivial

- The abstract's claim that blind attacks "outperform state-of-the-art MI attacks" is technically true for all 8 datasets but creates an expectation of large margins; a caveat for the two temporal datasets with near-ties would improve accuracy.

## Nice-to-Haves

- **Correlation analysis between MI attack scores and blind attack features**: The paper's argument is logically complete without this — if a blind attack with no model access outperforms a model-based attack, the evaluation is invalid regardless of what the MI attack is doing. However, showing that, e.g., Min-K%++ scores on WikiMIA correlate with publication year would directly confirm that MI attacks are exploiting temporal features rather than extracting genuine membership signal, making the argument even tighter.

- **Demonstration on a clean dataset**: Showing that a blind attack achieves chance performance on a properly randomized split (e.g., a random subset of DataComp) would validate the proposed path forward experimentally. The paper argues conceptually but does not demonstrate that the proposed evaluation methodology avoids the flaws it identifies.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Comparison against prior results may not be apples-to-apples (train-test split)"**: The critic argues that the blind attack uses 80/20 train-test split while prior work reports on full data. This concern is weakened because the blind attack has *less* training data, making the comparison conservative (harder for the blind attack). For datasets with large margins, this is irrelevant; even for the marginal cases, the asymmetry favors the baseline, not the authors' method. Per the hard rule on asymmetric comparisons that favor the baseline, this criticism is removed.

- **"ViT-B/32 duplicated for CommonPool Medium and Small"**: This concerns a cited entity from the DataComp paper which cannot be verified without external sources. The paper reports what is available; any discrepancy belongs to the cited work, not this paper. Per the rule on questioning cited references and formatting nitpicks, this is removed.

## Novel Insights

The most novel observation that emerges from synthesizing the reviews is a potential *meta-flaw* in MI evaluation research: the very process of constructing *a posteriori* evaluation datasets for foundation models may be *inherently* susceptible to distribution shifts because the attacker necessarily knows the construction procedure (e.g., cutoff dates, data sources). The critical structural insight is that blind attacks serve as an *upper bound* on what any model-based MI attack could plausibly claim: if a blind attack performs at a given level, any MI attack that performs below that level is provably *worse than useless* (it extracts less signal than a method with no model access), while any MI attack that performs *above* the blind attack may still be exploiting weaker auxiliary features. This means that the relevant baseline for MI evaluation is not 50% AUC/chance, but rather the blind attack's performance — a point the paper implies but does not fully formalize.

## Suggestions

1. **Add confidence intervals or standard deviations** for the main results in Table 2, especially for Temporal Wiki and Temporal arXiv where the margins are small. This would clarify whether the differences are meaningful.

2. **Reconcile the Temporal arXiv AUC values** between Table 1 (72.3% best) and Table 2 (74.5% best). If these come from different experimental settings (e.g., different temporal splits), state this explicitly.

3. **In Section 3.2, explicitly state** that the 1% FPR for greedy n-gram selection is calibrated on the training split and then evaluated on the held-out test split.

4. **Hedge the abstract slightly** for the two temporal datasets where the blind attack essentially ties rather than clearly beats the prior state of the art.

5. **(Optional) Add a brief correlation analysis** for one dataset (e.g., WikiMIA: plot Min-K%++ score vs. publication year) to directly demonstrate that MI attack scores track the features the blind attack uses. This would preempt the skeptical reader's objection.

## Score and Decision

The paper makes a clear, significant, and timely contribution. The demonstrated flaw in MI evaluation methodology is broad (8 datasets across modalities) and deep (per-dataset root-cause analysis), and the results are decisively supported for 6 of 8 datasets. The identified weaknesses are minor and easily addressable: adding confidence intervals, reconciling a between-table numeric inconsistency, and clarifying one methodological detail. None threaten the core conclusion.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>