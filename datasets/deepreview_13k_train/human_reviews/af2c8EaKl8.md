# Decision ConvFormer: Local Filtering in MetaFormer is Sufficient for Decision Making

- Decision: Accept
- Scores: 5, 8, 8

## Abstract
The recent success of Transformer in natural language processing has sparked its use in various domains. In offline reinforcement learning (RL), Decision Transformer (DT) is emerging as a promising model based on Transformer. However, we discovered that the attention module of DT is not appropriate to capture the inherent local dependence pattern in trajectories of RL modeled as Markov decision processes. To overcome the limitations of DT, we propose a novel action sequence predictor, named Decision ConvFormer (DC), based on the architecture of MetaFormer, which is a general structure to process multiple entities in parallel and understand the interrelationship among the multiple entities. DC employs local convolution filtering as the token mixer and can effectively capture the inherent local associations of the RL dataset. In extensive experiments, DC achieved state-of-the-art performance across various standard RL benchmarks while requiring fewer resources. Furthermore, we show that DC better understands the underlying meaning in data and exhibits enhanced generalization capability. Our code is available at \url{https://beanie00

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper revisits the efficacy of the transformer, originally devised for natural language processing, for reinforcement learning (RL). The authors' empirical studies demonstrate that the previous designs of the transformer for RL (e.g., decision transformer) could be an inefficient overparameterization mainly due to the lack of exploiting Markov property, which is a common assumption in RL. As a part of utilizing Markov property, the authors propose a new transformer model (which is a variant of MetaFormer), called Decision Convformer (DC). They empirically show the efficacy of DC in various environments, in particular, when Markov property holds.

### Strengths
The authors have demonstrated a potential risk and inefficiency of using the transformer with a long context length K when Markov property is strong.

As Markov property can be interpreted as a locality (or local dependence) in the sequence of interactions between the agent and the environment, the authors employ convolution filtering for token mixer in MetaFormer. The convolution filtering helps to reduce the number of model parameters (in particular, the number of token mixer parameters) and provides performance gain in offline RL settings (in particular, in hopper and antmaze datasets).

In the case of weak Markov property, the authors also propose DC^{hybrid}, which uses both the convolution filtering and the attention model. The hybrid DC showed superiority in Atari datasets, compared to DT.

The proposed DC and DC^{hybrid} might provide new promising options for model architectures in deep RL.

### Weaknesses
My major concern is the seemingly incomplete justification of the proposed architectures. In my understanding, just DT with a small K (i.e., short context length) could be sufficient and show comparable to or even better than DC. Additional comparisions (in terms of performance and computational complexity) on DC and DT with different choices of K would be helpful. Otherwise, it is unclear whether the gain of DC (or hybrid DC) is mainly from the good combinations of hyperparameters (including the embedding dimension, GELU, K, ...), or indeed the convolution filtering. 

In addition, the advantage of the proposed method (DC) is particularly remarkable in hopper and antmaze datasets. In fact, the gap between DC and DT is not significant in other environments. It seems necessary to clarify the environment-specific gain of DC over DT.

### Questions
Can you provide evaluations of the hybrid DC for the benchmark in Table 1 (environments with Markov property)? This would help choose architectures when the prior knowledge of the degree of Markov property is limited. If the hybrid DC is comparable to or better than DC and computational cost is not important, then one may simply consider the hybrid DC for such cases.

Can you report the computational complexity of the hybrid DC as you did for DT ad DC in Table 14,15,16?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
this paper propose Decison ConvFormer (DC) as an alternative of Decision Transformer (DT). The insight is that most RL task require locality and the particular parameterization of DT seems to not be optimal in learning it. In contrast, they propose to use a depth-wise conv block. The experiment results on both Mojuco and atari shows that it's better in both offline and online finetuning. The discussion section shows that the model generalizes better in RTG and dependes more on state in a meaningful way.

### Strengths
The paper provides a very good insight about the problem in modelling RL sequence, which is emphasis on local association. By introducing a convolution blocks, it is a very good idea built on insights to the specific problem, and I really like the motivating example in Fig3. 

The method is simple, and I think the community is easy to verify it after few lines of code changes.

The experiment results are strong, and cover both discrete and continuous domain. The hybrid architecture is a good balance between locality and long-term credit assignment.

The discussion section is good to see and the generaliation of RTG is an interesting result.

### Weaknesses
 There seems not much I can say. But I think to improve, the author could remove the mention of the MetaFormer framework. As someone who has never heard it before, I first though metaformer is a new transformer variant, but then I realized it's just a framework, which is a bit confusing to me.

Also the the name "token mixer block" should be avoided, since it reminds of the token mixing in the MLP-Mixer, which makes me confuse in the beginning.

### Questions
1. can you further describe details of the motivating examples? Do you only learn the attention directly of that one layer or all layers?
2. For the hybrid architecture, what happens if you do attention first then conv?
3. Can you also test the OOD generalization on novel task with multi-task learning?
4. Can you visualize the attention of that hybrid model in some atari games?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author proposed a new structure, called Decision Convformer, by replacing the token mixing step in MetaFormer with three causal convolution filter for RL tasks. The proposed Decision Convformer achieved better performance on well-known tasks with less training time.

### Strengths
1. Improvements with less training computation are achieved. Thus, the proposed DC is efficient.

2. The presentation is easy to follow. The motivation is also described clearly.

3. Extensive experimental results are provided.

### Weaknesses
1. How to compute the embeddings of a float number (reward) in the subsection 3.1? Some explanations might be helpful.

2. The reasons why the propose method is effective are needed to explained. It seems that the self-attention operation is more expressive then the proposed block (three causal convolution filters). Is the proposed DC only suitable for some settings, e.g. the setting with less data?

3. Why the ODC is worse than DC on some tasks?

### Questions
See the above section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
