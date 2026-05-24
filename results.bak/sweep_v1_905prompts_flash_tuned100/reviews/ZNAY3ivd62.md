Now I have all the data I need. Let me produce the final review.

## Summary

GUI-Spotlight proposes a multi-tool iterative refinement framework for GUI visual grounding, where a 7B MLLM learns to dynamically invoke *crop*, *extract*, and *find_color* tools to progressively narrow its focus to a target element. The model is trained in three stages (SFT warm-up, RL with a modified GSPO objective, and high-resolution refinement) using only 18.5K curated samples. On ScreenSpot-Pro it achieves 52.8% accuracy — the best among 7B models, surpassing V2P-7B (50.6% with 9.6M samples) — and shows improvements on UI-Vision. The data efficiency claim is genuinely striking, and the stabilized multi-turn RL training (tool-filtered cross-entropy loss) is a practical contribution.

## Strengths

1. **Impressive data efficiency.** GUI-Spotlight achieves 52.8% on ScreenSpot-Pro with 18.5K training samples, surpassing V2P-7B (50.6% with 9.6M), GTA-1-7B (50.1% with 1.56M), and UI-Venus-7B (50.8% with 107K). The >50× reduction in training data while exceeding competitor accuracy is clearly presented in Table 3 and is a genuine, well-documented advance.

2. **State-of-the-art among 7B models on ScreenSpot-Pro.** GUI-Spotlight (UI-TARS-1.5-7B backbone) tops the 7B leaderboard at 52.8%, and the per-domain breakdown in Table 3 shows improvements over the base model across all six domains. The variant starting from generic Qwen2.5-VL-7B gains +11.9 absolute points (26.8% → 38.7%), showing transfer beyond UI-specialized backbones.

3. **Stabilized multi-turn RL training.** The modified GSPO with tool-filtered cross-entropy loss (Eq. 2, auxiliary term 𝒥'(θ)) demonstrably prevents the oscillation and collapse that affect vanilla GRPO and GSPO. Figure 3 (right panel) shows GUI-Spotlight maintaining ~0.9 correct-answer reward after 400 steps, while baselines drop to ~0.3. This is a concrete algorithmic contribution.

4. **Comprehensive ablation and documentation of negative results.** Sections 4.1–4.2 systematically compare seven RL variants and multiple reward formulations, reporting both what works and what does not (e.g., "continuously updating the reference policy degrades accuracy"). This provides practical guidance and increases confidence in the design choices.

## Weaknesses

### Fatal
None.

### Major

1. **SFT warm-up causes a dramatic accuracy collapse without adequate analysis or justification.** After Stage-1 SFT on 2561 Qwen2.5-VL-72B trajectories, the model's ScreenSpot-Pro accuracy drops from 39.3% to 17.8% — a 55% relative decline (Figure 2). The paper describes this as "learning to invoke multiple tools but remaining under-aligned," which describes the symptom but does not explain why grounding ability is so severely degraded. No analysis of trajectory quality is provided, and no ablation shows whether SFT is necessary (e.g., can RL be applied directly to the base model?). The recovery to 49.6% in Stage 2 suggests RL is largely correcting damage from SFT rather than building on a useful initialization. The authors should explain why this drop is expected and harmless, or restructure training to avoid it.

2. **The gain over a simple training-free iterative baseline is modest, and the incremental contribution of multi-tool RL is not cleanly isolated.** Section 5.4 shows that a training-free repeated single-turn baseline achieves 47.6% on ScreenSpot-Pro, while GUI-Spotlight achieves 52.8% — a 5.2pp gap. The paper attributes this to the learned tool-use policy, but most of the improvement could come from the iterative cropping process itself (which both methods share). Training an RL baseline that directly outputs coordinates (no tool calls) on the same data and comparing to GUI-Spotlight would clarify whether the multi-tool policy is the source of the gain or merely a more complex way to achieve similar results.

3. **OSWorld-G results show minimal or negative gains, weakening generality claims.** On OSWorld-G (Table 5), GUI-Spotlight (UI-TARS backbone) goes from 61.9% (base) to 62.7% — only +0.8pp. Element Recognition actually decreases from 64.5% to 60.6%, and Fine-grained Manipulation improves only marginally (42.9% → 45.6%). Since the paper claims "substantially outperforming comparable 7B baselines" and the method is motivated as general-purpose, these near-zero gains on a general OS-level benchmark are a significant limitation that deserves discussion.

### Minor

1. **No statistical significance or variance reported.** All results are single runs. Given RL training noise and the 2.2pp margin over V2P-7B (50.6% vs. 52.8%), it is impossible to assess whether improvements are reliable. Multiple seeds with error bars would substantially strengthen the empirical claims.

2. **Potential circularity from using Qwen2.5-VL-72B for both trajectory generation and data filtering.** The same model family (72B variant) generates the 2561 SFT trajectories and also evaluates instruction quality and bounding box accuracy during data cleaning. This could bias the filtered data toward examples Qwen2.5-VL finds easy. The paper does not discuss this dependency.

3. **The crop window size *w* in *find_color* is not specified.** Table 1 describes "*find_color*: ... center a *w* × *w* window" but *w* is never defined. This is a minor specification gap.

4. **Data flow from 15K raw → 11.6K cleaned → 4K in Stage 3 is not fully explained.** The paper collects 15K high-res samples, the cleaning pipeline yields 11.6K refined samples, but only 4K are used in Stage 3. Clarification of what happened to the remaining 7.6K would help.

### Trivial
None.

## Nice-to-Haves
- Ablation applying RL directly to the base model (skipping Stage-1 SFT) to test whether SFT is strictly necessary.
- A study of which tools contribute most (e.g., ablating *find_color* or *extract* from the tool set).
- Reporting multiple seeds / confidence intervals for main results.

## Removed Points

These points from the reviewers were removed with justification:

- **"The RL contribution cannot be independently verified"** — Removed per hard rule: questioning existence of cited models and tools.
- **Generic strengths from Strength Finder** (e.g., "this paper addressed an important problem") — Removed as generic/superficial; only evidence-grounded strengths retained.
- **"The leaderboard may report different numbers for the base model"** — Removed as speculative; the paper reports its own evaluation using official GitHub instructions.
- **"Figure 3 (left) is hard to parse"** — Removed as a presentation nitpick; the figure is clearly annotated with numbered variants ①–⑦.
- **Formatting/typo concerns** — Removed per hard rule: these are parser artifacts, not author errors.

## Novel Insights

The main insight that emerges from synthesizing the two reviews is that GUI-Spotlight achieves genuinely impressive data efficiency — but the evidence for *why* it works is weaker than the headline numbers suggest. The SFT collapse (39.3% → 17.8%) and subsequent recovery (→ 49.6% after RL) together suggest the three-stage pipeline may be working less elegantly than presented: SFT teaches tool syntax while degrading grounding semantics, and RL primarily teaches the model to recover its grounding ability while exploiting the new tool interface. The near-zero gain on OSWorld-G further suggests the approach benefits disproportionately from the iterative cropping mechanism (already available without training) rather than from the learned tool-coordination policy itself. The data efficiency, however, is real and significant regardless of the mechanism.

## Suggestions

1. **Diagnose the SFT collapse.** Run an ablation that starts RL directly from the base model (skip Stage 1). If final accuracy is similar, the SFT stage can be removed or simplified. If the collapse is unavoidable, provide a clearer explanation (e.g., forward/backward transfer dynamics) and frame the pipeline accordingly.

2. **Isolate the tool-use contribution.** Train an RL baseline that outputs only direct coordinates (no tool calls) on the same data. This would show whether the multi-tool policy drives the 5.2pp gain over iterative cropping, or merely adds complexity.

3. **Add multiple seeds** for the main ScreenSpot-Pro result and report mean ± std, especially given the small 2.2pp margin to the second-best 7B model.

4. **Restructure the OSWorld-G framing.** Present these results as evidence that the approach transfers better to UI-focused benchmarks (ScreenSpot-Pro, UI-Vision) than to general OS-level tasks — which is itself an informative finding — rather than claiming generality.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>