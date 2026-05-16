Now I have all the information I need. Let me produce the final consolidated review.

## Summary

The paper proposes WASA, a watermarking framework that enables LLMs to embed invisible Unicode watermarks into generated text for source attribution (identifying which data provider's data contributed to a generated text) and data provenance (verifying whether a provider's data was used in training). The approach assigns unique 10-character watermarks to each data provider, embeds them into representative (top TF-IDF) sentences during training, and uses separate prediction spaces for word and watermark tokens. Experiments on ArXiv and BookSum datasets with GPT2 and OPT show high source attribution accuracy (74–88% top-1 for 10 providers) and robustness against several attack types.

## Strengths

- **Novel problem and first framework for source attribution via watermarking in LLMs.** The paper defines a new problem setting with 6 clearly articulated properties (accuracy, robustness, scalability, performance preservation, transferability, adaptability) and proposes the first method to address all of them. This is a meaningful contribution to an important practical problem (IP protection in LLM training data).

- **High source attribution accuracy significantly above random baseline.** Table 1 reports 74.84% top-1 accuracy on ArXiv with GPT2 (random 10%) and 88.26% on BookSum. Top-5 accuracy reaches 95–99% across settings, demonstrating that the watermarking approach works reliably under the tested conditions.

- **Robustness demonstrated via watermark regeneration.** Table 2 shows that after watermark removal/modification, regenerated watermarks achieve 71.60% top-1 accuracy (93.76% top-3). Under additional insertion/deletion/synonym substitution attacks, accuracy degrades but remains well above random chance, indicating the regeneration mechanism provides meaningful defense.

- **Scalability to larger numbers of providers is demonstrated.** Table 3 shows that with 100 providers, WASA achieves 18.38% top-1 accuracy (vs. 1% random) and 56.14% top-5 accuracy, with graceful degradation. The watermark design (6¹⁰ ≈ 60M unique watermarks) supports this scaling.

- **Adaptability to different LLM architectures.** WASA is demonstrated with both GPT2-Large and OPT-1.3B (Table 1), and the modifications required (adding 6 vocabulary entries, separate softmax layers) are mild and architecture-agnostic.

## Weaknesses

### Fatal

None.

### Major

- **Source attribution evaluation uses prompts from the same sentences that contained watermarks during training, limiting generalization evidence.** Section 4.1 (lines 158–160) states: "for each data provider, we use the **sentences selected for watermarking** (after removing the watermarks) as the inputs/prompts." These are the top-20% TF-IDF sentences into which watermarks were embedded during training. The model is tested on prefixes of the exact same sentences it saw during training (with watermarks at random positions). This experimental design cannot distinguish between (a) the model genuinely learning a general mapping from a provider's writing style to its watermark and (b) the model simply learning that after certain familiar sentence fragments, it should emit `[WTM]` followed by specific watermark tokens. The paper's central claim is that WASA learns "an accurate mapping from the texts of different data providers to their corresponding watermarks" (abstract, line 19), but the evaluation does not demonstrate this mapping generalizes to unseen, arbitrary text from the same provider. The data provenance experiment (lines 167) provides partial complementary evidence by testing on text from different papers/categories, but the core source attribution numbers rest entirely on the non-generalizing evaluation. This is the most significant weakness in the paper.

- **No comparison to any non-watermarking baseline.** The paper compares only to random chance (10% for 10 providers). A natural baseline would be a text classifier (e.g., fine-tuned transformer encoder) trained to predict the data provider from generated text without any watermarking. Such a baseline would help assess whether the complexity and constraints of the watermarking framework are justified. If a simple classifier achieves comparable accuracy, the value proposition of watermarking weakens considerably; if it does not, the paper's contribution is strengthened. Without this comparison, the reader cannot quantify the marginal benefit of the WASA approach.

### Minor

- **Transferability (Property 5) is asserted without empirical verification.** Section 2 lists transferability — "the generated watermarked texts can be readily used as training data for other LLMs" — as a key property, but the paper provides no experiment showing that a different LLM trained on WASA's output actually learns to produce correct watermarks. The argument is purely structural (lines 39–40, 201): the generated data "has the same structure" as the training data. This is a reasonable hypothesis but remains unvalidated.

- **Paraphrase attack not tested in robustness evaluation.** The paper tests insertion, deletion, synonym substitution, and syntactic transformation (line 185), but does not test a strong adversary who rewrites the entire text via a different LLM while preserving semantic meaning. Since the watermark consists of invisible Unicode characters, such paraphrasing could remove them, and it is unclear whether regeneration would work after such aggressive semantic-preserving modification.

- **Data provenance results for "not used" categories lack explicit numerical accuracy in the main text.** Line 167 states that for the 10 categories whose data was not used in training, WASA can "consistently recognize that their data was not misused," but no accuracy, false positive rate, or decision threshold is reported in the main paper. The full results are in Table 7 (appendix). For a central claimed capability, the main text should stand on its own.

- **False positive rate and per-provider precision/recall for source attribution are not reported.** The paper reports only top-k accuracy. For practical deployment (e.g., IP litigation), understanding the per-provider confusion matrix and the rate of false attributions is essential. The error analysis in Table 8 (appendix) partially addresses this but is not in the main text.

### Trivial

None.

## Nice-to-Haves

- Test on providers with imbalanced data sizes or similar writing styles, which the paper acknowledges as a limitation (conclusion) but does not explore.
- Provide an ablation isolating the generalization question: test source attribution on sentences from each provider that were *not* in the top-20% TF-IDF pool and thus never seen during watermark training.
- Report performance preservation metrics (e.g., perplexity) in the main text rather than only in the appendix.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh critic criticism about "the LLM sees the watermark tokens only after a specific sentence fragment, not after arbitrary text from the same provider" and "paper does not discuss how this generalization is supposed to occur":* This is largely a restatement of the first Major weakness above. However, the paper does discuss the mechanism for generalization indirectly via the separation of prediction/generation spaces (Sec. 3.2) and the training objective that conditions watermark prediction on text context. The reviewer's framing as a "missing discussion" overstates the gap — the issue is experimental, not conceptual. This point is subsumed by the first Major weakness.

- *Harsh critic criticism about forced watermark generation inflating accuracy:* The paper addresses this directly with ablations in Appendices G.3 and G.4 showing that natural vs. forced generation yields comparable accuracy and that longer texts reduce the need for forcing. The reviewer acknowledges these ablations exist. This criticism does not survive verification against the paper.

- *Harsh critic criticism about scalability (48.27% top-1 for 100 providers, questioning practical utility):* The paper is transparent about the accuracy decrease and explicitly recommends using top-k attribution for large numbers of providers (lines 192). This is an honest discussion of a limitation, not a weakness. The reviewer is criticizing the method for a known trade-off the authors already acknowledge.

- *Harsh critic criticism that data provenance evidence is entirely missing from the main text:* This is factually incorrect — the main text (line 167) reports 74.84% and 95.76% accuracy for the "used" categories and references Table 7 for "not used" categories. The reviewer's claim that "no accuracy or false-positive rate is reported in the main paper" is partially wrong. The partial validity (missing numbers for "not used" categories) is captured in the Minor weakness above.

- *Strength Finder's claim that "first framework for source attribution via watermarking in LLMs" is a strength:* This is retained in the Strengths section above (first bullet). However, the Strength Finder's phrasing of "adaptable to different LLM architectures" and "preserves LLM text generation performance" as strengths is retained but tempered — the latter relies on appendix-only data.

## Novel Insights

The harsh critic correctly identifies a significant experimental design limitation: the source attribution evaluation uses prompts drawn from exactly the same set of sentences that were watermarked during training, which conflates memorization with genuine generalization. However, the data provenance experiment provides partial evidence that WASA can work on text from entirely unseen categories (Table 7), suggesting the method has some generalization capacity beyond simple memorization. The most important gap is not that the paper's results are wrong, but that the reader cannot tell how much of the reported accuracy reflects genuine text-to-watermark mapping versus memorization of training instances. A clean experiment using held-out sentences from the same providers would resolve this.

## Suggestions

1. **Fix the generalization gap in the evaluation.** Repeat the source attribution experiment using prompts from sentences that were *never* watermarked during training — e.g., the bottom 80% of TF-IDF sentences from each provider, or entirely different documents from the same category. If accuracy remains comparable, the claim of learning a "text-to-watermark mapping" is strongly supported. If it drops significantly, the method is learning something closer to sentence-specific memorization, which would be a fundamental limitation.

2. **Add a non-watermarking baseline.** Train a standard text classifier (e.g., fine-tuned BERT/RoBERTa) to predict the data provider from generated text. Report its accuracy alongside WASA's. This single addition would greatly clarify the contribution's magnitude.

3. **Empirically verify transferability.** Train a second LLM (with the same WASA modifications) on WASA-generated watermarked text and measure whether it learns to produce correct watermarks. Without this, Property 5 remains an untested claim.

4. **Report per-provider precision/recall and a confusion matrix for the 10-provider setting.** This would give readers a clear picture of where errors occur and whether certain providers' watermarks are systematically confused.

5. **Test against LLM-based paraphrasing** as a robustness attack to strengthen the practical claims.

## Score and Decision

The paper tackles an important and timely problem, proposes a principled framework with clear properties, and provides extensive experimental results. The main technical ideas (separation of prediction/generation spaces, TF-IDF-guided watermark embedding, watermark regeneration for robustness) are sound and well-motivated.

However, the central evaluation limitation — testing source attribution on the same sentences that were watermarked during training — prevents the reader from assessing whether the claimed "text-to-watermark mapping" generalizes to arbitrary provider text. This is a significant empirical gap, especially since the paper's core claim hinges on this generalization. The absence of any non-watermarking baseline further weakens the ability to assess contribution magnitude. These are structural evidential issues, not minor presentation problems.

The paper could be substantially strengthened with additional experiments (held-out sentences, non-watermarking baseline), but in its current form, the evidence does not fully support the claims as stated. 

**Score: 5.0**

**Decision: Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>