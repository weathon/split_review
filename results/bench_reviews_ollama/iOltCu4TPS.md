Now I have read the full paper. Let me carefully synthesize the final review by verifying each claim against the actual text.

## Summary

This paper presents the first comprehensive benchmark of 12 single-cell retrieval methods spanning three classes: non-ML methods (CellFishing.jl, scFind), VAE-based methods (scVI, LDVAE, CellBlast, scmap), and single-cell foundation models (SCimilarity, scGPT, UCE, scFoundation, Geneformer, scMulan). The evaluation covers cross-platform, cross-species, and cross-omics retrieval settings, using both label-dependent metrics (Vote-Acc, Avg-Acc, BatchDiv, Recall) and novel label-free metrics (AvgOverlap and DE gene consistency). The key findings are that top scFMs outperform other methods in most settings but fail when species and omics are both distant from pre-training data, non-ML baselines remain competitive, and label-free metrics correlate well with label-dependent ones.

## Strengths

- **First systematic cross-class comparison of single-cell retrieval methods.** The paper evaluates all three method classes (non-ML, VAE-based, scFM-based) in a unified framework across cross-platform, cross-species, and cross-omics settings. Tables 1–3 provide the full comparative results, filling a genuine gap where prior work (SCimilarity, CellFishing.jl) was evaluated only in narrow configurations.

- **Important negative result on cross-omic retrieval.** The Recall metric for cross-omic exact-match retrieval (Section 3.2.1) provides unambiguous ground truth. The finding that all methods barely exceed random baseline (Section 4.3, Table 3) is a genuinely valuable negative result, demonstrating that identifying matching cells across omics remains a fundamental challenge.

- **DE gene consistency analysis goes beyond cell identity overlap.** The Jaccard similarity analysis of DE genes from retrieved cells (Figure 3, Section 4.4) captures semantic biological similarity rather than just cell index overlap, providing a more substantive evaluation than simple retrieval set agreement.

- **Non-ML baselines are surprisingly competitive.** CellFishing.jl ranks competitively with top scFMs on human PBMC (Table 1) and shows only ~10% gap behind the best scFM in cross-species retrieval (Table 2), which is a practically important finding for method selection.

- **Multi-species pre-training does not yield proportional cross-species gains.** UCE, the only multi-species pre-trained scFM, does not significantly outperform human-centered scFMs (SCimilarity, scFoundation) in human-mouse retrieval (Table 2, Section 4.2), raising important questions about current pre-training strategies.

## Weaknesses

### Fatal
None.

### Major

- **Unequal training conditions between method classes confound comparative interpretation, particularly for cross-omic conclusions.** VAE-based methods (scVI, LDVAE, CellBlast) are trained on the evaluation reference data, while scFM-based methods are used zero-shot (Section 3.3.1: "the foundation models are used in a zero-shot manner without additional tuning to avoid bias"). This design is defensible as reflecting practical usage, but the paper's interpretive claims overreach what the comparison supports. Most critically, on mouse cross-omic datasets (Table 3), the paper attributes scFM failure to "the large gap between the pre-training corpus of scFMs and the testing omic and species" (Section 4.3) and concludes that "VAE-based methods such as scVI and LDVAE are good alternatives" when target data is distant (Section 6). These conclusions cannot distinguish whether scFMs fail due to architecture/domain-gap limitations or simply because they lack access to target data that VAE methods have. The recommendation about VAE alternatives is therefore only conditionally supported—valid for the specific usage scenario tested (zero-shot scFM vs. fine-tuned VAE) but not for the stronger architectural claim the paper makes.

- **AvgOverlap as a label-free metric measures consensus, not correctness.** The AvgOverlap metric (Section 3.2.2) quantifies overlap between retrieval sets across methods. Its correlation with Vote-Acc (Figure 2c) demonstrates that top-performing methods tend to agree, but this does not establish that agreement implies correctness. A method that accurately captures rare cell states missed by consensus would receive a low AvgOverlap despite being correct. The "voting theory" justification (Section 3.2.2) assumes methods have approximately independent errors, which is not demonstrated and is unlikely given overlapping pre-training corpora among scFMs. The paper partially mitigates this by also proposing DE gene consistency (which captures semantic similarity), but the core interpretive claim—that AvgOverlap can "be employed in a broader scenario" as a proxy for correctness—is overstated without evidence about when and how it fails.

### Minor

- **BatchDiv as a standalone quality metric is potentially misleading.** The BatchDiv metric (Section 3.2.1) equates higher batch diversity with better retrieval quality. However, random retrieval would maximize batch diversity, and a method that correctly retrieves biologically similar cells from one dominant batch would score low. The claim that scFMs "can better find cells across different experiment platforms" based on high BatchDiv (Section 4.1) does not rule out that scFM embeddings may simply have less batch discriminability (which could reflect either good batch integration or collapsed representations). The paper presents BatchDiv alongside Vote-Acc, which partially addresses this, but does not condition diversity on accuracy or acknowledge the trade-off.

- **Preprocessing confound acknowledged but insufficiently discussed.** Section 3.3.3 states "we adopt the default pre-processing method of each method respectively to avoid bias," but using method-specific preprocessing could introduce its own bias. For example, scGPT uses 4000 HVGs while scFoundation uses all genes. No ablation controls for preprocessing differences, and the framing that defaults "avoid bias" is questionable since it trades one potential bias for another. This is a standard benchmarking decision and thus minor, but the paper should acknowledge the trade-off.

- **Speculative biological claims without validation.** The claim that sub-groups identified in DE gene patterns "may correspond to certain unannotated sub-types of CD4+ T cells" (Section 4.4) is speculative without validation against known sub-type markers or independent data.

### Trivial
None.

## Nice-to-Haves

- A fine-tuned scFM condition on at least one cross-omic/mouse dataset would strengthen the interpretive claims about domain gap vs. training access, though this is scope-expanding and not required for the current contribution.
- Conditional analysis showing whether BatchDiv correlates with accuracy among methods at similar Vote-Acc levels would validate BatchDiv's interpretation as a quality metric.
- Analysis of specific query cells where top methods disagree with consensus (failure cases of AvgOverlap) would clarify the metric's limitations.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Not yet released" / availability concerns about any cited models, tools, or datasets**: Removed per hard rule. All cited entities are assumed to exist and be available.
- **Missing variance across random seeds for VAE methods**: While technically valid, this is a reproducibility nitpick that is not standard practice in large-scale benchmarking. Removed as trivial reproducibility concern.
- **Claims about missing related works or appendix content**: Removed per hard rules, as the parser strips appendices and we cannot verify external references.
- **Introduction "overstates novelty" of label-free evaluation**: The paper does not claim to invent consensus-based evaluation; it proposes specific metrics (AvgOverlap, DE gene consistency) for the cell retrieval context. This is a valid extension of prior ideas, not an overstatement.
- **Cross-species gene homolog mapping as a "simplification"**: Using one-to-one ortholog mapping is the standard and well-justified approach for human-mouse comparison. The paper explicitly acknowledges that generalization to distant species without explicit homolog mapping "still remains an open problem" (Section 4.2), addressing this concern.
- **Formatting/typo complaints**: Removed per hard rules.

## Novel Insights

The paper's finding that non-ML methods remain competitive with or even outperform scFMs in several settings challenges the prevailing assumption that foundation models uniformly dominate retrieval tasks. More strikingly, the near-random performance of all methods on cross-omic exact-match retrieval (Table 3) suggests that current embeddings—even those trained on the target data for VAE methods—fail to bridge the modality gap for cell-level matching, indicating that the problem may require fundamentally different approaches (e.g., cross-modal contrastive learning) rather than better unimodal representations. The disconnect between scFMs' strong cross-platform and cross-species performance versus their near-random cross-omic performance maps a clear boundary of foundation model generalizability that prior benchmarks had not delineated.

## Suggestions

- Qualify the cross-omic conclusions to acknowledge that VAE superiority may reflect training access rather than inherent architectural advantages, and explicitly state that the recommendation for VAE alternatives applies specifically to the zero-shot vs. fine-tuned comparison tested.
- Add a brief discussion of when AvgOverlap may fail (e.g., rare cell states, methods with correlated errors) alongside its validation, to help readers assess its reliability as a proxy.
- Clarify in Section 3.3.3 that method-specific preprocessing is a design choice that trades off between fairness (each method at its best) and controllability (isolating model quality from preprocessing), rather than claiming it "avoids bias."

## Score and Decision

The paper makes a genuine contribution as the first comprehensive benchmark of single-cell retrieval methods, with important empirical findings (scFM failure modes, competitive non-ML baselines, cross-omic near-random performance). The two major weaknesses—the confounded training access comparison and the overreach of AvgOverlap as a correctness proxy—qualify but do not invalidate the core empirical contributions. The results are informative even with these caveats; the paper simply needs to temper its interpretive claims. The cross-omic recall finding alone is a valuable contribution.

**Originality**: The first systematic cross-class benchmark for single-cell retrieval. Solid but incremental methodology.  
**Importance**: Timely and practically important; single-cell retrieval is an increasingly critical problem.  
**Claims support**: Partially undermined by training confound and metric limitations; empirical results stand but interpretation needs qualification.  
**Experimental soundness**: Good coverage of settings and methods; standard preprocessing, adequate dataset selection.  
**Clarity**: Well-organized and clearly written; metrics well-defined.  
**Community value**: High—will serve as a reference point for future method development.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>