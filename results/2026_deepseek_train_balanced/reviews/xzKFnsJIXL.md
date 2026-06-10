## Summary

This paper proposes gradient-crafting adversaries for privacy auditing of DP-SGD in the hidden state (final-model-only) threat model. The key contributions are: (1) at every-step insertion (k=1), gradient-crafting adversaries match the theoretical privacy upper bound on over-parameterized models, establishing that hiding intermediate models does not amplify privacy in this regime; (2) at sparser insertion frequencies (k>1), the approach outperforms prior loss-based adversaries but cannot match the upper bound; (3) a synthetic analysis with an adversary that also crafts the loss landscape suggests two regimes depending on batch size relative to noise variance.

## Strengths

- **Gradient-crafting for the hidden state model is a genuine methodological advance.** Prior gradient-crafting adversaries (Nasr et al., 2023) required access to intermediate models. This paper adapts the idea so the adversary commits to a gradient sequence *offline* without ever observing intermediate updates (Section 4, lines 141–142). This decouples worst-case gradient leakage from the feasibility of crafting a canary that produces that sequence.

- **The k=1 tight audit is a clean, well-supported negative result.** Figure 1 shows that $\mathcal{A}_{GC}$-R (random biased dimension) matches the numerical accounting upper bound on ConvNet and ResNet across $C\in\{1,2,4\}$. The paper provides a mechanistic explanation (lines 202–203): in over-parameterized models, genuine gradients contribute $\mathcal{O}(C|B|/p)$ per dimension, orders of magnitude below the crafted magnitude $C$. This yields Implication 1 (line 211): hiding intermediate models does not amplify privacy when a data point is used at every step.

- **The simulated biased dimension adversary succeeds on low-dimensional models.** On the FCNN (68 parameters, Housing dataset), random dimension selection fails, but $\mathcal{A}_{GC}$-S — which pre-runs the algorithm to pick the least-updated dimension — recovers nearly tight results with small variance (Figure 1c). This shows the approach generalizes beyond the over-parameterized regime.

- **Concrete diagnosis of why prior hidden-state adversaries underperform.** The paper identifies two specific limitations: (i) prior loss-based canaries fail to saturate the gradient norm, making performance architecture-dependent (Figure 1), and (ii) reliance on loss as a proxy confidence score. Both are grounded in empirical measurements (Section 4, lines 144–147).

- **The periodicity ablation cleanly isolates the effect of noise accumulation.** Section 5.3 varies $k\in\{5,25\}$ and shows the gap grows with $k$, with a clear explanation tracing it to noise accumulation during the $k-1$ non-insertion steps (lines 228–229). This motivates the landscape-crafting analysis.

## Weaknesses

### Major

- **The strongest claims about non-convex privacy amplification rest entirely on a synthetic one-dimensional abstraction, not validated on any real neural network.** Section 6 introduces a stochastic process (Equations 248–254) with an adversarially chosen threshold function $g$ that abstracts the loss landscape. From this, the paper draws two implications: (i) tight audit at large batch sizes — "the privacy accounting of DP-SGD is tight" (Implication 2, line 289) — and (ii) privacy amplification at small batch sizes that is "qualitatively weaker than in the convex case" (Implication 3, line 297). The paper further states at line 311 that the converging privacy loss property "cannot hold for non-convex models in the general case." All of these conclusions are drawn from a model where the adversary can *arbitrarily choose the loss landscape* — a capability far exceeding what the hidden state threat model grants for any fixed architecture and dataset. The paper acknowledges this gap once in the Discussion (line 315: "it seems unlikely that this point could also maximally bias subsequent genuine gradients"), but this acknowledgment is in tension with the definitive tone of the implications. **No experiment on any actual neural network demonstrates the claimed two-regime behavior.** This is a structural issue: the paper's most novel claim about non-convex DP-SGD is supported by the weakest form of evidence.

- **The synthetic analysis studies a different setting than the experimental gap it purports to explain.** The gap that motivates Section 6 arises from the periodic-insertion experiments ($k=5, 25$). However, Section 6 considers a single-insertion scenario (crafted gradient inserted only at step 1, then $T-1$ steps without). The paper acknowledges this "for simplicity" (line 244) but never bridges the gap between the two settings. It is unclear whether the two-regime finding from the single-insertion abstraction informs the periodic-insertion setting, or whether periodic insertion would produce qualitatively different behavior.

### Minor

- **Claims are stated more strongly than the evidence warrants.** The introduction claims "strong evidence of privacy amplification for non-convex problems" (line 32), and the discussion asserts that the converging privacy loss property "cannot hold for non-convex models in the general case" (line 311). The former overstates what is a purely synthetic observation; the latter presents a definitive conclusion from an abstraction. The paper would be more accurate to describe these as hypotheses suggested by the synthetic model.

- **Limited experimental scope.** Two datasets (CIFAR10, Housing) and three architectures (ConvNet, ResNet, FCNN) are used. The ConvNet and ResNet k=1 results (the paper's strongest evidence) lack error bars or variance reporting — only the FCNN results (Figure 1c) show variance across runs. For a paper making tightness claims, statistical noise quantification would strengthen the conclusions.

- **Number of auditing runs $R$ is not reported.** Algorithm 1 takes $R$ as input, but the experimental section does not specify it, making it harder to assess the reliability of the reported lower bounds.

### Trivial

- Remark 5.1 (lines 232–235) reads as an unfinished note; it can be expanded or removed.

## Nice-to-Haves

- Validate the two-regime finding from Section 6 on an actual DP-SGD training run — even a small neural network with systematically varied batch size and $\sigma$ — to connect the synthetic abstraction to real non-convex DP-SGD.
- Report confidence intervals for the ConvNet and ResNet k=1 results to support the tightness claims.
- Explicitly discuss how the single-insertion synthetic analysis relates to the periodic-insertion setting studied in the real experiments.

## Removed Points

These points were raised by reviewers but are removed after verification against the paper:

- *"No formal argument exists for claims about an open theoretical problem"* (Harsh Critic Issue 2): The paper is an empirical auditing paper, not a theoretical one. Demanding a mathematical proof for what is framed as an empirical investigation demands evidence outside the paper's stated scope.
- *"The paper fails to note that known mini-batches isolate subsampling effects"*: The paper explicitly acknowledges this at line 138 ("allows to isolate the impact of concealing the intermediate models from other factors"). The criticism misreads the paper.
- *"Remark 5.1 is an incomplete/unfinished note"*: The remark is a complete sentence; any formatting issues are parser artifacts.
- *"The paper's importance is a strength"* (generic Strength Finder entries about the problem being important): Removed as superficial — these do not constitute concrete evidence of contribution.
- *"The gap between real experiments and synthetic analysis is never acknowledged"*: The paper does acknowledge the setup difference (line 244) and the limitation (line 315).

## Novel Insights

The review synthesis reveals a recurring disconnect between the paper's two components. The cleanest and most defensible contribution (tight k=1 audit) is a negative result confirming existing upper bounds are tight — showing that hiding intermediate models provides no additional amplification when a data point participates in every step. Meanwhile, the paper's most eye-catching positive claim (privacy amplification occurs at small batch sizes for non-convex problems) has the weakest evidence, resting entirely on a one-dimensional synthetic abstraction. This asymmetry — where the strongest claims have the weakest support — is not adequately flagged by the paper's presentation.

## Suggestions

1. **Recalibrate the claims from Section 6.** Present the two-regime behavior as a hypothesis suggested by the synthetic abstraction, not as a finding about DP-SGD. The abstract and conclusion should reflect this distinction.
2. **Bridge the periodic/single-insertion gap** either by extending the synthetic analysis to periodic settings or by explicitly acknowledging the disconnect and discussing when the single-insertion results are likely to transfer.
3. **Add error bars to the ConvNet and ResNet k=1 figures** to support the tightness claims.
4. **Report the number of auditing runs $R$** used in experiments.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>