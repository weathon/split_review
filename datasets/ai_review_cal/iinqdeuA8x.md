- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 5, 6, 5, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes a theoretical framework for quantifying Dynamic Graph Neural Network (DyGNN) expressiveness by extending the Weisfeiler-Lehman hierarchy to dynamic graphs ($k$-DWL tests). It proves that existing DyGNNs are bounded by 1-DWL and introduces **HopeDGN**, a DyGNN that (in its Global variant) achieves provable 2-DWL expressive power through Multi-Interacted Time Encoding (MITE) and node-pair level aggregation. A Transformer-based local implementation is provided, and experimental results on seven link prediction benchmarks show state-of-the-art performance with gains up to 3.12\%.

## Strengths

1. **Novel $k$-DWL hierarchy for dynamic graphs (Section 4.1)** — The paper extends the WL hierarchy to continuous-time dynamic graphs, defining $k$-DWL tests and proving $(k+1)$-DWL is at least as powerful as $k$-DWL (Proposition 1). This provides the first principled theoretical framework for quantifying DyGNN expressive power relative to a well-defined dynamic isomorphism test, a genuine gap in the literature.

2. **Provable 2-DWL equivalence for Global HopeDGN (Propositions 4 and 5)** — The paper formally proves that the Global variant of HopeDGN (aggregating over all nodes $w\in\mathcal{V}$) is both upper-bounded by 2-DWL (Proposition 4) and, with injective AGG, UPDATE, $f_1$, $f_2$, achieves expressive power equivalent to 2-DWL (Proposition 5). This is the first result linking a DyGNN architecture to a quantifiable higher-order expressiveness guarantee.

3. **Empirical superiority on link prediction across all 7 datasets (Table 1)** — HopeDGN achieves the highest Average Precision on every dataset under both transductive and inductive settings, outperforming nine strong baselines including DyGFormer, CAWN, and PINT. The gains are non-trivial on several datasets: 2.77\% (MOOC transductive), 1.37\% (LastFM transductive), and 3.12\% (MOOC inductive).

4. **MITE as a flexible, plug-and-play module (Table 3)** — Integrating MITE into three baseline models (TGAT, GraphMixer, TCL) yields large and consistent performance gains (e.g., +33.21\% AP for TGAT on Enron transductive), demonstrating that MITE generalizes beyond HopeDGN and can enhance existing methods — a practical contribution independent of the theoretical architecture.

5. **Clean ablation isolating MITE's contribution (Figure 2)** — Removing MITE causes significant performance drops across four datasets, while removing time encoding has a smaller effect. This provides direct evidence that the bi-interaction history captured by MITE is the key driver of improvement, not other architectural choices.

6. **Rigorous bound on existing DyGNNs (Proposition 2)** — The paper formally proves that the expressive power of current DyGNNs is upper-bounded by 1-DWL, using the Dynamic Adjacency Tensor to model interaction histories. This establishes a clear baseline that prior work lacked.

## Weaknesses

### Fatal
None.

### Major

1. **Global/local theory-practice gap is acknowledged but unresolved.** Propositions 4 and 5 explicitly apply to the *Global* HopeDGN, which aggregates over *all* nodes $w\in\mathcal{V}$. The actual implemented model (Section 4.4) is the *local* variant, which aggregates only over $\mathcal{N}(u,t) \cup \mathcal{N}(v,t)$. The paper acknowledges this as a computational concession (lines 192–193: "However, the number of nodes may be enormous... Therefore, we propose a local version") but provides **no theoretical analysis** of what expressiveness the local restriction sacrifices. The abstract and conclusion state without qualification that HopeDGN achieves 2-DWL, but this is proven only for a variant that is never tested. This disconnect weakens the core claim: we do not know whether the model that actually runs inherits the 2-DWL guarantee. The paper should either (a) prove that the local variant retains 2-DWL under stated conditions on the neighbor sets, or (b) explicitly characterize the local variant as a scalable approximation whose exact expressiveness is unknown, and discuss what is potentially lost.

2. **Missing node classification results — claimed but not presented.** The abstract claims "experiments on both link prediction and node classification tasks" (line 12), the introduction lists "Extensive experiments on both link prediction and node classification" as a main contribution (lines 39–40), and the conclusion repeats the claim (line 360). The experimental settings section mentions "temporal node classification tasks for evaluation" (line 253). **However, no node classification results appear anywhere in the paper.** No appendix is referenced. This is a factual discrepancy between the paper's claims and its content. The empirical evidence does not support the claimed scope of evaluation.

3. **Transformer implementation breaks the injectivity assumption central to Proposition 5.** Proposition 5's 2-DWL equivalence guarantee requires that AGG, UPDATE, $f_1$, and $f_2$ are *injective*. The implementation (Section 4.4) uses multi-head self-attention with mean pooling (Equation 8: $\text{MEAN}(\mathbf{H}^{(L)})$), which is not injective over multisets — mean pooling collapses distinct multisets that share the same mean. The paper briefly states that "injectiveness of each function... can be approximated with MLP or other neural networks due to the universal approximation theorem" (line 214), but this reasoning does not cover mean pooling, which is not a universal approximator. The gap between the theoretical requirement and the practical aggregation is unaddressed.

### Minor

4. **No direct empirical validation of the expressive power claim.** The paper motivates the work with Figure 1 — a concrete pair of dynamic graph structures that 1-DWL (and existing DyGNNs) cannot distinguish but 2-DWL (and HopeDGN) should. However, no synthetic experiment demonstrates that HopeDGN actually distinguishes this (or any similar) pair while baselines fail. The link prediction results show aggregate improvements but do not isolate expressiveness. A controlled synthetic experiment would directly validate the theoretical contribution and is standard practice in the GNN expressiveness literature (e.g., Xu et al. 2019, Morris et al. 2019).

5. **Empirical gains are marginal on saturated benchmarks.** On Reddit and Wikipedia, HopeDGN's improvements over DyGFormer are 0.09–0.21\% (transductive) and 0.15–0.34\% (inductive). While statistically significant given the reported standard deviations, these differences may not be practically meaningful. The paper does not discuss whether the additional complexity of HopeDGN is justified in these cases, or acknowledge diminishing returns.

6. **Patching technique's effect on expressiveness is unexplored.** The patching technique (Section 4.4) collapses neighborhood sequences into patches, reducing sequence length at the cost of discarding within-patch positional structure. The effect of this operation on the model's expressive power — whether it introduces collisions between distinct neighborhoods — is not analyzed.

7. **Proposition 3 is an existential claim without explicit construction.** Proposition 3 states "There exists two dynamic graphs... that DyGNN with MITE can distinguish while vanilla DyGNN cannot." This is a weak existential claim. Providing an explicit construction (e.g., realizing the Figure 1 example formally) would be more informative.

### Trivial
None.

## Nice-to-Haves
- A synthetic expressiveness experiment (as suggested in weakness #4).
- Analysis of the local variant's expressive power relative to the global version.
- A comparison of different pooling strategies (mean vs. sum vs. attention-based) to assess the injectivity gap in practice.
- Summary of node classification results or removal of the claim if such experiments were not conducted.

## Removed Points
- **"The paper should discuss why the extra complexity is justified for datasets with <0.5% improvement"**: This is a soft suggestion, not a concrete weakness. The paper reports improvements regardless of magnitude. Removed as a gentle recommendation rather than a weakness.
- **"Proposition 1 hierarchy proof not in main paper"**: Proofs in appendix are standard and expected. The paper states the proposition; absence of a proof in the main text is not a weakness. Removed by instruction (missing appendix content is a parser artifact).
- **"Missing related works"**: I cannot verify the existence of missing references externally. Removed by instruction.
- **"Reproducibility concerns about hyperparameters, n_g sampling, etc."**: These are standard implementation details that a paper at this stage of development would be expected to clarify but do not constitute a substantive weakness. Removed as nitpicks.
- **"The improvement on TGAT+Enron is just catch-up"**: This is speculative framing. The fact that TGAT underperforms on Enron and MITE brings it to competitive levels is itself informative — it shows MITE provides information TGAT critically lacks. This is a feature, not a flaw. Removed.
- **Strength Finder's generic strengths**: "This paper addressed an important problem" — removed as generic. The remaining strengths are kept and verified against the paper.

## Novel Insights
The harsh critic correctly identifies that the paper's central tension is between the clean theoretical narrative (Global HopeDGN = 2-DWL) and the messier implementation (local Transformer with patching and mean pooling). What is genuinely interesting is that despite this gap — despite the implemented model lacking theoretical guarantees matching the global variant — it still outperforms all baselines on all datasets. This suggests either that (a) the advantage comes primarily from MITE (which is explicitly designed to capture bi-interaction history relevant for higher-order expressiveness) and the local aggregation is sufficient to leverage it in practice, or (b) the theoretical framework is capturing a real structural property that survives approximation. Either interpretation has implications for future work: the paper shows that *even imperfectly realized* higher-order expressive power translates to empirical gains, raising the question of whether tighter alignment between theory and implementation would yield further improvements. The ablation study (Figure 2) strongly supports the MITE-centric interpretation, which is the paper's cleanest empirical result.

## Suggestions
1. **Clarify the global/local gap in the abstract and conclusion.** Add a sentence noting that the 2-DWL guarantee applies to the Global variant and discuss what (if anything) is known about the local variant's expressiveness.
2. **Either present node classification results or correct the claims.** If results exist (e.g., in a now-stripped appendix), summarize the key trends in a paragraph in Section 5 with a reference. If not, remove the claim from the abstract, contributions, and conclusion.
3. **Add a synthetic expressiveness experiment.** Construct the Figure 1 example (or any 1-DWL indistinguishable pair that 2-DWL can separate) and show that HopeDGN distinguishes them while TGAT, TGN, and DyGFormer fail. This would make the theoretical contribution tangible and directly verifiable.
4. **Acknowledge and discuss the injectivity gap in the Transformer implementation.** Note that the practical implementation relaxes the injectivity requirement and discuss why (e.g., mean pooling with attention weights may nonetheless be sufficiently expressive in practice).
5. **Acknowledge the diminishing returns on saturated benchmarks** and contextualize the computational cost trade-off.
