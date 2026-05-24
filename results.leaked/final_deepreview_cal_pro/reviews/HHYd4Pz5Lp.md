Now I have sufficient calibration data. Let me compile the final review.

---

## Summary
This paper introduces DelRec, the first method to learn transmission delays in recurrent connections of spiking neural networks (SNNs) using surrogate gradient learning (SGL). The core idea is a differentiable interpolation scheme (a triangular spread function with progressively tightening width) that enables backpropagation through discrete delay parameters, combined with a scheduling matrix for efficient spike routing. Using only simple LIF neurons, DelRec achieves strong results on SSC (82.58%) and PS-MNIST (96.21%), outperforming all prior models in the same neuron class, and provides a controlled functional study on SHD showing recurrent delays consistently surpass feedforward and fixed delays under resource constraints.

## Strengths
- **Novel and well-engineered method**: DelRec is the first SGL-based approach to learn axonal delays in recurrent SNN layers. The differentiable triangular interpolation (Eq. 9–11) with a progressively tightening spread parameter σ is a clean solution to the discrete-delay optimization problem, and the scheduling matrix mechanism (Algorithm 1) makes it practical to implement.

- **Strong empirical results on challenging benchmarks**: On SSC, DelRec achieves 82.58% (±0.08%) using only 0.37M parameters — better accuracy than all prior models in the simple-LIF class while using dramatically fewer parameters than comparable methods (e.g., DCLS at 2.5M). On PS-MNIST, it reaches 96.21% with 0.16M parameters.

- **Thorough functional study on SHD (Section 3.2, Figure 3)**: The controlled comparison across six model variants (vanilla SNN, vanilla RSNN, fixed random delays, learned feedforward delays, learned recurrent delays, and combined) convincingly isolates the contribution of recurrent delays. The scaling experiment showing recurrent delays maintain accuracy better under decreasing parameter counts is a genuine insight.

- **Transparent about limitations and exclusions**: The paper includes a clear footnote (p. 6) listing higher-scoring models that use more complex neuron architectures and explains the rationale for excluding them from the main comparison table. This honesty is commendable.

## Weaknesses

### Fatal
None.

### Major
- **State-of-the-art claim is unqualified in key places**: The abstract and conclusion state DelRec achieves "new state-of-the-art (SOTA)" on SSC and PS-MNIST without qualification. The paper's own footnote acknowledges that Wang et al. (2024) reach 83.69% on SSC and Chen et al. (2024) reach 97.78% on PS-MNIST — both higher than DelRec's numbers. The body of the paper (Section 3.1) does qualify the comparison as being among simple LIF-derived models, which is reasonable, but the abstract and introduction should carry that same qualification. This is a significant presentational issue because the abstract is what most readers see first, and an unqualified SOTA claim when higher numbers exist in the literature is misleading.

### Minor
- **PS-MNIST result based on a single training seed**: The 96.21% result on PS-MNIST is a single run. The justification that prior SOTA models on this dataset also used one seed does not make the result statistically reliable. With a margin of only ~0.4% over the previous best (95.77%), this could plausibly be noise. Multiple seeds with mean ± std would substantially strengthen the evidence. This is particularly important because PS-MNIST is one of the two headline benchmarks.

- **Gradient-mitigation claim lacks direct evidence**: Figure 1B and the accompanying text assert that "delays in recurrent connections reduce the risks of exploding or vanishing gradients." The paper provides only indirect evidence for this (random fixed delays improve RSNN training in Section 3.2). No gradient norm measurements or convergence analysis are reported. This claim should be presented as a hypothesis or motivation rather than an established benefit.

- **Interaction between feedforward and recurrent delays not fully analyzed**: On SSC, DelRec with only recurrent delays (82.58%) outperforms DelRec with both feedforward and recurrent delays (82.19%). This counterintuitive result — adding a capability degrades performance — is reported in Table 1 but never discussed. The paper also does not examine under what conditions combining delay types is beneficial versus when it hurts.

- **σ-annealing schedule and Algorithm 1 details deferred to appendix**: The paper references Algorithm 1 and mentions that σ decreases throughout training, but the specific schedule (initial value, decay law, final value) and efficient implementation details are entirely in the stripped appendix. A condensed description in the main text would improve readability.

### Trivial
- The paper uses the term "state-of-the-art datasets" to describe SSC and PS-MNIST (line 188), which is an odd phrasing — datasets aren't typically described as state-of-the-art.
- In the conclusion (line 291), "outperforms the previous state-of-the-art accuracy" again lacks scope qualification.

## Nice-to-Haves
- A brief gradient-norm tracking experiment on a small network (with vs. without learned delays) would directly support or refine the gradient-mitigation hypothesis.
- Discussing the memory footprint of the scheduling matrix — which stores future inputs over a window proportional to the maximum delay — would help practitioners assess scalability.
- Extending the PS-MNIST evaluation to 3+ seeds with reported mean ± std would be a low-cost but high-impact improvement.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Selective comparison / insufficient statistical support (evidential)" from harsh critic, framed as a fatal issue**: The paper does provide a transparent footnote listing higher-scoring excluded models and gives a reasonable scope qualification (simple LIF neurons vs. complex multi-compartment, attention-based, or distillation-based models). This is a presentational issue about where the qualification appears, not an evidential one. The harsh critic's claim that the paper "deliberately excludes models that obtain higher numbers" misrepresents the practice — the paper explicitly acknowledges those models and justifies the exclusion. Downgraded from fatal to major.

- **Harsh critic's concern about DCLS vs. DelRec hyperparameter fairness in the SHD study**: The critic speculates that "the comparison between feedforward and recurrent delays implicitly assumes that the hyperparameters of the competing delay-learning methods (DCLS vs. DelRec) are equally tuned." This is speculative — the paper describes comparable training procedures and the models use the same base architecture. Without evidence of unfair tuning, this concern is not substantiated. Removed.

- **Harsh critic's demand for 5 seeds instead of 3 for SSC**: Three seeds with reported standard deviation (0.08% for DelRec recurrent-only) is standard practice in this literature. Demanding 5 is a one-size-fits-all nitpick. Removed.

- **Strength Finder's claim about "setting new state-of-the-art"**: This strength conflicts with the verified weakness about the unqualified SOTA claim. The SOTA framing is valid only within the simple-LIF scope, which the paper sometimes fails to specify. This strength is retained but qualified.

## Novel Insights
The controlled SHD study reveals a non-obvious tradeoff: recurrent delays achieve better accuracy than feedforward delays at equivalent parameter counts, but feedforward delays reach their peak accuracy at lower firing rates. This suggests a practical design choice between maximizing accuracy (recurrent delays) and minimizing energy consumption (feedforward delays) that has not been previously characterized in the SNN delay-learning literature.

## Suggestions
- **Reframe the SOTA language precisely**: In the abstract and conclusion, explicitly state "new state-of-the-art among models using simple LIF neurons" or equivalent. The existing footnote is good practice but does not excuse the unqualified claim in the headline text.
- **Add multi-seed results for PS-MNIST**: Run at least 3 seeds and report mean ± std. This is straightforward and would substantially increase confidence in the headline result.
- **Discuss the SSC recurrent-only vs. combined result**: The fact that adding feedforward delays to an already recurrent-delay model slightly hurts SSC performance deserves analysis. Even a brief hypothesis would improve the paper.
- **Tone down the gradient-mitigation claim**: Rephrase Figure 1B's caption and the introduction to frame the gradient benefit as a motivating hypothesis rather than an established result, unless direct gradient measurements are added.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| DeNN (pIJR9uPjy3) | 4.50 | R1 | Delay-based but different paradigm; DelRec substantially stronger |
| PMSN (FlH6VB5sJN) | 5.20 | R1 | Multi-compartment SNN on same benchmarks; DelRec achieves better results with simpler neurons |
| SNN-ANN conversion (GTzP2GC7NR) | 5.75 | R2 | Technical SNN contribution with limited novelty; DelRec has a more distinctive contribution |
| TS-LIF (rDe9yQQYKt) | 6.00 | R2 | Novel neuron model for forecasting; accepted. DelRec has more comprehensive benchmarks and a cleaner technical contribution |
| Temporal Flexibility (9HsfTgflT7) | 6.20 | R1/R2 | Novel SNN training method; accepted. Comparable quality but DelRec's empirical results are more compelling |
| DeepTAGE (drPDukdY3t) | 6.25 | R1/R2 | Gradient enhancement for SNNs; accepted. DelRec's contribution is more self-contained and impactful |
| Saccadic ViT (qzZsz6MuEq) | 6.60 | R1/R2 | SNN+ViT with novel attention; accepted. Stronger paper with more comprehensive experiments across modalities |

**Round 1 bracket**: The paper sits clearly above the 3.0–5.2 rejected range and below the 8.0+ range of unrelated high-scoring papers. Initial bracket: 5.0–7.0.

**Round 2 narrowing**: Comparison with TS-LIF (6.00), Temporal Flexibility (6.20), DeepTAGE (6.25), and Saccadic ViT (6.60) places DelRec in the 6.0–6.5 range. The paper is at least as strong as TS-LIF (which also introduces a novel mechanism with solid empirical validation but has limited benchmarks) and comparable to DeepTAGE. The SOTA overclaim and single-seed PS-MNIST result prevent it from reaching the Saccadic ViT tier.

**Final score**: 6.0. The method is novel, well-engineered, and supported by strong empirical evidence. The main weaknesses are presentational (unqualified SOTA claim) and easily fixable (multi-seed PS-MNIST). The paper represents a genuine contribution to the SNN literature and deserves acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>