Now I have sufficient calibration data. Let me finalize the review.

**Round 1 Bracket:** 5.5–7.0 (novel idea + broad evaluation, but PEMS08 fairness issue and overclaiming)
**Round 2 Narrowing:** 5.5–6.5 (comparable to TS-LIF at 6.0, NFM at 6.2, TimeCapsule at 5.5)

**Comparison with anchors:**
- WARP vs. TS-LIF (6.0, Accept): Both have biological inspiration themes, novel architectural ideas, and solid but imperfect empirical evaluation. WARP has broader evaluation scope (5+ tasks) and more striking results (WARP-Phys 10x improvement), but has a more serious fairness concern (PEMS08 non-causal preprocessing). Comparable overall.
- WARP vs. NFM (6.2, Reject): Both are novel time-series architectures with broad task coverage. NFM is more compact; WARP has stronger individual results. NFM's weaknesses (limited classification datasets, missing baselines) mirror WARP's weaknesses but WARP's PEMS08 issue is more severe.
- WARP vs. TimeCapsule (5.5, Reject): WARP is more novel and more broadly evaluated.
- WARP vs. "Gated RNNs discover attention" (5.5, Reject): WARP has far more extensive empirical evaluation and more dramatic results.

WARP sits above the 5.5 anchors (more novel, better evaluated) but below the 6.2 anchor due to the PEMS08 fairness issue.

## Summary
WARP introduces a novel sequence model where the hidden state of a linear RNN consists of the flattened weights of an auxiliary MLP, updated via θ_t = Aθ_{t-1} + BΔx_t and decoded non-linearly as y_t = MLP_{θ_t}(τ). The paper evaluates across image completion, time series forecasting, dynamical system reconstruction, classification (6 UEA datasets), and in-context learning, claiming SOTA or near-SOTA performance. A physics-informed variant (WARP-Phys) achieves order-of-magnitude improvements on dynamical system reconstruction.

## Strengths
- **Genuinely novel architectural framework**: The core idea of using MLP weights as hidden states in a linear recurrence, with self-decoding (θ_t plays both hidden state and decoder), is a creative synthesis of weight-space learning and linear recurrence. The identity initialization of A (emulating gradient descent) and zero initialization of B are well-motivated (Section 2.2, line 86). This is distinct from hypernetworks and fast-weight literature.
- **Physics-informed variant achieves order-of-magnitude improvement**: Table 3 shows WARP-Phys achieves MSE 0.03±0.04 on MSD vs. 0.34±0.12 for Transformer (>10× improvement). This is a capability unique to the weight-space formulation — embedding domain knowledge into the root network's forward pass (e.g., τ ↦ sin(2πτ + φ̂)) is architecturally impossible in standard RNNs.
- **Strong UEA classification with comprehensive baselines**: Table 4 compares against 10+ baselines (Mamba, S5, LinOSS, FACTS, NCDE variants, Griffin) on 6 datasets spanning sequence lengths 405–18K. WARP achieves SOTA on Ethanol and Heartbeat, and top-3 on 4/6 datasets. This is the paper's most convincing empirical contribution with fair comparison design.
- **Superior image completion at matched parameter counts**: Table 1 shows WARP achieves best or tied-best MSE across all context lengths on MNIST and CelebA, with all models using ~1.68M parameters (MNIST). Figure 3(a) qualitatively shows WARP produces cleaner digit reconstructions than GRU, LSTM, and S4 at small parameter count.
- **Demonstrated gradient-free test-time adaptation and in-context learning**: Section 3.4 shows WARP can learn linear key-value mappings in-context, and the extracted θ_{T-1} can process subsequent queries without re-evaluating the full sequence (line 261), providing concrete computational advantages over Transformer-based ICL.

## Weaknesses

### Fatal
None

### Major
- **PEMS08 traffic forecasting uses non-causal preprocessing, rendering the headline comparison unfair**: The paper states "we preprocess the input sequence with a *non-causal* convolution" (line 180) for PEMS08. The baselines (GMAN, D²STGNN, STDCN) are causal spatial-temporal models. By accessing future information unavailable to baselines, the claimed 50%+ MAE reduction (Table 2: 6.59 vs. 13.45) cannot be attributed to model architecture alone. This is the paper's single most striking headline result and it rests on a flawed comparison.
- **ETT forecasting comparison uses only weak baselines**: Figure 3(b) compares WARP only against GRU and LSTM. These are not competitive contemporary baselines for the ETT benchmark. The paper claims "WARP's superiority" (line 169) but only demonstrates it beats basic RNNs. Even if Appendix E contains additional results, the main table's claim is unsubstantiated by the comparison shown.

### Minor
- **Overclaiming in the conclusion**: The conclusion (line 283) claims "infinite-dimensional RNN hidden states" and "leading us a step further towards human-level artificial intelligence." The hidden state dimension D_θ is finite and acknowledged as memory-limited in Section 4.2. The neuromorphic/STDP connection (line 271) is a loose analogy, not a technical contribution. These rhetorical claims risk undermining credibility.
- **"Sub-quadratic in-context learning" claim lacks empirical support**: Section 3.4 claims "sub-quadratic in-context learning" (line 251) but provides no complexity analysis, runtime measurements, or scaling plots. Without wall-clock time vs. sequence length comparisons against Transformer baselines, this is an unsupported assertion.
- **WARP underperforms significantly on the longest classification sequences**: Table 4 shows WARP achieves 70.93% on EigenWorms (~18K length) vs. LinOSS at 95.0%, a 24-point gap. The paper claims "overcoming of vanishing and exploding gradient problems" (line 243), but this result contradicts that claim for the most challenging long-range dependency setting.
- **No ablation of input differences (Δx_t vs. x_t)**: Using Δx_t rather than x_t is a core architectural choice (Section 2.2). While motivated by Kidger et al. for continuous-time settings, no empirical ablation compares these formulations. Since Δx_t discards DC/constant-level information, this choice deserves empirical validation.

### Trivial
None

## Nice-to-Haves
- Report actual D_θ values used in experiments and A matrix sizes to quantify the resolution vs. parameter cost tradeoff.
- Ablate the coordinate system τ choice (raw index, normalized position, sinusoidal encoding, pixel coordinates).
- Provide runtime/complexity analysis for the ICL claim.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"A matrix scaling bottleneck undermines high-resolution motivation"** — The paper explicitly acknowledges this in Section 4.2 and proposes concrete future directions (low-rank, block-diagonal). This is a known limitation, not an overlooked flaw.
- **"Lotka-Volterra not tested with WARP-Phys"** — The paper explains this is due to artificial discontinuities from the repeat-copy variant (line 237). Scope limitation, not a methodological gap.
- **"WARP-Phys hard-codes functional form"** — This is the intended design of the physics-informed variant and is clearly stated. The 10× claim is accurate for the comparison shown.
- **"Negative BPD values for CelebA"** — Computational artifact of metric normalization, not a model error.
- **Format/style nitpicks** — Removed per policy.

## Novel Insights
The paper's genuinely novel contribution is the conceptual framework of using MLP weights as hidden states in a linear recurrence. This uniquely enables: (1) physics-informed root networks where domain knowledge is embedded in the decoder's forward pass, achieving order-of-magnitude improvements; (2) gradient-free test-time adaptation through fast weight updates without backpropagation; and (3) self-decoding where the hidden state eliminates a separate decoder. The combination of linear recurrence efficiency with non-linear MLP decoding expressivity is a meaningful new architectural design space.

## Suggestions
- **Fix or remove the PEMS08 comparison**: Either remove non-causal preprocessing and report causal results, or add non-causal variants of the baselines. This is the single most impactful revision for credibility.
- **Add competitive ETT baselines**: Include at least PatchTST or iTransformer in the main table.
- **Temper rhetorical claims**: Replace "infinite-dimensional" with "high-dimensional," remove "human-level AI," and qualify "sub-quadratic" with measurements.
- **Add Δx_t vs. x_t ablation**: A foundational architectural choice that deserves empirical validation.

## Calibration Anchors Retrieved

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Linear Recurrent NNs with Feature-Sequence Twist | I1484gDBr4.md | 2.50 | 1 | WARP is substantially more novel and better evaluated than this incremental/rejected paper |
| On Dynamics of Learning Time-Aware Behavior with RNNs | 7eYmijcuqO.md | 3.00 | 1 | WARP has much broader empirical scope and a more novel core idea |
| Learning Successor Representations with Distributed Hebbian | fnO5h1CFyh.md | 3.00 | 1 | Different domain; WARP is more practically relevant |
| Mamba Neural Operator | VtP7CamOR5.md | 3.00 | 1 | WARP has more extensive empirical evaluation |
| Learning Sequence Attractors in Recurrent Networks | biNhA3jbHc.md | 5.25 | 1 | WARP is more novel and empirically stronger |
| Gated RNNs discover attention | rfSfDSFrRL.md | 5.50 | 1 | Similar theoretical depth, but WARP has far broader empirical evaluation |
| Towards Analyzing Self-attention via Linear Neural Network | 4fVuBf5HE9.md | 4.33 | 1 | Different focus; WARP is more practically relevant |
| Local Polyak-Lojasiewicz for Overparameterized Linear Models | O0FOVYV4yo.md | 5.00 | 1 | Different domain; WARP is more novel architecturally |
| Oscillatory State-Space Models (LinOSS) | GRMfXcAAFh.md | 8.00 | 1 | LinOSS is stronger: rigorous theoretical proofs + strong results without fairness issues. WARP is below this tier |
| Never Train from Scratch | PdaPky8MUn.md | 8.00 | 1 | Strong evaluation paper with important findings. WARP is below this tier |
| Amortized Control of Continuous State Space | 8zJRon6k5v.md | 8.00 | 1 | Strong theoretical/empirical paper. WARP is below this tier |
| DeepLTL | 9pW2J49flQ.md | 8.00 | 1 | Different domain. WARP is below this tier |
| Generative Time Series Learning with Energy-Based Model | rGdEM131Ht.md | 5.60 | 2 | WARP is more novel and more broadly evaluated |
| TS-LIF: Temporal Segment Spiking Neuron | rDe9yQQYKt.md | 6.00 | 2 | **Most comparable**: both have biological inspiration, novel architecture, solid empirical evaluation. WARP has broader scope but PEMS08 fairness issue |
| TimeCapsule | blgJ4g00rC.md | 5.50 | 2 | WARP is more novel and more broadly evaluated |
| Neural Fourier Modelling | 8sKXFvSCqA.md | 6.20 | 2 | Similar broad evaluation scope. NFM has weaker classification evaluation; WARP has PEMS08 fairness issue. Roughly comparable |
| Training NNs as Recognizers of Formal Languages | aWLQTbfFgV.md | 6.25 | 2 | Different focus; both have novel approaches |
| TiC-LM | MB53uAZKSc.md | 6.25 | 2 | Different domain |
| RETSim | 23b9KSNQTX.md | 7.00 | 2 | Strong SOTA paper. WARP is below this tier |
| TGB-Seq Benchmark | 8e2LirwiJT.md | 6.40 | 2 | Benchmark paper, different type |

**Round 1 bracket:** 5.5–7.0. Round 2 narrowed to 5.5–6.5. WARP sits closest to TS-LIF (6.0) — both have genuine novelty, biological inspiration themes, and solid but imperfect evaluation. WARP has broader evaluation scope and more dramatic individual results (WARP-Phys 10× improvement, strong classification SOTA), but the PEMS08 fairness issue and overclaiming temper enthusiasm. The score is positioned at 6.0, matching TS-LIF, as the broader strengths and novel concept roughly balance the PEMS08 fairness concern and weak ETT baselines.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>