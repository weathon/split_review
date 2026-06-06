Now I have read the full paper. Let me write the consolidated meta-review.

---

## Summary

WARP (Weight-space Adaptive Recurrent Prediction) introduces a linear RNN whose hidden state is the flattened weight vector of an auxiliary "root" MLP, updated via a linear recurrence driven by input *differences* (Δx) rather than raw inputs. This formulation enables gradient-free test-time adaptation, in-context learning, and seamless embedding of physics priors into the root network (WARP-Phys). The paper evaluates on image completion, time series forecasting, dynamical system reconstruction, multivariate classification, and a synthetic ICL task.

---

## Strengths

- **Novel architectural formulation.** The use of a network's flattened weight vector as the hidden state of a linear RNN is a genuinely original design (Fig. 1, Eq. 1). The self-decoding property — where θ_t serves simultaneously as hidden state and decoder parameters — meaningfully reduces learnable parameter count and is distinct from prior SSMs and linear RNNs.

- **Physics-informed (grey-box) variant yields dramatic gains on DSR.** WARP-Phys, which embeds the explicit mathematical form of the physical system into the root network (e.g., τ↦sin(2πτ+φ̂) for SINE), achieves MSE of 0.0003 vs. WARP's 0.0277 on SINE* and MSE of 0.0003 vs. 0.0094 for WARP on MSD (Table 3), representing more than a 10× improvement. This directly validates the paper's key claim that the weight-space formulation uniquely permits domain-specific priors to be embedded into the recurrence.

- **Competitive classification on UEA benchmarks.** Table 4 shows WARP achieves new best accuracies on Ethanol (36.49%) and Heartbeat (80.65%) against 10 strong baselines including Mamba, S5, LinOSS, Griffin, and FACTS, and places in the top three on four of six tasks. These are honest results — the absolute gaps on EigenWorms (70.93% vs. LinOSS 95%) and Motor (56.14% vs. 60.0%) are reported transparently.

- **Demonstrated gradient-free in-context learning.** Section 3.4 and Fig. 5 show that WARP can learn a linear key→value mapping from context without test-time gradient updates, and the final θ_{T-1} can be extracted to answer new queries without re-scanning the sequence. This is a concrete, measurable instantiation of the claimed adaptation property.

- **Competitive image completion on MNIST.** Table 1 shows WARP achieves best MSE at all context lengths and best/second-best BPD on MNIST against GRU, LSTM, ConvCNP, and S4 at matched parameter count (~1.7M), with qualitatively sharper digit completions in Fig. 3(a).

---

## Weaknesses

### Fatal

None that are definitively verifiable from the paper alone, but see the Major section for an issue that approaches fatal severity.

### Major

- **PEMS08 non-causal preprocessing constitutes a potential evaluation validity problem.** The paper states explicitly: "we preprocess the input sequence with a *non-causal* convolution, as detailed in Appendix D" and acknowledges this "significantly differs from the setting in Fig. 2." A non-causal convolution applied to a sequence can look at future time steps relative to each position. For a 12-step-ahead prediction from a 12-step context, if the non-causal convolution spans the context/forecast boundary, the preprocessed input would contain information from the target horizon — constituting target leakage. The paper provides no analysis of what the convolution kernel spans, no ablation without non-causal preprocessing, and no explanation for why the results are valid under this setup. The reported 50%+ improvement over SOTA (MAE: 6.59 vs. 13.45; RMSE: 10.10 vs. 23.28, Table 2) is extraordinary and far exceeds the scale of improvements typically seen on well-studied traffic benchmarks. As written, the PEMS08 result cannot be accepted as a valid forecasting comparison, and this is the paper's most prominent quantitative claim in the traffic domain. The authors must either demonstrate the non-causal convolution does not access future data, or replace this result with a fully causal evaluation.

- **ETT comparison limited to GRU and LSTM.** Section 3.1 compares WARP on ETT only against GRU and LSTM. The ETT benchmark has an extensive established ecosystem (DLinear, PatchTST, iTransformer, TimesNet, etc.) that is included in every credible recent ETT paper. The claim that WARP achieves "best performance on all subsets except ETT1" (Fig. 3b) has no informational content about the state of the art — it only establishes superiority over two legacy baselines. The ETT contribution cannot be evaluated without these standard comparisons.

- **Anomalous negative BPD on CelebA without explanation or S4 baseline.** Table 1 reports WARP achieving BPD of −0.043 (L=300) and −0.162 (L=600) on CelebA, while GRU achieves 24.14–71.51 and LSTM achieves 3.9–7.9. Negative BPD is mathematically possible for a Gaussian model with very small predicted variances, but the gap of ~70 BPD units versus GRU is implausibly large and most likely indicates σ̂ collapsing toward σ_min regardless of uncertainty, producing a favorable NLL without meaningful calibration. Furthermore, S4 — which appears in the MNIST portion of Table 1 — is absent from the CelebA portion without explanation, removing the SSM reference point. No qualitative CelebA comparison is provided. The paper provides no analysis of predicted variances on CelebA, making this result uninterpretable as-is.

### Minor

- **D_θ (weight-space dimension) not reported in the main text for any experiment.** Section 4.2 acknowledges that "the size of the matrix A limits scaling" and that "moderate D_θ values" were used on a 16GB GPU. But D_θ determines the hidden-state capacity of WARP and is the key architectural hyperparameter for evaluating whether comparisons are fair with respect to model capacity. This value should appear in every results table or a dedicated model-size table.

- **"X" entries for WARP-Phys on LV unexplained in main text.** Table 3 shows WARP-Phys as "X" for both LV columns with no explanation in the main text. The LV "Repeat-Copy" section notes the protocol is "incompatible with WARP-Phys due to the deliberate introduction of artificial discontinuities," but the DSR Table 3 is for *reconstruction*, not repeat-copy. Why physics injection is not attempted for Lotka-Volterra reconstruction is not explained.

- **ICL demonstration limited to synthetic linear regression.** Section 3.4 demonstrates ICL only on the synthetic linear key-value mapping of Garg et al. The claim of "significant computational savings compared to other models capable of ICL" is not supported by any runtime comparison against Transformers or linear-attention models on the same task.

### Trivial

- The conclusion's use of "infinite-dimensional RNN hidden states" (Section 4.3) is hyperbolic; the paper itself acknowledges in Section 4.2 that practical D_θ is constrained by the quadratic cost of A. The scare quotes in the original suggest this is intentional rhetorical framing, but it is still misleading.

---

## Nice-to-Haves

- A fair causal PEMS08 evaluation (or a separate traffic benchmark using fully causal preprocessing) and standard ETT baselines (at minimum DLinear) would substantially strengthen the forecasting section.
- For WARP-Phys on dynamical systems, ablation on *partial* physics knowledge (what if only the functional form but not the parameters are known?) would clarify how robust the physics injection advantage is.
- For the ICL demonstration, wall-clock and memory comparisons against a Transformer and linear-attention model on the same task would substantiate the "sub-quadratic computational savings" claim.
- Analysis of what datasets/modalities the input-difference recurrence particularly helps (do tasks where the discriminative signal lies in temporal derivatives benefit more?) would deepen understanding of the inductive bias.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "WARP-Phys comparison is unfair."** The harsh critic argues that WARP-Phys receives the exact generative form of the physical system, making the comparison unfair to baselines that don't. *Removed* because the paper explicitly and consistently frames WARP-Phys as a "grey-box" variant — the whole point of the physics-informed contribution is to demonstrate that the weight-space formulation naturally accommodates injecting physical structure. This is a stated design advantage, not a hidden confound. Comparing grey-box to black-box models under the label "physics-informed modelling" is legitimate.

- **Harsh Critic: "theoretical results deferred to appendix."** *Removed* under the hard rule against criticizing absent appendix content, which is stripped from this format.

- **Harsh Critic / general: "'infinite-dimensional' is hyperbole"** — retained as Trivial only; removed from Major because the scare quotes signal the authors' own awareness.

- **Harsh Critic: Neural ODE / Latent ODE baselines absent from DSR.** *Removed* as it amounts to requesting additional baselines. The paper uses two established RNNs and a Transformer, which covers the relevant comparison classes for the paper's scope.

- **Strength Finder: "Strong generative performance in image completion" based on CelebA BPD = −0.162.** *Removed* because the CelebA BPD result has a verified anomaly (negative and 70-unit gap vs. GRU, missing S4 comparison). This claimed strength directly conflicts with a verified weakness and is removed per the filtering rules.

---

## Novel Insights

The most genuinely novel observation from combining both reviews is that WARP's architecture creates a natural two-tier update structure — slow parameters (A, B, φ) updated by gradient descent once per batch, and fast parameters (θ_t) updated by recurrence T−1 times without gradients. This resonates with fast-weight / test-time training literature but with a key distinction: the fast weights are structured as a neural network, enabling non-linear decoding from a linearly evolved state. This is the architectural core that makes physics embedding natural and that the empirical results on DSR validate most cleanly. The paper's contribution is strongest precisely where this distinction from prior linear RNNs is most exploited — WARP-Phys on structured dynamical systems — and weakest where the contribution becomes one RNN competing against other RNNs on standard benchmarks.

---

## Suggestions

1. Replace the PEMS08 experiment with a fully causal evaluation (no non-causal convolution), or provide a rigorous analysis showing the convolution kernel does not span the forecast horizon. Extraordinary claims require extraordinary evidence.
2. Add at minimum DLinear and one Transformer-based baseline (e.g., PatchTST) to the ETT comparison.
3. Report D_θ, parameter count, peak GPU memory, and training time for every experiment in a unified model-size table.
4. For CelebA, provide (a) an analysis of predicted σ values to diagnose variance collapse, (b) qualitative completions, and (c) the S4 baseline.
5. Clarify why WARP-Phys is not attempted on Lotka-Volterra reconstruction in the main text.

---

## Assessment on Key Axes

- **Originality:** High. The use of a network's weight vector as a linear RNN's hidden state is a new idea, and the training algorithms and physics-injection mechanism are concrete and original.
- **Importance of research question:** High. Unifying linear recurrence efficiency with expressive non-linear decoding and test-time adaptation is an important problem in sequence modeling.
- **Claims well supported:** Mixed. Classification claims are well supported; physics-informed claims are well supported; forecasting claims have serious methodological problems (PEMS08, ETT) that undermine confidence.
- **Soundness of experiments:** Weak on forecasting (non-causal leakage risk, limited baselines, anomalous BPD); solid on classification and DSR black-box; excellent on WARP-Phys.
- **Clarity of writing:** Generally clear; the PEMS08 non-causal preprocessing is mentioned but its implications are inadequately discussed.
- **Value to the research community:** Moderate-to-high for the architecture idea and physics-informed direction; the forecasting evaluation as presented adds limited value.

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>