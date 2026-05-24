Now I have a thorough understanding. Let me compose the final review.

---

## Summary

This paper introduces WARP (Weight-space Adaptive Recurrent Prediction), a novel recurrent architecture where the hidden state is the flattened weights of an auxiliary MLP ("root network"), updated via a linear recurrence driven by input differences. Decoding is performed by applying the root network to a coordinate system. The weight updates in the forward pass are gradient-free (no BPTT needed for the fast weights), and the model supports convolutional and recurrent training modes via parallel scan. Experiments span image completion, energy/traffic forecasting, dynamical system reconstruction (including a physics-informed variant achieving >10x improvement), multivariate time-series classification, and in-context learning.

## Strengths

- **Genuine architectural novelty.** The core idea — treating the weights of an auxiliary network as a recurrent hidden state updated through a linear recurrence on input differences — is original and well-motivated. The combination of linear recurrence in weight space with non-linear decoding is a fresh contribution to the sequence modeling literature (Eq. 1, Figure 1).

- **Physics-informed variant demonstrates compelling capability.** WARP-Phys, which embeds explicit physical formulations (e.g., sinusoidal parameterization) into the root network, achieves more than an order-of-magnitude improvement over standard WARP and all baselines on dynamical system reconstruction (Table 3). This illustrates a unique and practically valuable ability to incorporate domain priors that standard RNNs and SSMs lack.

- **Broad empirical coverage.** The paper evaluates WARP across five distinct experimental settings (image completion, energy forecasting, traffic forecasting, dynamical systems, multivariate classification, in-context learning), demonstrating the architecture's versatility rather than cherry-picking a single favorable task.

- **Competitive classification results.** On UEA multivariate time-series classification, WARP establishes new best accuracies on Ethanol and Heartbeat and places in the top three on four of six datasets (Table 4), with results reported alongside a consistent set of baselines from a shared evaluation protocol [96].

- **Practical training.** The dual convolutional/recurrent training modes with parallel scan (Section 2.3, Appendix B.2) make the model practically trainable despite its high-dimensional hidden state.

## Weaknesses

### Fatal

None.

### Major

- **Overclaiming around "adaptation" and "in-context learning."** The paper repeatedly characterizes the forward-pass weight updates (Eq. 1) as "gradient-free adaptation" and "test-time adaptation" (abstract, Sections 1, 2.2, 4.1, 4.3). The update rule is simply the model's intended forward computation — the fast weights evolve according to a fixed learned linear recurrence, not in response to a distribution shift or new task. This is not adaptation in the standard ML sense (e.g., TTT, domain adaptation); it is the ordinary operation of the architecture. Similarly, the in-context learning experiment (Section 3.4) demonstrates that a network can be trained to regress a linear mapping from cumulative-sum-transformed keys, but the paper frames this as general ICL comparable to Transformers or few-shot learners. The claim of "sub-quadratic" ICL is made without any complexity comparison or runtime measurement against a Transformer baseline solving the same task. This inflated rhetoric weakens confidence in the paper's other claims and should be recalibrated.

- **PEMS08 traffic result lacks sufficient justification.** WARP achieves a 2× MAE improvement over the previous SOTA on PEMS08 (6.59 vs. 13.45) while not using the spatial graph structure that prior graph-based models explicitly leverage (Table 2). The paper mentions non-causal convolution preprocessing but defers all details to Appendix D. An improvement of this magnitude over carefully engineered GNN baselines demands at minimum a controlled ablation (e.g., same convolution with a standard RNN head) to disentangle the contribution of preprocessing from the architecture. Without this, the result is suggestive but not trustworthy as evidence of architectural superiority.

### Minor

- **Extreme LSTM BPD values on CelebA not discussed.** The LSTM baseline reports a BPD of 3869 for L=100 on CelebA (Table 1), which almost certainly indicates training failure rather than a genuine performance gap. While the paper's comparison with the properly-functioning S4 baseline (where WARP performs competitively) is the more meaningful evaluation, the paper should explicitly acknowledge that the LSTM and ConvCNP BPD numbers are unreliable and focus the comparison on converged models.

- **ETT results lack dispersion measures.** The ETT heatmap (Figure 3b) reports mean MSE from three runs but without error bars, standard deviations, or statistical tests. The numerical differences between WARP and the runner-up (LSTM) on some subsets are small (e.g., 2.06 vs. 3.42 on m1, but 6.44 vs. 2.02 on h2), making it difficult to assess whether the claimed superiority is statistically meaningful.

- **"Infinite-dimensional hidden state" language is inaccurate.** The conclusion states that the weight-space formulation yields "infinite-dimensional RNN hidden states," but the hidden state θ_t has fixed dimension D_θ (Section 4.3). This is rhetorical overreach and should be replaced with an accurate description.

- **Limited baseline coverage on the repeat-copy experiment.** The Lotka-Volterra repeat-copy evaluation (Section 3.2, Table 3) compares only against GRU, LSTM, and Transformer — modern long-range SSMs (S4, Mamba, etc.) are absent from this specific comparison, limiting the informativeness of the claimed superiority.

### Trivial

- The coordinate system τ is under-motivated in the main text; for classification tasks where the MLP output is reduced to a single softmax logit, it is not obvious why a full coordinate-based MLP decoder is needed over a simpler linear readout.
- The neuromorphic/STDP connection (Section 4.1) is mentioned but not developed, adding little.
- The fast-weights literature connection is noted only in passing; a more explicit differentiation from prior fast-weight programmers and TTT frameworks would strengthen the paper's positioning.

## Nice-to-Haves

- Scaling curves for training time and memory vs. D_θ would help readers assess practical trade-offs.
- Lifting key ablation results (effect of removing input differences, fixed readout vs. MLP decoder, varying D_θ) into the main text from the appendix would make the paper more self-contained regarding which components are necessary.
- Replacing "gradient-free adaptation" with precise language like "input-driven weight-space state updates" throughout.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **UEA non-standard split invalidates results (Harsh Critic #1):** REMOVED. The paper explicitly states that baseline numbers are "as reported in [96]," and that datasets were "selected and preprocessed following the criteria... with sequence length ranging from 405 to almost 18k [96]." This indicates [96] established a consistent evaluation protocol (70:15:15 split) under which all baselines were evaluated. The harsh critic's claim that baselines came from different papers using different splits is speculative and contradicted by the paper's description. The comparison appears to be on a shared, consistent protocol.

- **PEMS08 non-causal convolution may constitute data leakage (Harsh Critic #2):** DEMOTED to Major (above) and stripped of speculation. The concern about the 2× improvement is legitimate, but the "data leakage" claim is purely speculative without seeing Appendix D. The retained weakness focuses on the lack of controlled ablation.

- **"Gradient-free adaptation" is entirely misleading (Harsh Critic #4):** RETAINED but at Major tier — the paper's framing does overstate what the mechanism delivers, but the underlying mechanism (fast weights updated without gradients in the forward pass) is a real architectural property. The harsh critic's framing that this is "simply the model's forward computation" and "not an adaptation to a new task" is correct, which is why this is kept as a real concern about rhetoric.

- **Strength Finder claim "WARP achieves SOTA on multiple benchmarks":** PARTIALLY RETAINED. The UEA classification results are competitive and WARP leads on 2/6 datasets. The PEMS08 result is flagged as needing better justification. The general framing has been incorporated into the strengths but qualified.

- **Strength Finder claim about ablation studies:** RETAINED as Nice-to-Have, since the ablation results are cited but reside in the stripped appendix; the main paper would benefit from summarizing the most important ones.

- **All formatting/typo complaints from Harsh Critic:** REMOVED per instructions — parser artifacts.

- **Criticism about missing appendix/references:** REMOVED per instructions — the parser strips these.

- **Criticism about "redefine sequence modelling" and "transformative paradigm" rhetoric:** INCORPORATED into the Major weakness about overclaiming rather than treated as a separate formatting issue.

- **Human Finder weaknesses about missing related works:** REMOVED per instructions — cannot verify external sources.

## Novel Insights

The most interesting insight emerging from this work is that weight-space representations can serve as intermediate hidden states in recurrent architectures, not merely as inputs or outputs to meta-learners. The physics-informed variant (WARP-Phys) concretely demonstrates why this matters: because the hidden state *is* the parameters of a function approximator, domain knowledge can be injected directly into the recurrence's representational substrate (e.g., replacing a black-box MLP with a sinusoidal parameterization), yielding dramatic performance gains that are structurally impossible in standard RNNs where the hidden state is an opaque vector. This architectural property — that the hidden state has interpretable *functional* semantics — is genuinely novel and opens an interesting design axis for future sequence models.

## Suggestions

- The single highest-impact revision would be to recalibrate the language around adaptation and ICL. Replace "gradient-free adaptation" with "forward-pass weight modulation" or similar, and clearly distinguish the mechanism from test-time adaptation and few-shot ICL. This would let the real architectural contribution stand without the reader questioning whether the claims are inflated.
- For PEMS08, run an ablation replacing WARP's weight-space recurrence with a standard linear RNN head while keeping the same non-causal convolution. Report both numbers. If WARP still wins, the architectural claim is much stronger; if not, the paper should acknowledge the convolution's role.
- Add standard deviations to the ETT heatmap and Table 1 results, even in a footnote.
- Move a one-paragraph summary of key ablations (input differences, root network depth, D_θ) from Appendix E into Section 4.1.

## Score and Decision

**Calibration report:**

Round 1 bracketing placed the paper between ~5 and ~7.5 based on three bands of anchors.

Round 1 anchors:
- I1484gDBr4 (2.50), 7eYmijcuqO (3.00), 2NwHLAffZZ (2.33), kkVTeMvC9D (3.40) — weak band; WARP is clearly stronger than all of these.
- dM1wO2OkbO (6.33) "CausalRNs", GrmFFxGnOR (5.00) "Were RNNs All We Needed?", z6qmomJW91 (4.00), dALYqPm9gW (4.75) — middle band; WARP is comparable to or stronger than most of these in architectural novelty and breadth.
- GRMfXcAAFh (8.00) "LinOSS", PdaPky8MUn (8.00), 8zJRon6k5v (8.00), tyEyYT267x (8.00) — strong band; WARP is clearly weaker, lacking theoretical depth and rigorous evaluation.

Round 2 narrowing (bracket 5-7):
- vcJiPLeC48 (6.00) "Gradient-free training of RNNs" — WARP is comparable in novelty but has broader experiments.
- XoYdD3m0mv (6.00) "ProbeGen" — Both address weight-space learning; WARP is more ambitious in scope and has more diverse empirical results.
- wMXH8tTQE3 (6.00), Dxl0EuFjlf (6.00), lfPkGWXLLf (6.67) — benchmark/toolkit papers, not directly comparable.

The paper is stronger architecturally than the 5.00-6.00 anchors but has evaluation weaknesses and rhetorical overclaiming that keep it below the 7.5+ tier. It sits close to the 6.00 anchors (ProbeGen, Gradient-free RNNs) but with more breadth and a genuinely more novel core idea, offset by inflated claims. Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>