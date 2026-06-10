## Summary

This paper proposes a Model Predictive Control (MPC) framework for training deep neural networks, casting Back-Propagation (BP) and the Forward-Forward (FF) algorithm as special cases corresponding to full horizon (h=T) and minimal horizon (h=1), respectively. The paper provides a theoretical analysis of gradient quality as a function of truncation horizon for deep linear networks (Theorem 3.4, showing cubic convergence of gradient alignment as h→T), derives that the optimal horizon lies strictly between the two extremes under a linear cost objective, and proposes a polynomial-fitting-based horizon selection algorithm. The extracted text ends during the description of this algorithm; the promised experimental validation (Section 5) and conclusion (Section 6) are not present in the parser output.

## Strengths

- **Theorem 3.4 provides a non-trivial, quantitative characterization of gradient quality vs. horizon.** The cubic bound \(1-\cos^2(\theta_h)=O((1-h/T)^3)\) as \(h/T\to 1\) is a concrete theoretical result that goes beyond qualitative statements about truncated backprop. For deep linear networks with whitened data and near-identity initialization, the rate is precise and non-obvious.

- **The optimal-horizon derivation demonstrates that neither endpoint is optimal under a linear cost objective.** From the cubic bound and a linear memory cost \(M(h)=ah+b\), the paper derives a closed-form optimal horizon \(h^* = T(1-\sqrt{a\lambda/(3c)})\) that lies strictly between 1 and \(T\) (Section 3.3, lines 190–192). This gives a formal basis for the intuition that intermediate horizons offer a better trade-off than either extreme.

- **The trajectory-loss construction \(l(t,x(t),u(t)) = L(x(t+1))-L(x(t))\) is an elegant device** that transforms a terminal loss into a telescoping sum of local losses, enabling the MPC formulation without modifying the original loss function (Eq. 8, line 118). This is a clean design choice that makes the framework directly applicable.

## Weaknesses

### Major

- **The paper misrepresents the Forward-Forward algorithm, overstating its unification claim.** The paper defines \(g_{\mathrm{FF}}(u(t)) = \nabla_{u(t)} L(x(t+1))\) (line 75) and states this is the FF algorithm "using a more general form of the loss function" (line 78). This is incorrect: Hinton's FF (2022) uses a *local contrastive objective* (e.g., squared Euclidean norm of activations compared against a threshold, trained on positive vs. negative data) that is fundamentally different from evaluating the terminal loss \(L\) at the next layer's output. What the paper actually implements at \(h=1\) is truncated backpropagation through one layer — a well-known technique in the truncated BPTT literature, not the Forward-Forward algorithm. The paper's title ("Unifying Back-Propagation and Forward-Forward Algorithms") and framing (Figure 1, line 134) claim unification of two specific algorithms, but the paper instead unifies BP with *truncated backprop*, where \(h=1\) is a degenerate case. This is an overclaim that affects the paper's core positioning. The connection to local-loss methods cited in Remark 3.1 (Nøkland & Eidnes, 2019; Belilovsky et al., 2019) is more defensible, but the direct equation of FF with \(h=1\) in the MPC framework is inaccurate.

- **The optimal-horizon derivation relies on the untested assumption that the cubic bound holds globally.** Theorem 3.4 is proved only for deep *linear* networks with whitened data, weights near identity \((W(t)=I+\frac{1}{T}\tilde{W}(t))\), and in the asymptotic limit \(h/T\to 1\). The derivation of the optimal horizon (line 190) *assumes* \(\cos^2(\theta_h)=1-c(1-h/T)^3\) as if it holds for all \(h\), but Theorem 3.4 only guarantees this behavior as \(h/T\to 1\). The paper claims "the qualitative conclusions carry over to general networks" (abstract) and notes "the polynomial relationship is also observed for nonlinear cases (refer to Section 5.1)" (line 182) — but Section 5.1 is not present in the extracted text, so this crucial empirical support cannot be verified. The optimal horizon formula is predicated on an extrapolation of an asymptotic bound that is unverified outside the linear regime.

### Minor

- **The horizon selection algorithm requires the very computation it aims to avoid.** To fit the polynomial for \(\cos(\theta_h)\), the algorithm must compute both \(g_h\) and \(g_T\) (full backprop gradient) for a set of horizons \(H\) (lines 198–202). Computing \(g_T\) requires storing all intermediate activations — the same memory cost the method is designed to reduce. While this could be framed as a one-time calibration step on a few batches, the paper does not discuss this limitation, and it weakens the practical motivation: if full backprop is affordable even for a few batches, the marginal benefit of switching to shorter horizons for the bulk of training needs justification.

- **The theoretical analysis covers only the \(h/T\to 1\) regime.** Theorem 3.4 does not characterize gradient quality for small \(h\) (near the FF/\(h=1\) extreme), where the interesting trade-off between memory and accuracy is most consequential. The paper defers to "numerical experiments" (line 188) for behavior near \(h=1\), but these are not available in the extracted text. The theory thus provides guidance primarily about when *large* horizons are good enough, not about when *small* horizons are adequate.

- **The MPC framing is primarily terminological for the algorithmic content.** The core method (truncated backprop with variable horizon) is well-established in the truncated BPTT literature (Aicher et al., 2019, cited by the paper). The MPC lens reorganizes this known technique into a new vocabulary (horizon, trajectory loss, receding horizon) without introducing algorithmic novelty in the optimization procedure itself — the novelty lies in the *analysis* (Theorem 3.4) and the *horizon selection algorithm*, not in the training procedure.

### Trivial

- The extracted text contains several garbled symbols and broken equation fragments (e.g., lines 56, 62, 121, 149, 190) — these are parser artifacts and do not reflect the original submission.

## Nice-to-Haves

- The relationship between \(r(h)\) and \(\cos^2(\theta_h)\) (Eq. 14, line 185) is stated without derivation. A brief justification connecting gradient alignment to loss convergence (e.g., via the gradient descent update structure) would strengthen the theory-practice link.
- The algorithm description (Section 4) would benefit from specifying how many batches and how many horizons \(H\) are needed for robust polynomial fitting, and how measurements are aggregated across batches and parameter states.

## Novel Insights

The cubic convergence rate — that gradient alignment improves as \((1-h/T)^3\) rather than linearly — is a non-trivial finding from the linear-network analysis. If this rate holds approximately in nonlinear settings (which the missing experiments would show), it has a concrete practical implication: the marginal benefit of increasing horizon shrinks rapidly near full backprop, and the "sweet spot" is quantifiable. This is a genuinely useful insight beyond the existing qualitative understanding that truncated gradients are "good enough" at some horizon.

## Suggestions

1. **Reposition the contribution honestly.** Drop the claim of unifying "FF algorithms" specifically; instead present the framework as unifying global (BP) and local-loss training through a variable-horizon truncation perspective. The actual FF algorithm can be cited as an example of an \(h=1\) local-loss method, but should not be equated with \(\nabla_{u(t)}L(x(t+1))\). The paper would benefit from an explicit statement: "Our \(h=1\) case corresponds to truncated backprop with one layer, which is related to but distinct from Hinton's FF algorithm."
2. **Acknowledge the calibration cost of the horizon selection algorithm** and discuss when it is still worthwhile (e.g., rare calibration vs. repeated training).
3. **Add a non-asymptotic bound or simulation** for the gradient quality at finite \(h\) and \(T\) to complement the asymptotic result, even if only for the linear case.
4. **Provide the missing experimental section** so that the empirical claims about the algorithm's effectiveness on nonlinear models and various tasks can be evaluated.

## Removed Points

These were flagged by the reviewers but removed or demoted after cross-checking against the paper:

- **"The experimental section is entirely absent from the submitted text"** (from Harsh Critic) — The paper references Section 5.1 internally (lines 182, 188), indicating experiments exist in the original submission. Missing sections in the parser output are a known extraction artifact, not an author omission.
- **"Missing proofs in appendix"** — The instructions note that appendices are routinely stripped by the parser.
- **"The MPC framework reduces to... truncated backpropagation"** (Harsh Critic on novelty) — While the MPC framing is interpretive, the paper's contribution includes the theoretical rate analysis (Theorem 3.4) and horizon selection algorithm, which go beyond "just truncated backprop." Retained as minor rather than fatal.
- **"The relationship between r(h) and cos²(θ_h) is asserted but not derived"** — The paper cites this as an empirical observation (line 182–185, referencing Section 5.1), which is standard for empirical relationships; a full derivation is not essential.
- **"Baselines are not discussed"** — Baseline discussion would naturally appear in the missing experiments section.
- **Various formatting/style nitpicks** — Parser artifacts, not author errors.

## Score and Decision

**MY FINAL SCORE: <score>3.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**