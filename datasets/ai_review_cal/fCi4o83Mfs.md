- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 8, 6
Now I have a solid understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces TVBENCH, a benchmark for visual temporal reasoning in multimodal foundation models (MFMs). The authors propose three diagnostic principles (Multi-Frame Gain, Frame Order Sensitivity, Frame Information Disparity) to assess whether a benchmark truly requires temporal reasoning or can be solved with static shortcuts. They apply these metrics to four existing benchmarks and show they have low temporal demands, then introduce TVBENCH (1,484 questions, 1,417 videos, six tasks) designed to satisfy all three principles. A 29-model evaluation reveals best model accuracy at 37.9% (Qwen2-VL-72B) versus 95.2% human accuracy, with deeper analysis showing models fail to interpret frames as continuous sequences.

## Strengths

1. **Three principled diagnostic metrics with clear empirical support.** The paper defines Multi-Frame Gain (κ), Frame Order Sensitivity (τ), and Frame Information Disparity (ρ) in Section 3 and applies them in Section 5. The quantitative contrast is stark: existing benchmarks show κ < 5% and τ < 8% while TVBENCH achieves κ up to 66.3% and τ up to 34.1% (Tables 1–4). These numbers provide concrete evidence that prior benchmarks can be solved with single or shuffled frames, whereas TVBENCH genuinely requires multi-frame temporal reasoning.

2. **Thoughtful benchmark design that directly addresses identified shortcomings.** TVBENCH covers six temporal reasoning tasks across three video sources (YouTube, existing datasets, self-recorded/generated) with specific design choices — counterfactual edits (reversing, mirroring, speed changes) to defeat commonsense shortcuts (§4.2), and questions that require reasoning about transitions between all frames (§4.3). The 805 self-created videos with both human-centric and simulated scenarios fill a genuine gap in existing datasets.

3. **Comprehensive model evaluation (29 models) revealing a large and informative human-model gap.** Table 5 reports per-task accuracy for 20 open-source and 9 proprietary models. The best model achieves only 37.9%, against human performance of 95.2% (full video) and 79.7% (16 frames). This multi-faceted evaluation — including per-task breakdowns (§6.2), frame-count analysis (Figure 2a), and simulated vs. real-human video comparisons (Figure 2b) — provides rich evidence about where and how models fail.

## Weaknesses

### Fatal
None.

### Major

1. **Diagnostic benchmark comparison relies on only 2 models with no uncertainty quantification.** The comparison of κ, τ, and ρ across benchmarks (§5) uses only GPT-4o and Qwen2-VL-72B on ~200 sampled questions per benchmark, with no confidence intervals or model-diversity analysis. The paper acknowledges this implicitly ("using two state-of-the-art MFMs") but does not discuss sensitivity. While the reported gaps are large (e.g., 66.3% vs. <5% for κ), the metrics are model-dependent by definition — a model with weaker static-image understanding but stronger temporal processing could yield different relative rankings. The central claim that "existing benchmarks overestimate temporal reasoning" rests partly on these comparisons, and stronger evidence (more models, uncertainty bounds) would substantially increase confidence.

2. **Questions inherited from TGIF-QA and Perception Test may retain shortcut vulnerabilities.** For TGIF-QA and Perception Test (§4.3), the paper states: "we retained their existing questions but generate additional numerical answer options close to the groundtruth." If the original questions suffered from the same single-frame or out-of-order solvability identified in Section 5, adding distractor options does not fix the underlying shortcut — models might still answer correctly using a single informative frame. The paper does not analyze whether these specific retained questions satisfy the three diagnostic principles independently. Given that TVBENCH as a whole achieves strong κ and τ values, these questions likely constitute a small fraction, but the issue warrants explicit discussion and ideally per-question-source diagnostic breakdown.

### Minor

3. **Headline 57.3% gap compares human full-video performance to model 16-frame performance.** The abstract and Section 6.2 report a 57.3% gap (95.2% human full-video − 37.9% best model). The fairer comparison is Human (16 frames) at 79.7%, yielding a 41.8% gap — still large but meaningfully different. The paper does report both human conditions (full video and 16 frames) transparently (Table 5, line 30), so this is a presentation issue rather than a hidden flaw, but the prominence of the 57.3% figure in the abstract may mislead readers about the gap under matched conditions.

4. **"8-frame plateau" claim rests on only 4 unnamed models.** The analysis in Section 6.3 (Figure 2a) states "We assess four MFMs' performance across different number of frames" without specifying which four models were used, reporting only aggregate trajectories. Individual model trajectories are not shown, and no statistical test checks whether the 8-to-16-frame difference is significant. While this finding is presented as a secondary observation rather than a core claim, the generality of the conclusion ("models plateau after 8 frames") would be strengthened by naming the models, showing per-model plots, and testing across a broader set.

5. **Error analysis is qualitative/anecedotal rather than systematically categorized.** Section 6.3 identifies three failure modes (not interpreting frames as a continuous sequence, over-reliance on common sense, susceptibility to noise) with illustrative examples from appendices I–N. However, the paper provides no distributional analysis — e.g., what fraction of all 29 models' errors fall into each category. The current analysis is useful for insight but not for quantifying prevalence.

6. **The M-RoPE hypothesis lacks controlled ablation.** The paper suggests (§6.3) that Qwen2-VL's success "suggests that explicitly incorporating temporal-aware positional encoding like M-RoPE is likely essential." This speculation is acknowledged with hedging language ("suggests," "likely") but is not supported by controlled ablation (e.g., comparing Qwen2-VL with and without M-RoPE, or testing a non-M-RoPE model retrofitted with a temporal encoding). This should be presented more clearly as a hypothesis for future work rather than a conclusion from the data.

### Trivial
- The abstract's description of the gap could more precisely state the comparison conditions (full video human vs. 16-frame model).
- The four models used in the frame-count analysis should be named in the main text.

## Nice-to-Haves
- Run the diagnostic metric comparisons (§5) with 5–6 strong models and report mean/std across models to convert suggestive numbers into robust evidence.
- Provide confidence intervals for key accuracy figures (model performances, κ/τ/ρ values, human performance).
- Report inter-annotator agreement on the handpicked frame selection task used in computing ρ.
- Categorize failure modes systematically across all model outputs (or a representative subset) to quantify the prevalence of each of the three identified limitations.

## Removed Points

- **Human evaluation lacking sample size and inter-annotator agreement.** The paper references §G.1 (Table 10 for annotator biographies) and describes a three-stage quality check process. These details are in the appendix, which the parser stripped; they exist in the original submission. Removed per the rule that missing appendix content is not a valid criticism.

- **Missing statistical rigor throughout (confidence intervals).** While this would strengthen the paper, reporting point estimates without confidence intervals is standard practice in large-scale benchmark evaluations. The criticism is generic and does not identify a specific error.

- **Ethical/licensing details missing from main text.** The paper states license information is detailed in §F (appendix). Removed per the appendix rule.

- **Reproducibility concerns about model configurations in appendix.** The paper explicitly references "See Table 8 for detailed model configurations" in the main text (line 170). Appendix-deferred experimental details are standard.

- **Claims about "existing benchmarks overestimate" being asymmetrically tested (only 4 benchmarks).** The paper clearly scopes its analysis to "four existing widely-used temporal reasoning video benchmarks" and does not claim exhaustiveness. This is a scope-defined claim, not an omission.

- **M-RoPE discussion labeled as fatal/structural flaw.** The original review correctly noted this is speculation but the paper uses appropriately hedged language ("suggests," "likely"). Demoted from concern to nice-to-have.

## Novel Insights

The review surfaces a productive tension that the paper itself does not fully resolve: the diagnostic metrics (κ, τ, ρ) are intended as *intrinsic* benchmark properties, but they are operationalized through *model-dependent* measurements. This is not fatal — a benchmark-level property can be reliably estimated via sufficient model sampling — but the paper's current evidence (2 models) is the bare minimum. A genuinely novel direction the reviews hint at but do not develop: the fact that models plateau at 8 frames and yet human accuracy continues to rise suggests that the bottleneck is not frame count but a qualitative architectural limitation in how frames are integrated. The M-RoPE hypothesis from the paper is a plausible explanation, but the reviews correctly note the lack of ablation. None of this invalidates the core contribution — TVBENCH itself is a solid, well-motivated benchmark — but the paper's secondary claims about *why* models fail would benefit from more rigorous treatment.

## Suggestions

1. For the diagnostic comparison (§5), run κ, τ, and ρ with at least 5 models spanning different architectures and training paradigms, and report mean ± std across models. The large observed differences (66.3% vs. <5% for κ) are likely robust, but this would convert suggestive evidence into definitive evidence.

2. Report per-question-source diagnostic metrics (κ, τ, ρ) separately for the three video sources (YouTube, existing datasets, self-recorded), especially to verify that retained questions from TGIF-QA and Perception Test do not dilute the benchmark's temporal demands.

3. Name the four models used in the frame-count analysis (Figure 2a) and show individual per-model trajectories alongside the aggregate. Add a brief discussion of whether the plateau is consistent across all four models or driven by a subset.

4. Add a systematic error categorization: sample 50–100 errors across models and code them into the three failure types identified in §6.3, reporting the distribution. This would elevate the error analysis from anecdotal to quantitative.
