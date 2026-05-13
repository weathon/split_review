# Discovering Mixtures of Structural Causal Models from Time Series Data

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Discovering causal relationships from time series data is significant in fields such as finance, climate science, and neuroscience. However,  contemporary techniques rely on the simplifying assumption that data originates from the same causal model, while in practice, data is heterogeneous and can stem from different causal models. In this work, we relax this assumption and perform causal discovery from time series data originating from \textit{a mixture of causal models}. We propose a general variational inference-based framework called \ours{} to infer the underlying causal models as well as the mixing probability of each sample. 
 Our approach employs an end-to-end training process that maximizes an evidence-lower bound for the data likelihood. We present two variants: \ourslinear{} for linear relationships and independent noise, and \oursnonlinear{} for nonlinear causal relationships and history-dependent noise. We demonstrate that our method surpasses state-of-the-art benchmarks in causal discovery tasks through extensive experimentation on synthetic and real-world datasets, particularly when the data emanates from diverse underlying causal graphs. Theoretically, we prove the identifiability of such a model under some mild assumptions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose a variational inference adopted for causal discovery in time-series data; in particular for mixtures of multiple causal graphs.

### Strengths
- in general, exposition is good (although there is room for clarity and explanations in formal parts ).
- addressing  mixture of multiple-causal graph  discovery is an interesting/relevant direction of research, that hasn't been much investigated (although I have my reservations)
- experimental results are coupled with a theoretical structural identifiability result.

### Weaknesses
 - my main skepticism is due to the fact that all the results are for the training set, which I am surprised (and had a stronger positive impression until that point). Trivial enough: For an unquestionable positive score, I would rather need result on test data, on unseen graphs. 

-   How different the causal graphs in these mixture models (and also the data i.e., average SHD within the cluster is missing.  This is really important to really understand what is going on behaviour of the method. (hence, my question). No surprise to see its effect on highly-imbalanced one.

- on minor point,  an illustrative toy example is lacking would be very useful.

### Questions
-  What is the effect of the distance between causal graphs to the performance?

-  g_1 and g_2 are not defined in Theorem 1, is it a typo: should be h? or a particular graph?

### Soundness
3 good

### Presentation
3 good

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
This work presents a method that infers causal relationships from time-series data by allowing for mixtures of different causal models, rather than assuming a single underlying causal model. The authors utilize end-to-end variational inference to optimize parameters and perform inference on causal graphs, functional equations, and sample membership within mixture components. The method is assessed on both synthetic and real-world datasets, showcasing competitive performance on training data in causal discovery tasks. The authors establish the identifiability of the proposed model under mild assumptions.

### Strengths
The paper addresses a relevant and interesting aspect of causal discovery in time-series data.

The proposed loss function is a simple extension of the standard variational inference objective, enabling efficient end-to-end training with a mixture of core causal discovery models.

The method is flexible in terms of the choice of core causal structure learning algorithms, inheriting the structural identifiability properties of these algorithms.

Competitive empirical results (although on training data) are reported across various metrics.

### Weaknesses
The proposed objective function can be seen as a straightforward extension of the standard variational inference optimisation framework. Therefore, the overall novelty and significance of the work may be somewhat limited in this regard.

A major drawback of the work is that the reported results are based on training data, as the proposed method depends on learnable sample-specific parameters. It raises questions about why an encoder producing a K-way categorical random variable given a sample was not considered by the authors. This approach would allow for a more direct probabilistic interpretation of sample assignments to mixture components, rather than relying on deterministic, sample-specific parameters.

The lack of reported results on generalisation limits insight into the proposed method's ability to perform beyond the training data. Specifically, it is unclear how the method would perform on unseen data drawn from the same underlying mixture of causal models, which is a crucial aspect for assessing the practical utility of the approach.

Although the method claims flexibility in terms of core causal structure learning algorithms, performance is only demonstrated based on one causal discovery method. This limits the assessment of the method's general applicability and its potential benefits when combined with other causal structure learning techniques.

### Questions
Can you please clarify how the AUROC metric is computed for the different methods being compared?

Regarding the experiment on Netsim-permuted data, wouldn’t one expect the results of the proposed method to be inherently favorable compared to non-mixture alternatives? This is because by permuting the variables, we intentionally manipulate the data to explicitly align with the underlying assumption of a mixture model.

What specific hyper-parameter value K was chosen for the DREAM3 Gene Network experiment?

### Soundness
2 fair

### Presentation
3 good

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
An ELBO method is introduced for finding and assigning weight to component SEMs in a mixture and drawing causal inferences from this mixture.

### Strengths
The problem of identifying the different SCMs in a mixture model where each mixed dataset uses a different graph and parameterization is extremely important, so I’m glad it’s being addressed.

### Weaknesses
I do have some issues.

1.	If we turn to the experimental section of the paper, we get two examples: one for NetSim (which I’m very familiar with) and another for the DREAM3 gene network. Both of these have problems with respect to the goal of this paper, suggesting that the choice of experimental datasets could be improved.

2.	The problem with the NetSim data is that it’s not an extremely convincing time series, as the records in the simulation are spaced far enough apart in time to render the data nearly i.i.d. In fact, analyzing it as i.i.d. often yields better results than analyzing it as time series, frustratingly, as in this paper:

Multi-subject search correctly identifies causal connections and most causal directions in the DCM models of the Smith et al. simulation study. NeuroImage, 58(3), 838-848.

This paper also treats the distributions as a mixture, though doesn't assume non-i.i.d.

3.	As a result, it seems that any study proposing a time series analysis of this data should do a comparison of this result to one obtained by treating the data as i.i.d. instead, since this is a known phenomenon for this particular dataset. This is an issue because the proposed method is specifically designed to deal with time series.

4.	The problem with the DREAM3 examples is that none of the reported results have any lift with AUC; they’re all stuck around 0.5, which is more or less random. The differences between the methods are slight. This result doesn’t give a case where the proposed method is particularly helpful.

### Questions
Can you find better examples to show the usefulness of the theory?

Where can the theory really shine so far as the empirical application is concerned? Where can it be expected to do significantly better than alternative methods?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed an approach to perform causal discovery from time series data originating from mixtures of different causal models. This approach can simultaneously infer the underlying causal graphs and the posterior likelihood of each sample belonging to a specific mixture component by maximizing the evidence lower bound, on top of the framework of the Rhino algorithm.

### Strengths
1. The problem setting is interesting, and the approach holds potential for broad applicability.
2. The authors conduct extensive experiments on simulated and two real-world datasets, compared with several baselines.
3. The authors characterize a sufficient condition for the identifiability of such mixture models and explain the relationship between the constructed evidence lower bound and the data likelihood.
4. The authors provide ablation studies.

### Weaknesses
1. Certain notations and explanations remain unclear, and these will be described in the upcoming Questions section.
2. Some details concerning the comparison between the proposed method and baseline algorithms in the experiments are perplexing, and these questions will also be raised in the later section.
3. The baselines used in the paper are not algorithms designed for multiple DAGs and mixture SCMs. Even though the authors mentioned other algorithms designed for multiple DAGs, none has been applied in the comparison.

### Questions
**1. Notations and explanations**

1.1 The SCM described in equation (1) differs from equation (6) and also the equation below equation (6); which one is correct? Do you assume additive noise?

1.2 In Theorem 1 equation (*), what is the definition of $a_i$? Does it mean one sample from $i$th SCM?

1.3 In Theorem 1, what are $g_1$ and $g_2$? Should they be $h_1$ and $h_2$?

1.4 As mentioned in the main paper, "This highlights the idea that learning a mixture model is only beneficial when the underlying SCMs differ from one another significantly. " could you clarify what the significant difference is here?

**2. Details in the experiment**

2.1 In the experiment section, "(per sample) indicates that the baseline predicts one graph per sample." how to apply the algorithm with only one sample? For example, PCMCI$^{+}$ needs CI tests, and CI tests need a set of samples instead of only one sample.

2.2 In the experiment performance section, AUROC and F1 are used as metrics. However, it is not mentioned which kind of AUROC and F1 refer to adjacency or orientation AUROC/F1?

2.3 As far as I know, the Rhino algorithm is not designed for heterogeneous time series data. In the experimental section, would it be feasible to compare the proposed algorithm with "Rhino (grouped)" as well? This would involve applying the Rhino algorithm to the grouped data based on the true underlying causal graph. Considering this, the results regarding Rhino in Figures 3 and 6 could be more comprehensive if grouped data were utilized.

2.4 Could the post-processing of PCMCI$^{+}$ outputs potentially affect the AUROC/F1 scores of PCMCI$^{+}$? If it does, would this influence tend to favor the proposed method in the comparison results?

2.5 In the synthetic data experiment, the metrics are averaged across 3 runs. Does each run requires a newly generated synthetic dataset? Personally, 3 runs seem to be a limited number for comprehensive evaluation.

2.6 In Figure 3, it seems a little strange that the performance of PCMCI$^{+}$ (grouped) is better with $D=10$ than with $D=5$. The same phenomenon happened in other algorithms. Do you have any clue on why this happened?

2.7 In Figure 4, "The accuracy is averaged across 3 runs and across data dimensionality D = 5, 10, 20.", is it more appropriate to plot the results for $D=5,10,20$ separately as the value of $D$ could affect the accuracy? Again, 3 runs seem limited to me.

2.8 Could you explain more about "The clustering accuracy and performance metrics show high standard deviation when K is set to the true number of mixture components K* = 10." which is stated in the appendix and explain more about the "buffers" when $K>K^{*}$?

**3. Other questions**

3.1 Why maximizing ELBO is equivalent to maximizing or minimizing each term separately in the log-likelihood in terms of $\theta, \phi$, and $\psi$ as $\phi$ and $\psi$ appear together in the second term?

3.2 Is it better to mention the Rhino algorithm in the related work section and briefly explain how it works as the proposed algorithm is built on top of Rhino?

3.3 Is it essential to verify whether the data satisfies condition (*) to ensure the reliability of the results? If so, how to verify this?

3.4 The paper mentions that people can also infer functional equations through the proposed model. Could you help me locate the related outputs in the experiment section? Does this mean the causal effect?

3.5 Has any code been provided?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
