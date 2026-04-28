# How much can we Forget about Data Contamination?

- Decision: Reject
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
The leakage of benchmark data into the training data has emerged as a significant challenge for evaluating the capabilities of large language models (LLMs). In this work, we use experimental evidence and theoretical estimates to challenge the common assumption that small-scale contamination renders benchmark evaluations invalid. First, we experimentally quantify the magnitude of benchmark overfitting based on scaling along three dimensions: The number of model parameters (up to 1.6B), the number of times an example is seen (up to 144), and the number of training tokens (up to 40B). We find that if model and data follow the Chinchilla scaling laws, minor contamination indeed leads to overfitting. At the same time, even 144 times of contamination can be forgotten if the training data is scaled beyond five times Chinchilla, a regime characteristic of many modern LLMs. We then derive a simple theory of example forgetting via cumulative weight decay. It allows us to bound the number of gradient steps required to forget past data for any training run where we know the hyperparameters of AdamW. This indicates that many LLMs, including Llama 3, have forgotten the data seen at the beginning of training. Experimentally, we demonstrate that forgetting occurs faster than what is predicted by our bounds. Taken together, our results suggest that moderate amounts of contamination can be forgotten at the end of realistically scaled training runs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In the paper, the authors study the problem of data contamination in large language models, and the ability of these models to forget past contaminated samples during training. In the first part of the paper, the authors provide extensive experiments on the effects of data contamination and forgetting in a controlled setting, where some of the testing samples are included in the training set in random positions. In the second part, the authors derive a theoretical upper bound on the rate of forgetting in LLMs trained with AdamW as a function of the learning rate and the weight decay parameter.

### Strengths
Unfortunately I am not very familiar with the topic, so I cannot fully judge the novelty and impact of the work. Tot he best of my understanding, I find this paper very well written and the topic very interesting and timely. I also find the experiments provided by the authors are extensive and satisfying.

### Weaknesses
I would guess that the limit of the forgetting approach presented in the paper, in particular in Sections 4.2 and 4.3, is that no matter how long you train a model, there will reasonably always be contaminated samples in the last part of the training, say, in the final Chinchilla samples, that the final model has no time to forget. If you agree with this and I am not missing something, could you please elaborate on this? And can the results that you presented in the paper address this point?

Apart from the question in the Weaknesses section, I would also be interested to know if there is any correlation between the accuracy gap metric presented in Section 4.1 and the percentage of training samples that are contaminated. For example, it is expected that each line in Figure 2(b) decreases with the number of tokens, since the percentage of contaminated samples decreases as well. I was wondering if there is a proportionality law between the percentage of contaminated samples and the observed accuracy gap.

### Questions
Apart from the question in the Weaknesses section, I would also be interested to know if there is any correlation between the accuracy gap metric presented in Section 4.1 and the percentage of training samples that are contaminated. For example, it is expected that each line in Figure 2(b) decreases with the number of tokens, since the percentage of contaminated samples decreases as well. I was wondering if there is a proportionality law between the percentage of contaminated samples and the observed accuracy gap.

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
2

### Summary
This paper investigates the effects of small-scale data contamination in training language models. The experiments involve randomly injecting benchmark evaluation data into the training set, and then assessing the impact on loss and accuracy when evaluated against the "leaked" benchmark. The study examines how this effect changes with model size, the repetition frequency of contaminated examples, and scaling in accordance with the Chinchilla scaling law. The authors observe that generally a small amount of data contamination is forgotten after a few steps, and suggested a possible theory that weight decay influences this forgetting phenomenon. They provide a theoretical bound for the rate of forgetting due to weight decay, though they find that forgetting occurs much faster in practice.

### Strengths
- The research question is compelling and relevant, as data contamination is an unavoidable issue in practical LLM training.

- The experiments cover a wide range of model sizes and contamination scales.

### Weaknesses
 - My main concern is about the theory that weight decay influences forgetting. It's unclear to me why "forgetting past gradients" would equate to forgetting past training data since the model weights have already been updated based on that past data. In other words, past gradients have already shaped the optimization trajectory, so even if they no longer impact future updates, their influence isn't necessarily "forgotten." The fact that the theoretical bound is quite loose in practice also suggests that weight decay might not be the main factor behind forgetting. 

 - Evaluating LLMs is highly complex, and I'm unsure if simply comparing performance on the leaked benchmark is sufficient to fully capture whether the models have been influenced by data leakage or if it has been forgotten. It's possible that the model retains some form of implicit knowledge or bias related to the contaminated data, even if the benchmark performance appears to return to normal. A more comprehensive evaluation might involve probing the model's internal representations or using more nuanced metrics that can detect subtle forms of overfitting.

 - Although the observation is interesting, it’s unclear how this information can be practically applied, especially given the difficulty of accurately measuring data leakage in real-world LLM training. What is the practical impact of these findings? The paper needs to better articulate how the observed forgetting phenomenon can be leveraged in real-world scenarios, especially given the challenges in detecting and quantifying data contamination in large-scale datasets.

 - More of a future direction but would be interesting to see how data contamination affects other types of tasks and architectures, such as vision models and non-transformer models, as well as scenarios where training data are encountered multiple times. It would also be valuable to explore whether the weight decay explanation holds in these cases.

### Questions
- Intuitively, at least in more traditional ML, weight decay constraints drastic changes in model weights, which can help prevent both overfitting to earlier data and excessive drift from initial representations when new data is introduced. To me it makes more sense that weight decay plays a balancing role, encouraging the model to learn simpler representations. Indeed it can be challenging to determine how this applies to LLM training where factors like single-pass data and other complexities come into play. If the observed influence of weight decay on forgetting is specific to LLM training, what aspects of LLM training might be driving this effect?

- In the related work, the paper mentions that it focuses on "natural forgetting," which differs from catastrophic forgetting in continual learning. Could the authors provide a more quantitative explanation of this difference, beyond the distinction of being desirable or undesirable based on context?

- In the last sentence of the paragraph next to Table 1, it is mentioned that "under Chinchilla training, a single instance of contamination can lead to overfitting of up to 3 percentage points." I'm curious where the number "3%" comes from, as the scaling of the accuracy gap doesn’t appear linear with the number of repetitions. Is this a rough estimate? Additionally, why isn’t the effect of a single contamination instance directly shown in the experiments?

- In Figure 3 the description for plot (d) is very confusing since it's not actually the same as (a), please specify it more clearly. I'm interested in the difference between multi-pass data and single-pass data, but in this experiment, the number of tokens models are trained on is not the same between the two settings. So is the forgetting impacted by the fact that the training set is seen multiple times, or purely because the number of different tokens is lower?

### Soundness
2

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
The paper explores specific learning dynamics in language models, focusing on how these models gradually "forget" small-scale contaminations. This direction is crucial for understanding the reliability of benchmark evolution and its connection to potential contamination. To investigate this, training is conducted on data infused with samples from different benchmarks at varying contamination levels. Additionally, models of different scales are analyzed to assess the impact of model size on this phenomenon.

### Strengths
The paper empirically studies various settings:
- How various levels of contamination from various sets influences the performance in those respective sets?  Figure 2 
- How long does it take to forget these contaminations? Fig. 3a What kind of data makes it forget? Fig 3e and their position in training ? Fig 3b,c
- How is the effect the scales of model, data and frequency of contaminated examples on forgetting the contamination ? Figure 2 
These questions are  important and the paper tries to address them.

### Weaknesses
 - The theoretical analysis is very limiting - the only case considered is forgetting the exact gradient of the contaminated example. The analysis is preliminary as the paper already mentioned that it does not take into account the forgetting of the gradient by cancellation. The gradient of related contaminated samples late in the training are also not accounted. 
- Experiments with larger models are needed to validate the findings across scale.

### Questions
- Why the frequency of the repetitions are chosen as 4, 12, 32, 144 (instead of say 4,16,32,128 - the powers of 2) ?
- The forgetting phenomenon is attributed to the weight decay, does it mean training without weight decay does not forget contamination.

### Soundness
3

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
4

### Summary
The paper investigate the effects of data contamination in LLMs and explore whether these models can forget contaminated data during training. The author challenge the common assumption that minor contamination renders benchmark evaluations invalid, by presenting novel experimental and theoretical insights. They show that the benchmark overfitting scaling is monotone in the number of model params, the number of of repetitions of examples in training data, and the number of training tokens.  Authors also develop a theoretical framework to understand how cumulative weight decay in AdamW facilitates forgetting of contained data, suggesting that under certain conditions, this decay can render contaminated samples negligible by the end of training. TLDR; Contamination concerns may be overestimated for extensive training runs of modern LLMs, and weight decay play a critical role in “forgetting” in data-intensive training regimes.

### Strengths
This paper explores the critical topic of data contamination in LLM training, as model scale increases and samples contamination gets more likely. Authors offer a timely into how the contamination affects model evaluations, challenging the prevailing assumption that any contamination renders the evals invalud. The paper has a very scientific approach and combines nice theoretical insights with extensive experimental validation, presenting contamination as a challenge that might be mitigated by the large-scale and data-intensive nature itself of model LLM training setups. They propose that the cumulative weight decay in AdamW (often used to train modern LLMs) acts as a natural forgetting mechanism for contaminated data. The overall paper is very sound, balancing a solid theoretical framework, with carefully controlled experiments across various model scales, token volumes and contamination frequencies. The combinations of gpt-3 and large OLMo-1B model along with clearly documented, reproducible methods, code and datasets, adds significant credibility to the findings.

### Weaknesses
The theoretical framework for forgetting seems to rely on the assumption that contamination occurs uniformly and that the data scale follows the Chinchilla scaling law. This limits generalizability, as many real-world LLms operate outside this scaling regime or include more intricate forms of (more complex) contamination. The theoretical derivations in the cumulative weight decay analysis, although sound, assume orthogonality in gradient updates without acknowledging that in real-world training, gradient alignment might cause contaminated examples to persist longer (dependencies between gradients could affect forgetting). 

Minor things:
Line 055-056: I would change ordering of (2) and (3) to be consistent with lines 059-062.
Line 195: "We being" -> "We begin"

### Questions
— Given the focus on cumulative weight decay, how does your theory account for rare or privacy-sensitive data points that might resist weight decay due to repetition? Do you have experimental results that assess forgetting for low-frequency, high-sensitivity samples?
— As gradient updates are often correlated, especially, in high-frequency or structure contamination; have you considered conducting experiments simulating the effect of gradient alignment impact on the the cumulative weight decay effect?
— Do you have insights on why the empirical forgetting occurred faster than the predictions by your theory? What are the factors contributing to the discrepancy?

### Soundness
4

### Presentation
3

### Contribution
3
