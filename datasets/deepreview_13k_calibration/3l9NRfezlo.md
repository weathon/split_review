# DFL$^2$G: Dynamic Agnostic Federated Learning with Learngene

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
Dynamic agnostic federated learning is a promising research field where agnostic clients can join the federated system at any time to collaboratively construct machine learning models. The critical challenge is to securely and effectively initializing the models for these agnostic clients, as well as the communication overhead with the server when participating in the training process. Recent research usually utilizes optimized global model for initialization, which can lead to privacy leakage of the training data.
To overcome these challenges, inspired by the recently proposed Learngene paradigm, which involves compressing a large-scale ancestral model into meta-information pieces that can initialize various descendant task models, we propose a \textbf{D}ynamic agnostic \textbf{F}ederated \textbf{L}earning with \textbf{L}earn\textbf{G}ene framework. The local model achieves smooth updates based on the Fisher information matrix and accumulates general inheritable knowledge through collaborative training. We employ sensitivity analysis of task model gradients to locate meta-information (referred to as \textit{learngene}) within the model, ensuring robustness across various tasks. Subsequently, these well-trained \textit{learngenes} are inherited by various agnostic clients for model initialization and interaction with the server. Comprehensive experiments demonstrate the effectiveness of the proposed approach in achieving low-cost communication, robust privacy protection, and effective initialization of models for agnostic clients.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This manuscript proposes a framework, called DFL2G, to address two main challenges in federated learning: (1) initialization of the client model parameters for new "agnostic" clients and (2) to reduce communication overhead between clients and server during training process. The framework consists of three modules: Learngene Smooth Learning, Learngene Dynamic Aggregation, and Learngene Initial Agnostic Model, to effectively address these challenges. Experimental results demonstrate that the approach effectively reduces communication cost while maintaining comparative classification accuracy.

### Strengths
1. This paper proposes an innovative approach for federated learning, which dynamically initializes effective parameters for new clients and utilizes  Learngene concept to reduce communication overhead and strengthen privacy.
2. The results show that the performance of the proposed method is comparable with the baselines.
3. The paper is well-structured.

### Weaknesses
1. Lack of convergence proof and theoretical support.
2. The experimental results are limited. Further the authors have not considered different heterogeneous settings in their experiments.
3. There is no comparison with the baselines having similar objectives (e.g., FedProto, FedTGP).

### Questions
1. I believe that the "cef" measure in Table 1 doesn't provide a fair comparison, as there is no direct relation between communication cost and accuracy. 
2. It would be nice to see more experimental support, including diverse datasets and non-IID scenarios with different data heterogeneity levels (α = 0.05, 0.5, 0.1).
3. Also the authors should consider to include one or two standard FL baseline like SCAFFOLD, FedProto, FedTGP, to better demonstrate method's superiority.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce  **D2FL**, a novel method designed to address the challenge of initializing local models for agnostic clients in federated learning without necessitating the sharing of a global model. Leveraging the  **Learngene paradigm**, D2FL focuses on the rapid initialization of agnostic models through the use of "learngenes." These learngenes encapsulate essential model knowledge, allowing new or agnostic clients to initialize their local models efficiently by inheriting this distilled information. The primary claims of D2FL include reduced communication overhead and enhanced privacy compared to the standard Federated Averaging (FedAvg) approach. By minimizing the need to transmit large model updates and avoiding the distribution of a global model, D2FL aims to achieve more scalable and privacy-preserving federated learning.

### Strengths
1.  **Seemingly Effective Reduction of Communication Costs:**
    
   D2FL seemingly lowers communication overhead in federated learning  where instead of transmitting full model updates, local updates are compressed into lightweight "learngenes," which are then shared with the server. For a fixed communication budget, the tradeoff is improved. This is shown in experimental work
    
2.  **Efficient Initialization of Agnostic Client Models:**
    
 The framework leverages accumulated knowledge from participating clients to generate and store learngenes in a central pool. When new or agnostic clients join the network, they can initialize their models by inheriting these learngenes, facilitating rapid and effective model initialization. 
    
3.  **Improved Privacy Preservation:**
    
By avoiding the direct sharing of global models and instead using condensed learngenes, D2FL offers improved safety against standard gradient attacks unlike  FedAvg. The authors also highlight that the "privacy" means defense against gradient based attacks only.

### Weaknesses
 1.  **Ambiguous Notation for Agnostic Clients:**
    
 The notation used to represent agnostic clients, particularly in lines 128-129, is unclear.  
    
2.  **Scalability Concerns Due to Server-Side Storage Overhead:**
    
  The server maintains  K cluster models, which introduces significant storage overhead. As the number of clusters increases, the storage requirements may become prohibitive, raising concerns about the scalability of D2FL in large-scale federated learning environments. This limitation is not adequately addressed or acknowledged in the paper. This is especially relevant when comparing with other baselines
    
    
3.  **Insufficient Explanation of the Likelihood Function for FIM Computation:**
    
 The  **Fisher Information Matrix (FIM)**  is utilized within the framework, but the paper does not explicitly explain the likelihood function used to compute it 202-203. The description of how the FIM is calculated is vague, and it's not clear what probability distribution is being used to derive the likelihood function. This lack of clarity makes it difficult to assess the validity of the FIM approximation and its impact on the overall method.
    
4.  **Complexity of the Learngene Concept:**
    
 As there are multiple procedures happening in the paper, the introduction and explanation of the Learngene concept are convoluted, making the paper difficult to follow. It required multiple reading to understand some concepts. The authors should simplify the presentation of this concept, possibly by providing more intuitive explanations or systematically develop concepts to improve comprehension.
    
5.  **Unclear Combined Loss Function:**
    
  In line 230, the paper presents a combined loss function where the same weight parameter  λ  controls multiple aspects of the loss. The interaction and impact of  λ  on different loss components are not clearly delineated. Also the ablation studies do not incorporate the impact of the hyper parameter adjustment of these seperate learngene and elastic gene loss functins
    

 6.  **Ambiguities in Experimental Figures and Tables:**
    
  **Figure 4:**  The dataset and model used in this figure are not clearly specified. Additionally, the performance of D2FL in low epoch regions (e.g., epochs less than 10) is smaller than some baselines other methods that perform better under these conditions.  This needs to be acknowledged.
        
   **Table 4:**  The table does not include standard deviations. Furthermore, it fails to separately evaluate the impact of elasticity and the Learngene component, despite elasticity being a core component of the paper. Same hyper parameter controls both the loss function so it is difficult to establish the impact of these seperate loss functions. This omission makes it challenging to determine the individual contributions of each component to the overall performance.
        
  **Table 5:**  Similar to Table 4, Table 5 lacks descriptive information about the datasets used and the statistical measures reported.

7.  **Absence of Theoretical Convergence Guarantees:**
    
    The paper does not provide any theoretical analysis or proofs to support the convergence of the Learngene-based initialization method.

### Questions
Please refer to weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper studies dynamic agnostic federated learning, specifically on initializing the client models (by using the learngene paradigm) and achieving better communication overhead while protecting the privacy of the models. They propose DFL$^2$G, which consists of smooth updating, dynamic aggregation, and initial agnostic model.

### Strengths
- The paper proposes "collaborating, condensing, initializing" steps analogous to the Learngene paradigm. 
- The topic of dynamic agnostic federated learning is important. 
- The provided empirical results cover various settings and baseline methods.

### Weaknesses
- **Readability**: 
   - There are many mistakes, both in the text and notations, creating obstacles for the reader. 
   - $\mathcal{X}_{k,i}$: why do you need $k$ here? The local datasets $\mathcal{X}_i$ are not being clustered. The subscript $k$ seems unnecessary and potentially confusing. It should be clarified whether this notation represents a specific subset or a modified version of the local dataset.
   - Eq.8: why multiplier? The term "multiplier" is not defined in the context of this equation. It's unclear what this multiplier represents and how it affects the overall aggregation process. A more precise mathematical term should be used instead.
   - [Line 240]: $\sum_{l=1}^L \xi_{k,i}^{(l)} = 1$. How does this sum up to 1? It does not seem to be valid. The normalization of the coefficients $\xi_{k,i}^{(l)}$ across layers is not adequately explained. The equation suggests a constraint that might not hold true in the proposed method. A detailed explanation of how these coefficients are derived and normalized is required.
   - [Line 229]: Overall, you have the following objective function: 
\begin{equation}
\mathcal{L}\_ {all} = \lambda \mathcal{L}\_ {gen} + \lambda \mathcal{L}\_ {elg},
\end{equation}
which gives 
\begin{equation}
= \lambda \mathcal{L}\_ {cls} (\mathcal{X}\_ {k,i}) + \lambda^2 \|\| \theta\_ {k,i} - \Theta\_ {k} \|\|_2 + \lambda^2 \|\| \theta\_ {k,i}^{'} - \Theta_k ||_2, 
\end{equation}
and it has issues in the formulation. The transition between the two equations is not clear. The introduction of the squared L2-norms and the $\lambda^2$ term needs further justification. It's not evident how the $\mathcal{L}\_ {gen}$ and $\mathcal{L}\_ {elg}$ terms are expanded into these specific regularization terms.
   - Typos in lines: 198, 199, 201, 226 (what is the second loss function?), 243 (different subscripts), 272, 283 (why j? you can stick to k.), 313, etc. 

- Section 2.4. Problems in the SVD decomposition and formulation. How can you set the data dimension $d$ to 5? $d$ can not equal some other value than its original value. The paper states that the data dimension $d$ is set to 5. This is a significant point of concern. The dimensionality of the data is an inherent property and cannot be arbitrarily changed. Reducing the dimensionality to 5 through SVD would lead to a substantial loss of information, especially if the original dimensionality is much higher. The rationale behind this choice and its impact on the results need to be thoroughly explained and justified.

- Privacy analysis. For a fair comparison with other baseline methods, you need to leverage all available information to reconstruct the samples $\mathcal{X}_i$. Since clients are sharing $V_i$'s with the server, which can aid your reconstruction objective you have (Eq. 12), using the iDLG objective solely is not fair; therefore, it raises a question regarding the results in the paper (Figure 5). The privacy analysis relies solely on the iDLG method for reconstruction. However, the paper mentions that clients share $V_i$'s with the server. These shared components could potentially be exploited to improve the reconstruction accuracy beyond what iDLG alone can achieve. A more comprehensive privacy analysis should consider using all available information, including the shared $V_i$'s, to provide a fairer comparison with other methods.

- The number of local epochs is huge (line 335, local epochs = 10), which should not be the case in heterogeneous FL since it makes the clients overfit to their local data. The use of 10 local epochs is unusually high for a heterogeneous federated learning setting. This large number of local epochs could lead to significant overfitting on individual client data, thus hindering the model's ability to generalize across the entire federation. A more detailed justification for this choice, along with an analysis of its impact on model performance and generalization, is needed.

- The proposal of a new metric. Why propose a metric if you use it only in one table (Table 1)? Also, it is better to see the Acc. measures in Table 1. The newly proposed metric is only used in Table 1, which raises questions about its general applicability and usefulness. If the metric is indeed valuable, it should be used more broadly to evaluate different aspects of the proposed method. Additionally, including standard accuracy measures in Table 1 would provide a more comprehensive evaluation of model performance.

- Performance curve comparison (Figure 4). The figure doesn't correspond to what is reported in the table, which questions the study's validity. Also, the proposed method has a high variance (deviation) compared to other methods, which doesn't necessarily mean the method outperforms others. The baseline methods do not improve, having a straight-line performance (FedLP, Flearngene). There is a discrepancy between the performance curves shown in Figure 4 and the results reported in Table 3. This inconsistency needs to be addressed and clarified. Furthermore, the high variance observed in the proposed method's performance should be investigated and explained. While high variance might indicate potential for improvement, it also suggests instability and raises concerns about the method's reliability.

- Table captions should be on top. 
- Consider citing other works using \citep{}.

### Questions
See weaknesses.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper is aiming at addressing two key challenges in Federated Learning (FL): 
1) privacy leakage during client-server communication, and 
2) communication overhead in transmitting model updates. 
To tackle these issues, the authors propose the Learngene framework for Dynamic Agnostic Federated Learning (DAFL). The Learngene framework introduces a mechanism for compressing model updates into learngenes, which capture the most important information while reducing data transmission and mitigating the risk of privacy leakage. Additionally, the framework supports dynamic client participation, allowing clients to join and leave the system flexibly without compromising performance.

### Strengths
The paper presents an innovative solution through the introduction of the Learngene framework. By integrating Learngene into the Dynamic Agnostic Federated Learning paradigm, the authors enable efficient model initialization and communication, particularly for agnostic clients that join the system dynamically.

The experimental results are compelling, demonstrating a significant reduction in communication costs while maintaining or even enhancing model accuracy. This highlights the framework's ability to improve both scalability and performance in federated learning environments.

### Weaknesses
1) Assume a one-shot dataset in the client. This assumption allows for efficient clustering and model initialization but may limit the framework’s flexibility in handling the common dataset with more samples. Specifically, the use of a one-shot vector obtained through truncated singular value decomposition, while efficient for initial clustering, might not capture the full complexity of evolving client data distributions over time. 
2) Lack of Dynamic Cluster Management: The paper does not address how to manage clusters when they become too large or too small. In cases of high data heterogeneity, more clusters are required to accurately represent the diversity among clients. However, the framework does not discuss mechanisms to dynamically adjust the number of clusters based on client performance, data distribution, or scalability concerns. For example, a mechanism for splitting or merging clusters based on intra-cluster variance or inter-cluster similarity could be beneficial. 
3) Insufficient Privacy Guarantees: The paper does not provide strong privacy guarantees. The only implication we have based on your illustration is that "iDLG cannot recover the feature $X \in R^d $ given learngene". 
Moreover, the privacy protection is questionable when considering the specifics of the Singular Value Decomposition used in the framework. your $X_i \in R^{1\times d}$, $X_i = U_i \Sigma_i V_i^T$. $U \in R^{1\times1}$, $\Sigma \in R^{1\times d}$ diagonal matrix. Therefore, there are only 2 unknown numbers to recover $X_i$. if ignoring the scale ($U \in R^{1\times1}$), there are only one number left to recover your $X_i$, which would be easy. 
Besides, The dimensions are not clearly explained for SVD here. Your $X_i$ should be a matrix $X_i \in R^{1\times d}$


Presentation: 
1) Your citation format is incorrect for the entire paper. In latex, most of your citations should be \citep{}. and will be rendered "FL (McMahan et al. 2017)". 
2) Since you still have space, I suggest that your algorithm should be placed in the main body of the paper. Because it provides a more general view of how you integrate Learngene smooth learning, learngene dynamic aggregation, and learngene initial agnostic model into one framework.
3) your algorithm line 4. The tilde of $\theta$ is in the wrong place. 
4) #276 your mentioned $d=5$. Does this mean that your private data $X \in R^d = R^5 $, If so, is this a typo here?

### Questions
How you update the cluster was not specific in algorithm 1. As a new agnostic client join the network, it is added to the nearest cluster as stated in line 18 of Algorithm 1. However, as new clients involve the cluster should be updated. Or is it the cluster only built at the beginning?

### Soundness
3

### Presentation
2

### Contribution
3
