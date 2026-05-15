Now I have all the verification I need. Here is the consolidated final review:

---

## Summary

LLIT proposes using a frozen LLM to generate task tips and task content from descriptions of observation/action spaces, then training an auxiliary reward model to ground these language tips into reward signals for continual RL. A learnable prompt pool (modulation vectors for a Decision Transformer) is used to mitigate catastrophic forgetting by matching tasks to shared sub-networks via cosine similarity. The paper reports strong results on Continual World (CW10/CW20) against a broad set of baselines.

## Strengths

- **Novel integration of LLM-generated language into continual RL.** The idea of using LLM-inferred task tips to shape an auxiliary reward signal is genuinely novel and well-motivated. The two-stage grounding process (LLM inference → parsed tips → auxiliary reward model) is a creative attempt to bridge language and RL in a continual setting.

- **Strong empirical results on the Continual World benchmark.** On CW10 and CW20, LLIT achieves the highest Average Performance (0.53/0.60) and lowest Forgetting (0.02/0.01) among a comprehensive set of baselines including regularization-based, structure-based, rehearsal-based, and multi-task methods (Table 1). The advantage is substantial and consistent across metrics.

- **Comprehensive baseline comparison.** The paper compares against 10+ methods spanning all major categories of continual RL, alongside multi-task upper bounds. This is a fair and thorough experimental setup for the CW benchmark.

- **Memory efficiency.** By using a compact set of modulation vectors rather than replay buffers, LLIT avoids the memory and computational overhead of rehearsal-based methods while still exceeding their performance.

## Weaknesses

### Fatal

- **The auxiliary reward model — the paper's core mechanism — is not specified.** The paper states that a transformer model is trained on concatenated embeddings of parsed tips and observations to produce an auxiliary reward (Section 3.2, Eq. 3), but never specifies: (a) the loss function (regression? preference ranking?); (b) the training data or how ground-truth labels are obtained (offline trajectories? online rollouts? environment reward as target?); (c) the training procedure (jointly or separately from the policy? pre-trained before CRL starts or incrementally?). Line 88 simply says "After sufficient training of the auxiliary reward model" with no indication of what "training" entails. Since this reward model is the central claimed innovation for grounding language into policy signals, the method is unverifiable and unreproducible as described.

- **The headline claim of "adaptation to unseen tasks" is not evaluated.** The Abstract, Introduction, and Conclusion repeatedly assert that LLIT enables "adaptation to unseen tasks" and "generalizable meta-policy." However, the "Generalization" metric (Section 4.3) is defined as *the average number of steps needed to reach a success threshold during training on the same tasks* — i.e., learning speed, not zero-shot or few-shot transfer to held-out tasks. There is no experiment where tasks are held out during training and the agent must perform without further gradient updates. This claim is entirely unsupported by the experimental design.

### Major

- **Missing cross-domain results.** Section 4.1 describes a mixed-task-sequence setup sampling from Classical Control, Mujoco Control, and Continual World to evaluate cross-domain capability. Section 5.1 says "Table 1 summarizes our main results on CW10 and CW20 sequences" — but the cross-domain results are never reported. The paper cannot claim cross-domain generalization without presenting this evidence.

- **No ablation isolating the contribution of the language component.** The ablation study (Table 2) varies properties of the dictionary and prompt optimization, but never removes the LLM-inferred tips/content or replaces them with random strings. Without this, it is impossible to tell whether the observed gains come from the semantic content of the language or simply from having *any* structured auxiliary signal. This is a critical missing control for a paper whose central motivation is that language provides "high-level semantic understanding."

- **Inconsistency between the claimed "task-agnostic" setting and the method's requirements.** The paper states it targets a task-agnostic setting where no task ID or boundary is available (Sections 1, 3.1). Yet the LLM inference for task content and tips is performed "at the beginning of training for each task" (line 67), which presupposes knowledge of task boundaries. No mechanism for detecting task boundaries is proposed. The prompt pool retrieval also implicitly relies on per-task queries.

- **The Generalization metric is misnamed and conflates learning speed with generalization.** While the metric (steps-to-threshold on training tasks) is a reasonable measure of plasticity/adaptation speed, calling it "Generalization" and then claiming the method "generalizes to unseen tasks" is a significant framing error that misleads readers about what was actually measured.

### Minor

- **Prompt templates not provided.** The prompts $p_{content}$ and $p_{tips}$ (Eq. 2) are central to the quality of the LLM outputs but are never specified. Given that code is released, this is addressable but currently a reproducibility gap.

- **The tip-parsing mechanism is underspecified.** The "frozen similarity model" that parses tips by detecting whether a dimension description "exists in a tip" (Section 3.2) is not detailed — what model is used, what threshold, how are sub-sentences bound? This step is critical for bridging text and observations.

- **Training procedure for the Decision Transformer is unclear.** It is never explained whether the DT is trained with offline trajectories or online rollouts, whether it receives both environment reward and auxiliary reward, or how the two signals are combined. The relationship between the auxiliary reward model training and DT training is not described.

- **"CoTASP" referenced without introduction.** Line 166 mentions "CoTASP" as a comparison point, but this method is never defined or cited in the paper.

### Trivial

- PC is listed under both "rehearsal-based" (Schwarz et al., 2018) and "regularization-based" (Kaplanis et al., 2019) in Section 2. While these are different papers, the dual listing without clarification is confusing.

## Nice-to-Haves

- A hyperparameter sensitivity analysis for the prompt pool size (number of keys M) and the sparsity parameter $\lambda$ beyond the brief mention in Section 5.1.
- Additional analysis of the learned modulation vectors — e.g., a similarity matrix showing that related tasks indeed map to nearby keys.
- A comparison with a version that uses the prompt pool alone (i.e., L2P-style modulation) without the LLM/auxiliary reward, to separate the contributions of the two components.

## Removed Points

These points were flagged by reviewers but are removed (with justification) and should be treated with caution:

1. **"The paper cites unreleased models/tools"** — Removed per hard rules: all cited entities are assumed to exist and be released.
2. **"No confidence intervals / significance tests"** — Removed per soft rules: single-run evaluation on large benchmarks is the norm in this community, and mean±std over 5 seeds is reported.
3. **"Missing appendix / proofs"** — Removed per hard rules: the parser strips appendix content; it exists in the original submission.
4. **"Formatting and typo nitpicks"** — Removed per hard rules: these are parser artifacts.
5. **"Insufficient hyperparameter disclosure"** — Partially removed per hard rules: trivial implementation details impractical to include are acceptable; the paper states it re-uses the Continual World repository's hyperparameters (Section 4.2), which is reasonable.

## Novel Insights

The combination of the harsh critic's identification of multiple unsupported core claims and the strength finder's identification of genuine novelty in the approach reveals a paper with a promising idea but deep gaps between its rhetoric and its evidence. The most striking pattern is that every major claim in the paper — "training an auxiliary reward model from language," "adaptation to unseen tasks," "cross-domain capability," "task-agnostic operation" — is either underspecified to the point of unverifiability or simply not tested. The paper's actual contribution, when stripped of these claims, is a well-executed adaptation of L2P-style prompt pools to Decision Transformers for continual RL, augmented with LLM-generated auxiliary inputs. The empirical results on Continual World are genuinely strong, but the paper's framing systematically overclaims what was actually demonstrated.

## Suggestions

1. **Specify the auxiliary reward model training objective** — loss function, training data source, and training procedure. This is absolutely required for reproducibility.
2. **Conduct a proper zero-shot/few-shot transfer experiment** — train on a subset of tasks and evaluate on held-out tasks without additional gradient steps, or report the actual task-similarity-based transfer. Replace the misleading "Generalization" label.
3. **Report the cross-domain mixed-task-sequence results** promised in the setup, or remove the claim of cross-domain capability.
4. **Add an ablation replacing LLM outputs with random strings** to isolate the contribution of semantic language content.
5. **Clarify how task boundaries are handled** — if they are assumed known (as the current method implies), state this explicitly and remove the "task-agnostic" framing, or propose a boundary-detection mechanism.
6. **Provide the prompt templates and parsing similarity model details** in the main text or supplementary material.
7. **Clarify the Decision Transformer training loop:** what data it trains on (offline trajectories? online experience?), how environment reward and auxiliary reward are combined, and how the reward model training interacts with policy training.

## Score and Decision

The paper presents a genuinely novel and well-motivated idea with strong results on a standard benchmark. However, the core training mechanism (the auxiliary reward model) is unspecified to the point of unreproducibility, and several headline claims ("adaptation to unseen tasks," "cross-domain generalization") are categorically unsupported by the experimental design. The paper cannot be accepted in its current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>