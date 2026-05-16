Now I have a thorough understanding of the paper. Let me compile my final review.

## Summary
This paper formalizes the problem of black-box RAG Dataset Inference (RAG-DI), where a data owner aims to detect unauthorized inclusion of their dataset in a RAG system's corpus. It introduces the FRAD dataset (synthetic, fact-redundant articles built from RepliQA to avoid LLM training data contamination), adapts RAG MIA baselines (SIB, IBM), and proposes Ward—a proactive method that embeds LLM watermarks into a data owner's documents and detects them in RAG responses via a joint p-value test. The main result is that Ward achieves 100% accuracy across three LLMs, two system prompts, and both easy and hard (fact-redundant) settings, while all baselines fail in the hard setting.

## Strengths
- **Formalization of a novel problem (RAG-DI) with clear scope and realistic challenges.** The paper explicitly defines RAG-DI as a distinct black-box problem (Section 3) and demonstrates that existing datasets (EnronEmails, HealthcareMagic) are unsuitable because they lack fact redundancy and may have been seen in LLM training data (Section 3.1). This framing justifies the need for the new dataset and method.
- **FRAD dataset with controlled fact redundancy, designed to isolate the key difficulty.** The dataset uses RepliQA fictional articles provably absent from LLM training data, with groups of 4 articles sharing 5 key facts (Section 3.1, Figure 2). This enables, for the first time, evaluation under realistic fact redundancy, which is empirically shown to be the decisive factor separating successful methods from failing baselines (Section 5.1, Figure 5).
- **Ward provides rigorous statistical guarantees that no baseline matches.** By using a joint p-value test on collected responses (Section 4, Equations 2–3), Ward bounds Type I error at a user-specified level. Table 1 (Table 1 in the paper) shows that even the maximum p-values for the in-case are orders of magnitude below the decision threshold (~3×10⁻⁵), and the minimum p-values for the out-case are far above it, directly validating the guarantee.
- **Ward achieves 100% accuracy across all challenging settings while baselines fail.** In the main experiment (Section 5.1, Figure 5), Ward obtains perfect classification on both easy and hard (fact-redundant) settings, for three different LLMs (Haiku, GPT-3.5, Llama3.1-70b), under both naive and defended system prompts. All baselines (FACTS, IBM, SIB) fail in the hard setting.
- **Monotonic improvement with query count.** Ward's accuracy consistently rises with |D_owner|, reaching perfect accuracy at 80 documents, while baselines show highly variable accuracy that sometimes decreases with more queries (Section 5.2, Figure 6).
- **Robustness to strong defenses.** Ward maintains 100% accuracy under a defended system prompt designed to prevent information leakage, and even under MemFree decoding that strictly prevents n-gram overlap with retrieved documents (Section 5.2). Baselines' accuracy collapses under these defenses because they rely on the model's willingness to leak information.
- **Practical validation with imperfect retrieval.** When using a real embedding-based retrieval system (text-embedding-3-large, k=3), Ward still achieves 100% accuracy with 93.6% retrieval success, and p-values scale correctly with query count (Section 5.3, Figure 9), demonstrating that the perfect-retrieval assumption is not a limiting factor.
- **Watermarked text maintains high quality.** Quality evaluations using GPT-4 ratings and P-SP metric show that watermarked paraphrases have nearly identical scores to originals (Table 3), and response quality is indistinguishable between in-case and out-case, confirming that watermarking does not degrade RAG utility.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims (problem formalization, dataset, method with statistical guarantees, empirical superiority) are all well-supported. The weaknesses below are minor issues or scope for future improvement.

### Minor
- **The "provable" framing is slightly inflated relative to what the method delivers.** The paper titles itself "Provable RAG Dataset Inference" and states that Ward can "provably ... detect unauthorized data usage" (line 53). What the method provides is a statistically well-calibrated test (a valid p-value under the null hypothesis), not a logical guarantee. While this terminology is standard in the LLM watermarking literature (KGW et al. also use "provably"), the paper would be more precise by consistently describing Ward as providing *rigorous statistical tests* rather than "provable" inference. This does not undermine the contribution but the framing sets expectations slightly above what is delivered.

- **The perfect-retrieval assumption in the main experiments is only partially validated.** The paper acknowledges the assumption (line 247) and validates it with one end-to-end experiment using OpenAI text-embedding-3-large at k=3 (Section 5.3.1), showing 100% accuracy and 93.6% retrieval success. However, this validation covers only a single embedding model, one k value, and reports only average p-values without showing variance across queries or the effect on p-values in the ~6.4% of cases where retrieval fails. Given that the perfect-retrieval experiments are presented as primary evidence, a more thorough characterization of retrieval-dependent failure modes would strengthen the paper's claims about real-world applicability. This is a gap the authors partially address but do not fully close.

- **The FRAD dataset is entirely LLM-generated, leaving open questions about ecological validity.** The paper is transparent about FRAD's construction (Section 3.1): fictional articles from RepliQA are distilled into facts, and LLMs generate articles incorporating those facts. While this cleverly avoids training data contamination, the documents are generated by instruction-following models that may produce artifacts (e.g., formulaic structure, consistent register) not present in real user-authored content. The paper acknowledges expandability but does not discuss how the synthetic nature might affect either baseline methods (which rely on factual overlap) or watermark propagation (which might behave differently on more varied real text). The dataset is a useful starting point, but generalization to organic web content remains unvalidated. The paper should be more explicit that FRAD is a *synthetic proxy* and that this is a limitation.

- **Limited discussion of when and why Ward could fail.** The paper demonstrates Ward works under defended prompts and MemFree decoding, but does not systematically characterize the boundary conditions where the watermark signal would degrade to the point of failure. For instance: (a) when retrieved documents are truncated before being fed to the LLM, (b) when the RAG system uses highly abstractive readers that thoroughly paraphrase, or (c) when the data owner's documents are poorly suited to paraphrasing with a watermarked LLM (e.g., code, structured data). A characterization of the relationship between response-document n-gram overlap and resulting p-value would make the method's scope of applicability concrete.

### Trivial
None.

## Nice-to-Haves
- A quantitative analysis of how imperfect retrieval (varying the success rate below 93.6%) affects the number of queries required to reach a given confidence level, similar to the monotonicity experiment but with retrieval noise.
- A brief discussion of potential adversarial countermeasures beyond those tested (e.g., the RAG provider applying a generic paraphrasing filter on all responses, or detecting systematic probing patterns), and how Ward might be extended to handle them.
- A note on the computational/monetary cost of watermarking a large dataset for the data owner, and whether the method applies when only a subset of documents can be watermarked.
- Mention of the unlikely but theoretically interesting edge case where both the data owner and the RAG generator use the same watermarked LLM with the same key, which would confound detection.

## Removed Points
These points are flagged to be removed; treat them with caution.
- The reviewer's point about SIB gray-box adaptation not being compared to the original: The paper transparently states the adaptation (line 156) and uses it in the intended black-box setting. The original gray-box results would require a different access model that is inconsistent with the problem definition. This is a scope-appropriate adaptation, not a weakness.
- The reviewer's point about "the paper could also mention that [EnronEmails and HealthcareMagic] contain personal text... A brief discussion would strengthen the motivation": This is a minor suggestion, not a weakness. The paper already provides sufficient motivation by highlighting the lack of fact redundancy and potential training data overlap.
- The reviewer's point about "no discussion of the 'RAG provider's countermeasures' beyond prompt-level defenses": The paper already evaluates defended prompts AND MemFree decoding, which are the two most direct countermeasures. Additional speculative countermeasures are outside the paper's scope and typical for a first work on a new problem.

## Novel Insights
The most interesting insight from the review process is that the paper's core contribution — using LLM watermarks as a proactive detector for RAG corpus inclusion — is validated by the clean separation between the watermark propagation mechanism and the fact-redundancy challenge that breaks all passive baselines. The passive baselines (FACTS, SIB, IBM) fail because fact redundancy causes false positives: when multiple documents share facts, a response can be correct without relying on the specific target document. Ward sidesteps this entirely because the watermark is a content-independent signal that survives regardless of which redundant article the RAG system draws from. This reveals a deeper structural advantage: proactive watermarking is not just another baseline but a fundamentally different approach that is *invariant* to the exact property (fact redundancy) that makes the problem hard for passive methods. The paper's experimental design (Easy vs. Hard settings) cleanly exposes this invariance.

## Suggestions
- Rephrase "provable" claims throughout to emphasize "rigorous statistical guarantees" or "well-calibrated statistical tests" to avoid overclaiming relative to what a z-test provides.
- Add a richer end-to-end retrieval evaluation with multiple embedding models and k values, and report not just averages but the distribution of p-values (e.g., min, max, percentiles) across the ~6.4% of retrieval failures to quantify the worst-case degradation.
- Explicitly state "synthetic proxy" when describing FRAD's limitations regarding real-world generalization.
- Add a dedicated paragraph characterizing the boundary conditions: measure the correlation between the RAG response's n-gram overlap with the watermarked document and the resulting per-query p-value, to give practitioners a concrete sense of when Ward will and won't work.

## Score and Decision

The paper formalizes a novel problem, provides a carefully designed dataset that isolates the key difficulty (fact redundancy), establishes baselines, and proposes a principled method (Ward) that delivers strong empirical results with statistical guarantees. The weaknesses are minor — the "provable" framing is a matter of precision, the perfect-retrieval validation is limited but not absent, and the synthetic dataset is a justified design choice. The core contribution is sound and significant.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>