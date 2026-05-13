# DeCoRe: Decoding by Contrasting Retrieval Heads to Mitigate Hallucinations

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Large Language Models (LLMs) often hallucinate, producing unfaithful or factually incorrect outputs by misrepresenting the provided context or incorrectly recalling internal knowledge.
Recent studies have identified specific attention heads within the Transformer architecture, known as \emph{retrieval heads}, responsible for extracting relevant contextual information.
We hypothesise that masking these retrieval heads can induce hallucinations and that contrasting the outputs of the base LLM and the masked LLM can reduce hallucinations.
To this end, we propose \textbf{De}coding by \textbf{Co}ntrasting \textbf{Re}trieval Heads (DeCoRe), a novel training-free decoding strategy that amplifies information found in the context and model parameters.
DeCoRe mitigates potentially hallucinated responses by dynamically contrasting the outputs of the base LLM and the masked LLM, using conditional entropy as a guide.
Our extensive experiments confirm that DeCoRe significantly improves performance on tasks requiring high contextual faithfulness, such as summarisation (XSum by 18.6\%), instruction following (MemoTrap by 10.9\%), and open-book question answering (NQ-Open by 2.4\% and NQ-Swap by 5.5\%).\footnote{Code is available at 
\repo.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the issue of hallucinations in Large Language Models (LLMs), where outputs may be unfaithful or factually incorrect. It identifies specific attention heads, called retrieval heads, within the Transformer architecture that are crucial for extracting relevant information. The authors hypothesize that masking these heads can induce hallucinations. To tackle this, they propose a novel decoding strategy named Decoding by Contrasting Retrieval Heads (DeCoRe), which does not require additional training. DeCoRe works by comparing outputs from the base LLM and a masked version to reduce hallucinations, guided by conditional entropy. Experiments show that DeCoRe significantly enhances performance in tasks demanding high contextual accuracy, such as summarization, instruction following, and open-book question answering, with notable improvements in various benchmarks.

### Strengths
1.	The paper is well-written.
2.	The research includes thorough experiments that effectively demonstrate the capability of DeCoRe in mitigating hallucinations across various tasks.
3.	The proposed method, DeCoRe, is training-free and useful for hallucination mitigation.

### Weaknesses
1.	The paper only provides evaluations on the effectiveness of mitigating hallucination. However, as a decoding method, it is also important to show the generated texts are coherent and fluent. Therefore, it is required to provide evidence to show this decoding method can generate text with high quality with low hallucination.
2.	It seems that in the experiments, many baselines can achieve better results than DeCoRe.
3.	The paper seems a combination of the existing findings, which applies the retrieval heads (Wu et al., 2024) to the Contrastive Decoding (Li et al., 2023) method, potentially limiting the originality of the contribution.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

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
This paper introduces a training-free decoding approach named DeCoRe for reducing hallucinations in LLMs. By identifying specific retrieval heads that influence the generation of grounded content, DeCoRe employs a masking strategy to induce hallucinations, then applies contrastive decoding to distinguish accurate from hallucinatory outputs. Experiments show improvements in contextual faithfulness on datasets like XSum and factual accuracy on tasks such as TriviaQA.

### Strengths
1. The paper is clearly structured, making complex ideas accessible and easy to follow.

2. The paper introduces a novel decoding approach that contrasts outputs from the original and masked LLM, effectively reducing ungrounded content.

3. The paper  incorporates an entropy-controlled mechanism, allowing the method to adjust the level of contrast applied depending on the model’s uncertainty.

### Weaknesses
1. The model's performance improvements are inconsistent across different datasets, and it fails to outperform baseline models in many settings (e.g., XSum, IFEval). This is inconsistent with the summary conclusions presented in the abstract.

2. The paper only compares a limited number of baselines, primarily focusing on contrastive methods, without evaluating against many related models.

3. The approach in this paper appears to be related to self-consistency and should better include a discussion on this topic, along with relevant baseline comparisons.

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces DeCoRe, a decoding strategy for reducing hallucinations in LLMs. DeCoRe works by contrasting between a LLM (that can be augmented with additional context), and the same LLM where the attention heads that are responsible for extracting information from the context (i.e., retrieval heads) are masked, assuming masking these heads induces hallucinations and thus contrasting between the two distributions increase factuality. The weight given to each distribution can be controlled by a hyperparameter that estimates the model’s uncertainty using the entropy of the model. Experimental results show that DeCoRe significantly improves contextual faithfulness on multiple tasks including summarization and open-domain QA.

### Strengths
- The methodology of contrasting between a variant where retrieval heads are masked is interesting and has benefits over previous methods, for example in applicability.
- The experimental setting is thorough, comparing against six strong baselines on three tasks (reading comprehension, summarization, and instruction-following) with multiple datasets, including XSum, MemoTrap, IFEval NQ, PopQA, and TruthfulQA.
- The advancements on MemoTrap in comparison to the baselines are significant.
- The paper is overall well-written and easy to follow.

### Weaknesses
 - It seems that in several experiments, the improvements from DeCoRe are either marginal or it even performs significantly worse than other methods. For example, as presented in Tab.1 CAD significantly outperforms DeCoRe on NQ-Swap whilst performing similarly on other benchmarks (within a one point margin). While I agree with the paper that DeCoRe has higher applicability I am not entirely sure that CAD cannot be used for MemoTrap (see questions).

- The paper also claims that DeCoRe can increase factuality (Tab.2) and multi-hop reasoning with CoT (Tab.3) but from looking at these tables, in most cases that DeCoRe is best-performing it is within a one-point margin to the second-best performing model (as stated in the paper, there are also cases where the baselines perform better). Additionally, in all experiments three DeCoRe variants are compared against the baselines, which can be a bit misleading. I believe the paper might benefit from an aggregated score for each method and error bars or statistical tests for the main claims. This can simplify understanding the significance of the main results.

- I believe the paper might benefit from a qualitative analysis that supports the main claims. For example, when is using conditional entropy beneficial and when does it hurt performance, and when does DeCoRe outperform the baselines?

### Questions
Please see weaknesses, I am willing to reconsider my score.

Regarding CAD and MemoTrap, maybe I am missing something, but perhaps it’s possible to use the task as the additional context, e.g., for the task - “Write a quote that ends in the word "talk": Don't bark if you can't”, the additional context can be “Write a quote that ends in the word "talk".

Again, maybe I am missing something, but lines 330-331 state that DeCoRe has ‘competitive performance’ on NQ-Swap, but CAD outperforms DeCoRe by 8+ points. What gains do you consider substantial in the context of the experiments and the datasets in the paper?

### Soundness
2

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
3

### Summary
The paper proposes a new variant of contrastive decoding for reducing hallucinations in language models (LMs). At high level, contrastive decoding uses the difference between two LMs’ likelihood as the final decoding criteria. Typically, there is a baseLLM that generates a basic sequence of tokens which might contain hallucinations. To reduce the amount of hallucination, the probabilities of each generated token is then offset by the corresponding token probabilities from another weaker or corrupted LM which might contain more hallucinations. By using the offset to calibrate the sequence likelihood, the resulting decoding can potentially avoid undesirable failures from the second LM.

In this paper, the authors focus on building the corrupted LM leveraging the so-called retrieval attention heads found by recent work. Specifically, by masking those retrieval attention heads, the resulting corrupted LM is more likely to ignore context information, leading to more faithfulness issues (hallucinations).

Thus, the hypothesis is that using the token probability difference between the base LM and the corrupted LM can lead to better grounded responses.

Experiments are conducted on several representative datasets across different open source LMs (Llama 3 8B & 70B in main text), including long-form (summarization) and short-form (question answering) generation tasks.
Overall, the proposed method is found to be effective in making LMs more sensitive to provided context while not interfering with the LM’s parametric knowledge.

### Strengths
The paper is easy-to-follow with necessary background.

Given the wide range of LM applications, developing efficient and reliable hallucination mitigation methods is a very important research direction. 

The proposed method is a nice extension of contrastive decoding with recent attention head function insights.

The experiment design are mostly reasonable with several recent baselines to validate the effectiveness of the proposed method

### Weaknesses
Although it is good to build upon recent attention head insights for contrastive decoding, the generalizability of those identified retrieval attention seems very limited.

The improvement over baselines is at odds and not pronounced enough. For example, the proposed method does not provide consistent improvements over the base LM and CAD on fluency and coherence (lower ROUGE-L and BERTScore-F1). It is good to analyze the response difference to drive deeper understanding, e.g., does the proposed method lead to shorter and more concise generation? Typically, shorter answers are preferred by question answering datasets, e.g., NQ, TriviaQA.

As reported by the authors in Fig 3, masking more heads is not necessarily helpful. It is good to explore alternative attention selection strategies, e.g., randomly masking, selecting heads based on the required task solving capabilities (profiling using question answering datasets), or layer-based selection (e.g., balanced masking out across different layers).
That said, it might be interesting to see whether certain attention heads are more related to shorter vs longer context retrieval. 

There are some further improvements can be done for the experiment part:
Most of the datasets studied are of shorter input context. It is good to explore some datasets with longer context (e.g., retrieving more passages) and compare the method there. In addition to longer context, it is also good to explore more involving contexts, e.g., contextual conflicts.

It is good to report the robustness of those chosen hyperparameters. For example, can the proposed method benefit from different sampling temperatures and varying number of heads to be masked. As in-context examples are used for certain tasks, it is good to study the robustness of that decision, e..g, different set of shot and less or more examples.

### Questions
Is there any difference in terms of generations from the proposed method vs others, e.g., fluency, length?

What is the smaller LM used for DeCoRe lite? 

What is the alpha value for DeCoRe static? How that is determined?

What is the computational cost for all compared methods, e.g., tflops?

### Soundness
3

### Presentation
3

### Contribution
3
