Now I have sufficient calibration data. Let me produce the final review.

## Summary

This paper proposes SDQC, a framework for safe offline RL that decouples global observations into reward-related and cost-related representations via Q-supervised contrastive learning. Building on FISOR's HJ-reachability safety assessment, SDQC enables decision-making using different policies depending on whether the cost-representation assessment indicates safety, borderline safety, or unsafety. Theoretical analysis (Theorem 3.1) shows that Q*-irrelevance representations are coarser than bisimulation, yielding higher conditional entropy and thus better generalization. Experiments on DSRL benchmarks report zero-cost violations in the majority of 13 tasks and improved generalization under distribution shift.

## Strengths

1. **Novel and well-motivated problem framing.** The paper identifies a genuine OOD challenge in safe offline RL: global observations combine reward-related and cost-related information in unseen ways during test time. Decoupling these factors is a conceptually clean approach, distinct from prior methods that operate on the full observation. The UGV example (Figure 1) and the three-policy decision scheme (Figure 2, Section 3.3) concretely illustrate the idea.

2. **Q-supervised contrastive learning avoids model-estimation bottlenecks.** Representation learning in RL often relies on bisimulation, which requires estimating transition and reward/cost models — error-prone under sparse signals. SDQC replaces this with a contrastive loss supervised by learned Q-values, avoiding an explicit dynamics model. The paper explains the practical challenge of OOD actions in the offline setting and addresses it by sampling in-support actions from a pre-trained generative model (Section 3.2).

3. **Theoretical connection to representation coarseness.** Theorem 3.1 (Section 3.4) proves that bisimulation representations are finer than Q*-irrelevance representations, implying $H(s|\Theta_{\text{bisim}}(s)) \leq H(s|\Theta_{Q^*}(s))$. This provides a principled grounding for why a Q-supervised approach can yield better generalization than bisimulation-based methods. The extension from finite-horizon to infinite-horizon MDPs and inclusion of the safety Bellman operator is a meaningful technical contribution.

4. **Competitive empirical results on DSRL benchmarks.** The paper reports that SDQC achieves zero normalized cost on a majority of tasks, substantially improving over FISOR (the most relevant baseline). The generalization tests (Section 4.2, Figure 3) on CarGoal and CarPush with unseen configurations show SDQC maintaining near-zero cost while baselines degrade — this is the kind of OOD setting the paper is designed for, and the results support the central claim.

5. **Joint training of representations with Q-learning.** The contrastive loss is integrated as an auxiliary objective during value-function learning (Eqs. 8 and 12), avoiding a separate representation pretraining stage. The ablation (Section 4.3, Figure 4) confirms that removing this loss degrades both reward and cost performance, and the t-SNE visualization provides qualitative evidence that the loss indeed clusters states with similar Q-values.

## Weaknesses

### Major

1. **The theory-algorithm gap: the contrastive loss is not connected to the information-theoretic objective.** The paper sets up Eq. 4 (maximizing $H(s|z_\theta(s))$ subject to a Q*-preservation constraint) and then proposes a contrastive loss (Eq. 5) as the practical method. The connection between them is described only at an intuitive level: the paper states that Eq. 4 "can be achieved" by clustering states with similar Q* values and that contrastive learning "provides a promising solution." No formal derivation shows that minimizing Eq. 5 maximizes Eq. 4, nor that the learned representations satisfy the Q*-preservation constraint. The theoretical claim that "our Q-supervised contrastive learning method theoretically surpasses bisimulation" relies on Theorem 3.1, which is about Q*-irrelevance representations *in general* — but there is no argument that the specific representations learned by Eq. 5 actually correspond to a Q*-irrelevance representation (or approximately so). This leaves a gap between the theoretical framework and the implemented algorithm that reduces the paper's internal coherence. This is a significant concern because it is unclear whether the theory justifies the method or merely parallels it.

2. **Insufficient statistical evidence for safety-critical claims.** All results are reported as point estimates averaged over only 3 random seeds (20 episodes each). No standard deviations, confidence intervals, or significance tests are provided anywhere in the paper. For a method whose headline contribution is achieving "almost zero violations" — a safety-critical claim — this level of statistical evidence is inadequate. A single outlier seed could dominate the average. The generalization test results (Section 4.2) are described qualitatively ("SDQC is the only algorithm that ensures no increase in cost") without reporting numerical values, making them impossible to evaluate independently. This is the most impactful weakness because it undermines confidence in the paper's strongest empirical claims.

### Minor

3. **The main empirical results table is not machine-readable.** Table 1 is embedded as an image, so the actual numerical values (normalized return and cost per task per method) cannot be extracted. The paper states results qualitatively ("zero violations in the majority of tasks") but does not enumerate which tasks succeed, which fail, and by what margin. Providing the full table in the text would substantially improve verifiability.

4. **Ablation only compares with/without contrastive loss, not alternative decoupling methods.** The ablation (Section 4.3) compares SDQC with and without the contrastive loss, which shows that the loss helps but does not isolate whether the *Q-supervised decoupling* mechanism specifically is responsible for the gain, as opposed to the addition of *any* auxiliary contrastive objective. Comparisons against alternative decoupling approaches (e.g., random dimension split, bisimulation-based decoupling, or hand-crafted separation) would strengthen the claim that the Q-supervised logic itself drives the improvement. As presented, the improvement could also come from the general regularization effect of an extra loss.

5. **No analysis of failure cases.** The paper states that SDQC achieves "zero violations in more than half of tasks" but does not discuss which tasks failed, by how much, or why. Analyzing failure modes would help the community understand the method's limitations and when alternative approaches are needed.

6. **Stronger novelty claims than warranted.** The paper asserts it is "the first to utilize decoupled representations for decision-making in safe RL tasks" and "the first framework of state decoupling for safe decision-making." While the specific Q-supervised contrastive approach is novel, prior work on safe state abstractions, safety layers, and state decomposition in CMDPs exists (e.g., shielding methods, safe embeddings). The claims could be tightened to reflect the specific technical contribution rather than imply firstness in a broad space.

### Trivial

None.

## Nice-to-Haves

- **Hyperparameter sensitivity analysis.** Key parameters ($\delta$, $\eta$, $\nu$, number of anchor states) are not analyzed. Understanding sensitivity would aid reproducibility and deployment.
- **Computational cost comparison.** SDQC involves a pre-trained generative model, two contrastive losses, and three diffusion models. A runtime or parameter-count comparison with baselines (especially FISOR) would clarify the practical trade-off.
- **Quantitative evaluation of representation quality.** Metrics such as mutual information between $s_r$ and true cost (or $s_c$ and true reward) would directly test whether decoupling actually occurs as intended.

## Removed Points

- **Claim about generative model quality not being evaluated.** The paper references Appendix C.1 for details on the generative model. Since the appendix is stripped by the parser, this criticism cannot be verified from the available text. The rule to not penalize missing appendix content applies here.
- **Claim that the objective Eq. 4 is "conceptually inconsistent" (maximizing vs. minimizing conditional entropy).** The reviewer's argument is incorrect: maximizing $H(s|z)$ is equivalent to making the representation coarser (more states map to the same $z$), which is exactly what the paper aims to do. This aligns with cluster assignments increasing conditional entropy.
- **Criticism about Theorem 3.1 proof being deferred to appendix.** Standard practice for conference papers; the rule says to remove weaknesses about missing proofs in appendix.
- **Literature gap / missing related works.** The rules forbid mentioning missing related works as a weakness since external sources cannot confirm their existence.
- **Formatting and presentation nitpicks.** These reflect parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the theoretical narrative (Eq. 4 → Theorem 3.1) does not actually connect to the implemented algorithm (Eq. 5) is the most important insight to emerge from the review process. This is not a fatal flaw — many deep RL papers operate with informal theory-practice bridges — but it is a genuine structural weakness that the paper would benefit from addressing directly, either by deriving the loss from the objective or by relaxing the theoretical claims to match what the algorithm actually does.

## Suggestions

1. **Bridge the theory-algorithm gap.** Either (a) derive the contrastive loss from Eq. 4, for instance by showing that the InfoNCE loss lower-bounds a mutual information term that relates to the conditional entropy objective, or (b) reframe the theoretical claims as providing *motivation* rather than *justification* for the contrastive approach, and present Theorem 3.1 as a standalone result about representation coarseness that contextualizes the design choice. The current framing overclaims the theory-method connection.

2. **Increase statistical rigor.** Run at least 10 seeds for all main results and report mean ± std for both cost and reward. For the safety claims, report per-seed violation counts or cost distributions. Present generalization results in a table with numerical values rather than relying solely on a qualitative figure.

3. **Provide the full Table 1 as parseable text** rather than an image, and explicitly list which tasks achieve zero violations and which do not. Discuss failure cases.

4. **Add an ablation isolating the decoupling mechanism.** Compare against: (a) a single shared representation (no decoupling), and ideally (b) decoupling via random representation split or via a separately trained bisimulation model. This would isolate whether the Q-supervised contrastive *decoupling* is the source of gains versus the addition of a generic auxiliary loss.

5. **Validate the generative model.** At minimum, report the coverage or accuracy of the action-generation model (e.g., what fraction of the true in-support actions it captures) to substantiate that the contrastive loss is computed over a reliable action set.

## Score and Decision

**Bracketing (Round 1):** Three queries on safe offline RL and contrastive representation topics. Low band (score 0–3): papers at 2.0–3.0 (withdrawn/rejected). Middle band (score 4–7): papers at 4.0–5.0 (safe offline RL papers). High band (score 8–10): papers at 8.0+ (unrelated topics — e.g., rotation estimation, LLM agents). **Initial bracket:** 4.0 – 7.0, with the paper clearly in the lower half.

**Narrowing (Round 2):** Queries in [4.5, 6.5] and [5.5, 7.5] retrieved anchors at 4.5 (REP-PD, pure theory, no experiments — weaker than SDQC), 5.0 (SDGD, DSRL benchmark, similar statistical weaknesses — comparable to SDQC), 5.5 (PREFORL, offline contrastive RL, accepted Poster — slightly stronger), 6.0 (DQC, clean theory+experiments — stronger), 6.5 (DO-HJ-PPO, strong theory — stronger).

**Final score:** 5.0. Relative to the anchors: this paper is stronger than REP-PD (4.5) because it has an implemented system with empirical results. It is comparable to SDGD (5.0): both work on the DSRL benchmark, both have missing standard deviations identified as a weakness by reviewers, both have hyperparameter sensitivity concerns. It is weaker than PREFORL (5.5) and the 6.0+ papers, which either have tighter theory-experiment connections or more rigorous evaluation. The core idea is novel and promising, but the theory-algorithm gap and the weak statistical evidence (3 seeds, no confidence intervals) for safety-critical claims prevent the paper from reaching the 5.5–6.0 level. The paper requires substantial revision before publication.

**MY FINAL SCORE: 5.0**
**MY FINAL DECISION: Reject**