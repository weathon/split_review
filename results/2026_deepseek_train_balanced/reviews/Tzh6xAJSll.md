## Summary

This paper derives precise, provable scaling laws for outer-product associative memories under Zipf-distributed discrete data with random embeddings. It establishes tight upper and lower bounds (Theorem 1), joint scaling in data size \(T\) and model dimension \(d\) (\(\mathcal{E} \asymp d^{-\alpha+1} + T^{-1+1/\alpha}\), Proposition 4), and proves minimax optimality of a thresholded storage scheme (Theorem 2). The paper then provides a heuristic analysis linking these theoretical storage schemes to SGD, Adam, and LayerNorm, connecting optimization hyperparameters to learned association weights.

## Strengths

- **Tight joint scaling laws with matching minimax lower bound.** Proposition 4 derives the joint scaling \(\mathcal{E} \asymp T^{-1+1/\alpha} + d^{-\alpha+1}\) for the thresholding scheme, and Theorem 2 proves this rate is minimax optimal (up to log factors) over all weighting schemes. Figure 1 validates the predicted exponents empirically. This goes beyond prior work (Hutter 2021, Michaud et al. 2023) which handles only one error source, and provides a *proof* of optimality.

- **Mechanistic signal-to-noise characterization with matching lower bound.** Theorem 1 provides both an upper bound and a matching lower bound that decompose the generalization error into a signal term \(d\,q(x)^2\) versus interference \(Q_\infty = \max_y\sum_{x:f_*(x)=y} q(x)^2\). This explains *why* thresholding helps (it keeps \(Q_\infty\) small) and why uniform weighting outperforms frequency weighting — insight absent from purely empirical scaling-law studies.

- **Analytical bridge from SGD hyperparameters to memory weighting schemes.** Equation (16) derives \(q_\gamma(x) \approx f^{Tp(x)}(0)\) where the iterated map \(f\) depends explicitly on learning rate \(\gamma\), connecting step size and batch size to the theoretical weighting schemes \(q_\rho\) from the earlier analysis. Figures 5–6 validate this approximation, opening the black box connecting optimization to stored association weights.

## Weaknesses

### Major

None. The paper's core theoretical contributions (Theorems 1–2, Propositions 1–4) are sound, well-proven, and correctly scoped.

### Minor

- **The optimization analysis (§4) is heuristic and not on equal rigor footing with §3.** The derivation of the SGD weighting approximation (Eq. 16) relies on several uncontrolled approximations (concentration of \(\epsilon\), assumption that \(p_W(z|x)\) barely changes for \(z\neq f_*(x)\), approximate independence across tokens). The paper openly acknowledges when the approximation breaks down (\(d < N\), line 409), and the sections on Adam and LayerNorm are explicitly conjectural ("We conjecture that this introduces a clipping effect..."). This is not a flaw — the section is exploratory — but the presentation in §4 occasionally uses the same formal notation as the rigorous §3, which could give readers the impression that the SGD results are on equal theoretical footing. A clearer demarcation would help.

- **The transformer-motivation framing is slightly broader than what the model can directly support.** The paper repeatedly frames the associative memory as "a proxy for the inner layers of transformers" (abstract, §1, §2, §4) and concludes by calling it "a simple model to study memorization in transformers." The model makes several simplifications — deterministic labels \(y=f_*(x)\), random fixed embeddings, a single linear layer, argmax decoding — and the paper never compares its predicted exponents to empirically observed LLM scaling laws. The cited evidence (Bietti et al. 2023) does support a connection, and the paper is transparent about the simplifications, so this is not a fatal overclaim. But the framing could be more precisely scoped: the paper studies *one hypothesized component* of transformer layers, not "memorization in transformers" broadly. A sentence clarifying what the model can and cannot explain about actual LLM scaling would strengthen the paper.

- **The learned-embedding section (§4.2) partially undercuts the main random-embedding narrative without fully resolving the tension.** The paper shows (Figure 8, Eq. 17) that with learned embeddings, the capacity bottleneck vanishes entirely ("it is actually possible to store as many memories as desired"). The paper offers a brief justification (embeddings are shared across heads, so the idealized solution is unrealistic), but this receives only a single sentence. Given that real transformers learn their embeddings, a more thorough discussion of why the random-embedding analysis is nevertheless relevant (e.g., early-training dynamics, initialization, a lower bound that learned embeddings improve upon) would strengthen the paper's framing.

- **No sensitivity analysis for the Zipf exponent \(\alpha\).** The empirical validation focuses on \(\alpha=2\) (and briefly \(\alpha=0.5\) in Figure 3). For natural language \(\alpha\) is typically closer to 1, which would change the predicted exponents. Showing validation for \(\alpha \in \{1, 1.5, 2.5\}\) would strengthen confidence that the theory holds broadly rather than only at the specific value chosen.

### Trivial

- The paper could more explicitly note that the deterministic-label assumption (\(y=f_*(x)\)) implies zero Bayes error, which would change the \(T\)-scaling in a noisy setting (adding an irreducible error floor).

## Nice-to-Haves

- A brief discussion comparing the predicted exponents (e.g., \(d^{-1}\) when \(\alpha=2\)) to empirically observed LLM scaling exponents would help readers calibrate relevance.
- A comparison of error rates or capacity to modern Hopfield networks or other associative memory architectures would position the contribution more clearly.

## Removed Points

The following points from the input reviews are excluded under the filtering rules:

- *"Experimental validation is confined to tiny synthetic setting (N=100, M=5, d up to ~100)"* — For a primarily theoretical paper, small-scale synthetic validation of derived rates is standard and appropriate. The theory itself makes predictions about scaling; the experiments confirm the rates, not the practical applicability. Removed.
- *"No comparison to observed LLM scaling laws"* — The paper does not claim to have derived LLM scaling laws; it derives scaling laws for associative memories that are *motivated by* but not claimed to *explain* LLM behavior. This is a nice-to-have, not a weakness. Removed.
- *"Missing comparison to other associative memory models"* — The paper cites Hopfield networks and modern Hopfield networks. A comprehensive comparison is beyond the paper's stated scope. Removed.
- *"No discussion of the impact of the deterministic-label assumption"* — The paper explicitly states this assumption (line 50) and the minimax lower bound (Theorem 2) accounts for the worst-case conditional distribution. Removed as already addressed.
- Strength finder's claim about "Theoretical analysis of practical transformer components (Adam, LayerNorm)" being a core strength — The paper's own hedging language ("We conjecture...," "Arguably...") indicates this is exploratory, not a rigorous contribution. Demoted from strength to supporting observation.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely recapitulate the paper's results rather than adding interpretive synthesis.

## Suggestions

1. Add one or two clarifying sentences early in the paper (e.g., after Eq. 3) that the model studies *one component hypothesized to operate in transformer layers* rather than "memorization in transformers" generally.
2. Explicitly label §4 as "Heuristic analysis" or "Exploratory analysis" in the section header or first paragraph to distinguish it from the rigorous results of §3.
3. Expand the discussion in §4.2 of why the random-embedding analysis remains relevant despite learned embeddings potentially avoiding capacity limits. Even 2–3 sentences on initialization dynamics or the shared-embedding constraint would help.

## Score and Decision

This is a solid theoretical paper with precise, proven scaling laws, tight bounds, and a minimax optimality result — contributions that meet the ICLR bar. The optimization analysis is exploratory but interesting, and the transformer framing, while slightly ambitious, is supported by citations and caveats. The weaknesses are minor and addressable.

**MY FINAL SCORE: <score>7.5</score>**
**MY FINAL DECISION: <decision>Accept</decision>**