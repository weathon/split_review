Now let me write the final review.

## Summary

WARP (Weight-space Adaptive Recurrent Prediction) proposes a novel sequence modeling architecture where the hidden state of a linear RNN is the parameter vector of an auxiliary MLP, updated via a recurrence driven by input differences rather than raw inputs. This formulation unifies weight-space learning with linear recurrence, enabling gradient-free test-time adaptation, physics-informed variants, and in-context learning. Experiments span image completion, time series forecasting, dynamical system reconstruction, and classification.

## Strengths

- **Genuinely novel architectural formulation.** Using the flattened weights of an MLP as the recurrent hidden state (Eq. 1: θₜ = Aθₜ₋₁ + BΔxₜ) with input-difference-driven updates is a qualitatively new design. The paper correctly identifies (Section 1) that prior weight-space work treated weights as inputs/outputs, not intermediate representations. This is a clean synthesis of weight-space learning and linear recurrence.

- **Traffic forecasting without spatial structure beats graph-based SOTA by >50%.** On PEMS08 (Table 2), WARP achieves MAE=6.59 and RMSE=10.10 vs. the best prior model STDCN at 13.45/23.28. The paper is transparent that competing methods use graph structure while WARP does not, making this result genuinely noteworthy for a temporal-only model.

- **WARP-Phys achieves order-of-magnitude improvement on dynamical system reconstruction.** On MSD (Table 3), WARP-Phys achieves MSE=0.03±0.04 (×10⁻²) vs. the next-best Transformer at 0.34±0.12 — a >10× reduction. On MSD-Zero and SINE* the pattern is similar. Although this advantage comes from injecting the known physical form into the root network (which any architecture could do in principle), the ease of doing so within the WARP framework is a concrete benefit.

- **Competitive on UEA classification.** WARP achieves top-3 results on 4/6 datasets (Table 4), establishing new SOTA on EthanolConcentration (36.49%) and Heartbeat (80.65%). This is a solid showing against a strong lineup of SSM and RNN baselines.

- **Clean, well-motivated architecture.** The paper clearly explains the motivation behind each design choice: the identity initialization of A to emulate gradient descent, the zero initialization of B to prevent early divergence, the use of input differences for proportional updates, and the coordinate system τ for positional information.

## Weaknesses

### Major

- **The CelebA BPD values in Table 1 are anomalous and require explanation.** WARP's BPD values on CelebA are 0.052, –0.043, and –0.162, while baselines show wildly inconsistent values: GRU ranges 24.14–71.51, LSTM ranges from 3869 (L=100) down to 7.276 (L=300), and ConvCNP ranges 1.498–248.1. These values for the baselines do not follow the expected pattern (BPD should generally improve with longer context), and the drastic variation across methods trained with the same loss suggests a shared evaluation issue or miscalculation. WARP's negative BPD values — while theoretically possible for continuous data with a very sharp predictive distribution — are sufficiently unusual that the paper should explain them. Without clarification, the CelebA results cannot be taken at face value.

- **The in-context learning experiment (Section 3.4) lacks baselines and quantitative metrics.** The task is adapted from von Oswald et al., but no comparison is provided against ordinary least squares, linear regression, a Transformer, or even a simple RNN. Only scatter plots are shown; no MSE, R², or any other metric is reported. The claim of "sub-quadratic in-context learning" is unsubstantiated without knowing what performance level constitutes success. This section is essentially a qualitative demonstration, not an empirical evaluation.

### Minor

- **Root network size D_θ is not reported for any experiment.** Since the A matrix is D_θ × D_θ, the computational cost scales quadratically with root network size. The paper acknowledges scaling limitations (Section 4.2) and states experiments ran on an RTX 4080 with 16GB, but never reports actual D_θ values. This is essential for understanding the trade-off between expressivity and cost, and for evaluating the "high-resolution" / "infinite-dimensional" hidden state claim.

- **Significant gap on the most challenging long-range UEA dataset.** On EigenWorms (17,984 time steps), WARP scores 70.93%, trailing LinOSS by 24 points (95.0%). The paper's framing of "top three on four datasets" is accurate but obscures that on the dataset requiring the longest memory, WARP is far behind the leader. This is consistent with the paper's own acknowledgement that WARP "still struggles to achieve SOTA classification performance on extremely long sequences."

- **The "10× improvement" headline could be more clearly attributed.** The abstract states "a physics-informed variant outperforms the next best model by more than 10x." The paper is transparent that WARP-Phys embeds the known mathematical form of the dynamics (Section 3.2). However, the prominence of this claim in the abstract and conclusion, without equal prominence to the fact that it requires injecting the *exact* target function into the MLP forward pass, could misleadingly suggest this is a property of the core WARP architecture rather than of the prior knowledge.

### Trivial

- **"Infinite-dimensional" hidden state (Conclusion).** D_θ is finite and, given the 16GB GPU constraint, likely modest. This is an overstatement.

- **The MNIST BPD values in Table 1 show WARP is competitive but not dominant** (first at L=100 and L=300, second at L=600). The qualitative comparison in Fig. 3(a) is more visually compelling than the numbers suggest.

## Nice-to-Haves

- Add baselines (least-squares, simple RNN) and quantitative metrics to the ICL experiment.
- Report D_θ for all experiments to enable evaluation of the trade-off between root network size and performance.
- Include temporal-only baselines for PEMS08 to enable an apples-to-apples comparison.
- Provide a scaling curve showing performance vs. D_θ to demonstrate that larger root networks actually improve performance.
- Clarify the CelebA BPD computation to explain the anomalous baseline values.

## Removed Points

- **"Gradient-free adaptation is just a standard RNN forward pass"** — Removed because it misunderstands the paper. In standard RNNs, the decoder weights are fixed; in WARP, the *decoder itself* (MLP_θₜ) changes at each time step. The adaptive nature comes from this weight modulation, which is genuinely different from hidden-state-only RNNs.

- **"PEMS08 comparison is fundamentally unfair"** — Removed because the paper is transparent about the spatial-information asymmetry (Table 2 caption explicitly states baselines use spatial info), and the asymmetry makes WARP's result *stronger*, not weaker. The paper contextualizes the comparison appropriately.

- **"No controlled baseline reimplementation"** — Removed because citing results from published papers is standard practice in ML evaluation, especially for a first paper introducing a new architecture.

- **"No computation/memory benchmarks"** — Removed because the paper claims these are in Appendix E.3, which was stripped by the parser.

- **"The paper over-promises with 'transformative paradigm' and 'human-level AI'"** — Removed as a style/presentation nitpick; only the conclusion contains "human-level artificial intelligence" in a forward-looking sentence.

- Various duplicated/generic criticisms from the harsh critic's section-by-section sweep that lacked specific grounding in the paper.

## Novel Insights

The reviews reveal an interesting tension in the paper: WARP's core architectural idea — using MLP weights as the recurrent state with input-difference-driven updates — is genuinely novel and well-motivated. However, the paper's strongest headline results (PEMS08's 50% improvement, WARP-Phys's 10× improvement) are achieved in settings where the comparison is either asymmetric (temporal-only vs. spatial-temporal models) or relies on injected domain knowledge (physics-informed variant). The cleaner black-box comparisons (image completion, UEA classification, black-box DSR) show WARP as competitive but not dominant — typically within the top 2-3 methods but not uniformly ahead. This gap between the paper's most ambitious claims and the core architecture's demonstrated performance is common in new-method papers, but the paper would benefit from more carefully distinguishing what the architecture itself achieves from what domain-specific enhancements provide.

## Suggestions

1. **Clarify the CelebA BPD computation.** Explain why baseline BPD values vary so drastically with context length and across methods, and why WARP's BPD values are negative. If there is a legitimate reason (e.g., all models were evaluated on different scales), state it explicitly.

2. **Add baselines to the ICL experiment.** At minimum, compare against ordinary least squares (since the task is linear regression) and a small Transformer or RNN. Report quantitative metrics (MSE, R²).

3. **Report D_θ for all experiments** in the main paper or appendix. This is critical for understanding the computational trade-off.

4. **Tone down the "infinite-dimensional" and similarly overreaching language** in the conclusion to match what is actually demonstrated.

5. **Add a scaling experiment** showing how performance changes with D_θ to establish that the root network's capacity is actually being exploited.

## Score and Decision

**Round 1 (Bracketing):** Initial queries placed the paper in a band between weak anchors (~2.50) and strong anchors (8.00). The plausible range was determined to be roughly 4.5–6.5.

**Round 2 (Narrowing):** 
- *Gradient-free training of RNNs* (6.00, Reject): Similar profile (novel method, interesting approach, methodological clarity issues). WARP has broader experiments and clearer presentation but has questionable experimental results (CelebA BPD). Comparable quality.
- *Robustifying SSMs* (6.50, Accept): Stronger theoretical contribution, clearer writing, but more modest empirical gains. WARP has less theory but more novel architecture.
- *Mamba* (6.25, Reject): Highly influential work rejected over evaluation gaps. WARP has similar evaluation-gap issues (no ICL baselines, CelebA BPD) but less overall impact.
- *From Layers to States* (6.75, Accept): Novel application of SSMs, strong experiments. WARP's architecture is more novel but its experiments are less clean.

**Final determination:** The paper sits between 5.0 and 6.0. The core idea is genuinely novel and the experiments are broad, but the anomalous CelebA BPD values, missing ICL baselines, and unreported D_θ values are real weaknesses that would need resolution. WARP is stronger than the 2.50–5.25 range of rejected papers but has more unresolved issues than the 6.25–6.75 range of accepted papers.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>