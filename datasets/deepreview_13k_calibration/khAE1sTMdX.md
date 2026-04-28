# Towards Unified Multi-Modal Personalization: Large Vision-Language Models for Generative Recommendation and Beyond

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Developing a unified model that can effectively harness heterogeneous resources and respond to a wide range of personalized needs has been a longstanding community aspiration. Our daily choices, especially in domains like fashion and retail, are substantially shaped by multi-modal data, such as pictures and textual descriptions. The \reb{vision and language} modalities not only offer intuitive guidance but also cater to personalized user preferences. However, the predominant personalization approaches mainly focus on the ID or text-based recommendation problem, failing to comprehend the information spanning various tasks or modalities. In this paper, our goal is to establish a Unified paradigm for Multi-modal Personalization systems (\model), which effectively leverages multi-modal data while eliminating the complexities associated with task- and modality-specific customization. We argue that the advancements in foundational generative modeling have provided the flexibility and effectiveness necessary to achieve the objective. In light of this, we develop a generic and extensible personalization generative framework, that can handle a wide range of personalized needs including item recommendation, product search, preference prediction, explanation generation, and further user-guided image generation. Our methodology enhances the capabilities of foundational language models for personalized tasks by seamlessly ingesting interleaved \reb{vision-language} user history information, ensuring a more precise and customized experience for users. To train and evaluate the proposed multi-modal personalized tasks, we also introduce a novel and comprehensive benchmark covering a variety of user requirements. Our experiments on the real-world benchmark showcase the model's potential, outperforming competitive methods specialized for each task.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces UniMP, a unified framework for multi-modal personalization that seeks to simplify the integration of various data modalities and tasks. It constructs a universal data format that facilitates the incorporation of diverse user historical data. It also presents a cross-attention mechanism that enables multi-modal user modeling. Furthermore, it combines several personalization tasks into a cohesive token generation framework and introduces context reconstruction and token-level reweighting for alignment. The experimental results show that UniMP can outperform competitive baselines on various benchmark tasks.

### Strengths
- The motivation to establish a unified paradigm for multi-modal recommendation is good.
- The structure is clear and it is well-written.
- The evaluation is extensive and the experimental results look promising.

### Weaknesses
 - The rational behind the design choice of its approach is not well-explained.
- The experimental setting needs clarification.
- Whether this method can perform well on other datasets except for Amazon datasets is unknown.

### Questions
The paper introduces a unified framework for multi-modal recommendation, which is commendably motivated. Nonetheless, I have concerns regarding the design of its approaches and the evaluation setups, as outlined below:
- The authors introduce a cross-attention mechanism to merge visual and textual data. The rationale for this choice remains ambiguous. It is important to discuss how this approach compares to other vision-language fusion techniques such as CLIP[1] and other multi-modal recommendation systems like VIP5.
- The necessity of the context reconstruction loss is still unclear to me. I wonder the detailed design of this loss item and why it can benefit alignment. And about the token-level reweighting, I think it is important to give more definitions/explanations of easy/hard tokens and how to distinguish.
- In the evaluation part, it is crucial to offer clarity on the experimental settings. Some baseline models like MF and LightGCN operate differently from sequential models like S3Rec and BERT4Rec. Ensuring a clear distinction between these setups is essential to maintain fairness in comparisons.
- The experiments utilize sub-datasets from the Amazon dataset, which might possess similar data distributions. This might limit the generalizability of the results. It would be informative to observe the recommendation model's performance, especially in scenarios of zero/few-shot recommendations, on diverse datasets with visual content.

[1] Radford et al. Learning Transferable Visual Models From Natural Language Supervision. ICML 2021.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a unified personalization generative framework from multi-modal sources with the help of various LMs. Specifically, this work devises a generative personalization framework, UniMP, that can suit many downstream applications, including item recommendation, product search, preference prediction, explanation generation, etc. To achieve this, UniMP devises a universal data format, a user modeling architecture by combining a vision model and a language model, and a token generation framework by integrating multiple personalization learning tasks. Experiments on e-commerce datasets validate the effectiveness of the proposed framework.

### Strengths
1. The idea of proposing a unified personalization framework is intriguing and promising in light of the rapid development of various LMs. 

2. This work addresses several challenges encountered in multi-task learning when the different backbone pre-trained LMs are in different modalities.

### Weaknesses
1. Regarding the technical novelty in data fusion and user modeling, the contributions of this work are not impressive. 
In particular, the strategies of data fusion and user modeling are kind of straightforward. The effectiveness is not validated. Please clarify or verify your choice. 

2. The presentation of this work should improved. Typos can be found without too much effort. 
For instance,  

- the abbreviation UniMP is not introduced when it first appears in the Introduction (see the 3rd paragraph on page 2); 
- in the 1st paragraph of Section 2.1, "Based on s, ...". 

Besides, the notations should be reorganized to make them more readable; e.g., $i_i$ (in Eq. (1)) is confusing.

### Questions
1. How do you incorporate the behavioral data, like click, browse, and scroll?

2. How do you define and characterize the multi-modal information? The category, brand, description, and price are all textual inputs; why are they defined as multi-modalities in the paper?

3. What are the choices of backbone LMs?

4. How does a user handle the token limits of the LLMs when s/he aims to apply this framework?

5. How to apply the proposed framework to other domains other than e-commerce?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on multi-modal personalization systems where the input consists not only text and ID's also images. The output is also multi-modal output generation. The authors take advantage of LLMS as multi-modal prompts.

### Strengths
This paper has following strengths.
  - Good experimental study and results
  - Consider multi-modal multi-tasks

### Weaknesses
 - This paper has a lot of things, but lacks of novelty.
- All the components are already in the literature, bridging pre-trained vision and language models is not new, cross attention idea etc.

### Questions
- What is x (the visual input of the item), how do you provide it in eq 1? Apart from the special token [IMG]?
- If you are already providing the visual input in user's interaction history, you are using the same image in visual encoder again into cross attention module? (As far as l understand, no visual information is added to the user's history, the features come from visual encoder, if this is correct, l suggest that seperate image from the user's history in Fig 1.)
- What is s in page 3 Section 2.1 line 5?

Typos

Page 2, traditional methods suffers -> suffer
page 4, line 2,  infomration -> information
page 4, Section 2.2, the visual input -> The visual input

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study proposes UniMP, a method for enhancing individual user
experiences by integrating multi-modal user information
effectively. It introduces a flexible data format for combining
diverse user inputs, fine-grained user modeling, and a multi-task
optimization approach. UniMP can outperform specialized methods in
various personalization tasks and is particularly effective in
transfer learning scenarios with new users and domains. It also
demonstrates the ability to generate personalized content and handle
noisy multi-modal input. The study highlights the importance of
context reconstruction and token-level re-weighting mechanisms in
improving training effectiveness. Overall, UniMP offers a versatile
approach to multi-modal personalization.

### Strengths
1. UniMP seamlessly integrates multi-modal user data, accommodating
various input types, enhancing personalized recommendations.

2. The model's fine-grained user modeling ensures accurate user
preference predictions, improving overall performance.

3. UniMP excels in transfer learning, adapting well to new users and
domains, providing robust personalized recommendations.

### Weaknesses
The study's weakness lies in its perceived lack of novelty in
combining image and language learning, which may not be considered
highly innovative.

You claim it's "multi-modal," but it only deals with language and
images. Since there's no validation with video or audio, the term
"universal" might be overstated.

### Questions
You claim it's "multi-modal," but it only deals with language and
images. Since there's no validation with video or audio, the term
"universal" might be overstated. Would it be advisable to revise the
title or abstract to specify "language and images" to better reflect
the scope?

The dataset's limitation to Amazon data is acknowledged. To enhance
the study's scope, have you considered validating it with datasets
like Yelp, where there's a combination of image uploads, reviews, and
ratings? Additionally, could you extend the multi-modal validation to
include video and audio data, such as YouTube viewing history?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
