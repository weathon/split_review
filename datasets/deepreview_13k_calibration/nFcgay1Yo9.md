# Scale-Free Graph-Language Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Graph-language models (GLMs) have shown great potential in graph-based semi-supervised learning. In GLMs, graph generation and text embedding are two key stages, which are typically achieved by inferring a latent graph and finetuning a language model, respectively. However, the former relies on artificial assumptions about the underlying edge distribution, while the latter requires sufficient data annotations. This paper introduces a novel GLM that addresses these two challenges sequentially by leveraging a well-grounded structural prior. Specifically, we explore an inherent nature of real edge distribution—the scale-free property—for graph generation. We unexpectedly reveal that this natural characteristic can be closely approximated by a simple k-nearest neighbor graph. By using this scale-free graph, we subsequently develop a graph-based pseudo-labeler to generate complementary supervision for text embedding. Extensive experiments validate our findings and highlight the potential of GLMs built on scale-free structures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a graph-based method as a semantic complementary supervision for text-attributed graphs. The author first theoretically justifies that a kNN graph can approximately describe a scale-free network while fulfilling three constraints or properties. Based on this, the author proposes a kNN graph construction to initialize the document graph. Then, the author introduces a new iterative method that fuses embeddings from three sources: a pseudo-labeler, GCN embeddings, and text embeddings.

### Strengths
1. The author has focused on a topic with wide applications, going beyond GCN for text-attributed graphs. The proposed method can be applied to any document without explicitly extracting links.
2. This paper theoretically proves that k-nn can approximate the degree distribution of a scale-free network.

3. The paper presents an extensive set of experiments with several reference citation networks (Cora, Pubmed, ogbn-arxiv and arxiv23). Comprehensive experiments have been conducted using different labeling fractions under semi-supervision conditions and a different number of neighbors in the KNN model, with a detailed description of all hyperparameters used.

### Weaknesses
1. Contribution and Achievements are not clearly introduced: To the best of our knowledge, this work is the first attempt to integrate graph generation and text embedding into a unified GLM framework.

2. Algorithm Design: The introduction of the algorithm design should include necessary details in the main paper, not just in the Appendix. The roles of the GCN, text embedding, and pseudo-labeler should be explained in the main paper. A complexity analysis of each step should be provided shortly in the main paper too.

3. Experimental Results: Clarify whether the results from TAPE and GLEM are directly taken from their respective papers. Additionally, there are other important baselines such as GraphFormers, Leading, SimTEG, and Eingne. If possible, please discuss or compare your results with these models as well. You may also refer to related work in this paper: [https://www.ijcai.org/proceedings/2024/0634.pdf](https://www.ijcai.org/proceedings/2024/0634.pdf).

Introduction: 
0. Clarification of Focused Downstream Task: The specific downstream task of your proposed model is not clearly articulated in the introduction. "When developing a graph language model (GLM) for classification tasks", it is important to clearly define the target task. Typically, downstream tasks are categorized at the node level, edge level, subgraph level, or graph level. In machine learning, these tasks include classification, regression, clustering, and other related objectives. Please specify the precise downstream task your work focuses on. If it is interdisciplinary, make sure to distinguish it from existing topics and clarify its unique contributions in comparison to related fields. If the graph is directed graph please be clear about it too. adapt the section graph construction too. Directed graph should have +1 -1 but not binary for instance ?

0. "However, LGI models typically rely on artificial assumptions about the underlying edge distribution, which may
not accurately reflect the real graph structure." Regarding a series of gcn-based methods, please be concrete about the underlying assumption and why it is too strong in practise or theory?  artificial assumption should also be shortly mentioned with a reference. 

0. However, finetuning a pretrained LM typically requires target datasets with extensive annotations (Brown et al., 2020), which is an unrealistic requirement for semi-supervised learning tasks and may make LM finetuning unreliable if this requirement is not satisfied.  Please list out several publications or provide an example of computation demand? Please refer to https://arxiv.org/abs/2401.15569, https://arxiv.org/abs/2305.19523. 

0.  We identify two key challenges in existing GLMs: artificial structural assumptions for graph generation and unreliable LM finetuning for text embedding. https://academic.oup.com/book/27303 Please refer to this book, especially the estimation of alpha. Please provide an alpha estimation based on their method to identify the condition of validity and effectiveness. Theoretically any graph inhabits some extent of the hierarchy. But only alpha \in [2, 3) would be considered as scale-free is it? Please be clear about the limitation of this assumption https://www.nature.com/articles/s41467-019-08746-5. 

"To the best of our knowledge, this work is the first attempt to integrate graph generation and text embedding into a unified GLM framework. "
It would be better to shortly review previous assumption and their limitation. It is also necessary to prove whether such a prior is more complete than the previous one？Please also add some sentences about the contribution involved and why graph generation is crucial, from which perspective? performance improvement, identify the hypothesis gap? 

Figure 1, if the discussion is about scale-free network, it would be better to plot in log-log sorted degree template? 

Alpha could quite efficiently estimated https://academic.oup.com/book/27303, please also consider it to estimate k? 

in Section 2.3  The degree distribution of KNN graphs is primarily shaped by three critical factors: ① node distribution, is it edge distribution or node? 

Section 3.1 There is still some space to quantify such estimation of k, if the adjacency matrix is know, it should be possible to provide a approximation error? 

2. Regarding the graph's underlying assumptions, the homophily assumption is another important one. Would it not be necessary to compare your approach with this assumption in the related work? Please explain how your method relates to or differs from approaches based on homophily from various level, application, dataset setting?

3. If this work has outperformed the state-of-the-art (SOTA), please highlight it in the introduction and abstract with margin. If not, it would be interesting to mention the gap and your specific focus.

4. If GCN, LM and kNN graph is involved it would be necessary to provide an analytical time complexity analysis and if possible empirical space complexity analysis, so that reader could know whether it is a method with better complexity/performance ratio or refresh the upper bound of current algorithm without taking complexity and scalability into consideration.

### Questions
Introduction: 
0. Clarification of Focused Downstream Task: The specific downstream task of your proposed model is not clearly articulated in the introduction. "When developing a graph language model (GLM) for classification tasks", it is important to clearly define the target task. Typically, downstream tasks are categorized at the node level, edge level, subgraph level, or graph level. In machine learning, these tasks include classification, regression, clustering, and other related objectives. Please specify the precise downstream task your work focuses on. If it is interdisciplinary, make sure to distinguish it from existing topics and clarify its unique contributions in comparison to related fields. If the graph is directed graph please be clear about it too. adapt the section graph construction too. Directed graph should have +1 -1 but not binary for instance ? 


0. "However, LGI models typically rely on artificial assumptions about the underlying edge distribution, which may
not accurately reflect the real graph structure." Regarding a series of gcn-based methods, please be concrete about the underlying assumption and why it is too strong in practise or theory?  artificial assumption should also be shortly mentioned with a reference. 

0. However, finetuning a pretrained LM typically requires target datasets with extensive annotations (Brown et al., 2020), which is an unrealistic requirement for semi-supervised learning tasks and may make LM finetuning unreliable if this requirement is not satisfied.  Please list out several publications or provide an example of computation demand? Please refer to https://arxiv.org/abs/2401.15569, https://arxiv.org/abs/2305.19523. 

0.  We identify two key challenges in existing GLMs: artificial structural assumptions for graph generation and unreliable LM finetuning for text embedding. https://academic.oup.com/book/27303 Please refer to this book, especially the estimation of alpha. Please provide an alpha estimation based on their method to identify the condition of validity and effectiveness. Theoretically any graph inhabits some extent of the hierarchy. But only alpha \in [2, 3) would be considered as scale-free is it? Please be clear about the limitation of this assumption https://www.nature.com/articles/s41467-019-08746-5. 


"To the best of our knowledge, this work is the first attempt to integrate graph generation and text embedding into a unified GLM framework. " 
It would be better to shortly review previous assumption and their limitation. It is also necessary to prove whether such a prior is more complete than the previous one？Please also add some sentences about the contribution involved and why graph generation is crucial, from which perspective? performance improvement, identify the hypothesis gap? 

Figure 1, if the discussion is about scale-free network, it would be better to plot in log-log sorted degree template? 

Alpha could quite efficiently estimated https://academic.oup.com/book/27303, please also consider it to estimate k? 

in Section 2.3  The degree distribution of KNN graphs is primarily shaped by three critical factors: ① node distribution, is it edge distribution or node? 

Section 3.1 There is still some space to quantify such estimation of k, if the adjacency matrix is know, it should be possible to provide a approximation error? 


2. Regarding the graph's underlying assumptions, the homophily assumption is another important one. Would it not be necessary to compare your approach with this assumption in the related work? Please explain how your method relates to or differs from approaches based on homophily from various level, application, dataset setting?

3. If this work has outperformed the state-of-the-art (SOTA), please highlight it in the introduction and abstract with margin. If not, it would be interesting to mention the gap and your specific focus.

4. If GCN, LM and kNN graph is involved it would be necessary to provide an analytical time complexity analysis and if possible empirical space complexity analysis, so that reader could know whether it is a method with better complexity/performance ratio or refresh the upper bound of current algorithm without taking complexity and scalability into consideration.

### Soundness
3

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
The paper focus on node classification of text attributed scale-free graph. The authors discovers that citation networks have the property of scale-free graphs, and proposed KNN Graph based on text similarity distance.  The authors theoretically and empirically demonstrate that KNN graph has property of scale-free graph and can be used as a good prior for scale-free graph such as citation network. 

In the experiment, the authors showed that with small size of labeled data, the model can outperform both GNN based models and Pretrained Language Model based baselines. Ablation studies are performed to demonstrate the effectiveness of KNN Graph approximation for scale-free graphs.

### Strengths
1. The paper proposed a new KNN Graph, which has the property of scale-free graph, can be used as a good prior of scale-free graph such as citation graph. 

2. The paper first introduce the application of scale-free graph in text attributed citation network.

3. The proposed approach is carefully verified using empirical and theoretical approach. 

4. The proposed method outperformed strong baselines 

5. The experiments conducted by the paper is solid and comprehensive

6. Detailed ablation studies are done to analyze the impact different components. Including different text encoders, different graph neural network 

7. The paper is clear and easy to follow

### Weaknesses
1. The explanation of correlation between theory of scale-free network and KNN graph is a bit insubstantial, the theoretical explanation did not provide sufficient intuition to the approach.

2. I find that there are only experiments based on academic citation network. But in the appendix, some analysis on social network data are done, is there any experiment for the task on social network ? It can be more convincing if experiments on other domain can be performed

### Questions
1. Correspond to weakness 1, in the paper between line 103 - 209, the paper discuss why KNN graph is similar to scale-free graph. The property of Homophily and Directed seems trivial.  Upper bound of degree is proved using Proposition 1 and Proposition 2, but it can not explain why KNN graph's node degree follow the power law which is an important property of scale-free network. Empirical curve fitting shows that probability of node degree of KNN graph could follow the power law, is there any theoretical  explanation behind this ?

2. I find that there are only experiments based on academic citation network. But in the appendix, some analysis on social network data are done, is there any experiment for the task on social network ? It can be more convincing if experiments on other domain can be performed

### Soundness
3

### Presentation
3

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
The paper introduces a new framework that combines graph generation and text embedding using the scale-free property of real-world networks. By approximating this structure with a KNN graph, the model improves graph generation and enhances language model finetuning. The paper uses a graph-based pseudo-labeling method to improve performance on semi-supervised tasks, validated through experiments on several citation network datasets​

### Strengths
1. The idea is novel. A unique contribution is to use KNNs for Graph generation, which I think will be very inspiring for semi-supervised tasks in homogeneous networks, especially from the comparison with the Real Graph on Table 6, the generated graph is even better than the real graph.

2. The paper is well-written, providing a detailed description of the problem setting and research background.  The authors clearly articulate the challenges in existing graph-language models and their motivation for the proposed approach, making the rationale behind their work easy to follow.

3. The extensive ablation studies included in the paper significantly contribute to the credibility of the proposed method.

### Weaknesses
1. The paper primarily focuses on citation networks, which are inherently homophilic.  The applicability of the proposed KNN-based graph generation method to other types of textual networks, such as academic or social networks, is not explored. 

2. The core contribution of the paper lies in using KNN to approximate graphs, but this approach seems to be more suited for homophilic networks.  In more diverse scenarios, such as heterogeneous academic networks with different types of nodes, the use of a unified nearest-neighbor metric may introduce significant bias.  This limits the method’s applicability to broader graph structures. It is recommended to try a broader extension of the for KNN design.

3. While the paper provides strong theoretical and experimental support, the experiments on the validation of KNN could be more comprehensive. (See Questions)

### Questions
1. I believe validating KNN is crucial, and I suggest the authors include comparisons with other graph generation methods, such as random graph generation or rule-based approaches. 

2. I am curious how the specific implementation of real graph in Table 6 is set up?

3. I noticed that the real graph is not even as good as the graph generated by KNN, I hope the author can give your thoughts on this. Such results give people the inspiration that the graph generation is not for fitting the real network connections, but for the information transfer of nodes with high similarity. However, this ignores the information transmission of real edges, because nodes only believe the points that are close to each other, which is easy to introduce errors for complex network mechanisms.

4. I think a deeper experimental exploration of the above questions should involve trying LLM-only prediction ways in the network, such as [1] [2], etc., missing in the paper cited.

5. The paper lacks some experimental details, such as the division of datasets into labeled and unlabeled nodes (m, n) and the specific settings of the iterative algorithm. 

[1] Bi B, Liu S, Wang Y, et al. Lpnl: Scalable link prediction with large language models[C]//Findings of the Association for Computational Linguistics ACL 2024. 2024: 3615-3625.

[2] Ye R, Zhang C, Wang R, et al. Natural language is all a graph needs[J]. arXiv preprint arXiv:2308.07134, 2023, 4(5): 7.

Concise and powerful responses will help me understand better, and I will consider raising my score.

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
This paper proposes a novel scale-free graph-language (SFGL) model. There are two main components in the proposed framework: (1) Scale-free KNN graph construction; (2) LM Training augmented with KNN graph-based pseudo labels. Experiments demonstrate that SFGL shows comparable performance.

### Strengths
1. The use of scale-free properties for graph generation is clever and practical. The approximation via KNN graphs is a simple yet effective method.
2. While the use of pseudo-labels is not a new concept in integrating graphs and language models, the way it is applied in this paper is particularly effective.
3. The empirical results are compelling, with the SFGL model consistently outperforming baseline methods across various datasets and labeling rates.

### Weaknesses
1. The author could conduct more experiments with different values of labeling rates. Although the paper focuses on the low labeling rates, it will be meaningful to extend the experiments to higher labeling rates (e.g., 50% to 60%) to better understand the model’s scalability and performance under such higher labeling conditions. Observing the model's behavior with more labeled data could also provide insights into whether the proposed improvements hold up when labeled data is no longer a significant limitation.

2. Although the paper demonstrates that KNN graphs have comparable performance to the real graph (Table 6),  the differences between KNN and real graph structures are not thoroughly explored. A more detailed case study or analysis comparing the graph structures between KNN graphs and real graphs could provide valuable insights. Specifically, it would be beneficial to analyze the degree distribution, clustering coefficient, and average path length of both graph types to quantify their structural differences.

3. Some minor points:
In Algorithm 1, Textual feature X -> Text sequences X, consistent with line 265
In Algorithm 2, replace X with E -> replace F with E. (X are input text/tokens, E and F are text embeddings.)

4. In abaltion studies, the author could use some more powerful text encoders, especially some recently used LLM-based encoders, such as E5-Mistral-7B-Instruct (https://huggingface.co/intfloat/e5-mistral-7b-instruct). More powerful encoders can be found in the MTEB leaderboard (https://huggingface.co/spaces/mteb/leaderboard). 
5. In ablation study section, the author could report the results when only using KNN graph generation without the LM-finetuning.

### Questions
See Weeknesses part.

### Soundness
3

### Presentation
2

### Contribution
3
