# NEAR: A Training-Free Pre-Estimator of Machine Learning Model Performance

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Artificial neural networks have been shown to be state-of-the-art machine learning models in a wide variety of applications, including natural language processing and image recognition. However, building a performant neural network is a laborious task and requires substantial computing power. Neural Architecture Search (NAS) addresses this issue by an automatic selection of the optimal network from a set of potential candidates. While many NAS methods still require training of (some) neural networks, zero-cost proxies promise to identify the optimal network without training. In this work, we propose the zero-cost proxy \textit{Network Expressivity by Activation Rank} (NEAR). It is based on the effective rank of the pre- and post-activation matrix, i.e., the values of a neural network layer before and after applying its activation function. We demonstrate the cutting-edge correlation between this network score and the model accuracy on NAS-Bench-101 and NATS-Bench-SSS/TSS. In addition, we present a simple approach to estimate the optimal layer sizes in multi-layer perceptrons. Furthermore, we show that this score can be utilized to select hyperparameters such as the activation function and the neural network weight initialization scheme.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method for identifying optimal architectures in Neural Architecture Search (NAS) using a zero-cost proxy score derived from the activation rank, without requiring separate training. To achieve this, the authors calculate both pre- and post-activation ranks and introduce a sampling method to approximate matrices for efficiency. Additionally, the paper thoroughly discusses the potential of the proposed approach using effective rank.

### Strengths
* **Applicability Across Architectures**: A key contribution of this work is that the proxy score is applicable regardless of architecture structure or activation function, providing robustness and versatility.
* **Benchmark Performance**: The authors demonstrated the method’s efficacy across standard NAS benchmarks, showing its comparative strength against other zero-cost proxies.
* **Efficiency**: By not requiring separate training, the method significantly reduces computational overhead, which is valuable for practical NAS applications.

### Weaknesses
 * **Lack of Theoretical Clarification**: While the experimental results demonstrate the effectiveness of the NEAR score, the theoretical significance of using the effective rank (erank) in Definition 3.2 remains somewhat unclear. Numerous NAS studies have previously explored concepts related to rank. It would strengthen the paper if the authors could provide a more detailed theoretical analysis comparing NEAR to existing methods, highlighting any novel insights their approach offers. Additionally, clarifying why redefining Definition 3.1 is necessary or beneficial in this context would enhance the theoretical foundation of the work. The connection between the proposed effective rank and the information capacity of the network is not sufficiently established, relying primarily on empirical correlation rather than a rigorous theoretical framework. The leap from observed correlation to a claim about information capacity requires more substantial justification.

* **Evaluation Across Layers**: It is not entirely clear whether calculating the NEAR score across all layers is necessary to achieve optimal performance. The paper does not present experiments exploring how the NEAR score changes when calculated on different subsets of layers. Conducting such experiments could provide insights into the contributions of individual layers to the overall score and discuss the implications for computational efficiency and accuracy. The claim that all layers contribute equally to the NEAR score is not adequately supported. If the NEAR score is a proxy for network capacity, one would expect that the combined score across the entire network would demonstrably outperform scores calculated from individual layers or subsets of layers. Without experimental evidence showing this, the explanation of the NEAR score remains incomplete.

* **Comparison with Few-Shot Methods**: The paper focuses on zero-shot performance but does not compare the NEAR score with few-shot methods that involve minimal training (e.g., a few epochs). As noted in "Demystifying the Neural Tangent Kernel from a Practical Perspective: Can it be trusted for Neural Architecture Search without training?" (Mok et al., 2022), it would be beneficial to conduct experiments comparing the zero-shot NEAR score to scores obtained after a few epochs of training. This comparison could substantiate the robustness of the NEAR score and reinforce the claim that it can effectively identify optimal neural networks without training.

### Questions
* **Theoretical Advantages over Existing Methods**: Could the authors provide a more detailed theoretical analysis comparing the NEAR score to existing zero-cost proxies? Specifically, what theoretical advantages does the NEAR score offer that may account for its superior performance? Highlighting any novel insights or mechanisms by which NEAR improves upon prior methods would strengthen the contribution.

* **Justification for Redefining Definition 3.1**: Since Definition 3.1 (Effective Rank) was established in previous studies, can the authors clarify why redefining it here is necessary or beneficial in the context of their method? Providing justification or modifications that are specific to their approach would help readers understand the significance of this definition in their work.

* **Layer-wise Contribution to NEAR Score**: To understand the impact of each layer on the NEAR score, could the authors conduct experiments exploring how the score changes when calculated on different subsets of layers? For instance, does excluding certain layers significantly affect the correlation with final model accuracy? Discussing these findings could provide insights into optimizing computational efficiency without compromising accuracy.

* **Stability of NEAR Score After Minimal Training**: In line with observations from Mok et al. (2022) (1), have the authors considered evaluating the stability of the NEAR score after a few epochs of training? Conducting experiments that compare the zero-shot NEAR score to scores obtained after 2-3 epochs could demonstrate the robustness of the method and whether minimal training affects its predictive capabilities.

* **Comparison with Few-Shot Performance**: How does the zero-shot NEAR score compare with few-shot methods in terms of computational cost and accuracy? Including a comparison could help position the NEAR score within the broader context of NAS methods and provide evidence for its practical advantages.

**References**
1. “Demystifying the Neural Tangent Kernel from a Practical Perspective: Can it be trusted for Neural Architecture Search without training?” (Mok et al., 2022)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Zero-cost proxies in Neural Architecture Search aim to predict the performance of neural networks on a target task without training them (hence, zero-cost). The authors point out that the current zero-cost proxies share a few common limitations. First, they show a weaker correlation with the network performance than the number of parameters, which is a naive baseline. Second, they require a pre-defined search space, which may be unclear in many machine learning applications. Third, they have only been applied for finding optimal architectures, and they cannot be used to tune or select other important hyperparameters, such as the activation function and weight initialization scheme. To overcome these limitations, the authors propose a new zero-cost proxy called NEAR (Network Expressivity by Activation Rank) that estimate the optimal layer size for MLP networks without a search space. It can also be used to tune other miscellaneous hyperparameters. The idea behind NEAR consists of two key technical contributions 1) relaxing the definition of the activation patterns to encompass non-ReLU activation functions and 2) utilizing the effective rank of pre- and post-activation matrices to compute the NEAR score. The effectiveness of NEAR is verified empirically through experiments on several NAS benchmarks.

### Strengths
- The authors propose a novel zero-cost proxy score that can be utilized to predict not only the optimal architecture of the neural network but also the optimal set of hyperparameters, such as the weight initialization scheme and activation functions. 

- The proposed network utilizes the effective rank of pre- and post-activation matrices to predict the final performance of a neural network, which appears to be theoretically sound. Such an approach, however, has been used in previous literature, as noted by the authors in lines 152-154. Therefore, the main technical contribution of NEAR is relaxing the definition of the activation patterns to include various activation functions.

- The authors present sufficient empirical evidence to show the effectiveness of the proposed approach from three main perspectives: 1) high rank correlation on NAS benchmarks, 2) optimal layer size estimation, and 3) activation function and weight initialization selection.

### Weaknesses
 - Since the proposed method can be used to predict the performance of non-ReLU-based architectures, it can theoretically be applied to predict the performance of LLMs with GELU activations. Have the authors attempted this? It would be a strong extension of the proposed method especially since the authors argue that the major advantage of the proposed method is its applicability to tasks that do not have a fixed search space.

- The authors argue that this method enables estimation of optimal weight initialization and activation function, but it was not clear after reading the paper why other zero-cost proxies cannot be used for this purpose. It seems that although previous metrics did not explicitly take weight initialization or activation function into consideration, they can theoretically be used for the same purpose. Therefore, it would be helpful if the authors could add a comparison with previous approaches in Tables 7 and 8 to better highlight that only NEAR score can do this.

- I didn't quite follow how relaxing the definition of activation patterns affects the definition of the NEAR score. If the definition isn't relaxed and is constrained only to ReLU activations, how would the NEAR score be formulated? Or would it be impossible to formulate this score in the first place? If there is no difference between the two (theoretically speaking), why did this definition have to be relaxed? Does the NEAR score before and after relaxing this definition show lower/higher correlation with performance? Because this is unclear, I didn't understand how the NEAR is designed to serve all of its intended purposes, such as choosing the optimal number of layers, weight initialization, and activation function.

- In Tables 1-3, The NEAR score only outperforms other metrics only on NAS-Bench-101 and NATS-Bench-SSS (CIFAR-100). Tables 5-8 do not compare the NEAR score against previous approaches. This makes me question whether the NEAR score is as reliable as the authors claim. I would like to see at least one application in which the NEAR score is clearly far more advantageous than other metrics.

In general, the authors make very strong arguments about the theoretical novelty of the proposed proxy and its usability. However, because of the points stated above, I did not find the current manuscript convincing enough. After reading this paper, I am left wondering in what exact practical application the NEAR score would actually be more useful than previous proxies. If the authors can explicate both theoretically and empirically that the NEAR score does indeed have distinct advantages, I would be willing to adjust my score.

### Questions
Please refer to the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces NEAR (Network Expressivity by Activation Rank), a zero-cost proxy (ZCP) that estimates the rank of neural network architectures via the effective rank of pre- and post-activation matrices at initialization (without training). The method is quite generic and is agnostic to the type of activation function or labelled data. Experiments on benchmarks such NAS-Bench-101 and NATS-Bench demonstrate NEAR’s high correlation with model accuracy, often outperforming other proxies.

### Strengths
I think the direction of using the effective matrix rank as a zero-cost proxy (ZCP) for neural net accuracy is a useful idea and worth pursuing. Some of the results are interesting and the NEAR proxy seems to filter out architectures that perform worst and does provide somehow reliable information on which architectures are in the top 10% best performing ones.

### Weaknesses
Despite the aforementioned positives, I have the following major concerns related to this submission:

- The differences in test loss in Table 7 are not statistically significant and it seems to me that even for these small networks the NEAR score can't determine correctly the ranking of the models. Furthermore, there are only a few tasks and datasets considered for this evaluation, and despite NEAR being able to filter out the bad architectures, typically one is interested in finding the best architecture among the top 10% of architectures in the search space, which this is clearly not the case from the results in Table 8. The lack of statistical significance in Table 7 raises concerns about the robustness of the method, especially given the small scale of the networks being tested. The fact that NEAR struggles to accurately rank models even within this limited scope suggests that its predictive power may be weak, particularly when the goal is to identify top-performing architectures.

- I think that the usage of the standard image classification benchmarks in NAS such as NATS-Bench or NAS-Bench-101, as in this paper, poses the risk of overfitting new proposed methods on these benchmarks. For instance, I would recommend the authors running their method on benchmarks of NAS-Bench-Suite-Zero [1]. The reliance on well-trodden benchmarks like NATS-Bench and NAS-Bench-101 introduces a potential for overfitting the proxy itself to the specific characteristics of these datasets. This could lead to inflated performance metrics that do not generalize to other, more diverse tasks. Evaluating on NAS-Bench-Suite-Zero [1], which includes a wider range of tasks and search spaces, would provide a more rigorous assessment of the method's generalizability.

- The contributions of the proposed approach are marginal regarding novelty, and despite I find the idea behind using effective rank useful, I still do not fully understand how it can be used to determine effective training and generalization of neural nets at initialization. Can the authors comment on this point further (see questions below as well)? The application of effective rank to neural network analysis at initialization, while interesting, lacks a clear theoretical grounding that connects it to the generalization capabilities of the network. The paper does not provide a convincing explanation of why the effective rank of pre- and post-activation matrices should correlate with the network's ability to train effectively and generalize to unseen data. This theoretical gap weakens the contribution of the proposed method.

- In terms of significance, I do believe that the zero-cost proxy research could be beneficial to the community if it is rephrased in the current landscape of LLM compression [2]. I do find the standard NAS benchmarks useful for prototyping accuracy proxies, however I do not see anymore the practical relevance of these benchmarks outside prototyping and fast experimentation. This is my personal opinion though and my recommendation would be to think of ways how ZCP research on CNN models could be rephrased to structural pruning of LLMs (actually the ZCPs were inspired from network pruning methods in the first place).

- Finally, I think the paper could be made easier to read and gain more clarity with less text and a few more figures summarizing some of the main results described in the text.

### Questions
- What is the cost of computing NEAR and how does it compare to the cost of computing the other ZCPs?

- Can the authors comment on the relationship between their findings on the optimal initializaiton scheme and activation functions, and the maximal update parameterization (muP) [1], which enables effective transfer of hyperaparameters across model scales?

- As the efficiency of transformer-based models is becoming more and more relevant as their capacity keeps growing, I would suggest the authors assess the performance of their proxy method on approximating the rank of pruned transformer models. Could the authors evaluate their method on the recent HW-GPT-Bench [2]?

- Do the authors have any more theoretical justification of the effective matrix rank and its ability to assess the neural network generalization, trainability and expressivity at initialization? Is the effective rank of the pre- and post-activation matrices somehow related to the number of linear separable regions in TE-NAS [3]?

-- References --

[1] Yang et al. Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer. 2022

[2] Sukthanker et al. HW-GPT-Bench: Hardware-Aware Architecture Benchmark for Language Models. In NeurIPS 2024 DBT

[3] Chen et al. Neural Architecture Search on ImageNet in Four GPU Hours: A Theoretically Inspired Perspective. In ICLR 2021

### Soundness
2

### Presentation
2

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
NEAR is a zero-cost proxy that predicts machine learning model performance without training by estimating neural network expressivity through the effective rank of activation matrices. It demonstrates a strong correlation with final model accuracy on NATS-Bench and NAS-Bench-101, ranking first among 13 zero-cost proxies. NEAR requires only input data, not labels, and works with any activation function. It also helps select optimal activation functions, weight initializations, and layer sizes in multi-layer perceptrons.

### Strengths
The paper attempts to address a well-established and critical problem of correctly predicting the accuracies of different model architectures using zero-cost proxies.

Applies a good intuition of using ranks of pre and post-activation matrices as indicators of accuracy. 

Novel analysis of weight initialization and activation functions.

Comprehensive comparison with existing state-of-the-art on relevant benchmarks.

### Weaknesses
Although the authors show good performance of their techniques across benchmarks, it is not clear if the metrics used to determine the model performance compare different architectures correctly. For example, given two model architectures A1 and A2 with test accuracy of A1 being greater than A2,  how often is the case where the rank of pre and post-matrices of A1 greater than A2?

How well does this generalize to larger models and more complex datasets?

For convolution operations, there are many hyperparameters like kernel size, stride, dilation, in-channels, out-channels, grouped convolutions, etc. How does the flattening of these matrices and calculating the score take into account all of the above factors? The intuition in this case is unclear.



### Questions
In the case of using ranks of pre and post-activation matrices as indicators of accuracy, a study that verifies this claim would be helpful. The same goes for the convolution part.

Specifically for the convolution part how accurate is the predicted rank using sampling? What is the minimum sample size required?

For the results, in cases where the estimations are off, why does that happen? A post-analysis would provide some insights into cases where NEAR is not optimal

It has been shown in the literature that randomly generated matrices in high dimensions contain almost linearly independent vectors, how does this impact the prediction if we only derive the rank hypothesis only from a few input samples?

### Soundness
3

### Presentation
3

### Contribution
3
