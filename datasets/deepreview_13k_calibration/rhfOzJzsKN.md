# Communication-Efficient Federated Learning via Model-Agnostic Projection Adaptation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Federated learning (FL) enables collaborative model training across distributed clients without centralizing sensitive raw data while benefiting from diverse data sources. 
Despite recent advancements in FL, the communication overhead remains a significant challenge, especially for large-scale models.
Recent low-rank adaptation (LoRA) techniques have shown promise in reducing these burdens in FL, but they are typically applied to each layer individually and depend on the model architecture, which limits their performance.
To address these shortcomings, we propose  Model-Agnostic Projection Adaptation (MAPA), a novel approach that applies factorization to the entire model parameter space, which we view as a *single vector*, regardless of the number of layers and model architecture. 
MAPA factorizes the single-vector model update into a fixed *reconstruction matrix* and a trainable *projection vector*, with the reconstruction matrix being randomly initialized using a shared seed at each round. 
This ensures that *only* the projection vectors need to be communicated to the server, thereby reducing the communication cost.
Furthermore, MAPA's vector-based representation and relaxed rank constraints allow for a larger reconstruction matrix and smaller projection vector dimensions compared to LoRA, enhancing the expressiveness of model updates while significantly reducing communication overhead. 
Experimental results demonstrate that MAPA outperforms existing FL methods in both communication efficiency and model performance, effectively coupling optimization and communication efficiency in FL environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes Model-Agnostic Projection Adaptation (MAPA) to address communication overhead in federated learning by factorizing the model parameter space as a single vector, independent of layer count or model architecture. MAPA splits the update into a fixed reconstruction matrix and a trainable projection vector, sending only the projection vector to the server. This reduces communication costs while allowing a flexible, high-capacity reconstruction matrix. Experimental results show MAPA outperforms existing methods in both communication efficiency and model performance. Yet, aligning the experimental setup with model-agnostic principles remains an area for improvement.

### Strengths
1. The Model-Agnostic Projection Adaptation (MAPA) method introduces a novel approach to reduce communication overhead in federated learning (FL) by factorizing the entire model parameter space. The method employs a fixed reconstruction matrix and a shared random seed, allowing for larger reconstruction matrices and smaller projection vector dimensions. The paper provides strong theoretical support.
2. By transmitting only the trainable projection vectors, MAPA addresses a major challenge in FL by cutting communication costs. 
3. Experimental results indicate that MAPA outperforms existing FL methods in both communication efficiency and model performance.

### Weaknesses
1. Although the method is described as 'model-agnostic,' it currently uses the same CNN model and identical initial weights across all clients in the first round. This setup could contradict the claim of model agnosticism by implying a reliance on a specific model structure and initialization. Specifically, the use of a single CNN architecture with identical initializations across clients does not demonstrate the method's ability to handle heterogeneous model architectures and initializations, which is a key aspect of true model agnosticism. The current experimental setup only validates the method's performance under a homogeneous setting, limiting the generalizability of the findings. Therefore, it is essential to either revise the claims or provide further evidence that MAPA can operate with diverse initializations and model types across clients.
2. Additional experiments with different model architectures are recommended to showcase the method’s versatility and robustness. The current experiments are limited to a single CNN architecture, which does not provide sufficient evidence of the method's ability to generalize across different model types. Testing with architectures such as Transformers or other types of convolutional networks would be necessary to demonstrate the method's true versatility. The lack of such experiments raises concerns about the method's applicability to a wider range of practical scenarios.
3. Further testing on more complex datasets, such as ImageNet, would help demonstrate MAPA’s scalability. The current experiments are limited to relatively simple datasets. Testing on a more complex dataset like ImageNet would provide a more rigorous evaluation of the method's scalability and ability to handle high-dimensional data and more complex learning tasks. The absence of such experiments makes it difficult to assess the method's practical applicability to real-world scenarios.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
To reduce the substantial communication overhead in FL, this work presents MAPA and its extension MAPAX, a novel matrix factorization operating independently of the model architecture. The proposed method sends only projection vectors that leverage a shared reconstruction matrix generated at each round. MAPA treats the entire model parameter space as a single vector and factories it. The authors performed numerical experiments that showed that MAPA improves communication efficiency while maintaining strong model performance.

### Strengths
1. The paper provides theoretical analysis of MAPA's convergence and communication efficiency by clear and precise mathematical notations. The experiments on three dataset demonstrates MAPA's superiority over other methods.
2. The paper is well-organized, with straightforward writing and clear illustrations, especially the overview diagram, which effectively conveys MAPA's idea. Results are intuitively displayed, showcasing MAPA's improvement in reducing communication costs.

### Weaknesses
1. The paper lacks comprehensive experimental results for MAPAX, specifically missing accuracy and minimum cost outcomes on MNIST and CIFAR-10, which limits the ability to fully evaluate its effectiveness. The current results for MAPAX are insufficient to understand its performance trade-offs compared to MAPA, especially regarding the balance between communication efficiency and model accuracy.
2. I am curious whether the proposed method can be applied to the IID setting or the scenario where clients are sampled in each communication round. Evaluating and clarifying MAPA's performance under these conditions would strengthen the paper. The current experiments focus on non-IID settings, and it is unclear how MAPA would perform in more standard federated learning scenarios with IID data or with a subset of clients participating in each round. This is important for understanding the general applicability of the method.
3. Given the author's claim that MAPA is model-agnostic, the paper could strengthen this claim by combining MAPA with more FL models to demonstrate its versatility beyond the current implementations. The experiments are limited to a few model architectures, and it is not clear if MAPA can be easily integrated with other types of models, such as transformers or more complex CNN architectures. This limits the generalizability of the proposed approach.
4. There are several presentation issues that can be addressed: a) the text is too small to read in Fig. 4; b). misalignment between L. 517-524 and Fig. 6. Also, it would be better to provide more analyses and explanations for Fig. 6 in the main paper. The current presentation of results in Fig. 4 and Fig. 6 makes it difficult to fully understand the experimental outcomes and the behavior of MAPA and MAPAX.

### Questions
Refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method that factorizes the model within the parameter space, aiming to reduce communication overhead in the FL setting. By transmitting only the lower-dimensional projection vector rather than the entire parameter vector, the approach reduces the parameter need to be transmitted

### Strengths
1. Compared to related approaches like FFA-LoRA, this work’s MAPA method applies LoRA directly in the parameter space, thereby improving flexibility for agnostic models.

2. The extended method, MAPAX, provides a valuable trade-off between computational constraints and communication overhead. This balance makes MAPAX an interesting direction for further exploration.

### Weaknesses
 **Algorithm design**

1. The method requires generating and storing a matrix $A$ with $k \times d$ entries, where $d$ represents the number of parameters in the entire model, which is typically very large. This raises significant concerns about the method's practicality due to the immense computational and memory requirements. Although the authors introduce MAPAX as a solution to mitigate these issues, there is a lack of experimental results validating its effectiveness. Without empirical evidence, it's challenging to assess whether MAPAX successfully addresses the computational and storage challenges posed by MAPA.

2. The matrix $A$ is generated randomly, similar to the approach in FAA-LoRA [1]. Recent studies [2] have indicated that random generation of such matrices may lead to suboptimal performance.

**Theoretical analysis**

1. The "representation capacity rate" introduction in Definition 2 lacks clarity and justification. The term "representation capacity" is not well-defined in the context of the paper, and it's unclear why the proposed quantity effectively measures it. There is no evident connection between the introduced definition and established metrics for the complexity of function classes, such as covering numbers.

2.  In Definition 2, the focus is solely on the rank $k$ of matrix $A$, neglecting the influence of the dimension $d$. In representation learning literature, the complexity typically depends on both $d$ and $k$.

3.  Due to the unclear definition of the representation capacity rate, the claim in Proposition 1 that the proposed method "...achieves a higher representation capacity..." lacks substantiation.

4.  The convergence analysis is built upon Assumption 4, which appears to be too restrictive and not reflective of practical scenarios. For instance, this assumption may not hold if $W_t$ reaches a saddle point in the non-convex optimization landscapes.

**Experiments**

1. The reported accuracy on the CIFAR-10 dataset is unexpectedly low. Previous work, such as FedRep [3], published in 2021, has demonstrated significantly higher accuracy levels, even though it is not SOTA.  Besides, the selection of baseline algorithms in the experimental evaluation is inadequate.

2. Although MAPAX is proposed to address the computational and memory burdens introduced by MAPA, the paper does not present any experimental results for it.

### Questions
See the "Weakness" section.

### Soundness
3

### Presentation
2

### Contribution
2
