# Channel-aware Contrastive Conditional Diffusion for Multivariate Probabilistic Time Series Forecasting

- Decision: Reject
- Scores: 3, 8, 3, 3

## Abstract
Forecasting faithful trajectories of multivariate time series from practical scopes is essential for reasonable decision-making. Recent methods majorly tailor generative conditional diffusion models to estimate the target temporal predictive distribution. However, it remains an obstacle to enhance the exploitation efficiency of given implicit temporal predictive information to bolster conditional diffusion learning. To this end, we propose a generic channel-aware \underline{C}ontrastive \underline{C}onditional \underline{D}iffusion model entitled \textbf{CCDM} to achieve desirable \underline{M}ultivariate probabilistic forecasting, obviating the need for curated temporal conditioning inductive biases. In detail, we first design a channel-centric conditional denoising network to manage intra-variate variations and cross-variate correlations, which can lead to scalability on diverse prediction horizons and channel numbers. Then, we devise an ad-hoc denoising-based temporal contrastive learning to explicitly amplify the predictive mutual information between past observations and future forecasts. It can coherently complement naive step-wise denoising diffusion training and improve the forecasting accuracy and generality on unknown test time series. Besides, we offer theoretic insights on the benefits of such auxiliary contrastive training refinement from both neural mutual information and temporal distribution generalization aspects. The proposed CCDM can exhibit superior forecasting capability compared to current state-of-the-art diffusion forecasters over a comprehensive benchmark, with best MSE and CRPS outcomes on $66.67\%$ and $83.33\%$ cases.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents CCDM (Channel-aware Contrastive Conditional Diffusion Model), a novel approach for multivariate probabilistic time series forecasting. CCDM introduces two key innovations: a channel-aware conditional denoising network and a denoising-based temporal contrastive refinement. The channel-aware architecture incorporates channel-independent dense encoders and channel-mixing diffusion transformers to efficiently capture intra-variate and inter-variate temporal correlations. This design allows for better scalability across different prediction horizons and channel numbers. The denoising-based temporal contrastive refinement explicitly maximizes the prediction-related mutual information between past observations and future forecasts, complementing the standard denoising diffusion training.

The authors provide theoretical insights into the benefits of their approach from both neural mutual information and distribution generalization perspectives. They claim that CCDM exhibits superior forecasting capability compared to current state-of-the-art diffusion forecasters. The paper also presents a proposition on the upper bound of forecasting error for conditional diffusion models, linking the efficacy of conditional diffusion forecasters to the step-wise noise regression accuracy of the trained denoising network on unknown test time series.

### Strengths
The proposed CCDM (Channel-aware Contrastive Conditional Diffusion Model) introduces two key innovations that address important challenges in the field. First, it employs a channel-aware conditional denoising network that efficiently captures both intra-variate and inter-variate temporal correlations. This architecture, combining channel-independent dense encoders and channel-mixing diffusion transformers, allows for better scalability across different prediction horizons and channel numbers. Second, CCDM implements a denoising-based temporal contrastive refinement that explicitly maximizes the prediction-related mutual information between past observations and future forecasts. This approach complements the standard denoising diffusion training and improves forecasting accuracy and generalization on unknown test data.

Empirically, CCDM demonstrates superior forecasting capability compared to state-of-the-art diffusion forecasters. The method is also designed to be efficient, end-to-end, and seamlessly integrated with original simplified denoising diffusion optimization.

### Weaknesses
1. Lack of novelty and motivation. The paper's core contributions lack novelty in several aspects. The proposed Diffusion loss and mutual information concepts have been previously explored in the literature. Furthermore, the integration of contrastive learning loss within the Diffusion architecture seems arbitrary, and adding mutual information unnecessarily increases the complexity of the approach. While the authors attempt to justify their design choices with theoretical arguments, the discussion in lines 310-326 largely reiterates existing work (Tsai et al., 2020). The authors' decision to use KL loss approximation, necessitated by their inability to compute the upper bound in Proposition 1, is a standard approach in the field. This makes it difficult to justify the relationship between the two types of loss functions as a meaningful contribution.


2. Presentation: The paper's visual presentation suffers from several clarity issues. Figure 1's bidirectional arrows create ambiguity regarding the complementary learning pathways, and it's unclear when the losses described in equation 5 and 6 are applied. Figure 2 compounds this confusion by failing to clearly explain the implementation and timing of negative time series augmentation. Additionally, the distinction between channel-independent and channel-dependent approaches is not well articulated. The inclusion of CiDM appears redundant given that the Diffusion Transformer depicted in Figure 3 inherently supports multivariate input processing. This design choice is particularly questionable given the absence of any ablation studies to justify its necessity or demonstrate its effectiveness. These presentation issues significantly impact the reader's ability to understand the proposed architecture and its implementation details.


3. The experimental results lack clarity and comprehensive evaluation in several key aspects. First, although the proposed design makes no explicit claims about improving either short-term or long-term performance, the paper would benefit from including short-term prediction results using CSDI's benchmark datasets for better comparison. Second, the two-stage training process remains ambiguous throughout the paper. While line 289 claims to "improve the conditional denoiser behaviors in out-of-distribution (OOD) regions," no empirical evidence is provided to support this OOD performance improvement. Given the inherent uncertainty in Diffusion models, the absence of mean and variance statistics for the experimental results is a significant oversight. This statistical ambiguity is particularly problematic in Table 8, where the ablation results showing different components' contributions appear inconsistent and potentially arbitrary, making it difficult to draw meaningful conclusions about the model's effectiveness.

### Questions
1. Lack of novelty in motivation:
	- The introduction of diffusion loss and mutual information is not novel.
	- The use of contrastive learning loss in a diffusion architecture is not intuitive.
	- Introducing mutual information makes the problem more complex.
	2.	Insufficient theoretical justification:
	- The Theoretical Insights section (lines 310-326) appears to largely repeat (Tsai et al., 2020).
	- Proposition 1’s upper bound cannot be calculated in practice, which is why KL loss is used as an approximation. This is common knowledge and fails to effectively link the use of two different losses.
	3.	Unclear figures and methodology:
	-  Figure 1’s bidirectional arrows are confusing, raising questions about when to use the losses in equations 5 and 6.
	- Figure 2 adds to this confusion, leaving unclear when and how negative time series augmentation is used.
	- In Figure 3, it’s unclear why CiDM is necessary when Diffusion Transformer seems can naturally handle multivariate input. No ablation study is provided to justify CiDM's important.
	4.	Experimental results are difficult to follow:
	- Given that the proposed design doesn’t specifically aim to improve short-term or long-term performance, the reviewer suggests including results from the CSDI dataset (short-term prediction).
	- The two-stage training process is not clearly explained.
	- Despite claiming improved performance in out-of-distribution (OOD) regions (line 289), no evidence is provided to support this.
	- Given diffusion models’ inherent uncertainty, providing mean and variance of the data is crucial. This issue is particularly noticeable in Table 8, where different components’ contributions to model performance appear random.
	5.	Incomplete evaluation:
	- The paper lacks results on short-term prediction datasets (like those used in CSDI).
	- There’s no clear demonstration of OOD performance improvement.
	- The absence of mean and variance data for the uncertainty inherent in diffusion models is a significant omission.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors describe a novel diffusion model CCDM for multivariate probabilistic time series forecasting. They propose a channel-wise diffusion model with a novel training loss based on ideas from contrastive learning.
The training input $x$ and target time series $y_k$, degraded by the diffusion forward process at stage $k$, are first encoded with a known per-channel CiDM module, resulting in two equal-sized latent representations. They are concatenated and input to a standard channel-wise DiT. The transformer output is decoded yielding the estimated diffusion noise $\epsilon_k$.
Instead of training the model with the classical log-likelihood diffusion loss, the authors propose to add a contrastive loss term which takes into account one positive and $N$ negative target samples for each input sample utilizing the InfoNCE loss as introduced by Oord et. al. for general time series applications. They prove an upper bound of the denoising diffusion-induced forecasting error and finally propose an algorithm to generate the negative samples.
In experiments, the model shows improved performance compared to SOTA models on different datasets. An ablation study shows the influence of the contrastive weight on the performance and reveals that the choice of the number of negative samples is critical and needs to be found empirically by hyperparameter search.

### Strengths
The idea of extending the diffusion loss with a contrastive loss is new and interesting. The architecture of the model is built from known building blocks, but not known in this combination. The authors give a thorough prove concerning the properties of the forecasting error. They present a comprehensive bibliography.

### Weaknesses
A general weakness of the interesting idea is that (p 20, section A10) the real effect of $N$ is intractable and the optimal value must be found by hyperparameter search.

p 3: $y_0$ and $y_K$ is introduced one section too late

p 4: wording: accounts for … and can be any types of … (unclear)

p 5: replacing point-wise attention by channes-wise attention. (Could you elaborate this shortly?)

p 6 l 275: both a positive sample

p 7 l 327: efficiency

p 9: While the tables in the appendix show the influence of the constrastive learning, it is really hard to interpret the positive effect from figure 5. Can this be stated more clearly?

### Questions
p 3: $y_0$ and $y_K$ is introduced one section too late

p 4: wording: accounts for … and can be any types of … (unclear)

p 5: replacing point-wise attention by channes-wise attention. (Could you elaborate this shortly?)

p 6 l 275: both a positive sample

p 7 l 327: efficiency

p 9: While the tables in the appendix show the influence of the constrastive learning, it is really hard to interpret the positive effect from figure 5. Can this be stated more clearly?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes CCDM which is able to train a diffusion model for time series forecasting via the combination of a denoising loss and a contrastive loss, which they call a "neural mutual information" perspective.  This allows for the training of probabilistic forecasts in a deep learning setting, following other recent works.  By allowing for probabilistic forecasts, they are able to train a more accurate diffusion model when compared to historical regression-only style models.  Comparing across standard benchmark datasets and against several other baseline methods, favorable performance is achieved in the MSE (regression) metric and CRPS (probabilistic) metric.  Several ablation studies then confirm that the contrastive loss function is useful in diffusion model training.

### Strengths
The topic of how to combine the diffusion models of deep learning with the probabilistic forecasting of time series seems like an important and emerging area.

The specific success of contrastive learning in aiding the diffusion model in CRPS performance is demonstrated through ablation experiments.

Good performance is achieved in many datasets and on many tasks.

### Weaknesses
The theoretical insights do not seem cohesive.

The contribution seems extremely simple or are not well highlighted.  After reading, I have the understanding that the major or only contribution is the application of contrastive learning to diffusion models, as depicted in Figure 1.  If that is the case, it is not properly highlighted and the challenges are not sufficiently discussed.

Further probabilistic analysis like the one in Figure 4 could be helpful for emphasizing the impact of this work.

Is it possible to provide error bars for Figure 5? I understand the claim is that contrastive learning is helpful; however, looking at these figures, I get the completely opposite impression that actually the contrastive learning is doing almost nothing.  Perhaps it is possible to further explain these results.

If a key contribution of the work is the method to apply contrastive learning in the time series domain, can you elaborate on what the specific challenges of applying contrastive learning to time series data are?

### Questions
Can you clarify what is the difference between your proposed "neural mutual information perspective" and the combination of a denoising loss and contrastive loss?

Can you explain what the contributions are compared to the existing works [1] and [2]?  From reading the related work section, I got the impression that the other diffusion-based methods which "repurpose DiT" should be the closest related works; however, getting to the experiments it seems these two methods are not compared.

Is it possible to provide error bars for Figure 5? I understand the claim is that contrastive learning is helpful; however, looking at these figures, I get the completely opposite impression that actually the contrastive learning is doing almost nothing.  Perhaps it is possible to further explain these results.

If a key contribution of the work is the method to apply contrastive learning in the time series domain, can you elaborate on what the specific challenges of applying contrastive learning to time series data are?


[1] "Timedit: General-purpose diffusion transformers for time series foundation model" Defu Cao et al. 2024.

[2] "Latent diffusion transformer for probabilistic time series forecasting" Shibo Feng et al. 2024

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper innovatively designs a composite channel-aware conditional denoising network (CCDM) that merges a channel-independent dense encoder to extract univariate dynamics and a channel diffusion transformer to aggregate cross-variate correlations. And a time-contrast learning based on self-organized denoising is designed to explicitly amplify the predictive mutual information between past observations and future predictions. The method can consistently complement the plain stepwise denoising diffusion training to improve the prediction accuracy and generalization of unknown test time series.

### Strengths
Learning generalisable multivariate probability distributions based on a step-wise denoising paradigm is a pivotal problem where there are two challenging obstacles, firstly how to establish cross-channel temporal correlation connections between observed and denoising predicted sequences, and subsequently how to improve the capability to mine implicit representations from a given time series. 

To address these two issues, the authors propose two innovative architectures: 

* The channel-independent dense encoder and the channel-diffusion transformer to extract univariate and aggregated cross-variate correlations, respectively.

* Self-organized denoising-based temporal contrast learning to consistently complement plain stepwise denoising-diffusion training.

### Weaknesses
 **Weakness 1:** 

CCDM proposes contrastive learning for self-organizing denoising as a consistent complement to naive stepwise denoising diffusion training. Contrastive learning is a typical discriminative self-supervised learning. Compared with generative self-supervised learning, contrastive learning only needs to determine whether the sample is positive or not, and the low difficulty of the training task may lead to the model not being fully trained. 

In addition, CCDM establishes the training paradigm based on a contrastive learning strategy that maximizes the mutual information between input and output. However, the model will be applied to the generative task based on prediction. The discriminative representation information learned by the model during the training phase varies dramatically for downstream generation tasks. To the best of our knowledge, large models trained in a self-supervised manner often need to design efficient fine-tuning strategies to adapt them to specific downstream tasks, while CCDMS directly reason on concrete datasets after being trained with pairwise learning.

**Weakness 2:** 

There has been a lot of research (Crossformer[1], LIFT[2], SAMformer[3]) on building cross-channel connections between multivariate time series. The hybrid channel-aware denoising architecture proposed by CDDM includes two main structures, Channel-wise Diffusion Transformer and Channel-independent Dense Module (CiDM). CiDM, which is not originally from this article but from TiDE[4], The Channel-wise Diffusion Transformer looks like it combines the Dimension-Segment-Wise (DSW) structure designed in Crossformer[1] with the conditional diffusion model. These shortcomings make CCDM an incremental summary work rather than innovative research.

**Weakness 3:** 

The lack of advanced baselines leads to the inability to verify the competitiveness of the proposed CCDM. Specifically, only four baselines based on Diffusion are shown in Table 1, and both SSSD and CSDI are published in 2021. 

More extensive performance comparisons are expected to fully validate the effectiveness of the proposed method. The proposed baseline can be introduced in five sections:

* Models based on pre-trained LLM alignment to TS, OneFitsAll, TimeLLM, LLM4TS.

* Pre-trained time series base models on unified time series datasets from multiple domains, such as Timer, Moriai, Moment, UniTime.

* Small datasets to train and test on specific datasets, e.g. PatchTST, iTransformer[5], ModernTCN[6].

* Recent diffusion-based time series probabilistic prediction models, such as Diffuison-TS[7], mr-Diff[8], MG-TSD[9].

* Self-supervised prediction models based on contrastive learning and mask reconstruction SimMTM[10].

The CCDM is expected to be compared with at least one competitive model in each forecasting paradigm to indicate the plausibility of the model design.

Even compared with the four baselines in Table 1, CCDM has almost no performance improvement on all six datasets. Specifically, on the ETTh dataset, the MSE of CCDM is only 0.0017 lower than that of TimeDiff. On the Exchange, Appliance and Weather datasets, CCDM shows worse performance than TimeDiff and CSDI. On Electricity and Traffic datasets, the average improvement of CCDM in MSE metric is less than 10%.

**Weakness 4:** 

In the ablation experiment (Table 2), after removing contrastive refinement, the model improves only 1.2% and 1.08% on ECL and Traffic datasets. 

In addition, another confusing result is that ETTh and Weather have a small number of channels (7 and 21), while ECL has a huge number of channels (321). However, after removing the channel-wise design, On the contrary, the performance in ETTh and Weather drastically decreases (23.34% and 40.28% in MSE), and the performance in the ECL barely changes (5.71% in MSE). 

This may indicate that channel-wise designs fail to capture cross-channel latent representations from datasets with a large number of channels and instead perform well in other datasets with a smaller number of channels. The results of ablation experiments are negative and difficult to understand for the main thrust of this paper, "establishing cross-channel connections in Diffusion models".

### Questions
**Question 1:** 

See Weakness 3 for our concerns about the experimental results, and we believe that the introduction of competitive and up-to-date baselines is considered necessary.  In addition, the authors are expected to explain the phenomena in the ablation experiments, details of which can be referred to Weakness 4.

**Question 2:** 

It is mentioned in the main text that "density ratio function can be any types of positive real functions". Is there a clear strategy to determine the best density ratio function for different time-series data domains? Does designing different density ratio functions indirectly affect the training effect? How to construct similar and dissimilar instances to prevent model collapse? We believe that the construction of negative samples is critical to applying CCDM to a wide and diverse real-world setting.

**Question 3:** 

As far as we know, contrastive learning tends to consume a lot of computational resources. Specifically, we often need tens of thousands of iterations to fully train the diffusion model, and the total training overhead is staggering if we need to generate a set of n negative samples based on each positive example at each iteration. Therefore, theoretical analysis complexity and experimental results on time overhead of CCDM are necessary for their potential real-world applications.

### Soundness
1

### Presentation
2

### Contribution
1
