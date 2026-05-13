# Cycle Consistency Driven Object Discovery

- Decision: Accept
- Scores: 5, 6, 8, 8

## Abstract
Developing deep learning models that effectively learn object-centric representations, akin to human cognition, remains a challenging task. Existing approaches facilitate object discovery by representing objects as fixed-size vectors, called ``slots'' or ``object files''. While these approaches have shown promise in certain scenarios, they still exhibit certain limitations. First, they rely on architectural priors which can be unreliable and usually require meticulous engineering to identify the correct objects. Second, there has been a notable gap in investigating the practical utility of these representations in downstream tasks. To address the first limitation, we introduce a method that explicitly optimizes the constraint that each object in a scene should be associated with a distinct slot. We formalize this constraint by introducing  consistency objectives which are cyclic in nature. By integrating these consistency objectives into various existing slot-based object-centric methods, we showcase substantial improvements in object-discovery performance. These enhancements consistently hold true across both synthetic and real-world scenes, underscoring the effectiveness and adaptability of the proposed approach. To tackle the second limitation, we apply the learned object-centric representations from the proposed method to two downstream reinforcement learning tasks, demonstrating considerable performance enhancements compared to conventional slot-based and monolithic representation learning methods. Our results suggest that the proposed approach not only improves object discovery, but also provides richer features for downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a cyclic training loss to improve the slot-attention-based, object-centric representation learning in neural networks. Specifically, it aims to make the mapping from features to slots and from slots to features more distinct. Additionally, it emphasizes applying the learned representations to downstream tasks.

### Strengths
It is a reasonable idea to use additional regularization terms in the training objective to make each slot in slot attention represent a more distinct concept. The paper presents this idea clearly.
Experimental results show improved performance across various downstream tasks, including four Atari games, object discovery, and COCO/Scannet segmentation.
For segmentation tasks, it is interesting to see that additional cyclic losses are helpful with BO-Slate, as BO-Slate's optimization method should already aim to enhance disentangling between slots.

### Weaknesses
The experimental results show improvement, the overview accuracy level is low for real-world object discovery tasks. I doubt if adding more constraints on the disentanglement of representation is a promising direction.

The results on Atari games are a bit mixed. Also, why only evaluate it on four games?

### Questions
As there are already some works aiming to improve the slot attention-based method, the significance of this paper would be enhanced if it could show more compelling practical results, demonstrating that the overall direction is promising.
Why are the results limited to only 4 Atari games? Do the results generalize to more games?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tackles object discovery and introduces additional constraints to existing slot-based methods. Specifically, two cycle consistency objectives, slot-feature-slot consistency, and feature-slot-feature consistency are explored. The authors applies the learned object-centric representations to downstream reinforcement learning tasks and demonstrates the effectiveness of the proposed method.

### Strengths
1. The paper is well-written and easy to follow. 
2. The motivation and the development of the two consistency losses are clearly conveyed. 
3. Experiments are extensively conducted to evaluate the proposed method.

### Weaknesses
1. The authors point out one of the limitations of existing methods that a notable gap exists for the learned object-centric representations to be used in the downstream tasks. However, it does not make sense to claim the proposed method overcomes this by achieving better performance on downstream tasks. The logic here is somewhat doubtful. 

2. The main contribution of this paper is the two proposed consistency losses which constrain the model to learn discriminative slots. The technical novelty is limited.

### Questions
How to determine the number of slots? 

As shown in Fig. 2, in the bottom right, multiple semantics exist in slot 6. Why the model cannot depart them?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- This work identifies two shortcomings with existing object discovery methods. The first one being excessive reliance on specific architectural priors and meticulous engineering efforts. The second shortcoming is the gap in investigating the real world application of representations learned using the discovery methods.
- To mitigate the first shortcomings, authors propose an objective function based on cycle consistency that constraints features of a single or multiple instances of an object in a scene to belong to a single slot. 
- To mitigate the second limitation, authors demonstrate the effectiveness of learned representation in two downstream reinforcement learning tasks.
- Authors demonstrate that these enhancements hold true consistently across both synthetic and real world datasets showcasing the effectiveness of the proposed approach.

### Strengths
- The paper is well written and easy to follow.
- Authors validate all the claims made in the paper through appropriate experiments
- The proposed cycle consistency objectives are very simple and effective and I can foresee such objectives being useful for other q-former architectures like [1-2].
[1] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, Sergey Zagoruyko, End-to-End Object Detection with Transformers. 
[2] Junnan Li Dongxu Li Silvio Savarese Steven Hoi, BLIP-2:Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models.

### Weaknesses
 - I do not see any major drawbacks with the current work but I believe it misses a few more analysis to show the effectiveness of the cycle consistency objectiveness.
- For example, does the Slot-feature-slot consistency objective reduce the total number of required slots creating a bottleneck? Does it have an effect on the size of the feature dimension of the slots?
- Authors showed that increasing the value of $\lambda_{s f s}$ results in a trivial solution but are there any other modes of failure?

### Questions
- In Eq. 8 the softmax is applied using $\tilde F$ but only along the diagonal? Can the authors elaborate what happens if the full matrix is used for the loss? Isn't that a stricter case?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel regularization for object-centric learning methods which
cluster features into slots, for example Slot Attention. The proposed loss terms
regularize the cycle consistency between features and slots and vice versa:
Slot-feature-slot similarities are regularized towards an identity matrix and
feature-slot-feature similarties are regularized towards feature-feature similarities.
This regularization is shown to improve the segmentation performance compared to the
original Slot Attention model and other object-centric models. Moreover, the
regularization is shown to lead to more useful features for reinforcement learning.

### Strengths
- The proposed regularization is conceptually sound and leads to consistent improvements
  across the considered datasets and tasks.
- The proposed method is not only evaluated for unsupervised segmentation performance,
  but the learned, object-centric representation is also tested on a downstream task
  (reinforcement learning).

### Weaknesses
 - It is claimed that the proposed losses address that existing approaches "rely on architectural priors" for learning objects. In my view that's not true. Slot Attention can be related to soft k-means clustering; the proposed losses enforce more compact and better separated clusters. But what is considered as one cluster (i.e., an object) is still determined by architectural biases.
- In my view it is not sufficiently motivated why training unsupervised object-centric models on RGB images is the best approach for improving "object-based reasoning capabilities":
    - Segment Anything (Kirillov et al. 2023) suggests that generalizable object
      segmentation can be learned from limited supervised data.
    - Object-centric methods based on contrastive features such as DINO features are
      very capable, e.g. Dinosaur (Seitzer et al. 2022) or CutLER (Wang et al. 2023).
      It is argued that it "limits the applicability of the method to domains that the
      pretrained encoders are trained on". The works mentioned earlier however show that
      the resulting models work well on a range of datasets, including datasets that
      were not used to train DINO (e.g., MOVi).
    - Some works show that using additional data, such as optical flow or depth, allows
      training strong object centric methods (e.g., Karazija et al. 2022). The paper
      claims that "relying on [...] optical flow and motion is not feasible since many
      datasets and scenes do not come with this information". In my experience however,
      unlabelled video data is abundant for most practical settings.
  In summary, it is not clear to me why the restriction to unsupervised, image based
  methods trained from scratch is adequate for the goal of "developing object-based
  reasoning".
- Only FG-ARI is used as a metric for quantifying segmentation performance. It has been
  pointed out several times in the literature that this metric is problematic since it
  does not take into account whether object boundaries are accurate and favours
  undersegmentation (e.g., Engelcke et al 2020, Karazija et al. 2021, Monnier et al.
  2021). More established segmentation metrics, such as mIoU or AP, should be used that
  do not share these problems.

### Questions
- Slot Attention can be related to soft k-means clustering, as mentioned by Locatello
  et al. 2020. From this perspective the proposed regularization terms can be
  interpreted as enforcing compact, well separated clusters. In my view the paper would
  profit from discussing the proposed loss terms from this angle.
- The Dinosaur model, which is mentioned in the paper, shows improved scalability of
  object-centric learning to real world data by applying Slot Attention in the feature
  space of a large scale contrastive model (DINO). Do the proposed regularization terms
  also improve the Dinosaur model?
- I would find the result section more natural to read if object discovery came before
  the experiments on downstream tasks.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
