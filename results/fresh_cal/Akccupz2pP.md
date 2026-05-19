Now I have thoroughly verified the paper content against all reviewer claims. Let me construct the final consolidated review.

## Summary

This paper proposes GTD-LLM, a plug-and-play LLM reasoning module for gaze target detection that can be integrated with any existing gaze target visual model without retraining. The module extracts object-level information via pre-trained detectors, uses a novel prompt engineering method (GTD-Prompt) that decomposes gaze reasoning into atomic steps (scene analysis → activity reasoning → gaze reasoning), and fuses the LLM's knowledge with the base model's heatmap output. The method is demonstrated across 5 base models, showing consistent improvements of 3%–5% recall on all COCO-category targets and 8%–71% on activity-related categories, with extensions to shared attention and mutual gaze detection.

## Strengths

- **Plug-and-play integration demonstrated across 5 base models**: The paper integrates GTD-LLM with five distinct gaze target visual models (Chong, Fang, Tu, Tonini, Yang) without any retraining and shows consistent performance improvements across all of them (Table 1, Table 2). This provides strong empirical evidence that the module is genuinely model-agnostic.

- **Large, well-documented gains on activity-related and long-tailed targets**: The method achieves 8%–71% recall improvement on activity-related categories (sports ball, cell phone, frisbee, book, kite) and 11%–28% improvement on long-tailed categories (Table 1). These results directly address a known limitation of pure-visual methods and provide quantitative evidence that LLM prior knowledge fills a genuine gap.

- **Task-flow prompt design validated via systematic ablation**: The decomposition of gaze reasoning into atomic steps (scene → activity → gaze) is ablated in Table 3, showing each step contributes positively. Similarly, both angular and distance position relationship rules are ablated in Table 4. This provides evidence that the prompt's structure matters and is not a generic LLM invocation.

- **Extension to downstream tasks**: The method adapts to shared attention detection (Table 9) and mutual gaze detection (Table 10) with minimal prompt adjustments, demonstrating versatility beyond the primary task.

## Weaknesses

### Fatal

None.

### Major

- **No uncertainty estimation for stochastic LLM outputs**: GPT-4's responses are stochastic, yet all results in Tables 1–10 are reported as single numbers with no mention of multiple runs, variance, confidence intervals, or statistical significance tests. The core evidence for the method's contribution is the observed performance improvements, but the reader cannot evaluate whether these improvements are reliably above the noise level of the LLM's stochastic behavior. This should be addressed by running multiple independent queries (≥5) and reporting mean ± std, or by running a single deterministic pass at temperature=0 and explicitly stating this protocol.

- **Threshold tuning and ablations performed on the test set**: The paper states (Section 4.4, line 239) that "We conduct a series of ablation experiments in the GazeFollow test set." The angular thresholds (α₁=15°, α₂=45°) and distance threshold (β=0.5×face width) are described as set "through experiments" but no held-out validation split is mentioned. All ablation studies (Tables 3–8) are reported on the test set. This risks over-adapting to test-set statistics and inflating apparent performance. The paper should either (a) confirm thresholds were chosen on a held-out validation set, or (b) perform the ablations on a validation split and report test-set results only for the final configuration.

### Minor

- **Incomplete reproducibility details**: The exact prompt strings (system message and user message templates) and GPT-4 API settings (model version, temperature, max tokens) are not provided. The prompt is described at a high level (task-flow instructions t₁–t₄) and shown schematically in Figure 3, but the precise formatting that determines actual LLM behavior is absent. Including these in an appendix would enable independent verification.

- **The "plug-and-play" label paper-over setup complexity**: The module requires three external pre-trained detectors (MM-GroundingDINO, OpenPose, L2cs-net), a set of hand-tuned position-relationship rules, a modal transformation step, and a fusion mechanism. While the module is genuinely model-agnostic (identical integration path for any base model), calling it "plug-and-play" understates the pipeline effort a new user must undertake. A more precise framing — such as "model-agnostic" or "training-free integration" — would better describe the contribution.

### Trivial

None that are parser-independent. The paper's writing is clear and the presentation is adequate.

## Nice-to-Haves

- Report the number of samples that survive the YOLOv10-based filtering step and whether the filtering disproportionately removes hard cases (e.g., gaze targets not corresponding to COCO objects).
- Include a simple text-only or rule-based baseline that uses the same object-level information without an LLM (e.g., "always predict the nearest activity-related object within FOV") to isolate the added value of LLM reasoning vs. the information provided by the detector pipeline.
- Show failure cases where the LLM introduces errors, to help calibrate trust in the fusion mechanism.
- Report API cost and total number of calls.

## Removed Points

- *Potential train/test contamination of GPT-4*: This is speculative — there is no evidence from the paper that GPT-4 has memorized these specific datasets, and the authors cannot control GPT-4's training data. Such speculation about any widely-used foundation model would apply to nearly every LLM-based method and is not a specific weakness of this paper. **Removed per rule:** speculative fatal claim without in-paper evidence.

- *Comparison fairness (extra info argument)*: The reviewer claims the comparison is unfair because GTD-LLM brings external information. However, the paper's claim is specifically that adding LLM reasoning to base models improves performance — the comparison is base model alone vs. base model + GTD-LLM, which is exactly the right experimental design for this claim. **Removed:** does not reflect a real problem with the paper.

- *Activity-related categories bias*: The reviewer suggests that large gains on activity-related categories may simply be "bias toward a predefined set of categories." This is the claimed mechanism — the LLM supplies prior knowledge about human–activity correlations. The gains are meaningful precisely because these categories are where pure-visual methods struggle. **Removed:** misunderstanding of the paper's claim.

- *Base model heatmap calibration*: The reviewer speculates that pixel-wise multiplication assumes the base model's heatmap is calibrated. The fusion includes normalization (`norm()`) which handles scale differences, and the ablation (Table 6) tests the bias parameter. No evidence of a calibration problem is presented. **Removed:** speculative, not demonstrated.

- *"Merge similar position relationships" vague*: The paper provides a concrete example (two objects both "close to gaze" are merged into one description) and the rule is clear from context. **Removed:** overly nitpicky.

- *Domain adaptation detector quality*: The reviewer speculates about domain shift in detectors without evidence. **Removed:** speculative.

- *Various "Strengthening the Paper" suggestions* that are suggestions rather than identified weaknesses (e.g., release exact prompts, include statistical tests). These are absorbed into Nice-to-Haves above.

## Novel Insights

The two independent reviews converge on the same core structure: the paper's contribution (using decomposed prompt engineering to inject common-sense gaze reasoning into an otherwise vision-only pipeline) is genuinely novel and the experimental sweep across 5 models and 2 downstream tasks is thorough. The weaknesses cluster around evaluation hygiene — the stochastic output of the LLM demands variance reporting that is absent, and the use of the test set for threshold development and ablations is a methodological gap. No deeper insight emerges beyond what the paper already states and what the reviews separately identify.

## Suggestions

1. **Report variance**: Run each experiment at least 5 times (or state a deterministic temperature=0 protocol) and report mean ± std or confidence intervals for all main results.

2. **Hold out a validation set**: Either confirm that thresholds were chosen on a validation split, or re-run the ablations on a held-out set and report only final results on the test set.

3. **Provide exact prompts and API settings in an appendix**: Include the full system message, user message template, model version string, temperature, max tokens, and any other parameters.

4. **Tone down or clarify the "plug-and-play" framing**: The module is best described as "training-free integration" or "model-agnostic" — it adds a pipeline of detectors and rules, which is more than "plug-and-play" conventionally implies.

## Score and Decision

**Originality**: Good — first LLM reasoning module for gaze target detection; the prompt decomposition (scene→activity→gaze) is novel and well-motivated.  
**Importance of research question**: High — gaze target detection is an established problem, and incorporating common-sense prior knowledge addresses a recognized limitation of vision-only methods.  
**Claims supported**: Mostly well-supported, with gaps in uncertainty quantification and validation hygiene preventing full confidence.  
**Soundness of experiments**: Broad sweep across models, datasets, and tasks is a strength; lack of variance reporting and test-set threshold tuning are weaknesses.  
**Clarity of writing**: Clear; the method is described logically and the prompt design is well-explained.  
**Value to community**: Good — the model-agnostic nature and extension to downstream tasks make this useful for future work in gaze analysis and human attention understanding.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>