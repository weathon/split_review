- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3
Now I have all the information I need. Let me construct the final consolidated review, carefully separating valid weaknesses from those that should be removed.

---

## Summary

This paper studies federated compositional optimization (CO), focusing on the DRO formulation. It first proves that vanilla FedAvg fails for federated CO (Theorem 4.1), then proposes two algorithms: **FedDRO**, which adds low-dimensional communication of inner-function estimates to control bias, achieving O(ε^{-2}) sample and O(ε^{-3/2}) communication complexity; and **DS-FedDRO**, which uses two-sided learning rates to eliminate the additional communication, achieving O(ε^{-2}) sample and O(ε^{-1}) communication complexity (matching the best known for non-compositional FL). Both algorithms avoid accuracy-dependent large batch gradients and achieve linear speedup with the number of clients.

## Strengths

1. **First negative result for FedAvg on federated CO.** Theorem 4.1 formally establishes that vanilla FedAvg — with either intermittent or no sharing of inner-function estimates — cannot converge for federated CO problems. This provides a clear theoretical motivation for why new algorithmic designs are needed, and is the first such impossibility result for this setting.

2. **FedDRO achieves optimal sample complexity with practical batch sizes.** Corollary 4.4 gives O(ε^{-2}) sample complexity (linear speedup) and O(ε^{-3/2}) communication complexity. The hybrid momentum estimator (equation (8)) avoids the accuracy-dependent large batch gradients required by prior work (Huang et al. 2021, Haddadpour et al. 2022), which is a genuine practical advantage.

3. **DS-FedDRO matches the communication complexity of non-compositional FL.** Corollary 5.3 achieves O(ε^{-1}) communication complexity — matching the best known for standard (non-compositional) federated learning (Zhang et al. 2021, Acar et al. 2020) — via two-sided learning rates that avoid per-iteration communication of inner-function estimates. This is a meaningful theoretical advance.

4. **Addresses a genuinely harder setting than prior distributed CO work.** Remark 2.1 clearly distinguishes the paper's formulation — where the compositional function *g* is distributed across clients — from the setting in Huang et al. (2021) and Gao et al. (2022) where *g* is local per client. The distributed compositional setting introduces additional heterogeneity in the inner function and models realistic FL scenarios.

5. **Candid discussion of limitations.** The paper explicitly acknowledges the trade-offs between the two algorithms: DS-FedDRO's improved rates come with stronger assumptions (Assumption 5.1, bounded function-value heterogeneity) and additional tuning parameters, while FedDRO requires extra low-dimensional communication but weaker assumptions.

## Weaknesses

### Fatal
None.

### Major

1. **Central claim of communication efficiency is not empirically validated.** The paper's title and abstract foreground communication efficiency, and the theoretical contributions are rates of O(ε^{-3/2}) and O(ε^{-1}) communication complexity. Yet no experiment measures communication rounds required to reach a target accuracy, nor plots convergence against communication cost. The experiments show accuracy vs. time/rounds but do not isolate the communication savings the theory predicts. Additionally, the linear speedup claim (which requires varying the number of clients *K*) is not demonstrated — all experiments use exactly 8 clients. A reader cannot verify whether the theoretical improvements materialize in practice.

2. **Only one distributed baseline (GCIVR) on one dataset.** The Adult dataset experiments compare against GCIVR, a distributed method, but the main CIFAR experiments compare only against *centralized* baselines (FastDRO, PDSGD, MBSGD) run in parallel with I=1. While the paper explains this setup, it means the primary experiments do not isolate the effect of the proposed communication strategies versus a federated competitor. The distributed CO setting is the paper's claimed novelty, so more distributed baselines (or adaptation of existing methods to this setting) would substantially strengthen the empirical case.

### Minor

1. **Theorem 4.1 states existence without an illustrative example in the main text.** The negative result that motivates the entire paper is stated as an existence theorem with no concrete construction or intuition given in the main body. Even a brief one-dimensional example illustrating how local updates amplify bias would make the result accessible and compelling. (The full proof is likely in the appendix, which is stripped by the parser.)

2. **No error bars or variance reported.** The paper states results are averaged over 5 runs but does not report variance, confidence intervals, or show error bars in Figures 1–3. Given the small number of runs, this makes it difficult to assess whether observed performance differences are statistically meaningful.

3. **The condition on local updates for FedDRO (I ≤ O(T^{1/4}/K^{3/4})) is restrictive and its practical implications are not discussed.** While the paper notes this is a theoretical requirement, the bound is complex and no guidance is given for whether it allows realistically many local steps in typical settings. This matters for practitioners evaluating the method.

4. **DS-FedDRO's improved rates depend on a genuinely stronger heterogeneity assumption (Assumption 5.1 — bounded function-value heterogeneity) compared to FedDRO's gradient-level heterogeneity (Assumption 3.4).** The paper acknowledges this, which is commendable, but the comparison of the two algorithms' guarantees is not apples-to-apples. The claim that DS-FedDRO "eliminates the need for additional communication" is only valid under this stronger assumption.

### Trivial
None.

## Nice-to-Haves
- An ablation study showing sensitivity to the momentum parameter and learning rates would increase confidence in the method's robustness.
- A quantification of data heterogeneity (e.g., variance of local gradients or function values across clients) for the datasets used would help readers gauge the practical relevance of the heterogeneity assumptions.
- A baseline applying standard FedAvg directly to the DRO loss (ignoring compositionality) would illustrate whether the extra algorithmic complexity is necessary.

## Removed Points

These points are flagged to be removed; treat them with caution. A brief justification is given for each.

- **Lack of comparison to Huang et al. (2021), Gao et al. (2022), Guo et al. (2022):** The paper's Remark 2.1 explicitly states that these methods solve a *different* problem where the compositional function is local per client, not distributed. The paper explains that these algorithms cannot solve the setting in (2). The critic's suggestion that they "could be adapted" is speculative and unsupported. **REMOVED** — factually wrong criticism.

- **Centralized baselines "not how federated learning works":** The paper explains its comparison methodology (I=1, parallel implementation with matched gradient computation). This is a standard and reasonable way to compare optimization performance against centralized methods. The weakness about not isolating communication effects is already captured in Major weakness #2 above; the framing as a fundamental flaw is unwarranted. **MERGED into Major #2.**

- **GCIVR hyperparameters not reported:** The paper states "we adopt the parameter settings suggested in Haddadpour et al. (2022)" — i.e., the settings from the original GCIVR paper. This is standard practice for baseline comparisons. **REMOVED.**

- **"How exactly is the unbalanced CIFAR split among 8 clients?" / "What is the degree of heterogeneity?":** The paper states "split the (unbalanced) dataset equally for each client." The "unbalanced" nature refers to the CIFAR10-ST / CIFAR100-ST datasets themselves, which are class-imbalanced versions of CIFAR. The split is equally among 8 clients. This is sufficiently clear. The suggestion to quantify heterogeneity is a nice-to-have, not a weakness. **REMOVED** from weaknesses; kept as a nice-to-have suggestion.

- **"Comparison to a simple baseline that ignores compositionality":** The paper already includes MBSGD (minibatch SGD) and an "unconstrained" baseline for the Adult dataset, both of which ignore compositionality. This point is already addressed. **REMOVED.**

- **"The centralized baselines are effectively implemented with a batch size K times larger per client":** The paper explicitly states it uses "I=1 for FedDRO and implement[s] a parallel version of the centralized algorithms where the overall gradient computation is K times larger for each algorithm...to make sure that the overall gradient computations in each step are uniform across all algorithms." This is a deliberate and explained design choice for fair comparison. **REMOVED.**

## Novel Insights

The two reviews, taken together, surface an important tension: the paper's theoretical machinery is clean and makes precise predictions about communication savings, but the experiments do not measure the quantity the theory optimizes for (communication rounds to target accuracy). This suggests the paper would benefit from either adjusting its claims to match its experimental evidence or redesigning the experiments to directly validate the rates. The other notable insight from the reviews is that the two algorithms' theoretical guarantees are not directly comparable due to different assumptions (gradient heterogeneity vs. function-value heterogeneity), which the paper handles honestly but could discuss more prominently.

## Suggestions

1. **Add an experiment plotting communication rounds (high-dimensional parameter exchanges) vs. target accuracy** for FedDRO, DS-FedDRO, and at least one baseline. This directly validates the O(ε^{-3/2}) vs. O(ε^{-1}) claim.
2. **Vary the number of clients** (e.g., K = 2, 4, 8, 16) on a fixed total sample budget and plot iterations/communication rounds to a fixed accuracy to demonstrate the linear speedup claim.
3. **Provide a simple concrete example** illustrating Theorem 4.1 (e.g., a one-dimensional construction with 2 clients) in the main text or prominently in an appendix that the reader is directed to.
4. **Add error bars or variance bands** to all experimental figures and clearly state what measure of variation is used.
5. **Clarify the practical implications of the I ≤ O(T^{1/4}/K^{3/4}) condition** — provide a concrete numerical example showing what values of I are permissible for typical T and K.
