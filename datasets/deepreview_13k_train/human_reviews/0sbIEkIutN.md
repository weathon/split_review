# From Interpolation to Extrapolation: Complete Length Generalization for Arithmetic Transformers

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Since its introduction, the transformer model has demonstrated outstanding performance across various tasks. However, there are still unresolved issues regarding length generalization, particularly in algorithmic tasks. In this paper, we investigate the inherent capabilities of transformer models in learning arithmetic algorithms, such as addition and multiplication. Through experiments and attention analysis, we identify a number of crucial factors for achieving optimal length generalization. We show that transformer models are able to generalize to long lengths with the help of targeted attention biasing. We then introduce Attention Bias Calibration (ABC), a calibration stage that enables the model to automatically learn the proper attention biases, which we link to mechanisms in relative position encoding. We demonstrate that using ABC, the transformer model can achieve unprecedented \emph{perfect} length generalization on certain arithmetic tasks. \footnote{We will open source our code upon the publication of this paper.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores how transformer models can learn arithmetic algorithms and achieve optimal length generalization. It introduces attention bias calibration (ABC) to guide the model to focus on the right tokens. Using ABC, the Transformer model can perfectly generalize on certain arithmetic tasks. Finally, the paper also makes a connection between ABC and relative position encoding (RPE).

### Strengths
The raised research problem is well-motivated and interesting. The authors show that additional training time is negligible in the paper.

### Weaknesses
1. The writing should be improved in terms of clarity. Several terms and concepts are introduced without adequate definitions or elaboration. Specifically, the terms "complete length generalization" and "the organic Transformer" seem ambiguous. Furthermore, the paper lacks a clear explanation of how the attention bias calibration (ABC) is implemented in practice, making it difficult to reproduce the results. The description of how ABC guides the model to focus on the 'right tokens' is also vague and lacks concrete examples.

2. ABC constructs attention biases based on task-specific data. It's not clear if it can be applied in multi-task learning settings or even serve as a building block for general-purpose language models. The paper does not address the potential limitations of ABC when dealing with more complex tasks that require a combination of different arithmetic operations or logical reasoning. The reliance on task-specific data for bias construction raises concerns about its adaptability to new tasks.

3. More experiments should be conducted. While the results are promising on the four tasks detailed in Sec. 3.1, more extensive experiments are anticipated. It might be worthwhile for the authors to explore tasks in [1,2]. The current set of experiments is limited in scope and does not fully demonstrate the robustness and generalizability of the proposed approach. The paper should include experiments on a wider range of tasks with varying complexities to better evaluate the effectiveness of ABC.

4. Factual errors in the discussion on related works. Sec. 2 mentions that [3] is a follow-up of Alibi. This can’t be true because [3] appears much earlier than Alibi. Sec. 7 mentions that “Interestingly, such clipping is also used in RoPE”. I believe this claim is incorrect and can be misleading.

### Questions
Please see weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies length generalization of Transformer models on algorithmic tasks. It shows that the vanilla Transformer correctly learns the attention patterns up to the training length and fails beyond that. To address this problem, the authors propose Attention Bias Calibration (ABC), which introduce an additional stage to obtain proper attention biases from training data. Experiments show the effectiveness of the proposed approach.

### Strengths
- The experiment results are good on the tasks considered in this paper.
- The authors provide some interesting empirical study and visualization of the attention.

### Weaknesses
 - The presentation of this paper looks good in the first two sections, but the presentation quality drops in the subsequent parts. In particular, section 5 is very hard to read due to the intensive definition and sometimes abuse of notations albeit the idea is very simple. The definitions of some notations are far from where it is used. For example, the authors should have mentioned how $threshold$ is calculated when it appears for the first time – In the paper, it is not defined until section 6, which can confuse the readers.
- The method implicitly encodes sparse attention patterns, since the attention bias $\tilde A_{i,j}$ can be set to $-\infty$ for a large number of tokens. While it can be helpful for simple tasks, I’m not convinced of its effectiveness in more general settings (e.g., for natural language). I'm worried ABC can only be effective for a small number of tasks. The tasks in this paper also seemed to be oversimplified. I'm wondering if ABC can still work well for multi-digit multiplication rather than the simple $N\times 1$.
- ABC is only compared against weak baselines in the experiments. As discussed in the paper, existing papers have shown Alibi and RoPE are suboptimal on algorithmic tasks. The authors should compare ABC against stronger baselines, e.g., Randomized Positional Encodings, RoPE with Position Interpolation, etc. 
- Typos.
  - Footnote 4, “16 etc” $\to$ “16, etc”.
  - Footnote 6, “tasks” $\to$ “tasks.”.

### Questions
- Can ABC still work well for more complex task, e.g., multi-digit multiplication, or even natural language modeling?

- Can you compare ABC with more advanced baselines?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose an analysis of length generalization in sequence to sequence transformers for four arithmetic tasks: successor (adding 1), parity integration, addition, and multiplication by one digit operands.

In a first set of experiments, they observe that on these four operations, length generalization can be achieved if the attention window for the model is constrained to focus on a small number of tokens, either directly, by forcing the window to be of width one, or indirectly, by using small modular integers for positional encoding. On these tasks, such constrained attention models can effectively replace positional encodings. 

Finally, the authors propose a technique for creating such attention constraints for a specific task. To this effect, they average the biases in attention weights when a model, trained to generalize to sequence of the same length, performs the task. Then, they retrain on the specific task, using these biases to constrain attention. Experiment indicate that this allows the model to generalize to longer sequences for three of the four tasks.

### Strengths
The paper focuses on an important limitation of transformers: length generalization. The analysis of the role of the attention window is compelling, and the experimental results from appendix A.5 are quite convincing. 

The calibration technique proposed in section 5 is interesting, and experiments demonstrate its worth on the three tasks considered. 

Overall, the paper provides is a solid analysis of length generalization, and interesting ideas on how to solve it.

### Weaknesses
* The important results from section 4 are hard to understand if one only reads the main paper. In particular, the claim that constrained attention solves parity is only supported in the appendix. Also the logic behind section 5 is hard to comprehend without reading parts of section A.4 (the precise description of windowed attention, and the cyclic encoding). The paper would be made much stronger by moving a significant part of appendices A.4 and A.5 into section 4. This can probably be done at the expense of figure 1 (not very informative), and parts of section 5. 

* The claim that constrained attention, and ABC, offers a **complete** solution to length generalization on problems of arithmetic is exaggerated. All the tasks considered in the paper share a common trait: their solution can be computed by looking at just a few consecutive digits of the problem and the currently computed solution. This would break for such a basic arithmetic task as summing $n$ k-digit integers, and generalizing on larger $n$. As for multiplication, $N\times 1$ multiplication is closer to $10$ unary operation than a binary operation. $N\times N$ multiplication would have the same non local behavior.

* Given the comments in section 7, about the similarity between ABC and RPE, it is regrettable that the experiments in section 4 do not feature RPE (except addition, which corresponds to a different architecture). It would be interesting, in particular, to see how RPE perform on the successor and parity task.

### Questions
* You use 1/6 layer transformers, what is the benefit of a shallow encoder, compared to a (smaller) 6/1 encoder, or 4/4 model?
* All your vanilla models use the cosine positional embeddings. You observe that it sometimes interferes with the sliding window attention, could you try learnable PE? 
* Could you try RPE on the successor and parity experiments? Your conclusions suggest that it would help generalize.
* In the experiments from appendix A.5 (table 3), you try cyclic PE on top of a w=1 windowed attention, what happens if you use it without windowed attention? (it is another form of RPE)
* Have you tried $N\times N$ multiplication (for smaller values of $N$)? of $N\times k$ for $k$ larger than 3 (so that the model cannot memorize all cases as so many unary operations)?
* The Jelassi results in table 3 and figure 1 correspond to a different architecture (encoder-only, with shared layers), it would be better to rerun them, or at least to clarify this.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors achieve perfect length generalization on algorithmic tasks (x+1, x+y, and N x 1). The models are trained with as little as a sequence length of 6, and they generalize to sequences with a length of 5. They achieve this by learning an attention pattern on short sequences which interpolates and extrapolating the attention pattern to long sequences, in the form of an additive bias. This bias is somewhat learned, however it has a very strong structural prior in the form of lines in the attention matrix.

### Strengths
- Perfect length generalization in addition
- Clear presentation
- The method is based on the analysis of the attention patterns
- The paper has a clear scope
- The method clearly shows that the attention pattern is the bottleneck in extrapolating to longer sequences

### Weaknesses
 - The inductive bias is very strong: it biases the attention matrix to be diagonal lines. The method might not work in more general cases in 2 different ways: it might not help with generalization, but it might also hinder learning (I strongly suspect that this would be the case with language-related tasks). Thus, the limitations of the method are not clear. I think this is the biggest weakness of the paper.
- The authors already compare to lot of baselines. However, these relative positional encodings are known to have extrapolation issues. The authors also cite references for this. However, the authors do not cite some relevant work that has been shown to help with extrapolating to longer sequences [1, 2], for example by Transformer-XL style attention [3]. Other work already showed extrapolation on some algorithmic tasks, for example, ListOps and modular arithmetic [4]. Please cite it.
- The method, as presented, is limited to tasks where monotonic attention patterns are sufficient. The experiments with a simplified version of ListOps, where only a single operation is applied to a list, should be solvable with monotonic attention patterns. The fact that the method fails on this simplified version suggests a significant limitation in its applicability, and this should be emphasized more clearly in the paper. This is not a ready-to-go solution for length generalization, and the paper should make this limitation more explicit.

### Questions
- Adding a task where the attention pattern should not be a straight line would be interesting, to see the limitations of the method. One interesting task could be ListOps (for an analysis of attention patterns, see [4] from the "Weaknesses" chapter)
- On page 6, when explaining how the attention matrices are extracted, it is written "are parameter matrices in the last decoder layer". Does this mean that only the last decoder layer has the attention bias? Or do all of them have it, but set to the same as the last layer?
- The absolute PEs are usually not injected in the attention head directly, but to the residual stream immediately after the token embeddings. Given this, in the first eq. on P6, what are the additive p_i and p_j components? Do you do a custom method, where you inject the PE directly into the attention at each layer?
- How do you handle the cross-attention? Does that have this bias as well?
- Have you tried a less aggressive bias, where you don't set the elements to -inf, but to some finite negative number, such that the network has the chance to overcome the bias if it is good for the task? Do you think it would work in this case?

I'm willing to raise my score if my questions about the positioning of the biases are cleared, and if the authors could run their method on any task that does not require strictly monotonic attention (e.g ListOps), regardless of the outcome of the experiment. Just to make it clear what are the limitations.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
