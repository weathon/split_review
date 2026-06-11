Now let me compile everything into the final review.

---

## Summary

WARP introduces a sequence model where the hidden state of a linear RNN is the flattened weights of an auxiliary "root" MLP: θ_t = Aθ_{t-1} + BΔx_t, with decoding y_t = MLP_{θ_t}(τ). The architecture cleanly separates a parallelizable linear recurrence from expressive nonlinear decoding, and the weight-space formulation enables embedding physical priors directly into the root network (WARP-Phys). Empirical results are mixed: the physics-informed variant shows dramatic improvements, PEMS08 traffic forecasting shows a large MAE reduction, and classification is competitive on several UEA benchmarks, but anomalous BPD values in image completion and inconsistent baseline choices weaken the evidence.

## Strengths

- **Novel weight-space recurrence architecture**: The core recurrence (Eq. 1) using MLP weights as the hidden state of a linear RNN is genuinely original. Prior weight-space learning work treats weights as inputs/outputs to higher-level models; using them as intermediate recurrent hidden states is a distinct contribution supported by the clean decomposition in Fig. 1 and Eq. (1). The self-decoding property (θ_t serves as both hidden state and decoder, line 78) is a genuinely parsimonious design.

- **WARP-Phys: concrete, unique advantage of the framework**: Table 3 shows the physics-informed variant reducing SINE MSE from 2.77×10⁻⁴ to 6.2×10⁻⁵ and MSD MSE from 0.94×10⁻² to 0.03×10⁻². Embedding an explicit formulation like τ ↦ sin(2πτ + φ̂) directly into the root network's forward pass is a capability uniquely enabled by the weight-space formulation that conventional RNNs and SSMs cannot replicate. This is the paper's single most compelling result.

- **Competitive classification on several UEA benchmarks**: Table 4 shows WARP setting new SOTA on Ethanol (36.49%) and Heartbeat (80.65%), and ranking top-3 on 4 of 6 datasets against 10 baselines including Mamba, S5, Griffin, and LinOSS on sequences ranging from 405 to ~18k tokens.

- **Input-difference recurrence with theoretical motivation**: Using Δx_t = x_t − x_{t-1} rather than raw inputs (Section 2.2) is well-justified by citing Kidger et al.'s continuous-time RNN theory and creates a natural dampening mechanism when inputs change slowly.

## Weaknesses

### Fatal

None.

### Major

- **Overclaimed "gradient-free adaptation" framing**: The paper repeatedly characterizes the forward pass as "gradient-free test-time adaptation" (abstract, lines 9, 36, 108, 283). The distinction between slow parameters (A, B, φ, learned via gradient descent) and fast weights (θ_t, updated via Eq. (1)) is a real architectural feature rooted in the fast-weights literature. However, the term "test-time adaptation" is misleading — every RNN updates its hidden state at inference without gradients. WARP's hidden state happens to be interpretable as MLP weights, but the underlying mechanism is the standard forward pass of a recurrent model. This inflated framing pervades the abstract and conclusion, giving readers an exaggerated picture of the model's capabilities and diluting the paper's genuine contributions.

- **Unexplained anomalous BPD values in CelebA (Table 1, lines 135-141)**: LSTM achieves BPD of 3869 on L=100 but 7.276 on L=300 — a three-order-of-magnitude swing within the same model. WARP achieves *negative* BPD (−0.043, −0.162), which for a Gaussian likelihood on pixel data is physically impossible without pathological overconfidence (σ → 0). GRU BPD is also unstable (24.14 / 60.39 / 71.51). These values strongly suggest training instability, a BPD computation error, or numerical issues. The paper reports these numbers without comment, undermining the credibility of the image completion evaluation.

- **Inconsistent and weak baseline sets across experiments**: The ETT experiment (Fig. 3b) compares WARP only against GRU and LSTM — no S4, Transformer, or other SSM despite these being standard on this benchmark. The dynamical systems experiment (Table 3) omits S4/SSMs entirely. The PEMS08 results (Table 2) compare against published numbers from prior work, but WARP additionally uses non-causal convolution preprocessing (line 180) not used by those baselines in their original form. The ICL experiment (Section 3.4) has no standard ICL baseline. The pattern of shifting baseline sets makes it difficult to assess WARP's standing against any consistent competitor.

### Minor

- **Scalability limitation acknowledged but unquantified**: The A matrix is D_θ × D_θ, quadratic in root network size. Section 4.2 acknowledges this, but D_θ values are never reported for any experiment. With ~1.7M total parameters for MNIST (line 149), D_θ must be small (likely a few hundred), limiting the claimed "high-dimensional" expressiveness advantage.

- **Weak EigenWorms result glossed over**: WARP achieves 70.93% on EigenWorms (Table 4), ranking 9th of 11 methods — LinOSS achieves 95.0%. The paper's claim that WARP "outperform[s] established models such as Mamba and NCDE" on EigenWorms (line 243) is technically true (70.93 vs. 70.9 and 62.2) but cherry-picks the two models it barely beats while ignoring eight stronger baselines.

- **WARP-Phys applicability is narrow**: WARP-Phys cannot be applied to Lotka-Volterra (marked "X" in Table 3) or the repeat-copy variant (line 237), showing it requires known functional forms and clean, continuous data. The paper presents this as a feature without adequately acknowledging the limited scope.

### Trivial

- The abstract and conclusion use hyperbolic language ("redefine sequence modeling," "transformative paradigm," "human-level artificial intelligence") disproportionate to the empirical evidence.

## Nice-to-Haves

- An ablation isolating the weight-space formulation from co-varying factors (difference-based recurrence, coordinate-based decoding) — e.g., comparing against a standard linear RNN with the same nonlinear MLP decoder — would clarify which architectural choices drive the performance.
- Report root network sizes (D_θ, depth, width) for each experiment to let readers assess the scalability picture.
- Investigate and explain the anomalous CelebA BPD values.
- Run at least one consistent strong baseline (e.g., S4 or Mamba) across all experiments.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The ICL claim about extracting θ_T to process queries is just the observation that an RNN's final state summarizes the sequence"* — REMOVED. Overly reductive. The fact that the final hidden state IS a functional MLP that can be extracted and applied to new queries is a genuine, distinctive property not shared by standard RNNs whose hidden states are opaque vectors requiring a separate decoder.

- *"The neuromorphic analogy to STDP is superficial and bolted on"* — REMOVED. Subjective style judgment; the paper mentions it briefly in discussion (Section 4.1) without making it a central claim.

- *"No Transformer baseline for image completion"* — REMOVED. S4 is a strong and appropriate baseline for this pixel-by-pixel sequential task; Transformers are not standard here.

- *"Dynamical systems should compare against physics-informed baselines like Neural ODEs/PINNs"* — DEMOTED to Nice-to-Have. The existing comparison against black-box models already demonstrates the value of physics priors.

- *"Missing appendix content / proofs / architecture details"* — REMOVED per hard rule. The parser strips appendix; these exist in the original submission.

- *"The paper should report variance across runs for ETT and image completion"* — REMOVED as a generic one-size-fits-all criticism.

- *"The scalability bottleneck is fatal / makes the paper impractical"* — WEAKENED. The paper acknowledges this in Section 4.2 and discusses future directions (diagonal/low-rank parametrizations, line 279). It is a real limitation but not fatal to the current contribution.

## Novel Insights

The most thought-provoking idea in this paper is the conceptual unification of three distinct literatures: weight-space learning (where neural network weights are data points), fast-weights / meta-learning (where rapid weight updates enable adaptation), and linear recurrence (where the transition is parallelizable). The observation that a linear RNN's hidden state can literally be the parameters of a decoder network is simple in hindsight but has not been proposed before. This opens an interesting design space: the "hidden state" can be any structured object with its own computational semantics, not just a vector. The WARP-Phys results concretely demonstrate one unique payoff of this formulation.

## Suggestions

- Reframe the contribution around "weight-space hidden states as a representational choice" rather than "gradient-free adaptation." The architecture is genuinely novel without the oversell.
- Either fix and explain the CelebA BPD anomalies or remove those results. Negative BPD for a probabilistic model on pixel data is a red flag that will distract every careful reader.
- Add at least one consistent strong baseline (S4 or Mamba) to the ETT and dynamical systems experiments to establish WARP's standing against a fixed competitor.
- Report D_θ values for every experiment so readers can assess the scalability-expressiveness tradeoff directly.

## Score and Decision

### Calibration Anchor Comparison

**Round 1 — Bracketing:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| FSFC RNN for Text Classification | 2.33 | WARP is substantially stronger — genuine architectural novelty vs. incremental RNN variant |
| Cross Attention for Oddly Shaped Data | 2.00 | WARP has much broader evaluation |
| DIRAD (Structural Adaptation) | 2.33 | WARP has more coherent contribution and better empirical backing |
| Ricci Flows / Continuous-depth | 2.33 | WARP is more application-grounded |
| Episodic Memory Theory for RNNs | 4.25 | Comparable quality; EMT has theory focus, WARP has broader empirical scope |
| S7: Selective SSM Layers | 3.50 | WARP is more novel and has stronger results |
| Weight Space Representation Learning | 4.25 | Most topically related; comparable novelty but WARP's evaluation has credibility issues |
| Solution Degeneracy in RNNs | 4.20 | Similar quality tier; both have real but limited contributions |
| Sequence Attractors in RNNs | 5.25 | WARP is slightly below — Attractors paper has cleaner theory-experiment alignment |
| Gradient-Free Training of RNNs | 6.00 | WARP is clearly below — that paper has cleaner framing and evaluation |
| Gated RNNs Discover Attention | 5.50 | WARP is below — that paper has stronger mechanistic insights |
| HadamRNN | 6.00 | WARP is below — HadamRNN has tighter evaluation and clearer contribution |
| CausalRNs | 6.33 | WARP is below — CausalRNs has cleaner claims |
| Inverse Approximation Theory | 7.25 | WARP is substantially below |
| Memory Mosaics | 6.25 | WARP is below |
| LinOSS | 8.00 | WARP is substantially below |
| ModernTCN | 8.00 | WARP is substantially below |

**Round 1 Bracket:** 3.5–5.5 (WARP is clearly above strong reject papers at ~2.3 and clearly below strong accept papers at ~7.5–8.0; it sits above S7 at 3.50 and near or below the 4.25–5.5 cluster.)

**Round 2 — Narrowing:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| RotRNN | 4.00 | Most comparable: novel linear RNN architecture with competitive but not SOTA performance. WARP has more original idea but more evaluation credibility issues. Similar overall. |
| S7 | 3.50 | WARP is clearly more novel and has stronger results. |
| Mimetic Initialization | 4.50 | WARP has broader empirical scope but Mimetic Init has cleaner evaluation. WARP slightly below. |
| Weight Space Rep. Learning | 4.25 | Topically closest. WARP has more diverse experiments but the WSL paper has cleaner framing. Comparable. |
| GIFT-Eval (benchmark) | 5.25 | WARP is below — GIFT-Eval is a well-executed benchmark contribution. |
| Frequency Collapse in TS | 4.33 | WARP is comparable; both address specific technical problems. |

**Final Score Determination:** WARP sits most naturally near RotRNN (4.00) and the Weight Space Representation Learning paper (4.25). The architectural idea is more novel than RotRNN's, but the evaluation quality issues (anomalous BPD, inconsistent baselines, overclaimed framing) pull it down. The paper is a clear step above S7 (3.50) but does not reach the rigor of Mimetic Initialization (4.50) or the papers in the 5.0+ range. **Score: 4.0.**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>