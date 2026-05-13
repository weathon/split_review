# SANER: Annotation-free Societal Attribute Neutralizer for Debiasing CLIP

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Large-scale vision-language models, such as CLIP, are known to contain harmful societal bias regarding protected attributes (\eg, gender and age). In this paper, we aim to address the problems of societal bias in CLIP. Although previous studies have proposed to debias societal bias through adversarial learning or test-time projecting, our comprehensive study of these works identifies two critical limitations: 1) \textit{loss of attribute information} when it is explicitly disclosed in the input and 2) \textit{use of the attribute annotations} during debiasing process. To mitigate societal bias in CLIP and overcome these limitations simultaneously, we introduce a simple-yet-effective debiasing method called \textbf{SANER} (\underline{s}ocietal \underline{a}ttribute \underline{n}eutraliz\underline{er}) that eliminates attribute information from CLIP text features only of \textit{attribute-neutral} descriptions. Experimental results show that SANER, which does not require attribute annotations and preserves original information for \textit{attribute-specific} descriptions, demonstrates superior debiasing ability than the existing methods. 
  \keywords{Societal bias \and CLIP \and Debiasing \and Fairness}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper aims to overcome societal bias present in datasets used to train large scale multi-modal models like CLIP. The authors provide a study of debiasing methods and explain how these struggle with loosing important attribute information, e.g. gender, or depend on attribute annotations which are hard to get and even harder to get in the form of a large diverse dataset. Their contributed method Saner has four components which together aim to remove biases: attribute neutralization, feature modification and attribute annotation free debiasing and regularization losses. The paper compares the results on quite a few tasks such as text-to-image generation, text-to-image retrieval and zero-shot image classification.

### Strengths
The paper is very clearly written. Whenever an uncertainty comes up about a term footnotes help understanding.

The analysis of debiasing techniques is very clearly presented that it could be used for a tutorial. The experimental setup is well done, the evaluation metrics such as measuring the difference between a uniform distribution and a potentially gender biased image generation seems adequate for the task. Showing generated images, i.e. with Stable Diffusion shows also a very immediate practical application of this research.

The figures help understanding of the method even though the caption could be changed to make them more self-complete.

In general, this seems a very well written, easy to understand paper addressing a very current need.

### Weaknesses
The attribute groups will be limited to a specific set of defined attributes, which need to be agreed upon and could be debatable, e.g. "pregnant" (If I understand list C in the appendix correctly). There may also be missed attributes. This does not seem like a big issue but could be one in an adversarial setting. 

In general, the benefits of not needing a annotated dataset with attributes seems to be bought by needing a general list of attributes. This may not be a weakness per se but it would be interesting to either read about it in the limitations or have the author comment on why this is not a limitation.

There are general implementation details about the used architecture but none about the training process. Re-training clip with a loss to keep it's performance while having a re-projection that changes the semantics seems complex. Information about the used GPU would help understand how hard training for 5 epochs is.

Comparison against other state of the art in this small field is limited but understandably so and the author's did a good job re-implementing relevant approaches.

### Questions
- The caption in Figure 2 should contain ideally an explanation of what is seen in the figure. At least a reminder of the loss terms would be helpful to avoid having to jump back and fourth through the paper.

- How does Saner apply to non-binary gender? Does it properly use general pronouns like they?

- Conceptually, it seems hard to draw a line between terms related only to the gender and to the gender and a concept. Should de-biasing replace terms like pregnant? There is no male counterpart of this so replacing it will probably remove important information.

- Is the "multilayer perception" in line 81 supposed to be a multilayer perceptron?

- The definition of a dataset in Line 104 seems odd in the sense that, if a is a protected attribute then this dataset should only contain data with protected attributes. Is that intended? I would imaging the goal is to train on a large dataset which can have samples with protected attributes but not all samples have to have protected attributes?

- One added sentence for 2.2 on how a orthogonal projection is helping debiasing would be helpful for understanding.

- How hard is it to re-train clip? When the semantics are lost the regularization loss may be high. How computationally heavy is it to get to the same or a similar performance level?

- Table 2's caption should probably read "racial bias" and not recial bias.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to address societal biases in large-scale vision-language models, such as CLIP. The authors identify two limitations of existing methods: the loss of attribute information and the reliance on attribute annotations. To overcome these challenges, the authors propose SANER, a simple yet effective debiasing method for CLIP that incorporates attribute neutralization and an annotation-free debiasing loss. Extensive experiments are conducted to verify the method's effectiveness.

### Strengths
- The problems of existing methods are straightforward, and the authors conduct several experiments to verify these phenomena.
- The proposed method has a good performance.
- The experiments are conducted on both text-to-image retrieval and generation tasks.

### Weaknesses
 - Could the authors provide ARL results to verify the loss of attribute information? Besides, do other existing methods, such as Mapper and Prompt tuning-based debiasing, also have the lossing attribute information when debaising?
- Although effective in debiasing CLIP, the proposed method appears ad-hoc for this specific task and lacks major technical contributions, as most components seem to be existing technologies or tricks. Therefore, this paper may not have significant influence or provide broader insights beyond the CLIP-debiasing task.
- Why does adding only contrastive losses have a significantly negative impact on FairFace performance (as shown in Table 7)?
- Is the proposed method only applicable to CLIP? Could the authors test other VLMs to demonstrate its broader effectiveness?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed a CLIP debiasing pipeline that aims to address two existing challenges: 1. loss of attribute information and 2. Dependency on attribute annotations. Specifically, the paper focuses on adjusting the text feature by replacing the protected attributes with attribute-neutral terms and further regularizing the adjusted feature by two reconstruction losses. The pipeline is evaluated on Text-to-Image retrieval and generation tasks.

### Strengths
The two identified challenges, especially the loss of attribute information, sound critical and interesting. It seems like the pipeline only involves lightweight training, as only the debiasing layer is trained. The pipeline is evaluated on two different downstream tasks.

### Weaknesses
1. Although replacing the protected attribute words with an attribute-neutral word is a sound neutralization method, it requires a comprehensive list of the protected attributes (as listed in Appx. C). However, in real practice, and especially in non-binary cases, it will be very hard or nearly impossible to have a complete list. Further, since the "attribute annotation-free debiasing loss" relies on a set of attribute-specific descriptions, creating the attribute-specific descriptions set may lead to some concerns. For example, if the set is created by iterating all possible words and all possible groups (e.g., man, woman, male, female, he, she, etc), then the size of the set will be overlarge and increase the computation complexity. On the other hand, if only one word is selected for each group (e.g., man + female, woman + male), then how to select matching words from groups may also affect the debias performance. Also, is it possible that the generated description may have unmatched text (e.g., A woman/boy is eating salad) or text that has grammar errors (e.g., A he/she is eating salad, according to Appx. C). I would like to see more discussion on the text generation.

2. The proposed pipeline tried to address the challenge by combining the debiasing loss with two extra regularization losses. The debiasing loss tries to place the adjusted feature of the attribute-neutralized text in the middle point of several features of the attribute-specific text, which seems to be fine. However, the regularization losses try to project the attribute-neuralized feature to both text and visual features of an attribute-specific feature, which seems strange. As demonstrated in Figure 2, the input to the "Text encoder" has been neutralized, and the attribute-specific information has been removed. Further, the debiasing layer is also trained to adjust the features to be further neutral. Thus, even there is a residual connection in the "Feature modification" process, the output feature should not contain any information regarding the specific attribute. Then, how is it possible that such a feature can be mapped to either text or visual features that contain specific attribute information to avoid "the loss of attribute information"? Is it possible that the "retained attribute information" is some biased information from the dataset that is implicitly polluted by the regularization loss?

3. For the evaluation of the text-to-image generation, the paper only provides numerical results on debiasing performance and some visualizations but does not provide any image generation imperial results, like FID. Also, only a few SOTA are used as the baseline, which makes the comparison weak. However, this may be understandable as several baselines do not have public implementation, and it seems like the paper prepares all the baseline results.

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
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a method for finetuning a CLIP model to remove social bias by an intuitive training scheme.

### Strengths
I will start off by saying that the lede of the paper was buried: section 5 as an experiment is astounding. I absolutely love the drag and drop replacement of this debiased model into an existing model. The idea that, 1. you don't have to retrain the text-to-image model and 2. that you don't have to retrain CLIP from scratch is incredibly compelling. I recommend the abstract/intro be rewritten to highlight this experiment.

On another note, the paper is generally well-written and easy to follow. The problem of bias in VLMs is highly prominent and this work makes an excellent contribution to the field. I am fairly familiar with this field of debiasing clip and I feel section 2.1 does a good job summarizing the various papers.

### Weaknesses
I don't have too many issues with the paper. One thing I would like to have seen is a more automated method for text neutralization. While word level ablation is intuitive and makes sense for the social bias angle, a less hardcoded approach seems like it would be needed for a general-purpose debiasing solution, especially for concepts that are hard to ablate at the word level.

There's a dataset called FACET that addresses some issues with PATA and FairFace. If there's time, it would be great to run experiments on it as well. This would cement the proposed method as useful and cutting edge in my opinion.

### Questions
Have you considered running experiments with LLaVA-like models? I don't think it would be terribly difficult to replace the clip model with the proposed one, run standard llava experiments (there are a few githubs that are easy to setup for such eval), and report the results. As for debiasing experiments, I've seen people use PATA and FairFACE and just look at the next token predicted to get similar scores as the CLIP style. Showing this CLIP replacement method works on text generation as well as image generation would very much increase the impact of the work, in my opinion. However, I realize this experiment may best be left for future work.

### Soundness
3

### Presentation
3

### Contribution
4
