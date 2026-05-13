# DSparsE: Dynamic Sparse Embedding for Knowledge Graph Completion

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Addressing the incompleteness problem in knowledge graph remains a significant challenge. Current knowledge graph completion methods have their limitations. For example, ComDensE is prone to overfitting and suffers from the degradation with the increase of network depth while InteractE has the limitations in feature interaction and interpretability.
    To this end, we propose a new method called dynamic sparse embedding (DSparsE) for knowledge graph completion.
    The proposed model embeds the input entity-relation pairs by a shallow encoder composed of a dynamic layer and a relation-aware layer.
 Subsequently, the concatenated output of the dynamic layer and relation-aware layer is passed through a projection layer and a deep decoder with residual connection structure. 
 This model ensures the network robustness and maintains the capability of feature extraction.
    Furthermore, the conventional dense layers are replaced by randomly initialized sparse connection layers in the proposed method, which can mitigate the model overfitting.
  Finally,
 comprehensive experiments are conducted on the datasets of FB15k-237, WN18RR and YAGO3-10.
 It was demonstrated that the proposed method achieves the state-of-the-art performance in terms of Hits@1  compared to the existing baseline approaches.
 An ablation study is performed to examine the effects of the dynamic layer and relation-aware layer, where the combined model achieves the best performance.

\keywords{Knowledge Graph  \and Graph Completion \and Link Prediction \and Sparse Embedding.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new architecture of neural networks, the DSparsE, for graph completion. It is a link prediction model structure that uses only MLP layers and employs sparse and residual structures to alleviate overfitting, and reduce the difficulty of training deep networks. The paper provides performance comparison of various knolwege graph embedding techniques across two datasets.

### Strengths
- The proposed architecture utilizes various methods to prevent some of the well known problems, especially the overfitting problem which is important for knowledge graph completion.
- The paper provides ablation studies to show the benefit of implementing proposed methods.

### Weaknesses
 - Better explanations can be included. For instance, the paper states the expert kernels, but does not explicitly explain what is the expert kernels or why it is "expert".
- Better figures and figure captions can be written. The architecture figures are small and the explanations in the captions is very limited.
- Some statistical testings (or critical plots) for the comparing methods would make the arguments of the paper stronger.
- Comparison of computational time would be necessary to address the computational complexity problems in the existing methods.

### Questions
- What is an expert kernel?
- How does the model do in the case of no experts? Or simple mean of the outputs of k different mlps.
- How is imposing sparse structure different from the drop-connect (dropout on the weights)
- Why does the dynamic structure enhance the robustness of the model? Is it by some form of ensembling?
- How statistically different are the results between the models (or at least the top competing ones).
- How does the model perform in terms of computational complexity?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel dynamic sparse embedding method DSparsE for knowledge graph completion task. The DSparsE is proposed to solve the drawbacks of prone to overfitting and constraints on network depth of ConDensE and the limitation in feature interaction and interpretability of InteractE. DSparsE includes three main modules, the dynamic MLP layer and the relation-aware MLP layer in the encoder, and residual blocks in the decoder, and it named as DSparsE because the sparse MLP is applied. DSparsE is evaluated on two common KGC benchmarks, FB15k-237 and WN18RR. The results show DSparsE is effective for KGC task.

### Strengths
1. Authors tried to investigate how powerful the MLP is for KGC task by developing model based on pure MLP layers. This is significantly different to existing methods and very interesting. 
2. Though the experiment results of DSparsE is not comparable to state-of-the-art. But it shows DSparsE is effective for KGC tasks.

### Weaknesses
1. Though the overall model architecture is novel, the key advantage of pure MLP-based model such as DSparsE is unclear. As I understand, it is not efficiency since 15(35) experts are set for FB15k-237(WN18RR) with each expert represented by an MLP layer, which will introduce a lot extra parameters compared to 1 expert. It is also not superior performance, since the link prediction results of DSparsE is comparable to existing methods, such as RESCAL and ComDensE. The use of multiple experts, each being an MLP, significantly increases the parameter count without a clear demonstration of a substantial performance gain over simpler models. The computational cost associated with these additional parameters is also a concern, especially given the comparable performance to existing methods.

2. How do the different modules affect the performance of DSparsE is not well illustrated. For example, the output vectors from Dynamic MLP layer and the Sparse Relation-aware Layer are concatenated into one vector as the input of the decoder. It is unclear the output vector of which affects the results more significantly. The paper lacks a detailed ablation study to quantify the contribution of each module, particularly the dynamic MLP and the relation-aware layer. Without this analysis, it's difficult to understand the importance of each component and how they interact to achieve the reported results. The impact of concatenating the outputs of these two layers is also not clear.

3. Some minor points:
* In Table 2, the best MRR result on FB15k-237 should be 0.396 from ConvKB. 
* Both the blue line and orange dashed line represents marked as "with residual structure", it is a bit confusing.

### Questions
1. What is the key advantages of designing KGC models with pure MLP layers compared to the existing methods, such as tensor-decomposition models and translational models introduced in the related works? 
2. The definition of deep learning models is unclear. Is the graph neural network model be deep learning models? Why are translation models not deep learning models?
3. The output vectors from Dynamic MLP layer and the Sparse Relation-aware Layer are concatenated into one vector as the input of the decoder. Which vector affect the results more? 
4. What is the number of parameters of DSparsE model for FB15k-237 and WN18RR?  Is the number of parameters of DSparsE significantly more than baseline methods?
5. The results of 100 depth of the residual structures. Is this mean that 100 residual MLP blocks are used in the model? If yes, how long does it take to train the model?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes DSparsE, a novel knowledge graph link prediction model.  This model introduces a dynamic layer into the encoding end and a residual structure into the decoding end. Moreover, this model achieves a significant reduction in the number of parameters and a significant improvement in the efficiency by substituting the fully connected layer with a sparse layer. Extensive experiments demonstrate that DSparsE consistently outperforms existing state-of-the-art methods.

### Strengths
1. The paper is clearly written and easy to follow.
2. This model combines dynamic layer and residual structure, wwhich enables neural networks to better perform information fusion

### Weaknesses
1.	The number of datasets is only 2, relatively limited.
2.	The supplementary experiments in this article are not sufficient. For instance, Figure 4 provides a comparison between DSparseE and one baseline on a single dataset. Both the number of baselines for comparison and the diversity of datasets should be increased. Additionally, Figure 5 only illustrates three scenarios of expert quantity, making it challenging to discern a clear and definitive trend. In Figure 6, the blue and orange lines are difficult to interpret. The author mentions that these are results with different numbers of residual layer depth but fails to provide specific numerical values for these quantities. The inadequacy of supplementary experiments has compromised the rigor and credibility of the results.
3.	In the "Contribution" section, the authors claim that their model achieves a significant reduction in the number of parameters and a significant improvement in model efficiency. However, the subsequent text does not provide a particularly clear substantiation of this claim. It would be beneficial to provide more explicit details, such as in terms of runtime or the exact number of parameters, to support this assertion.

### Questions
1.	Can you add more datasets?
2.	Can you improve the supplementary experiments?
3.	Can you provide more explicit details of the improvement of the efficiency?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a knowledge graph link prediction model DSparsE, in which the dynamic layer and residual structure are incorporated to achieve higher efficiency. Experimental results on two datasets show its effectiveness.

### Strengths
1. The motivation of this paper is easy to understand.
2. The proposed model seems technically reasonable.

### Weaknesses
1. The difference and the superiority of DSparsE compared with baseline models are unclear. 
2. The contribution of this paper is limited. It only combines some existing techniques.
3. The current version of this paper is not easy to follow. There are some uncommon words without explanation, such as "reminiscent".
4. The citation and analysis of previous models are insufficient.
5. More datasets are required to verify the effectiveness of the proposed model.
6. More experimental results about the scalability of the proposed model should be provided.

### Questions
None

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
