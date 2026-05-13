# Transformers Provably Solve Parity Efficiently with Chain of Thought

- Decision: Accept
- Scores: 10, 8, 8

## Abstract
This work provides the first theoretical analysis of training transformers to solve complex problems by recursively generating intermediate states, analogous to fine-tuning for chain-of-thought (CoT) reasoning. We consider training a one-layer transformer to solve the fundamental $k$-parity problem, extending the work on RNNs by \citet{Wies23}. We establish three key results: (1) any finite-precision gradient-based algorithm, without intermediate supervision, requires substantial iterations to solve parity with finite samples. (2) In contrast, when intermediate parities are incorporated into the loss function, our model can learn parity in one gradient update when aided by \emph{teacher forcing}, where ground-truth labels of the reasoning chain are provided at each generation step. (3) Even without teacher forcing, where the model must generate CoT chains end-to-end, parity can be learned efficiently if augmented data is employed to internally verify the soundness of intermediate steps. Our findings, supported by numerical experiments, show that task decomposition and stepwise reasoning naturally arise from optimizing transformers with CoT; moreover, self-consistency checking can improve multi-step reasoning ability, aligning with empirical studies of CoT.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The paper provides a theoretical foundations which explain the benefits of chain-of-though. The authors study a simple setup of k-parity problem with 1-layer Transformer and in this case provide a separation results for transformer trained without intermediate supervision and one trained with teacher forcing. They also provide positive results for the case where the transformer can generate chain-of-thought but is not explicitly supervised with the intermediate results. They show conditions which are required in this case (data augmentation and self-consistency checking).

### Strengths
I find the work to be of very high quality and very relevant to the current research in reasoning abilities of language model. The theoretical setup is in my opinion well chosen, very concise and easy to understand.  Even though this is a theoretical paper, the authors are well aware of the current research on the applied side and the questions studied reflect it. I believe it is a strong accept, but I'm giving accept because I'm not sure whether theoretical results of this kind should have spotlight talks at ICLR.

### Weaknesses
I was not able to judge how limiting is the setup described in the paper overall, but for example the special masking seems quite artificial but I understand that it is required for the theoretical results. It would be nice if the authors explicitly describe the limitations they are aware of. The reliance on a specific k-parity problem, while allowing for clean theoretical analysis, might not fully capture the complexities of real-world reasoning tasks. The single-layer transformer architecture, while simplifying the analysis, also raises questions about the generalizability of the results to deeper, more complex models. The masking procedure, while necessary for the theoretical framework, introduces an artificial constraint that may not be present in practical applications of chain-of-thought reasoning, potentially limiting the direct applicability of the findings. The analysis also seems to depend on a specific learning rate regime, which might not be easily transferable to other optimization settings.

### Questions
I did not came up with any useful and educated questions. I believe the paper is of high quality and will need to study it in more depth.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a theoretical exploration of how transformers develop stepwise reasoning capabilities through recursive task decomposition, using the k-parity problem as a case study. Through formal mathematical proofs and asymptotic complexity analysis, the authors establish three key findings: without intermediate supervision, solving k-parity with finite-precision gradient-based algorithms requires exponentially many steps, extending prior impossibility results to finite-sample settings. In contrast, with teacher forcing—where ground-truth intermediate steps are provided—the model efficiently learns the task in a single gradient update, underscoring the value of explicit supervision for complex reasoning. Additionally, even without teacher forcing, the model achieves accurate reasoning by employing data augmentation to validate intermediate steps, implementing a form of self-consistency check that allows for logarithmic convergence. This research emphasizes theoretical analysis through mathematical proofs and complexity analysis, offering insights into how transformers can perform chain-of-thought reasoning and task decomposition, thereby aligning with recent empirical advances in complex reasoning tasks.

### Strengths
1. The paper innovatively uses the k-parity problem to theoretically analyze how transformers develop stepwise reasoning capabilities.
2. This paper introduces a novel hierarchical decomposition of the k-parity problem and designs a corresponding transformer architecture to handle this structure effectively.
3. This paper proposes mechanisms like data augmentation and self-consistency checks, enabling transformers to perform CoT reasoning even in the absence of explicit intermediate supervision.
4. The paper provides clear and logically rigorous analysis for the k-parity problem, offering strong, well-structured insights within this specific context.

### Weaknesses
1. The theoretical analysis is heavily focused on the k-parity problem, which, while illustrative, may not extend seamlessly to more complex or varied reasoning tasks. This limits the applicability of the findings to broader transformer applications. The k-parity problem, by its nature, has a very specific hierarchical structure where each intermediate step is a simple 2-parity operation. This structure is unlikely to be representative of real-world reasoning tasks which often involve a mix of different types of operations and dependencies, and may not have such a clear hierarchical decomposition. The paper does not address how the insights gained from k-parity would translate to scenarios where the intermediate steps are not neatly defined or where the relationships between sub-problems are more complex.
2. The paper lacks empirical experiments to support the theoretical conclusions, which could leave readers questioning the practical effectiveness of the proposed methods in real-world scenarios or on diverse datasets. While the theoretical analysis is rigorous within the confines of the k-parity problem, the absence of empirical validation makes it difficult to assess the practical relevance and robustness of the proposed mechanisms. For example, it's unclear how the data augmentation and self-consistency checks would perform in noisy environments or with more complex data distributions. The paper does not include any experiments on real-world datasets or even simulated data beyond the k-parity problem, which limits the confidence in the generalizability of the findings.

### Questions
1. For the k-parity problem, each layer’s intermediate state corresponds to a simple “2-parity” check, which is straightforward to define. In more complex tasks, however, defining such intermediate states may not be as intuitive. How could this approach be extended to real-world reasoning tasks where intermediate state decomposition is less clear?
2. The paper uses data augmentation to validate intermediate states in the reasoning process. If applied to practical reasoning tasks, would this data augmentation method require significant adjustments to be effective?
3. Given the proposed architecture, are there potential challenges that might arise in real-world training, particularly concerning stability and computational complexity?

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
Authors showed that CoT here is beneficial to learn a very hard problem, i.e. bit subset parity. Authors trained a one-layer transformer with a fixed CoT and with a tree based approach to determine the subset and they showed that without CoT it's not possible to learn an algorithm to detect the right bit, _assuming_ data cannot be manipulated freely. They introduced a causal mask to allow less error propagation during CoT.

### Strengths
S1. The study is very rigorous, sharing some lights on the importance of CoT on multi hop reasoning. 

S2. The introduction of the causal mask is indeed very simple to explain and very intuitive, but also very effective to limit the error compounding. I think this is the main contribution, given teaching forcing is not really useful on this problem.

S3. This work extended previous related work on more realistic setting, offering a clearer picture of why CoT is indeed essential for the given problem.

### Weaknesses
W1. Main weakness is a lack of empirical validation. I would love to see just a trained model on various settings (like with and without teacher forcing, parity problem sizes with different $k$ and $d$ values) to show that without teaching forcing the model is indeed able to learn the task. Specifically, the paper would benefit from a more thorough investigation into how the model's performance scales with increasing problem complexity, such as larger values of $k$ and $d$. It is not clear how the model would perform with a more realistic training regime, rather than the carefully chosen one-step learning rate used in the theoretical analysis. The absence of experiments with different training strategies, such as varying batch sizes or learning rate schedules, makes it difficult to assess the robustness of the proposed approach.

W2. The claim on the conclusion about finetuning transformer to improve multi step reasoning seems really too strong. In particular, it would be nice to show that it's easy to produce CoT data for all reasoning tasks before claiming this. So I would rephrase that sentence or provide a more detailed discussion on why authors believe their results may extend to other reasoning tasks. The current discussion lacks a rigorous justification for generalizing the findings to more complex reasoning tasks beyond the specific bit subset parity problem. The paper needs to address the potential limitations of the proposed approach when applied to tasks with more intricate dependencies and less structured intermediate steps.

### Questions
Q1. Is there any particular reason why one-layer transformer has been chosen? Would the same results (or even stronger) apply to 2 layer transformer?

Q2. Could we apply the same idea to less structured task which lack the hierarchical structure, hence the "easier" teaching forcing?

### Soundness
4

### Presentation
4

### Contribution
3
