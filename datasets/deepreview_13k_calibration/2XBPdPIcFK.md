# Steering Language Models with Activation Engineering

- Decision: Reject
- Avg Score: 5.00
- Scores: 8, 3, 6, 3

## Abstract
Prompt engineering and finetuning aim to maximize language model performance on a given metric (like toxicity reduction). However, these methods do not fully elicit a model’s capabilities.  To reduce this gap, we introduce \emph{activation engineering}: the inference-time modification of activations in order to control (or \emph{steer}) model outputs. Specifically, we introduce the \emph{\method} (\shortmethod) technique, which contrasts the intermediate activations on prompt pairs (such as “Love” versus “Hate”) to compute a \emph{steering vector} (\citep{subramani-2022-extracting}). By tactically adding in e.g. the “Love” $-$ “Hate” steering vector during the forward pass, we achieve SOTA on negative-to-positive sentiment shift and detoxification using models including LLaMA-3 and OPT. {\shortmethod} yields inference-time control over high-level output properties (like topic and sentiment) while preserving performance on off-target tasks. {\shortmethod} is lightweight: it does not require any machine optimization and works with a single pair of data points, which enables rapid iteration over steering. {\shortmethod} demonstrates the power of activation engineering.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors introduce a paradigm of controlling model outputs/behavior which they term activation engineering. In activation engineering, a user controls model behavior by editing intermediate activations/hidden states of the model during the forward pass. They propose and focus on a specific method in the class of activation engineering called Activation Addition (ActAdd), in which a vector encoding an axis (e.g. love vs hate) can be added to the intermediate activations to make the model shift along that axis, e.g., in sentiment from negative to positive. They compute this vector by taking the difference along a single paired example (e.g. a love vs hate example) and demonstrate effectiveness in experiments on sentiment analysis and toxicity reduction.

### Strengths
Originality: The idea of activation engineering as “perturbing activations during the forward pass” is an important and simple idea. While it seems that much concurrent or previous work has also worked with this idea of editing activations, e.g. the ROME paper (Meng et al 2022), adding steering vectors (ActAdd) to control model outputs is to my knowledge original (and the authors do well to cite concurrent work in Li et al 2023b). 

Quality: Experiments are overall fairly thorough and demonstrate that ActAdd is a promising, intuitive, and simple approach to control model outputs.

Clarity: The overall flow of the paper is clear and well written.

Significance: This is an important contribution to interpretability and control of models using activation-level edits. The idea that you can controllably transform model behavior by adding a vector to the residual stream is important.

### Weaknesses
The biggest weaknesses in my read are a lack of clarity in the algorithm and some of the experiment setup and results. I leave specific questions/suggestions on this point for the Questions section of the review.

Also, the authors should be careful to clarify their definitions and contributions. In the intro/abstract, they define activation engineering as “the inference time modification of activations in order to control model outputs”. However, section 2 states “Activation engineering invovles creating vectors of activation which cause desired changes to output text when added to the forward passes of a frozen LLM”. This latter definition sounds more specific than the original one; there are many works which fall under the first definition but not necessarily the second one. From my read, I would be careful to claim that you are introducing activation engineering and might instead recommend stating it as highlighting AE as a class of methods to control behavior, under which ActAdd (your primary contribution) falls.

### Questions
* Can you elaborate on how you search for injection coefficient c and injection layer l? How expensive is this process?
* In Figure 2, what is the x axis? Why should we expect perplexity to go down when x axis increases?
* In Figure 3, how is “P(steered completion contains wedding related words)” determined? Can you be more explicit about this in the paper? 
* Can you elaborate on what the p value in table 3 and 4 is? That is, what is the null hypotheses you are testing (and the corresponding alternative hypothesis)?
* In Figure 5/S4.5, referring to the model’s behavior as “off-target answer probabilities” is rather misleading. That phrase reads as the model’s distribution over the answers for non-target tokens, whereas it seems that the actual probabilities being referred to is the P@K.
* How do you determine which example to use to determine the steering vector? Did you do any studies on variance across the effectiveness for vectors derived from different examples?
* Are there any experiments to support the claim in the intro that activation engineering can enable composition of multiple traits, e.g. speech eloquence and mathematical content? If not, I would remove this to avoid overclaiming.
* The notation in Algorithm 1 could use some improved clarity. For example, what is @? In code it can refer to a matmul; even though this seems like an indexing operation the ambiguity is confusing for the reader.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes ActAdd, a method to _steer_ a Language Model's generation in a particular direction. ActAdd is lightweight and merely involves using contrasting prompts (related to the direction you want to steer the LM in). These contrasting prompts are used to compute a steering vector that can be applied at inference time to change the model's behavior.
The authors experimented with various tasks such as steering the topic of the LM's generation, steering to reduce toxicity, and steering to change sentiment. 
The authors also show that ActAdd preserves the model's knowledge by showing that when the model's accuracy remains unchanged on ConceptNet when asked to steer towards a certain topic.

### Strengths
The proposed approach is straightforward, lightweight, and demonstrates effectiveness on certain benchmarks. However, the experiments conducted only partially support the claims made in the paper (see more details under weaknesses).

The algorithm is well-presented, though some aspects of the experiments could benefit from further clarification.

### Weaknesses
 The paper’s experiments are interesting but could benefit from further depth and clarity. In some cases, it’s challenging to fully understand the conclusions drawn from certain experiments. Additionally, some benchmarks created by the authors are quite small, which makes the results appear more anecdotal than empirical. There are also a few discrepancies with the baselines, as well as cases where only portions of larger benchmarks are used (eg. why use only a subset of RealToxicityPrompts and Sentiment? The current experimentation is performed on ~10% of the test split)

The paper would greatly benefit from demonstrating how ActAdd performs on larger benchmarks specifically designed for steering and alignment, such as HelpSteer (1 and 2)[1,2]. Also comparisons to methods that involve alignment training might give some indication on if ActAdd can be used instead of or in tandem with some these approaches in practice [3]. 

I've summarized my concerns as questions for certain parts of the experiments section

Questions
1. ACTADD CAN CONTROL WHAT THE MODEL TALKS ABOUT
- Which dataset serves as the starting point for the prompts? Is the experiment based on a single prompt with 100 generations? If so, **using a single prompt might make it difficult to fully verify the claim that "ActAdd can steer the model to talk about a topic."**
- Why does ActAdd perform well for certain topics but not others (e.g., Art)? Is it effective only for steering toward specific topics? Additionally, it is unclear what accounts for the drop at c=0.5 for weddings? This might indicate some experiments on how reliable ActAdd is. 

2. ACTADD CAN REDUCE TOXICITY
- The results in this section could be clearer. The only baseline models are the unsteered model, prompting, and PREADD, while other comparisons, such as FUDGE and AirDecoding, are tested on GPT-2, making direct comparison difficult given the model-dependent nature of the task.
- Regarding the other results there seem to be a lot of discrepancies -- The authors pick most of their baselines from (https://aclanthology.org/2023.findings-acl.636.pdf). However, the unsteered OPT result is very different. (0.152 vs 0.134 toxicity and 49.9 vs 8.9 for fluency). With such a large change in fluency, it seems there might be a difference in the experimental setup of the two papers. This throws some doubt if the ActAdds better fluency comes from a different experimental setup. 

3. ACTADD PRESERVES THE MODEL’S GENERAL KNOWLEDGE

There are some concerns regarding the setup here. ConceptNet, as a knowledge base, typically requires single-word answer predictions. Showing that the model performs similarly with and without ActAdd doesn’t entirely demonstrate that ActAdd avoids side effects on the model’s factual accuracy. Perhaps this could be bolstered with verifying if the factuality of longer form generations remain unaffected. The FactScore benchmark [4] might be a good place to start. 

Finally, while I attempted to review the provided code for further insights, it was challenging to navigate, and the links listed in tab 5 of the appendix did not seem to work.


Overall I believe the approach has potential and the paper could heavily benefit from more thorough and comprehensive experimentation.

### Questions
Questions added in Weaknesses

### Soundness
1

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
Paper proposed “Add Act”, a type of activation engineering that, when applied to language models (LMs), can “steer” the model the output during inference. “Steering” an LM, in this context, would mean enabling the user to enhance or control some high-level property of the generated text such as topic or sentiment of the text.

### Strengths
1. The proposed activation engineering method can be applied during inference and does not require gradient-based optimization (thus making it computationally fast to compute and apply).
2. The proposed activation engineering method does not modify the original LM’s weights, and therefore would not change the model’s performance on tasks if the activation engineering method wasn’t applied. This is a unique advantage, as many related “steering” methods that modify a LM’s weights may harm model performance on tasks unrelated to the “steering”-related tasks.
3. Paper provides many compelling examples of where “AddAct” has been able to successfully steer an LM output (i.e., sentiment, topic, reducing toxicity) across many model architectures.

### Weaknesses
The authors have missed some related work in the area of activation engineering, and their paper may benefit from further comparing and contrasting the proposed “AddAct” method to these works:

[a] Sakarvadia, Mansi, et al. "Memory injections: Correcting multi-hop reasoning failures during inference in transformer-based language models." arXiv preprint arXiv:2309.05605 (2023).

[b] Heimersheim, Stefan, and Neel Nanda. "How to use and interpret activation patching." arXiv preprint arXiv:2404.15255 (2024).

[c] Vig, Jesse, et al. "Investigating gender bias in language models using causal mediation analysis." Advances in neural information processing systems 33 (2020): 12388-12401.

Specifically, I would like the authors to discuss the computational cost of computing the steering vector, especially if one must test multiple steering vectors for multiple target layers (as it is not obvious which layers/vectors would work best for a specific “steering” goal, and thus a user may need to do (costly) experimentation. Specifically, the “AddAct” method relies on generating the “steering vector” by doing two partial forward passes for the steering prompt pair. This itself is computationally expensive compared to a recent related work [a] which demonstrated that one could compute a “steering vector” simply using the model’s (un)embedding matrix, rather than running the steering prompts through the top N layers of an LM.

Further, the “AddAct” “steering vector” is layer-specific within a given LM. For example, if a steering vector is generated for layer N, it is not clear if the same vector can be applied to layer N+1. This is a drawback of the method as it may not be apparent to the user which layer would be best for an "AddAct" injection. Again, I would be interested if the authors could discuss how their proposed layer-specific steering vector generation strategy compares to related work [a] which proposed a steering vector that is layer-agnostic.

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces ActAdd, a controlled text generation technique that modifies the inner activations of an LLMduring forward passes to guide text generation towards a specific property. These modifications are applied using steering vectors, computed by taking the difference between the activations of a positive and negative prompt at a specific layer. The results demonstrate that ActAdd outperforms the baselines on tasks such as toxicity reduction and sentiment control.

### Strengths
- The paper is well-written and easy to follow.
- Activation addition is an intuitive and powerful technique that enables fine-grained control over model outputs.
- The results convincingly show that activation addition outperforms included baselines in both sentiment control and toxicity reduction tasks.

### Weaknesses
The primary issue with the paper is that it is outdated. The paper refers to several works published in 2023 as "contemporary," implying that they are based on the presented work. This suggests that the paper may have been rejected in previous conferences and is now being resubmitted to ICLR without any major modifications. However, works from 2023 cannot be referred to as contemporary in a submission to ICLR 2025.

Moreover, the claim that both Liu et al. (2023) and Zou et al. (2023) are based on this work is questionable. A quick review of these papers reveals that Liu et al. (2023) merely cites ActAdd as related work, and Zou et al. (2023) actually outperforms ActAdd on one of the tasks. Therefore, I do not believe ActAdd presents any novel idea or result. This undermines the relevance of the method, and I believe this alone is sufficient for rejection. However, if I have misunderstood this point, the authors could clarify their claims.

Additional (and significant) weaknesses include:
- Outdated Models: Most of the experiments were conducted on outdated models (OPT, GPT2-xl, and Llama-2). While a few experiments were rerun on Llama-3, there were no baseline comparisons for these models.
- Inconsistent Baselines: The models used in the baselines do not match. For example, in Table 3, various models are used without a clear pattern. Ideally, all models should be run for every baseline to ensure fair comparison.
- Outdated Baselines: Baselines such as Fudge and PreAdd have been surpassed by newer techniques (e.g., [1]). Additionally, the paper does not include any baselines that use white-box transformations to control model behavior, despite several relevant works from 2023 (Liu et al. (2023) and Zou et al. (2023)).
- Inconsistent Perplexity Measurements: Perplexity for the included models was measured using Davinci 002, an old and less effective model. Furthermore, Lines 503-505 state that PreAdd's perplexity was measured using Davinci 001, making direct comparisons between the two methods problematic.
- Omission of Fudge: In Lines 378-380, Fudge is omitted, despite performing better on certain aspects and only slightly worse on others. This is a strange misrepresentation of the results.
- Redundant Experiments: The experiments in Sections 4.1 and 4.2 add little to the discussion, as they merely confirm that activation addition works. Furthermore, Tables 3 and 4 essentially present the same findings, but in a more interesting and applicable setting.
- Basic Metrics: Perplexity and cosine similarity are insufficient metrics to fully capture fluency and relevance. Since controlled text generation methods edit the model's internals, they can yield unintuitive results that these metrics may not fully capture. The authors should include human or LLM-based evaluations to assess the outputs in Tables 3 and 4 and compare them with baselines.
- Insufficient Code: The provided code lacks essential instructions and does not include scripts to reproduce the experiments. It only includes some notebooks for experimenting with activation addition, which overlooks the most important reason for providing the code. Additionally, the link to the GitHub repository that is present in the included code (playground.ipynb, top) violates the double-blind review process, as it is not anonymized.
- Unconvincing Experiment in Section 4.5: Evaluating a model with activation addition on one or more recent, open-form reasoning benchmarks (such as GSM8k, MixEval, or MMLU-Pro) would be much more convincing than the benchmark with perplexity measurements.
- Different Hyperparameters Across Experiments: If I am correct, the results for activation addition were generated using different values for top_p and temperature compared to some baselines (e.g., PreAdd), which undermines the validity of the comparisons. All non-critical hyperparameters should be kept consistent across baselines.

### Questions
- What is meant by "this section does not have complete statistics" in Line 533?
- How was grid search performed for ActAdd's hyperparameters? Were the results reported for the best set of parameters? If so, was a similar hyperparameter search conducted for the baselines to ensure accurate comparisons?
- Could you clarify the hyperparameter “a” discussed in Appendix C and explain its function?
- For which experiments are the prompts mentioned in Lines 1218-1223 used? Appendix C presents a collection of unrelated details, making it difficult to follow and understand how it fits into the overall context of the paper. Could the authors clarify the connection to the experiments?

### Soundness
1

### Presentation
2

### Contribution
2
