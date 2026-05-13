# FigCaps-HF: A Figure-to-Caption Generative Framework and Benchmark with Human Feedback

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Captions are crucial for understanding scientific visualizations and documents. Existing captioning methods for scientific figures rely on figure-caption pairs extracted from documents for training, many of which fall short with respect to metrics like helpfulness, explainability, and visual-descriptiveness \cite{summaries-as-captions-preprint} leading to generated captions being misaligned with reader preferences. To enable the generation of high-quality figure captions, we introduce \textbf{FigCaps-HF} a new framework for figure-caption generation that can incorporate domain expert feedback in generating captions optimized for reader preferences. Our framework comprises of 1) an automatic method for evaluating quality of figure-caption pairs, 2) a novel reinforcement learning with human feedback (RLHF) method to optimize a generative figure-to-caption model for reader preferences. We demonstrate the effectiveness of our simple learning framework by improving performance over standard fine-tuning across different types of models. In particular, when using BLIP as the base model, our RLHF framework achieves a mean gain of 35.7\%, 16.9\%, and 9\% in ROUGE, BLEU, and Meteor, respectively. Finally, we release a large-scale benchmark dataset with human feedback on figure-caption pairs to enable further evaluation and development of RLHF techniques for this problem.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of generating high-quality captions for scientific figures. Traditional methods follow the simple image captioning approach for this task. The paper made two contributions: (1) introduction of an eval benchmark (2) conduct the first RLHF-based method for this problem. The dataset and code are open-sourced. Experimental results also suggest promising gains over baselines.

### Strengths
1. The paper presents a set of evaluation methodology and benchmark, which can be useful for future research in the field.
2. Experimental results show clear gains over the baseline.
3. The paper is well written and easy to follow.

### Weaknesses
1. The method used in the paper is a combination of existing techniques, i.e. RLHF. The technical innovation is hence limited.
2. The applicability of the method is narrow since it is targeting for figure captioning task only. It will be more inspiring if it can be extended to general image/video captioning.

### Questions
I found it a bit confusing to the two contributions in this paper together as a "framework", as I don't feel they share synergy.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on existing Figure-to-Caption models that fall short of metrics like helpfulness, explainability, and visual-descriptiveness. To this end, they introduce an RLHF framework for figure-to-caption generation with a small amount of actual human feedback for generating high-quality captions. They also propose a new benchmark of figure-caption pairs with caption quality scores for a better understanding of the read-aligned figure-caption pairs.

### Strengths
1. **The proposed method is effective**. As shown in Fig.2, the RLHF has improved the BLIP and Vit+GPT2 models with a clear improvement.

2. **The benchmark of figure-caption pairs is helpful**. This paper provides a new benchmark of figure-caption pairs is helpful for the research community, and they have done a great release.

### Weaknesses
1. **Time Complexity Analysis.** This paper claims that using offline reward-conditioned behavioral cloning for model optimization is computationally efficient. It is not convinced, that you should compare the time complexity analysis between the offline RLHF and online RLHF methods.

2. **The proposed method is not novel enough.** The framework of the RLHF for figure-to-text can not provide more insight for the understanding of the read-aligned figure-caption pairs. It may not be enough for the technical contribution.

3. **The writing needs to be improved**. There are many typos in the main text.
e.g. figure-ti-caption -> figure-to-caption in Section 6.

### Questions
As shown in weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This ppaer proposes a RLHF framework, FigCaps-HF, a novel framework that leverages domain expert feedback to generate high-quality figure captions tailored to reader preferences. Empirical results show that the caption performs better than BLIP finetuning. The authors also release the benchmark and human feedback data.

### Strengths
1. The proposed pipeline holds promise for enhancing image captions, with compelling results demonstrated on smaller datasets.

2. The comparison to the fine-tuned BLIP model highlights the superior performance of the RLHF method, as evident in both human evaluations and standard metrics.

3. The release of human feedback datasets is a valuable contribution that can benefit a broad range of research communities. The authors also provided detailed human data collection interface.

### Weaknesses
1. The experiments conducted in this study are limited in scale. The choice of a relatively weak baseline and potential data distribution shifts raises concerns about the fairness of the comparisons. Specifically, the use of BLIP fine-tuning as the primary comparison point, while common, does not represent the state-of-the-art in image captioning. The lack of comparison against more robust models, such as those employing transformer architectures with larger pre-training datasets, makes it difficult to assess the true performance gain of the proposed RLHF method. Furthermore, the relatively small size of the dataset used for both training and evaluation raises questions about the generalizability of the findings to more complex and diverse datasets.

2. The main technical novelty seems to be `HUMAN FEEDBACK PREDICTION MODEL`. However, this is limited discussion why such explicit prediction model can help RLHF. A fair comparions would be how proposed method performe better than end-to-end RLHF system. The paper lacks a detailed analysis of the impact of this prediction model on the overall RLHF performance. It is unclear how the model's predictions affect the policy optimization process and whether the model is truly capturing the nuances of human preferences. A more thorough investigation, perhaps through ablation studies or sensitivity analysis, would be necessary to validate the efficacy of this component. Moreover, the paper does not adequately address the potential limitations of the human feedback prediction model, such as its susceptibility to biases present in the training data.

### Questions
The authors mentioned `As can be seen from the results, our model is able to achieve good results on the validation set. This highlights that our human-feedback prediction model demonstrates out-of-sample generalization and proves the statistical significance of our model.` How different is the data distribution? How would you measure the genearlization ability?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel framework and benchmark dataset for improving figure caption generation using human feedback. The reinforcement learning with human feedback (RLHF) framework uses a small amount of expert annotations about the quality of figure-caption data and uses this to fine-tune figure-caption generation models.
Extensive experiments show that their RLHF framework outperforms standard fine-tuning for various models like BLIP, ViT+GPT2 etc. For example, BLIP-RLHF achieves 35.7% gain in BLEU over fine-tuned BLIP.
Moroever, they release the new benchmark dataset of figure-caption pairs labeled with human feedback such as helpfulness, takeaway, OCR etc. to promote further research in this area.

### Strengths
**Originality**

The paper presents a new RLHF framework that utilizes limited human feedback to optimize caption generation models. The technique of learning an "oracle" model to predict feedback scores at scale is creative. Applying offline RL methods like upside-down RL in this context is also novel.

**Quality and Clarity** 

The authors conduct extensive well-designed experiments on multiple models, ablations, and metrics to demonstrate the effectiveness of their approach. The paper is well written and easy to follow.

**Significance**

The focus on aligning figure captions to human preferences is significant for spurring progress in vision-language models for scientific literature. The paper proposes a feedback-based approach to align captions to human preferences and the annotated benchmark dataset will significantly help in improving research in this domain.

### Weaknesses
Please refer to the questions section for discussion of weaknesses. There is nothing in particular I would like to point out here.

### Questions
**Questions**

1. From Figure 2 (and also intuitively), it seems like the captions that are small in length are often uninformative and hence unhelpful. Would it make sense to add a baseline where the model does not incorporate the Oracle model but just uses this heuristic-based "good" or "bad" token during training? 

2. The improvements on ViT+GPT2 are very minor (Table 2). I wonder would the CLIPCap model be a better backbone model as it learns an adaptor to transform the image features to the language model space, by combining it with required prompts or the human feedback scores.

3. There are relevant missing related work and baselines: Matcha, ACL'23 (https://arxiv.org/pdf/2212.09662.pdf )and Deplot, ACL'23 (https://arxiv.org/pdf/2212.10505.pdf). Although both of these works do not focus on caption generation, they are very relevant for ChartQA task and can be used as backbones that can be fine-tuned for the task of figure caption generation. 

**Minor**

1. Make it clear in the main paper that the BLEU metric is BLEU-4. 

2. The information about how human scores look like comes very later in the paper after section 3.3/3.4. A very brief overview of what these scores are in the introduction would be helpful to the reader.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
