# HallE-Switch: Rethinking and Controlling Object Existence Hallucinations in Large Vision-Language Models for Detailed Caption

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 8, 5, 3

## Abstract
Current large vision-language models (LVLMs) achieve remarkable progress, yet there remains significant uncertainty regarding their ability to accurately apprehend visual details, that is, in performing detailed captioning. To address this, we introduce \textit{CCEval}, a GPT-4 assisted evaluation method tailored for detailed captioning. Interestingly, while LVLMs demonstrate minimal object existence hallucination in existing VQA benchmarks, our proposed evaluation reveals continued susceptibility to such hallucinations. In this paper, we make the first attempt to investigate and attribute such hallucinations, including image resolution, the language decoder size, and instruction data amount, quality, granularity. Our findings underscore the unwarranted inference when the language description includes details at a finer object granularity than what the vision module can ground or verify, thus inducing hallucination. To control such hallucinations, we further attribute the reliability of captioning to contextual knowledge (involving only contextually grounded objects) and parametric knowledge (containing inferred objects by the model). Thus, we introduce $\textit{HallE-Switch}$, a controllable LVLM in terms of $\textbf{Hall}$ucination in object $\textbf{E}$xistence. HallE-Switch can condition the captioning to shift between (i) exclusively depicting contextual knowledge for grounded objects and (ii) blending it with parametric knowledge to imagine inferred objects. Our method reduces hallucination by 44\% compared to LLaVA$_{7B}$ and maintains the same object coverage.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of object hallucination in large vision-language models detailed captioning. First, the authors quantify the degree of object hallucination by varying model size, fine-tuning data size, image resolution, etc. Second, they proposed two methods, namely (1) modifying the caption training data to distinguish contextual object vs parametric object; (2) adding a layer that acts as a switch between contextual knowledge and parametric knowledge. The proposed methods outperforms baseline on CCEval benchmark.

### Strengths
- Addressed a very timely topic of object hallucination in large vision-language models.
- Interpreting the objects using contextual/parametric knowledge framework seems novel.
- Showed results on multiple architectures, model scales, amount of fine-tune data, which are valuable findings to the community's future research.

### Weaknesses
 - Presentation needs polishing. The paper is very dense in text and requires some effort for reading.  Also, please address the points in "Questions" section.
- The first part and second part of the paper looks more like two separate and condensed papers. Due to this problem, especially the first part fails to deepen our insight about the root cause of the problem. I would expect a deeper treatment on each part.
- Results are mostly quantitative. It would be better to show more qualitative examples of hallucination.

### Questions
I'm generally happy with this submission and think it is above the acceptance bar. Readers could appreciate this work better if the presentation is improved. Please answer the following minor points.

1. In page 4, how are "consistent constraints" enforced? Please explain in detail.
2. Section 3.2 is not very clear to me. Does W correspond to "Projector" in Fig 2? According to Fig 2, W comes after LLM. However, equation   says the opposite. Is the epsilon parameter applied on word-by-word basis or sentence-by-sentence basis? 
I may have misunderstood something because I'm not familiar with the LM-Switch work. Regardless, I believe a good paper should be self-contained and can be readable to general audience in the community.
3. In page 2, object relationship hallucination is mentioned but this concept does not seem to appear again later pages, in metrics or methods presented in the paper. Did I misunderstood?
4. Do you observe any downsides or limitations of using this method that were not expressed in the result Table?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To tackle the hallucination, the authors introduce CCEval, a novel evaluation method assisted by GPT-4, specifically designed for assessing detailed captioning. Surprisingly, the study reveals that LVLMs exhibit minimal object existence hallucinations in existing Visual Question Answering (VQA) benchmarks. However, the proposed evaluation method exposes continued susceptibility to such hallucinations.

The paper delves into the investigation of these hallucinations and attributes them to various factors, including image resolution, the size of the language decoder, and the quantity, quality, and granularity of instruction data. One of the key findings highlights that hallucinations often occur when the language description includes finer object granularity than what the vision module can ground or verify, leading to unwarranted inferences.

To mitigate these hallucinations, the authors introduce HallE-Switch, a controllable LVLM that addresses object existence hallucinations. This novel approach allows captioning to shift between two modes: (i) exclusively depicting contextual knowledge for grounded objects and (ii) blending contextual knowledge with parametric knowledge to imagine inferred objects. HallE-Switch significantly reduces hallucinations, with a 44% reduction compared to the previous model LLaVA7B, while maintaining the same level of object coverage.

In summary, the paper introduces a new evaluation method, identifies factors contributing to object existence hallucinations in LVLMs, and presents HallE-Switch, a solution that effectively reduces hallucinations in detailed captioning without compromising object coverage. This research contributes to improving the reliability and accuracy of large vision-language models in fine-grained visual description tasks.

### Strengths
1.The paper is well-motivated and well designed
2. The proposed method is easy to follow

### Weaknesses
1. Some related methods have not been reviewed, such as ``Evaluation and Analysis of Hallucination in Large Vision-Language Models''

### Questions
na

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper analyzed the cause of hallucination in large vision-language models through the direction of the sizes of large language model, data volume, and input image resolution. The paper further proposes a way to control the generation of VLM, by learning a matrix for mode switching.

### Strengths
1. The paper proposes a new benchmark for evaluating hallucination in large vision-language models and analyzes that. Some findings in this paper are interesting and might provide insights for future research.
2. The paper proposes a way to control the hallucination in large vision-language model and obtains improvements on the proposed benchmark.

### Weaknesses
1. The overall story is not very coherent. First, the details of CCEval are not very clearly described. The paper introduces CCEval as a new benchmark for evaluating hallucination, but lacks a thorough explanation of its construction, including the process for selecting images, generating captions, and defining what constitutes a 'hallucinated' object. Then, analysis is conducted on two or three methods with some conclusions drawn. However, the observation mentioned in the paper seems not to have a specific relation with the proposed Hallu-Switch method. The technique is also only evaluated on CCEval, but previous benchmarks are discussed and used in this paper. The reviewer would expect more insights or explanations about why Hallu-Switch works, specifically how the learned matrix $M$ achieves the desired mode switching between parametric and contextual knowledge, and why this is effective for reducing hallucinations.
2. The study mainly focuses on LLaVA and InstructBLIP and draws some conclusions for large vision-language models. It might be better to study more models to verify the findings. The conclusions drawn about the impact of language decoder size, data volume, and input resolution on hallucination are based on experiments with only two models. This raises concerns about the generalizability of these findings to other vision-language models with different architectures and training procedures. It is unclear if the observed trends would hold for models with different vision encoders or language models.
3. There are many typos in sentences that hinders the reading and understanding. The paper needs careful revision to fix these issues.
    1. 'We additionally record **and and** balance the average number of objects and the average length of captions across all cases' in the last third paragraph of page 4
    2. ' We find **infeasible** to comparing object hallucinations is impractical when there is a significant disparity in average sentence length and the number of objects.' in the last fourth paragraph of page 4
    3. Table 4, the second column for CCEval should be 'finetuning data' rather than 'model'
    4. 'The learned M can be regarded as the transformation from a generic word space to the object sensitive word space' in the first paragraph of Sec. 3.2. It seems this describes $W$ rather than $M$
4. Small issue that does not affect the rating. Some LVLMs can also be discussed:
    1. Chatspot: Bootstrapping multimodal llms via precise referring instruction tuning
    2. GPT4RoI: Instruction Tuning Large Language Model on Region-of-Interest
    3. MultiModal-GPT: A Vision and Language Model for Dialogue with Humans

### Questions
1. The paper mainly discusses LLaVA and InstructBLIP; what if more models are analyzed? Do these findings still holds somehow?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyzes object hallucination (generating non-existent objects) in detailed image captioning by large vision-language models (LVLMs). It introduces a new evaluation method called CCEval to specifically assess object existence hallucination in detailed captions. Experiments reveal that even LVLMs with minimal hallucination on VQA-based benchmarks show substantial hallucination when evaluated on CCEval.

The paper conducts an analysis attributing hallucination to factors like language decoder size, training data amount/quality, and input image resolution to the vision encoder. The core issue is misalignment between objects mentioned in the caption versus those grounded by the vision encoder. Objects not grounded form incorrect word associations leading to hallucination.

To control hallucination, the paper presents HallE-Switch - an LVLM that can adjust the extent of hallucination via a control parameter. It is trained on datasets with only grounded objects versus with hallucinated objects marked. At inference, the parameter shifts the model between using solely grounded objects (-1) versus blending in hallucinated ones (+1). This achieves 44% hallucination reduction without impacting object coverage or sentence length.

### Strengths
1. The writing is clear. I like the flow of this paper where analysis of OH is conducted before providing any solutions.
2. The paper has thorough analysis of factors influencing object hallucination using the new evaluation methods.
2. It is novel to control hallucination levels in LVLMs via contextual/parametric knowledge.
3. The proposed solution maintains object coverage and sentence length while reducing hallucination.

### Weaknesses
1. Although it is interesting to argue that not all hallucination is bad, I don't think the authors successfully supported the argument with examples showing when hallucination is beneficial. With that said, more visualizations like example captions may help better explain the hallucination behavior.
2. There could be more specific illustrations on how the training data was generated using GPT-4.
3. Related work section doesn't really provide any useful information connecting existing work and the proposed work. For example, some references are missing such as https://arxiv.org/pdf/2110.01705.pdf.

### Questions
I don't have questions in addition to the points mentioned in the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
