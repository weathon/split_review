# Looking Beyond the Top-1: Transformers Determine Top Tokens in Order

- Decision: Reject
- Avg Score: 6.40
- Scores: 8, 5, 8, 8, 3

## Abstract
Understanding the inner workings of Transformers is crucial for achieving more accurate and efficient predictions. In this work, we analyze the computation performed by Transformers in the layers after the top-1 prediction has become fixed, which has been previously referred to as the ``saturation event''. We expand the concept of saturation events for top-$k$ tokens, demonstrating that similar saturation events occur across language, vision, and speech models. We find that these saturation events happen {\emph{in order}} of the corresponding tokens' ranking, i.e., the model first decides on the top ranking token, then the second highest ranking token, and so on. This phenomenon seems intrinsic to the Transformer architecture, occurring across different architectural variants (decoder-only, encoder-only, and to a lesser extent full-Transformer),  and even in untrained Transformers. We propose an underlying mechanism of task transition for this sequential saturation, where task $k$ corresponds to predicting the $k$-th most probable token, and the saturation events are in fact discrete transitions between the tasks. In support of this we show that it is possible to predict the current task from hidden layer embedding. Furthermore, using an intervention method we demonstrate that we can {\emph{cause}} the model to switch from one task to the next. Finally, leveraging our findings, we introduce a novel token-level early-exit strategy, which surpasses existing methods in balancing performance and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work expands the top-1 saturation event to top-k tokens and finds a significant phenomenon that there is an order law between the saturation events and the corresponding tokens' ranking. Additionally, such phenomenon is rooted in transformer architecture, which happens across all modality and even in untrained models. With the finding of such order law on the saturation events, an efficient decoding method is proposed for early-exit for next-token prediction.

### Strengths
1. The concept and research problem in this work is very novel. It significantly extends the range of saturation event to the top-k token level. 

2. The findings are very brute-force, which can be easily used for early-exit decoding for next token prediction acceleration without introducing much additional computation. And such decoding strategy is general and easily applied across all transformer based LLMs.

### Weaknesses
1. The evaluation of this method is limited in its size and targeted models. 60k tokens and 100 texts are a too small evaluation set size for a robust conclusion. GPT2-XL is also not well-trained and the experiments on Llama-3 is more recommended. If the saturation event for top-k tokens only happens at very late layers, then the acceleration ratio is not that ideal compared with GPT2-XL experiments. CNN summarization task is a very basic task for recent LLMs, while the benchmarks of MMLU, Hellaswag are more recommended for study and experiments.

2. The experiments on vision and speech transformers are great demonstrations to your claim on the generality of your findings but have no contribution to real applications like decoding acceleration. Maybe you can consider to remove them into appendix and enlarge your study on language model part.

3. I am very interested in whether such saturation event happens on all tokens in the context or just a few tokens? If it does not happen on all tokens, how you can deal with the prediction towards these non-saturation tokens?

### Questions
1. I recommend to change the definition of "task" to other words like "process". The concept of "task transition" makes me feel like there is some generality in different tasks like summarization, QA, dialogues, etc.

2. The experiments on vision and speech transformers are great demonstrations to your claim on the generality of your findings but have no contribution to real applications like decoding acceleration. Maybe you can consider to remove them into appendix and enlarge your study on language model part.

3. I am very interested in whether such saturation event happens on all tokens in the context or just a few tokens? If it does not happen on all tokens, how you can deal with the prediction towards these non-saturation tokens?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper is to understand the inner workings of transformers to achieve more accurate and efficient predictions. Authors expand the concept of saturation events for top-k tokens, demonstrating that similar saturation events occur across language, vision, and speech models. The experiments show that it is possible to predict the current task from hidden layer embedding. Furthermore, authors use an intervention method to cause the model to swithc from one task to the next.

### Strengths
1. This paper is well written with clear illustrations.
2. There are extensive experiments across different modalities, such as vision, language, and speech.
3. Compared with two baseline models, the proposed method demonstrates improved performance.

### Weaknesses
1. Compared with Line 275 and L 276, the proposed method seems to be model-specific. While the results in Table 1 show the layer embeddings contain information about the task number, such information may only work for language, but not vision and speech. The accuracy differences across modalities raise concerns about the method's general applicability. The fact that the language model achieves significantly higher classification accuracy (as implied by the response) suggests the method might be exploiting specific architectural features of language models, such as the number of layers, which are not consistent across vision and speech models. This makes the method less generalizable.

2. in Line 472, why the second token's saturation layer is at least "7" layers before the output? The hypothesis seems to be hand-crafted without any supportive evidence. The choice of '7' appears arbitrary, and the lack of a clear theoretical justification for this specific number undermines the robustness of the claim. There is no explanation of why a fixed number of layers would be universally applicable across different models and tasks. The authors should provide a more principled approach for determining the saturation layer.

3. In Table 2, the comparisons of different strategies are a little bit weak to support the claim. Is 40% accuracy a significant improvement compared to the baselines 35.9% and 37.5%? As these numbers are pretty low to have any real applications. The small absolute differences in accuracy, despite the statistical significance, raise concerns about the practical impact of the proposed method. The low overall accuracy suggests that the method may not be robust enough for real-world applications, and the improvements over baselines, while statistically significant, may not be practically meaningful.

### Questions
See the above weakness. The main concern is that the proposed method is quite heuristic and hand-crafted without enough supportive evidence. While the authors demonstrate the results across different modalities, it is difficult to evaluate the effectiveness of this method given the relatively low numbers.

### Soundness
2

### Presentation
3

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
This paper investigates the internal mechanisms of Transformers, particularly focusing on the computation performed after the top-1 prediction has been determined, a phenomenon referred to as the "saturation event." The authors expand the concept of saturation events to top-k tokens and demonstrate that these events occur in a ranked order across various modalities (language, vision, speech) and Transformer architectures. They propose a task-transition mechanism to explain this sequential saturation, where each task corresponds to predicting the k-th most probable token. The paper further shows that it is possible to predict the current task from hidden layer embeddings and to induce task transitions through interventions. Finally, the authors introduce a token-level early-exit strategy that improves performance and efficiency, outperforming existing methods.

### Strengths
1. The paper provides a fresh perspective on how Transformers process predictions beyond the top-1 token, which is a significant contribution to the field of model interpretability.
2. The study's scope extends across multiple modalities, enhancing the generalizability of the findings and demonstrating the robustness of the proposed mechanisms.
3. The authors back their claims with extensive experiments and provide empirical evidence supporting the task-transition hypothesis.
4. The paper not only has theoretic analysis but also explores practical applications, such as the early-exit strategy, which has potential implications for improving model efficiency and accuracy.

### Weaknesses
This is a suggestion rather than a weakness.

It would be great to discuss whether this is a fundamental solution for early exit problem. After all, it is ridiculous for us to let problems with all level of difficulties to go through all the layers. There must be a solution that significantly improve the inference efficiency of the current LLM through sparsity or early exit. Yet the solution proposed by this paper give only marginal improvement.

### Questions
Please see the weakness part. Highly appreciate if the author give some feedback.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
1) This study extends the concept of saturation from only the top-1 token to multiple top-ranked tokens, providing deeper insights into the computational processes within Transformer models.
2) Experiments across diverse domains, including text, vision, and speech, demonstrate the broad applicability of this sequential saturation mechanism.
3) Beyond observing this phenomenon, the authors propose an early-exit algorithm based on their findings, presenting a practical approach to enhance computational efficiency in Transformer models.

### Strengths
The paper is written in a clear and understandable manner, with a well-defined approach and valuable findings that go beyond observation to demonstrate practical benefits. I believe this is an good research, and with a few additional points, it would be well-suited for acceptance at the conference.

### Weaknesses
If the paper claims that these findings are unique to Transformers (as the title suggests), it should demonstrate that (1) this phenomenon does not occur in other architectures and (2) it consistently appears in recent, state-of-the-art models. Providing this evidence would make the paper much more logically sound and robust.

The practical applicability of the experiments in Sections 5.1 and 5.2 feels somewhat limited; further validation could enhance their real-world relevance. (For example, as shown in A.5, softmax and state cannot outperform ours even at the minimum speedup, which makes the comparison less compelling.)

### Questions
(1) Table 1 shows different chance levels for each model (e.g., 25% for Whisper-large vs. 20% for GPT2-XL and ViT-L/16) Could the authors clarify the reason for these differences?

(2) In Figure 3, how did the authors handle cases where two top-ranked tokens reach saturation at the same layer?

(3) Following up, how were such cases handled during classifier training?

(4) In Table 1, how was accuracy calculated in these scenarios?

(5) typo: 400lines: l1(s1) < l2(s2) => l1(s1) < l1(s2)

(6) Could the authors provide a comparison with other early exit methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores hidden states of intermediate layers of transformer-based models by mapping them onto the vocabulary space to extract ranking over tokens and analyzing their changes over the layers. The authors claim to identify sequential saturation events for top-k tokens, a phenomenon observed across language, vision, and speech models. They propose a type of discrete transition occurs during decoding.

### Strengths
Strengths:
The paper emphasizes the importance of investigating layer-wise states transition. The study tackles an important and interesting research question.

### Weaknesses
The hypothesis of “saturation events” is taken as granted without sufficient evidence. The mechanism in producing top-1 tokens in LLMs is influenced by various factors, including LLM architecture, contexts, and how an LLM reacts to an input. Based on practice shared by many colleagues in probing LLMs, transformers often alternate their top-1 token predictions, even in later layers, which undermines the claimed findings by this study.

The scope of the experiment is limited in terms of both the number and types of LLMs and tasks. This raises concerns about the generality of the findings. It is important to investigate both NLU and NLG tasks on a diverse range of LLMs under different regimes (e.g., pre-trained, post-trained, decoder-only, encoder-decoder) to ensure comprehensive insights. Instead of limiting to a small-scale LLM like GPT2-XL, the authors may consider exploring state-of-the-art (SOTA) LLMs, such as the LLAMA series, to broaden the scope of their research and enhance the robustness of the conclusions.

The use of ranks and central tendency in Figure 3 is confusing (i.e., why averaging ranks and std in figure 3). There are existing statistic rank tests the authors may leverage. The claimed sequential saturation pattern should be convincingly demonstrated.

The practical application of intervention is unclear, and the results shown in table 2 are not statistically significant. When you choose "Highest accuracy", how do you calculate it? Is it based on EM?

### Questions
as above

### Soundness
1

### Presentation
2

### Contribution
2
