# Understanding the Interplay between Parametric and Contextual Knowledge for Large Language Models

- Decision: Reject
- Scores: 5, 5, 3, 6, 6

## Abstract
Large language models (LLMs) encode vast amounts of knowledge during pre-training (parametric knowledge, or \pk) and can further be enhanced by incorporating contextual knowledge (\ck).
Can LLMs effectively integrate their internal \pk with external \ck to solve complex problems?
In this paper, we investigate the dynamic interaction between \pk and \ck, categorizing their relationships into four types: \textit{Supportive, Complementary, Conflicting}, and \textit{Irrelevant}. To support this investigation, we introduce \textsc{EchoQA}, a benchmark spanning scientific, factual, and commonsense knowledge. Our results show that LLMs tend to suppress their \pk when contextual information is available, even when it is complementary or irrelevant. While tailored instructions can encourage LLMs to rely more on their \pk, they still struggle to fully leverage it. These findings reveal a key vulnerability in LLMs, raising concerns about their reliability in knowledge-intensive tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper analyzes interactions between LLM parametric knowledge and contextual knowledge. It finds that parametric knowledge often gets suppressed when contextual information is provided. The paper tests several prompt techniques to improve the recall of parametric knowledge. The authors also plan to release a benchmark that they used to test this phenomenon.

### Strengths
The paper sheds light on an important phenomenon that contextual information in some cases prevents LLMs from recalling parametric knowledge.

The authors tested several major LLMs with various reasoning type tasks and various instructions.

### Weaknesses
I ran examples provided in the paper on three LLMs (Llama3, ChatGPT, Gemini) and wasn't able to reproduce the problem/results.

More importantly, I'm not convinced that the problem definition is valid across all setups that the paper explored: if the prompt provides distracting or conflicting knowledge, why should we expect the models to generate parametric knowledge and not follow the prompt?

This paper does not propose a solution, only highlights the problem.

The EchoQA dataset that will accompany this paper is a reformatted and processed version of four previously released datasets. It is not clear how much effort/novelty went into compiling this dataset.

### Questions
Is it even correct to expect from LLMs to rely on parametric knowledge recall (rather than following a prompt) when the prompt contains distracting/conflicting information?

### Soundness
2

### Presentation
3

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
This work investigate the interaction between the knowledge in model parameters (parametric knowledge, PK) and in-context knowledge (CK) by designing benchmark, ECHOQA, to explore if large language models could effectively utilized PK and CK together to solve the tasks. They define the PK by ensuring the LLMs could reach 100% performance for the knowledge and then define CK by construct them following four types of relation: supportive, complementary, conflicting, irrelevant. The experiments on ECHOQA seems to show that models are relying more on CK instead of utilizing PK (which might not be that surprising).

### Strengths
The direction about exploring the interaction between PK and CK is interesting.

The experiment and analysis seems comprehensive.

### Weaknesses
Though the direction is interesting, some designs might be further discussed. For example, 
1. How to define PK? What types of knowledge are considered as parametric knowledge? In this work, they seem to focus on world (science, factual, commonsense) knowledge while this set might not be comprehensive and could be biased (for example, certain types of knowledge might appear more in the training set and thus less likely to be affected by in-context-knowledge and certain types of information is rare in pre-training corpus and might be easily modified by in-context-prompts).

2. Also, different models might have different sets of PK based on the training corpus. As a results, the benchmark might not be generalized well to different sets of models.

3. The knowledge in the context might be more desired to use in actual applications as well. In actual use cases, people will put their own/personalized knowledge in the context and ask questions, and thus naturally hope the model to rely on the in-context text. Especially for the conflicting part, i think it makes more sense for models to rely more on in-context knowledge. And I think it is natural if models are more relied on in-context-knowledge (they should receive higher attention scores if the knowledge is related to the questions). 

4. There are also recent work on the interaction between PK and CK [1] where they encourage the model to utilize both in-context skills and built-in skills to solve the reasoning tasks (math and etc., Table 1, Table 25), which seems to make more sense compared to the conflicting part in the evaluation in this paper.  As in-context knowledge is limited, exploring the way to activate the abilities to utilize necessary PK in the model might make more sense.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper explores how effectively large language models (LLMs) integrate internal parametric knowledge (PK) with external contextual knowledge (CK) to solve question answering tasks. 
The relationship between PK and CK is categorized into four types: Supportive, Complementary, Conflicting, and Irrelevant.
 Based on these definitions, the paper synthesizes various types of evidence across four established QA benchmarks: ALCUNA, ConflictQ, MuSiQue, and OpenBookQA. 
The synthesized evidence is then used to evaluate LLM behavior when presented with different types of CK, utilizing three distinct hand-crafted prompts.
Empirical results reveal a range of phenomena based on these evaluations.

### Strengths
a. This paper constructs a new dataset using their synthesized evidence of different types, which could be valuable for future research on the interplay between PK and CK.

b. The experiments demonstrate a considerable level of effort, including analyses involving four QA datasets from different domains and six different LLMs.

c. Some findings from this paper might be new and interesting, such as the significant variance observed when different prompts are used.

### Weaknesses
 a. This paper’s contributions are modest, building upon prior work such as [1] and [2]. While it claims novelty through its evaluation of a broader range of relationships between PK and CK, including beyond just conflict, it is worth considering why conflicting knowledge has been the primary focus in the field—it is the most relevant and impactful aspect to study.  Notably, both the setup and evaluation in this paper are highly similar to those in [1], which was released over a year ago.

b. The paper would benefit from stronger focus and depth, as it currently presents a series of observations using various types of evidence without integrating them into a cohesive conclusion or offering actionable insights for the future design of RAG systems for LLMs. One potentially valuable direction that could have been explored in more detail is the sensitivity of LLMs to different types of prompts.

c. The experimental results in this paper highlight the significant impact of different prompt choices. However, the design of the three prompts used appears ad hoc and arbitrary. As a result, the empirical findings may not effectively translate to more practical, real-world scenarios.

A general issue with this paper is that the experimental setup could benefit from clearer motivation beyond simply aiming to differentiate itself from existing work. This raises questions about the overall value of examining relationships beyond knowledge conflict. Notably, the paper acknowledges that the supportive evidence scenario did not yield any surprising or meaningful results, so it was directly excluded from the main results. For the irrelevant evidence setup, the results appear to reflect primarily the influence of the ad hoc prompt. While the complementary evidence setup shows potential for more interesting insights, the paper’s lack of focus makes it challenging to draw in-depth conclusions from it.

### Questions
1. The numbers in Table 2 do not seem to be complete for ConflictQA/MuSiQue/OpenBookQA？

2. Why there's no speak out loud instruction in Figure 2?

3. The supportive type may not seem particularly interesting or surprising and was excluded from the main results for this reason. However, why do you still consider it important to include it in the final manuscript? Maybe just remove it from your paper.


Typos / Grammer issues:

line 72: LLMs leverage -> LLMs' leverage

line 812: reals -> reveals

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work investigates the interactions between an LLM's internal parametric knowledge and external contextual knowledge. It introduces a new benchmark, EchoQA, focusing on supportive, complementary, conflicting and irrelevant interaction types, to help inform these investigations.

### Strengths
The work is well-motivated and clearly presented. The experiments are well-structured and findings insightful. They are thorough and reveal various interesting and provoking questions about how LLMs operate across parametric and contextual knowledge. These include high level observations, such as that LLMs often disregard their internal knowledge in the presence of contextual knowledge, among a broader set of findings discussed in detail throughout the paper.

### Weaknesses
The work introduces a reasoning-oriented Question Answering task, but the Related Work section provides no mention of existing QA works designed to investigate model reasoning capabilities.

It is unclear which models are used to establish parametric knowledge (is this model-specific, or was one model selected as representative of all LLMs?). Similarly, further discussion of the effects of prompt templates to establish knowledge as presented in Table 5, in the main body of the paper seems valuable. 

Deeper analysis of how different models perform across settings would also be insightful.

Typos:
- L267: ck is not the right format

### Questions
Typos:
- L267: ck is not the right format

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the author proposes a new benchmark called `EchoQA`` to probe the subtle interactions between Parametric Knowledge (PK) and Contextual Knowledge (CK) in Large Language Models (LLMs). It considers the following four types of interactions: **Supportive, Complementary, Conflicting, and Irrelevant**. With this benchmark, the author aims to understand the behavior of LLMs in terms of the interaction between PK and CK, providing insights into existing models. Experimental results show that current models are more likely to rely on Contextual Knowledge rather than Parametric Knowledge even with dedicated instructions.

### Strengths
1.	It is good that the author introduces a new taxonomy to understand the interaction between PK and CK. This taxonomy—Supportive, Complementary, Conflicting, and Irrelevant—offers a useful framework for understanding these interactions.
2.	With the new benchmark, the author conducts a series of experiments to investigate the behavior of LLMs concerning PK and CK interactions. The results are interesting and provide valuable insights into existing models.
3.  The paper is well-structured and clearly written, making it easy to follow the author's arguments and findings.

### Weaknesses
1.	In the experiments, it would be better to discuss results from different types of models (e.g., DPO model, PPO model, SFT model, and so on). In the current version, the author only discusses the results from the base model (e.g. LLaMA-3.1-8B), which is not aligned with enhancing instruction-following abilities. With better instruction-following capabilities, LLMs may be able to follow instructions (e.g., *“Answer the question based on context/yourself”*) and effectively balance knowledge from PK and CK, rather than relying heavily on CK. Consider the author claims that the current models are more prone to rely on CK even with dedicated instructions (LINE 21-22), it would be interesting to see how different models (e.g. LLaMA-3.1-8B-Instruct) perform in this scenario.

2.	In lines 84-85, the author mentions that the reason behind the behavior is the imbalance of knowledge in the training corpus. However, I am not sure how the author defines the “popularity” of knowledge in the training corpus. Does this refer to the frequency of the knowledge appears in the training corpus (e.g. CommonCrawl) of LLMs?
3.	It would be good to discuss more relevant works on the interaction between LLMs and CK/PK.

### Questions
1.	In lines 84-85, the author mentions that the reason behind the behavior is the imbalance of knowledge in the training corpus. However, I am not sure how the author defines the “popularity” of knowledge in the training corpus. Does this refer to the frequency of the knowledge appears in the training corpus (e.g. CommonCrawl) of LLMs?
2. It would be good to discuss more relevant works on the interaction between LLMs and CK/PK.

### Soundness
3

### Presentation
3

### Contribution
2
