# POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Balancing safety and usefulness in large language models has become a critical challenge in recent years. 
Models often exhibit unsafe behavior or adopt an overly cautious approach, leading to frequent overrefusal of benign prompts, which reduces their usefulness. 
Addressing these issues requires methods that maintain safety while avoiding overrefusal. 
In this work, we examine how the overgeneration of training data using advanced teacher models (e.g., GPT-4o), including responses to both general-purpose and toxic prompts, influences the safety and overrefusal balance of instruction-following language models.
Additionally, we present POROver, a strategy to use preference optimization methods in order to reduce overrefusal, via employing a superior teacher model's completions.
Our results show that overgenerating completions for general-purpose prompts significantly improves the balance between safety and usefulness. 
Specifically, the F1 score calculated between safety and usefulness increases from 70.8\% to 88.3\%. 
Moreover, overgeneration for toxic prompts substantially reduces overrefusal, decreasing it from 94.4\% to 45.2\%. 
Furthermore, preference optimization algorithms, when applied with carefully curated preference data, can effectively reduce a model's overrefusal from 45.2\% to 15.0\% while maintaining comparable safety levels.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a framework that aims to reduce overrefusal in Large Language Models (LLMs), while improving their safety. It involves finetuning on overgenerated training data from teacher models, such as GPT-4o, and preference optimization to guide models to respond in benign (but possibly seemingly toxic) prompts. Through experiments on Phi-3 7B, and various teacher models, the authors find that their method achieves significant reduction in overrefusal, while maintaining a balance between usefulness and safety.

### Strengths
* The paper tackles an important aspect of LLMs, aiming to investigate and improve their tradeoff in mainting (or even improving) their safety, without, however, undermining their usefulness due to overrefusal.
* The experiments presented are extensive; the effectiveness of the presented method has been evaluated on a variety of datasets and benchmarks related to safety and overrefusal.
* The experiments suggest that the proposed framework effectively results in a balance between usefulness and safety, without significantly undermining the general capabilities of the tested model.

### Weaknesses
 * As the authors acknowledge, a limitation of their study is that the proposed framework is only tested on a single model family and size (e.g., Phi-3 7B). In my opinion, while the results are promising, this limitation is significant; given that the framework relies on finetuning and preference optimization of pretrained models, testing it across diverse model families and scales would prove its effectiveness and generality. It is unclear to me whether the results would be similar in that case.
* Adding more fine grained experiments on the number of Added Safety Data (ASD) would make the claim that **the proposed method is effective without undermining the general abilities of the tested model** more convincing.

### Questions
* Although experiments on models with different scales were not included, how do you expect the models to behave, assuming that they come from the same family? Would the benefits saturate as the number of parameters increases?
* How sensitive is the proposed method in the choice of the hyperparameter $\tau$? Were the results vastly different accross your grid search?

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
This paper is concerned with training language models that output safe content but do not refuse too often. They test two algorithmic techniques to achieve this. First, they use overgeneration, which involves sampling multiple possible outputs and choosing the best responses for training. Second, they generate preference data pairs, based on responses that were unsafe/over-refusal vs not.

### Strengths
1. The paper tackles an important problem of making models safer.
2. The paper evaluates on multiple benchmarks with different step counts to give broader analysis.
3. The paper's algorithm seems straightforward to implement.

### Weaknesses
1. I believe the algorithms in this work have limited novelty. Rejection sampling and preference optimization are some of the most used tools for current fine-tuning and safety alignment, so the paper needs to provide novel analysis instead.
2. I'm confused about the empirical gains. It seems that in Table 1, the random selection GPT-4o baseline performs on par with the rejection sampling, indicating that the filtering step is not that crucial. Moreover, in Figures 3 and 4, training on GPT-3 seems to be extremely safe (though it does not solve over-refual).

In general, I suggest focusing on key empirical takeaways, ensuring that POROver improves upon simple baselines, and organizing the presentation of the results.

### Questions
1. Looking at Figure 5, it looks like there was little improvement on XSTest performance and a reduction in over-refusal for ORBench but no improvement in safety. Why do you think this is? Is it related to the training set being ORBench?

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
This paper studies the impact of rejection sampling for safety training on the model's tendency to over-reject. The results show in the student teacher setting distilling from a stronger model like GPT-4 to Phi-3 the over-refusal reduces from near 100% to 45% on OR-bench.

### Strengths
1) The approach shows strong empirical improvement and scopes a relevant problem of over-refusing. 

2) Although the results are shown only on the 7B Phi-3 model, it's done on a variety of seemingly-toxic datasets. 

3) The results are supported by human annotations in appendix C.

4) The paper speaks to the trade off on the amount of safety training data needed to achieve the level of desired safety. This is defined in terms of additional safety datapoints.

### Weaknesses
1) The approach involves distilling from already safety trained models. In particular, safety trained models that are also likely targeting similar datasets. The work shows gpt3.5 vs gpt4, but it would be more convincing to show Llama-3 as the teachers also, or an somewhat unsafe teacher model. The concern is that the observed reduction in over-refusal might be an artifact of the specific teacher models used, which are known to have strong safety guardrails, rather than a generalizable property of the proposed method. Using a less safety-focused teacher or a model with different safety training would help isolate the effect of the rejection sampling technique itself.

2) Added Safety Data (ASD) is only evaluated at three levels 0, 2K, and 20K. More data would be needed to defend the claim that there is a tradeoff between ASD and safety. I would expect it to saturate based on the amount of base diversity represented in the prompts. The current evaluation lacks granularity to properly assess the relationship between ASD and safety performance. It is unclear if the observed trend is linear, logarithmic, or follows a different pattern. A finer-grained analysis with more data points would be necessary to understand the true nature of this tradeoff and to determine the optimal amount of ASD for achieving the desired safety level.

3) The figures have misleading axis starting at 85% to 100% for instance in Figure 4. This makes the difference look bigger than it is. This choice of axis scaling obscures the actual magnitude of the observed changes and can lead to misinterpretations of the results. A more appropriate visualization would use a full axis range to accurately represent the data.

### Questions
1) Do these results replicate on a different model other than Phi-3? It would be especially convincing if it replicates on different sizes of the llama-3 family of models. 

2) Is it possible that Phi-3 already has safety training that's particularly prone to over-refusing?

3) I interpret ASD to be the number of datapoints added after rejection sampling. Is this correct? If so, this correlates with the extent the model is deviated from the base model.

4) It's not clear where 15%, 45.5%, and 95.5% come from in the abstract.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper titled "POROVER: IMPROVING SAFETY AND REDUCING OVERREFUSAL IN LARGE LANGUAGE MODELS WITH OVERGENERATION AND PREFERENCE OPTIMIZATION" presents a comprehensive study on enhancing the safety and reducing overrefusal in large language models (LLMs). The authors examine the impact of overgenerating training data using advanced teacher models on the safety and usefulness balance of instruction-following language models. They introduce POROver, a strategy that employs preference optimization methods to reduce overrefusal by leveraging completions from superior teacher models. The study demonstrates significant improvements in the F1 score between safety and usefulness, and a substantial reduction in overrefusal rates.

### Strengths
The paper introduces a novel approach to reducing over refusal in LLMs through overgeneration and preference optimization, which is a creative solution to a common problem in the field. The paper is well-written and the results are clearly presented, making it easy to follow the authors' reasoning and findings. The work addresses a critical issue in the deployment of LLMs, improving their safety without compromising their usefulness, which has significant implications for real-world applications.

### Weaknesses
 - The paper primarily focuses on a single model size and family (Phi-3), which limits the generalizability of the findings. While the authors acknowledge this limitation, the lack of experimentation with different model scales makes it difficult to understand how these methods would perform across the spectrum of model sizes. This is particularly important given that safety and overrefusal behaviors often vary significantly with model scale. Including experiments with both smaller (3-4B) and larger (70B+) models would provide stronger evidence for the method's broad applicability. The paper's evaluation methodology relies heavily on automatic metrics and a limited set of benchmarks. While the chosen benchmarks (e.g., OR-Bench, XSTest) are relevant, they may not capture the full spectrum of real-world scenarios where safety and overrefusal matter. Including evaluations on more diverse datasets, particularly those featuring different languages, cultures, and domain-specific contexts, would strengthen the paper's conclusions about the method's effectiveness.

- The computational analysis of the proposed methods is notably absent from the paper. The overgeneration approach with GPT-4 as a teacher model likely incurs significant computational costs, yet there's no discussion of the training efficiency or resource requirements. This omission makes it difficult for practitioners to assess the method's feasibility in production environments. A detailed analysis of computational overhead compared to standard fine-tuning approaches would be valuable.

- The paper lacks a thorough comparison with existing safety and overrefusal reduction methods. While baseline comparisons are provided, the authors don't fully contextualize their results within the broader landscape of recent work on LLM safety alignment. A more comprehensive comparison with methods like constitutional AI, RLAIF, and other preference optimization approaches would better demonstrate the advancement over state-of-the-art.

- The robustness of the proposed method requires more thorough investigation. The paper doesn't examine how the method performs under adversarial conditions or when faced with edge cases. Additionally, there's no analysis of the consistency of results across multiple training runs or different random seeds. This makes it difficult to assess the reliability and stability of the approach in practice. The ethical implications of reducing overrefusal deserve deeper examination. While the paper successfully demonstrates technical improvements in reducing overrefusal, it doesn't adequately address the broader implications of making models more compliant.

### Questions
1. Can you provide more insight into why advanced teacher models require more safety examples? Is this related to the complexity of their responses or other factors?

2. How do you expect the observed trends to scale with different model sizes? Would smaller or larger models show similar patterns?

3. Could you elaborate on how different rejection sampling criteria were selected? Were other criteria considered?

   How sensitive are the results to the specific thresholds used in rejection sampling?

4. Could the authors expand on the ethical implications of their work, particularly regarding the balance between user freedom and model safety?

5. How do the results of POROver compare to other existing methods for improving LLM safety and reducing overrefusal? Are there any specific scenarios where POROver outperforms or falls short of other approaches?

6. Have you explored automated methods for tuning the containment threshold τ?

   Were other preference optimization methods considered besides DPO?

   How does the slight safety compromise in OR-Bench Toxic relate to the containment threshold?

### Soundness
2

### Presentation
2

### Contribution
2
