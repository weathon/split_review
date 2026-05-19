- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes an efficient memory-based importance/adaptive sampling algorithm for SGD, paired with a lightweight importance function computed from the loss gradient at the network's output layer. The key ideas are: (1) a persistent per-sample importance memory updated via exponential moving average that avoids costly resampling, and (2) an analytic cross-entropy importance metric derived from the softmax outputs without requiring backward passes. Experiments on MNIST, CIFAR-10/100, ModelNet40, Oxford Flowers, and an image regression task show consistent convergence improvements over uniform sampling and the DLIS and LOW baselines.

## Strengths

1. **Algorithm design avoids the resampling bottleneck of prior work.** The persistent per-sample importance memory (Algorithm 1, lines 5 and 17) eliminates the need for the costly dataset-wide forward passes that DLIS requires at each step. The experimental figures consistently show that DLIS is slower than uniform sampling at equal wall-clock time, while the proposed method maintains a speed advantage — a concrete practical benefit over the most directly related prior method.

2. **Cheap analytic importance function for cross-entropy.** The gradient of the cross-entropy loss w.r.t. the output logits (Eq. 7) can be computed directly from softmax outputs with no backward pass or gradient tape. The inline weight-comparison figure shows this heuristic produces importance scores close to the true gradient norm, supporting the method's motivation. This simplicity is a genuine engineering virtue.

3. **Consistent empirical improvement across diverse settings.** The proposed method (both IS and AS variants) achieves lower classification error or faster convergence than uniform, DLIS, and LOW across five different datasets/tasks (MNIST, CIFAR-10, CIFAR-100, ModelNet40, Oxford Flowers), using multiple architectures (MLP, ResNet-18, ViT, PointNet, VGG-16+FC). The adaptive sampling variant (Ours AS) consistently outperforms the adaptive weighting baseline (LOW), suggesting that selecting multiple high-importance samples is more effective than re-weighting a uniform batch.

4. **Demonstration beyond classification.** The image regression experiment using a SIREN network (Fig. 7) shows that the framework extends naturally to regression tasks via autograd, broadening the scope beyond the classification focus of most prior importance-sampling work.

## Weaknesses

### Fatal
None.

### Major

1. **Single-run results without error bars or statistical evidence.** Every convergence curve in the paper is reported from a single run. The paper does not mention random seeds, number of trials, or any measure of variance. Given the inherent noise in stochastic optimization — especially with non-uniform sampling that can amplify stochasticity — single-run comparisons cannot distinguish a genuinely better method from one that benefited from random chance. This is the most significant evidential gap: the central comparative claims (that the proposed method "outperforms" baselines) rest on unreplicated observations. Without at minimum 3–5 runs with error bars (or a statistical significance test), the results do not meet the standard for a methods paper making comparative claims.

2. **Missing ablation: loss-based importance within the same memory-based algorithm.** The paper's algorithm framework (Algorithm 1) can accept any importance function. The paper claims its proposed loss-gradient-based importance is superior, but never runs the most natural ablation: using the loss itself (a simpler, standard heuristic) as the importance function within exactly the same memory-based algorithm. This is critical because prior work (Loshchilov & Hutter, 2015, cited by the paper) uses loss-based importance with a similar memory-based scheme. Without this ablation, the reader cannot determine whether the observed gains come from the proposed importance function or from the algorithm framework itself (persistent memory + EMA + normalization). Given the paper's framing emphasizes the importance function as a contribution, this omission is a significant gap in the evidence.

### Minor

3. **No quantitative wall-clock overhead measurement.** The paper's central efficiency claim is "minimal computational overhead," but no quantitative timing breakdown is provided. The time-axis convergence curves are useful but do not disambiguate where time is spent (data loading, forward pass, importance computation, backward pass, resampling). Without profiling data (e.g., ms per iteration for each method under fixed hardware), the overhead claim is asserted more than demonstrated. A single table of per-epoch or per-iteration times would substantiate the paper's main practical selling point.

4. **Ambiguity in the importance metric computation (Algorithm 2).** Algorithm 2 returns $q = \sum_{j=1}^J s_j - \mathbf{1}_{j=y_i}$. The paper refers to a "norm of the gradient" (Section 4, line 186), but the algorithm notation suggests a sum of components. If interpreted literally as $\sum_j (s_j - \mathbf{1}_{j=y_i})$, the result is trivially $0$ (since $\sum_j s_j = 1$ and $\sum_j \mathbf{1}_{j=y_i} = 1$), which cannot be a valid importance metric. This likely reflects an intended norm (L1 or L2) that is not written correctly. The mismatch between the theoretical framing (vector norm) and the algorithm pseudocode (scalar sum) is a reproducibility issue that must be resolved.

5. **Hyperparameter $\alpha$ not reported per experiment.** The momentum coefficient $\alpha$ is said to be chosen from $\{0.0, 0.1, 0.2, 0.3\}$ with "the best trade-off" selected, but it is never stated which value was used for each dataset/experiment, nor whether the same value was used for all methods. If $\alpha$ was tuned for the proposed method but fixed for baselines, the comparison could be unfair.

6. **Regression experiment is anecdotal.** The image regression task (Fig. 7) uses a single image. A single-run result on one image cannot support general claims about regression performance. Multiple images or a quantitative metric (PSNR across runs) would be needed.

7. **Oxford Flowers explanation for DLIS failure is speculative.** DLIS divergence is attributed to "sparsity in the data" (10 samples per class). This is a plausible post-hoc explanation, but no controlled experiment (e.g., varying class count or per-class sample size) is provided to test this hypothesis.

### Trivial
- The inline weight-comparison figure (Section 5.2) lacks a colorbar, scale, or quantitative correlation metric (e.g., Spearman correlation between the proposed importance and the true gradient norm), which would substantially strengthen the visual claim.

## Nice-to-Haves
- A sensitivity study for $\alpha$ (e.g., vary from 0.0 to 0.9 on one dataset) and the offset $\epsilon$ would help guide users and demonstrate robustness.
- A correlation analysis (Pearson/Spearman) between the proposed importance metric and the true gradient norm over training, compared against loss-based and DLIS-based importance, would ground the heuristic in quantitative evidence.
- An empirical plot of gradient estimator variance (trace of covariance) for each sampling method would directly test the variance-reduction motivation.
- A quantitative measure of the bias introduced by adaptive sampling (vs. importance sampling) on a small dataset would clarify the bias-convergence trade-off.

## Removed Points

These points were raised by one of the reviewers but are removed or demoted after verification against the paper:

- **"Core novelty is modest / engineering combination of known components"** — This is an opinion about contribution size, not a verifiable weakness. The paper's combination of known components is a legitimate contribution if well-validated; opinions on novelty magnitude vary by reviewer and do not constitute a concrete flaw.
- **"Equation (8) does not provide a bound"** — This is incorrect. Eq. (8) is a valid application of submultiplicativity of operator norms ($\|ab\| \leq \|a\|\|b\|$). The paper explicitly acknowledges the bound may be loose ("may not offer conclusive proof"), which is honest. The criticism is factually wrong on the mathematical point.
- **"Adaptive sampling vs. adaptive weighting distinction is blurred in experiments"** — The paper defines both clearly in Section 3.2 with distinct equations and descriptions, and evaluates both separately (Ours AS vs. Ours IS vs. LOW). The reviewer's claim is not supported by the text.
- **"Missing related work" (general)** — The paper cites Loshchilov & Hutter (2015) and Schaul et al. (2016) in Section 3 and the algorithm description. The missing experimental comparison is addressed in Weakness #2 above.
- **Missing appendix/proofs** — These are stripped by the PDF parser; the original submission contains them.
- **Formatting/style nitpicks** — Typos, whitespace, etc. are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the method, the experiments, or the framing that is not already present or implicitly contained in the paper itself. The key gap identified (missing loss-based ablation) is standard reviewer reasoning about experimental design.

## Suggestions

1. **Add multi-run results with error bars.** Run each experiment at least 5 times with different random seeds and report mean ± std or show confidence bands on convergence curves. This is the single most impactful revision.

2. **Run the missing ablation.** Compare the proposed loss-gradient importance against (a) loss-based importance and (b) random importance within the same memory-based algorithm (Algorithm 1). This will disentangle whether the algorithm or the importance function drives the gains. If loss-based importance performs similarly, reframe the contribution accordingly.

3. **Fix Algorithm 2's ambiguity.** Clarify whether the importance metric uses the L1 norm, L2 norm, or another reduction of the gradient vector. Provide the explicit formula and ensure it matches the prose description (which says "norm").

4. **Report per-iteration timing.** Add a table showing average ms per iteration (or per epoch) for uniform, DLIS, LOW, and the proposed method on at least one dataset, with a breakdown of time spent in data loading, forward pass, importance computation, and backward pass.

5. **Report $\alpha$ values per experiment** in a table or in the experimental setup paragraphs.

6. **Run the regression experiment on multiple images** with a quantitative metric (PSNR/SSIM) averaged across runs.
