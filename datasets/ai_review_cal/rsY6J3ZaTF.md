- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Here is my consolidated review:

---

## Summary

DistillSpec proposes using white-box knowledge distillation to better align the draft model with the target model in speculative decoding (SD), yielding 10–45% speedups over standard SD. The paper provides a theoretical bound connecting on-policy TVD loss to acceptance rate, systematically ablates data sources (on-policy vs. off-policy) and divergence functions (FKL, RKL, JSD, TVD), extends to lossy SD, and demonstrates a model-garden strategy combining KD and SD for 6–10× latency reduction.

## Strengths

1. **Theoretical grounding linking on-policy KD loss to acceptance rate (Theorem 1, §4).** The paper proves that minimizing the on-policy (draft-generated) TVD loss ensures a lower bound on the expected sequence-level acceptance rate. This provides a principled justification for using the draft model's own generations during distillation, which is cleaner than prior heuristics.

2. **Consistent 10–45% wall-clock speedups over standard SD across multiple benchmarks (Figure 1, §5.1).** The gains are demonstrated under both greedy and temperature sampling on LM1B (decoder-only), XSum, CNN/DM, GSM8K (encoder-decoder). The improvements are substantial and directly attributed to DistillSpec.

3. **Systematic ablation of divergence functions and data sources for SD-specific KD (Figure 5, §5.2).** The paper compares four divergences and four data-generation strategies on two tasks, finding that the optimal recipe is task- and decoding-strategy-dependent. This nuanced finding goes beyond one-size-fits-all assumptions in prior KD-for-SD work and provides practical design guidance.

4. **White-box logit supervision is empirically shown to be vital for SD (Figure 2, §5.1).** Methods using the teacher's full logits (f-Distill, GKD) significantly outperform SeqKD, which uses only one-hot teacher labels. This justifies the white-box assumption and shows that the supervision signal matters beyond data source.

5. **Transferability of distilled drafts to unseen tasks (§5.1).** A draft distilled only on GSM8K improves average speedup on 23 BigBenchHard tasks from 1.93× to 2.21× (greedy) and 1.78× to 2.02× (temperature sampling), demonstrating generalization beyond the distillation task.

6. **Practical model-garden strategy with 6–10× latency reduction (Figure 7, §5.3).** By first distilling a large teacher into a smaller target and then applying DistillSpec to train an even smaller draft, the paper achieves dramatic latency reductions (6.4× on XSum, 10.7× on GSM8K) with minimal performance degradation. This is a practically useful recipe.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No statistical uncertainty reported for key comparisons.** Throughout the paper, block efficiency and speedup results are presented as point estimates without error bars, confidence intervals, or statements about variance across runs. This is especially relevant for fine-grained comparisons (e.g., "JSD slightly outperforms the other divergences on XSum with greedy"), where the reader cannot assess whether observed differences are meaningful or within noise. While single-run evaluation is common in this literature, the paper's specific design recommendations would be strengthened by multiple seeds.

2. **Reported cost ratios $c$ (draft/target forward-pass time) are absent.** The expected speedup formula is $\tau / (c\gamma + 1)$, and $c$ is critical for interpreting whether the observed block efficiency gains translate to latency improvements. The paper reports latency speedups but never provides the measured $c$ values for any model pair or task. This makes it harder for practitioners to gauge generalizability to their own hardware setups.

3. **Lossy SD evaluation is limited to one task (GSM8K, Figure 6).** The paper claims "fine-grained control over the quality-latency trade-off" via lenience functions, but the evidence is restricted to a single math reasoning dataset. Adding at least one more task (e.g., XSum) would substantially strengthen this claim.

4. **Theorem 1 bound is linear in $T$ and may be loose in practice; no empirical verification is provided.** The bound $1 - T\epsilon$ becomes vacuous for longer sequences unless $\epsilon$ is extremely small. The paper does not check how tight this bound is for trained models (e.g., by computing actual acceptance rates vs. the bound). This is not a requirement, but acknowledging the looseness would contextualize the theoretical contribution more honestly.

5. **The recipe analysis offers limited actionable guidance.** The honest finding that divergence choice is "task- and decoding-strategy-dependent" and should be treated as a hyperparameter (§5.2) is a limitation worth further discussion. The paper could at least note whether certain divergences consistently dominate or underperform across settings to help narrow the search space.

### Trivial

None.

## Nice-to-Haves

- In the model-garden results (Figure 7/8), it would be informative to include an ablation curve: "DistillSpec without target distillation" (i.e., use the raw target and only distill the draft). The 6–10× improvement is presented as a combined strategy; decomposing the contribution of target distillation vs. draft alignment would strengthen the analysis.

- The TVD optimization failure (§5.2 recommendation) is noted but not analyzed. A small diagnostic — e.g., training loss vs. validation block efficiency for TVD vs. FKL — would make this observation more informative.

## Removed Points

- **"Ambiguity in baseline draft model status" (from harsh critic, Critical Issue 1):** The paper states (line 152) that "T5 v1.1 models [are] fine-tuned on four different tasks, with T5-XL (3B) and T5-Small (77M) serving as the target and draft models, respectively." The phrasing "models fine-tuned" applies to both model sizes, so the standard SD baseline uses a task-fine-tuned draft model. The comparison against DistillSpec is therefore comparing task-fine-tuned draft vs. task-fine-tuned + KD-from-target draft, which is fair. The concern that the improvement could reflect "any task-specific training" is further contradicted by the paper's own results: SeqKD also provides task-specific training but underperforms DistillSpec, showing that the specific KD signal matters. This criticism is factually incorrect based on the paper's text. **Moved to Removed Points.**

- **"Model-garden headline claim conflates two separate effects" (from harsh critic, Critical Issue 3):** The paper explicitly frames the model-garden result as a *combined strategy* (lines 28–29, 196–202), not as a claim that DistillSpec alone delivers 6–10×. The comparison against "standard decoding without distillation" is an honest practical baseline. The critic's request to "decompose the contribution" is a nice-to-have ablation, but presenting the combined result as a "methodological gap" or "overstatement" misrepresents the paper's framing. **Moved to Removed Points** (relegated to Nice-to-Haves above as a constructive suggestion).

- **"Absence of draft model size ablation"** (from harsh critic, "Missing Parts"): The paper uses one draft size per family (33M for GPT, 77M for T5). Requesting additional draft sizes is a generic "more experiments" request that does not undermine the existing claims. The paper's contribution does not depend on showing the effect across multiple draft sizes. **Moved to Removed Points.**

- **Strength Finder's generic/superficial strengths:** The strength finder's list was checked against the paper. All listed strengths are concrete, evidence-backed, and specific to the paper's contributions. None were removed as generic or sycophantic.

## Novel Insights

The reviews surface a useful meta-point that the paper itself does not fully articulate: there is a fundamental tension between the theoretically-motivated objective (minimizing TVD, which directly governs acceptance rate) and the empirical finding that TVD minimization does not consistently yield the best performance. This raises an interesting question about optimization landscape mismatch — TVD may be the right evaluation metric but a poor training objective due to plateau gradients or sensitivity to distribution shape. The paper notes this observation but does not probe it. A follow-up investigating *why* this mismatch occurs (e.g., analyzing training loss trajectories, gradient properties of different divergences on the acceptance rate) would be a valuable extension.

## Suggestions

1. Add error bars (3–5 seeds) to the key block efficiency comparisons in Figures 2 and 5 to support the specific divergence recommendations.
2. Report the measured cost ratio $c$ for each model pair and hardware setup, enabling practitioners to assess generalizability.
3. Extend the lossy SD evaluation to at least one additional task (e.g., XSum) beyond GSM8K.
4. Add a brief empirical check of Theorem 1's tightness — compute actual acceptance rates vs. the bound for a trained model — to calibrate the theoretical contribution.
5. Include an ablation in the model-garden experiments that isolates DistillSpec's contribution from target KD's contribution.
