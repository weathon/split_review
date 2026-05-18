Now I have a thorough understanding of the paper and can cross-check each claim. Let me finalize my analysis and generate the review.

---

## Summary

This paper introduces ChuLo, a chunk-level representation method for long document understanding. The core idea is to divide long documents into fixed-length chunks, use an unsupervised keyphrase extraction algorithm (SKP, adapted from PromptRank) to identify semantically important phrases, and then compute each chunk's embedding as a weighted average that emphasizes keyphrase tokens over non-keyphrase tokens. These chunk embeddings are then processed by a Transformer-based chunk attention module for document classification or token classification. The method is evaluated on four document classification datasets (HP, LUN, EURLEX57K, Inverted EURLEX57K) and two token classification datasets (CoNLL-2012, GUM), claiming strong results including a 6.43% accuracy improvement on LUN over BERT and very high F1 on CoNLL NER.

## Strengths

1. **Novel integration of unsupervised keyphrase extraction with chunk-based document representation.** The SKP algorithm (Algorithm 1) adapts PromptRank to operate over the full document and uses the resulting keyphrase scores to re-weight token embeddings during chunk aggregation (Formula 1). This is a principled departure from prior chunking methods that treat all tokens equally (random chunking) or rely on sentence-level selection (CogLTX, BERT+TextRank). The approach gives the model a mechanism to retain semantically important content while reducing input length.

2. **Consistent improvements on document classification across multiple datasets.** ChuLo achieves the best or second-best results on all four document classification benchmarks: +6.43% accuracy over BERT on LUN (0.6440 vs. 0.5797), best micro-F1 on EURLEX57K (0.7332) and Inverted EURLEX57K (0.7244), and near-best on HP (0.9538 vs. Longformer's 0.9569, a difference of one instance). These gains are meaningful and suggest the keyphrase-weighted chunk representation helps capture document-level semantics.

3. **Robust performance on very long documents, including comparison with LLMs.** On documents exceeding 2,048 tokens in the LUN dataset, ChuLo achieves 0.7959 accuracy, surpassing both GPT-4o (0.7143) and Gemini 1.5 Pro (0.6531) (Table 3). On CoNLL documents exceeding 8,192 tokens, ChuLo maintains 0.9206 micro-F1 while Longformer drops to 0.3116 (Table 6). This demonstrates the method's strength in handling very long inputs where baselines degrade sharply.

4. **Transparent ablation studies that isolate design choices.** The ablation experiments (Tables 5/8-10) compare PromptRank-based keyphrase extraction against YAKE and simple averaging, test the effect of adding sentence embeddings, and evaluate different backbone models (BERT vs. RoBERTa vs. Longformer for the chunk attention module). These provide useful guidance for practitioners and help separate the contribution of each component.

## Weaknesses

### Fatal
None.

### Major

1. **Token classification methodology is critically underspecified.** The paper states (line 259) that for token-level NER, "we integrate a BERT-decoder module that utilizes the enhanced chunk embeddings to predict token labels," but provides no description of how a single chunk embedding (produced by weighted averaging of *n* tokens) is expanded back to *n* token-level predictions. No alignment mechanism, projection layer, or decoding architecture is given. The framework figure (Figure 1) is referenced but its content is not described in text. Without this architectural detail, the token classification results (0.9334 micro-F1 on CoNLL vs. Longformer's 0.5560) cannot be interpreted, reproduced, or trusted. The magnitude of the gap is so large that it raises further questions about whether the evaluation setup (e.g., label granularity, document selection criteria) is comparable across methods. **This is the most serious weakness in the paper** — it directly affects a core claimed contribution ("Enhanced Document **and Token** Classification"), and the claimed results rest on an unexplained procedure.

2. **Essential hyperparameters are not reported, preventing reproducibility.** The chunk size *n* (number of tokens per chunk) is described as a key hyperparameter (line 54) but its value is never given. The keyphrase/non-keyphrase weight parameters *a* and *b* (Formula 1) and the SKP algorithm parameters α and γ (Algorithm 1) are also unreported. The "512*Chunk Size" notation in Table 2 (line 185) is ambiguous — it could mean 512 chunks of chunk_size tokens each, or 512 × chunk_size total tokens. Without these values, the experiments cannot be reproduced or properly interpreted. The top-*n* value for keyphrases is partially reported ("15 was generally better" in a footnote, line 137), but this is insufficient without the other parameters.

### Minor

3. **The LUN baseline comparison relies on the authors' own implementations.** The paper transparently discloses (Table 1 caption, line 166) that "Results for LUN are obtained by our own experiment based on provided baseline codes and methods, while baseline results for the other datasets are from previous work." This means the largest claimed improvement (6.43% over BERT on LUN) rests on baselines re-implemented by the authors, without verification that the hyperparameters, data splits, and training setups match those used in the original published results. While this is a common practice, it weakens the strength of the primary numerical highlight, especially since LUN is the dataset where the improvement is largest and most central to the paper's claims.

4. **"Preserving all tokens" is a misleading phrase for a method that compresses tokens into weighted average embeddings.** The paper repeatedly emphasizes (lines 4, 17) that "preserving all tokens" is critical, especially for token classification. However, the method explicitly compresses each *n*-token chunk into a single weighted average vector (Formula 1), which is a lossy operation — individual token identities and fine-grained positional information within a chunk are discarded. What the method actually preserves is access to all chunks (i.e., no truncation), not all tokens as distinct representational units. The wording creates an expectation the method does not fulfill, particularly for the token classification setting where this tension is most acute.

5. **Small test set sizes limit the reliability of several conclusions.** The HP test set has only 65 samples, and the CoNLL and GUM test sets for token classification have 20 and 26 documents respectively (the paper explicitly selects only the longest documents). The claimed difference on HP between ChuLo (0.9538) and Longformer (0.9569) is one instance, which the paper acknowledges. Yet the paper still uses HP to support ablation conclusions (keyphrase method comparison, backbone comparison) and length-based analysis, where statistical conclusions from 65 samples are unreliable. Similarly, the CoNLL results (20 documents, many with extreme lengths) are high-variance.

6. **The keyphrase weighting benefit is demonstrated on only one of two ablation datasets.** In the ablation study (Table 5a), PromptRank-based weighting (0.6440) clearly outperforms simple averaging (0.5951) on LUN, but on HP, all three methods (Average, YAKE, PromptRank) achieve identical accuracy (0.9538). The paper attributes this to HP's small test set, but it nonetheless means the key weighting mechanism's general utility is established on a single dataset with a re-implemented baseline.

7. **The claimed adaptability to "any transformer-based architecture" is not demonstrated.** The paper states (line 120) that ChuLo "is adaptable to any transformer-based architecture," but the backbone ablation (Table 5c) shows that RoBERTa (0.8615 HP, 0.5906 LUN) and Longformer (0.8923 HP, 0.5600 LUN) both underperform BERT (0.9538 HP, 0.6440 LUN) as the chunk attention backbone. This suggests the method may not transfer easily, and the claim of architecture-agnostic adaptability is unsupported.

### Trivial

None.

## Nice-to-Haves

- A version of the SKP algorithm without the position penalty, to analyze the effect of the strong inductive bias that penalizes later-occurring keyphrases.
- Comparison against the simple averaging baseline on EURLEX57K and Inverted EURLEX57K (currently only shown for HP and LUN).
- Statistical significance tests (e.g., bootstrap confidence intervals) for the small test set results.
- The LLM prompting strategy should be described so that the zero-shot NER results (GPT-4o: 0.2290, Gemini: 0.3036 on CoNLL) can be interpreted as lower or upper bounds on LLM capability rather than artifacts of prompt design.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic, "Other Observations" — "these numbers likely reflect a poor prompt rather than inherent model limitations":** This is speculation unsupported by evidence. The paper does not describe the prompt, but there is no basis to assert it was poor. The underlying concern (prompting strategy not described) is moved to Nice-to-Haves.
- **Harsh Critic, "The paper should drop the token classification experiments entirely":** This is an editorial suggestion, not a weakness. The concern about methodological under-specification is kept (Major #1), but the demand to remove experiments goes beyond evaluation.
- **Strength Finder's claim that "Addresses an underexplored area—token classification in long documents":** This is not particularly accurate — there is substantial prior work on NER in long documents (e.g., Longformer, BigBird, hierarchical models). This strength is dropped as it conflicts with established prior work.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the token classification architecture.** Specify how chunk embeddings (one per *n*-token chunk) are projected to token-level predictions. Provide the decoder structure, alignment mechanism, and any loss function changes. If the approach is to concatenate original token embeddings with chunk-level context vectors, describe this clearly.
2. **Report all unreported hyperparameters** — chunk size *n*, keyphrase weight values *a* and *b*, SKP coefficients α and γ. Add sensitivity analysis for at least chunk size and the *a:b* weight ratio.
3. **Verify LUN baseline implementations** against published numbers where possible, or release the implementation code for community inspection.
4. **Disambiguate the "512*Chunk Size" notation** and report the actual number of chunk embeddings used (total input length in tokens after chunking) alongside baseline token budgets.
5. **Reconsider the "preserving all tokens" framing** to accurately describe what the method does: it preserves access to all chunks (no truncation) while compressing intra-chunk token information into weighted averages.
6. **Acknowledge test set size limitations more explicitly** in the conclusions drawn from HP and CoNLL, and consider reporting confidence intervals or bootstrap estimates.

## Score and Decision

The paper introduces a genuinely interesting idea — using unsupervised keyphrase extraction to weight chunk-level representations for long document understanding. The document classification results are encouraging and suggest the method has real merit. However, the paper has two serious weaknesses that prevent acceptance in its current form: (1) the token classification methodology is critically underspecified, making the claimed NER results uninterpretable and unsupported, and (2) essential hyperparameters (chunk size, *a*/*b*, α, γ) are missing, preventing reproducibility. Additionally, the largest claimed improvement (LUN) rests on author-implemented baselines. The core idea is salvageable and could form the basis of a strong paper after major revision — specifically, clarifying the token-level architecture, reporting all hyperparameters, and either strengthening the LUN baseline verification or tempering the claims. In its current state, the paper is not ready for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>