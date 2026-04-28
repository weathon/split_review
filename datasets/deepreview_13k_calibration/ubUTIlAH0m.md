# Multi-Physics Operator Network for In-context learning (m-PhOeNIX)

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
We propose a multi-physics operator network for simultaneous and sequential learning of solution operators of multiple heterogeneous parametric partial differential equations. Existing neural operators are adept at learning the solution operator of only a single physical system, and adapting to new physical equations requires training a new surrogate model from scratch with physics-specific intensive hyperparameter tuning. The proposed multi-physics neural operator leverages the recent advancements in wavelet-based kernel integral-induced neural operator modeling and instantiates a memory-based ensembling strategy for projecting heterogeneous physical systems into a common shared feature space. The local channel-level ensembling is supported by context gates, which not only utilize the shared features to embed the features of multiple heterogeneous physical systems into the network parameters but also allow the multi-physics operator to learn new solution operators by transferring knowledge sequentially; this allows the proposed model to continually learn without forgetting. We illustrate the efficacy of our algorithm by simultaneously and sequentially learning six complex time-dependent solution operators of six physical systems. The inference results on the simultaneous and sequentially trained models depict the ability to infer previously seen physical systems without fine-tuning and catastrophic forgetting, indicating the characteristics of a foundation model. The framework also demonstrates the super-resolution property and generalization to out-of-distribution input conditions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents m-PhOeNIX (Multi-Physics Operator Network for In-Context Learning), a model that combines local wavelet experts and context gates to enable multi-task and sequential learning for various physics-driven PDEs. The proposed framework aims to allow the model to learn new PDE systems without requiring extensive re-training, preventing catastrophic forgetting. However, significant limitations in theoretical rigor, computational efficiency, and a lack of sufficient validation experiments reduce the overall impact of the work.

### Strengths
The idea is interesting to use local wavelet experts and context gates to create a flexible framework for capturing multi-scale features across multiple physics systems.

### Weaknesses
1. The theoretical foundation of m-PhOeNIX is insufficiently developed. The authors need to provide a clearer theoretical rationale and motivation for combining the existing architectures. The paper also lacks a formal analysis of why Daubechies wavelets were chosen over other types of wavelets. Specifically, the paper does not explore the implications of using different wavelet families, such as Symlets or Coiflets, on the model's performance and computational cost. A more rigorous justification for the choice of Daubechies wavelets, including a discussion of their vanishing moments and their suitability for the target PDEs, is needed.

2. Wavelet-based operations are typically more computationally expensive than FFT, especially for high-resolution data or real-time applications. However, the paper does not provide any benchmarks on runtime or memory usage. This information is essential to evaluate the model’s practical viability in large-scale scientific applications. The lack of detailed profiling, including a breakdown of the computational cost associated with the wavelet transforms and the context gating mechanism, makes it difficult to assess the model's efficiency. It is also unclear how the computational cost scales with the number of wavelet experts and the input resolution.

3. The use of multiple wavelet experts and context gates adds significant model complexity, which scales up with the number of experts and task diversity. This may introduce memory overheads, making m-PhOeNIX less scalable for high-dimensional PDEs. The paper does not provide a thorough analysis of how the model's memory footprint changes with an increasing number of experts and the dimensionality of the input data. Furthermore, the paper lacks a discussion on how the model's architecture might be optimized to reduce memory consumption, such as through techniques like pruning or quantization.

4. Boundary conditions significantly impact the solutions to PDEs, yet m-PhOeNIX does not explore how it would handle varying boundary conditions across tasks. A strategy for managing changing boundary conditions could be promising. The paper should address how the model can be adapted to handle different types of boundary conditions, such as Dirichlet, Neumann, or Robin conditions, and how the model's performance is affected by changes in boundary conditions. The lack of experimentation with varying boundary conditions limits the practical applicability of the model.

5. The model is designed to handle cases where the underlying PDEs are unknown or complex, making it potentially valuable for real-world applications. However, the model has been tested only on synthetic data, limiting its demonstrated applicability. It is essential to test the model on real-world datasets and more complex, higher-dimensional systems. Such validation would provide stronger evidence for the model's claimed adaptability and robustness in handling diverse and realistic physical phenomena. The paper should include experiments on real-world datasets, such as those from fluid dynamics or materials science, to demonstrate the model's ability to generalize beyond synthetic data.

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a method for predicting spatio-temporal systems derived from various physical systems, based on neural operator while avoiding catastrophic forgetting. The model relies on wavelet neural operators experts and fine-tunes the mixing between these experts for each "physics" through context gates. The model is applied on various 1D and 2D PDEs including advection-diffusion, Nagumo-Burgers, Allen-Cahn, heat and wave equations.

### Strengths
- The paper tackles a fundamental problem with neural operators, which is catastrophic forgetting
- The paper provides a clear, concise and original integration of several non-trivial concepts—sequential learning, wavelet neural operators, and local ensembling.

### Weaknesses
The main claim of the paper is that it presents an architecture designed to avoid catastrophic forgetting. This claim could be strengthened with more specific comparisons (see questions below).

- Fig.4, and Fig.5 indeed show that there is no degradation of performances when training on new datasets. However, I'm having a hard time assessing the risk of a catastrophic forgetting in that case. For example, if you have a large enough neural operator, that you train incrementally on the datasets you used in these figures, will you see this catastrophic forgetting?  It is unclear if the observed stability is due to the specific architecture or simply because the model has sufficient capacity to memorize all tasks without significant interference. A more direct comparison, perhaps by incrementally training a standard neural operator with similar capacity, would be beneficial to isolate the effect of the proposed method.
- on 1D data (Fig.4), when training on Allen-Cahn PDE dataset, it seems that the performances are slightly degraded on the Heat PDE: the performances are slightly worst on row 5 from column 2 to column 3, do you think it is significant? Isn't the model starting to forget about the Allen-Cahn PDE dataset? This observation raises concerns about the robustness of the method. While the performance drop is small, it suggests that the model may not be entirely immune to forgetting, and further investigation is needed to understand the conditions under which this occurs.
- l516: "requires a small initial trajectory to learn the time-dependent solution operators". Maybe I didn't understand what you meant, but how can we expect determining the solution operator without at least 2 time-frames? A single time frame doesn't give you the time operator. The statement is confusing, as a single time frame provides only a snapshot of the system's state, not its temporal evolution. The requirement of a trajectory, even a small one, implies the need for multiple time frames to infer the time-dependent operator. The description should clarify the minimum number of time frames required and how they are used to initialize the model.

Minor comments / questions.
- abstract, l028: "indicating the characteristic of a foundation model": it only indicates ONE characteristic that a foundation model should have. In particular, it seems to me that a foundation model should showcase that training on all these datasets is actually beneficial for each dataset, which your results don't necessarily show.
- l327,328: I'm having a hard time convincing myself that this is a correct metric to measure the "distance" between two datasets, and in particular that this is a good notion of distance between operators as it is argued l330. For example, if I have the same advection-diffusion operators, but initial conditions that are completely different, e.g. non-overlapping, it seems that you can get distances that are quite small
- l490-493. I am not certain that the number of parameters is the relevant measure here. In particular, in a transformer model, such as a Transformer like MPP, that you compare with, reducing the spatial downsampling should increase drastically the performances of the model, while not changing the number of parameters at all.

### Questions
- Fig.4, and Fig.5 indeed show that there is no degradation of performances when training on new datasets. However, I'm having a hard time assessing the risk of a catastrophic forgetting in that case. For example, if you have a large enough neural operator, that you train incrementally on the datasets you used in these figures, will you see this catastrophic forgetting? 
- on 1D data (Fig.4), when training on Allen-Cahn PDE dataset, it seems that the performances are slightly degraded on the Heat PDE: the performances are slightly worst on row 5 from column 2 to column 3, do you think it is significant? Isn't the model starting to forget about the Allen-Cahn PDE dataset? 
- l516: "requires a small initial trajectory to learn the time-dependent solution operators". Maybe I didn't understand what you meant, but how can we expect determining the solution operator without at least 2 time-frames? A single time frame doesn't give you the time operator. 

Minor comments / questions. 
- abstract, l028: "indicating the characteristic of a foundation model": it only indicates ONE characteristic that a foundation model should have. In particular, it seems to me that a foundation model should showcase that training on all these datasets is actually beneficial for each dataset, which your results don't necessarily show.
- l327,328: I'm having a hard time convincing myself that this is a correct metric to measure the "distance" between two datasets, and in particular that this is a good notion of distance between operators as it is argued l330. For example, if I have the same advection-diffusion operators, but initial conditions that are completely different, e.g. non-overlapping, it seems that you can get distances that are quite small 
- l490-493. I am not certain that the number of parameters is the relevant measure here. In particular, in a transformer model, such as a Transformer like MPP, that you compare with, reducing the spatial downsampling should increase drastically the performances of the model, while not changing the number of parameters at all.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a neural operator designed to solve multiple physics problems simultaneously, thus removing the need to train distinct models for individual partial differential equations (PDEs). Additionally, the method employs an ensemble strategy to facilitate knowledge transfer when learning from new data, reducing the risk of overwriting pre-trained information during fine-tuning downstream tasks.

### Strengths
- The author conducts comparative experiments across a broad range of PDEs with varying dimensions in both single-task and joint training settings, which enhances the transparency of the proposed method’s performance.

- Including a demonstration showing similarities among each PDE dataset in the experiments section is commendable, as it highlights the model’s ability to generalize across diverse problem sets.

### Weaknesses
 - In the “Comparison against existing multiphysics operators” section in Numerical Illustration, it is unclear whether the reported results for ICON and AVIT are from 1) their pre-trained models or 2) from versions fine-tuned for each downstream task. If based on the first, it would be more rigorous to include their fine-tuned results for a fair comparison. For instance, MPP outperforms FNO on certain PDEs in their paper [1].

- To improve the clarity of the paper, consider including model parameters as a column in Table 1, along with such measurements for models in the problem-specific cases. For better readability, note that the term “parameter” is used in multiple contexts, leading to potential confusion, which could be mitigated by rephrasing in some cases. For instance, when describing the number of data. Additionally, consider adding punctuation to lengthy sentences, such as the second-to-last sentence in the “Problem-specific comparison” section.

### Questions
- Is there an intuition for why most of the 2D data on the same PDE exhibits a lower relative L2 error compared to 1D cases?

- How many local wavelet experts were used, and does changing this number affect performance?

### Soundness
3

### Presentation
2

### Contribution
3
