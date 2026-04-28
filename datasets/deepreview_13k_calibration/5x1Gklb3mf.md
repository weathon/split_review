# Learning Phase Representations for Microstructural Segmentation in Metallographic Images through Expert Knowledge

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 5, 6, 8

## Abstract
Automated segmentation of metallographic images containing multiple phases such as martensite, ferrite, and pearlite is essential for quantifying different phases and thereby helping in the understanding properties of materials. Segmentation of these phases is challenging as they often exhibit overlapping boundaries, similar textures, and other more complexities that require a holistic understanding of the microstructures and correct phase representation within the image. To this end, we propose a novel approach for learning phase representations that captures the subtle differences between phases. Our proposed Phase Learning Module strategically integrates phase ratio information with image encodings to produce ratio-aware features that preserve critical spatial details. Materials scientists can roughly estimate phase ratios by examining an image, and our proposed model leverages this expertise. While we use expert-estimated phase ratios during inference, we train a model using accurate phase ratios obtained from target mask images. To our knowledge, this is the first use of class ratios as input in a deep learning segmentation model that serves as constraints to guide consistent phase proportions in predictions. Experimental results demonstrate segmentation performance improvements on both private and public datasets, with a 5.65% increase in Dice scores on the private dataset and a 6.48% improvement on the MetalDAM dataset with only 1.07% increase in model parameters. Furthermore, visualizations show that our approach leads to learning of more distinct and better phase representations across models. The code and private dataset will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The author builds upon the existing SAM model and designs a new information fusion component called the Phase Learning Module. This module integrates additional information, such as phase ratio data, with image encodings to generate ratio-aware features that enhance segmentation performance. The author tested the model on both private and public datasets, achieving promising results. The application of artificial intelligence to explore less mature fields is commendable, and the author's commitment to making the code and datasets publicly available is beneficial to the field. However, the technical contribution of this work is insufficient for an ICLR paper and may be more suitable for a domain-specific journal.

### Strengths
1. According to the author, this is the first instance of using class ratios as input in a deep learning segmentation model, where they serve as constraints to guide consistent phase proportions in predictions.
2. The author claims that releasing the dataset and code may be meaningful for advancing research in a relatively new materials field.

### Weaknesses
1. The main issue with this paper is the limited technical contribution. As an ICLR paper, the primary focus should be on the machine learning contribution, but this work mainly relies on fine-tuning SAM. While some technical designs, such as the phase ratio prompt, are introduced, these are clearly minor modifications of SAM, and there are already numerous similar methods. With proper revisions, this could potentially be a good AI for Science paper; however, the current technical contribution is not substantial enough for this problem, and it lacks significant insights for the ICLR audience. It may be more suitable for a domain-specific journal.

2. Although the author claims that the Phase Learning Module is a technical contribution, there are some issues with its design and evaluation. The attempt to integrate external information into the SAM-based segmentation model for improved performance is commendable. However, the practical rationale and potential costs of this approach need thorough evaluation. During training, prompt information is derived from labels, but at the inference stage, acquiring additional information incurs costs. It is important to assess whether this additional cost is justified in real-world applications. Moreover, if the information is obtained from test labels, there is a risk of data leakage.

3. Specific comparison and evaluation shortcomings:
  
    a. Fairness of Comparison: The author mainly compares basic segmentation models, but even these comparisons lack comprehensiveness. For example, segmentation models based on fundamental transformer architectures, such as TransUNet and UCTransNet, are not sufficiently evaluated. Furthermore, the model with external information is only compared against SAM, ignoring other deep learning models that focus on similar multimodal information fusion. This raises concerns about whether SAM’s framework is necessary for multimodal fusion or if a simpler attention mechanism could achieve similar results.

    b. Metric Selection: The author evaluates the segmentation model using only the Dice coefficient, which may not be sufficient or reliable. Other metrics, such as IoU, NSD, or those assessing boundary accuracy, could provide a more comprehensive evaluation. Additionally, the dataset size is not clearly discussed. If the dataset is small, cross-validation should be performed, and the mean and variance reported, along with statistical tests like a t-test to prove the effectiveness of the newly added module.

    c. Parameter Comparison: Adding the new module likely increases the number of parameters. Comparing only performance without considering parameter count is not entirely fair. Moreover, the author does not compare different configurations of the SAM model (e.g., small, base, large versions), which should be addressed.

### Questions
Refer to the discussion in the Weaknesses section. The experimental comparisons need to be more comprehensive, with a wider selection of evaluation metrics and more baselines (including both basic segmentation models and multimodal fusion models, not just SAM). Additionally, a detailed comparison of model parameters and inference speed is necessary. Extra manual experiments may also be needed to evaluate the practicality of acquiring prompt information.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an approach for segmenting metallographic images by integrating expert knowledge through phase ratios, which are estimated by domain specialists. The proposed Phase Learning Module (PLM) enhances the segmentation model’s accuracy by refining image encoding with ratio-aware features, achieving improved performance on both public and private datasets.

### Strengths
By incorporating expert phase ratio input, the model bridges domain knowledge with deep learning, improving interpretability and alignment with real-world observations.

The model demonstrates clear performance improvements in Dice scores, achieving substantial segmentation accuracy increases on challenging microstructural datasets.

The model allows input of phase ratios during inference, improving usability in applications requiring expert oversight.

### Weaknesses
With only 42 images in MetalDAM and 24 in the private dataset, the training data is limited, potentially impacting the model’s ability to generalize across diverse materials. The small dataset size raises concerns about overfitting, especially given the complexity of the model architecture and the number of learnable parameters. It is unclear if the reported performance gains would hold up with a more extensive and varied dataset that includes a wider range of microstructural features and material types. The reliance on a limited dataset also makes it difficult to assess the robustness of the model to variations in image quality, such as noise, lighting conditions, and sample preparation artifacts.

The model’s effectiveness relies on accurate phase ratios, which may limit its utility when expert estimations are unavailable or imprecise. The performance degradation with inaccurate phase ratios is a significant concern, as it introduces a practical bottleneck. The model’s reliance on expert input for phase ratios makes it less suitable for automated systems or situations where domain expertise is lacking. Furthermore, the sensitivity to inaccurate ratios suggests a potential instability in the model's learning process, where the model might be overly influenced by the provided ratios, rather than learning the underlying image features.

### Questions
How does the model perform in the absence of accurate phase ratio inputs, and are there plans to mitigate this dependency?

Have you considered expanding the dataset, or are there augmentation techniques that could address the limited training data?

Could you provide ablation studies to assess the impact of individual modules, like Phase Ratio integration, SA, and FA, on overall performance?

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
This paper proposes a novel method for learning phase representations in the context of metallographic segmentation, effectively capturing subtle differences between phases. The phase learning module introduced in the paper adaptively integrates phase ratio information with image encoding to generate scale-aware features that preserve critical spatial details. During inference, phase ratios can be coarsely estimated from the image to achieve improved segmentation performance. The paper is clearly articulated and well-written.

### Strengths
1. The background, motivation, and proposed method are introduced clearly.
2. The comparison with CNN-based segmentation methods is comprehensive.
3. The experimental analysis and explanatory figures are well-presented, and the proposed learnable phase representation method demonstrates a significant improvement in results.

### Weaknesses
This paper introduces a learnable phase representation by incorporating phase ratios, statistically derived from ground truth, into the network. During testing, the method relies on expert-estimated phase ratios as conditions, yielding notable performance improvements over the baseline segmentation. However, certain aspects concerning innovation and fairness in comparison could be improved.

Firstly, the use of ground-truth statistical information was previously employed in [1], where such statistical information was constrained within the loss function, thus avoiding the need for conditional input during inference.
[1] Do we really need dice? The hidden region-size biases of segmentation losses.

Secondly, as the approach requires expert-estimated phase ratios during inference, it falls into the category of interactive methods, necessitating a fair comparison with interactive approaches in terms of interaction time and final performance.

Thirdly, the phase ratio is used as a scalar input condition, which represents a weak form of supervision. This single numerical value likely imposes stringent requirements on the phase ratio, potentially leading to weaker generalization capabilities. Furthermore, the contribution of this scalar input to the overall results appears to be relatively limited, requiring a stronger justification and more robust evidence.

### Questions
1. I am skeptical about the claim that precise phase ratios are needed during training but that inference can achieve high performance without accurate or even any phase ratio. If the authors' claim holds true, a cascade inference approach could be employed: the first step would involve prediction without phase ratios, followed by phase ratio estimation from the predicted results for a second inference step, thereby potentially removing the need for expert-provided phase ratio assessments.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a module that incorporates domain-specific knowledge to guide a segmentation model, to accurately segment metallographic images. This guidance is the ratio of each segment in the image, while during training it is computed using the GT and during inference it is provided by the operating experts.

### Strengths
Problem formulation and motivation is presented really well.
The paper is easy to follow.
It makes sense to utilize a segmentation foundation model and inject domain-specific hints.
It shows pretty consistent (and not negligible) improvements on several segmentation models and on two datasets.

### Weaknesses
1) The presented scientific background is too short. I suggest presenting a broader related work section that is separate from the introduction section. A bit more information on what is done on the vision-metallography domains may be helpful, and a bit more information at least on LoRA-SAM as your reported baseline utilizes it. At least - introduce its main components, since you use them in your encoder and decoder.

2) Currently the setting requires the operators to work "harder" as it demands their guidance.
I would suggest to to train another module that will predict the ratio from the input image. Instead of simply calculating it from the GT, predict it from the input and penalize using the GT ratio. This will give you the option to operate using only the image In inference.
It will be interesting to see in this zero-expert-intervention setting, how well does the model perform.

3) It will be interesting to see an analysis of gamma and delta. What did the model preferred to focus on?

Technical issues:
Line 24: "model" -> "a model"

Figure 3: Why is there an arrow from the input to the Phase Ratio Extractor in training? Shouldn't the arrow start from the GT?

Figure 4: Fix the squares behind the yellow square below add coords

Line 247: "denote" -> "denotes"

### Questions
The definition of n and k are not clear to me. Is n defined by the total number of phases in the dataset? Something else?
k is identical in each segmentation mask? If not, denote that each mask has a different k^i or something like it.

### Soundness
3

### Presentation
4

### Contribution
3
