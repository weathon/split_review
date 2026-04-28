# Why Has Predicting Downstream Capabilities of Frontier AI Models with Scale Remained Elusive?

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Predictable behavior from scaling advanced AI systems is an extremely desirable property. 
Although a well-established literature exists on how pretraining performance scales, the literature on how particular downstream capabilities scale is significantly muddier. 
In this work, we take a step back and ask: \textit{why has predicting specific downstream capabilities with scale remained elusive?} 
While many factors are certainly responsible, we identify a new factor that makes modeling scaling behavior on widely used multiple-choice question-answering benchmarks challenging.
Using five model families and twelve well-established multiple-choice benchmarks, we show that downstream performance is computed from negative log likelihoods via a sequence of transformations that progressively degrade the statistical relationship between performance and scale.
We then reveal the mechanism causing this degradation: downstream metrics require comparing the correct choice against a small number of specific incorrect choices, meaning accurately predicting downstream capabilities requires predicting not just how probability mass concentrates on the correct choice with scale, but also how probability mass fluctuates on specific incorrect choices with scale.
We empirically study how probability mass on the correct choice co-varies with probability mass on incorrect choices with increasing compute, suggesting that scaling laws for \textit{incorrect} choices might be achievable.
Our work also explains why pretraining scaling laws are commonly regarded as more predictable than downstream capabilities and contributes towards establishing scaling-predictable evaluations of frontier AI models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors show that down-stream performance for multi-choice question answering can be predicted using alternative surrogates. This has a lot of importance when predicting real world model performance than simply looking at the regression loss.

### Strengths
- The authors suggest alternate metrics to predict multi-choice question-answering performance than the current ones that is more predictive in real world benchmarks
- Their alternate metrics are also general (for instance, they don't have conditions on performance being above some level) and easy to compute
- This work should have a good impact on investigating alternate metrics for down-stream performance when pretraining LLMs

### Weaknesses
 - This work only focuses on multi-choice question answering, although quite general, it still is lacking when we consider even universal methods such as CoT does not directly fall into it, not to mention tool-usage etc.


### Questions
- Do you think these ideas will transfer to even larger models? I understand checkpoints for newer and larger models are usually not public.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the reasons behind why predicting downstream capabilities of large language models has remained challenging despite well-established scaling laws for pretraining performance. The authors show that the process of computing downstream performance metrics like accuracy from pretraining log likelihoods involves a sequence of transformations that progressively degrade the statistical relationship between performance and scale. They identify the key mechanism causing this degradation: downstream metrics depend not just on the probability mass assigned to the correct answer choice, but also on how probability mass fluctuates on the specific incorrect answer choices. The probability assigned to incorrect choices does not have a strong predictable relationship with scale. The authors argue this explains the comparative unpredictability of downstream performance and suggest paths forward, like modeling the scaling of probability on incorrect choices. They also advise on designing more predictable downstream evaluations tightly coupled to pretraining log likelihoods. Overall, the paper provides valuable insights into the factors affecting downstream predictability and guidance on improving evaluation of frontier models.

### Strengths
The key insight that downstream unpredictability is caused by probability fluctuations on incorrect answer choices is novel and not obvious a priori. Framing the problem in terms of a sequence of transformations that degrade predictability is useful to make modular progress on the problem. The experiments are comprehensive, covering many models, benchmarks, performance metrics, and correlation measures. the authorsalso perform robustness checks to establish their claims.

A key strength of the paper is the precise mathematical formulation of how downstream performance metrics are computed from pretraining log likelihoods. This formalism allows the authors to reason about how each step impacts the relationship between performance and scale.
The paper's experimental methodology is also comprehensive. The authors evaluate five model families on twelve diverse multiple-choice benchmarks, covering commonsense reasoning, science, math, social science, and the humanities. For each benchmark, they compute per-sample scores for three performance metrics (accuracy, Brier score, probability on correct choice) across many model scales. 

Beyond simply demonstrating that downstream metrics become less correlated with scale after a sequence of transformations, the authors provide a clear mechanistic explanation for why this occurs. They show in Section 5 that that fluctuations in the probability assigned to specific incorrect answer choices breaks the clean relationship between downstream performance and scale.

### Weaknesses
The paper focuses exclusively on multiple-choice question-answering benchmarks. While the authors justify this focus, multiple-choice has limitations as an evaluation format. It would strengthen the paper to discuss how the insights might generalize to other types of benchmarks like free-form language generation. Are there analogous factors that could cause unpredictability in other settings?

The experiments focus on predicting performance for individual samples. In practice, aggregate performance over a distribution is often of interest. The authors should also discuss if fluctuations on incorrect choices "average out" over a distribution, and if there are still challenges predicting aggregate performance.
The guidance on designing more predictable evaluations, is very limited. The authors should expand on this point with more details and examples of predictable benchmark designs.

### Questions
Some key questions that the authors can explore are as follows:

How can their results and insights about probability fluctuations on incorrect choices generalize beyond multiple-choice benchmarks to other types of language tasks? Are there similar factors that cause unpredictability for other task formats?

The experiments focus on individual samples. Do the challenges with predicting performance due to probability fluctuations persist even when averaging over a distribution of samples? Or do the fluctuations tend to "average out"?

The authors discuss modeling the scaling trends for probability assigned to incorrect answer choices as a path towards better downstream predictability. How feasible do they think this approach is in practice? What challenges do they foresee? How does it scale?

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
3

### Summary
This paper investigates why predicting downstream performance of large language models has remained challenging, despite the relative predictability of pretraining loss. The authors analyze multiple model families across various benchmarks and identify one factor which reduces the predictability of benchmark performance: people tend to focus on scaling laws looking at benchmark accuracy scores, rather than further upstream metrics such as the model logprobs on the correct choice (without renormalization to valid options).

### Strengths
The main strength of the paper is that the story is quite simple and is strongly supported by the experiments. It is also timely and a matter that has many downstream implications.

The empirical evaluation seems to be quite comprehensive and technically sound.

The authors also provide both a compelling mechanistic explanation as to why the probability mass on the incorrect choices matter, and actionable insights for the field moving forward in light of these results.

### Weaknesses
While the findings are interesting, I'm a bit confused as to why the authors did not try to use their insights to attempt novel predictions of performance on benchmarks, and just limited themselves to measuring correlations. It would have been more impactful to demonstrate how the proposed metrics, particularly log p^Vocab, can be used to predict actual benchmark scores, rather than just showing correlations. This would provide more concrete evidence of the practical value of their findings.

Also, I think I'm a bit confused about one of the takeaways: they say to use p^Vocab, but AFAICT in section 6 they also argue that to do even better in predicting benchmark scores, one would need to model the joint evolution of probabilities across all tokens. Do the authors think that the evolution of probabilities across other tokens is a large contributing factor to having good scaling laws? From the results from Figure 3, it seems like we already have very large correlations when using log p^Vocab?

To broadly recap, I think most of my confusion stems from the disconnect between the promising analysis using correlations, and the lack of actual predictions using their best technique (log p^Vocab), showing how they fit the performance that is actually obtained by models. It may be that I'm misunderstanding something.



### Questions
"All the scores we discuss are per-datum." / "Firstly, this negative log likelihood is not computed in expectation over a corpus;" -> What does this mean? What would it even look like to do the log likelihood in expectation over the corpus?

Is it fair to say that one of the main takeaways of your paper is that for best results, you would need to "model the joint evolution of probabilities across all tokens, not just the correct value" (and this is what you do in Section 6)?

You say "one must predict not just how probability mass concentrates on correct choices with scale, but also how probability mass fluctuates on incorrect choices with scale." -> would it be more fair to say that you think that predicting how probability mass fluctuates on incorrect choices *may* enable better predictions, but you don't really know by how much? Unless I'm missing something, you don't have strong evidence that it would improve things substantially? The results from Figure 3 seem already quite strong without this additional modeling?

### Soundness
4

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
The paper presents a case study demonstrating that measures of downstream performance do not correlate strongly with the scale of large language models, unlike measures of the pre-training performance. The study is conducted on multiple-choice question answering benchmarks, evaluated on downstream metrics like accuracy, brier score, etc with the pre-training metric being the probability mass on the correct choice. The key insight is that correlation with scale progressively reduces as the downstream metrics become increasingly non-linear functions of the pre-training metric. The reason is said to be the lack of consideration of the probability masses on the incorrect choices, which is then shown to be strongly correlated with the (predictable) pertaining metric.

### Strengths
- Insightful analysis of the degradation of predictability of metrics of interest with model scaling, highlighting the need for other scale-predictable indicators of performance.
- Extensive empirical evaluation spanning a wide range of model families and benchmark datasets.
- Generally, a well-presented paper.

### Weaknesses
 - The paper seems to draw some obvious conclusions in places, possibly highlighting an overarching drawback with using correlation-based analysis. Correlation measures the degree of *linear* relationship between two variables. Consequently, in the equation block around L357, it is known a priori that if $Corr(\text{Compute}, \log p_\theta^{\text{Vocab}}(\text{Correct Choice}))$ is high, then dropping the $\log$ is bound to reduce correlation statistic.

This highlights another potential oversight in the analysis: 
- Takeaway #1 and #3 rightly suggest thinking about scale-predictable metrics. The study highlights what transformations make metrics unpredictable, in particular, from $\log p_\theta^{\text{Vocab}}(\text{Correct Choice}) \to p_\theta^{\text{Choices}}(\text{Correct Choice})$. With the same reasoning, in conjunction with the first point above, it is highly likely that $\log p_\theta^{\text{Choices}}(\text{Correct Choice})$ will be scale-predictable although $p_\theta^{\text{Choices}}(\text{Correct Choice})$ is not.
  - Experiments like those in Figures 3 and 4, but for $\log p_\theta^{\text{Choices}}(\text{Correct Choice})$ will be insightful to study this, and in line with the overall takeaways of the paper. I am willing to update my score depending on the author's response to this point in particular.

Nitpicks: 
- Equation (2): should have a $\propto$.
- $N$ is overloaded, in Equation (6) as well as under compute budget calculations.



### Questions
- Figure 2 [bottom left]: The peak of the distribution is narrow, and reaches at most 7% samples. It seems unlikely that that area under the distribution curve covers 100% of the samples. What exactly is this graph denoting, if not the per-sample correlation distribution of *all* samples?
  - Moreover, since curves here are most similar to the green illustrative example [top left], the complementary CDF is expected to flatten out to the very right end (close to 1 on the x-axis), but no plots for experiments in the paper seem to have that pattern. Why is that?
- How do these findings relate to the objective mismatch problem: that the pre-training objective does not align with the evaluation objectives?

### Soundness
2

### Presentation
3

### Contribution
2
