# Actions-to-Action: Inductive Attention for Egocentric Video Action Anticipation

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 6, 3, 3, 5

## Abstract
Video action anticipation is a specific field within computer vision that diverges from action recognition, requiring the prediction of future actions through the analysis of historical video sequences. This paper unveils an innovative model designed to overcome the limitations of existing solutions by amalgamating recurrent and attention mechanisms, taking cues from the principles of object tracking. Notably, our model leverages prior anticipation results, enabling a nuanced interpretation of semantic transitions between actions and recognizing the uncertainty inherent in predicting future events. This strategy strikes a balance between computational efficiency and judicious data utilization, challenging the assumptions prevalent in current transformer models and thereby underlining its practicality for real-world applications. Distinctively, our model discerns temporal connection from abstract concepts in a way that mirrors human reasoning and adopts a recurrent structure to thoroughly capture video context. Extensive experiments conducted on EPIC-Kitchens-100, EPIC-Kitchens-55, and EGTEA Gaze+ confirm the superior performance of our proposed model and efficiency compared to established transformer architectures. Remarkably, it surpasses most multi-modality models using only RGB visual inputs, showcasing its exceptional generalization capabilities across a variety of unseen test sets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper produces an Inductive Attention Model (IAM) for egocentric video action anticipation. The model melds recurrent and attention
mechanisms to explicitly employ prior anticipation results to refine subsequent action predictions. This design allows the model to form higher-order recurrent states and make current predictions based on extended historical data. Experiment results on several action anticipation datasets show that the proposed model surpasses most multi-modality models using only RGB visual inputs, showing the effectiveness of the proposed method.

### Strengths
1. The proposed IAM architecture utilizes prior predictions as part of the attention mechanism. This allows for the aggregation of higher-order recurrent states, which is an advancement over traditional first-order recurrent models.
2. IAM achieves competitive performance on several datasets with relatively fewer parameters.
3. IAM achieves better performance on unseen classes on EK100, indicating good generalizability.

### Weaknesses
1. In Table 6, the ablation study shows that one of the major designs of this paper (predictions as prior) doesn't play a major role in the final performance improvement. The performance improvement is highly attributed to some design choices like a better backbone and class weighting.
2.  Lack of analysis and visualization of the proposed mechanism. For example, how do previous predictions affect future action anticipation? Specifically, it is unclear how the attention weights are influenced by the prior predictions and how this impacts the final action classification. The paper does not provide any examples of attention maps or visualizations that would help understand this process.
3. Is the proposed model able to also handle the long-term action anticipation tasks (i.e. predicting multiple future actions) defined in Ego4D (grauman2022ego4d) and EgoTOPO (nagarajan2020ego). The current evaluation is limited to short-term anticipation, and it's unclear if the proposed inductive attention mechanism can effectively capture long-range temporal dependencies.

### Questions
See weakness section

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Paper proposes a novel method which utilizes multiple S past actions anticipation results to improve the next action anticipation. Extensive experiments on 3 datasets and several analytic experiments on proposed model performance were conducted. Empirical results show competitive results against other State of The Arts approaches.

### Strengths
1. Paper's motivations are clear and the proposed method is explained in sufficient details.
2. Quality of experiment designs and analysis are excellent.
3. Novelty/originality is good within the context of action anticipation.

### Weaknesses
1. Originality is somewhat limited as using prior predictions to condition the target prediction has been applied to other problems. See reference
2. The choice of egocentric action anticipation problem for the proposed method is not well motivated. There is no inherent advantage of the proposed method for egocentric action anticipation, compared to other video prediction problems, e.g. physical interaction/dynamics, 3PV action anticipation, gaze anticipation/prediction etc.
3. Significance is average. While the problem of action anticipation is interesting, it is not clear how the proposed method can be applied to other related problems.

### Questions
1. Please explain the motivation for applying the proposed technique to egocentric videos only. There is no clear reason why the proposed method cannot be applied to other video prediction tasks, e.g. 3rd person videos, physics interactions, gaze prediction etc.

2. I will be interested to see the results comparison for S=1.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an approach for egocentric action anticipation by introducing an inductive attention module. This module is helpful in capturing longer, temporal, history information and resolves the forgetting nature of recurrent neural data by using a higher order information. For the inductive attention, the last/previous prediction is compressed using a learnable compression function and used as query. The before/history predictions are also compressed and used as key and the history recurrent states are used as value. The frame feature and the inductive attention value are aggregated together to form the current recurrent state. The method is evaluated on three datasets - Epic-kitchens-100, Epic-kitchens-55, EGTEA Gaze+

### Strengths
The quantitative results are quite exhaustive and the results are shown on three egocentric datasets for action anticipation.

### Weaknesses
It seems that the technical contribution of the work is weak. While the motivation of adding longer, temporal history is appreciated, the inductive attention module itself does not yield much improvement for the task of anticipation and does not provide a strong signal to the model for modelling the long-term, temporal history context. There seems to be less significant improvement in the performance with the inductive attention mechanism module. For example, in Table 1, when comparing Swin-IAM with MeMViT 32x3 there is only a performance improvement of 0.4% on actions, almost none on verbs, and 0.2% on nouns.

### Questions
Suggestion: 
1. There can be a grammar check run on the paper text. For example, the first line of section 3, problem statement can be edited. Additionally, multi-modal and multi-model terms have been used interchangeably in abstract and results table. The last line of the abstract can also be checked - 'multi-modality models using only RGB visual inputs' whereas multi-modal approaches have more modalities than visual input. 

2. The association with object tracking in the introduction and Figure 1 also seems a bit misplaced as it seems for the reader that object tracking would be used for the task of action anticipation, which is not actually used.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces the "Inductive Attention" mechanism, an approach to video action anticipation. Unique in its design, this method employs the class prediction from the prior step as the query for attention. The authors argue that this design allows the model to recognize many-to-many relationships more effectively. Experimental evidence demonstrates that the Inductive Attention model achieves state-of-the-art results on several large-scale datasets, highlighting its efficacy in predicting human actions within video content.

### Strengths
1. The paper reports commendable performance on benchmark datasets.
2. The idea of utilizing the prediction from the previous step as the attention query offers a fresh perspective and holds intrinsic interest.

### Weaknesses
The core contribution of the paper revolves around leveraging the prior prediction as an attention query. It is natural to use the input frame feature, or hidden state as a query, but if using the previous prediction leads to significantly better performance, it would be noteworthy and might have wider applications in related fields. However, the current version of the paper lacks depth in discussing the implications and rationale behind this choice. The proposed method, as presented, may seem like an incremental architectural tweak that provides some improvement in a particular task, significantly limiting its impact. For the authors' assertion that "class probability is a superior choice for attention" to be compelling, it requires a more rigorous justification than what is currently provided. Merely pointing out performance gains does not substantiate this claim sufficiently.

### Questions
Please see the weaknesses section. Is there any experimental evidence that can show the potential expandability of the proposed method to other related CV tasks?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a model for action anticipation based on the integration of attention-based (such as transformers) and auto recurrent (such as LSTM) mechanisms. Differently from previous works, the proposed method takes into account a history of previous hidden states rather than the last one when making predictions, thus relaxing the first-order Markovian assumption usually introduced in recurrent models. The proposed approach is evaluated on the main benchmarks for egocentric action anticipation. Results suggest that the method outperforms competitors when a single RGB modality is considered.

### Strengths
While the model proposes a few modifications to the attention mechanism, this ends up in a novel approach which outperforms previous works.

It is interesting to see that the proposed method works well with context length of up to 30s. This is not common in previous approaches and seems to be a promising direction for better exploiting past history.

### Weaknesses
1) PRESENTATION QUALITY
The quality of paper writing is not always up to standard. Some sentences are a bit overselling, unclear, or not adequate for scientific writing. Some examples:
- “by integrating gaze information within the observed frames”: is the paper referring to a specific work here? As far I know gaze analysis for intention prediction has not been systematically investigated in egocentric vision.
- “Unlike action recognition, which primarily relies on patter recognition”: this statement seems to imply that action anticipation does not rely on pattern recognition, which I don’t think is an accurate statement (neural networks are anyway patter recognition machines)
- “our model can infer causation from abstract concepts”: this statement is a bit overselling and does not seem to be shown/proved in any of the experiments. 
- “our innovative model sets new performance benchmarks”: I do not think this is accurate. It seems that the proposed model outperforms competitors by small margins. I would highlight instead that it may point out to a promising direction for future models.
- in section 3, the set X is later referred to $X_{T-t_s:t}$, which is a bit confusing
- It is not clear how equation (1) is an accurate description of existing methods, whether recurrent or transformer-based. In the equation, it seems that models following this formulation explicitly plug in the last observed action for predicting the future one. However, methods that directly predict future action do not do that (e.g., vanilla LSTMs)
- In eq (2), is $\hat y_i$ a probability or a predicted label?
- Section 5.3.1 “IAM demonstrated notable e enhancement over several formidable baselines”.I would suggest to revise the use of “formidable” in this scientific context.
- Throughout the paper, I could not find a clear motivation for the use of the term “inductive” in “inductive attention”. I think this could be clarified.

This are some examples. Overall, I would suggest a thorough review of the paper to improve presentation.

LITTLE INSIGHT ON WHY THE MODEL WORKS
While I appreciate the description of the model architecture in Eq (11)-(14), there is no discussion as to why the introduced modifications are adequate and what kind of processing they could be intuitively bring to the model. After reading the description, I felt there is little insight into why the attention mechanism is tweaked the way it is. Also, while ablation studies detail the weigh of each macro-component to performance (Table 6), it would have been interesting to see a more detailed ablation into the various modification introduced by each of the aforementioned equations with respect to a baseline attention architecture.

MULTI-MODALITY
The proposed algorithm outperforms competitors when a single modality is considered, while some approaches outperform the proposed method in the presence of multiple modalities. It would have been interesting to see how the proposed approach does when multiple modalities are considered, even with a simple late fusion. This would shed some light into the generalizability of the approach to the use of signals other than RGB images.

### Questions
I found the paper overall interesting, but I think the quality of presentation is somewhat limited. Also, there is little insight into why the proposed modifications work.

The authors could clarify this latter aspect in the rebuttal, while the quality improvements can only be done in the camera ready, if the paper is accepted.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
