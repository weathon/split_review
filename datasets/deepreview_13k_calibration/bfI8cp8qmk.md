# Perturbation-Restrained Sequential Model Editing

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Model editing is an emerging field that focuses on updating the knowledge embedded within large language models (LLMs) without extensive retraining.
However, current model editing methods significantly compromise the general abilities of LLMs as the number of edits increases, and this trade-off poses a substantial challenge to the continual learning of LLMs.
In this paper, we first theoretically analyze that the factor affecting the general abilities in sequential model editing lies in the \emph{condition number} of the edited matrix.
The condition number of a matrix represents its numerical sensitivity, and therefore can be used to indicate the extent to which
the original knowledge associations stored in LLMs are perturbed after editing.
Subsequently, statistical findings demonstrate that the value of this factor becomes larger as the number of edits increases, thereby exacerbating the deterioration of general abilities.
To this end, a framework termed \textbf{P}erturbation \textbf{R}estraint on \textbf{U}pper bou\textbf{N}d for \textbf{E}diting (PRUNE) is proposed, which applies the condition number restraints in sequential editing.
These restraints can lower the upper bound on perturbation to edited models, thus preserving the general abilities.
Systematically, we conduct experiments employing three popular editing methods on three LLMs across four representative downstream tasks.
Evaluation results show that PRUNE can preserve considerable general abilities while maintaining the editing performance effectively in sequential model editing.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper analyzes how the condition number of the edited matrix affects the models' sensitivity to perturbations and proposes a framework called PRUNE to impose constraints that lower this sensitivity. Experiments demonstrate that PRUNE effectively preserves the general abilities of LLMs while maintaining strong editing performance across various tasks.

### Strengths
* Sequential editing is indeed a crucial research issue in knowledge editing, and this paper examines it from a relatively comprehensive perspective while proposing an excellent solution.

* The literature review is thorough.

* The evaluation scope is extensive, based on three representative LLMs, including GPT-2 XL, LLaMA-2, and LLaMA-3. It also includes four representative downstream tasks—reasoning, summarization, open-domain question answering, and natural language inference—to broadly demonstrate the impact of model editing on the general abilities of LLMs.

* The performance of the method proposed is good, effectively mitigating the decline in model general abilities caused by sequential edits across multiple metrics.

### Weaknesses
Many choices and decisions made in the paper seem unmotivated or not explained properly. I defer to the questions sections where clarifications are requested. I am happy to revise my review post the discussion period once the questions have been answered.

 1. In section 3.2, where the authors perform matrix perturbation analysis, it is not clear to me how that is relevant. The main objection I have is that if an MLP layer in a model is edited, everything until that layer remains the same. This means that "keys", which are by definition input to the edited matrix, remain identical before and after editing. Then I'm not sure what is the meaning of ∆k here, since the value of k never changes when an edit is made.

 2. In line 241, the spectral norm definition is used, whereas line 203 says that ||*|| represents 2-norm.

 3. The hypothetical situation described in line 271-275 is not clear to me. Does the situation involve making N sequential edits about the same fact? If that's the case, then each edit matrix will not be equal to ∆W_1 as the value of ∆W_1 depends on the base matrix, which would be been changed. Although I understand that this is not important in the larger scheme of things, I think it is not correct. I am happy to provide more explanation.

 4. In Table 4, we can see that the singular value of the edited matrix increases way more dramatically for MEMIT compared to other methods. Why is that the case? Also it makes me question that the singular values are the only underlying cause for model degradation, as if that was the case, since MEMIT has the largest singular value blow up, it would be the least stable and see maximum model degradation. But that is not the case, in fact MEMIT is the most stable of the three. What is the author's take on this?

 5. In equation 4 and 5, I would like some more intuition and explanation of the choice of restraining function. It is not obvious to me why the log function suggested by them works. I think this part of the paper has the least detail whereas I would have preferred a lot more detail here. For example, I would like to see more ablations on the different actions that can be performed on the larger singular values of the ∆W_N matrix.

 6. From an intuitive understanding, this paper tries to attenuate the largest singular values of the edit matrix. But the largest singular values are the most important part of a matrix, providing the direction of largest variance and loosely speaking is the direction along which the most significant action is done by the matrix. How is attenuating the most significant action of a matrix not resulting in a lot of issues? Why is it okay to attenuate the largest singular values of a matrix? I think this is a much deeper question and warrants investigation.

 7. The experiments shown in Figure 3 and 4 involve too few sequential edits. This method will be a lot more believable if the authors presented results for atleast 1000 edits, but preferably even more.

My final comment to the authors is that while this paper presents an interesting empirical contribution and figure 5 makes a very good empirical case for usefulness, I have a hard time understanding why the approach proposed by the authors works (questions 4-6). I do not find the explanations or motivations given in the paper appropriate so far. I am looking forward to hearing the author's comments during the discussion phase and am very happy to update my scores based on it if the authors are able to sufficiently clarify these questions.

### Questions
Please see the Weaknesses section above.

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
This paper investigates the capability of large language models (LLMs) to preserve their general knowledge after sequential editing through a plug-and-play framework named PRUNE. The authors suggest that the condition number of the edited matrix significantly influences the general abilities of the edited models. They propose a method which involves SVD decomposition to ensure that the updated matrix maintains the singular values of the original matrix, thereby preventing substantial perturbations. The paper evaluates the effectiveness of this method across three popular editing methods and three large language models

### Strengths
1. Knowledge editing is an important topic, and addressing sequential editing is a challenging yet meaningful direction.
2. This paper is well motivated and the design of PRUNE clearly explained.
3. This paper proposes a plug-and-play method, which demonstrates significant improvements in sequential editing across various models.

### Weaknesses
1.  Some important details need further clarification. For example, in the editing setup, the key $k$ in the key-value pair $(k, v)$ typically does not change, and usually only $W$ and $v$ are modified. It is unclear why the paper focuses on analyzing the changes in $k_i$ instead of $v$ or $W$.
2.   The PRUNE method imposes constraints on parameters (as described in Equations (3), (4), and (5)), which might potentially reduce the model’s ability to retain other capabilities or preserve historical knowledge. However, the paper lacks sufficient analysis and investigation of the potential negative impacts on the efficacy of the most recent knowledge edits. A more detailed discussion in this regard would improve the overall quality of the analysis.
3.   A comparison with other sequential editing methods should be included in the related work section. Moreover, additional discussion is needed on works aiming at preserving the general capability of an edited model.
4.  The model requires utilizing historical $\Delta W$ in each editing operation, meaning that historical information must be reused. This could potentially lead to an increase in computational resources.

### Questions
See weaknesses.

### Soundness
3

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
The research tackles the issues that arise due to weight shifts in sequential model editing when using weight-modifying approaches. The authors present a new approach, PRUNE, which aims to stabilize editing by maintaining control over these shifts. Importantly, the paper proposes an upper bound on weight modifications, beyond which the model's original capabilities degrade, resulting in reduced performance and an inability to retain edits. This bound serves as a theoretical safeguard, ensuring that model modifications remain within an optimal range for consistent, reliable performance.

### Strengths
The paper introduces a theoretically derived upper bound for weight modification. By defining this threshold, the authors provide a quantitative limit which when exceeded, triggers degradation in the model’s original functions and leads to edit forgetting. This contribution deepens understanding of the trade-offs involved in weight modification and offers a practical guideline for preserving model performance.

The authors demonstrate that PRUNE effectively mitigates the negative impacts of sequential edits. PRUNE shows considerable performance improvement by stabilizing the model against shifts in weight values, which may otherwise lead to inconsistencies or loss of prior knowledge.

### Weaknesses
The study focuses solely on the Llama-2 (7B) model, with a relatively small set of samples for evaluation which is a concern as editing in large numbers might exacerbate the impact of the shift that needs to be controlled. To broaden the scope, the authors could consider using a smaller model from the GPT series or a single editing approach, allowing for an expanded sample size under computational constraints. This could strengthen the study by providing more robust evidence for PRUNE’s effectiveness across different architectures. (major)

While PRUNE is effective, some edits may still be lost in the process, particularly when just applying the operation. A deeper analysis of this limitation could provide valuable insights. (minor)

### Questions
The PCA visualization discrepancy is not entirely clear maybe a slightly modified visualization would clarify what is being referred to. 

The baseline capabilities of Llama on general abilities in Table 2 are missing.

### Soundness
3

### Presentation
2

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
Knowledge editing methods when applied sequentially lead to significant model degradation. In this paper, the authors identify the reasons behind the loss of model's general abilities in the form of increasing singular value of edit-matrix as a function of the number of edits, and propose methods to control that.

### Strengths
1. The authors provide an interesting analysis of the potential reasons behind the loss of general ability of a model as it is edited sequentially. 
2. The proposed methods is plug and play and can be applied on top of all existing parameter modifying model editing methods.

### Weaknesses
Many choices and decisions made in the paper seem unmotivated or not explained properly. I defer to the questions sections where clarifications are requested. I am happy to revise my review post the discussion period once the questions have been answered.

### Questions
1. In section 3.2, where the authors perform matrix perturbation analysis, it is not clear to me how that is relevant. The main objection I have is that if an MLP layer in a model is edited, everything until that layer remains the same. This means that "keys", which are by definition input to the edited matrix, remain identical before and after editing. Then I'm not sure what is the meaning of ∆k here, since the value of k never changes when an edit is made. 

2. In line 241, the spectral norm definition is used, whereas line 203 says that ||*|| represents 2-norm. 

3. The hypothetical situation described in line 271-275 is not clear to me. Does the situation involve making N sequential edits about the same fact? If that's the case, then each edit matrix will not be equal to ∆W_1 as the value of ∆W_1 depends on the base matrix, which would be been changed. Although I understand that this is not important in the larger scheme of things, I think it is not correct. I am happy to provide more explanation. 

4. In Table 4, we can see that the singular value of the edited matrix increases way more dramatically for MEMIT compared to other methods. Why is that the case? Also it makes me question that the singular values are the only underlying cause for model degradation, as if that was the case, since MEMIT has the largest singular value blow up, it would be the least stable and see maximum model degradation. But that is not the case, in fact MEMIT is the most stable of the three. What is the author's take on this?

5. In equation 4 and 5, I would like some more intuition and explanation of the choice of restraining function. It is not obvious to me why the log function suggested by them works. I think this part of the paper has the least detail whereas I would have preferred a lot more detail here. For example, I would like to see more ablations on the different actions that can be performed on the larger singular values of the ∆W_N matrix. 

6. From an intuitive understanding, this paper tries to attenuate the largest singular values of the edit matrix. But the largest singular values are the most important part of a matrix, providing the direction of largest variance and loosely speaking is the direction along which the most significant action is done by the matrix. How is attenuating the most significant action of a matrix not resulting in a lot of issues? Why is it okay to attenuate the largest singular values of a matrix? I think this is a much deeper question and warrants investigation. 

7. The experiments shown in Figure 3 and 4 involve too few sequential edits. This method will be a lot more believable if the authors presented results for atleast 1000 edits, but preferably even more. 

My final comment to the authors is that while this paper presents an interesting empirical contribution and figure 5 makes a very good empirical case for usefulness, I have a hard time understanding why the approach proposed by the authors works (questions 4-6). I do not find the explanations or motivations given in the paper appropriate so far. I am looking forward to hearing the author's comments during the discussion phase and am very happy to update my scores based on it if the authors are able to sufficiently clarify these questions.

### Soundness
1

### Presentation
3

### Contribution
2
