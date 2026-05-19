- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

The paper introduces SUFO, a systematic framework combining supervised probing, unsupervised similarity analysis (RSA), feature dynamics visualization, and outlier analysis with expert evaluation, designed to interpret fine-tuned transformer feature spaces for clinical decision-making. In a case study on pathology report classification (with MedNLI validation) comparing five 110M-parameter models spanning general-domain (BERT, TNLR), mixed-domain (BioBERT, Clinical BioBERT), and domain-specific (PubMedBERT) pre-training, SUFO reveals three main findings: (1) domain-specific PubMedBERT overfits to minority classes under class imbalance while mixed-domain models resist this; (2) in-domain pre-training accelerates feature disambiguation during fine-tuning; and (3) feature spaces undergo sparsification enabling outlier-based failure mode analysis.

## Strengths

- **Controlled probing baseline (Random-BERT)**. The paper includes a randomly initialized BERT as a baseline for supervised probing (Section 4.2, Table 2), explicitly addressing the known issue that even random features can perform well in probing methods. This ensures the reported probing scores are interpreted against a meaningful null.

- **Novel clustering-based outlier extraction procedure**. The paper develops a tailored clustering method on the top-2 principal components that handles differing scales and distributions across tasks by extracting one-dimensional intervals on PC1 and PC2 independently, then taking their cross-product (Section 6.1, Figure 3; lines 228–229). This goes beyond standard clustering in the sparsified feature space.

- **Identification of mixed-domain robustness via systematic comparison**. The paper reveals that PubMedBERT contains the most useful pre-trained features (highest probing score, Table 2) yet exhibits the worst fine-tuning performance on the imbalanced Path-PG task (0.770 vs. Clinical BioBERT's 0.959, Table 1), while mixed-domain models remain robust. This finding is replicated on simulated MedNLI subsets (Table 3), strengthening the conclusion beyond a single dataset.

- **Quantification of feature space sparsification**. The paper measures that the first two principal components explain on average 95% of variance across all tasks and models (Section 6.1), a crisp empirical observation that directly motivates the outlier extraction method.

- **Expert grounding of outlier modes**. The paper solicits feedback from a clinician to categorize outlier reports into five interpretable types (Section 6.2), providing domain-grounded insight into model failure modes that goes beyond purely quantitative evaluation.

## Weaknesses

### Fatal
None.

### Major

- **Missing per-class performance breakdown for the overfitting claim.** The paper's central finding—that PubMedBERT overfits to minority classes under imbalance—rests on aggregate F1 scores (Table 1) and a MedNLI simulation (Table 3), but per-class precision, recall, and F1 are never reported for Path-PG or any other task. The paper states that PubMedBERT "struggles with the minority one" (line 90) without showing the per-label numbers that would directly substantiate this. Without these, the performance gap could be driven by optimization failure, vocabulary mismatch, or other confounds rather than specifically minority-class overfitting. This is the single highest-leverage weakness because it concerns the paper's headline claim, and it is straightforward to fix.

- **Expert evaluation protocol is insufficiently rigorous to support comparative claims.** The outlier analysis is used to claim that domain-specific and mixed-domain models "allow for improved detection of missing medical information" (line 237–238), but this rests on feedback from a single domain expert with no mention of: (a) whether the expert was blinded to model identity, (b) how many outliers were evaluated per model, (c) what specific instructions or rubric was provided, or (d) any form of reliability quantification. With these details absent, the comparative statements about model behavior (e.g., "Clinical BioBERT and PubMedBERT identify more instances of truncated/unreported instances than BERT, BioBERT, and TNLR") are not empirically grounded. This is a methodological gap that weakens the entire outlier analysis section.

### Minor

- **Feature disambiguation speed claim is purely qualitative.** The claim that in-domain models "disambiguate faster" (epoch 6 vs. epoch 9; line 173) rests on visual inspection of PCA scatterplots without any quantitative cluster-quality metric (e.g., silhouette score, purity, or adjusted Rand index computed across training checkpoints). While the qualitative observation is plausible and illustrative, the current evidence does not support a comparative claim about speed. Adding a simple metric at each checkpoint would resolve this.

- **Missing fine-tuning hyperparameters.** The paper does not report learning rate, batch size, optimizer, or early stopping criteria for any of the fine-tuning experiments (confirmed via grep—none of these terms appear in the main text). The paper mentions "25 checkpoints" but does not clarify whether each checkpoint corresponds to an epoch. This is a substantive reproducibility gap for a paper whose core evidence comes from fine-tuning performance comparisons.

### Trivial
- The paper asserts that TNLR's different pre-training objective is "not expected to impact our findings" (line 71) before presenting evidence; the evidence does come later (TNLR behaves similarly to BERT), but the phrasing could be reordered to avoid the appearance of an unsupported claim.

## Nice-to-Haves

- **Confidence intervals or statistical tests on comparisons.** Tables 1 and 2 report standard deviations over three runs, which is useful, but the paper does not test whether differences between models (e.g., PubMedBERT vs. Clinical BioBERT on Path-PG) are statistically significant. A bootstrap test or confidence intervals would strengthen comparisons.
- **Robustness analysis for outlier extraction parameters.** The clustering procedure selects "either 2 or 3" intervals per PC "depending on the number of labels" (line 229), which is described, but a brief sensitivity analysis showing that conclusions are robust to small changes in this choice would strengthen the method.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism that the outlier distribution table (Table~ref{tab:gen_outlier}) is "not included in the provided text."* This is a parser artifact—the original submission contains the table. The paper clearly references it (line 237).
- *Criticism about missing statistical significance / variance estimates.* The paper already reports standard deviations over three runs. Requesting bootstrap tests goes beyond what is standard for this type of empirical study.
- *Criticism that "threats to validity are not discussed."* The paper's conclusion (line 245) explicitly states: "our results are limited in scale and to the setting of the clinical classification tasks. More work is needed to generalize." This partially addresses the concern.
- *Criticism about outlier extraction sensitivity (number of intervals).* The paper already specifies that intervals are set to "either 2 or 3 depending on the number of labels" (line 229), which is a clear rule.
- *Criticism that the TNLR remark is "asserted without justification."* The justification follows in the same paragraph (line 71: "we find that the quantitative and qualitative behavior observed in its analysis...are similar to BERT"), making this a presentation ordering issue at worst.
- *Strength about "expert validation" being strong evidence.* Given the weaknesses in the evaluation protocol (single unblinded rater, no reliability metrics), this strength is weaker than claimed. The attempt at expert grounding is commendable, but the resulting evidence is preliminary.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report per-class precision, recall, and F1 for Path-PG** (and ideally Path-SG, which also has some imbalance) for all five models. This single addition would directly substantiate or refute the overfitting claim and is the most impactful improvement.
2. **Strengthen the expert evaluation protocol** by documenting: number of outliers evaluated per model, whether the expert was blinded to model identity, and a clear description of the rubric used. Even with a single expert, transparency about these details would make the results interpretable.
3. **Add a quantitative cluster-quality metric** (e.g., silhouette score or purity) computed on PCA projections at each checkpoint to replace the purely qualitative speed-of-disambiguation claim.
4. **Report core fine-tuning hyperparameters** (learning rate, batch size, optimizer, epoch schedule) either in the main text or an appendix.
