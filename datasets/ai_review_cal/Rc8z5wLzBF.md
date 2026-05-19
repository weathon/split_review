- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 8, 3, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

OmniBench is a new benchmark (1,142 samples) designed to evaluate multimodal LLMs on tri-modal reasoning requiring simultaneous understanding of image, audio, and text inputs. The paper also contributes OmniInstruct, a curated instruction-tuning dataset (84.5K samples) for training omni-language models (OLMs). The evaluation spans a broad range of models (open-source OLMs, VLMs, ALMs, and proprietary models) under multiple ablation settings, revealing that even the best models perform poorly (most below 50% accuracy).

## Strengths

- **Rigorous three-stage annotation pipeline enforces true tri-modal dependency**: The annotation protocol (Section 3.2, Figure 3) combines human inspection with automatic MLLM verification (LLaVA-1.6-34B) under ablation conditions (image-only, audio-transcript-only, text-only). Samples pass only when the model cannot answer with fewer than three modalities, directly ensuring that the benchmark tests integrated tri-modal understanding rather than reliance on a single dominant modality.

- **Comprehensive baseline evaluation across modal families reveals clear patterns**: Tables 2–5 evaluate 6+ OLM baselines, 15+ VLMs, and 8+ ALMs under full-information and ablation settings. The consistent finding that open-source OLMs perform below 50% accuracy, and that VLMs outperform ALMs under textual approximations, provides concrete evidence supporting the paper's central claim that current models lack robust tri-modal reasoning.

- **Fine-grained taxonomy enables structured task analysis**: The benchmark organizes 1,142 questions into 3 major categories and 8 subclasses (Figure 2, Table 1) with detailed statistics on image resolution, audio length, and text length. This supports per-category performance reporting (Table 2 bottom), revealing that models struggle most on abstract-concept tasks (e.g., counting at 6–46%) while performing better on object identification.

- **Textual-approximation experiments isolate modality-specific bottlenecks**: By replacing images with VLM-generated captions and audio with human-annotated transcripts (Tables 3, 4; Figure 5), the paper provides a controlled way to study how each modality contributes to performance. Specific findings (e.g., UnifiedIO-2 gains 6.42% from audio transcripts but drops 1.87% from image captions) give actionable guidance for future architecture design.

- **OmniInstruct curation pipeline is transparent and aligned with the benchmark's challenge**: Section 3.3 describes a principled pipeline for filtering 93K triples from MSRVTT-QA, AVQA, and Music-AVQA2.0 using InternVL-2-76B to remove questions answerable from a single modality, providing a concrete resource for future OLM training.

## Weaknesses

### Fatal

None.

### Major

- **OmniInstruct is presented as part of the solution but is never experimentally validated**. The abstract states that OmniInstruct is curated *"to address this gap"* (i.e., poor tri-modal performance), and Section 3.3 opens with *"To improve the model capability of tri-modal reasoning, we develop the OmniInstruct dataset."* Yet no model is ever fine-tuned on OmniInstruct and evaluated on OmniBench (or any other benchmark) to demonstrate that the dataset actually improves tri-modal reasoning. The paper structurally presents two joint contributions—a benchmark and a training dataset—but validates only one. This overclaiming is significant: the dataset's effectiveness remains entirely unknown, and the framing in the abstract is misleading. The paper would be stronger as a pure benchmark paper or would need to include even a small-scale fine-tuning experiment.

- **Several subcategories have sample sizes too small to support the fine-grained conclusions drawn**. Count & Quantity (15 samples), Text & Symbols (25), and Identity & Relationship (32) each have tiny sample sizes. The paper states *"most of the models perform really bad on quantity & counting tasks"* (line 292) and draws per-category conclusions from these subgroups (Tables 2, 5, 6). With 15 samples, a difference of even two correct answers swings accuracy by ~13 percentage points, and no confidence intervals or uncertainty estimates are provided. The overall benchmark (1,142 samples) is fine, but the per-category claims carry little statistical weight and the paper does not acknowledge this limitation.

- **The evaluation conflates instruction-following ability with tri-modal reasoning**. The paper reports accuracy as the proportion of correct answer letters matched. Several models (AnyGPT at 18.04%, Mu-LLaMA at 1.58%) perform at or below random chance (25%). The abstract attributes this to *"critical limitations in instruction-following and reasoning capabilities within tri-modal contexts,"* but this conflates two distinct failure modes: (a) failure to understand the multiple-choice format (producing invalid output, refusing, or extracting the wrong letter), and (b) genuine failure to reason across modalities. Without reporting response validity rates (e.g., what proportion of outputs were parseable answer letters), the numbers for the weakest models could reflect format incompatibility rather than reasoning deficits. This reduces interpretability, particularly for the very low-scoring models.

- **Asymmetric textual approximations bias cross-group comparisons**. When evaluating VLMs, audio is replaced by human-annotated transcripts (high fidelity, low information loss). When evaluating ALMs, images are replaced by VLM-generated captions (likely lossy—details, spatial relationships, and visual nuances may be discarded). The paper acknowledges this asymmetry in passing (line 388: *"potential noise in the generated image captions compared to the human-written audio transcripts"*) but still draws strong conclusions like *"it seems to be easier for the researchers to train the future omni-language models from existing VLMs rather than ALMs"* (line 393). This conclusion does not follow from the experimental design, since the comparison is confounded by asymmetric information loss. A human evaluation of caption quality, or a symmetric design using human annotations for both, would be needed to ground this claim.

### Minor

- **No human performance baseline is reported**. For a benchmark that aims to measure alignment with human-level understanding, providing human accuracy (even as an upper-bound estimate from the annotators) would give crucial context for interpreting model scores. The paper's findings (e.g., "below 50%") are hard to calibrate without knowing how well humans perform on the same questions.

- **The MCQ prompt format is not specified**. The paper does not describe how the question and options were formatted for each model (e.g., "Choose the correct option: A. ... B. ... C. ... D. ..."). Prompt format can substantially affect performance in LLMs, and this omission hinders reproducibility.

- **No quality analysis is provided for OmniInstruct**. Beyond the filtering statistics (93K samples after filtering), there is no human evaluation of the resulting training data—e.g., what proportion of samples genuinely require all three modalities, how many contain errors, or how diverse the data is. This makes it difficult to assess the dataset's value as a resource, even if one accepts it as a future contribution.

- **The model inspection step uses LLaVA-1.6-34B, a VLM, to verify that samples require all three modalities**. Its failure on single-modality ablation does not guarantee that *no* model could answer with one modality; a different VLM or an OLM might succeed. The human inspection partially alleviates this, but the criteria for human judgment of "both modalities required" are not described in detail.

- **The conclusion does not discuss limitations of the benchmark**. A responsible benchmark paper should explicitly acknowledge known limitations (small subcategories, the asymmetry issue, the unvalidated dataset contribution). This is absent.

### Trivial

- Line 291 contains a typo: *"context/environment entities other than object entities"* seems to miss a comparative word.
- Line 218: *"on speech and music"* should likely be *"on speech and sound events"* to match the table categories.
- Line 201 has a footnote marker placement issue.

## Nice-to-Haves

- A deeper analysis of why UnifiedIO-2's performance does not consistently scale with model size (noted at line 216 but not explored) would strengthen the paper's analytical depth.
- A manual check of a random subset of OmniBench samples to verify that they genuinely require all three modalities (beyond the automatic pipeline) would further strengthen confidence in the benchmark's core design.
- A breakdown of which models refused or produced unparseable outputs, to better separate instruction-following failures from reasoning ones.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- The claim that the abstract's "most baselines... below 50%" is a minor overstatement because InternVL-2-40B reaches 54.29%. This is an overly nitpicky reading: "most" allows exceptions, and 54.29% is still poor. Removed as noise.
- Suggestion that the Related Work section could be condensed. This is a formatting/style nitpick. Removed.
- Comments about details being "relegated to appendix" (e.g., the filtering prompt, baseline details). By the rules of this review, appendix content is known to exist in the original submission; the parser strips it. Removed.
- Criticism about the paper not exploring why UnifiedIO-2 scaling is inconsistent. This is a nice-to-have, not a weakness. Moved to Nice-to-Haves.
- Claim about "minor overstatement" regarding InternVL-40B. Removed as overly nitpicky — "most baselines perform poorly" is factually accurate.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Validate OmniInstruct experimentally**: Fine-tune at least one open-source OLM (e.g., MIO-Instruct or UnifiedIO-2) on OmniInstruct and evaluate on OmniBench. Even a small-scale experiment demonstrating improvement would substantiate the dataset's claimed role as part of the solution. If this is not feasible, rephrase the abstract and introduction to clearly frame OmniInstruct as a future resource rather than a validated contribution.

2. **Address subcategory reliability**: Either aggregate the smallest categories (Count & Quantity, Text & Symbols, Identity & Relationship) into larger groups, or report accuracy with Wilson confidence intervals and explicitly caveat per-category conclusions for categories with <50 samples.

3. **Report response validity rates**: Add a column or table showing the proportion of each model's outputs that were parseable MCQ answers (i.e., valid A/B/C/D). This would disentangle instruction-following failures from genuine reasoning failures, especially for low-scoring models like AnyGPT and Mu-LLaMA.

4. **Symmetric textual approximations or explicit caveats**: Either conduct a human evaluation comparing image captions vs. original images to quantify information loss, or restructure the VLM vs. ALM comparison to acknowledge that the observed gap could be driven by asymmetry in approximation quality rather than inherent modality advantage.

5. **Add a human baseline**: Report accuracy of human annotators on a subset of OmniBench to calibrate the difficulty and provide context for model scores.

6. **Specify prompt format**: Document the exact prompt template used for each model family to ensure reproducibility.
