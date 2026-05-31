Now I have a thorough understanding of the paper and can cross-check the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes the Logical Formula Learner (LFL) framework, a general formulation of differentiable neural modules that converge to explicit logical formulas. It unifies prior designs (dNL, DSL) as special cases and introduces three novel instantiations with varying combinatorial search freedom: LFL-Type1 (arbitrary formulas), LFL-Type2 (look-up table), and LFL-Type3 (intermediate). An MLP gradient shortcut is introduced to enable LFL-Type1 to be trained end-to-end in Neuro-Symbolic (NeSy) predictors from scratch, which the paper claims as the first such system to jointly converge while explicitly learning arbitrary logical formulas.

## Strengths

- **LFL-Type1 outperforms dNL on learning formulas with limited hidden neurons.** Section 3.1.2 and Figure 4(c) show that when the number of hidden neurons is reduced toward 100, LFL-Type1 maintains higher accuracy than dNL on the MNIST Sum formula learning task from binary data. This is a concrete, direct improvement over the prior dNL design.

- **LFL-Type2 eliminates DSL's training-inference consistency gap.** Section 3.2 and Figure 4(d) show that LFL-Type2's Concrete-noise-based membership mechanism avoids the persistent random label choices of DSL's ε-greedy policy during inference, making training and inference behaviors consistent while matching DSL's task performance.

- **LFL-Type3 converges faster than DSL and LFL-Type2.** Section 3.3 and Figure 4(d) show LFL-Type3 achieves faster convergence on MNIST Sum with automatically tuned hyperparameters, demonstrating a practical advantage of its intermediate combinatorial-search design.

- **The MLP gradient shortcut is validated by ablation.** Section 3.4 shows that removing either the MLP shortcut or the label-distribution loss causes LFL-Type1 to fail on both MNIST Sum and Multi-digit Sum, providing empirical justification for the architectural innovation.

- **The LFL framework provides a clean unification of prior designs.** Sections 2.1 and 2.2 show that both dNL and DSL are special cases of the LFL framework (via specific choices of t-norms and membership functions), offering a formal foundation for comparing and extending differentiable logic modules.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient verification that LFL-Type1 learns *correct* arbitrary formulas in the NeSy setting.**  
   On MNIST Multi-digit Sum, LFL-Type1 achieves 72.18% accuracy versus 96.00% for LFL-Type3 (Table 1). The paper dismisses this 24-point gap by asserting that "differences in accuracy are caused only by CNN classifier mistakes when the LFL learns a correct formula" (p.8), and marks the learned formula as "✓ but different." However, **no formula extraction, exhaustive input-space verification, or controlled experiment (e.g., feeding ground-truth concept labels to isolate LFL errors) is provided.** The claim that the formula is correct despite drastically lower accuracy than a baseline with identical CNN backbone is asserted, not demonstrated. Without such validation, the paper's central contribution — that LFL-Type1 learns arbitrary logical formulas in a NeSy predictor — is not empirically supported for the more complex task.

2. **The MLP gradient shortcut's role is not fully disentangled.**  
   The MLP shares the same input/output as the LFL module and is randomly selected during training (50% per sample). The paper states that during inference, LFL's prediction is used for recurrence in the Multi-digit Sum task (Section 2.4.2). However, it does **not report LFL-only test accuracy with the MLP completely removed** for the non-recurrent MNIST Sum task, nor does it analyze whether the LFL module independently produces a correct formula. Without this isolation, it is unclear whether the LFL genuinely learns the formula or whether the MLP carries the bulk of the representation and the LFL merely approximates it post-hoc. The claim that *the LFL* learns the formula would be significantly stronger with LFL-only evaluation.

### Minor

3. **Missing comparison weakens the "first NeSy predictor" claim.**  
   The paper claims the first NeSy predictor satisfying three properties (end-to-end differentiable, trained from scratch, learns arbitrary formulas). However, dNL — which also learns arbitrary formulas — is neither evaluated on the NeSy tasks nor combined with the MLP shortcut to test whether it would also converge. Adding dNL+MLP as a baseline would directly test whether the novelty lies in the LFL-Type1 design or in the MLP shortcut trick itself.

4. **No statistical rigor.**  
   All experimental results in Table 1 and Figure 4 appear to be single runs with no reported standard deviations or multiple random seeds. Given stochastic elements (Concrete noise, random selection of LFL/MLP for recurrence), results may vary. Standard reporting of error bars or multiple trials is expected for ML papers.

5. **Missing hyperparameter and training details.**  
   The loss function (Eq. 22) includes three hyperparameters (β₁, β₂, β₃) and the network uses noise-scale hyperparameters (η, η₀, η₁), but **no specific values, ranges, or tuning procedures are reported**. Learning rates, batch sizes, and network sizes are also absent, limiting reproducibility.

6. **No analysis of sparsity.**  
   The LFL is designed to converge to a sparse network equating a simple logical formula, but no quantitative results are reported on actual sparsity achieved (e.g., number of active memberships after training, formula complexity/size). This is a gap given that sparsity constraints (Eq. 19) are central to the method's operation.

### Trivial
None.

## Nice-to-Haves

- Report LFL-only test accuracy at inference time (with MLP completely removed/shut off) for both MNIST Sum and Multi-digit Sum.
- Directly verify the learned formula via exhaustive enumeration on synthetically generated inputs (using CNN concept predictions) and report the fraction of inputs where LFL logic matches ground truth.
- Include dNL (+MLP shortcut) as a baseline in the NeSy experiments.
- Add a controlled experiment with ground-truth concept labels (no CNNs) to confirm LFL-Type1 can recover exact formulas in the NeSy predictor setting.
- Report error bars over multiple random seeds.
- Disclose specific hyperparameter values and tuning procedures.
- Report sparsity metrics (e.g., number of active memberships, formula size after binarization).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about "Section 2.3.3 definition of LFL-Type3 is terse"** — This is a matter of presentation preference, not a substantive weakness. The description is clear enough to understand the design.
- **Criticism about "50% probability not justified"** — While a sensitivity analysis would strengthen the paper, this is a design choice that is reasonable and common; not a core flaw.
- **Strength claimed about "LFL-Type1-based NeSy predictor is the first to learn arbitrary logical formulas"** — This conflicts with the verified weakness (#1) that the evidence for this claim is insufficient. The paper states this as a contribution, but the evidence is not sufficiently supportive, so this strength is downgraded.
- **Generic strengths about "addressing an important problem" or "targeting an interesting question"** — These are superficial and not specific to this paper's execution.
- **Missing related works** — Cannot be verified without external sources.
- **Grammar/formatting/style nitpicks** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an independent observation about the work that is not already stated by the authors.

## Suggestions

1. **Verify the learned formula directly.** For both MNIST Sum and Multi-digit Sum, extract the LFL-Type1 formula after training (by binarizing memberships) and test it on synthetically generated inputs. Report the fraction of inputs where the LFL's logic matches the ground-truth formula. This is the single most impactful experiment to strengthen the paper's core claim.
2. **Report LFL-only accuracy.** After training with the MLP shortcut, evaluate the model at inference with the MLP disabled entirely. If LFL alone performs comparably, the MLP is a true gradient helper; if accuracy collapses, the MLP is doing more than just helping gradients.
3. **Add dNL+MLP as a NeSy baseline.** This directly tests whether the claimed "first" is due to the LFL-Type1 design or the MLP shortcut.
4. **Run experiments with multiple random seeds** and report mean ± std to establish statistical reliability.
5. **Report hyperparameter values** (β₁, β₂, β₃, η, η₀, η₁, learning rate, batch size) and tuning procedures.
6. **Report sparsity achieved** after training (active memberships, formula complexity) to support the claim that the LFL converges to simple logical formulas.

## Score and Decision

The LFL framework, the three instantiations, and the MLP gradient shortcut represent genuine contributions. The binary-data experiments (Section 3.1) provide solid evidence that LFL-Type1 improves over dNL, and the LFL-Type2/LFL-Type3 experiments show clear practical advantages over DSL. However, the paper's headline claim — that LFL-Type1 yields the first NeSy predictor to learn arbitrary logical formulas end-to-end from scratch — rests on the Multi-digit Sum experiment, where the evidence is insufficiently validated. A 24-point accuracy gap relative to a simpler baseline using the same CNN backbone, with no formula verification or error isolation, means the central claim is not adequately supported as presented. The paper could potentially be strengthened to a strong acceptance, but in its current form the experimental validation does not meet the standard required for the claimed contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>