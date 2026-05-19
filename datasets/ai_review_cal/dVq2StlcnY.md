- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 6, 8, 6
Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces a theoretical framework — subgraph multilinear extension (SubMT) — to analyze the expressiveness of interpretable GNNs (XGNNs). It identifies that existing attention-based XGNNs suffer a fundamental gap in approximating SubMT (proved for linearized GNNs, supported empirically for nonlinear ones) and proposes Graph Multilinear neT (GMT) with two variants (GMT-lin and GMT-sam) that are provably more powerful at approximating SubMT. Extensive experiments across regular and geometric graph benchmarks show consistent improvements over state-of-the-art XGNNs in both interpretability and OOD generalization.

---

## Strengths

1. **Novel theoretical framework (SubMT).** The paper formalizes interpretable subgraph learning as a multilinear extension of the subgraph classifier (Definition 3.1), providing a principled lens to analyze XGNN expressiveness that was absent in prior work. This connects the problem to a well-studied combinatorial optimization tool and provides a clear target for what XGNNs should approximate.

2. **Provable limitation of linearized XGNNs.** Proposition 3.3 formally shows that linearized GNN classifiers with more than one message-passing layer cannot approximate SubMT due to Jensen's inequality. This pins down a specific failure mode in the prevalent attention-based paradigm with clear mathematical reasoning.

3. **Novel faithfulness metric.** Counterfactual fidelity (Definition 4.1) measures how sensitively a XGNN's predictions respond to changes in the extracted subgraph, and Proposition 4.2 ties it theoretically to SubMT approximation quality. The empirical diagnostic (Figure 2) showing that GSAT's fidelity is 2–3× lower than simulated SubMT demonstrates the metric's practical value.

4. **Provably better architecture with empirical validation.** GMT-sam is equipped with a probabilistic guarantee (Theorem 5.1) that it ε-approximates SubMT with high probability. The experimental results (Tables 1–4) show consistent improvements over state-of-the-art XGNNs (up to 10% in interpretability and generalization) across diverse benchmarks with multiple backbones (GIN, PNA, EGNN), lending credibility to the theoretical claims.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical claim is stronger than what is proven.** Proposition 3.3 shows that *linearized* GNNs (Eq. 9) with k>1 cannot approximate SubMT. However, the paper's narrative — in the abstract ("existing XGNNs can have a huge gap in fitting SubMT"), introduction ("the prevalent attention-based paradigm can fail to reliably approximate SubMT"), and Section 3.2 title ("ISSUES OF EXISTING APPROACHES") — frames this as a general diagnosis for all attention-based XGNNs. The paper does not prove the gap exists for nonlinear GNNs (the practically relevant case), where the Jensen argument does not directly apply. The empirical counterfactual fidelity evidence (Figure 2) is suggestive but not a proof. This is an **evidential gap**: the conclusion may well be correct, but the evidence provided does not fully close the distance between what is proven and what is claimed.

2. **GMT-sam's evaluation is confounded by computational cost.** GMT-sam approximates SubMT by averaging predictions over t random subgraph samples, requiring t forward passes through the classifier. The paper does **not report the value of t used in the main experimental tables** (Tables 1–4). Figure 3 shows interpretability improving with sampling rounds up to ~10–20. If t ≈ 10, inference requires ~10× the compute of a baseline like GSAT, yet no comparison controls for this (e.g., an ensemble of 10 GSAT forward passes, or GMT-sam with t=1 vs baselines). Without such a control, the reported improvements cannot be cleanly attributed to the method rather than to additional compute. This is a **methodological gap** in the evaluation design.

### Minor

1. **Ambiguity in GMT-lin's architecture.** Section 5.1 describes GMT-lin as using a linearized classifier with only 1 round of weighted message passing (via \(f_c^l(G_c)=\rho(\widehat{A}\odot A^{k-1}XW)\)). However, the experiments apply GMT-lin with highly nonlinear backbones (GIN, PNA), and the paper states it "can already achieve better interpretability than the state-of-the-art methods even with non-linear GNNs." Whether the *classifier* within GMT-lin is truly linearized or still uses a nonlinear GNN backbone is not clearly specified, making the connection between the theoretical motivation (linearity) and the implemented architecture difficult to verify.

2. **Neural SubMT variant proposed but not evaluated.** Section 5.2 introduces learning a "neural SubMT" that would require only a single forward pass at test time. This is a natural extension that addresses the computational cost concern of GMT-sam, but no experimental results are reported for it. The idea appears in the paper (and even in Figure 1's caption) as a core component, but remains empirically unvalidated.

3. **Counterfactual fidelity estimation does not perfectly match its definition.** Definition 4.1 involves distributions over whole graphs \(G\) and \(\widetilde{G}\) with different labels. The practical estimation (Eq. 11) instead perturbs the *attention matrix* of a single input graph to generate different extracted subgraphs and measures prediction sensitivity. While a reasonable approximation, the connection between the definition and the estimator is not justified, and the theoretical guarantee in Proposition 4.2 presupposes SubMT approximation — which is precisely what is being diagnosed.

4. **Theorem 5.1's guarantee is conditional on correct attention probabilities.** The theorem bounds the Monte Carlo sampling error *given* the learned attention matrix \(\widehat{A}\). It does not guarantee that the subgraph extractor \(g\) learns the correct Bernoulli probabilities in the first place — only that if it does, the sampling procedure approximates SubMT well. The paper could be clearer about this limitation.

5. **Non-standard statistical significance reporting.** The paper uses "mean − 1×std larger than the mean of the best baseline" as a significance criterion. This is uncommon and less informative than standard alternatives (confidence intervals, paired tests). It also conflates variance with effect size in a heuristic way.

### Trivial
- The derivation flow from Eq. 2 to Eq. 3 is somewhat compressed; the notation \(\mathbb{E}_{G_c\sim g(G)}\) appears abruptly after a shift in formalism.

---

## Nice-to-Haves

- **Compute-controlled ablation for GMT-sam.** Running GMT-sam with t=1 (or matching total forward passes against baselines) would cleanly separate the benefit of the method from the benefit of additional computation.
- **Extension of the theoretical analysis to nonlinear GNNs.** Even a partial result (e.g., showing the Jensen gap is bounded away from zero under specific conditions) would substantially strengthen the paper's core narrative.
- **Clearer architectural diagram or pseudocode for GMT-lin**, specifying which parts are linearized vs. nonlinear, and how the \(A^{k-1}\) term interacts with the backbone.
- **Discussion of the independent Bernoulli edge-sampling assumption's limitations.** Real causal subgraphs may have more complex dependencies (e.g., edge dependencies, path constraints), and acknowledging when this assumption might break would strengthen the paper's framing.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **"Derivation from Eq. 2 to Eq. 3 is hand-wavy"** — This is a presentation nitpick too minor to carry weight. The formalism is conceptually sound.
- **"Proposition 3.3 explicitly assumes linear GNNs; the paper should note this"** — The paper already states this clearly ("Eq. 8 with linear GNNs (Eq. 9) and k>1") and the proposition is correctly scoped. The broader issue about extrapolating to nonlinear GNNs is already covered in Major weakness #1 above.
- **"Notation \(\widehat{G}_c = g(G)\) is overloaded"** — A minor notation observation with no substantive impact on the paper's validity.
- **"Figure captions could be more self-contained"** — A formatting/style observation; not a substantive weakness.
- **"The paper should include results for neural SubMT or clearly state it is left for future work"** — Already captured in Minor weakness #2. The point is valid but does not need separate listing.
- **"Missing related works"** — Removed per hard rule: I cannot verify the existence of missing references without external sources.

---

## Novel Insights

The harsh critic's observation that the paper's failure diagnosis is broader than what Proposition 3.3 proves is accurate and important. However, a more subtle insight emerges when reading the paper's structure closely: the paper actually operates on *two levels of evidence simultaneously* — a clean theoretical result for linearized GNNs (Proposition 3.3) and an empirical diagnostic (counterfactual fidelity in Figure 2) for nonlinear GNNs. The paper would benefit from explicitly framing this as a two-tier argument rather than presenting the theory and then treating the empirical results as merely corroborative. The strength finder correctly identifies that the SubMT framework itself (not just the failure diagnosis) is the paper's primary contribution; even if the failure mechanism were only proven for the linearized case, the framework remains valuable for designing and analyzing XGNNs.

---

## Suggestions

1. **Report the value of \(t\) used for GMT-sam in all main experiments.** Without this, the evaluation is incomplete.
2. **Add a compute-controlled ablation** comparing GMT-sam with t=1 (or an ensemble baseline with matched forward passes) against GSAT to disentangle method benefit from compute benefit.
3. **Clarify GMT-lin's architecture precisely:** specify whether the classifier \(f_c^l\) uses activations, how the backbone's nonlinearity interacts with the "1 round of weighted message passing" design, and provide pseudocode or a block diagram.
4. **Soften the narrative scope claims** to match the proven scope. E.g., "We prove that linearized XGNNs with k>1 cannot approximate SubMT, and provide empirical evidence that this gap extends to popular nonlinear XGNNs."
5. **Either include experimental results for the neural SubMT variant**, or clearly relegate it to future work with an explicit statement.
6. **Use standard significance reporting** (confidence intervals or paired tests) to improve interpretability of the experimental results.

---
