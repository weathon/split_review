# Link Prediction on Text Attributed Graphs: A New Benchmark and Efficient LM-nested GNN Design

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 3, 6

## Abstract
Textual and topological information is significant for link prediction (LP) in textattributed graphs (TAGs). Recent link prediction methods have focused on improving the performance of capturing structural features by Graph Convolutional Networks (GCNs), the importance of enhancing text embeddings, powered by the powerful Pretrain Language Model (PLM), has been underestimated. We collect and introduce eight graphs with rich textual information. We further benchmarked current competitive link prediction methods and PLM-based methods in a unified experimental setting, systematically investigating the representation power of the text encoders in the link prediction task. Based on our investigation, we introduce LMGJOINT — a memory-efficient fine-tuning method. The key design features include: residual connection of textual proximity, a combination of structural and textual embeddings, and a cache embedding training strategy. Our empirical analysis shows that these design elements improve MRR by up to 19.75% over previous state-of-the-art methods and achieve competitive performance across a wide range of models and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides a benchmark for link prediction tasks on text-attributed graphs for models based on pre-trained language models (PLMs). This paper proposes a novel architecture for link prediction on Textual-Attribute Graphs (TAGs), introducing a "Residual Textual Proximity Connection" to enhance node representations by directly incorporating textual similarity information. The model aims to address over-smoothing in GNNs and claims to improve parameter and memory efficiency by leveraging smaller language models (LMs) as backbones.

### Strengths
1. The experiments cover multiple model configurations and report performance on various metrics.

2. The idea of ​​"residual connection of GCN" is proposed to solve the over-smoothing problem in GNN in text-attributed graph applications.

### Weaknesses
1. The readability of the article needs to be improved.

2. Some statments are confusing and not supported by exerimental results. Some unusual results are not discussed.

3. No dataset is provided in the referenced repository, hindering reproducibility. Some implementation details are missing.

4. Please review the references carefully to avoid duplicate entries, such as [1-4]. Some closely related work on link prediction in textual-attribute graphs is missing; consider including relevant studies, such as [5].

5. Please thoroughly check for typos. For instance, in the caption of Figure 1, in line 67, "$Hij$" should be "$H_{ij}$"; in line 69, "$HC$" should be "$H_C$"; in line 869, "$2^10$" should appear as "$2^{10}$", etc.

6. How to intialize $H^k$ in Eq. (4)?

7. The concept of a residual connection in this paper is confusing. Why is adding textual proximity information to the GCN’s output "residual"? Additionally, the authors claim that this connection mitigates the over-smoothing issue, but no experimental evidence supports this. The GNN used does have more than 3 layers, which does not qualify as a "deep GNN."

8. In lines 256-257, the authors claim that the model is both parameter and memory-efficient. However, the experimental results do not substantiate this claim. In Table 2, MiniLM, MPNet, and e5-large are used as PLM backbones of the proposed model (parameters less than 500M). It is not challenging to fine-tune these models.

9. There are inconsistencies between Algorithm 1 and the model description in Section 4. For instance, what is SE-NCN? Where is $H^K$, $H_C$ and $H_T$ in Algorithm 1? What is $X^{\mathcal{G}}$ and where is $X^{\mathcal{G}}$ in Section 4?

10. How do the additional statistics assist with link prediction tasks? The authors list this as a contribution, but there is no discussion on its relevance. If they do not improve link prediction, what purpose do they serve?

11. Key implementation details are missing. For instance, what specific fine-tuning techniques were used for the language models? Was full-parameter fine-tuning or parameter-efficient fine-tuning employed? How is $\beta$ in Eq. (5) determined?

12. The caption for Table 2 indicates that boxed results represent the best performance, but this is not the case.

13. In Table 2, it is unusual that fine-tuning PLM + MLP (FT-PLM-MLP) performs significantly better than fine-tuning PLM + GNN (FT-PLM-GCN), which contrasts with the findings of most prior studies. This discrepancy deserves further discussion.

14. No datasets are provided in the repository referenced.

15. What is $\theta_{\mathcal{G},T}$ in Eq. (7)?

16. The assumptions in the proofs for Theorems A.1 and A.2 appear oversimplified

### Questions
1. Please review the references carefully to avoid duplicate entries, such as [1-4]. Some closely related work on link prediction in textual-attribute graphs is missing; consider including relevant studies, such as [5].

2. Please thoroughly check for typos. For instance, in the caption of Figure 1, in line 67, "$Hij$" should be "$H_{ij}$"; in line 69, "$HC$" should be "$H_C$"; in line 869, "$2^10$" should appear as "$2^{10}$", etc.

3. How to intialize $H^k$ in Eq. (4)? 

4. The concept of a residual connection in this paper is confusing. Why is adding textual proximity information to the GCN’s output "residual"? Additionally, the authors claim that this connection mitigates the over-smoothing issue, but no experimental evidence supports this. The GNN used does have more than 3 layers, which does not qualify as a "deep GNN."

5. In lines 256-257, the authors claim that the model is both parameter and memory-efficient. However, the experimental results do not substantiate this claim. In Table 2, MiniLM, MPNet, and e5-large are used as PLM backbones of the proposed model (parameters less than 500M). It is not challenging to fine-tune these models.

6. There are inconsistencies between Algorithm 1 and the model description in Section 4. For instance, what is SE-NCN? Where is $H^K$, $H_C$ and $H_T$ in Algorithm 1? What is $X^{\mathcal{G}}$ and where is $X^{\mathcal{G}}$ in Section 4? 

7. How do the additional statistics assist with link prediction tasks? The authors list this as a contribution, but there is no discussion on its relevance. If they do not improve link prediction, what purpose do they serve?

8. Key implementation details are missing. For instance, what specific fine-tuning techniques were used for the language models? Was full-parameter fine-tuning or parameter-efficient fine-tuning employed? How is $\beta$ in Eq. (5) determined? 

9. The caption for Table 2 indicates that boxed results represent the best performance, but this is not the case.

10. In Table 2, it is unusual that fine-tuning PLM + MLP (FT-PLM-MLP) performs significantly better than fine-tuning PLM + GNN (FT-PLM-GCN), which contrasts with the findings of most prior studies. This discrepancy deserves further discussion.

11. No datasets are provided in the repository referenced.

12. What is $\theta_{\mathcal{G},T}$ in Eq. (7)?

13. The assumptions in the proofs for Theorems A.1 and A.2 appear oversimplified

---
[1] Kipf, Thomas N., and Max Welling. "Semi-supervised classification with graph convolutional networks." arXiv preprint arXiv:1609.02907 (2016).

[2] Luan, Sitao, et al. "When do graph neural networks help with node classification? investigating the impact of homophily principle on node distinguishability." arXiv preprint arXiv:2304.14274 (2023).

[3] Mao, Haitao, et al. "Revisiting link prediction: A data perspective." arXiv preprint arXiv:2310.00793 (2023).

[4] Xu, Keyulu, et al. "How powerful are graph neural networks?." arXiv preprint arXiv:1810.00826 (2018).

[5] Li, Zhuofeng, et al. "TEG-DB: A Comprehensive Dataset and Benchmark of Textual-Edge Graphs." arXiv preprint arXiv:2406.10310 (2024).

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
3

### Summary
The paper proposes a novel approach for link prediction on text-attributed graphs by integrating PLMs with GCNs. The authors introduce a new method called LMGJOINT, which optimizes the representation of both structural and textual information through residual textual proximity connections and a cache embedding training strategy. Additionally, the paper presents a comprehensive benchmark consisting of eight graphs to compare various existing and proposed methods, showing that LMGJOINT significantly outperforms the baselines in terms of MRR and other metrics.

### Strengths
1. The paper addresses a gap in the current research by proposing a joint framework that efficiently integrates PLMs with GCNs. This nested approach for link prediction on TAGs is novel and demonstrates strong performance improvements across multiple datasets.
2. The introduction of eight datasets, including well-established ones like Cora and PubMed, provides a robust experimental setup.
3. LMGJOINT is designed to be memory-efficient, making it scalable to large graphs.

### Weaknesses
1. One of the biggest concerns is the authors may not consider textual edge cases, which is quite essential in text-arrtibuted graph benchmarks.
2. The datasets used for evaluation, while comprehensive, are mostly academic in nature. The paper would benefit from demonstrating the applicability of LMGJOINT in more diverse, real-world scenarios (e.g., social networks or e-commerce systems) to show that the method generalizes well beyond citation networks.
3. The paper introduces a fine-tuning strategy for PLMs but does not delve deeply into its impact on performance compared to using frozen embeddings. It would be valuable to see more ablation studies or results that isolate the effect of fine-tuning versus other factors in the model's performance.

### Questions
More detailed ablation studies to isolate the impact of each design decision, especially the fine-tuning of PLMs, would clarify the relative contribution of each component of the model.

A minor issue: it would be more common to abbreviate "Equation" as "Eq." instead of "Equ".

### Soundness
3

### Presentation
3

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
This paper develops a benchmark for comparing graph-based and PLM-based baselines in link prediction tasks based on eight proposed TAG datasets. Furthermore, it introduces a parameter- and memory-efficient fine-tuning method, LMGJOINT, which effectively integrates structural and textual information via GCN and PLM. Experimental results demonstrate the effectiveness and scalability of LMGJOINT, showing consistent performance improvements over compared baselines.

### Strengths
1. This paper introduces eight TAG datasets for link prediction and provides an empirical benchmark that enables fair comparisons between graph-based and PLM-based baselines.
2. This paper proposes a language model graph joint design framework, LMGJOINT, effectively combining structural and textual embeddings from GCN and PLM, respectively. Moreover, LMGJOINT adopts a cache embedding strategy, significantly reducing the computational cost.
3. This paper conducts extensive experiments on eight proposed datasets for link prediction, illustrating the effectiveness and scalability of LMGJOINT with minimal hyperparameter tuning required.

### Weaknesses
1. Disorganized writing and structure. The writing structure of this paper should be reorganized for improved clarity. For example, the content in "Related Datasets and Current Situation" in Section 3 could be integrated with "Related Benchmarks" in Section 2. Moreover, more detailed analyses of the eight proposed graph datasets for link prediction are needed. "Link prediction using GCN" in Section 2 should be reorganized based on different categories, incorporating some recent GCN-based methods from 2024, such as HL-GNN [1].
2. Ambiguous benchmarking setup. In Section 5, the authors should describe more implementation details, particularly regarding the proposed LMGJOINT, such as the chosen GCN and PLM. It is important to clarify these details to ensure a healthier benchmarking and determine what kind of benefits LMGJOINT brings. Furthermore, Sections 5.1 and 5.2 should clearly list all compared baselines.
3. Missing important baselines. To comprehensively evaluate LMGJOINT's performance in link prediction, many traditional random work-based and relation learning-based methods should be included, such as Metapath2Vec [2], ConvE [3], and ComplEx [4]. They can effectively capture flexible topological structures of graphs and understand relations between nodes. Additionally, some recent GNN and LLM + GNN baselines should be also considered, such as HL-GNN[1], BUDDY [5], TAPE [6], and GraphGPT [7].
4. Typographical Errors. There are some typos in this paper. For example, In line 069, $\textbf{H}C$ should be revised as $\textbf{H}^C$ consistent with $\textbf{H}^K$. In line 144, there is a reference error in "TAG_Benchmark (Yan et al., 2023)". In line 177, the caption of Figure 2 lacks a period after "..., see Appendix G". In line 216, "feature as shown in Equ 4" should be corrected to "feature as shown in Eq. 4."

### Questions
1. Could the author further clarify and compare the differences between the widely used OGB datasets for link prediction and the eight datasets proposed in this paper?
2. Could the authors discuss the efficiency of LMGJOINT in comparison to other baselines, including in terms of training/inference time and memory usage? Such an analysis would be valuable for demonstrating that LMGJOINT is both parameter- and memory-efficient.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a comprehensive benchmark for link prediction on text-attributed graphs (TAGs) and proposes a novel PLM-nested GCN design called LMGJOINT. The authors analyze the importance of PLMs in link prediction and investigate the representation power of text encoders. They introduce LMGJOINT, which includes residual connections of textual proximity, a combination of structural and textual embeddings, and a cache embedding training strategy. Experimental results show that LMGJOINT outperforms previous state-of-the-art methods and achieves competitive performance across multiple datasets.

### Strengths
(1) The paper provides an innovative and practical methodology for link prediction on TAGs, addressing the importance of PLMs and proposing a novel PLM-nested GCN design.

(2) The paper conducts an extensive benchmark to compare current competitive link prediction methods and PLM-based methods, providing a comprehensive evaluation of different approaches.

(3) The paper is well-structured and provides a clear overview of related work, datasets, methodologies, and experimental results.

### Weaknesses
 (1) Edge Text Consideration. The dataset should incorporate edge text to enhance its robustness and relevance. For instance, in a citation network dataset, including the citation context as edge text would provide valuable semantic information, improving the analysis and interpretations of the relationships between nodes. The absence of edge text limits the model's ability to capture nuanced relationships that are often expressed in the textual context of the edges themselves. This is particularly relevant in scenarios where the relationship between nodes is not solely defined by their attributes but also by the context of their interaction.

(2) Domain Limitation of Datasets. Expanding the evaluation to include diverse domains, such as those in the TEG-DB datasets, which feature rich node and edge text, would strengthen the findings. The current evaluation is limited to a specific type of graph data, and it is unclear how the proposed method would generalize to other types of graphs with different characteristics. For example, graphs from social networks or e-commerce platforms might exhibit different patterns and require different modeling approaches. The lack of evaluation on such diverse datasets raises concerns about the robustness and general applicability of the proposed method.

(3 ) Writing Quality: There are several typos present, and the overall writing quality needs improvement for clarity and professionalism.

+ On page 1, Figure 1“X \in \mathbb{R}^d” should be “X \in \mathbb{R}^n*d”.
+ On page 1, Figure 1 caption “HC” should be “H_{c}”.

### Questions
Please see the Weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3
