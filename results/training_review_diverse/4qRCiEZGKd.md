Now I have all the evidence I need. Let me compile the consolidated review.

## Summary

This paper proposes EBR (Embedding-Based Reasoner), a method that maps Description Logic (SROIQ) concept retrieval to neural semantics using a pre-trained knowledge graph embedding model. The key insight is that instance retrieval for any SROIQ concept can be reduced (recursively via set operations) to retrieval for atomic concepts and existential restrictions, both of which rely on thresholded scores from a single neural link predictor. The paper evaluates EBR on six DL benchmark datasets and claims strong performance under incompleteness and noise, outperforming symbolic reasoners.

## Strengths

- **Novel and clean mapping from full SROIQ syntax to neural semantics using only a single link predictor.** The paper defines EBR for atomic concepts, negation, conjunction, disjunction, existential/universal restrictions, cardinality restrictions, and nominals via set operations over thresholded KGE scores (Section 3.3, Equations 1–5, Table 2). The reduction of all constructors to atomic concept retrieval and existential restriction retrieval is a non-trivial and well-designed insight that allows the approach to handle the full expressivity of SROIQ without requiring a specialized architecture for each constructor.

- **Clear and thorough positioning against prior work.** The paper systematically surveys symbolic reasoners (Section 2.1), KGE models (Section 2.2), neural query answering methods including CQD, GQE, Query2Box (Section 2.3), and DL embedding techniques (Section 2.4). It correctly identifies that prior neural approaches are limited to EPFO queries and do not support negation, universal restrictions, or cardinality restrictions, establishing a clear gap that EBR aims to fill.

- **Addresses a genuine practical problem.** Symbolic DL reasoners indeed struggle with incomplete and inconsistent KBs — a critical issue for real-world KGs like Wikidata and DBpedia. The motivation for an approximate, noise-tolerant approach to instance retrieval is well-articulated and practically relevant.

## Weaknesses

### Fatal
None.

### Major

- **The evaluation does not test whether the KGE captures logical entailments from the TBox.** The closed-world experiment on "perfect KBs" (Section 5.1) compares EBR's retrieved instances against the ground-truth ABox — i.e., the set of explicit triples the KGE was trained on. This measures how well the KGE memorizes its training data, not whether it performs reasoning. The central claim of being a "reasoner" requires showing that the KGE assigns high scores to logically entailed triples that are *not* explicitly present (e.g., inferring `(Alice, type, Human)` from `(Alice, type, Person)` and `(Person, subClassOf, Human)`). The paper needs to evaluate against the **deductive closure** computed by a symbolic reasoner on the same KB — without this, the method is only validated as a KGE-based retrieval system that reads off known triples.

  The Conclusion mentions strong results under 80% incompleteness and noise, but these experiments are absent from the extracted manuscript (presumably due to parser truncation). Even if present in the full submission, the core issue remains: without a test against the deductive closure, results on incomplete KBs only show that the KGE tolerates missing triples, not that it correctly infers what a symbolic reasoner would.

### Minor

- **No comparison against neural query answering baselines on shared query types.** The paper acknowledges CQD (Arakelyan et al., 2021) in related work and correctly notes that CQD does not support the full SROIQ fragment. However, on the subset of queries that CQD can handle (EPFO: conjunctions, existential restrictions), a direct comparison is necessary to isolate the value of EBR's design. Without this, it is unclear whether EBR's performance comes from its neural semantics or simply from the underlying KGE (ComplEx, via KECI), which CQD also uses. The paper's claim of outperforming "symbolic reasoners" under incompleteness is the natural experiment, but the absence of a neural baseline weakens the overall contribution.

- **Threshold γ is a free parameter with no guidance or sensitivity analysis.** All EBR operations rely on a threshold γ > 0 to binarize continuous KGE scores into instance sets. The paper does not discuss how γ is chosen (per dataset? per query type?), whether it is tuned, or how sensitive the results are to its value. Given that the closed-world results are nearly perfect, it is plausible that γ was set exploitatively for the known score distribution. Without a principled selection procedure or robustness analysis, claims about performance under noise/incompleteness are difficult to interpret.

- **The closed-world assumption for negation is not discussed.** EBR(¬C) is defined as the complement over Δ^ℐ (all entities in the KB). This adopts a closed-world semantics, which is inconsistent with the open-world semantics of DLs where absence of information does not imply falsehood. The paper does not acknowledge or justify this design choice or discuss how it affects correctness on open-world KBs.

### Trivial
None.

## Nice-to-Haves

- **Computational cost analysis for complex constructors.** Universal restrictions (∀r.C) are handled via ¬(∃r.¬C), and cardinality restrictions require counting r-successors per entity. Both involve enumerating all entities and checking existential conditions against the KGE, which could be computationally expensive for large KBs. A runtime or complexity analysis would strengthen the scalability claims, which are currently motivated but unmeasured.

- **Handling of logical contradictions during KGE training.** The paper motivates EBR by the inability of symbolic reasoners to handle inconsistent KBs, but does not discuss how KGE training (which assumes all observed triples are true) deals with contradictory assertions. Even if the KGE smooths over inconsistencies via distributed representations, this merits explicit discussion or evaluation on KBs with genuine logical contradictions.

- **A principled method for setting γ.** The threshold could be validated on a held-out set of known entailments, or an adaptive approach (e.g., percentile-based) could replace the fixed scalar.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"The method does not perform DL reasoning in any meaningful sense"** — Removed as an overstatement. The paper explicitly frames EBR as an *approximation* of symbolic reasoning ("rapidly approximate the results of a symbolic reasoner"), not a sound and complete DL reasoner. The reviewer demands exact deductive reasoning, which is outside the stated scope. That said, the *substantive core* of this criticism (lack of evaluation against deductive closure) is preserved above as a major weakness.

- **"Experimental evidence for the paper's central claims is missing"** — Removed as a parser truncation artifact. The Conclusion references results on 80% incompleteness and comparisons with HermiT/Pellet/JFact/Openllet that are not visible in the extracted text. The instructions state that content stripped by the parser is assumed to exist in the original submission.

- **Criticisms about TBox axioms being treated "atomistically" and the KGE not learning subclass entailment** — Folded into the major weakness above. The reviewer's proposed fix (adding a regularization loss for subclass constraints) is a reasonable suggestion but does not constitute a fatal flaw on its own.

- **"Paper lacks runtime/scalability analysis"** — Moved to Nice-to-Haves. The paper's scalability claim is a stated contribution, but the absence of measurements is not a fatal omission; it is a natural extension.

- **"Six benchmark datasets listed without statistics"** — Removed. The paper names the six datasets. The reviewer's request for dataset statistics (size, number of concepts, roles, axioms) is helpful but not a core weakness; it is a presentation detail.

- **Various formatting, typos, and presentation nitpicks** — Removed as parser artifacts or style preferences that do not affect the paper's scientific content.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuinely important methodological concern — that the paper's evaluation does not test the one thing that distinguishes a "reasoner" from a "retrieval system": whether the KGE correctly assigns scores to logically entailed triples not present in the training data. This is not a flaw in the method itself, which is defensible as an approximation, but a gap in the experimental design that the authors would need to address.

## Suggestions

1. **Add an experiment evaluating against the deductive closure.** Use a symbolic reasoner to compute the full set of entailed instance assertions for each KB (assuming consistency), then compare EBR's retrieved instances against this closure rather than just the explicit ABox. This directly tests whether the KGE captures logical entailments.
2. **Include CQD (or a comparable neural QA method) as a baseline on EPFO sub-queries** (conjunctions, existential restrictions). Use the same underlying KGE to ensure a fair comparison.
3. **Provide guidance on threshold γ selection.** Report sensitivity to γ via a sweep, or propose a principled selection method (e.g., percentile-based thresholding, or validation on held-out entailments).
4. **Acknowledge and discuss the closed-world semantics used for negation complement**, clarifying when this approximation is appropriate and how it deviates from DL's open-world semantics.

## Score and Decision

This paper presents a clean and well-motivated mapping from SROIQ to neural semantics and is clearly positioned against prior work. However, the evaluation has a structural gap: it does not verify that the KGE captures logical entailments beyond the training triples, which is central to the claim of being a "reasoner" rather than a retrieval system. This is remediable through additional experiments against the deductive closure, but as presented the evidence falls short of fully supporting the paper's core claim. I judge the paper as having a solid technical contribution that is incompletely validated.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>