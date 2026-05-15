Now I have all the information needed to write the consolidated review.

---

## Summary

This paper introduces ExID, a method that integrates domain knowledge (given as decision trees) into offline RL via a teacher-network regularization term on the CQL critic loss. The teacher is first cloned from heuristic rules, then adaptively refined during training when the critic's own action has higher Q-value *and* lower uncertainty (MC-dropout variance) than the teacher's action. Experiments on OpenAI Gym, MiniGrid, a sales-promotion dataset, and simglucose show that ExID outperforms several offline RL baselines equipped with the same domain knowledge as a test-time fallback.

## Strengths

- **Novel and well-motivated problem framing.** The paper correctly identifies that existing offline RL algorithms (including CQL) handle OOD *actions* but provide no mechanism for OOD *states* not present in the training buffer. This is a genuine gap, and the paper's motivation (Fig. 1) is clear and compelling.

- **Pragmatic use of domain knowledge with adaptive teacher refinement.** ExID does not treat the heuristic as a fixed oracle. The teacher-update condition (Cond. 6) gates improvements on an uncertainty check, and the ablation in Fig. 5c confirms that the teacher-update mechanism contributes positively to overall performance. The sensitivity analysis on domain-knowledge quality (Fig. 6) is informative and provides practical guidance.

- **Reasonable experimental breadth.** The evaluation covers three dataset quality levels (expert, replay, noisy) across discrete OpenAI Gym environments, two MiniGrid layouts, a real-world sales dataset, and a medical simulator. The real-world case studies (Sec. 5.3) add credibility beyond synthetic benchmarks.

- **Direct evidence for the claimed mechanism.** Fig. 4 shows that ExID's Q-values stay closer to expert Q-values on OOD states than CQL's, supporting the claim that the regularization term mitigates Q-value divergence on unseen states covered by domain knowledge.

## Weaknesses

### Fatal

None.

### Major

1. **Missing error bars / variance reporting.** All numerical results (Table 1, Table 2, Fig. 5, Fig. 6) report only point estimates averaged over 3 seeds, with no standard deviations, confidence intervals, or individual run values. Many claimed advantages are modest (e.g., Cartpole Noisy: CQLD 175.33 vs. ExID 175.67 — effectively a tie), and without variance information the reader cannot assess which differences are meaningful. This omission undermines the core empirical contribution.

2. **Baseline comparison does not rule out simpler integration strategies.** The "D"-suffixed baselines inject domain knowledge only as a test-time fallback (use domain-knowledge action for states not in the buffer, otherwise use the learned policy; see p. 141). A natural and stronger baseline would be to *augment the training buffer* with synthetic trajectories from the domain knowledge (or add a BC regularizer directly to CQL — essentially ExID without the teacher-update mechanism). Without this comparison, it is unclear whether ExID's full pipeline (teacher cloning from uniformly sampled states, Q-difference regularization, uncertainty-gated teacher update) provides any benefit over simply mixing domain-knowledge data into the buffer and running vanilla CQL. The paper's claim of outperforming "ensemble of domain knowledge and existing offline RL algorithms" (abstract) is therefore not convincingly demonstrated against the most natural baseline.

3. **Overclaimed headline result.** The paper states that "ExID surpasses the performance by at least 27%" (p. 147). Without error bars and given the critic's examples where ExID loses or ties (Cartpole Expert: CQLD 193.33 vs. ExID 190.33; Cartpole Noisy: 175.33 vs. 175.67), this claim appears to be an average over favorable cases rather than a guarantee across all tasks. The strength of this claim cannot be evaluated without per-cell variance.

### Minor

4. **Teacher-training fidelity not validated.** The teacher is trained via behavior cloning on synthetic data uniformly sampled over state boundaries (p. 84). The paper does not report: (a) the teacher's agreement with the ground-truth decision tree on held-out states, (b) whether uniform sampling adequately covers the relevant decision boundaries, or (c) how sensitive downstream performance is to approximation quality. Since the teacher drives the regularization term, some empirical sanity check would strengthen the paper.

5. **Uncertainty-gating condition in Cond. 6 is not isolated in ablation.** The ablation in Fig. 5c separates "with teacher update" from "no teacher update" but does not isolate the effect of the uncertainty condition (i.e., removing the variance check while keeping the Q-difference check). It is therefore unclear whether the complexity of MC-dropout variance is warranted, or whether a simpler Q-difference-only gate would suffice. This is a modest gap — the overall ablation still shows the update mechanism is beneficial.

6. **DKQ, the closest prior work, is not compared experimentally.** The paper acknowledges DKQ (Zhang & Yu, 2021) as the most related method (p. 35) and distinguishes it on the grounds that it requires "action importance," which is harder to obtain. This distinction is reasonable, but an experimental comparison would substantially strengthen the case for ExID's design choices.

7. **Continuous-domain extension is stated but not evaluated.** The paper mentions extending ExID to continuous action spaces (p. 126) in a single sentence but provides no continuous-control experiments (e.g., D4RL MuJoCo tasks). All evaluations use discrete-action environments, so the continuous claim is unsupported.

### Trivial

- The role of Definition 4.1 (sub-multiset) is not clearly connected to the method that follows; it reads as a standalone description without driving later analysis.

## Nice-to-Haves

- **Data-augmentation baseline**: Adding synthetic domain-knowledge trajectories to the buffer and running vanilla CQL would directly test whether ExID's specific mechanisms are necessary.
- **Teacher accuracy on held-out states**: Reporting the trained teacher's agreement with the decision tree would add confidence in the teacher-cloning step.
- **Extended ablation**: Showing λ and k analysis on a second environment (beyond Lunar-Lander) and isolating the uncertainty condition would strengthen the understanding of design choices.
- **Q-value landscapes for more environments**: Extending Fig. 4 to additional domains would reinforce the mechanism claim.

## Removed Points

These points were identified by reviewers but are excluded from the main weaknesses for the following reasons:

- **"No error bars" was already listed above as Major** (this is not a removed point; it is a kept point). 
- Criticism about Definition 4.1 not being clearly connected: moved to Trivial as a presentation observation, not a substantive weakness.
- The reviewer's suggestion about testing with BCQ or REM as base algorithms: moved to Nice-to-Haves. The paper focuses on CQL as the base, and showing generality across base algorithms is a reasonable extension but not a flaw in the current submission.
- Generic "needs larger datasets" or "needs more environments" criticisms: the current set of environments (Gym, MiniGrid, real-world SP, simglucose) is adequate for the paper's scope.
- Any criticism about missing appendix content (proofs, hyperparameter tables, algorithm pseudocode): these are stripped by the PDF parser and exist in the original submission.
- The harsh critic's suggestion about "ablating λ and k across environments": moved to Nice-to-Haves — the current single-environment ablation (Lunar-Lander) is standard practice and adequate for a hyperparameter sensitivity study.

## Novel Insights

The reviews collectively surface a nuanced tension: ExID's core idea is genuinely valuable (domain-knowledge regularization for OOD states) and is supported by direct mechanistic evidence (Fig. 4), but the empirical case for its superiority over *trivial* domain-knowledge integration (data augmentation) is never made. The harsh critic's central challenge — "Is ExID better than just mixing domain-knowledge data into the buffer?" — is unanswered and is the most important open question. This is not a fatal flaw in the method but a gap in the experimental design that prevents the paper from conclusively establishing that its specific pipeline (teacher cloning + Q-difference regularizer + uncertainty-gated refinement) is worth the complexity.

## Suggestions

1. **Report standard deviations** over at least 5 seeds for all main results. If computational budget is a concern, even min/max ranges or per-seed scatter plots would be far more informative than the current point estimates.
2. **Add a data-augmentation baseline**: generate synthetic rollouts from the domain-knowledge decision tree, add them to the buffer, and run vanilla CQL. Compare against ExID to isolate the value of the teacher-regularization + update pipeline.
3. **Tone down the "at least 27%" claim** to a more precise statement (e.g., "on average across tasks" or per-dataset breakdown) and make clear where ExID does and does not improve.
4. **Report teacher accuracy** on a held-out validation set (both in-distribution and uniformly sampled states) so readers can assess the fidelity of the teacher approximation.
5. **Isolate the uncertainty gate in an ablation** by comparing (a) full Cond. 6 vs. (b) Q-difference-only update to show whether the variance check is necessary.

## Score and Decision

The paper tackles a real, underexplored problem with a novel, well-motivated approach. The core idea and the mechanistic evidence (Fig. 4) are valuable. However, the experimental validation has two significant gaps: (1) no error bars on any numerical result, making the reported improvements unverifiable, and (2) the absence of a comparison against the simplest training-time domain-knowledge baseline (data augmentation), which leaves unclear whether ExID's specific pipeline justifies its complexity. These are evidential, not structural, flaws — the method itself is promising — but they prevent the contribution from being conclusively supported in its current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>