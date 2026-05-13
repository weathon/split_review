# Deconstructing What Makes a Good Optimizer for Autoregressive Language Models

- Decision: Accept
- Scores: 6, 8, 5, 5

## Abstract
Training language models becomes increasingly expensive with scale, prompting numerous attempts to improve optimization efficiency. Despite these efforts, the Adam optimizer remains the most widely used, due to a prevailing view that it is the most effective approach. We aim to compare several optimization algorithms, including SGD, Adafactor, Adam, and Lion, in the context of autoregressive language modeling across a range of model sizes, hyperparameters, and architecture variants. Our findings indicate that, except for SGD, these algorithms all perform comparably both in their optimal performance and also in terms of how they fare across a wide range of hyperparameter choices. Our results suggest to practitioners that the choice of optimizer can be guided by practical considerations like memory constraints and ease of implementation, as no single algorithm emerged as a clear winner in terms of performance or stability to hyperparameter misspecification.

Given our findings, we further dissect these approaches, examining two simplified versions of Adam: a) signed momentum (Signum)  which we see recovers both the performance and hyperparameter stability of Adam and b) Adalayer, a layerwise variant of Adam which we introduce to study Adam's preconditioning. Examining Adalayer leads us to the conclusion that the largest impact of Adam's preconditioning is restricted to the last layer and LayerNorm parameters, and, perhaps surprisingly, the remaining layers can be trained with SGD.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The study compares optimization algorithms, including SGD, Adafactor, Adam, Lion, and Sophia, for training language models of different sizes and architectures. Results show that, apart from SGD, all algorithms achieve similar performance and robustness to hyperparameter variations, suggesting practical considerations like memory and simplicity may guide optimizer choice. The researchers further dissect Signum and Adalayer to explore Adam’s adaptivity effects. They find that adaptivity on the last layer and LayerNorm parameters is essential for maintaining performance and stability, highlighting these elements as crucial for reliable training.

### Strengths
1. This paper is well-written and easy to understand. The experimental setups, discussion and interpretations of the results, and limitations of the methods are spelled out clearly. Though it might not have great novelty, I think the extensive study on hyperparameters on different optimizers is a valuable contribution to the LLM optimization community.  I enjoyed reading this paper.
2. Soundness of the result: As the authors mentioned in the paper, due to limits of computational resources, they only do 1D hyperparameter sweep, instead of 2D or even higher-order sweeps. This is fine for the major finding of the paper, which is a positive result, that the non-SGD mainstread optimizers are robust to choice of wide range of hyperparameters. Tuning remaining hyperparameters will definitely make the best performance of the current hyperparameter better. 
3. The finding that last layer and layernorm parameters need more  fine-grained (than layerwise) adaptivity is interesting. It shed lights on future research towards how Adam works and memory-efficient variant of Adam.

=============
I increased my score to 6 in reflection of the authors' additional experiments and clarifications.

### Weaknesses
Though I appreciate the extensive abalation on the LLM training experiments with different hyperparameters, the interpretation and the takeways of the experiments are vague and imprecise. I will elaborate it below.

1. The authors often use "Comparable" to describe the performance of models trained with different hyperparameters, which I could not find a precise definition in the paper. A validation loss of 3.07 may look close to 3.10 in terms of the relative ratio, but because the minimum of loss is not zero, the suboptimality between 3.07 and 3.10 maybe very significant, say if the minimum of population loss is 3.0 for 150M models. 

    As a result of imprecise definition, it is not clear what is the consequence of having comparable validation loss. Does it imply such gap between comparable losses are negligible so in practice if people use any hyper-parameters which lead to losses comparable to optimal validation loss in the first attempt, they are satisfied and do not need to spend more compute to rerun the experiments for the optimal optimal validation loss? If they would still like to rerun the experiment, no matter how small the gap in validation loss is, having a wide range of hyperparameters lead to comparable performance does not imply ease of hyperparameter tuning.

2. The authors write in line 327 "Takeaway: generally algorithms are more stable with respect to other hyperparameters and the possible gains in performance are relatively small compared to learning rate and momentum."

    I do not fully agree with this claim take-home message, given the experiments in the current draft. It seems that the authors get this conclusion just from the shape of the loss curves in those 1D hyperparameter sweep plots, instead of based on some quantative metrics. This could be problematic, because the range of some hyperparameter sweep in section 3.5 for hyperparameters other than learning rate and momentum seems to be smaller than that of learning rate and momentum. I am convinced that for sufficiently small WD and epsilon, the final validation losses are nearly the same. But for warmup, batch size, and $beta_2$, the range are smaller and thus I am not convinced. For example, the ratio between maximal and minimal batch sizes tried in the experiments are just 8, while the ratio is more than a thousand for learning rate. But given that the authors are training in the "chinchilla optimal" regime, which means the flops are fixed for different batch sizes, we should expect changing batch size can have similar effect to changing learning rates given the linear scaling rule for SGD [Goyal et al., 2017, Li er al.,2021] or square-root scaling rules for Adam [Malladi et al., 2022]. Therefore I suspect if the authors also vary batch size in a range of 1000 times, the impact of batch size would be much larger. (The authors also mention the 2D effect between batch size and learning rate in line 166)

    For pretraining percentage and $beta_2$, I encourage the authors to include more extreme values to support the claim that these hyperparameters do not matter. Instead showing them they do not matter in the current small range, it is more informative to show to the readers at what extreme values the loss starts to increase significantly. It is possible for warmup that we can completely get rid of it, and in this case it is useful to include that in the plot, just like weight decay.


**Soundness of finding in Section 3.6**: First the citation of Lemma 1 from [Balles\&Henni, 2018] seems to be quite different from what that is in the cited paper. Second, given the assumption in the Lemma 1, $\delta_{adam}$ seems just defined as $\frac{\mathbb{E}[m]}{\sqrt{\mathbb{E}[v^2]}}$, and the lemma implies that $\delta_{signum}$ must be $1$, which is not necessarily true, when sign of $m$ is negative. Maybe the authors are missing an absolute sign on $\mathbb{E}[m]$.

I also do not understand the argument between line 357-line 360 when $\beta_1=\beta_2$. The authors are essentially claiming for all coordinates and all time steps, the first and square root of second moment have the same ratio, which I do not see why it should be true. This prediction could be easily checked by just plotting the update magnitude per coordinate for Adam and see if they are roughly the same. If the authors allow a different scaling factor for every coordinates, then this claim becomes trivial because all first-order optimization algorithm using diagonal preconditioning have the same sign for each coordinate in its update and only differ by scaling.

### Questions
Despite the issues mentioned in the weakness, I have the following additional questions:

1. why the loss curve for signum are different in Figure 4, $\beta_1$ and Figure 5, $\beta_2$? Signum is defined as lion with $\beta_1=\beta_2$, if I remember correctly.

2. It would be interesting to add AdaSGD (Wang et al., 2020) into comparison, which only uses one more register than normal SGD, but has much better convergence, stability and tolerence to larger learning rate. AdaSGD can be viewed as a global version of adalayer, i.e., by viewing all the parameters as one layer. A very recent work by [Xie et al.,2024] shows that AdaSGD closes a large portion of the gap between SGD and Adam on GPT2. Replacing the SGD part in adalayer by AdaSGD might help us better understand the importance of adaptivity at different levels of granularity, under the unified framework of AdaLayer, or more generally Adam for arbitrary partition of parameter blocks.

3. typo. "in perplexity" in line 317 should be "in validation loss"?

I am willing to improve my score if the authors could address my concerns.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper conducts a thorough experimental evaluation of the performance and stability of common optimizers used in pre-training language models and uncovers interesting and previously unknown parameters in the transformer architecture that seemingly benefit more from the adaptivity of some of these optimizers.

### Strengths
* The thorough empirical evaluation fulfills a missing piece in the current literature of optimizers used in training language models, as most works in this literature stick to Adam.
* The experimental grids used for different experiments seem sufficient to draw robust conclusions. The authors incorporate models of different scales and explore 1 dimensional grid searches which is reasonable given the intense compute needs of such studies.
* This work uncovers an interesting phenomenon which attributes most of the adaptivity gains from Adam and similar algorithms to normalization and last layer's parameters.
* Considering stability of the training algorithms wrt hyperaparameters as opposed to the final performance is an important aspect since eventually a practitioner wouldn't be able to find the best possible hyperparameters but the hope would be to be able to easily food "good" set of hyperparameters.

### Weaknesses
 * One major drawback of this study could be the lack of a search over min learning rate at the end of cosine scheduling. As the authors have mentioned, learning rate plays the most important role among all these parameters. Recent studies (https://arxiv.org/abs/2410.05192) have shown that the final stage of training where the learning rate is decreased down to the minimum learning rate plays a crucial role in determining the final performance. Based on this, I'd be curious to know if certain algorithms would outperform others if the min learning rates were chosen carefully, since in that case individual momentums and how the history of gradients is dealt with could significantly differ among different algorithms. I would predict that using some optimizers, some larger learning rates would result in drastically better performances given that the minimum learning rate is small enough.

* I think implementing AdaFactor and AdaLayer would be more fruitful if parameters corresponding to different attention heads would be disentangled. Since the authors don't mention anything in this regard, I assume that they haven't implemented these algorithms to do so, but the nature of computations in attention heads would maybe benefit from adaptivity isolated to the attention head over all of the attention parameters. 

* Recently shampoo has gained significant popularity in training language models. It would be nice if the authors could incorporate shampoo among these optimizers to have a more complete story.

* It would be nice if the authors could elaborate on how optimality of different hyperparameters changes as the scale increases.

### Questions
* It is intuitive to me that adaptivity can help with optimization of LayerNorm as the affine parameters are applied in a coordinate-wise way, but I can't understand why the last layer (which I think is the embedding layer in the case of these models?) needs adaptivity. Can the authors please elaborate on this?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors argue that the Adam optimizer is the default choice for most practitioners training language models, and they seek to evaluate this belief by comparing Adam against other popular optimizers. Their findings show that, except for SGD, other optimizers perform on par with Adam. Following this, they explore what components contribute to Adam's success by evaluating two simplified versions of it: Signed Momentum and Adalayer.

### Strengths
The Authors show that most optimizers, other than SGD, can match Adam in stability and performance across varied model sizes and hyperparameter settings. Furthermore, it reveals that, to recover stability concerning learning rate and to maintain strong performance, adaptivity is essential, particularly in the last layer and LayerNorm parameters. This insight challenges the notion that Adam is uniquely suited for language model training.

### Weaknesses
 - Limited contribution: The main contribution of the paper is the finding that adaptivity on both the last layer and LayerNorm provides the necessary conditions for retaining performance and stability with respect to the learning rate.

- The paper could serve as a guide for those looking to choose an optimizer by comparing performance versus computational cost. However, after reading it, I didn’t feel I gained a clear insight to help decide on a better optimizer. In this sense, the paper has potential but feels incomplete.

### Questions
- line 165, are there only two hyperparameters in the problem? Because if there are more, then the optimal solution is only achievable by solving the N-D problem, with N being the number of hyperparameters.

- While I agree with the authors that cross evaluating all combinations of hyperparameters is intractable, why not use Bayesian optimization to find the best set of hyperparameters for each experiment?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper evaluates several optimizers, including SGD, Adam, Adafactor, Lion, and Sophia, in the context of large language models (LLMs). The results suggest that all optimizers, except for SGD, perform similarly regarding optimal performance and sensitivity to hyperparameters. The authors then further investigated two simplified versions of Adam: Signed Momentum and AdaLayer. They found that adaptivity in the LayerNorm and final layers is essential for achieving stable performance and learning rates.

### Strengths
- The evaluation of hyperparameters is thorough, and the documentation of experimental details is complete. Although it is limited to one-dimensional changes and does not capture the interplay between hyperparameters, the authors clearly state these limitations.

- The observation that adaptivity in the LayerNorm and final layers is necessary for LLMs is interesting.

### Weaknesses
 - My main concern with this paper is the significance of its contribution. The paper does not introduce new algorithms or provide insights into why some evaluated algorithms work or fail; it is limited to an empirical comparison. While this can still be valuable, I’m unsure if the paper adequately addresses the question posed in its title, “What Makes a Good Optimizer for Autoregressive Language Models.” It also does not seem to explain how the characteristics of “autoregressive” or “language” models interact with optimization or why the results might differ in other tasks and architectures. Additionally, the organization is somewhat confusing, and it’s unclear how the two parts of the paper relate.

- There are quite a few observations from each experiment, but it’s unclear what the main message or takeaway of the paper is. For example, it doesn’t clearly outline what practitioners should do, what future researchers in algorithm design should focus on, or provide any conceptual or theoretical insights that explain these observations. The paper could be significantly improved by clarifying the main questions it actually addresses and having a better discussion paragraph on what others could do with this information. 

- Citations of other optimizer-comparison papers could be more comprehensive. For instance, [Schmidt et al., 2020: *Descending through a Crowded Valley - Benchmarking Deep Learning Optimizers*] is an example that could be included.

### Questions
- Many follow-up works aim to improve Adam's performance or to develop memory- or compute-efficient versions of it. What is the rationale behind selecting these specific optimizers for comparison? Was the choice based on practical popularity, conceptual connections to Adam, or some other criteria?

- The plots comparing final validation loss (e.g., Figure 1) are presented so that each optimizer’s optimal learning rate aligns, with the x-axis showing multiples of this optimal learning rate. However, why should different optimizers be compared over the same scale of learning rate values? For example, SGD appears the most sensitive to changes in learning rate, but could this be due to it requiring a finer-grained learning rate grid for a fair comparison?

- A concurrent work, [Zhang et al. 2024: Adam-mini: Use Fewer Learning Rates To Gain More], also explores the concept of a coarser, "parameter-group" -wise learning rate for Adam, proposing it as the minimal level of adaptivity required. While it is of course not required to cite or evaluate concurrent work, a comparison with AdaLayer would be interesting given the similarity in approach. It would also be useful to see whether *Adam-mini* aligns with this paper’s findings on layer-specific adaptivity. This paper shows that adaptivity in the last layer and LayerNorm is necessary, yet limiting adaptivity to these layers alone still underperforms compared to Adam. So, what degree of adaptivity is "sufficient" to achieve Adam's full performance?

- Minor changes are needed on some of the later plots, as they are difficult to read due to small font sizes in the legends and axes, and they lose resolution when zoomed in. Please adjust these for clarity.

### Soundness
3

### Presentation
3

### Contribution
2
