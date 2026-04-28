# Manifold Constraint Reduces Exposure Bias in Accelerated Diffusion Sampling

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6, 6

## Abstract
Diffusion models have demonstrated significant potential for generating high-quality images, audio, and videos. However, their iterative inference process entails substantial computational costs, limiting practical applications. Recently, researchers have introduced accelerated sampling methods that enable diffusion models to generate samples with far fewer timesteps than those used during training. Nonetheless, as the number of sampling steps decreases, the prediction errors significantly degrade the quality of generated outputs. Additionally, the inherent exposure bias in diffusion models causes errors to propagate and amplify, further introducing non-negligible inaccuracies in inference. To address these challenges, we leverage a manifold hypothesis to explore the exposure bias problem in depth. Based on this geometric perspective, we propose a manifold constraint that effectively reduces exposure bias during accelerated sampling of diffusion models. Notably, our method involves no additional training and requires only minimal hyperparameter tuning. Extensive experiments on high-resolution datasets demonstrate the effectiveness of our approach, achieving a FID score of 15.60 with 10-step SDXL on MS-COCO, surpassing the baseline by a reduction of 2.57 in FID.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To narrow the gap between the training of the sampling phase of diffusion models, the authors analyze the diffusion processes from the view of the manifold. They propose to compute the statics of all intermediate diffusion variables and calibrate the sampling process based on the computed statics (variance, mean, \etc). Experiments show that the proposed method can reduce the sampling steps while maintain the generation quality.

### Strengths
1. The proposed method improves sample quality without adding substantial computational overhead.
2.Unlike some prior methods, this approach does not require model retraining or intensive hyperparameter tuning.
3. The manifold constraint method shows improved performance across various high-resolution datasets, achieving better FID scores with fewer sampling steps.
4. The paper provides both theoretical analysis and empirical evidence to support its method, including experiments on multiple tasks like image and video generation.

### Weaknesses
1. The proposed method needs to be verified on more diffusion schedulers, such as DPMSolver, PNDM.

2. Some ODE-based diffusion models such as rectified flow and consistency models can reduce the sampling steps to two or even one. The proposed method focuses on accelerating the sampling process but is not compared with these fast-sampling diffusion models.  The authors are encouraged to apply their methods to more recent diffusion models (\ie SD3, FLUX) to show their priority and general ability.

### Questions
See the weakness above

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
4

### Summary
- This paper proposes a method for improving the performance in accelerated diffusion sampling algorithms
- The paper identifies the exposure bias in accelerated diffusion sampling 
- The method applies manifold constraint for reducing the exposure bias that occurs in accelerated sampling.
-  The paper presents evaluations of the methods showing improvements over the baseline.
- A discussion on the geometric view of the exposure bias is presented.

### Strengths
- The paper is well written
- The method is evaluated on multiple diffusion models trained on different datasets
- The method is simple yet effective. It does not require any further training and the additional computations are marginal.
- The approach shows an improvement over the baselines in most cases

### Weaknesses
 - The derivation of section 4.2 is relatively weak, many assumptions and loose steps need to be either refined or omitted.
  - In section 4.2, you assume that $E[\epsilon_\theta^t]=0$, but this is not always the case. This assumption, while potentially valid in practice with well-trained models, lacks rigorous justification within the analytical framework. The derivation relies on this assumption without explicitly addressing the potential impact of deviations from this condition on the derived bounds. The analysis should either account for the variance of this term or provide a more robust justification for its omission.
  - In Equation (12) the authors utilize the fact that $\frac{1}{n}\sum_{i=1}^n \hat{x}_i \approx 0$, which does not always hold. This approximation is not universally valid and requires more careful consideration. The authors should either provide a theoretical justification for this approximation or empirically demonstrate its validity across different datasets and model architectures. The impact of this approximation on the final results needs to be quantified.
  - Equation (15) does not hold, an expectation value is required for it to be true. The equation as presented is not mathematically sound without the inclusion of an expectation operator. This oversight undermines the validity of the subsequent analysis and needs to be corrected.
- The evaluations include only comparison to DDIM, even though there are many accelerated samplers that achieve much better results [1,2,3], adding them to the tables is very important for evaluating the method.

### Questions
- Figure 3: the x-axis title is not clear, what do you mean by denoising steps if the sampling steps are given in the legend? and in general the figure needs to be explained properly
- In section 4.2, you assume that $E[\epsilon_\theta^t]=0$, but this is not always the case.
- Equation 15 does not make any sense without expectation value.

### Soundness
3

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
This paper views the issue of the quality degradation during accelerating diffusion model’s inference on the perspective of the explore bias. The authors point out that explore bias is an important reason that contributes to the loss of image quality when reducing inference steps. The noisy prediction will direct to inaccurate manifolds and thus the errors would be accumulated and amplified. A manifold constraint is proposed to curate this bias and thus lead to better image quality when significantly reducing inference steps.

### Strengths
1. The proposed method is well supported by a series of proofs with some assumptions.
2. The quantitative results look very promising, and largely outperforms the alternative.E.g.,  in Table 3, MCDO with 4 steps has better results than DDIM with 5 steps.
3. The method is well motivated and the writing logically reasonable and flows well.

### Weaknesses
1. Assumption 3 is a very important part in deriving the manifold constraint. I think it is too strong. I understand it's motivated by Equation (17), however \hat{x}_0 could have a different distribution of x_0 which is inaccessible during inference. Could you elaborate more?
2. There are some details not explained well for some key equations/explanations. I added those in the questions below.



### Questions
1. In table4, why do fewer steps have lower FID?
2. Can you add more details of how to get equation 11 and 16 in the appendix?
3. I didn’t understand why \epslon_t is equal to \sqrt{n} when n is large in L261? Can you explain?
4. Can you elaborate on L271? In my understanding, in fig3, var(x_t) decreases faster as reducing steps, thus potentially making d(.) larger than r_t in later steps. But figure 3 is only on one sample, how to generalize this observation?
5. The qualitative examples look a bit over-saturated, it would be helpful if you can also show an oracle results (e.g., 1000 steps) on the side for comparison.

### Soundness
3

### Presentation
3

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
This paper presents an approach to enhance the efficiency and accuracy of diffusion models by addressing the issue of exposure bias in accelerated sampling. Leveraging a manifold hypothesis, the authors introduce a manifold constraint that reduces error accumulation during sampling without requiring additional training or extensive tuning.

### Strengths
1. The use of the manifold constraint is an interesting idea, which addresses exposure bias without adding additional training costs during sampling.
2. The use of well-chosen visualizations enhances the readability of the method section, conveying key information and clarifying the approach.
3. The paper is technically clear and well-organized, with the proposed method thoroughly explained.

### Weaknesses
1. The term "denoising observations" requires a clear and precise definition, as its current use lacks specificity. A more rigorous description would help readers to understand and improve the technical clarity of the paper. Specifically, the paper should clarify whether these observations are simply the intermediate outputs of the denoising process, or if they are derived in some other way. The term is used without sufficient context, making it difficult to understand the exact nature of the data being used to derive the manifold constraint.
2. The pre-computation process still requires a full denoising sequence (e.g., 1000 steps), which incurs substantial computational cost, especially when applying the proposed method to new datasets or domains. It is suggested that potential strategies for reducing this computational cost be discussed or that an analysis of the trade-offs between the number of steps in pre-computation and the method's performance be provided. The computational cost is a significant practical limitation, and the paper should explore methods to mitigate this, such as using a smaller number of steps or a more efficient method for estimating the required statistics. The current approach limits the applicability of the method to scenarios where pre-computation is feasible.
3. The number of samples and their diversity will influence the resulting approach $v_t$. However, the experiments simply set the sample number to 20 without discussing the diversity of prompts or other characteristics of the samples. Including these details would be valuable for readers to have a better understanding, and provide insights for the community. It is recommended to conduct an ablation study on the impact of sample number and diversity on the performance of the proposed method, or to provide more details on how you selected the 20 samples used in the experiments. The paper should also discuss the potential impact of using samples generated from the same model, as this could introduce bias into the estimation of $v_t$.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
From the manifold hypothesis, the paper proposes a method to reduce Exposure Bias by adjusting the variance of $x_t$ at each step to match the variance of $q_t$ made by the forward diffusion process. The paper demonstrates that this approach yields FID gains across various model and datasets.

### Strengths
They validated the method in various datasets and methods. 

It is good to see that the method proposed from this work can be combined with the method from previous literature, i.e., DDIM-MCDO^\dagger.

### Weaknesses
 **1. strong assumption**

Assuming that the manifold can be understood solely by considering variance is too strong an assumption. It might be better to tone it down to suggest that this approximation is sufficient for performance improvement.



### Questions
**Q1**: Using the statistics of the data directly in generation—could this be seen as an FID "hack"? For example, I’m curious how the FID would change if the mean and variance of the generated data w/o MCDO were adjusted to match \( q_0 \).

**Q2**: Does this method can improve other ODE solvers like DPM-solver++ [1] or PNDM [2]? I know that DDIM performs poorly when the NFE is below 50. I also want to see the results where NFE is around 50.

[1]: DPM-Solver++: Fast Solver for Guided Sampling of Diffusion Probabilistic Models ([Arxiv](https://arxiv.org/abs/2211.01095))
[2]: Pseudo Numerical Methods for Diffusion Models on Manifolds ([ICLR22](https://arxiv.org/abs/2202.09778))

**Q3**: (Minor) When comparing performance, I recommend plotting FID on the y-axis and NFE on the x-axis for clarity.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the exposure bias of accelerated diffusion model sampling from geometry perspective. The authors extend the previous manifold constraint theory with more detailed description of pixel variance, claiming that both exposure bias and truncation error account for the performance degradation. To this end, the authors propose to pre-calculate the reference pixel variance, which serves as a correction during inference. Such method achieves a training-free and easy-to-implement solution to performance degradation. Comprehensive experiments confirm the efficacy of the proposed algorithm.

### Strengths
- The paper is well structured and easy to follow. Most of the derivation is clear.

- The paper extends the previous manifold constraint strategy with deeper study of the pixel variance and the consequent exposure bias, providing a novel perspective of geometric technique in diffusion models.

- The proposed algorithm is overall both efficient and effective, inference time cost barely increases.

- Quantitative experiments are convincing and extensive.

### Weaknesses
 - There seem some theoretical flaws in the draft, harming the soundness:
  1. Eq. (15) is wrong, when $x$ and $y$ are orthogonal, one can only deduce that $|x+y|^2=|x|^2+|y|^2$. Besides, what is the definition of $x_0$ and $\epsilon_t$? $\epsilon_t$ and $x_0$ may not be orthogonal if no further assumption are made.
  2. I cannot understand the relation between Eq. (18) and analytical form of $Var(x^{(t)}_0)$ and $Var(x_t)$, $Var(\cdot)$ is supposed to be the pixel variance as claimed in Eq. (12) which is a scalar. The connection between the derived equations and the pixel variance is not clearly established, making the theoretical justification weak.
  3. Eq. (16) and Eq. (19) are similar, but the authors conclude differently. If minimizing right hand side in Eq. (19) could lead to the distance reduction, then so could minimizing right hand side in Eq. (16) be. They are all the **lower bounds** of distance of samples to manifold. The distinction between these two equations and their implications for the proposed method needs further clarification.
  4. If the authors insist that nonzero $|x_0|$ affects the derivation, then (1) since $\hat{x_t}\in\mathcal{M}_t$, one can simply choose $x_0=0$ (which is reasonable since the authors have already assumed zero mean in L346), or (2) move the term with $|x_0|$ outside the absolute value using $|a+b-c|\geqslant|b-c|-|a|$, which is similar to the form of Eq. (19). The authors should make further clarification. The current justification for including the $x_0$ term is not sufficiently strong.
  5. Why assume zero mean in L346? $\hat{x}_0^{(t)}$ is the denoise observation at timestep $t$, somewhat a data sample with no noise. Then why is the case? The authors could calculate the mean to confirm the reasonability. The assumption of zero mean for the denoised observation needs more rigorous justification, especially given its role in the derivation.

- Figs. 4 and 6 only employ 64 samples, which seems inconvincing. The statistical significance of using only 64 samples for the analysis is questionable, and the results may not generalize well to larger datasets.

- Visualization in Fig. 7 fails to be photorealistic with obvious color shift artifact, which is also the case in Fig. 12. The color shift artifact in the visualizations raises concerns about the method's ability to generate high-quality, realistic images. The color shift is not a minor artifact, but a significant deviation from photorealism.

### Questions
- It is intuitive that applying MCDO with larger NFEs or better sampler will achieve weaker improvements. I am curious about the comparison on better sampler like Heun or DPM-Solver. There is also no discussion about applicability on high-order samplers.

- MCDO is proposed for manifold constraint to relieve exposure bias, how will the efficacy vary if different CFG scales are set? Larger CFG scale may also lead to severe exposure bias.

### Soundness
4

### Presentation
3

### Contribution
3
