# DiscoveryBench: Towards Data-Driven Discovery with Large Language Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 5

## Abstract
Can the rapid advances in code generation, function calling, and data analysis using large language models (LLMs) help automate the search and verification of hypotheses purely from a set of provided datasets?
To evaluate this question, we present \discoverybench{}, the first comprehensive benchmark that formalizes the multi-step process of data-driven discovery.
The benchmark is designed to systematically assess current model capabilities in discovery tasks and provide a useful resource for improving them.
Our benchmark contains 264 tasks collected across 6 diverse domains, such as sociology and engineering, by manually deriving discovery workflows from published papers
to approximate the real-world challenges faced by researchers, where each task is defined by a dataset, its metadata, and a discovery goal in natural language.
We additionally provide 903 synthetic tasks to conduct controlled evaluations across task complexity.
Furthermore, our structured formalism of data-driven discovery enables a facet-based evaluation that provides useful insights into different failure modes. 
We evaluate several popular LLM-based reasoning frameworks using both open and closed
LLMs as baselines on \discoverybench{} and find that even the best system scores only 25\%. 
Our benchmark, thus, illustrates the challenges in autonomous data-driven discovery and serves as a valuable resource for the community to make progress.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors consider the question of how capable
state-of-the-art LLMs are at automated data-driven discovery. More
precisely, the authors present a benchmark for this task, designed not
only to assess LLMs’ capability in discovery tasks but also to provide
information for improving these capabilities.

The benchmark presented in this paper consists of 264 manually
collected tasks, along with 903 tasks that were synthetically
generated. This benchmark is used to evaluate several LLM-based
reasoning frameworks, providing useful information on the current
capabilities of such systems in automated data-driven discovery.

### Strengths
S1) The authors introduce a simple yet expressive notion of
data-driven hypothesis. Discovering and validating such hypotheses
from a dataset is a challenging problem for LLMs.

S2) The authors develop a comprehensive benchmark to test the
capabilities of LLMs in discovering data-driven hypotheses.

S3) The authors use the benchmark to test some popular LLM-based
reasoning frameworks, drawing useful conclusions about the
capabilities of these systems in discovering data-driven hypotheses.

### Weaknesses
W1) As part of the benchmark, the authors developed some synthetic
tests. These tests are supposed to capture synthetic task examples
constructed from workflows in published works. However, the authors do
not clearly explain in what sense these synthetic tests properly
represent these workflows.

### Questions
The generation DB-SYNTH consists of four steps intended to capture
synthetic task examples from workflows in published works. In
particular, a task dataset is constructed in the third step by
generating synthetic data using various sampling strategies. The
authors do not explain how these steps, and particularly the data
generation step, provide good representations of the task examples from
workflows in published work (notice that there is a missing reference
to a section in the data generation paragraph). This justification
should be part of this work, as if the synthetic tasks are not good
representatives of the real examples, then we could be asking the LLMs
to solve tasks that may be too simple or too complicated, which could
reduce the quality of the tasks in the benchmark.

### Soundness
3

### Presentation
3

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
The advances in data science and AI seem to be evolving the process of scientific discovery (the scientific method) by (drastically) reducing the time needed to formulate hypotheses, conduct experiments, and evaluate results. This paper proposes a benchmark to evaluate the potential role of LLMs in the automatic formulation of hypotheses, starting from a dataset and a natural language question about that dataset.

Typically, for a classification or regression task, a human will identify certain attributes of interest (A_1, …, A_n), a target attribute Y, and attempt to build a relationship between these elements (A_1, …, A_n → Y). This is the current process for generating new knowledge. In this work, the authors aim to determine whether using LLMs allows for the production of valid knowledge in a more general setting: providing a dataset, posing a general question in natural language to the system using an LLM, and obtaining a response in the form of a scientific discovery. The main question the authors seek to answer is how well this approach performs using state-of-the-art LLMs.

There are some recent tools that evaluate the performance of LLMs in testing well-defined hypotheses (clearly formulated questions on a dataset). These methods utilize a constrained search space to look for hypotheses. DiscoveryBench expands the search space by finding hypotheses in a broader context, closer to a human approach. As expected, the performance of LLMs decreases in this setting. Indeed, the paper shows that the best results achieve 25% performance (which I interpret as 25% of responses being valid knowledge, even if it is a bit more complex to interpret).

### Strengths
- The role of LLMs in the scientific method is still unknown (if one exists), and evaluating their capacity to accelerate the process of knowledge discovery is a topic of significant interest. This work represents an incremental advancement in this domain, providing a formal definition of data-driven hypotheses and expanding the search space for these hypotheses. The paper also proposes evaluating proposed hypotheses against a gold standard using semantic similarity measures. In my opinion, this work is of genuine interest to the community.

- The proposition is well described, and the code is available on GitHub. The authors have done impressive work collecting datasets, defining objectives for these datasets, and constructing gold standard hypotheses.

- The results are clearly presented and discussed, demonstrating the limitations of current LLMs. This methodology can be utilized in the future to observe potential progress in the field of LLMs.

### Weaknesses
 - The process of finding a data-driven hypothesis can be time/energy-consuming. This aspect is not discussed in the paper, and I understand that the page limit might not allow space for such discussions. Although this is not the main focus of the paper, it could be useful to explore whether there is a relationship between the size of the search space and the performance of the results.

- The proposed formalism for defining data-driven hypotheses, discovery goals, and task difficulty is somewhat limited. At the same time, I understand that human expertise is essential in this process, and complete automation is difficult, if not impossible, to achieve.

### Questions
How can it be ensured that the data alterations in the proposed datasets (page 6) do not lead to contradictions with the discovery goal, resulting in only one answer—the target hypothesis?

Minor remarks:
 - Pg 3 : discopagevery --> discovery
 - Pg 6: Sec ?? --> update the number of the section

### Soundness
4

### Presentation
3

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
The work deals with the problem of data-driven discovery using large language models.

### Strengths
The authors attempt to formalize the problem of data-driven discovery, which, in my opinion, is a crucial step towards solving this task. In addition, a benchmark is introduced -- unfortunately, I did not have the chance to look at it in more detail, but the authors claim that they will publicly release it.

### Weaknesses
I am confused with the formulation of the problem of data-driven discovery as in Section 3. In line 049, the authors give an example of a data-driven discovery task: “How did urban land use affect the invasion of introduced plants in Catalonia?” The answer to this task is the ways urban land used affected the invasion of introduced plants in Catalonia (if this is the case). However, in Section 3, line 152, you define a hypothesis as a tuple of three elements and in line 141, you say that a hypothesis maps to supported or unsupported. So, if a hypothesis maps to true or false (supported or unsupported), then the example task that you have in line 049 cannot map to your formulation. Please clarify what is the case and, please specify concretely how the task in line 049 translates to your formulation. 

I have a few other comments/questions regarding the formulation in Section 3:
- In line 139, the authors say that a hypothesis is a sentence/semantic tree, and then in line 152 the authors define a hypothesis as a ternary tuple. Please fix this inconsistency, as it is confusing to the readers. 
- In line 141, the authors talk about a verification procedure \mathcal{V}_D mapping a hypothesis to supported and unsupported. Is my understanding correct, that the goal of the data-driven task is both to find whether a hypothesis is supported and unsupported and to return the exact \mathcal{V}_D? If my understanding is correct, then how do you define the space of valid verification procedures \mathcal{V}_D? I would kindly ask the authors to clarify this part, as it is missing. 
- In line 152, the authors write h := \psi(c,u,r). That formulation essentially means that h (the hypothesis) is defined as its answer, \psi(c,u,r). I believe what the authors want to say is that \mathcal{V}_D(h) = \psi(c,u,r), i.e., that the answer to h is defined as \psi(c,u,r). Please fix the notation accordingly or clarify what you meant.  
- Continuing with my previous comment, I would kindly ask the authors clarify what is the relationship between \mathcal{V}_D and \psi.    
- In line 161, the authors give another definition of the data-discovery task: that of given a goal G, to find a hypothesis h. From Section 3, I understood that the objective is: given a hypothesis h = (c,u,r) to derive \psi (or \mathcal{V}_D). I would kindly ask the authors to define concretely the problem they are dealing with, addressing all my comments from above, as now it is difficult for the reader to understand what is happening. 
- In line 293, the authors talk about hypothesis semantic trees, giving an example in Figure 1. However, in line 152, the hypothesis is a ternary tuple. 
- In line 240, the authors talk about the implementation workflow, however, they give no definition/specification of them in Section 3. 

The above issues, make it difficult for the reader to understand this work and the proposed benchmark. I am willing, however, to increase my score if the authors address my comments/questions.

### Questions
Please read my comments/questions from the above field. In addition: 

- One suggestion that I have for the authors is to start with the example given in lines 247 and show how G, h, \psi, c, u, r, and \mathcal{V}_D look like for this example. 
- Please clarify whether a hypothesis is represented as a sentence, a semantic tree, or a ternary tuple, and to explain how these different representations relate to each other if multiple are used.
- Please define the space of valid verification procedures V_D and clarify whether finding V_D itself is part of the task or if it's given. 
- Another suggestion that I have for the authors is to look into automated theorem proving, (e.g., “Handbook of Automated Reasoning”, Volume 1, 2001), where the notions of hypotheses, theorem proving, proof trees, are formally defined. I would suggest using this notation to formally define the data-driven discovery task. I believe that this work will benefit a lot from a more rigorous formulation, e.g., to my understanding, the elements in \mathcal{V}_D map to proof trees.

### Soundness
2

### Presentation
2

### Contribution
3
