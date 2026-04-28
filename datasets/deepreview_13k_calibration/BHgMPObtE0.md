# MuSiCNet: A Gradual Coarse-to-Fine Framework for Irregularly Sampled Multivariate Time Series Analysis

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 5, 6, 3, 3

## Abstract
Irregularly sampled multivariate time series (ISMTS) are prevalent in reality. Most existing methods treat ISMTS as synchronized regularly sampled time series with missing values, neglecting that the irregularities are primarily attributed to variations in sampling rates. In this paper, we introduce a novel perspective that irregularity is essentially \textit{relative} in some senses. With sampling rates artificially determined from low to high, an irregularly sampled time series can be transformed into a hierarchical set of relatively regular time series from coarse to fine. We observe that additional coarse-grained relatively regular series not only mitigate the irregularly sampled challenges to some extent but also incorporate broad-view temporal information, thereby serving as a valuable asset for representation learning. Therefore, following the philosophy of learning that \textit{Seeing the big picture first, then delving into the details}, we present the \textbf{Mu}lti-\textbf{S}cale and Mult\textbf{i}-\textbf{C}orrelation Attention \textbf{Net}work (MuSiCNet) combining multiple scales to iteratively refine the ISMTS representation. Specifically, within each scale, we explore time attention and frequency correlation matrices to aggregate intra- and inter-series information, naturally enhancing the representation quality with richer and more intrinsic details. While across adjacent scales, we employ a representation rectification method containing contrastive learning and reconstruction results adjustment to further improve representation consistency. MuSiCNet is an ISMTS analysis framework that competitive with SOTA in three mainstream tasks consistently, including classification, interpolation, and forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a framework for modeling irregularly sampled multivariate time series (ISMTS). The key contributions include leveraging Lomb-Scargle Periodogram-based Dynamic Time Warping (LSP-DTW) to enhance inter-series correlation modeling and adopting a multi-scale approach to iteratively refine representations across multiple scales. The framework is evaluated across three ISMTS tasks: classification, interpolation, and forecasting.

### Strengths
1. Hierarchical modeling for irregularly sampled multivariate time series is a promising and feasible approach.

2. The use of DTW to measure similarity between variables and construct a correlation matrix is intuitively sound and well-motivated.

3. The paper is clearly written and well-structured.

### Weaknesses
1. The paper’s core contributions, particularly the hierarchical design and the DTW-based correlation matrix, are not fully demonstrated in the ablation study. Key missing analyses include:

a) Comparing multi-scale modeling with single-scale modeling to quantify the benefits. An assessment of the optimal number of scales, along with the computational cost added by each scale.

b) Evaluating the LSP-DTW correlation matrix against inter-variable self-attention, as seen in prior work (e.g., Warpformer), to confirm its advantage over attention-based correlation modeling.

2. The LSP-DTW computation introduces additional overhead, raising concerns about efficiency. The authors should provide a detailed analysis of the computational trade-offs to demonstrate if the performance gains justify the added complexity.

3. The paper mischaracterizes Warpformer as a multi-scale model for regularly sampled time series, while Warpformer actually pioneered multi-scale modeling for irregular time series using DTW. A detailed comparison with Warpformer, including both similarities and distinct contributions, is essential for clarity. Besides, it should be included as an important baseline to be compared with.


Minor suggestion: Address minor typos, such as the use of \citep{} and \cite{}.

### Questions
- Can MuSiCNet be viewed as a hierarchical extension of mTAND, with the addition of a correlation matrix to capture inter-variable similarity?

- The approach to handling irregularity in MuSiCNet closely resembles that of mTAND, aside from the use of DTW. Are there any other unique design elements aimed at better adapting to irregular data?

- What specific challenges does hierarchical modeling pose for irregularly sampled time series compared to regular time series? The method described here—using regular time intervals with average pooling (e.g., hourly aggregation)—is commonly applied to regular time series. What irregularity challenges does this approach address, and which experiments support this claim?

See also Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
1. Innovation: The paper proposes a novel MuSiCNet framework for the analysis of irregularly sampled multivariate time series, which is innovative. It views irregularity from a new perspective and effectively solves the problems of existing methods through multi-scale and multi-correlation attention mechanisms.
  2. Rationality of the method: The method is reasonably designed. For example, using LSP - DTW to calculate the frequency correlation matrix can effectively handle the correlation problem in irregularly sampled time series and avoid the spurious correlations that may be generated by existing distance measurement methods. The processing methods within and across adjacent scales have theoretical bases and their effectiveness has been verified through experiments.
  3. Adequacy of experiments: The experimental part is very sufficient. In three mainstream tasks of classification, interpolation, and forecasting, multiple real-world datasets (such as P19, P12, PAM, PhysioNet, USHCN, MIMIC - III, etc.) are used to compare with a variety of advanced methods. The results show that MuSiCNet is competitive, verifying the effectiveness and generality of the framework.
  4. Limitations and suggestions: The paper also points out some limitations, such as the interaction between scales may be further simplified and the exploration of anomaly detection tasks is insufficient. It is recommended that the authors further study these problems in future work to improve the performance and applicability of the model.
  5. Overall evaluation: This is a high-quality paper that proposes a promising method for the analysis of irregularly sampled multivariate time series and makes an important contribution to the research in this field. It is recommended to be accepted.

### Strengths
- Innovation: The proposed MuSiCNet framework is novel. It offers a new perspective on irregularity and effectively addresses existing method problems via multi-scale and multi-correlation attention mechanisms.
- Rationality of the method: The method is well-designed. LSP - DTW for calculating the frequency correlation matrix is effective in handling correlations and avoiding spurious ones. Processing methods within and across scales have theoretical support and experimental verification.
- Adequacy of experiments: The experiments are comprehensive. Multiple real-world datasets are used in three mainstream tasks, and comparisons with advanced methods show the competitiveness of MuSiCNet,     validating its effectiveness and generality.

### Weaknesses
 - In the forecasting task performance, the model isn't SOTA(state-of-the-art) in two out of three datasets. 
- Moreover, there's no comparison of model complexity, training, and inference costs with baselines, making it hard to evaluate its efficiency.
- Some motivations have not been proved by experiments directly.

### Questions
- Performance in FORECASTING task: In the TIME SERIES FORECASTING task, the model is not SOTA on 2 out of 3 datasets. Further analysis is needed. Also, model complexity, training, and inference costs compared to baselines should be provided.
- Multi-scale training details: Regarding the multi-scale learning method, it's unclear if the number of training epochs is the same as without multi-scale training. Also, the relationship between sample numbers at different scales needs clarification.
- Experimental  validation of coarse-grained series: There is a lack of sufficient experimental analysis to prove that the coarse-grained series can help the representation capture broad-view temporal information as claimed. Although an ablation study shows the effectiveness of a related loss term, it doesn't directly prove this crucial aspect, which may affect the method's theoretical and practical credibility.

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
This paper introduces MuSiCNet, a novel framework for analyzing irregularly sampled multivariate time series (ISMTS). MuSiCNet addresses the challenges posed by ISMTS data by employing a multi-scale approach and a custom-designed encoder-decoder framework called CorrNet. The multi-scale approach allows the model to learn from both coarse-grained and fine-grained representations of the data, capturing long-term dependencies and detailed temporal variations. CorrNet utilizes time attention and frequency correlation matrices to aggregate information within and across series, improving the quality of the learned representations. The paper demonstrates the effectiveness of MuSiCNet on three mainstream ISMTS tasks: classification, interpolation, and forecasting, achieving competitive performance compared to state-of-the-art methods.

### Strengths
S1: The multi-scale approach and the use of frequency correlation matrices for inter-series attention are novel contributions to ISMTS analysis.

S2: The framework is experimentally validated with strong results on multiple benchmarks, indicating reliability. The results demonstrate the effectiveness of the proposed method.

S3: The paper generally explains its methodology well, with clear explanations of the key concepts and results.

S4: This work addresses a broad need in ISMTS analysis, particularly in medical and environmental fields, where irregular data sampling is common.

### Weaknesses
W1. The paper's summary and comments on current research work are not accurate and rigorous enough. For example:

(1) "Most existing methods treat ISMTS as synchronized regularly sampled time series with missing values." However, many recent studies do not treat ISMTS as synchronized but as asynchronous, such as in the papers "Set Functions for Time Series" and "Graph-Guided Network for Irregularly Sampled Multivariate Time Series."

(2) "Neglecting that the irregularities are primarily attributed to variations in sampling rates." However, "A review of irregular time series data handling with gated recurrent neural networks" has already pointed out and explained that different sampling frequencies lead to irregular time series data.

(3) "They rely on assumptions tailored to specific downstream tasks, hindering their ability to consistently perform well across various ISMTS tasks," yet the paper does not elaborate on or provide examples of these "assumptions tailored to specific downstream tasks."

W2. The language used in the paper is not precise enough, with extensive use of "in some senses," "to some extent," which makes it difficult to accurately gauge the degree the authors intend to convey.

W3. The paper lists the model's versatility across tasks as one of its three main contributions, yet many recent models can be applied to multiple tasks. For example, the papers "Latent ODEs for Irregularly-Sampled Time Series," "ContiFormer: Continuous-Time Transformer for Irregular Time Series Modeling," and "IVP-VAE: Modeling EHR Time Series with Initial Value Problem Solvers."

W4. Figure 2 (a) appears to have poor readability. The caption mentions three main components, but their positions and relationships are not clearly displayed in the figure. X appears to be the input, but the final output is not clearly indicated.

W5. The paper states, "MuSiCNet stands out due to its lower time and space complexity compared to ViTST," yet there is no theoretical derivation or experimental results provided in the paper to support this claim.

W6. The paper uses Informer, Fedformer, DLinear, etc., as baselines for time series forecasting, but these models were originally only suitable for regular time series data? How were they adapted and applied to irregular time series data? The paper does not specify.

W7. There is a spelling error in the Conclusion section. "...designed for analyzing IISMTS datasets" where "IISMTS" should probably be "ISMTS."

### Questions
1. How to accurately understand “irregularity is essentially relative in some senses”?

2. How sensitive is MuSiCNet to the choice of hyperparameters, such as the number of scales and the masking ratio?

3. How does the computational complexity of MuSiCNet compare to other ISMTS analysis methods?

### Soundness
3

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
4

### Summary
The paper addresses the problem of representation learning for irregularly sampled multivariate time series, where different individual time-series are not synchronized in terms of their measurement times, making it challenging to apply standard time-series modeling approaches. To address this problem the authors propose a multi-scale hierarchical representation scheme built on a combination of ideas from classical time-series modeling (periodograms, dynamic time-warping) and deep learning (encoder-decoder architectures, attention mechanisms, rectification). They then evaluate their proposed methodology across three different time-series tasks (classification, interpolation, forecasting) and compare the effectiveness of their approach to a variety of baselines.

### Strengths
- The problem being addressed is important and challenging and occurs in multiple real-world applications such as medical time-series analysis

- The paper describes extensive experimental investigations of the proposed methodology, comparing it with a variety of baselines, across classification, interpolation, and forecasting tasks.

### Weaknesses
Contributions and Potential Impact:
- The approached proposed in the paper seems like a potentially useful engineering contribution, one that may work well for time-series problems with certain characteristics - but it less clear if the paper provides any significant advance in general time-series modeling methodology that would be of interest to the ICLR community and to time-series researchers more broadly.

- A general issue with the paper is that the proposed methodology combines quite a few different heuristic choices, resulting in a  complex overall model (e.g., Figure 2) that involves multiple hyperparameters and design choices. As a consequence, given the types of inductive biases that are being built into the approach (implicitly, via the design choices), it makes sense to wonder what types of problems the proposed methodology will work well, and on what types of problems it will have limitations. The paper would be much stronger if it could be extended to provide this type of insight to the reader: for example, see suggestions below about potentially expanding the discussion of limitations, and possible inclusion of simulations to provide additional insight.


Writing:
- The paper could be improved and be of more value to a reader by improving the writing. 

- As an example, there are a few key terms used throughout the paper where it would be of great help to the reader if the terms were more clearly and precisely defined. For the term "ISMTS" its unclear what the scope of this term is: can each of the individual time-series be sampled at arbitrary times, in the general case? or are there any restrictions on this level of generality? You could use Figure 1 to help explain this to the reader: from looking at a blown-up version of Figure 1 (scale L), it would appear that there are no restrictions and that each time-series can be sampled at any arbitrary set of times: is this the case?. As an example of where this is described much more clearly, see Figure 1 in the Yalavarthi et al (2024) paper where the authors clearly illustrate different sampling scenarios and make it clear which one they are focusing on in their paper. 

- Another key term that is unclear is "missing ratio" which is used to characterize the datasets in Section 4: how is this defined? does it imply that all of the time-series are potentially being measured on the same discrete time-scale (e.g., hourly or daily) but that some of the time-series don't have measurements at each discrete time (e.g., are only measured every few hours or every few days) and the "missing ratio" is the number of missing measurements relative to this fixed sampling scheme? If so, then this would seem to imply that the datasets used in experiments are a special case of the general framework (since they all have a "missing ratio" defined, Table 7) which has implications for the interpretation of the experimental results and limits the generality of the claims earlier in the paper. Another possibility is that the "missing ratio" has a different interpretation than my guess above. Whichever is the case, it needs to be clearly defined for the reader. 

- As another example related to writing, in section 3.2, the key novel contribution of the paper, the CorrNet architecture is introduced. The writing here could be significantly improved by trying to impart more insight to the reader, for example by providing a clear and intuitive toy example (for example with just 3 time-series) of what the method is doing. The current description comes across as somewhat black-box in nature. In particular, while the inclusion of different components (attention, correlation, rectification, etc) each seem sensible from a high-level viewpoint, the reader may wonder how the different parts will work together. For example, it would be helpful to be realistic here and explain when and why these methods should work well, and when we might expect them to fail. 

- Figure 2 in its current form will be very difficult for a reader to understand. At a minimum I suggest that you devote part of the text in the paper to a clear description of how data flows through the model to accompany Figure 2 (currently the text mentions Fig 2(a) in one location, and Fig 2(b) in another and I didn't see a reference to Fig 2(c) in the main text, but may have missed it). You may need to change the figure so that you can more clearly describe the steps.  (again, using Yalavarthi et al (2024) as an example, their Figure 3 is a much clearer representation of information flow and their general approach than your Figure 2). Alternatively, skip the figure and use the space to more clearly describe the mapping (input-output) that it represents, with a clear sequence of equations and/or text.


Discussion of Limitations:
- The discussion of limitations of the approach (middle of page 10) is limited in terms of detail and scope. Readers would find it very helpful here to have a more realistic evaluation of the strengths and weaknesses of the approach. For example: what is the sensitivity of the method to architecture design choices? how sensitive are the results to hyperparameter tuning? are there situations where the LSP/DTW approach will fail? And so on.

Insights from Simulations:
- simulation results could also be quite helpful in providing insights into the method. For example, you could simulate datasets from some predefined (known) continuous-time multivariate temporal process and then evaluate, both theoretically and empirically, the effect of different sampling schemes for the time series, potentially making connections to concepts such as Nyquist sampling in this context, and how such concepts might be relevant to your proposed approach.  This would be a valuable addition to the paper and complement the leaderboard-style experiments in Section 4.


Minor suggestion:
- a name other than "MusicNet" is worth considering since the name "MusicNet" will immediately suggest to a reader that this paper is about neural networks for music (rather than the actual more general topic of the paper). And there is a well-known "Musicnet" dataset already in the literature.

### Questions
- please clarify definitions of the terms ISMTS and "missing ratio" (see weaknesses above)

- what is meant in  Section 3.2 by "materializing its output ... time points \tau = [ ..]". How is k selected here? what is the sensitivity of the overall approach to the selection of k?

- at lines 245-246 how are the K reference time points defined? is this a different K to the lowercase k above?
 
- the baseline methods (e.g., for classification at bottom of page 6, and for interpolation at the bottom of page 7) seem a little old, at least on the timescale of advances in deep learning, with most references being from the 2018-2021 period. Are there any more recent baselines that are more SOA and that would be worth comparing to? For example, for the interpolation task in particular it seems like there are quite a few more recent (and more accurate) baseline methods that you could have considered (see for example the list of post-2019 methods in Table 1 of Wang et al (2024) https://arxiv.org/pdf/2402.04059)

- in your forecasting experiments, is there a reason you omitted the LinODEnet method from Scholz et al (2023): in the Yalavarthi et al (2024) paper this was the next-best method to their Grafiti method, so it seems like it would be worth including in your evaluation.

- could one come up with a baseline method based on non-neural architectures, such as some form of a multivariate Gaussian process for example? This might not work particularly well empirically and might require some ad-hoc pre-processing to implement, but some discussion of why and when such an approach would not work well, and/or a demonstration of this in your experiments, would be helpful to the reader. (The non-neural approach need not be based on a Gaussian process, this is just one possible choice of a non-parametric model).

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work focuses on the challenges arising from data irregularities and introduce an innovative framework MuSiCNet designed for analyzing ISMTS datasets.  Through comprehensive experiment discussions, the manuscript demonstrates the effectiveness of the proposed approach beyond existing works.

### Strengths
S1. The research field  is meaningful, and the research motivation of this work is clear.

S2. The  experiment discussion is comprehensive.

### Weaknesses
W1. I am confused by the insight of irregular relativity. From the way it is presented in the introduction, I find it difficult to see this as a novel insight. And I remain skeptical about whether this insight can effectively guide the resolution of existing challenges.

W2. The definition of the symbols is poorly articulated. What does "with the length of observation $ T_n$" mean?  What do $ T_n$ and $ n$represent, respectively?

W3. What are the dimensions of the variables $ Q $, $ K$, $ A $, and $ C$ in Equation 1? They are not defined before their use.

W4. The writing in the manuscript is quite rough. While I don't deny that this may be an interesting work, it definitely needs substantial revision in terms of writing style. I argue it's crucial to clarify the details and enhance the coupling between each module.

### Questions
Q1. What are the generation principles for the hierarchical set? What advantages does this generation mechanism offer?

Q2. On the P19 dataset, what are the reasons that the proposed framework does not stand out?

A typo: Line 497, "IISMTS".

### Soundness
2

### Presentation
1

### Contribution
2
