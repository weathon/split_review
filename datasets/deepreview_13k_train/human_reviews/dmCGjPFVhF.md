# FACTS: A Factored State-Space Framework for World Modelling

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
World modelling is essential for understanding and predicting the dynamics of complex systems by learning both spatial and temporal dependencies. However, current frameworks, such as Transformers and selective state-space models like Mambas, exhibit limitations in efficiently encoding spatial and temporal structures, particularly in scenarios requiring long-term high-dimensional sequence modelling. To address these issues, we propose a novel recurrent framework, the FACTored State-space (FACTS) model, for spatio-temporal world modelling. The FACTS framework constructs a graph-structured memory with a routing mechanism that learns permutable memory representations, ensuring invariance to input permutations while adapting through selective state-space propagation. Furthermore, FACTS can be linearised to support parallel computation of high-dimensional sequences. We empirically evaluate FACTS across diverse tasks, including multivariate time series forecasting and object-centric world modelling, demonstrating that it consistently outperforms or matches specialised state-of-the-art models, despite its general-purpose world modelling design.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a framework that constructs a graph-structured memory for predicting the dynamics of complex systems with the selective state space architecture. The proposed architecture incorporates a graph-structured memory that dynamically routes input features to distinct latent factors and hence achieving permutation invariance. The proposed framework leverages parallel computation and selective state-space propagation (via attention) allowing it to handle sequences with complex dynamics efficiently. 

Through experiments on multivariate time series forecasting and object-centric world modeling, the paper shows that FACTS performs competitively or better than state-of-the-art baselines. The interesting result is its robustness to changes in input order, which simulates real-world scenarios where the configuration of inputs may vary unexpectedly.

### Strengths
- The proposed architecture introduces a permutable memory structure, allowing flexible handling of unordered or dynamically changing inputs. The paper achieves improved performance over baselines by compressing history efficiently, and hence capturing long-term dependencies. 
- The paper is easy to read and comprehend.
- The results shown on long term forecasting are interesting, and helps the reviewer to understand the implications of the proposed work better (especially forecasting with pre-defined and unknown order).

### Weaknesses
 - Object centric video modelling results are a bit weak. it will be interesting to report results also on OBJ3D (another benchmark used in Slotformer paper). It will also be helpful to report downstream results like Predictive VQA on CLEVRER, Physion (similar experiments as in Slotformer paper).

 - The SCOFF [1] and Neural Production Systems work [2] is very relevant. These works also proposed the idea of factorizing the latent state and ensuring the latent state is equivariant. These works also use the previous hidden state as a prior for modelling object consistency between consecutive time-steps. The reviewer understands that the proposed work attempts to model the factorization in state space models, whereas the related work mentioned by the reviewer is within attention augmented LSTMs/GRUs.

Please refer to weakness section.

### Questions
- The SCOFF [1] and Neural Production Systems work [2] is very relevant. These works also proposed the idea of factorizing the latent state and ensuring the latent state is equivariant. These works also use the previous hidden state as a prior for modelling object consistency between consecutive time-steps. The reviewer understands that the proposed work attempts to model the factorization in state space models, whereas the related work mentioned by the reviewer is within attention augmented LSTMs/GRUs.

Please refer to weakness section.

[1] https://arxiv.org/abs/2006.16225
[2] https://arxiv.org/abs/2103.01937

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the FACTored State-space (FACTS) framework to address input feature variance by employing a novel memory-input routing mechanism that ensures robust invariance to input permutations. This approach was empirically validated across tasks like multivariate time series forecasting and object-centric world modeling, demonstrating superior or competitive performance in benchmarks, showcasing its effectiveness and robustness in handling diverse input scenarios.

### Strengths
1. The paper addresses the critical challenge of input feature variance, an interesting issue in spatial-temporal learning, by introducing a novel method that utilizes a memory-input routing mechanism. This approach effectively manages the dynamic relationships between input features, ensuring robust modeling even when input orders change.

2. The proposed FACTS model is both simple and highly effective due to its memory-input routing mechanism, which dynamically assigns input features to latent state-space factors. This straightforward approach simplifies handling high-dimensional data and enhances the model's ability to capture temporal and spatial dependencies, making it practical for real-world applications.

3. The authors have conducted extensive experiments across various tasks, including multivariate time series forecasting and object-centric world modeling. These experiments provide strong empirical support for their claims, demonstrating that FACTS consistently outperforms or matches state-of-the-art models. The thorough evaluation across diverse datasets not only highlights the method's versatility but also its robustness in capturing complex temporal dynamics, further validating its effectiveness in real-world scenarios.

### Weaknesses
For the slot dynamics prediction experiment, the method proposed in the paper relies on a pre-trained encoder and is not end-to-end, which may limit its applicability.

### Questions
1. What’s the rationale behind designing selectivity through memory-input routing in the manner presented? Can you provide a more detailed justification for the reasonableness of equations 14 and 15? The current explanation appears overly simplistic and could benefit from a deeper analytical discussion.

2. What is the precise meaning of "permutable state-space memory" in the context of this work?

### Soundness
3

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
4

### Summary
This paper introduces FACTS, a modular or factored SSM model for world modelling applications. FACTS employs an SSM-based recurrent architecture with a permutable memory. This design uses an attention mechanism to dynamically assign input features to latent factors, enabling permutation invariance and efficient long-term prediction.  The experiments show that FACTS demonstrates robust performance on time-series forecasting and object-centric tasks, often outperforming state-of-the-art models.

### Strengths
- The paper is well-written and easy to follow. 
- Modular recurrent architectures are well-studied for world modelling in recent literature, this paper introduces modularity into SSMs while also maintaining their parallel processing capabilities thus the approach seems promising in terms of effeciency.

### Weaknesses
 - One integral component of the model is the attention mechanism which assigns input nodes to latent factors. I believe that similar kinds of attention mechanism for the tasks similar to the ones studied in this paper have  already been explored before in various past works [1, 2, 3]. I wonder if the authors could present a comparison of their method to these approaches or at least highlight the differences. Specifically, [2] proposes to also incorporate modularity and factorization into SSMs, it would be nice to highlight the differences with it and discuss in more detail. 
- The paper says that it is not feasible to compare to other approaches for unsupervised object discovery because of the unique way in which their model works. I would like to point to a few other modular world modelling methods which follow a similar setup as the unsupervised object discovery experiments in the paper which are described in [4]. This work uses a number of metrics which specifically also track moving objects. I wonder if there is any reason for not using the above metrics? Also it would be useful to have even a qualitative comparison to other methods for unsupervised object discovery, currently there is not baseline used for comparison and only two examples are shown for the proposed approach. 

### Questions
- I would like to ask the authors to clarify the difference between slot dynamics prediction and unsupervised object discovery experiments. It seems that slot dynamics prediction adopts the setup from slotformer which first trains a slot attention model and then uses a transformer to predict future slots conditioned on past slots. From my understanding, the proposed FACTS model is used instead of the transformer in slotformer. Considering this setup for the slot dynamics prediction task, I wonder what is different in the unsupervised object discovery ? Is it that both the slot attention module and FACTS model are trained jointly in this case?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors investigated the factorized State Space Model based World Modeling. Different from the previous works, they applied the attention mechanism to extract the factors from the inputs. With this, they can implement the input-order invariant factorized world model. Additionally, they also showed their modeling could be learned in parallel, so it doesn’t reduce the efficiency from other SSMs. They empirically analyzed their modeling on long-term multivariate time-series forecasting (MSTF) tasks and object-centric world modeling problems, and their model showed on par with the state-of-the-art models or better performance than them.

### Strengths
- It is a concrete paper with strong evidences in the theoretical and empirical aspects.
    - They discussed their modeling clearly, especially, showed the theoretical backgrounds and plenty of empirical results.
- It is based on a good motivation, which is to design the factorized world model with the contextually represented factors.
- The experiments are well designed, which is helpful to understand the strengths of their modeling. For instance, in section 4.1.2, they clearly showed the strength of the input invariant factorized world model and in section 4.2, they showed the FACTS performances on the dynamic predictions with the factorized inputs and the factorization performance (Unsupervised object discovery).

### Weaknesses
 - The paper highlights the FACTS can model the consistent factor representation regardless of changes in the spatial or temporal order of input features (e.g., contribution summary in Introduction section). The spatial order change is reasonable and the authors showed it as an experiment in section 4.1.2, but for the temporal order change, it is unclear what it is and why it is important at least for me.
- The interactions between factors are not clearly designed in their modeling, FACTS. The FACTS is to update the hidden with the factors from the inputs through the attention mechanism, but there is not explicitly designed the module or mechanism to learn the interactions between factors.

### Questions
- What is the temporal order change? Is it literally order changing between inputs? Why is it important and why should the world model be invariant for that?
- In your experimental results, it looks like the interactions between factors are considered in your modeling, but it is not explicitly. How are the interactions considered in your modeling?
-  In equation 19, isn’t $X_{t:s}$ $X_{s:t}$? Because $s$ is smaller than $t$. And, $\bar{A}^\times (Z_0, X_{t:s})$ needs to be $\bar{A}_{s+1} \odot \dots \odot \bar{A}_t$?
- And, $\bar{A}^\times (Z_0, X_{t:t})$ looks 1, it needs to be mentioned I think.
- In equations 16-20, the meaning of them is to replace the recurrent attentions to the attentions between the initial state ($Z_0$) and each input $X_t$, as I understand it. I am okay with the equations, but I am not sure intuitively, how it works (how the recurrent attention can be replaced to the dot products of the attentions between initial state and inputs). Can you explain it more how it works and can you compare the parallel and sequential training for simple tasks?
- In table 4, more factors make worse performance even the task is multivariate time-series forecasting. I expected there is a sweet spot. Can you explain it? And can you do this ablation studies for unsupervised object discovery problem? The results from the problem could be clearer (e.g., the MSE will be smallest when the number of factors is same with the number of objects or +1 from that for background).

### Soundness
3

### Presentation
3

### Contribution
3
