Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize my final review.

---

## Summary

WARP introduces weight-space linear RNNs, a novel architecture where the hidden state of a linear recurrence is the flattened parameter vector of an auxiliary MLP. The model updates these weights via input differences (Δxₜ) through a linear transition, then decodes by applying the resulting MLP to a coordinate τ. This design enables gradient-free adaptation, in-context learning, and physics-informed modeling. The paper evaluates WARP across image completion, traffic forecasting, dynamical system reconstruction, time-series classification, and a proof-of-concept ICL task, showing strong results particularly on PEMS08 traffic forecasting (>50% MAE reduction over SOTA) and physics-informed dynamical system reconstruction.

## Strengths

- **Genuinely novel architectural paradigm.** The core idea — using the weights of an auxiliary network as the hidden state of a linear recurrence — is a clean conceptual departure from both standard RNNs (which use fixed-dimensional hidden vectors) and prior weight-space methods (which treat weights only as inputs/outputs). Equation 1 and Figure 2 define this architecture crisply, and the self-decoding property (θₜ serves as both hidden state and decoder parameters) is an elegant parameter-saving design.

- **Strong, diverse empirical results.** On MNIST image completion WARP achieves the best MSE and BPD across all context lengths (Table 1), and on CelebA the BPD gap is dramatic (e.g., −0.162 vs. 71.51 for GRU at L=600). On PEMS08 traffic forecasting it reduces MAE from 13.45 to 6.59 without using graph structure (Table 2). On dynamical system reconstruction, black-box WARP ranks top-two on 3 of 4 settings (Table 3).

- **Compelling physics-informed variant.** WARP-Phys demonstrates that the architecture cleanly supports injecting domain-specific functional forms into the root network, achieving over an order-of-magnitude improvement on MSD reconstruction (0.03×10⁻² vs. 0.34×10⁻² for Transformer, Table 3). This is a concrete, well-executed demonstration of the framework's flexibility rather than merely a claim.

- **Honest limitations section.** The paper explicitly acknowledges the scalability bottleneck (quadratic growth of A with Dθ), the lack of theoretical grounding, and struggles on extremely long sequences (Section 4.2). This transparency strengthens the paper.

## Weaknesses

### Major

- **In-context learning evaluation is too weak to support the claim.** The ICL experiment (Section 3.4) tests only a simple linear mapping with random keys on a cumulative-sum transformation. No baseline model is evaluated in the same setting. The paper lists in-context learning as a core practical use case (contribution 2) and mentions it in the abstract, but the current evaluation — a single toy task with no comparison — does not substantiate that WARP has meaningful ICL capabilities. A credible demonstration would require standard few-shot regression benchmarks and at least one baseline (e.g., a linear attention model or Transformer). The architectural mechanism (extracting the final root network to answer queries without re-processing the context) is interesting but its practical value relative to alternatives remains undemonstrated.

### Minor

- **Classification benchmark is narrow.** The UEA evaluation (Table 4) uses only 6 of 30 datasets, selected by criteria from prior work. While the selection rationale is stated and the paper compares against 10 baselines, the narrow coverage means the claim of "top three in 4 out of 6" cannot be distinguished from favorable subset selection. On the longest-sequence datasets (EigenWorms, Motor), WARP performs substantially below the best models (70.93 vs. 95.0 LinOSS on EigenWorms). Expanding the benchmark or analyzing failure modes would strengthen the contribution.

- **ETT energy forecasting uses only weak baselines.** Figure 3(b) compares WARP against only GRU and LSTM — architectures that are decades old and not competitive with modern time-series forecasters. While the paper does not claim SOTA for this task, the results over-promise relative to the evidence. A modern baseline (e.g., PatchTST, TimesNet) would contextualize the numbers.

- **Non-causal convolution in PEMS08 not described in main text.** The paper states that input is preprocessed with a non-causal convolution and defers details to Appendix D (stripped). Given the remarkable >50% MAE improvement, the reader cannot assess whether this preprocessing leaks future information or creates an unfair comparison. At minimum, the main text should define the operation and justify its causality properties.

- **Ablation studies deferred to stripped appendix.** The paper claims (Section 4.1) that ablation studies in Appendix E confirm "architectural necessity of key components," including the input-difference design choice. Since these are not visible to the reviewer, the strength of these ablations cannot be verified. The paper would benefit from a summary of key ablations (especially Δx vs. raw x) in the main text.

- **Physics-informed narrative slightly overclaims.** The "more than 10x improvement" headline conflates the utility of the supplied analytical prior with WARP's innate predictive power. WARP-Phys receives the exact ODE form, so large gains are expected. The genuine contribution — architectural flexibility that cleanly supports such injection — could be presented more precisely by comparing against a baseline that also receives the physics prior.

### Trivial

- The statement that WARP is "the latest scientific machine learning technique that seamlessly integrates interpretable physical knowledge" overstates the novelty of physics-informed modeling, which PINNs and Neural ODEs have done for years. The contribution is the specific mechanism (integration into a discrete linear recurrence with weight-space states), not the general concept.

- The description of self-decoding ("θₜ plays both the roles of the hidden state and the parameters of the decoder, effectively decoding itself") slightly oversimplifies, since the root network also receives the external coordinate τ as a side input.

## Nice-to-Haves

- Adding a diagram or table showing computational complexity (wall-clock time, memory, parameter counts) compared to baselines like S4, Mamba, and Transformer would help readers assess the practical trade-offs.
- Demonstrating even a simple mitigation of the scalability issue (e.g., block-diagonal A with a small experiment showing it doesn't severely degrade performance) would address the most prominent architectural limitation.
- A direct comparison of Δx vs. raw x as recurrence input would justify a core design choice with evidence rather than citation alone.

## Removed Points

These points were flagged for removal during the consolidation process:

- **"Zero-initialisation of B causes training difficulties"** — The paper explicitly justifies this choice: "We find that initializing the input transition matrix B as the zero matrix is useful to ensure that the sequence of weights θₜ does not diverge early on in the training." This is a stated, reasoned design decision. The harsh critic's speculation about vanishing gradients is not backed by any evidence from the paper.

- **"Gradient-free test-time adaptation claim is ambiguous or conflated with standard TTA"** — The paper defines its usage clearly: θₜ are updated T−1 times using Eq. (1), not using gradient descent. This is a specific, self-consistent definition consistently applied throughout. The harsh critic's concern about conflation with standard TTA is a terminological disagreement, not a flaw in the paper.

- **"Scalability is a fatal/structural barrier"** — The paper acknowledges this openly in Section 4.2 as a limitation and future work direction. A self-identified limitation is not a weakness of the work as presented; it is responsible scholarship.

- **"First of its kind" claim overstated** — The paper qualifies this with "to the best of our knowledge" and the specific formulation (weight-space features as intermediate hidden states in a recurrence) is genuinely distinct from prior hypernetwork-based sequence models. The harsh critic acknowledges this: "though WARP's specific formulation is distinct."

- **Missing related works** — No external sources available to verify these claims; this is a universal removal rule.

- **Typos, formatting, grammar issues** — Parser artifacts, not author errors. Removed per hard rules.

- **Reproducibility nits (undisclosed hyperparameters, training logs)** — Removed per hard rules.

- **"Appendix is stripped so proofs/training algorithms cannot be verified"** — The parser strips all appendices; this is not an author error.

## Novel Insights

The most striking observation emerging from this review is that WARP's weight-space formulation creates an architecture where the hidden state's dimensionality scales with the *parameter count of the root network* rather than with a fixed hyperparameter. This means the model's memory capacity is architecturally tied to the expressivity of the decoder — a coupling that does not exist in standard RNNs or SSMs. The self-decoding property (θₜ is simultaneously the state representation and the decoder) elegantly enforces this coupling and eliminates a separate decoder parameter matrix. This design may have implications beyond the current paper: it suggests a general recipe for constructing sequence models where capacity allocation between memory and decoding is unified rather than independently tuned.

## Suggestions

- **Deepen the ICL evaluation.** Replace or supplement the current toy setting with a standard few-shot regression benchmark (e.g., sinusoid regression from meta-learning literature). Compare against at least a Transformer and a linear-attention model. This would transform the ICL claim from speculative to demonstrated.

- **Expand the classification benchmark or re-scope the claim.** Either run WARP on a larger random subset of UEA and report aggregate metrics, or explicitly narrow the classification claim to mid-length sequences where WARP excels, rather than implying broad competency.

- **Add a modern ETT baseline.** Include at least one Transformer-based or SSM forecaster to contextualize the energy-prediction results.

- **Summarize key ablations in the main text.** The claimed ablation confirming the necessity of input differences (Δx vs. x) is central to the biological motivation. A one-paragraph summary of this and the computational-efficiency ablation from Appendix E.3 would significantly strengthen the main paper without requiring much space.

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison to WARP |
|--------|------|-----------|-------|-------------------|
| FSFC RNN | 4ymHtDAlBv | 2.33 | R1 | Clearly weaker — limited novelty, narrow eval |
| Linear RNN Feature-Sequence Twist | I1484gDBr4 | 2.50 | R1 | Clearly weaker — incremental contribution |
| QuantFormer | BBldjKEBlJ | 3.00 | R1 | Clearly weaker — domain-specific, limited scope |
| FIA-Net | WFlLqUmb9v | 2.50 | R1 | Clearly weaker — narrow contribution |
| Learning Sequence Attractors | biNhA3jbHc | 5.25 | R1 | Weaker — more limited evaluation, narrower scope |
| Resonator-Gated RNNs | IlNVkYUSfF | 5.00 | R1 | Weaker — limited evaluation, missing modern baselines |
| Gradient-free RNN Training | vcJiPLeC48 | 6.00 | R1/R2 | WARP is stronger — broader evaluation, better results, more novel concept |
| TS-LIF | rDe9yQQYKt | 6.00 | R1 | Comparable score — solid novel architecture, good evaluation |
| ProbeGen | XoYdD3m0mv | 6.00 | R2 | Comparable — weight-space learning but narrower scope |
| Robustifying SSMs (PTD) | DjeQ39QoLQ | 6.50 | R2 | WARP broader empirically, PTD stronger theoretically |
| PoDiNNs | U1DjXQeJRx | 6.60 | R2 | Similar breadth, PoDiNNs stronger theory, WARP more novel concept |
| LinOSS | GRMfXcAAFh | 8.00 | R1 | Clearly stronger — theoretical backing, thorough single-domain eval |
| Artificial Kuramoto | nwDRD4AMoN | 9.00 | R1 | Clearly stronger — broader impact, stronger contributions |

**Round 1 bracket:** 5.0–7.5 (WARP is clearly above the weak 2–3 anchors and clearly below the strong 8–9 anchors, sitting in the middle band)

**Round 2 narrowing:** The comparison against Gradient-free RNN (6.0, Rejected), ProbeGen (6.0, Accepted), Robustifying SSMs (6.50, Accepted), and PoDiNNs (6.60, Accepted) places WARP solidly in the 6.0–6.5 range. WARP is stronger than Gradient-free RNN (broader evaluation, more novel concept, better results) and comparable to ProbeGen and Robustifying SSMs. It does not reach PoDiNNs' level (which has stronger theoretical foundations and cleaner domain-specific contributions) nor LinOSS (which has universality proofs and tighter evaluation).

**Final placement: 6.0.** The core architectural contribution is novel and well-supported by the image completion, traffic forecasting, and dynamical systems experiments. However, the in-context learning claim — listed as a core contribution — is not adequately substantiated, and the classification benchmark is narrow. These weaknesses are significant enough to prevent a higher score but do not invalidate the central contribution. The paper is a solid accept with the expectation that the ICL and classification evaluations are strengthened.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>