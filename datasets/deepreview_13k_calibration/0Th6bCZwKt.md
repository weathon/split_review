# Gaussian Mixture Models Based Augmentation Enhances GNN Generalization

- Decision: Reject
- Avg Score: 4.50
- Scores: 1, 5, 6, 6

## Abstract
Graph Neural Networks (GNNs) have shown great promise in tasks like node and graph classification, but they often struggle to generalize, particularly to unseen or out-of-distribution (OOD) data. These challenges are exacerbated when training data is limited in size or diversity. To address these issues, we introduce a theoretical framework using Rademacher complexity to compute a regret bound on the generalization error and then characterize the effect of data augmentation. This framework informs the design of GMM-GDA, an efficient graph data augmentation (GDA) algorithm leveraging the capability of Gaussian Mixture Models (GMMs) to approximate any distribution. Our approach not only outperforms existing augmentation techniques in terms of generalization but also offers improved time complexity, making it highly suitable for real-world applications.


\iffalse
We introduce a theorem that characterizes the effect of data augmentation on the generalization capabilities of GNNs. A second theorem employs the Fisher Information Matrix as a principled approach to guide the selection of augmentations, thereby enhancing the generalization performance of GNNs.
We have a condition on the above theorem between the distance between the distribution of the augmented graphs and original graph distribution.

Apply theorem to develop GMM-GDA algorithm, a new efficient algorithm for graph data augmentation (based on GMM)

Another Theorem uses Fisher Information Matrix to better guide the selection of our augmentations to improve the quality and performance downstream tasks.

We have better performance and more efficient in terms of time complexity compared to other graph augmentation techniques.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper discusses data augmentation for graphs. The concrete proposal is to use a Gaussian mixture model. The justification for this proposed approach is that Gaussian mixture models are universal density estimators.

### Strengths
Data augmentation for graphs is a topic that warrants investigation. There is little work on the subject. 
Numerical evaluations are comprehensive

### Weaknesses
The proposed data augmentation method is not specific to graphs. It could apply to any data type. No arguments are given as to whether this is suitable way of augmenting graph datasets.

Numerical evaluations are comprehensive but underwhelming. Improvements are marginal relative to training without data augmentation. All but 1 improvement in Tables 1 and 2 are well within one standard deviation and can be explained by random chance.

### Questions
I do not understand Theorem 1. Please expand explanation.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper the authors introduce a method to perform data augmentation algorithm for graph datasets. 
The algorithm leverages Gaussian Mixture Models (GMM) to find the maximum likelihood estimates for each cluster given by the embedding ofdifferent classes. Finlly they use the GMM to generate augmented data. Notice that augmented samples are generated directly in. the embedding space. The authors provide a bound for the Rademacher complexity fro the loss function  modified to account for augmented data.

### Strengths
- The proposed approach introduces a novel method for graph data augmentation. 
- The problem studied is relevant and interesting
- The algorithm's time complexity is  analyzed.

### Weaknesses
 - The clarity of the paper, particularly in Section 3, could be enhanced to guide the reader more effectively through the discussion.
- The method requires pre-training of the model  and moreover is dependent on the specific model architecture, meaning that the augmented dataset cannot be used by other GNN models.
- Baselines in Table 1 could be expanded to include additional augmentation techniques, such as edge insertion and feature drop.
- The metric used to measure the distance between $\mathcal{G}^{\lambda}$ and $\mathcal{G}$ in Theorem 3.1 and subsequent sections is not clearly defined.



### Questions
- In the case of GMM what does the parameter $\lambda$ represent ?
- Does the GMM-based sample generation method ensure that the augmented samples remain within the distribution of the original data?
 - Can the method be extended to different tasks on graphs? such as node classification and link prediction? 
Comment: 
If the maximum of the expectations $\mathbb{E}_{\lambda}[\mathcal{G}_n^{\lambda} - \mathcal{G}n]$ is non-zero, the Rademacher complexity of $\ell{aug}$ may not necessarily be smaller than the Rademacher complexity of $\ell$.

### Soundness
2

### Presentation
2

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
This paper proposed GMM-GDA, a graph data augmentation algorithm with better generalization abilities and faster training speed. GMM-GDA is presented based on a theoretical analysis relying a Rademacher complexity, which bounded the generalization error by the difference between the augmented data and original data. Furthermore, this paper verified the effectiveness of GMM-GDA from the perspective of influence functions and detailed experiments show the priority of the proposed algorithm.

### Strengths
1.	This paper analyzes the problem of GNN generalization capability, which is well-written and clearly clarified. The whole paper is easy to understand.

2.	This paper provides theoretical insights before presenting the algorithm. 

3.	The experiments of this paper is closely related to the research goal proposed.

### Weaknesses
1.	This paper did not explain the necessity of performing data augmentation by GMM. The authors should strengthen the explanation of the relationship between theory and the algorithm. Specifically, while GMMs are a universal approximator, the paper lacks a clear justification for why a GMM is preferred over other generative models, such as variational autoencoders (VAEs) or generative adversarial networks (GANs), which might offer more flexible or powerful representation learning capabilities. The theoretical analysis based on Rademacher complexity bounds the generalization error by the difference between augmented and original data distributions, but it does not inherently mandate the use of GMMs. The paper should clarify why the specific properties of GMMs are crucial for minimizing this difference, and why other generative models might not be as suitable.

2.	Some tables and figures do not seem to support the conclusions in the paper, which needs more explanation. For instance, Figure 2 shows the influence scores of the augmented embeddings on different datasets, but the authors do not provide a detailed analysis of why their algorithm performs worse on the DD dataset. This lack of analysis makes it difficult to fully understand the limitations of the proposed approach. Furthermore, the authors claim that GMM-GDA is efficient in the augmentation and training steps, and provide results in table 6. However, Table 6 shows that GMM-GDA still incurs significant augmentation and training time, which contradicts the claim of efficiency. The paper needs to provide a more nuanced discussion of the computational trade-offs and clarify what aspects of GMM-GDA are considered efficient relative to other methods.


### Questions
1.	Based on theorem 3.1, the motivation of the proposed method is to guarantee the alignment of the augmented data and original data, so the authors apply GMM to fit the embeddings of the training data. But there lacks an explanation of why GMM is applied, it seems that a simple DNN (or other more complex generative data augmentation techniques) can also fit the embeddings. Please explain the advantages of GMM. 

2.	It seems that only the post-readout function is trained by the combination of augmented data and original data (line 264). Why do not take several more iterations, and update the parameters of message passing layers? Please explain why only generate the embeddings of training data once but not re-generate them after updating the network. 

3.	Figure 2 shows the influence scores of the augmented embeddings on different datasets. But the authors did not analyze why in dataset DD their algorithm perform worse. This is an interesting phenomenon and worth a deeper analysis. 

4.	The authors claim that GMM-GDA is efficient in the augmentation steps and training steps and provide results in table 6 (line 315). But table 6 did not show the efficiency of GMM-GDA since it still cost much augmentation time or training time. Please explain why such a conclusion can be drawn from table 6. 

5.	In the result of table 1&2, it seems that GMM-GDA has a better performance in the setting of GIN compared with GCN. This phenomenon worth a deeper analysis. 

6.	The authors claim that the configuration models (line 470) is part of an ablation study, but it is hard to understand. Please explain more clearly about the conclusion of this experiment.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a novel graph data augmentation based approach to tackle the graph OOD problem. To be specific, they first train a GNN model using the training data. Then, graphs within each class in the training data are fed to the GNN model and the output of the readout layer are treated as the embeddings of this class. After that, the authors propose to fit a Gaussian Mixture Model (GMM) on the embeddings for each class using the classical EM algorithm. Finally, the augmented embeddings are generated by sampling from the GMMs for each class, which are combined with the embeddings of training data and used for fine tuning the post-Readout function. The proposed framework enjoy a high computation efficiency since the post-Readout function contains only a linear layer and the (time) complexity of fitting GMMs is linear. The authors also provide some theoretic analysis. First, they analyze the excess risk of the graph augmentation approach and the result shows that minimizing the expected distance between original graphs and augmented ones could reduce the excess risk. Second, they use influence functions to quantify the affect of augmented data on model's performance on testing data. Experimental results show that the their proposed method has competitive performance against baselines and has a significant benefit on advantages in robustness against structure corruption and time complexity.

### Strengths
The proposed technique is reasonable and efficient. The experimental results provided in the paper are sufficient to support the effectiveness of this technique. Considering the balance between effectiveness and computational efficiency of this technique, it has a potential application on real-world scenarios. Besides, the paper is well-written and easy to follow.

### Weaknesses
Although using a generative models to learn the graph representation distribution is reasonable, the motivation of adopting GMMs is still unclear. GMM is universal approximator of densities could be one of the reasons, yet how many component need to achieve a small approximation error is unknown. Besides, the theoretic results provided in this paper do not seem to explain why this method that generating augmentations in representation space is superior or comparable to previous methods that generating augmentations in data space, which could be a promising direction to be explored.

### Questions
Q1: The number of Gaussian distributions $K$ in GMMs is an important hyperparameter and has impact on the performance of GMM. How do you properly choose this hyperparameter in practices? Please describe the tuning process of $K$ or provide hyperparameter sensitivity analysis to show how performance varies with different values of $K$.

Q2: In line 349, the subscripts $i,j$ of the notation $\\mathcal{L}^{aug}_{i,j}$ are ambiguous. I think the correct one should be $\\mathcal{L}^{aug} _ {n,m}$.

Q3: The proof between line 703 to line 715 seems confusing. The first equality only holds when the right hand side also includes a expectation w.r.t. $\lambda_{n,m}$. Indeed, I think the proof should be proceeded as
\begin{equation}
\left\Vert \\frac{1}{N} \\sum_{n=1}^N \\mathbb{E}_{\\lambda \sim \\mathcal{P}} [\ell(\\mathcal{G}_n,\theta) - \ell(\\mathcal{G}'_n,\theta) ] \right\Vert =  \\left\\Vert \\frac{1}{N}  \\mathbb{E} _ {\\lambda \\sim \\mathcal{P}} [\ell(\\mathcal{G} _ k,\theta) - \ell(\\mathcal{G}' _ k,\theta)] \\right\\Vert \leq \\frac{1}{N}  \\mathbb{E} _ {\\lambda \\sim \\mathcal{P}} [\Vert \ell(\\mathcal{G}_k,\theta) - \ell(\\mathcal{G}'_k,\theta) \Vert ] \leq \frac{1}{N}.
\end{equation}
The first equality is obtained by your claim that $\\mathcal{G} _ k = \\mathcal{G}' _ k$ for $k = 1,\ldots, N$ and $k \neq n$. The last inequality is obtained by $\ell(\cdot) \in [0,1]$.
Please clarify this issue or correct this part of proof following the above steps.

Q4: In line 754, you claim that $\\hat{\theta} _ {aug}$ is the optimal parameter of the loss $\frac{1}{N} \\sum_{n=1}^N \\mathbb{E} _ {\\lambda \sim \\mathcal{P}}  [\ell(\\mathcal{G}^{\\lambda} _ n,\theta)]$, which is different from the definition of $\\hat{\theta}_{aug}$ in line 195 where $\\hat{\theta} _ {aug} = \\mathop{\rm argmin} _ {\theta} \\frac{1}{NM} \\sum _ {n=1}^N \\sum _ {m=1}^M \ell(\\mathcal{G} _ n^{\\lambda _ {n,m}}, \theta)$. This could make the inequality $v_3 \leq 0$ do not hold. Please clarify and check the definition of $\\hat{\theta} _ {aug}$. If the above issue do exist, you should consider revising your proof accordingly.

Q5: In line 221-223, you claim that minimizing the term $\\mathbb{E} _ {\\mathcal{G} \sim G} \\mathbb{E} _ {\\lambda \sim \\mathcal{P}} [\Vert \\mathcal{G}^{\\lambda} - \\mathcal{G} \Vert ]$ can guarantee with a high probability to decrease both the Rademacher complexity and the generalization risk. And you also show that the Rademacher complexity term $\\mathcal{R}(\ell _ {aug})$ is upper bounded by $\\mathop{\rm max} _ {n=1,\ldots,N} \\mathbb{E} _ {\\lambda \sim \\mathcal{P}} [ \Vert \\mathcal{G}^{\\lambda} _ n - \\mathcal{G} _ n \Vert ]$, which is a empirical estimation of $\\mathbb{E} _ {\\mathcal{G} \sim G} \\mathbb{E} _ {\\lambda \sim \\mathcal{P}} [\Vert \\mathcal{G}^{\\lambda} - \\mathcal{G} \Vert ]$ w.r.t. $\\mathcal{G}$. Therefore, minimizing the term $\\mathbb{E} _ {\\mathcal{G} \sim G} \\mathbb{E} _ {\\lambda \sim \\mathcal{P}} [\Vert \\mathcal{G}^{\\lambda} - \\mathcal{G} \Vert ]$ may not guarantee to decrease the Rademacher complexity term $\\mathcal{R}(\ell _ {aug})$. Please clarify this issue or modify your claim in line 221-223.

### Soundness
3

### Presentation
3

### Contribution
2
