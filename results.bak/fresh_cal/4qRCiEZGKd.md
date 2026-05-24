I now have a complete picture of the paper and both reviews. Let me construct the final consolidated review.

## Summary

The paper introduces EBR (Embedding-Based Reasoner), which maps the full SROIQ description logic syntax to operations on a thresholded neural link predictor. The core idea is to replace symbolic DL reasoning with set operations on entities ranked by a pre-trained KGE model (ComplEx via KECI), enabling instance retrieval for any SROIQ concept from only the learned embeddings. The paper claims robustness to incomplete and inconsistent KBs, a setting where symbolic reasoners fail.

## Strengths

- **Complete neural semantics for SROIQ (Section 3.3, Equations 2–6, Table 2):** The paper provides explicit, algebraic mappings for every SROIQ construct — atomic concepts, negation, conjunction, disjunction, existential/universal restrictions, cardinality restrictions, nominals, and self restrictions — using only a link predictor φ and a threshold γ. This is the first work to define such a complete mapping for an expressive DL, and the derivations are clearly presented.

- **Principled derivation of complex restrictions:** Universal restrictions are derived from the standard DL equivalence ∀u.C = ¬(∃u.¬C) (Equation 5), and cardinality restrictions are defined via set cardinality on scored neighbors (Equation 6). Role inverses are handled explicitly (Equation 4). The approach follows naturally from atomic retrieval, showing a theoretically grounded translation rather than a black-box approximation.

- **Inference without storing the KB:** The paper correctly identifies (Section 3.1, contributions) that after the KGE model is trained, only the learned embedding parameters are needed for instance retrieval — the original ABox and TBox are not required at inference time, enabling a form of memory-efficient reasoning.

- **Evaluation across diverse domains:** The closed-world evaluation (Section 5.1) covers six datasets spanning biological (Carcinogenesis, Mutagenesis), religious (Semantic Bible), historical (Vicodi), and family domains (Father, Family), demonstrating generality.

## Weaknesses

### Fatal
None.

### Major

- **Open-world-to-closed-world semantic shift for universal and cardinality restrictions is unacknowledged.** The mapping for universal restrictions (∀u.C = ¬(∃u.¬C), Equation 5) and cardinality restrictions (Equation 6) relies on a threshold γ to decide whether an entity is a filler of a role. This implicitly assumes a closed-world interpretation: entities scoring below γ are treated as non-fillers. In standard SROIQ DL semantics, universal and cardinality restrictions are interpreted under the open-world assumption — the absence of a known filler does not imply that no filler exists. The paper neither acknowledges this semantic shift nor argues why the closed-world approximation is appropriate for the intended setting (incomplete KBs). This is a methodological gap that affects the validity of instance retrieval for these constructs regardless of the experimental results. The paper claims robustness to *incompleteness*, but the semantics itself assumes complete knowledge of role fillers.

- **Threshold γ is central but its selection and sensitivity are unaddressed.** The threshold γ appears in every definition in Section 3.3 — it determines atomic concept membership, existential restriction fillers, and cardinality counts — yet the paper only calls it "a preset threshold γ > 0" (Section 3.3) with no discussion of: (1) how γ is chosen, (2) what specific value(s) are used, (3) whether it is tuned per dataset or per concept, or (4) how sensitive the results are to its value. This is especially critical for cardinality restrictions, where the count |{y | φ′(x,u,y) ≥ γ ∧ y ∈ EBR(C)}| is directly γ-dependent. Without this information, the reported results cannot be interpreted or reproduced.

### Minor

- **Training details are absent.** The link predictor (KECI/ComplEx) must be trained on the KB, but the paper provides no information about: negative sampling strategy, number of training epochs, optimizer, learning rate, embedding dimensionality, or whether the same training protocol was used across all six datasets (Section 4.1 just names the datasets). This hinders reproducibility.

- **Evaluation reporting is extremely sparse.** The entire results section for the first experiment (Section 5.1) consists of four lines of qualitative text claiming "near-perfect Jaccard and F1 scores" and "scores close to or equal to 1.000." No actual numbers, per-concept breakdowns, variance estimates, or the specific γ values used are provided. Table 3 is referenced but the content is not visible. Even accounting for parser artifacts, the prose discussion is minimal.

- **No runtime comparison despite claims of GPU-speed advantage.** The introduction and contributions claim that EBR can leverage GPUs for efficient handling of large-scale computations, but no runtime measurements are provided. Even a simple comparison of retrieval time per query on a single dataset would substantiate this claim.

- **Insufficient differentiation from CQD on expressivity.** The paper states that CQD "do[es] not support negations, universal restrictions, and cardinality restrictions" (Section 2.3). However, CQD also uses a pre-trained link predictor and decomposes complex queries. The paper would benefit from a clearer discussion of whether CQD's decomposition framework could be extended to these constructs, and if so, what specific novelty EBR adds beyond the threshold-based binarization.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of how the neural semantics relates to standard DL semantics for universal and cardinality restrictions — clarifying whether EBR is intended as a practical closed-world approximation (sacrificing soundness for robustness) or as a novel neural semantics with its own interpretation.
- A sensitivity analysis of γ on a representative dataset would substantially strengthen the empirical claims.
- Adding a table with dataset statistics (number of individuals, concepts, roles, axioms) would help contextualize the evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Absent experimental evidence for robustness claims" (Harsh Critic #1):** The harsh critic asserts that the paper's central claim (robustness to incompleteness and inconsistency) is entirely unsupported because the second experiment's results are absent. **Reason for removal (parser artifact):** The extracted text has systematic evidence of missing content — Table 3 (explicitly referenced in Section 5.1) is also absent, and the Conclusion (Section 6) makes specific quantitative claims ("up to 80% incompleteness," "10% and 20% noise levels") that strongly indicate the results existed in the original submission but were lost during PDF-to-text extraction. While the evaluation section *as extracted* is indeed incomplete, this is plausibly a parsing artifact rather than a paper flaw. I retain the *sparse reporting* concern as a Minor weakness above.

- **"No plausible operational definition of noise/inconsistency" (Harsh Critic #3, partially):** The paper defines noise as "adding false assertions or axioms" (Section 4.2). This is an operational definition; the harsh critic's demand for logically contradictory KBs (A(a) and ¬A(a)) goes beyond what the paper scoped. **Reason for removal:** The paper provides a reasonable operational definition; the critic is demanding a different evaluation design.

- **"Introductory inconsistency example is misleading" (Harsh Critic, abstract/introduction notes):** The critic says the example is "correct but misleading" because the reasoner "would not give an answer at all, not that it returns the wrong answer." **Reason for removal (factually wrong):** The paper says "a classical symbolic reasoner cannot determine the membership" — this is exactly what the critic claims it should say. The paper never says the reasoner returns the wrong answer; it correctly says the reasoner cannot determine membership.

- **"CQD could be extended — novelty is smaller" (Harsh Critic, Section 2.3/2.4):** **Reason for removal (speculative):** This is an untested speculation about what CQD *could* do, not a concrete weakness of the paper. The paper correctly states CQD's known limitations.

- **"Strength #2: Robustness under severe incompleteness" (Strength Finder):** This strength claims the paper reports robustness with up to 80% missing assertions, citing Section 6. **Reason for removal (not supported by visible evidence):** Section 6 is the Conclusion, not an experimental results section. The claims in the Conclusion are unsupported by visible data in the extracted text. What the Strength Finder treats as evidence are actually the paper's own forward-looking claims.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a discussion section on the semantic assumptions** of the neural mapping, specifically addressing the open-world vs. closed-world tension for universal and cardinality restrictions. Clarify whether EBR is a closed-world approximation or a novel neural semantics with its own interpretation.

2. **Provide explicit details about γ** (value, selection method, per-dataset variation) and include a sensitivity analysis showing how results change with γ.

3. **Augment the evaluation** with the missing experimental results (incomplete/noisy KBs, comparison with symbolic reasoners) as described in Section 4.2. Include actual numerical results in a table with standard deviations if multiple runs were performed.

4. **Add runtime measurements** comparing EBR's query time against symbolic reasoners to substantiate the scalability claim.

5. **Provide training hyperparameters** (embedding dimension, negative sampling strategy, number of epochs, optimizer) for reproducibility.

## Score and Decision

The paper presents a clear and complete neural semantics mapping for SROIQ — a genuine contribution. However, the evaluation as presented is too sparse to fully support the paper's central robustness claims, and the unacknowledged open-world/closed-world semantic shift for universal and cardinality restrictions is a significant methodological gap that needs resolution. The paper requires major revision before it can be accepted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>