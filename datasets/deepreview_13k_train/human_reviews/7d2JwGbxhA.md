# OCEBO: Object-Centric Pretraining by Target Encoder Bootstrapping

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Object-centric representation learning has recently been successfully applied to real-world datasets. This success can be attributed to pretrained non-object-centric foundation models, whose features serve as reconstruction targets for slot attention. However, targets must remain frozen throughout the training, which sets an upper bound on the performance object-centric models can attain. Attempts to update the target encoder by bootstrapping result in large performance drops, which can be attributed to its lack of object-centric inductive biases, causing the object-centric model's encoder to drift away from representations useful as reconstruction targets.
To address these limitations, we propose \textbf{O}bject-\textbf{Ce}ntric Pretraining by Target Encoder \textbf{Bo}otstrapping, a self-distillation setup for training object-centric models from scratch, on real-world data, for the first time ever. In OCEBO, the target encoder is updated as an exponential moving average of the object-centric model, thus explicitly being enriched with object-centric inductive biases introduced by slot attention while removing the upper bound on performance present in other models. We mitigate the slot collapse caused by random initialization of the target encoder by introducing a novel cross-view patch filtering approach that limits the supervision to sufficiently informative patches. When pretrained on 241k images from COCO, OCEBO achieves unsupervised object discovery performance comparable to that of object-centric models with frozen non-object-centric target encoders pretrained on hundreds of millions of images.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In the research background, large-scale foundation models are common due to self-supervised learning techniques in deep learning, especially in computer vision. Cognitive psychology research indicates human visual perception is object-centric, leading to object-centric representation learning, though such models lack successful pre-training on large-scale real-world datasets. The research purpose is to propose the OCEBO method for pre-training object-centric models from scratch on real data to overcome limitations and unleash potential. The research methods involve a model architecture with an image encoder, slot attention encoder, slot decoder, and a target encoder of the same architecture, and a training objective formulated as a self-distillation bootstrapping problem with defined object-centric self-distillation loss including cross-view patch filtering and an optional mask sharpening stage. The experimental results on the MS COCO dataset and evaluation on multiple datasets with different metrics show that OCEBO can avoid slot collapse and achieve comparable performance to existing models with pre-trained target encoders while demonstrating good data scalability.

### Strengths
1. A new object-centric pre-training method, OCEBO, is proposed. It is the first self-distillation setup for training object-centric models from scratch on real-world data.

2. Experiments prove that OCEBO can avoid slot collapse and achieve performance comparable to existing methods using a large number of pre-trained images on multiple datasets while demonstrating good data scalability.

3. The importance of object-centric inductive biases is emphasized, and its positive impact on the target encoder is verified through experiments, providing new insights into the theory of object-centric learning.

### Weaknesses
1. Although good results have been achieved on the MS COCO dataset, the requirements for pre-training datasets are relatively high. Datasets containing simple scenes like ImageNet are not suitable for pre-training object-centric models, and a large-scale dataset suitable for pre-training object-centric models has not yet been found. The paper does not provide a clear path for how to curate or create such a dataset, which limits the practical applicability of the method.

2. When comparing with existing state-of-the-art object-centric models, due to different pre-training methods and datasets used, the models are not directly comparable, which, to some extent, affects the accurate evaluation of model performance. The lack of a standardized evaluation protocol makes it difficult to ascertain the true advancement offered by the proposed method.

3. The experimental setup and evaluation system are still somewhat rudimentary and cannot fully demonstrate the scheme's advantages. The evaluation primarily focuses on object-centric tasks, and it is unclear how the learned representations perform on other downstream tasks, such as dense prediction tasks or tasks requiring fine-grained understanding. This narrow evaluation scope limits the understanding of the generalizability of the learned representations.

### Questions
1. When updating the target encoder as an exponential moving average (EMA) of the object-centric model encoder, how can we ensure that the introduced object-centric inductive biases do not overly affect the model's learning of other features, thus maintaining good generalization ability in different downstream tasks?  
2. When the cross-view patch filtering method determines which patches to use for training, although it considers the feature quality of the target encoder, is it possible that this method may overlook some patch information that is potentially helpful for the model's learning? How can the accuracy and comprehensiveness of patch selection be better balanced? 
3. The paper mentions that constructing a large-scale dataset suitable for pre-training object-centric models remains an open question. Do the authors have any preliminary ideas or directions on how to construct such a dataset?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose an approach to train object-centric models from scratch using real-world data, rather than relying on pre-trained non-object-centric foundation models.
The method is based on cross-view teacher-student self-distillation, in a similar fashion to DINO, IBOT and DINOv2.
The model architecture incorporates a slot-attention bottleneck and the patch-level loss uses a filtering strategy to stabilize training.
The method is trained on COCO and evaluated on different datasets on the task of unsupervised object discovery, where it attains performance comparable to (but lower than) previous methods that leverage large-scale pre-trained models.

### Strengths
The main strength of the paper is succeeding in training an object-centric model from scratch on COCO, which is known from previous works to be challenging.
The architecture or training procedure per-se are not particularly novel, mostly resembling the global and patch losses of DINO, IBOT and DINOv2, with the addition of a slot-attention bottleneck in the architecture.

What is novel is the idea of filtering noisy patches that could be detrimental to the object-centric objective, especially during the first stages of training.
This idea, albeit not well ablated, seems to be a strong contribution of the paper.

The paper is easy to follow, with a good balance between technical details, analogies, and high-level explanations.
Quantitative results are presented clearly and accompanied by qualitative examples.

### Weaknesses
 **Ablation on patch filtering:**
From section 4.2, it appears that patch filtering is crucial to stabilize training.
The chosen strategy uses an heuristic to filter out patches, especially during the first stages of training, as show in figure 2.
The first question that comes to mind is: how sensitive is the method to the choice of the heuristic?
It could be that the chosen heuristic has no importance and what really matters is that initially the global loss drives the training and the object loss is introduced gradually later.
In my opinion, this is an important ablation study to perform in the paper.
Two alternatives that I would like to see tested are:
- Keeping all the patches but gradually increasing $ \lambda_{oc} $ from 0 to 1 during training.
- Randomly dropping patches in $ \mathcal{L}_{oc} $ as opposed to selecting them via nearest neighbors. The drop ratio could be gradually increased from 0 to 1 during training to mimic the proposed heuristic.

**Measuring slot collapse:**
An important point of discussion is "slot collapse", defined in the footnote at L107.
Since the authors claim that the proposed patch filtering strategy is crucial to avoid slot collapse, it would be helpful to have a quantitative and objective metric to measure slot collapse.
This could be, for example, the correlation between slots and spatial positions across images, to measure whether a slot encodes the "bottom right corner" or a category of objects.
The green/red results in table 1 would be more informative and convincing if accompanied by such a metric.

**One model or several ones?**
The whole model is trained from scratch on COCO and evaluated on different datasets, each with a specific number of slots (L319).
Does it mean that a new model needs to be trained from scratch for each number of slots?
If so, this is highly impractical for real-world applications where a practitioner would like to sweep over the number of slots to find the best one.
In such a case, frameworks like DINOSAUR or SPOT are much less expensive to use.
If not, how is the number of slots changed in the model? Is it fixed before training or can it be changed at inference?

**No evaluation of the learned representation:**
All evaluations focus on segmentation-based metrics (FG-ARI and mBO) on several datasets.
The task of "object-centric learning", however, implies that the model should learn a representation of objects, not just segment them.
It would be useful to include a section that evaluates the slot representation on downstream tasks in a quantitative manner. 

**Projection head design:**
On L328-331 it says "The projection heads are identical to those of DINO (Caron et al., 2021), with the exception of setting L = 8192 instead of the original 65536. Compared to the DINO head, ours projects every patch rather than just the global representations and we find that the gain in performance does not justify the computational cost."
However, both IBOT and DINOv2 use per-patch heads and find that a large number of heads, even up to 131072, is beneficial.
If time allows, I recommend running an ablation study on the design of the projection heads, possibly splitting the object and global heads.

**Performance and usefulness:**
Weaker performance when compared to other methods that leverage large-scale pre-trained models (table 2).
This is somewhat expected, since the model is trained from scratch on a smaller dataset.
At a high level, this paper demonstrates that training from scratch is possible, but fails to prove that is actually beneficial.
If a pre-trained model achieves better performance, why should one train from scratch?

### Questions
**Equation 1:**
I suggest renaming $\mathcal{L}_{oc}$ to something else to avoid confusion with the actual loss used during training which is defined in equation 3.

**Ablation of head design:**
Equations 3 and 4, as well as the filtered version in 8, describe a cross-view teacher-student distillation loss.
This setup requires quite a few moving parts, especially the cropping strategy with overlapping parts and the inverse augmentation.
Would it be possible to train the model without cross-view distillation, but only using the teacher's output on the same crop as the target?

**Comparison with the DINO objective?**
The global loss in equations 5 and 6 is formulated exactly as in DINO, why does the paragraph above it cite other papers and not DINO?

**Suggestion about notation:**
Paragraph 3.3 and line 269 "where $nns_{n_n}(z_{t,1}, z_{t,2})_i$ denotes indices of nn nearest neighbors".

There are too many "n" characters in the chosen notation and it's hard to read.
I suggest trying to replace $n_n$ with $k$ if possible.

**Where is SPOT in the introduction?**
To the best of my knowledge, SPOT is the first work that unfreezes the encoder during training, and it was published months before FT-DINOSAUR.
However, in the introduction, FT-DINOSAUR is presented as the first and is discusses in depth, while SPOT is not mentioned. This is misleading and should be corrected.

**Missing results:**
L435 "In fact, an attempt to train OCEBO on ImageNet results in a drastically lower performance." where are these results?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposed an object-centric pretraining method that updates the target encoder by EMA. The experiment results show that the proposed method can successfully learn object-centric representation. When pretrained on 241k images from COCO, the proposed achieves unsupervised object discovery performance comparable to other models with frozen non-object-centric target encoders pretrained on hundreds of millions of images.

### Strengths
1. This paper is well written and easy to follow.
2. The proposed method can achieve unsupervised object discovery performance comparable to other models with frozen non-object-centric target encoders pretrained on hundreds of millions of images.
3. The proposed method demonstrates scalability well beyond a few thousand training images.

### Weaknesses
1. How exactly object-centric inductive biases are captured by the target encoder, it may be better to explain the mechanism more intuitively or theoretically. Specifically, the paper lacks a detailed explanation of how the EMA update of the target encoder, using gradients from the object-centric model, leads to the emergence of object-centric representations. It is not clear what specific properties of the gradients are being transferred and how these properties enforce object-centricity in the target encoder.
2. As the author mentioned, although the proposed method has achieved comparable results in COCO pre-training, its advantage still needs to be verified on a larger scale of pre-training data. The current results, while promising, are limited by the scale of pretraining. The paper does not provide any analysis or discussion on the potential challenges or bottlenecks that might arise when scaling up the pre-training process to datasets with millions or billions of images. This is a crucial point, as the effectiveness of self-supervised learning methods often hinges on the scale of pre-training.

### Questions
1. What distance is used when calculating nearest neighbors?
2. I don't understand what is the meaning of ``invaug(q1)''.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of effectively updating the target encoder in object-centric pre-training. Previous works use frozen pre-trained encoders as the target encoder, resulting in a performance upper limit. While updating the pre-trained encoders causes a significant performance drop, the paper proposes to bootstrap the target encoder from scratch. To prevent slot collapse, a cross-view patch filtering technique is proposed. Experiments show that OCEBO can be trained from scratch and learn from more data.

### Strengths
1. The paper is easy to follow and understand. 
2. The motivations for cross-view patch filtering and mask sharpening stage are straight-forward and these two techniques are proven to be effective.

### Weaknesses
1. The experimental evidence for scalability is too weak. A scaling plot, which shows how the model performs as training data increases, is more supportive. From only two data points, it's hard to tell the scaling trend. For example, what if the model is just in rapid growth on 100k images and has already plateaued on 200k images? The authors are suggested to provide a scaling plot instead of two data points. Furthermore, the provided scaling analysis lacks granularity; the jump from 100k to 200k is too large to accurately assess the scaling behavior. A more detailed analysis with smaller increments (e.g., 25k, 50k, 75k, 100k, etc.) would be beneficial to understand the model's performance curve and identify potential saturation points.
2. There still seem to be large gaps between the final results and previous methods, which can not support the claim that OCEBO is comparable to those with pre-trained encoders. The performance differences are not thoroughly analyzed, and it's unclear if these gaps are due to the proposed method or other factors such as training strategies or hyperparameter choices. A more detailed ablation study is needed to isolate the impact of OCEBO's core components.
3. Discussion on object-centric data and non-object-centric data should be added. While a frozen target encoder can be an upper limit, a feasible way is to use stronger target encoders, as shown in the comparison between DINOv2 and DINO. Stronger DINO can be trained using more data, where object-centric data and non-object-centric data can both be used. So what's the benefit of scaling object-centric data over scaling pre-trained data for target encoders? The paper does not adequately address the potential benefits of using non-object-centric data for pre-training the target encoder, especially given the success of methods like DINOv2. A discussion on the trade-offs between object-centric and non-object-centric pre-training is needed to justify the chosen approach.

### Questions
1. The authors are suggested to provide more evidence on scalability. Moreover, it would be better to provide an estimation of data amount required to achieve comparable performance with SOTA models.
2. More benchmarks should be compared. This paper only reported MOVi-C, MOVi-E, Pascal VOC, EntitySeg results, while only two of them are real-world datasets. The authors are suggested to add more real-world datasets, especially the COCO dataset.

### Soundness
2

### Presentation
3

### Contribution
2
