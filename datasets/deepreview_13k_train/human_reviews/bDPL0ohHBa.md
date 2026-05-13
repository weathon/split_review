# One Model for All: Multi-Objective Controllable Language Models

- Decision: Reject
- Scores: 6, 5, 6, 6, 5

## Abstract
Aligning large language models (LLMs) with human preference is critical to enhancing LLMs' safety, helpfulness, helpfulness, humor, faithfulness, etc. The current reinforcement learning from human feedback (RLHF) mainly focuses on a fixed reward learned from average human ratings, which may weaken the adaptivity and controllability of varying preferences. However, creating personalized LLMs requires aligning LLMs with individual human preferences, which is non-trivial due to the scarce data per user and the diversity of user preferences on multi-objective trade-offs, such as prioritizing humor and empathy in one context, while seeking efficiency and precision in another. Can we train one LLM to produce personalized outputs for different user preferences on the Pareto front? In this paper, we introduce Multi-Objective Control (MOC), which trains an LLM as a meta-policy to directly generate responses in the preference-defined regions of Pareto front. Our approach integrates multi-objective optimization (MOO) principles into Proximal Policy Optimization (PPO) to train an LLM as a preference-conditioned policy network. We improve the computational efficiency of MOC by applying MOO at the policy level, which enables us to finetune an LLM of 7B parameters on a single A6000 GPU. Extensive experiments demonstrate the advantages of MOC over baselines in three aspects: (i) Controllability of LLM outputs w.r.t. user preferences on the trade-off among multiple rewards; (ii) Quality and diversity of LLM outputs, measured by the hyper-volume of multiple solutions achieved; and (iii) Generalization to unseen preferences. These results highlight MOC’s potential for real-world applications requiring scalable and customizable LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In contrast with aligning LLMs to general human preferences, this paper focused on training the LLMs is such a way that they are controllable and can output responses according to the specified preferences. Current methodologies in Reinforcement Learning from Human Feedback (RLHF) often hinge on static reward functions drawn from averaged human ratings. This static nature presents limitations in adapting to or controlling varying individual preferences. To tackle this, the authors propose a novel approach that expands beyond a single preference model to accommodate multiple objectives. Their solution is positioned against the traditional single-objective focus of RLHF, aiming to deliver a more adaptable model capable of directly reflecting individual preferences. 

1. The problem formulation is insightful: framing the controllability problem as a MOO problem with preference being controls.
2. The paper introduces a surrogate objective that circumvents the computationally expensive operations typically required for direct MOO, such as multiple backpropagations.
3. Extensive experiments suggest that the proposed model consistently outperforms baseline RL methods by providing greater flexibility and generalizing across unseen preferences. This underscores the model's utility for real-world applications where preference distributions continually evolve.

### Strengths
1. By focusing on multi-objective control, the model allows for more nuanced alignments with human preferences, catering to a wider array of individual needs compared to single-objective models.

2. The introduction of a surrogate objective, which simplifies the computational demands typically associated with MOO, stands out as a significant advancement. This makes it feasible to implement more complex preference structures without prohibitive cost.

3. The ability of the model to generalize to new, unseen preference distributions highlights its potential for broader application and scalability in dynamic environments.

### Weaknesses
1. No variance is reported for any metric used in the evlaution which is a common thing in RL works.

2. The representation of the preference vector in the prompt is an important aspect of the paper and not explored at all in the paper. Does the preference vector need to be relative in magnitudes aka it just specifies an rank order of the preferences?  If that is the case, are their other representations of the vector possible and how does that impact the model? Can the model understand preference specified as decimals?

3. The method uses MSE loss between the preference vector and the rewards for each preference as reward for their MOO objective. The authors does not discuss any limitations or structure required for this to work. Should the reward and preference be of the same scale. What if the preference is specified as [p_1: 0.25, p_2: 30] and rewards are [r_1: 0.5, r_2: 40]

4. Some baseline approaches will help highlight the importance of the approach.  An interesting baseline can be to add preference vector in the prompt and define reward as MSE(p, r) and apply standard PPO/DPO methods.

### Questions
Please refer to the weakness section.

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
2

### Summary
This paper studies training a single language to fit difference preferences. The paper formulate the problem as a multi-objective optimization problem. The formulated problem is then simplified to another optimization problem with less computational complexity. Experiment results on Helpful assistant show that MOC outperforms baseline methods.

### Strengths
The strengths of this paper are listed as follows

1. This paper studies an important problem, which is to fit a single model to diverse user preferences. 

2. This paper models the problem as a multi-objective optimization problem. To tackle the challenge in the formulated problem, the authors use reward signal as target and also relax the complicated optimization problem to an easier one. These techniques are new to me.

3. The results of experiment looks good. The authors also include multiple dimension to evaluate the performance of MOC and generalization ability, which make the experiment comprehensive with respect to performances.

### Weaknesses
The weaknesses of the paper are listed below

1. The motivation of MOC are not clearly stated. However, this paper does not adequately discuss how previous methods view this problem and what the limitation of the previous approaches are. Therefore, the motivation behind formulating the problem as a MOO problem is not well-explained. Clarifying these shall make readers better understand the rationale of the method.

2. Some parts in method look confusing to me. For example, in equation (1), there seems a ambiguity regarding whether $J^i$ is a scaler or a vector. If it is a scalar, why there is a transpose ($\top$)? Otherwise, whats the definition of taking maximum over a bunch of vectors?Also, the intuition behind constraint in (1) could be better explained. Usually we want reward to be as large as possible, so why we want $R^i(x,y) \approx p_i$ even when $p_i$ is small? 

3. The experiment is restricted to three objective (helpfulness, harmless, humor). However, in real world scenarios, users' demand might encompass much more objectives. Therefore, experiments on a larger number of objectives are required to show the generalization ability of MOC over different numbers of objectives.

### Questions
Can author provide some intuitive explainations on why the value of $c^{(1)},c^{(2)}$ is determined by (8)?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MOC, a mutli-obejct optimization approach to align model's output with user preferences by balancing trade-offs across multiple objectives.

It involves a **preference vector** that represents user objectives, and use a dynamic scalarization technique that balances the objectives.
The authors conduct experiments on the Helpful Assistant dataset, the experimental results further demonstrate its superiority over baseline methods.

### Strengths
MOC offers significant computational efficiency and personalization flexibility, enabling single model to perform diverse preference-based tasks effectively

### Weaknesses
I still have concerns about the limitations in extreme preference scenarios, where trade-offs between objectives might not fully capture nuanced user expectations. Specifically, the method's reliance on a fixed preference vector might struggle to adapt to highly specific or context-dependent preferences that fall outside the pre-defined Pareto front. Additionally, while the computational cost is comparable to single-objective PPO methods, more complex applications might still require higher computational resources. The claim of comparable cost needs further scrutiny, especially when considering the overhead of managing multiple objectives and the potential for increased iterations to converge on a satisfactory trade-off.

### Questions
see weakness

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
3

### Summary
This paper tackles the challenge of aligning large language models (LLMs) with diverse human preferences without the impractical need to train separate models for each preference set. The authors introduce Multi-Objective Control (MOC), an algorithm that enables a single LLM to generate personalized outputs based on different user preferences along the Pareto front of multiple objectives. MOC integrates multi-objective optimization with Proximal Policy Optimization (PPO) which requires only one training phase without human preference data. The method shows that it is controllable, it offers diverse set of high quality solutions and it can handle unseen preferences during training.

### Strengths
1. The experiments include wide range of aspects. The authors evaluate its performance in terms of controllability, generalizability, Pareto front quality, and provide qualitative analyses.
2. Introducing preference vectors alongside multiple reward models allows the single policy model to adapt to different user preferences at inference time. This is an interesting idea in personalizing LLM outputs.
3. The paper effectively constructs the optimization problem, providing theoretical justifications and a clear algorithm.

### Weaknesses
1. The evaluation could be broadened by including more datasets and comparing MOC against additional baselines like Personalized Soups and MetaAligner.
2. The experiments are conducted solely with Llama 2 7B. Testing the approach on other models like Mistral or Gemma, and at different scales such as 13B, would strengthen the claim.
3. The method assumes the availability of N reward models or requires training N reward models, which can be computationally intensive.
4. The effectiveness of MOC isn't clearly illustrated in Figure 2b.

### Questions
1. Did you utilize pre-trained reward models, or did you train the reward models as part of your work? 
2. How did you decide on the number of reward models N and the number of preference vectors M used in your experiments?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an approach for fine-tuning LLMs to adapt to diverse user preferences through a new Multi-Objective Control (MOC) algorithm. Unlike traditional methods, MOC requires only a single training pass and eliminates the need for human preference data. The authors introduce a preference vector that encodes various user preferences, which is then appended to the original prompt to guide the model’s response.

The optimization process involves two main steps: first, solving a min-norm problem (Equation 12) to determine dynamic weights that balance the objectives, followed by optimizing a scalarized objective (Equation 7) based on these weights. The authors highlight that MOC’s computational cost is on par with single-objective Reinforcement Learning with Human Feedback (RLHF), making it an efficient alternative. Experimental results demonstrate MOC's effectiveness across multiple criteria, including solution quality, controllability, diversity, and generalization.

### Strengths
1. Clear Motivation and Writing: The paper is clearly motivated and well-written, effectively framing the relevance of aligning LLMs with diverse user preferences.

2. Important and Practical Problem: The research problem—aligning LLMs to accommodate diverse user preferences—is both interesting and of high practical importance.

3. Efficient Optimization Approach: The authors introduce an upper bound on the original objective (Equation 8) to serve as an optimization surrogate, addressing the intractable nature of multi-objective optimization and enhancing computational efficiency.

### Weaknesses
1. Lack of Clarity in Formulas: The mathematical formulation is unclear, particularly in Equation 5, where the reward model $R^k$ is fixed. The sampled response $y$ does not explicitly show its dependency on the policy parameters $\theta$, making it unclear how to compute the gradient with respect to $\theta$. Specifically, the equation appears to treat $y$ as independent of $\theta$ during the reward calculation, which is inconsistent with the standard policy gradient approach where the sampled action (or response) is a function of the policy parameters.

2. Marginal Improvement: The experimental results show that the Multi-Objective Control (MOC) does not significantly outperform other baselines in terms of solution quality, particularly in the Harmless & Helpful setting (as indicated in Figure 2(b)). The performance is also not clearly superior in the Humor & Helpful setting. The gains appear to be marginal, and it is not clear if the added complexity of the MOC algorithm justifies the limited performance improvements.

3. Limited novelty: The idea is similar to RiC (Yang et al., 2024). The core concept of using a preference vector to guide the model's response is not entirely novel, and the paper needs to better articulate the unique contributions of MOC beyond what is already present in RiC.

4. Weak experimental design: The paper lacks a comparison with the MODPO method, which could provide valuable insights into the proposed method's effectiveness against a strong baseline. The experiments are limited to the Llama2-7B model. Testing the proposed method across a broader range of model sizes and types would strengthen the validity of the findings.

### Questions
1. What do the numerical labels on the markers represent in Fig. 3 of the paper?

2. In Section 4.3, how do we obtain an unseen preference vector? Is it by randomly setting the values of $p_{i}$ in Eq. 3 of the paper?

3. Is there an SFT before PPO for the policy to understand input that contains both prompt and preference vectors?

### Soundness
3

### Presentation
3

### Contribution
2
