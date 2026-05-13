# Wasserstein Distances, Neuronal Entanglement, and Sparsity

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Disentangling polysemantic neurons is at the core of many current approaches to interpretability of large language models. Here we attempt to study how disentanglement can be used to understand performance, in particular under weight sparsity, one of today's leading post-training optimization techniques. We suggest a novel measure for estimating neuronal entanglement: the Wasserstein distance of a neuron’s output distribution to a Gaussian. Moreover, we show the existence of a small number of highly entangled "Wasserstein Neurons" in each linear layer of an LLM, characterized by their highly non-Gaussian output distributions and their significant impact on model accuracy. To study this phenomena, we propose a new experimental framework for disentangling polysemantic neurons. Our framework separates each layer’s inputs to create a mixture of experts where each neuron's output is computed by a mixture of neurons of lower Wasserstein distance, each better at maintaining accuracy when sparsified without retraining. We provide strong evidence that this is because the mixture of sparse experts is effectively disentangling the input-output relationship of every individual neuron, in particular the difficult Wasserstein neurons.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes using the Wasserstein distance to select entangled neurons. The authors use the mapping difficulty to measure the entanglement and argue that the Wasserstein distance is strongly correlated with it. They further introduce a sparse expansion method that disentangle the Wasserstein neurons better.

### Strengths
- Understanding the relationship between sparsity and entanglement is an important research area.
- The paper conducts extensive experiments to explore the connection between Wasserstein distance, entanglement, and their impact on sparsification.

### Weaknesses
 - The concept of using the Wasserstein distance has been addressed in prior work [1]. The authors could benefit from a broader literature review. It would be helpful to discuss how other works evaluate entanglement, particularly those that focus on disentangling representations rather than directly pruning neurons. The current approach seems to focus on the effect of pruning on individual neurons, while other methods may focus on the overall representation.
- The sparse expansion approach relies on prior knowledge of the distribution to support K-means clustering. How robust is this method for out-of-distribution data? Specifically, the reliance on a single training set for clustering may limit the generalizability of the learned experts. The paper should discuss the potential for performance degradation when the input data distribution shifts significantly from the training distribution.
- Practical aspects of the sparse expansion, such as runtime and inference speed (e.g., with 16 experts), should be discussed more thoroughly. The paper needs to quantify the computational overhead introduced by the routing mechanism and the multiple experts, especially in comparison to standard sparse linear layers. A detailed analysis of the trade-offs between model performance and computational cost is necessary.
- The writing could be improved; The reviewer finds that many phrases and sentences are difficult to parse.

### Questions
1. Directly normalizing the distribution to calculate the Wasserstein distance seems like a strong simplification. Is there a better approach that accounts for mean and variance?
2. In Equation (2), why is the mean used for mapping difficulty, the maximum for $N_x$ , and the median for $N_y$?
3. In Figure 4b, what does the "normalized input/output L2" represent?
4. On line 282, there is a missing word after “the.”
5. How is the weighted cluster distance calculated in Figure 6b?
6. Are the K-NN and evaluation conducted on the same training set of wikitext-2?
7. Could the authors explain why there is no correlation between the optimal number of Gaussians and relative improvement? Is this due to sparse expansion being applied directly to the weight matrix while the GMM is estimated for individual neurons? Is the relative improvement possibly influenced by the neurons with the largest GMM value? Could differences in measurement — one on the entire weight matrix, the other on individual neurons — lead to inconsistencies?
8. How do outlier weights (or neurons) overlap with neurons that have large Wasserstein distances?
9. How do neurons in the MoE model perform in terms of Wasserstein distance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper examines the performance of models under weight sparsity by considering the entanglement of the neurons in the dense model. The authors first empirically show that neurons with high Wasserstein distance (WD) to a Gaussian distribution will more negatively impact the model's performance when sparsified. They then demonstrate that the WD metric has positive correlation with the Mapping Difficulty (MD) of each neuron, which serves as a heuristic for measuring neuron entanglement.

Motivated by this observation, the authors propose an algorithm (Sparse Expansion - SE) that adjusts the SparseGPT (Frantar & Alistarh, 2023) algorithm for making the model sparse: For each layer, they learn $k$ sparse weights (experts), corresponding to $k$ clusters of input data, by the SparseGPT algorithm. The clusters at each layer are identified by $k$-means clustering on the low-dimensional representations derived from PCA on the original inputs. Then, during inference, each input is routed through the closest clusters. The paper claims that each cluster will help disentangle the neurons, leading to a decrease in WD in the sparse model. Finally, they show that the sparse models learned by SE have improved performance, as measured by perplexity.

### Strengths
I am not fully familiar with the literature on neural disentanglement and the interpretability results. However, I find the paper’s approach to improving the performance of sparsified models by analyzing neuron interpretations interesting.

The authors take a step-by-step approach to justify their claims/arguments and to make connections between the different concepts discussed in the paper.

### Weaknesses
I find that many of the arguments in the paper are either based on intuition or established by showing correlations between metrics. In some cases, it is not very clear to me whether there is some sort of causation also involved. For example,  I don't understand why a neuron with a smaller WD to Gaussian should be less entangled (and thus more interpretable?). In the paper, this conclusion relies on the correlation between WD and MD, which is itself an intuitive metric for measuring entanglement. Nevertheless, the arguments are still motivating for further research in this direction.

I think the flow of the paper can be slightly improved: For example, in section 2, Wasserstein neurons and entangled neurons are used interchangeably before properly establishing their connection in section 2.3. This was a bit confusing on the first read, requiring some back and forth through the sections to clarify their connections.

(Minor) The paper's generally well-written, but it would benefit from a revision as there are several typos throughout the paper.

### Questions
1.  On the Sparse Expansion (SE) algorithm:
    - How is the number of clusters $k$ chosen? From Figure A2, it seems that increasing $k$ consistently improves performance (in terms of perplexity). Besides increased memory usage, are there other performance trade-offs when increasing $k$?
    - If the clustering approach mainly addresses the issue with the entangled neurons, do all neurons need the same number of clusters? 
    - How much optimization/run-time overhead does the PCA+$k$-means step add to the sparseGPT algorithm when sparsifying the weights? 
2.  Since the link between entanglement and Wasserstein neurons is made through the MD metric, I am wondering if we see MD also decreases by the Sparse Expansion algorithm.
3. Shouldn't the clusters learned through the SE algorithm depend on the structure of the data/task used for this purpose? For example, in Figure 10, is SE both performed and validated on Wikitext2? If so, would the sparse model still have improved performance on other downstream tasks/datasets (like the ones evaluated in Figure 2)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose to compute the distance between the output distribution of a neuron in a neural network and a gaussian using Wasserstein distance as a measure of entanglement, i.e. a neuron could be highly polysemantic and thus entangled. It’s shown that some of the neurons in LLMs are highly entangled under the Wasserstein distance metric and sparsifying them leads to significant performance degradation compared to sparsifying random neurons. The authors propose sparse expansion by separating the input vectors and creating a mixture of neurons with low Wasserstein distance. The proposed sparse expansion methods outperform all other baselines under sparsity / pruning.

### Strengths
The proposed sparse expansion seems to outperform SparseGPT and all other baselines, though I’m not in this subfield and I don’t know what are the strong and weak baselines here.

### Weaknesses
 - It’s very unclear what do you mean by the gaussian output distribution of a single neuron. For example, the introduction section says that a column of a weight matrix is a neuron. Here it’s unclear what’s the matmul operation between input and weights. Is it right or left multiply? Are you saying that the output scalar $y=\mathbf{w}^\top \mathbf{x}$ is a sample from the gaussian distribution? As a reader I have to read between the lines to figure out what’s the proper definition. Please write down the precise mathematical quantity.
- There is a confounding factor here regarding the idea of highly entangled neurons. If I understand properly, the output distribution of a neuron at initialization is basically a gaussian. This is because the weights are gaussian initialized unless otherwise specified. Then perhaps highly entangled neurons are basically neurons with proper feature learning, i.e. enough gradient updates, and neurons with low wasserstein distance to a gaussian could just be a neuron that didn’t receive enough gradient update. This is especially true when you consider LLMs under width scaling, as some of the parameters might not be learned properly. See https://arxiv.org/abs/2203.03466. Then it might not make sense to prune out or sparse highly entangled neurons since they could actually be the useful neurons or neurons with proper feature learning. Would like to hear what the authors think about this.

### Questions
See weaknesses

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, the relevance of individual neurons in LLMs is estimated by comparing their normalized output distribution before the activation function to a Gaussian using the Wasserstein distance measure. 
They find that the output of a small group of neurons deviates significantly from the gaussian distribution, and that these neurons contribute significantly to the model's performance. They define that a neuron is particularly entangled when it has to produce different outputs for similar inputs. They find that neurons that deviate from a gaussian distribution are particularly entangled.
They provide a framework that disentangles the neurons to some extent, that is, they reduce the Wasserstein distance measure. Using this framework, they obtain a lower loss on Wikitext-2 compared to other techniques when creating a sparsified model.

### Strengths
1) The relevance of individual neurons is studied in detail, which is interesting from a technical point of view when reducing the model size, but also points to areas that explainable AI researchers should look for.

2) A potential application in terms of model reduction is provided.

### Weaknesses
1) The exact sparsification algorithm used to generate Figure 2 is not given in the manuscript.

2) There are some problems with the Figures: Figures 1, 3, and 7 lack x and y labels.
In Figure 10, the caption does not match what is shown in the figure.

3) The description of the sparsification method in the questions section is not detailed enough. It is unclear how the 95% of weights are chosen, and what is the impact of this choice on the model's performance. It is also unclear if the 3% of neurons are chosen randomly, or based on some criteria, and if so, what is this criteria.

Line 422 typo: "the the"
Line 428 typo: "as" -> has

### Questions
1) The way I understand your sparsification algorithm in Figure 2 is this: For 3% of the neurons, you set 95% of the weights going into them to zero. Is this correct? And if so, how do you choose these weights? 

2) Figure 10: Which model is used? The caption speaks of many, but the figure shows only one, as far as I understand it. 

Line 422 typo: "the the"
Line 428 typo: "as" -> has

### Soundness
4

### Presentation
2

### Contribution
3
