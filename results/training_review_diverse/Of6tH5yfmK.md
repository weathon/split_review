Now I have all the information needed to verify every claim. Let me produce the final review.

## Summary

This paper introduces a gradient-based inference-time framework for controlling LLM behaviors by leveraging the model's own self-evaluation. For a target behavior expressed as a natural-language suffix question (e.g., "Was the response helpful? Yes or No?"), the method computes the gradient of the suffix score (log-probability ratio of "Yes" vs. "No") with respect to the input's latent representations, then iteratively updates those representations to steer generation toward the desired behavior. A Prefix Controller (PC) module is further proposed to distill instance-level gradients into a lightweight adapter for efficient multi-behavior control. Experiments span detoxification, truthfulness, emotion control, privacy protection, reasoning, and data synthesis, reporting improvements over prior SOTA approaches.

## Strengths

- **Novel annotation-free control paradigm with broad empirical validation.** The paper's core idea — using gradients of the LLM's own evaluative response on a suffix string as a steering signal — is novel and eliminates the need for human-annotated preference data. The method is evaluated across six distinct control tasks (toxicity, truthfulness, emotion, privacy, reasoning, helpfulness/harmlessness), with reported improvements of **8.3%** in detoxification, **3.1%** in truthfulness, **4–10%** in emotion control, and **48.2%** in privacy protection (Abstract, Section 1). These results come from standard benchmarks (RealToxicityPrompts, DecodingTrust, GSM8K, Anthropic-HH).

- **Prefix Controller provides practical efficiency and composability.** The PC module compresses instance-level suffix gradients into a parameter-efficient adapter that achieves **10× faster** inference than the iterative Method itself (Table running_time) and enables simultaneous control of multiple behaviors (e.g., happier and calmer) with composable weights (Section 3.2, Figure ablations). This addresses the practical bottleneck of the Method's per-instance cost and demonstrates a path toward real-world deployability.

- **Demonstrates data synthesis utility beyond direct control.** The paper shows that Method-generated preference pairs improve model win rates via DPO (58.6% overall, comparable to SAMI's 60.0%), extending the method's value beyond inference-time control to training data augmentation (Table tab:win_rates).

## Weaknesses

### Major

- **Random perturbation ablation raises unresolved questions about gradient necessity.** The paper reports (Section 4.3, Table tab:ablation) that replacing the suffix gradient with a **random vector** while retaining iterative step-size search achieves a *lower* (better) toxicity score on Llama-2-7b-chat (0.264 vs. 0.285) — nominally SOTA on that model. The paper acknowledges this finding but treats it primarily as evidence for the "efficacy of the framework of searching step-sizes." This is insufficient. The result (though model-dependent: on Mistral the true gradient outperforms random, 0.282 vs. 0.296) directly challenges the claim that the gradient direction computed from self-evaluation provides meaningful guidance. If random perturbations combined with line search perform comparably or better on some models, the paper's central mechanism — that gradients of the LLM's self-evaluation are the key control signal — is partially undermined. The authors do not analyze *why* random vectors succeed on Llama-2-7b-chat, nor do they characterize conditions under which the true gradient helps versus hurts. This demands a dedicated investigation rather than a brief mention.

- **No statistical uncertainty reported for any experiment.** None of the main result tables include standard deviations, confidence intervals, or significance tests. Given that the Method involves iterative sampling, gradient computation, and line search — all of which introduce variance — the absence of error bars is a meaningful gap. For example, the emotion control results show Method performing *worse* than the uncontrolled original on several attributes (e.g., happiness: 3.99 vs. 4.60 original; fear: 2.90 vs. 3.26 original) despite being presented as effective. Without uncertainty estimates, it is impossible to tell whether these differences are meaningful or within noise.

### Minor

- **Self-evaluation signal is only indirectly validated.** The paper dismisses known LLM self-evaluation biases (position bias, distribution bias, sycophancy) with a brief statement that they "generally do not apply to our method" because it only probes first-token probabilities (Section 2). While the paper implicitly validates the suffix score by showing that optimizing it improves external metrics (Perspective API, accuracy, GPT-3.5 judgments), it never directly checks whether the suffix score correlates with human judgment or established classifiers on a held-out set. A simple sanity check — e.g., comparing suffix scores against a toxicity classifier for the detoxification task — would strengthen confidence that the optimization target is meaningful. As it stands, the reward signal's reliability rests on indirect evidence.

- **Duplicate Section 3 obstructs clarity.** Section 3 ("\method") appears twice in the paper (lines 76–166 and lines 169–243) with different text and framing. The second occurrence includes author-internal notes (\cm{...}) and is clearly a draft version that was not removed before submission. A reader cannot tell which version is intended as final, and the duplication makes the method description harder to follow. This is a presentation flaw that should be corrected.

- **GSM8K reasoning results show Method underperforming CoT Decoding.** On reasoning (Table tab:reasoning_results), Method achieves 37.30% vs. CoT Decoding's 42.00%, and the Prefix Controller scores only 27.14% (barely above greedy 26.61%). The paper attributes the PC's poor performance to limited training data (100 samples), which is plausible but weakens the generality claim for the controller. While not a fatal flaw, this limits the method's applicability to reasoning tasks.

- **PCA visualization analysis is informative but under-analyzed.** The claim that "Method fundamentally restructures representations" while Contrast Vector "primarily rotates and translates" (Section 5.2) is interesting but the connection to downstream accuracy is presented anecdotally. The analysis would benefit from quantitative metrics linking representational changes to task performance.

### Trivial

- None. The remaining issues (formatting, typos, missing tables via \input{}) are parser artifacts rather than paper flaws.

## Nice-to-Haves

- A direct analysis of the random gradient finding: comparing distributions of achieved suffix scores under true gradients vs. random perturbations across multiple tasks and step sizes would clarify when the gradient direction actually matters.
- Reporting standard deviations or confidence intervals for main results, especially given the variance likely introduced by iterative sampling.
- Direct correlation analysis between suffix scores and external classifiers/human judgments on a held-out validation set.

## Removed Points

These points were raised by reviewers but are factually incorrect, parser artifacts, or reflect reviewer misunderstandings; they are removed or downgraded here with justification:

- **"Tables referenced but not shown"** (Harsh Critic): Tables `Toxic_results` and `tab:llama2_privacy_results` are included via `\input{}` statements (lines 293, 470). These are separate files that the PDF parser stripped. The tables exist in the original submission. REMOVED (parser artifact).
- **"Emotion control metric is confusing"** (Harsh Critic): The caption "The lower score, the emotions are better expressed" is unambiguous. The original scores (1.56–4.60) leave clear room for improvement. REMOVED (reviewer misreading).
- **"Computational cost concern undercuts on-the-fly adaptability"** (Harsh Critic): The paper introduces the Prefix Controller specifically to address this cost. The observation is valid but the paper explicitly acknowledges the trade-off and provides a solution. MOVED to Nice-to-Haves (addressed by authors).
- **"DPO win rates comparable to SAMI — small margin"** (Harsh Critic): Being comparable to a strong baseline (60.0% vs. 58.6%) is a *positive* result for the data synthesis claim, not a weakness. REMOVED (incorrect framing).
- Strength Finder's "mechanistic interpretability" strength: The per-layer norm analysis and attention analysis are interesting but preliminary. KEPT but as a Supporting strength, not a Core one.

## Novel Insights

The most interesting finding that emerges across the reviews and the paper is the **asymmetric evidence for gradient necessity**: on Llama-2-7b-chat for toxicity, random perturbations + line search match or exceed true gradients, but on Mistral the true gradient outperforms random. This suggests the method's effectiveness may stem more from the iterative line-search framework than from the gradient direction per se, with model architecture or initialization determining whether the gradient adds value. This is a testable hypothesis the paper does not explore but that future work could investigate systematically.

## Suggestions

1. **Address the random gradient finding directly.** Compare true vs. random gradients across *all* tasks (not just toxicity) and both models. If the true gradient provides no consistent advantage, reframe the contribution around the iterative line-search framework rather than the gradient computation.
2. **Remove the duplicate Section 3** and present a single, clean method description.
3. **Add error bars** or bootstrapped confidence intervals to all main result tables.
4. **Validate the suffix score** against an external judge (e.g., a toxicity classifier for detoxification, human ratings for emotion) on a held-out set to confirm the optimization target is reliable.
5. **Clarify the scope of the reasoning results** — the paper should state upfront that Method is not designed for reasoning tasks and the results there are preliminary.

## Score and Decision

**Originality**: 4/5 — The self-evaluation gradient framing is novel.  
**Importance**: 4/5 — Annotation-free inference-time control is a practically relevant problem.  
**Claims support**: 2.5/5 — Partially undermined by the random gradient finding and missing error bars.  
**Soundness**: 3/5 — Experiments are broad but lack statistical rigor; one ablation raises unresolved questions.  
**Clarity**: 2.5/5 — The duplicate Section 3 and author-internal comments significantly harm readability.  
**Value**: 3.5/5 — The core idea and PC module have clear practical value, but the evidence for the mechanism needs strengthening.

The paper introduces a genuinely novel approach to inference-time LLM control and demonstrates it across an impressive range of tasks. However, the random-gradient finding casts doubt on whether the specific gradient computation is doing the claimed work, and the duplicate sections and missing error bars are non-trivial presentation issues. The paper would benefit from major revisions — particularly a dedicated analysis of gradient necessity and a cleanup of the manuscript — before it can be confidently accepted.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>