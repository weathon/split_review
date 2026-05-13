# Benchmarking Large Language Models as AI Research Agents

- Decision: Reject
- Scores: 1, 3, 6, 3

## Abstract
Human researchers can perform scientific experimentation loops – planning, experimenting, observing the results, and generating inferences. Can we build AI research agents to perform the same? To take a step towards building and evaluating research agents capable of such open-ended decision-making, we focus
on the problem of having agents perform machine learning (ML) tasks given a
research problem description and dataset. In this paper, we propose MLAgent-
Bench, a suite of ML tasks for benchmarking AI research agents. Agents can
perform actions like file system operations, executing code, and inspecting outputs.
With these actions, agents could run experiments, analyze the results, and modify
the code of entire machine learning pipelines, such as data processing, architecture, training processes, etc. The benchmark then automatically evaluates the agent’s performance objectively over various metrics related to performance and
efficiency. We also design an LLM-based research agent to automatically perform
experimentation loops in such an environment. Empirically, we find that a GPT-4-
based research agent can feasibly build compelling ML models over many tasks in
MLAgentBench, displaying highly interpretable plans and actions. However, the
success rates vary considerably; they span from almost 90% on well-established
older datasets to as low as 10% on recent Kaggle Challenges – unavailable during
the LLM model’s pretraining – and even 0% on newer research challenges like
BabyLM. Finally, we identify several key challenges for LLM-based research
agents such as long-term planning and hallucination. Our code is released at
https://anonymous.4open.science/r/MLAgentBench/.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a new benchmark for AI agents that conduct AI research, called MLAgentBench. The authors provide a baseline algorithm based on GPT-4 which achieves some successes on various tasks within the benchmark, but which also demonstrates the large gap between the state-of-the-art and expert performance, inspiring future research in this area. The code for the paper is open-sourced, enabling researchers to reproduce these results and build new models that push the frontier of AI research agents.

### Strengths
- The authors provide a novel, rigorous, open-source evaluation benchmark to galvanise and focus the community on the important topic of AI research agents. 
- The benchmark includes a well-chosen range of tasks, which represent a diverse range of machine learning challenges, from standard problems to more difficult Kaggle challenges. 
- The paper is very well-motivated, and the descriptions are clear and lucid throughout. 
- The authors provide a state-of-the-art agent, alongside baselines and ablations. The "no-retrieval" ablation, for instance is a good choice that enables the reader to establish scientific intuition and may inspire future work. 
- Qualitative analyses of agent behavior provides an insight into the capabilities and limitations of the agents.

### Weaknesses
- In the Results section figures, it is unclear what is meant by "baseline". Could the authors please clarify which model this is? It would be good to make this clear in the figure captions. 
- It would be useful to have a slightly longer description of each of the MLAgentBench tasks in Table 1. At the very least, a few words in the caption explaining the definitions of the terms used in the "task" column (e.g. node classification, improve speed, implement tool) would be very useful. 
- The future work section is too thin for a benchmark paper. Can the authors provide some more suggestions for possible future lines of agent research? For this paper to be maximally impactful they should take this opportunity to provide researchers in the field with some inspiration to drive rapid progress on this benchmark!

### Questions
See "Weaknesses".

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a benchmark for AI research tasks for large language model (LLM) based agents. They collect 15 tasks from various machine learning problems, ranging from “solved” tasks like cifar10 to “unsolved” tasks like BabyLM. Tasks consist of initial code and instructions to solve or improve performance for a given problem. They design baseline agents and assess their ability using the benchmark, showing that they are able to achieve >10% performance increases for many of the tasks, with varying success depending on model used, task type, and agent design. They perform a number of studies on the types of mistakes agents make, and the efficiency of agents in terms of tokens used.

### Strengths
The ability of LLMs to conduct research is an interesting question that seems to follow naturally from the focus on the reasoning ability of LLMs. A benchmark to measure this ability could be a valuable contribution. This paper does a lot of work analyzing the types of errors agents make, which is also valuable for the community.

### Weaknesses
Overall, while this paper contains some interesting findings and raises an interesting question, I feel that it needs more polishing before it’s ready for publication.

1. Though the main point of the paper is proposing a benchmark, there is relatively little information on how these tasks were selected and how the benchmark was constructed. The benchmark consists of only 15 tasks, and while there is some detail on the attributes that made the authors select these tasks, there are not enough to convince me that this is a thorough enough benchmark in its current state. Issues such as potential data contamination, formalizing what aspects of research are being tested and how these are addressed by the chosen tasks should be explained further.
2. Relatedly, the framing of this as an AI benchmark is slightly misleading. It tests LLM ability to complete research in empirical machine learning tasks, but does not test their ability to do other types of research (e.g. more qualitative or descriptive research not based purely around achieving performance increases). Though some elements of the process may remain the same, 15 tasks from machine learning are not enough to test an agent’s overall research ability.
3. The success criteria for these tasks involves models improving performance by >10%. This strongly limits the types of tasks that can be tested, as discussed in the previous point. However, it also provides limited insight into the performance of the model. One of the strengths of this paper is the analysis of the types of errors models make, but this is all done through human evaluation. For tasks involving many reasoning steps where lots can go wrong, it would be more valuable to see some breakdown of which step the model failed at or some other type of automated error analysis.

### Questions
1. Did you explore how likely it is that these tasks and their solutions appeared in training data? For example, for solved tasks, it seems likely that models would have seen high performing solutions already. Did you study this at all, either by looking at the data or comparing the similarity of model output to existing solutions?
2. Was human annotation performed by the authors? What was the criteria for annotation? If it was not performed by the authors, how were annotators recruited/paid?
3. What aspects of the tasks chosen make them suitable for testing research in general? What kind of research do you expect an agent achieving perfect performance on your benchmark to achieve?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new benchmark, MLAgentBench, for evaluating AI research agents that can perform open-ended ML tasks given a task description and a dataset. 
The benchmark provides a set of diverse and tasks, an environment where agents can interact with files and execute code, and metrics to measure the competence, reasoning, and efficiency of the agents. 
This paper tests several famous LLM and presents the experimental results.

### Strengths
It proposes a novel and general framework for specifying and evaluating AI research agents on ML tasks. 
It tests the feasibility and effectiveness of using common LLMs as AI research agents.

### Weaknesses
The testing scenario is simplistic and greatly differs from the demands of the real world to some extent, which limits its ability to accurately reflect the true capabilities of the model.

### Questions
Why is there no AutoGen test which should be much stronger than AutoGPT? 
If the output and input exceed the LLM context length during the process, how can it be resolved?
Will the model being tested receive feedback from the evaluation results of the submission? Will it then continue to carry out operations to improve the results?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a benchmark for evaluating large language models as AI research agents. The benchmark encompasses multiple modalities and a variety of tasks. Each task consists of reading a problem description and taking actions in an environment defined by the authors. Most of the problems are taken from Kaggle, with care taken to ensure that at least some of the problems were put online recently, so LLMs haven't had a chance to train on them. The authors then evaluate GPT-4 and Claude-1 on the benchmark, as well as agentic frameworks built around these models, such as AutoGPT and LangChain-React.

### Strengths
The paper is original, novel and addresses a significant research question. The benchmark covers a range of tasks, and the largest API-only LLMs (GPT-4, Claude-1) are evaluated. The evaluation of agentic frameworks like AutoGPT and LangChain-React is also useful, and surprising — I expected them to be better.

### Weaknesses
I have concerns about the relevance of the tasks chosen with respect to "AI Research". Some of the tasks are hardly "research tasks":
- CIFAR10
- IMDB
- Kaggle House Prices
- Kaggle Spaceship Titanic

I'm skeptical any research is being done on the Kaggle House prices dataset or the Spaceship Titanic dataset. 

The best possible action if pushing performance on CIFAR10 and IMDB at this point would be to load pretrained models from HuggingFace or TIMM and run it on CIFAR 10/IMDB, which is not research. 

The LLM Tools section does not seem possible to evaluate quantitatively, and the relevance of `bibtext-generation` to AI research seems tenuous. 

This means that 6/15 proposed tasks are not directly relevant to ml research. 

I understand that the motivation was 
> The tasks are chosen such
that they range in various difficulties and recency to test the generalizability of the research agent and
avoid data contamination. 

But I don't see anything to constrain the actions of the agent. If the task is to improve the baseline model, can I "improve" it by sticking it as one branch of a model that uses a much larger pretrained model? Why / why not? 

Right now, the problem I see is that the work is a collection of ~15 already existing tasks, with ~6 of them having arguable relevance to contemporary ML research. There needs to be additional work on top of this to make it a generally usable benchmark, such as constraining the actions of the agent, or defining each task more precisely, or adopting a principled definition of a research workflow and only including tasks based on that.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
