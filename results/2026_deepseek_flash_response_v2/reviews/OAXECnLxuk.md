## Summary

DaVinci introduces a two-stage framework (SFT + RL) for parsing raster scientific diagrams into TikZ code. It contributes the TiKZ30K dataset with code reordering and comment injection, and a hybrid reward function that uses PDF vectorization to avoid OCR errors. Built on Qwen2.5-VL-7B, DaVinci achieves 97.60% Pass@1 compile rate on DATiKZv3, substantially outperforming GPT-5 and Claude-Sonnet-4 while being competitive with much larger models including Gemini-2.5-Pro-Thinking.

## Strengths

- **Near-perfect compile rate (97.60%)**: DaVinci-7B dramatically outperforms all competitors on Pass@1 (next best: Claude-Sonnet-4-Thinking at 86.90%). Remaining failures are traced to a specific cause (context-length overflow on dense scatter plots), lending credibility.

- **Data strategies — code reordering and comment injection — cleanly ablated**: Table 4 shows reordering alone improves Pass@1 by +9.04%, and comments add another +5.72%. Each contribution is isolated and causally demonstrated with a clear experimental design.

- **Hybrid reward function using PDF vectorization**: Extracting text and geometry primitives from PDF vector data rather than OCR is well-motivated and genuinely avoids a class of errors. The ablation (Table 5) shows progressive improvements across SSIM, MSE, LPIPS when adding R_text and R_geom.

- **Honest analysis of results**: Section 4.3 explicitly notes that cBLEU decreases after RL while visual metrics improve — correctly concluding that strict code similarity is not the right objective. The paper also acknowledges Gemini-2.5-Pro's superior performance on several image metrics.

- **Temporal contamination control**: Training data restricted to pre-December 2023 sources, ensuring separation from the DATiKZ_og test set (January 2024+).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **"Error-free" claim is overstated**: The paper repeatedly claims PDF extraction is "error-free" (lines 34, 40, 52, 122). PDF text extraction via libraries like PyMuPDF can fail on text encoded as font paths, ligatures, composite glyphs, and encoding mismatches. The approach genuinely avoids OCR errors — a real improvement — but calling it "error-free" invites justified skepticism. Should be qualified as "avoids visual-recognition-based extraction errors."

2. **Reward ablation partially evaluates against metrics sharing machinery with the rewards**: The "Texual" and "Geometry" columns in Table 5 appear to use procedures that mirror R_text and R_geom (bipartite matching, same cost functions, same normalization). Improvement on these metrics is partly expected because the model optimizes for them during training. The table also reports independent image metrics (SSIM: 73.07→74.01, MSE: 64.58→62.30, LPIPS: 22.94→22.32) that genuinely improve — the paper should refocus the ablation on these independent signals.

3. **Abstract framing is selectively favorable**: The abstract claims DaVinci "surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4." While factually correct for those two models, the paper also evaluates Gemini-2.5-Pro-Thinking, which outperforms DaVinci on DreamSim (88.20 vs. 84.83), SigLIP, SSIM, and LPIPS, and dominates in human evaluation (μ=0.50 vs. DaVinci's -0.01). The paper's body acknowledges this honestly, but the abstract/conclusion present a selective picture that could mislead a casual reader.

4. **No statistical uncertainty for key metrics**: The 542-sample test set lacks confidence intervals or significance tests. The human evaluation (100 items, 6 raters) also lacks formal significance testing. This makes it unclear whether some observed differences (e.g., DreamSim 84.83 vs. 83.81) are meaningful.

5. **No inference cost or runtime comparison**: Not reporting generation speed or compute requirements for DaVinci vs. proprietary API models is a practical gap for practitioners.

### Trivial
- Table 5 header has "Texual" instead of "Textual."

## Nice-to-Haves
- A taxonomized failure analysis beyond compile errors (missing elements, misaligned text, wrong colors) would strengthen the contribution.
- Clarifying whether the Qwen-2.5-VL-32B and Qwen3-Coder-480B models used for data processing could introduce systematic biases from the same model family as the base model.
- Reporting the omitted RL training details (KL penalty coefficient, learning rate, ε clipping parameter).

## Removed Points

These points were flagged by the reviewers but removed per the filtering rules:

1. **Harsh critic's "misrepresentation" claim**: Removed — the paper specifically names GPT-5 and Claude-Sonnet-4, and Table 1 confirms DaVinci outperforms both across nearly all metrics. The paper also acknowledges Gemini's superior performance in the body (Section 4.3, line 194; Section 4.4, line 218). The claim is accurate, though selectively framed.

2. **"Missing related works"**: Removed per hard rule — I cannot verify external sources.

3. **"No code/data release URL"**: Removed — the paper states code/data/models are available with licensing details (Section "Data Release and License Information"); a missing footnote URL in the extracted text is a parser artifact.

4. **"Baseline prompt engineering insufficiently described"**: Removed — the paper states standard API access with default settings was used ("GPT-5-Default (self-control the thinking efforts)").

5. **Strength Finder's generic strengths** (e.g., "addressing an important problem"): Removed as generic/superficial.

6. **Harsh critic's concern that comparison asymmetry favors baselines**: Removed per hard rule — asymmetry favoring baselines is acceptable.

## Novel Insights

The observation that strict code-level similarity (cBLEU) decreases after RL training while visual fidelity improves (Section 4.3) is an important and honestly-reported finding. It demonstrates that for diagram-to-code tasks, the reward signal should target rendered output quality rather than code surface form — a lesson with implications beyond this specific setting.

## Suggestions

1. Reframe "error-free" to "avoids visual-recognition-based extraction errors" or similar qualification throughout the paper.
2. Add bootstrap confidence intervals to the main automatic evaluation table (Table 1).
3. In the reward ablation (Table 5), present the impact on independent held-out metrics (DreamSim, SSIM, MSE, LPIPS) more prominently; consider moving the "Texual" and "Geometry" columns to supplementary material.
4. Acknowledge Gemini-2.5-Pro's stronger performance on visual fidelity metrics more prominently in the abstract, or reframe the headline as "competitive with leading proprietary models at 7B scale."
5. Add a brief discussion of inference latency and hardware requirements vs. API-based alternatives.

## Score Calibration

### Round 1 — Bracketing (broad topical search)
| Anchor | Avg Score | Comparison |
|---|---|---|
| *Sketch2Diagram* (KvaDHPhhir) | 6.25 | **DaVinci is stronger**: SFT+RL vs. just SFT; larger curated dataset; more comprehensive evaluation against proprietary models; cleaner ablations. |
| *AutomaTikZ* (v3K5TVP8kZ) | 6.50 | **DaVinci is stronger**: tackles the harder image-to-code task (vs. text-to-code); uses RL post-training (vs. LoRA SFT); more extensive evaluation with human study against frontier models. |
| *Chain-of-region* (M6fYrICcQs) | 6.00 | **DaVinci is stronger**: addresses the harder generation problem with more methodological depth (SFT+RL vs. prompting-only). |
| *Delving into LLMs with SVG* (pwlm6Po61I) | 5.67 | **DaVinci is substantially stronger**: rigorous evaluation, dataset, method vs. exploratory study. |

**Initial bracket**: 6.5–8.5

### Round 2 — Narrowing within bracket
| Anchor | Avg Score | Comparison |
|---|---|---|
| *MAPS* (GR0y0F3Ipd) | 6.50 | **DaVinci is stronger**: harder generation task, more comprehensive evaluation, larger dataset. |
| *ChartMoE* (o5TsWTUSeF) | 6.75 | **DaVinci is comparable or slightly stronger**: ChartMoE has a 1M dataset and MoE architecture innovation, but DaVinci tackles the harder open-ended generation task with SFT+RL and has more thorough data ablations. |
| *MM1.5* (HVtu26XDAA) | 7.00 | **DaVinci is slightly weaker in breadth/scope**: MM1.5 is a broader MLLM methods paper with systematic study across model scales, but DaVinci is strong for its specific task. |
| *Multi-modal Agent Tuning* (0bmGL4q7vJ) | 7.50 | **DaVinci is weaker in scope**: broader agent-tuning paper with GAIA/GTA benchmarks; different type of contribution. |

### Score Determination
DaVinci clearly exceeds the TikZ-specific anchors (6.0–6.5 range) due to its sophisticated SFT+RL pipeline, carefully curated dataset with novel reordering/comment strategies, comprehensive evaluation against 10+ baselines including frontier proprietary models, and strong results (97.60% Pass@1 is transformative). It sits at or slightly above ChartMoE (6.75). It is slightly below broad MLLM methods papers like MM1.5 (7.00) in scope breadth, but its contributions for its specific task are strong. The identified weaknesses are minor and addressable — they do not threaten the core contribution. This places the paper at **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>