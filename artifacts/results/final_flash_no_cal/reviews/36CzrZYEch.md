Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes IRIS, a reinforcement learning framework for autoregressive text-to-image (T2I) models that uses *negative self-certainty* (NSC) — the forward KL divergence between the model's output distribution and a uniform distribution — as an intrinsic reward, requiring no external human labels, domain-specific verifiers, or preference data. The paper makes the counterintuitive observation that, unlike in text reasoning where maximizing self-certainty helps, minimizing self-certainty improves T2I generation (producing more visually rich images). Experiments on Janus-Pro 1B/7B models across GenEval, T2I-CompBench, and WISE show that IRIS achieves performance competitive with external-reward baselines (T2I-R1), while using only the model's own internal signal.

## Strengths

1. **Competitive T2I alignment without any external supervision.** Table 1 shows that Janus-Pro-1B + IRIS achieves scores of 0.72, 0.3793, and 0.37 on GenEval, T2I-CompBench, and WISE respectively, closely matching the external-reward baseline T2I-R1 (0.75, 0.3820, 0.38) and substantially outperforming the base model (0.66, 0.3338, 0.28). This is the paper's central contribution and the evidence is clearly presented. The 7B results (0.77 vs 0.78 on GenEval) further demonstrate scalability.

2. **Comprehensive ablation study validating the core design choices.** Four tightly designed ablations directly support the paper's claims: (a) Fig. 6 shows that minimizing image SC consistently outperforms maximizing it, (b) Fig. 7 shows that minimizing text SC outperforms maximizing it, (c) Fig. 8 shows forward KL (self-certainty) is superior to backward KL (entropy), and (d) Fig. 9 shows that RL-based optimization (GRPO) is necessary — direct NSC optimization leads to model collapse. These ablations are internally consistent and clearly presented.

3. **Semantic CoTs are shown to benefit intrinsic-reward training.** Fig. 5 demonstrates that IRIS with CoT consistently outperforms IRIS without CoT across all four external reward metrics (HPSv2, GIT, GDino, ORM), showing that the intrinsic reward framework leverages CoT reasoning to further improve generation quality.

4. **The observation of task-dependent self-certainty behavior is interesting and potentially impactful.** The finding that minimizing (rather than maximizing) self-certainty benefits T2I — opposite to text-reasoning results — is a genuine contribution that could inform future work on modality-specific RL alignment.

## Weaknesses

### Fatal
None.

### Major

1. **Best-checkpoint selection on test benchmarks inflates reported results and weakens reliability.** The paper explicitly states (Sec. 4.2, Table 1 caption) that it reports "the best result of different methods among the checkpoints from 100 step to 800 step on the three benchmarks," selected via "the best checkpoint (measured by the average performance)." This is a form of test-set overfitting: the test benchmarks are used for checkpoint selection rather than a held-out validation set. The learning curves in Fig. 3 show non-trivial fluctuation (e.g., WISE scores for IRIS peak and then decline), so the best-checkpoint numbers are optimistic. While both IRIS and T2I-R1 are evaluated under the same protocol (so the relative comparison is less affected), the absolute improvement percentages (9.1%, 13.3%, 28.8%) are not representative of expected performance at a fixed training budget. The paper should report final-step performance (visible in Fig. 3 but not in Table 1) and use a validation split for checkpoint selection. Without this, the headline numbers cannot be taken at face value.

### Minor

1. **Number of training seeds and variance decomposition are unspecified.** The paper reports ± values in Table 1 but never states whether these reflect variance across multiple training runs (seeds), across evaluation samples, or something else. The base model scores are reported without any variance, making it impossible to judge statistical significance. Given the known high variance of RL fine-tuning, multi-seed experiments with explicit reporting would substantially strengthen the evidence. The ablation studies (Figs. 5–9) appear to be single runs without error bars, so observed differences between conditions could partially reflect noise.

2. **The observation motivating the method (Fig. 2) confounds model architecture, task, and modality.** Fig. 2 compares Qwen2.5-1.5B-Instruct (text reasoning) with Janus-Pro-1B (image generation) — two different models, trained on different tasks, with different external rewards. The paper does not demonstrate the self-certainty trend within a single model family (e.g., Janus fine-tuned on a text-reasoning task vs. a T2I task) or control for confounds. This does not invalidate the method (the ablation studies provide the main evidence), but the motivating observation is weaker than the paper's rhetoric suggests.

3. **Analysis of why minimizing text self-certainty helps is shallow.** The paper claims minimizing text SC in semantic CoTs "encourages exploration" and "facilitates better exploration during training" (Sec. 3.2), but provides only a brief speculative explanation and one ablation run (Fig. 7). Quantitative analysis of CoT properties (e.g., token diversity, length, distinct n-grams, relevance to prompt) is absent. This gap weakens the justification for a central design choice.

4. **Figure 2's dual y-axis with different scales is visually misleading.** The left y-axis (text SC, range 31–38) and right y-axis (image SC, range 18.75–20.50) use different scales, making the magnitude of the two trends incomparable at a glance. While the direction of change is what matters, the presentation could mislead readers about effect sizes.

### Trivial
None.

## Nice-to-Haves

- **Report final-step performance alongside best-checkpoint results in Table 1**, to give readers a sense of training stability.
- **Report wall-clock time or FLOPs** to help readers assess the practical trade-offs between IRIS (which requires no external reward model evaluation) and external-reward methods.
- **Quantitative analysis of CoT diversity** (e.g., distinct n-grams, length, entropy over training) would strengthen the claim that minimizing text SC drives exploration.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Missing training data description"** — The paper states it follows the protocol of T2I-R1, and further details (dataset source, prompt count, overlap with benchmarks) are likely in the appendix (Appx. B.1, stripped by the PDF parser). Per guidelines, criticisms about missing appendix content are removed.

2. **"External-reward baseline re-implementation unclear"** — The paper explicitly states "We will use the four external reward models to train the multimodal LLM as the baseline (T2I-RI)" (Sec. 4.1), clearly specifying the four models (HPSv2, DINO, GIT, ORM). This claim is factually incorrect and removed.

3. **"Inherent advantage of T2I-R1 on ablation metrics"** — The paper explicitly notes that the four external reward models are used only as *evaluation* metrics for ablations on IRIS variants, and "we never use these reward models in the training objectives" (Sec. 4.3). The criticism overlooks this explicit addressal.

4. **Various presentation nitpicks** (brief explanation of forward KL, anecdotal qualitative examples, scope discussion) — These are either standard brevity for a conference paper or observations the paper acknowledges.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the evaluation protocol:** Use a held-out validation set for checkpoint selection (or report final-step performance) and run all main experiments with at least 3 seeds, reporting means and standard deviations.
2. **Strengthen Fig. 2's observation** by showing the self-certainty trend within a single model (e.g., Janus-Pro fine-tuned on a text-reasoning task vs. T2I), or at minimum acknowledge the confound.
3. **Add quantitative analysis of CoT properties** (diversity, length, entropy) to support the claim that minimizing text SC drives exploration.
4. **Include the training dataset description** in the main paper (number of prompts, source, overlap with evaluation benchmarks) — this may already be in the appendix but should be elevated for accessibility.

## Score and Decision

The paper makes a genuinely novel contribution — using negative self-certainty as an intrinsic reward for T2I alignment, with a well-designed set of ablations that validate the core ideas. The main weakness is the best-checkpoint-on-test-set evaluation protocol, which inflates the reported numbers and is a clear methodological concern. However, the learning curves (Fig. 3) and the fact that both IRIS and the baseline are evaluated under the identical protocol indicate that the core finding (IRIS achieves competitive performance without external supervision) is robust, even if the precise percentages are optimistic. With the evaluation issues addressed, this paper would be a solid contribution to the community. I recommend acceptance but with a strong suggestion to fix the evaluation protocol in the final version.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>