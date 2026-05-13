# Unlocking Global Optimality in Bilevel Optimization: A Pilot Study

- Decision: Accept
- Scores: 6, 5, 6, 3, 6, 8

## Abstract
Bilevel optimization has witnessed a resurgence of interest, driven by its critical role in trustworthy and efficient machine learning applications. Recent research has focused on proposing efficient methods with provable convergence guarantees.  However, while many prior works have established convergence to stationary points or local minima, obtaining the global optimum of bilevel optimization remains {\em an important yet open problem}. 
The difficulty lies in the fact that unlike many prior non-convex single-level problems, this bilevel problem does not admit a ``benign" landscape, and may indeed have multiple spurious local solutions.
Nevertheless, attaining the global optimality is indispensable for ensuring reliability, safety, and cost-effectiveness, particularly in high-stakes engineering applications that rely on bilevel optimization. In this paper, we first explore the challenges of establishing a global convergence theory for bilevel optimization, and present two sufficient conditions for global convergence. 
We provide algorithm-specific proofs to rigorously substantiate these sufficient conditions along the optimization trajectory, focusing on two specific bilevel learning scenarios: representation learning and data hypercleaning (a.k.a. reweighting). Experiments corroborate the theoretical findings, demonstrating convergence to global minimum in both cases.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the convergence properties of a penalized bilevel gradient descent (PBGD) algorithm, aiming to obtain global optimal solutions of bilevel optimization problems under the joint and blockwise Polyak-Łojasiewicz (PL) conditions. The joint and blockwise PL conditions are validated in the context of two specific applications: representation learning and data hyper-cleaning. Numerical experiments are provided to substantiate the theoretical results.

### Strengths
1.	The study of convergence of bilevel algorithms to global solutions is an interesting topic, and this paper offers an approach.
2.	The paper includes concrete application examples that validate the assumptions necessary for establishing global convergence results.

### Weaknesses
I have several concerns and comments on the submission (please correct me if I am wrong):

1. The applicability of the developed theorem seems unclear. The proof closely dependent on and follow existing convergence theorems for PBGD, and it’s unclear whether the analysis could extend to other bilevel algorithms. The non-additivity of PL conditions poses a great challenge for applying the developed theorem and no practical solutions are provided. The two applications studied rely on linear models and strong convexity of loss, which is overly idealized and simplified.

2. Moreover,  in line 228 (Section 3), the authors mention that convergence analysis may need “fine-tuning per application,” but it remains unclear which parts of the analysis are generally hold, such as whether the iteration complexity $𝑂(log⁡(𝜖^{−1}))$ generally holds to other settings that satisfy PL conditions. It also mention that "This may also shed light on a broader range of bilevel problems involving sophisticated neural network architectures in machine learning", but the paper lacks clearly summaries practical takeaways got from the developed theorem for achieving global convergence in such complex applications with modern non-linear deep models.

3. The numerical analysis lacks depth and discussion on robustness. I am suggesting throughly evaluating how values of parameters $\alpha$, $\beta$, $\gamma$ are set theoretically as well as practically, and whether the observed results match theoretical expectations on the convergence rate. Also, exploring how slight violations of PL conditions affect convergence would help clarify the robustness.

4. Section 2 provides an example to illustrate the complexity of the nested objective $𝐹(𝑢)$ caused by the lower-level mapping $𝑆(𝑢)$, but it lacks rigorous analysis of how the constrained formulation reliably produces a more benign landscape and to what extend. A precise definition of benign landscape in the context of bilevel optimization is also helpful. The conclusion that constrained reformulation yields a benign landscape relies heavily on prior literature (lines 211-215) rather than in-depth analysis in this paper.

5. In line 373 (page 7), matrix $𝑊_3$ is introduced without a clear explanation.

### Questions
In Line 1226, why is the blockwise PL condition of $L_\gamma$ over $u$ sufficient to ensure the PL condition for $L^*_\gamma$?

### Soundness
3

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
3

### Summary
This paper presents a theoretical framework for achieving global convergence in bilevel optimization. The authors propose that a constrained reformulation generally yields a benign landscape, and they analyze the global convergence of penalized bilevel gradient descent (PBGD) algorithm for bilevel objectives under the proposed joint and blockwise PL conditions. The paper illustrates that the specific applications of representation learning and data hyper-cleaning can satisfy these PL conditions. Theoretical results are then supported by experiments conducted on these applications.

### Strengths
The main strength is that it is a pioneering work that studies the challenging and important problem of global convergence in bilevel optimization, a topic with substantial real-world relevance. The proposed analysis extends PL to both joint and blockwise PL conditions and verifies them on two application cases. Overall, the paper is well-organized and easy to follow.

### Weaknesses
The paper's proposed conditions for achieving global optimality in bi-level optimization, while theoretically interesting, suffer from significant practical limitations. The joint and blockwise Polyak-Łojasiewicz (PL) conditions are extremely restrictive and unlikely to hold in most real-world bi-level optimization problems. The paper does not adequately address the challenge of verifying these conditions for non-trivial problems. The examples provided, such as linear models in representation learning, are overly simplistic and do not reflect the complexity of typical bi-level optimization scenarios. The assumption that these conditions can be easily satisfied, or even checked, is a major weakness that limits the applicability of the proposed approach. Furthermore, the paper lacks a discussion on how the proposed conditions relate to other existing conditions for bi-level optimization, such as those based on strong convexity or smoothness.

### Questions
1. How should one choose between joint and blockwise PL conditions for a given application?
1. Could you please clarify which aspects of the convergence results would generalize to more complex settings like non-linear models?
1. What practical takeaways does this work provide for achieving global convergence in more complex bilevel applications?
1. How robust are the convergence results if the PL conditions are only approximately met?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores global convergence in bilevel optimization, a crucial yet challenging objective due to the non-convexity and potential for multiple local solutions in bilevel problems. To address this, the authors propose sufficient conditions for global convergence and illustrate these in bilevel learning applications such as representation learning and data hyper-cleaning.

### Strengths
The paper offers conditions that ensure global convergence in bilevel optimization by generalizing the Polyak-Lojasiewicz (PL) condition.

### Weaknesses
While global optimality is underscored as essential, the precise definition or context of “global optimality” within this framework is unclear. A clear explanation of how this term is specifically applied in their method would strengthen the paper.

### Questions
1. Could the authors expand Section 1.1 with detailed theorems? The sentence following C3, “The joint and blockwise PL condition… are not assumptions, but the properties of the penalty reformulation,” is confusing. The authors should clarify the assumptions needed to establish global convergence rigorously.

2. In what specific way is “global optimality” used in the paper?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper proposed two PL conditions, by satisfying which the global optimality of bi-level optimization can be achieved using simple algorithms like Gauss-Seidel.

### Strengths
Achieving Global optimality is an important property.

### Weaknesses
The paper's assumptions are very restrictive. For most bilevel optimization problems, the Joint and blockwise PL conditions cannot be guaranteed, and even checking these conditions can be challenging.  The representative problems illustrated in the paper are very specific simple cases. For example, only linear models can satisfy the assumption for representation learning.

### Questions
Can it be applied to a more general bi-level optimization with constraints in (1)?

### Soundness
4

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
This paper propose a new bilevel optimization algorithm. This paper is generally very well written and provide plenty of theoretical results. Overall this paper is clear a good paper. If all these results are correct, this paper should be clearly accepted (However, I am inadequate to go through all proofs).

### Strengths
good. This paper is overall well written and provide plenty of theoretical results.

The proposed method also solves the neural network cases. That's especially good.

### Weaknesses
1. Experiments are not adequate. 

2. Some fonts seem strange.

### Questions
1. What does the a pilot mean in the title?

2. Line 057, a benign landscape, is there a direct meaning for that?

3. Line 53, the  goal of this paper, this sentence is not important. Do not need to emp{}. 

4. The numerical results seem too little? Does the proposed method outperform SOTA bi-level methods?

5. What are the best convergence results for bi-level optimization method before this paper?

6. line 414, what does \gamma to be O(\epsilon^{-0.5}) mean? If gamma is very very large (with a very large constant), can the algorithm still converge? What is the meaning of O(xx) here?

7. Will PL condition a bit too strong?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the global convergence rate of bilevel optimization. The main result is that if the penalized objective satisfies the PL condition, then the bilevel problem have almost linear global convergence rate if PBGD method is used to solve the problem. Then the authors give two applications: representation learning and data hyper-cleaning. These problems can be formulated as bilevel optimization problems, and their penalized objectives satisfy the PL condition. Thus, when applying PBGD algorithm, they should converge almost linearly. The preliminary computational results also support the theorem.

### Strengths
Clear Problem Statement: The authors articulate the limitations of existing methods, particularly those that only guarantee convergence to local minima or stationary points, which motivate them for pursuing global convergence.

Timeliness and Relevance: The paper proof the global convergent rate for a certain type of bilevel optimization problems. Given the increasing application of bilevel optimization in machine learning and high-stakes fields, this work has substantial relevance.

Theoretical Contribution: The authors provide sufficient conditions for achieving global optimality. By leveraging the penalty reformulation approach, the paper establishes an almost linear global convergent rate for some linear bilevel optimization problems.

Experimental Validation: The empirical results test on bilevel learning problems like representation learning and data hyper-cleaning. The preliminary computational results support the almost linear convergence theorem.

### Weaknesses
Assumptions and Limitations: While the paper claims global convergence for bilevel problems, it focuses primarily on linear models. Expanding the theoretical foundation to nonlinear models or other loss functions would improve the paper’s generalizability.

Comparative Analysis: While the paper mentions other approaches, a direct empirical comparison with state-of-the-art methods for bilevel optimization would strengthen its validation.

Connection between Theory and Experiment: the author should clearly specified the connections between the theory and experiment so that the experimental results can support the theory. For example: in section 6, the author should specific the choice of the step length and make sure that they satisfied the conditions stated in Theorem 2 and 3.

### Questions
1.	Major Concerns:

(a) In line 261, Danskin theorem is mentioned, then the gradient is calculated. Also, the variable $\omega$ is introduced later. I think it would be better to explain the connection and point out that the using Danskin theorem, the auxiliary variable $\omega$ will help us to find a good estimation of the gradient with respect to $u$.

(b) It may be better to put Algorithm 1 and 2 on Page 6 after the authors have summary these algorithms. It will give the readers a smooth reading experience.

(c) In section 6, you may want to specific the choice of $\alpha$ and $\beta$ and make sure that they satisfied the conditions stated in Theorem 2 and 3.

(d) If possible, adding more baseline methods would help readers better understand the convergence rate of the PBGD method. This is not necessary given the limited time.

2.	Minor Concerns:

(a) The sentence in line 199 is not very clear, please double check.

(b) There’s a “?” in line 309, please make sure it is correct.

(c) Misspelling in Line 973 and Line 2189. “invertiable” to “invertible”.

### Soundness
4

### Presentation
3

### Contribution
3
