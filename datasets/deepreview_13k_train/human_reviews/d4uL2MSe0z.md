# Dynamic Layer Tying for Parameter-Efficient Transformers

- Decision: Accept
- Scores: 6, 6, 1, 5

## Abstract
In the pursuit of reducing the number of trainable parameters in deep transformer networks, we employ Reinforcement Learning to dynamically select layers during training and tie them together. Every few iterations, the RL agent is asked whether to train each layer $i$ independently or to copy the weights of a previous layer $j<i$. This facilitates weight sharing, reduces the number of trainable parameters, and also serves as an effective regularization technique. Experimental evaluations validate that our model modestly outperforms the baseline transformer model with regard to perplexity and drastically reduces the number of trainable parameters. In particular, the memory consumption during training is up to one order of magnitude less than the conventional training method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors focus on the problem of reducing the number of parameters in transformers using Reinforcement Learning, specifically a variant of Q-Learning, to dynamically select layers in transformers and tie them together. They evalutate their approach on language models such as GPT-2 and BERT. They demonstrate the performance of their approach both in terms of final model performance and the amount of parameters reduced. They also conduct an ablation analysis of their approach.

### Strengths
1. Large transformer models have demonstrated excellent performance, but they are often very expensive in terms of computational resources. The paper addresses a very timely problem: ensuring transformer models can be applied in a practical setting without excessive cost.

2. The proposed method, parameter tying via Q-Learning-is intuitive and sensible approach for this problem.

3. Quantitative results both on the axis of performance and computational resources is convincing.

### Weaknesses
1. The approach is very specific in its focus. The architecture in question are only transformers, and evaluation is only on transformers in the language domain. It is unclear if these results hold for transformers in other data domains (such as vision transformers). It is also unclear if this approach (specifically parameter tying) could work for other neural architectures.

### Questions
1. The paper could be strengthened by evaluation on different data domains or perhaps even other neural architectures entirely. How would this approach perform on a vision transformer?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to reduce the number of trainable parameters of Transformers by dynamically tying the weights of different layers using reinforcement learning during the training process of Transformer. Experimental results indicate that compared to the conventional training method, the proposed approach effectively reduces the number of trainable parameters and slightly improves performance (perplexity score).

### Strengths
1 By employing a simple deep reinforcement learning algorithm, the number of trainable parameters of GPT-2 and BERT has been significantly reduced. The algorithm is easy to implement and holds the potential for application in other Transformer-based neural networks.

2 The algorithm has been thoroughly analyzed, providing a detailed explanation of the reasons for its effectiveness.

### Weaknesses
1 The Methods section contains a considerable amount of redundant content, providing a step-by-step explanation of the algorithmic process.

2 The experimental results only show the comparison of the proposed method and the conventional training method, lacking comparison with other baselines and the related methods.

3 The related work is not adequately summarized. There is only one publication after 2020 shown in the section of Related Work, and there is a lack of research focusing on improving the Transformer neural network architecture.

4 The conclusion "Having this global alignment is crucial for smooth training despite large blocks of weights being copied during the process" seems to conflict with Table 3.(vi).

5 'While in Tab. 2 it is demonstrated that our method somewhat slows down the training time, Tab. 1 presents a reduction of almost 50% in runtime. We believe, but have not yet verified, that this is due to the difference in hardware between the two experiments. While GPT-2 experiments run on A100, the BERT experiments run on A6000/A5000.' Is there a citation error present?

6 The ultimate goal of reducing training parameters is to decrease memory? What is the actual consumption of memory?

### Questions
1 The conclusion "Having this global alignment is crucial for smooth training despite large blocks of weights being copied during the process" seems to conflict with Table 3.(vi).

2 'While in Tab. 2 it is demonstrated that our method somewhat slows down the training time, Tab. 1 presents a reduction of almost 50% in runtime. We believe, but have not yet verified, that this is due to the difference in hardware between the two experiments. While GPT-2 experiments run on A100, the BERT experiments run on A6000/A5000.' Is there a citation error present?

3 The ultimate goal of reducing training parameters is to decrease memory? What is the actual consumption of memory?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new means for essentially doing architecture search on a transformer model. The available variation for the model are which layers should be tied together, and which should remain independent. 

They employ an RL algorithm to do the selection of what should be connected to what. The reward signal comes straight from the perplexity of a model after an action has been taken. The results are very exciting and significant. It is very possible that the authors have just opened the floodgates to a new research path on which many will walk in the near future. 

The resulting models demonstrate that a transformer model with 48 layers, may require between 7-10 independent layer weights to perform as well, or better than conventionally trained 48 layer models. This opens up a lot of questions related to modern artificial neural circuitry and may allow for interesting modularization research to take place.

### Strengths
1. Clear, concise and precise writing. 
2. The idea attempted itself is intriguing. 
3. The idea is executed very well, resulting in excellent outcomes. 
4. The results are very promising.
5. The results open up a lot of new questions, as well as motivate the need for research in the pathway the authors have opened up.
6. The paper represents what could be a seminal moment in architecture search methods, as well as understanding modularity in NNs.

### Weaknesses
 1. The method section, while technically sound, suffers from a lack of clarity as to the method being presented. For such a significant contribution, it is important to ensure that one can understanding the fundamentals of the method without having to crunch through all of the equations presented and fill many of the gaps with their own imagination. Perhaps something like a functional diagram, a more intuitive algorithm, or just a page that lays out the ingredients one by one, as well as how they are optimized, followed by the algorithm page would serve clarity of communication better. Specifically, the exact mechanism of how the RL agent interacts with the transformer model during training is not sufficiently clear. It's difficult to grasp how the agent's actions (tying or untying layers) are translated into concrete changes in the model's architecture and subsequent training dynamics. The description lacks a step-by-step breakdown of the training process, making it hard to follow the flow of information and optimization.
2. It's not clear if the authors have tried additional rewards in addition to PPL after updates, or if it was the only one tried. The choice of perplexity as the sole reward signal might be limiting. It's possible that other metrics, such as training speed, or perhaps a measure of the model's generalization capabilities, could provide a more comprehensive reward landscape, potentially leading to more efficient or robust architectures. The paper does not explore this space, which is a missed opportunity.
3. Figure 1 is hard to read and understand. A more intuitive approach could leverage colour-coding to indicate a particular layers weights and perhaps a sequential figure showing a layer by layer colour coding might be more helpful/clear. The current visualization makes it difficult to track the connections between layers and how they evolve over time. The lack of a clear visual representation hinders the understanding of the learned architectures. A more detailed visualization, perhaps with a node-link diagram where nodes represent layers and links represent weight sharing, could be more effective.

### Questions
1. Have you tried retraining the architecture that your method learned from scratch? As in, grabbing the connection maps, using that to initialize a new transformer and training from there. It would be interesting to how it compares with the model you trained jointly. 
2. How did you try to balance exploration with exploitation? Presumably past actions can have a major effect on future trajectories. Did you employ any random restarts, or perhaps running multiple models in parallel so you can get feedback from a population rather than an individual for your RL updates.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to share the weights across layers when training Transformer architecture from scratch. The proposed method utilizes a network Q, which is trained with Q-learning, to assign the sharing policy. Experiments on several text datasets show that the proposed method uses less trainable parameters, reaches comparable performance as the conventional training, and sometimes reaches better training speed.

### Strengths
The paper studies the weight-sharing scheme of training Transformers, and this may be used to reduce the training cost of developing large models.

### Weaknesses
There are two main weaknesses of the paper in my opinion.

1. The related work section is not complete and misses many relevant works and topics. I think several lines of research are very related to this paper but they are missing in the related work:

(1) network pruning (also lottery ticket hypothesis),

(2) weight sharing in Transformers,

(3) parameter-efficient fine-tuning methods (PEFT methods).

Network pruning is mentioned a bit in the introduction, but the paper doesn't mention the pros and cons of this paper against network pruning, making the contribution of this paper unclear. I also found that there are several shared-weight Transformers papers [1, 2, 3] that are not cited in the paper, and they should be discussed. The parameter-efficient methods (LoRA, Adapters, Prefix Tuning, Prompt-tuning, etc) save a significant amount of parameters (such as 1 - 5%) and are very relevant to this work.

[1] Subformer: Exploring Weight Sharing for Parameter Efficiency in Generative Transformers

[2] Sharing Attention Weights for Fast Transformer

[3] Lessons on Parameter Sharing across Layers in Transformers

2. Some weaknesses in experiments:

(1) Several weight-sharing techniques should be also included in the comparison.

(2) I would suggest reporting the performance on downstream tasks for a complete comparison. Lower perplexity sometimes does not mean higher downstream performance.

(3) The perplexity of the results seems very high compared to previous results. As far as I know, the perplexity of WikiText-2 is usually around 20 and the perplexity of 1-billion words is around 30. I would suggest finding the proper training recipe or training longer to let the model converge, or the current results may not be very convincing. The current better perplexity in Tables 1 and 2 might only be due to the faster convergence of the model with less trainable parameters.

### Questions
1. In Tables 1 and 2, why the training time of the proposed approach is a bit longer compared to the conventional training when training GPT-2 but is much less when training BERT?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
