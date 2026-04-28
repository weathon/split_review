# The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models

- Decision: Accept
- Scores: 6, 6, 6, 8, 8

## Abstract
Pre-trained Language models (PLMs) have been acknowledged to contain harmful information, such as social biases, which may cause negative social impacts or even bring catastrophic results in application. Previous works on this problem mainly focused on using black-box methods such as probing to detect and quantify social biases in PLMs by observing model outputs. As a result, previous debiasing methods mainly finetune or even pre-train PLMs on newly constructed anti-stereotypical datasets, which are high-cost. In this work, we try to unveil the mystery of social bias inside language models by introducing the concept of {\sc Social Bias Neurons}. Specifically, we propose {\sc Integrated Gap Gradients (IG$^2$)} to accurately pinpoint units (i.e., neurons) in a language model that can be attributed to undesirable behavior, such as social bias.  By formalizing undesirable behavior as a distributional property of language, we employ sentiment-bearing prompts to elicit classes of sensitive words (demographics) correlated with such sentiments. Our IG$^2$ thus attributes the uneven distribution for different demographics to specific Social Bias Neurons, which track the trail of unwanted behavior inside PLM units to achieve interoperability. Moreover, derived from our interpretable technique, {\sc Bias Neuron Suppression (BNS)} is further proposed to mitigate social biases. By studying BERT, RoBERTa, and their attributable differences from debiased FairBERTa, IG$^2$ allows us to locate and suppress identified neurons, and further mitigate undesired behaviors. As measured by prior metrics from StereoSet, our model achieves a higher degree of fairness while maintaining language modeling ability with low cost\footnote{This work contains examples that potentially implicate stereotypes, associations, and other harms that could be offensive to individuals in certain social groups.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to understand why the bias happens in LMs. They use integrated gap gradients (IG^2) to identify which neurons in language models contribute to the social bias. With the identified neurons, the authors proposed bias neuron suppression method to reduce the bias in LMs. Experimenting with BERT, RoBERTa and FairBERTa, the proposed IG^2 method demonstrates to reduce the bias.

### Strengths
Extending IG method to understand the biases in language models, where the topic is interesting and important. The authors did a good job of structuring the paper, so it is easy to follow.

### Weaknesses
It seems the IG^2 requires calculating the gap between the logits of different attributes. I'm wondering how general will it be, e.g., how can we extend it to other tasks instead of predicting the sensitive attributes? For example, what if the task is a hate speech detection?

### Questions
- Does the method only work when the output of the model is to predict the sensitive attributes (so that you can calculate the logit gap)?
- What model is being examined in Fig.2? Does the conclusion hold for all models, especially for FairBERTa? 
- It seems most of the time, Union_IG can make the bias score lower. Is it because Union_IG contains more neurons? Does this mean adding more neurons generally helps reduce the bias? How sensitive is the result w.r.t. $\sigma$?
- What if you replace Union_IG to Intersection_IG, i.e., the intersection of bias neurons for different attributes?
- Table 5, it should be "StereoSet".

### Soundness
3 good

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
The paper proposes INTEGRATED GAP GRADIENTS (IG2) approach that identifies problematic neurons in a language model that contribute to undesirable behavior, such as bias. They then use this identification framework and propose BIAS NEURON SUPPRESSION (BNS) to mitigate the effect of these problematic neurons to reduce the observed biases in LLMs. Authors also perform experiments to showcase effectiveness of their detection and mitigation approaches.

### Strengths
1. The paper is easy to follow and is written clearly.
2. The approach is easy to implement and be applied.
3. The paper studies an important issue.

### Weaknesses
1. The technical contribution of the paper is not significant as it simply extends a previous existing approach for identification of problematic neurons in the context of bias and fairness.
2. The experiments are done only on masked language modeling tasks which can limit the study.
3. The approach operates between binary demographics and might be limited when we want to study biases amongst large pool of fine-grained demographics.
4. Their constructed dataset only covers few demographics.
5. The paraphrases for constructing the dataset are generated using a language model which can impose its own biases in the study.

### Questions
For results in Table 5 under FairBERTa why are some approaches missing? Some clarification on this can be helpful.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the suitability of interpretability techniques used to attribute individual neurons to model generations for the study of social bias in neural networks. To do so, the authors introduce Integrated Gap Gradients (IG2) as an approach to identify neurons attributable to social bias. Their approach is evaluated on a dataset of around 200000 template-generated samples. The evaluation is carried out by either suppressing or amplifying the detected neurons, and the experimental results demonstrate that doing so indeed reduces or increases the generation of biased outputs. Based on these results, the authors propose a debiasing approach based on the suppression of detected neurons and evaluate it on the StereoSet benchmark. Comparing this approach to a range of baselines, the authors show that the method successfully debiases model predictions while at the same time having little impact on unrelated model predictions (measured via the Language Modeling Score).

### Strengths
* The paper combines interpretability techniques with an application to social bias research in neural networks and shows that doing so yields valuable insights.
* The results are promising and might represent a foundation for future work applying the method to other applications in NLP.
* The paper is well-written and the experiments are overall thorough.

### Weaknesses
* The paper could spend more attention on the implications of the presented results. Since the authors mention the importance of fairness research in this context, a brief discussion on the usability, practicability, and limitations of their results would be desirable.
* The paper does not discuss potential implications of BNS on other tasks that the investigated LMs are faced with. While this is difficult to measure directly, it remains unclear to what extent the manipulation of neurons at inference time impacts model performance on other tasks. I’d recommend the authors to address this in the manuscript carefully.

### Questions
* Did you experiment with regularizing detected neurons rather than suppressing them entirely? Considering their suppression more gradually as opposed to zero-ing them out might help in increasing the Language Modeling Score while keeping a high Stereotype Score.
* Not really a question but more a suggestion: I’d recommend moving the introduction of BNS to after the first report of experiments to improve the flow of the paper.
* Would it be worth adding a few examples (rather than only templates) to Table 3?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new method, Integrated Gap Gradients (IG2), for measuring how much an individual neuron contributes to differences between logit predictions at the outputs. Combined with curated prompts that have positive or negative sentiment and are intended to be completed with a demographic group, this method is used to identify neurons in the network that most strongly contribute to differences between demographic groups along different dimensions, including gender, ethnicity, etc. Once these neurons are identified, the paper applies a new technique, Bias Neuron Suppression (BNS), to zero out the activations of neurons that are above a threshold score. The paper shows that when identified bias neurons are amplified, demographic gaps increase, and when they are suppressed, demographic gaps decrease. The paper also shows improvement on scores based on StereoSet for measuring the demographic bias of a language model. Finally, the paper also presents interesting empirical results comparing to other debiasing methods, showing for example that the number of bias neurons in FairBERTa does not decrease. Instead, the neurons get shifted into earlier layers compared to networks that have not been debiased. Overall, the paper demonstrates the promise of this new technique.

### Strengths
The paper’s primary strengths are the empirical results and the clarity of the new method proposed. The work is an interesting extension of the integrated gradients technique to measurements of demographic bias, and the results seem to support the efficacy of the method well. The work is clearly written and easy to follow as well.

### Weaknesses
The primary weakness of the work is the fact that the paper primarily relies on StereoSet and associated metrics to measure the effectiveness of the debiasing technique. While this is not a major limitation, it might have been nice to evaluate on another dataset with targeted queries for a specific group, such as WinoQueer (https://arxiv.org/abs/2306.15087). Another weakness of the work is a more thorough discussion of the limitations of the method, and I have some questions in the following section that could be used to expand this discussion.

### Questions
Figure 2: it’s unclear to me from the caption what exactly the x-axis is plotting. Can the authors clarify?

Table 6: Could use a bit more explanation about what the “inter” and “intra” columns represent

Questions about limitations

Is there any empirical evidence or motivation, aside from the results here, to support the assumption that single neurons can strongly contribute to demographic disparities?

Is there a way to generalize the method to take into account interactions or correlations between neurons that might affect the result?
Do you think the method is limited by the kinds of prompts that you have templated here? How would you generalize?

Can this method be extended beyond differences in sentiment for demographic groups?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an interesting approach called Integrated Gap Gradients that aims to identify the neurons in a large language model that are responsible for the exhibition of undesirable behavior like social bias. Also, the paper presents a technique called Bias Neuron Suppression that aims to suppress the detected neurons that are responsible for the undesirable behavior, hence mitigating social biases in large language models. The paper performs an extensive evaluation comparing the approach to multiple baselines, demonstrating the merits of the proposed approach in mitigating social biases and being more fair.

### Strengths
The paper focuses on an important issue, and I believe that the proposed approaches can have a significant impact on the research community that aims to study social biases and ways to mitigate these issues in large language models. The proposed approach is a significant step toward more interpretable Artificial Intelligence and aims to mitigate social biases without the need for expensive re-training or fine-tuning of very large language models like BERT or RoBERTa. The paper makes an extensive evaluation of the proposed approach and compares it with multiple baselines such as DPCE, AutoDebias, and Union_IG, demonstrating that the proposed approach outperforms them in terms of various bias metrics. Also, I really liked that the paper makes an extensive evaluation, including a large number of demographic attributes as well as modifiers. Overall, I believe that this is a good paper submission, and I believe it can advance research and state-of-the-art methods in mitigating social biases that arise from the use of large language models.

### Weaknesses
Overall, I do not have major concerns with the paper, and I have only some mainly minor issues/suggestions for the authors to further improve their paper. First, it will be good to clarify how you came up with the Demographic dimensions that are included in Table 1. Is this based on previous work or did you construct these dimensions for the purposes of this work? Also, for figure 2, the paper does not clarify what model is used to generate the results? Is this based on the BERT model? I suggest to the authors to clarify this and also discuss if they observe any differences in the presented results for Figure 2 across models. Finally, I would have liked to see a more detailed discussion and explanation of how the authors envision the use of the proposed approaches in other applications beyond social biases and debasing. The authors touch briefly upon this in the Introduction, however, they do not go into details, and it is unclear from a reader’s perspective how the proposed approaches can be applied for other purposes.

### Questions
1. How are the demographic dimensions in Table 1 constructed?
2. How do you envision the proposed approaches to be applied for other purposes beyond debiasing?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
