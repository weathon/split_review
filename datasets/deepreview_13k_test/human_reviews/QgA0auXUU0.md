# A Consistent Pattern for Identifying Decisive Code Snippets for LLM-Based Code Inference

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
Which parts of pre-target input are most influential for next-token prediction in the context of programming languages? In this paper, we present evidence that code snippets at specific locations in pre-target inputs play a decisive role in large language model (LLM) inference, and these snippets exhibit a consistent pattern. Firstly, we introduce a novel causal tracing method to identify tokens,  so-called high-information tokens, that significantly contribute to next-token prediction. Building on this, we propose a multi-phase causal tracing process to analyze the importance distribution of high-information tokens, revealing a consistent pattern, named the  Important Position Rule (IPR). To further validate this hypothesis, we assess the role of IPR across various LLMs, languages, and tasks. Our extensive evaluations for code translation, code correction and code completion tasks (Java, Python, C++) on models CodeLlama-7b/13b/34b-Instruct and GPT-3.5/4-turbo, confirm this hypothesis. Furthermore, we observe that IPR exhibits structural and semantic properties similar to the $\langle \text{subject},  \text{relation}, \text{object} \rangle$ paradigm in natural language. Leveraging this insight, we successfully combine IPR with the knowledge editing method ROME in order to repair translation errors, achieving a correction rate of  62.73% to 75.31%. To our knowledge, this is the first application of knowledge editing  in the context of programming languages.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a causal tracing method to identify high information content tokens. This method involves corrupting one prefix token and comparing the similarity between the high-dimensional predicted next token and the original next token. A lower similarity indicates higher information content. Building on the causal tracing method, the authors conduct experiments from small to large sample sizes and discover a consistent pattern in the distribution of high information content tokens, which they name the Important Position Rule (IPR). The authors combine IPR with the knowledge editing method ROME in code translation tasks to demonstrate one application of IPR, resulting in an increase in the correction rate from 62.73% to 75.31%.

### Strengths
- The identification of high information content tokens of code is insightful.
- Clear progression from theoretical framework to practical applications.
- The paper is well-written and easy to follow.
- The proposed method is effective in knowledge editing tasks.

### Weaknesses
There are several major weaknesses in this paper:

1. This paper lacks justification for the datasets used. Where are the 3650 samples in Section 3.2 from?  What are the sources, dataset sizes and lengths of the correct and incorrect codes in Section 4.1? And how did the authors collect the 25227 Java functions with 2975 incorrect Python translations in Section 5.2? Where are the test cases mentioned in Line 493 from? The authors should provide more details about the datasets used in the experiments.
2. Many key decisions in this paper are unclear. For example, how did you determine the "4-token radius" for sec and "2-token radius" for the target in Line 343? Are there any supporting quantitative analysis, or are they just visual inspection from Figure 4? How will they affect the results in Section 4 and 5? Furthermore, how did you decide on keeping "12 high-information tokens" in the experiments in Section 4.2? What is the average length of the original input? How will the results change if you keep more or fewer high-information tokens? The authors should provide more details about the key parameter choices in the paper.
3. The idea of identifying high-information tokens has also been explored in prompt compression methods like LLMLingua [1] and Selective Context [2]. Do you think it is necessary to discuss these works and compare them in the paper?
4. There is a lack of baselines in the experiments. Other than the prompt compression methods mentioned above, some simple baselines like random selection of tokens as "decisive" should at least be included in the experiments to verify the effectiveness of the proposed method.
5. The methodology for calculating the success rate in Section 4.2 is ambiguous. For translation and completion tasks that typically involve generating a sequence of tokens, how exactly is the success rate computed? Is it based on token-level accuracy or sequence-level exact match? If the evaluation is done on a token-by-token basis, how are the test samples constructed? Does each test case involve predicting only a single token? It would be helpful to clarify the details in the paper.
6. Upon seeing the title of this paper, I've been curious to know what kind of snippets would be decisive. However, this question remains unclear after reading the paper. What does the "decisive code snippets" identified in this paper look like in practice? Are they some specific code patterns or structures, or is it just position-based? It would be helpful to provide some examples in the paper.

And some minor issues:

1. There are some concerns about scalability to real-world code. From Figure 2, all examples appear to have source lengths of around 30 tokens or fewer. However, production code is typically much longer. Can the proposed method be generalized to identify high information content tokens in longer code snippets?
2. In Tables 5-7 of the appendix, why do different tasks have varying sample sizes when using the same task? For example, in Table 5, the C++ to Python task has 529 samples for CL-7b-Instruct and 604 for CL-13b-Instruct.
3. In Line 481-482, The KL divergence term $D_{KL}(P_G[x|p'] || P_G[x|p'])$ computes divergence between identical distributions, I guess the correct version should be $D_{KL}(P_G[x|p'] || P_G[x|p])$. And the optimization term "argmin_z" uses an undefined variable z, will "argmin_v" be more appropriate?
4. Including examples in the appendix that show the next token predictions before and after using IPR would be helpful to better understand the method. Do the improvements in predictions primarily relate to syntax or semantics?
5. What is the exact version of GPT-4-turbo used in your experiments? There are multiple versions of GPT-4-turbo available from OpenAI according to [3], so specifying the version would help ensure reproducibility.

[1] LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models, EMNLP 2023

[2] Compressing Context to Enhance Inference Efficiency of Large Language Models, ACL 2023

[3] https://platform.openai.com/docs/models/o1#gpt-4-turbo-and-gpt-4

### Questions
Please address the concerns in the "Weaknesses" section.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates what tokens within input sequences critically influence the decoding of target tokens in code language models. Unlike prior methods that focus on perturbing tokens solely within the source sequence, this paper introduces the idea of incorporating the prefix of the target sequence for correlation analysis. The results demonstrate that next-token prediction relies heavily on core tokens (tokens that exhibit analogous functionality and purpose) in the provided sequence. The authors further validate this approach across three downstream tasks—code correlation, code completion, and code translation. Additionally, the method is applied to knowledge editing, yielding promising results in repairing translation errors.

### Strengths
• The focus on interpreting code language models is valuable and timely. This paper contributes a new idea by incorporating target sequence prefixes in correlation analysis.

• The experiments cover multiple coding tasks, including code translation, code completion, and code correlation, adding depth to the evaluation.

### Weaknesses
•	The novelty is somewhat limited, as the proposed approach bears similarity to prior methods (e.g., arxiv:1908.04626, arXiv:1612.08220,arXiv: 2004.14786) except including the decoding prefix for analysis.

•	The study only examines correlations between individual tokens, neglecting potential dependencies across phrases or combinations of tokens at multiple positions, which is common in structured source code (e.g., bracket pairs).

•	The evaluation lacks comparisons to baselines. For instance, Tables 1 and 2 present results only across variants of LLMs. Comparisons to traditional NLP methods, particularly those excluding the target prefix, would strengthen the evaluation. The following baseline methods may be considered for compassion: arxiv:1908.04626, arXiv:1612.08220,arXiv: 2004.14786

•	Ablation studies are needed to assess factors such as the number of core tokens, and the positional impact of target tokens within the sequence. For example, the authors can vary the number of core tokens from 1 to 5 and evaluate the effect on performance. 

•	While source code inherently has structured elements, this paper overlooks such structural information. Without it, the potential <subject, relation, object> analogies found in natural language are not fully analogous to source code.

•	The practical utility of the code correlation task is questionable.

•	Some essential details are missing. For example, in Line 373, the authors mentioned that they constructed a specialized IPR-based dataset. However, there are no details about how the authors constructed the evaluation dataset, such as the source of the code samples, the criteria for selection, and any preprocessing steps. In particular, I wonder why not use existing benchmarks for these tasks such as HumanEval and CodeSearchNet.

### Questions
1.	Why were only the 4th, 8th, 12th, and 17th positions in the target sequence chosen for information detection? Why specifically select seven pre-target inputs?

2.	The IPR method assumes the presence of core tokens influencing the target token. What happens if no core tokens exist?

3.	How did you construct the evaluation dataset? Why not use existing benchmarks?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates which parts of pre-target inputs significantly influence next-token prediction in programming languages within LLMs, including CodeLlama and GPT. The authors employ the causal tracing method and propose a multi-phase causal tracing process to analyze the importance distribution pattern of high-information tokens, demonstrating that specific code snippets at certain locations play a critical role in inference and exhibit a consistent pattern, named the Important Position Rule (IPR). Finally, experiments are conducted across various code downstream tasks to validate their findings.

### Strengths
1. This paper explores a very interesting question: which parts of pre-target inputs are most influential for next-token prediction in the context of programming languages? 
2. Based on the causal tracing method, the authors propose the IPR method to evaluate the influence between model tokens. 
3. The models used in the experiments cover a range of sizes and are applied to various coding tasks for validation.

### Weaknesses
There are some symbols, such as what s1 and s2 in Figure 2 are not defined, and the same applies to Stage 4 of Figure 1.
Additionally, there should be clear conclusions to answer the two key questions raised in lines 356-360.

### Questions
1. In line 242, the source of the "3,650 samples" used for single-token perturbations needs clarification. 
2. In section 4.1, the specific construction steps of the Test Dataset require further elaboration, ideally with detailed examples or illustrations, and it should be noted whether the dataset is publicly available.
3. Additionally, does the CAUSAL TRACING METHOD only consider the influence of a single token on the target token, without accounting for the effects of multiple or consecutive tokens?
4. In line 180, it mentions that specific tokens come from "the output of the final layer of a Transformer before the linear layer." However, given that ChatGPT is a black-box model accessed via an API, how to obtain the token output from the ChatGPT model is a question that needs to be addressed.
5. Note that this is not essential but could be considered: in the APPLICATION: IPR-BASED KNOWLEDGE EDITING section, providing a comparison with prefix tuning techniques, such as LoRA and prefix tuning, including the number of parameters.

### Soundness
2

### Presentation
2

### Contribution
3
