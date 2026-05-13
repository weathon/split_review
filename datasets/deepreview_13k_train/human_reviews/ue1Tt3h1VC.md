# Multiple Heads are Better than One: Mixture of Modality Knowledge Experts for Entity Representation Learning

- Decision: Accept
- Scores: 5, 6, 8, 6, 8

## Abstract
Learning high-quality multi-modal entity representations is an important goal of multi-modal knowledge graph (MMKG) representation learning, which can enhance reasoning tasks within the MMKGs, such as MMKG completion (MMKGC). The main challenge is to collaboratively model the structural information concealed in massive triples and the multi-modal features of the entities. Existing methods focus on crafting elegant entity-wise multi-modal fusion strategies, yet they overlook the utilization of multi-perspective features concealed within the modalities under diverse relational contexts. To address this issue, we introduce a novel framework with \underline{\textbf{M}}ixture \underline{\textbf{o}}f \underline{\textbf{Mo}}dality \underline{\textbf{K}}nowledge experts ({\model} for short) to learn adaptive multi-modal entity representations for better MMKGC. We design relation-guided modality knowledge experts to acquire relation-aware modality embeddings and integrate the predictions from multi-modalities to achieve joint decisions. Additionally, we disentangle the experts by minimizing their mutual information. Experiments on four public MMKG benchmarks demonstrate the outstanding performance of {\model} under complex scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles MKGE problems by proposing a Mixture of Modality Knowledge Experts framework. The authors develop relation-guided modality knowledge experts to obtain relation-aware modality embeddings while reducing mutual information among the experts. Empirical studies validate the model's effectiveness.

### Strengths
1. Experiments in complex environments demonstrate MoMoK's resilience to noise, data sparsity, and missing modalities.  
2. This work introduces a novel expert information disentanglement (ExID) module to separate expert decisions for each modality.  
3. The rationale for designing the relation-aware MKGC method is evident.

### Weaknesses
1. Metrics Reporting: Table 2 displays only the Hit@1 and MRR metrics for MKG-W and MKG-Y, showing modest performance improvements for MoMoK. Please include additional metrics such as Hit@3 and Hit@10 for MoMoK, AdaMF, and MMRNS to better assess the reported gains and provide a more comprehensive comparison across all methods.

2. MoMoK on Classic MMKGC Datasets: The absence of evaluations on classic MMKGC datasets like WN9-IMG, FB-IMG, WN18-IMG, and FB15K-237-IMG is a significant oversight. These datasets are crucial for establishing the generalizability of the proposed method and should be included for a thorough evaluation.

3. Modal Data and Encoder Details: The notation $\mathcal{X}_m(e)$ indicates information from multiple modalities, yet four datasets are used. It is unclear what specific modalities are used for each dataset, how multiple images per entity are handled, and whether VGG and BERT are consistently used as encoders across all datasets. This lack of clarity hinders reproducibility and understanding of the experimental setup.

4. Notation Standardization: Some formulas, such as $\mathcal{E}_h$ in formula (1), could benefit from standardized notation to improve clarity and consistency. The current notation is ambiguous and could lead to misinterpretations of the intended operations.

5. Relation-Aware Temperature ($\mathcal{E}_r$): The relation-aware temperature $\mathcal{E}_r$ is important for GFN computation, but its definition is absent. The lack of a formal definition and explanation of its impact on model performance makes it difficult to assess the contribution of this component.

6. Score Function Comparison: The proposed method employs Tucker decomposition as its score function, while the baseline methods utilize various other functions. This difference in score functions makes it difficult to isolate the impact of the proposed method from the choice of score function. A more controlled comparison is needed to understand the true benefits of the proposed approach.

7. Ablation Study: Ablation experiments indicate that components like adaptive fusion, noise $\delta_{r}$, and relational $\epsilon_{m}$ may have minimal individual impacts. The analysis of these components needs to be more detailed, and the significance of these components in different experimental contexts should be emphasized.

8. Ablation Experiments for MKG-Y and KVC16K: The ablation experiments are limited to MKG-W and DB15K. Including MKG-Y and KVC16K datasets in the ablation experiments would enhance the assessment of the method's performance across diverse data and conditions, providing a more robust evaluation of the proposed method.

### Questions
please see above.

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
This paper proposes a novel framework, Mixture of Modality Knowledge Experts (MoMoK), which aims to improve the quality of multimodal entity representation learning through relation guidance and expert information decoupling in multimodal knowledge graphs (MMKGs). MoMoK achieves better triple prediction by designing a relation-guided modal knowledge expert network, adaptively aggregating multi-view embeddings, and adopting a multimodal joint decision mechanism. Experimental results show that MoMoK performs well on four public MMKG benchmarks and significantly outperforms existing methods.

### Strengths
1. This paper considers the modal information hidden in different relational contexts and designs a relation-guided modal knowledge expert network to adaptively aggregate multi-view embeddings.
2. On four public MMKG benchmarks, MoMoK significantly outperforms recent baseline methods and demonstrates its superior performance in complex scenarios.
3. Through detailed ablation analysis, this paper verifies the effectiveness of the design and provides intuitive case studies to enhance the interpretability of the model.

### Weaknesses
1. Table 2 lacks a comparison of the number of model parameters. Although the authors have discussed the training memory consumption and time efficiency of some methods in Section 5.6, it is beneficial to supplement these values for all baseline models in Table 2 for fair comparison. Specifically, the parameter count is crucial for understanding the model's complexity and resource requirements, and should be included for all models, not just a subset. This is important for assessing the trade-off between performance gains and model size.
2. The description in Table 4 does not seem to be that comprehensive. Does the GPU memory here refer to the memory during inference or the memory during training? Does the time in seconds represent the time it takes to infer one sample? It is important to clarify whether the reported GPU memory usage and time costs are for training or inference, as these have different implications for practical deployment. Furthermore, the time cost should be specified more clearly, such as the time per epoch or per batch, rather than just 'time in seconds'.

### Questions
1. The parameter \lambda seems small enough. Can you explain why club loss can improve the model by about one point in almost every metric under a weight of 1e-4 (Table 3)?
2. The method seems to be insufficiently integrated with the multimodal large model. This paper uses BERT and VGG to extract the original features of the model. Have you tried to use a multimodal large model to represent them uniformly? I would like to know the performance comparison between the embedding representation of the multimodal large model and MoMoK.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a multi-modal mixture-of-experts entity representation framework MoMoK for knowledge graph completion task. MoMoK consists of three different modules called relation-guided modality knowledge experts, multi-modal joint decision, and expert information disentanglement.

### Strengths
- Multi-modal knowledge graph representation learning is a hot topic in the KG community.
- The three modules in the design of the method proposed by the authors are self-consistent and the authors provide a more detailed theoretical proof.
- The experimental part of the workload is sufficient, and the authors have done more experiments to prove the effectiveness, robustness, and efficiency of the method. Detailed case study and visualization results are also provided.

### Weaknesses
 - The discussion of MAIN RESULTS needs to go further, have the authors explored in depth why MKG-Y has a lesser MRR than baseline AdaMF?
- The fonts of the figure3 and figure4 are not consistent.
- The detailed settings of Section5.4 should be more carefully introduced. About how the training datasets are built and the detailed evaluation protocol.

### Questions
- Please make a response to the comments in weaknesses.
- What exactly are the advantages of the traditional embedding-based approach over the LLM-based approach for knowledge graph completion?

### Soundness
3

### Presentation
4

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
This paper introduces a novel model named MOMOK (Mixture of Modality Knowledge Experts), designed to address the challenges in multimodal knowledge graph completion tasks. The innovation lies in the relation-guided multimodal expert networks, which dynamically adjust the weighting of modal information based on relation, enhancing the model's completion performance. The experimental results demonstrate that MOMOK surpasses existing baseline models across multiple public datasets, showcasing its effectiveness in handling multimodal information. The paper is well-writing with contributions in both theoretical design and empirical results.

### Strengths
1. The introduction of relation-guided multimodal expert networks with adaptive weighting mechanisms enables the model to fully exploit different perspectives within each modality based on relational context, which represents a novel and impactful focus.
2. By minimizing mutual information, the model effectively reduces redundant information between modalities, enhancing disentanglement among the experts. This is a particularly noteworthy design feature.
3. The ablation experiments validate the importance of each module in the model's performance, particularly highlighting the significance of joint training and information disentanglement, proving the rationale behind the design.
4. The paper presents five well-defined research questions (RQs) that thoroughly address the model’s strengths, performance in complex environments, and the contribution of each design module. This makes the experimental section well-structured and logically cohesive.

### Weaknesses
1. The novelty is somewhat limited. The paper claims existing works lack considering the relational context, and proposes MoMoK frameworks by incorporates relation-guided modality knowledge experts for each modality, which constructs expert networks in each modality. But in my opinion, there are also lots of prior work (such as MoSE) considering relational context.
2. It would be beneficial to introduce datasets used in baselines for comprehensive comparison. The baselines, such as MoSE, further conduct experiments on (FB-15K, WN18, WN9) which this paper did not used. Including these datasets would be helpful to further demonstrate the robustness of the proposed model.
3. The expert networks rely on raw embeddings, which may limit their ability to fully capture the diversity within each modality. This could lead to less distinct perspectives being generated by the experts, especially if the raw embeddings have already compressed or lost key details, thereby reducing the overall effectiveness of the expert network design.
4. While the paper introduces CLUB to estimate the upper bound of mutual information and designs a corresponding loss function, it lacks sufficient explanation for why the conditional probabilities of different entities are used for disentanglement in formula 8.


Other Minor Weaknesses:

1. The related work section is too brief and fails to emphasize the superiority of the proposed framework compared to existing approaches. For example, in the experimental section, you mentioned the similarities between your method and MoSE and IMF as baselines, but you did not provide a more detailed discussion of the differences. This could be elaborated in the related work section to clarify the distinctions between your approach and these existing methods.
2. The paper discusses the use of three modalities, image, text, and structure
but it appears to lack a clear explanation regarding how the raw embeddings for the structural modality are obtained. Neither the main body of the paper nor the appendix provides detailed information about the specific model or method used to generate raw embeddings for the structural modality.

Typos:

1. Page2 'constrative' maybe is 'contrastive'
2. The second-best method in the MRR indicator of the MKG-W dataset in Table 2 should be MMRNS (35.03), but it was incorrectly marked as IMF (34.50).

### Questions
1. Given that the expert networks rely on raw embeddings, how does the model ensure that sufficient diversity within each modality is captured? Are there mechanisms in place to mitigate the potential loss of key details due to the use of compressed embeddings?
2. Could you provide further clarification on the rationale behind using the conditional probabilities of different entities for disentanglement in formula 8? How does this approach ensure effective disentanglement between experts?
3. In the final case study, the authors visualize the weighting between modalities. How does the model distinguish and prioritize features within a single modality?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors argue the limitations of entity-wise embedding fusion in existing MMKGC work and introduce a new method, MoMoK, which can learn relation-guided entity representations for each modality. The experimental results demonstrate the superiority and robustness of MoMoK.

### Strengths
The paper is well-written, and I was able to grasp authors' motivation and the general process of MoMoK at first glance. The algorithm is clearly presented overall. The performance of MoMoK surpassed existing methods by a significant margin. Sufficient experimental evidence supports the robustness of MoMoK.

### Weaknesses
I think **the discussion of the importance of KG Completion task, especially its position in the context of the pervasiveness of LLMs today, is lacking**. This reduces the overall interest and significance of the work from the audience's perspective, considering LLMs' strong performance in general knowledge reasoning. I suggest the authors add a brief discussion in the introduction or in the last section. Additionally, several places lack detail and need clarification (see questions).



### Questions
1. In the second paragraph of Section 4.1, are $\mathcal{W}\_{m,1}$, $\mathcal{W}\_{m,2}$, ... learnable matrics? What are their shapes? Also, what is the exact operation in $\mathcal{V}\_{m,i}^{e}=\mathcal{W}\_{m,i}(e\_m)$? If it is just a simple multiplication, I feel using parentheses is improper. 
2. In Eq. (2), what is the purpose/function of the temperature $\varepsilon_r$?
3. In Eq. (3), I think the relation $r$ is missing in the components $P\_m(\hat{e}\_{m})$ and $P\_n(\hat{e}\_{n})$?
4. In line 266, where the joint score of each triple is treated as the sum of the scores across all modalities, did the authors try other designs, such as using only the '$J$' modality score? I am curious about the results of using only the '$J$' modality.
5. What's the setting of the number of experts (the value of $K$) in the main experiment? This should be described in the implementation details.
6. In Section 5.1, what is the difference between the MKG-W and MKG-Y datasets?

### Soundness
3

### Presentation
4

### Contribution
2
