# The Pillars of Skill-Acquisition and Generalization; Why efficient General Intelligence requires Multi-Component Integration

- Decision: Reject
- Scores: 2, 3, 4

## Abstract
Breakthroughs of Large Language Models (LLMs) have rekindled hopes for broadly capable artificial intelligence (i.e., Artificial General Intelligence (AGI)). Yet, these models still exhibit notable limitations – particularly in deductive reasoning and *efficient* skill acquisition. In contrast, neuro-symbolic approaches can exhibit more robust generalization across diverse tasks, as they integrate sub-symbolic pattern extraction with explicit logical structures. In this position paper, *we go a step further* and dissect generalizing systems into *six pillars*: well-defined model specificity, (human) capability encoding, dynamic knowledge acquisition & transfer, meaningful representations, abstraction & hierarchies, as well as the synergy effects resulting from component interactions. Based on historical and contemporary Artificial Intelligence (AI) approaches, we conclude that such **a multi-component implementation strategy is necessary for efficient general intelligence**. Our position is reinforced by the latest performance gains on the Abstraction and Reasoning Corpus (ARC) generalization benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
2

### Rating Number
2

### Confidence
4

### Summary
This paper advocates for neurosymbolic AI, arguing that AI systems that can efficiently generalize need to use neurosymbolic AI to be successful. They list six pillars of for efficient generalization, based off the ARC-AGI benchmark.

### Strengths
The paper discusses an important topic — efficient generalization of AI methods — and issues related to an influential benchmark, ARC-AGI.

### Weaknesses
The argument is not clear. Terms are not clearly defined. Overall, the writing quality is the main thing dragging down the paper. The argument could be improved by making more precise terminology and arguments. For example, the paper proposes "multi-component integration" which could really mean anything in the context of AI architectures. Similarly, another pillar is "knowledge acquisition, transfer, and combination" which is vague. 

The paper discusses lots of interesting topics, and the discussion about each topic is interesting, but the overall argument is muddled. It mentions many different interesting research topics related to neurosymbolic AI, but seems to be advocating for the field of research as a whole, while also trying to argue that the whole thing is necessary.

### Questions
If the position in your paper were to be agreed with and adopted by AI researchers, what changes would you see in the community? Are there any existing works which would be approached differently as a result of your position?

### Presentation
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a few components that underpins the generalizability of AGI. Following Chollet [2019] it defines AGI as generalizability (skill-acquisition efficiency) , and uses  ARC generalization benchmark as the corresponding metric. It first reviews the limitations of existing neuro (LLMs) and symbolic approaches, and then lists main limitations of the combined neuro-symbolic approaches. 
1) exponential search space
2) bad data efficiency
3) require hard-coded DSL for new concepts
4) lack of standard implementation

Then it proposes to extend neuro-symbolic approaches with 6 components.
1) A limited model scope (e.g., counting, shape manipulation) allows high skill-acquisition efficiency
2)  encode human knowledge at an abstract level (e.g. move(object, vector)) to avoid overfitting to details.
3) Embedding spaces can be lack of specificity, while graph/object representations are both interpretable and reduce search spaces compared to pixels.
4) Abstractions and Hierarchies are useful as demonstrated by conv nets and AlexNet.
5) Knowledge Acquisition, Transfer, and Combination (pretraining, fine tuning, test time fine tuning)

### Strengths
This paper summarizes recent findings related to the ARC benchmark.

### Weaknesses
My main concern with this paper is its lack of novelty. The listed limitations of neuro-symbolic approaches are mainly known limitations of symbolic approaches. The listed components are useful characteristics but none is particularly novel given research in the past decades. The components feel more like a summary of recent results in deep learning and the ARC benchmark, and they lack a novel perspective or hypothesis. The completeness of these components is also not discussed, because there is little evidence that they are the most important ones. For example, are long term memory and spatial representations also important for AGI?

### Questions
See weakness

### Presentation
3

---

## Human Reviewer 3

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
This paper adopts the definition of AI as skill acquisition efficiency, and advocates evaluation of a model's capacity to abstract knowledge from sparse data and adapt to novel tasks. This paper critiques current predominant research in Large Reasoning Models and neuro-symbolic approaches, arguing that they are insufficient to build a truly generalizable system. 

Instead, they posit that a multi-component implementation strategy, which consists of six pillars, is necessary for efficient general intelligence. The six pillars include Model Specificity, (Human) Capability Encoding, Meaningful Representations, Knowledge Acquisition & Transfer, Abstractions & Hierarchies, and Multi-Component Synergy.

### Strengths
- The paper addresses a timely and important topic in the ongoing debate between neuro-based and symbolic methods, and identifies several valuable components for designing systems that are efficient in skill acquisition.

- The work is well-motivated from the perspectives of generalization and skill acquisition, and it clearly articulates both the advances and the limitations of recent LRM- and symbolic-based approaches.

- The discussion of the six pillars is well-grounded, with each point supported by relevant evidence from the literature.

### Weaknesses
- While the six pillars advocated are valuable, it is not clear whether they are strictly necessary for building such a system. Incorporating all six may increase system complexity, potentially hindering implementation and evaluation. The paper also lacks actionable guidance on the implementation of these pillars in real applications.
- The paper mentions generalization multiple times. However, the type or degree of generalization intended is not crystal clear. For instance, "local forms of generalization" (line 21) is not clearly defined. It would be clearer with precise definition and demonstrative examples.
- The evaluation centers on the ARC dataset, yet it is not clear how the six pillars apply to other datasets or domains. Many datasets may not easily be aligned with the structured style of ARC.

### Questions
- Instead of integrating symbolic modules with neural models at the architectural level, some approaches train neural models on neural–symbolic datasets (e.g., [1, 2]) in domains such as math, coding, and other symbolic tasks, showing improved performance and generalization on downstream tasks. How do you view this data-driven form of synergy between neural and symbolic methods, and how might it compare to the framework you discuss?\
[1] Math for AI: On the Generalization of Learning Mathematical Problem Solving\
[2] How Does Code Pretraining Affect Language Model Task Performance?

Would requiring all six pillars introduce unnecessary complexity into system design? For instance, some pillars are motivated by interpretability considerations, which can be challenging to achieve robustly. How practical and actionable do you consider the proposed pillars in real-world implementations?

### Presentation
2
