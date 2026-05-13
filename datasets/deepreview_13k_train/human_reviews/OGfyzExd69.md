# Procedural Synthesis of Synthesizable Molecules

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Designing synthetically accessible molecules and recommending analogs to unsynthesizable molecules are important problems for accelerating molecular discovery. We reconceptualize both problems using ideas from program synthesis. Drawing inspiration from syntax-guided synthesis approaches, we decouple the syntactic skeleton from the semantics of a synthetic tree to create a bilevel framework for reasoning about the combinatorial space of synthesis pathways. Given a molecule we aim to generate analogs for, we iteratively refine its skeletal characteristics via Markov Chain Monte Carlo simulations over the space of syntactic skeletons. Given a black-box oracle to optimize, we formulate a joint design space over syntactic templates and molecular descriptors and introduce evolutionary algorithms that optimize both syntactic and semantic dimensions synergistically. Our key insight is that once the syntactic skeleton is set, we can amortize over the search complexity of deriving the program's semantics by training policies to fully utilize the fixed horizon Markov Decision Process imposed by the syntactic template. We demonstrate performance advantages of our bilevel framework for synthesizable analog generation and synthesizable molecule design. Notably, our approach offers the user explicit control over the resources required to perform synthesis and biases the design space towards simpler solutions, making it particularly promising for autonomous synthesis platforms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
1. This paper addresses the challenge of designing synthesizable molecules and creating analogs for unsynthesizable ones by framing these tasks within a program synthesis framework. The paper introduces a bi-level approach to explore synthesis pathways by separating the structural skeleton of a synthetic pathway from its functional properties. 
2. Through Markov Chain Monte Carlo simulations, they refine molecular structures iteratively and optimize both syntactic and semantic dimensions with evolutionary algorithms.

### Strengths
1. The problem statement is well-defined, and the methods for synthesizing analogs and generating molecules are clearly explained, including the program's semantics.
2. The method achieves state-of-the-art performance in molecule generation on benchmark datasets and demonstrates significantly greater efficiency than the SynNet method when tested with various oracles, such as GSK, JNK, and DRD2.
3. Experimental analysis was conducted using various evaluation metrics, including bioactivity predictors (oracles), structural profiles, multi-property objectives, and docking simulations. The extensive number of experiments, detailed in Appendix G, provides strong evidence that this method outperforms other benchmarking methods.
4. The figures in the paper effectively clarify the methodology. The t-SNE and MDS plots in Appendix B, based on data from the final hidden layer representation of the MLP, clearly illustrate the most popular skeleton classes.
5. The model architecture used in the method is thoroughly explained, with detailed insights provided in the attention visualization section in Appendix E.

### Weaknesses
 1. This paper failed to mention the source code / anonymous repository and also in Appendix E . 6 ATTENTION VISUALIZATION figure number is missing.
2. Results are compared against the 2022 paper; The authors have not compared the results against any recent publications.
3. This paper doesn't address the computational cost or effectiveness of the algorithms. How long does it take to train the inner loop given ~136k synthetic trees, molecule generation or analog creation?

### Questions
1. How robust is bi-level framework to work with other architectures other than TransformerConv, something like Decision Transformer ?
2. Is there any recent papers like GFlowNet that could be referred other than synthesis-based SynNet published in 2022?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper reframes molecule design and synthesizable analog recommendation as conditional program synthesis problems. It introduces a bi-level framework that separates the syntactic skeleton of synthesis pathways from their chemical semantics, allowing efficient exploration of both syntactic and semantic design spaces using evolutionary algorithms and Markov Chain Monte Carlo simulations. By leveraging fixed-horizon Markov decision processes, the approach improves synthesizable molecule generation and offers control over synthesis complexity. Results demonstrate enhanced performance and resource efficiency, positioning this method as a promising tool for automated molecular discovery.

### Strengths
1. Frames molecular design and synthesizable analog recommendation as conditional program synthesis tasks, offering a fresh perspective in this field.
2. Demonstrates robust performance across key metrics, underscoring the effectiveness of the proposed methods.
3. Provides thorough experiments that validate the approach and its contributions to molecular design and synthesis.

### Weaknesses
1. The current approach uses a limited number of templates, and it is unclear how this framework could be expanded to include a broader range of templates, which could limit its flexibility. Specifically, the paper does not address the potential for combinatorial explosion in the search space as the number of templates increases, nor does it discuss the computational implications of managing a significantly larger template library. This raises concerns about the practical applicability of the method to real-world chemical synthesis scenarios, where a diverse set of reactions is often necessary.
2. Although the authors claim efficiency, the paper lacks direct comparisons to demonstrate this advantage against other methods. The claim of efficiency is not substantiated with concrete benchmarks against existing state-of-the-art methods for molecular design and synthesis. Without these comparisons, it is difficult to assess the true practical value of the proposed method in terms of computational cost and time savings.
3. The comparison between tasks in Section 3.1 could be enhanced with mathematical notation alongside chemistry examples. While the method draws on program synthesis concepts, the explanation may be confusing without using clear chemical illustrations. The current description relies heavily on program synthesis terminology, which may not be immediately accessible to chemists. A more detailed explanation, incorporating both mathematical formalisms and chemical examples, would greatly improve the clarity and accessibility of this section.

### Questions
The primary concern lies in the method's scalability under the current scheme. It remains unclear how the approach would handle a significantly larger design space with more templates, and how its performance would hold up as template diversity increases.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a method for synthesize of synthesizable molecules. It includes separates the syntactic skeleton (structure) of a molecule from the semantics (functional groups and properties), Markov Chain Monte Carlo (MCMC) Simulations for skeleton refinement, Genetic Algorithms for the optimization of both the structural and chemical aspects of molecules, and Surrogate Modeling with Graph Neural Networks to represent the molecular structure.

The experiments show that the proposed framework matches and outperforms the current state of the art approaches to synthesizable molecule and synthesizable analog design.

### Strengths
- The approach is interesting from the soft-computing point of view. The authors leverage the four different approaches on the right places. The separation between the structure and the content in the synthesis approach is interesting in particular. The use of MCMC and GA is more standard but is well suited for the new candidate tree generation and the search of the best structure and content of candidate molecule.

### Weaknesses
 - I think the possible weakness is the dependency on the tree and the grammar components. On one hand having a very large amount of templates will increase the computational complexity of the model (it is not clear how for instance the MCMC algorithm would handle this) and on the other hand a more efficient smaller set will not allow to generate all desired solutions

### Questions
How would the method handle a much larger set of the input alphabet and structural templates?

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
In this paper, the authors address the problems of synthesizable analog generation and synthesizable molecule design, employing syntax-guided synthesis techniques from the field of program synthesis. Specifically, they developed a bi-level framework that decouples the syntactical skeleton of a synthetic tree from the program semantics, and introduced amortized RL algorithms based on the framework. They demonstrated improvements across multiple dimensions of performance for both tasks, and include in-depth visualizations and ablation studies.

### Strengths
1. The problem of designing useful molecules with desirable properties and good synthesizability is very critical to drug discovery. 
2. The connection between the problem and the program synthesis community is vital. 
3. The method is carefully designed and well executed in experiments.

### Weaknesses
1. Since this work heavily involves discussion on search space, and amortized search within the synthesis tree, similar things are also explored deeply in the retrosythesis community. Thus, it would be beneficial to incorporate some discussions in the paper to discuss the connections and differences between this work and previous work.

    1. Self-Improved Retrosynthetic Planning, Kim et al., ICML 2021
    2. Retrosynthetic Planning with Dual Value Networks, Liu et al., ICML 2023
    3. Retrosynthesis Zero: Self-Improving Global Synthesis Planning Using Reinforcement Learning, Guo et al., JCTC 2024


2. The paper is clear and well-written. However, it would be helpful if the introduction includes a reference to the detailed description of the two tasks in the related work section. This will help readers understand the tasks before they delve into the techniques used.

3. Regarding the experimental setup, could you explain the choice of the 91 reaction templates and the 147,505 building block compounds? Are they forward reaction templates? Do these choices reflect real-world applications in molecular design?

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3
