# The Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model

- Decision: Accept
- Scores: 6, 6, 3, 6

## Abstract
Large language models (LLMs) have shown significant multilingual capabilities. However, the mechanisms underlying the development of these capabilities during pre-training are not well understood. In this paper, we use code LLMs as an experimental platform to explore the evolution of multilingual capabilities in LLMs during the pre-training process. Based on our observations, we propose the Babel Tower Hypothesis, which describes the entire process of LLMs acquiring new language capabilities. During the learning process, multiple languages initially share a single knowledge system dominated by the primary language and gradually develop language-specific knowledge systems. We then validate the above hypothesis by tracking the internal states of the LLMs through identifying working languages and  language transferring neurons. Experimental results show that the internal state changes of the LLM are consistent with our Babel Tower Hypothesis. Building on these insights, we propose a novel method to construct an optimized pre-training corpus for multilingual code LLMs, which significantly outperforms LLMs trained on the original corpus. The proposed Babel Tower Hypothesis provides new insights into designing pre-training data distributions to achieve optimal multilingual capabilities in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a Babel tower hypothesis for the evolution of multi-lingual code LLM, that is continual pre-training a monolingual code LLM to master a new language will go through translation, transition, and stabilization stages. The authors demonstrate the evolution process of a python LLM based on GPT2 for new languages PHP and C#, revealing the best performance achieved at the translation stage.  Based on the observation the authors propose an algorithm to estimate the optimal distribution of the training corpus for different languages based on a linear hypothesis of the training loss and the monolingual system. The authors conduct experiments for new languages PHP, C#, Go, and C++ for HumanEval and MBXP, suggesting better performance compared to a baseline data distribution.

### Strengths
1. Overall this paper is well organized and the topic is interesting. The authors justify their hypothesis in a clear way.

2. The authors make a strong analogy of the learning process to human acquisition of new languages, and present some well-designed results including the evolution process and the transition of the internal states of LLM. Also, they apply the transition for optimization of corpus distribution, which could be significant for training of multi-lingual LLMs.

### Weaknesses
1. The paper lacks some detailed demonstration of the crucial parts of their claims. Please refer to my questions.

2. When presenting the methodology, I believe the authors make some important assumptions and analogy without further justification, which might make the presentation less persuasive. Please also refer to my questions for details.


1. In Fig 2 the authors show the evolution of performance of new languages, however, it is also important to show the performance of Python to illustrate the impact on the learned languages.

2. Could the authors show some example of python-specific problems which are crucial to define the knowledge transferring procedure?

3. The authors define a linear relationship between the training loss and estimated portion of the python system as in eq (2). Could the authors clarify: (1) how to calculate the loss which might consist of python data only; and (2) further justification of the relationship other than results in Fig 6 and 7 to demonstrate the scalability of this hypothesis.

4. If I understand it correctly, the authors assume there is no intervening impact between different language during learning procedure. Both the evidences to demonstrate the learning stages of the new language and the proposed optimal data distribution are base on this assumption. Could the authors show some solid justification for this assumption?

5.  The authors only present the results with a baseline distribution in Table 2. I wonder if it is comparable to other optimized data distributions.

### Questions
1. In Fig 2 the authors show the evolution of performance of new languages, however, it is also important to show the performance of Python to illustrate the impact on the learned languages.

2. Could the authors show some example of python-specific problems which are crucial to define the knowledge transferring procedure?

3. The authors define a linear relationship between the training loss and estimated portion of the python system as in eq (2). Could the authors clarify: (1) how to calculate the loss which might consist of python data only; and (2) further justification of the relationship other than results in Fig 6 and 7 to demonstrate the scalability of this hypothesis.

4. If I understand it correctly, the authors assume there is no intervening impact between different language during learning procedure. Both the evidences to demonstrate the learning stages of the new language and the proposed optimal data distribution are base on this assumption. Could the authors show some solid justification for this assumption?

5.  The authors only present the results with a baseline distribution in Table 2. I wonder if it is comparable to other optimized data distributions.

### Soundness
3

### Presentation
2

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
This paper investigates the multilingual capabilities of large language models (LLMs), specifically focusing on how a monolingual code LLM trained in Python can integrate additional programming languages, such as PHP, C#, Go, and C++. 

Analyzing the model's performance on code problem-solving tasks, the study proposes a hypothesis, termed the "Babel Tower Hypothesis," suggesting that learning new languages involves three phases: 
 1. translation
 2. transition 
 3. stabilization

The hypothesis is tested through an analysis of working languages and language-transferring neurons. 
Additionally, the paper proposes a method to construct an optimal distribution of languages during pre-training to enhance multilingual performance.

### Strengths
1. This paper is clearly written, making it easy to read and follow.

2. The study’s perspective and findings are intriguing, with well-designed experiments and thorough analysis that convincingly support the conclusions. 

3. It achieves good code-LLM perfermance by experimenting with pre-training data distribution.

### Weaknesses
1. The scope of this paper is a bit limited, as it focuses exclusively on code LLMs. Due to the unique characteristics of programming languages, the findings may not be easily applicable to natural languages.

2. The scenario explored is somewhat simplistic, focusing mainly on extending a primary LLM (Python in this case) to additional languages. It remains unclear whether the hypothesis would still hold if a different primary language were used.

3. Some parts of this paper are unclear to me:
 - In sections 4.2.1 and 4.2.2, it is not well explained how $P(l)$ relates to $\alpha$ and $\beta$ and how $P(l)$ determines the optimal number of tokens for the target languages. 
 - Additionally, according to equation (2), the proportion $P(l)$ cannot exceed 1. What happens if there is sufficent amout of training data for the target language?
 - The hypothesis primarily addresses the extension of a dominant language to one additional language. However, in section 4.3.3, the strategy of training with five languages from scratch also appears to yield better performance. Why is this the case?

### Questions
Typo:
 - line 385 "Rrecoding" -> "Recording"

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This submission explores how Large Language Models (LLMs) develop multilingual capabilities. The authors propose a three-stage learning process: translation, transition, and stabilization. They experimented with code LLMs by tracking the working languages and language transferring neurons during pre-training.

### Strengths
The mechanisms behind the development of multilingual capabilities during pre-training is an important area.

### Weaknesses
 * The submission's use of the term "multilingual capabilities" is unclear. It seems to refer to the model's capacity to understand multiple programming languages, rather than the more common interpretation of "multilingual" as understanding multiple natural languages. Since the programming languages studied are all English-based, the method doesn't address the orthographic differences of various natural languages. Instead, the experiments reduced to focus on how the semantics of programming languages are developed during pre-training.

* The methodology's flaws undermine the hypothesis presented. The claim that multilingual programming language capabilities are primarily developed during pre-training is unconvincing. It's likely that fine-tuning plays a significant role, and a more comprehensive mechanism should be considered.

* Additionally, the assertion that Python is the dominant language due to its widespread use lacks evidence and requires further clarification.

### Questions
Why combine the concepts of multiple natural languages and multiple programming languages?

Note: Authors should not reveal their identities. Descriptions like "Specifically, we conducted preliminary experiments to analyze how monolingual LLMs learn a new language by continual pre-training the monolingual LLM on the corpus with the new language (Zheng et al., 2024)" should be revised to remove identifying information.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work focuses on LLM multilingual capability (in terms of programming language instead of natural language). The authors observed a 3-stage division during the continual learning setting (i.e. pre-train on Python, and continue pre-training on PHP/C#...): (1) translation stage, where the performance of the new language improves and the Python system is dominated in the LLM and the generation in the new language primarily relies on the Python system; (2) Transition Stage: the performance of the new language begins to decline while it gradually forms its own system; (3) Stabilization Stage: the performance of the new language stabilizes, and the generation in the new language depends on its own system. Based on such observation, the authors proposed the “Babel Tower Hypothesis” which depicts the language learning process in multilingual pre-training - a single knowledge system was first formed, followed by forming language-specific systems.

To support this claim, the authors used 2 methods to evaluate the internal state of the LLMs during pre-training, (1) working languages and (2) language transferring neurons. These metrics show similar 3-stage trends. Finally, the authors proposed to adjust the pre-training data distribution to make different languages to achieve optimal states concurrently. Empirical results show that this optimized data distribution outperforms the original data distribution in terms of the HumanEval and MBXP benchmarks.

### Strengths
1. The authors investigated the training dynamics for different data setup, which is intriguing.
2. I like the idea of checking LLM internal states using "working languages" and "Language transferring Neurons" concepts.
3. Experiments are solid.

### Weaknesses
1. The presentation of Algorithm 1 and subsequent experiments and results in Section 4.3.1 and 4.3.2 needs some clarification. The last line in Algorithm 1 states that the number of tokens in the target language is computed using $P(l_j)$ and $\eta_{python}$ based on Eqn 3. However, Eqn. 3 does not have a $P(l_j)$ term. 
2. Assuming the estimated num of tokens are obtained, I am still confused about the results in Fig. 6 and Fig. 7. For example, what do “PHP predicted” and “PHP Actual” mean? My understanding is that you are estimating the data proportion in pre-training corpora, not the performance on HumanEval. Why there are multiple results for multiple data proportions (i assume there should be an optimal one given by Algorithm 1.) And why there are much more “PHP predicted” dots than “PHP Actual”? I may have misunderstand something, but i think the presentation of these sections could be made clearer.
3. Section 4.3.3 states that the optimized pre-training data distribution is formed by “we randomly down-sampled the token quantity for PHP and C# to 5 billion and 10 billion tokens, respectively, while keeping the token quantities for the other languages unchanged ”. I’m quite surprised that training on a smaller amount of data provides such a big performance improvement in Table 2. What is the optimized data distribution?  The models are trained on the data collected by the authors themselves (as described in Section 3.1). Have you performed any checks on data quality? Is it possible that these results are actually due to some bad quality data (e.g. noisy/incorrect codebases), instead of the claimed knowledge transfer between languages?

### Questions
1. Section 4.3.3 states that the optimized pre-training data distribution is formed by “we randomly down-sampled the token quantity for PHP and C# to 5 billion and 10 billion tokens, respectively, while keeping the token quantities for the other languages unchanged ”. I’m quite surprised that training on a smaller amount of data provides such a big performance improvement in Table 2. What is the optimized data distribution?  The models are trained on the data collected by the authors themselves (as described in Section 3.1). Have you performed any checks on data quality? Is it possible that these results are actually due to some bad quality data (e.g. noisy/incorrect codebases), instead of the claimed knowledge transfer between languages? 
2. I think a better set of experiments may be to use existing open-source multilingual datasets, and show that the proposed optimized data distribution can produce stronger pre-train models. In this case the comparison can include existing coding LLMs. 
3. Further, programming languages are very different from natural languages due to their highly structured form. Based purely on programming languages, it is not clear whether the “Babel Tower Hypothesis” is generalizable or not. It may be more informative if there are more experimental results on natural languages to support this general hypothesis - though, I understand the difficulty due to resource demands for these experiments - a smaller scale of multilingual training data is understandable.

### Soundness
3

### Presentation
2

### Contribution
3
