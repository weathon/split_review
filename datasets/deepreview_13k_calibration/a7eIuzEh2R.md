# MANGO: A Benchmark for Evaluating Mapping and Navigation Abilities of Large Language Models

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Large language models such as ChatGPT and GPT-4 have recently achieved astonishing performance on a variety of natural language processing tasks. 
In this paper, we propose MANGO, a benchmark to evaluate their ability to perform text-based mapping and navigation. 
Our benchmark includes $53$ mazes taken from a suite of textgames: each maze is paired with a walkthrough that visits every location but does \emph{not} cover all possible paths. 
The task is question-answering: for each maze, a large language model reads the walkthrough and answers hundreds of mapping and navigation questions such as ``How should you go to \code{Attic} from \code{West of House}?'' and ``Where are we if we go \code{north} and \code{east} from \code{Cellar}?''.
Although these questions are easy for humans, it turns out that even GPT-4, the best-to-date language model, performs poorly when answering them. 
Further, our experiments suggest that a strong mapping and navigation ability would benefit the performance of large language models on relevant downstream tasks, such as playing textgames. %
Our MANGO benchmark will facilitate future research on methods that improve the mapping and navigation capabilities of LLMs. 
We host our leaderboard, data, code, and evaluation program at 
{\small \url{\weburl}} and {\small \url{\giturl}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a benchmark that evaluates the mapping and navigation abilities of LLMs. The proposed benchmark covers 53 mazes as well as evaluation strategies taken from text games dataset and modified to suit the requirement for the benchmark tasks. As base model performance is poor, hence it is claimed for future scope of research. Also, the authors promise to release the data and code. The authors claim their work as a first to measure the mapping and navigation abilities of LLMs. However, the novelty and hardness of the work done is not established.
Suggestions:
An experiment might be comparing trained human performance in similar task vs a data trained LLM.

### Strengths
The paper does a good work of curating a benchmark for text games based navigation and mapping. 
The metrics of evaluation for two identified tasks, namely DF and RF questions (destination, route) gives an head start to reuse existing datasets posing them for a different problem.

### Weaknesses
I will like to see the benchmark performance for random responses (within a class bound) to verify the amount of information gained by base model. 
Need some explaination regarding para before 3.4 in terms of pilot experiments.
Related work should be broken into sub-sections of research topics - the current norm - for ease of readibility.
The purpose of Fig. 6 which is too much info is not clear.
In page 7, what makes the maze challenging needs some results to support the text descriptions below.
The use cases and applicability in real life scenarios like robotics is not well established, requesting to look to the plethora of work in embodied intelligence and adapting the problem in that regard.

### Questions
How will the system evolve if vision language based models like CLIP need to be tested - as that is more practical?
How fruitfull are game environments to real life human occupied or indutstrial environments? Is the transfer easily equitable?
How are the easy and hardness of the DF, RF questions come up to? How does it vary with dataset characteristic changes?
What are the runtimes for the experimental evaluations? 
Are any subset minival of the dataset available for checking the model performance quickly? 
Also, why restriction to GPT based models only?
How is ambiguity in location and maps resolved? Any technical relation with length of text description?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new benchmark dataset for evaluating the mapping and navigation abilities of large language models. The authors construct 53 mazes from a suite of textgame. Given a walkthrough that visits every location in the maze, the LLM is tested with a suite of synthetically generated destination-finding and route-finding questions. The authors test with three families of LLMs, RWKV, LLAMA-2 and GPT, as well as LLMs of different sizes and notice clear performance gap in terms of model capabilities. They further conduct deep comparison between GPT 3.5 and GPT 4 on a range of controlled experiments which helps understand the factors that affect model performance, as well as the association with downstream tasks.

### Strengths
1. The data collection protocol is carefully designed and clearly stated in the paper. Making it easy to follow. The design of the task is elegant, challenging for models, yet rather straight forward for humans. The collection effort is non-trivial and the authors have carefully cleaned the data. 
2. The author conducts thorough comparison between GPT 3.5 and GPT 4 and extensive controlled experiments to help understand the model performance and how it associates with different features of the task.

### Weaknesses
1. While the experiments in the paper do demonstrate that the task is challenging for LLMs, it is unclear for me how the proposed benchmark differs from all other datasets in the literature. In particular:
    1. Is it necessary to derive the dataset from real textgames? Would it work to use pure synthetic data, similar to how some of the symbolic reasoning datasets such as SCAN are created.
    2. How this compares to datasets used in embodied AI and NL navigation such ALFRED?
    4. Does the dataset reveal strength/weakness of the LLMs that is overlooked on other datasets?
2. The authors conduct extensive experiments on GPT-3.5 and GPT-4 which is very helpful. However, instead of focusing on models that already perform good, I feel the paper could benefit from more experiments on:
    1. Why the other models perform much worse than GPT models, although they have demonstrated great performance on other tasks.
    2. Why for models like RWKV and LLAMA the size does not seems to affect the performance much.
    3. Are specific model designs, such as attention, position embedding, instruction tuning, affect the performance?
3. In the paper the LLMs are prompted to directly generate the solution, with small amount of COT reasoning. This is actually different from how human solve the task, where oftentimes we need to parse the walkthrough and draw the map first. This is also how many embodied agent/NL navigation works have built up the system. I would expect a baseline on this direction to have much better performance.

### Questions
1. Is there comparison between the proposed benchmark with pure synthetic generated mazes to demonstrate the value of construct the dataset from real textgames?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to evaluate the mapping and navigating abilities of large language models (LLMs) by proposing a new dataset called MANGO, which comprises 53 mazes taken from Zork-I. The LLMs are given a walkthrough as input and tasked with completing two types of tasks: destination-finding and route-finding. The study evaluates GPT-3.5, GPT-4, LLaMa, and RWKV models on this dataset and provides an analysis of the results for GPT models.

### Strengths
1. The paper is well-written, with clear explanations of dataset construction and experiments.
2. The study focuses on evaluating the mapping and navigating abilities of LLMs, which are important for both natural language processing and robotics. Many current robotics benchmarks overlook these challenges, using high-level functions like navigate_to(target_location) as an atomic operation. This paper highlights the challenges of these tasks and proposes a new dataset to test the abilities of LLMs.

### Weaknesses
1. The proposed dataset does not effectively test mapping and navigating abilities, as the samples can be easily converted into a graph with locations as nodes and directions as relations. This is too simplistic for most real-world robotics scenarios, which involve more complex object and position relationships. For example, the robots in a house, or robots (cars) on the street may be facing much more complex scenes.
2. The simplicity of the current dataset means it could be solved by an agent translating natural language into <source, path, destination> triples, then using code or search libraries. The natural language is generated by patterns, making natural language understanding easy. This paper may have limited research impact, as future studies might follow the path of the GSM8K dataset, using methods such as PAL or LLMs with code interpreters as tools.

### Questions
1. Can this task be addressed using traditional search algorithms like depth-first-search or breadth-first-search?
2. It is suggested that the authors test additional LLMs, particularly those pre-trained on code and fine-tuned on instructions, to provide a more in-depth analysis.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose a new benchmark for evaluating LLMs' mapping and navigation abilities (MANGO) by constructing 53 mazes (language-described walkthrough) from textgames and questions asking the LLMs to find a destination or infer a route. Extensive filtering and human examination are applied to ensure the data quality. Chain-of-Thoughts and prompt engineering are considered for LLMs. A range of latest LLMs including GPT-3.5-Turbo, GPT-4, Llama-2, and RWKV are evaluated accordingly to the success rate of the models in responding to the destination and route finding questions. Experiments show that GPT-3.5 and GPT-4 achieve the best results while still performing poorly on hard questions and occasionally hallucinate nonexistent locations or edges. Analysis also demonstrates that LLMs with better mapping and navigation capabilities can better solve relevant downstream tasks, suggesting potential in addressing other embodied navigation tasks.

### Strengths
Investigating the mapping and navigation capabilities of LLMs is an emergent and practical problem in embodied AI. As a researcher in this field, I am aware that extensive efforts have been devoted to understand and reason about the 3D space, which can greatly facilitate many functions such as explainable localization, path planning, and human intervention in agent navigation. As a result, I am very happy to see the benchmark proposed in this paper which I believe can benefit relevant research. In particular,
- The MANGO dataset is large, it is of an appropriate complexity and suitable for evaluating the LLMs; the selected mazes have clear and traversable structures and the walkthrough are described by rich texts, the spatial positions and agent's actions are nicely integrated, and the proposed destination and route finding questions are clear and effective to reflect the LLMs understanding and reasoning.
- The proposed data has been carefully filtered and examed, especially with the help of human annotators, to ensure the accuracy of text descriptions/questions and traversable paths.
- Dataset statistics, examples, and visualizations are clearly presented in this paper.

Besides, this paper benchmarks the most recent (and popular) LLMs including GPT-3.5, GPT-4, Llama-2, and RWKV on MANGO, and performs comprehensive analyses on their resulting success/failure cases. 
- Important questions such as "what makes those mazes challenging?" are nicely investigated through quantifying factors such as number of locations and number of imputed edges, showing valuable insights of the LLMs understanding.
- Critical issues such as "LLMs occasionally hallucinate nonexistent locations or edges" and "non-GPT models with careful prompt tuning still suffer high chance of failing" have been found, which might guide and inspire future relevant research.
- It was good to see the experiments in Section 3.4 about evaluation on a downstream navigation task - a relatively simple case but it is a nice start (can be improved, consider how it might link to practical navigation in the real-world). 

Overall, this paper was an enjoyable read to me. It is well-motivated, it is technically sound, it introduces a novel and useful benchmark. The paper is also very nicely-written, to me, almost all information are clearly presented.

### Weaknesses
1. The proposed MANGO constructs a simplified text-world, its connection to real-world navigation and mapping of embodied agents is unclear. Specifically,
    - It assumes a known environment but many real-world navigation is only partially-observed. This is a significant limitation as real-world agents must build maps incrementally from their sensory inputs, rather than having a complete map a priori. The benchmark does not address the challenge of simultaneous localization and mapping (SLAM), which is fundamental to real-world navigation.
    - The structures of spaces and agents' actions in MANGO are very simple, whereas in the real-world they are often very diverse and complex. The actions are limited to cardinal directions and do not account for the complexities of real-world movement, such as rotations, variable speeds, and interactions with objects. The spatial layouts are also highly simplified, lacking the intricate details and irregularities found in real environments.
    - It only provides text data and it is hard to extend to visual inputs (consider the emerging large VLMs for addressing similar problems). The lack of visual input makes it difficult to evaluate how well LLMs can integrate visual and textual information, which is crucial for real-world embodied agents. The benchmark does not address the challenges of visual perception, such as object recognition, scene understanding, and handling occlusions.

2. This paper does not discuss any limitation and it is unclear how MANGO can be extended to more practical scenarios in the future.

### Questions
Please address my concerns mentioned in the Weaknesses.

Some questions below are not critical to my evaluation. 
1. Section 2.2 and Appendix: I might overlooked this somewhere but I didn't find clear explanation on why slightly different data is applied to evaluate different LLMs?
2. Apart from the proposed metrics for DF and RF, do the authors think some navigation-oriented measurement might be helpful? e.g., Success weight by Path Length (SPL) (On Evaluation of Embodied Navigation Agents. Anderson et al., 2018).
3. Any results on experimenting with different prompts for the LLMs? And any insight on how to write those prompts?
4. The results shown in Tables are from a single-run of the LLMs or from multiple runs and averaged?

For the others, instead of just responding Yes/No, I hope the authors can share their thoughts that might help further improve this paper.
1. The authors mentioned the drawbacks of using unique IDs for locations (e.g., L01, L02, L03, ...), but it is important in real world because sometimes a space is hard to label with a clear name or there might be many same type of rooms in a building. I wonder how would the results change if IDs instead of names are used in the experiments. I also wonder some commonsense might help in practical navigation (e.g., a kitchen is likely to be on the first floor next to the living room) so a clear name might be helpful.
2. The walkthougt contains detailed descriptions of the observations at each location, how would the results change if those descriptions are removed?
3. Many large Vision-Language Models (VLMs) (e.g., the lastest GPT-4V) have been considered in addressing mapping and navigation problems, with egocentric image or top-dowm map inputs the models have very rich and less ambiguous information than only describing the world with language. I wonder how would VLMs impact the research presented in this paper.
4. What about tunning LLMs on MANGO, e.g., using adaptor for low compute cost, would the results become much better?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
