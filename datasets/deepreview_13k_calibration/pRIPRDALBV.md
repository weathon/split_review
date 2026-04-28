# Open-World Planning via Lifted Regression with LLM-based Affordances for Embodied Agents

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Open-world planning is crucial for embodied AI agents that must make decisions with incomplete task-relevant knowledge. In fact, the main challenges lie in reasoning about objects and their affordances that are unknown to the agent. Large Language Models (LLMs), pre-trained on vast internet-scale data, have emerged as potential solutions for open-world planning. However, LLMs have limitations in long-horizon planning tasks and face problems related to interpretability, reliability, and cost-efficiency. Symbolic planning methods, on the other hand, offer structured and verifiable approaches to long-horizon tasks, but often struggle to generate feasible plans in an open-world setting. In this work, we propose a novel approach, called LLM-Regress, which combines the strengths of lifted symbolic regression planning with LLM-based affordances. The lifted representation allows us to generate plans capable of handling arbitrary unknown objects, while regression planning is the only planning paradigm that guarantees complete solutions using lifted representations. For such tasks, we leverage LLMs to supplement missing affordances knowledge for unknown objects. The regression nature of our approach enables the agent to focus on actions and objects relevant to the goal, thus avoiding the need for costly LLM calls for every decision. We evaluate our approach on the ALFWorld dataset and introduce a new ALFWorld-Afford dataset with higher planning complexity and more affordances types. The empirical results demonstrate that our method outperforms existing approaches in terms of success rates, planning duration, and number of LLM Tokens. Finally, we show that our approach is resilient to domain shifts in affordances and generalizes effectively to unseen tasks. This work underscores the importance of integrating symbolic reasoning with LLM knowledge for open-world decision-making in embodied AI.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Manuscript presents an approach of combining canonical symbolic planning methods with LLMs to tackle the open-world challenge to classic planners and the inability of long-horizon planning of LLMs. The key idea is to replace all hand-crafted affordance functions with queries to LLMs, while still using the pre-defined list of objects and predicates (perception or grounding is assumed to be offered by the environments). The proposed method is evaluated against several LLM planner counterparts and its own ablations on ALFWorld and a variant.

### Strengths
+The manuscript is mostly clear and well-written. The research topic (open-world planning) is of interest to the NeurIPS community.

+The proposed method is technically sound. Indeed the component that requires most ontology engineering in canonical planning frameworks is the affordance functions and it makes sense to replace it with LLM queries. While I believe the perception part is also complicated and can be replaced as well, given the benchmark (ALFWorld) offers ground truth symbolic observations, I think it is ok to leave it as is.

+The empirical results look strong, as compared to the picked LLM planners. The ablation studies can be relatively simple but it delivers the points on the crucial roles of affordances.

### Weaknesses
My major concerns rely on the evaluation side:

-More benchmarks should be adopted. Albeit the reputation of ALFWorld in planning and LLM agents, it is not very "open-world" as the number of objects, functionalities, tasks, etc, can be relatively limited. My suggestion is to extend to some truly open-world environments, ex. Minecraft [1]. It adds more complexity as the environment is more volatile and necessitates much more background knowledge. I would like to see some results on this benchmark.

-More baselines, especially LLM planning methods should be compared. Notably, the community has already noticed that straightforward planning with LLMs does not usually work very well and several remedies have been proposed: interactive planning with self-check or reflections[1], adding memory as a means of learning[2], retrieval-augmented planning with LLMs[3], etc. I think [1] also has results on ALFWorld. A more comprehensive comparison of these approaches could help strengthen the merit of the proposed method.

-Misc: I found the font size of the graphics in the manuscript can be too small to see clearly.

### Questions
See "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work tackles open-world planning challenges for embodied AI, focusing on reasoning about unknown objects and affordances. The proposed approach, “LLM-Regress,” combines symbolic planning with knowledge from Large Language Models (LLMs) to improve efficiency and long-horizon planning. While LLMs provide affordance knowledge, symbolic planning offers structure but struggles in open-world tasks. LLM-Regress leverages LLM affordances selectively, reducing reliance on costly LLM calls and improving planning effectiveness. Tested on ALFWorld and a new, more complex ALFWorld-Afford dataset, LLM-Regress shows better success rates, faster planning, and improved generalization to unseen tasks. This approach emphasizes the benefits of blending symbolic reasoning with LLMs for open-world AI.

### Strengths
1. Rigorous formal reasoning may help ensure the safety and interpretability of planning.
2. Intuitively, reasoning backward from the conclusion could potentially simplify the process.

### Weaknesses
I am not very familiar with research on formal reasoning. However, from the perspective of developing large language models (LLMs) as agents, I feel that there is already a significant amount of similar work in this area, and the problem addressed in this paper does not appear to be particularly novel. I don’t believe that strict formal reasoning is a requirement for completing tasks in open-world environments. 

1. The paper emphasizes that this method is for “open-world planning,” but it is unclear to me how this approach relates to open-world concepts. How does the paper define “open-world”? Is the evaluation environment used, ALFWorld, truly an open-world environment? In my view, open-world scenarios often imply that the objects or predicates within the environment are unknown or theoretically infinite. How would this method function in such a scenario, and what would the complexity be?
2. What is “grounding”? The paper lacks a clear definition.
3. The assumption that “the affordances of the objects are unknown to the agent” is puzzling. If the next action or subgoal is determined primarily by prompting a large model, what is the fundamental distinction between this approach and previous works like SayCan [1]?
4. Figure 1 is not very clear. I suggest adding a more detailed caption to explain concepts such as “Lifted Regression” and “Grounded Regression” so that readers don’t have to refer to the main text for clarification. 
5. The experiments are only conducted in ALFWorld, which limits the paper’s persuasiveness.
6. The DEPS [2] framework has also been tested on ALFWorld. A discussion and comparison with DEPS in relevant sections would strengthen the paper.

### Questions
Refer to weakness.

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
4

### Summary
This work proposes a lifted regression planning method that consists of an LLM-prompting step to do partial grounding while expanding the search graph. Specifically, the LLM is used for grounding affordance-related propositions. While the proposal seems interesting, the motivation and the assumptions made are not very clear, which makes it a bit hard to assess the overall contribution.

### Strengths
- It might be smart to use LLMs to ground the affordance information, as affordances are relatively domain-independent properties, though some care should be taken as these affordances should be compatible with the agent (e.g., SayCan).

### Weaknesses
 - The overall weakness is that while we can more or less understand the general pipeline of the method, the motivation for doing so, the assumptions, and its limitations are not clear. Please see the below points for concrete examples.
- The comparison with the grounded planner casts a doubt on me, as I don’t understand the reason behind the difference between the two, and it’s not explained in the paper.

> LLMs do not require structured inputs or explicit knowledge modeling, which theoretically makes them well-suited for open-world planning

I don’t quite get why this would make LLMs *theoretically* well-suited.


> However, they require complete problem descriptions, which are not readily available in open-world scenarios.

> While classical planning guarantees completeness and consistency in its solutions, it requires detailed domain descriptions, which may be unrealistic in real-world settings.

There are some works that focus on learning abstractions to be used for planning [1-8].


> Our approach provides complete and verifiable plans, guaranteeing the discovery of a feasible plan if one exists.

Complete with respect to the affordance performance of LLMs?

The definition of \theta_o and \theta_a—grounding functions—are vague. It’s not clear what kind of input they take and output as a result. I can only guess.

> Rather than have predefined affordances, we want to extract them from LLM.

It would be nice to motivate this argument. Also, later in the experiments:

> The main affordances reasoning in this environment include determining whether an object can be heated, cooled, cleaned, or turned on.

This seems like pre-defining affordance classes.

I believe one implicit assumption is that \theta_o should also output the labels of objects, e.g., egg_1, microwave_2, etc. Does this mean that there is a pre-defined set of object names? 

We assume observation predicates \mathcal{P}_o are given but not affordance predicates \mathcal{P}_a. Why? More specifically,

> \mathcal{P}_a cannot be grounded by observation alone, but it is still required to check an action is feasible for some sub-goal.

why can we ground \mathcal{P}_o—for instance, p(hold(potato_1) | image)—but not p(canHeatStuff(microwave_1) | image)?
Relatedly, from the abstract,

> The lifted representation allows us to generate plans capable of handling arbitrary unknown objects,

If \mathcal{P}_o, which is the set of grounded propositions, is already given, then we don’t have any unknown objects?

I don’t understand how it is possible to get better results than the LLM-Affordance+FD baseline. Both the proposed method and this baseline use the affordance information generated from the LLM. So if I get this correct, the only difference in results should possibly be the planning times, since the FD should get correct plans if the operators are correct. The only way we get a difference in these results means that the domain definition should be different, which in turn means operators and/or the used propositions are different, which would further mean that the affordance-related propositions generated by the LLM are not consistent in these two approaches, LLM-regress and FD+LLM Afford.

## Some typos
- Citation typo to Russell and Norvig, AIMA, Lines 189, 192.
- Possibly typo, Line 212, “can be regressed *no* longer?”

### Questions
> LLMs do not require structured inputs or explicit knowledge modeling, which theoretically makes them well-suited for open-world planning

I don’t quite get why this would make LLMs *theoretically* well-suited.


> However, they require complete problem descriptions, which are not readily available in open-world scenarios.

> While classical planning guarantees completeness and consistency in its solutions, it requires detailed domain descriptions, which may be unrealistic in real-world settings.

There are some works that focus on learning abstractions to be used for planning [1-8].


> Our approach provides complete and verifiable plans, guaranteeing the discovery of a feasible plan if one exists.

Complete with respect to the affordance performance of LLMs?

The definition of \theta_o and \theta_a—grounding functions—are vague. It’s not clear what kind of input they take and output as a result. I can only guess.

> Rather than have predefined affordances, we want to extract them from LLM.

It would be nice to motivate this argument. Also, later in the experiments:

> The main affordances reasoning in this environment include determining whether an object can be heated, cooled, cleaned, or turned on.

This seems like pre-defining affordance classes.

I believe one implicit assumption is that \theta_o should also output the labels of objects, e.g., egg_1, microwave_2, etc. Does this mean that there is a pre-defined set of object names? 

We assume observation predicates \mathcal{P}_o are given but not affordance predicates \mathcal{P}_a. Why? More specifically,

> \mathcal{P}_a cannot be grounded by observation alone, but it is still required to check an action is feasible for some sub-goal.

why can we ground \mathcal{P}_o—for instance, p(hold(potato_1) | image)—but not p(canHeatStuff(microwave_1) | image)?
Relatedly, from the abstract,

> The lifted representation allows us to generate plans capable of handling arbitrary unknown objects,

If \mathcal{P}_o, which is the set of grounded propositions, is already given, then we don’t have any unknown objects?

I don’t understand how it is possible to get better results than the LLM-Affordance+FD baseline. Both the proposed method and this baseline use the affordance information generated from the LLM. So if I get this correct, the only difference in results should possibly be the planning times, since the FD should get correct plans if the operators are correct. The only way we get a difference in these results means that the domain definition should be different, which in turn means operators and/or the used propositions are different, which would further mean that the affordance-related propositions generated by the LLM are not consistent in these two approaches, LLM-regress and FD+LLM Afford.

## Some typos
- Citation typo to Russell and Norvig, AIMA, Lines 189, 192.
- Possibly typo, Line 212, “can be regressed *no* longer?”

# References
1. Konidaris, George, Leslie Pack Kaelbling, and Tomas Lozano-Perez. "From skills to symbols: Learning symbolic representations for abstract high-level planning." Journal of Artificial Intelligence Research 61 (2018): 215-289.
2. James, Steven, Benjamin Rosman, and G. D. Konidaris. "Autonomous learning of object-centric abstractions for high-level planning." Proceedings of the The Tenth International Conference on Learning Representations. 2022.
3. Ugur, Emre, and Justus Piater. "Bottom-up learning of object categories, action effects and logical rules: From continuous manipulative exploration to symbolic planning." 2015 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2015.
4. Ahmetoglu, Alper, et al. "Deepsym: Deep symbol generation and rule learning for planning from unsupervised robot interaction." Journal of Artificial Intelligence Research 75 (2022): 709-745.
5. Asai, Masataro, et al. "Classical planning in deep latent space." Journal of Artificial Intelligence Research 74 (2022): 1599-1686.
6. Chitnis, Rohan, et al. "Learning neuro-symbolic relational transition models for bilevel planning." 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2022.
7. Silver, Tom, et al. "Predicate invention for bilevel planning." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 10. 2023.
8. Shah, Naman, et al. "From Reals to Logic and Back: Inventing Symbolic Vocabularies, Actions and Models for Planning from Raw Data." arXiv preprint arXiv:2402.11871 (2024).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper addresses open-world planning for embodied AI agents facing incomplete task knowledge. It introduces LLM-Regress, which combines symbolic regression planning with LLM-based affordances to generate effective plans for unknown objects. Tested on ALFWorld and a new ALFWorld-Afford dataset, LLM-Regress outperforms existing methods in success rates, planning duration, and token usage, while also being resilient to affordance changes and generalizing well to new tasks.

### Strengths
1. The paper is clearly written and well-organized.
2.  The empirical evaluations conducted on both the ALFWorld and ALFWorld-Afford datasets are thorough and well-structured.
3. Symbolic reasoning and LLM are well combined, and the design is sophisticated.

### Weaknesses
While the LLM-Regress method is innovative, its performance is primarily evaluated within the confines of the ALFWorld datasets. More diverse environments or real-world scenarios could be explored to assess generalization capabilities. Including benchmarks against additional datasets or different planning contexts would strengthen the findings.

### Questions
No more questions.

### Soundness
3

### Presentation
3

### Contribution
3
