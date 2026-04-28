# Synthesizing Realistic fMRI: A Physiological Dynamics-Driven Hierarchical Diffusion Model for Efficient fMRI Acquisition

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 6, 8

## Abstract
Functional magnetic resonance imaging (fMRI) is essential for mapping brain activity but faces challenges like lengthy acquisition time and sensitivity to patient movement, limiting its clinical and machine learning applications. While generative models such as diffusion models can synthesize fMRI signals to alleviate these issues, they often underperform due to neglecting the brain's complex structural and dynamic properties.
To address these limitations, we propose the Physiological Dynamics-Driven Hierarchical Diffusion Model, a novel framework integrating two key brain physiological properties into the diffusion process: brain hierarchical regional interactions and multifractal dynamics. 
To model complex interactions among brain regions, we construct hypergraphs based on the prior knowledge of brain functional parcellation reflected by resting-state functional connectivity (rsFC). This enables the aggregation of fMRI signals across multiple scales and generates hierarchical signals. 
Additionally, by incorporating the prediction of two key dynamics properties of fMRI—the multifractal spectrum and generalized Hurst exponent—our framework effectively guides the diffusion process, ensuring the preservation of the scale-invariant characteristics inherent in real fMRI data.
Our framework employs progressive diffusion generation, with signals representing broader brain region information conditioning those that capture localized details, and unifies multiple inputs during denoising for balanced integration.
Experiments demonstrate that our model generates physiologically realistic fMRI signals, potentially reducing acquisition time and enhancing data quality, benefiting clinical diagnostics and machine learning in neuroscience.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel approach for generating realistic fMRI data using diffusion models, specifically designed to account for regional interactions and spectral features of the brain. The model captures regional connectivity in a hierarchical structure, where fine-scale signals are conditioned on larger-scale signals. To learn spectral features, it incorporates loss functions that capture fractal characteristics. Results demonstrate improved performance over existing time-series forecasting and diffusion-based models. Additionally, ablation studies validate the effectiveness of each model component.

### Strengths
1. The proposed method, which captures connectivity and spectral features, is a novel approach. 
2. The method is rigorously validated using multiple benchmarks and ablation studies.

### Weaknesses
1. The paper has limited reproducibility due to missing details about data preparation and experimental setup. Additional information is needed on the dataset used, including whether it involved resting-state or task-based fMRI, whether subjects were healthy or under specific conditions, and the rationale for selecting regions of interest (ROI), which were reduced from 268 to 82. Clarification on data split (e.g., train/test division, sample counts) is also required. If the codebase will not be provided, the paper should include a detailed description of the network architecture (such as layer specifications, kernel sizes, padding, and activation functions) and the training setup for benchmark methods in an appendix.
2. The practical implications, particularly the clinical applications of the proposed method, are somewhat unclear and could benefit from further exploration and discussion.

### Questions
1. What is the sampling frequency for the fMRI?
2. It would be beneficial to analyze the reconstructed signal to determine if the observed patterns align with expectations. Calculating the spectrum and fractal characteristics would provide an important validation of the model’s effectiveness. Additionally, some neurological features can also be checked. For instance, if the data is from resting-state fMRI, does it reveal the default mode network?  
3. Line 465 typo 69->96

### Soundness
3

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
4

### Summary
In this paper, the authors proposed a novel framework named the Physiological Dynamics-Driven Hierarchical Diffusion Model (PDH-Diffusion) for fMRI analytics. The PDH-Diffusion framework integrates two essential brain physiological properties, hierarchical regional interactions and multifractal dynamics, into the diffusion process. The primary goal is to improve diffusion models’ capability to generate realistic fMRI time series signals by accurately capturing these physiological characteristics.

### Strengths
Overall, the major strength of this work lies in its novelty. The authors have developed an innovative framework that captures complex interdependencies and multifractal dynamics within synthetic fMRI signals.

Specifically, their contribution includes integrating three key components into the diffusion process: a hypergraph-based signal generator, a dynamics properties guiding module, and a cross-brain region progressive diffusion model. This integration enhances the realism of the generated signals. The authors provide a robust theoretical foundation for their methods and perform extensive quantitative analysis, demonstrating the framework’s accuracy and effectiveness in time series forecasting. The paper is well-organized and includes relevant background information. Results from the proposed method outperform multiple peer models in time-series forecasting and diffusion models, as evidenced by superior MAE, MAPE, and RMSE scores, highlighting the model’s effectiveness.

### Weaknesses
The reviewers have multiple concerns about the framework and potential impact in this work.

1). The confusion about physiological fMRI. Usually, fMRI are categorized into resting-state and task-based fMRI. The resting-state fMRI is commonly scanned without specific stimulus, whereas task-based fMRI is acquired based on external stimulus, such as 7 tasks in HCP. Is physiological fMRI is either resting-state or task-based signal? The authors do not clarify the concept even in Introdcution section.

2). Limited motivation and impact. In Abstract, the authors mentioned "Functional magnetic resonance imaging (fMRI) is essential for mapping brain activity but faces challenges like lengthy acquisition time and sensitivity to patient movement, limiting its clinical and machine learning applications." It seems that the authros' work can advance the fMRI for clincial application, but the authors do not generate some neurological or psychiatric fMRI to validate. From reviewers' perspective, using the innovative PDH-Diffusion model, it can assist physician to provide lengthy fMRI signal which will denfinitely reduce the inconvenience of patients. Only generating healthy fMRI can impair the motivation and impact of this work.

3). Lacking of qualitative comparison. The authors have provided an extensive quantitative validation of PDH-Diffusion model with other peer methods using MAE, MAPE, and RMSE. Unfortunately, the autors do not provide any qualitative results, such as Functional Connectivity Map or Brain Connectivity Maps, of PDH-Diffusion. That is, although averaging metrics such as MAE, RMSE, MAPE across 10 runs may demonstrate robustness, these metrics  cannot fully capture the quality or realism of the synthesized fMRI signals. Notably, the qualitative results is also vital in clinics, since these results showcase which brain regions are severly impaired by neurological disorders.  Importantly, there is no visual representation given of the generated fMRI signal, which would be valuable for assessing their plausibility.

4). Several technical issues. The variance schedule (parameters $\alpha_n$ and $\beta_n$) in the diffusion process may not be fully optimized for different regions or scales, potentially leading to inappropriate noise levels in certain hierarchical levels. This could result in over-smoothing or overfitting at certain levels. Additionally, conditioning on historical data could lead to overfitting if the model becomes too dependent on past values, especially if the training data does not represent the full spectrum of brain dynamics. Without explicit mitigation measures, such as adaptive variance schedules or regularization techniques, these issues may limit the model’s ability to generalize to new or varied patterns, impacting its robustness and effectiveness.

5). Multiple typographical mistakes. In Section 4.3 (ABLATION ANALYSIS) there are many typographical errors. The term “share radio” is used instead of ‘share ratio’ in “The influence of share radio” this section. Similar typographical errors appear in the caption and text of Figure 3(b), as well as in Section 3.4. These typographical mistakes impair the redability of this paper.

### Questions
The reviewers have raised several questions regarding the weaknesses of this work:

1). Qualitative Comparisons: The authors are strongly encouraged to provide qualitative comparisons between the synthesized and real fMRI signals to allow for a qualitative assessment of the model’s performance.

2). Optimal Range of Brain Regions: The results suggest an “optimal” range of brain regions that enhances performance. How is this range determined, and is it manually set? Reviewers are concerned about the reliance on manual design for determining this optimal range.

3). Validation of Multifractal Properties: How do the authors validate that the generated signals preserve multifractal properties?

4). Risk of Overfitting: Do the variance schedule parameters ($\alpha_n$ and $\beta_n$) and the historical data used in training the PDH-Diffusion model lead to overfitting?

### Soundness
3

### Presentation
3

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
This paper proposes 'PDH-Diffusion', a framework that synthesizes fMRI data through a hypergraph-based hierarchical signals generator, the properties of a dynamic guiding module, and a cross-brain region guiding progressive diffusion model. The authors first introduced scientific priors, motivation, and concrete realization for building these modules in detail. They then provided the quantified results compared with previous approaches and the ablation experiment, showing their architecture has better performance in generating fMRI than other baseline models.

### Strengths
1. The paper established a novel framework for fMRI synthesis taking the dynamic characteristics and structure of the brain into consideration which has the solid and strong theoretical support.
2. The model incorporates hierarchical brain regional interactions and multifractal dynamics, enabling it to generate fMRI signals that better reflect physiological properties.

### Weaknesses
1. In the ''Experimental Setups'' section, the experiment did not test on multiple fMRI datasets or finer parcellation atlas, but only used the HCP dataset on the AAL atlas, which makes the results of the experiment not that solid. Meanwhile, I would suggest the framework could be extended to and tested in other modalities, for instance, EEG signals. The reliance on a single dataset (HCP) and a coarse parcellation scheme (AAL) limits the generalizability of the findings. Testing on diverse datasets, including those with different clinical populations or acquisition parameters, is crucial to validate the robustness of the proposed method. Furthermore, exploring finer parcellation atlases would allow for a more detailed analysis of brain activity and potentially reveal more nuanced patterns. The lack of testing on other modalities, such as EEG, also restricts the scope of the framework's applicability, given that EEG signals also exhibit multifractal characteristics and contain information about brain structure.
2. Although the paper introduces a novel framework for generating fMRI data, it lacks validation on the generated data’s impact on downstream tasks, such as disease diagnosis, or brain network analysis. The absence of validation on downstream tasks raises questions about the practical utility of the generated fMRI data. While the authors demonstrate the model's ability to synthesize fMRI signals, it remains unclear whether these synthetic signals can be effectively used for tasks such as disease diagnosis, cognitive prediction, or brain network analysis. Without such validation, the practical significance of the proposed method is limited.

### Questions
1. As noted in the weaknesses, synthetic neural signals are particularly intriguing in the neuroscience field. Would this framework be adaptable for application or testing on other fMRI datasets, especially those with different clinical populations, to assess its generalizability? 

2. Typically, fMRI signals are recorded in a low temporal resolution. Could the model be extended to work with high temporal resolution modalities, such as magnetoencephalography (MEG) or electroencephalography (EEG), where realistic signal synthesis could enhance downstream analyses?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this study, the authors proposed a novel algorithm for synthesizing realistic functional MRI (fMRI) via physiological dynamics-driven hierarchical diffusion model. Then, the authors validated the feasibility of synthesized fMRI data by comparing it to other generative mechanisms. The scientific merit of this work mainly comes from the conceptual advances in their proposed algorithm. It is indeed challenging to synthesize realistic fMRI data while preserving unique aspects of the brain system. The authors combined three different modules, each serving different roles, to synthesize brain dynamics with preserved network-like structure and fractal components. Given results of the extensive validation experiment on the large fMRI cohort, the validity of the proposed algorithm is clear; yet, the scientific significance of this work is somewhat limited as there was no experiment demonstrating the practical usefulness of the proposed algorithm.

### Strengths
The major originality of this study comes from its conceptual advances embedded in the proposed algorithm. It is indeed challenging to synthesize realistic fMRI data while preserving unique aspects of the brain system. The quality and clarity of the models in the main text are reasonably strong as well.

### Weaknesses
The major concern comes from the unclear significance of this work. As the authors argued in the Introduction, acquisition of fMRI is expensive. Thus, synthesizing fMRI signal can be tempting. Although expensive, real fMRI data reflects unique information of individuals. This study, however, was not able to demonstrate the synthesized fMRI still convey unique information of subjects. Slight improvement in forecasting future timepoints of fMRI signal does not suggest the significance or practical usefulness of the model. This works needs additional analysis or applications highlighting the unique advantage of the synthesized fMRI data from the proposed model. The forecasting task, as presented, is not particularly convincing. Predicting long time series, especially with pseudo-random signals like fMRI, is inherently difficult. The reported MAE error of approximately 30, even for a 32-timepoint prediction, suggests a limited ability to capture the true signal dynamics. This is further supported by the fact that baseline models achieve comparable performance, and increasing the prediction length to 64 or 96 timepoints only marginally increases the error. This raises questions about the validity of the forecasting task itself and whether the model is truly learning meaningful temporal patterns or simply fitting noise. The lack of a comparison against a naive baseline, such as a straight-line prediction, further weakens the argument that the model is capturing anything beyond simple trends.

### Questions
1. In table 1, does “T_Pred=32 or 64” mean predicting 32 or 64 time points of fMRI data?
2. If my speculation in the former question is right, it is counter-intuitive that forecasting more time points (96 vs. 32) did not lead to an increase in errors. Please clarify this. 
3. According to Fig 1, it looks like the resolution of synthesized data is bounded to the level of ROI. It is more desirable to synthesize fMRI dynamics at the level of vertex. Is the proposed method able to be applied at the vertex level as well?     
4. In line 451, please double check the definition of MAE.

### Soundness
3

### Presentation
3

### Contribution
3
