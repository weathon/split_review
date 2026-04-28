# Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 5, 8

## Abstract
Recent advancements in robot learning have used imitation learning with large models and extensive demonstrations to develop effective policies. However, these models are often limited by the quantity quality, and diversity of demonstrations. This paper explores improving offline-trained imitation learning models through online interactions with the environment. We introduce Policy Decorator, which uses a model-agnostic residual policy to refine large imitation learning models during online interactions. By implementing controlled exploration strategies, Policy Decorator enables stable, sample-efficient online learning. Our evaluation spans eight tasks across two benchmarks—ManiSkill and Adroit—and involves two state-of-the-art imitation learning models (Behavior Transformer and Diffusion Policy). The results show Policy Decorator effectively improves the offline-trained policies and preserves the smooth motion of imitation learning models, avoiding the erratic behaviors of pure RL policies. See our [project page](https://sites.google.com/view/policy-decorator/home) for videos.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper considers the setting of robot learning from demonstration with large policy models. The performance of existing supervised learning-based (i.e. behavioral cloning) approaches with large policy models is dependent on the quantity, quality, and diversity of the demonstrations, which in the robot setting are often resource-intensive to collect. To address these limitations, the paper considers fine-tuning the large policy models with reinforcement learning (with sparse rewards), and the paper identifies two major challenges: 1) non-differentiable components of the large policy models, and 2) performing many gradient updates on the policy model’s large number of parameters - as typically required during sparse-RL training - would be computationally expensive. The paper proposes learning a residual policy that can correct the behavior of the base policy. The paper proposes a method for controlling the exploration of the residual policy by progressively adding the residual policy’s output to that of the base policy throughout training. The paper conducts experiments on ManiSkill and AdroitHand tasks.

### Strengths
The paper presents a simple algorithm for fine-tuning large policy models in robot learning. The paper does a thorough job of validating baselines with ablation studies, providing justification for the design choices. The thorough empirical results - including the proposed method (Policy Decorator) showing improvement over the baselines across a number of tasks - is what establishes the quality of the paper and its contribution. In terms of clarity, the assumptions are clearly stated and the paper is written clearly.

### Weaknesses
One of the primary reasons to use large policy models in robot learning is they can model multimodal behavior, which a Gaussian policies parameterized by small neural networks cannot. In the paper, it remains unjustified whether adding the Gaussian residual policy to the base policy still retains the multimodal capabilities of the large policy model. (The answer may seem intuitive, but is worth justifying, as this is one of the principal motivations for using large policy models.)

The paper identifies fine-tuning large base policy models with RL as “prohibitively costly” due to the many gradient updates required and the large number of parameters. By using the large base policy (most of which are trained offline through a BC approach), this will dramatically improve the sample efficiency of RL. But, the point still stands that the large number of parameters may make gradient updates costly. However, no wall-clock times are reported, though they are mentioned when discussing the RLPD baseline (Appendix B.5) and Cal-QL baseline (Appendix F.3). Including wall-clock times for the proposed method and the baselines could help inform how much more costly gradient updates on large policy models are (required by the baselines) than inference (required by both baselines and Policy Decorator), and whether the proposed method truly mitigates this cost.

The paper does not compare to standard, non-large policy model baselines, such as GAIL with an MLP or CNN policy. The paper specifically focuses on large policy models. However, it still remains an important baseline to observe whether large policy models are even necessary on these tasks, or if a simpler policy could achieve comparable performance with less computational overhead.

The paper’s Policy Decorator approach, by controlling exploration through the Progressive Exploration Schedule, effectively allows the residual policy’s critic to be warm started before the residual policy has a noticeable effect on the behavior policy. It is therefore crucial to investigate whether warm starting the critic on the baselines improves their performance. The paper  addresses this in Appendix F. However, in Section F.5.2, the paper discusses warm starting in Q function training, noting that warm starting the critic causes a blowup in the entropy coefficient. Is it possible to fix the entropy coefficient during critic pretraining, but then unfreeze it during fine-tuning? This could potentially stabilize the warm-starting approach for the baselines.

Some of the tasks in this paper have a dense reward that are easy to specify. This fact should be noted, as it would significant affect RL training by ameliorating the exploration problem. The paper is justified in wishing to consider the sparse-reward setting. For full clarity, however, the paper should identify which tasks may have access to an easily-specified dense reward.

**Minor Comments:**
- Define “diversity” of demonstration data (Line 038), as it is not discussed in the rest of the paper. (This can connect to the multimodal behavior discussed above.)
- There is a comma missing on Line 013, between “quantity” and “quality.”
- The number of seeds is not listed for Figure 7. (I presumed it followed the same as Figure 6.)
- In Figure 4’s caption, “schedule” is spelled wrong.

### Questions
See Weakness section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers how to use a model-agnostic residual policy to augment imitation learning policy in an offline-to-online transfer setting. The approach is very simple: freeze the base policy, and learn only a small residual policy that outputs a residual action which can be added to the base action. Online RL updates is only applied to the small residual policy. This approach has been shown to be highly effective across a variety of policies (like autoregressive Transformer and diffusion policies), and a variety of online RL algorithms (like SAC and variants of PPO).

### Strengths
- The approach is simple to implement, and the presentation is clear. The paper is easy to understand.
- The experimental evaluation is thorough.
- The performance seems very strong.

### Weaknesses
In my view, the most important weakness of this paper is this: The proposed approach is way too similar to the old idea of "Residual Policy Learning" [1, 2]. In fact, I would argue that **it is essentially the same as the old residual policy learning**. In the past, residual policy learning used a fixed controller. In this paper, residual policy learning uses a frozen pretrained policy.

As such, I don't think it is appropriate for the paper to rebrand this approach as "Policy Decorator", since it is basically the same as residual policy learning.

It appears that the essential finding can be summarized as: residual policy learning is more effective than finetuning for offline-to-online RL. I think saying that this finding is a new framework is confusing and misleading.

### Questions
See the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents Policy Decorator, a novel method that can fine-tune large, offline-trained imitation policies using Reinforcement Learning. Notably, the fine-tuning happens using a small network as a residual action generation policy on top of the pre-trained imitation learning policy. Policy Decorator works independently of the underlying imitation learned policy and simply wraps it in the fine-tuning loop.

### Strengths
This paper addresses an important research question and might lead to major enhancements in the research field. Current big models perform favorably but need costly demonstration data to work on novel but related tasks.   
The well-written paper motivates the proposed method and clearly indicates the contributions. 
Importantly, the method is simple but seems to be effective.

### Weaknesses
I don't have major concerns regarding the paper, but I believe the paper lacks a couple of related works that need to be discussed in my opinion:

- Jia et al. Towards diverse behaviors:  A benchmark for imitation learning with human demonstrations (ICLR 2024) 
- Information maximizing curriculum: A curriculum-based approach for learning versatile skills (NeurIPS 2023) 
- Goal-conditioned imitation learning using score-based diffusion policies (RSS 2023)  

- Multi-modality might need more discussion (see Questions)

### Questions
I have some concerns regarding the effect of the residual policy on possible multi-modalities in the base distribution. The proposed base policies can represent multi-modal distributions (a mode does not refer to different input modalities in this case, but rather different modes in the underlying distribution given a state), making them a powerful method given that human data tends to be multi-modal. However, to my understanding, the residual policy is a Gaussian policy such that a mode collapse will happen once the fine-tuning starts. Does this mean that the overall fine-tuned policy is indeed maximizing performance, but therefore ignores other modes in the behavior? 

This question could probably be answered by benchmarking on one of the proposed environments and data sets in the work by Jia et al. (see Weaknesses) that exactly analyzes the capabilities of learning multiple modes of imitation learning methods by providing task-specific diversity metrics. 
Alternatively, plotting the policy for a multi-modal state (most often multi-modality occurs in the initial state) for the pre-trained and fine-tuned policy might provide some insights.

### Soundness
3

### Presentation
3

### Contribution
3
