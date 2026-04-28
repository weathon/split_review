# Decoupling the Class Label and the Target Concept in Machine Unlearning

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 3, 8

## Abstract
Machine unlearning as an emerging research topic for data regulations, aims to adjust a trained model to approximate a retrained one that excludes a portion of training data. Previous studies showed that \textit{class-wise} unlearning is successful in forgetting the knowledge of a target class, through gradient ascent on the forgetting data or fine-tuning with the remaining data. However, while these methods are useful, they are insufficient as the class label and the target concept are often considered to coincide. In this work, we expand the scope by considering the label domain mismatch and investigate three problems beyond the conventional \textit{all matched} forgetting, e.g., \textit{target mismatch}, \textit{model mismatch}, and \textit{data mismatch} forgetting. We systematically analyze the new challenges in restrictively forgetting the target concept and also reveal crucial forgetting dynamics in the representation level to realize these tasks. Based on that, we propose a general framework, namely, \textit{TARget-aware Forgetting} (TARF). It enables the additional tasks to actively forget the target concept while maintaining the rest part, by simultaneously conducting annealed gradient ascent on the forgetting data and selected gradient descent on the hard-to-affect remaining data. Empirically, various experiments under the newly introduced settings are conducted to demonstrate the effectiveness of our TARF.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Machine unlearning is an emerging field focused on enabling models to "forget" specific knowledge derived from training data. While existing research demonstrates that removing knowledge of certain classes can be achieved through techniques like gradient ascent, these 
approaches typically assume a perfect alignment between class labels and target concepts,  limiting their applicability to broader cases. This work expands on this by addressing misalignments in label, model, and data domains by proposing TARget-aware Forgetting  (TARF), a framework that selectively forgets target concepts by combining gradient ascent and descent methods, ensuring that unaffected data remains preserved. Experiments highlight TARF's effectiveness in achieving targeted forgetting.

### Strengths
1.The experiments are extensive and the results are promising.
2.The research question is novel, and the proposed solution is interesting.
3. The overall presentation is easy to follow.

### Weaknesses
While TARF shows promise, the experiments are comprehensive and thorough, this study faces several limitations: 
- Study Motivation: The motivation behind this work requires further clarity and discussion. In Section 3.1, there is a mention of "increasing concerns about trustworthiness," but this lacks detail. Expanding on how unlearning can enhance trustworthiness would strengthen this section. Additionally, existing unlearning research is primarily motivated by a desire to protect data owners' right to withdraw from the learning process. Please discuss how this work differs in motivation and approach from previous research.
- Experimental Design: In the experimental section, it is mentioned that superclass information from the CIFAR-10 dataset was used. However, CIFAR-10 does not natively include superclass information. Please clarify if artificial labels were applied to CIFAR-10. Additionally, the main results heavily rely on the appendix for image generation outcomes. Consider reorganizing this part to make key findings more accessible.
- Limitations in Real-World Application: Based on Equation 5 and Phase 1, TARF demonstrates effectiveness primarily when complete class information is available. If class information (such as subclasses or super classes) is unavailable or implicit, TARF may be  limited in real-world applications. Consider discussing this limitation in more depth.

### Questions
1.What kind of class (superclass) information have been introduced on the CIFAR-10 datasets for supporting the experiments?
 2. Whether the class information should all be available for the proposed TARF?

### Soundness
2

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
4

### Summary
Machine unlearning aims to enable a model to forget specific data without retraining, making it behave as if the data had never been used during training. This paper introduces a broader machine unlearning framework that extends the conventional all-matched forgetting scenarios. The proposed method performs target identification to recognize false remaining data. Then, the proposed method conducts forgetting on given forgetting data and identified false remaining data, and conducts retaining on identified true remaining data. Finally, extensive experiments validate the effectiveness of the proposed method.

### Strengths
1.This paper extends conventional all matched forgetting and proposes a general framework for machine unlearning.

2.The experiments are sufficient to demonstrate the effectiveness of the proposed method.

### Weaknesses
1.In the model mismatch scenario, the performance of the proposed method is significantly lower than that of existing methods that do not consider model mismatch. Specifically, while the proposed method aims to address the model mismatch scenario, its unlearning accuracy (UA) is substantially worse than methods like GA, IU, BS, and SalUn, which do not explicitly handle this scenario. This raises concerns about the practical effectiveness of the proposed approach in mismatched settings.

2.Compared to other approximate unlearning methods, the proposed method has a higher time cost. The increased computational overhead, particularly the target identification phase, makes the method less appealing for applications where efficiency is critical. The paper needs to provide a more detailed analysis of the trade-off between accuracy and computational cost.

3.The organization of the paper needs revision to improve its readability. Additionally, is such an extensive appendix necessary for the completeness of the paper? The current version seems somewhat unfriendly to readers. The lack of clear section introductions and the sheer volume of the appendix make it difficult to follow the core arguments and experimental results.

### Questions
1.In the target identification phase, the authors use the prediction loss before and after forgetting to reflect representation similarity, thereby selecting false remaining data. This operation is based on empirical observations from experiments. How should the parameter \beta be controlled during implementation to balance the amount of data being forgotten?

2.Compared to existing methods, the proposed approach adds a target identification phase. Does this phase cause performance degradation in the all-matched scenario? In the experiments, the proposed method shows less performance advantage in the all-matched scenario.

3.In Figure 3, what does "class-aligned data" refer to?

4.In the evaluation metrics, on which dataset is TA applied?

5.In Table 1, for the retrained method, why are the values of the metric UA not equal to 0 in the model mismatch scenario?

6.In the model mismatch scenario, the proposed method performs significantly worse on UA compared to existing methods such as GA, IU, BS, and SalUn. Please analyze the reasons behind this phenomenon. Furthermore, existing methods do not consider the model mismatch scenario, while the proposed method provides a specific solution for this scenario.

7.Since a smaller UA value is better, a downward arrow should be annotated.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a new formalization of unlearning based on label mismatches between ground truth, the learned hypotheses, and the unlearning data, define new unlearning problems as a result of this formalization, and present an algorithm and results for these problems.

### Strengths
- The developed viewpoint that the forgetting data may have their own labeling is nice, and I think important.

### Weaknesses
 - The problems appear a bit artificial to me. All explanations are based on the concept hierarchy in the CIFAR data. I miss a clear real-world motivation for the setting. For example, I would have thought of a problem as follows: Given a learned classifier from CIFAR, remove all images that have a certain characteristics (e.g., remove all images from copyrighted sources, etc.). This obviously has real-world implications. I can imagine that this can be formulated in the setting studied by the authors, but it is not clear how, because they always refer to existing classes (and there is no class for "images from copyrighted sources", I guess). Probably what they do is fine for an evaluation, but one should provide a clearer motivation, and then discuss why the restricted CIFAR setting can be used for evaluating the setting discussed in the motivation.

- I really had a hard time in understanding the < notation (this should be a curly <). Maybe this is for similar reasons as discussed above, because I was really looking for an intuitive understanding, not for an explanation that specifies in what way that affects the CIFAR data. Also terms like "false retaining set" and "true retaining set" I found hard to grasp, even though they are formally defined.

- The proposed method has three phases, which are apparently applied sequentially. Even though there is a blended phase in the middle, I would expect that a somewhat tighter integration of these phases would be better.

MINOR CONCERNS:

- I don't think that computation is the main problem with "exact unlearning", it is more that you have to have access to all the training data, i.e., you cannot simply store the model and unlearn new data from it.

- Table 1 is too small. Some of the subscripts cannot be discriminated from each other.

- The paper lists 63 references, many of which are not cited in the paper. I suppose they are cited in the appendix, but then I think the appendix should have a separate bibliography.

- Personally I find it preposterous and disrespectful of the reviewers' commitment to submit a 40 page document to a conference with a 10-page limit. As a result, I did not look at any of the supplementary material, and only read the work as a stand-alone paper. If you have a journal-length paper, do submit it to a journal, and not to a conference where reviewing time is necessarily limited. I did my best to not let this influence my assessment of the paper, but, if anything, the effect was certainly not positive.

### Questions
I don't need any clarifications at this point (I did not understand everything, see above, but I think this is a problem with the writing, so an explanation would not change my assessment of the paper).

### Soundness
3

### Presentation
2

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
This paper proposes a TARget-aware Forgetting (TARF) framework for machine unlearning, which decouples the class label and the target concept and investigates three problems beyond conventional all-matched forgetting. The authors conduct experiments on various datasets to demonstrate the effectiveness of TARF.

### Strengths
1. The authors introduce new settings in machine unlearning by decoupling the class label and the target concept, and investigate the label domain mismatch in class-wise unlearning, which makes sense and contributes to the community of machine unlearning.

2. The proposed TARF framework is novel in addressing the problem of three typical machine unlearning mismatch (target mismatch, model mismatch, data mismatch), and has the potential to improve the flexibility and practicality of machine unlearning.

3. The experimental results are comprehensive and show that TARF outperforms several baseline methods in different unlearning scenarios. The experiments cover a wide range of datasets and models, which adds to the credibility of the results.

4. This work systematically reveals the challenges of restrictive unlearning with the mismatched label domains, and give a new insight into machine unlearning that the representation gravity in forgetting dynamics is critical for achieving the forgetting target in the new tasks.

### Weaknesses
1. The keyword "gravity" is relatively unfamiliar to readers. It should be introduced as much as possible in advance or given a brief introduction to enhance the readability of the article. This would help readers better understand the context and significance of the term within the machine unlearning framework presented in the paper. The current usage lacks a clear definition within the context of machine learning, making it difficult to grasp the underlying mechanism of the proposed framework. A more precise explanation of how "gravity" relates to data point interactions and model behavior is needed to avoid ambiguity.

2. Under the three proposed mismatch scenarios, the metrics for measuring the algorithm's effectiveness are not very clear. For example, in the case of model mismatch where the model only outputs superclasses, it is not clear how the accuracy on the unlearning set is calculated. Appendix C only introduces the specific implementation of the baselines and seems to have omitted the specific calculation method of the metrics. This lack of clarity extends to the other mismatch scenarios as well, making it difficult to compare the performance of the proposed method across different settings. The paper needs to explicitly define how unlearning accuracy, retaining accuracy, and testing accuracy are computed in each scenario, especially when the labels used for training and evaluation differ.

### Questions
1. The article proposes three mismatch scenarios and then establishes a unified framework. What are the commonalities among the three mismatch scenarios? Please give more explanations about how to build a unified framework to deal with these scenarios.

### Soundness
3

### Presentation
3

### Contribution
3
