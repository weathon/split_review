- Decision: Reject
- Avg Score: 5.60
- Scores: 8, 6, 3, 6, 5
Now I have a thorough understanding of the paper and the reviews. Let me compose the final consolidated review.

## Summary

This paper introduces **Zebra**, a generative autoregressive transformer for solving parametric PDEs. The method uses a VQ-VAE to discretize physical states into tokens, then pre-trains a causal transformer (Llama architecture) on sequences that concatenate multiple trajectories from the same dynamics—i.e., in-context pretraining. At inference, Zebra can be conditioned on context trajectories (one-shot) or a few past frames (zero-shot temporal conditioning) to predict future states without any gradient-based adaptation. Experiments are conducted on 7 PDE datasets (5 in 1D, 2 in 2D) against meta-learning (CODA, CAPE) and temporal-conditioning (MPP) baselines.

## Strengths

1. **Unique combination of capabilities (adaptive conditioning + temporal conditioning + in-context learning without gradient updates).** Table 1 clearly shows that Zebra is the only method among those compared that supports all three criteria. CAPE requires parameter values as input (no adaptation), CODA only supports adaptation via gradient steps on a context vector, and MPP requires retraining for different input lengths. This is the paper's core contribution and is well-motivated.

2. **Competitive one-shot adaptation results, particularly on challenging 2D PDEs.** In Table 2, Zebra achieves the lowest relative L² error on Wave b (0.245 vs next best 0.971), Wave 2D (0.207 vs 0.271), and Vorticity 2D (0.119 vs 0.678), while CAPE diverges on both 2D datasets. These are large margins and demonstrate that in-context pretraining can handle complex parametric variations where gradient-based methods fail.

3. **Demonstrated flexibility in temporal conditioning across context sizes.** Table 3 shows that Zebra achieves best or second-best L² on 5 of 7 datasets when conditioned on 2 frames. More importantly, the paper shows that MPP[3] (trained on 3 frames) degrades sharply when tested on 2 frames (e.g., L² of 0.919 vs 0.0075 on Advection), while Zebra handles arbitrary context sizes without retraining. This directly supports the flexibility claim.

4. **Consistent improvement from adding context examples.** Figure 3 (zero-shot vs one-shot) shows that providing one additional context trajectory consistently reduces rollout error across all datasets. The improvement is dramatic on Wave b (from near-random to accurate), providing direct evidence that the in-context pretraining strategy works as intended.

## Weaknesses

### Fatal

None.

### Major

1. **No reported VQ-VAE reconstruction error.** Zebra's entire pipeline depends on the VQ-VAE encoding-decoding step. The paper trains the VQ-VAE to minimize Relative L² loss but never reports the achieved reconstruction error (neither training nor test) for any dataset. This makes it impossible to decompose the overall prediction error into VQ-VAE distortion vs. transformer prediction error. If the VQ-VAE reconstruction error is large, the transformer's low L² on the full trajectory could be misleading (or, conversely, if it is small, the transformer is the bottleneck). Reporting this separately is standard practice for VQ-based generative models and is needed to properly interpret the results.

### Minor

2. **Missing standard operator-learning baseline for the temporal conditioning setting.** The zero-shot temporal conditioning task (predict future states from 2 past frames) is a standard setting where a method like the Fourier Neural Operator (FNO) trained on the same parametric distribution would be a natural reference point. While MPP is a strong transformer-based baseline and the paper's contribution is about in-context learning (not raw accuracy), including FNO would help calibrate the significance of the results against a widely-known PDE-solving method. This omission weakens the comparison but does not invalidate the paper's core claims.

3. **Limitations section is empty.** The paper contains no discussion of its own limitations (e.g., sensitivity to codebook size, autoregressive error accumulation, computational cost relative to baselines, dependence on training environment distribution). Acknowledging limitations is standard practice and would strengthen the paper's credibility.

4. **Figure 2 (context vs. loss) lacks error bars.** The paper shows rollout loss as a function of the number of context examples but plots a single trajectory per condition despite acknowledging "noticeable variance" and stating the analysis "would benefit from being conducted with more than a single sample." This should have been addressed before submission.

### Trivial

None.

## Nice-to-Haves

- An ablation quantifying VQ-VAE reconstruction error separately would significantly strengthen the paper.
- An analysis of autoregressive error accumulation over rollout length for Zebra vs. iterative baselines.
- A direct efficiency comparison (inference time, memory) between Zebra (no gradient steps) and CODA/CAPE (with gradient steps), to quantify the claimed flexibility advantage.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Overclaimed novelty / missing related work.** The harsh critic claimed the paper overstates its novelty by not citing other generative models for PDEs (diffusion models, score-based models, GraphCast). *Removed because:* The paper's claim is specifically about "generative modeling **using quantized representations**" and "first adaptation of generative **auto-regressive transformers**" to physical dynamics—both qualifiers distinguish it from diffusion/score-based approaches. The criticism failed to identify a specific work that uses the same approach. GraphCast operates on a grid without discrete tokenization and targets weather, not general PDEs. The paper also includes "up to our knowledge" qualifiers. This criticism misunderstands the specificity of the claim.

2. **Baseline implementation details insufficient.** The harsh critic argued that gradient steps, learning rates, and initialization for baselines are not reported. *Removed because:* These details are typically placed in the appendix (referenced as \Cref{section:archi-details}), which is stripped by the parser. The paper describes the adaptation procedure clearly ("learning a context c^e with gradient updates"). Following the hard rules, reproducibility nitpicks about hyperparameters for baselines are removed.

3. **Confidence level metric is flawed.** The harsh critic argued that the "confidence level" metric can be high simply because the model is very uncertain. *Removed because:* The paper explicitly acknowledges this trade-off: "When modeling uncertainty, the model achieves a tradeoff between the quality of the mean prediction approximation and the guarantee for this prediction to be in the corresponding confidence interval." The analysis is presented as a characterization of this tradeoff, not as a claim of superior calibration.

4. **The paper's claim of "superior performance" is overstated.** *Removed because:* While the abstract uses "superior performance," the paper's detailed discussion is balanced—it notes where Zebra is best (2D cases, Combined) and where it is second-best (Heat, Advection). The results show Zebra is competitive, not uniformly dominant.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any novel observation about the method or results that the paper itself does not already state.

## Suggestions

1. **Report VQ-VAE reconstruction error separately for each dataset** (in both relative L² and a per-token accuracy metric). This is the single most important addition to the paper.
2. **Add FNO as a baseline** for the temporal conditioning setting, or at minimum discuss why it is excluded relative to the paper's claims.
3. **Add a brief limitations section** discussing codebook size sensitivity, autoregressive error accumulation, and computational cost.
4. **Include error bars or multiple-run statistics** in Figure 2, or replace the figure with a more robust analysis.
