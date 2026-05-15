Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper presents UNITIGBIN, a metagenomic contig binning tool that applies graph neural networks directly to **unitig-level** assembly graphs (rather than simplified contig-level graphs), while incorporating heterophilous constraints from single-copy marker genes. The pipeline has four stages: Learning (diffusive encoder with triplet Gaussian constraints and a p-batch parallelization strategy), Matching (initial bin assignment via greedy matching), Propagating (constraint-aware label propagation), and Refining (splitting/merging bins). Experiments across 12 datasets (simulated and real, from two assemblers) with 8 baselines show consistent improvements in bin quality.

---

## Strengths

- **First GNN applied to unitig-level assembly graphs for binning** — The paper provides clear evidence that prior graph-based binners (GraphBin, GraphMB, RepBin, MetaCoAG) operate on reconstructed contig-level graphs, which lose connectivity resolution. The paper explicitly documents this gap and fills it. (Lines 12, 16)

- **Consistent outperformance across a broad evaluation** — UNITIGBIN achieves higher HQ bin counts than all 8 baselines on both metaSPAdes-assembled datasets (76 vs. 69 on Sim100G, 21 vs. 17 on COPD) and metaFlye-assembled real WWTP datasets (1,775 vs. 962 bins meeting criterion A — a 45.8% gap). The advantage is consistent across all 12 datasets, not cherry-picked. (Tables 1, Figure 4)

- **Comprehensive baseline coverage and evaluation setting breadth** — The paper compares against 8 diverse tools (traditional, deep learning, graph-based) across datasets from two assemblers (metaSPAdes and metaFlye), using both CheckM (real data) and AMBER with ground truth (simulated data). This is an unusually thorough evaluation for the binning literature. (Section 4)

- **Novel p-batch strategy for scaling** — Training GNNs on unitig-level graphs (millions of nodes) requires batching that preserves contig completeness and positive relationships. The p-batch module addresses this with an iterative graph-splitting approach and a dedicated loss for joint-unitigs across batches. This is a genuine engineering contribution that enables the unitig-level approach to scale. (Section 3.1.3)

- **Ablation and parameter sensitivity studies** — The ablation (Figure 6) verifies that each component (Learning, Matching, Propagating, Refining) contributes positively. Parameter sensitivity analysis (Figure A3) shows low sensitivity to key hyperparameters, indicating robustness. (Section 4.3)

---

## Weaknesses

### Fatal
None.

### Major

- **Short-contig confound in simulated data comparison is not controlled** — The paper states that UNITIGBIN bins contigs <1,000 bp while other tools "typically discard" them (lines 143–144). On Sim20G, UNITIGBIN reports sequence-level F1=0.952 vs. MaxBin2's 0.632. If baselines were run with default filtering (discarding short contigs), they receive zero credit for thousands of contigs that UNITIGBIN bins, potentially inflating the performance gap. The paper does not specify whether baselines were run with modified settings to include short contigs, nor does it stratify results by contig length. This is a significant evidential gap because the claim of "significantly surpasses state-of-the-art" depends in part on this comparison. *Mitigation: run all baselines on the same contig set (including short contigs) or provide length-stratified results.*

- **Lack of statistical significance / error bars** — All metrics are reported from single runs. Since UNITIGBIN involves non-deterministic deep learning components, single-run results are insufficient to establish the significance of the reported improvements. This is a standard expectation for deep learning papers. (Tables 1, 2, Figure 4)

### Minor

- **The shared-marker-gene evaluation concern is acknowledged but not fully resolved** — The paper notes that CCVAE is circular (using CheckM for both constraints and evaluation) and claims to address this by using FragGeneScan+HMMER instead (lines 158–159). However, both FragGeneScan/HMMER and CheckM detect single-copy marker genes, and the paper provides no analysis showing the two marker gene sets are disjoint or that the evaluation is robust to any overlap. This does **not** invalidate the results — simulated data (AMBER with ground truth) avoids the issue entirely, and the practice is standard in the field (MaxBin2, MetaCoAG, and other baselines all use marker genes and are evaluated with CheckM) — but a controlled analysis (e.g., splitting marker gene sets) would strengthen the real-data claims.

- **The p-batch description in the main text is underspecified** — The description "selecting the largest contigs sets from the candidates, and feeding them into the smallest batch" (line 96) is vague without the pseudocode in Algorithm 1 (appendix). The method is likely reproducible from the appendix, but the main text could be clearer.

- **Benefit of unitig-level vs. contig-level graph is asserted but not directly quantified** — The paper's core motivation is that unitig-level graphs preserve higher-resolution connectivity. However, there is no controlled experiment comparing UNITIGBIN against a contig-level version of the same pipeline. The comparison against existing contig-level binners is confounded by many other differences (architecture, loss functions, etc.). An ablation replacing the unitig graph with a contig-level graph would directly validate this claim.

- **No code or trained model availability statement** — Given the complexity of the pipeline (FragGeneScan, HMMER, GNN training, p-batch, matching/propagating/refining), public code is essential for reproducibility. The paper does not state whether code will be released.

### Trivial
None.

---

## Nice-to-Haves

- Provide a stratified analysis of binning performance by contig length (<1,000 bp vs. ≥1,000 bp) on simulated data.
- Report mean and standard deviation over 3–5 runs for the main metrics.
- Include a contig-level version of the same pipeline as an ablation to quantify the benefit of unitig-level graphs.
- Release code publicly.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about p-Batch being insufficiently specified for reproducibility** — The reviewer claimed the description was too vague to reproduce without algorithmic details in the main paper. However, the paper references "Algorithm 1" (line 85) and states "Refer to Algorithm 1 for pseudocode" (line 98), which the appendix contains. Per the review guidelines, weaknesses about content deferred to the appendix (stripped by the parser) are removed.

- **Criticism about FragGeneScan/HMMER and CheckM using the "same universal single-copy marker gene sets"** — This claim goes beyond what the reviewer can establish. FragGeneScan uses TIGRFAM HMM profiles for gene prediction; CheckM uses lineage-specific marker gene sets (e.g., the 56 bacterial markers). These are different databases maintained by different groups. The paper explicitly addresses the concern by using a different pipeline (FragGeneScan+HMMER) than CheckM, following the same practice as MaxBin2 and MetaCoAG. The simulated data evaluation (AMBER with ground truth) is entirely free of this concern and still shows strong results.

- **Criticism about "Figure 6 reference is broken (just '7).')"** — This is a parser artifact from PDF extraction; the original paper's figure reference is intact.

- **Criticism about the Matching algorithm being "described qualitatively" with pseudocode in the appendix** — Same as p-Batch: the pseudocode exists in the appendix but was stripped by the parser.

- **Criticism about runtime comparison being "only on one dataset"** — While the runtime comparison is on a single dataset (Sim100G), this is standard practice in the binning literature. The comparison still shows UNITIGBIN is competitive (second-fastest among deep learning methods).

- **Strength claiming "first GNN modeling of unitig-level assembly graphs"** — This is a genuine claim supported by the paper. It is kept. (Not removed, but clarified here.)

---

## Novel Insights

The most interesting observation is the **asymmetry between the unitig-level approach and the constraint-based evaluation concern**. The paper's strongest contribution — modeling unitig-level graphs — is conceptually orthogonal to the marker gene constraints. A reader might expect the main advantage of unitig-level graphs to come from better connectivity information (homophily), not from constraints (heterophily). Yet the paper optimizes both simultaneously. This raises an underexplored question: *which part of the performance gain comes from better graph resolution, and which from better constraint handling?* The ablation study (Figure 6) begins to address this but does not separate these two effects cleanly. A version of UNITIGBIN using a contig-level graph with the same constraint framework would help disentangle the contributions.

---

## Suggestions

1. **Control the short-contig comparison**: On simulated datasets, run all baselines on exactly the same contig set (including contigs <1,000 bp) and report both overall and length-stratified metrics. This is the single most important experiment to address the major weakness.

2. **Report multiple runs with standard deviations** for the main tables (Table 1, Table 2, Figure 4). Even 3 runs would be sufficient to demonstrate that the improvements are not due to stochastic variation.

3. **Quantify the unitig-level advantage**: Implement a contig-level variant of your pipeline (convert the unitig graph to a contig graph using a standard strategy) and compare directly. This would directly validate the paper's core motivation.

4. **Publish code**: The pipeline involves multiple interdependent stages (graph disentangling, p-batch, triplet Gaussian constraints, matching, propagation, refinement). Public code would dramatically increase the paper's impact and reproducibility.

5. **Clarify whether baselines were run with default or modified filtering** for short contigs. If default filtering was used, explicitly acknowledge this as a limitation and quantify its effect.

---

## Score and Decision

This paper makes a genuine contribution to metagenomic binning by being the first to apply GNNs directly to unitig-level assembly graphs. The evaluation is unusually thorough in breadth (12 datasets, 8 baselines, two assemblers). The core results on simulated data (which avoids the evaluation circularity concern entirely) are strong and support the method's promise. The proposed p-batch strategy is a practical contribution to scaling GNNs on large assembly graphs.

The paper's most significant weakness is the uncontrolled short-contig comparison. The magnitude of the reported improvements on simulated data is likely inflated because baselines discard short contigs that UNITIGBIN bins. This is an evidential gap, not a fatal flaw — the paper still shows advantages even at the nucleotide level (AMBER metrics), and the real-data results are consistent. However, the authors should address this with additional analysis.

On balance, the paper merits acceptance at a competitive venue subject to the short-contig analysis being addressed. The idea is sound, the technical design is coherent, and the evaluation is broad. The weaknesses are substantial but addressable.

**Originality**: 7/10 — First to apply GNNs at the unitig level; the architecture itself adapts existing components (diffusion, triplet loss).  
**Importance of research question**: 8/10 — Metagenomic binning is an important problem; working at unitig level is well-motivated.  
**Claims well supported**: 6/10 — Strong but the short-contig confound and lack of error bars weaken support.  
**Soundness of experiments**: 6/10 — Broad but missing key controls.  
**Clarity of writing**: 6/10 — Clear overall but some algorithmic descriptions are vague.  
**Value to the community**: 7/10 — If released, UNITIGBIN would be a useful tool and the unitig-level direction is promising.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>