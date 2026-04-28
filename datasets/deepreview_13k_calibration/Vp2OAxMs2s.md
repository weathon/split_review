# Learning Interpretable Hierarchical Dynamical Systems Models from Time Series Data

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 8, 1, 8

## Abstract
In science, we are often interested in obtaining a generative model of the underlying system dynamics from observed time series. While powerful methods for dynamical systems reconstruction (DSR) exist when data come from a single domain, how to best integrate data from multiple dynamical regimes and leverage it for generalization is still an open question. This becomes particularly important when individual time series are short, and group-level information may help to fill in for gaps in single-domain data. At the same time, averaging is not an option in DSR, as it will wipe out crucial dynamical properties (e.g., limit cycles in one domain vs. chaos in another). Hence, a framework is needed that enables to efficiently harvest group-level (multi-domain) information while retaining all single-domain dynamical characteristics. Here we provide such a hierarchical approach and showcase it on popular DSR benchmarks, as well as on neuroscientific and medical time series.
In addition to faithful reconstruction of all individual dynamical regimes, our unsupervised methodology discovers common low-dimensional feature spaces in which datasets with similar dynamics cluster. The features spanning these spaces were further dynamically highly interpretable, surprisingly in often linear relation to control parameters that govern the dynamics of the underlying system. Finally, we illustrate transfer learning and generalization to new parameter regimes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the problem of analyzing multiple time series to extract the underlying dynamical properties that govern the observed data.  The authors propose hierarchical variant of the shallow PLRNN model which introduces group-level parameters in a subject latent space.  They propose a training scheme and implement/test the method on various experiments involving transfer learning and few-shot learning, comparing their method's performance with individual time series models and other models in the literature.  They also perform various analyses to showcase how their method is interpretable and uncovers ground-truth information about the underlying dynamics.

### Strengths
- This was a very nice paper to read, well-organized and well-written.  The authors included an extensive related works section to cover many developments related to their work.  In general, the presentation was quite clear, the figures were nicely formatted, and the experimental details were explained well.  
- The problem of extracting dynamical insights from many time series is a problem of both established and burgeoning interest across many fields -- particularly in scientific ones in which data is plentiful, yet we believe there are underlying laws that determine how the data is generated.  The ability to incorporate group-level information / multi-task learning into a model arguably has the potential to learn these dynamics better; it is exciting that the authors are able to show notable improvements in performance over individual-level models and some recently proposed other methods.
- I appreciate the authors' analyses to provide further insight into why their method is able to perform well.  It is one thing to obtain better numerical performance on a task; it is another to perform well for the right reasons.  The interpretability experiments are interesting because they convey that the model has been able to capture some knowledge of the underlying physics, which is something that one cares about in scientific applications.  
- The authors perform several experiments to showcase their method in different settings.  It appears that the method would have wide applicability to a range of different problems.
- The authors provide a link to their code and the code appears well-organized and a useful resource for the community.

### Weaknesses
 - The model development in a bit limited.  While the authors mention that their method is technically applicable to any DSR or TS model, they mainly focus on shPLRNN.  Their experiments focus on this one instantiation; it would be interesting to consider how the hierarchization could be applied to other models as well. It is not clear if the benefits observed are specific to shPLRNN or if they generalize to other architectures.
- The training method is also an amalgamation of many established techniques in the literature.  Though there is limited development of any one of these individual techniques, it should be noted that combining many ideas and getting things to "work" in practice is also a useful contribution. However, the paper could benefit from a more detailed discussion of the specific challenges in combining these techniques and how they were overcome, as well as a more thorough ablation study to understand the contribution of each component.

### Questions
- In Table 1, is there any sense of how your results vary as a function of T_max?  I'm wondering if there's a substantial regime of T_max (i.e. time series length) in which the group model performs much better than single time series models?  It would be interesting to see at what point performance between group/single becomes similar, if at all.  This could give practitioners a sense of what regimes the group model has an advantage over individual level models.
- As the authors mentioned in their literature review, there is a large body of work on sparse identification of nonlinear dynamics (i.e. Sindy) and physics-informed neural networks (PINNs) -- alternative approaches that have tackled some of the same datasets (e.g. Lorenz) as those used in this paper.  Is there a sense of how well your method compares against these other approaches in the literature (e.g. in an experiment such as Section 4.1)?

### Soundness
3

### Presentation
3

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
The paper presents a method for learning dynamical systems by leveraging information from multiple observations (referred to as ``subjects'') for scientific analysis. The authors achieve this by learning shared parameters across observations while preserving individual variability through a hierarchical model for time-series and dynamical systems reconstruction. They validate their approach using both synthetic data (e.g., Lorenz attractor) and real-world data (e.g., EEG), demonstrating that their method captures unique dynamical characteristics that other methods overlook.

### Strengths
I really enjoyed reading the paper and believe it addresses an important issue in computational neuroscience, where the data often includes multiple non-simultaneous observations across subjects. Moreover, the paper is well written, and the results clearly underscore the model's capability compared to other methods. They demonstrate their approach on multiple examples, including both synthetic and real-world datasets, under diverse settings.

### Weaknesses
# Critical:
1) While the paper was overall very well written, I believe that the Related Work (DSR section) missed discussion about DSR methods based on time-changing combinations of linear dynamical operators, including both  switching, e.g., [1], and decomposition [2] models. Specifically, the authors should discuss how their approach relates to methods that explicitly model transitions between different linear dynamical regimes, or those that decompose the dynamics into a set of latent components. These approaches offer alternative ways to capture non-stationarities and multi-faceted dynamics, and a discussion of their similarities and differences would strengthen the paper.
2) I also missed from the Related Work more methods that are designed or capable of leveraging multi-session information in neuroscience specifically, including both [3,4]. The authors should discuss how their method compares to techniques that explicitly model single-trial neural population dynamics using sequential autoencoders or methods that analyze cross-ensemble interactions in multi-view brain observations. These methods address similar challenges in neuroscience and should be acknowledged in the related work.
3) I think an important question that needs to be discussed is how many subjects you need for the method to succeed. For instance, if you have a total of $J$ subjects, what will happen if you leverage information from $J-1$ or$ J-2$? I would assume that performance will improve rapidly with low $J$ values and then level off as $J$ increases to higher numbers, potentially resembling a logarithmic function. It is crucial to understand the scaling behavior of the method with respect to the number of subjects, and this should be explored empirically or discussed theoretically.
4) A main concern of mine is the need for a discussion on the minimum overlap required between subjects in terms of dynamical modalities, channels, and time scales for the model to work effectively. While the authors show that different dynamical regimes can be modeled in synthetic data (e.g., through varying aspects of the Lorenz attractor under changing parameters), I assume that data from completely distinct dynamical processes—such as rapid interactions in neuropixels data combined with annual climate changes—or recordings from unrelated units even within the same field (e.g., neural activity from very different brain regions with zero overlap across subjects) might challenge the model’s effectiveness. I suspect there is a critical level of cross-subject similarity needed in both scales and channel identity for reliable performance. A complete benchmark may be impractical due to the sheer range of possibilities, but providing a list of mathematical assumptions or briefly addressing this in the discussion/limitations section would clarify these requirements. The authors should discuss the limitations of their approach when applied to datasets with minimal or no overlap in dynamical characteristics or measurement modalities.
5) The model requires a lot of hyperparameters. It is important to clarify which hyperparameters are critical for performance and how they should be tuned. A sensitivity analysis of the model's performance with respect to different hyperparameter settings would be beneficial.

# Minor but recommended:
1) Line 67: I believe an em dash (--- in LaTeX) should be used here instead of an en dash (-).
2) I would recommend that the authors more clearly state that the term `group` refers  to the observations from all subjects. Initially, I was unsure if `group` referred to some internal grouping within the data, so a brief clarification the first time you use it would help.
3) While I understand the page limit, it does not seem sensible to place the illustration figure (Fig. 7) in the supplementary materials. This figure is important for understanding the model, and the authors would want readers to see it. I suggest making it shorter and moving it to the main text.
4) Line 171-172: I suggest $P_{w_1} \in \ldots $ should be kept on a single line (i.e., by wrapping that formula in curly braces).
5) It is unclear how robust the method is to different model initializations. The authors should investigate the variability in the results across different random initializations and report the statistics of the performance.
6) The colormap in Fig. 4a seems off: the ticklabels do not align with the color change. I suggest using a legend with `Subject 1`, `Subject 2`, etc., instead of a colorbar, as that should be categorical, not sequential (unless Subject 1 is indeed more similar to Subject 2).

### Questions
1) Regarding Eq. 4, in line 296 you mentioned for the first time that it is piecewise-linear. Did you mean it is locally linear? Or are there full periods of linearity that switch between them (e.g., as in [1] from my Weaknesses text cell)? From equation 4 itself it just seems linear so  I would clarify it near the equation itself if that is the case.
2) Can you give some intuition for the meaning of the different $ P $s (e.g., $P_A$, etc.)? I would interpret them as capturing groups of features or parameters that operate together to link the latent and observed space.
3) In line 185, why did you choose to train the model directly on the observations  (i.e., the $x_t = z_t$ assumption)? What do you think will be the effect if a different approach is chosen?
4) When describing the batching, based on the notations, it seems that all samples start with the first time point (due to writing $x_1 \ldots $ in line 191). Is this correct, or is it a mistake and batches taken from some random $\tau$ to $\tau + {T_{\text{seq}}}$?
5)  What does `2X10` refer to in row 495? Do you mean 20 regions? How much overlap is there between them?
6)  How would you address temporal nonstationarities within your model?
7) What is the model's computational complexity? How does it increase with the number of subjects?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper presents a dynamical modeling approach for time series generative foundation models, focusing on scientific applications. The authors argue that a robust time series generative model requires both in-domain and cross-domain features, achieved through hierarchical dynamical systems. They frame the construction of such models as a dynamical system reconstruction (DSR) problem, training RNNs with low-dimensional task-specific and high-dimensional group-specific features. The method is supported by numerical experiments.

### Strengths
Overall, this paper might present a good idea, but it seems rushed, which affects the contribution of an otherwise very interesting work. Regardless of the final decision, I hope the authors find my comments helpful in further refining their draft.

* Important modeling problem for scientific AI/ML/Foundation Models

* The experiments are solid 

* Many ablation studies

### Weaknesses
 * **Clarity.** The language is overly complex and difficult to read. For example, in lines `134-145`, the authors use 10 lines for just 3 sentences, making the paragraph hard to follow. I had to read Sec 3.1 multiple times and still found it difficult to understand.

* **Novelty.** The proposal lacks clear motivation and feels too straightforward to be considered novel. Most components are derived from existing work (e.g., General Teacher Forcing, PLRNN, shPLRNN).

* **Practicality.** The model's parameterization is overly complex (e.g., passing learnable parameters to the next layer), raising concerns about its feasibility for end-to-end training and practical use as a time series generative model.

* **Significance.** The significance is difficult to gauge due to limited clarity. Overall, it seems lacking, given the assembly-like nature of the approach.

### Questions
* Why Eqn 3 is mathematically tractable?

* Why does this tractability matter? It seems only loosely connected to the task of interest (e.g., certain physical systems' ODEs).

* Could you test your proposal on common time series tasks? For example, multivariate time series datasets commonly used in forecasting literature, such as traffic, electricity, exchange rates, etc. If not, could you provide some justification? As mentioned in your conclusion:
  > Unlike TS models, where the interest lies mainly in forecasting or TS classification/regression, in DSR we aim for generative models that capture invariants of the true
 
  Why wouldn’t these common forecasting tasks contain such "invariants of the truth"?

* This paper reminds me of an ICML 2023 paper: https://arxiv.org/abs/2306.06252. While the scope is different (they focus on feature extraction of time series by assuming the underlying dynamical system is a dynamical Ising model), they also attempt to interpret general time series through a dynamical systems lens. While the exact relevance is unclear, treating TS modeling as a dynamical system is not new. I am sure there are other works in this direction. It would be valuable to discuss more related literature in the ML community.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce a general theoretical problem: reconstructing a set of dynamical systems, given short observations of each system with different underlying parameters. The authors map this problem onto problems frequently arising in biophysics and neuroscience, in which one needs to train a joint model with subject-specific attributes. The authors introduce a hierarchization scheme for training recurrent neural networks, that disentangles low-dimensional subject-specific features from the general features of a shared dynamical systems model. The authors apply their approach first to synthetic dynamical systems tasks, then to an arterial pulse dataset, and finally to EEG and fMRI datasets. Beyond strongly outperforming baselines and ablations, the authors show that their approach extracts predictive dynamical features that can be used for interpretability, or even for subject classification.

### Strengths
This paper is very clear, thorough, and well-motivated. I think this paper clearly exceeds the acceptance bar for the conference.

+ The Introduction and Related Work sections are comprehensive and concise. The authors cover standard references for SciML (Koopman/PINN/neural ODE/RC), but they also highlight several hihgly-relevant but lesser-known methods, including recent works that focus specifically on reconstructing invariant measures of dynamical systems.

+ The baseline models chosen are reasonable and appropriate points of comparison. The authors include an explicit ablation of the hierarchical portion of their model

+ The two application tasks (EEG and fMRI) are important and provide clear motivation for this approach, which has an inductive bias for datasets with discrete subjects. Framing subject-level clinical data as analogous to training a joint model on copies of a dynamical system with different parameters is a very conceptually-rich approach.

+ There are lots of novel details, which show that the authors have thought very deeply about their applications. For example, the covariance-scaled MSE (Eq. 5) helps account for clinical batch effects. 

+ The arterial pulse dataset is an excellent demonstration, showing that the model successfully finds a low-dimensional description of an otherwise complex and high-dimensional simulation. The regression showing that the fitted model predicts the haemodynamic parameters is a great demonstration of the interpretability of the learned features.

### Weaknesses
I’ve assigned a high score because I think this paper clearly meets standards of novelty, rigor, and interest for the conference. However, I have a few general concerns, which the authors might consider in order to attract a wider audience to their work:

+ The description of the training method itself could be expanded. I understand the architecture, and the use of a low-dimensional subject vector that linearly decodes into the high-dimensional weight vectors of the RNN. However, I do not understand the mechanics of how the subject-specific vectors are found and P matrices are trained. I understand that once we have the W matrices, then we can use generalized teacher forcing; it’s the step before that where I am unclear. I see this hierarchical training scheme as one of the main contributions of the paper, and so clarifying this is essential.

+ The shPLRN model is well-motivated for this problem and has been characterized extensively in prior work. However, I do perceive it as a bit of a specialized model, compared to more common approaches to DSR like PINNs or even SINDY. An example of the hierarchization scheme, which is general, used on one of these more common DSR approaches would be an interesting baseline (LEADS, a baseline currently included in the manuscript, is essentially this for neural ODEs).

My concern is that I perceive the primary contribution of this paper to be getting the hierarchization scheme, including the training approach (which may be hard to adapt to models that can’t be trained with teacher forcing). The other novelty is the choice of datasets and demonstrations, which are all interesting and strong. However, the current paper mixes these contribution with a specialized architecture from prior work, shPLRNN, making it hard to disentangle the contributions. My concern is that readers who encounter this paper will incorrectly think that the architecture itself is the main contribution, rather than the problem setup and training scheme.

### Questions
+ Eq. 5 — can you please clarify how this is used in the training loop? How and when is \Sigma updated? Generally I would prefer some more detail here.

+ Can you provide more description of how the Hierarchical training scheme works?

### Soundness
4

### Presentation
3

### Contribution
4
