# An Optimization-Based Framework for Adversarial Defence of Graph Neural Networks Via Adaptive Lipschitz Regularization

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Graph Neural Networks (GNNs) have exhibited exceptional performance across diverse application domains by harnessing the inherent interconnectedness of data. However, the emergence of adversarial attacks targeting GNNs poses a substantial and pervasive threat, compromising their overall performance and learning capabilities. While recent efforts have focused on enhancing GNN robustness from both data and architectural perspectives, more attention should be given to overall network stability in the face of input perturbations. Prior methods addressing network stability have routinely employed gradient normalization as a fundamental technique. This study introduces a unifying approach, termed as AdaLip, for adversarial training of GNNs through an optimization framework that leverages the explicit Lipschitz constant. By seamlessly integrating graph denoising and network regularization, AdaLip offers a comprehensive and versatile solution, extending its applicability and enabling robust regularization for diverse neural network architectures. Further, we develop a provably convergent iterative algorithm, leveraging block majorization-minimization, graph learning, and alternate minimization techniques to solve the proposed optimization problem. Simulation results on real datasets demonstrate the efficacy of AdaLip over state-of-the-art defence methods across diverse classes of poisoning attacks. On select datasets, AdaLip demonstrates GCN performance improvements of up to 20\% against modification attacks and approximately 10\% against injection attacks. Remarkably, AdaLip achieves a similar performance gain on heterophily graph datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper claims to address the vulnerability of GNN to adversarial attacks. While the topic is of interest, the paper's approach and presentation leave much to be desired. The authors introduce AdaLip, an optimization-based framework, but the effectiveness of this method are questionable based on the provided content.

### Strengths
The paper attempts to introduce an optimization-based framework, which could be of interest if executed well.

### Weaknesses
1. The paper lacks a clear and coherent structure. The introduction does not set a clear stage for the problem, and the motivation behind the proposed method is weak.

2. Notation Issues: The paper is riddled with unclear and undefined notations, which severely hampers its readability. Examples include:

$f$ in eq(2)

$\lambda$ in eq(4)

$\mathcal{X}$ in eq(6)

$\theta(x, \Delta)$ in eq(6).

$d$ in eq(7)

$\mathcal{L}, \mathcal{A}$ in Lemma 2

Furthermore, there are inconsistencies in notation usage, such as

 $\left(\theta_{(k+1)}, \phi_{(k+1)}\right)$ and $\left(\theta_{(k+1)}, \omega_{(k+1)}\right)$.

In eq(8), it writes $\min _{\theta, \phi \in \mathcal{S}_\phi}$, however this is different from eq(3).

3. Lack of Motivation for Lemmas: The relevance of certain lemmas, such as Lemma 1, is not clear. Why is it necessary, and how does it contribute to the overall narrative? The connection between Lemma 1 and the subsequent theoretical development is not adequately established.

4. Unclear Statements: The paper contains several vague statements that lack clarity or justification:

"On the contrary, this research explores methods for enhancing the robustness of training across diverse architectural models by inherently minimizing the likelihood of failure, quantified through its stability coefficient."

Clarification needed: How does your approach differ in terms of "robustness of training" compared to other methods? Specifically, what are the limitations of existing approaches in handling diverse architectures, and how does minimizing the stability coefficient address these limitations?

"The overall objective of learning a stable hypothesis $\theta$ as GNN parameters under the constraint of learning a denoised graph structure can be formulated as the general optimization problem". "The set $\mathbb{S}_\theta$ contains all possible stable hypothesis functions mapping from the domain set to the labelled set."

-Clarification needed: How exactly is a "stable hypothesis" defined in this context? It is just a combination of GNN under the constraint of a denoised graph structure. A more rigorous definition is needed, potentially linking it to the concept of Lipschitz continuity or other relevant stability measures.

"One effective method for enforcing Lipschitz constraints on a network during training involves normalizing the parameters of each layer using Projected Gradient Descent (PGD)."

-Clarification needed: Is there a reference here? Providing a specific citation would strengthen this claim and allow readers to understand the context and potential limitations of this approach.

"Without loss of generality, the adaptive Lipschitz regularization in (9) can be equivalently replaced by a logarithmic counterpart."

-Clarification needed: Can you provide proof or justification for this equivalence? This is a significant claim that requires a rigorous mathematical argument or a reference to an established result.

"Lemma 2. By defining linear operators $\mathcal{L}, \mathcal{A}$ and respective adjoint operators $\mathcal{L}^{\star} \mathcal{A}^*$"

-Clarification needed: What is the objective of this lemma? How are these linear operators defined, and why do we need the transformation from (10) to (11)? The purpose and implications of this lemma are not immediately clear.

"$\Delta_{(k)}$ denote the optimal adjacency matrix corresponding to the optimal graph Laplacian $\phi_{(k)}$ at the $k^{\text {th }}$ iteration while solving (8)."

-Clarification needed: what are the iterations here? The iterative process is not clearly defined in the context of solving equation (8).

5. Theoretical Errors:

In the derivation of Theorem 1, the initial inequality appears ambiguous. Either there are missing assumptions that need to be explicitly stated, or the derivation is flawed. A clearer presentation of the steps and underlying assumptions is necessary.

The assertion that $\left|X^{(0)}\right|_F=\sqrt{d}$ lacks justification. What is the basis for this equality? This statement requires a clear explanation or derivation, particularly regarding the properties of the initial feature matrix $X^{(0)}$.

Upon examining Lemma 1 and its accompanying proof, I am at a loss for words regarding its presentation and rigor. The proof lacks clarity and contains undefined terms, making it difficult to follow the logical flow and verify its correctness.

I ceased my examination of the subsequent proofs due to the glaring inadequacies in the mathematical statements presented thus far.

6. Grammatical Oversights: The paper is marred by numerous grammatical errors, particularly concerning punctuation. A glaring oversight is the absence of punctuation marks following ALL equations throughout the document.

7. Disconnect Between Theory and Experiments: The paper claims that AdaLip performs well on heterophily graph datasets, yet there's no evidence or explanation supporting this claim. The experimental section does not provide any analysis or results specific to heterophily graphs, leaving this claim unsubstantiated.

8. Experimental Deficiencies: The experimental section is glaringly inadequate. Not only does it lack a comprehensive set of baselines, but the range of attacks considered is also severely limited. It is imperative to incorporate evaluations against poison and evasion attacks, as well as both white-box and black-box scenarios, and to consider both injection and modification types.

The glaring omission of a multitude of established works on Lipschitz regularization for GNNs is concerning. This oversight casts doubt on the rigor of the literature review.

Furthermore, the paper fails to report any computational costs, leaving readers in the dark about the practicality of the proposed method.

### Questions
Please clarify the issues raised in the weaknesses section.

In its current form, I cannot in good conscience recommend this paper for acceptance. I strongly advise the authors to rigorously revise and contemplate resubmission to a future conference.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors propose a graph adversarial attack defense mechanism, based on the Lipschitz constant and its regularization. 

The authors provide significant amount of theory and then present the experimental evaluation of their method.

### Strengths
The paper is easy to follow. The results look promising.

### Weaknesses
 * The authors propose an optimisation based method. This approach requires taking the gradient of the network and then applying it to the learned weights. However, it is not promised that the network itself is a valid potential function. Therefore, I am afraid that it cannot be guaranteed that the method should converge. Therefore I believe that the theoretical guarantees are not complete as not all assumptions are provided, and also it is not clear if the experiments are conducted with a network that is a potential function. To my understanding, the authors use GCN as a backbone, which is not guaranteed to be a valid potential function. I look forward to read the authors response.

* The authors should add comparisons with recent methods such as "Robust Mid-Pass Filtering Graph Convolutional Networks"

* The authors should discuss recent findings about the evaluation of GNN robustness and conduct experiments with additional benchmarks to show the performance of the model. Please see discussion and data in "Are Defenses for Graph Neural Networks Robust?"

* The authors should provide the runtimes of the method.

### Questions
Please see my review

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces an approach called AdaLip to improve GNN robustness. Specifically, authors first introduce an objective function based on the adaptive Lipschitz regularization, which aims to purify the graph topology and train robust GNNs. Subsequently, authors develop an iterative algorithm that is provably convergent for optimizing the objective function. Experimental results indicate that AdaLip outperforms a few defense baselines under the transfer attack setting.

### Strengths
- Authors have considered both graph modification and injection attacks.
- AdaLip has been evaluated on both homophily and heterophily datasets.

### Weaknesses
 - Missing adaptive attack results. As shown by [1], most prior defense GNN methods can be easily broken by adaptive attacks, which are aware of the given defense method during attacking. Thus, it is very important to adaptively attack the proposed defense model to demonstrate its true robustness. The current evaluation only considers transfer attacks, which do not provide a comprehensive picture of the model's resilience against a determined adversary. Specifically, the attacks should be crafted to exploit the specific mechanisms of AdaLip, such as the adaptive Lipschitz regularization, to truly assess its limitations.
- Missing relevant defense models for evaluation. There are some prior methods (e.g., [2]) for defending on both homophily and heterophily datasets, which are not compared in this work. The absence of comparisons with state-of-the-art defense methods, particularly those designed for both homophilous and heterophilous graphs, limits the assessment of AdaLip's relative performance. For instance, methods that explicitly consider the graph structure and node feature interactions should be included to provide a more robust benchmark.
- Improper claims. It is unclear why prior adversarial training methods (e.g., PGD) cannot be applied to different GNN architectures. Furthermore, since the authors exclusively focus on GCN as the GNN backbone in their experiments, their claim on the adaptability of AdaLip to various GNNs is less convincing. Additionally, the authors assert that PGD is not a suitable choice for solving Equation (4), but they provide no empirical results to support this claim. The lack of empirical justification for these claims undermines the credibility of the proposed method and its purported advantages over established techniques. The authors should provide a more rigorous justification for their design choices.
- There is a lack of sensitivity analyses on $\alpha$ and $\beta$. The performance of AdaLip is likely sensitive to the choice of hyperparameters $\alpha$ and $\beta$, which control the trade-off between the Lipschitz regularization and graph purification. Without a thorough sensitivity analysis, it is difficult to determine the optimal parameter settings and the robustness of the method across different datasets and attack scenarios. This analysis is crucial for the practical application of the method.
- The tightness of the upper bound in Theorem 1 is unclear. The theoretical analysis relies on an upper bound on the Lipschitz constant, but the tightness of this bound is not discussed. A loose bound may not provide meaningful insights into the actual behavior of the method. The authors should discuss the implications of the bound's tightness and its relevance to the practical performance of AdaLip.
- The paper writing can be further improved. Authors have introduced several terms without adequate explanations or definitions, some of which I've listed in the following questions.

### Questions
- What's the "smoothness of vertices"? Do authors mean node feature smoothness? 
- What does the "data adaptivity" mean? 
- What's the definition of high-frequency components within the data? Do authors mean the Laplacian eigenvectors corresponding to the largest eigenvalues? If so, it's unclear to me why AdaLip can work on heterophily datasets since it is less responsive to those high-frequency components.
- What does the "adaLip w/o GD" mean in Figure 1?
- Remark 2 is somewhat unclear. Do the authors mean that AdaLip also employs low-rank approximation on the adjacency matrix? If so, could you please point out the equation in the paper that demonstrates this? Additionally, given that ProGNN also learns a low-rank adjacency matrix, why does Figure 1 illustrate the efficacy of the low-rank approximation?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The presented paper proposed a unified framework based on optimization unfolding. The proposed framewrok combines methods based on updating the graph (denoising) and methods based on training (network regularization).

### Strengths
- The presented paper combines two worlds (graph denoising and regularization), and is flexible enough to allow different choice of components by using different loss function.
- The framework is derived from an optimization perspective, which provides good interpretability of the proposed method.
- Experiment results shows the effectiveness of the proposed method.

-----
I have read the author responce and decided to keep my rating unchanged.

### Weaknesses
 - I found this paper rather sloppy in mathematics. In terms of:
    - Undefined synbols. See Questions.
    - Some synbols are overrided without explanation. For example, in eq.(6) $\theta$ is used to represent a function (the GNN model in my understanding), while in eq.(10) $\theta$ is used to represent the parameters of the model.
    - There are some imprecise terms. 
        - From (3) to (4) the authors say "The problem (eq.(3)) can be rewritten as a joint objective (eq.(4))". I don't see how eq.(3) can be rewritten as eq.(4). Indeed eq.(4) is a relaxed version eq.(3), but they are not equavalent. Doing such relaxation usually requires some related properties of the two problems, e.g. they share the same global optima. For the eq.(3) to eq.(4), I don't see such a relation, at least the authors didn't mention any. Furthermore, the relaxation seems to introduce a hyperparameter which is not discussed.
        - In section 4, there's a sentence "Without loss of generality, the adaptive Lipschitz regularization in (9) can be equivalently replaced by a logarithmic counterpart". I don't see how relacing a part of a equation by its logarithmic counterpart while leaving other parts unchanged is without loss of generality. It's likely eq.(9) and eq.(10) have different global optima. I would suggest the authors just add the log in the original definition eq.(9). The authors should provide a formal proof or at least a more detailed explanation of this claim.
- For the two stage approach, I don't see why it can converge. The given theorem only proves the convergence of the joint optimization approach. The two-stage approach is not guaranteed to converge to a stationary point of the original objective, and it is unclear if it even provides a good approximation.
- The experiments are performed only on small graphs. I wonder what is the computational complexity of the proposed algorithm and if it is limited on small graphs? A formal analysis of the computational complexity is missing. The provided experiments on the Cora dataset are insufficient to demonstrate the scalability of the proposed method. It is unclear how the runtime would scale with larger graphs, and the reported runtimes on Cora suggest that the method may be computationally expensive.
- The proof of Theorem 1 is looks problematic. Overall, I think it's unlikely that the Lipschitz constant depends only on the parameters but not on the activation function and the structure of the GNN.
    - For the first inequal symbol in eq.(2) in the appendix, how is $\sigma$ disapeared? Doesn't this require $\sigma$ to be $1$-Lipschitz? This step needs further clarification. The authors should explicitly state the assumptions on the activation function $\sigma$ for this inequality to hold.
    - The proof of Theorem 1 assums a very specific structure of GNN (basically GCN), which mismatches the definition of GNN given in section 2.1. The authors should state it explicitly that it works only for a specific implementation of GNN in the statement of  Theorem 1. Alternatively, you can also assume $\mathcal M$ and $\mathcal U$ are Lipschitz continous and combine the Lipschitz constant of them into the bound.

### Questions
There are some undefined or unclear notations. Although I can guess most of them but it's better to define them clearly.

 - In eq.(1), what is $\mathcal N$?
 - In eq.(3), what is $\phi$? Also, based on the definition of $\mathcal S_{\phi}$, is $\phi \in \mathcal S_\phi$ just a graph Laplacian?
- In Theorem 1, is $E$ a scalar or vector? In the statement it says $|\Delta - \Delta_p| \overset{\text{def}}= |E|$, which makes it looks like a scalar, but in the equation it uses $\\|E\\|_2$, which makes it looks like a vector.
- In Lemma 2, what is $\omega$? Is it a scalar or vector?
- In eq.(21), what is $L_q$?

It's possible that I missed some definitions or assumptions. Feel free to point out if I missed something.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
