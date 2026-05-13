# Exploring Representations and Interventions in Time Series Foundation Models

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
Time series foundation models (TSFMs) promise to be powerful tools for a wide range of applications. However, their internal representations and learned concepts are still not well understood. In this study, we investigate the structure and redundancy of representations across various TSFMs, examining the self-similarity of model layers within and across different model sizes. This analysis reveals block-like redundancy in the representations, which can be utilized for informed pruning to improve inference speed and efficiency. Additionally, we explore the concepts learned by these models—such as periodicity and trends—and how these can be manipulated through latent space steering to influence model behavior. Our experiments show that steering interventions can introduce new features, e.g., adding periodicity or trends to signals that initially lacked them. These findings underscore the value of representational analysis for optimizing models and demonstrate how conceptual steering offers new possibilities for more controlled and efficient time series analysis with TSFMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to understand the internal representations of time series foundation models (TSFM). By analyzing the self-similarity of the model layers, this paper reveals block-like redundancy in the structure that can be used for model pruning. This representational analysis also shows that the conceptual steering  potentially enables more controllable analysis for TSFM.

### Strengths
1.	The main aim of this paper is to address the gap in understanding the underlying mechanisms and learned representations of TSFMs, which remain largely unexplored. The representational analysis examined the representational similarity based on Centered Kernel Alignment (CKA), identified concepts, and localized them to specific hidden states. The representation redundancy found in this analysis was used to prune the model, which reduces the model size as well as improves the inference speed. 
2.	The findings in this paper help us understand the TSFMs, and the knowledge can potentially be used to improve their capabilities. For example,  the predictions can be steered along the conceptual directions using synthetic time series.

### Weaknesses
1.	The analysis is conducted using many existing techniques, which are not specifically designed for time series models. There may be room for improvement by introducing novel techniques specifically designed for TSFMs. 
2.	Section 3.2 is a huge subsection that contains many paragraphs. These paragraphs can be further grouped into subsubsections for better viewing.

### Questions
1. Applying concept steering interventions across all tokens is necessary to achieve the intended steered concept output compared to applying concept steering interventions to a single token. What is the main purpose of concept steering? Is it controllable to achieve some target objectives?

### Soundness
2

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
4

### Summary
This work investigates the internal representations of Time Series Foundation Models (TSFMs), revealing block-like redundancy in their representations. It leverages this redundancy for informed pruning to enhance inference speed and efficiency without compromising accuracy. The study also explores learned concepts like periodicity and trends, demonstrating the potential of latent space steering to manipulate these concepts and influence model behavior, introducing new features to time series signals. The findings highlight the importance of representational analysis for optimizing TSFMs and open new avenues for controlled time series analysis.

### Strengths
1 By comparing representational similarity between layers of the model, this work provides a new method for analyzing TSFMs. Systematic probing of TSFMs through representational similarity identifies redundant representations suitable for model pruning.

2 The work effectively reduces model size and improves inference speed while maintaining accuracy. It introduces the ability to steer model predictions along conceptual directions, influencing outputs in targeted ways.

3 The study provides comprehensive analytical experiments, verifying that steering interventions can introduce new features into signals, such as periodicity and trends. Moreover, it is not limited to a single model but spans multiple TSFMs, enhancing the generality of the findings.The use of open-source models and data facilitates community reproduction and further research.

### Weaknesses
1 Although a pruning strategy is proposed, the effectiveness of reducing computational resource consumption for extremely large models like TimeGPT has not been fully validated.

2 The selection of the parameter α in concept steering may require fine-tuning, increasing the complexity of model application. Have you explored automated methods for selecting the parameter α, or can you provide guidance on choosing appropriate α values for different dataset and models.

3 The study primarily focuses on forecasting and does not explore the generalization of the findings to other time series tasks such as anomaly detection or classification.

4 The computational overhead of calculating and applying steering matrices in real-time scenarios is not addressed, which could be significant for large-scale applications.

### Questions
Refer to weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the author investigates the structure and redundancy of representations across various time series foundation models, examining the self-similarity of model layers within and across different model sizes. This analysis reveals block-like redundancy in the representations, which can be utilized for informed pruning to improve inference speed and efficiency. Additionally, the autjor explores the concepts learned by these models—such as periodicity and trends—and how these can be manipulated through latent space steering to influence model behavior. These findings underscore the value of representational analysis for optimizing models and demonstrate how conceptual steering offers new possibilities for more controlled and efficient time series analysis with TSFMs.

### Strengths
The starting point of this article is very meaningful, being at a time when TSFMs are emerging, it is crucial to explore more efficient, interpretable, and controllable models. Additionally, some experimental findings in the article provide guidance for future TSFM architecture design. Moreover, the figures and tables in this paper are also aesthetically pleasing.

### Weaknesses
I have no objections to the content of this article. My only concern is that it reads more like a technical report, lacking an overall logical structure. Many figures and text sections appear isolated, which could make it difficult for beginners to read and understand. I suggest the authors expand the Introduction section to provide readers with a more comprehensive overview (currently only half a page) and adjust the layout of the figures to accurately correspond with the text content.

### Questions
* **Q1**: I am a bit unclear about the concept of "block" in the article. Does it refer to some adjacent layers? What does it mean to prune Block3 of MOMENT-large at line 426?

* **Q2**: Can you provide a more detailed explanation on how to control the generation of time series? Does this involve modifying some parameters of the model?

### Soundness
3

### Presentation
2

### Contribution
3
