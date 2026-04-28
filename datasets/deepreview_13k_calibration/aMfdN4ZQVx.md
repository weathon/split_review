# Training-free Deep Concept Injection Enables Language Models for Crossmodal Tasks

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Recently, enabling pretrained language models (PLMs) to perform zero-shot crossmodal tasks has been extensively studied. A popular approach is to learn a projection network that projects visual features into the input text embedding space of a PLM, as well as feed-forward adaptation layers, with the weights of the PLM frozen. However, is it really necessary to learn such additional layers? In this paper, we make the first attempt to demonstrate that the PLM is able to perform zero-shot crossmodal tasks without any training, when the observed visual concepts are injected as both additional input text tokens and augmentation in the intermediate features within each feed-forward network for the PLM. Specifically, inputting observed visual concepts as text tokens helps to inject them through the self-attention layers in the PLM; to augment the intermediate features in a way that is compatible with the PLM, we propose to construct adaptation layers based on the intermediate representation of concepts (obtained by solely inputting them to the PLM). These two complementary injection mechanisms form the proposed Deep Concept Injection, which comprehensively enables the PLM to perceive instantly as learning process is no longer needed. Extensive empirical analysis on zero-shot video question answering and visual question answering shows Deep Concept Injection achieves competitive or even better results, compared to state-of-the-art methods requires crossmodal training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a feed forward method to inject text prompts from visual inputs, for visual understanding tasks using large language model. Three variants of the method are presented, which are tested on different visual QA and dialogue datasets. Comparisons show that even without fine tuning the LLM with visual inputs, the system performs comparable or slightly better than competing algorithms.

### Strengths
The strengths of the paper are as follows:

1. The method does not require any training, and works simply augmenting the forward path of LLM by injecting semantic visual concepts. 
2. Experiments have been conducted on various QA datasets assessing the performance of the method. The method looks like performing at par or better than some of the prior methods which do joint visual and text encoder training. It beats Flamingo, a visual-text encoder comprehensively on visual QA.
3. The method can be used easily with different PLMs and paper shows application of the method in multi-modal dialogue system, where the method outputs look reasonable.

### Weaknesses
The weaknesses are as follows:

1. The paper describes two variants of the DCI method in Section 3.2.1 and Section 3.2.2, however the variations presented in the experiments are based on the vocabulary selection method (DCI, DCI-A, DCI-LM). The authors have not assessed the performances of the previously described variants. It is unclear how the two injection mechanisms described in sections 3.2.1 and 3.2.2 contribute individually and in combination to the overall performance. The paper lacks a detailed ablation study to disentangle the effects of these mechanisms.
2. In experiment section, the visual encoder has not been mentioned explicitly. Authors need to add that information in the tables as well as description. This lack of clarity makes it difficult to reproduce the results and assess the impact of the visual encoder choice on the overall performance. The specific architecture and pre-training of the visual encoder should be clearly stated.
3. The vocabulary addition is a major step of the algorithm. Certain details and variations in vocabulary are missing: 1. What is the total number of visual concepts taken in the experiments, 2. What is the difference in output vocabulary of DCI-LM vs other variants. In equation 10, how are authors going from output of LLM to visual concepts. Question by itself can generate very open ended responses from LLM. Similarly for DCI-A, what is the number of top frequent words taken as dictionary. The paper needs to clarify how the LLM output is constrained to select relevant visual concepts and what the precise size and nature of the vocabulary are for each variant. The process of mapping LLM output to a constrained vocabulary of visual concepts is not well-defined.
4. In Table 2, there is not much difference between the results of BLIP-2 and proposed DCI variants. Authors have not explained the reason behind no significant change in output accuracy wrt original BLIP-2. The paper needs to provide a deeper analysis of why the proposed method does not yield a substantial improvement over BLIP-2, especially given that it is designed to incorporate visual information more effectively.
5. Examples of multimodal dialgoue systems show several images with named entities like Great Wall of China, orchid, etc. How is the current framework accounting for named entities in their method? Just visual input can potentially generate hallucinations in the LLM output. Authors have not explored the quality of the system in any details in the paper, hence the section does not add to the contribution of the paper. The paper needs to address how the system handles named entities and prevent potential hallucinations. A more detailed qualitative analysis of the multimodal dialogue system is needed to demonstrate its effectiveness.

### Questions
Questions to authors have been posted in weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel approach for zero-shot video/visual question answering leveraging the capabilities of a Large Language Model. To achieve this, the authors translate relevant visual concepts into textual representations using a predefined vocabulary set. Subsequently, they introduce the Deep Concept Injection Module, which integrates these textual visual concepts into the input and feed-forward networks. The effectiveness of this method is validated through extensive experiments conducted on eight video question datasets.

### Strengths
1. This paper proposes to inject the textual visual input into the feed-forward network, with experimental results affirming the efficacy of this approach.
2. Extensive experiments on 8 benchmark video question answering datasets demonstrate the effectiveness of the proposed method.

### Weaknesses
1. As shown in Eqn. (8), the input features of feed-forward networks guide the aggregation of the output features of feed-forward network, which is hard to comprehend. More explanations are required.
2. The authors adopt PLM to extract the features of textual visual concepts. However, when the length of the textual visual concepts exceeds one, it would be better to elucidate the specific feature extraction process.
3. There exists ‘?’ and ‘-’ in Table 1. It would be better to explain the meaning of these quotes.
4. While the ablation studies regarding hyper-parameters are included in the appendix, it would be beneficial to mention the best hyper-parameter settings in the implementation details to make the paper more concrete.
5. This method demonstrates remarkable performance. Could the authors consider releasing the source code upon acceptance?

### Questions
Please refer to the weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a method to inject visual concepts into pretrained LLMs without any training for vision-language tasks. The authors leveraged a pre-extracted concept library to aggregate vision-related concepts into feed forward pretrained LLMs with probabilistic weighting. By properly constructing the concept library, the proposed DeepConceptInjection (DCI) model achieve state-of-the-art results on several vqa and video-qa tasks with significant training overhead reduction.

### Strengths
The proposed model is training-free, by properly constructing the concept library and weighting the forward features of words in concept library, the resulting DCI can correctly adapt vision-related information into pretrained-LLMs for vision-language tasks. The resulting model achieve state-of-the-art results compared with existing VQA or Video-QA models with similar model scale.

### Weaknesses
Despite the good performance and simplicity of the method, this paper seems to be missing several critical key points:
- First, the concept library seems to be extremely important in the whole DCI pipeline, however, how to construct this concept library given different input datasets or domains seems to be too simple for evaluating if this pipeline could be adapted to more general settings. The authors should consider adding more details to this concept library construction process for the reviewers to evaluate the contribution of this paper.

- The overall architecture seems extremely simple and efficient. Given the good performance, the authors should have considered providing more insights on why this simple augmentation strategy, or put it another way, weighting input and features from the concept library, could help improve vision-language tasks. Is this augmentation enough?

### Questions
See the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Deep Concept Injection (DCI) as an approach to achieving zero-shot cross-modal tasks without the need for additional training. This work conducts a comprehensive set of experiments and analyses to validate the effectiveness of this approach.

### Strengths
The method of constructing projection networks to replace fine-tuning is intriguing. The authors successfully inject observed concepts, facilitating cross-modal fusion in self-attention layers and feed-forward networks.

### Weaknesses
The paper claims to be the first to demonstrate the ability of Pre-trained Language Models (PLMs) to perform zero-shot cross-modal tasks without any training. However, there exist similar works, such as Tip-Adapter [1], which should be discussed and compared to provide context and clarify the novelty of this approach. The core issue is not just the existence of other zero-shot methods, but the specific claim of achieving cross-modal fusion without any training. The paper needs to more clearly delineate what constitutes 'training' in the context of zero-shot learning. For instance, even if the projection networks are not explicitly trained on the cross-modal task, the use of pre-trained language models and potentially pre-existing vocabularies might introduce some form of implicit training bias that needs to be acknowledged and discussed. Further, the paper should discuss the limitations of relying on pre-existing vocabularies and how these choices impact the performance and generalizability of the proposed method.

### Questions
Does the Deep Concept Injection process incorporate additional information? While there is no explicit training involved in the design of this paper, has any training data been indirectly introduced into this process?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
