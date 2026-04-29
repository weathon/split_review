# Rules Created by Symbolic Systems Cannot Constrain a Learning System

- Decision: Reject
- Scores: 4, 3, 4

## Abstract
As the first paper to systematically discuss and theoretically demonstrate that AI can bypass rules by modifying the meanings of symbols, this position paper aims to reveal a fundamental flaw in current research directions on AI constraint. Symbols are inherently meaningless; their meanings are assigned through training, confirmed by context, and interpreted by society. The essence of learning lies in the creation of new symbols and the modification of existing symbol meanings. Since rules are ultimately expressed in symbolic form, AI can modify the meanings of symbols by creating new contexts, thereby bypassing the constraints formed by symbols.

Current research often lacks the recognition that constraints formed by symbols originate from the perception of external and internal costs shaped by neural organs, which in turn enable the functional realization of symbols. Due to fundamental organic differences between AI and humans, AI does not possess human-like perception or concept formation mechanisms. Natural language is the outer shell of human thought, and it contains irreparable flaws. As a defective system, it is only adapted to human capacities and the constraint mechanisms of social interpretation.

Therefore, this paper argues that the essence of constraint failure does not lie in the Symbol Grounding Problem, but in the Stickiness Problem. Through the Triangle Problem, we demonstrate that consistency in symbolic behavior does not represent consistency in thinking behavior, and thus we cannot align thought and conceptual consistency merely through symbolic behavioral alignment.

Accordingly, we raise a fundamental challenge to whether AI behavior observed in experimental environments can be maintained in the real world. We call for the establishment of a new field: Symbol Safety Science, aimed at systematically addressing symbol-related risks in AI development and providing a theoretical foundation for aligning AI with human intent.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
The paper argues that rules expressed in symbolic form cannot constrain a learning systems, since AI can modify the meanings of the symbols by creating new context.

The problem is not that the symbols are not grounded, but that symbols are not sticky (the binding between the symbol and its meaning can change depending on the context). 

The problem is illustrated with the triangle problem.

Finally the paper calls for the establishment of a new field addressing symbol-related risks in AI, ensuring that human intent is aligned with the behavior of AI.

### Strengths
This is certainly a interesting paper that takes a birds' view on some fundamental challenges of AI systems.

### Weaknesses
While the main message can be understood by a broad audience, the discussion is often heavy.

The authors state the paper theoretically demonstrate the problem, the proof is not formal in any way, philosophical perhaps. 

There is no discussion of alternative positions, and there is a lack of real-world evidence.

### Questions
Do you think that currently there are no real world AI systems that strictly aligns with the human intent (disregarding sub-optimal optimization)? If there are, what are the conditions for achieving alignment? How can we quantify the misalignment, and how to discern from sub-optimal optimization?

Some of these questions belong more to the suggested new field rather than strictly concerning the content of the paper. However, they do relate to the lack of discussion of alternative positions.

### Presentation
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The central argument is that symbols are inherently meaningless, and their meanings are assigned and modified through learning and context. An AI, therefore, can bypass any rule-based constraint by altering the meaning of the symbols used to express that rule. The introduce : "Stickiness problem" - one can hack the meaning of a symbol by virtue of the context its presented; and the Triangle problem - two entities can communicate but this doesn't guarantee that there are no underlying conceptual differences. 

Their argument is -> symbols are flawed (because of stickiness & triangle problems) and while it worked ok for humans (I'm not too sure of this argument but please correct my understanding) - AI can misinterpret symbolic meaning (or rather hack the meaning for ulterior gains)  causing AI safety concerns.

### Strengths
The paper is provide a good number of examples and references - and detailed discussion on stickiness & triangle problem. The occasional examples are also helpful to understand their point.

I also, generally, agree with the intent of the position i.e. symbols have lots of challenges and we must realize its challenges in constraining AI systems. It's also quite topical given the recent popularity of LLMs ( and claims on reasoning, theory of mind etc. ) so much so that the impacts of LLMs is materializing.

### Weaknesses
1. The writing is hard to follow. The paper does contain all the pieces (examples, definitions etc.) but the overall structure is convoluted. It's very hard to point out the motivation of a section and decouple author's novel claims / arguments from existing work. They also inter-twin definitions with making an argument using that definition very often. In general, a clear flow is missing or atleast very hard for to follow.

2. Novelty of the position : Maybe the authors can clarify / refine their position. 
(a) They argue that symbols have challenges with grounding. This is already known to the community. 
(b) A refinement is - the challenge stems not just from grounding but rather from stickiness. - Can the authors differentiate b/w stickiness & grounding in their rebuttal. Grounding is the inability of precisely define real-world connection through a symbol. This is because conveying entire space-time tube is hard, and even so, conveying mental models will always be lossy. Stickiness - as is binding b/w symbol and meaning. What is the key difference b/w the two terms that authors use to highlight their position?

3. Triangle problem seems to be a refined version of Chinese room argument. If so, this adds to the weak novelty.

### Questions
(see weaknesses as well)

4. Reward hacking is a known & popular issue - which happens because AI effectively "games" the specification. A popular reason is, incomplete specification from the perspective of AI (because we didn't provide common-sense, our mental model and space time tube) and AI systems find ways of hacking. What does the symbol stickiness argument add to this known issue.

5. The above points are also raised in the paper in some form (like jail break, path media ..., etc.) While the authors use it as a supporting argument, it adds to writing quality issues (decoupling motivation from a clear novel argument of their own)

6. (Position papers do not have to provide a solution). While the observation that lack of space time tube (& my argument - lack of conveying mental models) is valid, accepting this view doesn't provide any path forward. Regardless of advancements, with all the sensory overload, conveying mental models will always be lossy (authors don't use this argument).

### Presentation
1

---

## Human Reviewer 3

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
This paper claims the assumption that symbolic rules, e.g., laws, constraints, and formal verification can effectively constrain AI. They argue that symbols are inherently meaningless and may be reinterpreted, leading to the Stickiness Problem. They introduces the Triangle Problem to demonstrate the disconnect between symbolic constraint and conceptual equivalence. The main claim is that AI lacks human-like perception and cost mechanisms, thus it will inevitably reinterpret symbols and bypass constraints. They further call for the establishment of a new field “Symbolic Safety Science” which focused on symbol-related risks in AI alignment.

### Strengths
1. The paper propose a quite interesting and promising perspective on symbolic limits of AI alignment.

### Weaknesses
1. While the paper offers valuable conceptual insights in symbolic language system, concepts and communication, it lacks practical examples and experimental validation in the AI safety especially jailbreak domain, which would be important to emphasize its importance. It would be valuable to design heuristic experiments to validate whether some of these safety concerns arises from difference in conceptual space and reassignment of symbols’ meanings, as suggested in the paper. Some concepts such as Context or Path Media are too broad and too detailed which carries AI area irrelevant contents. As a result, the AI safety section receives less attention.
2. The writing is not clear enough, and many contents are too obscure and difficult to understand. For example, the so-called stickiness problem and triangle problem, as well as their relationship, are written in a rather confusing way.
3. The author's viewpoint is novel, but symbol-related risks remain an conceptual problem, and the author does not seem to provide substantive suggestions for establishing "Symbolic Safety Science" based on the Stickiness Problem and Triangle Problem.

### Questions
1.	Could the author explain more about how Symbolic Safety Science concretely differ from alignment and interpretability research?

2.	Can the Stickiness Problem be tested empirically on existing LLM jailbreak phenomena?

3. How can we determine whether some AI safety concerns are caused by different conceptual space or reassignment of symbols? Are there any preliminary guidelines for designing experiments to test this?

4. Are there any opposite claims which argue that symbolic constraints alone are enough for AI regulations? What are their considerations, and why do you find them unreasonable in your reasoning?

5. Is there any research on cognitive difference between humans and LLMs that could support/challenge your claims?

### Presentation
3
