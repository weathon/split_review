# Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization

- Decision: Accept
- Scores: 6, 6, 5, 8, 5

## Abstract
Large language models (LLMs) have demonstrated remarkable in-context learning (ICL) abilities. However, existing theoretical analysis of ICL primarily exhibits two limitations: \textbf{(a) Limited \textit{i.i.d.} Setting.} Most studies focus on supervised function learning tasks where prompts are constructed with \textit{i.i.d.} input-label pairs. This \textit{i.i.d.} assumption diverges significantly from real language learning scenarios where prompt tokens are interdependent. \textbf{(b) Lack of Emergence Explanation.} Most literature answers \textbf{\textit{what}} ICL does from an implicit optimization perspective but falls short in elucidating \textbf{\textit{how}} ICL emerges and the impact of pre-training phase on ICL. In our paper, to extend (a), we adopt a more practical paradigm, \textbf{\textit{auto-regressive next-token prediction (AR-NTP)}}, which closely aligns with the actual training of language models. Specifically, within AR-NTP, we emphasize prompt token-dependency, which involves predicting each subsequent token based on the preceding sequence. To address (b), we formalize a systematic pre-training and ICL framework, highlighting the layer-wise structure of sequences and topics, alongside a two-level expectation. In conclusion, we present data-dependent, topic-dependent and optimization-dependent PAC-Bayesian generalization bounds for pre-trained LLMs, investigating that \textbf{\textit{ICL emerges from the generalization of sequences and topics}}. Our theory is supported by experiments on numerical linear dynamic systems, synthetic GINC and real-world language datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper derives generalization bounds for in context learning using a topic-dependent and data-dependent view of pre-training,

### Strengths
- This paper looks at in-context learning through a new lens of generalizing over topics and sequences, which is a novel contribution.
- The generalization bounds arrived at in Theorem 4.3 are similar but tighter than the bound from [Li et al](https://proceedings.mlr.press/v202/li23l.html), which is valuable.
- The paper has a comprehensive appendix that readers will find helpful while grokking the paper.

Overall I think the paper has a new view that adds to recent work on the theory of in context learning.

### Weaknesses
 - I am not entirely certain of the impact of this paper. Sure the bounds derived are new and tighter than previous similar ones in [Li et al](https://proceedings.mlr.press/v202/li23l.html), but I am not sure this contribution (alongside the view of modeling pre-training topics) is significant enough for ICLR. Perhaps a more fleshed out discussion section in the paper could remedy this, I am open to changing my opinion given a solid argument of why this result is significant compared to bounds from adjacent literature.

 - From what I can tell, the experiments in Appendix C.2 on GINC with varying number of topics are far more relevant than those in Section 5 which just show better ICL performance with more context length. Why did the authors choose to organize the paper in such a way? If there is a reason, I think the authors should highlight it, as it definitely stood out to me that the experiments in section 5 are common knowledge from existing in-context learning literature.

### Questions
- From what I can tell, the experiments in Appendix C.2 on GINC with varying number of topics are far more relevant than those in Section 5 which just show better ICL performance with more context length. Why did the authors choose to organize the paper in such a way? If there is a reason, I think the authors should highlight it, as it definitely stood out to me that the experiments in section 5 are common knowledge from existing in-context learning literature.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- This paper seeks to provide a theoretical understanding of in-context learning for language models.
 - A simple topic model is assumed, where a set of topics are drawn independently and a sequence is generated given each topic; this is done both for the pretraining data as well as the in-context learning data; note that the pretraining and in-context learning topics are different in general, but are drawn i.i.d. from a shared topic distribution.
 - The main result is a PAC-Bayes bound that controls the log-loss on new in-context learning instances, as a function of the number of topics, number of sequences per topic, and sequence length. (There are actually two results - one conditioned on a single topic, and one that averages over topics).
 - A few experiments demonstrate that accuracy improves as the sequence length increases.

### Strengths
- Obtaining theoretical analysis of in-context learning is a worthwhile goal, given the general lack of rigorous theory in this area.
 - The actual result that's derived is non-trivial (analyzing both sample complexity and optimization); and sensible in the sense that the bound scales fairly cleanly with the typical quantities (sequence length, number of sequences, number of topics).

### Weaknesses
 - Some of the claims/framing in the paper seemed a bit odd. For example, 'emergence' is highlighted a few times, but I don't think it's necessary to invoke that: the setting here is a much more conventional transfer learning + domain generalization.
 - The paper contrasts previous analyses's i.i.d. approach compared to the autoregressive one in this paper, but this paper still assumes that we have i.i.d. sequences (it's just that the tokens in each sequence are not independent, which is not remarkable).
 - The essence of in-context learning as it manifests in LLMs is that the pretraining data is meant to just be raw text from the Internet, and that the in-context data is supposed to be examples of some task. The surprising part of ICL is that the pretraining and in-context distributions are very different. The fact that this paper assumes the two are the similar I think misses the spirit of in-context learning.

 - It seems like Theorem 4.3 is optimization-dependent, but it seems like we are just analyzing the solution to Equation 1, so does the choice of optimization algorithm come in? Assumption 4.2 bounds the gradient by S, which I see appears in (6). But what is assumed on the optimization algorithm? How can we even guarantee that it converges to the global optimum?
 - Theorem 4.6: If you have a topic at ICL time that you didn't see at pretraining time, it seems like your loss could be arbitrarily bad (since I don't see any other distributional assumptions). How does this manifest in the bound? Indeed, I think this is the interesting part of ICL (which one can think of as a transfer learning problem).
 - In general, it seemed like a lot of the paper defines fairly basic things, and it's only at page 7 when things get interesting. But by that time, there's really no space in the paper to discuss the actual theorems (not to mention that the experiments are very abbreviated).
 - I'm not sure what insight to take away from the experiments (other than that increasing sequence length helps). It would have been nice to see some even more synthetic experiments that try to test the theory (how things actually scale with K, N, T).

### Questions
- It seems like Theorem 4.3 is optimization-dependent, but it seems like we are just analyzing the solution to Equation 1, so does the choice of optimization algorithm come in? Assumption 4.2 bounds the gradient by S, which I see appears in (6). But what is assumed on the optimization algorithm? How can we even guarantee that it converges to the global optimum?
 - Theorem 4.6: If you have a topic at ICL time that you didn't see at pretraining time, it seems like your loss could be arbitrarily bad (since I don't see any other distributional assumptions). How does this manifest in the bound? Indeed, I think this is the interesting part of ICL (which one can think of as a transfer learning problem).
 - In general, it seemed like a lot of the paper defines fairly basic things, and it's only at page 7 when things get interesting. But by that time, there's really no space in the paper to discuss the actual theorems (not to mention that the experiments are very abbreviated).
 - I'm not sure what insight to take away from the experiments (other than that increasing sequence length helps). It would have been nice to see some even more synthetic experiments that try to test the theory (how things actually scale with K, N, T).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper gives a generalization bound of sequences for in-context learning in a language model under the auto-regressive next-token prediction paradigm. It models the practical AR-NTP paradigm for an In-context Learning Framework, considering the two-level expectation loss over sequence and topic. Then it presents Theorems for the generalization of sequences and topics, provides the upper bound of the two-level expected loss. Thus, it indicates that ICL emerges from number of topics, number of sequences and sequence length, and demonstrated by limited numerical experiments.

### Strengths
1. This paper considers the Auto-Regressive Next-Token Prediction paradigm, which models token dependencies more realistically in actual language models, addressing a limitation in previous ICL studies.
2. This paper presents data-dependent and topic-dependent PAC-Bayesian generalization bounds for auto-regressive next-token prediction loss.
3. This paper presents a theoretical view about ICL emergence, and demonstrates that ICL emerges from the generalization of sequences and topics.

### Weaknesses
1. Some motivation of the paper is confusing and not clarified enough. The author claims that the i.i.d. setting is unrealistic in language tasks, but Section 3 directly shifts the paradigm towards the language model without an explanation of how to break through the i.i.d. limitation. Specifically, it is unclear how the theoretical framework transitions from the limitations of i.i.d. data to the complexities of auto-regressive next-token prediction, which introduces dependencies between tokens that are not present in the i.i.d. setting. The paper needs to explicitly address how the proposed framework handles these dependencies and how it differs from prior work that assumes i.i.d. data.
2. The experimental setting is not fully discussed, including the detailed information about GINC datasets (number of entries; example; split;), the initialization of GPT-2 (from-scratch or pretrained), the method to change sequence length on real-world datasets (directly mask the token that exceeds the specified length, ignoring the semantic?). The lack of detail makes it difficult to reproduce the results and assess the validity of the experimental findings. For example, the paper does not specify how the GINC dataset is split into training, validation, and test sets, nor does it provide examples of the generated sequences. Furthermore, the paper does not clarify whether the GPT-2 model is initialized from scratch or using pre-trained weights, which can significantly impact the results. The method of truncating sequences to change sequence length, without considering semantic context, is also a concern.
3. The paper does not adequately justify the bounded gradient assumption in the context of Transformers and large language models. While the authors claim that it is a common assumption, the highly non-linear nature of Transformers, with multiple layers of non-linear transformations, could lead to highly sensitive outputs with respect to input changes. The paper needs to provide a more detailed justification for this assumption, possibly by discussing the Lipschitz constant of the Transformer architecture or by citing relevant empirical studies that support this assumption.

### Questions
1. Can this result be directly adapted to the in-context learning paradigm in recent large language models? Since the difference in the empirical loss, is there still a gap between them?
2. Is the Bounded Gradient a strong assumption for the Transformer and recent large language model? After multiple layers of nonlinear superposition in the Transformer, the network output may be highly sensitive to input changes.
3. How do you define the topic examples in your experiments? Can you give some examples of the topic in linear dynamic systems and GINC?

### Soundness
3

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
2

### Summary
The paper critiques existing ICL theoretical analyses for relying on unrealistic i.i.d. (independent and identically distributed) assumptions and lacking an explanation of ICL emergence. To address these issues, the authors propose an auto-regressive next-token prediction (AR-NTP) framework, which mirrors real-world language learning by considering token dependencies within prompts. The paper introduces a pre-training and ICL framework, analyzing generalization bounds using PAC-Bayesian techniques and exploring how ICL arises through generalization of sequences and topics. The findings are validated through experiments on synthetic and real-world datasets, concluding that ICL capabilities emerge from the strong generalization of LLMs trained on diverse sequences and topics.

### Strengths
This paper presents an original contribution to the understanding of in-context learning (ICL) by introducing the auto-regressive next-token prediction (AR-NTP) framework. The paper seek to addresses two major limitations in the current literature: the i.i.d. assumption in prompt tokens and the lack of an explanation for how ICL emerges from pre-trained large language models (LLMs). By shifting the focus to token dependencies in AR-NTP and offering a novel pre-training and ICL framework, the authors provide a fresh perspective on ICL emergence through generalization. The originality stems from the use of PAC-Bayesian generalization techniques, and the proposed framework opens up new avenues for exploring token dependencies and generalization beyond previous work that relied on supervised function learning. The authors also provide theoretical results that are supported by empirical experiments on both synthetic and real-world datasets, enhancing the quality and rigor of their contributions.

the paper is well-structured and flows well, guiding the reader through complex concepts such as generalization bounds, topic-dependent priors, and PAC-Bayesian techniques without overwhelming them with technical jargon. The theoretical framework is detailed yet accessible, and the results are presented in a way that is easy to follow, particularly with well-placed diagrams and examples. The significance of the work lies in its ability to explain ICL as an emergent property of pre-trained LLMs, which has strong implications for both academia and industry. The results contribute to understanding why larger models exhibit better ICL performance and provide concrete recommendations for improving model generalization.

### Weaknesses
While the paper makes significant strides in addressing limitations in existing ICL literature, there are several areas where the work could be strengthened. One key weakness lies in the assumptions behind the AR-NTP paradigm. Although the shift from i.i.d. settings to token-dependent sequences is crucial, the paper could have provided a more thorough discussion on the potential challenges this poses for practical implementation. For example, the dependency between tokens may introduce computational inefficiencies in scaling to larger datasets or more complex sequences, which could affect the generalization results. A more detailed exploration of how to handle these challenges efficiently during training would improve the practical applicability of the proposed framework.

Altough the paper is mostly theoretical, there is no enough experiments in the main paper. Especially the claim that topic prior in pre-training would affect the ICL does not get justification. Appendix contains some synthetic topic results using GPT-2 but that is a bit too hand-wavy.
The authors validate their theoretical claims with experiments on synthetic and real-world datasets, which is commendable, but the diversity of the real-world datasets could be expanded. For example, the selection of datasets appears limited to common language tasks like sentiment analysis and topic classification. Including a wider variety of tasks such as training on Zipfian data but test on distributions like MMLU and GSM8k would better demonstrate the generalization and applicability of the proposed AR-NTP paradigm across different domains. Moreover, while the results show that increasing the number of pre-training topics, sequences per topic, and sequence length improves model performance, the experiments would benefit from more ablation studies.

Lastly, while the paper provides theoretical insights into how ICL emerges from pre-training, the connection between theory and practice could be more tightly integrated. The authors propose that ICL arises from excellent generalization of sequences and topics, but the specific impact of pre-training data diversity, model size, and optimization iterations could be made clearer. The paper could explore more explicitly how different pre-training regimes—such as training on more complex or diverse datasets —might affect ICL performance in practice. This would provide practitioners with clearer guidelines on how to optimize their pre-training procedures for better ICL outcomes. In particular, the paper could explore limitations of their generalization bounds when models are applied in low-resource environments, where generalization may suffer in no enough ICL examples are given or the pre-training FLOPs are constrained.

### Questions
Why particularly choose PAC-Bayesian framework for ICL? There are numerous works study ICL using statistical frameworks like [1]
Why not based on uniform convergence or algorithmic stability, could help situate the results within a broader landscape of generalization theory?

[1] Transformers as statisticians: Provable in-context learning with in-context algorithm selection

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes theoretical analysis to explain the ICL abilities exhibited by LLMs. The analysis establishes data-dependent, topic-dependent and optimization dependent generalization bounds for pre-trained LLMs, investigating that ICL merges from the generalization of sequence topics. The paper also present empirical evidence to support the theoretical implications.

### Strengths
1. The breakdown of pre-training loss into data and topic level optimization is interesting and inspiring. It is capable of identifying two sources of pre-training loss, sequences and topics. 

2. The theoretical bounds and empirical evidence are aligned: with longer sequence length, more number of sequence and more number of topics, the ICL loss is smaller and performance is better.

### Weaknesses
1. One concern centers around the controlled experiment of the empirical investigation. Given the data is sampled from the topic and token distribution, with more topic or more sequence, or longer sequence, it implies more training data, so it is expected that the ICL loss drops and that performance increases. It is unclear that the loss change can be attributed to the three sources or simply data size, under the current experiment setup. Specifically, when varying the number of topics (K), sequences (N), or sequence length (T) independently, the total training data size changes, making it difficult to isolate the effect of each variable. For example, increasing K while holding N and T constant results in a larger overall training set, which could inherently lead to better performance regardless of the topic diversity. This makes it challenging to attribute performance gains solely to the theoretical constructs of topic diversity, sequence quantity, or sequence length.

2. Although the theoretical analysis establish the bounds of ICL loss, but the results apply to general prompt, rather than in-context examples only. It also implies that the ICL loss should be lower and performance should be better with more training data (in terms of topic and sequence). But only well-structured in-context samples work empirically. I am uncertain if the presented theory is sufficiently tailored to address the problem of ICL. The theory does not explicitly account for the specific structure of in-context learning examples, where the order and relevance of examples significantly impact performance. The current theoretical framework does not differentiate between random prompts and carefully constructed in-context examples, which is a critical distinction in practice.

3. Now the empirical investigation is omitted from the main paper but experiment setup discussion remains. I suggest to put the main analysis of empirical result into main paper and defer some theoretical analysis into appendix.

### Questions
1. Did you control the training size for various topic size, sequence length and sequence amount?

### Soundness
2

### Presentation
2

### Contribution
3
