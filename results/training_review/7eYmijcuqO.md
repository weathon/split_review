Now I have thoroughly verified the claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces timed automata (TA) as a controllable task family for studying how RNNs develop internal representations of time, and provides a dynamical-systems analysis of the learning process. For a periodic "time-of-day" temporal flipflop, the authors show that RNNs learn stable periodic cycles around unstable fixed points that encode time modulo the period, and that the phase transition in time-dependent accuracy coincides with a bifurcation (|λ_max| crossing 1). They extend the analysis to a relative-timing TA, where the network instead learns multiple stable fixed points that support a counting mechanism. A retraining experiment and an accompanying oscillator model help explain why periodic orbits transiently destabilize when the period changes.

---

## Strengths

- **Novel and well-motivated task framework.** The TA-based tasks give direct control over the complexity of time-awareness required, enabling systematic study of how RNNs discover hidden temporal structure. This cleanly extends prior work on neural-network automata emulation (Pollack, 1991; Sussillo & Barak, 2013) to time-dependent behavior, filling a clear gap in the literature (Section 2).

- **Empirical demonstration of periodic orbit encoding.** The paper shows that trained RNNs use a 2D subspace (spanned by real/imaginary parts of the eigenvector of the top eigenvalue of W_hh) to represent time modulo period P, forming rings around unstable fixed points. The projection experiment (TD accuracy 99.43% → 99.45%) confirms this subspace carries nearly all temporal information (Section 3.2). This is a clean, concrete result.

- **First empirical link between a training bifurcation and a phase transition.** Tracking |λ_max| at fixed points throughout training reveals that the plateau in time-dependent accuracy ends precisely when |λ_max| crosses 1 and stable periodic orbits emerge (Figure 4b–c). This connects long-standing hypotheses about bifurcations and gradient pathologies (Doya, 1993; Pascanu et al., 2013) to observed learning dynamics in trained RNNs, and the paper appropriately differentiates from related work by Ribeiro et al. (2020) (Section 3.3).

- **Clever retraining experiment.** The shift from period P₁=24 to P₂=12, with the resulting loss and regain of stability, strengthens the causal story. The companion oscillator model provides an intuitive explanation for why periodic orbits transiently destabilize, with the loss-landscape analysis showing an additional ruggedness beyond simple vanishing gradients (Section 3.4, Figure 5).

- **Extension to a different temporal regime.** The relative-timing TA analysis shows that despite the same three-phase learning structure, the network uses qualitatively different dynamics (stable fixed points rather than periodic orbits), demonstrating the versatility of the framework (Section 4).

---

## Weaknesses

### Fatal
None.

### Major

- **Missing training hyperparameters preclude independent reproduction.** The paper specifies only "stochastic gradient descent" (line 44) and hidden size N_h=64 (line 68). No learning rate, momentum, batch size, sequence length, number of training examples/epochs, initialization scheme, or learning rate schedule is reported. These omissions are significant because the dynamical phenomena (plateau duration, bifurcation timing) are likely sensitive to optimization hyperparameters. Without these details, the experiments cannot be reproduced or meaningfully compared with future work.

- **The "distinct from grokking" claim is unsupported by the data shown.** The paper states the phase transition is distinct from grokking because "train and test sets improve simultaneously" (line 77), but Figure 2 only shows "learning curves" without specifying whether these are train or test accuracy, and no test curves are presented. The reader cannot verify this claim, which is used to frame a key contribution.

### Minor

- **Statistical rigor is uneven.** While Figure 2 shows trajectories for 30 seeds and the projection experiment reports mean±std, the core dynamical analyses (Figures 3–4, bifurcation timing, the relative-timing fixed-point emergence) lack multi-seed summary statistics. The paper reports that the bifurcation coincides with the phase transition, but provides no distribution of the iteration at which |λ_max| crosses 1, no correlation measure, and no error bars on the plateau duration. The claim of "quantitative evidence" (line 118) would be stronger with these statistics.

- **Relative-timing mechanism validation is qualitative.** The central hypothesis — that distance from null-symbol fixed points encodes elapsed time since the last non-null symbol — is supported by a 2D projection (Figure 7) but never quantitatively validated. There is no plot of hidden-state distance vs. elapsed timesteps, no demonstration of monotonicity or linearity, and no assessment of whether this mechanism is consistent across seeds. The 2D projection axes (first PC of input weights; logistic regression coefficients) are described but not validated to correspond cleanly to "state" and "time."

- **The oscillator model's connection to RNN gradients is suggestive, not evidential.** The model (Section 3.4) uses continuous gradient flow on a complex exponential, whereas the RNN uses discrete stochastic gradient descent with hidden-state recurrence and input-driven dynamics. The paper appropriately hedges ("this simple model suggests," line 135) and calls the relationship "analogous" (line 131), but never measures gradient norms or direction in the actual RNN to confirm the predicted behavior. This limits the strength of the explanatory claim.

- **Fixed-point detection methodology is underspecified.** The paper uses the Sussillo & Barak (2013) algorithm but does not discuss convergence criteria, the number of candidate states optimized, or sensitivity analysis for false positives/negatives. This is nontrivial for 64-dimensional hidden states, and the reliability of the stability plots depends on accurate fixed-point identification.

### Trivial

- The eigenvector dimensionality concern raised by one reviewer is already correctly addressed in the paper: "This eigenvalue was complex, and the real and imaginary parts of the associated eigenvector span a 2D space" (line 97).
- The paper does differentiate itself from Ribeiro et al. (2020) at line 118, contrary to what one review suggested.

---

## Nice-to-Haves

- A quantitative plot of hidden-state distance from null-symbol fixed points vs. elapsed timesteps (for the relative-timing TA) would concretely validate the hypothesized counting mechanism.
- Gradient norm measurements (e.g., ∂L/∂W_hh) during the plateau could connect the oscillator model to actual RNN dynamics.
- Showing both train and test curves in Figure 2 would cleanly resolve the grokking comparison.
- Varying the period P systematically and reporting plateau duration vs. P would further test the oscillator model's predictions.
- Extending the analysis to LSTMs/GRUs would test architecture generality, but this is explicitly scoped beyond the current paper.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Eigenvector dimensionality" criticism** — The critic claimed a single eigenvector spans only 1D, but the paper correctly notes the eigenvalue is complex and its real/imaginary parts span a 2D subspace. Factually wrong; removed.
- **"Does not differentiate from Ribeiro et al. (2020)"** — The paper explicitly states at line 118: "A similar bifurcation is observed by Ribeiro et al. (2020)... though they do not report a connection between the loss and the bifurcation." Already addressed; removed.
- **"Section 2.1 needs concrete formula for null vs. non-null probability"** — The paper gives the conceptual setup ("higher probability of receiving the null symbol to ensure Prob(Θ=0)≈Prob(Θ=1)"), which is sufficient for the paper's purposes. Scope creep; removed.
- **"TD/TI accuracy justification is missing"** — The paper clearly defines TD accuracy as accuracy on Symbol-a timesteps (the time-dependent symbol) and TI accuracy on Symbol-b timesteps. This is directly tied to the task definition; removed.
- **"Figure 6 panel (c) not clearly labeled"** — Likely a PDF extraction artifact; removed.
- **Multiple formatting/style nitpicks** about phrasing, presentation, and "missing parts" that amount to expanded-scope requests rather than paper flaws — these reflect the reviewer's wishlist rather than problems with the paper as scoped; moved here.

---

## Novel Insights

The most interesting insight to emerge across the reviews is that the same three-phase learning structure (learn TI behavior → plateau → rapid discovery of TD behavior) arises for two mechanistically different temporal tasks (periodic and relative-timing), yet the *dynamical mechanism* for representing time is fundamentally different — periodic orbits in one case, stable fixed points in the other. This suggests that the learning dynamics (plateau → phase transition) are driven by a common optimization difficulty related to discovering hidden temporal variables, while the *encoding* of those variables adapts to the structure of the temporal dependence. The oscillator model adds the novel suggestion that there is a ruggedness in the loss landscape specific to periodic tasks that goes beyond standard vanishing gradients — a point that, while not yet empirically validated in the RNN, opens a concrete direction for future work on training dynamics for temporally-structured tasks.

---

## Suggestions

1. **Add training hyperparameters.** Report learning rate, optimizer (with any momentum/decay), batch size, sequence length, dataset size (number of training sequences), and total training iterations/epochs. This is the single highest-impact change for the paper's long-term value.

2. **Clarify what Figure 2 shows.** State explicitly whether the plotted curves are train accuracy, test accuracy, or both. If only train accuracy is shown, add test accuracy curves or state that they are visually indistinguishable from train curves (and provide evidence).

3. **Add multi-seed summary statistics for the bifurcation analysis.** Report mean ± std (or median and range) for: (a) the iteration at which |λ_max| crosses 1, (b) the plateau duration, and (c) the TD accuracy at the bifurcation point. A scatter plot showing the correlation across seeds would significantly strengthen the causal claim.

4. **Quantitatively validate the relative-timing mechanism.** Add a simple plot: for a fixed input pattern (e.g., a, φ, ..., φ, b), compute the Euclidean distance from the hidden state at each null timestep to the nearest null-symbol fixed point, and show this distance decreasing monotonically over τ steps. This one plot would substantially elevate the relative-timing analysis.

5. **Report convergence criteria for fixed-point detection.** Even a brief statement (e.g., "we optimized 1000 candidate states per input and accepted fixed points with ||F(h,u)−h|| < 10⁻⁵") would address a legitimate methodological concern.

---

## Score and Decision

The paper introduces a genuinely novel and well-motivated framework (TA-based tasks for studying temporal representations), presents interesting dynamical phenomena (periodic orbit encoding, bifurcation-driven phase transitions), and provides a clever retraining experiment. The main weaknesses are (1) missing training hyperparameters that hamper reproducibility, (2) uneven statistical rigor (one multi-seed figure but no summary statistics for the core bifurcation claim), and (3) a few analysis gaps (no test curves for the grokking comparison, qualitative relative-timing validation). None of these are fatal — they are all addressable in revision. The paper's contributions are significant enough to warrant acceptance provided the reproducibility issues are resolved.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>