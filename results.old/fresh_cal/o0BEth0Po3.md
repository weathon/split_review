I have the full paper content from my earlier read. Let me now produce the final review.

---

## Summary

This paper proposes ExID, an offline RL algorithm that improves performance when data is scarce and confined to a subset of the state space. ExID incorporates imperfect domain knowledge through a teacher policy network, regularizes the critic's Q-values toward the teacher's actions on states matching domain knowledge (Eq. 3), and adaptively refines the teacher using the critic's own Q-values and uncertainty estimates (Cond. 6). The method is evaluated on OpenAI Gym, MiniGrid, a real sales promotion dataset, and a simglucose diabetes dataset, with ablations on the key design choices.

## Strengths

- **Novel regularization loss (Eq. 3) with clear motivation.** The paper identifies a genuine failure mode — offline RL critics overestimating OOD actions for states missing from the limited training buffer — and introduces a targeted regularization that penalizes the squared Q-value difference between the critic's action and the teacher's action on domain-knowledge-covered states. This directly addresses the diagnosed problem and goes beyond existing static domain-knowledge integration approaches.

- **Adaptive teacher improvement using critic confidence (Cond. 6).** The update condition requires *both* a higher expected Q-value *and* lower uncertainty (via MC dropout variance) for the critic's action relative to the teacher's. This mitigates the risk of updating the teacher based on spurious OOD Q-values. This adaptive refinement of an initially heuristic teacher is a genuine novelty over prior domain-knowledge methods such as DKQ, which treat heuristics as fixed.

- **Empirical evidence of OOD generalization (Fig. 4a,b).** The paper directly measures the Q-value difference between expert actions and the learned policy's actions for states not in the reduced buffer. ExID maintains a much smaller gap than CQL across both expert and noisy datasets, providing direct evidence that the regularization successfully generalizes to unseen states covered by domain knowledge.

- **Robustness analysis to domain knowledge quality (Fig. 6a,b).** The paper tests five domain rules of varying quality (average reward from 52 down to 11). Sub-optimal rules (Rule 3) match the performance of an optimal rule after training, and even relatively poor rules (Rule 4) still improve over CQL. This demonstrates that the method is not brittle to heuristic quality — a practically important finding.

- **Ablation isolating the teacher update contribution (Fig. 5c).** The comparison of "just warm start," "no teacher update," and full ExID on CartPole confirms that both the initial regularization and the adaptive teacher improvement are important, with the full method clearly outperforming the ablations.

## Weaknesses

### Fatal
None. The core idea is sound, and the experimental evidence broadly supports the method's effectiveness, even if some claims are imprecisely presented.

### Major

- **Unsupported headline performance claim ("at least 27% improvement").** The paper states in Section 5.2 that "ExID surpasses the performance by at least 27% in the presence of reasonable domain knowledge" without showing how this figure is computed. No aggregate improvement percentage is calculated in any table, and the claim's baseline comparison is ambiguous (best D-suffix baseline? average over all baselines?). Since the tables are images and the computation is not spelled out, this central quantitative claim is unverifiable as presented. The paper should either compute and report the aggregate improvement with clear attribution or remove the unsubstantiated claim.

- **Internal numerical inconsistency in the real-world case study.** The paper claims that "the intuitive domain rule enhances performance by 10.49% in the real dataset" (Section 5.3). From Table 2, ExID obtains 2.51 and CQL D obtains 2.13, which yields a ~17.8% improvement. The paper does not explain whether 10.49% refers to a different baseline (e.g., an unmentioned comparison in the appended table) or is miscalculated. This inconsistency undermines trust in the reported numbers.

- **Missing variance/confidence intervals on all main results.** All results in Tables 1, 2, and the MiniGrid table are reported as averages over three seeds without standard deviations, confidence intervals, or any measure of dispersion. Given that the harsh critic's claims about specific table values cannot be verified from the text (tables are images), the lack of error bars is particularly consequential — the reader has no way to assess whether the reported gains are systematic or within the noise of three runs. This is a standard reporting expectation for empirical ML papers.

### Minor

- **Under-specified teacher training procedure.** The teacher network is trained via behavior cloning on synthetic states "sampled from a uniform random distribution over state boundaries B(s)" (Section 4). The paper does not define what B(s) is concretely for any environment (e.g., min/max bounds per state dimension). While the concept is intuitive and the paper acknowledges that the synthetic data "may have state combinations that will never occur," the lack of specification makes it difficult to reproduce this step.

- **Teacher update ablation limited to one environment.** The ablation comparing full ExID, "no teacher update," and "just warm start" (Fig. 5c) is conducted only on CartPole. Given that the teacher update condition (Cond. 6) involves two hyperparameters (MC dropout passes T, dropout rate) and compares averages over a batch, its behavior could be environment-dependent. Validating it on at least one additional environment would strengthen the evidence.

- **The regularization design choice is not discussed.** When the critic's action is preferred over the teacher's action (Algo 1, lines 11–13), the regularization loss ℒ_r is set to 0, meaning the critic is no longer constrained by the teacher for those states. This design choice — effectively disabling the regularizer when the critic is confident — is not discussed or ablated, though it could impact convergence behavior.

### Trivial

- The caption for Fig. 1 says "partial dataset with first 10% samples" — "first 10% of an ordered dataset" could be misinterpreted. The paper clarifies later in Section 5.2 what the reduction process is (removing based on state conditions), but the initial phrasing is slightly ambiguous.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals on all main results (as noted above, this is a Major concern rather than a nice-to-have).
- A quantitative characterization of the reduced datasets (what fraction of transitions are removed, how many states become unseen). The paper describes the removal conditions qualitatively but does not quantify the difficulty regime.
- Extending the teacher update ablation to at least one additional environment beyond CartPole.
- A comparison with a version where the teacher update condition is replaced by a simpler rule (e.g., always use the critic's action) to isolate the value of the uncertainty check.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Warm-start parameter k not defined in main text.** Removed because the definition resides in the algorithm pseudocode in the appendix, which was stripped by the PDF parser. The parser strips appendix content from all papers; this information exists in the original submission.

- **BCQ not included as a baseline.** Removed because BCQ is explicitly listed among the eight compared algorithms for discrete environments in Section 5.1 ("These algorithms include... BCQ...").

- **Synthetic states may be physically unrealizable (Mountain Car).** Removed because the paper explicitly acknowledges this limitation: "Note that this does not represent the true state distribution and may have state combinations that will never occur" (Section 4, lines 84-85). The harsh critic's framing as an oversight is factually incorrect.

- **"First 10% samples" phrasing is vague.** Removed because the paper clearly explains the data reduction process per environment in Section 5.2 ("remove states with position > -0.8", etc.), and the "first 10%" is simply describing the reduced dataset size.

- **Missing continuous-domain experiment.** Removed as scope creep. The paper's experiments focus on discrete domains with a brief extension mention; requiring a HalfCheetah experiment for a method whose core components (discrete teacher update via cross-entropy with softmax Q-values) are fundamentally discrete-oriented would be outside the paper's stated scope.

## Novel Insights

An interesting observation emerges from comparing the harsh critic's and strength finder's assessments: both agree on the paper's strengths (novel regularization, adaptive teacher update, clean OOD generalization visualization) but disagree sharply on how to weight the numerical inconsistencies. This highlights that the paper's empirical evidence is *directionally* consistent (ExID improves over baselines in most settings) but *precisely* sloppy (the headline 27% and 10.49% figures are not properly explained). The disconnect between clearly positive qualitative evidence (Fig. 4 Q-value gaps, Fig. 6 robustness to knowledge quality) and imprecise quantitative framing is the paper's central flaw — it has real results but fails to present them accurately. A useful meta-lesson: the strength of the evidence for a paper's claims often depends less on the magnitude of reported gains and more on whether the reader can trace each number back to a specific, verifiable computation.

## Suggestions

1. **Drop or precisely justify the "at least 27%" claim.** Either compute the aggregate improvement over all environments/datasets with the methodology clearly stated, or remove the claim and let the individual results speak for themselves. The supportive evidence (Table 1, Table 2) is strong enough without an opaque aggregate figure.

2. **Clarify the 10.49% figure.** State explicitly which baseline the improvement is relative to. If it refers to a different baseline than CQL D (e.g., BC D or an average), say so. If it's an error, correct it.

3. **Add standard deviations or per-seed results** to all main tables. This is especially important given the modest 3-seed count.

4. **Define B(s) concretely** for at least one representative environment (e.g., "for Mountain Car, B(s) = [−1.2, 0.6] × [−0.07, 0.07]") so the teacher training procedure is reproducible.

5. **Run the teacher update ablation (Fig. 5c) on at least one more environment** (e.g., Lunar Lander) to confirm the pattern is not specific to CartPole.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>