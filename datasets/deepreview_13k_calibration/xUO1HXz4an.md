# Negative Label Guided OOD Detection with Pretrained Vision-Language Models

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
\textit{Out-of-distribution} (OOD) detection aims at identifying samples from unknown classes, playing a crucial role in trustworthy models against errors on unexpected inputs.  
Extensive research has been dedicated to exploring OOD detection in the vision modality. 
\emph{Vision-language models} (VLMs) can leverage both textual and visual information for various multi-modal applications, whereas few OOD detection methods take into account information from the text modality. 
In this paper, we propose a novel post hoc OOD detection method, called NegLabel, which takes a vast number of negative labels from extensive corpus databases. We design a novel scheme for the OOD score collaborated with negative labels.
Theoretical analysis helps to understand the mechanism of negative labels. Extensive experiments demonstrate that our method NegLabel achieves state-of-the-art performance on various OOD detection benchmarks and generalizes well on multiple VLM architectures. Furthermore, our method NegLabel exhibits remarkable robustness against diverse domain shifts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a novel method for zero-shot out-of-distribution (OOD) detection, leveraging the capabilities of vision-language models (VLMs). The primary objective is to enhance OOD detection by incorporating textual information. NegLabel introduces a large number of negative labels, extending the label space to distinguish OOD samples more effectively. The method uses a novel scheme for the OOD score, taking into account affinities between images and both ID labels and negative labels. The paper provides a theoretical analysis, justifying the use of negative labels.

### Strengths
- **Well-written and technically sound paper** The paper is well-structured and its concepts and contributions are clearly presented.

- **Quality illustrations**

- **Extensive experiments** The paper conducts extensive experiments, including OOD detection, hard OOD detection, and robustness to domain shifts. 

- **Large and consistent gains compared to several SOTA baselines** The paper's results show substantial improvements over several state-of-the-art (SOTA) baselines. 

- **Intuitive justification and theoretical analysis provided** The paper offers an intuitive justification for the proposed method and includes theoretical analysis to explain the mechanism of negative labels.

- **Extensive ablations**

### Weaknesses
 - **Assumption about CLIP's latent space** The assumption that ID image and corresponding ID label embeddings are close in CLIP's latent space is actually false. The contrastive learning strategy of CLIP is based on cosine similarity and thus textual and visual embeddings are actually on different manifolds see (Weixin Liang et al. 2022) for more details. Using ID labels as proxies for the ID images may thus produce unexpected results. In my understanding, the negative labels are compared to the images using cosine similarity, and thus having them close to ID textual embeddings still makes sense but the authors should be cautious here.

- **Comparison with related work** The method is close in spirit to CLIPN (Wang et al. 2023) as well as ZOC (Esmaeilpour et al 2022). The former fine-tunes CLIP to incorporate negative prompts to assess the probability of a concept not being present in the image. An extensive comparison with CLIPN would be overkill but some discussion about it would be welcome.  The second also performs zero-shot OOD using maximum softmax probability on the labels extended with the object detected in the images. Comparisons with ZOC are presented in the supplementary but would better belong in the main paper IMO as it is one of the few recent zero-shot OOD detection baselines. To be fair this comparison should be provided with the same set-up as in Table 2.

- **Misleading baseline presentation** Even if the MSP, ODIN, or Energy Logit baseline are generally used on models fine-tuned on a downstream task, one could also use these detectors in a zero-shot setting. Classifying them in purely zero-shot can be misleading eg. MCM can be seen as zero-shot MSP on CLIP's output probabilities.

- **Short Related Work** The related work section is relatively short, especially for such a prolific field as OOD detection. I don't think it is really detrimental to the paper but a discussion on the sense of OOD detection for foundation models trained on vast and various data would be welcome.

- **Lack of novelty in OOD scoring**: Upon rereading Fort et al, 2021, I see that the last section is the same as the proposed NegLabel score. It seems that the novelty of NegLabel rather relies on the mining algorithm and the grouping strategy than the OOD scorer itself which is not explicit in the contributions. Comparisons with this baseline would have been appreciated.

### Questions
- I wonder why the authors did not add the simple and strong baseline Mahaloanobis (Lee et al. 2018) /SSD (Sehwag et al. 2022).
- No ablations are provided on $n_g$. How do the authors set this parameter and what is its impact?
- Would the hard OOD detection task be better qualified as Open-Set Recognition?
- Why the comparison with ZOC is performed using ImageNet-200 and not ImageNet-1k as in Table 2? A Homogeneous comparison setup would greatly enhance the paper quality. 

**References**

Lee, K., Lee, K., Lee, H., & Shin, J. (2018). A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks. Advances in Neural Information Processing Systems, 31. 

Sehwag, V., Chiang, M., & Mittal, P. (2022, February 10). SSD: A Unified Framework for Self-Supervised Outlier Detection. International Conference on Learning Representations.

### Soundness
4 excellent

### Presentation
4 excellent

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
This paper is a pioneer work to study the OOD detection problem under VLMs. Compared to state-of-the-art papers in this frontier, this paper addresses several issues that SOTA methods do not cover. These issues are justified well in this paper, and the corresponding explanation is reasonable and solid. Then, a OOD-word selection method and a corresponding score function is proposed to address the observed issues. The proposed method makes sense and works well in the extensive experiments.

### Strengths
1 As a pioneer study in this field, I find that this paper is easy to follow and demonstrates issues of SOTA methods very clearly. Thus, in my point of view, this paper has a great potential to motivate more relevant work in this important field: OOD detection with VLMs/Zero-shot OOD detection.

2 I am convinced that the proposed work has a solid contribution by the extensive experiments conducted by the authors. The experiments cover many scenarios, which is a solid evidence that the proposed method has its own contribution to this field.

3 This paper also benefits from the theoretical understanding of the proposed score function. The analysis is easy to follow and looks totally new to me.

### Weaknesses
1 Figure 1 is clear and important. However, it makes me think about one question: in a statistical view, what should the right subfigure be? Specifically, if the x-axis represents the labels, and the y-axis represents the similarity score, how should the distribution of the similarity scores for negative labels look like? Should they be uniformly distributed, or should they follow a specific distribution given the nature of the negative label selection process? This is unclear and needs more elaboration.

2 In Algorithm 1, the comments are too long. It would be better to say the key functionality of this part. For example, instead of detailing the steps of negative label selection, a high-level description of the purpose of this section would be more helpful. The current comments make it difficult to quickly grasp the overall flow of the algorithm.

3 Why does grouping strategy appear in Section 3.2 instead of 3.1? It seems that Grouping Strategy is a more advanced way to pre-process negative labels? If the grouping strategy is indeed a pre-processing step, it would be more logical to introduce it before the score function. The current placement makes it seem like an afterthought, rather than an integral part of the negative label handling process.

4 Can the authors explain why is the case considered in B.3 more general? While the text mentions that it is more general, it does not provide sufficient intuition or explanation as to why. What specific aspect of real-world data does the Poisson binomial distribution capture that the binomial distribution does not, and why is this crucial for the OOD detection problem?

### Questions
1 Figure 1 is clear and important. However, it makes me think about one question: in a statistical view, what should the right subfigure be?

2 Why does grouping strategy appear in Section 3.2 instead of 3.1? It seems that Grouping Strategy is a more advanced way to pre-process negative labels?

3 Can the authors explain why is the case considered in B.3 more general? More explanation can make readers know your analysis better.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the traditional OOD detection, the text information of labels will be abandoned, which actually loses some information regarding labels. With the assist of VLMs, this kind of information might be useful for OOD detection. The authors present a study aligning with this interesting and new research direction: OOD detection with VLMs. The existing methods are quite on the early stage, and this paper challenges these methods and proposes a new OOD detection method consisting of a negative label selection method and a new score function. Experiments are solid and form a solid contribution to OOD detection with VLMs.

### Strengths
+ Experiments are solid and cover many aspects, which can address many in-the-mind issues
automatically. It is enjoyable to the whole experimental section, which also contains some interesting insights directly from the experiments conducted in this paper.

+ The idea to design the new score function is straightforward after demonstrating an intuitive motivation. The motivation of this paper is supported by some evidence instead of "wording", which appreciated. 

+ The presentation is generally good. The flow is great to follow, and necessary analysis is easy to follow as well.

### Weaknesses
 - OOD detection methods have different performance on different datasets. On some datasets, the performance is extremely good. Can we see the difference among these datasets? Why can OOD detection be easily addressed on some datasets?

- Especially for results based on CLIP-B/16 with various ID datasets, the performance is too high. More explanation is need.

- Figures might be better to illustrate the final performance in Section 4.

- What is the relationship between Bernoulli distribution and binomial distribution? This is a well-known result in statistics?

- Why is B.3 more general than things demonstrated in main context?

- Please keep the naming strategy consistent in Algorithm 1 and other algorithms.

### Questions
In general, this paper addresses a significant problem and makes a solid contribution to this field. However, please answer questions listed in the Weakness:

- OOD detection methods have different performance on different datasets. On some datasets, the performance is extremely good for all methods. Can we see the difference among these datasets? Why can OOD detection be easily addressed on some datasets?

- What is the relationship between Bernoulli distribution and binomial distribution? This is a well-known result in statistics?

- Why is B.3 more general than things demonstrated in main context?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The field of out-of-distribution (OOD) detection seeks to recognize samples originating from unknown classes, thereby ensuring the trustworthiness of models when confronted with unanticipated inputs. While there exists a vast body of research delving into OOD detection within the visual modality, vision-language models (VLMs) stand out by synergizing both textual and visual data for a range of multi-modal tasks. However, there's a noticeable gap, with only a few OOD detection techniques capitalizing on the textual modality. In this study, the authors introduce a groundbreaking post hoc OOD detection technique, termed NegLabel, which harnesses a plethora of negative labels sourced from expansive corpus databases. They meticulously craft an innovative scheme, wherein the OOD score seamlessly collaborates with these negative labels. A detailed theoretical scrutiny aids in unraveling the intricate workings of these negative labels. Rigorous experimentation underscores that their NegLabel approach not only sets new standards in OOD detection benchmarks but also exhibits a laudable adaptability across diverse VLM architectures. Moreover, the NegLabel technique showcases exemplary resilience when faced with various domain shifts.

### Strengths
1 The research topic is very novel and important. There are a few papers focusing on this field. After reviewing this paper and relevant literature, it can be found that this paper moves a solid step to detect OOD samples when VLMs are available. 

2 This paper identifies an important issue of relevant literature: how to select the negative words to improve the OOD detection power. Correspondingly, this paper proposes a novel method to address this important issue, which is a significant contribution in my view. The method's effectiveness is also verified by the extensive experiment.

3 The claims of this paper obtains strong support via extensive experiments that are based on various zero-shot OOD detection benchmarks and multiple VLM architectures.

4 The theoretical understanding starts from the data modelling, which is an elegant way to build up an understanding from the scratch. I am glad to see how the score is built up via a well-motivated data modelling method. The use of the probability tools is very interesting in the field, as we can directly see the distribution.

### Weaknesses
1 In Eq. (5), the cosine similarity is selected. Although the reason is given in the paper, it is still interesting to see if we can have other choices.

2 I enjoy reading how you move from basic data modelling to a more realistic data modelling in B.3. However, it would be better to point out why the contents in B.3 is more general, which can increase the interests of readers for understanding the proposed score.

3 In Table 2, all methods can obtain good results (AUROC>90% or FPR95<10% in the most cases). I actually do not see the necessarity to put that table in the main content. It would be better to move some interesting parts in Appendix to the main content.

4 What will happen if we select all different words from the ID classes?

### Questions
1 In Table 2, all methods can obtain good results (AUROC>90% or FPR95<10% in the most cases). I actually do not see the necessarity to put that table in the main content. Can we move it to appendix?

2 What will happen if we select all different words from the ID classes?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
