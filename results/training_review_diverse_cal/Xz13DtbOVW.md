Now I have a thorough understanding of both the paper and the reviews. Let me compose the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write this now.

I need to be very careful about the harsh reviewer's criticisms. Let me go through them systematically:

1. **"Constraint set does not fully capture the stated notion of disparate impact"** — The paper acknowledges this (lines 141-148, references appendix). The paper says: "This choice motivates an operational definition of disparate impact which focuses on the group with the highest EAG, given by $\max_g \psi_g$" (line 148). So the paper does partially reframe. However, the earlier definition (line 108, "change approximately equally") and the evaluation metric $\Psi_{pw}$ (line 131) still suggest equalization rather than worst-case bounding. This is a valid narrative clarity issue. **Keep as Minor.**

2. **"Surrogate gradients may be misaligned"** — Valid concern about the heuristic relationship between loss gaps and accuracy gaps. The paper's justification is a single sentence (line 208). No formal analysis. **Keep as Minor** — real but not fatal since the dual variables use true constraints as a correction mechanism.

3. **"Generalization failure fundamentally limits practical contribution"** — The paper is very transparent about this. CEAG achieves best test disparity on FairFace and UTKFace but not on CIFAR-100. This is a real limitation, though the paper doesn't hide it. **Keep as Major.**

4. **"Replay buffers as a contribution"** — The paper DOES include ablation with and without RBs (line 358: "CEAG (no RB)"). The reviewer's claim that the comparison isn't apples-to-apples is factually wrong. **REMOVE** this criticism.

5. **"Definition of $\Delta$ as global accuracy gap"** — Computing $\Delta$ on the training set is standard practice. This criticism adds nothing. **REMOVE.**

6. **"No discussion of early stopping for CEAG"** — Valid observation but minor. NFTES is shown to have "very high disparity" (line 381), so this asymmetry doesn't favor NFTES. **Keep as Trivial.**

7. **"Recast fairness notion as controlling worst-case degradation"** — Good suggestion but not a weakness per se. The paper partially does this. **Move to Nice-to-Haves.**

8. **"Analyze surrogate-quality alignment"** — Valid suggestion. **Move to Nice-to-Haves.**

9. **"Devote subsection to analyzing generalization gap"** — Valid suggestion. **Move to Nice-to-Haves.**

10. **"Add experiment with very large groups (ImageNet)"** — Practically infeasible. **REMOVE** per rule about infeasible asks.

11. **"Convergence analysis"** — Beyond scope for an empirical paper. **Move to Nice-to-Haves.**

12. **"Ablation on replay buffer size"** — Valid suggestion. **Move to Nice-to-Haves.**

13. **"Reporting the value of $\epsilon$"** — Likely in the stripped appendix. **REMOVE** per rule about missing appendix content.

14. **"Comparison to original EL without replay buffers"** — Paper DOES include this (CIFAR-100 table). **REMOVE** (factually wrong).

Now, the strength finder's strengths seem reasonable. Let me filter:

Strength 1: Valid and well-supported. Keep.
Strength 2: Valid. Keep.
Strength 3: Valid. Keep.
Strength 4: Valid but needs caveat about generalization. Keep.
Strength 5: Valid. Keep.
Strength 6: Valid — the paper is the first to document this. Keep.
Strength 7: Valid. Keep.
Strength 8: Valid. Keep.

None of these are generic or conflict with verified weaknesses.

Let me now write the review.---

## Summary

This paper proposes a constrained optimization formulation (CEAG) for mitigating the disparate impact of model pruning. The key idea is to directly bound per-group *excess accuracy gaps* (EAGs) between the dense and sparse models, rather than using loss-based surrogates as in prior work. The method handles non-differentiable accuracy constraints via proxy constraints (Cotter et al., 2019) and uses replay buffers to stabilize stochastic constraint estimation. Experiments on FairFace, UTKFace, and CIFAR-100 show that CEAG consistently achieves near-zero disparity on the training set across sparsity levels and architectures, with interpretable tolerance parameters.

## Strengths

- **Direct formulation via accuracy gaps rather than loss surrogates.** Prior work (Tran et al., 2022) constrains the sparse model's loss across groups, which addresses disparity only indirectly and is agnostic to the dense model's per-group performance. CEAG directly bounds group-level accuracy changes between the dense and sparse models, giving practitioners an actionable success criterion (e.g., "no group may degrade more than 1% beyond the overall change").

- **Interpretable constraints with operational meaning.** The tolerance $\epsilon$ directly bounds per-group accuracy degradation relative to the global change. As stated in Section 3.3, "setting $\epsilon=1\%$ implies the worst affected class may not lose beyond $1\%$ accuracy compared to the overall model change." This is more transparent than loss-based constraints, where the tolerance has no clear accuracy interpretation.

- **Scalability to large numbers of groups.** CEAG handles up to 100 groups (CIFAR-100) and intersectional groups (UTKFace race×gender, ~28 groups) with negligible computational overhead — one forward/backward pass per iteration, matching ERM. The memory overhead is minimal (one float per constraint plus a boolean replay buffer).

- **Consistent mitigation on the training set across tasks.** On FairFace at 99% sparsity (Table 1), CEAG achieves $\max_g\psi_g = 0.0$ on the training set, versus 4.0 for equalized loss and 13.3 for FairGRAPE, while maintaining comparable test accuracy (~65.5%). On UTKFace intersectional at 95% sparsity (Table 2), CEAG achieves $\max_g\psi_g = 0.8$ versus 18.3 for naive fine-tuning. This pattern holds across architectures (ResNet-34, MobileNet-V2, CifarResNet-56) and sparsity levels (85%–99%).

- **Replay buffers as a stabilizing technique.** The replay buffer mechanism aggregates accuracy measurements across $k$ recent datapoints per group, reducing noise in constraint estimation for small or numerous groups. The paper shows that both CEAG and the equalized-loss baseline benefit from replay buffers (CIFAR-100, Table 3: EL $\max_g\psi_g$ drops from 10.3 to 7.8 with RBs; CEAG from 8.6 to 5.8).

- **First documented characterization of the generalization gap.** The paper honestly reports that *all* considered methods (including CEAG) fail to transfer disparity guarantees to unseen data. This is stated in the abstract and discussed in Section 6. Identifying and documenting this open problem is a valuable contribution in its own right.

## Weaknesses

### Fatal

None.

### Major

- **The generalization gap fundamentally limits practical utility, and CEAG does not universally dominate baselines on test data.** The paper honestly reports that "all methods considered in this paper (including ours) fail to mitigate pruning-induced disparities on unseen data" (Introduction). On CIFAR-100 — the largest-scale experiment with 100 groups — the equalized-loss baseline with replay buffers (EL+RB) *outperforms* CEAG on test disparity: "the smallest $\max_g \psi_g$ on the test set are obtained by ELGRB" (Section 5.3). While CEAG achieves the best test disparity on FairFace and UTKFace, the mixed results mean the method's practical advantage is task-dependent and does not hold universally. The paper would benefit substantially from analyzing *why* generalization fails — whether due to distribution shift between training and test sets, overfitting to constraints, or a property of accuracy-gap constraints themselves.

### Minor

- **Narrative disconnect between the stated fairness notion and the actual constraints.** The paper initially defines low disparate impact as accuracy changes being "approximately equal" across groups (Section 3.1: $\Delta_g \approx \Delta_{g'}$) and evaluates with the pairwise disparity metric $\Psi_{pw}$. However, the CEAG formulation (Equation 6) constrains only the positive excess accuracy gaps ($\psi_g \leq \epsilon$), not the negative ones ($\psi_g \geq -\epsilon$). The paper acknowledges this gap (Section 3.2, referencing the appendix for motivation) and reframes the problem as "focus[ing] on the group with the highest EAG, given by $\max_g \psi_g$." This operational definition is defensible — bounding the worst degradation controls the most concerning form of disparity — but the paper's narrative still invokes "equal accuracy gaps" and reports $\Psi_{pw}$ as a primary metric. Aligning the framing with what the constraints actually enforce (worst-case degradation control) would clean up the exposition.

- **Surrogate-gradient alignment is not empirically or theoretically characterized.** The primal parameters are updated using gradients of a surrogate $\tilde{\psi}_g$ (based on loss gaps), while the dual parameters are updated using the true accuracy gaps $\psi_g$. The paper's justification ("drops in accuracy correspond to increases in loss," Section 4.1) is heuristic and not guaranteed pointwise or per-minibatch. Cases where loss decreases while accuracy also decreases (e.g., growing confidence in wrong predictions) could send misaligned gradient signals. While the dual update using true constraints provides a correction mechanism, the paper does not analyze how well $\tilde{\psi}_g$ tracks $\psi_g$ during training or whether misalignment causes convergence issues. This is a gap in methodological justification.

- **Asymmetric use of early stopping.** The NFTES baseline selects the best iterate of naive fine-tuning in terms of test accuracy (early stopping), but early stopping is not applied to CEAG or EL+RB. While NFTES is shown to produce "very high disparity" (Section 6) — so this asymmetry does not favor NFTES in the disparity comparison — the different treatment means the comparison is not fully controlled.

### Trivial

- The paper computes the global accuracy gap $\Delta$ on the training set (Equation 1), which is the natural choice for the constrained optimization but may not reflect the population-level global gap. This is standard practice and a minor caveat.

## Nice-to-Haves

- **Empirical analysis of surrogate alignment.** A correlation plot showing how $\tilde{\psi}_g$ (negative loss gap) relates to $\psi_g$ (accuracy gap) during training would strengthen confidence in the proxy constraint approach.
- **Ablation on replay buffer size $k$.** The paper mentions a trade-off between variance reduction and staleness but provides no analysis. A simple ablation would help practitioners set this hyperparameter.
- **Analysis of the generalization gap's causes.** Investigating whether the gap correlates with overfitting, distribution shift, or a property of accuracy-gap constraints themselves would turn the documented limitation into a scientific contribution.
- **Reframing the fairness notion explicitly as "controlling worst-case accuracy degradation."** This would eliminate the narrative disconnect between the definition and the constraints.

## Removed Points

These points from the reviews are removed or corrected; they are listed here for completeness but should be treated with caution:

- *"The paper should disentangle gains from CEAG vs. replay buffers; comparison against EL without RBs is missing."* — The paper *does* include CEAG without RBs and EL without RBs (CIFAR-100 experiments, line 358). This is already addressed.
- *"Comparison to the original equalized loss method (without replay buffers) would strengthen the contribution."* — Already present for CIFAR-100. The paper includes both EL and EL+RB.
- *"Missing reporting of $\epsilon$ values."* — The appendix (stripped by the parser) likely contains these values. The instruction explicitly notes that appendix content should not be treated as missing.
- *"Add an experiment with very large groups (ImageNet, 1000 groups)."* — Practically infeasible for an academic submission and goes well beyond the paper's demonstrated scope.
- *"Convergence analysis or guarantees."* — This would require substantial theoretical work beyond the paper's empirical scope. The approach builds on a published technique (Cotter et al., 2019), and a full analysis would constitute a separate paper.
- *"The definition of $\Delta$ as global accuracy gap on training data may not reflect the population-level gap."* — Computing training-set metrics for use in training is standard practice in ML. This is not a weakness.
- *"Replay buffers comparison is not apples-to-apples."* — The paper includes controlled variants with and without RBs for both methods, directly addressing this concern.

## Novel Insights

The most novel observation emerging from these reviews — beyond the paper's own contributions — is the tension between the stated fairness notion (equalization of accuracy gaps) and the actual constraint set (worst-case bounding). The paper's choice to constrain only positive EAGs is pragmatically motivated (the feasible region with both bounds is too small relative to noise), but this creates a gap between what the method promises and what it enforces. This tension, combined with the documented generalization gap, suggests that accuracy-gap constraints for disparity mitigation face two fundamental challenges: the optimization formulation must navigate an inherently noisy feasible region, and even when successful on the training set, the guarantees do not transfer. The paper's most lasting contribution may be less the specific algorithm than the rigorous empirical demonstration that these challenges exist and are not trivially resolved.

## Suggestions

1. **Reframe the fairness notion explicitly as "controlling worst-case accuracy degradation" rather than "equal accuracy gaps."** This would align the narrative with what the constraints actually enforce, eliminate the disconnect with $\Psi_{pw}$, and better position the method's strengths. The pairwise disparity metric can remain as a secondary diagnostic.

2. **Provide an empirical alignment plot.** Show how $\tilde{\psi}_g$ (surrogate, based on loss) correlates with $\psi_g$ (true accuracy gap) during a typical training run. If the correlation is strong, this strengthens the methodological justification. If weak, discuss the implications openly.

3. **Investigate the generalization gap.** Devote a subsection to analyzing why disparity mitigation fails on test data — is it overfitting to constraints, distribution shift, or a property of the accuracy-gap objective? Even a preliminary investigation would substantially increase the paper's scientific value.

4. **Address the early stopping asymmetry.** Either apply a similar early-stopping procedure to all methods (selecting the best epoch on a held-out set) or explicitly justify why it is not applied to constrained methods.

## Score and Decision

The paper makes a solid technical contribution — a principled formulation for directly constraining accuracy gaps with interpretable tolerances, accompanied by a practical algorithm that scales to many groups. The empirical evaluation is thorough, the limitations are honestly documented, and the replay buffer technique is a useful engineering contribution. However, the generalization gap sharply limits practical applicability, the narrative framing is somewhat inconsistent with what the constraints enforce, and the surrogate-gradient justification lacks empirical support. The paper is a promising research direction rather than a fully deployable solution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>