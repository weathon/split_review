# Goal-Directedness is in the Eye of the Beholder

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Our ability to predict the behavior of complex agents turns on the attribution of goals. Probing for goal-directed behavior comes in two flavors: Behavioral and mechanistic. The former proposes that goal-directedness can be estimated through behavioral observation, whereas the latter attempts to probe for goals in internal model states. We work through the assumptions behind both approaches, identifying technical and conceptual problems that arise from formalizing goals in agent systems. We arrive at the perhaps surprising position that goal-directedness cannot be measured objectively. We outline new directions for modeling goal-directedness as an emergent property of dynamic, multi-agent systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a critical analysis of current methods for identifying goal-directed behavior in AI agents. They argue that goal-directedness is an attribution by an observer. They examine behavioral and mechanistic approaches. 

The paper argues that both approaches suffer from significant technical and conceptual problems. Behavioral methods face "syntactic problems" in pathological cases (e.g., when a goal is unreachable) and "conceptual problems" regarding the ambiguous granularity of goals (e.g., wanting cheese vs. wanting to stave off hunger). These methods also become computationally intractable in multi-agent scenarios. Mechanistic approaches are challenged by the principles of multiple realizability (a single goal can be implemented in many ways) and externalism (a goal may not be fully encoded in an agent's internal states). The authors support this with a simple experiment showing that linear and non-linear probes fail to distinguish between agents trained on two distinct goals.

### Strengths
1. There is a strong critical analysis provided, revealing significant and overlooked conceptual ambiguities.
2. Effective use of examples
3. Concepts from philosophy of mind, CS are thoughtfully integrated

### Weaknesses
1. The multi-agent simulation alternative is not fully fleshed out.
2. It is unclear if this result would hold against the more sophisticated models (e.g., Transformers) currently used in the field.
3.  An alternative view, which the paper acknowledges but could engage with more deeply, is that current measures are useful, if imperfect, proxies necessary for practical safety engineering.

### Questions
1. Your paper argues that goal-directedness is in the "eye of the beholder." How does your proposed solution of using simulation escape this critique? Doesn't an observer still need to interpret the simulation's results and attribute goals to the observed emergent behaviors?
2. You raise excellent points about the ambiguity of a goal's granularity (e.g., "obtain cheese" vs. "stave off hunger"). How would a simulation-based approach be designed to distinguish between these different levels of abstraction without an observer imposing them?

### Presentation
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper provides a position about goal-directedness, in particular, the position says that goal-directedness cannot be measure objectively. The paper considers two types of approaches towards goal-directedness: behavioural and mechanistic, then provide various arguments as well as examples to derive towards the proposed position, which is that goal-directedness is not enumerable.

### Strengths
+ The paper aims to propose a proposition in an important research area, which is to consider goal-directed behaviour of agents in complex environments.
+ The paper writing is really good. I really enjoy reading this paper. The paper provides a very clear proposition as well as the supporting arguments.
+ The paper also provides various related works as well as various related positions.

### Weaknesses
I think I would like more if some technical details were explained in a clearer way in the paper.

+ First, the definition of goal-directedness should be explained clearer, and also, the scope of the types of agents the paper considers is not clear. The paper states that an agent is modelled as a node in a Bayesian Network; is this true for all types of agents? If not, then the paper needs to make this clear.

+ Second, the arguments for the position, even very well-explained, are quite intuitive and general. For me, I hope for a more technical arguments for the position. 

+ Third, just my point of view regarding the position, I’m just wondering if the reason the goal-directedness cannot be measured objectively is that we do not have a well-defined definition of goal-directedness. If we have this ideal definition, can goal-directedness be measured appropriately?

### Questions
The authors could answer the comments and questions I listed in the Weaknesses section.

### Presentation
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper discusses goal-directed behavior. It claims that goal-directedness cannot be measured objectively. Then, it outlines new directions for modeling goal-directedness as an emergent property of dynamic, multi-agent systems.

### Strengths
1. The problem studied is important and fundamental. 

2. The writing is very good. It provides sufficient background knowledge, shows evidence regarding the limitation, and then points out new directions.

### Weaknesses
I am not familiar with this area. So my question might be very superficial. 

1. The conclusion is obtained from a toy example under some assumptions. Does the assumption hold for practical applications? Does the obtained conclusion work for the generic settings? If not, the foundation of this position paper is problematic. It would be good to provide more convincing results. 

2. As a position paper, it would be good to provide more discussions for the future direction. The current version just uses two pages to point out the future direction. It is kind of not sufficient. It would be good to provide more comprehensive discussions for the future direction.

### Questions
1. The conclusion is obtained from a toy example under some assumptions. Does the assumption hold for practical applications? Does the obtained conclusion work for the generic settings? If not, the foundation of this position paper is problematic. It would be good to provide more convincing results. 

2. As a position paper, it would be good to provide more discussions for the future direction. The current version just uses two pages to point out the future direction. It is kind of not sufficient. It would be good to provide more comprehensive discussions for the future direction.

### Presentation
2
