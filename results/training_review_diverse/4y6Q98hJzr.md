Now I have a complete picture. Let me write the final consolidated review.

## Summary

This paper documents a "stability gap" — a V-shaped performance curve (initial drop, then recovery) — during domain continual pre-training of LLMs, an important and under-explored phenomenon. The authors adapt the plasticity/stability gradient framework from vision continual learning to explain this effect and propose three practical strategies to mitigate it: (I) training on a smaller subset for multiple epochs instead of the full corpus for one epoch, (II) selecting the highest-quality subset, and (III) maintaining a pre-training-like data mixture ratio. Experiments on OpenLlama-3B and TinyLlama show that these strategies accelerate recovery and improve peak performance using 60% fewer tokens than full-corpus baselines. Applied to Llama-3-8B, the resulting model (Llama-3-Physician) achieves strong medical benchmark results competitive with GPT-4.

## Strengths

- **Novel empirical discovery of the stability gap in LLM continual pre-training.** The V-shaped performance curve (Figure 2(a)) is documented consistently across model scales (OpenLlama-3B, TinyLlama-1.1B) and domains (medical, legal). This is a genuine finding that challenges the tacit assumption that continual pre-training yields immediate gains, and it gives practitioners a new understanding of what to expect during training.

- **Practical, compute-efficient strategies with clear validation on OpenLlama-3B.** The three strategies are intuitive, grounded in the stability-gap framing, and convincingly shown to accelerate recovery and improve peak performance (Table 1: 36.2% → 40.7% average medical accuracy using 20B tokens vs. 50B for all baselines). Figure 4(a) directly shows the recovery speed advantage of quality-selected multi-epoch training over the single-epoch full-corpus baseline. The ablation analysis (Section 5.2) on learning rates and subset sizes provides actionable guidance.

- **Strong results when deployed on Llama-3-8B.** Llama-3-Physician achieves the best medical performance among open-source models of similar scale (Table 2, Table 3) and is competitive with GPT-4 on several benchmarks (Figure 1). This demonstrates the practical utility of the strategies beyond the proof-of-concept 3B experiments.

- **Extension to instruction tuning.** Figure 5 shows that the same stability-gap phenomenon and strategy principles apply to instruction tuning, where using 25% of instruction data (quality-selected + mixed with general instructions) achieves the best performance across diverse medical tasks.

## Weaknesses

### Fatal

None.

### Major

- **No general task performance evaluation for Llama-3-Physician — the "no forgetting" claim is unverifiable for the main model.** The title promises "No Forgetting" and the abstract explicitly states that the strategies "enhance the average general task performance without causing forgetting." However, this claim is verified only for OpenLlama-3B (Figure 3a, on commonsense tasks). For the highlight model, Llama-3-Physician, Section 5.3 reports *only* medical task accuracy and perplexity. We learn that "the average medical performance drops slightly" for Llama-3 after continual pre-training (line 111), which itself is a concerning signal, but we are given no general-domain evaluation — no MMLU overall, HellaSwag, GSM8K, or any other general benchmark. Without this, the paper's central narrative ("Efficient and No Forgetting") is unsupported for its flagship result. This is the most consequential gap: the paper would be significantly stronger if it either included general-task numbers for Llama-3-Physician or scoped its claims explicitly.

- **Missing compute-matched baseline in Table 1 conflates strategy effects with reduced compute.** Table 1 compares "Our strategies" (20B tokens: 5B subset × 4 epochs) against baselines that all use 50B tokens. This conflates two factors: the strategies themselves and the reduced compute budget. A reader cannot tell whether simply training on 20B tokens (random subset, single epoch) would achieve similar results. While "5b Random" and "5b HQ" appear in Figure 4(a), they are multi-epoch (5 epochs, 25B tokens), not a direct compute-matched single-epoch control. The paper would be strengthened by adding a 20B-token, single-epoch, random-subset baseline to Table 1.

### Minor

- **The stability gap mechanism is claimed more strongly than the evidence supports.** The paper presents the plasticity/stability gradient explanation as the *explanation* rather than a *hypothesis* consistent with the data. The supporting evidence is indirect: (a) general tasks also show a V-shaped curve (Figure 3a), and (b) bottom layers update more than top layers early in training (Figure 3b). Neither observation directly measures the plasticity or stability gradient, and the weight-update analysis has alternative explanations (e.g., bottom layers simply adapt faster to new domain statistics). The authors use hedging language ("hypothesize," "infer") in some places but then claim "This suggests that the top layers' weights indeed lack sufficient stability gradient" (line 68), overstating the certainty. Reframing this as a plausible conceptual motivation rather than a verified mechanism would better match the evidence.

- **Strategy III implementation for Llama-3 is not specified.** Strategy III (pre-training-like data mixture) relies on knowing the pre-training data mixture rate, which is available for OpenLlama (based on Llama-1) but unknown for Llama-3. The paper acknowledges this (line 111: "likely due to the unknown data mixture rate of Llama-3") but never explains what approximation was used. Did the authors assume a default ratio? Use the OpenLlama mixture as a proxy? Omit Strategy III? This ambiguity undercuts the claim that "our three strategies" were faithfully applied to the main result.

- **No statistical significance or variance reported.** No standard deviations, confidence intervals, or multiple-seed runs are reported for any experiment. Given the modest margins over strong baselines in Table 1 (e.g., 40.7% vs. 39.4% for 20% replay — a 1.3-point gap), it is unclear whether these differences are reliable. This is standard practice for many LLM benchmark papers, but the modest margins make variance information particularly relevant here.

- **Instruction tuning experiment design is underspecified.** The "25% instruction data" experiment with 25% of the full instruction data's tokens (Figure 5 caption) presumably uses fewer epochs on a subset, but this is never explicitly stated relative to the 3-epoch full-data baseline. If the 25% experiment uses 3 epochs on 25% of the data, the total tokens are 75% of the full baseline, not 25%. If it uses proportionally fewer epochs, the number of passes over the seen data differs. Clarification is needed.

- **Modest margins over strong baselines.** While Table 1 shows a 4.5-point improvement over the base model, the improvement over the re-warming/re-decaying baseline (38.7%) is 2.0 points, and over 20% replay (39.4%) is 1.3 points. These are meaningful but modest, which makes the missing variance information and compute-matched baselines more important for interpretation.

### Trivial

None.

## Nice-to-Haves

- A direct comparison of Strategy II (quality selection via KenLM perplexity) against other data selection methods (e.g., Lin et al., 2024) would strengthen the claim that the specific quality metric matters. However, the current baselines (random vs. HQ vs. full corpus) already tell a clear story.

- For the weight-update analysis (Figure 3b), examining attention heads and MLP layers separately, or reporting gradient norms directly, would make the mechanism argument more convincing.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The initial performance drop is asserted rather than tested" (harsh critic's overall framing).** This is weakened because the paper explicitly uses "hypothesize" (lines 4, 18) and frames the supporting evidence as "consistent with" the explanation. However, some later claims (e.g., "indeed lack sufficient stability gradient," line 68) overstate certainty. The substantive concern (indirect evidence) is kept as a Minor weakness above.

- **"Comparison to existing continual pretraining methods beyond the small set in Table 1" (harsh critic's missing parts).** This is a request for additional baselines that the paper could not reasonably be expected to exhaust (data selection, architectural methods). The current baseline set (re-warming, replay, freezing) covers the most directly relevant approaches for the paper's setting. This is scope creep.

- **"Missing evaluation of general ability after continual pretraining on the main model" (the critic frames this as "most critical missing piece").** This is kept in full as a Major weakness above — it is valid and important.

- **"The paper should discuss whether the task format itself (multiple-choice) is a confound"** (critic's section notes on Figure 2(c)). This is speculative. The perplexity is measured on medical Wikipedia text, while task accuracy is on multiple-choice QA — these measure different things by design. The V-shape in accuracy and monotonic drop in perplexity are not contradictory findings.

## Novel Insights

The harsh critic correctly identifies the most critical gap (no forgetting evaluation for Llama-3-Physician) and the most significant methodological concern (missing compute-matched baseline). The strength finder correctly highlights the core empirical discovery, the practical value of the strategies, and the SOTA results. The most interesting tension across the reviews is about the stability gap mechanism: the strength finder takes the paper's evidence (general task V-shape + weight update analysis) at face value as "empirical verification," while the harsh critic correctly notes that this evidence is indirect and does not rule out alternative explanations. The paper's real contribution is the empirical phenomenon and the practical strategies — the mechanism is a plausible conceptual frame that helps organize the strategies but is not independently validated. A revision that weakens the mechanistic claims while strengthening the missing evaluation would resolve this tension cleanly.

## Suggestions

1. **Add general task performance for Llama-3-Physician.** This is the single highest-impact improvement. Report accuracy on 3–5 standard general-domain benchmarks (e.g., MMLU overall, HellaSwag, GSM8K, ARC-Challenge) before and after continual pre-training. Without this, the title claim of "No Forgetting" is unsubstantiated for the paper's main model.

2. **Add a compute-matched baseline to Table 1.** Include a 20B-token, single-epoch, random-subset baseline. This will isolate the effect of the multi-epoch strategy from the effect of reduced compute, and it already exists in spirit in Figure 4(a) with slight modification.

3. **Clarify Strategy III for Llama-3.** State explicitly what data mixture rate was used (e.g., assumed the same as OpenLlama, or omitted the strategy, or used a heuristic). If unknown, present results with and without Strategy III to show its impact.

4. **Temper the stability gradient claims.** Replace "indeed lack sufficient stability gradient" with "consistent with the hypothesis that top layers initially lack sufficient stability gradient." The practical strategies do not depend on the mechanism being proven.

5. **Report variance or multiple seeds** for at least the main comparison table, given the modest margins over strong baselines.

## Score and Decision

The paper reports a genuine and useful empirical finding (the V-shaped stability gap), proposes practical strategies with clear benefits on the 3B model, and achieves strong medical results on Llama-3-Physician. However, the missing forgetting evaluation for the flagship model and the incomplete baseline comparison are significant gaps that prevent acceptance in the current form. The paper can become a solid accept after these are addressed.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>