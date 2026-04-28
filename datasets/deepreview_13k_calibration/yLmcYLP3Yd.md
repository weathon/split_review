# Discrete Neural Algorithmic Reasoning

- Decision: Reject
- Avg Score: 5.40
- Scores: 8, 5, 3, 5, 6

## Abstract
Neural algorithmic reasoning aims to capture computations with neural networks via learning the models to imitate the execution of classic algorithms. While common architectures are expressive enough to contain the correct model in the weights space, current neural reasoners are struggling to generalize well on out-of-distribution data. On the other hand, classic computations are not affected by distributional shifts as they can be described as transitions between discrete computational states. In this work, we propose to force neural reasoners to maintain the execution trajectory as a combination of finite predefined states. To achieve that, we separate discrete and continuous data flows and describe the interaction between them. Trained with supervision on the algorithm's state transitions, such models are able to perfectly align with the original algorithm. To show this, we evaluate our approach on multiple algorithmic problems and get perfect test scores both in single-task and multitask setups. Moreover, the proposed architectural choice allows us to prove the correctness of the learned algorithms for any test~data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel approach to neural algorithmic reasoning by enforcing neural networks to operate with discrete states and separating discrete and continuous data flows. The authors propose a model that integrates hard attention mechanisms, feature discretization, and a separation between discrete computations and continuous inputs (scalars). This design aims to align neural network computations closely with classical algorithms and thus improves out-of-distribution generalization and interpretability. The method is evaluated on several algorithmic tasks from the SALSA-CLRS benchmark, including BFS, DFS, Prim's algorithm, Dijkstra's algorithm, Maximum Independent Set (MIS), and Eccentricity calculations. The proposed Discrete Neural Algorithmic Reasoner (DNAR) achieves perfect test scores on these tasks, even on graphs significantly larger than those seen during training. The authors also discuss the limitations of their approach and potential directions for future work.

### Strengths
- Originality: The paper presents a novel method that enforces discrete state transitions in neural networks, which is a significant departure from traditional continuous representations. By integrating hard attention and separating discrete and continuous data flows, the authors address key challenges in neural algorithmic reasoning, particularly out-of-distribution generalization, and interpretability.
- Quality: The experimental results are strong, with DNAR achieving perfect test scores across multiple algorithmic tasks and graph sizes. The comparison with baseline models and state-of-the-art methods demonstrates the effectiveness of the proposed approach.
- Clarity: The paper is generally well-written and structured. The authors explain their methodology, including architectural choices and training procedures. The inclusion of diagrams and tables aids in understanding the proposed model and its performance.
- Significance: The work contributes to the field by showing that neural networks can be designed to mimic classical algorithms with perfect generalization and interpretability. This has implications for developing reliable and trustworthy AI systems that can be formally verified.

### Weaknesses
 - Expressiveness Limitations: The enforced constraints, such as hard attention and discrete state transitions, limit the model's expressiveness. For instance, in a single message-passing step, the model cannot compute certain aggregate functions, like averaging over neighbors or calculating more complex statistics such as variance or standard deviation. This restricts the method's applicability to algorithms that fit within these constraints. The inability to perform weighted sums or other non-linear combinations of neighbor features further limits the model's ability to capture complex relationships within the graph structure.
- Scope of Evaluation: The experimental evaluation focuses on specific algorithmic tasks where the proposed method aligns well. It remains unclear how the model would perform on more complex algorithms that require different computational primitives or continuous manipulations beyond simple increments, decrements, and selections. For example, algorithms involving matrix operations, spectral analysis, or iterative optimization procedures are not addressed, leaving a gap in understanding the method's general applicability.
- Training Without Hints: While the method achieves excellent results with hint supervision, training without hints is identified as challenging. This limitation reduces the method's applicability in scenarios where intermediate algorithmic steps (hints) are unavailable. The reliance on detailed step-by-step guidance during training may not be feasible for many real-world problems, limiting the practical use of the method.
- Sensitivity to Hyperparameters: The paper mentions that certain hyperparameters, like the number of discrete states, significantly impact performance, especially when training without hints. However, there is limited discussion on how sensitive the model is to these hyperparameters and the implications for generalization. The lack of a systematic analysis of hyperparameter sensitivity makes it difficult to assess the robustness of the method and its practical applicability.
- Presentation Details: While the paper is generally clear, some sections could benefit from additional explanations. For example, the scalar updater's mechanism could be elaborated further to better understand if someone is not in the NAR field. The precise nature of the discrete operations performed on the scalars and the rationale behind their selection could be made clearer.

### Questions
1. How does the proposed method handle algorithms that require more complex continuous manipulations or aggregate functions beyond simple increments and selections? Can the model be extended to support such algorithms without losing the benefits of discretization and interpretability?
2. Are there potential strategies to improve training without hint supervision? How does the model perform on tasks without hints when compared to continuous models?
3. The constraints improve generalization but reduce expressiveness. Is there a way to balance this trade-off by selectively relaxing some constraints?
4. Can the proposed separation between discrete and continuous data flows be applied to other neural network architectures beyond attention-based models? What challenges might arise in such adaptations?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors make some modifications to Transformer training to make it more effective for algorithmic reasoning tasks. In particular, they constrain it to learn hard attention, and separate discrete and continuous "flows" to prevent information loss. Overall these modicfications result in a model than the GIN and PGN baselines they consider.

### Strengths
The approach seems to work much better than the baselines considered, and achieves perfect performance on the two datasets studied in this article.

### Weaknesses
I found this paper to be difficult to read, but I'm not an expert in the area. It would be useful to see each of the design decisions in this paper ablated, with their corresponding effect on the datasets covered in this research. Specifically, the impact of hard attention versus soft attention mechanisms needs to be more thoroughly investigated. It's unclear if the reported perfect performance is due to the hard attention constraint, the separation of discrete and continuous flows, or a combination of both. Furthermore, the discretization of the scalar updater, while potentially beneficial, requires a more detailed analysis to understand its contribution to the overall performance. The paper lacks a clear understanding of how each component contributes to the final result, making it hard to assess the true value of the proposed approach. I am also concerned about the claim that the model will mirror the desired algorithm for any graph size, as this is not sufficiently supported by the experiments presented in the paper. The no-hint setting also deserves more attention, as it's not clear where the source of the gains are in this setting.

### Questions
1. I'm very much not an expert in this area, so I did a bit of a literature search on related papers in the field. I found one such paper [1], used a text-based version of the CLRS-3o, called TextCLRS-text. Does it make sense to use that dataset here? Or to compare to the proposed TransNAR architecture?

2. As mentioned earlier, it would be useful to ablate the different algorithmic decisions made in this paper. In its current form, I can't ascertain which of the architectural decisions is responsible for which gains on these datasets.

### Soundness
2

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
3

### Summary
The paper proposes a use of a finite set of predefined discrete states and manipulation of continuous inputs to improve limitations of current paradigms in neural algorithmic reasoning such as redundant dependencies in algorithmic data. The method achieves perfect performance on chosen tasks in SALSA-CLRS and CLRS-30 benchmarks and introduces a starting perspective on use of discrete states to pave the way for future methods in discrete neural algorithmic reasoning and their interpretability.

### Strengths
- Impressive performance achieved across selected tasks in SALSA-CLRS and CLRS-30 benchmarks
- Interpretability and simplicity of the proposed model which utilizes set of discrete states to capture continuous inputs using edge priorities
- Further perspectives on paving way for discrete neural algorithmic reasoners

### Weaknesses
 - There is limited explanation of how the discrete states are computed, the paper extensively discusses related work in sections 1 and 2, perhaps it would be better if this space was used for providing further detail on proposed architecture
- Work is limited in providing mathematical / theoretical definitions or explanation of discrete state space and manipulation with continuous inputs which is the main novelty
- Results show perfect performance on SALSA-CLRS and CLRS-30 benchmarks. The paper does not adequately address the lack of variance in results across different seeds, which is atypical for neural network training. The claim that this is due to the discretization is not sufficiently supported with a theoretical analysis or empirical evidence beyond the specific tasks used.
- The paper mentions modifying hints from the benchmark, but does not provide sufficient detail on the nature of these modifications, or why they were necessary. It is unclear if these modifications were applied to the baselines as well, which would be necessary for a fair comparison.
- The explanation of the virtual node is somewhat vague. The paper states it is used to select a unique node, but does not fully clarify how this selection occurs via the attention mechanism, or why this approach is superior to graph-level features or complete graphs for message passing.

### Questions
1. Results show perfect performance on SALSA-CLRS and CLRS-30 benchmarks. Could you elaborate on reported results and 0 variance between your seeds given that this is not the case in majority of comparable baselines or ablation experiments? Could you please report variance on results in table 1? 
2. Could you please explain the differences in computed discrete states used for SALSA-CLRS and CLRS-30 tasks as well as how the model performs on out-of-distribution data?
3. Could you provide a pseudocode behind Discretize_nodes and Discretize_edges functions shown on page 4?
4. Work mentions modifying hints from the benchmark, could you clarify if this was included for tested baselines as well as how the hints are modified?
5. Could you further elaborate on the addition of a virtual node in your model (section 4.3)?
6. Could you provide results of the hyperparameter search mentioned in section 6? 
7. Could you provide further detail on reverse-engineering (perhaps a toy example) mentioned in section 6?

### Soundness
2

### Presentation
2

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
This paper studies neural algorithmic reasoning and proposes a discrete transformer-based processor architecture. The authors show that the proposed model empirically achieves perfect size generalization on several algorithms picked from the CLRS benchmark.

### Strengths
- The problem of learning neural algorithmic reasoning is important. I like the overall idea of learning discrete neural reasoners since the previous efforts of learning neural networks with continuous states and or continuous operators failed miserably.

&nbsp;

- The architecture design has some interesting components. For example, the separation of the data and the computational flow that manipulates the data is interesting. In particular, the scalars (continuous input) only affect the computation of attention weights and do not affect the node or edge states. Although designs with the same spirit have appeared before, e.g., in Neural Execution Engines, this part has its own merits.

&nbsp;


- The paper is easy to follow and well-written, except that a few technical details are sparse.

### Weaknesses
 - I am concerned about the significance of the contributions. If the claims of this paper are all correct, then we just obtain a recipe for learning a neural reasoner to perfectly mimic a known algorithm. However, to make the learning successful, we need to first run the algorithm to collect the full trace of the execution, i.e., the sequence of intermediate states generated by the algorithm (the so-called hints). In other words, we just perfectly fit the “correct algorithm” using a neural network. 

  Moreover, I do not see a theoretical guarantee of when this perfect fitting would happen. For example, would it happen on a specific class of algorithms or any algorithm? See my next comment on the claim about “the guarantee”.

  This is unsatisfying since the goal of neural algorithmic reasoning is to learn correct algorithms from data without knowing the algorithms. From this perspective, the really interesting and valuable part is the exploration under the no-hints setting. However, in Section 6, the authors did not provide any experimental results and just stated that their model never achieved perfect validation scores. In short, the authors should provide a thorough empirical study of their proposed model under the no-hints setting and compare it with other approaches on benchmarks like CLRS. 

&nbsp;

- In Section 5, the claim “we can guarantee that for any graph size, the model will mirror the desired algorithm, which is correct for any test size” is quite strong. In my opinion, such a strong claim needs rigorous theoretical proof. However, the authors only provide some vague arguments to support this claim. 
  In particular, can you elaborate on the following two questions?
  1) How do you confirm that the attention block indeed operates as “select_best” selector?
  I neither see any empirical investigation nor theoretical proof on this point.
  2) Even if the attention block operates as “select_best” selector, why does this condition lead to the above claim?
  You should at least demonstrate your detailed logic using an example algorithm like DFS.

&nbsp;

- I think the size of the discretized states would matter a lot to the expressivity of the proposed neural reasoner, i.e., what algorithms can be represented by the designed class of neural networks. However, I did not see the experimental study and discussion on its effect.

&nbsp;

- An interesting experiment is to check if there is some sort of phase transition in terms of problem size. Specifically, I would imagine the phenomenon of perfect fitting to the correct algorithm would disappear if we decreased the problem size in training. Then, what is the minimum problem size to ensure it fits perfectly for a particular algorithm?

&nbsp;

- The details of how to train task-dependent encoders and decoders are not provided, and how they affect the processor's training is not discussed at all. I would imagine the quality of the encoded embedding is quite important to the success of learning the processor, even with teacher forcing. 

&nbsp;

- In section 3.3, I get the high-level idea that the scalars (continuous input) only affect the computation of attention weights and do not affect the node or edge states. However, the description of the idea in the 2nd paragraph of Section 3.3 is not so clear that I could not figure out how exactly the computation is designed. It would be great to either write the equations and or illustrate the computational graph.

### Questions
Please see my comments in the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenges of generalization and interpretability in neural algorithmic reasoning (NAR) by introducing a novel architecture that guides the model to follow algorithmic execution as a series of finite, predefined states. The proposed architecture has three main components: feature discretization, hard attention, and separation of discrete and continuous data flows. The empirical results show that the model achieves perfect scores in both single-task and multi-task experiments across various algorithms. Additionally, the architecture enhances interpretability, allowing validation of the correct execution of desired algorithms.

### Strengths
1. The writing is generally clear, though some areas could be further elaborated.
2. The paper is well-motivated, as both OOD generalization and interpretability in NAR are both important questions. The proposed architecture of separating the discrete and continuous data flows are novel and effective.
3. The perfect scores across algorithms are impressive, especially given the model’s capacity for size generalization on graphs 100 times larger, outperforming strong baselines.
4. The proposed architecture consists of three design components, each of which is validated through ablation studies to demonstrate its effectiveness.

### Weaknesses
1. While the perfect scores achieved in the experiments are impressive, the paper could be strengthened by testing on a wider range of algorithms. Although both parallel (e.g., BFS) and sequential (e.g., Prim) algorithms are covered, most algorithms studied are graph-based, where previous NAR methods have already proven effective. The CLRS-30 dataset includes a broader variety of algorithms (e.g., sorting and search), where many NAR methods can struggle. Although SALSA-CLRS was chosen for its thorough OOD evaluation, testing the model on the CLRS-30 dataset with larger graph sizes would add valuable insights due to the dataset’s extensive algorithm coverage.

2. Another limitation is the lack of application to real-world datasets, as the authors note in the Future Work section. A significant advantage of NAR methods is their ability to operate on high-dimensional data by utilizing a pretrained model that mimic algorithms. This presents an additional OOD challenge with potential distribution shifts in real-world data. Evaluating the proposed architecture on real-world datasets would demonstrate its practical value; even a single real-world experiment, as seen in related works (e.g., Numeroso et al., 2023), could significantly strengthen the method's implications.

3. Although interpretability is a valuable strength of the proposed method, it is unclear how this model’s interpretability, achieved through analyzing state transitions and attention blocks, differs from other NAR approaches, which also allow interpretation of intermediate executions (e.g., using decoder outputs to indicate a node’s current predecessor in a sorting algorithm).

### Questions
1. For the multi-task experiments, do the results in Table 2 correspond to these settings? It is unclear which algorithms were trained simultaneously and how this compares to the baselines’ configurations.

2. Without hints, DNAR struggles to generalize. Could you clarify the reverse-engineering issue described? Was any intermediate approach, such as noisy teacher forcing or teacher forcing decay, tested to examine the impact of hints on DNAR?

3. How were GIN and PGN used as baselines? Were they employed to treat this as an end-to-end node-level prediction task?

### Soundness
2

### Presentation
2

### Contribution
3
