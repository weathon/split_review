Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper proposes WASA (Watermarking for Source Attribution), a framework that embeds invisible Unicode character watermarks into the training data of data providers, trains an LLM with separate prediction spaces for text and watermark tokens, and enables the LLM to generate text with embedded watermarks that can be decoded to identify which data provider's training data most influenced the output. The framework is evaluated on ArXiv and BookSum datasets across multiple model architectures (GPT2-Large, OPT-1.3B, Llama2-7B), reporting top-1 accuracy of ~75–83% and top-5 accuracy of ~97–99%, substantially outperforming a BM25 baseline.

## Strengths

- **Principled problem formulation and property framework**: The paper identifies six key properties for source attribution watermarking (accuracy, robustness, scalability, performance preservation, transferability, adaptability) and organizes the presentation around verifying each one (Section 2). This provides a structured evaluation methodology that goes beyond simply reporting accuracy.

- **Separate prediction space design minimizes interference**: Using separate softmax layers for word tokens (Eq. 3) and watermark tokens (Eq. 4) is a clean engineering solution that adds only E×V' parameters while preventing the watermark generation from interfering with text generation and vice versa (Section 3.2). This directly supports both the accuracy and performance preservation properties.

- **Cross-architecture adaptability demonstrated**: The framework is validated across GPT2-Large, OPT-1.3B, and Llama2-7B with consistent improvements over BM25 (Table 1 and appendix references), supporting the adaptability property across different decoder-only transformer architectures.

- **Fine-grained error analysis**: Decomposing errors into misclassification vs. incorrect watermark generation (Section 4.1) reveals that the model rarely generates watermarks not belonging to any category, indicating the learned mapping is internally consistent even when attribution fails. This insight is informative for understanding failure modes.

- **TF-IDF-based selective watermarking is well-motivated**: Selecting the top 20% TF-IDF sentences for watermarking explicitly targets the most provider-distinctive content, providing a principled trade-off between attribution accuracy and text quality (Section 3.1), and the appendix shows it outperforms random selection.

## Weaknesses

### Fatal
None.

### Major

- **Conceptual gap between style-based classification and genuine source attribution**: The paper defines source attribution as identifying when a data provider's training data "contributed to the generation of a synthetic text" (Section 1), but WASA operationalizes this as classifying which provider's stylistic patterns the input most resembles. If a user prompts with text mimicking Provider A's style, WASA will output Provider A's watermark—regardless of whether Provider A's data actually influenced the model's knowledge. The paper explicitly assumes "each data provider contributes ample balanced data with unique characteristics" (Line 53), which concedes the method relies on providers having distinctive styles. This limits applicability to settings where data providers have distinguishable characteristics and, more fundamentally, means the method measures input classification rather than training data influence. The evaluation results (75–83% top-1 accuracy) in this most-favorable setting (where prompts are characteristic sentences from known providers) also underscore the gap: even when prompts are stylistically distinctive, accuracy is far from perfect.

- **Evaluation is confined to the easiest case and avoids the most challenging scenarios**: The accuracy evaluation (Section 5.1) uses "the sentences selected for watermarking (after removing the watermarks)" as prompts—these are the top-20% TF-IDF sentences, i.e., the most stylistically distinctive sentences from each provider. The paper explicitly acknowledges that it excludes the "edge case where the generated content correlates the most with pretraining data rather than data from data providers" (Line 94), ensuring evaluations only handle the unambiguous case. There is no evaluation with generic prompts (e.g., "Explain quantum computing") where source attribution is most needed and most challenging. Without testing such cases, the claimed "effective source attribution" (abstract) is supported only in the most favorable setting.

- **Missing comparison with a trained classifier baseline**: BM25, the sole baseline, is an unsupervised retrieval algorithm with no learning capability. Comparing against only BM25 does not establish how much WASA's watermarking mechanism adds beyond what a straightforward supervised classifier (e.g., fine-tuned on TF-IDF features or a simple neural text classifier) would achieve. Since WASA's watermarking component essentially learns a text-to-provider mapping (similar to classification), a classifier baseline would reveal whether the watermark injection mechanism provides benefits beyond classification alone. This is especially important given that BM25 already achieves 55–60% accuracy on this favorable task, suggesting classification is partially solvable without any watermarking.

### Minor

- **Robustness to Unicode stripping is not fully addressed**: The watermarks use invisible Unicode characters (U+200B, U+200C, U+200D, U+2062–U+2064), which can be removed by standard text normalization pipelines. The paper argues the WASA-LLM can "regenerate" watermarks from cleaned text (Section 3.2), but regeneration requires re-accessing the model. If the model is unavailable or the operator is uncooperative, the watermarks are permanently lost. While this is partially addressed by the regeneration mechanism within the paper's threat model, it represents a meaningful practical limitation not fully discussed.

- **Scalability claims should be validated beyond 10 providers**: The main experiments use only 10 data providers per dataset. The watermark space supports 6^10 ≈ 60 million unique watermarks in theory, but empirical accuracy degradation with increasing provider count is not demonstrated in the main paper.

### Trivial
None.

## Nice-to-Haves

- Evaluation with generic/out-of-distribution prompts where no single provider's style dominates, to test source attribution in realistic deployment conditions.
- A controlled experiment disentangling style from influence: e.g., Provider A provides distinctive style, Provider B provides substantive knowledge on a topic; test whether the model attributes to A or B.
- Comparison with a fine-tuned text classifier to quantify the value added by the watermarking mechanism beyond classification.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Circular evaluation" claim that the evaluation is tautological**: The Harsh Critic called the evaluation "cautological" and "circular" because the model is trained on text-watermark associations and then tested on them. However, the evaluation uses a separate set of 50 sentences per provider (not training data) for testing. The model must generalize the learned mapping—this is supervised classification with train/test splits, not tautology. The real weakness is that the test prompts are the most characteristic sentences (top-20% TF-IDF), which makes the task easier, but it is not circular.

- **"The ~75–83% accuracy is surprisingly low for a nearest-neighbor classification task"**: This mischaracterizes the method—WASA is not nearest-neighbor classification, it is a language model that must learn to produce the correct watermark sequence during generation. The task involves continued text generation conditioned on a prompt, not simple retrieval.

- **BM25 comparison is "not informative"**: The Harsh Critic argued that since BM25 has no watermarking capability, comparing against it is unfair. This is incorrect—comparing against BM25 actually tests the asymmetric question of whether the watermark injection adds value beyond what surface-level text similarity alone can provide. BM25 is a reasonable natural baseline for a problem with no prior solutions.

- **"Watermarking scheme is trivially defeatable" (as a fatal flaw)**: The paper discusses a regeneration mechanism (Lines 274-275) where the WASA-LLM can regenerate watermarks from cleaned text. Within the paper's threat model (honest LLM platform operator), this is a partial solution. While the vulnerability to Unicode stripping is a genuine minor limitation, frame it as the paper does partially address this.

- **Missing related works / "no existing baseline" claim questioned**: As per my instructions, I do not flag missing related works.

- **Formatting/typo nitpicks**: Removed per hard rules.

- **Requests for reproducibility details**: Removed per hard rules (undisclosed hyperparameters, implementation details).

- **Strength finder claims about "first framework" novelty**: Removed as a strength since the novelty claim is undermined by the conceptual gap weakness above—that the method measures style classification rather than influence attribution.

## Novel Insights

The paper's most interesting contribution is the formalization of the source attribution problem through the lens of six desirable properties (accuracy, robustness, scalability, performance preservation, transferability, adaptability), which provides a useful evaluative framework even if the current instantiation falls short on the most important property. The separation of prediction spaces for watermark vs. text tokens is a technically clean idea that minimizes parameter overhead while ensuring watermark generation does not interfere with text quality. However, the fundamental tension this review identifies—between what the paper claims to do (identify which data provider "contributed to the generation") and what it actually does (classify which provider's style the input most resembles)—remains the central unresolved issue. The paper's own explicit scope restrictions (distinctive provider styles, excluding pretraining data dominance, single-source attribution) collectively mark out the boundary of the method's applicability, and these boundaries are narrower than the paper's broad framing suggests.

## Suggestions

- Reframe the contribution as "style-attributed watermarking" rather than "source attribution" to accurately reflect what the method achieves, or add a substantial discussion of the gap between style correlation and causal influence.
- Add experiments with open-ended/generic prompts (not derived from any provider's data) to establish performance in more realistic deployment conditions, and compare against a fine-tuned text classifier to isolate the contribution of the watermarking mechanism beyond classification.

## Score and Decision

The paper addresses a genuinely important problem and proposes a technically clean framework with a novel mechanism (separate prediction spaces for watermark tokens). However, the conceptual gap between style-based classification and genuine source attribution is substantive: the method determines which provider's style the input most resembles, not which provider's data causally influenced the output. The evaluation is restricted to the most favorable case (characteristic sentences from known providers), explicitly excluding the harder scenarios where source attribution is most needed. The absence of a trained classifier baseline makes it unclear whether the watermarking mechanism adds value beyond a simpler approach. These issues significantly limit the strength of the paper's central claims, though the technical framework itself is sound engineering.

**Originality**: Moderate — watermarking for source attribution in LLMs is a new framing, but the method reduces to learned style classification with watermark tokens as labels.

**Importance of research question**: High — source attribution for LLM-generated text is a significant and timely problem.

**Claims well supported**: Partially — supported in the favorable setting tested, but not in the more challenging settings that matter most.

**Soundness of experiments**: Limited — only the easiest case is tested, with no classifier baseline and no generic-prompt evaluation.

**Clarity**: Good — clear presentation with well-organized properties framework.

**Value**: Moderate — the problem formulation and property framework contribute value, but the solution's scope is narrower than claimed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>