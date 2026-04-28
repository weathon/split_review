# Domain Shift Tuning over Knowledge Gap

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
This paper introduces Domain Shift Tuning (DST), a novel framework designed to guide pre-trained language models (PLMs), including Large Language Models (LLMs), in overcoming domain discrepancies (i.e., source-target).
PLMs, pre-trained on extensive and diverse corpora, the source domain, often encounter domain gaps after fine-tuning over the target domain.
Unlike conventional adapters or Parameter-Efficient Fine-Tuning (PEFT) methods, 
DST conceptualizes domain gaps as differences in knowledge encapsulated within multiple subnetworks of PLMs. 
To bridge this gap, 
our challenge is to find a subnetwork set that corresponds to these pieces of knowledge and their weight.
This direction leads DST to employ a lightweight subnetwork, the Knowledge Steering Layer (KSL), and a training objective, Knowledge Distribution Modeling (KDM). 
These components enable DST to fine-tune PLMs by aligning the knowledge weights of the source domain with those of the target domain. 
Experimental results on diverse datasets demonstrate that DST effectively mitigates the domain gap, allowing PLMs to generate text that closely aligns with even a small target corpus, thereby significantly enhancing domain adaptation for PLMs at lower computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents Domain Shift Tuning (DST), a framework for enhancing domain adaptation in PLMs. DST tackles the challenge of domain shift, where PLMs trained on a large, generalized corpus underperform on a specific target domain. DST introduces two key components:  Knowledge Steering Layer (KSL) and Knowledge Distribution Modeling (KDM). Through these, DST fine-tunes PLMs to align domain-specific weights with the target domain, thus overcoming the domain gap and reducing computational costs associated with large-scale fine-tuning.

### Strengths
- By framing domain adaptation as knowledge distribution alignment, DST minimizes computational overhead and sidesteps catastrophic forgetting. This is particularly beneficial for limited-resource settings, allowing PLMs to adapt to new domains effectively with minimal data.
- The experimental results demonstrate that the proposed method outperforms several baslines.

### Weaknesses
 - The motivation in introduction is presented in a somewhat cursory manner, lacking clear logical connections between sentences. In line 32, the claim that “size discrepancy can lead to catastrophic forgetting and poor generalization” is not convincingly supported by the cited references. Additionally, the transition to “Given the swift diversification of PLM applications…” feels abrupt, missing a logical connection that ties it smoothly to the preceding discussion.
- The foundational hypothesis that "PLMs encapsulate multiple pieces of knowledge as subnetworks" (Lines 38-40) lacks supporting references or verification experiments. Furthermore, the approach of representing domain gaps by differences in model parameters between source and target domains is not sufficiently justified. Although empirical results support DST’s effectiveness, the Introduction lacks a clear causal rationale for these core design choices. Specifically, the assumption that differences in model parameters directly correspond to domain gaps needs more rigorous justification. It is unclear how the proposed method ensures that these parameter differences capture meaningful domain-specific knowledge rather than noise or irrelevant variations.
- In Table 4, the absence of performance metrics for base methods such as PEFT on LLMs limits the comprehensiveness of the evaluation. The evaluation would benefit from including a more diverse set of baselines, particularly those that are directly comparable to the proposed method in terms of computational cost and performance. For example, a comparison with other parameter-efficient fine-tuning methods on LLMs would provide a clearer picture of DST’s relative advantages.
- Writing Issues:
  - Figures and tables, such as Figure 1’s left side, appear cluttered, detracting from clarity.
  - The citation style disrupts readability; author names would be clearer within parentheses.
  - Minor issues, such as the incorrect symbol following "else" in equation (6).

### Questions
refer to the comments

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a domain adaptation technique called domain shift tuning which consists of a lightweight knowledge steering layer (KSL) and a training method called knowledge distribution modeling (KDM). The KSL is a layer affixed after the last transformer layer in a pre-trained LM, and KDM is applied as an auxiliary loss to attempt to align topic/knowledge latent representations with textual similarity. The KSL predicts a topic and selects a weight accordingly to project the final hidden before projecting again into the vocabulary. The model is kept frozen while the KSL is fine-tuned using a modified CE loss accounting for knowledge vectors and the KDM. The method is tested on encoder models for topic clustering and decoder-LMs for text generation.

### Strengths
1. The authors test their method against an impressive number of baselines, from both domain adaptation and other PEFTs
2. The use of rKSL is important and helpful to understand how much more knowledge than the residual is being used, and it is interesting to see values much bigger than 0. 
3. The method is seemingly model-agnostic which strengthens its applicability to things beyond just language and just Transformers.
4. The subnetwork motivation and integration with the knowledge steering layer is an interesting and intuitive motivation.
5. The authors test on both clustering and text generation. It is great to see a method that applies to both of these tasks, especially as there is a lot of need for good embedding models in addition to LMs.

### Weaknesses
1. Although the KSL is smaller compared to the size of the model, it must have some sort of slow-down associated with it since it appears as an additional layer with an additional step across K subcomponents. What is the speed reduction in using this method? The parameter count may be low, but the additional computation required by the KSL, especially with its K subcomponents, could introduce a non-trivial overhead during both training and inference. A detailed analysis of the inference time and training time compared to baselines is needed.
2. This paper makes multiple references to VAEs as inspiration for the latent vector $z$, but this connection is never formally introduced, nor are any details about what is being referred to in VAEs. Some formal background and direct linking would strengthen the work. The paper should explicitly define the relationship between the latent space in VAEs and the discrete knowledge components in DST, including how the continuous latent space of VAEs inspires the discrete representation in DST. A discussion of how the training objectives differ and how this affects the final representation would also be beneficial.
3. The notation and writing is not always the most clear, where some key variables are not clearly defined, and some motivation is not clearly written. For example, latent “knowledge” vector $z$ is not clearly defined nor is its length $K$, and the notion of knowledge is redefined several times in the text, including as a “latent relative concept” or “co-occurence pattern of tokens with similar semantics”. The paper needs to clearly define the length K of the latent vector z, and clarify whether this is a fixed value or varies based on the input sequence. The definition of 'knowledge' needs to be consistent throughout the paper, with a clear explanation of how it is represented and used in the model. The multiple definitions of knowledge make it hard to understand the method.
4. The published parameter settings for each baseline may not be the fair comparison here, what may be more fair is scaling the baselines according to the parameter budget or throughput associated with the DST method. The paper should justify why the baselines are not scaled to match the parameter budget or throughput of the DST method. A comparison of performance with baselines that have a similar computational cost would be more informative.
5. The LLM experiments are not compared to few-shot/zero-shot prompting despite these models being able to perform in-context learning. The LLM experiments (Table 4) need some sort of baseline to compare to, like in Table 3. The lack of comparison to few-shot or zero-shot prompting for LLMs is a significant omission. Given the capabilities of these models, it is crucial to demonstrate that DST provides a performance benefit over these simpler, parameter-free methods.
6. $L_{KDL}$ is not ablated to show its usefulness in this work. The paper needs to include an ablation study to demonstrate the impact of the $L_{KDL}$ loss term on the overall performance of the model. This should include a comparison of results with and without this loss term.
7. Some code or pseudocode would strengthen knowing how the KSL/KDM is actually implemented. For example, it is unclear how the selection process works for the Waz matrices, and the minimum operation in KDM is also unclear as to how this is differentiated. The paper should provide pseudocode or a detailed description of the KSL and KDM implementation, including the selection process for the Waz matrices and the differentiation of the minimum operation in KDM. The lack of implementation details makes it difficult to reproduce the results.

### Questions
1. Is $z$ length $K$ for each index in $|x|$? It is defined as length $K$, but then also indexed over the t indices along with the sequence length. Is it different at each sequence index? And if yes, how can it be a scalar as in equation 4 without some sort of argmax/softmax operation, and why should it be different for the same utterance? And if it is argmaxed, how can it be useful in KL divergence unless it remains continuous?
2. What is meant by "KSL considers knowledge as a quantized sample of the underlying token distribution"? Like in a vector quantized/code book sense?
3. Why is $SIM_z$ KL-divergence and $SIM_{TID}$ cosine? Are the $z$ vectors softmaxed and probability distributions? How do these different functions affect the minimization term in KDM?
4. What is the number of fine-tuning steps? It is missing, which is important for defining linear decay, and understanding the cost of the method. 
5. Why minimize the minimum $SIM_z$- $SIM_{TID}$ rather than the maximum for minimax?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents Domain Shift Tuning (DST), an innovative framework designed to enhance the adaptability of pre-trained language models (PLMs), across different domains. DST addresses the challenge of domain discrepancies by conceptualizing these gaps as variations in knowledge encapsulated within multiple subnetworks of PLMs. To bridge these gaps, the framework introduces two key components: Knowledge Steering Layer  and Knowledge Distribution Modeling.

### Strengths
1. The idea of this work is interesting. DST introduces a new perspective by treating domain gaps as differences in knowledge subnetworks.

2. KSL provides a lightweight mechanism for representing domain-specific knowledge without changes to the underlying PLM architecture.

3. DST achieves domain adaptation improvements with lower computational overhead

### Weaknesses
1. Citation Formatting: When adhering to the ICLR template guidelines, replace all instances of  `\cite` with `\citep` to ensure proper citation formatting.

2. Motivation: The paper posits that the discrepancy in `dataset sizes` can lead to catastrophic forgetting and poor generalization, but authors have not provided sufficient empirical evidence in the era of LLMs. Specifically, the claim that smaller datasets cause catastrophic forgetting needs more rigorous justification, especially given the known robustness of large language models to some degree of domain shift. The paper should include experiments or cite studies that demonstrate this issue with models of the size used in the experiments.

2. Outdated References and Baselines:  Most of the previous work discussed and baselines compared are already 2 years ago. This raises concerns about the relevance of the comparisons, as the field has advanced rapidly. The paper should include more recent baselines and discuss how DST compares to state-of-the-art methods.

3. Marginal Improvements on modern models Llama and BLOOM:  In Table 4, the application of DST on the Llama and BLOOM models results in only negligible improvements, calling into question the effectiveness of the proposed method for these specific models. The gains are not only marginal but also inconsistent across different tasks, suggesting that the method may not be robust or generalizable for modern LLMs.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
