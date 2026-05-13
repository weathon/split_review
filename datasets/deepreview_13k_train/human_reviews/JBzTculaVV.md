# OASIS: Open Agents Social Interaction Simulations on a Large Scale

- Decision: Reject
- Scores: 1, 5, 8, 3

## Abstract
There has been a growing interest in enhancing rule-based agent-based models (ABMs) for social media platforms (i.e., X, Reddit) with more realistic large language model (LLM) agents, thereby allowing for a more nuanced study of complex systems. As a result, several LLM-based ABMs have been proposed in the past year. While they hold promise, each simulator is specifically designed to study a particular scenario, making it time-consuming and resource-intensive to explore other phenomena using the same ABM. Additionally, these models simulate only a limited number of agents, whereas real-world social media platforms involve millions of users.
To this end, we propose OASIS, a generalizable and scalable social media simulator. OASIS is designed based on real-world social media platforms, incorporating dynamically updated environments (i.e., dynamic social networks and post information), diverse action spaces (i.e., following, commenting), and recommendation systems (i.e., interest-based and hot-score-based). Additionally, OASIS supports large-scale user simulations, capable of modeling up to one million users. With these features, OASIS can be easily extended to different social media platforms to study large-scale group phenomena and behaviors. We replicate various social phenomena, including information spreading, group polarization, and herd effects across X and Reddit platforms. 
Moreover, we provide observations of social phenomena at different agent group scales. we observe that the larger agent group scale leads to more enhanced group dynamics and more diverse and helpful agents' opinions. These findings demonstrate OASIS's potential as a powerful tool for studying complex systems in digital environments.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
2

### Summary
In this paper, the authors present an LLM-based platform for the agent-based simulation of user behavior and interactions in online social media at large scale. The system consist of multiple components, which allow to incorporate data on real-world users on social media platforms and generate a large number of artificial agents by prompting a large language model. A time module controls the temporal acticity of those agents and an LLM is used to generate actions such as the creation of new posts, liking or disliking the posts of others or forming new follower relationships. A recommender system module that models recommendation algorithms of real platforms determines which content is shown to agents. The authors include experimental results on simulations of information spreading and group polarization on the platform X, and herd effects in terms of comment scores on the platform Reddit. Aggregate scores are used to compare the results of these simulations to behavior of humans.

### Strengths
[S1] The work highlights an interesting direction of research on leveraging large language models for realistic agent-based simulations of collective social behavior at large scale. 

[S2] The authors present a practical design of a platform for agent-based simulations at large scale.

[S3] The system is experimentally evaluated by comparing the results of agent-based simulations of information spreading and group polarization with actual human behavior.

### Weaknesses
[W1] Given the complexity of LLMs, it is unclear which insights an LLM-based agent-based simulation can yield into the actual microscopic mechanism underlying collective social phenomena that emerge at the macroscopic scale. 

[W2] The description of the platform remains at a rather high and superficial level. Some details of the complex platform design are not explained in detail.

[W3] I am not convinced by the way how temporal and topological characteristics of agent interactions are integrated into the simulation.

[W4] I do not think that the contributions summarized in this paper are of sufficient relevance for the wider ICLR research community.

### Questions
Regarding [W1], the authors clearly position their work as a tool for researchers who are interested to investigate complex collective phenomena emerging in social systems at large scale. To that end, agent-based models are typically employed in computational social science not to faithfully simulate all aspects of a given system but to understand how simple mechanisms of agent behavior and agent interactions at the micro-scale give rise to collective phenomena at the macro-scale. A crucial aspect in this approach is thus the ability to trace back a given phenomenon at the macro-scale to a specific mechanism operating at the microscale between individual agents. Given the approach proposed in this work and the complexity of the LLM models governing agent dynamics, it is unclear how the design of the system can help to gain insights into such mechanisms. Could the authors comment on this?

Referring to [W2]. from the rather short descriptions of the individual components, I did not understand many crucial details of the platforms and the experiments. For instance, what exact data on real users are used to initialize the simulation and how much of such data is needed. How have the specific users in the experimental evaluation (e.g. for the group polarization experiment) been chosen? How were the features of users (e.g. profession, Myers–Briggs Type Indicator) chosen and which data were used to fit the distribution? How exactly was the iniital social network between agents generated and how realistic is this compared to relationships between real users? What is the rationale behind the specific prompts used to generate agents or actions and how could the formulation of the prompt change the result? Related to [W1] all of those aspects could be thought as "parameters" in an immensely complex agent-based simulation, which may crucially influence the results!

Regarding [W3], it is well-known in the network science and complex systems community that both the topology of interactions between agents as well as their temporal dynamics crucially influences collective dynamics in multi-agent systems. While both aspects are (somehow) considered by the Time Engine and the initial network generated when agents are created (and new follower relations generated by the action module), it is unclear how realistic those two crucial components are. To be more specific, a simple vector of hourly probabilities of activity underfits the real complexity of human dynamics on social media, as it assumed a memoryless process. In contrast, real-world human behavior on social media has been shown to be characterized by complex non-Markovian and bursty activity patterns which are not captured by this approach. Similarly, the initial follower network will likely strongly influence agent behavior as well as the evolution of agent relations. It is not clear to me how realistic the proposed approach for network initialization is.

Finally and considering [W4], I am not convinced that the contributions made by this work are sufficient to be relevant for the ICLR research community. As also clearly stated by the authors, the general idea to use LLMs for more realistic agent-based simulations is not new and has been explored in several recent works. One key contribution of this work is that it proposes a practical design how such LLM-based agents can be integrated with a rule-based system to facilitate large-scale simulations of agent societies. 

The fact that the developed system has been evaluated experimentally against a population of human users is noteworthy, but I am not convinced that the rather simple aggregate results (e.g. on the scale, breath, and depth of information propagation paths or on simple mean comment scores) actually support the strong claim that the proposed approach allows to replicate real-world social phenomena. Moreover, to justify the considerable computational resources required to perform LLM-based agent simulations at large scale, it would be necessary to compare those results to simpler agent- or network-based models for information propagation or opinion formation. 

In summary, I am not convinced that the contributions of this work justify publication at ICLR. To me, this work seems more fitting to a venue focussing on agent-based simulations, simulations of social dynamics, computational social science, or so-called "agent societies". My low score on the contribution of this work - and the recommendation to reject it - should thus be interpreted in the context of a deep learning venue and does not imply that this work does not make a contribution that is more valuable for other communities.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces OASIS, a scalable and generalizable social media simulator designed for studying complex systems with large language model (LLM) agents. Unlike existing simulators, which are scenario-specific and limited to small agent counts, OASIS can simulate up to one million users on platforms like X and Reddit, incorporating dynamic environments, diverse actions (e.g., following, commenting), and adaptive recommendation systems. OASIS replicates social phenomena such as information spreading, group polarization, and herd effects across various platforms. Results show that larger agent groups enhance group dynamics and yield more diverse opinions, demonstrating OASIS’s versatility for large-scale digital social studies.

### Strengths
1. I am very interested in the topic of this paper; it is a large-scale social simulation that exceeds the number of agents used in current social simulations.

2. This paper presents a thorough piece of work with a substantial engineering effort. The meticulous design of each module contributes to excellent results.

3. This paper excels in writing, experimental illustration, and analysis, providing a great experience for readers.

4. The topic of this paper is very meaningful; social simulation is highly important and crucial for the development of social media and computational social science.

### Weaknesses
1. The primary contribution of this paper is significantly increasing the scale of existing social simulations to the one-million level. However, I did not find scientific insights on this issue in the paper, such as:

*   No explanation of why previous methods could not scale to the million level, is there any novel algorithms, data structures, or distributed computing techniques used?
*   No details on the methods used to overcome this bottleneck

The approach in this paper seems more of an engineering solution rather than a scientific discovery, which does not sufficiently support the argument presented in the paper. The authors include a more in-depth comparison to previous approaches, highlighting the key differences that allowed for increased scale. This would help clarify whether there are scientific contributions beyond engineering optimizations.

2. An important contribution of this paper is incorporating dynamically updated environments, diverse action spaces, and recommendation systems. The diverse action spaces are a good innovation, aligning well with the actions on social media platforms in real life. However, I have some questions regarding the dynamically updated environments and recommendation systems:

*   For dynamically updated environments, I understand this should involve continuous changes in users or relationships between users.  I think the authors should tell us how new users are added, how relationships evolve over time, or how the content of the simulated social media platform changes as agents interact.

*   Many social simulations already include a recommendation systems module[1], so as a contribution to this paper, the recommendation systems module lacks novelty.

3. This work lacks comparisons with previous methods. For example, in the Information Propagation experiment, previous studies have also explored similar experiments[2]. The paper should include some comparison results to demonstrate the advantages of OASIS.  (e.g. scalability, accuracy of replicating real-world phenomena, computational efficiency). (I am not necessarily requesting that these experimental results be provided at the rebuttal stage, nor do the baseline selections need to be limited to my references. However, I believe that before this paper is published, it should include the results of this comparison experiment.)

4. In section 3.4, this part explores "DOES THE NUMBER OF AGENTS AFFECT THE ACCURACY OF SIMULATING GROUP BEHAVIOR?" However, in the two experiments (“INFORMATION PROPAGATION IN X” and “HERD EFFECT IN REDDIT”), there is no detailed explanation of how accuracy is defined for each experiment. 

5. This paper does not provide data and code, which raises significant concerns about its reproducibility.

6. There is a typo on line 411, “curs?”.

### Questions
First, I hope the authors can respond to the points outlined in the weaknesses section.

Then, I have some additional questions I would like to discuss with the authors.

1. On line 180, the paper mentions a "relations network." In what format is this relations network stored? Is it in the form of a graph, text, or something else?

2. On line 341, the paper mentions a "propagation graph." In what format is this propagation graph stored? Is it in the form of a graph, text, or something else?

3. How is an “uncensored LLM” defined?

4. For Comment scores, why is it calculated as upvotes minus downvotes? If a post has 100 upvotes and 100 downvotes, while another post has 5 upvotes and 5 downvotes, both would have a Comment score of 0. However, the level of attention these two posts receive on social media is clearly different.

5. Why not use models like GPT-3.5-turbo, GPT-4 (possibly more costly), or GPT-4o-mini for the experiments? Given their relatively strong reasoning abilities, they might achieve higher accuracy.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This manuscript proposes an LLM-based ABM simulation framework, OASIS, to study large-scale social phenomena arising from social interactions in a multi-agent social media environment. Compared with existing frameworks, OASIS can host many users (1M), simulate X & reddit, have a bigger action space, implement recommendation systems, and simulate dynamic network evolution. The authors demonstrate the utility of OASIS by simulating several social phenomena such as information spreading, group polarization, and herding behavior.

### Strengths
- The OASIS framework seems to be an impressive and comprehensive piece of engineering for simulating large-scale social media environments with LLMs, which can be useful for future studies on large-scale social phenomena.

- The framework seems to be capable of exhibiting somewhat realistic behavior in several social phenomena, which is a promising sign. 

- Many ablation studies are performed to show the robustness of the results and the importance of each component of the framework.

- The paper is fairly well-written and relatively easy to follow.

### Weaknesses
 - I think, in a way, the paper tries to pack too much in a single paper. I think it was challenging to provide all the details of the engineering AND conduct thorough social experiments. As a result, I feel that the social phenomena simulations are somewhat shallow and not very insightful. For instance, the simulations raise the question of "null models" -- how surprising or insightful are these massive LLM-simulated results compared to a simple model? -- as well as the question of potential parameter and environment settings. Given so many parameters one should set to simulate a social media, it is really hard to know what is driving the results and how different the simulation results would be in different settings. It is simply impossible to know whether the results shown in the paper are typical across different settings or something that only arises in the specific settings used in the paper. While I think it is still meaningful to demonstrate that the OASIS framework can produce somewhat realistic social phenomena, I think it could have been more insightful if there was a separate, in-depth analysis of each social phenomena.

- I was not entirely sure whether the paper contributes to the advancement of representation learning. The paper uses LLMs, but the focus is more on the engineering of the simulation framework. Although it may be possible to argue that the paper enables the study of large-scale social phenomena that can be studied with LLMs and how the "representation" that LLMs use can affect the social phenomena, it is still quite indirect.

### Questions
- Studies have shown that many large-scale patterns from social media can be explained by simple models and few key mechanisms. For instance, Weng et al. Sci. Rep. (2012) showed that limited attention is enough to produce the power-law distribution of propularity of hastags; the "burstiness" of human behavior (see Barabasi's work on burstiness) has been studied as a key mechanism for many patterns in social phenomena; the "homophily" mechanism has been shown to be a key mechanism for many social phenomena; There are also many cognitive biases that can explain many social phenomena.

I don't think it is required for this paper at this stage to incorporate all these mechanisms into the OASIS framework, but I think it would be great to discuss how the OASIS framework can be used to study these mechanisms and how the results from OASIS can be interpreted in light of these cognitive mechanisms.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper approaches the problem of social simulation. The authors build about 1 million users and use LLM agents to simulate 21 kinds of actions. The authors evaluate the system by observing the trend of scale, trend of depth, trend of max breadth, etc. The results indicate that the developed system, named OASIS, can partially replicate real-world phenomena.

### Strengths
- The authors use real-world datasets from X and Reddit and simulate a very large-scale user community.
- There are some new features compared with the existing works, including a dynamic network and more actions.
- The paper is generally well-written.

### Weaknesses
 - It is very strange and may introduce bias to simulate the recommendation system in a social network, which is not so important. Users can interact with information in multiple ways, and the recommendation system is only one of them. Introducing recommendation algorithms in social simulation may introduce bias as we don't know the details of recommendation algorithms in the collected data. I have also checked the papers in Table 1, in which only RecAgent and Agent4Rec considered recommendation systems (of course, as they are about the simulation of recommendation rather than social simulation).
- The evaluation should be improved. Can we use the results in Figure 4 to claim that the simulation is accurate and useful? There are still errors. The authors should carefully analyze where the error comes from and help the readers know when we can use the results of OASIS. In other words, what kind of use can these imperfect simulations have? We all know that perfect simulations are not possible, but it is important to analyze what kind of impact these errors may have.
- The authors should conduct more evaluations based on social network theory. Could the simulation system be consistent with those representative theories such as network dynamics? These important and basic questions have not been well answered.

### Questions
The questions are based on the weaknesses, and it will be great if the authors can offer feedback.
1. Why simulate recommendation system? What kind of bias it involves?
2. Can we use the results in Figure 4 to claim that the simulation is accurate and useful? What kind of use can these imperfect simulations have? 
3. Could the simulation system be consistent with those representative theories such as network dynamics?

### Soundness
2

### Presentation
3

### Contribution
2
