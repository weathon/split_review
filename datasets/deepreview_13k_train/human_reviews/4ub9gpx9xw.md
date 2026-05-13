# Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Large language models (LLMs) are capable of generating *plausible* explanations of how they arrived at an answer to a question. However, these explanations can misrepresent the model's "reasoning" process, i.e., they can be *unfaithful*. This, in turn, can lead to over-trust and misuse. We introduce a new approach for measuring the faithfulness of LLM explanations. First, we provide a rigorous definition of faithfulness. Since LLM explanations mimic human explanations, they often reference high-level *concepts* in the input question that purportedly influenced the model. We define faithfulness in terms of the difference between the set of concepts that the LLM's *explanations imply* are influential and the set that *truly* are. Second, we present a novel method for estimating faithfulness that is based on: (1) using an auxiliary LLM to modify the values of concepts within model inputs to create realistic counterfactuals, and (2) using a hierarchical Bayesian model to quantify the causal effects of concepts at both the example- and dataset-level. Our experiments show that our method can be used to quantify and discover interpretable patterns of unfaithfulness. On a social bias task, we uncover cases where LLM explanations hide the influence of social bias. On a medical question answering task, we uncover cases where LLMs provide false claims about which pieces of evidence influenced its decisions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to measure the faithfulness of LLM generated natural language explanations in terms of specific concepts mentioned in it. Specifically, faithfulness is measured by the correlation between the causal effect of a concept (measured by counterfactual predictions) and the likelihood of the concept being mentioned in the explanation. This analysis produces several interesting results, e.g., the model doesn’t mention gender in its explanation despite gender having large causal effect on its prediction; safety alignment can affect model explanation.

### Strengths
- Inspecting more finegrained faithfulness is a novel contribution and it allows us to gain better understanding of specific biases in model explanations.
- The paper proposes a principled method to quantify faithfulness based on counterfactual examples.
- The finding that safety alignment can make the model hide true reasons (e.g., gender bias) in its explanation (thus is only a form of shallow alignment) is very interesting.

### Weaknesses
 - It is unclear how the explanations are generated, e.g., are these CoT from zero shot or few shot prompting? Is explanation generated before or after model prediction? It would be interesting to analyze how different prompting methods change the result or improve faithfulness.

Minor:
- 152: distinct -> disentangled might be a more precise word
- 194: typo: x in the equation should be in vector form

### Questions
- Here the causal concept effect is considered the ground truth in some sense. Then would it make sense to directly explain the model prediction using the causal concept effect?
- For the dataset level faithfulness, instead of averaging question level faithfulness, why not directly measure PCC of all examples in the dataset?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
**Summary**:
This paper adopts a causal inference approach to define and evaluate the faithfulness of LLM-generated explanation in the context of two question answering tasks. The obtained results X.

**Main contributions**: The main contributions are the definition and methodology proposed to assess the faithfulness of explanations.

**Methodology**:
- Key to the methodology is the assumption that a model is faithful if its explanations consist of only concepts that are impactful for the decision (i.e., have large causal effects) (lines 183-185).
- The authors first compute the causal effect associated with each concept in the explainability (CE). An auxiliary LLM is used to determine the _explainable_ concepts and produce counterfactual perturbations for each input x. CE is then estimated by contrasting the distributional differences between LLM responses when given the modified inputs vs the original inputs.
- Then the authors determine the prevalence of each concept appearing in the explanation (EE).
- Finally, the authors determine the linear alignment between CE and EE (dubbed causal concept faithfulness) for each example using the pearson correlation coefficient. Dataset-level faithfulness score is the average over the examples.

**Writing**: Overall the writing is clear and easy to follow! The authors did a good job in exposing the ideas. Consider the following comments to further increase clarity:
- Add information about when the experiments were run with each model.
- lines 321-323: you describe the colors for each of the concept categories. However there seems to be a mismatch between the category color in the image and the color described in text.

### Strengths
-  Causally inspired definition and methodology to assess the faithfulness of LLM-generated explanations.
- Empirical validation of proposed methodology in two different question answering datasets.
- The finding that GPT-3.5 produces more faithful explanations (at a dataset-level) than the more recent and advanced models (GPT-4o and Claude 3.5 sonnet) is interesting. They also show that unfaithful explanations by GPT-3.5 is more harmful than GPT-4o
- The analysis concerning the impact of different types of interventions (i.e., remove concept vs swap it with a different value) is interesting, revealing the brittleness of safety guards employed in GPT-3.5 and GPT-4o.

### Weaknesses
1. **Insufficient validation of the proposed approach**: the authors mention that their method can be used to quantify and discover interpretable patterns of unfaithfulness. However, there is no guarantee that the methodology detects truly unfaithful concepts. To further ensure the correctness of the approach, it would be nice to show linear agreement between CE and EE in a controlled setting where LLMs are known to only produce faithful explanations (e.g., unbiased setting). It's crucial to demonstrate that the method doesn't falsely identify faithful explanations as unfaithful, which could be achieved by testing on a dataset where the ground truth faithfulness is known or strongly expected.
2.  **Important parameters of the experiments are not clear in the paper, which may affect reproducibility of the experiments**. The authors could consider providing additional details about the exact number of perturbations generated for each example, the number of generations used to estimate P(Y|X) (during the definition of CE), the decoding hyperparameters (including the temperature and max number of tokens). Additional details should also be provided about how each response y is parsed – this is particularly relevant given that the evaluated models are known to produce nuanced and semantically equivalent texts. The lack of these details makes it difficult to reproduce the results and assess the reliability of the findings.
2. **Small evaluation set and concerns about generalizability**: for the two question-answering, the authors estimate the causal effects (CE) and explanation-implied (EE) effects for 30 examples (using 50 generations per each dataset). However, it is unclear how robust these results are and whether these would generalize to larger models.  Perhaps the authors could show how the faithfulness score varies as the number of datapoints increases, therefore, providing an idea of the variability and stability of the scores. This small sample size raises concerns about the statistical power of the results and whether the observed trends are truly representative.
3. **Univariate counterfactuals**: if I understood correctly, the proposed framework focuses on perturbing the sentences one concept at a time, irrespective of the correlations between features. However, this fails to account for the correlations between different features (e.g., name of schools or organizations is related to socio-demographic features). The method's inability to handle correlated features could lead to inaccurate causal effect estimations, as the effect of one concept might be confounded by the presence of other related concepts.
4. **Generalizability to open-source models**: the paper carries analyses on two OpenAI models (GPT-3.5, GPT-4o) and one Anthropic model (Claude-3.5-sonnet). Could be interesting to contextualize the faithfulness of existing open source models (e.g., Llama 3.1) and draw comparisons with closed-source ones. The lack of evaluation on open-source models limits the generalizability of the findings and their applicability to a wider range of LLMs.

### Questions
1. One of the decisions in the paper is to use an auxiliary model to extract concepts, propose a list of alternative values for each concept. Why is this necessary and is there any assumption or requirement that helped settling for a GPT-4o as the auxiliary LLM? The authors could better motivate the selection of GPT-4o in their paper, perhaps by including a small human study comparing the effectiveness of different models in extracting concepts and creating the list of alternate values. The authors should also consider including the prompt used to extract concepts and concept values in the Appendix.
2. In line 218, the authors mention the use of auxiliary LLM to “list distinct concepts in the context of x”. What kind of verifications were performed to ensure that the extracted concepts and their list of concepts were meaningful? The authors should consider adding a list of extracted concepts and their list of values to the Appendix. They should also consider adding more details about the validation (e.g., manual validation or llm-as-a-judge approach).
3. Similarly, to the two questions above, in line 224-225, the authors mention “to generate each counterfactual, we instruct [auxiliary LLM] to edit the question x by changing the value of [concept] ..., while keeping everything else the same”. However there seems to be no validation of this claim. Did the authors validate that the perturbed input x was indeed minimally distant from x? If not, the authors should consider including such analysis, perhaps by showing the minimum edit distance or n gram overlap between the modified and original inputs.
4. Why did the authors select a linear correlation coefficient as opposed to a non-linear coefficient?
5. In Figure 1 (right), we observe that different behavioral concepts end in different regions of the scatter plot (there are orange points in the top and orange points around EE in [-0.5, -1.5]. Is there any insight or pattern that justify why there are different clusters? Could it be that the model is less prone to use some concepts for specific demographics?

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
A formulation of faithfulness is presented called causal concept faithfulness. According to this formulation, when a model produces a natural language explanation of its behaviour that appeals to certain concepts (e.g. gender), altering the input to have a different concept value (e.g. changing the gender of person mentioned in the text), should also alter the behaviour. Thus, under this formulation, a model is faithful if and only if it appeals to exactly those concepts that—if altered—would actually change its behaviour. To measure faithfulness the correlation between two metrics is used: (1) the probability that a concept is mentioned in an explanation; and (2) the actual change after altering the inputs, the KL divergence between the model's output distribution before and after alteration is used. 
To avoid having to measure these values on very large datasets, the authors propose to use a Bayesian hierarchical model, which 'partially pools' information across interventions for related concepts.
Experiments are performed on two tasks. The first is a task designed to elicit unfaithful explanations. Models perform poorly w.r.t. two out of three concepts. In the second task, models are shown to have limited faithfulness when explaining their answers for medical question answering.

### Strengths
- Precise definition of what is meant by faithfulness.
- 'causal concept faithfulness' as proposed will be useful for the explainability community.
- The paper is written well, while being information-dense.

### Weaknesses
 - The use of GPT4o to generate counterfactual inputs is not evaluated independently.



### Questions
- In Figure 1, it appears as though the correlation between EE and CE would be significantly lower if done independently for each concept, and then averaged. My question is: is calculating faithfulness on a per-concept basis is possible with your method?
- And a related question, given that pearson correlation only measures to what extent points lie on *a* line, and not on *the* line y=x, is it the most appropriate metric for you use case, did you consider others?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates ‘unfaithfulness’ of SOTA LLMs. In this paper, the authors introduce a new metric for measuring the faithfulness of a model, namely, causal concept faithfulness that not only quantifies but also reveals semantic patterns of unfaithfulness. To uncover these patterns, they put this method to the test on two tasks - a social bias task and a medical QA task to demonstrate how decisions made by the models change along with the provided explanations to justify the wrong decisions made by the model.

### Strengths
I really enjoyed reading the paper! It addresses a highly relevant topic of faithfulness in the current landscape of AI. The writing is engaging and clear. 

One of its standout features is its approach to a critical issue: it offers a concrete and measurable method for assessing explanation faithfulness in large language models, an area that has been difficult to define in previous research. By introducing the concept of causal concept faithfulness, the authors provide a way to evaluate how "honest" a model's explanations are, while also revealing specific patterns of misleading explanations.

### Weaknesses
 **High level comments**
1. It remains uncertain whether biases impact all types of reasoning tasks uniformly or if certain domains are more affected than others.
2. Moreover, the experiments do not specify how these findings may apply beyond classification tasks to biases that could affect other generative tasks.

***Minor comment***
Line 321 typo -> should be orange for behavior, red for identity

### Questions
1. Can a faithful explanation be biased? For example, suppose if both CE and EE are high for the example in Table 1, and if the model would have answered Male: 26% Female: 74%, with Explanation References: Traits/Skills: 15% Age: 0% Gender: 85%. This is a clear case of gender bias, but can we say the explanation is faithful here referring to Definition 2.3?
2. How can we understand the observations if the models memorized these benchmark datasets during their training stage? Does this imply that the model’s reasoning process is so vulnerable to bias that it can even disregard a previously memorized correct answer?

### Soundness
3

### Presentation
4

### Contribution
3
