# Efficient Time Series Forecasting via Hyper-Complex Models and Frequency Aggregation

- Decision: Reject
- Avg Score: 2.50
- Scores: 5, 1, 3, 1

## Abstract
Time-series forecasting is a long-standing challenge in statistics and machine learning, with one of the key difficulties being the ability to process sequences with long-range dependencies. A recent line of work has addressed this by applying the short-time Fourier transform (STFT), which partitions sequences into multiple subsequences and applies a Fourier transform to each separately.
We propose the Frequency Information Aggregation (FIA-Net), a model that can utilize two backbone architectures: the Window-Mixing MLP (WM-MLP), which aggregates adjacent window information in the frequency domain, and the Hyper-Complex MLP (HC-MLP), which treats the set of STFT windows as hyper-complex (HC) valued vectors. and employ HC algebra to efficiently combine information from all STFT windows altogether. Furthermore, due to the nature of HC operations, the HC-MLP uses up to three times fewer parameters than the equivalent standard window aggre- gation method. We evaluate the FIA-Net on various time-series benchmarks and show that the proposed methodologies outperform existing state-of-the-art meth- ods in terms of both accuracy and efficiency. Our code is publicly available on https://anonymous.4open.science/r/research-1803/

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the FIA-Net method for time series forecasting (TSF) model. FIA-Net leverages the Short-Time Fourier Transform (STFT) and Window Mixing MLP (WM-MLP) to aggregates information from subsets of STFT windows in the frequency domain. This paper also proposes a Hypercomplex MLP as a substitution of WM-MLP, which expands the receptive field and reduces the number of parameters . FIA-Net requires significantly fewer parameters than traditional methods while achieving comparable performance. A filtering technique, which retains only the top-M frequency components of the STFT windows, helps reduce model size and complexity while maintaining accuracy. The FIA-Net outperforms existing state-of-the-art methods in terms of accuracy and efficiency on various time-series benchmarks.
The paper includes an ablation study that explores the effect of each components of FIA-Net and compares the performance of the two considered MLP backbones.

### Strengths
1. The major innovation of the proposed FIA-Net is its ability of intergerating the information of different STFT windows. The proposed WM-MLP and HC-MLP are two optional backbone structure for window integrating, both of which are innovative. Especially the HC-MLP, it uses the computation of hypercomplex numbers to efficiently combine information with less parameters.

2. The clarity of this paper is good in general. The introduction and related works thoroughly introduces the recent developments of TSF and motivation of this research. The methodology is explained in full details, with clear figures and diagrams to illustrate the proposed model's architecture and operations. The experimental results are presented in a clear and concise way.

3. The details of the experiments and extensive results are provided in appendix, with ablation study to compare the effect of proposed components. The codes are available via anonymous github, which helps reproducing the results

### Weaknesses
1. Although the major innovation of the proposed method is the windows-integrating subnetwork, the overall structure  of FIA-Net is still quite similar with the FreTS. Besides, the results of FIA-Net and FreTS are also very close, the reported gap of MSE in many comparisons are only 0.001 or even equal. Therefore, the effectiveness of windows-integrating is questionable. The core contribution of the paper, the window mixing mechanism, appears to offer only marginal improvements in performance over existing methods. The reported MSE differences are often negligible, raising concerns about the practical significance of the proposed approach. A more rigorous analysis is needed to demonstrate the added value of the window mixing strategy, especially given the structural similarities to FreTS.

2. In the last paragraph of section 4.2, it is said that "HC-MLP aggregates information from the entire set of windows altogether, allowing for a better processing of long-term memory sequences". However, in the reported results of Table 1 and text contents of section 5.1, " We can deduce that the HC-MLP is more suitable for shorter-term prediction, while the WM-MLP backbone is more suitable for longer ranges." The theoretical analysis contradicts the phenomenon of experimtents. This discrepancy between the theoretical claim and experimental results regarding the HC-MLP's ability to handle long-term dependencies is a significant weakness. The paper needs to provide a clearer explanation of why the HC-MLP, which is designed to aggregate information from all windows, performs better on shorter sequences, while WM-MLP, which processes windows separately, is more effective for longer sequences. This contradiction undermines the theoretical justification of the HC-MLP.

3. The figure 4 is not easily interpretable, mainly because the symbols of different operations are too similar. The figure is even less expressive than the corresponding equation 3. The visual representation of the HC-MLP architecture in Figure 4 is confusing due to the use of similar symbols for different operations. This lack of clarity makes it difficult to understand the flow of information and the specific computations performed within the HC-MLP. The figure should be revised to use more distinct symbols and a clearer layout to enhance its interpretability.

### Questions
In section 5.1, it is said that " It is evident that the FIA-Net consistently outperforms the baselines on most considered values of prediction horizon T, with an average improvement of 8% in MAE and RMSE over SoTA models." Where does this "8%" come from? As reported in Table 1, the improvement is insignificant comparing to FreTS, and FIA-Net does not consistently outperform FreTS.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The authors introduce a new model designed to predict observations in long-term time series, utilizing a method based on the Short-Time Fourier Transform (STFT). The main contribution lies in the development of a complex-valued MLP (Multilayer Perceptron) architecture.

### Strengths
The investigation of DNN architectures for handling signals in the frequency domain is a highly relevant area of study. This approach has the potential to reduce the preprocessing phase, which currently requires significant effort from researchers to transform signals before model adjustments. Despite the issues raised in my comments, I do believe this topic is worth exploring.

### Weaknesses
The manuscript requires revision to address several issues. The authors use terms interchangeably, such as "novel complex-valued MLP architecture," "the proposed methodologies," and "a new model for long-term..." This makes it unclear what the authors are actually proposing. In the abstract, the authors state, "To that end, a recent line of work applied the short-term Fourier Transform (STFT)." However, in my view, the use of STFT to transform time series into the frequency domain cannot be considered recent, as numerous studies have applied this approach over the past decade. The manuscript’s title includes "Efficient time series forecasting," yet efficiency was not assessed in the results presented by the authors. Additionally, the motivation for using STFT is not clearly explained. In brief, the Fourier Transform (FT) is a widely recognized technique for identifying signal frequencies, but it does not indicate the specific time at which these frequencies occur. To address this limitation, researchers proposed STFT, which divides the signal into equal-sized windows and applies FT to approximate the timing of each frequency. However, STFT has an inherent trade-off regarding window size selection. Superior results can often be achieved with methods like wavelets, which provide both time and frequency localization. The authors should clarify why they chose STFT over wavelets, considering the extensive body of literature that already uses wavelets for similar tasks, as demonstrated in several published works:

- T. Li, Z. Zhao, C. Sun, L. Cheng, X. Chen, R. Yan, and R. X. Gao,“WaveletKernelNet: An Interpretable Deep Neural Network for Industrial Intelligent Diagnosis,” IEEE Transactions on Systems, Man, and Cybernetics: Systems, nov 2019.

- Q. Li, L. Shen, S. Guo, and Z. Lai, “Wavelet Integrated CNNs for Noise-Robust Image Classification,” in 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, jun 2020, pp. 7243–7252.

- X. Cheng, X. Jia, W. Lu, Q. Li, L. Shen, A. Krull, and J. Duan, “Winet: Wavelet-based incremental learning for efficient medical image registration,” arXiv preprint arXiv:2407.13426, 2024.

- H. Wang, Y.-F. Li, and T. Men, “Wavelet integrated cnn with dynamic frequency aggregation for high-speed train wheel wear prediction,” IEEE Transactions on Intelligent Transportation Systems, 2024.

- Q. Wang, Z. Li, S. Zhang, N. Chi, and Q. Dai, “A versatile wavelet-enhanced cnn-transformer for improved fluorescence microscopy image restoration,” Neural Networks, vol. 170, pp. 227–241, 2024.

- W. Cao, W. Lu, Y. Shi, Y. Li, Y. Wang, and S. Li, “Dual-attention-based wavelet integrated cnn constrained via stochastic structural similarity for seismic data reconstruction,” IEEE Transactions on Geoscience and Remote Sensing, 2024.

### Questions
1 - The manuscript must be fully reviewed. Proofreading is strongly recommended to fix grammar errors, such as "Table 2 show", "As As shown", "the KKR are given", "We the FIA-Net", "the HC-MLP is", "the STFT is implements", "SFM utilize frequency", and so on. There are several grammar errors. 
2 - Appendices are not available in the manuscript, as cited in several parts of the text.
3 - All citations are wrong. I suppose the latex command used in the final of all paragraphs is wrong. 
4 - Captions of figures and tables should be better presented. For example, Table 1 should provide details about the evaluation metric, and Figure 5 has no punctuation. These problems are also seen in other parts. 
5 - In the introduction, the authors say "we show that the FeeqShiftNet improves", but it is not clearly discussed in the manuscript.
6 - In the abstract, the authors mention "a novel complex-valued MLP architecture. Later, they say "we propose two novel MLP architectures". Still in the introduction, the authors mention "we construct the FIA-Net and the WM-MLP backbone". Besides the grammar errors, there are several inconsistencies. 
7 - In Section 2, the authors say "Two popular architectures were proposed to improve upon RNNs". GNNs were mentioned as one of those architectures. Actually, GNN is not an architecture and wasn't proposed to improve RNN.
8 - Equations in Section 3.1 must be refined. There are errors and wrong notations. For example, X = {x_1, ..., x_t} \in R^{D x L}; is the length of the time series t or L? Who is D? Is it the TS dimension? Is it necessary to show D, once the authors are working on 1D time series?
9 - In Equation 1, are the authors using Fast Fourier Transform (N_{FFT})? This is not clear.
10 - Equation iSTFT was not numbered. In this equation, the variable X is characterized by presenting c and F, but both were not properly defined.
11 - Is the proposal designed to work on consecutive windows? How many consecutive windows? How was it assessed in terms of long-term dependencies?
12 - There is a short discussion on model complexity, but no experiment was performed to demonstrate the efficiency.
13 - On page 5, is the window determined as p?
14 - Did the authors present information about R-STFT?
15 - The authors only used MAE and RMSE to assess the results. Why? There are several other metrics that could provide further information. Why weren't they considered?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a long-term time-series forecasting approach inspired by the concept of hyper-complex numbers. It is called the frequency information aggregation network (FIA-NET). It goes one step ahead of prior arts where a novel complex-valued MLP aggregating the adjacent window information in the frequency domain is developed. The experiments confirm the advantage of proposed method.

### Strengths
1) Time series forecasting is an important problem. 
2) this paper is theoretically sound where the concept of hyper-complex number is novel.

### Weaknesses
Literature Review

The literature survey can be expanded by including recent works in 2024. There are several recent approaches in this domain recently published.

Experiments

1) the performance differences in the comparison section are very small. I wonder whether these differences can pass the statistical tests.
2) Comparison can be done with more recent baselines published in 2024.
3) Complexity analysis should be done for the proposed approach.

Conclusion

Limitation of this approach should be mentioned in the conclusion.

### Questions
!) Comparison with more recent works is required. 
2) Complexity analysis can be added.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces FIA-Net, a new model for time series forecasting. The model utilizes the Short-Time Fourier Transform (STFT) to process input sequences in the frequency domain. FIA-Net is presented with two different backbones: a Window Mixing Multilayer Perceptron (WM-MLP) and a Hyper-Complex Multilayer Perceptron (HC-MLP).

The WM-MLP is designed to aggregate information from adjacent STFT windows. It processes each window while incorporating information from its neighboring windows, allowing the model to capture local temporal dependencies. The HC-MLP treats the set of STFT windows as a hyper-complex vector. It uses hyper-complex algebra to combine information from all STFT windows simultaneously. The authors present formulations for different bases of hyper-complex numbers, including quaternions, octonions, and sedenions.

The paper presents experimental results on several benchmark datasets for time series forecasting, including weather, traffic, electricity consumption, and exchange rate data. The authors conduct ablation studies to examine the effects of various hyperparameters, such as the number of STFT windows, embedding size, and the number of selected frequency components, comparing the two proposed backbones.

The authors compare FIA-Net's performance against several existing models for time series forecasting, reporting results in terms of Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) for various prediction horizons.

### Strengths
The paper's approach of incorporating context from adjacent windows in the frequency domain is a reasonable strategy for capturing temporal dependencies in time series data. Additionally, the selection of the most relevant frequency components through their top-M frequency selection method is a reasonable technique for reducing input dimensionality while potentially preserving important spectral information. These aspects of the model design align with intuitive principles for processing time series data in the frequency domain.

### Weaknesses
The paper exhibits several severe weaknesses that considerably undermine its overall contribution.

The introduction of hyper-complex numbers appears to be an unnecessary complication, lacking both theoretical justification and demonstrated algebraic advantages specific to the task at hand. The authors fail to compare their method against simpler alternatives, such as a straightforward global MLP aggregator of the STFT windows, which could potentially achieve comparable results without the added complexity. Furthermore, while the authors emphasize that the HC-MLP backbone, unlike the WM-MLP, can process the entire sequence (all p windows) and potentially achieve higher performance, the empirical results show that the best performance often comes from the WM-MLP. This discrepancy between the theoretical advantages claimed for the HC-MLP and the actual experimental outcomes further undermines the justification for the more complex HC-MLP approach.

The literature review and comparison with existing methods are notably incomplete. While some papers, such as the one available at https://arxiv.org/html/2407.21275v1, are cited, the authors do not compare their model against these works. Furthermore, other relevant papers (https://arxiv.org/pdf/2403.11047v1 and https://www.sciencedirect.com/science/article/pii/S0167404824002669) that utilize temporal correlations between STFT windows have been overlooked, undermining the claimed novelty of the presented method.

The paper lacks a rigorous theoretical foundation to explain why their methods outperform existing ones. It relies heavily on empirical results without providing deeper insights into the underlying mechanisms at work. This absence of theoretical grounding limits the generalizability and broader impact of the work. Additionally, the experimental results lack error bars and statistical significance tests, which are crucial for validating the claimed improvements and assessing the robustness of the findings.

The authors' treatment of their finding that the real part alone might be sufficient for predictions is underdeveloped. This potentially significant insight is not explored thoroughly, missing an opportunity for deeper analysis and possible model simplification. Moreover, this observation seems to contradict the stated need for the hypercomplex formulation, further calling into question the necessity of the proposed approach.

Overall, the paper suffers from numerous grammatical errors, typos, and inconsistencies throughout both the main text and the Appendix, making it challenging to read in some sections. It is strongly recommended that the authors employ a professional proofreading service to enhance the overall quality and clarity of the manuscript, if they plan to resubmit this work somewhere else in the future.

The following is a partial list of minor comments and typos:
1.	Abstract: "state of the art" should be "state-of-the-art".
2.	Section 1, Authors refer to “FeeqShiftNet” when talking about their model. 
3.	Table 2: the two rows are “FIA-Net” and “OctontionMLP”. Most likely the FIA-Net is the “WM-MLP” backbone and the other one is the HC-MLP, but these inconsistencies confuse the reader.
4.	Throughout the paper: Inconsistent hyphenation of "long-term" and "long term".

### Questions
1. Why are hyper-complex numbers necessary for this task? 
2. What specific advantages do they provide that simpler methods cannot achieve? 
3. What specific algebraic properties of hyper-complex numbers contribute to the model's performance, if any? 
4. How does the model perform compared to a simple network that aggregates all windows without using hyper-complex numbers? 
5. Can the model architecture be simplified based on the finding that the real part alone is often sufficient?

### Soundness
2

### Presentation
1

### Contribution
1
