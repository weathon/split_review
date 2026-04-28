# Hi-Patch: Hierarchical Patch GNN for Irregular Multivariate Time Series Modeling

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Multi-scale information is crucial for multivariate time series modeling. However, most existing time series multi-scale analysis methods treat all variables in the same manner, which is not well adaptive to Irregular Multivariate Time Series (IMTS), where different variables have distinct original scales/sampling rates. Therefore, extracting temporal and inter-variable dependencies at multiple scales
in IMTS remains challenging. To fill this gap, we propose a hierarchical patch graph network Hi-Patch. The key components of Hi-Patch are an intra-patch graph layer and several inter-patch graph layers. The intra-patch graph layer flexibly represents and fully captures both the local temporal and inter-variable dependencies of densely sampled variables at the original scale by employing fully connected graph networks within each patch, and obtains patch-level node representations through aggregation. Subsequently, several inter-patch graph layers are stacked to form a hierarchical architecture, where each layer updates specific patch-level nodes through scale-specific graph networks, progressively representing and extracting more global temporal and inter-variable features of both sparsely and densely sampled variables, and further aggregating to produce the next patch-level node representations. The output of the last inter-patch graph
layer is fed into task-specific decoders to adapt to different downstream tasks. Experimental results on 8 datasets show that Hi-Patch outperforms a range of state-of-the-art models in both IMTS forecasting and classification tasks. Code is available at this repository: https://anonymous.4open.science/r/Hi-Patch-F42E.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel hierarchical patch graph network (Hi-Patch) designed to address the challenges of modeling irregular multivariate time series (IMTS) data. The proposed method leverages both intra-patch and inter-patch graph layers to capture local and global temporal and inter-variable dependencies at multiple scales. The hierarchical architecture allows for a bottom-up extraction of features, from fine-grained to coarse-grained, adapting to the distinct scales and sampling rates of different variables in IMTS. The authors demonstrate the effectiveness of Hi-Patch through extensive experiments on eight datasets, showing superior performance over various state-of-the-art models in both forecasting and classification tasks for IMTS.

### Strengths
1.Hi-Patch offers a unique hierarchical architecture that effectively handles the irregularity and multi-scale nature of IMTS data, which is an interesting thoughts  in the field.

2.The method's ability to extract features at multiple scales is a strength, as it allows for a more comprehensive understanding of the data, capturing both local and global patterns.

3.The paper provides a thorough experimental evaluation on eight different datasets, which strengthens the credibility of the proposed method. Hi-Patch outperforms a range of existing state-of-the-art models, which is a testament to its effectiveness

### Weaknesses
1.While the concept of integrating local and global information is not new, the paper could better articulate the innovative aspects of Hi-Patch that distinguish it from existing methods, especially those that also employ patching techniques or graph neural networks.

2.While the paper does offer a comparison between MTS forecasting methods and multi-scale forecasting methods, there seems to be a concern regarding the equitable selection of parameters for the methods in question. The potential imbalance in parameter tuning could skew the comparative analysis, undermining the validity of the study's conclusions.

3.The hierarchical nature of Hi-Patch might introduce increased complexity in terms of model training and inference time, which could be a drawback for applications with real-time requirements.

4.The paper could benefit from a deeper analysis of the interpretability of the model, which is an important aspect of time series modeling, especially in fields like healthcare and climate science.

### Questions
1.How does the computational complexity of Hi-Patch scale with the size and number of variables in the IMTS data?

2.In 5.5 ‘EFFECT OF PATCH SIZE’, will patch size 3 in Fig 5 (a) and (b) be a better choice?

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
5

### Summary
This paper addresses Irregular Multivariate Time Series (IMTS) forecasting, presenting it as an application-driven extension of multi-scale time series analysis methods. The approach leverages patch aggregation in a manner that is both simple and elegant. While the intra-patch and inter-patch layers are distinct in structure, a unified Multi-Head Attention (MHA) mechanism is effectively employed to aggregate information across both layers. The writing is clear and well-executed; however, the limited availability of IMTS data may make the experimental results appear somewhat insufficient.

### Strengths
**Significance:** This paper presents an application-oriented extension of multi-scale time series analysis methods. Unlike traditional prediction models that rely on fixed sampling frequencies, this model can effectively model, analyze, and forecast irregular, non-stationary multivariate data across three dependency dimensions: 1) same variable across different times (SVDT), 2) different variables at the same time (DVST), and 3) different variables across different times (DVDT).

**Originality:** The approach utilizes patch aggregation in a way that is both straightforward and elegant. A unified Multi-Head Attention (MHA) mechanism is skillfully employed to aggregate information across the two kind of graph layers, namely intra- and inter- patch.

**Quality:** The writing is clear, concise, and well-structured.

**Clarity:** The presentation is clear and accessible.

### Weaknesses
1. If the model is applied to real-world IMTS prediction tasks, the input should include not only historical data but also a query. It is necessary to explain how the **Query** should be designed in practical applications.

2. The experiment in Appendix F.1 is nearly an invalid comparison and does not yield any substantial conclusions. Such results fail to reflect the model's ability to learn more temporal dependencies from longer-term data. It would be better to illustrate this using a line chart. The experiment should be modified by fixing either the input or prediction length and then varying the other. For example, on the PhysioNet dataset, use input lengths of {12, 24, 48, 96, 192} hours to predict 24 hours ahead.

3. The experimental datasets are actually too limited, which necessitated adding a classification task. While it's understandable that IMTS datasets are scarce, I hope you can test the model on traditional datasets with fixed sampling frequency, such as ECL, ETT, and PEMS. Including these in the appendix would enhance the model's generality. Cause based on the structure of **Hi-Patch**, it should be able to directly handle time series datasets with fixed sampling frequencies.

### Questions
1. The paper does not clearly explain how the model handles situations where, given a fixed patch length 10 seconds, there are no observations within an initial patch. For instance, if in Figure 2, variables V1 and V2 have no data between 10–20th time steps, how would this affect the model's generation of the intra-patch graph?

2. If the model is applied to real-world IMTS prediction tasks, the input should include not only historical data but also a query. It is necessary to explain how the **Query** should be designed in practical applications.

3. In Equation 4, what is the meaning of **d**?

4. The experiment in Appendix F.1 is nearly an invalid comparison and does not yield any substantial conclusions. Such results fail to reflect the model's ability to learn more temporal dependencies from longer-term data. It would be better to illustrate this using a line chart. The experiment should be modified by fixing either the input or prediction length and then varying the other. For example, on the PhysioNet dataset, use input lengths of {12, 24, 48, 96, 192} hours to predict 24 hours ahead.

5. The experimental datasets are actually too limited, which necessitated adding a classification task. While it's understandable that IMTS datasets are scarce, I hope you can test the model on traditional datasets with fixed sampling frequency, such as ECL, ETT, and PEMS. Including these in the appendix would enhance the model's generality. Cause based on the structure of **Hi-Patch**, it should be able to directly handle time series datasets with fixed sampling frequencies.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates multi-scale temporal and spatial correlations in irregular multivariate time series and proposes a hierarchical patch graph network, effectively addressing the challenges of uneven sampling intervals within each variable and asynchronous observations among different variables. Experimental results demonstrate that the proposed method achieves state-of-the-art performance across eight datasets.

### Strengths
1. This paper effectively integrates a patch strategy with a graph network in a hierarchical architecture, successfully addressing the challenges posed by irregularly sampled time series.

2. The designed hierarchical architecture effectively models multi-scale features from fine-grained to coarse-grained.

3. Experimental results validate the superior performance of the proposed model across eight datasets.

### Weaknesses
1. The proposed model overlooks missing values, which may result in significant information loss. Additionally, the entanglement of spatial and temporal correlation modeling may increase the training complexity of the model.

2. The presentation of core functional modules is mainly based on text description accompanied by snippets of equations that only show the intermediate transformation steps whereas the whole picture is lost. The authors are supposed to provide a precise mathematical description of the entire data transformation process, i.e., how the inputs are transformed into the output step by step. 

3. A complexity analysis of the proposed model, as well as comparisons with other baselines, should be included.

### Questions
1. The framework of the Hi-Patch, as illustrated in Figure 2, is not easily understood.

2. The references should follow a uniform style.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents Hi-Patch, a hierarchical patch graph network designed to model irregular multivariate time series. The model uses intra-patch and inter-patch graph layers to address local and global temporal dependencies at multiple scales, offering enhanced adaptability to the distinct sampling rates and scales across variables. The core contributions include the hierarchical multi-scale design that captures both fine-grained and coarse-grained features of IMTS, enabling comprehensive representation and task adaptability. Hi-Patch was evaluated on several datasets and demonstrated good performance in both forecasting and classification tasks compared to other well-known methods.

### Strengths
+ The hierarchical patching is reasonably adapted to IMTS, an approach that builds on traditional graph-based temporal models by adding intra- and inter-patch components. This layered approach appears to effectively handle asynchronous data dependencies within a multi-scale framework.
+ Hi-Patch is trying to address an important challenge in time series analysis: handling irregularity across multivariate data. The hierarchical, multi-scale approach has the potential to be impactful.
+ The methodology is well-structured and has been systematically evaluated. The overall performance appears good, although I have not examined the results in detail. The ablation study offers good insights into how different components affect the model's performance.

### Weaknesses
+ The overall technical contributions are limited. The multi-scale approach is well-established in other domains, and the intra-patch/inter-patch distinction is primarily a reconfiguration of existing graph network concepts.
+ The major concern is the presentation of this work. (1) Abstract and introduction could benefit from clearer articulation of the connections between multi-scale and multivariate modeling. (2) The abstract’s explanation of intra-patch and inter-patch layers is also somewhat confusing. (3) Additionally, Figures 1 and 2 are not effective in supporting the discussion; Figure 1 lacks readability, and Figure 2 fails to clearly illustrate the intra-patch and inter-patch processes. It is detailed but unclear, especially concerning the absence of intra-patch aggregation on the right side of the illustration.

### Questions
I have no specific questions.

### Soundness
3

### Presentation
2

### Contribution
2
