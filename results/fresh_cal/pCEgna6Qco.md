Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper identifies **format specialization** — where an LLM overfits to the constrained output format of a fine-tuning task (e.g., only emitting "True"/"False") — as a key cause of lost in-context learning (ICL) ability during fine-tuning. The authors show that format learning occurs at the very beginning of fine-tuning through a gradient alignment analysis, and propose **ProMoT** (Prompt Tuning with MOdel Tuning), a two-stage framework: first, a soft prompt is trained to absorb the task format while the model is frozen; second, the model is fine-tuned with the prompt frozen. Experiments on mT5 XXL across RTE, WMT14 En-Fr, and 8 evaluation tasks show that ProMoT preserves or improves average ICL performance (e.g., Norm. Avg. +2.58 on RTE, +1.35 on En-Fr, +8.35 in multi-task setting) while matching or exceeding standard fine-tuning on the supervised task.

## Strengths

1. **Identifies format specialization as a distinct mechanism of ICL loss and shows it occurs early.** Section 3 provides converging evidence: (a) ICL accuracy on QA collapses during RTE fine-tuning (Figure 1); (b) output fraction of "True"/"False" on TriviaQA reaches 90%+ within 300 steps (Figure 2); (c) cosine similarity between full and format-only gradients is high at initialization and drops to ~0.2 at step 400, confirming format learning precedes semantic learning (Figure 3).

2. **ProMoT preserves or improves average ICL performance while matching supervised accuracy.** Table 1 shows ProMoT achieves comparable or better supervised scores (e.g., RTE 92.78% vs. 92.06% for standard FT). Table 2 shows standard RTE fine-tuning drops Norm. Avg. from 17.52 to 15.43 (1-shot), while ProMoT raises it to 20.10 (+2.58) and ProMoT+1-shot to 22.26 (+4.74).

3. **Demonstrates surprising cross-task generalization across dissimilar formats.** ProMoT on RTE (binary NLI) improves summarization (XSum Rouge-2 from 6.41 to 7.02, vs. 0.00 for standard FT). ProMoT on En-Fr translation boosts WMT16 En-De from 3.97 to 15.55 and En-Ro from 1.82 to 17.80, where standard FT collapses to near zero. This semantic transfer across task formats is a novel finding.

4. **Multi-task results are compelling.** Table 4 shows Multi-ProMoT achieves Norm. Avg. 25.88 vs. 20.06 for standard multi-task FT (+8.35 improvement), substantially exceeding the +2.54 from standard multi-task FT alone. This is where the method's value is clearest.

5. **Ablation study cleanly isolates the benefit of the two-stage design.** Table 5 shows that joint fine-tuning, fine-tuning with a 1-shot natural language prompt, and fine-tuning with a random fixed prompt all fail to preserve ICL (e.g., TriviaQA 0.75, 0.03, 0.83 vs. ProMoT 17.82), confirming the staged decoupling is essential.

## Weaknesses

### Fatal

None.

### Major

- **The gradient analysis demonstrating that "format learning happens first" is conducted on only one task (RTE, a binary classification task).** While the behavioral evidence (format specialization causing ICL loss) is supported across multiple fine-tuning tasks in the experiments, the causal timing claim — that format learning front-loads and can be captured via prompt tuning — derives from a single gradient-alignment experiment. A generative task like WMT14 En-Fr might exhibit a different specialization pattern (e.g., output length collapse or language-id fixation) that the RTE gradient analysis does not capture. Replicating this experiment on at least one more task would substantially strengthen the generality of the diagnosis that motivates ProMoT.

### Minor

- **The claim that the soft prompt "absorbs format" while model fine-tuning learns "semantic skills" is not directly verified.** The paper infers this mechanism from three pieces of circumstantial evidence (prompt-tuning achieves reasonable performance, joint fine-tuning fails, ProMoT works). The authors acknowledge this uncertainty in the conclusions ("no theoretical guarantee on how much format specialization can be absorbed by the soft prompt"). A direct check — e.g., feeding random inputs through the frozen model + prompt and measuring format-specific output statistics — would confirm the narrative. Without it, the explanation remains plausible but untested.

- **The baseline set omits simple regularization methods that could achieve similar effects.** Comparisons to L2-regularized fine-tuning, KL divergence against the pretrained model, or elastic weight consolidation (EWC) would help determine whether ProMoT's benefit is specific to format absorption or merely a side effect of limiting parameter deviation. The joint fine-tuning ablation (same total parameter count) partially controls for this, but does not fully separate format absorption from general regularization.

- **The paper states that prompt-tuning works better than LoRA for absorbing format (Section 4) but provides no empirical evidence for this claim.** This assertion appears without any LoRA comparison in the results. If the authors intend to make this claim, they should show the comparison.

- **Statistical significance is not reported.** Given small evaluation sets (e.g., CB has 56 examples), some reported differences (e.g., 66.07 vs. 73.21 on CB) may not be reliable without confidence intervals or significance tests.

### Trivial

- **The gradient analysis reports only two time points (step 0 and step 400).** A curve over more intermediate steps would more clearly resolve the trajectory of format vs. semantic learning and rule out the possibility that alignment degrades gradually.

## Nice-to-Haves

- **Direct verification of soft prompt behavior:** Show that the frozen model with only the learned prompt produces format-consistent outputs (e.g., "True"/"False") on out-of-distribution inputs. This would confirm the format-absorption story.
- **Prompt length ablation:** The paper does not analyze how the prompt dimension \(p\) affects the format-vs.-semantics trade-off. A study varying \(p\) would provide practical guidance and mechanistic insight.
- **Inclusion of a task sharing format but not semantics with the fine-tuning task** (e.g., sentiment classification when fine-tuned on RTE) would help disentangle format generalization from semantic generalization.

## Removed Points

These points were identified by the reviewers but are removed from the main assessment for the following reasons:

- **"No comparison to FLAN-T5"** — Removed because the paper explicitly explains this exclusion (FLAN-T5 was fine-tuned on evaluation datasets). This is a deliberate methodological choice, not an oversight.
- **"The gradient analysis may depend on the specific batch chosen"** — Removed as speculative. The paper states gradients are computed on "the same batches" without specifying "the first batch," and there is no evidence that batch choice invalidates the result.
- **"Format learning continuing vs. stopping"** — Removed because the paper's claim is that format learning happens *first*, not that it stops; the data at step 400 (high True/False ratio, low alignment) already supports the intended claim.
- **"The improvement on summarization is modest"** — This is a factual observation about the magnitude of results, not a weakness. The paper claims ProMoT "can enhance" generalization, which is supported.
- **"Duplicate Table 2"** — Parser artifact from PDF extraction; not present in the original submission.
- **"Missing hyperparameters"** — These details were in the appendix (stripped by the parser); they exist in the original submission.
- **Generic or unfalsifiable reviewer assertions** about "could the metric measure a proxy" or "confounders" without specific anchoring to paper content have been removed.

## Novel Insights

None beyond the paper's own contributions. The key novel angle — that format specialization is a distinct, early-occurring phenomenon separable from semantic learning via prompt-tuning priors, and that this decomposition unlocks cross-format generalization — is already well-articulated by the authors.

## Suggestions

1. **Replicate the gradient-alignment experiment on a generative fine-tuning task** (e.g., WMT14 En-Fr, measuring alignment of format vs. randomized-format gradients). This would directly address the main generality concern.
2. **Add a simple regularization baseline** (e.g., fine-tuning with a KL penalty against the pretrained model) to demonstrate that ProMoT's advantage is not merely a side effect of constraining model change.
3. **Provide a direct behavioral analysis of the soft prompt's role** — e.g., freeze the model after Stage 2, remove the prompt, and show that the model reverts to format-agnostic outputs, or use only the prompt on random inputs to show format-specific output patterns.
4. **Include confidence intervals** for the few-shot evaluation scores, especially on small datasets like CB.
5. **Either provide the LoRA comparison or remove the unsupported claim** that prompt-tuning outperforms LoRA for format absorption.

## Score and Decision

This is a solid paper with a clear problem identification, a well-motivated and simple method, and generally supportive experimental evidence. The main weaknesses — that the gradient analysis underlying the causal diagnosis is limited to one task and that the prompt-absorbs-format mechanism is not directly verified — are real but do not invalidate the core contribution. The experimental results showing ProMoT's effectiveness, particularly in the multi-task setting (Table 4), are compelling. The paper makes a practical contribution to an important problem (ICL loss during fine-tuning) and provides a clean framework that others can build on.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>