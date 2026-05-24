Now I have sufficient calibration data. Let me construct the final review.

## Summary

The paper introduces **WARP** (Weight-space Adaptive Recurrent Prediction), a sequence model whose hidden state is the linearly-updated weights of an auxiliary MLP (the "root network"), decoded by feeding a coordinate $\tau$ through that MLP. The recurrence uses input differences $\Delta \mathbf{x}_t$ rather than raw inputs. The paper evaluates WARP on image completion, traffic/energy forecasting, dynamical system reconstruction (with a physics‑informed variant), multivariate time series classification, and a synthetic in‑context learning task.

---

## Strengths

1. **Novel conceptual contribution — weight‑space as hidden state in a linear recurrence.**  
   The idea of treating the *weights* of a neural network as the hidden state of an RNN, and updating them via a learnable linear map $A$, is genuinely novel. This goes beyond prior "fast weight" ideas by making the weight update itself parametric and differentiable. The resulting architecture cleanly separates the linear recurrence (efficient, parallelizable) from the non‑linear decoding (expressive). The self‑decoding property ($\theta_t$ serves as both state and decoder) is a neat mechanism that saves parameters.

2. **Strongest result: physics‑informed variant achieves >10× improvement on dynamical system reconstruction.**  
   WARP‑Phys obtains MSE $0.03\times10^{-2}$ on MSD and $0.04\times10^{-2}$ on MSD‑Zero (Table 3), compared to $0.34\times10^{-2}$ and $0.48\times10^{-2}$ for the next best models. This is a striking demonstration that injecting domain‑specific priors into the root network — which is straightforward in this architecture — can yield large gains, and this result stands independently of other experiments.

3. **Competitive classification results on 4/6 UEA datasets.**  
   WARP achieves state‑of‑the‑art accuracy on EthanolConcentration ($36.49\%$) and Heartbeat ($80.65\%$), ranks second on SelfRegulationSCP2, and third on MotorImagery (Table 4). The evaluation includes 11 diverse baselines (LRU, S5, Mamba, Griffin, etc.) and reports standard deviations over 5 runs.

4. **Parallel training via convolutional mode.**  
   The derivation of a convolution kernel $K$ such that $\theta_{0:T} = K \star \Delta \mathbf{x}_{0:T}$ (Section 2.3) allows the hidden states to be pre‑computed in parallel, sharing the hardware‑efficient training of linear RNNs/SSMs while retaining non‑linear decoding.

---

## Weaknesses

### Major

1. **Core architectural parameters (D_θ, root network structure, A parametrization) are never specified.**  
   Equation (1) defines $A \in \mathbb{R}^{D_\theta\times D_\theta}$ and $B \in \mathbb{R}^{D_\theta\times D_x}$ where $D_\theta$ is the number of parameters of the root MLP. The paper reports ~1.68M total parameters for MNIST experiments but never states $D_\theta$, the root network depth/width, or whether $A$ is stored as a full dense matrix or approximated (diagonal, low‑rank, block‑diagonal). The Limitations section (p. 8) acknowledges that "the size of the matrix $A$ limits scaling to huge root neural networks" and mentions future work on structured parametrizations, strongly implying the current implementation uses a full $A$. If $A$ is full, $D_\theta^2$ dominates the parameter count, so $D_\theta \approx 1300$ for MNIST — a very small root MLP. Without explicit architecture details the method is not reproducible from the paper alone, and the reader cannot assess whether the root network is expressive enough to justify the claims about "high‑resolution" or "infinite‑dimensional" hidden states.

2. **Image‑completion evaluation on CelebA is compromised by clearly broken baseline BPD values.**  
   In Table 1, baseline bits‑per‑dimension on CelebA are orders of magnitude beyond reasonable ranges: LSTM reaches 3869 (at $L=100$), ConvCNP reaches 248.1 (at $L=600$), GRU reaches 71.51. These values indicate catastrophic failure of the baselines' uncertainty estimation under the NLL loss, not meaningful comparison. Meanwhile WARP reports negative BPD (e.g., −0.162), which, while mathematically possible for a Gaussian NLL on bounded data, is unusual and goes unexplained. The paper states all models were "trained with the NLL loss in recurrent AR mode to ensure fair comparison," but the results suggest the baselines were not properly configured for this loss. This undermines the claim that WARP outperforms baselines on image completion — the MSE comparison may still stand, but the headline BPD comparison is unreliable. *(Note: MNIST BPD values are reasonable across all models, so the problem is specific to CelebA but still significant.)*

3. **Traffic‑forecasting result lacks sufficient experimental context for the claimed 50%+ improvement.**  
   WARP achieves MAE 6.59 on PEMS08, more than halving the previous best (13.45, Table 2). This would be a remarkable result — a simple sequence model without graph structure far outperforming specialized spatiotemporal GNNs. The paper mentions a "non‑causal convolution" preprocessing step (deferred to Appendix D, which is not available in this version) and provides minimal detail about data splits, training procedure, and evaluation protocol. Given the extraordinary magnitude of the improvement, the main paper should include enough detail for a reader to assess the evaluation's fairness. The current presentation makes this result impossible to verify without access to the code and supplementary materials.

### Minor

4. **Black‑box WARP is not consistently dominant.**  
   On the MSD dynamical system, the black‑box WARP (MSE $0.94\times10^{-2}$) is *worse* than the Transformer baseline ($0.34\times10^{-2}$, Table 3). On EigenWorms classification, WARP ($70.93\%$) substantially underperforms the best method LinOSS ($95.0\%$, Table 4). The paper's framing sometimes implies across‑the‑board superiority, but the actual results are more mixed — WARP is strong on several tasks but weak on others, which is fine but should be acknowledged more precisely.

5. **"Gradient‑free test‑time adaptation" is standard forward recurrence, not an additional adaptation mechanism.**  
   The paper repeatedly highlights "gradient‑free adaptation" as a key advantage. In reality, the update $\theta_t = A\theta_{t-1} + B\Delta x_t$ is simply the forward pass of the model — there is no separate test‑time optimization loop, no loss computed at inference, and no steering of the update toward a test‑time objective. Every RNN "adapts" its hidden state in this sense; what differs here is that the hidden state *is* a set of neural network weights. The terminology evokes methods that perform explicit test‑time optimization (e.g., test‑time training) and is somewhat overblown, though the paper does clearly describe what the recurrence does.

6. **In‑context learning evaluation is limited to a single synthetic linear‑regression task.**  
   Section 3.4 demonstrates that WARP can learn a linear mapping from synthetic key‑value pairs. This is a proof‑of‑concept but far from the scale or complexity of ICL benchmarks used in the LLM literature. No comparison to other ICL‑capable models is provided.

7. **No results on standard long‑sequence benchmarks (LRA, WikiText‑103, sCIFAR, etc.).**  
   The paper acknowledges this in the Limitations section, but given the centrality of long‑range dependency modeling to the SSM/linear‑RNN literature that WARP builds on, the absence of any such evaluation makes it hard to assess where WARP sits relative to S4, Mamba, LRU, etc. on tasks that genuinely require long memory.

### Trivial

8. The paper would benefit from an ablation that replaces $\Delta \mathbf{x}_t$ with $\mathbf{x}_t$ to isolate the effect of input differencing. An ablation varying $D_\theta$ with fixed total parameters would also clarify the scalability limitation.
9. The caption ordering of subfigures in Figure 3 is confusing (labels a, b are used for both the digit grids/heatmap and the MNIST comparison/ETT heatmap).

---

## Nice‑to‑Haves

- A breakdown of how the total parameter budget is distributed among $A$, $B$, $\phi$, and other components.
- Statistical significance tests or confidence intervals for the main comparison tables.
- A study of how performance changes as $D_\theta$ is varied while controlling total parameter count via root network depth/width.

---

## Removed Points

- **Criticism about the A matrix making the method "not implementable" / "misrepresented"** (Harsh Critic #1): The concern that a full $D_\theta\times D_\theta$ matrix is too large is legitimate *as a missing detail*, but the paper *does* implement the method and report results — the criticism that it "cannot be reproduced" or is "misrepresented" is too strong given that the code is released and the limitation is acknowledged. Retained as Major #1 with softened language.
- **Criticism about traffic experiment "cannot be trusted" due to appendix being missing** (Harsh Critic #3): The parser strips appendices from all papers. The criticism that experimental details are in an "appendix that is not available" conflates parser artifact with author omission. Weakened to Minor #3 with focus on the need for more main‑text detail given the extraordinary result magnitude.
- **Criticism that "gradient‑free adaptation" is "overblown" and "inflates the novelty"** (Harsh Critic #4): The paper clearly describes what the recurrence does. The term is somewhat marketing but not incorrect — the θ_t updates are indeed gradient‑free in the sense that no gradient computation is needed for the weight‑state update, unlike test‑time training methods. Retained as Minor #5 with softened language.
- **Strength Finder claim about "state‑of‑the‑art traffic flow forecasting without exploiting graph structure"**: This is factually correct as presented in Table 2, but the magnitude of improvement warrants caution. Kept as implicit in Weakness #3.
- **Strength Finder claim about "order‑of‑magnitude improvement"** and **"top‑three on 4/6 UEA datasets"**: Both are accurate and supported by Tables 3 and 4. Retained in Strengths.

---

## Novel Insights

The review process surfaces a tension not fully resolved in the paper: the conceptual appeal of "infinite‑dimensional" weight‑space states versus the practical reality of a small root MLP constrained by the $O(D_\theta^2)$ memory of $A$. The physics‑informed results suggest that the *quality* of the root network representation (incorporating domain structure) matters more than its raw size — a potential insight the paper could lean into more explicitly. The classification results also reveal that WARP's strengths are task‑dependent rather than universal, which is valuable for guiding future applications.

---

## Suggestions

1. **Specify D_θ and root network architecture for every experiment.** State whether $A$ is stored as a full matrix or approximated. If it is full, give D_θ explicitly and discuss the implied root network capacity.
2. **Fix the CelebA image‑completion evaluation.** Either retune the baselines to produce sensible BPD values, switch to a metric that is robust across models (raw MSE with a discussion), or explain why the baseline BPD values are so extreme.
3. **Provide a more complete experimental protocol for PEMS08 in the main paper** (or ensure the appendix contains all details). Add a discussion of why a non‑causal convolution is used and how this differs from prior work's preprocessing.
4. **Add an ablation replacing Δx_t with x_t** to justify the input‑difference design choice.
5. **Tone down the "gradient‑free adaptation" framing** to accurately describe what the recurrence does, or add a small experiment that tests adaptation to distribution shift at test time.
6. **Include at least one standard long‑sequence benchmark** (e.g., sequential CIFAR, sMNIST, or a subset of LRA) to position WARP relative to the SSM/linear‑RNN literature.

---

## Score and Decision

### Calibration anchors

**Round 1 (bracketing):**
| Anchor | Avg score | Round | Comparison |
|--------|-----------|-------|------------|
| I1484gDBr4 (Linear RNN feature‑sequence twist) | 2.50 | R1 | Weaker than WARP — less novel, narrower scope |
| 7eYmijcuqO (Dynamics of learning time‑aware behavior with RNNs) | 3.00 | R1 | Weaker — narrower analysis, less empirical breadth |
| hgjpO0H0id (Interplay between learning and memory in deep SSMs) | 4.00 | R1 | Comparable theoretical depth but less empirical breadth |
| iVy7aRMb0K (Mimetic Initialization helps SSMs) | 4.50 | R1 | Comparable novelty, narrower evaluation |
| DjeQ39QoLQ (Robustifying SSMs via Approx. Diagonalization) | 6.50 | R1 | Stronger — rigorous theory + thorough experiments |
| STUGfUz8ob (When can transformers reason with abstract symbols?) | 7.60 | R1 | Stronger — tight theory‑experiment coupling |

**Round 2 (narrowing):**
| Anchor | Avg score | Round | Comparison |
|--------|-----------|-------|------------|
| biNhA3jbHc (Learning Sequence Attractors in RNNs) | 5.25 | R2 | Less novel, narrower empirical scope than WARP |
| XoYdD3m0mv (Deep Linear Probe Generators) | 6.00 | R2 | Cleaner method and evaluation, but on a different task family |
| EGjvMcKrrl (Generalization analysis to optimization for SSMs) | 6.00 | R2 | Stronger theory, weaker empirical |
| rfSfDSFrRL (Gated RNNs discover attention) | 5.50 | R2 | Comparable — novel connection, limited experiments |
| GrmFFxGnOR (Were RNNs All We Needed?) | 5.00 | R2 | Less novel (simplification of existing), broader benchmarks |
| dALYqPm9gW (Recurrent Linear Transformers) | 4.75 | R2 | Less novel, narrower evaluation |
| UU9Icwbhin (Retentive Network) | 4.75 | R2 | Less novel architecture, larger‑scale eval |
| amOpepqmSl (HadamRNN) | 6.00 | R2 | More specialized contribution, cleaner evaluation |
| AL1fq05o7H (Mamba) | 6.25 | R2 | More influential architecture, broader impact |
| l0ZzTvPfTw (FlashRNN) | 6.50 | R2 | Stronger engineering contribution, clearer results |

**Initial bracket (Round 1):** 4.0–6.5. **Narrowed bracket (Round 2):** 5.0–6.0.

Comparing WARP to the closest anchors: it is more novel than "Were RNNs All We Needed?" (5.00) and "Recurrent Linear Transformers" (4.75), but has more significant evaluation issues than "Gated RNNs discover attention" (5.50) or "Deep Linear Probe Generators" (6.00). The missing architectural details and the CelebA BPD problem are concrete weaknesses that the anchors at 6.00 do not have. I therefore place WARP at the lower end of the narrowed bracket.

**Final score: 5.5** — Genuinely novel contribution with broad experiments, but significant missing implementation details and a compromised baseline comparison prevent acceptance in the current form. With these issues addressed, the paper could be competitive at a venue with a ~6.0–6.5 threshold.

**Decision: Reject**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>