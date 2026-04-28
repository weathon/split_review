# MIRAGE: Modelling Interpretable Multivariate Time Series Forecasts with Actionable Ground Explanations

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
Multi-variate Time Series (MTS) forecasting has made large strides (with very negligible errors) through recent advancements in neural networks, e.g., Trans- formers. However, in critical situations like predicting a death in an ICU or sudden gaming overindulgence; an accurate prediction without a contributing evidence is irrelevant. It is important to have model driven Interpretability, allowing proactive comprehension of trajectory to an extremity; and an associated Explainability, al- lowing for preventive steps; e.g., controlling BP to avoid death, or nudging players to take breaks to prevent overplay. We introduce a novel deep neural network, MI- RAGE, which overcomes the inter-dependent challenges of—(a) temporally non- smooth data trajectories for interpretability; (b) highly multi-dimensional tempo- ral space for explainability; and (c) improving forecasting accuracy—all at once. MIRAGE: (i) achieves over 85% improvement on the MSE of the forecasts on the most relevant SOM-VAE based SOTA networks; and (ii) unravels the intricate multi-variate relationships and temporal trajectories contributing to any sudden movement to criticalities on temporally chaotic datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a Multi-variate Time Series (MTS) forecasting model designed to address non-smooth data and deliver high-quality interpretable forecasts. The model, named MIRAGE, comprises multiple components, including a Deep Markov Model (DMM) for handling non-smooth data, an Attention Module (AM), a Damping Factor (DF) element, Forecasting Fine-tuning (FFT) element, and a Self Organizing Map (SOM). The DMM manages non-smooth data, while the AM, SHAP (SHapley Additive exPlanations) analysis, and the SOM contribute to model interpretability.

### Strengths
I value the paper for its specific insights into how the MIRAGE architecture can be extended, offering a clear path for further research and development. Additionally, the paper's overarching emphasis on addressing the interpretability challenge in the realm of time-series data is commendable and contributes to a better understanding of complex forecasting models.

### Weaknesses
1. The analysis for the other datasets is somewhat limited. Since the paper primarily revolves around model interpretability, a more in-depth examination of how the features in these datasets are employed in making predictions would enhance the comprehensiveness of the research. Specifically, the paper lacks a detailed analysis of feature importance and their temporal dynamics within the eICU, ETTh, and other datasets. The current analysis focuses heavily on the player dataset, while the other datasets are treated superficially, which undermines the generalizability of the interpretability claims.
2. There are labeling issues in Table 6/1.
3. Figure 2 isn’t labeled as such.
4. The text within the figures should be presented in a larger font size to improve readability, ensuring that readers can easily interpret the visual content. This is especially crucial for figures that contain detailed plots or multiple data series, where small text can obscure important information.
5. The description of the MIRAGE model is difficult to follow, which may pose a barrier to understanding its functionality. The paper would benefit from a clearer, step-by-step explanation of how the different components (DMM, AM, DF, FFT, SOM) interact and contribute to the overall forecasting process. The current description lacks sufficient detail on the mathematical formulations and algorithmic procedures, making it hard to reproduce or extend the work.

### Questions
Have you considered comparing your model with architectures based on the Temporal Fusion Transformer?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The goal of this work is to provide an interpretable model for time-series forecasting. The proposed method involves a clustering stage to determine a general Markov state structure using the first part of a trajectory, with learned transition dynamics. The second part of the trajectory is used for prediction/forecasting after being mapped to an interpretable SOM-VAE latent space (proposed in prior work). Attention weights and SHAP values are extracted on top of the proposed model to provide explainability.

### Strengths
* Interpretability + time-series modeling remain a important, open problem in the literature.
* Some interesting ideas to challenge modeling assumptions in prior work (e.g. smooth changes in latent space).
* A variety of time-series datasets are considered.

### Weaknesses
 * The proposed method reads as a large, complex collection of unmotivated components, and little insight is given as to why they are necessary. I would encourage authors to narrow down the key, novel elements of their method and to propose a more fundamental motivation and rigorous analysis of their added value.
* Empirical results consist of some illustrative examples (are these random examples or cherry-picked?) and few rigorous numerical analyses.
* Not sure I understand the premise of interpretability/explainability used in paragraph 1 of the introduction.

* Presentation: I found the paper confusing and tiresome to read.
  * Figure 1 is overcrowded and confusing. Most elements are undefined. Poor quality (delineation of underlying elements, poor alignment).  Figure 2: what is CCE loss? What is shift loss?
  * Figures in the experimental results section are generally illegible with little or no labeling. Fig 4, for example: what are alternate features? What do the medical variables correspond to, and how does this correlate to medical insight? There is no legend for what dashed/solid lines correspond to.
  * A lot of notation is undefined. e.g. what is index $w$? Difference between $Z$ and $z$?
  * Definition of abbreviations (many in abstract!)
  * Language is overcomplicated (see abstract again) with many undefined or unclear ideas: “proactive comprehension of trajectory to an extremity”, “observations are competitively mapped”, “part of its learning stride”, “collaboratively trained”, “results are assuring”, “Recollect that”, “agrressive” typo, “movement to criticalities on temporally chaotic datasets”, “Providing Ground explanations” etc.
  * Please put references in parentheses when they  do not form part of the sentence.
  * Missing hyphenation between words (“outcome oriented”, “down stream”, “scale varying”) and punctuation.

Unfortunately, with such major issues unaddressed, the manuscript is not ready for publication.

### Questions
* P1, “The psychological imprints…” how does this example illustrate lack of smoothness? I agree with the last sentence ("the factors affecting the future predictions (co-variates) are not completely observed, measurable, or generalizable") but don't see how this relates to "non-smoothness".
* what does "scale-varying/variably scaled features" mean? Isn’t this inherent to any TS data? If variable scale is an issue, why not just normalize? And how does MIRAGE specifically tackle this?
* Why use an LSTM and not a transformer as prediction architecture?
* How is $C$ determined?
* Why is the MSE of MIRAGE on eICU data (Table 2) not reported? Perhaps authors could report reconstruction error in addition to  forecasting performance.
* How do authors determine that “interpretations appear quite smooth” in Fig 7?
* Could authors provide numerical results that support the interpretability/correctness of latent trajectories, beyond the few qualitative examples proposed?
* Also would be curious to understand how HUFL can be interpreted as contributing to a drop in variable OT, whereas the least dominant feature LULL also shows a trend over a similar timescale…

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a time-series forecasting approach with Deep Markov model (DMM) architecture, an extension over an exsting model T-DPSOM. The DMM module added an extra loss function for state-transition on T-DPSOM which seems to perform well over T-DPSOM for fine-tune forecasting model.

### Strengths
Used analysis on multiple public and real-world data like game player and medical ICU data.

### Weaknesses
1. What is the exact novelty of Mirage over T-DPSOM paper? What is the motivation behind DMM architecture?
	- Table 1, Mirage underforms crossformer over MSE/MAE score for all public data. 
	- Table 2, performance only shown for T-DPSOM for ICU and Mirage analysis only shown for player data, where mirag has negligible improvement over crossformer.
	- Which dataset is used for Table 3 performance? Is it average performance on all data?

2. Table 1, authors bolded the values of Mirage in MSE, where clearly Cross-former is the lowest scores. Is this mistakes been done to create misinterpretation fir the reviewers or just type error?

3. Overall the paper is very hard to conceive, specially Sec 4 Evaluation. 
	- For someone not in medical/health data expert, the real world medical data needs a bit more explanation. What do the timeseries represent, length of the sequence, condition, etc.? Is biluribin level a time-series feature for patient?
	- I am not clear on the part how the trajectory steps are being tracked and how the heatmap being generated? Is the heatmap represent the attention weights?
	- used many abbreviations w/o terminology, e.g., acf
	- Table and Fig. captions are not self-explanatory.

4. I had to do back-n-forth multiple times to understand the entire loss function. Using proper eq. labels would have helped a lot.

### Questions
1. What is L_{DPSOM}? Could not find the equation. Without reading the T-DPSOM paper, this will be hard to understand the Mirage paper. If there is an short background of T-DPSOM model, its pros and cons, where it performs and why it fails were explained in the beginning would have been easier.

2. Evaluation analysis explanations are hard to conceive. Authors first start with Fig. 5 then suddenly jumped back to Fig. 3

3. Reviewer is not clear on how the figs (3-5) are generated.

4. Overall, the Mirage results showing underperfroming crossformer on both public and real-world data. Then what is the usefulness of Mirage architecture?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
