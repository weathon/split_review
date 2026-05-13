# TopoFR: A Closer Look at Topology Alignment on Face Recognition

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
The field of face recognition (FR) has undergone significant advancements with the rise of deep learning. 
   Recently, the success of unsupervised learning and graph neural networks has demonstrated the effectiveness of  data structure information.
   Considering that the FR task can leverage large-scale training data, which intrinsically contains significant structure information, we aim to investigate how to encode such critical structure information into the latent space.
    As revealed from our observations, directly aligning the structure information between the input and latent spaces inevitably suffers from an overfitting problem, leading to a structure collapse phenomenon in the latent space.
    To address this problem, we propose TopoFR, a novel FR model that leverages a topological structure alignment strategy called PTSA and a hard sample mining strategy named SDE.
  Concretely, PTSA uses persistent homology to align
  the topological structures of the input and latent spaces, effectively preserving the structure information and improving the generalization performance of FR model.
  To mitigate the impact of hard samples on the latent space structure,
  SDE accurately identifies hard samples by automatically computing structure damage score (SDS) for each sample, and directs the model to prioritize optimizing these samples. Experimental results on popular face benchmarks demonstrate the superiority of our TopoFR over the
  state-of-the-art methods. %We hope that our findings can provide insights for future research on FR.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a TopoFR approach for face recognition task.
The proposed TopoFR consists of two main components:
(1) a topological structure alignment strategy, namely PTSA, which adopts persistent homology to align the structure of input and latent spaces.
(2) A hard sample mining strategy, namely Structure Damage Estimation (SDE), and a structure damage score (SDS) to detect and prioritize the learning process of these hard examples.
TopoFR is validated on several FR benchmarks and shows its advantages in comparison to previous works.

### Strengths
- The paper is well-motivated.
- The idea of structural alignment is interesting.
- Experimental results show improvements in comparison to other baselines.
- Ablation study shows the contributions of each component.

### Weaknesses
There are some concerns on the design and experimental results.

1. Novelty: While I acknowledge the motivation of TopoFR approach, the novelty of its components is limited. For example, Diverse Data Augmentation (DDA) consists of common augmentation operators such as GaussianBlur, Grayscale, ColorJitter and Random Erasing (Zhong et al., 2020). 
Moreover, Invariant Structure Alignments (ISA) is also adopted from previous work (i.e, Moor et al (2020).

Although it is ok for adopting previous works as building blocks, the novelty of the approach should be further emphasized. Otherwise, the paper becomes an incremental work.

2. Is the pairwise distance computed in Pixel Space (i.e. /matcal{X}) robust enough to estimate the topology? If this is sensitive, it should not be used to guide the learning process of the latent space.

3. In order to produce a good topology for learning process, how many samples should be used for each mini-batch? 

4. How is the computational cost of the Structure Damage Estimation process during training? 

5. What is the performance of the framework if only Focal Loss is used without SDS ?

6. The results on Figure 5 seems to be a bit tricky as TopoFR is trained with topological structure discrepancy metric. Adopting this metric for comparison will, of course, provide higher performance.

7. While large-scale model already gives high recognition results, the authors should adopt some more light-weight backbones. By this way, the contributions of the proposed components can be further emphasized.

### Questions
Please address the concerns in the Weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper in face recognition (FR) proposes a topology-based approach for exploiting the  structural information present in face images.  The paper proposes perturbation-guided  topological structure alignment  (PTSA) for aligning the structural information in the input face images and latent feature spaces. The paper combines PTSA with a  hard sample mining strategy called structure damage estimation (SDE). Authors report experimental results on state of the art face image datasets (LFW, CFP-FP, AGEDB-30, IJB-C) with training on MS1MV2 and Glint360K.  An appendix containing many additional results is provided and both code and data are made available.

### Strengths
The major strength of the paper is the novel approach introduced. The PTSA method based on persistent homology (PH) appears to be novel in face recognition (FR) research and seems to outperform state of the art FR methods on pretty large FR datasets.

The experimental results presented are impressive. They not only show superior verification performance over state of the art FR methods, but authors seem to have conducted a pretty thorough experimental study and report a variety of results in the main paper and in the appendix.

### Weaknesses
The main weakness of this paper is that it is difficult to follow. Authors use many acronyms and technical phrases in early sections whereas those concepts are not explained until later sections. For example, Fig. 1 has  "death" and "birth" along the axes and refers to  "j-th dimension homologies" which are not defined.  Also, how do these figures in Fig. 1 indicate that there are high-dimensional holes as the amount of data increases? My estimation is that most readers will find this paper a hard read.

The paper also suffers from minor English language deficiencies, but these can be corrected during the revision.

### Questions
1. The paper refers to point clouds. Can you state clearly whether the face images are those taken with a normal RGB camera or whether these are point clouds from a LIDAR or something else.

2. Fig. 1:  What are the "death" and "birth" and what are j-th dimension homologies? How do these figures indicate that there are high-dimensional holes as the amount of data increases?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the combination of a topological loss directly adopted from [Moor20] (Topological Autoencoders, ICML 2020) and a novel hard examples mining strategy to the problem of face recognition within the margin-based softmax loss approach.  The paper’s main claim is that the topology preservation of the data’s representation learned by a neural network would improve the model is supported with experiments on several benchmark datasets. 
In particular, the authors introduce three observations they claim to be novel, supporting them with empirical evidence only, with the illustrations of the results of computational experiments:

a) data’s topological complexity increases with its amount, illustrated by the persistence diagrams,

b) persistent homology-based distance between input data and its representation learned by a neural network increases with data’s amount, illustrated by the distance histograms evaluated for batches of sizes 256, 512 and 1024,

c) persistent homology-based distance between input data and its representation learned by a neural network decreases with the network’s depth, illustrated by the distance histograms evaluated for batch of size 128 for ResNets of three several depths.

An extensive ablation study shows the contribution of each component with the topology-based loss improves on 0.95-0.69 percentage points (with and without data’s augmentation), while adding other components brings only 0.27 percentage points improvement.

### Strengths
1. Interesting implementation of topological data analysis and persistence diagrams in face recognition
2. Strong experimental results that demonstrate benefits over existing methods

### Weaknesses
1.	The observation (a) is not novel, as it was theoretically investigated before [Kahle11,Bobrowski18], more on this later. The purpose of providing this observation is not completely understood. Is the author’s point that real world data, face images in particular, have complex topology, that need to be preserved? Then illustrating it with persistence diagrams just having more homology classes representatives as the amount of data’s increase is not enough. One would observe that with any random data of size n in dimension d, as it was shown that the expected k-th Betti number is $\mathbb{E}[\beta_k^{VR}(r)] = c_k n(nr^d)^{2k+1}$, with only the constant $c_k$ actually depends on data’s distribution [Kahle11]. In other words, the more data you have the more configurations of r-thickened points could form k-cycles. So what matters is the distribution of persistence diagrams as they would be different for random and real-world data. The authors need to clarify the specific topological properties they aim to preserve beyond simply observing an increase in the number of homology classes, and provide a more rigorous justification for why this particular observation is relevant to face recognition.
2.	The observation b) could be done by not properly normalizing the distance. BTW, it is better to use the same colors for batches of the same size for an improved comprehension, and to use the same size of the batch for illustrations of c) and one of the batch sizes of b). The lack of normalization makes it difficult to interpret the distance histograms. Without proper normalization, the observed increase in distance might simply be an artifact of scale rather than a genuine indication of topological change. Furthermore, the inconsistent use of batch sizes and colors across different figures hinders a clear comparison of the results.
3.	The claim that optimal transport-based distances have high time complexity to be used with real-world data is too loud, with the Wasserstein distance is only 1.5 times slower as shown in Table 6. The authors should acknowledge that while the classic implementation of Wasserstein distance has a cubic time complexity, there exist more efficient approximations with quadratic or even near-linear time complexities. The current presentation overstates the computational burden of optimal transport, and does not fully acknowledge the available efficient alternatives.
4.	The significance of the results (Table 1,2) is not analyzed. It would be better to report standard deviation instead of the mean accuracy only. The lack of statistical analysis makes it difficult to assess the robustness of the proposed method. Without standard deviations, it is impossible to determine if the observed improvements are statistically significant or simply due to random variations.
5.	Minor comments:
5.1.	It would be better to show the author’s attempt to train ArcFace by their own instead of using the pre-trained model in ablation study (Table 3). It is possible that they get higher accuracy, and the difference with the proposed technique will be lower.
5.2.	the software used to compute persistence diagrams is not stated in the main text,
5.3.	the homology dimension(s) H_* to be preserved by the topological loss are not stated in the main text;
5.4.	for the optimal transport-based distances only the time complexity O(n^3) is stated, yet the approximations in O(n^2) [Cuturi13], O(n log n) [Carriere17], O(n^~1.6) — empirically estimated [Kerber17], and near linear [Chen21] time exists, with at least first two are differentiable.

### Questions
1. What results of the proposed method in Table 1,2 are significantly better than the current state-of-the-art methods?
2. The authors mainly report results for R100 backbone, but Table 7 contains results for R50 only. hHat is the difference in training time with vanilla ArcFace for R100?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a topological structure alignment method for face recognition. Benefiting from the invariant topology structure in latent space, the authors propose diverse data augmentation (DDA) and invariant structure alignment (ISA) to optimize face embeddings. Experiments on various face recognition datasets achieve state-of-the-art performance and the code is provided

### Strengths
1. The authors propose a topological structure alignment method for face recognition.
2. The authors propose diverse data augmentation (DDA) and invariant structure alignment (ISA) to optimize face embeddings.
3. Experiments on various face recognition datasets achieve state-of-the-art performance.
4. Code is provided.

### Weaknesses
1. For diverse data augmentation and invariant structure alignment, the ISA loss only uses original face images and the corresponding augmented images for optimization. It is similar with discriminative self-supervised learning. However, for face recognition, the intra-class relations are also important.  Could the authors give some detailed comparisons and analyses to optimize the topological structure alignment with intra-class and inter-class distances?

2. Since face recognition has made great progress in recent years, the generalized performance is important. I recommend the authors to pay more attentions on the current SOTA on FRVT (https://pages.nist.gov/frvt/html/frvt11.html) and MFR-Ongoing (http://iccv21-mfr.com/#/leaderboard/academic). It is not difficult to obtain a comparable performance on FRVT and MFR-Ongoing by only using the WebFace260M dataset. For face recognition community, it is more meaningful to certificate that the proposed method can improve the perforamnce of generalized evalutions on age/pose/cross-domain face recognition.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
