- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 6, 3
Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes T-GAE (Transferable Graph Autoencoder), a generalized graph autoencoder architecture for network alignment. The key idea is to train a GNN-based encoder on a family of small graphs in a self-supervised manner (reconstructing graph structure), then transfer the learned encoder to produce node embeddings on larger, unseen graphs. Alignment is performed by solving a linear assignment problem on the learned embeddings. The paper claims a theoretical connection to spectral methods (Theorem 3.2) and demonstrates through experiments that T-GAE achieves high matching accuracy on graphs up to ~18k nodes, outperforming several baselines including GAE, VGAE, WAlign, and spectral methods.

## Strengths

- **Transfer learning enables alignment of very large graphs (Table 3).** T-GAE trained on four small graphs (Celegans, Arena, Douban, Cora) achieves >99% accuracy on Dblp (~16k nodes) and Coauthor CS (~18k nodes) at 0% perturbation without any retraining on those large graphs. No compared baseline scales to this setting. This is the paper's strongest empirical contribution.

- **Data augmentation via perturbed training improves robustness (Table 4).** Training with perturbed versions of the training graphs yields a 15.5 percentage point improvement on Arenas at 5% perturbation (51.4% vs 35.9%), directly supporting the claim that augmented training produces more robust representations.

- **Subgraph matching outperforms baselines on real cross-network tasks (Figure 3).** T-GAE achieves a higher hit rate than all competing methods on ACM-DBLP and Douban Online-Offline subgraph matching. Notably, the paper includes both a per-graph-pair trained variant and a transfer-learned variant of T-GAE for this experiment, providing cleaner attribution of the architectural benefit.

- **Explicit complexity analysis for deployment (Section 4.4).** The paper provides a detailed complexity breakdown (O(|V|c²+|E|c) for the GNN, O(|V|²) for greedy Hungarian, and a low-complexity O(|V|c²+|E|c+|V|log|V|) variant for large graphs), which directly supports the scalability claims.

- **Permutation equivariance by construction (Theorem 3.1).** The paper correctly identifies that GNN embeddings are permutation-equivariant, a property that spectral embeddings lack due to eigenvector sign ambiguity. This provides a principled architectural motivation for using GNNs in alignment.

## Weaknesses

### Fatal
None.

### Major

- **Theoretical claim overreach: Theorem 3.2 does not prove what the paper asserts about T-GAE.** Theorem 3.2 proves that *there exists* a GNN whose alignment error is no worse than that of the spectral method. The paper, however, repeatedly claims that "T-GAE representations … are provably at least as good in network alignment as certain spectral methods" (abstract, line 22, contribution C2, conclusion). The gap between "there exists a GNN" and "the trained T-GAE (Eq. 9/10) satisfies this" is unbridged. There is no argument that the training objective converges to that specific GNN, nor any bound on the suboptimality of the learned embeddings relative to the ideal ones. This is an important overstatement — the theoretical contribution should be reframed as an expressivity result (GNNs *can* represent spectral alignment embeddings) rather than a provable guarantee about the trained model. The strong empirical results stand on their own and do not require this overclaim.

- **Missing single-graph ablation for main graph matching experiments (Table 3).** T-GAE is trained on a family of four graphs, while all baselines (including GNN-based ones like GAE, VGAE, WAlign) are trained per test graph. This means T-GAE benefits from multi-graph training and a form of regularization that the baselines do not receive. Without a variant trained *on each test graph individually* (no transfer), it is impossible to attribute how much of the improvement comes from the architectural design versus the multi-graph training setup. The subgraph matching experiment (Section 5.4) partially addresses this by including a per-graph-pair T-GAE, but the main graph matching experiments lack this control. The paper should include this ablation or explicitly reframe the contribution as a *transfer learning pipeline* rather than an architecturally superior method.

### Minor

- **Missing implementation details.** The paper specifies architectural choices (2-layer MLPs, skip connections) but does not report learning rate, optimizer, number of training epochs, hidden dimensions (c), number of GNN layers, or perturbation parameters for data augmentation. These details are essential for reproducibility and should be included in the main text or clearly indicated as appendix content.

- **No error bars for subgraph matching (Figure 3).** The hit-rate curves in Figure 3 are shown without confidence intervals or error bars, unlike the main matching results in Table 3 where 10-sample statistics are reported. Adding error bars would strengthen the evidence.

- **Ablation for input structural features not included.** All GNN-based methods use 7 NetSimile-derived structural features as input. An additional variant using raw features (e.g., one-hot degree vectors) or no features would help isolate how much of T-GAE's performance depends on feature engineering versus the GNN processing itself.

- **"First attempt" claim is difficult to verify.** The paper claims to be "the first attempt that performs exact alignment on a network at the order of 20k nodes and 80k edges" (line 219). This is a strong claim that is not substantiated by a survey of prior work; the authors should either verify it with explicit references or remove the "first" qualifier.

### Trivial
None.

## Nice-to-Haves

- **Cross-dataset transfer analysis in both directions.** The transfer experiment trains on small graphs and tests on larger ones. Testing the reverse direction (train on large, test on small) would help determine whether the transferability depends on motif overlap or is symmetric.
- **Statistical significance tests** comparing T-GAE against the strongest baseline per dataset would strengthen the claims in Table 3 beyond reporting means and standard deviations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Provable connection to spectral methods" as a strength** — Removed because it conflicts with the verified weakness that the theorem is oversold. The theorem is technically correct (existence of a GNN), but framing it as a strength supporting the paper's main claims would be misleading without acknowledging the gap between existence and learnability.
- **Missing related work on GMNs (Graph Matching Networks)** — Removed per policy: I cannot verify the existence or relevance of uncited works.
- **Baseline training details request (number of runs, data splits, compute)** — Merged into the implementation details point above; the standalone request was too broad.
- **General evaluation rigor concerns without concrete anchors** ("the evaluation lacks rigor," "could the metric be measuring a proxy") — Removed as speculative area sweeps that lack specific citations to the paper.
- **Criticism about "existence ≠ guarantee" being a fatal flaw** — Demoted from the critic's implied severity (fatal) to Major. The empirical results are strong and the issue is fixable via re-framing, not a model collapse.

## Novel Insights

The main novel insight from the reviews is the identification of a systematic asymmetry in the experimental setup: T-GAE's transfer learning advantage (training on multiple graphs) is conflated with its architectural advantage in the main experiments, making it difficult to attribute performance gains. The theoretical overclaim compounds this by presenting a capacity result (there exists *some* GNN) as a guarantee about the specific trained model. Neither issue individually sinks the paper, but together they reveal that the paper's strongest contribution is the *transfer learning pipeline for scalable alignment* rather than a provably superior architecture — which is still a valuable contribution if reframed honestly.

## Suggestions

1. **Reframe the theoretical contribution.** Replace claims that "T-GAE is provably at least as good as spectral methods" with a more precise statement: Theorem 3.2 shows GNNs have the capacity to express spectral alignment embeddings. This is an interesting expressivity result that motivates the approach, but it does not constitute a guarantee for the learned model. The empirical results already provide the evidence that T-GAE works well in practice.

2. **Add a single-graph ablation.** Evaluate T-GAE trained from scratch on each individual test graph (Celegans alone, Arena alone, etc.) and compare to the multi-graph trained version in Table 3. If the single-graph variant also outperforms baselines, the architecture is vindicated. If not, reframe the contribution as a transfer learning pipeline.

3. **Report full implementation details** (learning rate, optimizer, epochs, hidden dimensions, number of layers, GPU/CPU specifications) in the main text if the appendix is not available to readers.

4. **Add error bars or confidence intervals to Figure 3** and tone down the "first attempt" claim with a literature check or by dropping the "first" qualifier.
