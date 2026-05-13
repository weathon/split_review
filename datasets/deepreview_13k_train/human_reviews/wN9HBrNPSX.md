# Enhancing Temporal Knowledge Graph Completion with Global Similarity and Weighted Sampling

- Decision: Reject
- Scores: 6, 5, 3, 6

## Abstract
Temporal Knowledge Graph (TKG) completion models traditionally assume access to the entire graph during training. This overlooks challenges stemming from the evolving nature of TKGs, such as: (i) the model's requirement to generalize and assimilate new knowledge, and (ii) the task of managing new or unseen entities that often have sparse connections. In this paper, we present an incremental training framework specifically designed for TKGs, aiming to address entities that are either not observed during training or have sparse connections. Our approach combines a model-agnostic enhancement layer with a weighted sampling strategy, that can be augmented to and improve any existing TKG completion method. The enhancement layer leverages a broader, global definition of entity similarity, moving beyond mere local neighborhood proximity of GNN-based methods. The weighted sampling strategy employed in training accentuates edges linked to infrequently occurring entities. Our evaluations, conducted on two benchmark datasets, demonstrate that our framework outperforms existing methods in overall link prediction, inductive link prediction, and in addressing long-tail entities. Notably, our method achieves a 10\% improvement in MRR for one dataset and a 15\% boost for another. The results underscore the potential of our approach in mitigating catastrophic forgetting and enhancing the robustness of TKG completion methods, especially in an incremental training context.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper is about the temporal knowledge graph completion problem and its challenges. Models proposed to solve this problem need to take into consideration the requirement for generalization and assimilation to new knowledge, and the sparseness or connection between newly introduced entities. To overcome these challenges, the authors propose an incremental training framework specifically designed for temporal knowledge graphs, a unique enhancement layer that can be integrated with various GNN-based temporal knowledge graph completion methods, and a weighted sampling strategy during the training process which emphasizes the connections of infrequent entities. The experimental setup contains two versions of ICEWS datasets, link prediction tasks (overall, inductive), hit@k and MRR evaluation metrics, and the comparison methods that include the baseline model (Titer) with three variations (FT, ER, EWC) and three proposed variations (weighted sampling, enhancement layer, full). The results show the overall improvement in the model when utilizing the proposed enhancement layer and the proposed weighted sampling.

### Strengths
1) The paper is about an interesting topic (TKG completion task). The authors highlight the challenges in this topic and provide with proposed solutions that can be adapted in existing TKG completion models.
2) The results show the performance improvement when adding the proposed layer and sampling.
3) The paper is well-written and well-structured. The authors have done a great job to describe the area of research, its limitations, provide the related works, give solutions for each limitation and support the proposed methodology with experiments around three research questions.

### Weaknesses
1) The proposed methodology is incremental. The proposed layer and sampling are extensions to an existing model, Titer. While this demonstrates applicability, it raises questions about the generalizability and novelty of the core contribution. The reliance on Titer as a foundation might limit the scope of the method's impact.

2) It would be useful if the authors could add other state of the art models (from their related work) to the comparison models. The experiments would be more convincing and would make a stronger point if the authors could show how the proposed methodology can be added in other models too, and to be able to see the performance of other models with the proposed extensions. Specifically, incorporating a comparison with at least one other recent, high-performing temporal knowledge graph completion model would significantly strengthen the experimental evaluation. This would provide a more comprehensive understanding of the proposed method's effectiveness relative to the current state of the art.

3) Another useful aspect on the proposed methodology is to add the run times and the time complexities when the layer and the sampling strategy are added. A quantitative analysis of the computational cost introduced by the enhancement layer and weighted sampling would provide valuable insights into the practical trade-offs between performance gains and computational efficiency.

### Questions
The authors can respond to my 2) and 3) comments in the weaknesses section.

Minor comment: In section 5.2, 3rd sentence, the citation was not added/compiled properly on LaTeX.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an incremental training framework for temporal knowledge graphs by incorporating a model-agnostic enhancement layer and a weighted sampling strategy. The authors conduct extensive experiments on the two popular datasets and the results show the effectiveness of the proposed method. The target problem is interesting.

### Strengths
1. The authors conduct extensive experiments on the two popular datasets and the results show the effectiveness of the proposed method. 
2. The paper is well written and the target problem is interesting.

### Weaknesses
1. The motivation is not well established.  It seems that the authors combine the two methods (global similarity and weighted sampling).
2. In Table 1, many various recent works should be considered and discussed:
Xu et al., 2023. Temporal knowledge graph reasoning with historical contrastive learning.
Zhang et al., 2023. Learning Long- and Short-term Representations for Temporal Knowledge Graph Reasoning.
Zhu et al., 2021. Learning from History: Modeling Temporal Knowledge Graphs with Sequential Copy-Generation Networks.

### Questions
1. The motivation is not well established.  It seems that the authors combine the two methods (global similarity and weighted sampling). 
2. In Table 1, many various recent works should be considered and discussed:
Xu et al., 2023. Temporal knowledge graph reasoning with historical contrastive learning.
Zhang et al., 2023. Learning Long- and Short-term Representations for Temporal Knowledge Graph Reasoning.
Zhu et al., 2021. Learning from History: Modeling Temporal Knowledge Graphs with Sequential Copy-Generation Networks.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an incremental training framework for Temporal Knowledge Graph (TKG) completion, addressing the challenges of generalizing new knowledge and managing sparse connections. The framework combines a model-agnostic enhancement layer that leverages global entity similarity and a weighted sampling strategy to improve link prediction and handle long-tail entities.

### Strengths
Clear writing, making it easy to understand the author's ideas.

### Weaknesses
W1. The experimental dataset is very single. ICEWS14 and 18 are only different in years, and the homogeneity is serious. Moreover, the author reconstructed ICEWS without even giving a detailed data description of the new dataset.

W2. The comparison method is single. The author mentioned a lot of related work, but in the end only one method was selected as the basic model for the experiment. Such an experiment does not prove that the enhancement method proposed by the author is universal.

W3. The method is too simple. The global similarity and weighted sampling proposed in the paper are superficial training strategies. There is no in-depth discussion and unique insights into the problem, and there is a lack of breakthrough contributions.

### Questions
Q1. Have you tried experimenting on more TKGs, such as WIKIDATA and GDELT?

Q2. Have you tried more TKGC methods? For example, Cygnet, LCGE?

Q3. Since global similarity is used to enhance the representation of entities, why not just cancel the incremental training setting and train the representations of all entities together from the beginning?

Q4. Generally speaking, incremental training only reduces training costs and should not be more effective than training from scratch. If you want to use incremental training to enhance the effect of TKGC, is this starting point wrong?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In summary, the paper presents an incremental learning approach for TKG completion that incorporates techniques like weighted sampling and a model-agnostic enhancement layer to address challenges of handling unseen and sparsely connected entities in a growing knowledge graph over time. Evaluation on the constructed benchmarks demonstrates the effectiveness of the proposed framework. The paper

### Strengths
1. The paper tackles the relatively new problem of incremental learning for temporal knowledge graph completion, which has practical values in real-world applications, as most real-world knowledge bases must address as data arrives continuously over time.
2.  It proposes a novel model-agnostic enhancement layer that leverages global entity similarity, providing a creative approach beyond local neighborhood proximity used in existing methods.
3. Results demonstrate substantial quantitative gains over baselines, indicating the high technical quality of the proposed framework components.

### Weaknesses
1. Real-world deployment considerations are not discussed. For example, analyzing memory/compute needs and ability to handle streaming data. The paper lacks a discussion on the practical aspects of deploying the proposed model, such as the memory footprint of the model and the computational cost associated with training and inference. Specifically, it would be beneficial to analyze the scalability of the approach with respect to the size of the knowledge graph and the rate at which new data arrives. Furthermore, the paper does not address how the model would handle streaming data, which is a common scenario in real-world applications.
2. While weighted sampling is an intuitive idea, the sampling function used could be further explored and justified. For example, analyzing alternative frequency-based formulas or evaluating sampling directly from a learned importance weighting. The current approach uses a specific inverse frequency-based sampling function, but it is not clear why this particular function was chosen over other alternatives. A more detailed analysis of different sampling functions, such as mean, max, or min inverse frequencies, would strengthen the justification for the chosen approach. Moreover, exploring the possibility of learning importance weights for each entity, rather than relying on a fixed frequency-based approach, could lead to improved performance.

### Questions
1. In Figure 2.a, it seems that the proposed method (Full) is outperformed by the proposed method (Enhancement Layer) on HITS@10, and the proposed method (Full) is outperformed by the proposed method (Weighted Sampling), any insights on that?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
