Now I have all the information needed to verify each claim against the paper. Let me write the consolidated review.

---

## Summary

This paper introduces Ferumal flows, which replace the neural-network-based scaling and translation functions inside affine coupling layers (RealNVP, Glow) with kernel machines. Using the representer theorem, the authors show the resulting objective can be kernelised, and they employ auxiliary points (analogous to inducing variables in GPs) for computational efficiency. The paper demonstrates that kernelised flows match or exceed the density estimation performance of their neural counterparts while using up to 93% fewer parameters, and show particularly strong results in low-data regimes.

## Strengths

- **Novel and theoretically grounded integration of kernels into coupling-layer flows.** The representer theorem argument (Proposition 1) correctly shows that any solution can be projected onto the span of training features without changing the objective, enabling kernelisation. The paper is transparent about the lack of a regulariser and the "if a solution exists" caveat (lines 148–149). This is a clean theoretical contribution.

- **Dramatic and well-documented parameter reduction.** Table 4 (lines 334–350) shows that kernelising RealNVP reduces parameters by up to 93% (Power: 228K → 16K) and kernelising Glow reduces parameters by up to 91% (Power: 228K → 20K), while density estimation performance is maintained or improved. This directly validates the paper's central efficiency claim.

- **Competitive or superior density estimation on real-world benchmarks.** Table 2 (lines 273–293) shows FF-RealNVP and FF-Glow match or exceed their neural counterparts on all five UCI datasets. FF-Glow on Gas (10.75 vs. 8.15) and Power (0.35 vs. 0.17) show notable improvements.

- **Strong low-data performance.** Table 3 (lines 306–320) shows that kernelised RealNVP (e.g., 11K params on Gas) substantially outperforms the continuous-flow FFJORD (e.g., 279K params on Gas) on 500-example subsets of all five datasets. This supports the paper's claim that kernelised flows are well-suited for data-scarce applications.

- **Drop-in compatibility with existing coupling-layer architectures.** The method applies to both RealNVP and Glow without architectural disruption, and the discussion (lines 373–375) notes extensibility to spline flows, ButterflyFlows, and other coupling-layer designs.

## Weaknesses

### Fatal

None.

### Major

- **Incomplete low-data comparison limits the paper's central claim.** The stated motivation is that kernelisation rescues flow performance when data are scarce. Yet the low-data experiment (Table 3) compares only against FFJORD — a continuous flow with a very different architecture and far more parameters. The paper states that "Glow and RealNVP struggled to generalise" (line 322), citing prior work and noting increasing validation losses, but provides *no quantitative results* for these neural baselines under the same 500-example conditions. Without showing that the *same architectures* with neural networks fail in the identical setting, the paper cannot isolate the effect of kernelisation from other architectural differences. Adding direct kernelised-vs-neural comparisons (e.g., RealNVP vs. FF-RealNVP, Glow vs. FF-Glow) on the low-data subsets would significantly strengthen this core claim.

- **No ablation or diagnostic analysis of why kernelisation yields large improvements.** FF-Glow improves over Glow by roughly 2.6 nats on Gas and 6.7 nats on Miniboone. These are very large gains for replacing only the learned functions inside each coupling layer. The paper offers no analysis of whether this comes from the kernel's inductive bias, the parameter reduction, the data-dependent initialisation, or something else. The "Initial performance" section (lines 296–299) mentions faster convergence but gives no quantified decomposition. Without ablations (e.g., varying the number of auxiliary points, comparing different kernel choices, studying the effect of parameter reduction while holding architecture constant), the reader cannot rule out baseline tuning gaps or implementation artifacts as drivers of these improvements. This is the paper's most significant empirical gap.

- **Missing analysis of computational cost.** The paper claims efficiency advantages ("faster convergence", "fewer hyperparameters") but reports no wall-clock time, per-epoch time, or total training time comparisons. Kernel methods with auxiliary points can be slower at inference when the number of auxiliary points is moderate, and the paper does not acknowledge or quantify this trade-off. Given that the paper motivates its method partly on efficiency grounds, this omission is notable.

### Minor

- **Several experimental details are underspecified in the main text.** The kernel choice (SE vs. Matern) per dataset, lengthscale initialisation and bounds, and the number of auxiliary points used for each dataset are not reported. The paper references appendix tables (e.g., Table~\ref{tab:error bars}, Table~\ref{train details}) that were stripped by the parser, so this information likely exists in the full submission. However, the main text should at least summarize these choices per dataset.

- **Toy dataset neural-network baseline is not identified.** Table~\ref{toy datasets} (lines 243–256) reports "NN-based (44K)" without specifying whether this is RealNVP, Glow, or a different architecture. This matters because the toy results are meant to illustrate the benefit of kernelisation, but the reader cannot assess whether the comparison is against a reasonable neural baseline.

- **Error bars are referenced but not presented in the main results.** The paper states "Please refer to Table~\ref{tab:error bars} for error bars" (line 268), suggesting they exist in the appendix. While this is common practice, the main results table (Table 2) is the first thing a reader examines, and the absence of variance information there weakens the immediate credibility of the results. Including a summary (e.g., "±X" notation in the main table) would improve presentation.

### Trivial

- The claim that "parameter sharing … resulted in a decline in performance" (line 205) is mentioned without any experimental data. Either present the negative result or remove the claim.

- The Discussion mentions "hybrid modelling" (line 359) but provides no description or evaluation. Either describe it or remove the mention from the summary.

- The framing of "negligible" hyperparameters (line 234) is mildly overstated: the method still requires choosing the kernel family, lengthscale initialisation, number of auxiliary points, and layer-sharing scheme. The paper does list these honestly in the same paragraph, so this is a presentational choice rather than a substantive error.

## Nice-to-Haves

- An ablation study varying the number of auxiliary points to show how approximation quality trades off against performance.
- Training loss curves with variance bands comparing kernelised and neural versions under controlled conditions (same architecture, differing only in the coupling function).
- Wall-clock time comparisons (per-epoch and total) between kernelised and neural versions.
- A direct low-data comparison between kernelised and neural versions of the *same* coupling-layer architecture (RealNVP or Glow) with both training and test likelihood curves.

## Removed Points

These points were identified by reviewers but are removed or downgraded after verification against the paper:

1. **"No error bars on any experimental result"** — Removed. The paper explicitly references "Table~\ref{tab:error bars}" (line 268) for error bars. They exist in the appendix. The criticism is downgraded to a minor presentation issue above, not a missing-results issue.

2. **"Representer theorem argument is incomplete"** — Removed. The paper explicitly states "if a solution exists" (lines 148–149) and acknowledges the lack of a regulariser. The mathematical claim is correctly qualified and the proposition is sound. The reviewer's concern about optimization stability is valid but concerns a different issue (convergence, not representer theorem validity).

3. **"Missing related work on regularising neural flows (weight decay, dropout, normalisation)"** — Removed. The paper's scope is kernelisation, not a survey of regularisation techniques. Line 234 actually lists "normalisation" and "dropout" as neural-network hyperparameters, showing awareness. The paper does not claim neural flows cannot be regularised.

4. **"Paper implicitly assumes neural-network flows cannot be regularised"** — Removed. This claim is not made anywhere in the paper. The paper argues neural flows are over-parameterised and struggle with generalisation in low-data regimes, which is a different claim.

5. **"Missing figure in Initial performance section"** — Removed. The paper references "Figure~\ref{fig:nats}" (line 297) which was stripped by the parser. The figure exists in the original submission.

## Novel Insights

The reviewers' comments surface a tension that the paper does not fully resolve: the method's most impressive results (low-data generalisation, dramatic gains on Gas and Miniboone) are presented as consequences of kernelisation, but the paper lacks the controlled experiments needed to attribute these gains to specific properties of the kernel (inductive bias, parameter efficiency, data-dependent initialisation, or simply better optimisation dynamics). This gap is not unusual for a first paper on a new approach, but it means the paper's contribution is currently better described as "demonstrating that kernelised flows can work well" rather than "explaining why kernelised flows work well." The theoretical framing via the representer theorem is solid, but the empirical story needs more internal controls before the mechanism can be claimed with confidence.

## Suggestions

1. **Run a controlled low-data comparison**: Compare FF-RealNVP vs. RealNVP and FF-Glow vs. Glow on the 500-example subsets (same architecture, same training setup, differing only in the coupling function). This directly isolates the effect of kernelisation.

2. **Add an ablation on the number of auxiliary points** across at least one dataset to show how performance and training time trade off against approximation quality.

3. **Report training loss curves with variance bands** for kernelised vs. neural versions of the same architecture under identical conditions, to substantiate the claimed convergence advantage.

4. **Add wall-clock time comparisons** per epoch and total for kernelised vs. neural versions.

5. **Clarify the toy dataset baseline**: specify which architecture "NN-based (44K)" refers to.

6. **Include a summary of error bars** (e.g., "±X" notation) directly in the main results table rather than only in the appendix.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>