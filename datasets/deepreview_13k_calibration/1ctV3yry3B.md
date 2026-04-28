# MazeNet: An Accurate, Fast, & Scalable Deep Learning Solution for Steiner Minimum Trees

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5, 3, 3

## Abstract
The Obstacle Avoiding Rectilinear Steiner Minimum Tree (OARSMT) problem, which seeks the shortest interconnection of a given number of terminals in a rectilinear plane while avoiding obstacles, is a critical task in integrated circuit design, network optimization, and robot path planning. Since OARSMT is NP-hard, exact algorithms scale poorly with the number of terminals, and so practical solvers sacrifice accuracy for large problems. We propose and study {\em MazeNet}, a deep learning-based method that learns to solve the OARSMT from data. MazeNet reframes OARSMT as a maze-solving task that can be addresssed with a recurrent convolutional neural network (RCNN). A key hallmark of MazeNet is its scalability: we only need to train the RCNN blocks on mazes with a small number of terminals; mazes with a larger number of terminals can be solved simply by replicating the same pre-trained blocks to create a larger network. Across a wide range of experiments, MazeNet achieves perfect OARSMT-solving accuracy, with significantly reduced runtime compared to classical exact algorithms, and with the ability to handle larger numbers of terminals than state-of-the-art approximate algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The authors propose a neural network-based framework named Mazenet for the Obstacle Avoiding Rectilinear Steiner Minimum Tree problem, an important combinatorial problem associated with circuit routing. 

Mazenet is derived from an image classification perspective. The algorithm involves mapping an input graph and set of terminals to an image. An recurrent convolutional network is then trained on synthetic data to sequentially predict elements of the steiner tree. A termination condition module is trained to detect once a candidate path is detected. 

The authors demonstrate that Mazenet recovers the OARSMT faster than classical exact algorithms and highlight its ability to generalize to problem settings beyond its training set. Some ablation experiments detailing Mazenet’s  test accuracy and training time are provided. Superior runtimes are reported and perfect test accuracy.

### Strengths
- The authors propose a novel image-based pipeline for the OARSMT problem
- The synthetic dataset generation is interesting
- Superior runtimes are reported on a variety of synthetic benchmarks compared to classic methods

### Weaknesses
 - weak experimental results. The authors evaluate their method on synthetic benchmarks and compare to old methods.
- some confusing results. figure 14 does not imply perfect test accuracy despite the claims made in the paper.
- the authors may consider a more rigorous evaluation with the current state of the art, FLUTE or any number of other recent methods, e.g. Chen et al., A Reinforcement Learning Agent for Obstacle-Avoiding Rectilinear Steiner Tree Construction, 2022, Kahng et al., NN-Steiner: A Mixed Neural-algorithmic Approach for the Rectilinear Steiner Minimum Tree Problem, 2023, etc.
- evaluation on real datasets is critical to understand the performance benefit of the proposed method.



### Questions
can the authors comment on how does the method compare to other recent works?

can the authors clarify the discrepancy between figure 14 and the perfect accuracy claims made in the main text

_our method reaches the solution in very few iterations, as seen in Figure 15. This contrasts with the competing methods, which often rely on loops that repeat for many more iterations to arrive to a solution_ - I could not understand the significance of this claim. Can the authors provide additional insight?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes MazeNet, a learning-based algorithm that leverages a recurrent convolutional neural network to predict a single-channel binary matrix iteratively, thereby solving the Obstacle Avoiding Rectilinear Steiner Minimum Tree (OARSMT) problem. The algorithm is evaluated on different mazes with 2-8 terminals, showing 100% test accuracy and competitive planning speed.

### Strengths
1. This paper formulates the OARSMT into a binary image prediction problem, which is easy to understand and reasonable.

2. The experimental results show that MazeNet is able to achieve an impressive 100% test accuracy.

3. The experimental results show that MazeNet scales well with an increasing number of terminals.

### Weaknesses
1. The mazes that MazeNet is evaluated on are too small, of only 11 x 11 kernels. There is not strong evidence that MazeNet can perform well on larger mazes. The current evaluation does not sufficiently demonstrate the algorithm's ability to scale to more complex scenarios. The limited size of the mazes may not capture the challenges associated with longer paths and more intricate obstacle configurations, which are commonly encountered in real-world applications of OARSMT.

2. This work only compares MazeNet with classical solvers like Dijkstra, Mehlhorn and Kou, etc. However, there are some more recent algorithms that are either learning-based or CPU-based, e.g., [1], [2]. [3]. Comparison with more and stronger baselines is needed to consolidate the conclusion. The lack of comparison with state-of-the-art methods, particularly those that also leverage learning or are optimized for similar problems, makes it difficult to assess the true novelty and performance of MazeNet. The current baseline selection does not provide a comprehensive view of the landscape of existing solutions.

3. It is not new to learn to predict the future images, e.g., [4] also formulated the grid-like motion planning problem into a video prediction problem. From this paper, I can not see how the specific domain knowledge from OARSMT is incorporated into the network design. The paper does not clearly articulate how the specific constraints and characteristics of the OARSMT problem are embedded into the neural network architecture. The approach seems to treat the problem as a generic image prediction task without leveraging the unique properties of Steiner tree construction.

### Questions
1. How is the threshold 0.65 decided as the TC threshold? Is there ablation study to find the optimal value?
2. What is the step size of the solver, i.e., how many cells are the trees extended in each iteration? How many one entries are contained in the predicted binary matrix?
3. Curious what is the performance of MazeNet on large mazes, e.g., 256 x 256?

### Soundness
2

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
4

### Summary
MazeNet, a recurrent convolutional neural network (RCNN) for the Obstacle Avoiding Rectilinear Steiner Minimum Tree (OARSMT) problem, shows promise with 100% accuracy in initial tests but requires further validation on larger grids and more terminals to confirm scalability. Questions remain on its novelty, given similar RCNN applications in maze-solving, and on its high training time (48.12 hours on four GPUs), along with the need to reduce training data complexity and evaluate the TC module's computational overhead. Additional context through a more detailed literature review would also strengthen the work.

### Strengths
1. MazeNet is designed for scalability and adaptability, making it effective for solving mazes of varying sizes and numbers of terminals that need connection.

2. While RCNNs alone may struggle to identify and verify a correct solution to terminate the process, MazeNet addresses this by incorporating a search-based algorithm that reliably detects a correct solution. This approach combines the speed of graph-based approximate algorithms with the precision of exhaustive graph-based methods.

3. RCNNs provide step-by-step interpretability of the method’s operations, as the head module can be applied at any iteration, allowing for observation of intermediate solution stages. These stages can be visualized as image outputs, providing insight into the solution process at each step.

### Weaknesses
1. The proposed approach of using a recurrent convolutional neural network (RCNN) to solve the Obstacle Avoiding Rectilinear Steiner Minimum Tree (OARSMT) problem may lack novelty, as RCNNs have previously been applied to similar maze-solving problems. The paper does not sufficiently differentiate its approach from existing RCNN applications in pathfinding or maze navigation, leaving the reader questioning the unique contribution of this work.

2. Although MazeNet demonstrated 100% accuracy in the reported experiments, additional proof is needed to confirm it can consistently achieve this level of accuracy across all problem instances. The experiments are limited to a small set of configurations, and it is unclear how the model would perform with different obstacle distributions or more complex topologies.

3. The experimental setup appears limited; testing just on a grid of 11 × 11 nodes with up to 8 terminals may not be sufficient to thoroughly assess MazeNet’s performance, particularly regarding its scalability. The lack of testing on larger grid sizes and with a greater number of terminals raises concerns about the generalizability of the results and the practical applicability of the method.

4. While the TC module improves MazeNet's accuracy, it introduces significant computational overhead, which has not yet been systematically evaluated. The paper does not provide a detailed analysis of the computational cost of the TC module, making it difficult to assess its practical impact on the overall performance of the algorithm. It is unclear how the TC module's runtime scales with problem size and complexity.

5. The paper lacks a dedicated related work section, and a more comprehensive discussion of relevant literature would strengthen the context for this research. The absence of a thorough literature review makes it difficult to position the work within the broader context of existing research on OARSMT and related problems.

### Questions
1. In what ways does the proposed method differ from prior work that applies Recurrent Convolutional Neural Networks (RCNNs) to solve maze-related problems?

2. Does MazeNet require separate training for different grid and terminal configurations, such as an 11×11 versus a 9×9 node grid, or can a single model handle multiple setups?

3. What strategies can be employed to reduce the time and computational complexity involved in generating training data?

4. Training MazeNet reportedly took around 48.12 hours across four GPUs, which is considerable. How does training time scale with increased problem complexity and size, and what optimizations could help reduce this duration?

5. In Figure 8, is the runtime of MazeNet measured with parallelization applied?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The article establishes a MazeNet model to solve the OARSMT problem. Specifically, it first converts the graph representation of the maze into image representation, then processes the image data using the RCNN model, and finally reduces the model's running time through a termination condition.

### Strengths
The application is interesting.

### Weaknesses
1.	The motivation is not clear, as the article does not explicitly outline the problems with previous solutions to the OARSMT problem, nor does it explain how this article addresses these issues.
2.	The experimental evaluation metric design is unreasonable. The OARSMT problem is an NP-hard problem. However, the evaluation metric used in this article's experimental section is accuracy. While for small-scale problems, the shortest path can be obtained using Dijkstra's algorithm for comparison to calculate precision, for large-scale problems, it is challenging to solve using Dijkstra's algorithm. 
Furthermore, the second part of the article clearly states that the optimization goal is to minimize path length. However, the evaluation metric in the experimental section does not use path length as a measure, which is confusing.
3.	In line 164 of the text, it is stated that "However, these problems were in domains where traditional methods are both fast and accurate, leaving open the question of whether RCNNs can provide similar advantages for more complex graph-based problems." Given that traditional algorithms can achieve good results, what is the significance of this research? Moreover, the question of whether RCNNs can provide similar advantages for more complex graph-based problems remains unresolved. How does this study address or prove this issue?
4.	The resolution of figures 2b and 2c is too low. Although the generated data size is 48x48, clear images should still be placed in the article.
5.	The author's proficiency in English is lacking, and the translation traces are too obvious.
The innovation in this article is weak. Regardless of whether it is RCNN or the conversion of graph representation to image representation, the innovation is very limited. From both a writing and experimental perspective, it resembles more of an experimental report and is not suitable for publication as a research paper.

### Questions
1. The article only mentions the number of samples in the test set. What is the number of samples in the training set?
2. In terms of problem scale, for instance in the field of chip design where there are tens of thousands of nodes with connections that must adhere to certain constraints, can this algorithm achieve good results in larger-scale tasks?
3. The testing accuracy can reach 100%, could this be a result of overfitting?

### Soundness
2

### Presentation
2

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
This paper addresses the Obstacle Avoiding Rectilinear Steiner Minimum Tree (OARSMT), which seeks to find a set of horizontal and vertical connections between a set of points while avoiding obstacles using the minimum overall connection length. The paper's technical approach is to convert OARSMT graphs to images then use a Recurrent Convolutional Neural Network (RCNN) to iteratively highlight the solution. RCNN-based solutions to OARSMT were introduced in previous work, but this paper uniquely extends RCNN-based maze solving to larger maze domains with more terminals where traditional methods are computationally inefficient. In addition, this paper develops a termination condition to avoid both premature termination and excessive runtimes. Finally, this paper includes experimental results with 2-7 terminals in 11x11 mazes with 100% accuracy.

### Strengths
Approach for converting Obstacle Avoiding Rectilinear Steiner Minimum Tree (OARSMT) problem to image-based Recurrent Convolutional Neural Network (RCNN) with extensible training images and more than 2 terminals.

100% empirical accuracy on test cases (40,000 total mazes for 2-5 terminals and 3,000 mazes for 6-8 terminals). Alternatively, graph-based approximation methods of Kou et al. 1981 and Mehlhorn 1988 have errors with 3 or more terminals.

MazeNet is computationally faster than Dijkstra's algorithm when 5 or more terminals are used. 

Maze figures are straightforward and informative (e.g., Figure 4).

### Weaknesses
Several details technical details are unclear (see specific feedback below).

Does not provide any limitations or failure cases. For example, what happens if >> 8 terminals are used? This is only discussed as future work. Does algorithm run indefinately for unreachable terminals?

A lot of overlap with Schwarzschild et. al. 2021, but with additional terminals and the terminal condition module.

The paper emphasizes that their approach is parallelizable (L23, L155, L315) but does not provide key details on how this approach works or report accuracy of experimental results on larger mazes to verify it's utility. Instead, the paper provides a vague description of the parallelization process (Section 3.4, L315) and reports only on runtime performance from parallelization on larger mazes (Figure 9, L466).



### Questions
## Questions

How would researchers replicate your work?

L111 How is O(T!) permutations determined for exhaustive methods?

What is the purpose of the paragraph at L174-182? Is the progressive training algorithm of Bansal et al. used in this work? If so, be explicit and state that.

At L224, "...position, indicating a cycle, it is terminated to prevent redundant processing." After finding a cycle and terminating, which single path is chosen?

Algorithm 1 L245-250 is a bit difficult to follow. "junction found" can only be understood by referencing back to the text. Also, what if the "Move to the direction with highest 'whiteness'" is in the backwards direction?

L269 Why are mazes of 2, 3, or 4 terminals chosen for training? (e.g., as opposed to 5, 6, 7)

L293-295 reference random variables n,k. What distributions are these sampled from?

Parallelization for Scalability Section 3.4 is missing specific details.
How many sections are images divided into? (L320)
How many pixels are "sufficient" overlap? (L322)
For a section with two or more terminals, what is the incentive to find additional paths to other unknown sections?
What is the goal of a section with only one terminal?
How does parallelization work for sections without terminals?

L378 What does "20 MazeNet iterations" refer to? Earlier sections indicated that 30 module iterations are used before checking terminal conditions (L261) and 16 training epochs are used (L310). There is no explanation in the text or table.

## Feedback

L55 describes a 11x11 maze, but the paper does not clarify what "11" refers to until L125 in Section 2.1. Explain what 11x11 means at L55 (e.g., "11x11 node graph").

Figure 5 is first referenced at L266 but provides almost no detail or context for what the "Projection," "Batch," and "Head" blocks are. Projection was referenced once at L176 when discussing another paper's work. Multiple configurations of the batch and head modules are referenced earlier, but all blocks are uniformly labeled without any specification of the differences between them. For example, the first "Batch" represents 30 RB iterations and subsequent "Batch" represents 10 iteration (L261) but these are labeled as the exact same module in Figure 5. As another example, L177-180 reference a "Head" module that produces the output and a "final head module" that transforms the network's output to single-channel prediction. Why not add these details to Figure 5 to be more informative and accurate?

### Soundness
2

### Presentation
2

### Contribution
2
