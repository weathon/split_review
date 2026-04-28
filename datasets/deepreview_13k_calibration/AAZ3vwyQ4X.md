# Multimodal Structure Preservation Learning

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 1, 3, 3

## Abstract
When selecting data to build machine learning models in practical applications, factors such as availability, acquisition cost, and discriminatory power are crucial considerations. Different data modalities often capture unique aspects of the underlying phenomenon, making their utilities complementary. On the other hand, some sources of data host structural information that is key to their value. Hence, the utility of one data type can sometimes be enhanced by matching the structure of another. We propose Multimodal Structure Preservation Learning (MSPL) as a novel method of learning data representations that leverages the clustering structure provided by one data modality to enhance the utility of data from another modality. We demonstrate the effectiveness of MSPL in uncovering latent structures in synthetic time series data and recovering clusters from whole genome sequencing and antimicrobial resistance data using mass spectrometry data in support of epidemiology applications. The results show that MSPL can imbue the learned features with external structures and help reap the beneficial synergies occurring across disparate data modalities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a multimodal framework called MSPL, which builds upon encoder decoder structure with extra regularizations form prediction task and structure loss.

### Strengths
I think the paper has several strenghs: 
1: It presents a flexible framework that can incorporate different modality as inputs, incorporating various loss functions and clustering objectives
2: It addresses a real-world problem in epidemiology (using MALDI data as a cost-effective alternative to WGS)
3: It introduces a new cluster evaluation metric (cluster F1 score)

### Weaknesses
This paper has several areas that can be improved:
1: lt could benefit from more extensive comparison with other multimodal learning approaches. Specifically, the paper lacks a thorough comparison against methods that handle similar data scenarios, even if not directly identical. The current comparisons are limited, and a more comprehensive analysis is needed to justify the novelty and effectiveness of the proposed framework.
2: Authors could explore more sophisticated structure preservation objectives. The three losses are common objective functions in multimodal and VE/VAE variants. Besides, there is limited discussion of the impact of different encoder architectures. The choice of loss functions seems somewhat arbitrary, and a more detailed analysis of their impact on the final performance is needed. Furthermore, the paper does not explore different encoder architectures, which could significantly impact the quality of the learned representations. The lack of ablation studies on these aspects makes it difficult to assess the robustness of the proposed method.
3: Model needs further optimization. Even comparing with its own variants, the proposed model cannot outperform them in most cases. The performance of the proposed model is inconsistent, and it does not consistently outperform its own variants across different datasets. This suggests that the model might be overfitting to specific datasets or that the optimization process is not robust enough. The paper needs to provide more details on the optimization process and explore techniques to improve the model's generalization capabilities.
4: I am not sure if it can handle a large number of clusters or clusters with imbalanced sizes. The paper does not provide any analysis of the model's performance with a large number of clusters or with imbalanced cluster sizes. This is a critical limitation, as many real-world datasets have these characteristics. The lack of discussion on these aspects makes it difficult to assess the practical applicability of the proposed method.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper presents an approach to multimodal representation learning that leverages an autoencoder along with a combination of 3 loss functions (reconstruction, pretext task performance and structural alignment) in order to learn representations of the data that preserve the structure in one of the modalities (represented by a dissimilarity matrix) without requiring the raw data itself.
 
The authors apply the method in the context of epidemiology, where mass spectrometry data is becoming a potentially valuable tool for outbreak detection but is limited in power compared to whole genome sequencing, which can be a prohibitively labor-intensive and costly approach. They present the method as a way of integrating these modalities. The method is evaluated on a simulated dataset, a public dataset of paired MALDI spectra and antibiotic resistance data, and a proprietary dataset of WGS structural data and MALDI spectra. To evaluate, the authors compare their proposed method (MSPL) to two baseline methods that they construct without the structure alignment loss function, and evaluate clusterings based on the resulting representations using a variety of extrinsic clustering metrics with respect to ground truth.

### Strengths
The concept of preserving structure level alignment without need for the entire dataset is interesting, and the proposed approach appears to be novel. The application of multimodal deep representation learning approaches of this kind to mass spectrometry data in the context of epidemiology is particularly original and exciting.
 
The method is very clearly described, as is the evaluation approach and the metrics used. In evaluating, the authors considered extrinsic clustering metrics that went beyond more common approaches such as ARI and NMI, which greatly assist in the interpretation of the results.
 
Additionally, the authors evaluate the method on multiple datasets, including a variety of simulations and two real-world datasets, which are well-described.

### Weaknesses
The paper has several significant weaknesses. 

First, the significance of the method’s real-world impact in the application area is somewhat unclear. The introduction states that the main utility of the learned representation in this context is that it could replace WGS in practice as a more cost-effective alternative; however, the method seems to require SNP distances between each pair of samples (and thus WGS for every sample) as an input in order to learn the representation. As such, it is not clear how such representations would be learned without doing WGS first – thus incurring the same costs as would be necessary to do outbreak detection in the usual way. This somewhat reduces the perceived contribution of the work. 

The evaluation approach is also a major weakness of the paper. The performance of the model is poor in many cases, and the proposed metrics make it very difficult to understand why. Cluster purity, precision, recall and F1 scores for clustering have already been defined in existing literature  – see the chapter on “Evaluation of Clustering” in Information Retrieval by Manning. In order to deal with the challenge of comparing clusters of different sizes and number, precision, recall and F1 score are typically defined with respect to the cluster memberships of sample pairs. However, the paper defines these metrics very differently: with respect to purity, which is easy to achieve when cluster sizes are large, and makes the results very difficult to interpret. For example, while the F1 scores seem generally high, they appear to be driven predominantly by a sharp increase in recall. Figure 6 demonstrates that MSPL learns many fewer clusters than the ground truth – if MSPL is also learning fewer or larger clusters than the baseline models, then this could easily explain the increase in the purity-based recall metric. Although the purity-based precision metric decreases in these cases, it could also be artificially inflated or otherwise biased by cluster size or distribution. Unfortunately, the number of clusters learned in each experiment is not reported, which makes evaluation even more difficult. The NMI and ARI metrics are designed to account for these potential sources of bias, but the authors were not able to demonstrate that MSPL consistently outperforms the baselines according to these metrics in real-world data. Overall, the evaluation approach should be reformulated to be consistent with the literature and the results require much more investigation.
 
The choice of baselines is also a substantially limiting factor. While the authors construct two baselines, the paper does not make any comparison of MSPL to existing methods. While relevant deep learning approaches may be limited, there are many papers on late integration multi-view clustering approaches, which integrate multiple modalities using only clustering labels or dissimilarity matrices and not the original data (see, e.g. “Multi-omic and multi-view clustering algorithms: review and cancer benchmark” by Rappaport et al for a brief review of such approaches). Since the evaluation in the paper is based entirely on the quality of clustering based on the learned representation, this class of methods seem very relevant. Furthermore, there is no attempt to evaluate how well the model performs in comparison to models that leverage the entire dataset rather than just the distance-based structure. This makes it difficult to evaluate the real-world utility of the method.

Finally, there is no reproducibility statement and no mention of code or data being made available.

### Questions
The above comments raise some broader questions regarding the method and particularly the evaluation approach. Some more specific questions are listed below:
 
- Regarding the choice of the custom loss function for SNP distance, the choice to impose no penalty when feature distance and SNP distance both exceed 15 seems confusing. The cited source suggests that a distance <= 5 indicates a definite transmission  <= 15 indicates probable transmission. When clustering this data, might it also be useful to have a representation that accurately captures the relationships between samples that are even somewhat less likely to cluster together? If so, it could make sense to either relax this constraint or try a different normalization approach (such as log transforming the SNP distances).

- The model requires the choice of a pretext task, and the authors suggest that the difficulty of the pretext task does not affect MSPL’s ability to preserve structure. What, then, is the effect of the pretext task on the learned representation, and how should a user choose the pretext task for their particular application?  
 
Some minor comments on Figure 5 that did not affect my score:
-  e) and f) are missing species labels.
-  The paper claims that F1 lift and species diversity are correlated based on c) and e) – a regression line or correlation statistic would be helpful to back up this claim.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposed a domain adaptation method that learns the data distribution structure in one modal and transfer it to the other modal. They applied it to the problem of hospital outbreak detection that using MALDI and whole genome sequencing.

### Strengths
The stated problem is pervasive in biomedical applications and is challenging.

### Weaknesses
1) This is a typical subset of domain adaptation problems. However, they did not include SOTA domain adaptation methods into the baseline. The baseline methods are weak.
2) Also, from references we see that there are already methods that perform prediction tasks directly based on MALDI, which were not compared.
3) The experiments are carried out only on MALDI-WGS datasets and most are synthetic datasets. Due to the small-sample nature of these problems, the models are vulnerable to short-cut learning and testing on several similar datasets is not reliable. I don't see any reason that the problem should be restricted on MALDI-WGS data. There are lots of two-domain problems with similar character in biomedical fields and the data should be tested on more types of applications.

### Questions
How does the "seasonal and trend components" in the synthetic datasets related to MALDI-WGS matching?

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
3

### Summary
The authors propose the Multimodal Structure Preservation Learning (MSPL) approach that learns data representations utilizing clustering structure in one data modality to inform upon the other modality using a regularization approach towards compliance of this clustering structure when learning representations. The approach is applied to synthetic as well as whole genome sequencing (WGS) and antimicrobial resistance datasets. Rather than learning a shared feature space the approach thus relies on gross structural information at the level of groups exploring alignment according to the dissimilarity-based clustering learned by the opposing modality. The approach relies on three tasks, an autoencoder for learning representations, a pretext discriminatory task, and  alignment of the two modalities clustering structure formulated as a multiobjective function reflected in three loss terms with associated relative weights. Apart from conventional ARI and NMI cluster validity metrics the authors further propose a cluster-based F1 score. The approach is compared against two model ablations (baselines) not having the structure preserving loss and classifying the cluster groups respectively as opposed to operating on dissimilarities.

### Strengths
The approach is useful and enable to integrate information of multiple (two) modalities taking overall structural information into account from the opposing modality.

The considered problem domain is interesting and the approach’s seem to enhance the learned representations in terms of cluster level structures.

The paper is well written and easy to follow.

### Weaknesses
The methodological contribution of the paper is very limited and rather straightforward combining three loss components. As such, the contribution seems rather incremental and limited in scope.

The contribution of the F1 metric is also straightforward and does not contribute much in terms of novelty.

The comparisons are very limited only considering simple model ablations but not any alternative state-of-the-art methodology for the same problem domain.

The results are not overly convincing with the approach working better than baselines in some situations and not in other.

Overall I find the contribution of limited novelty and the experimentation not overly convincing - and therefore do not recommend publication at this point.

### Questions
It would be good to further discuss how to suitable tune the contribution of each loss term.

How is the approach influenced by initialization conditions?

How does architectural choices influence the model and why is UNETs chosen as the backbone as opposed to other architectures such as transformer based architectures?

Why is the approach not compared to any existing SOTA approaches within the domain or similar domains for instance based on the approaches reviewed in related work?

The results are also not that surprising in that regularizing towards a clustering structure will enhance such learning of the clustering structure. It would in this context be interesting to see if the regularization also improves upon the pretext class and contrast this to other methodologies directly learning the pretext class.

### Soundness
3

### Presentation
2

### Contribution
2
