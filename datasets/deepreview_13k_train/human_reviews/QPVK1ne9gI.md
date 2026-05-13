# MPFBench: A Large Scale Dataset for SciML of Multi-Phase-Flows: Droplet and Bubble Dynamics

- Decision: Reject
- Scores: 6, 3, 8, 3

## Abstract
Multiphase fluid dynamics, such as falling droplets and rising bubbles, are critical to many industrial applications. However, simulating these phenomena efficiently is challenging due to the complexity of instabilities, wave patterns, and bubble breakup. This paper investigates the potential of scientific machine learning (SciML) to model these dynamics using neural operators and foundation models. We apply sequence-to-sequence techniques on a comprehensive dataset generated from 11,000 simulations, comprising 1 million time snapshots, produced with a well-validated Lattice Boltzmann method (LBM) framework. The results demonstrate the ability of machine learning models to capture transient dynamics and intricate fluid interactions, paving the way for more accurate and computationally efficient SciML-based solvers for multiphase applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper contributes a new large-scale dataset for droplet and bubble formation, which is important within the engineering and chemical process industry. The main contributions is a dataset larger than before and one which has been evaluated on state of the art SciML methods e.g FNO, UNet etc.

### Strengths
The main strength is the creation of a larger than previously available dataset and one which has been tested on numerous different state of the art ML methods. This is a very useful contribution to the AI4Science field that is strongly lacking in openly available datasets.

### Weaknesses
Whilst the paper (and the associated website) are well written, there are some aspects that are missing, particuarly in the paper. There is no discussion on the license of the dataset (a very important topic) within the paper itself. Looking at the sample data I found CC-BY-NC - which means no commerical usage. I would like to see a discussion on this in the main paper. Additionally there is limited discussion on how to actually use the data. On the website (hugging face) there are some steps on how to unzip and then a script to read in the data, but this should be in the appendix of the paper too.

### Questions
1) What is the license of the dataset (please justify your choice)
2) How do you plan to host the data (is it hugging face?)
3) What are you plans to ensure it's maintances over years and potentially decades.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
MPF-Bench provides a large dataset of two multiphase fluid flow simulation types, namely rising bubble and falling droplet dynamics. The paper includes the performance of six popular neural network baselines, covering both sequence-to-field and sequence-to-sequence predictions.

### Strengths
1) Dataset accuracy is ensured by providing validation studies for the LBM solver used to generate the datasets.
2) The work is overall well presented and the limitations are discussed.

### Weaknesses
On a high level, I see how multi-phase flow simulations can be useful in industry, but I'm not convinced that the proposed dataset is practically useful. Typically, industrial applications involve at least one of (a) interactions between bubbles, (b) thermal exchange with the environment, (c) interactions with walls, or (d) complex geometries. I would suggest adding such more practically relevant cases, i.e., if a task of interest is cavitation at turbine blades, one could simulate bubbles next to a metal surface. The currently proposed dataset is relatively simple in its setup, and I would describe it as a scaled-up version of BubbleML.

Ideas for improvement of the manuscript:
1) Consider rewriting line 85 as there has been a predecessor for multiphase benchmarking using neural operators, i.e., BubbleML. For example, you could rewrite the sentence to "To our knowledge, only one study (Hassan et al., 2023) has evaluated the performance of neural operators on multiphase flows, and we are the first to evaluate a foundation model that has been pre-trained on single-phase data."
1) In line 137, mention how many datasets are for 2D and 3D separately.
1) In Section 3.3, line 261, the input field part could be rewritten. Does the input to the models include only the scalars?
1) In lines 269-270: Provide clarification regarding the timestep used to save the dataset. Is the timestep interval used to generate the dataset the same as the timestep of the LBM solver? Clarification on choosing this timestep coarsening factor would be insightful.
1) Provide the mathematical formula for the metrics (MSE and relative L2 error) in the appendix. Also, mention a reason for choosing these metrics and potentially discuss alternative, more physical metrics. By physical metrics, I mean something aligned with the downstream application, e.g., the error of the volume fraction of the bubble/droplet, the error in the velocity of the center of mass of the bubble/droplet, or any other relevant derived metric.
1) As a benchmarking paper, please consider providing standard deviations (over multiple seeds) of the metrics in Tables 5 and 6.
1) Providing details on the number of model parameters and hyper-parameters for each model used for benchmarking would be insightful.

### Questions
1) In line 268, by interface indicator, do the authors refer to the signed-distance function?
1) Looking at the figures in the manuscript, most flow fields seem symmetric with respect to the centered vertical axis, meaning that one could store only one half of the field in 2D and one quarter in 3D to describe the full flow field. Did you consider doing this to reduce the dataset size?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Good paper on a useful physics dataset. Multiphase flows represent a frontier domain in flow physics. Time-series datasets are also useful across different ML domain including video modeling, etc.

I only have questions that would help clarify some context and experimental choices for better presentation.

Edit 1: Concerns have been addressed. Raising score to 8 to recommend for strong acceptance.

### Strengths
1. Time-dependent multiphase data -- rich dataset.
2. Extensive model evaluation
3. Good lit review of previous work
4. Lattice boltzmann solvers are high fidelity
5. 4000 GPU hours is substantial
6. Good Qualititative demonstration of ML predictions
7. Solid Appendix
8. Good reproducibility efforts.

### Weaknesses
1. Applications of this dataset are not obvious -- could be emphasized more in introduction or via eval demonstrations
2. Description of physics methods requires a bit more clarity for non-physics readers in this general ML venue.
3. Connection to anonymous repo had 522 timeout when I clicked -- I assume that this will be fixed after double blind review.

### Questions
1. In appendix A, can you briefly describe the Allen Cahn equations a bit more for the readers? Specifically on big picture descriptions on how close is this to direct numerical simulation of Navier Stokes?
2. In appendix A, what's the benefit of Lattice Boltzman methods vs conventional interface-capturing Finite Volume Solvers? Are there any cost-accuracy tradeoffs with your simulation approach? This could be useful for readers to know as well.
3. Since Section 4, line 365. How were hyper parameters chosen?
4. Section 4 and 5 -- How many train/val/test splits?
5. Can you spend a paragraph or 2 explaining the broader applications of this dataset and importance of sequence to field and sequence predictions benchmarks in the intro?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
MPF-Bench provides a dataset that contains 11,000 2D and 3D simulations of challenging multiphase fluid dynamics, and is produced with a well-validated Lattice Boltzmann method framework. Six neural operators and foundation models are trained and evaluated on six different datasets, including both sequence-to-field and sequence-to-sequence tasks. The authors finally get encouraging results which show that machine learning approaches are able to learn multiphase fluid dynamics.

### Strengths
1. MPF-Bench provides a large number of snapshots.
2. The simulation framework is well-validated.
3. Six models are evaluated,

### Weaknesses
1. 'Our models are trained on a random selection of 1000 samples from the bubble dataset.': Does this mean that all models are trained with the **2D** bubble dataset? Are these 1000 samples fixed for different models? It's unclear if the models are being trained on the same data, which is crucial for a fair comparison. The lack of clarity on this point makes it difficult to assess the validity of the results.
2. It would be meaningful to explore the results of models on different types of datasets and compare them (e.g., bubble and droplet, different difficulty due to different parameters), which will help us figure out which model is better at handling which case. This is important for understanding the generalizability of the models. The current evaluation is limited to a single dataset, which does not provide a comprehensive view of model performance.
3. The evaluation of models on the 3D datasets will be closer to the real world and more interesting. The absence of 3D results limits the practical relevance of the study. The 3D simulations are more complex and would provide a more rigorous test of the models' capabilities.
4. More visualizations of different models will be more convincing and help better compare their performance. The current lack of visualizations makes it difficult to interpret the results and compare the performance of different models. Visualizations are essential for understanding the qualitative behavior of the models.
5. l156: It is better to explain what each symbol in the equations refers to. The lack of explanation makes it difficult for readers to understand the underlying physics.
6. l168: Do not need ".
7. l307: [resolution_z] is incorporated...
8. l310: families.

### Questions
1. How do you train the foundation models (scOT and Poseidon)? Are they retrained or fine-tuned based on pre-trained checkpoints?

### Soundness
2

### Presentation
3

### Contribution
2
