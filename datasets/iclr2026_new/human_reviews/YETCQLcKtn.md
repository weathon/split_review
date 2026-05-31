## Human Reviewer 1

### Summary
This paper proposes a novel on-policy algorithm named PolicyFlow. Its core contributions are:

1) Efficient importance ratio approximation: Instead of computing the full flow path during training updates, PolicyFlow approximates importance ratios using velocity field variations along a simple "interpolation path". This significantly reduces computational overhead.
2) Brownian entropy regularizer: To prevent potential mode collapse and encourage diverse behaviors , the authors introduce a lightweight entropy regularizer inspired by Brownian motion. It implicitly increases policy entropy by shaping the velocity field , avoiding the significant cost of explicit entropy or log-likelihood computation.

The authors conducts experiments in diverse environments, including MultiGoal, IsaacLab, and MuJoCo Playground. Particularly on the MultiGoal task, PolicyFlow demonstrates its ability to capture diverse multimodal action distributions.

### Strengths
1) The core contribution of this paper is a novel and efficient importance ratio approximation method. By evaluating velocity field differences along a simple interpolation path, it avoids the significant overhead of solving ODEs and backpropagation during PPO updates, making the application of CNF policies computationally feasible. Additionally, inspired by physical processes, the paper proposes a novel Brownian regularizer, which provides a lightweight means of preventing mode collapse by directly acting on the velocity field, thereby avoiding expensive entropy calculations.
2) The method of this paper performs well on MultiGoal (Figure 1) and demonstrates high computational efficiency.

### Weaknesses
1) The baselines are limited, comparing only against PPO and FPO. Methods like GenPO and DPPO are missing. Furthermore, the method does not show an advantage in half of the tasks in the IsaacLab benchmarks.

2) There are too many hyperparameters, making reproduction difficult. Beyond standard PPO hyperparameters, it also involves the sampling strategy for $t$, noise variance learning, time or observation embedding dimensions, integration steps, and $w_b$, $w_g$, among others. The paper provides limited discussion on the sensitivity to these hyperparameters and the default strategies used.

3) No code available.

### Questions
1) Table 5 shows that using different interpolation paths leads to drastically different performance on the MultiGoal task. This suggests that the choice of interpolation path is another critical design decision. Why does the paper default to the Rectified-Flow path? What advantages does it have, in theory or practice, compared to other paths?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
5

---

## Human Reviewer 2

### Summary
The paper introduces PolicyFlow, an on-policy RL method that uses continuous normalizing flows for more expressive policies. It avoids expensive backpropagation through flow trajectories by using an interpolation-based importance ratio. A Brownian regularizer is added to encourage exploration. Experiments on MuJoCo, IsaacLab, and MultiGoal show stable and competitive results compared to PPO and FPO.

### Strengths
The paper proposes an interesting and original idea — combining continuous normalizing flows with on-policy policy optimization in a practical way.
The paper is clearly written, with intuitive explanations and helpful figures that make the method easy to understand.

Experiments cover multiple benchmarks (MuJoCo, IsaacLab, MultiGoal) and show consistent improvements over PPO and FPO.

Overall, the work is technically solid and provides a promising direction for expressive yet stable flow-based policy learning.

### Weaknesses
Methodological Weaknesses:
1. The proposed interpolation-based estimation of importance ratios is only heuristic; the paper does not quantify the bias introduced or establish convergence guarantees. Providing analytical error bounds or controlled experiments comparing with exact estimators would strengthen credibility.
2. The Brownian regularizer, while novel, lacks clear motivation and comparison with existing entropy regularizers (e.g., Haarnoja et al., 2018; Chao et al., 2024). Its empirical benefit is only qualitatively shown; a quantitative ablation isolating its contribution is necessary.


Experiments Weaknesses:
1. The experimental evaluation is also fragmented—PolicyFlow is compared with FPO on MuJoCo and PPO on IsaacLab, preventing a unified cross-method assessment. 
2. Including all three under identical settings would clarify relative efficiency and expressivity. Furthermore, results are averaged over five seeds without significance testing
3. The MuJoCo Playground evaluation covers only a moderate subset of tasks (e.g., BallInCup, CheetahRun, FingerTurnHard, ReacherHard) but omits the most challenging or high-dimensional environments such as Humanoid or Walker. This limits claims of scalability to complex continuous-control domains.

Minor Issues:
1. some notations is not well defined: Sec. 3. $s,a$ is not defined before using. $p_{\pi}(s)$ is never defined. $\pi^*$ is mentioned but not clearly defined.

### Questions
Can you clarify whether the interpolation-based importance ratio introduces any noticeable bias? It would help to know if you’ve compared it against an exact or less-approximated version.

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper introduces PolicyFlow, an on-policy reinforcement learning algorithm that replaces the standard Gaussian policy used in PPO with a continuous normalizing flow parameterized by ordinary differential equations. This modification aims to enhance expressiveness for complex or multimodal action distributions. The approach also incorporates a Brownian motion-inspired implicit entropy regularizer to promote exploration without relying on explicit policy entropy terms. The paper compares PolicyFlow against PPO and other flow-based policy optimization methods, such as FPO, reporting similar or slightly improved empirical results on selected benchmarks.

### Strengths
- Addresses the expressiveness limitation of Gaussian policies by exploring normalizing flows for policy representation.
- Introduces a Brownian motion-based entropy regularizer to encourage implicit exploration.
- Presents a clear and structured implementation based on PPO.
- Includes runtime and parameter analyses, offering transparency on computational cost.
- Demonstrates engagement with related work, including comparisons to other flow-based methods.

### Weaknesses
- The reported empirical results are very close to PPO, providing limited evidence of improvement.
- The additional model complexity and slower runtime are not justified by corresponding performance gains.
- The theoretical connection between the flow-based representation and policy gradient optimization is underdeveloped.
- The motivation for emphasizing FPO comparisons is not well justified relative to the paper’s main objective.
- Benchmark evaluations and variance reporting are incomplete, limiting the strength of the experimental conclusions.

### Questions
**Detailed Review:**

The paper proposes PolicyFlow, which replaces the Gaussian policy distribution in PPO with a continuous normalizing flow modeled through ordinary differential equations. The design aims to capture multimodal action distributions and improve policy expressiveness. The use of a Brownian motion-inspired implicit entropy regularizer seeks to enhance exploration without introducing explicit entropy terms in the loss.

Although this approach is conceptually sound, the paper does not provide strong empirical or theoretical evidence that PolicyFlow meaningfully improves over PPO. The observed results in Figures and Tables suggest comparable performance rather than clear gains. The discussion of results should better address why these similarities occur and whether the proposed approach offers other advantages, such as stability or robustness.

The focus on comparison with FPO is noted, but it is unclear why this method receives particular attention when the central comparison should remain with PPO. It would be helpful to clarify the methodological differences that justify this choice. The analysis could also include visualization or theoretical examples that demonstrate how the normalizing flow structure affects action representation or optimization dynamics.

While the Brownian entropy regularizer is an appealing idea, its effect on exploration and stability is not quantified. A comparison with standard entropy regularization would help assess whether it provides genuine benefit or simply replicates existing behavior. Similarly, the discussion on computational efficiency should more clearly address the trade-offs between the added parameterization and any observed gains in performance.

The runtime and parameter analyses are appreciated, as they help contextualize the computational implications of the proposed method. However, since the improvements are small and the training time increases, the practical benefit of adopting PolicyFlow remains uncertain. The lack of variance reporting in Tables 1 and 2 also limits confidence in the consistency of the results.

In summary, the idea of integrating normalizing flows into policy gradient methods is interesting and potentially valuable, but the paper does not yet establish sufficient justification, theoretical insight, or empirical advantage to support its adoption.

**Questions:**

1. What is the specific benefit of using normalizing flows over Gaussian policies in terms of policy expressiveness and action representation?
2. How does the Brownian entropy regularizer contribute to exploration compared with standard entropy regularization?
3. What is the motivation for emphasizing comparisons with FPO, and how do these comparisons support the main claims of the paper?
4. How does PolicyFlow perform in terms of computational cost and sample efficiency relative to PPO?
5. Could the authors include a simple theoretical or illustrative example showing how the flow-based policy captures multimodal actions more effectively?
6. Are the experimental results averaged over multiple runs, and if so, could variance be reported to strengthen the reliability of the findings?
7. What is the runtime difference between **sampling action** from the normalizing flow policy and from the Gaussian policy?
8. Under what conditions does PolicyFlow provide a clear improvement over PPO, and how does this relate to its theoretical formulation within policy gradient optimization?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper introduces PolicyFlow, a novel on-policy reinforcement learning algorithm designed to leverage the expressive power of Continuous Normalizing Flows (CNFs) for policy representation within a PPO-like framework.  They show how to avoids the need for full ODE simulation and backpropagation during the policy update and how to implement the entropy regularization in a smart way in the generative policy situation by imitating the Brownian motion. They finally show improved performance compared to the traditional PPO and related flow-based PPO method.

### Strengths
1. The authors demonstrate how to bypass the computationally expensive full ODE simulation and backpropagation typically required when using Neural ODE-based policies with a PPO objective. Their key insight is to use an efficient approximation of the importance ratio, enabling stable on-policy training without the standard computational bottlenecks.
2. the paper introduces a lightweight "Brownian regularizer" to enhance behavioral diversity and mitigate mode collapse.

### Weaknesses
1. How is the initial flow matching model for the method in this paper obtained? What is the impact of the initial model's performance on the overall method?

2. The target distribution of the flow-based policy changes dynamically during training, yet the objective function samples only a single t from the path at each step. Could this, due to the varying sample weights (different values of A) for each t along the path, prevent the model from learning an effective distribution?

3. A sensitivity analysis experiment should be conducted on the parameters used in the algorithm, e.g, Brownian regularizer weight wb.

### Questions
1, since the first-order approximation of the importance ratio may introduce bias into the gradient estimate, have you empirically assessed its impact? For example, did you observe any degradation in performance or training instability as the PPO clipping range ϵ increases, which would amplify the approximation error?

2, could you clarify the sampling strategy for tk (Algorithm 1, lines 15–16)? In the final experiments, did you use uniform sampling U[0, 1], and if so, did it perform better than sampling from the discrete simulation time points?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4