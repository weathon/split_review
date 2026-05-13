# GFlowNets Need Automorphism Correction for Unbiased Graph Generation

- Decision: Reject
- Scores: 6, 5, 6, 6, 5

## Abstract
Generative Flow Networks (GFlowNets) are generative models capable of producing graphs. While GFlowNet theory guarantees that a fully trained model samples from an unnormalized target distribution, computing state transition probabilities remains challenging due to the presence of equivalent actions that lead to the same state. In this paper, we analyze the properties of equivalent actions in the context of graph generation tasks and propose efficient solutions to address this problem. Our theoretical analysis reveals that naive implementations, which ignore equivalent actions, introduce systematic bias in the sampling distribution for both atom-based and fragment-based graph generation. This bias is directly related to the number of symmetries in a graph, a factor that is particularly critical in applications such as drug discovery, where symmetry plays a key role in molecular structure and function. Experimental results demonstrate that a simple reward-scaling technique not only enables the generation of graphs that closely match the target distribution but also facilitates the sampling of diverse and high-reward samples.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper shows that the so-called problem of equivalent actions (appearing from graph symmetries) biases graph generation processes in GFlowNets. To tackle this, the paper proposes a simple correction procedure that scales the reward function by the number of symmetries of the associated graph (terminal state).  Experiments on artificial data and molecule generation tasks aim to show the effectiveness of the proposed approach.

### Strengths
- **Clarity**: Overall, the text is well-written and easy to follow (despite some overloaded notation);
- **Motivation and Relevance**: The motivation is clear, and the problem is relevant as graph (molecule) generation is one of the main applications of GFlowNets;
- **Flexibility**: The proposed correction procedure is flexible as it applies to different training schemes (balance conditions).

### Weaknesses
 - **Computational cost**: While the paper mentions the additional cost didn't lead to "significant delays in computation", it is not clear why. I believe the paper deserves a more comprehensive discussion about the computational complexity of the proposal. Specifically, the paper should analyze the time complexity of computing the automorphism group size for different graph structures and sizes. Also, I wonder if the proposed approach becomes prohibitive in some settings, particularly for very large or highly symmetric graphs. The lack of a detailed analysis makes it difficult to assess the practical applicability of the method.

- **Experiments**: The theoretical analysis does not seem to support the claimed gains on real-world datasets. The paper should clarify how the proposed correction impacts the diversity and reward of the generated molecules, especially in the top-k setting. It is not sufficient to only measure Pearson correlation; the practical implications for downstream tasks should be more thoroughly investigated. Also, although the paper cites ZINC250K in the Introduction, the experiments only include the QM9 dataset. The absence of experiments on larger, more complex datasets limits the generalizability of the findings.

- **Technical novelty**: The theoretical contributions of the paper are straightforward. I wonder if the GFlowNet community already knows about the equivalent action problem. The paper should provide a more detailed comparison to existing methods that might implicitly or explicitly address this issue. The lack of a thorough literature review makes it difficult to assess the true novelty of the proposed approach.

- **Notation**: I found the notation overloaded, which may confuse readers unfamiliar with GFlowNets. For instance, the paper uses the same $P_F$ to refer to the graph-level, state-level policies, and the marginal distribution over terminal states (i.e., $P_F(x)$). This ambiguity can lead to confusion and hinder the understanding of the proposed method.

- **Limitations**: The paper does not discuss limitations. The authors should address the limitations of the proposed method, such as potential issues with very large graphs, specific types of reward functions, or the approximation of the automorphism group size.

### Questions
1. Could the authors provide a detailed analysis of the computational complexity of the proposal? Are there environments where the proposed method becomes prohibitive?

2. Could you provide time comparisons for the real-world experiments?

3. The paper says "A reward exponent of 1 is used for the atom-based task, and a value of 16 is used for the fragment-based task". Was this choice based on prior works? If not, could you elaborate on this choice?

4. Is this the first paper to bring attention to the "action equivalent problem"? Could you elaborate on the impact of your findings on previous works that use GFlowNets for graph generation? 

5. I suggest turning Theorem 2 into a Corollary of Theorem 1.

### Soundness
3

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
This work points out that automorphic actions may cause GFlowNets to artificially over/undersample terminal states compared to the target distribution. They also propose a fix by re-scaling the reward to account for the size of the automorphism group of terminal states. They illustrate the pathology and their fix in a toy example and a molecule generation task.

### Strengths
* This work is overall well-written and easy to follow;
* It shows that a common practice of treating graphs as if they were the GFlowNet states leads to incorrect sampling --- implying that, to some extent, there is a series of incorrect experiments in the GFlowNet literature;
* Authors provide a quick fix to the issue.

### Weaknesses
 * It appears Figure 3 uses Equation 3 to compute the final state probabilities. I am not sure this is a fair evaluation. I suggest the authors use the empirical approximations of the distributions over terminal states (based on GFlowNet samples) for comparison. For instance, measuring L1 between the empirical sampling distribution and the target.

* The metrics in Table 1 have no direct relationship to goodness-of-fit. I understand enumerating the terminal states is impossible for extensive supports, making computing the L1 distance to the target unfeasible. Nonetheless, authors could use the FCS [1] as a proxy. Otherwise, we cannot draw conclusions about sampling correctness in large environments.

* Authors said the additional cost of running BLISS in the final states is negligible. I reckon this should be task-specific. This shouldn't intuitively be negligible if all intermediate states are also final. Please elaborate on the discussion and provide numbers/experimental evaluations. 

* The experimental campaign is relatively short compared to recent works on GFlowNets. 

* While I value the authors' contribution, I believe their contributions and derivations are somewhat straightforward and the work's novelty is limited.

### Questions
* It would be nice to see an illustration of the bias authors point to using a uniform target. Then, plotting the marginal over the size of automorphism relations for each sample should highlight this bias.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work first studies the properties of equivalent actions when applying GFlowNets for graph generation. Equivalent actions denote the set of actions that lead to isomorphic graphs at each step of the autoregressive generation process. This work provides a theoretical analysis on the impact of ignoring equivalent actions and points out that it would introduce bias in the sampling distribution. With this insight, this work further proposes a simple correction on the GFlowNet objectives by using the order of the automorphism group to account for equivalent actions. This can correct the reward for highly symmetric graphs.

Experiments on small graph generation and small molecule generation are conducted to show the performance of the proposed correction.

### Strengths
(1) It is really interesting and valuable to the community to identify the impact of ignoring equivalent actions in GFlowNets for graph generation. The theoretical analysis is quite sound from my reading and I think it is valuable to other readers.

(2) The theoretical results are quite elegant, thus leading to a simple correction to the original GFlowNets objectives. It is quite enjoyable to see that the correction term is the order of the automorphism group.

(3) The experiments can show that with such a simple correlation, the sampling bias and resulting performance are notably improved, which can support the theoretical analysis and the proposed corrected objectives straightforwardly.

(4) The paper is well written.

### Weaknesses
 (1) It looks really computationally expensive to evaluate the order of the automorphism group and the complexity could increase exponentially with the size of the graph. I understand that the paper provides some analysis on the computation. However, the experimental study on the complexity is missing, while it is very important to assess the practical usefulness of the proposed idea.

 (2) I am a bit concerned about the practicality of the method. The experiments are mainly on small graph and small molecule generation. It is unclear if this method can be scalable to generate large molecules.

### Questions
See the weaknesses section

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to address issues in graph generative GFlowNets that may fail to construct the target distribution due to equivalent actions. Specifically, it analyzes how discrepancies in the number of automorphism groups cause GFlowNets to incorrectly estimate the true reward. To address this, the paper incorporates the number of automorphism groups into the reward function and proves how this corrects reward underestimation. Notably, this paper also considers practical implementation for correction in fragment-based generation. Experimental results show that the proposed method better captures the target distribution.

### Strengths
- The paper is well-written and easy to follow, and the proposed method is conceptually straightforward.
- This work is the first to address a significant pitfall in GFlowNets, i.e., errors due to equivalent actions, within primary setting of GFlowNets, i.e., graph generation.
- The authors provide a solid theorem for the corrected objectives showing how their global optima enable GFlowNets to construct the correct target distribution. Although the proofs consider TB and DB, these can also be easily extended to other objectives, such as subTB.
- The experiments are thorough and consider both important settings, namely atom-wise and fragment-wise graph generation.

### Weaknesses
No weakness in the major flows. It seems that there are no errors in the proof.

### Questions
- To better highlight the pitfalls, I wonder if the authors provide or illustrate a toy-example or toy-experiments where the conventional approaches induce an incorrect generative distribution, e.g., a distribution significantly biased towards the graphs with a low number of automorphism groups.
- Can authors provide the experimental computational costs for computing $|\text{Aut}(s)|$? I am curious about how much overhead the proposed method requires in practice, although the authors provide the time complexity in **Line 378**. Could this overhead be minor relative to time for reward computation or time for sampling trajectories?
- In DB-based implementation, I wonder if there might be improvement in convergence speed when we reparameterize the flow function $F(s)=\tilde{F}|\text{Aut}(s)|$ (like a prior flow reparameterization approach [1]), although this preserves the asymptotic optimality to induce the target distribution.

---

[1] Pan et al., Better Training of GFlowNets with Local Credit and Incomplete Trajectories, ICML 2023

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
2

### Summary
This paper focuses on Generative Flow Networks (GFlowNets), which are generative models used to produce graphs. While GFlowNet theory ensures that a fully trained model can sample from an unnormalized target distribution, the challenge lies in computing state transition probabilities, particularly due to equivalent actions that lead to the same state. The paper analyzes these equivalent actions in graph generation tasks and proposes efficient solutions to mitigate the associated challenges.

### Strengths
1. The paper is well organized and the theories are well formulated.

2. The motivation is well introduced.

### Weaknesses
1. How does the proposed method compare with other graph generative models, such as flow-based and discrete diffusion-based models?

### Questions
N.A.

### Soundness
2

### Presentation
2

### Contribution
2
