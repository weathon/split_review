Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes DDLR, a dual-denoising framework for inductive knowledge graph completion (KGC) that combines **path-based sampling** (a scoring function for selecting important reasoning paths) and **edge-based sampling** (Bernoulli sampling of relations based on single-rule confidence statistics) to filter noise during GNN message passing. Experiments on WN18RR, FB15k-237, and NELL-995 across four inductive splits each show competitive results and the ablation studies confirm both sampling components contribute to performance.

## Strengths

- **Dual denoising validated by direct ablation (Table 2):** Removing either the edge-sampling module or the path-sampling module causes clear MRR drops across all three datasets (e.g., WN18RR v1 drops from 73.1 to 67.8 and 68.3 respectively). This provides concrete evidence that both mechanisms are needed for the reported performance.

- **Path-scoring components decomposed via ablation (Table 3):** The paper separately ablates the current-path score and the remaining-path score. Performance degrades when either term is removed, confirming that the two-part scoring design in Section 4.1 is not redundant.

- **Edge-sampling design validated against alternatives (Table 4):** The proposed single-rule confidence measure for relation relevance is compared against cosine similarity, KL divergence, and JS divergence, and consistently outperforms them. This supports the design choice for the edge-sampling component.

- **Competitive results across multiple datasets and splits (Table 1):** DDLR achieves best or second-best results on most of the 12 evaluation settings (3 datasets × 4 inductive splits) against a strong set of baselines including NBFNet, RED-GNN, Adaprop, and GraPE, demonstrating generalization across different knowledge graphs.

## Weaknesses

### Fatal
None.

### Major

- **The "remaining path score" is conceptually misnamed and its approximation is unvalidated.** In Eq. 9, the representation \(\mathbf{r}_q^{(t)}(x,v)\) is computed solely from the current path representation \(\mathbf{h}_q^{(t)}(u,x)\) and the query relation \(\mathbf{q}\). It contains no information about the actual graph structure from \(x\) to the (unknown) answer \(v\). The paper acknowledges this is an approximation (lines 113–115) because "we do not possess the representation of the answer entity \(v\)." However, calling this a "remaining path score" is misleading — it is a learned function of the current path and query, not a structural evaluation of whatever comes next. The paper provides no sanity check (e.g., comparing against a ground-truth remaining-path score on a small graph where enumeration is feasible) to verify that this approximation behaves reasonably. Since the path-scoring mechanism is billed as a core contribution for addressing a limitation of prior node-based scoring, this gap weakens the conceptual foundation of the method.

### Minor

- **No variance or uncertainty reporting.** The main results (Table 1) report only point estimates. Given that many margins between methods are small (e.g., 0.1–0.5 MRR on several splits), it is impossible to assess whether the reported improvements are statistically reliable. Standard deviations or confidence intervals from multiple runs would substantially strengthen the evidence.

- **No controlled ablation isolating the new path-scoring function from Adaprop's scoring.** The paper compares against Adaprop as a full baseline and shows DDLR outperforms it, but this comparison conflates two changes: the new path-scoring function *and* the added edge-sampling module. An ablation that replaces DDLR's path-scoring with Adaprop's scoring (while keeping edge-sampling fixed) would cleanly attribute the benefit of the scoring innovation, which is the paper's primary claimed improvement over node-based sampling.

- **Figure 1's motivating example is not empirically verified.** The paper uses a concrete example to argue that node-based top-K sampling selects the wrong entity (e) over the correct one (d), and claims DDLR fixes this via remaining-path scoring. No experiment confirms that DDLR actually selects entity d in this or structurally similar cases. A small case study or qualitative analysis would strengthen the motivation-to-evidence chain.

### Trivial

- **Best hyperparameter values not reported.** The paper gives extensive tuning ranges (learning rate, K, p_e, p_τ, etc.) but does not list the final selected hyperparameters per dataset, making reproduction harder than necessary.

## Nice-to-Haves

- The remaining-path approximation could be validated on a small graph where all paths are enumerable, comparing the proposed score against an oracle.
- An additional ablation in Table 3 that removes both the current and remaining scores (i.e., accepting all paths up to length L) would show the overall scoring function helps beyond an unfiltered baseline.
- A brief discussion of how single-rule confidence (which captures direct co-occurrence) relates to multi-hop path structures would clarify the scope of the edge-sampling heuristic.

## Removed Points

*"Novelty is incremental relative to Adaprop"* — Removed because this is a general judgment not anchored to a specific technical deficiency in the paper. The paper's contributions (path-based scoring + edge-level sampling) are clearly differentiated from Adaprop's node-based top-K attention, and the ablation studies confirm their additive value. The related controlled-ablation request is kept as a **Minor** weakness above, which is the concrete technical form of this concern.

*"SOTA claim is not supported"* — Removed in its strong form. The paper's text ("frequently securing the best or second-best rankings") is factually accurate based on Table 1. The lack of variance reporting is kept as a separate weakness. The claim is competitive rather than dominant, but that does not constitute a flaw — the paper does not claim to be uniformly best on every split.

*"Edge sampling conflates directionality / doesn't discuss multi-step reasoning"* — Removed because the paper explicitly models directionality (ordered relation pairs r₁⇒r₂ and r₂⇒r₁ have different confidences, as they should). The multi-step issue is a scope observation rather than a concrete flaw — the paper uses single-rule confidence as a filtering heuristic, not as a complete multi-hop reasoning model.

*"Missing comparison to NeuralLP or DRUM for relation relevance" (from Section notes)* — Removed; NeuralLP and DRUM are already in the main baseline table (Table 1), and Table 4's purpose is to compare different *measures* of relation relevance, not different end-to-end models.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Rename or clarify the "remaining path score."** Since Eq. 9 does not encode structural information about the path from x to v, consider renaming it (e.g., "path continuation score" or "future relevance score") and providing a clearer justification for why combining the current path representation with the query relation is a reasonable proxy.

2. **Report standard deviations** for the main results (Table 1) over at least 3–5 random seeds. This is important given the small margins between methods on several splits.

3. **Add a controlled ablation** comparing DDLR's path-scoring function against Adaprop's node-scoring function within the same framework (keeping edge sampling fixed) to isolate the contribution of the scoring innovation.

4. **Report the final selected hyperparameters** for each dataset in the main text or appendix.

5. **Consider a small case study** that demonstrates DDLR correctly selects the evidence path in the Figure 1 example (or a structurally similar one), directly linking the motivating intuition to empirical behavior.

## Score and Decision

**MY FINAL SCORE: <score>6.5</score>**
**MY FINAL DECISION: <decision>Accept</decision>**