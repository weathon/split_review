# CreDes: Causal Reasoning Enhancement and Dual-End Searching for Solving Long-Range Reasoning Problems using LLMs

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 5, 3, 5, 5

## Abstract
Large language models (LLMs) have demonstrated limitations in handling combinatorial optimization problems involving long-range reasoning, partially due to causal hallucinations and huge search space. As for causal hallucinations, i.e., the inconsistency between reasoning and corresponding state transition, this paper introduces the Causal Relationship Enhancement (CRE) mechanism combining cause-effect interventions and the Individual Treatment Effect (ITE) to guarantee the solid causal rightness between each step of reasoning and state transition. As for the long causal range and huge search space limiting the performances of existing models featuring single-direction search, a Dual-End Searching (DES) approach is proposed to seek solutions by simultaneously starting from both the initial and goal states on the causal probability tree. By integrating CRE and DES (CreDes), our model has realized simultaneous multi-step reasoning, circumventing the inefficiencies from cascading multiple one-step reasoning like the Chain-of-Thought (CoT). Experiments demonstrate that CreDes significantly outperforms existing State-Of-The-Art (SOTA) solutions in long-range reasoning tasks in terms of both accuracy and time efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces CreDes, a model designed to enhance large language models (LLMs) for long-range reasoning tasks, addressing two main challenges: causal hallucinations and extensive search spaces. 

To counteract causal hallucinations, the **Causal Relationship Enhancement (CRE)** mechanism ensures accurate causal alignment between reasoning steps by incorporating Individual Treatment Effect (ITE) metrics during training. This addition makes reasoning steps causally consistent with state transitions, reducing errors.

To manage extensive search spaces in complex reasoning tasks, the **Dual-End Searching (DES)** approach initiates search from both the start and goal states, creating a bidirectional search that segments the problem into smaller, manageable parts. This process improves efficiency by meeting in the middle of a causal probability tree.

Together, CRE and DES enable CreDes to perform simultaneous multi-step reasoning, tested in scenarios like Blocksworld and Hanoi Tower, where it significantly improves both accuracy and processing speed over existing methods.

### Strengths
- **Originality**: This work addresses the significant challenge of long-range reasoning in LLMs. The authors’ approach to incorporating **causal metrics (ITE)** into LLM training introduces a promising cross-disciplinary solution, effectively combining causal inference and language modeling to enhance reasoning depth. This innovation could pave the way for further advancements in handling complex, multi-step reasoning tasks in LLMs.

- **Significance**: Empowering LLMs with improved long-range reasoning capabilities is highly significant. It opens up new applications in fields requiring extensive reasoning, such as societal simulation and economic modeling. The potential impact of overcoming existing limitations in LLM reasoning could enable more complex and nuanced use cases across various domains.

- **Quality of Results**: The **results** illustrate the contributions effectively, showing that CreDes achieves substantial improvements over previous methods. Testing across tasks such as Blocksworld and Hanoi Tower validates the model’s capability to handle complex reasoning with higher accuracy and efficiency, underscoring the benefits of the CRE and DES mechanisms.

### Weaknesses
 - **Clarity of Methodology (Section 3)**: The writing in Section 3, especially subsection 3.2, lacks clarity and coherence. Key variables like $Y$ and $W$ are not defined in the appropriate context when first introduced, which makes following the logic challenging. Additionally, it’s unclear how $ITE$ can exceed 1 when working with binary variables, as suggested later in the section. These inconsistencies hinder understanding and suggest that additional clarity and structure are needed for readability.

- **Equation Definition and Consistency**: Several equations raise concerns due to unclear or inconsistent definitions. In Equation 3, it’s stated that $L_{CRE} = \ln(PPL)$, which seems incorrect, as it doesn’t align with the rest of the formulation. Similarly, in Equation 4, the term "coordinates of node $i$" is ambiguous. If this refers to correctness metrics, as previously suggested, using this metric to indicate proximity in the solution space seems tenuous and warrants further justification.

- **Comparative Analysis**: The methods presented in this work are not compared against any other models that also incorporate training. Including a baseline comparison with vanilla Fine-Tuning (especially for CRE, sinceit is the part that requires training). This omission makes it difficult to fully evaluate the model's contributions relative to existing approaches.

### Questions
These questions stem from the weaknesses identified above:

1. Could the authors provide clearer definitions for variables like $Y$ and $W$ when first introduced in Section 3? Additionally, how is it possible for $ITE$ to exceed 1 with binary variables, as indicated later in the text?

2. In Equation 3, why is $L_{CRE}$ defined as $\ln(PPL)$? This does not seem consistent with the rest of the formulation. Could the authors clarify this choice and explain how it aligns with the training objectives?

3. In Equation 4, what exactly is meant by "the coordinates of node $i$"? If these coordinates represent correctness metrics, can the authors provide further justification for using this as a measure of proximity in the solution space?

4. How does the CRE approach compare to vanilla fine-tuning? Including insights into this comparison could enhance the evaluation of CreDes.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a methodology for enhancing reasoning in LLMs. They adopt a two-pronged approach:
1. Firstly, the authors propose a methodology of fine-tuning the model which enhances the 'causal reasoning' of LLMs. 
2. Secondly, the authors propose a dual-end search algorithm to efficiently solve multi-hop reasoning problems which involve a large number of steps.

### Strengths
1. The paper tackles the important problem of long-range reasoning and search in LLMs. 
2. The empirical results show a significant improvement over the existing baselines.

### Weaknesses
My main concern with this paper is that the methodology is not presented clearly.
1. Until Section 3.3, it is not clear what the ITE is, in the context of LLM reasoning. For example, the actions/interventions and the outcomes are only defined in Section 3.3. These should be introduced (at least at an informally) earlier in the paper so that the readers understand what the causal effect refers to in this setting. 
2. In Eq (2) the cross-entropy loss is for predicting the binary outcome $Y$, and not the next token (as is the case for LLMs). Firstly, this should be clarified earlier when the authors refer to 'cross-entropy loss' in line 249. Secondly, it is unclear how the LLM is fine-tuned with this new cross-entropy loss? The output space of LLM is the token space and not $\{0,1\}$. 
3. It is unclear how the causal probability trees are constructed exactly. The authors should provide explicit examples for clarity. 
4. > From $T_{head}$, infer 4 steps toward $T_{tail}$ based on reducing distance $D$.

How is this achieved concretely? Again, I think explicit examples are quite important for clarity

5. > Calculate the Euclidean distances between the resulting end nodes of both trees to form a distance matrix $M$

How is the Euclidean distance measured between two nodes? What are the $(x, y)$ coordinates for a node in a general reasoning problem?

6. Why is the DES method not tested for 2 - 6 step problems in Tables 2,3,5?

### Questions
See weaknesses section above.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces two methodologies aimed at improving the performance of LLMs on multi-step reasoning tasks. The first method, CRE, adds a loss term inspired by the causal Individual Treatment Effect (ITE) to measure causal influence on state transitions. The second method, DES, proposes a search strategy to solve reasoning problems more efficiently. Finally, the paper combines both methods and compares the combined approach against several baselines across three different common benchmark tasks.

### Strengths
- The attempt to introduce causal estimates into the training process of LLMs is a creative approach to improving multi-step reasoning performance. 

- The combination of two distinct methodologies—CRE for causal reasoning and DES for efficient search—provides an interesting way to tackle the challenge of multi-step reasoning with LLMs as it would address both causal inference and context window issues.

### Weaknesses
 - The clarity of the paper is a significant issue. Spelling mistakes, awkward sentences, unsubstantiated claims, and missing references make the paper difficult to follow. A thorough revision is needed to improve readability and coherence. 

 - Key concepts, such as causal probability trees, are mentioned multiple times without proper definition, leaving readers uncertain about what the authors mean. 

 - The paper makes ambitious claims about the ability to "enhance causality" and "guarantee causal rightness," but it does not provide sufficient evidence or guarantees to support these claims. Given the stochastic nature of LLMs, it's unclear how these guarantees can be made. 

 - The connection between CRE and the LLM's actual performance is not sufficiently explained. The experimental results, such as the 89% accuracy in multiplication tasks, do not convincingly demonstrate improved multi-step reasoning capabilities. 

 - The methodology, particularly the DES strategy and the causal probability trees, is under-explained, leaving gaps in understanding how the proposed solutions work. 

 - There are numerous unsubstantiated or unclear claims regarding causality and reasoning, making it hard to evaluate the validity of the methods proposed. 

 See questions for details

### Questions
Content-related: 

- L41-44: "Causal hallucinations... are somewhat entrenched in statistical inevitability." What is meant by "statistical inevitability"? Do you have a reference for this? 

- L53: "Embedding the causality measure between OSR and state transition..."—what causality measure are you referring to? Is it "some" or "a" causality measure? 

- The introduction of DES in L60-67 is too detailed without introducing necessary terminology: "state transitions," "unidirectional reasoning," "causal probability trees." 

- L71: In the abstract, you state that CRE can "guarantee the solid causal rightness," but here you mention it can "enhance the causality." Are these two different contributions? 

- L76: "Causal probability trees" are mentioned without explanation—please clarify what these are. 

- L78: "Constructing a new metric guaranteeing both..."—can you actually guarantee anything given the stochastic nature of LLMs? 

- L99: What do you mean by "detailed reasoning"? 

- L140: You mention "long time-series tasks"—is this referring to prediction, completion, or reasoning? How does inference fit in this context? 

- L160: Is 89% accuracy in multiplication evidence of the ability to "process multiple reasoning steps effectively"? 

- L165: How can you infer from a 1996 paper that LLMs struggle with long-range reasoning? What exactly is long-range reasoning in this context? 

- L190: What do you mean by "categorically similar"? 

- You mention "ITE typically indicates..." but isn’t ATE more commonly used in this context? Do you have a reference for this? 

- L222: What is meant by "enhancing the significance of causality" and "stability of causality"? It is unclear how expected values and variance of ITE can be interpreted this way. 

- L273: Are X and Y binomial random variables (0 = incorrect, 1 = correct)? How is the next state defined? This is under-specified. 

- L297: Causal probability trees are mentioned again without a proper definition, and the reference to Shafer (1996) remains under-specified. 

- L465-470: This section does not appear to summarize the previous results effectively as it appears to introduce new information.

- L485: The word "ensures" is problematic here, as no guarantees are demonstrated in the paper. 

- L526: You mention that the method "struggles with very long reasoning steps"—wasn’t the goal to address this limitation? This statement contradicts the claimed causal improvements. 

Minor points: 

- Is the missing space before a citation (e.g., "citep") a deliberate choice? It feels distracting in the text. 

- L213: "CONSISTANCY" typo—did you mean "consistency"? 

- L231: Another "consistancy" typo. Do you have a reference for interpreting the mean of a normal distribution in terms of causal significance? 

- L269: Do you have a definition or reference for "PPL"? 

- L284: Typo "lowing"—did you mean "lowering"? 

- L524: What is meant by "strict order of precedence"? Is this referring to a causal ordering?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents CreDes, a novel framework combining Causal Relationship Enhancement (CRE) and Dual-End Searching (DES) to improve large language models' capabilities in long-range reasoning tasks. The work addresses two key challenges: causal hallucinations in reasoning steps and the complexity of large search spaces in long-range reasoning problems. The main contributions include:
1. A CRE mechanism that enhances causality between reasoning steps using Individual Treatment Effect (ITE).
2. A DES approach that breaks down long reasoning chains into manageable segments.
3. Implementation of simultaneous multi-step reasoning to improve efficiency.
4. Experimental validation on multiple datasets (Blocksworld, GSM8K, Hanoi Tower).

### Strengths
1. Novelty that enhances LLM reasoning through causal modeling and search algorithms.
2. Comprehensive empirical validation across multiple datasets and models.
3. Significant performance improvements over existing methods on up to 12-step Blocksworld problems.
4. Thorough ablation studies and analysis.

### Weaknesses
1. Insufficient analysis of failure cases and limitations
2. Lack of detailed comparison with some recent relevant work, e.g. multi-agent verification, Tree-of-Thought, etc.  
3. Some experimental results lack error bars or statistical significance tests. 
4. The relationship between CRE and DES could be explained more clearly.
5. The explanation of causal intervention remains unclear. The authors' response that "We intervene to change the inputs to the model and observe the changes in the outputs" is too general. How is causal intervention implemented in LLMs? How is the effectiveness of intervention guaranteed? These key technical details are not elaborated.
6. The theoretical foundation of the CreDes framework needs strengthening:
- The integration of CRE and DES appears more empirical than theoretical
- The calculation and application of ITE requires more rigorous mathematical derivation
- Lacks theoretical guarantees for causal consistency in multi-step reasoning
7. Experimental validation is insufficient:
- 5% error range is relatively large for reasoning tasks, especially in long-sequence reasoning
- Lacks detailed analysis of failure cases
- Missing comparisons with other recent methods (e.g., multi-agent verification)
- The construction method of the Hanoi Tower dataset may be biased
8. Regarding method generalizability:
While the authors mention potential migration to knowledge-related tasks, they don't provide specific migration plans or feasibility analysis, which reduces the method's persuasiveness.

### Questions
1. How cause-effect interventions is conducted in LLMs? Authors should provide an elaboration. 
2. Could the DES be extended to other types of reasoning tasks beyond the tested tasks? Some examples, on highly knowledge-demanding tasks, will be better. 
3. How does the framework handle cases where multiple valid reasoning paths exist?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed CreDes, a pipeline for optimizing multi-step state transitions (a trajectory) from given initial and goal states. CreDes has two components: the CRE part improves transition accuracy, i.e., there are fewer hallucinations, and the DES part speeds up searching speed. A numerical experiment on long-range reasoning tasks shows CreDes outperforms CoT and RoT in five datasets.

### Strengths
1. **Less hallucination**: For long-range inference tasks (such as Blocksworld), CreDes with a 7B model significantly outperforms baseline methods with the same model size and is even stronger than a RAP method with 70B models. 

2. **More efficient**: The CRE is trained to generate multiple steps from one output and the DES method searches from both ends. The numerical study (Fig 5) also shows CreDes has a relatively consistent average time for different task ranges, while baseline methods can be slower for long-range tasks.

3. **Improved Stability**: Based on empirical study, the CRE loss function incorporates the variance term, augmented from a single expectation term, of the Individual Treatment Effect (ITE).

### Weaknesses
1. **Can be more general**: the method section ties in with the experiment section. For example, the CRE loss function is based on numerical supports, which leaves a gap (need to test both for new cases thus more training cost) for more general applications.

2. **Causality Comments**: Here the causal definition seems more like "Improve the possibility of what should happen of an action by minimizing the CRE loss thus we can reduce hallucination", from which I do not see the role of "treatment for control" part, i.e. W = 0. Also, the claims between lines 275 - 278 are incorrect. Given the condition "X and Y are correlated", we cannot simultaneously have "Y can be predicted using X" and "intervening in X would not lead to any changes in the distribution of Y".

### Questions
1. For baseline methods (or frameworks), are we using the same template/prompt for different datasets? How can we determine a representative performance for each one of them?

2. During reading I need to assume exact definitions of "state", "treatment", and "treatment effect". I am still a bit uncertain about the treatment effect. E.g. what is the treatment effect of "Pickup Orange" for the initial state of "The orange block is on the table ...[left panel from figure 2]"

3. How to determine/calculate the dynamic coefficients, alpha and beta, in the CRE loss function during training?

### Soundness
3

### Presentation
3

### Contribution
3
