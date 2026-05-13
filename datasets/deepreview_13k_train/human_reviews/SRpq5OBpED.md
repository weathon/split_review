# Meta-Dynamical State Space Models for Integrative Neural Data Analysis

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Learning shared structure across environments facilitates rapid learning and adaptive behavior in neural systems.
This has been widely demonstrated and applied in machine learning to train models that are capable of generalizing to novel settings.
However, there has been limited work exploiting the shared structure in neural activity during similar tasks for learning latent dynamics from neural recordings. 
Existing approaches are designed to infer dynamics from a single dataset and cannot be readily adapted to account for statistical heterogeneities across recordings. 
In this work, we hypothesize that similar tasks admit a corresponding family of related solutions and propose a novel approach for meta-learning this solution space from task-related neural activity of trained animals. 
Specifically, we capture the variabilities across recordings on a low-dimensional manifold which concisely parametrizes this family of dynamics, thereby facilitating rapid learning of latent dynamics given new recordings.
We demonstrate the efficacy of our approach on few-shot reconstruction and forecasting of synthetic dynamical systems, and neural recordings from the motor cortex during different arm reaching tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The proposed meta-learning framework for analyzing neural dynamics across diverse datasets that have shared underlying structure. By encoding dataset-specific variations in a low-dimensional embedding space and conditioning a shared dynamical model on this embedding, it allows for the integration of heterogeneous neural recordings. However, it's essential to consider the model's limitations, such as its dependence on shared dynamics, semi-large-scale pre-training data, and its lack of systematic benchmarking. However, overall, the proposed meta-learning framework presents a promising new direction for neural data analysis.

### Strengths
*   **Integration of Multi-Session Neural Recordings:** The proposed framework effectively addresses the challenges of integrating (potentially heterogeneous) neural recordings. It achieves this through a parameterization of latent dynamics using a low-dimensional dynamical embedding to capture variations across datasets. While they are not the first report to do so, it is an important direction/application.
*   **Learning a Shared Dynamical Structure:** The model learns a shared dynamical structure across diverse datasets, which is adapted based on the specific characteristics of each dataset. 
*   **Rapid Adaptation to New Data:** The proposed method demonstrates good performance in few-shot learning scenarios, where it can rapidly adapt to new recordings with limited training data. This is particularly valuable in neuroscience research, where collecting large amounts of data can be time-consuming and expensive. The ability to learn from small datasets expands the applicability of the framework and makes it suitable for a wider range of experimental paradigms.
*   **Generalizability:** The framework shows promising results in generalizing to new datasets, as evidenced by its performance on held-out data from both synthetic and motor cortex recordings. By learning a manifold of dynamical embeddings, the model is able to capture the variations in dynamics across different recordings and leverage this knowledge to adapt to new, unseen data.

### Weaknesses
 **Missing Benchmarks & Issues in Related Works** 

- There are some inaccurate statements in the introduction; for example, "CEBRA (Schneider et al., 2023) and CS-VAE (Yi et al., 2022) extract latent representations but do not learn underlying dynamics." Schneider et al. specifically learn the underlying dynamics rather than a priori prescribing them, as other algorithms do (e.g., SIDS, LFADS). CS-VAE assumes the same shared underlying dynamics and uses witching linear dynamical systems (SLDS) to discover them (and the authors should update their citation to: https://elifesciences.org/reviewed-preprints/88602.  Furthermore, the core issue is that the authors are conflating learning latent representations with learning the parameters of a dynamical system. While the authors' method does both, it is not clear that their specific method for learning latents is superior to other methods, and this should be benchmarked. The authors should clarify the distinction between learning the latent space and learning the dynamics, and why their approach is the only way to do both.


- Furthermore, this paper does not provide any benchmarking against models that they themselves acknowledge have the same goal: to create robust encoders across multiple datasets for downstream tasks (e.g., decoding). Therefore, they should report their results in comparison to Ye et al., 2023; Zhang et al., 2023; Caro et al., 2024; Azabou et al., 2024; & Schneider et al., 2023 (which they also fail to cite, but which showed joint training of an encoder rapidly adaptable to unseen data).


 **Dependence on Large-Scale Pretraining Data, and Only Within One Neural Domain:** 
- The effectiveness of the proposed framework depends on the availability of large-scale pretraining data. The sources show that models trained on smaller datasets tend to learn specialized solutions that may not generalize well to new recordings. Moreover, they only test on limited motor cortex settings, vs. more complex settings such as vision decoding. The authors should also clarify what they mean by 'rapid' adaptation, as there is no information on the time to run their method.

 **Accurate Embedding Inference:** 

- The model's generalization ability hinges on accurate inference of the dynamical embedding for a new dataset. If the embedding is not accurately inferred, the model's performance on downstream tasks can be significantly compromised. Showing how corrupted/noisy data, and in other domains (see above) affects the utility of the algorithm will be important for adoption in neuroscience.

**Assumptions of Shared Structure:** 
- The current framework assumes that there is a shared structure across the related tasks being analyzed. This assumption might not hold true in all cases, particularly when dealing with recordings from very different brain regions or unrelated behaviors. Future work may need to explore ways to incorporate modularity or other mechanisms to accommodate datasets without expected shared structures. The authors should comment on this. Furthermore, the motor cortex data used is from highly similar tasks across all subjects, which limits the generalizability of the findings.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

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
This paper tackles the problem of analysis across different animals, tasks, and recordings by introducing an unsupervised and dataset-hierarchical model of neural time series data. Their model class seeks to characterize a unified latent space over dynamical structures, which the authors claim has advantages for both inference efficiency and interpretability.  The authors propose different simplifications or ablations to their model class as baselines, showcasing the usefulness of the full interaction between the components. The authors investigate a synthetic example to show recovery performance and provide intuition for the shortcomings of typical approaches. Finally, they analyze recordings in the motor cortex of monkeys performing reaching tasks, highlighting the common dynamics across recordings.

### Strengths
- The paper is well-motivated. The introduction frames the paper well by highlighting surrounding literature and results on shared structure across subjects/tasks in task-trained models. Then section 2 provides a compelling example of the limitations of a shared latent dynamics model, with dataset-specificity only in the emission likelihood. 
- The paper is generally well-written. 
- The synthetic results are strong and form a cohesive story with Section 2
- The motor cortex recording analysis is extensive, analyzing two different tasks, and provides compelling results. In particular, assessing the variability in dynamics across different stimuli and further showing how this variability itself varies between tasks showcases the model's fit. Finally, interpolation in an embedding space (Figure 7) that encompasses both tasks showcases the model's use for interpretability generally.

### Weaknesses
While the authors do explore ablations and specific perspectives on their own model class, a comparison to other models is missing. There are two fronts to this comparison:
- **Theoretical and modeling connections**, investigating how their SSM relates to known models. Can you cast known models as special cases of yours? For instance the shared dynamics motifs (Driscoll et al, 2024), how would they best fit within this framework? Alternatively, the embedding analysis of (Cotler et al., 2023), how would it fare on SOTA unsupervised models of neural activity compared to your analysis directly on the data? It is unclear how the proposed model relates to existing methods for learning shared dynamics, and a more thorough analysis of the theoretical underpinnings is necessary.
- **Empirical comparisons**, implementing the other models mentioned in Section 4 using the way they would typically handle the variability across datasets (such as inputs or indicator variables). The lack of direct comparison to existing methods makes it difficult to assess the true performance of the proposed approach. Specifically, it is unclear how the method would compare to models that use indicator variables or other techniques to handle variability across datasets.

Medium:
- Figures 3 and 4 lack detail on how they were generated, specifically as to which parameters (/embedding values $e^i$) are being used. It is not clear what specific parameters are being visualized, making it difficult to interpret the results. For example, are these visualizations based on the mean embedding, or specific embeddings for each dataset? The lack of detail makes it difficult to assess the validity of the visualizations.
- Section 3.1. takes unnecessary turns in presenting the hierarchical model in my opinion. It starts with eq (3) with $\theta^i = \theta + \epsilon_i$, and but then discards this model (due to dimensionality of $\epsilon_i$) in favor of eq. (8) with $e^i \sim p(e)$, only to come back in eq. (11) to a form $\theta^i = \theta + h(e^i)$. I believe a more streamlined exposition could help the reader, going from eq (3) to eq (8) directly in some fashion. The current presentation is confusing and makes it difficult to understand the core ideas of the model.

Minor (/typos):
- L131, "we model the likelihood as a linear function of $z_t$": the mean of the likelihood is an affine model (from the $+D$), but the likelihood function/distribution itself is not "linear". The wording is imprecise and should be corrected to reflect the affine nature of the mean.
- Eq (5), $\phi^i$ undefined. I gather from L205 that each $\phi^i$ is learned independently  -- I would clarify this aspect. The lack of a clear definition makes it difficult to understand the model's structure and how the parameters are learned.
- L155: I am unsure about the use of the term "inductive bias". $\theta$ and $\epsilon_i$ capture shared and dataset-specific structure *by construction* -- I see the "bias" here as referring to how dynamical structures are similar to a mean structure with $\theta$. The term 'inductive bias' is not accurately used here, as the model's structure is a direct consequence of the parameterization, not an external constraint.
- Eq. (14) and surrounding (and further, L347), $d_r$ and $r$ are used interchangeably

### Questions
- How does the read-in network $\Omega$ handle different data dimensionalities?
- A readout matrix $C^i \sim \mathcal{N}(0,0.01)$ is highly contractive. What effect does that have on the model, does it not induce degeneracy?
- What are the color schemes in Figures 3A and 4A? How are these figures generated? 
- Why did the linear adapter and Embedding-Input methods get worse as $n_s$ increased in Table 1? Is this from a similar intuition as high M in Section 2?

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
3

### Summary
The authors present a method for learning the dynamics of neural data across individuals and tasks. Due to the heterogeneity of neural data (e.g. different neurons are recorded across different days, and of course across different subjects) much of the work in inferring dynamics from neural data has focused on single-session models. This limits the ability to train large models with lots of data, and to directly compare dynamics across individuals/sessions. The authors propose a state space model approach that learns a single set of shared latent dynamics, as well as session-level embedding that modifies the shared dynamics. They demonstrate the efficacy of their method on simulated data, and then apply it to real-world neural recordings from monkeys.

### Strengths
The paper addresses a long-standing problem in the field of neural data analysis, and one that will only become more pronounced as data collection methods improve. The approach is novel and well-motivated, and provides a tool for not only nicely reconstructing neural dynamics but also providing interpretable model components that will be crucial for scientific understanding. Additionally, the paper is well-written.

The proof of concept presented in figs 2+3 is extremely helpful for introducting the problem, and much appreciated.

The analysis of the synthetic data in sec 5.1 is also well-designed and instructive.

The real neural data is a well-chosen dataset that balances real world heterogeneity and simplicity for exploring model performance and behavior.

### Weaknesses
While the authors generally do a great job keeping track of all the notation, I find myself confused about how different trials are handled. It seems that trial averages over, say, certain reach directions are being modeled, rather than individual trials (perhaps I missed this somewhere). But how, then, are the different conditions handled in the notation y_{1:T}^{1:M}? I became confused about this in section 3.2 regarding the read-in network and the dynamical embeddings. Is there a single dynamical embedding per session, or per session-condition? If the former, does this require concatenating data across all conditions? Please clarify. [related, in sec 5.2, are test _trials_ left out, or test _conditions_?]

Fig 5B is difficult to interpret; some more annotations or a clearer caption would be appreciated.

The authors cite large-scale training of models as a motivation for their work, but there are no results that directly demonstrate how adding more data improves performance - the only results here are single session models vs the "all sessions" model. It would be interesting to see some of the metrics computed as a function of the number of sessions used for training the model (and then, for example, testing few-shot performance on held-out sessions/subjects).

### Questions
minor comments:
- L390, "Fig" missing before 17?
- would be helpful to show the true dynamics in fig 12

### Soundness
4

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
4

### Summary
This work proposes a new model class for learning shared sets of latent neural dynamics across heterogeneous data sets. While a number of recent papers have demonstrated empiricially that such population dynamics may be shared across tasks or even species, differences in number of neurons, individual behaviors, etc. present an obstacle to learning a shared model from which inferences might be drawn. The solution in this work involves learning a dataset-specific embedding vector used to parameterize low-rank updates to the weight matrices of state space models. These embedding vectors then parameterize differences across sessions, tasks, and individuals.

The paper is clearly written, and the problem is a timely one for the field. The experiments are thoughtfully chosen and give good insights, though some aspects (data type, model comparisons) are a bit limited. In all, a good paper that's above the bar for acceptance in my view.

### Strengths
- Methods for combining insights across datasets are a huge priority in neuroscience. 
- The model builds on several well-understood components and proposes a sensible ansatz for how embeddings alter to underlying system dynamics. 
- Multiple experiments carefully examine several key variables, including data set size, look-ahead prediction, and number of training trials. These are all clearly presented.

### Weaknesses
 - The model makes a number of design choices that are unclearly or incompletely motivated. For instance: does the dynamical VAE matter? Should one use the Bowman et al. inference scheme or the SMC-based autoencoder models of [1, 2, 3]? What about the bidirectional RNNs for $\mu_\alpha$ and $\sigma^2_\alpha$? One can't ablate everything, but it would be good to know how much conclusions depend on these choices.
- Related but distinct: The experimental comparisons are done for alternative approaches to learning the embeddings, but there aren't really comparisons with other models. At least one of the metrics tabulated is $k$-step ahead $R^2$, which could surely be compared with LFADS on single-session data or POYO [4] on multi-session data. I recognize that this paper has goals in addition to pure prediction, but since the authors do consider that metric, it would be good to see how the model proposed here compares to other predictive models. Likewise, it would be good to know how to assess (other than qualitatively) what constitutes a "good" learned latent space in the absence of ground truth.

### Questions
- There are some experiments to demonstrate that the parameterized low-rank embeddings outperform linear adapters or using embeddings as inputs, and these are convincing, but the intuition supplied for this is pretty terse. Why should one expect interference in these cases? Why does the rank-1 update protect against this?
- Figure 1: It would be helpful if panel B (or some other panel) could include $\Omega$ and the inference networks proposed by the model. For generation, this seems fine, but that's only capturing half the model.
- Is there a ground truth for Figure 2? It's hard to judge what one _should_ be looking for here.

### Soundness
4

### Presentation
3

### Contribution
3
