Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces Ferumal flows, a novel approach that replaces the neural-network-based scaling and translation functions in affine coupling layers (RealNVP, Glow) with kernel-based functions defined in an RKHS. The authors adapt the representer theorem to the non-convex, unregularized flow objective, proving that optimal RKHS elements can be expressed as kernel expansions. Auxiliary points (analogous to inducing variables in sparse GPs) keep the method practical. On five standard tabular benchmarks, kernelised flows match or exceed their neural-network counterparts while using up to 93% fewer parameters, and they show strong low-data performance against FFJORD.

---

## Strengths

- **Parameter reduction of up to 93% with maintained or improved likelihood (Tables 1 and 5).** On Power, FF-RealNVP requires only 16K parameters vs. RealNVP's 228K (93% reduction), yet achieves a higher log-likelihood (0.24 vs. 0.17). Across all five datasets, both FF-RealNVP and FF-Glow match or exceed their NN counterparts on likelihood while using drastically fewer parameters. This is the paper's strongest evidence and directly supports its core claim.

- **Strong generalization in the low-data regime against a stronger baseline (Table 4).** With only 500 training examples, kernelised flows outperform FFJORD by large margins on all five datasets (e.g., Gas: 0.22 vs. −7.50 nats) while using 71–97% fewer parameters. This is noteworthy because FFJORD is described (and known) to be stronger than RealNVP/Glow, so winning against it with far fewer parameters makes a compelling case.

- **Principled theoretical foundation for kernelisation (Proposition 1, Section 3).** The paper adapts the representer theorem to the non-convex, unregularized flow objective. The proof shows that orthogonal components of the RKHS elements can be dropped without changing the objective, so optimal solutions can be expressed as kernel expansions. This is non-trivial because standard representer theorems rely on a regularizer; the paper correctly handles this case.

- **Clear novelty and differentiation from prior kernel-based generative methods (Section 4).** The paper convincingly distinguishes itself from Iterative Gaussianisation methods (which use dimension-wise kernel density estimation + rotation) and kernel transport operators (which use pre-trained autoencoders). Ferumal flows replace the network directly in each coupling layer, enabling a genuine drop-in replacement.

- **Dramatically simplified hyperparameter space.** The paper correctly notes (lines 234–236) that kernelised flows require tuning only of kernel hyperparameters and auxiliary point count, whereas NN flows require choices for hidden layers, nodes, activation functions, normalization, dropout, etc. This is a practical advantage, especially in low-data settings.

---

## Weaknesses

### Fatal

None.

### Major

- **Low-data claim about RealNVP/Glow "failing entirely" is not directly tested in the paper's own experimental setup.** The paper's Discussion (line 359) states that "Glow and RealNVP fail entirely" in the low-data regime, and the Introduction (lines 22–24) motivates kernelisation by arguing that NN flows "struggle to generalise in the low-data regime." However, Table 4 (the low-data experiment) compares only the kernelised version against FFJORD — not against RealNVP or Glow on the same 500-example subsets. The claim about RealNVP/Glow failing is cited from Meng et al. (line 322) rather than demonstrated in the paper's own controlled setting. Since FFJORD is a continuous-flow model with a completely different architecture, the comparison does not isolate the effect of kernelisation on the same coupling-layer architecture. This weakens the paper's central motivating argument. **Why it matters:** A reader cannot fully attribute the low-data improvement to kernelisation rather than to architectural differences between coupling-layer flows and FFJORD. The paper would be significantly strengthened by adding the direct comparison with RealNVP/Glow in this setting.

### Minor

- **Number of layers \(L\) per dataset is not reported.** The paper provides the parameter count formula \(2Ln(D-d)\) (line 164) and gives total parameter counts in Table 5, but never states how many layers were used for each dataset. This makes it difficult to cross-check the parameter counts or reproduce the experiments without reverse-engineering \(L\) from the reported counts.

- **No sensitivity analysis on the number of auxiliary points \(N\).** The paper reports using \(N=150\) in most cases (line 235) but does not study how performance varies with \(N\). Since \(N\) is a new hyperparameter introduced by the method, understanding its impact (e.g., on Gas or Power) would help readers assess robustness and guide practical use.

- **Faster convergence claim lacks quantitative support.** The paper claims faster convergence (lines 297–299) and references Figure~\ref{fig:nats} (learning curves), but no quantitative summary is provided — e.g., number of epochs to reach a given validation loss or a convergence speed comparison metric. The evidence is purely visual from a single figure. A brief quantitative statement would substantially strengthen this claim.

### Trivial

None.

---

## Nice-to-Haves

- A wall-clock time or per-iteration cost comparison between kernelised and NN-based coupling layers on one representative dataset would help readers understand the practical trade-off (kernelised flows save parameters but may incur overhead from kernel matrix computation).
- An ablation comparing the kernelised flow to an NN flow with a deliberately matched parameter count (e.g., reducing RealNVP's hidden-layer width to match the kernelised model's 16K parameters on Power) would directly test whether the performance gain comes from kernelisation itself or simply from having fewer parameters.

---

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

1. **Missing Figure~\ref{fig:nats} / convergence figure absent from paper** — The paper at line 297 references Figure~\ref{fig:nats} showing learning curves. This figure exists in the original PDF submission but is stripped by the PDF-to-text parser. Parser artifacts are not author errors.

2. **Missing training details table (Table~\ref{train details})** — Referenced at line 240; exists in the original submission but stripped by the parser.

3. **Missing error bars table (Table~\ref{tab:error bars})** — Referenced at line 268; exists in the original submission but stripped by the parser.

4. **Unfair comparison / hyperparameter tuning imbalance** — The critic suggests the baseline comparison may be unfair because NN flows require more tuning. The paper describes this as a general property of NN vs. kernel methods (lines 234–236), not as an excuse for undertuned baselines. The baselines (RealNVP, Glow) are standard implementations with well-known configurations. This criticism is speculative and generic.

5. **Missing related works** — The rules prohibit citing missing related works as a weakness since I cannot verify their absence or existence.

6. **Reproducibility concerns about undisclosed hyperparameters** — The paper provides kernel type (SE/Matern), optimizer (Adam with adjustable β₁, β₂), learning rate schedules (StepLR/CosineAnnealing), auxiliary point count (150), and implementation framework (PyTorch, GPyTorch). This is adequate for a conference submission; the training details table is in the appendix.

---

## Novel Insights

The two reviewer perspectives, when synthesized, reveal a tension between the paper's strongest and weakest elements that is not immediately obvious from either review alone. The paper's theoretical contribution — a representer theorem for the non-convex, unregularized flow objective — is genuinely novel and goes well beyond a mechanical application of existing kernel theory. This theoretical framing gives the paper depth that purely empirical kernel + flow combinations would lack. However, the experimental evaluation has an asymmetry: the paper's most striking empirical claim ("kernelisation fixes the low-data failure of NN flows") rests on the weakest evidence (comparison against FFJORD rather than the same architecture with/without kernelisation), while its best-supported claim (parameter efficiency with maintained likelihood on full datasets) is somewhat underplayed. This suggests the paper could be strengthened not by adding more experiments, but by re-centering its narrative on the parameter-efficiency result (which is airtight) and treating the low-data result as suggestive rather than definitive.

---

## Suggestions

1. **Add the direct low-data comparison with RealNVP and Glow (not just FFJORD).** This is the single highest-impact improvement. Use the same 500-example subsets and show that the NN baselines' test loss increases (or underperforms the kernelised version) while the kernelised version generalizes. This would validate the paper's central motivating claim on its own terms.

2. **Report the number of layers \(L\) per dataset** in the main tables or in a supplementary table alongside the parameter counts in Table 5.

3. **Add a brief sensitivity analysis** of the auxiliary point count \(N\) on one dataset (e.g., Gas or Power) showing likelihood vs. \(N\).

4. **Provide a quantitative convergence comparison** — e.g., "FF-RealNVP reached a test log-likelihood of X in Y epochs, whereas RealNVP required Z epochs to reach the same value."

5. **Re-center the narrative** to lead with the parameter-efficiency result (well-supported) and present the low-data finding as a promising additional benefit rather than a primary motivation, unless the direct comparison is added.

---

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>