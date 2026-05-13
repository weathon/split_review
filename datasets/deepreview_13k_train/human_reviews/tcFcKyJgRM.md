# HeaP: Hierarchical Policies for Web Actions using LLMs

- Decision: Reject
- Scores: 8, 3, 6, 3

## Abstract
Large language models (LLMs) have demonstrated remarkable capabilities in performing a range of instruction-following tasks in few and zero-shot settings. However, teaching LLMs to perform tasks on the web presents fundamental challenges -- combinatorially large open-world tasks and variations across web interfaces. We tackle these challenges by leveraging LLMs to decompose web tasks into a collection of sub-tasks, each of which can be solved by a low-level, closed-loop policy. These policies constitute a shared grammar across tasks, i.e., new web tasks can be expressed as a composition of these policies. We propose a novel framework, Hierarchical Policies for Web Actions using LLMs (HeaP), that learns a set of hierarchical LLM prompts from demonstrations for planning high-level tasks and executing low-level policies. We evaluate HeaP against a range of baselines on a suite of web tasks, including MiniWoB++, WebArena, a mock airline CRM, as well as live website interactions, and show that it is able to outperform prior works using orders of magnitude less data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces HeaP, a framework that leverages Large Language Models (LLMs) to decompose complex web tasks into modular sub-tasks. It uses a hierarchical approach, learning high-level task plans and low-level policies from human demonstrations, enabling LLMs to perform web actions effectively. It addresses challenges related to the combinatorially large space of web tasks and variations in web interfaces. Experimental results demonstrate that HeaP outperforms previous methods with significantly fewer training examples on various web tasks and interfaces such as MiniWoB++, WebArena, and a mock airline CRM

### Strengths
-Originality: The idea is interesting in the way HeaP leverages hierarchical policies to decompose complex web tasks using a high-level task planner 
 into modular  low-level web policies.

-Quality: The paper is quite thorough in its experimental setup as it tests on 4 interesting datasets, including simulated and live websites, to assess the performance of the proposed approach. 

-Clarity: The paper is well-written and structured, making it easy for readers to follow and understand the proposed approach

-Significance: The paper addresses a significant challenge in the field of natural language processing and machine learning, which is teaching LLMs to perform web-based tasks which can lead to a huge set of applications

### Weaknesses
 - The tasks are not that challenging and the results are very weak relative to how powerful the LLM model used here which is GPT-3.5. For example, it seems that the proposed method struggles with book-flight which is a basic constrained task and therefore this method is very far from being deployed in the real world

- Using closed source methods like GPT-3.5 is expensive. I'd be curious to see how this method would perform with open source methods like Llama and Mistral.

- No code was provided to asses and verify the results as well as understand the low level details of how the method is implemented

### Questions
Please address the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method HeaP for LLM to perform tasks on the web. It first asks LLM to decompose the task into several steps as a planner, where each step is a call to low-level policies. Then within each low-level policy, LLM is called to predict the next action sequentially. Both the planner and low-level policy execution have prompts constructed automatically by collecting few shot examples from autolabeled human demonstrations. Extensive experiments over several datasets demonstrate the gain over ReAct which does not use hierarchical planning.

### Strengths
- The paper is overall easy to read, although some important methodological details like autolabeling and prompt construction are in appendix which makes it hard to read.
- The experiments are extensive over 4 datasets with many tasks. The gain demonstrated is substantial.

### Weaknesses
 - The paper is overall easy to read, although some important methodological details like autolabeling and prompt construction are in appendix which makes it hard to read.
- The experiments are extensive over 4 datasets with many tasks. The gain demonstrated is substantial.

- The idea of hierarchical planning with a high-level planner and low-level policies using LLM has been explored by many previous robotics works e.g. LLM-planner (https://arxiv.org/pdf/2212.04088.pdf and the line of works they cited). Additionally, PaP (https://aclanthology.org/2022.suki-1.8.pdf) and Parsel (https://arxiv.org/pdf/2212.10561.pdf) have also explored similar ideas of prompting LLM to generate a hierarchical plan but implementing low-level planners with programs. Implementing both high-level and low-level planners with LLM prompting has been explored in Decomposed Prompting (https://openreview.net/pdf?id=_nGgzQjzaRy). Considering these previous works, the novelty of this paper is limited to applying existing ideas to web datasets and potentially the technical details of autolabeling from human demonstrations.
- The low-level policies are manually defined during autolabeling, making the framework limited in flexibility comparing to previous works that allow LLM to generate decompositions freely. 
- The only LLM prompting baseline compared against is ReAct, which demonstrates the benefits of hierarchical planning. However, such benefits have been demonstrated with the prior works mentioned above.

### Questions
n/a

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a framework that learns hierarchical prompts from demonstrations for planning high-level tasks and executing them via a sequence of low-level policies. The approach decomposes complex web tasks into a sequence of high-level subtasks, each of which can be then solved by a sequence of low-level policies. This method learns hierarchical LLM prompts for both levels of tasks and policies. The approach was evaluated on a range of increasingly complex benchmarks and the results show that the proposed approach achieves excellent performance compared with existing approaches.

### Strengths
The approach introduces a novel hierarchical approach to prompt LLMs to perform web tasks. Experimental results on various complex web benchmarking datasets show the superiority of the proposed approach.

### Weaknesses
I recommend moving some implementation details like prompts into the main body to help the reader better understand the work.

### Questions
Do you label the high-level task plans?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work presents their design of a web action agent with LLM that can follow the natural language instruction and perform actions on the website. The agent consists of a high-level planner and a low-level actor, both of which invoke LLM for concrete output given different input context and prompt. The core idea is to decompose the task to achieve higher performance and generalization capacity.

### Strengths
The design of this method is sound and reasonable. 

Exhaustive details of the prompt and results analysis are presented.

### Weaknesses
The evaluation is based on too few samples: 45 tasks on MIniWob++, 125 examples of two domains on WebArena, 5 distinct tasks with 20 scenarios on Ariline CRM, and 3 website with 10 searches per site on Live Websites.

Given the fact that human demonstration is collected to form the prompts to the LLM in HEAP, it should be actually evaluated on more diverse websites instead of fewer websites.

### Questions
1. Could the author elaborate on the demonstration collection process described in 4.2?

2. What's the purpose of D_{label} on the end of page 4 (Sec 4.2)? How does this dataset utilized in the HEAP?

3. What is the trainable component in the HEAP? e.g. which function / parameters described in Algorithm 1 is learnable? 

4. Why the models are not evaluated on the entire benchmarks but only a set of them. 

5. What does training size 21 in Table 1 last row mean? The HEAP was shown 21 samples, in which format, to train which part?

6. It really depends on the demonstration collected and the diversity of evaluation cases that whether the benefit claim of "sample efficient" and "generalization" are sound.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
