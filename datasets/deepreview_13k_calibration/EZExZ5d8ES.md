# Dynamic Mixture-of-Experts for Incremental Graph Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
Graph incremental learning is a learning paradigm that aims to adapt models trained on previous data to continuously incremented data or tasks over time without the need for retraining on the full dataset. However, regular graph machine learning methods suffer from catastrophic forgetting when applied to incremental learning settings, where previously learned knowledge is overridden by new knowledge. Previous approaches have tried to address this by treating the previously trained model as an inseparable unit and using regularization, experience replay, and parameter isolation to maintain old behaviors while learning new knowledge.
These approaches, however, do not account for the fact that not all previously acquired knowledge is equally beneficial for learning new tasks, and maintaining all previous knowledge and the latest knowledge in a single model is ineffective. Some prior patterns can be transferred to help learn new data, while others may deviate from the new data distribution and be detrimental. To address this, we propose a dynamic mixture-of-experts (DyMoE) approach for incremental learning. Specifically, a DyMoE GNN layer adds new expert networks specialized in modeling the incoming data blocks. We design a customized regularization loss that utilizes data sequence information so existing experts can maintain their ability to solve old tasks while helping the new expert learn the new data effectively. As the number of data blocks grows over time, the computational cost of the full mixture-of-experts (MoE) model increases. To address this, we introduce a sparse MoE approach, where only the top-$k$ most relevant experts make predictions, significantly reducing the computation time. Our model achieved 5.47\% relative accuracy increase compared to the best baselines on class incremental learning with minimal computation increase, showing the model's exceptional power.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a Dynamic Mixture-of-Experts (DyMoE) approach for graph incremental learning, utilizing specialized expert networks for incoming data blocks. It introduces a customized regularization loss to help existing experts retain performance on old tasks while supporting new learning. Additionally, a sparse MoE model is developed to reduce computational costs by using only the most relevant experts for predictions.

### Strengths
1.	This paper introduces a Dynamic Mixture-of-Expert (DyMoE) module with separate experts for each data block, allowing dynamic relevance-based information synthesis.
2.	This paper proposes a block-guided loss function to minimize negative interference among experts, reducing catastrophic forgetting.
3.	This paper integrates the DyMoE module into GNN layers to effectively handle data shifts in continual graph learning.
4.	This paper develops a sparse DyMoE variant that focuses on the most relevant experts, enhancing efficiency while maintaining accuracy.

### Weaknesses
1.	In real-world applications, how do the dynamic changes in graph structures and data blocks affect the model's performance? Have you considered the impact of data noise and outliers on the results? Specifically, how does the model perform when faced with significant shifts in node degree distributions or the emergence of entirely new graph substructures within incoming data blocks? The paper should also address the robustness of the proposed method to noisy labels or the presence of adversarial examples, which are common in real-world graph datasets.
2.	Experiments:
1)	The MoE structure increases the number of parameters in the model, thereby enhancing its capability. In contrast, the parameter count of the baseline model is not specifically mentioned. Does this represent an unfair comparison? The paper needs to provide a detailed analysis of the parameter counts for both the DyMoE model and the baseline models, ensuring a fair comparison. It is crucial to evaluate the performance of the baseline models with a similar parameter budget to the proposed method to isolate the effect of the DyMoE architecture.
2)	This paper mentions "with minimal computation increase," but it seems insufficient experimental or theoretical evidence is provided. Could there be a comparison of throughput? The paper should include a thorough analysis of the computational overhead introduced by the DyMoE module, including both training and inference time. A comparison of throughput (e.g., samples processed per second) with baseline methods would be beneficial to validate the claim of minimal computational increase. This should also include a breakdown of the time spent on different parts of the model, such as expert selection and forward passes.
3)	The paper claims that this method can handle topological and contextual changes, but how is this topological change quantified and assessed? Understanding the extent and nature of these changes is crucial for evaluating the effectiveness of the proposed approach. There are no experiments to address this problem. The paper needs to define specific metrics to quantify the topological changes in the graph structure across different data blocks. For example, changes in graph diameter, average path length, or clustering coefficient could be used to characterize the structural shifts. Experiments should be designed to evaluate the model's performance under varying degrees of topological change, providing a more comprehensive understanding of its capabilities.

### Questions
1. How do the dynamic changes in graph structures and data blocks affect the model's performance? Have you considered the impact of data noise and outliers on the results?

2. Enhance experiments and analysis.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a dynamic mixture-of-expert (DyMoE) model for graph incremental learning. Specifically, DyMoE uses separate expert networks to model different data blocks. When a new data block arrives, it learns a new expert without modifying previously learned experts.  In addition to the conventional MoE loss, DyMoE introduces a block-guided regularisation loss to correctly assign experts for different data blocks. To improve the efficiency of the DyMoE model, the paper also proposes a sparse DyMoE model, where instead of fusing the predictions from all the expert networks, it only uses the top-K most relevant experts to make predictions.

### Strengths
The paper is easy to follow. The idea of using the MoE model to address graph incremental learning is novel and interesting. Experimental results on six graph incremental learning datasets demonstrate the effectiveness of the proposed DyMoE model and the block-guided regularisation loss. The results also indicate the DyMoE model can learn dedicated experts for different data blocks.

### Weaknesses
1. Theorem 1 is established under the assumption that the data follow a Gaussian mixture distribution, and this assumption should be explicitly stated in the theorem to make it more precise. Can this theorem extend to data following distributions other than the Gaussian mixture distribution?

2. The details of the data balancing training procedure (line 297-301) is not very clear from the paper. Specifically, how to select the memory set for the new data block? Does this training procedure use both $L_{cls}$ and $L_{BL}$ loss?

3. There are several missing details in the experimental setups that should be clarified: 

(1) The number of nodes and edges per data block is not provided in Table 8. Moreover, the paper only introduces how to split the data into different blocks in Appendix C.2. However, it is unclear how to obtain the training, validation and test sets in each block. 

(2) It is unclear which GNN model was used in the experiments, and whether the same GNN model was applied to the baseline models. 

(3) Details of the evaluation metrics are missing, including how each metric is calculated. 

4. The analysis of the results is inaccurate and unconvincing in some cases: 

(1) In line 429, the paper states that “we can see our method significantly improves over existing baselines for both AA and AF”. However, this is inaccurate since the performance of DyMoE (57.85) is actually worse than the baseline PI-GNN (59.18) on DBLP in terms of AA. 

(2) In line 430, the paper states that “We reach an average of 5.47% improvement in AA and 34.64% reduction in AF”. However, it didn’t specify which model these improvements are compared to. 

(3) The results in Table 1 and Table 2 indicate that the proposed DyMoE model performs worse than baselines on the DBLP and Arxiv in terms of AA. However, the paper lacks analysis to explain this result. 

(4) I also have some concerns regarding the efficiency experiments. In table 3, the paper provides the training time of DyMoE and three baselines: Finetune, ER-GNN and Retrain. In table 5, the paper only compares DyMoE and ER-GNN in terms of inference time. It is unclear why the paper only compares these three baselines instead of the more effective baseline C-GNN. Moreover, the results in table 5 show that the inference time of DyMoE is worse than ER-GNN, which indicates that the proposed DyMoE model actually cannot achieve good performance while maintaining good efficiency. 

(5) In table 4, I don’t think the comparison between Full and the other variants is fair given that all the other variants are based on the sparse model. Comparing the results of Sparse and w/o DB, w/o BL, w/o Dy, the statement that “we see performance drop whenever a component is missing from the model, validating the importance of each component” is not very accurate as the performance of w/o Dy (92.09) is better than Sparse (91.57) on Reddit in terms of AA and the performance of w/o DB (83.09) is better than Sparse (82.93) on Paper100M in terms of AA. 

5. The effect of the hyperparameter $K$ in the sparse model is not investigated. 

6. The code is not available, which makes it difficult to reproduce the results given that a lot of experimental details are missing.

### Questions
1. Can Theorem 1 extend to data following distributions other than Guassian mixture distribution?
2. In the efficiency analysis, why not report the training and inference runtime of more effective baselines such as C-GNN?
3. The proposed DyMoE learns a new expert when a new data block arrives. This requires prior knowledge of which data belong to different blocks and a sufficient amount of data in each block to effectively learn a new expert. This assumption may present challenges in real-world incremental learning applications, where data blocks are not predefined or large enough for expert learning.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a Dynamic Mixture-of-Experts (DyMoE) framework to address the challenge of catastrophic forgetting in dynamic graphs for incremental graph learning. The DyMoE framework introduces a novel approach by dynamically adding specialized expert networks for each incoming data block. These expert networks are used selectively through a gating mechanism, which determines the relevance of each expert based on the input data.

### Strengths
1. The paper identified the issue of existing continual learning methods that ignore the correlation between different data blocks.
2. The paper tackled a significant dynamic graph problem in real-world scenarios, where data arrives incrementally, offering a scalable solution without the need for full dataset retraining.
3. The paper developed a DyMoE module with specialized experts for each data block and introduced a data block-guided loss to reduce negative interference among the experts.

### Weaknesses
1. The use of symbols is inconsistent, and the explanations lack clarity. Specifically:

   (a) What do m and n represent in Eq. (3)? Are they referring to the feature dimension or the number of nodes? 

   (b) In Eq. (13), what is the specific meaning of y? Does it convey the same meaning as h?

   (c) In Figure 1, triangles are used on the left and circles on the bottom right to represent blocks.

The authors can include a notation table or provide more explicit definitions for each symbol when first introduced.

2. The baseline methods used in the experiment mainly come from older works, with only one baseline in recent 3 years. State-of-the-art approaches, such as MSCGL [1], RLC-CN [2], SEM [3], and UGCL [4], would have provided a more comprehensive evaluation. Can you justify the choice of baselines if more recent methods were intentionally excluded? 

   [1] J. Cai, X. Wang, C. Guan, Y. Tang, J. Xu, B. Zhong, and W. Zhu, ''Multimodal continual graph learning with neural architecture
       search,'' in Proceedings of the ACM Web Conference, 2022, pp.1292–1300.    

   [2] A. Rakaraddi, L. Siew Kei, M. Pratama, and M. De Carvalho, ''Reinforced continual learning for graphs,'' in Proceedings of the
       31st ACM International Conference on Information & Knowledge Management, 2022, pp. 1666–1674.   

   [3] Zhang, Xikun, Dongjin Song, and Dacheng Tao. ''Ricci curvature-based graph sparsification for continual graph representation 
   learning,'' IEEE Transactions on Neural Networks and Learning Systems (2023).

   [4] T. D. Hoang, D. V. Tung, D.-H. Nguyen, B.-S. Nguyen, H. H.Nguyen, and H. Le, ''Universal graph continual learning,'' Transactions 
   on Machine Learning Research, 2023.

3. In line 255, ''Figure 6 shows that direct training will not result in specialized experts'' seems confusing, can you explain it more clearly?

4. In Section 3.3, it’s unclear how to tweak the gating values during training randomly so all experts have similar selection chances. What is the magnitude of the tweaks, or can you give a mathematical formulation of how the randomization is applied?

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a Dynamic Mixture-of-Experts (DyMoE) framework for incremental graph learning, aiming to address catastrophic forgetting in graph neural networks (GNNs) when new data arrives sequentially. Unlike traditional approaches that treat prior knowledge uniformly, DyMoE dynamically adds specialized expert networks to handle each new data block, optimizing the reuse of relevant information. To reduce computational demands, the authors introduce a sparse DyMoE variant that selectively activates only the top-k experts for predictions. DyMoE achieves a notable improvement in accuracy with minimal computational overhead, making it an effective solution for class and instance incremental learning settings.

### Strengths
- the studied problem is important and interesting. It deserves more attention
- the proposed method and identified problem, despite not being very novel, is sound to some extend.

### Weaknesses
 - the identified problem and the proposed method are not novel.

  a. the correlation induced by the dependency of graph data was previously introduced (e.g., see [1,2]), rendering continual learning on graph data is different from other i.i.d data 

  b. applying the MoE model to continual learning seems to be a common combination (e.g., see [3,4]). I certainly agree with the fact that in different settings (especially under graph data), such a combination might require different considerations and tailored designs. However, in the current version of the paper, I fail to understand what are the unique problems for applying such a combination in the studied setting in the paper.

- the effectiveness of the method needs further support

  a. I agree with the intuition that a separate expert network can better store/memorize information for each task. However, it comes with two natural questions: 1) what happens to the parameter complexity (overall model size) when the data stream is large and 2) how effective is this approach for parameter/information sharing among tasks (otherwise, why not train a separate network for each task)

  b. It is not clear why the gating mechanism in MoE is effective in addressing catastrophic forgetting. In the graph data case, as shown in [1,2], the correlation/dependence among data can induce a distribution shift and can render the problem unlearnable. Why the (proposed) gating mechanism can address this? Furthermore, even in the case of i.i.d data, it is still not clear to me why the gating mechanism does not suffer from catastrophic forgetting (e.g., forget how to router the decision for the previous task).  

- the theoretical result is not rigorous and clear, and it is not connected well to support the proposed method

  a. First, it is not clear what $\mathcal{L}(Dy)$ and $\mathcal{L}(PI)$ are exactly. Assuming the loss function is the one given by (10), the loss function would have a dependency on the $\beta$ which is not reflected in the theorem statement.

  b. There are many cases, where the theoretical result does not add any value. For example, in the case of separable data, it can be shown that with enough model parameters, there exists a model parameter that can achieve zero loss. In this case, the other side of the result is also true, i.e., $\mathcal{L}(PI) \leq \mathcal{L}(Dy)$. Furthermore, the result is about existence. It does not tell us much about how difficult to find such a parameter.

  c. The theorem statement tells us that it is possible for the proposed method to achieve a smaller loss value (with respect to the proposed objective) compared to the parameter isolation. It needs further argument why the proposed training objective is the best/very reasonable for measuring model performance. what happens if the objective is switched to the one used in $\mathcal{L}(PI)$ paper? How does this training loss connect with the generalization performance (what we actually care)?

- the experimental studies have some questions as well

  a. (minor) The selected baselines seem to be a bit outdated 

  b. (major) The performance of the baseline method seems to be much lower than the one presented in the benchmark study[5]. What are the reasons behind this?

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
1
