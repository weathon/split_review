## Summary

The paper investigates whether LLM-generated bibliographies (from GPT-4o and Claude Sonnet 4.5) can be distinguished from human-curated citation networks using graph topology and semantic embeddings. Working with 10,000 focal papers (~275k references) from SciSciNet, the authors construct paired citation graphs and a field-matched random baseline, then apply a progressive modeling strategy: structural feature RFs (~0.60 accuracy distinguishing LLM vs. ground truth), embedding-based RFs (~0.83), and GNNs with embedding node features (~93% test accuracy). The main finding is that LLMs convincingly reproduce the topology of citation networks but leave detectable semantic fingerprints—detection therefore should target content signals rather than graph structure.

---

## Strengths

- **Large-scale, well-constructed dataset.** 10,000 focal papers with ~275k references drawn from a curated scientometric database provides strong statistical power, and the paired construction (same focal paper → human vs. LLM references) is a rigorous design.
- **Clean and informative progressive decomposition.** The stepwise progression from structural-only descriptors (RF ~0.60) → embedding-level RF (~0.83) → GNNs (~0.93) is elegant and directly answers "what carries the signal," resulting in a clear actionable conclusion for the community.
- **Extensive robustness checks.** The authors replicate across two LLM families (GPT-4o, Claude Sonnet 4.5), two embedding models (OpenAI text-embedding-3-large and SPECTER2), three random baselines (field-level, subfield-level, temporally-constrained), and run cross-generator transfer experiments. Very few ICLR papers provide this level of validation.
- **Cross-generator generalization.** Training on GPT-4o graphs and testing on Claude Sonnet 4.5 yields above-chance accuracy (~0.72 RF, substantial GNN generalization), suggesting the semantic fingerprint reflects a shared LLM-class artifact rather than model-specific idiosyncrasy.
- **Transparent reporting.** Distributions of validation accuracy across hyperparameter sweeps (500 configurations per model) rather than cherry-picked top results, combined with standard deviations across 10 random seeds, supports reproducibility and honest comparisons.
- **Practical significance.** The finding that structure-only diagnostics will "under-detect" LLM bibliographies provides direct guidance for audit tools and citation recommendation systems, which is highly relevant as LLM-assisted literature review becomes widespread.

---

## Weaknesses

### Fatal
None.

### Major

1. **The semantic fingerprint is demonstrated but not explained.** The paper's most important positive finding is that embeddings expose a learnable semantic difference, yet there is no analysis of *what* semantic dimensions drive the discrimination. The 3072-dimensional embedding space is treated as a black box, and the RF leaf-depth analysis only confirms that early splits are discriminative—not what they split on. Given that prior work (Algaba et al., 2025, which is the source of the data) already identifies specific LLM biases (recency preference, prestige amplification, Matthew effect), even a simple attribution analysis—e.g., are top RF splits correlated with average publication year, venue prestige, or topical drift?—would elevate the contribution substantially and make the debiasing recommendation concrete rather than aspirational.

2. **The RF-to-GNN accuracy jump (~0.83 → 0.93) is not properly ablated.** The GNN experiments use embedding *and* structure jointly (node features = 3072-d embeddings, propagated via message-passing over the citation graph). Because the RF baseline uses only aggregated (summed) embeddings without leveraging relational structure, the GNN advantage likely comes from joint structure+semantics, but the paper attributes it to embeddings and does not isolate the contribution of the structural message-passing on top of embeddings. A simple ablation—GNN with embeddings but no edges (i.e., an MLP)—would clarify whether message-passing adds anything once rich embeddings are available.

3. **Potential confound in size-matching.** When matching the size of ground truth and random graphs to the (typically smaller) generated graph by randomly removing references, the removal is random but undirected—this could alter structural statistics. There is no analysis of whether the removal procedure is size-biased (e.g., preferentially destroying triadic closure) or whether alternative matching strategies affect results.

### Minor

1. **Sum pooling is used without justification.** Graph-level embedding features are formed by summing reference embedding vectors. Mean or attention-weighted pooling could behave differently in high dimensions; the choice of sum is not motivated or compared.

2. **Cross-generator results are relegated to appendix and under-discussed.** The finding that semantic fingerprints generalize across generator families is arguably more policy-relevant than the within-LLM result, but it receives only two sentences in the main text.

3. **The random baseline removes only 779 graphs (8.4%) from GPT-4o set**, while retaining 9,218 graphs. It is unclear whether these removals are biased toward certain fields or paper characteristics, which could affect structural comparisons.

### Trivial

- Table 3 header symbols for Accuracy/F1 appear as LaTeX arrows in the extracted text, likely a parser artifact.

---

## Nice-to-Haves

- A feature-importance or SHAP analysis of what semantics drive RF discrimination (e.g., recency-weighted embedding centroids, venue-specific signals) would transform a "what" finding into a "why" finding.
- An MLP baseline with the same 3072-d embeddings (no graph structure) would cleanly isolate the added value of GNN message-passing.
- Including a qualitative case study (e.g., two matched focal papers where LLM vs. human choice diverges the most in embedding space) would make the abstract finding concrete for readers.

---

## Novel Insights

The most genuinely novel insight is that LLMs achieve *structural mimicry* of citation networks—matching not just individual graph statistics but their joint multivariate relationships (e.g., degree–clustering coupling, density scaling)—while simultaneously leaving a learnable semantic fingerprint. Prior work had documented single-statistic alignment; this paper demonstrates multi-feature joint alignment and, critically, the gap between structural realism and semantic realism. The cross-generator experiment further suggests the semantic fingerprint is a shared LLM-class property (rather than model-specific noise), which is important for designing robust detection methods. The practical implication—that topology-based auditing will systematically under-detect LLM bibliographies—is a concrete and actionable contribution not previously established at this scale or rigor.

---

## Suggestions

- Add a simple MLP experiment (same 3072-d node features, no message-passing) to isolate the contribution of graph structure in the GNN results.
- Add at least one interpretability analysis: project the discriminative embedding dimensions onto known bibliometric features (publication year, venue tier, citation count, author count) to give meaning to the "semantic fingerprint."
- Report the cross-generator result in the main text with at least one table; it is one of the strongest robustness claims.
- Discuss whether the semantic signal might be entirely attributable to the well-documented LLM recency/prestige biases (i.e., can you explain away the ~0.83 accuracy by conditioning on year and venue statistics?).

---

## Score and Decision

The paper makes a solid empirical contribution to a timely and consequential problem: it is large-scale, well-controlled, robustly validated, and produces a clear actionable finding. The main gap—not explaining *what* semantic dimensions drive separability—limits impact but is acknowledged as future work. The progressive experimental design, cross-LLM replication, and practical guidance are notable strengths that place this clearly in the accept range for the ICLR community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>