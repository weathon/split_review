# Transformers Have the Potential to Achieve AGI

- Decision: Reject
- Scores: 4, 7, 7

## Abstract
As large language models (LLMs) based on the Transformer architecture continue to achieve impressive performance across diverse tasks, this paper explores whether Transformers can ultimately achieve artificial general intelligence (AGI). We argue that Transformers have significant potential to achieve AGI, supported by the following insights and arguments. (1) A Transformer is expressive enough to simulate a programmable computer equipped with random number generators and, in particular, to execute programs for meta-tasks such as algorithm design. (2) By the extended Church-Turing thesis, if some realistic intelligence system (say, a human with pencil and paper) achieves AGI, then in principle a single Transformer can replicate this capability; Besides, we suggest that Transformers are well-suited to approximate human intelligence, because they effectively integrate knowledge and functions represented in network form (e.g. pattern recognition) with logic reasoning abilities. (3) We argue that Transformers offer a promising practical approximation of Hutter's AIXI agent, which is an ideal construction to achieve AGI but is uncomputable.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
2

### Summary
This position paper argues that the Transformer architecture—by its demonstrated capacity to simulate probabilistic turing machines, its accord with the extended Church–Turing thesis, and also the potential to approximete theoratical constructs—has both the theoretical expressiveness and practical promise to ultimately achieve artificial general intelligence. The authors marshal a three‑part argument. First, Transformers can simulatees any computable process via chain‑of‑thought prompting. Second, by the extended Church–Turing thesis, any physically realizable intelligence can in principle be emulated by a Transformer. Third, Transformers offer tractable approximations of universal search and induction frameworks, and are composed into an environment modeler and action planner to approximete AIXI in practice.

### Strengths
This is an ambitious call that directly links Transformers to core AGI constructs, giving a bold, unified vision.

The paper provides formal theorems and detailed backgrounds and theoretical contexts for readers to understand.

The call is impactful, given that there are always heavy discussions on whether LLMs or any Transformer-based model is the correct direction of AI development to achieve AGI.

### Weaknesses
The most important concern is the practical gap between the call and the real implementation scenario. The analysis of the paper is way too heavy on theory, and there is almost no empirical evidence showing how to realize this potential at scale. Also, this dense formalism may alienate readers seeking intuitive understanding or real‑world application guidance. I highly recommend that the author break down a little bit of the theory and link it to the current development of transformer-based models, and this may help strengthen your argument and clarity.

### Questions
Following the concern about the weakness of the gap between theory and implementation, how would you empirically validate or suggest to other researchers that the two‑Transformer AIXI approximation—what tasks or benchmarks would you propose?

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
arguments:
1. It is shown that transformers with Chain of Though (CoT) can simulate Probabilistic Turing Machines (PTMs) with a number of CoT steps linear to the steps taken by the corresponding PTMs.
1. Assuming the extended Church-Turing thesis and based on the previous argument PTMs should be able to simulate any physical system with a polynomial computation overhead. Furthermore, citing the affinity of transformers to connectionism and symbolicism it is argued that transformers should be good approximations of the specific case of human reasoning.
1. In the more specific situation of problem solving, formalized by Hutter's AIXI agent, based on the ability of transformers with CoT to simulate universal Turing machines and efficiently solve sequence prediction, they are presented as a good approximant it. A specific framework with an environment modeler and action planner transformer is provided as a practical setup.

Finally, two alternative views are considered:
- Transformers lack embodied experiences and hierarchical planning capabilities.
- Transformers are limited by their bounded compute.

### Strengths
Strengths:

1. The paper has a clear statement and reasoning
1. Given the difficulty to define AGI it is nice that two different approaches are considered, one with the extended Church-Turing thesis and one with Hutter's AIXI agent.
1. The topic lies in the heart of the field and independently of the success of the authors' arguments it will probably trigger many discussions and draw more attention to it.

### Weaknesses
1. The paper considers a polynomial overhead to be acceptable in terms of efficiency in the extended CT thesis and in the attention mechanism which in general is quadratic on the number of input tokens. This could be both a practical and theoretical issue since assuming an agent needs to constantly process input which is arriving on pace linear to its size, then this poses a limitation on the input and CoT size. This could be a topic by itself as one should consider the different approaches to avoid quadratic space and the limitations they pose to the computational power of the agent as well as a study on the physical systems. Nevertheless, it is an alternative position that the quadratic time attention could be an inherent limitation of transformers that may not be present on other physical systems.  

1. The first alternative view which is based on the interview of Yan LeCun does not seem to directly question the capabilities of transformers. Instead, he argues specifically against using only LLMs to achieve AGI. Also the combination of agents mentioned in the interview which could lead us closer to AGI are comparable to the framework described in section 4.3 with the exception of the idea of using the transformers as UTMs.

### Questions
No questions.

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
The paper posits that the Transformer architecture is a viable path to AGI. It supports this strong claim with three main theoretical arguments: (1) Transformers are Turing-complete and can simulate probabilistic universal computers, enabling them to perform any computation, including meta-algorithmic tasks. (2) The Extended Church-Turing Thesis implies that if AGI is physically possible, a Transformer can in principle replicate it. (3) Transformers can serve as tractable, practical approximations of theoretically optimal but uncomputable AGI agents like Solomonoff's Inductor, Levin's Searcher, and Hutter's AIXI. The paper culminates in a novel proposal for a two-Transformer framework to approximate the AIXI agent.

### Strengths
Builds on principles from theoretical computer science and algorithmic information theory, providing a formal and rigorous framework for AGI discussions rather than relying solely on empirical evidence. 

integrates insights from diverse research areas, linking Transformer computational theory with practical methods for approximating Solomonoff Induction (SI) and Levin Search (LTS), leading to a distinctive AIXI approximation proposal. I appreciated the multidisciplinary stance that this paper posits its arguments on.

Addresses alternative, rather contentious, viewpoints, including concerns about embodiment and limited computational resources, showing awareness of opposing arguments despite providing only brief counterpoints.

### Weaknesses
The paper's primary weakness is its failure to adequately address the vast gap between the theoretical capabilities of idealized "tranformers" and the practical realities of trained LLMs. It heavily relies on Turing completeness proofs without discussing their critical, and likely invalidating, assumptions for standard models (e.g., hard attention, arbitrary precision)

The big claim about a "single Transformer" was challenged by recent work distinguishing between fixed models (computationally equivalent to finite-state machines) and evolving lineages of models (computationally equivalent to interactive TMs with advice). I think the paper would be amiss without incorporating this nuance. Doing so would make the argument more precise and defensible in my opinion.

Being a position paper, the authors should add a section on broader impact and ethical considerations, especially around this contentious topic. The dual-use nature of AGI research should be acknowledged. The authors should should discuss what safeguards might be necessary for the powerful, general-purpose systems they envision.

### Questions
Further to my review of the weaknesses of the paper, I think I would be interested in knowing what safeguards do the authors think might be necessary for the solution that they have proposed? Do you think a more concrete evidence should be provided that transformers can function as an environment modeler. Many luminaries in the field have attested that LLMs lack this capability.

### Presentation
3
