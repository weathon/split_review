---
job_id: ff7c17d5-7e54-4f3f-b625-43f45a43a707
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 5asbtzIVpS.pdf
paper: Forest-Based Graph Learning for Semi-Supervised Node Classification
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is directly in graph representation learning and semi-supervised node classification, which is well within ICLR scope.

## Minimum Quality
Pass ✅. The submission contains the expected core sections, presents a coherent method, includes theory and experiments, and provides enough detail to assess the main claims, even though several important technical and empirical issues remain.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious content targeting automated review behavior in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes Forest-based Graph Learning (FGL), a framework for semi-supervised node classification that replaces standard graph message passing with propagation over a small forest of spanning trees. The method combines a pseudo-label-based graph augmentation stage, a homophily-guided tree sampler based on learned edge scores and Wilson sampling, a linear-time tree aggregator derived from two recursions, and a mean-based tree fuser with a local residual module. The paper also provides an asymptotic analysis relating the quality of the edge homophily estimator to the homophily of sampled trees, and reports competitive accuracy and runtime on several node classification benchmarks.

## Strengths
1. The paper has a clear high-level motivation. The framing in **Figure 1** and the four-stage pipeline in **Figure 2** make the central idea easy to grasp: instead of stacking many local layers or paying quadratic cost for global interactions, the method routes information through a small set of spanning trees. Even if some components are individually familiar, the overall perspective is conceptually interesting and easy to remember.

2. The tree aggregator is the strongest technical component of the paper. The recursion in **Equation 5** and **Equation 6**, followed by the linear instantiation in **Equation 7** and **Equation 8**, gives a concrete mechanism for all-node aggregation on a tree in linear time. **Figure 3** is useful here, because it explicitly illustrates the “neighboring roots differ by one edge direction” intuition that underlies the dynamic-programming style derivation. This part is much more than a slogan about “using trees”, it is an actual computational recipe.

3. The main empirical table is strong at face value. In **Table 1**, the method is competitive on all nine datasets and is best on every listed benchmark. The gains are especially large on Cornell, Texas, Wisconsin, Arxiv, and Flickr. Even allowing for the fact that these are transductive node-classification settings where preprocessing can matter a lot, the breadth of the comparison is better than many graph learning submissions.

4. The efficiency claims are supported reasonably well by **Table 2**. The method is consistently fast, and unlike several transformer baselines it avoids OOM on large graphs. The ArXiv and Flickr numbers are particularly relevant, since they show that the method is not just “fast on Cora-sized toy graphs”. The practical runtime advantage over heavier GT baselines is a real positive.

5. The ablation in **Table 3** is informative. It shows that the local module, global tree module, homophily-guided sampling, and multi-tree fusion all matter. In particular, the comparison between uniform sampling, a single homophily-guided tree, and the full forest gives at least some evidence that the claimed forest design is not arbitrary.

6. Theorem 2, as stated in **Section 4.6**, provides a useful sanity check for the sampling story. The result is not a full end-to-end learning theory, but it does formalize the intuition that increasing the score ratio on homophilous versus heterophilous edges shifts the tree distribution toward higher-homophily trees, up to the structural limit induced by NHCC. That is a reasonable theoretical contribution for this kind of paper.

7. The paper is ambitious in scope. It attempts to connect graph augmentation, homophily estimation, random spanning tree sampling, and efficient global aggregation in one framework, rather than making a tiny architectural tweak and benchmarking it on the usual three citation graphs.

## Weaknesses
1. The novelty claim is somewhat overstated, because the method is largely a composition of existing ingredients, and the paper does not sharply isolate what is truly new at the level of learning formulation. The graph augmentation with pseudo-label neighbors in **Section 4.1** is reminiscent of self-training / graph rewiring heuristics, the tree sampler in **Section 4.2** uses Wilson sampling with learned edge weights, and the fuser in **Equation 10** and **Equation 11** is just row-normalize, mean, then residual mix. The most original part is the tree aggregation recursion, but the paper sometimes writes as if the whole framework constitutes a fundamentally new graph learning paradigm. That pitch is a bit too spicy relative to what is actually instantiated.

2. The method depends heavily on preprocessing and graph augmentation, yet this dependence is under-discussed in the main paper. In **Section 4.1**, the graph is first augmented using pseudo-label nearest neighbors, and the text explicitly states that this step both enforces connectivity and increases homophily. This matters a lot, because the favorable tree distribution and later performance may stem substantially from the augmented graph rather than from the forest mechanism itself. Put differently, the model is not just learning on the original graph, it is learning on a rewritten graph whose edges are partially induced by pseudo-label predictions. That makes the attribution of gains murky. A stronger paper would report, in the main text, how much of **Table 1** is already obtained by the augmentation plus local module before any forest aggregation.

3. There is a technical mismatch between the theoretical distribution in **Equation 2 / Theorem 2** and the actual estimator used in **Equation 3**. The theorem analyzes a stylized setting where each edge score is exactly \(p\) for homophilous edges and \(q\) for heterophilous edges, so the tree probability depends only on the count of homophilous edges. In practice, however, \(s(e)\) is a continuous attention-derived score \( (\alpha_{i\to j} + \alpha_{j\to i})/2 \), and the model is trained against pseudo-label targets \(Y'\), not true homophily labels. This is not a minor detail. The theorem justifies a much simpler object than the one actually used. The paper repeatedly uses the theorem to support the learned sampler, but the bridge from discrete \(\{p,q\}\)-weights to noisy real-valued attention scores is mostly rhetorical rather than rigorous.

4. The statement around “quadratic node-pair interactions with only linear complexities” is too loose and should be phrased more carefully. In **Section 4.3** and the abstract, the paper suggests that the tree aggregator realizes quadratic node-pair interactions in linear time. But on a tree, what is computed is a structured global aggregation induced by the tree topology and the chosen associative / disentanglable aggregator. This is not equivalent to arbitrary dense pairwise interaction as in a full attention layer. The distinction matters scientifically, because readers may otherwise infer a stronger expressivity claim than the actual operator provides.

5. The generality claims in **Section 4.3** are not fully convincing from the main text alone. The paper states that many aggregators, including linear attention, RNNs, SSMs, and even non-linear variants, satisfy the required Properties (I) and (II). But the main-paper formalism is underspecified. In **Equation 4**, \(f_{\mathrm{Agg}}\), \(\mathcal M^{+}\), and \(\mathcal M^{-}\) are described at a very abstract level, and it is not obvious for a nontrivial aggregator what the exact state representation is, what auxiliary information is carried, and under what conditions the “disentangle” operator exists. In practice, the actual implementation immediately falls back to the linear case in **Equation 7** and **Equation 8**. So the paper sells broad generality, but empirically and mathematically validates only the easiest special case.

6. There are notation and exposition issues in the core math. A few examples:
   - In **Equation 3**, \(V = XW_V\) is defined but never used in the edge score.
   - The neighborhood notation alternates between \(\mathcal N(i)\) and \(\mathcal N_i\).
   - In **Equation 9**, the object \(\alpha\) is used like an \(n \times n\) matrix in the local submodule, but it was introduced as local attention coefficients in **Equation 3** without a clean matrix definition in the main text.
   - The residual formula in **Algorithm 1**, line 13, uses \(H'' \gets \gamma H' + (1-\gamma)H\), while **Equation 11** uses \(H'' = (1-\gamma)H' + \gamma H\). That is not a harmless typo, because \(\gamma\) controls the local/global tradeoff.
   - In **Section 4.5**, the complexity uses \(K\) in \(\mathcal O((n+m)Kd)\), while the main text elsewhere uses \(N_T\) and \(K_L\). It is unclear what \(K\) denotes here.

   These may look like presentation issues, but they hurt confidence in a paper whose central value proposition is a custom propagation derivation.

7. The empirical evaluation is broad in benchmark count, but still narrow in task scope relative to the paper’s framing. The entire main-paper validation is on transductive semi-supervised node classification. The introduction and conclusion frame FGL as a more general graph learning paradigm, yet there is no main-paper evidence on inductive node classification, graph classification, link prediction, dynamic graphs, or other tasks where “efficient long-range propagation” is also relevant. Since the proposed tree machinery is not obviously task-specific, the absence of even one additional task leaves the contribution more specialized than advertised.

8. The comparison protocol in **Table 1** raises some fairness questions that the main text does not resolve. The paper uses the same train/val/test splits for baselines, but it is not clear whether all baselines were retuned as aggressively as FGL. In the supplementary, the authors describe a two-stage search that effectively treats sampled trees as hyperparameters and performs 200 random trials. That is quite a lot of tuning budget for a method with stochastic structure selection. If baselines were not matched with comparably careful search, the table may partly reflect optimization effort rather than purely model quality. Given that several margins in **Table 1** are modest on the citation graphs, this matters.

9. Some of the claimed interpretability evidence is weaker than the prose suggests. **Figure 5** studies performance versus “homophily estimator accuracy”, but the perfect-accuracy end point leading to perfect classification is a synthetic or oracle-style sanity curve, not an attainable setting. It does show that the architecture can benefit from better edge scores, but the text oversells this as if it establishes “no performance bottleneck”. Similarly, **Figure 6** shows higher homophily ratio under guided sampling, which is consistent with the design, but it does not by itself establish that the downstream gain comes specifically from better long-range semantics rather than from graph rewiring effects introduced earlier.

10. The runtime analysis is useful but incomplete. **Table 2** reports sec/epoch, which is good, but memory usage is not shown, preprocessing cost is not broken out, and tree sampling cost is somewhat blurred by the “pre-training epoch” description in **Section 4.5**. Since the method relies on pseudo-label generation, augmentation, and repeated tree sampling, a more transparent decomposition would help. Right now the efficiency story is directionally convincing, but not fully audited.

11. The paper does not position itself sufficiently against some adjacent lines of work on hierarchical or global semi-supervised node classification methods that also aim to escape shallow local propagation. The related-work discussion in **Section 2** is broad, but it is still a bit selective around methods that provide efficient long-range structure through coarsening, smoothing, or explicit nonlocal dependencies. This weakens the novelty positioning.

## Questions
1. Please disentangle the contribution of graph augmentation from the contribution of forest aggregation. Specifically, what is the performance of:
   - local module on the original graph,
   - local module on the augmented graph,
   - forest module on the original graph when the graph is connected,
   - full FGL on the augmented graph?
   A clean decomposition would substantially increase my confidence that the gains are not mostly coming from the augmentation in **Section 4.1**.

2. Can the authors clarify the exact relation between **Theorem 2** and the learned edge scores used in practice? The theorem assumes binary homophily-dependent edge weights \(p\) and \(q\), while the implemented \(s(e)\) in **Equation 3** is continuous and learned from pseudo-label supervision. Is there any approximation argument, calibration statement, or weaker corollary connecting the two settings?

3. Please make the math in **Section 4.3** more explicit. For the implemented linear case, it would help to rewrite **Equation 7** and **Equation 8** in a fully consistent matrix-vector form with dimensions annotated, and to define exactly how \(\alpha\) is materialized in **Equation 9**. At present, several notation mismatches make this harder to verify than it should be.

4. How expensive is tree sampling in wall-clock time relative to the rest of training? A table breaking total runtime into pseudo-label pretraining, graph augmentation, tree sampling, tree aggregation, and classifier training would be very helpful, especially for ArXiv and Flickr.

5. How sensitive are the results in **Table 1** to the hyperparameter search budget? Given the stochasticity in both learned edge scores and sampled trees, I would like to know whether the method remains strong under a more modest and standardized tuning protocol.

6. The paper argues that the forest paradigm is broadly useful for long-range graph learning. Can the authors provide at least some evidence, even brief, on one non-node-classification setting, or else temper the broader claims in the introduction and conclusion?

7. In **Algorithm 1** and **Equation 11**, the residual weighting appears inconsistent. Please clarify which formula is actually used in experiments, since this directly affects the local/global balance.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns based on the main paper. The work studies standard semi-supervised node classification benchmarks and does not present an obvious privacy, safety, or fairness issue beyond normal considerations for graph datasets.

## Soundness Rating
3: good. The central method is technically plausible and supported by solid experiments, but some theory-to-practice gaps, notation inconsistencies, and unresolved protocol questions prevent a higher score.

## Presentation Rating
2: fair. The paper has good intuition and decent figures, but the main technical presentation has too many notation slips, overclaims, and places where key objects are not defined cleanly enough.

## Contribution Rating
3: good. The tree-based global propagation perspective and the concrete aggregation mechanism are valuable, although the contribution is weakened by dependence on preprocessing and by incomplete isolation of what is genuinely new.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
This is an interesting and reasonably strong submission with a compelling tree-based propagation mechanism, good benchmark coverage, and convincing efficiency trends. I am positive overall, mainly because the paper offers a concrete alternative to deep/local versus shallow/global graph learning and backs it with strong empirical numbers. That said, the paper also has real issues: the novelty is somewhat compositional, the method leans heavily on graph augmentation, the theory only partially matches the implementation, and the presentation of the core equations needs tightening. So I land slightly on the positive side, not enthusiastically.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I checked the main technical parts and experiments carefully, but some implementation details and the full breadth of adjacent related work could still benefit from clarification.