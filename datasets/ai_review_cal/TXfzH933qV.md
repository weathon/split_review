- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me construct the final review.

## Summary

This paper proposes **PretexEval**, a framework for dynamically generating test samples from medical knowledge bases to evaluate LLMs' mastery of medical factual knowledge. The core idea is to represent knowledge triplets as predicates, apply logical transformations (inversion, instantiation, double negation), and convert the resulting variants back into textual statements. Evaluated on 12 LLMs across two knowledge bases (MedLAMA, DiseK), the framework shows that LLMs perform substantially worse and less consistently on these generated samples than on simpler baselines, revealing knowledge gaps not captured by static benchmarks.

## Strengths

- **Novel approach with sound logical foundation.** The predicate-transformation schema (Equation 4) provides a principled way to generate structurally diverse test samples from a given knowledge triplet while maintaining a formal connection to the original fact. The paper explicitly acknowledges in a footnote that "instantiation" is an implication rather than a strict equivalence, showing appropriate caution.

- **Consistent and extensive empirical evidence.** Table 1 shows that all 12 evaluated LLMs achieve lower accuracy under PretexEval than under both template-based (Direct) and LLM-based (LLMEval) baselines across both MedLAMA and DiseK. For example, GPT-4o drops from +35.8 (Direct) to +31.7 (PretexEval) on MedLAMA, and smaller models like Llama2-7B drop by over 50%. This pattern is remarkably consistent, ruling out model-specific artifacts.

- **Joint accuracy metric is a clinically relevant contribution.** The metric (Section 4.2, Equation 8) captures consistency across diverse expressions of the same knowledge point — a dimension absent from average-accuracy-only evaluations. Figure 2 shows joint accuracy dropping sharply as more expressions are added, quantifying inconsistency that prior benchmarks would miss.

- **Ablation cleanly isolates the source of difficulty.** Table 3 shows that removing predicate transformations raises accuracy by ~5–9 percentage points, while removing LLM rephrasing produces a smaller increase. This confirms that structural diversity (predicate transformations), not lexical variation (rephrasing), is the primary driver of the framework's stricter evaluation.

- **Human evaluation supports the reliability claim.** Two experienced doctors rated PretexEval-generated samples highly on reliability (~5/5) and structural diversity (~4.5/5) after rephrasing, while LLMEval samples scored lower on both dimensions (Figure 5). This provides direct evidence that the generated samples are factually correct relative to the original triplets.

## Weaknesses

### Fatal
None.

### Major

- **Transformation validity is assumed rather than verified per relation.** The paper does not list the 19 relations in MedLAMA or the 4 in DiseK, nor does it analyze whether each transformation type (inversion, instantiation, double negation) is semantically valid for every relation. For example, inversion from "treats" to "prescribed_drug_includes" is reasonable, but whether all 19 MedLAMA relations have natural, truth-preserving inverses is unexamined. The paper notes that "two relations in MedLAMA… are the inversion of the other two relations" and were excluded (line 125), showing some awareness, but this analysis is not extended to all relation-transformation pairs. If even a subset of generated statements are not entailed by the original triplets, the evaluation labels would be wrong and the headline finding ("LLMs exhibit significant deficiencies") would be at least partially undermined. The human evaluation (50 triplets) provides some reassurance but is too small to cover all relation types.

### Minor

- **Human evaluation is limited in scale and reporting.** The evaluation uses only 50 triplets from one knowledge base (MedLAMA). The paper does not report inter-annotator agreement (Cohen's κ), the exact scoring rubric for "reliability," or whether doctors were blinded to the method that generated each sample. Without these details, the reliability scores from Figure 5 are informative but not fully rigorous.

- **LLM rephrasing as a potential confound is not fully diagnosed.** The ablation results (Table 3) show that removing LLM rephrasing *improves* performance on most model/dataset combinations (e.g., Llama3-70B on MedLAMA: +26.9 with rephrasing → +30.4 without). The paper attributes this to increased diversity, but it could equally indicate that rephrasing introduces awkward or misleading phrasings that cause LLMs to answer incorrectly for reasons unrelated to medical knowledge. A finer-grained analysis (e.g., does accuracy vary with syntactic complexity of the rephrased statement?) would strengthen the claim that the evaluation measures knowledge mastery rather than language comprehension artifacts.

- **Negative triplet construction is underspecified.** The paper states (line 125) that negative entities are "randomly sampled" such that ¬R(h,c) holds, but does not describe how c is verified against the KB. If the KB is incomplete, some c sampled as "negative" could actually be positive entities absent from the KB. This introduces potential label noise. The practical impact is likely small given the consistent results across models, but the mechanism should be clarified.

### Trivial
- No confidence intervals or error bars are reported for the main results (Table 1), despite the subsampling procedure introducing variance.
- The paper could benefit from breaking down accuracy by transformation type (inversion vs. instantiation vs. double negation) to show whether certain transformations drive the performance drops more than others.

## Nice-to-Haves
- Expanding the human evaluation to ~200 triplets across both knowledge bases with a clear scoring rubric and inter-annotator agreement reporting would strengthen the reliability claim substantially.
- A per-relation table showing which transformations are applied to which relations, with a brief justification, would preempt concerns about transformation validity.

## Removed Points

- **"Unvalidated reliability of predicate transformations (structural flaw)"** → Moved from Fatal to Major. The paper's footnote (line 31) explicitly acknowledges that instantiation is an *implication* rather than a strict equivalence, showing appropriate caution. The human evaluation (Figure 5) provides direct empirical validation of reliability. The critic's characterization of this as a "structural flaw that invalidates the core claim" is not supported by the paper as written — the paper's logical framework plus empirical validation provides reasonable, if not exhaustive, evidence.

- **"No discussion of transformation validity across relation types"** → Merged into the first Major weakness above. The critic's call for a full relation-by-relation table is a reasonable suggestion but the absence of it is a Major gap, not Fatal.

- **"Speculative concerns about negative triplet completeness causing systematic label noise"** → The critic's concern about KB incompleteness is speculative (the paper does not report that the KB is incomplete). The practical impact of random negative sampling from curated medical KGs (derived from UMLS) is minimal. Retained as Minor with softened language.

- **"Sample size too small to support conclusions"** → The 50-triplet evaluation is limited but the paper uses it only as supporting evidence, not as the primary basis for its conclusions. The main findings rest on the large-scale automated evaluation across 12 LLMs. Retained as Minor with appropriate framing.

- **Strength Finder item about "joint accuracy metric captures consistency"** → This is a valid strength and correctly identifies a contribution not present in prior work. Retained.

- **Strength Finder claim "Figure 3, right panel shows..."** → The paper's figure is actually Figure 5 (line 211-216). The reference is slightly off but the content is correct. This is a harmless mislabel.

## Novel Insights

The most interesting pattern across the two reviews is that the paper's main experimental finding (LLMs perform worse under PretexEval) admits two competing interpretations: either the framework genuinely reveals knowledge mastery gaps, or it introduces artifacts (invalid statements, confusing phrasing) that LLMs correctly reject. The paper's own ablation and human evaluation provide evidence for the former, but the reviews sharpen the question of exactly *what kind* of knowledge gap is being measured — is it factual knowledge per se, or the ability to recognize the same fact across diverse syntactic/semantic frames? The joint accuracy metric (Figure 2) begins to answer this, but the paper could go further by analyzing which transformation types cause the most inconsistency and whether errors cluster by linguistic form (e.g., negation) or by knowledge domain. A second insight from the reviews is that the rephrasing confound (rephrasing lowers accuracy) is under-explored: if the LLM's own rephrasing makes statements harder, the evaluation may partially measure robustness to linguistic variation rather than pure medical knowledge.

## Suggestions

1. **Add a per-relation analysis or justification.** For each of the 19 MedLAMA and 4 DiseK relations, state which transformations are applied and why they preserve truth. Even a supplementary table with a brief rationale would substantially address the core validity concern.

2. **Expand and formalize the human evaluation.** Use at least 100–200 triplets, report inter-annotator agreement (Cohen's κ), clarify the scoring rubric, and include samples from both knowledge bases.

3. **Diagnose the LLM rephrasing effect.** Perform an analysis of whether accuracy on rephrased statements correlates with measurable linguistic properties (sentence length, syntactic complexity, etc.) or with the specific LLM used for rephrasing. This would distinguish "rephrasing introduces harder but valid statements" from "rephrasing introduces noise."

4. **Report results by transformation type.** Break down accuracy for inversion, instantiation, and double negation separately. This would reveal whether certain transformations are driving the observed effects and would help interpret what kind of knowledge "gaps" the framework detects.

5. **Clarify the negative entity sampling procedure.** Describe how ¬R(h,c) is verified and whether any validation against the KB's completeness is performed.
