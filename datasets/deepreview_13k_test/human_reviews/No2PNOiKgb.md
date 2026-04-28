# Improved Convex Decomposition with Ensembling and Boolean Primitives

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Describing a scene in terms of primitives -- geometrically simple
  shapes that offer a parsimonious but accurate abstraction of
  structure -- is an established vision problem.  This  is a good model of
  a difficult fitting problem: different scenes require different
  numbers of primitives and primitives interact strongly, but any
  proposed solution can be evaluated at inference time.  
  The state of the art method involves a learned regression procedure
  to predict a start point consisting of a fixed number of primitives,
  followed by a descent method to refine the geometry and remove
  redundant primitives.  Methods are evaluated by accuracy in depth
  and normal prediction and in scene segmentation.  This paper
  shows that very significant improvements in accuracy can
  be obtained by (a) incorporating a small number of \emph{negative}
  primitives and (b) ensembling over a number of different regression
  procedures.   Ensembling is by refining each predicted start point,
  then choosing the best by fitting loss.  Extensive experiments on a
  standard dataset confirm that negative primitives
  are useful in a large fraction of images, and that our
  refine-then-choose strategy outperforms choose-then-refine,
  confirming that the fitting problem is very difficult.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an approach for decomposing indoor scenes into convex primitives from a single RGBD image. It introduces two key strategies for convex decomposition: the ensembling process and the use of boolean primitives. The ensembling strategy involves employing multiple networks, each predicting a different number or type of primitives, and selecting the optimal primitive set based on refinement loss. The boolean primitives strategy utilizes constructive solid geometry (CSG) operations, allowing up to two negative primitives for subtraction, which enhances geometric accuracy by trimming unnecessary parts of positive primitives. Additionally, the paper proposes skills to improve fitting accuracy, such as biasing sample loss, annealing loss weights, and data augmentation. Experiments on the NYUv2 dataset demonstrate that the proposed strategies enhance geometric representation accuracy and outperform previous state-of-the-art methods in depth estimation, normal prediction, and scene segmentation accuracy. While the method proposed in the paper enhances task performance, some design aspects remain somewhat puzzling and could be further improved.

### Strengths
1.This paper tackles a challenging and unresolved task of scene convex decomposition from a single RGBD image and significantly advances the performance on the NYUv2 dataset.
2.It is reasonable to introduce negative primitives as a subtraction operator in CSG, which adds flexibility to primitive-based scene representations. The authors show examples demonstrating that boolean primitives are parameter-efficient for fitting certain geometric shapes. Additionally, the ensembling strategy is straightforward and easy to follow.
3.The paper includes extensive ablation experiments to validate the contribution and performance improvement of each proposed module.

### Weaknesses
1.The main contributions of this paper are ensembling predictions from multiple networks and introducing negative primitives. However, these strategies do not appear to yield consistent performance gains. In Table 1, the naive method '24/32/40' outperforms both 'Pos - S→R' and 'Pos + Neg S→R', suggesting that ensembling and negative primitives are not accurate enough to help candidate selection before refinement. Although 'Pos - R→S' and 'Pos+Neg - R→S' achieve better performance, this is likely due to the availability of more final results for selection, indicating that the "refinement then selection"  is still necessary and impactful. In Table 2, it is also somewhat puzzling that, in some cases, introducing negative primitives reduces fitting accuracy.
2.The ensembling strategy is simple but underdeveloped. While it provides more candidate sets of convexes, it also increases computation time significantly. Besides, the number of primitives is preset, meaning the approach is only effective if sufficient networks are available to generate adequate candidates across diverse scenarios. A more effective approach might be to fuse all convexes from multiple networks and then learn to select the best results.
3.Boolean primitives convincingly provide a more accurate and efficient scene representation. However, it is confusing that the maximum number of negative primitives is limited to only 2, and in some cases, the negatives actually reduce performance, as shown in Table 2. Additionally, the paper notes that the primary performance gains from the negative operation occur when a negative primitive occupies empty floor space, whereas it seems more reasonable that negative primitives should have greater potential to remove excess space occupied by positive primitives.
4.In the experiments, the paper mainly compares its results to "Convex decomposition of indoor scenes," but lacks a comparison to "Robust Shape Fitting for 3D Scene Abstraction, IEEE Transactions on Pattern Analysis and Machine Intelligence, 2024."  Besides, while shape abstraction is a lighter-weight representation, it would be appreciated to include application examples of convex decomposition for completeness.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a shape abstraction method using convex primitives for indoor scene understanding. The core contribution lies in the observation that while negative (in the CSG sense) primitives alone provide limited benefits, their combination with model ensembling yields notable performance gains. The method is evaluated on the NYU v2 dataset, using reconstruction accuracy metrics for depth and normal, and segmentation accuracy, following the experimental setups of previous works. Notably, the proposed method significantly outperforms the most relevant SOTA method in depth accuracy.

### Strengths
- The paper is well-written and easy to follow.
- The ensemble of results to avoid local optima, though straightforward in general, is novel in learning-based shape abstraction. This ensembling and "pick-best" strategy is well-suited to the setup, where multiple inference results can be evaluated against the given depth map. Interestingly, using negative primitives alone shows limited performance gain, and the paper empirically demonstrates that a refine-then-choose strategy is more effective than the reverse.
- The proposed method outperforms previous works across all metrics, with a notable improvement in depth accuracy over the current SOTA.
- The bias loss term is well-motivated for negative primitives.

### Weaknesses
- According to the descriptions of Figures 10 and 11, the negative primitive is used only for the floor. This raises concerns about whether the negative primitive is functioning as intended, as indicated in Figure 2.
- While following the experimental setup of previous works, the proposed method is only evaluated on the NYU v2 dataset, which is relatively small compared to other commonly used benchmarks for indoor RGB-D data, like SUN-RGBD and ScanNet. Evaluation on these larger datasets would strengthen the paper significantly.
- Although well-motivated, the impact of the bias loss term does not seem significant or consistently effective in improving accuracy, as shown in Figure 8.
- An ablation study on learning rate annealing is missing.
- The paper lacks a theoretical explanation on why using negative primitives alone provides limited benefits and combining them with the ensemble method yields better performance.

### Questions
I wonder how each proposed component makes a qualitative difference.

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
4

### Summary
This paper studies two techniques to improve the problem of fitting a set of primitives to indoor scenes. Specifically, they first propose to use an ensemble of networks to predict a variety of solutions, and to choose the best one according to certain metrics. They further propose to predict negative primitives to complement with the positive primitives and perform boolean operations, which improves the performances as well. Experiments are conducted to show the effectiveness of the proposed components.

### Strengths
- The problem studied in this paper is interesting and important. Decompositing 3D indoor scene geometry into several primitives could facilitate the better understanding of the structure of 3D scene geometry.
- The proposed method in this paper appears to be sound and effective. Performing decomposition with multiple networks will indeed improve the reconstruction result for sure, and adding negative primitives indeed might reduce the representation complexity under certain scenarios.
- Extensive ablation studies are conducted in the paper to show the effectiveness of the proposed compoenents.

### Weaknesses
- The writing of this paper is hard to follow. Specifically the paper is based on a prior work, yet the prior work is not fully explained beforehand. Therefore the general method reads disconnected and fails to explain the method well enough.
- It is not clear on the relationship between the proposed method and works that perform CSG decomposition, such as [Du et al. 2018]. However, the negative boolean primitive discussed in this work is relevant to the traditional CSG decompostion of 3D geometry. Moreover, can the proposed method be applied to more general CSG grammar?
- The experiment setting of the evaluation section is not clearly illustrated. Specifically the major metric is the reconstruction metric, which might not convey enough message since the main goal of doing decomposition is to facilitate understanding. Moreover the experiment setting of the proposed method and prior works can be pretty different, since prior works do not predict negative primitives.
- Bringing negative primitives to the prediciton result, although improving reconstruction accuracy, yet can bring other issues. For example, the segmentation and understanding can become more tricky when there are negative primitives.

[Du et al. 2018] InverseCSG: automatic conversion of 3D models to CSG trees.

### Questions
- What exactly is the criteria for evaluating a decomposition result? In L195, the authors mention that they use depth map error to decide which decomposition is the best. However, this criteria might not be perfect, since the user might want a decomposition with fewer primitives and clearer structure, despite having larger reconstruction error.

### Soundness
2

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
3

### Summary
This paper proposes an improved approach to convex decomposition by integrating ensembling techniques and Boolean primitives. The method enhances the accuracy of depth, normal prediction, and segmentation, addressing issues in scene fitting and reducing reliance on a fixed number of primitives by allowing a flexible start point that is iteratively refined.

### Strengths
1. Innovative Use of Boolean Primitives: The introduction of negative primitives is a notable addition, enabling more efficient geometric abstraction by allowing finer control over free space representation.

2. Effective Ensembling Strategy: The refine-then-choose approach in ensembling leads to significant improvements in fitting accuracy by allowing multiple regression methods to predict different start points.

### Weaknesses
1. High Computational Demand: The ensemble-based approach requires significant training and inference resources, which may limit scalability and real-world applications.

### Questions
1. Can the model generalize to more varied datasets given its high resource demands?

### Soundness
3

### Presentation
3

### Contribution
3
