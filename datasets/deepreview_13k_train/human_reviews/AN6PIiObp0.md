# SALSA: Soup-based Alignment Learning for Stronger Adaptation in RLHF

- Decision: Reject
- Scores: 5, 5, 5, 6, 3, 5

## Abstract
\looseness=-1 In Large Language Model (LLM) development, Reinforcement Learning from Human Feedback (RLHF) is crucial for aligning models with human values and preferences. RLHF traditionally relies on the Kullback-Leibler (KL) divergence between the current policy and a frozen initial policy as a reference, which is added as a penalty in policy optimization algorithms like Proximal Policy Optimization (PPO). While this constraint prevents models from deviating too far from the initial checkpoint, it limits exploration of the reward landscape, reducing the model's ability to discover higher-quality solutions. As a result, policy optimization is often trapped in a narrow region of the parameter space, leading to suboptimal alignment and performance. This paper presents \textbf{\methodname}\space (\textbf{S}oup-based \textbf{A}lignment \textbf{L}earning for \textbf{S}tronger \textbf{A}daptation), a novel approach designed to overcome these limitations by creating a more flexible and better located reference model through weight-space averaging of two independent supervised fine-tuned (SFT) models. This model soup allows for larger deviation in KL divergence and exploring a promising region of the solution space without sacrificing stability. By leveraging this more robust reference model, \methodname\space fosters better exploration, achieving higher rewards and improving model robustness, out-of-distribution generalization, and performance.
We validate the effectiveness of \methodname\ through extensive experiments on popular open models (Llama2-7B, Mistral-7B, and Gemma-2B) across various benchmarks (MT-Bench, Arena-Hard, UltraFeedback), where it consistently surpasses PPO by fostering deeper exploration and achieving superior alignment in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper studies RLHF and proposes SALSA, which leverages a "model soup" approach, averaging weights from two supervised fine-tuned (SFT) models to create a more flexible reference model. They claim that this allows broader exploration of the solution space without sacrificing stability. In the experiments, the authors use models like Llama2-7B, Mistral-7B, and Gemma-2B, along with benchmarks (MT-Bench, Arena-Hard, UltraFeedback, demonstrating that SALSA consistently outperformsPPO by achieving higher rewards and win rates.

### Strengths
The idea of this paper is clear and straightforward. The experiment results also seem promising.

### Weaknesses
The authors didn't provide sufficient explanations about the occurred phenomenon (see the Questions part), which makes their method not convincing enough. It would be great if the authors can provide some theoretical analysis, even for a simple case study. Specifically, the claim that the midpoint model consistently performs the best is not well-justified. The authors should explore why averaging the weights of two randomly trained SFT models would lead to a superior reference model, and why the midpoint consistently yields the best results. The lack of theoretical grounding for this observation makes the method less robust and harder to generalize. Furthermore, the relationship between the KL divergence coefficient, $\beta$, and the interpolation parameter, $\alpha$, is not sufficiently explained. The observation that the optimal $\beta$ changes drastically with $\alpha$ requires more in-depth analysis. The authors should provide a more detailed explanation of why the KL divergence term seems unnecessary when using the midpoint model, and why the trained model does not produce gibberish responses in this case. The current explanation is insufficient, and a more rigorous justification is needed.

### Questions
1. Why does the mixed model work the best at the midpoint? It seems that both SFT models are trained randomly, and it seems strange that always the midpoint of them performs the best.

2. For the KL hack phenomenon, is it useful to fix the length of the generated response of the model?

3. The value of the optimal $\beta$ also changes drastically with $\alpha$. When $\alpha = 0.2$ the optimal $\beta$ is 0.2. However, when $\alpha=0.01$, the optimal $\beta$ decreases to $0.01$ quickly. It is also strange that when you take the midpoint model, the KL divergence term seems unnecessary and the trained model won't produce gibberish responses. Could the authors explain more about this phenomenon?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers using the technology of model soup by weighted averaging two reference models which is fine-tuned on the same pre-trained model to improve the reference model in RLHF. It demonstrates that using model soup to improve the reference model will lead to better aligned model by PPO algorithm.

### Strengths
1. The experiment is well done. It demonstrates the advantage of model soup for reference model in RLHF from different aspects. It explores the different weighting ratio when averaging two or three models. When the ratio is averaged, the aligned model by PPO algorithm has better performance.

### Weaknesses
1. If the weighted averaged model has better performance than initial model, it is obvious that the aligned model by the PPO algorithm has better performance than others.

2. It is well known that the neural network is non-convex, which means that applying weighted averaging on several models could lead to a poor performance. Is there always good performance when applying model soup for the reference model? Or how do we avoid this when merging models?

### Questions
1. It is well known that the neural network is non-convex, which means that applying weighted averaging on several models could lead to a poor performance. Is there always good performance when applying model soup for the reference model? Or how do we avoid this when merging models?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a simple modification to the KL-constrained objective used in RL finetuning. Instead of regularizing to the same fixed policy $\pi_{ref}$, the authors propose to regularize to a souped policy $\pi_{soups}$ which is the model soups of multiple $\pi_{ref}$ (each SFT-ed on the same dataset with different seed or hyper-parameters). The authors claim this is a more robust ref model, and demonstrate results on instruction following benchmarks (MT-Bench, Arena-Hard, UltraFeedback) where the proposed approach improves over the classic $\pi_{ref}$ regularization.

### Strengths
1. The paper illustrates a simple phenomenon, that applying model soups to the anchor policy for KL regularization can lead to improved win-rates in many benchmarks.
2. The paper includes some ablations, including on how the policies are souped (finding that uniform souping is best). Also, the authors show that multiple KL terms to each individual policy does not lead to any benefits, whereas a single KL term to a souped policy does.

### Weaknesses
1. I think some claims made in the paper are not rigorously justified. For example, Figure 2 shows that reward increases with model souping, but it is also important to plot the KL wrt a fixed anchor policy (whether pi_ref or pi_soups or both). In other words, it may be possible to get a higher reward by simply having higher KL and this is not ruled out in the experiments.
2. Related to (1), simply showing higher win-rates in Table 1, without plotting the KL as well, is also not very convincing, since these benchmarks are easy to game. It would be much more convincing if SALSA leads to higher rewards/win-rate while maintaining the same or lower KL compared to pi_ref.
3. The paper does not discuss any important related works that apply model soups to RLHF, for example:
[1] "WARP: On the Benefits of Weight Averaged Rewarded Policies", https://arxiv.org/abs/2406.16768
[2] "WARM: On the Benefits of Weight Averaged Reward Models", https://arxiv.org/abs/2401.12187
[3] "Conditional Language Policy: A general framework for steerable multi-objective finetuning", https://arxiv.org/abs/2407.15762

### Questions
1. Could the authors plot results showing also KL wrt fixed anchor policy? (as mentioned in Weaknesses)
2. In the abstract and several places in the paper, the author claimed that model soups lead to "improving model robustness, out-of-distribution generalization". How are model robustness and OOD generalization entailed by the experiments?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose an alternative to RLHF which instantiates two models and then takes the average of them at each training step, replacing the KL divergence term in the classical RLHF setup.

### Strengths
- interesting and nice train of work! 
- I appreciate the novel look at RLHF.

### Weaknesses
 - PPO at this point has fallen out of favor as a canonical RLHF architecture (see the Back to Basics paper by Cohere AI). Furthermore, PPO operates using a trust region policy, so it bounds the steps that a learning update could anyway. In order for me to recommend your paper for publication, I'd want to see you repeat this experiment with REINFORCE, Actor-Critic, and perhaps another RL algorithm that makes up the backbone of your RLHF pipeline.

### Questions
- Is your model soup similar to a model ensemble? I’m curious as to why there is the separate terminology.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces SALSA (Soup-based Alignment Learning for Stronger Adaptation), a novel method in the field of large language models, aimed at enhancing model alignment through Reinforcement Learning from Human Feedback (RLHF). Unlike traditional methods that rely on a fixed initial policy as a reference, SALSA employs a model soup created by weight-space averaging of two independently fine-tuned models. This approach allows for greater flexibility and exploration during policy optimization, resulting in improved model performance and robustness.

### Strengths
The SALSA method introduces the novel concept of model soup to address alignment issues in large language models. By employing weight-space averaging of two independently fine-tuned models, this innovation overcomes the limitations of KL divergence constraints in traditional RLHF methods, opening new research directions.
The paper is well-structured and logically coherent, offering detailed and easily understandable descriptions of the SALSA method. By contrasting traditional methods with SALSA, the authors effectively convey the core ideas and advantages of the method, enabling readers to clearly grasp its contributions.

### Weaknesses
1 Limited Dataset Generality: The experiments primarily use the UltraChat-200k and UltraFeedback datasets, which may not be comprehensive enough to reflect the model's performance across different domains or applications. As a result, the findings might not be generalizable to broader real-world scenarios.

2 Lack of Training Curve Presentation: The article does not provide training curves, making it difficult for readers to assess the model's convergence and stability during training. Training curves can help understand the learning dynamics and potential issues in the optimization process.

3 Lack of Comparison with Other Related Works: Apart from PPO, the article does not compare the SALSA method with other existing alignment or optimization methods. This limits a comprehensive understanding of SALSA's relative advantages and its competitiveness in a broader context.

### Questions
Here are some questions and suggestions for the authors:

Dataset Generality:Could you provide more details on the choice of datasets? How do you ensure that the results are generalizable across different domains?

Have you considered testing the model on additional datasets to validate its performance more broadly?

Training Curves:Can you include training curves in your supplementary materials? These would help in understanding the convergence behavior and stability of your model.What insights can you provide about the model's learning dynamics during training?

Comparison with Other Methods:Why did you choose to compare only with PPO? Are there specific reasons for not including other related methods in your analysis?Would you consider conducting experiments with other alignment or optimization methods to provide a more comprehensive evaluation?

KL-Hack Issue:Can you elaborate on the KL-Hack phenomenon and potential strategies to mitigate it?Have you explored any preliminary solutions or adjustments to address this issue?

Future Work and Extensions: What are your plans for extending this research? Are there specific areas you believe are promising for further exploration?How do you envision incorporating more than three SFT models into the model soup, considering computational constraints?

These questions aim to clarify certain aspects of your work and suggest areas for potential improvement or further research.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work investigates improving the reference model in RLHF through model merging. The authors propose to use the average parameter of several SFT models that are initialized from the same base model but trained with different seeds as the reference model in the PPO algorithm. Their results demonstrate that by using a "soup" model as the reference model, PPO obtains a significant performance improvement in three dialogue benchmarks.

### Strengths
1. The proposed technique is clear and effective according to the experiment results.
2. The proposed technique is evaluated with different base models.
3. The authors provide sufficient analysis of the impact of model merging in the final reward, which well motivates the proposed technique.

### Weaknesses
1. As important algorithms in RLHF, reward-free methods such as DPO are not discussed in this paper.
2. The proposed technique is not fully explored in the context of RLHF. For example, the soup model can also serve to be the reference model in reward-free RLHF methods like DPO.
3. The paper lacks a discussion on how the proposed method compares to other RLHF algorithms, specifically DPO, which has shown promise in similar tasks. A more thorough comparison would strengthen the claims of the paper.
4. The paper does not explore the impact of using the soup model for initialization of the RL process, which could potentially influence the final results. The current implementation only uses the soup model for KL divergence calculation, but the impact of using it for initialization should be investigated.
5. Line-321: "high KL coefficients cannot be applied when using SALSA because the response length tends to converge to zero. Specifically, if the response length y for a given prompt x is zero, the KL divergence between the trained policy and the frozen policy also becomes zero." This statement is incorrect since when the response length y is zero, the EOS token would contribute a non-zero value for KL divergence and thus the KL divergence between the trained policy and the frozen policy would not be zero.

### Questions
1. How does the SALSA perform when compared to DPO?
2. Can using the soup model as a reference model also bring benefit to DPO?
3. In the implementation of SALSA, how is the model initialized at the beginning of the RLHF process? If the soup model is used for initialization, a further analysis about the impact of using soup model as the RL initialization model would be expected.
4. Line-321: "high KL coefficients cannot be applied when using SALSA because the response length tends to converge to zero. Specifically, if the response length y for a given prompt x is zero, the KL divergence between the trained policy and the frozen policy also becomes zero." This statement is incorrect since when the response length y is zero, the EOS token would contribute a non-zero value for KL divergence and thus the KL divergence between the trained policy and the frozen policy would not be zero.

### Soundness
3

### Presentation
3

### Contribution
2
