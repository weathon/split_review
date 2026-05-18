Now I have all the information needed. Let me construct the consolidated review.

## Summary

This paper introduces ChuLo, a method for long document processing that segments documents into fixed-length chunks and uses unsupervised keyphrase extraction (via a modified PromptRank algorithm called SKP) to assign higher weights to keyphrase tokens in chunk-level representations. These weighted chunk embeddings are then processed by a Transformer backbone (BERT) for both document-level classification and token-level NER tasks. The method is evaluated on three document classification datasets (HP, LUN, EURLEX57K, Inverted-EURLEX57K) and two NER datasets (CoNLL-2012, GUM).

## Strengths

- **Novel keyphrase-weighted chunk representation**: The idea of using unsupervised keyphrase extraction to weight chunk embeddings, rather than simple average pooling, is a principled and clean approach to the information-loss problem in long-document processing. The SKP algorithm (Algorithm 1) provides a concrete mechanism for this weighting.

- **Strong empirical gains on long document classification, particularly LUN**: ChuLo achieves 0.6440 accuracy on LUN, a +6.43% improvement over the second-best method (BERT at 0.5797). This is a meaningful and credible improvement on a dataset with substantial document lengths (Table 1, lines 155-164). The method also achieves best or second-best results on EURLEX57K (0.7332) and Inverted-EURLEX57K (0.7244).

- **Consistent performance across document lengths**: On the LUN dataset, ChuLo maintains strong accuracy even on documents exceeding 2048 tokens (0.7959), outperforming GPT-4o (0.7143) and Gemini 1.5 Pro (0.6531) on the same subset (Table 2). This demonstrates genuine robustness to long inputs.

- **Ablation studies confirm design rationale**: The ablations show that PromptRank-based keyphrase extraction outperforms YAKE and average pooling on LUN (0.6440 vs. 0.5951), and that sentence embeddings hurt performance (Table 6). These controlled comparisons support the key design choices.

## Weaknesses

### Fatal
None. While several weaknesses are serious, none individually invalidate the entire paper. The document classification results retain some value independent of the token classification issues.

### Major

- **Token classification decoder architecture is critically underspecified, making results uninterpretable.** The paper describes the token classification architecture in a single sentence (line 259): "we integrate a BERT-decoder module that utilizes the enhanced chunk embeddings to predict token labels more accurately." This is insufficient. The method produces one weighted-average vector per chunk (Eq. 1), losing all per-token positional and identity information within each chunk. How a decoder reconstructs per-token labels from these chunk-level vectors is never explained — there is no description of the decoder's architecture, its input representation, how it recovers positional information across chunk boundaries, or how the loss is computed. Without this, the token-level NER results cannot be assessed for correctness or reproduced. This is a fundamental gap in the paper's presentation of what is claimed as a core contribution ("Enhanced Document and Token Classification," contribution 2).

- **The CoNLL-2012 NER evaluation is on a tiny, non-standard subset (20 test documents) with no statistical reliability measures, yet is used to claim a dramatic ~68% relative improvement.** The paper selects "the top-k longest documents in each split" (line 134), yielding a test set of only 20 documents (Table 5, line 275). No confidence intervals, error bars, or significance tests are reported. The claimed 0.9334 micro F1 vs. 0.5560 for Longformer (Table 4) — a 38-point gap — could easily be dominated by a handful of examples in such a small set. Combined with the architectural underspecification above, this result cannot be taken at face value. The paper should either evaluate on the full CoNLL-2012 test set (stratified by length) or provide statistical confidence measures.

- **The SKP algorithm's prompt template introduces an ambiguous dependency that could constitute label leakage, contradicting the "unsupervised" claim.** Algorithm 1 (line 76) constructs the prompt "The * mainly discusses \(k_i\)" where "* is the category of the document." For the classification datasets evaluated (HP: hyperpartisan/not; LUN: satire/propaganda/hoax; EURLEX57K: 4271 legal concepts), the document "category" is precisely the classification label. If the category is obtained from the label during keyphrase extraction, this is label leakage and the method is not unsupervised. The paper does not clarify where the category comes from or whether the SKP algorithm is applied without access to labels. This needs immediate clarification.

- **No description of how Longformer and BigBird baselines were adapted for token-level NER on this specific long-document subset.** The paper compares against Longformer and BigBird for NER (lines 258-260) but provides no detail on whether they were fine-tuned on the same training subset of longest documents, how they were configured for token classification (which is not their standard use case), or what hyperparameters were used. If the baselines were trained on standard (short) CoNLL-2012 data and evaluated on the long-document subset, the comparison is fundamentally unfair and the 38-point gap is spurious.

### Minor

- **Keyphrase weighting provides zero benefit on the HP dataset.** The ablation study (Table 6a) shows that average chunk representations (no keyphrase weighting) achieve identical accuracy (0.9538) to the full PromptRank-based method on HP. Only on LUN does PromptRank yield a material gain (0.6440 vs. 0.5951). The paper overstates the importance of the keyphrase extraction pipeline given that in half the document classification datasets, it contributes nothing.

- **Ablation studies are limited to HP and LUN (document classification only).** No ablations are performed for the NER setting, so the contribution of the keyphrase weighting to token-level performance is not isolated. For NER, the paper does not compare against a simple average-pooling baseline, so the reader cannot tell whether the 0.9334 is due to keyphrase weighting or simply the chunking+decoder setup.

- **No hyperparameter sensitivity analysis.** The paper introduces several hyperparameters — \(a, b\) (token weight ratio, Eq. 1), \(\alpha, \gamma\) (SKP algorithm, Algorithm 1), chunk size \(n\), and top-\(n\) keyphrases — but reports no sensitivity analysis for any of them, noting only that they are "experimentally determined."

### Trivial

None.

## Nice-to-Haves

- Include training cost comparisons (FLOPs, runtime, throughput) to substantiate the "Efficient" claim in the title and contribution (3).
- Replace the zero-shot GPT-4o/Gemini NER comparisons with fine-tuned token-level baselines (e.g., RoBERTa + hierarchical NER head) for a more meaningful comparison.
- Expand the qualitative analysis beyond a single example (Figure 6) to include failure cases and side-by-side comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Non-overlapping chunking is the standard method the paper criticizes"** — The paper's contribution is the keyphrase-weighted chunk representation, not the chunking strategy itself. The criticism conflates the generic chunking mechanism with the paper's specific semantic weighting approach, which is distinct from standard chunking. The paper is transparent about using non-overlapping chunks as a preprocessing step.

2. **"The comparison to GPT-4o/Gemini is weak/tangential"** — While these comparisons have limited value for benchmarking, they are presented as additional context rather than core evidence. The reviewer's suggestion to replace them with fine-tuned baselines is valid but is a suggestion for improvement, not a weakness of what the paper does report. Moved to Nice-to-Haves.

3. **"Inverted-Eurlex57k is not clearly described"** — The paper describes it as "where the header and recitals are moved to the end" (line 131), which is sufficient for a synthetic benchmark.

4. **Strength: "Dramatic improvement on token classification"** — This directly conflicts with the verified weaknesses that the token classification experiments are on a tiny subset with an unspecified architecture. Per the rule, when a strength and verified weakness disagree, the weakness wins. Removed.

## Novel Insights

The harsh critic's observation that the SKP prompt template introduces an ambiguous circular dependency ("category of the document") is a genuinely insightful catch that goes beyond surface-level issues. If the "category" refers to the classification label, this would constitute label leakage in an allegedly unsupervised pipeline — a structural flaw rather than a presentation issue. Conversely, if the authors clarify that "category" is obtained from document metadata or some unsupervised signal, this concern is resolved. Either way, this ambiguity is a real issue that needs addressing and was not noted in any straightforward reading of the paper itself.

## Suggestions

1. **Fully specify the token classification decoder architecture.** Provide the complete logical flow: how chunk embeddings (which are weighted averages per chunk) serve as input to the decoder, how per-token logits are generated, how positional information is recovered, and how the loss is computed. Without this, the token-level results are not publishable.

2. **Re-run the CoNLL-2012 evaluation on the full test set** (or a principled long-document subset with proper statistical measures). Report results stratified by document length, and include confidence intervals or bootstrap estimates. Also ensure baselines are fine-tuned on the same training distribution.

3. **Clarify the SKP prompt's "category" field.** Explicitly state whether this requires access to the label during keyphrase extraction. If it does, the method is not unsupervised and the paper must report experiments controlling for this leakage. If it does not, explain what "category" refers to and how it is obtained without labels.

4. **Add an NER ablation with average chunk representations** (no keyphrase weighting) to isolate the contribution of semantic emphasis to token-level performance. This is currently missing and is essential for supporting the paper's claims.

5. **Report hyperparameter sensitivity** for \(a, b, \alpha, \gamma\), at least on one dataset, to demonstrate robustness.

## Score and Decision

The core idea — keyphrase-weighted chunk representations — is reasonable and shows genuine promise for document-level classification, particularly on LUN where gains are substantial and well-supported. However, the paper's most eye-catching claims (the 38-point NER improvement on CoNLL-2012) rest on insufficiently described methodology, an extremely small evaluation set, potentially unfair baseline comparisons, and an underspecified decoder architecture. Additionally, the SKP algorithm's ambiguous use of "document category" raises potentially serious concerns about label leakage in what is described as an unsupervised pipeline. These issues collectively mean the paper's token-level contributions are not currently credible, and one of the paper's three stated contributions is substantially unsupported.

The document classification results alone represent a modest but solid contribution. However, the paper frames token classification as a central motivation and key contribution. In its current form, the evidence is insufficient to support acceptance at a top venue. The paper would need substantially revised token-level experiments and full architectural transparency to be reconsidered.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>