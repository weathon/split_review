# ZAPBench: A Benchmark for Whole-Brain Activity Prediction in Zebrafish

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
Data-driven benchmarks have led to significant progress in key scientific modeling domains including weather and structural biology. Here, we introduce the Zebrafish Activity Prediction Benchmark (ZAPBench) to measure progress on the problem of predicting cellular-resolution neural activity throughout an entire vertebrate brain. The benchmark is based on a novel dataset containing 4d light-sheet microscopy recordings of over 70,000 neurons in a larval zebrafish brain, along with motion stabilized and voxel-level cell segmentations of these data that facilitate development of a variety of forecasting methods. Initial results from a selection of time series and volumetric video modeling approaches achieve better performance than naive baseline methods, but also show room for further improvement. The specific brain used in the activity recording is also undergoing synaptic-level anatomical mapping, which will enable future integration of detailed structural information into forecasting methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors built a benchmark dataset for whole-brain activity prediction in zebrafish. This dataset contains a 4d light-sheet microscopy recordings of over 70,000 neurons in a larval zebrafish brain and corresponding segmentations of the neurons. To illustrate how well current time-series prediction models do, they benchmarked several models on this dataset.

### Strengths
1. Building such kind of dataset for whole-brain activity prediction and understanding is quite valuable.
2. Solid study with detailed procedures described, e.g. 2000 neurons were manually labeled as training data.

### Weaknesses
1. If I understand correctly, this dataset is built based on a single zebrafish. So benchmarks acquired from this dataset and evaluations may not be well generalized to other zebrafishes.

2. Regarding time-series predictions, there are no sota methods employed in this study, e.g. temporal fusion transformer, informer, n-beats, and deepar to name a few.

### Questions
1. For the 2000 neurons manually annotated, how accurate they are? Are there any metrics to measure the segmentation accuracy?
2. The authors are encouraged to discuss how likely the results abtained from a single test zebrafish to other live zebrafishes.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on understanding the predictability of neuronal activity using zebrafish as a model organism. The study introduces the Zebrafish Activity Prediction Benchmark (ZAPBench), a structured framework designed to forecast neuronal behavior at single-cell resolution. The primary research question is centered around how accurately future neuronal activity can be predicted based on prior observations. This investigation aims to uncover fundamental predictability limits in complex neural systems, providing a formal benchmark that can guide and standardize future research in this domain.

Key contributions of the paper include:

The creation of ZAPBench, a dataset tailored for predictive neuroscience, focusing on single-cell activity in zebrafish.
A comprehensive methodology to assess prediction accuracy across various models.
Foundational insights into the neural predictability that could enhance brain function understanding and improve modeling standards in neuroscience.

The framework is intended to encourage reproducibility and provide a standard for benchmarking advancements in neuronal activity prediction methods.

### Strengths
Originality:
The paper demonstrates originality by addressing the challenge of predicting neuronal activity with a new focus on zebrafish, providing a dataset that enables prediction at single-cell resolution. By framing a well-defined benchmark (ZAPBench) and emphasizing zebrafish as a model organism, the study introduces a valuable structure for exploring neuronal predictability. This originality lies in applying prediction models to a high-resolution, single-cell level dataset, which pushes beyond the coarser frameworks commonly used in neural forecasting.

Quality:
The research is grounded in solid methodology, with a detailed approach to constructing the ZAPBench framework and rigorously evaluating prediction models. By providing an extensive dataset and clear benchmark criteria, the authors lay a high-quality foundation for reproducible research. The paper's methodology allows for systematic assessment and comparison of various forecasting methods, thereby contributing significantly to the reliability and comprehensiveness of the research.

Clarity:
The paper’s clarity is evident in its systematic presentation of the problem, methodology, and dataset. It carefully articulates the goals, including the potential limits of predictability in neuronal systems, and provides transparent descriptions of the benchmarks and data structures. Additionally, the focus on single-cell resolution is well-explained, helping readers grasp the significance of such granular predictability in the context of neuroscience.

Significance:
The significance of this work is substantial, given the pressing need for robust frameworks in neuroscience to predict and understand brain function. By creating ZAPBench, the authors lay the groundwork for a standardized method to evaluate neuronal predictability, likely stimulating future research and practical applications in brain modeling and potentially even in clinical neuroscience. The dataset and benchmark fill a critical gap in neural forecasting studies, advancing the field's understanding of predictability within complex biological systems and establishing a model that could inspire cross-disciplinary innovations.

### Weaknesses
1. Limited Scope of Evaluation Models:
While the paper establishes ZAPBench as a benchmark for predicting neuronal activity, it would benefit from a broader exploration of prediction models. Presently, if only a limited selection of forecasting models is tested, it may not fully illustrate the benchmark's potential to evaluate diverse approaches across neural network architectures, classical machine learning algorithms, or even emerging time-series models. Including additional model categories, such as recurrent neural networks (RNNs) or more advanced transformer architectures, or hybrid approaches that combine different modeling paradigms, could better demonstrate ZAPBench’s versatility and the applicability of its predictive insights across various methodologies. The current selection, while including some state-of-the-art models, may not fully capture the range of potential predictive capabilities that could be explored with this dataset.

2. Lack of Real-World Validation:
Although ZAPBench provides a controlled dataset for benchmarking, validation in diverse environments or settings would strengthen the applicability of its findings. For instance, if the framework could be tested or at least hypothetically mapped to real-time or less controlled environments, this would add value by showing the benchmark’s robustness and adaptability. Specifically, the benchmark could be evaluated on data with varying levels of noise or different experimental conditions to assess its sensitivity and generalizability. Additionally, introducing comparisons with other neural prediction benchmarks, if available, could highlight the strengths and limitations of ZAPBench in relation to existing datasets and benchmarks, increasing confidence in its practical utility. Without such comparisons, it is difficult to contextualize the performance of models on ZAPBench relative to other established benchmarks in the field.

3. Limited Analysis on Predictability Boundaries:
While the paper raises the important question of the fundamental limits of predictability, it could benefit from a deeper analysis or even a dedicated section on the boundaries of predictability within neural systems. Specifically, the authors could include additional metrics or scenarios that highlight instances where predictability fails or reaches theoretical limitations. This could involve analyzing the distribution of prediction errors across different neurons or brain regions, identifying patterns of high and low predictability, and exploring potential factors that contribute to these variations. This would provide researchers with a clearer understanding of where model improvements might be focused, enhancing the practical impact of the benchmark. For example, analyzing the temporal dynamics of prediction errors could reveal whether predictability is consistent over time or varies depending on the specific neural activity patterns.

4. Insufficient Discussion on Potential Applications:
While the framework is designed as a benchmark, an expanded discussion on its practical applications could add significant value. For instance, the authors could discuss how ZAPBench might be used in specific fields such as neuroprosthetics, disease modeling, or behavioral neuroscience. By laying out clear, actionable scenarios in which this benchmark might influence real-world applications or interdisciplinary studies, the authors could better contextualize the benchmark's significance and foster broader adoption. This could include specific examples of how improved prediction models could be used to design more effective neural interfaces, develop better diagnostic tools for neurological disorders, or enhance our understanding of the neural basis of behavior. Without these concrete examples, the practical relevance of the benchmark may not be immediately apparent to researchers in these fields.

5. Dataset Generalization and Potential Biases:
It’s unclear if the zebrafish dataset is representative of broader neuronal predictability patterns, especially for application to other species or contexts. Providing a more explicit discussion on the generalizability of the zebrafish model—or any limitations it may present—could offer readers a clearer sense of the benchmark's scope. This could also include the authors' considerations or guidelines on potential dataset biases and how they might affect downstream applications or interpretations of the benchmark's results. For example, the authors could discuss how the specific experimental conditions used to collect the data might influence the observed predictability patterns and whether these patterns are likely to generalize to other species or experimental settings. A more detailed discussion of these limitations would help researchers appropriately interpret the results obtained using ZAPBench.

### Questions
How did you select the specific prediction models tested in the benchmark?

It would be helpful to understand the rationale behind the chosen models. Are they meant to represent a range of prediction approaches, or were they selected based on prior performance in related studies? This clarification can provide insight into how comprehensive the benchmark is in capturing predictive capabilities across model types and whether the authors plan to expand the set of models in future work.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors will share a dataset of neuronal activity (both 1D traces and 4D movies), a benchmark metric to rank models by their predictive power, and a comparison of different classes of models using this metric.

This dataset and benchmark contribution can accelerate the development of predictive models of the dynamics of neuronal systems. 

Such datasets and benchmarks are timely for the field and can spur innovations in representation learning and predictive modeling (fully data-driven, fully physics-based, and hybrid models). In turn, the models can accelerate the analysis of time series data acquired in neuroscience and potentially be helpful for other time-series modeling problems, such as weather prediction.

### Strengths
* The dataset is comprehensive, and the tooling to preprocess and explore the dataset is well-developed.
* The choice of sharing both 1D traces and 4D movies is sound because it encourages the development of various models with the same dataset.
* The authors report useful naive baselines and performance with useful classes of models.
* The relative strengths of the models and areas of improvement are articulated.

### Weaknesses
 * Insufficient data to evaluate model generalization across brains: The data is from only one fish brain, which poses challenges in training models that generalize across multiple brains. The authors point out that the data took ~2 hours to acquire but much longer to preprocess. Now that they have the pipeline established, I think they should image more fish (2-8) and process them together.  Given the technological challenges, I understand that connectome can be mapped only in one or two fish. However, the live imaging data across many fish can guide which connectomes should be built.
* The MAE (mean absolute error) metric is insufficient to develop probabilistic models and models of underlying biology:  An important class of models is the ones that predict the probability of underlying biology activity, e.g., the probability of action potential from GCaMP activity or estimating functional connection between pairs of neurons from synchrony of activity.  The mean absolute error metric per neuron is unlikely useful for ranking such models. The authors should introduce a metric that enables modeling of the statistical distribution of activity per neuron or pair of neurons.

### Questions
* Why does the paper report data only from one zebrafish brain? What are the key challenges, and given the work you have done so far, can you collect data from more brains?
* Why does the paper not report estimates of action potential? I am not an expert in the properties of GCaMP. Can you clarify the limits of accuracy with which action potential be estimated from GCaMP activity?
* JAX's adoption is growing, but PyTorch is still more widely used. What can you do so that the community can reuse your code, e.g., wrap it with CLI and containerize the code?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors provide an image dataset of neuron activity in an almost entire zebrafish brain under a variety of visual stimuli. The activity dataset is acquired at a resolution of 406nm x 406nm x 4um x 914ms using calcium imaging. The image volumes are spatially aligned and segmented using machine learning to produce activity traces for 71,721 putative neurons. The authors split the data into training/validation/test sets then evaluate several time-series forecasting methods in their ability to predict neural activity. Parametric models generally show modest improvements over naive models, especially with longer context.

### Strengths
The authors provide a comprehensive, cellular-resolution calcium-imaging dataset which they process for alignment and cell segmentation which, to my knowledge, is a unique contribution to publicly available neuroscience datasets. Their data allows computational researchers to test neural activity forecasting models with little to no preprocessing, lowering barriers to this kind of research. The authors also test a diverse collection of forecasting algorithms to establish performance standards.

### Weaknesses
Introduction
- The authors could do more to describe which cellular-resolution calcium imaging datasets already exist. While the authors argue that their contribution is to the forecasting community, I think some publicly available datasets could be trivially processed for this goal as well. Specifically, Nguyen et al., 2016 (which they reference), and the MICrONS dataset arguably serve offer similar information as the authors' dataset, in other organisms.

Figures
- It is hard to see much detail in several of panels with whole-brain views. Consider enlarging panels or adding more insets to, especially, Fig 1B, Fig 2C
- It is hard to interpret Fig 2B, I encourage alternative registration visualizations e.g. showing deformed gridlines, overlaid images, and/or differences between overlaid images.
- Trace heatmaps (Fig. 3 and S2) could use colorbars, and, if possible, a graphic (aligned in time) showing the treatment conditions e.g. marking the light vs. dark conditions in the FLASH phase.

Segmentation
- It is hard to determine the accuracy of segmentation, a better visualization of the segmentation results and/or performance on a validation set would help evaluate how well the segmentations can be trusted.

EM
- The authors mention future plans of registering EM images, but in the absence of any concrete results, I don't think this should be included in the paper beyond mentioning it in the Future Work section.

### Questions
I encourage the authors to include answers to these questions in the paper, to the extent possible:
- Do any other whole-brain, cellular-resolution activity datasets exist publicly for zebrafish?
- Are there any preliminary results in the EM analysis? e.g. Can you show preliminary results of registering cell bodies across EM and calcium imaging? Can you show the reconstructed morphology of one of the neurons in the calcium data? I think some results like this are necessary to justify inclusion in this paper.
- Why do you choose MAE over MSE, which might have advantages in optimization? Zeng et al., 2023 includes both MAE and MSE.
- Doesn't the output of the stimulus model also depend on past covariates and past activity? The equation only shows future covariates as an input.
- As someone new to calcium signal analysis, an MAE of < 0.03 seems surprisingly good for the naive models - why do you think this is? I think computing the global variance of the data, or the variances of the individual neurons could help contextualize whether a 3% average error is good or not. This is related to my earlier comment about colorbars on the trace heatmaps.
- "Variability due to seeding" - does this mean initialization of the model parameters? The term "seed" is also used in FFN inference, which potentially overloads the term.
- How does the stimulus baseline work for the TAXIS dataset, where there is no training dataset available for lookup?
- The flood-filling network approach was designed for tracking neuronal processes, but the segmentation task here is cell body instance segmentation

### Soundness
3

### Presentation
2

### Contribution
4
