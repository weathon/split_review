# Deciphering Cross-Modal Alignment in Large Vision-Language Models with Modality Integration Rate

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 3, 5, 5

## Abstract
\iffalse
Inspired by the success of large language models (LLMs), large vision-language models (LVLMs) have also adopt the ``first pretraining, then supervised finetuning'' paradigm.
While LLM pretraining focuses on capturing diverse language patterns, LVLM pretraining aims to bridge the modality gap between vision and language. 
Evaluating the pretraining quality of LLMs is relatively straightforward using intrinsic metrics (e.g., perplexity) or extrinsic performance on text tasks, as LLMs deal with a single modality. 
However, evaluating LVLMs is more challenging due to the absence of effective methods to measure its cross-modal alignment. 
Common approaches that are borrowed from LLMs, including first-epoch loss, perplexity, or in-context evaluation, present distinct limitations under specific scenarios for LVLMs. 
In this paper, we aim to establish a domain-informed metric named Modality Integration Rate (MIR), to quantify the cross-modal alignment gap.  
This metric accumulates the domain gap of modalities across the language model layers, uncovering a critical fact that: a significant modality gap often exists in the text embedding space, which gradually diminishes at the shallower layers during training and disappears at the middle layers. 
Based on this fact, this metric can serve as an effective indicator of the pretraining quality of LVLMs, remaining input-agnostic and robust against model overfitting. 
Through extensive experiments, the metric further provides valuable insights into the training configurations of LVLMs, encompassing 
1) principles of scaling pretraining data, 2) laws of enhancing pretraining data quality, 
3) the impact of different training recipes or strategies, and 
4) the effectiveness of various architectural designs. 

\fi

We present the Modality Integration Rate (MIR), an effective, robust, and generalized metric to indicate the multi-modal pre-training quality of Large Vision Language Models (LVLMs). 
Large-scale pre-training plays a critical role in building capable LVLMs, while evaluating its training quality without the costly supervised fine-tuning stage is under-explored. 
Loss, perplexity, and in-context evaluation results are commonly used pre-training metrics for Large Language Models (LLMs), while we observed that these metrics are less indicative when aligning a well-trained LLM with a new modality. 
Due to the lack of proper metrics, the research of LVLMs in the critical pre-training stage is hindered greatly, including the training data choice, efficient module design, etc.
In this paper, we propose evaluating the pre-training quality from the inter-modal distribution distance perspective and present MIR, the Modality Integration Rate, which is 1) \textbf{Effective} to represent the pre-training quality and show a positive relation with the benchmark performance after supervised fine-tuning. 2) \textbf{Robust} toward different training/evaluation data. 3) \textbf{Generalize} across training configurations and architecture choices.
We conduct a series of pre-training experiments to explore the effectiveness of MIR and observe satisfactory results that MIR is indicative about training data selection, training strategy schedule, and model architecture design to get better pre-training results. 
We hope MIR could be a helpful metric for building capable LVLMs and inspire the following research about modality alignment in different areas.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes Modality Intergration Rate (MIR) to evaluate the pre-training quality of LVLMs, which measures the distance between vision and text modalities. The experiments show that MIR is not only robust but also highly related to the pre-training quality, showing a positive relation with the SFT performance. Inspired by the analysis of MIR, the authors further introduce a lightweight module MoCa in SFT to improve multi-modal understanding.

### Strengths
- MIR as a new metric is proposed to evaluate the pre-training quality of LVLMs. Sufficient experiments in the paper shows the effectiveness, robustness and generalisability of MIR.
- Based on the MIR design, a lightweight module MoCa is proposed and used in SFT, improving multi-modal understanding.
- The paper is well written, clear and easy to read.

### Weaknesses
1. The authors merely adapted the FID metric to create the proposed MIR score, which limits the originality of the paper's contribution.
2. FID has recently faced criticism as an evaluation metric. The authors should refer to [1] for more details. Besides, why did they decide to use FID rather than some other metrices, for example, KL-divergence, mutual information, maximum mean discrepancy and so on?
3. The experiments were conducted only on LLaVa-v1.5. To demonstrate MIR's generalizability, the authors should have tested it on more LVLMs. Additionally, the datasets used in the study are too few to prove MIR's effectiveness and generalizability.
4. In my view, the paper's motivation is somewhat lacking. Given the existing metrics for evaluating LVLM performance, introducing a new intermediate metric feels unnecessary.

### Questions
- In Equ. 3, how is the ω function based on the "3σ" principle implemented? Have the authors examined the characteristics of the outlier tokens?
- How does the MIR change at each layer of the model with MoCa, compared with the one without it? Is there a decrease in per-layer MIR as expected?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a metric called Modality Integration Rate (MIR), designed to evaluate the pre-training quality of Large Vision-Language Models (LVLMs) by measuring the distribution distance between visual and textual features. Unlike traditional metrics like loss or perplexity, MIR is shown to be a more effective and robust indicator of pre-training performance, particularly in aligning vision and language modalities. The paper demonstrates MIR’s utility in assessing training strategies, dataset choices, and model configurations.

### Strengths
The evaluation of modality alignment after pre-training LVLMs has not been explored before. The authors highlighted this gap and designed a relatively good metric to address this issue.

### Weaknesses
1. The authors merely adapted the FID metric to create the proposed MIR score, which limits the originality of the paper's contribution.
2. FID has recently faced criticism as an evaluation metric. The authors should refer to [1] for more details. Besides, why did they decide to use FID rather than some other metrices, for example, KL-divergence, mutual information, maximum mean discrepancy and so on?
3. The experiments were conducted only on LLaVa-v1.5. To demonstrate MIR's generalizability, the authors should have tested it on more LVLMs. Additionally, the datasets used in the study are too few to prove MIR's effectiveness and generalizability.
4. In my view, the paper's motivation is somewhat lacking. Given the existing metrics for evaluating LVLM performance, introducing a new intermediate metric feels unnecessary.

[1] Jayasumana, Sadeep, et al. "Rethinking fid: Towards a better evaluation metric for image generation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

### Questions
Please see Weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces the Modality Integration Rate (MIR) as an evaluation metric for the pre-training quality of large vision-language models (LVLMs) and proposes a lightweight Modality Calibration (MoCa) module to enhance alignment between visual and textual modalities. The MIR metric demonstrates good robustness and generality, effectively guiding data scale, strategies, and model design during pre-training. However, the paper shows some limitations in terms of innovation and experimental rigor. For instance, the visualization in Figure 2 lacks persuasiveness, and the choice of weights for the mean and covariance in the MIR formula has not been thoroughly explored. Overall, MIR and MoCa provide a new approach for cross-modal alignment in LVLMs, but there is room for improvement in theoretical discussion and experimental validation.

### Strengths
1.	Introduction of an Innovative Evaluation Metric (MIR): The paper introduces the Modality Integration Rate (MIR), a novel metric to quantify cross-modal alignment quality during the pre-training stage of large vision-language models (LVLMs). MIR effectively reflects pre-training quality without relying on supervised fine-tuning, filling a gap in pre-training evaluation for LVLMs.
2.	Wide Applicability and Robustness: MIR demonstrates robustness across different types and quantities of data inputs. It adapts well to various modal inputs (such as different types of images and texts) and remains stable in the face of overfitting and changes in data distribution. This makes MIR highly generalizable across different data and model configurations.
3.	Practical Optimization Guidance: The experiments showcase the application of MIR in optimizing data scale, data detail level, training strategies, and model architecture design, providing practical guidance for multi-modal pre-training. MIR helps researchers identify optimal data scale and training strategies during pre-training, thereby improving training efficiency.
4.	Introduction of the MoCa Module for Enhanced Alignment: The paper proposes a lightweight Modality Calibration (MoCa) module that further improves cross-modal alignment by calibrating visual features. MoCa reduces MIR values and enhances multi-modal task performance, offering an efficient solution for cross-modal alignment in LVLMs.
5.	Advantage over Traditional Metrics: Compared to traditional metrics such as loss function, perplexity, and other evaluation metrics, MIR shows stronger indicative power and stability, especially in multi-modal scenarios. The experiments demonstrate that MIR is more effective at capturing the fusion between visual and textual modalities during multi-modal pre-training.

### Weaknesses
1.	The paper’s originality appears limited; it is recommended that the author consider either enhancing the contribution or submitting to a general CCFA venue.
2.	The visualization in Figure 2 lacks persuasiveness. Using t-SNE for modality difference visualization appears somewhat redundant. t-SNE requires extensive parameter tuning, and the choice of random data can influence visualization outcomes, making it highly flexible. This flexibility allows almost any pattern to display differences through t-SNE, thus reducing rigor and persuasive impact.
3.	The optimality of the ratios in the MIR formula has not been explored. The MIR formula uses a 1:1 weight ratio of mean distance and covariance to measure modality differences. However, it remains unverified whether this ratio is optimal. Investigating alternative ratios might allow for more effective assessment of pretraining quality. Further exploration of how different weightings affect MIR’s effectiveness in various application contexts is recommended to enhance the indicator’s adaptability and versatility.

### Questions
Refer to Weakness.

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
3

### Summary
This paper introduces a novel metric, the Modality Integration Rate (MIR), to assess cross-modal alignment quality in large-scale Vision Language Models (LVLMs) during their pre-training phase. Through extensive experiments, the authors demonstrate the utility and effectiveness of MIR across a variety of pre-training configurations, thereby proving its practicality and efficacy in evaluating and optimizing LVLM pre-training processes.

### Strengths
1. The introduction of MIR addresses the shortcomings of existing pre-training evaluation metrics, providing a fresh perspective on model assessment.
2. The extensive experimental validation of MIR confirms its stability and predictive power, enhancing the credibility of the research.
3. The study not only discusses theoretical aspects but also provides concrete application examples, offering valuable guidance for practical model training and optimization.

### Weaknesses
1. While the paper demonstrates the practicality of the MIR metric through experimental validation, the discussion on its theoretical basis may be lacking. The absence of a deep mathematical analysis of the metric's nature and influencing factors might hinder understanding of its theoretical support and conditions for applicability.
2. The verification of MIR primarily utilizes standard, large-scale visual language datasets, such as ALLaVA and ShareGPT4V-PT. These datasets might share similar characteristics, limiting the indicator's demonstrated generalizability. Further verification experiments are necessary to establish broader applicability.
3. The paper includes multiple experiments to verify MIR's effectiveness but does not provide a sensitivity analysis of MIR values under various parameter settings. Expanding the analysis to include variations in input data characteristics, model configurations, or training strategies could help evaluate its stability and reliability.
4. Although the paper showcases the practicality and effectiveness of MIR, it lacks a direct comparison with other existing evaluation methods. To better highlight MIR's advantages, further quantitative comparative experiments with other modal fusion indicators are recommended.

### Questions
1. The paper employs the Fréchet Inception Distance (FID) to calculate the distribution distance between modalities. Is there a specific rationale behind this choice? Are there alternative metrics that could also be suitable?
2. The computational time and resource consumption of MIR are not detailed in the paper. What is the computational complexity of MIR when applied in actual large-scale model training?
3. Has there been consideration for performing a parameter sensitivity analysis on MIR? For instance, how do variations in the number of model layers, the scale of modality pairing data, or different regularization strategies impact MIR values?

### Soundness
3

### Presentation
3

### Contribution
3
