# Interpretable Concept Discovery and Learning from Pretrained Vision-Language Models

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
Vision-language models (VLMs) pretrained on web-scale data excel at recognizing complex visual objects. However, it remains mysterious if and how the VLMs learn and utilize rich semantic information of visual concepts, such as colors and shapes, for recognition. While some prior work concluded that pretrained VLMs do not capture interpretable concepts, other work observed that leveraging the concept-based text prompts improves visual recognition accuracy, and appears to offer some degree of interpretability. In this paper, we aim to address this discrepancy and understand pretrained VLMs' true capability of encoding interpretable visual concepts. We identify that the discrepancies on concept definition and concept prompting (class-conditioned or class-agnostic) lead to different observations in prior works, and (class-conditioned) concept prompts that provide discriminative information for visual recognition are often not interpretable. To address these challenges, we propose a new framework to jointly discover and learn interpretable visual concepts from pretrained VLMs. Our discovered concepts are class-agnostic, and selected based on the visual discriminability as measured by mutual information between images and concepts. We then propose a self-supervised framework to efficiently fine-tune a VLM to better recognize the discovered concepts. Through extensive quantitative and human evaluations, we demonstrate that our concept discovery and learning (CDL) framework significantly improves the interpretability of the discovered concepts, while achieving state-of-the-art performance on concept-based visual recognition. All code and data related to this paper will be made public.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a  framework to jointly discover and learn interpretable visual concepts from pretrained VLMs.  The authors claim that the discovered concepts are class-agnostic, and selected based on the visual discriminability measured by mutual information between images and concepts. 
Besides this, the authors propose a self-supervised framework to adapt the CLIP models to recognize the discovered concepts. Experiments on several datasets show these concepts are helpful for understanding CLIP models.

### Strengths
+ easy to follow and implement
+ clear figures for readers to understand
+ present experiments on multiple datasets.

### Weaknesses
The technical novelty. The overall framework aims to decompose an existing class name into basic visual concepts and then compose them into a semantic verb for final supervision. This structure seems to be trivial and does not provide us with many insights. The ranking for concepts simply borrows the definition of mutual information as Eq.(3). The reviewers doubt the overall novelty of this framework and the contributions seem to be weak.

The experimental results somehow do not support the overall idea. From Tab.1 using concepts provides little performance improvements. Specifically, the reported gains are marginal and do not justify the complexity of the proposed approach. In Tab.2, boosting the concepts from 1000 to 2000 provides only 0.1% improvements on the public imageNet dataset. This minimal improvement suggests that the concept space is not being effectively utilized, or that the selected concepts are not sufficiently discriminative. The experimental results do not fully support the proposed contributions.

The overall presentations and organizations are not well exhibited. The paper is somehow not easy to follow the key idea and many insights behind the simple language concepts are not clearly explored. The reviewers suggest the authors further explore the semantic concepts or some hidden contextual information rather than this simple architecture.

### Questions
Please refer to the weakness section above. Considering its overall quality, I tend to give a negative score.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The study delves into Vision-Language Models (VLMs), specifically models like CLIP, and their proficiency in discerning and utilizing visual concepts such as colors and shapes for multi-modal recognition. Past research offers mixed views: some findings suggest VLMs might lack in interpretability, while others indicate that concept-based text prompts can enhance recognition and offer some degree of interpretability. This paper attributes these discrepancies to varied concept definitions and prompting methods among prior works. To address this, a novel framework is introduced to extract and learn interpretable, class-agnostic visual concepts from pretrained VLMs. These concepts are selected based on their visual distinctiveness, evaluated through mutual information between the images and the concepts. A self-supervised approach is then proposed to refine the VLM's recognition capabilities of these concepts. Results, supported by extensive quantitative and human evaluations, confirm that this approach not only bolsters interpretability but also enhances recognition accuracy.

### Strengths
The idea is reasonable and contributes to the interpretability. Experimental results also support that the proposed approach outperforms the baselines.

### Weaknesses
1. This paper found out that the classification accuracy drops significantly when the input prompt for the text encoder is without the class name. However, not using the class names may not be a large problem. The key concept of using CLIP is based on the contrastive learning between image-text pairs, which is powerful. As such, it is reasonable that the class names associated with the descriptions improvement the classification. Moreover, the model with class names can provide the correct description, e.g., the examples in Fig. 1.
2. The method for alleviating the problem is to use different prompts, e.g., “What are useful visual features for distinguishing a {category name} in a photo?,” which is heuristic. Another alternatives should be considered and compared.
3. The experiments should follow the similar setting with previous work. It is suggested to compare with VDES (and following works) and show the results with different backbones.
4. The references are out-of-date. Only two papers published in 2023 are cited. Moreover, VDES is published in ICLR 2023, while the reference in the paper is still an arxiv paper.

### Questions
It is suggested to provide a little bit more details about previous work (Menon & Vondrick, 2022) to improve the readability.

### Soundness
3 good

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
This paper proposes a concept discovery and learning (CDL) framework aiming to better align the semantic representation for a category label and its relevant attribute labels. It is inspired by an observation that in current visual-language models (VLM), there are inconsistencies between class labels and the attributes.

To mitigate such inconsistency, given a category label (e.g., a panda), CDL queries a large language model (LLM) about useful visual features that helps recognition of that category. This process results in a concept-class corelation matrix. A mutual information inspired method is then used to obtain the most informative concepts for a specific class. In the end, each class will correspond to a 0-1 vector indicating whether a concept is useful for that class. The obtained concept vectors are then used to finetune the last projection layer of CLIP. Through this process, the paper claims that CDL helps visual-language model learn a better correspondence between class labels and the attributes.

Experimental studies on ImageNet, Food-101, CIFAR-100, and a few smaller datasets were conducted to show the efficacy of the proposed method. A human study on the interpretability of the CDL framework is also provided.

### Strengths
- The paper is technically and intuitively correct.
- Extensive experiments on different image datasets and human study about interpretability are conducted.

### Weaknesses
 - Table 1 is used as a support of the paper's claim about the misalignment of concepts and classes in CLIP. However, there is not a similar table for CLIP+CDL using the same evaluation to show that it does improve the alignment between classes and concepts. Current experiments only show that VLM+CDL becomes a good concept detector but does not say that it effectively relates concepts with classes.
- Mutual information-based concept selection is correct but not new. Moreover, I do not see the necessity of introducing MI here. The paper should better rationalise the choice of this criterion.
    * How does using MI differ from using the normalised cooccurrence frequency between categories and classes?
    * Is there any example showing the concepts selected for different classes?
- Missing details about the similarity threshold ``$\texttt{th}$'' (page 5). There is no further discussion on it except in Section 3.2.
    * What is the typical value for it?
    * Is the parameter fixed for all the datasets?
    * Is the framework sensitive to this parameter?
- Missing details about human study.
    * There are no error bars in Figure 4, making it difficult to tell how well the human annotators agree and how significantly CDL improved over prior methods. Since each data point has been annotated by three human annotators (as described in the appendix), there should be at least an error bar for each result in the figure.
    * Moreover, there is no information about the interface viewed by the annotators. For example, Are samples fairly displayed to the annotators, removing the possible bias caused by the order or the position of display?
- Clarity: what is the "CDL+CDL" setting in Table 2?
- Typo: "directlyed" in page 2.

### Questions
Please see my points above. As a summary, I expect answers regarding:
1. Does VLM trained with CDL really better models the relation between concepts and classes?
2. MI for concept selection is good, but why bother using it here? Any ablation study about it?
3. Missing details about model design, for example the similarity threshold $\texttt{th}$.
4. Missing details about human study, for example the error bars.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
