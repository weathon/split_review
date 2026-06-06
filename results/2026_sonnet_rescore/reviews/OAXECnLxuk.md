## Summary

DaVinci is a 7B-parameter MLLM trained in two stages — SFT on a newly curated TiKZ-30K dataset featuring drawing-order normalization and comment-injection scaffolds, then GRPO-based reinforcement learning with a hybrid reward that combines compile-success, image-fidelity, spatio-textual, and geometric signals derived from error-free vectorized PDF representations. The resulting model achieves the highest compile rate (97.60%) among all evaluated systems and competitive image-fidelity metrics, surpassing all open-source models and several proprietary ones on the DATiKZv3 benchmark.

---

## Strengths

1. **Strong empirical compile-rate result with validated ablation**: DaVinci-7B attains 97.60% compile rate — far above all baselines (Table 1). Table 4 decomposes the gain clearly: raw code SFT → 69.74%, adding reordering → 78.78%, adding comments → 84.50%. This 14.76 percentage-point gain over the raw-code baseline establishes drawing-order normalization and comment annotation as concretely impactful, previously underexplored data features.

2. **Extraction-error-free reward design**: The use of PyMuPDF to extract text objects and geometric primitives directly from compiled vectorized PDFs (Section 3.3, Algorithms 1–2) is a practical improvement over OCR-based rewards. It sidesteps a well-documented failure mode (OCR misreading symbols/graphical elements in scientific diagrams) and feeds precise spatial-textual and geometric feedback into RL training.

3. **Comprehensive comparison against diverse baselines**: The evaluation covers proprietary models (Gemini-2.5-Pro-Thinking, GPT-5, Claude-Sonnet-4), open-source general MLLMs (Qwen2.5-VL series, GLM-4.5V), and specialized TiKZ models (DetikZify-V2-8B, DiagramAgent-7B). A human evaluation using Best-Worst Scaling over 100 items with two separate groups validates results beyond automatic metrics (Tables 2–3).

4. **Insightful "thinking vs. non-thinking" analysis**: The finding that enabling explicit reasoning chains does not consistently improve diagram parsing — and actually hurts GLM-4.5V's compile rate (67.90% → 62.92%) — is an interesting empirical result, supported by the hypothesis that sequential code generation itself serves as an implicit reasoning process.

---

## Weaknesses

### Fatal
None.

### Major

- **Abstract and conclusion overstate the competitive comparison by omitting Gemini-2.5-Pro-Thinking**: The abstract claims DaVinci "surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4." The conclusion repeats: "outperforming both open-source MLLMs and leading proprietary models such as GPT-5 and Claude-Sonnet-4." Both omit Gemini-2.5-Pro-Thinking, which in Table 3 scores +0.50 in human evaluation while DaVinci-7B scores −0.01, and which beats DaVinci-7B on DreamSim (88.20 vs. 84.83), SigLIP (95.59 vs. 93.93), SSIM (75.86 vs. 73.65), and LPIPS (21.64 vs. 22.32) in Table 1. The body of the paper does acknowledge this (Section 4.3: "Gemini-2.5-Pro presents better performance than DaVinci-7B regarding certain metrics"; Section 4.4: "Gemini-2.5-Pro-Thinking significantly outperforms all other models in both groups"), but this accurate framing is absent from the abstract and conclusion. The correct headline is that DaVinci-7B is state-of-the-art among open-source and task-specialized models, competitive with GPT-5 and Claude-Sonnet-4, but clearly behind Gemini-2.5-Pro-Thinking on visual-quality metrics and human judgment. This selective framing is pervasive and should be corrected; it is a presentation problem, not a methodology problem, but it is consequential.

### Minor

- **Table 5 DreamSim regression is unaddressed**: Adding $R_\text{text}$ and $R_\text{geom}$ to the base reward improves SSIM, MSE, LPIPS, and the explicit structural metrics (Textual, Geometry), but the final model's DreamSim (84.75) is lower than the base ($R_\text{img} + R_\text{pass}$) at 85.00. This implies a small perceptual–structural trade-off when structural rewards are added. The paper presents Table 5 without acknowledging this inversion. A brief explicit statement about whether this trade-off is acceptable and why would strengthen the analysis.

- **Human evaluation split-group design limits cross-group inference**: Group 1 evaluates DaVinci-7B against open-source models; Group 2 evaluates it against proprietary models, with different item samples and different competing-model fields. DaVinci-7B's scores across groups (−0.01 in Group 2, +0.36 in Group 1) are not directly comparable. The design is appropriate for the within-group conclusions drawn (DaVinci-7B best open-source; competitive with GPT-5 and Claude-Sonnet-4), but cannot support cross-group ranking. The paper does not flag this limitation. It should be noted, even briefly, to avoid over-interpretation.

### Trivial
None beyond the framing issue already captured above.

---

## Nice-to-Haves

- A structured failure analysis of the ~2.4% of DaVinci-7B outputs that still fail to compile, cross-referenced with diagram type, would sharpen understanding of where the RL training still falls short.
- Discussion of sensitivity to the scaling constant $k$ in Eq. 4 ($R_\text{geom}$), which is a free parameter that currently has no stated value or robustness analysis in the main text.
- A report on what fraction of the 30K SFT samples were discarded by the post-verification filter (rendering consistency before/after reordering) would quantify the prevalence and difficulty of the code-ordering problem the paper addresses.
- Exploring whether inference-time search (as used by DetikZify-V2-8B via MCTS) provides additional gains on top of DaVinci-7B's RL-trained policy would close an interesting open comparison.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: compile-rate improvement achieved at cost to faithfulness (reward-induced simplification)** — The paper acknowledges that the few remaining failures are scatter plots that exceed context length, and DaVinci-7B's MSE (61.81) is the best of all models in Table 1, better than even Gemini (66.62). The simplification hypothesis is speculative and not supported by the evidence on the page. Demoted to background concern; not substantiated enough to retain as a weakness.

- **Harsh critic: geometric reward penalizes valid alternative reconstructions** — The concern that the ground-truth PDF compiled from reference TiKZ is "one plausible reconstruction, not certified ground truth" is generic to any learned-reward approach. There is no specific example or analysis in the paper showing this causes problems. It reads as a category-sweep speculation, not a grounded finding.

- **Harsh critic: statistical power of 100-item human evaluation** — With SHR values of 0.72 and 0.79 and clear numerical separations (DaVinci-7B scores 0.36 vs. −0.26 for the weakest in Group 1; Gemini scores 0.50 vs. −0.35 for the weakest in Group 2), the 100-item sample with 6 evaluators is in line with prior work that the paper explicitly cites (Belouadi et al., 2024b; 2025). Demanding significance tests is a methodological practice not standard for this evaluation paradigm. Moved to nice-to-have at most.

- **Strength Finder: "DaVinci-7B earns the highest human preference score among non-proprietary models"** — Confirmed by Table 2. Kept in strengths.

- **Strength Finder: "surpasses GPT-5 and Claude-Sonnet-4"** — Accurate as a narrow claim (Tables 1, 3) but conflicts with the verified weakness about omitting Gemini. Removed as a standalone strength to avoid echoing the overstatement.

---

## Novel Insights

The observation that cBLEU (code-level lexical similarity) *decreases* from SFT to RL while all image-quality and compile metrics *improve* is a concise and well-supported empirical demonstration that visual reconstruction fidelity and code surface similarity are dissociated for TiKZ generation. The finding that explicit reasoning chains ("thinking" mode) do not consistently help structured code-generation tasks — and may actively hurt compile rate — adds a practically important counterpoint to the broad assumption that extended reasoning universally improves MLLM performance.

---

## Suggestions

1. **Fix the abstract and conclusion**: Replace "surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4" with a more accurate framing such as "achieves state-of-the-art performance among open-source models and surpasses GPT-5 and Claude-Sonnet-4, while narrowing the gap to the strongest proprietary model (Gemini-2.5-Pro-Thinking) with a 10× lower parameter count." This requires no new experiments, only accurate language.
2. **Address the Table 5 DreamSim regression explicitly**: Add one or two sentences in Section 4.5 acknowledging the slight DreamSim drop when structural rewards are added, and take a position on whether this trade-off is intentional (e.g., structural accuracy at mild perceptual cost).
3. **Note the split-group human evaluation limitation in Section 4.4**: A single sentence clarifying that Group 1 and Group 2 scores are within-group-only comparisons would pre-empt misinterpretation.
4. **Report the post-verification discard rate** for the code-reordering step (in appendix if not main text), as it quantifies the severity of the ordering-noise problem the paper is designed to address.

---

## Evaluation

**Originality**: The two-stage framework and GRPO-based RL for diagram parsing are incremental relative to prior work, but the specific combination of drawing-order normalization, comment-based planning scaffolds, and vectorized-PDF geometric rewards represents meaningful methodological novelty. Moderate-to-good.

**Importance of research question**: Parsing scientific diagrams into editable structured representations is a practically significant problem, under-explored relative to UI or chart parsing. Good.

**Claims well-supported**: Most quantitative claims are directly verifiable in Tables 1–5 and ablations. The headline claim in the abstract/conclusion overstates the competitive comparison. The core contribution claims are otherwise solid.

**Soundness of experiments**: The ablation design is clean and isolates the key components; the test benchmark (DATiKZv3) is the established standard; the human evaluation follows published protocols. Sound overall, with the human-eval split-group caveat noted.

**Clarity of writing**: The paper is well-organized and readable. The framing inconsistency (abstract/conclusion vs. body) is the main clarity issue.

**Value to the research community**: The open-sourced TiKZ-30K dataset and the vectorized-reward design are immediately reusable. Code and models are released. High practical value.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>