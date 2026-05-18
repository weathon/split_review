I have thoroughly analyzed the paper against all the reviewer claims. Now I will produce the final consolidated review.

## Summary

The paper proposes WASA, a watermarking framework for source attribution and data provenance of LLM-generated text. It assigns unique invisible Unicode watermarks to data providers and trains the LLM (via second-stage pre-training with separated prediction spaces for word and watermark tokens) to embed provider-specific watermarks into generated text. The paper identifies six key properties such a framework should satisfy and provides empirical results on ArXiv and BookSum datasets using GPT2-Large and OPT-1.3B.

## Strengths

- **Well-motivated and clearly defined problem.** The paper addresses a timely and practically important issue — identifying which data provider contributed to LLM-generated text — with a clean problem formulation involving three parties (data providers, LLM operator, users) and the data provider characteristics that support the approach.

- **Clean technical design with explicit separation of prediction/generation spaces.** The method of augmenting the vocabulary with 6 Unicode watermark tokens, maintaining separate softmax/output spaces for word vs. watermark tokens, and using a special `[WTM]` switch token is elegant. The design minimizes interference with the LLM's original capabilities (via separated gradient updates for the last linear layer) and naturally supports both training and generation of watermarks.

- **Source attribution accuracy well above random baseline on the evaluated setting.** Table 1 reports 74.84% top-1 and 95.76% top-3 accuracy with 10 providers (10% random baseline), consistent across GPT2-Large and OPT-1.3B on two datasets. This demonstrates the model can learn a text-to-watermark mapping when evaluated as designed (see Weaknesses for caveats on evaluation protocol).

- **Robustness evaluation across multiple attack types.** Table 2 shows that top-3 accuracy remains between 83.76%–87.20% under combined attacks (watermark removal/modification plus insertion, deletion, or synonym substitution), suggesting the learned text-to-watermark mapping provides genuine robustness.

- **Scalability demonstrated up to 100 providers.** Table 3 shows that top-5 accuracy remains at 65.88% with 100 providers (5% random baseline), demonstrating the method can meaningfully attribute across a large provider set.

- **Multiple ablation studies validate key design decisions.** The paper includes ablations on: TF-IDF vs. random sentence selection, impact of watermark length, forced vs. natural watermark generation, and proportion of watermarked training data — all backed by empirical results.

## Weaknesses

### Fatal
None.

### Major

- **Source attribution accuracy is evaluated using prompts from the training set, so generalization to unseen prompts is unmeasured.** The evaluation (Sec. 4.1) uses "the sentences selected for watermarking (after removing the watermarks) as the inputs/prompts" (line 159). These sentences were seen during training (with watermarks embedded). While the model generates *new* continuations (100 tokens), the prompts are from the training distribution. The paper reports 74.84% accuracy, but this may reflect the model's ability to map memorized prompt-to-watermark associations rather than a generalizable text-to-watermark mapping. For a practical deployment, the LLM must attribute based on arbitrary user prompts, not just pieces of training sentences. A proper evaluation requires holding out some papers per provider for testing, or using unseen prompt templates from each provider's style. Without this, the central claim of "accurate source attribution" for real use is not supported.

- **Transferability (Property 5) is claimed without any experimental validation.** The paper states (line 201) that generated watermarked text "can be readily used as training data for other LLMs" based solely on structural similarity to the training data. No experiment trains another LLM on WASA-generated text and measures whether watermarks persist across models (let alone accurately). Since transferability is listed as one of the six key properties that the framework "satisfies," its absence from the empirical evaluation is a significant gap.

- **Performance preservation is weakly supported.** The paper cites only Table 10 (in the appendix, which we cannot verify from the main text) and a qualitative example in App. C. No perplexity comparison against an unwatermarked baseline, no standard fluency/quality metric (e.g., perplexity, BLEU with respect to ground-truth continuations, or human evaluation) is reported. The claim that watermarks "do not significantly degrade" text generation ability is therefore unsubstantiated by the evidence presented in the main paper.

### Minor

- **Data per provider is not controlled in the scalability experiment.** Sec. 4.3 reports accuracy as the number of providers grows, but does not clarify whether total training data is held constant (meaning less data per provider) or data per provider is held constant (meaning less ability to learn fine-grained mappings for each provider). These two scenarios have different interpretations for the accuracy drop, and the paper should clarify or control for this.

- **The watermark regeneration protocol for robustness evaluation is underspecified.** The paper says (line 183): "we clean the generated sentence by removing the corrupted watermark, and use the cleaned sentence as input/prompt to WASA-LLM to regenerate the watermark (without synthetic texts)." It is not specified whether `[WTM]` is appended to force watermark generation (as in the accuracy evaluation), or whether the model generates `[WTM]` naturally, or whether some other mechanism is used. Since the robustness numbers rely on regeneration, the protocol should be explicitly stated and reported with and without forced regeneration as a baseline.

- **No discussion of how invisible Unicode watermarks interact with downstream text processing.** The 6 chosen Unicode characters (zero-width spaces, joiners, invisible operators) are rendered invisible on many platforms, but common text processing (copy-paste, HTML rendering, tokenization, spell-checkers, NLP pipelines) may strip, canonicalize, or alter these characters. The robustness results may not hold if the text passes through such systems, and this limitation is not discussed.

### Trivial
None.

## Nice-to-Haves

- A held-out evaluation where prompts come from papers/sentences not seen during training (e.g., a time-based or random split within each provider's data) would directly address the generalization concern.
- An actual transferability experiment training a small LLM from scratch (or fine-tuning another pre-trained model) on WASA-generated text and measuring watermark persistence would substantiate Property 5.
- Perplexity scores or a standard fluency metric comparing WASA-LLM against the original unmodified LLM would quantify performance preservation.
- The TF-IDF vs. random sentence selection ablation (currently in App. G.5) is informative enough to belong in the main paper.
- Reporting whether data per provider is held constant in the scaling experiments would rule out the data-sparsity confound.

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

- **"No comparison with any alternative method"** — The paper claims to be the first watermarking framework for LLM source attribution. A style-based classifier (e.g., fine-tuned BERT) solves a different problem and does not use watermarking. Since there is no directly comparable prior method in this specific setting, the absence of a baseline does not constitute a weakness. The paper's contribution is in watermark-based attribution, not in generic text classification.

- **"Data provenance experiment lacks a proper false-positive test"** — The paper (line 167) explicitly tests 10 categories whose data was NOT used in training and reports they are "consistently able to recognize that their data was not misused." This is a proper false-positive test. The criticism is factually incorrect.

- **"Novelty claim should be toned down given Liu et al. (2023a)"** — The paper acknowledges Liu et al. and clearly distinguishes its focus (source attribution) from data provenance. The claim is qualified as "to our best knowledge" and is about watermarking frameworks specifically for source attribution, which is a fair distinction.

- **"Forced watermark generation obscures natural behavior"** — The paper acknowledges this concern, provides ablations showing forced vs. natural generation yield comparable accuracy (App. G.3), and shows that longer generated texts require less forced generation (App. G.4). The concern is already addressed by the paper's own experiments.

- **"Testing on training-set sentences means results are meaningless"** — While the prompts come from training data, the evaluation tests whether the model generates the *correct watermark in newly generated continuations* (100 new tokens). This is not simply regurgitating memorized training examples. The concern is real (generalization is unmeasured), but the characterization as "testing on training data" in a standard supervised sense is overstated.

## Novel Insights

None beyond the paper's own contributions, but one key observation emerges from cross-referencing the reviews: WASA sits at an unusual intersection. It proposes a watermarking method that must be evaluated for both *detection* accuracy (can we read the watermark?) and *generation* accuracy (does the model embed it correctly?), but the evaluation conflates both into a single accuracy number by forcing watermark generation. This makes it hard to diagnose whether failures are from the model not learning the text-to-watermark mapping or from the watermark decoder not extracting it correctly. The reviewers' critiques about forced generation, training-data prompts, and regeneration protocol all stem from this conflation, suggesting the paper would benefit from reporting generation rate (how often does the model naturally produce `[WTM]`?) and decoding success rate separately.

## Suggestions

1. **Add a held-out prompt evaluation.** Split each provider's data so some papers/sentences are never used in training (second-stage pre-training). Use these as evaluation prompts. Report accuracy separately for seen vs. unseen prompts.

2. **Experimentally test transferability.** Train a small GPT-2 model from scratch on WASA-generated watermarked text, or fine-tune a pre-trained model, and measure whether watermarks persist and remain source-attributable.

3. **Report perplexity or a standard fluency metric** comparing WASA-LLM to an unmodified version of the base model on a held-out corpus, to substantiate the performance preservation claim.

4. **Explicitly specify the watermark regeneration protocol** in the robustness experiments — specifically whether `[WTM]` is appended to force generation, and report accuracy both with and without forced regeneration.

5. **Control for data-per-provider in scalability experiments.** Either hold data per provider constant (adding more total data) or total data constant (splitting among more providers) and clearly state which.

## Score and Decision

**Originality:** The paper introduces a novel technical approach (separated prediction spaces for provider-specific watermark generation) to a problem (LLM source attribution) that has received little prior attention in the text domain. The six-property framework is well-considered.

**Importance:** The problem is timely and practically relevant given the growing use of LLMs in commercial applications and IP/data protection regulations.

**Soundness:** The technical design is sound. However, the empirical evaluation has significant gaps: source attribution is tested with training-set prompts (generalization unverified), transferability is not experimentally tested, and performance preservation lacks quantitative fluency metrics. These gaps prevent full acceptance of the claims.

**Clarity:** The paper is generally well-written and the method is clearly explained. The regeneration protocol and scalability confound could be clearer.

**Value to community:** If the evaluation gaps are addressed, this could be a valuable contribution to watermarking and LLM governance. In its current form, the claims outpace the evidence.

The paper has a well-motivated approach and a clean technical design, but the evaluation has two major gaps (training-set-only prompting for accuracy measurement, untested transferability) and several minor ones. These are addressable in revision but prevent acceptance in the current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>