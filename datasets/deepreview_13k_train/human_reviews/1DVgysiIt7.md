# Improved Diffusion-based Generative Model with Better Adversarial Robustness

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Diffusion Probabilistic Models (DPMs) have achieved considerable success in generation. However, its training and sampling processes are confronted with the problem of distribution mismatch. During the denoising process, the input data distributions of the model are different during the training and inference stages, which makes the model potentially generate inaccurate data. To obviate this, we conduct an analysis of the training objective of DPM, and theoretically prove that the mismatch can be mitigated by Distributionally Robust Optimization (DRO), which is equivalent to conducting robustness-driven Adversarial Training (AT) on the DPM. Furthermore, for the recently proposed consistency model (CM), which distills the inference process of the DPM, we prove that its training objective similarly faces the mismatch issue. Fortunately, such a problem is also mitigated by AT. Thereafter, we propose to conduct efficient AT on both DPM and CM. Finally, a series of empirical studies verify the effectiveness of AT in diffusion-based models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to introduce DRO to address the distribution matching problem at training diffusion model.

### Strengths
1. The paper present theories to show that DRO can help address the distribution matching problem in training and testing diffusion models.

2. The improvement over baselines on Cifar and Imagenet64 show that DRO is useful.

### Weaknesses
1. There is no qualitative comparisons. Authors mainly conduct experiments on Cifar, ImageNet and Laion dataset. It would be better to put some images for more direct comparisons. In addition, the code is not provided. 

2. The efficiency comparison. I am wondering how much overhead it brings to adopt eq 14 instead of the classical denoising objective.  I am expecting that it is quite large.

### Questions
as above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the training of unconditional diffusion model. In particular, in order to achieve a better generation quality and enable robust learning of the score network, this paper develops a DRO-based method, and prove the DRO objective in training diffusion models can be formulated as an adversarial learning problem. The paper also identifies a similar mismatch issue in the recently proposed consistency model (CM) and demonstrates that AT can address this problem as well. The authors propose efficient AT for both DPM and CM, with empirical studies confirming the effectiveness of AT in enhancing diffusion-based models.

### Strengths
1. This paper performs a theoretical analysis of diffusion models and identifies the distribution mismatch problem.

2. This paper further builds a connection between the distribution robust optimization and adversarial learning for diffusion models, and develops an adversarial training method for diffusion models.

3. This paper conducts efficient adversarial training methods on both diffusion models and consistency models in many tasks. Experimental results demonstrate the effectiveness of the developed algorithms.

### Weaknesses
1. In general, the algorithm developed in this paper is motivated by the distribution mismatch along the diffusion path. However, there is no experimental results to justify the motivation, there are also no experimental results to verify that the DRO framework can indeed help mitigate the distribution mismatch problem. Specifically, while the paper claims to address distribution mismatch, there is no direct measurement of the distance between the distributions of generated intermediate samples and the true data distribution at corresponding noise levels. This makes it difficult to assess whether the proposed method actually achieves its stated goal.

2. Proposition 2 has already been discovered in existing theoretical papers [1], see their section 3.1. The authors should comment on this point around Proposition 2. The lack of acknowledgment of prior work on similar theoretical results is a significant oversight, and the authors should clearly differentiate their contribution from existing literature.

3. The advantage of ADM-AT is not that significant compared with the ADM method, a more detailed ablation study or theoretical analysis on using adversarial noise or random Gaussian noise should be added. The empirical results, while showing some improvement, do not convincingly demonstrate the superiority of adversarial noise over simpler alternatives like Gaussian noise. A more rigorous analysis is needed to justify the added complexity of the adversarial approach.

4. Some statements are not clearly presented. For instance, the description of ADM is not given, the norm notations $\|\|$ are abused, should that be $\ell_1$, $\ell_2$, or $\ell_\infty$?

### Questions
1. some ablation studies for different perturbation levels $\alpha$ should be given.
2. Some discussions about different perturbation methods ($\ell_1$, $\ell_2$, or $\ell_\infty$) should be discussed.

### Soundness
3

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
4

### Summary
This paper identifies the distribution mismatch problem in the training and sampling processes. Consequently, they propose a distributionally robust optimization procedure in the training to bridge the gap. The authors apply the method to both diffusion models and the consistent model, and demonstrate the effectiveness of the proposed method on several benchmarks.

### Strengths
1. Identifying and formulating the distribution mismatch problem in diffusion model is an important problem in practice.
2. The proposed solution is elegant, supported by sufficient theoretical analysis. The derivations of the solution is clear and sound.
3. The writing is fairly clear.

### Weaknesses
My main concern on this paper is the evaluation. Currently the proposed method is only evaluated using the ADM model. I wonder whether the effectiveness on more advanced model such as the stable diffusion still holds?

Furthermore, the authors only use FID score as the evaluation metric, while it is easy to evaluate the results using other metrics such as IS, sFID, precision, recall, as done in the ADM paper. Why these metrics are not included?

### Questions
The paper is a good one in general. I like how the problem is formulated and how the solution is derived. However, given the current evaluation (see the weakness), I am not fully convinced the proposed method is an effective way to deal with the problem. I would like to see how the authors respond to my concerns.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper points out the distribution mismatching problem in traditional training of diffusion-based models (DPM) and proposes to conduct efficient adversarial training (AT) during the training of DPM to mitigate this problem. Theoretical analysis is strong enough to support its argument and experiments also verify the effectiveness of the proposed method.

### Strengths
1. The motivation for mitigating distribution mismatching is clear and important for efficient sampling. 

2. This paper provides strong theoretical support for implementing adversarial training to correct distribution mismatching, making this method convincing.

### Weaknesses
1. The experimental results may not be enough, for example, for Table 1 and Table 2, more NFEs should also be verified, although this method can improve efficient sampling, whether is adaptable and robust for more denoising steps should also be verified. Specifically, the current experiments only explore a limited range of NFEs, and it's unclear how the proposed adversarial training method behaves with significantly more or fewer denoising steps. The performance could degrade when pushed to more extreme settings, which is important to demonstrate for practical use.

2. Some complex derivations in supplementary material are too brief to understand, such as Eq(30) and Eq(59-62), I'm not sure if there are any typos in them, I suggest checking the equations carefully and modifying them. The lack of detailed explanations makes it difficult to verify the correctness of the derivations, and the potential typos raise concerns about the validity of the theoretical claims. Without clear and complete derivations, it's hard to assess the soundness of the proposed method.

### Questions
1.  As the weakness above, for Table 1 and Table 2, more NFEs should also be verified.

2. Why not also try generation using consistency models on benchmark datasets such as CIFAR10 and ImageNet, which can be more common and convincing?

3. Derivations in supplementary material should be checked carefully and written with more details. 

4. Why efficient AT can improve performance compared with PGD is a bit confusing. Intuitively, PGD should be more accurate to find $\delta_t$, thus more deep insights should be provided here.

### Soundness
3

### Presentation
2

### Contribution
3
