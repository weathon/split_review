Now I have a thorough understanding of both the paper and the calibration anchors. Let me write the final review.

---

## Summary

GUI-Spotlight proposes a multi-turn, tool-augmented approach to GUI visual grounding, where a 7B VLM iteratively invokes crop, extract, and find-color tools to progressively narrow its focus on a target UI element. The model is trained via a three-stage pipeline (SFT warm-up → stabilized GSPO RL → high-resolution refinement) and achieves 52.8% on ScreenSpot-Pro with only 18.5K training samples, surpassing other 7B models. The paper also documents systematic negative results across RL algorithms and reward designs.

## Strengths

- **Strong empirical results with data efficiency:** GUI-Spotlight reaches 52.8% on ScreenSpot-Pro, outperforming all other 7B models (V2P-7B at 50.6%, GTA-1-7B at 50.1%) and matching some 72B models, while using only 18.5K curated training samples — orders of magnitude less than competitors like UGround-V1-7B (~10M) or V2P-7B (9.6M). This is substantiated in Table 3 (Section 5.1).

- **Systematic RL algorithm and reward ablation with negative results:** Sections 4.1 and 4.2 compare multiple GRPO variants (Clip-Higher, KL removal, top-p% filtering, reference-policy updating, positive-example LM loss) and reward designs (dense vs. sparse answer reward, varying crop/extract reward ratios). The paper explicitly documents which modifications degrade performance and which help, and Figure 3 (right) demonstrates that the auxiliary cross-entropy loss on tool-filtered correct completions prevents the training collapse observed in vanilla GRPO/GSPO after ~300 steps. This level of empirical transparency is uncommon and valuable for the field.

- **Robustness across different backbone models:** The method transfers from a UI-specialized backbone (UI-TARS-1.5-7B: +14.1 pp, from 38.7% to 52.8%) to a general-purpose VLM (Qwen2.5-VL-7B-Instruct: +11.9 pp, from 26.8% to 38.7%), as shown in Table 3. This demonstrates that the training framework is not tied to a particular initialization.

- **Multi-benchmark evaluation:** The model is evaluated on three distinct benchmarks — ScreenSpot-Pro (high-res professional software), UI-Vision (desktop applications), and OSWorld-G (OS-level tasks) — providing a broader picture of generalization than papers that evaluate on only one or two benchmarks.

## Weaknesses

### Fatal

None.

### Major

- **No controlled single-step baseline with identical training data and budget.** The paper's central claim is that iterative tool use ("spotlighting") improves grounding. The primary comparisons in Table 3 are against the base models UI-TARS-1.5-7B and Qwen2.5-VL-7B-Instruct, neither of which was fine-tuned on the same filtered UGround + high-resolution web data used to train GUI-Spotlight. The reported gains (+14.1 pp for UI-TARS, +11.9 pp for Qwen) are therefore confounded: they could arise from (a) the additional training data, (b) the SFT+RL training pipeline itself, (c) the iterative tool-use mechanism, or any combination thereof. Section 5.4 compares against training-free iterative inference strategies and shows they do not work, but this does not isolate the tool-use contribution from the data/training contribution. Without a baseline that receives the same SFT+RL pipeline on the same data but outputs coordinates directly (or uses at most one crop), the core contribution remains unvalidated.

- **The `find color` tool is a hand-crafted heuristic whose contribution is not analyzed.** As described in Table 1 and Section 3.1, `find color` requires the model to predict an RGB value, then performs a deterministic 10×10 patch scan minimizing ΔE in CIE Lab space to locate the closest color match, returning a centered crop. This programmatic color-matching search automates a substantial portion of the grounding task via a pixel-level operation, relieving the model of spatial reasoning, shape recognition, and layout understanding. The paper provides **no** analysis of: (a) how frequently this tool is invoked at test time, (b) whether the model's RGB predictions are accurate, or (c) what performance would be without this tool. The presence of such a strong heuristic inflates apparent capability and makes it difficult to interpret results as evidence for learned visual reasoning.

- **No behavioral evidence that the model actually performs iterative multi-turn refinement.** The paper's narrative centers on "iterative spotlighting," yet it reports no statistics on the number of tool calls per episode, the distribution of tools used, or the success/failure rates of intermediate steps. Algorithm 1 permits up to T_max steps, but a single well-placed `crop` or `find color` followed by an answer suffices to satisfy the reward structure (Table 2). It is entirely possible that the trained policy uses only one tool invocation in most cases, which would mean the "iterative" framing is overstated. Without behavioral diagnostics, the central narrative is unsupported.

### Minor

- **Marginal gains on OSWorld-G for the UI-TARS backbone.** GUI-Spotlight trained from UI-TARS-1.5-7B achieves only +0.8 pp on OSWorld-G (62.7% vs. 61.9%, Table 5). The paper describes this as evidence that "RL with tool-augmented feedback provides clear benefits" (Section 5.3), which overstates a gain that could plausibly fall within evaluation variance. The +4.2 pp gain from the Qwen2.5-VL-7B backbone is more meaningful, but the paper does not investigate why the method fails to help a UI-specialized backbone on this benchmark, which undermines the generality claim.

- **Teacher model dependence not ablated.** The SFT trajectories are collected from Qwen2.5-VL-72B, and the data filtering pipeline (Section 3.2.1) also relies on this 72B model for auditing. The extent to which final performance depends on teacher quality is unexplored, making it unclear whether the method would transfer to settings where a strong teacher is unavailable.

### Trivial

- The tool set design choices (why 10×10 patches, stride 10, fixed 200×200 window for `find color`) are stated but not justified.
- Section 4's RL algorithm explorations are conducted over only 400 training steps rather than full convergence, so the long-term relevance of these findings to final performance is uncertain.

## Nice-to-Haves

- A diagnostic study investigating why OSWorld-G gains are negligible for the UI-TARS backbone, and whether the tool set is poorly suited to OS-level tasks.
- Qualitative case studies showing actual tool-call trajectories from the trained model (like Figure 1 but with real outputs), including both successful and failed grounding attempts, to characterize the model's actual behavior.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

**From Harsh Critic:**

- The claim about "no baseline that applies the same SFT+RL training pipeline but outputs coordinates directly" is **kept** as a major weakness — it is factually correct and substantive.

- The claim about `find color` being hand-crafted and skewing evaluation is **kept** as a major weakness — verified against Table 1 and Section 3.1.

- The claim about OSWorld-G gains being negligible is **kept but downgraded to minor** — the +0.8 pp on the UI-TARS backbone is indeed marginal, but the +4.2 pp on the Qwen backbone shows some transfer. The paper overstates the conclusion but the data is there.

- The claim about no analysis of actual multi-turn behavior is **kept** as a major weakness — verified; the paper genuinely does not report tool usage statistics.

- The criticism about "Related Work omits work on iterative refinement" is **removed** — the paper does discuss GUI agents, RL for grounding, and related approaches (UniVGR1, GROUNDR1, self-evolutionary RL). Per instructions, I do not add missing references that I cannot confirm.

- The criticism about RL algorithm explorations over only 400 steps is **kept but moved to trivial** — it is correct but does not invalidate any core claim.

- The criticism about Stage 3 enforcing balanced tool usage via bucketed sampling ("further indicating that RL alone does not produce diverse tool-using behaviour") is **removed** — the paper explicitly acknowledges this and addresses it as a training-stage refinement, not a limitation. The bucketed sampling is a design choice to encourage exploration, not evidence of failure.

- The Section-by-Section notes about teacher-model dependency and benchmark alignment are **consolidated into the minor weakness** about teacher model dependence not being ablated.

**From Strength Finder:**

- "Significant accuracy on high-resolution GUI grounding with minimal data" — **kept**, verified against Table 3.

- "Effective three-stage training that yields large gains over base models" — **kept**, verified against Figure 2 and Table 3.

- "Stabilized multi-turn RL via an auxiliary cross-entropy loss" — **kept**, verified against Section 4.1 and Figure 3.

- "Robustness to different backbone models" — **kept**, verified against Table 3.

- "Systematic ablation of RL algorithms and reward components" — **kept**, verified against Sections 4.1-4.2.

- "Learned iterative refinement outperforms naive inference-time strategies" — **kept but noted** that Section 5.4 compares against untrained heuristics and does not isolate tool-use from data/training.

- "Quality-focused data curation via large-model auditing" — **removed**. While the filtering pipeline exists, there is no ablation showing this filtering actually improves final accuracy over unfiltered data. It is a plausible but unvalidated strength.

## Novel Insights

None beyond the paper's own contributions. The systematic documentation of negative RL results (e.g., which GRPO variants degrade performance, why dense answer rewards underperform sparse ones) is the most distinctive empirical contribution, providing actionable guidance for practitioners that is rarely found in published work in this area.

## Suggestions

- **Add a single-step baseline trained with identical data and pipeline.** This is the minimal experiment needed to attribute gains to iterative tool use. Train a model on the same SFT+RL data but constrained to output a single coordinate (or at most one crop), and compare against the full GUI-Spotlight. Without this, the core contribution claim is unsupported.

- **Report tool-usage statistics for the final model.** Provide the distribution of tool calls per episode, the frequency of each tool type, and the success rate of intermediate steps. This would substantiate (or refute) the "iterative spotlighting" narrative.

- **Ablate the `find color` tool.** Evaluate performance without this tool and report how often it is invoked. If performance collapses without it, the paper should acknowledge that the method depends heavily on a hand-crafted heuristic rather than learned visual reasoning.

- **Investigate the OSWorld-G results.** Diagnose why the UI-TARS backbone sees near-zero improvement and whether the tool set needs adaptation for OS-level tasks.

## Score and Decision

**Anchor comparison:**

| Anchor | Path | Avg Score | Decision | Comparison to GUI-Spotlight |
|--------|------|-----------|----------|-----------------------------|
| GTA1 | `3VIPmz7iAi.md` | 5.50 | Accept (Poster) | GTA1 has a simpler method but cleaner experimental validation and shows gains on both grounding and agent execution. GUI-Spotlight has broader RL ablations but a more fundamental missing baseline. |
| GUI-Cursor | `kNAQMZf53k.md` | 5.00 | Reject | Most comparable anchor. Both use multi-turn RL for GUI grounding, both achieve strong ScreenSpot-Pro results, both lack a same-data single-step baseline. GUI-Spotlight has broader benchmark coverage (3 vs 2) and more systematic RL ablations, but has the additional `find color` heuristic concern. |
| InfiGUI-R1 | `wywgRd1MUQ.md` | 5.00 | Reject | Similar score band. InfiGUI-R1 proposes a two-stage training paradigm for GUI agents. GUI-Spotlight is more narrowly focused on grounding but has more thorough empirical analysis. |
| RewardMap | `iRVbPxHNrX.md` | 5.00 | Accept (Poster) | Different domain (transit maps vs GUI). Both use multi-stage RL. RewardMap's contributions are more clearly isolated through ablations. |
| GUI-AIMA | `ypptmENxJn.md` | 4.00 | Reject | GUI-Spotlight has substantially stronger empirical results, broader benchmark coverage, and more extensive ablations than GUI-AIMA. |
| V2P | `D4ZcCiyYeC.md` | 4.00 | Reject | GUI-Spotlight surpasses V2P in benchmark breadth (3 vs 2), backbone diversity (2 vs 1), and methodological novelty (RL + tool-use vs attention calibration), achieving comparable or better accuracy. |
| GMS | `hu2aOpy11D.md` | 2.50 | Reject | GUI-Spotlight is clearly stronger: actual training vs. training-free framework, broader benchmarks, better results. |
| LongVTG-R1 | `8H1HmGH8ua.md` | 3.50 | Reject | Different domain (video temporal grounding). GUI-Spotlight's experiments are more comprehensive. |

**Calibrated score rationale:** GUI-Spotlight is clearly stronger than the 4.0-anchored papers (V2P, GUI-AIMA) in terms of experimental breadth, result quality, and methodological depth. However, it shares with GUI-Cursor (5.00, Reject) the critical weakness of lacking a controlled single-step baseline, and has the additional concern of an unablated hand-crafted heuristic (`find color`). The core claim — that iterative spotlighting drives the improvement — is not adequately isolated from confounding factors. I place it at 4.5, acknowledging stronger experimental execution than the 4.0 tier but with a methodological gap that prevents acceptance in current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>