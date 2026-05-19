- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3
Here is my consolidated review.

---

## Summary

This paper demonstrates that existing membership inference (MI) evaluation datasets for foundation models contain distribution shifts between members and non-members so large that simple "blind" attacks (which ignore the target model entirely) outperform all reported state-of-the-art MI attacks across 8 datasets spanning LLMs, diffusion models, and CLIP. The paper categorizes these shifts into temporal, replication-bias, and distinguishable-tail types, and proposes replacing flawed *a posteriori* evaluation datasets with properly randomized train-test splits (e.g., DataComp, DataComp-LM).

## Strengths

1. **Strong empirical demonstration across diverse settings.** Table 1 and the extended Table 2 show blind attacks beating reported MI numbers on 8 evaluation sets covering different modalities, models, and dataset constructions. The most striking results (WikiMIA: 94.4% vs 43.2% TPR@5%FPR; Multi-Webdata: 83.5% vs 40.3% TPR@1%FPR; Gutenberg: 59.6% vs 18.8% TPR@1%FPR) involve gaps large enough that protocol differences could not plausibly explain them. These clear-cut cases alone convincingly support the paper's core thesis.

2. **Useful taxonomy of distribution shifts.** Section 3.1 identifies three concrete categories (temporal shifts, biased replication, distinguishable tails) and then maps each to specific datasets in Section 4. This goes beyond the temporal-shift observation of concurrent work (Duan et al., Maini et al.) and provides a framework for diagnosing future evaluation-set flaws.

3. **Interpretable methodology strengthens the argument.** The blind attacks (date regex, bag-of-words, greedy n-gram selection) are deliberately simple, making it obvious that the distribution shifts are large and trivially exploitable. For instance, on arXiv-1 month a citation-year check achieves 13.4% TPR@1%FPR — over double the best MI attack — without any model access whatsoever (Section 4.1.4).

4. **Constructive path forward.** Section 5 proposes concrete datasets with random train-test splits (DataComp, DataComp-LM, the Pile) and catalogs available models and pool sizes in Table 3. This provides a practical starting point for rigorous future evaluations, which is a genuine positive contribution beyond the critique.

## Weaknesses

### Fatal
None.

### Major

1. **Comparison against reported numbers rather than re-implemented baselines on identical splits.** The paper compares blind attack results against "best reported" numbers from prior work without re-running those MI attacks under the same conditions (same data splits, same evaluation protocol). For the large-margin datasets this does not threaten the core argument — the gaps are too wide for protocol differences to bridge. However, for Temporal Wiki (79.9% vs 79.6% AUC) and Temporal arXiv (75.6% vs 74.5% AUC), the margins are within the range of typical metric variance across evaluation protocols, and the paper's claim of "outperform[ing]" is weakened by the lack of a direct apples-to-apples comparison. The paper acknowledges these margins are small (line 213: "slightly outperforms"), but the evidential gap remains: without running prior attacks on the exact same splits, the conclusion that the blind attack "beats" prior work on these two datasets is not fully supported.

### Minor

1. **Evaluation set sizes not reported.** The paper does not state the size of each MI evaluation dataset. This matters for assessing the reliability of the bag-of-words and greedy n-gram results, especially for smaller datasets where 10-fold cross-validation on an 80/20 split could have high variance. The reader cannot assess whether results like the 79.9% vs 79.6% AUC gap on Temporal Wiki is statistically significant.

2. **No confidence intervals or significance estimates.** Results are reported as point estimates without variance or confidence intervals. For the marginal cases (Temporal Wiki, Temporal arXiv), this makes it impossible to determine whether the blind attack's lead is real or within noise. Even for the larger-margin cases, confidence intervals would strengthen the presentation.

3. **"Worse than chance" phrasing is imprecise without clarification.** The paper states that existing MI attacks perform "worse than chance" (lines 42, 96), meaning they perform worse than a simple blind baseline that exploits distribution shifts. A reader who takes "chance" to mean random guessing (50% AUC or equal TPR/FPR) would be confused, since the blind attack achieves well above 50% AUC. The paper defines its meaning implicitly but could be more explicit that the relevant baseline has moved from random to a shift-exploiting blind attack.

4. **Replicated dataset fidelity is uncertain.** For arXiv-1 month and Gutenberg, the paper follows the original collection steps but cannot fully guarantee the resulting datasets are identical to those used in prior work. The paper states this transparently (line 177), but the results on these datasets would be stronger if the prior attacks could be evaluated on the same replicated datasets. This does not undermine the paper's diagnostic argument but adds uncertainty to the quantitative comparisons.

### Trivial
None.

## Nice-to-Haves

- Re-running at least one representative prior MI attack (e.g., Min-K%++ or the loss-based Carlini et al. 2022 attack) on the exact same data splits used for the blind attacks would transform the comparison from "our number beats their reported number" to "under identical conditions, a model-blind classifier outperforms a model-dependent one."
- Briefly testing the proposed DataComp path (e.g., running a simple loss-threshold attack on a DataComp model with a random train-test split) would solidify the constructive contribution, though this is not required for the critical contribution of the paper.

## Removed Points

The following points from the input reviews are excluded per meta-reviewer guidelines:

- **Asymmetry in information / unfair comparison:** The claim that blind attacks have more information (labeled training data from the evaluation set) than prior MI attacks is removed by rule: the asymmetry is intentional to prove a stronger point, and the paper's diagnostic argument does not require the comparison to be "fair" — it only needs to show that data features alone suffice to discriminate members from non-members.
- **Missing appendix/code/implementation details:** Removed by rule — the parser strips supplementary sections from all papers; these exist in the original submission.
- **Generic speculation about confounders:** The harsh critic's speculation that "prior attacks might also be successfully exploiting distribution shifts (albeit less effectively) while still extracting *some* real membership signal" is noted but does not rise to a verifiable weakness — the paper's conclusion ("evaluations tell us nothing about membership leakage") is appropriately scoped and does not claim prior attacks extract *zero* signal, only that the evaluations cannot separate model leakage from distribution artifacts.
- **Missing related works:** Removed by rule — I cannot externally verify existence of omitted references.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add dataset sizes (sample counts) to the case studies in Section 4, so readers can assess statistical reliability.
2. Provide confidence intervals (e.g., from the 10-fold cross-validation) for the blind attack results, particularly for the datasets where margins are small.
3. For the marginal cases (Temporal Wiki, Temporal arXiv), either re-run the best prior MI attack on the identical split, or explicitly state that the blind attack essentially matches (rather than beats) prior work on these datasets and that this is still damning because it shows the model adds nothing.
4. Clarify the "worse than chance" framing in Section 2 with an explicit definition: the relevant baseline is a blind attack that exploits the distribution shift, not random guessing.
5. In each case study subsection, explicitly state whether the prior attack result was obtained on the same data (and if not, what the differences are), rather than stating this once in the preamble.

**Originality:** High — the paper identifies a widespread but previously unrecognized methodology flaw.  
**Importance of research question:** Very high — MI attacks are used for copyright detection, unlearning audits, and privacy measurement.  
**Claims supported:** The core claim is well-supported by the large-margin cases; weaker on small-margin datasets.  
**Soundness of experiments:** The methodology is sound for a diagnostic study, though the uncontrolled comparison weakens the quantitative precision.  
**Clarity of writing:** Clear and well-structured.  
**Value to community:** Significant — the paper should change how MI evaluations for foundation models are conducted.
