# Large Scale Knowledge Washing

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large language models show impressive abilities in memorizing world knowledge, which leads to concerns regarding memorization of private information, toxic or sensitive knowledge, and copyrighted content. 
 We introduce the problem of \textbf{Large Scale Knowledge Washing}, focusing on unlearning an extensive amount of factual knowledge.
 Previous unlearning methods usually define the reverse loss and update the model via backpropagation, which may affect the model's fluency and reasoning ability or even destroy the model due to extensive training with the reverse loss.
 Existing works introduce additional data from downstream tasks to prevent the model from losing capabilities, which requires downstream task awareness. Controlling the tradeoff of unlearning and maintaining existing capabilities is also challenging.
 To this end, we propose \ours (\textbf{La}rge Scale \textbf{W}ashing) to update the MLP layers in decoder-only large language models to perform knowledge washing, as inspired by model editing methods and based on the hypothesis that knowledge and reasoning are disentanglable. 
 We derive a new objective with the knowledge to be unlearned to update the weights of certain MLP layers. 
 Experimental results demonstrate the effectiveness of \ours in forgetting target knowledge while maintaining reasoning ability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents LAW (Large Scale Washing), a novel method for removing a large set of factual knowledge from large language models (LLMs) while preserving reasoning abilities. The authors hypothesize that knowledge and reasoning abilities in LLMs are disentangled. LAW is inspired by model editing, which focuses on adding factual relations, while LAW deletes factual relations. Experiments on datasets (zaRE and CounterFactual), also including a new large-scale dataset called Wiki-Latest, demonstrate that LAW achieves better knowledge removal than other methods while maintaining the model's reasoning abilities.

### Strengths
Novelty: The paper proposes a novel objective function specifically designed to remove knowledge represented in triplet format, achieving an approach distinct from existing methods.

Creation of a large-scale dataset: The development of Wiki-Latest, a new large-scale dataset derived from Wikipedia triplets, is a valuable contribution to the field.

Comprehensive evaluation: The paper presents a detailed comparative analysis with multiple existing methods.

### Weaknesses
Knowledge vs. Reasoning: While the paper aims to disentangle knowledge and reasoning, it doesn't explicitly define what constitutes "reasoning," while the knowledge is defined as triples. Are they referring to specific modules or functionalities within the model? Or are they more abstract concepts related to the model's behavior? The lack of a clear definition makes it difficult to evaluate the claim of disentanglement. For instance, if reasoning is defined as the ability to perform multi-hop inference, the current evaluation using tasks like LAMBADA and HellaSwag, which primarily assess next-token prediction, might not be sufficient to validate the claim. A more rigorous definition is needed to assess the true impact of the proposed method on reasoning capabilities.

Insufficient discussion on disentanglement: While the paper claims in section 5.2 that "In this paper, we show the possibility of the disentanglement between knowledge and reasoning by washing a large amount of knowledge from the model while only minimally affecting the reasoning abilities," this assertion doesn't seem to be sufficiently discussed in the later sections. It lacks a theoretical foundation to support the claim that knowledge and reasoning are truly disentangled in the model. The paper primarily relies on empirical evidence from the experiments, and it could be strengthened by exploring the underlying mechanisms that allow for this separation. For example, the paper could analyze the changes in attention patterns or the activation of specific neurons after applying the knowledge washing method to provide more insights into the disentanglement process. Without such analysis, the claim remains largely empirical and lacks a deeper understanding of the model's internal workings.

The limited scope of knowledge washing: They lack the ability to address the washing of knowledge expressed in more general or abstract forms, such as knowledge embedded within the text that doesn't have a clear subject-relation-object structure. It might be beneficial to consider and compare an abstract editing method that modifies behavior at the sentence level, such as DINM, proposed in 'Detoxifying Large Language Models via Knowledge Editing' (ACL 2024). The current method's focus on triplet-based knowledge limits its applicability to real-world scenarios where knowledge is often expressed in more complex and nuanced ways. Expanding the scope of knowledge washing to handle unstructured text would significantly enhance the practical value of the proposed approach.

### Questions
The choice of reasoning benchmark: It is not clear why the three benchmark datasets (LAMBADA, HellaSwag, ARC_easy) were chosen from many other reasoning benchmark datasets. The setup for LAMBADA and HellaSwag is word/sentence prediction, which does not seem to be the "reasoning" ability that this paper tries to disentangle.  Can something more like logical and/or numerical reasoning, such as GSM8K, be added?

Validity of  `<|endoftext|>` output: Could you provide a more detailed explanation of the rationale behind configuring the model to output `<|endoftext|>` in place of the original object when deleting knowledge? Are there any existing research studies that employ a similar task setup? If this configuration is specific to this study, please clearly state so. Additionally, could you explain the fundamental difference between outputting `<|endoftext|>` (deletion) and outputting another appropriate object (editing)?

Model architecture clarification: Although equation (1) in Section 3 illustrates a parallel model structure with Attention and MLP (like GPT-J), the experiments also include GPT2-XL, which has a serial structure. To prevent misunderstanding, it might be beneficial to explicitly state that the proposed method is not dependent on any specific model architecture.

### Soundness
3

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
Large language models (LLMs) can memorize a vast amount of knowledge, which leads to concerns about the memorization of sensitive knowledge. This paper focuses on the problem of large-scale knowledge washing, that is, how to forget knowledge on a large scale while minimizing the impact on the model's reasonining ability. The authors propose a method named LAW, which is based on the model editing technology to update the MLP layers of the decoder model. It determines the keys and values related to the forgotten knowledge in a specific way, redefines the objective function, and considers practical factors. Experiments show that LAW performs excellently in both small-scale (zsRE and CounterFactual datasets) and large-scale (Wiki-Latest dataset) knowledge washing in terms of the cleanliness of knowledge forgetting and the maintenance of reasoning ability, outperforming many baseline methods.

### Strengths
1. The paper is well-written with clear logic.
2. The experiments consider both small- and large-scale knowledge washing settings and include baselines for both model editing and machine unlearning methods.
3. The ablation studies are thorough.

### Weaknesses
1. Model editing methods often face a problem of generalization where, after editing for a specific query, the model's response reverts to the pre-edit state when the query is rephrased. This raises the question of whether LAW truly makes the model forget sensitive knowledge or just forgets the specific case. It is necessary to use jailbreak prompts to verify true washing;
2. The abstract mentions that machine unlearning affects the fluency and reasoning ability of the model's generation. While reasoning ability is evaluated in subsequent experiments, the fluency of the generated text is not assessed.

### Questions
1. FT-UL is used, but there is no consideration of using FT-UL with utility loss as a baseline.
2. It would be better to conduct more experiments with the LLaMA or Qwen series.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- This study introduce the problem of Large Scale Knowledge Washing, focusing on unlearning an extensive amount of factual knowledge. 
- This study proposes a method of unlearning LaW (Large Scale Washing), which update the MLP layers in decoder-only large language models to perform knowledge washing, as inspired by model editing methods. 
- Experimental results demonstrate the effectiveness of LaW in forgetting target knowledge while maximally maintaining reasoning ability.

### Strengths
- The proposed unlearning method borrows the idea from the existing knowledge editing method to some degree, but the proposed method itself is original and interesting from the viewpoint of problem setting and derivation (4.Problem setup and 5. Methodology). Especially, problem reformulation by equation (8) is inspiring.
- The study conducts wide range of experiments with several benchmarks and baselines, demonstrating the effectiveness of the proposed method.

### Weaknesses
 - Some existing unlearning methods are not considered as baselines. e.g. https://arxiv.org/abs/2309.11852
- Some important and basic information is not sufficiently explained e.g. how to calculate K and K_w in practical setting in the experiments. It is also better to explain how to derive K and V in equation (2) with more details.
- The authors conducted experiments with GPT2 and GPT-J, without clarifying the effectiveness with the current state-of-the-art open models like Llama3 or Gemma.

### Questions
- Applying the proposed method will lose all information about the target Subject (since K depends on the Subject in triplets), is my understanding correct? In other words, Is it possible to erase part of the information related to the target subject? e.g. retain (S, R1, O1) but erase (S, R2, O2).
- Updating the models to output wrong answers could be interpreted as hallucination, not unlearning. From this viewpoint, just outputting nothing (EOS) or "I don't know" seems to be more appropriate approach for unlearning, but what do the authors think about this?

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
The paper introduces a novel approach to unlearning factual knowledge from large language models (LLMs) while preserving reasoning capabilities. The primary contribution is the development of the *LaW* (Large Scale Washing) method, which updates the MLP layers of decoder-only models to remove specific knowledge, inspired by model editing techniques.

Key contributions include:
1. **Novel Approach (LaW)**: LaW selectively updates MLP layers responsible for factual knowledge using a newly formulated objective. Unlike previous methods, which may degrade model performance, LaW preserves reasoning by carefully optimizing the updates.
2. **Experimental Validation**: The paper demonstrates LaW’s effectiveness on small and large datasets, showing superior results in knowledge forgetting and maintaining reasoning abilities compared to existing methods.

This work represents a good advance in unlearning in LLMs, addressing a critical need for managing sensitive or private data.

### Strengths
- **Originality**: From a theoretical perspective, LaW reconstructs MEMIT and applies it to model unlearning.
- **Quality**: The paper demonstrates the effectiveness of LaW in knowledge unlearning, ranging from small-scale to large-scale, on the zsRE, CounterFact, and the newly constructed Wiki-Latest datasets.
- **Clarity**: The paper is well-structured and clearly articulated. The source code and data have been open-sourced, ensuring high reproducibility.
- **Significance**: Model unlearning is an important problem. The introduction of LaW provides new insights for addressing model unlearning—leveraging model editing insights to update MLP layers for effective model unlearning.

### Weaknesses
 - **Lack of results on model unlearning benchmarks**: Providing results of LaW on model unlearning benchmarks (e.g., TOFU) would make its effectiveness more convincing. 
- **Lack of in-depth analysis of LaW's ability to retain unrelated knowledge**: The paper mentions that LaW performs comparably to MEMIT in retaining unrelated knowledge, yet MEMIT's performance in this aspect is average. The paper should delve deeper into this, offering more detailed results and analysis of LAW's ability to retain unrelated knowledge.
- **Lack of examples**: I'm curious about what the actual outputs look like after using LAW and other unlearning methods.

### Questions
- Does LAW's reasoning ability decline the more it forgets? If so, are there any measures to address this issue? How significantly does unlearning at the scale of 100,000 affect the model's reasoning ability?

### Soundness
3

### Presentation
3

### Contribution
3
