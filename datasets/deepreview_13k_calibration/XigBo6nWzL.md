# DDRL: A DIFFUSION-DRIVEN REINFORCEMENT LEARNING APPROACH FOR ENHANCED TSP SOLUTIONS

- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 5, 3, 5, 3

## Abstract
The Traveling Salesman Problem (TSP) is a fundamental challenge in combinatorial optimization, known for its NP-hard complexity. Reinforcement Learning (RL) has proven to be effective in managing larger and more complex TSP instances, yet it encounters challenges such as training instability and necessity for a substantial amount of training resources. Diffusion models, known for iteratively refining noisy inputs to generate high-quality solutions, offer scalability and exploration capabilities for TSP but may struggle with optimality in complex cases and require large, resource-intensive training datasets. To address these limitations, we propose DDRL (Diffusion-Driven Reinforcement Learning), which integrates diffusion models with RL. DDRL employs a latent vector to generate an adjacency matrix, merging image and graph learning within a unified RL framework. By utilizing a pre-trained diffusion model as a prior, DDRL exhibits strong scalability and enhanced convergence stability. We also provide theoretical analysis that training DDRL aligns with the diffusion policy gradient in the process of solving the TSP, demonstrating its effectiveness. Additionally, we introduce novel constraint datasets—obstacle, path, and cluster constraints—to evaluate DDRL's generalization capabilities. We demonstrate that DDRL offers a robust solution that outperforms existing methods in both basic and constrained TSP problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors proposed a learning framework that combines diffusion and RL to better solve the TSP problem. Through experiments, they confirmed that it shows excellent performance on TSP problems of various sizes, and especially shows better performance than other algorithms on problems with constraints.

### Strengths
The authors proposed a deep learning algorithm that can solve TSP problems of various sizes. In particular, the proposed method showed good performance even in situations with various constraints.

### Weaknesses
Although a good method has been proposed, I think the following points should be additionally confirmed.

1) Doesn't DDRL have a problem that it can generate completely wrong solutions for test inputs that have different distributions from the training data distribution?
2) Doesn't the diffusion step also require high computation cost?
3) Why can you say that the proposed method can handle complex constraint conditions well? Is there a logical basis for it?
4) It is expected that RL-based policy learning may not work well for difficult problems with large size and high difficulty. When using RL, it is necessary to provide a logical basis for learning so that the correct and good solution can always be found.
For example, the proposed reward maximization cannot always guarantee that it will produce a good solution.

### Questions
Please explain about above weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Diffusion-Driven Reinforcement Learning (DDRL), a novel framework combining reinforcement learning (RL) with diffusion models to address the complex, NP-hard Traveling Salesman Problem (TSP). Traditional RL approaches, while effective, face stability and resource challenges, and diffusion models, though scalable, often lack optimality. DDRL uses a latent vector to generate an adjacency matrix, integrating image and graph learning within RL for enhanced scalability and stable convergence. Leveraging a pre-trained diffusion model, DDRL outperforms certain existing methods on both basic and newly introduced constrained TSP datasets (obstacle, path, and cluster constraints).

### Strengths
1. The paper proposes a novel method to combine the diffusion models and RL models, tending to enjoy the strengths of both.

2. The paper introduces constrained TSP datasets, which is meaningful for practical scenarios.

### Weaknesses
 $1.$ The empirical results are not comparable to previous state-of-the-art methods, e.g., DIFUSCO [1], T2T [2], and LEHD [3]. The paper only compares very primary methods. Indeed, image-based diffusion models are not suitable for solving combinatorial problems on graphs due to the complex relationships between edges in graphs. Image models rely on learning local connectivity patterns, which do not align well with the requirements of these problems. Additionally, Gaussian noise is not ideal for discrete decision variables. In fact, discrete diffusion models [1] [2] perform significantly better than continuous diffusion models in solving combinatorial problems.

I suggest that the authors compare their method against these more recent and relevant baselines (DIFUSCO, T2T, LEHD). Additionally, the authors could address the potential limitations of using image-based diffusion models and Gaussian noise for discrete combinatorial problems, and explain how their approach overcomes these challenges.

$2.$ The paper lacks a strong motivation for the proposed methodology. While it appears that the primary motivation is to address performance limitations, discrete diffusion models already yield good results for the TSP, and the results presented in this paper do not surpass those achieved by existing models (indeed not compared).

### Questions
1. Please show evidence that image-based diffusion models can maintain advantages over graph-based models in solving combinatorial optimization problems. Please also provide the empirical evidence.

2. For Tables 2, 3, and 4: The baselines did not account for handling more complex constraints, so a direct comparison is somewhat unfair. It is necessary to introduce some naive constraint-handling training approaches for a fairer evaluation. For instance, authors could consider finetuning the baselines on the constrained TSP datasets with the same adopted adaptations in evaluation.

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
4

### Summary
This manuscript introduces DDRL as an approach for solving the Traveling Salesman Problem (TSP), combining diffusion models with reinforcement learning to address both standard and constrained TSP instances. DDRL leverages a pre-trained diffusion model to improve scalability and convergence stability, showing competitive performance across a range of problem sizes and constraints, including obstacles, paths, and clusters. Experimental results indicate that DDRL outperforms provided approaches in terms of robustness and computational efficiency.

### Strengths
1. Combining image representations with graph data within the reinforcement learning framework is innovative. 
2. The introduced new constraint types likely resemble challenges in real-world applications, such as avoiding restricted zones or adhering to specific routes.

### Weaknesses
1. The proposed integration of diffusion models with reinforcement learning for TSP appears to be a straightforward adaptation rather than a deeply innovative approach. 
2. The experimental comparison lacks a broader set of competitive baselines in Table 1. Including additional RL-based methods, such as POMO [1] and the following works, which has demonstrated strong performance on TSP, would provide a more rigorous assessment of DDRL’s effectiveness.
3. The TSP instances addressed in this work are relatively small. Existing diffusion-based methods[2] can solve TSP instances up to 10,000 nodes, so demonstrating DDRL’s applicability to larger-scale problems would significantly enhance its impact and practical relevance.
4. Tables 2–4 introduce constraints that fundamentally alter the TSP problem’s nature, but the baseline deep learning methods are trained only on basic TSP instances. Without adapting these models to constraint-specific conditions, the comparison may not fully reflect their potential performance, limiting the fairness of the results.

### Questions
1. Given the challenges of scaling DDRL to large TSP instances, how does the method address the trade-off between image resolution and the number of nodes? As the number of nodes grows, higher resolution images would be required to accurately represent node relationships, potentially increasing computational demands. Are there strategies within DDRL to manage this balance effectively?
2. How does the choice of pre-trained diffusion model affect DDRL's performance? Since the pre-trained model provides prior knowledge, its influence on convergence and solution quality may be significant. A more detailed ablation study examining different pre-trained diffusion models or varying levels of pre-training could provide insights into its impact on the results and the model's dependency on this component.

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
3

### Summary
This paper presents DDRL, a framework that integrates diffusion models with RL to solve TSP and its complex constrained variants. DDRL uses a latent vector to generate an adjacency matrix, unifying image and graph learning within a single RL framework. A pre-trained diffusion model is employed as a prior to improve convergence. Extensive experiments on various TSP variants demonstrate the framework’s effectiveness.

### Strengths
* This paper is well-written.
* The proposed method is novel, integrating diffusion with RL to solve TSP.
* The author provides a theoretical foundation for the approach.
* The authors provide the source code for reproducibility.

### Weaknesses
 * The literature review is limited. More recent works on TSP should be discussed.
* The problem size is relatively small. While DIFUSCO can solve TSP instances up to 10,000 nodes, this paper only addresses instances ranging from 20 to 200 nodes. This limited scale raises concerns about the method's applicability to real-world problems, where instances often involve thousands of nodes. The paper does not adequately address the computational complexity of the proposed method as the problem size increases, which is a critical factor for practical use.
* The baseline comparisons are insufficient. For the basic TSP, recent methods such as POMO, DIFUSCO, and UTSP should be included. Furthermore, the comparison should not only focus on the final solution quality but also on the computational cost and convergence speed. The lack of a thorough comparison makes it difficult to assess the true advantages of the proposed approach.

### Questions
* Is the trained model invariant to problem size $N$? 
* Could the proposed method guarantee satisfaction of the constraints? How?
* Could the proposed method solve constrained problems that are not visually intuitive (e.g., PCTSP and CVRP)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a method integrating diffusion models with reinforcement learning (RL) to solve Traveling Salesman Problems (TSPs). They use image to represent TSP, then optimize the latent matrix corresponding to the TSP image using RL.

### Strengths
1. The attempt of combining TSP images and RL seems interesting and original.
2. The structure of this paper is reasonable.

### Weaknesses
1. The proposed method may have limited applicability to other combinatorial optimization problems due to the following reasons:  
   a) Images might only be effective in representing certain graph-based problems, which restricts their contribution to the broader field of neural combinatorial optimization. Specifically, the transformation of a graph into an image may lose crucial structural information, such as edge weights or specific node relationships, that are essential for many combinatorial problems beyond the TSP. This raises concerns about the generalizability of the approach to problems with more complex graph structures or constraints.
   b) The use of images could significantly slow down inference speed. The image-based approach introduces additional computational overhead due to the processing required by the diffusion model, which involves multiple denoising steps. This overhead could be particularly problematic for large-scale instances, making the method less practical compared to direct graph-based methods that operate on the problem's native representation.
   c) Image resolution may heavily impact model performance, further limiting the method's generalization. The fixed image resolution may not be suitable for all problem sizes, potentially leading to information loss for larger instances or unnecessary computational costs for smaller ones. The choice of resolution is a critical hyperparameter that requires careful tuning and may not generalize well across different problem scales.

2. The baseline models used in the study are outdated, with the most recent one published in 2022. Additionally, these baselines do not account for constraint modeling, potentially making the comparison experiments unfair. The lack of comparison against state-of-the-art methods that incorporate constraint handling makes it difficult to assess the true performance of the proposed method. It is crucial to compare against recent, strong baselines that address similar problem settings to provide a fair evaluation.

3. The paper lacks a thorough discussion on computational cost, including inference and training time, as well as scalability when addressing larger TSP instances. The absence of detailed computational analysis makes it difficult to assess the practicality of the method. Information on training time, inference time, and memory usage is essential for understanding the method's feasibility for real-world applications.

4. It is noted that the dimension of the latent matrix is predefined and fixed. This raises concerns about how the method generalizes to TSP instances of varying sizes. The fixed latent matrix dimension may limit the method's ability to adapt to different problem sizes, potentially requiring retraining for each new instance size. This lack of flexibility is a significant limitation for practical applications where problem sizes may vary.

### Questions
Please refer to the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2
