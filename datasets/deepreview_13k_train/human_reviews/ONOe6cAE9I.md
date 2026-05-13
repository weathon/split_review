# A Generalist Intracortical Motor Decoder

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Mapping the relationship between neural activity and motor behavior is a central aim of sensorimotor neuroscience and neurotechnology. 
Most progress to this end has relied on restricting complexity: studying specific simple behaviors, in limited subjects, with interpretable computational models. However, current trends in deep learning suggest that modeling a breadth of neural and behavioral data all at once is not only possible, but that such a model would also benefit downstream analysis of related data. We accordingly developed Neural Data Transformer 3 (NDT3) as a foundation model for motor decoding of neural data from intracortical microelectrodes. We pretrained NDT3 with 2000 hours of neural population spiking activity paired with diverse motor covariates from over 30 monkeys and humans from 10 labs. Pretrained NDT3 is broadly useful, benefiting decoding on 8 downstream decoding tasks and generalizing to a variety of neural distribution shifts. However, we find signs that scaling over diverse neural datasets may be challenging, as scaling from 200 to 2000 hours already requires increasing model size to 350M parameters to avoid model saturation, and several downstream datasets scarcely benefit from scale. We provide two demonstrations that this scaling is at least partially limited by variability in input and output spaces across neural datasets, which pretraining alone may not resolve.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces NDT3, a foundation model for motor decoding from spiking activity. NDT3 is trained on large scale and diverse motor tasks and subjects, demonstrating benefits of scaling law in some scenarios. The paper also reports cases where the model fails to generalize to downstream tasks.

### Strengths
* The NDT3 model is original, extending NDT2 with architectural changes to accommodate pretraining on large scale and diverse datasets.
* The paper shows extensive experiments to evaluate the model and was open to discuss failure modes of the model.
* The method is well motivated. Building foundation models for neural data has great implications for BCI and neuroscience applications in general.

### Weaknesses
 * My main concern about the paper is its lack of clarity in writing. The paper seems to focus a little too much on technical details and verbose explanation, making it hard to follow the main points sometimes. For example, lines 371 to 376 briefly mention joint tuning and sequential tuning, which are minor technical details of fine-tuning choices and do not largely contribute to the main point being discussed in the paragraph which is about input order sensitivity in cross-subject transfer. It might be better to show one type of tuning and leave the other in the Appendix to maintain the flow of writing, which would also help make the plots in Figure 4 cleaner with key takeaways only. Another example is Figure 3C to 3E, where it might be better to only show the 1.5hr, 200hr and 2khr models to avoid cluttering in the plots while still convey the main points.
* Cross-subject transfer which is the main use case of neuroscience pretrained models does not seem to be promising with the proposed model. The usefulness of such foundation model to the community therefore might be limited.

### Questions
* Figure 1: are non-neural tokens removed entirely or replaced by zeros tokens? If they are removed entirely from the sequence, would neural tokens assume new positional embeddings left by the non-neural tokens?
* Line 156: why wouldn’t segments be padded with zeros rather than being concatenated with another partial segment to form the two-second cut?
* Figure 3D: what the errorbars would look like if plotted? Pretrained models seem to not differ much by their mean $R^2$. In the absence of errorbars, it’s hard to know if it’s worth scaling up the data and model size for additional performance if the differences are not statistically significant.
* Line 181: why cross-entropy loss was used instead of Poisson likelihood loss that is traditionally used for spike counts? Is there a coefficient balancing MSE loss and cross-entropy loss?
* Figure 5D: was the test monkey with S1/FEF/MT recordings seen during pretraining, i.e. the S1/FEF/MT data might have been recorded from a subject whose motor cortex recordings were present in the pretraining set? If not, this would be the case of cross-subject transfer?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a large-scale model that has been pretrained on a large corpus of spiking activity collected from 30 monkeys and humans across 10 labs during diverse motor tasks. It presents a multimodal transformer that tokenizes both neural activity and behavioral data into token streams, allowing the causal decoding of behavior tokens from neural tokens. The findings highlight the challenges of scaling across diverse neural datasets, showing that increasing both model size and data volume can prevent degradation during pre-training. Additionally, the paper suggests that scaling is constrained by variability in input-output relationships, which pre-training alone may not fully resolve.

### Strengths
1. This paper attempts to address an important question of whether pretraining large-scale models can yield field-wide improvements for neuroscience.
2. While the model architecture itself may not be novel, there is a lack of effective large-scale multimodal models in this field, and this paper effectively fills that gap.
3. The comprehensive evaluation of how pretraining affects the decoding of diverse motor tasks from datasets of humans and monkeys offers valuable insights for the neuroscience community.

### Weaknesses
1. The author observed scaling difficulties, suggesting they may come from variability in datasets. However, I think there are other factors worth considering. For example, model performance may saturate when there is not enough information about behavior in the neural data, and the gain provided by pre-training has less room for improvement. Another factor may be that different behavior modalities/tasks have different training dynamics s.t. the model selected for final evaluation may be good at some tasks but not the others. Thus, it may not be that the model cannot scale across heterogeneous datasets, but that the model has trouble balancing the optimization of different modalities/tasks. Specifically, the model is trained with mean-squared error for predicting behavioral variables, and categorical cross-entropy losses for predicting neural spike count and reward. It is unclear if the model is equally optimized for each of these objectives, and if the final model selection criteria adequately addresses this potential imbalance. This could lead to a model that performs well on some tasks at the expense of others, masking the true scaling potential.
2. Although I don't assess a paper based on its writing and figures, I feel that clearer writing and more understandable figures could better deliver the paper's message. These aspects do not impact the overall quality of the work, but would certainly make it easier for readers to grasp the content. For example, in Fig 3C, it's hard to distinguish different pre-training volume by colors. In Fig 3E, what do the different colors mean?

### Questions
I will probably increase my scores if the author can address the questions below:
1. This paper argues that pretraining may be constrained by inherent variability within the neural datasets. Did the author explore other possible explanations for this issue? Given that the model is evaluated on decoding tasks, could it be that certain tasks are inherently easier, leading to performance saturation with little room for improvement? For example, if there is only a limited amount of decodable information about behavior in the neural data, then scaling can not allow us to go beyond that information upper bound. **This is just a hypothesis that is hard to test empirically, but could the author suggest a specific analysis or experiment to test this hypothesis about information upper bounds about some tasks in the neural data?**
2. The author mentioned that “all behavior is normalized per dataset so that the maximum absolute value of each variable is one.” I wonder whether this preprocessing step might influence model training. For example, the small values of all behaviors could lead to a low loss value, which might hinder backpropagation and parameter updates, preventing the model from effectively learning to optimize behavior prediction. Could this be a contributing factor to the scaling challenges? Additionally, why doesn’t the author consider alternative preprocessing methods, such as using the mean and standard deviation to balance the behavior tasks? **Could the authors provide justification for their chosen normalization method, or to conduct an ablation study comparing different preprocessing approaches?**
3. In the evaluation section, the author stated, “To manage compute and storage demands and to reflect that real-world datasets are rarely collected or analyzed in isolation, we fine-tune NDT3 jointly over data combined from multiple evaluation sessions.” I wonder how much this fine-tuning process affects the scaling challenges observed. If the pre-trained model is fine-tuned on multiple, heterogeneous test sets, could this complicate the fine-tuning results? What if the author selected specific test sessions and behavior tasks for targeted fine-tuning? Would that alleviate the scaling difficulties? **Could the author do a simple experiment to quantify the impact of joint vs. targeted fine-tuning on scaling performance?**
4. What specific criteria did the author use for model selection? A common challenge in multimodal multi-task training is that data from different modalities contain varying amounts of information, and some decoding tasks are inherently easier than others. As a result, when one behavior decoding task reaches optimal performance, other prediction tasks may suffer from overfitting. Could model selection contribute to these scaling difficulties? It’s possible that the pre-trained model has already learned to decode each behavior very well during training, but the selected model for final evaluation may be good at certain tasks but bad at others due to imbalanced optimization. **Could the authors provide more details on their model selection process and consider conducting an analysis of task-specific performance across different model checkpoints to investigate potential imbalances?**

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes large-scale pretraining of a Transformer-based foundation model, called NDT3, for motor decoding. Building on prior work by Ye et al. (2023), the model scales up to incorporate diverse datasets involving both monkey and human motor tasks.  The authors evaluate their pretrained model on eight downstream datasets and find that while some downstream tasks benefit from extensive pretraining, others show minimal improvement. They report that NDT3 model needs to be scaled up to 350M parameters to avoid performance drops when pretrained with 2000 hours of data. The authors also hypothesize that the poor generalizability may stem from the input-output shift, highlighting challenges in developing foundation models for neural data.

### Strengths
- Extending the scale of foundation models pretraining for neural population spiking activity. The authors have used very large amount of data (2000 hours) for pretraining a generalizable model for motor decoding. This represents a valuable step forward in investigating the effectiveness of foundation modeling approaches for motor decoding, and more broadly, for neuroscience applications.

- Building on prior research, the authors perform analyses to offer insights into scenarios where foundation models may be more effective. Understanding when and why these approaches are beneficial (or may fail) can illuminate domain-specific challenges for motor decoding.

### Weaknesses
 - The main contribution of this work lies in extensive pretraining of large foundation models (45M or 350M parameters) using substantial amount of neural-behavioral data for better generalizability.  However, the performance gains from this heavy pretraining seems minimal and task-dependent. In several cases, the authors report that pretraining NDT3 with large datasets yields only minor improvements on downstream tasks. While the in-depth analysis of why generalizability has been limited is insightful (as outlined in the strengths), the results overall suggest minimal progress towards the goal. For example, in Fig. 3D, increasing the pretraining data volume from 200 hours (even from 1.5 hours) to 2000 hours only slightly improves the average downstream decoding. 

- The authors find that to benefit from pretraining with up to 2000 hours of data, the model’s capacity needs to be significantly increased to 350M parameters. The goal of this extensive pretraining is to facilitate easy downstream use. However, finetuning such a large model entirely can itself be of significant cost. Therefore, it remains questionable whether or not scaling the model with data provides a practical solution. 

- Lack of sufficient baselines: NDT3 has been primarily compared to itself under different data regimes or training from scratch. The authors additionally compare it to two baselines trained from scratch: 1) the predecessor model NDT2, 2) a very simple linear method (WF). These baselines seem insufficient for careful evaluation of NDT3. More expressive baselines such as MLP or RNNs should be added to strengthen the results. Additionally, without comparisons to other foundation models, it’s unclear whether the generalization challenges observed are unique to NDT3 or representative of foundation models for neural decoding more broadly. For example, comparisons with the foundation model in Azabou et al., 2023 will be needed, at least on the Neural Latent Benchmark. See next. 

- The authors note that: “we avoid the Neural Latents Benchmark (Pei et al., 2021) as it does not directly measure decoding performance”.
I did not follow the above reasoning. Decoding is also assessed on this benchmark (NLB) it seems. Could the authors clarify how NLB differs from the evaluated datasets? It’s understandable that comparing to other foundation models may be challenging due to the lack of publicly available pretrained models. Nonetheless, aren’t there any other foundation models with available code and pretrained weights for comparison? For example, Azabou et al., 2023 evaluated their method (in terms of behavior decoding) on NLB datasets with motor tasks similar to those analyzed here. If benchmark comparisons on the authors’ data is not possible, NDT3 should be compared to such approaches including Azabou et al., 2023 on common downstream datasets such as NLB. 

- Novelty compared with NDT2: Novelty compared with NDT2 seems limited and the model differences compared to NDT2 (if any) are not discussed in detail. It is not clear if NDT3 is the same model (potentially with more parameters) just pretrained with more data. In fact, the smaller NDT3 with 45M parameters seems to have comparable capacity to the NDT2 models used (20M and 72M parameters).  Please provide a detailed comparison of the model architectures, training procedures, and key innovations of NDT3 compared to NDT2. This would help clarify the extent of the novelty in NDT3. Also, related to the previous point, why is pretrained NDT2 not provided as a baseline in the main figures? Please provide this in the main figures. As NDT2 is also a foundation model and its pretrained weights are available, providing its finetuned downstream performance is a more informative baseline than the one trained from scratch e.g., in Fig. 3D and Fig. 10. Does pretrained NDT3 outperform pretrained NDT2? Please provide these in main figures and discuss.

- Novelty in terms of generalizability results: The utility of large-scale pretraining of foundation models and their transferability to downstream tasks for neural data (although not spiking activity) has been shown before. For example, Zhang et al., 2024 have proposed a foundation model for SEEG data with even larger pretraining data than NDT3. Similar to NDT3, Zhang et al., 2024 also evaluated the effect of model size on generalizability and showed improved performance with higher-capacity models. Therefore, the idea and conclusions about generalizability of foundation modeling with more brain data are not novel in the field.



### Questions
My questions are the ones stated in weaknesses and Minor/questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors developed Neural Data Transformer 3 (NDT3), a neuroscience foundation model for decoding movements. They pretrained NDT3 using 2,000 hours of neural data, paired with various motor target labels, from over 30 monkeys and humans across 10 labs. Following this, they demonstrated the limitations of the pretrained foundation model on certain downstream datasets.

### Strengths
This is the **largest dataset** used so far. A highly relevant previous study (Azabou et al., NeurIPS 2023) utilized 100 hours of recordings from 7 monkeys, whereas this paper includes 2,000 hours of recordings from 30 monkeys and humans. With this unprecedentedly large dataset, the authors found that scaling from 200 to 2,000 hours of data necessitates increasing the model size from 45M to 350M.

### Weaknesses
 **Contribution of NDT3:**
The primary contribution I gather from this paper is the limitation of scaling when dataset size increases. To my knowledge, there are at least six foundation models in the neuroscience field (listed by year):

NDT, Ye and Pandarinath, NBDT 2021
**EIT**, Liu, ..., Dyer, NeurIPS 2022 (monkey motor tasks)
NDT2, Ye, Collinger, Wehbe, Gaunt, NeurIPS 2023
**POYO**, Azabou, ..., Dyer, NeurIPS 2023 (monkey motor tasks)
Wang, ..., Tolias, bioRxiv 2023/2024 (mouse visual cortices)
Zhang, ..., Dyer, Paninski, Hurwitz, arXiv 2024 (mouse brain regions)

NDT3 has only been benchmarked against NDT2 and the Wiener Filter (WF) but not against two highly relevant baselines: **EIT and POYO**. The absence of these comparisons is a significant oversight, as EIT and POYO represent state-of-the-art approaches in motor decoding with foundation models. Without these benchmarks, it is difficult to assess the true advancement offered by NDT3.

**Writing Quality:**
The writing in this paper is poor, making it challenging to read due to some typos in the text.

Examples when referring to Figures:
L107: There is no left or right panel in Fig. 2A; it should be Fig. 2B.
L466: It should be Fig. 5B instead of Fig. 5C.
L479: There is no Fig. 5D; it should be Fig. 5C.

A difficult-to-understand sentence:
L214-215: "Other Transformer variants have been proposed for pretraining on spiking data (Azabou et al., 2024; Zhang et al., 2024), but the field yet lacks consensus benchmarks to distinguish the most promising proposal to scale." Does “benchmark” here imply that the authors plan to benchmark their Causal Transformer against other Transformer architectures? In this study, they only benchmarked NDT2, which used the MAE structure. However, is the performance difference due to the different structures or different data sizes? The lack of clarity around the term 'benchmark' and the absence of direct architectural comparisons makes it difficult to interpret the significance of NDT3's performance.

**Minor Issues:**
L200: Extra word: Prior work (Azabou et al., 2024; Ye et al., 2023; Zhang et al., 2024) **ran** focused evaluations by tuning...
L277-278: Missing parentheses: ...that increasing model size and dataset size in tandem is important for performance **(**Dosovitskiy et al., 2021; Kolesnikov et al. 2020; Aghajanyan et al. 2023**)**
L392: Remove the extra parentheses: ...which fail completely **(**(Rizzoglio et al., 2022)**)**.
L482: Missing a word: While the former can be attributed **to** the close interaction of sensorimotor areas...

### Questions
Why was the MAE Transformer structure in NDT2 replaced with the Causal Transformer in NDT3?

Why are the red lines broken in Fig. 3A and 3B? Does this indicate that R² suddenly dropped between 100 and 200 epochs?

Regarding the dimensionality of movement covariates (Fig. 2A), why could it be as high as 10? My understanding is that if a hand is moving on the XY plane, the dimensionality would be 2. Can a hand move in 10 dimensions?

### Soundness
3

### Presentation
3

### Contribution
3
