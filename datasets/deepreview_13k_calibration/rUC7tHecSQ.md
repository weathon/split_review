# Mechanism and emergence of stacked attention heads in multi-layer transformers

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
In this paper, I introduce the \textit{retrieval} problem, a simple reasoning task that can be
   solved only by transformers with a minimum number of layers. The task has an
   adjustable difficulty that can further increase the required number of layers
   to any arbitrary value. I demonstrate that large language models can solve
   the task under different prompting formulations without any fine-tuning. To
   understand how transformers solve the retrieval problem, I train
   several transformers on a minimal formulation. I find that successful
   learning occurs only under the presence of an implicit curriculum. I uncover
   the learned mechanisms by studying the attention maps in the trained transformers.
   I also study the training process, uncovering that attention heads always
   emerge in a specific sequence.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a novel retrival problem to conduct an empirical but theoretically grounded anaylsis of mechanisms leading to reasoning in transformers. 
Expanding on the induction problem the authors generalize the task to an arbitrary number of inductions steps and introcude a conditional variant. 
The authors demonstrate that current SOTA LLMs struggle with the retrival problem and their performance approaches random guessing with increased problem complexity. 
Experiments on a minimal problem formulation indicate the importance of implicit curricula and highlight a correlation between the difficulty of the task and the number of layers.
Through manual inspection and subsequent experiments the authors identify learned circuits in a subset of attention heads which emerge one head at a time during training.

### Strengths
- The paper makes a strong contribution to the field of mechanistic interpretability and furthering our understanding of the transformer architecture and training behavior. Especially the finding on the sequential emergence of attention heads for reasoning circuits is valuable. 
- The **problem statement** at hand is presented nicely, and the paper follows a logical progression building up to the final insights.
- The **structure and flow of the experiments** are sensible, starting with higher-level analysis and ending in more focused experiments. 
- Furthermore, the experiments were conducted rigorously.

### Weaknesses
 **Readability:** 
- Section 5 "THEORETICAL ANALYSIS OF INFORMATION FLOW" is quite **hard to follow** and requires some time to understand, especially with limited prior knowledge. The notation is dense and the connection to the experimental setup is not immediately clear. For instance, the variables E, F, and subsequent mathematical expressions lack concrete grounding in the context of the transformer architecture and the specific retrieval task. The authors should provide more intuitive explanations and examples, perhaps by explicitly mapping these variables to components of the model and the data used in Section 4. A step-by-step walkthrough of how the theoretical framework applies to a specific example from the experiments would significantly improve readability. 

**Missing clarity:** 
- Large portions of the paper's analysis are **based on a strong assumption**. Key aspects are *Assumption 1* along with simplification of the transformer architecture. The authors should provide further justification for the reasonability of these assumptions and why they would generalize to LLMs. The assumption that "shared token information" is limited to pure token embeddings and positional encodings needs more rigorous justification, especially considering the complex non-linear transformations within transformer layers. An analysis of how this assumption might break down in more complex scenarios, where tokens interact through multiple layers, would be beneficial. For example, the authors could discuss how the assumption might be affected by the presence of non-linearities in the feed-forward networks or by the interaction of multiple attention heads.
- The **real-world example from the discussion section could be used earlier** to better motivate the theoretical analysis and problem statement. The current placement of the example makes it feel disconnected from the core analysis. Integrating this example earlier would help the reader understand the practical relevance of the theoretical framework and the retrieval problem. 

**Generalization:**
- Similarly, the paper would benefit from an analysis on a real-world question-answer dataset, for example. The current experiments are limited to synthetic data, which raises concerns about the generalizability of the findings. An evaluation on a dataset with more complex linguistic structures and semantic relationships would provide stronger evidence for the practical relevance of the identified reasoning circuits. 

**Method:**
- Lastly, the **method of _manually_ reverse engineering** the circuits is only mentioned but **not described in detail**. This severely affects the potential replicability of the paper and makes independent assessments of the methodology challenging. The authors should provide a detailed step-by-step description of the manual reverse engineering process, including the specific tools and techniques used to analyze attention maps and identify circuits. The lack of detail makes it difficult to assess the reliability and validity of the identified circuits.

### Questions
1. Can the authors elaborate on why Assumption 1 should hold for LLMs, as well as how their 
2. From section 4 and Figure 2, I take that all variations of the problem formulations (F1 to F4) include 4 choices, given the random guessing probability of 25%. However,  this does not seem to be the case for F5 "Relatives". Is there a specific reason for that?
3. Do the authors have an intuition of how their results might be generalized to real-world data? It would be valuable to asses if reasoning circuits follow similar emergence patterns during training. However, I assume that the manual identification of circuits is not scalable. 
4. What methods were used to "reverse engineer" the attention head circuits?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a retrieval task to illustrate the source of the reasoning power of hierarchical transformer models. With the retrieval task, the author takes various structures to verify the connection between successful learning and the presence of an implicit curriculum. In my opinion, this work is helpful in understanding the ability of large language models. As descributed in this paper,  a transformer cannot solve the retrieval problem with a specific difficulty unless it has the minimum number of necessary layers.

### Strengths
This is a good joy for understanding the ability of LLM, especially the emergent ability of models.


1.  a novel idea to study the ability of the reasoning ability of LLM.

2. The finding is exciting and fits with human intuition. 

3. The visualization of attention can give describution on how LLM takes retrieval reasoning tasks.

### Weaknesses
1. Can you provide a more complex example? 

2. In my opinion, I hope I can see a general framework that can unify more tasks with your retrieval task.

3.  There are a lot of chapters in the article, and I can't quite understand the relationship between different chapters.

### Questions
Can you describe the definition of the implicit curriculum in detail? In your experiments, I can see the connection between the number of layers and the model's performance, as shown in Figure 4.

The emergent ability of LLM is more depend on depth or width?  This paper mainly analyzes the effect of model depth on emergence ability.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the retrieval problem, a fundamental task that challenges transformers to retrieve information from multiple positions within an input sequence. The authors demonstrate that solving the retrieval problem requires a certain depth of transformer layers.
 This paper explores how large language models and transformers handle retrieval tasks. They introduce two tasks: the retrieval problem and a variant called the conditional retrieval problem. It shows that large language models can solve retrieval tasks without fine-tuning by leveraging complex mechanisms involving multiple attention heads, which emerge in a specific sequence when trained with an implicit curriculum.

### Strengths
● The paper provides insights into how LLMs perform retrieval using attention heads.
● Introducing these tasks gives a clear way to study transformers' retrieval abilities.
● The study highlights the role of learning curriculum in the development of retrieval mechanisms.

### Weaknesses
1. **Lack of Experimental Validation for Theoretical Claims**: Theoretical claims like Theorem 1 lack empirical support, making it hard to verify their practical impact. Specifically, the assertion that the target embedding appears in the residual stream only when \( t \geq \log_3(2D) \) needs concrete experimental validation. The current theoretical framework suggests a specific relationship between the number of layers and the ability to solve the retrieval problem, but without empirical evidence, the practical implications remain unclear.
2. **Insufficient Details on Experimental Setup**:: The paper lacks detailed explanations for key experimental settings. The implicit curriculum (IC) formulation, which performs better than non-IC, is not clearly defined. The description provided does not sufficiently explain how the target vectors are constructed or how the concatenation of tokens forming the retrieval chain is implemented. Additionally, Section 8’s description of manually reverse-engineering circuits lacks detail, making the experiments difficult to reproduce. The process of identifying and validating the mechanisms for each head is not adequately described, leaving a gap in understanding how these conclusions were reached.

### Questions
1. Assumption 1, which requires shared positional or token information for attention between positions, is overly restrictive and conflicts with the flexibility of Transformer models. Transformers are designed to allow any position to attend to any other, enabling them to learn complex relationships without pre-shared information. This assumption limits the model's ability to capture long-range dependencies and generalize to tasks where connections are context-driven rather than based on shared information. I recommend reconsidering this assumption to better align with the strengths of the Transformer architecture.
2. Theorem 1  would benefit from experimental validation. Testing whether the target embedding truly appears in the residual stream only when \( t \geq \log_3(2D) \) would strengthen the claim and confirm its practical relevance. I recommend adding experiments to verify this behavior across different settings.
3. The specific details of the implicit curriculum formulation remain vague, and the reasons for its superior performance are not clearly explained. Additionally, it would be helpful to clarify why the non-IC formulation, which aligns more closely with traditional problem setups, fails to perform well.
4. In Section 8,  "manually reverse-engineering the circuits learned by the transformers" , the specific details of this process are not fully explained. Providing more information on the methodology used to reverse-engineer these circuits, as well as any criteria or steps involved, would enhance the clarity and reproducibility of this analysis.
5. The experimental results need to be validated under more complex settings, such as with longer retrieval steps.
We will increase the score based on the answer to the question.

### Soundness
2

### Presentation
2

### Contribution
2
