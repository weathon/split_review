# FlowAgent: a New Paradigm for Workflow Agent

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Combining workflows with large language models (LLMs) allows LLMs to follow specific procedures, thereby extending their application to more real-world scenarios. However, incorporating workflows often compromises the flexibility of LLMs. For example in the case of Task-Oriented Dialogue (TOD), workflow atomize the function of LLM while programmatically imposing restrictions on execution path making the dialogue obstructed and less flexible when facing out-of-workflow (OOW) queries. Prompt-based methods offer soft control but sometimes fail to ensure procedure compliance. This paper introduces a new agent paradigm to address this challenge. Specifically, we first propose a novel Procedure Description Language (PDL) that integrates the flexibility of natural language and the precision of code for workflow expression. Additionally, we present a comprehensive framework that enables LLM to handle OOW queries while keeping execution safe with a series of controllers for behavioral regulation. This includes pre-decision and post-decision methods, where the dependency relationships between workflow nodes are modeled as a Directed Acyclic Graph (DAG) to validate node transitions. Beyond the primary objective of compliance considered in previous work, we introduce a new approach to evaluate the agent's flexibility in OOW situations. Experiments on three datasets demonstrate that FlowAgent not only adheres well to workflows but also responds better to OOW queries, showcasing its flexibility. Furthermore, exploration on WikiHow data confirms that the PDL effectively represents broader formats of workflow, inspiring further research on workflow-based QA tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces FlowAgent, a framework for integrating workflows into LLMs that balances procedural compliance with flexibility, addressing the limitations of existing prompt-based and rule-based methods. To achieve this, the authors propose a Procedure Description Language (PDL) that combines the natural language flexibility and programming-like precision needed for diverse workflows.

### Strengths
1. This paper defines a novel PDL to address OOW requests that agents may encounter during workflow execution. A comprehensive and unified framework like this facilitates further research in this field.
2. The authors also introduce a new evaluation framework specifically designed to assess workflow agents' performance in OOW scenarios.

### Weaknesses
1. The introduction of PDL lacks thorough analysis. After observing the impacts of OOW queries, it is unclear what specific considerations led to the development of PDL. Additionally, the completeness of PDL requires further examination to demonstrate its capability to handle more complex, real-world workflows effectively.

2. The evaluation of experiments is incomplete; the authors only assess GPT-4 and Qwen2-72B, with a brief note that “weaker models could not handle more complex workflow tasks.” However, there is no detailed analysis on what specific issues smaller models faced. Further exploration is needed to show how smaller models perform on simpler workflow tasks to provide a clearer picture of model scalability across task complexity.

3. Several key details are missing, such as the hyperparameters used during LLM inference, the prompts employed during data collection, dataset construction details, and relevant examples from the datasets. Including these would improve the reproducibility and clarity of the experiments.

### Questions
Minor Issues:
1. The text in Figure 4 is difficult to read, and the radar chart lacks specific performance values, making it challenging to interpret the results accurately.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper creates a framework (FlowAgent) for task-oriented agents that can offer flexibility and compliance with LLMs. They propose a new language, PDL, that creates a Directed Acyclic Graph with out-of-workflow (OOW) slots, making the agent flexible and using pre- and post-controllers for compliance. They perform an extensive evaluation on augmented datasets for showing how PDL handles flexibility and compliance.

### Strengths
- The work tries to add flexibility and compliance to the conversational agents, which is a real-world challenge.
- They experimented with three augmented datasets and showed that FlowAgent with PDL designed by humans works the best compared to NL, Code, and flowcharts created by GPT-o. 
- The writing is clear and easy to understand.

### Weaknesses
 - The paper has several missing details, especially regarding the experimental setup. I don't think there is enough evidence to suggest that PDL works for the WikiHow case study.
- The authors simulate users. However, as several studies have suggested, simulated users still do not capture real-world cases. The authors should have done a real-user study.
- With PDL, as the number of tools scale, it might be difficult for the developer to define all the pre_conditions. Especially since you need to define multiple flows and the logic is non-trivial to write to cover all the cases. See question 9.
- The baselines (NL, Code, and Flowcharts) are automatically converted from text using GPT, while the PDL is manually crafted for the in-house dataset, making the evaluation unfair. This discrepancy in creation methodology introduces a potential bias in favor of PDL, as manually crafted solutions often outperform automatically generated ones. The authors should ensure a consistent generation process for all formats to enable a fair comparison.
- The paper lacks a clear explanation of how Out-of-Workflow (OOW) nodes are added to the Directed Acyclic Graph (DAG). The description of adding an `answer_oow_questions` node is insufficient, as it does not clarify how this node interacts with the rest of the DAG or how the system determines when to invoke it. The mechanism for transitioning to and from this node needs to be explicitly defined.
- The evaluation of the WikiHow case study is based on manual interaction, which is not a rigorous method for assessing the broad applicability of FlowAgent to real-world workflow-based QA tasks. The authors need to conduct systematic experiments, including human studies for session-level evaluation, to demonstrate the effectiveness of their approach in practical scenarios. The lack of a standardized benchmark for workflow-based QA further complicates the evaluation process.
- The absence of code and data makes it difficult to reproduce the results. The authors should provide the code and data to ensure the reproducibility of the experiments and allow other researchers to build upon their work.

### Questions
1. For pass rate in turn-level evaluation, do you use an LLM to check whether the output is correct by turning it into a binary classification problem? 
2. Why do you use three types of OOW categorization? Changing their previous answers could be another scenario of OOW.
3. I believe that the Star dataset also contains OOW scenarios; why did you add more such dialogues, and how do you generate such queries?
4. Can you provide some stats or descriptions for your in-house dataset?
5. It is unclear how you converted existing flows into natural language, code, and flowcharts. Who made these conversions? Xiao et al. 2024 uses GPT to convert the text into NL, code, and flowcharts, whereas you write your own PDL. I don't think the comparison is fair here.
6. How do you construct reference sessions from tasks for turn-level evaluation using GPT-4o? Please provide more information.
7. Can you please provide an example conversation with the simulated users? There are works that demonstrate that user simulation is non-trivial in a conversational setting. [1]
8. Do you have any experiments with users or simulated users to suggest that PDL can handle WIKIHOW like examples?
9. In the WIKIHOW example, what would happen if the user directly asks how to find a website's publication date using code? Since the write PDL says `if publication_date is None:` then use Google search or other tools. In this, the publication date will not be None, right? This makes me believe that you must define several "flows" for the PDL to work in all scenarios.
10. Table 1 typo, for # Turn in Star turn-level row.
11. Who add the OOW nodes to the DAG?
12. What metric did you use to decide the flexibility and compliance score in Figure 1 (c)? What is the scale for the plot?

[1] Zhou, X., Su, Z., Eisape, T., Kim, H., & Sap, M. (2024). Is this the real life? is this just fantasy? the misleading success of simulating social interactions with llms. arXiv preprint arXiv:2403.05020.

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
The authors propose FlowAgent, an agent built using LLMs and incorporates workflow rules to balance between flexibility and compliance. The agent leverages both pre-decision and post-decision controllers to adjust the agent's behavior. Experimental results on existing and custom datasets show FlowAgent's superiority compared to other approaches from the literature.

### Strengths
The paper was easy to read and addresses an interesting problem in the literature that is very relevant to industry applications. The solution also seems simple to implement making it easy to adopt in use cases. The experimental section shows the benefits of the authors' proposed method.

### Weaknesses
The paper contains a few gaps in the both the presentation of the work and the experimental section. 

First, it is unclear how the controllers were implemented, i.e., there isn't sufficient information in the write up for one to reimplement or even have an idea of what approach was adopted. It seems that the controllers rely on deterministic syntax and logic checks but that is pure speculation on my part as the paper only has a few lines describing both pre and post decision controllers, namely focusing on their purpose as opposed to their implementation. It would be helpful if authors could either include a pseudocode of their controllers or a diagram describing their operations. 

Second, the experimental section does not discuss the computational cost and additional overhead of FlowAgent compared to other approaches. Since FlowAgent operates in a conversational setting, a level of responsiveness is expected but we have no way of knowing from the paper how much overhead the added controllers are causing from both responsiveness and computational cost perspectives. It would be helpful if the authors included runtime comparisons or latency measurements between FlowAgent and the baseline approaches in their experimental results. Additionally, an analysis of how the controllers impact the overall response time in a conversational setting and the accuracy of the end to end system would be very helpful 

While figure 2 serves as the main architecture diagram describing the approach, it is very abstract. The paper could benefit from another figure showing how the controllers were working since those seem to be a key contributor. Again, I assume they rely on some sort of graph algorithm based on the DAG in figure 3 but more information is needed. Including a flowchart showing the decision-making process of the pre-decision and post-decision controllers, or a diagram illustrating how they interact with the DAG structure. This would help clarify the relationship between the controllers and the workflow representation.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper deals with an important topic: that of controlling the responses of an LLM based on a workflow. The authors introduce a new workflow specification language for controlling the LLMs’ responses, called PDL.

### Strengths
The proposed topic is interesting and, certainly, useful. However, several issues in the presentation make it difficult to understand the contributions of this work and the limitations of the state-of-the-art. For example, the authors talk about out-of-workflow queries, however a clear definition/example of such queries is missing. 

As I state at the end of comments/questions to the authors (please see below), I am willing to increase my score if the authors address my comments.

### Weaknesses
*Typos*

Sentence in line 014-015 difficult to understand. Please revise. 

*Presentation issues*

In the paragraph starting in line 042, the authors discuss the pros and cons of prompt-based and rule-based methods. Two comments: 
- References to prompt-based and rule-based methods are missing, making difficult for the readers to understand how the aforementioned approaches work.
- A concrete example demonstrating the issues describe in the paragraph in lines 042--052 is missing (i.e., how the responses of a state-of-the-art prompt-based method and of a state-of-the-art rule-based method a state-of-the-art differ on a specific user question based for a given LLM). I recommend the authors adding such an example as that would help the readers understand concretely the limitations of previous work and appreciate the contributions of the proposed work.    

*Related work*

- A more elaborated discussion on previous work is missing. The only discussion I found is in Section 2.2. 
- Please add a discussion and conduct experiments against work on constrained-decoding using regular expressions, which I find it very relevant to this work:
(1) “Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning” by Sabio Geng et al. 
(2) “Validating Large Language Models with Relm” by Michael Kuchnik et al. 

*Technical questions*

- How PDL differs from other workflow specification languages, not necessarily designed to support LLMs – some references for the authors to consider: 
(1) Serge Abiteboul, Pierre Bourhis, Victor Vianu. Comparing workflow specification languages: A matter of views. ACM Transactions on Database Systems, 2012, 37 (10).
(2) W.M.P. van der Aalst and A.H.M. ter Hofstede .YAWL: yet another workflow language. Information Systems. Volume 30, Issue 4, June 2005, Pages 245-275.
- Following up from the previous question: why cannot we use/extend existing workflow specification languages to constrain the responses of LLMs?  
- In line 050 the author state: “for an existing rule-based workflow, if we want it to support a new demand outside the original procedure, such as helping a user check the weather (the yellow diamond in the figure), significant modifications to the original workflow are required, which becomes impractical as more out-of-workflow demands are required.” How exactly PDL overcomes this crux? This should be demonstrated both via a (toy) example and via experiments.  
- The authors say that their framework can support out-of-workflow queries, however a clear definition/example of such queries is missing, making it difficult to assess the importance of the proposed work.   

*Overall assessment*

A clear positioning of the contributions against the state-of-the-art is missing, making it difficult to understand the novelty of this research. I am willing to increase my score if the authors address my comments/questions.

### Questions
Please see my questions/comments in the above field. In particular: 

- Please give a concrete example from a domain of your interest (e.g., booking a hotel room) showing how prompt-based and rule-based methods from paragraph in 042--052. differ on their responses to a user query and stressing the limitation of the prior art and the contributions of this work. Please also give exact references-- there is no reference in this paragraph. 
- Please create a table or analyse the key differences between PDL and previous established workflow languages (see for example Serge Abiteboul, Pierre Bourhis, Victor Vianu. Comparing workflow specification languages: A matter of views. ACM Transactions on Database Systems, 2012, 37 (10)), particularly focusing on aspects relevant to LLM control.
- Please provide a dedicated subsection defining out-of-workflow queries, along with a few concrete examples demonstrating how these queries differ from in-workflow queries and how PDL handles them.
- Please experimentally compare your framework against one recent constrained-decoding technique using regular expressions, e.g., “Validating Large Language Models with Relm” by Michael Kuchnik et al. The experiment should demonstrate how the authors' approach differs from or improves upon previous constrained-decoding methods in the context of workflow control for LLMs. 
- Please provide a specific toy example showing how PDL handles a new out-of-workflow demand, and include an experimental comparison demonstrating the flexibility of PDL versus rule-based approaches in adapting to new demands.

### Soundness
2

### Presentation
2

### Contribution
2
