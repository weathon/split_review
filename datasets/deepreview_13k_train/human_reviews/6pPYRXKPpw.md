# Towards Diverse Behaviors: A Benchmark for Imitation Learning with Human Demonstrations

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Imitation learning with human data has demonstrated remarkable success in teaching robots in a wide range of skills. However, the inherent diversity in human behavior leads to the emergence of multi-modal data distributions, thereby presenting a formidable challenge for existing imitation learning algorithms. Quantifying a model's capacity to capture and replicate this diversity effectively is still an open problem. In this work, we introduce simulation benchmark environments and the corresponding \textit{Datasets with Diverse human Demonstrations for Imitation Learning (D3IL)}, designed explicitly to evaluate a model's ability to learn multi-modal behavior. Our environments are designed to involve multiple sub-tasks that need to be solved, consider manipulation of multiple objects which increases the diversity of the behavior and can only be solved by policies that rely on closed loop sensory feedback. Other available datasets are missing at least one of these challenging properties.
To address the challenge of diversity quantification, we introduce tractable metrics that provide valuable insights into a model's ability to acquire and reproduce diverse behaviors. These metrics offer a practical means to assess the robustness and versatility of imitation learning algorithms. Furthermore, we conduct a thorough evaluation of state-of-the-art methods on the proposed task suite. This evaluation serves as a benchmark for assessing their capability to learn diverse behaviors. Our findings shed light on the effectiveness of these methods in tackling the intricate problem of capturing and generalizing multi-modal human behaviors, offering a valuable reference for the design of future imitation learning algorithms. 
Project page: \href{https://alrhub.io/d3il-website/}{https://alrhub.io/d3il-website/}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
As the interest in learning behaviors from natural human data raises, importance of imitation learning algorithms that can successfully learn from diverse and potentially multi-modal human behavior raises similarly. However, such algorithms are only recently gaining traction, and such there does not exist many benchmarks for properly comparing them. This situation is what D3IL aims to resolve, by creating a new benchmark to evaluate and compare imitation learning algorithms capable of learning multi-modal behavior.

The paper is divided the following sections: first the authors introduce the diversity metric used to evaluate the algorithms, which is an important component since the diverse, multi-modal behavior require a good notion of "coverage" of the behaviors. Then, they introduce the environments, baseline algorithms, and follow up by showing the performance of the algorithms and architectures on the tasks, both on terms of success rate and behavior diversity. Finally, they run a host of ablation experiments, such as limited data and impact of historical information.

### Strengths
This paper is a timely work since learning from diverse human data has shown major success in other fields such as natural language processing, and evaluation of candidate algorithm that can learn from diverse datasets is of vital importance at this moment. Here are the things this paper did well:

1. The benchmark is quite principled, and both the success metric and the diversity metric are well justified while being intuitive and implementable.
2. The list of baseline algorithms is also quite comprehensive, and covers the list of recent important developments in the space.
3. The set of ablation experiments run covers the primary points of interest, such as dataset size, visual/state based models, and impact of history.

Overall, this is a paper with a straightforward mission that achieves its goals well.

### Weaknesses
The paper, while quite strong on the execution, has some major shortcomings that can be improved in the future.
- A benchmark paper is useless without the environment codes and the data, which is absent from the supplementary materials. This is a major negative for this paper because we are being asked to judge it without being able to understand how easy it may be to run new algorithms against this benchmark.
- Another primary criticism is that all five environments are very simple tabletop environments, and thus the complexity of the algorithm needed to solve that may not be quite high. A better benchmark would involve multiple kinds of environments, involving 2D/3D environments, potentially with different intractable elements.
- One critical component missing from the evaluation is the required forward pass time or control frequency of the algorithms, which to my understanding is one of the largest disadvantages of diffusion-based models.

### Questions
What is the action space used by the environments? In the diffusion policy paper they show that diffusion policies are better for some absolute action spaces while being worse for others relative action spaces. Clarification as to that would be great.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a benchmarking for imitation learning from human demonstrations. Compared to other released benchmark datasets, the authors place emphasis on using human demonstrations and those demonstrations covering diverse behaviors.  The argument for doing so is because human demonstratinos inherently have some noise if the teleoperator differs, if people have different levels of expertise, etc. The goal is also to propose a quantitative measure of diverse behavior.

The proposal for this is to assume there exists a space $\mathcal{B}$ of discrete behavior descriptions $\beta \in \mathcal{B}$ (i.e. for pushing, whether we are pushing red to red or red to green and in what order). Our demonstrations define a $p(\beta)$ distribution of how often different behaviors appear. A learned policy $\pi$ will induces its own $\pi(\beta)$ distribution of behaviors, and similarity is measured by $KL(\pi(\beta) || p(\beta))$. This is simplified to a uniform distribution for $p(\beta)$ in all experiments, with entropy scaled to lie in range $[0,1]$. This reduces to $H(\pi) = - \sum \pi(\beta) \log_{|B|}\pi(\beta)$

Diversity is further defined as achieving many behaviors from the same initial state $s_0$, giving the conditional behavior entropy of

$$
H(\pi(\beta|s_0)) \approx -\frac{1}{S_0} \sum_{s_0} \sum_{\beta} \pi(\beta|s_0) \log_{|B|} \pi(\beta|s_0)
$$

Since the $p(s_0)$ distribution is unknown, this is approximated by Monte Carlo estimates using $S_0$ samples of the initial state.

The proposed benchmark is implemented in MuJoCo using a Panda robot and mostly consists of block moving tasks. A variety of imitation learning methods are tried, varying from pure MLPs to history-aware methods and diffusion policies. Experiments are also conduted on history length and on size of dataset.

### Strengths
The authors run an extensive series of benchmark methods over their proposed environments. The environments are described in sufficient detail to reproduce them. The evaluation protocol and model selection criteria is documented well, a rarity in robot learning papers. The paper is also written quite clearly.

### Weaknesses
The fact that different behaviors must be enumerated ahead of time is a large limitation of the proposed behavior-level entropy measure. This enumeration requires a priori knowledge of the task's possible outcomes, which may not always be available or easily defined, especially in complex environments. The reliance on a discrete behavior space also limits the applicability to tasks with continuous or highly variable behaviors. I also found the KL-divergence to be a bit unmotivated. This paper assumes the demonstration dataset is always uniformly distributed among all behaviors, but in cases where the demonstration dataset is not uniformly distributed, it's not clear to me if KL divergence is the right measure to use. (We would expect a good learning method to have low KL, but if the demo dataset is skewed, we may still prefer a policy that is uniform across behaviors, even if this has higher KL than identicall matching the skewed distribution.) It seems like the entire discussion about KL is pointless and it would be more straightforward to just use the behavior entropy definition.

Setting aside this for the moment, the paper also does not ever make a claim that multimodal policies would be good. Success rate need not be correlated with high behavior entropy - as argued by the experiment results, deterministic policies can still achieve okay success rate without diverse behavior. And hypothetically, you could have a 100% success rate policy that only follows a singular behavior $\beta$. Such a policy may even be preferred (i.e. in factory automation, repeatable behavior given initial conditions is desired.)

Arguably, the paper is just about measuring this quantity, rather than arguing why it matters, but I would have appreciated some argument on this front.

### Questions
Overall I feel the paper is okay, despite the flaws it does make some strides towards focusing on diversity of behavior. But could the authors comment on where conditional imitation learning falls into the picture. In the pushing task for example, if the 4 behaviors are known ahead of time, you could imagine conditioning the policy on a 1-hot with 4 values for "push X1 to Y1, push X2 to Y2", and that would allow a deterministic policy to achieve any of the behaviors assuming a perfect learning method. What is the argument for why we cannot or should not do something where we provide additional context to the policy on how we want the task to be performed?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new benchmark for imitation learning with a focus on evaluating diverse behaviors. The authors perform an extensive comparison of different imitation learning algorithms, ranging from deterministic to stochastic algorithms using MLPs and transformers along with interesting insights about state-based and image-based policies and other algorithmic aspects.

### Strengths
- The paper introduces a new benchmark for imitation learning along with appropriate metrics to quantitatively evaluate diverse behaviors.
- The paper performs ablation studies and provides good insights about state-based vs image-based policies, the impact of history and action prediction horizon, and learning with less data.
- The paper provides some results that are consistent across methods - (1) transformers improve performance over using MLPs, (2) historical inputs enhance the performance of transformer-based policies, and (3) transformers exhibit superior performance in the low data regime.
- The paper has tasks of varying difficulty with a task like stacking-3 which is not satisfactorily solved by any of the existing algorithms. This provides a scope for improvement.

### Weaknesses
 - Based on the results, it seems like all tasks can be solved by existing methods except one. Though this gives some scope for improvement on the algorithmic side, I believe just a single variant of a task remaining unsolved might not be a very useful for future works considering this benchmark for evaluations. It would be great if the authors could include other tasks or provide functionalities for adding new tasks.
- It would be great if the authors could provide code since a benchmark is only useful if the code is available.

### Questions
It would be great if the author’s could address the points mentioned in “Weaknesses”.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
