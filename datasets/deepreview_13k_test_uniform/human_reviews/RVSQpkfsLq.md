# Evolving Virtual World with Delta-Engine

- Decision: Reject
- Scores: 3, 3, 1, 1

## Abstract
In this paper, we focus on the \emph{virtual world}, a cyberspace where people can live in. An ideal virtual world shares great similarity with our real world. One of the crucial aspects is its evolving nature, reflected by individuals' capability to grow and thereby influence the objective world. Such dynamics is unpredictable and beyond the reach of existing systems. For this, we propose a special engine called \textbf{\emph{Delta-Engine}} to drive this virtual world. $\Delta$ associates the world's evolution to the engine's scalability. It consists of a base engine and a neural proxy. The base engine programs the prototype of the virtual world; given a trigger, the neural proxy generates new snippets on the base engine through \emph{incremental prediction}.

This paper presents a full-stack introduction to the delta-engine. The key feature of the delta-engine is its scalability to unknown elements within the world, Technically, it derives from the prefect co-work of the neural proxy and the base engine, and the alignment with high-quality data. We introduce an engine-oriented fine-tuning method that embeds the base engine into the proxy. We then discuss the human-LLM collaborative design to produce novel and interesting data efficiently. Eventually, we propose three evaluation principles to comprehensively assess the performance of a delta engine: naive evaluation, incremental evaluation, and adversarial evaluation.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, authors propose a Delta-Engine generates executable code and embed it into the base engine using Large Language Models.

### Strengths
In this paper, the authors tried to make the game engine (a backbone of the virtual world) changing over time. It's interesting to update the backbone engine using Large Language Models.

### Weaknesses
This paper tries to tackle challenging problems to update game engines (usually static components of the virtual world) over time. However, the solution description on the problem is not clearly defined in the manuscripts. 

In the Abstract, authors stated that "existing virtual worlds are strictly defined by the back-end engine and cannot be changed by user's behavior." It's an interesting statement however, it's still questionable that the engine needs to be changed by user's behavior. It's a radical change to the world and there could be a solution to reflect the user's behavior's outcome to the world without changing the game engine itself. 

In the Abstract, there are terms that make it difficult for readers to focus on the contribution. For example, they're "scalability to user-generated content," "dual aspects of algorithm and data," "neural proxy," and "novel and interesting data." It's relatively new to be difficult to grasp the concepts from the first reading. It's recommended to improve the summary to be readable for the audience. 

In the Introduction, authors argue the necessity of "evolving nature." What's the definition of the evolving in this paper to be used? I recommend authors to provide more explanation why back-bone engines needs to be "evolving" instead of other alternative solutions (evolving objects instead of changing the world itself) traditionally approached in many game-related articles. Also, it's good to add some evidence on "Such dynamics is unpredictable and beyond the reach of existing systems." 

Authors need to improve their manuscripts by avoiding unclear definitions of words or terminologies. For example, they're "Its codebase will become more and more along with the world's evolution." "God mode," "Biodiversity," "Imagination," and "Tags of Interest" so on. 

In Chapter 3, the Delta-Engine description needs to be improved. For example, the Base engine part includes "only walking ability" "learns to run and even fly." It seems that the engine is limited to the sample scenario. It's desirable to provide a general introduction of the methodology. In the incremental prediction part, please explain what is the input, and what is the value? In the retrieval, what is the sparse version? 

In conclusion, this paper's weak point is unclear description of their ideas with ill-defined justification of research goals.

### Questions
* Could you generalize the Delta-engine to other problems instead of the Pokemon?
* What is the critical benefit of using Delta-engine instead of traditional game engine (unity, or unreal or custom engines)?
* Could you differentiate your system with an LLM-based story generator? What's the main difference between your work and other narrative generators?
* When you apply Procedural Contents Generation, it assumes the world is not changing over time (e.g., basic rules of the game, or physical property is fixed). How can we modify the current PCG in the context of your changing game engines?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper introduces a novel virtual world engine called Delta-Engine, that evolves dynamically based on user behavior. Delta-Engine is composed of a base engine and a neural proxy. The neural proxy generates new content on the base engine through incremental prediction. The technical implementation uses retrieval techniques to enhance the connection between the neural proxy and the base engine. Additionally, it introduces a human-LLM collaborative design to ensure that the generated content is novel and engaging.

To be honest, the reviewer fails to identify what this work actually does / the contributions. The above summary was written based on the paper text. The reviewer is happy to revise the review if the following comments/questions can be addressed.

### Strengths
-  Appendix provides a demo.

### Weaknesses
- The manuscript lacks clarity, making it difficult for readers to understand the significance and motivation behind the study. 

- The absence of a clear problem definition undermines the overall coherence of the paper. The concept of the Delta-engine is vaguely defined, and the paper does not provide definitions for fundamental terms, such as “engine state,” “new features,” and their relationships with virtual environmental dynamics generated by the neural proxy. 

- Additionally, the description of the engine and evolving world lacks sufficient details, making it challenging to evaluate the feasibility and innovation of the proposed approach. The authors mention that the engine must address challenges in both algorithm design and data management. However, the experiments on AI co-design and the synthetic data generation process remain unclear in terms of how they work.

### Questions
Please refer to the comments. Can the authors clarify the contribution of the work?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
In this paper the authors present a concept for a continually expanding game engine which they call a "delta engine". The authors pitch is that an LLM can be used as a wrapper to determine how best to update an engine written in code based on some instruction or signal. They then present a toy environment based on Pokemon where they use a fine-tuned LLM and prompts to create new Pokemon or add additional moves to a Pokemon. They then present an experimental evaluation in which they demonstrate their approach can accurately recreate existing Pokemon and Pokemon designed by human volunteers.

### Strengths
The core concept of the delta engine is an interesting one, though it's unclear whether this is substantially different than any game engine that includes generated content from a code generator LLM. Generating new Pokemon moves or base stats is technically novel, but it is not surprising that LLMs can generate code that works for these purposes.

### Weaknesses
This paper has a very large number of issues in its current state. To organize my feedback I'll introduce these issues in each section. 

### Introduction

The introduction has the primary issue of not being particularly relevant to the actual research work that has been done. There is no clear pathway from the authors prompt-based Pokemon generation to the virtual worlds they describe. It would be better to focus the paper on the specific research project being presented. I would further suggest that the authors remove all unsupported claims like "Its codebase will become more and more along with the world’s evolution" or "Delta-engines can serve as the basic components of the world to simulate their evolving processes, encompassing roles, surroundings, props, and other integral components", given there's no proof of either in this paper or in prior work. Similarly, I would suggest the authors remove tangential sentences like "The evolution is triggered by specific signals within the world, e.g. observations, behavior, and events.". The introduction also introduces two other recurring issues in the paper. The first is that many of the figures are not legible, like the choice and size of font in figure 1. The second is that the language is very poor with many grammar or inappropriate wording issues, such as "Such dynamics is unpredictable"->"Such dynamics are unpredictable" or the use of "Pokemon role" when I believe the authors may have meant "Pokemon character". 

The authors notably claim that code, data, and a demonstration are available in the supplementary materials, but this is untrue. There is a small Pokemon battling clone with some pre-generated elements.

### Related Work

The authors cite a great deal of prior work, which is great. However, many of the citations are not relevant to this work. For example, the authors do not need to list all the AI work across various games in the final paragraph. Instead, I would have recommended that the authors discuss prior work in generating code for game characters [1,2]. In addition, the authors likely should have touched on prior work on generating Pokemon, though the majority of this prior work is focused on generating Pokemon-like visuals [3,4,5], some of the prior work does touch on descriptions [3] or type information [5]. 

It is also notable that GameNGen is not based on prompts.

### Delta Engine and Playground: Free Pokemon and Training Data Generation

I am grouping all three of these as they make up the system overview equivalent sections of the paper. In general, the authors would ideally have included all technical aspects of the work in sufficient detail that they could be replicated. But this is not the case, the authors do not include their representation of Pokemon or rules (except via examples), they do not give their prompts or prompt structure, and most importantly they do not give how their co-creative setup works. Part of the problem here may be the lack of clarity (writing and language issues) in the paper.

### Experiments 

The authors present an experiment to show that their approach can recreate existing Pokemon and that it can recreate Pokemon created by human "volunteers". The issues here are primarily with the volunteers with the experiments otherwise being very reasonable for evaluating Pokemon generation. The authors do not specify if they had ethics approval for this human subject work or if the participants were compensated. It's also unclear what prior knowledge they had or what their relationship is to the authors. Without full methodological information it is impossible as a reader to judge the validity of their date, making the results related to it similarly difficult to trust. Similarly, it's unclear what the co-creative experience was or who the humans were who took part in it, making it very unclear how to interpret the "& CO." results. These issues remove any generalizable knowledge other researchers may have been able to take from this experiment. 

Figures 5 and 6 similarly have issues in terms of how they were made and what they mean. For Figure 5, it's unclear if this experiment was run a single time or what all the colours and lines indicate. For Figure 6, it's unclear how the authors created their semantics and interestingness spaces or how they are projected into two dimensions.  


1. Butler, Eric, Kristin Siu, and Alexander Zook. "Program synthesis as a generative method." Proceedings of the 12th International Conference on the Foundations of Digital Games. 2017.
2. Sorochan, Kynan, and Matthew Guzdial. "Generating real-time strategy game units using search-based procedural content generation and monte carlo tree search." arXiv preprint arXiv:2212.03387 (2022).
3. Geissler, Dominique, et al. "Pokérator-unveil your inner Pokémon." 11th International Conference on Computational Creativity, ICCC 2020. 2020.
4. Liapis, Antonios. "Recomposing the pokémon color palette." Applications of Evolutionary Computation: 21st International Conference, EvoApplications 2018, Parma, Italy, April 4-6, 2018, Proceedings 21. Springer International Publishing, 2018.
5. Gonzalez, Adrian, Matthew Guzdial, and Felix Ramos. "Generating gameplay-relevant art assets with transfer learning." arXiv preprint arXiv:2010.01681 (2020).

### Questions
1. Have I substantially misunderstood the authors work?
2. What was the methodology for the human subject study/volunteers?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This manuscript is not suitable for publication. I cannot understand it. It’s full of strange, nonsensical sentences and descriptions. It uses all sorts of unusual jargon without ever defining it. Sometimes it feels like it is about to veer toward making sense, only to confuse me again. I am unable to judge the quality or purpose of any experiments done (or their motivations) because the writing is so confusing. I am not sure if it was written by a poor language model (the best ones would write something more understandable), or scientists that have not undergone any or at least proper training, but it is not ready for publication. If this is a well-intentioned attempt, I apologize for the harsh review, but I recommend you work closely with trained scientists to learn how to write a clear manuscript that meets the bar for scientific manuscripts. There are some hints of some good ideas, but they are far from being dealt with properly enough to evaluate them, let alone endorse the entire manuscript for publication. 

This is the shortest review I have ever written in over 20 years in the field. It is hard to think of what else to say except the manuscript is unintelligible enough that there’s not much more to say than that.

### Strengths
See main review.

### Weaknesses
See main review.

### Questions
I do no understand almost anything, so my question/challenge is to try to explain everything clearly in your next submission of the work.

### Soundness
1

### Presentation
1

### Contribution
1
