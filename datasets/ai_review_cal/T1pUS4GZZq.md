- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6
Now I have all the information needed. Let me write the consolidated review.

**Summary**

This paper introduces a Large Recurrent Action Model (LRAM) that replaces the Transformer backbone of Decision-Transformer-style agents with modern recurrent architectures (xLSTM, Mamba). The authors conduct a large-scale empirical study across 432 tasks from 6 domains with 894M transitions, comparing four model sizes (16M–206M parameters). The key findings are that recurrent architectures match or exceed Transformer performance on the evaluated tasks while offering substantial inference-time advantages (constant per-step cost, lower memory footprint), especially at long context lengths.

**Verification of reviewer claims against the paper:**

1. **Training convergence (200K updates, ~2.8% of data)**: Confirmed from line 250 ("200K updates with a batch size of 128") and Table 1 (894M total transitions). 200K×128=25.6M/894M≈2.86%. No learning curves showing evaluation performance over time are presented.

2. **Inference complexity claims**: The paper explicitly states at line 362: "The Transformer with KV-caching has a linear time complexity per step and quadratic in the sequence length." This is accurate. The critic's claim that this is misleading is wrong. **REMOVED.**

3. **A100 hardware**: Confirmed at line 358 ("on A100 GPUs with 40GB of RAM"). The paper's limitations section (lines 419-427) mentions missing real-robot evaluation but not the hardware gap.

4. **Fine-tuning missing Transformer baseline**: Confirmed at lines 283-284: only compares pretrained xLSTM vs randomly initialized xLSTM.

5. **ICL missing Transformer baseline**: Confirmed at line 300: "exchange the Transformer backbone architecture with modern recurrent architectures" — the comparison is between recurrent variants only.

6. **Error bars**: Confirmed absent from Figure 2.

---

## Summary

This paper proposes a Large Recurrent Action Model (LRAM) that replaces the Transformer backbone of Decision-Transformer-style agents with modern recurrent architectures (xLSTM, Mamba). The authors conduct a large-scale empirical study across 432 tasks from 6 domains with 894M transitions, comparing four model sizes (16M–206M parameters) and four backbones (xLSTM [7:1], xLSTM [1:0], Mamba, and GPT-2-style DT). The central claim is that modern recurrent architectures are better suited for large action models due to competitive performance combined with substantial inference-time advantages.

## Strengths

1. **Systematic large-scale comparison**: The study compares four architectures at four model sizes across 432 tasks — an unusually broad empirical effort. The per-domain breakdown (Figure 3) shows that xLSTM outperforms competitors on 3/6 domains at 206M parameters and is competitive on the remaining 3. The consistency of the trend across model sizes strengthens the evidence.

2. **Inference advantage cleanly demonstrated**: The inference experiments (Section 4.4) show that xLSTM maintains constant per-step latency regardless of context length, while Transformer-based DT runs out of memory at context lengths beyond ~5K timesteps (batch size 1) and batch sizes beyond 64. This is a genuine practical advantage — the OOM failure at large context sizes is a real limitation for Transformers that the paper correctly highlights.

3. **Large-scale multi-domain dataset**: The paper compiles and releases a dataset of 894M transitions across 432 tasks from 6 domains with careful per-domain statistics (Table 1). This resource enables the controlled scaling study and is valuable for future work.

4. **Architectural design insights**: The paper identifies that removing actions from the input sequence improves performance (particularly for continuous control), and introduces a shared action head for faster inference. These design choices are well-motivated and empirically validated.

## Weaknesses

### Fatal
None.

### Major

1. **No convergence evidence for the central performance comparison.** All models are trained for 200K updates with batch size 128, amounting to ~25.6M transitions seen out of 894M (~2.8% of the data). The paper does not show learning curves of evaluation performance over training steps, so it is impossible to assess whether the reported rankings between architectures have stabilized. The paper's claim that recurrent architectures are "better suited" (line 82) and achieve better "final performance" (line 279) implies a general advantage, but this could reflect a fixed-compute advantage that reverses with more training. Validation perplexity on held-out data (Figure 2a) provides partial support, but this is a surrogate for the actual metric of interest (environment scores). While the fixed-budget comparison is a legitimate experimental design, the paper's rhetoric extends beyond what the evidence supports without convergence analysis.

### Minor

2. **Fine-tuning evaluation lacks a Transformer baseline.** The fine-tuning experiment (Section 4.3) compares only pretrained xLSTM vs. randomly initialized xLSTM. A Transformer (DT) baseline fine-tuned under the same protocol is needed to support the claim that "fine-tuning performance is not negatively affected by switching the backbone" (line 287). Without this comparison, the experiment only shows that pretraining helps — a well-known result.

3. **In-context learning evaluation is limited.** The ICL experiment (Section 4.3) compares xLSTM variants and Mamba on the Dark-Room grid world but does not include the original Transformer-based Algorithm Distillation baseline. The claim about ICL advantages is therefore unsubstantiated relative to the paper's main comparison (recurrent vs. Transformer). The comparison between xLSTM [7:1] and [1:0] does support the claim about sLSTM state-tracking, but this is a narrower point.

4. **Main scaling figure lacks error bars.** Figure 2 reports aggregate normalized scores without confidence intervals, interquartile ranges, or any variance measure. Given that scores are averaged across 432 diverse tasks with different normalization schemes (human-normalized for Atari, data-normalized for others), the reliability of a single point estimate is unclear.

5. **Inference benchmarks are on A100 GPUs, not robotics-grade hardware.** The paper's stated motivation is real-time control (100–1000 Hz, <10ms per step) on embedded devices. All latency experiments are on A100 GPUs (40GB). Whether the observed advantages transfer to devices like Nvidia Jetson is unknown, and the paper does not discuss this gap. The relative advantage in memory footprint (no KV-cache) is architecture-level and should transfer, but per-step latency ratios may differ substantially on less powerful hardware.

### Trivial
None.

## Nice-to-Haves

- Show learning curves of evaluation performance (over training steps) for a subset of models to verify that the relative ordering between architectures is stable.
- Include DT fine-tuning and DT ICL baselines to complete those comparisons.
- Add confidence intervals or interquartile ranges to Figure 2.
- Run a subset of latency experiments on embedded hardware (e.g., Nvidia Jetson) or at least discuss the expected transfer.
- Report total GPU hours spent to help assess the computational cost.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

1. **"Misleading framing of inference complexity"** — The paper correctly states at line 362: "The Transformer with KV-caching has a linear time complexity per step and quadratic in the sequence length." This is accurate. The critic's claim that the paper mischaracterizes inference complexity is factually wrong. **Removed.**

2. **"UMAP is decorative"** — UMAP visualization is a standard qualitative tool for analyzing learned representations. While not quantitative evidence for downstream performance, it provides useful insight into representation quality. Characterizing it as merely "decorative" is overly dismissive. **Removed.**

3. **"Should note other Transformer variants (sliding window attention, FlashAttention)"** — The paper already uses FlashAttention (line 359) and KV-caching. Requesting every possible Transformer variant is outside the paper's scope and would be an unbounded comparison. **Removed.**

4. **"Action-removal ablation should be checked"** — The paper does check this in Section "Removing Actions & Effect of Context Length," finding that removing actions helps both backbones. The critic appears to have missed this section. **Removed.**

5. **"Computational budget missing GPU hours"** — The paper reports updates, batch size, and context length, enabling compute estimation. GPU hours are a nice-to-have but not a weakness. **Removed.**

6. **"In-context learning claim is unsupported"** — The critic claimed the ICL claim about state-tracking is unsupported, but the paper's comparison of xLSTM [7:1] vs. [1:0] (with and without sLSTM blocks) does provide evidence for the state-tracking advantage. The absence of a Transformer baseline is a separate issue (tracked in Weakness #3). **Partial removal: the state-tracking claim is supported; the general ICL advantage over Transformers is not.**

## Novel Insights

The most useful observation across the reviews that is distinct from the paper's own contributions is the framing of the convergence issue: the paper conducts a fixed-budget comparison but then discusses "final performance" as if it reflects asymptotic behavior. A recognition that the main experiment is a *compute-efficiency* comparison at a fixed budget — not necessarily a *final-performance* comparison — would make the paper's claims more precise and better aligned with the evidence. The reviews collectively surface that this ambiguity between "better under a fixed budget" and "better asymptotically" is the paper's central evidential gap.

## Suggestions

1. **Reframe the performance claim.** Change language like "final performance" and "better suited" to describe a fixed-budget advantage. Add learning curves for evaluation scores over training steps (even for a subset of model sizes, e.g., 16M and 206M) to show whether the relative ordering is stable.
2. **Add missing baselines.** Run DT fine-tuning and DT-based ICL on the same Dark-Room setup to directly compare recurrent vs. Transformer for those settings.
3. **Add variance information.** Include error bars (e.g., bootstrap CIs across tasks) on the main scaling figure.
4. **Discuss the hardware gap.** Acknowledge that A100 tests may not directly reflect embedded deployment and discuss which aspects of the advantage are architecture-level (memory, O(1) per-step cost) vs. hardware-dependent.
