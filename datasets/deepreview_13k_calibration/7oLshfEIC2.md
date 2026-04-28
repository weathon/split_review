# TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 8, 3

## Abstract
Time series forecasting is widely used in extensive applications, such as traffic planning and weather forecasting. However, real-world time series usually present intricate temporal variations, making forecasting extremely challenging. Going beyond the mainstream paradigms of plain decomposition and multiperiodicity analysis, we analyze temporal variations in a novel view of multiscale-mixing, which is based on an intuitive but important observation that time series present distinct patterns in different sampling scales. The microscopic and the macroscopic information are reflected in fine and coarse scales respectively, and thereby complex variations can be inherently disentangled. Based on this observation, we propose \emph{TimeMixer} as a fully MLP-based architecture with \emph{Past-Decomposable-Mixing} (PDM) and \emph{Future-Multipredictor-Mixing} (FMM) blocks to take full advantage of disentangled multiscale series in both past extraction and future prediction phases. Concretely, PDM applies the decomposition to multiscale series and further mixes the decomposed seasonal and trend components in fine-to-coarse and coarse-to-fine directions separately, which successively aggregates the microscopic seasonal and macroscopic trend information. FMM further ensembles multiple predictors to utilize complementary forecasting capabilities in multiscale observations. Consequently, TimeMixer is able to achieve consistent state-of-the-art performances in both long-term and short-term forecasting tasks with favorable run-time efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed TimeMixer, which employs a multiscale mixing architecture to address the complex temporal variations in time series forecasting. By utilizing Past-Decomposable-Mixing and Future-Multipredictor-Mixing blocks, TimeMixer leveraged disentangled variations and complementary forecasting capabilities. Additionally, thanks to its fully MLP-based architecture, TimeMixer demonstrated efficient runtime processing.

### Strengths
S1. The paper has a clear and easily understandable structure.

S2. The experiments are extensive, involving long time series forecasting without the use of highly noisy exchange-rate and illness datasets. Additionally, a new solar-energy dataset is introduced, and the provided code and configurations enhance the credibility of the experimental results.

### Weaknesses
W1. In general, upsampling results in more data points, while downsampling results in fewer data points (as illustrated in Figure 1, leftmost). Based on this, I believe the descriptions 'Up-mixing' and 'Down-Mixing' in Figure 2 by the authors may not be appropriate and should perhaps be reversed.

W2. The paper lacks significant innovation. (1) Decoupling of multiscale [1], seasonal-trend disentanglement [2] are common modules that have already been proposed.  (2) The so-called FMM module appears to be essentially a linear layer mapping the concatenated multiscale features back to the prediction length in the time dimension. In my view, the author's main contribution seems to be the integration of these two [1,2]  modules.

W3. The improvement in experimental performance is marginal. Table 10 (the best results among all baselines) reveals that the actual enhancement by TimeMixer is not substantial, especially in three larger datasets, 'traffic,' 'weather,' and 'Electricity,' where it only holds a slight advantage at the third decimal place.

### Questions
Please see my listed weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors tackled the challenge of temporal variations in time series forecasting, recognizing that real-world time series frequently present complex temporal fluctuations, which intensify the intricacy of forecasting. In response, they introduced TimeMixer: a model grounded in a multiscale mixing architecture, integrating both Past-Decomposable-Mixing and FutureMultipredictor-Mixing components. Central to their approach is the notion of capturing variations across different time scales. This design leverages disentangled variations while harnessing complementary forecasting strengths. Empirical evaluations revealed that TimeMixer consistently achieved state-of-the-art results for both long-term and short-term forecasting, with its MLP-centric architecture offering remarkable runtime efficiency.

### Strengths
1. **Solid Motivation**: 
    - The motivation behind the paper is robust and well-justified. 
    - The significance of **TIME SERIES FORECASTING** is inherently evident and requires no further validation.
    - Echoing the authors' sentiments, the multiscale analysis paradigm stands out as a classic yet crucial methodology to model the intricate temporal variations inherent in time series data.

2. **Coherent Conceptual Framework**: 
    - The core idea of decomposing the signal into various scales and subsequently aligning trends across these scales is both intuitive and compelling.
    - This seemingly straightforward approach not only resonates with the fundamentals of time series analysis but has also demonstrated its efficacy in the authors' experiments.

3. **Rigorous Experimental Evaluation**:
    - The experiments conducted in the paper are methodologically sound, lending further credence to the proposed approach.
    - The ablation study is particularly convincing, illuminating the individual contributions of different components.
    - It's worth noting the diverse range of benchmarks utilized and the comparison with competitive models, which further underscores the robustness and generalizability of the proposed method.

4. **Clear Presentation**:
    - The paper is commendably articulated. 
    - The authors present their ideas with a blend of intuitive explanations supplemented with coherent textual descriptions, making the content both accessible and insightful for readers.

### Weaknesses
1. **Analysis and Explanation of the Results**:
    - While the empirical experiments, inclusive of the ablation study, provide evidence of the effectiveness of TimeMixer, the underlying reasons for its superior performance remain somewhat opaque. Specifically, when juxtaposed against competing models, it's not lucidly expounded how TimeMixer excels in capturing temporal variations. A deeper dive into this comparative analysis would have been enlightening. Introducing spectral analysis or similar methodologies might offer theoretical insights that bridge this understanding gap. For instance, a visualization of the learned representations in the frequency domain, compared to those of baseline models, could reveal if TimeMixer is indeed capturing a broader range of frequencies or if it is more sensitive to specific frequency bands relevant for forecasting. Without such analysis, the claim of superior temporal variation capture remains empirically supported but theoretically shallow.

2. **Alternative Decomposition Methods**:
    - The paper seems to sidestep the exploration of alternative decomposition techniques that are prevalent in the domain. For instance, methods such as the Discrete Fourier Transformer (DFT) have been widely recognized in time series analysis. How does the TimeMixer's Past Decomposable Mixing distinguish itself fundamentally from these frequency-based techniques? A comparative discourse delving into the nuances between the proposed method and established frequency-based approaches would enrich the paper's content and address potential queries from the readership. It's unclear if the moving average decomposition is truly capturing the underlying seasonal and trend components, or if it's simply a convenient approximation. Further, the choice of average pooling for downsampling is not justified. While computationally efficient, it may discard crucial information, and the authors should explore other pooling methods, such as max pooling or learned pooling, to demonstrate that average pooling is indeed the optimal choice.

### Questions
In relation to the second weakness mentioned, how does TimeMixer's Past Decomposable Mixing fundamentally differentiate itself from frequency-based methods like the Discrete Fourier Transformer (DFT)? I wonder if, while it might compute variations across domains, it might not efficiently capture temporal dynamics without specific design considerations. Furthermore, as I've highlighted, could there be alternatives to Average pooling that might perform better? How can the authors demonstrate that average pooling is indeed the optimal choice?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To better forecast complicated time series that include distinct patterns in each scale, this paper proposes TimeMixer which is a fully MLP-based architecture. This model incorporates Past-Decomposable-Mixing(PDM) and Future-Multipredictor-Mixing (FMM). As for PDM, it first decomposes time series into seasonal and trend parts. Subsequently, PDM processes seasonal and trend in a fine-to-coarse and coarse-to-fine manner. After PDM processes input time series, FDM forecasts future observations with multiple predictors. TimeMixer equipped with PDM and FMM shows the best results in various datasets for short-term and long-term forecasting. Furthermore, it proves the efficacy of the decomposition, different-way processing, and multiple predictors.

### Strengths
**1. Easy to understand**  
In simpler terms, the paper is written well. It explains its ideas clearly and in a way that anyone can understand. This makes it easier for readers to grasp the concepts and improves the paper's overall clarity.

**2. Good performance with simple models**  
Empirically, TimeMixer exhibits remarkably low computational and memory costs because it consists of only simple linear models. However, it's important not to overlook its performance, which should not be underestimated.

**3. Good observations**  
From the thought that fine-scale seasonality can provide coarse-scale one with detailed information while coarse-scale trend can provide fine-scale one with more denoised information, TimeMixer processes trend and seasonality in a different way. The experiment section proves the efficacy of this design and thought. I think that this can broadly affect how to utilize multiple scales in time series.

**4. Enough experiments**  
In the experimental section, the paper presents numerous forecasting results, including outcomes for both long-term and short-term forecasting tasks.

### Weaknesses
In spite of the good aspects of this paper, I hesitate to give acceptance because of some minor but important concerns.

**1. Absence of some important baselines**
Because this paper is based on decomposition, I think the authors have to include methods based on decompositions [1] into baselines. Furthermore, (although they are not accepted to any conference, ) it is beneficial to include methods based on MLP-Mixer [2,3]. I think that this absence makes the second and fourth strengths fade.

**2. Insufficient experiment in ablation studies**
I think the biggest contribution of this paper, or the main reason for acceptance, is different-way processing (coarse-to-fine and fine-to-coarse). Although the thought leading to this asymmetric design is not quite intuitive, Table 5 provides empirical results. However, the used datasets are insufficient. Considering its importance, more datasets should be used so this design has to be tested more rigorously. Furthermore, because small $M=1$ is employed for short-term forecasting such as M4, M4 cannot prove the efficacy of the asymmetric design sufficiently. Finally, there isn't an ablation setting where seasonal is coarse-to-fine and the trend is fine-to-coarse. These insufficient ablation studies make the third strength vanish.

If these main concerns are resolved (include more related baselines and design more strict ablation studies to prove the efficacy of asymmetric design), I will consider raising my points.

### Questions
1. Most datasets you used are multivariate datasets but I am curious about why didn't you design MLPs to capture inter-feature connections. 

2. I think the equation (6) is not aligned with Figure 4. An average of Figure (b,c,d,e) ($\hat{x}=\frac{1}{M+1} \sum_{m=0}^{M}\hat{x}_m $) can produce figure 4. However, just summing Figure (b,c,d,e) doesn't result in Figure (a). When I checked your code, not average but the sum was implemented. Can you explain this situation?

3. In table 4, I am confused about the meaning of x mark in pasting mixing and future mixing columns. What does it mean in each column in detail? In other words, how did you implement the method with x mark in each column?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
