# TPP-LLM: Modeling Temporal Point Processes by Efficiently Fine-Tuning Large Language Models

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Temporal point processes (TPPs) are widely used to model the timing and occurrence of events in domains such as social networks, transportation systems, and e-commerce. In this paper, we introduce TPP-LLM, a novel framework that integrates large language models (LLMs) with TPPs to capture both the semantic and temporal aspects of event sequences. Unlike traditional methods that rely on categorical event type representations, TPP-LLM directly utilizes the textual descriptions of event types, enabling the model to capture rich semantic information embedded in the text. While LLMs excel at understanding event semantics, they are less adept at capturing temporal patterns. To address this, TPP-LLM incorporates temporal embeddings and employs parameter-efficient fine-tuning (PEFT) methods to effectively learn temporal dynamics without extensive retraining. This approach improves both predictive accuracy and computational efficiency. Experimental results across diverse real-world datasets demonstrate that TPP-LLM outperforms state-of-the-art baselines in sequence modeling and event prediction, highlighting the benefits of combining LLMs with TPPs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on the event sequence modeling with LLM-enhanced temporal point processes. Since the former methods of LLM for event sequences often lack fully utilization of the temporal and semantic richness of event sequences, this paper proposes a novel approach about integrating LLM with TPPs by leveraging textual event descriptions and temporal embeddings. By fine-tuning LLMs with TPP losses, the model can generate the event type and the occurence time. Experimental results evaluate the effectiveness of the proposed method.

### Strengths
1. Utilizing LLMs to enhance TPP modeling is an important and interesting attempt for event sequence modeling.
2. Extensive experiments show the superior ability of TPP-LLM compared to existing neural TPP models.
3. The paper is mostly well-writing. The problem background and related work is detailed.

### Weaknesses
 1. The novelty of the approach seems to be somewhat limited. The most contribution is to utilize the description of event types as the input of LLM, and then prompting and fine-tuning the LLM with TPP losses. This improvement seems to be incremental and straightforward, which is also my main concern.
2. The overall result improvements seem to be marginal as shown in Table 2. Most of the best results are from the baseline methods.
3. In 5.7.3, it would be helpful to make further explanation and observation about the prompt effect on “the flexibility in multi-task scenarios” in Line 458. Besides, experiment in 5.7.2 is about the processing order of time and event detailed in line 193, but there is little explanation or reason behind on which strategy should be selected when facing different scenarios. 
4. It will be better to provide details of case study about the event and time prediction, and show how LLM intrinsically helps to make event and time prediction.

### Questions
1. Would different intensity functions affect event and time prediction?
2. What kind of event type description will lead to better event type prediction? Will the event type description affect the time prediction?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces TPP-LLM framework for event sequence prediction. It integrates pretrained LLMs to capture the semantic richness of event types and also employ temporal embeddings. Its strong points are listed below:
1. This papers proposes a novel framework for event sequence prediction based on pretrained LLMs. Existing related works mostly focus on RNN or attention-based mechanism. 
2. This paper gives detailed mathematical expressions of temporal point process and use them to derive the loss function for training.
3. This paper conducts extensive experiments on five real-world datasets, and compare its model with four SOTA models from existing works. This paper also gives ablation studies to analyze how different components of its model contribute to the improved performance.

### Strengths
see summary

### Weaknesses
This paper is slightly below the acceptance bar because (1) lack of related works and baselines; (2), limited improvements on experiment results compared with baselines; (3) unreasonable method in the experiment. Specifically,
1. There are some related works that this paper may overlook, such as Meta TPP [ICLR’23], Fully neural network for TPP [Neurips’19], etc. It seems that Meta TPP [ICLR’23] achieves 46% on next event type prediction on StackOverflow, which is higher than TPP-LLM proposed by this paper.
https://openreview.net/pdf?id=QZfdDpTX1uM] for Meta TPP [ICLR’23]
https://proceedings.neurips.cc/paper_files/paper/2019/file/39e4973ba3321b80f37d9b55f63ed8b8-Paper.pdf for Fully neural network for TPP [Neurips’19]
2. According to table 2 and 3, the improvements brought by TPP-LLM on event sequence modelling, next event type prediction and event time prediction are not significant or convincing. Models without the help of LLM, including AttNHP and THP, have already achieved performance very close to, or even outperformed, TPP-LLM.
3. The design of few-shot experiments may be unreasonable. TPP-LMM is built upon the pretrained LLM, with only several linear layers and LoRA modules left for training. With the assistance of well-pretrained LLMs, it is not surprised that 2% of training data would lead to significant improvement on TPP tasks. But other TPP-specific models are only built on neural networks and trained from scratch. 2% of training data is probably not enough for them to learn and handle TPP tasks. Therefore, the few-shot design may be unnecessary.

### Questions
Given the weak points mentioned above, here are some questions for the authors:
1. What does t_j in Equation (3) mean? Is it one element in t_i?
2. In line 193, there are two choices of event sequence representation, depending on the order of event type and time. Would these two choices make a difference on the experiment result? Which one is used during your experiment?
3. In line 247 and 318, how is the non-event integral term in the loglikelihood calculated in detail during experiment? 
4. In line 323, it says “Experiments results are averaged over five runs.” Is this averaging method commonly used in TPP modelling works? Is it possible that you could provide the experiment results in all five runs?
5. In section 5.7.2, could you give more details on the difference between positional encoding and linear embedding of event type and time? Why they lead to different performance?

### Soundness
2

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
4

### Summary
This paper proposes TPP-LLM, a new framework which integrates temporal point processes (TPPs) with large language models (LLMs). To grasp a better semantic understanding of event types, TPP-LLM applies pre-trained LLMs to encode textual event descriptions and implements parameter-efficient fine-tuning (PEFT) for a better domain knowledge adaptation.  

TPP-LLM stacks the sequence of historical event embeddings into TPP modeling and completes the downstream event prediction as a multi-class classification task and time prediction as a regression task. Comprehensive experiments across multiple real-world datasets demonstrate the effectiveness of the proposed approach.

### Strengths
(1) This paper introduces convincing motivations to study an important problem, event prediction. This paper also has clear problem formulations to split the prediction into event type classification and event time regression. This paper’s presentation is good.  

(2) This paper shows solid mathematical derivations of the eventual loss function for TPP-LLM, which consolidates the proposed contribution of integrating TPPs with LLMs.  

(3) This paper conducts comprehensive experiments across diverse real-world datasets, evaluates the framework’s performance with various metrics, and performs detailed ablation studies to demonstrate the significance of each component of TPP-LLM.

### Weaknesses
 (1) This paper has limited technical novelty. As TPPs, LLMs, and PEFT have been well-known strategies for event prediction, TPP-LLM is a new integrating application, but does not involve fundamental innovations in either semantic or temporal modeling.  

(2) The baseline comparisons are not fair. For Tables 2, 3, 4, 5, the four baselines (NHP, SAHP, THP, AttNHP) are not empowered by state-of-the-art LLMs. However, in Section 2 (from line 100 to line 102), LAMP [1] leverages generative LLMs to handle textual events for abductive reasoning, but also optimizes embedding-based TPP models for multiple downstream prediction tasks. This means that LAMP should be a good baseline competitor, but it was not included in these tables.  

(3) The lack of empirically computational complexity analysis. Although PEFT helps reduce the number of trainable parameters, the GPU memory space occupied by putting the entire TPP-LLM for downstream inference tasks should not be overlooked. An explicit comparison of memory usage and average training time between TPP-LLM and selected baselines is encouraged.  

(4) The lack of interpretability discussion. Apart from experimental results of log-likelihood, accuracy, and RMSE, several case studies involving historical vectors (which act as the bottleneck between LLMs and TPPs) are encouraged to better demonstrate the benefits or importance of integrating LLMs with TPPs.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces TPP-LLM, a novel framework that combines large language models (LLMs) with temporal point processes (TPPs) to model event sequences effectively. The framework utilizes parameter-efficient fine-tuning (PEFT) methods, specifically low-rank adaptation (LoRA), allowing it to adapt pretrained LLMs without extensive retraining.

### Strengths
1. The paper presents a unique integration of LLMs with TPPs, moving beyond traditional categorical representations to utilize the semantic richness of event descriptions. 

2. The paper is well-structured and clearly articulates the methodology, experimental setup, and results.

### Weaknesses
1. The paper does not compare LoRA with other fine-tuning methods like adapter layers, missing an analysis of trade-offs in efficiency and adaptability.

2. The paper lacks testing in diverse domains, limiting insights into how well the model generalizes to different event sequence types.

3. Alternative temporal encoding methods are not explored, leaving questions about whether other techniques might enhance performance.

4. The model’s scalability and computational efficiency on larger datasets or longer sequences are not fully analyzed.

5. There is no discussion of how the size of the pre-trained LLM impacts performance, particularly in the context of using PEFT.

6. The explanation of temporal embedding placements is limited, and more thorough tests of their interaction with semantic features are needed.

### Questions
1. The model focuses on predicting event times with temporal embeddings, but real-world events often have uncertainty or noise in their timing. How does TPP-LLM account for uncertainty or variability in event timing? Are there mechanisms in place to model uncertainty or predict time windows rather than specific times?


2. Temporal point processes often involve continuous event streams. How does TPP-LLM handle event sequences in real-time or streaming contexts where the data is not static? Are there mechanisms to ensure that the model can update dynamically without requiring full retraining?

### Soundness
2

### Presentation
3

### Contribution
3
