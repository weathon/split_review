Now I have all the information I need. Let me synthesize the final review.

## Summary

The paper proposes SABER, a federated learning algorithm that combines a global control variate with proximal regularization to mitigate client drift under second-order data heterogeneity (Hessian similarity). The main contributions are: (1) a stateless algorithm supporting partial participation, (2) theoretical communication complexity claims of O(δ ε^{-2} √M) for non-convex problems and O((δ/μ √M + M) log(1/ε)) under the PL condition — improving over SVRP when δ/μ ≥ √M, and (3) empirical validation on CIFAR-10, FEMNIST, and logistic regression against FedAvg, FedProx, and SCAFFOLD.

## Strengths

1. **Well-motivated problem and clean algorithm design.** The paper makes a clear case for why second-order data heterogeneity (Hessian similarity) is more appropriate than first-order bounded-gradient assumptions for concept-shift scenarios (Section 1, lines 34–50), giving concrete examples (linear regression, logistic regression). SABER's design — a single shared control variate v_k combined with proximal regularization — is clean, stateless (per-client), and supports partial participation.

2. **Strong theoretical claims with explicit comparison to prior work.** The paper states convergence rates that improve upon SVRP whenever δ/μ ≥ √M and matches SVRS, without requiring convexity (line 65). Table 1 provides a structured comparison of prior methods across dimensions (partial participation, general non-convex, stateless, second-order analysis). Lemma 1 provides a descent property relating progress to the control variate error.

3. **Empirical improvement in high-heterogeneity settings.** On CIFAR-10 with LDA α=0.1 (high heterogeneity), SABER achieves a 1.89× speedup over FedAvg and a 4.04× speedup over SCAFFOLD in rounds-to-accuracy (Table 2), and 14.14 pp accuracy gain over FedAvg under a fixed communication budget (Table 3). These results directly support the claim that SABER reduces client drift under data heterogeneity.

4. **Honest reporting of limitations.** The logistic regression experiments (Section 4.2) show SABER does not outperform SCAFFOLD, which the authors explicitly acknowledge and explain as consistent with SCAFFOLD's accelerated rate under well-tuned hyperparameters. This candor is commendable.

## Weaknesses

### Fatal
None.

### Major

1. **The convergence theory section does not contain formal theorem statements for the claimed rates.** Section 3.2 is titled "Convergence Theory" but presents only Lemma 1 (a descent property) and Algorithm 1. The abstract and introduction claim specific rates — O(δ ε^{-2} √M) for non-convex and O((δ/μ √M + M) log(1/ε)) under PL — but these are not formalized as theorems with explicit assumptions in the main body. For a paper whose central contribution is theoretical, the main text should contain the theorem statements whose proofs justify these claims. The current presentation makes it difficult to evaluate the paper's core contribution from the main text alone.

2. **Hyperparameter tuning is uneven across experiments.** The deep learning experiments (Section 4.1) use identical hyperparameters for all methods (stepsize 0.01, batch size 32, local epochs 1), while the logistic regression experiments (Section 4.2) tune the stepsize per method individually. This asymmetry raises concerns that the deep learning results may not reflect the best achievable performance of the baselines. A method's sensitivity to hyperparameters should be explored or at least discussed, and the choice of common hyperparameters should be justified.

### Minor

1. **No ablation study isolating the contributions of SABER's components.** The algorithm combines two elements: a control variate (bias correction) and a proximal term (regularization). Without ablations that remove or vary each component, it is unclear which part drives the empirical improvement. An ablation would also clarify how SABER differs from FedProx-only or SCAFFOLD-only variants.

2. **No sensitivity analysis for key hyperparameters.** The paper uses fixed values for the synchronization probability p=0.5 and the proximal coefficient η=0.5 across all experiments. No analysis is provided for how performance varies with these choices, making it difficult to assess the method's robustness to different settings.

3. **SCAFFOLD's large performance gap is not discussed.** On CIFAR-10 α=0.1, SABER requires 163 rounds vs. SCAFFOLD's 658 rounds (4× gap). While this favors SABER, the paper does not analyze whether this reflects a genuine advantage of SABER or simply suboptimal SCAFFOLD hyperparameters, especially given that all methods use the same stepsize and local epochs.

4. **No measurement or estimation of δ for the experimental datasets.** The theoretical results depend critically on the second-order heterogeneity parameter δ being small. The paper does not estimate or bound δ for any of the datasets, leaving the connection between theory and experiment unverified. This is common practice in optimization papers but worth noting.

### Trivial

- Algorithm 1's pseudocode appears to have an incomplete "otherwise" branch (line 159), likely a formatting artifact from PDF extraction rather than an omission in the original submission.

## Nice-to-Haves

- **Measure or bound δ** for the experimental datasets (or at least the gradient/Hessian differences) to connect the theoretical regime to the empirical one.
- **Include diagnostic experiments** tracking quantities like the norm of client drift, accuracy of the control variate estimate ‖v_k − ∇f(w_k)‖, or the effect of varying the proximal coefficient, to build intuition about why SABER works.
- **Compare against SVRP/SVRS** on smaller-scale problems (e.g., logistic regression) where they are tractable, to validate the theoretical advantage empirically.
- **Vary the synchronization probability p** and report sensitivity, since this controls the communication-computation trade-off.

## Removed Points

These points from the reviews are flagged for removal with justification:

- **"Algorithm specification is incomplete / missing 'otherwise' branch"** — The pseudocode truncation is a PDF-parser artifact; the text (line 94) and reference to Algorithm 2 (presumably in appendix) describe the control variate update. The single-client vs. subset discrepancy is explained at line 130 (theory uses single-client for simplicity; practice uses subsets).
- **"Missing SVRP/SVRS baselines in experiments"** — The paper explicitly scopes its empirical comparison to "standard baselines such as FedProx and SCAFFOLD" (line 66). The theoretical comparison to SVRP/SVRS is separate. Requesting additional baselines that the paper never claimed to include is scope creep.
- **"Logistic regression contradicts the narrative"** — The paper acknowledges and explains this observation (line 187). It does not claim universal empirical superiority; SABER's advantage is theoretically grounded and demonstrated in deeper/non-convex settings.
- **"Stateless claim is only half-true"** — The paper's phrasing "stateless by design" refers to per-client statelessness (no per-client control variate), which it clearly explains (line 86). The single global v_k is still a single scalar state, which is consistent with the claim.
- **Generic strengths from Strength Finder** — Some framing around "comprehensive empirical comparison" is somewhat inflated but not incorrect; retained as a tempered strength.
- **"Small δ is untested"** — Moved to Nice-to-Haves rather than treated as a weakness.

## Novel Insights

None beyond the paper's own contributions.

The main novelty is the synthesis: by adding a global recursive gradient estimator (in the style of MARINA/PAGE) to a proximal-regularized local subproblem (in the style of FedProx), the paper obtains a method whose communication complexity under second-order heterogeneity improves on SVRP (which requires convexity) while remaining stateless per-client. The conceptual insight — that combining bias correction with regularization avoids the per-client state burden of SCAFFOLD — is clear and well-articulated.

## Suggestions

- **Add formal theorem statements to Section 3.2** stating the convergence rates claimed in the abstract and introduction, even if proofs are deferred to the appendix. This is essential for a theory-contribution paper.
- **Add an ablation study** comparing SABER against variants without the control variate (FedProx-only) and without the proximal term (control-variate-only) to isolate the contribution of each component.
- **Conduct a hyperparameter sensitivity analysis** for p and η, and consider tuning baselines individually (at least stepsize) for the deep learning experiments.
- **Discuss or estimate δ** for the experimental settings to strengthen the theory-experiment connection.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>