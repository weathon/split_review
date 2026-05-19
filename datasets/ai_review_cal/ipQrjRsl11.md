- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 8, 5, 6, 6
Now I have all the information needed. Let me construct the consolidated review.

## Summary

This paper establishes a formal connection between ADMM-based and Variational-Bayes-based federated learning by showing that dual variables in ADMM emerge naturally as "site" parameters in Partitioned Variational Inference (PVI) when isotropic Gaussian approximations with a delta approximation are used. Using this connection, the paper derives two new algorithms: FedLap-Cov, which learns diagonal precisions as preconditioners, and FedLap-Func, which incorporates function-space information over unlabeled inputs. The theoretical derivation is sound and the proposed methods are well-motivated.

## Strengths

- **Formal derivation connecting two previously disconnected frameworks.** Section 3.1–3.2 provides a precise line-by-line correspondence between PVI and ADMM under isotropic Gaussian assumptions (Eqs. 6–8). The paper identifies the site parameters $\hat{t}_k(\mathbf{w})$ as the source of the linear dual term $\mathbf{v}_k^\top\mathbf{w}$, establishing a principled mapping that goes beyond the informal observation that both methods use local-global synchronization. The three remaining differences (separate $\delta$ and $\rho$ parameters, scaling by $N_k$, and the $q_g$ update lacking a $K$ division) are clearly enumerated, demonstrating intellectual honesty.

- **Competitive performance with fewer hyperparameters.** FedLap matches FedDyn across all datasets and heterogeneity levels (Table 1) despite having one fewer hyperparameter to tune (no local weight-decay). This is a practical advantage: Appendix D.1 shows FedDyn is sensitive to this additional hyperparameter, and FedLap removes the need to tune it. The practical simplicity is a concrete benefit of the Bayesian derivation.

- **New algorithms are well-motivated by the theoretical connection and show consistent (if modest) empirical trends.** FedLap-Cov (Section 3.3) introduces a learned second dual variable $\mathbf{V}_k$ acting as a preconditioner — a structure that follows naturally from relaxing the isotropic covariance assumption in the VB derivation. FedLap-Func (Section 3.4) incorporates function-space information while avoiding double-counting through a Hessian subtraction term. Across five heterogeneous settings in Table 1, FedLap-Cov shows accuracy improvements of 1.7%–5.9% over FedDyn on four settings, and FedLap-Func improves over FedLap on heterogeneous FMNIST and CIFAR-10. The results are consistent across 10-client and 100-client settings.

- **Communication and computation costs are explicitly characterized.** Each variant includes per-round communication cost (e.g., $2P$ for diagonal FedLap-Cov) and per-client computation complexity, giving practitioners clear guidance on overhead.

## Weaknesses

### Fatal
None.

### Major

- **The central empirical claims are not statistically robust.** Table 1 reports only 3 random seeds, and the paper acknowledges overlapping standard deviations by stating it "bold[s] the top two performing algorithms (even if their standard deviations overlap with others)" (line 230). Many reported improvements fall within one standard deviation of the baseline (e.g., UCI Credit heterogeneous: FedDyn 79.1(3.2) vs FedLap-Cov 81.5(1.4); FMNIST heterog. 10 clients: FedDyn 89.8(1.1) vs FedLap-Cov 91.6(0.4)). The paper uses "significantly improves" (line 238) to describe these results, but no statistical significance tests are provided. The empirical contribution of the paper is framed as demonstrating that the new VB-derived algorithms improve over ADMM baselines, yet the evidence is suggestive rather than conclusive. This does not undermine the theoretical contribution, but it weakens the claim that the connection "delivers" practically useful improvements.

- **The averaging-over-previous-3-rounds metric obscures final accuracy.** The paper reports average accuracy over the previous 3 rounds "to account for instabilities" (line 230). This nonstandard metric conflates convergence behavior with final performance. While the paper notes that max accuracy over the same window is reported in Appendix Table 2, the main results use the averaged metric, making direct comparison with typical FL reporting difficult. This alone is not a fatal issue, but combined with the 3-seed setup and overlapping standard deviations, it further reduces confidence in the empirical claims.

### Minor

- **The FedLap-Func algorithm sends client-data predictions to the server without adequate privacy analysis.** The paper acknowledges that sending predictions over client-selected points "breaks the strictest requirement of not sending any client data to the global server" and suggests it "might be reasonable to send a few random points having obtained prior permission" (line 236). However, no analysis of information leakage is provided — e.g., bounding the number of bits leaked, discussing whether the method can be made differentially private, or comparing against privacy-preserving distillation baselines. The paper does not report FedLap-Func results on FLamby-Heart "because of the sensitive nature of medical data" (line 236), which underscores that this is a genuine limitation. This does not invalidate the contribution but limits its applicability in privacy-sensitive domains.

- **The delta approximation is used without analysis of its impact.** Both FedLap and FedLap-Cov rely on a delta approximation (replacing $\mathbb{E}_q[g(\mathbf{w})]\approx g(\mathbf{m})$) and a second-order variant that requires the Hessian. The paper does not discuss the quality of these approximations in the federated setting or analyze how far the resulting algorithms can diverge from the true VB solution. An ablation comparing FedLap to a more faithful PVI implementation (without the delta approximation) would clarify whether the connection or the approximation is driving performance.

- **Overclaim in the novelty narrative.** The paper states "No prior work have shown the emergence of dual variables while estimating posterior distributions" (line 243). This is too strong: the paper itself cites Khan & Lin (2017) and Khan & Rue (2021), which relate natural gradients to dual averaging and mirror descent. The specific contribution — mapping VB site parameters to ADMM dual variables in federated learning — is genuinely novel, but the broader claim should be softened.

- **All clients are sampled every round.** The paper acknowledges this as future work (line 247). For large-scale FL, partial client participation is the norm, and the current favorable setting limits generalization of the conclusions.

### Trivial
None.

## Nice-to-Haves

- A wall-clock or FLOP comparison between FedLap-Cov and FedDyn. FedLap-Cov adds a Hessian computation (an extra backward pass per client), and knowing whether the accuracy-per-round gains translate to gains in total computation time would strengthen the practical case.
- Guidance on setting the $\tau$ hyperparameter in FedLap-Func beyond the general suggestion that $\tau>1$ may help when $\mathcal{M}_k$ is small.
- Confidence intervals or bootstrap-based significance tests for the main comparisons in Table 1.

## Removed Points

- *"The derivation is relegated to the appendix"* (Harsh Critic, Section 3.4 comment) — Removed per hard rule: missing appendix content is a parser artifact, not an author error.
- *"If FedDyn's additional weight-decay hyperparameter was not tuned as carefully, the comparison could be unfair"* — Speculative; the paper provides FedDyn sensitivity analysis in Appendix D.1.
- *"The datasets are small"* — Generic criticism; the benchmarks used (UCI Credit, MNIST, FMNIST, CIFAR-10) are standard in the FL literature.
- *"Connection claim is narrower than paper's framing suggests"* — The paper explicitly qualifies the connection ("with isotropic Gaussian covariances" in the abstract, three differences listed) and does not claim universal equivalence. The framing is appropriately scoped and the contribution is genuine.
- *Various formatting/presentation nitpicks* — Removed per hard rules on parser artifacts and style nitpicks.

## Novel Insights

The harsh critic and strength finder together surface an interesting tension: the VB–ADMM connection is simultaneously the paper's strongest contribution (the derivation is clean, explicit, and opens a new bridge between two literatures) and the source of its weakest evidence (the delta approximation that makes the connection tractable is also what the paper does not analyze). Neither reviewer identified a flaw in the derivation itself or suggested the connection is incorrect — the concern is entirely about how far the connection can be pushed beyond the isotropic-Gaussian-plus-delta setting. A genuinely novel observation that emerges is that the VB derivation naturally produces a form of preconditioning (FedLap-Cov's $\mathbf{S}_g$) that existing ADMM methods lack, and that the functional regularization viewpoint (FedLap-Func) connects ADMM-style FL to federated distillation — a link that the paper notes but does not fully exploit. These two directions (preconditioning through Bayesian covariances, and function-space knowledge transfer) are where the paper's framework has the most unexplored potential.

## Suggestions

1. **Strengthen the experimental evidence base.** Increase to 5–10 random seeds, report standard evaluation metrics (final-round accuracy alongside or instead of the 3-round average), and provide statistical significance tests (e.g., bootstrap confidence intervals or paired t-tests) for the FedLap-Cov vs. FedDyn comparisons. If the improvements are not statistically significant, frame the results as promising trends rather than definitive improvements.
2. **Add an analysis of the delta approximation.** Show analytically or empirically how far FedLap can diverge from the true PVI solution under the delta approximation. A small ablation comparing FedLap to a non-approximate PVI implementation would clarify the source of performance.
3. **Address the privacy limitation of FedLap-Func more seriously.** Either bound the information leakage, discuss differentially private variants (the paper cites Heikkilä et al. 2023 on DP-PVI), or explicitly scope the method to settings where the shared inputs $\mathcal{M}_k$ are public/unlabeled data rather than client data.
4. **Soften the novelty claim** on line 243 to acknowledge the existing connections between natural gradients and dual methods.
