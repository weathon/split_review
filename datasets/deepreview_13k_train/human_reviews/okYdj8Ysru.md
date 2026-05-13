# A Lie Group Approach to Riemannian Batch Normalization

- Decision: Accept
- Scores: 8, 1, 8, 3, 6

## Abstract
Manifold-valued measurements exist in numerous applications within computer vision and machine learning. 
Recent studies have extended Deep Neural Networks (DNNs) to manifolds, and concomitantly, normalization techniques have also been adapted to several manifolds, referred to as Riemannian normalization. Nonetheless, most of the existing Riemannian normalization methods have been derived in an \emph{ad hoc} manner and only apply to specific manifolds. This paper establishes a unified framework for Riemannian Batch Normalization (RBN) techniques on Lie groups. Our framework offers the theoretical guarantee of controlling both the Riemannian mean and variance. Empirically, we focus on Symmetric Positive Definite (SPD) manifolds, which possess three distinct types of Lie group structures. Using the deformation concept, we generalize the existing Lie groups on SPD manifolds into three families of parameterized Lie groups. Specific normalization layers induced by these Lie groups are then proposed for SPD neural networks. We demonstrate the effectiveness of our approach through three sets of experiments: radar recognition, human action recognition, and electroencephalography (EEG) classification.git}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors describe a new kind of Batch Normalization layer for
Riemaniann neural networks. The proposed technique is a theoretical
improvement over existing batch-norm layers by being a generalized and
unified view on all previously proposed technique, using the Lie-group
structure of the manifold.

### Strengths
- A very pleasant to read recap on all batch norm-like layers for
  Riemannian networks.
- Theoretical guaranties on the control provided by the layer.
- Convincing experimental evaluation (not SOTA obviously, but an
  improvement over other manifold methods)
- LieBN reduces to the classical BN for Euclidean manifold.

### Weaknesses
 - Nearly all tables are barely readables.
- Novelty of the work should emphasized more. LieBN provides more
  guaranties and a more sound approach. But in the writing, it is not
  completely clear of what is a full novelty over previous methods and
  what is a generalization.
- A broad zoo of choices (AIM, LEM, LCM and alpha beta variants), but no
  clue on choosing. It's an usual question with this type of methods,
  and it always a little bit disapointing to simply benchmark over all
  the possible choices.

### Questions
- What is the interest of the (alpha, beta) generalization ? In
  particular in context of neural networks ? And what are the value used
  in the experiments ?
- In the article about RBN, Brooks et al discuss about the amount of
  data need to achieve good performance. Any insight about this for your
  layer ?
- Is there a link between Frechet variance and the variance of the
  Gaussian used for normalization ?

- I guess it should be "neutral element" instead of identity in Eq 13 ?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a batch normalization layer for neural networks on Lie groups. The authors then focus on SPD neural networks to showcase their approach. The proposed method is validated on radar recognition, action recognition, and electroencephalography (EEG) classification.

### Strengths
* Proofs are given in the supplementary material (I did not thoroughly check them)
* Experiment results show improvements over some state-of-the-art SPD neural networks

### Weaknesses
 * The paper lacks of novelty
* Experimental results are not convincing
* No discussion about the limitations of the proposed approach

The proposed technique is a simple tweak of those from Kobler et al. (2022b), Lou et al. (2020), Chakraborty (2020).
No new concepts or ideas have been developped w.r.t. these works. While the authors state that the proposed technique works for Lie groups and is able to control mean and variance in contrast to these works, extensions of these works to Lie groups, as done in the paper, are trivial.

The experimental results are not convincing since the proposed method is only compared with some SPD neural networks. For example, on human action recognition, the proposed method is outperformed by the method of Laraba et al. (2017) on HDM05 dataset by a large margin (72.27% vs. 83.33%). This shows that the proposed technique is probably not effective compared to other learning techniques designed in Euclidean space.

### Questions
The proposed technique is a simple tweak of those from Kobler et al. (2022b), Lou et al. (2020), Chakraborty (2020). 
No new concepts or ideas have been developped w.r.t. these works. While the authors state that the proposed technique works for Lie groups and is able to control mean and variance in contrast to these works, extensions of these works to Lie groups, as done in the paper, are trivial.

The experimental results are not convincing since the proposed method is only compared with some SPD neural networks. For example, on human action recognition, the proposed method is outperformed by the method of Laraba et al. (2017) on HDM05 dataset by a large margin (72.27\% vs. 83.33\%). This shows that the proposed technique is probably not effective compared to other learning techniques designed in Euclidean space. 

*Question*

How does the proposed method perform on another Lie groups, e.g. when being used in LieNet (Huang et al., 2017) ?

*References*

1. Sohaib Laraba, Mohammed Brahimi, Joëlle Tilmanne, Thierry Dutoit: 3D skeleton-based action recognition by representing motion capture sequences as 2D-RGB images. Comput. Animat. Virtual Worlds 28(3-4) (2017)

2. Zhiwu Huang, Chengde Wan, Thomas Probst, Luc Van Gool: Deep Learning on Lie Groups for Skeleton-Based Action Recognition. CVPR 2017: 1243-1252.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Study of Deep Neural Networks (DNNs) on manifolds, associated with normalization techniques, with a unified framework for Riemannian Batch Normalization (RBN) techniques on Lie groups. Theoretical guarantee are provided to caracterize the stability of the process. 
Approach is illustrated for Symmetric Positive Definite (SPD) manifolds, with three families of parameterized Lie groups, in a SPD neural networks.  Experiments have been done for radar recognition, human action recognition, and electroencephalography (EEG) classification.

### Strengths
Interesting algorithm LieBN, which enables batch normalization over Lie groups, to normalize both the sample and population statistics.and apply to SPD manifolds.

### Weaknesses
Density of probability on SPD matrix could be only defined as invariant to all the automorphisms of SPD manifold. To assess which density verify this property, you have to consider "Lie Groups Thermodynamics" developped by Jean-Marie Souriau. Consider upper-half space of Siegel (pure imaginary axis is the space of SPD matrix) where the Lie group SU(n,n) acts transitivelly. With Souriau method, you are able to compute the Gibbs density of maximum entropy that is covariant to SU(n,n). If you restrict to the imaginary axis, you find the density for SPD matrices. See the following reference and put it in your references:
[A] Barbaresco, F. (2021). Gaussian Distributions on the Space of Symmetric Positive Definite Matrices from Souriau’s Gibbs State for Siegel Domains by Coadjoint Orbit and Moment Map. In: Nielsen, F., Barbaresco, F. (eds) Geometric Science of Information. GSI 2021. Lecture Notes in Computer Science(), vol 12829. Springer, Cham. https://doi.org/10.1007/978-3-030-80209-7_28

### Questions
Add the following references on batch normalization
[B] Daniel Brooks. Deep Learning and Information Geometry for Time-Series Classification. Machine Learning [cs.LG]. Sorbonne Université, 2020. English. ⟨NNT : 2020SORUS276⟩. ⟨tel-03984879⟩; https://theses.hal.science/tel-03984879
[C] D. Brooks, O. Schwander, F. Barbaresco, J. . -Y. Schneider and M. Cord, "Deep Learning and Information Geometry for Drone Micro-Doppler Radar Classification," 2020 IEEE Radar Conference (RadarConf20), Florence, Italy, 2020, pp. 1-6, doi: 10.1109/RadarConf2043947.2020.9266689.
[D] D. Brooks, O. Schwander, F. Barbaresco, J. -Y. Schneider and M. Cord, "A Hermitian Positive Definite neural network for micro-Doppler complex covariance processing," 2019 International Radar Conference (RADAR), Toulon, France, 2019, pp. 1-6, doi: 10.1109/RADAR41533.2019.171277.
[E] D. A. Brooks, O. Schwander, F. Barbaresco, J. -Y. Schneider and M. Cord, "Complex-valued neural networks for fully-temporal micro-Doppler classification," 2019 20th International Radar Symposium (IRS), Ulm, Germany, 2019, pp. 1-10, doi: 10.23919/IRS.2019.8768161.
[F] D. A. Brooks, O. Schwander, F. Barbaresco, J. -Y. Schneider and M. Cord, "Exploring Complex Time-series Representations for Riemannian Machine Learning of Radar Data," ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Brighton, UK, 2019, pp. 3672-3676, doi: 10.1109/ICASSP.2019.8683056.
[G] Brooks, D., Schwander, O., Barbaresco, F., Schneider, JY., Cord, M. (2019). Second-Order Networks in PyTorch. In: Nielsen, F., Barbaresco, F. (eds) Geometric Science of Information. GSI 2019. Lecture Notes in Computer Science(), vol 11712. Springer, Cham. https://doi.org/10.1007/978-3-030-26980-7_78

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper concerns batch normalization for Lie group valued data. The authors propose a unified framework for batch normalization that they claim offers theoretical guarantees.

### Strengths
I have a hard time finding strengths that were not already presented in previous papers. I hope the authors can argue to the opposite, but as of now I am not sure of what is the actual contribution of the paper.

### Weaknesses
 - I am unsure what is the contribution of the paper. As the authors state, the normalization scheme they propose has been used in previous work. There are some claims like "In contrast, our work provides a more extensive examination, encompassing both population and sample properties of our LieBN in a general manner. Besides, all the discussion about our LieBN can be readily transferred to right-invariant metrics. " but I was not able to find out what specifically these differences are. The approach seems to be almost exactly the same when I look up in the cited papers where it is applied to Lie groups as well.
- using the Riemannian or Lie group exp and log maps for batch normalization was a good idea the first time it was presented, but I don't see the value added with the current paper

### Questions
I believe the authors need to argue convincingly what is the contribution of the paper, and why the paper presents a significant contribution relative to the previously methods.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a batch-normalization (BN) method for manifold-valued features in neural networks. While in prior works several BN techniques are proposed for specific types of manifold, the authors present a general manifold-based BN formulation from a viewpoint of Lie-group. Besides, especially for SPD manifolds, practical BN methods are derived from the general formulation based on three types of pull-back metrics [Chen+23].
The experimental results using SPDnet and TSMnet demonstrate that the propose methods exhibit competitive performance to SOTAs.

### Strengths
+ A general formulation of manifold-based BN is presented through reviewing/summarizing several Riemannian-normalization (RN) approaches.
+ Practical BNs for SPD matrices are derived in an efficient form from the general formulation.

### Weaknesses
Novelty of LieBN in Sec.4 is limited as it is rather straightforward from the prior works [Kobler+22a] and [Chakraborty+20].

On the other hand, the pull-back metrics [Chen+23ab] are effectively applied to the general formulation to instantiate practical BN methods for SPD manifolds in an interesting way.
Though especially pull-back Euclidean metrics seem to be efficient as shown in Table 3, this paper lacks in-depth analysis about the methods from qualitative and/or computational viewpoint. It is demanded to clarify computational details such as by showing back-props through comparison to the other RN approaches based on complicated manifold-based computation, which would significantly improve reproducibility.

Considering \theta-parameterization does not work so well as shown in Sec.6, such a parametric extension might be redundant, rather complicating the discussion in Sec.4. In stead of that extension, it may be better to focus on analyzing the practical BN methods shown in Table 3.

As to empirical performance results reported in the experiments, superiority of the method is less clear since the performance improvement is not significant due to large stds of performance scores.
To clarify the efficacy of the proposed method, it should be compared with the other RN methods in terms of computation cost not only the classification performance.

Based on the experimental results, one cannot identify the best SPD-BN method that outperforms the others consistently. Although the authors insist such an inconsistency shows generality of the approach, it is less understandable and unfavorable from a practical viewpoint. In this case, provide some discussion and/or analysis about connection between types of metrics and tasks (or network architectures) for rendering insights into the SPD metrics.

Minor comments:
In Eq.5: $\frac{1}{N} \sum$ -> $\sum$

### Questions
The above-mentioned concerns should be addressed especially in the following points.
- Analysis about the SPD-BN methods in Table 3 from computational viewpoint in comparison to the other RNs.
- Empirical comparison regarding computation cost.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
