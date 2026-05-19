Now I have a thorough understanding of the paper and can verify/cross-check all reviewer claims. Let me write the consolidated review.

## Summary

This paper introduces the problem of **openset noisy labels in federated learning**, where each client's observed label space is a *subset* of the global label space and those labels are noisy. The authors propose **FedDPCont**, a framework combining (1) a differentially-private label communication mechanism that shares DP-protected labels among clients and (2) a contrastive loss that uses the recovered global label distribution to prevent local models from overfitting to their limited and corrupted label sets. Theoretical guarantees for both privacy (label-DP) and gradient alignment with centralized training are provided, and experiments on CIFAR-10/100, CIFAR-N, and Clothing-1M show consistent improvements over several baselines.

## Strengths

- **Formal problem definition with concrete failure analysis.** Section 3.1 formally defines openset label noise in FL (Definition 1) and provides a compelling worked example (the $T_{\mathrm{real}}$ vs. $T_{\mathrm{OptEst}}$ matrices) showing why loss-correction methods that require a noise transition matrix fail when the local label space is a subset of the global space. This clearly motivates the need for a different approach.

- **Principled DP guarantee for label sharing.** Theorem 1 (Section 4.1) proves that the symmetric-random-response mechanism used to flip shared labels satisfies $\epsilon$-label differential privacy, grounding the communication step in a well-established privacy framework.

- **Theoretical alignment with centralized training.** Theorem 2 (Section 4.2) proves that the aggregated gradient update of FedDPCont equals the expected centralized update under infinite data, providing a consistency justification for the distributed approach.

- **Consistent empirical advantage across benchmarks.** The paper evaluates against 8 baselines (FedAvg, FedProx, FedBN, FedDyn, Scaffold, LC, Co-teaching, T-revision) on CIFAR-10 and CIFAR-100 under multiple noise types and ratios, and extends to real-world noisy datasets (CIFAR-N, Clothing-1M). The claimed gains (e.g., +4–5% on high-noise CIFAR-100 settings) are substantial and consistent.

- **Empirical robustness to privacy budget.** Section 5.4 studies sensitivity to $\epsilon$ and shows stable performance across different privacy levels, corroborating the theoretical DP guarantee.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation study isolating the core components.** FedDPCont has two distinct ideas: (a) label communication to obtain a global label distribution, and (b) a contrastive loss using samples from that distribution. The paper does not ablate either. For example: What is the performance with label communication but standard cross-entropy (no contrastive term)? What is the performance with the contrastive loss but using only *local* labels (no communication)? Without these ablations, it is impossible to determine whether the gains come from both components working together or from one component alone, and the paper's central claim that *both* are necessary remains unsupported.

2. **No convergence analysis or training dynamics.** The paper reports only "best accuracy" over 300 communication rounds. There are no training curves (test accuracy vs. rounds), no loss curves, and no analysis of training stability. This is especially important given that the contrastive loss formulation ($\ell_{\mathrm{PL}} = \ell(f(x), \tilde{y}) - \ell(f(x), \check{y})$) uses a negative cross-entropy term: the paper should demonstrate empirically that training does not diverge or oscillate, and that the lower-unboundedness of the loss in theory is not a problem in practice.

3. **No statistical significance or variability reporting.** The paper states experiments are run "for 3 times with different random seeds" but does not report standard deviations, confidence intervals, or error bars. Without this, it is impossible to assess whether performance differences between methods are meaningful or within noise. This needs to be added for all numerical results.

4. **Theorem 2's limitations acknowledged but unaddressed.** The paper correctly notes that Theorem 2 applies "only...in the expectation level (infinite data size)" and that "the gap between distributed learning and centralized learning given limited data still exists." However, this gap — stemming from DP noise, local multi-step updates, and client sampling — is never analyzed or bounded. While it is reasonable for Theorem 2 to be a consistency result, the paper should discuss how these practical factors affect the approximation.

### Minor

1. **Real-world experimental results lack sufficient detail in text.** Section 5.3 describes the CIFAR-N and Clothing-1M results in only qualitative terms ("FedDPCont outperforms all the baseline methods"). While the full numerical results likely appear in a table (which may have been stripped by the parser), the prose should at minimum summarize the key numbers to make the section self-contained.

2. **No sensitivity analysis for key hyperparameters.** The paper fixes local update iterations $E=5$ and client fraction $\lambda=0.1$ without studying sensitivity. The impact of the openset generation matrix $Q$ (which controls how many classes each client misses) is also not varied. Understanding when the method helps most (e.g., when clients miss few vs. many classes) would strengthen the contribution.

3. **The gradient analysis of the contrastive loss deserves discussion.** The loss $\ell_{\mathrm{PL}}$ has a gradient $\delta_{\check{y},k} - \delta_{\tilde{y},k}$ that pushes the logit of the noisy label *up* and the logit of the contrastive label *down*. This is a very simple gradient that does not depend on the current model confidence. The paper references negative-learning works (Liu & Guo, 2020; Cheng et al., 2020) but does not discuss how the gradient behavior or convergence properties differ when sampling from the recovered global distribution (non-uniform) rather than uniformly from complementary classes. A brief analysis or discussion would help the reader understand the loss dynamics.

### Trivial
None.

## Nice-to-Haves
- A comparison against adapting centralized noisy-label methods that *do not* rely on the transition matrix (e.g., sample-selection or MentorNet-style approaches) could strengthen the claim that centralized methods "cannot work."
- An information-theoretic comparison quantifying how much less information the recovered label distribution leaks versus individual labels would strengthen the privacy discussion.
- Varying the degree of opensetness (fraction of missing classes per client) would give insight into the operating regime where FedDPCont is most beneficial.

## Removed Points

*"Contrastive loss is potentially unstable and conceptually ungrounded; can be driven to $-\infty$"* — **Removed** (with the training-dynamics part retained in Major Weakness 2). The specific collapse mechanism described (increasing confidence on the contrastive label while keeping the noisy-label loss finite) is not possible because softmax probabilities sum to 1. The gradient $\nabla\ell_{\mathrm{PL}} = e_{\check{y}} - e_{\tilde{y}}$ is a bounded vector ($\pm1$ on logits), independent of the current probabilities, so the loss cannot "trivially" diverge. However, the broader point about missing convergence/empirical stability analysis is valid and retained.

*"Missing FL noisy-label baselines (Yang et al., 2022; Xu et al., 2022)"* — **Removed**. The paper explicitly notes (Related Work, line 28) that these methods assume *identical* noisy label spaces across clients, which is a fundamentally different setting. Comparing against them would require non-trivial adaptation, and the paper reasonably scopes its evaluation to methods applicable to the openset setting.

*"Definition 1 is vague"* — **Removed**. While the definition ($\tilde{\mathcal{D}}_c \neq \tilde{\mathcal{D}}$) is compact, the surrounding generation process (lines 46–50) and the worked example (3-class $T_{\mathrm{real}}$ vs. $T_{\mathrm{OptEst}}$) clearly clarify its meaning (different label-space supports).

*"Theorem 2 novelty is limited"* — **Removed**. A consistency result that validates the distributed update approximating the centralized update is standard for FL algorithms but worth establishing. The novelty lies not in the theorem itself but in that it holds for the proposed loss and communication scheme, which is a non-trivial check.

*"Baselines are 'stacked' in favor of the proposed method"* — **Removed**. The baseline set includes FedProx, FedBN, FedDyn, Scaffold (heterogeneity methods) as well as LC, Co-teaching, T-revision (noisy-label methods). This is a reasonably comprehensive set. If the asymmetry existed, it favors the baselines (which are established methods), not the proposed method.

## Novel Insights

The reviews do not surface genuinely novel observations beyond the paper's own contributions. The most useful cross-cutting insight is that the paper's evaluation would benefit substantially from a clean ablation isolating the label-communication and contrastive-loss components, which would separate the contributions of each and directly test the paper's central claim.

## Suggestions

1. **Add an ablation study:** Compare (a) FedDPCont (full), (b) FedAvg with label communication but standard cross-entropy (no contrastive term), (c) FedAvg with the contrastive loss using only local labels (no communication), and (d) FedAvg baseline. This would isolate the effect of each component.

2. **Report training curves** (test accuracy vs. communication rounds) for a representative setting, along with loss curves to demonstrate training stability. Include standard deviations across runs.

3. **Add a non-private upper bound** ($\epsilon = \infty$) for the main results to quantify the privacy cost explicitly.

4. **Report standard deviations** for all numerical results, and add error bars to figures.

5. **Expand the real-world results section** to include explicit numerical comparisons in the text, even if the full table appears elsewhere.

## Score and Decision

**Overall assessment:** The paper identifies a real and underexplored problem (openset noisy labels in FL), proposes a creative combination of label communication with DP and a contrastive loss, and provides both theoretical justification and consistent empirical gains. The core weaknesses are evidential rather than structural — the method likely works, but the paper does not provide sufficient dissection (ablations, training curves, statistical significance) to convincingly attribute the gains to the claimed mechanisms or to rule out simpler explanations. These are addressable with revisions, but in the current form the evidence is incomplete.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>