# Towards Fast Graph Generation via Autoregressive Filtration Modeling

- Decision: Reject
- Scores: 5, 5, 3, 5, 6, 6, 8

## Abstract
Graph generative models often face a critical trade-off between learning complex distributions and achieving fast generation speed. We introduce Autoregressive Filtration Modeling (AFM), a novel approach that addresses both challenges. AFM leverages filtration, a concept from topological data analysis, to transform graphs into short sequences of monotonically increasing subgraphs. This enables a structured autoregressive generation process, contrasting with the stochastic trajectories of diffusion models. We propose a novel autoregressive graph mixer model to learn this filtration process, coupled with a noise augmentation strategy to mitigate exposure bias and a reinforcement learning approach to refine the generative model. Extensive experiments on diverse synthetic and real-world datasets demonstrate AFM's superior performance compared to existing autoregressive models. Additionally, AFM achieves a 100-fold speedup in generation time compared to state-of-the-art diffusion models while maintaining the quality of generated graphs. This work represents a significant advancement towards high-throughput graph generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an Autoregressive Filtration Modeling (AFM) approach for graph generation, utilizing filtration to transform graphs into sequences of progressively denser subgraphs. The proposed filtration function, based on graph topology, enables a structured autoregressive generation process. This approach employs a two-stage training framework with several strategies to refine the generative model, achieving faster generation than existing autoregressive models.

### Strengths
1. The presentation is organized.
2. The paper introduces noise augmentation and reinforcement learning approach, reducing the model's exposure bias, which is common in autoregressive models.
3. The ablation studies are comprehensive. The ablations reveal the importance of noise augmentation and adversarial fine-tuning and demonstrate the effect of the different filtration function.

### Weaknesses
1. A comparative analysis with other approaches, such as the autoregressive model by Kong et al. (2023) and the EDGE graph diffusion model by Chen et al. (2023), would be helpful. Specifically, a direct comparison on the same datasets, using identical evaluation metrics, would provide a clearer picture of the proposed method's strengths and weaknesses relative to existing state-of-the-art techniques. The absence of such a comparison makes it difficult to assess the true novelty and performance gains of the proposed approach.
2. An analysis on the impact of filtration steps is missing; it would be insightful to see how generation quality changes as the number of filtration steps varies. It's crucial to understand the trade-off between the number of steps and the quality of the generated graphs. For instance, does increasing the number of filtration steps beyond a certain point lead to diminishing returns or even a degradation in performance? This analysis is essential for determining the optimal configuration of the model.
3. Another potential limitation, as acknowledged by the authors, is that the current filtration function design primarily considers the graph’s topology, which may not fully satisfy structural consistency for attributed graphs. The lack of explicit mechanisms to handle node and edge attributes could limit the applicability of this approach to real-world graphs, where attributes often carry crucial information. Exploring ways to incorporate attribute information, such as node features and edge labels, is essential for broader applicability.

### Questions
Q1: Have you explored how varying the number of filtration steps might impact generation quality, especially on larger and more complex graphs? It would be helpful to understand if fewer filtration steps lead to notable quality degradation or if additional steps have limited benefit.

Q2: Given that the experiments were conducted on graphs with up to 500 nodes, have you considered evaluating the model’s performance on larger, real-world datasets? It would be interesting to see how well the approach performs on larger graphs, such as Cora, Citeseer, or Polblogs (with over 1000 nodes). It could provide valuable insights into the model’s feasibility for high-throughput, large-scale applications.

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
The AFM utilizes graph filtration to determine a generation sequence that guides the graph generation process. In addition, a data augmentation technique based on edge perturbation, alongside an adversarial fine-tuning module, has been developed to address the problem of exposure bias associated with teacher-forcing methods. The efficiency of the proposed model compared to diffusion models has been demonstrated through numerical results.

### Strengths
1. The use of graph filtration in designing generation sequences for graph generation shows great promise. 
2. The proposed model demonstrates significant efficiency advantages compared to diffusion models. 
3. The paper is well-organized and clearly presented, making it easy for readers to understand.

### Weaknesses
1. The key contribution of this work lies in graph filtration and filtration sequences. While the paper clarifies how graph filtration is used to generate training samples in the form of generation sequences, and discusses the motivation behind the proposed three filtration functions and three filtration schedule sequences, it is still unclear why these filtration sequences benefit the step-by-step graph generation compared to other possible sequences. For instance, in another paper [1], the authors design a generation sequence for each graph as well. Although their task may differ slightly, as they define a pair consisting of a source graph and a target graph, they identify the "shortest" generation sequence necessary to synthesize a graph, where the concept of shortest "edit distance" justifies their generation sequences. 
Additionally, if any theoretical guarantees regarding the rationale of the filtration sequences exist, they would significantly strengthen the justification for the use of graph filtration in graph generation. The results in the ablation studies section (Table 4) raise further concerns; specifically, the performance of "Stage I w/o Noise" appears to be not good, suggesting that the filtration sequences may not enhance performance. It seems that the randomness of perturbed generation sequences is what leads to improved outcomes. If I have misunderstood any aspect, please provide clarification.

2. The diversity of baselines is limited. The baselines include only two auto-regressive models, two diffusion models, and 1 GAN method. There is a lack of representation of other general graph generation models, particularly those related to normalizing flows and variational autoencoders, which restricts the completeness of the quantitative experiments. Moreover, since the authors aim to highlight the superiority of AFM over diffusion models, simply including two diffusion models as comparisons is insufficient. I recommend considering additional diffusion models (e.g., low-rank diffusion models) as competitors, as suggested in paper [2].

3. In terms of running time, AFMs only outperform diffusion models. However, the efficiency difference between AFMs and GRAN (another autoregressive model) is minimal, which negatively influences the significance of the work. Aside from running time, the experiments do not provide clear evidence that AFMs perform better than the baseline models.

### Questions
1. I strongly recommend that the authors include a paragraph analyzing the time complexity of AFM and diffusion models in depth. Otherwise, the empirical running time alone does not convincingly support the claim of superior efficiency of AFMs. 

2. Additionally, the introduction of extra hyperparameters, such as T, K, gamma(t), and lambda_t, complicates the selection of appropriate hyperparameters for a given dataset. As a solution, an extensive study or guideline for selecting these hyperparameters should be included in the manuscript’s appendix.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an autoregressive based graph generation by sequentially adding edges until the graph is completed. The author uses "graph filtration" to define the autoregressive edge sequence, modeling edge dependency with multivariant bernoulli distribution, adding noise to each next-block prediction task to reduce the exposure bias of autoregressive method, and finally using GAN based adversarial training to further improve the generation quality. Experiments show the speed improvement comparing with diffusion based graph generation, but the performance is not improved much. The author also discussed the limitations of the proposed method, such as not supporting general attributed graphs with node labels and edge labels.

### Strengths
1. The direction of autoregressive graph generation is important given its superior speed to diffusion models. 
2. The paper contains extensive designs for many issues raised in autoregressive graph generation, such as designing the order, exposure bias, multivariable dependency, and the generator issue caused during iterative generation. 
3. The author discussed their method's limitation in detail, which helps to clarify several important questions.

### Weaknesses
1. Some part of the method is not clear or containing error:     

* eq. 7 left side is conditional on t+1 to T steps, which is not correct. 
* while figure 1 shows the illustration of training procedures, the generation procedure is not mentioned, as well as the detailed setting of the generator during GAN training. 

2. Some part of design is not efficient: 
* the mixer architecture design uses too many representations: T x N with N being the total number of nodes. This can cause significantly increased memory requirement.  
* many designs are not general, such as not supporting attributed graphs with node labels and edge labels, which are well supported by diffusion models and traditional AR graph generation methods. 

3.  The designed method is a bit complicated: with many designs in autoregressive part, and additional adversarial training for further performance improvement. However, when comparing to baselines, I cannot find consistent and noticeable performance improvement, although the method is faster than diffusions. 

4. The author miss some important and highly related references and baselines, such as the [1]. They share many common parts and should be discussed. 

5. Limited experiments: only simple and small simulation graphs.

### Questions
Except these weakness, can you provide some possibilities of extending the current method to attributed graphs? 
If it cannot show its application to graphs like molecules, the usage and scope of the proposed method is very limited.

### Soundness
1

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
This paper introduces an efficient autoregressive graph generation algorithm that leverages filtration to decompose graphs into ordered sequences of nested subgraphs each consisting of a subset of edges from the original graph. The paper explores different filtration functions and a filtration schedule sequence. The generation process first inverses the filtration process and learns the parameters of structural mixing and temporal mixing networks in a teacher-forcing fashion. Then, in the second stage, adversarial fine-tuning with reinforcement learning is employed to mitigate exposure bias of the AR process. Additionally, it uses noise augmentation to further mitigate exposure bias by randomly perturbing edges of intermediate graphs during the first stage of training. This results in speedup in the graph sampling from the proposed AR model.

### Strengths
- The paper proposes a novel autoregressive graph generation based on filtration and employs various techniques to improve generation performance. 
- The graph generation idea is sound and appealing.
- The paper is well-written and provides clear justification for the core elements of the proposed graph generative process, including using adversarial fine-tuning, noise augmentation, filtration functions and filtration scheduling.

### Weaknesses
1. **Lack of Complexity Analysis**: While the paper mentions that the drawback of the available diffusion and AR models is that “their quadratic or higher computational complexity with respect to the number of nodes” (which is not exact), it does not provide complexity analysis which is crucial for such work. A section or table comparing the training and sampling complexity with baseline models is recommended. Specifically, the paper should analyze the time complexity with respect to the number of nodes $N$ and the number of filtration steps $T$. The current analysis is insufficient to understand the computational bottlenecks and scalability of the proposed approach. Regarding non-monotonic graph sequences, the complexity will increase quadratically if the algorithm needs to decide on all the possible edges rather than just adding new subsets to the existing ones.
2. While the main part of the paper is discussing the filtration process, but the ablation shows that many tricks, including noisy edge augmentation, stochastic perturbations to node orderings, and Adversarial Fine-tuning with RL, are crucial to the overall graph sampling performance and AR graph generation based on filtering, without these additions performs worse than other AR-based baselines such as GRAN. So, the effect of such techniques on other AR-based models is recommended to be investigated for a fair comparison. It is unclear if the performance gains are due to the filtration method itself or these additional techniques. A more controlled study is needed to isolate the impact of each component.
3. **Missing Citation and Comparison**: The paper lacks citations and comparisons to several relevant graph generation models. For example, HiGen also offers a scalable hierarchical graph generation in autoregressive manner in a sequence of coarse to fine subgraphs which captures multi-scale properties of the graph. Also other graph diffusion models such as GDSS [2] and EDGE [3] are not cited.
4. **Insufficient Empirical Studies**: The experiments presented are not sufficient to fully demonstrate the capabilities of the proposed model. In many cases, the performance of AFM falls short compared to diffusion models and sometimes even AR counterparts.  
   - a. While this paper claims to improve efficiency, it lacks experiments for large graphs (graphs with >1k ). Evaluating the performance on larger graphs is crucial to assess its scalability.  
   - b. The method can provide a trade-off between expressiveness and efficiency. Investigating how a larger sequence of subgraphs affects performance and determining the optimal sequence length particularly for large graphs would be valuable. The paper should explore the impact of varying the number of filtration steps $T$ on both the quality of generated graphs and the computational cost.
5. The choice of filtration function may affect the scheduling method. Also, An analysis of different scheduling methods with various filtration functions is recommended to understand their interplay. The paper should investigate how different combinations of filtration functions and scheduling methods affect the performance and provide guidelines for choosing appropriate combinations.
6. One potential limitation of this approach is its edge independence [4]. The proposed method's approach of adding many edges simultaneously could lead to the edge-independence issue. The paper should address the potential for edge independence and discuss how the model mitigates this issue, or if it is a limitation.
7. More clarification is needed regarding the adversarial fine-tuning with RL. The reward used in PPO should be specified, and the figure illustrating the process needs clarification. Additionally, a more detailed explanation of the "TRAINGENERATORANDVALUEMODEL" pseudo-code is necessary for better understanding.

### Questions
1. The proposed method learns the joint likelihood of the sequence (equation 4). However, graph generative models aim to learn $P_{\theta}(G_T)$. The paper should clarify the relationship between these two, especially considering the use of noise augmentation and multiple trajectories in the training set.
2. What are the training complexity and sampling complexity of the proposed model?
3. AR models' sensitivity to node ordering is a known drawback, is the proposed AFM order equivariant? While the paper mentions that the proposed AFM depends on the choice of edge ordering, this point requires additional clarification and empirical experimentation. 
4. Since the line Fiedler function outperforms the other two options and is preferred in your experiments, then does it infer that structural consistency is prioritized? How does it affect the graph generation?
5. In Page 1, line 48 needs a citation.  



Conclusion:

While the proposed idea is very appealing, and I acknowledge its potential impact, I am not sure that the paper is ready for ICLR and as impactful as it could be in its current form. Therefore, I am hesitant to support acceptance but I am willing to reconsider my score if my concerns and questions are addressed.


References:  
[1] M. Karami, “HiGen: Hierarchical Graph Generative Networks”, International Conference on Learning Representations, 2024.  
[2] Jaehyeong Jo, Seul Lee, and Sung Ju Hwang. Score-based generative modeling of graphs via the system of stochastic differential equations. In International Conference on Machine Learning, pp. 10362–10383. PMLR, 2022.  
[3] Xiaohui Chen, Jiaxing He, Xu Han, and Li-Ping Liu. Efficient and degree-guided graph generation via discrete diffusion modeling. arXiv preprint arXiv:2305.04111, 2023.  
[4] Sudhanshu Chanpuriya, Cameron Musco, Konstantinos Sotiropoulos, and Charalampos Tsourakakis. On the power of edge independent graph models. Advances in Neural Information Processing Systems, 34: 24418–24429, 2021.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Autoregressive Filtration Modeling (AFM), a new method for graph generation. AFM transforms graphs into sequences of monotonically increasing subgraphs. It incorporates an autoregressive graph mixer, noise augmentation to reduce exposure bias, and reinforcement learning for refining the model.

### Strengths
S1: Improving the efficiency of graph generation is an interesting research direction of practical importance. 

S2: The proposed mixture-of-Bernoullis component enhances the expressiveness of the generative model. 

S3: The proposed adversarial finetuning method significantly boosts the fidelity of generated graphs. 

S4: The authors clearly disclosed experimental details to facilitate reproducibility.

### Weaknesses
W1: The motivation is inconsistent with the proposed method. Section 3.1 states that a filtration has G_t ⊇ G_{t-1}. However, the proposed method in Section 3.2 both add and delete edges, which violates the definition of a filtration. It is more like a diffusion model except that they replace p(G_t|G_{t-1}) with p(G_t|G_{t-1},...,G_0). The objective function looks the same as that of DiGress (a diffusion model). Hence, it might make more sense if the authors motivate the proposed method from a diffusion model perspective instead of a filtration perspective. The use of the term 'filtration' is misleading, as the method does not adhere to the core property of monotonic subgraph inclusion. The noise augmentation process, which randomly adds and deletes edges, fundamentally alters the structure and invalidates the filtration property. This makes the connection to filtration theory tenuous and weakens the theoretical grounding of the approach.

W2: The experimental results are not presented in a very meaningful manner. It seems that the speedup comes mainly from the small number of steps (i.e., T) of the proposed method AFM. For example, on the Expanded Lobster dataset, DiGress runs 1000 steps for 4.86 sec and achieves VUN=96.58 while the proposed AFM runs 30 steps for 0.03 sec but achieves only VUN=79.10. Thus, directly comparing them does not provide much information. To provide a more meaningful comparison, the authors can plot a VUN-vs-time curve for each method (by varying T) and compare these curves instead. The current comparison obscures the trade-off between generation quality and computational cost, making it difficult to assess the true practical value of the proposed method. A more comprehensive analysis should explore the performance of both AFM and baseline methods across a range of time steps to reveal their efficiency-quality trade-off curves.

W3: The time complexity of autoregressive generation is O(T^2). Thus, it might be inefficient if we seek to increase the generation quality by increasing T. This quadratic time complexity could become a significant bottleneck for large graphs or when high generation quality is required, limiting the scalability of the method. The authors should provide a more detailed analysis of the computational cost associated with increasing T, especially in the context of large-scale graph generation tasks.

W4: The ablation studies are a bit insufficient. The authors did not report the performence of using only stage II (i.e., no stage I). Thus, it is unclear how effective the proposed stage I is. Besides that, the authors did not provide ablation studies on performance vs K. The lack of ablation studies for stage I makes it difficult to assess the contribution of the initial training phase. It is unclear if the performance gains are primarily due to the adversarial finetuning or if the proposed filtration-based training is essential. Furthermore, the absence of an ablation study on the parameter K, which controls the mixture of Bernoulli distributions, makes it difficult to understand the sensitivity of the method to this hyperparameter.

W5: The comparison is a bit unfair. As the proposed adversarial finetuning (AF) is orthogonal to the generative model, comparing the proposed method with AF and baseline methods without AF is not an apple-to-apple comparison. The use of adversarial finetuning as a post-processing step introduces a confounding factor in the comparison. It is unclear whether the performance gains are due to the proposed method itself or the adversarial finetuning. A more rigorous comparison would involve applying adversarial finetuning to all baseline methods to ensure a fair evaluation.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Autoregressive Filtration Modeling (AFM), a novel approach to graph generation that leverages the concept of graph filtration from topological data analysis. AFM transforms a graph into a sequence of nested subgraphs, enabling a structured and efficient autoregressive graph generation process. The method integrates noise augmentation and adversarial fine-tuning with reinforcement learning to address challenges like exposure bias.

### Strengths
- The application of graph filtration for graph generation is a novel and unique contribution, moving beyond existing approaches like diffusion models and node/edge-addition methods.
- The integration of reinforcement learning for adversarial fine-tuning further distinguishes AFM from other autoregressive methods.

### Weaknesses
 - The multi-step approach (including filtration, autoregressive modeling, noise augmentation, and adversarial fine-tuning) may be challenging to implement and tune, particularly for practitioners.
- The focus on non-attributed graphs limits the model’s applicability to scenarios involving node or edge labels, a common requirement in many practical applications.
- The paper can be better motivated by stating why there is a need for graph generation algorithms especially for high-throughput applications. And also why is graph generation important. These are missing in the introduction.
- The experimental results, among all, do not stand out the superiority of the proposed method against baselines.

### Questions
- How could AFM be extended to handle node or edge attributes? Are there plans to address this limitation in future work?
- How to extend AFM to work on directed graphs? 
- Can we solve the problem of high computational complexity of previous autoregressive and diffusion models with distributed computing resources?
- Please justify why diversity and structural consistency are important for filtration function?
- What is $f_\text{remote}$ in line 200?
- What does 'appropriate edges' in line 292 refer to?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 7

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes AFM, a methodology to use filtration sequences to generate graphs autoregressively using parts of subgraphs. Compared with existing methods, the proposed AFM achieves much faster graph generation with similar and competitive performance.

### Strengths
1. The paper is well-written, easy to follow and understand. Specifically, the related work section is well-structured, covering the most relevant and important research works in graph generation.

2. The authors tried three different schedule functions: linear, convex, and concave, to better control the graph generation process. Experiments with different schedule functions showcase that each can perform better than others in terms of specific metrics.

3. The running speed of the proposed AFM method is impressive, with competitive performance in terms of various metrics compared to other baselines.

4. The ablation study showcases the importance of noise augmentation.

### Weaknesses
1. The authors made the assumption that only connected graphs are presented in the model during training. However, I am slightly concerned that this assumption might be too strong, which could limit the applicability of the proposed AFM method in generating certain real-world graphs.

2.The baselines that the authors compared with in Section 4.2 (expanded synthetic datasets) and Section 4.3 (real-world datasets) are too few. Comparison with more baselines could better showcase the proposed method.

### Questions
1. For the filtration function, the authors chose the line Fiedler function $f_{Fiedler}$, which is the second smallest eigenvector of the symmetrically normalized Laplacian of the line graph $L(G)$. Is there any good theoretical or at least intuitive explanation as to why this $f_{Fiedler}$ might perform well?

2. I am a bit curious about the scalability of the proposed method in terms of the size of the graph it can generate. How does the runtime of the AFM method change as the graph size N increases?

### Soundness
3

### Presentation
3

### Contribution
3
