# FastTF: 4 Parameters are All You Need for Long-term Time Series Forecasting

- Decision: Reject
- Scores: 3, 3, 1, 5, 5

## Abstract
Time series forecasting is essential across various sectors, including finance, transportation, and industry. In this paper, we propose FastTF, a powerful yet lightweight model in Time-Frequency domain for long-term time series forecasting. Our aim is to push the boundary of model lightweighting and facilitate the deployment of lightweight model on resource-constrained devices. Leveraging the global nature and information compressibility of the time series in frequency domain, we introduce patch-wise downsampling,  Sparse Frequency Mixer (SFM), and patch predictor to capture the temporal variations of frequency components across different patches. Experimental results on five public datasets demonstrate that FastTF with very few parameters outperforms several state-of-the-art models and demonstrates a strong generalization capability. Notably, on the ETTh1 dataset, FastTF with only 4 parameters achieves a performance that is close to the DLinear and FITS in the horizon-96 forecasting. Furthermore, we deployed our model on a FPGA development board (Zynq UltraScale+ RFSoC ZCU208 Evaluation Kit), where the corresponding resource usage statistics illustrate that our model has a very low computational overhead and latency, making it easily implemented on hardware devices.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper leverages the global nature and information compression capabilities of time series data in the frequency domain, proposing a powerful yet lightweight model for long-term time series forecasting. Specifically, FastTF includes three key components: patch-wise downsampling, Sparse Frequency Mixer (SFM), and a patch predictor to capture temporal variations in frequency components across different patches.

### Strengths
1. The authors propose a lightweight model that can be deployed on resource-constrained devices.
2. FastTF combines the global perspective and the information compression capabilities of the frequency domain.
3. FastTF is demonstrated to be effective, achieving state-of-the-art (SOTA) performance in the experiments.

### Weaknesses
Dataset Dependency: The headline achievement of 4-parameter model works well on ETTh1 but requires orders of magnitude more parameters on other datasets (1928 for ETTh2, 4329 for Electricity). This variation isn't well explained and suggests important dataset dependencies not fully explored.

Missing Analysis: The paper doesn't adequately explore when the model might fail or what dataset characteristics lead to optimal performance. Including comparison with recent lightweight approaches like SparseTSF would better contextualize the contribution.

TimeMixer shows in Table 3 but not Table 2, causing some concerns.

### Questions
See Weaknesses

### Soundness
3

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
5

### Summary
This paper introduces a lightweight model, FastTF, which utilizes only 4 parameters. Leveraging the global characteristics and compressibility of information in the frequency domain of time series, this model captures key information through patch-wise downsampling, Sparse Frequency Mixer (SFM), and patch predictor. The experimental results are used to try to demonstrate the effectiveness of FastTF. The experimental results are used to try to demonstrate the effectiveness of FastTF.

### Strengths
1. The author's focus on long-term time series forecasting issues is worthy of research.

2. The model exhibits good motivation and innovation.

### Weaknesses
1. The practical value and motivation of this research are questionable. While reducing the number of parameters to an extremely low level is interesting, the manuscript does not adequately justify why such extreme parameter reduction is necessary given the increasing performance of modern hardware. The authors need to provide more compelling use cases where a model with only 4 parameters is essential, especially when considering the potential trade-offs in accuracy. The current justification is not strong enough to convince the reader of the practical need for such a small model.
2. The number of experimental datasets used by the study is too small. Although the authors claim to have used five datasets, the main experimental results presented in the manuscript focus on only four, with the fifth presented separately. Furthermore, the inclusion of only three additional datasets in the appendix is insufficient to demonstrate the generalizability of the proposed method. The limited number of datasets weakens the persuasiveness of the experimental results and raises concerns about the robustness of the model across diverse time series data.
3. In the experimental results, the method does not seem to perform as well as other SOTA models on the electricity and traffic datasets. While the authors highlight the performance of their model on other datasets, its underperformance on these two common benchmarks raises questions about its overall effectiveness and applicability. The manuscript needs to provide a more detailed analysis of why the model struggles on these datasets and what specific limitations might be causing this performance gap.

### Questions
1. Can the author include the methods mentioned in Weakness 1 and 2 in the experiments on all datasets?

2. Can the author, based on Question 1, describe more detailed baseline model parameter search results (such as e_layers, d_models, n_heads, etc.)? While model lightweighting is commendable, performance is more crucial than efficiency. I believe that by conducting more thorough experiments to demonstrate this, the quality of the paper can be enhanced.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces FastTF, a lightweight model for long-term time series forecasting that operates in the time-frequency domain. The key innovation is achieving strong predictive performance with remarkably few parameters - as few as 4 parameters in certain configurations.
The paper develops a novel architecture that combines patch-wise downsampling for weight sharing, a Sparse Frequency Mixer to capture correlations between frequency points, and a patch predictor to forecast temporal variations. The authors provide theoretical foundations for their design choices, drawing on the Nyquist sampling theorem and analysis of spectral properties.
Through extensive experiments across multiple datasets, FastTF demonstrates competitive or superior performance compared to state-of-the-art models while using orders of magnitude fewer parameters. The authors also show successful deployment on FPGA hardware with low resource usage and latency, making it particularly suitable for resource-constrained applications.
The work represents a significant step toward efficient time series forecasting, offering a solution that is both lightweight enough for edge devices and accurate enough for practical applications.

### Strengths
Originality:
The paper shows originality in that rather than pursuing better accuracy through larger models, it takes the novel approach of extreme model compression while maintaining performance. 
Quality:
The technical quality is high, with theoretical foundations and empirical validation. The authors provide thorough mathematical analysis, including proofs related to sampling theory and spectral properties. The experimental evaluation is ok, covering multiple datasets, and horizons. The ablation studies and hyperparameter analyses demonstrate robustness. Notably, the authors went beyond software simulation to validate their approach on actual FPGA hardware, providing practical evidence of deployability. The comparison with numerous baselines across different model families (Transformers, CNNs, MLPs) strengthens the findings.
Clarity:
The paper is well-structured and clearly written. Complex technical concepts are explained with appropriate mathematical rigor while maintaining readability. The authors use effective visualizations to illustrate key concepts like spectral leakage and frequency correlations. 
Significance:
The work's significance is good in both theoretical and practical terms. Theoretically, it demonstrates that extremely lightweight models can match or exceed the performance of much larger models in time series forecasting, challenging conventional wisdom about model capacity requirements. Practically, the ability to deploy effective forecasting models on resource-constrained devices opens up new applications in edge computing and IoT scenarios. The dramatic reduction in parameter count (up to 46,400x fewer than some baselines) while maintaining competitive performance represents a significant advance in efficient deep learning.

### Weaknesses
Dataset Dependency: The headline achievement of 4-parameter model works well on ETTh1 but requires orders of magnitude more parameters on other datasets (1928 for ETTh2, 4329 for Electricity). This variation isn't well explained and suggests important dataset dependencies not fully explored.

Missing Analysis: The paper doesn't adequately explore when the model might fail or what dataset characteristics lead to optimal performance. Including comparison with recent lightweight approaches like SparseTSF would better contextualize the contribution.

TimeMixer shows in Table 3 but not Table 2, causing some concerns.

### Questions
TimeMixer is missing from Table 2. Was it intentionally omitted from Table 2 or if this was an oversight? Including TimeMixer in Table 2 would provide a more comprehensive comparison across all datasets and ensure consistency with Table 3

### Soundness
2

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
3

### Summary
This manuscript proposes a lightweight long-term time series prediction model based on time-frequency domain information, which uses the compressibility of frequency domain information to significantly reduce model parameters so that it can be deployed on a wider range of platforms. While maintaining an extremely low number of parameters, the model can still achieve competitive prediction accuracy. The authors conduct a large number of experiments to prove the effectiveness of the method and deploy it on the FPGA platform to demonstrate its extremely low hardware requirements.

### Strengths
1. This study reduces the number of model parameters and computational complexity to an extremely low level while maintaining its predictive effectiveness. This is a novel and impressive study.
2. The experiments conducted by the authors are very detailed and reliable, and they provide a detailed analysis of various performance aspects including algorithm complexity and resource usage.
3. The manuscript is well-written and the relevant figures and tables are clear and easy to read.

### Weaknesses
1. The practical value and motivation of this research are questionable. The performance of various types of computing hardware is constantly increasing, and whether it is really necessary to reduce the number of parameters to 4 is a question that needs to be considered.
2. The number of experimental datasets used by the study is too small. The main experimental results presented in the manuscript are from only four datasets, which weakens the persuasiveness of the experiment.
3. In the experimental results, the method does not seem to perform as well as other SOTA models on the electricity and traffic datasets.

### Questions
1. The performance of the PatchTST provided by the author seems to be quite different from that of the original paper. Although the authors state that it is caused by a code bug, can a single error in drop_last lead to such a large performance gap?
2. Fits（arXiv:2307.03756, 2023.）also proposed a lightweight frequency domain prediction algorithm. What are the similarities and differences between FastTF and it? Can the authors give a detailed comparison to highlight the research contribution?

### Soundness
3

### Presentation
3

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
The authors introduce FastTF, a model architecture for time-series forecasting, with the goal of being light-weight while maintaining a competitive performance. FastTF uses two layers of patching in time, then an rFFT on each subpatch, truncated after a chosen cutoff frequency. The learnable parameters of the network are in a blockwise diagonal linear layer for the frequency space subpatches, mixing information within each patch, and another linear layer that mixes information between patches, with the weights being shared across one of the patching dimensions. Afterwards, the frequency data is padded, the FFT inverted and the time data reshaped to obtain the model output. Through this use of sparsity and weight sharing the total number of parameters of this model architecture is significantly lower than in other approaches for time-series forecasting. The authors show competitive performance of FastTF for prediction tasks on several standard time-series datasets and prediction horizons and present a study on the impact of different hyperparameter choices in FastTF as well as a small studies on generalizability, converge speed, and deployability on an FPGA.

### Strengths
- Overall the authors fulfilled their aim: FastTF seems to be very light-weight with competitive performance
- Fairly extensive hyperparameter study
- Architectural choices are motivated by and take advantage of empirical observations of weight matrix structures, i.e. weight matrix sparseness as the motivation for the SFM 
- The authors also present prediction results that do not perform well, e.g. figures 15 and 16 in the appendix.

### Weaknesses
- (major) The case study in Section 5.4 shows that ETTh1 can be predicted with high accuracy from local means; this can be done within FastTF, but is not a good example of its strengths since neither the full expressivity of the Fourier representation nor the SFM is used; the Fourier transforms just add unnecessary overhead here; in summary, this is a finding about the dataset, not the FastTF architecture and thus should not be in the main text.
- (major) The patch size $P$ is always an integral multiple of the fundamental frequency, e.g. 24h for ETTh. For Transformer architectures it has been shown that patching the data like this can improve the performance significantly (see also below the remark about related work), so it cannot be excluded that this (and not the specific structure of the architecture) is the reason for the good performance of FastTF. The effects of stacking the data according to its base frequency and the new architecture need to be disentangled (see also (Q2))
- (major) The authors did not provide statistics of their achieved results, e.g. variation of the metrics across multiple runs with different seeds, making it possible to have cherry-picked results (not necessarily the case in reality)
- (minor) The related work could be extended to include additional works such as:
    - Wen, Q., He, K., Sun, L., Zhang, Y., Ke, M., \& Xu, H. (2021, June). RobustPeriod: Robust time-frequency mining for multiple periodicity detection. In Proceedings of the 2021 international conference on management of data (pp. 2328-2337).
    - Wen, Q., Zhou, T., Zhang, C., Chen, W., Ma, Z., Yan, J., \& Sun, L. (2023, August). Transformers in time series: a survey. In Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence (pp. 6778-6786).
    - A. Weyrauch et al., "ReCycle: Fast and Efficient Long Time Series Forecasting with Residual Cyclic Transformers," 2024 IEEE Conference on Artificial Intelligence (CAI), Singapore, Singapore, 2024, pp. 1187-1194, doi: 10.1109/CAI59869.2024.00212.
- (minor) quote at the beginning of the text seems to be out of place for a brief proceedings article
- (minor) division into patches and downsampling as used in the submission are identical, use only one to avoid confusion (preferably patching since downsampling implies loss of information)
- (minor) the description of the Exchange dataset in Appendix A.5 seems to be mixed up with that of a different dataset
- (minor) the number of parameters given in section 5.3 is correct for the number of complex degrees of freedom; for comparison with models that do not work with complex numbers this is slightly misleading; give additionally the number of real parameters (even if that is just a factor of two)
- (minor) the magnitude of the error implies that all the metrics given are still normalized; either give denormalized metrics or acknowledge that it is still normalized
- (minor) Transformer part of the Related Work section: "Informer and Autoformer capture the temporal dependence of time-series" is non-informative. We would encourage the authors to additionally state how these are captured. Furthermore, "..., while FEDformer models the frequency domain of the time-series.". this implies that Autoformer and Informer do not work in Fourier space, which does not hold for the Autoformer, albeit the motivation is different compared to FEDformer 
- (minor) The authors should closely check the manuscript for grammar and phrasing. Some of the minor issues that the reviewer found are:
    - "Natual Correlation" should likely be "Natural correlation" (l. 230)
    - Inconsistencies with the use of capitalization/title case, e.g. "**N**atural **C**orrelation'' vs. "**T**he **e**ffect of **d**ownsampling"
- (minor) The reviewer would like to request from the authors to increase adherence with the paper template, which includes, but is not limited to:
    - Tables need to be centered
    - Figure colors should be legible even on black/white printouts, currently some pastel colors are difficult to read even in the PDF
    - Please use large enough font sizes for all visual elements
    - Refrain from using color to highlight elements in tables, especially the lime green.
- (minor) The reviewer does not agree with the use of "Theorem" as used in this manuscript
       - Theorem 1 is not a new insight by the authors and therefore does not need to be proven again. Theorem would imply that it is novel.
        - Theorem 2 is more of an observation or counting not a mathematical insight

### Questions
- What is the energy consumption during training? If convergence of FastTF is faster and the number of parameters is smaller, does this convert into energy savings?
- How does FastTF perform if the patch size $P$ is not a multple or integer divisor of the fundamental frequency, e.g. 24h for ETTh? This could be a stress test for the ability of the SFM mechanism to deal with spectral leakage as claimed.
- The reviewer has observed that FastTF is mostly just learning a singular template pattern that is, if at all, simply shifted by the local mean. While this performs well (see your metrics), it is quite questionable to refer to true learning by the model. What would happen if the model was faced with strong out-of-distribution data, e.g. with strong noise or shifts?

### Soundness
3

### Presentation
2

### Contribution
2
