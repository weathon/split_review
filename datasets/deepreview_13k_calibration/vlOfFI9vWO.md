# Multi-Agent Reinforcement Learning for Efficient Vision Transformer with Dynamic Token Selection

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 3, 5

## Abstract
Vision Transformers (ViT) have revolutionized the field of computer vision by
leveraging self-attention mechanisms to process images. However, the computational
cost of ViT increases quadratically with the number of tokens. Dynamic token selection methods which aims to reduce computational cost by discard redundant tokens during inference, are primarily based on non-differentiable binary decisions methods and relaxations methods. However, Reinforcement Learning( (RL) based methods, which have astonishing decision-making ability, is considered to have high variance and high bias, not adopted for dynamic token selection task in previous work. Yet, RL-based methods have been successfully applied to many binary decision problems such as neural pruning, routing, path selection. In this paper, we propose Reinforcement Learning for Dynamic Vision Transformer (RL4DViT), a novel framework for the dynamic token selection task in ViT using RL. By harnessing the powerfull decision-making capabilities of Multi-Agent Reinforcement Learning(MARL) algorithms, our method dynamically prunes redundant tokens based on input complexity, significantly
reducing the computational cost while maintaining high accuracy. Extensive experiments
on the ImageNet dataset indicate that our approach reduces the computational cost by
up to 39%, with only a 0.17% decrease in accuracy. To the best of our knowledge,
this is the first RL-based token selection method for efficient ViT.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
2

### Summary
This paper models the token selection acceleration for ViT models as a Multi-Agent Reinforcement Learning problem. Compared with the unaccelerated baseline, the proposed method reduces the computational cost while largely maintaining the performance on the ImageNet classification benchmark.

### Strengths
- This paper models the token selection problem in ViT model as a Multi-Agent RL process. Though I am unfamiliar with this field, I think it is a novel attempt.

### Weaknesses
 - Several issues with spacing and formatting throughout the paper.
- Typos in Figure 1. “specified”, “zeroed-out tokens” and many other typos throughout the manuscript.
- Experiments are only conducted on ImageNet which calls into question the scalability / applicability of the RL4DViT approach on other computer vision tasks and datasets.
- Little motivation provided for the design decisions in formulating the Multi-Agent MDP problem. For example, why is each token an agent in the environment? It is unclear why each token needs to be an independent agent, and what benefit this provides over a single agent predicting a mask.
- Too many unnecessary RL implementation details provided in the methods section. Equation 1 and 2 are simply the actor and critic losses for PPO training and doesn’t feel necessary. The description of the RL algorithm is overly verbose and does not provide any novel insights into the method.
- What does it mean for an agent to be alive in the reward function definition? Also it is not clear why these agents are both competitive and cooperative? It is not clear why the agents’ actions are not independent of one another. The reward function seems overly complex and lacks clear justification for its design.
- Instead of framing this as a MAMDP, could this just be a single agent that predicts the full binary mask? This would greatly simplify the approach and remove the need for multi-agent training.
- Can Figure 2 also show what the token selection is for the baseline methods so there is a qualitative comparison? It is difficult to assess the effectiveness of the proposed method without a visual comparison to baseline token selection.
- In Table 1, it looks like the base Deit-B model has a higher GLOPs and better Top-1 Acc on compared to the proposed approach. This raises concerns about the overall effectiveness of the method, as it seems to underperform the baseline in some aspects.

### Questions
- Will more insights be provided so that the paper could be easier to follow?
- What's the meaning of the repetitive rows in the tables?
- Is the performance of the proposed method better or worse than
- I also have a concern that the token selection approach is effective mainly because the ImageNet classification problem is too easy. Would it also be effective on more challenging tasks?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Vision Transformers have a fixed token sequence that is independent of the input. However, computer vision tasks vary in complexity and the amount of token require maybe dependent on the input. This paper explores dynamic token pruning using an RL approach, and demonstrate that this reduces the computational cost of ViTs. They apply Multi-Agent Proximal Policy Optimization (MAPPO) to determine at each layer of a ViT whether a subset of token should be discarded. They claim to be the first work that integrates RL for dynamic token selection in ViT models. Experiments are on ImageNet, and show that their method reduces computational cost by 39% with a 0.17% decrease in accuracy.

### Strengths
- The motivation is clear why we want to prune tokens in large vision transformer models and an RL approach seems like a reasonable solution.
- Experiment results on ImageNet are interesting, showing that their approach does reduce redundant / unnecessary tokens in the image thereby reducing the computational cost without compromising performance.

### Weaknesses
1. __Reference format error__: `\citep{}` should be used for references w.r.t. the ICLR submission style.

2. __Lacking proper references__: In the Introduction section Lines 80-81, the authors state that previous works on dynamic token pruning favour Gumbel-Softmax since RL-based methods converge slowly. Could the authors cite which existing work(s) claims this? Besides, in the Introduction section Lines 87-88, MAPPO is mentioned as a representative RL-based method, but without reference.

3. __Missing quite a lot of important token reduction works__: In both the Introduction and Related Work sections, only a few fundamental yet outdated token reduction methods are cited. EViT [1] that proposes an efficient token selection strategy based on the [CLS] attention should be mentioned and compared as a strong baseline. ATS [2] that utilizes a learnable scoring function for estimating the importance of each token should be mentioned and compared as a strong baseline as well. In addition to [1,2], many following token pruning methods [3,4,5] and token merging methods [6,7,8] should be included and possibly compared in this paper. 

4. __Insufficient experiments__:

    4.1. __Lacking backbones__: The proposed RL4DViT is only adopted and validated on DeiT-B [9]. However, its performance on other backbones is unclear. To demonstrate its __generalizability on different model sizes__, experiments on DeiT-S and/or DeiT-T should be conducted. To demonstrate its __generalizability on different ViT architectures__, experiments on LV-ViT [10] or Swin-Transformer [11] should be conducted.

    4.2. __Lacking runtime comparisons__: Although this paper provides theoretical computational complexities (i.e., GFLOPs), these complexities do not indeed reflect the model's efficiency. Some methods with low GFLOPs may result in an even longer inference time since some operations (e.g., tensor reshaping, and in-memory selection) do not count toward the theoretical complexity [12]. Following the latest common practice, I suggest the authors report the real inference time.

5. __Lacking motivations on using multi-agent RL__: When utilizing MAPPO in RL4DViT, the authors adopt the parameter-sharing schema for agent policies and value functions. Thus, it arouses an intuitive question that whether current MAPPO can be replaced by __single-agent__ PPO. This question is not well addressed from the perspective of both the Introduction and Method parts. In addition, in the experiments, owing to the utilization of MAPPO, both PPO and IPPO [13] should be included in the baseline methods to illustrate the advantages of the multi-agent framework and the centralized critique respectively.

6. __Trivial performance gain__: While DynamicViT [14] achieves 81.3% top-1 accuracy on DeiT-B with 11.2GFLOPs, the proposed MAPPO-DeiT-B only achieves 81.38% with 11.6GFLOPs. Such performance gain is trivial and does not demonstrate the superiority of using RL in token selection. Nonetheless, DynamicViT is a 2021 work and has been surpassed by many following works in both accuracy and efficiency. 

7. __Lacking in-depth analysis__: Following Weakness 6, given that this paper focuses on the token selection part, the authors should justify why the MARL-based selection is better, with comparisons to other token selection strategies outlined in [1,2,6,7,8]. However, this paper lacks a quantitative analysis of the benefits of using MARL. And the qualitative analysis in Figure 2 does not clearly demonstrate its advantage over existing token selection methods.

### Questions
- Why did you choose to model this as a multi-agent RL problem as opposed to a single agent? 
- Can you explain the design choices for constructing the MDP in more detail? 
- Can you provide more experimental results in other computer vision tasks and datasets?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes to utilize a multi-agent reinforcement learning (MARL) approach for the token selection process in token pruning for efficient ViTs. Specifically, a multi-agent proximal policy optimization (MAPPO) method is adapted to the token selections. The proposed method is validated on one ViT backbone and compared with existing token pruning methods.

### Strengths
1. __Interesting idea__: The idea of incorporating MARL into the token selection process is interesting and novel. As far as I know, this is the first work leveraging MARL for token reduction.

2. __Well written and organized__: This paper is well-written and organized. It's easy to read and follow.

3. __Clear explanations__: The introduction and explanations to the MARL method are clear.

### Weaknesses
1. To address the proposed token selection by using RL, a straightforward approach is to optimize it with a single-agent reinforcement learning method. The input features can be regarded as the input state and the decision of whether to retain or discard each token can be regarded as the action. However, the authors didn’t explore single-agent RL methods or discuss the differences. It would be better for the authors to explain the reason for not exploring single-agent RL methods or analyzing the differences between single-agent and multi-agent RL methods.
2. Except for classification results on ImageNet-1K on ViT-B, there are no other datasets (CIFAR-10/100) or vision models (ViT-T/ViT-L/Swin). It would be better for the authors to validate RL4DViT on more datasets or vision models or explain the reasons for choosing only one experimental setting.
3. There are several outstanding token pruning methods that the authors didn’t compare or mention [1][2]. I think the authors should discuss the differences or the advantages of RL4DViT with more baseline methods.
4. Should the rewards of discarded tokens be the same? I think the tokens discarded at earlier stages should have higher rewards, which can cause more computation cost reduction. This is just my suggestion that may be helpful for further improvement and will not affect my ratings.

### Questions
1. According to W2, could the authors please provide references/citations to the claim in Lines 80-81 and which MAPPO method is adopted?

2. According to W3, could the authors please discuss these token reduction methods in the paper and compare the proposed RL4DViT with them? Moreover, could the authors please further compare different token selection strategies since this paper mainly focuses on the token selection part?

3. According to W4, could the author please provide more experimental results on different backbone sizes and different backbone architectures? Could the authors please provide real running time comparisons, especially with EViT, ATS and ToMe?

4. According to W5, could the authors please provide a clear justification for using multi-agent PPO over single-agent PPO? Could the authors please conduct experiments to validate this choice?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents "RL4DViT", a novel framework for the dynamic token pruning task in ViTs based on multi-agent reinforcement learning methods. RL4DViT takes each image token as an agent and decides whether to retain or discard itself based on its vector. Within sequential ViT blocks, RL4DViT formulates a Markov Game, to maximize the reward (higher accuracy & lower computational cost). Extensive experiments validate that RL4DViT can reduce 39% computational cost with only a 0.17% top-1 accuracy decrease on ImageNet-1K, validating the effectiveness of the proposed method.

### Strengths
1. Modeling the dynamic token pruning task as a Markov Game is quite novel and reasonable.
2. Utilizing MAPPO to solve it makes sense.
3. The presentation of the algorithm is clear.
4. Compared with DynamicViT and A-ViT, the proposed method performs slightly better.

### Weaknesses
1. To address the proposed token selection by using RL, a straightforward approach is to optimize it with a single-agent reinforcement learning method. The input features can be regarded as the input state and the decision of whether to retain or discard each token can be regarded as the action. However, the authors didn’t explore single-agent RL methods or discuss the differences. It would be better for the authors to explain the reason for not exploring single-agent RL methods or analyzing the differences between single-agent and multi-agent RL methods.
2. Except for classification results on ImageNet-1K on ViT-B, there are no other datasets (CIFAR-10/100) or vision models (ViT-T/ViT-L/Swin). It would be better for the authors to validate RL4DViT on more datasets or vision models or explain the reasons for choosing only one experimental setting.
3. There are several outstanding token pruning methods that the authors didn’t compare or mention [1][2]. I think the authors should discuss the differences or the advantages of RL4DViT with more baseline methods.
4. Should the rewards of discarded tokens be the same? I think the tokens discarded at earlier stages should have higher rewards, which can cause more computation cost reduction. This is just my suggestion that may be helpful for further improvement and will not affect my ratings.

[1] Kong, Zhenglun, et al. "Spvit: Enabling faster vision transformers via latency-aware soft token pruning." European conference on computer vision. Cham: Springer Nature Switzerland, 2022.

[2] Bolya, Daniel, et al. "Token Merging: Your ViT But Faster." The Eleventh International Conference on Learning Representations.

### Questions
Please refer to weaknesses. Why should the authors use MARL, instead of single-agent RL? This is my main concern, and I will raise my ratings if the authors' response addresses it well.

### Soundness
3

### Presentation
3

### Contribution
3
