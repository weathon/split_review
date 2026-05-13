# Reward Dimension Reduction for Scalable Multi-Objective Reinforcement Learning

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
In this paper, we introduce a simple yet effective reward dimension reduction method to tackle the scalability challenges of multi-objective reinforcement learning algorithms. While most existing approaches focus on optimizing two to four objectives, their abilities to scale to environments with more objectives remain uncertain. Our method uses a dimension reduction approach to enhance learning efficiency and policy performance in multi-objective settings. While most traditional dimension reduction methods are designed for static datasets, our approach is tailored for online learning and preserves Pareto-optimality after transformation. We propose a new training and evaluation framework for reward dimension reduction in multi-objective reinforcement learning and demonstrate the superiority of our method in environments including one with sixteen objectives, significantly outperforming existing online dimension reduction methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a reward dimension reduction technique to improve the scalability of multi-objective RL (MORL). Specifically, it adopts an affine transformation and theoretically establishes conditions to guarantee the Pareto-optimality of learned policies in the original reward space and to build a valid mapping between the reduced and original preference spaces. Additionally, a reconstruction neural network helps preserve the information of the original rewards. The paper evaluates the proposed method through experiments with sixteen objectives, demonstrating superior performance compared to existing reduction and non-reduction methods.

### Strengths
- The paper is well-motivated. The scalability of MORL is crucial for real-world applications but is rarely studied. This work thoroughly considers the nature of multi-objective settings and develops a simple yet effective dimension reduction solution.
- The paper is well-written and well-organized, with clear theoretical explanations and implementation details that make the methodology easy to understand.
- Empirical evaluations and ablation studies are convincing, demonstrating the effectiveness of the proposed approach.

### Weaknesses
 - The number of test preferences $N_e $, seems slightly insufficient, even for a 4-dimensional reduced reward space. I’m a bit concerned about whether this is enough to represent the performance across the whole Pareto front in the original 16-dim reward space.
- I wonder if it would be helpful to evaluate the dimension reduction technique on existing MORL benchmarks, even those with fewer objectives. Doing so could help assess the influence of the reduction method on performance and visualize the Pareto front in both the reduced and original reward spaces, helping us understand the relationship of Pareto in two reward spaces. 
- In certain cases, learned policies may cover a broad Pareto front in the reduced reward space but occupy only a narrow area in the original reward space and lead to low sparsity. How could this situation be avoided or detected during evaluation? Without visualizing the high-dimensional Pareto front, I am curious whether metrics like hypervolume and sparsity are sufficient to detect such issues.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a novel method for reward dimensionality reduction as well as a new evaluation protocol & benchmark for high dimensional multi objective reinforcement learning. The developed approach reduces the dimensionality of the rewards with an affine transformation that is additionally constrained to be row stochastic & feature only positive elements in its matrix. The authors show in an empirical evaluation that their approach beats relevant baselines in a high-dimensional multi-objective environment.

### Strengths
To the best of my knowledge, the approach is novel. It is furthermore simple & elegant and leads to demonstrated improvements over baselines on a high-dimensional multi-objective environment. In addition, the paper proposes a new evaluation setup for their work. Finally, it is well written & understandable also for readers outside of the multi-objective sphere.

### Weaknesses
The empirical evaluation is limited to a single environment. This is partially due to the fact that the authors address a problem that has so far been only explored to a limited degree before, however it still means the demonstrated superiority of the approach has to be taken with a grain of salt. Also, the evaluation doesn't feature uncertainty estimates. I would be glad to improve my score if those two points are addressed.

### Questions
I am not quite sure whether due to the affine nature of your approach, the resulting transformation function will deterministically always be the same given the same data (?), but I presume that the online data collection as well as the base RL algorithm used will introduce some stochasticity into the results, so could you please add corresponding uncertainty estimates in your tables (it seems you should have the data already anyways since you mention 8 random seeds)?

I think the following paper could enrich your related work section, would you care to review and potentially add it?
Weber, M., Swazinna, P., Hein, D., Udluft, S., & Sterzing, V. Learning Control Policies for Variable Objectives from Offline Data. In 2023 IEEE Symposium Series on Computational Intelligence (SSCI) (pp. 1674-1681). IEEE.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a reward reduction approach for multi-objective reinforcement learning (MORL) that transforms a high-dimensional reward vector into a lower-dimensional one. Unlike previous methods that primarily rely on static datasets, this approach supports online learning while ensuring that Pareto optimality is preserved after the transformation. Additionally, the authors introduce a comprehensive training and evaluation framework for reward dimension reduction in MORL.

### Strengths
1. This paper focuses on the important problem of multi-objective reinforcement learning in the presence of high-dimensional rewards.

### Weaknesses
1. This paper proposes applying an affine transformation to reduce the original high-dimensional reward vector to a lower-dimensional representation. However, the authors do not provide a theoretical justification demonstrating why reducing the reward dimension would improve multi-objective training, particularly when compression may result in information loss.
2. One major limitation is the experimental scope. The experiments are conducted solely on a traffic light control environment, without exploring the impact of varying the dimensionality mmm, which undermines the generalizability and robustness of the results.

### Questions
1. In Tables 1 and 2, it seems the scale of the reported metrics is really large. Could the author illustrate more about metrics?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work studies multi objective RL (MORL), considering the Pareto frontier and measures hypervolume and sparsity of solutions to judge viability in downstream tasks. They propose a new dimensionality reduction technique to tackle existing challenges in high-dimensional problems. This can help to collapse similar objectives to reduce the effective reward space. The authors give some theoretical and empirical demonstration validating their method.

### Strengths
- Simplicity of idea and execution
- Providing well-founded theory to motivate their method, and proof given is easy to follow
- Modular (could be applied with other MORL methods)
- Provides potential new SOTA for the sample experiment
- nice explanation of MORL problem for non-experts
- I was hoping to see an ablation on dropout as soon as it was mentioned, and it was indeed given (Maybe mention Table 3 in L363)

### Weaknesses
Overall, I can't quite tell if I should think of this as a theory or experiment paper. For the former, I believe the theory given is not strong enough. But for the latter, there is only one environment, so I think it is not fair to claim total SOTA performance without a more systematic set of experiments. Below I'll give some points of weakness mixed in with related questions.

- Somewhat unclear empirics (the authors only provide scalar statistics on a single environment)
- Theory is somewhat weak. Specifically, they provide a sufficient, but not necessary condition. However, the surrounding text (Line 320) makes it sound like a necessary condition "we require...". Just be careful to not over-sell the result.
- I'm unsure how limiting the linearity in Theorem 1 is. Although it is beneficial for its simplicity from a computational perspective, is something being lost here? It seems to only capture linear relationships among various objectives. Can a counterexample be provided to better understand the breakdown of the (<=) other direction of the theorem?
- Some pre-assumed knowledge: As mentioned in L412, the final rank=4 was assumed to be known. But this would come at the end of training. How big an impact is there in different choices of rank? Can the rank be changed adaptively?
- L449: It's a bit unclear to me if NPCA was tuned appropriately for a fair comparison. Can better choices of the regularization strength be chosen? (Also, where's the reference to NPCA, I think I missed it)

I'm not totally aware of the MORL literature, but are there any other baselines with which to compare?

### Questions
Beyond those in the previous section, here are a few more questions for the authors. If the authors are able to sufficiently abate my concerns, I can raise the score.

- In your theorem, do you think it would be possible to generalize to PSD matrices? I'm not seeing the hurdle, but it would be enlightening (for me at least (:  )  to discuss either way
- Can you discuss any potential use of work like [3] to reduce reward space by canonicalizing objectives (ensuring they truly are distinct)? Would that be applicable here?
- RE Table 4, Can you also give an ablation of "-positivity"? (with the rowst constraint)
- L500 is unclear. Why does finite ep length introduce more overhead?
- Relatedly, what is the complexity of the constrained optimization problem?
- Table 1: why did you choose this reference point? Maybe you can normalize the values wrt ${10^{4*16}}=10^64$ then?
- Can you provide the learning curves or more dynamic information about your algorithm? How about other statistics (cf https://github.com/google-research/rliable)
- L325, A brief discussion on the connection to [1] would be interesting, if possible
- How does this work (or MORL more generally) relate to the successor features framework, e.g. [2]?

minor:
- Fig 2, can you change to e.g. $|AB|^2$ if that is meant. Also the quality of figures is a bit low, maybe just increase DPI a bit
- "works" -> "work"

[1]: https://proceedings.neurips.cc/paper_files/paper/2022/file/f600d1a3f6a63f782680031f3ce241a7-Paper-Conference.pdf
[2]: https://arxiv.org/abs/1606.05312
[3]: http://aima.cs.berkeley.edu/~russell/papers/iclr21-epic.pdf


I'm genuinely curious to understand the effect of dropout. I think the explanation starting at L475 is a bit confusing (for me). Can you offer any additional explanations/re-wordings?

### Soundness
3

### Presentation
3

### Contribution
2
