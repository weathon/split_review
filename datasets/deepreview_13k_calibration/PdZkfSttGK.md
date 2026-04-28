# Nonparametric Covariance Regression for Massive Neural Data on Restricted Covariates via Graph

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Modern recording techniques enable neuroscientists to simultaneously study neural activity across large populations of neurons, with capturing predictor-dependent correlations being a fundamental challenge in neuroscience. Moreover, the fact that input covariates often lie in restricted subdomains, according to experimental settings, makes inference even more challenging. To address these challenges, we propose a set of nonparametric mean-covariance regression models for high-dimensional neural activity with restricted inputs. These models reduce the dimensionality of neural responses by employing a lower-dimensional latent factor model, where both factor loadings and latent factors are predictor-dependent, to jointly model mean and covariance across covariates. The smoothness of neural activity across experimental conditions is modeled nonparametrically using two Gaussian processes (GPs), applied to both loading basis and latent factors. Additionally, to account for the covariates lying in restricted subspace, we incorporate graph information into the covariance structure. To flexibly infer the model, we use an MCMC algorithm to sample from posterior distributions. After validating and studying the properties of proposed methods by simulations, we apply them to two neural datasets (local field potential and neural spiking data) to demonstrate the usage of models for continuous and counting observations. Overall, the proposed methods provide a framework to jointly model covariate-dependent mean and covariance in high dimensional neural data, especially when the covariates lie in restricted domains. The framework is general and can be easily adapted to various applications beyond neuroscience.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors consider modeling neuroscience data (such as LFP and neural spike count data) in settings where experimental conditions can vary in complicated ways (that may not be well-modeled by assuming conditions lie in a Euclidean space, for instance).  They propose a non-parametric mean-covariance regression model.   They impose smoothness along both experimentation conditions and latent factors. To handle restricted domains they incorporate Graph Laplacian (GL) kernels.  For count data they handle non-conjugate count likelihood using a data augmentation technique.  In the inference step, they propose an MCMC algorithm with a data augmentation technique and derive full conditional to get posterior samples. They consider both continuous (LFP) and count observation real world neuroscience datasets.

### Strengths
## Strengths
- Analyzing neuroscience data (esp. count also LFP) is challenging but important.  
- The problem of handling restricted spaces arising from experimental conditions is well-motivated.
- The use of a graph-Laplacian GP to allow for more flexibility than assuming an unknown manifold is interesting.
- The presentation overall was good.
- Experiments are included from two real-world neuroscience experiments, one on LFP data and one for count data.

### Weaknesses
## Weaknesses
### Major
- My major concern regards technical novelty.  From my reading, the results seem to largely follow from integrating two key prior works, Fox and Dunson 2015 which proposed  predictor-dependent factor loadings modeled using GPs and Dunson et al 2021 which studied Graph Laplacian based GP regression for restricted domains.  Perhaps the authors could elaborate on any significant technical challenges that were overcome. Specifically, the combination of these two approaches, while practically useful, does not seem to introduce significant theoretical or methodological advancements. The core idea of using a GP prior for factor loadings and a Graph Laplacian kernel for restricted domains is directly adopted from these prior works, and it's unclear what novel mathematical or statistical insights are gained by combining them.
- The title includes “MASSIVE NEURAL DATA” and “massive” is mentioned several times but not described in particular with respect to computational or sample complexities
    – can you elaborate what ranges of which data dimensions qualify as “massive”?  
    - The computational complexity of the proposed method is not discussed, especially important in settings with massive data; how does the complexity vary with different data dimensions?  For instance, how does the computational cost scale with the number of experimental conditions, the number of neurons, and the length of the recording? A detailed analysis of the computational bottlenecks, such as the matrix inversions required for the GP, is missing.
    -  Relatedly, empirical run-times for your experiments and the GPWP baseline are not reported
    - sample complexity is not analyzed theoretically or experimentally
    - The HC experiment involved 36 neurons in one recording session  with 200 ms bins.  The LFP data set I am not sure of the dimensions (eg LFPs from 13 areas – how many LFPs recorded per area?), but from the description did not appear to be ``massive.’’  The lack of clarity on the scale of the datasets used makes it difficult to assess the method's applicability to truly massive datasets.
    - (minor) in the discussion, a point is made regarding computational complexity in lines 467-470 “in applications to massive data” which sounds like saying in settings with even larger data dimensions than is considered here


### Minor
- For the GPWP baseline (Nejatbakhsh et al., 2023), the authors mention the used "single trial", but did not include further discussion on the choice.  It's unclear why the single-trial version was chosen over other possible implementations of GPWP, and how this choice might affect the comparison. A more detailed justification for this choice is needed.
- The GPWP reported value in the simulation experiment for the Gaussian case differs dramatically – any thoughts why that is? The large discrepancy in the Gaussian simulation raises concerns about the reliability of the baseline implementation or the experimental setup. A thorough investigation of this discrepancy is needed.
- The L-GP baseline’s scores in most experiments (to me) seemed pretty close to the proposed method. This raises questions about the practical advantages of the proposed method over the L-GP baseline, particularly given the added complexity of the proposed approach. A more detailed analysis of the conditions under which the proposed method significantly outperforms the L-GP baseline is needed.


### Very minor (Typos/etc.)
- line 71 ‘massive neurons.’
- 081 "(p >> N)" although standard notations, p and N are have not been introduced before this line
- a few commas start a new line after equation blocks (eg line 148)
- line 196 ‘identifiablility.’

### Questions
(I have some doubts related to technical novelty, computational complexity, sample complexity, and baselines mentioned above -- clarification on those points would be appreciated)

### Soundness
3

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
3

### Summary
This work proposes a nonparametric mean-covariance regression model that leverages latent factor analysis and Gaussian Processes (GPs) to jointly model the mean and covariance of the high-dimensional neural data. Despite the a bit hard to follow writing flow, a notable claimed contribution is the integration of graph-based Gaussian processes to manage covariates in resricted subspaces with the MCMC algorithm. The model is validated through simulation dataset and applied to real-world LFP and HC neural datasets.

### Strengths
1. The introduction of graph-based Gaussian processes to handle restricted covariates adds a novel dimension to mean-covariance modeling, which I believe is helpful for neural data. Because this approach can be effective while maintaining the interpretability of the method.
2. The authors employ an MCMC algorithm with data augmentation techniques to handle intractable count models effectively, which can be more computationally effficient.
3. The authors argued and claimed that this proposed framework can be extended beyond neuroscience resaerch to other domains requiring mean-covariance modeling under similar constraints.

### Weaknesses
1. The paper is a bit hard to follow in writing, the scientific question or mathematical task you hope to solve is not very clear.

2. There has the assumption of independent GPs for each factor dimension, although computationally efficient, might overlook some inherenet underlying dependencies between factors that could be relevant in most neuroscience applications.

### Questions
1. What's the potential broader applications of this framework beyond neuroscience?
2. My other concerns please relate to the Weakness section.

### Soundness
3

### Presentation
2

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
The authors present a framework for modeling neural data and covariates through including graph properties of covariates to account for restricted subspaces. They demonstrate their method in simulation and in two experimental datasets.

### Strengths
- The inclusion of accounting for restricted space / inputs is smart and very relevant for neuroscience applications in particular. 
- The model components and math are well explained individually, though the thread of motivation throughout the methods section could be strengthened to connect back to the overall picture.  
- Simulations, training, selection of parameters, and results on experimental datasets are all very clear with a high level of detail (needed for any future work or replication, which is excellent).

### Weaknesses
 - The results overall are underwhelming. In the simulated data, all model fits look extremely similar. The differences in explained variance between models are marginal, and it's unclear if these small differences would be meaningful in a neuroscience context, where variability is often high. The PC plots are presented as results, but the interpretation of these plots is not sufficiently explained. What specific insights about the neural data or underlying processes do these PCs reveal? The manuscript lacks a clear demonstration of novel findings derived from this modeling approach.
- Computational costs are discussed but not shown empirically. The authors mention the computational burden, particularly with large datasets, but do not provide any quantitative analysis of the runtime or memory usage of their method compared to alternatives. This makes it difficult to assess the practical feasibility of the approach.
- Minor notes: typo (extra ')') in line 66 
- References to e.g. Figure 4 (which is really in the supplement) are confusing. 
- Grammar throughout could use some editing for correctness and clarity (e.g., the sentence spanning lines 82-84 doesn't make sense to me). 
- The provided code is complex (many files/functions) and lacks documentation, and is in Matlab, which lessens its overall impact in the ML field (and likely the efficiency and speed of computation for MCMC). The lack of documentation makes it difficult to understand the specific implementation details, and the choice of Matlab limits accessibility and potential for integration with other ML tools.

### Questions
- The code implementation appeared custom. Why not use established packages where appropriate (e.g. MCMC)?
- "we observe that the inference can be sensitive to hyper-parameters ({, K, t}) for GL-GP" (line 222) Is there evidence to show here?
- How does this scale to higher numbers of latent factors and increased dimensionality?  The simpler experiments showed "L = 10 is large enough" (line 262), so perhaps it is not a concern for low-dimensional tasks, but I would be curious to know the authors' thoughts on scalability (to tasks involving more freely moving behaviors, for example). 
- The observed data for the simulations in Figure 1 were fairly widely spread out throughout the space. How well would this method work for the cases where test or new data extended outside the range of previous observations?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present a non-parametric covariance regression method that allows modeling non euclidean via the  Graph Laplacian Gaussian process proposed by Dunson et al. 2022. They perform numerical experiments on simulated and neuron data.

### Strengths
The paper is sound, correctly written, and well-motivated. Overall, the work reads solid, and the method proposed seems to work relatively well.

### Weaknesses
The paper essentially relies on the work of Dunson et al. and the presented work seems to be closer to an adaptation of this work than a novel prior /method in the context of covariance regression. While this is interesting in principle, the method contribution seems a bit limited to a slight variation of the original work of Dunson and colleagues. Similarly, the authors do not tackle any particularly novel complex sampling scheme for their MCMC part and rely on existing work that they blend with the GL-GP prior to Dunson and colleagues.

Further, the simulations are somehow limited (perhaps due to the heaviness of the computation for inference). The simulation section lacks a thorough exploration of the parameter space, and it's unclear how the method performs under various conditions. For instance, the number of neurons and the length of the time series are not systematically varied to assess the method's robustness. The choice of simulation parameters seems somewhat arbitrary, and a more rigorous approach would be beneficial.

Figure 6 seems to advocate the most for the method, but Figures 1, 4, and 5 do not strike me as proper improvements. The improvements shown in these figures are marginal at best, and it's difficult to discern a clear advantage of the proposed method over existing approaches. The lack of substantial improvement in these figures raises concerns about the practical utility of the method in scenarios beyond the specific conditions of Figure 6. Lastly, it would have been nice to compare with non-GL-GP methods (perhaps a standard vanilla GP approach).

### Questions
Have run similar experiment using some of the competing methods?
Could you clarify the data size (covariate and neurons data).

### Soundness
3

### Presentation
2

### Contribution
2
