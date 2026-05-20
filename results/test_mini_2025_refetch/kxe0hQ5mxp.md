Now I have sufficient calibration data. Let me write the consolidated review.

---

## Summary

This paper proposes **elephant activation functions** — bell-shaped functions (Elephant(x) = 1/(1+|x/a|^d)) whose outputs *and* gradients are both sparse — to reduce catastrophic forgetting in neural networks. The core theoretical insight (Lemma 3.1) is that for non-linear approximations, the NTK contains an extra term involving activation-function gradients, so representation sparsity alone is insufficient; gradient sparsity is also needed. Experiments are conducted across three domains: streaming regression (sine approximation), class-incremental learning (Split MNIST), and reinforcement learning (four classic control tasks).

## Strengths  

1. **Novel theoretical framing linking gradient sparsity to catastrophic forgetting.** Lemma 3.1 cleanly derives the NTK for a one-hidden-layer MLP and identifies the extra gradient term `u^T u (x^T x_t + 1) φ'_θ(x)^T φ'_θ(x_t)`. This formally shows why representation sparsity (which makes `φ_θ(x)^T φ_θ(x_t) ≈ 0`) does not guarantee local elasticity when the encoder is learnable — a simple but conceptually important observation that motivates the paper's design.

2. **Compelling regression experiment with direct NTK visualization.** On streaming sine approximation, EMLP achieves test MSE of **0.0081 ± 0.0009** versus the best baseline (SR-NN) at **0.4061** — a roughly 50× improvement. Figure 2 visualizes the NTK of EMLP dropping to near zero away from the training point while SR-NN's NTK remains flat, directly confirming local elasticity. Figure 3 further demonstrates nearly point-wise output editing, which classical MLPs cannot achieve. These experiments are the paper's strongest evidence.

3. **Broad applicability demonstrated across three domains.** The same elephant activation function (d=4 or d=8) improves performance on regression, class-incremental classification, and RL — suggesting the mechanism is robust and not task-specific.

4. **Significant improvements under strict continual learning constraints.** On Split MNIST with a single pass and no replay/task boundaries, EMLP (0.802) and ECNN (0.850) with 10K neurons substantially outperform the best comparable baseline (MLP+Streaming EWC at 0.609, CNN+Streaming EWC at 0.780). The 10K-neuron ECNN result (0.850) approaches the 0.91 of FlyModel, which requires task boundaries.

5. **Clear writing and clean mathematical exposition.** The derivation from basic principles (Section 2) to the NTK lemma to the function definition flows logically; the sparsity definition (Def 4.1) is precise and well-motivated.

## Weaknesses

### Major

1. **Theory-practice gap between Theorem 4.4 (d→∞) and actual experiments (d=4 or 8).** Theorem 4.4 proves that when d→∞ and |V(x−x_t)| > 2a·1_m, the NTK becomes exactly zero for dissimilar inputs. The paper explicitly acknowledges (Remark 4.5) that experiments use small d, and provides empirical validation that EMLP works at d=8 or d=4. However, there is **no analysis bridging the gap** — no bound on the NTK norm for finite d, no empirical check of whether the condition `|V(x−x_t)| > 2a·1_m` actually holds during training, and no guidance on how large d must be to approximate the ideal behavior. The paper is framed as theoretically grounded, but the core theoretical result applies in a regime far from the one actually used, and the connection is left qualitative.

2. **Classification evaluation scope is limited in the main paper.** The main paper presents class-incremental results only on Split MNIST (a simple 10-class digit dataset). The paper states that CIFAR-10, CIFAR-100, and Tiny ImageNet results are in the appendix (which was stripped during parsing and cannot be evaluated here). Split MNIST alone is insufficient to demonstrate that the method scales to problems where continual learning is considered genuinely challenging (e.g., longer task sequences, higher-dimensional inputs, many classes). On Split MNIST itself, FlyModel (which uses task boundaries) achieves 0.91 with 10K neurons versus ECNN's 0.850 — a non-trivial gap that the paper's framing ("excellent performance") somewhat overstates.

3. **Insufficient algorithmic baselines.** The paper adopts a strict continual learning setting (no replay, no task boundaries, single pass), but among algorithmic methods, only Streaming EWC is compared. Multiple regularization-based methods (SI, MAS, VCL) and optimization-based methods (OGD, AGEM) can be applied without replay or task boundaries and would provide a more complete picture. The paper's claim that "architectural improvement is larger than algorithmic improvement" rests on a comparison against a single algorithm-derived baseline (Streaming EWC), which is insufficient to support such a broad conclusion.

4. **No ablation or sensitivity analysis for key hyperparameters d and a.** The hyperparameters d (steepness) and a (width) are central to the method — d controls gradient sparsity, a controls output sparsity — yet there is no systematic study of how performance varies with these parameters. The paper uses d=8 for regression and d=4 for classification/RL without explanation or ablation. This makes it difficult for practitioners to understand how to set these parameters for new problems and raises questions about whether the method is fragile to this choice.

### Minor

5. **RL results are suggestive but not conclusive.** The paper claims EMLP(m=32) "matches" MLP(m=1e4) on three of four tasks. On Pixelcopter, there is a clear gap, as the paper acknowledges. Moreover, the variance (shaded areas in Figure 4) is substantial, making the "matching" claim imprecise. The paper does not report whether hyperparameters (learning rate, exploration schedule) were tuned separately for EMLP versus MLP, which could affect the comparison.

6. **Sandbagging of the sine regression baselines.** The paper reports baseline MSEs around 0.4 for a sine approximation with a 1000-neuron hidden layer — surprisingly poor for this simple function. While the EMLP result (0.0081) is genuinely impressive, the absolute baseline numbers raise the question of whether the baselines were optimally configured (e.g., learning rate, number of training steps, optimizer settings). The paper does not discuss this.

7. **SDMLP results lack standard errors.** In Table 2, SDMLP accuracy is reported without standard errors (0.69 for 1K, 0.53 for 10K), while other methods include them. This makes the comparison less rigorous.

### Trivial

8. The paper could more precisely qualify the "state-of-the-art" language in the abstract given that FlyModel (with task boundaries) outperforms the proposed method on Split MNIST.

## Nice-to-Haves

- An ablation decomposing the effect of gradient sparsity from representation sparsity (e.g., by comparing elephant activations to an activation with sparse gradients but dense outputs).
- Empirical verification of the condition in Theorem 4.4 during training (measuring |V(x−x_t)| and showing it exceeds 2a for dissimilar inputs).
- Statistical significance tests for the class-incremental results.

## Removed Points

- **"Missing related works"**: Removed because I cannot independently verify which works exist or do not exist.
- **"Reproducibility concerns about undisclosed hyperparameters"**: Training details are referenced to the appendix (which was stripped during parsing — this is a parser artifact, not an author omission).
- **"Harsh critic's claim that baselines were not tuned fairly"**: This is speculation without evidence; I cannot verify tuning procedures from the paper text.
- **"The paper should be rejected because the evaluation is too narrow"**: This claim has been retained in weakened form as a major weakness (point 2), not as a fatal flaw, because the paper does have genuine contributions beyond Split MNIST (regression NTK visualization, RL experiments).
- **"Missing appendix/CIFAR results"**: The appendix was stripped by the parser; the paper states CIFAR results exist in the appendix, which I cannot evaluate.
- **Strength Finder's claim of "state-of-the-art"**: Toned down — the method is strong among methods that do not use task boundaries, but FlyModel outperforms it.
- **Formatting/style nitpicks and typo corrections**: These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The key insight — that gradient sparsity of activation functions is a necessary complement to representation sparsity for non-linear continual learning — is genuinely the paper's own contribution and is well-motivated by the NTK derivation.

## Suggestions

1. **Bridge the theory-practice gap** by providing a non-asymptotic bound on the NTK norm for finite d, or at minimum an empirical analysis showing how the NTK norm decays with d and whether the condition in Theorem 4.4 is satisfied during training.

2. **Expand the classification evaluation** by including at least one more challenging benchmark (e.g., Split CIFAR-100 or Split Tiny ImageNet) in the main paper, and add algorithmic baselines (SI, MAS, VCL without replay).

3. **Add a systematic ablation** on d and a to show how performance varies with these parameters, providing practical guidance for setting them.

4. **Improve the regression baseline comparison** by tuning baselines more carefully or discussing why the classical baselines perform so poorly on this seemingly simple task.

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Score | Round | Comparison |
|---|---|---|---|
| /home/wg25r/review_agent/human_reviews/A1JdcLawSu.md | 3.00 | R1 | Much weaker — poorly motivated CL method |
| /home/wg25r/review_agent/human_reviews/ZHTYtXijEn.md | 2.33 | R1 | Much weaker — structural adaptation with limited evidence |
| /home/wg25r/review_agent/human_reviews/ZyMXxpBfct.md | 1.50 | R1 | Much weaker — speculative theory, no experiments |
| /home/wg25r/review_agent/human_reviews/HCCkCjClO0.md | 3.00 | R1 | Much weaker — weight approximation approach, limited scope |
| /home/wg25r/review_agent/human_reviews/qFeeJ2ZQiH.md | 4.33 | R1 | Weaker — KAN-based CL with insufficient experiments, no std devs |
| /home/wg25r/review_agent/human_reviews/YFdopzmpdr.md | 5.20 | R1 | Similar — architectural CL paper with better experiments but weaker theory |
| /home/wg25r/review_agent/human_reviews/tVNZj27pb3.md | 3.67 | R1 | Weaker — poorly motivated parameter-isolation CL |
| /home/wg25r/review_agent/human_reviews/1nHQRsb3Ze.md | 5.00 | R1 | Similar — auxiliary classifiers CL, solid but incremental |
| /home/wg25r/review_agent/human_reviews/gc8QAQfXv6.md | 9.00 | R1 | Much stronger — thorough CL analysis on LLMs, top-venue quality |
| /home/wg25r/review_agent/human_reviews/TpD2aG1h0D.md | 8.67 | R1 | Much stronger — meta-CL with rigorous theory and experiments |
| /home/wg25r/review_agent/human_reviews/AoraWUmpLU.md | 8.00 | R1 | Much stronger — thorough convergence analysis of Neural ODEs |
| /home/wg25r/review_agent/human_reviews/agPpmEgf8C.md | 8.00 | R1 | Much stronger — comprehensive RL + representation learning study |
| /home/wg25r/review_agent/human_reviews/KIq6p9iv2q.md | 5.75 | R2 | Slightly stronger — more thorough analysis of plasticity loss, but rejected |
| /home/wg25r/review_agent/human_reviews/rhhQjGj09A.md | 7.00 | R2 | Stronger — accepted poster with rigorous theory (statistical physics) |
| /home/wg25r/review_agent/human_reviews/2dhxxIKhqz.md | 6.67 | R2 | Stronger — accepted poster, function-space parameterization for CL |
| /home/wg25r/review_agent/human_reviews/Pin2kdWloe.md | 5.75 | R2 | Similar — good theoretical CL paper with limited experiments, rejected |
| /home/wg25r/review_agent/human_reviews/B9XP2R9LtG.md | 5.25 | R3 | Slightly weaker — activation sparsity laws with limited validation, rejected |
| /home/wg25r/review_agent/human_reviews/TLBPjECC5D.md | 5.25 | R3 | Similar — sparse representations for unlearning, rejected |
| /home/wg25r/review_agent/human_reviews/MEGQGNUfPx.md | 6.00 | R3 | Stronger — accepted poster with thorough empirical validation |
| /home/wg25r/review_agent/human_reviews/fHvh913U1H.md | 5.00 | R3 | Weaker — pruning-based CL for LLMs with limited evidence |

**Round 1 Bracketing**: The paper sits clearly between the weak anchors (1-3) and the strong anchors (7.5+), establishing a bracket of approximately 4–7.

**Round 2–3 Narrowing**: Compared to middle-band anchors, the paper is comparable to KIq6p9iv2q (5.75, rejected) and Pin2kdWloe (5.75, rejected) in overall quality, slightly stronger than YFdopzmpdr (5.2, rejected) and B9XP2R9LtG (5.25, rejected), and slightly weaker than MEGQGNUfPx (6.0, accepted poster). The paper's genuine theoretical contribution and compelling regression experiments place it above the 4–5 range, but the theory-practice gap, limited classification evaluation, missing baselines, and lack of hyperparameter analysis keep it below the acceptance threshold.

**Score**: 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>