Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper formalizes the novel problem of black-box RAG Dataset Inference (RAG-DI), where a data owner aims to detect unauthorized inclusion of their dataset in a RAG system's corpus. The authors introduce FRAD (Fact-Redundant Article Dataset), a synthetic dataset built from fictional Repliqa articles that avoids LLM training-data overlap and models real-world fact redundancy. They adapt existing RAG membership inference attacks as baselines and propose Ward, a proactive method that embeds LLM watermarks into protected documents and detects them via a joint statistical test across RAG responses. Experiments show Ward achieving 100% accuracy across challenging settings with fact redundancy and defended prompts, where all baselines fail.

## Strengths

- **First formalization of the RAG-DI problem.** Section 3 clearly defines the entities (data owner, RAG provider), the dataset-level decision, black-box query access, and desiderata (monotonicity, guarantees, robustness), providing a principled foundation for a previously underexplored problem.

- **Novel dataset (FRAD) designed to address RAG-DI-specific challenges.** FRAD uses fictional Repliqa articles (ensuring no LLM training-data overlap) with controlled fact redundancy across groups of four independently authored articles. The paper empirically validates (Figure 2) that the easy setting (no redundancy) is trivially solvable by a simple baseline, while the hard setting (with redundancy) causes all baselines to fail — confirming that fact redundancy is essential for realistic RAG-DI evaluation.

- **Ward provides rigorous statistical guarantees.** Unlike all baselines, Ward inherits the watermark detector's p-value, enabling a well-controlled hypothesis test for dataset inclusion. Table 1 shows in-case p-values orders of magnitude below the decision threshold and out-case p-values well-calibrated near 1, directly satisfying the guarantee desideratum.

- **Ward achieves 100% accuracy across all challenging settings.** In the main experiments (Figure 2), Ward obtains perfect accuracy on both easy and hard settings, across three LLMs, under both naive and defended system prompts. All baselines fail in the hard setting, especially under the defended prompt where they produce both false positives and false negatives.

- **Ward exhibits monotonic improvement with query count.** Figure 3 shows Ward's accuracy increasing smoothly with |D_owner|, reaching 100% with at most 80 documents, while baselines like SIB show high variance and non-monotonic behavior. This satisfies the monotonicity desideratum.

- **Comprehensive evaluation and ablations.** The paper adapts existing RAG MIAs to the dataset-level setting, introduces a Facts baseline, ablates watermark parameters (δ, h), retrieval settings (k), and even tests against MemFree decoding defense (details in appendix). Quality evaluation confirms watermarked documents maintain high text quality and do not degrade RAG response quality (Table 2, Section 5.3).

## Weaknesses

### Fatal

None.

### Major

- **The end-to-end retrieval experiment is underanalyzed, leaving a quantitative gap unexplained.** Section 5.3 reports that a realistic embedding-based retriever succeeded in retrieving the targeted watermarked article in only 93.6% of requests, yet Ward still achieves "100% accuracy across all settings." The paper does not explain how the 6.4% retrieval failures are absorbed — presumably the joint p-value across n=200 queries remains significant even with ~12-13 missing signals, but this is never explicitly quantified or analyzed. The accuracy curves are deferred to the appendix, and the main text provides only a one-sentence claim. Given that the main experiments assume perfect retrieval, the end-to-end validation needs a more detailed breakdown (e.g., does accuracy degrade when retrieval success drops below some threshold? How much safety margin does the joint test provide?). As presented, the reader cannot assess how robust Ward is to realistically imperfect retrieval.

### Minor

- **Limited threat model discussion.** The paper evaluates two system prompts (naive and defended) and one decoding-level defense (MemFree), but does not systematically define the RAG provider's knowledge, capabilities, or potential countermeasures. A proper threat model would list what the provider knows (e.g., that Ward is in use, the watermark scheme, the detection algorithm) and enumerate considered countermeasures (e.g., paraphrasing retrieved text, adding noise, perturbing token distributions). The current evaluation feels ad hoc rather than systematic.

- **FRAD's synthetic construction limits external validity, and this limitation is understated.** FRAD articles are LLM-generated from a fixed set of key/additional facts, with watermarked versions being paraphrases of that LLM-generated text — a best-case scenario for watermark preservation. Real-world documents have varied writing styles, lengths, and quality, and natural fact redundancy is messier (different sources selecting different facts, temporal variation, chunking artifacts). The paper acknowledges FRAD's design choices but does not discuss what would be needed to extend evaluation to more naturalistic settings or what kinds of real-world documents might break the watermark propagation assumption.

- **No discussion of computational or API cost.** The paper reports query counts but not token counts, API costs, or the overhead of watermarking the dataset. For practitioners considering whether Ward is practically deployable, this information matters (e.g., watermarking 200 documents, plus 200 queries to the RAG system, plus watermark detection on responses — what is the total cost in dollars and time?).

- **Ablation on very small dataset sizes is missing.** The paper varies |D_owner| from 20 to 200 but does not probe the lower bound (e.g., |D_owner| = 5 or 10). Since the joint p-value requires accumulating enough green tokens to reach significance, understanding the minimum dataset size for reliable detection would help practitioners assess Ward's applicability to their setting.

### Trivial

None.

## Nice-to-Haves

- **Compare against other proactive methods.** The paper compares Ward against passive baselines adapted from RAG MIA. The contribution would be strengthened by also comparing against other proactive approaches (e.g., inserting canary strings, invisible perturbations, rare-sequence insertion) to show that watermarking specifically is the right proactive tool for RAG-DI.

- **Characterize the lower bound on |D_owner|.** A brief experiment with |D_owner| = 5, 10, 15 would help practitioners understand the minimum dataset size needed for reliable detection.

- **Sensitivity analysis of baseline thresholding.** The paper uses the midpoint of s_in and s_out as a threshold for baselines. A brief note on whether results are sensitive to this choice, or a comparison with ROC-based thresholding, would be helpful.

## Removed Points

These points were identified from the reviewer inputs but are flagged as removed per the review guidelines. Treat them with caution if referenced.

1. **"Proactive watermarking assumption limits practical applicability / paper misaligns problem framing."** — The paper explicitly states in Section 3 that the data owner "may proactively modify D_owner before publishing it." The problem definition includes proactive modification; the paper does not claim to solve passive detection of already-published content. The reviewer's characterization is a misreading.

2. **"Unfair comparison with baselines due to proactive/passive asymmetry."** — The asymmetry favors the author's method (proactive watermarking), which is the paper's core innovation. Showing that existing passive methods fail while a proactive approach succeeds is the point of the paper, not a flaw. The comparison is informative, not unfair.

3. **"Query generation not fully specified."** — The paper states that all prompts (including query generation) are in the appendix (line 252). The appendix is stripped by the parser; it exists in the original submission. Per guidelines, this criticism is invalid.

4. **"MemFree defense experiment relegated to appendix with only one-sentence summary."** — Full results are in the appendix (app:more_results:memfree), stripped by the parser. The main text appropriately summarizes the key finding. Per guidelines, this is an artifact of parsing.

5. **"Baseline thresholding method is arbitrary (mean of s_in and s_out)."** — The paper uses a training-validation split with grid search over parameters, which is a standard and defensible approach for adapting document-level methods to dataset-level decisions.

6. **"Table 1 (p-values) is hard to read."** — This is a formatting/style nitpick, not a substantive weakness. Per guidelines, pure formatting/style nitpicks are removed.

7. **"Guarantees section conflates statistical significance with practical guarantees."** — The paper correctly states that the guarantee is Type 1 error control at threshold α, which is standard. The reviewer's point is pedantic and does not identify a genuine flaw.

8. **"Ablation on very small dataset sizes (5 or 10) is missing."** — Keep as minor weakness (included above), but the reviewer's framing as a major gap is disproportionate for what is a reasonable scope limitation.

## Novel Insights

The most interesting insight from the review process is the tension between the paper's proactive framing and the broader RAG-DI problem definition. The paper formalizes RAG-DI as including proactive modification in the problem definition itself, but the high-level narrative (abstract, introduction) sometimes suggests a more general detection problem. This creates a subtle framing gap: the paper's contribution is a proactive solution to a problem that, in its most general form, also includes a passive subproblem that Ward does not address. Clarifying this boundary would strengthen the paper without changing any results. Additionally, the 93.6% retrieval → 100% accuracy result is more interesting than the paper acknowledges — it implies the joint p-value test has considerable slack, which is worth quantifying and discussing as a robustness property.

## Suggestions

1. **Expand the end-to-end analysis.** Provide a breakdown of how the 6.4% retrieval failures affect the joint p-value distribution, and quantify the safety margin. Ideally, sweep over retrieval accuracy (e.g., by varying the number of retrieved documents k or using a weaker retriever) to show where Ward begins to degrade.

2. **Add a threat model subsection.** Clearly state what the RAG provider knows, what countermeasures are considered realistic, and systematically evaluate robustness (e.g., response paraphrasing, token-level noise, instruction-tuned "don't repeat" prompts beyond the two tested).

3. **Report computational and API costs.** Provide token counts for watermarking the dataset, querying the RAG system, and running detection. This is essential for practitioners assessing deployability.

4. **Soften the language around "realistic conditions."** FRAD is a purpose-built synthetic dataset that captures one specific dimension of realism (fact redundancy) while sacrificing others (natural text variation, organic redundancy patterns). Acknowledge this trade-off more explicitly and discuss what naturalistic evaluation would require.

## Score and Decision

The paper makes a clear contribution: formalizing a novel problem, providing a purpose-built benchmark, and introducing an effective method with statistical guarantees. The weaknesses are real but addressable and do not undermine the core contribution. The paper is ready for acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>