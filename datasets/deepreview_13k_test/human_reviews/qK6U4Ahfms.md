# OpenCity: A Scalable Platform to Simulate Urban Activities with Massive LLM Agents

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
Agent-based models (ABMs) have long been employed to explore how individual behaviors aggregate into complex societal phenomena in urban space. Unlike black-box predictive models, ABMs excel at explaining the micro-macro linkages that drive such emergent behaviors. The recent rise of Large Language Models (LLMs) has led to the development of LLM agents capable of simulating urban activities with unprecedented realism. However, the extreme high computational cost of LLMs presents significant challenges for scaling up the simulations of LLM agents. To address this problem, we propose OpenCity, a scalable simulation platform optimized for both system and prompt efficiencies. Specifically, we propose a LLM request scheduler to reduce communication overhead by parallelizing requests through IO multiplexing. Besides, we deisgn a ``group-and-distill'' prompt optimization strategy minimizes redundancy by clustering agents with similar static attributes. Through experiments on six global cities, OpenCity achieves a 600-fold acceleration in simulation time per agent, a 70\% reduction in LLM requests, and a 50\% reduction in token usage. These improvements enable the simulation of 10,000 agents’ daily activities in 1 hour on commodity hardware. Besides, the substantial speedup of OpenCity allows us to establish a urban simulation benchmark for LLM agents for the first time, comparing simulated urban activities with real-world data in 6 major cities around the globe. We believe our OpenCity platform provides a critical infrastructure to harness the power of LLMs for interdisciplinary studies in urban space, fostering the collective efforts of broader research communities. 
Code repo is available at \hyperlink{https://anonymous.4open.science/r/Anonymous-OpenCity-42BD}{https://anonymous.4open.science/r/Anonymous-OpenCity-42BD}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper describes an approach	where LLM agents are used to simulate individual behaviour in large (city-scale) simulations of people.	The proposed platform uses LLM agents that can adapt their behaviour depending on context and memory. This is different to the classic agent based approach for this type of simulation where behaviours are static over time. 
The development of the platform is one of the main contributions of the work, and the development of a user-friendly web interface is another contribution highlighted by the authors. From a machine learning perspective, the proposed “group-and-distill” approach to reduce LLM usage is the main contribution of the work, essentially a clustering approach before prompting the LLM for each cluster (as opposed to prompting an LLM for each individual).

### Strengths
The use of a LLM for the purpose of larger scale population modelling appears to be novel, and the suggested group-and-distill approach enables this idea, with relatively low hardware resources. 
Overall, considerable effort appears to have gone into development of the system. The system could be an interesting resource for research in complex systems.

### Weaknesses
The paper has quite a broad focus, like an overall project report. For a venue like iclr, it would have been better to focus on the specific contributions in machine learning, and to provide more technical details rather than an overall description of architecture and usability aspects as the main contributions. In its current form, ICLR does not appear to be the right venue for the work as it is presented.

The work lacks depths in aspects that I would see essential for any ML paper: for example the group-and-distill concept is introduced, but the paper is very sparse in detail of the specific algorithms. Similarly it would have been interesting to see what are the initial prompts and the optimised prompts, in contrast. 
Any details comparing to the original approach without group-and-distill / ablation would have been an improvement too. 

Moreover it didn’t become clear to me what LLM has been used or how was it trained, and how do LLM outputs influence agents’ behaviours.

Finally, the paper mentioned at the beginning the explainability of ABM as an advantage over black box neural network approaches. with the lack of detail on how the actions are influenced by the LLM or how the LLM are trained or fine tuned, the proposed model has the same disadvantage as any other neural network model.  

Minor presentation issues:

"Agent-based models (ABMs) were first introduced to urban studies in the seminal work of Thomas Schelling about 50 years ago Schelling (2006)"
- if the work referenced was from approx 50 years ago, Schelling 2006 is the wrong reference. I believe the correct year would be 1978.
- there are two	kinds of citations, narrative (like the one in the sentence), and parenthetical (Schelling, 2006). It doesn't make sense to use	narrative style	when it doesn't fit into the sentence structure. In LaTeX with natbib, this is the difference between \citet and \citep. 
The referencing is an issue throughout the paper.

### Questions
While the approach and system are interesting, I don't see this paper as a good fit for ICLR, in its present form, and suggest it be rejected. 
Some of my questions:

- What LLM model is used in the simulation, and how was it trained?
- How do the prompts look before and after applying the group-and-distill approach?
- What is the output of the LLM, and how does it influence agent behaviour?
- To what extent is the group-and-distill technique generalisable beyond urban simulations?
- How does the platform maintain long-term consistency in agent behaviour, given the variability in LLM responses?
- What mechanisms are in place to manage or correct for inconsistencies in agent behaviour across prompts?
- Is there an evaluation of the platform’s accuracy in simulating real-world behaviours compared to traditional ABMs?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The recent rise of Large Language Models (LLMs) has led to the development of LLM agents capable of simulating urban activities with unprecedented realism. Nevertheless, the extreme high computational cost of LLMs presents significant challenges for scaling up the simulations of LLM agents. With this motivation, this paper introduces OpenCity, a scalable simulation platform designed to efficiently simulate urban activities using a large number of LLM agents. The platform incorporates innovative techniques, including LLM request scheduler and a group-and-distill prompt optimization strategy, to reduce the computational overhead of simulating LLM agents significantly. OpenCity achieves a 600-fold speedup and reduces both LLM requests and token consumption. Extensive experiments on six global cities verify the platform's scalability and its capability to replicate real-world urban dynamics.

### Strengths
Strengths
1.	This paper introduces a scalable platform for urban simulations using LLM agents, which addresses a growing need for realistic human behavior modeling in urban environments.
2.	This paper shows a high quality of presentation. The paper is technically sound and the research question is clear. The optimizations, particularly the LLM request scheduler and prompt optimization strategies, demonstrate clear performance benefits. The experimental results showing a 600x speedup and significant resource savings are compelling.
3.	The paper is generally clear and well-structured. It provides a clear problem statement, introduces the proposed framework, and highlights key findings.
4.	The contribution of the paper is relevant for LLM agent. The results of this paper is interesting and significant in LLM agent simulation. The proposed OpenCity framework is relevant for urban planning and policy-making. The development of a web portal that allows researchers to configure and visualize simulations without requiring programming skills is a valuable addition, making the platform accessible to a broader audience.

### Weaknesses
1.	The introduction part fails to convey to the reviewers what is the motivation and novelty in this paper. In fact, the authors should add more previous work on LLM agents based simulation platform. The problem this paper addresses and the reason why this paper uses system-level LLM request scheduler and prompt-level “group-and-distill” strategy to solve the problem of scalability should be further explained. Besides, the contribution the authors listed in the introduction section is inaccurate，the authors should focus on the system-level LLM request scheduler and prompt-level “group-and-distill” strategy. Thus, I would recommend a revision for the introduction section in this paper.
2.	This paper utilizes Group-and-Distill Meta-Prompt Optimizer to classify similar agents to reduce computational complexity, which indeed improve efficiency. However, this may overlook differences between individuals, so the reason why this method can preserve the distinctive characteristics of the agents, as show in the experimental part, should be further explained in the method section。
3.	Figure 2 illustrates the principle of Group-and-Distill Meta-Prompt Optimizer. However, it seems difficult to follow. It is more intuitive to add an example to explain how IPL works. 
4.	There lacks explanation for the reason why the proposed method IPL is superior to conventional prototype learning. Moreover, the principles for setting the value of M and T in IPL should be further illustrated.
5.	Experimental part: the authors should add an explanation of the indicators including JSD, T1 and bold the important data in Table 2 . Similarly, Table 3 also requires revision. The metrics of RMSE of New York和San Franciscoin are not displayed in Table 3, which seems a little bit confusing, the authors need to provide explanations. 
6.	The authors should pay attention to the standardization of citations throughout the paper, especially in introduction and related works section. For example, “conventional prototype learning methods...”(line305), “the baseline represents the simulation time without optimization” (line 389), “we analyze the performance of the Generative Agent and EPR Agent ”(line 450).
7.	The authors should carefully proofread the manuscript for typos and formatting issues. There exists some typos: in the abstract: “we deisgn a “group-anddistill” prompt optimization”, “where τqα is is the proportion”(line 687) , etc.

### Questions
1.	Why did the authors conduct additional assessment on merely two cities: New York and Paris using the GPT-4o model in Table 2? Rather than conducting experiments in all six cities like 4o-mini?
2.	As for the experimental setup, do the following parameters: exploration rate ρ= 0.6, exploration-return trade-off parameter γ = 0.21, waiting time distribution parameters τ = 17 affect the results？
3.	In line 389，what does baseline mean? As the citation is missing, the reviewer guess whether it means the method in Park et al. (2023)？If not, comparative experiments on the Park et al. (2023) method should be added.
4.	 Why the result of baseline method is 50s/agent when the number of agents is very small in Figure 3, such as merely a single agent?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper is considering the problem of agent-based modeling of environments such as cities. Such models had been previously used with the agents performing relatively simple behaviors. While LLMs open new opportunities for controlling the behaviors of the individual agents, their computational cost presents a significant scaling problem. 

The paper describes an architecture that enables the parallelization of the agents, to allow the modeling the daily activities of a city with 10,000 agents. The architecture appears to be based on an efficient polling model of the LLM, as well as the development of a prompting model called "group-and-distill". The application of these models show a more than 600-fold increase.

### Strengths
* The overall goals of the paper, of capitalizing on the abilities of LLMs to achieve a better ABM model of cities, as well as addressing the scaling problems, are laudable.

### Weaknesses
* Achieving a more than 600 fold speed increase in terms of an improved process scheduler and I/O scheduler can be probably seen as "debugging", rather than research result, and very likely has nothing to do with the LLM. 
* It seems that the very considerable computational effort of an LLM can only achieve an approximate parity with the much cheaper rule based efforts. This is understandable, as description of the behavior of the agents described in the paper follows the same position based rules that the ABM models historically use. As there is no consideration of language or other type of reasoning, the paper does not make it clear what type of benefits one would expect from LLMs.
* The only part of the paper that has a connection to the topic of this conference is the way in which the "group-and-distill" model is proposed to achieve the simulation of multiple agents with one prompt. However, there is very little about this technique in the paper proper, so it is difficult to form a judgement.

### Questions
* The paper spends comparatively less effort on explaining what kind of benefits do we expect from an LLM-based ABM. For instance, we can try to model thought processes of the humans, or their communication. Does the choice of this modeling impact the proposed techniques?

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
ABM and LLM is leveraged to develop one platform for open city modeling and planning. It is a nice simulation platform and the paper provides application scenarios. Concretely, 

1. This paper combines agent-based models with large language models to develop the OpenCity platform for simulating urban activities. It reduces simulation computational costs through IO multiplexing and the "group-and-distill" prompt optimization strategy.
2. Through experiments conducted in six major cities worldwide, OpenCity demonstrates a 635 plus increase in average simulation speed per agent, along with a 70% decrease in LLM requests and a 50% reduction in token usage. The time savings are mainly concentrated in the LLM response wait time and the CPU multiplexing process.
3. The OpenCity platform proposed in this paper achieves the first benchmark testing for LLM agent-based urban activity simulation research.

### Strengths
The paper give a detailed introduction of the novel methods and the real outcome.

1. Originality: The paper presents a novel approach by integrating Large Language Models with agent-based modeling to simulate urban activities. There has been limited research on combining LLMs with agent-based models, and even less so in the context of large-scale urban activity simulations. By using IO multiplexing and the "group-and-distill" prompt optimization strategy to reduce the computational cost of simulations, this paper has made the application of LLMs in large-scale urban activity simulations possible.
2. Quality: The research is well organized with a clear methodology and experiments conducted in real cities data. The results show notable improvements in both simulation efficiency and accuracy, confirming the effectiveness of the proposed platform.
3. Clarity: The paper is written in a clear and concise manner; it is easy to understand through the explanation of figures
4. Significance: This paper establishes a benchmark for LLM agent-based urban activity simulation research. This paper also provides a scalable framework for simulating urban dynamics.

### Weaknesses
There is a lack of theoretical contribution, overall, rather it is an application tool development with leveraging well established tools. It may not fit ICLR the best though not out of scope at all. Further,

1. Some parts of the main body text are not rigorous enough. For example, Equation 1 is missing a parenthesis, and the IPL method is mistakenly labeled as the LPL method in Figure 2.
2. This research has high requirements for data quality. Additionally, despite significantly improving computational efficiency and reducing costs, the platform may still require substantial computational resources.
3. When simulating cities in different countries, the dynamic properties to be considered should not be entirely the same, and some of the assumed static properties may also change during the simulation process.

### Questions
1.	It seems that the formula in Equation 1 misses a parenthesis?  And it can also be split into two separate equations.
2.	In Section 3.2, the content of Figure 1(b) is introduced, however, the Figure 1(a) is discussed in Section 4.1. Is this logical? It is suggested to swap the subtitles of the figures for better coherence.
3.	This paper categorized the CPU task as ”local IO”, offload it to available cores for computation through a multi-core parallel scheme, and then return the result to the designated agent upon completion of the computation.
4.	Is there an increase in CPU task scheduling time? How does it compare to the time saved in saving#3?
5.	The paper states that "A conventional approach is to reuse the generated result of a single LLM request across multiple agents, and this approach presents two significant drawbacks." However, it only describes one drawback.
6.	The paper introduces Figure 2(a) first, which prompts readers to check the content of Figure 2(a). However, they will encounter a series of unexplained equations, which could cause confusion. The paper cites Figure 2 only in the subsequent description, and the explanation of Figure 2(a) is found only in the explanation of the methodology of Figure 2 in the main text. Is it possible to optimize this part of the description?
7.	From the subsequent description in the main text, it is understood that Figure 2(a) is introducing the IPL method, but in the figure is labeled as the LPL method.
8.	How is the threshold T in the IPL method of this paper determined?
9.	Are the baseline in Figure 3 increased simulation response time due to the load as the number of agents increases?
10.	In Table 3, there is no explanation for the missing RMSE results for New York and San Francisco. According to Appendix A, the data for these two cities comes from Safegraph, and the number of users is aggregated. So how is the GROUP-AND-DISTILL performed in these two cities?

### Soundness
2

### Presentation
2

### Contribution
2
