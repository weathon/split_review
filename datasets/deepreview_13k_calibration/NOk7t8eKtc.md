# Extracting and Transferring Abilities For Building Multi-lingual Ability-enhanced Large Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 5, 8, 6

## Abstract
Multi-lingual ability transfer has become increasingly important for the broad application of large language models~(LLMs). 
Existing work highly relies on training with the multi-lingual ability-related data, which may be not available for low-resource languages. To solve it,  we propose a \textbf{M}ulti-lingual \textbf{A}bility \textbf{E}xtraction and \textbf{T}ransfer approach, named as \textbf{MAET}. Our key idea is to decompose and extract language-agnostic ability-related weights from LLMs, and transfer them across different languages by simple addition and subtraction operations without training. 
Specially, our MAET consists of the extraction and transfer stages. In the extraction stage, we firstly locate key neurons that are highly related to specific abilities, and then employ them to extract the transferable ability-specific weights. In the transfer stage, we further select the ability-related parameter tensors, and design the merging strategy based on the linguistic and ability specific weights, to build the multi-lingual ability-enhanced LLM.
To demonstrate the effectiveness of our proposed approach, we conduct extensive experiments on mathematical and scientific tasks in both high-resource lingual and low-resource lingual scenarios. 
Experiment results have shown that MAET can effectively and efficiently extract and transfer the advanced abilities, and outperform training-based baselines methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Given that related work mostly trains LLMs with ability-related corpus in target languages, which is relatively rare in low-resource languages, the authors propose MEAT, an approach to multilingual ability extraction and transfer. The basic idea is to identify the "ability-specific weights" inside the LLMs, and decompose them from the "language-specific" ones. By examining the weight changes after a post-pretraining phase, it identifies the top-k neurons as the "key neurons". Then, it trains the key neurons on two different corpora, and further obtains ability-specific weights for the identified key neurons. Finally, it conducts the cross-lingual ability transfer by weighted average among several weights that are trained on various corpora. Experimental results show that MEAT outperforms continual pre-training, domain adaptation and task vector approaches on the multilingual mathematical and scientific tasks.

### Strengths
- Multilingual LLM is an important research area for improving the accessibility of LLMs for non-English users. Obviously, current LLMs are not good at processing non-English tasks, especially in low-resource languages. Thus, research on how to transfer abilities or knowledge to low-resource languages is meaningful.
- Identifying and decomposing the "ability-specific" weights of LLMs is an interesting idea, which would potentially further enhance the more types of capabilities of LLMs in low-resource languages.
- Experimental results show that MEAT outperforms continual pre-training, demonstrating its effectiveness on cross-lingual transfer.

### Weaknesses
 - Although there are few human-labeled multilingual instruction data (aka ability-specific data, or downstream task data), synthetic data generation is currently a practical way towards multilingual LLMs. For example, the translate-train method is a simple and strong baseline for multilingual tasks [1] [2], which simply translates the instruction data into other languages, achieving significant improvements. Another way to synthesize data is to prompt LLMs (e.g., GPT-4) to generate multilingual responses such as Bactrian-x [3]. Besides, the translate-test pipeline is also commonly used in multilingual evaluation (e.g., MEGA [4], XLM-R [5]). Therefore, it is necessary to clarify why we should use MEAT rather than these common approaches.
- Some terms used in the paper are confusing. There are "ability-related weights", "key neurons", "ability-specific weights", "ability-related tensors", and "language-specific weights" mentioned in the paper, and the relation and differences among the terms are not clear. For instance,  what the difference is between "ability-specific weights" and "ability-related weights".  At L236, R(L_1) is a typeof ability-related weights, and R(A_i) is a type of ability-specific weights according to Eq (2). What is the language-specific weight mentioned at L054?
- Minor: In Table 5 (Appendix), both stages are labeled as "Extraction".

### Questions
Please clarify the relations and differences among "ability-related weights", "key neurons", "ability-specific weights", "ability-related tensors", and "language-specific weights".

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel method to enhance the multilingual capabilities of large models, providing the model with new abilities through both the extraction and transfer stages. In the extraction stage, MAET sequentially identifies key neurons and learns ability-specific weights. In the subsequent transfer stage, MAET selects ability-related parameter tensors, which are then used to construct a multilingual ability-enhanced LLM. Experiments have shown that MAET is better than some existing continuous pre-training methods in multilingual mathematics and science tasks.

### Strengths
-	A novel multilingual enhancement scheme that offers valuable inspiration for future research.
-	The technical solution is sound, and the details, such as the method for cumulative gradient, are well thought out.

### Weaknesses
 - Although the technical contribution of this paper is novel, the experiments are relatively limited and do not fully validate the proposed contributions. For instance, the paper only tests the effect of using LLaMA-3 as the backbone, but as a general LLM enhancement technology, this scope is insufficient. I understand that training large models requires significant resources, but there are many existing smaller LLMs worth experimenting with, such as Qwen2.5-0.5/1.5B and Gemma2-2B.
- The choice of some hyperparameters is not clear, such as \mu in equation (3).
- This paper involves many abbreviations. It is recommended to bold the first appearance of the baseline and dataset names in Section 5.1 for clarity.
- The related work on model merging is missing key citations [1][2], which demonstrate significantly better performance on multilingual mathematical tasks (MGSM dataset). The authors should reference these studies and engage with their findings in the discussion.

### Questions
-	Is the “Ability-related Parameter Tensor Selection” in Section 4.2 more closely related to the extraction stage in Section 4.1 rather than the transfer stage?
-	The concepts of “tensor selection” and “parameter weights” are easily confused. Can add examples or annotate the dimensions to distinguish them?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a novel solution towards enhancing a specific ability for low-resource languages. Their method MAET requires a multi-lingual general corpus and an ability-specific corpus from a single language (e.g., English). After extracting ability-related weights, the related parameter tensors can be readily patched to improve multi-lingual performance. Results and ablations have shown the effectiveness of MAET. Analysis provides insights onto the possible location of ability-related parameters.

### Strengths
- **Novelty**: key units are identified to implement sparse update in model training and merging.
    - In the extraction stage, key neurons and ability-specific weights are identified.
    - In the transfer stage, ability-related parameters are further filtered by their similarity with language-related parameters.
- **Concrete experiments**: ablations establish the necessity of each component in MAET.
- **Insightful analysis**: the detailed analysis provides insights.

### Weaknesses
 - A useful and strong baseline would be to include a multi-lingual ability-related corpus for training. 
    - This can be obtained by translating $C_{{L_0}, A_i}$ to $C_{{L_j}, A_i}$ for other languages $j$.

### Questions
- Can you explain how domain adaptation is done?

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
This paper seeks to combine multilingual abilities and other "abilities" together when ability-specific data is not available in a particular low-resource target langauge. In order to do so, they propose a solution that involves first finding the parameters that are most important for the "ability" by finding the most important continually pretraining separate variants of a base LLM, one on generic multilingual data and the other on ability-specific data, typically in English. Then, they extract what parameters are holding the learned information by evaluating which parameters changed most for each. Using these parameters, they then merge the two variants together to create a model that has boosted capabilities in the target task in the target language. They evaluate this method across numerous LLMs, two tasks (math & science), four languages, and evaluate numerous baselines, all of which show the effectiveness of MAET.

### Strengths
1. This paper extends previous work on task vectors and outline a novel methodology to extract parameter updates most important to language capabilities and to a specific domain/task. This meticulously designed methodology then allows for combining model updates in a matter that alleviates parameter interference.
2.  The experiments are impressively thorough: they cover multiple models, two tasks, many possible CPT setups, and a small, but diverse set of languages. This extensive experimentation clearly took significant resources and effort. The results show MAET is effective and comparable to different possible full CPT setups.
3. The results show that MAET is significantly more effective than the well-established model merging method from Ilharco et al., 2023, which does arithmetic over task vectors.
4. Interesting secondary findings, which they detail in Section 5.3.
a) One is the parameter location that they find to be most important (Line 474-482). This aligns with previous literature, but they come to this conclusion in a very different manner
b) The second is the fact that MAET is much more successful in not "forgetting" other domains/tasks in comparison to full CPT. This would need further experimentation to control for overfitting in both settings, but this is a very promising avenue for why MAET would be impactful.

### Weaknesses
 1. Shortcomings of neuron locating strategy:

a) I don't think that the value change of neurons is an appropriate approximation for accumulated gradients. The value change maps the net trajectory taken after many gradient updates, versus the accumulated gradient is the mean gradient across different data points. At minimum, you could remove mention of accumulated gradients and state that value change is the desired method for estimating neuron importance. Furthermore, the method of using the absolute value of the change is also questionable, as it does not distinguish between positive and negative changes, which could be important for understanding the direction of influence on the neuron.

b) (Line 205) I don't understand why you would train \nu_L_0 and create LLM_{A_i,L_0}. Would it not make sense to simply subtract the language difference from the ability difference and not from the ability & language difference. This step seems unnecessarily complex and lacks clear justification. It's unclear why the language-specific parameters need to be included in the ability-specific model before the subtraction.

c) Is R(A_i) therefore a task vector as in Ilharco et al., 2023 ? This should be mentioned as it is currently very unclear what R(A_i) represents. The authors need to explicitly define the relationship between their approach and existing task vector methods, as the current description is ambiguous.

d) [Most important] Calculating R(A_i) required ability-specific and generic data in English (L_0). In that case, it is very unclear what R(L) is for all other languages and how it was calculated. I thought domain/ability-specific data for these target languages was unavailable ? Authors need to define how exactly R(L) is calculated for languages other than English and if ability-specific data in the target language is used. The lack of clarity on this point is a major concern, as it undermines the core claim of the paper regarding low-resource scenarios.

e) Generally, this section lacks justification and references to justify the methodology, many parts of which feel arbitrary. The choices made in the parameter selection and merging process need to be better motivated with theoretical or empirical evidence.

f) In Line 161, the authors imply they use a small subset of C_{L_0,A_i} and yet Algorithm 1 implies all available data samples in C_{L_0,A_i} are used. This discrepancy needs to be addressed for clarity.

3. This paper positions this method as one to use when data in the target languages is highly limited, and yet they use 1M tokens per language. This is a significant amount of in-language data, undermining the practicality of this method. The claim of low-resource applicability is not well-supported by the experimental setup, as 1M tokens is a substantial amount of data for many truly low-resource languages.

4. Results are not very impressive. Full continual pre-training on all the data available is a much simpler and less computationally expensive method and it performs very close on average. I would argue this average performance is within a hyperparameter-tuning error range — by that I mean is there is likely hyperparameter setups where full continual pre-training data is slightly better across languages and therefore the average is higher than MAET. The same applies to full CPT on just the multilingual data + domain adaptation. I would need more evidence of full effort to maximize performance in comparative scenarios (i.e. CPT scenarios). The lack of a clear performance advantage over simpler baselines significantly weakens the impact of the proposed method.

a) Why is CPT only on the ability data not evaluated ? My intuition is that that would be more effective than CPT on the multilingual generic data only. The absence of this baseline makes it difficult to assess the true effectiveness of the proposed method.

5. The authors have interesting findings in Section 5.3, but do not highlight them and present them as key contributions of the paper. I believe that a possible reformulation of the presentaiton of this work which puts these findings more in focus would lead to a more captivating paper.

### Questions
- I don't recommend the term "ability"/"ability-related" that the authors selected. I would use the term "domain"/"domain-specific" as it is more common and more concise to what you are attempting to do: improve a model's capability in a target domain in a target language.

- Line 43: "dominated the linguistic expressions of the open web data" does not make sense. I would word this differently.
- Line 44, 131: In Bengali and Telugu, there are millions (maybe even billions of samples) available on the open web. I would specify this statement that either the availability of (a) *labeled* data or (b) domain-specific data is highly limited. I think the framing of these languages as low-resource is a stretch given they are some of the 10-20 most spoken languages in the world. I would encourage the authors to emphasize the 
- Line 45: I would include older citations for cross-lingual transfer, a phenomena that has been studied for 5+ years.
- Line 56: Please explain "multilingual ability-enhanced LLM *like building blocks*".
- Line 70: improvement *compared to the base* LLM
- Line 74,336,366: "monolingual" instad of "single-lingual"
- Line 116-123: there are numerous typos
- Line 120: "Despite the fact that"
- Line 160: How small of an amount ? 
- Line 197: You need to recite the TIES-merging paper here
- Line 246: How are you calculating the cosine similarity of a multi-dimensional tensor ? Are you flattening it before calculating the dot product ?
- Line 250: Is sim() the dot product or cosine similarity ?
- Line 336: Use of "L" to mean both LoRA and multilingual general corpus is very confusing
- Line 370: You need to cite the LoRA paper
- Table 3: So if i understand correctly, only merging these specific tensor types individually get you almost the same score ? This seems like a very significant finding, no ?
- Line 470-472: This claim is not explained or justified with references.
- Line 474-482: This also seems like a more significant finding than authors give it credit for.
- Line 539: You need to provide justification for the claim that MAET is applicable to safety alignment.
- Stylistic suggestion: I believe you are overusing "e.g.", for the purpose of reading flow, I would suggest using alternative terms "like", "such as", and sometimes i.e. instead of e.g.

- an high-impact body of work that is highly related yet not discussed is Composable Sparse Fine-Tuning for Cross-Lingual Transfer by Ansell et al.

### Soundness
3

### Presentation
2

### Contribution
2
