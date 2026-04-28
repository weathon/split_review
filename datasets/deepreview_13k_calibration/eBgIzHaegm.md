# Keep Your Friends Close, and Your Enemies Farther: Distance-aware Voxel-wise Contrastive Learning for Semi-supervised Multi-organ Segmentation

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
Voxel-wise contrastive learning (VCL) is a prominent approach in semi-supervised medical image segmentation. Based on the initially generated pseudo-labels, VCL pulls voxels with the same pseudo-labels toward their prototypes while pushes those with different labels apart, thereby learns effective representations for the segmentation task. However, in multi-organ segmentation (MoS), the complex anatomical structures of certain organs often lead to many unreliable pseudo-labels. Directly applying VCL can introduce confirmation bias, resulting in poor segmentation performance. A common practice is to first transform these unreliable pseudo-labels into more reliable complementary ones, which represent classes that voxels are least likely to belong to, and then push voxels away from the prototypes of their complementary labels.  However, we find that in this approach, if voxels with unreliable pseudo-labels are originally close in feature space, they can end up far apart after being pushed away from their complementary prototypes. This disruption of the semantic relationships among voxels can be detrimental to the MoS task. In this paper, we propose DVCL, a novel distance-aware VCL method for semi-supervised MoS. DVCL is based on the observation that voxels close to each other in the feature space ('neighbors') likely belong to the same semantic category, while distant ones ('outsiders') likely belong to different categories. In DVCL, we first identify neighbors and outsiders for all voxels with unreliable pseudo-labels, and then pull their neighbors into the same clusters while pushing outsiders away. In this way, neighbors of unreliable voxels remain their neighbors and outsiders remain outsiders. This approach helps maintain useful semantic relationships among unreliable voxels while still enjoying the advantages of VCL. We conduct extensive experiments on four datasets to validate the effectiveness.  Extensive experiments on four datasets demonstrate the superior performance of DVCL compared to state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The proposed method introduces a voxel-wise contrastive learning approach for semi-supervised medical image segmentation. This approach aims to move voxels with the same pseudo-labels closer to their respective prototypes while separating those with different labels. While this idea has been explored in previous research, the novelty of the proposed method appears limited. Additionally, the authors have not sufficiently clarified how their approach stands out from existing methods. Despite these limitations, the proposed method demonstrated strong performance on multi-organ segmentation tasks.

### Strengths
1. Voxel-wise contrastive learning is an interesting concept, even though it has been explored in previous works. I agree with the effectiveness of separating negative labels while bringing positive labels closer together.

2. The proposed work is well written and easy to understand.'

3. The proposed works aims to solve the meaningful problem of semi-supervised medical image segmentation task.

### Weaknesses
1. The concept of voxel-wise contrastive learning has been widely used in previous research, and the reviewer finds limited novelty in this approach. Specifically, the paper does not adequately articulate how the proposed method differs from existing contrastive learning techniques applied to medical image segmentation, particularly in how it handles unreliable pseudo-labels. The core idea of bringing similar voxels closer and pushing dissimilar ones apart is not novel, and the paper lacks a detailed explanation of the specific modifications or innovations that distinguish it from prior work.
2. The evaluation of this work is limited to the FLARE 2022 dataset. While the authors mention multi-organ segmentation, the lack of experiments on other datasets, especially those with more complex segmentation tasks such as pathology or vessel structures, makes it difficult to assess the generalization capability of the proposed approach. The FLARE 2022 dataset, while useful, may not fully represent the challenges encountered in other medical imaging scenarios. Therefore, the conclusions drawn from this dataset may not be broadly applicable.
3. Visualizations of the feature space or clustering results would be beneficial to observe the distribution and patterns of different prototypes. Without such visualizations, it is difficult to assess whether the contrastive learning is effectively separating different classes and grouping similar voxels together. The paper lacks a clear demonstration of how the feature space is organized, which is crucial for understanding the effectiveness of the proposed method.

### Questions
1. Despite differences in the tasks to which it is applied, what are the technical difference between the proposed method and existing approaches?
2. Organ segmentation is relatively simpler compared to other medical segmentation tasks, such as those involving pathology or vessel structures. Has the proposed method been shown to be effective on these more complex tasks?
3. The definition of a prototype is unclear, and it would be helpful for the authors to include a figure to illustrate its meaning and visualize the results in the feature space.

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
This paper introduces a semi-supervised learning method called Distance-aware Voxel-wise Contrastive Learning (DVCL) to enhance multi-organ segmentation (MoS) in medical imaging. Traditional voxel-wise contrastive learning (VCL) aligns features based on initial pseudo-labels, which can cause confirmation bias and poor segmentation in complex anatomical contexts with large organ component variations. Distance awareness allows DVCL to cluster local voxels and push away distant ones, ensuring semantic consistency among uncertain pseudo-labels. An entropy-based selection module (ESM) classifies pseudo-labels as reliable or unreliable using a reweighting mechanism to maximize contrastive learning. In multi-organ segmentation tasks, DVCL outperforms state-of-the-art algorithms in four datasets.

### Strengths
1. The paper’s DVCL approach is innovative in the context of contrastive learning for segmentation, particularly in preserving neighborhood relationships within noisy pseudo-labels. 
2. The method demonstrates robust quantitative improvements across four datasets, showing consistent performance gains over previous state-of-the-art models. The ablation studies and comparisons in Table 1 also strengthen the claim that DVCL’s modifications lead to meaningful improvements.
3. The paper explains complex concepts such as "neighbors" vs. "outsiders" in the feature space well, making the rationale behind DVCL accessible. The illustrations, especially Fig. 1(b), effectively contrast DVCL with existing methods, helping readers understand the unique aspects of the approach.

### Weaknesses
1.The entropy-based selection mechanism is crucial for DVCL's performance, however its selection threshold values (τ) are not thoroughly investigated across many datasets. While this may appear to be a minor drawback, a more transparent discussion or empirical study of threshold selection and any dataset-specific adjustments will improve clarity and allow for greater replication of results.

2.The DVCL's dependence on neighbors and outsiders to manage semantic ties between voxels presupposes that these associations remain stable during training iterations. However, for complicated anatomical structures, boundary voxels may present a barrier since their classification as "neighbors" or "outsiders" varies. An examination of how DVCL handles such boundary scenarios, particularly in places where organs overlap, would provide more insight into the method's semantic maintenance resilience.

### Questions
1.How are entropy thresholds for reliable and unreliable pseudo-labels (τ) determined? Are they dynamically modified between datasets or fixed based on previous experiments?

2.How do changing K and K' values affect DVCL's segmentation accuracy for anatomically complex or tiny organs? Further clarification on this topic may provide useful insights for enhancing DVCL across a variety of organ segmentation tasks.

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
This work presents a voxel-level contrastive learning (VCL) method for multi-organ semantic segmentation from medical images using semi-supervised learning (learning from small number of labeled and large number of unlabeled examples). Voxel-level contrasting learning for semi-supervised segmentation is not new by itself, where voxels with similar labels are considered positive examples and their representations are pulled closer, whereas voxels with dissimilar labels are considered negative examples and their representations pulled away from each other; various methods have shown applications for medical segmentation as listed in the references. A problem with these methods is the issue of handling poor pseudo labels (initial labels generated on unlabeled examples using model trained on labeled examples), which can result in noisy labels and hence poor contrastive training and algorithm performance. A known method to address this problem in semi-supervised learning literature is to use complementary labels, where the idea is to rely on the lowest predicted probability class and enforce that the voxel does not belong to that class rather than use the highest probability class with low confidence for contrastive learning. The paper claims that when using this method (complementary label) of contrastive learning on unreliable (poor confidence) pseudo labeled voxels, it can incorrectly move the voxel features that are semantically similar (close by in feature space) away from each other, while moving dissimilar voxel features incorrectly closer to each other. Hence, the main claimed contribution of the paper is a method to retain similar voxel features (closest neighbors in feature space) closer and dissimilar voxel features (farthest neighbors in feature space) far from each other. The second claimed contribution of the paper is a dynamic way to ascertain which voxels are unreliable in the image during each iteration of training using entropy of the predicted label distribution. If the entropy is higher than a certain threshold based on the average entropy of the voxels of the image in that iteration, it is deemed unreliable, and vice-versa. For training, the paper uses the Cross Pseudo Supervision (CPS) framework where consistency of predictions on same input using two similar but differently initialized networks is enforced in addition to supervised loss using labeled images, contrastive loss using labeled and unlabeled but reliable voxels, as well as the proposed complementary label contrastive loss method for unreliable voxels that claims to maintain semantic neighborhood relationships between voxel features. The evaluation and ablation experiments are performed on 4 open source CT image data sets and a small improvement in performance over other VCL methods is demonstrated.

### Strengths
1.	The area and the general problem of handling noisy pseudo labels in semi-supervised learning has high practical importance and would be of interest to the community. 
2.	The dynamic entropy based method for ascertaining unreliable voxels proposed by the paper, while is not the primary contribution, seems original and a simple way to account for the varying confidence in the algorithm predictions over training iterations.
3.	The paper is written and presented well.
4.	The comparisons and ablations experiments are extensive.

### Weaknesses
1.  The paper does not clearly demonstrate the existence of the problem they are trying to solve, except for the cartoon illustration. It is not clear how often the claimed problem of semantically (dis)similar voxel features being (pulled)pushed (closer)away while using complementary label based VCL happens and by what degree, and how much does that affect the output. The paper needs to better illustrate the significance of the problem with real data. E.g., this could be demonstrated empirically in the following ways: a) Analyzing feature space visualizations before and after applying complementary label VCL; b) Quantifying how often semantically similar voxels end up far apart after complementary label VCL; c) Measuring the impact on segmentation performance when this issue occurs. Specifically, the paper should quantify how often the top k nearest neighbors of a voxel feature do not all have the same label for different k using ground truth labels.
2.  A primary concern is the reasoning/motivation of the paper’s main contribution, which is to retain the neighborhood relationships of voxel features in the feature space as determined prior to applying VCL. The paper claims that these relationships should be maintained through the VCL process. But it is not clear why this should be the case. This unreliably assumes that the feature representations of voxels and their neighborhoods prior to VCL are indeed correct, which may not be the case. In fact, the purpose of complementary label VCL methods is to address the potential incorrectness in the feature representations in the first place. It may as well be the case that the initial feature representations (prior to VCL) were incorrect, and that their neighborhood relationships should not be maintained during the VCL training process. The paper needs to present data on this assumption. E.g., how often does the initial neighborhood relationships of unreliable pseudo labeled voxels align with ground truth labels on labeled data?
3.  A second concern with the paper’s main contribution is that even if assuming that the voxel representations prior to VCL are reliable, it may be the case that voxels that are neighbors in the feature space may in fact happen to be from different organs with different labels. I.e., CT image voxels from different organs may have ended up being neighbors in the feature space. The current method of the paper will then incorrectly pull them together and assign the same label, whereas they should be assigned different labels. It is not clear how the method accounts for the above two scenarios. The paper should acknowledge and discuss this as a limitation. If this is not a problem, the paper should demonstrate that by quantifying the number of times the voxels may potentially have different ground truth labels but close by features for different values of k. A future iteration of the method can account for the potential similarity in features across different labeled regions.
4.  The paper doesn’t clearly describe or refer to prior work specifically on complementary label based VCL methods for semi-supervised segmentation. It needs to better describe what methods exist currently, their performance, merits and drawbacks, and present the claimed novelty of the paper in this prior context. a) Please include a paragraph in the related work section summarizing key complementary label VCL methods for segmentation; b) create a table compare features and performance of existing complementary label VCL methods for segmentation to the proposed approach.
5.  The presented method improves over existing method only by a small margin. While this is not the reason for the decision recommendation, it is necessary to evaluate statistical significance and confidence intervals of the results. The authors can use methods like Monte Carlo dropout to compute uncertainties over segmentation predictions.

### Questions
Questions, clarification and corrections that need to be addressed in the paper:

1.	In the introduction, the sentence “Experiments demonstrate that VCL based on complementary labels helps to learn good voxel representations.” is not substantiated. There are no references. This is where it is important for the paper to clarify what already exists with complementary label VCL methods and present their contribution in this context.

2.	In the introduction, the sentence “Despite the successes of this technique, we have identified a hidden drawback. This approach can disrupt the relationships among some unreliable voxels, and these relationships are helpful when learning features.” needs to be substantiated well with data. This is missing and is a major drawback currently.

3.	How are the cases where the nearest neighbors that still happen to be far distance wise in the feature space handled? Would the method still force them to belong to same category? Just relying on the neighbors irrespective of how far they are can lead the algorithm astray. Is there a distance threshold in the feature space that is used? If not, how would the differences in distances of neighbors across voxels be handled? Please explain the rationale and discuss potential limitations. Consider adding an ablation study examining the impact of different distance thresholds.

4.	This statement, “This approach helps maintain useful semantic relationships among unreliable voxels while still enjoying the advantages of contrastive learning.” needs to be substantiated well with reasoning and data. In fact, using a similar idea to impose this kind of constraint on physically closer voxels in the image (rather than in feature space) seems more intuitive. Neighbors typically belong to the same category, except at the boundaries. But the paper imposes the constraint in the feature space, and it is not clear why this should always be satisfied in unreliable pseudo labeled voxels. 

5.	“Then, after DVCL, voxel A is pulled to the same cluster of B, while voxel C is pushed
away from it.” => But in this process, C also happens to be pushed closer to 2, which is the incorrect category. How are these kinds of scenarios handled?

6.	In equation (4), perhaps the expression for W_A is incorrectly swapped between unreliable and reliable pseudo labels? I.e., M_r and M_u? Please check.

7.	In section 3.3. sentence “The negative candidates are selected from labeled voxels.” Why are reliable pseudo labeled voxels not used for negative candidates?

8.	Why are the distributions in equation (14) denoted as normal distributions?

9.	Regd. the method for distance aware contrastive learning, why are likelihoods of class relationships used instead of just minimizing (bringing closer) or maximizing (moving them farther) distances in the feature space? The motivation for the presented method is not clearly explained. Also, using class relationships doesn’t give leeway for the features to belong to nearby but different classes, which minimizing distances may.

10.	This sentence: “where ||pTm − pn||2 represents the l2-norm between the query feature and the features in the close” seems incorrect since pTm and pn are probabilities and cannot be L2 norm between features. Please clarify.

11.	The methodology using bounds is not clearly explained since the final equation (17) still seems to depend on Ur. A better description of the problem that is being solved here needs and how it is solved is needed.

12.	 In this sentence “In Table 4, we compare DVCL with existing nearest neighbor VCL methods (Wu et al., 2023; Dwibedi et al., 2021; Chongjian et al.) and find that DVCL exhibits superior performance. This improvement can be attributed to two main factors. First, for unreliable voxels, DVCL not only considers..”. Why are these references not included earlier in the introduction and related sections? These are important to place the contributions of the paper in prior research context. Please discuss them there as well.


Things to improve the paper that did not impact the score

1.	Reference Wang et al., 2022a seems incorrect since it does not even seem to talk about complementary label contrastive learning.

2.	In figure 2: Visual difference b/w nearest neighbors (solid lines) and farthest outsiders (dashed lines) doesn’t come out well. Please use color coding or other ways that make they easy to distinguish visually.

3.	In framework overview under methods, the paper needs to describe and motivate the CPS framework they use. Why was this framework chosen and not others? The paper doesn’t motivate the choice well.

4.	In Table 2, Ablation experiments on component aspect: (1) EBL; (2) DVCL, it appears including either EBL or dvcl already takes the result closer to when including both as compared to the baseline. A discussion on this would be good to add to the paper.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose an entropy-weighted cross pseudo supervision loss (a variant of the cross pseudo supervision loss), a high-quality voxel-wise contrastive learning loss (a variant of contrastive learning loss), and a distance-aware voxel-wise contrastive learning loss, focusing particularly on the latter for semi-supervised medical image segmentation. Experiments were conducted on four medical imaging datasets.

### Strengths
Performance evaluation and comparison were conducted on four datasets, with both quantitative and qualitative results presented.

### Weaknesses
1. The authors address semi-supervised segmentation, motivated by the high cost and expertise needed for manual annotation. While this is a valid concern for large-scale datasets, it is less compelling for smaller datasets, as used in this paper. In the experiments, the maximum number of labeled samples is only 90 (in AMOS), raising questions about the method’s applicability to real-world applications. Would the proposed approach demonstrate improved performance with hundreds or thousands of labeled images for training? Additionally, it remains unclear how much annotation effort is saved (i.e., the percentage of labeled data needed with this method to match the performance of fully supervised models).
2. The method design appears to contradict its intended objectives (details below).
3. Certain parts of the paper lack clarity.
4. Language issues are frequent.

### Questions
1. How would the proposed method perform with a larger number of labeled images for training? While this study is not alone in using a small dataset for model training and evaluation, such a setup may fall short of addressing the core challenges that motivate semi-supervised segmentation research. In fact, the substantial gap between fully supervised and semi-supervised learning is expected to narrow significantly when either the training or testing set is increased.
2. Why discriminative features for segmentation can be learned by maintaining useful semantic relationships among unreliable voxels? I think they contradict with each other, because discriminativeness means features from different classes are separated, but the proposed distance-aware voxel-based contrastive learning loss may pull close together voxels that are semantically similar but belong to different classes.
3. What are the thresholds used in Fig 1a? It is surprising to see that the ratios of reliable labels are all lower than 1%.
4. In Fig 1b, A and B are apparently closer to prototype 1, and C and D are closer to prototype 2. However, in the text, it is mentioned that A $\notin$ 1, B $\notin$ 1, C $\notin$ 2, and D $\notin$ 2 (Line 99). Shouldn't it be A $\notin$ 2, B $\notin$ 2, C $\notin$ 1, and D $\notin$ 1? Additionally, using an illustrative figure as evidence (Line 96) is unconvincing.
5. In Table 2, is EBL equivalent to entropy-weighted cross pseudo supervision loss? If so, why the proposed high-quality voxel-wise contrastive learning loss is missing?
6. The performance of different methods shows considerable variability. However, does the small number of test images provide sufficient statistical power?
7. In Equation 3, do you use a fixed $\alpha$ throughout training? Additionally, for some easy samples, e.g., image patches that is entirely from the background region, the model can make confident and correct predictions. Will the proposed strategy incorrectly treat a part of the voxels as unreliable voxels?
8. It is surprising to see the optimal value of $\tau$ is 1. With $\tau = 1$, will the high-quality contrastive loss reach 0 as the training goes?
9. In Equation 9, are $r_{c}$ L2-normalized? If so, why the feature center of all anchor voxels can be used for computing contrastive loss? If not, please also explain.
10. The K nearest voxels are selected as neighbors, and K furthest as outsiders, for calculating the distance-aware voxel-wise contrastive learning loss. Do these straightforward choices risk making model training too easy to achieve and thus this loss terms make no differences?
11. Language issues are common, e.g., in Line 338, "fearest" should be "furthest".

### Soundness
2

### Presentation
2

### Contribution
2
