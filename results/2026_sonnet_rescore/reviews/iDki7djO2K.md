---

## Summary

"Forgetting is Everywhere" proposes a unified, algorithm- and task-agnostic formalism for forgetting in learning systems. The core idea: forgetting is a violation of *k*-step predictive self-consistency in a learner's induced futures (Definition 4.5), operationalised as a divergence measure called the *propensity to forget* (Definition 4.6). The formalism is validated empirically across regression, classification, generative modelling, class-incremental learning, and RL, and the paper argues that a moderate amount of forgetting improves learning efficiency. The framing is thoughtful and the theory is internally consistent.

---

## Strengths

- **Unified, algorithm-agnostic definition of forgetting.** The *k*-step consistency condition (Definition 4.5) cleanly separates forgetting from backward transfer (Desideratum 4.2) and from parameter drift (Desideratum 4.3), addressing a long-standing conflation in the CL literature. The general interaction framework (Definitions 3.1–3.6) casting supervised learning, RL, and generative modelling as instances of the same stochastic process is the structural backbone that makes this generality possible.

- **The Bayesian learner illustration (§5.1, Figure 2) is the most precise empirical contribution.** Equations (10)–(12) show formally that exact Bayesian updates satisfy the consistency condition, while diagonal Gaussian variational inference and gradient point estimates demonstrably violate it. Figure 2 makes this concrete and reproducible, directly supporting Takeaway 2 ("parameter changes alone do not imply forgetting"), which is one of the more counterintuitive and useful insights in the paper.

- **Theoretical justification for replay buffers.** The remark following Definition 4.5 — that when *u* depends on history *H*_{0:t−1}, the consistency condition requires access to past data — provides a principled, derivation-based rationale for replay, rather than the usual heuristic motivation.

- **Forgetting observed across paradigms (Figure 3).** The empirical result that ∑_k(t) is non-zero and dynamic even in i.i.d. settings substantiates the paper's framing that forgetting is not confined to CL or RL.

---

## Weaknesses

### Fatal
None.

### Major

- **The forgetting-efficiency trade-off (§5.3, Figure 4, Takeaways 3–4) conflates correlation with mechanism.** The momentum experiment (Figure 4, left) reports that "maximum training efficiency [occurs] at 0.9 momentum" and that this coincides with a particular level of forgetting. However, SGD momentum of 0.9 is well-known to improve convergence through standard optimization dynamics (noise reduction, faster progress through ravines) entirely independent of any forgetting mechanism. The paper establishes that forgetting and training efficiency co-vary with momentum, not that forgetting drives efficiency. To support the causal reading implicit in Takeaways 3 and 4, one would need an intervention that holds optimization dynamics fixed while varying the propensity to forget independently — e.g., a penalty directly targeting the consistency condition rather than varying a hyperparameter whose primary effect is on the optimizer. As stated, the evidence supports only correlation, not the claim that "effective approximate learners *utilise forgetting* as a mechanism for adaptive and efficient learning."

- **Empirical validation of the propensity-to-forget measure is weak.** §5.2 and Figure 3 demonstrate that Γ_k(t) is non-zero and varies over training across different settings — but non-zero is a very weak form of validation. The measure would be far better validated by showing it *ranks* algorithms in a discriminative way consistent with known forgetting properties: e.g., does it correctly order an EWC learner vs. naive fine-tuning on a standard CL benchmark? The class-incremental learning panel (Figure 3, right) shows an abrupt increase at a task boundary, which is the expected behavior, but does not show whether the magnitude or ordering between algorithms matches prior ground-truth measures. Without such discriminative evidence, the claim that the measure "allows empirical validation of our definition" (§6) is partially unsubstantiated.

### Minor

- **The RL takeaway is overstated for its experimental basis.** The conclusion that "forgetting is an essential component of RL" (§5.4) rests entirely on DQN trained on CartPole — a minimal environment with stationary dynamics and no task heterogeneity. CartPole's simplicity means the correlation between the forgetting curve and TD loss may not generalize to settings with genuine non-stationarity, sparse rewards, or multi-task RL. The observation that the two curves track each other is interesting but does not establish that forgetting *causes* or *enables* information acquisition at the level claimed.

- **The "first generalised definition" claim (§6) needs qualification.** The paper acknowledges its relationship to Fortini & Petrone (2019) and Fong et al. (2023); equation (10) is precisely the standard Bayesian posterior marginalization property, and the connection between the *k*-step consistency condition and the martingale property of Bayesian posteriors is not made explicit. The paper should clearly articulate whether Definition 4.5 is formally equivalent to existing predictive-Bayesian consistency conditions, or what specifically is added beyond their extension to non-Bayesian learners. The claim may be correct, but it is not adequately substantiated as written.

### Trivial

- The abstract's phrase "manifesting as a loss of predictive information" invites confusion with well-defined information-theoretic quantities (mutual information, entropy). The body correctly grounds the definition in KL divergence between predictive distributions; the abstract phrasing should match.

---

## Nice-to-Haves

- A one-paragraph sketch in the main body describing how q_k* is approximated in practice for neural network learners (even a high-level description of the estimation strategy) would help readers assess whether the empirical results depend on the validity of a tractable approximation. The details are in §SF of the supplementary material; a brief pointer with a sketch would strengthen Section 5 significantly.

- Adding a discriminative experiment — e.g., measuring Γ_k(t) for EWC vs. naive fine-tuning on a CL benchmark and confirming the measure correctly orders them — would substantially improve the validation of Definition 4.6 beyond showing it is non-zero.

- For the efficiency trade-off, an experiment that varies the propensity to forget through an explicit regularizer targeting the consistency condition directly (rather than indirectly through momentum or model size) would provide stronger evidence for the causal claim.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **[Removed per hard rule: supplementary/appendix stripped by parser]** The harsh critic's concern that "the approximation scheme for q_k* is entirely absent from the main body, making empirical validity unassessable" was grounded in the missing §SF. Since all papers have their appendices stripped during parsing, and §SF exists in the original submission, this is a parser artifact rather than an author omission. This concern is partially reflected in the "Nice-to-Haves" as a suggestion.

- **[Removed: scope creep]** The criticism that the paper should demonstrate generalization to "more complex RL environments with sparse rewards or multi-task settings" goes beyond the paper's stated empirical scope. The RL section's overclaim has been retained as a Minor weakness with appropriate calibration.

- **[Removed: generic strength]** The strength finder noted that "the paper addresses an important problem." Removed as generic.

---

## Novel Insights

The most genuinely novel observation in this paper — partially surfaced by the reviewers but not fully articulated — is that the *k*-step consistency condition provides a single unifying criterion that explains why three otherwise unrelated practical mechanisms (replay buffers, Bayesian updates, and exact inference) all mitigate forgetting: they are precisely the mechanisms that restore or maintain predictive self-consistency. This is a clean theoretical payoff that goes beyond prior ad hoc justifications for these techniques. The efficiency-forgetting trade-off hypothesis, while currently underevidenced, is also a potentially important reframing: it suggests that the goal for algorithm designers should not be to minimise forgetting unconditionally, but to find a regime where the amount of forgetting is *optimal for the learning task at hand*.

---

## Suggestions

1. **Strengthen the efficiency-forgetting experiment.** Design an intervention that directly modulates forgetting (e.g., a penalty on Γ_k(t)) while holding optimizer hyperparameters fixed. Even a small-scale version of this in the regression setting would partially deconfound the momentum result.

2. **Add a discriminative validation.** Measure Γ_k(t) on a standard CL setting for at least two algorithms with known ordering (e.g., replay vs. no-replay, or EWC vs. finetune) and show the measure correctly ranks them. This converts the validation from "non-zero" to "informative."

3. **Clarify the relationship with predictive Bayesian martingales explicitly.** A one-paragraph remark stating precisely whether Definitions 4.5 and (10)–(12) are equivalent to or strictly generalize the conditions in Fortini & Petrone (2019) and Fong et al. (2023) would adequately substantiate the novelty claim in §6.

4. **Soften the RL takeaway.** Replace "forgetting is an essential component of RL" with "these results suggest forgetting may be an essential component of RL," and flag CartPole as a preliminary illustration warranting study in richer environments.

---

## Assessment

**Originality:** The framing of forgetting as predictive self-consistency is novel in its generality; the mathematical machinery borrows from predictive Bayesianism but is extended meaningfully to non-Bayesian and RL settings.

**Importance of the research question:** High. A principled, unified notion of forgetting has been a gap in the field for decades.

**Claims supported:** Partially. The core formalism and Bayesian illustration are well-supported. The efficiency-forgetting trade-off is currently suggestive rather than established.

**Soundness of experiments:** Moderate. Coverage across paradigms is good; discriminative validity of the measure and causal interpretation of the efficiency-forgetting relation are not established.

**Clarity of writing:** Good. Definitions are precise, desiderata are well-motivated, and the narrative is coherent.

**Value to the research community:** Moderate-high. The unifying formalism and the replay justification are immediately useful; the efficiency-forgetting hypothesis opens a new design principle if better validated.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>