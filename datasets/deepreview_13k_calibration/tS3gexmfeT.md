# Fusion Token: Enhancing Compression and Efficiency in Language Model Tokenization

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
In the realm of language models, data encoding is pivotal, influencing efficiency and effectiveness of model training. Byte Pair Encoding (BPE) is a well-established subword tokenization technique that balances computational efficiency and linguistic expressiveness by merging frequent byte or character pairs.
As language model training requires substantial computational resources, we propose Fusion Token, a  method that substantially enhances the conventional Byte Pair Encoding (BPE) approach in data encoding for language models. Fusion Token employs a more aggressive computational strategy compared to BPE, expanding the token groups from bi-grams to 10-grams. Remarkably, with the addition of 1024 tokens to the vocabulary, the compression rate significantly surpasses that of a regular BPE tokenizer with a vocabulary of one million. Overall, the Fusion Token method leads to noticeable performance improvements due to an increased data scope per compute unit. Additionally, higher compression results in faster inference times due to fewer tokens per given string. By devoting more compute resources to the tokenizer building process, Fusion Token maximizes the potential of language models as efficient data compression engines, enabling more effective language modeling systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper present a Fusion Token method for tokenization, by expanding the token groups in BPE from bi-grams to 10-grams.
By adding extra 1024 10-grams tokens to  a 51K BPE vocabulary, this paper claims the compression rate surpasses that of a regular BPE tokenizer with a vocabulary of one million.

In experiments, this paper trains 125M LM and 650LM respectively, and shows the new vocabulary (51K + 1K) trained model is better than the 51K one for code generation task.

### Strengths
1. The proposed tokenization method show a faster inference time thanks to the shorter tokenized sequence length.

2. The proposed method brings improvement for code generation task.

### Weaknesses
Experiments and results alone are insufficient to support the claim. I believe this paper fails to demonstrate that the proposed method can enhance the performance of a language model.


- 1. Introducing an additional 1024 10-gram tokens can indeed result in a higher bytes-per-token value compared to vanilla BPE tokenization, which is an expected outcome and not surprising. The contribution of this higher compression rate is not clear, as the language model's performance does not appear to improve, as shown in Table 4.

- 2. The paper falls short in establishing connections between the results and existing language models, particularly in terms of data, model architecture, and downstream tasks. This paper trains two language models, one with 125 million parameters and another with 650 million parameters, using a subset of the Pile dataset, and evaluates them with two code generation tasks. There is a lack of discussion about the rationale behind this specific experimental setup, which makes it challenging to comprehend and verify the results since they cannot be directly compared to other papers. I have a question: Why not use widely recognized language model benchmarks such as PG-19 and WikiText103 for training and evaluation, or follow the setup described in the official Pile dataset paper to train GPT2 models of varying sizes (small, medium, large)?

- 3. Only the code generation downstream task is evaluated.

### Questions
How is "Bytes per token" in Table 1 calculated? Is it the average length E[l]?

It appears that the proposed method is not specifically designed for programming languages but rather for general language modeling. If that's the case, why was a programming language chosen for testing?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a fusion token method. Given a dataset, the proposed method integrates the newly constructed n-gram tokens derived from that dataset into the existing BPE vocabulary. These newly added tokens are treated as special tokens, taking precedence over existing tokens during inference. Experimental results demonstrate that these added tokens enhance the compression rate of the dataset and achieve higher scores on code generation benchmarks.

### Strengths
The paper underscores the significance of optimizing tokenization by analyzing the relationship between bits per word and bits per byte. The proposed method is articulated as an algorithm, facilitating comprehension.

### Weaknesses
The main concerns regarding this paper are:

- A significant issue is the potential bias in the experimental setup. The existing BPE tokens are formed from data comprising multiple ``text’’s. However, the added tokens from Fusion token method become contingent upon the additional training data. Essentially, they hinge on $D$ provided as input in Algorithm 1. If the distribution of the training data and the data being evaluated are similar, the newly added tokens will notably influence the evaluation. In section 4.2, the training data was obtained from code written in various programming languages, with subsequent evaluations conducted on code benchmarks. Since both the dataset for building the additional tokens and the dataset for evaluation are similar, an enhanced performance over the conventional BPE is anticipated. Specifically, the concern is that the 1K tokens added by the Fusion Token method are tailored to the specific code dataset used, potentially leading to overfitting and an overestimation of performance on similar datasets.

- The aforementioned bias is also observed in Table 1 and Figures 2(a) and 2(c). Tokens introduced via Fusion Token show a remarkable performance improvement in code part relative to text. Since the tokens were derived from code data, their impact in the experiments is profound. This suggests that the performance gains might be inflated due to the homogeneity of the training and evaluation data, rather than a true reflection of the method's generalizability.

- To validate the robustness of the tokenization, evaluations using a variety of benchmarks other than code generation are essential. The current evaluation is narrowly focused on code generation, which limits the understanding of the proposed method's effectiveness across different domains and tasks. Diversifying the evaluation benchmarks would provide a more comprehensive view of the method's strengths and weaknesses.

- Assessing the efficacy of the 1K tokens added by the proposed method necessitates a comparison against a tokenization with 1K tokens appended solely through bi-gram merging (existing BPE approach). This comparison would help isolate the impact of the Fusion Token method from the simple addition of more tokens to the vocabulary. Without this baseline, it is difficult to determine whether the observed improvements are due to the novel token integration method or merely the increased vocabulary size.

- Based on the data in Table 4, it's premature to infer that "BPE for large models with Fusion Token is superior to standard BPE" from tests on just two models. The sample size is too small to draw a definitive conclusion about the superiority of the proposed method across a wide range of large language models. Further experimentation with a larger variety of models is needed to substantiate this claim.

### Questions
Q1: Of what are the actually added 1K tokens comprised?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Fusion Token, a method that enhances the conventional Byte Pair Encoding (BPE) technique for data encoding in language models. Fusion Token utilizes a more aggressive computational strategy by expanding token groups from bi-grams to 10-grams. This approach results in a higher compression rate compared to regular BPE tokenization with a vocabulary of one million. The method demonstrates noticeable performance improvements and faster inference times, as it increases the data scope per compute unit and reduces the number of tokens per string. By dedicating more computational resources to the tokenizer building process, Fusion Token maximizes the efficiency and effectiveness of code language models as data compression engines.

### Strengths
The paper exhibits strong motivation and is easy to follow. In the pursuit of achieving the highest data compression ratio, it is justified to expand token groups from bi-grams to 10-grams. Although the method is relatively simple, I believe it should outperform the naive BPE model in practical scenarios. However, the observed performance gap in the experiments is not as significant as described. Grouping frequent n-grams together in a straightforward manner can indeed increase the data compression ratio, even without complex theories or networks behind it.

### Weaknesses
1. My main concern with this paper is the performance of token fusion on natural language (NL) corpora. The authors have only conducted experiments using a code corpus, which is significantly different from NL. Code language typically consists of similar patterns, better structure, and limited vocabulary size, making token fusion more likely to be effective. However, NL content is more complex, with greater variability in content. Therefore, it is essential for the authors to conduct experiments on an NL corpus to demonstrate the effectiveness of their method. In my opinion, token fusion should have a greater impact on code than on language.

2. The paper would benefit from conducting additional ablation studies in the experiments. I am particularly curious about the rationale behind selecting only 1K tokens in the paper. It would be interesting to explore the outcomes by varying the number of tokens, such as selecting 500 tokens, 2K tokens, or 4K tokens. This would provide valuable insights into how the performance changes with different token selections.

### Questions
1 How to decide the fusion token for different corpus? Why you choose 1K in your paper?
2 Does token fusion cross whitespace?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes FusionToken as an approach to improve the standard bpe tokenization and shows this approach improve tokenization efficiency: adding 1k additional vocabulary over 50K original vocabulary can achieve better tokenization efficiency (i.e., shorter sequence) than using 1M BPE vocabulary. The shorter sequences owing to the efficient tokenization can make inference faster, making language modeling efficient.

### Strengths
The strengths of this paper are two-fold:

- It shows promising results that adding 1k additional vocabulary can achieve better tokenization efficiency than 1M bpe tokenization in code data, demonstrating a potentially useful tokenization method for code language processing.

- The evaluation on code generation benchmarks show that the tokenization can also improve language modeling performance in addition to inference efficiency.

### Weaknesses
Firstly, the details of the tokenization process are not entirely clear to me. For standard subword tokenization methods such as BPE or SentencePiece, these methods will not merge tokens that are separated by whitespace. For instance, in a sentence like "I go to the park every day.", these standard tokenization methods would not merge "go to" into a single token, nor would they merge "every day" into a single token, even if these phrases co-occur very frequently. I'm unsure if the method proposed in this paper follows the same principle as standard tokenization, refraining from merging tokens separated by whitespace. If this is the case, I have serious doubts about the claim that adding 1k vocabulary can outperform 1M vocabulary, as this seems unlikely from my understanding. I suspect that the method proposed in this paper might merge tokens separated by spaces, such as "go_to" or "every_day". If this is true, the comparison with the original BPE method seems unfair as they operate under different settings. Although I acknowledge that this approach may be more reasonable for code data, standard tokenization can also be easily applied to this setting. If so, the authors should provide more details and evaluations to demonstrate the superiority of their method.

Secondly, this method seems to be only applicable to code data, as code data contains many very frequent patterns (e.g., "int cnt = 0;". If we allow merging tokens beyond spaces, we can have "int_cnt_=_0;" as 1 token). This is why it makes sense to do so in code data. However, in the Natural Language (NL) domain, this approach would likely result in a significant reduction in performance improvement and could cause semantic confusion due to the tokenization. Therefore, I question the universality of this method and wonder if the authors have conducted experiments on natural language datasets to validate this method.

Thirdly, the improvement of this tokenization method on the code dataset is not substantial, with only about a 10% increase. Recent works have used neural methods for context compression, achieving a compression ratio of 2-4 times. The authors should discuss and compare their method with these techniques to demonstrate the value of FuseToken.

### Questions
See weakness

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
