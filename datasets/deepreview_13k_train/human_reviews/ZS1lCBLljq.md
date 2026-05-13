# Class-Relational Label Smoothing for Lifelong Visual Place Recognition

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Visual Place Recognition (VPR) is a task of estimating the location of a query image, predominantly executed through image retrieval using learned global descriptors from a reference database of geo-tagged images. While recent approaches have aimed to improve the scalability of VPR training by leveraging classification loss as a proxy task, this leads to a task gap between classification and retrieval - classification discretizes the feature space into distinct class regions, often overlooking visual differences between classes. This gap makes VPR systems particularly vulnerable to extreme visual changes such as lifelong variations. To remedy these problems, we propose a novel Class-Relational Label Smoothing (CRLS) that transforms one-hot labels into soft labels by considering visual information of inter-class relations. We further enhance this method by dynamically adjusting the influence of CRLS based on the stability of class weights, which is quantified by their magnitudes. Importantly, our findings suggest that the magnitude of class weights serves as an indicator of class stability, which is also supported by derivative analysis. We demonstrate that our method outperforms state-of-the-art methods on the most extensive 17 benchmarks, effectively bridging the task gap between classification and retrieval in visual place recognition. Codes and trained weights will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the problem of visual place recognition, where the goal is given a query image and a database of images at different locations to localize the query by matching it to the database.  Building on previous work, this task is formulated as a classification task where the individual places are classes, and the goal is to classify the query image into one of the possible classes (places). The first contribution of this work is to use a label smoothing regularization strategy that assigns non-zero probability during training to  visual places other than the ground truth places with larger probability assigned to places that are visually similar. The second contribution is to adjust the weight of the label smoothing regularization weight for each individual class during training. Results are shown on several place recognition benchmark and demonstrate improvements over prior methods.

### Strengths
- Novelty: using the inter-class relations to adjust the label smoothing is a nice idea, which makes sense for place recognition and seems novel in the place recognition context. 

- Results: the proposed approach demonstrates relatively small but consistent improvements over prior methods in many benchmarks.

### Weaknesses
 - 1. The clarify of the second contribution. (L268): The paper describes “min-max” normalization of the magnitudes over all classes”. However, it is not clear what is exactly meant here. Please describe exactly the step-by-step procedure that is used for this normalization. Please include a motivation for each step. Please link this procedure to the analysis shown in the equation 9 and in the supplementary material. This is important to justify/clarify the second contribution of the paper.  

- 2. L250: “We assign labels in a sequence that mirrors the visual similarity to the target class, thereby enhancing the model’s ability to generalize across visually similar scenarios, e.g., lifelong variation.” The idea of using the intra-class visual similarity for label smoothing makes sense and is well explained and justified. But it is not clear how it relates to lifelong variation. Why should it improve generalization across lifelong variations? Please clarify this point.

### Questions
- Please address the questions 1 and 2 above. 

- 3. [Optional] It could be interesting to do error bars for the presented results by bootstrapping, which is a standard approach in other application areas of machine learning such as bioinformatics, see e.g. : https://www.dummies.com/article/academics-the-arts/science/biology/the-bootstrap-method-for-standard-errors-and-confidence-intervals-164614/ 

 I understand that this is not standard in the place recognition research and for the place recognition benchmarks (hence it is marked as optional here), but it would be interesting to start reporting those when comparing the different methods or ablations going forward.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new model for visual place recognition (VPR) that incorporates a customized label-smoothing technique. By leveraging visual relationships between classes, the model is designed to learn a continuous representation space to manage various appearance changes, such as lifelong variations, that may often occur in VPR. In their label-smoothig approach the authors replace the traditional random class label smoothing with a similarity-based label smoothing. They note that label smoothing results in different class weights, where more challenging classes often require more training updates. To address this, they propose a method to identify these difficult classes and adjust their weights dynamically throughout training, ensuring training stability.

### Strengths
The paper tackles a specific aspect in VPR, that is lifelong changes that had not been explicitly addressed in prior research. The concept is effectively demonstrated, and the paper is well-written. The authors also analyze current benchmarks in this respect. The approach is novel and demonstrated over many experiments.

### Weaknesses
I have some concerns about the comparisons made in the paper and the rational behind the method.

1. The abstract's claim of "outperforming SoTA across 17 benchmarks" seems to be an overstatement. Current state-of-the-art (SoTA) methods typically rely on pretrained foundation models (e.g., SELA, SALAD, Crica, BoQ [1]). However, the paper includes only a limited number of experiments that compare against these leading techniques. While the paper does demonstrate the method's effectiveness across various architectures and benchmarks, it achieves SoTA results on only 5 benchmarks. To the best of my knowledge, on all the benchmarks used in the paper, SoTA is reached by foundation based models. I encourage the authors to extend their tests with foundation models to all the benchmarks used in the paper to better assess the effectiveness of label smoothing when applied to these SoTA techniques.

2.	Foundation models excel at capturing partial matches between images, potentially making label smoothing less impactful or redundant. When part of an image changes, current models, particularly those based on foundation models, are highly effective at identifying matches on the unchanged parts. This is why they also perform well in scenarios involving occlusion. It raises the question of what exactly CRLS captures in such cases—does it identify the changes and recognize what has been altered, or does it simply rely on the unchanged areas like other methods? It seems to me that the benefit of the suggested method is not really due to the moderate changes in the image, but rather due to smoothing of the classification space. I suggest the authors to provide attention maps that may shed light to this issue. I’d be glad to see examples of attention maps with foundation models against for instance SALAD, where the current model succeeds and SALAD fails.
3.	Another mechanism used to handle partial changes is re-ranking. It is unclear whether the results presented include re-rankers in the various methods compared. There are multiple approaches that incorporate re-ranking, such as SELA and R2Former. It is necessary IMO, to see results with re-ranking of those methods (and others) and also on benchmarks with occluded benchmarks. Table 4, is particualry important as it includes datasets with more significant changes, such as day vs. nights, weather changes etc. I’d suggest to compare the suggested method against foundation models on these datasets. I believe that most of the results can be found in the literature.
4.	Regarding the reported results, the model performs worse on MSLS - R@5 when using foundation models (as shown in Table 11 - Appdx). It shows better performance on SF, which it was trained on. In the single-view category, the results are significantly behind MixVPR, which is attributed to the use of longer features. However, since the authors add extra layers to foundation-based models, I’d suggest to train their model with additional layer to obtain the same feature size, for comparison. It is not clear if the observed differences are solely due to feature size.

$l$ is EQ. 1 is not defined. It will be fair to state in the comparison with AnyLoc that it is a zero-shot approach (without training on VPR data).

### Questions
1.	How will it work on Nordland, with seasonal changes?
2.	It is not clear what is the training dataset? Which data has been used? 
3.	For DINOv2 based foundation model, the authors apply two-layer MLPs for token embeddings, followed by a fully connected layer for the dimensionality reduction. Is there any ablation study showing that the performance boost is not due to these architectural changes?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a Class-Relational Label Smoothing technology for the Visual Place Recognition (VPR) method with classification loss for training. The proposed Label Smoothing transforms one-hot hard labels into soft labels based on inter-class visual similarities and can bridge the task gap between classification and retrieval in VPR. To improve training stability, the authors also propose a Class Stability Weighting strategy, which dynamically adjusts the label smoothing process according to the stability of class weights.

### Strengths
1.	This paper is well-written and clearly presented.
2.	The proposed method is novel (in the VPR area) and well-motivated. The authors also provide derivative analysis for further explanation.
3.	Experiments are conducted on diverse benchmark datasets.

### Weaknesses
1.	Although the experimental results seem ok, the advantages compared to SOTA methods are not obvious. For example, on the commonly used Pitts30k/Pitts250k and MSLS val, this method doesn't outperform EigenPlaces with an obvious margin.
2.	The work follows the training setting of the EigenPlaces framework. However, this work uses a larger batch size and learning rate than EigenPlaces. The authors claim those do not enhance the performance of the baseline model. So why not use the exact same settings as EigenPlaces? Whether the benefits of the proposed method will become marginal under such a setting.
3.	Although the proposed method with the DINOv2 backbone seems to outperform other DINOv2-based methods (SelaVPR, SALAD, CricaVPR), their training datasets are different. The SF-XL dataset used in this work is the biggest one, so this comparison may be not fair. The results of this method seem to be worse than those of EffoVPR, but the latter uses a stronger backbone DINOv2-large. My suggestion is that the proposed method should be compared with EigenPlaces based on the DINOv2-base backbone.
4.	Minor error: In some places (Line 939, 940, 1019), EigenPlaces was mistakenly written as EigenPlace.
5.	All analysis in this paper is based on the CosFace loss function used in EigenPlaces/CosPlace. However, many recent VPR works are using multi-similarity loss in MixVPR. The contribution that this work can make to the VPR community seems limited.

### Questions
The results of two-stage methods (TransVPR, StructVPR, R^2Former, SelaVPR) seem much lower than the original papers. Did the authors only perform the first stage? This is unfair because the global features of these methods are more low-dimensional than others.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes to use class-specific soft target labels for classification, applied to visual place recognition and in particular lifelong scenarios, where scene appearance evolves over time while labels remain the same. In the proposed Class-Relational Label Smoothing (CRLS), each ground truth one-hot target label is replaced by a soft one, obtained by pairwise class similarities, as expressed by class weight vectors while the classifier is being learned. In Class Stability Weighting (CSW), a convex combination of the proposed loss and a baseline loss (e.g. label smoothing) is used. The weight of the baseline loss is the norm of the ground truth class weight vector. The main competitor, both in motivation and in comparisons, is label smoothing, where the distribution over background classes is uniform.

### Strengths
The paper is well written and easy to follow. The idea is sound and simple. There are only two hyper-parameters and a related ablation study. The method is competitive in most experiments and outperforms competing methods in lifelong visual place recognition.

### Weaknesses
The related work, background and competitors in experiments are insufficient. The positioning of providing an improvement over a naive baseline and then competing methods that are not relevant as ideas is problematic. Details follow.

1. CRLS is presented as an improvement over label smoothing, applied to visual place recognition and compared with state of the art (SOTA) methods in the field. The main idea is that the appearance of the input examples is not consistent with the labels, hence the labels are modified. This happens in the particular problem because of evolution over time in the lifelong scenario and the competing SOTA methods are presumably not using any such label modification, although this is not clarified.

    This kind of positioning is problematic, because it treats visual place recognition as a benchmark, with the objective to beat the competition in the benchmark using ideas from anywhere. The proper positioning would be to beat relevant ideas. It would be to provide an improvement over other methods where examples are not consistent with labels, hence discuss such methods in related work and background, then compare with them as competitors in experiments, with visual place recognition being merely the application. Comparison is SOTA in the field of visual place recognition would be a secondary target.

    In this sense, there are several tasks where examples are not consistent with labels, for example learning with weak supervision where labels are noisy, semi-supervised learning where labels are missing, or active learning where examples are selected for labeling. Taking learning with noisy labels as an example, here are some prior works with relevant ideas:

    > [*1] Reed et al. 2014, Training Deep Neural Networks on Noisy Labels with Bootstrapping
    >
    > [*2] Sukhbaatar et al. 2014, Training Convolutional Networks with Noisy Labels
    >
    > [*3] Lee et al. 2017, CleanNet: Transfer Learning for Scalable Image Classifier Training with Label Noise
    >
    > [*4] Li et al. 2017, Learning From Noisy Labels with Distillation
    >
    > [*5] Sharma et al. 2020, NoiseRank: Unsupervised Label Noise Reduction with Dependence Models
    >
    > [*6] Han et al. 2019, Deep Self-Learning From Noisy Labels
    >
    > [*7] Iscen et al. 2022, Learning with Neighbor Consistency for Noisy Labels

    By studying such methods, one realizes that label smoothing is only a very naive baseline. There are many more advanced ideas and some are similar to the proposed method. A quite universal idea is distillation where soft target labels are obtained by a model, possibly the same while being learned. This is used in [*1], [*4] and [*6]. Of those, [*4] also uses a "knowledge graph". This graph plays the same role as the similarity-based affinity in this work, it is just constructed based on class semantics. Beyond pairwise class similarities, [*3] and [*5] use similarities between examples and class prototypes, hence can provide more fine-grained operations per example, while [*7] uses pairwise similarities between examples directly, hence provide even more localized operations per example. The idea of multiple class prototypes would also work well against evolution over time in the lifelong scenario, and there are several such methods in deep metric learning.

    The authors should present such methods as background, also methods from other relevant tasks, then compare with them as competitors. Here, they do not even compare with label smoothing (LS). This could have happened in table 6 for example, which is ablation, but LS is not presented in the absence of CRLS and CSW. There is comparison with other label smoothing strategies (LR and ACLS) in Table 7, but this is treated as ablation study. Instead, more advanced competitors should be chosen and this should be the main comparison. In this comparison, the authors should build on top of the best performing method on visual place recognition and show that adding CRLS works better than adding any other competitor. By doing so, the resulting solution would still beat the SOTA on visual place recognition.

2. For CSW, there are again many strategies by which to assign weights to different loss components based on some sort of confidence, and these weights can be per class like this work or per example, which is more fine-grained. Such ideas can be found in the tasks of semi-supervised learning or active learning. The authors should again study the literature and come up with strong competitors, present them mas background and compare with them.

### Questions
How much of the proposed line of work could the authors do? Could they present some additional concrete results and a plan for updating the paper? It is realistic to re-position the paper as suggested for ICLR?

### Soundness
3

### Presentation
3

### Contribution
2
