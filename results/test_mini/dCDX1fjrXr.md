Now I have sufficient evidence. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the full consolidated review.

First, let me carefully verify the Section 4.2 vs Section 5.2 inconsistency one more time to make sure I'm being accurate.

Section 4.2 (lines 81-85):
"The second phase in our proposed pipeline is to select a label node set V_L to use for sparse labels classification. Here we chose a number of nodes l_H from the pseudo label class returned by the Label distribution estimation model. For every pseudo-label class H_{:,j} (where H_{:,j} is a column of H), the l_H nodes were chosen to be the nodes with the smallest loss used by the Label distribution estimation model (such as the loss ||F F^T - H H^T||). As the number of nodes needed for training increased beyond the number of clusters l_c, the rest of the labeled nodes l_R selected for training are selected at random. As such the total number of labeled nodes used for training is |V_L| = l = l_H + l_R."

Section 5.2 (lines 170-173):
"For the labels used, we randomly selected #num × c training nodes over the entire set of nodes V, where c is the number of unique classes and #num was varied from 1-4."

So the inconsistency is:
- Section 4.2: labeled nodes are partially selected from pseudo-label clusters based on confidence (l_H nodes) plus random (l_R nodes)
- Section 5.2: labeled nodes are purely random

These CAN be made consistent if l_H = 0 (i.e., no key nodes selection used), making all nodes random. But the paper never states this explicitly. The paper also says in Section 4 that the ELI framework has step (2) "key nodes selection as labeled nodes" - but the experiments use random selection.

This is a genuine issue. The paper should clarify.

However, the harsh critic's claim that this "invalidates the paper's central claim of a four-step framework for SLNC" is an overstatement. The central technical contribution is the incorporation of pseudo-label information via additional Laplacian terms (steps 3-5), not the key nodes selection (step 2). The experiments evaluate this core contribution.

Let me write the review now.Now I'll produce the final consolidated review.

## Summary

The paper formalizes the Sparse Labels Node Classification (SLNC) problem, where only a handful of randomly selected labels (not per-class) are available at training time—meaning some classes may have zero labeled examples. The authors propose ELI, a framework that first runs unsupervised graph clustering (AGC) to obtain pseudo-label assignments, then uses the resulting cluster structure to construct two additional Laplacian smoothness terms (over a pseudo-label graph and a true-label graph), which are averaged with the standard graph Laplacian to guide label propagation or a simplified GCN (SGC). Experiments on seven benchmarks show that LP-ELI and SGC-ELI outperform plain LP, SGC, DGI, GMI, and CGPN by 10–20% absolute accuracy when only 1–4×c random labels are available.

## Strengths

1. **Formalization of a practically relevant under-explored problem (SLNC).** The paper clearly defines a setting—extremely sparse, non-per-class random labels—where standard SSNC methods predictably fail. Figure 1 and Tables 3–4 document this failure (e.g., SGC achieves only 55.2% on Cora with 1 label×c), justifying the need for dedicated approaches.

2. **Consistent and substantial gains over baselines across 7 datasets.** The ELI-enhanced models deliver 10–20% absolute accuracy improvements over LP and SGC in the SLNC regime. For example, on Cora (#1 label×c): LP 53.3% → LP-ELI 65.4%; SGC 55.2% → SGC-ELI 69.5% (Table 3). Similar margins hold on Citeseer, Pubmed, Wiki, Computers, Photo, and Cs, with 10-run statistics reported.

3. **Principled generalization beyond label propagation to GNN architectures.** Section 4.5 shows that the average Laplacian \(L_A\) can replace the standard graph Laplacian as a graph filter in SGC, backed by a feature-denoising argument following Fu et al. (2020). SGC-ELI often outperforms LP-ELI (e.g., Cora #1: 69.5% vs 65.4%), demonstrating the framework applies to convolution-based models, not just propagation-based ones.

4. **Computational efficiency through sparse construction.** The paper replaces the dense \(H H^T\) pseudo-label adjacency with a KNN graph built from an SVD of the filtered features, yielding sparse matrices. Runtime comparisons are reported (Citeseer: LP-ELI 0.27s, SGC-ELI 2.18s vs CGPN >48s), showing practical feasibility.

## Weaknesses

### Fatal

None.

### Major

1. **Unexplained inconsistency between the described pipeline and the experimental protocol.** Section 4.2 ("Key Nodes Selection") describes selecting labeled nodes preferentially from high-confidence pseudo-label clusters, with only the remainder drawn at random. However, Section 5.2 states that labeled nodes are "randomly selected over the entire set of nodes." The paper never clarifies whether the key-nodes selection was actually used in the experiments. If it was used, Section 5.2 is inaccurate; if it was not used, then the method described as a four/five-step pipeline is only partially evaluated, and Section 4.2 describes a component whose effect on the results is unknown. This ambiguity goes beyond a presentation nitpick—it makes it impossible for a reader to determine precisely what was evaluated, and it undermines trust in the empirical results. The authors must resolve this and state explicitly what variant produced each reported number.

2. **Narrow baseline set relative to the strength of the claims.** The paper compares ELI only against LP, SGC, DGI, GMI, and CGPN. LP and SGC are basic methods that are expected to fail with ≤4 random labels; beating them is necessary but not sufficient to establish the method's significance. Many relevant approaches for extremely low-label regimes are neither compared nor convincingly ruled out: self-training with iterative pseudo-labeling on GCN features, consistency-regularization methods (e.g., Π-model, VAT adapted to graphs), transductive few-shot methods (which do not require per-class selection at test time), and other graph SSL techniques. Without these comparisons, the paper can claim that ELI improves over a few standard baselines, but not that it sets a new state of the art for SLNC.

3. **No analysis of the method's dependence on clustering quality.** The entire ELI framework assumes that the unsupervised clustering (AGC) produces pseudo-labels that are semantically meaningful. The paper provides no diagnostics—no clustering accuracy, NMI, or ARI for any dataset; no ablation where clustering is intentionally degraded (wrong number of clusters, shuffled assignments); no experiments on heterophilic graphs where enforcing smoothness on pseudo-label neighborhoods could be harmful. Since the clustering uses the known number of ground-truth classes, even a modest misalignment could propagate errors through the additional Laplacian terms. This gap makes it difficult to assess when the method would succeed or fail.

### Minor

1. **The three Laplacian terms are weighted equally (β₁=β₂=β₃=1/3) without justification or ablation.** No experiment separates the contribution of the graph-structure term, the pseudo-label term, and the true-label term. An ablation showing each term's individual effect would clarify which component drives the improvement and whether all three are needed.

2. **Evaluation is limited to homophilic graphs.** All seven datasets (Cora, Citeseer, Pubmed, Wiki, Computers, Photo, Cs) are homophilic or near-homophilic. The method's two key smoothness terms (graph Laplacian and pseudo-label Laplacian) both assume nearby nodes have similar labels. Testing on heterophilic graphs (e.g., Texas, Cornell, Wisconsin) would reveal whether the pseudo-label information helps or hurts when the original graph structure is adversarial.

3. **The paper references ablation and sensitivity studies in appendices (Section D.1) that are not present in the main text.** The reader cannot evaluate robustness to KNN neighborhood size, clustering stopping parameters, or label count without consulting material that was stripped from the submission. Key results from these studies should be summarized in the main paper.

### Trivial

None.

## Nice-to-Haves

- Adding comparisons to self-training and consistency-regularization baselines would substantially strengthen the empirical case.
- An analysis showing clustering accuracy (NMI/ARI) per dataset and correlating it with ELI gains would validate the core intuition.

## Removed Points

The following points from the harsh critic are removed or weakened as per the review rules:

- **"Fatal inconsistency ... invalidates the paper's central claim"** — downgraded from Fatal to Major. The inconsistency is real and serious, but the paper's central contribution (extra Laplacian terms derived from unsupervised clustering) is evaluated in the experiments regardless of whether key-nodes selection was used. The core claim is not invalidated, but the ambiguity is a significant flaw.
- **"Baseline set is too weak and narrow to support the claimed 10–20% improvement"** — retained as Major weakness #2. The critic's characterization is essentially correct.
- **"No analysis of dependence on clustering quality"** — retained as Major weakness #3.
- **"The paper cannot claim state-of-the-art performance"** — the paper does not explicitly claim SOTA; it claims 10–20% improvement over baselines. The criticism is kept but rephrased to match what the paper actually asserts.
- **Criticism about missing related works** — removed per rule: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."
- **"Remove or clarify the key nodes selection step"** — this is incorporated into the Major weakness, not removed.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") — removed. All retained strengths are concrete and evidence-backed.
- **Formatting/style nitpicks** from any reviewer — removed per rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself does not make.

## Suggestions

1. **Resolve the Section 4.2 vs Section 5.2 discrepancy immediately.** State exactly whether the key-nodes selection was used in the experiments. If it was not used, remove or clearly mark it as an optional extension; if it was used, correct Section 5.2 to describe the actual selection procedure.

2. **Add at least two additional baselines** from the low-label regime literature: a self-training method (e.g., GCN trained with iterative pseudo-labeling) and a consistency-regularization method. Without these, the claim of "10–20% better" is only validated against the weakest competitors.

3. **Include a clustering-quality analysis.** Report NMI/ARI of AGC clusters on each dataset. Add an experiment where clusters are corrupted (wrong K, shuffled assignments) to show the method degrades gracefully. Test on at least one heterophilic graph.

4. **Add an ablation study** isolating each of the three Laplacian terms (graph-structure, pseudo-label, true-label) to show which components drive the improvement and whether equal weighting (1/3 each) is appropriate.

## Score and Decision

**Calibration anchors (all from the provided corpus):**

- **OeQE9zsztS** (avg 8.00): Spectrally Transformed Kernel Regression. Strong theoretical contributions, rigorous proofs, clear writing. *Much stronger than the current paper on theoretical depth and clarity.*
- **y21ZO6M86t** (avg 7.25): PolyGCL. Well-motivated method, strong experiments on heterophilic graphs. *Stronger than the current paper in experimental breadth and presentation.*
- **Syt4fWwVm1** (avg 5.67): SpaceGNN. Solid method with 9 datasets, theoretical analysis, good baselines. *More comprehensive evaluation than the current paper, though the current paper has a more novel problem formulation.*
- **4UP387Adir** (avg 5.50): Weakly Supervised GCL. Good experiments but limited novelty. *Comparable overall quality—both have interesting ideas but significant limitations.*
- **GEZACBPDn7** (avg 5.25): KDGCN for scarce-label graph classification. Mixed reviews (3–8). *Similar quality profile: interesting idea, split reviewer opinions, limited baselines.*
- **nRD5TriJ0O** (avg 4.60): Heterophilic Graph Active Learning. Good phenomenon analysis but mixed execution. *Slightly weaker than the current paper; the current paper's contribution is more novel.*
- **w8BL1NShjk** (avg 3.50): Universal SSL on graphs. Inconsistent results, missing details. *Weaker than the current paper; the current paper has cleaner empirical evidence.*
- **VyMW4YZfw7** (avg 3.00): Simplifying GNN Performance. Limited novelty, weak experiments. *Weaker than the current paper.*

The paper introduces a genuinely underexplored problem (SLNC) and a practical, well-motivated approach with consistent empirical gains. However, the unresolved inconsistency between the method description and the experimental protocol, the narrow baseline set, and the absence of any clustering-quality diagnostics are significant weaknesses. The contribution is real but the presentation and evaluation fall short of a strong paper.

Relative to the anchors, this paper sits between nRD5TriJ0O (4.60) and 4UP387Adir (5.50)—better motivated and empirically cleaner than the low-scoring anchors, but with more serious presentation issues and weaker baselines than the mid-scoring ones.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>