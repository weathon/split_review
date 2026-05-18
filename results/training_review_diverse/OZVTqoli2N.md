Now I have all the information needed to construct the final review.

---

## Summary

This paper studies model compositionality — the ability to combine multiple fine-tuned modules into a single multi-task model — in standard non-linear deep networks. The authors derive a second-order Taylor expansion framework around pre-training weights to show that staying within the "pre-training basin" is critical for effective composition, and they propose two incremental learning algorithms (ITA and IEL) that enforce proximity to pre-training weights via Fisher-based regularization. The resulting methods achieve strong empirical results on six class-incremental benchmarks and support zero-shot specialization and unlearning through task-vector arithmetic.

## Strengths

- **Generalization beyond linearized networks.** The paper's second-order framework applies to any fine-tuning strategy (full FT, LoRA, IA³) in standard non-linear networks, whereas prior theoretical work on compositionality (e.g., Ortiz-Jiménez et al., Liu et al.) was restricted to linearized models. The paper explicitly contrasts its inequality (Eq. 4) with the linearization-based result (Eq. 6–7) and notes it "applies to *any* fine-tuning strategy" (lines 63–69).

- **Exact decomposition of the composed-model loss (Theorem 1).** The paper derives an exact expression for the second-order approximation of the composed model's loss, decomposing it into a convex combination of individual losses plus a non-negative diversity term Ω(·) proportional to pairwise distances in the Hessian-induced Riemannian manifold (Eqs. 11–12). This result directly motivates the regularization used in both algorithms.

- **Dual algorithms with different trade-offs.** The paper proposes two distinct incremental learning algorithms (ITA for individual training, IEL for ensemble training) from the same second-order formulation, and shows that they have complementary properties: ITA supports modular editing (specialization/unlearning) while IEL does not, a practically significant finding demonstrated in Tables 3–4.

- **Strong empirical performance.** ITA and IEL achieve state-of-the-art or competitive final accuracy on six class-incremental benchmarks (Table 1), including challenging domain-shift datasets (Resisc45, CropDiseases), outperforming prior methods like TMC, APT, and InfLoRA. The results hold across full fine-tuning and PEFT variants.

- **Demonstrated specialization and unlearning capabilities.** The paper shows that ITA's task vectors can be added/subtracted to specialize on a subset of tasks or unlearn a target task, with ITA achieving the best absolute performance on target tasks and a clear accuracy gap between target and control tasks (Tables 3–4). The finding that IEL *cannot* support modular editing while ITA can is a novel and useful insight.

## Weaknesses

### Fatal
None. The paper's core empirical contributions stand even if the theory is approximate.

### Major

- **The local-minimum assumption for θ\_ptr is not verifiably satisfied.** The central theoretical result requires that the pre-trained weights θ\_ptr are a local minimum of the empirical risk over *all* tasks (including unseen ones), so that H(θ\_ptr) ⪰ 0. The paper's practical strategy to "enforce" this — linear probing (LP) during pre-consolidation — fine-tunes only the classification head while leaving backbone weights frozen (line 157). This does not ensure that the backbone is at a stationary point of the loss on new-task data; the gradient w.r.t. backbone weights at θ\_ptr is typically non-zero, and the Hessian is not guaranteed positive semidefinite over the combined data distribution. The paper acknowledges the assumption (line 55) and discusses approximation concerns in the limitations (Section 6), but the claim that the condition is "easily satisfied with over-parameterized deep learning models" is not substantiated. Since the Jensen inequality, the convexity of the second-order approximation, and the non-negativity of Ω in Theorem 1 all depend on H(θ\_ptr) ⪰ 0, a violation weakens the theoretical guarantees to heuristic intuition. The paper would be stronger if it either relaxed this requirement or provided empirical evidence (e.g., smallest Hessian eigenvalues after LP).

- **The Fisher-based regularization is not isolated from simpler proximity baselines.** The ablation in Table 2 shows that removing the EWC-like regularization term hurts performance, confirming that regularization helps. However, the paper does not compare against a simpler baseline that achieves proximity to θ\_ptr through a plain L2 penalty on ∥τ\_t∥² (weight decay toward pre-trained weights). Since the paper's core message is that "staying within the pre-training basin" is the key condition for compositionality, a simple L2 regularizer to θ\_ptr would be a natural competitor to test whether the Fisher weighting — rather than mere proximity — drives the improvement. The paper compares against standard EWC (which has a shifting anchor rather than a fixed one at θ\_ptr), but this does not isolate the effect of Fisher-weighting vs. uniform weighting. Including an L2 baseline would either demonstrate the added value of the FIM or reveal that the theoretical apparatus primarily justifies a known regularization strategy.

### Minor

- **Gap between second-order theory and the actual loss used in the algorithms.** The derivations in Section 2 use the second-order approximation ℓ̂, but the algorithms in Section 3 optimize the exact loss ℓ (line 161). The paper acknowledges this explicitly ("this proxy is often relaxed, and the full target function is used instead for simplicity"), which is standard in the continual learning literature. However, no empirical check is provided (e.g., measuring how well the quadratic proxy tracks the true loss over the region of parameter space visited during training). A small-scale verification of approximation quality would strengthen the link between theory and practice.

- **No wall-clock training time or computational cost comparison.** One of the claimed advantages is constant complexity with respect to the number of tasks, but the paper does not report wall-clock time or FLOPs for the compared methods. A direct runtime comparison (e.g., total training time for a 10-task sequence) would substantiate this claim and help practitioners gauge practical efficiency.

### Trivial

- The notation in several equations (Eq. 11, 16, 17) is dense, with nested sums over index sets that require effort to parse. Brief prose intuition after each key equation would improve readability.

- The constant-memory claim is qualified with "provided we are not interested in more complex forms of composition than the simplest uniform average (as required for model customization and unlearning)" (line 163). This caveat is present but easy to miss — it could be made more prominent when the abstract advertises unlearning as a key benefit.

## Nice-to-Haves

- An ablation for IEL (removing the Ω regularization term) analogous to the ITA ablation in Table 2, shown in the main paper rather than deferred to the supplementary (though the supplementary content exists in the original submission).

- A task-by-task learning curve visualization to complement the final-accuracy tables and show whether performance degrades over the incremental sequence (forgetting is already in the supplementary).

- Exploration of more accurate Hessian approximations (e.g., Kronecker-factored) beyond the diagonal Fisher, which the paper itself mentions as future work.

## Removed Points

- **"Constant complexity claim is misleading because unlearning requires storing task vectors."** The paper already includes the explicit caveat (line 163): "provided we are not interested in more complex forms of composition than the simplest uniform average (as required for model customization and unlearning)." This criticism reflects a failure to read the qualification already present in the paper. *Removed because the paper already addresses it.*

- **"The paper should acknowledge the theory-algorithm gap more explicitly."** The paper already states (line 161) that "the full loss ℓ is instead employed in our algorithms" while the derivations use ℓ̂, citing precedent in the literature. The acknowledgment is already explicit. *Removed as factually inaccurate about what the paper does; the underlying concern (lack of empirical verification) is kept in Minor weaknesses above.*

## Novel Insights

The most interesting finding that emerges from the reviews — beyond the paper's own contributions — is the sharp behavioral difference between ITA and IEL uncovered in the specialization/unlearning experiments. While both algorithms achieve comparable final accuracy, ITA supports modular editing (addition/subtraction of task vectors) while IEL fails when any ensemble member is removed. This provides a practical design principle: methods that optimize the composed model as a whole may sacrifice component-level modularity, even when aggregate performance is strong. This tension between ensemble accuracy and editability is a useful consideration for future work on modular systems.

## Suggestions

1. **Add a simple L2 proximity baseline.** Compare ITA against the same algorithm with the Fisher-weighted EWC term replaced by a plain L2 penalty (weight decay toward θ\_ptr). If ITA outperforms this baseline, the added value of Fisher weighting is demonstrated; if not, the theoretical framework primarily justifies a known heuristic (stay close to pre-training), and the paper should acknowledge this honestly.

2. **Provide empirical evidence for the Hessian condition.** For at least one model/task setting, estimate the smallest eigenvalue of the empirical Hessian (or its diagonal/Fisher approximation) after linear probing to verify whether H(θ\_ptr) is positive semidefinite in practice. If it is not, discuss how the algorithms still work despite the violation.

3. **Add a small-scale verification of the second-order approximation.** For one or two tasks, compare ℓ(θ\_ptr + τ) with the quadratic approximation ℓ̂(θ\_ptr + τ) over the range of τ visited during training to show the approximation is empirically reasonable.

4. **Report training time.** A wall-clock comparison (e.g., total training time for a 10-task sequence across methods) would substantiate the constant-complexity claim and aid reproducibility.

5. **Temper the theoretical claims in the abstract/introduction.** The paper's empirical contributions are strong enough to stand on their own. The theoretical framing should be presented as a useful approximation that provides intuition and motivates algorithmic design, not as a rigorous guarantee requiring assumptions that are not verifiably satisfied.

## Score and Decision

This paper makes a solid empirical contribution: two well-performing incremental learning algorithms, strong results across six benchmarks, and a novel analysis of specialization/unlearning capabilities that reveals a practically important distinction between individual and ensemble training. The theoretical framework, while approximate and built on assumptions not fully verifiable, provides useful intuition and connects compositionality to the well-studied idea of staying close to pre-training. The weaknesses are genuine but not fatal — the Hessian assumption and missing L2 baseline are the most significant, and addressing them (as suggested above) would substantially strengthen the paper even without changing the core algorithms.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>