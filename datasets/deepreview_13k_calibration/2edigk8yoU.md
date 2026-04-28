# Looped Transformers for Length Generalization

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Recent work has shown that Transformers trained from scratch can successfully solve various arithmetic and algorithmic tasks, such as adding numbers and computing parity. While these Transformers generalize well on unseen inputs of the same length, they struggle with length generalization, i.e., handling inputs of unseen lengths. In this work, we demonstrate that looped Transformers with an \emph{adaptive number of steps} significantly improve length generalization. We focus on tasks with a known iterative solution, involving multiple iterations of a RASP-L operation—a length-generalizable operation that can be expressed by a finite-sized Transformer. We train looped Transformers using our proposed learning algorithm and observe that they learn highly length-generalizable solutions for various tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- This work studies the efficacy of Looped Transformers for Length Generalization of several algorithmic tasks whose computation complexity is known (as a function of the query length).
- The paper proposes the definition of $n$-RASP-L, a generalization of the RASP-L computation model allowing the loop of RASP-L programs. It is shown, under a general framework called full-answer prediction (FAP), that some tasks (Copying binary sequence (allowing duplicates), Parity, and Binary Addition) have their own $n$-RASP-L program with a linear number of steps in problem length.
- The authors propose training Looped Transformers (with input injection and curriculum learning) to learn $n$-RASP-L-programmable tasks, where the ground-truth number of steps is known for each task during training. They also propose two variants of inference methods: either we retain the knowledge about the number of steps at inference time (*Oracle*), or we adaptively decide the number of iterations based on the confidence of FAP (*Maximum confidence*).
- The proposed method is tested on several algorithmic tasks.

### Strengths
S1. The paper is written and organized well. Overall, the presentation of the methodology and empirical results is clear and easy to follow.

S2. The idea behind the proposed method is neat and plausible. It is natural to think about adaptively scaling the depth of the model according to the problem length or the problem complexity. This paper successfully implements this idea to solve various interesting algorithmic tasks with the power of Looped Transformers. Also, $n$-RASP-L is an interesting but intuitive generalization of the RASP-L framework by allowing the loops. 

S3. The proposed answer-generation framework called FAP is also an interesting component of this work. It might be of separate interest to study.

S4. The paper presents extensive ablation studies on several components of the proposed method. Also, the empirical results (length generalization performances) are impressive enough to convince the readers about the proposed method’s efficacy.

### Weaknesses
W1. The definition of $n$-RASP-L (Definition 3.1) can be improved.

- I think the equation “$T(n): \mathbb{N} \rightarrow \mathbb{N}$” should be corrected to “$T: \mathbb{N} \rightarrow \mathbb{N}$” because $T$ (instead of $T(n)$) is a function of input length $n$ representing the number of steps inside a task-solving $n$-RASP-L program.
- In (2), I guess $P’$ should be a RASP-L program, which is unspecified in the definition.
- Should $P$ be decomposed to a sequential application of $P’$, i.e., $P = (P’)^{T(n)}$? I don’t think this is exactly true because there are pre-/post-processing parts inside the proposed $n$-RASP-L programs (in Appendix A). Can the same RASP-L program $P’$ handle such parts? (It might be true because of the experimental results, but I cannot fully understand this part.) If not, I guess the definition should be modified to include the pre-/post-processing parts. For example, $P = P_{\tt pre} \circ (P’)^{T(n)} \circ P_{\tt post}$.

**W2. “Ground truth” number of steps?**

- According to Definition 3.1, a program $P$ suffices to be an $n$-RASP-L if a corresponding $T(n)$ exists. Indeed, Propositions 3.2, 3.3, and 3.4 claim and prove the existence of $T(n)$ for the Parity, Copy (with duplicates), and Binary Addition tasks, respectively.
- My question is about the uniqueness or optimality of such $T(n)$’s. There might be a clever way to construct another RASP-L program $\tilde{P}$ so that $P$ can be implemented with $\tilde{T}(n)$ steps of applying $\tilde{P}$, where $\tilde{T}(n)$ is much smaller than the previously known $T(n)$ (e.g., $\tilde{T}(n) \in o(T(n))$). It may happen since there is no uniqueness guarantee or lower bound result on $T(n)$.
    - If I venture a guess, I would say it might be possible to implement an $O(\log n)$-step $n$-RASP-L solution for the Parity task by using the parallelism of the transformer architecture. Please correct me if I am wrong. Also, I understand if it is impossible to show whether this bold guess is true. If you are interested, there are some (probably) useful references about logarithmic-depth transformers [1,2].
- However, the authors keep using the phrase “ground truth number of steps” throughout the paper, which may lead to misunderstanding that the only way to implement the given $n$-RASP-L program is by using a loop of length $T(n)$.
- If two different $T(n)$’s can be applied to a single $n$-RASP-L-programmable task, it might be interesting to observe whether the model’s performance changes depending on the choice of $T(n)$.
- Furthermore, if multiple choices of $T(n)$’s exist for a given task, does knowing only one of them suffice to train reasonably performant Looped Transformers? If we know more than one, how should we choose $T(n)$ when we train the model?

**W3. Shouldn’t we consider the input injection when implementing an $n$-RASP-L program for the given task?**

- The input injection seems to be an important component of their experiments. Since it changes the input vectors of each layer, I guess the task-solving algorithm under input injection might be different from that without it.
- However, I can’t see that the $n$-RASP-L programs provided in Appendix A reflect the input injection. As I inspect inside the loop of each program, every iteration only reuses the calculation(s) from the previous iteration right before the current one.
- Shouldn’t we consider the very first input sequence and the result from the previous iteration when implementing the loops? Or is it a valid implementation of input injection? Getting even further, Is there any way to embed the input injection into the $n$-RASP-L programs?

**W4. The proposed training method requires prior knowledge of the task’s structure.**

- The proposed method is limited in that it requires a prior understanding of the structure (e.g., $T(n)$) of the task where we want to train a model. This is because it hinders fully end-to-end training.
- Are Looped Transformers still useful for achieving length generalization even when we don’t (or cannot) know the exact expression of $T(n)$?
- Besides, it seems that the depth of the decoder block is determined based on the complexity/difficulty of the subroutine $P’$ at each step inside the loop (Appendix F). How are they actually chosen? Or, how should we decide the size of the repeating decoder block?

**W5. Some experimental details seem missing or wrong.**

- I guess Equation (2) has a typo: shouldn’t it be arg-main instead of arg-max?
- In Binary Addition, it seems that $T$ is chosen to be $n$ (the length of each operand). However, Proposition 3.4 claims that $T(n)=n+1$ for the same task. Why is there a discrepancy between theory and experiment?
- In Binary Multiplication, I guess some words are used in a wrong way. In Lines 417-418, I think it should be: “We define the problem length to be the **length** of the second **number**, and set $T$ to be the product of the lengths of two **numbers**.”
- In Section 6.1.2, are input injections also applied to NTP-based methods? Also, I’m not sure why it is fair to compare their method (based on FAP) to NTP methods with the architectural setting “…with a depth 20 times the depth of the looped block” because such depth might be suboptimal for NTP-based methods.
- Although the paper indirectly showcases that their adaptive decision of the number of steps works quite well via Figure 5, it would be better to display similar performance plots to Figure 4 (plots based on the “Oracle” inference) but using the adaptive confidence-based method instead, at least in their appendix.

**W6. Minor writing issues**

- Section 4.1, fourth bullet point: I guess $T(n) \in \{T(1), \ldots, T(n_{\rm max})\}$ is correct ($T(1)$ instead of $1$).
- Equations (1) and (2) have several weird-looking brackets (too many open brackets etc.)
- Line 510: Use *less* abbreviations like “w.r.t.”

### Questions
**Q1. Question on the visualization in Figure 3**

- Why don’t the illustrations in the figure contain any “#” (EOS) tokens? Is it due to the pre-processing?

**Q2. Do the trained Looped Transformers simulate the $n$-RASP-L program?**

- Although it might be difficult to reverse-engineer a trained transformer model to figure out what algorithm it actually simulates or implements, it might be interesting if we can observe any kind of similarity between it and the $n$-RASP-L program.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the length generalization problem of Transformer models, which refers to the inability of the model to deal with longer samples than encountered during the training phase. While recent literature has focused on modifying the positional embeddings and the input formats, this paper proposes to use Looped Transformers, which can dynamically adjust their computation steps according to the problem length. The authors define n-RASP-L problems to figure out which problems can be solved by Looped Transformers. Then, they train the models on these tasks (parity, copy, binary addition, binary sum, binary multiplication, unique set) under a full-answer prediction setup. Empirically, the trained models could successfully length-generalize to longer lengths by appropriately adapting the number of loops at inference time.

### Strengths
- The paper is well-structured and clearly written.
- The introduction of Looped Transformers is well-motivated and effectively argued.
- The results are strong and solid. They do not require the use of a scratchpad. Also, the prediction is conducted using an end-to-end, full-answer prediction setup, which is a more general way than the conventional next-token prediction setup.
- The paper clearly illustrates that the model can determine the number of steps to take on its own and does not require T(n) in the test time.

### Weaknesses
Weakness 1: Applicability Limited to n-RASP-L Tasks

- The approach is limited to tasks that belong to n-RASP-L categories, as it requires the ground-truth number of steps in the training data.

Weakness 2: Insufficient Experimentation.

- ***Effect of Curriculum Learning.*** How does the model perform without curriculum learning? Is the use of curriculum learning necessary?

- ***Tolerance to Step Counts.*** I am curious whether this method will still perform well with different choices of T(n). For example, for tasks like parity, would the model maintain its performance if T(n) were set to n+1 rather than n? What about 2n instead of n? This question stems from the possibility that there might be more efficient solutions to n-RASP-L problems than human-designed ones, which could work with fewer steps. Testing whether the model is robust under overestimated T(n) values could help verify the robustness of this approach.

- Overall, the paper requires more ablation studies.

### Questions
Q1. In Figure 5, why do some tasks perform well even when exceeding the step count, while others degrade immediately? For instance, the performance of the parity task and the binary sum task immediately drops when executed with additional steps, whereas the addition, multiplication, and copy tasks retain accuracy to some extent.
- Particularly for the copy task, the selected step count is significantly higher than the actual number of steps required, which seems unusual to me.

Q2. Are there any tasks whose T(n) is nonlinear (e.g. sqrt(n), n^2) to the length of the input sequence? It would be interesting to see experimental results for such tasks.

Q3. Why is the output reversed for binary multiplication (but not for binary addition)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper examines how looped transformers perform in terms of length generalization. The focus is on n-RASP-L problems, which are problems that can be tackled using a loop of a single RASP-L program. The concept is that Transformers can learn steps that are independent of length, employing a flexible number of iterations in the looped transformer to achieve length generalization. The authors first demonstrate that n-digit addition, n-bit parity, and copying n symbols can be addressed with n-RASP-L solutions. They then reveal that when utilizing the looped transformer with adaptive stopping time, the results exhibit significantly stronger length generalization compared to next token prediction (NTP) and other methods like using pause tokens or NTP-loop with a fixed stopping time.

### Strengths
Overall, I really liked the paper, I think that using a looped transformer to achieve length generalization is an interesting idea that was not studied in the past to my knowledge. This paper complements all the other techniques (universal transformers, different types of position emebedding, etc.) that were used in the past for length generalization The paper is well-written and well-explained. This is why I advocate for acceptance of this paper.

### Weaknesses
I would like to raise the following weaknesses/questions regarding this paper:

- **Lack of other baselines**: What would happen if you have a very deep universal transformer? Universal transformers also have shared parameters and looks equivalent to the loop transformer. The depth may play the role of the number of loops. Would this be equivalent to the fixed loop NTP? It would be interesting to run the same experiments with a universal transformer. Specifically, it's unclear how the performance of the proposed looped transformer compares to a standard Universal Transformer with a comparable number of parameters and computational cost, especially when the Universal Transformer is allowed to have a large number of layers. The paper should explore this comparison more thoroughly, as the depth of the Universal Transformer might capture similar iterative behavior.

- **Comparison with other methods**: Where would you position the looped transformers in the list of all the tricks for length generalization? Are the effects similar or complementary to change of the input (index hinting, reverse order of operands, etc.) ? Changes of positional encoding? Chain of Thought? It would be interesting to understand this by making combinations of the tricks with looped transformers with other tricks and analyze the performance differences. The paper does not adequately explore how the proposed method interacts with other known techniques for length generalization. For example, it would be valuable to see if combining the looped transformer with input manipulations like index hinting or reversing the input sequence further improves performance. Similarly, the interaction with different positional encoding schemes and chain-of-thought prompting should be investigated to understand the method's complementarity with these techniques.

-  What is the depth of the encoder block in the loop transformer? I think this information is important to put in the main paper. 

- **Adaptive inference time**: I think one weak point of the method is actually coming up with an adaptive inference time. The methods that are proposed are nice but may look a bit hacky. Do you think one could learn this adaptive inference time?

- In Figure 2, which adaptive inference time method is used for FAP-Loop-Adaptive?

- Lastly, this is a wild question: have you tried your method on problems where there is no n-RASP-L solutions?  Would it still work better than just doing NTP?

### Questions
I listed my questions in the weaknesses section.

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
Empirically explores the ability of looped Transformers, i.e. Transformers that repeatedly apply the same block of layers, to length-generalize on several algorithmic tasks, including copy, parity, and addition. First, the authors manually derive length-generalizing solutions to the considered tasks through a variant of the RASP language, which they term n-RASP-L. Then, based on these ground truth solutions, they show that looped Transformers length-generalize well when trained with access to the true number of steps required to compute the output for a given input.

### Strengths
1. The paper is mostly well-written and easy to follow.

2. Demonstrates that, given knowledge of the number of steps required to perform a given task, a certain looped Transformer, which jointly predicts the full output sequence, tends to learn a length-generalizing solution. The length-generalizing capabilities of this looped Transformer are shown to surpass baselines that use next-token prediction.

### Weaknesses
1. The main weakness of the current paper is that the significance of the results is somewhat limited. In particular, I find that it falls somewhere in between works that are practically relevant and those that may not be practically relevant, but improve our understanding of certain phenomena. On the one hand, this work shows empirically that, in some algorithmic tasks for which we already know how to write explicitly a length-generalizing solution (in terms of looped Transformer weights), looped Transformers generalize well to longer lengths, if they have access during training to the number of steps required for solving the task for a given input. Consequently, the practical relevance is limited since the proposed method requires that we already know how to manually write a length-generalizing solution, in which case there is arguably no point in learning. On the other hand, this work does not provide much in terms of understanding why or how looped Transformers are able to length-generalize.

    Note that one may consider the demonstration of such length generalization to be possible as a main contribution. Yet, the ability to extrapolate through recurrence of layers has been demonstrated in the past, albeit for other architectures (see Bansal et al. 2022 [1], which notably do not require knowing the ground truth number of steps in training).

2. A related issue is the usage of ground truth stopping time during inference. The quantities reported in Figure 5 seem to be for a single training example, yet it is not entirely clear. If so, then how does the maximum confidence stopping criterion fair across the dataset? It would be useful to report results similar to those of Figure 4 but when using the proposed stopping criterion as opposed to the ground truth stopping time, which should be unknown.

Overall, my assessment of the paper tends towards the positive side, yet it is not a clear accept due to the substantial limitations mentioned above. Specifically, the significance of the contributions can be greatly improved if it would be possible to remove the dependence on knowing the ground truth number of steps required to solve the task for a given input during training (and by how it seems from the current results, during test time as well).


Additional (more minor) comments:
- In Definition 3.1, it seems that the intention is for $P’$ to be some RASP-L program, as opposed to just a program. Otherwise, trivially any program $P$ is an n-RASP-L program by choosing $P’ = P$ and $T(n) = 1$.
- In Equation (2), I believe that the criterion should be an argmin over the cross entropy loss instead of an argmax.

### Questions
1. Are the quantities reported in Figure 5 indeed for a single training example? When using the maximum confidence criterion, how do the results compare to the ones reported in Figure 4 with access to the ground truth number of steps?

2. In Bansal et al. 2022, they avoid the need for knowing the exact number of steps during training and inference. Have you tried using similar heuristics?

### Soundness
4

### Presentation
3

### Contribution
2
