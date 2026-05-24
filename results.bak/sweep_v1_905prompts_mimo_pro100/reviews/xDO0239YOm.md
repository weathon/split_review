## Summary

HYPOGENEAGENT proposes an LLM-driven framework for selecting clustering resolution in single-cell/Perturb-seq data. An LLM agent generates ranked GO-based hypotheses for each cluster's gene signature; these are embedded and combined into a Resolution Score (RS) that balances intra-cluster annotation agreement (ICS) with inter-cluster distinctiveness (ICD). The optimal resolution maximizes RS. The paper applies this to a K562 Perturb-seq dataset at both gene-expression and perturbation levels, and benchmarks against silhouette, modularity, and functional enrichment analysis.

## Strengths

- **Genuine conceptual novelty in closing the annotation-resolution loop.** The paper identifies a real gap — existing pipelines perform resolution selection and functional annotation as disconnected steps — and proposes a concrete metric (RS = w·ICS + (1-w)·(1-ICD)) to bridge them. This is formally defined in Section 3.4 and Table 1.

- **Thorough Stage 1 ablation on the gene-set annotation sub-task.** The paper systematically benchmarks 5 LLMs (GPT-4o, GPT-o3, GPT-5, Gemini-2.0-flash, Gemini-2.5-pro), 3 embedding methods, 2 prompt versions, and temperature sweep [0,1] on 100 curated GOBP sets (Section 4.3, Figures S1–S3). This establishes that the chosen configuration (GPT-o3 + hypothesis prompt + OpenAI embedding) is evidence-based rather than arbitrary, and Figure S1d demonstrates that the LLM's self-ranked confidence correlates with semantic accuracy.

- **Internal convergence of component metrics.** At the GEX level, both ICS (peaking at 0.4, Figure 3d) and ICD (lowest at 0.4, Figure 3c) independently converge on the same resolution as the combined RS (Figure 3a). An identical pattern holds at the perturbation level (Figures 4c,d both indicating 0.5). This internal consistency across independently computed quantities is a positive signal.

- **Dual-level application** demonstrating the framework works on both gene-expression clusters (marker gene signatures) and perturbation-level clusters (perturbed gene labels), with coherent results at both levels.

## Weaknesses

### Fatal

None.

### Major

- **The enrichment-based validation undermines, rather than supports, the paper's claims.** The paper presents functional enrichment analysis (Section 4.4.3) as independent validation that HypoGeneAgent's resolution selection is "biologically coherent." However, the figure caption for Figure 6 explicitly states: *"In (a), the resolution score peaks at 0.7."* The text then claims "the selected resolution can be 0.5 or 0.4, which is consistent with our previous selection with HypoGeneAgent" — but this relies on an overridden criterion ("consider the reasonability of cluster numbers we expected"), not on the enrichment score itself. The enrichment RS peaks at 0.7 while HypoGeneAgent selects 0.4 (GEX) and 0.5 (perturbation). The paper misrepresents this discrepancy as validation. This is the most significant issue because it was supposed to be the key independent check.

- **No ground-truth validation of resolution selection.** The Perturb-seq data contains known perturbation labels that provide natural ground-truth groupings. The paper never computes whether HypoGeneAgent's selected resolution (r=0.4) maximizes recovery of perturbation-to-cluster assignments, nor does it report any metric that directly tests whether the selected resolution recovers known biology. The only "validation" is a UMAP visualization (Figure 3b) described as showing "nine well-separated clusters," which is not a quantitative assessment and would look plausible at many resolutions.

- **Resolution Score measures LLM self-consistency, not biological validity.** RS is a function of how similar the LLM's 5 hypotheses are to each other within clusters and how different they are across clusters. A high score means the LLM produces internally coherent and mutually distinct descriptions — but this is a property of the LLM's generation behavior and the vocabulary overlap in GO terms, not necessarily of biological reality. The paper does not establish that LLM annotation consistency is a reliable proxy for cluster quality.

- **Single-dataset validation.** The entire Stage 2 evaluation rests on one public dataset (K562 Perturb-seq from Replogle et al. 2022) evaluated at one resolution grid (10 values from 0.1 to 1.0). There are no synthetic datasets with known ground truth partitions, no additional cell lines, no cross-validation, and no statistical significance testing. For a methods paper whose contribution is a resolution selection framework, this is insufficient.

### Minor

- **Comparison with baselines is asymmetric.** Silhouette and modularity operate on the original feature/graph space without biological annotations. HypoGeneAgent incorporates biological knowledge through GO/KEGG retrieval. The expected advantage is partly built into the comparison design. A more informative comparison would be against other biology-aware approaches at equal information access — but the paper's own enrichment analysis (which is biology-aware) is poorly presented as noted above.

- **No cost or runtime analysis.** The method requires multiple LLM API calls (5 hypotheses × clusters × resolutions). For the single K562 dataset this is manageable, but the conclusion claims applicability to "millions of cells" and "whole-genome CRISPR screens" without substantiation.

- **ICD naming confusion.** The metric labeled "Inter-cluster distinctiveness" is defined as mean cosine *similarity* (lower = more distinctive). The RS formula then uses (1 - ICD). While internally consistent, this naming invites confusion. This is a presentation issue, not a correctness issue.

- **Weight parameter w = 1/3 is under-supported.** The paper states it was "chosen by a small grid search and found to give a stable ordering," but the search procedure and stability analysis are not shown in the main text.

### Trivial

None.

## Nice-to-Haves

- Use the Perturb-seq perturbation labels as ground truth to compute recovery metrics (e.g., adjusted mutual information between clusters and known perturbation groups) at each resolution.
- Provide a head-to-head comparison between HypoGeneAgent's RS and the enrichment-based RS with confidence intervals across multiple datasets.
- Report sensitivity analysis of RS to the number of marker genes, embedding model choice, and LLM backbone.
- Include cost/runtime characterization to substantiate scalability claims.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Circular evaluation" framing:** The harsh critic frames the evaluation as circular because the same LLM is used for annotation and for scoring. This is partially valid but overstated — the Stage 1 benchmark uses curated GOBP ground truth, and the enrichment analysis is independent (though poorly presented). The core problem is better captured as "no ground-truth resolution validation" and "enrichment score discrepancy."

- **Criticism about "objective" being misleading:** The paper uses "objective" to describe the resolution selection process. While the LLM outputs are probabilistic, the RS formula is indeed a deterministic, quantitative criterion — calling it "objective" in the sense of "automated and reproducible" is reasonable hyperbole, not a factual error.

- **Criticism about Stage 1 conflation with Stage 2:** The harsh critic notes that Stage 1 validates annotation accuracy while Stage 2 uses annotation consistency for resolution selection, and these are "logically independent claims." This is technically true but somewhat pedantic — if the LLM cannot annotate gene sets accurately, annotation consistency is meaningless, so Stage 1 is a necessary (if not sufficient) condition.

- **Criticism about w=1/3 grid search not shown:** Partially addressed — the paper states the grid search was done. Detailed analysis deferred to appendix (which the parser strips). This is a minor transparency issue, not a methodological flaw.

- **Criticism about Figure 3a discrimination being "modest":** The harsh critic notes medians range "roughly 0.3–0.75." This is actually a meaningful range for a continuous metric and represents reasonable discrimination across resolutions.

## Novel Insights

A genuinely novel observation from this review: the enrichment-based resolution score in Figure 6a peaks at 0.7, not 0.4–0.5 as HypoGeneAgent selects. The paper acknowledges this inconsistency only indirectly by invoking "reasonability of cluster numbers" — a subjective override that contradicts the paper's own stated goal of eliminating subjective resolution tuning. This suggests either (a) the LLM agent and traditional enrichment analysis actually disagree about optimal resolution, or (b) the RS framework requires secondary heuristics to produce reasonable results. Either interpretation weakens the paper's central claim.

## Suggestions

1. **Use perturbation labels as ground truth.** The K562 Perturb-seq data naturally provides perturbation-to-cluster ground truth. Compute ARI/AMI between clusters and known perturbation groups at each resolution, and show that HypoGeneAgent's selected resolution maximizes this metric (or at least outperforms silhouette/modularity selections).
2. **Honestly report the enrichment score discrepancy.** Either argue why the enrichment RS peak at 0.7 is wrong, or revise the claimed validation to acknowledge the discrepancy. The current presentation misleads readers.
3. **Add at least one additional dataset** (e.g., another cell line from the same Perturb-seq study, or a public PBMC dataset) to demonstrate generalizability.
4. **Characterize cost and runtime** to support scalability claims made in the conclusion.

## Anchoring Report

**Round 1 bracketing anchors:**
- Weak (avg < 3.5): scMPT (3.40), DrugAgent (2.50), "No Factor Left Behind" (3.00), LLM for KG Construction (3.00)
- Middle (avg 3.5–7.5): ZerOmics (4.67), CellPLM (6.50, accept), LLM4GRN (4.33), sCellTransformer (4.50)
- Strong (avg > 7.5): GeSubNet (8.00), LLM-SR (8.00), Protein Discovery (8.00), Synthetic Continued Pretraining (8.00)

**Round 2 narrowing anchors:**
- Lower band (avg 3.0–5.5): GenoAgent (4.00, reject), LLM4GRN (4.33, reject), ZerOmics (4.67, reject)
- Upper band (avg 5.0–7.0): DNA LMs for RNA (5.33, reject), DNALONGBENCH (5.67, reject), MTGRN (5.75, reject), RNA Splicing (5.50, reject)

**Bracket and comparison:** Round 1 placed the paper between 3.5 and 7.5. Round 2 narrowed to the 4.0–5.0 range. Compared to GenoAgent (4.00), HypoGeneAgent has a more novel formal contribution and better ablation work, but worse validation (enrichment score discrepancy). Compared to LLM4GRN (4.33), it has a more focused methodological contribution but similar limitations in validation scope. Compared to DNA LMs for RNA (5.33), it has weaker experimental breadth. The enrichment score discrepancy is a distinctive flaw not present in these anchors. Final score: **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>