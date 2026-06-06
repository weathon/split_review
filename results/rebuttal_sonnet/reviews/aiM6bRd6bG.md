## Summary

This paper introduces PPI candidate ranking as a prospective retrieval task: given a target protein's known interaction partners from STRING v11, rank novel candidates that appear in STRING v12. The core framework uses contact-map-guided "active residue" selection to compute cosine similarity between known partner embeddings and candidate proteins (exemplar-based retrieval), followed by a multi-source re-ranking module (interaction scores, SpeedPPI/pDockQ, functional annotations, fine-tuned LLMs). Large empirical gains over raw prediction probability baselines are reported, with D-SCRIPT Recall@10 rising from ~1.2% to ~26.4%.

---

## Rebuttal Assessment

### Weakness: Missing ablation on unmasked cosine similarity
- **Author's response:** Partially address
- **Assessment:** Unconvincing. The author acknowledges the ablation is absent and agrees it is necessary to disentangle the exemplar-anchor paradigm from the contact-map masking contribution. Their counter-argument—that the IS baseline "already exploits the contact map via Eq. (6)"—is misleading: Eq. (6) is just the max contact probability used as a scalar ranking score, not cosine similarity over masked embeddings using known-partner anchors. The reviewer's specific request was for a full-embedding cosine similarity baseline using the same exemplar-anchor strategy, which remains entirely absent from the paper. The author promises this for a future revision, which does not count.
- **Score impact:** Weakness unchanged

### Weakness: "Two orders of magnitude" conclusion overstates the result
- **Author's response:** Acknowledge
- **Assessment:** Fully confirmed. The author verifies all the reviewer's numbers: D-SCRIPT Recall@5 0.0071→0.1832 (≈26×), MRR 0.034→0.169 (≈5×), MAP@5 0.0103→0.2714 (≈26×). The claim that "D-SCRIPT Success@5 = 0.0000 at baseline" is confirmed in Table 1, but correctly identified by the author as insufficient to substantiate a "two orders of magnitude" claim across metrics. The abstract (line 25) and conclusion (lines 278–279) both retain the "two orders of magnitude" language as submitted, contradicted by the body text in Section 5.3. The author acknowledges this as "a legitimate error" and promises correction in revision—but the paper as submitted still contains the overstatement.
- **Score impact:** Weakness unchanged

### Weakness: Re-ranking evaluation does not report absolute quality after re-ranking
- **Author's response:** Acknowledge
- **Assessment:** Fully confirmed. The author concedes Table 2's rank-shift fractions do not capture the scenario where a signal improves many pairs by small margins while degrading a few by large margins. The paper contains no absolute nDCG@10 or Precision@k before/after re-ranking. The author promises this for revision.
- **Score impact:** Weakness unchanged

### Weakness: Data leakage risk for LLM re-ranking is acknowledged but unanalyzed
- **Author's response:** Partially address
- **Assessment:** Partially convincing. The author's rebuttal points to Section 4.2's GroupKFold protein-identity split (confirmed at line 145 of the paper) as evidence that *fine-tuning* leakage is properly controlled. This is a genuine and meaningful clarification—the cross-encoder training/eval split is sound. However, the reviewer's concern was specifically about *pretraining* leakage (PubMedBERT trained on PubMed, which may contain descriptions of STRING v12 interactions). The author's differential-performance argument (PubMedBERT 75.5% vs. BioBERT/BioMedRoBERTa 65–72%) is suggestive of architectural superiority but not conclusive—it cannot rule out that PubMedBERT also has higher pretraining leakage because it is trained more thoroughly on the same domain. The paper acknowledges this uncertainty in lines 262–264 but provides no further characterization.
- **Score impact:** Weakness downgraded (fine-tuning leakage concern resolved; pretraining leakage concern weakened but not removed)

### Weakness: xCAPT5's precision advantage may reflect abstention bias
- **Author's response:** Acknowledge
- **Assessment:** Confirmed as a valid limitation. The author correctly notes this does not affect the primary comparison (their approach vs. D-SCRIPT and Topsy-Turvy, which share the same protein set and embeddings). This is a reasonable framing—xCAPT5 is an additional reference point, not the primary competitor. The weakness is minor in scope.
- **Score impact:** Weakness downgraded (properly contextualized as not affecting main comparison)

### Weakness: Maximal contiguous segment lacks precise algorithmic definition
- **Author's response:** Acknowledge
- **Assessment:** Confirmed. The author concedes no smoothing window or threshold is specified in the main text, and notes the details are in "Appendix A.1." Critically, the paper as read ends with "Rest of paper (reference and Appendix) is removed"—meaning the appendix was unavailable to reviewers. The promise that A.1 contains the details cannot be independently verified. This is a genuine reproducibility gap.
- **Score impact:** Weakness unchanged

---

## Strengths
- **Prospective temporal evaluation design.** Use of STRING v11→v12 as a genuine prospective benchmark (Eqs. 1–2) is methodologically sound and addresses a real gap. Confirmed in Section 4, lines 63–72.
- **Substantial empirical gains in early-rank retrieval.** Table 1 confirms D-SCRIPT Recall@10: 0.0124→0.2641 (~21×), MRR: 0.034→0.169 (~5×). These are practically significant for candidate screening.
- **Comprehensive metric coverage.** Eight metrics at six cutoffs and three baselines (Table 1) reduce single-metric gaming.
- **Complementarity analysis across 10 re-ranking signals.** Table 2 provides systematic pairwise characterization. The finding that PubMedBERT (75.5%) and lightweight KeyTerm Jaccard (69.3%) outperform pDockQ (47.2%) is a useful practical insight.

---

## Weaknesses

### Fatal
None.

### Major
- **Missing ablation on unmasked cosine similarity.** The paper never compares its masked exemplar-cosine approach against full-embedding cosine similarity using the same known-partner anchors. The core mechanistic claim—that contact-map masking specifically drives the improvement—remains unvalidated. The author acknowledges this and promises revision, but the gap persists in the submitted paper.
- **"Two orders of magnitude" overstatement.** The abstract (line 25) and conclusion (lines 278–279) claim "two orders of magnitude" improvement (100×) when Table 1 shows ≈5–26× across all computable metrics. The body text (Section 5.3) is self-consistent but directly contradicts the abstract and conclusion. Author acknowledgment confirms this is an error.

### Minor
- **Re-ranking evaluation lacks absolute quality reporting.** Table 2's maintain-or-improve fractions are insufficient to characterize whether re-ranking signals improve overall nDCG@10. Author-confirmed gap.
- **LLM pretraining leakage uncharacterized.** PubMedBERT's gains may partly reflect pretraining exposure to PubMed literature describing STRING v12 interactions. Fine-tuning leakage is properly controlled (GroupKFold, confirmed); pretraining leakage is acknowledged but unquantified.

### Trivial
- **Maximal contiguous segment lacks threshold definition** in main text; appendix removed from reviewed version. Reproducibility gap.
- **xCAPT5 abstention bias** is a valid methodological concern for the xCAPT5 comparison, though it does not affect the paper's primary results.

---

## Nice-to-Haves
- Add unmasked-cosine ablation baseline: highest-leverage single experiment for validating or reframing the contact-map masking narrative.
- Report nDCG@10 before and after each re-ranking signal to complement Table 2.
- Clarify UniProtKB version used for functional annotation retrieval (potential look-ahead bias).
- Analyze which protein categories benefit most/least from the approach.

---

## Novel Insights

The most genuinely novel insight is the reframing of PPI prediction as an exemplar-based information retrieval problem: using known interaction partners as embedding anchors for nearest-neighbor search dramatically outperforms raw model output probabilities as a ranking criterion—regardless of whether the contact-map masking is the specific driver. The prospective temporal evaluation framework (STRING v11→v12) is a concrete and transferable methodological contribution. The re-ranking analysis demonstrates that lightweight functional annotation signals (KeyTerm Jaccard, TF-IDF) match or exceed computationally expensive structural signals (pDockQ), a practically actionable finding for prioritizing candidate validation resources.

---

## Suggestions
1. Add the unmasked-cosine-similarity ablation using the same exemplar-anchor framework. Either outcome is informative.
2. Correct "two orders of magnitude" in the abstract, introduction, and conclusion to the verified ~5–26× range from Table 1.
3. Extend Table 2 with nDCG@10 before and after each re-ranking signal.
4. Include the algorithmic definition of "maximal contiguous segment" (threshold, smoothing) in the main text or a clearly marked appendix.

---

## Score and Decision

**Rebuttal impact summary:** The rebuttal is entirely one of honest acknowledgment. Every major weakness identified in the original review is confirmed as legitimate by the author. No weaknesses were refuted with paper evidence. No previously hidden strengths were revealed. The only meaningful positive change is the partial resolution of the fine-tuning leakage concern (GroupKFold protein-identity split is confirmed in the paper)—which slightly reduces the severity of one minor weakness—and the contextualization of xCAPT5's abstention bias as not affecting the primary comparison. These adjustments are insufficient to move the score.

The two major weaknesses—missing ablation and two-orders-of-magnitude overstatement—remain fully intact in the submitted paper. Promises to fix them in a future revision do not count. The original score of 5.0 is maintained.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>