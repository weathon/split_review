# Towards Black-Box Membership Inference Attack for Diffusion Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Given the rising popularity of AI-generated art and the associated copyright concerns, identifying whether an artwork was used to train a diffusion model is an important research topic.
The work approaches this problem from the membership inference attack (MIA) perspective. We first identify the limitation of applying existing MIA methods for proprietary diffusion models: the required access of internal U-nets.
To address the above problem, we introduce a novel membership inference attack method that uses only the image-to-image variation API and operates without access to the model's internal U-net. Our method is based on the intuition that the model can more easily obtain an unbiased noise prediction estimate for images from the training set. By applying the API multiple times to the target image, averaging the outputs, and comparing the result to the original image, our approach can classify whether a sample was part of the training set. We validate our method using DDIM and Stable Diffusion setups and further extend both our approach and existing algorithms to the Diffusion Transformer architecture. Our experimental results consistently outperform previous methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To provide protection for the artworks and detect misuse of data, this paper proposes a black-box membership inference attack for diffusion models used in image generation. It first gives a brief introduction to popular diffusion models. Then it introduces the black-box MIA method based on the variation API. The core idea of the method is based on the hypothesis that images used in the training set typically result in smaller reconstruction errors compared to images not in the training set. Experiments are conducted on several datasets, followed by further ablation studies and an application in a real-world setting.

### Strengths
1. This paper introduces a novel black-box MIA method that merely requires access to variation API, which makes it more practical and easy to perform.

2. The core idea of the proposed method is intuitive and effective, as demonstrated through both theoretical and experimental results.

3. The experiments are comprehensive. The proposed method is applied to three diffusion models and experiments are conducted on multiple datasets. Also, further ablation study for several key hyper-parameters and real application to DALL-E’s API are conducted.

### Weaknesses
1. The written of this paper can be further improved. The motivation discussed in Introduction is not solid enough in my opinion.

2. Although many experiments are conducted, the analysis to the results is insufficient. For example, in Table 1, the TP value of REDOFFUSE on CIFAR-10 is much lower than others, while no analysis is provided. Also, there is a lack of analysis on why longer diffusion steps, an important factor affecting performance, seriously degrade the results. Potential solutions for this issue should also be discussed.

3. More cases should be provided to analyze the differences between member and non-member samples. But there is only one case in Sec.6.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel membership inference attack method that uses only the image-to-image variation API and
operates without access to the underlying model. The experimental results suggest that the model offers a significant boost over prior works.

### Strengths
- Clear and intuitive method. As someone who does not directly work on membership inference problems, the proposed methodology makes a lot of sense. I am not able to judge if prior works have proposed a similar idea before.
- The paper provides a good theoretical analysis of the effectiveness of the proposed method.
- The performance boost over prior works seems to be quite significant.

### Weaknesses
 - The paper should better discuss the connections between the proposed idea and prior works. For example, have relevant ideas been proposed in other types of membership inference attack methods?
- The abstract is too brief. The paper could benefit from elaborating the abstract with more insights of the proposed method and the key experimental results.
- Table 4 is vague, how to interpret the L1 and L2 distance as membership inference accuracy?


### Questions
- Since the proposed idea is quite intuitive, have relevant ideas been proposed in other types of membership inference attack methods?
- Table 4 is vague, how to interpret the L1 and L2 distance as membership inference accuracy? 
- In general, is there a way to provide any confidence to the membership inference results? After all, any mistake could lead to wrong accuse for the diffusion API.

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
This paper introduces a new membership inference attack method for diffusion models. Unlike previous approaches that require direct access to the U-Net component within the diffusion model, this method only needs access to the model’s variation API. Extensive experiments demonstrate the effectiveness of the proposed approach.

### Strengths
Strength:
1. The paper is well written and easy to follow.

2. The paper considers a broad range of model types, including DDIM, Stable Diffusion, and Diffusion Transformers and the proposed method performs well across different models.

3. The paper provides theoretical justification for the proposed method.

### Weaknesses
1. **Practicality of the Scenario**: The paper assumes that the variation API allows users to conduct denoising by querying the model with noisy images and receiving denoised outputs. However, in most real-world APIs for diffusion models (e.g., Stable Diffusion 3 API [1]), users typically only have access to final generated images and cannot query intermediate denoising stages. Therefore, while the proposed attack method does not require model parameter access, it may not be feasible for API-only models. If there are any API-only models with accessible variation APIs, it would be helpful if the authors could provide references to these in the rebuttal. It is crucial to clarify the specific types of variation APIs that would enable this attack, as the current description is too broad and may not reflect the reality of most deployed diffusion model APIs.

2. **Lack of a Comparison of Computational Requirements**: As mentioned in Weakness 1, although the paper suggests that the method can operate in a black-box setting, its reliance on denoising queries rather than direct image generation could limit its applicability similarly to “white-box” approaches. Therefore, it is reasonable and necessary to have more comparison, particularly of computational resource requirements, because it seems that the proposed method may require more computational resources compared with the baselines. The paper should provide a detailed analysis of the number of denoising queries required for a successful attack and compare this to the computational cost of other membership inference attacks. This analysis should include the time complexity and memory requirements, making it easier to assess the practical feasibility of the proposed method.

3. **Clarity of Algorithm Explanation**: The intuition behind the proposed algorithm in Section 4.2 is not clear enough. The statement, “If the noise prediction from the neural network exhibited high bias, the network could adjust to fit the bias term, further reducing the training loss,” is ambiguous. What specifically is meant by “bias” here, and why does this lead to the condition $ \nabla_\theta L(\theta) = 0$ for a well-trained model? While the method itself is intuitive, a more thorough explanation in this section would improve clarity. The paper needs to explicitly define the bias term in the context of diffusion models and explain how it relates to the gradient of the loss function. A more detailed mathematical explanation, perhaps including a derivation, would be beneficial.

### Questions
1. Can the proposed method further generalize to fine-tuning of diffusion models?

2. Although the DDIM model is widely used and much more effective than DDPM, can you still provide some results regarding the performance in DDPM?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This article explores the limitations of SOTA methods in addressing the significant problem of identifying whether an artwork has been used to train a diffusion model, i.e., the required access of internal U-nets. To this end, this paper proposes a new membership inference attack method that is based on an image-to-image transformation API without accessing to the model's internal U-net. The experimental results reflect the effectiveness of this method to some extent.

### Strengths
-This article aims to identify whether an artwork was used to train a diffusion model without accessing to the model's internal U-net, which is an Interesting and relevant topic that fits within the scope of the conference.
- Novelty. The article proposes a novel membership inference attack method based on an image-to-image transformation API.
- The author(s) performed several experiments, and try to validate the effectiveness of the proposed method.

### Weaknesses
 - A certain part of experimental results reveal that the proposed method can only achieve very limited improvements over the existing SOTA methods. For example, as shown in Table 1, the proposed method only improves by about 1-3% on most metrics, and even performs worse than the SOTA method PIAN on the TP metric for CIFAR10. Unfortunately, the authors did not discuss or explain this in the paper. Therefore, the effectiveness of the proposed method is questionable.
-The organization of this paper lacks clarity. The author does not clarify why it is difficult to implement MIA without access to the internal U-net, what challenges will be encountered, and how the author effectively addresses these challenges. Without this crucial information, it is difficult to evaluate the significance of the authors’ work.
- The organization of this paper is poor. In the ablation experiments, the author attempts to test the impact of experimental parameters on the robustness of the algorithm; however, the evaluation metric is one-sided (i.e., only AUC). Hence, the experiment results are therefore difficult to be convincing. While we note that the author seems to provide more contents in the appendix, but these contents exceed the page limits of the paper and should not be considered.
- The application experiments may have biases, as the author only conducts the evaluations on a single model (DALL-E) and relies on a small dataset (i.e., only 30 famous paintings and 30 generated paintings). Hence, the experiment results are therefore difficult to be convincing. Without comprehensive experiments, the effectiveness of the proposed methods cannot be validly verified.

The paper requires an in-depth editorial review. The authors are recommended to examine structure, argumentation, and language clarity to ensure the paper meets high-quality standards. For example, the equation numbering in the paper is chaotic, and the format of Algorithm 1 lacks indentation

### Questions
-Could authors provide more detailed discussion or explanation on the experiemnt results precented in Table 1?
-Could authors clarify the challenges that will be encountered while implementing MIA without accessing to the internal U-net, as well as how the author effectively addresses these challenges?

### Soundness
2

### Presentation
2

### Contribution
3
