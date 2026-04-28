# Domain Generalization Deep Graph Transformation

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Graph transformation that predicts graph transition from one mode to another is an important and common problem. Despite much progress in developing advanced graph transformation techniques in recent years, the fundamental assumption typically required in machine-learning models that the testing and training data preserve the same distribution does not always hold. As a result, domain generalization graph transformation that predicts graphs not available in the training data is under-explored, with multiple key challenges to be addressed including (1) the extreme space complexity when training on all input-output mode combinations, (2) difference of graph topologies between the input and the output modes, and (3) how to generalize the model to (unseen) target domains that are not in the training data. To fill the gap, we propose a multi-input, multi-output, hypernetwork-based graph neural network (MultiHyperGNN) that employs a encoder and a decoder to encode topologies of both input and output modes and semi-supervised link prediction to enhance the graph transformation task. Instead of training on all mode combinations, MultiHyperGNN preserves a constant space complexity with the encoder and the decoder produced by two novel hypernetworks. Comprehensive experiments show that MultiHyperGNN has a superior performance than competing models in both prediction and domain generalization tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel approach to graph transformation, specifically focusing on domain generalization. Traditional graph transformation techniques often assume that testing and training data have the same distribution, which is not always the case. The authors address challenges like space complexity, differences in graph topologies, and generalizing to unseen domains. They propose a multi-input, multi-output, hypernetwork-based graph neural network (MultiHyperGNN) that uses an encoder and a decoder to handle both input and output modes. The model also incorporates semi-supervised link prediction to enhance the transformation task. Experiments demonstrate that MultiHyperGNN outperforms competing models in prediction and domain generalization tasks.

### Strengths
- Originality: The paper addresses the under-explored area of domain generalization in graph transformation. And introduce MultiHyperGNN, a multi-input, multi-output hypernetwork-based GNN.
- Quality: The proposed model effectively tackles the challenges of space complexity, varying graph topologies, and generalization to unseen domains. And comprehensive experiments validate the effectiveness of MultiHyperGNN.
- Clarity: The paper is well-structured, with a clear presentation of the problem, challenges, and the proposed solution.
Significance:

The work has potential implications for various applications where domain generalization is crucial, enhancing the robustness and applicability of graph transformation models.

### Weaknesses
1.  The introduction part seems to be incomplete. In the third paragraph, the three challenges of the problem are emphasized. The fourth paragraph should focus on writing the core idea of ​​solving these challenges in this work.
However, the authors only wrote about their implementation, so I did not understand the innovative ideas of this work from a high-level perspective.
2.  The paper does not adding ablation studies to understand the contribution of each component of MultiHyperGNN. 
3.  While the challenges are listed, a more in-depth discussion on how each challenge is specifically addressed by MultiHyperGNN would enhance understanding.

### Questions
1.  How do the proposed hypernetworks differ from existing ones in terms of architecture and functionality?
2.  Consider adding ablation studies to understand the contribution of each component of MultiHyperGNN.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article addresses the graph transition problem. And the authors introduce the MultiHyperGNN model, which reduces complexity and enhances model generalization as well. The experimental results on real-world datasets demonstrate the effectiveness and efficiency of the proposed framework. Overall, the paper is a bit hard to understand.

### Strengths
1. Solving the graph transformation problem is novel.

2. The experimental results are extensive, covering a wide range of datasets.

### Weaknesses
1.	It is unclear about the practical use case of the proposed model, and hard to understand the problem setups. Can you elaborate on the potential real-world applications in which you proposed domain transformation problem can be applied? 

2.	It would be beneficial for the authors to explain why traditional methods require O(3^N) to solve the problem. Additionally, is it possible that the traditional method, despite its time-consuming nature, performs the best and can serve as a baseline? 

3.	In the experiments on climate dataset (e.g., table 1 and 2), why does HyperGNN use late-night data while MultiGNN uses morning data? Is it a fair comparison?

4.	In the ablation studies, the authors compare with HyperGNN-1 and HyperGNN-2, but do not compare with MultiHyperGNN-1 or MultiHyperGNN-2. I noticed that HyperGNN contains only one decoder, and its structure does not align with the proposed MultiHyperGNN model. Could you please clarify this choice？

5.	In Section 4.3, the definition of meta-information is very strict. It is necessary to discuss how meta-information in the datasets in experiments can satisfy the condition in the definition of meta-information. The authors mentioned that “An ample amount of meta-information will result in reduced generalization error”, but it is unclear of how to measure the “ample amount”, which makes the conclusion too vague.

6.	The notation are overly complex and contain some errors, which hinders readability. For example, in Figure 2, encoder should be represented as f^{(2)}_e. The distinction between \widetilde{A} and \hat{A} in Equations 8 and 9 should be clarified. Moreover, Figure 2 is unclear to me. Whether the decoder's input is a graph or the latent embedding obtained by the encoder, as shown in Equation 11. Why there are two layers of decoder f^{(1)}_d.

### Questions
see weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel framework, MultiHyperGNN, designed to address challenges in graph transformation, particularly in predicting transitions of graphs across various modes (such as gene expression networks) and generalizing to unseen domains. The primary challenges identified are the high complexity of training on all input-output mode combinations, the difficulty in transforming graphs with differing topologies, and the need to predict graphs in unseen target domains.

MultiHyperGNN introduces a multi-input, multi-output strategy utilizing hypernetworks to generate encoders and decoders, facilitating domain generalization. This approach dramatically reduces space complexity and enables the model to adapt to varying topologies and unseen domains. The framework includes semi-supervised link prediction to enhance output graph completion. Extensive experiments on three real-world datasets demonstrate that MultiHyperGNN outperforms existing models in both prediction accuracy and domain generalization.

--------------------- after reading the authors' comments/rebuttal------------------------------------------
I thank the authors for providing explanations to my questions and answering them satisfactorily. In particular, my concerns regarding the hyperparameter were sufficiently addressed by the experiments the authors conducted by changing the weight on the reconstruction loss for semi-supervised link prediction. 

However, I would like to point out two things when the authors were addressing my concerns on the scalability issue. First, it is sufficiently demonstrated that given the largest graph sizes that the model is trained on, scalability doesn't pose any challenges, but my point was to ask if, for even larger graphs, the model is scalable. Second, it is true that the scalability issue is faced by the papers that the authors provided, but the argument "because the field couldn't do it" is not as strong. Nonetheless, I concur that scalability is indeed a difficult topic faced by works about/on graph transformation, and the paper shouldn't be judged unfavorably solely because of it.

The authors argued that meta information is crucial to the domain generalizability and explained in Theorems 1 and 2 to demonstrate the importance that the meta information captures relationships among different domains. The significant improvement over HyperGNN-2 demonstrates the importance of the meta information. However, it's always worth-wondering on the fairness of comparison against approaches to whom meta information (or its variation) is not available. Nonetheless, I do view this as a negative trait of the work as the authors have demonstrated the importance of meta information in their experiment settings.

In summary, I believe this paper demonstrates novelty and valuable info for it to be considered to be accepted. However, when I first reviewed the paper and got to know the strengths and weaknesses of it, I thought the weaknesses are not significant enough to eclipse the strengths. The authors' response addressed some of my concerns. I will maintain my original rating for this paper: marginally above the acceptance threshold

### Strengths
+ The multi-input, multi-output hypernetwork-based framework is a novel contribution, particularly in reducing training complexity and addressing domain generalization.
+ Successfully reducing space complexity from exponential to constant during training is a significant advancement, making the model more practical for large-scale applications.
+ The ability to generalize to unseen target domains is a crucial advancement in graph transformation tasks.

### Weaknesses
 - While space complexity is addressed, the overall computational complexity and potential overfitting risks due to the complex model structure are not discussed in detail.
- The use of hypernetworks might introduce sensitivity to hyperparameters, but this aspect isn’t thoroughly explored.
- The extent to which the model can generalize to radically different unseen domains is not clearly defined.
- It’s unclear how well the model scales to extremely large graphs or how transferable it is across significantly different domains.

### Questions
- Can you elaborate on the computational efficiency of MultiHyperGNN, especially when dealing with very large graphs?
- How does the model handle the risk of overfitting, given its complexity?
- Could you discuss any limitations or boundaries in the model's ability to generalize across radically different domains?
- Could you discuss any limitations or boundaries in the model's ability to generalize across radically different domains?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The presented work proposes a novel model that learns to solve graph transformation problem under a domain generalization setting.

### Strengths
- The superiority of the proposed framework is clearly stated and tested through experiments.
- The proposed model targets on domain generalization, which is a major problem in graph representation learning.
- The use of hypernetworks in graph transformation is novel, as far as I know.
-----
after reading the author responce, I decide to keep my current rating to this paper unchanged.

### Weaknesses
 - I find this paper vague in some places with its wording. See Questions.
- I don't quite understand what is the essence of the optimization of space complexity in this model. The authors claim that, if we traverse all possible combinations of input and output pairs it will require $\Omega(3^N)$ time (BTW the paper uses the asymptotic notation $O$, but actually should be $\Omega$ here), which is true, but usually you don't require to traverse all possible input-output pairs to learn a not-bad model, just like in ordinary supervised classification, the model doesn't need to travers all possible samples from the ditribuition but just a finite subset of them (the training set). In my understanding, the presented paper basically asumed there is a distribution of meta information and the training of the proposed model will require meta information as input. However, if there is indeed an underlying distribution of meta information, then just simply sampling some pairs from all the $\Omega(3^N)$ possible combination might also work well. That's why I don't quite understand the necessity of using this multi-input, multi-output, hypernetwork-based framework here. It is possible that my understanding is wrong. If so feel free to point it out.
- I don't understand why the authors claim the space complexity of the propsed model is constant. Based on Algorithm 1, the output size  is linear in the size of $\mathcal Y$ and $n$.
- In Theorem 1, it makes no sense to me to assume the genralization error to be iid Gaussian (as the notation is quite confusing here, I don't actually know what does the authors mean here, but I guess it means iid Gaussian. Please correct me if my understanding is wrong). According to Definition 3, the error comes from $X_i ^{(k)} - f_{\hat \gamma_{\mathcal X\to \mathcal Y}}(\cdots)$, and as $f_{\hat \gamma_{\mathcal X\to \mathcal Y}}$ is based on GNNs, there should be inter-node interactions. It is very unlikely ${\boldsymbol{\epsilon}}_i$ can be iid.

### Questions
- In Section 3, there's a sentence "where $A^{(j)} \in \mathbb R^{p_j \times p_j}$ is the graph of size $p_j \leq p$". Do you mean $A^{(j)}$ is the **adjancency** of a graph? Also, sincein the definition $A^{(j)} \in \mathbb R^{p_j \times p_j}$, do you mean the entries of $A^{(j)}$ can be take any real numbers, even negative numbers?  
- In Definition 1, what does "s.t. $\mathcal X^{\mathcal  T} \times \mathcal Y^{\mathcal T} \not \in \mathcal S$" mean?  Does that mean, say $\mathcal X^{\mathcal T}$ contains modes that are not in $\mathcal G$?
- In equation (1), what is $\beta_d^{(k)}$? What is the dimensioanlity of $\hat X_i^{(k)}$? 
- In the definition of $f_{\gamma_{\mathcal X \to \mathcal Y}} = \left\\{f_d^{(k)} \star \left\\{f_e^{(j)}\right\\}\_{j \in \mathcal X}\right\\}_{k \in \mathcal Y}$, what does $\star$ mean here?
- In Algorithm 1, what is $i$ in the output? It doesn't seems to be in the input nor is it a loop variable.
- In Theorem 1, ${\boldsymbol{\epsilon}}_i \sim \mathcal N({\boldsymbol{0}}, {\boldsymbol{\sigma}}^2)$, what does ${\boldsymbol{\sigma}}^2$ mean? Do you mean $\sigma^2 {\boldsymbol{I}}$ where ${\boldsymbol{I}}$ is the identity matrix?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
