# Can LLMs Understand Time Series Anomalies?

- Decision: Accept
- Avg Score: 5.20
- Scores: 6, 3, 6, 6, 5

## Abstract
Large Language Models (LLMs) have gained popularity in time series forecasting, but their potential for anomaly detection remains largely unexplored. Our study investigates whether LLMs can understand and detect anomalies in time series data, focusing on zero-shot and few-shot scenarios. Inspired by conjectures about LLMs' behavior from time series forecasting research, we formulate key hypotheses about LLMs' capabilities in time series anomaly detection. We design and conduct principled experiments to test each of these hypotheses. Our investigation reveals several surprising findings about LLMs for time series: (1) LLMs understand time series better as \textit{images} rather than as text, (2) LLMs did not demonstrate enhanced performance when prompted to engage in \textit{explicit reasoning} about time series analysis. (3) Contrary to common beliefs, LLM's understanding of time series \textit{do not} stem from their repetition biases or arithmetic abilities. (4) LLMs' behaviors and performance in time series analysis \textit{vary significantly across different model architectures}. This study provides the first comprehensive analysis of contemporary LLM capabilities in time series anomaly detection. Our results suggest that while LLMs can understand trivial time series anomalies (we have no evidence that they can understand more subtle real-world anomalies), many common conjectures based on their reasoning capabilities do not hold.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies how Large Language Models (LLMs) reason about anomalous time series. The authors formulate 7 hypothesis, based on recent work at the intersection of time series & LLMs, their own understanding of the problem, and prevailing hypotheses about LLMs, and carefully design experiments using synthetic time series to accept or refute their hypotheses.

### Strengths
1. The intersection of time series and LLMs is an exciting and active area of research. The authors present a very neat study on LLM capabilities on the anomaly detection problem. 
2. The hypotheses are interesting and most experiments are designed well. 
3. The paper is well-written, and aesthetically appealing, and some findings are interesting. 
4. The authors demonstrate a fairly good understanding of the literature, on time series, anomaly detection and LLMs.

### Weaknesses
1. **Some claims need to be supported or softened:** The authors make some claims in the paper which are not well supported by the experiments and the overall story. (a) *on the question of LLMs understanding time series*:  There are many different notions of understanding in addition to anomaly detection, such as in predictive tasks such as classification and forecasting, but also other inductive tasks such as understanding of (granger) causality. The ability to reason about one class of problems, does not imply the ability to reason about other classes of problems, hence LLMs are expected to do well in some tasks, and not in some others. What the authors show evaluate is if LLMs can reason about some kinds of anomalies using synthetic data. In the abstract, the authors mention: "These insights pave the way for more effective LLM-based approaches in time series analysis". However, it is unclear how some insights, while interesting, are actionable (e.g., on perceptual reasoning abilities). I must note that some insights are actionable, e.g. on long context bias. (c) The model-specific finding is not new, and is consistent with prior work which has established the need and value of model selection for anomaly detection.  
2. **On the defining anomaly detection:** Anomaly detection is a tricky problem with a lot of nuances. The authors only study one variant of the problem, i.e. detecting *4 different kinds of anomalies in synthetic time series with labels in zero-shot and few-shot settings*. Meanwhile, there is a large body of work in unsupervised or semi-supervised anomaly detection, which does not rely on explicitly labeled anomalies as training examples.  Finally, the authors state (line 223 onwards) the connections between forecasting and anomaly detection. These are valid. However, (1) only a subset of AD methods rely on forecasting, other methods rely on reconstruction or differences in latent space, (2) the authors do not rely on their LLMs ability to "forecast", and therefore the ability that they are testing have little to do with extrapolating, as against interpolating based on past and future context. 
3. **Reproducibility**: The authors haven't shared examples from their generated dataset, or the inference and evaluation code. They also have not shared visual examples of their generated time series, which makes it harder to reproduce their work.  
4. **Hypothesis 5 ("LLMs’ understanding of anomalies is consistent with human visual perception.") is too broad and not well supported:** (a) The study by Mueller & Timney, 2016, only exhibits 1 form of human perceptual bias. Disproving it only shows that LLMs do not have this particular bias. (b) It is not immediately clear to me how this bias manifests in anomaly detection. I am not sure how constant speed change differs from acceleration (which causes a change in speed). This hypothesis would greatly benefit from being fully specified, motivated, and examples of datasets shown. 
5. **Hypothesis 2 (LLMs’ repetition bias (Holtzman et al., 2020) corresponds precisely to its ability to identify
and extrapolate periodic structure in the time series. is unclear:** The hypothesis has 3 key terms, "identify", "extrapolate" and "periodic", but the authors do not vary any of these key terms. The settings that the authors consider have nothing to do with "extrapolation" (forecasting), they only consider periodic or periodic time series with noise (which is still periodic), and the paper provides no evidence if or how well LLMs identify periodic structure, and how that corresponds to their findings. I think examples of the generated dataset and the nature of the noise would benefit this section. Also, correlating the ability of models to identify / extrapolate periodic structure with their ability to identity anomalies in periodic and non-periodic time series, would be a much better way to break down this complex claim in my opinion. 
6. **Hypothesis 1 ("LLMs do not benefit from engaging in step-by-step reasoning about time series data.") is too broad:** The authors only provide evidence that the models are not capable of chain of thought reasoning. CoT reasoning is only one way to do step-by-step reasoning. The hypothesis should instead be that these models are not helped by engaging is CoT reasoning or some variant of this claim. 
7. **Use of Images:** This is an interesting finding and is consistent with recent work. I wonder if highlighting the location of the anomaly in the image, just like the authors have done it for illustrative purposes would benefit AD performance even more. I suspect it might be true because I am not convince that models understand this statement: `[{"start": 171, "end": 178}]` especially because the reader has no idea how the time series plots look, if they have an x and y-axis that's marked with sufficient font size and precision. 
8. **Synthetic data:** I understand why the authors use synthetic data, but without knowledge of the difficulty of the synthetic dataset, and how SoTA and simpler methods perform on these datasets. Also from the tables in the Appendix it seems that a simple threshold-based baseline does really well. This raises the question about the limited nature of anomalies, for example [5] can inject many more varieties of anomalies to real-world signals, which provides a much larger, and diverse set of real-world anomaly examples than the considered work. Also the authors cite [6] but do not use their datasets for their experiments. This might be important given that this studies' primary focus is on measuring LLM's ability to detect anomalies. 

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
With the increasing popularity of LLMs and applications to various tasks, such as forecasting, their performance for anomaly detection remains largely unexplored. This work studies zero-shot and few-shot scenarios of popular LLMs and formulates hypotheses to debunk current norms in this fastly emerging field. The analysis suggests that several beliefs were wrong so this paper offers a useful tool for helping to move the field forward.

### Strengths
S1. Timely problem to understand the performance of LLMs in this context
S2. Reasonable hypotheses formulated and tested
S3. Interesting findings useful for the community

### Weaknesses
W1. Unclear focus on LLMs and not pure focus on time-series Foundation Models.

Indeed, the field started by changing language models, assuming their sequential structure could have some benefit for time series as well. I think from the first moment, the time-series community understood how problematic that was.. and the lack of strong experimental results, comparisons with baselines, etc. exacerbated the situation and more and more folks tried to use such LLMs.. however, very fast, the field moved into pure time-series foundation models and abandoned LLM or VLMs for such use. So even though I appreciate the effort, at the same time I think the picture is already much much bigger to just make claims about LLMs which are obviously problematic for this area. I think a much bigger study to include VLMs/LLMs/FM for this area is needed

W2. Missing evaluation measures

The study focuses on problematic solutions for assessing anomaly detectors. There has been significant recent progress that is omitted [a].

[a] "Volume under the surface: a new accuracy evaluation measure for time-series anomaly detection." Proceedings of the VLDB Endowment 15.11 (2022): 2774-2787.

W3. Missing benchmarks

Similarly, limited datasets are used when established benchmark exists for this problem [b]

[b] "TSB-UAD: an end-to-end benchmark suite for univariate time-series anomaly detection." Proceedings of the VLDB Endowment 15.8 (2022): 1697-1711.

W4. Missing experimental comparison against baselines to understand the performance of these methods

Even though I understand this might be somewhat out of scope, I think what matters in the end is how they performs vs. SOTA methods. Let's say even if they greatly understand time-series, in the end where they stand in comparison to SOTA techniques. Therefore, an evaluation using such methods ([a,b] should be a good starting point) is needed as well

### Questions
W1. Unclear focus on LLMs and not pure focus on time-series Foundation Models.

Indeed, the field started by changing language models, assuming their sequential structure could have some benefit for time series as well. I think from the first moment, the time-series community understood how problematic that was.. and the lack of strong experimental results, comparisons with baselines, etc. exacerbated the situation and more and more folks tried to use such LLMs.. however, very fast, the field moved into pure time-series foundation models and abandoned LLM or VLMs for such use. So even though I appreciate the effort, at the same time I think the picture is already much much bigger to just make claims about LLMs which are obviously problematic for this area. I think a much bigger study to include VLMs/LLMs/FM for this area is needed

W2. Missing evaluation measures

The study focuses on problematic solutions for assessing anomaly detectors. There has been significant recent progress that is omitted [a].

[a] "Volume under the surface: a new accuracy evaluation measure for time-series anomaly detection." Proceedings of the VLDB Endowment 15.11 (2022): 2774-2787.

W3. Missing benchmarks

Similarly, limited datasets are used when established benchmark exists for this problem [b]

[b] "TSB-UAD: an end-to-end benchmark suite for univariate time-series anomaly detection." Proceedings of the VLDB Endowment 15.8 (2022): 1697-1711.

W4. Missing experimental comparison against baselines to understand the performance of these methods

Even though I understand this might be somewhat out of scope, I think what matters in the end is how they performs vs. SOTA methods. Let's say even if they greatly understand time-series, in the end where they stand in comparison to SOTA techniques. Therefore, an evaluation using such methods ([a,b] should be a good starting point) is needed as well

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates whether MM-LLMs can effectively detect anomalies in time series data,from the perspective of validating 7 hypotheses about LLM performance on the proposed tasks. By conducting controlled experiments, the authors assess LLM capabilities across various anomaly types and input representations (text vs. visual). The findings reveal that LLMs perform better with visualised time series data. Additionally, the study challenges several assumptions about LLMs, including their reliance on arithmetic abilities and repetition biases, which were previously thought to aid in pattern recognition, and the impact of CoT on time series tasks. Finally the authors show that different model architectures can have significantly different performance in anomaly detection, suggesting that previous results using just one or two architectures may not generalise.

### Strengths
S1. The authors articulate hypotheses proposed by existing literature or propose some based on analyses of current research and then conduct controlled, synthetic, experiments to test these hypotheses.

S2. Visual vs. Textual Representation: this paper extends existing research into the feasibility of visual detection models for time series analysis by comparing multimodal LLMs' performance on visual versus textual time series data, revealing that visual inputs often yield better anomaly detection. Given the applicability of recent multimodal LLMs for a lot of tasks, the analysis on time series anomaly detection is timely.

S3. The study sets up interesting tests for the hypothesis around arithmetic abilities and repetitive biases. The noise injection and artificial arithmetic reasoning drop seem like a well-constructed approach.

### Weaknesses
W1. While the study is insightful, its primary focus on hypothesis testing rather than direct practical application might limit its immediate utility for practitioners looking to deploy LLMs in anomaly detection systems. This can still be helpful for theoretical progress and providing direction for further time-series anomaly detection research, however I think some of the experiments were not defined very strictly or in such a way that they could be built upon for future analysis which hampers the benefit of the work. Specifically, the lack of clear definitions for anomaly types and the methods used to generate synthetic data makes it difficult to reproduce the experiments or extend them to more complex scenarios. For example, the 'noise injection' method could be more rigorously defined with specific parameters and distributions. The absence of a standardized evaluation protocol for the anomaly detection task also makes it hard to compare the results with other studies.

W2. The experiments and the hypothesis validation, primarily rely on synthetic datasets for testing. Introducing real-world datasets, such as the 18 datasets found in the TSB-UAD univariate anomaly detection benchmark (Paparrizos et. al. 2022) can help with further validating these hypotheses in real-world settings. The reliance on synthetic data, while allowing for controlled experiments, does not fully capture the complexities and nuances of real-world time series data, which often contain various types of noise, missing values, and non-stationary patterns. Furthermore, the synthetic data generation process should be more transparent, including the specific parameters used to generate different anomaly types, to ensure reproducibility and allow for more targeted experiments.

### Questions
Q1. For further validation of the arithmetic ability hypothesis, did the authors consider simply comparing different variations of the same model architectures (e.g. by size) and their performance on standard arithmetic benchmarks and correlating it with performance on anomaly detection? It seems that for many of these hypothesis relying on other real-world benchmark proxies could provide additional verification.

Q2. For validating hypothesis 5, the authors claim the test dataset “is too subtle to be visually detected by humans”. How is this validated? 

Q3. I did appreciate that the authors stuck by the claim that humans preferred visual anomaly detection and also presented most of their results visually, however this did make it somewhat difficult to interpret the results. Would it be possible to summarise the most important tests for each hypothesis in a single table? I think this could add to the presentation.

Nits:

P.6. “We hypotheses…” grammar.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper explores the potential of using Large Language Models (LLMs) for analyzing anomalies in time-series data, focusing on the insights in terms of reasoning that can be gained from detecting them. To do this, the paper proposes a set of hypotheses and scenarios to assess the effectiveness of LLMs when processing time-series anomalies, providing an overview of their strengths and limitations, as well as the possible parallels with human reasoning.

### Strengths
- It introduces an attractive problem related to assessing how LLMs can detect time-series anomalies and explores whether there are similarities in how humans approach this task.
- It emphasizes the importance of analyzing time-series data from different perspectives, such as using visual features in a multi-modal setting, which may yield better results than relying solely on text input.
- The paper is generally well-written and relatively easy to follow.

### Weaknesses
 - The contributions of the paper are not explicitly defined, making the goal of the paper ambiguous. For example, it is unclear whether the goal was to provide a strategy for assessing how LLMs deal with anomaly detection (via the hypotheses), or to simply present the results of evaluating LLMs under specific settings (as highlighted in the abstract and introduction).
- The paper lacks a clearly defined and replicable method. The reasoning for establishing the hypotheses needs stronger support from previous work, and the evaluation design should clearly outline how each hypothesis is assessed and the logic behind it. Specifically, the prompt design and the method for impairing LLMs' arithmetic capabilities are not sufficiently detailed, making it difficult to understand how the experiments were conducted and how the results were obtained.
- The experiments lack essential details, such as the differences between prompt variants, and the results are inconsistent across all evaluated settings (e.g., combining zero-shot and few-shot in the same figures). This raises doubts about whether the highlighted findings are supported by the experimental results. The lack of a consistent baseline makes it challenging to compare the performance of different models and prompts.
- The paper contains claims like "prevailing beliefs about LLMs" or "expected patterns" that are not properly discussed. For instance, the Related Work section should explain what these prevailing beliefs are, and the Definitions section should clearly define what is considered an expected pattern. The absence of these definitions makes the claims vague and difficult to evaluate.
- The definitions of time-series are not formalized and are ambiguous. Many of them are not used, leaving it unclear as to why they were included. Additionally, there are inconsistencies between them (see details below).

# Detailed Comments
## Introduction
- There is not clear justification of focusing the evaluation solely in the F1 score
- The content is mostly focused on the experimental findings, so it is not clear what is the paper contribution
## Related Work
- It is mostly a literature review, with no discussion over the main topic of reasoning over times-series anomalies
- There is no discussion about the continuously mentioned controversy about time-series analytics in LLMs. A paper close to that topic, Jin et al. (2024a), was not discussed in this section.
- The claim of lack for visual M-LLM on time series is not accurate. For instance, Jin et al. (2024a) already included references to that approach

## Definitions
- Definition of anomaly is very ambiguous. What is an expected pattern? 
- There is no definition of the multiple thresholds
- Equation 1 needs a better explanation. What is G? A forecaster? If G generates x_t, so where the external x_t comes from?
- The anomaly detection algorithm is not clear. For example, it is a function that generates anomaly scores for each x_t...
- Interval-based anomalies definition seems incorrect. Why i /in {1,...,k} for a given y_t? It is probably Y, although it seems an unused definition
- If the interest in the data-point level anomalies, why using interval-based
- The few-shot definition is inconsistent with previous definitions and g is undefined. The output is probably referring to Y, instead of the actual s_1 or y_1
- The definition of zero-shot needs more details, contextualized to the prompt setting

## Time-Series Categories
- Shuffled time series? It is contractionary to the concept of series and time-dependency
- Trend example is not that clear. Which gradient?
- Frequency example is not clear, there is no significant shift in Fig. 1(b)
- What is an expected pattern? It is a very ambiguous term used frequently

## Time-Series Forecasting
- There are not clear details about the implication of extrapolation: "Therefore, both time series forecasting, and anomaly detection rely heavily on extrapolation."
- Connection with of time series and tokens needs to be clearly specified

## Understanding LLM 
- "To demystify LLMs’ anomaly detection capabilities" What are the myths? 
- There are many assumptions underlying the description of a LLM from a cognitive science perspective. The argument needs to be carefully elaborated because it is implying that a LLM behaves like a human brain, which is a strong statement. Then, it is not clear how the evaluation between reflexible and reflective modes is conducted
- It is not clear how the second hypothesis may be evaluated using noisy time series
- There is necessary to include some support for proposing the fourth and fifth hypotheses
- Fifth hypothesis evaluation is not as consistent with the approach of the referred paper
- In general, the hypothesis is not aligned with the paper goal regarding anomalies and are mostly focused on looking for some parallels with human reasoning

## Prompting
- The prompts seem very important, but there is no information about how they are designed. For instance, it is not clear what the variants are doing 

## Experiments
- The process for generating of data sets does not provide design details, even in the Appendix. It should disclose more technical details, and show some examples, since it is over this data that the hypotheses will be evaluated
- Metrics depend on a threshold, but there is no mention of it
- It is not clear what Figures 2,4,5,6,7,8 are showing. It is a comparison between prompts that may or may not be comparable and there is not clear point of reference
- There is not consistency between the selected prompts, so the results are hardly comparable between anomaly types or LLM engines. Also combining zero-shot and few-shot prompts will introduce unnecessary noise to the evaluation 
- In general, the experiments are not providing enough support for evaluating the hypotheses. For example, with the third hypothesis, how the arithmetic capability is removed? The experiment needs to include all this type of details
- The visual-text experiment, which is a major claim for the paper, need to explore with more details, how it was conducted, how the prompts were designed to achieve a fair comparison 
- Why the frequency anomalies failed? It needs a better explanation, perhaps showing an example of the actual task that the LLM is doing and the chart with the time-series

### Questions
- What are the prevailing beliefs about LLMs when processing time series? Where had they come from?
- How to impair a LLM for evaluating the third hypothesis?
- What are the foundations and support to evaluate a LLM from the perspective of cognitive science?


Post rebuttal comments:
Thank you for the authors' rebuttals, which address many of the questions. I thus increase the score.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study investigates large language models' (LLMs) understanding of time-series anomalies by proposing and testing specific hypotheses.

### Strengths
The study incorporates a wide range of prompting and representation techniques.

### Weaknesses
Writing
1. Some redundancy is present; for instance, the discussion in Section 3.3 lacks direct relevance to problem motivation and is only tangentially related.

Experiment/Study
1. Some hypotheses are tested without adequate scientific rigor. For example, in the discussion of Hypothesis (7) on architecture bias, several variables—such as model architecture (e.g., QWEN vs. GPT-4o-mini), model size, and the content and size of the pretraining corpus—are not controlled. This lack of control makes it difficult to attribute performance differences specifically to architecture, as they may instead stem from variations in model size or pretraining data.

2. No mention of using statistical tests for hypothesis. For instance, in the "retrained Hypothesis 1 on CoT reasoning," it is unclear if the claimed result is from statistical testing with a null hypothesis of no difference or heuristic. It would be made the study scientific and convincing by reporting some results from, say t-test on accuracy difference through bootstrapping.

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
