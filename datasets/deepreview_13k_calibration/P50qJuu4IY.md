# Self-Supervised Learning with the Matching Gap

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 8, 1, 5, 5

## Abstract
Contrastive learning (CL) is a fundamental paradigm in self-supervised learning. CL methods rely on a loss that nudges the features of various views from one image to stay closer, while pulling away those drawn from different images. Such a loss favors invariance: feature representations of the same perturbed image should collapse to the same vector, while remaining far enough from those of any other
image. Although intuitive, CL leaves room for trivial solutions, and has a documented propensity to collapse representations for very different images. This is often mitigated by using a very large variety of augmentations. In this work, we address this tension by introducing a different loss, the matching gap. Given a set of $n$ images transformed in two different ways, the matching gap is the difference between the mean cost (e.g. a squared distance), in representation space, of the $n$ paired images, and the optimal matching cost obtained by running an optimal matching solver across these two families of $n$ images. The matching gap naturally mitigates the problem of data augmentation invariance, since it can be zero without requiring features from the same image to collapse. We implement the matching gap using the Sinkhorn algorithm and show that it can be easily differentiated using Danskin’s theorem. In practice, we show that we can learn competitive features, even without extensive data augmentations: Using only cropping and flipping, we achieve 74.2% top-1 accuracy with a ViT-B/16 on ImageNet-1k, to be compared to 72.9% for I-JEPA (Assran et al., 2023).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel contrastive loss based on optimal matching cost. The proposed matching gap loss may avoid feature collapse according to its property. The author conducts experiments mainly on ImageNet classification, and the experiment results show its superiority.

### Strengths
i) The idea of introducing matching costs is reasonable. The experiment results show it superior to some baseline results

ii) The writing is clear and easy to follow.

### Weaknesses
i) As I know, DINOv2 and SwAV also use the optimal transport algorithm to solve contrastive learning. But I can not find the discussion about such methods in related work. I would like to find the discussion about the difference between Matching Gap and SwAV/DINO

ii) As for experiments. In Table 1, the performance of the Matching Gap is not as good as DINO, which is a strong baseline proposed 1 year before.

iii) The author only conducts downstream experiments on transfer classification. Many self-supervised learning methods evaluate the downstream detection(COOC, VOC) and segmentation(COCO, aed20k) performance. I think the simple downstream classification task is not enough.

### Questions
Refer to the weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper suggest a novel approach to unsupervised representation learning. Following previous work (e.g. IOT), the main idea is to use an optimal transport plan between different view to guide the metric learning process. The main contribution is in the way this is done, which relies on trying to match the *cost* of the plan, rather than the plan itself to the ground truth pairing of augmented views. 
This seemingly simple change brings several advantages in training, with very competitive results, and is shown to have an interesting interpretation when compared to the commonly used InfoNCE loss.

### Strengths
1] The matching gap loss is an important finding that I expect to have impact on the field. It is well motivated as a way to allow the needed flexibility in the contrastive learning setup, where positive views should not necessarily be forced to the same point. 
2] Its ease of use and computational advantages are clearly shown - the ability to use the OT guidance without the need to differentiate through the Sinkhorn iterations, with computations involving only the pairwise n x n pairwise matrices.
3] The analysis that compares the new loss to the known InfoNCE is very enlightening and gives a very good understanding about what is happening in the optimization.
4] The paper is well written in all aspects, from the motivation, throughout the solution and experimental results.

### Weaknesses
Here are some, but rather minor:
1] Experimentation - I think that this new form of loss would be better justified if there would be empirical evidence that supports the intuitions (in addition to the standard benchmarking and ablations). It would perhaps be interesting to see how the embeddings of an augmented batch behave, in comparison to standard NCE, or some statistics of that kind. Specifically, visualizing the distribution of distances between positive pairs in the embedding space, and comparing it to the distribution obtained with InfoNCE, could provide valuable insight into the behavior of the proposed loss. This could reveal whether the matching gap loss indeed allows for more flexibility, as hypothesized, or if it leads to a different kind of clustering behavior.
2] The formulation is restricted to the 2-view setting. While this is simple, it would be interesting to know whether there are effective generalizations to multi-view settings. The current approach relies on a pairwise optimal transport plan, which might not be directly applicable when dealing with more than two views. Exploring alternative formulations that can handle multiple views simultaneously, perhaps by considering a joint optimal transport problem across all views, would be a valuable extension.
3] There is no specification or discussion regarding batch size, which has an important role in contrastive learning. Supposedly, the compact computation and 2-view setup could allow for larger batch sizes. It would be interesting to see how performance scales with batch-size. The effect of batch size on the stability and convergence of the training process should also be investigated. It is possible that the optimal value of the regularization parameter epsilon is dependent on the batch size, and this should be explored.
4] Several minor inaccuracies (which don't affect the analysis or correctness): (i) Bistochastic should be non-negative (ii) Should be <P,logP> in Equation 3 (without the -1) (iii) Last row of the loss equation is wrong, resulting in a matrix rather than a value: should probably be \eps<P,logP> instead of \eps\logP.

### Questions
* Please related to the above 'weaknesses'
* I understand (and am in favor of) the limited budget experimentation. Did you ablate on number of epochs, within the budget, to see if the dimnishing returns behavior is comparable to other methods?
* Due to the approach that does not require positives to converge to the same point - Perhaps there is actually room for more aggressive augmentation, that can exploit a richer extension of the training data?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new contrastive loss based on the matching gap. The proposed method is an extension of the paper "Understanding and generalizing contrastive learning from the inverse optimal transport perspective”. Also, the main idea of this paper is related to "whether the cost of the identity ground-truth pairing is significantly higher than the optimal matching cost that can be achieved, and use their difference as a loss".

### Strengths
This paper provides an explicit relationship between the gradients of the proposed matching gap loss with that of InfoNCE.

### Weaknesses
1. The novelty of this paper is rather limited. This article only uses a previously proposed technique to improve the computational complexity of inverse OT-based contrast loss in the optimization process. I do not find any new insights related to the field of contrastive learning.
2. This paper is really hard to follow. There are many mathematical symbols and proper nouns that lack explanation. For example, what is t in eq. 6 and 7, what is bistochastic matrices, and what are the difference between matching cost,  measuring agreement,  matching gap, and optimality gap?
3. The organization of Section Introduction is superfluous. I cannot find the relationship between the first two paragraphs and the last paragraph.
4. The experimental results cannot verify the effectiveness of the proposed method. First, the performance gain is pretty small. Second, there are many cases where the proposed method obtains a bad result.
5. The "A Link between InfoNCE and the Matching Gap" part and the "Our Contribution: Single Level Optimization with the Matching Gap" part are so vague that I have read them many times without understanding the logical relationship.

### Questions
1, How do you get eq. 8 from eq. 7?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed an alternative loss, Matching Gap (MG), to contrastive loss for self-supervised representation learning. Unlike contrastive loss enforcing the sample-wise invariance to data perturbations, the MG loss is a set-based loss, driven by minimizing the difference between the ground-truth transport loss and the optimal transport loss computed in the representation space using the Sinkhorn algorithm. The authors detailedly discussed the differences and connections of MG loss to contrastive loss and prior optimal transport, showing the unique properties of the proposed method. Finally, experiments on ImageNet-1k dataset suggested a comparable performance of MG to prior arts.

### Strengths
1. The paper is overall well-motivated. The reliance on data augmentation is one of the most prominent nuisances of contrastive learning. It is good to see more exploration toward bypassing this issue.

2. The theoretical analysis presented MG loss in a straightforward way and is overall easy to grasp. It also discussed the links between MG loss and contrastive loss/invert optimal transport loss, showing its unique properties as a set-based loss with single-level optimization.

3. MG loss exhibited superior performance to contrastive loss in weak augmentation and low training epochs regime.

### Weaknesses
1. The advantages of the single-level optimization in MG loss over the bi-level optimization in IOT loss are not provided clearly. Figure 2 shows that MG loss slightly underperforms but is competitive with IOT loss. I wonder if it improves the training speed/convergence or reduces the memory consumption?

2. Unfair comparisons. The implementation of the experiments largely followed the setting of Dino, which used two global crops and ten local crops by default. However, some of the baseline methods, e.g., MoCov3 and I-JEPA, used only two global crops, making it unfair to directly compare the performance with MG loss on the default setting.

3. Even under the potentially unfair comparison, the performance of MG loss is only comparable and sometimes even inferior to the contrastive loss.

4. Some notations are used without first introduced, e.g., $c(\cdot,\cdot)$ in Introduction and $t(\cdot,\cdot)$ in Sec. 3.

### Questions
See the weaknesses.

Overall, I think the proposed loss is interesting, and I like the presentation of this paper. However, the evaluation part still has significant room for improvement.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new self-supervised method that reduces the gap between the ground-truth matching and optimal matching. The proposed loss, matching gap, could potentially alleviate the problematic signal that force different views of the same image to collapse to the same point, even when they capture dramatically different contents, i.e. foreground vs background. To further ease the optimization, the paper proposes to learn the optimal matching via the Sinkhorn algorithm. Experimental results show that the proposed method performs on par with SOTA approaches with strong data augmentations and outperforms several latest self-supervised works with simpler data augmentations.

***
Post-rebuttal comment:

Following the discussion with the authors regarding their revision, the reviewer has maintained the original rating (marginally below the acceptance threshold), as the revision has not fully addressed the reviewer’s two primary concerns: i) the need for fair comparisons on the reported metrics (mainly about performance) ii) lack of sufficient justifications for the claimed benefits other than performance. The first concern was partially addressed in the rebuttal, which seems to indicate that MG is less effective than the baselines in terms of performance. The second concern was not addressed in the rebuttal due to time constraints,  making it difficult for the reviewer to understand the extra advantages of the work beyond the performance aspects. The reviewer suggests the author further explore and demonstrate MG’s benefits beyond mere performance. The authors have recognized these shortcomings, and are committed to further improving the work in accordance with the feedback from both Reviewer 1FzB and the present reviewer.

### Strengths
(S1) [Motivation] self-supervised learning learns feature representation via pretext tasks. As there are typically no human supervision involved. The “ground-truth” signals of such tasks are usually pretty “noisy”. The paper aims to alleviate the noisy supervision by reducing the gap between the ground-truth matching and optimal matching that could be computed on-the-fly. The reviewer believes this is an interesting topic.

(S2) [Method] the paper proposes to approximate the optimal matching via the Sinkhorn algorithm, which could further ease the online optimization.

(S3) [Ablation] Ablations on different components of the proposed method are included

### Weaknesses
(W1) [Evaluation] The evaluation section could have been more comprehensive. For example, when strong data augmentations are involved (Table 1), only several SSL baselines are included, e.g. MoCo-v3, DINO. The settings shown in Table 1 are also not consistent, e.g. different number of epochs, which makes it difficult to interpret the results, e.g. could the proposed method match DINO’s performance when trained for the same number of epochs? Also, it would be beneficial to include architectures beyond ViT-B(L)/16, e.g. ViT-S, CNN, etc. The lack of consistent training settings across baselines makes it hard to draw any firm conclusions about the effectiveness of the proposed method. Specifically, the different number of training epochs introduces a confounding variable, making it unclear if performance differences are due to the method itself or simply the training duration. Furthermore, the limited architectural diversity restricts the generalizability of the findings, as the method's performance on other architectures remains unknown.

(W2) [Performance] With strong augmentations, the proposed method shows no benefit compared to SOTA methods. The method outperforms several SSL approaches with weaker augmentations. However, at least from the application perspective, it is unclear to the reviewer what are the advantages of using only weak augmentations, especially when the training epochs are the same. The paper does not provide a clear use case or justification for focusing on weak augmentations, particularly when stronger augmentations are known to yield better performance in self-supervised learning. This raises questions about the practical relevance of the proposed method in scenarios where high performance is a priority. The lack of a clear advantage in performance with strong augmentations further diminishes the impact of the work.

(W3) [Claim] Some of the claims are not well-justified. For example, i) compared to CL that may “collapse representations for very different images”, the proposed method learns diverse representations for different views of the same image; ii) stronger data augmentations could help mitigate the representation collapsing problem. In order to justify the claims, the authors may measure/compare the mean distance of different views of the same image, or different samples of the same classes, across different models (i.e. the proposed method and baselines) and settings (i.e. strong/weak augmentations). The paper's claims about representation diversity and the mitigation of collapsing are not supported by empirical evidence. The absence of quantitative metrics to measure the diversity of learned representations makes it difficult to assess the validity of these claims. Without such evidence, the claimed advantages of the proposed method over contrastive learning remain speculative.

### Questions
N.A.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
