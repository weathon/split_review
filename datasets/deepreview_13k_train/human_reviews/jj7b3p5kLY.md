# The AdEMAMix Optimizer: Better, Faster, Older

- Decision: Accept
- Scores: 6, 10, 5, 6, 6

## Abstract
Momentum based optimizers are central to a wide range of machine learning applications. These typically rely on an Exponential Moving Average (EMA) of gradients, which decays exponentially the present contribution of older gradients. This accounts for gradients being local linear approximations which lose their relevance as the iterate moves along the loss landscape. This work questions the use of a single EMA to accumulate past gradients and empirically demonstrates how this choice can be sub-optimal: a single EMA cannot simultaneously give a high weight to the immediate past, and a non-negligible weight to older gradients. Building on this observation, we propose AdEMAMix, a simple modification of the Adam optimizer with a mixture of two EMAs to better take advantage of past gradients. Our experiments on language modeling and image classification show---quite surprisingly---that gradients can stay relevant for tens of thousands of steps. They help to converge faster, and often to lower minima: e.g., a $1.3$B parameter AdEMAMix LLM trained on $101$B tokens performs comparably to an AdamW model trained on $197$B tokens ($+95\%$). Moreover, our method significantly slows-down model forgetting during training. Our work motivates further exploration of different types of functions to leverage past gradients, beyond EMAs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper propose a new optimizer called AdEMAMix, which add an additional EMA sequence to Adam. The intuition is to to keep a high sensitivity to recent gradients (using m1), while also incorporating information from older gradients (using m2).

### Strengths
The prerformance of AdaEMAMix is quite impressive. The writing is excellent. The ablation studies are thorough.

### Weaknesses
The motivation is rather vague. See below.

1. The motivation on the Rosenbrock function is rather weak.  Why do you consider the Rosenbrock function? How does it relate to LLM training?  Why do you think the implication on the Rosenbrock function can be transferred to LLM?  To me, there is a huge gap between these two.

2. Need more evidence that "beta1 = 0.9 is indeed suboptimal for LLMs". While I fully understand Figure 3, i still did not fully convinced that "LLM training really needs to use more historical gradients, in one way or another". More LLM-related evidence is needed to convince the that it is indeed a major bottleneck. Despite the impressive performance, the overall motivation still seems quite vague to me. I suggest the authors put more effort into designing more experiments for better motivation.

3. It is difficult to understand the highlighted sentence in the introduction: "While changing the direction of the slow momentum is difficult, any adjustment orthogonal to that direction is easy—which favors fast progress in sinuous canyon-like landscapes." I don't understand what you mean by "change the direction of the slow momentum" or "any adjustment orthogonal to that direction". Please explain more.  Also, the authors mentioned "canyon-like landscapes (in Rosenbork function)." but never connected it to LLM in the script. This also makes the motivation rather weak.

4. I don't quite understand how to read Figure 2. For instance: 

   -- in Figure 2 (a), is AdaEMAMix considered better than Adam? It is not clear whether we can draw such conclusion based on the figure. In my opinion, at least 10 x more iterations are needed to draw valid conclusions.

   -- in Figure 2 (c), did AdaEMAMix converge to the optimal solution? 

5. The proposed method boosts performance by using extra memory (to store an additional copy of momentum). Though many readers might regard it as a drawback,  I personally think such a trade-off is acceptable as long as the performance gain is significant.  Further, I think AdaEMAMix can be combined with some orthogonal methods to reduce memory. For instance, AdaEMAMix can be combined with the recent method Adam-mini [1] to reduce the memory for V. I suggest the authors try it out.


6. Some missing related works: [2] proves that vanilla Adam can converge under a wide range of beta1  = 0, 0.5, 0.9, 0.99, etc., as opposed to the divergence result in Reddi et al. 2018. This result lays down a preliminary foundation of this work.  Without the theoretical guarantee, it would be dangerous to play with beta1 of Adam.

### Questions
1. The motivation on the Rosenbrock function is rather weak.  Why do you consider the Rosenbrock function? How does it relate to LLM training?  Why do you think the implication on the Rosenbrock function can be transferred to LLM?  To me, there is a huge gap between these two.

2. Need more evidence that "beta1 = 0.9 is indeed suboptimal for LLMs". While I fully understand Figure 3, i still did not fully convinced that "LLM training really needs to use more historical gradients, in one way or another". More LLM-related evidence is needed to convince the that it is indeed a major bottleneck. Despite the impressive performance, the overall motivation still seems quite vague to me. I suggest the authors put more effort into designing more experiments for better motivation.

3. It is difficult to understand the highlighted sentence in the introduction: "While changing the direction of the slow momentum is difficult, any adjustment orthogonal to that direction is easy—which favors fast progress in sinuous canyon-like landscapes." I don't understand what you mean by "change the direction of the slow momentum" or "any adjustment orthogonal to that direction". Please explain more.  Also, the authors mentioned "canyon-like landscapes (in Rosenbork function)." but never connected it to LLM in the script. This also makes the motivation rather weak.

4. I don't quite understand how to read Figure 2. For instance: 

   -- in Figure 2 (a), is AdaEMAMix considered better than Adam? It is not clear whether we can draw such conclusion based on the figure. In my opinion, at least 10 x more iterations are needed to draw valid conclusions.

   -- in Figure 2 (c), did AdaEMAMix converge to the optimal solution? 

5. The proposed method boosts performance by using extra memory (to store an additional copy of momentum). Though many readers might regard it as a drawback,  I personally think such a trade-off is acceptable as long as the performance gain is significant.  Further, I think AdaEMAMix can be combined with some orthogonal methods to reduce memory. For instance, AdaEMAMix can be combined with the recent method Adam-mini [1] to reduce the memory for V. I suggest the authors try it out.



6. Some missing related works: [2] proves that vanilla Adam can converge under a wide range of beta1  = 0, 0.5, 0.9, 0.99, etc., as opposed to the divergence result in Reddi et al. 2018. This result lays down a preliminary foundation of this work.  Without the theoretical guarantee, it would be dangerous to play with beta1 of Adam.

[1] Zhang, Y., Chen, C., Li, Z., Ding, T., Wu, C., Ye, Y., ... & Sun, R. (2024). Adam-mini: Use fewer learning rates to gain more. *arXiv preprint arXiv:2406.16793*.

[2] Zhang, Y., Chen, C., Shi, N., Sun, R., & Luo, Z. Q. (2022). Adam can converge without any modification on update rules. *Advances in neural information processing systems*, *35*, 28386-28399.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper proposes AdEMAMix, a new optimizer which outperforms Adam on language model training and ViT training. Their empirical results show large benefits (~50% reduction) over Adam in the regime of noisy gradients i.e. small batch size or longer runs. The main idea behind the optimizer is to maintain two momentum terms and combine them to get the final movement direction. The coefficient of momentum and their combination are also dynamically adapted.

### Strengths
These are strong results on a very important problem. They also provide many optimizer ablations in the Appendix showing the robustness of their proposed optimizer.

### Weaknesses
Since many of the experiments are with small batch size it would have been interesting to explore the effect of weight averaging. For example, is it the case that weight averaging helps AdamW and AdEMAMix equally? Or not?

The authors state “While no answer to those questions is given in this work, we
provide a toy justification which indicates that large momentums can have a positive impact in
noise-free non-convex settings (see Fig. 2)—indicating the improvement of our approach is at least partially explainable without considering variance-reduction effects.” Is there empirical support for this in the LLM experiments? looking at Figure 17 the benefit seems to drop with increasing batch size. Note that the maximum batch size used here (512k) is smaller than that used for LLMs like Llama (4m), though I agree that the model size is also small here. Could the authors provide an experiment with 2m batch size to see the trend?

### Questions
The authors state “While no answer to those questions is given in this work, we
provide a toy justification which indicates that large momentums can have a positive impact in
noise-free non-convex settings (see Fig. 2)—indicating the improvement of our approach is at least partially explainable without considering variance-reduction effects.” Is there empirical support for this in the LLM experiments? looking at Figure 17 the benefit seems to drop with increasing batch size. Note that the maximum batch size used here (512k) is smaller than that used for LLMs like Llama (4m), though I agree that the model size is also small here. Could the authors provide an experiment with 2m batch size to see the trend?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to use an additional momentum buffer for the Adam optimizer. The motivation behind is that a single momentum buffer may not be able to utilize both past and current gradient information efficiently. To this end, one buffer with large momentum parameter $\beta$ is for slow-changing directions, and the other one with small $\beta$ is for fast adaptation to current gradient. Then, the two momentum buffers are mixed according to some fixed ratio ($\alpha$), and the rest of updates (i.e., pre-conditioning and weight-decay) follow those of AdamW. However, a large $\beta$ (for slow-changing momentum buffer) can cause training instabilities in the initial stage. To this end, the paper proposes to gradually increase this parameter until the target value is reached.  Then, experiments are performed on various language modelling tasks to show that the proposed algorithm is faster than AdamW given a fixed computation budget.

### Strengths
- The paper is well written and easy to follow. The experiments on the Rosenbrock function are convincing. There are some similar (loss landscape) models proposed recently to analyze learning rate schemes [1]. It maybe interesting to draw some theory/experimental connections in the case of momentum.   

- The experiments seem to be comprehensive covering different settings and tasks. The improvement over baseline is shown.

[1] Understanding Warmup-Stable-Decay Learning Rates: A River Valley Loss Landscape Perspective.

### Weaknesses
 - There are some additional hyperparameters introduced. Noticeably, it seems that $\alpha$ (that controls the mixing ratio)  is important for the algorithm. It would be important to study the sensitivity of the algorithm to this hyperparameter, given that it essentially controls the contribution of each momentum buffer to the current update. Specifically, it's unclear how the optimal value of $\alpha$ might vary across different tasks or datasets, and whether a single, fixed value can be reliably used in practice. Furthermore, the interaction between $\alpha$ and the two momentum parameters ($\beta_1$ and $\beta_2$) needs more investigation. It is possible that the optimal value of $\alpha$ is dependent on the values of $\beta_1$ and $\beta_2$, and this dependence should be explored.

- It would be better if some convergence guarantees of the algorithm can be provided even in the convex setting. For example, what is the relationship between the two momentum parameters that would guarantee convergence? It is not clear if there are any constraints on the values of $\beta_1$ and $\beta_2$ that would ensure the stability of the algorithm. The paper should also discuss the potential for divergence if these parameters are not chosen carefully. Furthermore, the paper should provide some insights into how the proposed method compares to other momentum-based optimization algorithms in terms of convergence rate and stability.

### Questions
Overall, I think the idea introduced in this paper is interesting. The paper can be improved if the above  weaknesses can be addressed.

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
This paper introduces AdEMAMix, an optimizer modifying Adam by incorporating a mixture of two Exponential Moving Averages (EMAs) to better leverage past gradients. Traditional Adam or AdamW optimizers rely on a single EMA to smooth gradients, which prioritizes recent gradients over older ones. However, the authors argue that this approach is suboptimal because it cannot simultaneously emphasize both recent and very old gradients. They conduct experiments across language (LLMs and Mamba) and vision (ViTs), showing that AdEMAMix outperforms and tends to forget training data slower than Adam.

### Strengths
- The paper is written and organized well. The optimizer is a simple modification to Adam and is conceptually easy to understand, with the algorithmic differences presented clearly.
- The authors extensively benchmark their proposed optimizer against Adam across architectures, dataset domains and hyperparameters.
- The spirit of AdEMAMix (having a ‘fast’ and ‘slow’ tracking of gradients) could be useful for mitigating forgetting in continual learning regimes, and is also shown to be relevant for current pretraining regimes where we often train much longer past eg. Chinchilla-optimal tokens.
- The authors have experiments which address one’s immediate concerns of the proposed optimizer, like hyperparameter tuning and memory overhead.

### Weaknesses
 - The proposed optimizer is not that novel, with several existing approaches in maintaining a longer horizon at the cost of memory which have been mentioned by authors; in particular, AggMo is essentially the same as AdEMAMix but applied to gradient descent, and the only difference in the setting of this work is applying the same principle to Adam. While the authors demonstrate empirical gains, the core idea of combining multiple momentum terms is not new, and the adaptation to Adam, while practically useful, is not a significant conceptual leap.
- Although the authors have performed experiments on the hyperparameter stability of AdEMAMix, they do introduce two new parameters beta_3 and alpha which require the use of schedulers for larger values to avoid divergence in early iterations, which may require more extensive tuning depending on the setting (eg. fast domain shifts). The need for schedulers, especially for beta_3 and alpha, introduces additional complexity in hyperparameter tuning, potentially making the optimizer less user-friendly and more sensitive to initialization, particularly in non-stationary settings. The authors should more thoroughly explore the interaction between these new parameters and the learning rate schedule.
- There is an additional memory overhead in the order of the model size to incorporate the second EMA, which the authors propose can be mitigated by setting beta_1 to be 0; however, these runs exhibit instabilities and sometimes large spikes in training especially at larger batch sizes (Figure 22). These spikes are generally undesirable even though the loss seems to ‘recover’, it is unclear to me that such spikes wouldn’t have more detrimental effects at larger scales. The instability observed when setting beta_1 to 0, particularly the large spikes in training loss, raises concerns about the robustness of this memory-saving approach. While the loss may recover, such fluctuations can be detrimental to the final model quality and may be indicative of underlying issues with the optimization process.

### Questions
1. Doesn’t the introduction of the additional beta_3 term potentially lead to an exploding step size if the incoming gradients are extremely small for many steps (the additional term in the numerator causes it to decay slower than the denominator in the update)? This isn’t unforeseeable in language model training, where the model could encounter multiple documents of rare tokens consecutively.
2. Do the authors have any experiments adding an EMA to other optimizers like Adafactor or Signum? Does the additional EMA always provide a gain, even with factored gradients?
3. Related to the previous question to address the memory overhead, does storing the slow-moving EMA in lower precision affect AdEMAMix performance?
4. Why was the optimal Adam learning rate being too high for AdEMAMix only manifesting at higher scales? Does this perhaps suggest AdEMAMix being more difficult to tune at larger scales? I’m wondering if there was there further investigation into this eg. Was there a certain part of the network that was destabilizing?
5. Did the authors use certain stabilization strategies, eg. QK-LayerNorm in your experiments? I’m wondering if this could be used for the author’s benefit, to stabilize training and offer greater ease in hyperparameter tuning. 
6. Why was alpha set to 2 and 1 for the switching Adam -> AdEMAMix experiments whereas the optimal values found in hyperparameter tuning were much higher?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a new optimization algorithm named AdEMAMix, a variant of Adam(W). They add an aditional moving average of gradients to the algorithm, on top of the existing first and second moment moment averages. In contrast to the traditional  $\beta_1 = 0.9 $ moving average typically used in Adam, the new moving average that updates much slower ( $\beta_3 = 0.9999 $). This additional moving average is then used with the traditional moving average to update the parameters, in a similar fashion to the Adam update. The authors argue this assists in preventing the “forgetting” of data and better uses past information than the traditional Adam update, and show strong empiracle performance on some vision and language settings.

### Strengths
The primary strength of this paper apperas to be an algorithm with strong empiracle performance. The authors conduct a thorough set of experiments and ablation in the setting of language modelling and vision using multiple architectures and configuarations. The idea is interesting and combines other ideas from the optimization literature (the Adam update, multiple momentum terms). I am particularly interested in the authors study of how the loss with respect to different batches changes over time depending on the order in which they where trained on. I think this direction is a promising area of research for understanding why some optimizers work better than others. The paper also contains many interesting questions that are of interest to the optimization community, although struggles to answer them (as does the rest of the field).

### Weaknesses
Some specific concerns are addressed in the questions section, but I think the fundamental challenge this paper faces is explaining why the algorithm is better. As is typical with deep learning optimizers, it would be too hard for any provable reason why the algorithm may be superior, but I do think some more effort in the paper could be focused on explaining why this is a good idea, especially with the increased memory requirments. As said in the strengths, I do like the amount of questions being asked but it would be nice to see if the answer to any of those questions is leading to a better optimizer. I think it’s possible that the “forgetting slower” direction may lead to an answer, but the majority of the experiments and argumentation for that is relegated to the appendix. While practically showing plots with better performance is good, from a scientific perspective understanding why that performance is better is important.

I’m slightly concernerd by the number of additional hyperparameters being introduced, which appear to be somewhat sensitive given the use of schedules for most of them. This one can make the algorithm more difficult to use in practice, and two runs the risk of having some lucky configurations for a given problem that works great but in general may not be great. I also feel that the additional memory requirment is a non trivial drawback. While it does not increase communication costs, just running in FSDP is not an easy option for many people who do not have easy access to multi-gpu servers.

A more cosmetic note, the figures in this work can lead to confusion at times. In multiple of the figures, there are three subplots where some and perhaps all are unrelated. In some cases, Some subplots are meant to be related, but use different colours for the same thing. This is also likely the reason many of the figure captions are  $\approx $ half a page. I think it would be valuable for the authors to give the plots another pass before any camera ready version. 

Overall despite being a potentially effective algorithm, I do feel that this paper is somewhat lacking in the motivation and justification of that. I would be open to raising my score in the discussion period but in it’s current state I’m not sure this work is ready. I would be interested in why the authors think this is a good idea and if there are better ways to show that to be the case. This does not need to be large experiments or rigorous theory. Well designed small experiments or simple derivations can be just as effective give an intuition to explain the performance on minimizing the loss or solving some problem existing optimizers have.

### Questions
- In figure 2, authors claim the proposed algorithm does not exhibit oscilations when compared to Adam. However, in both 2 (a) and 2 (c) it appears the AdEMAMix does in fact overshoot the minimizer, further than Adam at that. It looks to me that Adam with “default” hypterparamters appears to be the most stable of all the options. In general this is a little concerning as modern loss surfaces will be much more complex than the Rosenbrock function and these large oscilations/overshooting minimizers may be difficult to deal with or even diagnose. A seperate point on this figure but potentially contributing to my confusion is that the colour scheme in the three subplots is not consistent, if the authors could use a shared legend or something along those lines the results may be more interpretable.

- Given this method requires an additional buffer for the second EMA, this authors discuss it potentially being slower and mention that it is also possible to set  $\beta_1 $ to zero to compensate for this. I’m curious if any of the main experiments or the wall time comparison are using this  $\beta_1= 0 $. The hyperparameter configuration for figure 1 uses  $\beta_1 =0.9 $ so I would just  want ensure the wall time comparison is too to ensure figure 1 doesnt change substantially if the x axis is changed from steps to hours.

- What does older gradients being outdated mean? Is there any way to quantify this? Any intuition? All the data is weighted equally as far as minimizing the loss is concerned despite being at different points in the loss surface when you evaluate it. In general this whole idea of older/newer gradients being less/more relevant seems vaugly okay, but it would be nice to see a more scientific defintion or explanation. This doesn’t need to be totally rigorus and have proof but the current explanations seem hand-wavey and leads to far more questions than answers.

- Why not just use a normal non exponential moving average? You can have a uniformly weighted moving average that should not diverge, has this been tried?

- Is there any intuition for why  $\alpha $ is so large (in particlar  $\ge1 $?) Does this lead to a smaller step size being necessary? Can you also set it to zero until some point to fight early instability?

- Why is there no bias correction on  $m_2 $? I don’t really think it matters much much and most analysis ignores it but I’m curious why that decision was made in comparison to the typical Adam bias correction step.

- Regarding figure 4, while it does appear that the proposed algorithm “forgets” slightly less quickly than AdamW, is the claim that this is why it works better? It appears to me that the biggest predictor of “forgetting” is the injection time  $t_B $ rather than the algorithm, although perhaps if this minor difference is compounded across batches this leads to the superior performance of the algorithm. 

- In many experiments, notably figure 5, the x axis is limited to not show the optimization performance in earlier parts of training. Given that instability is cited as a challenge for this algorithm, to a point where complex schedules need to be used, I’m curious how unstable the well tuned algorithm is. Are there instability issues in the 0-200k range in figure 5 (b) with AdEMAMix from 0 for example?

- Recent analysis in [1] has shown Adam(W) should work well if the gradient and Hessian become correlated, and [2] provided a mechanism where that shows up in language models. Can the authors reconcile this with their modifications to the algorithm? It seems to me those works would suggest this new variant is not a great idea so I’m wondering if the authors have any thoughts for why that isn’t the case.

- Any idea why there is less good performance on imagenet 1k? It seems AdamW is performing better there although all the plots are fairly close.


[1]
Michael Crawshaw, Mingrui Liu, Francesco Orabona, Wei Zhang, Zhenxun Zhuang

Robustness to Unbounded Smoothness of Generalized SignSGD

https://openreview.net/forum?id=8oj_2Ypp0j

[2]
Frederik Kunstner, Robin Yadav, Alan Milligan, Mark Schmidt, Alberto Bietti

Heavy-Tailed Class Imbalance and Why Adam Outperforms Gradient Descent on Language Models

https://arxiv.org/abs/2402.19449

### Soundness
3

### Presentation
2

### Contribution
3
