# Synthetic Datasets for Machine Learning on Spatio-Temporal Graphs using PDEs

- Decision: Reject
- Scores: 8, 3, 3, 6

## Abstract
In this work, we describe the creation and use of synthetic datasets based on various partial differential equations to support spatio-temporal graph modeling in machine learning for different applications. More precisely, we showcase three equations to model different types of disasters and hazards in the fields of epidemiology, atmospheric particles, and tsunami waves. Further, we show how such created datasets can be used by benchmarking several machine learning models on the epidemiological dataset and, additionally, by showing how pre-training on such synthetic datasets can improve model performance on real-world epidemiological data. The presented methods enable others to create datasets and benchmarks customized to individual requirements. The source code for our methodology and the three created datasets can be found on https://github.com/github-usr-ano/Temporal_Graph_Data_PDEs .

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors identify a lack of established benchmark data sets for spatio-temporal graph learning, which inspires them to generate synthetic spatio-temporal graph data using partial differential equations (PDEs). They consider 3 different PDEs: an epidemiological PDE, an advection-diffusion equation, and a wave equation. They then use the synthetic data generated from the epidemiological PDE to compare different temporal and spatio-temporal models on different prediction tasks, including forecasting. Perhaps most importantly, they demonstrate the importance of the synthetic data for transfer learning on a prediction task involving real epidemiological data.

### Strengths
- High potential significance by creating synthetic data benchmarks in an area where they are lacking. I could certainly envision these datasets being used in future spatio-temporal graph learning papers.
- Very interesting experiment on real epidemiological data demonstrates the potential of the synthetically generated data to translate to prediction tasks on real data. This is much stronger evidence for the utility of the synthetic data than I typically see in this type of paper.
- Detailed comparison of temporal and spatio-temporal models on a variety of prediction settings for the synthetically generated epidemiological data.

### Weaknesses
 - Some missing details on the real data experiment--see question 1 below. A more detailed description in the supplementary material would be useful.
- Sizes of the datasets seem to be fixed to somewhat small spatio-temporal graphs with a few hundred nodes and a few thousand edges, potentially limiting the scope. It is unclear if the method can scale to larger graphs with tens of thousands or millions of nodes, which are common in many real-world applications of spatio-temporal graph learning. The current scale may not be sufficient to fully evaluate the performance of complex models.
- No results on the advection-diffusion and wave equation data in the body of the paper. Given the interests of the ICLR audience, I believe that the paper would be strengthened if there were more results on these datasets, particularly in the main body of the paper, while moving some details from Section 2 into the supplementary material. The absence of these results in the main body makes it difficult to assess the general applicability of the proposed synthetic data generation method beyond the epidemiological context.

Minor issue:
- Line 041: datata -> data

### Questions
1. What is the prediction task in Section 4.3? Is this a forecasting task?
2. Is there an easy way to generate larger spatio-temporal graphs using your proposed method?

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
This paper presents a method to create synthetic datasets based on different PDEs that capture different applications. Three PDE equations are presented as examples, namely epidemiology, atmospheric particles, and tsunami waves. Empirical analysis demonstrates that the generated synthetic datasets can be used to benchmark machine learning models, and pre-training on the synthetic datasets can greatly improve model performance on real-world epidemiological data.

### Strengths
Contribution: As the spatio-temporal graph data lacks, this paper presents an alternative. With high-quality synthetic datasets, machine learning studies can be improved compared to theoretical analysis.

Presentation: The three example PDE equations came from reliable sources, and help with demonstrating how to generate synthetic datasets.

### Weaknesses
1. This paper boldly claimed that real-world datasets have limitations in quality due to high noise. I personally believe that clean synthetic datasets are better for exploration and preliminary studies. In contrast, although the real-world dataset has high noise, it is necessary before the application is implemented. So, there is a trade-off between cleanness and reality. 

2. Other ways exist to generate synthetic datasets, such as quasi-Monte Carlo simulation. This paper fails to compare with existing methods to demonstrate the superiority of the PDE-based generation method.

3. In the empirical analysis of the pre-training, effectiveness is measured by RMSE loss, which could skew towards the high-performing models. With previous low RMSE losses, a small definite improvement will show a bigger percentage. Have you considered other measurements?

### Questions
How is the presented dataset generation method better than the existing ones? I think this comparison need to be discussed in the paper.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this work, the authors generate synthetic spatio-temporal graphs with fixed structure and evolving node features by solving PDEs.

### Strengths
- The authors identified the gap in the literature, wherein high quality temporal graph datasets are not abundant.

### Weaknesses
### `(W1) Benchmarking`
The authors use the following models:
- Repetition (naive)
- RNN (classic)
- TST (Transformer)
- MP-PDE (modified baseline)
- RNN-GNN-Fusion (source of this model is not clear)
- GraphEncoding (modified baseline)

They report the performance of these models on the synthetic datasets in Table 1 (Forecasting column), where the model `GraphEncoding` performs worse than the naive baseline `Repetition`. This is an odd observation, and better baselines should've been used for benchmarking. The fact that a model designed to incorporate spatial information (`GraphEncoding`) performs worse than a model that ignores it (`RNN`) is also concerning. This suggests that the datasets may lack meaningful spatial information, undermining their utility for benchmarking graph learning algorithms. Furthermore, the use of a custom `RNN-GNN-Fusion` model, instead of established temporal GNN architectures, makes it difficult to assess the true performance of the datasets. It is recommended to check the paper **Graph-based Multi-ODE Neural Networks for Spatio-Temporal Traffic Forecasting** (TMLR) and the baselines used there. For example, the authors could test out the benchmarks `STGODE`, `GRAMODE`, and `ARIMA` on the generated datasets.

### `(W2) Contribution Claim`
The PDEs used to create the datasets are not novel, nor is the technique to solve them. The authors claim:
> This or any similar epidemiological PDE, based on the SIR-ODE (Kermack & McKendrick, 1991), has never been solved numerically

And then in footnote 1 on page 4, the authors mention:
> The methodology we use here as well as the numerical code can be found in this tutorial of the used library https://www.dealii.org/current/doxygen/deal.II/step_23.html. We made only smaller adaptions to the code.

It is not clear what is the contribution of this work, apart from setting hyper-parameters of known PDEs and solving them numerically using known libraries. The authors claim to generate spatio-temporal graphs, but the graph structure is fixed, and the node features are generated by solving PDEs on a mesh, which is then sampled at fixed locations to form the nodes of the graph. The novelty of this process is not clear, and the authors do not clearly highlight how their approach differs from existing methods like PDEBench, beyond using FEM instead of FVM.

### `(W3) Lack of new insights`
Consider this experiment: there are n number of models $M_1, M_2, \cdots, M_n$ and a standard dataset $D$ which is used in the literature. When the models are tested on this dataset, it results in a ranking $r_1, r_2, \cdots, r_n$. Now consider a synthetic dataset $D'$ which when used for benchmarking the models results in the ranking $r_1', r_2', \cdots, r_n'$. Comparing these two rankings can highlight the use of the synthetic dataset $D'$ and the authors could comment on the reason for such change in ranking, if any. On the other hand, if there is no change in the ranking, then the dataset $D'$ brings no new insights.

It is recommended that the authors run this experiment using at least two standard spatio-temporal traffic datasets `METRLA` and `PEMSBAY`.

### `(W4) Organization of the contents`
The content in the paper is not well organized. The focus was moving from one topic to another without a smooth logical transition. Here are some thoughts on an alternative structure for the paper:
- In **Introduction** the authors only discuss the problem they are trying to solve and dedicate a clear paragraph to the motivation, then in a subsection they discuss the **related works**, as in what has been tried before in the same setting.
- Then, in a **Methodology** section, the authors should expand on their proposed technique using a block diagram giving a higher-level overview of the work, and present a detailed version through a step-by-step algorithm. The PDE should be kept generic, and the three special cases can just be mentioned after the algorithm is presented
- Then, a section on **Experiments** should be included to specify clearly what the authors what to conduct, and divide experiments into self-contained subsections, with highlighted key insights derived from the results. Here, the authors may mention the baselines being used and delegate further information on their implementation/modification to the Appendix for those interested.
- The figures with **dataset examples** should be deferred to the Appendix as well.
- In the conclusion section, the authors should clearly state the **limitations** of the work, and what could be potentially improved in the future.
- Some results which are currently in the Appendix should be brought to the main body.

### `(W5) Limitations of the generated datasets`
The graph structure is fixed, and the dimensionality of the node feature is limited to 2. The fact that the graph structure is fixed over time limits the applicability of these datasets to real-world scenarios where the relationships between nodes may evolve. Furthermore, the low dimensionality of the node features (only 2) may not be sufficient to capture the complexity of real-world spatio-temporal phenomena. It is unclear if models trained on these synthetic datasets with node dimension 2 can effectively transfer to real datasets with higher node feature dimensions.

### questions:
 ### `(Q1) Transfer Learning` (Sec. 4.3)
- Could the authors please elaborate on the meaning of fine tuning?
- How does the chosen (modified) baselines used in this paper compare against the standard spatio-temporal benchmarks, for example `GraphWaveNet`, and `STGODE`?
- Why did the authors only report validation loss?
- What is the test RMSE on (1) training a model $M$ on real data $D$, and (2) training the model $M$ on real data $D$ after pre-training on synthetic data $D'$?
- How do the models compare against the naive repetition baseline?

### `(Q2) Noise` (Sec. 4.2)
The authors mention:
> We found the Gaussian noise with distribution $\mathcal{N}(0, 0.01)$ to be an interesting setting for the normalized dataset.

Could they please provide their rationale for choosing the specific noise variance? The explanation would aid in understanding the experiment better.

- The figures 10-12 are not clear; Why is there a drop in RMSE for dropout noise? Are the zero values emulating missing sensor data considered or ignored during evaluation? In the literature, zeros are treated as missing values and ignored during training and evaluation.
- In Table 1, it is better to report the relative change in RMSE. That would show that the naive repetition baseline is robust to the Gaussian noise considered in the study.


### Questions
### `(Q1) Transfer Learning` (Sec. 4.3)
- Could the authors please elaborate on the meaning of fine tuning?
- How does the chosen (modified) baselines used in this paper compare against the standard spatio-temporal benchmarks, for example `GraphWaveNet`, and `STGODE`?
- Why did the authors only report validation loss?
- What is the test RMSE on (1) training a model $M$ on real data $D$, and (2) training the model $M$ on real data $D$ after pre-training on synthetic data $D'$?
- How do the models compare against the naive repetition baseline?

### `(Q2) Noise` (Sec. 4.2)
The authors mention:
> We found the Gaussian noise with distribution $\mathcal{N}(0, 0.01)$ to be an interesting setting for the normalized dataset.

Could they please provide their rationale for choosing the specific noise variance? The explanation would aid in understanding the experiment better.

- The figures 10-12 are not clear; Why is there a drop in RMSE for dropout noise? Are the zero values emulating missing sensor data considered or ignored during evaluation? In the literature, zeros are treated as missing values and ignored during training and evaluation.
- In Table 1, it is better to report the relative change in RMSE. That would show that the naive repetition baseline is robust to the Gaussian noise considered in the study.

----

### `Feedback for improvement`
- The paper needs to be reorganized and re-written for clarity
- Relevant baselines for node feature forecasting should be used for benchmarking
- The benchmarking results should be contrasted with the ranking on standard datasets to deliver new insights
- The transfer learning and noise robustness experiments need to be clarified and more details should be added
- The experiment setup should be explained more clearly
- The limitations of the work should be admitted
- The contributions should be stated clearly
- A scalability section can be added, where synthetic datasets can be generated for increasing number of nodes, and the relative performance of the baseline models can be reported across the varying size.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a methodology for generating synthetic spatio-temporal graph datasets using partial differential equations (PDEs). The authors illustrate their approach by creating three datasets that model disaster scenarios: the spread of epidemics, atmospheric particle movement, and tsunami propagation. The main contributions of this work include (1) a detailed methodology that employs the Finite Element Method to convert PDE solutions into graph data, (2) three ready-to-use synthetic datasets, (3) an open-source implementation for creating custom datasets, and (4) empirical validation through benchmarking and transfer learning experiments.

### Strengths
- The PDE solving methodology demonstrates mathematical rigor through detailed documentation and established numerical methods.
- The authors provide practical resources through ready-to-use datasets and accompanying code for the research community.
- The experimental results strongly validate the approach by showing significant benefits in transfer learning tasks.
- The framework enables researchers to create custom datasets by modifying parameters and PDEs for different applications.

### Weaknesses
 - The paper only demonstrates relatively simple PDEs despite covering three different scenarios. While the chosen PDEs (diffusion, advection-diffusion, wave) represent different classes, they are all linear and do not explore the complexities of non-linear terms or coupled systems. This limits the applicability of the generated datasets to more complex real-world phenomena.
- The transfer learning experiments are limited to epidemiological applications without exploring other real-world domains. Although the authors demonstrate transfer learning for an epidemiological task, the lack of experiments in other domains, such as climate modeling or fluid dynamics, makes it difficult to assess the generalizability of the approach. The datasets created for atmospheric particle movement and tsunami propagation are not leveraged for transfer learning, which is a missed opportunity.
- The authors do not thoroughly analyze how variations in PDE parameters impact the learning outcomes. The paper lacks a systematic study on how changes in parameters like diffusion coefficients, wave speeds, or boundary conditions affect the quality of the synthetic data and the performance of models trained on it. This analysis is crucial for understanding the sensitivity of the method and its robustness.

### Questions
1. Have you explored how the choice of PDE parameters affects the quality of the synthetic data for transfer learning?
2. Could this approach be extended to more complex PDEs with coupling or higher-order terms?
3. How do the computational requirements scale with domain size and mesh resolution?
4. Have you considered applications beyond the disaster scenarios presented?

### Soundness
3

### Presentation
3

### Contribution
3
