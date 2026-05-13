# Analyzing and Mitigating Object Hallucination in Large Vision-Language Models

- Decision: Accept
- Scores: 5, 6, 8, 6

## Abstract
Large vision-language models (LVLMs) have shown remarkable abilities in understanding visual information with human languages. However, LVLMs still suffer from object hallucination, which is the problem of generating descriptions that include objects that do not actually exist in the images. This can negatively impact many vision-language tasks, such as visual summarization and reasoning. To address this issue, we propose a simple yet powerful algorithm, \textbf{LVLM Hallucination Revisor (\ours)}, to post-hoc rectify object hallucination in LVLMs by reconstructing less hallucinatory descriptions. \ours\ is grounded in a rigorous statistical analysis of the key factors underlying object hallucination, including co-occurrence (the frequent appearance of certain objects alongside others in images), uncertainty (objects with higher uncertainty during LVLM decoding), and object position (hallucination often appears in the later part of the generated text). \ours\ can also be seamlessly integrated with any LVLMs. We evaluate \ours\ on six open-source LVLMs and found it outperforms the previous best approach in
both general object hallucination evaluation metrics, GPT, and human evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper finds three key factors related to object hallucination: co-occurrence, uncertainty, and object position. Based on this, the authors propose LVLM Hallucination Revisor (LURE) to rectify the object hallucination issue in LVLMs. LURE takes text descriptions as input and outputs refined ones. The authors collect a hallucinatory dataset using GPT-3.5 and thereby train the LURE. The experiments evaluate LURE on existing open-source LVLMs and results demonstrate LURE's effectiveness.

### Strengths
1. This paper proposes a framework to address the hallucination of LVLMs, by identifying key factors and training a revisor correspondingly.
2. This paper presents the technical details clearly. Rigorous theoretical derivations are provided as well.
3. This paper conducts extensive experiments and shows the quantitative improvements of LURE.

### Weaknesses
1. The definition of positioning score is not intuitive. Have the authors analyzed the position score distribution under different description lengths? If shorter descriptions yield lower position hallucination, would generating multiple short descriptions and combining them result in a high-quality description?
2. Lack of results of other popular benchmarks. This paper only reports the performance on the COCO 2014 test dataset, which is small and may be biased. There is no result about the performance on other popular benchmarks for LVLMs, such as MMBench, MME, POPE, SEED, MM-Vet, etc. Will the performances be better or worse on these benchmarks?
3. Lack of an analysis of the complexity and usefulness of the responses. There is a tradeoff between the correctness and complexity of the responses. Directly removing the hallucination context may improve the correctness but reduce the diversity and complexity. An analysis regarding this concern is important for a comprehensive understanding of the impact of the proposed method.

### Questions
The results of Figure 1(c). Is this quantity of images (just 200) sufficient to consolidate the distribution statistics? And even if a sufficient number of samples are provided in a specific domain, can this conclusion be generalized to the distribution of other datasets or benchmarks?

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a simple algorithm, LVLM Hallucination Revisor (LURE), to post-hoc rectify object hallucination in LVLMs. Their reported results demonstrate that LURE can significantly reduce object hallucination under general object hallucination evaluation metrics.

### Strengths
- The paper compares hallucinatory and non-hallucinatory captions from three critical viewpoints, including co-occurrence, uncertainty, and object position. This viewpoint though simple, is instructive.
- LURE is a lightweight and effective post-hoc method, which achieves reasonable performance on six open-source LVLMs.
- LURE consistently improves its performance compared to the original description, which shows its robustness under different backbones.

### Weaknesses
- The authors' introduction of their training dataset appears to be insufficiently detailed in certain areas. Firstly, the dataset's composition is not entirely clear, especially concerning the proportion of hallucinated content within it. Secondly, during the training of the hallucination revisor, they used 5,000 image-text pairs from the LLaVA-150k dataset randomly. However, the study does not provide adequate experimental backing to validate the adequacy of this sample size for their objectives. It would be beneficial if the authors could offer a more comprehensive description of their dataset, and ideally make it open-sourced. Such an act could serve as an added contribution to their work. Furthermore, the LURE methodology, as presented, comes across as somewhat straightforward, lacking a distinctive innovative edge.
- LURE is designed as a post-hoc solution aimed at addressing object hallucination; however, it doesn't directly confront the underlying causes of the issue. A more direct challenge would be formulating strategies for guiding the LVLM to produce answers with reduced hallucination tendencies.
- Lack of comparing LURE's performance on the fine-grained caption and concise caption. Intuitively, the problem of hallucination would be more common in fine-grained captions.

### Questions
- The effect of object position on object hallucination is not clear. I am still confused why hallucination occurs in the latter part of the descriptions. Is it possible to fundamentally reduce LVLM hallucination from this perspective.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes LURE, a post-hoc approach to reduce object hallucination in large vision-language models (LVLMs). LURE is grounded in a statistical analysis revealing co-occurrence, uncertainty, and object position as key factors causing hallucination. Experiments show LURE outperforms prior methods in reducing hallucination across multiple LVLMs according to general metrics, GPT evaluation, and human evaluation.

### Strengths
1. The paper focus on an important problem, object hallucinations in large vision-language models. 
2. It spots three key factors of the object hallucinations, the co-occurrence, uncertainty, and object positions.
3. The paper proposes a new post-hoc method to reduce object hallucinations of LVLMs. Extensive experiments verify the effectiveness of proposed methods.

### Weaknesses
1.The proposed method helps improve performance on object hallucinations. However, there is a concern that it may harm performance on other metrics like creativity and completeness of captions. It seems to replace detailed words with coarse words as shown in Fig 8.
2.It is unclear if the removed objects are truly hallucinated or if it wrongly removes some non-hallucinated objects. A new metric to quantify this would be helpful.

### Questions
1.Do the authors think image captioning metrics are good metrics for LVLMs? The BLEU scores seem low compared to image captioning models. Some important metrics like METEOR, ROUGE, CIDER, and SPICE are missing in Table 10.
2.Why were co-occurrence, uncertainty, and object positions identified as the three key factors for object hallucinations? Were other factors investigated?

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
This paper studies the problem of object hallucination in large vision and language models. They first analyze the patterns and relations between object hallucinations and three concepts. Then, they provide theoretical analysis and explanation for the observations. Based on the analysis, they create a dataset for training a caption revising model to mitigate the hallucination in captions. The experiment results show that the caption after revising has fewer object hallucinations than the original caption generated by LVLMs and outperforms several baselines.

### Strengths
1. The paper conducts an early study on the caption object hallucination problem of LVLMs and provides some analysis, observations, and theoretical analysis on object hallucination. The findings are meaningful to future research. 
2. Based on the analysis, the paper proposes a simple and effective method to mitigate caption object hallucination by training a caption revising model.
3. The paper tests the proposed method on multiple LVLMs and different metrics and compares it with different baselines. The results validate the effectiveness of the proposed method.

### Weaknesses
1. The study and the proposed method are limited to caption hallucination problems, and seem not generalized to other settings like VQA.
2. Both the training data of the hallucination revisor and the testing data are from COCO datasets. Whether the proposed method can be generalized to new datasets with object labels needs to be validated.

### Questions
The reviewer has some questions on the theoretical analysis part: 
1. In the analysis of **Co-occurrence**, can the authors please explain what is the meaning and why $fˆ_{2} = ⟨ϕ_{1}(s<i, x), βˆ_{1}⟩+⟨ϕ_{2}(s<i, x), βˆ_{2}⟩$? (which means that $fˆ_{2} = fˆ_{1}+⟨ϕ_{2}(s<i, x), βˆ_{2}⟩$)
2. The reviewer understands how the proposed methods related to the three observations on the object hallucinations. However, the reviewer doesn't see a clear connection between the theoretical analysis and the proposed methods. Can the authors explain this point?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
