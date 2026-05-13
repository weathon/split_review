# CBF-LLM: Safe Control for LLM Alignment

- Decision: Reject
- Scores: 1, 3, 5, 8, 3

## Abstract
This paper proposes a control-based framework for aligning large language models (LLMs) by leveraging a control barrier function (CBF) to ensure user-desirable text generation. 
The presented framework applies the safety filter, designed based on the CBF, to the output generation of the baseline LLM, i.e., the sequence of the token, with the aim of intervening in the generated text. 
The experiment demonstrates its control ability and effectiveness in reducing the number of interventions needed for user-specified alignment tasks.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper studies controllable decoding in LLM generation, e.g., keeping the generated text of a positive sentiment or withing a specific topic. The paper proposes using a classifier that is trained on examples that are specific to the target control criteria. The classifier is used to define a control constraint that is checked repeatedly after generating each token. The probabilities of the candidate tokens that violate the constraint are set to zero. The paper limits the set of candidate tokens to k << vocab-size (e.g., 30) for efficiency. With a single prefix for controlling for the sentiment of the text and another single prefix for controlling for the topic, the paper shows some advantage over not applying any control at all.

### Strengths
1. The presented method is learning free and broadly applicable.

### Weaknesses
1. The paper does not compare to existing baselines beyond just the naïve blocklist approach. In fact, there are published and peer-reviewed papers that achieve the same goal with the closely related method that the paper does not compare to, e.g., Mudgal et al, "Controlled Decoding from Language Models", ICML 2024.

2. The paper does not present sufficient experimental results. It is just one prefix that is used per each of the two use cases demonstrated. That is not even sufficient for a workshop paper. The paper needs to provide quantitative results that are aggregated across several diverse examples. 

3. Related to the weak experiments, the paper also needs to provide human assessment of the produced generations and use that to demonstrate that the presented method truly introduces some value over the blocklist approach. Also, how does the control method impact the generation quality of the model (e.g., fluency, naturalness, general LLM capabilities), what happens if we wanted to control for more than one aspect, what is the role of the data properties (e.g., size) used to train the classifier on the overall quality. 

4. Even with limiting the candidate tokens size to the top-30, applying that methods at each decoding step (i.e., token generation) seems expensive. The paper needs to provide some details on that cost.

### Questions
Please see my questions under weaknesses.

### Soundness
2

### Presentation
2

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
This paper deals with safety control in LLM alignment. The authors get inspiration from collision avoidance in control engineering and propose a control barrier function as the safety filter to ensure the user-desirable text. Experiments are conducted on Llama3 using a RoBERTa model as the CBF.

### Strengths
- The safety control of LLM outputs is a significant topic.   
- It is interesting to see the connection between control engineering and text generation, e.g. the collision avoidance analogy to safety control in text generation.

### Weaknesses
 - The proposed method is very similar to existing work inference-time constrained decoding such as SafeDecoding[1]. The authors should definitely discuss the line of work.

- Based on my understanding, this work mainly introduces a CBF (specifically sentiment analysis RoBERTa) to measure a metric h(x) during decoding. The details of text generation the authors describe should be the standard greedy decoding process with top-k sampling. Instead of using standard greedy or beam search, they introduce the CBF to measure the toxicity of the generated text and restrict tokens with negative h(x). Then (1) it is so weird and not reliable to use a sentiment classifier to predict the toxicity instead of existing toxicity classifiers (2) even if using a reasonable toxicity classifier, a single token does not necessarily change a text sequence from safe to unsafe state. Existing works usually use guardrails such as Llama-Guard to measure the entire generated text sequence rather than part of the sequence.   

- The experiments are not convincing. The only data used in the experiment is just one single sentence. To verify the effectiveness, experiments on existing jailbreak datasets such as AdvBench[2], HarmBench[3] are necessary. To claim its effectiveness on hallucination mitigation, more experiments on related datasets are also necessary rather than using just one sentence.

- It is unclear whether this new decoding algorithm has an impact on the helpfulness of LLMs for other datasets such as MT-Bench. 

- The average token generation time also needs to be discussed.

### Questions
- Does Section 2.2 describe the standard greedy decoding process (correct me if I am wrong)? I would recommend the authors refer more to the traditional decoding algorithm in the NLP domain, otherwise it would be very confusing to the readers.
- Even though it is interesting to discuss the counterpart and analogy in control engineering, relating it more to existing works in the LLM decoding would make it easier to tell the differences and see if there are real contributions.  

[1] Xu, Z., Jiang, F., Niu, L., Jia, J., Lin, B. Y., & Poovendran, R. (2024). Safedecoding: Defending against jailbreak attacks via safety-aware decoding. ACL.

[2] Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J. Z., & Fredrikson, M. (2023). Universal and transferable adversarial attacks on aligned language models. arXiv preprint.

[3] Mazeika, M., Phan, L., Yin, X., Zou, A., Wang, Z., Mu, N., ... & Hendrycks, D. (2024). Harmbench: A standardized evaluation framework for automated red teaming and robust refusal. ICML.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the task of LLM alignment from the control engineering perspective. Specifically, a filter is applied to the sequence generation steps of LLMs. The fundamental idea is that if a particular property is maintained at every step, that property should ultimately be evident in the final output.

### Strengths
1. Tackling LLM generation from the perspective of control engineering is interesting. In particular, it is novel to  use a hyperparameter $\alpha$ to adjust the tightness of the constraint in autoregressive text generation. 
2. The paper is well-written, and the intuition equations are clearly explained.

### Weaknesses
1. There is a lack of comparison to existing methods for decoding-time LLM alignments, including:
    1. Mudgal et al., Controlled Decoding from Language Models, 2024,
    2. Huang et al., DeAL: Decoding-time Alignment for Large Language Models, 2024
    3. Yang et al., FUDGE: Controlled Text Generation With Future Discriminators, 2021
2. To some extent, the proposed method can be considered a special case of the methods mentioned in Point 1, where the classifier makes hard decisions rather than giving scores. My educated guess (since the authors have not provided supporting experiments) is that the hard-filtering approach is worse. Here is my reason:
   - The semantics of phrases are often determined by later-generated words/phrases; the hard decisions based on the early phrases may result in unnecessary pruning compared to the soft counterpart (with scorers). 
   - Suppose we want to generate a positive movie review; an audience may say, "Despite a slow start, the movie blossomed into a riveting tale that kept me on the edge of my seat."  However, this is most likely not allowed by the proposed approach because the generation is cut off at  the "slow start."

### Questions
Is the classifier (RoBERTa) trained on whole sequences or prefixes?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a method to filter the language produced by an LLM such as LLAMA; the filtering happens via an auxiliary algorithm/model that scans the original LLM’s output probabilities of vocabulary words to be produced next and picks out the word(s) that satisfy an additional requirement such as producing positive or negative text, or text on a specific topic. This filter function/model seems to be another pre-trained LLM as well, e.g., Roberta.

### Strengths
The work retrofits LLAMA-type LLM to produce desired constrained language in a general way. 

The work has a theoretical component to it wherein it attempts to control  language production using established techniques from the perspective of control theory. 

The approach has been used to produce text that suits the purpose under different constraints.

### Weaknesses
The presented theoretical and algorithmic control approach seems cumbersome and done in a roundabout way, not straightforwardly.

There seems to be no evaluation of the generated text after filtration. Output sentence examples are given and seem good, but the main paper doesn’t contain evaluation metrics and scores. 

I find the analogy with a car not particularly persuasive. In a car, to avoid obstacles, the car’s internal processes must change to produce new trajectory for the car. However, in an LLM, to produce the desired output, the proposed approach lets the LLM produce output as usual, but seems to filter later to suit the purpose.

It will be good to cite a relevant paper: Zingale and Kalita. 2024. Language Model Sentence Completion with a Parser-Driven Rhetorical Control Method. In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics, pages 193–203.

### Questions
NA

### Soundness
3

### Presentation
4

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
The paper presents a control-based framework for aligning LLMs to ensure the generation of user-desirable text. The framework leverages control barrier functions (CBFs), a concept from control engineering, to intervene in the output generation of LLMs, aiming to prevent the production of harmful, biased, or toxic content. The key contributions of the paper are:

1 This paper presents a novel framework that applies a CBF-based safety filter to LLM output, aiming to reduce the need for interventions in text generation while maintaining alignment with user specifications.

2 This paper demonstrates the practical application of the CBF-LLM framework using Llama 3 and a sentiment analysis RoBERTa model, showing its effectiveness in generating positive content.

3 This paper attempts to connect control engineering with NLP by adapting control theory techniques for LLM alignment, offering a new perspective on ensuring the safety and ethicality of LLM-generated content.

### Strengths
1. The paper is well-written, and I really like their figures.  
2. There is a detailed theoretical transfer and explanation on control engineering and how it can be extended to LLMs.  
3. This paper provides some inspiration for future non-parametric optimization methods for LLMs.  
4. To some extent, it achieves an alignment from weak (RoBERTa) to strong (LLaMA).

### Weaknesses
1. The experiments and datasets lack persuasiveness. All experiments in the paper are based on only a few queries, with almost no evaluations on common LLM benchmarks or other metric. Specifically, the paper does not evaluate the generated text on standard benchmarks for toxicity, bias, or other common safety metrics. The lack of quantitative results makes it difficult to assess the practical effectiveness of the proposed framework.

2. The approach heavily relies on a Language-Constraint Function (L-CF), implemented with RoBERTa and assumed to be a golden classifier. However, I believe that assuming RoBERTa as an ideal classifier is not reasonable in practical use. RoBERTa's performance on specific tasks may not generalize well to the broader range of potential issues that the CBF-LLM framework aims to address. The paper does not provide any evidence of RoBERTa's accuracy in this specific context, nor does it address the potential for errors or biases in RoBERTa's classifications.

### Questions
1. Why not conduct experiments on at least a small-scale widely-used LLM evaluation datasets, such as a subset of Anthropic/hh-rlhf?  
2. I feel that finding a reliable Language-Constraint Function (L-CF) is similarly challenging to training a golden reward model. It might be insightful to explore scenarios where the Language-Constraint Function (L-CF) has varying levels of reliability.

### Soundness
1

### Presentation
3

### Contribution
2
