- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5
Now I have thoroughly verified the paper against the reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes Artsy, a class-incremental learning framework for pre-trained models that uses a binary gating mechanism — an MLP-based "artificial synapse" per task — to determine which adapter sub-networks contribute to the final prediction. The gating is inspired by the conversion of silent synapses to functional synapses in the mature brain. On CIFAR-100 and TinyImageNet benchmarks, Artsy achieves the highest Average and Last accuracies reported in Table 1, outperforming prior pre-trained-model-based CIL methods (EASE, MoE, ZSCL).

## Strengths

- **Competitive empirical results across multiple settings.** Table 1 reports that Artsy achieves the highest Average and Last accuracies on CIFAR-100 and TinyImageNet across all five incremental-step configurations. On CIFAR-100 (10-step), Artsy reaches 92.44% Avg / 87.94% Last, surpassing the prior best PTM method EASE by 0.91% and 2.14%, respectively. The gains hold consistently across all settings (5, 10, 20 steps).

- **Demonstrated balance between plasticity and stability.** Figure 3 (Sec. 4.4) compares Artsy against EASE across incremental steps, showing that Artsy maintains higher accuracy on both previously learned tasks and newly introduced tasks. This supports the claim that the gating mechanism aids the plasticity-stability trade-off.

- **Grounded biological inspiration with clear analogical mapping.** The paper draws on Vardalaki et al. (2022) on silent synapses in adult neocortex and constructs a consistent analogy: the frozen pre-trained network ↔ mature brain (memory stability), adapter sub-networks ↔ postsynaptic filopodial neurons (learning plasticity), and the MLP binary classifier ↔ silent-to-functional synapse conversion. While this connection is metaphorical rather than mechanistic, it is clearly articulated.

## Weaknesses

### Fatal
None.

### Major

- **No uncertainty quantification.** Table 1 reports only point estimates to two decimal places with no standard deviations, confidence intervals, or indication of the number of trials. The margins over the strongest baseline (EASE) are small (e.g., 0.91% average accuracy on CIFAR-100 10-step). Without error bars, the claimed "significant outperformance" cannot be assessed for statistical meaningfulness. This is the single most important weakness — it directly undermines the paper's core empirical claim.

- **The ablation study does not isolate the proposed gating mechanism.** The ablation (Figure 4, Sec. 4.5) compares "good feature" vs. "bad feature" as inputs to the artificial synapse (binary classifier). This tests the quality of the binary classifier's input representation, not the value of the gating mechanism itself. The paper never defines "good" and "bad" features operationally, making the experiment non-reproducible. Crucially, the paper does not ablate the gate itself: e.g., what happens if the gate is always on (no gating), if a random mask is used, or if the true task ID is provided as an oracle? Without these controls, the claimed benefit of the silent-synapse-inspired gating is not causally supported.

### Minor

- **Algorithm description has critical gaps.** Algorithm 1 states "Optimize the networks: $\sum_{i=0}^{t}E_{i}(x)$" but never specifies the loss function (cross-entropy? contrastive? distillation?). The step "Complete the prototypes for former classes" is invoked but never explained — how are prototypes computed (class mean? feature averaging? which features?). The text in Sec. 3.2 attempts to clarify the training procedure, but the algorithmic presentation remains ambiguous about what exactly is being optimized and how.

- **The biological inspiration is metaphorical, not operational.** The paper's extensive biological framing (AMPA/NMDA dynamics, spike-timing-dependent plasticity, filopodia) does not constrain or inform the technical design. The actual mechanism is a two-layer MLP binary classifier trained to distinguish old-task data from new-task data — a standard task-identification classifier. The biological narrative adds rhetorical weight but no technical novelty. The paper would be stronger if it either operationalized the biological concepts more tightly or dropped the pretense and presented the method on its own terms.

- **The method description omits what "good" vs. "bad" features are in the ablation.** Section 4.5 and Figure 4 compare the impact of different features on the artificial synapse but never define what constitutes "good" or "bad" features. This makes the ablation non-reproducible and difficult to interpret.

### Trivial

- None beyond those already covered above.

## Nice-to-Haves

- Report the accuracy of the binary synapse classifier (gate) on held-out test data across tasks. A confusion matrix of gate decisions would help diagnose when the gating mechanism succeeds or fails.
- Report parameter count and inference-time overhead compared to EASE and MoE, since adding one adapter + one MLP per task increases the model size linearly with the number of tasks.
- The comparison table groups scratch-trained methods (iCaRL, LwF, UCIR, DyTox, PASS) with PTM-based methods under a single "Methods" column. Although the paper does use "Type" labels to distinguish them, the main claim of superiority could be stated more precisely by focusing the headline comparison on the relevant peer group (PTM methods with the same backbone).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Eq. (3)–(3.1) are problematic: the sum cannot be causal."** — Removed. At training step t, sub-networks only exist up to task t; the sum $\sum_{i=0}^t h_i$ is causally sound. Future sub-networks (t+1, etc.) do not exist at this point. The concern is based on a misreading of the incremental procedure.

2. **"Comparison set is not aligned; scratch-trained methods inflate apparent gains."** — Removed (weakened to Nice-to-Have above). The paper explicitly labels PTM vs. scratch-trained methods with "Type" categories in Table 1 and acknowledges the distinction in the text (line 173). This is standard practice in the pre-trained-model CIL literature.

3. **"Missing related works (Expert Gate, PackNet, HAT)."** — Removed. These are all cited in the paper: Expert Gate (aljundi2017expert) in the Introduction, PackNet (mallya2018packnet) and HAT (serra2018overcoming) in the Related Work section.

4. **"Is the pre-trained network frozen or fine-tuned?"** — Removed. The paper clearly states (line 66): "The parameters of the pre-trained network remain fixed during the continual learning process."

5. **"Code availability would strengthen the paper."** — Removed per rule (reproducibility nitpick about large artifacts impractical to include).

6. **Strength Finder: "Ablation validates the synaptic mechanism."** — Removed. The ablation tests input feature quality for the binary classifier, not the gating mechanism itself. This conflates two different claims.

7. **Strength Finder: "Detailed algorithmic specification."** — Removed. Algorithms 1 and 2 have substantive gaps (missing loss function, undefined "complete prototypes"), so calling them "detailed" is inaccurate.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves do not make. The key tension — that the biological framing and the technical implementation (MLP binary classifier) operate at different levels of abstraction — is noted by the harsh critic but is also something the paper implicitly acknowledges by treating the neuroscience as inspirational rather than as a source of algorithmic constraints.

## Suggestions

1. **Run the main experiments at least 3 times and report mean ± std** for all entries in Table 1. This is the single most important fix — without it, the claimed improvements over EASE are unsubstantiated.

2. **Add controlled ablations that isolate the gating mechanism:** (a) no gate (all sub-network features always summed), (b) random binary mask with the same sparsity, (c) oracle using the true task ID. These would show whether the learned gating actually improves over naive alternatives.

3. **Specify the loss function explicitly** in Algorithm 1 and the main text. Define how prototypes are computed ("Complete the prototypes for former classes") — are they class-mean features from the current embedding space?

4. **Define "good feature" and "bad feature" operationally** in the ablation study, or replace this experiment with one that tests the gating mechanism directly.

5. **Tone down or tighten the biological narrative.** Either draw a tighter connection between specific biological mechanisms (STDP, NMDA/AMPA dynamics) and specific algorithmic choices, or present the method as a task-identification gating mechanism with biological inspiration rather than a model of synaptic consolidation.

6. **Consider focusing the comparison on PTM methods** in the headline results, with scratch-trained methods relegated to a separate table or supplement, to avoid distracting from the relevant comparison set.
