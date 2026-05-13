# BioBridge: Bridging Biomedical Foundation Models via Knowledge Graphs

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Foundation models (FMs) learn from large volumes of unlabeled data to demonstrate superior performance across a wide range of tasks. However, FMs developed for biomedical domains have largely remained unimodal, i.e., independently trained and used for tasks on protein sequences alone, small molecule structures alone, or clinical data alone.
To overcome this limitation, we present \method, a parameter-efficient learning framework, to bridge independently trained unimodal FMs to establish multimodal behavior. \method achieves it by utilizing Knowledge Graphs (KG) to learn transformations between one unimodal FM and another without fine-tuning any underlying unimodal FMs.
Our results demonstrate that \method can
beat the best baseline KG embedding methods (on average by $\sim 76.3\%$) in cross-modal retrieval tasks. We also identify \method demonstrates out-of-domain generalization ability by extrapolating to unseen modalities or relations. Additionally, we also show that \method presents itself as a general-purpose retriever that can aid biomedical multimodal question answering as well as enhance the guided generation of novel drugs.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This submission tackles the problem of learning large multi modal ML models without requiring the pairwise cross modal dataset (as it is infeasible in where no of models >2). unlike recent work that aligns all modalities to a single modality, this submission takes a different approach of learning cross modal alignment transformation in embedding space while keeping the underlying unimodal fixed/frozen. Given Given an input embedding that was encoded by a unimodal model, the proposed submission transforms it to the embedding space of the target modality accounting for their relations. the cross modal alignment transformation is parametrized by a vanilla transformer module and learned with a contrastive loss. The proposed method is evaluated on several benchmarks/tasks such as protein protein interaction, protein-phenotype matching, cross modal retrieval where it outperforms several baselines.

### Strengths
- the problem of aligning large unimodal models efficiently is very relevant in general and even more so when the modalities are proteins, drugs and diseases (focus of this submission) as it opens up plethora of clinical applications.

- the problem is well motivated in introduction and contextualised. The paper is clearly written and easy to follow except one section (see below). 

- the idea of aligning the different embedding space of unimodal pretrained models with a cross modal transformation is sensible and simple. 

- experimental validation: evaluation of proposed s convincing on several benchmarks where the proposed method outperforms several baselines and in some cases is the only applicable solution. evaluation and applicability of the proposed method on cross modal retrival and gene-phenotype matching are quite interesting.

### Weaknesses
 - Presentation of Related work : Currently the submission only has one paragraph on knowledge graph learning and barely describes the embedding alignment literature e.g. in the context of cross modal retrieval (one of the application of proposed method), one can also mention deep CCA literature as Canonical correlation analysis (CCA) is the core of many cross modal retrieval methods.  

- Presentation of Methodology:  the submission should motivate the solution somewhat intuitively. Section 3.2 on encoding and transformation is very to the point and concise. the proposed methodology could be motivated better e..g by contextualizing wrt some prior work on KGE literature. Although there is a paragraph in the related work on KGE completion, the proposed method is not contexualized. Similarly, It is not very clear to me what parameters are optimized with contrastive loss since the submission keeps the pretrained model frozen. 

- Parameterization of alignment transformation as a transformer : the submission should also somehow motivate this choice wrt other options starting with simplest one such as a MLP or a vanilla autoencoder.

### Questions
Could the submission place the main assumptions and theorem from appendix into the main text? The appendix could include the proof.  I imagine this will make main paper more self contained and detailed. In the current form, methodology section is quite short.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces BioBridge, a novel framework for training across modalities (entities) that bridges independently trained uni-task models to establish cross-task abilities in biomedical domains. BioBridge employs contrastive learning to align entity representations and to facilitate learning of transformations between them. The resulting model demonstrates strong performance relative to several baseline knowledge graph (KG) embedding methods in retrieval tasks and highlights potential applications in the guided discovery of new drugs. Overall, BioBridge represents a promising approach for the integration of biomedical data resources and the enhancement of performance in various downstream tasks.

### Strengths
- This paper proposes a novel concept for learning across modalities via the bridging of knowledge graphs.
- The authors have conducted extensive experiments on various types of entity mapping and numerous approaches to tail entity prediction.
- With only the bridge module requiring updates during training, and all base feature models (FMs) remaining fixed, the proposed method is computationally efficient.
- Overall, the paper is well-written, with clear explanations of the methodology and empirical results.

### Weaknesses
 - The term "multimodal" as mentioned in this paper is confined to different types of biomedical entities. While the authors compare their work with "ImageBind," the experimental section lacks tasks that bridge text and image modalities, which are more complex and crucial for multimodal foundation models. Specifically, the absence of experiments involving image data, such as medical imaging, limits the scope of the claimed multimodality. The current framework only leverages modalities present within the knowledge graph, and therefore does not fully explore the potential of true multimodal learning across diverse data types.
- The learning process is guided by knowledge graphs, limiting the scope of "modalities" to those represented within biomedical knowledge graphs. Therefore, instead of the broad term "biomedical foundation model," it would be more accurate to describe it as a "biomedical knowledge graph foundation model." The reliance on KG structure for bridging modalities restricts the generalizability of the approach to scenarios where such structured knowledge is not available or is incomplete. This dependence raises questions about the method's applicability to novel biomedical entities or relationships not yet captured in existing KGs.
- The paper does not present ablation studies, such as evaluations of the contrastive learning objectives or hyper-parameter tuning. The lack of ablation studies makes it difficult to assess the contribution of individual components of the BioBridge framework. For example, it is unclear how the choice of the InfoNCE loss impacts performance compared to other contrastive losses, or how sensitive the method is to variations in batch size or learning rate. Without these studies, it is hard to isolate the factors that contribute to the observed results.
- The case study focusing on molecule generation is intriguing. Quantitative assessments of generation performance would be beneficial, for instance, by making direct comparisons with general-domain foundation models, or by offering more qualitative examples to demonstrate the efficacy of the proposed framework. The current evaluation lacks a clear benchmark against existing molecule generation methods, making it challenging to determine the practical utility of the proposed approach.
- The baseline comparisons are predominantly with knowledge graph link prediction methods. It is unclear whether the observed advantages stem from the effective transformation learning of the proposed method or from the knowledge supervision of the biomedical knowledge graph. The comparison should include more diverse baselines, such as methods that do not rely on knowledge graph supervision, to better isolate the contribution of the proposed bridging mechanism.
- This paper omits a discussion on limitations and potential failure modes. The authors are strongly encouraged to offer deeper insights into the generalizability of BioBridge. A discussion of the scenarios where the method might fail or underperform is crucial for a comprehensive understanding of its capabilities and limitations.

### Questions
- Can the proposed method be applied to other types of downstream tasks, such as image captioning and visual question answering? If applicable, could the authors provide empirical results and case studies?
- Could the author offer a more detailed explanation of the compared baselines? Specifically, how are they trained, and can they also learn from an external biomedical knowledge graph to ensure a fair comparison?
- Would employing different contrastive learning objectives, such as SimCLR or MoCo, in place of InfoNCE, impact the performance?
- Also, please refer to weaknesses for other concerns.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes BioBRIDGE to bridge unimodal FMs, keeping each FM fixed. BioBRIDGE utilizes a multi-modal knowledge graph to learn cross-modal relationships of entities. Compared to multi-modal FMs and ImageBind, BioBRIDGE is parameter efficient. The experiments on cross-modal retrieval tasks demonstrate the effectivness of BioBRIDGE. The paper also shows that BioBRIDGE has good generalization ability.

### Strengths
1. The idea of bridging several unimodal FMs is novel. 
2. The paper is well written and easy to follow.
3. Compared to existing studies, BioBRIDGE keeps all unimodal FMs fixed and thus is parameter efficient.

### Weaknesses
1. The reasons of using contrastive learning is not clear. It would be better to provide further explanation and experimental supports. Specifically, the paper should clarify why the InfoNCE loss was chosen over other contrastive losses, and what specific benefits it provides in this context. Furthermore, the paper lacks ablation studies to demonstrate the impact of different contrastive learning parameters on the final performance. For example, the temperature parameter in InfoNCE can significantly affect the results, and this should be explored.
2. The baselines in Section 4.1 are several years ago. No recent studies are included. The baselines used for comparison in the cross-modal retrieval tasks are not state-of-the-art. The paper should include more recent methods, particularly those that leverage multi-modal embeddings, to provide a more comprehensive evaluation. The absence of these comparisons makes it difficult to assess the true performance of the proposed method.

### Questions
1. What are the contributions of the contrastive learning?
2. How about the influence of the knowledge graph on this method? From your perspective, what could be the challenges if BioBRIDGE is adapted to other domains?
3. For the cross-modality retrieval tasks, are the baselines trained on single modality or multiple modalities? Why not include multi-modal embedding methods published recently?

    a. Lu X, Wang L, Jiang Z, et al. MMKRL: A robust embedding approach for multi-modal knowledge graph representation learning[J]. Applied Intelligence, 2022: 1-18.

    b. Cao X, Shi Y, Wang J, et al. Cross-modal knowledge graph contrastive learning for machine learning method recommendation[C]//Proceedings of the 30th ACM International Conference on Multimedia. 2022: 3694-3702.

    c. Zhu J, Huang C, De Meo P. DFMKE: A dual fusion multi-modal knowledge graph embedding framework for entity alignment[J]. Information Fusion, 2023, 90: 111-119.
4. Though it is easier to collect unimodal data than to collect paired data from two modalities, could the model trained on the paired data perform better or competitively to model trained on the large unimodal data?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes to bridge multiple biological modalities through KG. The motivation is that most of the data are uni-modal, paired data is scarce and due to the combinatorial explosion, infeasible to collect and train a multi-modal model. The author learns a transformation layer among the uni-modal representations to achieve multi-modal learning.

### Strengths
- Interesting problem setting on bridging multi-modal FMs in biology. Makes intuitive sense.
- Interesting approach on the bridge module
- Lots of interesting applications and analysis

### Weaknesses
 - The method proposes several new modules that lack motivation and seem ad hoc.
- The clarity of the technical methods of the paper can be improved
- Looking at equation 1, the transformation seems dependent on the (1) target modality node type and (2) relation type and (3) individual node in the target modality. For example, given the same node drug, it could have one transformed representation for protein A, a different one for protein B, and a different one for disease, etc. Is that right? Could the authors describe the design choice of this? why not map all of them into a single unified space? This brings a separate question: how do you conduct a similarity search if the embedding is dependent on individual node?
- The transformation loss function (eq.2) makes intuitive sense, but there seem to be numerous other options to achieve similar goals such as self-supervised link prediction. Have the authors experimented with other transformation techniques? if so, could the authors provide any additional information? if not, could the authors describe the motivation on why choosing this particular approach? 
- The author uses a transformer model to achieve the transformation. It seems unnecessary since it is just encoding 4 embeddings? Have the authors experimented with other simpler approaches?
- How are the negative samples created? 
- For individual application, is the model trained on every possible bridge transformation or is the model different for each application and individual task?
- Cross-modality retrieval seems to be exactly link prediction. In that case, there are numerous approaches for GNN-based link prediction that is missing as a baseline and has shown much better performance compared to the KG embedding methods. Have the authors compared to any of the latest link prediction method? 
- For semantic similarity task, I worry that there is data leakage. Since the protein node is connected to these GO terms in the PrimeKG, the embedding already implicitly knows the labels during training. Have the authors addressed this concern by conducting some holdout protein-go links?
- For PPI, since it is the same modality between the head and tail nodes, why do we need bridge module? 
- For cross-species task, why is phenotype not available? it seems to be available in PrimeKG? 
- For the multi-modal generation, it is an interesting application, but have the authors checked if the retrieved list is novel predictions or existing links? It will be great to compare with a baseline that is just retrieving the top K entities in the KG and show the difference on answers.

### Questions
- Looking at equation 1, the transformation seems dependent on the (1) target modality node type and (2) relation type and (3) individual node in the target modality. For example, given the same node drug, it could have one transformed representation for protein A, a different one for protein B, and a different one for disease, etc. Is that right? Could the authors describe the design choice of this? why not map all of them into a single unified space? This brings a separate question: how do you conduct a similarity search if the embedding is dependent on individual node?
- The transformation loss function (eq.2) makes intuitive sense, but there seem to be numerous other options to achieve similar goals such as self-supervised link prediction. Have the authors experimented with other transformation techniques? if so, could the authors provide any additional information? if not, could the authors describe the motivation on why choosing this particular approach? 
- The author uses a transformer model to achieve the transformation. It seems unnecessary since it is just encoding 4 embeddings? Have the authors experimented with other simpler approaches? 
- How are the negative samples created? 
- For individual application, is the model trained on every possible bridge transformation or is the model different for each application and individual task?
- Cross-modality retrieval seems to be exactly link prediction. In that case, there are numerous approaches for GNN-based link prediction that is missing as a baseline and has shown much better performance compared to the KG embedding methods. Have the authors compared to any of the latest link prediction method? 
- For semantic similarity task, I worry that there is data leakage. Since the protein node is connected to these GO terms in the PrimeKG, the embedding already implicitly knows the labels during training. Have the authors addressed this concern by conducting some holdout protein-go links?
- For PPI, since it is the same modality between the head and tail nodes, why do we need bridge module? 
- For cross-species task, why is phenotype not available? it seems to be available in PrimeKG? 
- For the multi-modal generation, it is an interesting application, but have the authors checked if the retrieved list is novel predictions or existing links? It will be great to compare with a baseline that is just retrieving the top K entities in the KG and show the difference on answers. 



I am happy to raise score if the authors address my questions.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
