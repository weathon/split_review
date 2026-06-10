## Summary

This paper proposes Vision-Language Bootstrapping (VLB), a dynamic multimodal evaluation framework that transforms static benchmark samples by bootstrapping both images (adding/removing objects, expanding scenes) and language (word substitution, rephrasing, adding context) while preserving answer correctness via a judge module. By composing strategies, VLB produces variants with controllable difficulty and claims reduced data contamination. Experiments across 11 LVLMs and multiple benchmarks show consistent difficulty modulation (e.g., harder variants drop GPT-4o by 6.68% on SEEDBench; composition produces up to 41-point gaps).

## Strengths

- **First framework to bootstrap visual content in dynamic evaluation.** Prior dynamic evaluation methods (DyVal, NPHardEval, MPA) operate only on NLP tasks. VLB introduces three image-bootstrapping strategies that alter visual content while preserving answer correctness — a genuine capability gap that this paper fills (Section 2).

- **Demonstrated controllable complexity via compositional bootstrapping.** Table 6 shows across MMBench_DEV_Full, MMvet, and LLaVABench that the hardest composition (V1+L4) consistently degrades performance and the easiest (V2+L3) boosts it, for all 7 evaluated models. For example, on MMvet, DeepSeek-VL scores 22.88% (hard) vs. 64.03% (easy) vs. 41.88% (vanilla) — providing a meaningful performance gradient rather than a single transformed version.

- **Comprehensive evaluation across diverse models and tasks.** The paper evaluates 11 LVLMs (closed- and open-source) across three benchmark formats (Yes/No, MCQ, VQA), with consistent directional effects, strengthening generality beyond any single model family.

- **Well-motivated strategy design.** The image/language bootstrapping strategies are grounded in concrete user-interaction scenarios (different visual attention, varying linguistic expression), which makes the difficulty manipulation interpretable rather than ad-hoc.

## Weaknesses

### Fatal
None.

### Major

- **Contamination analysis conflates semantic similarity with data leakage, weakening the motivational foundation.** The paper's Figure 1 claims images "can be exactly found in the training set," but the detection method uses a CLIPScore threshold of 0.9 that measures *semantic similarity*, not exact or near-duplicate matching. Two distinct photos of a kitchen can score >0.9 without sharing pixels. The 84.46% "contamination" rate is therefore methodologically uninterpretable as evidence of training-data overlap. The image-text contamination detection (GPT-4 judging whether answers can be "directly inferred" from training captions) is similarly unvalidated — no precision/recall figures are reported. This weakens one of the paper's two motivating pillars (data contamination). *Quoting the paper*: the method (line 94) uses CLIPScore for "high visual similarity" while the caption (line 31) asserts "exactly found" — this is a genuine inconsistency.

- **The claim that VLB reduces data contamination is not convincingly demonstrated.** The empirical evidence (Figure "data_after") re-applies the same CLIPScore methodology to dynamic variants and finds reduction. This is nearly tautological: editing an image that scored >0.9 with a training image will naturally reduce its CLIPScore to that same training image. The paper does not test whether generated images match *other* training images through different pathways (since PowerPaint and GPT-4V are trained on large datasets themselves). The paper's two stated mechanisms for contamination reduction (random process, dissimilarity from original) are plausibly correct but the evidence provided does not cleanly separate true contamination reduction from the methodological artifact of measuring similarity to the *same* training image.

- **No statistical uncertainty quantification anywhere.** All results are point estimates with no confidence intervals, standard deviations, or significance tests. With subsampled test sets (10% of SEEDBench, 30% of MMBench for main experiments), many reported deltas — especially the sub-1% changes in language bootstrapping (Table 2) — could lie within noise. The paper's central claim about ranking compositions as "hardest" vs. "easiest" depends on these differences, and the reader cannot assess whether they are meaningful.

- **"Co-evolve" framing overstates what is demonstrated.** The abstract and introduction claim VLB "enables the evaluation to co-evolve with the ever-evolving capabilities of LVLMs." What is shown is one round of transformations producing variants with different difficulty levels. There is no demonstration of an iterative process where VLB generates *new, previously unseen* variants as models improve. The contribution is one-shot difficulty scaling, not a truly adaptive or co-evolving benchmark.

### Minor

- **InternVL-2 serves as both the judge module and one of the evaluated models.** If the judge systematically over-approves outputs for easier strategies or over-rejects harder ones, the observed performance gaps could partly reflect judge bias. The proportion of samples that fail the judge five times and revert to original (line 166) is not reported — if this varies by strategy, it could dilute the intended difficulty manipulation. *(The paper references human verification in an appendix section that was stripped by the parser; per review guidelines, this is not penalized as missing.)*

- **Image bootstrapping quality and failure modes are not analyzed.** The V1 and V3 strategies depend on GPT-4V for object selection and PowerPaint for image editing. Failures in these components could produce unrealistic images that test artifact recognition rather than the intended capability. No analysis of generation quality, failure modes, or success rates is provided.

- **Claude model name inconsistency.** The introduction (line 46) names "Claude3-Sonet" while Table 4 (line 344) uses "Claude3-5V-Sonnet." This suggests carelessness in reporting.

### Trivial
None.

## Nice-to-Haves

- Adding a simple perturbation baseline (e.g., random crops + color jitter for images, random synonym replacement for questions) would strengthen the argument that VLB's strategies capture meaningful, user-grounded complexity rather than any arbitrary transformation.
- Reporting judge agreement rates per strategy (with humans or cross-validation) would strengthen confidence in the overall pipeline.

## Removed Points

The following points from the inputs were removed with justification:

- **"Output contamination" concern (harsh critic point 3, last paragraph)**: The critic argued that since answers remain the same, models could still benefit from answer memorization. This misunderstands the setting — if both image *and* question change, the (I,Q) → A mapping that memorization would rely on is broken. Removed as a misunderstanding.

- **Judge validation being "underspecified in main text"**: The paper explicitly references human verification in an appendix section (sec:exp_human_verification). Per guidelines, sections stripped by the parser cannot be penalized as missing.

- **Strength Finder claim about contamination analysis being a core strength**: This directly conflicts with a verified weakness (methodology conflates similarity with contamination). Per rules, when a strength and verified weakness disagree, the weakness wins. Removed.

- **Generic/superficial strengths from Strength Finder**: Claims that the paper "addressed an important problem" or that contamination analysis is "clear and data-driven" are too generic or conflict with verified weaknesses. Removed.

## Novel Insights

The most striking finding not fully foregrounded by the paper is the *asymmetry* in how language strategies affect different models: L4 (adding irrelevant context) is devastating for some models (Qwen-VL-Chat drops 35.08% on MME under L1, 20.18% under L4) while barely affecting others (GPT-4o drops 1.34% under L1). This suggests that sensitivity to linguistic distraction varies dramatically across model architectures/families — a finding that merits deeper investigation beyond the paper's current scope. The paper notes "longer text poses a greater influence" but does not explore why some models are 10-20x more affected than others by the same linguistic perturbation.

## Suggestions

1. **Replace or substantially caveat the CLIPScore-based contamination analysis.** At minimum: report exact-image matching via perceptual hashing alongside CLIPScore, clarify that CLIPScore measures similarity not duplication, and acknowledge that the 84.46% figure is an upper bound on semantic similarity, not confirmed training-data overlap.

2. **Add confidence intervals or bootstrap variance estimates** to the main results (Tables 1–3). Given the subsampled test sets, this is essential for readers to assess whether observed differences (especially the sub-1% deltas) are meaningful.

3. **Tone down the "co-evolve" framing** to match what is demonstrated: one-shot difficulty scaling from static benchmarks, not iterative adaptation.

4. **Report the judge's fallback rate** (proportion of samples using original after 5 failed attempts) and whether it varies by strategy difficulty.

5. **Fix the Claude model name** for consistency.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>