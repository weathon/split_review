# Fragile Giants: Understanding Susceptibility of Models to Subpopulation Attacks

- Decision: Reject
- Scores: 5, 8, 5, 6, 6, 5, 8

## Abstract
As machine learning models become increasingly complex, concerns about their robustness and trustworthiness have become more pressing.
A critical vulnerability of these models is data poisoning attacks, where adversaries deliberately alter training data to degrade model performance.
One particularly stealthy form of these attacks is subpopulation poisoning, which targets distinct subgroups within a dataset while leaving overall performance largely intact.
The ability of these attacks to generalize within subpopulations poses a significant risk in real-world settings, as they can be exploited to harm marginalized or underrepresented groups within the dataset.
In this work, we investigate how model complexity influences susceptibility to subpopulation poisoning attacks.
We introduce a theoretical framework that explains how overparameterized models, due to their large capacity, can inadvertently memorize and misclassify targeted subpopulations.
To validate our theory, we conduct extensive experiments on large-scale image and text datasets using popular model architectures.
Our results show a clear trend: models with more parameters are significantly more vulnerable to subpopulation poisoning.
Moreover, we find that attacks on smaller, human-interpretable subgroups often go undetected by these models.
These results highlight the need to develop defenses that specifically address subpopulation vulnerabilities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study highlights that overparameterized models are particularly vulnerable, often failing to detect issues in smaller, interpretable subpopulations. The analysis reveals a strong relationship between model complexity and susceptibility to such attacks, exacerbated by the long-tailed nature of modern datasets. These findings stress the need for subpopulation-specific defenses, as traditional approaches may be insufficient for increasingly complex systems.

### Strengths
1.	The study provides a robust theoretical framework that highlights the vulnerability of locally-dependent mixture learners to subpopulation poisoning attacks. This builds on existing knowledge of how long-tailed data distributions are memorized, offering a deeper understanding of the challenges in defending against these attacks.
2.	The research empirically demonstrates that complex models exhibit significant shifts in their decision boundaries when exposed to subpopulation poisoning. This finding highlights the vulnerability associated with increased model complexity.
3.	The study conducts an extensive empirical analysis of realistic, overparameterized models across diverse real-world image and text datasets. By executing 1,626 individual poisoning attacks on various combinations of dataset, subpopulation, model, and parameters, it robustly establishes that larger models are more susceptible to subpopulation poisoning attacks.

### Weaknesses
1. The paper's novelty is unclear, as prior research, such as that by Jagielski et al., has proposed two methods for defining subpopulations: one based on data annotations and the other using clustering techniques. The authors then use this foundation to establish Theorem 1, which seems unchallenging.

2. The authors assert that "In this model, subpopulations have distinct supports, meaning that each data point is associated with only one subpopulation." However, in real-world datasets, some data points may belong to multiple subpopulations.

3. The authors' analysis focuses on a specific type of poisoning attack, where the adversary targets a subpopulation. This approach does not consider other poisoning attack methods, such as backdoor attacks, which rely on modified samples with artificial triggers. As a result, it becomes challenging to understand how the strength of an attack varies across different subpopulations and model sizes.

### Questions
1. What is the attack scenario that the adversary knows the specific subpopulation within the mixture distribution to which the validation samples belong?

2. The authors focus on binary classification. How would this approach apply to a more complex task? Would it still be effective?

3. In Figure 5b, ResNet 50 appears to be more vulnerable to subpopulation attacks than ResNet 101. Could you elaborate on the reasons for this difference?

4. The authors conduct 1,626 individual poisoning attacks across various combinations of dataset, subpopulation, model, and alpha. I’m curious if different poisoning attack methods yield varying effects on the models. Could you elaborate on that?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors explore the relationship between subpopulation attacks and the complexity/overparameterization of machine learning models. Subpopulation attacks are a form of model poisoning attack in which an adversary targets a specific distribution instead of isolated samples and aims to degrade model performance on that specific distribution without significantly impacting the overall performance of the model. The authors theoretically and experimentally proved that ML models that exhibit local dependence (including larger and overparameterized models) are more susceptible to subpopulation attacks. Although the paper focuses on subpopulation attacks, I believe that this work could be helpful in improving fairness-aware ML.

### Strengths
1. Theoretical explanations for local dependence vs. susceptibility to subpopulation attacks are supported by experimental results.
2. The experimental setup contains different types of dataset (tabular, image, and text), which strengthens the authors' claim.

### Weaknesses
1. The authors consider only the binary classification case, which limits the full exploration. This is a significant limitation as many real-world problems involve multi-class classification, and the dynamics of subpopulation attacks could differ substantially in such scenarios. For instance, the attack might be more effective in some classes than others, or the transferability of the attack across classes might be an important factor. Furthermore, the decision boundaries in multi-class scenarios are more complex, and the impact of local dependence on these boundaries needs to be investigated.


### Questions
1. Do you think subpopulation attacks could be used to measure fairness in ML? Or are ML models that incorporate bias removal less susceptible to subpopulation attacks? 
2. Is it possible to detect and/or mitigate local dependence?
3. Could one subgroup be affected by the subpopulation attack target another subgroup due to their "closeness"?
4. Page 1, line 053: repetition of "more". Page 10, line 535: missing full stop.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a subpopulation poisoning attack targeting specific subgroups within data, exploiting the complexity of overparameterized machine learning models, which can inadvertently memorize and misclassify these subgroups. The paper reveals the relations of the attack success and model complexity and subgroup size.

### Strengths
- S1: The paper explores some key parameters of learning including model complexity and learning of similar inputs.
- S2: the paper is easy to read.

### Weaknesses
 - W1: It is unclear how the subgroups are identified.
- W2: The significance of the work over the existing work is not clear. Also, these observations look consistent with the understanding of general supervised training.
- W3: The approach is limited to discriminative models.

### Questions
- Q1: Are subgroups manually identified (Line 306) or automatically clustered (Line 205)?

### Soundness
2

### Presentation
2

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
This paper examines the vulnerability of machine learning models of various sizes to subpopulation poisoning attacks. The authors develop a theoretical framework to explain why overparameterized models are particularly susceptible to these attacks. They then conduct extensive experiments across multiple models and datasets, showing that more complex models are indeed more vulnerable to subpopulation poisoning. Additionally, the paper highlights the challenges in developing effective defenses to mitigate these specific vulnerabilities.

### Strengths
- The topic of understanding subpopulation attacks is interesting.
- The authors provide valuable insights, such as the finding that larger models are more susceptible to subpopulation attacks.
- Extensive experiments strengthen the credibility of the conclusions.

### Weaknesses
 - The definition needs more illustration.
- The generalizability of the conclusions is not entirely clear.

### Questions
Definition 2 needs more detailed explanation. Specifically, what does f_p represent here? Also, what does S_p signify? The authors should clarify these terms when they are introduced to improve readability.

The paper mentions two types of subpopulation definitions: one based on clustering of samples’ latent space representations, and another based on predefined semantic annotations in the dataset. In their evaluation, the authors use subpopulations defined by manual annotations that provide semantic information about the samples. I would like to know if this selection might influence the conclusions—specifically, can the findings in this paper generalize to the first type of subpopulation definition? Additional insights on this point would be helpful.

Another concern is related to generalization. I noticed that the authors adopt a straightforward implementation of subpopulation attacks by flipping labels within the subpopulation. Have the authors tried other, potentially stronger, attack methods? If so, would these different attack types affect the conclusions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores how model complexity influences susceptibility to subpopulation poisoning attacks. The authors first prove that a learning algorithm is naturally susceptible to subpopulation poisoning attacks if it exhibits local dependence (Theorem 1). After that, the authors speculate that modern overparameterized deep learning models (e.g., MLP) also have this vulnerability since most of the existing learning algorithms have local dependency (in some settings) proved in existing works. Besides, the authors empirically verify this understanding through experiments. In particular, the authors also show that this vulnerability varies across different subgroup sizes.

### Strengths
1. The authors attempt to give a deeper understanding and theoretical analysis of existing attacks. It should be encouraged.
2. This is a well written paper. The definitions of symbols and the overall flow are clear.
3. The experiments are sufficient to support author’s statements to a large extent.

### Weaknesses
1. The scope of this paper is limited.
- In this paper, the authors focus only on the subpopulation poisoning attacks. To the best of my knowledge, this particular attack type (rather than the general data poisoning) is still not yet a widely recognized threat. 
- In particular, this paper only focuses on the label flipping subpopulation poisoning attack. It further limits the generalizability of the ideas in this paper.
- The main finding (i.e., that more complex models are more vulnerable to such attacks) seems to be expected. More importantly, the authors do not provide insights on how to exploit some of the understandings found in this paper.
2. There are some potential over-claims.
- Line 19-21: To the best of my knowledge, Theorem 1 is only related to locally dependent learners instead of overparameterized models, not to mention model capacity.
- Line 41-44: missing the type of backdoor attacks [1].
- Line 130-131: please provide references or experiments to show that the previous findings are not necessarily true in subpopulation poisoning attacks.
3. Theorem 1 seems to be a straightforward extension of the one proposed in [2].
4. The authors should discuss potential applications of their findings, instead of simply highlighting the need for more attention for defenses.
5. The authors should also conduct experiments on other types of poisoning attacks, instead of just the label flipping subpopulation poisoning attack.


Minor Comments
1. There are still many typos (e.g., Line 183, Line 204).

### Questions
Please kindly refer to 'Weakness' for more details.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper primarily investigates the relationship between model complexity and vulnerability to subpopulation poisoning attacks. Through theoretical analysis and experimental research, the authors examine how machine learning models of varying complexity (such as neural networks of different sizes) respond to data poisoning attacks targeting on specific subgroups. They discover that as model complexity increases, so does the model's sensitivity to these attacks, particularly for medium-sized subgroups. The research also reveals that very small subgroups are often resistant to effective poisoning attempts.

### Strengths
1. Integrates theoretical framework with empirical analysis, enhancing result validity.

### Weaknesses
1.	While the paper identifies vulnerabilities, it does not provide possible defense strategies to mitigate the risks associated with subpopulation poisoning attacks, which could be improved.
2.	This paper touches on the impact on marginalized groups, and it could benefit from a more in-depth discussion of the ethical implications of subpopulation poisoning attacks and the responsibilities of researchers and practitioners

### Questions
-	Section 5.1 notes that "Small Subgroups are Difficult to Poison," which seems at odds with the conclusion suggesting defenses for subgroup vulnerabilities. The authors should clarify the relationship between subgroup size and vulnerability. The paper concludes that "Larger Subgroups Are Less Affected by Model Size" and "Model Complexity Affects Medium-Sized Subgroups Disproportionately." The authors should further analyze how these findings for medium and large subgroups differ from model performance under traditional data poisoning attacks. This would align the paper's observations with its recommendations and highlight the uniqueness of subgroup poisoning attacks.
-	I am wondering how model interpretability might influence the detection and understanding of subpopulation poisoning attacks, which could be a critical aspect of building trustworthy ML models.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 7

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This manuscript inspects models' robustness against data poisoning attacks and empirically finds that models with more parameters are significantly more vulnerable to subpopulation poisoning. Fine-grained analysis suggests that attack intensity and subgroup size may also influence attack damages.

### Strengths
1. Clearly, a lot of effort has been put into this work. I believe the contribution is sufficient for a publication. The topic of data poisoning attacks is popular, especially in the era of generative AI. 

2. The layout of the paper is clear. Most of the concepts are formally defined or introduced. 

3.  The claims made are grounded by sufficient empirical evidence, as well as fine-grained analysis.

### Weaknesses
No efforts were made to build a defense against the attacks explored, and thus not maximizing social benevolence. 

Intensity of an attack remains undefined.

### Questions
1. What is the intensity of a data poisoning attack? It was used in the paper but not defined/introduced. 

2. It would be nice if the manuscript could talk about how the findings made in this paper can help build a defense even if the defense might not work for all subgroups.

### Soundness
3

### Presentation
4

### Contribution
3
