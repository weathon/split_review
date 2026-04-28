# EffoVPR: Effective Foundation Model Utilization for Visual Place Recognition

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
The task of Visual Place Recognition (VPR) is to predict the location of a query image from a database of geo-tagged images. Recent studies in VPR have highlighted the significant advantage of employing pre-trained foundation models like DINOv2 for the VPR task. However, these models are often deemed inadequate for VPR without further fine-tuning on task-specific data.
In this paper, we propose a simple yet powerful approach to better exploit the potential of a foundation model for VPR. We first demonstrate that features extracted from self-attention layers can serve as a powerful re-ranker for VPR. Utilizing these features in a zero-shot manner, our method surpasses previous zero-shot methods and achieves competitive results compared to supervised methods across multiple datasets.
Subsequently, we demonstrate that a single-stage method leveraging internal ViT layers for pooling can generate global features that achieve state-of-the-art results, even when reduced to a dimensionality as low as 128D. Nevertheless, incorporating our local foundation features for re-ranking, expands this gap. Our approach further demonstrates remarkable robustness and generalization, achieving state-of-the-art results, with a significant gap, in challenging scenarios, involving occlusion, day-night variations, and seasonal changes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an effective approach for visual place recognition (VPR) using a foundation model (DINOv2). The features extracted from the self-attention layers are used as re-ranker for VPR. Experiments on several datasets show the proposed method is robust and effective.

### Strengths
1. The proposed method is easy to follow. It leverages the foundation model’s feature representation capability to improve the effectiveness of image retrieval and re-ranking. 

2. The proposed method outperforms some existing approaches on several VPR benchmarks.

### Weaknesses
1. Since the proposed method mainly leverages the strong representation power of a foundation model (DINOv2), the technical novelty of the proposed method in VPR is somewhat incremental. 
2. Certain design choices, such as using the V_l matrix for keypoint descriptors, lack clear motivation and justification, particularly in explaining why such choices are effective. The paper does not sufficiently explore the impact of using different attention facets (K, Q, V) for keypoint detection and description. A more thorough ablation study is needed to understand the contribution of each component.
3. Although the proposed method outperforms several existing methods, the improvement could come solely from using a stronger foundation model feature representation. Therefore, the comparison may not be fair. The paper should include a more detailed analysis of the performance gains, specifically isolating the contribution of the proposed keypoint extraction and descriptor method from the base feature representation.
4. The computational complexity and memory footprint of the proposed method should be discussed and compared with other existing methods. The paper lacks a detailed analysis of the computational cost associated with the proposed method, including both training and inference time, as well as memory requirements for storing intermediate feature maps and descriptors. This is critical for practical applications.
5. It would be good to also show some failure cases and provide analysis. The paper should include a qualitative analysis of failure cases, discussing the reasons behind the failures and providing insights into the limitations of the proposed method.

### Questions
Please see the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a new method, called EffoVPR, to effectively use vision foundation models for visual place recognition. This method leverages the output class token of the DINOv2 model to generate global features to retrieve candidates. It also uses ViT internal attention matrices to obtain local features for re-ranking these candidates. EffoVPR achieves good zero-shot performance. After training on the SF-XL dataset with the EigenPlaces framework, it outperforms previous SOTA methods on several VPR datasets.

### Strengths
1.	The methods proposed in the paper are generally novel.
2.	The experiments provided in the paper are sufficient. The author provides the results of other SOTA methods on datasets such as SF-XL. As far as I know, completing such evaluation experiments requires a lot of time and effort.
3.	The performance of the proposed method is really good. It achieves excellent results even with compact global features.

### Weaknesses
1.	The methodological contribution of this paper is a little weak. Its training strategy follows the EigenPlaces work. The global feature is the class token (following a linear layer) of the ViT model. The local matching in the re-ranking process is based on the mutual nearest neighbors searching, and it also already exists. I think the authors should state that the previous SelaVPR work also does not require spatial verification in re-ranking. The biggest contribution of this work seems to be the use of the internal self-attention matrices to yield selected local features, which is meaningful but maybe not enough.
2.	The proposed method is trained on SF-XL, which is a very large dataset and time-consuming to train. If training on other datasets, such as GSV-Cities or even MSLS/Pitts30k. Can it still achieve such good results? If the proposed method cannot extend to other training sets, it is better to have an appropriate explanation in the paper.
3.	The proposed method uses 224×224-pixel images for training, while 504×504-pixel images for evaluation. Using the DINOv2-large model to process such high-resolution images is time-consuming and memory-consuming. Although the paper gives results using low-resolution images on MSLS and Tokyo247, I think it is also necessary to give a comparison of GPU memory usage, and better to provide results on more datasets (e.g., Nordland and SF-XL-Night).

### Questions
see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a method that uses DINOv2 foundation model to address the Visual Place Recognition task. This is achieved by retrieving the top-K most similar candidates in the first stage by measuring the similarity of (finetuned) DINOv2’s [CLS] tokens between the query and the candidate images. In the second stage, the proposed approach re-ranks the retrieved candidates using local features computed using the Queries, Keys and Values from the self-attention module of an intermediate DINOv2 layer. The method outperforms other state-of-the-art zero-shot approaches, as well as supervised methods when the last layers of the DINOv2 network are finetuned. Moreover, the proposed method achieves results competitive with the supervised methods even when using only the first stage of the method.

### Strengths
- S1: The paper is clear and easy to read.

- S2: Simple, yet effective and robust method that improves the performance over the DINOv2 baseline and other state-of-the-art methods, while reducing the required dimensionality of the used features.

- S3: The method finetunes DINOv2 to achieve better performance but is still effective even in a zero-shot setting.

### Weaknesses
 - W1 Even though the results of the three proposed variants of the method (EffoVPR-ZS, EffoVPR-G and EffoVPR-R) are provided, the paper is missing their comparison in a single table, to directly see how large is the effect of finetuning and re-ranking. It would be good to see this comparison in a single table to understand (and compare) the direct benefits of the different components of the proposed approach. 

- W2 The notation for Queries, Keys and Values and corresponding local features would be more readable if the layer index would be consistently used always as superscript or always as subscript ($V_l$ versus $v^l_i$). Alternatively, since the Queries, Keys and Values are always taken from the same layer, maybe the layer index could be completely omitted for better readability.

- W3 What are the failure cases and limitations of the main presented method, EffoVPR-R? The paper contains only failure cases for the zero-shot setting. It is important to understand the failure modes of the full method, not just the zero-shot variant, to assess its robustness in practical scenarios.

### Questions
- Q1: The paper shows that EffoVPR-R achieves SOTA results even with K=5. I am curious, how much does this change for the zero-shot setting. I.e., when the last layers of DINOv2 are not finetuned, is it also sufficient to use K=5, or would K need to be increased?

- Q2: It should be clearly stated that the ablations in the appendix we done using the EffoVPR-R. Would it be possible to confirm this?

- Q3: The re-ranking stage requires storing local features for the re-ranked images. It would be good to add discussion and analysis of memory requirements for the proposed approach and in particular the memory requirements to store the local features for spatial re-reranking.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents a model for visual place recognition, specifically aimed at achieving robust zero-shot retrieval performance. The model uses a Vision Transformer (ViT) with DINOV2 weights as its backbone to identify nearest neighbors based on global feature similarity, followed by a mutual nearest neighbor (NN) re-ranking strategy to pinpoint the closest reference image using local features. For training, the Eigenplace paradigm is applied to promote view invariance in the ViT. Only the final layers of the backbone are fine-tuned, with the rest of the model kept frozen. Fine-tuning was performed on the SF-XL dataset, and testing was conducted on several benchmarks: Pitts30k, Tokyo24/7, MSLS-val, and MSLS-challenge, as well as more challenging datasets, including Nordland, Amsterdam Time, SF-XL Occlusion, SF-XL Night, SVOX Night, and SVOX Rain.  For contribution, EffoVPR proposed a novel reranking architecture that does not require training and works well even with a small number of candidates.  The paper also claims to demonstrate the lack of need for aggregate methods to capture local features

### Strengths
Performance: 
EffoVPR achieves SOTA performance by performing better than previous recent SOTA models such as SALAD and EigenPlaces.  In particular, EffoVPR performs significantly better on the more challenging datasets  
EffoVPR is able to fine tune on cities in SF XL but then perform very well on Nordland which is mainly rural and natural scenes taken from a train. 
EffoVPR has very impressive zero shot performance compared to other zero shot methods and some trained models, showing effectiveness of reranking model 
EffoVPR with only the first stage also performs very well  
Architecture: 
The architecture for EffoVPR is intuitive and simple to understand 
Efficiency: 
EffoVPR utilizing only reranking during evaluation makes training efficient and fast, as the reranking does not need to be trained 
Experimentation: 
Paper presents very detailed ablation studies on the choice of layer for reranking, the different thresholds, which layer to choose reranking features for, etc.   
Papers shows the model being performed on a wide range of datasets.

### Weaknesses
Performance:
Model does not perform better than other models by a significant margin on the less challenging datasets.  However, the less challenging datasets are already inferred very well by the other datasets so there’s not as much room for improvement.   
Paper is not entirely clear how much the reranking contributes to performance compared to DINOV2
Novelty:
In contribution, the paper claimed “We introduce a novel image matching method for VPR that relies on keypoint detection and descriptor extraction from the intermediate layers of a foundation model”.  However, R2Former also uses filtered local features from intermediate layers from the VIT backbone. Perhaps need to change wording to reflect true level of novelty.

The paper mentions reduced memory footprint, but only shows dimension of global feature and not other aspects such as parameter size (ex. R2Former uses VIT-S whereas EffoVPR uses VIT-L but is not reflected anywhere on paper)

Training:
T1, T2, along with which layer to get feature map all being fixed hyperparameters means there’s more manual tuning involved to achieve optimal results

### Questions
The paper mentions time evaluation, but only shows time evaluation on the first step and not the reranking.  From the look of the model, the time of reranking doesn’t seem to be particularly time efficient.  How fast is the reranking?  

The paper mentioned memory efficiency and reduced memory footprint.  Quantitatively, how much memory consumption does the modal overall take compared to the other models? 

On the ablation on T1 and T2, table only shows the result with different T1 and different T2, but didn’t specify what the other filter value is (ex. On table S5, When showing performance when T1 equals 0.05 and 0.10, it didn’t specify what T2 is when evaluating).  What is the value of T2 when evaluating for table S5 and what is the value of T1 when evaluating for table S6? 

How well does the model do on the Pittsburgh 250k dataset? 

Are there experimental results of EffoVPR trained on other datasets other than SFXL? 

In the Eigenplaces paper which the training process of EffoVPR seems to be heavily based on, the backbone was completely trained.  How well would the model perform if every layer of the backbone was trained? 

Paper mentions that only the “final layers” are trained.  What are the final layers that are trained? 

Paper calls itself a “foundational model”, which should be able to be used for multiple tasks, yet only same view matching capability is shown in the paper.  Can the model be used for other tasks like cross view matching or detection? 

Could the global descriptor be used also during the reranking phase to further filter out the nearest neighbors, perhaps to only neighbors that belong in the same predicted cell? 

How well does the model perform with anyloc as backbone rather than DINOV2?

### Soundness
3

### Presentation
3

### Contribution
2
