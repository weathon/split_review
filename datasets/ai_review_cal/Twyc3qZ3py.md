- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5
Now I have sufficient information to produce the final consolidated review. Let me compose it.

## Summary

The paper proposes a probabilistic GNN that jointly infers the appropriate neighborhood scope (number of aggregation hops) and identifies important edges via a Beta-Bernoulli process combined with a feature-similarity kernel. The method models the expansion of neighborhood scope as a stochastic process, develops a variational inference algorithm to approximate the posterior of hop counts and GNN weights, and uses kernel-weighted edge sampling to preserve informative connections. Experiments on citation, co-author, and OGB datasets show competitive accuracy, better over-smoothing resistance, and improved calibration compared to several baselines.

## Strengths

1. **Novel integration of automatic depth selection with adaptive edge sampling.** The paper proposes a joint framework where a Beta-process-like prior over layers (Eq. 3–4) enables the model to infer the appropriate number of aggregation hops during training, while kernel-weighted edge sampling (Eq. 8) preserves semantically meaningful connections. The ablation study in Table 4 systematically validates both components: the beta process alone yields gains (e.g., +1.1% on Citeseer over vanilla GCN), and adding the kernel further improves and stabilizes performance.

2. **Demonstrated robustness against over-smoothing.** Figure 4 provides compelling evidence: as the truncation level increases, the proposed method maintains nearly flat accuracy while GCN, GCNII, DropEdge, and DropEdge++ all degrade sharply. Figure 3(a) additionally shows that the method preserves higher total variation in hidden representations compared to vanilla GCN, GCN+Dropout, and GCN+DropEdge, confirming the adaptive sampling's role in preventing over-smoothing.

3. **Better-calibrated uncertainty estimates.** The paper evaluates uncertainty quantification using both PAvsPU (Figure 5) and ECE (Table 6). On all three citation datasets, the proposed method achieves lower ECE than GCN, GCNII, and BBGDC (e.g., 0.018 on Cora vs. 0.061 for GCN), indicating that its predictive probabilities better reflect true likelihoods.

4. **Scalability to medium-scale graphs.** Table 3 reports results on five larger datasets (Flickr, ogb-Arxiv, ogb-Mag, ogb-Proteins, ogb-Products), where the method achieves competitive or best results. This demonstrates that the inference mechanism does not break down as graph size grows.

5. **Clear ablation isolating each component's contribution.** Table 4 systematically removes the skip connection, beta process, and kernel, showing that each component contributes meaningfully. The beta process alone outperforms vanilla GCN, and the kernel further stabilizes and improves results.

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical inconsistency between the variational distribution and the actual edge-sampling distribution.** The variational distribution in Eq. (6) defines Bernoulli/Concrete-Bernoulli masks with parameter π_l (uniform per layer). However, the actual edge sampling used during training (Eq. 8) replaces π_l with π_l · κ(x_n,x_n′)/Σκ(x_i,x_j), introducing node-similarity-dependent weights that break the layer-wise uniformity. The ELBO in Eq. (7) computes KL[q(Z|ν)||p(Z|ν)] against the prior of Eq. (4) (which assumes uniform π_l per layer), but the sampling distribution q̃ implied by Eq. (8) differs from the variational q(Z|ν) in Eq. (6). **This means the KL terms in the ELBO are computed against the wrong distribution, and the training objective no longer provably lower-bounds the true marginal likelihood.** The paper does not acknowledge or address this mismatch. This undermines the Bayesian theoretical justification of the method.

2. **Truncation T=2 in all main experiments severely limits the claimed "infinite neighborhood scope."** The paper explicitly motivates its approach as inferring an *infinite* count of hops via a Beta process, and the variational distribution in Eq. (6) claims a truncation that "can approximate the theoretical assumption of an infinite count." Yet the main experiments (Table 2, Table 3) use K=2 (stated in §4.2). With only two layers, the model can at most decide between a 1-hop and 2-hop neighborhood — a trivial decision. Figure 4 does explore larger T for robustness analysis, but the core accuracy results that support the method's claimed advantage over baselines use T=2. The paper does not justify why T=2 suffices, nor does it show that the method can infer a genuinely deeper scope when beneficial.

### Minor

3. **Missing critical baselines in accuracy comparisons.** The related work discusses DropEdge++ (a feature-dependent edge sampler) and methods like JK-Net and DeepGCN that also automate depth selection, but DropEdge++ is absent from the main accuracy table (Table 2) and the larger-dataset table (Table 3). It only appears in the over-smoothing analysis (Figure 4). Without comparing against these relevant automatic-scope methods, the paper's central claim of superiority over alternatives that require grid search is not fully substantiated.

4. **Absence of error bars / confidence intervals in the main accuracy table.** Table 2 reports only point estimates. On semi-supervised node classification with only 20 labels per class, variance across splits is substantial. The paper itself notes "no statistical significance between our method and GCNII on the Cora dataset," yet does not provide confidence intervals for any of the other entries. Table 4 (ablation) does report standard deviations, making the omission in Table 2 conspicuous.

5. **Several experimental details are missing.** The paper does not report: (a) the Concrete Bernoulli temperature τ, (b) the values of the Beta prior hyperparameters α and β, (c) how the KL divergence terms are computed (for a Concrete Bernoulli relaxation, the KL to a true Bernoulli is not analytically tractable and requires Monte Carlo estimation or approximation), and (d) the number of Monte Carlo samples used for the predictive distribution (Eq. 9). These omissions hinder reproducibility.

6. **The kernel is pre-computed on initial features and does not adapt during training.** The paper states that kernel values are pre-computed and not recalculated iteratively (§3.6). Since node features evolve through GNN layers, edge importance that is frozen at initialization may miss features learned later in training. The paper does not discuss or ablate this design choice.

7. **The "beta process" terminology is imprecise.** The stick-breaking construction in Eq. (3) (π_l = ∏_{j=1}^l ν_j, ν_l ∼ Beta(α,β)) is the standard representation for the Indian Buffet Process, not the standard definition of a beta process (which is a Lévy process with mean measure cπ^{-1}(1-π)^{c-1}dπ). While the construction is valid as a prior over decreasing activation probabilities, calling it a "beta process" adds unnecessary confusion. This does not affect the method's validity but should be corrected.

### Trivial
None.

## Nice-to-Haves

- An experiment demonstrating inference at larger truncation levels (e.g., T=8 or 16) on a dataset where deeper neighborhoods are beneficial (e.g., Coauthor Physics or ogb-Arxiv), with the learned π_l values reported.
- A case study or qualitative analysis showing that the kernel-weighted sampling preserves semantically meaningful edges (e.g., correlation with attention weights or ground-truth edge importance).
- A discussion of how the theoretical inconsistency (Weakness 1) might be resolved — e.g., by adopting a prior that matches the weighted sampling, or by reinterpreting the kernel weights as part of a data-dependent prior.

## Removed Points

- **"TV definition is unusual / may be reversed"** — The paper's TV definition (∥H − 1/|λ_max| A H∥_2^2) is a standard smoothness measure on graphs. The claim that "lower TV implies over-smoothing" is correct (when nodes become similar, TV decreases). The critic's concern is not valid given the definition provided. **Removed.**

- **"KL terms not expanded" as a structural flaw** — While the paper does not detail how KL terms for the Concrete Bernoulli are computed, this is a missing implementation detail, not a structural error. **Demoted to Minor (see Weakness 5).**

- **"Prior works claim is too broad" (about grid search)** — The paper discusses JK-Net and GCNII in the introduction as prior work but frames grid search as a limitation. This is a reasonable characterization of the landscape. **Removed as a strength/weakness — it is a framing choice, not a factual error.**

- **Strength about "computational cost comparable"** — The paper's Table 5 shows training time is 7.5× slower on Cora (1.5s vs 0.2s). While the overhead is modest in absolute terms, it is not negligible. The strength claim is overstated but not entirely wrong. **Demoted from explicit mention; the time analysis remains a positive point.**

- **"PAvsPU curves nearly overlap" speculation** — Without access to the actual figure with readable axis detail, the critic's visual assessment is speculative. The paper's own claim (and the ECE numbers in Table 6) supports the calibration improvement. **Removed.**

- **Various general/speculative "area-of-concern" sweeps** — E.g., "could the metric be measuring a proxy?", "assuming Y is the case…" — these are not tied to specific evidence in the paper. **Removed.**

## Novel Insights

The most interesting dynamic surfaced by the reviews is the tension between the paper's rich Bayesian machinery (Beta process, conjugate Bernoulli, structured variational inference) and the practical compromises needed to make it work (T=2 truncation, pre-computed kernels, unmatched variational objectives). This gap between the theoretical framing and the actual implementation is common in variational deep learning papers, but here it is particularly acute because the kernel-weighted edge sampling (Eq. 8) introduces a distribution mismatch that the paper does not acknowledge. The reviewers collectively identify that the method's empirical success likely derives more from the combination of skip-connections + regularized edge-dropping than from the Bayesian inference machinery per se — a hypothesis the ablation study (Table 4) partially supports, since even without the kernel the beta process alone improves accuracy. A focused follow-up could strip away the Bayesian scaffolding entirely and ask whether a simple two-layer GCN with learnable edge-dropping rates and a skip connection achieves the same results, which would delineate the actual contribution more cleanly.

## Suggestions

1. **Resolve the theoretical inconsistency.** Either (a) adopt a prior over edge masks that matches the kernel-weighted sampling distribution, (b) reparameterize the kernel weights as part of a data-dependent prior and derive the corresponding KL terms, or (c) if the kernel-weighted sampling is used only during the forward pass (not in the KL computation), state this explicitly and discuss the approximation error.

2. **Demonstrate inference beyond T=2.** At a minimum, run the method at T=4, 8, 12 on a dataset where deeper neighborhoods help (e.g., ogb-Arxiv or Coauthor Physics) and report the learned π_l values. If the method indeed stops activating unnecessary layers, this would be strong evidence for the core claim.

3. **Add DropEdge++ and at least one automatic-scope method (e.g., JK-Net with learnable aggregation) to the main accuracy table.** Include confidence intervals or standard deviations over multiple splits.

4. **Report all missing hyperparameters** (α, β, τ, temperature schedule, number of Monte Carlo samples, KL computation details) in the final version.

5. **Consider ablating the frozen kernel** — compare pre-computed vs. dynamically updated kernel values to test whether edge importance adaptivity matters.
