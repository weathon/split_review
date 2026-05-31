Now let me run the calibration search to anchor the score.Round 1 bracket: initial estimate is **between 4 and 6**, based on the novel architecture idea but significant evaluation flaws. Let me do Round 2 narrowing.Now I have sufficient calibration. Let me write the final consolidated review.

---

## Summary

WARP (Weight-space Adaptive Recurrent Prediction) proposes a novel linear RNN variant that parametrizes its hidden state as the flattened weight vector of an auxiliary MLP ("root network"), with state transitions driven by *input differences* rather than direct inputs. The root network's weights evolve via a linear recurrence, while decoding is performed non-linearly by applying the reconstituted MLP to a task-appropriate coordinate system. The paper evaluates on image completion, time-series forecasting (ETT, PEMS08), dynamical system reconstruction, UEA multivariate classification, and a gradient-free in-context learning demonstration, and also introduces a physics-informed grey-box variant (WARP-Phys) that injects domain-specific priors into the root network.

---

## Strengths

- **Genuinely novel architecture.** Treating the MLP weight vector as a linearly-updated RNN hidden state is a distinctive contribution that unifies weight-space learning with linear recurrence. The formulation in Eq. (1) is clean, and the use of *input differences* Δxₜ has theoretical motivation from Neural CDEs. To our knowledge this is the first work to use weight-space features as *intermediate* recurrent hidden states in an end-to-end training system.

- **Physics-informed variant achieves order-of-magnitude improvements on DSR.** Table 3 shows WARP-Phys reduces MSE on MSD by >10× relative to WARP (0.03 vs 0.94), and >30× relative to the best baseline (Transformer: 0.34). This concretely demonstrates the architectural flexibility of the weight-space formulation — domain equations (e.g., τ ↦ sin(2πτ + φ̂)) can be embedded directly in the root network with no structural changes to the outer recurrence.

- **Competitive classification results on UEA benchmarks.** Table 4 presents a well-constructed comparison including contemporary baselines (Mamba, LinOSS, FACTS, Griffin, LRU, S5, Log-NCDE). WARP achieves new SOTA on Ethanol (36.49 ± 2.8%) and Heartbeat (80.65 ± 1.9%), and ranks top-3 on SCP2 and Motor. The evaluation protocol is sound (5 runs, 70:15:15 split, averaged accuracy).

- **Demonstrated gradient-free in-context learning.** Section 3.4 provides a concrete ICL demonstration: WARP learns linear key-value mappings from context without test-time gradient steps, and the final root network can answer new queries directly (Fig. 5). This is a meaningful, measurable instance of the claimed gradient-free adaptation property.

---

## Weaknesses

### Fatal
None.

### Major

- **PEMS08 evaluation is structurally invalid due to non-causal preprocessing.** The paper (Section 3.1, Table 2) reports MAE 6.59 / RMSE 10.10 on PEMS08, a >50% reduction over prior SOTA (13.45 / 23.28). However, the paper explicitly states: "we preprocess the input sequence with a *non-causal* convolution, as detailed in Appendix D." A non-causal convolution in a 12-step-ahead forecasting task can encode future time steps into the preprocessed input, constituting temporal leakage. The paper acknowledges that this "significantly differs from the setting in Fig. 2" but frames this as a *design choice* without analyzing what information the non-causal filter passes to the model. Comparing a non-causally preprocessed WARP against strictly causal GNN/Transformer baselines (GMAN, D²STGNN, STDCN) is not a valid comparison. The extraordinary numeric gap is most parsimoniously explained by leakage rather than architectural quality, and this result should not be taken as evidence for WARP's forecasting capability.

- **ETT forecasting comparison against only GRU and LSTM.** Figure 3(b) and Section 3.1 present ETT results as evidence of WARP's forecasting strength, but the comparison pool contains only GRU and LSTM — the two simplest baselines. The ETT benchmark has a well-established set of strong comparators (DLinear, PatchTST, iTransformer, Autoformer, etc.) that form the standard comparison baseline in virtually every ETT paper. The claim "best performance on all subsets except ETT1" is informative only relative to GRU/LSTM and carries no content relative to the state of the art. This omission makes the ETT forecasting claim uninterpretable as a contribution.

- **Anomalous negative BPD values on CelebA require explanation.** Table 1 reports BPD values for WARP of −0.043 and −0.162 on CelebA (L=300 and L=600), while GRU achieves 60.39 and 71.51 respectively — a gap of ~70 BPD units. Negative BPD is mathematically possible under a Gaussian model when predicted variance collapses, but the magnitude of separation from all other baselines is far outside expected ranges and strongly suggests metric miscalibration rather than genuine generative quality. The paper provides no explanation. Furthermore, S4 is absent from the CelebA portion of Table 1 without explanation, removing the one SSM comparator that would most naturally contextualize the result.

### Minor

- **Weight-space dimension D_θ is never reported.** Section 4.2 acknowledges that "the size of the matrix A limits scaling to huge root neural networks" and that experiments used "moderate D_θ values," yet D_θ is not reported in any table or figure in the main text. The A matrix scales as D_θ², so the actual hidden-state dimensionality is crucial for assessing whether WARP's capacity is comparable to its baselines. Without this, fair comparison is impossible to assess.

- **WARP-Phys "X" entries on Lotka-Volterra are unexplained.** Table 3 shows "X" for WARP-Phys on the LV system without explanation in the caption or surrounding text. The text mentions incompatibility with the repeat-copy protocol, but this only applies to the LV *repeat-copy* task. Why physics injection is unavailable for standard LV reconstruction is not stated.

- **In-context learning demonstration lacks quantitative comparison to baseline models.** Section 3.4 claims "sub-quadratic in-context learning" and "significant computational savings compared to other models capable of ICL," but neither claim is substantiated with runtime or memory measurements against a Transformer. The demonstration is qualitative (scatter plots in Fig. 5), not comparative.

### Trivial

- The "infinite-dimensional" characterization in the conclusion (Section 4.3) is hyperbole. The paper does use quotation marks ("infinite-dimensional"), and D_θ is explicitly acknowledged as finite and memory-limited. This framing should be softened to avoid overstating the contribution.

---

## Nice-to-Haves

- **Deeper analysis on why WARP wins specific classification tasks.** The gap between WARP (70.93%) and LinOSS (95.0%) on EigenWorms versus WARP's win on Ethanol/Heartbeat suggests the input-difference recurrence has task-specific inductive biases. An analysis of what discriminative information lives in temporal derivatives for the winning tasks would make the classification contribution significantly more insightful.

- **WARP-Phys extended to more physical systems.** The physics-informed grey-box result is the strongest demonstration of the architecture's unique capabilities. Extending to additional systems, ablations on partial physics knowledge, and comparison to physics-informed Neural ODEs would make this the paper's centerpiece contribution rather than a secondary result.

- **Quantitative wall-clock and memory comparison to Transformers on the ICL task** would directly substantiate the "sub-quadratic computational savings" claim.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **WARP-Phys fairness concern.** The harsh critic argues that WARP-Phys has an unfair advantage because it embeds the ground-truth generative form. However, the paper clearly labels this as a *grey-box* setting and explicitly contrasts it with the *black-box* setting. Comparing a deliberately physics-informed model to generic baselines is the entire point of the grey-box demonstration, not a fairness violation. **REMOVED** as a strawman.

- **"Top three" abstract framing.** The harsh critic flags that the abstract says "top three in 4 out of 6 datasets" without noting that LinOSS beats WARP by 24 points on EigenWorms. This is accurate as stated — "top three" is not a false claim — and the absolute gaps are visible in Table 4. **REMOVED** as a nitpick.

- **Theoretical expressivity claim about non-linear decoding.** The harsh critic argues that the paper does not formally establish that non-linear decoding from a linearly-evolved weight state is strictly more expressive than a linear RNN + MLP decoder. The paper cites this as motivation and the formal results are in Appendix B.2. Per the hard rule removing missing-appendix criticisms, this is **REMOVED**.

- **Absence of Neural ODEs in DSR baselines.** The harsh critic asks for Neural ODEs as baselines for dynamical system reconstruction. This is a valid suggestion but falls under "missing related works / missing baselines" and per soft rule discipline, this is a nice-to-have, not a fatal or major weakness. **DEMOTED TO NICE-TO-HAVE.**

---

## Novel Insights

The weight-space hidden state formulation creates an unusually clean interface for physics injection: because the hidden state *is* the weight vector of the root network, swapping a black-box MLP root for a physics-structured function (e.g., a damped oscillator response or a sine with learned phase) requires no architectural surgery beyond replacing the root's forward pass. This is more modular than conventional physics-informed neural networks, which typically require adding physics loss terms or constraining layers. The paper under-exploits this insight — the WARP-Phys results in Table 3 are the clearest demonstration of what is unique about the architecture, but the paper presents them as a supporting experiment rather than its headline contribution.

---

## Suggestions

1. **Redo PEMS08 with a strictly causal preprocessing pipeline** (or causal convolution), and explicitly compare like-for-like against the GNN baselines. If WARP still improves on SOTA under causal conditions, it is a strong result; if not, the non-causal preprocessing should be re-framed as a separate task setting rather than a benchmark comparison.
2. **Add at minimum DLinear as an ETT baseline** (it is a simple linear model that is frequently competitive and widely reproduced), and ideally PatchTST or iTransformer to place the ETT results in context.
3. **Report D_θ** (weight-space dimension used in each experiment) in every table or in a model-size table alongside parameter counts, to allow fair capacity comparison.
4. **Explain or correct the CelebA BPD anomaly**: either show qualitative samples at the anomalous settings, report calibration metrics (e.g., spread of predicted σ), or include an ablation on σ_min to demonstrate that the near-zero BPD is not a variance-collapse artifact.
5. **Include WARP-Phys for LV** with explanation of why physics injection is or is not feasible, or state it explicitly as a limitation in Table 3.

---

## Score and Decision

### Anchor Summary

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| I1484gDBr4 (Linear RNN feature-sequence) | 2.50 | R1 low | Weaker than WARP — minimal novelty, rejected |
| 7eYmijcuqO (RNN temporal dynamics) | 3.00 | R1 low | Narrower scope than WARP |
| z6qmomJW91 (RotRNN) | 4.00 | R2 | Close anchor: solid linear RNN, good theory, no performance gains. WARP is more novel with genuine wins in classification and DSR, but has worse evaluation integrity. |
| hgjpO0H0id (Deep SSMs theory) | 4.00 | R1 mid | Theoretical focus, WARP is more empirically ambitious |
| HEcbGXzIHK (Episodic memory RNNs) | 4.25 | R1 mid | Different focus, moderate anchor |
| 9EBSEkFSje (GIFT-Eval benchmark) | 5.25 | R2 | Benchmark paper without novel architecture |
| XoYdD3m0mv (ProbeGen weight-space) | 6.00 | R2 | Clean weight-space contribution with valid evaluations. WARP is more novel architecturally but has more evaluation problems |
| GRMfXcAAFh (LinOSS) | 8.00 | R1 high | Strong anchor: theoretical universality + SOTA results, clearly stronger than WARP |
| qKf0tZtF6B (Dynamical systems GP) | 5.80 | R2 | Physics-informed modeling, solid but narrower |

**Round 1 bracket:** 4–6

**Round 2 narrowing:** WARP's architectural novelty and classification/DSR contributions are genuine and exceed RotRNN (4.0). However, the paper's forecasting section — which occupies a substantial portion of the experimental contribution — contains three major validity issues (non-causal PEMS08, minimal ETT baselines, anomalous CelebA BPD), all unaddressed by the authors. ProbeGen (6.0) has clean, valid evaluations with a narrower but well-executed contribution. WARP falls *below* ProbeGen on evaluation integrity despite having more ambitious ideas. The paper lands just above RotRNN given real classification wins and the novel physics-informed capability, but the evaluation problems prevent acceptance.

**Final score: 5.0 (Reject)**

The paper introduces a genuinely interesting idea (weight-space hidden states for linear RNNs) and has credible results in classification and physics-informed dynamical system reconstruction. However, its most prominent quantitative claims — the PEMS08 result and ETT superiority — are not credibly established due to non-causal preprocessing and severely limited baselines, respectively. The CelebA BPD anomaly is unexplained. These are not gaps addressed by adding experiments to an appendix; the PEMS08 comparison requires a valid causal setup, and the ETT section needs standard comparators. As submitted, the forecasting contribution cannot be accepted as valid, and this undercuts a major portion of the paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>