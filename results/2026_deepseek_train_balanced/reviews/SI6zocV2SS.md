Here is my final consolidated review.

---

## Summary

This paper proposes CAN (Continuously Adapting Networks), an architecture for continual learning that uses Hebbian learning to compute importance scores for neurons, then scales SGD gradients by these scores to selectively freeze or modulate parameter updates across tasks. The method is evaluated on 2-task MNIST and CIFAR-10 splits in both task-incremental and domain-incremental settings.

## Strengths

- **Hebbian-based gradient scaling as a different mechanism from prior importance measures**: The paper proposes scaling SGD gradients continuously by Hebbian-derived importance scores, producing a spectrum from full update to complete freezing, rather than using Fisher information (EWC), path integrals (SI), or hard binary parameter isolation (Hou et al. 2025). Section 1 (line 12) describes "a hebbian update matrix which upon normalization acts as scaler values to scale the incoming gradients with the connection importance," and Section 3.2 describes gradients being "scaled according to the importance of the connections and even completely ignored if the scaling value is 0." This is a conceptually distinct approach to importance-weighted gradient modulation in continual learning. However, this claimed strength is almost entirely undermined by the fact that the actual computation of these scores is never specified (see Fatal weakness).

## Weaknesses

### Fatal

- **The method is critically under-specified, making the core contribution unreconstructable.** The paper never specifies which Hebbian variant is used in practice. Section 3.1 presents three different formulations — the basic Hebbian rule (Eq. 1, line 86), Oja's rule (Eq. 2, line 99), and lateral inhibition (Section 3.1.3) — without stating which one actually computes the importance scores used in experiments. The importance score computation itself is described only as "calculate the average of all the weights relevant to one particular neuron at a time and repeat the same for all the neurons. At the end, the values are scaled to get a score value" (Section 3.1.1, lines 83-84). Which weights? Which neurons? What scaling? The threshold for freezing is called "pre-defined" (Section 3.3, line 130) but its value is never given. The relationship between the Hebbian network and the main ANN — whether they share weights, operate in parallel, are trained jointly or sequentially — is never clarified. Gradient scaling is described only as "multiply the scaled hebbian updated values with the gradients" (Section 3.2, line 116). No pseudocode, algorithm listing, or formal specification is provided. At ICLR, a new-method paper must present its method precisely enough to be implemented; this paper does not meet that bar. This weakness alone is sufficient for rejection.

### Major

- **The evaluation compares only to vanilla SGD, which is not a meaningful baseline for continual learning.** The only comparison in the paper is between CAN and a standard neural network with no continual learning mechanism at all ("vanilla" SGD, Figures 3-6). Established continual learning methods — Elastic Weight Consolidation (EWC), Synaptic Intelligence (SI), Progressive Neural Networks, Memory Replay (ER), GEM — are cited in the related work but never compared against. Beating vanilla SGD on a 2-task problem does not demonstrate that CAN reduces catastrophic forgetting relative to existing approaches that also target the problem. Without this comparison, the paper cannot support its claim of "significantly reduc[ing] the risk of catastrophic forgetting" (abstract, line 4).

- **The task-incremental evaluation relies on a task oracle (manual mask selection), sidestepping a core challenge of continual learning.** Section 4.3 (lines 184-185) states: "Currently, to analyze the performance of the model, we are manually selecting the mask." The model is provided with the identity of which task it is evaluating during inference. In standard continual learning, task identity must either be inferred or is unknown. The paper acknowledges this as future work, but the reported results conflate the method's performance with the provision of privileged task information, making them uninterpretable as a demonstration of autonomous continual learning.

- **The domain-incremental experiment does not actually employ the paper's claimed masking mechanism, and what the algorithm does in this setting is unspecified.** Section 4.1.2 (line 161) states: "In this case masks are not used for forward propagation as the entire dataset is used when it is trained both the times." Section 4.2.2 (line 176) repeats: "In this experiment there are no masks since the entire data is used to train." Since masking/freezing is the paper's core mechanism for preventing forgetting, and the algorithm's behavior without masks is never described, this experiment cannot support any claim about the method's effectiveness. The paper says "Our algorithm showed improvements from the vanilla model" (Section 4.1.2, line 161), but the reader is not told what "our algorithm" actually does when masks are not used.

- **Results are not interpretable: no numerical accuracy values, single seed, no variance estimates.** All results are presented as images (Figures 3-6, Table 1). No accuracy numbers appear in the text. Experiments were run with a single seed (720, Section 5.3, line 230). No standard deviations, confidence intervals, or run counts are reported. For a paper claiming to demonstrate a performance improvement on a 2-task setup with small datasets, this makes it impossible to assess whether the reported improvements are meaningful or robust.

- **The evaluation is extremely limited in scope.** Only 2 datasets (MNIST, CIFAR-10) are used, with only 2 tasks per dataset. No standard continual learning benchmarks (e.g., split CIFAR-100, 5-task or 20-task Permuted MNIST, Mini-ImageNet) are employed. The paper acknowledges a constraint that "we can't use a continuous stream of data belonging to a variable number of classes" (Section 4.1.1, line 153), which is a severe limitation for a method claiming to address continual learning.

### Minor

- **The related work survey is shallow and does not position the paper's contribution.** Sections 2.1-2.5 list broad categories (regularization, replay, parameter isolation, dynamic architectures, meta-learning) with 1-2 citations each and one-sentence descriptions. The paper never explains what EWC, SI, Progressive Networks, or GEM actually do, how they fail, or why the proposed Hebbian approach might overcome their specific limitations. This makes it impossible to understand what gap the paper fills.

- **"Time to Stability" is introduced informally without a formal definition.** Section 5.3 (lines 226-230) defines this concept only in prose ("Stability is reached when the model's performance on the new task no longer fluctuates significantly") without specifying a quantitative criterion. The observation that the second task required 20 epochs vs. 10 for the first is reported without analysis or explanation.

- **No ablation studies are provided.** The method combines Hebbian score computation, gradient scaling, binary masking, and forward-propagation masking. Without ablations, it is impossible to know which components contribute to the reported behavior.

## Nice-to-Haves

- Including a step-by-step algorithm or pseudocode listing would address the Fatal weakness.
- A simple baseline such as freezing a random subset of neurons with the same mask budget would help isolate whether the Hebbian scoring mechanism provides any advantage over naive approaches.
- Implementing at least a basic gating mechanism (the auto-encoder approach mentioned in Section 4.3) would remove the task oracle, even if imperfect.

## Removed Points

These points were flagged for removal from the original reviews, but are included here for transparency:

- "The paper conflates parameter isolation with biologically-inspired Hebbian scoring without clarifying what is novel" (Harsh Critic) — Too vague to be actionable; removed per discipline rule.
- "The Hebbian-based importance computation is biologically grounded" (Strength Finder) — Generic framing, common to many papers in the area; removed per filtering rule.
- "Evaluation across both task-incremental and domain-incremental settings" (Strength Finder) — Conflicts with verified weakness that domain-incremental setting does not use the core mechanism; removed per conflict rule.
- Comments about code release and formatting (Harsh Critic) — Removed per hard rules about reproducibility nitpicks and formatting artifacts.
- Speculative criticism that "the domain-incremental experiment does not actually use the proposed method" was restated as a verified Major weakness (the paper confirms masks are not used) rather than being removed entirely.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fully specify the algorithm.** Provide a pseudocode listing or formal description of: (a) which Hebbian rule is used, (b) how importance scores are computed from Hebbian weights, (c) the threshold and how it is set, (d) the architecture of the Hebbian network and its relation to the main ANN, (e) how the Hebbian network is trained (jointly/separately/sequentially). This is a prerequisite for any further evaluation.

2. **Compare against actual continual learning methods.** At minimum, include EWC and SI as baselines on the same 2-task setup. Hard-freezing a random subset of neurons with the same budget would also clarify whether the Hebbian scoring adds value over random assignment.

3. **Remove the task oracle.** Either implement a gating mechanism or clearly bound the paper to the "task-labeled" setting and compare against task-labeled baselines.

4. **Report numerical results with variance.** Give actual accuracy numbers, run multiple seeds, and report standard deviations.

5. **Test on standard continual learning benchmarks** (e.g., split CIFAR-100, Permuted MNIST with 5+ tasks) to demonstrate scalability beyond 2-task toy problems.

## Score and Decision

This paper cannot be accepted in its current form. The method is too under-specified to be understood or reproduced (Fatal), the evaluation lacks any comparison to methods that actually address catastrophic forgetting (Major), the task-incremental results rely on a task oracle (Major), the domain-incremental experiment discards the core mechanism without specifying what was actually done (Major), and the results are reported without numerical values or variance estimates (Major). These are not minor deficiencies addressable in a rebuttal — they reflect a complete absence of the algorithmic specification and evaluation rigor required for a methods paper at a top venue.

**MY FINAL SCORE: <score>2.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**