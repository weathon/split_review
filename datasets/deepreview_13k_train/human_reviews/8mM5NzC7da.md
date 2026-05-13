# Out-of-Distribution Detection using Synthetic Data Generation

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Distinguishing in- and out-of-distribution (OOD) inputs is crucial for reliable deployment of classification systems. However, OOD data is typically unavailable or difficult to collect, posing a significant challenge for accurate OOD detection. In this work, we present a method that harnesses the generative capabilities of Large Language Models (LLMs) to create high-quality synthetic OOD proxies, eliminating the dependency on any external OOD data source. We study the efficacy of our method on classical text classification tasks such as toxicity detection and sentiment classification as well as classification tasks arising in LLM development and deployment, such as training a reward model for RLHF and detecting misaligned generations. Extensive experiments on nine InD-OOD dataset pairs and various model sizes show that our approach dramatically lowers false positive rates (achieving a perfect zero in some cases) while maintaining high accuracy on in-distribution tasks, outperforming baseline methods by a significant margin.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the simple idea of generating synthetic OOD data for training OOD detectors. The core idea is to generate near-OOD and far-OOD data by prompting an LLM given the ID data. The synthetic data are generated with Llama-3 Instruct. 

The authors ran experiments on three tasks: toxicity detection, harm detection, and reward modeling data classification. These experiments are done on Llama-2 13B and Starling-RM-7B-alpha. 

The empirical results are generally positive across different datasets and experiment setups, although I have some questions and concerns as explained in later sections.

### Strengths
- Experiments are pretty comprehensive. 
- Empirical results are generally positive.

### Weaknesses
I don't find this paper particularly well-recognized, and I had a hard time finding some relevant experiment details. Can I clarify: 
1. Are all the baseline methods (MSP, Energy, DICE) trained with the original real data? And are the synthetic data the same size as the original OOD data? 

2. You are using a 70B model to generate the synthetic data but using 13B or 7B data for the OOD detection task. In a way this is distillation? Have you analyzed the impact of the size of the synthetic data generation model? Would a 7B data be able to generate high-quality OOD data? 

This is probably minor but I really don't like the way your wrote your related work section (first two paragraphs). Dumping a bunch of citations with minimal descriptions is not particularly useful.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a novel framework for OOD detection, which leverages LLMs to generate synthetic data for the training data with external OOD data source. Upon experiments on nine InD-OOD dataset pairs, this method is shown to be effective and outperforms baselines.

### Strengths
1. This paper is really easy to follow, with proper figures and content analysis. Also, the methods proposed are very simple, and, as far as I know, new. 

2. The selected datasets and metrics are proper to me.

### Weaknesses
In sec4 last paragraph, the authors stated that "our synthetic data is nearly as effective as real OOD data, and possibly more diverse, in representing OOD samples." with only showing the figures of visualization. I believe more statistical analysis is needed to make this claim valid.

### Questions
1. I am interested in the models used. In different sections of the experiments, the authors seemed to use different models, e.g., Llama3 70b for generating synthetic data, Llama2 13b for fine-tuning on the datasets tested, and Starling 7B for the RLHF model. Although they are all Llama based models, they are different versions with different parameter settings. Why did you use different settings rather than being consistent? 

2. In prompting the model to generate synthetic data, did you use a fixed prompt template? Have you tried different prompt templates? Is it  necessary to test the robustness with different prompts? What kind of decoding strategy did you use?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the problem of out-of-distribution detection by using LLMs to generate synthetic OOD data, which can then be used to train OOD detectors without needing existing OOD data. 

Overall, I think this paper is ready for publication. The results reported are not clear and well-presented at the moment. More importantly, it is unclear whether the definition of OOD detection that is considered in this paper is relevant. 

Recommendations for Improvement:
To improve the quality of the paper in future re-submissions, I would encourage the authors to define more clearly the OOD task and argue why the definition they use is useful. In particular, engaging with the distinction between cross-tasks OOD versus within-task OOD. 

To better discuss the contribution, the paper should disentangle the synthetic OOD data generation process from modifications to the OOD detector itself. First show that the synthetic OOD data generator is useful independently of the OOD detector used. Then, show that the OOD detector with 3 classes is useful independently of the training data. Finally, sell the combination of the two.

### Strengths
The authors have performed extensive experimental testing, which could be useful if the results were presented more clearly.

### Weaknesses
Overly Simplistic Definition of OOD:
The OOD detection tasks considered in this study, even those termed “near-OOD,” seem simplistic and easy to solve. For instance, distinguishing between tasks like CC and GSM8k does not appear to be particularly challenging. It is not clear what is the real-world relevance or difficulty of these OOD tasks. It would be very surprising that no baseline method perform well on these tasks.  
Additionally, for the few baselines reported on table 1, there seems to be an unusual amount of repetitions of numbers, which seems to point to mistakes in reporting.

Do we need Synthetic OOD Data: 
Given the definition of OOD used here as “task vs. task” detection, it’s unclear why synthetic data generation is necessary. Instead of synthetic data, one could simply use any existing task/dataset as OOD data for this problem, there would be plenty of them already available without the need for generating need data. This should actually be a baseline to test the usefulness of the synthetic data generation: Instead of training OOD detector with synthetic OOD data, train with other existing data as OOD. 

Generally, I feel that it would be more interesting to focus on within-task OOD detections where the distribution shift comes from shifts in the labels distribution shift, input properties, or mappings between the inputs and labels. This setup would be significantly harder, more relevant, and more likely to need synthetic OOD data.

Clarity of the Presentation: The current structure of the paper is disorganized, with key elements of the methodology, metrics, and datasets introduced only later in the paper, despite being referenced earlier. There is also some confusion about the different types of contribution between modifications to the OOD training pipeline ( generating synthetic OOD data) and modifications to the OOD detector itself (adding a third class instead of using a binary setup). These two modifications should be evaluated separately to clarify their individual contributions.

### Questions
Why are there some many repeated numbers in Table 1?
Why the tasks presented in Table 1 are not solved by simple heuristics (different tasks clearly ask different questions, it should be fairly easy to recognise them)?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to use Language Models to generate synthetic OOD data to train OOD detectors. 
Their experiments show that the synthetic OOD data can help improve the performance of the OOD detection.

### Strengths
1. This paper explores the possibility of using language models to help improve the performance of the  OOD detector. 

2. The experiments consider various baselines and different OOD cases, such as near OOD and far OOD. 

3. The author considers different tasks including toxicity detection, harm detection and RLHF reward modeling.

### Weaknesses
1. The overall writing and the formatting are poor. The arrangement of the figures all around and the main text always refers to figures in the appendix, which should be avoided (line 192, 212, 400, ). The logic between sections is not very clear. The author first showed the results and comparisons to baselines in section 3 without describing the method and setup first. Then the author refers to Table 1 (at page 2) at section 5.3 (page 7) which is not intuitive. 

2. The results in Table 5 show that using real OOD data outperforms the synthetic OOD data in most of the cases. This doesn't support the claim of the author about the quality of their synthetic data, which was discussed in section 4.

### Questions
I'm not sure if it is a fair comparison if you compare the synthetic OOD setup with other baselines which are not trained on any OOD data.
I think the result in Table 5 is a more realistic one where you compare the synthetic data with the real one. This tells you how good the synthetic OOD data is. I see the point of the OOD scarcity issue if you consider everything as training data, then it would be hard to find real-world OOD data for training the detector. But it would be nice to have some more analysis about the quality of the synthetic as the result in Table 5 is contrary to the discussion in line 259-266, stating that synthetic OOD data is nearly as effective as real OOD data.

### Soundness
2

### Presentation
1

### Contribution
2
