# Communication-Efficient Heterogeneous Federated Learning with Generalized Heavy-Ball Momentum

- Decision: Reject
- Scores: 6, 3, 6, 6

## Abstract
Federated Learning (FL) has emerged as the state-of-the-art approach for learning from decentralized data in privacy-constrained scenarios.
However, system and statistical challenges hinder real-world applications, which demand efficient learning from edge devices and robustness to heterogeneity.
Despite significant research efforts, existing approaches (i) are not sufficiently robust, (ii) do not perform well in large-scale scenarios, and (iii) are not communication efficient. 
In this work, we propose a novel \textit{Generalized Heavy-Ball Momentum} (\ghb), motivating its principled application to counteract the effects of statistical heterogeneity in FL. Then, we present \fedhbm{} as an adaptive, communication-efficient by-design instance of {\ghb}.
Extensive experimentation on vision and language tasks, in both controlled and realistic large-scale scenarios, provides compelling evidence of substantial and consistent performance gains over the state of the art. \footnote{Code is provided for the review process and will be released upon acceptance}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel Generalized Heavy-Ball Momentum (GHBM) technique for federated optimization with partial participation, enhancing convergence without relying on the bounded heterogeneity assumption. The proposed method is both theoretically and experimentally shown to improve convergence rates. Empirical results across various federated learning benchmarks demonstrate benefits over previous approaches.

### Strengths
1. The paper tackles the important problem of federated learning optimization in heterogeneous settings and under partial participation.

2. The proposed technique builds on the classical momentum mechanism in a straightforward manner, making it promising for practical implementation in federated learning systems.

3. The authors conduct diverse experiments showing the advantages of GHBM (and variations) across multiple realistic computer vision and language tasks.

### Weaknesses
 **W1.** The **literature overview** in Subsection 3.2 omits some recent works, such as ScaffNew [1] and related papers, that achieve accelerated communication complexity in heterogeneous settings through control variates similar to SCAFFOLD. In addtion, there are recent papers on federated optimization [2, 3], which leverage momentum as a local correction term to benefit from second-order similarity (such as MIME and CE-LSGD). The omission of CE-LSGD is particularly concerning, as it provides lower bounds on communication complexity that this work appears to circumvent, yet there is no discussion of this discrepancy.

**W2.** On **presentation and clarity.** Many equation links, particularly those referencing the appendix (e.g., Eq. (122)), are not functional, making the paper cumbersome to follow. 
The symbol $G$ is used without definition in Lemma 4.4.
Referring to notations introduced in the appendix, such as equations (11) and (12), makes understanding Lemma 4.6 challenging without flipping back and forth between sections.

A clear, intuitive explanation of Assumption 4.3 would be beneficial to the reader.

**W3.** The local version (LocalGHBM) may not be well-suited for cross-device settings, as it necessitates storing local states similarly to SCAFFOLD, which has been identified as a limitation by Reddi et al. (2021).

The following work has already been published:

> Konstantin Mishchenko, Eduard Gorbunov, Martin Takác, and Peter Richtárik. Distributed learning with compressed gradient differences, 2019.

### Questions
1. What is actually the problem being tackled in this paper: cross-device or cross-silo?

2. The results in Figure 1 are somewhat counterintuitive, showing higher variation for the “iid” case. Could the authors clarify this observation?

3. The work by Patel et al., (2022) suggested an algorithm CE-LSGD and provided some lower bounds, which seem to be circumvented by this submission. Please explain how is it possible? Please also provide a comparison to that paper.

4. How important is the cyclic participation Assumption 4.3 for achieving the main theoretical contribution of the paper?

5. Do the convergence rates benefit from introducing local steps, as seen in ScaffNew? From equation (122), it seems that the local step size $\eta_l$ must decrease inversely with the number of local steps $J$.

6. How does GHBM interact with server momentum, which has been shown to be essential for achieving good convergence rates?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes new federated learning (FL) algorithm variants—GHBM, LocalGHBM, and FedHBM—which generalize previous momentum-based methods by allowing the momentum term to be computed using multiple past iterations, rather than just the most recent one. The authors theoretically prove that the iterates of GHBM, with access to a stochastic gradient oracle, converge to a first-order stationary point in a mean-squared sense for non-convex functions, even with partial client participation and arbitrary client dissimilarity. Experimentally, they demonstrate that for large neural network training, their methods outperform existing FL approaches, especially in scenarios with high client dissimilarity and low client participation.

### Strengths
The paper advances previous theoretical results that relied on assumptions of bounded client heterogeneity or full client participation. The authors’ method generalizes the Fed-Avg-M approach from Cheng (2024), achieving the same convergence rate without requiring full client participation. Experimental results are compelling, with the proposed methods showing significant improvements over existing methods used for comparison.

### Weaknesses
The main weakness of the paper’s contribution is the similarity to (Cheng 2024). The theoretical novelty is limited as the authors admit the analysis is based on (Cheng 2024). Further, this paper compares against Fed-Avg-M from (Cheng 2024), but makes no mention of the SCAFFOLD-M algorithm from the same paper which has convergence guarantees in the desired setting of unbounded client heterogeneity and partial client participation. SCAFFOLD-M incurs a slightly worse convergence rate but does not require cyclic client participation. The line in the introduction section that reads“existing momentum-based FL methods still theoretically rely on bounded heterogeneity in partial participation…” is thus misleading. The absence of discussion of SCAFFOLD-M in terms of theoretical guarantees and experimental performance is a major weakness, especially since (Cheng 2024) showed that SCAFFOLD-M performed much stronger than Fed-Avg-M under severe client heterogeneity.

Although the experimental results are strong relative to the other methods chosen for comparison, the discussion on why the proposed methods significantly outperform existing methods is unsatisfying. It is mentioned throughout the paper that existing methods perform poorly in the “large-scale” setting and the proposed methods improve in this area, but this difference does not seem to relate to the theoretical convergence results established in the paper.

### Questions
Can you compare your theoretical and experimental results to SCAFFOLD-M? It seems to be the most natural algorithmic competitor to the proposed methods. Also, can you offer an explanation as to why the proposed methods outperform existing methods in the “large-scale” setting especially? This point is made many times but does not seem to be supported by the theoretical discussion. Are the proposed methods just converging faster than other methods, or is there something about using the generalized momentum method that biases the networks to learn better quality solutions?

### Soundness
2

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
1

### Summary
This paper proposes propose a Generalized Heavy-Ball Momentum (GHBM), proving that it enjoys an improved theoretical convergence rate w.r.t. existing FL methods based on classical momentum in partial participation, without relying on bounded data
heterogeneity. This paper also presents FEDHBM as an adaptive, communication-efficient by-design instance of GHBM. Extensive experimentation on vision and language tasks, in both controlled and realistic large-scale scenarios, confirms our theoretical findings, showing that GHBM substantially improves the state of the art, especially in large scale scenarios with high data heterogeneity and low client participation.

### Strengths
1. The authors present a novel formulation of momentum called Generalized Heavy-Ball (GHBM) momentum, which extends the classical heavy-ball (Polyak, 1964), and propose variants that are robust to heterogeneity and communication-efficient by design.
2. The theoretical convergence rate of the proposed GHBM is given for non-convex functions, which extend the previous result of Cheng et al. (2024) of classical momentum, showing that GHBM converges under arbitrary heterogeneity even (and most notably) in partial participation.
3. The authors empirically show that existing FL algorithms suffer severe limitations in extreme non-iid scenarios and real-world settings. In contrast, FEDHBM is extremely robust and achieves higher model quality with significantly faster convergence speeds than other client-drift correction methods.

### Weaknesses
Although this paper is written very clearly, the Assumption 4.3 (Cyclic Participation) is important and should be further discussed in this paper.

### Questions
Although this paper is written very clearly, the Assumption 4.3 (Cyclic Participation) is important and should be further discussed in this paper.

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
4

### Summary
This paper proposes a multistep inertial momentum method in federated learning to alleviate the biases of the partial participation. It provides the theoretical improvements that the proposed method can achieve the full-participation rate under partial-participation. Experiments also shows its efficiency on different setups.

### Strengths
1. The writing is well-done and easy to understand the motivation and design in this paper.

2. The motivation of reducing the gaps caused by partial participation is also a good perspective, which is also a essential academic issue in FL.

### Weaknesses
1. The proposed approach is incremental. The use of momentum averaged over $\tau$ rounds, rather than a single round, was introduced based on experimental intuition. Although a correction scheme was applied both locally and globally, this appears to be a simple extension of the FedCM and FedADC approach [1].

2. The assumption 4.3 is too strong. Periodic participation is feasible, but the disconnect between the experiments and the theory prevents these two parts from supporting each other. Periodic participation implies that the sampling distribution is time-varying and uneven, which simplifies the impact of heterogeneity. The difference between the two is analogous to the theoretical analysis of SGD versus incremental GD. In fact, incremental GD has been proven under certain conditions to surpass the convergence speed of SGD. I believe this is one of the main weaknesses of the paper. The authors mention that under optimal participation rate design, the heterogeneity assumption is unnecessary. In fact, this is one of the theories behind incremental GD eliminating the stochastic biases. This proof does not accurately demonstrate that such properties can be maintained under random selection.

3. Some of the assumptions in the proofs seem to differ. Lemma 4.4 and Corollary 4.5 adopts the heterogeneity assumption but the authors do not claim it clearly. See question (3).

4. Some of the conclusions seem to lack precision. Line 381 comments "since increasing $\tau$ does not increase the overall error due to this term." Does the term $\frac{1}{\tau}\sum_{k=t-\tau+1}^{t}U_{k}$ is proven a constant order? If I missed this proof, please let me know. Currently, there does not seem to be sufficient evidence to indicate the specific nature of this term.

5. The comparisons in Table 1 lack important information. Although Table 1 shows that the proposed method can achieve global participation convergence speed under partial participation, this seems to strictly rely on Assumption 3 and the cyclical setting. I believe it is necessary to clearly state the conditions of this conclusion, rather than allowing readers to mistakenly think that it has surpassed the upper bound of partial participation as it currently stands.  In fact, after reading the entire paper, I believe that with the help of Assumption 3, the theoretical conclusions of FedCM could also reach the same conclusions presented in this paper. Based on the current results, I do not think this theoretical advancement is due to improvements in the algorithm itself.

### Questions
1. What is the meaning of $\alpha$ in Figure.1? And, why is the variacne of the gaps larger on iid than non-iid? In principle, the raw gradients of identically distributed datasets should remain highly similar between local clients, resulting in smaller variance. The author could further elaborate on the experimental process and explain why this conclusion leads to counterintuitive results.

2. I have a question about the form of Equation 3. Why is this considered the desired momentum update? Especially for the term $\widetilde{g}^{k}(\theta^{t-1})$, if the state $\theta^{t-1}$ is fixed, i.e. it is irrelated to $k$, then it seems to be only related to $S^k$. Do authors mean by that under a large $\tau$, the union of $S^k\rightarrow S$? I believe the explanation here is overly simplistic, making the approach appear unreasonable.

3. Eq (8) and (9) adopt the bounded heterogeneity assumption, since there is $G$ terms to show the deminished errors. However, the absence of the $G$ term's influence in the subsequent conclusions. Additionally, are the inferences from Equations (8) and (9) still valid for the later conclusions?

4. Can authors provide the general result of Theorem 4.7? For instance, under any selection on $\tau$ without fixing it as $1/C$. Also, how to recover the $\tau =1$ case? And how does the selection $\tau$ impact the final results?

5. I notice the general rounds are set as $10,000$. What is number of local steps $J$? This seems to be a very exaggerated setup, as the referenced baseline algorithms typically do not exceed 1,000 training rounds on the same task. Though FedCM provides results after 4,000 rounds. Additionally, why Table 3 does not contain the results of FedCM and FedADC, and other methods in Table 2?

6. The selection of $\beta$ seems to be related to $T$ and $J$. So, this term is a parameter that needs to be precisely designed in this algorithm rather than being a constant? Does it imply that different total training lengths $T$ will affect the choice of $\beta$? 

Some typos:
(1) Line 142, $\theta^{t,J_i}$ should be corrected as $\theta_i^{t,J_i}$.

---------------------------------- After rebuttal -----------------------------------------------

I hope the author can include a discussion section in the main text to draw an analogy between the discussion of IGD comparisons and heterogeneity in FL. This will help enhance the paper's impact, as it truly highlights the core source of this technique. Secondly, regarding the author's mention of research on lower bounds, I encourage them to pursue related studies. Research on lower bounds has always been very challenging yet valuable, but it does not need to be included as a contribution in this paper. Finally, I suggest further revising the narrative in the paper to explicitly state the conditions and assumptions for any claimed theoretical advancements to prevent readers from being misled. Regarding the author's statement that other methods cannot achieve certain results due to the lack of guarantees in existing proofs, I understand this writing style—it is sometimes valid. However, in the context of this paper, it is clearly debatable. After all, new assumptions can also be applied to many previous algorithms to derive entirely new conclusions. I have raised my score to 6.

### Soundness
2

### Presentation
3

### Contribution
2
