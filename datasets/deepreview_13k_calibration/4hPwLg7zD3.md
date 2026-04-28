# Fourier Head: Helping Large Language Models Learn Complex Probability Distributions

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
As the quality of large language models has improved, there has been increased interest in using them to model non-linguistic tokens.
For example, the Decision Transformer recasts agentic decision making as a sequence modeling problem, using a decoder-only LLM to model the distribution over the discrete action space for an Atari agent.
However, when adapting LLMs to non-linguistic domains, it remains unclear if softmax over discrete bins captures the continuous structure of the tokens and the potentially complex distributions needed for high quality token generation.
We introduce a neural network layer, constructed using Fourier series, which we can easily substitute for any linear layer if we want the outputs to have a more continuous structure.
We perform extensive analysis on synthetic datasets, as well as on large-scale decision making and time series forecasting tasks.
We also provide theoretical evidence that this layer can better learn signal from data while ignoring high-frequency noise.
All of our results support the effectiveness of our proposed Fourier head in scenarios where the underlying data distribution has a natural continuous structure.
For example, the Fourier head improves a Decision Transformer agent's returns by 46\% on the Atari Seaquest game, and increases a state-of-the-art times series foundation model's forecasting performance by 3.5\% across 20 benchmarks unseen during training.
We release our implementation at \url{https://nategillman.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a Fourier Head based on the Fourier series as a replacement for the usual linear classification head to induce continuous densities across the class IDs. It presents a theoretical analysis of the expressiveness and smoothness trade-off as the number of frequencies increases and empirically shows the advantage of the Fourier Head over the conventional linear head in tasks with output classes with a continuous structure.

### Strengths
- The proposed Fourier Head layer is well-motivated in domains where classes have a continuous structure
- The method is straightforward and clearly explained
- Visualizations clearly demonstrate the advantage of the Fourier head on toy problems in learing continuous densities
- Experiments in RL and time-series show the Fourier head can improve performance in non-toy settings

### Weaknesses
 - As the paper is focused on improving LLM's ability to model numerical values, there are important related works that explore alternative ways of extracting continuous probabilistic predictions from LLMs over numerical data [1, 2], which are worth discussing. These methods use a hierarchical representation of the numerical values, encouraging nearby values to have similar densities, as they do not correspond to independently predicted classes. These methods therefore do not have the limitations of "not consider any continuous structure that resides among the tokens", which the Fourier head claims to address.
- Similar to methods based on classification over binned values, the Fourier head can only represent a finite range of values. Methods like [1, 2] in principle do not have this issue. While a tanh reparameterization can map the domain to the real line, it is not clear whether the inductive bias of the model is natural for representing an unbounded range of values once such a transformation is involved. 
- The advantage of using the Fourier head seems most significant with small models trained on limited data. At a large scale, the model should be able to learn the continuous structure in the output classes, diminishing the benefit of using the Fourier head. It would be useful to show how the benefit of replacing the linear head with the Fourier scale with training data and model size, such as for Chronos models of different sizes. While the authors have shown scaling results for the Decision Transformer, it would be more compelling to see similar results for the Chronos experiment, where both the model and data size are much larger and arguably more representative of practical settings. For example, training with a 124M parameter GPT-2 model would be a good benchmark.

### Questions
- Can you provide more details on the Decision Transformer and Chronos experiments? How did you choose the size of the models, and how long to train?
- Can you show how the benefit of using the Fourier head varies as the model size or amount of training data increases? That is, does the benefit of the Fourier head persist at scale or does it vanish?

### Soundness
2

### Presentation
2

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
The paper introduces a novel Fourier head for large language models (LLMs), designed to improve the modeling of continuous structures in non-linguistic tokens, such as decision-making sequences in games and time series forecasting

### Strengths
Fourier head allows LLMs to better capture continuous structures in non-linguistic tokens, addressing the limitation in traditional models that use softmax over discrete bins.  The authors provide both theoretical justifications and empirical analysis.

### Weaknesses
1. The author posits that Fourier Head can endow the model with a continuity prior, which can be described as semantic adjacency. However, since LLMs inherently incorporate attention mechanisms that aggregate tokens with higher similarities, the contribution of the Fourier Head seems incremental. The claim that the Fourier head ensures neighboring tokens have similar likelihoods during next-token prediction needs more rigorous justification, as the attention mechanism already captures token relationships, potentially diminishing the unique contribution of the Fourier head in enforcing continuity.

2. Regarding the time series prediction section, the author has employed the T5 architecture, yet the baseline comprises only this architecture, which is overly simplistic. There is a significant body of work on time series LLMs currently, with most eventually employing a linear layer (could also be replaced with a Fourier head), such as TimeLLM GPT4TS[1,2]. I believe the author needs to further supplement the experiments. The lack of comparison against state-of-the-art time series forecasting models, particularly those utilizing linear output layers, makes it difficult to assess the true advantage of the proposed Fourier head. The experimental setup needs to be expanded to include more competitive baselines.

3. Additionally, I think the effectiveness of the Fourier Head may stem from its ability to analyze input frequency and amplitude through Fourier series. The author should consider comparing methods that are based on decoupling[3]. The paper does not adequately explore the potential overlap between the Fourier head's frequency analysis capabilities and existing decoupling methods, which also aim to disentangle time series components. This omission makes it unclear whether the Fourier head offers a truly unique advantage over these existing techniques.

### Questions
I am unclear about the organization of the paper, such as why the related work is placed in the latter half.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors argue that current methods for parameterizing a discrete distribution over numerical data suffer from ignoring ordinal structure, which should imply that adjacent discrete buckets will have similar density and therefore "smoothness" in the probability mass function. To fix this oversight, the authors propose a new parameterization on the coefficients of a Fourier series, leading to a smooth function on the interval [-1,1], which is then quantized. The new parameterization is therefore a drop-in alternative to a uniform bucketing of the interval. The method is evaluated on toy univariate densities as well as on an offline reinforcement learning problem and in time-series forecasting, and the result indicate that using Fourier head leads to lower errors in density estimation and higher returns in reinforcement learning.

### Strengths
The proposed method is simple and outlined with clarity in the paper. While the method is not complex, it is relatively novel to my knowledge. The significance is also reasonably large because modeling continuous numerical values using discrete tokens is increasingly popular.

### Weaknesses
To my understanding, the main goal of the paper is to propose a practical method, and given this goal, the empirical evaluation is not very impressive. I'll break this criticism down into a few subcategories

1. Emphasis on smoothness: The authors devote a lot of space and attention to the notion of "smoothness", proposing a new metric to measure it and including this metric in all the evaluations. However, from a practical standpoint it's not clear why we should care about smoothness independent of its effect on metrics like MAE or RMSE. In fact, it's possible to contrive examples where we want less smoothness (related to the square wave examples in the appendix), and it's not clear a priori that the marginal distributions for a particular downstream application will be "smooth". The "smoothness" numbers therefore feel like a distraction from what really matters, which is whether this ordinal inductive bias actually helps the model fit the data distribution. In many cases, the method seems to improve smoothness without affecting reward/loss or vice versa.

2. Limited empirical impact: while Fourier head does seem to yield significant benefits in offline RL, it doesn't seem to have a significant effect on time series modeling. The benefit in terms of MASE and especially in terms of WQL is very marginal, and if I were looking for ways to improve my model, I might not adopt the additional complexity needed for such a small improvement, which is probably on par with tuning other hyperparameters or making small architectural changes. It might be helpful to identify possible explanations for why the effect is relatively minor in time series but more pronounced in offline RL. For example, are the next-action distributions significantly different in their multimodality? It might be much more compelling to replace the time series experiments with additional offline RL experiments if that application happens to be the ideal use case for this method.

3. Limited baselines: Fourier head is only compared to the most naive possible baseline, uniform binning on [-1, 1]. In practice, there are more widely-used alternatives, such as Gaussian mixture models (GMMs) and quantile regression. Both of these techniques have an ordinal bias and should learn solutions that are much more smooth. I don't know if these methods are viewed as out-of-scope in this paper because they are not learned with cross-entropy loss. From one perspective, it might be reasonable to limit the investigation to discrete tokenization methods and discrete loss functions, but it does make the practical impact lower, as it's hard to tell whether this method is actually the best among all simple options or just an improvement upon simple uniform binning. This particular subcategory of criticism feels especially pertinent given the toy experiments in Section 4, where Fourier head is shown to approximate a GMM. It seems reasonable to conclude that in many cases a GMM should also therefore be able to approximate Fourier head. Is the converse not true and how important are the case where GMMs might not be able to match the performance of Fourier head?

Beyond empirical evaluation I think there are also other potential weaknesses:

1. Limited expressiveness: Presumably this method only works for bounded sequences. In the case of RL this might be reasonable if the state and action spaces are constrained. In the case of time series, this limits applications to series without a significant trend component, which would eventually cause the values to exit the range of past observations.

2. Additional hyper-parameters in the form of chosen Fourier series frequencies and regularization strength.

### Questions
I included a few questions in my "Weaknesses" response. I've also included a few below:

1. How were the frequencies used in the time series experiments chosen? Were they chosen a priori or through a cross-validation procedure? If cross-validation, how were the splits constructed?

2. Why not explore other bases besides the Fourier basis? Is there something intrinsically better about that basis? Alternatively, there are many other parameterizations that would encourage smoothness. For example, one could parameterize only the differences between buckets and regularize these differences to be small. The final probability mass function would be calculated by integrating the differences. Is there a reason to believe a priori that this approach might perform worse?

### Soundness
3

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
3

### Summary
The paper proposes the "Fourier head" as an alternative to linear classification heads for tasks where the output can be thought of as a quantization of a continuous space. The Fourier head learns the Fourier coefficients of the target function and then quantizes it instead of learning the quantized values directly. The authors theoretically and empirically demonstrate that varying the number of frequencies in the Fourier head trades off between smoothness and modelling performance. The Fourier head is shown to improve over the baseline linear head on a toy task, an agentic decision-making task, and for time-series modelling.

### Strengths
- The paper provides evidence that the Fourier head is an improvement over the baseline linear head in a wide variety of settings (toy example, agentic decision making, time-series modeling).
	- The Fourier head improves both smoothness and accuracy (MLE, MASE, WQL).
- The exposition of the Fourier head is clear and easy to understand.
- Various practical details (training objective, hyperparameter choice, regularization, binning strategy) are provided. This is helpful for reproducibility and to those who wish to apply the Fourier head to other tasks.

### Weaknesses
 - For regression tasks with continuous-valued target output, it is not clear to me the practical motivation for outputting an entire probability distribution, instead of just a point estimate. Thus one of the main advantages of the Fourier head, that its outputs are more smooth, feels somewhat unmotivated to me. I would like to see more discussion of why exactly the smoothness is beneficial in practice.

 - The justification of the Fourier regularization term as imposing that the coefficients decay as $1/n^2$ is a little strange to me -- this is an asymptotic condition and, in practice, there are a finite number of coefficients, so isn't the condition always vacuously met? It is unclear how the $k^2$ factor in the regularization term $\sum_k k^2 |c_k|^2$ enforces the decay of coefficients as $1/n^2$ in a truncated Fourier series. The connection between this regularization term and the smoothness of the output distribution is not clearly explained. Also, it seems that smoothness could be increased either by increasing regularization strength or decreasing the number of Fourier frequencies $N$. How do these relate? When is it appropriate to tune one vs the other?
- For the Decision Transformer, the output space as described in the paper is more naturally a quantization of $S^1 \sqcup S^1\sqcup \{0,1\}$ instead of $[-1, 1]$. (Either a shooting direction or a moving direction, each of which takes eight different values arranged on the circle $S^1$. Also two actions without an associated direction.) It would be interesting to see if the Fourier head can be generalized to output spaces that are not naturally interval-shaped.
- Actually, if I remember correctly, functions can only be approximated by Fourier series if they are periodic, i.e. functions on $S^1$. I suppose this does not affect the toy example and the time-series modelling, since the interval is chosen to be large enough that the distribution is near zero at the boundaries and so is approximately periodic. But I wonder if this is a limitation in other settings.
- Often, for tasks with continuous-valued target output (e.g. the toy example and time-series example), only a point estimate is necessary, not the full distribution. Hence a good baseline to include for the toy example is an MLP model with only one output dimension (possibly with atan nonlinearity to map outputs to the interval), evaluated on MSE. Likewise for the time-series example, but with MASE.

Minor typos:
- Line 193: "hyperparamter" -> "hyperparameter"
- Line 205: $c_n$ should be $c_k$ 
- Line 244: "and $D$ be some measure of discrepancy such that $L^2$," should be "such as"?
- Line 257: "Denote by $g_\sigma(x)$ is" delete "is"
- Line 515: "descretized" -> "discretized"

### Questions
- The justification of the Fourier regularization term as imposing that the coefficients decay as $1/n^2$ is a little strange to me -- this is an asymptotic condition and, in practice, there are a finite number of coefficients, so isn't the condition always vacuously met?
- For the Decision Transformer, the output space as described in the paper is more naturally a quantization of $S^1 \sqcup S^1\sqcup \\{0,1\\}$ instead of $[-1, 1]$. (Either a shooting direction or a moving direction, each of which takes eight different values arranged on the circle $S^1$. Also two actions without an associated direction.) It would be interesting to see if the Fourier head can be generalized to output spaces that are not naturally interval-shaped.
- Actually, if I remember correctly, functions can only be approximated by Fourier series if they are periodic, i.e. functions on $S^1$. I suppose this does not affect the toy example and the time-series modelling, since the interval is chosen to be large enough that the distribution is near zero at the boundaries and so is approximately periodic. But I wonder if this is a limitation in other settings.
- Often, for tasks with continuous-valued target output (e.g. the toy example and time-series example), only a point estimate is necessary, not the full distribution. Hence a good baseline to include for the toy example is an MLP model with only one output dimension (possibly with atan nonlinearity to map outputs to the interval), evaluated on MSE. Likewise for the time-series example, but with MASE.

Minor typos:
- Line 193: "hyperparamter" -> "hyperparameter"
- Line 205: $c_n$ should be $c_k$ 
- Line 244: "and $D$ be some measure of discrepancy such that $L^2$," should be "such as"?
- Line 257: "Denote by $g_\sigma(x)$ is" delete "is"
- Line 515: "descretized" -> "discretized"

### Soundness
3

### Presentation
3

### Contribution
3
