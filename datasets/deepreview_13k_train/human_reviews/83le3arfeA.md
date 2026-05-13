# Balanced Hyperbolic Embeddings Are Natural Out-of-Distribution Detectors

- Decision: Reject
- Scores: 5, 6, 8, 3

## Abstract
Out-of-distribution recognition forms an important and well-studied problem in computer vision, with the goal to filter out samples that do not belong to the distribution on which a network has been trained. The conclusion of this paper is simple: a good hierarchical hyperbolic embedding is preferred for discriminating in- and out-of-distribution samples. We introduce Balanced Hyperbolic Learning. We outline a hyperbolic class embedding algorithm that jointly optimizes for hierarchical distortion and balancing between shallow and wide subhierarchies. We can then use the class embeddings as hyperbolic prototypes for classification on in-distribution data. We outline how existing out-of-distribution scoring functions can be generalized to operate with hyperbolic prototypes. Empirical evaluations across 13 datasets and 13 scoring functions show that our hyperbolic embeddings outperform existing out-of-distribution approaches when trained on the same data with the same backbones. We also show that our hyperbolic embeddings outperform other hyperbolic approaches and naturally enable hierarchical out-of-distribution generalization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
## Summary

The paper proposes Balanced Hyperbolic Learning for improved out-of-distribution detection by utilizing the hierarchical label information and learning more discriminative representations between ID and OOD samples. This is done in a two-step hierarchical hyperbolic embedding optimization process, where the first step involves a combination of distortion loss and norm based loss to learn the hyperbolic class prototypes from the label hierarchy. Then, the second step involves obtaining the hyperbolic representation for each image by optimizing a hyperbolic distance-based cross entropy loss. Experimental results are provided on two ID datasets for a suite of near and far OOD datasets, and involves comparison with well known OOD detection techniques from literature. 

---

### Strengths
## Strengths 

1. The paper is generally well organized. 

2. Connections between hyperbolic representation learning and out-of-distribution detection have been evidenced by prior work and new contributions at this intersection are interesting and valuable to the community. 

3. The authors provide a good coverage of related works in out-of-distribution detection, hyperbolic embeddings of images, and hyperbolic learning of hierarchies, to place their proposed method in the right context. 

4. The authors propose generalizations of existing OOD detection scores to hyperbolic variants which are simple and easy to adapt. 

5. Hyperbolic distance based loss function during optimization as in (11) is intuitive and naturally suitable for learning discriminative representations for distance-based OOD detection 

---

### Weaknesses
## Weaknesses 

1. Some of the claims made by the authors are not substantiated by prior work or experimental evidence, for instance L077 “existing hyperbolic embedding methods are biased towards deeper and wider sub-trees, with smaller sub-trees pushed towards the origin” - how do the authors define the bias and how is this verified experimentally? The authors should provide a quantitative measure of this bias, perhaps by analyzing the distribution of norms or distances within the learned hyperbolic space for different sub-trees. Furthermore, it is unclear if this bias is inherent to all hyperbolic embedding methods or specific to certain techniques, and this needs to be clarified.

2. Key details of the setup and specific experiments are missing, making it difficult to accurately evaluate the comparison with prior methods and impact of the work (see list of questions below for missing details)


3. The goal and setup of the OOD detection task is to improve OOD detection performance  while maintaining the ID accuracy, however the authors do not report the ID accuracy as compared to the baseline methods for either the CIFAR100 or the ImageNet100 datasets. The ID accuracy is reported for only a subset of methods for CIFAR100 in Table 3, and the reported ID accuracy for the proposed method seems to be lower than the accuracies reported by other methods, for instance CIFAR 100 ID acc is 73.4 whereas the CIDER paper reports ID acc of 75.35 on CIFAR100 with ResNet34 (page 19). This discrepancy raises concerns about the trade-off between ID and OOD performance, which needs to be addressed with a more comprehensive evaluation.


4. The design of the loss function in Eq. 7 can potentially lead to scale mismatch issues due to the difference in the source and nature of the hyperbolic distance $d_B$ and graph distance $d_G$. $d_B$ grows non-linearly as the points approach the boundary and can dwarf $d_G$ which remains typically bounded and grows linearly w.r.t the edge counts, especially in smaller graphs. This can cause mis-alignment where large $d_G$ does not map proportionately to large $d_B$, did the authors investigate the scales of these terms and the overall loss trends? The authors should provide an analysis of the scale of these terms during training, perhaps by plotting the average values of $d_B$ and $d_G$ over training iterations, to demonstrate that the loss function is well-behaved and does not suffer from scale imbalance issues.


5. Some pivotal connections to prior works are not fully acknowledged or discussed, for instance the primary hypothesis of this paper from Fig 1(b) and L082 - “OOD samples lie between ID clusters and the origin” is similar to an identical hypothesis proposed in CIDER (Figure 2, page 4 of the CIDER paper), albeit in hyperspherical embeddings, the key idea remains the same. The authors should explicitly acknowledge this connection and discuss the differences and advantages of their approach compared to CIDER, particularly regarding the use of hyperbolic space versus hyperspherical embeddings.

### Questions
## Questions

1. What is the loss function and experimental setup used for all the baseline (non-hyperbolic) experiments as reported in Tables 1 and 2? L250-253 mention using the “same features as in existing works for the most direct comparison to Euclidean-trained counterparts” which indicates that the methods and losses from original works are used, whereas L310-315 mentions “for the baseline and ours, we use the exact same backbone and training procedure” which is confusing since the loss function for the two settings (original and proposed balanced hyperbolic) are expected to be different. Additionally, did the authors experiment with the Supervised Contrastive Loss [1] for the baseline Euclidean setting? Empirically much better results are reported using the euclidean SupCon loss in SSD [2] and KNN (Sun et. al, 2022) as compared to the cross entropy loss. 


2. How is the distortion measured in Table 3?


3. How do the learnt representations and hierarchies differ when the proposed method is used without the norm-balancing loss? While this is observed via the OOD detection performance in 349-360, how does it affect the learning intuitively? 

4. Since the initialization of the hyperbolic prototypes is dependent on another technique, how do the authors see their method generalizing to other models of hyperbolic geometry? 


5. Have the authors visualized the learnt hierarchies from the hyperbolic embeddings to verify if the underlying hierarchical relationships are indeed accurately encoded in the hyperbolic space using the two-step optimization process? 

---

## Suggestions on improving presentation: 

1. The description in Section 3.2 (154-161) does not mention any details about the initializations of the prototypes, this description can be moved up from the next section to provide more context

2. “distortion” is mentioned in the introduction and Section 3.1 several times without any references or description, this should be included 

3. The Algorithm 1 on page 4 should include an “Output” marker and corresponding notations to denote the expected result from the optimization process 

4. Some minor typographical fixes - 157 “corresponding the the n graph..” -> “corresponding to the ..” , 183 “should have a the same..” -> “should have the same norm”, 417 “we have the use backbone for all methods” -> “we use the same backbone for ..”, etc. 

---


## References: 

[1] Supervised Contrastive Learning, Khosla et. al, NeurIPS ‘20 

[2] SSD: A Unified Framework for Self-Supervised Outlier Detection, Sehwag et. al, ICLR ‘21

---

## Post Rebuttal 

I thank the authors for the rebuttal. Having gone through their responses, their are several issues raised in my original review about the completeness and presentation of the results that are still not addressed during the rebuttal, specifically the discrepancy in the in-distribution accuracies and reported results for only a subset of the settings, and details about the choice of experimental setup and it's implications. Therefore, I would like to maintain my score.

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
This paper proposes hierarchical hyperbolic embedding for out-of-distribution detection. Specifically, it introduces a balanced hyperbolic embedding that maintains a similar distance between any two nodes. The learned hyperbolic embedding demonstrates superior performance compared to existing OOD approaches across various benchmarks and scoring functions, and its effectiveness is validated through numerous ablation studies.

### Strengths
The hierarchical hyperbolic embedding shows promise for OOD detection, which is an interesting idea. 

The effectiveness of the method is demonstrated through comparisons with various benchmarks and ablation studies. 

Overall, the paper is clear.

### Weaknesses
1) The motivation of “hierarchical” hyperbolic embedding for OOD detection is somewhat unclear. 
Could you please clarify the motivation behind using hierarchical relationships for hyperbolic embedding in OOD detection? Although it is well-known that hyperbolic embeddings can effectively represent distances in hierarchical graphs, it’s a little confusing about how this specifically benefits OOD detection.

2) It would be helpful to include some recent related works on hierarchical hyperbolic embedding [1, 2].

### Questions
Related to W1, could you please clarify the motivation behind using hierarchical relationships for hyperbolic embedding in OOD detection? Although it is well-known that hyperbolic embeddings can effectively represent distances in hierarchical graphs, it’s a little confusing about how this specifically benefits OOD detection.

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
4

### Summary
This work first identifies that hyperbolic embeddings are stronger at differentiating between in and out of distribution than euclidean methods due to the inherent distance / hierarchy property of the space. The authors identified that OOD points will lie closer to origin and as such have a more uniform distribution to classification prototypes placed at the boundary. Following this observation, the authors present a new distortion based loss function to match embedding targets to a known hierarchy, and balances hierarchy levels to ensure that correct hierarchical depths are preserved. This method is then applied to  to a variety of OOD scoring functions to demonstrate wide applicability. The results show that the proposed method outperforms Euclidean and hyperspherical approaches over a variety of benchmarks and OOD scores and visualisation mostly support their hypothesis. All implementations and empirical evaluations are described in full detail for replication.

### Strengths
**Structure and Clarity:**
- The problem statement is very clear, hypothesis is well reasoned, and the justification well described. 
- Preliminaries are concise yet highly informative, and add little bloat to the work while providing the reader with the necessary understanding for both OOD and hyperbolic learning. 
- Results are presented clearly, with descriptive figures, graphs and accompanying written discussions.

**Method hypothesis, findings, and rationale:**
- The method is very well motivated by observations and key findings of hyperbolic deep learning, where the properties of hyperbolic distances wrt distance from the origin are leveraged.
- Balancing all learnt embeddings to match the known tree like hierarchy is a nice addition, while it has its limitations as addressed below, should enforce correct hierarchical structure in representation space.
- The proposed method is simple in each of its components, allowing for simple and neat incorporation into a variety of existing settings, providing good impact and insight, valuable to the community.

**Reproducibility:**
- All details are presented for full reproduction in the text including optimisation, hyperparameterisation, datasets, and architectural settings, with the addition of algorithm of the method further adding clarification.

**Experimental results:**
- The performance improvements of the proposed method in comparison to Euclidean approaches are significant across almost all OOD scoring methods, providing clear justification for its future use. 
- A variety of experimental settings are evaluated, while more could always be added, that present are enough to provide confidence on the generalisation of the method.

**Ablations:**
- The presented ablations do a good job of analysing each proposed component and justify empirically its value in the proposed system in addition to being visually very interpretable. 
- The addition of comparisons to hyperspherical work appropriately evaluates this work in line with existing and preferred methods, which further provides confidence of the findings.

### Weaknesses
 **Learning a well defined hierarchy:**
- One assumption you make is that the hyperbolic method does indeed learn a strong hierarchy. However, this work does not demonstrate empirically or theoretically that the hierarchy is in fact learnt. The distortion loss should help enforce this structure, however, empirical analysis would be a great addition. Specifically, while the distortion loss aims to preserve relative distances within the hierarchy, it does not guarantee that the absolute depth or radial positioning of embeddings accurately reflects the hierarchical levels. The paper lacks a direct measure of how well the learned hyperbolic embeddings correspond to the intended hierarchical structure, such as a correlation between the radial distance from the origin and the depth of the node in the hierarchy. 
- Following from the prior, it is well known that in hyperbolic space embeddings can “collapse” to the boundary of the ball, and hence no hierarchy is learnt. Do you provide evidence that this does not happen or that the hierarchy is indeed present? While the norm loss should help address this, it would good to see how this holds as prior attempts to regularise hyperbolic embeddings via norm result in clipping like effects. While you show oil ablation comparisons to clipped embeddings, directly 

**Assumption of a known and correct hierarchy:**
- Less of a weakness and more of a limitation, the method assumes access to a well defined and known hierarchy. While in the demonstrated case this is know, in most settings this is not the case. Therefore the generalisation of this method is somewhat limited
- As mentioned above, while an understandable and reasonable limitation, this needs to be clarified and addressed explicitly as part of the limitations of the work.

**Distance of OOD:**
- Figure 3 measures the distance between embedding of each distribution, however to more appropriately support your hypothesis of OOD points being lower shallower nodes in the tree, a more appropriate analysis would be on the norm of the embeddings from the origin. The current distance metric does not directly reflect the radial positioning of the embeddings which is crucial for the hypothesis.
- As can be seen from figure 4, the points can achieve high distance but lie very deep in the tree given the increase in hyperbolic pairwise distance wrt to distance of the points from the origin. Therefore, for the most part your hypothesis holds, unknown points lie closer to the origin. However, this is not always the case.
- Furthermore, from the prior point, do you have any intuition how so much of the OOD points are taking up space close to the boundary? If you assume a relatively uniform distribution of embeddings of the hierarchy during training of ID points then figure 4 embeddings for OOD are lying in the hierarchy of an ID point.
 
**Minor:**
- Figures 1 a is informative and descriptive for the problem setting and help visually demonstrate the properties of hyperbolic space. However, 1 b is less informative and is not clear if this is an illustration or real embedding positions? If simply an illustration, it does not add a great deal to the narrative or work. I assume the latter, but would argue that figure 1 a is a clear selling point.
- Following the prior point, it would be good if the figures are slightly larger and the points made more distinguishable.

### Questions
1. How does the method perform if the OOD same is highly related to the semantic concepts captured in the learnt hierarchy. This method assumes that the OOD sample is semantically very different from the training dat
2. Does the method generalise well to other curvatures, given it has been shown that most visual embeddings are not fully hyperbolic, and thus different curvatures may be optimal for different datasets.
- Additional questions are asked for improve clarity to the authors in the weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces balanced hyperbolic learning for improved OOD detection by leveraging hyperbolic embeddings to represent class hierarchies. The authors propose a method to embed classes as hyperbolic prototypes that capture hierarchical relationships and seek to balance shallow and wider subtrees in the learned embedding with a distortion loss and norm minimizing term. This method can be easily integrated into existing OOD detection pipelines with minimal modification and works effectively in a wide range of datasets.

---

**Post Rebuttal** I want to first thank the authors for engaging in the discussion period. After the rebuttal discussion, I am more certain that the norm loss does not directly relate to the InD/OOD position. Thus why norm loss is helpful for OOD detection tasks is still not unclear. Even if I assume empirically *"without a norm loss, shallow subtrees also gravitate towards the origin, leading to unwanted biases."* mathematically norm loss does not directly control the distance of nodes to the origin (which is the major motivation in the introduction), putting one of the main contributions of this paper in doubt. Besides, in the current submission, the empirical evidence of *"without a norm loss, shallow subtrees also gravitate towards the origin, leading to unwanted biases."* seems missing. Also, the current paper does not provide a correct definition of what they mean by "levels". This will cause complete confusion for the methodology and many analyses provided in the paper, unfortunately. In summary, I do not think this submission is ready for publication. I will keep my original score and raise the confidence score to 5.

### Strengths
The writing of the methodology section is clear. The method is simple and flexible, which means it can be widely applicable to many OOD scores and settings.

### Weaknesses
 - Novelty is somewhat limited: “the hyperbolic classifier provides strongly uniform distributions for samples near the origin and strongly peaked distributions for samples near the boundary,” this motivation of this paper can date back to at least [1] Fig. 1. [1] uses distance to hyperbolic disk origin as an uncertainty metric in Sec.5.1, which can be also used for OOD detection, without leveraging any training labels. Please cite [1] accordingly in the introduction section and treat it as an important baseline for comparison. Also, the idea of leveraging hierarchical relationships for OOD detection is old, such as [2]. Therefore, Sec 1 and 2 are mostly from previous literature.
- Writing for the experimental section can be improved. In Section 5, because you have multiple paragraphs, it might be better to include a few sentences for summary about what experiments/settings you are going to cover at the beginning of Section 5. Some paragraph names probably need to be revised: for example, “comparison to hyperbolic embeddings” sounds similar to “comparison to other hyperbolic methods”, which is very confusing while reading. 
- Soundness of core methodology: the motivation of using the exact formulation of distortion loss and particularly norm loss is questionable. It requires either more explanation or more experimental support. Also, there are many details below that need to be clarified in the experimental section for OOD detection.
- Lacking comparison with some important baselines for the choice of distortion loss functions and hyperbolic neural networks. See Questions section for more details.
- The core motivation of the norm loss for OOD detection remains unclear. While the norm loss successfully enforces equidistant placement of nodes at the same depth from the origin, it's not evident how this directly benefits OOD detection. The paper's introduction and motivation, drawing from prior work, suggest that OOD data tends to cluster near the origin, while in-distribution data resides near the boundary. The norm loss, by potentially pulling in-distribution nodes closer to the origin (especially those with lower depth), could inadvertently cause overlap with the OOD data region, thereby hindering OOD detection. Without norm loss, nodes at the same depth might have a wider distribution, with some closer to the origin and others further away, potentially creating a more distinct separation from OOD data. The paper needs to provide a more convincing argument for why this norm loss is beneficial for OOD detection, addressing how it affects the placement of in-distribution nodes relative to the origin and how this relates to the expected behavior of OOD data in hyperbolic space. The current justification lacks a clear, intuitive connection to the OOD detection task, making it difficult to assess the true value of this component.

### Questions
- Line 70: “distance to the class prototype” how is prototype defined on Poincare disk? Also, how are Euclidean logits, based on dot products with Euclidean classifiers, and Poincare logits comparable? How to compare logits derived from different hyperbolic methods, especially Eq. 11 and those in Hyperbolic Neural Networks such as [1]? This is important because you rely on logit values heavily for many OOD detection scores as you described in Sec. 3.3. Why do you specifically use Eq. 11 as your classification loss? It would be interesting to explore the impact of loss function on hyperbolic OOD detection.
- Line 141-144: How does the quality of the hierarchy affect your method? How do you verify if LLM-generated hierarchies are reliable? Why can you directly transfer WordNet hierarchies to image datasets, because some semantic relationships are not reflected in images. For example, “large/small” in CIFAR100 hierarchy’s coarse label.
- Line 146: what does “equivalent edge distances” mean?
- Line 157-159: Distortion Loss’s motivation is the same as [2] by simply replacing Euclidean feature distance in [2] with Poincare distance, please include the comparison of Eq.7 and CPCC loss. Besides, why do you divide d_G in the loss instead of directly minimizing the l2 distance between two distance metrics?
- Norm loss: What’s the motivation for “nodes on the same level in the hierarchy should have the same norm, ensuring a uniform distribution across levels”? How does this affect OOD detection? I would recommend you to visualize the learned embeddings (like in [3]) of different types of trees with varying structures to illustrate this argument and put it in the main body, as this will add to the soundness of your methodology. Current A.1 is not straightforward enough, as I will discuss later below. Additionally, how can you apply norm loss for weighted hierarchies?
- Line 168/171: The format of i and e doesn’t match. Also i is defined twice, one in subscript of distance matrix, and one in the epoch number.
- Line 172: Why do you use Riemannian SGD if your encoder ResNet is fully Euclidean?
- Line 199: curvature c = -1. Curvature is not introduced in Section 2.2 where you hide all c terms in the operations. Although you set c = -1 by default, it’s better to show this term in equations. More importantly, curvature will affect the distance between points on the Poincare disk, which may have a significant impact on OOD detection. Please consider adding this in the experiment section for comparison.
- Line 228-229: “We also exclude … Euclidean”, Can you map your Poincare features to its tangent space with tangent map, so the features are on Euclidean space, and you can use Mahalanobis-distance based OOD score?
- Line 268: Can you include the details of “hierarchical out-of-distribution evaluations” as this is not common in OOD literature.
- Table 2: 89.1 => 89.10, 74.4 => 74.40 the number of digits should be consistent across tables. Compared to Table 1, why do you only use 5 OOD scores? Can you show the comparison of base and your method for each OOD dataset for Table 1 and Table 2? 
- Figure 2: Which in-distribution dataset do you use to plot this figure? What about the comparisons of AUPR and n-AUROC for the same setting?
- Line 362-365 “Several … options”: since you initialized with [3]’s representation (line 176-177), it’s not surprising that your method is better than [3] because [3] is not designed for OOD detection.  
- Line 369-371 “These values … standard classification”: Again [3] and HEC are not designed for classification. In my opinion, it is a method to visualize hierarchical data with lower distortion of input hierarchies. This is also the reason why comparing with [1] [4] [5] etc. is important and you can try to apply the Poincare Multinomial Logistic Regression layer on top of [1]. 
- Table 3: How do you compute the distortion metric and accuracy metric in Table 3? It seems PE has high AUPR and AUROC values, and can you explain this advantage (and disadvantage of your method)?
- Table 4: Why do you choose k = 300? In [6], k is 200 for CIFAR100, 50 for CIFAR10.
- Hierarchical Ablations: I’m a bit confused about this setting. Are hierarchical ood datasets really OOD data? Then in Table 6, you show that you can learn some hierarchical relationships on the OOD data, but is this going to hurt or improve OOD performance if you treat hierarchical held-out data as the OOD data? Why are FPR95/AUROC/AUPR metrics missing for this comparison?
- Table 6: What does “base” stand for in Table 6?
- Line 842-850: 
  - I strongly recommend authors to move the motivations of your loss design to the main section for better readability. 
  - Could you elaborate why ensuring equal distance to origin for nodes at the same level is beneficial for OOD? In hyperbolic embeddings, OOD samples are closer to the origin as you said, but how does training in distribution data with norm loss affect the location of OOD distribution? Shouldn’t we try to push all in-distribution samples away from the origin? 
  - Please include details about the “toy tree example” you used to plot Figure 6.
  - Text in Figure 6 is too small.

[1] Ganea, Octavian, Gary Bécigneul, and Thomas Hofmann. "Hyperbolic neural networks." Advances in neural information processing systems 31 (2018).

[2] Zeng, Siqi, Remi Tachet des Combes, and Han Zhao. "Learning structured representations by embedding class hierarchy." The eleventh international conference on learning representations. 2023.

[3] Nickel, Maximillian, and Douwe Kiela. "Poincaré embeddings for learning hierarchical representations." Advances in neural information processing systems 30 (2017).

[4] van Spengler, Max, Erwin Berkhout, and Pascal Mettes. "Poincare resnet." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

[5] Yue, Yun, et al. "Hyperbolic contrastive learning." arXiv preprint arXiv:2302.01409 (2023).

[6] Sun, Yiyou, et al. "Out-of-distribution detection with deep nearest neighbors." International Conference on Machine Learning. PMLR, 2022.

### Soundness
2

### Presentation
2

### Contribution
2
