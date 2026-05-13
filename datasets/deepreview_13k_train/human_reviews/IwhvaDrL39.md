# Research Town: Simulator of Research Community

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Large Language Models (LLMs) have demonstrated remarkable potential in scientific domains, yet a fundamental question remains unanswered: Can we simulate human research communities using LLMs? Addressing this question could deepen our understanding of the processes behind research idea generation and inspire the automatic discovery of novel scientific insights. In this work, we propose ResearchTown, a multi-agent framework for simulating research communities. Within this framework, the real-world research community is simplified and modeled as an agent-data graph (i.e. community graphs), where researchers and papers are represented as agent-type and data-type nodes, respectively. We also introduce TextGNN, a text-based inference framework that models diverse research activities (e.g., paper reading, paper writing, and review writing) as specific forms of a generalized message-passing process on the agent-data graph. To evaluate the quality of research simulation, we present ResearchBench, a benchmark that uses a node-masking prediction task for scalable and objective assessment. Our experiments reveal three key findings: (1) ResearchTown effectively simulates collaborative research activities by accurately predicting the attribute of masked nodes in the graph; (2) the simulation process in ResearchTown uncovers insights, like not every author contributes equally to the final paper, which is aligned with real-world research communities; (3) ResearchTown has the potential to foster interdisciplinary research by generating reasonable paper ideas that span across domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors explore the question of whether multiple LLMs can collaborate like human researcher community to generate high-quality research proposals. Specifically, the authors introduce RESEARCHTOWN, which is a multi-agent research simulator that can automatically pair LLM agents for tasks such as literature review, idea discussion, and peer review. RESEARCHTOWN takes advantage of the connections by selecting a paper and providing its related works to LLM agents with relevant expertise. Unlike traditional methods that use citation graphs to study academic collaboration, RESEARCHTOWN employs a dynamic, graph-based approach where agents with distinct expertise engage in research activities such as brainstorming, literature review, and peer review, emulating real-world interdisciplinary collaboration. Overall, the topic is novel and interesting, and the writing is fluent.

### Strengths
S1: The idea is interesting. The paper introduces a multi-agent, graph-based simulation framework where LLMs collaborate like human researchers to generate proposals. This approach shifts from traditional citation-based studies to simulating real-time interactions in research, opening new possibilities for AI-driven research collaboration.

S2: Most modeling decisions are well-documented and likely sufficient to reproduce the approach. Evaluated through RESEARCHBENCH, the proposed framework shows strong performance in generating coherent proposals. The multi-agent versus single-agent comparisons further validate the quality and relevance of the approach.

S3: The paper is well-structured and easy to follow.

### Weaknesses
W1: The authors only compare the proposed method with a single agent, but do not compare it with the current LLM for automatic research mentioned in related work. 

W2: The authors could add ablation experiments to illustrate the effectiveness of each module.

W3: RESEARCHTOWN appears computationally intensive, especially with multi-agent setups for complex proposal tasks, which could hinder its scalability and usability in practical research environments.

W4: While the RESEARCHTOWN framework’s proposals are evaluated through similarity metrics and some human assessment, the criteria for judging proposal quality could be more robust. For instance, the authors could integrate domain-specific expert reviews and structured evaluation criteria that assess innovation, feasibility, and alignment with real-world research standards. 

W5: The technical innovation is somewhat limited.

### Questions
Q1. Can you further elaborate on the contribution of the paper? For example, how to ensure the similarity between two nodes in subgraph extraction? In addition to semantic similarity, should structural or other attribute similarities be considered?

Q2. How to improve or optimize the scalability of the RESEARCHTOWN framework? For example, implementing efficient resource management strategies could make RESEARCHTOWN more accessible for a wider range of users and research groups.

Q3. How does RESEARCHTOWN compare to the existing multi-agent LLM framework? Why can't the existing multi-agent framework be directly applied in the research? Why doesn't the author compare the framework with the existing multi-agent framework?

Q4. The validation data set is a bit small. Will the conclusions (made in this paper) still be held for large(r)-scale datasets?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Summary: This paper describes software and an accompanying conceptual model for running multi-agent simulations of research activity (using LLM outputs as “agent actions”). The core research question being studied here is whether the orchestration of multiple models (inspired by past “generative simulation” work can produce better research related artifacts.

The agents generate “proposals”, which can be compared in terms of similarity scores to human-generated output.

The paper then discusses three key insights regarding the alignment (similarity) of model outputs to human proposals, the variance in “idea novelty”, and potential for cross-domain research.

### Strengths
- The motivation regarding science of science, citation graphs, etc. is strong. In particular, I expect readers may find the potential for future work incorporating agents (with or without LLMs) and explicit modeling of “collaboration” graphs to be an exciting future direction.
- Evaluation contribution (“Research-Bench”) here can be very useful for the community 
- The current draft has a reasonable discussion of ethical issues. I think the appendix sections included here make a meaningful contribution to what are likely to be high-stakes discussion in academia and society more broadly about the inevitable use of systems like these.
- The experiments presented here can be useful for further understanding the usefulness of LLMs in academic labor.

### Weaknesses
 * Some concerns with very generalizable claims, especially regarding wide-reaching social benefits (see exact line numbers in “Questions” below).
* Current draft has some ambiguity about why the focus on “dynamic interactions” (e.g. line 104) is critical, vs. simply treating this as a system that produces good research artifacts (see Questions below)
* There is a user study component here, but it is only mentioned briefly.
* Subjective: while I understand some potential benefits, I am not convinced that using examples that focus on LLMs (e.g. Figure 3) is the best choice here for clarity or making the results more convincing (compared to e.g. an example from the hard sciences).
* While the first and second contribution are reasonably well-supported, the paper could do more the justify the idea that cross-disciplinary innovation was produced.
    * In the current draft, it is not clear in Section 6 how the “hadron” example (line 485) was determined to be high quality whereas the “MoJE” (line 495) was not. Being more familiar with the ML side of things, this claim seems reasonable, but describing this process more systematically will convince more readers.

At a high-level, I think the largest weakness of the paper is the lack of clarity about whether the goal here is make an agent-based modeling, somewhat social scientific contribution, or if the goal is the create a system that does a very good job at creating high-quality research proposals (as defined based on similarity or human labeling.)

### Questions
* I did not understand the claims on line 88-90. Can you further justify the connection with this work and democratization, diversity, etc.? It seems equally possible that all the results here true (that LLMs can produce useful research outputs) but actually serve to concentrate power (i.e. empower already well-resourced researchers) or homogenize thought.
    * More generally, I think some of the sweeping broad motivations here may distract from the strengths of the work, which is the motivation about modeling collaboration graphs.
* Regarding the discussion of the Community Graph idea, is the reader meant to take away the idea that Community Graphs are useful for conceptual reasons (e.g., because they connect this work with social science theory) or primarily focus on the fact that they work well for the task at end? In other words, to what extent is the goal here to do well on a Research-Bench like task?
    * Would future versions of this system try to explain their inner workings via the graph?
* How exactly is a “research proposal” defined in this context and what is the most similar “familiar artifact” – a grant proposal, an abstract, etc.? This caused me to stumble a bit when reading the evaluation, as I couldn't latch onto a clean picture of what being a human labeler for this task would look like. Is the closest analog a grant reviewer?
* How exactly was the user study conducted (human evaluation?). Many additional details are needed here, including details about the labelers and the instructions given for the labeling process.
* Are there cases in which user study suggests that similarity is not a good metric here?
* How will the benchmark contribution be shared (e.g., via data package release)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces ResearchTown, a multi-agent framework that simulates academic research communities using LLMs. The system allows multiple LLM agents to collaborate like human researchers to generate research proposals. The framework is built on a graph-based structure where agents (representing researchers) and papers are nodes, connected by various relationships (authorship, citations, collaborations). The authors evaluate their system using ResearchBench, comparing generated proposals to ground truth papers, and find that multi-agent approaches outperform single-agent baselines.

### Strengths
The paper presents a novel formalization of LLM-based research collaboration as a heterogeneous graph problem. While multi-agent LLM collaboration has been explored before (e.g., Tang et al., 2023), this paper captures academic dynamics through explicit graph modeling of relationships between agents and papers. 

The authors demonstrate special attention to ethical considerations, providing a detailed discussion of potential issues like plagiarism, research fabrication, and the responsible use of simulated research profiles in the appendix.


Tang, X., Zou, A., Zhang, Z., Li, Z., Zhao, Y., Zhang, X., ... & Gerstein, M. (2023). Medagents: Large language models as collaborators for zero-shot medical reasoning. arXiv preprint arXiv:2311.10537.

### Weaknesses
The paper's fundamental assumption that successful research simulation should produce proposals similar to existing papers warrants deeper examination. While alignment with human research can indicate quality, it's not obvious to me that matching existing papers is the ideal outcome for an AI research assistant.

The evaluation methodology of comparing generated proposals to existing papers, while practical, may not fully capture the value of novel research directions. Although the authors acknowledge this through their discussion of "underexplored research ideas," the evaluation framework could benefit from additional metrics that assess both alignment with existing research and potential for innovation.

The paper's framing of the system as a "text-version of GNN" appears unnecessarily complex, as all operations fundamentally work with text representations, and the benefits of this analogy over a simpler multi-agent framework are not clearly demonstrated. For example, encoding text may be confusing as it could also mean having an embedding vector for these texts.

the experimental section would benefit from more comprehensive details about implementation specifics, computational requirements, and ablation studies to validate individual components, particularly in comparison to simpler baseline approaches that might achieve similar results without the graph-based framework. Especially the lack of details makes it hard to assess the results. For example, how is the single agent implemented?

### Questions
Why would the human papers be the ideal outcome of a research agent (or multi-agent team)?

Could you provide more details on the experiments?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes researchTOWN for research community simulation by constructing the community graphs. Experiments show that researchTOWN generates cross-domain proposals with high-quality research recommendations through the interdisciplinary collaboration of agents from different domains. In addition, the paper proposes an LLM-based framework for evaluating the agent's RESEARCH-BENCH capability, which relies on similarity metrics rather than human judgment alone, making it scalable and practical for various applications.

### Strengths
S1. The paper presents a novel approach to constructing a community graph for message passing and implements brainstorming among LLM agents. The ideas articulated in the paper are quite innovative.

S2. The authors propose a framework for assessing RESEARCH-BENCH capabilities that rely on similarity metrics rather than solely on human judgment, demonstrating high scalability and practical applicability.

### Weaknesses
W1. The inputs and outputs of the tasks presented in this paper are not clearly specified, making it difficult for readers to discern them independently.

W2. The number of experiments conducted is limited compared to the theoretical content, and the significance of a single model's performance for the overall researchTOWN is not adequately addressed.

W3. The importance of the proposal format discussed on line 356 in relation to the overall researchTOWN is not clearly articulated, and the robustness of this format remains uncertain.

W4. The task query mentioned in lines 238 and 271 is not described accurately in the paper.

W5. The prompts used in GPT-SIM are not explained in the manuscript.

### Questions
Q1. What is the rationale for using both GPT-SIM and ROUGE-L for evaluation?

Q2. Why are only the models GPT4o, GPT4o-mini, and Llama3.1-72B selected? Were other models like Gemini and Claude considered?

Q3. How critical is the performance of a single model to the overall researchTOWN? If smaller models, such as Llama3.1-8B, were employed, could similar results still be achieved?

### Soundness
3

### Presentation
3

### Contribution
2
