# Robust multimodal models have outlier features and encode more concepts

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
What distinguishes robust models from non-robust ones?  This question has gained traction with the appearance of large-scale multimodal models, such as CLIP. These models have demonstrated unprecedented robustness with respect to natural distribution shifts. While it has been shown that such differences in robustness can be traced back to differences in training data, so far it is not known what that translates to in terms of what the model has learned. In this work, we bridge this gap by probing the representation spaces of 12 robust multimodal models with various backbones (ResNets and ViTs) and pretraining sets (OpenAI, LAION-400M, LAION-2B, YFCC15M, CC12M and DataComp). We find two signatures of robustness in the representation spaces of these models: (1) Robust models exhibit outlier features characterized by their activations, with some being several orders of magnitude above average. These outlier features induce privileged directions in the model's representation space. We demonstrate that these privileged directions explain most of the predictive power of the model by pruning up to $80 \\%$ of the least important representation space directions without negative impacts on model accuracy and robustness; (2) Robust models encode substantially more concepts in their representation space. While this superposition of concepts allows robust models to store much information, it also results in highly polysemantic features, which makes their interpretation challenging. We discuss how these insights pave the way for future research in various fields, such as model pruning and mechanistic interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the features learned by robust multimodal models. This paper explores the concept of robustness in multimodal models, specifically looking at the differences between robust and non-robust models and uncovering two signatures of robustness in the representation spaces of these models. The authors find that robust models have outlier features, which are highly activated components of the representation space. These outlier features induce privileged directions in the representation space, which are important for the model's performance. The authors also find that robust models encode more unique concepts than less robust models. This leads to polysemy, where a single representation can be used to represent multiple concepts. Additionally, they demonstrate that privileged directions in the model's representation space explain the model's predictive power. The paper analyzes multiple robust multimodal models trained on various pretraining sets and backbones. Overall, this paper provides valuable insights into the nature of robustness in multimodal models and sheds light on the factors that contribute to their success.

### Strengths
1. This paper makes a significant contribution to the field of multimodal models by uncovering two signatures of robustness in the representation spaces of these models. This is a novel approach that has not been explored in previous research. It provides a new understanding of the features that make robust multimodal models robust. The authors identify two key features: outlier features and privileged directions. Outlier features are highly activated components of the representation space, while privileged directions are directions that are important for the model's performance. The authors show that both of these features are more prevalent in robust models than in less robust models.

2. The authors analyze different robust multimodal models trained on various pretraining sets and backbones, providing a comprehensive and rigorous analysis of the factors that contribute to robustness in these models. The paper uses a variety of methods to validate its findings. In addition to using activation kurtosis and singular value decomposition (SVD) to identify outlier features and privileged directions, the authors also use concept probing to show that robust models encode more unique concepts. This provides strong evidence that the authors' findings are not just artifacts of the specific methods they used.

3. The findings of this paper have practical implications for the development of robust multimodal models. The authors demonstrate that outlier features and privileged directions in the model's representation space are key factors in the model's success, which can inform the development of more robust models in the future. The authors' identification of outlier features and privileged directions suggests that these features should be preserved in model training. This could be done by using training objectives that encourage the model to learn these features, or by using regularization techniques to prevent the model from overfitting to the training data.

### Weaknesses
1. The paper only analyzes CLIP robust multimodal models with different backbones, which may not be representative of all possible models. This limits the generalizability of the findings. There are many other large scale multimodal models, which should be included, i.e., BLIP [1], FLAVA [2]. The analysis should be extended to models with different architectures and training procedures to ensure the observed phenomena are not specific to the CLIP family of models. For example, models like ALBEF or even those using transformer encoders instead of vision transformers should be considered.

2. The paper only focuses on robust models and does not compare them to non-robust models. This makes it difficult to determine the extent to which the findings are specific to robust models. It is crucial to include a comparative analysis with models that are explicitly trained for standard accuracy rather than robustness. Without this comparison, it's unclear if the identified features are truly indicative of robustness or just general properties of large-scale models. The paper needs to define what constitutes a non-robust model and provide a clear rationale for the selection of comparison models. The current comparison to ImageNet supervised models is not sufficient, as these are not multimodal models.

3. Lack of explanation of outlier features: While the paper identifies outlier features as a key factor in robustness, it does not provide a clear explanation of what these features are or how they contribute to robustness. The paper should provide a more detailed analysis of the nature of these outlier features, including their semantic meaning and how they relate to the model's predictions. While the paper does discuss the practical implications of the findings, it could have gone into more detail about how these findings can be applied in practice to develop more robust multimodal models, i.e., VK-OOD [3]

### Questions
1. What are the two signatures of robustness in the representation spaces of multimodal models, and how do they contribute to the models' success?

2. How do outlier features in robust multimodal models differ from those in non-robust models, and what is their role in robustness?

3. What are privileged directions in the model's representation space, and how do they explain the model's predictive power?

4. In Figure 1, what are baseline models and baseline models fit training on? Directly from ImageNet? How can this accuracy compare with the multimodal fine-tuning ones?

5. Figure 2 is a little bit hard to read and understand. The authors should present and well-explain the figures clearly.

6. Why only use kurtosis value to determine outlier features? The model of reference work has different number of parameters, how did authors choose the same one as their work?

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
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper demonstrates the existence of outlier features and the substantial encoding of multiple concepts in robust models through the study of models like CLIP.

### Strengths
This paper provides a systematic investigation of models like CLIP, offering compelling evidence that robust models encode outlier features and a greater variety of concepts. This research is quite interesting.

### Weaknesses
1, This paper appears to explain some interesting phenomena but doesn't offer methods for improving model performance. Therefore, I believe the contributions of this research may be relatively limited. As a result, I consider the overall quality of the paper to be at a borderline level.

2, I believe what might be more interesting is understanding why these phenomena occur rather than merely showcasing them.

3, I might have been more eager for the authors to utilize the findings in this paper to inspire some ideas for addressing unresolved problems.

### Questions
See Weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper empirically showed that robust multimodal models have outlier features and these outlier features encode more concepts. The paper analyzed the representation spaces of various multimodal models and found that more robust models have much more outlier features. What’s more, by probing these outlier features of robust multimodal models, the authors find that the principled directions in them encode substantially more concepts.

### Strengths
1. The paper is tackling an important problem in understanding robust multimodal models. Multimodal models are often found to be more robust than prior supervised models. It is not clear why that is the case. This paper provides many intriguing evidences for this observation.  
2. The finding that robust multi-modals have more outlier features is interesting. It is another evidence that zero-shot CLIP models are much different than other non-robust models.  
3. The analysis of the paper is thorough, including using activation kurtosis to analzye outlier features and also the use of concept probing.

### Weaknesses
 1. It is not clear to the me, what is the reason for selecting the metric of activation kurtosis for the analysis in Section 3. What makes this metric interesting for the analysis of outlier features?   
2. It seems section 2 is an re-evaluation of existing works on effective robustness. It would be good to summarize these results and definitions in a concise fashion.

### Questions
1. In table 2, why would the kurtosis of OpenAI CLIP models be much higher? It seems to be an extreme value. I am interested as to what would be the difference between OpenAI and YFCC-15M/CC-12M CLIP models.  
2. From equation 3, the definition of privileged directions in representation space seems to be based on SVD decomposition of the classification head. Have the authors tried more involved methods, e.g. reduced rank regression? Instead of finding the low-rank approximation of W, reduced rank regression would find the low-rank approximation of WX.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The goal of this paper is to characterize CLIP-style models in terms of their weights and hidden representations. This is motivated by these model’s superior generalization ability, which suggests that their internal representations are qualitatively different than smaller models trained on less data. The work finds that robust models exhibit outlier features, that is, individual neuron activations with significantly higher magnitude than the average. The work also tries to quantify the number of distinct concepts that these models learn (relative to models either finetuned or trained from scratch on ImageNet), with results suggesting that models with CLIP-training on large datasets learn more concepts.

### Strengths
- **Motivation:** As greater and greater resources are poured into training frontier models, developing an understanding of what makes these models so much more robust than their counterparts trained on smaller datasets becomes a more and more pressing problem. The approach taken by this paper, attempting to characterize robustness, through model structure alone, is promising as a low compute way of assessing the robustness of a model and a starting point to finding a mathematical basis for robustness.  
- **Clarity:** The work is mostly well-written and well-structured. The reviewer particularly appreciated the way that the work summarizes key takeaways in colored boxes that are easy to find. The visualizations and plots were well-thought-out and communicated their information efficiently.
- **A strong premise:** Though the reviewer had some concerns around the way the experiments were run and the conclusions that were drawn from them (see the "Weaknesses" section), the premise is very interesting and feels like a strong avenue for further exploration.

### Weaknesses
 - **Experiments:** From this reviewer’s perspective, the main issues with the paper come from the experiments and the conclusions drawn from these. We outline our concerns below.
    1. **Privileged directions experiment:** This reviewer did not understand how the privileged directions experiment connected with outlier features. To check our understanding, outlier features are a subset of activations that have substantially higher magnitude than the average activation for that input. Privileged directions on the other hand, are (a subset of?) the right singular vectors for the final linear layer. To determine whether a right singular vector $v_i$ is important to the encoder, the cosine similarity between $v_i$ and a sequence of activation vectors is computed and scaled by the corresponding singular value. This is termed the *importance* of $v_i$. It is not clear to the reviewer how ‘importance’ says anything about outlier features. The latter seems to be a property specifically related to the activation (or neuron) basis whereas the former consists of right singular vectors of the weight matrix, which are almost certainly not the activation basis. To be clear, identifying whether activations align with singular vectors with large singular value seems interesting, it just doesn’t seem to be related to outlier features. Perhaps the tool one wants is closer to a measure of sparsity?
    2. **Pruning experiment:** In Section 3, “Pruning non-privileged directions”, the paper notes that one can prune away the smallest 80% of all singular vectors without substantial loss of accuracy. This technique is a standard method of finding a low-rank approximation of a matrix and well-studied. For large matrices, it does not seem surprising that the impact on classification is small even when using a low-rank approximation as the data itself can be approximated by a low-dimensional subspace of the ambient space. Furthermore, it is hard to tell if the results are specific to robust models when this technique is not applied to the finetuned and trained from scratch models.
- **Lack of coverage of the multimodal aspect of the models:** Given the title, one would expect that there would be some discussion about how the multimodal aspect of CLIP-type models impacts the results. Surprisingly, this feature was never addressed. This reviewer would suggest either removing the word ‘multimodal’ from the title or adding a section to address this aspect. Further, it would be more precise to say that the work considers CLIP-type models since the experiments focus exclusively on this particular family.
- **Experimental breadth:** Related to the previous point, it would make the work stronger if the results were expanded, either by increasing the breadth of the experiments (more models for instance) or providing some analysis of why we see the phenomena that we do. 

### Nitpicks
- The abstract and introduction use the term *outlier feature* without any explanation. The term is not defined for several pages. While outlier features are known within the interpretability community, for the sake of accessibility, this reviewer would recommend putting at least an informal explanation of what this concept is the first time it is mentioned. 
- It’s possible the reviewer missed it, but it seems that $d_X$ and $d_H$ are never defined in Section 3, “Approach”.
- SVD is a foundational method in linear algebra. As such, there probably isn’t a reason to include (3).  
- The reviewer appreciates the validation of previous work showing trends in effective robustness (ER). It would be good if more papers did these kinds of validation experiments. On the other hand, as space is precious, this reviewer would suggest moving some of the text in this section to the appendix to focus on this work’s contributions. It would seem that the main point the paper needs to make with regard to ER is that CLIP-style models stand-out for their ER relative to the same architectures finetuned on ImageNet or trained from scratch on ImageNet. This could be done more concisely.

### Questions
- Looking at Table 3, one sees that the ImageNet supervised models tend to often have more concepts than some of the finetuned CLIP models. Is there an explanation for why this is?
- Figure 4 suggests that the ViT models tend to share more of the same concepts between training techniques, are there any guesses for why this is?
- This reviewer did not understand the remark “An interesting parallel can be drawn with the work of Bondarenko et al. (2023), which found that outlier features in language models assign most of their mass to separator tokens (such as the end of sentence token).”

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
