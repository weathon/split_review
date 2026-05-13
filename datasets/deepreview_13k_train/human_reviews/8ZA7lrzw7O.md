# Sharper Analysis of Data Echoing and New Communication-Efficient Algorithm for Data Parallelism

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Over the past decade, breakthroughs in both general-purpose and specialized hardware have propelled the success of large-scale machine learning. However, the advancements in general-purpose hardware are not keeping pace with those in specialized hardware. Consequently, operations conducted on the general-purpose hardware have become the primary performance bottleneck. Notably, data loading significantly lags behind the gradient computation during training. To address this issue, the technique of data echoing has been introduced, whereby the current batch of samples is reused for gradient computation to minimize idle time while waiting for new data. However, this approach can lead to overfitting on the current batch, and it remains unclear whether convergence benefits from this practice. In this paper, we provide a sharper analysis on a stochastic variant of data echoing and show that it obtains linear speedup proportional to the number of reuse times. Additionally, we investigate the impact of the communication bottleneck in data parallelism of data echoing, and propose a new communication-efficient data echoing algorithm via reducing the frequency of model averaging. We then show that it is possible to perform data echoing without additional communication cost with data parallelism. Finally, we perform empirical experiments to verify our analysis on the data echoing and the proposed efficient algorithm for data parallelism.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new analysis (ie extending and improving previous work) of data echoing, an important technique use in practice in the training of DNN.
Moreover, the author also propose a new (communication efficient) technique tackling the problem of communication bottleneck.
 Numerical experiments support the proposed techniques.

### Strengths
- The paper is well written, easy to follow and the contributions are stated clearly.
- the paper proposes an improvement/extension over the work of  Agarwal et al. (2020) by extending their results to the non-convex setting and do not require the gradients to be bounded. Rather, they propose require an assumption present from in Even, 2023. I have not written the proof in details, but I am not surprised by this result.
- to the best of the reviewer's knowledge the problem of finding  "communication efficient data echoing algorithm" has not been addressed in the litterature. The reviewer this is in an interesting direction worth tackling (which this paper does)

### Weaknesses
 - the reviewer finds the idea of the cosine scheduler for data loading probability particularly interesting. 
However, the reviewer wishes to see some theoretical/formal arguments on the soundness of this technique/how this impacts convergence/the results developed in the paper.
Perhaps this is trivial (admittedly the reviewer is not an expert on this topic). In any case, the reviewer does believe this should be stated/clarified.
- The numerics should be more extensive/have more results. MobileNet-V2 are not SOTA anymore (see MobileNet-V3). Moreover, the application is for the training of neural nets. Hence the reviewer expects that results for more modern/SOTA architectures  (transformers....) should be present, regardless of the speed of these architectures at inference time. 
- please edit the graphs in figure 4/5 to include the name of the dataset, model and lr (as title for instance....)

### Questions
- please see my comment above on cosine LR schedulers and the comment on the architectures used for the numerical experiments
- the reviewer is curious how definition 3.1 differs from the definition of a "standard" markov chain.
Note that i am not raising this in the "weaknesses" section but I do believe this could be clarified/highlighted.

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
2

### Summary
This paper provides a convergence analysis for SGD with reused data samples (i.e., dada echoing). The analysis is standard for non-convex optimization; however, it uses an unusual assumption (line 076) that the gradient is still unbiased with the reused data samples.

### Strengths
1. The work is well-motivated: As data movement is expensive in modern computer systems, data reusing can significantly improve the performance of neural network training. Previous work has shown practical benefits and preliminary theoretical results for reusing data samples in SGD. This work aims to provide a sharper analysis for the data echoing algorithm. 

2. Presentation is good: The paper is well written. The author clearly described the data echoing algorithms and their theoretical results.

### Weaknesses
My main concern about the paper is the unusual assumption it uses (line 076). The key difference between standard SGD and data echoing SGD lies in gradient computation. For standard SGD, we can assume unbiased gradients due to i.i.d. sampling of data. However, for data echoing SGD, I strongly suspect this assumption doesn't hold. If we could make the same assumption for data echoing, I don't see how the analysis would differ from standard SGD.

The core issue is that the gradient at step t+τ, using a batch B_{t+τ} that is derived from the echoed data, is unlikely to be an unbiased estimate of the true gradient at x_t. The data echoing process introduces a dependence between B_t and B_{t+τ}, which violates the standard assumption of independence required for unbiased gradient estimates. The assumption that the gradient is unbiased for large enough τ seems problematic because in the actual algorithm, τ is limited by M, the size of the echoed data buffer. It is unclear how the analysis accounts for this limitation, and how the diminishing correlation between B_t and B_{t+τ} translates to an unbiased gradient estimate when τ cannot be arbitrarily large.

Furthermore, the paper lacks a clear explanation of how the Markov chain view of the data echoing process directly leads to the unbiased gradient assumption. While the mixing time concept is mentioned, the connection to the specific gradient calculation is not sufficiently detailed. The analysis needs to explicitly demonstrate how the diminishing correlation, due to the Markov chain property, ensures that the gradient calculated with echoed data is an unbiased estimate of the true gradient, especially when τ is bounded by M.

### Questions
You assume the gradient is unbiased for large enough $\tau$; however, in the actual algorithm, I guess $\tau$ is limited by M. Can you give more explanation on the assumption?


----
It seems the discussion period has ended -- The authors posted responses at the last minute which does not give time for thorough discussion. 

The last response from the authors is interesting. How could you say something is large enough with big O notation, shouldn't it be $\Omega$. At this point, I feel  that either I have a serious misunderstanding of the paper, or there are serious errors in the paper. Too bad we don't have time for sufficient discussion. I will leave it to the AC and other reviewers for the final decision.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper suggests a markovian perspective when analysing the data echoing algorithm, the technique that allows to mitigate the data loading overhead. Data echoing combined with Stochastic Gradient Descent uses the biased gradient in the parameter update. The authors show the boundedness of such bias under mild assumptions and run a few experimental runs to show its efficiency in practice. In addition to that, they introduce a novel data echoing algorithm that is adjusted to data parallelism setting.

### Strengths
The authors tackle more general setting than the prior works by considering non-convex optimization problems. They take an interesting approach to model data echoing in SGD through Markov chain processes. They provide an analysis of the problem, proving the comparable convergence to SGD while having a linear speedup in terms of number of reuse steps. 

The authors also provide an adaptation of the data echoing algorithm to a data parallelism setup. They noticed that the communication that happens when synchronizing the weights negates the benefits that data echoing introduces for a single node setup. Thus, they combine a data echoing algorithm with the delayed weight synchronization to keep idle time low, while proving the convergence of the novel optimization scheme. 

Overall, the work extends on the previous line of work with an interesting algorithmic and theoretical contributions.

### Weaknesses
As a person who has not been familiar with data echoing before, I find the experimental results counter-intuitive and misleading. In particular, they do not answer the question "if your hardware has a particular data loading speed what level of data echoing you need to use?".

I see the data echoing technique as a way to reduce the idle time that is due to the long waiting for the next loaded samples. So I expect data echoing may decrease the total training time, but as a method that uses a biased gradient estimation, it should require more optimization steps to converge to a minimum compared to a vanilla SGD. In the experimental section we only see experiments with respect to «number of example loads», which creates an impression that data echoing is in general always better than SGD. This paper lacks more figures that are plotted against the number of gradient steps or epochs to see a bigger picture and compare convergences. More thorough experimental section would provide a better intuition whether you need to use data echoing or not if your hardware support a certain data transfer speed.

Moreover, to have a fair comparison of the data echoing algorithm and SGD, we need to choose the best learning rate for each algorithm independently, right now the learning rate is the same for both algorithms. Indeed, if roughly speaking data echoing performs as an SGD that reuses the same batch several times, then the similar effect can be sometimes obtained by increasing the learning rate for SGD, which can be partially observed on some figures.

Concerning the theoretical analysis, the convergence results look reasonable, but the proofs are not easy to follow as some derivation steps are either skipped or not explained, which makes it harder to read and thus verify the correctness of the proofs for a person not familiar with this line of work. Overall, the appendix seems to be written hastly, I suggest the authors to pay more attention to how they explain their derivations and add missing details in the proofs.

Minor remarks:

line 038: parallelism -> parallel

line 237: slow -> slows

line 265: it is stated that $\nabla f(x_t, B_t)$ approximates well $\nabla f(x_{t-\tau})$ and that it follows from Lemma 3.6. Please comment more on this as it is not a straightforward induction

line 307: explain how do you get the minimum burn-in time (a lower bound for T)?

line 363: effect to -> effect on

line 370: $c_{\nu}$ was never introduced before

Use $\times$ or $\cdot$ for multiplication, instead of *

Figure 1 from the main paper contradicts the description in the appendix, as in one place higher i means higher data loading speed, in other place the opposite.

I suggest using separate numbering for Definition, Lemmas and Theorem independent of section number, so that there are Theorem 1 and Theorem 2, instead of Theorem 3.8 and Theorem 4.2

In equation 4, I would use $p_t$ instead of $p$ directly to simplify Algorithm 1 and 2 descriptions (e.g. line 3 of Algorithm 1)

The order of Figures doesn’t follow their order of mentioning in the text

### Questions
Can you do an experiment where each algorithm is compared with their best corresponding learning rate? (see above)
How to set your algorithm for a given data loading speed for it to do the best performance?

Please provide the modern GPU performance numbers for a standard SGD algorithm and what it corresponds to in figure 1?

The equation 8 in the appendix is explained with independent sampling property, which seems to contradict the whole Markov Chain formulation of the optimization problem where $d_l$ depends on $d_{l-1}$ due to data echoing. Can you please explain these transitions more in detail?

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
2

### Summary
This paper provides a sharper analysis of previous data echoing work. The paper concludes that data echoing can get linear speedup proportional to sample reuse times. Then it proposes reducing gradient averaging frequency based on data echoing frequency to reduce communication cost. For evaluation, this paper adopts a cosine diminishing schedule for data echo probability and valid its effectiveness.

### Strengths
Theoretical proof of data echoing achieving linear speedup proportional to num of reus times. The authors formulate stochastic data echoing as Markov chain gradient descent problem and provide a sharper analysis.

data echo is a good direction for reducing data loading overhead in distributed environments.

The proposed cosine diminishing schedule on data echoing achieves better model test accuracy.

### Weaknesses
1 ) the paper lacks of systematic understanding of how distributed training works and what could be bottleneck. For example, one major contribution in this paper is to reducing cross GPU communication frequency for gradient averaging with probability p^{c}_{t} (detailed in Algorithm2 and section 4). It does not consider how it can be grounded in real world training.

1.1) If every GPU's triggering gradient averaging probability is i.i.d, then it is almost impossible to pre-allocate and pre-form the GPU communication group for each gradient averaging collective. If forming communication groups ad hoc, it means every time before starting communication, we need to initialize a new communication group and ping every involved GPU to build connection, which will be much bigger overhead compared with reduced communication frequency gain. This overhead would likely negate any benefits from reduced communication frequency, making the approach impractical for real-world distributed training.

1.2) If all GPUs communicate at same time but with lower frequency, this kind of techniques already exists as gradient accumulation steps. Further more, comparing with data echoing's reducing data communication frequency with probability and may have model training accuracy loss, gradient accumulation step can mimic identical model training loss curve of pure distributed data parallel (DDP) but communicate gradient at a much lower frequency. The paper does not adequately address why data echoing with probabilistic gradient averaging is superior to gradient accumulation, which is a simpler and more established technique.

2 ) the paper lacks major results. LLM is a good example for distributed model training. As mentioned in Sec.5, the paper also use wiki text and gpt-2 model training for evaluation. However, I could not find any results in the paper. The only results on cifar-10/100 + small CNN like resnet/mobilenet usually do not need distributed training. Therefore cifar10/100+ small CNN results are not very convincing. The absence of results on larger models and datasets makes it difficult to assess the practical value of the proposed method.

3 ) The paper is lack of novelty. Two major contributions in this paper. First it provides a tighter convergence analysis of previous work of data echoing via formulating stochastic data echoing to markov chain gradient descent. This first contribution is theoretical contribution but does not proposing any new idea. The second contribution is reducing cross-GPU gradient averaging frequency based on data echoing frequency. The idea seems novel in data echoing setting, but there is a much widely adopted and existed approach call gradient accumulation step, which does not hurt model training accuracy at all while reducing gradient averaging communication frequency. One minor novelty is adding cosine diminishing schedule on data echoing, but this novelty contribution is limited, since any diminishing schedule may work in data echoing setting.

minor issues:

all the figures from fig3 to fig7 (especially fig7) in both x and y axis, the texts are too small to see even enlarge to 200%.

### Questions
How does communication with some probability compared with widely used gradient accumulation step approach? To me, gradient accumulation step approach does not hurt any model training accuracy loss and much easier to be used in real world applications (i.e. reuse the same communication groups all the time with NCCL/RCCL).

How would this paper's approach works in real distributed training environment? (either larger dataset like imagenet, or larger models like gpt-2/3, llama-2/3)

### Soundness
2

### Presentation
2

### Contribution
2
