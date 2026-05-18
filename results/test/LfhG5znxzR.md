Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces **codebook features**, a method that inserts vector quantization bottlenecks into pretrained neural networks to produce sparse, discrete hidden states. The output of each layer is replaced by the sum of the top-\(k\) most similar code vectors from a learned codebook. The method is validated in two settings: (1) a controlled finite-state machine (TokFSM) task where the latent states are known, and (2) transformer language models up to 410M parameters trained on TinyStories and WikiText-103. The paper shows that codes can be more interpretable and causally controllable than raw neuron activations, and that topic-level steering is achievable by activating identified topic codes during generation.

## Strengths

1. **Strong causal evidence in the controlled FSM setting.** Changing MLP-layer state codes to those of a different FSM state shifts the next-state distribution to nearly match the target state (normalized JSD ≈ 0.0; Figure 3b). This is a clean interchange intervention that establishes a direct causal mapping between specific codes and model behavior, going well beyond correlational analysis.

2. **Demonstrates that networks can operate under extreme sparsity with modest degradation.** On TokFSM, a \(k=1\) attention-only codebook model achieves 96.39% state accuracy vs. 96.77% for the original (Table 1). On TinyStories, the MLP \(k=100\) codebook model ties or slightly exceeds the finetuned baseline (loss 1.57, accuracy 59.47% vs. 59.27%). These results show that the dense continuous activation paradigm is not strictly necessary for strong performance.

3. **Codes substantially outperform neurons as interpretable units in the controlled setting.** On TokFSM, state codes achieve 97.1% average precision at state classification vs. 70.5% for the best neuron (Figure 2a). Since the FSM states are independently defined by the task structure (not by the codes), this comparison is clean and the margin is striking.

4. **Practical topic steering with large, interpretable effect sizes.** Activating all topic codes in attention heads raises target-topic frequency from single-digit baselines to 75–100% across multiple topics (Table 4), with qualitative generations that are coherent and natural (Table 3). This provides a concrete demonstration of inference-time control using the discovered codes.

5. **End-to-end training through discrete bottlenecks in deep networks.** The paper successfully trains codebooks across models up to 24 layers deep using straight-through estimators and a reconstruction loss with stop-gradient (Section 2.1), showing that the method scales to modern architectures.

## Weaknesses

### Fatal
None.

### Major

1. **LM topic steering lacks necessary control conditions.** The authors activate topic codes and measure topic frequency increases (Table 4), but do not report control interventions such as activating random codes, activating codes from a *different* topic, or adding noise to the codebook selection. Without these controls, it is difficult to fully attribute the observed shift specifically to the semantics of the chosen codes — the effect could partly stem from a generic "nudge" from any deviation. The FSM experiments (Section 3.2) included a proper counterfactual (swapping to a different state's code) and are much stronger for it; the LM experiments do not replicate this rigor. The qualitative evidence (coherent topic-specific generations even under the aggressive "all codes" intervention) is suggestive and partially mitigates this concern, but a formal control would significantly strengthen the causal claim.

2. **The interpretability comparison for the LM experiments has selection bias.** In Section 4 (lines 240–242), the authors first identify codes with simple, interpretable activation patterns, then create heuristic regular expressions targeting the features those codes fire on, and finally compare code precision against the best-thresholded neuron. Because the feature definition is derived from the code's behavior, the comparison systematically favors codes over neurons. This limits the generalizability of the "30% higher average precision" claim to the specific, code-defined features studied. The FSM experiment (where features are independently defined by the task) does not have this issue and still shows a large gap (97.1% vs. 70.5%), so the bias does not invalidate the overall claim, but the LM-specific comparison should be interpreted cautiously or the claim should be bounded explicitly.

### Minor

1. **Performance degradation is understated in the paper's framing.** The paper states that codebook models "can still achieve strong language modeling performance" and can be "close to or better than the original models with the proper settings." However, the attention-only \(k=8\) model on WikiText (the model used for the main analyses) has loss 2.74 vs. the finetuned baseline's 2.41 — a non-trivial gap. On TinyStories, the same \(k=8\) attention model (loss 1.66 vs. 1.57 finetuned) is also worse. The comparison to the 160M model on WikiText (loss 2.72, roughly matching the \(k=8\) codebook model) further suggests the bottleneck effectively reduces useful capacity. The data are presented transparently in Table 2, but the text's framing could be more precise about the performance trade-off.

2. **No analysis of code interaction for \(k>1\).** The LM experiments use \(k=8\), meaning each codebook output is the sum of 8 codes. The paper does not study whether these codes interfere, whether the sum remains interpretable, or whether activating a topic code alongside unrelated codes dilutes its effect. The "all codes" intervention (replacing all \(k\) codes with copies of one code) sidesteps this by ignoring the other codes, but the "single code" intervention (replacing just the lowest-scoring code) implicitly assumes the other codes are irrelevant, which is not justified.

3. **Generation evaluation is limited to topic presence.** The quantitative evaluation in Table 4 uses only a word-based classifier to detect whether the topic appears in the generated text. No metrics for fluency, diversity, or overall generation quality (e.g., perplexity of generated text, human evaluation) are reported. The qualitative examples appear reasonable, but systematic evaluation of whether steering degrades generation quality is absent.

4. **Selection of topic codes involves manual filtering.** The pipeline uses a heuristic (codes activating on >50% of tokens in a sequence) plus manual filtering. This is reasonable for a proof-of-concept but limits reproducibility and makes it unclear how general the topic-steering procedure is. The paper does not analyze how many codes survive automatic filtering or how the manual step could be automated.

### Trivial

1. **No error bars on quantitative results.** Tables 1, 2, and 4 report point estimates without standard deviations or confidence intervals. This is especially relevant for the generation evaluation (Table 4), where variability across seeds could be substantial.

## Nice-to-Haves

- An automated pipeline for discovering steering codes (e.g., using TF-IDF or clustering on activation patterns) would improve reproducibility and reduce the manual filtering bottleneck.
- Analysis of codebook utilization (e.g., frequency of each code's activation) would show whether the codebook is fully utilized or whether many codes are unused or redundant.
- A systematic ablation of codebook placement (attention-only vs. MLP-only vs. both, at different layer depths) would clarify design choices.
- Comparison to sparse autoencoders (cited as concurrent work) or other sparse representation methods would help contextualize the benefits of codebooks — though this is naturally limited by concurrent timing.

## Removed Points

These points were flagged by reviewers but are removed or weakened based on verification against the paper:

- **"TokFSM codes are the definition of the state, so high precision is by construction."** This misunderstands the experiment. The FSM states are independently defined by the task structure (100 states with transition rules). The codes *learn* to detect these states. The comparison is fair: both codes and neurons are evaluated on how well they detect an externally defined state. (Harsh Critic, Critical Issue 1)
- **"Lack of a baseline method (sparse autoencoders, quantized activations)."** Sparse autoencoders are cited as concurrent work and could not be compared. The paper's primary baseline (neurons) is a natural and defensible comparison. Removing SAEs is not a methodological gap. (Harsh Critic, Other Observations)
- **"No study of codebook placement."** The paper does compare attention-only vs. attention+MLP in Table 1 for TokFSM. A full sweep is absent but the paper is not silent on the question. (Harsh Critic, Missing Parts)
- Generic/dropped strengths from Strength Finder: all of the listed strengths were substantive and specific enough to retain.

## Novel Insights

Neither reviewer surfaced an insight that goes significantly beyond the paper's own framing. The key observation — that replacing dense continuous activations with a sparse sum of discrete codes preserves task performance while enabling more interpretable and controllable representations — is the paper's own contribution, and the reviews do not add a further novel synthesis.

## Suggestions

1. **Add control interventions for LM steering.** For each topic, activate a random code (or a code from a different topic) with the same multiplicity and show that topic frequency does *not* increase. This directly supports the causal claim and requires no additional model training.
2. **Bound the interpretability claim more precisely.** Either rephrase the LM comparison as "among codes we selected for interpretability, these outperform the best thresholded neuron for the features those codes detect" or (better) define features independently of code activations.
3. **Add generation quality metrics.** Report perplexity of steered generations, or at minimum a human evaluation / LLM-based fluency rating, to show steering does not degrade output quality.
4. **Analyze code interaction for \(k>1\).** Report whether topic-code precision drops when the topic code fires alongside other unrelated codes, and whether the "lowest-scoring" code intervention is sensitive to which code is replaced.
5. **Report variability.** Add standard deviations or confidence intervals to the main quantitative results, especially the generation steering results in Table 4.

## Score and Decision

The paper introduces a clean, well-motivated method for producing sparse and discrete neural representations and provides compelling causal evidence in a controlled setting. The language model experiments are less complete — the interpretability comparison has selection bias, the steering lacks formal controls, and the performance trade-off is larger than the framing suggests — but none of these issues are fatal, and the core idea is sufficiently novel and interesting. With targeted revisions (especially control conditions for steering and more precise framing of claims), the paper would make a solid contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>