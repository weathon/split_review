# The Labyrinth of Links: Navigating the Associative Maze of Multi-modal LLMs

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
Multi-modal Large Language Models (MLLMs) have exhibited impressive capability. However, recently many deficiencies of MLLMs have been found compared to human intelligence, \textit{e.g.}, hallucination.
To drive the MLLMs study, the community dedicated efforts to building larger benchmarks with complex tasks.
In this paper, we propose benchmarking an essential but usually overlooked intelligence: \textbf{association}, a human's basic capability to link observation and prior practice memory.
To comprehensively investigate MLLM's performance on the association, we formulate the association task and devise a standard benchmark based on adjective and verb semantic concepts.
Instead of costly data annotation and curation, we propose a convenient \textbf{annotation-free} construction method transforming the general dataset for our association tasks.
Simultaneously, we devise a rigorous data refinement process to eliminate confusion in the raw dataset.
Building on this database, we establish three levels of association tasks: single-step, synchronous, and asynchronous associations.
Moreover, we conduct a comprehensive investigation into the MLLMs' zero-shot association capabilities, addressing multiple dimensions, including three distinct memory strategies, both open-source and closed-source MLLMs, cutting-edge Mixture-of-Experts (MoE) models, and the involvement of human experts.
Our systematic investigation shows that current open-source MLLMs consistently exhibit poor capability in our association tasks, even the currently state-of-the-art GPT-4V(vision) also has a significant gap compared to humans. 
We believe our benchmark would pave the way for future MLLM studies. 
\textit{Our data and code are available at:} \url{https://mvig-rhos.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work proposes a new benchmark testing the zero-shot association ability of MLLMs. Association origins from object concept learning, where the task is to connect observations with previous practice memory by identifying the underlying principle. For example, images of fresh apples,  oranges, vegetables could be connected through the adjective "fresh". It is a fundamental capability for humans. The proposed benchmark leverage previous datasets of object concept learning and is created in an annotation-free way. Basically, the labels in datasets of object concept learning directly provide the underlying principle (concept) that could connect objects.

The authors designed different settings to test MLLMs' zero-shot association ability: single-step vs multi-step, synchronous vs asynchronous. According to the reported results, all the leading MLLMs show a gap in terms of the association ability, compared to humans.

### Strengths
**originality**
The originality is good. The work proposed and will open-source a new benchmark for MLLMs, by transforming a previous ML benchmark into a LLM benchmark.

**significance**
It shows all MLLMs have an obvious gap vs humans. In this sense, the benchmark is able to evaluate and push an overlooked capability towards AGI.

### Weaknesses
 **quality**
There are two aspects that improvements could be made on. First, regarding error analysis, more insights are preferred. For example, by "limited perception capability", is it due to the limitation of image encoder/resolution or something intrinsic to LLMs. Most public MLLMs are composed of a separate image encoder+adaptor and the main LLMs. Some ablation studies on this aspect are preferred. Second, checking the correlation between this new benchmark and existing benchmarks is preferred. For example, if the performance on this new benchmark is strongly correlated with a weighted sum of those on some existing benchmarks, we could better know how to improve such a capability. If no correlation, this work might point out an overlooked dimension, which could also motivate more related benchmarks to be created.

**clarity**
The presentation could be improved a bit, by adding more clear examples. For example, Figure 7 in the context is better in explaining the exact task than Figure 1. And adding figures for the annotation-free transformation from object concept learning datasets can better explain the exact dataset building process.

### Questions
1. I don't see a clear argument on why sticking to zero-shot setting? As there is a practice memory involved, is it also naturally similar to few-shot?
2. Why does the study only focus on MLLMs? Is it because the object concept learning dataset is for multi-modal initially? How hard is it to make a text-only corresponding benchmark?

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
This paper proposed an evaluation benchmark, which evaluates multimodal large language models' performance on predicting association in three scenarios: single-step association, synchronized multi-step associations, and asynchronized multi-step associations.

### Strengths
1. This paper proposed a novel task and a perspective on MLLMs.

2. Various MLLMs are tested on the benchmark.

### Weaknesses
1. The definition of the task "deduction" in Table 1 could be better explained and illustrated like the "association" task in Figure. 2.

2. It would be essential to include human performance in Table 1 to understand current gap between MLLMs and human. In addition, the authors might consider including more recent and powerful GPT-4o performance in Table 1.

3. For Table 1, since MLLMs' performance on the association task is rather high (around 80\% accuracy), there could be concerns about the potential improvement MLLMs can achieve for future works. To understand such, human performance might be a valuable baseline to refer to.

4. The evaluation settings in the synchronous association task in Figure 3 could be difficult to understand. The authors might consider better explaining their inputs and expected outputs and their metric calculation as some pseudo-code.

5. The performance comparison in Figure 3 is not very insightful, which might lacks proper explanations about why MLLMs are significantly inferior to human judgement. Such significant gap could raise concerns about the effectiveness of the proposed evaluation protocol.

6. The illustration of Figure 6 is not very self-explainable, while its textual explanations in context are also very brief, which could hinder readers understanding of the major concerns in current MLLMs on such tasks.

### Questions
1. Could the authors explain the input and expected output of the single-step "deduction" task? Since the benchmark is claimed to evaluate MLLMs' ability in association prediction, whether deduction is part of the benchmark? In addition, could the authors explain the relation between the "association" and "deduction" tasks?

2. For the results in Figure 3, since the human expert could achieve hundreds rounds of association, could the authors explain how the length of association is evaluated? Specifically, is the benchmark contains the ground truth of hundreds rounds of associations? Is each prediction on the next association necessarily requires all the previous memories? Are those MLLMs prompted with such long-term association or with only current inputs?

3. What would be the prompting format for such tasks. Are those images concatenated as a single image or separately input into the prompt? Are those images interleaved with proper textual instructions, so that MLLMs could understand the intention correctly? In addition, is the proposed tasks formatted as multi-choice question-answering tasks, where generated answers could be well mapped to ground-truth?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a novel benchmark aimed at evaluating the association capabilities of Multi-modal Large Language Models (MLLMs), a crucial yet often overlooked aspect of human intelligence. The authors formulate a specific association task based on adjective and verb semantic concepts and introduce an innovative annotation-free method for constructing these tasks, minimizing the reliance on expensive data annotation. They implement a rigorous data refinement process to enhance dataset clarity and present three levels of association tasks: single-step, synchronous, and asynchronous. The investigation covers a wide range of MLLMs, including both open-source and closed-source models, exploring various memory strategies and involving human experts. Findings reveal a significant performance gap between current MLLMs, including state-of-the-art models like GPT-4V, and human capabilities in association tasks. It implies that this benchmark could advance future MLLM research.

### Strengths
1. **Originality**:
   - The benchmark specifically targeting association capabilities represents a unique contribution to the MLLM literature. While benchmarking is prevalent, focusing on association adds a novel dimension to the evaluation of language models.

2. **Quality**:
   - The authors' annotation-free construction method for association tasks is a practical innovation that alleviates the common challenges associated with extensive manual data labeling, enhancing the quality and usability of the benchmark.

3. **Clarity**:
   - The paper is well-structured and clearly articulated, with straightforward definitions and explanations of association tasks. This clarity facilitates comprehension and accessibility for a broad audience.
   
4. **Significance**: 
   - By highlighting the substantial gap between MLLM performance and human intelligence in association tasks, the paper underscores the importance of developing models that can better mimic human cognitive capabilities. This sets the stage for future research efforts in enhancing MLLMs.

### Weaknesses
1. **Limited Novelty**:
   - The benchmarking of association capabilities is not entirely novel. Similar efforts can be found in previous research focusing on common sense reasoning, such as "CommonSenseQA" and "HellaSwag," which also evaluate reasoning and associative capabilities. While the authors focus on adjectives and verbs, the core concept of evaluating associative reasoning is not new, and the paper could benefit from a more detailed comparison with existing benchmarks to highlight its unique contributions beyond the specific semantic focus.

2. **Subjectivity in Tasks**:
   - Association tasks can be influenced by subjective interpretations, yet the paper does not sufficiently address how such subjectivity is mitigated. The paper lacks a detailed discussion on the potential for varied human interpretations of associations, especially in the context of the prompt design for MLLMs. For example, in analogy tasks, different individuals might perceive different relationships between concepts, and the paper does not specify how these variations are controlled or accounted for in the evaluation.

3. **Resource Intensiveness**:
   - The comprehensive nature of the study, involving multiple models and memory strategies, raises concerns regarding reproducibility. The resource demands, including computational power and time, may hinder wider adoption among researchers with limited computational resources. The paper does not provide sufficient detail on the specific hardware and software requirements, making it difficult for other researchers to replicate the experiments.

4. **Experimental Design**:
   - The rationale for selecting specific MLLMs could be more thoroughly explained, and comparisons with existing benchmarks would strengthen the justification for the new benchmark's necessity. The paper does not clearly articulate why the chosen models were selected over other available MLLMs, nor does it provide a systematic comparison with existing benchmarks to demonstrate the unique value of the proposed benchmark.

5. **Discussion Depth**:
   - The discussion section could delve deeper into the implications of the findings, particularly regarding practical applications and theoretical contributions to AI and cognitive modeling. The paper's discussion lacks a thorough exploration of the broader implications of the observed performance gap between MLLMs and human intelligence, and it does not adequately discuss the potential practical applications of the benchmark.

6. **Performance Gap Exploration**:
   - While the performance gap between MLLMs and human intelligence is significant, the paper could provide more in-depth analysis of the causes and potential paths toward bridging this gap. The paper does not offer a detailed analysis of the underlying reasons for the observed performance gap, nor does it propose specific strategies for improving MLLM performance in association tasks.

7. **Bias in Dataset Annotation**:
   - The paper lacks clarity on how biases in the initial dataset annotations are addressed, which could affect the robustness of the findings. The paper does not provide a clear methodology for identifying and mitigating potential biases in the initial dataset, which could impact the validity of the results.

### Questions
1. **Rationale for Focus**: What is the rationale behind selecting adjectives and verbs as the focal point for your semantic concepts in the association tasks?

2. **Bias Mitigation**: Regarding equation (1), where \(z_{ij}\) is constrained to 0 or 1, could this introduce bias from human evaluations? How can this bias be effectively removed from the assessment?

3. **Overlooked Capability**: Can you elaborate on why you believe the association ability of MLLMs has been overlooked in previous research?

4. **Novelty Clarification**: How does your proposed benchmark differentiate itself from existing benchmarks assessing association and reasoning capabilities in language models?

5. **Bridging Performance Gaps**: Given the performance gap observed, what advancements do you foresee as crucial for future MLLMs to approach human-level performance in association tasks?

6. **Resource Considerations**: How can researchers with limited resources effectively utilize your benchmark, considering its resource-intensive nature?

7. **Model Selection Criteria**: What criteria informed your selection of specific MLLMs for this study, and how do you view these models in the context of the current state of MLLM research?

8. **Future Implications**: How do you envision your findings influencing the design of future MLLMs and the benchmarks used for their evaluation? What next steps do you recommend in this line of research?

9. **Evolving MLLM Performance**: As MLLMs continue to evolve and improve in association tasks, how do you anticipate the relevance of your findings will change?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a benchmark, using an annotation-free construction method to transform general datasets. The benchmark includes three levels of association tasks: single-step, synchronous, and asynchronous associations. The authors conduct extensive experiments involving multiple open-source and closed-source MLLMs, including state-of-the-art models like GPT-4V, and compare their performance with human experts.

### Strengths
The paper offers a fresh approach to assessing MLLMs by focusing on their associative abilities, which is a novel contribution to the field. The annotation-free construction method for association tasks is innovative and has the potential to simplify the creation of benchmarks in this area.

### Weaknesses
The evaluation is limited to MLLMs’ zero-shot ability in association tasks across adjectives and verb semantic concepts. This may not fully capture the complexity of real-world scenarios where MLLMs are expected to perform.

While the paper analyzes failure cases in the association process, it could have provided a more in-depth understanding of why these failures occur. 

The paper focuses on single-step, synchronous, and asynchronous associations, which are complex tasks. However, it might not fully capture the nuances of human associative learning, which often involves more gradual and contextually influenced processes.

### Questions
How might the authors' findings on the associative capabilities of MLLMs influence the design of future models, particularly in terms of memory and reasoning architectures?

Are there any specific areas of application where the authors believe the current gaps in associative capabilities are particularly problematic, and thus, warrant immediate attention in research?

How did you ensure that the limitations of the original datasets did not significantly affect the results?

### Soundness
3

### Presentation
3

### Contribution
3
