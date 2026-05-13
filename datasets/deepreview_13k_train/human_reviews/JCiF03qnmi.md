# How Does Critical Batch Size Scale in Pre-training?

- Decision: Accept
- Scores: 6, 8, 6, 6, 8

## Abstract
Training large-scale models under given resources requires careful design of parallelism strategies.
In particular, the efficiency notion of critical batch size (CBS), concerning the compromise between time and compute, marks the threshold beyond which greater data parallelism leads to diminishing returns.
To operationalize it, we propose a measure of CBS and pre-train a series of auto-regressive language models, ranging from 85 million to 1.2 billion parameters, on the C4 dataset. Through extensive hyper-parameter sweeps and careful control of factors such as batch size, momentum, and learning rate along with its scheduling, we systematically investigate the impact of scale on CBS. Then we fit scaling laws with respect to model and data sizes to decouple their effects. Overall, our results demonstrate that CBS scales primarily with data size rather than model size, a finding we justify theoretically through the analysis of infinite-width limits of neural networks and infinite-dimensional least squares regression. Of independent interest, we highlight the importance of common hyper-parameter choices and strategies for studying large-scale pre-training beyond fixed training durations.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the scaling behavior of critical batch size in the pre-training of autoregressive language models.
They first define the critical batch size (CBS) as the point where increasing the batch size no longer leads to significant gains in computational efficiency (>20% overhead when doubling the batch size vs. a linear scaling). They then perform experiments to determine the CBS of autoregressive Transformer-based language models of varying scales, finding that CBS scales primarily with the size of the training dataset rather than model size. They provide theoretical support for this finding by studying infinite-width limits of neural networks and infinite-dimensional least squares regression problems.

### Strengths
- The paper provides an interesting finding that the critical batch size scales mostly with data set size, and is largely invariant to model size. This is a relevant and, to my knowledge, novel insight.
- The paper considers models ranging from 85 million to 1.2 billion parameters and thus covers a reasonably large domain of models.
- I really liked the highlighted practical takeaway blocks throughout the paper, which made it easy to understand, well-structured, and accessible.

### Weaknesses
Some of the takeaways seem to me a bit too bold or not backed by enough evidence for the given claim.

- For example, in Section 2.2, they compare the efficiency of learning rate schedules across batch sizes by comparing the number of steps to achieve a given target validation loss. They conclude that "EWA consistently improves model training efficiency. [...] while outperforming Cosine for large batch sizes [...] and even with appropriate learning rate decay, [Cosine] underperforms our constant+EWA strategy in large-batch settings." (line 188). However, looking at Figure 2b), we can see that the training duration of cosine was chosen inefficiently. It continues to decay well beyond the target validation loss, achieving the target at roughly 50% of its decay schedule. It is also clear to see for the WSD schedule, which hits the target loss shortly after starting its decay, i.e. it is still halfway in its decay phase when crossing the threshold loss. I believe making a statement like "EWA consistently improves model training efficiency" requires a more rigorous empirical analysis. For instance, Schedule-Free [1] suggests a similar running average strategy to improve efficiency, providing a much more comprehensive and rigorous analysis.
- Similarly, Section 2.3 claims that different context lengths have similar CBS, based on a single (comparably small) model & dataset. It seems that the lines start to diverge a bit more for larger batch sizes, so is it possible that this is more pronounced for other settings (e.g. larger models, more training data, etc.)?
- All claims are made for the definition of CBS using 20% overhead. The authors state that "20% can be replaced by any other suitable measure of increase from linear scaling". I wonder how the results and conclusions would change if one varies this parameter, e.g. to 10% or 50%. For example, what would a plot look like of the CBS per model or data size as a function of the overhead?


### Questions
- A central takeaway of the paper is that "CBS remains invariant when scaling up N [model size]" (line 93). However, isn't this partially contrasted by the results in Section 2.4, where you write "Figure 4 shows that increasing depth and width [and thus model size] can both slightly increase the CBS" (line 264)?
- I found the plots to sometimes be a bit confusing or less accessible. Some suggestions:
  - Could you add the linear scaling line as well as the 20% region?
  - Could you highlight the critical batch sizes, e.g. by a star marker?
  - Nit: The font sizes are inconsistent between subplots, e.g. the x-axis labels between Figure 1a and the subplots of Figure 1b.
  - In the legend of Figure 1b (left), what is the number in parenthesis? Is it the (relative) number of training samples?
  - The lines are sometimes hard to read. E.g. in Figure 2a, the Constant+EWA line is very bright. Similarly the lines in Figure 2b. I also had trouble distinguishing the shades of blue, e.g. in Figure 1. But it does look pretty :)
  - Nit: The white spaces in Figure 4 are a bit weird. There is only a small space between the subcaption of subplot (a) and much more white space between the subcaption (b) and its subplot.
- In line 110 you mention that "traditional learning rate decay strategies typically require predefining the total training duration" and you mention Defazio et al., (2024). However, isn't Schedule-Free a counter-example? Schedule-Free is also using a, at least to me, a relatively similar approach to your "constant+EWA" strategy, no (e.g. comparing the equation in line 158 to Eq. (5) by Defazio)? Could you elaborate on how your method differs from Schedule-Free?
- For most of the paper, you sweep the batch size between $2^6$ and $2^{13}$ with the exception of Figure 3, where the batch size is between $2^{16}$ and $2^{22}$. Is this because in this figure, you count the number of tokens, so practically batch size * tokens per batch?
- You provide a scaling law fit of the CBS. Did you try checking how close your thus predicted CBS tracks the true CBS for "unseen data points", i.e. test its predictive power?
- In the concluding remarks you write "Our findings contribute insights into [...] particularly highlighting the role of hyper-parameters such as learning rate scheduling and optimizer settings" (line 530). What "optimizer settings" are you referring to?
- Nits:
  - Line 120: I believe the "Refer" is superfluous.
  - Line 157: There is probably a closing parenthesis missing after the second citation.
  - Line 185: Typo for "maximum".
  - Figure 3a doesn't need to be a subplot as there is no other subplot.
  - Line 260: This sentence seems grammatically weird to me "As the main result in Figure 1 only involves a single way for scaling up models [...]". I might also have misunderstood the sentence. For example, doesn't scaling from 151M to 302M double the depth, and therefore Figure 1 involves multiple ways of scaling up models?
  - Line 271: "Compute-optimal" should probably be lowercase.
  - Line 288: Typo with "achieved" and "batch size".
  - Line 351: "chinchilla" should probably be capitalized.
  - Line 366: "They" -> "Then"?

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
3

### Summary
The paper studies how the critical batch size (CBS) - the threshold beyond which increasing batch size causes diminishing return - scales with the model and data size for pre-training language models. The authors conduct careful experiments on models ranging from 82 million to 1.2 billion parameters and show that the CBS slightly scales with data size rather than the model size (remains invariant to model size). The authors also provide theoretical justifications for this phenomenon using infinite-dimensional least squares regression and the infinite-width limits of neural networks. These findings have important implications for designing efficient pre-training strategies.

### Strengths
- The paper is well-written with clear organization. This work would be a valuable contribution to the ICLR community. I especially appreciated the “key takeaways summary” after each section.
- The experimental design is rigorous; for example, decoupling various hyperparameters makes the claims more convincing.
- Detailed experimental procedures are provided in Appendix D.
- The formalization of CBS (beyond [1] “An empirical model of large-batch training”) would be helpful in the literature. The key findings that the CBS scales slightly with data size (and stays invariant to model size) are interesting. These insights have important implications for efficient pre-training strategies.

### Weaknesses
 - The experimental scope is limited to models up to 1.2B parameters trained on C4, which may not fully capture scaling behaviors at larger scales (e.g., models with over 50B parameters). On a similar note, key ablation studies are primarily conducted on smaller models (with C4). However, given the careful experimental design and clear theoretical analysis, I do not believe that these impact the validity of the findings.
- It would be helpful to have a dedicated section discussing the limitations of both the theoretical analysis and empirical findings (e.g., Gaussian data distribution).
- However, I believe that the work has substantial limitations that would prevent me from recommending acceptance.

### Questions
- (Minor) It would be nice to use $\times$ instead of * (asterisk) in line 135.
- (Minor) The color contrast in Figure 9 can be improved.

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
The paper revisits the role of batch size in scaling language models during pre-training. The core finding is that the critical batch size needs to scale alongside the model. However, both the critical batch size (CBS) and model scale (specifically, model width) show diminishing returns when scaled under a given training budget. The authors demonstrate and conclude that CBS scaling is dependent on data scale but invariant to model scale. Various hyperparameter ablations provide additional insights into relative pre-training performance efficiency.

### Strengths
1. The paper is well-written and largely easy to follow.
2. The related literature covers the important papers in the topic well.
3. Formalizations and hypotheses are clearly outlined and help understand results better.
4. Though personally I would like to reconsider its exact design and placement, the _Takeaway_ block was helpful while reading the paper first time.
5. The model scales reported in experiments are adequate in applying the insights to large-scale pre-training.
6. Formalizing the notion of critical batch size (CBS) through the 20% overhead assumption is novel and seemingly useful.
7. Considering various hyperparameters ablated across selected model scales is important and welcome in a scaling-related paper.

### Weaknesses
1. Some lower scale experiment with repetitions over different seeds to show the robustness of the findings (laws, exponents) and insights (data dependence and model scale invariance).
2. The work is mostly a benchmarking study with main contribution relying on the hypothesis constructed and how the experiment for it is setup, which therefore leaves more room for explaining some of the design choices, especially with model scale, hyperparameters (see, Questions below for examples).
3. Section 3.3 mentions how different hyperparameters were adjusted _to achieve optimal performance_ (at 302M), however, the grid search (for ablations) were done on a different model scale (151M), and thus is unclear what were the different HP settings considered in fitting points for the power law. Furthermore, it is not clear if the optimal hyperparameters found on the 151M model would generalize to the larger models, especially given the different training dynamics that might exist at different scales.
4. Theorem 1's proof by existence could do with more details and support, i.e., it is unclear how _training iterations t_ related to models of different width (thereby, scales), possibly different batch size scales and naturally different compute budgets under Chinchilla-optimality (see, Questions). The theorem also lacks a clear connection to the empirical results, making it difficult to assess its practical relevance.
5. Despite leveraging theoretical insights from muP, there is only a limited grid search over learning rate values over the smallest available scale while that is apparently used as-is for even the larger model trainings, i.e., hyperparameters are not suitably scaled (this is unclear overall). The paper should provide more justification for why the learning rate is not scaled with model size, especially given the theoretical underpinnings of muP.
6. The outcome of the theoretical proofs and empirical results appear independent and do not knit the contributions as well.
    * Is there a way to connect the toy regression experiment with the scaling law exponent fits?


Minor issues/fixes:
1. Discrepancy of batch size 256 or 512 as the batch size for calculating overhead ratios
    * L52, Fig. 1,3,4,6,8 y-axes, L370, L888.
2. Should likely be `b > a` in L1299.
3. Typo on L366: perhaps should be "They" -> "Then"
4. Discrepancy in Fig. 5 caption where $C_{chin}$ comes to be around 6 as per the equation given for $B^*$.
5. Figure 4.a doesn't mention which model width or depth.
6. Figure 10 mentions _context length_ but has nothing to show for it.



Nitpicks:
1. Irregular and inconsistent plot sizes.
2. Recommended to refer sections/tables/figures in the Contributions list in Section 1.
3. Vertical lines in Table 4 separating different model sizes.
4. Parantheses in L1119-1122 would enable easier parsing for readers.

### Questions
1. Could the paper have bit more insight into why certain model scales were picked for certain experiments, since it is not always the smallest (151M) model that was selected?
2. Any reason explaining the worsening _efficiency_ for a 1.2B model on larger batch sizes in Figure 1.b) (right)?
3. For a study with even lesser bias or confounding factors, would it make sense to make conclusions on the critical batch size (CBS) or its scaling exponents without an EWA of model weights? 
    * In a similar vein, can we see in Figure 2 what only constant LR schedules look like?
    * Is cosine here with or without warmups?
4. Why does Figure 2 (right) have different step lengths for the same batch size assuming similar compute budgets overall, given same model size? 
    * Similar to above, why does Figure 9 all have different lengths?
5. Why do we expect the rankings of different schedulers found on 151M scale would transfer to larger scales? Do we have a literature or empirical reference for it?
6. Is the only notion of _efficiency_ in paper as denoted by the overhead ratio metric as defined by the measure on batch size 256/512?
    * For every result seen as plot/table, does it mean there was an equivalent run made on a batch size 256/512?
7. Would Figure 3 result hold for larger models with bigger context sizes? (I am not asking for an experiment at such scales but a cheaper experiment that could serve as proof-by-contradiction)
    * How does the model size change when Figure 3 writes about a model of size 151M but with context size ranging from 512-4096?
    * Are model sizes calculated without the embedding parameters?
8. Could the 20% and the resulting 5 in Section 3.2 be more generalized in the formalism?
    * Could the readers have a clearer reference/intuition for the 20% overhead?
9. Could L318-319 have more support?
10. Does Figure 5 have empirical backing regarding the predicted CBS and the formalism of staying within the 20% margin of steps for similar loss?
    * Or if the decoupled prediction for batch sizes hold _reliably_ for different scales or ablations such as architecture, datasets, hyperparameters?
11. How exactly are the tuning decisions undertaken especially in Section 3.3 (example, L371-372)?
12. In Theorem 1, is it expected or meant to be $w_2 > w_1$? If so, then there is a typo and makes a significant difference to the interpretation.
13. What is the significance of _t_ in Theorem 1? Should we compare losses under similar tokens for two vastly different model scales, especially following Chinchilla?
14. What is the specification or how is $\mathbf{H}$ defined in Section 4.2?
15. Is there a more intuitive summary for the proofs for Theorem 2 and 3 especially for readers (like me), not familiar with Zou et al. (2023)?
16. How exactly does the _hybrid evaluation_ (L968) provide _more accurate_ information?
17. What or how are the hyperparameters (HPs) for parameter sweeps ranked or ordered (L977-979)? Does a different ordering yield potentially different results?
    * What are the default values for other hyperparameters when tuning each of these in order?
    * Assuming in this order that LR is considered to be the most important HP, why tune the least important HPs (in $\beta_2$ and $\lambda$) for each model scale and not LR (Table 4)?
18. I may have missed it but could there be a reference for how the power law model fit is made for the values in the caption of Figure 7?


Overall, the paper reads nice and does touch on an important and often under-studied aspect in scaling literature.
However, the paper writing and presentation raises some eyebrows with really big plots, white spaces used, and a theory which feels like a sub-paper than something that brings the story together.
Given the expensive space of empirical experiments, the authors did well to consider multiple design choices and study them. 
Unfortunately, that also opens up more questions on how these designs were arrived at and that clarity would be my primary criticism.
One other thing would be the lack of _a_ clear takeaway in terms of _how_ a pre-training practitioner could use the insights from this paper when scaling (model or data).


Scores may be increased depending on suitable responses to most of the points raised above.
Thank you for the paper, it was a nice read overall.


PS: I was unaware of Zou et al. 2023 and have not verified the proof on Pages 22-24.

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
4

### Summary
The authors reassess the notion of critical batch size (CBS) in the context of language model training, and investigate the impact of scale on CBS. They find that the CBS does not scale with model size in majority, but with data size, and highlight roles of optimizer choices, where they find exponential averaging with a constant LR to be performant, matching or outperforming cosine or WSD.

### Strengths
First of all, I thank the authors for looking into this problem — I believe the question of CBS is both extremely relevant and understudied. The paper is written in a clear manner, the experiments are very extensive, and the authors additionally provide theoretical studies. The work could be a starting point for further studies, e.g. going beyond Chinchilla optimal points.

### Weaknesses
While I very much appreciate the topic and investigation of the paper, I unfortunately have to be very critical of the experimental evaluation.

- First, the authors note in the Appendix that they disable weight decay of AdamW, without justification; this means effectively only studying Adam and not AdamW. However, weight decay is not only a major part of modern large scale training (see e.g. Chinchilla Fig A7 https://arxiv.org/pdf/2203.15556 or Wortsman et al. (2024) https://openreview.net/pdf?id=d8w0pmvXbZ), but it also strongly changes the training trajectory, where disabling it leads to a practical decrease of the effective learning rate even for a constant schedule; see e.g. Kosson et al. https://arxiv.org/pdf/2305.17212. Therefore, it is unclear how the findings would generalize to actual practical settings (proper baselines), and assuming the same results is misleading. The absence of weight decay not only impacts the final performance but also alters the learning dynamics, potentially masking the true behavior of the critical batch size. The effective learning rate reduction caused by disabling weight decay can lead to an underestimation of the optimal batch size, and the conclusions drawn from these experiments may not hold when weight decay is properly applied.
- The authors find a constant LR + EWA to be extremely performant. I have tried to replicate their results with the same hyperparameters (including disabled WD) in the same setting of LLM pretraining and fail to obtain the same results. While EWA can give a slight boost, it is far from the cooldown loss; even more, using e.g. a decay of 0.99 or higher results in a similar curve to the one of 0.9999 in Fig. 8 (increase in loss, but much earlier in training) and then EWA is *much worse* than the original model. Since the authors have not provided code, it is unclear to me where this discrepancy is coming from — I repeat this point as a question below. The specific implementation details of EWA, such as how the decay rate is adjusted during training, are not clearly defined, making it difficult to reproduce the reported results. Furthermore, the claim that EWA is extremely performant is not sufficiently supported by the provided evidence, and the lack of a detailed analysis of EWA's behavior across different decay rates and training stages raises concerns about the robustness of this finding.
- For most experiments, the schedule free optimizer performs surprisingly bad; if well tuned, I would think it should be at least as good or below the stable phase of WSD from my experience. The poor performance of the schedule-free optimizer suggests that it may not have been tuned adequately, or that the chosen hyperparameters are not suitable for the experimental setup. This raises concerns about the validity of the comparisons made in the paper, as the baselines may not represent the true potential of each optimizer. The lack of a thorough hyperparameter search for the schedule-free optimizer undermines the conclusions drawn from these experiments.

### Questions
I mention the main points in the section above, but repeat them here as questions (with some others):

- Why did the authors choose to disable weight decay?
- How did you use EWA in detail, or is there a specific implementation trick that was required?
- Did you tune SFO with the same sweeps as Adam?
- Why are the warmup steps chosen between 0.15, 0.25 and 0.35? These are quite large fractions, whereas in practice the warmup is often a very minor part of training (e.g. less than 5%).

I would be very happy to engage in a discussion about these points. More broadly, I hope the authors see my comments as not only critical but encouraging.

Another minor comment: I think the choice of colors for the plots is not ideal, as the contrast is very low and it makes it hard to read and compare lines (especially for people with color vision deficiency).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies how a compute-optimal batch size, the critical batch
size (CBS) is influenced by scaling the amount of data or model
parameters in a Transformer-based language modeling objective. Most
importantly, the authors show a correlation between the training
duration and CBS, both empirically and theoretically. Importantly, the
experiments also show that model size does not have an effect on CBS.
Finally, a secondary but interesting part of the experiments concerns
allowing to change the training duration mid-training. It is shown
that a simple constant schedule combined with exponential weight
averaging at the end of training outperforms both "standard" cosine
decay and the recently proposed warmup-stable-decay (WSD) schedule.

The empirical study also includes a controlled setting to study the
effect of width- vs. depth-scaling on the CBS (the finding being that
both scaling methods influence the CBS similarly). Finally, the
authors additionally underline their empirical findings using
NTK/tensor programs and Gaussian linear regression theory.

### Strengths
For their experiments, the authors used C4, a de-facto standard NLP
research dataset, which makes interpretation and reproduction of the
paper of the paper easier.

A particularly strong section is that of relevant work, in which
various important related papers are summarized well.

I also really enjoy the "takeaway" boxes as section summaries.

### Weaknesses
The paper heavily relies on Chinchilla scaling theory and
Transformer-decoder training with the language modeling objective. It
does not account for settings which use fewer training steps than
Chinchilla-optimal training and does not study other data sets or
models. This means it is difficult to extrapolate the results to the
general domain of deep learning.

I would personally have preferred use of a more standard "dynamic
horizon" schedule such as WSD for the experiments in order to improve
interpretability/comparability with regard to other research. That
said, the finding regarding constant+EWA quality is important.

Weight decay was disabled for the experiments, which is hardly done in
practice.

### Questions
### Please address

In Proof of Theorem 1 (page 8, line 418-419), it is stated that "the
trajectory of the network approaches a limit as width tends to ∞". I
would wish for what exactly is meant by "trajectory" to be defined
more clearly. E.g., is it the trajectory of the weights during
training? Also, please cite a source for this statement.

Appendix D, Evaluation data size and frequency (page 18, line 964ff):  
Which which model after what training have these evaluation variance
numbers been obtained?

### Minor comments

Page 3, line 158:  
Please describe the meaning of θ.

Page 8, line 416:  
$R(M, t)$ denotes the loss of network $N$ at time $t$.  
-> $R(M, t)$ denotes the loss of network $M$ at time $t$.

In the experiments, ideally, the optimizer's ε hyperparameter would
also have been scaled with the model size
(https://arxiv.org/abs/2309.14322).

### Soundness
4

### Presentation
4

### Contribution
4
