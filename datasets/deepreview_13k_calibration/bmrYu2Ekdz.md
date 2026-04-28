# PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Understanding the stability of language model pre-training and its effects on downstream performance is still understudied. 
Prior work shows that the training process can yield significantly different results in response to slight variations in initial conditions, e.g., the random seed.
Crucially, resources to study pre-training stability in language models are still lacking, especially for decoder-only models.
We introduce the PolyPythias, a set of 45 new training runs for the Pythia model suite: 9 new seeds across 5 model sizes, from 14M to 410M parameters, resulting in about 7k new checkpoints that we release.
Using these new 45 training runs, in addition to the 5 already available, we study the effects of different initial conditions determined by the seed---i.e., parameters' initialisation and data order---on (i) downstream performance, (ii) learned linguistic representations, and (iii) emergence of training phases.
In addition to common scaling behaviours, our analyses generally reveal highly consistent training dynamics across both model sizes and initial conditions.
Additionally, the new seeds for each model allow us to identify outlier training runs and delineate their characteristics.
Our findings show the potential of using these methods to predict training stability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors created 45 different training runs on 5 existing language model series Pythia 14M to 410M with varying random seeds. The authors named these runs as PolyPythia, and performed several investigation on the model performances and dynamics. Specifically, the authors reported (1) downstream performance and its agreement (between other seeds) and consistency (within the same seed), (2) algebraic analysis on the embedding vectors (through trained probes), and (3) HMM-based transition analysis. Every experiment show that there is a consistent trend among different model sizes and seeds except 2 runs on the largest model they trained. These 2 runs are specifically investigated in detail in the paper, compared with other stable runs.

### Strengths
* It is definitely useful if the trained checkpoints in this study are released. Especially, it involves unstable runs (runs with loss spikes), so this will provide clues to understanding loss spikes, which are always a problem when training large language models.
* Probing and HMM analysis are ones of interesting examples of the recent techniques to analyse the inner representation/dynamics of the models.

### Weaknesses
 * As noted in the paper, the size of the model trained by the authors is limited. Compared with the sizes of recent language models that tend to have usually more than 1B-10B parameters, the size of the maximum model in this paper (410M) is too small and it is still unclear that (1) the same phenomena observed in the paper can be identified in larger models and (2) if other unseen phenomena will happen in the large models. Specifically, the scaling properties of the observed phenomena, such as the consistency of downstream performance across seeds or the identified state transitions in the HMM analysis, remain uncertain for models beyond the 410M parameter scale. The paper does not provide any analysis or discussion on how these observations might extrapolate to larger models, which limits the generalizability of the findings.
* It is also still unclear if the phenomena on training are discovered well even in the same range of model sizes that the paper focused on. The paper confirmed its stability of each runs (except the two runs on 410M), it is not revealed that what configuration affects the stability as the experiment only varied the random seed for each model size. The study does not explore other potential factors that could influence training stability, such as variations in learning rate schedules, batch sizes, or optimizer settings. The lack of exploration of these factors makes it difficult to attribute the observed instabilities solely to random seed variations. Furthermore, the paper does not provide a clear definition of what constitutes a 'stable' run, making it hard to interpret the claims of stability for the majority of the runs. A more rigorous analysis of the training dynamics, including metrics like gradient norms and eigenvalue distributions of the Hessian, would be beneficial.



### Questions
* It looks the number of checkpoints mapped in every figure is less than that the authors actually captured, especially checkpoints after 10^3. Though I think authors have sampled some of them for some reason, it would be useful to plot all data points.
* As shown in figures, there are remarkable trends between steps 10^2 to 10^4 in all runs. It may be desirable to save and analyse checkpoints at more frequent intervals in this range, rather than following the same schedule in Pythia.
* Related to the second itemizing on the weaknesses, I'm also curious whether we can say that the observed state transisions in the HMM analysis are generic tendency or not, especially for unstable runs, to judge whether we can utilize this tendency to forecast problematic behavior of training runs, or we can use this tool for only analysing the checkpoints *after* they were obtained. It would be better to take more observation around this point, but I also understand that it requires more compute resources.
* In my personal experience on billions-scale LMs, I often observed loss spikes during many runs, but most of them can be recovered very quickly within less than 100 steps, but there are also several spikes that catastrophically destroys the whole model and the recovery requires as many steps as the authors observed in this study. I'm curious if authors observed similar trends to that I noted here or only the two the paper mentioned.

### Errors
* It looks Fig. 1 is strange:
  * It is mentioned with "middle and bottom rows" in p.3, but it looks the correct reference should be "middle and right columns."
  * Some important data points are mentioned in p.4 paragraph "Finding outlier seeds ...", but the figure actually doesn't show them. Especially the paragraph mentioned the two unstable runs, that Fig.1 doesn't include any data points for specific runs.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces 45 training runs (~7K checkpoints) for 5 model sizes of Pythia, ranging from 14M to 410M parameters across 9 seeds. The work mainly studies model training dynamics and scaling behaviours across seeds and model sizes.

### Strengths
- The paper is well-written. The authors support every claim with a thorough experimental setup.

### Weaknesses
 - I do not find any significant weakness(es). Please refer to other reviews for a collective opinion.

### Questions
--

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the stability of language model training, specifically focusing on how random seed variation affects downstream performance. The authors release a dataset of 45 additional runs for the Pythia model across various model sizes, of up to 400M. They explore downstream task performance, stability properties and training phase dynamics. Their findings indicate mostly stable training behaviors for the sizes used, with the exception of a few outliers at the larger size.

### Strengths
- Impact of the data released: This data will allow other researchers to investigate the questions in this paper and potentially others. Some of the findings, even if unexplained are very interesting: for example the fact that the inter-seed agreement peaks at the moment where models start to leaning meaningful patterns.
- The paper is well written and provides thorough and extensive investigations into the questions addressed. The experimental results in themselves are very interesting and likely to aid in furthering this topic. A better understanding of training dynamics can lead to more efficient and effective use of resources in the community.

### Weaknesses
 - The representational stability investigation: I am not convinced by the interpretation (or explanation) given to the experiments in this section, namely: 1) It looks like you are building classifiers to solve various tasks based on the hidden representations of the networks (which is a very useful setup in practice for solving those tasks). However the entire setup is cast as a way to investigate the representation stability. Imo this requires more explanation, since it's not stability as e.g. similarity of hidden representations (the most straightforward way to understand it), but stability w.r.t to their ability to solve certain tasks. As such I am struggling to understand the MDL and linear probe interpretation of this setup 2) The sparsity-inducing prior: If random vectors can be used to learn the tasks perfectly then the tasks may not be well designed. If random vectors can be used to learn the task to some extent, in that case just use that as a baseline factor (which I assume is what codelength ratio aims for). 

- Gender bias tasks: the authors are not sure if the small benchmark size is causing the results observed. I would recommend making this investigation more thorough and use gender bias data sets released for other tasks. Given that LLMs can be used to address any task, that should not be an issue (I know machine translation has such data sets, but I am sure other tasks as well). 

- Interpretability of section 5: motivate why you use feature maps rather than something simpler and more interpretable (see suggestions bellow)

### Questions
Questions:
- I find the sparsity inducing prior in equation 1) problematic. Please give more details there: I assume it's kept constant across all setups; or can you design experiments that don't require it (where random representations don't perfectly solve the tasks)?
 
Suggestions
- in section 4: I would recommend to explain the MDL and linear probe interpretation of this setup a bit better, or alternatively remove it altogether. Specifically, what I see is a setup of training classifiers on top of the hidden representations to solve various tasks. You are then looking at various metrics across different checkpoints: task performance, task performance relative to random baseline, change in classifier parameters. The interpretation that is more natural to me is that you want to investigate the change in model parameters; you are investigating this change in a task-oriented setup, because the relation between parameters when varying the seed is not obvious (although at different training stages that relation can be easily quantified with standard metrics). 

- in section 5: it's unclear why you need something as complicated as training maps to explore this. If previous work explained the limitations of using a list of simple interpretable metrics please, do include that here. Table 3 showing the actual features determining transitions is much more illuminating and shows that the data is quite interpretable. I would recommend listing these features at the beginning of section 4 to give the reader a more concrete understanding of this section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents PolyPythias, which extends the Pythia model suite with 9 additional training runs (with different seeds) for 5 model sizes (from 14M to 410M). Detailed analyses are performed from different aspects, including downstream performance, intermediate hidden representations and model parameters. Several interesting patterns are discovered with regard to different training phases and identifying outlier seeds. The presented checkpoints as well as the analyses can inspire more future work on the direction of understanding LM training.

### Strengths
- Understanding LM training is an important research direction that could lead to better model interpretability and better LM training.
- The analyses and the released checkpoints could help the community to study the stability of LM training.

### Weaknesses
 - While it is understandable due to limited resources, the model sizes studied in this work is overall small (the largest one is 410M), while commonly utilized LMs are typically larger than 1B.
- Though the analyses are well-presented, there is still a lack of guidances on how we could train better LM models. One potentially interesting thing is to predict outliers to make the training more stable, and it would be nice if there could be more experiments and analyses on this point.

### Questions
- For the "inter-seed agreement" metric described in Sec. 3.1, how about comparing all the pairs of models trained with different seeds? Would it lead to similar results compared to only checking against seed 0?
- It would be nice if there could be some highlighted summarizations at the end of each section to describe key takeawys for the analyses.

### Soundness
3

### Presentation
3

### Contribution
3
