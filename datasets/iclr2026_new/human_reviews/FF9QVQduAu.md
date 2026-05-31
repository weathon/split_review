## Human Reviewer 1

### Summary
This paper introduces CrowdFM, a graph neural network-based "foundation model" for crowdsourced label aggregation, pretrained on synthetic data to enable retraining-free, cross-dataset generalization. The model is evaluated on 22 real-world datasets and shows strong empirical performance and efficiency. However, the main weakness of this paper is its failure to acknowledge and position itself with respect to highly relevant prior work—specifically, the hyper label model (Wu et al., ICLR 2023). The methodology, motivation, and even the technical design of CrowdFM are very similar to those of the hyper label model, with the only substantive difference being the application domain (crowdsourcing vs. programmatic weak supervision) and the technical details in training data generating and the graph neural network architecture design. The paper overstates its novelty and does not provide a meaningful discussion or comparison to this existing work. As a result, the contribution is incremental and the claims of being the "first" to propose such a foundation model are not justified.

### Strengths
- The paper addresses a real and important challenge in crowdsourced label aggregation: the need for scalable, retraining-free aggregation methods that generalize across datasets.
- The paper provides a synthetic data generation process for training such models.
- CrowdFM achieves fast inference times, comparable to simple methods like Majority Voting, while outperforming more complex dataset-specific models.

### Weaknesses
1.  Lack of proper acknowledgement of closely related work. The most significant issue with this paper is its failure to properly acknowledge and position itself with respect to existing work that is nearly identical in methodology and motivation. In particular, the ICLR 2023 paper[1] that proposes a hyper label model for programmatic weak supervision that is, in essence, the same as the approach in this paper:
  - Both solve the label aggregation problem. 
  - Both aim for cross-dataset generalization and retraining-free inference.
  - Both papers propose a GNN-based model that is pretrained on synthetic data to learn a generalizable label aggregation function.
  - Both use size-invariant initializations and GNN architectures to handle variable numbers of annotators (workers/LFs) and tasks.
  - Both demonstrate that their model, once trained, can be applied to new datasets in a single forward pass, outperforming dataset-specific methods in both accuracy and efficiency.

While the paper claims to be the "first foundation model for label aggregation," this is not accurate. The hyper label model[1] is a direct precedent, and the technical similarities are substantial. The only notable difference is the application domain: The hyper label model[1] focuses on programmatic weak supervision (labeling functions), while this paper focuses on crowdsourcing (human workers). However, the mathematical setup is essentially the same (a bipartite label matrix with noisy annotators) in these two domains.
The lack of discussion, comparison, or even citation of this highly relevant prior work is a serious omission. This gives the misleading impression that the proposed approach is novel, when in fact it is a straightforward adaptation of an existing method to a closely related domain.

2. The paper repeatedly claims to be the "first" to propose a foundation model for label aggregation, and to introduce a new paradigm. Given the existence of[1], these claims are overstated.

3.  Given the existence of the hyper label model approach[1], the main contribution of the paper seems to be modifications to the synthetic data generator and GNN architecture.

[1] Wu et al., "Learning Hyper Label Model for Programmatic Weak Supervision" (ICLR 2023)

### Questions
1. Are the authors aware of the hyper label model[1]? Can the authors clarify the technical and conceptual differences between CrowdFM and the hyper label model, beyond the application domain? Please explicitly discuss this prior work in the related work section, and provide a detailed comparison (both conceptual and empirical) to clarify what is novel in CrowdFM.
2. How does CrowdFM perform compared to the hyper label model?
3. What new insights does CrowdFM provide for the crowdsourcing setting on top of what is discussed in[1].
4. Is CrowdFM able to provide any theoretical guarantees as in[1].

[1] Wu et al., "Learning Hyper Label Model for Programmatic Weak Supervision" (ICLR 2023)

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper proposes CrowdFM, the first foundation model for crowdsourced label aggregation. It replaces traditional per-dataset parameter estimation with a pretrained bipartite graph neural network trained on a vast, domain-randomized synthetic dataset. By leveraging a size-invariant initialization and attention-based message passing, it learns universal principles of collective intelligence and generalizes to new, unseen datasets. Experiments on 22 real-world datasets show that CrowdFM matches or outperforms state-of-the-art methods in both accuracy and efficiency, while its learned representations also support worker assessment and task assignment.

### Strengths
1.The proposed CrowdFM is the first foundation model for label aggregation, enabling cross-dataset generalization without retraining and marking a key step toward universal label aggregation.

2.CrowdFM further exhibits strong versatility, as its pretrained representations can be directly adapted to multiple downstream tasks such as worker assessment and task assignment without additional training.

3.Extensive experiments on 22 real-world benchmarks demonstrate that the proposed single, fixed model consistently matches or surpasses dataset-specific methods in both accuracy and efficiency.

### Weaknesses
1.The paper lacks a systematic quantitative analysis of synthetic and real-world crowdsourced data. Although the authors validate generalization on real datasets, they do not analyze the distributional differences of key parameters (e.g., worker ability θ, task difficulty β, task guessing rate c) between synthetic and real data, making it difficult to assess how well the learned patterns reflect real human annotation behaviors. Besides, how to obtain these sampling ranges?

2.Although the parameters in the synthetic data generator are randomly sampled, the paper lacks a sensitivity analysis of key parameters. Random sampling alone cannot fully verify the model’s robustness across different crowdsourcing conditions. It is recommended to include such an analysis to strengthen the credibility of CrowdFM’s generalization claims.

3.With regard to the comparison results, statistical tests are needed in the comparison results. The detailed description about statistical tests for comparisons of multiple algorithms on multiple datasets can be found from the papers such as Statistical comparisons of classifiers over multiple data sets.

4.The paper lacks ablation studies to verify the individual contributions of key components (e.g., attention-based aggregation, size-invariant initialization, and synthetic data diversity). Without such analysis, it is difficult to determine which design choices are most critical to the model’s performance gains.

### Questions
The same as the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
Traditional methods (e.g., Dawid–Skene, GLAD, EBCC) typically adopt a dataset-specific modeling paradigm: they require training model parameters from scratch for each new dataset, resulting in poor generalization. Meanwhile, Majority Voting (MV), widely used in industry, requires no training but ignores differences in annotators' capabilities, leading to limited accuracy.
To bridge this gap, the authors propose a universal aggregation paradigm: by pre-training a bipartite GNN on large-scale, domain-randomized synthetic datasets, the model learns transferable "collective intelligence" aggregation rules. During the inference phase, the model can be directly applied to any real crowdsourced dataset without fine-tuning or retraining.

### Strengths
1.	Strong paradigm innovation: For the first time, the foundation model concept was introduced into crowdsourced label aggregation, breaking the dataset-specific paradigm that has persisted for decades.
2.	The problem definition has practical significance: Shifting the aggregation of crowdsourced labels from the "dataset-by-dataset modeling" paradigm to the "unified fundamental model" paradigm aligns with the urgent demand of the industrial sector for scalable and retraining-free systems.
3.	The experiments were thorough: 22 real datasets covered text, images, and audio, and included extreme scale/density scenarios, verifying the generalization ability.
4.	The accuracy rate and running time were reported, and it was pointed out that some methods failed due to insufficient memory

### Weaknesses
1.	How can we ensure that the distribution of synthetic data is sufficient to cover the feature space of real crowdsourcing tasks? Is there any performance degradation under certain types of tasks (such as extremely unbalanced ones)?
2.	Can CrowdFM be regarded as the specialization of GraphFM in the field of crowdsourcing? Has the pre-training objective of the existing GFM been borrowed?
3.	The performance for extremely large-scale data (such as Senti and Fact) slightly decreases, but the reasons are not discussed.
4.	The absence of ablation experiments makes the contributions of each module unclear
5.	Although it includes recent works such as EBCC, GOVERN, TiReMGE, etc., some new methods for 2024-2025 are missing (such as Zhang et al., KFNN and IWBVT of NeurIPS 2024 are cited but not used as baselines);
6.	The superparameters such as the number of layers L and dimension d of GNN were not discussed in detail.
7.	The "Sim-to-Real Gap" between synthetic data and real data has not been fully quantified
8.	Has the model truly learned the "principle of collective intelligence", or has it merely fitted the statistical patterns of synthetic data? How to prove.

### Questions
Same as weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper aims at building a foundation model for crowdsourced label aggregation that generalizes across heterogeneous datasets without dataset-specific training. It first generates a synthetic crowdsourced data generator to produce diverse synthetic datasets, and then trains a bipartite graph neural network which can be generalizable to other data and tasks. Experiments show the foundation model is efficient and achieve performance comparable to or superior to state-of-the-art aggregation methods.

### Strengths
1. Generating the synthetic data and then train a generalizable GNN model to approximate it is a smart idea to unify the data-specific crowdsourcing models. I think it is essentially a type of knowledge distillation, which distills the knowledge from the data generator to a GNN with less input features (e.g. task difficulty/worker ability, which are generally regarded as latent parameters in traditional probabilistic models). 
2. The method is sound, and the presentation is clear.
3. Experiments show good accuracy with more efficiency.

### Weaknesses
1. The backbone model is relatively simple and not new, but the design is a good fit for crowdsourcing, e.g. the size-invariant initialization for worker/task emebddings. I do not see it as a weakness, but just not a novel contribution. I still like the whole framework of building synthetic data and train a simple domain-indepedent model as foundation models.

2. The possible limitation of the model is it may lack the flexibility to adapt to the case when workers/tasks have their attributes, since these nodes are initialized with fixed pretrained embeddings.

3. Another possible weakness is the limitation of the data generator. Although it is a quite general scheme, there might be other graphical models that it cannot cover; and also the prior distribution of the parameters might cause some bias for the pretrained foundation model.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3