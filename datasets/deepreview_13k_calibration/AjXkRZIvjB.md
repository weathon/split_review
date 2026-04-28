# GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 8, 5, 3

## Abstract
Recent advancements in Large Language Models (LLMs) have sparked interest in their formal reasoning capabilities, particularly in mathematics. The GSM8K benchmark is widely used to assess the mathematical reasoning of models on grade-school-level questions. While the performance of LLMs on GSM8K has significantly improved in recent years, it remains unclear whether their mathematical reasoning capabilities have genuinely advanced, raising questions about the reliability of the reported metrics. To address these concerns, we conduct a large-scale study on several state-of-the-art open and closed models.
To overcome the limitations of existing evaluations, we introduce GSM-Symbolic, an improved benchmark created from symbolic templates that allow for the generation of a diverse set of questions. GSM-Symbolic enables more controllable evaluations, providing key insights and more reliable metrics for measuring the reasoning capabilities of models.Our findings reveal that LLMs exhibit noticeable variance when responding to different instantiations of the same question. Specifically, the performance of all models declines when only the numerical values in the question are altered in the GSM-Symbolic benchmark. Furthermore, we investigate the fragility of mathematical reasoning in these models and demonstrate that their performance significantly deteriorates as the number of clauses in a question increases. We hypothesize that this decline is due to the fact that current LLMs are not capable of genuine logical reasoning; instead, they attempt to replicate the reasoning steps observed in their training data. When we add a single clause that appears relevant to the question, we observe significant performance drops (up to 65\%) across all state-of-the-art models, even though the added clause does not contribute to the reasoning chain needed to reach the final answer. Overall, our work provides a more nuanced understanding of LLMs' capabilities and limitations in mathematical reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper creates a novel dataset (GSM-Symbolic) with several different variants to test whether LLMs are capable of generalized reasoning. GSM-Symbolic has several variants which change the numbers involved in the problem and/or removes or adds clauses that change the difficulty level of the problem but not in a way that is too different from the original problem. They benchmark across a number of models and show that many LLMs show significant drops when changing the numbers only slightly or adding irrelevant information.

I have some questions that I raise in the sections below. In particular, I think some of the claims are not fully supported by the provided evidence and that it's not clear that you can make strong, broad claims about LLMs as opposed to claims about the particular models tested. Nevertheless, I believe this paper to be both high quality and important work and think that it should be accepted to the conference.

Nits:

l84, citation format error
L759: spacing error

### Strengths
Paper tests a very good question. The state of LLMs is very strange right now. They can clearly solve very tricky problems. At the same time, they often fail in very elementary ways as well. This paper is an exceptional analysis of this, especially testing across several different variants of GSM-Symbolic. In general, I think this paper is a fantastic contribution to the field and as a result vote accept.

### Weaknesses
Some weaknesses are referenced in the questions section. One additional question: would the authors be able to include statistical significance results in the Appendix or main results? I think this would significantly improve the paper.

Secondly, while the GSM-Noop experiments are very interesting, I think there is a large difference in the claim (also made by prior work) that LLMs are bad at handling irrelenvant context and them not performing reasoning.

Related Work: I think Srivastava+ 2024 should be cited and compared to, as it is a very similar method on the MATH dataset with similar-ish findings.

@misc{srivastava2024functionalbenchmarksrobustevaluation,
      title={Functional Benchmarks for Robust Evaluation of Reasoning Performance, and the Reasoning Gap}, 
      author={Saurabh Srivastava and Annarose M B and Anto P V au2 and Shashank Menon and Ajay Sukumar and Adwaith Samod T and Alan Philipose and Stevin Prince and Sooraj Thomas},
      year={2024},
      eprint={2402.19450},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2402.19450}, 
}

@misc{shi2023largelanguagemodelseasily,
      title={Large Language Models Can Be Easily Distracted by Irrelevant Context}, 
      author={Freda Shi and Xinyun Chen and Kanishka Misra and Nathan Scales and David Dohan and Ed Chi and Nathanael Schärli and Denny Zhou},
      year={2023},
      eprint={2302.00093},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2302.00093}, 
}

1. The abstract claims that “Specifically, the performance of all models declines when only the numerical values in the question are altered in the GSM-Symbolic benchmark.” However, if I’m reading this right, this is not what you report in Table 1 in A.2? For example, o1-mini and both Llama3 8B models seem to get a higher score on Symbolic compared to GSM8k (100).

2. One potential concern I have with the paper is that. Especially given (1), how do you differentiate between results that apply to LLMs more broadly compared  claims that apply broadly to specific LLMs? In particular, several models in your evaluations are well known to have interesting results regarding overfitting on GSM8k as per works in your current related works section.

### Questions
1. The abstract claims that “Specifically, the performance of all models declines when only the numerical values in the question are altered in the GSM-Symbolic benchmark.” However, if I’m reading this right, this is not what you report in Table 1 in A.2? For example, o1-mini and both Llama3 8B models seem to get a higher score on Symbolic compared to GSM8k (100).

2. One potential concern I have with the paper is that. Especially given (1), how do you differentiate between results that apply to LLMs more broadly compared  claims that apply broadly to specific LLMs? In particular, several models in your evaluations are well known to have interesting results regarding overfitting on GSM8k as per works in your current related works section.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models" presents a thorough investigation into the mathematical reasoning capabilities of large language models (LLMs) using a newly developed benchmark, GSM-Symbolic. This benchmark, derived from the GSM8K dataset, includes modifications to test the robustness of LLMs against changes in numerical values, proper names, and question complexity.

**Key Contributions:**

1. **Introduction of GSM-Symbolic**: The paper introduces GSM-Symbolic, a benchmark that generates diverse and controllable mathematical question variants based on symbolic templates. This allows for more precise evaluations of LLMs by modifying elements like numbers and text within the questions to assess their impact on model performance.

2. **Empirical Analysis of LLM Performance**: Through extensive testing with GSM-Symbolic, the authors demonstrate that LLMs exhibit significant performance variability and sensitivity to minor changes in question structure. Their experiments reveal that even small perturbations, such as altering numerical values or adding irrelevant clauses, can significantly degrade the performance of state-of-the-art models.

3. **Exploration of Reasoning Fragility in LLMs**: The study details how the introduction of irrelevant information (via the GSM-NoOp dataset) into mathematical problems significantly impacts model accuracy, highlighting a critical flaw in the current models' ability to discern relevant from irrelevant data.

Overall, the paper provides a deeper understanding of the limitations inherent in current LLMs regarding their mathematical reasoning capabilities and offers a comprehensive framework for future research to explore and mitigate these weaknesses.

### Strengths
**Strengths:**

1. **Comprehensive Experimental Design**: The authors explore various perturbations in mathematical questions such as changing names or numbers, adjusting the number of clauses, and introducing irrelevant information. These detailed experiments provide robust evidence of the fragility exhibited by prominent language models under slight modifications, thereby contributing significantly to our understanding of their limitations.

2. **Development of the GSM-Symbolic Dataset**: The introduction of the GSM-Symbolic dataset and its variants is a notable contribution. By coding 100 problems from the GSM8K dataset and creating corresponding modifications, the authors have developed a valuable resource that can facilitate future research into model robustness.

3. **Relevance and Depth of Analysis**: The topic is highly relevant to current discussions in the field, and the paper delivers extensive empirical data concerning critical questions about the robustness of current language models when subject to various perturbations.

### Weaknesses
 **Weaknesses:**

1. **Oversight of Computational Complexity**: The paper does not sufficiently address the computational challenges posed by the range of parameter values (5 to 100) used in their experiments. This range suggests that computing expressions like x + y + z, particularly with all parameters as two-digit numbers, could introduce significant computational errors unrelated to the models' reasoning capabilities. The potential impact of these computational difficulties on the results, particularly evident in Figure 4, suggests that the observed distribution shifts in Figure 2 might be attributed more to computational challenges than to data contamination. Specifically, the paper lacks a detailed analysis of how the complexity of multi-step arithmetic operations, such as (A + B) * C or A + B + C, impacts the accuracy of the models, compared to simpler operations like A + B. The study should differentiate between errors arising from flawed reasoning and those caused by simple arithmetic mistakes within the generated solutions, especially when dealing with three-digit or larger numbers.

2. **Ambiguity in Defining Reasoning**: The paper's definition of reasoning needs clarification. Asserting that models capable of only three-step inferences lack reasoning capabilities seems overly restrictive. Since the GSM8K focuses on the NLP aspect of reasoning rather than the length of reasoning required, it naturally tailors models to excel within these confines. Thus, introducing additional clauses or irrelevant details, as done in the experiments, effectively renders the questions out-of-distribution (OOD). This shift likely degrades performance due to the models not being trained to handle such modifications, which doesn't necessarily indicate a lack of reasoning ability but rather a limitation in the training paradigm. The paper should more clearly define reasoning, perhaps by breaking it down into specific capabilities such as dictionary lookup, dependency understanding, and Chain of Thought processing, and then analyze how the models perform on each of these aspects. The current definition is too broad and does not allow for a nuanced analysis of the models' limitations.

### Questions
**Q1: Computational Complexity Impact**
Could the authors provide a detailed analysis of how computational complexity affects the accuracy of the models tested? Specifically, it would be informative to understand the proportion of errors that can be attributed directly to the failure of numerical computations versus those caused by reasoning errors. This differentiation could help clarify the extent to which computational demands influence the performance of large language models on the GSM-Symbolic dataset.

**Q2: Impact of Fine-Tuning on Model Robustness**
Would the authors consider conducting experiments where some models are fine-tuned on the GSM-Symbolic dataset and its variants to assess whether this training approach enhances their robustness to the types of perturbations introduced in your study? This could provide valuable insights into whether the observed limitations are inherent to the model architectures or can be ameliorated through targeted training, potentially challenging the paper's conclusions about the fundamental nature of these limitations.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the reasoning capabilities of LLMs using the GSM8K benchmark and introduces a new benchmark called GSM-Symbolic. The authors highlight the variability in model performance, particularly noting that LLMs struggle more when numerical values are altered compared to when only proper names are changed. They also explore the impact of question difficulty on performance, revealing that as complexity increases, both average performance and variance decline. The findings emphasize the need for more reliable evaluation methodologies and further research into the reasoning abilities of LLMs, suggesting that while these models show potential, their understanding of mathematical concepts remains limited

### Strengths
+ GSM-Symbolic provides a strategy to enrich the math reasoning datasets. The symbolic template can be applied for other datasets.
+ The NoOp design is innovative, it shows undiscussed disadvantage of current LLM on reasoning tasks.
+ The experiment design is adequate and valid. This paper evaluates 25 models, the results provide a comprehensive overview of the current SOTA methods.

### Weaknesses
 - Figure 3 shows the chatgpt-o1 and GPT-4o has tiny accuracy drop. But even without GSM-Symbolic, running any LLM models for 50 times on the same dataset can cause this variance.
- For numerical variables, how did the authors choose their boundary? This is not explained in the paper
- To add clause in GSM-NoOp, we can see results drop a lot in Figure 8, but what is the standard to add this extra clause? Because adding clause can be subjective if authors already know some patterns will make the model fail.
- Part of the beginning paragraph of section 3 should belong to related work discussion.

### Questions
1. For numerical variables, how did the authors choose their boundary? Why x belongs to (5, 100) in Figure 1? I think this range may also influence the performance, especially when some extreme values are selected.
2. To add clause in GSM-NoOp, we can see results drop a lot in Figure 8, but what is the standard to add this extra clause? Because adding clause can be subjective if authors already know some patterns will make the model fail.

### Soundness
3

### Presentation
2

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
The paper "GSM-SYMBOLIC: Understanding the Limitations of Mathematical Reasoning in Large Language Models" explores the mathematical reasoning capabilities of Large Language Models (LLMs) through the introduction of a new benchmark, GSM-Symbolic. This benchmark aims to address the limitations of existing evaluations like GSM8K by generating diverse question variants and adjusting complexity levels. The study finds that LLMs exhibit performance variance when faced with different instantiations of the same question, particularly when numerical values are altered. It also highlights the fragility of LLMs' reasoning capabilities, as performance deteriorates with increased question complexity and the introduction of irrelevant information. The paper suggests that current LLMs rely on probabilistic pattern-matching rather than robust logical reasoning.

### Strengths
- The study provides empirical evidence of the performance variance and fragility of LLMs when faced with different question instantiations and increased complexity in grade school math questions.
- The introduction of the GSM-Symbolic benchmark allows for the creation of diverse instances of the GSM8K dataset, which helps avoid data contamination and enables a more comprehensive evaluation of LLMs' reasoning capabilities.

### Weaknesses
 - The findings largely reconfirm known limitations of LLMs, such as their reliance on probabilistic pattern-matching and sensitivity to small changes in question statements, which have been explored in depth in previous works, notably in "Are NLP Models really able to Solve Simple Math Word Problems?"
- The methods used to curate the dataset, such as altering numerical values and adding irrelevant information, are not novel and have been employed in other studies, such as "PAL: Program-aided Language Models," which introduces GSM8k-hard.
- The paper uses ambiguous terms like "true logical reasoning," "genuine mathematical reasoning," and "formal [reasoning] in the common sense term" without providing clear definitions of these terms.
- The paper’s findings on performance degradation with increasing question complexity have been similarly explored in other works as compounding errors in multi-step reasoning processes.
- The authors suggest that  performance of LLMs on GSM-Symbolic compared to their performance on GSM8k indicates significant limitations in LLMs’ ability to perform genuine mathematical reasoning. However,  performance of GPT4-o remains robust on GSM-Symbolic, as shown in figure 3, suggesting that the performance variance resulting from different numerical instantiation of the questions may be resolved with scaled training or model size and this limitations may not be inherent to all LLMs.

### Questions
1. Can you clearly define "true logical reasoning"? What conditions need to be satisfied for a language model to demonstrate true logical reasoning?
2. Why was the performance of o1 not investigated in certain parts of the study, such as in Figure 3?
3. Given that some models like GPT4-o show robustness across numerical changes, do the authors believe that scaled training and model size can alleviate the identified limitations? If so, how does this impact the generalizability of the findings?

### Soundness
2

### Presentation
2

### Contribution
2
