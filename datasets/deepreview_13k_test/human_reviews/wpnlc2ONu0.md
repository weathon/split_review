# Adaptive deep spiking neural network with global-local learning via balanced excitatory and inhibitory mechanism

- Decision: Accept
- Scores: 5, 8, 8, 5

## Abstract
The training method of Spiking Neural Networks (SNNs) is an essential problem, and how to integrate local and global learning is a worthy research interest. However, the current integration methods do not consider the network conditions suitable for local and global learning, and thus fail to balance their advantages. In this paper, we propose an Excitation-Inhibition Mechanism-assisted Hybrid Learning(EIHL) algorithm that adjusts the network connectivity by using the excitation-inhibition mechanism and then switches between local and global learning according to the network connectivity. The experimental results on CIFAR10/100 and DVS-CIFAR10 demonstrate that the EIHL not only has better accuracy performance than other methods but also has excellent sparsity advantage. Especially, the Spiking VGG11 is trained by EIHL, STBP, and STDP on DVS_CIFAR10, respectively. The accuracy of the Spiking VGG11 model on EIHL is 62.45%, which is 4.35% higher than STBP and 11.40% higher than STDP, and the sparsity is 18.74%, which is 18.74% higher than the other two methods. Moreover, the excitation-inhibition mechanism used in our method also offers a new perspective on the field of SNN learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed an Excitation-Inhibition Mechanism-assisted Hybrid Learning (EIHL) algorithm for training Spiking Neural Networks (SNNs), a learning algorithm that hybrid local learning rule and global learning rule. 
Experiments on CIFAR10/100 and DVS-CIFAR10 showed that EIHL outperforms other methods in terms of accuracy and sparsity.

### Strengths
1. Fusion of Global and Local Learning Rules: According to the authors, the integration of both global and local learning paradigms could potentially pave the way for attaining enhanced performance and energy efficiency in neural networks.

2. Performance on CIFAR Benchmark: The authors successfully demonstrated an improvement in performance on the CIFAR dataset when compared to the traditional backpropagation technique.

### Weaknesses
1. The authors should elucidate their contributions more explicitly in order to provide a comprehensive understanding of the research.

2. In the context of hybrid learning, 'STDP' process employs a contraction curve to facilitate Long-Term Depression. Nevertheless, the authors have not adequately expounded upon the association between LTD and STDP, and the proposed method do not have a dependence of the spike timing. It's not clear why excitation should be like STBP and depression should be like STDP.

3. The accuracy of references should be ensured. For example, the paper states, "Spike-Timing Dependent Plasticity (STDP) was proposed based on these rules by Caporale & Dan (2008)." However, the discovery of STDP predates 2008. Caporale & Dan (2008) is a review paper.

### Questions
1. In the context of the hybrid learning rule, what is the significance of excitatory and inhibitory synapses, given that STDP and STBP do not appear to rely on the distinction between these synapse types? Furthermore, it seems that excitatory and inhibitory synapses are not typically delineated in deep spiking neural networks.

2. Weight pruning is a technique employed in deep learning to increase network sparsity by eliminating the smallest weights. Please elucidate the distinctions between the 'STDP' process in EIHL and weight pruning techniques in deep learning.

3. Kindly review the terminology and references utilized in the manuscript to ensure a more precise and coherent presentation of the research study.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an Excitation-Inhibition Mechanism assisted hybrid Learning (EIHL) algorithm. Inspired by the biological neural excitation-inhibition mechanism, it achieves adaptive adjustment of spiking neural network connectivity, and automatically alternates between global and local learning according to the growth or decay of synaptic strength which depends on the excitation-inhibition mechanism. It also conducts three experiments to demonstrate that this method has higher accuracy than global learning, and higher sparsity than local learning.

### Strengths
This paper proposes a new hybrid method of local and global learning, which is regulated by the biological neural excitation-inhibition mechanism. The paper also argues that the excitation-inhibition mechanism leads to sparse results for neural networks, which is an innovative perspective. Moreover, the language and logic of the introduction and method description are clear and smooth. Finally, the paper presents EIHL as a new point in the field of SNN training methods, and also provides new insights for ANN training methods, which has some significance.

### Weaknesses
The paper conducted three experiments to verify the performance advantages of the method, but the details of the third experiment are less described. The third experiment should specify which layer or the whole network is randomly pruned at different levels, and also explain the specific operation of random pruning.

### Questions
I would like to ask the author, is the random pruning at different levels applied to the whole network or to a specific layer? And will the synapses that are randomly cut off at the beginning be restored in the later learning or remain disconnected? Maybe it should be explained in the third experiment.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a hybrid learning method that uses the neural excitation and inhibition mechanism to assist local learning and global learning (called EIHL), by simulating the biological neural excitation and inhibition mechanism to adjust the network connection state, thus integrating local learning and global learning. The experimental results also show that this method has advantages in accuracy and sparsity compared to separate local learning and global learning.

### Strengths
This paper is inspired by the biological neural excitation-inhibition mechanism and proposes a new hybrid learning method for SNN, which is more brain-like than previous methods and has originality. Moreover, this paper has some practical significance from both the biological perspective and the accuracy and sparsity of the experimental results. Furthermore, the whole paper is logically coherent and fluent, and the language is concise and clear.

### Weaknesses
The Fig.1 in this paper that explains the EIHL algorithm is too simple and not detailed enough, only showing the connection processing between the convolutional layer and the IF neuron layer. This figure could consider adding another layer to show the specific operation of the algorithm more finely.

### Questions
Is the EIHL method only applied to the convolutional layer? If not, I hope it can be reflected in the figure. I suggest updating and optimizing Fig.1.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes the Excitation-Inhibition Mechanism-assisted Hybrid Learning (EIHL) algorithm for training spiking neural networks. The algorithm combines the global learning and local learning together, and achieves better results than individual learning rules, as demonstrated through the experiments.

### Strengths
The method is inspired by biological mechanisms. Researchers in the SNN community should be encouraged to seek inspiration from neuroscience.

### Weaknesses
1.The authors do not provide a clear and comprehensive description of their method in section 4. The review raises several concerns, outlined as follows:

 (i). What does the notation $x$ mean? Is it a global parameter for the entire network? How does it "gradually increase" during the STDP period and "decay by itself" during the STBP period?

 (ii). What is the precise formula for the operation $thresh(\cdot)$? It appears that $b$ remains unchanged during the STDP period based on Alg. 1. Does this imply that $thresh(b)$ remains constant in each STDP period?

 (iii). Could the authors provide further elaboration on Eq. 7? Why is gradient descent necessary for updating the weight in the STDP period? How is dL/dx computed, given that L does not seem to be differentiable with respect to x? Also, why do x and W share the same dimension? The reviewer thinks that it should be a scalar. Additionally, why is the "contraction factor" $a$ needed?

 (iv). Regarding alg. 1, how is the "current sparsity" calculated? Why is "Curr S >= Pre S" required in the algorithm?


2.The contribution of this work is not very clear at the current stage. In the reviewer's understanding, this work aims at improving the current hybrid learning algorithms which "have some theoretical and practical shortcomings and need further improvement". However, there is no theoretical (mathematical) results in the paper and the biological plausibility of the proposed hybrid method is not inadequately clarified. Furthermore, the practical preformance is relatively unsatisfactory: 

(i). The improvement based on the global learning rule STBP is minimal. In essence, STBP represents a special case of the proposed EIHL with specifically chosen hyperparameters. Consequently, EIHL can consistently yield slightly superior results to STBP through randomness and careful hyperparameter tuning.

(ii). The performance notably lags behind the latest research. Especially, the SOTA results of DVS_CIFAR10 is 20% better than the proposed method.

(iii). There is no comparison between this work and other hybrid methods regarding accuracy and biological plausibility.

(iv). No experiments on large-scale datasets.

In summary, the motivation and contribution of the paper remain ambiguous. The reviewer perceives this work as merely a combination of two exsiting methods without convincing reasons. 

3.This paper is not well-written. Several sentences lack coherence, making the overall presentation disjointed. The presentation of equations is arbitrary and non-standard. The resolution of Fig. 1 is low.

### Questions
Could the authors provide a more comprehensive explanation of the excitation-inhibition mechanism and how it is used in this work? Although the authors keep mentioning it, the reviewer cannot understand how excitatory and inhibitory synapses are handled differently and how they are balanced.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
