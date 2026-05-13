# Mitigating Copy Bias in In-Context Learning through Neuron Pruning

- Decision: Reject
- Scores: 6, 3, 8, 5

## Abstract
Large language models (LLMs) have demonstrated impressive few-shot in-context learning (ICL) abilities. Still, we show that they are sometimes prone to a `copying bias', where they copy answers from provided examples instead of learning the underlying patterns. In this work, we propose a novel and simple method to mitigate such copying bias.  First, we create a synthetic task and use the Integrated Gradients method to identify neurons that prioritize copying over generalization. We demonstrate that pruning these neurons consistently improves performance across a diverse set of ICL tasks. We also show that our method is applicable across various LLM architectures, including Transformers and State-Space Models, without requiring modifications.  
In our analysis, we adopt a task-recognition perspective on ICL and examine task vectors ~\citep{hendel2023context} induced by the model. We find that pruning enhances the quality of these vectors, suggesting that the pruned neurons previously hindered effective task recognition.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel approach to addressing a key issue in large language models (LLMs) during In-Context Learning (ICL)—the tendency to copy answers from provided examples, known as “copying bias.” Instead of learning and generalizing from the patterns in the context, models often replicate the examples, especially in few-shot learning settings. To tackle this, the authors propose using Integrated Gradients (IG) to identify neurons responsible for this copying behavior. By pruning these “copying neurons,” the model’s ability to reason and generalize is improved.

The method is task-agnostic and applicable across various LLM architectures, including Transformer-based models like GPT, Bloom, OPT, and LLaMA, as well as State-Space Models such as Mamba. Extensive experiments across different tasks show that neuron pruning significantly reduces copying errors, enhancing overall task performance. The paper also demonstrates that this pruning improves the quality of task vectors, leading to better task recognition and generalization.

### Strengths
This paper successfully implemented neural pruning into tackling the copy bias in ICL. The proposed IG method with pruning strategy are relatively reasonable to solve the copy bias problem. This is a significant contribution as previous work primarily focused on prompt engineering and calibration methods without directly addressing the internal model dynamics causing copying errors.

Also, the proposed method is versatile, as it can be applied across LLM architectures, including both Transformersand SSM, without needing task-specific modifications. This general applicability makes the method highly practical for a wide range of ICL tasks and model types. It provides “out-of-the-box” improvements without requiring model retraining or access to large amounts of task-specific data, making it an efficient post-processing step in LLM deployment pipelines.

The authors use a vowel-counting task as a proxy for detecting copying errors, where language models are prone to making copying mistakes. The proxy ICL dataset generation method is clear are easy to follow. The diverse range of tasks helps to demonstrate the robustness and general applicability

### Weaknesses
The primary weakness of this paper is the lack of a comprehensive evaluation of the model’s capabilities after pruning. While the method effectively mitigates copy bias, this paper presents more of a case study rather than demonstrating its real-world applicability. Pruning techniques generally have an impact on the overall performance of the model, and as such, it is critical for the authors to provide results showing how the pruned model performs on downstream tasks. Unfortunately, this paper does not offer that kind of evaluation, which is a necessary component to fully understand the implications of the pruning approach on the model’s general capabilities.

Another issue with the paper is the limited comparison with baselines. The authors provide several ICL-related baselines, but they seem to operate under the assumption that copy bias can only be addressed with ICL-focused solutions. The paper would benefit from a broader exploration of the problem, including a more detailed definition of copy bias and an examination of its resolution under different types of models, such as base and instruct models. Notably, the authors did not experiment with instruct models, which may behave very differently, especially with methods like APE that are known to improve prompt-following capabilities. Additionally, it would be valuable to explore whether fine-tuning or data engineering, such as modifying the SFT dataset or providing higher-quality alignment data, could address the issue. If data engineering alone could solve the problem, one must question the necessity of introducing an additional, complex pruning process, particularly for large models where pruning is a non-trivial engineering task.

### Questions
- How does the pruned model perform on downstream tasks, such as reasoning, math, long-context understanding, instruction following, and safety? While it may not be necessary to conduct an exhaustive evaluation due to computational resource limitations, at the very least, relevant experiments should be included.

- Does it matter if the model is a base model or an instruct model? For example, if Bloom-560M is turned into an instruct model or fine-tuned with DPO, will the experimental results change or remain the same?

- Can data engineering help solve this problem? If it can, why do we still need an additional step to prune the model?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces "copying bias" in large language models (LLMs) in-context learning and presents a method for detecting copying neurons and improves the performance on ICL tasks. The author conducts experiments on ICL tasks and task vectors to verify the claim.

### Strengths
1. The author uses illustration to help the reader better understand how the proposed method works.
2. The author considers different ICL tasks for validation.

### Weaknesses
1. Lacks some implementation detail: in Section 3.3, what is the size of n? The author assumes that $\hat{y}\notin S_p$ and therefore if n is large, there will be many repetitions in $S_p$ since labels in $S_p$ are the count of vowels, which are integers. Also, does the author explicitly held out an integer so that when constructing $S_p$, the words cannot have the number of vowels equal to this held-out integer?
2. Universality of copying neurons detection: This paper only studies how to detect copy neurons on the vowel counting task. What if this proxy ICL task is switched to other tasks? Will the copying neuron detected still work, and if not (e.g., if all elements in $S_p$ are unique), what makes vowel counting special that it works as a proxy ICL task?
3. Continuation of the previous point: method in 3.3 assumes that the output has single token. This is probably fine for the vowel counting task as single-digits are single-tokens. What if we have other ICL tasks as proxy ICL task and the outputs are multi-tokens?
4. How are errors being calculated? There are two ways: 1) probability-based: all probability summed for labels not equal to the true label and averaged across all inputs; 2) accuracy-based: 1 - (accuracy for the correct output) with greedy decoding.
5. In Figure 2 and 3, it seems that only models up to 1.3B are evaluated. In Figure 2 it seems that a large proportion of error comes from the copying error. However, for larger models (e.g., 8B, 14B) and for the singular to plural task, I suspect that larger model will not have this high copying error if each in-context example is unique. For 1-shot and 2-shot setting, the performance might simply be improved by adding a task description at the very front to eliminate task ambiguity.
6. Pruning the neuron is essentially "training" the model on the ICL task. It would be convincing if the author presents other training-based method as baselines (with a sweep of hyperparameter on the validation set) in Figure 2 and 3.
7. For Figure 5, while there is improvement, the author does not show how much improvement comes from less copying bias. The author has larger models like Llama-3-8B in Figure 4 experiment but there lacks evidence that the pruning decreases the copying error.

Minor issues:
1. Example in the introduction can be ambiguous. it could also be the case to count the number of words and this case the correct answer for "Florida" is 1.
2. Line 063-064: the first quotation mark of "Copying Neurons." is not correct.

### Questions
Please see the weakness section above where I asked some questions.

### Soundness
2

### Presentation
2

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
This paper addresses the issue of copying bias in LLMs during in-context learning (ICL). To mitigate copying-biase, the authors identify and prune specific "copying neurons". They use Integrated Gradients (IG) on a synthetic vowel-counting task to locate these neurons and then prune them. The approach is shown to generalize across multiple model architectures (e.g., GPT-2, OsPT, BLOOM) and improves the quality of task vectors—representations that encapsulate task-specific information—indicating better task recognition. This method provides an effective way to enhance ICL performance without task-specific fine-tuning, offering a broadly applicable strategy for deploying more reliable LLMs.

### Strengths
1. This paper demonstrates that mechanistic interpretability methods like Integrated Gradients (IG), typically used for understanding model behaviors, can have practical implications such as improving in-context learning (ICL). By identifying and pruning neurons responsible for copying behavior, the paper presents an innovative approach to enhancing ICL performance.

2. The authors conduct experiments across a wide range of tasks and model architectures, demonstrating consistent performance improvements. This thorough evaluation reinforces the robustness and generalizability of the proposed method.

3.  I appreciate that authors can first justify the prevalence of copying errors to justify why such a bias is worth targeting across different models and tasks. This rigorous approach highlights the significance of addressing this bias, underscoring the method’s relevance and value in improving model generalization.

### Weaknesses
1. **Similarity of Tasks and Limited Generalizability**: The 18 tasks studied in this paper share notable similarities with vowel counting, meaning that the copying neurons identified through Integrated Gradients primarily apply to a set of very related and rather synthetic tasks. While the authors also attempt to show improvements on non-synthetic tasks, I am not sure how to interpret "copying error" on datasets like SST2 and SST5, which are multiple-choice tasks with a limited set of choices (e.g., 2 or 5 options)? In such cases, does the model exhibit a genuine copying bias or if the improvements are driven by other factors? Would the copying bias be easily mitigated by using unbiased ICL samples (for example, one sample for each answer choice A/B/C/D).

2. **Limited Exploration of Trade-offs**: The paper does not extensively address the potential trade-offs introduced by pruning neurons. Authors only claim that the pruned model never has a drop in performance but what about other side effects? For instance, pruning could theoretically affect the model's performance on tasks where copying might be beneficial (e.g., fact-based retrieval tasks). A more detailed analysis of cases where pruning could have a negative impact would be beneficial.

3. **Minor Reproducibility Concerns**: The paper lacks details on certain experimental settings, such as the dataset specifications (e.g., training/validation sizes, number of shots) for the vowel-counting data, as well as the hyperparameter settings used for pruning. Including these details would enhance reproducibility and provide greater clarity on the experimental setup.

### Questions
1. In Figure 2, it’s clear that the copying error rate has dropped consistently across different models and tasks, contributing to improved accuracy. However, I’m surprised that copying errors still dominate the error rate in the unpruned model. Do the authors have any insight into why this phenomenon occurs? Additionally, how does the copying error rate compare for the vowel-counting task specifically? I’m curious about the extent to which copying errors can be reduced on the in-distribution task (vowel counting) versus out-of-distribution tasks (the other ICL tasks).”

2. Why are all the tasks restricted to 4 shots? My intuition is that with more few shot examples, the model is more likely to pick up the actual pattern and less likely to copy, therefore, the method will become less effective. This analysis is not  to weaken the method — as authors have pointed out that some task might have limited ICL examples as a restriction, and the proposed method is a great way to mitigate the bias. I am trying to get a better understanding on the limitation of the proposed method. 

3. For the BBH object counting task, my understanding is that these are complex reasoning tasks that benefit from Chain-of-Thought (CoT) reasoning, which ICL examples could potentially demonstrate. Can the authors clarify if CoT prompting is employed in either the baseline models or the copy-error-pruned method?

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
This paper shows that large language models (LLMs) can exhibit a copying bias, often simply copying their answers from the in-context examples. The authors identified task-agnostic neurons responsible for this copying behavior using integrated gradients [1] on a vowel-counting proxy task (Secs. 3.2 & 3.3). They mitigate their influence by pruning them (i.e., simply setting them to 0; Eq. 8). Their neuron pruning method improves in-context learning (ICL) performance across various tasks, including the ICL benchmark proposed by Hendel et al [2], two sentiment analysis tasks and an object counting task, and various models, including GPT-2, Llama variants or Mamba. They also find that pruning these neurons improves the effectiveness of task vectors [2].

---

[1] Sundararajan, M., Taly, A., & Yan, Q. (2017). Axiomatic attribution for deep networks. In ICML.

[2] Hendel, R., Geva, M., & Globerson, A. (2023). In-context learning creates task vectors. In EMNLP.

### Strengths
* **S1**: Previous work has focused on improving ICL primarily through black-box approaches (e.g., prompt tuning), whereas this work adopts a mechanistic perspective. This shift is valuable, as it has the potential to deepen our understanding of the internal workings of ICL in these models.

* **S2**: The pruning method effectively improves ICL performance across various architectures and tasks. Additionally, it enhances the quality of task vectors, also leading to improvements in ICL performance.

### Weaknesses
 * **W1**: The overall technical contributions (Sec. 3) are modest. The work applies a well-established attribution method (integrated gradients) to identify neurons responsible for a specific behavior (copying) and then prunes these neurons to achieve the intended outcome (no copying, though that’s unclear to me, see **W2**). Unfortunately, this is highly similar to prior work such as the one by Ghorbani et al [1]. For example, they used Shapley values (another attribution method) to identify neurons that led to gender-specific biases and pruned them to achieve gender fairness. Thus, while the application to copying in ICL is novel, the methodological contributions remain limited (i.e., the use of prediction shift ΔL instead of max probability for integrated gradients, l. 227-230). The core idea of using attribution methods to identify and remove problematic neurons is not new, and the specific adaptation using prediction shift instead of max probability, while potentially useful, does not represent a significant methodological leap. The novelty is primarily in the application to the specific problem of copying in ICL, rather than a fundamental advance in the methodology itself.

* **W2**: It is unclear to me whether the performance improvement results from the reduction of copying neurons or from the pruning of neurons exhibiting different behavior. For example, why would performance improve on *copying* tasks such as “list first” or “list max” in the ICL benchmark of Hendel et al [2], which require copying from the in-context examples? Tabs. 3-6 consistently also show improvements on these *copying* tasks. If the identified neurons indeed suppress the copying behavior, we would expect to see drops in performance on such tasks. This seems to contradict one of the authors’ main claims that they “identify specific neurons responsible for triggering the copying behavior (copying neurons)” (l. 71-73). The improvement on tasks that require copying suggests that the method may not be specifically targeting copying behavior, but rather some other aspect of model behavior that is correlated with copying. A more thorough analysis is needed to understand the precise mechanism by which the pruning improves performance, and whether it is indeed related to the suppression of copying as claimed.

* **W3**: It is unclear whether the copying bias is merely an artifact of the ill-posed nature of few-shot ICL problems, and whether it remains relevant for many-shot ICL problems. Does this copying bias persist beyond the few-shot setting? (This point is also raised in the questions below.) The study should investigate the persistence of this bias in more realistic scenarios with a larger number of examples, as the current analysis is limited to few-shot settings. The relevance of this bias in practical applications needs to be established.

* **W4**: The writing could be improved. There are several typos throughout, and clarity and reproducibility would benefit from including all necessary details, such as those regarding proxy dataset generation.

* **W5**: Code is not provided, making reproducibility challenging.

### Questions
* **Q1**: Is the copying bias merely an artifact of having a limited number of examples (e.g., <= 4)? For instance, what happens in a 64-shot setting? Could this bias indicate that the copying issue arises from an ill-posed in-context learning (ICL) problem rather than a general model flaw?

* **Q2**: Could the authors provide additional details about the proxy dataset? For example, how many shots are used, and could a few more examples be included for completeness?

* **Q3**: How does pruning of these neurons affect the overall model performance beyond ICL tasks? For example, how do the pruned LLMs perform on more general benchmarks such as [Live-Bench](https://livebench.ai/) or other reasoning benchmarks (e.g., MMLU or GSM8K)? Or, what’s the performance on the indirect object identification (IOI) task? The authors suggest that their method “could be broadly applicable, potentially becoming a standard post-processing step in LLM deployment pipelines” (l. 497-498). However, it remains unclear if this would be a sensible approach for LLMs deployed “in the wild.”

* **Q4**: Are the minimum and maximum values of the normalizing functions calculated across the dataset alone, or are they based on both the dataset and all neurons?

* **Q5**: What’s the significance of the meta-optimization (l. 319-369)? Why not greedily remove the neurons based on the “copying score” from Eq. 7 (this may be related to the question in **Q4**)?

* **Q6**: What’s the relation of the real-word experiments in Sec. 4.2 (sentiment analysis and object counting) to the copying behavior that’s the main topic of the present work?

### Soundness
2

### Presentation
2

### Contribution
1
