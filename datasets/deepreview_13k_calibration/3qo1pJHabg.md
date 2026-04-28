# LRR: Language-Driven Resamplable Continuous Representation against Adversarial Tracking Attacks

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Visual object tracking plays a critical role in visual-based autonomous systems, as it aims to estimate the position and size of the object of interest within a live video. Despite significant progress made in this field, state-of-the-art (SOTA) trackers often fail when faced with adversarial perturbations in the incoming frames. This can lead to significant robustness and security issues when these trackers are deployed in the real world.
To achieve high accuracy on both clean and adversarial data, we propose building a spatial-temporal implicit representation using the semantic text guidance of the object of interest extracted from the language-image model (\ie, CLIP). This novel representation enables us to reconstruct incoming frames to maintain semantics and appearance consistent with the object of interest and its clean counterparts.
As a result, our proposed method successfully defends against different SOTA adversarial tracking attacks while maintaining high accuracy on clean data. In particular, our method significantly increases tracking accuracy under adversarial attacks with around 90\% relative improvement on UAV123, which is close to the accuracy on clean data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an adversarial defense method against recent attacks on visual object tracking. The defense method is guided by the language-image mode CLIP to reconstruct the area that has been perturbed by attacks. Two modules named the spatial-temporal implicit representation (STIR) and the language-driven resample network (LResampleNet) are involved in the whole framework to obtain a consistent representation. The experimental results against four attack methods are evaluated on three datasets.

### Strengths
1. The idea of using an image-language model (CLIP) to defend against adversarial attacks is interesting.
2. The experiments show the effectiveness of the proposed defense against various types of adversarial attacks and can be applied to different trackers (e.g., CNN-based and transformer-based trackers).

### Weaknesses
1. The proposed method basically relies on the reconstruction technology to destroy the distribution of perturbations. For VOT, does the proposed method reconstruct the whole search image? An intuitive and simple idea is to apply the inversion technology in StyleGAN or Diffusion on it, does it work? Please give some analysis on this point.
2. Please provides some visual result on the difference between clean images and adversarial examples, and between clean images and defense examples, to show how the distribution of adversarial perturbations is reduced or suppressed. 
3. The writing of the paper needs to improve. Some results in supplementary materials can be combined in the main paper to better support the effectiveness of the proposed method.

### Questions
1. Please provide some analysis on directly implementing the inversion technology in StyleGAN or Diffusion.
2. Please provide some visual results before and after attacks to intuitively illustrate how the adversarial perturbations are eliminated. 
3. Add the key results and analysis in supplementary materials to the main paper.

### Soundness
3 good

### Presentation
2 fair

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
The authors propose a method to defend visual object tracking against adversarial attacks. They introduce a spatial-temporal implicit representation (STIR) that constructs neighboring pixels, and a language-driven resample network (LResampleNet) that provides consistency between reconstructed frames and object templates. They use the CLIP model to guide their approach. The effectiveness of their method is demonstrated through experiments on the OTB100, VOT2019, and UAV123 datasets, which show that it can effectively defend against recent VOT attack methods.

### Strengths
1. The proposed method considers both the spatial and temporal information during defense, which is reasonable.
2. Using the language-image model to guide the defense process is interesting.
3. The experiments are thorough, including the defense results against various attack methods, as well as ablation studies on the efficiency of each component.

### Weaknesses
1. Provide visual comparisons among clean images, adversarial images, and the image after defense to show the visual effects and their difference. The tracking results should be added as well.
2. For the experiments, the reviewer suggests that the authors compare with basic defense methods, including adversarial training and image preprocessing (e.g., resize or compression). And analyze the pros and cons between the proposed method and the defense methods mentioned above.
3. In Table 1, for the results without defense, how to implement the attack is not clear. In other words, which attack method is selected for the results in Table 1?
4. There are some minor problems, and the author should polish this paper again.
- In Table1, defends -> defense?
- In Table 2 and 3, IouAttack -> IoUAttack. It is a typo.

### Questions
1. Please supply the visual comparisons among clean images, adversarial images, and the image after defense.
2. Please compare with other basic defense methods, like resizing or compression.
3. Please state the details of the experiments in Table 1.
4. Fix the typos and polish this paper again.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work presents a study on improving object tracking performance on adversarial data while maintaining the model's superiority over clean data. The essence is building a spatial-temporal implicit representation using the semantic text guidance of the object of interest extracted from the language-image model. Then the novel representation is used to reconstruct incoming frames. Experimental results on different benchmarks show the effectiveness of the proposed framework. Overall, the paper sounds reasonable.

### Strengths
- The writing is clear and easy to follow.
- Introducing language embedding to adversarial training is interesting.
- Reconstructing video frames to defend against adversarial attacks is reasonable.
- Experimental results are sufficient.

### Weaknesses
 - Although it's interesting to introduce nlp embedding in the adversarial defense framework, it sounds not so reasonable. Using a template seems enough for the purpose. Besides, single-object tracking is class-agnostic. What if the object class is unknown? How to run the proposed model in this situation?
- Lack of experiments on more challenging benchmarks, e.g. trackingnet, tnl2k (Towards More Flexible and Accurate Object Tracking with Natural Language: Algorithms and Benchmark).
- It is noticed that only SiamRPN++ is used as the baseline model. The baseline model is out of date. Do the effectiveness and conclusion still hold on recent transformer-based models, like OSTrack, SwinTrack, MixFormer? What if the tracking model is already able to track objects using natural language like the algorithms introduced in tnl2k.

### Questions
Please conduct experiments on recent trackers and provide results on more challenging and up-to-date benchmarks.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
