Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper proposes EBR (Embedding Based Reasoner), a neural approach that uses a pre-trained knowledge graph link predictor (KECI/ComplEx) to perform approximate instance retrieval for SROIQ description logic concepts. The main technical contribution is a mapping from SROIQ concept syntax (including negation, conjunction, disjunction, existential/universal restrictions, cardinality restrictions, and nominals) to neural semantics that requires only atomic concept and existential restriction retrieval as primitives. The paper claims this enables robust reasoning on incomplete and noisy KBs where symbolic reasoners fail.

## Strengths

- **Complete neural semantics for SROIQ concept expressions**: Section 3.3 and Table 2 define a principled mapping from all SROIQ concept constructs to neural semantics. The key insight — that only atomic concept retrieval and existential restriction retrieval are needed as primitives, with other constructs derived via set operations — is technically sound and distinguishes EBR from prior neural query answering methods (CQD, GQE, Query2Box) which do not support negation, universal restrictions, or cardinality restrictions (Section 2.3).

- **Near-perfect retrieval on complete and consistent KBs**: Section 5.1 reports that in closed-world evaluation, EBR achieves Jaccard similarity and F1 scores close to 1.000 across six datasets for named concepts, negations, intersections, unions, existential/universal restrictions, and cardinality restrictions. This validates that the neural semantics accurately approximate symbolic instance retrieval on ideal data. (Table 3, referenced in the paper, is likely a parser-stripped image; the textual description is present.)

- **Well-motivated problem and approach**: The paper correctly identifies that real-world KBs are often incomplete and inconsistent, and that symbolic reasoners are fundamentally limited in such settings. Using a link predictor trained on KG-encoded KB data (including `rdfs:subClassOf` triples from GCIs) is a reasonable approximate strategy for instance retrieval under these conditions.

## Weaknesses

### Fatal

None.

### Major

1. **The noise/incompleteness experimental results that constitute the paper's central claim are entirely absent.** The paper describes the experimental setup for noise and incompleteness experiments in Section 4.2 but presents no results section for them — there is no Section 5.2, no tables, no figures, and no numerical data. The conclusion asserts that EBR "significantly outperforms traditional symbolic reasoners" and "maintained strong retrieval performance, even with up to 80% incompleteness" with "high Jaccard similarity in noisy datasets with 10% and 20% noise levels," but none of these claims are backed by any data in the provided paper. Since robustness to incompleteness and noise is the paper's primary claimed differentiator from symbolic reasoners (Abstract, Introduction, Conclusion), the absence of this evidence means the paper's central contribution is unsubstantiated.

2. **Scalability claims are unsubstantiated.** The paper claims (Section 1, contributions) that "instance retrieval can be tackled without storing knowledge bases in memory" and "inference time can be decreased by leveraging GPUs." No runtime experiments, memory usage measurements, or scaling analyses are provided. Given that computing EBR for complex concepts may require scoring all entities against multiple relations (e.g., cardinality restrictions require counting related entities above threshold γ), the computational cost is non-trivial and should be empirically characterized.

3. **No comparison with relevant neural query-answering baselines.** The paper compares only against symbolic reasoners (HermiT, Pellet, JFact, Openllet), which are designed for sound and complete logical entailment under the open-world assumption — a fundamentally different task. The natural peer group for approximate instance retrieval over incomplete graphs are neural query-answering methods (CQD, Query2Box, TeMP, Andresel et al.'s ontology-aware extensions), which the paper discusses in related work but does not compare against. Without this comparison, it is impossible to assess whether EBR's approach adds value over existing neural methods for complex query answering. The paper claims EBR supports negation, universal, and cardinality restrictions, which prior methods do not, but provides no experiments demonstrating this advantage.

4. **The comparison with symbolic reasoners is framed in an apples-to-oranges manner.** The paper repeatedly characterizes symbolic reasoners as "failing" or being unable to handle incompleteness/inconsistency. Symbolic reasoners correctly refrain from inferring statements that do not follow logically — this is by design, not a failure. When a KB is inconsistent, they correctly report inconsistency; they do not "fail." The paper's framing conflates a design limitation (soundness under the open-world assumption) with a bug. A honest framing would acknowledge that symbolic and neural approaches solve different tasks, and position EBR as complementary rather than superior.

### Minor

5. **TBox/RBox axiom-driven inference is handled only indirectly and without analysis.** The paper extracts GCIs as `(C, rdfs:subClassOf, D)` triples and trains the link predictor on them alongside instance assertions. This means the link predictor may learn statistical associations that approximate some GCI-driven inferences, but there is no guarantee or formal analysis. For example, if the TBox contains `∃r.A ⊑ B`, EBR will never infer that an entity satisfying `∃r.A` should be classified under `B` unless the link predictor happens to learn this from co-occurrence in the training graph. The same holds for role characteristics (transitivity, symmetry, disjointness). The paper should explicitly scope this limitation rather than claiming "SROIQ reasoning."

6. **Missing methodological details hinder reproducibility.** The value of threshold γ is never specified or justified, yet it directly controls the precision/recall trade-off. Training details for the link predictor (splits, negative sampling strategy, number of epochs, hyperparameter settings) are not provided. The paper states that KECI with p=0, q=1 is used (equivalent to ComplEx), but does not specify embedding dimensionality or training configuration. Some of these may be in the supplemental material (referenced in Section 3), but key choices like γ should be in the main paper.

### Trivial

7. The abstract opens with "Concept learning exploits background knowledge..." which frames concept learning as the motivation, but the paper is about instance retrieval, not concept learning. This creates a mild framing mismatch.

## Nice-to-Haves

- A comparison against neural query-answering methods (CQD, Query2Box) on the same incomplete/noisy KBs would substantially strengthen the paper.
- Analysis of how the threshold γ affects precision/recall, and a description of how it was selected (e.g., cross-validation).
- A concrete example illustrating whether and how TBox axioms like `∃r.A ⊑ B` are captured after link predictor training, or explicit acknowledgment that such inferences are not guaranteed.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Table 3 is missing"** (from Harsh Critic): Table 3 is referenced in Section 5.1 and is highly likely a parser-stripped image (Tables 1 and 2 appear as image references in the extracted text for the same reason). The textual description of the closed-world results is present.
- **"Symbolic reasoners comparison is meaningless"** (overly strong version): While the comparison is conceptually asymmetrical, it is not *meaningless* — the paper's argument is precisely that symbolic reasoners cannot answer instance queries when data is incomplete, motivating a neural alternative. The comparison has limited value but is not invalid. Framed more carefully (as in Major #4 above), the concern is about framing, not invalidity.
- **Strength: "Demonstrated robustness to incompleteness and noise"** (from Strength Finder): This strength cites the conclusion. Since no experimental results for these conditions appear in the paper, this strength is unsubstantiated and conflicts with verified weaknesses. Removed.
- **Strength: "GPU-accelerated inference" and "Memory-efficient operation"** (from Strength Finder): These are claims from the introduction, not demonstrated capabilities. No evidence supports them. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Present the noise/incompleteness experimental results** with tables and figures showing retrieval performance as a function of noise/incompleteness level. Include a comparison with the symbolic reasoners mentioned (HermiT, Pellet, JFact, Openllet) and ideally with neural QA baselines (CQD, Query2Box). Without this, the paper's central claim is unverifiable.

2. **Re-scope the paper's claims.** Replace "SROIQ reasoning" with "SROIQ concept instance retrieval" and explicitly acknowledge that TBox/RBox axiom-driven logical deduction is not guaranteed — the link predictor only captures statistical associations from the KG encoding. This would make the paper's actual contribution clearer and more defensible.

3. **Add runtime and memory measurements** to ground the scalability claims, or remove them.

4. **Specify the threshold γ** and describe how it was chosen. Provide a sensitivity analysis.

5. **Reframe the comparison with symbolic reasoners** to acknowledge their different design goals. The paper would be stronger if it positioned EBR as a complementary approximation technique for settings where symbolic reasoning is not applicable (incomplete/noisy KBs), rather than claiming superiority on a task symbolic reasoners were not designed to solve.

## Score and Decision

The paper introduces a technically interesting mapping from SROIQ concept syntax to neural semantics. The closed-world validation suggests the neural semantics can accurately approximate symbolic retrieval on complete data. However, the paper's central claim — robustness to incompleteness and noise — is entirely unsupported by experimental evidence in the provided text. No results are presented for the noise/incompleteness experiments that the paper itself describes and that the conclusion references. Scalability claims are similarly unsubstantiated. The comparison with symbolic reasoners is framed in a way that does not fairly represent their design purpose, and no comparison is made against relevant neural QA baselines. In its current form, the paper presents an interesting idea but does not deliver the evidence needed to support its core claims. Major revisions including a complete set of comparative experiments are required.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>