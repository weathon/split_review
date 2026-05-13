# White-Box Text Detectors Using Proprietary LLMs: A Probability Distribution Estimation Approach

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
Large language models (LLMs) can generate text almost indistinguishable from human-written one, highlighting the importance of machine-generated text detection. However, current zero-shot techniques face challenges as white-box methods are restricted to use weaker open-source LLMs, and black-box methods are limited by partial observations from stronger proprietary LLMs. It seems impossible to enable white-box methods to use proprietary models because the API-level access neither provides full predictive distributions nor inner embeddings. To break this deadlock, we propose Probability Distribution Estimation (PDE), estimating full distributions from partial observations. Despite the simplicity of PDE, we successfully extend white-box methods like Entropy, Rank, Log-Rank, and Fast-DetectGPT to latest proprietary models. Experiments show that PDE (Fast-DetectGPT, GPT-3.5) achieves an average accuracy of about 0.95 across five latest source models, improving the accuracy by 51% relative to the remaining space of the baseline (as Table 1). It demonstrates that the latest LLMs can effectively detect their own outputs, suggesting advanced LLMs may be the best shield against themselves. We release our codes and data at https://github.com/xxx/xxxxxx.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors consider the task of artificial text detection (ATD); one commonly-used approach here is to use a model itself to detect its own output. This scheme is inapplicable to modern proprietary LLMs because they don’t give access to their internal states. To address this issue, authors introduce an extension to existing white-box detection methods that rely on the distribution of model-assigned probabilities to each token. The authors propose to substitute token probability distributions by their density estimations (PDE) based on probabilities of the few most probable tokens and a hypothesis on the shape of the rest of the distribution. They test various candidates for the hypothetical token probability distributions. On example of Fast-DetectGPT authors illustrate the scheme of PDE-approach application to ATD solutions. Authors perform numerous experiments on different types of texts produced by various generating models and show the high performance of their method. They also perform ablation study, investigate the effect of different prompt designs, and explore the effect of paraphrasing adversarial attack.

### Strengths
**S1.** The proposed approach shows promising results at increasing the efficiency of previously existing Artificial Text Detection methods against modern generating models.

**S2.** The text of the article is well-written and was easy to follow; extensive mathematical explanations are given.

**S3.** Proposed method is robust against some common adversarial attacks (e.g., automatic paraphrasing of generated texts).

### Weaknesses
**W1.** The proposed method still requires the internal information from the source models – model-assigned probabilities of K most probable candidates for each token. Some proprietary models might not provide such information.

**W2.** The novelty of the proposed method compared to `vanilla’ Fast-DetectGPT is somewhat ambiguous. Essentially, this work proposes to compute statistics not from probability distribution over the entire dictionary (as in Fast-DetectGPT), but from probabilities of K most likely tokens and some assumptions on the distribution. 

**W3.** Datasets used for experiments are small: 150 pairs of human-written/AI-generated texts each. In particular, there are concerns regarding the generalization capabilities of the proposed. Also, given data is not large enough to properly train the baseline methods (RoBERTa).

**W4.** AUROC is the only quality metric reported. It has a number of limitations, and alone it is not enough to accurately compare different models. This experimental setup does not allow properly accessing the generalization capabilities of the model and discriminating different types of their biases. 
For reference, one of the common practices for Zero-shot AI-content detector evaluation is to set a threshold (by fixing FP-rate) on some 'training’ data (i.e., the probability of falsely declaring human-written text as AI-generated) and then report metrics (TPR/TNR/detection accuracy/etc.) on the `evaluation’ data.

**W5.** It is unclear how good this method would generalize across different styles of texts. As it follows from the text, all reported experiments were performed only in “in-domain” setup. Datasets used in this work are very small and style-specific (e.g., scientific-like *PubMed* and free-form fictional *Writing*). It is well known that some classifiers (like RoBERTa-based) excel on `familiar’ data but experience a significant drop in performance when they face texts of styles or genres unseen during training. From the presented results it is impossible to say whether the proposed method will fall into the same pitfall or not.

### Questions
**Q1.** DetectGPT (and many other methods) has a known limitation of a drastically high rate of false alarms on texts written by people who are not fluent in English; for example, by undergraduate students preparing for the IELTS exam [1]. Have you considered such scenarios?
This issue becomes more and more crucial as AI-content detection tools become part of automatic anti-plagiarism systems in education in countries where English is taught as second-language.

> [1] W. Liang, M. Yuksekgonul, Y. Mao, E. Wu, and J. Zou. GPT detectors are biased against non-native English writers. In ICLR 2023 Workshop on Trustworthy and Reliable Large-Scale Machine Learning Models.

**Q2.** How big is the difference in performance between your method (PDE + Fast-DetectGPT) and the original Fast-DetectGPT on various data?

**Q3.** Table 3 states that you use RoBERTa-large model as a baseline for experiments on robustness over languages. This is incorrect because RoBERTa was trained only on English-language data. Did you mean XLM-RoBERTa- large, which is actually multilingual, there?

**Q4.** Could you please specify in more detail the experimental setup for assessing the robustness against paraphrasing attacks (Appendix E.1)?

**Q5.** What are the limits for cross-model transferability of your method? (i.e, the proposed method works well when transferred from ChatGPT to GPT-4 and vice versa, but what would happen when it faces older models like GPT-2 or XLNet as source models?)

**Other remarks:**

-	Table 2 caption: instead of “average accuracies”, there should be “average AUROC”. In general, please revise your usage of the phrase “detection accuracy”, because right now it is difficult to understand whether you mean Accuracy (that is not reported by value anywhere) or AUROC.

-	lines 485/511: technically, PHD is a "black-box" method. It does not require the knowledge of what model was used to generate text; it uses inner embeddings from a fixed auxiliary encoder transformer.

-	Code to reproduce the experiments was not provided (this could be done in attachments to submission in or via an anonymous Github repository).

-	Please fix lettercases in paper titles in the references (e.g., “Fast-detectgpt: Efficient zero-shot detection of machine-generated text via conditional probability curvature” should be “Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature” in line 552; and so for other articles).

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
5

### Summary
The paper considers the topic of detecting the texts, generated by closed (proprietary) LLMs. Authors suggest several ways to approximate the distribution of token probabilities of those closed LLMs accessible via API (such as GPT-4), knowing only the probabilities of top-K or even top-1 tokens. Using these distributions, authors managed to emulate several methods of LLM-generated text detection (i. e. Fast-DetectGPT, Entropy, etc) as if they had access to these LLMs. Using these methods upon approximated distributions, they overperformed analogous methods based on distributions of GPT-Neo-2.7B.

### Strengths
- The topic of LLM-generated text detection is important.
- The idea of the paper is worth considering.
- Authors check how their detectors behave when they fix a low False Positive Rate, that is a good practice.
- Authors check their detectors against paraphrasing attacks and consider the influence of various prompts.

### Weaknesses
The major drawbacks of the paper lie in its experimental setup.
- The amount of machine-generated texts in the datasets in Table 2 (which is supposed to contain the main results) is extremely small. E.g., as far as I understood from part 3.1 SETTINGS, for each sub-domain "XSum", "Writing", and "PubMed" in Table 2, only 150 machine-generated texts vs 150 human-written texts are used. It's hard to tell anything for sure from such a small amount of examples, and the results may be very noisy. The authors need to increase their datasets to get reliable results.
- The choice of baseline open LLM (i.e. GPT-Neo-2.7B) for applying methods like Fast-Detect and Likelihood seems unreasonable because GPT-Neo-2.7B is weak compared to the newer open LLMs of comparable size. I would recommend adding at least the Phi-2 model (it also has 2.7B parameters) as a base for Fast-Detect, Likelihood, and other similar methods because its perplexity scores seem to be good in LLM-generated text detection (AI-generated text boundary detection with RoFT, Kushnareva et. al, 2024). Besides, many bigger models look like fair candidates for a good baseline (e.g. LLaMA 3.2 and many others).
- AUROC scores in the Tables seem to be very high both for the best baseline and for the best method suggested by the authors. It means that the task statement is too easy. It would be good to add more complicated data, where all the methods will struggle, and the difference between methods will become more clear.

Minor remarks about the presentation:
- Overusing the appendices: appendices D.1 and E look more suitable for the main text;
- Typos: log p(x|x) in Figure 1 and Equation (2);
- Figure 1 contains an extremely bright red color, it is hard to look at it. Please, change it to a softer color.

**UPDATE**: The first two of my concerns were addressed, so I updated my main score from 3 to 5. I adjusted scores about "soundness" and "presentation" accordingly.

### Questions
- Line 138-140, Equation 2: why do you call this $d(x, p_\theta)$ value "curvature"? It doesn't seem to have a meaning of a curvature. Maybe "skewness" would be better word?
- Only AUROC is reported as a metric for comparison in the Tables. It would be interesting to see, what are the accuracy scores for all methods (for some fixed threshold)?
- Are there any differences between "Likelihood" method and perplexity scores?

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
3

### Summary
The paper proposes Probability Distribution Estimation (PDE), a method for enhancing the capabilities of white-box text detection methods, such as Fast-DetectGPT, in identifying machine-generated text from proprietary large language models (LLMs) like GPT-4 and Claude-3. PDE extends traditional white-box methods to proprietary models by estimating full probability distributions from limited API access. The authors demonstrate that using PDE with Fast-DetectGPT achieves improvements in detection accuracy over previous methods.

### Strengths
- A thorough explanation of the PDE approach, describing its implementation across different parameterization methods (e.g., Geometric, Zipfian).
- Extensive ablation studies and analyses (distribution choices, top-K probabilities, language variations). This adds depth and clarity to the method’s application across proprietary LLMs.
- Completing datasets with new models that authors will release

### Weaknesses
- The evaluations are conducted on limited datasets (150 pairs), potentially restricting the findings’ generalizability across more diverse or larger data sources. There are more samples for other models in the original M4 dataset.
- While PDE is an effective enhancement, it primarily focuses on density estimation and integration with existing detection methods rather than introducing a fundamentally new detection approach.
-  Although PDE improves upon Fast-Detect, the accuracy increase is relatively modest, raising questions about the practical advantage of this added complexity in real-world applications. In table 2 you report Fast-Detect (GPT-J/Neo-2.7) which has relatively good. It hints that it may be better to use bigger or newer open models (like Qwen2.5-1.5B or Llama3) than to use PDE to proprietary models.

### Questions
- Did you try to Fast-Detect with other open models rather than GPT-J/Neo-2.7? Could you please scores from newer/larger models for better comparison?
- The evaluation dataset is very small; did you try other datasets? I believe it would be better to perform testing on bigger datasets, for example the original M4. 

Small remarks:
- line 101-102: "(↑ more than 25%)" might confuse readers. Better to add "relative to the remaining space"
- "*" in equations looks strange
- line 297: gpt-35-turbo -> gpt-3.5-turbo

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
To enable existing white-box methods to proprietary models, the authors propose Probability Distribution Estimation (PDE), extending methods like Entropy, Rank, Log-Rank, and Fast-DetectGPT to latest closed-source LLMs. This work uses only the top-K probabilies returns by the API to estimate the necessary metrics (such as mean and variance in DetectGPT). They estimate the probs after rank K using parametrized distribution (which token each pk refers to is not important). Three algorithms are tested: Geometric, Zipfian, and MLP.

It is applied to ChatGPT (gpt-35-turbo) (OpenAI, 2022), GPT-4 (gpt-4) (OpenAI, 2023), Claude3 Sonnet (claude-3-sonnet-20240229) and Opus (claude-3-opus-20240229) (Anthropic, 2024), Gemini-1.5 Pro (gemini-1.5-pro). The results is quite promising, and suggests larger LLMs can be universal detectors.

### Strengths
I think the idea of estimating unknown probs using Geometric, Zipfian, and MLP is very interesting.

The idea can be applied to different white-box methods.

The performance are quite promising.

### Weaknesses
Comparing to this proprietary and estimation approach, why not use open-source large model such as LLaMA as the scoring model? This paper did not mention models like LLaMA at all. If authors can give me a convincing answer or add some comparison experiment, I'll consider raise score.

It still assumes some partial information from the API. But I do agree this setting is realistic and interesting.

Some parts of the writing can be improved (refer to my questions).

### Questions
Line302 : I did not understand what's the difference between source model and scoring models… My current understanding is that the authors want to argue that a good scoring model can detect machine-generated text from a wide range of LLMs, is my understanding correct? I think if you can add some text to explain that will be helpful.

Figure1: I think the notation p(x|x) is weird.

Line293: What do you mean by "generate corresponding text from source LLMs for each sample"? Do you mean generate text with the same prefix?

### Soundness
3

### Presentation
3

### Contribution
3
