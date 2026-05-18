Now I have a thorough understanding. Let me write the final consolidated review.

## Summary

This paper introduces CoST, a framework for graph reasoning that combines structural information from graph neural networks (GNNs) with textual information from pre-trained language models (PLMs) through an alternating training procedure motivated by a variational objective. The method iterates between updating the PLM (to produce better text embeddings) and updating the GNN (to improve reasoning), using pseudo-targets sampled from the fixed counterpart model. Empirical results across homogeneous graphs (Amazon, MAG, CitationV8, GoodReads) and heterogeneous knowledge graphs (FB15k237, WN18RR, Wikidata5M) show CoST outperforming a range of structure-based and text-based baselines.

## Strengths

- **Novel alternating training formulation**: CoST proposes a principled alternation between GNN and PLM training on large graphs, where concurrent joint training is infeasible. The variational framing (Algorithm 1) gives a clean interface between the two modalities, and the framework is modular with respect to GNN architectures.

- **Consistent empirical improvements across diverse benchmarks**: CoST outperforms baselines on homogeneous datasets (Amazon, MAG, CitationV8, GoodReads in Tables 2–3), heterogeneous KGs (FB15k237, WN18RR in Table 4), and the large-scale Wikidata5M dataset (Table 5). On FB15k237 (MRR 0.402 vs. best baseline A*Net 0.383) and WN18RR (MRR 0.601 vs. AdaProp 0.595), the gains are clear. The breadth of improvement across dataset types supports the claim that the framework effectively integrates textual and structural information.

- **Generalizability across GNN backbones**: Figure 3a shows consistent improvement from CoST over pretrained baselines when using RGCN, CompGCN, or NBFNet as the backbone on both FB15k237 and WN18RR. This demonstrates the framework is not tied to a specific GNN design.

- **Rapid convergence**: Figure 3b shows CoST reaching near-peak performance within a few alternating iterations (5–10) on FB15k237 and WN18RR, supporting the practical viability of the alternating paradigm.

## Weaknesses

### Fatal
None.

### Major
- **Unclear theoretical presentation undermines the "principled" framing.** Theorem 2.1 and Equation (6) use the notation \(\mathcal{O}(\theta^2)\) which is ambiguous in context — it is not a standard big-O complexity notation, and its role in the claimed "equivalence" between the original objective \(\mathcal{O}(\phi)\) and the new combined objective is never defined in the main text. The paper states that optimizing \(\mathcal{O}(\phi)\) is "equivalent" to optimizing the new objective, but standard variational inference yields a lower bound, not an equivalence. While a full derivation may reside in an appendix, the main body's presentation of this theoretical foundation is too cursory to support the strong claim of a "principled" alternating framework. This does not invalidate the method (Algorithm 1 is independently implementable), but it substantially weakens the claimed theoretical contribution.

- **Essential experimental setup details are missing, compromising reproducibility.** The paper does not specify (i) which GNN backbone produced the main results reported in Tables 2, 3, and 5 (the ablation in Figure 3a tests three options on FB15k237/WN18RR only, but the main tables cover many more datasets); (ii) which PLM variant was used (BERT-base, RoBERTa-large, or another); (iii) the number of alternating steps \(L\) used in practice; nor (iv) the values of the loss weighting hyperparameters \(\gamma\) and \(\tau\) from Equation (12). These are not minor tuning details — the GNN backbone and PLM choice are core architectural decisions that directly affect reported numbers, and \(L\) is a defining parameter of the proposed algorithm. Without them, the experiments cannot be independently reproduced or assessed for soundness.

### Minor
- **Hard pseudo-target approximation is used without empirical validation.** Equations (8) and (11) replace continuous variational objectives with hard positive/negative samples drawn from multinomial distributions. The paper justifies this by citing the "intricateness and instability of optimizing the entropy of \(q_\theta\)" (lines 112–114), which is a reasonable motivation, but no ablation is provided comparing hard sampling against soft targets or analyzing the effect of sampling noise. In an EM-style alternating scheme, this choice could affect convergence behavior, and empirical validation would strengthen confidence in the approach.

- **No error bars or variance reporting.** All results in Tables 2–5 are reported as single numbers. On FB15k237 (Table 4), CoST's MRR of 0.347 is only 0.005 above AdaProp (0.342) and 0.006 above NBFNet (0.341) — gaps so small that without variance estimates it is impossible to know whether they reflect meaningful improvement or random variation. While single-run reporting is not uncommon in KG completion, the paper claims "state-of-the-art" performance, which demands stronger statistical support for close margins.

- **Scalability claims are not quantitatively supported.** The paper motivates CoST by arguing that concurrent GNN+PLM training is infeasible at the scale of real-world graphs (abstract, introduction), but never reports training time, memory usage, or any computational cost comparison. The largest dataset (Wikidata5M) is mentioned only in Table 5 with no discussion of the resources required. The scalability advantage of alternating over joint training is asserted rather than demonstrated.

- **The "pretrained GNN" baseline understates the comparison.** The pretrained GNN baseline in all tables uses embeddings from an *unaltered* PLM (frozen BERT). A fairer comparison would include a GNN initialized from a PLM that was fine-tuned on the same task in a separate step, to isolate whether CoST's alternating procedure adds value beyond simply fine-tuning the PLM once.

### Trivial
- The paper does not explain why the query edge \((h, r_q, t)\) is excluded from message passing (the conditioning \(\mathcal{E}_{/\{(h, r_q, t)\}}\) in Equation 1). While this is standard in inductive link prediction, a brief clarification would help readers.

## Nice-to-Haves
- Reporting results over multiple seeds with standard deviations for tight-margin comparisons.
- An ablation comparing hard vs. soft pseudo-targets to validate the approximation.
- Training time / GPU-hour comparisons on at least one large dataset (e.g., Wikidata5M) to substantiate the scalability claim.
- A baseline where the PLM is fine-tuned on the reasoning task alone (without alternating) and then fed as initialization to the GNN, to isolate the benefit of alternation.
- A brief discussion of limitations and failure cases (e.g., graphs with sparse or uninformative text).

## Removed Points
These points from the reviewers were flagged and removed; they are listed here for completeness but should not be weighed in the evaluation:

- **"No heterogeneous graph experiments"**: Removed because the paper explicitly categorizes FB15k237, WN18RR, and Wikidata5M as heterogeneous datasets (Table 1) and reports results on them (Tables 4–5). The criticism is factually wrong.
- **"Hard pseudo-targets used without justification"**: Removed — the paper does provide a justification (lines 112–114 cite the instability of optimizing entropy). The remaining concern (lack of empirical validation) is kept in Minor above.
- **"Theorem 2.1 is never proved"**: Removed — proofs may reside in the appendix, which the parser strips from all submissions.
- **Missing hyperparameters (learning rate, batch size, optimizer)**: Removed per rule — these are considered trivial implementation details that do not affect the core assessment.
- **Missing comparison against Zhao et al. (2023)**: Removed — the reviewer's characterization of this paper as a directly competing combined method cannot be independently verified from the cited context alone, and the paper does include a broad set of baselines across multiple categories.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective that the authors themselves do not already acknowledge or that would reframe the work in a fundamentally different light.

## Suggestions
1. Clarify the theoretical derivation in Section 2.2: define the \(\mathcal{O}(\theta^2)\) term explicitly, explain why standard ELBO lower-bound reasoning applies, and provide the key steps of Theorem 2.1's derivation in the main body (not just the appendix).
2. Specify the GNN backbone and PLM variant used to produce the results in each main table (Tables 2, 3, 5), and report the number of alternating steps \(L\) and the loss weights \(\gamma, \tau\).
3. Add an ablation comparing hard vs. soft pseudo-targets on at least one dataset to validate the approximation.
4. Report results over at least 3 random seeds with standard deviations for the tightest-margin comparisons.
5. Include training time and memory usage for at least one large dataset to support the scalability motivation.

## Score and Decision

The paper proposes an interesting alternating training framework that shows consistent empirical gains across diverse benchmarks. The core idea is sound and the experimental results, while missing some details, are uniformly positive. However, the paper's central theoretical claim is presented with unclear notation and insufficient justification in the main text, and essential experimental setup details (which GNN backbone, PLM variant, number of alternating steps) are omitted, making the results difficult to reproduce or fully assess. These are significant weaknesses but not fatal — the method is implementable from Algorithm 1, and the empirical patterns are coherent. I recommend acceptance conditioned on the authors clarifying the theoretical framing and providing the missing experimental details.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>