# Sample-specific Noise Injection for Diffusion-based Adversarial Purification

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Diffusion-based purification (DBP) methods aim to remove adversarial noise from the input sample by first injecting Gaussian noise through a forward diffusion process, and then recovering the clean example through a reverse generative process. In the above process, how much Gaussian noise is injected to the input sample is key to the success of DBP methods, which is controlled by a constant noise level $t^*$ for all samples in existing methods. In this paper, we discover that an optimal $t^*$ for each sample indeed could be different. Intuitively, the cleaner a sample is, the less the noise it should be injected, and vice versa. Motivated by this finding, we propose a new framework, called Sample-specific Score-aware Noise Injection (SSNI). Specifically, SSNI uses a pre-trained score network to estimate how much a data point deviates from the clean data distribution (i.e., score norms). Then, based on the magnitude of score norms, SSNI applies a reweighting function to adaptively adjust $t^*$ for each sample, achieving sample-specific noise injections. Empirically, incorporating our framework with existing DBP methods results in a notable improvement in both accuracy and robustness on CIFAR-10 and ImageNet-1K, highlighting the necessity to allocate distinct noise levels to different samples in DBP methods. Our code is available at: https://anonymous.4open.science/r/SSNI-F746.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Neural networks are highly susceptible to adversarial noise, which compromises their robustness in critical applications. Diffusion-based purification (DBP) methods address this by introducing Gaussian noise in a controlled process to counteract adversarial noise, typically using a fixed noise level $t*$ across all samples. However, this uniform approach can lead to suboptimal results, as the ideal noise level varies by sample. In response, the authors propose Sample-specific Score-aware Noise Injection (SSNI), a framework that adaptively adjusts $t*$ based on a sample’s deviation from the clean data distribution, estimated through score norms. By tailoring noise levels—lower for cleaner samples and higher for noisier ones—SSNI enhances both accuracy and robustness across benchmarks like CIFAR-10 and ImageNet-1K, outperforming traditional DBP methods.

### Strengths
1. The need for sample-based noise injection is intuitive and well-motivated. I really like Figure 1.
2. The paper is well-written and easy to follow.

### Weaknesses
First, I would like to make a note that my background is more on diffusion rather than adversarial perturbation. Thus, I am not sure about the significance of the empirical performance of the proposed method, compared to the baselines. I will leave the assessment of this part to the other reviewers more qualified than me.

My biggest concern with the paper is that a lot of the arguments and designs feel hand-wavy without proper principles or justification. I will write the detailed point below.

1. I would like to point out that diffusion models are never trained to model the score directly, but scaled versions of its variants, and only represent scores through reparametrizations. Typically, the training objective of diffusion models is parameterized so that the model's prediction has a **constant** norm across noise levels (for the ease of training), for example, the $\epsilon$-prediction in DDPM and the more modern EDM [1,2]. The difference in terms of the score norm comes only from $t$ through reparametrization. Essentially, in terms of diffusion model training, they are not trained to differentiate the norm of the scores across noise levels. This property holds for the two models the authors used in experiments. Thus, I am wondering what exactly the authors observe here in Figure 4 in Appendix B. How is this score norm calculated? Is this calculated through a pre-trained model or through some analytic solution? If the pre-trained models' output norm really correlates with the sample $x$ (and we should keep the input of time/noise level constant), then it is really an undesired outcome of those models. Then what about the more modern, better-trained models, like EDM?
2. I am also confused by the logic that the further "away" the sample is from the "clean" distribution, the more noise we need to inject for purification. In particular, why are we adding a proportional amount of noise estimated in the sample again? For example, if the procedure estimates the model is at time $t$, Algorithm 1 essentially forwards the sample to $t+t'$ time right? I don't understand the logic behind this choice. Also, now when you run the backward sampling process, do you start at $t+t'$ or $t'$? Essentially, when you do the forward and backward, are you treating the test (start) sample $x$ as a clean or a noisy one in terms of diffusion?
3. The two realizations of the reweighting function have no justification at all. Also, how is the bias term $b$ selected?

### Questions
1. The sub-caption of Figure 1 can be simplified (shared).
2. Judging from Equation 7, are you suggesting to evaluate the pre-trained diffusion model on many $t$s? If so, this requires many network evaluations, right?
3. On Line 344, I think you mean "the key idea is to scale the coefficient" right? Instead of scaling $\|EPS(x)\|$.
4. The time overhead reported in Section 5.5 is not very meaningful. Some relative measurements are more desired.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new framework, called Sample-specific Score-aware Noise Injection (SSNI). SSNI uses a pre-trained score network to estimate how much a data point deviates from the clean data distribution, then adaptively adjusts the injected noise level for each sample, achieving sample-specific noise injections for diffusion-based purification.

### Strengths
A new framework that adaptively adjusts the injected noise level for each sample, thus achieving sample-specific noise injections for diffusion-based purification.

### Weaknesses
There are some unclear points that need more clarification; and insufficient theoretical justifications; see below for detailed questions.

How is the standard accuracy calculated? Are the clean samples also purified before applying the pre-trained classifier network?

What is the value of t within s_\theta in eq (5)?

It is a bit confusing to me how the theoretical results in sec 3 support the claimed relationship between score norm and the optimal noise level. It seems like that Lemma 3 and Prop 1 are about the score norm of $p_t(x)$ where $p_t$ is the marginal distribution of $x_t$, generated by injecting sequential Gaussian noise to clean data $x_0$. In practice, the data may be attacked in different ways and contained by non-Gaussian noise. I think it would be more beneficial to present the theoretical insights for the score norm evaluated on contaminated data under certain attacks (maybe measured by the contamination level $\epsilon$), and how this norm depends on the contamination level $\epsilon$, thus showing that it will be significantly larger than the score norm of clean data.

### Questions
How is the standard accuracy calculated? Are the clean samples also purified before applying the pre-trained classifier network?

What is the value of t within s_\theta in eq (5)?

It is a bit confusing to me how the theoretical results in sec 3 support the claimed relationship between score norm and the optimal noise level. It seems like that Lemma 3 and Prop 1 are about the score norm of $p_t(x)$ where $p_t$ is the marginal distribution of $x_t$, generated by injecting sequential Gaussian noise to clean data $x_0$. In practice, the data may be attacked in different ways and contained by non-Gaussian noise. I think it would be more beneficial to present the theoretical insights for the score norm evaluated on contaminated data under certain attacks (maybe measured by the contamination level $\epsilon$), and how this norm depends on the contamination level $\epsilon$, thus showing that it will be significantly larger than the score norm of clean data.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The work provide a method to adapt the diffusion step for each sample in adversarial purification based on diffusion model in order to enhance the trade-off between robust acc and test acc. The paper use the norm of score to reflect how much a data point deviates from the clean data distribution and utilize the metric to design the diffusion step function. The work show a theoretical explanation that the score norm can act as a proxy for distinguishing between noise levels.

### Strengths
Good theory and experimental results

### Weaknesses
None

### Questions
How to adapt bias in the reweighting function in different datasets and network ?

### Soundness
3

### Presentation
3

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
In this paper, the authors proposed to purify the adversarial examples via diffusion models with sample specific noise levels. Hence the adversarial purification can both sufficiently remove the adversarial attacks and preserve the semantic information. In order to obtain the sample-specific noise levels, the authors started from their other key finding that the difference between the clean image and the data point in the purification process can be measured using the score norm. In their experiments, the proposed method SSNI demonstrated both higher standard accuracy and robust accuracy than the baseline diffusion-based purification methods

### Strengths
1. *Originality*: It is an original approach to measure the difference between the clean data and the data point sampled from the reverse process in the diffusion model, using the score norm. Given this score norm, it is also novel to compute sample specific noise levels for purification on the adversarial examples.

2. *Clarity*: The core method sample-specific score-aware noise injection is clearly articulated. It is easy to follow from the framework of the method to the design of experiments. The key contributions are also explicitly presented with high clarity.

### Weaknesses
1. *Presentation*: The presentation of this work should be improved, especially for the visual presentation. For example, Figure 1 would be clearer to deliver the observations using the ImageNet dataset, because it has higher-resolution images which allow the audience to distinguish the objects.


2. *Quality*: I would highly recommend the authors to have a sufficient check on their lemmas and propositions, especially the proofs. Based on the coherent and flawless proofs, the lemmas and the propositions would be more convincing and solid. For example, the plus or minus sign in the proof of Proposition 1 when they apply the Cauchy-Schwarz inequality. More examples can be seen in **Questions**.

### Questions
1. In terms of the significance and the novelty of this paper, could the authors compare the novelty of this work with Diffusion Models Demand Contrastive Guidance for Adversarial Purification to Advance [1] in ICML 2024 in terms of the $t^*$ selection? It would be better to present the difference to highlight the contributions in this submitted paper.

2. For Lemma 3, there is a minor question on in the proof: it seems that given $K>0$, $(1 - \epsilon - K\epsilon) || \mathbf{x} || \geq (1-2\epsilon) ||\mathbf{x}||$ may not hold. Would the authors please elaborate it?

3. For Proposition 1, could the authors explain why the derivative of $\bar{\alpha}_t$ is $\frac{\partial \bar{\alpha}_t}{\partial t} = -\beta_t \bar{\alpha}_t$, given $\bar{\alpha}_t= \prod^t (1-\beta_t)$? 

4. BPDA+EOT as a white-box attack has been shown to achieve lower attack success rate than those utilizing direct gradients of the defense process when evaluating diffusion-based purification methods [2]. It would be better to elaborate the reason why BPDA+EOT is chosen to evaluate the proposed diffusion-based purification method.
    

[1] Bai, M., Huang, W., Li, T., Wang, A., Gao, J., Caiafa, C.F. & Zhao, Q.. (2024). Diffusion Models Demand Contrastive Guidance for Adversarial Purification to Advance, Proceedings of the 41st International Conference on Machine Learning.

[2] Minjong Lee and Dongwoo Kim. Robust evaluation of diffusion-based adversarial purification. In ICCV, 2023.

### Soundness
2

### Presentation
2

### Contribution
2
