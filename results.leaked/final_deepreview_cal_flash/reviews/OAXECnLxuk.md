## Summary

This paper introduces DaVinci, a multimodal LLM for parsing rasterized scientific diagrams into structured TikZ code. The method uses a two-stage pipeline: supervised fine-tuning on a curated dataset (TikZ30K) with code reordering and comment injection, followed by reinforcement learning (GRPO) guided by a hybrid reward function that combines code pass rate, image fidelity, and vectorized textual/geometric similarity. Experiments on the DATiKZv3 benchmark show that DaVinci-7B achieves a 97.60% compile rate, outperforming GPT-5, Claude-Sonnet-4, and all open-source baselines, while trailing Gemini-2.5-Pro on several image-quality metrics and human evaluation.

## Strengths

**1. Carefully constructed dataset with demonstrably effective augmentations.** TikZ30K introduces two well-motivated innovations — code reordering and comment injection as planning scaffolds — that go beyond simply scaling data. Table 4 cleanly isolates each component's impact: reordering improves Pass@1 from 69.74% to 78.78%, and comments add another 5.72% to reach 84.50%. The temporal separation (data cut-off Dec 2023 from the test set) and the licensing-aware release strategy (diff files for non-redistributable sources) are rigorous practices that strengthen experimental credibility.

**2. Strong empirical results across code-level and image-level metrics.** DaVinci-7B achieves the highest Pass@1 compile rate (97.60%) and best MSE (61.81) among all evaluated models, including proprietary ones. It surpasses GPT-5-Default and Claude-Sonnet-4 on every metric in Table 1 and all open-source baselines across the board. The human evaluation (Group 1, non-proprietary models) confirms a clear advantage over specialized TikZ-generation models (score 0.365 vs. -0.05 for the next best).

**3. Novel hybrid reward design using vectorized representation.** The paper's use of PDF vectorization (via PyMuPDF) to extract text and geometric primitives for reward computation is a genuine technical contribution — it avoids OCR errors that plague diagram-text extraction. The spatio-textual (R_text) and geometric (R_geom) rewards provide finer-grained structural feedback than pixel-level or perceptual losses alone. The ablation in Table 5 shows that adding these components improves not only the "Texual" and "Geometry" metrics but also independent measures like SSIM, MSE, and LPIPS.

**4. Comprehensive and contemporary evaluation.** The baseline set spans 12 models: proprietary (Gemini-2.5-Pro, GPT-5, Claude-4 variants), open-source (Qwen2.5-VL at three scales, GLM-4.5V), and specialized TikZ systems (DetikZify-V2, DiagramAgent). The human evaluation uses Best-Worst Scaling with six annotators, reports split-half reliability (0.72–0.79), and provides evidence beyond automatic metrics. The analysis of "thinking vs. non-thinking" modes and the finding that high code similarity is not necessary for good diagram parsing are insightful secondary contributions.

## Weaknesses

### Fatal
None.

### Major

**1. Selective framing underplays Gemini-2.5-Pro's superior performance.** The abstract and conclusion repeatedly state that DaVinci "surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4," but Gemini-2.5-Pro-Thinking substantially outperforms DaVinci on several automatic metrics (DreamSim 88.20 vs. 84.83, SSIM 75.86 vs. 73.65, LPIPS 21.64 vs. 22.32) and dominates the human evaluation (Group 2 score 0.50 vs. -0.01). While Section 4.3 acknowledges that "Gemini-2.5-Pro presents better performance than DaVinci-7B regarding certain metrics," this qualification is absent from the abstract and conclusion, giving an incomplete picture. A naive reader could come away believing DaVinci is broadly superior to all proprietary systems. The paper should explicitly acknowledge Gemini's performance in the abstract and conclusion and discuss where and why it excels.

**2. Reward-component ablation is partially circular.** Table 5 shows that adding R_text improves the "Texual" score and R_geom improves the "Geometry" score — metrics computed through the same vectorized-extraction procedure used to define the rewards themselves. Directly optimizing a metric naturally improves that metric. To the paper's credit, independent metrics (SSIM, MSE, LPIPS) also improve, partially mitigating the concern. However, the framing overstates the conclusiveness of the evidence; a human evaluation comparing models with and without each reward component, or at least a fully independent perceptual metric, would substantially strengthen this claim.

### Minor

**3. RL and data-augmentation contributions are confounded.** The final model starts from the SFT checkpoint trained on augmented data (TikZ30K, 84.50% Pass@1) and then applies RL (97.60% Pass@1). The paper does not isolate what RL alone would contribute starting from the non-augmented SFT checkpoint (Original30K, 69.74% Pass@1). Some of the 13.1% gap may be attributable to data augmentation rather than RL per se. Running RL from the Original30K checkpoint would clarify this.

**4. No variance or confidence intervals for main results.** Table 1 reports point estimates without any measure of uncertainty. For the 542-item test set, bootstrapped 95% confidence intervals would help readers assess the stability of comparisons, especially for metrics where differences between models are small (e.g., DreamSim: DaVinci-7B 84.83 vs. Claude-Sonnet-4 83.81).

**5. Human evaluation split into two non-overlapping groups prevents joint comparison.** Because DaVinci was evaluated in separate groups for non-proprietary and proprietary models, there is no single human-judgment ranking across all models. While the split is understandable given the logistical constraints of BWS, this limitation should be discussed.

**6. The "error-free" claim for PDF-based extraction is slightly overstated.** The paper states that vectorized extraction via PyMuPDF is "error-free." While this avoids OCR errors, complex TikZ constructs (decorations, shadings, transformed paths) can produce ambiguous or incomplete metadata when parsed by PyMuPDF. A brief qualification would improve accuracy.

### Trivial
None.

## Nice-to-Haves
- A systematic failure analysis (categories of diagrams where DaVinci struggles compared to Gemini) would help users understand the method's limitations.
- Running RL from the Original30K SFT checkpoint (without code reordering/comment injection) would disentangle the contributions of RL vs. data augmentation.
- A brief discussion of potential bias introduced by using Qwen-2.5-VL-32B for quality scoring during dataset filtering would be helpful.
- The paper could briefly discuss cost or alternatives to using Qwen3-Coder-480B for code reordering.

## Removed Points
- **Computational cost of Qwen3-Coder-480B for code reordering**: Using a large model for data preprocessing is standard in dataset curation and not a weakness of the paper's method.
- **Formatting/style nitpicks and broken references**: These are parser artifacts from the PDF extraction, not author errors.
- **Missing related works**: Not verifiable without external sources; I cannot confirm or deny their existence.
- **Reproducibility concerns about undisclosed hyperparameters or missing appendix content**: The parser strips appendices; these exist in the original submission.
- **Speculative "could the metric be measuring a proxy?"-type concerns**: These are area-of-concern sweeps without concrete anchors in the paper.
- **"This paper addressed an important problem" (from Strength Finder)**: Generic — every paper addresses an important problem by construction; not a specific, grounded strength.
- **"Rigorous data construction with contamination control and legal compliance" from Strength Finder**: Kept as a concrete strength above (point 1).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Revise the framing** to explicitly acknowledge Gemini-2.5-Pro's strong performance in the abstract and conclusion, and discuss why it may excel (model scale, chain-of-thought reasoning, data).
2. **Strengthen the reward ablation** by either (a) adding a human-evaluation comparison across reward settings, or (b) reporting results on a fully independent metric (e.g., CLIP score) and explicitly discussing the partial circularity.
3. **Add bootstrapped confidence intervals** to the main metrics in Table 1.
4. **Run RL from the Original30K SFT checkpoint** as an additional ablation to isolate the RL contribution from data augmentation.
5. **Qualify the "error-free" claim** regarding vectorized PDF extraction to acknowledge edge cases with complex TikZ constructs.
6. **Acknowledge the human evaluation grouping limitation** and consider a follow-up study with a unified comparison.

---

## Calibration Anchors

All anchors retrieved across rounds:

| Path | Avg Score | Round | Comparison to DaVinci |
|------|-----------|-------|----------------------|
| iTrd5xyHLP (LLMatic) | 3.40 | R1 | Much weaker — different domain (NAS), limited evaluation |
| N18Z2MkMEa (FALCON) | 3.00 | R1 | Much weaker — code generation RL, limited scope |
| nNyjIMKGCH (Reinforced UI Grounding) | 5.75 | R1 | Weaker — similar RL-for-vision technique, but criticized for baseline fairness and scalability; DaVinci is more thorough |
| KRdiRGSNc9 (HumanEval-V) | 4.60 | R1 | Weaker — benchmark paper with limited novelty and small dataset |
| bO31lfEdos (Hallucination RL) | 5.00 | R1 | Weaker — only one base model, limited generalizability |
| KvaDHPhhir (Sketch2Diagram) | 6.25 | R1/R2 | Weaker — simpler method (SFT+multi-candidate), smaller dataset; DaVinci has more technical depth |
| v3K5TVP8kZ (AutomaTikZ) | 6.50 | R2 | Comparable — text-to-TikZ (easier task), similar domain; DaVinci tackles harder image-to-code task with RL |
| M6fYrICcQs (Chain-of-region) | 6.00 | R2 | Weaker — diagram analysis (not generation), simpler CV heuristics |
| IEduRUO55F (Eureka) | 6.25 | R2 | Comparable — different domain (robot reward design), impressive but criticized for unrealistic assumptions |
| wN3KaUXA5X (Diffusion On Syntax Trees) | 7.20 | R2 | Stronger — fundamentally different approach (diffusion models), very high scores; DaVinci is not at this level |

**Round 1 bracket:** 5.5–7.5  
**Final score determination:** The paper is stronger than Sketch2Diagram (6.25) due to more sophisticated methodology and evaluation, comparable to AutomaTikZ (6.50) while tackling a harder task. The weaknesses (selective framing, partial reward circularity) are real but addressable and do not undermine the core contributions. The paper is clearly not at the 7+ level of truly exceptional work like the Diffusion On Syntax Trees paper. Score: 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>