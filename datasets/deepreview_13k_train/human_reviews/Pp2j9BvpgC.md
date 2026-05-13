# Attribute Recognition with Image-Conditioned Prefix Language Modeling

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
Predicting object identity and visual attributes is a fundamental task in many computer vision applications. While large vision-language models such as CLIP had largely solved the task of zero-shot object recognition, zero-shot visual attribute recognition remains challenging because CLIP's contrastively learned language-vision representation does not effectively encode object-attribute dependencies. In this paper, we revisit the problem of attribute recognition and propose a solution using generative prompting, which reformulates attribute recognition as the measurement of the probability of generating a prompt expressing the attribute relation. Unlike contrastive prompting, generative prompting is order-sensitive and designed specifically for downstream object-attribute decomposition. We demonstrate through experiments that generative prompting consistently outperforms contrastive prompting on two visual reasoning datasets, Visual Attribute in the Wild (VAW) and a proposed modified formulation of Visual Genome, which we call Visual Genome Attribute Ranking (VGAR).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work is about rcognizing image attributes through utilizing language models. Some experiments are shown for the results, and compared with other published works.

### Strengths
The use of existing language models for recognizing image attributes is interesting. 

The experimental comparisons are important.

### Weaknesses
In my understanding, the main contribution of the work is the prompt engineering, i.e., designing prompt for accessing large language models, which is interesting and useful, but it is not develping a new mothod to advance the state-of-the-art, from the algorithm or theory viewpoint. Thus if my understanding is correct, the contribution of the paper is not at the level of ICLR.

To my knowledge, there are already some existing companies that work on prompt engineering for a better use of the ChatGPT or other large language models. Thus the prompt engineering is not that new, even from the application point of view.

It could be better if the prompting engineering shown in the work can be combined with some novel algorithm development, the paper might be a better contribution to the ICLR conference.

### Questions
As my concerns shown in the Weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
While large vision-language models like CLIP excel at zero-shot object recognition, they struggle with zero-shot visual attribute recognition due to an inability to effectively encode object-attribute relationships. This paper tackles this challenge by introducing generative prompting. This approach redefines attribute recognition by assessing the likelihood of generating prompts that express the attribute relation. Unlike its counterpart, contrastive prompting, generative prompting is order-sensitive and tailored for object-attribute decomposition. Experimental results reveal that generative prompting surpasses contrastive prompting in performance on two visual reasoning datasets: Visual Attribute in the Wild (VAW) and a newly introduced version of Visual Genome, termed Visual Genome Attribute Ranking (VGAR).
The paper also shows strong performance against SOTA, despite being trained without annotated data.

### Strengths
1. The paper also shows strong performance against SOTA, despite being trained without annotated data.
2. The paper has clear ablations to show the value of their proposed method
3. In general, the key idea of using generative prompting/modeling to solve complex localized reasoning tasks is an interesting direction
4. The VGAR benchmark which unifies object and attribute recognitions, is broadly useful for the community

### Weaknesses
I don't see any major weaknesses in the paper

### Questions
N/A

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
While zero-shot object recognition has largely been solved by large language-vision models such as CLIP, visual attribute recognition remains challenging because CLIP’s contrastively learned representations do not effectively encode object-attribute dependencies. 
In this paper, the authors revisit the problem of attribute classification and propose a solution using generative prompting, which revolves around a strategy for measuring the probability of generating prompts. 
Unlike contrastive prompting, generative prompting is order-sensitive, and its design reflects the downstream requirements of object-attribute decomposition. 
The authors demonstrate through experiments that generative prompting outperforms contrastive prompting on two datasets that require visual reasoning, Visual Attribute in the Wild (VAW), and a modified formulation of Visual Genome (VGAR).

### Strengths
- The proposed method is easy to understand.
- In terms of attribute recognition research. The proposed approach with generative prompting seems new.

### Weaknesses
 - As a machine learning research, the technical significance and novelty seem weak. This work looks like a simple prompt engineering paper to me. To claim the technical significance, the authors should try with more various prompts and compare the results.

- Also, as the main contribution of this paper is to replace contrastive prompting with generative prompting for attribute recognition, the authors should provide a theoretical explanation of why generative prompting is better than contrastive prompting. Otherwise, the technical contribution might be weak as a machine learning paper.

- The experiment is also weak. In Table 3, the performance of the proposed method is not noticeably better than the baseline models (e.g., TAP).

- Finally, there should be more comprehensive experimental results. For example, how about the result with other LLM models than CoCa? Also, in Tables 4 and 5, why didn’t the authors compare the proposed model with the state-of-the-art methods? Finally, it would be better to evaluate the proposed method on other attribute recognition datasets, such as UTZappos or MIT datasets, or HOI detection datasets, such as HICO or V-COCO datasets.

### Questions
Please refer to the questions in the weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed an image captioning way to address object attribute recognition and object-attribute compositional learning. Given the limitations of previous methods like the CLIP-based method, the authors proposed a generative prompting method to solve both the classification and compositional learning problems. On two datasets, the proposed method was compared with recent works and showed improvements.

### Strengths
+ Given the current development in LLM, using the captioning solution to address the visual understanding is non-trivial. This work used a general pipeline to address a classical visual relation and recognition problem.

+ The discussion about the CLIP-based works makes sense.

### Weaknesses
 - Though the solution is sound according to the new development tendency, I do not find too many new insights and "surprising" parts. There are many works using captioning via LLM to solve nearly all other directions in visual understanding, e.g., action/object recognition, visual relationship understanding, VQA, etc. Please give a discussion covering more domains to analyze the contribution.

- Compositional learning and its zero-shot setting (CZSL) is challenging with previous paradigms given the fixed train and test sets. Now, we have huge datasets like LAION and many other datasets beyond images like text. More discussion or insights about the new weapons and the CZSL would be a better contribution. 

- Though previous non-LLM works are "old", they can still be used as the baselines.

- The method part is kinda of too brief.

- More experiments on more datasets would be more solid to support the claims.

- typo: many wrong quotation marks ”xx”.

- some weird green boxes appeared.

### Questions
- Using huge LAION, then the fairness consideration in the experiments?

- Detailed analysis of the long-tailed distribution and results?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
