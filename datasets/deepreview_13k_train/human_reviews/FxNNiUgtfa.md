# Knowledge Capacity Scaling Laws for Language Models

- Decision: Accept
- Scores: 5, 6, 8, 10

## Abstract
Scaling laws describe the relationship between the size of language models and their capabilities. Unlike prior studies that evaluate a model's capability via loss or benchmarks, we estimate information-theoretically the number of knowledge \emph{bits} a model stores. We focus on factual knowledge represented as tuples, such as (USA, capital, Washington D.C.) from a Wikipedia page. Through multiple controlled datasets, we establish that language models can and only can store \emph{2 bits of knowledge per parameter, even when quantized to int8}, and such knowledge can be flexibly extracted for downstream applications. 

More broadly, we present 12 results on how (1) training duration, (2) model architecture, (3) quantization, (4) sparsity constraints such as MoE, and (5) data signal-to-noise ratio affect a model's knowledge storage capacity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates the relationship between language model size and its capacity to store factual knowledge, quantified in bits per parameter. The authors introduce a framework that measures a model’s knowledge based on tuple-based information (e.g., (Entity, Relation, Attribute)) and propose that language models, after sufficient training, achieve an approximate capacity of 2 bits per parameter. The study extends this analysis across various factors such as model architecture, quantization levels, sparsity, and training data quality. Using synthetic and controlled datasets, the authors examine how these elements influence the knowledge storage capacity of language models.

The technical claims are generally supported by experiments; however, there are concerns about the robustness of the findings. The reliance on synthetic data raises questions about the applicability of the results to real-world scenarios. Additionally, the paper does not thoroughly explore the impact of quantization during training.

The paper has several formatting issues that hinder its readability. Notably, it lacks a conclusion section. Some figures are not clear. The organization of the paper could be improved drastically.

### Strengths
•	Originality: Introducing a framework to measure language model capacity in bits per parameter is a novel approach that adds a quantitative dimension to model evaluation.

•	Methodology: The use of controlled synthetic datasets allows for the isolation of specific variables, providing clarity in the analysis of different factors affecting knowledge capacity.

### Weaknesses
•	Formatting Issues: The absence of a conclusion section and unclear figures detract from the overall quality of the paper and impede the reader’s understanding.

•	Generalization to Real-world Data: The heavy reliance on synthetic data limits the applicability of the findings to natural language processing tasks involving complex and diverse datasets. The use of tuple-based information extracted from synthetic data may not accurately reflect the nuances and complexities of real-world knowledge, where information is often implicit, context-dependent, and expressed in diverse linguistic forms. This raises concerns about the ecological validity of the 2-bit/parameter capacity claim.

•	Incomplete Exploration of Quantization: The paper does not investigate quantization during training, which could provide insights into mitigating the observed decrease in capacity with int4 quantization. Specifically, the study does not explore whether quantization-aware training or other techniques could preserve knowledge capacity during the quantization process. This limits the practical implications of the study for resource-constrained environments where quantization is crucial.

•	Limited Architectural Diversity: The study does not explore a wide range of model architectures, such as encoder-only or decoder-only models, which could affect the generalizability of the proposed scaling law. The focus on a single architecture limits the scope of the conclusions, as different architectures may exhibit varying capacities for knowledge storage and different scaling behaviors with respect to model size.

### Questions
1.	How would the proposed 2-bit/parameter scaling law hold up when applied to language models trained on real-world, diverse datasets?

2.	Could incorporating quantization into the training process mitigate the reduction in capacity observed with int4 quantization?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors investigate how the size of language models influences their ability to store factual knowledge. Unlike previous studies that assess model capabilities through loss metrics or benchmarks, this research estimates the amount of knowledge from an information theory perspective. The authors find that an LLM can store about 2 bits of factual knowledge per parameter, meaning a 7B parameter model can hold approximately 14B bits of knowledge, covering Wikipedia-level information.
Other influencing factors of the amount of stored information include: extended training, specific architectures (e.g., GPT-2 with rotary embeddings), and higher data quality. Precision reduction (e.g., int8) minimally impacts storage, while domain annotations (like labeling Wikipedia data) significantly boost capacity.

### Strengths
1. The authors propose a novel method to measure the knowledge stored in an LLM by a bit complexity lower bound, and show that the amount of information stored in a single parameter is approximately 2 bits.

2. The authors investigate various influencing factors to the knowledge storage capacity of LLMs, which provide many practical insights to LLM training.

### Weaknesses
1. What do the long plateaus in the stored information mean? Does the maximum information reached by the plateaus equal to the bit complexity upper bound? The main scaling law only describes the linear increasing part, not the plateaus part. It remains unclear what the specific value of the maximum information is, and when this maximum is reached, especially considering the N-specific nature of the plateaus. A more detailed description of the maximum information value, perhaps as described in Proposition 2.3, and the conditions under which this maximum is achieved, would be beneficial.

2. The scaling law seems to be incomplete. i.e. the paper describes the influencing factors to the stored knowledge separately. Is there an empirical law that can describe and summarize all the results?

3. What does it mean if we say that the LLM stores N bits of knowledge? Does it mean this amount of knowledge is ready for extraction or just memorized in a fixed form? There are some memorization v.s. extraction accuracy plots in the appendix, which seem also show a first linearly increase and then plateau trend, but these results are not well associated with the bit information results. e.g. Would the bits of knowledge stored linearly be associated with the knowledge memorization/extraction accuracy? If the meaning of this information theoretical definition of storage knowledge is not well understood, it is hard to interpret the insights obtained from it.

4. The derivation of the bit complexity lower bound feels a bit ad hoc. It seems that the authors just tried to build a lower bound in a similar form to the upper bound involving the training losses. Some steps in the derivation do not feel natural to me, especially lemma 1.6. What is the meaning of the RHS of equation I.1? How tight would this lower bound be? It would be helpful to provide a more intuitive explanation of the lower bound, perhaps with a simple example, to clarify its meaning and tightness.

5. The training data generation process is basically uniformly random. There are also similar uniformly random assumptions used in the proof of the bit information lower bound. I wonder if the derived lower bound can be applied to real-world data, which is not uniform, but usually naturally exhibits a long-tailed distribution. I understand that certain assumptions are needed for synthetic experiments, but it is also important to understand how much the obtained conclusions can be applied to real-world applications. The current analysis, while insightful under uniform distribution, does not address the knowledge scaling in real-world pretraining scenarios where data follows a power-law distribution. This limitation should be acknowledged.

6. The writing can be improved.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper examines scaling laws concerning model size versus its knowledge storage capacity. The paper addresses the following research questions: 
- Does the knowledge scale linearly with  model size, and what is the exact constant of this scaling?
- How does training affect model capacity? 
- How does  model architecture relate to model capacity?
- How do quantization and model sparsity affect model capacity?
- How does irrelevant/noisy data affect model capacity?

Unlike prior studies that evaluate a model’s capability via loss
or benchmarks, this paper  estimates  the number of knowledge bits a model store, focusing  on factual knowledge represented as tuples, such
as (USA, capital, Washington D.C.) from a Wikipedia page. Experimental results across model architectures establish that language models can only store 2
bits of knowledge per parameter. Detailed analyses further illustrated that a sufficiently trained 7B language model can store 14B bits of knowledge. Achieving 2bits per parameter capacity requires each knowledge piece to be revisited 1000 times. Quantizing to int8 does not compromise model capacity,  however, quantizing to int4 reduces capacity to 0.7bit/param.
Mixture-of-experts (MoE)  only reduce 1.3x in capacity,  despite using just 8.8% of the total parameters during inference.
Finally, noisy data significantly reduces model capacity but an  effective mitigation is to prepend a special token to all useful knowledge.
The model autonomously identifies high-quality data without prior knowledge of
valuable domains.

### Strengths
- Scaling laws are of interest to the community as they allow us to analyze and understand the capacity of large language models. They also enable the design of new models and pertaining experiments. The authors claim they are the first to propose a scaling law for the knowledge capacity of LLMs. 

- The paper contains a very thorough and exhaustive list of experiments, answering several questions. 

- There are practical recommendations about LLM model builders, such as domain tagging for pertaining data. 

- the paper provides an explanation as to why Quantized models perform on part to their non-quantized variants in terms of knowledge storage, and similarly why  mixture of experts models perform decently despite being sparse. 

- Finally, it reveals specific architectural choices in models like Llama and Mistral which might lead to slightly inferior performance (e.g., weight tying, MLP layers). 

- The experimental framework is reproducible, and although the authors focus on binary knowledge base tuples, it could be extended to of the knowledge-based facts or event language structures.

### Weaknesses
 - the paper is very dense, the appendix is very many pages long.  As a result, it is not easy to absorb all important details. 

- the graphs are in very small scale and are not explained appropriately.

### Questions
- Please explain why you selected GPT2, Llama, and Mistral model families for your experiments. Although I understand that these represent the most popular model families, it would have been interesting to see how other, less similar architectures fare like S4. 

- I would have been good to mention something about the computational requirements for your experiments. 

- Aside from knowledge-base tuples, are there any other areas you think your framework might be applied to? 

- I would have liked to see explicit suggestions to researchers pertaining or using LLMs. It seems that you are saying that the
quality of the data and the times of exposure matter a lot more than differences in architecture.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper studies knowledge capacity scaling laws for language models. The authors design a set of novel and solid evaluation methods to assess the knowledge capacity ratio of language models. The evaluation covers different model architectures from dense to sparse LLms as well as different settings such as quantization and data noise, making it a complete and solid paper.

### Strengths
1. The proposed knowledge capacity evaluation is novel and useful in practical applications
2. The experiments are solid and comprehensive

### Weaknesses
One limitation could be the readability of this paper. Some figures are not visible such as result 8. The fonts in some figures such as Figure 1 and 3 are also too small to read. I would suggest the authors remove some sections such as result 8 to appendix, therefore more space could be left for more detailed explanation on other sections.

### Questions
Current I do not have questions on this paper.

### Soundness
4

### Presentation
4

### Contribution
4
