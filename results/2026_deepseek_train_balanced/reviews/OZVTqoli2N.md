Now I have enough information to write the consolidated review. Let me produce it.

## Summary

This paper proposes a second-order Taylor expansion framework around pre-training weights to study model compositionality. It derives two incremental training algorithms—ITA (individual training with regularization toward pre-training weights) and IEL (ensemble training that directly optimizes the composed model)—from this theoretical analysis. The algorithms are evaluated on class-incremental learning benchmarks across full fine-tuning, LoRA, and IA³, and the paper additionally evaluates specialization and unlearning capabilities.

## Strengths

- **Generalizes compositionality theory beyond linearized networks**: The second-order analysis (Eq. 5–6) applies to any fine-tuning strategy (full fine-tuning, LoRA, adapters, IA³), whereas prior theoretical guarantees from Liu et al. (2023) and Ortiz et al. (2024) required linearized networks operating in the tangent space. The paper explicitly contrasts these settings (lines 63–69), including the practical disadvantage that linearized inference requires costly Jacobian-vector products.

- **Exact decomposition of the composition gap (Theorem 1, Eqs. 12–13)**: Rather than only an inequality, the paper derives an exact expression for the gap between the composed model's risk and the weighted individual risks. The term Ω (Eq. 13) is a non-negative pairwise distance between task vectors in the Hessian-induced Riemannian manifold. This decomposition is not present in prior work and yields the insight that minimizing Ω encourages alignment among task vectors and that regularization becomes increasingly important as the number of components grows.

- **Closed-form gradients with O(1) complexity in the number of tasks**: The derivation (Eq. 20, referenced at line 149) shows gradients of the IEL regularization term can be computed in closed form. Both training and inference maintain constant time and memory with respect to T (line 163), which is a concrete advantage over methods like SEED that store separate models for each task.

- **Controlled ablation isolating the regularization effect**: The ablation study (line 186) systematically removes the EWC-like regularization term for full fine-tuning, LoRA, and IA³, and tests partial regularization (classifier-only vs. all layers). This identifies that PEFT modules suffer less degradation when regularization is removed, attributing it to their tendency to forget less pre-training knowledge—a reproducible, evidence-backed finding.

- **Demonstration of specialization and unlearning via task-vector arithmetic**: The paper evaluates zero-shot specialization and unlearning (lines 197–200) with controlled target vs. control accuracy metrics, comparing against TMC. The finding that ITA supports both operations while IEL fails at specialization (line 200, "severe drop") is a non-trivial empirical result that reveals a structural difference between the two algorithms and provides actionable guidance.

- **Evaluation on challenging domain-shift benchmarks**: Beyond standard class-incremental splits (ImageNet, CIFAR, CUB), the paper tests on Resisc45 and CropDiseases, which have low domain similarity to ImageNet pretraining. The results (line 184) indicate the methods are not severely affected by large domain shifts, providing evidence that the framework remains effective even when the pre-training optimality assumption is challenged.

## Weaknesses

### Major

- **The central theoretical assumption (local minimum of the empirical risk across all tasks) is insufficiently justified.** The entire Jensen inequality (Eq. 6) and the convexity argument depend on $\theta_{\text{ptr}}$ being a local minimum of the full empirical risk over all tasks (line 55), so that the Hessian is PSD and the gradient is zero. The paper attempts to enforce this through "pre-consolidation" (linear probing of the classification head, line 157). However, linear probing only optimizes the head, not the backbone. There is no reason a pre-trained backbone—especially on datasets with large domain shift from ImageNet (Resisc45, CropDiseases)—should be a local minimum of the classification loss on those tasks. If $\theta_{\text{ptr}}$ is not a local minimum, the gradient is non-zero, the linear term in Eq. 2 matters, the Hessian is not guaranteed PSD, and the convexity argument for Jensen's inequality collapses. The paper's claim that "such a condition can be easily satisfied with over-parameterized deep learning models" (line 55, footnote) is offered without evidence in the target setting. This gap means the theoretical framework that motivates both algorithms rests on an assumption that is unverified and unlikely to hold strictly. The algorithms may work well for other reasons, but the theoretical guarantees do not apply as cleanly as presented.

### Minor

- **Theory-practice gap between the derived second-order objective and the actual training loss.** The paper explicitly states (line 161) that "while our derivations regard the second-order approximation $\hat{\ell}$, the full loss $\ell$ is instead employed in our algorithms." The inequality in Eq. 6 applies to $\hat{\ell}_{\text{emp}}$, not $\ell_{\text{emp}}$, so it does not provide a formal guarantee for the quantity actually being optimized. Similarly, the KL-Fisher equivalence (Eq. 7) requires $\tau_t \to 0$, but in practice task vectors are non-negligible during fine-tuning. The paper acknowledges this (Section 7) but it means the theory serves as a source of inspiration for the regularizer rather than a rigorous justification of the algorithms' behavior. This is a common pattern in theory-motivated ML and does not invalidate the empirical contributions, but the gap should be more clearly scoped.

- **ITA's algorithmic novelty relative to EWC is modest.** The paper acknowledges the strong analogy to Elastic Weight Consolidation (line 103), with the key difference being a fixed anchor at $\theta_{\text{ptr}}$ rather than a shifting anchor at $\theta_{t-1}$. This difference is real and meaningful (it targets preservation of pre-training knowledge rather than prevention of catastrophic forgetting of previous tasks), but the Fisher estimation procedure (diagonal, Monte Carlo, incremental accumulation) follows Chaudhry et al. (2018) and Schwarz et al. (2018) directly. The novelty lies more in the interpretation and the specific anchor choice than in the mechanism. Distinguishing this more sharply in the paper would help readers understand what is genuinely new.

- **Standard deviations for the main results are deferred to the supplementary material.** The paper reports results averaged over three runs (line 182) but the variance is only in the supplementary. Given that three runs is a small sample, the main text should include standard deviations or confidence intervals so readers can assess whether reported improvements are significant.

- **Pre-consolidation linear probing is not separately ablated.** The pre-consolidation stage (linear probing of the head) is an integral part of the pipeline. While the pre-trained model baseline in Fig. 1 partially addresses this, a direct comparison of ITA with and without the pre-consolidation step would clarify how much of the performance comes from the head optimization alone versus the regularization during fine-tuning.

### Trivial

- The claim about "constant complexity" (line 163) for IEL depends on derivations in the supplementary material not visible in the main text. A brief sketch or citation to a visible equation would help the self-contained reader.

## Nice-to-Haves

- Empirically validate the core assumption by measuring whether $\theta_{\text{ptr}}$ (after pre-consolidation) is actually a local minimum of the empirical risk on held-out data from all tasks, or at least measure gradient norms at that point.
- Compare ITA directly against a version with a shifting EWC anchor (standard EWC) to disentangle whether the fixed anchor at $\theta_{\text{ptr}}$ is the cause of improved compositionality, or whether any parameter-distance regularization would suffice.
- Ablate the pre-consolidation linear probing step to isolate its contribution from the regularization.
- Consider Kronecker-factored approximations (as noted in Section 7) as a middle ground between the diagonal Fisher and the full Hessian.

## Removed Points

The following points from the reviews were removed with justification:

- **"Tables are not visible in the main text" / "Numerical results should be in the main text"**: This is a parser artifact—the paper uses `\input{tables/...}` which works correctly in the actual PDF. The reviewer could not see them, but the original submission includes them.
- **"The paper would benefit from directly acknowledging the high similarity of ITA to EWC"**: The paper already acknowledges this at line 103. The reviewer appears to have missed this paragraph.
- **Fisher estimation is "directly adopted" from prior work**: The paper explicitly cites Chaudhry et al. (2018) and Schwarz et al. (2018) (line 95). This is standard scientific practice; building on established methodology is not a weakness.
- **Missing related works / reproducibility concerns about existence of cited models or benchmarks**: Rules prohibit raising such concerns. All cited works, models, and datasets are assumed to exist as of the review date.
- **Several general criticisms from the harsh reviewer that were speculative or lacked concrete anchors**: Removed per filtering discipline (e.g., speculation about supplementary material content, framing concerns that could not be tied to specific paper content).
- **Strength Finder strengths that were generic** (e.g., "this paper addresses an important problem"): Removed per filtering discipline. Only strengths with specific evidence anchors are retained.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface an unappreciated angle that the paper itself does not discuss. The most interesting fringe findings—that IEL fails at specialization while ITA succeeds (line 200), and that PEFT modules suffer less degradation when regularization is removed (line 186)—are already presented and discussed in the paper.

## Suggestions

1. **Address the local-minimum assumption head-on.** Either provide empirical evidence (gradient norms, Hessian eigenvalues at the pre-consolidation point) that the assumption approximately holds, or reframe the theoretical discussion as a "motivation" rather than a derivation, making clear that the algorithms are inspired by the second-order analysis but do not inherit its guarantees when the assumption is violated.

2. **Move standard deviations for the main results into the main text** (or at least into a table caption). Three runs is a small sample; without variance the reader cannot assess significance.

3. **Ablate the pre-consolidation linear probing step** to quantify its contribution separately from the EWC-like regularization. This is a small experiment that would strengthen the paper's claims about the regularization term.

4. **Discuss the practical computational cost of IEL's pairwise alignment term more concretely** when scaling to many tasks. The constant-complexity claim (line 149) is important but its justification is deferred to the supplementary.

5. **Soften the theoretical claims** in the Abstract and Introduction to match the level of support. Phrases like "the proposed formulation highlights the importance of staying within the pre-training basin" (Abstract) are fine as motivation. But the paper should not imply the Jensen inequality provides a guarantee for the actual loss being optimized.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>