Now let me run calibration searches to properly score this paper.**Round 1 bracket: 5.5–7.5** — DaVinci is clearly stronger than the weak anchors, has solid methodology and results, but has some overclaiming issues. Let me narrow in.Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

DaVinci is a 7B-parameter MLLM for scientific diagram parsing that converts raster images into compilable TiKZ code. The paper proposes a two-stage framework: (1) supervised fine-tuning on a newly curated TiKZ-30K dataset enriched with drawing-order normalization and comment-based planning scaffolds, and (2) GRPO-based reinforcement learning with a hybrid reward combining compile success, image fidelity, and novel extraction-error-free spatio-textual and geometric rewards computed directly from vectorized PDF output. The method achieves 97.6% compile rate — the best across all evaluated systems — and outperforms open-source models and several proprietary models (GPT-5, Claude-Sonnet-4) in both automatic metrics and human evaluation.

---

## Strengths

- **Best compile rate and competitive visual fidelity for an open-source model**: DaVinci-7B achieves 97.60% Pass@1, a +13.1 pp gain over its SFT initialization, and ranks second overall on DreamSim (84.83) and LPIPS (22.32) across all evaluated models — outperforming every non-Gemini system (Table 1). This directly validates the two-stage framework.

- **Error-free reward signal via vectorized PDF extraction**: By using PyMuPDF to directly extract text objects and geometric primitives from the compiled PDF (rather than OCR), the paper avoids known OCR failure modes on diagrams (Section 3.3, Algorithms 1–2). This is a practically clean and reproducible design choice that concretely improves on prior work.

- **Validated ablation of drawing-order normalization and comment injection**: Table 4 demonstrates that reordering alone raises compile rate from 69.74% to 78.78% (+9.04 pp), and adding comments further raises it to 84.50% (+5.72 pp), validating these data features as genuinely important — not merely asserted.

- **Human evaluation confirms open-source leadership**: In Group 1 (open-source), DaVinci-7B achieves a BWS score of +0.365 vs. −0.05 for the next-best models, with SHR of 0.72 indicating reasonable annotator agreement (Section 4.4, Table 2).

- **Insight on code similarity vs. visual quality**: The paper correctly observes that cBLEU *decreases* from SFT to RL while visual quality metrics improve, demonstrating that strict code-level similarity is neither necessary nor sufficient for diagram fidelity (Section 4.3). This is a useful finding for the community.

---

## Weaknesses

### Fatal
None.

### Major

- **Selective framing in abstract and conclusion regarding proprietary model comparison.** The abstract states DaVinci "surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4," and the conclusion repeats "outperforming... leading proprietary models such as GPT-5 and Claude-Sonnet-4." This is technically accurate for those two models but omits Gemini-2.5-Pro-Thinking, which is clearly better: DreamSim 88.20 vs. 84.83, SSIM 75.86 vs. 73.65, LPIPS 21.64 vs. 22.32, and a BWS human evaluation score of +0.50 vs. DaVinci-7B's −0.01 (Tables 1 and 3). Section 4.3 briefly acknowledges "Gemini-2.5-Pro presents better performance than DaVinci-7B regarding certain metrics," but this acknowledgment is buried in the body and absent from the abstract and conclusion. The correct characterization is that DaVinci-7B is the best open-source/specialized model and competitive with GPT-5 and Claude-Sonnet-4, while remaining behind Gemini-2.5-Pro-Thinking on visual quality and human judgment. This framing error is pervasive and should be corrected.

### Minor

- **DreamSim regression in Table 5 is unexplained.** The base reward ($R_\text{img} + R_\text{pass}$) achieves DreamSim of 85.00; adding $R_\text{text}$ gives 84.85; and the full model with $R_\text{text} + R_\text{geom}$ gives 84.75. The paper claims the full model improves across the board but does not comment on this visible regression. The full model does improve MSE (62.30), LPIPS (22.32), and the specialized textual and geometric scores — but the perceptual similarity score declines. This trade-off deserves explicit discussion: does the structural reward introduce more syntactically correct but perceptually slightly different code?

- **Possible reward-induced simplification not investigated.** DaVinci-7B's compile rate jumps +13.1 pp from SFT to RL, but SSIM improves by only +1.0 pp (72.65 → 73.65). The paper notes failure cases are "mainly dense visualizations like scatter plots, where the model over-produces data points, leading the output to exceed the context limit" — suggesting the RL pressure toward compilability may lead to truncated/simplified outputs on hard inputs. Whether this quality–compilability trade-off exists for challenging diagram types is not analyzed. An investigation of compiled-but-low-quality RL outputs vs. non-compiled SFT outputs on hard inputs would substantiate (or refute) this possibility.

- **Split human evaluation design limits cross-group inference.** Group 1 evaluates DaVinci-7B against open-source models; Group 2 evaluates it against proprietary models. Because the competing set differs, DaVinci-7B's score of +0.365 in Group 1 and −0.01 in Group 2 are not directly comparable, and cross-group ranking (e.g., that Gemini-2.5-Pro outperforms DetikZify-V2-8B) cannot be established from this design. The paper presents these as a unified picture in Section 4.4 without flagging this limitation.

- **Scaling constant $k$ in $R_\text{geom}$ (Equation 4) is not discussed.** This is a free parameter in the exponential decay function that governs how geometric dissimilarity is penalized. Its value and any sensitivity analysis are deferred to the appendix (which the parser strips), but a single sentence in the main text discussing its robustness would strengthen confidence in the reward's stability.

### Trivial
None.

---

## Nice-to-Haves

- A structured failure analysis of the ~2.4% non-compilable RL outputs and of cases where Gemini-2.5-Pro beats DaVinci-7B in human evaluation (e.g., by diagram type or density) would sharpen the paper's understanding of where visual-structural syntax learning succeeds and where it still falls short.
- The "to think or not to think" comparison (Section 4.3) is underpowered because Gemini-2.5-Pro and GPT-5 are only available in thinking variants. A more controlled analysis (e.g., using Claude-Sonnet-4 vs. Claude-Sonnet-4-Thinking with matched temperature/budget) would help clarify the finding. The paper appropriately defers this to future work.
- Reporting the fraction of samples discarded because reordering broke rendering would quantify the difficulty and scale of the ordering noise problem.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "High compile rate may reflect reward-induced simplification" elevated to structural concern.** This is a valid observation worth investigating (kept as Minor), but the critic elevated it to a near-structural concern. Given that the paper explicitly identifies the failure cases (dense scatter plots exceeding context limits) and that the image quality metrics do improve — just modestly — this is a gap in analysis, not a flaw that invalidates the compile-rate result.

- **Strength Finder: "Superior performance" claim in abstract treated as validated strength.** The claim that DaVinci surpasses all proprietary models is only partially true; Gemini-2.5-Pro clearly outperforms it. This strength is demoted to "best open-source / competitive with GPT-5 and Claude-Sonnet-4," consistent with the factual record.

- **Strength Finder: "Error-free element verification" described as entirely OCR-error-free.** Partially retained but qualified: the vectorized extraction is free of *OCR* errors but relies on the reference TiKZ rendering as ground truth, which is one valid reconstruction rather than a certified unique ground truth. This is a minor qualification, not a fatal flaw.

---

## Novel Insights

The paper's most genuinely novel observation is the "high code similarity is not necessary" finding (Section 4.3): cBLEU drops from SFT to RL while visual quality metrics improve, suggesting that RL training discovers a broader space of TiKZ programs that render equivalently to the reference, and that strict lexical code similarity is a poor proxy for visual fidelity. Combined with the ablation showing that drawing-order normalization adds nearly 9 percentage points of compile rate independent of the base model, this suggests that the space of TiKZ programs is substantially under-constrained and that training data organization — not just data scale — is a key factor for structured code generation tasks.

---

## Suggestions

1. **Fix the abstract and conclusion framing**: replace "surpasses leading proprietary models" with "outperforms open-source models and competitive proprietary systems (GPT-5, Claude-Sonnet-4), while Gemini-2.5-Pro-Thinking remains the top system overall." This is the most important revision.
2. **Add a paragraph in Section 4.5 discussing the DreamSim regression in Table 5**: take a position on whether the structural rewards trade perceptual similarity for geometric/textual accuracy, and whether this trade-off is acceptable given the task.
3. **Explicitly flag the split human evaluation design limitation** in Section 4.4: note that cross-group score comparisons require caution and that the Group 2 evidence supports only that DaVinci-7B beats GPT-5-Default and Claude-Sonnet-4-Thinking in human evaluation.
4. **Add a short failure analysis**: one table or figure showing which diagram categories DaVinci-7B fails on (non-compilable or low-quality) would ground the "remaining challenges" discussion.

---

## Score and Decision

**Axis evaluation:**
- *Originality*: Solid. The vectorized-extraction reward is genuinely novel for diagram generation; the drawing-order and comment-injection insights are underexplored and well-validated.
- *Importance*: Moderate-to-high. Scientific diagram parsing is a real and growing problem; a 7B model that compiles reliably and matches proprietary performance is valuable to the community.
- *Claims vs. support*: Mostly well-supported; the overclaiming in the abstract/conclusion is the main gap.
- *Soundness of experiments*: Good. Two-stage ablations, human evaluation with SHR, diverse baselines. The human eval is lean (100 items, 6 evaluators) but consistent with prior work norms.
- *Clarity*: Good, with the exception of the framing issue.
- *Community value*: High. Dataset and model release, clear training recipe.

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| OXIIFZqiiN.md | 1.50 | R1 | Much weaker — dual-modal patch paper with thin contribution |
| pLvh9DTyoE.md | 2.50 | R1 | Weaker — multimodal NER low-resource prompting |
| HfJxXbXlYJ.md | 3.00 | R1 | Weaker — incremental CLIP extension |
| KLUDshUx2V.md | 3.40 | R1 | Weaker — concept bank automation |
| nNyjIMKGCH.md | 5.75 | R1/R2 | Somewhat weaker — UI grounding with RL, narrower contribution |
| 9RFocgIccP.md | 6.00 | R1/R2 | Comparable but DaVinci more novel; DaVinci has better-designed reward |
| bO31lfEdos.md | 5.00 | R1 | Weaker — RL for hallucination, smaller contribution |
| KRdiRGSNc9.md | 4.60 | R1 | Weaker — benchmark-only paper |
| IEduRUO55F.md | 6.25 | R2 | Comparable; Eureka broader scope but DaVinci tighter execution |
| cJQ1K2fjpD.md | 6.20 | R2 | Similar tier — vision-language alignment |
| HVtu26XDAA.md | 7.00 | R2 | Somewhat stronger — broader MLLM family with more experiments |
| k5VHHgsRbi.md | 6.80 | R2 | Similar scope but benchmark paper rather than method |
| o5TsWTUSeF.md | 6.75 | R2 | Comparable — ChartMoE for chart understanding, similar scale |
| kwqhn2VuG4.md | 7.50 | R2 | Stronger — large-scale dataset at 10B scale |

**Round 1 bracket**: 5.5–7.5  
**Round 2 narrowing**: DaVinci sits above the 6.0–6.25 anchors (Multi-Reward, Eureka, FiSAO): it is technically more novel, has a cleaner evaluation, and makes a real practical contribution. It sits below MM1.5 (7.0) and OmniCorpus (7.5), which have broader scope and impact. It is roughly comparable to ChartMoE/MME-RealWorld at 6.75–6.80 in contribution depth.  
**Final score**: The paper is a solid contribution with genuine novelty in the reward design and dataset curation, but the framing overclaiming in abstract/conclusion and the unexplained DreamSim regression prevent a higher score. Positioning at **6.5** — clearly above the 6.0–6.25 cluster, below the 7.0 cluster.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>