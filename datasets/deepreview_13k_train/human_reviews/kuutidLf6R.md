# Diffusion Attribution Score: Which Training Sample Determines Your Generation?

- Decision: Accept
- Scores: 8, 6, 10, 6

## Abstract
As diffusion models advance, the scientific community is actively developing methods to curb the misuse of generative models, which aims to prevent the reproduction of copyrighted, explicitly violent, or personally sensitive information in generated images.
One strategy is to identify the contribution of training samples in generative models by evaluating their influence to the generated images, a task known as data attribution.
Existing data attribution approaches on diffusion models suggest representing the contribution of a specific training sample by evaluating the change in the diffusion loss when the sample is included versus excluded from the training process.
However, we argue that the direct usage of diffusion loss cannot represent such a contribution accurately due to the diffusion loss calculation. Specifically, these approaches measure the divergence between predicted and ground truth distributions, which leads to an indirect comparison between the predicted distributions and cannot represent the variances between model behaviors.
To address these issues, we aim to measure the direct comparison between predicted distributions with an attribution score to analyse the training sample importance, which is achieved by Diffusion Attribution Score (DAS).
Underpinned by rigorous theoretical analysis, we elucidate the effectiveness of DAS.
Additionally, we explore strategies to accelerate DAS calculations, facilitating its application to large-scale diffusion models.
Our extensive experiments across various datasets and diffusion models demonstrate that DAS significantly surpasses previous benchmarks in terms of the linear data-modelling score, establishing new state-of-the-art performance.
Code is available at https://anonymous.4open.science/r/Diffusion-Attribution-Score-411F.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
(1) This paper examines the choice of the model output function in D-TRAK, demonstrates the theoretical shortcomings of D-TRAK's choice, and proposes using the predicted noise of a diffusion model as the output function (i.e., the output of the noise predictor). (2) With the proposed model output function, the leave-one-out attribution is approximated with Taylor expansion and Newton's method. (3) Additional tricks such as moving the expectation w.r.t the timestep inside the norm and using CLIP score to select candidate important data are proposed. Finally, the proposed method (i.e., DAS) achieves better linear datamodeling scores than existing attribution methods.

### Strengths
- This paper addresses the gap left by Zheng et al. (2024) and demonstrates why the simple diffusion loss is not an appropriate model output function for TRAK-based methods (Equation 8).
- The proposed, theoretically more principled method DAS actually leads to improved linear datamodeling scores.
- This paper proposes to reduce the number of candidate training samples for computing data attribution scores, using CLIP score as the criterion. This approach can significantly improve computational efficiency and is shown to work fine (Table 7).

References
- Zheng et al. (2024) - Intriguing properties of data attribution on diffusion models.

### Weaknesses
 - Although the paper shows that $L_{\text{simple}}$ is not an appropriate model output function, it is not directly shown why $L_{\text{Square}}$, as proposed in Zheng et al. (2024), is more appropriate. Specifically, Equations (9) and (10) are not exactly equivalent. In this sense, this paper does not fully explain the intriguing findings in Zheng et al. (2024). A more direct theoretical comparison between Equations (9) and (10) would make the contribution greater.

- In lines 153-155 and Equation (7), the paper states that D-TRAK uses the simple loss $L_{\text{simple}}$ as the output function. However, the main experimental results from Zheng et al. (2024) come from D-TRAK implemented with $L_{\text{Square}}$ as the output. This mismatch in writing needs to be resolved.

- Quantitative results are missing in the experiment where the top 1,000 positive influential samples are removed. Something like the counterfactual evaluation in Zheng et al. (2024) would suffice.


### Questions
- How does Equation (9) validate the effectiveness of Equation (10) in comparison to the ineffectiveness of Equation (7)?
- Why do you think $\lambda$ has such a big impact on the performance of DAS (shown in Figure 4)? How is $\lambda$ tuned for CelebA and ArtBench?
- In the proof for applying Newton's Method, it is assumed that $\theta^*$ is a global optimum. Can you explain why this assumption is reasonable for diffusion models?
- Since Newton's Method can be applied to approximate $\theta^*_{\setminus i}$, why can't we used the approximated $\theta^*_{\setminus i}$ in Equation (9)? This way we don't need to linearize $f_{\text{DAS}}$.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel metric called Diffusion Attribution Score (DAS) to more accurately quantify the attribution of training samples to generated images. While the paper is tackling an important problem of accurate data attribution for diffusion models, it has areas for improvement, such as justification of their proposed and more rigorous evaluation of the method as described below.

### Strengths
- The paper addresses the important problem of attributing diffusion models’ output to training samples.
- The metrics in quantitative evaluation look good, all showing significant gaps accounting for the confidence interval or standard deviation (though further clarity on these intervals would be helpful as they are not noted).

### Weaknesses
 - The equations in Section 3.1 only show that DAS is independent of data distribution, unlike D-TRAK. However, it has not been shown how significant it is. While DAS seems to be working well in the experiment results, the theory behind it appears weak.
- The evaluation solely relies on the LDS metric, which is based on the strong assumption of additive data contributions. There have been discussions on the effectiveness of LDS for evaluating data attribution algorithms, such as https://arxiv.org/abs/2409.18153 Adding other metrics or justifying its use looks necessary.
- In Figure 1, diffusion model outputs from the same random seeds are presented. The rationale behind the comparison seems to be that the same random seed should lead to a similar output when models are trained on datasets of similar distribution. However, this may not be true since models are retrained, and they are essentially different ones. How can you ensure that two diffusion models trained on the same dataset generate the same output for a random seed when other randomness, such as batch sampling, is not controlled?

### Questions
- Could you please clarify the theoretical benefits of DAS over D-TRAK?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors introduce the Diffusion Attribution Score (DAS) to address limitations found in D-TRAK, a data attribution method for diffusion models. This is a timely and surprisingly under-explored task: While data attribution task (AKA data valuation), which strives to assess training samples' impact on trained model's predictions, has a long history - only recently methods for diffusion models emerged, motivated by the timely copyrights issues that such models present. The previous method D-TRAK approximates comparisons between prediction loss of diffusion models trained with and without specific training samples. However, the authors argue that the reliance on diffusion loss leads to indirect comparisons, and hypothesize that this indirect approach does not accurately capture the influence of training samples on model outputs. To overcome this, they propose DAS, which approximates a direct comparison. As demonstrated in thorough evaluations, this approach indeed provides more precise data attribution scores, when compared to D-TRAK and other baselines.

### Strengths
1. The authors picked up on the counterintuitive finding of D-TRAK that switching loss functions in their method, to a loss that is not used during training, increases attribution correctness. Though D-TRAK proposed an explanation, I personally share the author’s belief that this finding calls for further exploration (in my view D-TRAK's explanation requires further substantiation in itself). 

2. The authors provide a significant observation: D-TRAK’s attribution scores, as expressed in Eq. (7), do not directly compare (approximate) predictions with/ without training samples. I agree with this found limitation.

3. They propose to derive attribution formulas, that fall within the TRAK methodology, but starting from a direct comparison between the predictions (Eqs. 9). This original paradigm not only solves the newfound limitation, but also sheds light on the counterintuitive finding of D-TRAK: L_square does indeed differ from L_simple by providing a direct comparison of the predictions (Eq. 10).

4. Sufficient performance experiments: The authors demonstrate that DAS indeed outperforms D-TRAK (and several other baselines) across four datasets, and in several settings. Evaluations are in terms of LDS - a widely accepted choice in evaluating TRAK-based methods. Ontop of being appropriate, it is also extensive as it requires multiple training.

### Weaknesses
 1. The paper lacks a "Previous Work" section—a significant omission, as it currently mentions only one attribution method for diffusion models (D-TRAK) in the introduction. The authors appear to have overlooked other relevant approaches, such as [1], [2], and [3], which should be acknowledged, even if not necessarily included in direct comparisons. Acknowledging these methods is especially important, given that this domain is still underexplored, and the current structure of the paper will give researchers a misleading impression that only gradient-based methods are available. Additionally, key baselines like Journey TRAK, TracInCP and others are introduced in the evaluation tables without prior context - an earlier introduction would clarify their relevance.

 2. The mathematical claims lack direct verification through numerical experiments or even qualitative examples, and the improved performance alone is too indirect to serve as convincing validation  **[Edit: i.e. better LDS scores against competitors on standard benchmarks is not enough to substantiate the mathematical claims]**. With that said, given that it is common practice in ML to present mathematical derivations and substantiate them only via improved performance, this is not a critical flaw in terms of acceptance. However, it would significantly improve the impact if such experiments were added - here is a possible idea (other convincing experiments can work as well): Find cases where DAS succeeds and D-TRAK fails, and show that D-TRAK is indeed limited by its indirect comparisons (Sec. 3.1), where DAS solves this. 

### Questions
Please refer to weaknesses

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
The paper introduces a new data attribution method called "Diffusion Attribution Score (DAS)" to quantify the influence of training samples in diffusion models, specifically addressing the challenges of data attribution in generative tasks. Experimental results demonstrate that DAS achieves state-of-the-art performance in LDS across various datasets and diffusion models, with strategies explored to accelerate DAS computation for large-scale models.

### Strengths
1. Compared to previous work, the proposed DAS method shows significant improvements in experimental results.
2. The article provides anonymized source code, demonstrating the reproducibility of the proposed approach.
3. The data attribution problem in diffusion models studied in this paper is meaningful.

### Weaknesses
1. The author mentions "these approaches measure the divergence between predicted and ground truth distributions, which leads to an indirect comparison between the predicted distributions and cannot represent the variances between model behaviors." and provides a brief explanation in Section 3.1. However, as an important argument of the paper, the vague explanation given in lines 178–180 is insufficient to convincingly illustrate the shortcomings of previous work. Specifically, the argument that comparing predicted and ground truth distributions is 'indirect' needs more elaboration. It's unclear why measuring the divergence between these distributions inherently fails to capture the nuances of model behavior. A more detailed explanation, perhaps with a concrete example, would strengthen this claim. For instance, how does a direct comparison of model distributions, as proposed by DAS, better capture the impact of a training sample compared to methods that consider the ground truth distribution?
2. Similar to W1, lines 191–194 lack adequate support, whether theoretical justification, appropriate citations, or experimental evidence. The claim that treating the model output as a scalar, rather than a vector in latent space, introduces a significant error requires more rigorous justification. The authors should provide a more detailed explanation of the mathematical implications of this simplification, perhaps by showing how the inner product term, which is omitted in the scalar approach, contributes to a more accurate attribution score. A theoretical derivation or a toy example could help illustrate the magnitude of the error introduced by this simplification.
3. The logical connection from Sections 3.2 to 3.3 is unclear. The motivation for each sub-module, the problems they aim to solve, and why the proposed methods were chosen are not explained. Additionally, the theoretical proof follows similar derivations as [1] without clearly explaining the motivation behind each step, making it difficult to follow the authors' reasoning. The paper should clearly articulate the purpose of each step in the derivation, explaining why a Taylor expansion is used, and why Newton's method is employed to approximate the model parameter difference. Furthermore, the connection between the theoretical derivation and the practical implementation in Section 3.3 needs to be more explicit. It's not clear how the dimensionality reduction and the reduction in sampled timesteps and training samples directly address the computational challenges highlighted in Section 3.2.

### Questions
Please refer to the Weakness

### Soundness
3

### Presentation
3

### Contribution
3
