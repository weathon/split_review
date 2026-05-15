Now I have all the evidence I need. Let me produce the consolidated review.

## Summary

This paper identifies a systematic flaw in existing membership inference (MI) evaluation datasets for foundation models. Across 8 published MI datasets (covering LLMs, diffusion models, and CLIP), the authors show that simple "blind" attacks — which exploit temporal shifts, biased replication, or distinguishable tails in member/non-member construction — outperform all state-of-the-art model-based MI attacks. The paper categorizes the failure modes and proposes using datasets with genuine random train-test splits (e.g., the Pile, DataComp, DataComp-LM) as a path forward.

## Strengths

- **Systematic diagnosis across all 8 evaluated MI datasets.** The paper categorizes distribution shifts into three types (temporal shifts, biased replication, distinguishable tails) and demonstrates each with concrete, verifiable evidence — e.g., the 2017/2023 year threshold in WikiMIA, non-English characters in LAION-MI, `.htm` vs `.html` formatting in Gutenberg. This breadth makes the critique far more general than concurrent work that only addressed temporal shifts in WikiMIA alone.

- **Blind attacks consistently and dramatically outperform reported state-of-the-art MI attacks.** Table 1 shows results like 94.4% vs 43.2% TPR@5%FPR on WikiMIA, 59.6% vs 18.8% TPR@1%FPR on Gutenberg, and 83.5% vs 40.3% TPR@1%FPR on Multi-Webdata. These gaps are so large they cannot be explained by noise, and they use the same metrics as the original papers.

- **The blind methods are simple, interpretable, and clearly expose the root causes.** Date regex, bag-of-words, and greedy n-gram selection are trivially implementable and each targets a specific type of distribution artifact. Showing that these simple methods beat sophisticated attacks with full model access (e.g., Min-K%++, loss-based attacks) makes the case that the evaluation sets are fundamentally invalid.

- **Constructive alternative proposed.** Section 5 identifies the Pile, DataComp, and DataComp-LM as benchmarks where random train-test splits exist, enabling genuine IID evaluation. Table 5 lists pool sizes and available model architectures, providing a concrete direction for future work.

- **Controls for confounding factors.** BookMIA analysis (footnote, line 200) removes books with shared authors between train and test and still achieves 80.3% AUC, demonstrating the distribution shift goes beyond author-specific features.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claim — that existing MI evaluation datasets are systematically flawed — is well-supported by the evidence presented.

### Minor

1. **Purely diagnostic; no positive demonstration on a clean IID split.** The paper shows that existing evaluations are broken, but does not run the complementary experiment: (a) confirm that blind attacks perform at chance on a properly constructed IID split (e.g., Pile), and (b) show that a state-of-the-art MI attack can extract meaningful signal on that same split. Without this, readers cannot assess whether MI attacks for foundation models are salvageable or fundamentally unworkable. This is not a flaw in what the paper does, but it limits the paper from being a complete evaluation cycle rather than a critique.

2. **Numerical inconsistency for Temporal arXiv between Table 1 and Table 4.** Table 1 reports the best reported AUC for Temporal arXiv as 72.3% (with our blind attack at 73.1%), while Table 4 (the "extended" version) reports the best attack AUC as 74.5% (with ours at 75.6%). Both cite the same source (duan2024membership). This is confusing and needs resolution — it is unclear whether the discrepancy reflects different splits, different baselines, or an error.

3. **Confidence intervals / variance not reported for most results.** The paper states results are "averaged from multiple runs" (line 177) and uses 10-fold cross-validation for bag-of-words classifiers, but no variance is reported. This matters for close comparisons such as Temporal Wiki (79.9% vs 79.6% AUC) and Temporal arXiv, where the gap is small enough to be within noise. Readers cannot assess whether these marginal "beats" are meaningful.

4. **Framing of supervised classifiers as "attacks" risks misinterpretation.** The blind attacks are supervised classifiers trained on member/non-member labels from the evaluation set itself, which is not a realistic threat model for MI. The paper does clarify this (lines 118–120: "We do not aim for our blind attacks to be optimal"), but the title and abstract repeatedly frame blind attacks as "outperforming" MI attacks, which could mislead readers about the nature of the comparison. This is a presentation choice that understates the paper's actual contribution — which is a diagnostic of flawed datasets, not a new attack.

### Trivial

1. **FPR calibration for greedy n-gram selection is underspecified.** The paper states "we use 80% of the data to pick the n-grams... until we hit a 1% FPR" (line 272) but does not clarify whether the FPR is calibrated on the training split or a separate validation split. While the held-out test evaluation mitigates overfitting concerns, the calibration process should be explicit.

2. **Gutenberg text-only control (16.6% TPR@1%FPR) excluded from Table 4.** This is a useful control result showing the shift persists even when ignoring formatting metadata, but it is only mentioned in prose (line 289) and not added to the table. Including it would strengthen the claim.

## Nice-to-Haves

- Run blind attacks and a standard MI attack on a clean IID split (e.g., Pile test set vs. training set) to complete the argument. This would validate that blind attacks fail and MI attacks can succeed under proper conditions, significantly raising the paper's impact.
- Release the replicated datasets (arXiv-1 month, Gutenberg) and code for all blind attacks to enable community verification and adoption.
- Plot ROC curves for at least one dataset (e.g., WikiMIA) to make the "outperforms" claim more transparent than point metrics alone.
- For BookMIA, quantify how much of the 90.5% AUC is attributable to temporal cues (publication date) vs. stylistic vocabulary differences beyond temporal shift.

## Removed Points

These points were flagged in the raw reviews but are removed (or moved from the main weaknesses) with justification:

- **"Replication of non-public datasets is underspecified"** — The paper explicitly states it "follows the specific collection steps" (line 177). The reviewer's concern about version differences is speculative and applies to any replication effort; the paper already acknowledges the limitation ("replicate a similar setup"). The blind attack still convincingly beats the MI attack regardless of small distributional differences. Moved here as a minor concern that doesn't affect the paper's conclusions.

- **"Multi-Webdata should also check image-only baseline"** — The paper explicitly scopes to captions ("For simplicity, we focus only on the image captions and ignore the visual content," line 237) and notes that visual features would likely strengthen the attack further (line 238). This is scope creep; not a weakness.

- **"Use a reference model feature instead of labels for blind attacks"** — This misunderstands the purpose of blind attacks, which are specifically designed to use NO model at all to diagnose dataset flaws. Not a valid weakness.

- **"Release datasets and code"** — Standard reproducibility suggestion, not a weakness. Moved to Nice-to-Haves.

- **"Missing ROC curves"** — Nice-to-have visualization, not a weakness. Moved to Nice-to-Haves.

- **"Section 5 proposal is vague"** — The paper clearly describes how IID splits can be constructed from the Pile/DataComp/DataComp-LM (lines 298–312) and provides pool size and model architecture details in Table 5. Not vague in the context of the paper's stated purpose.

## Novel Insights

Beyond the paper's own contributions, the most striking insight from the reviews is that the very *structure* of a posteriori dataset construction for MI evaluation is fundamentally broken: the act of trying to construct member and non-member sets from different sources introduces detectable artifacts that no amount of careful matching can fully eliminate. The paper's evidence that even carefully controlled datasets like LAION-MI (which explicitly tried to align distributions) still leave exploitable "distinguishable tails" suggests that the problem is not merely poor dataset design but an inherent limitation of the a posteriori approach. This implies that future MI research on foundation models must either adopt genuine IID splits (like DataComp) or develop entirely different evaluation paradigms — a more fundamental conclusion than the paper itself draws.

## Suggestions

1. **Resolve the Temporal arXiv AUC discrepancy** between Table 1 (72.3%/73.1%) and Table 4 (74.5%/75.6%) and provide a brief explanation. This is a concrete error that will confuse readers.
2. **Add a small-scale experiment on the Pile** (which is already used in prior work cited in the paper) confirming that blind attacks perform at chance on IID splits. Even a single-row addition to Table 4 would dramatically strengthen the positive case.
3. **Report standard deviations or 95% confidence intervals** for all results, especially for close comparisons (Temporal Wiki, Temporal arXiv).
4. **Rename "blind attacks" to "blind baselines" or "diagnostic baselines"** in the title and high-level framing to avoid conflating supervised classifiers with practical MI attacks. "Blind Baselines Beat..." more accurately reflects the contribution and reduces risk of misinterpretation.
5. **Add the Gutenberg text-only control (16.6% TPR@1%FPR) to Table 4** for completeness.

## Score and Decision

The paper makes a strong, timely, and empirically well-supported contribution by systematically exposing a fundamental flaw in the evaluation methodology of an active research area. The core claim is robust and consistently demonstrated across 8 datasets spanning multiple modalities. The weaknesses identified are primarily about completeness framing and presentation — none threaten the paper's main conclusions. The lack of a positive demonstration on a clean IID split limits the paper from being a complete evaluation cycle, but does not invalidate its diagnostic contribution. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>