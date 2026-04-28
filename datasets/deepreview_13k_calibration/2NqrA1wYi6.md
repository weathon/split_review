# Unraveling the Complexity of Memory in RL Agents: an Approach for Classification and Evaluation

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
The incorporation of memory into agents is essential for numerous tasks within the domain of Reinforcement Learning (RL). In particular, memory is paramount for tasks that require the utilization of past information, adaptation to novel environments, and improved sample efficiency. However, the term ``memory'' encompasses a wide range of concepts, which, coupled with the lack of a unified methodology for validating an agent's memory, leads to erroneous judgments about agents' memory capabilities and prevents objective comparison with other memory-enhanced agents. 
This paper aims to streamline the concept of memory \new{in RL} by providing \new{practical} precise definitions of agent memory types, such as long-term versus short-term memory and declarative versus procedural memory, inspired by cognitive science. 
Using these definitions, we categorize different classes of agent memory, propose a robust experimental methodology for evaluating the memory capabilities of RL agents, and standardize evaluations. 
Furthermore, we empirically demonstrate the importance of adhering to the proposed methodology when evaluating different types of agent memory by conducting experiments with different RL agents and what its violation leads to.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This is a sort of conceptual paper, it's main concern is to taxonomize the concept of memory in reinforcement learning. Given the taxonomy, it aims to demonstrate why paying attention to the categories it suggests is important for interpreting the results of experiments on RL agents involving memory.

### Strengths
I'm generally favorably disposed toward conceptual papers like this. And I do agree with the authors that their target, memory in RL, is a worthy target for such an effort.

The main distinction is between declarative and procedural first, and then short-term versus long-term second. The latter is defined with respect to a context length parameter. I do think it's a good idea to highlight somehow the difference between associations within the context window and outside of it. This is a very relevant difference with many algorithmic implications.

### Weaknesses
 - This is trying to be a conceptual paper aimed squarely in the intersection between AI and cognitive /neuro science. However, judged in that way, I don’t think it really makes the grade. The problem is that it doesn’t really connect clearly into the conversation on the cognitive / neuro science side. There are very few references to these disciplines for one, or less than I would expect any way. And critical references for multiple memory systems are missing (there are so many, but I like some of Squire's old papers on the topic).  And there is basically no context in the paper connecting the work to the ways that researchers in these other fields have thought about memory. For a paper like this which purports to offer a formalization of what is meant by ‘memory’, it's clearly important to relate the new formalization to old ones and discuss how they are similar and different, and to try to sustain an argument for why the present one is an advance on the old.

- I’m not buying the claim that RL is capturing declarative memory. I would tend to say that a defining feature of declarative memory as opposed to procedural memory is the declarative memory’s arbitrariness. The classic prototype example of a declarative memory is a person’s name. And most definitions you find look something like "declarative memory is defined as the type of memory that involves consciously recalling facts and events". It’s all very language-like. But RL memories aren’t usually like that. In some cases they may be, but it’s not too common memory in RL outside of language data. I would probably have been more forgiving of this claim to capture declarative memory with RL had come a few years ago, but now that we have LLMs, what’s the point in trying to get all bent out of shape to capture declarative memory in RL? The prototype of declarative memory is arbitrary information conveyed by language e.g. “My teacher’s name is Bob” (episodic flavor) or “Paris is the capital of France” (semantic flavor). So it seems very reasonable to expect a model of declarative memory to use the kinds of AI systems that work for that kind of data, now that they exist and are so widespread. And of course there are plenty of ways to combine RL and LLMs. I understand though that that would take this too far afield for the present work. And this isn’t really a computational neuroscience modeling paper. So this isn’t really a weakness of the paper here. No need to reply to this bullet point since I don’t think it really matters for your paper. But I’m just leaving it here as a way to convey a bit more my mindset with regard to this paper. At very least, the arbitrariness of the associations seems like a critical part of declarative memory.

- Right after positing a difference between declarative and procedural memory in terms of the algorithms that implement them, in the very next paragraph it then acts like this distinction is established and ready to support further claims when it says “many studies fail to differentiate between agents with declarative and procedural memory”. But that’s  not a strong argument given that it just followed right after defining these terms. Why should other papers have tried to probe things according to the arbitrary categories you just defined?  Especially since, I suspect many researchers would not necessarily agree with the classification. At any rate, the paper merely asserts that one set of tasks are declarative and another are procedural, but it offers no evidence that this distinction corresponds to what others mean by those terms.

- Definition 3 says one should call RL problems involving a “single environment”  problems of declarative memory and RL problems featuring multiple environments problems of procedural memory. This definition would be  impossible to apply in practice. It would appear to suggest that all memory is declarative since one can always compose “multiple environments” together into a single meta-environment. The difference between one environment or many environments is not in the task itself, it’s just a purely formal aspect of the modeling language. One generally is not supposed to predicate a general definition on such a purely formal property since it would make your classifications float around following specific and contingent task parameterization properties.  Note: all the same comments also apply to the episode concept too.

### Questions
1. In this paper, is memory meant to be a problem or a solution?

2. Is there some kind of Marr-Poggio levels of analysis story that could be used to clarify the overall structure of the argument here?

3. Doesn't this taxonomy seem to bundle together too many things that really are not similar? Replay buffers used just for training and dynamically accessed external memories, used at test time, are quite different algorithmically, and used in quite different ways. Why does this classification scheme seem to drop these in the same bucket? (There is text in the appendix suggesting this). Also, I don't see why it's even true according to the definition in the main text. I would think that definition would separate these approaches.  And that would. be kind of the whole point of separating declarative and procedural memory. Why doesn't it separate them in the appendix anymore?

4. The paper includes the following sentence in the results section “This ambiguity arose because the first experiment did not follow our proposed methodology”, well this certainly doesn’t inspire any confidence. Why talk about an experiment that doesn’t fit the proposed methodology? It's likely I've misunderstood this paragraph. I find it very hard to follow this part.

5. How would you think about an RL model that remembers and reproduces a time interval? E.g. [Deverett, B., et al. (2019). Interval timing in deep reinforcement learning agents. NeurIPS.]  That paper showed that purely feedforward agents can sometimes solve what appear to be memory tasks. Does that matter? How would your definitions classify the feedforward agent in that paper?

### Soundness
2

### Presentation
2

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
The paper attempts to create clarity in the use of the term "memory" in a reinforcement learning context.  As well as suggesting definitions for different kinds of memory and different memory related tasks, the authors present a more rigorous way for testing memory capabilities of reinforcement learning techniques and show possible pitfalls of violating the proposed methodology.

### Strengths
I really like the paper and the topic it presents.  I think it is good to have a more clear definition of what exactly is meant by memory and what its contribution can be in reinforcement learning.  I like the approach the authors came up with and the clarity with which they presented it.  I think there is a need for a paper like this, and I like how the authors looked at the current state of affairs in reinforcement learning research and its treatment of a new and important branch in the field that deals with memory in a bunch of different contexts.

### Weaknesses
However, the topic seems difficult to deal with in a conference paper.  When reading the introduction and the goal of the paper as set out, I was expecting a more broad overview of current use of the memory term and the different ways it is used and abused in reinforcement learning literature and research.  I think the topic is very interesting, but a paper doing a deep dive into a topic such as this has to build a clear foundation for its contributions by taking the body of existing work into account (To be clear, I am not suggesting that the authors don't do this.) and illustrating this by giving a broad overview of said existing work in the paper.  

In my view, this contribution wants to be presented in a review paper, with an overview of recent existing work laying a strong foundation for the contributions made by the authors, namely, bringing clarity to the current mismatch in use of the term "memory" in the field.  

Currently, the paper includes a very brief section on POMDPs, which are important, but don't represent all ways in which the term memory is used.  However, since this is section 2, I think this is a bit misleading, as it seem to set the context in full.  The related works section is very brief, and much related work is relegated to the appendix, where most of it is only referenced, but not placed in context of the suggested structure and definitions.  Section 4 lays some foundation from cognitive science and RL, and talks about the credit assignment problem in relation to memory handling, but it feels rushed and the role or importance it plays isn't obvious.  All of this should be given more room to be elaborated on.  I understand that this is impossible in a conference paper however, but now it feels rushed, and I don't feel the work will get the attention it deserves or reach the audience that it should.

### Questions
This is where double blind reviewing sucks, as I would strongly recommend that the authors produce the review paper, with additional contribution this paper could be, and I would happily serve as a reviewer for said paper.

### Soundness
3

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
3

### Summary
The paper introduces an approach inspired by human cognitive abilities to formalise memory types in reinforcement learning (RL), providing precise definitions for short-term memory (STM) and long-term memory (LTM). STM is defined as the agent's reliance on recent interactions, while LTM involves recalling information over longer time intervals outside of the immediate context. The authors differentiate between Meta-Reinforcement Learning (Meta-RL), which focuses on cross-task skill transfer (procedural memory), and Memory Decision-Making (Memory DM), where agents use historical data within a single environment (declarative memory).

In the Memory DM setting, the authors develop a rigorous evaluation methodology to assess memory capabilities in RL agents. This approach is validated in memory-intensive environments, such as the Passive T-Maze and Minigrid-Memory, by varying critical parameters—context length (the memory span an agent can handle) and correlation horizon (the temporal dependency between events). By varying key parameters, the experiments demonstrate the Memory DM framework’s ability to reliably assess STM and LTM in RL agents.

### Strengths
* The paper provides neuroscience-based definitions of memory types, clarifying RL memory research, which enables more accurate agent comparisons and tailored evaluation methods for each type​. The cognitive science-inspired approach has interdisciplinary appeal, likely to attract interest from both RL and cognitive science researchers, fostering potential collaboration and cross-disciplinary insights.
* The paper’s methodology is grounded in theoretical rigour, offering a scientifically robust framework that enhances the validity and reliability of memory evaluation in RL studies.
* It introduces a standardised methodology for assessing memory capabilities, promoting reproducibility and consistency across RL studies by providing clear criteria for experimental setups.

### Weaknesses
 * The framework has been validated in simple environments, which may not capture the challenges of more sophisticated settings or real-world scenarios, potentially limiting its practical applicability.
* The paper discusses procedural memory as part of its classification scheme but does not provide or suggest an evaluation methodology related to it, focusing solely on declarative memory. This results in an incomplete validation and leaves open questions about the classification’s practical application to skill-transfer scenarios.
* The methodology section is dense and complex, additional visual aids or examples could clarify the experimental design and enhance comprehension for a broader audience.

### Questions
* Could the framework be extended to evaluate procedural memory in Meta-RL settings? Are there specific experiments that could be added to address skill transfer across tasks?
* In my interpretation, declarative and procedural memory are intended as distinct concepts; however, the definitions in Equation 2 of Definition 3 imply that declarative memory could be included within procedural memory due to the “or” condition and “≥” allow for overlap. Could the authors clarify whether declarative memory is meant to be a subset of procedural memory or fully distinct? How does this impact the proposed distinction between Memory DM and Meta-RL in the framework?
* How does this framework compare to existing memory evaluation approaches in RL? What are the specific advantages of using cognitive science-inspired definitions over more traditional RL memory metrics?
* What motivates the specific classification of memory types (declarative vs. procedural, STM vs. LTM), and how does it improve memory assessment in RL over a general approach?

### Soundness
3

### Presentation
2

### Contribution
2
