## Human Reviewer 1

### Summary
Direct Optimal Action Learning (DOAL) simplifies offline RL policy extraction by decoupling optimal action computation from policy training. It achieves this by generating a synthetic "optimal" action via Q-function ascent, then uses efficient behavior cloning to train the policy to match it. This framework, which also introduces a more stable trust region hyperparameter, consistently outperforms strong baselines across various policy types and benchmarks.

### Strengths
1. Novel Policy Extraction. DOAL elegantly decouples optimal action computation from policy training, sidestepping complex backpropagation through generative models by reframing optimization as simple behavior cloning.
2. Improved Hyperparameter Stability. Reinterpreting the BRAC trade-off coefficient $\alpha$ as a normalized trust region $\delta$, backed by Proposition 2 and the Batch-Normalizing Optimizer, offers a more interpretable and stable hyperparameter. Empirical evidence shows $\delta$ can be shared across algorithms, simplifying tuning.
3. Strong Empirical Results. DOAL achieves consistent and significant performance gains across 15 challenging offline RL tasks, notably improving over meticulously tuned baselines, which enhances the credibility of its effectiveness.

### Weaknesses
1. Inconsistency in Theorems and practical implementation: Proposition 1 establishes the gradient equivalence by defining $a^{\text {target }}$ using the Q-gradient evaluated at the policy's output, $\pi_\theta(s)$. However, the paper then argues this is conceptually inconsistent and, in the final DOAL objective (Eq. 16), defines the target using the Q-gradient evaluated at the data action, $a$. While this change is key to decoupling, the original equivalence from Proposition 1 no longer strictly holds, leaving a gap in the theoretical justification for the final objective.
2. The paper introduces the Batch-Normalizing Optimizer and the trust-region parameter $\delta$ as a more stable replacement for the sensitive hyperparameter $\alpha$ from the BRAC objective. Despite this, the final DOAL actor loss in Equation 15 still contains an $\alpha$ parameter, which is described as a controller for the "learning rate of actor" and is copied from a prior work. This is confusing. It is unclear how this $\alpha$ interacts with $\delta$ and why it is still necessary if the optimization trade-off is now managed by the trust region. This ambiguity detracts from the otherwise clean narrative of simplifying hyperparameter tuning.
3. In Table 1, some experimental results with D- still behind the vanilla algorithms. Also, the reviewer suggests that the authors to better present this table such as showing the final averaged performance.

### Questions
see weakness

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
2

---

## Human Reviewer 2

### Summary
The paper proposes Direct Optimal Action Learning (DOAL), a framework for offline RL that reframes behavior-regularized actor–critic training as directly learning an “optimal” action target for each data point and then imitation-learning that target using losses native to the policy family (Gaussian Policies, flow policies and diffusion policies). This avoids costly backpropagation through iterative sampling chains in expressive policies (diffusion/flow), while keeping value guidance from the learned Q-function. The authors also introduce a Batch-Normalizing Optimizer that sets a dataset-level “trust region” (δ) to control how far targets move from behavior actions, aiming to make tuning more interpretable and consistent across policy distributions. Empirically, across 15 tasks from OGBench and D4RL Adroit, DOAL variants match the performance of strong baselines (IQL/FQL/TrigFlow) with shared, environment-level hyperparameters.

### Strengths
The paper presents a novel and elegant reformulation of behavior-regularized actor–critic training by directly learning an optimal per-sample action target and then imitating that target with policy-native losses, which removes the need for costly backpropagation through iterative sampling chains in flow and diffusion-based policies. This idea is conceptually clean, improves computational practicality for expressive policy classes, and introduces a trust-region–style batch normalization that provides a more interpretable and stable hyperparameter compared with traditional BRAC scaling. Empirically, across OGBench and D4RL Adroit, the method achieves performance comparable to strong baselines (IQL/FQL/TrigFlow) while using shared environment-level hyperparameters, suggesting that the proposed reformulation maintains effectiveness without extensive tuning

### Weaknesses
1. Writing & clarity: The paper has noticeable grammatical issues, inconsistent notation, and several typos, which make the narrative harder to follow; The main results table is dense and difficult to scan, hindering quick cross-method comparisons across policy families and environments; consider adding per-method aggregates (e.g., mean/median across tasks) to improve readability.

2. Shallow experimentation: The evaluation covers only 15 tasks total—6 from D4RL Adroit and 9 from OGBench. Moreover, results are averaged over just 4 seeds (D4RL) and 3 seeds (OGBench), which weakens statistical confidence and robustness of the findings.

3. No compute analysis: A central claimed benefit is reduced computational cost by avoiding backpropagation through iterative diffusion/flow sampling chains, yet the paper provides no wall-clock or memory measurements to substantiate this. Even a simple per-epoch time or training-step latency comparison against BRAC-style training would clarify the practical value.

4. Missing ablations: There are no targeted ablations to disentangle contributions from (i) direct optimal-action targets, (ii) the Batch-Normalizing optimizer; the current analysis discusses hyperparameters but doesn’t isolate causal impact on performance.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper presents Direct Optimal Action Learning (DOAL), a framework that replaces end-to-end BRAC-style policy gradients through the value network with a two-step policy extraction:
(1) compute an “optimized” target action per data point via a first-order step on the Q-function;
(2) train the policy to imitate this target with a behavior-native loss (e.g., Gaussian MSE, flow matching, diffusion reconstruction).
This yields distribution-agnostic policy extraction without backpropagating through iterative samplers used by diffusion/flow policies. The authors reinterpret the BRAC trade-off as a trust region and introduce a Batch-Normalizing Optimizer that scales the action step by the batch norm of |\∇ₐQ|, controlled by a single hyperparameter δ. Experiments on OGBench and D4RL Adroit show consistent improvements of DOAL variants (Gaussian, flow, diffusion) over their respective baselines, and analyze Max-Q sampling and the role of candidate count 
𝑛
sample
n
sample
	​

.

### Strengths
Simple, general recipe for policy extraction. Shows BRAC’s policy gradient can be reframed as target-matching against an action updated by ∇ₐQ, enabling training with any policy family’s native loss (Gaussian/flow/diffusion) and avoiding gradients through multi-step samplers.

Interpretable trust region. The Batch-Normalizing Optimizer controls expected step size via δ, normalizing by batch statistics of |\∇ₐQ|²—cleaner than tuning BRAC’s 𝛼.

Covers expressive policies. Instantiates DOAL for Gaussian, Flow Matching, and Diffusion policies with concrete objectives (e.g., DIQL, DIFQL, DTrigFlow).

### Weaknesses
Novelty is mainly a reinterpretation plus a practical recipe.
The equivalence that turns BRAC into target-matching is neat but technically light. Stronger differentiation from value-guided diffusion/flow, energy guidance, and behavior-regularized objectives would clarify what DOAL achieves beyond engineering convenience.

Value-quality dependence and limited uncertainty handling.
DOAL targets rely on ∇𝑎𝑄 at data actions; there’s no integrated uncertainty-aware step control (ensembles, variance-based scaling) for OOD safety, which matters in offline regimes.

Benchmark scope and stability.
While OGBench and Adroit are covered, Adroit volatility and late-training collapse are reported without a full diagnosis, weakening stability claims.

### Questions
1. Target evaluation point. You compute ∇𝑎𝑄 at data actions to avoid a mismatch with 𝜋𝜃(𝑠). Have you compared evaluating at 𝜋𝜃(𝑠） (or hybrids) and quantified the difference?

2. δ scheduling. Does adaptive or annealed δ improve late-training stability on Adroit where collapses occur?

3. Value backbones. What happens when pairing DOAL with ReBRAC-style critics—do gains persist?

4. High-D actions. For diffusion/flow in high-D action spaces, does anisotropy in ∇𝑎𝑄 hurt target-matching? Any whitening or per-dimension scaling beyond batch normalization? 

5. Max-Q proposals. Beyond sampling from 𝜋𝜃, can proposal refinement (e.g., short Langevin steps guided by Q) reduce noise sensitivity for large 𝑛 samples?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes Direct Optimal Action Learning (DOAL), a framework for offline RL that avoids backpropagating through multi‑step generative policies (diffusion/flow) when using BRAC‑style actor objectives. The key observation is that the BRAC policy gradient is (approximately) equivalent to minimizing the distance between the policy output and a single “optimal action” target derived via a first‑order update from the dataset action. DOAL computes that target directly from \nabla_a Q_\phi(s,a) (evaluated at the dataset action) and then trains the policy to imitate the target using a loss native to the policy family (e.g., flow matching or a diffusion loss), thus decoupling target computation from the policy’s sampling chain. The paper further replaces the sensitive BRAC coefficient \alpha with a Batch‑Normalizing Optimizer that scales the update so that the expected squared step size equals a user‑chosen trust‑region parameter, and presents Algorithm 1 showing integration with IQL for value learning. Experiments on 9 OGBench tasks and 6 D4RL Adroit tasks compare Gaussian, flow, and diffusion policies show mixed results.

### Strengths
- Clear, unifying insight and simple objective. This paper makes explicit that BRAC’s policy gradient equals the gradient of a squared‑error to a target action. This clarifies what end‑to‑end training is doing and motivates learning the target directly, which is easy to implement and compatible with any policy class.
- DOAL avoids backprop through iterative sampling chains, which is particularly important for diffusion/flow actors by supervising with native behavior losses. This makes the approach broadly plug‑and‑play with flow/diffusion policies.
- Hyperparameter reinterpretation via a trust region. The Batch‑Normalizing Optimizer replaces a brittle \alpha search with an interpretable \delta that sets an expected squared update magnitude; the denominator’s batch statistic stabilizes scale across tasks.

### Weaknesses
- To me, it's unprincipled to replace a’ that which should be sampled from the policy with the dataset action a, the paper does not provide a solid justification for this change (cf. Prop. 1/Eq. 13). In addition, the derivation appears to hinge on an L2 BC loss—how does the argument extend to other losses (e.g., log-likelihood, flow-matching, diffusion objectives)? 
- Results are not uniformly stronger. The claim that DOAL “consistently improves performance” over strong baselines is only partially supported. For example, DTrigFlow is dramatically worse on cube‑single‑play, and DIQL is broadly weaker than IQL on many tasks. 
- Efficiency claims lack measurement. A central motivation is avoiding BPTT through iterative samplers, but there are no wall‑clock time, memory, or gradient‑call counts comparing DOAL to TrigFlowQL/FQL under matched hardware.
- The observation of Max-Q sampling does not constitute a novel contribution. Prior work (e.g., Q-chunking) already formalizes that the candidate count N in Max-Q sampling implicitly sets the level of KL regularization between the induced policy and the proposal/sampling distribution. From this perspective, increasing N weakens the effective regularization and can degrade performance, so it is unsurprising that “the bigger N, the better” does not hold. Please cite these results.. 
- Scope of value learners. Most experiments couple DOAL with IQL for a controlled study, but since BRAC‑style methods remain strong (e.g., ReBRAC in Table 1). Is this policy extraction approach still improve on other value learners?

### Questions
see Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
5