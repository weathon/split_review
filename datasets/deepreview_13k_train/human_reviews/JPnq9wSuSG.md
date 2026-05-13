# Adaptive Causal Experimental Design: Amortizing Sequential Bayesian Experimental Design for Causal Models

- Decision: Reject
- Scores: 6, 3, 5, 6, 5

## Abstract
Interventions are essential for causal discovery and causal reasoning. Acquiring interventional data, however, is often costly, especially in real-world systems.
A careful experimental design can therefore bring substantial savings. 
In the sequential experimental design setting, 
most existing approaches seek the best 
interventions in a greedy (myopic) manner that does not account for the synergy from the yet-to-come future experiments. We propose Adaptive Causal Experimental Design (ACED),
a novel Bayesian sequential design framework for learning a design policy capable of generating non-myopic interventions that incorporate the effect on future experiments.
In particular, ACED maximizes the Expected Information Gain (EIG) on flexible choices of causal quantities of interest (e.g., causal structure, specific causal effects) directly, bypassing the need for computing intermediate posteriors in the experimental sequence.
Leveraging a variational lower bound estimator for the EIG, ACED trains an amortized policy network that can be executed rapidly during deployment. 
We present numerical results demonstrating ACED's effectiveness on synthetic datasets with both linear and nonlinear structural causal models, as well as on in-silico single-cell gene expression datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Adaptive Causal Experimental Design (ACED) is an algorithm that chooses a sequence of experiments designed to maximize expected information gain (EIG) for a variety of different possible causal questions. In contrast to current algorithms, it is non-myopic (maximizes the EIG for a sequence of experiments rather than for the next experiment), is adaptive in real-time, and works on a variety of different causal questions, including constructing causal graphs and calculating the effects of interventions. It uses variational methods to lower bound the EIG for a given policy. Experiments indicates that the runtime of ACED is much faster than various other state of the art experimental design algorithms, and is more accurate in SHD and F1 score on reconstructing graphs in linear Gaussian models.

### Strengths
The strengths of the article are that it describes an algorithm that has major advantages over existing algorithms.
1. It is non-myopic.
2. It is real-time adaptive.
3. It is flexible which causal questions it can answer. l
4.It performs significantly better on SHD and F1 score in graph reconstruction on linear Gaussian data as the number of stages increases on simulated data.
5. It  performs significantly better on SHD and F1 score in graph reconstruction on two read Genetic Regulatory Networks.
6. It is much faster than alternative algorithms such as DiffCBED and SoftCBED.

### Weaknesses
1. A major advantage the authors claim for ACED is its speed. But they don't put their discussion of speed into the main body of the paper, even though there is room for it. In Figure 10, the X axis is deployment time, with no indication of what the units are. The Y axis is labelled variable dimensions. I am not sure what variable dimension refers to - number of variables? The ACED line has 0 variable dimensions for every Deployment time, while the diffBCED and Soft-BCED lines have variable dimension that start in the thousands and increase over Deployment time. The accompanying text say that this shows that ACED has significantly faster inference times, but it is hard to see exactly what the graph indicates or how it shows that ACED is faster. I am unclear about how many variables ACED can be applied to, and how long that would take
2. The differences between random choice of experiment and ACED are quite small in many of the non-linear cases, and in some cases even after a large number stages, the random experiment does better.
3. Points 1 and 2 raise the question of whether one would be better off using random experiments for large numbers of variables in non-linear cases.
4. The authors say that they took are to take care that the structural causal models that they generate are not identifiable from observational data. However, in the linear case, the data was generated with random noises all of which had equal variance. This is known to provide extra information and make the graph identifiable without doing any experiments. In the non-linear case they generated additive noise models, which are also known to be identifiable except in special circumstances (e.g. linear Gaussian.) See Zhang and Hyvaarinen in "On the Identifiability of the Post-Nonlinear Causal Model".
5. There are a number of minor issues that make the paper difficult to read:
   a. On line 187 p(M|D) is introduced with no explanation of what M is.
   b. Results are reported for two "realistic" data sets from yeast and E. coli. There is no description of these 
       data sets at all - how many variables, how dense the graphs were, what functions related parents to 
       children, etc., or in what sense they are "realistic".
   c. The paper does not define RELU, FFN.

### Questions
1. Where is the density of the simulated graphs specified? Without that, it is hard to tell how hard the problem is.
2. The authors make the following statement: "Although some baselines achieve a low E-SHD as the number of nodes increases, this is likely due to the posterior inference model DiBS converging to low-entropy solutions, which tend to predict only a few edges. When considering both E-SHD and F1-score, ACED outperforms the baselines significantly". E-SHD and F1-score are measuring very similar things and ought to be very highly correlated. Please explain how taking both into account would lead to a different conclusion than only taking E-SHD into account.
3. There are a number of different related ways of defining structural Hamming distance (for example how to treat a reversed edge.) Please specify more exactly how it was calculated.
4. In equations 3 and 4, h_t = {xi_{1:t}, x_{1:t}}. So I thought that would mean h_{t-1} =  {xi_{1:t-1}, x_{1:t-1}}. But then h_{1:t-1} also occurs in the equations. If h_{t-1} already contains all the information about xi and x from 1 to t-1, what is h_{1:t-1} add to h_{t-1}?
5. Could you expand the dicussion of the setup in 4.2?  What are n and d in Figure 2? Why is L = 4? A little more detail about what each part is doing would be helpful.
6. For the causal reasoning task, in the linear Figure 7 why not compare the estimated effects of the interventions directly, instead of log q? 
7. How were the number of stages chosen? Is that limited by how long each stage took? For the larger graphs it looks like doing more stages would be helpful.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents ACED (Adaptive Causal Experimental Design), a method for sequential experimental design in causal discovery using reinforcement learning. The approach trains a transformer-based policy network to select interventions that maximize expected information gain for causal queries. The method aims to be non-myopic, computationally efficient at deployment, and flexible for different causal queries.

### Strengths
* Good technical writing and presentation.
* The technical execution is solid.
* Interesting extension to handle specific causal queries beyond structure learning.
* Novel mutation of the AVICI architecture to handle multimodality.

### Weaknesses
 * Overlap with concurrent work (CAASL) that is not acknowledged or discussed, although cited. Please see next section for questions.

 The paper has significant overlap with CAASL (https://arxiv.org/abs/2405.16718v1) in several key aspects: Both use transformer-based policies with alternating attention and both train using RL (i understand this work is not branded as RL but it's a policy optimization method maximizing a reward based on AVICI model) to maximize information gain. Although ACED focuses also on causal queries beyond structure learning and uses a different variational approximations for the posterior, this work misses comparisson with CASSL (e.g. as a baseline) or a critical evaluation of the differences and the novelty. How does your work differ fundamentally from CAASL? Which components of your method are novel compared to CAASL?

 Also, you compare with CBED line of work which is not sequential but batch experimental design, the main difference being that during batch selection there is no for feedback and thus can't adjust for the new information. I would argue that this might not be the most fair comparisson but i'm keen to hear your views on this.

 In figure 4, the methods starting points have very large variance. I would expect for small number of steps (e.g. 2) to have relatively smaller differences. Do all methods use the same posterior model and hyperparameters during evaluation?

### Questions
The paper has significant overlap with CAASL (https://arxiv.org/abs/2405.16718v1) in several key aspects: Both use transformer-based policies with alternating attention and both train using RL (i understand this work is not branded as RL but it's a policy optimization method maximizing a reward based on AVICI model) to maximize information gain. Although ACED focuses also on causal queries beyond structure learning and uses a different variational approximations for the posterior, this work misses comparisson with CASSL (e.g. as a baseline) or a critical evaluation of the differences and the novelty. How does your work differ fundamentally from CAASL? Which components of your method are novel compared to CAASL?

Also, you compare with CBED line of work which is not sequential but batch experimental design, the main difference being that during batch selection there is no for feedback and thus can't adjust for the new information. I would argue that this might not be the most fair comparisson but i'm keen to hear your views on this.

In figure 4, the methods starting points have very large variance. I would expect for small number of steps (e.g. 2) to have relatively smaller differences. Do all methods use the same posterior model and hyperparameters during evaluation?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel approach called Adaptive Causal Experimental Design (ACED) for optimizing intervention selection in experimental design. The proposed framework generates non-myopic interventions, taking into account the effects on future experiments, unlike existing methods that optimize interventions in a greedy (myopic) manner via an offline policy network. ACED maximizes the Expected Information Gain (EIG) on causal quantities of interest, such as causal graph structure and specific causal effects, bypassing the need for intermediate posterior computations.

### Strengths
* Unlike previous methods, the proposed method uses the information from the history of experiments to select the best possible experiment for the next stage.
* The offline policy network significantly reduces the computational cost of the proposed framework during deployment.

### Weaknesses
 * The training costs (e.g. in terms of compute and number of required interventional data points) of the offline policy model are not accounted for in the paper. While it is true that the proposed method requires significantly less computational budget during deployment, these training costs should not be completely overlooked. Specifically, the paper lacks a thorough analysis of how the complexity of the causal graph (number of nodes and edges) impacts the training time and the amount of interventional data needed for the offline policy. This is a crucial factor when considering the practical applicability of the method, as the training phase could become prohibitively expensive for larger, more complex systems.
* The method does not seem to scale well with a larger number of nodes e.g. it is evident in Figures 8 and 9 that DiffCBED starts to outperform the proposed method on both E-SHD and F1 score as the number of nodes increases. This suggests a limitation in the method's ability to effectively explore the exponentially growing space of possible DAGs as the number of nodes increases. The reported performance degradation with increasing node count raises concerns about the method's scalability to real-world problems involving complex causal relationships. Furthermore, the paper does not provide a clear explanation for why the performance of ACED degrades with larger graphs, nor does it offer any mitigation strategies.

### Questions
1. As mentioned in the weaknesses, Figures 8 and 9 show that other baselines start to outperform the proposed method by a considerable margin as n increases in both graph types, as well as in both linear and nonlinear cases. Could you please elaborate on this?
2. How many steps and samples at each step ($n_{step}$ and $T$) are used for training the offline policy model?
3. How large is the policy network e.g. in terms of number of parameters?
4. Can you explain how the proposed method performs under changes and distribution shifts compared to online methods? This is particularly important in dynamical systems where the underlying mechanisms or noise may change over time.
5. It seems like "D" is missing on the LHS of Equations 5 and 6.
6. How are the prior P(G|D) and the likelihood defined?
7. Given that the experiments are only conducted on synthetic data, can you elaborate on how the method can be used/extended to semi-synthetic/real-world settings (e.g. [1])?

[1] Greenfield, Alex, et al. "DREAM4: Combining genetic and dynamic information to identify biological networks and dynamical models." PloS one 5.10 (2010): e13397.

### Soundness
2

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
The authors develop a sequential experimental design framework to pick intervention targets and values to learn a particular causal quantity under a fixed experimental budget. Their method aims to provide an experimental design that aims to (1) maximize the information gain after the entire experimental budget instead of greedily selecting interventions at each step, (2) allow estimating different causal quantities directly without having to learn intermediate quantities (e.g., the graph), and (3) be amortized, that is, having a low computational cost in selecting the next intervention after each experiment.

To produce a policy, the authors use a transformer-based architecture that is trained using data-generating processes sampled from the prior and repeated “simulated” runs of experiment sequences. During deployment, the network does not need to be retrained after obtaining the data from each experiment. The training objective is a variational lower bound on the expected information gain over the complete experimental budget. The authors provide a proof on the validity of this bound.

The authors evaluate their method on a collection of synthetic data: synthetic causal models with different underlying graphs and structural assignments, and simulations of gene expression mechanisms in E-Coli and Yeast.

### Strengths
- The paper takes an innovative approach to providing an amortized experiment selection policy.
- The experiment section provides experiments to back up some of the claims of the paper, providing different data-generating models and quantities of interest. However, it lacks details (see weaknesses)
- Besides some issues with grammar (see Questions section), the text is easy to follow
- The figures (e.g., 1 and 2) are informative and nicely complement the text

### Weaknesses
In my opinion, the main weakness of the paper is that there are few details on the experimental setup, which is exacerbated by not providing code or artifacts to reproduce the results. There is also no reproducibility statement.

At best, this makes it difficult to perform an in-depth analysis of the results. At worst, it gives the impression that the authors picked some settings that are excessively favorable to their method and are trying to hide this fact. This overshadows the otherwise valuable contribution of the paper. In my opinion negative results are also valuable, and as long as the methodology is comprehensive this is not grounds for rejection.

I am more than happy to raise my score if these issues are addressed— also, if I missed this information, please let me know!

Let me turn this into some actionable feedback:

- For figures 3,4,8,9:  I apologize if I missed this, but are these results on a single data-generating process (i.e., ground-truth SCM) or an average over many graphs? If the results are over only one graph: how was this graph chosen? If you ran several examples and picked the one with the best results, you should say this and provide the results for a few other random examples in the appendix. Showing statistics (e.g. mean results + error bars) over a large number of randomly sampled data-generating processes would be the most informative and dispel any suspicions.
- For the in-silico experiments with (E. Coli / Yeast). You say ACED achieves almost perfect performance, but you give no details about the experimental setup, except that you use a 10-node graph. There is also no reference to the datasets you used.
  - How did you generate the data? Giving details would dispel the suspicion that you are cherry-picking. It would be good to provide some details such as the source of the gene regulatory network structure, the type of noise model used (if there is one), and any preprocessing steps applied to the data. You should also make the datasets publicly available.
  - What is the experiment horizon? Sample size of each experiment?
- How did you train Algorithm 1 in the experiments? In particular,
  - What is the prior used to train the network in Algorithm 1? Is it the exact same prior as the one used to generate the data-generating processes in Appendix 8?
  - What is the number of training samples n_env? I can imagine that if this is extremely large, you are able to reasonably cover the prior space. I don’t see this as a drawback, but it would be interesting to understand how the performance of the method is affected by this parameter, as it would be useful for a practitioner to know that they can improve performance by simpling elongating the training stage! As an idea, an ablation study showing how different values of n_env affect the performance, could provide valuable practical insights.
- Line 314: “We present results for ER graphs in the linear SCM setting”. However, in the results in Appendix 10, on non-linear SCMs for ER graphs, ACED performs close or worse than the random policy. This should be clearly stated in the main text, instead of hidden behind “the prior is more informative for SF graphs” in line 364. Admitting “mixed results” is in my opinion totally OK, and should not be a reason for rejection.

### Questions
- Throughout, the authors have a tendency to omit articles (a / the) in front of words. Here are some examples (I stopped after a few, so maybe check the whole text):
  - Line 053: “suboptimality in learning full causal model…” -> “suboptimality in learning A full causal model…” (or make models plural)
  - Line 302: “For causal reasoning task” -> “For THE causal reasoning task” (or make tasks plural)
  - Line 431: “Considering uniform intervention on node 1” -> “Considering uniform interventionS…” or “Considering A uniform intervention…”
  - Line 986: “over graph” -> “over the graph”?
  - Line 964: “Scale-free graph is characterized…” -> “Scale-free graphS ARE charachterized” or “A scale-free graph is…”
- Some weird sentences / typos:
  - Line 304: “[...] NMC could be efficient for estimating the shifted EIG than NFs” -> perhaps this should be “more efficient”?
  - Line 484: “[...] on Erdos-Renyi with 10 nodes” -> “on AN Erdos-Renyi graph with 10 nodes”
  - Line 485: “mechanism” -> “mechanismS”
- The sentence in Line 431 is unclear:
  - The enumeration [-5,4,...5] is a bit weird. Did you mean [-5,-4,...5]?
  - Also, what do you mean with values [-5,4,...5]. Is it that the intervention value is sampled uniformly at random from this range?
- Some minor points:
  - Line 282: Reference to (Erdos & Renyi, 1959) is strangely formatted -> perhaps something is off with the bibliography entry?
  - Line 311: You repeat Erdos-Renyi twice
  - Line 283: “various node sizes” -> I assume you mean number of nodes?
  - References to figures are not consistent, i.e., sometimes you write figure and sometimes Figure (e.g., figure 7 in line 485)
  - Subfigures in Figure 1 are labelled with double parenthesis, e.g., ((a)). In line 086 this also results in a double parenthesis when referencing it, i.e., “(Figure 1(b))”. An idea is to simply write (Figure 1b).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores methods to enhance causal discovery and reasoning, especially when dealing with costly interventional data. The authors introduce Adaptive Causal Experimental Design (ACED), a new framework that aims to produce non-myopic (long-term beneficial) interventions. The goal is to maximize the Expected Information Gain (EIG) throughout a sequence of experiments rather than focusing solely on the immediate next experiment. ACED uses a policy network (leveraging a transformer-based architecture) to predict the most informative interventions. This policy is trained offline, allowing quick decision-making during actual deployment. The authors also texted ACED on both simulated datasets and real datasets.

### Strengths
1. The design of policy network is interesting
2. Some theoretical analysis is provided.

### Weaknesses
1. The notations are not consistent, which makes it hard to read. For example, in equation (3), (4), the notation of $h_t$ and $\xi$ are not consistent to definition in line147.
2. As far as I am concerned, the proposed model does not has constraint on DAG, which means it may result in cycles.
3. The authors show that the proposed model is optimizing EIG at each step with variational lower bound, however, there is no analysis on non-asymptotic convergence to the ground truth given enough interventional samples.
4. As the authors mentioned in the discussion section, the model is proposed to relive real world budgets such as time and cost. Some metric to demonstrate this could be more convincing. For example, compare the time of GRU experiments with ACED's policy network.
5. The authors compared ACED with 3 baselines including a random policy. I wonder if the authors could include some baseline that does not fall into the BOED category such as [1] which is also discussed in the related works section in the appendix.

### Questions
See weakness for major questions.
1. Is $Z$ independent to $\mathcal{D}$ given $G, \theta$?
2. Is $\theta$ independent to $G$?
3. I wonder if there is any justifications on the choose of the neural network architectures. For example, the ablation study on the hyper parameters of the transformers could be attached or any suggestion on the selection of parameters. Also, why normalizing flow is preferred?
4. The authors mentioned there could be bias in the EIG estimation in the discussion section. Could the authors elaborate more on how much the bias could aff5ect the model's performance?
5. The actual computation of posterior is replaced by $\pi$ in ACED. I wonder if the author can show the advantage of $\pi$ over actual computation of posteriors with an ablation study on simple simulated graphs?

### Soundness
3

### Presentation
2

### Contribution
2
