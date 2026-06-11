## Summary

WARP introduces a novel sequence modeling paradigm that uses the weights of an auxiliary MLP as the hidden state of a linear RNN, driven by input differences. The core idea — blending linear recurrence in weight-space with nonlinear decoding through the root MLP — is genuinely novel and clearly formulated. The paper evaluates this architecture across image completion, time series forecasting, dynamical system reconstruction, and classification.

## Strengths

1. **Genuinely novel architectural paradigm (Eq. 1, Figure 1)**: The paper's core idea — treating the weights of an auxiliary MLP as the hidden state of a linear recurrence, driven by input differences — is clearly distinct from standard RNNs, SSMs, and Transformers. The formulation is simple and implementable, and the paper appears to be the first to explore weight-space features as intermediate hidden state representations in a recurrence.

2. **WARP-Phys demonstrates meaningful physics-informed modeling (Table 3)**: On the Mass-Spring-Damper systems, WARP-Phys achieves MSE 0.03±0.04 vs. the next-best Transformer at 0.34±0.12 (an ~11× improvement), and on MSD-Zero achieves 0.04±0.01 vs. WARP's 0.32±0.02. These results are valid on their own terms and demonstrate the benefit of injecting domain knowledge into the root network.

3. **Principled initialization strategy (Section 2.2)**: Initializing A=I and B=0 is well-motivated by connections to gradient descent and residual networks, with a clear rationale for gradient flow during backpropagation through time.

4. **Broad empirical evaluation across diverse domains**: The paper evaluates on image completion (MNIST, CelebA), energy forecasting (ETT), traffic forecasting (PEMS08), dynamical system reconstruction (MSD, MSD-Zero, LV, SINE), multivariate time series classification (UEA, 6 datasets), and in-context learning — covering a wide range of sequence modeling settings.

## Weaknesses

### Fatal
None.

### Major

1. **CelebA image completion results are unreliable (Table 1)**. Two problems are evident from the reported numbers:
   - **WARP achieves negative BPD** (−0.043 at L=300, −0.162 at L=600). While negative BPD is technically possible under the simplified NLL in Eq. (2) when σ is driven pathologically small (the reviewer's claim that this is "impossible" is incorrect — the simplified NLL omits the 0.5·log(2π) constant, allowing log σ to dominate negatively), this is a clear sign of degenerate, overconfident uncertainty estimates. The paper provides no discussion of this pathology.
   - **LSTM reports BPD=3869 at L=100** while the same model achieves 7.276 and 7.909 at L=300 and 600 — a ~500× swing that strongly suggests an evaluation implementation issue.
   
   Whatever the cause, the CelebA comparison — a flagship generative modeling experiment — cannot be interpreted as trustworthy evidence of WARP's generative quality. This significantly weakens the overall empirical case.

2. **PEMS08 result is extraordinary and insufficiently analyzed (Table 2)**. WARP achieves MAE 6.59 and RMSE 10.10 — over 50% better than the best graph-aware model (STDCN: 13.45/23.28) *without using graph structure*. A result of this magnitude, if true, would fundamentally change the traffic forecasting field. But the paper provides no error bars, no analysis of whether data splits and evaluation protocols match prior work, and only briefly mentions a "non-causal convolution" preprocessing step deferred to an appendix the reviewer cannot access. Without further scrutiny, this result cannot be taken at face value.

3. **Selective baselines on ETT (Figure 3b)**. The ETT comparison includes only GRU and LSTM — architectures from 2014–2017. Modern SSMs (S4, Mamba), Transformers, and other competitive baselines are absent. The paper compares WARP against S4 on MNIST but provides no explanation for excluding SSMs and Transformers from this benchmark, making the claimed "superiority" on ETT weak.

4. **The "gradient-free adaptation" claim is overstated (Sections 1, 4.1)**. The θ_t update in Eq. (1) is simply the forward pass of a linear dynamical system. Calling this "gradient-free adaptation" conflates feedforward computation with genuine test-time adaptation. Standard in-context learning in Transformers also operates without gradients at inference time, and the paper's own footnote 2 concedes that gradients may still be needed for finetuning. The claimed advantage is not unique to WARP.

5. **In-context learning experiment is a toy (Section 3.4)**. The ICL task uses only 32 tokens on a simple linear regression problem. The cumulative-sum preprocessing changes the task structure. The claim about extracting θ_{T-1} for subsequent queries without re-evaluation is described but never empirically verified.

### Minor

1. **WARP underperforms significantly on EigenWorms (Table 4)**: At 70.93% vs. LinOSS 95.0% on the longest sequence (17,984 steps), WARP is near the bottom of the table. The paper attributes this to "not being designed with long-range dependencies in mind," which undercuts the paper's own argument that weight-space recurrence provides superior memory.

2. **A matrix scaling constraint is structural (Section 2.2, 4.2)**: The transition matrix A is D_θ × D_θ, growing quadratically with root network size. The paper acknowledges this as a limitation, but the future work suggestions (low-rank diagonal parametrizations) would make the method structurally resemble existing SSMs. This doesn't invalidate current results but limits the paradigm's practical scalability and future direction.

3. **WARP-Phys embeds the ground-truth function on SINE (Section 3.2)**: On the SINE dataset, the root network hard-codes sin(2πτ+φ̂), the exact target function form. The MSD results (where no such formula is hard-coded) remain valid, but the "10x improvement" framing benefits from this SINE-specific design choice.

4. **No evaluation on standard long-sequence benchmarks**: Without Long Range Arena or similar benchmarks, it is difficult to assess WARP's long-range capability relative to the SSM literature it positions itself against.

### Trivial
None.

## Nice-to-Haves
- Controlled ablation: compare WARP against a standard linear RNN with hidden state h_t ∈ ℝ^{D_θ} decoded by a fixed-topology MLP, to isolate the benefit of the weight-space representation over simply having a large hidden state.
- Ablation of input difference mechanism vs. direct inputs x_t.
- Demonstrate the convolutional mode's wall-clock training speed vs. recurrent mode.
- Error bars and detailed protocol information for PEMS08.

## Removed Points
- **Criticism that negative BPD is "mathematically impossible"**: Removed because the simplified NLL in Eq. (2) can produce negative values when σ is very small (the constant term 0.5·log(2π) is omitted, and log σ can dominate negatively). The concern about degenerate uncertainty estimates is real, but the absolute impossibility claim is factually incorrect.
- **Criticism about missing related works**: Removed per instructions — cannot verify whether works exist.
- **Formatting/style nitpicks**: Removed as parser artifacts.
- **Criticism about WARP-Phys not being evaluated on LV**: Removed from weaknesses — the paper explicitly explains that the LV repeat-copy protocol introduces discontinuities incompatible with the physical prior. This is a reasonable scoping choice.
- **Strength Finder's generic claims** (e.g., "important problem", "timely direction"): Removed as superficial/non-specific.
- **Claim that the abstract's "10x" is misleading because it refers to SINE**: The 10x improvement is on MSD (MSE 0.03 vs. Transformer 0.34), where no target function is hard-coded. This is a valid comparison.

## Novel Insights
None beyond the paper's own contributions. The evaluation anomalies (CelebA BPD values, PEMS08 verification gap) are directly observable from the reported numbers and do not require novel insight beyond careful reading.

## Suggestions
1. Fix or remove the CelebA experiment — the negative BPD values and anomalous baseline numbers make this comparison unreliable as evidence of generative modeling quality.
2. Provide detailed replication information for PEMS08, including data splits, preprocessing steps, evaluation protocol, and error bars. If the result holds under rigorous scrutiny, document it properly.
3. Add modern baselines (S4, Mamba, Transformer) to the ETT comparison to make the claimed superiority meaningful.
4. Tone down the "gradient-free adaptation" rhetoric — the θ_t update is the forward pass of a linear RNN, not adaptation beyond standard inference.
5. Add the controlled ablation (standard linear RNN + nonlinear decoder) to isolate the benefit of the weight-space representation.

## Score and Decision

**Calibration:**

Round 1 (Bracketing): Compared against anchors across the score range:
- Weak (<3.5): kkVTeMvC9D (3.40), 9L9j5bQPIY (2.50), NYPJz0CL5X (3.00), ZyMXxpBfct (1.50) — all clearly weaker than WARP.
- Middle (3.5–7.5): hgjpO0H0id (4.00, Reject, limited theory paper), iVy7aRMb0K (4.50, Reject, incremental initialization), QFgbJOYJSE (5.75, Accept, theory paper with limited experiments), DjeQ39QoLQ (6.50, Accept, strong theory+experiments).
- Strong (>7.5): PdaPky8MUn (8.00), GRMfXcAAFh (8.00), tyEyYT267x (8.00), OvoCm1gGhN (8.00) — all clearly stronger than WARP.

Initial bracket: 4.5–6.0.

Round 2 (Narrowing): Compared against:
- orEX9GKQAD (4.00, benchmark paper, Reject) — weaker than WARP.
- DQfHkEcUqV (4.75, extrapolative sequences, Reject) — comparable but less ambitious.
- vcJiPLeC48 (6.00, gradient-free RNN, Reject) — similar overclaiming issues, less architectural novelty.
- XoYdD3m0mv (6.00, ProbeGen, Accept) — cleaner, better-scoped weight-space paper.
- xwKt6bUkXj (6.75, emergent mechanisms, Accept) — solid but different domain.

WARP is clearly above the 4.0–4.5 rejected papers (more architectural novelty, broader experiments) but below the 5.75–6.5 accepted papers (evaluation issues, overclaiming). The closest comparable is the gradient-free RNN paper at 6.0 (rejected for overclaiming and limited validation), but WARP has more architectural novelty, placing it slightly below that paper's score.

**Final score: 5.0** — The architecture is genuinely novel and the evaluation is broad, but the combination of unreliable flagship experiments (CelebA), an extraordinary unverified result (PEMS08), selective baselines on key benchmarks (ETT), and consistently overstated rhetoric prevent acceptance in the current form. The paper would need substantial revisions to be publishable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>