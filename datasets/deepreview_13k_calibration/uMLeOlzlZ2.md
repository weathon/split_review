# LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 8, 1, 8

## Abstract
Reducing hallucination of Large Language Models (LLMs) is imperative for use in the sciences, where reliability and reproducibility are crucial. However, LLMs inherently lack long-term memory, making it a nontrivial, ad hoc, and often biased task to fine-tune them on domain-specific literature and data. Here we introduce LLaMP, a multimodal retrieval-augmented generation (RAG) framework of hierarchical reasoning-and-acting (ReAct) agents that can dynamically and recursively interact with computational and experimental data from the Materials Project (MP) and run atomistic simulations via high-throughput workflow interface. Without fine-tuning, LLaMP demonstrates strong tool-usage ability to comprehend and integrate various modalities of materials science concepts, fetch relevant data stores on the fly, process higher-order data (such as crystal structure and elastic tensor), and streamline complex tasks in computational materials and chemistry. We propose a metric combining uncertainty and confidence estimates to evaluate the self-consistency of responses by LLaMP and vanilla LLMs. Our benchmark shows that LLaMP effectively mitigates the intrinsic bias in LLMs, counteracting the errors on bulk moduli, electronic bandgaps, and formation energies that seem to derive from mixed data sources. We also demonstrate LLaMP’s capability to edit crystal structures and run annealing molecular dynamics simulations using pre-trained machine-learning interatomic potentials. The framework offers an intuitive and nearly hallucination-free approach to exploring and scaling materials informatics and paves the way for knowledge distillation and fine-tuning of future language models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript describes the introduction and test of LLaMP, an LLM fine tuned to interact with the materials science data from the Materials Project database and run atomistic simulations via a workflow interface.

### Strengths
The introduced LLM is very likely of great interest for the materials science community, in particular because it is ready to be used and it is fine tuned on one of the largest and most consistent corpus of materials-science data, especially computational (atomistic-simulation) data. 
Results suggest it would be a useful tool used for materials-science research.

### Weaknesses
 There is no methodological advance worth highlighting here. The described "hierarchical agent framework" is a simple device to design and implement, while the metric assessing consistency is reasonable for reporting and discussing results but does not strike as a major advance.
In view of these strengths and weaknesses, the paper seems more indicated for a materials-science specialized journal such as npj Computational Materials.

- Figure 2, which reports with Table 1 the main results of the manuscript, is barely readable. 
Besides working harder on contrasting colors overall visibility, the authors should explain all symbols' choices and consider either reducing the amount of data shown or make the figure in more panels (possibly reporting some crucial example in the main text and the rest in an appendix).
- in Table 1, confidence scores equal exactly to 1 (at least to the third digit precision), especially if combined with MAE equal to 0.000 (see electronic band gaps of common elements for LLaMP) look unlikely good and suggest the prediction use training data. This aspect would need discussion in presenting the results, and probably a different design of the performance tests.

### Questions
- Figure 2, which reports with Table 1 the main results of the manuscript, is barely readable. 
Besides working harder on contrasting colors overall visibility, the authors should explain all symbols' choices and consider either reducing the amount of data shown or make the figure in more panels (possibly reporting some crucial example in the main text and the rest in an appendix).
- in Table 1, confidence scores equal exactly to 1 (at least to the third digit precision), especially if combined with MAE equal to 0.000 (see electronic band gaps of common elements for LLaMP) look unlikely good and suggest the prediction use training data. This aspect would need discussion in presenting the results, and probably a different design of the performance tests.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose LLaMP, a multimodal retrieval-augmented generation (RAG) framework leveraging hierarchical reasoning-and-acting (ReAct) agents to dynamically interact with Materials Project (MP), arXiv, Wikipedia, and atomistic simulation tools. To reduce the hallucination of Large Language Models (LLMs), the framework provides LLMs with high-fidelity material informatics derived from various sources. Consequently, LLaMP leverages hierarchical planning and correctly retrieves higher-order materials data and also combines different modalities to perform complex, knowledge-intensive inferences and operations essential for real-world research applications. LLaMP manifests enhanced performance in predicting key material properties, real-world applications in materials science, and language-driven simulations.

### Strengths
1. The paper presents a well-designed hierarchical ReAct agentic framework that dynamically manages multiple agents, each specialized in distinct tasks. This structured approach is highly modular, improving the model's accuracy and efficiency in handling complex workflows.

1. The authors provide a comprehensive discussion of LLaMP's strengths and limitations, offering valuable insights into its potential and constraints in materials science. This balanced analysis enhances the paper's utility for related researchers by clarifying LLaMP's practical applicability and areas for further development. 

1. The self-correcting agent mechanism enables real-time error correction during tool usage and API interactions. This design minimizes the propagation of errors and enhances reliability in complex tasks. 

1. The paper not only presents benchmarking results and analysis but also discusses the real-world applications in materials science. This applied focus, combined with LLaMP's use of high-fidelity data sources, makes it highly relevant and impactful for researchers.

### Weaknesses
1. The framework relies heavily on data from the Materials Project, which may restrict its application to new or less-explored materials. Although MP is comprehensive, the paper acknowledges that the database's coverage is not exhaustive, particularly for certain magnetic and bandgap configurations. This dependence on a single database could limit the model's ability to generalize to materials not well-represented in MP, potentially hindering its application in novel materials discovery.

2. While the paper demonstrates LLaMP’s applications in materials science, the analysis is primarily based on one or two examples for each application. A more comprehensive experiment or in-depth discussion of success and failure cases should be helpful for exploring real-world applications. The limited number of examples makes it difficult to fully assess the robustness and generalizability of the framework across a wider range of materials science problems. A more thorough analysis, including edge cases and failure modes, would provide a more complete picture of LLaMP's capabilities and limitations.

3. The statistics for precision and CoP in Table 1 seem not consistent with the equation in Section 4.2. See the questions for details.

### Questions
1. According to Section 4.2, $CoP = exp(−Precision)$. However, a lot of Precision and CoP results in Table 1 do not match this relationship. For example, The Precision of LLaMP on bulk modulus is $2.698$, then $exp(-2.698) = 0.067$, but the reported value is $0.900$. Can the authors clarify that?

1. Have the authors tried LangGraph instead of LangChain for a more structured agentic workflow instead of a linear one? Langgraph will probably be beneficial as it may enhance the hierarchical planning in LLaMP, potentially improving agent coordination and task prioritization, especially for complex, multi-step processes.

1. In the example in Figure A.1, it seems that the supervisor gives mp-9258 as the answer to the query even though the two assistant agents never return any of the relevant information. So can I interpret that the example ends up with a hallucination? Is there any method to prevent this, and why is there not an observation step to capture the mismatch between the requested and returned MP IDs and to require the refinement of the action?

1. While LLaMP shows strength in typical systems (e.g., Si-O, Li-based compounds), how does it perform on less common or highly complex systems, such as multinary oxides or intermetallic compounds?

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
4

### Summary
The paper proposes a new method for LLMs (LLAMP) applied to materials science based on retrieval-augmented generation (RAG) and hierarchical reasoning-and-acting (ReAct) that addresses language-based materials science tasks. The papers starts by motivating LLAMP based on the fact that many LLMs lack access to up-to-data for solving timely materials challenges and are prone to hallucination. As such, LLAMP aims to alleviate those challenges by providing a way to infuse external data sources when solving materials science tasks. The paper claims five contributions: 1. the LLAMP method; 2. metrics for understanding self-consistency for LLMs; 3. a study for materials property prediction; 4. showcasing LLAMP capabilities in synthesis and materials structure generation; 5. demonstrating high-throughput atomistic simulations using LLAMP.

Next, the paper describes related work in Section 2 and Section 3 respectively focused on the materials project, NLP in science as well as the application of prompting and tool use to solve materials science challenges. Section 4 the describes the main pieces of the LLAMP-ReAct framework, including the supervisor agent and assistant agents that help perform relevant tasks. Section 4 also outlines the metrics used in subsequent analysis, including Prediction, Coefficient of Precision, Confidence and the Self-consistency of Response (SCoR). The primary aim of the metric is the understand the consistency and confidence of LLM responses to certain queries where reliability is important. Section 5 provides the main experiments with the main focus on including materials property prediction. The paper then provides an analysis based on the metrics proposed in Section 4. The analysis generally shows that LLAMP provides lower MAE in property prediction and usually second best in SCoR. Section 5.2 also showcases a study on data retrieval for materials property analysis where LLAMP with its ReAct framework generally outperforms vanilla LLMs relying on implicit knowledge. Section 5.3 provides a brief description summarization of synthesis procedures as well as crystal generation and language-drive simulation. The discussion of the experiments in Section 5.3 is brief with much reference to the appendix for supporting information. The general claims in Section 5.3 is that LLAMP outperforms vanilla LLMs.

The paper concludes in Section 6 with a discussion on robustness, which ties into one of the main motivations outlined in the introduction, as well as limitations and a broader summary of the work and potential future work.

### Strengths
* The paper introduces a new framework to relevant challenges in materials science. 
* The tools and knowledge bases included in the LLAMP framework could be useful to build upon.

### Weaknesses
In its current form, the paper has substantial weaknesses related to limited machine learning novelty, scant evidence of the initial claims and missing discussion of relevant related work.

* Machine Learning Novelty: the paper does not provide good evidence for its machine learning novelty. The background and related work provided limited discussion of RAG and tool-calling in general and miss relevant work in related domains. As such it is difficult to understand the novelty of the LLAMP.
* Evidence for claims: In the current form, the main addition novelty related to LLAMP focuses on RAG and ReAct and many of the presented experiments show that a RAG-based performs better a RAG-based tasks (e.g., information retrieval) compared to a non-RAG model. As such, the only claim that is somewhat properly supported is that a RAG-based model is somewhat better and more consistent on tasks where RAG is useful, which is not particularly surprising given prior success of RAG. Additionally the paper provides scant evidence for claims 4 & 5 in the main text with much reference for the appendix. This is not (in my opinion) best practice and weakens the initial claims made in the introduction.
     * The claims related to the ReAct framework could also be strengthened by adding an ablation on tool calling - especially since the paper mentions flat tool calling.
* Related work: The paper provides a limited discussion of relevant work related to machine learning for relevant parts of the proposed method, including RAG and tool-calling. This extends to LLMs for chemistry and materials science where methods, including agent methods, have been proposed [1] [2]. The section on NLP for science could also benefit from a broader inclusion of work on applying LLMs for question-answering tasks in materials science [3] [4] [5] along with additional work on LLMs for materials science data extraction [6] [7 - mara].

### Questions
* How are the agents distinguished from each other? Do they receive different prompts, different context? It seems like not all of them are LLM based - it would be good to describe more details on what is considered an agent and what is considered a tool.
* Have you compared to other RAG methods? It seems a bit unfair to have to benchmark LLMs solely on implicit knowledge. It would also be good to get additional context on how your proposed tool calling method compares to other methods [8]
* How limited are the proposed methods to Materials Project? What would be needed to apply it to other materials science knowledge sources?
* Could you add the main conclusions in the captions of figures and tables for greater clarity?

[8] Qin, Yujia, et al. "ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs." The Twelfth International Conference on Learning Representations.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes LLaMP, a RAG framework based on hierarchical ReAct agents. The supervisor agent handles high level logic while assistant agents interact with Materials Project, arXiv, Wikipedia and atomistic simulation tools. 

The authors then introduce a metric, the Self-Consistency of Response (SCoR), which aggregates the model's confidence in answering with the variability of the answers. 

Experiments show that LLaMP achieves a low MAE and high SCoR in generating Bulk Modulus, Formation Energy, and Electronic Bandgap while LLMs and other RAG frameworks achieve higher MAEs and comparable or lower SCoR. 

LLaMP is also able to predict the magnetic orderings and total magnetisation, retrieve inorganic synthesis recipes, edit crystal structures and drive simulations.

### Strengths
**Originality**
LLaMP is original in its use of hierarchical agents and the combination of agents used. The metrics and combination of tasks is also original. 

**Quality**
The hierarchical orchestration is well thought out and seems to perform well. The variety of agents makes the framework useful for materials scientists. The SCoR is mostly well justified. The experiments are convincing. The variety of tasks used is a bonus.

**Clarity**
The paper is easy to read  and well organised. Figures and Tables are informative (except Figure 2, see Weaknesses).

**Significance**
Accuracy of answers and reducing hallucinations is important when using LLMs in a scientific context. LLaMP is a significant step towards addressing these issues and thus is a valuable contribution to the community.

### Weaknesses
1) The name precision in SCoR feels misleading. When SCoR = 1, the model generates the same response to queries, meaning that the standard deviation is zero and also the precision is zero. This is counter-intuitive as I think of precision as True Positives / (True Positives + False Positives). The use of 'precision' to describe the standard deviation of the model's responses is confusing, especially given the established use of 'precision' in information retrieval and classification tasks. In those contexts, precision measures the proportion of true positives among all predicted positives. The authors should consider using a different term, such as 'response variability' or 'consistency', to avoid this confusion.
2) Figure 2 is unclear. How should I read the values produced by each method? What is the ground truth? The box plots lack clear labels indicating what each axis represents, and the absence of a ground truth reference makes it difficult to assess the performance of each method. It is not clear whether the values represent absolute errors or some other metric. The figure needs to be more self-explanatory, with clear axis labels and a visual indication of the ground truth values.
3) (Minor) I can't find a citation for LangChain.

### Questions
1) Can you please elaborate on how the standard deviation in SCoR is calculated? I assume that it only works for numerical answers and it's the standard deviation of the population.
2) Can you please clarify Figure 2. What are the ground truth values?
3) Can you provide code to reproduce the framework? This would add value to your submission.

### Soundness
3

### Presentation
3

### Contribution
3
