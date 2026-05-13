# Time-Dependent VAE for Building Latent Representations from Visual Neural Activity with Complex Dynamics

- Decision: Reject
- Scores: 3, 3, 6, 8

## Abstract
Seeking high-quality representations with latent variable models (LVMs) to reveal the intrinsic correlation between neural activity and behavior or sensory stimuli has attracted much interest. Most work has focused on analyzing motor neural activity that controls clear behavioral traces and has modeled neural temporal relationships in a way that does not conform to natural reality. For studies of visual brain regions, naturalistic visual stimuli are high-dimensional and time-dependent, making neural activity exhibit intricate dynamics. To cope with such conditions, we propose Time-Dependent Split VAE (TiDeSPL-VAE), a sequential LVM that decomposes visual neural activity into two latent representations while considering time dependence. We specify content latent representations corresponding to the component of neural activity driven by the current visual stimulus, and style latent representations corresponding to the neural dynamics influenced by the organism's internal state. To progressively generate the two latent representations over time, we introduce state factors to construct conditional distributions with time dependence and apply self-supervised contrastive learning to shape them. By this means, TiDeSPL-VAE can effectively analyze complex visual neural activity and model temporal relationships in a natural way. We compare our model with alternative approaches on synthetic data and neural data from the mouse visual cortex. The results show that our model not only yields the best decoding performance on naturalistic scenes/movies but also extracts explicit neural dynamics, demonstrating that it builds latent representations more relevant to visual stimuli.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
A latent variable model is described and used to reanalyze a publicly available dataset of population recordings in mouse visual cortex.
In particular, this work proposes a time series analysis of the neural dynamics in response to videos.
This method combines a variational auto-encoder loss and a self-supervised contrastive learning objective in the latent space.
The latent space is split into a static state and a dynamic state, and both evolve according to learned recurrent dynamics.

### Strengths
As large population recordings neural datasets are being measured, developing correspondingly flexible latent time series models is an important research direction.
This work proposes an architecture and unsupervised objective for discovering structure in such neural data.
The focus on neural dynamics in response to video input is timely and relevant.
The presentation begins with simple toy synthetic experiements and then builds to the analysis of a rich neural dataset.

### Weaknesses
The proposed architecture is quite complex and no clear justification is provided for the design of factorized latent states. Moreover the latent states are also swapped for the computation of the objective function. I see that these design choices are inherited from a previous publication, but I think that it would help the reader if you could explain clearly the reason for these choices. If a conceptual or mathematical explanation is not possible, ablation experiments could also help (e.g. with vs. without latent state factorization).
The current explanation is vague, e.g. line 231: "To enhance the effect of the positive sample, we adopt the practice of swapping content latent variables between the positive pairs while maintaining style latent variables."

The proposed objective function combines three terms: a VAE style ELBO, a weight decay regularizer, and a contrastive term.
Your reader will find it difficult to think about the overall objective: what is being optimized exactly?
Is this multi-objective optimization still amenable to an interpretation in terms of likelihood?
It seems like you are combining a generative and a disctiminative objective, I wonder if it may be possible to express all that in a nice unified and coherent Bayesian framework, rather than simply saying that you added many terms.
This is also important for the interpretation of the results, it would help clarify what each of these part is contributing and may also help selecting natural hyperparameters.
The writing is vague and should be clarified, for example:
line 74: "we apply self-supervised contrastive learning to enhance the time constraint and to shape latent variables"
line 134: "The output ... is an estimate of firing rates of the input."
line 213: "Besides, we added L2 regularization to the expectation and log-variance of the prior distribution to stabilize model training."

The results are difficult to interpret because you compare methods that are all quite sophisticated.
It would help if, for each task, you reminded your reader where chance performance is.
Another way to do that would be to provide some simple linear method baseline.
Some of the writing is unclear, e.g. line 298: "The dataset contains 32 sessions, each for one mouse. Since the class of neurons responsive to natural visual stimuli is found in six visual regions, in this work we choose to analyze the neural activity of five mice that have as many neurons as possible (about 300, see Appendix D for exact numbers) with them evenly distributed across all regions (the coefficient of variation for the number of neurons across six brain regions is below 0.5)."

Most of the evaluations are concerned with properties of the learned representations.
Adding a discussion of the performance of the autoencoding performance would help.
How well are the spikes reconstructed by the autoencoder, can you show examples of successes and failures?

### Questions
Have you considered using only the contrastive objective, i.e. without the decoder and VAE loss? I am asking this because all your benchmarks quantify decodability of image identity from the learned representation.
 
You write line 303 "We select five scenes that elicit the strongest average responses".
Could you tell us more about the images you selected, and maybe show examples?
How does you method behave on the other images, is the approach robust enough to apply to lower signal to noise examples?

Again for the natural videos, it would help if you could give a precise description of the stimulus.
In particular, how much motion is there in these videos?
This is important because you define a very liberal criterion for correct decoding, line 447: "we take the accuracy measured by considering the error between a predicted frame and the true frame within 1s (default size of time window constraint) as a correct prediction."

In line 409 and following, you interpret the shape of the tSNE visualizations.
Is it safe to interpret such a nonlinear embedding? How much of your interpretation depends on hyperparameter choices?

There is a very large performance difference between Mouse 1 and others in Table 3 and 4, what do you make of the variability and can you help us understand this outlier? You already removed one mouse from your analysis, what was the reasoning behind that?

The original paper from which you get the neural data was focused on describing the mouse visual hierarchy. Can your method reveal interesting structure in each visual area and can it reveal a gradient in the visual representation along the cortical hierarchy?

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
4

### Summary
This paper proposes TiDeSPL-VAE, a sequential latent variable model that aims to jointly model neural and visual inputs. The model uses separate embeddings to represent visual features and internal states. However, there are significant issues in motivation and clarity that hinder evaluating its contributions in its current form.

**Strengths:**
- The idea of separating visual features from internal states could be beneficial for neuroscience and machine learning, with potential applications in visual decoding.
  
**Concerns:**
1. **Motivation and Related Work**: The study’s motivation is weak and lacks clarity. Statements on motor encoding and temporal relationships lack precision, and relevant prior work on task-relevant/irrelevant models is omitted. Checking for grammar would also be good to do.
2. **Benchmarking and Fairness**: No clear details on benchmarking models, hyperparameter choices, or treatment of time dependencies are provided. Models like CEBRA and LFADS are compared inadequately due to differences in architecture and training parameters. Additionally, benchmarks on common datasets like the Allen Brain Natural Movie 1 or Sensorium Challenge data are missing, limiting reproducibility/interpretability.
3. **Scientific  Impact**: It remains unclear if the model’s components contribute unique insights, as it largely combines established techniques (VAEs, contrastive learning) without a compelling scientific rationale. The model complexity, evidenced in ablations, appears to drive performance rather than underlying innovations in latent space separation.

**Recommendation:**
While TiDeSPL-VAE may hold promise, the paper’s current form lacks clarity and adequate benchmarking, raising concerns about model novelty and effectiveness. Addressing these issues is essential for it to be a meaningful addition to the field.

### Strengths
Anonymous et al. present a method for joint modeling of neural and visual inputs called TiDeSPL-VAE. The proposed method leverages a sequential latent variable model (LVM) to learn two separate embeddings - one to represent the visual latent features and one to capture the animals' “internal state.” As such, building robust and interpretable latent variable models is of great interest to fundamental neuroscience, translational work (restoring vision), and in machine learning. However, due to missing details and critical baselines (see below), it is not clear the originality or value of the solution they present.

### Weaknesses
I find the study poorly motivated with statements such as *“Most work has focused on analyzing motor neural activity that controls clear behavioral traces and has modeled neural temporal relationships in a way that does not conform to natural reality.”* - what is natural reality? 
Also, note that actual realistic motor behavior encoding-decoding is an unsolved problem. 

Or equally worrisome: *“even though how the visual system encoded input to recognize objects is a primary topic(DiCarlo et al.,2012), and decoding visual neural activity visual stimuli is a challenging research highlight in the neuroscience community (Kay et al.,2008; Wen et al.,2018; Duetal.,2023). Furthermore, existing LVM treat temporal relationships unnaturally (Pandarinathetal., 2018; Schneider et al., 2023) or even don't consider time dependence (Zhou & Wei, 2020; Palmerston & Chan, 2021). Given that visual neural activity has strict antecedent time dependence, these models may struggle to build high-quality latent representations.”* - as a trained neuroscientist and ML expert, I can confidently say this is not neurally accurate. Also, how does LFADS or CEBRA treat “temporal relationships” unnaturally? LFADS uses a dynamical system and CEBRA can leverage the natural time inherent in the neural code, which is a tunable hyperparameter. 

**Related Works/Motivation**

- Why not motivate this study by just stating what you do – you want to see if separating visual features from internal states could lead to better LVMs for understanding (decoding) visual systems. 

- You also miss the related work on task-relevant and task-irrelevant models, such as [1](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=csGAeKgAAAAJ&sortby=pubdate&citation_for_view=csGAeKgAAAAJ:WbkHhVStYXYC) and [2](https://pubmed.ncbi.nlm.nih.gov/37398400/), which should be benchmarked. 

- You also claim, of the models you benchmark: *“None of them build latent representations progressively along the chronological order.”* (L253) - what does this mean? 

**Benchmarking Issues**

- In the main text or Appendix, there are NO details on how you benchmarked the other models, aside from *“In this experiment, we set all models to have 128-dimensional latent variables and train them for 5,000 iterations”*. How is this a fair comparison? Did you not try other dimensions and training losses until convergence? How did you treat time in CEBRA or LFADS, as you can set different offsets - you only mentioned once: *“5 time points for natural scenes and for natural movie”*, but this does not tell me about the offset time in the model? 

- Moreover, the complexity of the different models - B-VAE, LFADS, CEBRA are extremely different. For example, the work from Schneier et al. 2023 (CEBRA)  uses only a 5-layer MLP/GeLU, as the innovation is in the generalized contrastive loss - the point was you can get great performance with a simple model; to fairly benchmark this, then you should use the same RNN as the base model (vs. their MLP). All models you test have many hyperparameters and a full analysis of the parameters you tested is absolutely critical to show. 
- You additionally need to compare model complexity and ideally, run-time estimations.

- You use the Allen Brain Observatory Dataset because you allude that this is the data that Schneider et al. 2023 use, which, I agree, would be ideal. However, you do not benchmark on Natural Movie 1 in the same way; rather, your main benchmark is Natural Images – notably, devoid of time in the stimulus space. It is strange to me that you don’t benchmark on any data - synthetic or otherwise - that anyone else has used in ML to benchmark on. It raises the concern that you are unfairly enhancing the performance of your approach compared to letting the original authors run their code on common data. See my points above.

- Thus, my strong recommendation is that you should also test your approach on “motor tasks” on standardized benchmarks, such as the Neural Latent Benchmark, as well as established vision benchmarks, such as the [Sensorium Challenge](https://www.sensorium-competition.net/) for natural images. At the very least, the Allen Brain Natural Movie 1 data as it was presented in CEBRA where you can add their numbers to a Table to directly compare; here you don’t reach the same decoding performance and you seemingly pick the neurons differently (they report close to 90%, which here your overall is much lower (65%), again making it hard to compare.

- Scientifically, I am also missing how the separate embeddings perform in tasks; by separating vision from task-irrelevant information, do you see a more interpretable latent space? 

- Moreover, it is unclear to me how this is not just an A+B solution; you leverage VAEs, and swaps, and contrastive learning, I don't inherently see the novelty (but this does not affect my score, novelty is a construct anyhow), but I would like to better understand the scientific rationale for the design choice.

**Summary**

I believe your approach could be useful for the field, but in the paper's current form:

1. Lacks the proper motion and clarity in grammar/thought.
2. It is impossible to know if you did a fair comparison due to lacking details, and common benchmarks, and the missing required benchmarking of alternative methods. 
3. Missing task-relevant and task-irrelevant baselines.
4. Your method is more complicated than those you benchmark, and your ablation studies hint at this as well. Comparing Mouse 2 in Table 3 you reach 65.38%, while the second best (much simpler) method reaches 52.76% decoding performance. Now, in Table 4, if you remove anything, you are well below the 52.76%, suggesting that the complexity of your model is driving performance. Just as another test, if you drop in an MLP (as you did from GRU→ LSTM), do you still outperform other models? I would suspect not.

### Questions
Please see above weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new model, the TiDeSPL-VAE, to decode mice's neural activity during passive viewing of natural images and movies. 
The TiDeSPL-VAE is a recurrent auto-encoder-like model composed of two latent spaces, each updated based on the current input and the recurrent state of the previous input. The model is also trained using a combination of losses: reconstruction, KL, and contrastive.
All in all, the authors demonstrate that the TiDeSPL-VAE outperforms numerous baselines in reconstructing spiking activity on synthetic and naturalistic datasets.

### Strengths
The authors have been rigorous in the research methodology, comparing their model against a wide variety of baselines and testing the ability of these models on different datasets, from synthetic to more naturalistic settings -- and a complementary ablation detailing the critical components of the model.

The authors also attempt to solve a novel problem by decoding visual data from mice instead of the widely studied mice's motor system.

### Weaknesses
 **Major Weakness**: The authors insist on the novelty of their work as it deals with visual data instead of motor data from mice. However, the format of the data -- spiking activity -- is treated similarly, whether it is from the motor or the visual cortex. The model still takes the spiking activity as input and outputs the reconstructed spiking activity. To take advantage of the visual modality, it would be interesting to evaluate whether it is possible to decode the input stimuli (image or movie) or to relate the model better with neuroscientific findings about the mouse visual cortex. As it is presented now, the model could also be employed on motor data and perform similarly well. The use of visual data should be better exploited to highlight the scientific advances of this article more than the methodological part. 

**Minor Weaknesses**:
- The writing should be slightly improved to make the paper easier to read. A lot of sentences are not very clear, and others have grammatical flaws. For example, L269 "... and others are even difficult to split four clusters ..."; L482 "contrast learning"; ...

### Questions
- Why are the reconstruction and KL losses computed on the positive samples as well as the other samples? Isn't there an incentive already with the contrastive loss to emphasize positive samples? Can the authors include in the ablation study the training with the losses on all samples only to evaluate the impact of these terms?

- L259, the authors mention that the two synthetic datasets consider "different properties of visual neural activity". What are these properties?

- It looks like the authors train a model for each mouse and treat each mouse as a single dataset. How different would the results be if the authors tried training on all the mice? Or training on some of them and testing on the left-out individuals?

- Can the authors include in appendix the number of samples (train, val and test) for each dataset? It looks like, with all the exclusion criteria, the dataset size ends up being very small. Can the authors confirm that the models are not overfitting on data of a single animal?

- Can the authors also include a table indicating the number of parameters of each model in the Appendix to confirm that the comparisons are fair?

- The ablation study highlights the importance of the contrastive loss and swap operation. Without these objectives, the model does not outperform most of the baselines. But the model has other characteristics that the baselines do not have such as the recurrence due to the two RNNs and two latent spaces. To ensure that these additions are important, can the authors include in the ablation study a non-recurrent version of the model (i.e. setting the number of timesteps of the RNNs to 1), and a version without each of the latent spaces?
Additionally, would it be possible to train one of the best baselines with the contrastive loss and the swap operation?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce the latent model, which separates the visual activity in the content and context representations, also taking the time dependency into the account. This seems to help to have more disentangles representations of mice visual cortex activities

### Strengths
* Original work, applying a new idea of splitting context and content of neural activity in the visual cortex
* The necessary baselines such as LFADS, pi-VAE, and CEBRA are represented in the paper
* Careful evaluation on both synthetic and real-world datasets, also following classic for the field benchmarks, like Lorenz systems
* Sanity checks experiments, such as shuffling time dependent dateset help to disentangle the impact of time-dependency for the model 
* The authors are very transparent about the limitations of the model

### Weaknesses
 * Reproducubility might be an issue. The code is not provided and the implementation details in the appendix A are not sufficient. Details like how many RNN layers were used, how exactly the RNN was implemented, what activation functions were used, and the precise initialization strategies are missing. GRU is mentioned later in the paper but I think an explicit model architecture picture and more parameter details in appendix A would help to improve the paper. Furthermore, the loss function details are not fully specified, such as the exact form of the reconstruction loss and the weighting of different loss terms.
* Generalisability and robustness of the model is an issue as scores per mouse differ a lot, also it is not clear how the model would behave if the animal was shown different stimuli (ie gratings instead of the natural images). The performance variability across mice suggests potential overfitting to individual subject characteristics or specific experimental conditions. It is also unclear how the model would perform with different types of visual stimuli, such as simple gratings or other artificial patterns, which would be important to assess the generality of the learned representations.
* Some references like [1,2] are missing, which could be nice to position the TiDeSPL-VAE model in the space of LVM as they are the representatives of modern non-VAE based LVM (while they are different from the current work)

### Questions
* RNNs are often tricky to train. Were there any issues that you phased during the model training or some details, which are crucial for a successful learning. 
* Did you train a new separate model per mouse? Or was it a shared model across mice?
* In figure 3 for TiDeSPL-VAE, LFADS and especially CEBRA there seems to be a clear train/test bias (points are separated), which is stronger than the cluster separartion based on the stimuli. How do you interpret this?
* how exactly the train/test splits are done with respect to the time? As the train loss takes a sequence of responses from the near future with some $\vartriangle t$ - do you ensure that none of the validation/test responses were shown during training?

### Soundness
3

### Presentation
3

### Contribution
3
