# Boundless Socratic Learning

- Decision: Reject
- Scores: 3, 3, 6, 5, 3

## Abstract
An agent trained within a closed system can master any desired capability, as long as the following three conditions hold: (a) it receives sufficiently informative and aligned feedback, (b) its coverage of experience/data is broad enough, and (c) it has sufficient capacity and resource. In this position paper, we justify these conditions, and consider what limitations arise from (a) and (b) in closed systems, when assuming that (c) is not a bottleneck. Considering the special case of agents with matching input and output spaces (namely, language), we argue that such pure recursive self-improvement, dubbed "*Socratic learning*", can boost performance vastly beyond what is present in its initial data or knowledge, and is only limited by time, as well as gradual misalignment concerns. Furthermore, we propose a constructive framework to implement it, based on the notion of *language games*.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper explores the concept of Socratic learning, a recursive self-improvement process in the context of language model.  Central to this approach is the framework of language games, derived from Wittgenstein's philosophy, which facilitate interactive data generation and provide feedback mechanisms through scoring. The paper seems more proper to a philosophical or language conference, as the current manuscript consists no quantitive evaluation or concrete algorithm presentation, as noted by the authors.

### Strengths
Idea is somewhat interesting by drawing connection of learning and philosophical concepts.

### Weaknesses
1. No concrete algorithm for the proposed framework;
2. No quantitive evaluation of the proposed framework

### Questions
How would the proposed framework and language game cope with any existing language model (e.g., llama, ChatGPT)? Can the authors perform some prototyping and validation of the proposed framework?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This is a position paper that argues for open-ended learning in `a closed system' based on the framework of 'language games.' 
The agent interacts with itself using natural language inputs and outputs like a group of Socratic philosophers talking to themselves. The question raised is if this kind of interaction can result in self-improvement ultimately leading to 'artificial super intelligence.'

### Strengths
This is a thought-provoking position paper and not a technical paper. It raises some interesting questions and makes connection to frameworks such as reinforcement learning and language games. The idea of reaching super-human intelligence through self-improvement is a tantalizing goal, but leads to many questions I outline in the next section.

### Weaknesses
Unfortunately the claims of the paper are not compelling. I could appreciate the analogy to reinforcement learning, where the agent is trying to optimize a given reward function. However in the absence of such as a known reward function or human feedback, it is unclear how the "self-improvement" is supposed to occur.

"External to the system is an observer whose purpose is to assess the performance of the agent"

However, if the agent is oblivious to this performance assessment, how does it help the agent improve it? If the agent does receive feedback and adapt itself to improve its performance, this seems identical to RL with human feedback.

The idea of language games is an old one, but again it is not clear what the goal of such a game is supposed to be, and what guarantees 'alignment' of meaning or purpose with humans. Communication between people (and philosophers) is possible due to shared meaning, shared life experiences, and shared culture.  Not sure how a pure language model that interacts with itself can improve itself.

Some concrete examples of the concepts put forth here would have been more useful.

Consider for example a mathematical language like first order calculus. A theorem prover might start with something like  Peano axioms and derive a lot of new facts about integers. Or someone can axiomatize chess and derive some interesting consequences. Does it qualify as an example of what you have in mind? These systems have some inherent limitations in that what they can learn is limited to what follows from the axioms. Further, it is known that the proof systems are incomplete and intractable even in the simplest of cases.  

In summary, this is a thought-provoking position paper. Despite the authors' attempts to clarify their paper and answer the reviewers' probing questions, I remain unconvinced about the novelty and significance of the arguments.

### Questions
Please give some concrete examples of the framework you have in mind. Argue how such a system can be constrained to reach a desirable goal or if it is open-ended how it can be guaranteed to be safe.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The article discusses a type of learning in which the learning agent is self-reflective, rather than relying on external data and knowledge inputs to improve itself, as is typical of most existing learning agents. In fact, even the most advanced large language models (LLMs) today strengthen their capabilities through data-driven training and human feedback. However, the author suggests an alternative: a learning agent that is capable of introspective or self-improving learning within a closed environment—improving itself without external inputs. This self-contained learning, termed “Socratic learning,” is feasible if the environment meets three conditions: (a) sufficiently informative and aligned feedback, (b) broad coverage of experience or data, and (c) adequate capacity and resources, the latter of which the author believes is only a matter of time.

The author presents a unique framework called “language games” as an implementation example to support Socratic learning, explaining how multi-player dynamics and the design of language games into many narrow but well-defined language games—rather than a single, universal one—may satisfy the requirement for broad coverage. Additionally, features like a meta critic could make these language games scalable. The author also suggests feasible approaches to ensure feedback consistency.

### Strengths
The article takes a higher-level view of today’s artificial intelligence, introducing "Socratic learning" as a potential path toward AGI and offering an implementation framework for realizing Socratic learning. The ideas presented are thought-provoking and stimulate valuable reflection.

### Weaknesses
This article is intended to be a thought-provoking piece, aimed at stimulating reflection and discussion. Since this is a conceptual position, its suitability for a technical conference like ICLR may require further evaluation.

As a reviewer, I have one observation. If I’ve understood correctly, Socratic learning presupposes that the game’s agent/player is already somewhat intelligent, meaning it can independently derive insights, learn from experiences, and comprehend new knowledge without external input. However, today’s agents, even the most advanced LLMs, lack true intelligence; they generate responses probabilistically rather than through logical understanding. Therefore, should the design of an intelligent agent itself also be considered a prerequisite for Socratic learning?

### Questions
As a reviewer, I have one observation. If I’ve understood correctly, Socratic learning presupposes that the game’s agent/player is already somewhat intelligent, meaning it can independently derive insights, learn from experiences, and comprehend new knowledge without external input. However, today’s agents, even the most advanced LLMs, lack true intelligence; they generate responses probabilistically rather than through logical understanding. Therefore, should the design of an intelligent agent itself also be considered a prerequisite for Socratic learning?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This position paper sets the grounds for discussion around *Socratic learning*, a concept that is used within the paper to describe recursive self-improvement in closed systems and in the language space. First, three necessary conditions for self-improvement to work are described, namely feedback, coverage and scale. The latter is assumed a non-issue in this paper so that it can focus on the other two. Next, the authors provide an explanation of what coverage and feedback conditions mean within the Socratic learning and list some of the limitations they entail for this setting. It is argued that these limitations can be addressed by the language games framework, which can effectively serve as a basis for implementing and applying Socratic learning. Finally, some recursion alternatives for self-improvement are discussed.

### Strengths
The discussion brought forward by this paper is a relevant one: what are the capabilities and limitations of language agents who attempt to self-improve.There is a plethora of recent works that approach this question from a technical perspective by looking at different aspects and applications such as debate or red-teaming. Coming up and proposing a comprehensible and well-structured framework which can be used for discussing this or related questions can be quite beneficial.

The paper reads very well and all its points are made clear. The transitions between the three main sections 3, 4 and 5 helped greatly the flow of the paper which ends up telling a quite coherent story. I believe this part to be particularly important for position papers.

The necessary conditions posed in this paper are something standard in the literature and hold in general for most learning settings including the one considered here. Their incorporation in the Socratic learning setting was interesting and well done, and they also helped motivating in a convincing way the use of language games within this setting. All in all, I found the statements of this paper to be reasonable, well-explained and well-grounded.

### Weaknesses
My main criticism for this paper is two-fold:

**Unclear contributions and insufficient covering of prior work:** The authors state in lines 33-36 that the aim of this paper is not to provide a survey of prior work, which is fair. However, even then I believe that prior/related work has not been sufficiently covered in this paper making its contributions somewhat unclear (at least to me). For example, are definitions in Section 1 all derived from prior work? And if yes where from? If not, which are novel ones and which are not? The only exception to this is recursion which is being covered properly in Section 6 of the paper. Moreover, in Section 7 you mention that all three conditions described in Section 2 are common, but you do not provide any reference in any of the two sections + I would expect this acknowledgement to already come in Section 2. Is this the first work to propose the use of language games for recursive self-improvement or related topics? I strongly believe that the paper would benefit by including a related work section discussing works that have attempted similar discussions and making clear which parts of the paper are novel and to what extent.

**Lack of concrete example:** Even though I enjoyed reading this paper and I found its claims reasonable, I missed a concrete example that connects the described methodology to real-world applications. For instance, you could include any of the recent applications that have an LLM agent self-playing with the goal of improving in some aspect, e.g., negotiation, debate, fact checking, etc.

### Questions
**Q1:** What *compatible* inputs and outputs exactly mean in line 138?

**Q2:** How should Socratic learning and the framework you are proposing be modified when the Observer dynamically changes, instead of being stationary as implicitly assumed by the paper?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper outlines a very broad abstract framework, at a philosophical level, for how self-improving AI without an upper bound in capabilities (i.e., scaling toward superintelligence) could be created. The main restriction of their framework is that of a closed system without input from the outside world. Within the closed system, arbitrary interactions of the agent with the system are possible. Specifically, the authors discuss socratic learning (outputs become future inputs), and specifically language games, where several agents compete against each other to achieve a high score. The authors argue that within this broad framework, recursive self-improvement to superintelligence is in principle possible, and wish to provide a framework of concepts to ground the discussion of other researchers about these topics.

### Strengths
The main strength is that this paper grapples at all with questions of the development of artificial superintelligence and recursive self-improvement, which are severely underdiscussed in the academic literature compared to their importance and plausibility.
I also think it is important to think about the conditions that allow for recursive self-improvement to get a better handle on how things are (or should be) developing, and this paper tries to be a step in this direction.

### Weaknesses
The paper does not propose theoretical or empirical results, and so it is essentially philosophy, and could as such maybe be considered a position paper. (The authors themselves call it a whitepaper). This means that in order to evaluate this work, we need to judge its *thinking* relative to prior work: in what sense does this paper enhance the reader's ability to think clearly about issues of superintelligence and recursive self-improvement, relative to the body of literature that already exists?

Unfortunately, I think this paper is not very grounded in the existing literature (more on that especially in point 2 below), which means I need to evaluate the philosophical thinking in this paper directly. However, when doing this, I immediately start to disagree with aspects of this paper, especially related to the "closedness of the system" that's part of their framework (see point 1 below). In disagreeing, I am myself bound to "philosophize", which means that my review might not appear very grounded in literature either; I hope this is excused given the nature of this paper. Overall, I thus think that while this paper engages with an important topic, it feels not ready for publication.

I recommend the authors to look at the paper [The Alignment Problem from a Deep Learning Perspective](https://openreview.net/forum?id=fh8EYKFKns) for an example of a position paper that was published at ICLR despite being pure philosophy; what made this paper worthwhile is partially that it engaged very extensively with prior work, thus providing a much more stable base for future engagement.

# 1. On Closedness of the system
The authors argue that it is in principle possible to create a recursively self-improving superintelligence in a closed system, i.e., a system that does not interact (via outputs or inputs) with the outside world. Language games are then their main instantiation of this procedure. I disagree with this, for the following reasons:
- Eventually, any true superintelligence will have to act in the real world to create new knowledge, e.g. by steering experiments. This likely requires to already interact with the world in the learning process itself since any closed system we could encode today would miss information about the world that we did not yet discover.
- Likewise, I think alignment (with society/preferences/humans etc.) might be impossible to achieve in a closed system. To solve this, the authors propose to have a meta-critic that evaluates which games should be played to lead to an aligned system; however, no reasons are given for how to design this meta-critic to achieve alignment. The authors seem themselves not fully convinced, since in line 259 they write "Stepping out of our assumption of the closed system for a moment: when we actually build ASI, we will almost surely want to not optimistically trust that alignment is preserved, but instead continually check the process as carefully as possible, and probably intervene and adjust throughout the training process." However, if closedness is an optional part of their framework, then it becomes an "everything framework" without bounds, thus making it hard to allow an informed and concrete discussion.
- I actually think recursive self-improvement will, at least in practice, not happen in a closed system. We already have the example of [AlphaChip](https://deepmind.google/discover/blog/how-alphachip-transformed-computer-chip-design/), an AI that feeds into better chip design (and thus more compute, which enables better future AI). Similarly, there are companies that try to [steer toward AI that can do ML research](https://openai.com/index/mle-bench/). Arguably, the AI would not act in a closed system but train other (better) AI systems on real-world servers, initially in collaboration with humans.
- I think one can also make the meta argument that researchers have a bad track record of proposing games or task taxonomies that comprise "all there is to learning". E.g., in the past, people thought once we have a chess AI, we will have solved AGI. Now, some people think once we have superhuman math-AI, we will have AGI. This paper seems to suggest that once we have sufficiently good learning procedures in closed language games, we will have AGI. I am a priori skeptical of such claims unless they are very well supported and address possible limitations / counter-arguments / existing literature etc.


# 2. Missing engagement with other work
There is a lot of other work that engages with the question of how (aligned) superhuman AI could or will be developed, and the challenges that arise therein. This paper does not demonstrate engagement with that work. A non-comprehensive list of works that could be engaged with (Very steered toward my personal interests; I am sure there are many others that make sense or that I could name if I'd thought about it for longer):
- Iterated distillation and amplification, see [here](https://arxiv.org/abs/1810.08575) and [here](https://ai-alignment.com/iterated-distillation-and-amplification-157debfd1616).
- The original [debate proposal](https://arxiv.org/abs/1805.00899).
- [11 proposals for building safe advanced AI](https://arxiv.org/abs/2012.07532).
- [constitutional AI](https://arxiv.org/abs/2212.08073), a method that could actually make closedness of the system somewhat easier for alignment (offering a different perspective from my perspective above that alignment isn't possible in a closed system).
- [Coherent extrapolated volition](https://intelligence.org/files/CEV.pdf). This relates to the following paragraph from the paper: "We encourage the reader to imagine an unbroken process of deliberation among a circle of philosophers, maybe starting with Socrates and his disciples, but expanding and continuing undisturbed for millennia: what cultural artifacts, what knowledge, what wisdom could such a process have produced by now?"


# 3. Terminology:
The terminology of recursive self-improvement isn't well thought-through. The definition in the paper seems to be this sentence:
> "The specific type of self-improvement process we consider here is recursive self-improvement, where the agent’s inputs and outputs are compatible (i.e., live in the same space), and outputs become future inputs."

However, the *idea* of recursive self-improvement is of course that the system improves itself, which is not part of this definition. Additionally, we can consider ways of recursive self-improvement that do not feed outputs into future inputs (e.g., if the AI rewrites its own training code, then the training code is not necessarily an input of the AI; yet, this would still arguably be recursive self-improvement in the correct philosophical sense.)


# 4. Addressing the academic community where it's at
This paper engages with an important topic that is, to some degree, at the border of the overton window of academic discussion. As such, it is very important to address the community at a level that engages with common assumptions and the level of the discourse. Otherwise, the distance between viewpoints in the community and this paper become too large to productively engage. Just two examples that exemplify this point:
- The paper assumes some things that I find plausible, but that aren't common knowledge / commonly agreed upon in the literature. E.g., the first paragraph assumes superintelligence will be developed, without grounding this even in the literature, let alone in careful thought.
- "We can motivate this simplification by taking the long view: assuming that compute and memory keep growing exponentially, scale constraints are but a temporary obstacle." -- This clearly requires more extensive discussion or citations since there are varying viewpoints on whether compute will continue to grow exponentially in the foreseeable future.

### Questions
Line 102: "The fundamental property for system-internal feedback is be aligned with the external observer, and remain aligned throughout the process."

Do you mean "**to be** aligned", and do you mean "requirement" instead of "property"?

### Soundness
2

### Presentation
3

### Contribution
1
