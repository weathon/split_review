# Heterogeneous Federated Learning: A Dual Matching Dataset Distillation Approach

- Decision: Reject
- Scores: 3, 5, 3, 5, 3

## Abstract
Federated Learning (FL) often struggles with error accumulation during local training, particularly on heterogeneous data, which hampers overall performance and convergence. While dataset distillation is commonly introduced to FL to enhance efficiency, our work finds that communicating distilled data instead of models can completely get rid of the error accumulation issue, albeit at the cost of exacerbating data heterogeneity across clients. To address the amplified heterogeneity due to distilled data, we propose a novel FL algorithm termed \textit{FedDualMatch}, which performs dual matching in the way that local distribution matching captures client data distributions while global gradient matching aligns gradients on the server. This dual approach enriches feature representations and enhances convergence stability. It proves effective for FL due to a bounded difference in the testing loss between optimal models trained on the aggregation of either distilled or original data across clients. At the same time, it can converge to within a bounded constant of the optimal model loss. Experiments on controlled heterogeneous dataset MNIST/CIFAR10 and naturally heterogeneous dataset Digital-Five/Office-Home demonstrate its advantages over the state-of-the-art methods that communicate either model or distilled data, in terms of accuracy and convergence. Notably, it maintains accuracy even when data heterogeneity significantly increases, underscoring its potential for practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work the authors propose a new method for private synthetic data for federated learning. The method takes advantage of Local Distribution Matching and further propose Global Gradient Matching to mitigate the heterogeneity exacerbated in the LDM stage. The method comes with some formal guarantees and experiments on several real world datasets suggest that the proposed method converges faster compared to prior baselines.

### Strengths
- Overall this work is well written.
- The direction of private synthetic data for federated learning is important.
- The combination of LDM and GGM is nice and well explained.
- The method comes with convergence guarantee.

### Weaknesses
 - The authors should more carefully highlight and discuss the contribution and difference between the proposed method and FedDM. Correct me if I'm wrong: the key new stuff seems to be 1. Sec 4.2 which is the global gradient matching part, 2. introduction of the error ball in Sec 4.1, which is mainly building upon the technique used in FedDM? If so, I suggest the authors to highlight it more clearly in the intro / list of contributions.
- Theorem 2 does not provide the exact convergence rate. $C$ is a term that contains $\mathbb{E}[L(w_{t-1};\mathcal{D})]$. Hence, it's not a constant. Could the authors work out the convergence rate for the proposed algorithm?
- Privacy guarantee is pretty hand-wavy and I have the following questions.
 1. What are $\sigma_r$, $\sigma_s$, and $\sigma_d$ respectively?
 2. What does the private algorithm look like? From the appendix, the Gaussian mechanism is applied to the gradient and $R_t$ directly. The later looks like an output perturbation but it's unclear where the former DPSGD style update is performed? Is it done during client update or server update?
 3. If the gradient privatization is done at client side, I'm wondering why do we need privatization of $R_t$ as isn't that directly followed by post-processing? 
- Algorithm description is not clear enough. Is the synthetic data being regenerated for each communication round?
- Figure 4 seems to provide some intuition on communication efficiency vs utility but it's unclear what is the size of the synthetic data (information communicated in the proposed method) vs the size of the actual gradient (information communicated in FedAvg). A more intuitive plot to me is to replace the x-axis to be the amount of information being communicated in size.
- CIFAR 10 accuracy seems abnormally low (compared to Figure 3 in FedDM). Is it due to the use of a less powerful model?
- Figure 4 legend, I guess it's FedDualMatch instead of FedBi-Match?

### Questions
See the above weaknesses about questions related to privacy analysis and experiments.

### Soundness
2

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
3

### Summary
This paper introduces a federated learning method, FedDualMatch, which leverages dataset distillation to address client heterogeneity. FedDualMatch combines the strengths of two dataset distillation approaches—distribution matching and gradient/trajectory matching—to enhance overall performance. The authors observe that distribution matching can intensify data heterogeneity, while gradient/trajectory matching helps to mitigate client drift. FedDualMatch is specifically designed to balance these effects, addressing the limitations of each approach. The authors validate the effectiveness of FedDualMatch through experiments on the MNIST and CIFAR-10 datasets, supported by an ablation study and further discussions in the experiments section.

### Strengths
1. The paper is motivated well. The findings in figure 1 are impressive. 

2. The authors aim to provide adequate theoretical proof to support their derivation.

3. The authors conduct ablation studies to verify the effectiveness of their methods.

### Weaknesses
1. The mathematical notation is currently unclear, leading to confusion. There are no prior definitions for the variables and terms used in the equation, resulting in potential misunderstandings.

(a) what is the definition of $S_k$ in line 236? A very rough definition appeared in line 242.  

(b) What is the meaning of $w^{t+E}$? Does it refer to the weights at epoch $E + t$? Then what does $W_t^{S_k}$ signify? What is the difference between the two kinds of $t$.  What is the meaning of $S_k$ here? The updated weights using $S_k$? This lack of clarity makes the derivation difficult to follow.

2. Assumption 4 may be too strong to generalize to real-world scenarios. It states that 'Assumption 4 ensures that gradients computed on distilled datasets closely approximate those computed on the aggregated dataset, minimizing error accumulation.' However, based on my experience with dataset distillation, the difference between gradients on distilled datasets and the full dataset can be significant, which could lead to substantial error accumulation.

3.  Figure 2 and Figure 3 are too complicated to understand. There is no emphasis on these figures. The figures should be simplified while the captions should be more detailed. 

4. The paper only examines MNIST and CIFAR-10 datasets, which limits its relevance and applicability. For a 2024 publication, a broader range of datasets would strengthen its impact and generalizability, particularly with more complex or diverse data reflecting modern challenges.

### Questions
1. For the equation in lines 188 to 192, how would it change if $ n_k $ differs for each client? Also, in the second line, $ x_i $ should be written as $ x^i $, consistent with $ x^i_k $ in the first line.

2. Could the authors conduct experiments on at least the CIFAR-100 dataset? Including Tiny-ImageNet would also be beneficial. Notably, recent dataset distillation papers have conducted experiments on larger datasets, such as ImageNet-1K, which would enhance the paper's relevance and demonstrate the method's scalability.

3. How to adjust the client heterogeneity ($\alpha$) in your experiments? Does any other baselines use the same method to adjust client heterogeneity ($\alpha$)? The reported results of baselines in table 1 are produced by you own reproduction or cited from other papers?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors of this work propose to use distribution matching at the client and gradient matching at the server to take advantage of the former in extracting the best features and the latter in reducing the heterogeneity. They provide theoretical proof for the closeness of the solution in the case of using the actual dataset vs the distilled dataset using their method. They also provide convergence analysis and proof for differential privacy under their algorithm. The experiments show convincing improvements.

### Strengths
The main strengths of the paper include:
- taking advantage of mixing distribution matching at clients and gradient matching at the server
- the authors provide good introductory intuition of why they use these distillation algorithms at different stages, i.e., client distillation and server training rounds
- the experiments show convincing improvements in the proposed algorithms (although there are some under-explored axes when considering the algorithm)
- the authors provide several theoretical proofs.

### Weaknesses
While the paper tackles a significant problem in the domain, there are several drawbacks of the methodology proposed (some of which are under-explored or not discussed in the paper):
- while authors tell that they would use distribution matching and gradient matching for certain properties, i.e., extracting features and tackling heterogeneity, the paper does not provide the reader with insights into why these techniques impart these properties to the corresponding representations. Specifically, it is not clear how distribution matching at the client level leads to better feature extraction compared to other methods, nor is it clear why gradient matching at the server is effective in reducing heterogeneity beyond simply averaging gradients. The paper lacks a detailed explanation of the underlying mechanisms that cause these methods to have the desired effects.
- the authors do not consider client sampling during FL. This is a significant limitation as in real-world federated learning scenarios, not all clients are available at each round. The absence of client sampling makes the results less applicable to practical settings.
- authors compare their work with only one comparable baseline. FL-based techniques are drastically different in terms of data transfer and thus cannot be considered appropriately strong baselines for such a technique. Perhaps authors could look into techniques that similarly rely on data sharing such as [1] which considers sharing data in a different form or techniques such as [2] that consider privacy-preserving data sharing. The current comparison does not adequately contextualize the performance of the proposed method against other data-sharing approaches.
- The computation cost of the algorithm is quite high. The authors should provide those comparison apart from the performance comparison they have included. The computational overhead of generating and processing synthetic data, especially with distribution matching, is not thoroughly analyzed. A detailed comparison of computational costs with other methods is needed to assess the practical feasibility of the proposed approach.

### Questions
- Will the theoretical analysis hold if the authors consider client sampling?
- Will the experimental results hold if the authors consider a larger number of devices in an FL round?
- Will the experimental results hold if the authors were to consider larger neural networks? How will the size of the network affect the computational complexity of the algorithm?
- Could the authors cite other works in the literature that use assumptions 3 and 4? These seem very restrictive assumptions and citations would help assess the prevalence of such assumptions.
- How will the performance compare against more recent FL algorithms in works such as [3]?
- Could the authors provide the class distribution for different $\alpha$'s in the Dirichlet distribution?
- In Fig 5, why does the performance drop as the IPC increases beyond 10?
- Do the authors have intuition into why the algorithm would stagnate in low-heterogeneity scenarios?

[3] Reddi, Sashank J., et al. "Adaptive Federated Optimization." _International Conference on Learning Representations_.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel framework for communicating distilled datasets in Federated Learning (FL), aiming to address the challenge of data heterogeneity across clients.

Each client generates a synthetic dataset using Local Distribution Matching (LDM), which is based on Maximum Mean Discrepancy (MMD). The synthetic dataset is then communicated to the server instead of model parameters.

On the server, Global Gradient Matching (GGM) is performed, which aligns the gradients of the synthetic datasets from all clients to reduce client drift and improve convergence stability. An error ball is employed to constrain model updates during the GGM process, ensuring that parameter updates remain within a controlled range.

### Strengths
The paper presents an interesting approach to addressing the data heterogeneity problem in Federated Learning (FL) by introducing Global Gradient Matching (GGM). 

Proposed a combination of Local Distribution Matching (LDM) and Global Gradient Matching (GGM). Demonstrate convergence on the proposed framework.

### Weaknesses
Weakness: 
1) Computational Overhead: The method relies on dataset distillation and performs layer-wise alignment of the feature distributions between the original dataset and the synthetic dataset $S_k$. This process, especially the backward layer-wise alignment and the repeated distillation of $S_k$ is computationally expensive. 
This high computational cost is particularly problematic in resource-constrained environments such as edge devices, which are common in FL applications.
On the server side, the Global Gradient Matching (GGM) introduces additional overhead since multiple rounds of gradient matching (M iterations) need to be performed, requiring the server to compute gradients on all clients’ synthetic datasets. 
This dual burden on both the clients and the server could limit the scalability and practical deployment of this method in real-world FL scenarios, especially when computational resources are limited.

2) Communication overhead: The method requires clients to transmit synthetic datasets to the server, which could incur significant communication costs. 

3) While the inclusion of Differential Privacy (DP) provides privacy guarantees, it feels like an add-on rather than a core part of the proposed solution. The main focus of the research is on handling data heterogeneity, and the addition of DP doesn't significantly contribute to addressing that core problem. If the paper is mainly concerned with addressing data heterogeneity, it might be more effective to focus on that and remove the DP component to streamline the discussion. 

Presentation problems: 
1) Citation at #240, should be \citep{}. 
2) The presentation of the algorithm can be improved. 
>1. Specify the equation used to fine-tune the model in #283. You acquired $L_{GGM}$ and how you used it in the following? 
>2. Specify how you acquired synthetic dataset $S_k$ by minimizing the equation in #290, i.e. using $\argmin$ directly. 
>3. The method for minimization was not specified, i.e. how you iterate to optimize $S_k$. (#290). 
3) The *algorithm* for your DP scheme on how you add noise is not clearly defined. How did you add noise to the radius $R_t$ and dataset $S_k$? is the noise sampled each round? My suggest is adding it into the algorithm.

### Questions
See weeknees.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents FedDualMatch, a federated learning framework that addresses the challenges of training with heterogeneous client data. The proposed method uses distilled data for communication rather than model updates, employing local distribution matching (LDM) to capture client-specific data features and global gradient matching (GGM) to stabilize global model training. This dual approach aims to reduce error accumulation, mitigate client drift, and improve convergence stability, demonstrating superiority over traditional federated learning methods in terms of accuracy and convergence speed. However, uploading distilled datasets to the central server introduces potential privacy risks, which could conflict with federated learning's privacy-preserving philosophy.

### Strengths
- By transmitting distilled datasets instead of model updates, the paper introduces an innovative approach to tackle error accumulation and instability in federated learning, offering a fresh perspective over traditional methods like FedAvg.
- The paper provides detailed theoretical justifications, validating the effectiveness, convergence, and differential privacy of using distilled data for federated communication, which adds credibility to the proposed method.

### Weaknesses
 - Although the paper claims to maintain differential privacy, transmitting distilled datasets may still pose privacy risks, as these representations could retain sensitive information. This potential weakness is particularly concerning for high-stakes applications. The authors could strengthen the analysis by conducting additional experiments or analyses to quantify any sensitive information that might be retained in the distilled representations. Specifically, an analysis of the information leakage through membership inference attacks or reconstruction attacks on the distilled data would be beneficial. Furthermore, the paper should clarify the specific parameters of the Gaussian noise added to the distilled data and how these parameters are chosen to balance privacy and utility.
- The dual matching process, especially gradient matching on the server, introduces significant computational overhead, which could challenge deployment in resource-constrained environments, such as edge devices. A detailed analysis of computational costs, compared to baseline methods, would provide clarity, and discussing potential optimizations or trade-offs could make the approach more feasible for limited-resource settings. The paper should provide a breakdown of the computational complexity of each step in the dual matching process, including the local distribution matching and global gradient matching, and compare these complexities with those of traditional federated learning methods. This analysis should also consider the memory requirements of the proposed method, especially when handling large distilled datasets.
- The paper notes that FedDualMatch shows performance stagnation when client data distributions are similar, indicating that the method may not consistently outperform traditional approaches in low heterogeneity scenarios. An explanation of potential reasons behind this limitation and suggestions for addressing it in future work would offer valuable insights into the method’s adaptability. The authors should investigate whether the local distribution matching process becomes less effective when client data distributions are similar, and whether the global gradient matching process is sufficient to overcome this limitation. A more detailed analysis of the interplay between local and global matching under varying degrees of data heterogeneity would be beneficial.

### Questions
- Figures like Figure 3 are helpful for visualizing the concepts, but adding more detailed explanations or captions could further enhance their clarity.
- The proposed approach introduces distilled data updates to the central server to eliminate error accumulation, but it also increases communication overhead. As the dataset size grows, this communication overhead could become more significant.
- In Figure 4, the number of communication rounds is limited to 20. From the plots, it appears that some of the federated learning methods have not yet converged within this range. Extending the number of rounds might provide a clearer comparison.
- Comparing Table 1 with Figure 4 reveals an inconsistency in the results for SCAFFOLD on CIFAR-10 when alpha =0.01 vs alpha = 0.005. Specifically, the test accuracy for alpha = 0.01 is around 17.14, while for alpha = 0.005, it is around 33.83. Theoretically, the accuracy for alpha = 0.01 should be better than that for alpha = 0.005, so this discrepancy warrants further explanation. Similar inconsistencies appear with other methods as well.
- The experiments were conducted with only 10 clients, which may not be sufficient to demonstrate the robustness and generalizability of the results. A larger number of clients would strengthen the reliability of the experimental findings.

### Soundness
3

### Presentation
2

### Contribution
2
