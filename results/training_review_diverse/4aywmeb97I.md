Now I have thoroughly cross-checked every claim. Let me write the final consolidated review.

## Summary

This paper studies the convergence degradation in asynchronous federated learning caused by the joint effect of asynchronous delay and data heterogeneity. The authors (1) provide a convergence analysis of FedBuff under non-i.i.d. data, identifying a joint amplification term O(Kτ_maxτ_avgσ²_g/T); (2) propose CA²FL, which caches each client's latest update at the server and reuses it to calibrate global aggregation; and (3) prove that CA²FL removes this joint effect term and achieves a convergence rate matching synchronous FL. Experiments on vision (CIFAR-10/100) and language (GLUE) tasks support the theoretical claims.

## Strengths

- **Formally identifies the joint amplification of delay and heterogeneity.** The convergence analysis of FedBuff (Eq. 3.2) derives a term O(Kτ_maxτ_avgσ²_g/T) that explicitly quantifies how asynchronous delay and data heterogeneity compound to slow convergence. This provides rigorous motivation for addressing both factors jointly rather than separately.

- **Convergence guarantee that eliminates the joint effect.** Theorem 5.2 proves that CA²FL achieves O(1/√(TKM)) (matching synchronous FL rates), with the problematic joint term removed (Remark 5.4). The theory cleanly shows the cache mechanism, not just better hyperparameters or lower variance, is responsible for the improvement.

- **Ablation studies confirm reduced sensitivity to heterogeneity.** Figure 3(a)–(b) shows CA²FL's training loss fluctuates less than FedBuff's across varying data heterogeneity levels, directly corroborating the theoretical claim about mitigating the joint effect.

- **Efficiency simulation demonstrates practical speedup.** Table 4 shows CA²FL reaches target accuracy in fewer simulated time units than FedBuff and FedAsync across most settings, supporting practical advantage beyond final accuracy.

## Weaknesses

### Major

- **Undefined variant "MF-CA²FL" in the conclusion.** The final sentence (line 133) introduces "MF-CA²FL" as a method that "could largely save the memory overhead while maintaining the superior performance benefits from the cached update." This acronym appears *nowhere else* in the paper — not in the method section, not in the experiments, not in any table or figure. There is no description of what "MF" stands for, how it saves memory, or any experimental evidence. This is not a minor typo; it signals either a missing section or a draft-merge error that makes the paper feel incomplete. The authors must either define and evaluate this variant or remove all references to it.

- **Abstract/contribution statements overclaim given the empirical results.** The abstract claims "superior performances compared to other asynchronous federated learning baselines" and Contribution bullet 3 claims "superior performances." Yet the paper's own experimental section honestly acknowledges that FedAsync outperforms CA²FL on CIFAR-100 α=0.1 (52.46% vs. 48.30%) and on MRPC (85.54 vs. 83.69 accuracy). These are not "superior" across the board. The paper would be stronger if it explicitly characterized the regimes where CA²FL helps (high heterogeneity, vision tasks) and where it struggles (some language tasks, moderate heterogeneity) rather than making unqualified claims.

- **Statistical reporting uses within-run variation, not independent runs.** The paper reports "the mean accuracy and the standard derivation for the last 5 rounds" (line 100). This measures fluctuation over consecutive rounds of a *single* run, not the stability across multiple random seeds/initializations. For credible comparison in FL, experimenters should report mean ± std over 3–5 independent runs with different seeds. The current practice could obscure high-variance results and makes the reported standard deviations uninterpretable as measures of reproducibility.

### Minor

- **FedAsync performance on ResNet-18 (CIFAR-10) is not discussed.** The text (line 94) discusses FedAsync's non-convergence on the CNN model but says nothing about FedAsync's performance for the ResNet-18 model in the same table. Since the text states "We observe that the proposed CA²FL shows improvement upon the FedBuff and FedAsync" as a general claim about Table 1, but only provides detailed analysis for the CNN case, the reader cannot assess whether the pattern holds for the more modern architecture. The authors should explicitly state whether FedAsync was included in the ResNet-18 experiments and discuss its performance.

- **The cached update combination mechanism is underspecified.** The paper says the server uses the cached update for "global calibration" (lines 4, 11 in Algorithm 2), and the textual description (line 53) references line numbers of a pseudocode that was stripped by the parser. But even from the text alone, the exact operation — is the cached update averaged, weighted, or combined via some more complex rule? — is never stated explicitly. While the convergence analysis suggests the mechanism works, the experimental section would be stronger with a precise mathematical description of the calibration step.

- **The remaining bound term and trade-off are not discussed.** Theorem 5.2's bound still contains O((τ_max+ζ_max)σ²/T). The paper claims CA²FL "tackles the data heterogeneity issue" (Remark 5.4) but does not discuss the regime where this remaining term could dominate (e.g., when stochastic gradient noise σ is large). A brief discussion of when the theoretical advantage materializes would help readers understand limitations.

- **Missing experimental comparison with related caching-based methods.** The related work section discusses Gu et al. (2021), Yang et al. (2022), and SWIFT (Bornstein et al., 2023) — methods that also use cached/historical information. For a paper whose core contribution is caching stale updates, not comparing against the most directly related approaches weakens the empirical positioning. This is partially mitigated because some of these methods operate in different (synchronous or decentralized) settings, making direct comparison non-trivial.

### Trivial

- The learning rate grid (line 85) has a missing comma: "{0.001 0.01, 0.1, 1}".
- The target accuracies in Table 4 appear notably low (e.g., 0.2 for CIFAR-10 CNN — roughly 20% accuracy), though the reviewer cannot verify exact numbers from the image. If correct, the authors should explain why these targets were chosen, since they may not reflect practically meaningful performance levels.

## Nice-to-Haves

- Adding FedProx or FedDyn as synchronous FL upper-bound references would help calibrate how much of the heterogeneity challenge CA²FL closes relative to methods designed for the synchronous setting.
- A controlled synthetic experiment that varies heterogeneity (σ²_g) and delay (τ_max) independently would more directly validate the theory than the current mix of real datasets.
- A brief discussion of the server memory cost (N clients × model parameters) and how MF-CA²FL (if it exists) reduces it.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Reviewer claim that MF-CA²FL appears in the introduction/contribution bullets.** This is factually wrong. Checking lines 14–18, the introduction and contribution bullets mention only CA²FL. The reviewer's error does not invalidate the real problem in the conclusion, but the inaccuracy is removed.
- **Reviewer claim that the paper does not discuss mixed results.** The paper *does* acknowledge them (lines 96, 98). However, the *abstract and contribution bullets* still make unqualified "superior" claims, which is a separate issue kept above.
- **Criticism about missing algorithm pseudocode and assumption statements.** These are parser artifacts — the original submission contains them as images/latex that was stripped. The paper cannot be faulted for parser failures.
- **Missing related works as a structural flaw.** While some relevant caching-based methods are mentioned but not compared, this is scope-creep to demand experimental comparison with every related method, especially those in different settings (e.g., SWIFT is decentralized FL). Kept as a minor point above, not a structural flaw.
- **Formatting nitpicks (typos, missing commas in table description, etc.).** Parser artifacts; removed per instructions.
- **Strength Finder claim about "consistent empirical superiority"** — dropped because it conflicts with the verified weakness showing mixed results. Per rules: when a strength and verified weakness disagree, the weakness wins.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not identify any conceptual synthesis or pattern not already present in the paper.

## Suggestions

1. **Define MF-CA²FL or remove it entirely.** If it is a memory-efficient variant (e.g., compression or selective caching), describe it, show its experimental results, and compare it with the full CA²FL. If it was a draft artifact, delete all traces.
2. **Qualify the empirical claims** in the abstract and introduction to match the actual results. State clearly where CA²FL helps most (high heterogeneity, vision tasks) and where it does not consistently outperform baselines.
3. **Report experiments over 3–5 independent random seeds** with mean ± std across runs, not variation over the last 5 rounds of a single run.
4. **Explicitly discuss FedAsync's performance on ResNet-18** for CIFAR-10. If it was omitted, explain why; if it was included, report and discuss it.
5. **Add a precise mathematical description** of how the cached update is combined with the received update in the calibration step.

## Score and Decision

The paper's core contribution — identifying the joint amplification effect and proposing a caching-based remedy with convergence guarantees — is solid and well-motivated. The theoretical analysis is the strongest component. However, the empirical presentation is undermined by (a) an undefined variant appearing in the conclusion, (b) overclaiming in the abstract given mixed results, and (c) weak statistical reporting. These are fixable in revision but non-trivial. The paper represents a genuine contribution to asynchronous federated learning.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>