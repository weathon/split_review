# Efficient Heterogeneous Meta-Learning via Channel Shuffling Modulation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
We tackle the problem of meta-learning across heterogenous tasks. This problem seeks to extract and generalize transferable meta-knowledge through streaming task sets from a multi-modal task distribution. The extracted meta-knowledge can be used to create predictors for new tasks using a small number of labeled samples. Most meta-learning methods assume a homogeneous task distribution, thus limiting their generalization capacity when handling multi-modal task distributions. Recent work has shown that the generalization of meta-learning depends on the similarity of tasks in the training distribution, and this has led to many clustering approaches that aim to detect homogeneous clusters of tasks. However, these methods suffer from a significant increase in parameter complexity. To overcome this weakness, we propose a new heterogeneous meta-learning strategy that efficiently captures the multi-modality of the task distribution via modulating the routing between convolution channels in the network, instead of directly modulating the network weights. This new mechanism can be cast as a permutation learning problem. We further introduce a novel neural permutation layer based on the classical Benes routing network, which has sub-quadratic parameter complexity in the total number of channels, as compared to the quadratic complexity of the state-of-the-art Gumbel-Sinkhorn layer. We demonstrate our approach on various multi-modal meta-learning benchmarks, showing that our framework outperforms previous methods in both generalization accuracy and convergence speed.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper deals with the heterogeneous meta-learning problem from the perspective of channel shuffling modulation.   
Instead of the conventional fixed backbone + modulation layer scheme for multiple task distributions, this paper seeks to find a task-specific channel permutation routing mechanism.   

The idea is motivated by ShuffleNet and implemented with a task-specific prototypical vector to learn the shuffling operation. For the permutation matrix, this paper first adopts the Gumbel-Sinkhorn layer to generate the permutation. Then, the classical Benesˇ routing network is utilized to improve the efficiency. 

Experiments are conducted on several heterogeneous datasets and compared with various MAML-based methods. As a parameter-efficient method, the proposed method also performed generally better than baselines.

### Strengths
- (1) This paper provides a different perspective for heterogeneous meta-learning, i.e., channel shuffling by permutation learning. It can be a good alternative to the modulation-based methods. 
- (2) The utilization of the traditional Beneˇs network can improve the efficiency of the proposed method. 
- (3) Experiments are conducted on the meta-learning benchmark, and the results are fair and generally better than other MAML-variant methods.

### Weaknesses
 - (1) The authors describe the heterogeneous meta-learning problem from the MAML perspective. However, similar to heterogeneous meta-learning, researchers also used the terminology multi-domain/cross-domain to describe the diverse task distribution when dealing with few-shot meta-learning problems, e.g., [R1]. Besides Li et al. (2022), other related works applying feature modulation can also be discussed, such as [R2, R3]. 
- (2) I am wondering why permutation and channel shuffling work compared with modulation. The intuition of modulation assumes a strong shared backbone, and each dataset/distribution performs task-specific adjustments for its data. For the permutation case, it is better to visualize what permutation can be learned for different distributions. Specifically, it is unclear how the learned permutation matrices relate to the underlying task distributions. The paper would benefit from a more detailed analysis of the learned permutation matrices, perhaps by showing the actual permutation patterns or providing some statistical analysis of the learned permutations across different tasks. Furthermore, the connection between the task-specific prototypical vector and the learned permutation is not fully clear. It would be helpful to understand how the prototypical vector influences the permutation learning process and why this approach is effective for heterogeneous meta-learning.

### Questions
Please see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
**Edit: I have raised my score to 6 to reflect the author's updates to the submission.**


The paper considers the problem of meta-learning across heterogeneous tasks when the model is expected to extract and generalize the meta-knowledge and transfer it to quickly learn the novel tasks. Whereas, many meta-learning models focus on the tasks coming from the same distribution (homogeneous), the authors consider the directly the tasks coming from a multi-modal task distribution (heterogeneous setting). Recently, many appeared many methods that tackle the heterogeneous meta-learning, but they suffer from a significant increase in parameter complexity. As an alternative approach, the authors propose a novel strategy which incorporates modulating the routing between convolution channels in the network. The paper introduce a novel neural neural permutation layer based on the classical Benes routing network. Finally, the proposed method is compared against various meta-learning benchmarks.

### Strengths
The paper has a few significant strengths overall, which I will outline below:
1. Considering directly the heterogeneous tasks setting which I found especially significant within the Meta-Learning.
2. The main idea of introducing the Gumbel-Benes routing layer is very interesting and seems to be novel in Meta-Learning.
3. Leveraging the complexity of permutation layer inspired by the Benes network is fair.
4. I like experiment presented in Figure 3.
5. The presentation is clear. Overall, the flow of the manuscript is well-organized.

### Weaknesses
However, despite the strengths, the paper has a few major and minor weaknesses. I will focus on the experiments section especially, because I recognize it as insufficient: 

1. The results of all methods, presented in the Table 1 and Table 2, are usually within their standard deviations. Because of that, I will not support the claim that the presented method is significantly better than others.
2. The methods that are chosen for the comparison are not a current state-of-the-art methods, having a few years. I strongly encourage authors to include comparison with other methods like [1] or [2].
3. The comparison are considered only across a single neural network architecture. I admit that the scenarios of using the Gumbel-Benes routing layers are limited into CNN architectures. However, there is not the reason to skip the comparison on highly popular in Meta-Learning, ResNet architectures. I will suggest for sure comparison on at least ResNet-10 (as in, e.g., [3]).
4. The lack of more challenging 1-shot 5-way classification on Mini-Imagenet dataset. 
5. As far as I know, there is the first example of the Benes networks-inspired Meta-Learning approach. However, there were others works based on the Benes routing, e.g, [4]. I would like to see the Related Work section given credits to that works and comparing the proposed method with them.

### Questions
I would like to see especially the following experiments and improvements:
1. Provide results for the 1-shot 5-way classification setting on Mini-Imagenet.
2. Please, compare with state-of-the-art methods as suggested in Weaknesses section. 
3. The work will be better if you could test the Gumbel-Benes layers in ResNets also.
4. Add the Related Work section regarding other deep learning works utilizing the Benes networks/routing algorithm.

**Questions:**

1. Another place where the Gumbel-Benes routing layers might be beneficial are standard methods working on the Meta-Dataset [1], which is a created really heterogeneous tasks dataset. The best methods working on Meta-Dataset are often ResNets with some adapting layers within, so they are really within the scope of the Gumbel-Benes layers. For the example methods, please see the rank tables in [2].


**References:**

[1] Triantafillou, E., Zhu, T., Dumoulin, V., Lamblin, P., Evci, U., Xu, K., ... & Larochelle, H. (2019). Meta-dataset: A dataset of datasets for learning to learn from few examples. arXiv preprint arXiv:1903.03096.

[2] https://github.com/google-research/meta-dataset

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new meta-learning approach for heterogeneous sets of tasks. The method is presented as a permutation learning problem in which convolution channels are shuffled via a continuous switch network. This trainable routing network is parameterized by input embeddings learned via the prototypical loss (Snell et al., 2017), in which the centroids encode the prototype shuffling parameters corresponding to each task. The method is favorable compared to using Gumbell-Sinkhorn layers (Mena et al., 2018) which use routing embedding dimensions quadratic in the number of channels, hence requiring larger networks with more parameters and longer inference times. The proposed method is also empirically compared to a few other baseline algorithms that do not account for heterogeneity, matching SOTA performance in single task regime and outperforming alternatives in the heterogeneous task setup.

### Strengths
Originality and significance: The presented method shows clear improvements over the studied baselines by showing how a task-based ordering can be derived from a smaller dimensional embeddings: $C \log C$ v.s. $C^2$. The empirical analysis uses both problems with synthetically generated tasks (JIGSAW), as well as problems formulated by grafting multiple tasks. The results show the effectiveness in heterogeneous meta-learing domains.

Quality and clarity: The paper is easy to follow and the experiments are explained in sufficient detail.

### Weaknesses
The paper is not self-contained and requires prior knowledge of prototypical networks and Gumbel-Sinkhorn layers. A reader not familiar with both topics will have to consult the references for basic definitions of key components of the proposed method (namely $L_{proto}$ and  $GS(.)$). A minimal overview of these should have been included in the main body of the paper, or at least in the appendix.

Even though the method reduces the nominal parameter complexity of the required routing network, it might still be over parametrizing the space by a log factor. Specifically, in order to define an ordering of $C$ channels one should require no more than $C$ values (each with at least $\log_2C$ bits). I suspect that one can derive a (continuous) shuffling using embeddings of size $C$ instead of $C \log C$ by using a sorting network (e.g. Bitonic sort) in a similar fashion as the Benes network is used in this work, but with a different switch type: $(U_j, channel_j)$ pairs are sorted by the key values and deltas between key values (passed a sigmoid) can form continuous switches. Can such a mechanism work in the use cases presented by the paper, and how would it compare to using the MRM-GB in terms of parametrization and evaluation speed?

### Questions
Even though the method reduces the nominal parameter complexity of the required routing network, it might still be over parametrizing the space by a log factor. Specifically, in order to define an ordering of $C$ channels one should require no more than $C$ values (each with at least $\log_2C$ bits). I suspect that one can derive a (continuous) shuffling using embeddings of size $C$ instead of $C \log C$ by using a sorting network (e.g. Bitonic sort) in a similar fashion as the Benes network is used in this work, but with a different switch type: $(U_j, channel_j)$ pairs are sorted by the key values and deltas between key values (passed a sigmoid) can form continuous switches. Can such a mechanism work in the use cases presented by the paper, and how would it compare to using the MRM-GB in terms of parametrization and evaluation speed?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper addresses the issue of meta-learning methods assuming a uniform task distribution, which hinders their performance on multi-modal task distributions. To address this, the authors introduce a new strategy for heterogeneous meta-learning that modulates the routing between convolution channels in neural networks. This strategy, called the Gumbel-Benes layer, offers a more efficient parameter complexity compared to existing methods and shows improved performance in terms of accuracy and runtime on multi-modal meta-learning benchmarks.

### Strengths
**Originality**: The paper innovatively tackles the homogeneous task distribution assumption in meta-learning by introducing a modulation mechanism between convolution channels, showcasing a fresh approach to the problem. 

**Quality**: The proposed Gumbel-Benes layer is robustly validated on multiple multi-modal meta-learning benchmarks, evidencing its effectiveness and superiority over existing methods.

**Clarity**: The presentation of the novel strategy and its underlying concepts is coherent, making the methodology and results easily understandable.

**Significance**: By addressing the limitations of previous meta-learning methods and offering a more efficient parameter complexity solution, this work holds substantial potential to influence future research and applications in the field of meta-learning.

### Weaknesses
Overall, the paper exhibits commendable novelty, particularly in utilizing meta-routing to learn task-specific activations for diverse tasks. However, I have several concerns related to the experiments:

1. What is the impact of the lambda in front of the prototype loss on the model's performance? It's unclear how sensitive the model is to this parameter, and a more thorough analysis of its effect on the final performance is needed. Specifically, what is the range of values for lambda that yields optimal performance, and how does this range vary across different datasets or tasks?
2. Did the authors experiment with adding routers only in shallow or deep layers of the network? I'm curious about the influence of routers on the model across different layers. The current presentation lacks a clear understanding of how the placement of the routing mechanism affects the model's learning capacity. It would be beneficial to see results with routers placed only in the initial layers, only in the final layers, and in different combinations to understand their impact.
3. Concerning the complexity introduced by the Router to the model, could the authors provide comparisons in terms of parameter count and training efficiency with HSML? The current comparison lacks a detailed analysis of the computational overhead introduced by the proposed routing mechanism. A comparison of the number of parameters and the training time with HSML is crucial to understand the practical implications of the proposed method.

### Questions
1. Given that $\phi(D_1)$  produces the prototype for the entire task rather than for individual classes, I'm curious: is $L_{PROTO}$'s loss computed for each class's prototype? 

2. A more in-depth theoretical analysis would undoubtedly solidify the paper further and provide a more comprehensive view.

3. It would greatly benefit readers if the authors could include an algorithm in the appendix, offering clearer insight into the paper's approach.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
