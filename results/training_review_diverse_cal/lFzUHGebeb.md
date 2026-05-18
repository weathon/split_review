Now I have all the information I need. Let me carefully produce the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me draft this carefully.

---

I'll now write the final review with proper consideration of all the rules and verified facts.

For the **-kF-Bayes notation issue**: Looking at line 192, `k_{t+1} = k_t = x_t^T η_t x_t`. The reviewer says this is contradictory. Let me verify: if we set k_{t+1} = k_t AND k_t = x_t^T η_t x_t, then at step t+1, k_{t+2} = k_{t+1} = x_{t+1}^T η_{t+1} x_{t+1}. But k_{t+1} was set to x_t^T η_t x_t at the previous step. So k_{t+1} ≠ x_{t+1}^T η_{t+1} x_{t+1} unless x_t^T η_t x_t = x_{t+1}^T η_{t+1} x_{t+1}. The notation is genuinely problematic - either k is constant (k_{t+1}=k_t) or it's adaptive (k_t = x_t^T η_t x_t). It can't be both simultaneously unless all x_t^T η_t x_t are equal.

BUT - the Figure 2 shows k varying, which means the actual implementation does NOT have k_{t+1}=k_t as a constraint. So the written update rule contradicts the empirical results. This is a clear presentation error.

For the "Bayesian" label: the paper says "based on Bayesian learning" (line 16, 24, 268) and "based on Bayesian principles" (line 268). But there's no derivation from a Bayesian posterior, no prior over k, no marginal likelihood. The update k = x_t^T η_t x_t resembles a predictive variance but is not connected to any Bayesian framework. This IS an overclaim.

OK, now I'm confident in my assessment. Let me write the review.Now I'll produce the final consolidated review.

---

## Summary

This paper proposes Variable Forward Regularization (-kF), which generalizes Forward Regularization (-F) for online linear regression by introducing a scalar parameter \(k\) that controls the strength of the forward penalty term. The authors derive closed-form recursive updates for -kF, establish regret bounds (Theorems 4–5) showing that \(0<k<1\) yields a tighter bound than -F, and introduce -kF-Bayes as an adaptive variant that attempts to set \(k\) dynamically from the data. Experiments on simulated data, tabular benchmarks, and CIFAR-100 in class-incremental learning settings (using an edRVFL randomized neural network backbone) are presented to demonstrate the approach.

## Strengths

1. **Principled generalization of existing regularizers with provable advantage.** Remark 1 shows that -kF degenerates to Ridge (-R) when \(k=0\) and to Forward (-F) when \(k=1\). Theorem 5 gives an explicit expected regret bound, and Remark 4 shows that for \(0<k<1\) the growth rate of cumulative regret is strictly smaller than that of -F (Equations 17–19). This provides a theoretical argument that a properly chosen \(k\) yields a tighter adversarial regret bound than either prior method.

2. **Adaptive mechanism that eliminates manual \(k\)-tuning.** The -kF-Bayes variant (Theorem 6) determines \(k\) from the data (\(k_t = x_t^\top \eta_t x_t\)), and the empirical \(k\) variation curves (Figures 2, 4b) confirm that \(k\) does change over time. This is valuable because the paper's own experiments show that -kF with a fixed \(k\) requires expensive hyperparameter optimization (via SMAC3) for good performance, while -kF-Bayes is ready-to-deploy.

3. **Non-replay closed-form updates suitable for online learning.** Theorem 3 provides one-shot incremental updates for both parameters and learning rates without storing past data. This is critical for the online task-free continual learning (OTCIL) setting used in the experiments, where replay is forbidden.

4. **Broad experimental scope.** The paper evaluates on three distinct settings (numerical simulation, tabular CIL benchmarks, and CIFAR-100 image classification with a pretrained ResNet-56) and compares against several baselines (EWC, CRNet, DYSON, GEM, GSS, RanPAC, NICE), showing consistently favorable curves for the proposed methods across multiple figures.

## Weaknesses

### Fatal
None.

### Major

1. **The -kF-Bayes update notation is self-contradictory and the "Bayesian" label is unjustified.** Theorem 6 (line 192) states \(k_{t+1} = k_t = x_t^\top \eta_t x_t\). If \(k_{t+1} = k_t\), then \(k\) is constant across steps, contradicting the claimed adaptivity. If \(k = x_t^\top \eta_t x_t\) (which depends on \(t\)), then \(k_{t+1} = k_t\) cannot hold in general unless the quantity \(x_t^\top \eta_t x_t\) is stationary — which it is not, as the paper's own Figure 2 shows \(k\) varying. The written update rule is therefore inconsistent with the empirical behavior presented. Moreover, the method is called "-kF-Bayes" and described as "based on Bayesian learning" and "Bayesian principles," yet no actual Bayesian derivation is given: there is no prior over \(k\), no posterior computation, no marginal likelihood, and no connection to a Bayesian model. The quantity \(k = x_t^\top \eta_t x_t\) resembles a predictive variance from Gaussian process regression, but the paper does not derive it from any Bayesian objective. This overclaiming of the term "Bayes" and the contradictory notation together make the adaptive method poorly specified and its claimed adaptivity unverifiable from the paper alone.

2. **No tabular results are provided; all experimental claims rely solely on figures.** The paper reports that "edRVFL-kF and edRVFL-kF-Bayes outperform other methods on most datasets" and that they "achieve impressive results," but no tables with mean accuracy, standard deviations, or regret values are given. Figures 1, 3, 4, 5, and 6 show curves, but the absence of numerical tables makes it impossible for readers to precisely compare methods, assess the magnitude of improvements, or evaluate statistical significance across the 4-fold trials and repeated runs. This is a fundamental gap for a paper that aims to demonstrate practical efficacy. The paper even states that "our methods are noticeably more stable as indicated by the low stds," yet no standard deviation values are reported numerically.

3. **The regret bound is derived under an i.i.d. Gaussian assumption that conflicts with the paper's own motivation.** The paper motivates -kF by arguing that -F fails in practice partly due to "non-i.i.d. disturbance" and that "premise i.i.d. is not held in OL" (lines 14–15). Yet Theorem 5's bound (Remark 3, line 157) explicitly "assume[s] the entire \(\mathcal{X}\) respects independent identical Gaussian distribution in proof, which allows us to involve approximation \(\mathbb{E}[x_{t+1}^\top \eta_t x_t] = 0\)." This means the bound is proven under precisely the assumption the paper argues should be relaxed. Remark 3 acknowledges that "the regret bounds are fluctuating" and that the bound is approximate, which partially mitigates the concern but does not resolve the fundamental tension: the theoretical guarantee does not cover the non-i.i.d. setting that the paper targets. The paper also notes "Our future studies will focus on concrete regret bounds of -kF under stochastic setups" (line 268), suggesting the authors are aware this is unfinished.

4. **The extension from linear regression to randomized neural networks is not specified, breaking the link between theory and experiments.** The theory is developed entirely for a single-layer linear model with weight vector \(\theta\). The experiments (Section 4.2) use a multi-layer ensemble deep random vector functional link network (edRVFL) and state that "we used \(-k\)F and -kF-Bayes algorithms to reconstruct" edRVFL, but no description is given of how the update equations (Theorem 3 or Theorem 6) are applied per layer, across the ensemble, or in conjunction with the random projections. Are the updates only applied to the output layer weights? To all layers? How are the random features handled? Without algorithm pseudocode or any specification, the experimental results cannot be interpreted as a validation of the theoretical contribution.

### Minor

1. **"Learning dissipation" is used without definition.** This term appears at lines 16 and 242, where the paper states that -kF "has less learning dissipation" and that the proposed methods are "better suited to this situation because no learning dissipation in theory." The concept is never defined or explained, making the claim nearly meaningless.

2. **No ablation study varying \(k\) to validate the theoretically predicted range \(0<k<1\).** Remark 4 derives that \(0<k<1\) yields tighter bounds than -F, and the paper claims "such \(k\) values exist with a high probability" (line 129). Yet the numerical simulation (Section 4.1) only tests \(k \in \{0.2, 0.4, 0.6, 0.8\}\), and the tabular experiments use SMAC3 to optimize \(k\). A simple synthetic experiment systematically sweeping \(k\) from 0 to 2 would directly validate the core theoretical prediction.

3. **No complexity analysis.** The -kF updates involve additional matrix-vector products and an extra matrix inverse compared to -F (Theorem 3). The paper does not discuss per-step computational complexity, which matters for practical deployment in online learning.

### Trivial

- The "Bayes" label in -kF-Bayes is misleading given the complete absence of Bayesian derivation. This could be addressed by renaming the method to something like "-kF-Adaptive" and reserving "Bayes" for a method that actually has a Bayesian derivation.

## Nice-to-Haves

- Providing precise numerical tables with mean accuracy, std, and regret values across all datasets and methods would greatly strengthen the empirical claims.
- A clear algorithm pseudocode for how -kF/-kF-Bayes is applied to edRVFL (or any randomized neural network) would bridge the theory-experiment gap.
- A derivation of the regret bound that relaxes the i.i.d. Gaussian assumption, or at least a clear separation of the tractable i.i.d. bound from an empirical discussion of non-i.i.d. robustness, would resolve the tension in Theorem 5.

## Removed Points

- **"No quantitative results" framing**: The harsh critic described the experiments as having "no quantitative results." This is overstatement — figures do contain quantitative information on their axes. The real issue is absence of tabular results, which is kept in Major.
- **Formatting/style nitpicks about equation numbering**: The harsh critic noted equations may be "out of sequence" and that the paper "occasionally uses 'where' to start a new clause." These are parser artifacts and/or minor presentation issues. Removed per the formatting nitpick rule.
- **Criticism about related work being "mostly lists without substantive comparison"**: This is a generic complaint that does not identify any specific missing comparison or factual error. Related work citations serve to situate the paper's contribution, which they do adequately.
- **Strength Finder's claim about "Adaptive Bayesian mechanism"**: The "Bayesian" part of this claimed strength conflicts with the verified weakness that no Bayesian justification exists. The adaptive mechanism is real, but the "Bayesian" label is removed from the strength.
- **Strength Finder's claim about "consistent empirical superiority" without caveat**: This framed as a definitive strength without acknowledging the lack of tabular support. The strength is kept but moved to the empirical scope strength with appropriate qualification.

## Novel Insights

Beyond the paper's own contributions — generalizing -F with a tunable \(k\) and providing regret bounds — the most interesting observation from the reviews is the tension between the theoretically established \(0<k<1\) range and the empirical observation that -kF-Bayes's \(k\) values (shown in Figures 2, 4b) sometimes fall outside this range. The paper notes that -kF-Bayes's \(k\) values "being in the range of the maximum and minimum \(k_t\) of -kF-Bayes is interesting," but it does not analyze whether -kF-Bayes violates the \(0<k<1\) condition and, if so, under what circumstances. Understanding when and why the adaptive \(k\) leaves the provably optimal range would be a valuable direction for future work. None beyond the paper's own contributions.

## Suggestions

1. **Fix the -kF-Bayes update notation.** Clearly specify whether \(k\) is updated stepwise (e.g., \(k_t\) as a function of time) or held constant. If adaptive, remove the spurious \(k_{t+1}=k_t\) equality and define \(k_{t} = x_t^\top \eta_t x_t\) (or whatever the intended update is) unambiguously.
2. **Either provide a genuine Bayesian derivation for -kF-Bayes or rename it.** The current name overclaims. If the method is a heuristic (which is acceptable), call it something like "-kF-Adaptive" and describe the update rule as a data-dependent heuristic.
3. **Add tables with mean accuracy, standard deviations, and cumulative regret values** for all datasets and methods alongside the figures.
4. **Provide algorithm pseudocode** showing how the linear regression updates are applied to the edRVFL architecture.
5. **Address the i.i.d. assumption gap** by either deriving a bound that does not require the i.i.d. Gaussian assumption, or by clearly stating that the theoretical bound is a best-case analysis under i.i.d. data and explicitly discussing robustness to non-i.i.d. settings separately.
6. **Define "learning dissipation"** if it is to be used as a technical term, or remove it.
7. **Add an ablation study** experimentally validating the \(0<k<1\) claim by sweeping \(k\) on synthetic data.

## Score and Decision

This paper identifies a real limitation of Forward Regularization and proposes a reasonable generalization with a tunable parameter \(k\). The theoretical regret bound (Theorem 5, Remark 4) demonstrating that \(0<k<1\) yields tighter bounds than -F is a genuine contribution. However, the paper has four major weaknesses that collectively undermine its claims: the -kF-Bayes method is presented with contradictory notation and an unjustified "Bayesian" label; all experimental results are in figures only, with no tabular data for verification; the regret bound relies on an i.i.d. Gaussian assumption that conflicts with the paper's own motivation; and the connection between the linear regression theory and the neural network experiments is unspecified. These issues are addressable but prevent acceptance in the current form.

**Originality**: Good — generalizing -F with a tunable \(k\) is a natural but underexplored direction.
**Quality of claims**: Weak — claims about -kF-Bayes's Bayesian adaptivity are overclaimed and the notation is self-contradictory; experimental claims lack numeric support.
**Soundness**: The theoretical derivation has merit but is limited by the i.i.d. assumption; the experiments lack sufficient detail to verify the claimed results.
**Clarity**: Below average — contradictory notation in Theorem 6, undefined "learning dissipation," missing pseudocode.
**Value to community**: Moderate — the idea of tuning forward regularization strength is practically relevant, but the paper needs substantial revision to be usable.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>