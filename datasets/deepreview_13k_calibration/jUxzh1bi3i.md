# GlobalTomo: A global dataset for physics-ML seismic wavefield modeling and FWI

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Global seismic tomography, taking advantage of seismic waves from natural earthquakes, provides essential insights into the earth's internal dynamics. Advanced \ac{fwi} techniques, whose aim is to meticulously interpret every detail in seismograms, confront formidable computational demands in forward modeling and adjoint simulations on a global scale. Recent advancements in \ac{ml} offer a transformative potential for accelerating the computational efficiency of \ac{fwi} and extending its applicability to larger scales. This work presents the first 3D global synthetic dataset tailored for seismic wavefield modeling and full-waveform tomography, referred to as the \ac{dataset} dataset. This dataset is uniquely comprehensive, incorporating explicit wave physics and robust geophysical parameterization at realistic global scales, generated through state-of-the-art forward simulations optimized for 3D global wavefield calculations. Through extensive analysis and the establishment of \ac{ml} baselines, we illustrate that \ac{ml} approaches are particularly suitable for global \ac{fwi}, overcoming its limitations with rapid forward modeling and flexible inversion strategies. This work represents a cross-disciplinary effort to enhance our understanding of the earth's interior through physics-\ac{ml} modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper, "GlobalTomo: A Global Dataset for Physics-ML Seismic Wavefield Modeling and FWI," introduces a 3D global synthetic dataset designed specifically for machine learning applications in seismic wavefield modeling and full-waveform inversion. The GlobalTomo dataset integrates high-resolution seismic simulations that span various scales, from acoustic and elastic wave propagation to planetary-scale simulations representing real Earth conditions. The paper demonstrates the utility of this dataset by benchmarking several machine learning models for both forward modeling and inversion tasks, underscoring the potential of ML to accelerate seismic data interpretation and enhance our understanding of Earth’s interior.

### Strengths
This paper addresses a key gap by providing a global-scale dataset that integrates ML-friendly features with robust physical modeling for seismic applications. The dataset’s design across three tiers (acoustic, elastic, and real Earth) allows it to support scalable and complex seismic modeling tasks.

### Weaknesses
1. Wavefield Estimation. The necessity of including the wavefield as part of the dataset is not entirely convincing. While the authors provide further discussion on this in Supplementary Section F.2, this inclusion could be misleading for two primary reasons.

First, from a practical inverse problem perspective, only surface wavefield measurements (seismograms) are typically available in real-world FWI applications. The full wavefield throughout the Earth’s interior is generally inaccessible and, therefore, impractical for use in inversion. Furthermore, the inclusion of the full wavefield could inadvertently encourage the development of models that rely on information not available in real-world scenarios, thus limiting their practical applicability. This is a critical concern as it could lead to over-optimistic performance evaluations that do not translate to real-world data.

Second, traditional model-based FWI methods do require calculating the full wavefield as they rely on directly solving the wave equation. However, end-to-end ML-based inversion strategies approximate the inversion process and thus do not depend on the full wavefield. These methods instead focus on estimating target parameters directly from surface measurements, bypassing the need for a complete wavefield solution. Therefore, the inclusion of the full wavefield seems unnecessary for the intended purpose of training end-to-end ML models for FWI.


2. Comprehensive Assessment of the Dataset.  An essential purpose of a benchmark dataset is to support various realistic scenarios that may arise in practical applications. A key example would be testing generalization capabilities. However, this aspect is not clearly addressed in the manuscript.

It remains unclear whether the dataset, or its three tiers, adequately represents different distributions or if they cover a range of scenarios that would facilitate generalization. No visualizations are provided to illustrate sample distributions, making it difficult to assess the dataset’s diversity. Specifically, it is unclear if the dataset adequately covers the range of velocity structures, source-receiver geometries, and noise levels that are typically encountered in real-world seismic data. Additionally, I did not find any generalization tests conducted with direct inversion methods, as outlined in Section 3.2.2. This raises concerns about the dataset's robustness across diverse inversion tasks.

### Questions
1. Could the authors clarify the intended benefit of including the full wavefield in the dataset, given that only surface measurements are typically available in realistic FWI scenarios? How does the inclusion of the full wavefield impact the dataset’s applicability to practical, real-world inversion problems where the wavefield is not accessible?


2. Could the authors provide more details on the distribution of samples within each tier of the dataset? Are there visualizations available to illustrate the diversity of scenarios represented?


3. Were any generalization tests conducted using direct inversion methods to assess the dataset’s performance across varied inversion scenarios? If not, it would be much appreciated if some generation tests could be conducted using the direction inversion methods used in this current manuscripts (InversionNet-3D, InversionMLP).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
- This paper presents the first 3D global synthetic dataset tailored for seismic wavefield modeling and full-waveform tomography, referred to as the Global Tomography (GlobalTomo) dataset.
- This paper also utilizes and compares several machine learning models on forward modeling and FWI based on this dataset.

### Strengths
- The dataset itself is good and could benefit the community a lot. 
- The paper is well-written and easy to follow.
- The figures and tables are clear.

### Weaknesses
I think the machine learning models are kind of simple. Based on my experience, MLPs seem not to be the best choices for 3D problems compared with other methods you chose in the paper (CNN or transformer). But the results show that MLP / InversionMLP performs best in most cases. I am concerned whether all methods are well-trained and under the best hyperparameters.

I am also concerned about the generalizability of the models, specifically whether they can perform well in out-of-distribution scenarios. The paper does not explore this aspect, which is crucial for real-world applications where the input data may not perfectly match the training data distribution.

In line 396, the paper says “To evaluate the flexibility of FWI”. Why is this FWI? I think this section is talking about forward modeling. Could you clarify whether this section is indeed about forward modeling rather than FWI?

### Questions
- If you are sure all methods are well-trained and under the best hyperparameters, could you explain why MLPs perform better than methods like CNN and Transformer in 3D cases, which seems counterintuitive? Or, could you provide additional analysis or ablation studies that might shed light on why MLPs are outperforming other architectures?

- Could you compare the performance of these methods in scenarios of out-of-distribution?

- In line 396, the paper says “To evaluate the flexibility of FWI”. Why is this  FWI? I think this section is talking about forward modeling. Could you clarify whether this section is indeed about forward modeling rather than FWI?

### Soundness
2

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes datasets for the forward and inverse modeling for global tomography. The forward modeling entails predicting seismogram from a velocity structure, while the inverse modeling solves for a velocity structure from an observed seismogram. They have considered three different cases for data generation: (1) Acoustic Ball (1km radius sphere filled with pure fluid medium), (2) Elastic Ball (1km radius sphere isotropic media), and (3) Real Earth (based on isotropic PREM model). Each dataset has two types of output data, the first type is surface seismogram data, and the second type is the seismic wavefield data. In the paper, the authors have employed several ML models for forward and inverse problems and have shown the efficacy of ML models in solving the two problems on the proposed dataset.

### Strengths
1.	The idea to generate a large-scale dataset for global seismic tomography is interesting and essential to bridge the gap between machine learning and seismic tomography.
2.	The proposed dataset has three tiers to model seismic wave propagation from simple to complex settings and for each tier the dataset contains seismic wavefield and seismogram information.  
3.	The paper explores multiple ML methods to establish a benchmark for both forward and inverse problems in seismic tomography.

### Weaknesses
1.	Although the paper is overall well-written, there are certain sections which is little obscure like model configuration, spherical harmonics, and data generation. These sections need improvement to understand how the dataset was generated, model training and inference results.
(a)	For generating different examples, do we always perturb the same 1D background model or different? How is the data generation algorithm create different varying geological settings in the dataset? How do we measure the variability in different velocity structures?
(b)	In the model configuration section, it is mentioned that the model 3D structure is generated by perturbing a 1D background model from -10% to 10%. Given a 1D background model, how are number of layers decided per model example and how the perturbation and parameterization (using spherical harmonics) work to create a synthetic example?

2.	The results section is not very clear to understand especially due to lack of enough evidence for certain claims. I would highly appreciate if the paper could provide following information
(a)	Evidence to back claims in the results section related to training of H-Fourier models, how was physical constraint incorporated in the training, improve overall flow of forward and inverse results discussion with more figures/visualizations and share modeling related information
(b)	Number of examples generated in each tier
(c)	Incorporate more evaluation metrics such as MAE, MSE, SSIM. 

3.	The results section is primarily limited to acoustic dataset (tier-1) and provides very little insights on experimentation on the elastic dataset (tier-2). There is no discussion on training and evaluation results for the tier-3 dataset (real earth) which seems to be the main Earth’s scale dataset for global tomography. Would it be possible to have some visualizations of some datasets from all tiers along with experimental results for forward and inverse modeling for tier-2 and tier-3 dataset? 

4.	The paper explores model generalizability only for in-distribution cases, and it may be better to also study out-of-distribution generalizability to investigate ML effectiveness for both forward and inverse problems.

### Questions
1.	Section 1 Introduction (Line 106): While the paper proposes to address the gap for high-resolution wave propagation modeling for the Earth’s entire scale, the Real Earth dataset employs wave with 30 second period. How does the 30 second wave period (likely low frequency) facilitate in generating high-resolution imaging of the internal Earth’s structure?

2.	Section 2.2 Model Configuration (Line 191): What is meant by Model Configuration (machine learning model, wave velocity distribution, or something else)? Assuming it means wave velocity distribution. The paper proposes to generate synthetic 3D velocity structure by perturbing a 1D background velocity model by -10 to 10%. While this may be more accurate for local heterogeneity, this assumption seems to oversimplify the 3D structure for the Earth’s scale data. Is there any rationale behind using this simplification or limitations in representing Earth’s complex structure?

3.	Section 2.3 Data Generation (Line 213): How many examples for velocity structures were generated per tier of dataset? How many source configurations were generated per tier of dataset? Is it same as number of velocities generated or different?

4.	Section 2.3 Data Generation (Line 221): The definition of the input and output variables is not clear and difficult to understand. For example, what does Source, Structure, Sample Number mean here? How does these parameters affect the quality of generated dataset in terms of heterogeneity, geological structures, and scale?

5.	Section 3 Experiments (Line 254): For wavefield dataset, there are 7 timesteps considered (0 to 3 seconds), with each timesteps consist of 16 slices and 3648 points per slice. How does these 16 slices represent the entire internal Earth’s structure? Does each slice represent a unique sub-region inside the Earth? (A schematic figure to represent this would be good) Why are there 3648 points per slice, are these points indicating positive and negative wave displacement in that slice? 

6.	Section 3.2.1 Forward Modeling (Line 324): Based on the wavefield dataset description in the line 253, the total number of timesteps should be 7 from 0 to 3 seconds, the Figure 2 shows that the results for 13 timesteps. Does the dataset contain 7 or 13 timesteps?

7.	Section 3.2.1 Forward Modeling (Line 324): Figure 2 shows seismogram data, how are source and receivers positioned relative to each other? A schematic diagram to explain this may be helpful to understand the seismogram data for each tier of dataset. 

8.	Section 3.2.1 Forward Modeling (Line 402): How was the physics constraints enforced to DeepONet that led to improved generalizability? Appendix B.1 shows governing physics equations for each tier of dataset but do not provide insights into training the model with physics. 

9.	Section 3.2.2 Inversion (Line 424) and Figure 4: What does it mean to select five random points for each test structure? Does this mean that there are 5 initial velocity guesses, and inversion is carried out for all of them independently? Which tier dataset is used for inversion here? Why the model pre-trained on acoustic tier is selected? Which model from the acoustic tier is selected for the forward simulation? Can we have some figures to compare the inverted velocity structures from different models for each dataset? How does the model pre-trained on one dataset generalizes to other dataset for both forward and inverse problems?

10.	Section 3.2.2 Inversion (Line 446): In the dataset description, the acoustic data is defined as a 1 km radius fluid sphere. Figure 6 shows inverted Earth’s structure derived from acoustic data. What does it mean? 

11.	Section 3.2.2 Inversion (Line 457): Does different starting point undergo optimization independently? If not, how the inversion algorithm is processing multiple starting point to reach to one ground truth while affecting each other?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper propose a dataset for the global tomography problem. The data set consists of earth models and the wave fields that are obtained by using numerical simulations. The goal of this data is to be able to Tain a forward an an inverse network that allows for fast solutions of the global tomography problem.

### Strengths
The main strength of this work is in the data. There are many researchers in the scientific machine learning community that are looking for complex data sets that they can test their methods. I believe that the data set may be used for that.

### Weaknesses
There are a number of concerns that I have when considering this work.
1. The main problem is the diversity of the earth models. It is not clear to me that the models used are diverse enough to serve as a data set for the task at hand. The authors did not discuss this point clearly but this may be the most important point in the data set. I the models are not diverse enough then how can we learn something meaningful?

2. The second problem with the models is that we do not have ground truth and we will never have. Unlike problems in image processing, It is impossible to "open" the earth and obtain its physical properties at the resolution needed. How do you know you do not have bias in your models? 

3. The testing of the forward problem is not convincing. Wave equation solvers typically being judged on accuracy and on dispersion. Numerical dispersion is particularly important for solving inverse problem as it can introduce artifacts. It would be nice if the authors do not treat the wavefield as an image but rather follow most numerical PDE books when estimating the solution of a PDE.

4. How would the forward model do for models that are out of distribution?

5. The inversion strategies use both optimization and direct methods where direct methods seems to win. Does this still work for out of distribution problems?

6. What is the data fit for all the inversion methods. Do you actually fit the data? How does this compared with standard Gauss-Newton inversion where the data fit is being considered with the forward problem

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
3
