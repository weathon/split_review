# Dual-Model Defense: Safeguarding Diffusion Models from Membership Inference Attacks through Disjoint Data Splitting

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Diffusion models have demonstrated remarkable capabilities in image synthesis, but their recently proven vulnerability to Membership Inference Attacks (MIAs) poses a critical privacy concern. This paper introduces two novel and efficient approaches (DualMD and DistillMD) to protect diffusion models against MIAs while maintaining high utility. Both methods are based on training two separate diffusion models on disjoint subsets of the original dataset. DualMD then employs a private inference pipeline that utilizes both models. This strategy significantly reduces the risk of black-box MIAs by limiting the information any single model contains about individual training samples. The dual models can also generate \text{\textquotedblleft}soft targets\text{\textquotedblright} to train a private student model in DistillMD, enhancing privacy guarantees against all types of MIAs. Extensive evaluations of DualMD and DistillMD against state-of-the-art MIAs across various datasets in white-box and black-box settings demonstrate their effectiveness in substantially reducing MIA success rates while preserving competitive image generation performance. Notably, our experiments reveal that DistillMD not only defends against MIAs but also mitigates model memorization, indicating that both vulnerabilities stem from overfitting and can be addressed simultaneously with our unified approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a comprehensive study on a defense mechanism against membership inference attacks specifically targeting diffusion models. The authors employ an ensemble of two diffusion models, each trained on two disjoint datasets, to develop their defense strategy. Subsequently, they propose two distinct defenses utilizing these two models.
The first defense, referred to as DualMD, involves alternating between the two models during the diffusion process. By doing so, half of the steps are executed without any influence from half of the training data. This approach is expected to significantly reduce the overall impact of the training data, thereby making membership inference more challenging, particularly for black-box attacks.
The second defense, denoted as DistilMD, involves distilling the resulting model from DualMD into a new model. This process aims to eliminate even white-box attacks by further reducing the vulnerability of the model to membership inference attacks.
The authors provide empirical evidence demonstrating the effectiveness of their proposed defense mechanism in reducing the performance of existing white-box and black box attacks.

### Strengths
- Membership inference and memorization is a key challenge with diffusion models. Mitigating such vulnerabilities is hence an important topic.

- The idea of using an ensemble of model is clever.

### Weaknesses
 - Although the idea is clever the same idea is explored in previous work as a way to defend against MIA both in classification [1] and generative models (diffusion models in particular!) [2]

- The paper is not evaluated against any adaptive attacks. Is there an attack that can be optimized for DualMD and DistillMD?

- The evaluation of utility is limited.

### Questions
- The paper in [2] uses a very similar idea for realizing differentially private diffusion models. 


- The utility of your models need to be evaluated more extensively. First, you need to provide some real generation so that reviewers can inspect the visual effect of your method. You also need more quantitive evaluation of your technique. It seems you are improving the metrics over non-private models? Does it mean you can claim SOTA for generating with diffusion models? 

- I think there is a need for exploring adaptive attacks. For example, is there something the attacker can do by calling the decoding with different number of steps? If you believe the existing attacks are optimal against your defense, you need to bring a convincing argument.

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
4

### Summary
This paper studies the membership inference defense for diffusion models by training two diffusion models on disjoint data. This work introduce two methods, DistillMD and DualMD. After training model A on dataset A and model B on dataset B, DistillMD uses model A to generate image for dataset B and model B to generate image for dataset A. DistillMD then use generated images to train a student model. DualMD use the model A and B to perform denoising together in denoising the images. At each step, DualMD use one model to perform denoising at that step, then at next step, DualMD use the other model to perform the denoising.
Experimental evaluation include unconditional diffusion model and text-to-image diffusion model, including black-box attacks and white-box attacks.

### Strengths
1. The idea is intuitive and easy to follow, training two diffusion models on disjoint dataset and designing models on how to design defense against MIAs based on these two models.
2. The evaluation considers both white-box attacks and black-box attacks on both unconditional diffusion models and text-to-image diffusion models.

### Weaknesses
I have concerns regarding the privacy and utility evaluation in this work.

1. For the privacy evaluation, it seems to me that similar to Tang et al. 2022, the disjoint dataset training in this work still face some issues for the correlated pairs, Tang et al. 2022 provides a case study how severe the correlated pairs issue is in CIFAR10 dataset. It would be helpful to investigate and discuss the correlated pairs and potential mitigations. It is also unclear to me whether DualMD is better or DistillMD is better for text-to-image diffusion models, as the AUC and TPR-FPR show different trends and Carlini et al. 2022[1] emphasize the importance of worst-case analysis for privacy leakage.

2. For the utility evaluation, it would be helpful to provide the FID and IS metric for images generated from model A and model B with the original data to understand utility trend among DualMD and DistillMD. I wonder if there is a explanation for why DualMD is better than DistillMD for text-to-image diffusion models, or utility gap is small, or the conclusion is dawn on a single dataset Pokemon that may not be true in general. Also it is unclear to me if results for Pokeman in Table 1 is with prompt diversification or without. 

3. The writings could be improved. In introductions, the contribution 2 states the "proposing a technique to prevent the models from overfitting to prompts", it seems to me this method is prompt diversification and is from Somepalli et al. 2023b, maybe the author could clarify what is different from prompt diversification and Sompalli et al. 2023b.  The connection between MIA and memorization are also studied in prior works. For example, in the extraction attack for diffusion models by Carlini et al. 2023, MIA is applied to select those images that are likely to be memorized. Minor question, what is "stopgrad" in Equation (7)?

### Questions
See above.

### Soundness
2

### Presentation
2

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
The paper proposed an ensemble-like method to defend membership inference attacks (MIA) in diffusion models (DM). Instead of training a single DM on the whole dataset, the proposed method train two models on disjoint subsets of the training set. At inference time, the denoising process will be alternately done by two models. The method is tested on the SoTA MIA attacks.

### Strengths
* The proposed method is simple yet effective in defending MIA attacks.
* In the tested datasets and models, the proposed method is effective in defending MIA attacks.
*

### Weaknesses
1. The experiments lack essential baselines and ablation studies. Though most defense methods mentioned in the Related Work were not designed for diffusion models, the distillation-based method should be generally applicable. Note that the proposed method is also a distillation-based method. Thus, the distillation of a single diffusion model (following prior arts noted in the Related Work) should be included as a baseline. More detailed ablation studies should be conducted. For example, if the two models are necessary. Specifically, the paper should investigate the impact of varying the degree of overlap between the training sets of the two models, ranging from completely disjoint to nearly identical, to understand the necessity of the disjoint training sets. Furthermore, the paper should compare against a single model trained with a similar number of total training iterations as the proposed method, to isolate the effect of the dual-model architecture.
2. The claim in the introduction, "We evaluate the effectiveness of our methods in training large text-to-image diffusion models and propose a technique to prevent the models from overfitting to the prompts.", is misleading. In the experiment (Table 4), without using their method, the no-defense baseline can effectively reduce the risk of MIA. I don't think the proposed method contribute to the prompt overfitting.
3. The logic of the paper is confusing.
* It is not clear why the prompt overfitting is considered. In Line 112-113, the prompt overfitting is raised for model memorization, whose connection to the MIA is not clarified in the context.
* Throughout the paper, there are many forward references, making the logic very hard to follow.
* Lacks intuitive explanation on why this method works.
4. In MIA evaluation, the ROC curve should be presented to show the rigor of evaluation in MIA. The paper should also report the Area Under the Curve (AUC) for the ROC curve, which is a standard metric for evaluating the performance of binary classifiers, such as membership inference attacks. Furthermore, the paper should include a more detailed analysis of the trade-off between the defense effectiveness and the utility of the defended model, such as the image quality or diversity.
5. Only one diffusion model (SDv1.5) is used, which makes the conclusion less generalizable. The paper should evaluate the proposed method on other diffusion model architectures, such as DDPM or other Stable Diffusion variants, to demonstrate the generalizability of the proposed method.

### Questions
* How is the proposed method compared to distillation-based baselines?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces two  defense strategies—DualMD and DistillMD—to protect diffusion models against Membership Inference Attacks (MIAs) without significantly compromising model utility. The two defense strategies introduced operate differently: DualMD mitigates MIA risks in black-box settings by dividing data between two models and alternating inference to reduce data exposure. DistillMD combines dual models into a student model via distillation, offering robust defenses against both white-box and black-box attacks.

### Strengths
DualMD and DistillMD effectively adapt ensemble learning and distillation to protect diffusion models from MIA attacks
The paper includes evaluations across various datasets, models, and attack types (both white-box and black-box). This thorough testing underscores the robustness of the proposed methods.

### Weaknesses
Lack of Comparative Analysis with Existing Methods: The study does not explicitly compare its defense methods with existing privacy defense methods beyond describing MIA vulnerabilities. A side-by-side comparison with traditional distillation or differential privacy approaches in image synthesis could underscore the novelty and effectiveness of the proposed methods. Specifically, the paper lacks a quantitative comparison against other defense mechanisms, such as those based on adversarial training or noise injection, which are commonly used in the context of privacy-preserving machine learning. This absence makes it difficult to assess the relative advantages and disadvantages of DualMD and DistillMD.

Limited Discussion of Practical Constraints: The methods require dual models (DualMD) or distillation (DistillMD), both of which can be computationally intensive. Discussing potential resource constraints, such as memory limitations or model scalability in real-world applications, would make the methods' practicality more transparent. The paper should include a more detailed analysis of the computational overhead, including training time and memory requirements, especially when scaling to larger models and datasets. This analysis should also consider the inference time implications, as the dual model approach might introduce latency.

Lack of Explanation on Evaluation Metrics: While metrics like FID, IS, and AUC are widely used, a brief explanation of their relevance to privacy defense and utility preservation would clarify the evaluation approach for readers. The paper assumes that the reader is familiar with the nuances of these metrics in the context of privacy, but a brief discussion on how these metrics capture the trade-off between utility and privacy would be beneficial. For instance, it is not immediately clear how a lower AUC directly translates to better privacy protection, or how the FID and IS scores are impacted by the defense mechanisms.

Improve Clarity on Methods and Results: I find the caption for Figure 1 a bit confusing. I find the presentation a bit confusing. For example, I dont remember the DDPM being introduced but somehow where is an algorithm 1 for the DDPM while there is no algorithm for the DualMD.

### Questions
Could you clarify why you randomly sample t instead of doing it sequentially? in the Algorithm 1 and 2?

### Soundness
3

### Presentation
2

### Contribution
3
