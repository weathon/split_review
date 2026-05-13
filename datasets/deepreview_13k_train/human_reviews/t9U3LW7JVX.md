# Automated Design of Agentic Systems

- Decision: Accept
- Scores: 10, 8, 3, 3

## Abstract
Researchers are investing substantial effort in developing powerful general-purpose agents, wherein Foundation Models are used as modules within \emph{agentic systems} (e.g. Chain-of-Thought, Self-Reflection, Toolformer).
However, the history of machine learning teaches us that hand-designed solutions are eventually replaced by learned solutions.
We formulate a new research area, \textbf{A}utomated \textbf{D}esign of \textbf{A}gentic \textbf{S}ystems (\textbf{\problem}), which aims to \emph{automatically create powerful agentic system designs, including inventing novel building blocks and/or combining them in new ways.}
We further demonstrate that there is an unexplored yet promising approach within \problem where agents can be defined in code and new agents can be automatically discovered by a meta agent programming ever better ones in code.
Given that programming languages are Turing Complete, this approach theoretically enables the learning of \emph{any possible} agentic system: including novel prompts, tool use, control flows, and combinations thereof.
We present a simple yet effective algorithm named \ouralgo to demonstrate this idea, where a meta agent iteratively programs interesting new agents based on an ever-growing archive of previous discoveries.
Through extensive experiments across multiple domains including coding, science, and math, we show that our algorithm can progressively invent agents with novel designs that greatly outperform state-of-the-art hand-designed agents.
Importantly, we consistently observe the surprising result that agents invented by \ouralgo maintain superior performance even when transferred across domains and models, demonstrating their robustness and generality. Provided we develop it safely, our work illustrates the potential of an exciting new research direction toward automatically designing ever-more powerful agentic systems to benefit humanity.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
In the style of neural architecture search, the authors argue that the design of agentic systems can be automated and provide a system that is a step toward solving that problem. They show that their system can achieve strong performance on several benchmarks compared to hand-designed systems.

### Strengths
- The work is decently well presented and does read like a paper one would expect to see at ICLR.
- The topic is relevant, the paper is timely, and the results are somewhat strong.
- I can see this naturally integrating with work trying to design better evaluators (LLM-as-a-Judge, Agent-as-a-Judge, etc.).

### Weaknesses
 - My most serious concern lies with the novelty of this work. There are papers like Voyager out there which incrementally build up sets of tools for solving a specific task. Is this actually fundamentally different from such code-generating systems? Or just a new paint job?
- The authors keep citing the Turing Complete nature of their proposal. Most things in AI are, in one way or another, Turing Complete, so I wonder if that is really a big deal here. Like everything else here, the Turing Completeness of their system is wholly dependent on the components of the actual system (here, whether the LLMs actually act as Turing Complete systems in practice).
- From the main text, it is quite unclear how their proposed system works exactly. Is it just a trivial loop writing a basic program?
- I think you want to cite "The Bitter Lesson" alongside Clune in Line 50. It's more disconnected from the other works this one cites, so it is a bit less biased. While a blog post, it predates the cited work from Clune here and was quite influential. I'm sure there's earlier stuff that's good to cite here, too (this is one of the core motivations of this work, so it's worth fleshing out).
- I like the presence of the research question on lines 88-89. But given that it's so important to the text, maybe polish it a bit by refining it (maybe just drop everything from "rather" onwards).
- When bolding results, you need to bold everything that has overlapping error bars. Statistically, the results probably wouldn't pass a t-test and that's normal in the field, but we still can't get away with totally ignore statistics.

### Questions
Please respond to the above when possible as well.

- What exactly is the flowchart for the system here? It would be good to see something like that covering all the details in Section 3 (something more detailed than Figure 1).
- Do LLMs act as Turing Complete systems?
- What is and isn't hand-engineered here? Maybe use Figure 3(b) to explain.
- The system seems to build itself up bit by bit. This isn't exactly a nice optimization space, though, so how do you counteract local minima? Neural architecture search has quite a bit of focus on this (even the original NEAT is mainly focused on this).
- Can you clarify why you are using grids to sample in line 267?
- Can you compare this with Voyager? I'd like to see something differentiating it from generic code-generation tasks here.
- It's maybe a bit of an unfair comparison but did you compare against a vanilla GPT-o1 (I don't view this is required here)?

If the other reviewers bring up no serious issues, I can see myself changing my score if you can address most of the above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a new research area called Automated Design of Agentic Systems (ADAS), aiming to automate the creation of powerful agentic systems by inventing novel building blocks and combining them in innovative ways. The authors propose an approach where agents are defined in code, allowing a meta-agent to program new agents iteratively. They present an algorithm called Meta Agent Search, where a meta-agent utilizes Foundation Models (FMs) to generate, evaluate, and improve agent designs based on an ever-growing archive of previous discoveries. Through extensive experiments across multiple domains—including logic puzzles, reading comprehension, mathematics, and science—they demonstrate that agents discovered by Meta Agent Search outperform state-of-the-art hand-designed agents. Moreover, these agents show strong generalization capabilities when transferred across different domains and models.

### Strengths
1. The introduction of ADAS as a research area is novel, and framing the agent design problem as code generation by a meta-agent is a creative approach.
2. The Meta Agent Search algorithm is well-conceived, and the experimental results are robust, showing consistent improvements over existing methods.
3. The paper clearly articulates the motivation, methodology, and implications of the work, making it accessible to readers.
4. Automating agent design has the potential to accelerate AI development significantly, and the demonstrated generalization capabilities suggest wide applicability.

### Weaknesses
1. While the paper mentions safety concerns, a more in-depth analysis of potential risks and mitigation strategies associated with ADAS would be beneficial.
2. A deeper discussion on why certain baselines were chosen and how they were implemented would strengthen the evaluation.

### Questions
1. How does Meta Agent Search address potential biases or unsafe behaviors that might emerge from automatically generated agents? Are there mechanisms in place to detect and mitigate these issues?
2. How does the approach scale with more complex tasks or larger domains? Are there computational limitations that need to be considered?
3. Could the authors elaborate on how higher-order ADAS (e.g., improving the meta-agent itself) might be achieved and what challenges are anticipated in that direction?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes an approach that automatically searches building blocks and combinations of them as code generation for the Automated Design of Agentic Systems. Meta Agent Search, an iterative optimization method with foundation models generating new agents, is presented. The experiment shows that the Meta Agent Search is capable of inventing novel designs of agents. It is claimed that Meta Agent Search consistently outperforms state-of-the-art hand-designed agents in various domains. The optimized agents are shown to be transferable to different domains and foundation models.

### Strengths
1. The work is well-motivated.
2. The transferability results are interesting.

### Weaknesses
 1. Some of the sentences are not written with care. For example, "Given that programming languages are Turing Complete...". The fact is that some programming languages are not Turning complete. This is awarded by the authors on line 106.
2. It should be stated in the main text that the implementation of the meta optimizers is different for different tasks.
3. As an optimization method, it is only compared with handcrafted baselines. More comparison with other optimization methods is expected.
4. I think there are missing citations for self-referential higher-order meta-learning. See Schmidhuber. Evolutionary principles in self-referential learning, or on learning how to learn: The meta-meta-... hook. Diploma thesis, Institut für Informatik, Technische Universität München, 1987 and its follow-up works.
5. I think there is a lack of explanation of how the work illustrates the potential of this direction to benefit humanity, which is claimed in the abstract. 
6. The optimization starts with the baseline method as the initial solution. For a fair comparison, I think the optimization result starting without any manually optimized initial solution should be presented.

### Questions
1. How should I interpret the legend "E.g. LLM defines agents using code" in the search algorithm box of Figure 2?
2. What is "the framework" on line 265 referring to?
3. What is the motivation for reporting the median accuracy instead of the mean? Is this a common practice? Could you also so the mean?
4. The paper states that the method is compared with five state-of-the-art baselines, namely COT, COT-SC, Self-Refine, LLM-Debate, and Quality-Diversity. Could you elaborate in what sense they are state-of-the-art? Are they the best-performed known method for at least one of the tasks being tested? To my knowledge, the best handcrafted solution of ARC achieves at least 20% accuracy (see the reference below). Please specify the scope of your baselines.

Ferré, S. (2021). First steps of an approach to the arc challenge based on descriptive grid models and the minimum description length principle. arXiv preprint arXiv:2112.00848.

5. How exactly is the meta agent implemented? Is it a single query of an LLM with a handcrafted template presented in Appendix C?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Through this paper the authors propose to "form" a new research area they call "Automated Design of Agentic Systems", in which the high level general idea is to automate the generation of "new agents" (in this case the word agent is loosely used for a piece of code, apparently), that are continuously evolved.

### Strengths
- Thought-inducing subject, as the authors propose to work on "agent-generating agents".
- Contemporary work, following the trend of developing approaches to improve inference once the LLM is already trained, which makes it of interest to a good portion of the community.

### Weaknesses
 - The biggest and greatest critique to this paper is that on the high level the authors are proposing to create a sub-community dedicated to exploring what could be seen as a primitive form of self-replication. Given that in practice the proposed method is pretty much just a code generator (easy to isolate and secure by making the code run in a Domain Specific Language), I won't reject or reduce the score of the paper due to this point, but I urge the authors to reflect on whether if push for the development of such general "Agent generation procedures" is really a good idea. Conceptually speaking, it's not a big jump to go from an agent that generates code that generates other agents, to a robot that builds other robots.

- Related to the first matter, such a research should have safety as a cornerstone of the design, with clear descriptions of how to make the agent generation safe. However, the only mention of "safety" throughout the paper is pretty much the discussion on section 6, that only talks about the "danger of creating AGI" (which in my opinion is totally eclipsed by the danger of self-replication in the case of this paper), and to which the author's only response is to push to future works to think of safety, which in my opinion is completely inappropriate. Every single building block of the algorithm should have been thought of in terms of safety and clear recommendations to avoid dangers should have been given.

- The practical description of the method is very unclear and far too high-level in the main text. I cannot understand from the description exactly what type of code is generated and what are the building blocks that are given as prior to the agent. The expanded analysis of the related works should have been moved to the appendix to make room for a better explanation of the method. Overall, it seems like the authors' approach would require a lot of compute AFTER a lot of compute has already been dedicated to train the LLM, yet, the computational cost addition to the inference was not compared to the other, clearly less-computationally expensive, approaches such as chain of thought in table 1. The method has very limited applicability if it clearly cannot be applied to hundreds of billions of parameters even if you have the supercomputers for that.

- The author statement "community has not reached a consensus on the definitions or terminologies of agents" is at the very least a weird one. Certain communities have been working on agents since the 80s and while there is always space to argue about certain gray areas of the definition, textbooks used to teach undergrad students already have a pretty decent definition for "agents", for example AI a modern approach. The authors seem to be too focused in the LLM subcommunity and disregarding past work and definitions that are relevant to the work they are trying to develop.

- Unless the authors are part of openAI I suggest against using their logo in figure 2.

- Despite being at some extent intriguing to think about some aspects of the authors' work, in my opinion the work is not very technically mature, with relatively simple and overly high level descriptions, and very limited experimentation. In my judgement this paper is more suited to an ICLR workshop.

### Questions
no specific question.

### Soundness
2

### Presentation
2

### Contribution
1
