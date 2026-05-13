# Directed Structural Adaptation to Overcome Statistical Conflicts and Enable Continual Learning

- Decision: Reject
- Scores: 3, 3, 1

## Abstract
Adaptive networks today rely on overparameterized fixed topologies that cannot break through the statistical conflicts they encounter in the data they are exposed to, and are prone to "catastrophic forgetting" as the network attempts to reuse the existing structures to learn new task. We propose a structural adaptation method, DIRAD, that can complexify as needed and in a directed manner without being limited by statistical conflicts within a dataset. We then extend this method and present the PREVAL framework, designed to prevent "catastrophic forgetting" in continual learning by detection of new data and assigning encountered data to suitable models adapted to process them, without needing task labels anywhere in the workflow. We show the reliability of the DIRAD in growing a network with high performance and orders-of-magnitude simpler than fixed topology networks; and demonstrate the proof-of-concept operation of PREVAL, in which continual adaptation to new tasks is observed while being able to detect and discern previously-encountered tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a novel technique to train adaptive networks by greedily adding nodes to a network when the edge weights exhibit zero gradient after training on a batch (saturation). The intended goal is to handle catastrophic forgetting in continual learning settings by gradually incrementing the network capacity when the capacity is full. A mechanism that requires training another network sharing the same set of nodes can be utilized to perform task detection for CL setting (see Sec 4). The method is benchmarked on MNIST and FashionMNIST and performs better than two baselines (EWC, MAS) and consistently worse than the other (PNN+FAE).

### Strengths
The idea seems to be completely original, with multiple novel components and procedures.

### Weaknesses
The proposed method is completely new and extremely complex. Section 3 and 4 are incapable of explaining the methodology properly. Many terminologies are coined, yet the relevance of coining these terminologies are ill-justified. The complexity of the method requires many design choices, yet these choices see to be determined arbitrarily (see P16L819 "Among the many ways to realize this condition, we choose to let .. Again, among infinite alternatives, we decide to set bk,1 = 0 and σ1 to be a scaled and shifted logistic function"). I even read the full Appendix yet failed to capture the essence of the proposed method.

The paper is poorly written. Pieces of information are scattered all around. Terminologies are not clearly defined before usage. Run-on sentences make the arguments hard to parse (e.g. P15L772 "Our goal with this point of modulation is to modulate the opposing yet nonzero gradients that the original edge was once under the influence of, in a manner that aligns them so that their adaptive potential, as quantified by their total magnitude, can be fully utilized without falling for statistical stable points.").

The main concern I had was, is designing such framework necessary when plugging in a familiarity autoencoder into an adaptive network sufficient to achieve the intended goal of performing adaptive increasing of network capacity while dealing with different tasks in continual learning? What is the justification for taking such complex routes yet yielding such marginal gains empirically and doesn't scale to normal sized models and datasets?

The terminology "statistical conflict" is not formally defined, despite it being a key motivation for designing DIRAD.

Couldn't the familiarity autoencoder be plugged into any adaptive networks to support continual learning with automatic detection of new data and assigning encountered data to suitable models adapted to process them?

There are many self-expandable / adaptive network papers mentioned in the related works session. Why are none of those part of the baseline for comparison?

How does the proposed technique contextualize with respect to the grand scheme of existing adaptive networks?

How does the proposed technique generalizes its performance to hold out dataset? The greedy approach of ENC is prone to either being stuck in local minima or overfitting to noise in the training data, since whenever the edge saturation condition triggers, the model expands its capacity to accommodate the training batch.

### Questions
* The terminology "statistical conflict" is not formally defined, despite it being a key motivation for designing DIRAD.
* Couldn't the familiarity autoencoder be plugged into any adaptive networks to support continual learning with automatic detection of new data and assigning encountered data to suitable models adapted to process them?
* There are many self-expandable / adaptive network papers mentioned in the related works session. Why are none of those part of the baseline for comparison?
* How does the proposed technique contextualize with respect to the grand scheme of existing adaptive networks?
* How does the proposed technique generalizes its performance to hold out dataset? The greedy approach of ENC is prone to either being stuck in local minima or overfitting to noise in the training data, since whenever the edge saturation condition triggers, the model expands its capacity to accommodate the training batch.

### Soundness
2

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
3

### Summary
Seeing that neural networks are prone to catastrophic forgetting due to their fixed topologies, this work proposes a new method of structural adaptation, namely DIRAD, which leads to a new type of networks that grow with a minimal complexity for a single task learning. Based on this adaptation method, this paper further proposes a framework so-called PREVAL to prevent forgetting (destructive adaptation or DA as defined by the authors in the paper) in continual learning (CL), through a two-stage learning and new task detection with L0 and L1 networks. Experiments on MNIST and F-MNIST are conducted to compare the performance of PREVAL with several CL approaches in neural networks in terms of the classification accuracy.

### Strengths
1. The proposed structural adaptation method is interesting and novel.

2. The resulted networks show less model complexity compared to neural networks.

3. DIRAD is further applied in CL as an architecture based method to address forgetting.

### Weaknesses
1. The major weakness lies in the scalability of the proposed method, as also pointed out in the discussion in section 6. The computational complexity of the proposed method increases a lot with high dimensional data, where the situation can be even worse in CL due to the need to handle a sequence of tasks. Specifically, the edge generation process, which involves calculating and comparing activation potentials (APs) across all possible node connections, becomes prohibitively expensive as the number of nodes and the dimensionality of the input increase. While the authors expect future "AI hardware" to support the proposed network structure, it is not clear how this type of networks can be used in practice and how significant the improvement is for them to replace neural networks.

2. I understand that the scale of experiments is largely limited by the computation complexity. Still, to convince the readers about the performance improvement of the proposed method, more experimental results with more datasets such as CIFAR and more advanced baselines are needed. The current experiments on MNIST and F-MNIST, while demonstrating the core concept, do not provide sufficient evidence of the method's effectiveness on more complex, real-world datasets. Furthermore, comparisons with state-of-the-art continual learning baselines, including those that incorporate regularization or replay strategies, are necessary to establish the proposed method's competitive performance.

3. One important property of the proposed method for CL is about new task detection without data replay. However, many out-of-distribution detection techniques indeed can be incorporated with current CL techniques to detect data distribution shifts based on new task data only, e.g., a suddenly increased loss of the current model with new data most time will detect the data distribution shift. To better justify the advantage of the proposed node validation based technique, experimental study should also be conducted to compare with CL techniques with simple data distribution shift detection strategies. The authors should also clarify how the proposed method performs when the data distribution shift is subtle or gradual, as a sudden increase in loss might not always be a reliable indicator of a new task.

4. The writing also needs to be improved. It is not easy to follow and understand what the authors are trying to say in general, particularly in section 3 and 4, e.g., how the APs are defined, how to check the conditions for edge generation. The description of the edge generation process lacks clarity, making it difficult to reproduce the results or understand the underlying mechanisms. The relationship between immediate and total APs, and the conditions under which edges are generated, should be explained more precisely.

### Questions
1. What is the relationship between the immediate AP and the total AP? This is not clear as least from the main body.

2. In Figure 1b, why the immediate AP of the node is exhausted but its total AP is not? Why does the generated edge have a zero gradient?

3. A priority ordering mechanism is introduced to grow the network and the authors took a conservation scheme by only performance a single generative process per step. This seems still not to answer the question "when to stop growing" (or "how much growth is necessary").

4. It seems that PREVAL needs to store multiple models and evaluate new data on all of these models. This will increase the complexity a lot in terms of both memory size and computation cost.

5. While I agree that using neural networks to predict internal nodes can cost much more compared to DIRAD, it is not clear if doing this thing, i.e., predicting internal nodes, is necessary or worth at the first place.

6. How is the inference conducted? As shown in Figure 2, the test sample is processed by the best-matching model. But during inference no task ID or ground truth is provided, how to determine the best matching model?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper claims to design a continual learning approach that can non-parametrically scale with the complexity of the data. They show their performance on two grayscale vision datasets: MNIST and FMNIST.

### Strengths
I did not find any strength in the paper.

### Weaknesses
The paper is hard to follow and uses technical terms and math notations without first defining them and they use confusing terminology without properly setting the stage for the discussion. The figures are vague and small, captions are inadequate to describe the experiments done.

The paper only considers average accuracy which is a poor indicator of performance of a continual learning (CL) system. In a CL system, there are multiple tasks in the environment which arrive sequentially. The dynamics between the task performance is important to characterize the system's capability of transferring knowledge between tasks. Reporting only accuracy may mask the performance in other tasks. For example, consider a CL system with 3 tasks having accuracies 100 (task 3), 70 (task 2) and 10 % (task 1). The average accuracy will be 60% which completely masks the poor performance on task 1. However, as can be seen, the system drastically forgets the older tasks and focuses on the current task more. This is a general phenomenon for most of the learners and CL aims to avoid that drastic reduction in older task accuracy (popularly known as catastrophic forgetting). So reporting transfer as well as forward and backward transfer is necessary to fully characterize the system. Another important feature to consider in a CL system is its memory overhead. These CL systems are meant to perform in an environment with a lot of tasks and how they grow and perform with the task complexity is important. See references 1, 2 for other performance statistics like transfer, forward and backward transfer, memory overhead. Moreover, they chose EWC as a baseline which is a really old method and I believe it requires task ids which is different from their setup. However, I never found EWC performing as poor as the author reported.

The proposed approach does not address catastrophic forgetting, In Table 1 their accuracy degrades over tasks and this indicates they may completely forget the older tasks if they had tested their system on more tasks. To eliminate this criticism, an experiment with a lot of tasks from imagenet would help. They choose poor baselines. There are methods in the literature that can improve on past tasks by virtue of seeing new task (backward transfer). A comparison with such approaches in [1,3,4] would help to quantify their novelty. In CL, the goal is to incrementally improve the model representation while having access to more data from different tasks. If the model breaks the plasticity-rigidity trade-offs and overfits to the recent tasks, the representation does not improve over time. I think the field has moved beyond trying to avoid forgetting [1,3], rather the goal should be to improve performance on older as well as recent tasks.

They consider only 3 tasks and chose grayscale datasets. To my experience, MNIST does not require even CNNs to perform well and can perform really well even with an MLP. It is popularly known that these datasets are of lower complexity. Methods that perform well on MNIST may break when tested on more complex RGB datasets like CIFAR10, CIFAR100, Imgaenet, FOOD1k. As the authors do not provide any theoretical proof that their CL can retain performance on a large enough task-sets and relies heavily on empirical validation, it is useful to validate their model over large and varied datasets. Otherwise, they may be overfitting to a particular simple scenario. CL systems are not useful unless they can perform on a lot of tasks (~100-1000 tasks) on a relatively constrained resource setting.

They lack a detailed literature review. The field is vast and diverse. Some methods use constant capacity (EWC, O-EWC, LwF) while others grow capacity [1,2,3] as more tasks arrive. Even there are different types of replay strategies in the literature which rehearse on older task data to mitigate forgetting. Without comparing and contrasting their approach with different groups in the literature, it is really hard to make decision on their performance.

The biggest flaw I found is lack of detailed experiments and poor writing. It is hard to follow their flow of writing and they abruptly start describing their model without any pre-context. CL systems are complicated. There are multiple algorithmic modifications contributing to a particular feature. Hence, for any CL system, it is necessary to do ablation study to tweak out the relative contribution of different algorithmic modification in comparison with the control group. Another important experiment is adversarial experiment where one tries to break the algorithm by providing adversarial tasks or making the environment really complex. These experiments provide valuable insights on how the model behaves and when it may fail. The paper does not include any of the above experiments.

### Questions
1. The paper only considers average accuracy which is a poor indicator of performance of a continual learning (CL) system. In a CL system, there are multiple tasks in the environment which arrive sequentially. The dynamics between the task performance is important to characterize the system's capability of transferring knowledge between tasks. Reporting only accuracy may mask the performance in other tasks. For example, consider a CL system with 3 tasks having accuracies 100 (task 3), 70 (task 2) and 10 % (task 1). The average accuracy will be 60% which completely masks the poor performance on task 1. However, as can be seen, the system drastically forgets the older tasks and focuses on the current task more. This is a general phenomenon for most of the learners and CL aims to avoid that drastic reduction in older task accuracy (popularly known as catastrophic forgetting). So reporting transfer as well as forward and backward transfer is necessary to fully characterize the system. Another important feature to consider in a CL system is its memory overhead. These CL systems are meant to perform in an environment with a lot of tasks and how they grow and perform with the task complexity is important. See references 1, 2 for other performance statistics like transfer, forward and backward transfer, memory overhead. Moreover, they chose EWC as a baseline which is a really old method and I believe it requires task ids which is different from their setup. However, I never found EWC performing as poor as the author reported.

2. The proposed approach does not address catastrophic forgetting, In Table 1 their accuracy degrades over tasks and this indicates they may completely forget the older tasks if they had tested their system on more tasks. To eliminate this criticism, an experiment with a lot of tasks from imagenet would help. They choose poor baselines. There are methods in the literature that can improve on past tasks by virtue of seeing new task (backward transfer). A comparison with such approaches in [1,3,4] would help to quantify their novelty. In CL, the goal is to incrementally improve the model representation while having access to more data from different tasks. If the model breaks the plasticity-rigidity trade-offs and overfits to the recent tasks, the representation does not improve over time. I think the field has moved beyond trying to avoid forgetting [1,3], rather the goal should be to improve performance on older as well as recent tasks. 

3. They consider only 3 tasks and chose grayscale datasets. To my experience, MNIST does not require even CNNs to perform well and can perform really well even with an MLP. It is popularly known that these datasets are of lower complexity. Methods that perform well on MNIST may break when tested on more complex RGB datasets like CIFAR10, CIFAR100, Imgaenet, FOOD1k. As the authors do not provide any theoretical proof that their CL can retain performance on a large enough task-sets and relies heavily on empirical validation, it is useful to validate their model over large and varied datasets. Otherwise, they may be overfitting to a particular simple scenario. CL systems are not useful unless they can perform on a lot of tasks (~100-1000 tasks) on a relatively constrained resource setting.

4. They lack a detailed literature review. The field is vast and diverse. Some methods use constant capacity (EWC, O-EWC, LwF) while others grow capacity [1,2,3] as more tasks arrive. Even there are different types of replay strategies in the literature which rehearse on older task data to mitigate forgetting. Without comparing and contrasting their approach with different groups in the literature, it is really hard to make decision on their performance.

5. The biggest flaw I found is lack of detailed experiments and poor writing. It is hard to follow their flow of writing and they abruptly start describing their model without any pre-context. CL systems are complicated. There are multiple algorithmic modifications contributing to a particular feature. Hence, for any CL system, it is necessary to do ablation study to tweak out the relative contribution of different algorithmic modification in comparison with the control group. Another important experiment is adversarial experiment where one tries to break the algorithm by providing adversarial tasks or making the environment really complex. These experiments provide valuable insights on how the model behaves and when it may fail. The paper does not include any of the above experiments.

[1] https://arxiv.org/abs/2004.12908
[2] https://arxiv.org/pdf/2012.12631
[3] Ramesh, Rahul, and Pratik Chaudhari. "Model zoo: A growing" brain" that learns continually." arXiv preprint arXiv:2106.03027 (2021).
[4] Ruvolo, Paul, and Eric Eaton. "ELLA: An efficient lifelong learning algorithm." International conference on machine learning. PMLR, 2013.

### Soundness
1

### Presentation
1

### Contribution
1
