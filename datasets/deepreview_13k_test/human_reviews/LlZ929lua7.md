# Seeing the Unseen: How EMoE Unveils Bias in Text-to-Image Diffusion Models

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Estimating uncertainty in text-to-image diffusion models is challenging due to their large parameter counts (often exceeding 100 million) and operation in complex, high-dimensional spaces with virtually infinite input possibilities. In this paper, we propose EMoE, a novel framework for efficiently estimating epistemic uncertainty in diffusion models. EMoE leverages pre-trained networks without requiring additional training, enabling direct uncertainty estimation from a prompt. We introduce a novel latent space within the diffusion process that captures model uncertainty better during the first denoising step than existing methods. Experimental results on the COCO dataset demonstrate EMoE's effectiveness, showing a strong correlation between uncertainty and image quality. Additionally, EMoE identifies under-sampled languages and regions with higher uncertainty, revealing hidden biases related to linguistic representation. This capability demonstrates the relevance of EMoE as a tool for addressing fairness and accountability in AI-generated content.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an Epistemic Mixture of Experts (EMoE), a framework that efficiently estimates epistemic uncertainty without additional training by leveraging pre-trained networks. EMoE operates within the latent space in the diffusion process, capturing uncertainty early in the denoising phase. The authors demonstrate the results on the COCO dataset, where the alignment of uncertainty estimates with image quality is chosen as the evaluation criteria. This work also claims to identify biases, such as under-represented languages and regions.

### Strengths
- The authors address a significant and well-explored challenge: uncertainty quantification in text-to-image diffusion models.
- The proposed use of EMoE for uncertainty quantification is straightforward and offers clear interpretability.
- The authors present a methodology for integrating the MOE network into text-to-image diffusion models to quantify epistemic uncertainty.
- The literature review is comprehensive, effectively situating the work within the context of existing research.

### Weaknesses
- The core component of this work is the Mixture of Experts (MOE) network, a well-established method for uncertainty quantification, as demonstrated in previous studies [1,2,3]. This reliance on a pre-existing approach may limit the perceived novelty of this work, as it may appear to simply adapt a plug-and-play method to diffusion models without substantial innovation.

- The authors rely solely on the CLIP score to evaluate their model’s performance, which may raise issues since CLIP has known biases. For example, CLIP often correlates “man” more strongly with “woman” than with “boy,” suggesting potential misalignment with accurate demographic representation. Refer to [4] for additional details on CLIP’s limitations in bias.

- Epistemic uncertainty, a primary focus of this work, is also highly relevant to the concept of hallucinations in generative models, but this connection is absent in the manuscript. For more on this topic, see [5].

- The motivating examples (Figure 1) illustrate the link between epistemic uncertainty and concerns of bias and fairness. However, the paper lacks a thorough discussion of how EMoE addresses bias and fairness within text-to-image models, a critical aspect of the model's real-world implications.

[1] Self-Supervised Mixture-of-Experts by Uncertainty Estimation

[2] Training of Neural Networks with Uncertain Data: A Mixture of Experts Approach

[3] Efficient Deweather Mixture-of-Experts with Uncertainty-aware Feature-wise Linear Modulation

[4] TIBET: Identifying and Evaluating Biases in Text-to-Image Generative Models

[5] Understanding Hallucinations in Diffusion Models through Mode Interpolation

### Questions
- Since the CLIP score has known biases, particularly with demographic representation, why did you choose it as the sole performance metric? Could you discuss any potential impacts of these biases on your evaluation and whether you considered any additional metrics to provide a more comprehensive assessment?

-  Epistemic uncertainty is closely linked to hallucinations in generative models, yet this is not addressed in the manuscript. Could you explain how EMoE might capture or identify hallucinations in generated images, and why this aspect was not included in the current analysis? 

-  A connection could be made with the hallucination metric proposed in [5], allowing for a comparison. This might serve as an alternative to the CLIP metric.

- With reference to Figure 1 there may exist a relationship between epistemic uncertainty and issues of bias and fairness. Could you expand on how EMoE addresses these concerns, and whether additional analysis on bias and fairness in generated content was considered?

- Since EMoE aims to provide interpretable uncertainty estimates, could you discuss how practitioners could use these estimates to improve model reliability or detect potential biases? Are there any specific guidelines for interpreting and acting on the model’s uncertainty scores?


[5] Understanding Hallucinations in Diffusion Models through Mode Interpolation

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Epistemic Mixture of Experts (EMoE), a method for estimating epistemic uncertainty in text-to-image diffusion models by leveraging pre-trained models for zero-shot uncertainty estimation. EMoE leverages pre-trained networks for zero-shot uncertainty estimation, avoiding the need for additional training. In order to achieve this, they ensemble expert models from libraries such as HuggingFace during the diffusion process and compute the variance between them to give an uncertainty score. The method allows for early detection of uncertainty at the first U-Net layer, which could enable early stopping to save computational resources. To refine this score for final output, the authors additionally calculate variance after the U-Net mid-block. Experiments do show a correlation between uncertainty scores and CLIP scores, demonstrating its ability to measure uncertainty over previous work, DECU in and out of distribution. Additionally, they show experiments to support design choices such as ensemble size and estimating at the first layer. Overall, EMoE advances uncertainty estimation in diffusion models, but could use some additional clarifications in terms of expert selection. The authors mention that memory overhead is a potential concern, and I would agree that this could be a major limiting factor in the practicality of this approach.

### Strengths
- Their method estimates epistemic uncertainty without needing additional training as evidence by their correlation with CLIP scores
- The idea of separating the computational paths early to allow for early stopping is useful, saving potential computational cost
- They show results that this can perform well in out of distribution tasks

### Weaknesses
- Although they do not need to train their gating mechanism for their experiments, in a practical application, this would need to be done as it cannot account for more complex prompts
- More complex generation tasks would theoretically need more domain specific experts which could quickly add to computational overhead
- In figure 4 and table 1, the difference in clip score and word count between quartiles is very small (but does correlate with their score)
- The background section is almost 2 full pages. This definitely could have been filled with more results or ablations or methodology.

### Questions
- They mention that the quality and the diversity of their experts has a great effect on performance but have no analysis on how they selected their expert models.
- It might be useful to show an additional ablation that shows the amount of additional computational overhead their approach adds compared to base generation.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes to measure the epistemic uncertainty associated with text-to-image diffusion models by using a mixture-of-experts model constructed by using a collection of off-the-shelf diffusion models. The uncertainty is estimated via the aggregated variance across dimensions of a latent variable across ensemble members. Experimental results show alignment of the proposed metric with the CLIP score, indicating that a low uncertainty generally indicates high CLIP score.

### Strengths
+ This paper presents a simple method to quantify the uncertainty associated with the text-to-image generation process, potentially helping users decide whether or not a given generation may be accurate or not

+ The alignment with CLIP score seems to indicate that the proposed uncertainty measure seems to capture some important signal regarding the correctness of the generated image

### Weaknesses
One of the weaknesses of this paper is that it considers an **ill-motivated problem**. For example, Figure 1 is used as a motivating figure to demonstrate that text-to-image models may be biased. However, this figure does not seem to showcase any problems with these models, as the generated images for all prompts seem accurate. It is unclear how the observed descrepancy in the numerical uncertainty scores highlight any problem with the input-output behaviour of such models. 

Additionally, the underlying problem is also **not well-posed mathematically**. In particular, while the paper aims to estimate the epistemic uncertainty, it does not specify the precise random variable of which the uncertainty is estimated. Because of this, it is unclear how one must interpret the numerical uncertainty estimate. While the method itself computes the variance across dimensions of a latent representation, it is unclear whether this fundamentally translates to uncertainty of any aspect of the input-output map. This results in the numerical uncertainty estimate itself being an **ill-motivated heuristic**, as without defining the random variable whose uncertainty is being estimated, it is hard to reason about whether the proposed metric is a good estimate or not. 

Experimentally, the paper relies on the usage of the CLIP score to motivate its method, where it finds that the CLIP score generally aligns with the uncertainty metric. However, this fails to account for the fact that the **CLIP score may itself have issues with bias**, particularly that CLIP score may be higher for english text than finnish text due to the lack of finnish training data for training CLIP. This implies that experiments involving the CLIP score may not be useful in demonstrating correctness of the proposed metric.  

Finally, I believe the paper **conflates ensembles and mixtures of experts**. Unless I am mistaken, the method in the paper seems to employ an ensemble, while the text claims usage of mixtures of experts. 

Given these weaknesses, I am inclined to reject the paper at this time.

### Questions
I request the authors to address the weaknesses mentioned above. In particular, clarifying the mathematical and conceptual issues relating to the underlying random variable whose uncertainty is being estimated will help. In addition, some conceptual motivation regarding why the proposed uncertainty estimation metric is accurate will also improve this paper. 

In addition, I request the authors to clarify how the proposed metric measures epistemic and not aleatoric uncertainty, as this is unclear in the draft.

(Minor Suggestion) In section 2, please specify the dimensions of all latent variables for clarity

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper proposes EMOE, a method to measure epistemic uncertainty (EU) in text-to-image diffusion models using pre-trained components. Experiments show that higher EU relates to poorer image quality and inconsistent outputs. The authors also carry out experiments to measure societal biases such as language and gender using EU.

### Strengths
- Using pretrained components to measure EU is more resource-efficient than training the MOE in baselines. 
- Showing that EU can be used to reveal biases such as on language and gender is highly relevant given the increasing interest in safe and fair generative models.

### Weaknesses
- My main issue with the paper is the explanation of how the method works, which could stem from my unfamiliarity with MoE models. Are the authors using M different diffusion models and decoding the same prompt, then measuring the variance between models at a predefined layer of the Unet block to calculate EU? Fig 2 and 3 are not clear to me.

- As I understand, MoE requires training of a gating layer and the experts, while the authors appear to use a pretrained library (segmoe) that can accomodate any combination of different diffusion models without explanation of how it works. Could the authors clarify how segmoe works? I suggest including an explanation in the paper as well.

- In paragraph lines 306-315, how does the gating mechanism work? The method 'compares the input activations to the gating module with the precomputed gate vectors", but theres no further details of what this means. Can the authors either provide pseudocode (or concrete mathematical expressions if they differ from vanilla MOE) of the gating mechanism? Are these modifications what the authors are referring to in line 321: "with modifications to support our method"? 

- I believe providing pseudocode of the modifications they made and the inference process to measure EU will improve clarity of the paper substantially.

### Questions
- What does CA refer to in Figure 3 caption?
- Typo on line 353-354: "Prompts in the lower uncertainty quartiles (i.e., Q1 and Q2) were shorter in both character and word count" but it is the other way around in Table 1.
- Is it normal for the CLIP score variation to be so small and are such small variations meaningful? E.g. in Fig 4, the left axis scale is so small (0.3 between the min and max points) while its very large in Fig 7.
- I'm not sure what Fig 6 is showing and what the English prompts are for. Without any basis for comparison like qualitative samples of lower quality images or quantitative metrics we cannot conclude whether those images are 'high' or 'low' quality in line 376.

### Soundness
2

### Presentation
1

### Contribution
2
