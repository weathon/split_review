Here is the final consolidated review:

---

## Summary

This paper proposes UFGM, the first unsupervised federated graph matching (FGM) method. It uses MCMC-based graphlet sampling to extract node structural features and generate pseudo-matched node pairs across clients, enabling supervised-style training in a federated setting without ground-truth pairs. It then introduces a separate trust region optimization architecture where the server evaluates the global model on cross-client pseudo pairs while clients optimize locally, with a scalar-matrix Hessian approximation derived from integrated weak quasi-Newton conditions. Empirical results on SNS and PPI datasets show UFGM outperforms federated baselines in matching accuracy and convergence speed.

## Strengths

1. **First formalization of federated graph matching as a distinct problem.** The paper correctly identifies that existing FGL covers node classification, graph classification, network embedding, and link prediction but not graph matching, and provides a clean problem definition (Section 2.2, Eqs. 3–4) that formalizes the privacy constraint. This framing is a genuine advance over prior work.

2. **Separate trust region architecture that directly addresses the FGM optimization challenge.** The paper identifies a real obstacle: standard SGD fails in FGM because clients cannot compute cross-client loss on pseudo-matched pairs (Section 1, line 20). The server-evaluates/client-optimizes separation (Section 4, lines 137–147) is a principled architectural response to this constraint, and the protocol is made explicit.

3. **MCMC-based graphlet sampling with theoretical grounding.** The paper provides a closed-form sampling probability (Theorem 1) and a variance bound for the Horvitz–Thompson estimator (Theorem 2), linking estimation quality to the choice of the starting-node distribution *q*. This goes beyond a black-box heuristic.

4. **Hessian approximation via integrated weak quasi-Newton conditions with error analysis.** The derivation integrating two weak quasi-Newton conditions into a scalar-matrix approximation α**I** (Eqs. 18–19) is non-trivial, and Theorem 3 provides a formal characterization of the approximation error.

5. **Empirical results showing UFGM outperforms federated baselines** on SNS and PPI, with reported convergence improvements of 31.8% and 35.4% over other federated methods.

## Weaknesses

### Major

1. **Privacy claims are asserted without any formal analysis, despite being the paper's core motivation.** The paper centrally motivates the federated setting by privacy concerns and lists "strong privacy protection" as its first compelling advantage (Section 1, final paragraph). However, it provides no threat model definition, no privacy analysis of any kind (no differential privacy, no cryptographic security argument, no information-theoretic bound), and no characterization of what an adversary can or cannot infer. The encryption mechanism — a random nonsingular matrix **K** shared among all clients but not the server — is described in a single paragraph (Section 3, lines 76–77) with no security analysis. Furthermore, since **K** is shared among all clients, any single compromised client exposes all encrypted data to the server; this failure mode is not discussed. For a paper whose central claim is privacy-preserving FGM, this gap undermines the paper's own framing. The authors need to either provide a formal privacy analysis with a clear threat model, or substantially temper their privacy claims.

2. **No ablation study to isolate component contributions.** The method has three main components: (a) graphlet-based pseudo-label generation, (b) separate trust-region optimization, (c) Hessian approximation via weak quasi-Newton conditions. Without ablations that replace each component with a simpler alternative (e.g., random pseudo-labels, standard FedAvg with SGD, exact Hessian), the reported improvements cannot be attributed to specific design choices. This is a particular concern because the method is "first of its kind" — without ablation, readers cannot tell which component drives performance.

3. **No error bars, variance, or statistical significance on reported results.** All results are presented as single numbers without standard deviations, confidence intervals, or multiple-run statistics. Federated learning is inherently stochastic (random initialization, training dynamics); single-run comparisons do not provide reliable evidence. This is a basic experimental rigor requirement.

### Minor

4. **The variance bound in Theorem 2 is practically vacuous.** The bound involves *D* = ∏_{l=2}^{k-1} (*d*₁ + ... + *d*ₖ), which grows exponentially with graphlet size *k* and with node degrees. No practical number of samples *O* needed to achieve a given error tolerance is derivable from this bound. The paper's claim that this bound demonstrates estimates are "close to the actual count" (line 128) does not follow from the bound as presented.

5. **The Hessian approximation error (Theorem 3) involves unquantified higher-order derivatives.** The error expression depends on third- and fourth-order tensors (𝒜_{b+1} and ℬ_{b+1}) for which no bounds are provided. The result characterizes the error structure but does not yield a practical guarantee or actionable bound.

6. **No communication cost or wall-clock time analysis.** The paper motivates graphlet sampling and Hessian approximation by efficiency concerns ("expensive cost," "time-consuming"), but never reports communication rounds, per-round cost, wall-clock time, or memory usage. For a federated method, communication efficiency is a primary concern and should be quantified.

7. **Baseline comparisons include methods designed for fundamentally different tasks** (centralized graph matching, node classification, domain adaptation). While no direct FGM baseline exists and the paper acknowledges this, the comparison against centralized methods (which have no privacy constraints) is labeled as showing UFGM is "only 15.3% lower," which is an expected asymmetry. A federated adaptation of an existing graph matching method would provide a more informative comparison. The paper also does not explain how the federated graph learning and domain adaptation baselines are adapted for graph matching.

### Trivial

None.

## Nice-to-Haves

- Sensitivity analysis for graphlet size *k* (critical parameter affecting both discriminative power and computational cost).
- Analysis of the weighting parameter ω in the integrated weak quasi-Newton condition.
- Clarification of the exact adaptation protocol for federated baselines to the graph matching task.

## Removed Points

These points were raised by one or both reviewers but removed after verification against the paper or per the review guidelines:

- *"Results embedded as non-extractable images; no extractable numerical data"*: Parser artifact — tables and figures exist as standard PDF images in the original submission.
- *"Pseudo matched node pairs leak the same information as ground-truth pairs"*: Misunderstands the paper's threat model. Pseudo pairs are derived from structural graphlet features (local topology) and do not contain identity information. The threat is about raw graph data leakage, not the matching output.
- *"DBLP results not reported"*: May appear in the appendix (Section A.5), which was stripped by the parser.
- *"Missing hyperparameter settings, GCN architecture details"*: Per the Reproducibility Statement (Section 7), these details are in the appendix (A.5), which was stripped.
- *"Missing related works on private entity resolution / private set intersection"*: Rule prohibits citing missing related works without external source verification.
- Various formatting, typographical, and garbled-text nitpicks: Parser artifacts, not author errors.
- *"K shared among clients means any client can decrypt others' data"*: While factually correct as a limitation of the specific encryption mechanism, it was raised as a fatal flaw rather than a design limitation worth noting in a discussion of failure modes. Relocated to the discussion of privacy analysis gap (Major weakness #1).
- *"Strength: MCMC graphlet enumeration with theoretical variance bound"*: The strength is valid but overstated; the bound's practical vacuity is now noted in Minor weakness #4.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide a formal privacy analysis with a clear threat model (honest-but-curious or otherwise), and either (a) justify why the linear transformation **K** provides meaningful protection, (b) adopt a stronger cryptographic primitive (e.g., secure multi-party computation or homomorphic encryption), or (c) temper the privacy claims to match what the mechanism actually provides.
2. Run a full ablation study removing each of the three main components.
3. Report all results with error bars over at least 5 random seeds with statistical significance tests.
4. Report communication cost and wall-clock time.
5. Consider adapting a centralized graph matching method into a federated setting via FedAvg as a more directly comparable baseline.

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>