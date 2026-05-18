Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes a data filtering method for Chinese Spelling Correction (CSC) that uses a well-calibrated model (trained on random-replacement data) to filter noisy samples from OCR/ASR-based training corpora. The authors provide empirical evidence that random-replacement data yield better-calibrated CSC models, offer a Bayesian theoretical analysis explaining this phenomenon, and show that a simple BERT model trained on the refined corpus substantially reduces false positive rates while improving F1 over the plain BERT baseline.

## Strengths

- **Empirical demonstration of a calibration gap between data types.** Figure 1 shows that the random-replacement model achieves ECE 0.104 vs. 0.163 for the OCR/ASR-based model, with a lower sentence-level false positive rate. This is a genuine, well-supported observation that motivates the work.

- **Consistent and substantial improvements over a strong BERT baseline.** Table 1 shows F1 gains of +3.4 (SIGHAN13), +5.2 (SIGHAN14), and +2.7 (SIGHAN15) over plain BERT, achieved purely through data filtering without architectural changes. This cleanly demonstrates the value of corpus refinement.

- **Effective reduction of over-correction.** Table 2 reports that the filtering strategy drops FPR from 37.9% to 6.9% on SIGHAN13 and from 15.1% to 7.7% on SIGHAN15, while also lowering ECE. This directly validates the paper's core claim about mitigating over-correction.

- **Comprehensive comparison against alternative corpus-utilization strategies.** Table 3 contrasts the proposed method with mixing, heuristic filtering, self-filtering, and self-adaptive training. The proposed method consistently outperforms all alternatives, showing that the learned calibration-based filter is more effective than simpler approaches.

- **Practical parameter analysis.** Sections 5.5 and 5.6 study the effect of the confidence threshold and data volume, finding that p=1e-2 works well across datasets and that million-scale auxiliary data suffice for stable estimation.

## Weaknesses

### Major

- **Factually incorrect state-of-the-art claims that contradict the paper's own results.** The abstract claims "impressive state-of-the-art performance" and the conclusion states "Our method impressively achieves state-of-the-art performance on SIGHAN 13/14/15." However, Table 1 shows the method does not exceed the best published results on any of the three benchmarks: DORM achieves 85.8 vs. the method's 82.3 on SIGHAN13; PHMOSpell achieves 71.6 vs. 69.5 on SIGHAN14; SCOPE achieves 80.7 vs. 76.1 on SIGHAN15. Furthermore, §5.1 (line 294) itself says "Although our method did not achieve state-of-the-art results," directly contradicting the abstract and conclusion. A paper that misrepresents its central empirical achievement has a coherence problem that must be resolved. This is not a minor rhetorical flourish — it is factually wrong and undermines trust in the authors' characterization of their contribution.

- **Calibration comparison uses a non-standard preprocessing step without full-data validation.** In §2.2 (line 79), the authors state that they "eliminate those characters—in whose prediction distribution the possibility of being corrected to other characters is below 0.1—to draw the calibration curve and calculate ECE." This filtering removes easy correct predictions, which could significantly alter reported ECE values. The paper does not show calibration curves or ECE on the full set of predictions, nor does it justify why the standard definition of calibration (over all predictions) should be abandoned. Since the calibration difference between data types is a primary motivation for the whole paper, this needs to be validated on unfiltered predictions.

### Minor

- **The theoretical analysis is loosely connected to the actual filtering method.** The Bayesian derivation (§3) produces equations and the insight that random-replacement data yield upper-bounded confidence for noisy samples. However, the filtering step (§4.1) simply trains a BERT model on random-replacement data and applies a dataset-specific threshold. The theory does not predict what the threshold should be, nor does it provide a principled way to set it without per-dataset search (as analyzed post-hoc in §5.4). The theory serves as a plausible *explanation* for why filtering might work but does not *guide* the method beyond the general idea of using confidence. This disconnect weakens what is presented as a main contribution.

- **The empirical validation of sample categorization (§5.2) is weak.** The heuristic identification of noisy and multi-answer samples uses arbitrary thresholds (λ_N=0.9, λ_M=0.8) on a BERT masked-prediction criterion, finding only 160 noisy and 34 multi-answer samples out of 3000 checked. While the paper acknowledges this is a "heuristic method to roughly find these samples," the thresholds are not justified, the sample sizes are tiny, and the claim that this "verifies" the theoretical categorization is overstated given the fragility of the identification method.

- **Uneven FPR reduction across datasets is not discussed.** Table 2 shows FPR drops from 37.9→6.9 on SIGHAN13 but only 17.0→14.6 on SIGHAN14. The dramatic drop on SIGHAN13 may partly reflect the exclusion of 的/地/得 from evaluation (as noted in the table caption). The paper does not discuss why the benefit is uneven, nor does it report FPR for the SOTA baselines, making it unclear whether the high FPR of BERT is a general problem or specific to this evaluation setup.

- **No discussion of computational cost.** Training a filtering model on 9 million sentence pairs is not trivially cheap. The paper positions itself as "simple and efficient" but provides no runtime or GPU-hour comparison with baselines, which would help assess the practical trade-off.

- **No comparison against other data-filtering baselines.** The paper cites confident learning (Northcutt et al. 2021) in related work but does not implement it as a baseline. Adding even one off-the-shelf denoising baseline would strengthen the comparison.

### Trivial

- None.

## Nice-to-Haves

- Report ECE and calibration curves on the *full* set of predictions (without the 0.1-probability filtering in §2.2) to allow readers to directly assess the central calibration claim.
- Report FPR for the SOTA baselines (PHMOSpell, DORM, SCOPE, etc.) to contextualize whether the over-correction problem is specific to BERT or more general.
- Add a discussion connecting the theoretical bounds to the chosen threshold p=1e-2, explaining why this value works or how it relates to the derived quantities.

## Removed Points

These points were identified by the original reviewers but have been removed during consolidation for the reasons stated below. They are preserved here in case they are useful, but should be treated with caution.

- **"The method's computational cost is not discussed"** — Kept as a minor weakness above. Not removed.
- **"The paper's central claim of state-of-the-art performance is false"** — This is a real, verified weakness. Kept as a Major weakness above. Not removed.
- Any complaints about formatting/typos/garbled text — These reflect parser artifacts, not author errors. Removed per hard rules.
- Any complaints about missing appendix sections — These exist in the original submission but were stripped by the parser. Removed per hard rules.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper makes a genuine contribution (showing that data filtering can meaningfully close the gap between a simple BERT and more complex multi-modal architectures) but undermines itself by overclaiming SOTA. The actual message — "a simple BERT with clean data is competitive with specialized architectures" — is arguably more interesting than the false SOTA claim, because it reframes the problem: the bottleneck in CSC may be data quality rather than model architecture. The reviews collectively suggest the paper would be *stronger* if it leaned into this narrative rather than reaching for a SOTA label it does not support.

## Suggestions

1. **Correct the SOTA claims immediately.** Replace "state-of-the-art" in the abstract and conclusion with an honest characterization: the method significantly improves BERT and achieves competitive performance with more complex models, but does not surpass the best published results on these benchmarks. This honest framing better highlights the paper's genuine contribution.
2. **Report calibration metrics on the full set of predictions** (without the 0.1-probability filtering) to allow readers to directly evaluate the central empirical claim.
3. **Add even one off-the-shelf data-denoising baseline** (e.g., confident learning) to strengthen the comparison.
4. **Strengthen the theory-method connection** by discussing why p=1e-2 works and whether it corresponds to any derived theoretical quantity.
5. **Discuss why FPR improvement varies across datasets** and report FPR for SOTA baselines to contextualize the over-correction problem.

## Score and Decision

This paper has a solid core: a well-motivated data filtering method that improves BERT-based CSC and reduces over-correction, supported by a thoughtful theoretical analysis. The experiments are comprehensive in comparing against alternative corpus-utilization strategies and studying hyperparameters. However, the paper is marred by a significant and verifiable problem: the abstract and conclusion claim state-of-the-art performance when the paper's own Table 1 clearly shows otherwise, and §5.1 even explicitly contradicts this claim. This is not a minor presentational issue — it is a factual error in the paper's central empirical assertion. Combined with the non-standard calibration preprocessing that is not validated on full data, the paper cannot be accepted in its current form. The underlying science is sound enough that with honest corrections, it could be a solid contribution, but as submitted the misrepresentation is too severe to overlook.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>