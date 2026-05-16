Now I have a thorough understanding of the paper and all the review inputs. Let me compose the final consolidated review.

## Summary

The paper introduces CoST, a framework for graph reasoning that alternates between training a Graph Neural Network (GNN) and a Pre-trained Language Model (PLM) using a variational objective. Rather than jointly training both models (which is computationally infeasible for large graphs), CoST iteratively optimizes each model while keeping the other fixed, using pseudo-targets sampled from the fixed model to guide the training of the active model. The framework is evaluated on homogeneous graphs (Amazon, MAG, CitationV8, GoodReads) and heterogeneous knowledge graphs (FB15k237, WN18RR, Wikidata5M), achieving state-of-the-art results.

## Strengths

- **Alternating training enables scalable integration of GNN and PLM**: The paper proposes a principled alternating optimization scheme (Theorem 2.1, Algorithm 1) that addresses the scalability bottleneck of joint GNN+PLM training. Empirical results (Tables 2–5) show consistent improvements over both structure-only and text-only baselines across six datasets, confirming that the alternating scheme effectively combines both modalities.

- **Consistent state-of-the-art performance across diverse graph reasoning benchmarks**: CoST achieves the best MRR and Hits@k scores on homogeneous graphs (AmazonSports, AmazonClothing, MAGGeology, MAGMath, CitationV8, GoodReads) and heterogeneous knowledge graphs (FB15k237, WN18RR, Wikidata5M), often surpassing resource-intensive LLM-based methods (GraphGPT, LLaGA, LINKGPT) as well as strong structure-based methods like NBFNet.

- **Architecture-agnostic improvement demonstrated via ablation**: The ablation study (Figure 3a) shows that CoST improves over three different GNN backbones (RGCN, CompGCN, NBFNet) on FB15k237 and WN18RR, with consistent gains. Convergence analysis (Figure 3b) also shows rapid convergence, validating the stability of the alternating training procedure.

- **Clear motivation with illustrative example**: Figure 1 provides a concrete scenario (Kylian Mbappé team membership) where purely structural reasoning fails but textual information resolves ambiguity, effectively motivating why combining text and structure is essential.

## Weaknesses

### Fatal
None.

### Major

- **Theory-empirics disconnect between the variational objective and the implemented losses**: The paper claims a theoretically grounded variational framework (Theorem 2.1), but the actual training objectives in Equations (9) and (12) are heuristic contrastive losses using pseudo-targets sampled from the fixed model. The term \(\mathcal{O}(\theta^2)\) in Theorem 2.1 is never defined or explained. The entropy term in the KL divergence is dropped with only the qualitative justification that it is "intricate and unstable" (line 112). The paper does not show that the contrastive losses in (9) and (12) are consistent with optimizing the claimed ELBO. This gap between the theoretical framing and the implemented algorithm weakens the methodological contribution — the value of the paper rests primarily on the empirical results rather than the theoretical derivation.

### Minor

- **Missing error bars and statistical significance**: No standard deviations, confidence intervals, or significance tests are reported for any experiment (Tables 2–5). While single-run evaluation is common in KG completion benchmarks, the central claim of state-of-the-art performance rests on unquantified point estimates. The improvements are generally large and consistent across datasets, which partially mitigates this concern, but variance reporting would substantially strengthen the evidence.

- **Incomplete specification of experimental setup affecting reproducibility**: The paper does not clearly state which PLM architecture (BERT-base, BERT-large, RoBERTa?) is actually used as the encoder for CoST's own experiments — BERT is mentioned only for baseline methods. The GNN backbone used for CoST's main results (vs. the ablation study which tests multiple backbones) is not specified. Hyperparameters \(\gamma\) and \(\tau\) (Equation 12) are introduced with no values or sensitivity analysis. The update steps \(L\) and decoder network \(g\) are not parameterized. Some of these details may reside in the appendix (which the parser strips), but the main text lacks sufficient detail for independent implementation.

- **Limited analysis of the pretrained GNN underperformance**: The paper notes (line 264) that "the pretrained GNN model in CoST falls slightly behind key baselines" and attributes this to "the difficulty of unaltered language models in providing effective text representations." This is a relevant observation that would benefit from deeper analysis — e.g., does the PLM provide poor initial embeddings? What changes during alternating training that fixes this? The brief attribution is plausible but not investigated.

### Trivial
None.

## Nice-to-Haves

- Sensitivity analysis for the weighting hyperparameters \(\gamma, \tau\) in Equation (12) and for the number of sampled positives/negatives would help understand the method's robustness.
- A comparison with a fine-tuned PLM+GNN baseline (e.g., using gradient checkpointing or sampling to make joint training tractable) would clarify whether the alternating scheme is essential or if a simpler approach suffices.
- A qualitative analysis (e.g., case study showing how text representations change after alternating training) would complement the quantitative results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- "Table 1 is garbled by OCR" / "Tables 2 and 3 are difficult to read due to OCR artifacts" / "Equation (10) is garbled" / "Table 6 is unreadable" — These are parser-induced artifacts from extracting text/math from PDF; the original submission does not have these issues.
- "The notation \(\mathbb{P}\mathbb{L}\mathbb{M}\) is unorthodox" — Pure formatting/style nitpick; does not affect scientific content.
- "Several recent graph+text methods... are missing from the discussion" — Per policy, I cannot confirm the existence or relevance of unnamed missing references.
- "The pretrained GNN underperformance is not discussed" — Factually incorrect: the paper explicitly discusses this on line 264, attributing it to "the difficulty of unaltered language models in providing effective text representations."
- "Without more baselines (e.g., other GNN variants with text), it is unclear how competitive CoST really is on these larger graphs" — Scope creep; the paper's chosen baselines (BERT + topological contrastive learning) are defensible for its setting.
- "The paper should also cover Y / domain Z / additional tasks" — Demands for breadth outside the paper's stated scope.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the theory-empirics gap as the central tension but do not identify new directions or insights not already implicit in the paper's framing.

## Suggestions

1. **Bridge the theory-empirics gap**: Either provide a self-contained derivation showing how the contrastive losses in Equations (9) and (12) arise from the variational bound in Equation (6), or explicitly reframe the contribution as a heuristic alternating training method motivated (but not derived) by variational inference. Define the \(\mathcal{O}(\theta^2)\) term.
2. **Add error bars**: Report means and standard deviations over at least 3 random seeds for all main results.
3. **Specify experimental details clearly in the main text**: State which PLM variant and which GNN backbone are used for CoST's primary results. Report key hyperparameters (learning rates, batch sizes, \(L\), \(\gamma\), \(\tau\)).
4. **Deepen the analysis of the pretrained GNN underperformance**: Investigate why the initial PLM embeddings are suboptimal and what the alternating procedure specifically recovers.

## Score and Decision

The paper proposes a plausible and empirically effective framework for combining GNNs and PLMs in graph reasoning, with strong results across multiple benchmarks. The core weakness is the gap between the claimed variational derivation and the implemented heuristic contrastive losses — this does not invalidate the empirical contribution but means the paper's value rests on the experimental results rather than the theory. The missing variance reporting and incomplete experimental specifications are addressable concerns.

Given that the paper presents a novel framework with consistent SOTA results across diverse benchmarks, but has a significant theory-empirics gap and incomplete reproducibility details, the paper is a borderline accept with major revisions needed.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>