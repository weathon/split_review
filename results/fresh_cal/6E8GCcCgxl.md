Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces Eidetic Learning, a pruning-and-freezing approach to continual learning that eliminates catastrophic forgetting. The method iteratively identifies the minimal subnetwork for each task (via structured pruning), freezes those important neurons, prunes synaptic connections from recycled (pruned) neurons to frozen neurons in downstream layers, and recycles freed neurons for subsequent tasks. The paper defines two conditions — Persistence (important neurons stay frozen) and Resistance (pruned neurons cannot affect frozen ones) — and argues these are sufficient to guarantee no forgetting. Empirical results on Permuted MNIST (MLP), Sequential CIFAR-100 (ResNet50), and Imagenette (ResNet18) show flat per-task accuracy across sequential training.

## Strengths

- **Formal conditions for guaranteeing no forgetting**: The paper identifies Persistence and Resistance as sufficient conditions for immunity to forgetting (Section 2). This is a clearer theoretical framing than most continual learning methods, which offer only empirical mitigation. The reasoning that freezing important neurons and isolating them from recycled neurons' outputs prevents representation drift is sound.

- **Empirical demonstration of zero forgetting**: Figure 1 shows that test accuracy for each of 10 Permuted MNIST tasks remains completely flat as subsequent tasks are trained. Tables 4 and 5 extend this to ResNet50 on CIFAR-100 and ResNet18 on Imagenette, demonstrating the method works beyond simple MLPs.

- **Constant hyperparameter complexity**: As shown in Table 1, Eidetic Learning requires only a constant number of hyperparameters per ANN, compared to methods like CLNP whose hyperparameter count is linear in the number of layers. This is a practical advantage for deep networks.

- **Task routing without oracle task IDs**: Section 4 describes and evaluates a meta-classifier that predicts the task ID at inference time, showing only a modest drop in per-class accuracy compared to oracle routing (e.g., 1.8% for ResNet50 on CIFAR-100 in Table 8). This makes the method applicable when task identity is unknown.

- **Explicit treatment of residual connections**: Section 3.1 provides a principled method for handling skip connections in residual networks, describing how to prune the residual path to maintain the guarantee.

## Weaknesses

### Fatal
None.

### Major

- **Batch normalization handling is significantly underspecified, conflicting with the claimed scope**. Section 3.1 describes that for BN layers, the paper will "(i) make the β,γ of the previous tasks stay in evaluation mode when training subsequent tasks, and (ii) ensure that internal running statistics are not updated." However, the paper does *not* specify the mechanism by which this is achieved while still allowing new tasks to learn. If the BN layer is in training mode, the running statistics (μ,σ) update globally; if it is in evaluation mode for previous tasks' channels while training mode for new tasks' channels, the paper does not describe how this per-channel mode switching is implemented. The paper also claims the method "supports contemporary ANN architectures without modification" (line 29) while *Kaushik et al. (2021) requires a separate batch normalization layer per task* — but the paper's own BN handling may require non-trivial training-loop modifications. Since BN is used in every convnet experiment (ResNet50, ResNet18), the reader cannot verify whether the reported results reflect the claimed guarantee. This is the single most consequential weakness: the paper needs to either (a) provide a complete, implementable description of the BN mechanism, or (b) acknowledge limitations and report which experiments were affected.

- **Overclaim of "provable" without a formal proof**. The title promises a "Provable Solution," and the abstract states the paper will "prove that it guarantees networks do not forget." What the paper actually provides is an informal argument: two conditions (Persistence and Resistance) are stated as sufficient, then Section 3 describes a procedure and asserts it satisfies them. No theorem statements, no rigorous justification of sufficiency (e.g., handling of nonlinearities, the transitive nature of Resistance), and no formal derivation are given. While the conditions and reasoning are plausible, calling this a "proof" or a "provable" solution is misleading. The paper would be better served by clearly stating that it provides a sufficient-condition framework with strong empirical validation.

- **No quantitative baselines in the main experimental tables**. The paper mentions "We show in Table 3 that our method is competitive" (line 58) and Figure 1's caption says "See Table 3 for a comparison with other methods." However, Table 3's caption reads "Mean and standard deviation of *our method* on 10 tasks of Permuted MNIST" — no baseline methods are listed in the caption. Tables 4 and 5 (CIFAR-100, Imagenette) similarly report only the proposed method's results with no comparison values from EWC, SI, PackNet, CLNP, or any other method mentioned in the related work. Without direct comparisons on the same benchmarks under the same experimental conditions, the reader cannot assess whether the method is competitive with the state of the art. Given that methods like PackNet and CLNP use similar sparsity patterns and also report high retention on simple benchmarks, the claimed advantages are not empirically substantiated.

### Minor

- **Limited experimental scope**: The method is evaluated only on task-incremental scenarios with ≤10 tasks on small-to-medium datasets (PMNIST, CIFAR-100, Imagenette). The paper explicitly scopes out class-incremental learning and does not test on longer task sequences, larger datasets (e.g., full ImageNet), or more diverse architectures (Transformers). While these are acknowledged limitations, the paper's framing as a general "solution to catastrophic forgetting" is broader than what the evidence supports.

- **The Resistance condition is not directly verified**: The core guarantee is that hidden states entering frozen neurons remain unchanged for any input from previous tasks. Yet the experiments only report final accuracy — they do not directly measure whether hidden states actually remain identical. Direct verification (e.g., measuring the L2 norm of hidden state differences before/after subsequent training) would substantially strengthen confidence in the guarantee.

- **Taylor pruning limitation acknowledged but not resolved**: The paper notes that Taylor pruning does not prune uniformly across layers and can violate the method's principles, yet it is used as a primary pruning strategy in several experiments. The conditions under which the pruning step actually satisfies the Resistance condition are not clearly characterized.

### Trivial
None.

## Nice-to-Haves

- Provide pseudo-code or an explicit algorithmic listing of the training and inference procedures, including how BN statistics are managed across tasks.
- Report the fraction of capacity pruned per layer after each task to help readers understand whether the Resistance condition was satisfied.
- Test on longer task sequences (e.g., 20+ tasks) to demonstrate that the guarantee holds when capacity becomes scarce.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"BN handling is a structural flaw; the method cannot work for networks with normalization layers"** (Harsh Critic). Removed because this claim is speculative and not verified from the paper as written. The paper describes an approach (freeze β,γ; prevent running statistics from updating) that is implementable — e.g., via per-channel masking or PyTorch hooks — even though the description is incomplete. The critic asserts impossibility without proof.

- **"Missing formal proof of pruning finding the smallest set of neurons"** (Harsh Critic). Removed because the method's pruning procedure is a practical heuristic (iteratively prune until accuracy drops below a threshold), not a formal optimization. The critic's demand for a guarantee that the "smallest set" is found is not part of the paper's core claim; the claim is that important neurons are frozen and isolated.

- **"Residual connection handling is insufficient for complex topologies"** (Harsh Critic). Removed because the paper provides a general construction that handles skip connections by porting masks from the first and last layers to the residual path, and states it holds "regardless of the use of nonlinearity, the use of BN, or the number of internal layers." Demanding coverage of every possible architecture (dense blocks, inception modules) is scope creep.

- **"General formatting, missing appendix, missing code release"** (Harsh Critic). Removed per hard rules: parser artifacts are not author errors; missing appendix sections were stripped by the parser; code release is promised upon publication which is standard.

- **Strength Finder: "Principled handling of batch normalization"** claimed as a core strength. Removed because the BN description is too underspecified to be called "principled" — the mechanism for preventing running statistic updates while allowing new tasks to learn is not described. The strength is the *intention* to handle BN, not the execution.

- **Strength Finder: Generic or superficial strengths** (e.g., "this paper addressed an important problem"). Removed as generic observations that any paper in this area would satisfy.

## Novel Insights

The Persistence and Resistance conditions provide a clean decomposition of what is needed to guarantee no forgetting: preserve the weights *and* isolate the inputs to those weights. This separation is more principled than most continual learning methods' reliance on regularization penalties or replay buffers. The key insight — that excess capacity can be exploited by pruning task-critical subnetworks and directionally deleting synapses from recycled neurons to frozen ones — is distinct from simply maintaining task-specific masks (as in PackNet or CLNP) because it handles the *forward propagation* of changes through recycled neurons. However, the paper's failure to fully specify the BN handling mechanism and its lack of quantitative baselines prevent this insight from being properly evaluated.

## Suggestions

1. **Specify the BN mechanism completely.** Describe, ideally with pseudo-code, how per-channel BN statistics are frozen for previous tasks while allowing new tasks to learn. If this requires training-loop modifications (e.g., per-channel hooks), acknowledge this and explain how it interfaces with the claim of "no architecture modification."

2. **Add quantitative comparisons** to at least EWC, SI, PackNet, and CLNP on Permuted MNIST and CIFAR-100. Report not just per-task accuracy but also forgetting rates (average accuracy on previous tasks after all tasks are trained).

3. **Tone down the "provable" claim** or actually provide a formal proof (theorem + proof). The paper's conditions are sufficient, but the paper should present them as a sufficient-condition framework with supporting empirical evidence, not as a "provable solution."

4. **Directly verify the Resistance condition** by measuring whether hidden states for previous tasks' test inputs change before and after subsequent training. This would provide direct evidence for the claimed guarantee.

## Score and Decision

The paper proposes a novel approach with a clear theoretical framework and promising empirical results. However, the BN handling is critically underspecified for a method that relies on standard convnet architectures, the "provable" claim is overstated without a formal proof, and the absence of any quantitative baseline comparisons makes it impossible to assess the method's competitiveness. These are major issues that would need to be resolved before the paper meets the bar for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>