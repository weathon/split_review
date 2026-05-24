Now I have enough context for calibration. Let me synthesize the final review.

## Summary

The paper proposes a "universal learning principle" for designing GNN graph filters: they should have absolutely summable coefficients (guaranteeing convergence to infinite depth) and be Lipschitz continuous (guaranteeing stability). The authors instantiate this with APGNN, which uses exponentially decaying weights ($\theta_k = \beta_k \alpha^k$) with a $P$-hop aggregation. They also provide a generalization bound analysis under a continuous-graph setting. Experiments on 8 benchmarks show APGNN achieving top-1 accuracy on 7 of them.

## Strengths

1. **Clear, well-motivated design principle.** The idea that a graph filter needs (a) absolutely summable coefficients for convergence and (b) Lipschitz continuity for stability is clearly articulated. Theorem 1's sufficient condition (absolute summability → convergence) is correctly used, and connections to existing methods (PPNP, DAGNN, GPR-GNN) in Section 4.2 demonstrate the principle's organizing power.

2. **Strong empirical results on diverse benchmarks.** Table 1 shows APGNN achieves the highest average accuracy on 7 of 8 datasets (Cora, Citeseer, Pubmed, Wiki-CS, MS-Academic, Cornell, Wisconsin), often with non-trivial margins (e.g., 93.27% vs 90.39% on Cornell, 94.12% vs 92.94% on Wisconsin). Standard deviations are reported over 10 runs.

3. **Informative ablation studies.** Figure 2 validates that accuracy plateaus for $K > 10$ (consistent with the exponential truncation error bound) and identifies the optimal $\alpha$ range $[0.6, 0.9]$. Figure 3 demonstrates the $P$-hop filter's ability to maintain or improve accuracy while reducing the number of parameters.

4. **Graph-size-independent truncation error bound.** Equations (13)–(14) give an upper bound $\alpha^{K+1}/(1-\alpha)$ on the approximation error of the $K$-order truncated filter that depends only on $\alpha$ and $K$, not on the graph structure. This allows principled control of depth vs. precision.

## Weaknesses

### Fatal

None.

### Major

1. **Incorrect "if and only if" in Lemma 1 / Theorem 1.** Lemma 1 states that for a fixed $\gamma \in (-1, 1]$, $\sum a_k \gamma^k$ converges uniformly and absolutely *if and only if* $\sum a_k$ converges absolutely. The "only if" direction is false when $|\gamma| < 1$ (e.g., $a_k = 1$, $\gamma = 0.5$: $\sum (0.5)^k$ converges but $\sum 1$ diverges). This error propagates to Theorem 1. While the sufficient direction is all the paper actually uses (APGNN always satisfies $\sum |\theta_k| \leq 1/(1-\alpha) < \infty$), presenting a wrong claim as a foundational lemma undermines theoretical rigor. The authors should replace "if and only if" with "if" (i.e., state it as a sufficient condition) or clarify that the "only if" direction refers to uniform convergence over the whole interval $\gamma \in (-1, 1]$ (in which case evaluating at $\gamma=1$ would salvage it — this needs clear rephrasing).

2. **Unclear experimental comparison methodology.** The paper states: "To ensure a fair comparison with the compared methods, we also applied our optimal hyperparameters to them, selecting the maximum value to display." This is genuinely ambiguous — it could mean APGNN's hyperparameters were forced onto baselines (which would systematically disadvantage them), or it could mean something else entirely. Combined with the preceding sentence "their parameter settings follow the previous practices," the overall experimental protocol for baselines is unclear. Since the paper's central claim of SOTA performance depends on this, the authors need to clarify exactly how each baseline was tuned, report the hyperparameter search ranges, and ideally confirm that baselines were independently tuned using their own recommended protocols.

### Minor

3. **Generalization bound presented with informal notation and missing constants.** Theorem 2 uses "$\lesssim$" notation and a constant $C$ "related to the graph function" without derivation. While the notation is briefly defined (line 197), the bound's tightness cannot be assessed. The proofs are deferred to an appendix that is not visible in the submission. Given the paper's emphasis on theory, a proof sketch in the main text would strengthen the presentation.

4. **The $P$-hop filter's approximation bound has a minor inaccuracy.** The bound $|g_\beta^{\infty,P}(\lambda_i) - g_\beta^{K,P}(\lambda_i)| < (\alpha(1-\delta)^P)^{K+1}/(1-\alpha)$ should have denominator $1-\alpha(1-\delta)^P$ rather than $1-\alpha$, assuming standard geometric series summation. The approximation is close when $\alpha(1-\delta)^P \approx \alpha$ but not exact as stated.

5. **Continuous-graph generalization analysis has unclear connection to discrete experiments.** The generalization bound (Section 5) is derived under a continuous-graph setting with integral operators, while the experiments use standard discrete graphs. The paper does not discuss how the bound transfers to the discrete case or whether the continuous assumptions are reasonable for the benchmarks used.

### Trivial

None.

## Nice-to-Haves

- A brief complexity statement ($O(KP|E|d)$ or similar) in the main text rather than deferred entirely to the appendix.
- A limitations paragraph discussing when the P-hop filter may become dense for large $P$, the additional hyperparameters $\alpha$ and $P$ requiring tuning, and that the "universal" principle is only a sufficient condition.

## Removed Points

- **"The generalization bound uses an undefined '≲' symbol"** — The paper defines it on line 197: "The notation '≲' denotes 'less than or approximately equal to the right-hand side' and guarantees an approximation error of at most $\mathcal{O}(\sqrt{\log(1/\tau)/n_l})$." The definition is informal but present. Demoted from the critic's claim to a Minor weakness (lack of full derivation).
- **"The paper fails to discuss that DAGNN is only defined for finite $K$ in practice"** — The paper's point is about the *inconsistency* with infinite-depth extension, which is a valid theoretical observation. The critic's framing of this as a weakness blurs the paper's intended contribution (characterizing infinite-depth behavior). Removed.
- **"Missing related works"** — Cannot be confirmed without external literature search. Removed per instructions.
- **"Missing appendix / proofs"** — The parser strips these. Removed per instructions. (Deferral to appendix is noted as Minor weakness 3 above in a mitigated form.)
- **Strength Finder's generic strengths** — Removed generic/superficial praise such as "the paper addressed an important problem."

## Novel Insights

The reviews surface an interesting tension: the paper's claimed "universal learning principle" is essentially a rediscovery, in the GNN context, of the standard Weierstrass M-test (absolute summability implies uniform convergence) plus a Lipschitz stability condition. The novel insight from merging both reviews is that the paper's *methodological* contribution (APGNN with exponential decay) is more valuable than its *theoretical* contribution (the "universal principle"), since the principle itself is standard analysis dressed in graph terminology, while APGNN's design — using $\theta_k = \beta_k \alpha^k$ to get controllable truncation error $O(\alpha^K)$ and favorable generalization bounds $O(\sqrt{\log K})$ — is a concrete and well-executed instantiation that demonstrably works on benchmarks. None beyond the paper's own contributions.

## Suggestions

1. **Fix Lemma 1 and Theorem 1.** Change "if and only if" to a clear sufficient condition statement, or rephrase Lemma 1 to say "if $\sum |a_k|$ converges, then for any $\gamma \in (-1, 1]$, $\sum a_k \gamma^k$ converges uniformly and absolutely." This does not affect any downstream result.
2. **Rewrite the experimental setup paragraph.** State clearly: (a) each baseline was tuned over its own hyperparameter space following its original paper's protocol, (b) the best hyperparameter setting per baseline was selected via validation accuracy, and (c) report the search ranges for all methods.
3. **Include a proof sketch for Theorem 2** in the main text, giving the key steps of the excess risk decomposition and showing where the Lipschitz constant $L_M$ enters.
4. **Correct the denominator** in the $P$-hop filter bound from $(1-\alpha)$ to $(1-\alpha(1-\delta)^P)$.
5. **Explicitly state computational complexity** $O(KP|E|d + \text{MLP cost})$ in the main text.

## Score and Decision

Let me finalize my score through calibration.

**Round 1 (bracketing):** I queried three bands:
- Low (< 3.5): retrieved papers avg 2.33–3.40 (Dirichlet energy, oversmoothing, random weights). The current paper is clearly stronger.
- Middle (3.5–7.5): retrieved papers avg 4.00–5.25 (polynomial filter theory, spectral generalization, spectral benchmarking). The current paper is in this band.
- High (> 7.5): retrieved papers avg 8.00–8.50 (spectral algorithms, graphon NNs, Hölder stability). The current paper is far below this.

**Round 1 bracket: [4.0, 6.0].**

**Round 2 (narrowing):** I queried inside the bracket (4.5–6.0 and 6.0–7.5) and read full reviews for:
- *Rethinking Spectral GNNs with SAF* (avg 5.5, Reject) — well-written with solid theory and comprehensive experiments, but required expensive eigendecomposition. Current paper has cheaper computation but a mathematically imprecise lemma. Slightly weaker overall → suggests score below 5.5.
- *Generalization of Spectral GNNs* (avg 5.0, Reject) — rigorous theory but weaker experiments. Current paper has stronger experiments but less rigorous theory → comparable, around 5.0.
- *Spectral Benchmarking* (avg 5.25, Accept-Poster) — good empirical benchmark but limited novelty. Current paper comparable in quality but different profile.

**Final score: 5.0.** The paper has a genuinely useful core idea (exponential decay for provably convergent graph filters) and strong empirical results. However, the mathematical error in the foundational lemma and the unclear experimental comparison methodology are significant concerns that prevent acceptance at a top venue in the current form. The paper's position relative to the anchors: clearly above the 3–4 cluster (Dirichlet energy, random weights), comparable to the mid-5 spectral GNN papers, but not reaching the 6+ threshold for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>