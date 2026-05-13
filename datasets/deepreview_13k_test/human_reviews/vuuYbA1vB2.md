# Enhancing Mathematical Reasoning in Language Models Through Focused Differentiation Training

- Decision: Reject
- Scores: 3, 5, 3, 8

## Abstract
Enhancing the mathematical capabilities of large language models (LLMs) is crucial for applications requiring precise and rigorous mathematical reasoning. Current models, even when trained with methods like Direct Preference Optimization (DPO), often struggle to effectively differentiate between correct and erroneous mathematical responses, especially when errors occur in multi-step solutions. Traditional approaches focusing on token or logit-level analysis fail to capture the nuanced semantic differences in mathematical reasoning. To address this challenge, we propose leveraging the rich semantic information embedded in the hidden state space of LLMs. Our novel approach, Focused Differentiation Training (FDT), fine-tunes the model by emphasizing the differences between the hidden states of correct and incorrect responses, rather than their common features. Unlike other methods that detect errors at the token or logits level and often rely on human input or more powerful models, our approach enhances mathematical reasoning capabilities using only the model's inherent abilities. This methodology promotes a more accurate alignment with mathematical correctness, thereby improving the model's ability to evaluate and generate precise mathematical responses. Experimental results demonstrate that our algorithm substantially outperforms traditional alignment methods in mathematical tasks, offering a robust solution for enhancing the mathematical reasoning capabilities of language models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a tweak to DPO-style post-training for large language models. In particular, their technique can be applied when a dataset of paired examples $(x, y_w, y_l)$ is available (where $y_w$ is a preferred completion and $y_l$ is a dispreferred completion). The proposal is to modify the gradient update for the last-layer weight matrix. The usual gradient update for the last-layer weight matrix is a function of the last-layer hidden representations of $y_w$ and $y_l$. The proposed modification makes the update a function only of the \textit{difference} in these representations. The paper shows how their proposed method can be implemented using stop-gradient/detach, and illustrates that it improves performance on mathematical reasoning problems.

### Strengths
The main strength of the paper is that the proposed method appears to have some positive effect, empirically. Fig. 2 suggests that the method does help the model better distinguish between preferred and dispreferred responses, and the results in Tab. 1 suggest that the method might be useful for marginally improving performance on some reasoning tasks.

### Weaknesses
The proposed approach is described and motivated rather vaguely. The goal is to "focus on" semantic differences. But there isn't really any explanation or analysis of why the proposed approach facilitates this, or in what sense it "focuses" on the differences. The method itself is explained in terms of a series of stop-gradient/detach operations; it is not clear what effect this series of operations has on the objective function being optimized or the dynamics of training. No intuition is provided for why semantic differences should be computed only at the last layer. The theorems are not unpacked to explain why they are interesting or why they validate core claims of the paper. As for the empirical results, they are encouraging, but there is no real empirical analysis of why the method helps, alternative design choices, etc. -- just benchmark numbers that go up.

### Questions
The related work section talks only generally about DPO and mathematical reasoning. Are there any techniques that are more closely related to your proposed approach?

Minor comment: the equations on L201 and L203 are missing the probability of y_1.

### Soundness
2

### Presentation
2

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
Current alignment methods like DPO often struggle to effectively differentiate between correct and erroneous mathematical  responses. Particularly since there are some shared semantics and some distinctive semantics between responses, they fail to disentangle these two characteristics when imposing the loss at the final token or logit level. Instead this paper proposes to leverage the rich semantic information embedded in the hidden state space of LLMs. Their method Focused Differentiation Training finetunes the model by emphasising the differences between the hidden states of correct and incorrect responses, rather than their common features. The authors provide theoretical analysis as well as some experiments on GSM8k, Math and MMLU-redux datasets.

### Strengths
- This an interesting thought proposition to utilise the rich semantic information in the hidden state representations, rather than the final token or logit level analysis. 
- Decomposing the hidden states into shared and distinctive semantic component and amplifying  the hidden states that contribute more to the differences in order to improve the models ability to distinguish between correct and incorrect responses seems quite meaningful
- The authors have gone into depths of this problem, giving some theoretical insights and proofs 
- Main contribution of the paper are some theoretical analysis which are contingent on some assumptions. I am not sure how general those assumptions are (see Questions to Author)

### Weaknesses
- Experiments are not thorough or mature enough. Experimental results are not very convincing as the improvements do not seem very consistent - In most of the cases improvement is around 1-2% which is somewhat insignificant. In some cases improvement is 3-4% or even over 6% for model for either DPO/Step-DPO setup, but if the model or DPO is changed, the performance improvement drops to again ~<1% or even hurting performance in some cases. From all this it is not very clear what is giving performance improvement and under what conditions? Some ablations would definitely be helpful in understand this.
- This seems to be a generic direction to investigate but I am curious why the entire setting in the paper was framed as a problem for mathematical reasoning alone? The authors show some results on MMLU-redux but those are also not very convincing (related to my above point)
- Since this exploration is based on the hidden states rather than the final logics, this seems to be a very model specific characteristic & empirical results also indicate that. Given that more llms should be considered for experiments on this work.
- Overall I feel this can be a good fundamental contribution if more empirical results and better consistency can be shown - more experiments on a wider set of llms across different  sizes and across different tasks - can focus on specific downstream tasks like reasoning (logical, mathematical and planning). At this stage, the paper feels quite incomplete mainly because of lack of enough experiments

### Questions
- Does the assumption in Theorem 2 require the hidden states to be bounded with some constant M and \delta for every input? If it is for every input then it seems to be quite restrictive. Remark 1 also then follows the similar restriction Can the authors comment on how general the applicability of this theorem would be?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To enhance the mathematical reasoning abilities of LLMs, this paper proposes the FDT algorithm. The paper points out that traditional DPO algorithms struggle to distinguish correct answers and incorrect answers at the token level, whereas FDT leverages hidden state analysis to fine-tune the model’s output layer weights, achieving better results.

The contributions of this paper include:

1. Proposing the FDT algorithm, which can be plugged into the RLHF framework, to improve mathematical reasoning capabilities.
2. Providing theoretical analysis and formula derivations.
3. Offering experimental results of the FDT algorithm and other baselines.

### Strengths
The paper proposes the FDT algorithm to  enhance the mathematical reasoning abilities of LLMs, and provides the detailed formula derivations. Mathematical reasoning capabilities of  LLMs are an important research direction. Considering the difference between correct answers and wrong answers are an interesting perspective. The datasets the paper chooses (e.g. GSM8K and MATH) are widely recognized to evaluate model's math reasoning ability. Experiments are conducted on  Llama-3.2-3B-Instruct and Qwen2.5-3B-Instruct, which both are great open-source LLMs.

### Weaknesses
1. Some expressions and statements in this paper are not sufficiently clear, making the article difficult to understand. For example, The expressions in Eq 7 and Eq 8 do not fully correspond to each other.

2. Theorem 2 in this paper, which serves as the foundation of the methodology, does not seem to be entirely correct. There is no evidence to support that the hidden states for correct and incorrect answers should be very close. More often, we prefer the difference between the two vectors to be significantly large. In addition, the similar and different aspects between correct and incorrect answers are difficult to be decoupled. The method in this paper does not provide any effective strategies for decoupling them, but rather assumes that they can be decoupled directly.

3. The experimental results cannot support the effectiveness of the method. Firstly, the experiments do not provide valid ablation analysis to demonstrate the effectiveness of the proposed modules. Secondly, the performance improvements of the proposed method is not significant. Finally, this work does not compare with other baselines. Methods based on LLM have already achieved better performance on the selected benchmarks.

4. The paper does not provide any interpretability results to support its conclusions. The detailed case analysis should be provided to expain how hidden state correction or  difference between the correct answers and wrong answers can influnce mathematical reasoning.

### Questions
1. The paper define $y$ as a sequence of tokens in line 197 to 198, but claims token $y$ in line 207 to 209. There are the two inconsistent definitions. Could you clarify what $y$ refers to?

2. There seems to be a lack of continuity between Equation 7 and Equation 8. Could you please provide further explanation?

3. The paper claims " As the responses of the same question are similar, the hidden states of correct response and incorrect response are similar", which seems to be problematic. I believe the authors need to provide more substantial evidence to demonstrate the causal relationship between the two.

4. Since the premise of Theorem 2 is problematic, it raises the question about the validity of Theorem 2 itself. Could you further clarify this issue?

5. The paper adopt the inconsistent  experimental settings between FDT and baselines, such as learning rate and hyperparameter β (in Section 5.3). Why is that?

6. For main results, shown in Table 1, there are several quetions:
(1)  llama-3.2 model fails in  MMLU-redux datasets, only achieving 7.48 % accuracy. Why is that?
(2) The performance of DPO+FDT and Step-DPO+FDT is inconsistent. For example, on the GSM8K dataset, Qwen2.5-3B-Instruct+DPO+FDT improved by only 0.1% over Qwen2.5-3B-Instruct+DPO, while Qwen2.5-3B-Instruct+Step-DPO+FDT showed a 2.4% improvement over Qwen2.5-3B-Instruct+Step-DPO. Could you explain the reason behind this inconsistency?
(3) Following up on the above question, this inconsistency varies across different datasets (GSM8K or MATH) and base models (Qwen2.5 or Llama-3.2). Could you explain the reason for this?
(4) Performance of Llama-3.2-3B-Instruct+DPO+FDT is even lower than Llama-3.2-3B-Instruct+SFT. Why is that?

7. Several minor errors. For example, citation errors in Seciton 5.1; repeated formula in Equation 7; the reference to $K$ is inconsistent in Algorithm 1.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper improves math reasoning by Focused Differentiation Training. That is, by comparing the win and lose answer, it calculates the difference between their embeddings. Then the algorithm takes gradients on the difference part, rather than the original embedding, using a stop gradient technique. By doing so, the model will get better signal from the main difference between the two solutions, rather than some common semantic features. This FDT algorithm shows good performance empirically on Math, GSM8K, and MMLU.

### Strengths
This paper proposes to take gradient only on the feature difference between the win and lose solutions, and shows this idea works well empirically. 

- Originality: I am familiar with the math reasoning literature. As far as I know, this idea is novel and interesting. It makes sense to me, and can be potentially used by all other models, as demonstrated by Theorem 1. 

- Quality: This is a nice paper presented with intuition, theorems, algorithms description, as well as experimental results. The theorems and intuitions are good and non-trivial, and the algorithm is also clearly stated, and easy to implement. I think this is a high quality paper. 

- Clarity: this paper is very easy to follow, especially if the reader is familiar with DPO. 

- Significance: I think this paper provides a very useful gadget for doing math reasoning. As stated in Theorem 1, it can be used for any other models as well. Therefore, I think many researchers in the field will be interested to try. However, since the improvements showed in the experiments are not very big, I will not say this is a ground breaking technique.

### Weaknesses
There is one thing that I am a bit confused. If the embeddings of win and lose can be decomposed into two parts, i.e.,  shared semantic component and distinctive semantic component, then it seems that the shared component is somewhat "same" for both win and lose answers. Therefore, even if we use the standard DPO, I think the algorithm will still automatically "ignore" this part, and try to optimize the distinctive part, is it?

I certainly understand that FDT algorithm makes this process explicit, which brings a better optimization process. However, it would be better if the author can explain why "throwing away" the shared component, what is the real benefit? Will the original DPO somehow optimize that component? If so, how does it affect the performance of DPO?

### Questions
I do not have additional questions.

### Soundness
4

### Presentation
4

### Contribution
3
