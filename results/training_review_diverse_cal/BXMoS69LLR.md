I have all the information needed. Let me now produce the consolidated review.

## Summary

This paper demonstrates that eight published membership inference (MI) evaluation datasets for foundation models contain systematic distribution shifts between members and non-members. The authors design simple "blind" attacks that never query the target model (e.g., date thresholding, bag-of-words classifiers, greedy n-gram selection) and show these attacks outperform every reported state-of-the-art MI attack across all datasets. The paper thus exposes a fundamental methodological flaw: current evaluations cannot distinguish whether MI attacks detect actual training data leakage or merely exploit dataset artifacts. It recommends replacing flawed datasets with those having random train-test splits (e.g., the Pile, DataComp).

## Strengths

- **Systematic evidence across 8 datasets and two modalities.** The paper shows blind attacks outperform the best reported MI attacks on every dataset examined. For example, on WikiMIA the blind bag-of-words attack achieves 94.4% TPR@5%FPR versus the best prior attack's 43.2%; on Multi-Webdata the blind greedy n-gram attack achieves 83.5% TPR@1%FPR versus 40.3%. This covers text (LLMs) and vision-text (diffusion models, CLIP) modalities.

- **Simple, model-agnostic blind baselines that prove existing MI attacks are not measuring model leakage.** The blind attacks ignore the target model entirely yet beat all reported results. The date-detection baseline on WikiMIA (52.3% TPR@5%FPR) already exceeds the state-of-the-art attack simply by extracting date strings. This directly supports the conclusion that current evaluations conflate distribution differences with membership signal.

- **Causal analysis backed by concrete evidence for each distribution shift.** The paper categorizes three sources (temporal shifts, biased replication, distinguishable tails) and provides explicit demonstrations: citation-year patterns in ArXiv-1 month (13.4% TPR@1%FPR via regex on `\cite` commands); character-level biases in LAION-MI traced to translation artifacts (Russian letters `о`/`т` appear in 0.23%/0.15% of members vs 0.03% of non-members); and formatting drift in Gutenberg (.htm vs .html file extensions).

- **Demonstration that even explicit distribution-mitigation attempts still leave exploitable biases.** For LAION-MI, the authors tried to align members and non-members via translation and aesthetic filtering, yet blind character-level n-grams still achieve 9.9% TPR@1%FPR (vs 2.5% best attack). For Gutenberg, restricting publication dates to 1850–1910 still allows 59.6% TPR@1%FPR via metadata formatting differences. This shows the problem is persistent and subtle.

- **Constructive proposal for replacing flawed datasets.** Section 5 recommends the Pile, DataComp, and DataComp-LM, which have random train-test splits, and lists specific models and pool sizes already available.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Quantitative comparison uncertainty for two recreated datasets.** For ArXiv-1 month and Gutenberg, the paper correctly notes the original datasets were not public and it recreated similar ones following the original collection steps. However, Table 1 presents the numbers as direct comparisons without caveats. Since the paper itself demonstrates that even subtle differences in data collection can introduce exploitable shifts, the exact margin of outperformance on these two datasets carries additional uncertainty. The qualitative conclusion (these datasets are flawed) stands, but the specific quantitative margins may not be directly comparable to prior reported scores.

- **No empirical validation that the proposed alternatives actually pass the blind attack test.** The "Path Forward" recommends the Pile, DataComp, and DataComp-LM as alternatives but does not empirically demonstrate that blind attacks achieve chance performance (50% AUC) on these datasets when tested against models trained on them. A controlled experiment showing this—even on a small subset such as a Pythia model on the Pile—would substantially strengthen the constructive proposal. Without it, a skeptical reader could wonder whether the blind attack would still find confounds in these datasets.

- **Limited systematic connection between feature analysis and classifier decisions.** The paper provides intuitive feature-level analyses (dates, non-English characters, file extensions) but these are not systematically linked to the bag-of-words classifier's decision boundaries. For example, the BookMIA bag-of-words classifier could be using book content beyond the demonstrated distributional artifacts (the paper controls for authors, but not for other content-specific features). This does not weaken the main argument—the blind attack beats MI attacks regardless of *why*—but it leaves room for ambiguity about exactly which features drive the performance gap.

### Trivial
- The paper could include an explicit, upfront statement of what constitutes a valid evaluation (blind attack achieves chance) to sharpen the framing early on. This is currently implicit in Section 3.1 but could serve as a clearer organizing principle.

## Nice-to-Haves

- A controlled experiment showing that blind attacks achieve chance on a model trained with a proper random train-test split (e.g., Pythia on the Pile).
- A small-scale attribution study connecting specific bag-of-words features to the performance gap, to clarify whether MI attacks use weak signals or exploit distributional features suboptimally.
- Discussion of how varying the member/non-member balance interacts with distribution shifts across datasets.

## Removed Points

These points were raised by reviewers but are factually incorrect, misread the paper, or violate the review guidelines:

- **"Blind attacks are not truly blind to member/non-member distributions."** The paper (abstract, line 15–17; line 42) consistently defines "blind" as *blind to the model* and transparently states it uses 80% of labeled data for training (line 129–130). This criticism reflects a misreading of the paper's terminology.
- **"The main claim is slightly overgeneralized."** The paper's claim about "existing evaluations" is explicitly scoped to the eight datasets studied. The evidence supports this scope; the paper later identifies valid alternatives (Pile, DataComp), which is consistent with a specific rather than universal claim.
- **"Would benefit from separating the two sub-claims."** The paper already compares blind attacks against "Best Reported" scores per dataset, which implicitly separates the question of distribution shifts from MI attack quality. No additional restructuring is needed.
- **Formatting/style nitpicks and generic reproducibility concerns** (hyperparameter disclosure, missing appendix references, etc.) that reflect parser artifacts or are standard for the paper type.

## Novel Insights

The key insight that goes beyond the paper's own framing is that the failure of MI evaluations is not merely about temporal shifts (already known from concurrent work on WikiMIA) but is *structural and pervasive*: even careful mitigation attempts (LAION-MI's translation + filtering, Gutenberg's date-range restriction) fail to remove exploitable artifacts. This means that a proper evaluation of MI attacks on foundation models is not simply a matter of "fixing" existing datasets but requires fundamentally redesigning the evaluation protocol around models with known train-test splits—a much higher bar for the community than previously appreciated.

## Suggestions

- Add a small-scale validation experiment (on a subsection of the Pile or DataComp) showing that the blind attack achieves chance performance on models trained with proper random train-test splits.
- Add explicit caveats in Table 1 for ArXiv-1 month and Gutenberg that the numbers compare against prior work on *recreated* (not original) datasets.
- Include an upfront principle: "A valid MI evaluation must yield chance performance (50% AUC) for a model-blind baseline."
- Consider a simple ablation that compares the bag-of-words classifier's performance on the 80% train split to a single MI attack (not just "best reported") on each dataset, to help disentangle whether the gap comes from distribution shifts or suboptimal MI attack design.

## Score and Decision

The paper makes a significant and well-supported contribution. The core claim—that existing MI evaluation datasets for foundation models contain distribution shifts that blind attacks can exploit—is convincingly demonstrated across 8 datasets, two modalities, and multiple sources of shift. The weaknesses are minor (uncertainty margins on two recreated datasets, lack of validation for proposed alternatives) and do not threaten the paper's central finding. The paper is clearly written, the negative result is important, and the constructive path forward is sensible.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>