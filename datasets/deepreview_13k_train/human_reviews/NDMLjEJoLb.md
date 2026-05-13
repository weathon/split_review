# Blending Concepts in Text-to-Image Diffusion Models using the Black Scholes Algorithm

- Decision: Reject
- Scores: 5, 3, 8, 3

## Abstract
Many image generation tasks, such as content creation, editing, personalization, and zero-shot generation, require generating unseen concepts without retraining the model or collecting additional data. These tasks often involve blending existing concepts by conditioning the diffusion model with text prompts at each denoising step, a process known as ``prompt mixing''. We introduce a novel approach for prompt mixing to forecasts predictions w.r.t. the generated image and makes informed text conditioning decisions at each time step during diffusion denoising. To do so, we leverage the connection between diffusion models (rooted in non-equilibrium thermodynamics) and the Black-Scholes model for pricing options in Finance, and draw analogies between the variables in both contexts to derive an appropriate algorithm for prompt mixing using the Black Scholes model. Specifically, the parallels between diffusion models and the Black-Scholes model enable us to leverage properties related to the dynamics of the Markovian model derived in the Black-Scholes algorithm. Our prompt-mixing algorithm is data-efficient, meaning it does not need additional training.  Furthermore, it operates without human intervention or hyperparameter tuning. We highlight the benefits of our approach by comparing it, qualitatively and quantitatively using CLIP scores, to other prompt mixing techniques, including linear interpolation, alternating prompts, step-wise prompt switching, and CLIP-guided prompt selection across various scenarios such as single object per text prompt, multiple objects per text prompt and objects against backgrounds. The resulting code will be made publicly available for research reproduction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an approach to enhance prompt mixing in diffusion models. It leverages the concepts from the Black-Scholes algorithm used in financial markets. The authors analyze the relationship between diffusion models and the Black-Scholes model. It uses the connect to develop a method to select optimal text prompts during the denoising process. The method aims to generate images that effectively blend multiple concepts without requiring additional training or data collection. Experimental results indicate that the proposed method outperforms baselines in both CLIP scores and qualitative comparisons across various settings.

### Strengths
1. Novel conceptual connection: The paper makes an interesting theoretical connection between diffusion models and the Black-Scholes algorithm. It provides a new perspective on prompt mixing.

2. No additional training: The proposed method is data-efficient and requires no additional training or fine-tuning of the underlying diffusion model.

3. Comprehensive evaluation: The authors test their approach across multiple experimental settings with varying complexity and provide both qualitative and quantitative comparisons.

### Weaknesses
1. Weak theoretical foundation: While the paper tries to connect diffusion models with Black-Scholes, the connection is inadequately justified. The authors fail to rigorously demonstrate why the financial markets in the Black-Scholes model should apply to image generation. The mapping of concepts like "strike price" and "risk-free rate" to the image generation domain seems not very straightforward and intuitive. Specifically, the paper lacks a clear explanation of how the stochastic differential equations (SDEs) underlying both diffusion models and the Black-Scholes model are related, and how the assumptions of the Black-Scholes model (e.g., efficient markets, log-normal price distributions) translate to the latent space of diffusion models. The analogy feels superficial without a deeper mathematical justification.

2. Limited evaluation metrics: The paper relies heavily on CLIP scores for quantitative evaluation. However, CLIP scores is not the optimal evaluation strategy due to their vulnerability to hallucination and bias issues. More robust evaluation metrics should be given to validate the proposed method. Besides, the improvement of CLIP score is also minimal. The paper should consider metrics that assess the quality of the generated images beyond text alignment, such as measures of image diversity, fidelity to individual concepts, and the absence of artifacts. Relying solely on CLIP scores makes it difficult to assess the practical utility of the proposed method.

3. Insufficient ablation studies: The ablation studies to justify the specific choices made in adapting the Black-Scholes model are not given. For instance, the authors set the strike price K to a constant value of 0.25 without exploring how different values might affect the results. Similarly, the choice of risk-free rate as 1/T is not adequately explained or validated through experiments. The paper should include a sensitivity analysis of these parameters to demonstrate the robustness of the method and to provide a better understanding of their impact on the final results. The lack of ablation studies makes it difficult to understand the contribution of each component of the proposed method.

### Questions
1. Could the authors provide a more rigorous mathematical justification for why the market behavior should apply to the image generation domain? 
2. What is the computational cost of computing Black-Scholes scores at each step?
3. How is the result with more than two prompts?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work uses the Black Scholes algorithm to generate images with concatenated prompts. The core idea is to evaluate the effect of the intermediate latents on the final latent by evaluating the CLIP similarity score. Qualitative analysis compare the approach with that of vanilla SD, alternate sampling, Linear Interpolation,  Step-switching techniques.

### Strengths
+ The work utilizes the Black Scholes algorithm to combine two prompts for style blending. 
+ Qualitative analysis show that the approach can blend two prompts to generate images. 
+ The proposed approach is data efficient.

### Weaknesses
 - The number of steps needed for blending is not clear, the associated computational overhead is not discussed. How does the approach compare to competing approaches in terms of computational time?
- The results are limited to two prompts and limited qualitative results are presented. The quantitative results as in prior work eg, Chefer et al,
- The claim that average CLIP similarity is 0.25 is not correct. The average CLIP score is generally close to 0.34, see Fig 8  in Chefer et. al.
- The experimental setup is not clear. What dataset and size is considered for evaluation in Table 1.
-  Results are limited to single objects and comparison to recent work for style blending is limited. For example, there are many works which have not been compared to [a, b, c, d].

### Questions
- The approach is limited to two prompts. How does it scale with different number of prompts?
- Evaluation benchmarks such as [a1] could have been considered for quantitative analysis.
[a1] T2i-compbench: A comprehensive benchmark for open-world compositional text-to-image generation
- How does the method perform in multi-subject scenarios? 
- Does the order of prompts effect the blending of concepts? Stable diffusion is sensitive to concept ordering, how does this extend to the proposed approach.
- Also see weaknesses above for the questions.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the challenge of generating new concepts in image generation tasks without retraining the model or collecting additional data. The authors propose a novel "prompt mixing" technique that guides text conditioning at each diffusion step by forecasting predictions about the generated image. Drawing on the connection between diffusion models and the Black-Scholes model in finance, the approach derives a data-efficient prompt-mixing algorithm that requires no additional training or human intervention. The method is compared qualitatively and quantitatively against other prompt mixing methods across various scenarios, demonstrating its effectiveness.

### Strengths
- The paper presents an innovative method for prompt mixing in text-to-image diffusion models by integrating the Black-Scholes algorithm, a concept from financial modeling, offering a fresh interdisciplinary approach to enhance image generation tasks.
- This method is data-efficient, requiring no additional training or data collection.
- It dynamically selects the most relevant text prompt at each diffusion step, minimizing the need for human intervention and hyperparameter adjustments.
- Qualitative and quantitative comparisons using CLIP scores highlight the method's advantages over existing techniques, including vanilla stable diffusion, linear interpolation, alternating prompts, and step-wise switching.
- The paper thoroughly analyzes performance across diverse scenarios (single objects, multiple objects, and objects with backgrounds) demonstrating the method's versatility.

### Weaknesses
 - The paper relies heavily on CLIP scores for quantitative evaluation. ​ While CLIP scores are widely used, they may not always capture the fine-grained details and quality differences in generated images. ​ The authors acknowledge this limitation and suggest exploring more advanced image-language models for evaluation in future work. ​
- The study focuses on prompt mixing with two prompts. ​ The impact of using more than two prompts is not explored. ​
- The use of financial concepts (i.e., the Black-Scholes algorithm) may be challenging for readers without a background in finance, potentially limiting the accessibility of the paper.

### Questions
- The paper acknowledges the limitations of relying on CLIP scores for evaluation, yet it lacks alternative metrics or a deeper analysis of how these limitations may affect the interpretation of the results.
- Incorporating additional evaluation metrics, such as human evaluations or perceptual quality scores, would enhance the assessment and provide a more comprehensive view of the generated images.
- Although the paper mentions image generation time, a more detailed breakdown of computational resource requirements, such as GPU hours and memory usage, would be informative.
- Information on the method’s scalability with larger models or handling of more complex prompts would be valuable for understanding its broader applicability.
- A more in-depth explanation of how the Black-Scholes model's assumptions apply within the diffusion model context would strengthen the theoretical foundation.
- Providing specific details about the parameter settings used in the experiments, such as values for diffusion schedule hyperparameters, would improve the reproducibility of the study.

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
5

### Summary
The authors claim that the Black-Scholes fiance price options model is similar to the diffusion model. Based on this, the authors introduce a novel approach for prompt mixing which can be explained as mixing the prompt with the highest scores measured by CLIP during each denoising step. The authors claim their method is data-efficient, requiring no additional training and operates without human intervention or hyperparameter tuning. To validate the effectiveness of the method, the authors only use CLIP score under the scenario of mixing only two prompts.

### Strengths
From my perspective, the strengths of this paper mainly lie in:

1. introduce the Black-Scholes model into diffusion models.

2. the only one experiment to validate the performance across the whole paper.

### Weaknesses
From my perspective, the strengths of this paper mainly lie in:

1. introduce the Black-Scholes model into diffusion models.

2. the only one experiment to validate the performance across the whole paper.

I appreciate the authors' efforts. From my perspective, $\textbf{significant revisions are necessary}$, including the addition of substantial content and a reorganization of the structure. Therefore, $\textbf{I lean towards recommending the rejection of this paper}$.

Presentation(I only list several parts):

1. Frankly speaking, the organization, the writing and the format of this paper are awful. It is difficult for the reviewers to understand the authors` motivation and so on. The cite format of this paper is totally wrong. $\textbf{The authors make the wrong utilization of \citep{} and \citet{}}$, which can lead to desk reject of this paper.

2. The content of the article is somewhat disorganized. When introducing the proposed method, the authors abruptly shift to discussing related work. I believe this section should have been addressed earlier in the text.

3. Grammar mistakes and missing references.  In line 167, "$\textit{determine the price of European call options of assets. which is used to determine the price of European call options on assets}$". Wrong commas and repeated sentences.  The authors only use the CLIP score to evaluate the effectiveness of the proposed method, but no reference to the CLIP score.

Method and Experiments:

1. The proposed method is not novel, it just directly introduces the Black-Scholes model in fiance into diffusion models. The core of the proposed method is to select the optimal prompt to mix during each denoising step. The authors claim the difference between the proposed method and previous ones is the proposed method can connect to the dynamics of the diffusion denoising process. However, there is no evidence to show the superiority of the connection to the dynamics of the diffusion denoising process.

2. In the conclusion part, the authors acknowledge the limitations of their method; however, I believe these issues must be addressed. First, the experimental section utilizes $\textbf{only one evaluation metric and one diffusion model}$, resulting in a single experiment throughout the paper. This makes it difficult to validate the effectiveness of the proposed method. Furthermore, the intuitive results provided do not demonstrate any significant changes. Second, the authors state that $\textbf{the method is currently applicable only to mixing two prompts}$, which clearly does not establish the method's scalability. Additionally, the pseudocode provided indicates that the time complexity of the proposed method approaches $O(n^2)$, raising doubts about its efficiency.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
