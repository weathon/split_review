# Learning through experience:Episodic memory representation for cognitive agents

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
As the demand for intelligent robots and cognitive agents rises, the ability to retain and utilize past experiences through episodic memory has become crucial, especially for social companion robots that rely on previous interactions for task execution. To address this, we introduce Episodic Memory for Cognitive Agents (EMCA), a novel framework that advances knowledge representation by integrating real-world interactions. EMCA enables agents to adapt to complex environments by learning from tasks, interacting with humans, and processing multimodal data—such as speech, vision, and non-verbal cues—without pre-training on specific scenarios.
EMCA models episodic memory through a graph-based structure , allowing for incremental storage and retrieval of experiences. Each interaction or event enriches the memory graph, supporting continuous learning and adaptation without extensive retraining. This human-like memory formation optimizes the agent’s ability to retrieve relevant information for tasks like localization, planning, and reasoning based on prior experiences.Unlike conventional models relying on temporal markers or recurrent patterns, EMCA encodes data like human memory, allowing reasoning across diverse scenarios regardless of temporal patterns. The framework dynamically builds a memory graph with semantic and temporal connections based on the agent’s experiences, promoting flexible temporal reasoning. It also introduces mechanisms for clustering new memories and a dynamic retrieval policy that adjusts based on context or query type, ensuring robustness even in unpredictable scenarios. Empirical tests show EMCA adapts effectively to real-world data, offering reliability and flexibility in dynamic environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents Episodic Memory for Cognitive Agents (EMCA), a framework designed to support memory retention and retrieval in  cognitive agents. EMCA models episodic memory using a graph-based structure that incrementally stores and organizes multimodal experiences—such as speech, vision, and non-verbal cues—without pre-training on specific scenarios. This approach enables agent to keep adding new experiences continuously from data. This supposedly allows for flexible temporal reasoning across different datasets. EMCA’s dynamic memory graph builds semantic and temporal connections, enabling context-aware retrieval and clustering of memories based on query relevance. The framework aims to improve task execution , and reasoning by recalling contextually significant past events. Empirical tests reported indicate that EMCA adapts to real-world data, demonstrating good recall in unpredictable settings.

### Strengths
I think the paper is trying to address a very important problem of how can an autonomous agent keep memoring new experienes and the recall those flexibly based on the context, question or query. Specifcally I see two main strengths.  
Pretrained Models: The model builds on pretrained models that help with extraction of compenents, but this also means the system does not require pre-training on every specific scenario from scratch, which is a significant strength as it allows flexibility across contexts.
Dataset Diversity: The authors evaluated the system on multiple datasets, demonstrating a broad application range, although it should be noted that most of these datasets were developed by the authors.

### Weaknesses
Despite tackling an important problem, the paper suffers from serious clarity and coherence issues that obscure its contributions and weaken its scientific rigor. The presentation is fragmented, key concepts are inadequately explained, and essential technical details are missing, all of which make it challenging to assess the model’s validity and potential impact. Specifically, the weaknesses include:
1. The authors claim EMCA encodes data in a way that resembles human memory, but there is no evidence or detailed explanation to support this claim from a neural encoding way. Such claims should be toned down. You should instead  emphasize on the 'what', 'where' 'when' organisation from a psychological perspective of episodic memory.

2. Insufficient Motivation: The introduction section does not adequately establish the necessity of this system or why it improves upon existing learning frameworks for cognitive agents. Additional motivation for the need of an episodic memory for a cognitive agent would help contextualize EMCA's contributions.


3. Minimal Related Work Discussion: Essentialy the model is an encode and retrival model with some dynamic reorganistion. The related work section is sparse and lacks comparisons to key formal methods like Hopfield networks or other established models in episodic memory encoding and retrieval. A more rigorous comparison to established human memory models would also strengthen the paper.

4. Unclear Implementation and Integration Details: Although multiple models and methods are mentioned, the paper lacks a cohesive description of how these components integrate within the system. Critical details such as model architecture, parameter settings, and processing pipelines are absent, making it difficult to assess or replicate the work. A system architecture diagram, a table of key parameters, or pseudocode for the main processing pipeline would help.

Vague Statistical Estimation Methods: The paper mentions the use of statistical methods for estimating missing timestamps but does not specify which methods were used, leaving an important aspect of the framework unexplained.

Surface-level Comparison with Temporal and Knowledge Graphs: The comparisons with temporal and knowledge graph structures are brief and lack depth, offering limited insight into how EMCA differs from or improves upon these existing approaches.

Undefined Terminology and Variables: Certain terms and variables (e.g.,"key events", "location weight," "subjective temporal timescales") are introduced without sufficient explanation or definition, reducing clarity.

Overreliance on Custom Datasets: While the use of various datasets to evaluate EMCA is a strength, most of these datasets were developed by the authors, which could indicate potential biases in testing and validation.

Limited Explanation of Retrieval Policy: The retrieval policy and memory clustering mechanisms, while central to EMCA’s functionality, are described only briefly. A more detailed explanation would clarify how these mechanisms adapt to different query types and scenarios.

### Questions
Statistical Estimation Methods for Timestamps: Which specific statistical methods are used for estimating timestamps in the absence of explicit temporal markers?

Union of Tacoustic and Tvoiced: In combining Tacoustic and Tvoiced, what is the methodology for performing this union? Is Tvoiced identical or related to another variable, such as St?

Format and Extraction of Visual Details: What is the format of the visual scene details (e.g., Vscene, Vplace, Vtime), and how are these extracted and integrated into the memory graph?

Defining Key Events and Hierarchical Organization: How are key events identified, and what hierarchical structure is used to organize these events?

Relation between Taudio and Tcombined: Is Taudio equivalent to Tcombined, or is there another relationship between these variables?

Task Categories for Text Summarization: How are text summaries grouped into broader task categories (e.g., meetings, lunches)? What criteria and process are used to define these categories?

Similarity Calculation in Equation 8: Equation 8 is intended to measure similarity between an event and multiple episodes, but it isn’t clear how it accomplishes this. Could you clarify how this calculation works?

Location Weight Definition: How is "location weight" defined, and how does it differ from location similarity in the model?

Temporal Parameter in Equation 14: In Equation 14, should the parameter be (t-k) instead of just t? If not, what purpose does the current form of the equation serve?

Meaning of "Agent Comprehends": In line 274, it says the "agent comprehends" something. Does this imply processing by a language model, and if so, could you clarify which model is used?

Definition of the Set Du: How is the set Du defined in the context of the framework?

Similarity Function in Line 283: Which similarity function is used in line 283, and what factors are considered?

Role of w and l Functions: In line 287, the w and l functions are mentioned. Could you elaborate on their roles within the memory retrieval mechanism?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce Episodic Memory for Cognitive Agents (EMCA) that models episodic memory based on a graph-structure. This allows them to incrementally store memories and retrieve experience. They also can cluster memories, have dynamic retrieval, and can handle temporal reasoning. Memory is structured as a graph, where each episode contains characters, temporal elements, location, and events. The edges of this graph can be temporal or semantic. They then build a retrieval system that can handle contextual, temporal, and spatial queries.

### Strengths
- The Big Bang Theory and the Agent datasets seem very useful! 
- Their results indicate that their method performs better than other graph-based approaches. 
- This area is a growing field, especially as robots and agents become more capable and need better ways to scale their context. And their graph-based approach seems to be a meaningful contribution
- Table 2 is interesting, as it showcases that some of their questions require access to vision, acoustics, and/or dialogues. This result would be better if we knew what the Big Bang Theory and Agent dataset contained.

### Weaknesses
## Main weaknesses
- After reading the full paper, I am not sure what the actual task is. What commands does the master ask? I understand the approach, but not what task it is specifically solving. Is the output the location of a specific memory? Or is it a free-form text answer?
- In terms of the structure of the paper, I do not think that the text space used for discussing how signals are captured (section 3.1) is very useful. I would argue this is the case with a chunk of this paper's equations, where it simply adds space when it does not need to, and it makes the paper more difficult to read. I would recommend condensing the information and matching ICLR's 9-page recommendation as opposed to 10. Similarly, there is an excessive use of new lines at arbitrary positions.
- There is no discussion on how the Big Bang Theory and Agent datasets were constructed. This on its own seems like a major contribution on its own. I would recommend the authors remove much of the superfluous equations and newlines (and move that into the appendix), and put more of an emphasis on this dataset component.
- I think I like what Section 4.1 is implying about combining a "master's" memory with that of an agent's, but it is not presented very clearly, and I do not see a connection with temporal graphs like the subsection title suggests
- Nor do I see how this section is a "theoretical comparison"
- "Master" terminology in line 346 is confusing, and should be introduced earlier in section 4.1. Also, the term "master" is generally frowned upon in these settings, so I would recommend a different term
- Results are poorly presented


## Formatting/Clarity issues:
- Check for spaces after periods or colons throughout the paper.
- Line spacing is odd in much of the paper
- Figure placement should ideally be on the top or bottom of a page, not in the middle with paper text above and below the paper. This makes the paper difficult to follow
- Figure 4, the legend has oddly shaped circles
- Figure 5's result is good, but it should not be a line graph with x axis being method and lines being the dataset. Instead it should be datasets on the x-axis and methods on the y-axis
- The results in section 5.1.1 are all discussed in a single paragraph. Is that all the main results? I would recommend splitting this up into a few bolded mini-sections and showing the main takeaway of each figure along with highlights on how the method performed, possibly with qualitative results.
- The focus of the introduction on falls a bit flat. Rather than focusing on the historical definition of episodic memory, focus more on how people have been engineering and building these kinds of systems. Focus on why other systems do not work, and why yours does.
- I would recommend larger fonts for the figures; they are difficult to read in the paper.

### Questions
- How was the dataset constructed? This is a major contribution that is not discussed.
- What does a successful or unsuccessful example look like? I would recommend looking at [2] or [3] above to see how to discuss dataset creation in such a setting.
- In Table 1, what metric is being used? It does not say in the caption or the table. It should be re-iterated in the table itself.
- Is a forgetting mechanism necessary, or would it be more like a memory aggregation mechanism so that retrieval is still efficient?
- How does the incremental storage/retrieval scale as the number of episodes change? This result is not displayed in the paper but I would argue is very important. If you only used say 10 episodes of EM instead of 181, is there a difference in performance? This would directly support contribution number 2 in Section 1 of your paper
- What is "Time complexity" in Table 3? Time complexity of BFS is O(V+E), but here a number is used instead. Authors should use "retrieval time" or something similar instead of time complexity.
- Can the authors describe the main takeaways of Section 4? I still do not understand the insights this section is supposed to provide.
- Also, there are some questions/concerns in the weaknesses section


Overall, I like the paper. But I think there are a lot of issues with how to content is shown to the reader that makes the paper's contributions fall flat. In its current state, I would recommend rejecting the paper, but if the authors address my concerns above, I believe I would lean more towards accept.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents Episodic Memory for Cognitive Agents (EMCA), a novel framework that enables AI systems to retain and utilize past experiences through a graph-based memory structure. The key innovation lies in its ability to: 1) Process multimodal data (vision, speech, non-verbal cues) without requiring pre-training; 2) Dynamically build and update memory representations through a graph structure with semantic and temporal connections; 3) Adapt to complex environments through continuous learning from interactions.

### Strengths
originality: graph-based episodic memory structure multimodal processing without pre-training, dynamic clustering

quality: comprehensive testing on multiple datasets, benchmarking against exsiting methods, systematic component analysis in ablation study

clarity: clear problem formulation, good visual aids explaining complex concepts

significance: adresses crucial challenges in cognitive AI, social robot applications, potential impact on memory assistance systems

key innovations: 
1) removes pre-training requirements
2) enables continuous learning
3) provides real-time processing campability

### Weaknesses
1. Scalability limitations: Does the graph structure grow exponentially with experiences? What are the computational costs? It is unclear how the graph's node and edge creation scales with the number of episodes, and whether the system maintains acceptable performance with a large number of nodes. The paper should provide a more detailed analysis of the graph's growth rate, considering both node and edge counts as the number of stored episodes increases. The current analysis lacks a rigorous treatment of the computational complexity of the graph traversal and update algorithms.
2. More details about the Big Bang Theory dataset are needed. The description of the dataset is insufficient, lacking details on the annotation process, the types of questions asked, and the specific challenges it poses for episodic memory. The paper should clarify how the dataset was constructed, including the criteria for selecting episodes and the method for generating questions. It should also discuss the dataset's limitations and potential biases.
3. More implementation details about the method in section 5.0.2 should be provided. The description of the method in section 5.0.2 is too high-level, lacking specific details about the algorithms used for graph construction, node embedding, and memory retrieval. The paper should provide a more detailed explanation of the implementation, including pseudocode or algorithmic descriptions, to allow for reproducibility and a better understanding of the technical details.
4. Forgetting is one of the key problems in memory systems - how does the paper assess and handle memory retention and decay? The paper does not adequately address the issue of memory decay and forgetting. It is unclear how the system handles outdated or irrelevant information, and whether it implements any mechanisms for memory pruning or consolidation. The paper should discuss the strategies used to manage memory decay and provide experimental results demonstrating their effectiveness.
5. What is the real-time performance? The paper lacks a detailed analysis of the system's real-time performance, including latency measurements for memory retrieval and update operations. It should provide a more comprehensive evaluation of the system's speed and efficiency, especially in real-time scenarios.
6. The paper tries to claim episodic memory for agents and robots, but robotic interaction with the environment is different from and much harder than agent interaction in a virtual environment. It is better to make a clear definition and scope. For instance, in L391, "robot's episodic memory" should be "agent's episodic memory". The paper's claims about the system's applicability to robotic episodic memory are not well-supported, given the significant differences between virtual and real-world environments. The paper should clearly define the scope of its contributions and avoid overstating the system's capabilities in real-world robotic applications. The current evaluation is limited to virtual environments, and the paper should acknowledge the challenges of transferring the approach to physical robots.
7. Can authors provide the code and dataset for evaluation? The lack of publicly available code and datasets limits the reproducibility and verifiability of the results. The paper should clearly state whether the code and datasets will be made available to the research community.
8. Repeated paragraph: L054-L062
9. Subtitle formatting issue in line 480

### Questions
1. Will the code and datasets be made publicly available?
2. How does the system maintain temporal consistency without explicit time markers? Can you provide quantitative results comparing temporal reasoning accuracy with and without explicit timestamps?
3. What are the specific model architectures and hyperparameters used?
4. What are the computational costs for memory retrieval at different scales?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a novel method for storing multi-modal episodic memories. The design takes inspiration from a model of human memory. More specifically, the paper introduces a novel type of memory graph with different types of connections. The method compares favorably against baselines in experiments.

### Strengths
The paper tackles and interesting problem. The architecture is described in an intuitive way and seems sound and novel. The experiments are reasonably extensive with comparisons to baselines, multiple datasets, and ablations and show very promising results.

### Weaknesses
 - I found the paper to have some "false advertising":
  - Some of the introduction, motivation, and discussion circles around 'robots', I didn't see anything specific to robots in this paper. Yes, it could be integrated into a robot, but the method would equally well work for a body cam, social agent, etc. In robotics there is quite an extensive literature on 'lifelong learning' that covers some of the same challenges: what to memorize, how to store and to retrieve, how to generalize, what to forget, etc.
  - The title says 'learning'. At least according to my definition there is no learning in the paper. It proposes a way to store information and to retrieve it, so that would correspond to 'memorization' (=rote learning), while learning implies understanding the information and being able to apply it to new situations. The method could serve as a starting point for learning, but in the current paper that doesn't seem to be present in the method nor in the experiments.
  - The introduction makes it sound like a general method. But I have a few doubts about that. There are quite a lot of design choices, and some of choices in Sect. 3 seem rather specific. In the end the method is evaluated with a question answering task. What would need to change for a different task, say for a robot learning low-level movement control? Please clarify the generalizability of your method. Specifically, it would be nice if you could discuss how your approach might be adapted for different tasks (such as robot movement control), or explain any limitations in its applicability to other domains.
- Section 3 describes the method. It remains however very much on the level of HOW, rather than providing many insights in the WHY (reasoning behind design choices, consequences of design choices) and it isn't always clear what is a core part of the method and what is an implementation detail. Please provide more explanation for the key design decisions, discussing the rationale behind these choices and their potential implications. Additionally, please clearly distinguish between core methodological components and implementation details.
- Fig. 5 isn't very convincing (except for Arigraph)
- Memory requirement would be another interesting metric for comparing methods.
- The paper mentions the missing forgetting mechanism as a major limitation. Related to that it also leaves the question on 'what to store' unanswered. It reads like everything is stored, even if it is effectively a duplicate. I believe the real challenging question that needs to be solved is the memory management: what to store, what to consolidate/merge, what to forget, etc. Without those a memory representation is of limited value, and it remains unclear to me how suitable the proposed architecture is for extending it in that way - or if we would be better off redesigning it from scratch.
- The method relies on various models to extract features and to summarize things before storing them. I don't believe there is a 'one size fits all approach' but how to best do that depends on the retrieval task and the type of downstream tasks you have. The paper does not provide any indications on how to deal with that.
- There are a whole lot of design choices in this paper, an ablation on only the modalities and search methods seems a bit limited. There also is no sensitivity analysis for e.g. the clustering thresholds
- This seems to be a rather complex system, which makes reproducing results very difficult, with probably quite lot of additional implementation and setting details. I couldn't find any promises to release code (or at least a detailed appendix), which would have alleviated this concern.

### Questions
- The paper seems to miss all details on how the responses are generated, but the whole experiments are based on evaluating the answers. Please provide a detailed explanation of your response generation process, as this is crucial for understanding and evaluating the experimental results.
- Sect. 3.2.4: This seems to result in just 'jumping' nodes. Conserving the chronological structure is a nice property, but the real question/challenge rather is on the side of the module that determines if there is any harm in 'skipping a step', e.g. when thinking about some of the uses-cases 'predict ... next activity' you mention
- Quite a lot of unclear details
  - Eq (1) vs (2): the difference between S_T and T_voiced is unclear
  - How is T_acoustic generated
  - Sect. 3.1.2, 3.1.3, and 3.2, l. 218: at places the paper sounds like everything is represented as 'text', at others it seems to be a mixture of text and other embeddings. It would be great to explain earlier on what it stored as what
  - l. 184: "organized by place, characters, and events" raises the question where those come from - that is explained later in the text
  - l. 220: "relevance of these tasks is assessed" - again HOW?
  - l. 212: what are the implications/limitations resulting form using a simple metric like cosine similarity?
  - Eq (17) sim seems undefined
- Fig. 2 and Sect. 4.1: I didn't get the terminology "master". Maybe that term can be avoided altogether (similar to https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/m/master-slave )
- The paper comes across as unpolished
  - missing and extra spaces - e.g. in the title and abstract
  - the template uses natbib, not using correct commands for references \citep \citet (and resulting repeats of names) makes it painful to read
  - LaTeX has different opening and closing quotation marks
  - paragraph above "Contributions" is double
  - broken sentences in Sect. 5.1.2
  - a few references with incomplete info (e.g. l. 300 "as shown in 4", l. 191, l.468)

##After rebuttal
I appreciate the very detailed replies. However, I still believe the paper is not ready to be published and will maintain my score (see message below).

### Soundness
3

### Presentation
2

### Contribution
2
