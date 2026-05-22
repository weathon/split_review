Now I have sufficient calibration data. Let me write the final review.

## Summary

This paper investigates the role of pooled text embeddings (e.g., CLIP) in diffusion transformers, finding that they contribute minimally to generation quality for long prompts and are fully inactive in some models (HiDream-Fast, COSMOS). Building on this analysis, the authors propose "modulation guidance" — a training-free technique that repurposes the pooled embedding as a guidance signal in modulation space (structurally analogous to CFG) to improve aesthetics, complexity, object counting, and hand generation. The method is validated across multiple models (FLUX, SD3.5, HiDream, COSMOS, Hunyuan, CausVid) and tasks (T2I, T2V, image editing) with both human and automatic evaluation.

## Strengths

- **Genuinely useful empirical finding about pooled embeddings.** Table 1 provides concrete, quantitative evidence that removing the CLIP pooled embedding from FLUX schnell has negligible effect on quality for long prompts (−0.3 PickScore, +0.1 ImageReward) and no effect at all for HiDream-Fast. Figure 1 further shows DreamSim deviation dropping to near zero beyond ~40 tokens. This finding is directly actionable for model designers.

- **The COSMOS ablation elegantly disentangles the two contributions.** Table 2 shows that simply adding CLIP to COSMOS yields no improvement (43% complexity win rate — actually worse than 50%), but combining CLIP with modulation guidance yields 70% and 61% complexity win rates. This demonstrates that the improvement comes from the guidance mechanism itself, not merely reintroducing a pooled embedding.

- **Broad cross-model and cross-task validation with human evaluation.** The method is demonstrated on 6+ models across T2I (Table 2), T2V (Table 4), and image editing (Figure 8, Appendix F), with side-by-side human preference evaluation on four criteria. Win rates are substantial: up to 78% for complexity on FLUX schnell, 72% for aesthetics, and consistent statistically significant gains across models. This breadth exceeds typical guidance method papers.

- **Attention analysis provides mechanistic insight.** Figure 4 shows that modulation guidance redirects model attention toward semantically relevant tokens (e.g., "hands" and hand-related tokens receive higher mean attention), offering a plausible mechanism rather than treating the method as a black box.

- **Practical value: training-free, simple, broadly applicable.** The method requires only hand-crafted positive/negative prompts and a guidance scale, with no model-specific tuning. The dynamic guidance strategy (Figure 3) provides a better quality-fidelity trade-off than constant scaling.

## Weaknesses

### Fatal
None.

### Major

- **The paper does not fully resolve the tension between "CLIP is ineffective" and "modulation guidance works."** The analysis (Section 4) shows CLIP contributes negligibly to conventional conditioning, yet the method produces large improvements by shifting in CLIP's modulation space. The paper does not explicitly address how a "weak" or "inactive" signal becomes highly effective when used directionally. The likely explanation — that the *direction* in embedding space (p+ minus p−) is informative even if the *magnitude* of CLIP's modulation contribution is small — would significantly clarify the contribution. Without this reconciliation, the reader is left to infer the mechanism, which undermines the paper's claim to "rethinking" global text conditioning. [Lines 87–93 vs. 99–109]

- **Baseline comparisons are relegated to Appendix E rather than presented in the main text.** For a paper proposing a new guidance method, the main comparisons against Normalized Attention Guidance (Chen et al., 2025) and Concept Sliders (Gandikota et al., 2024) appear only in Appendix Tables 8–9. The main text states the results ("outperforms Normalized Attention Guidance by 34% and Concept Sliders by 16%") but does not present the data. This is a structural weakness — readers cannot assess baseline fairness without consulting the appendix. [Line 230]

### Minor

- **Automatic aesthetic metrics are partially circular.** When using "beautiful, highly detailed, professional" as the positive prompt for aesthetics guidance, the resulting images will naturally score higher on PickScore, ImageReward, and HPSv3 — these metrics encode human aesthetic preferences that the guidance explicitly optimizes for. The human evaluation partially addresses this, but the paper presents automatic metrics with equal prominence and does not acknowledge the circularity. Placing greater weight on human evaluations would strengthen the evaluation. [Tables 2–3, automatic metrics columns]

- **No runtime comparison is provided.** The paper claims "negligible computational overhead" (lines 16, 30, 107), arguing that $\hat{y}$ only affects modulation coefficients. However, the method requires computing MLP outputs for both positive and negative prompts at each denoising step. For multi-step models (e.g., 50 steps), this is not trivially negligible. The claim should be supported by wall-clock timing. [Lines 107, 230]

- **Image editing results in the main paper are qualitative only.** Section 6.3 presents only Figure 8 (two examples) for the editing task, with quantitative SEED-Data results deferred to Appendix F. For a claimed contribution (contribution (3) in the abstract), the main paper should include key editing metrics. [Line 265]

- **Prompt sensitivity analysis is missing.** The method's effectiveness depends on hand-crafted positive/negative prompts for each property (aesthetics, complexity, hands, counting). The paper does not analyze how much results vary with different phrasings. This leaves open the possibility that specific prompts were found by trial and error, which would limit reproducibility and generalizability. [Appendix D referenced for prompt choices]

- **The analysis of *why* CLIP is weak for short prompts vs. long prompts in FLUX schnell is underexplored.** Table 1 shows CLIP matters for short prompts (−1.7 ImageReward) but not long ones. The paper notes this but doesn't analyze the mechanism — is it information redundancy (long prompts give T5 enough context to make CLIP redundant), or is it that modulation layers can't amplify CLIP's signal? This distinction matters for understanding the broader applicability of the finding. [Table 1, lines 87–89]

### Trivial
None.

## Nice-to-Haves

- GenEval results (Table 3) are reported only for FLUX schnell. Results for other models would strengthen the generality claim.
- The CausVid improvement (dynamic degree: 75.25 → 86.59) could partly reflect that distillation compressed out dynamics that modulation guidance restores. Discussing this explicitly would add nuance.
- Figure 4's attention analysis covers only the hands correction case. Understanding the mechanism for aesthetics/complexity guidance (where there is no single "relevant token") would be more convincing.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh critic's claim that the "discovery" about CLIP is "architectural trivia"**: The paper does disentangle the finding across multiple architectures (FLUX schnell uses CLIP, HiDream-Fast uses a different encoder, COSMOS uses no CLIP at all). The finding that pooled embeddings are inactive generalizes across these architectures, which is more than architectural trivia.
- **Harsh critic's claim that modulation guidance is "essentially CFG" with overstated novelty**: The paper acknowledges inspiration from attention guidance methods (Chen et al., 2025) and does not claim to invent the formula itself. The title uses "rethinking" which is standard framing for empirical analysis papers. The real contribution is the cross-model analysis + practical technique, not the equation.
- **Missing related works, missing appendix content, formatting issues**: These are parser artifacts or external knowledge gaps, not paper problems.

## Novel Insights

The most novel insight is the empirical demonstration that pooled text embeddings are functionally dead in modern diffusion transformers across multiple architectures, but that this "dead" signal can be resurrected as a directional guidance mechanism in modulation space. The COSMOS ablation (CLIP alone fails, CLIP + guidance succeeds) is a particularly clean experimental design that isolates the contribution of the guidance mechanism. This insight has practical implications for model designers (pooled embeddings can be safely removed from conventional conditioning) and for practitioners (they can be repurposed as a cheap, training-free control signal).

## Suggestions

1. Add an explicit paragraph reconciling "CLIP is weak as conditioning" with "modulation guidance is effective" — likely the direction in embedding space carries semantic information even when the magnitude contribution is small.
2. Move baseline comparison results (Tables 8–9 from Appendix E) into the main paper body, even if abbreviated.
3. Add wall-clock runtime numbers for at least one multi-step and one few-step model.
4. Add a brief prompt sensitivity analysis (e.g., vary the positive prompt for aesthetics across 3–5 phrasings and report variance in human preference scores).

## Calibration Report

**Round 1 bracketing anchors:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Towards Enhanced Controllability of Diffusion Models | 3.75 | 1 | Weaker: vague multi-method paper with unclear contributions |
| AccCtr | 3.50 | 1 | Weaker: limited scope, unclear improvement over prior work |
| Universal Guidance for Diffusion Models | 5.25 | 1 | The paper under review has broader validation and human eval |
| Momentum-driven Noise-free Guidance | 5.33 | 1 | Similar approach scope, but paper under review has broader validation |
| Revamping Diffusion Guidance (ICG/TSG) | 6.00 | 1 | Comparable: both propose guidance variants; paper under review has broader model/task coverage |
| Get What You Want (content suppression) | 6.00 | 1 | Comparable: both practical contributions with moderate novelty |
| Deconstructing Denoising Diffusion Models | 6.50 | 1 | Comparable: both empirical analysis papers with practical insights |
| Representative Guidance (RepG) | 7.33 | 1 | Stronger: more novel theoretical framing (coherence problem) |
| Rare-to-Frequent (LLM Guidance) | 7.50 | 1 | Stronger: more novel concept with LLM integration |

**Round 2 narrowing anchors:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Universal Guidance | 5.25 | 2 | Paper under review is stronger (broader validation, human eval) |
| Revamping Diffusion Guidance | 6.00 | 2 | Paper under review is comparable or slightly stronger |
| There and Back Again | 5.50 | 2 | Paper under review is stronger (clearer contribution) |
| Deconstructing Denoising Diffusion Models | 6.50 | 2 | Paper under review is comparable (empirical analysis + practical contribution) |
| ViCo | 5.50 | 2 | Paper under review is stronger |

**Round 1 bracket:** 5.5–7.0
**Round 2 narrowing:** The paper is clearly above Universal Guidance (5.25) and Revamping Diffusion Guidance (6.0), comparable to Deconstructing Diffusion (6.5), and below Representative Guidance (7.33). This places it at **6.5**.

## Score and Decision

The paper makes a solid empirical contribution with a genuinely useful finding about pooled embeddings and a practical training-free technique validated across many models and tasks. Its main weaknesses are moderate novelty (the core formula is CFG-like), some unresolved tension in the analysis, and structural evaluation issues (baselines in appendix, circular automatic metrics, missing runtime). These are real but not fatal. The breadth of validation and the clean COSMOS ablation are meaningful strengths that push it above typical guidance papers.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>