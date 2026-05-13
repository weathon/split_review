# Revealing and Mitigating Over-Attention in Knowledge Editing

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Large Language Models~(LLMs) have demonstrated superior performance across a wide range of tasks, but they still exhibit undesirable errors due to incorrect knowledge learned from the training data. To avoid this, knowledge editing methods emerged to precisely edit the specific model knowledge via efficiently modifying a very small percentage of parameters. However, those methods can lead to the problem of **Specificity Failure**, where the existing knowledge and capabilities are severely degraded due to editing.
Our preliminary indicates that Specificity Failure primarily stems from the model's attention heads assigning excessive attention scores to entities related to the edited knowledge, thereby unduly focusing on specific snippets within the context, which we denote as the **Attention Drift** phenomenon.
To mitigate such Attention Drift issue, we introduce a simple yet effective method **S**elective **A**ttention **D**rift **R**estriction(**SADR**), which introduces an additional regularization term during the knowledge editing process to restrict changes in the attention weight distribution, thereby preventing undue focus on the edited entity.
Experiments on five frequently-used strong LLMs demonstrate the effectiveness of our method, where SADR can significantly mitigate Specificity Failure in the predominant knowledge editing tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The use of LLMs in real-world scenarios and applications creates the need for procedures to correct and update the knowledge in these models. The aim here is to change the model's knowledge without costly retraining in order to prevent hallucinations or correct obsolete facts without diminishing the model's performance. 
Recently, the research field of knowledge editing has emerged, in which various techniques such as fine tuning, in-context editing, memory-based and locate-then-edit methods have already been proposed. The disadvantage of these methods is that they can negatively influence the model, especially if information of the edited knowledge triple or related content appears in the context. The study in this paper has set itself the task of shedding more light on this phenomenon, investigating its cause and proposing a method to prevent or mitigate this overcompensation of the edited model. In order to investigate the deteriorating specificity performance of an edited model, the authors develop two metrics and show that even a single updated fact can lead to a so-called specificity error.
An examination of these errors leads to the realization that they are  mainly caused by attention activations, the attention module places too  much focus on the edited information (attention drift) and ultimately  predicts an incorrect token. Consequently, the authors propose selective  attention drift restriction (SADR) as a method to mitigate this false focus.

### Strengths
The paper impresses with its consistently comprehensible and stringent argumentation. The authors start with a problem of a current methodology, prove that this problem exists, identify the underlying significant cause and can thus propose a solution method for the problem. The paper is comprehensibly written and error-free throughout, the illustrations and tables are helpful and well chosen. An additional plus is the ablation study, which deals with the trade-off between editing success and specificity.

### Weaknesses
A look at the appendix shows that the experiments for this article were much more extensive than stated in the actual paper. in addition to further details and results of the experiments described, further results for additional editing methods (WISE, MEND) and additional data sets can be found here. A human evaluation is also attached. It is a pity that even the section on limitations and future work did not find space in the main text. A minor weakness of the paper could be that it is not made clearer why the experiments are limited to locate-then-edit methods, although it is emphasized that the specificity error also occurs with meta-learning and parameter-preserving methods.
Typo line 47: Paris

### Questions
•	It is mentioned that there are specificity errors for models of all types. Have parameter preserving or meta-learning methods also been investigated? It might be interesting to know the RS/RM and DNS/DNM scores for methods like GRACE or ICE.
•	I would suggest adding at least the scores for MEMIT and PMET to Table 1

### Soundness
4

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
4

### Summary
This work focuses on addressing the issue of over-attention during knowledge editing in large language models (LLMs). Knowledge editing techniques were developed to correct LLM's error by precisely modifying a small portion of the model's parameters. However, these methods can lead to Specificity Failure, where the model's existing knowledge and capabilities degrade post-editing. From the analysis in the paper, this phenomenon is attributed to Attention Drift, where attention heads excessively focus on edited entities. The authors propose Selective Attention Drift Restriction (SADR), which adds a regularization term to prevent undue shifts in attention during the editing process. Experiments show that SADR effectively mitigates Specificity Failure while maintaining or improving performance metrics like fluency and reliability across multiple LLMs.

### Strengths
1. The specificity is an important problem of the knowledge editing and the proposed method can effectively alleviate this problem.
2. The authors consider the specificity problem comprehensively and conduct a thorough evaluation of SADR against existing methods and models, providing a comprehensive analysis of its performance.

### Weaknesses
1. From the experiment results, the proposed method leads to a performance drop in the generalization, which is actually an important metric in knowledge editing. In my view, this drop may be caused by the attention-learning method as it would make the model focus less on the subject in other contexts. This drawback would deteriorate the contribution of the method.
2. Although the proposed method demonstrates good performance under the specificity metric, I'm not that convinced by the analysis and conclusion of the reason via the attention head. The attention head may be one reason it focuses more on the subject. However, as the editing is conducted at the MLP in some methods, it may also be the editing vector that influences the specificity. 
This can be seen from recent work that the edit vector's direction[1,2], space[1], and norm[2,3] would influence the specificity. For example, if we constrain the updated W, the information flow may not be dominated by huge logits. 
Some works are contemporary work and I don't require the experiment results, but a proper analysis would encourage me to raise my score. 
3. About the decoding constraints, can you provide a comparison between the attention-based and decoding-based constraint[4] methods here?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The author finds that the existing knowledge editing methods tend to  spend over attention on the knowledge that has already been edited. This leads to failure in the model's answers when the edited subject appears in context (Specificity Failure). This article takes the first step towards alleviating specificity failure, which consists of two parts: 1) Investigating the reason for specificity failure; 2) Proposing a new loss function. In the first part, the author first finds that the last token of the edited subject leads to attention drift and then proposes a preliminary solution to alleviate specificity failure. Based on the above findings, this paper proposes a new method (SADR) in the second part, which effectively mitigate the specificity failure.

### Strengths
* The paper is well-motivated: it explores the reasons behind the Specificity Failure observed in edited models, and proposes an effective solution to address this issue.
* SADR is generalizable: by incorporating an additional loss function, the SADR can be applied to various knowledge editing techniques.
* The article is well-structured: it first identifies specificity failure through guided experiments and then delves into the causes of specificity failure. Finally the paper proposes solution.
* The ablation study proves the effectiveness of the method.

### Weaknesses
 **Main Weaknesses**
* *W1*: I suggest conducting additional experiments on Mquake [1] to prove the effectiveness of the method.  Recent research [1] has shown that existing knowledge editing methods are not good at multi-hop editing. For example, when we edit a piece of knowledge from *<CountryX, Prime_Minister, PersonY>* to *<CountryX, Prime_Minister, PersonZ>*, the corresponding knowledge *<CountryX, First_Lady,  PersonY's wife>* should also be changed to *<CountryX, First_Lady, PersonZ's wife>*. Based on the paper's findings, the failure of multi-hop questions is because the edited model's over-attention on the subject CountryX. So I'm curious about whether SADR can effectively solve the above-mentioned problems. It's crucial to evaluate if SADR can prevent the model from focusing too much on the edited subject in multi-hop scenarios, where the edited subject might appear in a different context or relation, and whether the method can generalize to unseen relations involving the edited subject.

**Minor Weaknesses**
* *W2*: I notice that in Line 165, the editing target is represented as $o^*$, while in other places it is represented as $o_{edit}$. Perhaps changing all occurrences of $^*$ to $_{edit}$ can improve the readability of the article.

* *W3*: In Table 2 *Relation*, Equation 3 seems to have extra 'xs'.

**Missing References**
* Knowledge Editing for Large Language Models: A Survey. (2023)
* A Survey on Knowledge Editing of Neural Networks. (2023)

$Ref$:

[1] Mquake: Assessing knowledge editing in language models via multi-hop questions. (2023)

### Questions
**Main Questions**
* *Q1*: It would be better if the author could point out the reasons that lead to attention drift. One possible reference could be: after editing, the norm of the model parameters $\hat{W}$ increases, causing the norm of the hidden layer vector $v^*$ to grow. This leads to an enhanced attention on the last token towards the edited subject.

* *Q2*: Compared to conventional editing methods, how much additional time overhead does SADR incur? I noticed that SADR computes the attention weights for each layer before editing.

**Minor Questions**
* *Q3*: I notice that $\mathcal{L}_{SADR}$ traverses all layers $l$ in Equation (2). So my question is: is it possible to achieve the same result by restricting attention weights of only one or a few layers?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes the Selective Attention Drift Restriction (SADR) method to address the issue of specificity failure in knowledge editing for LLMs. This failure occurs when models, after being edited to modify specific factual knowledge, disproportionately focus on the edited entity, leading to incorrect outputs in related contexts. SADR introduces a regularization term during knowledge editing to restrict excessive attention on the edited knowledge. The method is evaluated on five language models and shows improvements in mitigating specificity failures without significantly affecting edit success rates.

### Strengths
The paper addresses a critical issue in knowledge editing for LLMs, focusing on the problem of specificity failure, which is essential for ensuring model stability after modifications. The proposed SADR method offers a novel extension to existing techniques by dynamically constraining attention heads to prevent over-attention on edited entities, effectively improving specificity. The method is thoroughly evaluated across multiple models and tasks, showing significant improvements in mitigating attention drift while maintaining high edit success rates. Additionally, SADR is versatile and adaptable to various knowledge editing approaches and model architectures, enhancing its applicability in diverse editing scenarios.

### Weaknesses
1. The methods section is overly concise, i.e., Section 4 does not provide a thorough explanation of SADR. For example, why is KL divergence used to constrain the two attention weights in Eq. 2? Is there a theoretical basis or any prior work that can be referenced?

2. While the SADR method shows significant improvements on the Relation and Distract Neighborhood tasks, the performance drop on generalization metrics suggests that the method struggles to balance specificity and generalization. Table 4 shows a general decline in generalization, especially for PM, which dropped by as much as 20 points. Can sacrificing generalization to improve specificity really be considered effectiveness?

3. In Table 6, the max difference with or without head selection is less than 1.5 points (some difference is less than 0.5 points). Could this be due to random fluctuations? Could you provide a significance testing to demonstrate the effectiveness of head selection? Additionally, what would the performance be if a head were selected at random?

4. There is a lack of efficiency analysis. Does using SADR increase computational load, memory usage, or runtime?

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
