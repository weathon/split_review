Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

ChuLo proposes a chunk-level representation for long documents that: (1) splits the document into fixed-length chunks, (2) applies an unsupervised keyphrase extraction algorithm (SKP, adapted from PromptRank) to identify important phrases, and (3) computes chunk embeddings as weighted averages where keyphrase tokens receive higher weight (a > b). These chunk embeddings are then fed into a Transformer-based "chunk attention module" for document classification or into a BERT-decoder for token classification. The method is evaluated on four document-classification datasets and two NER datasets.

## Strengths

1. **Novel and clearly motivated idea**: The paper proposes integrating unsupervised keyphrase extraction into chunk-level document representation (Section 3.2-3.3, Algorithm 1 + Equation 1). The intuition—that not all tokens in a chunk are equally important, and that keyphrase emphasis can preserve semantic content during compression—is a reasonable step beyond prior chunking methods (ChunkBERT, ToBERT) that treat all tokens equally.

2. **Meaningful gains on document classification (LUN dataset)**: On LUN, ChuLo achieves 0.6440 accuracy vs. BERT's 0.5797—a +6.43% improvement (Table 1). For documents >2048 tokens, ChuLo (0.7959) outperforms GPT-4o (0.7143) and Gemini 1.5 Pro (0.6531) (Table 4a). This is the strongest evidence in the paper.

3. **Ablation study shows keyphrase weighting matters**: Table 3a shows PromptRank-based keyphrases (0.6440 on LUN) substantially outperform simple average chunk representations (0.5951) and YAKE-based keyphrases (0.5951). This directly supports the paper's core design claim.

4. **Counterintuitive finding about sentence embeddings**: The ablation in Table 3b shows adding sentence-level information to chunk representations hurts performance (0.9076 vs 0.9538 on HP). While not explored deeply, this is a non-obvious result worth noting.

## Weaknesses

### Fatal
None.

### Major

1. **Token-classification architecture is critically underspecified.** The paper states (line 259) that it "integrate[s] a BERT-decoder module that utilizes the enhanced chunk embeddings to predict token labels." However, no details are given about: (a) how chunk-level embeddings (which collapse all tokens in a chunk via weighted averaging) are mapped back to individual token positions, (b) the loss function used for token-level prediction, (c) whether token-position information is somehow retained or reconstructed, or (d) the architecture of the BERT-decoder and how it interfaces with the chunk attention module. The paper's central claim includes handling "fine-grained token-level tasks," yet the mechanism for doing so is absent. Without this, the NER results in Tables 4-6 are uninterpretable as evidence for the approach's effectiveness at token classification.

2. **NER evaluation uses extremely small, non-standard test sets with no statistical rigor.** On CoNLL-2012 (converted from coreference to NER), the test set contains only 20 documents; on GUM, 26 documents with length >512 tokens (Table 6a/6b). For the longest CoNLL buckets, only 6 (>4096) and 2 (>8192) documents are used. Standard deviations, confidence intervals, or significance tests are never reported. A single-sample difference on the HP dataset (0.0031 margin, 65 test samples) is acknowledged by the authors (line 145) but no correction is applied. With these sample sizes, the headline NER numbers (0.9334 Micro F1) are not credible as evidence of general superiority—they could reflect idiosyncrasies of the particular 20 documents selected. Standard benchmarks (CoNLL-2003, OntoNotes 5.0) with full test sets should have been used.

3. **SKP algorithm has a missing-prompt problem for token classification and unknown-category scenarios.** Algorithm 1 (line 76) constructs the prompt "The * mainly discusses \(k_i\)" where * is the document category. For token classification datasets (GUM, CoNLL-2012), no document-level category exists. The paper never explains how this is handled. If the category was omitted or replaced, this could affect keyphrase extraction quality and fairness; if it was somehow derived from the data, this information leak could artificially inflate results. No ablation addresses this gap.

4. **SKP computational cost is never analyzed.** Algorithm 1 loops over all candidate keyphrases (potentially hundreds) × all document segments, requiring an encoder-decoder forward pass per segment per candidate. The paper provides no runtime, FLOPs, or wall-clock comparison against baselines. Since efficiency is a stated contribution (Contribution 3: "Scalable and Efficient Solution"), the omission is significant—especially because SKP's cost may dominate any savings from shorter input sequences.

### Minor

1. **The "preserving all tokens" claim is overstated.** The abstract and introduction emphasize that the method "preserves all tokens." In reality, individual token identities within a chunk are collapsed into a single weighted-average vector. All tokens contribute to the representation, but their individual information is aggregated away. Token-level tasks require recovering this lost information through the unspecified BERT-decoder. The phrasing over-promises.

2. **Missing ablations on critical hyperparameters.** No ablation is provided for: chunk size (n), weight ratio (a/b), or top-n keyphrase count. These directly affect the trade-off between compression and information preservation. The paper states "Top-n value is set to 15" with a footnote "generally better in most datasets" but no supporting data.

3. **LLM comparisons are zero-shot vs. fine-tuned ChuLo.** Tables 3, 5, and 6 compare fine-tuned ChuLo against zero-shot GPT-4o and Gemini 1.5 Pro. The asymmetry favors the author's model. The paper acknowledges this (line 328: "without fine-tuning") but still uses these comparisons as evidence of superiority. They should either fine-tune the LLMs or clearly separate the comparisons as "fine-tuned" vs. "zero-shot" in the narrative.

4. **The BERT+Random baseline on LUN (0.3015) is surprisingly low with no verification.** While this is not necessarily buggy (random token selection from long documents could yield near-chance performance on a 4-class problem), the authors ran LUN baselines themselves (Table 1 caption) and do not describe their setup, random seeds, or confirm correctness. Since LUN is where ChuLo shows its largest gain, readers cannot fully rule out baseline implementation issues.

### Trivial

- The position penalty term \(r_i = \frac{L_c}{l_d} + \frac{\gamma}{(l_d)^3}\) uses \(\gamma\) with unclear units/scale; its value is not reported.
- Section 3.4 vaguely describes "refined contextual representations" from the chunk attention module without tensor shapes or a clear architectural diagram (Figure 1 is referenced but not parsed).

## Nice-to-Haves

- Evaluating on standard NER benchmarks (CoNLL-2003, OntoNotes 5.0) with full test sets would allow direct comparison with existing NER literature.
- Reporting runtime/wall-clock measurements vs. baselines would substantiate the efficiency claim.
- An ablation isolating the effect of the SKP keyphrase extraction (e.g., using ground-truth keyphrases vs. SKP vs. random weighting) would clarify whether the bottleneck is extraction quality or weighting strategy.

## Removed Points

- **"Impossibly high NER results suggesting unfair comparison/preprocessing mismatch"** — The paper clearly explains that Longformer/BigBird use 4096-token limits and the CoNLL-2012 documents span 1798–9778 tokens. The baseline degradation on documents exceeding 4096 tokens is expected from truncation, not necessarily from a flawed setup. The real issue is test-set size (20 documents), which is retained as a Major weakness. The accusation of "preprocessing mismatch" or "wrong task setup" is speculative without evidence.
  
- **"Token-position discarding makes method unsuitable for document classification"** — For document-level tasks, aggregating tokens within chunks and relying on chunk-level positional encoding is standard practice in hierarchical transformers (ToBERT, ChunkBERT). Chunk positions can be encoded by the chunk attention module. The criticism overstates the issue for document classification.
  
- **"Figure 1 not shown"** — The parser stripped the figure; it exists in the original submission.
  
- **"Table 2 input usage column is uninformative"** — This is a presentation preference, not a substantive weakness.
  
- **"BERT+Random at 0.3015 is far below random guessing"** — The reviewer confuses "random token selection" with "random label prediction." BERT+Random selects 512 random tokens from a long document; 0.3015 on a 4-class problem (25% chance) is actually plausible—barely above chance because random token sampling destroys signal. The criticism is factually incorrect in its reasoning.
  
- **Strength Finder's generic strength about "reasonable motivation"** — The first strength paragraph is too generic ("The motivation is reasonable and relevant") and conflicts with verified weaknesses about underspecified architecture; it is dropped.

## Novel Insights

The most novel observation emerging across the reviews is the tension between the paper's stated goal of "preserving all tokens" and the actual mechanism (weighted averaging within chunks). The averaging step is explicitly lossy at the token level, yet it works reasonably well for document classification on LUN. This suggests a trade-off that the paper does not fully grapple with: a method that demonstrably loses token-position information can still be effective for document-level tasks, but whether it genuinely preserves fine-grained information for token-level tasks remains unsubstantiated. The counterintuitive finding that adding sentence embeddings hurts performance (Table 3b) also points to a poorly understood interaction between hierarchical representation levels—this could be a direction for future work.

## Suggestions

1. **Specify the token-classification architecture completely.** Provide tensor shapes showing how chunk embeddings (num_chunks × hidden_dim) are transformed into token-level predictions (num_tokens × num_labels). Describe the BERT-decoder: is it a Transformer decoder cross-attending to chunk embeddings? How are token positions indexed? What is the loss function? Without this, the NER results cannot be evaluated.

2. **Replace or augment the NER evaluation.** Use standard NER benchmarks (CoNLL-2003, OntoNotes 5.0) with full test sets and report macro/micro F1 with standard deviations over multiple runs. If the method only applies to long documents, at least use the full GUM test set (not just 26 long documents) and report per-length-bin results with confidence intervals.

3. **Address the SKP prompt-category gap.** Explain what category label is used for token-classification datasets (or when the category is unknown). Ablate performance with and without the category in the prompt.

4. **Ablate the key hyperparameters**: chunk size, weight ratio a/b, and top-n keyphrases. Even a single table showing sensitivity on the LUN or HP dataset would substantially strengthen the paper.

5. **Report runtime for SKP vs. baselines.** Provide wall-clock time per document for each stage (keyphrase extraction, chunk embedding, training) so readers can assess the scalability claim.

## Score and Decision

The paper presents a reasonable idea with clear document-classification gains on one dataset (LUN). However, the token-classification architecture is critically underspecified, and the NER evaluation is too thin (tiny, non-standard test sets with no statistical rigor) to support the paper's core claim of handling token-level tasks. The SKP algorithm's prompt-dependency and computational cost are undiscussed. These are major weaknesses that significantly reduce confidence in the paper's claims. The document-classification results are partially convincing but rely heavily on one dataset where baselines were run by the authors with limited verification.

**Weak Reject.** The idea has merit, but in its current form the token-classification contribution is not supported, and the document-classification evidence is too narrow to carry the paper alone. Major architectural specification and evaluation revisions would be needed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>