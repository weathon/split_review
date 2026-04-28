# COOL: Efficient and Reliable Chain-Oriented Objective Logic with Neural Networks Feedback Control for Program Synthesis

- Decision: Reject
- Avg Score: 2.50
- Scores: 1, 1, 5, 3

## Abstract
Program synthesis methods, whether formal or neural-based, lack fine-grained control and flexible modularity, which limits their adaptation to complex software development. These limitations stem from rigid Domain-Specific Language (DSL) frameworks and neural network incorrect predictions. To this end, we propose the \textbf{Chain of Logic (CoL)}, which organizes the synthesis process into an activity flow and provides heuristic control to guide the process. Furthermore, by integrating neural networks with libraries and introducing a \textbf{Neural Network Feedback Control (NNFC)} mechanism, our approach modularizes synthesis and mitigates the impact of neural network mispredictions. Experiments on relational and symbolic synthesis tasks show that CoL significantly enhances the efficiency and reliability of DSL program synthesis across multiple metrics. Specifically, CoL improves accuracy by 70\% while reducing tree operations by 91\% and time by 95\%. Additionally, NNFC further boosts accuracy by 6\%, with a 64\% reduction in tree operations under challenging conditions such as insufficient training
data, increased difficulty, and multidomain synthesis. These improvements confirm COOL as a highly efficient and reliable program synthesis framework.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The submission discusses a technique for synthesis of logical rules from data.

### Strengths
n/a

### Weaknesses
The paper fails at presenting the contribution, and I am not able to provide a review of the actual contribution due to the presentation.

After reading the paper, I do not know
* what the form of the actual inputs to the system are, and how a user would interact with it
* how the components of the system are constructed (i.e., what is "DSNN" - is it a feed-forward network? An LLM? What shape does its input take? What is its actual output? Similarly, THD, SSPH, SGH are only explained at the highest possible level)
* what ideas can transfer to other contexts

The only way forward I see is to rewrite the entire submission. I would recommend to ask colleagues who are not closely familiar with this project to review draft submissions, and provide feedback on whether they understand what you are trying to present, before submitting the paper again.

### Questions
n/a

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper describes a form of program synthesis called COOL and applies it to the CLUTTR dataset (logical family relation problems embedded in natural language) and a toy quadratic equation dataset. COOL is a combination of a "Chain of Logic" (CoL) DSL and a neural network feedback control system (NFCC) for guiding search. CoL is a framework for sketching templates of useful DSL rule applications to guide the problem solving process. For example, for the CLUTTR dataset, the CoL DSL contains rules "Separate relations and genders", "Reason inverse relations", "Reason Indirect Relations", "Recombine relations and genders, eliminate irrelevant info", while the CoL DSL for quadratic equations contains rules such as 0 + a = a, (a + b) ^ 2 = a^2 + 2ab + b^2. NFCC is a complicated system that uses neural networks to guide and control the synthesis process. Program search is conducted with A* using heuristics I believe from the neural network. The authors show that COOL achieves 100% accuracy, uses fewer tree operations, and spends much less time solving compared to the baseline of a normal DSL without NNFC.

### Strengths
The paper is very thorough and complex. There is a lot of detail and technical content. I have never seen a control system like that used for the neural network feedback control and it seems like a very novel way of synthesizing programs. While I don't fully understand it, the authors analysis of inner coupling as a key factor to the improved synthesis quality of COOL seems interesting.

### Weaknesses
I find this paper very hard to understand.

The method is very complicated, with a lot of moving parts. The method is never described end-to-end in a coherent way — instead, bits of detail are mentioned throughout the paper, but I never get the sense that I fully understand what is going on. Some questions that I cannot answer from reading the paper: how are the neural networks trained? how are the heuristics computed? what is the input and output for a given synthesis problem? what are tree operations? One of the datasets, the quadratic equation dataset, is only described at a high level — I don't even know what the problems look like exactly.

I would recommend writing the paper in a more linear order. Even if there is not space in the main text, the appendix can contain a full description of the (1) problem input and output, (2) overview of algorithm that transforms input to output prediction, (3) description of how your techniques plug in to the algorithm at different parts. You can also include more detailed definitions for things like tree operations, the DSL rule definitions, etc.

Overall, I am baffled at this paper. I am not foreign to program synthesis, yet most of the content of this paper is beyond me.

To summarize, the technique is extremely complicated and not adequately explained. This is the main weakness of the paper.

Beyond this, the evaluation is not very convincing. This is in large part due to the poor explanation — as stated earlier, I don't have a full understanding of what the input and output for each problem is, or even how search is conducted. So it's hard to know what to make of the accuracy metrics or time spent. "tree operation" and "transformation pair" are not defined either.

### Questions
See weaknesses section for questions

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces a neuro-symbolic program synthesis method that combines rule-based logic with neural feedback, termed Chain-Oriented Objective Logic (COOL). This technique allows fine-grained control over search processes within DSL-induced program spaces. Modularity is achieved through a component called Chain of Logic (CoL), inspired by the activity diagram model from software engineering and system control. CoL structures complex rule applications by assigning heuristic values to rules, enabling more efficient search strategies. Selecting specific rules based on heuristic values at particular stages (e.g., returning, jumping, or terminating synthesis branches) enhances search efficiency by aligning rule applications with promising paths, akin to human problem-solving approaches.

The paper also introduces Neural Network Feedback Control (NNFC), which uses multiple neural networks in series with specific heads for task detection, search pruning, and guidance. This prioritizes rules and tasks, allowing the synthesis process to bypass infeasible paths early, thereby improving the quality of synthesized outputs.

Experiments were conducted on static and dynamic benchmarks, categorized by difficulty level. The results validate both the general applicability of the approach and impressive improvements in accuracy and search efficiency under different task demands. A detailed ablation study clarifies the contribution of each component.

### Strengths
1. The ideas introduced in the paper are interesting. The Chain of Logic structure mirrors human problem-solving steps, allowing for more intuitive management of the program synthesis process within the DSL. This hierarchical structuring likely enhances interpretability.
2. The paper provides some experimental validation, with ablation studies showing the contribution of each component.

### Weaknesses
1. The CoL framework is highly domain-specific, and it is unclear how adaptable it would be for tasks outside its designed domain. The reliance on activity diagrams suggests that applying CoL in other fields may require substantial modification, limiting generalizability. The core of CoL seems to be tied to the specific rules and heuristics defined within a given DSL, making it unclear how these would be transferred or adapted to a new DSL with different syntax and semantics. For example, if the DSL were to shift from symbolic manipulation to, say, natural language processing, the heuristic vectors and keywords would likely need a complete overhaul, which raises questions about the framework's reusability.
2. The description of NNFC is somewhat opaque, especially regarding how incorrect neural network predictions are “suppressed through filtering.” The paper lacks a clear explanation of the mechanism by which the series of neural networks in a DSNN interact to achieve this filtering. It is not clear how the system identifies unreliable predictions from upstream networks and how this information is used to prevent downstream networks from propagating errors. The absence of specific details about the thresholds used for cross-validation and the precise nature of the comparison between upstream and downstream network outputs makes it difficult to assess the robustness of this filtering process.
3. There is insufficient detail about the design choices behind the Domain-Specific Neural Networks (DSNNs), such as how they are trained and what training data or ground truth is used, especially when handling partial programs. The paper does not specify the architecture of the neural networks, the loss functions used during training, or the optimization algorithms employed. Furthermore, it is unclear how the DSNNs are trained to handle partial programs, which are inherently incomplete and may not have a clear ground truth. The paper also lacks information on the size and diversity of the training datasets, which are crucial for the performance of neural networks.

### Questions
1. The process by which DSNNs generate error signals from partial programs is not clearly explained. What constitutes a “correct” path in the training process? Is there a universal ground truth, or does it vary by domain? Also how much data does each DSNN require to perform effectively?
2. Did the dynamic experiments include any resource constraints (e.g., time or computational power limits)?
3. I did not understand what “multidomain tasks” are and what is their role in the experiments. Can you clarify please?

### Soundness
2

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
I do not feel I have a sufficient understanding of this paper to summarize it in detail. See the Weaknesses section for details on this. My best attempt to summarize this paper follows.

COOL is a system for neurosymbolic program synthesis, in which programs are generated incrementally in a DSL annotated with specific kinds of assertions and guides that allow for specific guidance of the neural network that drives the search. This leads to significant pruning, improving accuracy while reducing the size of the search space.

### Strengths
The results seem very impressive, showing both an improvement in performance and a reduction in computational cost.

### Weaknesses
This paper provides insufficient details and precision for a reader to understand the nature of the algorithm. The following questions remain unanswered by the introduction, figures, and methods section: What is the artifact a user of this system needs to provide? The baseline is to provide a DSL, what additional information needs to be provided to use COOL?

The details on the amount of effort a user needs to complete to make a DSL in COOL are crucial because without this information, it is unclear how much of the benefits shown in the results section are downstream of the user providing more scaffolding and thus making the task easier.

The figures do not help clarify this to a reader as it is not clear whether they represent the user-provided activity diagram, an execution trace for an activity diagram, or a schematic explanation of how the algorithm functions. It is also unclear what heuristic vectors are, and when logic jumps / abort commands should be used, or even if these are being written by a programmer or the output of some neural network.

Additionally, it is never specified how the DSNN network is trained. How is the data gathered for the DSNN? Is it trained via supervised learning, some kind of wake/sleep loop, or reinforcement learning? What does it mean for the DSNN to be pretrained?

### Questions
See Weaknesses section for a series of questions regarding this system.

### Soundness
1

### Presentation
1

### Contribution
2
