- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 5, 8, 5, 3, 6
Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

This paper presents the first comprehensive benchmark of 12 single-cell cell-retrieval methods spanning three classes (2 non-ML, 3 VAE-based, 7 scFM-based), evaluated across cross-platform, cross-species, and cross-omics settings using both standard label-dependent metrics (Vote-Acc, BatchDiv, Recall) and two newly proposed label-free metrics (AvgOverlap, DE gene consistency). The key findings are that top scFMs (UCE, scFoundation, SCimilarity) show overall advantage but struggle on distant species/omics, traditional non-ML methods remain competitive, and label-free metrics correlate with label-dependent ones, enabling evaluation when cell-type annotations are unavailable.

## Strengths

- **First systematic comparison of scFMs against non-scFM and VAE-based methods under identical settings.** The paper explicitly identifies the gap ("there is no direct comparison between scFMs and other methods in existing works") and fills it with 12-method comparisons across Tables 1–3, covering settings the individual method papers never tested (e.g., cross-species, cross-omics).

- **Novel label-free evaluation metrics (AvgOverlap, DE gene consistency) with empirical validation.** Section 3.2.2 defines these metrics, and Figure 2c shows strong correlation between AvgOverlap and Vote-Acc across four datasets — a practical result that enables evaluation when cell-type annotations are unreliable or unavailable, which is a known limitation in the field.

- **Cross-omics recall metric and revealing negative results.** Section 3.2.1 defines Recall_K for paired multi-omics data, and Table 3 reports the important finding that all methods perform near random on mouse multi-omics datasets — a concrete boundary condition for scFM applicability that prior individual evaluations missed.

- **Traditional non-ML method (CellFishing.jl) validated as a competitive baseline.** CellFishing.jl outperforms several scFMs in certain settings (e.g., cross-species mouse-to-human in Table 2), challenging the default assumption that deep learning methods are always preferable for cell retrieval — a practically useful finding.

- **Per-cell batch diversity metric adapted for retrieval evaluation.** Section 3.2.1 defines BatchDiv at the per-cell level using entropy of batch labels in retrieved sets, distinguishing it from global metrics like kBET and adapting it specifically to the retrieval setting.

## Weaknesses

### Fatal
None.

### Major

- **No uncertainty quantification on any reported result.** All Tables 1–3 report point estimates with no error bars, standard deviations, confidence intervals, or indication of multiple runs. VAE-based methods (scVI, LDVAE, CellBlast) involve stochastic initialization and mini-batch sampling, so their embeddings are random quantities. Even the Faiss IVF training for dense retrieval introduces randomness. The paper makes strong ranking claims ("UCE, scFoundation and SCimilarity show substantial overall advantage"), but the reader cannot judge whether observed differences of a few percentage points between adjacent methods are reliable or within noise. For a paper positioned as a definitive benchmark, this is the most significant weakness.

- **Complete omission of computational efficiency.** The paper defines cell retrieval as a search problem across large databases, yet provides no runtime, memory usage, indexing time, or throughput comparison for any of the 12 methods. A method that is 90% as accurate but 100× faster may be preferable in practice. The paper's own recommendation that "traditional non-machine learning methods should not be neglected" cannot be evaluated without this dimension. This is a concrete gap for a comprehensive benchmark.

- **Speculative claim about unannotated subtypes without supporting evidence.** Section 4.4 states that sub-groups identified by top methods "may correspond to certain unannotated sub-types of CD4+ T cells" and that "the cell DE sub-groups identified in common can be further explored and explained by biologists." No marker gene analysis, independent validation against known cell-state relationships, or any biological evidence is provided to support this interpretation. The observation of structured DE gene patterns is interesting, but the implication that they correspond to real biological subtypes is unsubstantiated as presented.

### Minor

- **Label-free metric validation is correlational without independent ground truth.** The validation of AvgOverlap (Figure 2c) shows correlation with Vote-Acc, but the paper's own motivation for label-free metrics is that cell-type annotations are "coarse-grained" and "can be biased or incorrect." If the annotations are indeed unreliable, correlation with them does not independently validate that the label-free metric measures retrieval correctness — it only shows that different methods' retrieval sets agree with each other and with noisy labels. The paper would be strengthened by validating against an independent biological gold standard (e.g., known cell-state markers). The correlation is still informative as a first step, but the claim that label-free metrics "can be employed in a broader scenario" is partially undercut by this circularity.

- **Batch diversity entropy formula has a notation error.** In Section 3.2.1, the entropy formula uses $\sum_{i=1}^{N_q} \mathbb{I}(b_{ik}=b_m) / N_q$ as the probability term, but for a per-query entropy the sum should be over $k=1$ to $K$ (retrieved cells) and the denominator should be $K$, not $N_q$. This is likely a typesetting artifact rather than an implementation error, but it should be corrected for clarity.

- **Missing a simple non-learned baseline.** The benchmark does not include cosine similarity on raw or log-normalized count vectors as a baseline. CellFishing.jl uses LSH on binarized counts, which is qualitatively different. A direct cosine-similarity baseline would provide a useful lower bound to calibrate how much improvement the methods actually provide.

- **Hyperparameter sensitivity for VAE methods not discussed.** The VAE-based methods use fixed latent dimensions (e.g., 10 for scVI, 10 for LDVAE). The paper does not discuss or ablate whether performance is sensitive to this choice, which could affect the relative rankings.

- **Cross-omics gene-activity mapping noise not quantified.** Section 3.3.3 describes mapping scATAC-seq peaks to gene space via gene regulatory potential from DeepMAPS. This preprocessing step injects noise that is not quantified or discussed as a potential confound in the cross-omics results.

### Trivial
- None that are not already covered in Minor.

## Nice-to-Haves

- Adding 3–5 random seeds for VAE-based methods and reporting mean ± std would transform the rankings from suggestive to trustworthy. A paired bootstrap or Wilcoxon test across query cells could establish significance.
- A runtime comparison on a single dataset (wall-clock retrieval time for a fixed database size, indexing time) would substantially increase the practical utility of the benchmark.
- Validating the DE-gene sub-group analysis against known cell-state markers (e.g., naïve vs. memory CD4+ T cell markers) would turn the speculative claim about unannotated subtypes into a genuine strength.

## Removed Points

These points were raised by the reviewers but are removed or demoted for the reasons stated:

- **"scVI/LDVAE are primarily embedding models, not retrieval methods"** — The paper accurately describes them as VAE-based methods used for generating embeddings, which are then used for retrieval. The critic's framing as a weakness is a categorization preference, not a flaw. Not included in Weaknesses.
- **"Reproducibility concern about codebase not being in manuscript"** — The parser strips supplementary materials and code links from all papers. Per instructions, this is a known artifact, not an author error. Removed.
- **"Batch effects underemphasized in problem definition"** — Too vague to constitute a specific weakness; the paper's problem definition is adequate for its scope. Removed.
- **"Related works missing"** — Not permitted to cite absent related works per instructions. Removed.
- **"Cross-omics results under-analyzed"** — The paper does analyze the failure on mouse multi-omics and attributes it to distribution shift. The critic's request for deeper analysis is a nice-to-have, not a weakness. Moved to implicit coverage in Minor.
- **"Formatting / style nitpicks"** — PDF extraction artifacts, not author errors. Removed.
- Several generic Strengths from the Strength Finder were removed (e.g., "this paper addressed an important problem") as generic/superficial. Only concrete, evidenced strengths are retained above.
- The DE gene strength about "biologically meaningful subgroups" is retained but caveated by the verified weakness about speculative unannotated-subtype claims.

## Novel Insights

The most interesting observation from the synthesis is that the paper's label-free metrics and label-dependent metrics are validated against each other, creating an internal consistency that is useful as a practical tool but insufficient as an independent proof of concept. The deeper issue — that the field lacks any ground-truth cell-pair relationship data to validate retrieval — is a structural problem the paper correctly identifies but does not solve. The correlation between AvgOverlap and Vote-Acc is best interpreted as evidence that method agreement and label agreement converge, not that either is correct. This suggests that the next step for the field is not another benchmark but a curated set of validated cell-state relationships (e.g., perturbation-matched cells, lineage-traced cells) to serve as ground truth.

## Suggestions

1. **Add variance estimates.** Run VAE-based methods with 3–5 random seeds and report mean and standard deviation. Include a note on whether differences between adjacent methods in the rankings are significant (paired bootstrap across query cells or Wilcoxon signed-rank test).
2. **Add a runtime comparison.** A single-table comparison of wall-clock retrieval time, indexing time, and memory footprint on one fixed dataset would address a major practical gap.
3. **Tone down or support the unannotated-subtypes claim.** Either replace "may correspond to unannotated sub-types" with a more measured statement about structured DE patterns, or validate against known sub-cell-type markers (e.g., CD45RA for naïve T cells, CD45RO for memory T cells).
4. **Acknowledge the circular validation limitation.** Add a sentence noting that the AvgOverlap–Vote-Acc correlation shows consistency but not independent correctness, and that validation against held-out biological signals would strengthen the claim.
5. **Fix the entropy formula notation** in Section 3.2.1 to use K (retrieved cells per query) as the denominator.
6. **Add a raw cosine-similarity baseline** on log-normalized counts for at least one dataset to calibrate improvement magnitude.
