# Pruning via Ranking (PvR): A unified structured pruning approach

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
The increase in width and depth has facilitated neural networks to learn from large amounts of data leading to state-of-the-art results in both vision and NLP tasks. 
    In order to democratize such massive networks, it is important to deploy them on resource-limited devices through model compression techniques such as structured pruning. 
    Unfortunately, most pruning methods are tailored towards compressing specific models due to widely differing network architectures for distinct tasks. 
    At the same time, it is desirable for pruning algorithms to generate optimal subnetworks according to user-specified parameter budgets.
    In this work, we propose Pruning via Ranking (PvR), a novel, global structured pruning approach which generates dense sub-networks that comply with any user-supplied parameter budget. 
    PvR consists of a grouping module and a ranking module that are used to generate smaller networks in terms of both function composition as well as network width for a given dataset. 
    The smaller networks are then trained from scratch instead of being fine-tuned as we empirically demonstrate using a recently proposed model complexity measure that re-initialization after pruning followed by re-training results in better performance. 
    We compare our method against multiple pruning approaches on benchmark datasets, namely, CIFAR10, Tiny ImageNet and IMDB 50K movie reviews, with standard models, namely, VGG16, ResNet34 and Bert-base-uncased. 
    We use both accuracy and model inference latency metrics to evaluate the performance of each approach. 
    The smaller networks proposed by PvR for a range of parameter budgets when trained from scratch outperform all other methods across all datasets and models. 
    In fact, our recommended sub-networks with fewer layers achieve less than $1$\% test accuracy drop even after pruning $90$\% of the original model across all networks and datasets while enjoying lower inference latency due to reduced depth.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a neural network pruning method. The importance of the network parameters is sorted based on their importance to the prediction result change before and after pruning. The model parameters are grouped to reduce computational cost. Pruning strategies are discussed for VGG 16, ResNet 34, and Bert model.

### Strengths
A novel network pruning method is proposed and verified by experiments.

### Weaknesses
1. The algorithm introduction is hard to follow. The missing of algorithm flowchart makes the reviewer difficult to have a clear idea about how exactly the described components work together.
2. Even though grouping is used to reduce computational cost, the cost of computational cost can still be quite high. There is no empirical analysis of time cost in the experiment.
3. The baseline models compared in the experiment are not quite state-of-the-art. More recent models need to be covered. Some of the existing methods are relevant to this work, such as
Kuang J, Shao M, Wang R, et al. Network pruning via probing the importance of filters[J]. International Journal of Machine Learning and Cybernetics, 2022, 13(9): 2403-2414.

### Questions
Please refer to the comments.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a new pruning method which can prune neurons, channels and layers. The authors claim that the method apply to both vision (VGG and ResNet) and NLP models (Bert). The core steps of the proposed pruning are:
1. Evaluate the importance of each neuron/channel/layer, etc. The importance metric is shown in Eq.2 of the original paper. It consists of two parts: (1) The output's L1 error before and after pruning a certain neuron (rescontruction error). (2) A constant error (hyper-parameter) if pruning a certain neuron leads to a different prediction result.
2. Group similar neurons/channels according to the correlation.
3. Prune unimportant groups. While the authors do not explain how to compute group importance according to neuron importance. I just assume the most naive "average" method is used.
Experiments are done on CIFAR-10, TinyImageNet, and IMDB.

### Strengths
1. The paper is well-written and easy to understand.
2. The authors propose to takes that "whether the prediction result changes" as a parts of importance metric. While most previous papers only concider the change of the output.
3. Experiments are done on both vision and NLP tasks.

### Weaknesses
I think the paper has some obvious flaws:
1. Lack of essential ablation studies. The authors introduce two very important hyperparameters: the constant error "d" and the group size. I think they will have a great influence on the final accuracy. The authors claim their algorithm applys to both vision and NLP models. However, it would meaningless if we have to carefully adjust these two hyper-parameters for the best accuracy on different models and tasks. This is my main concern.
2. The authors claim the proposed algorithms consider the paramete budget. While as I know, all existing pruning methods can achieve this because it is a basic requirement. Take L1 norm based pruing as an example, you can consider the parameter budget by adjust the pruning threshold (This process is very fast with ignorable cost).
3. Limited creativity. GC based initialization method is proposed by another paper, this paper only uses it.
4. VGG-16 is a very redundant model for CIFAR-10 dataset. The has been a consensus in the field. I doubt whether the corresponding results are still convicing.
5. I am not sure but the authors may not describe how to compute group importance according to neuron/channel/.. importance.
6. Lack of some details. As the paper says, the proposed method achieves lower latency because of layer pruning. Could you please describe in which case the proposed methed will prune an entire layer?
7. Lack of reference papers such as [1] (correlation based pruning) and [2] (reconstruction error based pruning).
[1] COP: Customized Deep Model Compression via Regularized Correlation-Based Filter-Level Pruning. IJCAI 2019
[2] ThiNet: A Filter Level Pruning Method for Deep Neural Network Compression

### Questions
Please see the weaknesses for details.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new pruning criterion based ranking. The ranking is achieved by a carefully designed importance function that pays more attention to those parameters that change the prediction of the network. An additional term  is introduced to penalise prediction changes. The experiments show positive results on CIFAR-10 and TinyImageNet.

### Strengths
This approach introduces an interesting ranking function. It would be beneficial if the author could offer a more detailed analysis of the ranking outcomes. Specifically, it would be intriguing to explore the ramifications of eliminating weights that do not result in incorrect predictions. What impact would this have on the overall model performance and efficiency?

### Weaknesses
The paper conduct empirical experiments on CIFAR-10 and Tiny-ImageNet, both of which are relatively small-scale datasets. It raises concerns about the generalizability and robustness of the proposed method. It would be advantageous if the author could present additional results using the ImageNet-1K dataset, which is more complex and varied. Furthermore, the paper currently lacks a thorough analysis of the proposed ranking method, which is crucial for understanding the efficacy and underlying mechanics of the technique. Including such an analysis would significantly enhance the paper's contribution to the field. Specifically, the analysis should include a detailed examination of the sensitivity of the method to the group size parameter used in the pruning process. It is unclear how the choice of group size impacts the final pruned network's performance and the computational cost of the pruning procedure. A more rigorous analysis of this parameter is needed to understand the practical trade-offs involved in its selection. Additionally, the paper does not provide sufficient insight into the behavior of the importance function, particularly how the penalty term for prediction changes interacts with the other components of the function. A deeper analysis of this interaction is needed to justify the design choices made in the importance function.

### Questions
Please see weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a structured pruning approach named Pruning via Ranking (PvR) that can prune the models according to user-assigned budget. PvR has one grouping module to group neurons for speeding up pruning process and one ranking module to estimate the importance of grouped neurons. It can reduce model depth, leading to training and inference efficiency wins. Apart from this, the authors suggest to retrain the subnet from scratch and proposes a metric called Geometric Complexity to measure its efficacy. The authors validated the PvR on several classic models comparing with other pruning methods.

### Strengths
1. PvR can work for both NLP and vision models
2. PvR can prune with user-provided parameter budget.

### Weaknesses
Lacks validation on the proposed grouping module. How can different grouping settings impact the performance of pruned model? How much it can speed up the overall process?

### Questions
1. What makes PvR perform well on both vision and NLP models? Why couldn't other pruning methods achieve this? Would like to hear more insights on this claim.
2. How long does Grouping and Ranking processes each take? How does the total time PvR takes compared to other pruning methods?
3. Is there any strategy to initialize and retrain the pruned model (does it have any relationship, like some proportional to the original model)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
