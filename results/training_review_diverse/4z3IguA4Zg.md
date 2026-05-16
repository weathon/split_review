Here is my consolidated final review:

---

## Summary

This paper investigates *why* MLLMs hallucinate and proposes a training-free decoding correction method (Deco). The key empirical finding is that MLLMs encode correct visual object information in their middle layers (20–28 out of 32), but this signal is suppressed by language-model priors in later layers, causing hallucinated tokens to overtake ground-truth tokens. Deco exploits this by dynamically selecting an early "anchor" layer where candidate tokens have highest probability, then interpolating that layer's logits into the final layer with a soft modulation coefficient. Experiments on InstructBLIP, MiniGPT-4, LLaVA-1.5, and Qwen-VL across CHAIR, POPE, MME, and GPT-4o evaluation show consistent hallucination reduction at ~1.2× latency overhead.

---

## Strengths

1. **Empirical insight into where and why visual information is lost.** The probing experiment (Section 2.1) shows that MLLMs achieve ~80% accuracy in predicting object existence from middle-layer representations, and the early-exit experiment (Section 2.2) pinpoints layers 20–28 as the region where ground-truth tokens are "activated" before being overtaken. The 91.05% overlap between hallucinated tokens and tokens predicted without any visual input directly implicates LM priors as the suppression mechanism. This goes beyond prior work by locating the phenomenon spatially (which layers) and attributing it causally (LM priors, not visual encoding failure).

2. **Simple, training-free, and demonstrably efficient.** Deco adds ~1.2× latency over the base decoder, compared to 1.8× for VCD and 5.1× for OPERA (Figure 3, Section 4.4). It integrates with greedy, beam, and nucleus sampling without retraining or external tools. This practical advantage is well-documented and non-trivial.

3. **Thorough evaluation across models, metrics, and decoding strategies.** The paper evaluates 4 MLLMs × 3 decoding strategies on CHAIR (image captioning), POPE (VQA), MME (comprehensive benchmark), and GPT-4o-assisted evaluation. The consistency of improvement across all settings (average 10.8% hallucination suppression on captioning) provides strong evidence for the method's generality.

4. **Ablations that validate the core design choices.** The perturbation experiment (Table 5) shows that randomly shifting the anchor layer by ±5 significantly degrades performance, confirming that dynamic selection is meaningful. The hyperparameter analysis for α and layer interval (Figure 4) aligns with the mechanistic finding and justifies the default choices.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Insufficiently disentangled comparison with DoLa.** Both DoLa and Deco use an earlier layer's logits to adjust the final layer, but with different selection criteria (DoLa: layer with maximum distributional divergence from final layer; Deco: layer where candidate tokens have highest probability). DoLa is included as a baseline but with its default hyperparameters designed for LLM factuality. The paper would be stronger with a direct ablation that replaces Deco's selection mechanism with DoLa's divergence-based criterion within the same pipeline (same backbone, same α weighting, same soft modulation). Without this, the marginal contribution of the selection mechanism is unclear. (The overall method still shows gains against DoLa as a black-box baseline, which is why this is minor rather than major.)

2. **Over-interpretation of probing results as "MLLM can see."** The title's question mark and the hedging ("to some extent," "a certain level of understanding") are appropriate, but the framing still risks anthropomorphizing the model. The probing experiment shows that object existence is *linearly decodable* from middle-layer representations at ~80% accuracy — not that the model "recognizes" objects in any agentive sense. The early-exit experiment is stronger on this front. The paper's rhetorical framing is effective but slightly outruns its evidence. The mechanistic analysis is a genuine contribution regardless; this is a presentation concern.

3. **Missing variance reporting for non-deterministic decoding.** Results for nucleus sampling and beam search (CHAIR, POPE) are not accompanied by standard deviations or multiple-seed runs. Since these are sampling-based procedures, single-run results are difficult to assess for statistical reliability. This is standard practice to report in this field and should be addressed.

4. **Candidate token definition in early-exit experiment may bias results.** The early-exit analysis (Section 2.2) defines candidate tokens via top-p (0.9) truncation from the *final* layer, then checks whether those tokens are "activated" in earlier layers. This filters to cases where the ground-truth token is already in the final layer's candidate set, potentially inflating the apparent support for the claim. The analysis is still informative, but the paper should explicitly discuss this conditioning.

5. **Limited discussion of failure modes.** The paper honestly notes a minor detailedness trade-off in GPT-4o evaluation (Section 4.2, Limitations) but does not analyze *when* Deco might fail — e.g., scenarios where the ground-truth token is not in the top-p candidate set, or where the selected anchor layer's highest-probability token is itself hallucinated (the 61.69% hit rate leaves ~38% of cases where it is not). A brief failure analysis would strengthen the paper.

6. **Per-model hyperparameter tuning is under-specified.** The paper states that α is set within [0.1, 0.6] and the layer interval is [20,28] based on experiments on LLaVA-1.5. It does not state whether these were tuned independently per model or kept fixed. If the latter, the results for InstructBLIP, MiniGPT-4, and Qwen-VL may be slightly suboptimal, which warrants discussion.

### Trivial

- The MME results are presented only as a bar chart (Figure 4) without numeric values. A small table with per-task scores would be more informative and standard for a conference paper.
- Section 2.1 does not discuss whether the probe classifier might exploit correlations with scene-level features (e.g., "beach" → "sand") rather than object presence. This is a standard concern for probing experiments; acknowledging it would strengthen the analysis.

---

## Nice-to-Haves

- A direct ablation comparing Deco's selection criterion against DoLa's divergence-based criterion within the same pipeline, as discussed above.
- Multi-seed variance reporting for all sampling-based results.
- A brief discussion of the conditioning issue in the early-exit candidate token definition.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- The Harsh Critic's statement "cannot be verified without the table (parser issue)" — the tables exist in the original submission but were stripped by the parser. This is not a paper flaw.
- Any concerns about "missing appendix sections" or "absent references" — these are parser artifacts.
- The Harsh Critic's comment about "the probe simply learning to correlate object labels with common image-level features" — this is a generic concern applicable to almost all probing studies; the paper's early-exit experiment provides converging evidence. I have moved this to Trivial rather than removing it entirely, as acknowledging it would indeed strengthen the paper.

---

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated claims and do not surface a genuinely novel interpretation that the paper itself misses.

---

## Suggestions

1. Add a direct ablation: replace Deco's candidate-token-based layer selection with DoLa's divergence-based selection on the same backbone models, keeping all other components (α, soft modulation) identical. Report CHAIR/POPE numbers for this variant. This cleanly separates the contribution of the selection mechanism from the rest of the pipeline.

2. Report CHAIR and POPE results for nucleus and beam search as mean ± std over at least 3 random seeds.

3. Add a brief failure analysis paragraph: under what conditions does the 61.69% hit rate fail (i.e., the selected token is not the ground truth), and what is the downstream effect on generated text?

4. Replace the MME bar chart with a table including numeric per-task scores.

5. Move the hedging from the intro ("to some extent," "a certain level") into the claim statements themselves — e.g., "representations in layers 20–28 linearly encode object presence" rather than "MLLMs can see."

---

## Score and Decision

**Originality:** The empirical finding — that visual information is robustly present in middle layers but suppressed by LM priors — is genuinely insightful and goes beyond prior characterizations. The method is a clean adaptation of the earlier-layer-correction idea to the MLLM setting with a new selection mechanism, which is solid though not paradigm-shifting.

**Importance of research question:** Hallucination in MLLMs is a central problem. Training-free, low-latency mitigation is practically valuable.

**Claims support:** Well-supported overall. The main claim (Deco reduces hallucination) is backed by consistent results across 4 models × 3 decoding strategies × multiple metrics. The mechanistic claim (layers 20–28 contain visual info later suppressed) is supported by converging evidence from probing and early-exit experiments, though the candidate-token conditioning issue slightly weakens it.

**Soundness:** Reasonable. The main gap is the DoLa comparison — the paper should more clearly separate Deco's contribution from DoLa's. The missing variance reporting is a standard concern. No fatal flaws.

**Clarity:** Well-written and well-motivated. The structure (mechanism → method → experiments) is logical.

**Value to community:** High. The mechanistic insight can inform future hallucination mitigation research. Deco is simple enough to be widely adopted.

Overall, the paper makes a credible, well-evaluated contribution. The weaknesses are addressable and none threaten the core claims.

**Score:** 7.5 / 10

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>