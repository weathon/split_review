## Summary
WARP (Weight-space Adaptive Recurrent Prediction) introduces a linear RNN whose hidden state is the flattened weight vector of an auxiliary MLP ("root network"), updated via linear recurrence on input *differences* Δx_t = x_t − x_{t-1}, and decoded by evaluating the root MLP at a coordinate τ. This blends linear-recurrence efficiency with non-linear decoding, enabling gradient-free test-time adaptation, in-context learning, and injection of physical priors. The paper demonstrates WARP across image completion, time-series forecasting, dynamical system reconstruction, and multivariate classification benchmarks.

---

## Strengths

- **Genuinely novel architectural concept.** Treating the weights of an auxiliary function approximator as the intermediate hidden state of a recurrence (rather than merely as inputs/outputs) is a fresh contribution. The self-decoding property—where θ_t is simultaneously the hidden state and the decoder—is elegant and reduces parameter count.

- **Physics-informed extension is compelling.** WARP-Phys, which embeds domain-specific equations (e.g., sinusoidal structure, spring-mass-damper dynamics) directly in the root network, achieves more than an order-of-magnitude improvement over WARP on MSD and MSD-Zero (Table 3: 0.03 vs. 0.94 MSE), cleanly demonstrating the value of the modular grey-box design.

- **Broad empirical scope.** The paper covers image completion (MNIST, CelebA), long-range energy forecasting (ETT), traffic flow (PEMS08), dynamical system reconstruction (MSD, LV, SINE), and six UEA multivariate classification datasets. Coverage across modalities strengthens the generality claim.

- **Competitive classification performance.** Top-3 on 4/6 UEA datasets, SOTA on Ethanol and Heartbeat, with strong long-sequence results on EigenWorms (18k steps) despite no explicit long-range design—attributable to the well-motivated initialization and positional encoding scheme.

- **Principled use of input differences.** The choice Δx_t is theoretically grounded (Kidger et al. for NCDEs) and has an intuitive learning-from-change interpretation that connects to continual and synaptic-plasticity literature.

---

## Weaknesses

### Fatal
None.

### Major

1. **Extraordinary PEMS08 result lacks credibility without broader baselines.** Table 2 reports WARP at MAE 6.59 / RMSE 10.10 versus the next best (STDCN) at 13.45 / 23.28—a >50% reduction in MAE. A halving of error on a well-studied benchmark would be a landmark result in the spatial-temporal forecasting community. The three baselines cited all come from a single older reference [62], and prominent recent methods (STAEformer, STID, PDFormer, AGCRN, TimesNet, etc.) are absent. Additionally, WARP uses a non-causal pre-processing convolution on this task (mentioned briefly in Section 3.1) that is never applied to the baselines and could alone account for most of the gap. The result is therefore not trustworthy as presented and could mislead readers about WARP's capabilities.

2. **Quadratic cost in hidden dimension D_θ is a fundamental architectural limitation that is underanalyzed.** Matrix A ∈ R^{D_θ × D_θ} grows quadratically with root-network size, capping the root MLP at a few hundred parameters in practice (the paper acknowledges this but does not report the actual D_θ values used in any experiment, nor does it quantify its effect on model capacity relative to baselines with millions of parameters). Without this information, the reported parameter-count parity claim (e.g., ~1.68M for MNIST) may conceal that WARP's root network itself has negligible capacity, most parameters residing in A and B rather than in the expressive non-linear decoder.

3. **ETT comparisons omit modern SOTA baselines.** Figure 3(b) compares only against GRU and LSTM—models that perform poorly on ETT. No PatchTST, iTransformer, Mamba, DLinear, TimesNet, or other standard ETT baselines appear, making the "WARP surpasses SOTA on ETT" narrative unsubstantiated.

4. **In-context learning experiment (Section 3.4) has no baselines.** The ICL demonstration is visually pleasing but reports no comparison against standard ICL models (e.g., Transformers, Mamba, or neural processes on the same task). The claim of "sub-quadratic in-context learning" is stated but not benchmarked against any quadratic baseline to quantify the speedup.

### Minor

1. **Connection to fast-weight RNNs could be made more precise.** WARP is structurally similar to fast-weight RNNs (Ba et al. 2016) with a linear outer update rule—the main differences are: (a) input differences instead of raw inputs, (b) A initialized to identity, (c) the root network evaluated at a coordinate τ rather than directly at the input. The paper mentions fast weights but does not offer a formal comparison that would sharpen the contribution.

2. **Repeat-copy / pattern-retention claim is partially undermined by experimental scope.** The LV repeat-copy result (Fig. 4, Table 3) is interesting, but WARP's advantage over LSTM/GRU is modest on this task, and no standard repeat-copy benchmark (e.g., the original synthetic sequences from [89]) is included.

3. **The "brain-inspired" / STDP framing in Section 4.1 is superficial.** Δx_t as input differences has a loose analogy to spike-timing, but WARP's recurrence contains no spiking dynamics, rate codes, or biologically meaningful timescales. The paragraph adds limited scientific value.

### Trivial
- The CelebA BPD values in Table 1 include −0.162, which is impossible for a true BPD metric but likely a parsing artifact—not a scientific error.

---

## Nice-to-Haves

- Ablation comparing Δx_t input differences against raw x_t inputs on the forecasting benchmarks would directly validate one of the paper's key design claims.
- Experiments with a low-rank or diagonal parameterization of A (mentioned in the limitations) to understand how much expressivity is traded for scalability.
- At minimum one modern SOTA baseline (e.g., PatchTST or iTransformer) on ETT to contextualize the forecasting results.
- Clear reporting of D_θ (root network size) and A matrix size for every experiment.

---

## Novel Insights

The most genuinely novel insight is that a linear recurrence can operate effectively in the weight space of a secondary network, enabling the same high-dimensional parameter vector to serve simultaneously as a memory representation and a non-linear decoder without requiring a separate readout module. This "self-decoding" property is conceptually distinct from standard meta-learning, hypernetworks, and fast-weight models because the weights are never trained by gradient descent during inference—they are directly updated by a learned linear operator applied to signal differences. The physics-informed variant elegantly demonstrates that this modular design allows domain knowledge to be injected without altering the recurrence structure, a property not available in standard RNNs or SSMs where the hidden state has no semantic interpretation.

---

## Suggestions

- Report actual D_θ values and the fraction of total parameters that reside in A versus the root MLP in every experiment to allow the community to understand the true capacity constraints.
- Re-run PEMS08 comparisons against recent non-graph baselines (and at minimum verify the non-causal convolution preprocessing is either also applied to baselines or removed from WARP) before drawing state-of-the-art claims.
- Add at least PatchTST or iTransformer on ETT; these are standard and take minimal additional effort.
- Consider a dedicated ablation: WARP with A = I (frozen) to test whether learning A at quadratic cost is necessary.

---

## Score and Decision

The weight-space hidden state idea is novel and the physics-informed results are strong. However, the PEMS08 claim—one of the paper's most prominent empirical contributions—is inconsistent with the literature and the experimental setup introduces a confound (non-causal preprocessing) not applied to baselines. The ETT section lacks credible comparisons, and the scalability bottleneck is unquantified. These are resolvable concerns but collectively weigh against unconditional acceptance at this revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>