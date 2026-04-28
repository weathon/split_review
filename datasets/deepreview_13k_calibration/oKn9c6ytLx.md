# WebArena: A Realistic Web Environment for Building Autonomous Agents

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
With advances in generative AI, there is now potential for autonomous agents to manage daily tasks via natural language commands. However, current agents are primarily created and tested in simplified synthetic environments, leading to a disconnect with real-world scenarios.
In this paper, we build an environment for language-guided agents that is \emph{highly realistic} and \emph{reproducible}.
Specifically, we focus on agents that perform tasks on the web, and create an environment with fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management.
Our environment is enriched with tools~(\eg a map) and external knowledge bases~(\eg user manuals) to encourage human-like task-solving.
Building upon our environment, we release a set of benchmark tasks focusing on evaluating the \emph{functional correctness} of task completions.
The tasks in our benchmark are diverse, long-horizon, and designed to emulate tasks that humans routinely perform on the internet.
We experiment with several baseline agents, integrating recent techniques such as reasoning before acting. 
The results demonstrate that solving complex tasks is challenging: our best \textsc{GPT-4}-based agent only achieves an end-to-end task success rate of 14.41\%, significantly lower than the human performance of 78.24\%.
These results highlight the need for further development of robust agents, that current state-of-the-art large language models are far from perfect performance in these real-life tasks, and that \ours can be used to measure such progress.%\footnote{Code, data, environment setup, and video demonstrations are available in the supplementary material.}

Our code, data, environment reproduction resources, and video demonstrations are publicly available at \url{https://webarena.dev/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper emphasizes the potential of generative AI in creating autonomous agents that can handle daily tasks using natural language commands. Recognizing the limitations of current synthetic environments, the authors introduce "WebArena," a realistic and reproducible web environment. This environment hosts websites from four key domains: e-commerce, social forums, collaborative software development, and content management, and is equipped with tools and knowledge bases to support human-like task performance. The authors also provide a benchmark of diverse tasks that mimic human internet activities and prioritize evaluating functional correctness over mere textual similarity. Testing with agents, including a GPT-4-based one, showed a significant performance gap, with the agent achieving only a 14.41% success rate compared to humans at 78.24%. This underscores the need for enhanced agent development and the value of WebArena as a testing ground for future advancements.

### Strengths
**Originality**: I am truly delighted to have the opportunity to review this work. I had the privilege of reading this manuscript a few months ago, and its significance resonated with me. The issues addressed in this paper are both critical and captivating. The work notably bridges a substantial gap, laying a pivotal foundation for future industrial applications of web agents. Over the last six months, I've come across numerous works on agent benchmarks. However, this particular study stands out, primarily due to its compelling motivation and remarkable originality. It has quickly become one of my favored works in this domain.

**Quality**: After personally setting up the environment, running the provided code, and assessing the dataset, I can attest to the high caliber of this work. The construction of the benchmark is solid and robust, testifying to the meticulous efforts behind it.

**Clarity**: The paper is lucidly crafted with a coherent structure and logical flow, making it accessible and comprehensible.

In conclusion, this is a high-quality, original, clear, and significantly impactful piece of scholarship.

### Weaknesses
While the work presented is undeniably valuable, from an academic perspective, I believe there are several weaknesses, primarily related to experimental evaluations and the choice of baselines. Here are the specific areas of concern:

1.  **Lack of Evaluation with the Latest Intelligent Agents**: 

The paper seems to miss out on evaluating some of the latest intelligent agents, especially those grounded in modern reasoning and planning methods. Works like the "Tree of Thought" and the new "Reflection" architecture have been in the public domain for a while. It would have greatly enhanced the paper's comprehensiveness if these contemporary agents were included in the evaluations. Specifically, the absence of agents employing iterative refinement strategies, which have shown promise in complex tasks, is a notable gap. These methods often involve a cycle of planning, execution, and reflection, which could be particularly relevant in the multi-step web navigation scenarios presented in the benchmark.

2.  **API Call Methodology and Ablation Experiments**: 

The manner in which API calls are presented in the paper, particularly as web pages, does not seem to align with the current prevalent paradigms where APIs are usually invoked within context. It raises the question of whether an agent can effectively utilize this format. Additionally, it would have been illuminating if the authors had included ablation studies in their experiments. Specifically, it would be insightful to discern the efficacy of these tools and whether they genuinely aid the agent in realizing the desired goal of "encouraging human-like task-solving". For example, an ablation study could examine performance with and without the tool websites, or with different levels of tool access, to quantify their impact.

3.  **Html or Accessibility Tree?** 
   - Many language models (LLMs) are pre-trained with an abundance of HTML content, but they might not necessarily contain the Accessibility tree. Hence, it might be more natural for these LLMs to understand and parse HTML.
   - Both DOM and the Accessibility tree adopt a tree-like structure. The seemingly "redundant" symbols in HTML could potentially assist LLMs in better understanding the hierarchical nature of the content.
   - It is vital to conduct empirical tests to validate the advantages of either approach. Given that the Accessibility tree is not commonly adopted in other benchmarks, using it here could also be viewed as one of the paper's core contributions, setting it apart from the current landscape of research in this area. It would be beneficial to see a more thorough investigation into why the accessibility tree was chosen over HTML, supported by empirical evidence.

4.  **Gold Trajectories**: 

The paper would benefit significantly from the inclusion of "Gold" trajectories. These trajectories can offer a benchmark for the best possible action sequences, making them an invaluable asset for future research in this domain. The absence of these trajectories is a noticeable gap in the paper. These trajectories would not only serve as a performance ceiling but also provide a means to analyze the efficiency of different agent strategies.

5.  **Evaluator Demographics**: The choice of computer science graduate students as evaluators raises certain concerns regarding the generalizability of the results.
   - Computer science graduate students typically possess an advanced understanding of web page interactions, which might not be representative of the average user. Their performance might be notably better than what we'd observe with a more diverse group, especially when considering common tasks like online shopping that even non-technical users frequently engage in.
   - Furthermore, it's essential to address potential biases that might arise if any of the evaluators were involved in the dataset's creation. This could compromise the validity of the scores. From a personal standpoint, I, along with several colleagues, have engaged in case studies with this dataset. Interestingly, our accuracy rates didn't match the high scores reported in the paper, which adds a touch of humor to this serious concern.

To ensure the paper's robustness and generalizability, it's crucial to address these points, preferably with empirical evidence and further discussions.

### Questions
See the weaknesses above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new, realistic RL envionrment for Web tasks named WebArena as well as a first evaluation of GPT-based agents performing the defined tasks. The framework includes environments for e-commerce, social forums, collaborative software development similar to Gitlab and content management and therefore provides additional tools, including maps or Wikis. The obervation space can be screenshots of web pages, HTML DOM trees or accessibility trees. The authors proposes a Partially Observable Markov Decision Process modelling of tasks, where the action space comprises keyboard and mouse. The authors present 812 tasks in their benchmark and evaluate GPT-based agents for the tasks, which yield sub-par performance against human baselines from a user study.

### Strengths
The authors propose an Independent platform, implementing a large variety of realistic end-user tasks on the Web. The framework provides provides realistical, challenging tasks for Web agents. The quality of the benchmark is sufficiently high. To this end, a good choice of task variety was made, which is backed up by a user study. This is very nice to see, as the taken design decisions then are probabily matching with user needs.  

The paper includes a preliminary evaluation of agents based on closed-source LLMs (ChatGPT / Text-Bison), which gives first insights.

The code is made available for review, and is usable and documented, which makes the paper's contributions quite clear. The available tasks are sufficiently challenging for evaluating (LLM) agents, which makes the contributions significant for more research advances in the field.

While there are other related benchmarks in the field, it is quite clear from the paper content what is being improved / what is original.

### Weaknesses
 The related work advantage not completely clear. The related work states functional correctness as advantage over AndroidEnv, but no further explanation is given. It might hint to the diffeence between the used evaluation metrics, but it would be interesting/important to clarify this. Also, it mentions the lack of diverse or complex task availability, but new tasks can be defined within the framework.  

The agent evaluation is performaned with standard GPT variants only, not pointing to stronger alternatives. Also, little to no details about how the agent was implemented/tested are given in the main paper. Only the appendix shows examples, which impedes understanding the paper.

As the used LLMs for the evaluation are closed-source, this impedes reproduciability. As the evaluation can been seen as first validation of the benchmark, this might still be fine, but it would be good to have open-source agents integrated.

Lastly, the POMDP model is not argued for in the paper, but it would be important to justify the modelling choice. This is not to say that a POMDP model is not sensible.

### Questions
Can new tasks be easily added to the benchmark within the available environments?

Would it it have been possible to include the benchmark tasks into another, existing benchmark system from the related work?

What could be future works wrt to (RL-) agents for solving the benchmark tasks? 

Are the presented tasks on par wrt difficulty or even superior to other benchmarks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a web environment designed for the development and testing of autonomous agents. The proposed environment WebArena includes fully functional web applications and genuine data from four major categories, providing a realistic platform for agent interaction. The authors also proposes a benchmark consisting of 812 examples, as well as an evaluation method. The experiments show that GPT-4 only achieves a task success rate of 14.41%, which is much lower than human performance of 78.24%.

### Strengths
1. This paper proposes a highly-realistic and complicated web environment compared with the previous simplified environment;

2. The proposed environment includes four common and real domains;

3. The paper is well written and easy to follow.

### Weaknesses
1. The major weakness of this paper is the lack of technical novelty. Though the contribution on simulated environment/datasets/resources are welcomed and very important to the research community, such papers may not match the general style of ICLR papers.

2. For evaluation, the proposed framework uses GPT4 to evaluate the answer or the execution paths, which potentially has two issues: 1. GPT4 is a commercial tool, which may limit the potential use of this environment; 2. GPT4 is not guaranteed to be 100% right, which may make the evaluation results not convincing.

3. The success rate of human on the designed tasks are only 78%, which is a little surprising since it seems that these tasks are not that difficult for human to complete. It is better that the authors provide more analysis on these tasks and evaluations to show that why human fails and if these tasks are too difficult for agents.

### Questions
1. Is there any analysis or discussion on the performance of GPT4 evaluation?

2. Why the success rate of human is only 78%?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
