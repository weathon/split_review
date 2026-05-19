- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 6, 5, 5, 3
Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper challenges the necessity of spectral augmentations in contrast-based graph self-supervised learning (CG-SSL), arguing that simple edge perturbation (edge dropping for node-level tasks, edge adding for graph-level tasks) is more effective, more efficient, and sufficient. The authors support this claim with experiments across four CG-SSL frameworks (MVGRL, GRACE, BGRL, G-BT) and 12 datasets, plus supporting analyses on spectral degeneration and a spectral perturbation experiment.

---

## Strengths

- **Broad and systematic empirical comparison showing SPAN is not superior to simple edge perturbation.** Tables 2 and 3 compare DROPEDGE/ADDEDGE against SPAN (a state-of-the-art spectral method) under four distinct CG-SSL frameworks and 12 datasets. In nearly every setting, simple edge perturbation matches or outperforms SPAN. This is a solid, reproducible finding within the controlled comparison.

- **Efficiency and scalability evidence.** Table 1 provides concrete time and space complexity comparisons (e.g., SPAN's empirical time on PUBMED is ~2737s vs. ~0.12s for edge perturbation), showing spectral augmentations are orders of magnitude more expensive. The paper also explicitly states it excludes OGBN datasets because spectral methods cannot scale—an honest acknowledgment of a real practical limitation.

- **The spectral degeneration analysis (Section 7.1) is a creative diagnostic approach.** Visualizing how the average spectrum of augmented graphs collapses across datasets (Figure 2) provides an interesting perspective on why spectral cues may not drive performance. While the analysis is limited to one framework and augmentation, the idea is sound and could inform future work.

---

## Weaknesses

### Fatal
None. The paper's core empirical finding—that SPAN does not outperform simple edge perturbation under fair comparison—is supported by the experiments in Tables 2 and 3. The weaknesses below are serious but not fatal.

### Major

- **Overclaiming beyond the evidence: the paper equates "spectral augmentations" with "SPAN."** The paper claims spectral augmentations as a class are unnecessary, yet only SPAN is directly compared under controlled conditions across all settings. GASSER has no open-source code and its results are taken directly from the original paper (marked with †); SpCo is only applicable in its original setting (GRACE, node-level). The paper is transparent about these limitations (lines 107-110), but the bold title, abstract, and conclusion do not hedge accordingly—they assert "spectral augmentations" broadly. This is a mismatch between the claim and the evidence. The paper would be stronger if it reframed its contribution as "SPAN does not outperform simple edge perturbation" rather than "spectral augmentations are unnecessary."

- **No variance or statistical significance reporting.** All results in Tables 2 and 3 are reported as single point estimates. Graph SSL results are known to vary with random seeds, data splits, and initialization. Several gaps between DROPEDGE/ADDEDGE and SPAN are small enough (e.g., CORA under GRACE: 83.6 vs. 83.2; COAUTHOR-CS under G-BT: 92.9 vs. 92.6) to be within one standard deviation. Without multiple runs or statistical tests, readers cannot assess whether the reported differences are meaningful. Given the paper's strong claims, this is a significant omission.

- **The Spectral Perturbation Augmentor (SPA) experiment (Section 7.2) is conceptually interesting but poorly executed and reported.** The paper introduces r_SPA as an "empirically negligible ratio" and d_SPA as spectral divergence, but provides no numerical values, no explanation of how a negligible r_SPA can produce a large d_SPA without meaningfully changing the topology, no dataset or framework details for the experiment, and no quantitative results—only Figure 3, which is a qualitative figure without error bars. The claim that "performance is still comparable" is vague and unsupported. This experiment could provide strong causal evidence, but in its current form it does not.

### Minor

- **The argument that shallow GNN encoders (1-2 layers) "cannot meaningfully leverage spectral information" (Section 4) is insufficiently substantiated.** The paper shows that deeper encoders degrade performance (Figure 1), but this could be explained by overfitting, oversmoothing, or optimization difficulties rather than inability to capture spectral properties. The reasoning that limited receptive fields prevent spectral encoding is plausible but asserted rather than tested. Moreover, SPAN itself uses a 2-layer GCN encoder, partially undercutting the argument. The degeneration analysis (Section 7.1) provides more direct evidence, but it tests only one framework (G-BT) and one augmentation (DROPEDGE).

- **The ablation studies (Section 6.3) are described too briefly** — they reference "Table 1" and "Table 2" for the layer and encoder type ablations respectively (which are not accessible in the extracted text), and no numerical results are presented in the body text. The ablation on encoder type (GAT, GPS) would be more convincing with quantitative results shown.

### Trivial
None.

---

## Nice-to-Haves

- A theoretical or intuitive explanation for *why* edge dropping works best for node-level tasks while edge adding works best for graph-level tasks. This is an interesting empirical pattern that the paper does not attempt to explain.
- Re-implementing SpCo or GASSER under the same controlled conditions would substantially strengthen the generalization of the claims, though the paper correctly acknowledges the practical constraints preventing this.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about code availability at review time ("not verifiable"):** Removed per hard rule — questioning the existence/release status of artifacts the paper cites is not permitted. The paper states code will be released. This carries no weight in evaluation.

- **Criticism that the paper should have included OGBN datasets:** The paper explicitly states why these are excluded (spectral methods cannot scale), so this is scope-creep. Removed per soft rule about evaluating within stated scope.

- **Generic "the evaluation lacks rigor" framing without specific anchor:** The harsh critic's concern about "misleading" inclusion of GASSER/SpCo numbers, when the paper marks them with † and explains the limitations, was softened. The paper is transparent; the real issue is the claim-vs-evidence mismatch (already captured as a Major weakness above).

- **Strength about SPA providing "direct causal test":** The Strength Finder overstates this. The SPA experiment is a clever idea but too poorly executed/reported to count as a clear strength. Demoted.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface genuinely novel observations that the paper itself does not already make.

---

## Suggestions

1. **Align the claims with the evidence.** Reframe the central claim from "spectral augmentations are unnecessary" to "SPAN, a prominent spectral augmentation method, does not outperform simple edge perturbation under fair comparison." Or, if the broader claim is retained, clearly delimit its scope (e.g., "among spectral augmentation methods with available code that can be fairly compared").

2. **Add variance reporting.** Report means and standard deviations over at least 5 random seeds for all main experiments. This is essential for the reader to assess the reliability of the observed performance differences.

3. **Improve the SPA experiment.** Provide (a) numerical values for r_SPA and d_SPA, (b) an explanation of how a small edge perturbation rate can produce a large spectral divergence, (c) results with error bars, and (d) specify which datasets and frameworks were tested.

4. **Strengthen or reframe the shallow-encoder argument.** A direct probe (e.g., training a predictor on eigenvalues of representations, or checking whether spectral similarity of augmented views correlates with downstream performance) would be more convincing than the current depth-vs-performance plot.

5. **Include quantitative ablation results** in the main text rather than referencing inaccessible tables, especially for the encoder-type (GAT, GPS) ablation.

6. **Acknowledge limitations more explicitly** in the conclusion rather than restating the broad claim without hedging.

---
