# Robust Deep Equivariant Structure from Motion

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 5

## Abstract
Multiview Structure from Motion is a fundamental and challenging computer vision problem. A recent deep-based approach utilized matrix equivariant architectures for simultaneous recovery of camera pose and 3D scene structure from large image collections. That work, however, made the unrealistic assumption that the point tracks given as input are almost clean of outliers. Here, we propose an architecture suited to dealing with outliers by adding a multiview inlier/outlier classification module that respects the model equivariance and by utilizing a robust bundle adjustment step. Experiments demonstrate that our method can be applied successfully in realistic settings that include large image collections and point tracks extracted with common heuristics that include many outliers, achieving state-of-the-art accuracies in almost all runs, superior to existing deep-based methods and on-par with leading classical (non-deep) sequential and global methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an architecture for Multiview Structure from Motion (SfM) focusing on the robust recovery of camera pose and 3D scene structure from large, uncontrolled image collections that contain numerous outliers. Traditional and deep-based SfM approaches often struggle with outlier point tracks resulting from viewpoint variations, illumination changes, and repetitive structures, significantly impacting their performance. The authors propose an enhancement to the deep network architecture proposed by Moran et al. in 2021, incorporating an outlier classification module within a permutation equivariant framework. The revised architecture also integrates a robust bundle adjustment step to correct classification errors. The method has been tested on challenging datasets like MegaDepth and 1DSFM and has shown good accuracy and competitive runtimes against both contemporary deep-learning methods and established classical techniques.

### Strengths
1. This paper improves the existing ESFM framework by integrating a new inlier-outlier classification branch, alongside a robust structure from motion (SfM) mechanism. This approach makes sense, given that outliers represent a primary challenge for SfM methods in real-world applications. Quantitative experiments demonstrate the efficacy of these components.

2. This paper conducts extensive experiments over various datasets to prove their claims.

### Weaknesses
1. The main concern about this work is the novelty of the proposed framework. Compared to ESfM, the new designs are just (1) a simple classfication branch to identify inlier/outlier, which conducts simple binary classfication, and (b) robust BA considering high projection error, point track length, and multi-step refinement. Both these two designs have been proven effective over the long time and are not the new techniques from this work. For instance, systems like COLMAP, Theia, and VGGSfM incorporate variants of robust BA. Numerous matching and tracking methodologies, including SuperGlue, LightGlue, PiPs, and Cotracker, implement classification branches to classify inlier/outlier status. While the reviewer acknowledges the effectiveness and importance of these features, there are reservations about their originality as claimed by this work.


2. Moreover, the section of ablation study needs more thinking. The authors discussed "the impact of our permutation sets-of-sets equivariant architecture" and "importance of the equivariant features". However, as far as the reviewer understands, both these two are the benefits from the architecture of ESfM.  To validate the design choices of this paper, the authors should focus on why their error handling designs are better, instead of proving their base model is better. 


3. Concerns also arise regarding the reliability of the results. If interpreted correctly, the rotational metrics in the study are reported in degrees, not radians. Notably, in Tables 3 and 4, the reported rotational errors for some methods are as low as 0.02 or 0.03 degrees. The reviewer questions whether such marginal differences are statistically significant enough to discriminate between methods. (e.g., BlendedMVS, despite being half-synthetic, does not offer flawless ground truth)

### Questions
The main question is about the Weaknesses 1 and 2, i.e., what's the main novelty of the proposed method compared to the existing literature?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, authors robustify the existing deep equivariant SfM method from [1] by incorporating an inlier-outlier prediction module and robust Bundle Adjustment. Specifically, deep SfM uses projective factorization on a 2D point track matrix, but the method in [1] assumes that this matrix is complete and outlier-free. Authors in this work argue that these assumptions are unrealistic. Hence, authors proposed a deep equivariant SfM that works on a large collection of internet photos and works with a matrix of point tracks that might have outliers. In their method, they first train an end-to-end outlier prediction and camera poses + 3D point prediction network from a matrix of 2D point tracks. At test time, they use "inlier-outlier" predictions from the pre-trained network to remove outliers and fine-tune the network for 3D pose + 3D points recovery using unsupervised losses for each scene.

Authors show impressive results across different datasets. Their method achieves the best results among deep SfM methods and achieves comparable results to the best classical SfM methods.

References:

[1] Moran, Dror, et al. "Deep permutation equivariant structure from motion." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.

### Strengths
Paper is well-written with a clear objective being robustifying the method proposed in [1]. Overall content of the paper is well-written, coherent, and easy to understand and follow.

The proposed inlier-outlier prediction head shows improvement compared to ESFM [1]. Results across many scenes of indoor and outdoor datasets show that the proposed method improves over [1] and achieves comparable results to the best classical SfM methods.

Authors use unsupervised reprojection losses. This means that the network can be easily fine-tuned for different scenes, removing a limitation of deep SfM networks that they cannot generalize to scenes outside their training sets.

References:

[1] Moran, Dror, et al. "Deep permutation equivariant structure from motion." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.

### Weaknesses
Authors mention that they did not use Mast3R [2] as one of the baseline method because it does not work with large number of images. But, I do think Mast3R [2] is able to work with large sets of images. At least on Stretcha and BlendedMVS experiments, authors should be able to use Mast3R for full 3D reconstruction 

What is not clear from the paper is whether other methods use Robust Bundle Adjustment proposed in this work. I agree robust BA is necessary for accurate reconstruction, but the contribution of the paper is robust "deep equivariant SfM". For apples-to-apples comparison, authors should also compare with Standard BA or authors should apply robust BA post-processing to compared methods. I see that authors do provide ablation study for effectiveness of robust BA, but to verify the claim of deep robust sfm, it would be great to compare all the methods with either regular BA or robust BA.

### Questions
Can we compare with Mast3R / Spann3R [3]? These methods are new way of doing scene reconstruction and does show promise. They are also deep "reconstruction" methods because they use deep networks directly to get 3D pointmaps.  This comparison with help researchers find limitations or benefits of one method over another.

Is it possible to make results table a bit easy to read? Color + bold letters are not visible clearly. It is hard to find best method for each scene. Also, is there a way to get an average of some of metrics across scenes? (or over whole dataset). 

References:

[3] Wang, Hengyi, and Lourdes Agapito. "3d reconstruction with spatial memory." arXiv preprint arXiv:2408.16061 (2024).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies an important problem in multi-view structure from motion, specifically aiming to recover 3D points and camera poses from input point tracks. To this end, based on an existing permutation equivariant architecture, an outlier classification module is integrated to cope with outliers. A robust Bundle Adjustment method is also proposed, based on recursive potential outlier removal. Experiments are conducted on multiple datasets, demonstrating the robustness of the proposed method against existing ones.

### Strengths
The paper is well-presented in general and easy to understand, with a comprehensive literature review and extensive experiments.

### Weaknesses
The paper studies an interesting and practical problem, but the main weakness is its limited contribution.

1. The proposed method is largely built on existing network architecture, the difference being only that outlier classification output channels are added.

2. The proposed solution for handling outliers incurs much additional overhead in the recursive "finetune" process, lacks theoretical justification, comprises inliers recall, and can not reject outliers well (according to Table 7). Thus the contribution of the method is limited. The same problem also goes for the proposed robust Bundle Adjustment method.

### Questions
Experiment-wise, why ESFM* has much larger rotation error in some cases, and why GLOMAP has good rotation predictions but not translation predictions. And it might be better to give the mean errors in the table for more straightforward comparisons.

### Soundness
2

### Presentation
2

### Contribution
1
