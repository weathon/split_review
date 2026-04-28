# A Clustering Baseline for Object-Centric Representations

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Object-centric learning aims to discover and represent visual entities as a small set of object embeddings and masks, which can be later used for downstream tasks. Recent methods for object-centric learning build upon vision foundation models trained with self supervision because of the rich semantic features they produce. However, they often involve additional training to optimize for object mask accuracy for a specific granularity of objects on a test dataset, while overlooking the evaluation of the quality of the object embeddings which is arguably more important.

In this work, we demonstrate how to discover objects and parts with a simple multi-scale application of k-means to the features of an off-the-shelf backbone. Our method is fast and flexible, produces interpretable masks, preserves the quality of the backbone embeddings, does not require additional training, and can capture different part/whole structures.

We evaluate the quality of the obtained representation on a variety of downstream tasks including scene classification and action recognition in videos, showing that it surpasses the performance of fine-tuned object-centric learning methods. Object masks produced by our method also effectively capture real-world objects and parts at various granularity, with comparable quality to specialized methods when evaluated on unsupervised segmentation benchmarks. These results suggest rethinking the current approach to object-centric learning, with a greater focus on the quality of the representation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a simple method that clusters feature from the representation from existing backbones, i.e., K-means clustering based on the extracted feature. The K is a fixed value. Some experiments are conducted to claim that this simple clustering method performs better than many other methods requiring additional training.

### Strengths
1. The presentation is good. The story is very clear to understand.
2. The method is simple, and simplicity means easy to be applied to downstream fields.

### Weaknesses
1. Claiming a kind of generally learned representation is better needs numerous diverse experiments to fully evaluate the method from different perspectives.  The experiments, which include only single-label classification and unsupervised segmentation, are insufficient. I think this work just selects a few experimental settings supporting the desired conclusion.
2. Clustering based on the representation produced by existing backbones is a commonly used baseline in fields like few-shot and unspervised learning. There is no new information in this paper.

### Questions
I recommend the authors delving deeper into the studied problem to reveal some insightful observations.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper reveals that directly applying the classic K-Means clustering algorithm to DINOv2 features can yield meaningful object-centric representations. To enhance flexibility, the authors propose a multi-round K-Means clustering pipeline that utilizes varying K values and hierarchical resolutions. Experiments demonstrate the characteristics of the object-centric embeddings captured through K-Means clustering and compare these results to those obtained from learning-based methods.

### Strengths
- The motivation is clear, and the method is straightforward to understand.
- Extensive experiments and thorough analysis are conducted to explore the characteristics of embeddings obtained by applying K-Means on DINO V2 features, along with comparisons to those captured by learning-based methods.

### Weaknesses
 - The main weakness of this work is the lack of novelty. DINOv2 features are already well-established for their ability to be clustered to represent objects, as evidenced not only by the original figures in DINO but also by numerous studies (both learning-based and non-parametric) in the field of unsupervised segmentation that have explored this capability. Consequently, it is expected that a simple K-Means clustering algorithm can be applied directly to DINOv2 features to yield meaningful object-centric representations.
- K-Means clustering also offers limited flexibility, as the choice of the number of clusters K and the design of the hierarchical structure to achieve optimal performance are hyperparameters that vary per dataset. Furthermore, whether the origin information contained in the resulting object embeddings is closely tied to the specific downstream tasks being addressed, making it difficult to assert that maintaining full semantic information is a definitive advantage.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a simple and effective clustering-based method for obtaining object-centric feature representations from state-of-the-art ViT models trained with self-supervision. While existing object-centric learning methods are designed with specialized architectures or training techniques, they are limited to specific granularity and small flexibility. The proposed method takes patch features from state-of-the-art ViT models and applies multiple steps of the K-means algorithm to obtain a small set of cluster centroids that represent objects at different levels of granularity. The proposed method shows efficacy at downstream tasks such as image and video classification, with much lower computational cost compared with the baselines.

### Strengths
In comparison with learning-based methods, the proposed method offers a set of advantages. 1) It doesn't require any training or fine-tuning to extract object features from the off-the-shelf models. 2) It also renders object features with different levels of granularity on multiple objects/parts with multiple running of the k-means algorithm. 3) The centroids of the extracted features hold semantics that can be applied to downstream tasks.

### Weaknesses
1) There is a lack of interpretability and expandability of the "object-centric" features extracted from ViT models. Current ViT models DINO and DINOv2 take image patches as input and are optimized with self-supervised losses. The self-attention layers extract the features at the image patch level, not the object level.  Simply applying K-means clustering on patch features does not guarantee that these features stand for the objects in the images. Wondering about the rationale behind why these features are defined as "object-centric features"?

2) The whole framework of the proposed method relies on the "well-trained features" from ViT models. With some epochs of clustering, these features are used for downstream tasks. Despite its simplicity, I wonder if further steps involving fine-tuning could be taken to update the ViT backbone. This is meaningful as it can help refine the self-supervised ViT features to bring out more semantic information.

3) What is the motivation for choosing video action recognition as one of the experiment setups? To evaluate the semantics quality of object-centric features, it may be a good idea to evaluate on more segmentation tasks on video or image datasets.

### Questions
1) Is it possible to evaluate more video/image-based segmentation tasks to show the quality of the semantics of the learned features?

2) What layer of self-attention to extract the patch tokens? Using keys, queries, or values?

3) Time and efficacy analysis: comparison with the baselines?

4) Ablation to the number of running clustering K?

### Soundness
2

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
This paper introduces an object-centric framework for extracting object representations without the need for training. The proposed approach involves applying simple k-means clustering to features from off-the-shelf backbones, specifically DINOv2 [1]. The centroids from clustering, computed with different numbers of clusters (k values), are stored to capture varying levels of granularity. The resulting set of centroids is then treated as the object-centric representation of the image. These representations are evaluated on downstream tasks such as classification and video action recognition to assess their quality, and on image segmentation to determine how well they visually align with objects.

---
[1] Maxime Oquab et al., DINOv2: Learning Robust Visual Features without Supervision, arXiv

### Strengths
* Learning object-centric representations in an unsupervised manner is both crucial and challenging, making the task addressed in this paper highly significant.
* Evaluating object-centric representations beyond object segmentation, on downstream tasks like video action recognition, is an important demonstration of their usability. The evaluation uses diverse and comprehensive datasets.
* The paper is well-written and easy to follow.

### Weaknesses
 * Applying clustering to pretrained encoder features is a well-known concept. Previous work in object-centric learning, such as DINOSAUR [1] and SOLV [2], has reported k-means clustering results in their ablations. Furthermore, clustering DINO [3] features has been used for segmenting objects in videos [4] and images [5, 6, 7]. This paper currently provides an evaluation of this well-established clustering approach on different benchmarks, but it is unclear how the framework represents a significant improvement or introduces novelty.

* In section 3.2, assuming overlapping masks across different granularities is an advantage over current object-centric methods, it’s worth noting that SAM [8] can extract overlapping masks for any object at any scale with pixel-level precision. This approach offers higher precision than patch clustering and can be used to extract object-centric representations in a zero-shot manner. What is the advantage of the proposed model compared to SAM in this regard?

* Since the CLS token is included in the $S_N$ representation set, it is expected to perform similarly in single-object classification tasks (e.g., ImageNet). For multi-object datasets like COCO, centroids should enhance performance by adding more granularity, whereas the CLS token summarizes the entire scene. Therefore, the comparison with the CLS token in Table 1 doesn’t provide much insight. Moreover, the approach uses multiple levels of granularity ($k = \{1, 2, 4, 8\}$), whereas SPOT [9] is limited to a single scale (7, 8, or 16), placing SPOT at a disadvantage. For a fair comparison, SPOT should include multi-scale representations, similar to the evaluations in Tables 2 and 3.

* For video action recognition (Figure 3), how does dropping some portion of tokens in the “all-patches” setting affect the tradeoff between token count and performance? Redundant tokens are common in video understanding tasks [10]. This comparison is important to highlight the efficiency of clustering centroids.

* The proposed approach leverages DINOv2 [11], which has been shown to significantly improve performance in object-centric tasks [2], while other models in Table 3 rely on the original DINO. Despite this advantage, both DINOSAUR and SPOT outperform the proposed method when using a single scale, i.e., a fixed number of slots/centroids, suggesting that the performance gain may primarily stem from the use of multi-scale representations. Given this, a multi-scale version of prior object-centric representations, such as a collection of DINOSAUR slots with $S = \{1, 2, 4, 8\}$, is expected to provide richer information than k-means clustering.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1
