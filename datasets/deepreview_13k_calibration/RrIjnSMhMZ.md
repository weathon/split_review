# Watchmaker Functions and Meta Specification of Open-Ended Learning Systems

- Decision: Reject
- Avg Score: 2.50
- Scores: 1, 5, 1, 3

## Abstract
Open-ended learning systems aim to foster the continuous evolution of increasingly capable agents through the dynamic generation of novel challenges. The efficacy of these systems is fundamentally influenced by two critical factors: the design of the underlying system, which delineates the space of possibilities, and the open-ended algorithms that drive ongoing progress within this space. Current approaches to system design rely on explicit specification, where state spaces and evolution functions are fully defined at design time, often leading to prohibitive design complexity as systems scale. To address this challenge, we propose an alternative design principle termed *meta specification*. This approach defines systems implicitly through constraints, utilizing *watchmaker functions*—generalized stochastic evolution functions—coupled with verification routines to perform system evolution. Meta specification principles have the potential to significantly expand the space of possibilities while reducing design complexity, thereby enhancing the potential for open-ended learning. We demonstrate the viability of this principle through an illustrative implementation that co-evolves robot morphologies and robotic tasks, showcasing its capacity for emergent novelty and highlighting the shift in focus towards verification in system design.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
2

### Summary
The author’s propose an alternative approach to tackling design problems to mitigate the limitations of defining explicit specifications (e.g. a reward signal). Instead, the authors argue for a framework which specifies meta constraints to evaluate designs against to verify their feasibility in practice. They describe an extensive abstract framework and propose the concept of “watch maker functions” as a means of handling meta specifications. They then show an example scenario using a larger language model as a watchmaker function for generating robotic designs. This work is motivated in advancing the development of open-ended learning systems that generate novel challenges to push the limits of learning agent systems.

### Strengths
Overall the manuscript reads quite coherently. The author’s proposition of defining constraints as opposed to target specifications is an interesting approach for addressing design problems. By having fewer specifications, it seems plausible the authors framework could offer nove alternatives for addressing a number of hard problems.

### Weaknesses
 - Plagiarism of existing ideas, see Details Of Ethics Concerns section
- Lack of novelty
- No empirical results

### Questions
- What are the potential theoretical benefits of having a watchmaker function?
- What are other more tangible examples of watchmaker functions? 
- Are the costs the authors mean when they say they “omitted any training procedure”? If this is directly related to having used gpt-4, this seems a notable limitation of the idea of watchmaker functions if you must rely on larger language models to have a meaningful function for this purpose.

### Soundness
2

### Presentation
1

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
The paper introduces a novel framework for the design of Open-Ended Learning Systems (OELS), proposing an alternative design principle termed meta specification. Instead of relying on explicit specification, where state spaces and evolution functions are predefined, this approach uses constraints to define systems implicitly. Central to the framework is the concept of watchmaker functions—stochastic evolution functions coupled with verification routines to foster system evolution within generalized representation spaces. The authors showcase an implementation that co-evolves robotic morphologies and tasks, leveraging a LLM as a watchmaker function.

### Strengths
The meta-specification approach presents a unique perspective on OELS, shifting from an explicit to an implicit design, which could simplify design complexity while expanding the space of possibilities.

Additionally, the paper formalizes a unified framework for OELS, creating a common language that facilitates the comparison of different OELS approaches.

The implementation of co-evolving robotic agents and tasks showcases the potential of meta specification and watchmaker functions to create emergent behaviors without requiring highly specific design constraints.

The use of LLM-based watchmaker functions offer a promising approach for larger-scale OELS implementations.

### Weaknesses
I think the paper is interesting and it's a valuable addition to the open ended learning literature. However, I think the contributions of the paper could be made clearer. For example, compared to POET, can the proposed system solves anything that POET can not or is it mostly just a generalized formulation of a class of algorithms. 

Additionally, for a paper on open-endedness, the paper does not really show any open ended learning. The authors note that "Most notably, we have omitted any training procedure (due to the cost and compute requirements), which is crucial for the evolved robots to become increasingly capable. Furthermore, a control mechanism should be integrated to ensure continuous progress." but I think showing an actual more open-ended learning process would have made the paper more impactful. 

Minor comments:
- Typo: “representation sapce” in the watchmaker function definition

### Questions
Is it always possible and feasible to run the verification process? How difficult is it to design this part in comparison to traditional explicit specification?

Figure 5 only show very low generation numbers. Why was the system not run for longer?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces "meta specification", a novel approach to designing open-ended learning systems. While current systems rely on explicitly defining all spaces and functions at design time, which becomes prohibitively complex at scale, meta specification defines systems implicitly through constraints using "watchmaker functions" - generalized evolution functions coupled with verification routines. The authors propose Large Language Models as potential watchmaker functions and demonstrate their approach through a system co-evolving robot morphologies and tasks.

### Strengths
The strength of the paper is that it offers a practical solution to a significant scaling problem in open-ended learning systems.

### Weaknesses
- Plagiarism of existing ideas, see Details Of Ethics Concerns section
- Lack of novelty
- No empirical results

### Questions
No question.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a general framework for open-ended (co-)evolution. They first formalize existing work in that domain under the term "open-ended learning systems". Then they propose "watchmaker" functions to enable evolution to operate over arbitrarily flexible representations (including language), rather than being constrained to what they call "explicit specifications". 

A "watchmaker function" seems to designate any mutation operator with an acceptable chance of producing viable output, together with validation procedures to ensure that the mutated outputs are viable under the requirement of the experiment.


They then describe early experiments to illustrate these ideas in a 3D physical simulation, co-evolving both environments (tasks) and agents, based on language descriptions and large language models.

### Strengths
Open-endedness is an important subject that deserves more attention.

The experiments, although minimal, seem to point towards some novelty (I am not aware of any experiment co-evolving both tasks and agents, in a 3D world, with language descriptions and LLM-based evolution operators) and hint at potentially interesting future work.

The paper is very well written, both in terms of content and of the very pretty presentation.

### Weaknesses
**Main contribution**

As I understand it, the first 8 pages of the paper can be summarized as follows:
 
"If we want to explore spaces defined by more flexible representations than fixed-shape tensors, such as language, we need to add some checks to ensure the resulting proposals are feasible".

I don't disagree! Does it require a whole paper, with considerable novel notation and terminology?

To illustrate the problem, in line 302 we read:

> Whereas an explicitly specified system completely describes all possible states as XΘ = {x(θ) | θ ∈ Θ}, meta specification implicitly
defines the state space through constraints: XR = {x ∈ V | x |= R}. Here V denotes the universal
set, which conceptually refers to the set of all possible elements under consideration.

If the system is to be evolvable at all, it *must* be represented through some kind of parametrization. As such, in reality, both of these sets imply a "theta". The former one seems to imply that the explicitly defined set Cap_Theta contains only, and all, valid specifications, whereas in the latter we need additional checks to ensure validity. But almost all non-trivial open-endedness experiments are already of the second kind, and definitely involve such checks!

For example, systems based on Karl Sims' virtual creatures (1994!) can represent any non-cyclic morphology, including infinitely many unfeasible ones, and as a result, require filtering to reject unfeasible agents (e.g. self-intersecting). It seems superfluous to call tree operations followed by sanity checks "watchmaker functions". More recently Lehman et al. (arxiv 2206.08896) proposed to use LLMs to mutate and evolve simple robots represented in code, which of course required some a posteriori filtering.

Thus, the contribution of the paper seems unclear.

**OELS framework**

The authors also attempt to provide a formal specification of "open-ended learning systems", but this formalization seems confusing to me. It is not obvious what should be regarded as part of the "evolution functions", and what should be part of the "control system". 

This is evident in the authors' own chosen illustrative example, namely Wang et al.'s POET. They define the "Control mechanism" as consisting of the minimum criterion and the novelty check. But these are just how new environments are created and selected, i.e. the environment "evolution function" ! (In fact the original POET paper defines this as "Mutate_envs", algorithm 3 in the appendix)

**Experiments**

The experiments bear strong resemblance to those of Faldor et al. 2024 (OMNI-EPIC: https://arxiv.org/abs/2405.15568 ), which also use LLMs and PyBullet. The main addition IIUC is that now the agent co-evolves with the task (this would potentially be a valid contribution if the experiments were the central focus of the paper, which doesn't seem to be the case here).

Yet Faldor et al. is apparently not cited in this submission, which seems to be a serious oversight. 

[UPDATE] I see that Reviewer sx3L has also noted the strong similarity and the lack of citation. Even if this submission is from the same team, Faldor et al. 2024 must be cited!

**Minor:**

In line 334, shouldn't "generalized transformation" read "viability" or some such single noun to match "Stochasticity" ? (authors use the term 'viable' in line 343)

l331: sapce -> space

### Questions
Why do we need additional formalism, notation and terminology to describe what has been done for decades, namely, evolution over representations sufficiently flexible to produce non-viable outputs?

What is the exact difference between the "evolution function" and the "control mechanism", and can you update your description of POET to match the original paper?
 
Could you please cite Faldor et al. 2024 and briefly specify the difference?

### Soundness
3

### Presentation
4

### Contribution
1
