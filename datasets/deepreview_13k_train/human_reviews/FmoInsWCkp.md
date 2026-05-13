# Predicting Time-Varying Flux and Balance in Metabolic Systems using Structured Neural ODE Processes

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Flux-balance-analysis is one of the most important techniques used to determine the effect of environmental stress on cellular organisms-- for example in the form of drugs. For doing so the techniques use Genome-Scale-Metabolic-Models that take a lot of effort to build meticulously, in this work we aim to bypass that effort using novel data driven techniques. Our work uses time varying scRNA-seq gene-expression datasets from studies published on GEO (gene-expression-omnibus) and get time varying metabolic flux values from them. We then use our proposed novel architecture, CSNODEP (controlled structured Neural ODE Process), to learn the dynamics, predict gene-expression distribution on unseen timepoints, and predict metabolic flux distribution on unseen timepoints for different metabolic pathways under environmental stress simulated by gene-knockouts. We've also open-sourced our datasets and scripts to perform the study on different datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenging problem of predicting metabolic flux and metabolic balance from single-cell data. The authors formulate this prediction problem as learning the underlying dynamics of metabolic flux and metabolic balance and propose a novel method, structured neural ODE process (SNODEP), based on neural ordinary differential equations (Neural ODEs). Through extensive empirical experiments, the authors demonstrate that their novel method, SNODEP, yields improved performance on metabolic flux and metabolic balance prediction relative to baseline methods.

### Strengths
The proposed method, SNODEP, presents several key contributions that help address the challenging problem of metabolic flux and balance modelling and prediction: 

- SNODEP is able to effectively and efficiently model the dynamics of metabolic flux and balance, normally a challenging endeavour, by formulating metabolic flux and balance prediction as a data-driven problem. 
- SNODEP is evaluated over an extensive set of different pathways and experiments to showcase its utility for predicting metabolic flux and balance.
- The proposed method can learn the dynamics of metabolic flux and metabolic balance in regularly and irregularly sampled time-series settings as well as under various gene-knockout conditions.

### Weaknesses
Although this work presents a novel perspective for tackling the problem of predicting metabolic flux and metabolic balance under a data-driven framework, it contains several unaddressed items that limit the overall quality and contribution of this work. For example:

- At times, the presentation and exposition of text in the manuscript is difficult to follow. For example, the learning objective in the problem formulation section, which appears to be a key section of the paper, is not very clear. Moreover, equations throughout the text don't have labels -- it would be helpful to numerically label all equations and reference them in the text. See the questions below for further details.
- Evaluation metrics are limited, only the mean squared error (MSE) metrics is considered. This provides a narrow view and comparison of model performance relative to baselines. The task appears to be to predicting over distributions of cells, in which case it is worth considering a wider range of metrics that quantify prediction performance over distributions (see questions below). 
- It feels that the novelty and methodological contribution is limited. SNODEP incorporates a variety of data-driven learning tools, including Neural ODEs, variational inference, and recurrent architectures. Given this, the primary contributions and novelty of the proposed method appear to be the application to predicting metabolic flux and metabolic balance in a data-driven way. In contrast, there is limited advancement in the individual methodological components used in this work.

### Questions
- Line 181: "the goal is to learn a model $F: t \rightarrow Y(\theta) ...$". Does the model only take time as input? My understanding is that $F$ is the decoder. Is using just time sufficient?
- What does the $Y$ variables represent? The distributions $\{G, M^f, M^b, \tilde{M}^f, \tilde{M}^b \}$? This is not entirely clear.
- If the objective is to predict entire distributions, why only consider the mean squared error (MSE) metric? Why not consider other metrics which can be specifically used to quantify the distance between distributions? For example, the Wasserstein distance and/or maximum mean discrepancy (MMD) distance. 
- What is the setup for predicting metabolic flux and metabolic balance with gene knockouts, i.e. is this for *test* gene knockouts that are seen during training, or gene-knockouts *unseen* by the model during training? This is not entirely clear.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a forecasting architecture based on Neural Ordinary Different Equation Processes (NODEP) which they call Strutrude Neural ODE Process (SNODEP) and applies it to the problem of forecasting gene expression and metabolic flux and balance values across time. More specifically, given a time series of single-cell gene expression data, the authors first generate metabolic flux and balance values from this data using the previously published [scFEA algorithm](https://genome.cshlp.org/content/31/10/1867.short). They do this both for the actual data as well as for synthetic genetic knockout data produced by overwriting some genes' expression value to zero and then applying the scFEA algorithm to this semi-synthetic dataset. Given a partially observed time course of this data, the task then is to predict the value at future time points.

In order to solve the task, the authors modify the original NODEP architecture. NODEP parametrizes distributions over ODEs through an encoder-decoder framework. In this framework, the authors change the latent distribution from Gaussian to Log-normal and the sampling distribution/loss function from Gaussian to Poisson to better match the nature of the gene expression data. Moreover, they replace the order-invariant encoder architecture of the original NODEP framework with time-structured networks such as Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU).

They apply this framework to one dataset of human pluripotent stem cell differentiation and observe improved MSE performance compared to Neural Process (NP) and NODEP baselines.

### Strengths
The specific proposed changes to the NODEP architecture look novel to me.

### Weaknesses
 * **Limited overall contribution:** The paper makes two contributions, introducing the metabolic system forecasting problem as a test case of interest and developing a novel architecture to solve it. In the following, I will outline why I think it does not hit the mark in either of those areas.
* **Poorly motivated metabolic system forecasting problem**
    * While understanding metabolic flux and balances is useful, the authors don't make a strong point for why the forecasting problem is specifically impactful. They consider an 80%/20% data split, so if they could show near-perfect prediction of future values, this would correspond to a 20% saving in experimental budget. Is that impactful enough in this domain for people to adopt this? Moreover, they make no attempt in characterizing how good is "good enough". The only evaluation shown is mean squared error. Are there specific scientific questions that can be solved or cannot be solved at the attained accuracy as compared to the baselines?
    * ODE systems often come with the advantage of understanding inherent dynamics of the underlying system. It seems to me like the NODEP formulation foregoes this in favor of an abstract latent space. However, even latent spaces could lend themselves to interpretations.  Unfortunately, the authors do not show any interpretation of the learned systems.
* **Narrow scope of ML contributions**
    * While SNODEP definitely seems superior to NODEP in the presented experiments, the paper leaves me wondering which of the changes (different neural network architecture, different loss function, different latent distribution) is responsible for the performance boost. This could easily be explored in ablation studies.
    * To meet the bar of a significant machine learning contribution, I would have liked to see comparisons of SNODEP on problems in the original NODEP paper and related subsequent publications, not only one very bespoke biological problem setup.
* **Limited choice of baselines:** The considered baselines are verry narrow in scope, essentially copied over from the NODEP paper. If I understand the metabolic systems prediction task correctly as a time series prediction task, what about trying simpler methods (like LSTM or GRU directly applied to the data) or time series foundation models?
* **Poor presentation of problem & results:**
    * I could not fully understand the inputs and outputs to the method (see questions below).
    * I am confused as to why all the MSE results are shown as MSE curves over training epochs. This suggests no replicate experiments were performed and thus that no uncertainty quantification on the results can be performed. It would have been simpler to summarize the final MSE values as bar plots or tables with error bars/intervals.

### Questions
* I did not fully understand the inputs and outputs to the method. For example, are the gene expression values and metabolic flux and balance values treated as separate time series or does the method process them jointly?
* Could the problem be set up as a regular prediction task, with a simple LSTM or GRU architecture to predict, or are there specific problem characteristics that force the use of ODE based architectures?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This papers proposes a new method (SNODEP) to predict temporal flux and balance in metabolic systems. The architecture relies on a Neural ODE approach where they model the joint temporal evolution of scRNAseq, flux, and balance. The model is then trained to predict the future of the trajectories based on a contextual window. The authors state that their machine learning contributions includes modifying the emission distribution, as well as a new structured encoder approach for encoding context. The experiment section shows comparison with neural processes and neural ode processes, and shows that SNODEP performs better on scRNAseq forecasting, as well as flux and balance prediction.

### Strengths
Predicting flux and balance from metabolic systems in a temporal way is a very interesting topic and the Neural ODE formalism seems well adapted for this task. Therefore, the motivations of the paper are clear and the intended impact is evident.

The results suggest than SNODEP outperforms the considered baselines, highlighting its potential for metabolic predictions.

### Weaknesses
A. The contributions of this paper are insufficient from a machine learning perspective.

1. changing the emission distribution of a neural ODE model is typically considered a design choice in all existing NODE architectures. Such that choosing a Poisson emission can hardly qualify as a contribution. 
2. I am afraid that the identified limitation of the lack of structure for the conditioning is artificial. The authors state that : "The encoded representation is calculated using context points without any particular structure in NODEP. [...] The order between the context points and their sequential dependence on each other is not efficiently utilized." This may be the case for the specific NODEP model the authors refer too but this statement is inaccurate for most NODE models such as RNN-ODE (Rubanova et al.) or GRU-ODE (De Brouwer et al.)

Given that these are the two contributions laid out by the authors, the machine learning impact is minimal. That said, that does not take away anything from their impact for biological modeling (metabolic).

B. Modeling problems.

1. The authors appear to consider that cells taken at different time points form a time series. However, they recognize that "The challenge, however, lies in that gene expression trajectories for individual cells cannot be tracked over time since cells die once their gene expression is read.". I could not find anything in the present paper that directly addresses that challenge. Instead, it seems different cells at different time points are directly taken as a time series, which seems inaccurate. At the very least, the authors should make this assumption clear and motivate it.

C. Results.

1. Most of the results are given in the form of training curves which make rapid evaluation of the performance difficult. The scales of some subplot is sometimes off, such that the different methods cannot be distinguished.
2. I am pretty sure that RNN-ODE and GRU-ODE could also be used for this problem. I would encourage the authors to expand their list of baselines. I would also include very simple baselines like RNNs - or even one-step-ahead linear regressors.

### Questions
- Can you please address the concern regarding the destructive measurement process of scRNAseq ? It seems different cells at different time points are directly taken as a time series, which seems inaccurate.

- I didn't fully understand why the distribution of the latent is that important, given that you end up modulating it with a non-linear function for the final predictions. Could you please motivate this choice more rigorously ? Line 260 - Latent distributions.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
In this submission, the author propose a data-driven solution to Dynamic Flux Balance Analysis (DFBA), a classical tool from Systems Biology to analyze genome-scale metabolic network. At each timestep, DFBA solves a time-varying constrained optimization problem where the goal is to determine the value of the fluxes that lead to maximal biomass production, under time-varying biological constraints, which typically can only be brought by a  deep understanding of the system at hand.

Leveraging gene expression data in both control and knockout experiments thanks to single-cell flux estimation analysis, the authors aim at predicting time-resolved unseen gene expression, flux, balance, in both control and knockout experiments. This is achieved by means of Neural ODE processes (NODEP). Particularly, the main contribution of the paper is to cast DFBA in the framework of NODEP, and to highlight the need for a modification of NODEP to better handle the 1) irregularly sampled data and 2) non-gaussianity of certain distributions involved. This leads to Structural NODEP (SNODEP).

Finally, the authors carry a number of experiments on different metabolic pathways, demonstrating the clear improvement provided by SNODEP, particularly for sparsely sampled data across time.

### Strengths
- The paper is well-organized and well-motivated by a biological question.

- The empirical assessment clearly demonstrate the superiority of the proposed method.

### Weaknesses
 - There is little to no technical novelty. The paper feels like the application of Neural ODE processes to DFBA, with minor tweaks to make it work better. Although the results are convincing, and there is definitely value in framing the DFBA problem in terms of Neural ODE processes, I am not sure that ICLR is a relevant venue for this work.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
1
