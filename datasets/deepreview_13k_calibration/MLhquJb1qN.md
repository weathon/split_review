# Time Transfer: On Optimal Learning Rate and Batch Size In The Infinite Data Limit

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
One of the main challenges in optimal scaling of large language models~(LLMs) is the prohibitive cost of hyperparameter tuning, particularly learning rate~$\eta$ and batch size~$B$. While techniques like $\mu$P~\citep{yang2022tensorprogramsvtuning} provide scaling rules for optimal $\eta$ transfer in the infinite model size limit, the optimal scaling behavior in the infinite data size limit~($T \to \infty$) remains unknown. We fill in this gap by observing for the first time an interplay of three optimal $\eta$ scaling regimes: $\eta \propto \sqrt{T}$, $\eta \propto 1$, and $\eta \propto 1/\sqrt{T}$ with transitions controlled by $B$ and its relation to the time-evolving critical batch size $B_\mathrm{crit} \propto T$. Furthermore, we show that the optimal batch size is positively correlated with $B_\mathrm{crit}$: keeping it fixed becomes suboptimal over time even if learning rate is scaled optimally. Surprisingly, our results demonstrate that the observed optimal $\eta$ and $B$ dynamics are preserved with $\mu$P model scaling, challenging the conventional view of $B_\mathrm{crit}$ dependence solely on loss value. Complementing optimality, we examine the sensitivity of loss to changes in learning rate, where we find the sensitivity to decrease with $T \to \infty$ and to remain constant with $\mu$P model scaling. We hope our results make the first step towards a unified picture of the joint optimal data and model scaling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies how to set the learning rate $\eta$ and batch size $B$ when the total number of steps $T$ increases. A series of conclusions are drawn from the experiments on MPT of scale 32M, 101M and 354M:
1. A scaling law of the optimal learning rate given $B$. It depends on whether $B$ is smaller than a threshold $B_{crit}$.
2. A scaling law of the optimal batch size, assuming the learning rate is tuned to the optimal.
3. $B_{crit} \propto T$.

### Strengths
1. This paper studies an important problem. Hyperparameter tuning is very costly in LLM pretraining. The optimal choices of these hyperparameters are particularly unclear when the number of steps $T$ is a variable.
2. Experiment results are well-organized.
3. A series of scaling laws have been derived. These laws could be useful for tuning the learning rate and batch size.

### Weaknesses
My major concern is whether the experiment results can indeed support their scaling laws.
1. It is hard to see the claimed scaling of optimal LR from Figure 1. The curves in Figure 1 are very noisy, and the scaling formulas match the experiment results only for a few choices of $T$. It is thus unclear whether the scaling formulas here describe a real trend or just some noise. Specifically, the optimal learning rate seems to fluctuate significantly across different values of $T$, and the proposed scaling law doesn't consistently capture these fluctuations. For instance, the optimal learning rate for a given batch size at $T=1000$ might be higher or lower than what the scaling law predicts based on the optimal learning rate at $T=500$, and this inconsistency is observed across different batch sizes. The lack of a clear, monotonic trend makes the proposed scaling law questionable.
2. It is even harder to see the claimed scaling of optimal batch size from Figure 2. In fact, the optimal batch size only changes once in the figure, which makes me wonder if any scaling concluded from just a single change of optimal batch size could be an overclaim. The optimal batch size appears to jump from one value to another with no intermediate steps, and this single jump is used to derive a scaling law. This is problematic because it doesn't provide sufficient evidence to conclude a continuous relationship between the optimal batch size and the number of training steps. It's possible that the observed change is an artifact of the specific experimental setup or a local optimum, rather than a generalizable trend.

Minor weaknesses:
1. It would be good to do some sanity checks on downstream tasks: Does the optimal LR for reducing the pretraining loss also lead to good performance on downstream tasks?
2. Experiments are conducted on only one dataset, C4.

### Questions
I wonder if the authors could provide stronger empirical evidence to support the scaling of optimal LR and batch size proposed in the paper.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors investigate optimal learning rate, optimal batch size and critical batch size as the number of training training tokens increases.  The authors also investigate the effects of changing mode size within $\mu$P and find that optimal learning rate and batch size do not vary with model size.  The authors also investigate the sensitivity of the loss to learning rate as data and mode size change finding decreased sensitivity as data increases, but similar relationships within $\mu$P scaling.

### Strengths
Understanding how optimal learning rate and batch size scale as data scales is a very important and potentially impactful direction.  Understanding the diminishing returns of batch size significantly impact practitioner decisions regarding data parallelism.  Implications here can help go beyond compute optimal scaling paradigm that couples data and model size. In addition, strong understanding of relationships between hyperparameters can help reduce the need for expensive hyperparameter sweeps.

Aligning with existing theoretical models and providing the conjecture of eq. 1 can be useful modes of thinking to eventually provide a deeper understanding of these phenomena.

The scaling of batch size in data presented in Fig 2b and the sensitivity analysis of Fig 3 are both intriguing and useful for the community empirically.

### Weaknesses
Overall, the writing needs work. The empirics of this paper are not comprehensive enough to make such a strong claim on training regimes as 3 different growth regimes are being implied from 6 batch sizes and 8 token budgets.  We essentially have 6 trajectories from 8 points and the scaling does not even start immediately because of the "lost" epochs (mainly looking at Fig 1a here).  Given this, the origin of these explicit scaling rules need to be justified by existing work or theory in my opinion.  Content from A.2 should be much more prominent in the main paper.  In addition, the intro feels misleading; the contributions section makes this sound like a theoretical contribution and the specific growth proposed isn't justified by empirics alone.

Fig 2: a 2^2 times budget increase in budget increase of 2^5 is oberved from the sequence with only one step increase?  Extrapolating a general rule from one bump in $B_{\text{crit}}$ is not convincing. In my opinion, it is valuable to look into this, but it is a detrimental to quantitative claims from such little evidence.

Fig 1a pattern in batch size is not monotone, what's going on here?

### Questions
Fig 1a pattern in batch size is not monotone, what's going on here? 

Overall, my opinion of the paper is mixed but I lean towards acceptance.  I think much of the empirics are valuable to the community, but the paper is dragged down by overselling some weak empirics.  While I think it is completely reasonable that we don't have comprehensive answers to these questions (presumably from an onerous compute requirement), I'd like to see the claims tempered to mach the strength of the empirics.  I would recommend suggesting further work to investigate what looks like it could be a trend and provide some intuition on why the $T^{-0.5}$, constant and $ T^{0.5}$ regimes are a good conjecture, but hold off on a more forceful claim.

The content of A.2 and I think would be useful to integrate more directly in the main text.  

A more rigorous definition of critical batch size (line 107) would be useful.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the optimal scaling of LLMs in terms of the training hyperparameters, including learning rate $\eta$ and batch size $B$, and their optimal choices with respect to different data sizes $T$. In particular, they show that for different batch size $B$, the optimal $\eta$ has entirely different scaling with $T$. Furthermore, this paper also shows that the optimal batch size is positively correlated with $T$. Then, this paper also shows that the sensitivity with respect to $\eta$ is decreasing when using larger data size $T$. The results can help build a unified picture of the joint hyperparameter tunning of learning rate and batch size.

### Strengths
This paper develops extensive experiments on training LLMs with different choices of learning rates, batch sizes, model sizes, and data sizes. Then based on the experimental results, this paper identifies some patterns regarding the optimal hyperparameter configurations. In particular, this paper shows that

* the optimal learning rate has a different evolution in the limit of the data sizes when choosing different batch sizes. 
* the optimal batch size is approximately proportion to $\sqrt{T}$ when choosing optimal $\eta$.
* the critical batch size is approximately proportion to $T$ that will affect the optimal choice of learning rate.
* The learning sensitivity can be mitigated when using larger $T$.

Overall these findings provide unified results for guiding the hyperparameter choices when having different token budgets.

### Weaknesses
The major weakness of this paper is that it seems to be an experimental report that summarizes the key patterns observed from the experiments, while no further explanation and deeper analysis are conducted. Although there are extensive experimental results and the findings seem to be reliable, it remains unclear whether the findings can be generalized to other settings. I suggest the authors include some understanding of the empirical results, especially about why the learning rate can be much larger when  $T$ is large and we are using a large batch size.

Besides, I am not sure whether only considering $\mu P$ models is sufficient to understand the model with different sizes. It would be good to have more experiments and discussions on the models beyond the $\mu P$ ones.

The definition of $B_{crit}$ is a bit confusing. This may be a kind of clarity issue. The authors begin to mention $B_{crit}$ in the abstract and many places in the introduction. However, the reader cannot quickly get what's the formal definition of $B_{crit}$.

More details about the definition of the effective learning rate for Adam (line 428) should be provided.

### Questions
See the weakness section.

### Soundness
3

### Presentation
3

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
This paper investigates the optimal learning rate $\eta$ and batch size $B$ as a function of the data size $T$ in language model (LM) training, using the maximal update parametrization (muP). While muP focuses on hyperparameter transfer as model width increases (with other parameters fixed), this work centers on how hyperparameters evolve as $T$ grows, assuming a large but fixed model size (with results averaged across three model sizes). The authors show that the optimal $(\eta, B)$ can vary in complex ways with $T$; for example, there are regions where $\eta \propto 1/\sqrt{T}$ and others where $\eta \propto \sqrt{T}$. Overall, this work offers valuable insights into the optimal scaling of learning rate and batch size as data size increases.

### Strengths
In modern LM training, scaling both model size and data size is essential. Understanding how optimal hyperparameters scale with these factors is crucial. While muP provides insights into how hyperparameters scale with model size, less attention has been given to how they scale with data size. This work contributes meaningfully in this direction. Through a set of experiments, the paper offers intriguing insights into how optimal learning rate and batch size scale with increasing data size.

### Weaknesses
While this paper addresses an important problem and provides interesting insights, certain clarifications would help strengthen the presentation. Below are some suggestions for improvement:

- **Line 107:** It is mentioned that the "crucial batch size" is defined as the region where $\eta \propto \sqrt{B}$ breaks, and that this comes from Shallue et al. (2019). Could you please point to the specific section in Shallue et al. (2019) where this is discussed?
- **Line 122:** The notation $\epsilon = 1e^{-8}$ seems more like Python syntax. It would be clearer to revise this to $10^{-8}$.
- **Lines 188 and 294:** These lines refer to the "critical batch size" (as a function of data size) as the batch size that leads to the best validation error for a given data size, if I understand it correctly. This definition appears different from the one given in Line 107. Could you please clarify this discrepancy?
- **Lines 265-266:** The paper claims that $B^* \propto \sqrt{T}$. However, in Figure 2a, $B^*$ is either $2^{18}$ or $2^{20}$. How is this square root rule derived with only two data points?
- **Lines 294-296:** The claim that $B_{\text{crit}} \propto T$ is also unclear. Can you explain how this scaling is derived?

For all the claimed scaling laws, if possible, providing the observed data points along with using a scientific fitting method to derive the scaling laws would make the claims more convincing. 

I think the paper could be more clear if the speculated laws were better explained and justified.

### Questions
See above please.

### Soundness
2

### Presentation
2

### Contribution
2
