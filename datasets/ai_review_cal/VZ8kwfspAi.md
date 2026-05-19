- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5, 3, 5, 3
Now I have all the information needed. Let me compose the final consolidated review.

## Summary
This paper proposes the Spacetime $E(n)$-Transformer (SET), an architecture that extends $E(n)$-equivariant graph convolutions (EGNN) with temporal self-attention mechanisms for spatio-temporal graph modeling. The method is evaluated on the charged $N$-body problem, predicting positions and velocities $H$ steps ahead from $L$ observed time steps. The core idea is to preserve rotation, translation, and permutation equivariance in both the spatial and temporal dimensions.

## Strengths
- **Ablation study cleanly demonstrates that $E(n)$-equivariance provides a measurable benefit**: Table 1 directly compares Equiv=True (test MSE 1.25e‑10) vs Equiv=False (2.03e‑10) while keeping all other components fixed. The 1.57× ratio is the cleanest evidence that the equivariance inductive bias improves performance.
- **Parameter count does not grow with the number of particles $N$**: Figure 2 (bottom) and the accompanying text confirm that SET's parameter count stays constant as $N$ increases from 5 to 30, unlike the LSTM baseline which grows from 8.2e5 to 1.8e6. This is achieved by sharing EGCL weights across time steps and having attention depend only on feature/coordinate dimensions — a practical advantage over many temporal graph networks.
- **Concise identification of a design failure**: The ablation shows that temporal attention for the adjacency matrix (Adj=True) worsens performance (ratio 8.96×). The paper provides a reasoned explanation: edge attributes contain time-invariant charges and distances already encoded in coordinates. This self-critical analysis strengthens credibility.

## Weaknesses

### Major
- **Velocity attention formula (Eq. 8) is mathematically inconsistent as written**: The weight $\gamma_i(t,s)$ is defined as $\frac{\omegab_i(t)^\top \omegab_i(s)}{\sum_{s'=1}^L \exp(\omegab_i(t)^\top \omegab_i(s'))}$. The numerator uses a raw dot product (which can be negative) while the denominator uses exponentials. This is not a standard attention distribution — the weights need not be non-negative and do not sum to one. Even if this is a typographical error (missing $\exp$ in the numerator), the formula as presented cannot be implemented as-is. This is a core component of the claimed contribution.
- **Temporal attention for adjacency matrices (Eqs. 10–11) is underspecified**: $K(t)=KA(t)$, $Q(t)=QA(t)$ with $K,Q\in\mathbb{R}^{N\times N}$ yield $Q(t)^\top K(s)\in\mathbb{R}^{N\times N}$, yet $\pi(t,s)$ appears intended as a scalar attention weight (weighting $V(s)\in\mathbb{R}^{N\times N}$). The notation conflates element-wise and matrix operations, and it is unclear how the attention mechanism produces a scalar weight from matrix-valued keys and queries. This component is not reproducible from the description.
- **The EGNN baseline is not adequately described**: The paper reports that the EGNN (the spatial backbone of SET) achieves test MSE 2.05e‑6 — four orders of magnitude worse than SET (1.25e‑10). However, it does not specify how EGNN is applied to the sequential prediction task (e.g., single-step autoregressive, learned temporal aggregation, or mean pooling). Without this information, the comparison is uninformative. Moreover, the EGNN baseline has 100k parameters vs SET's 796k, so the comparison conflates architectural differences with equivariance benefits.
- **No variance estimates or multiple runs reported**: Every numerical result in the paper appears to come from a single run. Given the orders-of-magnitude gaps between methods and the suspiciously low MSE values (1.25e‑10 for predicting 10,000 steps ahead from 10 observations), statistical grounding is essential to establish reliability.

### Minor
- **Inconsistency between EGNN baseline and equivariance ablation**: Removing equivariance from SET (Equiv=False) increases MSE by only 1.57× (2.03e‑10), yet the EGNN baseline (which is itself $E(n)$-equivariant and spatial-only) achieves 2.05e‑6 — four orders of magnitude worse. This gap suggests that factors other than equivariance (model capacity, temporal architecture, training setup) dominate the comparison. The paper does not address this inconsistency.
- **Input feature $h_i(t)=\|\mathbf{v}_i(t)\|_2$ discards directional velocity information**: Using only the norm of velocity as the node feature removes all directional information. Non-equivariant baselines (LSTM, MLP) that rely on features for direction information are disadvantaged, while SET processes coordinates separately and is less affected. This choice may inflate the performance gap.
- **Scalar $B$ in Eq. 5 (position update) is not defined**: The parameter $B$ in $\tilde{\xib}_i(t):=\xib_i(t)+B\sum_{s\ne t} \beta_i(t,s)(\xib_i(s)-\xib_i(t))$ is introduced without explanation of whether it is a learned scalar, a hyperparameter, or a fixed constant.
- **Noether's theorem framing is motivational but undeveloped**: The introduction invokes Noether's theorem to motivate temporal and spatial symmetry, but the paper never formalizes or leverages this connection. The framing may mislead about the nature of the contribution.

### Trivial
- Positional encodings $W^{[1:L]}, X^{[1:L]}, Y^{[1:L]}, Z^{[1:L]}$ are used in Algorithm 1 and Figure 1 but never explicitly defined in the text (their roles are inferable from context as positional encodings for features, coordinates, velocities, and adjacency matrices).

## Nice-to-Haves
- Comparing against a spatio-temporal baseline that uses the same spatial backbone (EGNN) with a simple temporal model (e.g., EGNN + LSTM or EGNN + mean pooling) would isolate the benefit of the Transformer temporal attention.
- Reporting results on additional dynamical systems (beyond charged $N$-body) would strengthen claims of generality.
- An equivariance proof or verification for the full SET architecture (beyond noting that composition of equivariant layers preserves equivariance) would be welcome.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *"The background definitions (Section 2) add little and could be removed"* — This is a presentation nitpick. The definitions are standard and appropriate for a self-contained paper.
- *"The $SE(3)$-Transformer paper briefly alludes to temporal integration"* criticism about scope — The paper's related work discussion is adequate.
- *"No existing spatio-temporal GNN baseline (DynGCN, DyGFormer, STGCN, TGN) is used"* — Missing related works should not be listed per instructions. However, the concern about *experimental comparison* against these methods is noted in the Nice-to-Haves above.
- *"The paper does not provide an equivariance proof for the full SET"* — The paper correctly notes that composition of equivariant layers preserves equivariance. A full formal proof would be nice but is not a weakness.
- *"Connection to Noether's theorem is misleading"* — The introduction uses Noether's theorem as high-level motivation, which is acceptable in a paper that does not formally prove conserved quantities. This is covered adequately in the Minor weaknesses section.
- *"The $E$ function's charge input $c_i$ is not defined in the algorithm"* — The charges are defined in the experimental setup (Section 5), and their use is clear from context.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the mathematical inconsistency in the velocity attention formula (Eq. 8) and the underspecified adjacency attention, but these are problems in the paper's presentation, not new insights about the approach itself. The observation that the EGNN baseline gap vs the equivariance ablation gap is inconsistent is a useful critical point that the authors should address.

## Suggestions
1. **Fix Eq. 8**: Change the numerator to $\exp(\omegab_i(t)^\top \omegab_i(s))$ (a standard softmax), or explicitly justify the current non-standard form.
2. **Clarify or remove the adjacency attention**: Either specify the attention mechanism precisely (distinguishing element-wise from matrix operations) or remove it, since the ablation shows it hurts performance.
3. **Describe the EGNN baseline setup**: Report how EGNN was adapted for sequential prediction (autoregressive? temporal aggregation?) and, ideally, add an EGNN + simple temporal model baseline to isolate the effect of the Transformer attention.
4. **Report confidence intervals**: Re-run the main experiments multiple times and report mean ± std, especially given the remarkable orders-of-magnitude gaps.
5. **Define all free parameters** (e.g., $B$ in Eq. 5) and clarify the role of positional encodings.
