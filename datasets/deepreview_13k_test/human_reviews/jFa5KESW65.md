# IRAD: Implicit Representation-driven Image Resampling against Adversarial Attacks

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
We introduce a novel approach to counter adversarial attacks, namely, image resampling. Image resampling transforms a discrete image into a new one, simulating the process of scene recapturing or rerendering as specified by a geometrical transformation.
The underlying rationale behind our idea is that image resampling can alleviate the influence of adversarial perturbations while preserving essential semantic information, thereby conferring an inherent advantage in defending against adversarial attacks.
To validate this concept, we present a comprehensive study on leveraging image resampling to defend against adversarial attacks. We have developed basic resampling methods that employ interpolation strategies and coordinate shifting magnitudes.
Our analysis reveals that these basic methods can partially mitigate adversarial attacks.
However, they come with apparent limitations: the accuracy of clean images noticeably decreases, while the improvement in accuracy on adversarial examples is not substantial.
We propose implicit representation-driven image resampling (IRAD) to overcome these limitations. First, we construct an implicit continuous representation that enables us to represent any input image within a continuous coordinate space. Second, we introduce SampleNet, which automatically generates pixel-wise shifts for resampling in response to different inputs.
Furthermore, we can extend our approach to the state-of-the-art diffusion-based method, accelerating it with fewer time steps while preserving its defense capability.
Extensive experiments demonstrate that our method significantly enhances the adversarial robustness of diverse deep models against various attacks while maintaining high accuracy on clean images.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel image resampling approach for adversarial attacks. Specifically, two implicit neural representations are adopted to model the image reconstruction and shift map, respectively. With the estimated continuous representation and the learned shifting, the generated image becomes robust toward adversarial attacks. This method achieves significant performance on several benchmarks.

### Strengths
1. The proposed method provides a novel approach to solving the adversarial attack problem. This is the first paper to solve the problem in such an implicit representation manner. The idea is impressive。

2. The writing is easy to follow. It starts with the naive solution, and then gradually introduces the proposed one. Each step is logically based on the last step.

3. The experimental results are strong. It not only significantly outperforms baselines in Table 1, but also achieves higher performance than state-of-the-art approaches with totally different solutions.

### Weaknesses
1. One important ablation study is lacking. Table 8 verifies the effectiveness of the SampleNet. However, the usefulness of RECONS is not proven. How about the performance of bilinear interpolation with SampletNet?

2. The learned shift map contains explainable information, however, analysis of which is lacking. The only visualization shown in Fig 2 contains little information and a deeper analysis should be adopted.

3. The running time of the proposed method is not provided.

### Questions
Are there any severe distortions in the shift map?

### Soundness
4 excellent

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new method for defending against adversarial attacks. Given an input image, the proposed method aims to first build an implicit representation and then reconstruct the image by resampling. For further improvement, the paper also proposes to introduce a network to dispatch different inputs to different level pixel-wise shifts for resampling. Experiments results show that the proposed methods improve the adversarial robustness.

### Strengths
- The underlying idea and the proposed method appear very novel to me. 

- The paper conducts extensive experiments and demonstrates significant improvements over the baseline.

- The paper is well-written and easy to read

### Weaknesses
I am having difficulty being convinced of why this approach works. The paper's objective is to construct an implicit representation for the input image and then reconstruct the clean image from this implicit representation, claiming that the reconstructed image would be free from any adversarial patterns. However, if we assume that the underlying implicit representation faithfully represents the input signal, it should also contain the adversarial patterns that present in the input signal. This contradicts the explanation for why the proposed method is effective.

To the best of my thoughts, the only plausible explanation to explain why the proposed method works well quantitatively is that the underlying implicit representation is biased toward fitting low-frequency or smooth signals, and thus, it fails to represent high-frequency adversarial patterns. However, this would imply a degradation in the image quality represented in the implicit model, as it suggests that the model cannot faithfully represent high-frequency signals. In either case, this highlights certain weaknesses in the proposed method

### Questions
See my comments on the weaknesses session above. I'm willing to improve my rating if the author can convince me in the rebuttal period.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a test-time adversarial defense mechanism realized via image resampling. Central to their proposal is the "Implicit Representation Driven Image Resampling (IRAD)" methodology, which operates in two distinct phases: a) the creation of a continuous coordinate space, and b) the utilization of the newly proposed SampleNet. Unlike conventional heuristic sampling strategies, SampleNet is designed to predict pixel-wise shifts based on the embedding of the input image automatically. Moreover, in a pursuit of optimal performance and a marked increase in processing speed, the authors have integrated their method with DiffPure.

### Strengths
1. The introduced image-resampling defense "IRAD" substantially enhances the Robust Accuracy (RA) when juxtaposed with the elementary implementation of image resampling (IR).
2. The paper presents SampleNet, a novel approach for automated sampling, designed to supplant traditional heuristic sampling strategies.
3. The methodology presented has been rigorously evaluated across various datasets and neural network architectures.

### Weaknesses
1. There's room for optimization in the placement of tables and figures to enhance readability and presentation.
2. Merging IRAD with a 20-step DiffPure yields superior results while economizing computation time. Nonetheless, a more comprehensive analysis examining the integration of IRAD with varying steps of DiffPure would enrich the study's depth and relevance.

### Questions
None

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors adopt image resampling to defend against adversarial attacks. In particular, they first construct an implicit continuous representation for reconstruction. Second, they introduce SampleNet, which automatically generates pixel-wise shifts for resampling. And their method can be extended to the state-of-the-art diffusion-based method, which is significantly accelerated.Extensive experiments on several datasets have shown the effectiveness.

### Strengths
1. The paper is well-written and easy to follow.

2. Adopting image resampling is a novel and interesting idea to defend against adversarial attacks.

3. The proposed SampleNet is simple yet effective, which can effectively defend against adversarial attacks to some extent.

4. They have adopted various datasets to validate the effectiveness.

### Weaknesses
1. It is not clear why resampling can effectively defend adversarial examples. Especially, image resampling via bilinear or nearest interpolation might be not effective enough to eliminate adversarial perturbation.

2. How can you guarantee that SampleNet is not attacked? As a result, in Table 5, IRAD cannot exhibit robustness when SampleNet is attacked simultaneously. 

3. In my opinion, such a resampling method cannot effectively defend against white-box attacks. However, it might be effective in defending against black-box attacks, especially transfer-based attacks [1,2,3]. I suggest you add such a comparison.

4. Since image resampling pre-processes the input image before the model, it is similar to a purifier that eliminates adversarial perturbation [4]. I think it is necessary to compare with such baselines.

[1]  Zhang et al. Patch-wise attack for fooling deep neural network. ECCV 2020.

[2] Wang et al. Enhancing the transferability of adversarial attacks through variance tuning. CVPR 2021.

[3] Wang et al. Admix: Enhancing the transferability of adversarial attacks. ICCV 2021.

[4] Naseer et al. A self-supervised approach for adversarial robustness. CVPR 2020.

### Questions
See weakness

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
