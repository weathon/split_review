# Increasing Both Batch Size and Learning Rate Accelerates Stochastic Gradient Descent

- Decision: Reject
- Scores: 3, 3, 1, 3

## Abstract
\vspace{-1mm}
The performance of mini-batch stochastic gradient descent (SGD) strongly depends on setting the batch size and learning rate to minimize the empirical loss in training the deep neural network.
In this paper, we present theoretical analyses of mini-batch SGD with four schedulers: 
(i) constant batch size and decaying learning rate scheduler,
(ii) increasing batch size and decaying learning rate scheduler,  
(iii) increasing batch size and increasing learning rate scheduler,
and 
(iv) increasing batch size and warm-up decaying learning rate scheduler. 
We show that mini-batch SGD using scheduler (i) does not always minimize the expectation of the full gradient norm of the empirical loss, whereas it does using any of schedulers (ii), (iii), and (iv).   
Furthermore, schedulers (iii) and (iv) accelerate mini-batch SGD. 
The paper also provides numerical results of supporting analyses showing that using scheduler (iii) or (iv) minimizes the full gradient norm of the empirical loss faster than using scheduler (i) or (ii).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a convergence analysis of mini-batch stochastic gradient descent which highlights the interplay of batch size and learning rate schedules. The paper then proceeds to apply this analysis to various combinations of batch size and learning rate schedules.

### Strengths
- The paper is generally well-written.
- The work is adequately positioned in the context of related work.
- The paper explicitly compares various batch size and learning rate schedules, demonstrating and contrasting quite clearly the effect of these choices.

### Weaknesses
1) The main issue I see with the paper is that the convergence analysis is formulated purely in terms of the number of steps $T$, without regard to the cost per step of different batch size schedules. In particular, if my understanding is correct, this pertains to the main conclusion (in the title) that "increasing both batch size and learning rate accelerates stochastic gradient descent". This statement is rather void if acceleration means it requires fewer steps, but each step is (after a certain point) more expensive.
2) I have some reservations about the correctness of the analysis with increasing batch size and learning rate. The learning rate grows exponentially without an upper bound. Irrespective of batch size / stochasticity, this should not lead to convergence. Shouldn't a simple noise-free quadratic $f_i(\theta) = \Vert \theta \Vert^2$ be a counter-example?
3) The bounded noise assumption (Assumption 2.1, A2) is quite strong. In my experience, it can often be weakened to a quadratically bounded noise, such as $\mathbb{V}[\nabla f_\xi ] \leq a + b\Vert \nabla f_\xi\Vert^2$.
4) Minor nitpick: The notation $L_n$ is ambiguous and could be replaced with somethign like $\bar{L}$.

### Questions
I would encourage the authors to respond to the points listed as weaknesses (1) and (2). It is quite possible that I am misunderstanding something here.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a theoretical analysis of different learning rates and batch size schedulers in the case of mini-batch SGD. They theoretically provide a justification for a scheduler that increases the learning rate as it increases the batch size to accelerate convergence of SGD.

### Strengths
There is a wide range of schedulers that are popular in practice. Their effect on the bound from the descent lemma is very clearly presented. The assumptions are clearly stated and the statements are rigorous.

### Weaknesses
I am uncertain whether this paper provides a substantial contribution. From a theoretical perspective, the primary upper bound utilized, Lemma 2.1, is a fairly standard result, which limits the theoretical novelty primarily to a detailed analysis of the \(B_T\) and \(V_T\) terms across different schedulers. While the analysis is rigorous, the bounds derived are relatively coarse, and the results may not provide sufficient novelty. The findings on SGD speed-ups with corresponding schedulers also align with expected outcomes—namely, that increasing batch size accelerates SGD by reducing noise, and increasing the learning rate speeds up convergence. Theorem 3.4, in particular, seems a straightforward combination of these established insights. On the other hand it doesn’t really explain why we need learning rate warm-up and not just start with a high learning rate. Moreover, I am not sure there is a confirmation for the claim in introduction, part (iv): “using mini-batch SGD with increasing batch sizes and decaying learning rates with a warm-up minimizes [..] faster than using a constant learning rate in Case (ii) or increasing learning rates in Case (iii)” - I am not sure this agrees with the results of Section 3.4 or the claims in the abstract. That is, I am not sure some of the claims of the paper are stated consistently.

From a practical and empirical standpoint, I have additional reservations. Specifically, the proposed bound generally does not constitute a tight upper bound on the rate of convergence, and its applicability is limited by certain assumptions. Furthermore, there appears to be insufficient empirical evidence to substantiate the claims regarding the practical effectiveness of schedules that simultaneously increase learning rate and batch size, or increasing batch size with decaying lr with warm-up.

### Questions
I think there needs to be a sufficient increase in theoretical contribution, if possible. Alternatively, or in addition to it, I think the paper requires extensive additional experimentation to support the claims of faster convergence of the proposed scheduler.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper provides a convergence analysis of stochastic gradient descent (SGD) with various learning rates and batch sizes. Some experiments on image classification tasks in deep learning are conducted to verify the theoretical results.

### Strengths
The paper presents a comprehensive analysis of different choices of learning rates and batch sizes for optimizing a nonconvex and smooth objective.

### Weaknesses
1. The theoretical proofs are straightforward extensions of SGD analysis (e.g., Ghadimi and Lan 2013), which have limited technical novelty.

2. There are limited discussions about why some learning rate/batch size choices are preferred in practice, as well as the connection between the theoretical and empirical results. 

2. The main message of this paper about increasing both batch size and learning rate is well-known in the literature (e.g., Goyal et al. 2018), which significantly weakens the contribution of this paper.

3. The experimental results offer limited insight compared with (Goyal et al. 2018).

### Questions
See the weaknesses section.

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
4

### Summary
This paper analyzes the dependence of a SGD convergence upper bound on different scheduling strategies of learning rate and batch size. Specifically, it conveys the summation terms in the upper bound for several popularly used scheduling strategies. Based on these upper bound analysis, it further claims that increasing batch size and learning rate can accelerate the SGD training.

### Strengths
The paper is clearly written. Theoretical proofs seem correct. Most of the currently popular schedulers are analyzed/discussed in the paper.

### Weaknesses
1. The analysis of the paper is quite simple and straightforward. It basically just conveyed the summation over time $T$ (appeared in Lemma 2.1), for several popular scheduling methods. For each of these schedulings, the step size function and batch size function are already well-defined. It is just a matter of elementary level of math to write out these summation or their upper bounds. Therefore, the paper is not technically strong.

2. The analysis and claims are only based on a single upper bound expression (Lemma 2.1). It is unclear how loose the bound is. Note that having a smaller upper bound does not mean having a faster convergence, especially when the bound is very loose.

I am suspicious about the claim of acceleration via an increasing learning rate schedule. Typically, having a constant learning rate with a value that is similar to the largest value of the learning rate scheduling should have a faster convergence than the increasing scheduling. However, the paper claims the opposite. One possibility is that the bound itself is not tight enough to reflect the true trend; another is that the constant absorbed by $O()$ may not be ignored. 

3. It is inappropriate to consider the constant learning rate as a “decaying” learning rate.

4. In Lemma 2.1, the optimal loss $f^* $ should not be equivalent to the average of $f_i^* $. Note that the optimal solution of each individual loss $f_i$ is generally not the same as the optimal solution $\theta^* $. Therefore, $f^* = 1/n \sum f_i^* $ is generally not true.

### Questions
no

### Soundness
2

### Presentation
3

### Contribution
2
