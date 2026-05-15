Now I have thoroughly verified each claim against the paper. Let me construct the final consolidated review.

## Summary

The paper introduces EBR (Embedding-Based Reasoner), a method that maps $\mathcal{SROIQ}$ description logic concepts to neural semantics using knowledge graph embeddings. The core idea is: (1) convert a DL knowledge base (TBox + ABox) into a knowledge graph of triples, (2) train a KGE (ComplEx via KECI) on this graph, (3) retrieve instances for atomic concepts by thresholding KGE scores, and (4) handle complex concepts (negation, conjunction, disjunction, existential/universal restrictions, cardinality restrictions, nominals) via set operations on the atomic retrieval results. The paper argues this approach is robust to incomplete and noisy KBs where symbolic reasoners fail, and evaluates against HermiT, Pellet, JFact, and Openllet on six datasets.

## Strengths

- **Complete neural semantic mapping for $\mathcal{SROIQ}$ constructs**: The paper defines a systematic mapping from every $\mathcal{SROIQ}$ construct (atomic concepts, negation, conjunction, disjunction, existential/universal restrictions, cardinality restrictions, nominals, self-restrictions) to neural embedding-based retrieval (Section 3.3, Tables 1–2). This goes beyond the expressiveness of prior neural query answering approaches (CQD, GQE, Query2Box, TeMP), which the paper correctly notes are limited to EPFO queries (Section 2.3). The mapping is constructive and requires only pre-trained KGE scores for atomic concepts and existential restrictions.

- **Identifies a genuine gap**: The paper correctly identifies that symbolic DL reasoners (HermiT, Pellet, JFact, Openllet) fail on incomplete or inconsistent KBs — they either return empty result sets or declare inconsistency — and that existing evaluations of these reasoners did not assess robustness to incomplete/noisy data (Section 2.1). This motivates the need for approximate neural approaches.

- **Conceptually clean decomposition**: Reducing instance retrieval for all $\mathcal{SROIQ}$ concepts to atomic concept retrieval + existential restriction retrieval (via a single pre-trained KGE) is elegant and practically appealing, as it decouples the hard learning problem (KGE training) from the retrieval procedure (set operations).

## Weaknesses

### Fatal
None.

### Major

1. **TBox/RBox axioms are not integrated into the retrieval procedure; the method performs set-theoretic retrieval, not logical reasoning.**  
   TBox axioms (GCIs like $C \subseteq D$) and RBox axioms (role hierarchies, transitivity, disjointness) are converted to triples (e.g., $(C,\texttt{rdfs:subClassOf},D)$) and fed to the KGE during training, but they play no explicit role in the retrieval procedure itself (Section 3.3). For example, if the KB contains $C \subseteq D$ and the KGE predicts $a$ as an instance of $C$, there is no mechanism to propagate this prediction to $D$ beyond what the KGE's embeddings may implicitly capture from training. The paper claims to handle "$\mathcal{SROIQ}$ reasoning" but the retrieval for complex concepts is purely set-theoretic (intersection, union, complement, cardinality counting) on thresholded KGE scores for atomic concepts and existential restrictions. This is a substantial gap between the claimed contribution (neural DL reasoning) and the delivered method (KGE-based retrieval with set operations). The paper frames itself as approximating symbolic reasoning but does not analyze where or how the approximation breaks down with respect to TBox reasoning (e.g., subsumption propagation, role hierarchy).

2. **Missing comparison to neural query answering methods on overlapping query types.**  
   The evaluation compares EBR only against symbolic reasoners (HermiT, Pellet, JFact, Openllet) on incomplete/noisy KBs — a setting where symbolic reasoners are known to fail. While this demonstrates EBR's robustness, it does not establish relative merit against existing neural query answering approaches (CQD, Query2Box, GQE) on the query types they do support (conjunction, disjunction, existential restriction). The paper discusses these methods in related work (Section 2.3) and notes they lack support for negation, universal restrictions, and cardinality restrictions — but a comparison on the *overlapping* subset of query types would be the natural way to benchmark performance. Without this, it is unclear whether EBR's advantage comes from its method or simply from the fact that KGE scores are being used at all.

3. **The threshold $\gamma$ is critical but its selection is not discussed.**  
   Every EBR computation (Eqs. 2, 4, 5, 6 for atomic concepts, existential restrictions, and cardinality restrictions) depends on a single threshold $\gamma$ that separates predicted positives from negatives. The paper gives no ablation, no discussion of how $\gamma$ is chosen, whether it is tuned per dataset, or how sensitive the results are to its value. This is a significant methodological gap: different choices of $\gamma$ will produce arbitrarily different result sets, and without understanding how $\gamma$ is set, the reported results cannot be interpreted or reproduced.

4. **The experimental results for noisy/incomplete KBs lack substantive reporting.**  
   The second set of experiments (noisy and incomplete KBs) is described in the setup (Section 4.2) but the results are only mentioned in the conclusion (Section 6) with high-level qualitative statements ("maintained strong retrieval performance, even with up to 80% incompleteness"). No numerical table, no error bars, no comparison numbers, and no analysis of which types of noise or incompleteness affect performance are provided in the extracted text. The reader cannot assess the validity or generalizability of these claims.

### Minor

1. **Ambiguity about open-world vs. closed-world semantics.**  
   The introduction criticizes symbolic reasoners for failing to infer Person(Joe) when the KB lacks this assertion (Section 1). Under open-world semantics, a symbolic reasoner correctly refrains from non-entailed inferences — this is a feature, not a bug. The paper later evaluates in a "closed-world scenario" (Section 4.2) but never clarifies which semantics EBR targets or how the mismatch between these semantic assumptions affects the comparison. This weakens the framing of the paper's motivation.

2. **Role inverse handling is ad hoc and may not work with all KGEs.**  
   The handling of role inverses in Eq. 4 swaps arguments: $\phi'(x, r^{-1}, y) = \phi(y, r, x)$. This assumes the KGE generalizes to seeing $(y,r,x)$ as a valid triple for $r^{-1}$, which is not guaranteed by training only on $(x,r,y)$ triples. The paper does not test or discuss this assumption.

3. **No explicit handling of transitive roles, role chains, or role disjointness.**  
   These are part of $\mathcal{SROIQ}$ (RBox) but the neural semantics provide no mechanism for them. The paper acknowledges RBox axioms but does not show how they are handled in retrieval. If the KGE implicitly learns transitivity from the training data, this should be discussed and tested.

4. **Qualitative results description for the complete-data experiment.**  
   Even accounting for the missing table (parser artifact), the textual description of Table 3 results in Section 5.1 is purely qualitative ("near-perfect," "consistently high," "scores close to or equal to 1.000"). Standard deviations, per-dataset breakdowns, and comparison to symbolic reasoners on the same (complete) data are absent.

### Trivial
None.

## Nice-to-Haves
- An ablation study showing how Jaccard/F1 varies with $\gamma$ for each dataset would substantially strengthen the paper.
- A case study illustrating how EBR handles TBox subsumption (e.g., $C \subseteq D$, with $a$ predicted for $C$) would clarify the role of the KGE in approximating ontological inference.
- Comparison to neural query answering methods (CQD, etc.) on the subset of queries they support would contextualize the contribution.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Table 3 is entirely missing"** — This is a parser artifact. The table exists in the original submission but the PDF-to-text extraction could not render it.
- **"The mapping is mathematically trivial"** — This is a dismissive value judgment, not a concrete weakness. The contribution is the systematic mapping, not its mathematical depth.
- **"CQD already supports existential and universal restrictions, conjunctions, disjunctions, and negation"** — This is factually incorrect. The paper correctly notes CQD supports only EPFO queries (existential, conjunction, disjunction), not universal restrictions or negation in the general case.
- **"The inconsistent KB example is misleading"** — The example is technically sloppy (an inconsistent KB does entail everything), but the broader point that symbolic reasoners struggle with inconsistency in practice is valid, and the example is used only for motivation.
- **"No standard deviations"** — Single-run evaluation is standard practice for KGE-based retrieval benchmarks; requesting confidence intervals goes beyond the norms of this subfield.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution precisely.** The paper should describe EBR as "a set-theoretic retrieval method over KGE-based atomic concept scores" rather than "neural DL reasoning." Explicitly state which aspects of $\mathcal{SROIQ}$ reasoning are approximated and which are not captured.

2. **Add a $\gamma$ sensitivity analysis.** Without this, the results are uninterpretable.

3. **Add comparisons to neural query answering methods** (CQD, at minimum) on conjunction and existential queries. This is the most natural baseline for the claims.

4. **Provide numerical results** for the noisy/incomplete KB experiments with proper tables, including the specific noise levels, datasets, and metric values.

5. **Discuss the OWA/CWA issue explicitly** and clarify which semantics EBR is designed to approximate.

6. **Test TBox reasoning propagation** with a targeted case study (e.g., does EBR retrieve $a$ for $D$ given $C \subseteq D$ and $C(a)$?).

## Score and Decision

The paper makes a genuine contribution by defining a systematic neural semantic mapping for all $\mathcal{SROIQ}$ constructs, and the core idea of reducing complex concept retrieval to atomic KGE scores plus set operations is practically appealing. However, the evaluation is significantly incomplete: it lacks comparison to relevant neural baselines on overlapping query types, provides no discussion of the critical threshold $\gamma$, and reports results for noisy/incomplete KBs only as qualitative claims in the conclusion. The gap between the claimed "$\mathcal{SROIQ}$ reasoning" and the delivered "set-theoretic retrieval with implicit TBox information from KGE training" is substantial and not adequately acknowledged. These weaknesses are addressable but require non-trivial additional experiments and a more precise framing of the contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>