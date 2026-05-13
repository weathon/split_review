# Open-CK: A Large Multi-Physics Fields Coupling benchmarks in Combustion Kinetics

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
In this paper, we use the Fire Dynamics Simulator (FDS) combined with the {\fontfamily{lmtt}\selectfont \textit{supercomputer}} support to create a \textbf{C}ombustion \textbf{K}inetics (CK) dataset for machine learning and scientific research. This dataset captures the development of fires in industrial parks with high-precision Computational Fluid Dynamics (CFD) simulations. It includes various physical fields such as temperature and pressure, and covers multiple environmental combinations for exploring \underline{multi-physics} field coupling phenomena. Additionally, we evaluate several advanced machine learning architectures across our {\fontfamily{lmtt}\selectfont {Open-CK}} benchmark using a substantial computational setup of 64 NVIDIA A100 GPUs: \ding{182} vision backbone; \ding{183} spatio-temporal predictive models; \ding{184} operator learning frameworks. These architectures uniquely excel at handling complex physical field data. We also introduce three benchmarks to demonstrate their potential in enhancing the exploration of downstream tasks: (a) capturing continuous changes in combustion kinetics; (b) a neural partial differential equation solver for learning temperature fields and turbulence; (c) reconstruction of sparse physical observations. The Open-CK dataset and benchmarks aim to advance research in combustion kinetics driven by machine learning, providing a reliable baseline for developing and comparing cutting-edge technologies and models. We hope to further promote the application of deep learning in earth sciences. Our project is available at \url{https://github.com/whscience/Open-CK}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper details a new dataset created using FDS for industrial fire parks. The authors use various state of the art SciML techniques on the dataset to show it's usefulness.

### Strengths
There is such a lack of data within the AI4Science domain, and in particular for fluid dynamics and fire modelling that any additional, well produced data is a strength. Clearly a lot of work has been undertaken to produce the data, which is a credit to the authors.

### Weaknesses
I'm afraid there are a number of weaknesses that makes this work, at present, not suitable for publication/presentation at ICLR:

1) Lack of any verification or validation of the underlying FDS methodology/mesh/technique for the simulated domain. 
2) there are some phrases in the document sound odd i.e the use of the word supercomputers in italics. It sounds a little odd and is repeated in several places
3) no discussion on how the data will be maintained/stored/accessed
4) limited discussion of the limitations of the work

Overall, not high enough quality at present but I would encourage the authors to revisit and improve the paper for future conferences/publications.

### Questions
as per above

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This is a strong work with good dataset and ML evals for an important application. The paper is written well. There is good documentation and open practices -- well done.

However, the language and claims can come across a bit strong for a scientific paper -- see questions. I can confidently recommend this paper for acceptance -- if my concerns in questions are addressed.

Edit 1: Questions and concerns have been addressed. Changing score to 8.

### Strengths
1. Good motivation and review of related work
2. Impressive dataset covering many scenarios and physical quantities with expensive compute.
3. Good eval with many architectures.
4. Open Repository
5. Good future insight and limitations discussion
6. Good documentation.

### Weaknesses
1. Language is a bit bold for some claims.



### Questions
1. Is OpenCK the first combustion CFD benchmark? This is a strong statement. For example, Sandia's Engine Combustion Network by Pickett,Payri et al has been providing open data and benchamrking with regards to gasoline and diesel CFD since about 9 years ago. Another similar effort to this is BLASTNet in Chung et al (NeurIPS 2023) which involved Direct Numerical Simulation data of canonical combustion configurations.  Please revise this statement to be more moderate.
2. "Open-CK involves several PDEs" -- All listed PDE's are actually just scalar/vector conservation equations. Is this statement really true?

3. It would be interesting to see if the effects of model scaling has metrics in table 2. Bigger,expensive models tend to outperform smaller models. What does MSE vs FLOPS or MSE vs Params, SSIM vs (FLOPs, Params) look like in a scatter plot? This can provide more insight into useful architectures.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This is data set and benchmarking paper that uses the Fire Dynamics Simulator (FDS) to create a Combustion Kinetics (CK) dataset for SciML research. It includes various physical fields such as temperature and pressure, and covers multiple environmental combinations for exploring multi-physics field coupling phenomena. The authors evaluate SOTA ML architectures to establish an Open-CK benchmark.

### Strengths
1. This is an interesting and potentially useful data set for SciML research, the authors made substantial computational effort to create the data set and establish the ML benchmark - the motivation of the work and description of the contributions are nicely laid out. 
2. The consideration of multiphysics simulations, particularly over complex boundaries/plant layouts is interesting and could lead to interesting SciML models and applications. 
3. The use of LPIPS metric and other natural image based metrics to evaluate the models is quite intriguing.

### Weaknesses
1. From the paper, it is not very clear how many samples are actually in the dataset - the authors mention that there are '300 different fire scenarios' (I could not open the Project website link that was provided in the paper - not sure if it's a problem on the server side or on my side). So, are there just 300 time series samples of different lengths across various combustion parameters and environmental conditions?

2. If I understand correctly, the paper considers only one geometrical layout for the data set. While the setup represents a typical industrial park scenario, the data set may not be rich enough for generalizable SciML research without having diverse geometrical layouts.

### Questions
1. Provide better description of the sample size in the data set. How does the '300 different fire scenarios' connect with the details provided in Table 1?

2. Can the data set be enriched by adding diverse layouts for the industrial park scenario? e.g., different number oil storage areas, other geometrical constructions/objects

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
4

### Summary
This paper unveils a novel benchmark dataset for improved modeling of combustion kinetics (CK) using data-driven techniques. Specifically, the dataset simulates the development of fires in industrial parks using computational fluid dynamics simulations using the fire dynamics simulator. In the paper, the authors detail that the generated dataset comprises 300 different scenarios of fire development all emanating from a single ignition source (SIS) or three ignition sources (TIS). In addition to the dataset, authors also conduct extensive experiments using state of the art scientific machine learning baselines to establish a research benchmark for modeling fire development, a critical and challenging problem. This dataset will fill a critical need, serving to accelerate the modeling of fire development using data-driven techniques.

### Strengths
1. The dataset is necessary and crucial. As pointed out by the authors, other datasets for fire development usually target satellite images and are in the context of wildfires or have low spatial and temporal resolution. 

2. The set of scientific machine learning models employed to evaluate performance on the developed dataset is comprehensive, setting up a strong research benchmark.

3. The rigorous experimental evaluation is well detailed and has been carried out with vision backbones (e.g., U-Net, ViT, ResNet), scientific machine learning backbones (e.g., Fourier Neural Operator) as well as spatio-temporal backbones (e.g., ConvLSTM).

### Weaknesses
1. Currently, the narrative lacks detailing of the domain background of the combustion kinetics field. For the reader to fully appreciate the comprehensive nature of the benchmark, a more thorough description of the problem and the generated dataset is necessary. Specifically, a reading of the current version of the paper does not leave the reader with a sense of how representative the current Open-CK dataset is of real-world single-source (or multi-source) fires in industrial contexts?

2. A more thorough description of the design decisions made to select the various scenarios is necessary. These scenarios are summarized in Table 1 but a detailed description is lacking of why each of these scenarios is important, representative o real-world scenarios and challenging to model. Without this, it is hard to truly appreciate the extent of the contribution of this dataset to the field of combustion kinetics.

3. Finally, a better motivation about exactly why modeling the physical coupling between the multiple physical fields is challenging and crucial is necessary to fully understand the richness and impact of the current dataset in the CK context.

### Questions
1. How were each of the 300 scenarios conceived and selected for simulation? How representative are these 300 scenarios of real-world fire development dynamics?

2. What might be the possible deficiencies of models trained on the current datasets in predicting real-world fire development dynamics? Specifically, how can a model pre-trained on the Open-CK dataset be adapted to real-world fire dynamics modeling?

3. What are some existing popular theoretical models (reduced-order or otherwise) that are employed to estimate fire development dynamics, how do data-driven models compare to these models w.r.t physical consistency and estimation accuracy?

### Soundness
2

### Presentation
2

### Contribution
3
