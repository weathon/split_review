# FacLens: Transferable Probe for Foreseeing Non-Factuality in Large Language Models

- Decision: Reject
- Scores: 3, 5, 8, 5

## Abstract
Despite advancements in large language models (LLMs), non-factual responses remain prevalent. Unlike extensive studies on post-hoc detection of such responses, this work studies non-factuality prediction (NFP), aiming to predict whether an LLM will generate a non-factual response to a question before the generation process.
Previous efforts on NFP have demonstrated LLMs' awareness of their internal knowledge, but they still face challenges in efficiency and transferability.
In this work, we propose a lightweight NFP model named \textbf{Fac}tuality \textbf{Lens} (\model), which effectively probes hidden representations of questions for the NFP task. Besides, we discover that hidden question representations sourced from different LLMs exhibit similar NFP patterns, which enables the transferability of \smodel across LLMs to reduce development costs.
Extensive experiments highlight \model's superiority in both effectiveness and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a model method (FacLens) to predict the likelihood of language models (LMs) generating non-factual responses before generation occurs, a task called non-factuality prediction (NFP). This work claims that, unlike traditional non-factuality detection (NFD) methods that probe response representations, FacLens probes the question's hidden representations to make non-factuality predictions. FacLens can be adapted to different LMs by leveraging unsupervised domain adaptation techniques, which reduces the resource-intensive need to generate new labeled data for each model. The authors conduct experiments across four models and three datasets to demonstrate FacLens's superior performance and efficiency compared to baseline methods.

### Strengths
1. FacLens can be adapted to different LMs by leveraging unsupervised domain adaptation techniques, which reduces the resource-intensive need to generate new labeled data for each model. 
2. The authors present a shift from traditional non-factuality detection (NFD) to non-factuality prediction (NFP). They show that models are internally aware of whether they can accurately answer a question before generation.

### Weaknesses
1. The authors claim that different LLMs share similar cognitive patterns in terms of knowledge awareness, as they rely on transformer-based architectures. However, not all LMs use the same architecture; for instance, recent MoE architectures, which have gained significant popularity, replace feed-forward networks with MoE modules. It is essential to study MoE-based models to examine if this claim holds. Additionally, the proof of this hypothesis is unclear and not convincing and needs further support.
2. Apart from the domain adaptation techniques, FacLens’s development heavily relies on previous work and lacks substantial novelty.
3. The overall performance gain compared to baselines, particularly SAPLMA, is marginal, and so there is no compelling evidence that probing question hidden representations leads to better non-factuality prediction.
4. In the main experiments (Table 1), NFD baselines are excluded, and only a selected set of methods categorized under NFP are reported.
5. The experiments do not represent a practical LM generation setting, as they are limited to a set of short-form QA datasets. While the authors define the NFP task, they compare it with naive baselines, such as entity popularity, and do not consider more sophisticated methods developed for factuality improvement using model internals.
6. Some findings, such as LLMs generally recognizing “whether they know” in their middle layers, have been previously reported and are not new findings.

### Questions
Please refer to the weaknesses for clarification. Also, the paper has multiple typos that can be addressed.

### Soundness
2

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
3

### Summary
Unlike studies on post-hoc detection of non-factual responses, this paper studied non-factuality prediction (NFP), that aims to predict whether an LLM will generate a non-factual response to a question before the generation process. While previous efforts on NFP have demonstrated LLMs' awareness of their internal knowledge, they still faced challenges in efficiency and transferability. Thus, this paper proposed a lightweight NFP model, named Factuality Lens (FacLens), which effectively probes hidden representations of questions for the NFP task. Further, this paper discovered that the hidden question representations from different LLMs exhibit similar NFP patterns, which enables the transferability of FacLens across LLMs to reduce development costs. The experiments highlighted FacLens’s superiority in both effectiveness and efficiency.

### Strengths
This paper tackled an interesting task of non-factuality prediction (NFP), tried to solve the problems of previous work in efficiency and transferability, and proposed a lightweight NFP model, named Factuality Lens (FacLens). The experiments highlighted FacLens’s superiority in both effectiveness and efficiency.

### Weaknesses
1. While the observations that the hidden question representations from different LLMs exhibited similar NFP patterns in Sec. 4.2 is interesting, we are eager to know why they happened and why unsupervised domain adaptation is possible in cross-LLM FacLens. It is better to investigate and mention some possible reasons for them, if possible, while the inspiration from the research on human cognition was mentioned in the paper.

Further, I wonder the observations in Sec. 4.2 can be really applicable to other LLMs. Can the authors mention the generalizability of the observations?

More seriously, in Sec. 5, depending on the datasets, the characteristics and the performance of LLMs seem different in Fig. 6. For example, on PQ and EQ, Qwen2 is rather different from the others, that leads to a concern that the assumption is not really correct and the transferability cannot be really valid among the LLMs.

2. I have a concern about the method for NFP dataset construction. Following previous work, the authors adopted a method for QA datasets with short answers. However, all current QA datasets are not generally in the category. It is better to show how large the method can cover the current QA datasets and/or to describe how they can cope with QA datasets with longer or more complex answers.

3. When the authors construct training data on just an LLM, the selection of the LLM might be important and might affect the performance. So it is better to show which LLM the authors selected as the best for constructing the training data and how they decided it.

4. In human evaluations in Sec. 5.3, it is better to have comparisons with some baselines.

### Questions
1. While the authors criticized the output statement in cases when LLMs cannot provide factual answers in the end of Sec. 2, I could not understand the criticization because the statement is not necessarily a non-factual answer. I hope the authors will clarify the point.

### Soundness
2

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
This work introduces FactLens, a NFP model which, unlike previous NFP methods, exhibits transferability across different LLMs. The authors make the following major contributions through the introduction of FactLens:
1. Show clear evidence of the importance of hidden layers in the pre-hoc/NFP setting.
2. Introduce a novel architecture for Factlens, such that the Factlens model weights can be adapted to a new LLM for good performance on the NFP task. 
3. Conduct experiments to show superior performance in comparison to both post-hoc models, as well as similar NFP models. Factlens is also considerably faster than other similar models.

### Strengths
* This paper solves a series of important problems, notably the transferability in the NFP domain. This kind of domain adaptation is an important area of NLP research and should be encouraged across the community.
* The experiments are very well thought, extremely detailed, and the paper is overall pretty decently written.

### Weaknesses
Certain questions that seem to remain open:
* The size of LLMs used for training seems small. While this isn’t a major concern, it would be good to understand how FactLens does with larger models (say size > 50B)
* It’s not clear whether Domain Adaptation is used for the results in Table 1. If no, how does the domain-adapted Factlens do in comparison to other NFP baseline?. In general, the authors should clarify which of the results in the paper use DA for FactLens. This can be added in the experimental setup.

### Questions
Nothing major, see weaknesses.

### Soundness
4

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
This paper introduces FactLens, a probing method designed to predict whether a large language model (LLM) is likely to provide factual responses to a given question. Additionally, the authors demonstrate that FactLens can be effectively transferred across different models.

### Strengths
1. The method is clear and straightforward. FactLens is a simple probing method to assess question factuality, and its streamlined structure makes it easy to adopt.
2. Excellent efficiency and transferability. The experiments demonstrate that FactLens can be effectively transferred to other models, performing well across various benchmarks, including PopQA, Entity Questions, and Natural Questions.

### Weaknesses
1. The primary weakness is that FactLens does not show a clear performance improvement over previous methods. Both Figure 3 and Table 1 indicate that FactLens performs comparably to, but not significantly better than, prior approaches. Specifically, the gains over methods like LoRA and Self-Evaluation appear marginal, raising questions about the practical significance of the proposed method. The similarity in performance, particularly in Figure 3, between $f_m$ and $f_{mix}$, suggests that the transferability, while present, does not lead to a substantial advantage in predictive accuracy.
2. The experiment lacks a wider range of benchmarks. Adding more datasets, such as TriviaQA [1] and HotpotQA [2], could provide a more comprehensive evaluation. The current benchmarks, while relevant, do not fully capture the diversity of factual question-answering scenarios. For instance, the inclusion of datasets that require more complex reasoning or multi-hop inference would be beneficial to assess the robustness of FactLens.

### Questions
Refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
2
