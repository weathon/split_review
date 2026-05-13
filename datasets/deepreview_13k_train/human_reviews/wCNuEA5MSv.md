# Language Model Empowered Spatio-Temporal Forecasting via Physics-Aware Reprogramming

- Decision: Reject
- Scores: 8, 3, 5, 6

## Abstract
Spatio-temporal forecasting is pivotal in numerous real-world applications, including transportation planning, energy management, and climate monitoring. 
In this work, we aim to harness the reasoning and generalization abilities of Pre-trained Language Models (PLMs) for more effective spatio-temporal forecasting, particularly in data-scarce scenarios. 
However, recent studies uncover that PLMs, which are primarily trained on textual data, often falter when tasked with modeling the intricate correlations in numerical time series, thereby limiting their effectiveness in comprehending spatio-temporal data.
To bridge the gap, we propose \textsc{RePST}, a physics-aware PLM reprogramming framework tailored for spatio-temporal forecasting. 
Specifically, we first propose a physics-aware decomposer that adaptively disentangles spatially correlated time series into interpretable sub-components, which facilitates PLM to understand sophisticated spatio-temporal dynamics via a divide-and-conquer strategy.
Moreover, we propose a selective discrete reprogramming scheme, which introduces an expanded spatio-temporal vocabulary space to project spatio-temporal series into discrete representations. This scheme minimizes the information loss during reprogramming and enriches the representations derived by PLMs.
Extensive experiments on real-world datasets show that the proposed \textsc{RePST} outperforms twelve state-of-the-art baseline methods, particularly in data-scarce scenarios, highlighting the effectiveness and superior generalization capabilities of PLMs for spatio-temporal forecasting. % superior generalization capabilities

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper provides a novel method of using pre-trained large language models (PLMs) for spatiotemporal forecasting. The method, REPST, is a 3-step process:
1. Using the Spatio-Temporal Decomposer to extract "evolutionary signals" that summarize the system dynamics and encode these signals into patches
2. Using the Reprogrammed Language Model to transform the signal patch embeddings into the semantic space of the PLM such that the PLM can output the final latent representations
3. Using the Projection Layer to obtain the predictions
The paper evaluates REPST on 6 real-world datasets and demonstrates SOTA performance even with few-shot, zero-shot learning. 

The overall contribution of the paper is providing a framework with dynamic mode decomposition that allows the usage of PLMs for accurate spatiotemporal modelling.

### Strengths
The paper is well-written in preparing the reader with sufficient background knowledge to fully understand REPST. Specifically, the appendix includes a section on Koopman Theory to justify the assumption of treating spatiotemporal data as a linear dynamic system. Section A.5. also describes the evolutionary decomposition step in detail, clearing questions readers might have about the method. At the same time, the paper provides very recent literature such as Koopa by Liu et al., 2024.

The overall framework is also creative. By decomposing the input into its most important signals and transforming them into the semantic latent space, the power of PLMs can be harnessed for prediction. 

The ablation study also helps readers understand the effectiveness of the separate components in REPST.

The question being asked in this paper is very important since LLMs are rapidly developing and REPST bridges the progress from LLMs to spatiotemporal forecasting.

### Weaknesses
 * **Writing clarity**:
    * Some parts of the paper use vague descriptions. For instance, from Line 226-231, it could be better to be more specific in what the "reprogramming" does, and how "rich physical semantic information can boost the pretrained physical knowledge of PLMs".
    >To enrich spatio-temporal semantics and enable more comprehensive modeling of hidden spatio-temporal physical relationships, as well as unlocking the reasoning capabilities of PLMs, we further reprogram the components into the textual embedding place via an expanded spatio-temporal vocabulary. When handling textual-based components, the rich physical semantic information can boost the pretrained physical knowledge of PLMs, resulting in an adequate modeling of the hidden physical interactions between disentangled components.
    Specifically, the claim that "rich physical semantic information can boost the pretrained physical knowledge of PLMs" requires further justification, as it is not clear how the reprogramming process achieves this. The paper should provide more concrete evidence or references to support the claim that PLMs possess and utilize pre-trained physical knowledge.
    * At lines 93-94, 467-468, and 537, the paper mentions that the spatio-temporal vocabulary enables PLMs to focus on relationships among 3D geometric space, but it is not further justified or explained in the main text. It is unclear why. The paper should clarify how the vocabulary is constructed and how it facilitates the understanding of 3D relationships, especially given that the input data is a 2D spatial grid with a 1D time axis, not a true 3D geometric space. The experiment that replaces the spatiotemporal vocabulary with a dense mapping function is unclear, and the term "fused vocabulary" is not defined. An example of this fused vocabulary would be helpful.
    * In many spatiotemporal datasets, $\mathbf{X}$ is not two-dimensional but three-dimensional. For instance, in Line 830, the paper mentions that the Air Quality dataset has 6 indicators, so $\mathbf{X} \in \mathbb{R}^{35 \times 24 \times 6}$. It is unclear how REPST handles multi-dimensional input data, and the paper should clarify whether the method can be applied to such datasets or if it is limited to single-dimensional time series for each spatial location. The paper should also explain how the method can be extended to handle multi-dimensional data.
    * CHI Bike dataset not referenced and included in Table 3.
 
* **Typos**:
    * At Line 44-45, GPT-3 is not by Bai et al., 2018
    * At Line 40-41, it may be better to quote DCRNN and STGCN
    * At Line 50, the FPT acronym is not spelled out
    * At Line 156 SVD not spelled out
    * At Line 195-196 and line 204-205 A.5. >> (see section A.5.)


### Questions
* Since this Selective Reprogrammed Language Model of REPST produces the Top-K word embeddings from the pre-trained vocabulary of the PLM, what are the Top-K words that the signal patch embeddings are being mapped to? This semantic relationship would make the model more interpretable.
* In terms of the experimental setup for traffic prediction, why is the prediction horizon 24, and not {3, 6, 12} like the baseline methods? This would allow for a more rigorous comparison in prediction performance. Additionally, for Figure 4, multiple prediction horizons are tested for the other datasets, but no data is provided on METR-LA and PEMS-BAY. Similarly, for Figure 5, only 3 datasets are shown, and the additional results are not found in the Appendix.
* What is the Projection Layer? Is it a fully connected layer? How does it project $\mathbf{Z}\_{text} \rightarrow \hat{\mathbf{Y}}$
* How is REPST transferred to different datasets with different numbers of nodes? E.g. how are the learnable matrices transferrable from Solar with 137 nodes to Air Quality with 35 nodes? Why is a new dataset "CHI Bike" introduced for zero-shot?
* At Line 213 what is $L_P$?
* The authors should include anonymized code for reproducibility

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes REPST, a spatiotemporal prediction framework that enables PLM (Pre-trained Language Models) to understand complex spatiotemporal patterns through a reprogramming strategy based on physics-aware decomposition. This framework employs a physics-aware decomposer to decompose spatially correlated time series, enhancing the model's ability to comprehend the patterns. Additionally, the paper introduces a selective discrete reprogramming scheme, which projects spatiotemporal series into discrete representations.

### Strengths
1. This paper is the first to propose a physics-aware spatio-temporal decomposer.
2. The experimental datasets span the fields of traffic, solar energy, and air quality, offering good diversity.
3. REPST demonstrates strong performance under the parameters and datasets specified in the paper.

### Weaknesses
1. The statement that "the rich physical semantic information can boost the pretrained physical knowledge of PLMs" (Line 288-231) lacks experimental or theoretical evidence demonstrating that it was specifically the physical knowledge of PLMs that contributed to the results. It seems more likely that the physical methods applied simply extracted features that were more reasonable and of finer granularity.
2. The paper, i.e., abstract part, mentions that the physics-aware decomposer allows PLM to understand complex spatiotemporal dynamics using a divide-and-conquer strategy. How exactly does this relate to the divide-and-conquer approach?
3. The experimental setup is limited to a short prediction length, with no results for other prediction lengths.
4. The experimental results do not include standard deviations and there is no mention of random seeds used, making it difficult to assess the statistical significance and reproducibility of the results.
5. The complete numerical results for Figure 3 are not provided in a tabular format, which would have been helpful for detailed comparison.
6. The paper could benefit from more visualizations to better illustrate how the physics-aware decomposer enhances interpretability.
7. There are relatively few models compared when evaluating Zero-Shot performance.
8. There is a typo in the middle of Section A.5, specifically in the last line of page 17 (line 916).

### Questions
1. Does REPST perform well only for short prediction lengths?
2. Line 212: If the concatenation of two parts in $X_{dec}$ is necessary, it would be necessary to include this component in the ablation study to assess its impact. Additionally, sensitivity analysis should be conducted to evaluate the effect of the hyperparameter $\alpha$.
3. It is recommended to provide the detailed settings of the ablation experiments in the appendix, as the current text only gives a very brief overview of the approach.
4. In the ablation study, why does the performance of the Solar Energy dataset show relatively little impact when the pretrained model is not used, compared to the other two datasets?
5. Why is the dimension of E' in Figure 2 inconsistent with its description in the text?
6. Line 285: What model does "HI" represent in line 285?
7. Since the Koopman theory-based evolutionary matrix can describe the evolution of the system over time $t$, is it possible to use matrix $\mathcal{A}$ directly for prediction? If so, it is recommended to include it in the comparative experiments.

### Soundness
3

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
4

### Summary
The paper proposes REPST, a novel framework for spatio-temporal forecasting that leverages Pre-trained Language Models (PLMs), traditionally used for text, by adapting them for numerical time series analysis. Recognizing the limitations of PLMs in modeling complex spatio-temporal correlations, REPST introduces two key components: a physics-aware decomposer that breaks down spatially correlated time series into interpretable sub-components, enhancing PLM understanding through a divide-and-conquer strategy; and a selective discrete reprogramming scheme that expands the spatio-temporal vocabulary, minimizing information loss and enriching PLM representations. Experiments on real-world datasets show that REPST outperforms twelve existing methods, demonstrating strong performance, especially in data-scarce settings, and unlocking the potential of PLMs for spatio-temporal tasks.

### Strengths
* I think the authors’ approach to leveraging PLMs for spatio-temporal forecasting is innovative, especially considering the usual challenges these models face with numerical time series. By adapting PLMs for spatio-temporal data, they explore an intriguing direction that could have broader implications for forecasting tasks in various fields.

* The proposed REPST framework’s integration of the physics-aware decomposer and selective discrete reprogramming is a creative attempt to enrich PLM comprehension of complex spatio-temporal patterns. This combination appears to facilitate a more structured understanding of the input data, which is promising for zero-shot and few-shot learning.

* The forecasting results presented in Table 1 are interesting, showing that REPST outperforms state-of-the-art baselines, especially in data-scarce scenarios. This suggests that the framework could be beneficial in practical applications where limited data is a significant constraint.

### Weaknesses
 * I think the authors’ approach to leveraging PLMs for spatio-temporal forecasting is innovative, especially considering the usual challenges these models face with numerical time series. By adapting PLMs for spatio-temporal data, they explore an intriguing direction that could have broader implications for forecasting tasks in various fields.

* The proposed REPST framework’s integration of the physics-aware decomposer and selective discrete reprogramming is a creative attempt to enrich PLM comprehension of complex spatio-temporal patterns. This combination appears to facilitate a more structured understanding of the input data, which is promising for zero-shot and few-shot learning.

* The forecasting results presented in Table 1 are interesting, showing that REPST outperforms state-of-the-art baselines, especially in data-scarce scenarios. This suggests that the framework could be beneficial in practical applications where limited data is a significant constraint.

* I’m not entirely convinced by the claim of “physics-aware” decomposition. The use of the Dynamic Mode Decomposition (DMD) model seems more like pattern extraction from the input data X rather than incorporating actual physical laws. DMD is primarily designed for linear systems and is mainly focused on capturing patterns. If the authors are labeling it as “physics-aware,” I wonder why they didn’t opt for eigenvectors or simpler methods like PCA, which could also provide interpretable components. This makes me question whether the use of DMD here truly justifies the physics-informed label. Please clarify your reasoning behind using DMD over other methods like PCA or eigenvectors. Additionally, please provide more evidence or examples of how your decomposition method incorporates physical principles beyond pattern extraction.

* The terminology of “reprogramming” feels overstated to me. Typically, reprogramming would imply substantial changes to the PLM’s architecture or layers. Based on Figure 2, however, it seems that the base architecture of ChatGPT2 is not significantly modified, apart from the input transformation to align with spatio-temporal dynamics. I would appreciate a clearer explanation of what changes were made to the PLM, and whether these modifications involved retraining or fine-tuning beyond input alignment. Please provide a more detailed explanation of the changes made to the PLM architecture, if any, and clarify whether any retraining or fine-tuning was involved beyond input alignment.

* The results in Table 1 are intriguing, but I wonder if there is an inconsistency in how the baseline models were evaluated. It appears that REPST benefits from augmented data generated through the DMD process, while the baselines might have used only the original data. I believe a fair comparison would require running the baselines on the same augmented data to better understand the performance gap. Please clarify whether the baseline models were evaluated using the same augmented data as REPST, and if not, provide results of baselines run on the augmented data for a fair comparison.

* I find the claims about reasoning and generalizability improvements through PLM usage to be a bit unclear. The authors emphasize generalization, demonstrated by zero-shot performance improvements, but I don’t see a convincing demonstration of enhanced reasoning capabilities, particularly in spatial dimensions. If the improved reasoning is attributed to the DMD-based decomposition, it seems weak, as DMD primarily enhances temporal embedding rather than spatial reasoning. Please provide specific examples or analyses that demonstrate enhanced reasoning capabilities, particularly in spatial dimensions. Also, please clarify how DMD contributes to spatial reasoning, if at all.

### Questions
* Is the physics-aware component primarily derived from DMD modes? If so, how does this differ from other decomposition methods like PCA or eigenvectors, which can also capture patterns in data?

* How does DMD, which primarily captures temporal embeddings, contribute to enhancing spatial information? I’m still unclear about how DMD facilitates better spatial representation in the context of spatio-temporal dynamics.

* Could autoencoders, which also offer non-linear embeddings, serve as an alternative to the DMD for capturing dynamic information? Would such embeddings also be considered physics-aware in this context as you also have some augmentation from the data?

* How exactly does the authors’ approach to “reprogramming” the PLM differ from simply changing input structures? Were there any modifications to the PLM architecture or retraining steps involved?

* Have the baseline models been tested with the same augmented data as REPST? If not, how would the results compare under such conditions?

* How do the authors substantiate their claim of improved reasoning capabilities in the model, especially in terms of spatial reasoning? Is there specific evidence beyond improved zero-shot performance?

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
3

### Summary
This paper presents a physics-aware PLM reprogramming framework REPST tailored for spatio-temporal forecasting. The proposed REPST consists of a physics-aware spatio-temporal decomposer and a selective reprogrammed language model.  Experiment results confirm that the proposed framework unlocks the capabilities of PLMs to capture fine-grained spatio-temporal dynamics and achieves better performance than existing methods.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper introduces a unique approach to enable PLMs to handle spatio-temporal data by using a physics-aware decomposer to disentangle complex spatio-temporal dynamics into components with rich physical semantics.
3. Extensive experiments are conducted to validate the effectiveness of the proposal.

### Weaknesses
1. The proposed decomposer is not clearly described. Since the decompostion is a common tool in time series analysis, there lacks a discussion of why the decomposed components are physics-aware. 
2. The usage of the reconstruction matrix is ambiguous. Further ablation studies are needed.
3. Most Transformer-based baselines use 96 or longer input lengths. The paper only provides experimental results with an input length of 48, and the experiment under increasing the input length is missing.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
