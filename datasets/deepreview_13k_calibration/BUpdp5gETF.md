# Different Rates for Different Weights: Decoupled Relative Learning Rate Schedules

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 3, 1

## Abstract
In this work, we introduce a novel approach for optimizing neural network training by adjusting learning rates across weights of different components in Transformer models. Traditional methods often apply a uniform learning rate across all network layers, potentially overlooking the unique dynamics of each part. Remarkably, our introduced Relative Learning Rate Schedules (RLRS) method accelerates the training process by 13.6%, particularly in complex models such as the Mixture of Experts (MoE). Hyperparameters of RLRS can be efficiently tuned on smaller models and then extrapolated to 27x larger ones. This simple and effective method results in a substantial reduction in training time and computational resources, offering a practical and scalable solution for optimizing large-scale neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Conventionally, when training  a transformer model, the learning rates and the learning rates schedules of parameters in the entire model are set the same. However, recent works have shown that the weight updates of different modules in a Transformer model have varied dynamics, indicating that letting all modules share the same learning rate schedule may decrease the stability of the training process. Motivated by this, this paper has proposed a module-adaptive learning rate schedule called Relative Learning Rate Schedules (RLRS), which fine-tune the learning rate schedule for each module adaptively using a proposed approach called Local Search. The paper has also suggested that the RLRS's of a smaller model can be preserved to be applied by a larger model without much loss of performance. Experiments have been conducted to show the efficiency and effectiveness of the proposed RLRS.

### Strengths
1. Has a valid and strong motivation.
2. The finding that the RLRS's of a smaller model can be transfered (with slight adjustment) to a larger model without losing much fitness on the larger model is intriguing and practically meaningful.
3. The experiments are comprehensive and do show the effectiveness and efficiency of the proposed RLRS.

### Weaknesses
1. The validity of the claim that the hyperparameters of small model remains robust in large model is not convincingly demonstrated.
2. The hyperparameter tuning process is based on plain searching, which make the algorithm lack of efficiency in practice. Also, in this context, it's not convincing enough to say that the improvement of RLRS comes from using different learning rates schedules for different modules. It's simply because we have introduced more hyperparameters so that we have more degree of freedom to fine-tune the training process, just like in a standard deep learning task, if the model has more parameter, it's natural to predict that the training performance of the model will be much improved.

### Questions
1. Line 123 to 124 on page 3. Here the authors indicate that they demonstrate that the same set of relative learning rates remains robust across a range of model sizes "in the next section". However, in the next section 2.1, I don't see any demonstrations of the claim, but only introductions of the relative LR adjustment algorithms. Also, although Figure 4 does somehow show that the performance of $\lambda_{small}$ extrapolated to large models remains optimal or nearly optimal, it still hasn't demonstrated the "across 'a range of model sizes'" part in the claim.
2. Algorithm 1 and Algorithm 2 are named the same: "Relative LR Adjustment Algorithm". Although they can be distinguished by simply indicating algorithms 1 or algorithm 2, it's still better to give them distinct names since they seem to be an essential part of the paper.
3. Line 159. What "substantial gains" exactly has applying relative rate to an already tuned base model offered?
4. Algorithm 3, step 2. How are the set of the 4 values derived?
5. Algorithm 3, step 3. How is an "improvement" defined? Also, speak of improvement, I believe we are comparing the current experiment with the previous one. Then in this context, how is the very first experiment set up and run?
6. Section 3.3. This section indicates that after we have got the best learning rate schedules for both RLRS model and baseline model, the former one can be trained faster than the latter one. But is the process of fine-tunning taken into account? Meaning, will the process of fine-tunning in RLRS take much longer time that that in baseline, since there are more hyperparameters to be tuned, and the process seems to be based on plain searching?
7. Should we care about the changes in the test loss between RLRS trained model and baseline trained model?
8. Section 4.1. Is the analysis in this section conducted on a small model or a large one?
9. Section 4.1, Attention. Is there an explanation or an insight behind the behavior of the Attention module that the learning rate remains unchanged? Also, the authors haven't analyzed the behavior of learning rates in the Attention module in the dense models, which is illustrated in Figure 5.
10. Table 4. The start value of Embedding should be 3.3 right, according to line 279 to 280?
11. Whenever mentioning "performance" or "loss" etc., please specify which kind of performance or loss (training or test), e.g., Figure 2, and other places.
12. Does the stability of the training process necessarily lead to better eval loss?
13. Line 375. The authors claim the Figure 4 also shows the importance of tuning the relative learning rate for individual modules. Please explain this claim from the plots in Figure 4.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes Decoupled Relative Learning Rate Schedules (RLRS) for Transformers, assigning distinct learning rates to different components like Embedding and Attention layers. The authors suggest tuning these rates on smaller models and then applying them to larger ones to save on computational costs. Experiments with dense and Mixture of Experts (MoE) models show improved training speed and stability, particularly in large-scale MoE setups. The results indicate that RLRS can scale efficiently, offering an approach to optimize Transformer training at larger scales.

### Strengths
1. The proposed method has been applied to large model scales, which is practical if the implementation and results can be verified.

### Weaknesses
1. (**Limited Novelty of proposed approach**) The authors assume that relative learning rates tuned on smaller models will perform equally well on much larger models. A similar idea has been proposed in [1], but there is no discussion of comparing it with related work.

2. The rationale for introducing separate learning rate schedules for different components is not well-explained. The rationale and motivation mentioned in the paper are only listed below, which is not convincing.
> At the same time, modern Deep Learning architectures are not homogeneous, with different parts on the training phase, which can be problematic in some cases. For example, in Mixture of Experts (MoE) models, the Router often stabilizes early in training, leading to deterministic routing to the Experts

3. The paper does not sufficiently compare its approach with established methods for adaptive learning rates, such as [2]. 


**Reference**
[1] Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer

[2] Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training

### Questions
1. could the author provide the training curves or the measurement of training time to verify the time reduction reported in the paper?
2. What is the computational overhead associated with tuning the relative learning rates on smaller models? A breakdown of the resources required to tune these rates on smaller models and transfer them to larger ones would clarify the practical efficiency of this approach in real-world applications.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes using different peak learning and final learning rates for different types of layers in GPT training across both dense and mixture-of-expert configurations. They show that the adjustments can be tuned on a small scale and transferred to larger models, providing a speedup (reduced tokens for a given loss) on the order of 10-20% in both cases. The paper then analyzes and interprets some of the tuned adjustment values.

### Strengths
- Problem tackled is practical and of interest to the community.
- The core idea is interesting.
- The paper is clear and easy to follow.
- The authors tune their hyperparameters well.

### Weaknesses
- The overall novelty of the work might be limited given that tuning learning rates for each component of the network is already well known e.g. in muP works [1] [2].
- The paper doesn’t answer the question of whether the final lr values are truly needed. Figure 4 suggests that training is mostly sensitive to the peak lr of different components, but this is exactly what existing work does.
- The experiments are relatively small in scale and could be better ablated.

[1]: https://arxiv.org/abs/2407.05872
[2]: https://arxiv.org/abs/2407.17465

### Questions
Recommendation: Overall I recommend rejection based on seemingly limited novelty over existing approaches combined with the lack of other significant contributions (e.g. a large-scale validation or a theoretical analysis of these approaches could be valuable despite the method not being novel).

Suggestions:
- I recommend trying to add stronger evidence that the final learning rate values are needed to justify your approach over existing work.
- I somewhat doubt that schedules for short runs transfer well to longer runs. For example weight decay can be seen as an (effective) learning rate scheduler but it only makes a significant difference for longer runs. It might be more convincing if you could provide an example or arguments to support this approach.
- In Figure 1 you show the update size over time and use this to justify the learning rate schedules. Some other optimizers like Lion would fix the update size. Would you expect different schedules for different parameters to help in this case?
- If you pursue using schedules for each parameter it would be nice to see a greater difference, e.g. something like different warmup lengths or earlier decay with a WSD. This would be a greater differentiator from the peak lr.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes to have different learning rates for different parts of the transformer model. The authors propose a simple heuristic for deciding what the best learning rate is for each component. Their method, RLRS, improves training speed and stability. The proposed approach shows a 13.6% acceleration in training time and can scale effectively to models up to 27 times larger without the need for extensive re-tuning of hyperparameters.

### Strengths
• I think the topic the authors are aiming to address is interesting, and it makes sense that different learning rates for different components would help to increase convergence and performance.

### Weaknesses
• This proposed method is not theoretically motivated and the proposed method appears to be a very crude heuristic for selecting the learning rate. Algorithm 3, which discusses how the hyperparameters are found suggests that the authors are just doing a kind of random search, where you multiply the values by a factor from (x0.2 - x5). 

• There is very little background or discussion covering the central topics of this paper. For example, there is almost no time spent discussing contemporary hyper-parameter optimization techniques. Furthermore, the idea of giving different components different learning rates is not a new one – in fact it is natively supported in libraries such as PyTorch.

### Questions
N/A

### Soundness
1

### Presentation
2

### Contribution
1
