Now let me write the full consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
- weakness 1 — why it matters
### Minor
- weakness 1 — why it matters
### Trivial
- weakness 1

## Nice-to-Haves
- suggestion

## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

---

Let me write it all out now.

## Summary

The paper proposes JoMA (Joint MLP/Attention dynamics), a theoretical framework that derives closed-form invariants connecting self-attention logits and MLP weights during Transformer training. By "integrating out" the attention layer, the framework predicts a novel sparse-then-dense attention pattern under nonlinear activations and qualitatively extends this to hierarchical feature learning in multilayer settings. Experiments on WikiText, OPT, and Pythia models provide partial empirical support.

## Strengths

1. **Closed-form invariants linking attention and MLP (Theorem 1, Sec. 3)**. The paper derives exact mathematical relationships between self-attention logits $\vz_m(t)$ and MLP projections $\vv_k(t)$ for linear and exp attention (and an approximate invariant for softmax attention). This is a genuinely novel theoretical contribution that extends prior work (Scan&Snap) by incorporating residual connections and MLP nonlinearity. For exp attention, the invariant $\vz_m(t) = \frac12\sum_k \vv^2_k(t) + \vc$ is clean and exact under the stated assumptions.

2. **Prediction of sparse-then-dense attention dynamics under nonlinear activations (Sec. 4, Fig. 5-6)**. The paper predicts that attention first becomes sparse (focusing on salient co-occurring tokens) then becomes denser (incorporating less salient tokens). This non-monotonic behavior goes beyond prior theoretical work that only predicted monotonic sparsification. The prediction is supported by experiments on 1-layer and multi-layer transformers trained on WikiText, and via stable rank dynamics in OPT/Pythia checkpoints.

3. **Broader token coverage than Scan&Snap (remarks after Theorem 2, Sec. 3)**. The analysis factors $\Delta_{lm} = \mathbb{E}[g_{h_k}] \Pr(l|m)$ into "token discriminancy" and "token frequency," covering the full token spectrum continuously rather than a binary distinct/common dichotomy.

4. **Testable prediction about MLP stable rank dynamics (end of Sec. 4, validated in Fig. 6)**. The paper predicts that the MLP lower layer's stable rank should first drop then rebound — a parameter-only metric confirmed across OPT-2.7B and Pythia (70M-6.9B) checkpoints. This provides an independent empirical anchor for the theory.

5. **Empirical alignment between hidden MLP nodes and latent variables (Table 1, Sec. 5)**. In synthetic hierarchical data (HBLT), hidden MLP nodes show normalized correlation 0.94–1.00 with ground-truth latents at layer 0 and 0.55–0.81 at layer 1, supporting the claim that MLP layers can learn latent hierarchical structure.

## Weaknesses

### Fatal
None.

### Major

1. **Softmax invariant relies on assumptions in tension with the paper's core narrative, with uncontrolled approximation error (Theorem 1).** The softmax case of Theorem 1 requires $\bar\vb_m$ (expected attention output) to remain constant over time — yet the paper's central claim is that attention patterns *change* (sparse-to-dense). While the paper acknowledges this as an approximation and shows empirical correlation in Fig. 1, **no numerical correlation coefficient, error bound, or stability analysis is reported.** The reader cannot assess how close the approximation actually is. For linear and exp attention the invariants are exact under the stated assumptions, but softmax attention is what real transformers use, and the gap between the theorem and the phenomenon is uncontrolled.

2. **Nonlinear dynamics derivation has a critical gap (Section 4).** Theorem 3 analyzes dynamics under *uniform attention* — effectively removing attention from the dynamics. Attention is reintroduced in Eqn. (9) via a heuristic step: $\dot{\vv} \propto (\vmu - \vv) \circ \exp(\vv^2/2)$ with a proportionality sign, where "scalar terms are omitted" without justification that they do not affect the relative convergence rates that Theorem 4 then analyzes. Furthermore, the convergence analysis (Theorem 4) depends on an exponential-of-exponential condition ($|\delta_k(t)| \ll |\delta_k(0)|\exp[-C_{jk}\exp(\mu_k^2)]$) that is not verified to hold during actual training. The central qualitative prediction (salient components converge first) is plausible and empirically supported, but **the formal derivation connecting the assumptions to this prediction is weaker than the paper's framing suggests.**

3. **Orthonormal embedding assumption is violated in all large-scale experiments.** The paper assumes $U_C^\top U_C = I$, requiring embedding dimension $d \ge M$ (vocabulary size). In all real-model experiments (OPT-2.7B: $d=2560$, $M \approx 50000$; Pythia models), this fails substantially. The Discussion invokes Johnson-Lindenstrauss to argue that near-orthogonality suffices when $d \ge 8\epsilon^{-2}\log M$, but for realistic numbers ($M=50000$, $\epsilon=0.1$) the required $d$ is $\approx 8640$, exceeding all tested models. The paper defers "additional $\epsilon$-related terms" to future work, but **the main experiments operate in a regime where these terms would be substantial, with no correction applied.**

4. **Hierarchical learning claims are largely qualitative despite being presented as a key contribution (Section 5).** Theorem 5 (HBLT) computes token co-occurrence probabilities — a static property of the data distribution, not a learning dynamics result. The actual claims about how sparse-then-dense attention enables hierarchical feature learning ("this leads to learning of high-level features," "the latent hierarchy is implicitly learned") are presented in prose without theorems, proofs, or dynamical analyses. The synthetic experiment (Table 1) shows that MLP hidden nodes correlate with latent variables after training, but **does not demonstrate that this arises *because* of the specific sparse-then-dense attention dynamics** as opposed to any other training mechanism. The correlation also drops substantially from layer 0 (~0.95–1.00) to layer 1 (~0.55–0.81), a degradation the paper largely attributes to "more complicated" settings.

### Minor

1. **Experiments measure aggregate proxies rather than the theory's specific quantities.** The theory makes per-token predictions about $\vz_m(t)$ and $\vv_k(t)$, but the experiments measure aggregate statistics (attention entropy, stable rank). While consistent with the theory, these coarser measures could arise from multiple mechanisms, and the relationship between per-token predictions and aggregate curves is not formally established.

2. **Key quantitative comparisons are missing.** The paper states "high correlation" (Fig. 1) without a correlation coefficient; states attention patterns "consistent with our theoretical analysis give the lowest validation losses" (Fig. 5 caption) without validation perplexity values or standard errors; and positions itself against Scan&Snap without any direct quantitative comparison.

3. **The claim that JoMA "removes unrealistic assumptions" from prior work is overstated.** The paper replaces Scan&Snap's assumptions (no residual connections, linear activation) with different assumptions (orthonormal embeddings, stationary backpropagated gradients, constant expected attention). The net reduction in restrictiveness is unclear, and some new assumptions (stationary backpropagated gradients during joint end-to-end training) are themselves strong.

4. **The backpropagated gradient stationarity assumption (Assumption 1) is not tested for the central experiments.** The paper notes this holds exactly for layer-wise training and approximately for joint training, but the main experiments (end-to-end WikiText training) are joint training where gradients depend on the entire evolving model state. Whether the approximation is reasonable is not investigated.

### Trivial

- The paper does not specify how "attention sparsity" is computed (e.g., whether it is entropy, a sparsity coefficient, or something else) in the experiment descriptions.
- Architecture details for the WikiText-trained models (number of layers in multi-layer settings, hidden dimension) are communicated only through figure captions (e.g., "nlayer3," "nlayer5") rather than in the main text or a table.

## Nice-to-Haves

- **Quantify the softmax approximation error.** Derive or empirically bound the error between predicted and true $\vz_m(t)$ as a function of how much $\bar\vb_m$ varies. This would transform the softmax invariant from a claimed approximation into a controlled one.
- **Restore the link between Theorem 3 (uniform attention) and Eqn. 9 (with attention).** Show rigorously how the $\exp(\vv^2/2)$ factor emerges from the JoMA invariant in the nonlinear setting, or clearly characterize Eqn. 9 as a separate approximation.
- **Direct quantitative comparison to Scan&Snap** on a setting where both frameworks make predictions.
- **Report correlation coefficients** for the Fig. 1 validation of Theorem 1, ideally on synthetic data where the orthonormal embedding assumption can be satisfied exactly.

## Removed Points

The following points from the inputs were removed for the reasons stated:

1. **"The figure itself is not viewable in this text"** (softmax correlation figure) — This is a parser artifact; the original submission contains the figure.
2. **"The paper would be most strengthened not by adding more experiments but by making the existing theoretical connections tighter"** (and the four numbered suggestions from the Strengthening section) — These are suggestions, not weaknesses. Moved to Nice-to-Haves.
3. **Strength Finder claim about "principled explanation of hierarchical feature learning"** — Overstated. Section 5 is largely qualitative for the dynamics claims; the weakness-side characterization is more accurate. The empirical alignment (Table 1) is retained as a separate strength (#5).
4. **Strength Finder claim about "empirical finding that the theoretically-predicted attention pattern coincides with best validation loss"** — The paper asserts this without quantitative comparison; it's retained in weakened form under the minor weaknesses rather than as a standalone strength.
5. **"No quantitative comparison to Scan&Snap"** — While factually correct that no direct comparison is made, this is more of a missed opportunity than a flaw in the paper's own contributions. Moved to Nice-to-Haves.
6. **"The value of the sparse-then-dense claim for downstream understanding is unclear"** — Speculative criticism about what the paper *could have done* rather than what it claims. Removed.
7. **Criticisms about missing appendix content, proofs, or references** — The parser strips these sections from all papers.

## Novel Insights

Beyond the paper's own contributions, the review process reveals a key structural tension: the paper's cleanest theoretical results (exact invariants for exp/linear attention) apply to attention variants that are not standard in practice, while the empirically relevant case (softmax attention, nonlinear activation) requires approximations whose error is uncontrolled. This gap between theoretical elegance and empirical coverage is common in Transformer dynamics work but is particularly acute here because the paper's headline phenomenon (sparse-then-dense) depends on the heuristic step in Eqn. 9 rather than following directly from the proven invariants. The stable-rank prediction offers a promising way to bridge this gap by providing a theory-grounded metric that depends only on model parameters.

## Suggestions

1. Report numerical correlation coefficients for the Fig. 1 validation of Theorem 1's softmax invariant, along with error bars across multiple random seeds.
2. Clarify the derivation from Theorem 3 (uniform attention) to Eqn. (9) (with attention): either prove that the $\exp(\vv^2/2)$ factor emerges rigorously from the JoMA invariant applied to the nonlinear setting, or explicitly characterize Eqn. 9 as a heuristic approximation with testable consequences.
3. For the hierarchical learning claims, provide even a simplified two-layer dynamical analysis showing that the co-occurrence structure of latents induces the predicted attention dynamics at higher layers, rather than relying solely on qualitative prose.
4. Fix the missing experimental details: specify how attention sparsity is computed, report architecture hyperparameters for WikiText experiments, and include validation perplexity values with standard errors for the learning rate comparison (Fig. 5).

## Score and Decision

The paper has a genuinely novel theoretical contribution in the closed-form invariants (especially for exp/linear attention) and makes an interesting empirical observation about sparse-then-dense attention dynamics. However, the theoretical apparatus suffers from a significant gap between its clean results (which apply to simplified settings) and its empirical validation (which targets realistic settings but relies on uncontrolled approximations). The hierarchical learning claims are largely qualitative. These issues are addressable but substantial.

Score: 5.0 (weak reject / borderline)

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>