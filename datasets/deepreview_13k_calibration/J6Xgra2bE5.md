# Context-aware Prompt Tuning: Advancing In-Context Learning with Adversarial Methods

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Fine-tuning Large Language Models (LLMs) typically involves updating at least a few billions of parameters.
A more parameter-efficient approach is Prompt Tuning (PT), which updates only a few learnable tokens, and differently, In-Context Learning (ICL) adapts the model to a new task by simply including examples in the input without any training.
When applying optimization-based methods, such as fine-tuning and PT for few-shot learning, the model is specifically adapted to the small set of training examples, whereas ICL leaves the model unchanged. 
This distinction makes traditional learning methods more prone to overfitting; in contrast, ICL is less sensitive to the few-shot scenario.
While ICL is not prone to overfitting, it does not fully extract the information that exists in the training examples.
This work introduces Context-aware Prompt Tuning (CPT), a method inspired by ICL, PT, and adversarial attacks. 
We build on the ICL strategy of concatenating examples before the input, but we extend this by PT-like learning, refining the context embedding through iterative optimization to extract deeper insights from the training examples.
We carefully modify specific context tokens, considering the unique structure of input and output formats. 
Inspired by adversarial attacks, we adjust the input based on the labels present in the context, focusing on minimizing, rather than maximizing, the loss.
Moreover, we apply a projected gradient descent algorithm to keep token embeddings close to their original values, under the assumption that the user-provided data is inherently valuable. 
Our method has been shown to achieve superior accuracy across multiple classification tasks using various LLM models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Context-aware Prompt Tuning (CPT) as a new method to address the overfitting problem of prompt tuning. The optimization of CPT consists of a novel loss design and controlled token embedding optimization. Extensive experiments on various datasets using different LLMs demonstrate that CPT achieves better performance than baselines.

### Strengths
1. The research problem is interesting, and the authors proposed a new method for better LLM performance on several benchmark classification tasks. 
2. The authors have provided detailed literature studies and discussed the motivation of their method, 
3. The authors have done extensive experiments to demonstrate the effectiveness of CPT.

### Weaknesses
1. The paper is not clearly written and well-organized. It is hard to understand the authors' ideas and the proposed methods. For example, the motivation for presenting Figure 1 and Figure 2 before the introduction is not clear. Although the authors show some input presentation in Sec.3.1, it is still unclear what the inputs look like. The authors should have provided detailed examples in this section. 
2. The novelty if this paper is limited, it is a simple combination of several existing works, such as prompt tuning and adversartial training. Besides the empirical results, the paper also lacks theoretical analysis. 
3. The figures, such as Figure 2 and Figure 4, are not clear and hard to understand. For example, why are there two x_emb2 in Figure 4. What do different colors mean in these figures? 
4.  Some concepts need further clarification. For example, how to do projected gradient descent as presented in Lines 272-273. 
5. The authors only work on simple classification tasks and lack experiments on more general generation tasks, such as summarization and machine translation.

### Questions
1. Does the final loss have any tuning parameters, as presented in Line 252?
2. See weaknesses.

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
4

### Summary
This paper introduces an approach to mitigating overfitting in few-shot learning scenarios, where traditional fine-tuning often leads to overfitting, and in-context learning (ICL) performance is highly sensitive to the choice of demonstration examples. The authors propose a context-aware prompt tuning strategy that integrates elements of ICL and prompt tuning. In this method, the demonstration examples provided to the model are treated as tunable parameters, while the associated labels remain fixed. By tuning the context of these demonstrations rather than the entire model, the approach leads to improved generalization across multiple benchmarks.

### Strengths
- Proposes a simple extension of prompt tuning by combining it with in-context learning. 
- Evaluates the model on different open-source datasets like AGNews, SST-2, DBpedia and TREC.
- The figures (fig 2) in the paper are really helpful in understanding key differences between their method and various baselines they implemented.

### Weaknesses
 - The idea introduced is very similar to prompt tuning and the whole paper is just about applying it in-conjunction with in-context learning making it harder to find novelty in the approach. 
- The writing of the paper can be improved by quite a bit eg: abstract of this paper is hard to understand talking about different approaches rather than making it more crux on the solution/method and same applies to description provided on the set classification dataset.

### Questions
- Was any hyperparameter tuning or prompt optimization conducted for the baseline models? The reported performance of Llama-3 seems surprisingly low on straightforward tasks like SST-2, where zero-shot models typically perform well. This raises questions about whether the baseline results fully reflect the model's potential or if they were hindered by suboptimal configurations. Clarification on any tuning efforts for the baselines would be helpful to ensure a fair comparison with the proposed method.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a few-shot method called context-aware prompt tuning. This method is inspired by in-context learning and prompt tuning, concatenating examples before the input as in ICL and learning these examples as in prompt tuning. The authors verify the effectiveness of the proposed context-aware prompt tuning method on several classification tasks using three models.

### Strengths
The proposed method is straightforward and easy to understand.
The experiments in this paper are comprehensive, which use three models and test on several classification datasets.
The results show that the proposed method outperforms LoRA, PT, IPT and ICL in most cases.

### Weaknesses
1. The proposed method integrates ICL and PT intuitively, thus the novelty is not very significant.
2. Since the proposed context-aware prompt tuning is an optimization-based method, it also has the overfitting problem, just like fine-tuning and PT. Thought authors tried to mitigate overfitting by incorporating context labels into the loss function and applying projected gradient descent, the overfitting problem still exists in context-aware prompt tuning.

### Questions
1. Why ICL cannot fully extract the information that exists in the training examples?
2. In Table 1, CPT† (incorporating instructions) outperforms CPT on some datasets/models (for example SST-2 with BLOOM 1.7B), but underperforms CPT on other settings (for example DBpedia with BLOOM 1.7B, decreasing from 58.85 to 33.80 using 2 shots). How to explain this phenomenon?

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
This paper proposes context-aware prompt tuning (CPT), a few-shot learning method that optimizes the in-context example using projected gradient descent (PGD). The authors conduct experiments on various models and benchmarks, finding CPT outperforms other baseline methods (prompt tuning, LoRA, instruction prompt tuning).

### Strengths
The idea of optimizing the context using PGD is novel. If one needs to optimize the in-context example, it makes sense to use PGD so that the examples will not change by too much and the optimization does not overfit the few-shot examples.

### Weaknesses
1. It is unclear what is the motivation for optimizing the in-context example. Does that make more sense than optimizing the prompt in instruction prompt tuning (IPT)? There is one possibility that the performance should be attributed to the use of PGD, which might prevent from overfitting. It will be beneficial if there is abation study on that, e.g., uses other regularized optimizers or use PGD in baselines (IPT, PT).

2. Lack of analysis on the experimental results. Again, it might make the results easier to analysize if the authors disentangle these two components: (i) train on in-context samples; (ii) PGD as the optimizer. 

3. Some paragraphs are not clearly written. For example, in section 4.3, the authors introduce another variant $\dagger$ which initializes trainable tokens with human engineered instructions. It is unclear what is the difference between $PT^\dagger$ and $IPT^\dagger$ for few-shot setting since they both have few-shot examples and trainable instruction-initialized tokens. 

4. The Set Classification dataset is confusing. I feel the only mechanism that works for an input sequence from that dataset is to search in the context to see if the test example appears and copy the cooresponding label (if any) as the output (please correct me if I am wrong), which is simply an induction head,  and the loss design of CPT seems to be encouraging the forming of induction head. Therefore is it a good benchmark to measure few-shot learning?

5. In section 5.1 the title "Better with Harder Tasks" for that paragraph seems to be overclaiming.

### Questions
Please see weakness.

### Soundness
2

### Presentation
2

### Contribution
2
