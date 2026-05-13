# Your Weak LLM is Secretly a Strong Teacher for Alignment

- Decision: Accept
- Scores: 6, 6, 6, 10, 6

## Abstract
The burgeoning capabilities of large language models (LLMs) have underscored the need for alignment to ensure these models act in accordance with human values and intentions. Existing alignment frameworks present constraints either in the form of expensive human effort or high computational costs. This paper explores a promising middle ground, where we employ a weak LLM that is significantly less resource-intensive than top-tier models, yet offers more automation than purely human feedback. 
We present a systematic study to evaluate and understand weak LLM's ability to generate feedback for alignment. Our empirical findings demonstrate that weak LLMs can provide feedback that rivals or even exceeds that of fully human-annotated data. Our study indicates a minimized impact of model size on feedback efficacy, shedding light on a scalable and sustainable alignment strategy. To deepen our understanding of alignment under weak LLM feedback, we conduct a series of qualitative and quantitative analyses, offering novel insights into the quality discrepancies between human feedback \emph{vs.} weak LLM feedback.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper concentrates on the critical research topic of large language model (LLM) alignment, especially related to super-alignment. Considering existing mainstream alignment approaches rely on paired human preference data, which highly relies on human or powerful LLMs for annotation, using a weak LLM to provide alignment feedback becomes a promising alternative. This paper aims to bridge that gap of lacking a systematic evaluation and understanding of weak LLM’s capability of generating feedback of alignment. The authors first formalize a workflow to conduct semi-supervised alignment training of a model and conduct evaluation. Based on this uniformed experimental setting, the paper assesses the effectiveness of models of various scales in providing alignment feedback and finds that weaker LLMs can indeed play an effective role in alignment tasks. Additionally, an in-depth analysis is conducted on the quality of feedback provided by weaker LLMs.

### Strengths
- The research topic in this paper is critical and popular. Given the high costs associated with human and large model annotations, exploring the potential of weaker LLMs in providing alignment feedback is a timely and necessary endeavor.
- This paper is well-written and easy-to-follow, with an introduction to associated alignment background techniques.
- A dedicated discussion section highlights the differences between this work and the most relevant prior studies.

### Weaknesses
 - More comprehensive experiments are required to validate the reliability of the primary conclusions in this paper, including but not limited to the following aspects.
    + The most relevant baselines with the idea of RLAIF. Beyond that the original RLAIF methods rely on large LLMs to provide feedback, it is crucial to delineate differences between the proposed training pipeline and RLAIF. Additionally, a comparison with RLAIF employing weaker LLMs as the reward model would strengthen the findings.
    + Human annotation data of different quality levels. Previous studies [1,2] have indicated that the HH-RLHF dataset may contain noise in its human preference labels. Comparing with higher-quality human data, such as a revised version of HH-RLHF, would enhance the robustness of the results.
    + LLMs with larger sizes.
    + GPT-4 with more advanced prompts or instructions to provide alignment feedback.

[1] Wang, Binghai, et al. "Secrets of rlhf in large language models part ii: Reward modeling." arXiv preprint arXiv:2401.06080 (2024).

[2] Liu, Yan, et al. "Elephant in the Room: Unveiling the Impact of Reward Model Quality in Alignment." arXiv preprint arXiv:2409.19024 (2024).

- The issue of overfitting to a specific dataset in smaller models is not discussed. Since small LLMs are prone to overfitting to specific datasets but LLMs alignment target diverse domains, you should consider the generalization of the weaker LLM to provide alignment across domains. If it shows very weak generalization, it may need annotation data in each domain, which also requires a large human cost.
- More diverse and more reliable evaluation metrics should be considered.
- The actionable insights derived from the in-depth analysis are sparse. The main finding is that issues persist in the original annotated data, and both weaker LLMs and large models like GPT struggle to handle noisy data with high confidence.

### Questions
- Why the weaker LLM to provide alignment feedback is referred to as a task-specific model? It is trained with the HH-RLHF dataset, which is a general domain dataset for LLM alignment.
- What does the “pre-trained strong model” mentioned in Line 371 specifically refer to? Is is the LLM that only undergone pre-training without fine-tuning or alignment, or is it the trained with positive examples?
- I have concern about the result that GPT-4 underperforms compared to smaller models. Could you please provide more reasonable explanations?

### Soundness
3

### Presentation
3

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
This paper introduces an alignment approach using weak large language models (LLMs) that balances cost and efficiency. The authors find that weak LLMs can generate feedback comparable to or even better than human feedback and stronger LLMs and propose the method to employ a semi-supervised framework where a weak LLM, trained on a small labeled dataset, provides preference feedback for a larger unlabeled dataset, reducing reliance on human annotation.

### Strengths
1. This paper proposes a cost-effective alignment framework that reduces computational costs and reliance on extensive human feedback,  using weak LLMs that have significantly fewer parameters than high-capacity models.

2. The study demonstrates that weak LLMs can perform as well as, and in some cases better than, human annotators in generating preference feedback for alignment through extensive experiments. For example, by demonstrating similar alignment success across different model families and sizes, the study provides a strong case for the generalizability of the weak LLM approach, suggesting that high alignment quality can be achieved without the latest or most powerful models.

### Weaknesses
1. The paper lacks a thorough analysis of feedback consistency over repeated evaluations. For example, when weak LLM and human preferences conflict, the study does not adequately explore the stability of weak LLM feedback. A quantitative analysis of consistency across multiple runs or various weak models would be helpful to assess whether the weak LLM’s feedback is repeatable and reliable. Specifically, the study should investigate the variance in feedback when using different initialization seeds for the weak LLM, or when using different weak LLMs from the same family, to ensure that the observed alignment is not due to a specific, potentially unstable, configuration.

2. The evaluation metrics are only based on 2 models, the gold reward model and GPT-4. If the models are biased, the evaluation given by them would be unreliable and it could lead to skewed assessments that do not accurately reflect the quality of weak LLM alignment. The reliance on a single gold reward model and GPT-4 introduces a potential for systematic bias, as these models may not capture the full spectrum of desirable qualities in the aligned models. The study should explore a more diverse set of evaluation models, including those trained on different datasets or with different architectures, to provide a more robust assessment of the alignment quality.

### Questions
1. Is the consistency of weak LLM feedback assessed across multiple prompts or model runs?

2. How do the authors ensure that the gold reward model and GPT-4 are reliable in evaluation? Are other potential evaluation metrics considered?

3. The paper listed many LLM alignment methods in the related work. Did the authors compare their method with these alignment techniques?

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
The paper explores the potential of using weak large language models (LLMs) for AI alignment. It proposes a new framework that leverages weak LLMs to provide feedback, thereby reducing reliance on costly human labor and computational resources. Experimental results show that even weak LLMs with as few as 125 million parameters can offer feedback comparable to human feedback. The paper also analyzes the quality of the feedback from weak LLMs and finds that it can surpass human judgment in some cases, although there is uncertainty in fine differentiation. The study offers a new perspective for AI alignment and demonstrates that weak LLM feedback is a promising, scalable and sustainable solution.

### Strengths
1.The paper introduces a framework that leverages weak LLMs for alignment, which offers a promising alternative to existing methods that rely of either extensive human labor or expensive computational resources.

2.The paper conducts comprehensive evaluation of weak LLM feedback across various model scales and families. The result consistently demonstrate the effectiveness of this approach, highlighting its potential for practical application.

3.The paper is well-organized, with clear sections and logical flow. The authors effectively communicate the research objectives, methodology, and findings.

4.The research has significant practical implications for the development and deployment of aligned LLMs. Utilizing weak LLM feedback can reduce costs and improve efficiency, making alignment more scalable and accessible.

### Weaknesses
1.In this paper， the authors propose a framework that utilizes weak LLMs for alignment, striving to strike a balance between RLHF and RLAIF, it appears that the weak-to-strong approach and methodology in the paper are still quite similar to Burns et al. (2024). Burns et al. (2024)’s study focus on reward modeling and binary classification, where the outputs in this paper are either scalar or categorical labels. Your study is closely tied to alignment and involves a more complex output space. However, it seems that the two are consistent in their methodological approach. Therefore, I think that there are still some limitations in terms of novelty. I hope you can explain more about the difference between the two works.

2.The paper points out that even advanced LLMs like GPT-4 may show feedback inconsistency when the quality difference between two responses is subtle. In the case where it is uncertain whether gold RM is stronger than GPT-4, when using gold RM for evaluation, is it also possible to make incorrect judgments about two responses with similar quality, leading to bias in the evaluation？Additionally，When using GPT-4 for evaluation, although the prompt already mentions and ensures that the order of the responses should not affect its judgment, in actual experiments, it is difficult to avoid the model's preference caused by the order. A fairer approach would be to swap the positions of the two responses and conduct the experiment again. I believe that conducting the experiment twice with different positions would result in a more accurate evaluation.

3.While the paper demonstrates the effectiveness of weak LLM feedback across alignment task, it would be beneficial to investigate its applicability to more complex tasks.

### Questions
1.See weakness 2.

2.See weakness 3. Can this weak-to-strong approach be evaluated for more complex tasks? Like a math task or a code task?

3.In Contribution 2, the authors mentioned that using weak LLMs to provide preference labels for alignment can match or even surpass the performance of using full human feedback with the same training data scale. Why is it that training on data labeled by weak LLMs on unlabeled data can outperform the training set labeled by humans? Is it because the human-labeled training set contains some incorrect labels and its quality still needs improvement?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper investigates the use of a weak supervised LLM to annotate preference data, as a middle ground between labor-intensive, costly human annotations and computationally expensive annotation based on high-capacity LLMs such as GPT-4. More specifically, the weak LLM (with approx. 100M parameters) is fine-tuned with DPO on a set of human labeled preference data and then its associated implicit reward model is applied to an unlabeled set to predict preferences. The resulting completed preference dataset is ultimately used to align a student LLM, whose performance enables measuring the quality of the annotations provided by the weak LLM.

The proposed weak LLM-based annotator is evaluated through multiple experiments where it is compared against both human annotators and stronger LLM annotators. It also includes experiments with weak LLMs and students models from different model families. Overall, the results show that using weak LLM-based annotations lead to similar or better performance compared to using human annotations or prompted high-capacity LLMs.

### Strengths
- The paper is clear, polished and reads very well.
- The experiments are comprehensive and convincing.
- The proposed idea of using a weak supervised LLM as annotator is likely to have a significant impact on future LLM alignment practices.

### Weaknesses
 - The choice of using DPO fine-tuning to obtain a weak LLM-based annotator is not fully intuitive and lacks motivations, as only a reward model is needed for the preference annotation -- a model with generation capabilities is unnecessary for this (more details on this point in the "Questions" section).



### Questions
- In the second paragraph of the introduction (lines 40-50), expliciting the fact that what is studied is a weaker _supervised_ LLM might help the reader understand the middle-ground nature of this approach. Otherwise it may not be fully clear why weaker LLMs are positioned in between human annotators and high-capacity LLM annotators.
- In Figure 1, it is a bit unintuitive to show A < B in all the annotations, as it seems that answer A is a better (at least more helpful) answer than B in the given example. This example is mentioned later in Table 3, as a case where human annotation contradicts the gold reward model.  But using this (potentially incorrect) human annotation in Figure 1 when describing the approach might be confusing for the reader.
- The construction of $\mathcal{D}_{weak}$ in Section 3.1 is done by first learning a generation model through DPO and then use the implicit reward model induced by DPO to annotate the unlabeled dataset $\mathcal{D}_u$. It seems unnecessary to train a generation model as only the reward model is needed for the annotation. Given this, it is then unclear why DPO was used in this step instead of simply training a traditional reward model by following the standard RLHF protocol (but without the unneeded PPO stage). The argument given lines 139-140 that training with RLHF requires the use of multiple models is only valid for the PPO stage (when there are both the LLM policy and the reward model to handle), but not in the reward modeling stage which only consists of an LLM augmented with a regression head. It would have been interesting to study the impact of the DPO reward model vs the RLHF reward model.
- In Section 3.2, one of the metric introduced is the gold reward. However it is not entirely clear why a large auxiliary reward model can be considered as "gold". Does it just have to be a "recognized" reward model, or are there any requirements on the training data used for this reward model?
- For the GPT-4 win-rate metric, it does not seem necessary to ask for a numeric rating to be assigned to the two compared responses. Would it not be sufficient to just ask GPT-4 to identify the better response out of the two? This seems to be a more standard approach (see, e.g., Prometheus 2: https://arxiv.org/abs/2405.01535).
- What is the ratio $|\mathcal{D}_{l}|/|\mathcal{D}|$ used for the main experiments in Section 3.3? The ablations in Section 3.4 do study the results when this ratio is varied, but I could not find the default ratio that is used in other experiments.
- The x axis label of Figure 7 in Appendix C seems to be incorrect: it should be $\beta$ instead of "student model size".

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes to investigate whether "weak" language models could serve as a reward model/preference generator for alignment. Experiments demonstrate that they can to varying extents and match some of the benefits of HF/AIF.

### Strengths
+ ailgnment with synthetic feedback/preference is an important research question
+ the experiments are comprehensive

### Weaknesses
 - On the high-level framing, why is "weak LLM as feedback" positioned as the "middle ground" (line 42) between human feedback and AI/LM feedback? You could say that weak LLM feedback is still AI feedback, just with a smaller/weaker model, and not necessarily offers something strikingly new that make it "middle ground" in the "spectrum".

- By "weak LLM" the authors actually mean "small LLM": for example, "while a model like GPT-4 might have trillions of parameters,
a weak LLM might only have hundreds of millions or even fewer" (lines 44-45). The experiments focus on size too by employing OPT models, which are small compared to today's standards. However, "small LLM" for feedback is not necessarily "weak": if you take a small model and train it on large quantities of quality human preference data, it might become a moderate reward model. It would be great to disentangle "weak" and "small" in the narrative and also in the experiments.

- Section 2 is a bit trivial and takes up too much space. These math primers on DPO/PPO were not particularly helpful in later sections too. It would be great to assume readers of an "alignment" paper are already familiar with the basics, move them to the appendix, and use the space for analysis/results.

- I see that there is some investigation into the quality of preferences by the "weak" OPT model. Maybe something like RewardBench might offer a more rigorous quantitive evaluation.

- I would argue that things like self-rewarding language models [1] did things similar to "feedback from a weak model", albeit not as weak as OPT. Starting from a "weak-ish" models that are not good in both generating and evaluating, they show it is possible to jointly improve both. I wonder if the uniqueness of this paper's contribution might be weakened a bit by works like this.

- Ultimately, some might say that this work is a fine analysis paper on a niche technical design choice and does not offer something greater: taking RLAIF pipelines, changing the "AI" model part to a smaller model, and run some evaluation. Please highlight additional contribution if any.

### Questions
please see above

### Soundness
3

### Presentation
3

### Contribution
2
