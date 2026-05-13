# L3Ms — Lagrange Large Language Models

- Decision: Accept
- Scores: 6, 5, 6, 5

## Abstract
Supervised fine-tuning (SFT) and alignment of large language models (LLMs) are key steps in providing a good user experience. However, the concept of an appropriate alignment is inherently application-dependent, and current methods often rely on heuristic choices to drive the optimization. In this work, we formulate SFT and alignment as a constrained optimization problem, where the LLM is trained on a task while being required to meet application-specific requirements, without resorting to heuristics. To solve this, we propose Lagrange Large Language Models (L3Ms), which employ logarithmic barriers to enforce the constraints. This approach allows for the customization of L3Ms across diverse applications while avoiding heuristic-driven processes. We demonstrate experimentally the versatility and efficacy of L3Ms in achieving tailored alignments for various applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Lagrange large language models (L3Ms), which formulate supervised fine-tuning and alignment of large language models as a constrained optimization problem. L3Ms use logarithmic barriers to enforce constraints, allowing for customization across diverse applications without relying on heuristics. The paper demonstrates the versatility and efficacy of L3Ms in achieving tailored alignments.

### Strengths
The formulation of SFT and alignment as a constrained optimization problem and the use of logarithmic barriers in L3Ms is a novel approach that has the potential to improve the customization of LLMs for different applications.

The paper provides a solid theoretical foundation for the proposed method, including discussions on constraint types, Lagrange multipliers, and the connection to the KKT conditions.

The experimental results on length-constrained L3Ms and helpful and harmless (HH) L3Ms show that the proposed method can effectively customize LLMs according to different constraints while maintaining performance on the original task.

### Weaknesses
The experiments mainly consider length constraints and helpful and harmless preferences. It would be interesting to see how the proposed method performs on a more diverse set of tasks, such as computational and reasoning tasks, and whether it can optimize for task-related metrics specific to those tasks.

The paper primarily focuses on perplexity as an evaluation metric. It would be beneficial to include other metrics to provide a more comprehensive assessment of the performance of L3Ms.Are there any plans to incorporate other evaluation metrics in addition to perplexity to better evaluate the performance of L3Ms? If so, which metrics are being considered and why?
Will the authors explore the application of L3Ms to a wider range of tasks, such as computational and reasoning tasks? How would the method be adapted to optimize for task-related metrics specific to these tasks?

### Questions
-Are there any plans to incorporate other evaluation metrics in addition to perplexity to better evaluate the performance of L3Ms?

-Will the authors explore the application of L3Ms to a wider range of tasks, such as computational and reasoning tasks? How would the method be adapted to optimize for task-related metrics specific to these tasks?

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
3

### Summary
This paper presents a novel approach to the supervised fine-tuning (SFT) and alignment of large language models (LLMs), formulating it as a constrained optimization problem. The authors propose Lagrange large language models (L3Ms), which use logarithmic barriers to enforce application-specific requirements, eliminating the need for heuristic-driven processes. This approach allows for the customization of L3Ms across diverse applications. The paper demonstrates the versatility and efficacy of L3Ms through experimental results, showing their ability to achieve tailored alignments for various applications. This work contributes a new perspective and methodology to the fine-tuning and alignment of LLMs, enhancing their adaptability and effectiveness across different applications.

### Strengths
1. The paper innovatively formulates SFT and alignment as a constrained optimization problem, offering a fresh perspective that avoids traditional heuristic methods.
2. L3Ms, with their logarithmic barriers, demonstrate technical excellence and adaptability across diverse applications, ensuring robust performance.
3. By providing a systematic approach to fine-tuning LLMs, this research addresses a critical need and offers practical benefits for both academic and industrial use.

### Weaknesses
1. The paper's experimental section may lack comprehensive evaluations, which could limit the full demonstration of L3Ms' capabilities and robustness across a wide range of scenarios.
2. The choice of datasets used in the experiments appears to be restricted, potentially affecting the generalizability of the findings and the ability to assess the method's effectiveness on varied data types.
3. Utilizing LLMs with only 7 billion parameters might restrict the scalability and performance of L3Ms, as larger models are often necessary for handling complex tasks and achieving state-of-the-art results.
4. Writing Issues: The paper has some writing issues, including incorrect formula numbering, which can cause confusion and disrupt the flow of the paper. Improving the clarity and accuracy of the writing would enhance the overall quality and readability of the paper.

### Questions
See the above weaknesses.

### Soundness
3

### Presentation
2

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
This work introduces a new method for fine-tuning and aligning large language models (LLMs) by treating these processes as a constrained optimization problem. Instead of relying on heuristic methods, the authors propose using Lagrange Large Language Models (L3Ms) that incorporate constraints directly into the optimization through logarithmic barriers. This approach allows models to maintain performance on primary tasks while being customized to meet specific user or application-related preferences. The paper provides experimental evidence showing that L3Ms are effective.

### Strengths
- Clear problem statement. This work discusses the shortcomings of previous works on constrained RLHF and proposes corresponding improvements to solve it, which seems convincing to me.
- Good optimization problem conversion. I find it quite interesting and instructive how this work converts a general target of balancing task performance and multiple specific requirements into a solvable object function of Lagrangian and introduces the necessary components of the logarithmic barrier to make it practically work.

### Weaknesses
 - My main concern is with the experimental results in Figure 3, where MM appears to achieve a better performance frontier than L3M. Although L3M results in lower perplexity (PPL), it's unclear how significantly this affects real task performance, as the improvement seems marginal. Could the authors provide further discussion on this?
- The constraints used in the experiments are somewhat limited in terms of variety. It's unclear how the proposed algorithms would perform in scenarios with more complex or demanding constraints.
- The experimental setups seem relatively simple, which may not fully capture the real-world performance of the fine-tuned LLMs.

### Questions
- Can authors provided more discussions on computation overheads introduced in this work in comparison to the general SFT and other related works (https://openreview.net/forum?id=TyFrPOKYXw, https://openreview.net/forum?id=gkfUvn0fLU).

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper suggests to model SFT and alignment into one constrained optimization problem and proposes a method called L3M, which is to optimize such constrained optimization problems via approximate Lagrangian.

### Strengths
- The paper suggests to formulate SFT and alignment into one constrained optimization problem and optimize its approximate Lagrangian.

### Weaknesses
 - The core objective Eq.(10) $\mathcal{G} _ \mu(\theta)=L(\theta)+\frac{1}{k}\sum _ {i=1}^k\mathcal{B} _ {\mu,\mu^2}(C _ i(\theta))$ is equivalent to the lowerbound of multi-objective RLHF objective with induced reward models and a SFT term. Given a reward model $r _ i(x,y)$, a monotonically increasing function $f _ 1(x)=\mathcal{B} _ {\mu,\mu^2}(x)$, and a monotonically decreasing function $f _ 2(x)=b _ i-x$, we can induce a new reward model $r _ i'(x,y)=-f _ 1(f _ 2(r(x,y)))=-\mathcal{B} _ {\mu,\mu^2}(b _ i-r _ i(x,y))$. As $\mathcal{B} _ {\mu,\mu^2}(x)$ is convex,
$$
\begin{split}
\min &\mathbb{E} _ {x,y}[-r _ i'(x,y)]\\
=&\mathbb{E} _ {x,y}[\mathcal{B} _ {\mu,\mu^2}(b _ i-r(x,y))] \\
\geq&\mathcal{B} _ {\mu,\mu^2}(\mathbb{E} _ {x,y}[b _ i-r(x,y)])\\
=&\mathcal{B} _ {\mu,\mu^2}(C _ i(\theta)),
\end{split}
$$
where the inequality holds by jensen’s inequality. It can be extend into multi-objective scenario with a SFT term $L(\theta)$:
$$
\begin{split}
\min &L(\theta)+\mathbb{E} _ {x,y}\left[\frac{1}{k}\sum _ {i=1}^k-r _ i'(x,y)\right]\\\n=&L(\theta)+\frac{1}{k}\sum _ {i=1}^k\mathbb{E} _ {x,y}[-r _ i'(x,y)]\\
\geq&L(\theta)+\frac{1}{k}\sum _ {i=1}^k\mathcal{B} _ {\mu,\mu^2}(C _ i(\theta))=\mathcal{G} _ \mu(\theta),
\end{split}
$$
which is Eq.(10) of the paper.

 - For baselines, as Line 355-358 writed: “L3Ms have the same time complexity as traditional approaches as we combine the SFT and alignment stages into one”. Traditional SFT+alignment, having the same training budget with L3M, should be considered as a baseline.

 - For benchmarks, more instruction following tasks should be evaluated to demonstrate the generalization of L3M across diverse distribution.

 - For evaluations, 1) ppl (perplexity) can not directly reflect the instruction following ability of an aligned LM. 2) As reward hacking is a considerable problem in RLHF, the score of reward models which are involved into L3M training is not a valid metric. Other metrics should be considered to evaluate the alignment.

### Questions
- Why the log barrier parameter $\mu$ should be decayed during training? (Lines 715-716) 

- As the log barrier parameter $\mu$ is a hyper-parameter of L3M, what the relationship between its value and L3M performance?

### Soundness
3

### Presentation
2

### Contribution
2
