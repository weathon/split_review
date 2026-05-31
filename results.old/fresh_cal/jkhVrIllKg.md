Now I have all the information I need. Let me compile the final consolidated review.

## Summary

This paper proposes SABER, a federated learning algorithm designed for heterogeneous data under a **second-order data heterogeneity (Hessian similarity)** assumption. SABER combines a bias-correction term (inspired by SCAFFOLD's control variates) with a proximal regularization term (from FedProx) in a **stateless** manner — it maintains a single shared control variate rather than per-client states — making it naturally support partial participation. The paper claims state-of-the-art communication complexity for nonconvex objectives ($O(\delta\varepsilon^{-2}\sqrt{M})$) and for objectives satisfying the Polyak–Łojasiewicz condition ($O((\frac{\delta}{\mu}\sqrt{M}+M)\log\frac{1}{\varepsilon})$). Experiments on logistic regression, CIFAR-10, and FEMNIST compare SABER against FedAvg, FedProx, and SCAFFOLD.

## Strengths

1. **Novel stateless algorithm combining desirable properties.** SABER maintains only a single shared control variate $\mathbf{v}_k$ instead of per-client states (Section 3, Algorithm 1). This design makes it naturally support partial participation without the memory/staleness issues of per-client control variates. The derivation from the FedProx and SCAFFOLD subproblems (Section 3, equations (5)–(9)) is pedagogically clear and positions SABER within existing work.

2. **Well-motivated theoretical claims with explicit state-of-the-art comparisons.** The paper's stated rates (contributions bullet, lines 63–65) improve on SVRP's $O((\delta^2/\mu^2 + M)\log 1/\varepsilon)$ when $\delta/\mu \ge \sqrt{M}$, match SVRS, and — unlike SVRP and SVRS — do not require convexity. The motivation for second-order (Hessian) heterogeneity over first-order heterogeneity is concretely argued with a squared-loss regression example (Section 1, lines 50–52), showing that $\delta$ can be small even when labels differ, as long as input distributions are similar.

3. **Empirical improvement under high heterogeneity.** On CIFAR-10 with LDA $\alpha=0.1$, SABER achieves a $1.89\times$ speedup over FedAvg and $1.78\times$ over FedProx in rounds-to-accuracy (Table 2), and accuracy gains of 14.14 pp over FedAvg and 8.3 pp over FedProx (Table 3). These gains are shown under the highest heterogeneity setting, which directly targets the paper's claimed regime of advantage.

4. **Honest reporting of limitations in the logistic regression experiments.** The paper explicitly acknowledges that SCAFFOLD outperforms SABER on the logistic regression tasks (line 187), which lends credibility to the reporting — the authors do not cherry-pick only favorable results.

## Weaknesses

### Major

- **SCAFFOLD comparison fairness is inadequately documented, with suspicious results.** On CIFAR-10 ($\alpha=0.1$), SCAFFOLD achieves only 44.55% accuracy — substantially worse than FedAvg (48.61%) — which is unusual for this well-established method in heterogeneous settings. The paper does not specify how SCAFFOLD's control variates were initialized, updated, or which variant was used (standard SCAFFOLD vs. Scaffnew). With 1 local epoch per round, a single step size (0.01) for all methods, and random client sampling, SCAFFOLD's control variates may become stale. The paper reports tuning step sizes "for each method individually" only for logistic regression (line 187); for the deep learning experiments, a single step size (0.01) is used for all methods (line 180), which is unlikely to be optimal for each baseline. While SABER's advantages over FedAvg and FedProx stand even if SCAFFOLD were perfectly configured, the paper's claim of superiority "up to 4.04× over SCAFFOLD" cannot be verified without proper documentation of the SCAFFOLD setup.

### Minor

- **Results reported without error bars or variance.** All tables (Tables 2, 3) report single numbers with no indication of multiple runs, standard deviation, or confidence intervals. For a setting with random client sampling and SGD, single-run results can be misleading. Additionally, on FEMNIST, all methods converge to similar accuracy (around 73%), and SABER's advantage is only 0.15–0.36 pp — negligible without variance estimates.

- **Single step size for all methods on the deep learning experiments.** A single step size (0.01) is used for FedAvg, FedProx, SCAFFOLD, and SABER on CIFAR-10 and FEMNIST (line 180). Step size tuning is only mentioned for the logistic regression experiments. Different methods (especially SCAFFOLD) may require different learning rates, and applying a common step size may systematically disadvantage some baselines.

- **Incomplete presentation of Assumption 2.** The "inexact solution" assumption that the theory rests on is introduced but the two conditions it references are cut off mid-sentence (line 141), so the reader cannot verify the assumptions underlying the theoretical claims.

### Trivial

- The otherwise-clear Algorithm 1 has a line (5–6) whose formatting makes the "otherwise" branch ambiguous — the second case of the control variate update is not fully readable from the algorithm box.

## Nice-to-Haves

- The theory-to-practice gap acknowledged by the authors (lines 130–131: theory uses single client per round, experiments use 10 clients) is a common practice, but a discussion of how the guarantees degrade (or are preserved) under minibatching would strengthen the connection.

## Removed Points

These points were flagged but removed (with brief justification):

1. *"The core theoretical contribution is not present"* — The claimed rates are stated in the abstract and contributions section (lines 63–65). While Section 3.2 only contains Lemma 1 in the extracted text, this is attributable to parser truncation (Assumption 2 is cut off mid-sentence, suggesting lost content). The paper's central claims are present even if full proofs are deferred. Removed per the parser truncation rule.

2. *"Algorithm 2 not shown"* — The paper references Algorithm 2 for the full practical version. Its absence in the extracted text is a parser artifact. Removed per the parser truncation rule.

3. *"The paper does not directly compare to rates of SVRP/SVRS"* — Factually incorrect; the contributions (line 65) explicitly compare to SVRP and SVRS rates. Removed as factually wrong.

4. *"ResNet-18 is unusually large for FEMNIST"* — This is a subjective implementation choice, not a methodological flaw. Removed as a formatting/style nitpick.

5. *"Missing related works"* — Cannot verify absence of related works without external sources. Removed per instructions.

6. *"Questions about code release / reproducibility of cited references"* — All cited models, tools, and benchmarks are assumed to exist. Removed per hard rules.

7. *Generic concern sweeps* — The harsh critic's broad area sweeps (e.g., "could the metric be measuring a proxy?") without concrete anchors were removed per filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective on SABER that the paper itself does not already address or imply.

## Suggestions

1. **Fix the SCAFFOLD baseline documentation.** Provide the specific initialization and update scheme for SCAFFOLD's control variates, the variant used (standard SCAFFOLD or Scaffnew), and confirm whether the step size was tuned individually for SCAFFOLD on the deep learning tasks. If the current CIFAR-10 results for SCAFFOLD are reproducible with proper tuning, that should be demonstrated. If they are not, the comparison should be revised.

2. **Add error bars.** Report at least 3 independent runs with standard deviation or confidence intervals for all tables. This is especially needed for FEMNIST where performance differences are tiny.

3. **Tune hyperparameters per method on all tasks.** The deep learning experiments should follow the same protocol as the logistic regression experiments: tune the step size individually for each baseline and report the best configuration.

4. **Complete Assumption 2 in the main body.** The two conditions for the inexact-solution assumption must be fully stated for the theoretical claims to be verifiable.

5. **Clarify the control variate update in Algorithm 1.** The "otherwise" branch of the $\mathbf{v}_k$ update should be clearly written out.

## Score and Decision

**Overall Assessment:** The paper presents a well-motivated algorithm with a clear design rationale and stated theoretical advantages. However, the experimental evaluation has significant weaknesses that undermine confidence in the empirical comparisons: the SCAFFOLD setup is undocumented with suspiciously poor results, no error bars are reported, and a single step size is applied across methods on the main deep learning tasks. The paper's core contributions (the algorithm design and theoretical rates) are valuable, but the empirical evidence requires strengthening before it meets the standard for publication.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>