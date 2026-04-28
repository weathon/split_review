# UTSD: Unified Time Series Diffusion Model

- Decision: Reject
- Scores: 5, 6, 5, 5, 5

## Abstract
Transformer-based architectures have achieved unprecedented success in time series analysis.
However, facing the challenge of across-domain modeling, existing studies utilize statistical prior as prompt engineering fails under the huge distribution shift among various domains.
In this paper, a Unified Time Series Diffusion (UTSD) model is established for the first time to model the multi-domain probability distribution, utilizing the powerful probability distribution modeling ability of Diffusion.
Unlike the autoregressive models that capture the conditional probabilities of the prediction horizon to the historical sequence, we use a diffusion denoising process to model the mixture distribution of the cross-domain data and generate the prediction sequence for the target domain directly utilizing conditional sampling.
The proposed UTSD contains three pivotal designs: $(1)$ The condition network captures the multi-scale fluctuation patterns from the observation sequence, which are utilized as context representations to guide the denoising network to generate the prediction sequence; $(2)$ Adapter-based fine-tuning strategy, the multi-domain universal representation learned in the pretraining stage is utilized for downstream tasks in target domains; $(3)$ The diffusion and denoising process on the actual sequence space, combined with the improved classifier free guidance as the conditional generation strategy, greatly improves the stability and accuracy of the downstream task.
We conduct extensive experiments on mainstream benchmarks, and the pre-trained \myformer outperforms existing foundation models on all data domains, exhibiting superior zero-shot generalization ability. After training from scratch, \myformer achieves comparable performance against domain-specific proprietary models. In particular, \myformer shows stable and reliable time series generation, and the empirical results validate the potential of \myformer as a time series foundational model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes a Unified Time Series Diffusion (UTSD) model for time series tasks (mainly focusing on forecasting tasks). The model utilizes a diffusion-based approach rather than traditional autoregressive methods. In particular, the conditional network, adaptor fine-tuning strategy are considered. Numerical experiments and sample codes are provided.

### Strengths
1. This paper considers an interesting research topic which trying to apply the diffusion model into time-series analysis domain.

2. Various experimental tasks are considered and cover diverse domains and performance comparisons against both foundation models and domain-specific models.

### Weaknesses
1. My primary concern lies in the suitability of employing a non-autoregressive diffusion model for forecasting tasks. Forecasting is typically a regression problem rather than a generative one, and autoregressive behavior is often observed in certain domains, such as climate and finance. Given this, the current draft would benefit from further justification regarding the choice of a non-autoregressive diffusion model in this context.

2. The architecture of the proposed model requires further discussion. Section 3 describes the proposed model as a combination of convolution and attention blocks. However, existing literature shows that models based solely on either convolutional or attention networks are already effective for forecasting tasks. Could the authors clarify why a hybrid structure is necessary here? Specifically, how does this configuration address any limitations of diffusion models in forecasting?

Minor Issue: In Appendix E.2, the benchmarks also include imputation and classification tasks, but these seem to be missing from the main draft.

### Questions
Please see the weakness section.

At this stage, the novelty of the work is insufficient for acceptance at a top-tier machine learning conference, so I tend to recommend rejection. However, I am open to reconsidering my evaluation based on further discussion.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces UTSD (Unified Time Series Diffusion), a novel diffusion-based model for multi-domain time series forecasting. The key contributions include:
- A condition-denoising architecture that captures multi-scale temporal patterns
- Direct modeling in actual sequence space rather than latent space
- An improved classifier-free guidance strategy for conditional generation
- A transfer-adapter module for efficient domain adaptation
The model achieves state-of-the-art results on multiple benchmarks in different forecasting scenarios including across-domain training, zero-shot learning, and probabilistic forecasting.

### Strengths
This study introduce an innovative condition-denoising architecture along with an actual-space diffusion and denoising process, complemented by a classifier-free guidance strategy for conditional generation. This study represents the first establishment of a foundational time series model leveraging diffusion techniques. The model demonstrates exceptional cross-domain generalization capabilities, indicating its potential to redefine paradigms in time series analysis.And the Unified Time Series Diffusion (UTSD) model achieves state-of-the-art (SOTA) results across various benchmarks. 
The originality of this model, coupled with its high-quality outcomes, clarity in methodology, and significant implications for the field, underscores the importance of this findings.

### Weaknesses
- There are too few types of evaluation indicators, as a model generated by the diffuison process, more indicators such as those used in the DiffusionTS paper, such as Context-FID Score, Correlational Score, Discriminative Score, Predictive Score, etc.
- Theoretical analysis of why the model works better in actual sequence space vs latent space could be stronger
- Memory and computational complexity analysis is missing
- Limited discussion of model limitations and failure cases
- Some architectural choices (like number of blocks) need better justification
- Comparison with some recent relevant works could be expanded

### Questions
1. Can you please add evaluation indicators other than MSE and MAE?
2. As the author said in the paper “the average MSE is reduced by 17.9%, 18.6% and 22.4% compared to the existing TimeLLM, LLM4TS and GPT4TS, which indicates that the proposed method can fully utilize a small amount of data for efficient training.” Could you please explain why a decrease in MSE means that less data can be used for training? 
3. In order to train a across-domain model, a mixed dataset needs to be established. However, will the training cost increase after the dataset is enlarged?
4. How does the computational complexity compare to existing approaches?
5. What are the main limitations/failure cases of the model?
6. How sensitive is the model to hyperparameter choices?
7. Can the authors provide theoretical justification for why modeling in actual sequence space is better?
8. How does the model perform on extremely long sequences?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The model presents a Unified Time Series Diffusion (UTSD) model, which is established for the first time to model the multi-domain probability distribution, utilizing the powerful probability distribution modeling ability of Diffusion.

### Strengths
1 The condition-denoising architecture is novel.
2 The performance improvement compared to listed baselines.
3 The paper presents cross-domain generalizability.

### Weaknesses
1 The comparison did not include some interesting baselines.
2 The cross-domain transfer is limited to similar datasets. 
3 I did not see obvious advantages compared to DiffusionTS.

### Questions
1 The evaluation is very limited int he time series prediction. As listed in DiffusionTS, we should include other different metrics (like Discriminative Score and so on) to evaluate the performance. MSE/MAE evaluation is very biased evaluation metrics. For example, a straight average line achieve reasonable performances but is not meaningful.
2 The model should compare with DiffusionTS in Table 1/2, which I did not see in this paper. I would highly recommend the comparison since it is also diffusion based methods.
3 DiffusionTS can handle both conditional and unconditional generation. Is there a way for this method also be applicable to unconditional time series generation?
4 The paper claims this paper to be a foundation model for TS area. I would like to see the performance of a short forcasting model applied to long context prediction and vice versa.
5 For Table 3, the performance of ETHh1 to ETHh2 should be needed.
6 The performances of the other two datasets: Solar Forecasting and Mujoco Imputation should be included since it is widely benchmarked.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work introduces a conditional diffusion model for MTS prediction task. Different from previous non-Diffusion based methods, it employs a complicated denoised process to model the latent discrepancies in both temporal and channels (domains as described in this work). Different from the diffusion-based methods, it is flexible since it can be easily scalable for N time steps input and M time steps output scenario thanks to its well-designed interaction between conditional embeddings and denoised outputs. In general, the proposed method achieves promising results in various MTS prediction tasks such as prediction and cross-domain prediction.

### Strengths
1. The motivation of designing conditional diffusion model for flexible N time steps input and M time steps output is clear and reasonable, the model architecture is also well-designed.
2. Experimental results are soundness and promising.

### Weaknesses
1. The dimension transform is not clearly presented, which may make readers confused. For example, given N time steps input lookback, how to obtain a M time steps output prediction? Although it might be discussed in the manuscript, however, it is still not so easy to follow.
2. As claimed by the authors in line 201-206 that “existing conditional diffusion models often use simple NN layer to capture … demonstrates low accuracy”. However, according to Sec. 3, as far as I understand that the authors use CNN or Transformer based modules to transform features along the time embedding dimension of input series. For example, in denoising net of Fig. 2, the dimension of condition $\overline{h}$ is $P_L \times P_d$ while the dimension of denoised series before decoder block-a is also $P_L \times P_d$. The time dimension transformation happens at the very last block in denoising net, decoder block-a. Therefore, it should still be a simple NN layer conceptually, which is conflicted with the authors claim.
3. How do the authors obtain a so called pretrained models? It is not clear in the manuscript.
4. The authors mentioned many times in the manuscript on down stream tasks of MTS, it might be unsuitable since they only concern MTS prediction task, although including traditional prediction and cross-domain prediction, but it still belongs to MTS prediction task, not involving other down stream MTS tasks, such as anomaly detection or impainting.
5. In Fig. 4, the authors show results of some short-term periodic series. How about the results for long-term periodic series and short-term non-periodic series? These should be crucial for practical use.

### Questions
See the weakness above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a time series diffusion model for time series forecasting in multi-domain settings. The proposed model consists of the condition net, adapter, and denoising net. Different from prior autoregressive models, a diffusion denoising process is applied to capture the mixture distribution of cross-domain data and generate predictions directly. Experimental results show the effectiveness of the proposed method on probabilistic time series forecasting tasks.

### Strengths
According to the authors' claim, this is the first work to incorporate diffusion models into time series foundation models.

### Weaknesses
- The paper is generally not well-written. There are many typos and formatting issues.

- Example of typos: adaptor in the abstract

- Example of formatting issues: Text size is not consistent in the abstract, and citep is not used.

- There are false statements when criticizing prior works to motivate the proposed method. For example, while UniTime [Liu et al., 2024a] and Moirai [Woo et al., 2024] are non-autoregressive, authors claim that they "rely on an auto-regressive mechanism" in L085-088.

- Different from the statement around key contributions, the idea of denoising with condition has already been studied in many prior works, including [Fan et al.], [Shen et al., 2024], [Yuan and Qiao, 2024].

[Fan et al.] MG-TSD: Multi-Granularity Time Series Diffusion Models with Guided Learning Process. In ICLR, 2024.

- L114-116: "each iteration of the denoising stage causes an accumulation of errors in the latent space, which are further amplified during the alignment of the latent space to the actual sequence space." -> Is there any evidence on this statement?

- Not enough justification on the effectiveness of the proposed components. The ablation study in Table 5 is insufficient to explain why they should work.

- L177-179: Any supporting theory or experiments on the inherent drawbacks stated here?

- While it is natural to consider large-scale datasets for "unified" time series diffusion model, the datasets used in this paper is limited to small single-task datasets.

- Average performance should not be counted when ranking methods.

- Please distinguish citet and citep.

- Zero-shot forecasting is done in an unusual way; while the source and target datasets are similar ETT variations in this work, they usually have a significant gap in the standard zero-shot forecasting settings.

- Table 3 caption does not make sense.

- In Table 5, it is not clear what happens if condition net is missing, which implies that no input is given.

### Questions
Please address concerns above.

---
I appreciate the response from authors, they addressed some of my concerns. I raised my rating accordingly.

### Soundness
2

### Presentation
2

### Contribution
1
