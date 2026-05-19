- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6
Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper proposes the Logical Session Complex Query Answering (LS-CQA) task, extending complex query answering (CQA) to hypergraphs where sessions are treated as ordered hyperedges of items and attributes. It introduces the Logical Session Graph Transformer (LSGT), which tokenizes items, sessions, logical operators, session structures, and logical structures into a unified sequence processed by a standard Transformer encoder. The method is evaluated on three datasets (Amazon, Diginetica, Dressipi) across 14 query types including negation and out-of-distribution queries, achieving state-of-the-art results.

## Strengths

- **Formalization of LS-CQA as a well-defined task.** The paper extends CQA to hypergraphs with ordered hyperedges (Section 2), providing a clean problem formulation with FOL queries over sessions, items, and attributes. The distinction from hyper-relational KG CQA (where n-ary facts lack order information) is clearly stated, and the task bridges session-based recommendation and logical query answering in a principled way.

- **Consistent state-of-the-art results across three datasets.** LSGT achieves the highest average EPFO MRR on all three datasets: Amazon (33.26, +0.73), Diginetica (44.16, +1.03), and Dressipi (74.10, +0.82) — with statistical significance marked (Tables 2–3). On negation queries, gains are larger (+2.93, +2.13, +1.92). Gains on out-of-distribution query types range from +1.28 to +3.22 MRR (Table 4/OOD).

- **Strong compositional generalization to unseen query types.** LSGT outperforms all baselines on zero-shot query types (3iA, 3ip, 3inA, 3inp) across all three datasets (Table 4), demonstrating that the token-based encoding generalizes to complex logical structures not seen during training. This is a concrete advantage over sequence-linearization approaches like SQE.

- **Ablation study confirms the contribution of each component.** Removing logical structure tokens causes a dramatic performance drop (e.g., Amazon average MRR falls from 31.99 to 15.98), and removing session order information degrades performance further (to 8.45). This empirically validates the design choices (Table "Tab:ablation").

- **Theoretical analysis of expressiveness and permutation invariance.** The paper proves (Theorems 1–3) that LSGT is at least as expressive as 1-RWL and can approximate operator-wise permutation invariance — properties that distinguish it from sequence-based encoders like SQE and justify its architectural choices.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Framing-to-evaluation gap on "understanding intentions."** The paper's title, abstract, and introduction motivate the work with real user scenarios (e.g., "Nike or Adidas running shoes," "not another mattress"). However, the evaluation is entirely on synthetically sampled logical queries from a hypergraph (Section 6: "we conduct sampling of fourteen types of logical session queries"), following standard CQA methodology. The paper never demonstrates that these query structures correspond to actual user intents expressed in natural language or search behavior. While this is standard practice in the CQA literature, the ambitious framing ("Understanding Inter-Session Intentions") creates a gap that the paper does not bridge. This does not invalidate the technical contribution but limits the external validity of the claimed motivation.

- **Why session order information matters is not explained.** The paper treats sessions as *ordered* hyperedges (Section 2.1), uses positional encoding for items within sessions (Section 4.2), and the ablation shows that removing order information causes a catastrophic performance drop (e.g., Amazon average MRR 31.99 → 8.45). However, the logical queries in LS-CQA only check membership ("exists a session containing these items"), not sequence order. The paper's explanation — "item orders within each session play a crucial role" — is circular and does not identify *why* order matters for membership queries. Is order a proxy for item relevance or purchase completion? Does it help the model distinguish "browsed-and-abandoned" from "browsed-and-purchased"? The paper provides no analysis, leaving a conceptual puzzle: if order is logically irrelevant to the queries, its outsized empirical importance suggests the model may be relying on it as a confounding signal rather than for its claimed purpose of "capturing meaningful order information."

- **Random orthonormal node identifiers adopted without task-specific justification.** The paper follows Kim et al. (2022) in using random orthonormal vectors as node identifiers (Section 4.1). This design choice is not analyzed or justified for the LS-CQA setting — e.g., whether learned embeddings would work as well or better, how the random vectors interact with the Transformer's attention over the combined item/session/operator sequence, or what role they play beyond node disambiguation. Given that identifiers appear twice in the input ($\mathbf{P}_p$ is concatenated twice), the absence of any analysis or ablation on this component is a gap.

- **Missing complexity analysis.** The Transformer processes sequences of length $O(n+m+w)$ (items + session-structure tokens + logical-structure tokens). The paper does not report typical or maximum sequence lengths per dataset, inference time, or memory cost relative to baselines. This makes it difficult to assess the practical cost of the method's architectural complexity.

- **Modest gains on EPFO queries and inconsistent per-type performance.** Average EPFO improvements are small (+0.73, +1.03, +0.82 MRR), and on several individual query types (e.g., 2is, ip) LSGT is not the best method. The paper acknowledges this for 2is/ip (Section 6.4, "the any-to-any attention mechanism may not be necessary") but does not analyze *why* these query types resist improvement, nor does it discuss whether the gains on other types warrant the architectural overhead.

### Trivial
None beyond standard formatting issues caused by the text extraction pipeline.

## Nice-to-Haves

- A small-scale validation connecting synthetic LS-CQA queries to real user search or session behavior (e.g., manually annotated query-to-intent mappings) would substantially strengthen the task motivation.
- Analysis of which query types LSGT systematically fails on (error analysis by query structure and answer type).
- Reporting of maximum sequence lengths and training/inference throughput relative to baselines.

## Removed Points

These points were identified in the reviews but are removed with justification:

1. **"Theoretical claims unverifiable (appendix missing)"** — Per hard rules: the parser strips appendices from all papers; the proofs exist in the original submission. Not a valid criticism.
2. **"NQE's low performance suggests suboptimal use"** — Speculative; no evidence of suboptimal tuning is provided. The paper states consistent hyperparameter settings.
3. **"Paper conflates session-based recommendation with CQA in related work"** — The related work clearly distinguishes these lines (Section 3 subsections); the paper uses session encoders as baselines but does not conflate the fields.
4. **"The difference between session and n-ary relation is not substantive"** — The paper explicitly defines sessions as *ordered* hyperedges (Section 2), which is a real distinction from n-ary facts in hyper-relational KGs. The ablation validates that order matters empirically.
5. **"The OOD query types are still synthetic"** — This is redundant with the framing-gap weakness already included above; the OOD generalization results are valid as a technical contribution regardless.
6. **Formatting, grammar, and style nitpicks** — Per hard rules, these are parser artifacts or non-substantive.

## Novel Insights

The harsh critic identifies a genuine tension between the paper's framing ("understanding intentions") and its methodology (synthetic query evaluation on a hypergraph), but this mirrors standard practice across the CQA field — Query2Box, BetaE, and others also evaluate on synthetic queries without mining real user queries. The more interesting observation, which neither reviewer fully develops, is the disconnect between the claim that sessions are *ordered* hyperedges (presented as the key novelty distinguishing LS-CQA from hyper-relational CQA) and the fact that the LS-CQA queries only test *membership* — never sequence order. The ablation's dramatic collapse when order is removed (31.99 → 8.45 MRR) suggests the model is exploiting order as a powerful discriminative signal, but the paper neither identifies what that signal is nor justifies why a task claiming to bridge to real user intentions should depend on it. This is the most substantive unaddressed issue in the paper.

## Suggestions

1. Add an analysis of *what* information the positional encoding captures — is it item recency, purchase vs. browse distinction, or session-level temporal patterns? This would resolve the conceptual puzzle about why order matters for membership queries.
2. Include a brief complexity table (max sequence length, GPU memory, inference time) to help readers assess practical cost.
3. Add a small-scale validation or case study connecting synthetic LS-CQA queries to plausible real user intents, or explicitly reframe the paper's claims to match the synthetic evaluation.
4. Ablate the random orthonormal identifiers vs. learned identifiers to justify that design choice.
