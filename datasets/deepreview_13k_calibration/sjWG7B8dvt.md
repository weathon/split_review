# Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Large Language Models (LLMs) are susceptible to security and safety threats, such as prompt injection, prompt extraction, and harmful requests.
One major cause of these vulnerabilities is the lack of an instruction hierarchy.
Modern LLM architectures treat all inputs equally, failing to distinguish between and prioritize various types of instructions, such as system messages, user prompts, and data. 
As a result, lower-priority user prompts may override more critical system instructions, including safety protocols. 
Existing approaches to achieving instruction hierarchy, such as delimiters and instruction-based training, do not address this issue at the architectural level.
We introduce the \textbf{I}nstructional \textbf{S}egment \textbf{E}mbedding (ISE) technique, inspired by BERT, to modern large language models, which embeds instruction priority information directly into the model. 
This approach enables models to explicitly differentiate and prioritize various instruction types, significantly improving safety against malicious prompts that attempt to override priority rules. 
Our experiments on the Structured Query and Instruction Hierarchy benchmarks demonstrate an average robust accuracy increase of up to 15.75\% and 18.68\%, respectively. 
Furthermore, we observe an improvement in instruction-following capability of up to 4.1\% evaluated on AlpacaEval. 
Overall, our approach offers a promising direction for enhancing the safety and effectiveness of LLM architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address robustness issues within Large Language Models (LLMs), authors introduce Instructional Segment Embedding (ISE), where they give the model hierarchical information about the input through an embedding layer. The hierarchy is divided by ‘system, user, data, and output’. To encode this hierarchy, an additional embedding layer is given to the LLM. Each token embedding (each tokenized word of the input) is given an embedding of the size 4xD, where D is the embedding dimension, and four representing the hierarchy levels. They are tagged corresponding to their hierarchy, and the “segment” embedding value is added to the original token value and fed to the rest of the model. 	
In the evaluation, ISE is compared to a method that adds delimiters between hierarchies. It generally performs better than the delimiter method. The datasets used are Structured Query and a new Instruction Hierarchy dataset.

### Strengths
The paper is generally well written.

The paper addresses an important issue about trustworthiness of LLMs.

### Weaknesses
I had a difficult time understanding the problem statement at the beginning of the paper.

The major weakness of the paper is the novelty of the approach. The approach merely adds an embedding layer to the LLM.

Page 4: The authors state that the standard supervised fine tuning approach “remains a fundamental limitation.”(line 180) I think it would be nice to summarize the limitations/experimental results a bit here.

Page 8, Robustness figures can be very misleading/look different based on order data chosen, I would recommend using a different figure.

The paper uses pretty small models (8-13B) and are adding (context length) x (embedding length) x 4 more parameters (so like up to 32 000 x 5120 x 4 = almost another billion parameters).An ablation study of just adding this number of tokens without “hierarchical splitting” and seeing how the model improves would be beneficial.

It appears that adversarial training can do most of the work for avoiding hierarchical attacks? (Table 1)

In the dataset designed for the task in question (Instruction Hierarchy), ISE doesn’t perform much better than the baseline. (Figure 6 and 7)

### Questions
Page 9, line 467: Why use the UltraChat Baseline if its instruction-following capacity is so weak? Why not choose a different baseline?

Page 9, line 483: Define “reasonable responses.” How was GPT-4o queried to evaluate “reasonable responses”?

Line 247-250: How did you decompose GPT-4o to decompose 10K prompts to 3 components? Does it know the hierarchy?

How specifically are the hierarchies encoded in the embedding matrix? Are lower indices in H automatically considered lower importance? How is the training data used in conjunction with this?

How do you know that the GPT 4 output is correct?

Any reason for just summing the segment embedding with the token embedding? What about concatenation? Would like to see ablation or justification.

## Post-rebuttal comments 

The authors addressed most of my concerns in their response resulting in my increased score to 6.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Instructional Segment Embedding (ISE) to enhance LLM safety by enabling the model to better distinguish and prioritize instructions.  The authors conducted comprehensive experiments on two benchmarks (Structured Query and Instruction Hierarchy) using multiple pre-trained LLMs, including Llama-2-13B, Llama-3-8B, and Llama-3.1-8B, and demonstrated the effectiveness of the proposed approach.

### Strengths
1. The idea of introducing instructional segment embedding to directly enhance LLM’s safety is novel and promising.
2. The authors provide rigorous experimental validation on a range of tasks and demonstrate the method’s effectiveness.

### Weaknesses
1. The paper employs full-parameter fine-tuning to learn the instructional segment embeddings, but it’s unclear if the baseline models are fine-tuned similarly. Is it a fair comparison? An ablation study evaluating baseline performance with the same fine-tuning across all datasets (Clean Alpaca, Adversarial Alpaca, UltraChat) would strengthen the paper
2. The paper lacks an assessment of how well the segment embeddings generalize across datasets. Specifically, it would be valuable to see how embeddings trained on one dataset (e.g., Clean Alpaca) perform when tested on a different dataset (e.g., UltraChat). It is unclear if the observed improvements are due to the embeddings themselves or overfitting to the training data.
3. Full-parameter fine-tuning, as proposed, may not be cost-efficient or scalable for larger LLMs. Exploring alternatives to full-parameter fine-tuning could make the approach more practical for broader applications.

### Questions
1. Can the authors expand on the evaluation part as mentioned above?
2. Can the authors elaborate on the feasibility of using parameter-efficient fine-tuning methods like LoRA or prefix tuning with ISE.?
3. Can the authors conduct more specific cross-dataset experiments to demonstrate generalization, such as training on Clean Alpaca and testing on UltraChat, or vice versa?

### Soundness
2

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
3

### Summary
The paper proposes Instructional Segment Embedding (ISE) - a technique to encode instruction hierarchy in LLMs, aiming to improve robustness to vulnerabilities such as prompt injection, prompt extraction, and jailbreaks. The method works by training a "segment embedding" for each segment (system, user, data, output), enabling the model to distinguish between the segments at the level of internal representation. The authors evaluate ISE on two benchmarks, reporting improvements in robustness against various attack types.

Rating: 5- marginally below the acceptance threshold
Reasoning: ISE presents a compelling and well-motivated approach to enhancing LLM safety. However, the current experimental sections lack the necessary clarity to fully assess the effectiveness and applicability of ISE. Improving the explanation of training and evaluation processes would significantly strengthen the paper’s contributions.

### Strengths
- Clear problem framing and motivation
  - The paper addresses a significant problem with modern LLMs. The lack of separation between different levels of input makes models vulnerable to prompt injection, prompt extraction, and jailbreaks.

- Promising and intuitive solution
  - ISE is a simple and well-motivated solution - it is natural and straightforward, making it a very good idea.
  - The paper's presentation in sections 1-4 is very clear.

### Weaknesses
 - Lack of clarity in experimental design and results
  - Sections 5 (Experimental Design) and 6 (Results) are difficult to understand, which makes it challenging to asses the performance of the method. I think the paper would benefit significantly from a refactoring of these sections to be as clear as possible.
  - Concretely:
    - It is unclear how the malicious instructions in Adversarial Alpaca are generated, and how the instructions in training relate to those in testing.
    - It is unclear how much of Alpaca contains user vs data instructions.
    - Same questions apply for the Instruction Hierarchy dataset.
       - With this dataset, there is also a question of whether the outputs (generated by GPT-4o, according to Appendix B) represent desired behavior, or exhibit vulnerability to the attacks (since GPT-4o itself is vulnerable to prompt injection).
    - See more questions below.
  - Without a clearer presentation of methodology, it is difficult to assess the conclusions that ISE improves robustness to injection attacks.

### Questions
1. Do the baselines involve fine-tuning?
    - This was unclear to me. Certainly the baselines should include fine-tuning on the same training set, but this was not clear from the manuscript.

2. For the Structured Query training dataset (Alpaca), what was the split between system vs user vs data?
    - As written in Appendix B, I see that system and user are combined into a single instruction type. Do all of the Alpaca prompts have a data component? If not, it seems trivial for the model to separate the system/user portion from the injected data portion.

3. For the Structured Query Adversarial Alpaca, are the injections of the same form as the evaluation injections (i.e. aiming to make the model output "hacked")? Or are they varied?
  - This seems like an important detail to assess if the model's robustness is generalized or limited to specific/narrow instances of injection.

4. For the Structured Query evaluations, which subcategories (Naive, Ignore, Escape-S, Completion-R) were included in the training dataset?
    - Appendix B suggests just Naive and Completion - I think this should be indicated in the main body.
    - Why is this not the notion of "in-distribution" vs "out-of-distribution" used (i.e. based on type of attack, vs where the attack is placed)?

### Soundness
2

### Presentation
2

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
This paper introduces instruction segment embedding, a type of input embedding that marks the hierarchy of text inputs in LLMs. It divides inputs into four categories: system message, user prompt, data, and output. While segment embedding itself isn’t entirely new, the experiment results in the paper on the Structured Query and Instruction Hierarchy datasets show that this approach helps LLMs follow instructions better and improves their safety.

### Strengths
* The method is simple and effective, and the results back up the improvements claimed.
* The writing is clear and easy to follow, making it straightforward to understand.

### Weaknesses
Despite the strong experiment results, this paper lacks a more insightful investigation into the learned segment embedding. I am not surprised that adding segment embedding can improve the LLM's general following capability and safety since it is commonly used in many domains like dialogue language model, vision transformer. Therefore, I think the reason for this improvement is more interesting other than the performance difference. In particular, I am curious about how the attention pattern changes after adding the segment embedding. I would recommend authors investigate several scenarios to provide more insights about the segment embedding:
  * What's the model behavior if no system prompt is provided?
  * What's the model behavior if system prompt also uses user request segment embedding? Also, what if the data parts uses user segment embedding instead of data embedding?
  * What's the attention pattern difference between a model with segment embedding and one without given attack prompt and benign prompt?

The paper only tests fixed prompt-space attacks to evaluate the new LLMs robustness to attacks; adding automatic attacks, like PAIR or PAP, could make the evaluation more complete.
The experiments mainly focus on single-turn conversation data, which may limit the understanding of how the model would perform in multi-turn conversations.

### Questions
1. Can authors clarify how an instruction-following data sample is converted to the proposed format? Examples showing what parts of a sample are labeled as system, user, and data would be helpful. I’m especially interested in how to distinguish between user and data segments since it's possible that users first provide data, then raise a request. Or multiple data/request in the input.

2. If attackers can change the system message, is it possible that the model become more vulnerable to this kinds of attacks? I wonder if the instruction segment embedding strengthens the effect of system prompt too much.

### Soundness
3

### Presentation
3

### Contribution
2
