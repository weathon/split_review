# FairLoRA: Targeted Bias Mitigation without Performance Loss

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 8, 3, 3

## Abstract
Ensuring fairness in machine learning models is critical, but existing debiasing techniques often sacrifice model performance, struggle to adapt to emerging biases, or require extensive sensitive attribute annotations. To address these challenges, we propose FairLoRA, a novel low-rank adaptation method that mitigates bias while preserving model performance. FairLoRA incorporates parameter-efficient modular LoRA components, enabling iterative bias mitigation to ensure fairness across multiple sensitive attributes without interfering with previous adjustments. Furthermore, it employs discriminators to identify biased classes with reduced reliance on sensitive information, significantly reducing the need for annotated data. We theoretically derive conditions under which FairLoRA fine-tuning can effectively mitigate bias while maintaining the original model's performance. We then empirically validate its effectiveness across diverse computer vision and natural language processing tasks. Our experimental results show that, even for models that have undergone prior bias mitigation training, the integration of FairLoRA fine-tuning can further enhance fairness, while maintaining or even slightly improving the original performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces FairLoRA, an approach to finetuning for debiasing ML models while preserving model performance. FairLORA approaches debiasing by combining a group discriminator with LoRA modules. It works by activating the LoRA block only if the discriminator determines the sample belongs to a minority group. Otherwise, the model processes the sample through its unmodified layers without LoRA intervention. FairLoRA demonstrates improvements in minority group performance while maintaining the performance for the majority group. Additionally, FairLoRA supports multiple attribute debiasing by performing chained finetuning.

### Strengths
- FairLoRA leverages the parameter efficient finetuning method LoRA, meaning it’s a much more efficient technique compared to existing fairness finetuning approaches. Most previous fairness mitigations require either *(i)* retraining the model from scratch on group-balanced data or *(ii)* finetuning a pretrained model. It’s a solid idea to use a modified version of LoRA.
- FairLoRA is also strategic because it selectively activates the LoRA blocks. Only samples from minority groups use the LoRA blocks; the other samples are processed by the unchanged base model. This is one way the model is able to maintain majority-group performance while seeing the minority-group performance gains.
- FairLoRA also supports multiple sensitive attributes. I like this part particularly because often, fairness mitigations are designed in either a single attribute setup. It addresses the component of intersectionality that is not supported in most prior work.
- From the experimental side, many performance metrics are used to better support the claim of improved/maintained performance. I also appreciate that performing chained finetuning does not decrease performance for earlier debiased groups.

### Weaknesses
 - The largest weakness is that FairLoRA requires a balanced dataset for finetuning. This means that existing datasets have to be downsized because minority groups are nearly always, by definition, much less represented in the data. (In the instances where they’re not less represented, they’re often more stereotypically represented). The lack of balanced labels is one of the main reasons for such fairness disparities in ML models. The other issue I see with requiring balanced labels is that groups that are extremely underrepresented in the data will likely not benefit from FairLoRA. By the time the dataset has been balanced such that size(majority group) == size(minority group), the dataset will be very small.
- The experiments are a bit limited. For instance, for CelebA, the paper tests the bias of “male” and “blond hair”. Because CelebA has so many attributes, at least one other combination should be evaluated as well to better validate FairLoRA.

### Questions
**Questions**
- Figure 1’s caption describes the discriminator as essentially being a simple binary classifier, trained to predict whether the sample is from the majority group or minority group. Then in lines 201-205, the discriminator’s objective function appears more detailed: “The discriminator is trained using a fairness-oriented objective function, which focuses on reducing disparities in classification performance across different groups.” Can you explain the specific loss function for the discriminator? Is this just a binary classifier trained on the target attribute?
- In Section 4.1.1, *M* isn’t defined explicitly. I assume this refers to the model?
- Regarding the datasets selected -- while MNLI is a great dataset, I would not refer to it as a fairness dataset. Its usage is primarily (non-fairness based) natural language inference. I’d just reword L311: “We conduct experiments on three widely-used fairness benchmark datasets”. There are also NLP datasets specifically designed to test model fairness like Winogender, HolisticBias, CrowSPairs.
- As another more minor point, why is the sensitive attribute “blond hair” instead of “male” for CelebA?

**Comments**

- While I broadly agree that finetuning ML models to reduce bias tends to decrease performance, there are instances in NLP where model performance holds, including [1] and [2] below.
- L325: I suggest saying “African American” instead of “African”. Though HateXplain uses this label, there’s not a notion of the “African ethnicity”. It may seem like a minor point but I want to really emphasize that Africa is a huge continent with thousands of ethnicities. Additionally, it’s a separate concept from “African American” or Black, which I believe is the target group being referenced. Otherwise, the target attribute axis should not be referred to as “race”. Given the subject matter of the paper, these differences are quite critical.
- L390: Similar to the point above, I would strongly consider rewording “FairLoRA Africa” to something like “FairLoRA African American”, “FairLoRA Black American” or “FairLoRA Race”. Saying the work is to mitigate racial bias “(FairLoRA Africa)” conflates the continent of Africa with race.


**Small typos**

- L126: “can significantly reducing” → “can significantly reduce”
- L130: “may worsens fairness” → “may worsen fairness”

**References**

[1] Perturbation Augmentation for Fairer NLP

[2] Causal-Debias: Unifying Debiasing in Pretrained Language Models and Fine-tuning via Causal Invariant Learning

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a technique that boosts the model performance on minority groups, by (1) training a cascade of discriminators that predict whether or not samples contain belong to a minority group and (2) selectively applying LoRA updates on predicted minority samples.

### Strengths
## Strengths:
- There are very few conditions for FairLORA to be applied, making it a versatile solution for enhancing the fairness of pretrained models. 
- Significant improvements in terms of WGA are present even when very few sensitive attribute labels are present (Table 3)
- Experiments in both vision and language are quite compelling

### Weaknesses
## Weaknesses:
- The theoretical contribution of this work is a bit overstated. The final conclusion of Thm. 3, that the ratio between TPR and FPR must be high in order to prevent performance degradation, seems obvious. Also, Thms 1 and 2 should be lemmas rather than stand alone theorems, since they seem like intermediate steps to build up Thm 3. 
- As far as I understand it, one must sequentially (1) adapt the model to the task with standard techniques and (2) apply FairLoRA. However, what if the base adaptation technique learns representations that do not contain much information about the sensitive attribute? This can happen if y does not depend on the sensitive attribute or if the adaptation technique explicitly encourages invariance to the sensitive attribute [1]. 

## Minor: 
- In table 3, WRA -> WGA

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a framework that given a pre-trained network, finetunes a different set of LoRA weights for each sensitive attribute group and the LoRA weights are applied to the pre-trained weights for each sample if a `Discriminator` network is activated. The Discriminator network is trained using a fairness-oriented objective function.

### Strengths
- The paper uses multiple fairness metrics for evaluating their method.
- They further provides theorems and proves for their theorems.

### Weaknesses
 - Details about the models and experiments done is vague.
- Details of the models used for Experiment 1 and 3 are not mentioned. Also, none of the models are "state-of-the-art" as claimed in the paper.
- No exact mentioning of which splits of which datasets were used for training and testing and the claim "FairLoRA operates under a partial-information setting, where group labels are observed only for the validation set, not for the (much larger) training set." is incorrect based on the experiments explained. It can "also" be applied to the partial-information setting.
- The method is never "compared" one-to-one with another method. All tables merely mention the results after their method *is added* to ERM and previous fairness frameworks and improves them. But their method is *not* compared to either of them head-to-head to my understanding.
- Limited hyper parameter tuning and using a single set of hyper params for all models. (or the complete set was not reported) Also, number of seeds were not reported.
- Given the standard deviations, the differences in Table 1 don't seem significant for in most comparisons.

### Questions
- Please address the weaknesses mentioned above.
- What is the model used in the experiments of Section 5.2 for each of ERM, GroupDRO, DFR, and Lu et al? Also, are they all the same models?
- Do you have insights as to why the EoD(R) improves in the final stage of experiment 2 in Table 2? I.e., why does the EoD(R) further improve when mitigating gender bias?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Mitigating bias becomes essential to ensure trustworthy AI systems, but it is often not effective and requires extensive bias supervisions. The authors proposed FairLoRA, which incorporates LoRA technique to mitigate bias while preserving the performance, and a bias discriminator to reduce the reliance on bias supervision. Theoretical analysis presents the condition when bias mitigation without performance loss is effective.

### Strengths
- Experimental results on three standard datasets are provided.
- It extends FairLoRA framework to address multiple bias attributes

### Weaknesses
 - What is the meanings of theoretical analysis? It does not guarantee that FairLoRA algorithm ensures fair results (for meaningful theoretical analysis, at least it needs to show that FairLoRA satisfy Eq.(7)).
- Hard to find the novelty and motivation of the proposed method. Integrating discriminators or adopting LoRA for fairness are well investigated in this literature [1,2,3,4].
- It still requires the knowledge of the presence of sensitive attribute, which could be not applicable to unsupervised scenarios.
- Writing should be improved. In Section 3, it is hard to follow to understand the overall training pipeline. (Why the details and algorithms are in Appendix?) The caption of Figure 1 is also not well described.
- Performance improvements are not strong and experimental results are not comprehensive. Fairness-accuracy trade-off is a well-known phenomena in this literature, and the results merely present the trade-off. It is hard to verify whether the proposed method actually improves the fairness. Most of improvements are within the standard deviations.

### Questions
- What if the sequence of debiasing is changed (gender → racial) or eliminating multiple bias simultaneously. I think it could adopt multiple discriminators at once.
- No worst-group accuracy results in Table 2.
- Limitations of this work should be addressed.

### Soundness
2

### Presentation
2

### Contribution
1
