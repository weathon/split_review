Here is my consolidated review:

## Summary

This paper introduces Logical Session Complex Query Answering (LS-CQA), a new task that extends complex query answering to hypergraphs where sessions are ordered hyperedges. The authors propose LSGT (Logical Session Graph Transformer), which linearizes items, sessions, logical operators, and their relations into tokens processed by a standard transformer. The paper provides theoretical analysis of LSGT's expressiveness (WL tests) and permutation invariance, and evaluates on three datasets (Amazon, Diginetica, Dressipi) with 14 query types covering conjunction, disjunction, and negation. LSGT achieves consistent, modest improvements over baselines including session-encoder+query-encoder combinations and existing CQA models.

## Strengths

- **Novel task formulation (LS-CQA).** Extending CQA to hypergraphs with ordered session hyperedges is a meaningful conceptual advance that bridges session-based recommendation and logical query answering. The formalization (Section 2) cleanly handles sessions as N-ary relations within first-order logic expressions.

- **Consistent empirical improvements.** LSGT achieves the best average EPFO MRR across all three datasets (e.g., +0.73 on Amazon, +1.03 on Diginetica, Table 2) and larger gains on negation queries (up to +2.93 on Amazon, Table 3) and compositional generalization (up to +3.22 on Diginetica, Table 4). Improvements are supported by statistical significance markers.

- **Informative ablation study.** The ablation in Table 5 (Table 6 in the paper's numbering) shows that removing logical structure tokens causes a large performance drop (e.g., Amazon average from 31.99 to 15.98) and removing session order causes an even larger drop (to 8.45). This demonstrates that both components contribute meaningfully.

- **Construction of benchmark datasets.** The paper constructs three datasets with 14 query types and full support for first-order logical operators, providing a standardized evaluation setup for LS-CQA that the community can build on.

## Weaknesses

### Fatal
None.

### Major

- **Query generation pipeline is underspecified, harming reproducibility.** The paper states that queries are sampled "by using the sampling algorithm described by [bai2023sequential]" (line 311), but the adaptation of this algorithm to hypergraphs with sessions as ordered hyperedges is not explained. Key details are missing: how anchor sessions are selected, how ground-truth answer sets are determined from held-out edges, and how query difficulty is controlled. The referenced work addresses sequential CQA on KGs, not hypergraphs of sessions, so the necessary modifications are non-trivial. The number of queries per type is referenced as Table~\ref{tab:num_queries} (likely in the appendix) but absent from the main text. Without this description, the evaluation cannot be independently reproduced.

### Minor

- **Permutation invariance claim is asserted but not empirically supported.** Theorem 3 states LSGT "can approximate" operator-wise permutation invariance. However, the paper then uses this property to explain LSGT's advantage over SQE (line 445: "LSGT demonstrates better capability in encoding graph structural inductive bias due to its operation-wise permutation invariance property"). No experiment tests whether the trained model actually exhibits invariance under input permutations (e.g., swapping child nodes of an intersection). While the theorem is a theoretical capacity claim, its use as an explanation for empirical gains requires some verification. The paper uses fixed deterministic node identifiers and positional encodings that could break invariance in practice.

- **Baseline comparison partially confounds two factors.** LSGT processes all raw item embeddings across sessions jointly, while the session-encoder baselines (GRURec/SRGNN/Attn-Mixer + FuzzQE/Q2P) compress each session into a single vector before query encoding. This means LSGT's advantage could come from (a) avoiding information loss from session compression, (b) the specific logical-structure tokenization, or (c) both. The "w/o Logic Structure" ablation (Table 5) partially addresses this by showing that removing logical structure tokens hurts performance, establishing that the tokenization matters beyond raw item access. However, a cleaner control — e.g., a transformer with the same item visibility but a simpler operator encoding — would more cleanly isolate the benefit of LSGT's specific graph tokenization versus the general advantage of avoiding compression.

- **WL expressiveness theorems are loosely connected to the task.** Theorems 1 and 2 establish that LSGT is at least as expressive as 1-RWL and session-encoder+query-encoder models under WL tests. However, LS-CQA requires learning to project, intersect, union, and negate over semantic item embeddings — not just distinguishing non-isomorphic query graphs. The paper does not bridge this gap to explain why WL expressiveness should translate to better query answering performance on this task. The theorems are technically correct but read as mathematical decoration rather than substantive support for the method's design.

### Trivial
None.

## Nice-to-Haves

- An empirical permutation invariance test (measuring embedding similarity under operator input swaps) would directly validate the claimed property.
- A baseline with the same transformer architecture and item visibility but a simpler operator encoding (e.g., operator type sequence without explicit graph edges) would cleanly separate the benefit of LSGT's specific tokenization from the advantage of avoiding session compression.
- An analysis of which specific query types drive the overall improvement, beyond the aggregate MRR numbers.

## Removed Points

- "Number of queries per type and per dataset not in main text" — This table likely lives in the appendix, which the parser strips from all papers. The paper's main text references it.
- "Missing appendix details" — Parser strips appendices from all papers; they exist in the original submission.
- "Dressipi results are near ceiling (96-98 MRR)" — The paper explicitly addresses this (lines 451-452), noting the low attribute diversity of the fashion domain and that all models reflect this property.
- "Task not evaluated against a human-defined gold standard" — Standard evaluation practice in CQA; not a weakness of this paper specifically.
- "No discussion of alternative formulations (rule-based, KG re-formulation)" — Scope creep; the paper covers a reasonable set of baselines within its stated direction.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Describe the query generation pipeline in detail.** Include how anchor sessions are selected, how ground-truth answer sets are derived, and how the sampling algorithm from Bai et al. 2023 is adapted to hypergraphs of sessions. A short pseudocode block would suffice.
2. **Add an empirical permutation invariance test.** Swap the child nodes of an intersection/union operator and measure the cosine similarity of the resulting query embeddings. If the model is approximately invariant, the similarity should be near 1.0.
3. **Either verify the permutation invariance claim or soften the language** about it driving performance improvements.
4. **Acknowledge the compression confound explicitly** and discuss what the ablation study does and does not establish about the contribution of graph tokenization.

## Score and Decision

The paper defines a worthwhile new task, proposes a sensible architecture, and provides consistent though modest empirical improvements backed by informative ablations. The main weakness affecting the paper's contribution is the underspecified query generation pipeline, which harms reproducibility, and the unverified invariance claim that is used to explain performance. These are addressable but as presented, the paper's evidence does not fully resolve whether LSGT's specific graph tokenization or the general advantage of avoiding session compression drives the gains.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>