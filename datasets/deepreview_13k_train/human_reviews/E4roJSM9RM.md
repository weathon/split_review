# Unveiling the Secret of AdaLN-Zero in Diffusion Transformer

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Diffusion transformer (DiT), a rapidly emerging architecture for image generation, has gained much attention. However, despite ongoing efforts to improve its performance, the understanding of DiT remains superficial. In this work, we delve into and investigate a critical conditioning mechanism within DiT, adaLN-Zero, which achieves superior performance compared to adaLN. Our work studies three potential elements driving this performance, including an SE-like structure, zero-initialization, and a “gradual” update order, among which zero-initialization is proved to be the most influential. Building on this insight, we heuristically leverage Gaussian distributions to initialize each condition modulation, termed adaLN-Gaussian, leading to more stable and effective training. Extensive experiments following DiT on ImageNet1K demonstrate the effectiveness and generalization of adaLN-Gaussian, e.g., a notable improvement of 2.16% in FID score over adaLN-Zero.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates three mechanisms of adaLN-Zero, including the SE-like network structure, zero-initialization, and the weight update order. Based on the analysis of adaLN-Zero, this work proposes an improved initialization method, adaLN-Gaussian, which utilizes Gaussian distributions to initialize the weights of each condition modulation.

### Strengths
The proposed adaLN-Gaussian initialization is simple and effective, achieving remarkable performance.

### Weaknesses
1. The overall logic of the paper is somewhat disorganized, and there is a logical gap between the analysis of adaLN-Zero and adaLN-Gaussian. Could the authors provide a more detailed explanation of why Gaussian distributions are used to initialize weights?
2. This work lacks mathematical analysis; all conclusions are drawn from experimental results and statistics, and the authors only conducted experiments using the ImageNet dataset. I think more extensive and general experiments are needed to validate the effectiveness of adaLN-Gaussian.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work focuses on an overlooked part in the diffusion transformer - the zero initialization of adaptive LayerNorm.
Authors start from the similarity between SENet with DiT's adaLN, and develop some variants from adaLN.
After several discussions about the gradient update over the weight of adaLN and the summarization of the benefits from adaLN-zero, authors  propose to leverage Gaussian distributions to initialize the adaLN.
The exps over IN-1K and DiT-based backbones are sufficiently perferformed.

### Strengths
1. The motivation is very good (the overlooked part in DiT) and the issue in this work in quite interesting.

2. Clear clarity and good presentation.

3. Provide sifficient evidence to support the exploration inside the adaLN-zero, not only the gradient update but also the varients of adaLN.

4. Good and fair experimentss to support the proposed method. Authors provide relatively big scale exps on IN-1K 512X512 which is expensive, and the backbones are mainly based on large scale DiT. Besides authors also evaluate the effectiveness on other DiT-based backbones.

### Weaknesses
1. The start point is very unclear for me. How can you find the similarity between adaLN and SE archtecture？ 
I consider that this start point should be better explained and provide a structure figure of SE archtecture.



### Questions
1. How can you find the similarity between adaLN and SE archtecture？ This is an intersting point. Hope that authors can provide some principles but not intuitions.

2. As shown in Figure2, the performance of Gaussian initialization is a U-shaped trending. Could you please some analysis about this trending? Why the large std can brings a relatively bad results.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates adaLN-Zero, a key component of DiT. They find three key factors that contribute to the superior performance of adaLN-Zero: an SE-like structure, a good zero-initialized value, and a gradual weight update order. The second one plays the most important role. Finally, they propose adaLN-Gaussian, which achieves better results.

### Strengths
1. This paper is easy to follow, and the experiments are relatively sufficient.
2. This paper provides some inspiring conclusions.

### Weaknesses
1. Part of the description needs further explanation, e.g. line 208：They also zeros out weights of all modulations including Wγ1,Wβ1, Wγ2, and Wβ2 in a block, rendering γ1, β1, γ2, and β2 zero.
2. Some of the inferences are intuitive, and it would be better if there were more rigorous analysis. e.g. line 448：Moreover, this moment should be neither too late, ... ,nor too early, as there may be minimal difference from zero-initialization.

### Questions
1. From line 129~130, we know that all alpha are initialized to 0. Can you expalin line 209: why are gama1, beta1, gama2, beta2 also zero?
2. In Table 4, if there is no limit on steps, will the results of adaLN-Zero catch up with adaLN-Gaussian when training for more steps? Do you have any relevant experimental results? Maybe different initialization methods mainly affect the convergence speed.
3. In addition to adaLN-Zero, have you analyzed the distribution of parameters of other parts of DiT? Do they also end up being Gaussian? How were these parameters initialized?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates AdaLN-Zero within the DiT architecture and proposes three potential reasons for the performance difference between AdaLN-Zero and AdaLN: the incorporation of an SE-like structure, the use of an effective zero-initialized value, and a gradual weight update order. The authors conduct a series of analyses, ultimately concluding that the zero initialization is the most significant factor. Building on these findings, they introduce a method that leverages Gaussian distributions to initialize each condition modulation, referred to as adaLN-Gaussian. Extensive experiments demonstrate an improvement of 2.16% in FID on ImageNet1K.

### Strengths
The presentation is clear, three potential reasons for the performance difference between AdaLN-Zero and AdaLN are studied in detail, and the designed experiment is reasonable.

### Weaknesses
1. The contribution of this paper is limited; the only significant advancement is the introduction of adaLN-Gaussian, which leverages Gaussian distributions to initialize each condition modulation in the DiT architecture. The performance gains are also limited.
2. The experiments conducted are insufficient. Training for 800k iterations may not be adequate for the convergence of the DiT model. Given the 2% improvement in the current results at 400k iterations, it raises doubts about whether Gaussian initialization will outperform zero initialization in terms of final performance. Furthermore, to demonstrate the broader applicability of this method, I recommend conducting additional experiments on transformer-based models such as SiT[1] and PixArt-alpha[2] (text-to-image).

### Questions
1. How do you summarize the differences between AdaLN-Zero and adaLN as the three points?
2. In Fig. 4, it appears that regardless of the type of initialization used, the weight distribution converges to a similar state after a certain number of training iterations. This raises the question of why the choice of initialization has such a significant impact on performance.
3. A few minor suggestions: 1) Simplify Figure 6 by merging the subgraphs to enhance information density. 2) Rotate Figure 2 to improve the visibility of the text.

### Soundness
2

### Presentation
3

### Contribution
1
