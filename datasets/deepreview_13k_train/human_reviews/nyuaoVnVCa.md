# EMERGENCE OF GROUNDED, OPTIMALLY COMPOSITIONAL SPATIAL LANGUAGE AMONG HOMOGENEOUS AGENTS

- Decision: Reject
- Scores: 3, 1, 3

## Abstract
A mechanism of effective communication is integral to human existence. An
essential aspect of a functional communication scheme among a rational human
population involves an efficient,  adaptive, and coherent apparatus to convey one’s goal to others. Such an effective macro characteristic can
emerge in a finite population through adaptive learning via trial and error
at the individual (micro) level, with nearly consistent individual learning faculty and experience across the population. In this paper, we study and hypothesize
 pertinent aspects of glossogenetics, specifically primal human communication mechanisms, through computational modeling. In particular, we model the
process as a language game within the fabric of a decentralized, multi-agent
deep reinforcement learning setting, where the agents with local learning and neural
cognitive faculties interact through a series of dialogues. Our homogeneous agents seek to achieve the principle of least effort and overcome the poverty of stimulus through efficient concept selection, guided feedback and mirror learning. In our examinations,
we observe the emergence of successful and structured communication among static and dynamic agent populations through consistent and continual learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a model of emergence of compositional languages in the reinforcement learning framework.

### Strengths
The review of the previous works regarding emergence of language is well organized.

### Weaknesses
On the other hand, the original contribution of the present work on top of previous works is not clear.
There is no result figure in the main part of the paper. They should be moved from Appendix to the main part while method details can be put in the Appendix.

### Questions
What do you mean by ontology? Is it assumed that all agents discretize the continuous environments exactly the same way even before any language is evolved?
When communication failed, how is the topic node disclosed to the listener without language?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The paper investigates the emergence of language in a multi-agent setting, in which different agents have to communicate with each other and evolve their own language. To this end, the paper introduces a special environment, which is essentially a guessing game in which a speaker selects a concept, which has to be correctly guessed by a randomly selected listener via the discrete & noise-free communication channel. The paper uses an RL-driven multi-agent algorithm to encourage agents to develop a language maximising a shared return.

### Strengths
- The overall analysis and statement of made assumptions seem sound
- The visualization of the guessing game are indeed nice
- There is some formal grounding of the paper, ie technical detail is there

### Weaknesses
 - My biggest concern is that after reading the paper, I don't know its actual contribution. While the paper lists several prior works, to me, it essentially introduces a specific game that may or may not be novel, develops an RL-driven framework to allow the emergence of a communication protocol, and then shows that it works. I will list the points of concern in detail below.
- Is the game novel? Knowing some related works, it does not seem to deviate from prior environments in any important concept or detail. If the game is novel and allows agents to learn or equip new abilities, there should be at least a comparison against a prior (i.e. weaker) environment showing that this is the case.
- Is the language channel/discretization novel? Again I don't think so but the paper is not clear on this.
- While a RL-learning method is introduced, its discussion falls short of pointing out what makes it special from prior work, nor is a good ablation study performed. The paper essentially shows that the framework works, but it is not clear what makes it work nor how it relates to prior works in emergent language learning.
- While related work is mentioned, the paper would greatly benefit form a related works section clearly stating its contribution and differences to prior work. The current contributions section falls short of describig the novelty of the presented research.
- The paper is not concise and sometimes goes on tangents, seemingly not relevant to the main contribution of the paper (e.g. section 6.2 to just name a single example). I also want to remind the authors that the reviewers are not obliged to read the supplement, nor should all relevant experimental results be included in the supplement. Strictly speaking, the paper itself (pages 1-10) does not present any results, as all results/tables/figures are in the appendix. The paper needs to be rewritten so that at least the main results are in the first 10 pages; additional experiments or further analyses may be included in the supplement. The paper needs to be more concise and detail its core contribution, core results and detail the impact it has for other researchers/the field.
- I fail to see the impact of the paper. It shows that a language emerges in the framework, but how is this significant? Is any new problem solved? Can we do anything with the concepts introduced in the paper? I fail to see how the paper would be of interest to other researchers without further discussion on these points.

### Questions
Please see the weakness above. In my opinion it is not clear what the core contribution of your paper is beyond introducing a method and showing it works. It is unclear where it goes beyond the current state of the art.

The paper needs some comparison against another baseline, environment or similar. The paper is not the first to introduce a framework for emergent language.

I do think the paper needs an extensive rewrite + additional experiment. I am very unlikely to change my opinion without these concerns being addressed.

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates emergent communication and its properties under the paradigm of decentralized multi-agent deep reinforcement learning. The entire investigation is based on a proposed multi-agent ‘guessing game’ that is a lot more complex than existing Lewis signaling games in terms of vocabulary alignment and learning. A multi-component object function is proposed to learn how to communicate, inducing properties of interchangeability, compositionality, and the principle of least effort. In particular, the paper shows that enabling interchangeability avia mirror learning allows agents to act effectively as both a listener and a speaker. Studying the emergent linguistic patterns developed by agents in this game shows findings that align with natural phenomena like the alignment with Zipf’s law in terms of word frequencies.

### Strengths
- The paper proposes a novel multi-agent guessing game with greater complexity than existing signaling games which could be useful for future works 
- The proposed properties and objective function show aligned properties with languages in the nature

### Weaknesses
 - The paper is unfortunately poorly written. At times, it becomes difficult to understand what the authors mean. For instance, the abstract lacks clarity with a lot of vague use of vocabulary. An abstract is supposed to allow readers to understand the general idea of the paper. But this abstract is very confusing. The introduction is also poorly written, with a long chain of citations without much of a coherent message. The paper needs a lot of revision before it meets the standard of ICLR
- There should at least be some key results in the main paper, instead of having all the results in the supplementary materials
- Figure 1 should have a more elaborate caption

Places that need clarifications:
- Line 74, what do you mean by self-organization in language games?
- Line 92-93, a vague sentence
- Line 257, what do you mean by ‘effective guidance’?

### Questions
- In line 67, how does mirror learning ensure continual learning?
- In line 510, how does the mentioned property mirror patterns observed in human interactions? Please give support and example

### Soundness
2

### Presentation
1

### Contribution
2
