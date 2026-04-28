# u-$\mu$P: The Unit-Scaled Maximal Update Parametrization

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
The Maximal Update Parametrization (\mup) aims to make the optimal hyperparameters (HPs) of a model independent of its size, allowing them to be swept using a cheap proxy model rather than the full-size target model.
We present a new scheme, \umup, which improves upon \mup\ by combining it with Unit Scaling, a method for designing models that makes them easy to train in low-precision.
The two techniques have a natural affinity: \mup\ ensures that the scale of activations is independent of model size, and Unit Scaling ensures that activations, weights and gradients begin training with a scale of one.
This synthesis opens the door to a simpler scheme, whose default values are near-optimal. This in turn facilitates a more efficient sweeping strategy, with \umup\ models reaching a loss that is equal to or lower than comparable \mup\ models and working out-of-the-box in FP8.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a combination of the maximal update parametrization (muP) and unit scaling, coined u-muP. It brings together the two main ideas of 1) hyperparameter transfer and 2) the ideal principle of unit variance of activations, weights, and gradients. The authors implement this idea with decoder language models, showing both the transfer of parameters, the performance, as well as scaling to 7B models and FP8.

### Strengths
I am very positive about this paper -- I think it is both a valuable contribution and an important direction for future work, as it is both practically and theoretically motivated and I agree with the concept of unit scale. I also appreciate the demonstration of failed HP transfer of muP for typical Llama-like models, which I have experienced myself. The experiments are very broad and consider not only HP transfer, but dependence between parameters, numerical properties during training, FP8 and 7B scale with downstream evaluations. Certainly, the 7B experiments are most convincing. 

Some side note: As the authors note themselves (so I do not see it as a weakness, but future work), unit scaling does not give guarantees for the behavior during training, so I would be particularly interested to see this method combined with models like the outlier protected block (He et al., NeurIPS 2024 https://arxiv.org/pdf/2405.19279), investigating the outliers during training, for which this model might enable even better/easier FP8 training.

### Weaknesses
While I am an advocate for the paper, I want to raise some points/irregularities that came to my mind while reading and I think would need to be addressed, both to improve the work, its insights or my score. They concern, in particular, the experimental setups:

- Why not use a larger dataset for the HP transfer experiments? I understand it is to compare to the setup of Yang et al., but I am asking because it is really small compared to modern training settings. For instance, in Fig. 4, 34k steps imply ~4 epochs over the dataset? Similarly, a warmup of 2000 steps is relatively long compared to the overall steps? In comparison, the large scale training only used 500 warmup steps.
- When sweeping the LR, is the final LR always changed to 10% of the chosen rate? The final LR should either be swept independently or kept fixed to a low enough value for a proper LR cooldown, otherwise this can skew results.
- Comparison to SP, in particular 7B: If understand correctly, you use the exact same model for SP and u-muP. Does this mean you also use the tweaks (non-trainable RMSNorm, independent WD) for the SP model? Since the LR setup for Llama was chosen without those changes enabled, I think a fair comparison would be to use the original model, in particular with coupled weight decay.

I particularly think the point on the comparison to SP is very important — the main focus of the paper is on a comparison to muP, but there is the simple reason of being more convincing to adopt the method because of its performance and not just its elegance (e.g. for practitioners, many of which haven’t adopted muP yet either).

Relation to prior work: I think it would be important to add references and discussions to the field of signal propagation in neural networks, e.g. Noci et al. https://arxiv.org/pdf/2206.03126 and the many references within their related work.

### Questions
I have raised questions/weaknesses in the section above, which I would be happy to discuss and eventually raise my score. Beyond, I am curious what the authors think about HP transfer to larger scale and longer training. This connects to the first point above. For instance, there seems to be a slight shift of the optimal LR to the right when growing batch sizes (Fig. 4 middle). This could be problematic for planning large scale runs (where batch sizes have become enormous). Similarly, do you have concerns about transferring to much longer training lengths (e.g. more than 1M steps for Llama 3, unfeasible for LR sweeps). To be clear: I do not expect the authors to have a solution for this, I am just curious about their thoughts.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper combines two approaches—(1) mup and (2) unit-scale—to enable hyperparameter transfer for low-precision training (FP8). The paper is overall well-written and contains many details and ablations.

I do like this direction of research, and low-precision training is important for speeding up training, lowering training costs, and enabling more research.

However, I have several concerns regarding the paper listed below. I am happy to raise the score if these are addressed properly.



---- update ----

I am delighted with the promised change. in particular, down play the batch, depth scaling results; detailed discussion of embedding scaling and potential limitation; 

i raised my score to 6 ( i would give 7 if that option is available).

### Strengths
I think this is important research direction that has many practical values. The paper contains a lot of useful details (many of them are in  the appendix). I really appreciate that. 

The embedding scaling rule seems interesting and novel but also controversal.

### Weaknesses
 - Transfer across batch, depth, training steps is not convincing (Fig. 4).
 - (important) The learning rate in the embedding seems unnatural and contradicts the original mup paper. In the infinite-width setting, the update will go to zero, and the input layer is frozen; this doesn't seem right to me.
 - (Important) Everett also studies hyperparameter transfer thoroughly and is highly related to this paper. Please make a more comprehensive comparison. In particular, the mean-field parameterization is very close to the unit-scale proposed here. Please clarify what's new and what the differences are.
- Citations to previous mean-field papers are needed and should have been discussed.
- The results of the paper seem to contradict some results of the original mup paper. I would love to see a table/section summarizing them + an explanation of why the original mup setup is not right.
- I  also want to see a wall clock time comparison between fp-8 vs. bf-16 runs at different scales, which is why we want to use fp-8. In addition, it may be good to know how much memory can be saved.

### Questions
Independent weight decay vs coupled weight decay? need more clarification. I am not sure which one to use. Lingle proposes to use wd=0.1 * LR, while og mup, wortsman and here propose scale-independent weight decay.  

Fig 2. Are the legends regarding C_embed correct? It says C_embed = 1 is better than C_embed  = 1/ root(fan_out). 

The uses of non-trainable rmsnorm "scales" seem non-standard to me, have you done ablations by yourself?

### Soundness
2

### Presentation
3

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
This work proposed u-$\mu P$, which combines $\mu P$ with unit scaling to facilitate hyper-parameters (HPs) search. u-$\mu P$ does not require a base shape and the HPs have less interdependency. Moreover,  u-$\mu P$ empirically maintains unit scaling for the activations, weights and gradients, which enables FP8 low-precision training.

### Strengths
The paper is well-written and the idea is clearly delivered. The authors have conducted extensive experiments to compare the performance of the proposed methods with the original $\mu P$.

### Weaknesses
 * As the authors discussed, this work lacks a comparison with other proposed methods (e.g., Large et al., 2024).
* There is no theoretical justification of why choosing a different scaling for the embedding learning rate.

* The lack of comparison with other methods, such as Modula, makes it difficult to assess the relative merits of u-$\mu P$. While the authors mention Modula, a direct comparison would be beneficial to understand the advantages and disadvantages of each approach. The current work only provides an empirical comparison with the original $\mu P$, which is insufficient to position the method within the broader landscape of hyperparameter optimization techniques.

* The choice of a different learning rate for the embedding layer lacks a clear theoretical basis. While the authors provide empirical evidence for its effectiveness, a deeper theoretical understanding of why this specific scaling is necessary or beneficial is missing. This makes the method less robust and potentially harder to generalize to other architectures or datasets. It is not clear if this scaling is a heuristic or if there is a more fundamental reason behind it.

### Questions
* Maybe the authors already mentioned this, but I wonder how is the performance of u-$\mu P$ with embedding LR =1 compared with $\mu P$?

* I am curious about how whether u-$\mu P$ can be applied to non-transformer models and how to select the HPs (as in line 304-316) in this case? I am not asking for additional experiments, any useful insights or discussion would be appreciated.

* Typo in Figure2 right panel: the solid and dotted lines are swapped?

### Soundness
3

### Presentation
3

### Contribution
3
