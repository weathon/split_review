## Summary

This paper empirically documents and theoretically analyzes the phenomenon that Sharpness-aware Minimization (SAM) yields greater generalization improvements over standard optimizers as models become more overparameterized. The authors demonstrate this trend consistently across eight workloads spanning vision, language, graph chemistry, and reinforcement learning domains with five architecture types. They attribute the effect to the complementarity between overparameterization (which enlarges the solution space) and SAM's implicit bias toward flat minima, and provide supporting theoretical results on Hessian uniformity, linear convergence under the PL condition, and test error bounds for two-layer networks. Additional experiments examine the role of label noise, sparsity, and regularization.

## Strengths

1. **Comprehensive and diverse empirical demonstration of the central trend.** The paper evaluates eight workloads across five domains (synthetic regression, image classification on MNIST/CIFAR-10/ImageNet, POS tagging, sentiment classification, molecular property prediction, and Atari game playing) using five architecture families (MLP, CNN, RNN, GCN, Transformer). The finding that SAM's generalization benefit grows with model size is consistent across all of them (Figure 2, Table 1). This goes well beyond prior isolated observations and establishes the phenomenon at an unmatched scale.

2. **Clean mechanistic evidence from one-hidden-layer experiments.** The controlled experiments in Section 4.1 (Figures 3–4) show that with 10 neurons (underparameterized), SAM and GD converge to similar solutions, but with 100 neurons (overparameterized), SAM finds visibly simpler, flatter functions while GD does not. Trajectory plots confirm they reach different basins only in the overparameterized regime, directly supporting the proposed mechanism.

3. **Novel theoretical characterization of SAM's linearly stable minima.** Theorem 1 derives necessary conditions for linear stability of stochastic SAM, bounding higher-order Hessian non-uniformity terms ($s_2, s_3, s_4$) that are absent in the corresponding SGD analysis. This yields a testable prediction — SAM minima should have more uniform Hessian moments — which is empirically verified in Figure 6(a). The result connects SAM's implicit bias to a concrete spectral property.

4. **Convergence and generalization theory for SAM under overparameterization.** Theorem 2 establishes linear convergence for stochastic SAM under the PL condition and interpolation (both enabled by overparameterization), improving over the known $\mathcal{O}(1/t)$ rate. Theorem 3 shows that for two-layer ReLU networks trained by SAM, achieving $\varepsilon$ test error requires width $M \propto 1/\varepsilon$. These results extend overparameterization benefits previously proven for SGD to the SAM optimizer.

5. **Actionable practical insights.** The experiments on label noise (improvement grows from 5% to nearly 50% at high noise rates), sparsity (large sparse models outperform small dense ones), and regularization (weight decay, early stopping, and inductive bias are necessary to realize the benefit) provide useful guidance for practitioners deploying SAM at scale.

## Weaknesses

### Fatal

None.

### Major

1. **Unspecified $\rho$ tuning procedure for the main experiments (Section 3).** The paper's central empirical claim — that SAM's generalization benefit grows with overparameterization — is presented without specifying whether the perturbation radius $\rho$ was held constant or tuned per model size. Section 4.2 (Figure 5) later demonstrates that the optimal $\rho^*$ increases substantially with the number of parameters (e.g., from 4 to 256 filters in ResNet-18). If the main experiments used a single fixed $\rho$ across all model sizes, the observed trend could be partially confounded: smaller models would use a suboptimal $\rho$ and show less improvement, while larger models would operate closer to their optimal $\rho$. The paper defers to the appendix for experimental details, but this detail is central to evaluating the core empirical finding. **The authors need to clarify whether $\rho$ was tuned per model size in Section 3, or demonstrate that the trend survives when $\rho$ is individually optimized for each configuration.**

### Minor

1. **Theorem 2 largely inherits from the PL condition, and the paper could be more precise about what SAM specifically adds.** The linear convergence rate in Theorem 2 is driven primarily by the PL condition and interpolation assumptions, which are known to give linear rates for SGD and other first-order methods. The paper correctly states the assumptions (smoothness, PL, interpolation) but could more explicitly acknowledge that the dominant factor is the PL condition induced by overparameterization, and clarify what the SAM-specific rate dependence on $\rho$ contributes beyond what SGD would achieve under the same assumptions. Without this, the claim of "much faster convergence at a linear rate" in the abstract risks overstating the SAM-specific novelty.

2. **Missing variability information in the main figure.** Figure 2 presents single trend lines for each of the eight workloads without error bars, confidence intervals, or seed variability. Given that the strength of the central claim rests on the *consistency* of the pattern across diverse settings rather than statistical depth within any one setting, showing variability (even for a subset of workloads) would substantially strengthen credibility. The one-hidden-layer experiments use three seeds (Section 4.1) but the main multi-scale experiments do not report seed-level variation.

3. **The link between Theorem 1 and the empirical measurement of Hessian uniformity could be sharper.** Theorem 1 derives a *necessary* condition for linear stability involving bounds on Hessian non-uniformity ($s_2, s_3, s_4$). The empirical verification (Figure 6a) measures that SAM has "more uniform Hessian distribution." The connection is plausible but the theorem's forward implication is that linear stability *requires* bounded non-uniformity, not that SAM explicitly *pursues* it. Making this logical gap explicit would improve precision.

### Trivial

None.

## Nice-to-Haves

- **Systematic variation of overparameterization ratio in the one-hidden-layer experiments.** The current comparison uses only two points (10 vs. 100 neurons). Varying the ratio smoothly (e.g., 10, 20, 50, 100, 200 neurons) and measuring both function simplicity (number of linear regions) and sharpness (Hessian trace) would show whether the separation between SAM and GD grows *smoothly* with overparameterization.
- **Direct measurement of SAM's implicit bias strength.** Instead of using optimal $\rho$ as a proxy, fixing $\rho$ and measuring how much the SAM gradient deviates from the GD gradient (or the norm of the perturbation gradient term) as a function of model size would more directly test whether the implicit bias is amplified by overparameterization.
- **Discussion of remaining confounds.** Beyond linearization (which is ablated in Section 7), other factors change when models grow (effective learning rate dynamics, feature learning vs. lazy training, etc.). A brief discussion of which confounds are ruled out and which remain would strengthen the paper's internal validity.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Causal language overstatement"** — The critic claimed the paper overstates causal evidence. However, the paper uses appropriately hedged language ("we posit," "potentially due to," "it is observed"). The supporting evidence (one-hidden-layer experiments, solution space analysis, implicit bias measurements) is consistent with the claims made. The "critical influence" framing describes a well-supported pattern, not an unsubstantiated causal claim. This criticism is removed as a strawman that misreads the paper's careful hedging.

- **"Missing related works"** — Removed per instructions; cannot be verified without external sources.

- **"Linearization ablation is insufficient"** — The paper already includes a dedicated ablation (Section 7, lines 542–546) showing SAM underperforms SGD in linearized regimes by >10%, ruling out linearization as the explanation. This criticism ignores the existing experiment.

- **The Strength Finder's overly generic strengths** (e.g., "this paper addresses an important problem") — dropped per instructions when not backed by specific content.

## Novel Insights

The most insightful observation from cross-referencing the reviews is the tension between the paper's ambition (claiming a unified "critical influence" of overparameterization on SAM) and the fragmented nature of the three theoretical results (stability, convergence, generalization), each requiring different assumptions and not forming a single tight narrative. The harsh critic correctly notes that Theorem 2's convergence rate is less a distinctive property of SAM and more an inheritance from the PL condition — but this is itself an interesting point: it shows SAM *benefits from* the same overparameterization-enabled properties that help SGD, rather than SAM unlocking some completely new advantage. The paper's real contribution may be better framed as "overparameterization is *necessary* for SAM's implicit bias to manifest" (supported by the clean one-hidden-layer experiments) rather than "overparameterization *uniquely* amplifies SAM." The practical findings on regularization being a prerequisite are also underappreciated by the reviewers but add nuance that prevents an oversimplified takeaway.

## Suggestions

1. **Clarify the $\rho$ tuning procedure for Section 3** — this is the single most impactful fix. State whether $\rho$ was tuned per model size, and if not, show the trend holds when $\rho$ is individually optimized.
2. **Add error bars or seed variability to at least a representative subset** of the main Figure 2 workloads to strengthen internal validity.
3. **Explicitly acknowledge in Section 5.2** that the PL condition (not SAM) is the primary driver of linear convergence, and clarify what SAM-specific dependence on $\rho$ adds.
4. **Reframe the rhetorical emphasis** slightly: the strongest evidence is the cross-domain *consistency* of a *necessary condition* (overparameterization is needed for SAM to differentiate from SGD), which is more defensible than claiming overparameterization *uniquely* amplifies SAM's advantage.

## Score and Decision

Based on the paper's originality (documenting an underexplored but important phenomenon at scale), the importance of the research question (understanding when and why SAM works), the soundness of the experiments (addressable gaps but consistent evidence), and the value to the community (actionable insights for practitioners and theoretical foundations), the paper makes a solid contribution. The main weakness (unclarified $\rho$ tuning) is addressable and does not undermine the consistent cross-domain pattern. The theoretical results, while individually not decisive, provide useful supporting perspective.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>