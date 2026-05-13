# AITTI: Learning Adaptive Inclusive Token for Text-to-Image Generation

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Despite the high-quality results of text-to-image generation, stereotypical biases have been spotted in their generated contents, compromising the fairness of generative models. 
  In this work, we propose to learn \textit{adaptive inclusive tokens} to shift the attribute distribution of the final generative outputs. 
  Unlike existing de-biasing approaches, our method requires neither explicit attribute specification nor prior knowledge of the bias distribution. 
  Specifically, the core of our method is a lightweight \textit{adaptive mapping network}, which can customize the inclusive tokens for the concepts to be de-biased, making the tokens \textit{generalizable to unseen concepts} regardless of their original bias distributions.
  This is achieved by tuning the adaptive mapping network with a handful of balanced and inclusive samples using an anchor loss.
  Experimental results demonstrate that our method outperforms previous bias mitigation methods without attribute specification while preserving the alignment between generative results and text descriptions. Moreover, our method achieves comparable performance to models that require specific attributes or editing directions for generation. Extensive experiments showcase the effectiveness of our adaptive inclusive tokens in mitigating stereotypical bias in text-to-image generation.
  \keywords{Fairness \and Bias Mitigation \and Generative Model}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on addressing the bias problem in current T2I models. To tackle this, the authors introduce a prompt-tuning approach based on an adaptive mapping network and anchor loss. Experimental results demonstrate its effectiveness in mitigating gender, race, and age biases.

### Strengths
1. The paper focuses on addressing the bias problem in current T2I models, particularly gender, race, and age biases, which has important social benefits.

2. The proposed method is simple yet model-agnostic, as stated by the authors, and can be easily adopted in existing approaches to help reduce bias issues.

3. Extensive experiments were conducted to evaluate the effectiveness of the proposed method in mitigating biases.

### Weaknesses
1. The biases present in current T2I models are not primarily due to the models themselves but stem from other non-technical issues, such as dataset limitations or unclear prompts. Additionally, for evaluation, the authors use a CLIP zero-shot classifier to classify sensitive attributes. However, since CLIP is likely trained on biased datasets, the classifier may more accurately identify attributes that are highly frequent in its training data, which could, in turn, affect the accuracy of evaluation results.

2. From the quantitative comparison shown in Table 1 and the qualitative results, the proposed method does not show significant improvement over other methods, particularly FM, in addressing different biases. As discussed in the paper, the proposed method is model-agnostic—can it enhance the performance of other methods?

3. What are the experimental settings for Figure 1(a)? More details are needed to illustrate the bias problems present in current T2I models.

4. I am confused about the ablation studies shown in Table 2. What is the setting for without adaptive mapping network? Without AM, how is the anchor loss in Eq. (2) calculated?

### Questions
See above weaknesses.

### Soundness
3

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
This pape addresses the critical issue of stereotype bias in text-to-image generation models. The authors propose an innovative method that adjusts the attribute distribution of the final generated output by learning adaptive inclusive tokens. This approach does not require explicit specification of attributes or prior knowledge of bias distribution. Instead, it customizes concept-specific inclusive tokens through a lightweight adaptive mapping network. The method introduces an anchoring loss to constrain the influence of adaptive inclusive tokens on the final output, thereby enhancing the fairness and inclusivity of the generated results without compromising the consistency between the text and the generated images.

### Strengths
The paper introduces a novel approach by using adaptive inclusive tokens to mitigate bias in text-to-image generation models without the need for explicit attribute specification or prior knowledge of bias distribution, sounds interesting.

Experimental results demonstrate that the proposed method outperforms previous bias mitigation techniques in scenarios without attribute specification. 

The method seems generalizes well and this paper is easy to read.

### Weaknesses
Potential Introduction of Factual Errors: The proposed method may introduce factual inaccuracies when dealing with non-neutral concepts. For example, generating an image of a female U.S. president, which does not align with historical facts. The authors do not discuss or evaluate the conflict between accuracy and fairness in their approach.

Lack of Motivation and Theoretical Foundation: The adaptive mapping network proposed by the authors lacks a clear motivation and theoretical discussion. This makes it difficult to understand the underlying principles and rationale behind the approach.

Implementation Details: While the paper outlines the overall framework of the method, the description of the implementation is vague, particularly regarding the specific structure and training process of the adaptive mapping network. The diagrams provided are unclear and fail to effectively convey the authors' intentions.

Quality of Generated Models: There is a lack of effective discussion and comparison regarding the quality of the generated models. The impact of the prompts, models, and data volume on the final model is not adequately addressed.

Limited Experimental Setup: The experimental setup is relatively limited, especially in terms of evaluating performance in complex scenarios and across different datasets. This restricts the understanding of the method's robustness and applicability.

Practical Application Value: The paper lacks a discussion on the practical application value of the proposed method. It is unclear how the generated images can be ensured to be both fair and factually accurate.

### Questions
Provide a deeper exploration of the theoretical foundation and motivation behind the adaptive mapping network and anchor loss. Discuss how these components compare to existing bias mitigation techniques.

Include a more detailed description of the structure and training process of the adaptive mapping network in the paper. This will help other researchers better understand and replicate the method.

Enhance the clarity and readability of the figures and diagrams in the paper to effectively convey the authors' intentions.

Increase the number of experiments in complex scenarios. Discuss the impact of fairness on accuracy and how to mitigate such issues.

Provide some practical application cases to demonstrate the effectiveness and potential challenges of the method in real-world scenarios. This will help readers better understand the practical application value of the method.

### Soundness
3

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
4

### Summary
The paper presents a novel approach to mitigate stereotypical biases in text-to-image (T2I) generation models. The authors introduce a method for learning adaptive inclusive tokens that can adjust the attribute distribution of the generated images to be more equitable, without the need for explicit attribute specification or prior knowledge of the bias distribution. The core of their approach is a lightweight adaptive mapping network that customizes inclusive tokens for concepts that are targeted for de-biasing, which enhances the generalizability of the tokens to new, unseen concepts. The method is evaluated on the Stable Diffusion framework and demonstrates improved performance over existing bias mitigation techniques, showing its effectiveness in reducing stereotypical biases in T2I generation.

### Strengths
1. The paper introduces a novel method for reducing biases in text-to-image generation, which is critical to AI ethics and fairness. The concept of learning adaptive inclusive tokens that can shift attribute distributions in generative outputs is a creative solution.
2. The method's ability to generalize to unseen concepts and handle multiple attributes is a major advantage, showcasing its potential for broad application across various domains.

### Weaknesses
1. While the authors claim to have developed a lightweight adaptive mapping network to address bias mitigation, the training time of nearly one hour suggests that it may not be as lightweight as initially proposed. This process raises concerns about the practicality and efficiency of the solution, especially in contexts where rapid deployment or real-time adjustments are required.
2. While the authors demonstrate quantitative improvements over the baseline in comparative analysis, the qualitative examples presented in the supplementary material show that the method is not entirely effective, with many prompts still generating images with a predominantly single gender. This inconsistency between quantitative and qualitative results casts doubt on the overall effectiveness of the method and its ability to achieve the desired inclusiveness in text-to-image generation.
3. Overall, I think the authors' approach of training to shift certain biased concepts towards less ambiguous representations using a better mapping network, akin to a new token, is quite straightforward. However, as mentioned earlier, I am concerned about whether such a simple method can be truly effective.

### Questions
1. The main metric $D_{kl}$ for attribute distribution demonstrates that the original SD1.5 outperforms SD2.1 and SDXL (SD1.5>SD2.1>SDXL). This is not consistent with the qualitative results. Does it mean the metric there is a problem with the metric itself?
 2. Why does a single token perform better than multiple tokens (with higher complexity)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a bias mitigation approach for T2I generation using adaptive inclusive tokens, enhancing fairness without needing attribute specifications. By employing an adaptive mapping network and anchor loss, the approach effectively mitigates biases while maintaining quality and text alignment. The method is versatile but has limitations when handling non-neutral concepts and potential semantic drift.

### Strengths
1. The paper is well-written and reads clearly.
2. Learning an adaptive mapping network to generate inclusive tokens specific to different occupation is reasonable and justified.
3. Experimental results effectively demonstrate the method’s effectiveness.

### Weaknesses
1. Calculating anchor loss requires predefined information on non-dominant bias attributes for each occupation in the training data, which necessitates human pre-determination.
2. The paper primarily focuses on biases introduced by the text encoder and does not examine potential biases inherent to the diffusion model itself. However, text embedding may be attacked[1]. The proposed method may become ineffective after being attacked.
3. The reported FID metric is in the range of 200–300, whereas this metric usually falls within the magnitude of 10^1. This discrepancy may result from insufficient statistical sampling, casting doubt on whether FID accurately reflects image quality here. ImageReward [2] or PickScore [3] might be fairer metrics in this context.
4. The method's reliance on the text encoder introduces a potential vulnerability: if the text encoder itself is biased or manipulated, the mitigation strategy might not be effective. Furthermore, the paper does not explore the impact of using different text encoders, which could significantly influence the results. The method's effectiveness is therefore tied to the specific text encoder used, limiting its generalizability.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
