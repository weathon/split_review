# Arithmetic Transformers Can Length-Generalize in Both Operand Length and Count

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 5, 8, 5

## Abstract
\makeatletter\phantomsection\def\@currentlabel{abstract}\makeatother % without this line, the result of backref is "(document)"
Transformers often struggle with \emph{length generalization}, meaning they fail to generalize to sequences longer than those encountered during training.
While arithmetic tasks are commonly used to study length generalization, certain tasks are considered notoriously difficult, e.g., multi-operand addition (requiring generalization over both the number of operands and their lengths) and multiplication (requiring generalization over both operand lengths). 
In this work, we achieve approximately 2--3$\times$ length generalization on both tasks, which is the first such achievement in arithmetic Transformers.
We design task-specific scratchpads enabling the model to focus on a fixed number of tokens per each next-token prediction step, and apply multi-level versions of \emph{Position Coupling}~\citep{cho2024position,mcleish2024transformers} to let Transformers know the right position to attend to.
On the theory side, we prove that a 1-layer Transformer using our method can solve multi-operand addition, up to operand length and operand count that are exponential in embedding dimension.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the problem of length generalization in transformer models over arithmetic operations, particularly over both number of operands and length of operands. They achieve 2-3$\times$ length generalization on both addition and multiplication using task-specific scratchpads and multi-level versions of Position Coupling (Cho et al., McLeish et al.). They also provide a theoretical result for a 1-layer transformer showing that it can solve multi-operand addition up to lengths and counts exponential in the embedding dimension.

### Strengths
1. The paper is well written with well described experiments and intuition.
2. Length generalization is known to be challenging on arithmetic problems with Transformers. The results in this paper are extremely impressive in that they not only achieve length generalization in operand lenght, but also operand count.
3. The authors perform extensive ablations on th effect of zero-padding, trained-lengths and also connect some of their experimental results with their theoretical construction.

### Weaknesses
1. While the problem of length generalization is important, it is mainly relevant in how it applies to more general tasks. However, position  coupling seems to be highly task specific and it is not clear to me how to generalize this idea to non-arithmetic tasks other than very artificial problems. The method relies on carefully crafted positional embeddings that encode both the digit position within an operand and the operand index itself. This explicit encoding, while effective for arithmetic, may not be readily transferable to tasks where the underlying structure is not as clearly defined or where positional relationships are more complex and less hierarchical.
2. The size of the test set seems to be too small for 30 operands of length up to 30. I would like to see if the test accuracy remains roughly the same even when scaling up the test set sizes. With a limited test set, it's possible that the reported performance is an overestimate due to a lack of diversity in the test samples. A larger test set would provide a more robust evaluation of the model's generalization capabilities, especially when extrapolating to unseen lengths and operand counts.
3. The model assumes a singly digit tokenizer. It would be interesting to see if the results extend to more general tokenizers at all. The single-digit tokenizer simplifies the problem by aligning each digit with a single token, but this may not be representative of real-world scenarios where numbers are often represented using multi-digit tokens or subword units. It is unclear if the proposed method would still be effective with a more complex tokenization scheme.
4. The zero-padding to match lengths seems to make the input size explode. If you have n inputs with max length n, then the input length will be $O(n^2)$ even if only one operand is of max length. This quadratic increase in input length could pose a significant computational burden, especially for longer sequences, and may limit the scalability of the approach. It would be beneficial to explore alternative methods for handling variable-length inputs that do not rely on such extensive padding.
5. Do you have any intuition on why 1L8H has particularly bad performance? Shouldn't it be strictly more expressive than the 1L4H construction? The 1L8H model, despite having more attention heads, exhibits worse performance than the 1L4H model. This suggests that simply increasing the number of heads is not sufficient to improve performance, and that other factors, such as the dimension per head or the overall model capacity, may play a more critical role. It is not clear why the increased number of heads does not translate to better performance in this case.
6. In Theorem 4.1, does "solve" mean solve perfectly? Are there any constants in max digits or operands? $2^d$ is a very large number, so this is an extremely impressive result!

### Questions
1. Is the main contribution of the paper over Cho et al., proving length generalization over number of operands and the introduction of multi-level position coupling? I would appreciate this being made more clear.
2. For the comparison in Figure 3, why use NoPE? What about FIRE or Rotary position embeddings? With NoPE, is the model trained for longer durations?
3. Is there a comparison with He et al., and Zhang et al. on multi-level relative PEs?
4. In the data sampling, what is the purpose of the second chunk? Is it so that you ensure that you see every position?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper extends the idea of position coupling to get better generalization for the tasks of addition and multiplication. Position coupling is one of the several methods for leveraging the symmetries of a task, and in this paper, it is used in tandem with scratch-padding, padding the integers, and reversing. The paper instantiates generalization for up to 30 digits for addition with the mentioned techniques, and around 20 digits for multiplication, which is impressive.

### Strengths
1- The paper is well written, with their ideas well articulated in all the sections. By comparing their methods to some of the previous work they have made the reader convinced that their methods are necessary in the given framework (leveraging the structure grounded on APE) to achieve length generalization in arithmetic. 

2- The idea of position coupling is applied to parity to achieve perfect length generalization. 

3- Tri-level position coupling facilitates length generalization on both the first and second operands in multiplication.

### Weaknesses
1- In line 18, the paper claims to offer the first length generalization results for arithmetic tasks. To my knowledge, there are several other works that have argued the same. For instance, [1] has leveraged the same symmetries of addition (In a different framework, and using RPE)  to offer generalization up to 50 digits (for both operands) when trained on samples up to 5 digits. Can you explain the advantages of your work? Authors should have done a better comparison with previous work and stayed truthful about the results. 

2- Scratch-padding has been explored before for the problem of parity as also mentioned in line 179. I'm not convinced that position coupling is the core solution for this problem, since it's been only compared with a NoPE  + scratchpad approach. To me it is clear why such an approach cannot work in a next-word-prediction setting as the generated string in the output relies on the order of the the bits in the input, and  scratch-padding makes the final answer reliant on the previous bits in the output. Therefore, even though the final answer of parity is intrinsically independent of the string order, with this solution it is in fact regarding the order. Position coupling had to be compared with other methods that utilizes positional encoding as well. 

3- The contribution of the paper is pretty limited considering that position coupling is introduced in previous work, and bi-level and tri-level versions are two extensions of that method. Besides, the effectiveness of padding and reversing is already well-known and widely studied. 

4- The scope of the experiments are limited to solely having numbers and in the absence of any text. How does this apply to a broader range when numbers are amongst text? For instance, [1] has tried to address this with training some additional attention heads tailored for arithmetic along with rest of the architecture. Besides, is it true that with your method multiplication and addition require different sets of positional encoding? Please correct me if I'm wrong.

### Questions
Please address the concerns expressed in the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper describes methods allowing decoder-only transformers to generalize to longer operands when performing integer addition or multiplication, and to generalize to a larger number of operands when performing addition.

The authors mix two existing techniques, scratchpad, which forces the model to output a sequence of intermediary steps before producing the result, and position coupling, problem-specific hierarchical positional encodings. They experiment with three tasks. 

For parity calculation over bit strings, they use a scratchpad which computes parity integration, ie force the transformer to compute the parities of successive prefixes, and use the same (absolute) positional encoding in the input and output sequences. 

For addition of $n$ positive integers, they use a scratch pad of partial sums (0, first operand, sum of the first two...) and two positional encodings: one for the position of digits in each operand and output, and one for the position of each operand and output in the operation and scratchpad.

For multiplication of 2 position integers, they use a scratchpad of single digit products and partial sums, and three positional encodings, which reflect the different subtasks in multi-digit multiplication.

Experimental results indicate that such techniques allow for generalization to longer lengths on all three tasks, and a larger number of operands for addition.

### Strengths
The paper studies an important limitation of arithmetic transformers, their inability to scale to longer sequences that those seen at training. The authors propose a solution to this problem.

The paper is clearly written, the methods is clearly described and the experimental results are compelling. Some ablation results are provided.

### Weaknesses
The authors seem to only focus on positive integers. This greatly reduces the practical interest of the findings, since integer arithmetic usually involve positive and negative numbers. Could the results be extended to relative numbers, either by adding a sign in the number representation, or changing the tokenization scheme to a number system that encode negative numbers as well (e.g. encoding them in base -10 instead of base 10, or using balanced base 10, with digits -4, -3, -2, -1, 0, 1, 2, 3, 4, 5)? Since the only change is the tokenizer, this could work out of the box. (besides, arithmetic might be easier to learn in balanced base, because the addition and multiplication tables feature less carries).

The paper makes heavy use of techniques introduced in prior work, this is not a problem, but it would be fitting to have a proper "related work" section in the main, describing these methods and acknowledging anteriority. At present, these descriptions are scattered in sections 1 and 2. This could be done at the expense of the preliminaries section (sec. 2, which serves little purpose), and perhaps some of the parity results, which are underwhelming, compared to the rest of the experiments.

Both the scratchpad structure and the position encodings proposed in this paper are strongly dependent on the task. This suggests that the model can be trained to perform one operation (addition OR multiplication), but not calculations featuring both. This is a strong limitation. Have you experimented with such tasks (add and multiply)? Can they be learned zero or few shots? A discussion of these questions would be useful.

### Questions
* At test time, for a model prediction to be correct, you insist on both the output and the scratchpad to be correctly predicted. Prior work suggests that models sometimes learn despite incorrect scratchpads. Have you tested models by judging them on the final result only? (this could have an impact ablation results, and comparisons with other approaches)
* Is reversing the order of digits in the scratchpad and output sequence really necessary? Can you provide ablations for this? 
* What would be the impact of reversing the digits in the input sequence? 
* Your architecture ablations suggest that shallow models can learn and length generalize. Unfortunately, they all use a large embedding dimension (512), which translates into a large number of parameters. Have you tried models with smaller dimensions (128, 64 even)?
* In figure 10, you report better performance of 2 layer models than 4 or 6 layer models with 2 and 4 heads, and better performance of 4 layer models than 6 layer models with 8 heads. Could this be due to the size of your training sample (500k may be on the low side for the larger architectures), or the number of steps you allow? 
* An ablation on the training set size would be useful.
* For addition, what is the point of adding 0 and a copy of the first operand in the scratchpad? 
* The main text claims the model has 63M parameters, the appendix claims 25M, which is right?
* Would this approach benefit from an encoder-decoder model? (intuitively, bidirectional attention over the input sequence should help, all the more as the digits in input sequences are not reversed)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, arithmetic transformers refer to transformers trained on arithmetic tasks.  The core idea of the paper is to combine position coupling and scratchpad, and the authors demonstrate that this allows for length extrapolation in arithmetic tasks.

### Strengths
They show that by using a specific position embedding encoding (tri-level position coupling), they are able to also perform well on multiplication. This is an interesting observation for multiplication that when baked into the ‘structure’ of the transformer can give generalisation on arithmetic.

### Weaknesses
My first slightly minor nitpick is that the scratchpad requires scratchpad data generated in that particular format, for the multiplication specific task. In a general pretraining or fine-tuning setting, this could probably be added in as additional data to shape the model’s behaviour.
However, the specificity of position coupling (for all variants of position coupling) means that it can’t be a general modification to standard Transformers in a pretraining setting, and have it improve arithmetic capabilities. To their credit, the authors have already addressed this in the Limitations section of the paper.

### Questions
- Is there a way for the position coupling to be done “automatically” that you know of? I am unfamiliar with this specific line of work. 
- For PARITY, at least, I have seen a prompt construction that asks the model to number the bit that the model has generated as it generates the internal state (odd or even) given the prefix. 
  For example, given the sequence 1101. 
  ```
    1. 1 odd
    2. 1 even
    3. 0 even
    4. 1 odd

    Final answer: odd.
  ````
  The intuition here being that the numbering allows the attention mechanism to more accurately pin-point the required informaton, which has a similar flavour to your approach.
  I was wondering if you have attempted to prompt a model so that it generates the same positioning scheme (just in human readable form), and I wonder if that will improve multiplication generalisation.

### Soundness
3

### Presentation
4

### Contribution
2
