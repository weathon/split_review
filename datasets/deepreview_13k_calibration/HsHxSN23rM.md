# STAR: Synthesis of Tailored Architectures

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
noindent 
Iterative improvement of model architectures is fundamental to deep learning: Transformers first enabled scaling, and recent advances in model hybridization have pushed the quality-efficiency frontier. However, optimizing architectures remains challenging and expensive. Current automated or manual approaches fall short, largely due to limited progress in the design of \textit{search spaces} and due to the simplicity of resulting patterns and heuristics. In this work, we propose a new approach for the \textit{synthesis of tailored architectures} ({\tt STAR}). Our approach combines a novel search space based on the theory of \textit{linear input-varying systems}, supporting a hierarchical numerical encoding into architecture \textit{genomes}. {\tt STAR} genomes are automatically refined and recombined with gradient-free, evolutionary algorithms to optimize for multiple model quality and efficiency metrics. Using {\tt STAR}, we optimize large populations of new architectures, leveraging diverse computational units and interconnection patterns, improving over highly-optimized Transformers and striped hybrid models on the frontier of quality, parameter size, and inference cache for autoregressive language modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents an iterative improvement of model architectures to achieve quality-efficiency frontier called STAR. It leverages the theory of  linear input-varying systems to obtain architecture genome encoding and optimize the model through evolutionary algorithms. The experiments reveal optimized models compared to highly optimized transformers and striped hybrid models.

### Strengths
--It shows promising results.
-The encoding for architecture genome seems to be novel.

### Weaknesses
 -The idea of using evolutionary algorithm for the architecture design space exploration  is not new.

-The mutation mainly happens on the backbone and  it is not clear if will affect the underlying components.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a new approach for automated deep learning architecture search based on evolutionary optimization. To realize effective optimization, the work introduces 'linear input-varying systems' (LIVs), a general formulation of input-dependent token vector transformations. With this formalism, a wide range of commonly used model operators such as attention, recurrence, and convolutions can be expressed as special LIV-cases, that compose into model architecture backbones via a set of compositional rules. Notably, the set of LIVs and their composition can be expressed in a hierarchical coding scheme that describes a specific network architecture as a sequence of integers. This 'genome' lends itself to evolutionary optimization via recombination and random mutation of the genome integer elements. Using the LIV genome representation with multi-objective evolutionary algorithms such as NSGA-2, the authors demonstrate that they can automatically discover network architectures that offer improvements over highly optimized Transformer architecture baselines.

### Strengths
The work proposes a straightforward method for constructing a well-conditioned and comprehensive model architecture search space that is amenable to evolutionary optimization under multiple objectives. The hierarchical construction of the LIV building blocks and the coding schemes ensures that a wide variety of candidate architectures can be expressed and searched efficiently. Notably, the genome representation has a clear interpretation which makes it easy to apply constraints to ensure robustness to random edits.

The paper is well-written and provides a clear presentation of the motivation and context of this work. The experimental evaluation is logically structured and presents the key findings in an accessible way. 

The extensive experimental results provide convincing evidence that the STAR method is effective in finding high-performing architectures under various optimization objectives.

### Weaknesses
By construction, the method appears to be geared towards finding tweaks of transformer-based architecture stacks and does not aim to discover fundamentally new architecture designs. For instance, genomes are constructed assuming a pre-norm residual structure that cannot be varied by the optimizer. This is a reasonable assumption but it arguably relies on the manual design expertise that automated architecture search is ultimately aiming to overcome. Can you think of ways to extend the genome to parametrize the residual connection and normalization schemes?

On a similar note, the mutation constraints described in Section 4.2 -- while well motivated and reasonable -- suggest that an unconstrained STAR genome is not sufficiently robust to random edits, meaning that expert intuition is still required to 'guide' the mutation process. Can you quantify the impact of unconstrained edits on the search outcomes, e.g. through an ablation study that compares constraint vs unconstrained mutations? Specifically, what is the distribution of valid vs invalid architectures generated by unconstrained mutations, and how does this impact the convergence of the evolutionary search?

Finally, minor points, I found the notation in Eq. L128 and L138 a little confusing.
- The underbrace in Eq. L128 suggests that the summation is part of $T_{ij}^{\alpha \beta}$, but in Eq. L138 the summation is repeated.
- Additionally, as noted in L155 $T_{ij}$ is used to denote a whole range of possible operators, so it seems that $T_{ij}^{\alpha \beta}$ in L128 is overloaded. It may be clearer to use the underbrace in Eq. L128 to annotate 'attention $T_{ij}$' and 'attention $T^{\alpha \beta}$' explicitly as the special case and then use $T_{ij}^{\alpha \beta}$ to define the generalized version in Eq. L138.

### Questions
I might have missed it, but in Table 5.1, what is the difference between STAR-1 to STAR-8? Presumably, the optimization finds a Pareto-front of solutions, but I couldn't find any details on how you picked the evaluated solutions. Could you please provide details on the selection criteria for these eight models and explain how they differ architecturally? This would give readers a clearer picture of the diversity of solutions found by the method.

The experiments used a fixed number of LIVs to form a backbone. How did you choose this default backbone length of 24 LIVs? Could you discuss the potential challenges and benefits of allowing a variable-length search space with an arbitrary number of LIV modules, and whether this would be something to consider for future work?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper tackles a crucial research problem in the ML community—Optimizing the design of neural network architectures beyond predefined and typical search spaces. The authors posit important research questions on the limitations of existing automated neural network design approaches—mainly relying on predefined backbones and limited search parameters. Also, existing works on NAS methods overlook the inherent hierarchy of the NN design at the level of operators and architecture topology. The authors propose STAR, a novel framework to address the issues above, and build a synthetic, multi-pattern, hierarchical search space-optimized with evolutionary algorithms. A comprehensive evaluation has demonstrated the effectiveness of STAR, showing significant improvements in perplexity, downstream benchmarks, model size, and inference caching compared to optimized hybrid Transformer baselines.

### Strengths
- The paper presents an important research problem for the ML design automation community: The limitations of existing search spaces, especially for hybrid and transformer models in language processing applications, which typically require significant computational resources to evaluate different design choices.
- The hierarchical search space design is grounded in the theory of linear input-varying systems, providing a solid theoretical foundation. Characterizing neural network architectures through featurization, structure, and backbone offers a clear and logical approach, supporting the creation of a more generalizable search space that extends beyond predefined backbones.
- The authors' choice of an evolutionary algorithm to explore the hierarchical design space is well-justified, given the complexity of the architectures being searched. This approach facilitates the evolution of large populations of architectures using mutation and recombination operators.
- The evaluation section is thorough and detailed, with promising results that demonstrate the effectiveness of the STAR framework. Overall, the paper is well-written and flows smoothly.

### Weaknesses
 - While Section 2 provides a thorough overview of the hierarchical search space, certain design choices would benefit from additional explanation, particularly in relation to existing implementations and empirical justification for their inclusion. For example, the distinction between channel and token mixing could be clarified, along with an explanation of the LIVs to which each can be applied. Since STAR operates within a hybrid design space that may incorporate either convolution or attention mechanisms, it would be helpful to discuss how each design choice applies to different LIV operators and whether any constraints are involved. Specifically, the paper should clarify how the channel and token mixing are implemented for each LIV, detailing the specific operations and parameters involved, and provide empirical evidence supporting the chosen configurations.
- Section 3 explains the STAR genome and the role of each gene. However, it lacks a detailed description of the encoding strategy used in the evolutionary process, particularly regarding parameter ranges and the significance of each genome gene. For example, it would be helpful to clarify which integers correspond to each LIV class and the specific meaning behind each integer value. Additionally, further explanation is needed on how the evolutionary algorithm processes the genome encoding. To enhance clarity, the authors are encouraged to include a table (in addition to Figure 3.1) listing all search parameters (genes), their definitions, possible values, and how they translate into the neural network architecture. The paper should specify the exact numerical ranges and the corresponding architectural implications for each gene, including the specific mapping between integer values and LIV classes, and the rationale behind these choices.
- In the abstract and introduction, the authors claim that STAR’s optimization framework is a gradient-free evolutionary algorithm. However, this statement is somewhat misleading, as certain parameters of the explored architectures are indeed trained during the STAR evolution process. To clarify, the authors should provide a detailed schematic of the optimization process, including a clear figure, and add specifics regarding the training and evaluation times within the STAR evolution. This would allow readers to better understand how much STAR improves upon native GA frameworks. For a gradient-free optimization, it would be interesting to see how zero-shot approaches (e.g., ZiCo [1]) can be integrated into the STAR framework to accelerate the fitness evaluation. The paper needs to clearly distinguish between the training of the network parameters and the evolution of the architecture, emphasizing that while the architecture search is gradient-free, the evaluation of each architecture involves training its parameters using gradient descent.
- Although Section 4.1 introduces the evolutionary operators, such as mutation and recombination, these are not explained in sufficient detail. Specifically, the authors do not clarify which types of mutation (e.g., uniform, polynomial) and recombination (e.g., uniform, fixed-point) operators are employed, nor do they discuss how the STAR framework manages invalid designs generated after evolution. Additionally, it would be helpful to understand the likelihood and extent to which STAR produces invalid designs during evolution. To address this important aspect, the authors should consider including a figure or algorithm that illustrates the evolution process, detailing how mutation and recombination are applied and explaining how invalid neural network designs are managed—whether through replacement, alteration, correction, or removal. The paper should specify the exact mutation and recombination operators used, including their parameters, and provide a detailed analysis of the frequency and types of invalid designs generated during the evolution process, along with the mechanisms used to handle them.
- Given the hierarchical nature of the design space and STAR's apparent use of a single-genome representation, concerns arise regarding optimization convergence. Specifically, what are the pros and cons of a one-shot optimization approach versus a multi-stage optimization strategy, where multiple evolutionary algorithms are employed to optimize different levels of the search space? The authors are encouraged to discuss this comparison and to evaluate STAR's scalability on complex tasks, where achieving convergence toward optimal architectures may be challenging. The paper should include a discussion on the potential benefits and drawbacks of a multi-stage optimization approach, and provide an analysis of the convergence behavior of STAR, especially when applied to more complex tasks and larger search spaces.
- The evaluation of STAR is somewhat limited, as it is only applied to two architectures (i.e., Striped Mamba and Transformer++). Since this paper aims to push neural network design beyond typical search spaces, it would be beneficial to evaluate STAR models on state-of-the-art (SOTA) architectures that have demonstrated strong performance on benchmarks such as RedPajama, LAMBADA, HellaSwag, ARC-e, and PiQA. A comparison with SOTA models like LLama [2], BitNet [3], and Falcon-Mamba [4] would provide valuable insights. To ensure a fair comparison, all models could be trained under the same conditions, with both performance and efficiency metrics used to assess the effectiveness of STAR’s design approach. The paper should include a more comprehensive evaluation of STAR, including a comparison with state-of-the-art models on standard benchmarks, and provide a detailed analysis of both performance and efficiency metrics.
- Reproducing STAR without access to the original source code proved challenging. Despite my best efforts to replicate the work using the information provided in the appendix, I was unable to do so. To facilitate further investigation into the technical implementation details, it is recommended that the authors share the source code.

### Questions
- Could you provide additional explanation for certain design choices within the hierarchical search space in Section 2, specifically regarding how they relate to existing implementations and the empirical rationale for their inclusion?
- Since STAR operates within a hybrid design space that may involve either convolution or attention operations, could you discuss how each design choice applies to different LIV operators, including any constraints involved?
- Could you elaborate on the encoding strategy used in the evolutionary process, particularly in terms of parameter ranges and the significance of each genome gene?
- You mention in the abstract and introduction that STAR’s optimization framework is gradient-free, yet some parameters of the explored architectures are trained during the evolutionary process. Could you clarify this point?
- Could you provide more detailed information on the mutation (e.g., uniform, polynomial) and recombination (e.g., uniform, fixed-point) operators used within STAR?
- How does the STAR framework handle invalid designs generated through evolution, and could you provide information on the likelihood and extent of these occurrences?
- Given that STAR operates within a hierarchical design space with a one-genome representation, there are some concerns about optimization convergence. Could you discuss the pros and cons of using a one-shot optimization approach versus a multi-stage optimization strategy that involves separate evolutionary algorithms for different levels of the search space?
- Without access to the original source code, reproducing STAR is challenging. Would you be open to sharing the source code to allow for further investigation into the technical details of your implementation?
- The current evaluation seems limited to only two architectures (Striped Mamba and Transformer++). Since this paper aims to explore neural network design beyond typical search spaces, would you consider evaluating STAR models on state-of-the-art architectures that perform well on benchmarks such as RedPajama, LAMBADA, HellaSwag, ARC-e, and PiQA?
- A comparison between STAR models and other SOTA models, such as LLama, BitNet, and Falcon-Mamba, trained under consistent configurations, could offer valuable insights. Would you consider including performance and efficiency metrics to assess STAR’s effectiveness relative to these models?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the approach for the synthesis of tailored architectures (STAR). STAR genomes are automatically refined and recombined with gradient-free, evolutionary algorithms to optimize for multiple model quality and efficiency metrics. In the experimental results, the proposed method is compared with Transformer++ and StripedMamba.

### Strengths
1.	The proposed method combines a novel search space based on the theory of linear input-varying systems, supporting a hierarchical numerical encoding into architecture genomes.
2.	The proposed method STAR optimizes architectures for various combinations of metrics simultaneously: quality (perplexity during pretraining), quality and size, and quality and inference cache size (KV cache and fixed state cache). 
3.	The experimental results are well analyzed.

### Weaknesses
The proposed method is only compared with Transformer++ and StripedMamba. Comparison with additional LLMs (such as Llama series) would be preferred.

### Questions
1.	How about the performance compared with other LLMs, such as Llama series?
2.	How about the performance compared with KV cache optimization methods ?

### Soundness
2

### Presentation
3

### Contribution
2
