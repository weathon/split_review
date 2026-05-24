Now I have enough context to write the final review. Let me synthesize everything.

---

## Summary

This paper introduces DelRec, the first surrogate gradient learning (SGL) method for training per-neuron delays in recurrent connections of spiking neural networks. The core technique is a differentiable interpolation scheme using a triangle spread function with an annealed width parameter σ, which allows real-valued delays to be learned via backpropagation and then rounded to integers at inference. The method achieves new state-of-the-art results on the SSC dataset (82.58% ± 0.08%, 3 seeds) and PS-MNIST (96.21%, single seed) using simple LIF neurons, and provides a thorough functional study on SHD demonstrating that learned recurrent delays are more parameter-efficient than feedforward delays.

## Strengths

- **Novel, well-executed method**: The scheduling matrix + triangle spread function (Eq. 9–11) is a clean design that handles non-integer delays during training and reduces cleanly to integer delays at inference. The σ-annealing strategy provides a principled coarse-to-fine optimization. This is the first SGL-based approach for per-neuron recurrent delays, filling a clear gap in the SNN toolbox.

- **Strong, reproducible SSC results**: On the Spiking Speech Commands dataset — a large (100k+ samples), far-from-saturated benchmark with dedicated train/validation/test splits — DelRec achieves 82.58% ± 0.08% over 3 seeds using only simple LIF neurons and 0.37M parameters. This convincingly surpasses all prior LIF-derived models, including those with adaptive neurons (SE-adLIF: 80.44%, SiLIF: 82.03%), feedforward delays (DCLS: 80.69%), and the ASRC-SNN baseline (81.54%). The use of multiple seeds and a clean train/validation/test split makes this the paper's strongest empirical result.

- **Rigorous ablation on SHD**: The functional study uses a 20% validation split and 10 seeds, comparing vanilla SNN, vanilla RSNN, fixed random delays, learned feedforward delays, learned recurrent delays, and their combination (Fig. 3). The results show that learned recurrent delays yield consistent and significant improvements over fixed delays and that recurrent delays degrade more gracefully than feedforward ones under parameter constraints. The paper also responsibly notes that SHD is saturated and recommends it only for proof-of-concept studies.

- **Clear algorithmic specification**: The method is fully described with equations (1–13), an explicit algorithm, and released code. Hyperparameters are documented (referenced to appendix), making reproduction straightforward.

## Weaknesses

### Fatal

None.

### Major

- **PS-MNIST evaluation is insufficient to support a SOTA claim**: The paper reports a single training run (96.21%) on PS-MNIST without a held-out validation set. The improvement over the reproduced ASRC-SNN baseline (95.77%) is only 0.44 percentage points. The paper justifies this by noting that "all the previous state-of-the-art models on the dataset" also report single seeds (line 190), but a new method claiming SOTA should provide stronger evidence — multiple seeds with mean and standard deviation, and ideally validation-set model selection. This does not invalidate the method (the SSC and SHD results provide independent, rigorous support), but it weakens one of the two pillars of the paper's central empirical narrative. The abstract's unqualified "new state-of-the-art" claim for PS-MNIST is overstated given this evidence.

- **The gradient propagation hypothesis from Figure 1B is never empirically tested**: The introduction claims that recurrent delays "may mitigate gradient challenges by implementing temporal skip connections, improving gradient propagation during training" (line 80) and Figure 1B illustrates this idea, but the paper provides no gradient norm measurements, effective-depth analysis, or any empirical test of this claim. This leaves a motivating intuition unverified.

### Minor

- **Abstract does not qualify the SOTA claim**: The abstract states "new state-of-the-art (SOTA) on two challenging temporal datasets" without noting that models with substantially more complex neuron dynamics (multi-compartment, attention-based, GRU-based) are excluded from the comparison. The main text does include this qualification (line 190–191 and footnote 1), making the abstract's unqualified framing misleading.

- **Architecture asymmetry in the feedforward vs. recurrent delay comparison**: In the SHD functional study, feedforward delays are applied between the two hidden layers while recurrent delays operate within the second hidden layer (Fig. 3A, line 267–268). The conclusion that "recurrent delays can achieve better performance than feedforward delays" is supported in this specific configuration, but the architectural mismatch means the comparison is not fully controlled — the two delay types operate on different parts of the computation graph. This limits the generality of the claim.

- **No discussion of computational/memory cost**: The method's scheduling matrix scales with the maximum delay plus σ (Eq. 13), which grows during early training. While the paper notes that the support narrows as σ decreases, it never quantifies the memory overhead or runtime compared to a vanilla RSNN, which matters for practical adoption.

### Trivial

- The σ decay schedule is referenced to the appendix (A.2.5) but the specific schedule (initial value, decay rate, final value) is not mentioned in the main text. The paper would benefit from stating at minimum the initial σ value (visible in Fig. 2C as σ=5) and the decay strategy.

## Nice-to-Haves

- An ablation where σ is held fixed (e.g., σ=0 or σ=constant) would demonstrate that the progressive smoothing schedule is indeed necessary for effective delay learning, rather than simply the presence of differentiable interpolation.
- Characterizing the learned delay distributions (e.g., histograms, correlation with spike patterns) would provide insight into what temporal strategies the network discovers, strengthening the narrative beyond accuracy numbers.
- A short limitations paragraph acknowledging the memory cost of the scheduling buffer for very long sequences would make the paper more balanced.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's demand for PS-MNIST validation split and multiple seeds as a "critical evidential gap"**: While this is a genuine weakness (retained above as Major), the harsh critic's framing that it makes the paper's "central empirical message incomplete" is too strong. The SSC results with 3 seeds and the SHD results with 10 seeds provide independent, rigorous evidence for the method's effectiveness. The PS-MNIST single seed is a weakness, not a fatal flaw.

- **Harsh critic's note about "the paper never discusses practical memory cost or runtime"**: Retained as Minor because it's a real omission, but the harsh critic's speculation about "extremely long sequences" is speculative — the benchmarks used (SSC, PS-MNIST, SHD) all have moderate sequence lengths where this is unlikely to be a bottleneck.

- **Strength Finder's claim that the paper achieves "SOTA on all three benchmarks"**: Softened. The SHD result is explicitly not claimed as SOTA by the paper itself (the authors note saturation and exclude SHD from Table 1). The PS-MNIST SOTA claim is weakened by the single-seed evaluation.

- **Strength Finder's generic praise**: Removed "the paper addressed an important problem" and similar generic statements that lack concrete anchors in the paper.

- **Harsh critic's note about missing appendix details (sigma schedule)**: The appendix is stripped in the parser output. The paper references appendix A.2.5 for hyperparameters; this is not an author error. Moved to Trivial with the note that main-text mention would help.

- **Harsh critic's suggestion to "characterize the learned delays" and "directly probe the gradient-propagation claim"**: These are reasonable suggestions but are scope creep — they ask the paper to become a different type of paper with additional empirical analyses. Moved to Nice-to-Haves.

## Novel Insights

The paper's key insight — that per-neuron recurrent delays can be learned via SGL by using a future-oriented scheduling matrix combined with an annealed spread function — is genuinely novel and practically useful. Beyond the paper's own contributions, the finding that recurrent delays remain robust under aggressive parameter reduction (while feedforward delays degrade) suggests that recurrent temporal structure may be a more parameter-efficient way to encode temporal dependencies than feedforward temporal structure. This has implications beyond SNNs for the design of any temporally-structured recurrent architecture.

## Suggestions

- Run PS-MNIST with at least 3 seeds, report mean ± std, and use a validation split (e.g., hold out 10k from the training set). This is low-cost and would substantially strengthen the paper's weakest empirical result.
- Add a sentence to the abstract qualifying the SOTA claim to match the careful wording in Section 3.1 (e.g., "among models without substantially more complex neuron dynamics").
- Either remove the gradient-propagation hypothesis from the introduction or add a brief measurement (e.g., gradient norm comparison between vanilla RSNN and DelRec at different time lags) in the functional study.
- Quantify the memory footprint of the scheduling matrix relative to a vanilla RSNN for the SSC configuration, even as a brief note in the main text.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Delay Neural Networks (DeNN) — `pIJR9uPjy3` | 4.50 | R1-mid | Rejected; similar topic but less developed method, weaker results |
| SOLO — `vq75kRCYuY` | 4.00 | R1-mid | Rejected; SNN training method, less competitive results |
| Spiking Vision Transformer — `qzZsz6MuEq` | 6.60 | R2 | Accepted; novel attention for SNN-ViTs, SOTA results but weaker ablations and less rigorous evaluation than DelRec |
| Temporal Flexibility in SNNs — `9HsfTgflT7` | 6.20 | R2 | Accepted; novel training method, but weaker performance gains, unclear motivation-experiment alignment |
| SpikeLLM — `ZadnlOHsHv` | 7.00 | R2 | Accepted; scaling SNNs to LLMs, more ambitious scope |
| Barrel Cortex Model — `UvfI4grcM7` | 6.75 | R2 | Accepted; biologically constrained model, different contribution type |
| Predictive Coding Networks — `sahQq2sH5x` | 7.33 | R2 | Accepted; benchmarking + method, strong engineering contribution |
| Kuramoto Oscillatory Neurons — `nwDRD4AMoN` | 9.00 | R1-high | Much stronger; theoretical depth + broad empirical validation |

**Round 1 bracket**: Between 5.0 and 7.5. The paper is clearly stronger than the 3.0–4.5 range (rejected SNN papers with weaker methods/results) and clearly weaker than the 8.0+ range (papers with theoretical depth or transformative scope).

**Round 2 narrowing**: DelRec is stronger than Temporal Flexibility (6.20) — it has clearer motivation, stronger empirical results, and better-aligned experiments. It is comparable to or slightly stronger than the Spiking Vision Transformer (6.60) — DelRec has more rigorous evaluation (multiple seeds, validation splits, thorough ablation) and a cleaner method, though the Spiking ViT has a more ambitious architectural contribution. DelRec is roughly comparable to SpikeLLM (7.00) in quality — different contribution types, but both are solid method papers with strong benchmarks.

**Final placement**: 7.0. The method is genuinely novel and well-executed, the SSC and SHD evaluations are rigorous, the ablation study is informative, and the paper is clearly written. The PS-MNIST single-seed weakness and the unqualified abstract partially offset the strengths, preventing a score in the 7.5–8.0 range, but the core contribution is solid and well-supported by the independent SSC and SHD evidence.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>