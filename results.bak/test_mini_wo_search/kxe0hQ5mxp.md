Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper studies how activation functions impact catastrophic forgetting in neural networks. It derives that for non-linear approximations, sparse representations alone are insufficient to control forgetting — sparse gradients are also needed to make the neural tangent kernel (NTK) locally elastic. Based on this insight, the authors propose "elephant activation functions" (bell-shaped, with tunable width and slope) that produce both sparse function values and sparse gradients. Experiments in streaming regression (50× MSE improvement over sparse-representation baselines), class-incremental learning on Split MNIST, and four RL tasks demonstrate that simply replacing classical activations with elephant activations reduces forgetting under strict streaming constraints.

## Strengths

- **Theoretical derivation connecting gradient sparsity to local elasticity goes beyond prior work.** Lemma 1 derives the NTK for a one-hidden-layer non-linear network, revealing an explicit gradient-dependent term beyond the representation inner product. Theorem 1 then proves that with elephant activations (sparse in both value and derivative), the NTK becomes exactly zero for sufficiently dissimilar inputs when \(d \to \infty\), satisfying Property 3 (local elasticity). Prior work (Liu et al. 2019, Shen et al. 2021) only considered sparse representations, making this a formally grounded extension.

- **The streaming regression experiment provides striking direct evidence of the claimed mechanism.** EMLP achieves MSE 0.0081 vs. 0.4061 for the best sparse-representation baseline (SR-NN) on approximating \(\sin(\pi x)\) — a 50× improvement. Figure 3 visually confirms that the NTK of EMLP decays rapidly away from the training point, while SR-NN's NTK does not. Figure 4 further shows that this local elasticity enables nearly point-wise output editing (updating the function at one input without globally distorting it), directly validating the theoretical prediction.

- **Competitive class-incremental learning under the strictest streaming constraints.** On Split MNIST, EMLP/ECNN achieves 0.723/0.732 (1K neurons) and 0.802/0.850 (10K neurons) using single-pass training without replay buffers, task boundaries, or pre-training. The paper correctly identifies that no prior method operates under all these constraints simultaneously — FlyModel requires task boundaries, SDMLP uses 500 dataset passes — isolating the contribution of the activation function itself.

- **Formal sparsity measure for activation functions.** Definition 1 provides a clean, continuous-domain measure of function sparsity \(S(\sigma)\), and verifies that both the elephant function and its derivative are 1-sparse (while classical activations like tanh are 0-sparse and ReLU is \(\frac12\)-sparse). This gives a rigorous basis for comparing activations on the property the paper argues is essential.

## Weaknesses

### Fatal
None.

### Major

- **Results for CIFAR10, CIFAR100, and Tiny ImageNet are claimed but not presented.** Section 5.2 states "We test various methods on several standard datasets — Split MNIST, Split CIFAR10, Split CIFAR100, and Split Tiny ImageNet," yet only Split MNIST results appear (Table 2). No table, figure, or text reports performance on any larger dataset. This directly undermines the paper's conclusion that the method has "broad applicability" for class incremental learning. If these results exist in a corrupted or appendix section, the authors must clearly present them; if not, the evaluation is incomplete.

- **Theorem 1 requires \(d \to \infty\) but experiments use \(d=4\) or \(d=8\).** The paper acknowledges this gap in a remark ("even when \(d\) is a small integer, EMLPs still exhibit local elasticity") but provides no non-asymptotic analysis, no bound on how local elasticity degrades with finite \(d\), and no quantification of the approximation error. The theory therefore offers intuition rather than a rigorous explanation of the experimental results. While this pattern (asymptotic theory + finite-d experiments) is common in ML, the gap is larger here because \(d=4\) is very far from infinite and the theorem's strong condition (\(\lvert V(x - x_t)\rvert \succ 2a\mathbf{1}\)) may also not hold in practice.

### Minor

- **Properties 1–3 are derived for a single gradient step, but catastrophic forgetting arises from many steps.** The analysis shows that if each individual update preserves memory for dissimilar inputs (Property 3), then forgetting is controlled — but the paper does not discuss whether the small approximation errors from each step accumulate over many steps to cause collapse. This gap weakens the link between the one-step NTK analysis and the empirical multi-step results.

- **The RL evaluation is thin relative to the claims.** Only one base algorithm (DQN), one architecture (MLP with 1000 hidden units), and four simple tasks are tested. There is no comparison against regularization-based RL methods (e.g., EWC applied to DQN) that also operate under memory constraints. The claim that "EMLP matches MLP with large buffer" holds for only 3 of 4 tasks (MountainCar, Acrobot, Catcher), with Pixelcopter showing a clear gap. The evidence is suggestive but far from conclusive.

- **CNN architecture for ECNN is underspecified.** The paper states "a simple CNN" without detailing the layer structure, kernel sizes, stride, pooling, or how the elephant activation is applied (after which layers). This makes the class-incremental learning results difficult to reproduce independently.

### Trivial

- **The sparsity definition (Definition 1) operates on a 1D input domain, measuring the fraction of \([ -C, C ]\) where \(|\sigma(x)| \le \epsilon\).** While this is mathematically clean, it characterizes the function's sparsity on its domain, not the sparsity of the resulting representations for high-dimensional inputs. The connection between "1-sparse in this 1D sense" and "representations/gradients are sparse for high-dimensional inputs" is intuitive but not formally bridged.

## Nice-to-Haves

- Add an ablation study systematically varying \(a\) and \(d\) in the streaming regression setting to validate that these parameters directly control the degree of local elasticity (e.g., measure NTK decay rate as a function of \(a, d\)).
- Add an ablation comparing activations with only sparse function values (e.g., a thresholded variant) vs. only sparse gradients (e.g., a squashing activation with near-zero derivative over most of the domain) to test whether *both* types of sparsity are necessary as claimed.
- Include a fairness check: verify whether the MLP/CNN baselines would improve with a brief hyperparameter search (learning rate, optimizer) in the streaming regression setting.

## Removed Points

These points were raised by reviewers but are removed from the main assessment for the reasons given. Read with caution — they may reflect misunderstandings or subjective judgments rather than verifiable weaknesses.

- **"The class incremental learning comparison is fundamentally unfair"** — The paper is transparent about which constraints each baseline meets (single pass, task boundaries, buffer). SDMLP and FlyModel are included as strong references with their limitations explicitly stated. The critic's characterization of a "contrived setting" is a subjective judgment, not a verifiable flaw.
- **"Baselines may be poorly tuned" / "tuning issues"** — Speculative. The claim that Streaming EWC "hurts plain MLP on 10K neurons" (0.621→0.609) could indicate that EWC's regularization is unnecessary for wider networks, not poor tuning. The streaming regression baselines use standard architectures and optimizers with no evidence of suboptimal configuration.
- **"Missing hyperparameter sensitivity / search details"** — A generic reproducibility nitpick that applies to most papers. The paper reports standard errors over multiple runs, which is standard practice.
- **"Missing statistical significance tests"** — Standard errors are reported for all experiments; formal hypothesis testing is not standard practice for all experimental paradigms used here.
- **"Lack of non-asymptotic analysis"** — This is already captured under the Major weakness (theory-practice gap). The critic's framing as "effectively a heuristic motivation, not a valid theoretical grounding" overstates the issue; the theory provides a clear intuition and the experiments confirm it works in practice.
- **"The streaming regression gap is not convincingly explained"** — The paper does provide an explanation (local elasticity via NTK analysis, supported by Figure 3) and visual evidence. This criticism speculates without evidence that baselines could match EMLP with better tuning.
- **"Not discussing prior work on designing activation functions for continual learning"** — I cannot verify the existence of such prior work; papers are evaluated on their own merits.
- **Strength Finder claim about "the single most important piece of evidence"** — This is a subjective prioritization and is removed from the strength list.

## Novel Insights

None beyond the paper's own contributions. The reviewer comments do not surface a perspective on the work that the paper's own framing already provides.

## Suggestions

1. **Complete the class-incremental evaluation.** Report results on at least one larger benchmark (e.g., Split CIFAR-100) under the same strict constraints to support the claim of broad applicability. If these results exist in a section not visible in the current manuscript, clearly reference them.
2. **Strengthen the theory-practice bridge.** Provide a non-asymptotic bound on the NTK inner product \(\langle \nabla f(x), \nabla f(x_t) \rangle\) in terms of \(d\), \(a\), and the distance \(\|x - x_t\|\). Even a rough characterization of how local elasticity degrades with finite \(d\) would substantially increase the theory's explanatory power.
3. **Expand the RL evaluation.** Add at least one regularization-based RL method (e.g., online EWC for DQN) as a baseline under the same buffer constraints, and report results on 1–2 additional environments of higher difficulty.
4. **Provide full architecture details.** Specify the CNN structure for ECNN (layer types, kernel sizes, activation placements, initialization) to enable independent reproduction.
5. **Add an ablation separating the two forms of sparsity.** Design an activation with sparse values but non-sparse gradients (and vice versa) to test the core claim that *both* are necessary.

## Score and Decision

**Overall assessment:** The paper proposes a genuinely novel idea — designing activation functions with dual sparsity (representations + gradients) for continual learning — and provides a clean theoretical motivation plus a striking streaming regression result. However, the evaluation is incomplete in two important ways: (1) class-incremental results are only shown for Split MNIST despite claiming tests on three larger datasets, and (2) the theory only covers the \(d \to \infty\) regime while experiments use \(d=4\) or \(d=8\) with no non-asymptotic analysis. The RL evaluation is also thin. The core contribution is credible and potentially significant, but the evidence does not yet support the strong claims of "broad applicability." Major revision addressing the missing results and the theory-practice gap is needed before the paper can be accepted.

- Originality: High
- Importance of research question: High
- Claims support: Moderate (strong for regression, limited for classification, weak for broad applicability)
- Soundness of experiments: Moderate (incomplete dataset coverage, limited baselines in RL)
- Clarity of writing: Good
- Value to community: Moderate–High (if validated on larger benchmarks)

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>