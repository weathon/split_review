- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes MambaExtend, a method to improve long-context performance of Mamba models by learning per-layer (or per-channel) scaling factors for the discretization step Δ_t, calibrated via either backpropagation or zeroth-order optimization. The key insight—that OOD discretization steps at long contexts cause Mamba's failure, and that scaling them down can mitigate this—is well-motivated through empirical analysis (Fig. 2, Fig. 3). The method requires orders of magnitude fewer parameter updates than full fine-tuning (e.g., ~L or L×D scaling factors vs. all model parameters) and is evaluated on perplexity (Pile, PG-19), LongBench, and passkey retrieval.

## Strengths

1. **Identification of OOD discretization as the root cause of Mamba's long-context failure.** Section 3 and Figure 2 empirically demonstrate that ∑Δ_t grows with context length and varies substantially across layers. Figure 3 shows that uniformly scaling Δ_t down reduces PPL from ~268 to ~23.5 at 32k, providing direct causal evidence that Δ_t is the right lever. This motivational analysis is clear and convincing.

2. **Dramatic parameter efficiency with competitive performance.** MambaExtend calibrates only L or L×D scaling factors (a few hundred to a few thousand parameters). On passkey retrieval (Fig. 5), it achieves accuracy comparable to or better than full fine-tuning and DeciMamba while updating ~3500×–7100× fewer parameters. On PG-19 (Fig. 4), it improves PPL by up to ~40.6% over DeciMamba.

3. **Zeroth-order optimization performs on par with backpropagation.** Table 4 (described in text) shows that CF_ZO and CF_BP yield nearly identical perplexity (e.g., ~14.80 vs. ~14.81 at 32k). This supports the practical claim that a gradient-free, forward-pass-only calibration is sufficient, making the approach accessible in memory-constrained settings.

4. **Ablation on scaling granularity provides actionable design insight.** Table 3 systematically compares per-tensor, per-token, and per-channel sharing of scaling factors. Per-channel sharing achieves strong retrieval accuracy while per-tensor (one scalar per layer) fails, validating the need for channel-level granularity.

## Weaknesses

### Fatal
None. No identified weakness invalidates the paper's core claims. The method demonstrably reduces PPL and improves retrieval accuracy at extended contexts using very few additional parameters.

### Major

1. **Missing experimental details that hinder reproducibility.** The paper mentions using SPSA (Spall, 1992) for zeroth-order optimization but does not specify the perturbation size (ε), learning rate, number of iterations, or any SPSA-specific hyperparameters. The paper also does not specify the hidden dimension D for Mamba-130M or Mamba-1.4B (needed to understand per-channel scaling factor counts), the optimizer and hyperparameters used for fine-tuning baselines, or the convergence criteria. These omissions make it impossible to independently reproduce the results.

2. **No DeciMamba baseline reported on LongBench.** Table 2 compares Mamba vs. MambaExtend on 7 LongBench tasks, reporting a 6.03% average improvement. However, DeciMamba—the primary baseline the paper compares against elsewhere—is absent from this table. Since LongBench is the main long-context benchmark used in the paper, this is a significant evidential gap for the claim of superiority over DeciMamba.

3. **"Training-free" terminology is misleading.** The paper repeatedly calls MambaExtend "training-free" (abstract, Section 4, conclusion). However, the method requires calibration on data (20 samples for PPL, 10 for LongBench, one epoch for retrieval), with learned scaling factors that are data-dependent. This is not zero-shot or training-free—it is parameter-efficient calibration. The terminology sets unrealistic expectations and should be qualified (e.g., "without full model fine-tuning" or "calibration-based").

4. **No error bars or variance reported for passkey retrieval.** Figure 5 reports retrieval accuracy for MambaExtend vs. baselines, but no standard deviations, confidence intervals, or multiple-seed results are provided. Given that the differences between methods are in the 5–20% range, it is unclear whether these differences are statistically significant. This weakens the reliability of the claimed superiority over DeciMamba and full fine-tuning.

### Minor

1. **No explicit comparison of per-layer learned scaling vs. best uniform scaling.** The motivational experiment (Fig. 3) shows that the best uniform scaling achieves PPL ~23.5 at 32k for Mamba-1.4B, while Table 1 (presumably) shows MambaExtend achieving ~14 PPL at 32k. However, these results are in different figures/tables and are never directly tabulated side-by-side. A clean comparison would strengthen the motivation for per-layer scaling over a single global scalar.

2. **The relationship between learned scaling factors and per-layer Δ_t norms is not analyzed.** The paper shows that Δ_t accumulation varies by layer (Fig. 2) and that MambaExtend reduces it (Fig. 7), but never directly demonstrates that the learned scaling factors correlate inversely with per-layer Δ_t norms. Doing so would validate the intuition that different layers need different scaling.

3. **Missing uniform-per-layer baseline for passkey retrieval.** Table 3 shows per-channel, per-token, and per-tensor scaling for retrieval, but does not include a "single global scalar" baseline (one scalar across all layers and channels). This would contextualize whether even per-tensor (one per layer) provides benefit over a single uniform scalar.

### Trivial
- Figure 2's y-axis uses a logarithmic scale but is not labeled.

## Nice-to-Haves
- A systematic experiment testing generalization across unseen context lengths (e.g., calibrate at 4k, evaluate at lengths from 8k to 64k) would strengthen the OOD generalization claim beyond what the passkey retrieval experiment already partially provides.
- A brief discussion of when scaling Δ_t might fail (e.g., tasks requiring very fine-grained long-range memory where reducing Δ_t could hurt retention of distant tokens) would add depth.
- A theoretical connection from Δ_t scaling to the decay factor exp(−∑Δ_t A) and its impact on effective state space could deepen the contribution beyond the empirical analysis.

## Removed Points

- **"PPL numbers are implausible and may be meaningless"** (Harsh Critic #1): The paper is transparent about the baseline PPLs (~1e6 for Mamba-130M at 70k). These extreme values are precisely the problem the method aims to solve; they are not presented deceptively. The passkey retrieval task provides a complementary metric that is not subject to this concern. Removed because the criticism is a misunderstanding of the paper's motivation — the high baseline PPL is the finding that motivates the work, not a flaw in the evaluation.

- **"Comparison fairness with DeciMamba — one epoch may not be enough"** (Harsh Critic #2, partially): The paper explicitly states that all methods are trained for the same number of epochs to ensure fair comparison under equal compute budget (lines 113, 119). The critic's claim that DeciMamba's original paper "likely uses more extensive training" is speculative and not grounded in the paper's content. Per Hard Rules, speculative claims about what might happen under different training regimes are removed. However, the valid sub-point (missing DeciMamba on LongBench) is retained as a Major weakness.

- **"The 5.42e6× ratio is a trivial consequence of design choice"**: This is not a weakness — the paper's contribution is precisely that such a small number of parameters suffices, which is not obvious a priori. The ratio is a meaningful empirical finding, not a triviality.

- **"No transformer baselines"**: The paper is about extending Mamba models, not comparing Mamba to transformers. Requesting transformer baselines is scope creep beyond the paper's stated contribution.

- **Missing appendix/proofs**: The parser strips these; they exist in the original submission.

- **Formatting/style nitpicks**: Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The paper's core observations—that OOD Δ_t accumulation is the root cause of Mamba's long-context failure, that per-layer learned scaling of Δ_t suffices to mitigate this, and that zeroth-order optimization works as well as backpropagation for this tiny parameter set—are novel and clearly communicated. The reviews do not surface additional insights beyond what the paper already provides.

## Suggestions

**Specific actionable suggestions for improvement:**

1. **Add a dedicated "Experimental Setup" subsection** that specifies: (a) SPSA hyperparameters (perturbation size ε, learning rate, convergence iterations), (b) the hidden dimension D for each model size, (c) optimizer and learning rate for fine-tuning baselines, and (d) the calibration context length for each evaluation setting.

2. **Add DeciMamba results to the LongBench table.** Without this, the main long-context benchmark comparison is incomplete.

3. **Run passkey retrieval with 3–5 random seeds** and report standard deviations or confidence intervals. This is critical for establishing the reliability of the claimed improvements.

4. **Replace or qualify "training-free"** throughout the paper with a more precise term such as "without full model tuning" or "calibration-based." This is a simple terminological fix that would prevent reader confusion.

5. **Add a direct comparison table** showing: pre-trained baseline at 2k, best uniform scaling at 64k, and MambaExtend at 64k (per-layer scaling). This would cleanly demonstrate the value of non-uniform scaling over the best single scalar.
