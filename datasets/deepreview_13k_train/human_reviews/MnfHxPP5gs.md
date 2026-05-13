# HelpSteer2-Preference: Complementing Ratings with Preferences

- Decision: Accept
- Scores: 6, 6, 6, 5, 6

## Abstract
Reward models are critical for aligning models to follow instructions, and are typically trained following one of two popular paradigms: Bradley-Terry style or Regression style. However, there is a lack of evidence that either approach is better than the other, when adequately matched for data. This is primarily because these approaches require data collected in different (but incompatible) formats, meaning that adequately matched data is not available in existing public datasets. To tackle this problem, we release preference annotations (designed for Bradley-Terry training) to complement existing ratings (designed for Regression style training) in the HelpSteer2 dataset. To improve data interpretability, preference annotations are accompanied with human-written justifications. Using this data, we conduct the first head-to-head comparison of Bradley-Terry and Regression models when adequately matched for data. Based on insights derived from such a comparison, we propose a novel approach to combine Bradley-Terry and Regression reward modeling. A Llama-3.1-70B-Instruct model tuned with this approach scores 94.1 on RewardBench, emerging top of more than 140 reward models as of 1 Oct 2024. We also demonstrate the effectiveness of this reward model at aligning models to follow instructions in RLHF. 
We open-source this dataset (CC-BY-4.0 license) at \url{https://huggingface.co/datasets/nvidia/HelpSteer2} and openly release the trained Reward Model at \url{https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Reward}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores whether a Bradley-Terry or regression approach is more effective for reward modeling and proposes a novel method that combines both styles. The conclusion is intriguing: the format in which data is collected and the specific model training approach do not significantly impact the results.

### Strengths
This paper provides an excellent dataset that will be highly valuable to the community. It addresses an important question: whether the Bradley-Terry style or regression style is more effective for reward modeling. Additionally, the reward model (RM) proposed here is capable of effectively training a LLaMA-70B model.

### Weaknesses
I'm glad to see that the BT training method with an added margin (eq.2) is effective. However, this finding somewhat conflicts with the results in the Llama 3 paper, where the authors mention: "The training objective is the same as Llama 2, except that we removed the margin term in the loss, as we observed diminishing improvements after data scaling." What could be the reason behind this discrepancy?

I understand that this work provides an excellent dataset and rigorous experimental validation. However, I would like to see more analysis, such as:

1. A comparison of results on out-of-distribution prompts.

2. A consideration of annotation costs: since preference annotations are likely cheaper and easier to scale than Likert scores, a fair comparison might require factoring in annotation costs rather than simply matching dataset sizes.

3. An analysis of robustness to annotation errors. For instance, assume that preference annotations have a 5% chance of being reversed, or that Likert scores have a similar error rate (where a 9 might be incorrectly marked as a 1, rather than just slightly off, like 8). Which reward modeling approach is more robust to such errors?

These aspects would provide valuable insights into the practical implications of each approach.

### Questions
Has a prompt filter been applied to ensure that prompts from the rewardbench are not included in the training set?

Additionally, how does SteerLM regression, initialized with the Bradley-Terry model, perform?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents HelpSteer2, a dataset designed to facilitate research in RM for aligning language models with human preferences. This work addresses the gap of fairly comparison of BT and regression style of RM by releasing preference annotations compatible with the BT style alongside existing ratings formatted for Regression-style training. The authors then conduct a head-to-head comparison of the BT and Regression models when matched for data quality, providing valuable insights into the effectiveness of each approach. They also propose a hybrid model that combines elements of both BT and Regression approaches, achieving state-of-the-art performance on the RewardBench benchmark. Additionally, the authors open-source the HelpSteer2 dataset and trained reward model to promote further research in RM alignment tasks.

### Strengths
- The authors have created and open-sourced the HelpSteer2 dataset, which includes high-quality preference annotations and justifications specifically designed for reward model (RM) training.
- The paper conducts a detailed, head-to-head comparison between Bradley-Terry (BT) and Regression-style reward models, providing insights into the relative strengths and weaknesses of each approach.

### Weaknesses
 - While the hybrid approach is innovative, it seems to be an incremental improvement rather than a fundamentally new modeling technique. 
- Lack of statistical significance testing to validate the effectiveness of proposed hybrid modeling method.
- The paper does not evaluate the aligned models on standard language modeling tasks, which would help in quantifying the alignment tax.


### Questions
- Could the authors provide statistical significance testing to validate the reported performance improvements of the hybrid model? This would strengthen the robustness of the conclusions.
- Have the authors considered evaluating the align models on standard language modeling tasks to assess the alignment tax? 
- Based on the appendix, it appears that the RL training involved approximately 10k examples, and the model was trained for fewer than 100 iterations. Could the authors clarify the stopping criteria for the training process? Additionally, could you specify the KL divergence value of the choosen checkpoints from the reference policy? This information would provide better insight into the training stability and convergence behavior of the reward model.
- Are the conclusions valid for cases where, e.g, 5 responses ranking are used for RM training?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work addresses two major paradigms: Bradley-Terry (BT) and Regression style models, examining which is better when matched for data. The main challenge in previous studies was the lack of comparable datasets collected using both methodologies. To resolve this, the authors introduce the HelpSteer2-Preference dataset, which complements existing ratings with preference annotations, including human-written justifications. This dual-annotation allows a head-to-head comparison between BT and Regression models under controlled data conditions.

### Strengths
First, it complements existing ratings with detailed preference annotations, allowing for more nuanced training of reward models. By collecting preference data alongside Likert-scale ratings, the dataset enables direct comparisons between models trained under different paradigms (e.g., Bradley-Terry vs. Regression), which was previously difficult due to incompatible data formats in existing datasets. This dual approach provides a richer training ground for testing and developing models that need to evaluate comparative quality.

Second, the dataset includes human-written justifications for preferences, adding a layer of interpretability. This is particularly valuable for training models that can both assess and explain their choices, supporting applications where transparency is important, such as in human-in-the-loop systems. The justifications make the dataset unique by facilitating the development of models that are not just performance-driven but also capable of detailed decision-making explanations.

Third, the dataset maintains high-quality standards, demonstrated by its filtering processes and the steps taken to ensure strong inter-annotator agreement. By curating data that passes rigorous quality checks, the authors improve the signal-to-noise ratio, making it more effective for training robust models. This attention to quality addresses common issues in training data, where noisy or inconsistent annotations can limit model performance.

Overall, the HelpSteer2-Preference dataset's strengths lie in its dual-format data collection, the inclusion of human justifications for enhanced interpretability, and its commitment to high-quality, reliable annotations. This makes it a valuable resource for advancing research in reward modeling and instruction-following alignment in language models.

### Weaknesses
While the HelpSteer2-Preference dataset brings several innovations and benefits, it also has certain weaknesses that could impact its applicability and use in research and development:

First, the dataset's format, which includes both ratings and preferences, may require more complex preprocessing and handling by researchers. The dual data structure means that models need to be capable of leveraging both individual ratings and comparative preferences, which could increase the implementation complexity for teams that are not equipped with extensive data processing expertise. Specifically, the need to manage two distinct annotation types, potentially requiring separate data loaders and model architectures, adds an extra layer of engineering overhead. This is not just about combining data formats, but also about ensuring that models can effectively learn from both types of signals simultaneously, which may necessitate custom loss functions or training procedures.

Second, despite the inclusion of human-written justifications enhancing interpretability, these justifications may introduce variability due to subjective writing styles or annotator biases. This subjectivity can make it challenging to maintain consistency across annotations and could potentially affect the model's ability to generalize when trained with such data. The free-form nature of the justifications means that the same underlying reasoning could be expressed in many different ways, making it difficult for models to extract consistent patterns. Furthermore, the lack of a standardized vocabulary or structure in the justifications may require the use of more complex natural language processing techniques, which might not be accessible to all research teams. Additionally, the potential for annotator biases to be encoded in the justifications could lead to models that amplify these biases.

Third, while the dataset emphasizes high-quality annotations with steps taken to filter out low-confidence or inconsistent data, this strict filtering reduces the overall volume of usable data. The exclusion of samples with high variability among annotators may result in a smaller training set, potentially limiting model performance, especially for models that benefit from a large and diverse dataset. This trade-off between quality and quantity could be a bottleneck for researchers who need extensive data for training large-scale models. The filtering process, while improving the quality of individual samples, may also inadvertently remove some of the natural diversity present in the data, potentially reducing the generalizability of models trained on the filtered dataset.

Lastly, the HelpSteer2-Preference dataset is tailored to specific types of model training and evaluations, such as Bradley-Terry and Regression-based reward models. This specialization may limit its generalizability to other types of machine learning tasks or applications that do not align with these paradigms. Researchers working on models with different objectives or those requiring more diverse data formats might find the dataset less adaptable. For instance, models that rely on reinforcement learning with more complex reward structures or those that require multi-modal inputs might not be able to directly leverage this dataset.

### Questions
1. How were the annotators trained to provide consistent ratings and justifications, and what measures were in place to minimize subjective bias?
2. How well does the dataset generalize to real-world applications beyond reward modeling and instruction-following?
3. What is the impact of filtering out samples with high annotation variability on the overall representativeness and diversity of the dataset?
4. Would models trained on a smaller, higher-quality dataset perform better than those trained on larger datasets with more noise?
5. How might the dataset be expanded or adapted to cover other dimensions of reward modeling, such as domain-specific use cases or more complex types of preferences?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper complements the existing HelpSteer2 dataset with preference annotations, showing that pairwise annotation can further distinguish responses with similar likert scores. This dataset, together with its counterpart HelpSteer2, enables a head-to-head comparison between Bradley-Terry and Regression style reward models, by training models with the same prompts and responses in HelpSteer2 and only differing the feedback annotation. Using insights from this comparison, they propose a novel approach combining both methods, achieving superior reqward modeling performances. They also conduct experiments with RL algorithms to demonstrate the effectiveness of the reward models.

### Strengths
1. The paper introduces a carefully annotated preference dataset that could be useful. The authors also conduct some analysis on the difference of pointwise and pairwise annotation.

2. This paper compares Bradley-Terry and Regression style reward modeling paradigms, which motivates them to design a new method to make the best of both worlds.

### Weaknesses
 1. The motivation is somehow overclaimed. In line 013-016, the authors claim that there lacks datasets to enable the comparison between Bradley-Terry and Regression style reward modeling. However, all preference datasets with point-wise scores can be converted into pair-wise setups, which should have been able to allow the comparison between the two paradigms. But I agree with authors that "Regression-style data collection (where responses are rated individually) gives
annotators a different set of expectations for comparative ranking of responses" (line 055-056), so it'd be better to have a pair of dataset directly annotated in point-wise and pair-wise schema. Admittedly, the comparison setup is improved now but it was not totally undoable.

2. The authors conducted a lot of experiments, but it's hard for readers to parse useful information from the experiments with almost no highlights in writings. The abstract mainly focuses on what they did, with no mention on what they have found in their experiments. In the experiment sections, readers would benefit a lot from bolded high-level excerpts to quickly grasp the key findings. 

3. The results are good to know, e.g. the comparison between Bradley-Terry and Regression style reward modeling, but personally I don't find it surprising or informative enough to serve as the main claim of a conference paper. It would better to investigate deeper what properties of an algorithm make a good reward model. Also, the experiments are mainly conducted on general chats with subjective metrics (LLM-as-a-judge), thus the conclusions may not be able to generalize to other taks like reasoning, which is known to be very different from chatting. Regarding other experiments, such as section 5, the authors conduct RL with their reward models and datasets mainly for the sake of demonstrating their usefulness. In this case, it seems baselines are needed so that readers can be better aware of the necessity of another preference dataset, given the existence of many good alternatives, and distinguish this dataset with existing ones.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Helpsteer2-preference, a preference dataset that provides additional pairwise preference annotations alongside the existing Likert-5 style rating of the Helpsteer-2 dataset. Using this dataset, the authors conduct head-to-head comparisons between two major types of reward models. Then, they propose a method to combine two types of reward models to achieve better performances on RewardBench and preference learning.

### Strengths
- The writing is clear and easy to follow.
- The data collection process is well-designed, with detailed and comprehensive analysis provided.  The proposed dataset provides a direct and fair comparison between Bradley-Terry and Regression-based reward models. 
- The proposed method of  combining of different reward models is effective on RewardBench, and improves LLaMA-3.1 through preference alignment.

### Weaknesses
 - One major concern is the paper/s dependence on HelpSteer2. While the authors states that "converting regression-style data to preference pairs cannot fully capture nuances in preferences", there are no experimental results to support this claim. It would strenghthen the paper to include experimental comparisons with models trained on the preference dataset converted from Helpsteer2. This would help clarify whether the improvement is due to the new preference data itself or the different formulation of reward models.

- Lack of comparison with other reward models or preference dataset in preference alignment (RLHF, DPO).
  - For DPO, what if you apply the converted preference dataset from HelpSteer2?
  - For PPO, can you compare it with other reward models of the same base model(e.g. Llama3-70B-SteerLM-RM, TextEval-Llama3.1-70B)?

### Questions
- How does the reward model perform if combined vice-versa, using SteerLM Regression model with the initialization of Bradley-Terry model?
- How many hours of human labors do you use to collect the human annotations?
- How does the proposed reward model combination method compared with model ensembling?

### Soundness
2

### Presentation
3

### Contribution
3
