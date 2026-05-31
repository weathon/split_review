## Summary

This paper presents **Direct Optimal Action Learning (DOAL)**, a framework for policy extraction in offline RL. The key insight (Proposition 1) is that the reparameterized policy gradient of Behavior-Regularized Actor-Critic (BRAC) can be reinterpreted as learning to imitate a target action obtained by taking a gradient ascent step on the Q-function from a data action. DOAL decouples target computation from policy training, enabling efficient, policy-native losses (e.g., flow matching) without costly end-to-end backpropagation through iterative sampling chains. The paper also introduces a **Batch-Normalizing Optimizer** that normalizes gradient updates by batch statistics, yielding a more interpretable hyperparameter δ (trust region magnitude). Additionally, the paper identifies the number of MaxQ sampling candidates (n_sample) as a previously underappreciated hyperparameter that balances distributional coverage against Q-value overestimation bias.

---

## Strengths

- **Clean theoretical insight with practical payoff.** Proposition 1 cleanly establishes that BRAC implicitly trains the policy to match a gradient-shifted target action, motivating DOAL as a principled decoupling of target generation from policy learning. This unlocks the use of any behavior-cloning loss—including flow matching—without BPTT through iterative sampling chains, which is the core computational bottleneck in prior work (FQL, EDP, etc.).

- **Breadth and versatility.** DOAL is demonstrated across three policy classes (Gaussian, flow, diffusion) and three Q-value frameworks (IQL, Q-learning, ReBRAC), with each DOAL model nesting its baseline as the δ=0 special case. This systematic coverage is more convincing than a single-architecture result.

- **Strong empirical performance on OGBench.** With proper n_sample tuning, both baseline (IFQL/MFQL/TrigFlow) and DOAL models outperform the previously strongest published result (FQL) across the 9 OGBench tasks in aggregate, sometimes by large margins (e.g., scene-play: FQL 76 vs DMFQL 90, DMFReBRAC 92).

- **Computational efficiency.** The DOAL overhead over MaxQ baselines is precisely one additional Q forward + backward pass (18 vs 16 total calls for DMFQL vs MFQL), with verified actual runtimes (37 vs 35 min). This is far more efficient than BPTT (61 min, 37 calls) with superior stability.

- **Identification of n_sample as a critical hyperparameter.** Proposition 3 and the surrounding analysis give a principled explanation (maximization bias from noisy Q-estimates) for why "more samples is not always better" in MaxQ sampling—a point overlooked or misunderstood in prior literature.

---

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistent gains on D4RL/Adroit.** On the 6 Adroit tasks under IQL (Table 1), DOAL models show no improvement or slight degradation over their baselines, and even under Q-learning (Table 2), DMFQL performs marginally worse than MFQL on several tasks. The only consistent D4RL gains appear under ReBRAC regularization. This substantially limits the generality of the DOAL claim—the method's effectiveness is critically dependent on Q-function quality, which is not guaranteed in practice.

2. **The δ hyperparameter still requires task-group–specific tuning.** While δ varies less than α within a benchmark, Table 3 shows that δ ranges from 0.03–0.1 on OGBench and 0.0003–0.003 on D4RL—a 100× range across settings. The paper acknowledges this but frames it as "easier to search for," which is only marginally better. The claim that δ is "shareable across policies" is within the same task and value function, not across benchmarks.

3. **Proposition 1 is limited to MSE loss and deterministic policies, yet the practical method uses flow matching with stochastic policies.** The formal grounding of DOAL holds tightly only in the MSE-deterministic setting. The generalization to flow/diffusion policies with velocity matching loss is motivated intuitively but not formally justified, leaving an important gap between theory and practice.

### Minor

1. **Batch normalization benefit is arguably marginal.** Figure 3 shows that batch gradient norms are approximately stable throughout training, and the paper itself states: "if the gradient statistics is stable, you can always get the same result by having g(s,a) = C·∇_a Q_φ(s,a)" (Section 5.3). This undermines the practical necessity of the batch-normalization scheme—it is essentially equivalent to a fixed learning rate rescaling in stable regimes.

2. **Large and inconsistent standard deviations in Table 1.** Several entries show standard deviations of ±23 or ±24 (e.g., IFQL: 6±23, 16±29, 40±26), suggesting bimodal or near-zero results for multiple seeds. Summing totals across tasks with such variability makes aggregate comparisons less reliable.

3. **Instability acknowledged but unexplained.** The paper notes that DTrigFlow and ETrigFlow dropped performance on antmaze-large due to "two seeds that have very low performance," but does not investigate why DOAL may destabilize training in some configurations—an important open question given the method's practical claims.

### Trivial

- Proposition 3 is presented informally and relies on a standard result about the maximum of many noisy Gaussians growing as √(2 log n). The insight is useful contextually but is not a novel theoretical contribution.

---

## Nice-to-Haves

- An investigation into why IQL-based Q-function gradients are unreliable for DOAL (and whether gradient regularization of IQL itself could fix this) would significantly strengthen the paper.
- A sensitivity plot showing performance vs. δ across representative tasks would make the "δ is easier to tune" claim more concrete and verifiable.
- Extending the formal equivalence in Proposition 1 to stochastic policies and non-MSE losses, even approximately, would close the gap between theory and the main experimental setup.

---

## Novel Insights

The most genuinely novel contribution is the reinterpretation of the BRAC gradient as learning to match a gradient-shifted target action, and the resulting decoupling that allows arbitrary behavior-cloning losses for expressive generative policies. This resolves a real practical bottleneck (BPTT through iterative sampling) with a theoretically grounded and computationally cheap alternative. The insight that optimal n_sample for MaxQ sampling is finite—with a principled explanation via Q-value maximization bias—is also a useful empirical and conceptual contribution that corrects prior guidance in the literature.

---

## Suggestions

- Provide a theoretical or empirical analysis of when Q-function gradients are reliable enough for DOAL to work—this is the crux of the method's applicability and is currently left at "investigate in future work."
- Report per-task δ selection explicitly across all experiments (not just 4 environments) to allow readers to assess the true hyperparameter sensitivity.
- Include an ablation comparing batch-normalized δ vs. a fixed learning rate C on a representative task to demonstrate whether batch normalization actually helps in practice.

---

## Score and Decision

DOAL is a solid method paper with a clean central insight, a comprehensive experimental study covering multiple policy families and Q-value frameworks, and genuine state-of-the-art results on OGBench. The theoretical contribution is modest but sufficient, and the claims are largely supported. The most significant limitations are the inconsistent gains on D4RL (calling into question broad applicability) and somewhat overstated benefits of the batch-normalizing scheme. These are real weaknesses but do not invalidate the core contribution, which is practically useful and clearly presented.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>