# Locally Connected Echo State Networks for Time Series Forecasting

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Echo State Networks (ESNs) are a class of recurrent neural networks in which only a small readout regression layer is trained, while the weights of the recurrent network, termed the reservoir, are randomly assigned and remain fixed.
Our work introduces the Locally Connected ESN (LCESN), a novel ESN variant with a locally connected reservoir, forced memory, and a weight adaptation strategy.
LCESN significantly reduces the asymptotic time and space complexities compared to the conventional ESN, enabling substantially larger networks.
LCESN also improves the memory properties of ESNs without affecting network stability.
We evaluate LCESN's performance on the NARMA10 benchmark task and compare it to state-of-the-art models on nine real-world datasets.
Despite the simplicity of our model and its one-shot training approach, LCESN achieves competitive results, even surpassing several state-of-the-art models.
LCESN introduces a fresh approach to real-world time series forecasting and demonstrates that large, well-tuned random networks can rival complex gradient-trained models.
Additionally, we provide a GPU-based implementation of LCESN as an open-source library.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work the authors propose an Echo State Network for time series prediction whose most distinctive properties lie in a local (small-world) connectivity pattern of its neurons as well as an approach termed memory forcing where neuron activations of various previous timesteps are linearly combined with the current activations. In combination with rigorous hyperparameter optimization by means of an evolution strategy, the proposed models manage to outperform classical ESNs at a selection of timeseries prediction tasks as well as achieve on-par performance to transformer-based models on a wide variety of prediction benchmarks.

### Strengths
Overall, the work is executed well. All ideas and approaches are explained clearly, the manuscript is well-written and the visual quality of its figures is sufficient. 

The strongest point of the paper is it's extensive experimental evaluation with a wide range of state-of-the-art methods as well as the proposed method showing a viable alternative to the transformer architecture. This is especially important as previous work [1] suggests that transformers are less than optimal for timeseries prediction due to the intrinsic permutation equivariance of the attention module. Therefore, in principle, I consider this work to be of interest to the ICLR audience.

[1] https://github.com/valeman/Transformers_And_LLM_Are_What_You_Dont_Need

### Weaknesses
A comparison to transformer models with respect to runtime for a typical amount of hyperparameter-configurations is missing (see below for elaboration). Furthermore, in the reservoir computing literature a number of approaches closely related to the ones proposed in the manuscript have already been explored in the past (see below for references).

While the final least squares training of an ESN tends to be very fast, the authors conduct an extensive hyperparameter optimization. Due to the relatively large amount of hyperparameters optimized, as well as their strong influence on the dynamics of the echo state network, especially w.r.t. memory capacity and nonlinearity, I consider this optimization process as a form of training in itself, which should be accounted for when comparing model's training times. 
To actually reliably assess whether the proposed ESNs constitute a faster/easier-to-train alternative to a small transformer model, where in general fewer hyperparameters need tuning, the manuscript should contain more detailed  timing information w.r.t. the time required to find an ESN suitable for a given task, and compare these timing with the time needed to find good hyperparameters to achieve comparable performance on a state-of-the-art transformer model on that task. The comparison should not only focus on the final training time but also on the time required for hyperparameter optimization, which is crucial for a fair comparison.

In my experience, transformers tend to perform rather well for most tasks with somewhat universal and task-agnostic default hyperparameters (i.e. Adam optimizer, learning rate 1e-3, dropout 0.2 etc.). Echo State Networks on the other hand, due to the fixed nature of their hidden layer, typically require much more rigorous hyperparameter tuning than current gradient-based-models (see e.g.  [1])

A comparison between the execution time of the finally trained ESN and a similarly performing transformer model would be important as well to precisely quantize the dimension of the gained speedup. 

For the proposed approaches and methodologies, closely related work exists in the reservoir computing literature:

- In terms of drawbacks of ESNs as introduced by the authors, I strongly disagree with the third point (Ln 53): the output layers of reservoirs have been trained online using LMS, RLS and other gradient-based approaches since the early 2000s, most-prominently as Backpropagation-Decorrelation [2] but also in other forms [3,4,5].

- Locally connected reservoirs and reservoir computing with small-world networks have been investigated in the 2010s especially in the reservoir-computing-as-neuromorphic-hardware-community, where fully connected networks imply high wiring effort, e.g. see [6,7]

- I consider the memory-forcing-approach introduced by the authors a more explicit formulation of a mixed internode-delay reservoir computing approach which has previously been explored in the literature, most recently as Distance-Delay-Networks [8], where the parameters of a distribution determining the length of variable inter-node-delays in ESNs using CMA-ES. While this approach takes a more biological view than the memory-forcing approach in this manuscript, with the exception of an optimized "memory-leak-factor" (w_{\text{mem}} in the manuscript), the actual implementations appear almost identical to me.
  
- In general, while the authors provide clear intuitions on the underlying issues, the discussion of background work on reservoir computing and dynamical systems falls somewhat short in the manuscript. For well-researched issues such as the proverbial "edge of chaos" or memory in reservoir computing systems, only very few references are given.

### Questions
Ln 129:  I am not familiar with describing a uniform distribution through  parameters /mu and /sigma (notation and methodology). They seem to loosely correspond to input scaling and bias scaling as used in reservoir literature? 

Ln 143: Are hyperparameters for baseline ESNs optimized with CMA-ES as well?

In order to gauge the effectiveness of the proposed improvements to real-world tasks, additionally reporting the performance of an ESN baseline, for which the hyperparameters have been optimized using the same process (evolution strategy) and compute budget applied to find good LCESNs for all (or at the very least: several) tasks would be nice to have.. 

On metrics: As the MSE of NARMA-10 is typically dependent on the scaling of the input signal, in literature it is typically normalized by the variance of the target signal and reported as the Normalized MSE (NMSE) [1]. While the very low MSE values reported in the manuscript suggest sufficient performance, they are hard to interpret without context. Considering the limits of floating point precision, I am unsure on whether comparing values between 1e-8 and 1e-13 yields applicable insight (Figure 5). I would recommend reporting the NMSE instead and eventually additionally plot signal traces to demonstrate how well the proposed approach approximates the target signal.


[1] Jaeger, H. (2002). Adaptive nonlinear system identification with echo state networks. Advances in neural information processing systems, 15.

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
This paper builds on Echo State Networks by providing specific structural constraints through local connections. Further, specific memory context is encoded through skip/residual temporal connections. The updated architecture is presented as a novel framework titled Locally Connected ESN (LCESN) and it's performance is benchmarked against nine real-world datasets.

### Strengths
The paper introduces a unique architecture and framework to ESNs via the introduction of locally connections. Second, by providing a fixed context length the authors introduce memory forcing which is motivated to prevent the network from being unstable. Third, the authors present multiple weight adaptation strategies. Taken together the authors present a novel architecture of ESNs and a gradient-free training procedure for them. Lastly, they test their framework to be computationally and memory efficient and evaluate their results on real-world datasets.

### Weaknesses
1. While the authors motivate the problem, little to no information/references are provided on some critical components. For instance in the introduction section the authors discuss main advantages of ESNs but do not provide any references. Critically, the paper misses references to additional reservoir computing frameworks like FORCE (Sussillo, David 2009)/FULL-FORCE (DePasquale 2018).
2. The paper is motivated by providing better time and space complexity on the ESN step, however this step is never formalized or discussed in the paper. 
3. They restrict their models to have a weight adaptation after every 100 steps, however it's unclear if more/less steps could lead to better/worse performance.
4. The authors “proposed topology is designed with GPUs in mind”: however there is no link/discussion describing why the torus structure scales well with GPU architecture.

### Questions
1. Can the authors expand on why their method reduces the time and space complexity? 
2. The authors motivate forced memory for the network to be stable. Can the authors provide additional discussions/experiments relating this to the "edge of chaos"? i.e is there a temporal look-back connection at which the network transitions from being chaotic to stable, with highest performance? Additionally, can the authors provide clarification on why a max delay of 100 was set?
3. In section 3.5 the authors present multiple ways to update W_out. Are these all novel methods? Is there a reason W_out is retrained every 100 steps? how does this change with larger/fewer steps?
4. Fig 5,6,7: Confusion on results: Can the authors provide some clarification/insight on why locally connected ESNs without forced memory perform better that ESNs? From Fig 5 it appears larger networks are better, however kernel size doesn't significantly affect performance. Yet, table 1 and fig 7 show ESNs perform worse than LCESN. Can the authors provide theoretical/empirical experiments discussing at what kernel size LCESNs behave like ESNs?
5. Is there a relation to the kernel size and forced memory with the data being presented? I.e how do LCESNs perform on datasets with longer term time dependencies compared to ESNs and other state of the art methods?
6. Can the authors provide insight on how this method compares to methods like FORCE/full-FORCE where structure is provided in W_feedback instead of within the reservoir itself?

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
4

### Summary
This work considers time series forecasting problem and introuces an ESN-based architecture to tackle this problem. The authors are motivated by ESNs' strengths but note that previous works show that their performance may be lacking compared to alterantive appraoches. The authors note three potential reasons for their lack of performance: constraint on reservoir size, ESN's memory-stability tradeoff and a lack of adaptive training of the readout as the new data arrives. 

The authors address all of these points by intruducing local connectivity in the reservoir, memory forcing, and evaluate their approaches under a multitude adaptive strategies of the readout weights updates. Author's approach appears to outperform vanilla ESNs and are competitive with SOTA approaches.

### Strengths
- Overall the presentation of the work is clear.
- Three key components for enhancing ESNs' performance appear sound; their advantange is illustrated well. I think the ESN community will appreciate such results. Comparisons against vanilla ESN in terms of performance and wall-clock time are appreciated.
- The methods are compared on a difficult benchmark.

### Weaknesses
1. The final performance of LCESN doesn’t fully reach SOTA levels, despite this being a main goal of the paper. While results are comparable to SOTA, the primary advantage of ESNs—fast training and inference times—is not fully emphasized, aside from a brief mention. Without a comparison of these speed benefits against SOTA methods (including hyperparameter search and inference times), the broader appeal of using ESNs, especially over vanilla ESNs, may be limited.
2. The comparisons in Table 2 have some notable omissions:
	- There is no comparison against a vanilla ESN.
	- TSMixer, the best-performing model, isn’t evaluated on some datasets. Claims about model ranking may be misleading, as TSMixer could outperform the authors' LCESN model. While the original paper did not evaluate TSMixer on the two excluded datasets, either these datasets should be excluded, or TSMixer should be evaluated on them.

### Questions
- Conceptually, is forced memory in your approach equivalent to stacking up the hidden state vectors from a pre-defined range in history under a vanilla ESN setting?
- Could a relative ranking matrix be added across the methods? For example, an N x N matrix showing how many times model *i* outperformed model *j* across datasets, to summarize the results in Table 2.

### Soundness
3

### Presentation
3

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
Interesting work and a solid paper.

It presents an ESN architecture with a cleverly designed local connectivity, whose primary goal is to overcome the computational limitations of traditional ESNs.

The interpretation of the results could be expanded. In particular, it is unclear why and how the forced memory positively affects the outcomes.

### Strengths
The algorithm’s motivations are clear, and they are fulfilled by the current algorithm.

As a bonus, it performs better on certain tasks compared to the other algorithms investigated.

The paper’s presentation is mostly clear, and the results are correctly interpreted.

### Weaknesses
The analysis of the model is really small. You proved that your ESN connectivity performs better than others ESN on a variety of benchmark, but advanced no reason as why it would be the case. See question 1.

Similarly,  It's still unclear to me what are the real advantage of the forced memory and there is really few motivations for its design, that would have been great to see further explanation of that.

You should the following minor changes anyway :
* You should change the legend of figure 5 so that it matches the order of your results and be ordered by size. 
* LCESN-LMS is never clearly defined but is understood from context.

### Questions
- You should discuss why local clustering improves performance compared to classic ESNs. In particular, the performance of your algorithm seems to increase with kernel size (as highlighted by Figure 5). Doesn’t this suggest that a standard ESN, which is equivalent to having a kernel size equal to the size of the ESN, should perform better?

- I have already emphasized the lack of justification for the forced memory mechanism. You briefly mentioned the leaky neuron; you should evaluate the performance of the leaky neuron compared to the forced memory mechanism.

- You argue that the primary advantage of your algorithm is the faster matrix multiplication, which in turn allows for larger networks. However, ESN connectivity can be very sparse, meaning the methods used to compute matrix products will differ from what you propose in the paper. You should compare the performance of your algorithm with sparse matrix multiplication.

### Soundness
2

### Presentation
3

### Contribution
3
