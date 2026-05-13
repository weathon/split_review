# Neural Deconstruction Search for Vehicle Routing Problems

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Autoregressive construction approaches generate solutions to vehicle routing problems in a step-by-step fashion, leading to high-quality solutions that are nearing the performance achieved by handcrafted, operations research techniques.
In this work, we challenge the conventional paradigm of sequential solution construction and introduce an iterative search framework where solutions are instead deconstructed by a neural policy. Throughout the search, the neural policy collaborates with a simple greedy insertion algorithm to rebuild the deconstructed solutions. Our approach surpasses the performance of state-of-the-art operations research methods across three challenging vehicle routing problems of various problem sizes.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes Neural Deconstruction Search (NDS), a novel method for vehicle routing problems that iteratively improves solutions by selectively removing and re-inserting nodes. A reinforcement learning-based policy network guides the removal process, while a greedy insertion strategy reconstructs efficient routes. NDS achieves competitive performance and improves solution quality compared to traditional approaches.

### Strengths
- Originality: The paper proposes a unique deconstruction-reconstruction framework for VRPs, leveraging a reinforcement learning policy to optimize solution quality in a novel way.
- Quality: The experiments are thorough, showing significant performance improvements across multiple VRP benchmarks and validating the approach’s robustness.
- Clarity: The paper is well-organized, with clear explanations and visuals that make the deconstruction and reconstruction process easy to understand.

### Weaknesses
 - The paper introduces a deconstruction and re-insertion heuristic for VRP improvement, but it lacks a clear comparison with well-known heuristics, such as the 2-opt method, which also iteratively refines solutions. Providing an explanation of how the proposed approach differs from 2-opt would clarify the advantages of using a learning-based method for the deconstruction-recreation process.

- While the paper presents NDS as a novel learning-based improvement heuristic (Costa, 2020), it does not include comparisons with other learning-based approaches in the same category. A comparative analysis with similar methods would offer a more complete view of NDS’s performance and highlight its specific strengths and weaknesses within the context of learning-based VRP solvers.

- The current experiments are restricted to a specific subset of VRP problems, but VRP encompasses a wide variety of problem settings (see Berto, 2024). Testing the proposed approach on additional VRP problems, or explaining any limitations that prevent its application to other settings, would strengthen the generalizability of the method and provide clarity on its applicability across diverse VRP scenarios.

- The paper lacks details on how LEHD, BQ, and other learning-based solver baselines were trained and configured for this study. This is especially crucial because the reported performance for these methods differs from their original papers. Specifically, LEHD was originally trained on problems with up to 100 nodes; further clarification on how it was trained in this paper’s setting is necessary to interpret the experimental results accurately. Including these details would make the experimental setup more transparent and allow for better reproducibility and understanding of the baseline comparisons.

### Questions
Is the proposed deconstruction-reconstruction framework specifically designed to be effective only for VRP-type problems, or could it be adapted to other combinatorial optimization problems with different structural properties, such as Maximum Independent Set (MIS)? Have the authors considered or explored the potential adaptability of this approach to CO problems beyond VRP? Understanding any insights or limitations regarding its generalizability would clarify whether this framework could be broadly applicable across different types of optimization challenges.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper falls within the realm of using learning-based approaches or elements to solve vehicle routing problems. Specifically, it proposes to deviate from the existing step-by-step approaches that usually focus on autoregressive construction techniques. Instead, it proposes an iterative search framework that uses a neural policy for deconstruction and a relatively simple greedy insertion algorithm to repair the respective solutions.
The paper shows promising results on various vehicle routing problem variants.

Overall, I think that this paper makes a valuable contribution to the field but is currently borderline in its exposition as the authors clearly oversell the contribution. Yet, this aspect can easily be healed and if the authors are willing to do so, I believe that this paper will be of interest to the ICLR community and could be accepted.

### Strengths
1) The paper is technically well-written and easy to follow

2) The presented experiments are of sufficient breadth

3) The proposed methodology opens an interesting avenue for algorithm design that deviates from existing approaches that usually focus on using neural policies to construct solutions in a step-by-step fashion.

4) The results show promising performance compared to existing methods.

### Weaknesses
As indicated in my summary, the authors are currently (significantly) overselling the contribution of the proposed method.

This relates to the fact that numerical experiments are - to some extent - comparing apples with oranges due to limiting the computation times of the studied algorithms instead of using a proper performance-based stopping criterion. This experimental design choice clearly favors the search technique proposed by the authors, as the neural deconstruction works instantaneously.

In practice, one would not use such a time-based criterion as the problems studied are static problems usually solved in a day-ahead fashion, where solution times are not limited to seconds. In such cases, one would usually finetune an algorithm based on a performance-based stopping criterion, i.e., the number of consecutive iterations without improvements.  Furthermore, the time limit does not account for the training time of the neural network, which is a significant overhead not present in the benchmark algorithms. This makes the comparison even more skewed.

Beyond this rather unconventional experimental design decision, the authors also do not provide details if and if so how the benchmark algorithms have been tuned.

Looking at the fact that hyperparameter tuning seems to be missing for the benchmark algorithms and that the experimental design in general favors the proposed algorithm, I think that statements like "Our approach surpasses the performance of state-of-the-art operations research methods" are not sufficiently substantiated and should be toned down, not only in the abstract but in the manuscript.

I think that the authors make an interesting contribution to the field that is obvious without such overselling statements. The paper as well as the understanding of the reader will benefit from a more nuanced discussion and analyses of performance and computational complexity. I think that the authors can easily address this aspect, e.g., by
1) toning down the respective claims, particularly in the papers abstract, contribution section, and results discussion.
2) adding information on hyperparameter tuning for all algorithms in an appendix
3) adding results where the benchmark algorithms have a more suitable stopping criterion. -even if the proposed algorithm then does not surpass the benchmarks, one can see the full picture and discuss the results for both stopping criteria more nuanced
4) commenting on the training effort of the proposed method compared to the benchmarks not requiring such a training phase

### Questions
In Section 4.4 you discuss generalization against distribution shifts, did you also investigate this for varying instance sizes?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper adopts a destroy-reconstruct iterative search framework to improve the quality of VRP solutions. The destruction step is performed by the proposed attention-based model, which removes customer nodes step by step from the solution; then, the removal of customer nodes are inserted into the destroyed solution node by node using a simple greedy insertion method. In addition, this paper also adopts a simulated annealing mechanism to allow worsening solutions to be accepted during the iteration process. Experimental results show that the proposed method achieves state-of-the-art performance on CVRP, CVRPTW, and PCVRP.

### Strengths
1. The paper writing is fluent.
2. Experiments show outstanding performances on three VRPs.

### Weaknesses
1. From my point of view, the framework of this paper is mainly based on SISRs. This paper replaces the heuristic destruction process of SISRs with a learning-based destruction strategy. The greedy insertion with simulated annealing in this paper is essentially the same as the heuristic reconstruction process "greedy insertion with blinks" in SISRs, both of which have the probability of accepting differential solutions to jump out of the local optimum. Based on the above observations, I think the framework of this paper remains at the engineering level. It is a migration of the framework of SISRs, which is not novel enough.
2. Since the performance of SISRs is promising, it is foreseeable that it will be better after adding the machine learning strategy. In Table 1, the performance gap between the proposed method and SISRs is not significant especially when N is large. Therefore, I believe that the main performance source of the proposed method is the framework of SISRs.
3. The proposed method is similar to the SISRs framework, so I suggest the authors discuss its relation to SISRs in the related work section. Many details are not explained clearly, such as how to train the model on VRPTW and PCVRP, what changes are made, and how to meet the constraints.
4. There needs more baselines to compare. It should introduce more comparison algorithms for VRPTW and PCVRP, and CVRP should also introduce newly emerged baselines such as ELG [1] and UDC [2].

### Questions
1. Why is greedy insertion used to reconstruct the solution, rather than other methods such as regret insertion?
2. Can the proposed method solve the TSP?
3. There is no ablation study on the random seed v. And could you describe the reason for choosing the hyper-parameters in this paper, such as threshold factor and temperature?
Minor question:
4. Figure 3 should be corrected to a vector diagram.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Tins paper uses deep neural network (DNN) to trun the operation of removing nodes into a sequence generation process with the aim of achieving a fast serach process without sacrificing the high quality search guidance of the DNN. The solution is then finally reconstructed using greedy methods. While the work has some merit, the main contribution does not meet the novelty expectations of ICLR.

### Strengths
1. Although the method is simple, it achieves a certain effect.

### Weaknesses
1.	Just replacing a heuristic process of removing nodes with a DNN is too simple. The contribution here does not significantly advance the field. I think the authors need to explain what are the differences and advantages of the proposed method for removing nodes over the previous methods?
2.	A similar approach of using DNNs to remove and reconstruct solutions has been used in papers [1]. However the proposed method only uses DNNs for node removal and greedy methods for reconstruction. There are three other papers[2-4] on learning similar local search operations in VRP, and those methods can also be used directly to learn removal and reconstruction.
3.	IMPROVEMENTSTEP is used first in Algorithm 1, with no specific explanation as to why.
4.	There are no details about the way you use DNNs in the decoding process, leading the reader to have little understanding of the mechanism.
5.	This part of the formulation needs further discussion: “This contrasts with construction-based methods, where each decision is independent of prior selections.”. However, the current construction-based methods also retain the customer information selected in the previous step or part of the path information during the decoding process.

### Questions
What are the advantages of this paper over previous papers that have implemented reconstructive solving using DNN, please explain in detail.

### Soundness
3

### Presentation
2

### Contribution
2
