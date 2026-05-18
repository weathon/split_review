Now I have all the information I need. Let me synthesize the final review.

## Summary

The paper formalizes the novel problem of black-box RAG Dataset Inference (RAG-DI), introduces a purpose-built dataset (FRAD) with controlled fact redundancy to enable realistic evaluation, adapts existing RAG MIA methods as baselines, and proposes Ward — a method that embeds LLM watermarks into documents before publication to enable provable detection of unauthorized use in a RAG corpus. The central empirical finding is that Ward achieves 100% accuracy across all tested settings (including fact-redundant hard settings where all baselines fail), with statistical guarantees that the baselines cannot offer.

## Strengths

1. **Formalization of a novel and well-motivated problem**: The paper gives a clean formal definition of RAG-DI with clear entities, problem scope, and desiderata (monotonicity, guarantees, robustness), establishing a principled foundation for future work (Section 3).

2. **Creation of a dataset (FRAD) that enables meaningful evaluation**: FRAD uses fictional articles from RepliQA (no LLM training data contamination) and explicitly models fact redundancy by having multiple LLM authors write grounded articles sharing core facts. This exposes the core failure mode of baselines in the hard setting (Section 3.1, Figure 3).

3. **Ward provides statistical guarantees that baselines cannot**: By using red-green watermarks and joint p-value computation across queries, Ward produces a test with controlled Type I error under the null hypothesis. The theoretical scaling analysis (Equation 2, Figure 2) shows that even weak per-query watermark propagation becomes detectable with enough queries — a key advantage over all baselines (Section 4).

4. **Empirical demonstration of perfect accuracy under challenging conditions**: In the main experiment (Figure 3), Ward attains 100% accuracy across both easy and hard (fact-redundant) settings, across all tested LLMs (Haiku, GPT-3.5, Llama3.1-70b), both naive and defensive system prompts, and under MemFree decoding. All baselines fail in the hard setting, and the evidence is consistent across 5 random seeds.

5. **Validation of all three desiderata with concrete evidence**: Ward shows monotonic accuracy improvement with more queries (Figure 4 left), produces p-values orders of magnitude from the decision boundary in-case (Table 1, max in-case p-value < 8.44e-10), and remains accurate under strong defenses including both prompt-level and decoding-level (MemFree) protections.

6. **Practical utility preserved**: Watermarked documents maintain high quality (Table 2: similarity scores 0.898–0.933) and do not degrade RAG response quality (Section 5.3), supporting practical deployability.

## Weaknesses

### Fatal
None.

### Major
1. **Imperfect-retrieval evaluation tests only a narrow operating regime**: The end-to-end RAG experiment (Section 5.3) uses a single embedding model (OpenAI text-embedding-3-large) and achieves a 93.6% retrieval success rate — so it tests Ward under near-perfect conditions, not under substantially degraded retrieval. The paper acknowledges this limitation but does not address it experimentally. Lower-quality retrievers (e.g., BM25, different embedding models) or lower top-k values could yield meaningfully lower retrieval rates, and it is unclear how many additional queries Ward would need to compensate. A theoretical or empirical characterization of Ward's detection power as a function of retrieval probability would directly inform practitioners deploying the method with imperfect retrieval systems.

### Minor
1. **The "provable" claim could be more precisely scoped**: The paper's title and framing emphasize "provable" detection with "rigorous statistical guarantees." The guarantee is indeed valid for Type I error control under the null hypothesis (i.e., if the dataset is not in the corpus, the chance of a false accusation is ≤ α). However, the *power* of the test depends on empirical assumptions: the watermark must survive the RAG pipeline (retrieval + generation), must not leak from other sources, and must not be stripped by adversarial transformations beyond what is tested. The paper provides good empirical validation but acknowledges these limits only implicitly. Qualifying the title or abstract slightly — e.g., "statistically rigorous detection" — would more precisely match what is proven vs. what is demonstrated empirically.

2. **Limited coverage of baseline approaches**: The paper adapts SIB, IBM, and proposes FACTS. While these are reasonable starting points, a baseline based on token overlap, embedding similarity at the corpus level, or a classifier trained on query-response features could further strengthen the claim that baselines fundamentally fail under fact redundancy. The paper's claim that "all baselines fail" is only as strong as the set of baselines considered.

### Trivial
None beyond what is noted in Removed Points.

## Nice-to-Haves

- Test against a defense that paraphrases retrieved documents before response generation (e.g., an auxiliary LLM rewriter) — this would test watermark robustness under a stronger text transformation than MemFree's n-gram blocking.
- Report the effective token count after n-gram deduplication, not just raw query count, to give practitioners a clearer idea of the actual usable signal.
- Discuss the computational cost of paraphrasing a data owner's documents with a watermarked LLM (both in tokens and time).
- A dedicated limitations section would help practitioners understand where Ward does and does not apply (e.g., need to pre-watermark, dependence on watermark robustness to transformations).

## Removed Points

- **"The guarantee that the decision is correct requires additional assumptions"** (from harsh critic's item 2): This is already partially acknowledged; the paper's claim is about Type I error control of the statistical test, not absolute detection guarantees under all adversarial conditions. The concern is kept above as a Minor weakness about scope precision rather than removed entirely, since some overclaim in the title remains.
- **"The dataset is synthetic, limiting generalizability"**: The paper explicitly acknowledges this is an initial step and that synthetic construction avoids LLM training-data contamination. The synthetic nature is a feature, not an unforeseen limitation. Removed because this is inherent to the paper's design choice, not an oversight.
- **"The paper should add more comprehensive baselines"**: Kept as Minor above since it's a reasonable but secondary concern.
- **"The paper should study partial inclusion in more depth"**: The paper already studies this (Section 5.4 references to appendix). The request for more depth is a nice-to-have.
- **"No dedicated limitations section"**: Moved to Nice-to-Haves. The conclusion mentions limitations implicitly.
- **"Effective token count not reported"**: Moved to Nice-to-Haves.
- **"Computational cost of watermarking"**: Moved to Nice-to-Haves.

## Novel Insights

The key insight that emerges across the reviews is that RAG-DI is fundamentally different from existing MI/DI problems because RAG pipelines preserve watermark signal much better than fine-tuning (as noted in the related work discussion of Radioactivity). This makes proactive watermark-based approaches particularly well-suited to this setting in a way they are not for other data provenance tasks. The paper's demonstration that even weak per-document watermark signals can be aggregated into a strong dataset-level signal through joint p-values is the core technical contribution. A second subtle insight is that fact redundancy — a natural property of real RAG corpora — actually makes watermark-based methods more attractive relative to content-based approaches, since semantic overlap becomes a confound for similarity-based detectors but leaves the watermark signal unaffected.

## Suggestions

1. **Broaden the retrieval robustness experiment**: Test Ward with at least one or two additional retrievers (e.g., sentence-transformers/all-MiniLM-L6-v2, BM25) to show that performance does not collapse when retrieval accuracy drops below 90%. Alternatively, provide an analytical relationship between retrieval probability and the required number of queries for detection.

2. **Qualify the "provable" language slightly**: The current title "Provable RAG Dataset Inference via LLM Watermarks" could be read as claiming provable detection under all conditions. Consider "Provably-Sound" or "Statistically Rigorous" to match what is actually proven (Type I error control).

3. **Add a test against a paraphrasing-based defense**: A RAG provider that rewrites retrieved content with an auxiliary LLM before generation could be a stronger test of watermark robustness than the current defenses. Adding this (even as an ablation) would strengthen the robustness claims.

4. **Report deduplicated token counts in the qpd analysis**: The paper correctly notes that repeated n-grams reduce the effective number of scored tokens (Section 5.4). Reporting the mean/median effective token count per document after deduplication would make this analysis more actionable.

## Score and Decision

This is a solid, well-executed paper that formalizes a new problem, provides a purpose-built dataset, establishes baselines, and proposes a principled method that clearly outperforms them. The weaknesses are real but minor — the evaluation's narrow retrieval robustness test and the slight over-scope of the "provable" language — and do not undermine the core contribution. The paper should be accepted.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>