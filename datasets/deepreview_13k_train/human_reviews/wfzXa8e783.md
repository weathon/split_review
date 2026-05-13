# Navigating Text-To-Image Customization: From LyCORIS Fine-Tuning to Model Evaluation

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Text-to-image generative models have garnered immense attention for their ability to produce high-fidelity images from text prompts. 
Among these, Stable Diffusion distinguishes itself as a leading open-source model in this fast-growing field.
However, the intricacies of fine-tuning these models pose multiple challenges from new methodology integration to systematic evaluation.
Furthermore, we present a thorough framework for the systematic assessment of varied fine-tuning techniques. This framework employs a diverse suite of metrics and delves into multiple facets of fine-tuning, including hyperparameter adjustments and the evaluation with different prompt types across various concept categories.
Through this comprehensive approach, our work provides essential insights into the nuanced effects of fine-tuning parameters, bridging the gap between state-of-the-art research and practical application.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose LyCORIS, an open-source library that contains multiple fine-tuning techniques for Stable Diffusion. The authors also explore many improved fine-tuning techniques such as LoCon, LoHa and LoKr. This paper also presents evaluations for different fine-tuning techniques using multiple metrics and prompt types.

### Strengths
(1) The theory and experiments are both solid. The paper has over 57 pages devoted to analyzing the fine-tuning techniques.
(2) The details for experiments are very clear.
(3) In addition to the framework, the authors also explore other fine-tuning techniques.

### Weaknesses
(1) The results of this framework combined with ControlNet can be presented in this paper.
(2) Efficiency (time and GPU memory cost) of different approaches are not provided and analyzed.

### Questions
(1) Please refer to the main questions in the weakness section.
(2) A minor question: It will be better if the authors provide the results on other versions of stable diffusion, such as SD2.0 and SDXL.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This author introduces LyCORIS, an open source library dedicated to fine-tuning of Stable Diffusion, which integrates a comprehensive range of finetuning methods. For rigorous comparisons between the implemented methods, the author proposes a comprehensive evaluation framework that incorporates a wide range of metrics. Based on the evaluation framework, the author performs extensive experiments to compare different fine-tuning algorithms and to assess the impact of the hyperparameters (i.e, training epochs, learning rate, trained layers, et al). Overall, the experiments, comparisons, analyses, and results of the entire paper are very well-rounded and thorough.

### Strengths
1. Developing an open-source library is of great significance in fostering the advancement of a particular field. After comparing the existing open-source libraries available online, the LyCORIS library offers a relatively more comprehensive set of algorithms.

2. The author has developed a comprehensive benchmark to evaluate various algorithms from multiple perspectives, addressing a significant gap in the text-to-image field. This thorough evaluation and comparison of existing finetuning methods have been lacking in the domain until now.

3. The author conducted comprehensive experiments for different algorithms and parameters; in addition, the author also provided a detailed analysis of the current mainstream fine-tuning algorithms.

### Weaknesses
1. HuggingFace has also released the PEFT library, which supports a wider range of pre-trained models and includes the methods mentioned in the paper. Therefore, what are the advantages of the LyCORIS library compared to PEFT? Specifically, while PEFT may be geared towards expert users, the paper does not clearly articulate the specific design choices in LyCORIS that make it more accessible to less experienced users. For example, does LyCORIS offer a simplified API, pre-configured training scripts, or more extensive documentation tailored for beginners? Furthermore, the claim that LyCORIS covers more methods for text-to-image fine-tuning needs to be substantiated with a detailed comparison of the specific algorithms included in each library, highlighting the unique contributions of LyCORIS.

2. The paper conducted a multitude of experiments and comparisons on existing methods and various hyperparameters, leading to certain conclusions. Based on these findings, could there be a more optimal algorithm or design compared to previous ones? The current analysis, while thorough, primarily focuses on comparing existing methods. It would be beneficial to explore whether the experimental results suggest avenues for novel algorithm design or modifications to existing methods that could lead to improved performance. For instance, are there any observed correlations between hyperparameter settings and algorithm performance that point to a more principled approach to fine-tuning, or any limitations of current methods that could be addressed through new architectural designs?

### Questions
For this kind of paper that builds benchmarks based on a certain field, I would recommend the author to submit to a journal.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a comprehensive library for evaluating text-to-image finetuning methods, typically based on LoRA. In addition to different algorithms, it also provides comprehensive evaluation criteria. Finally, some experimental results provide some insight about different finetuning methods.

### Strengths
1. This is a good engineering paper that provides a library for text-to-image finetuning methods evaluation.
2. It support different matrix factorization techniques such as LoRA, LoHa, LoKr, DyLoRA, GLoRA, GLoKr and so on.
3. This paper also consider comprehensive evaluation metrics, including fieldity, controllability, diversity, base model preservation and image quality.

### Weaknesses
1. This paper mainly focus on LoRA-based finetuing strategies, can it be expanded to other parameter-efficient finetuning methods such as [1] and [2]? It doesn't provide a clear explanation.
2. The conclusion about the performance of different finetuning methods is not clearly presented in the experimental section. Maybe some tables can more straightforwardly represent your final conclusions.

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

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
**Summary:** 
This paper presents an open-source toolkit based on LoRa. I believe this work might be more appropriate for the "benchmarking and datasets" track. Positioned here, it's challenging for me to evaluate the innovation this paper offers.

### Strengths
**Remarks:** 
While the improvements and variants on LoRa are relatively straightforward, the theoretical part of the paper seems sound.

### Weaknesses
 **Summary:** 
This paper presents an open-source toolkit based on LoRa. I believe this work might be more appropriate for the "benchmarking and datasets" track. Positioned here, it's challenging for me to evaluate the innovation this paper offers.

 **Remarks:** 
While the improvements and variants on LoRa are relatively straightforward, the theoretical part of the paper seems sound.

 **Recommendation:** 
I would advise the authors to provide clear insights through experiments and offer some specific suggestions.

 I cannot evaluate this paper because I believe it is proper for a benchmarking and dataset track, not the main track.

### Questions
I cannot evaluate this paper because I believe it is proper for a benchmarking and dataset track, not the main track.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
