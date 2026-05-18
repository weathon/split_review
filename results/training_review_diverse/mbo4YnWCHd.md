Now I have all the evidence I need to write the consolidated review. Let me finalize.

---

## Summary

This paper proposes an EM-based unified framework for non-negative tensor decomposition optimizing KL divergence, covering CP, Tucker, and Tensor Train decompositions, their mixtures, and adaptive noise modeling. The key technical insight is connecting low-rank decomposition to many-body approximation, which yields exact closed-form updates in the M-step for Tucker and Train, eliminating iterative gradient methods and learning rate tuning. Experiments on eight real-world categorical datasets show competitive generalization against tensor-based baselines (MPS, BM, LPS).

## Strengths

- **Unified EM framework across diverse low-rank structures**: The paper derives a single EM formulation where the M-step decouples into independent many-body approximations, each solvable in closed form via Equations (6) and (7). This handles CP, Tucker, Train, tree-structured combinations (Section 3.4), and mixtures with noise (Section 3.5) without piecemeal gradient-based solvers. This is a genuine contribution to the non-negative tensor decomposition literature.

- **Closed-form M-step eliminates gradient tuning**: By connecting low-rank decomposition to many-body approximation, the paper derives exact closed-form updates for Tucker (Eq. 6) and Train (Eq. 7) factor tensors. The framework does not require a learning rate, unlike the MPS/BM/LPS baselines which need careful tuning. This is a concrete and demonstrable practical advantage.

- **Consistent generalization on discrete density estimation**: CPTrainON (mixture of CP + Train with noise and mode reordering) achieves the best or near-best test cross-entropy on 7 of 8 datasets compared to tensor-based baselines. The paper also shows that the mixture of CP and Train combines the strengths of both decompositions.

- **Linear-in-\(N\) complexity via sparsity**: Section 3.2 derives \(O(\gamma D N R^2)\) for EM-Train using cumulative-core computations, exploiting sparsity of the empirical tensor. All methods scale linearly in the number of nonzero elements \(N\).

- **Convergence guarantee**: The EM formulation ensures monotonic increase of the objective at each iteration regardless of the chosen low-rank structure — a property not shared by gradient-based approximations.

- **Adaptive noise term for robustness**: The learnable uniform noise component provides protection against overfitting when models are specified with large numbers of parameters, without requiring a separate hyperparameter.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Closed-form M-step novelty is overstated**: The closed-form solutions in Equations (6) and (7) are a natural consequence of standard EM theory for exponential-family models — when the complete-data distribution is a log-linear model, the M-step reduces to computing expected sufficient statistics, which here are normalized marginals of \(\mathcal{M}\) over the relevant indices. The paper's real contribution is recognizing that this connection exists for Tucker and Train decompositions and can be operationalized within a unified framework, not discovering fundamentally new optimization principles. The framing as a novel theoretical result (Theorems in supplementary) is slightly overblown. This does not invalidate the paper but should be acknowledged more honestly.

- **Initialization sensitivity is unexamined**: The paper reports results over 10 random initializations but provides no analysis of variance, range of outcomes, or description of how initializations were generated. EM is known to be sensitive to initialization, especially for mixtures. Without discussing whether performance is robust across initializations or whether some initializations lead to poor local optima, the reliability claim is somewhat hollow. A brief analysis (e.g., min/max range or standard deviation of test cross-entropy) would strengthen the paper.

### Trivial

- **Adaptive noise term is additive smoothing**: The noise term is equivalent to a uniform Dirichlet prior / additive smoothing. The paper presents it as a novel feature, but it is straightforward and its practical benefit is marginal (as the paper itself notes). The value is that the mixing weight can be learned automatically, which is convenient but not novel.

- **Mode reordering heuristic's effectiveness is relegated to supplementary**: The mutual-information-based mode reordering is a reasonable engineering heuristic, but its effectiveness is only discussed in the supplementary material. Including a brief demonstration (or at least a summary sentence about observed gains) in the main text would strengthen the argument for the Train variant.

- **No runtime or convergence speed comparison**: The paper argues that avoiding gradient methods in the M-step is advantageous, but provides no wall-clock time or convergence-iteration comparison against MPS/BM/LPS. A plot of objective vs. runtime would make the practical advantage concrete and is standard for such claims.

## Nice-to-Haves

- A runtime or convergence-speed comparison (objective vs. wall-clock time) against gradient-based baselines would make the practical advantage of closed-form M-steps tangible.
- Demonstrating the method on a higher-dimensional dataset (\(D > 10\), e.g., from UCI or NLP) would better support the scalability claims, especially for the Train variant where the \(O(\gamma D N R^2)\) complexity is most attractive.
- A brief summary of the mode reordering heuristic's impact (even one sentence reporting the improvement observed) in the main text would be helpful.

## Removed Points

These points were flagged but removed after verifying against the paper; they are listed for transparency:

1. **"Empirical claims unverifiable from main text"** — The table `\input{tables/experiment}` and figure `\includegraphics{figs/fig_all.pdf}` are LaTeX commands that the text parser could not expand. This is a parser-level formatting artifact, not an author error. The paper provides textual summary of results (lines 242–243, 252). Per hard rules, remove criticisms about formatting artifacts.

2. **"Narrow experimental scope (demanding non-tensor baselines)"** — The abstract explicitly states "compared to conventional tensor-based approaches" and the paper compares against three tensor baselines (MPS, BM, LPS). Demanding comparisons to naive Bayes, MADE, smoothed empirical distributions, or other non-tensor methods is scope creep. The paper is about tensor decomposition methodology; evaluating against other tensor methods is appropriate.

3. **"Linear complexity claim is misleading"** — The paper states "linear computational complexity relative to the number of nonzero elements." The complexity expressions given are: CP \(O(\gamma N D R)\), Tucker \(O(\gamma D N R^D)\), Train \(O(\gamma D N R^2)\). All are \(O(N)\) — linear in the number of nonzero elements. The claim is accurate for all three methods. The reviewer's assertion that "this holds only for CP" is factually incorrect.

4. **"No learning rate claim is problematic"** — The paper accurately states the framework does not require a learning rate *in the M-step* because the closed-form updates replace gradient descent. EM iteration and initialization are standard and unrelated to learning rate tuning. The claim is correct as stated.

5. **"Missing related work on broader NTF literature"** — Per hard rules, do not mention missing related works.

6. **"Simple baselines needed"** — See point 2; this is scope creep.

## Novel Insights

The most interesting observation emerging from the reviews is the recognition that the paper's "theoretical novelty" and its "practical value" are somewhat decoupled. The closed-form M-steps are theoretically straightforward (normalized marginals under exponential-family EM), but the practical value of *recognizing* that Tucker and Train decompositions admit this structure and can be combined in mixtures without separate gradient solvers is substantial. The paper's real contribution is architectural unification, not theoretical depth — and the reviews suggest the paper would be stronger if it leaned into this framing rather than claiming "novel theorems."

## Suggestions

1. Reframe the closed-form M-step contribution: acknowledge it follows from exponential-family EM theory, but emphasize that recognizing and operationalizing this connection for Tucker and Train is the contribution.
2. Add a brief analysis of initialization sensitivity (e.g., range of test cross-entropy across 10 runs, or a note on the initialization scheme used).
3. Include a runtime comparison (wall-clock time or iterations to convergence) against MPS/BM/LPS to substantiate the practical advantage.
4. Provide a 1–2 sentence summary of the mode reordering heuristic's empirical impact in the main text.
5. Be precise in the abstract: instead of "linear computational complexity" (which is accurate but could be read too broadly), say "computational complexity linear in the number of observations" — this is less ambiguous.

## Score and Decision

The paper presents a well-motivated, technically sound, and genuinely useful unification of non-negative tensor decomposition methods. The experimental evaluation is appropriate for a methodology paper in this area. Weaknesses are minor — the chief one being a slight overstatement of theoretical novelty and a missing analysis of initialization sensitivity. The core contribution is solid and the framework has clear practical value.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>