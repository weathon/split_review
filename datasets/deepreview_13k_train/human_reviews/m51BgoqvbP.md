# Understanding Warmup-Stable-Decay Learning Rates: A River Valley Loss Landscape View

- Decision: Accept
- Scores: 6, 6, 10, 3, 5

## Abstract
Training language models currently requires pre-determining a fixed compute budget because the typical cosine learning rate schedule depends on the total number of steps. In contrast, the Warmup-Stable-Decay ($\wsd$) schedule uses a constant learning rate to produce a main branch of iterates that can in principle continue indefinitely without a pre-specified compute budget. Then, given any compute budget, one can branch out from the main branch at a proper time with a rapidly decaying learning rate to produce a strong model.
Empirically, $\wsd$ generates an intriguing, non-traditional loss curve: the loss remains elevated during the stable phase but sharply declines during the decay phase. 
Towards explaining this phenomenon, we conjecture that pretraining loss exhibits a \emph{river valley landscape}, which resembles a deep valley with a river at its bottom. Under this assumption, we show that during the stable phase, the iterate undergoes large oscillations due to the high learning rate, yet it progresses swiftly along the river. During the decay phase, the rapidly dropping learning rate minimizes the iterate's oscillations, moving it closer to the river and revealing true optimization progress. Therefore, the sustained high learning rate phase and fast decaying phase are responsible for progress in the river and the mountain directions, respectively, and are both critical. Our analysis predicts phenomenons consistent with empirical observations and shows that this landscape can naturally emerge from pretraining on a simple bi-gram dataset.
Inspired by the theory, we introduce $\wsds$, a variant of $\wsd$ that reuses previous checkpoints' decay phases and keeps only one main branch, where we resume from a decayed checkpoint. $\wsds$ empirically outperforms $\wsd$ and $\cycliccosine$ in obtaining multiple pretrained language model checkpoints across various compute budgets in a single run for parameters scaling from 0.1B to 1.2B.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work proposes a perspective on pretraining loss landscape drawing a metaphor to a river valley. The authors run toy experiments in support of this persepective, and present theoretical analysis as well. The authors present WD-S, a variant of Warmup-Stable-Decay, which they favorably compare against WSD and cosine-derived learning rate schedules across a number of model sizes.

### Strengths
The paper is well-written, with clear prose and clean figures. The elucidation of the river-valley loss landscape is intriguing and intuitive. The empirical results are good, though they could cover a broader range of experiment setups. The work is of potential interest to model-training practitioners who may desire to train large models without pre-specifying a compute budget.

### Weaknesses
The related works is deferred to the appendix. This makes it difficult to contextualize the work presented. If space is a concern, please still present a truncated related work section and defer a more extended discussion to the appendix. Of course the optimization literature is large but the most relevant works need to be discussed in the main text to provide context.

The originality of the technical contribution of this extension of WDS is marginal, though the empirical results suggest it is a useful one.

The loss curves presented in Fig 9 are very spiky, and the field of view is highly zoomed in. These should be re-run with a larger number of training runs and averaged, otherwise the result seems plausibly artifactual. Same for Figures 10 and 11.

### Questions
Nit:
Fig 7 occludes the caption of Fig 8. Please fix. Fig 7 captions includes 'textbf'

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper compares the optimization space of language models to a river, thereby demonstrating the effectiveness of the WSD method. Based on this method, a simplified version, WSD-S, is proposed, which reduces computational complexity by reusing checkpoint weights without compromising performance.

### Strengths
1. The optimization algorithms supported by theoretical foundations are a crucial research direction.
2. Despite involving complex theoretical proofs, the writing of the article remains clear and easy to understand. 
3. The proposed WSD-S performs no worse than WSD.

### Weaknesses
1. The theoretical proof in the paper relies on many assumptions, and the validity of these assumptions in complex large models is difficult to ascertain. For example, the paper assumes that the loss function is analytic, which seems unreliable in models like GPT2 that are filled with GELU functions. Specifically, while GELU is infinitely differentiable, the assumption that its Taylor series converges to the function is not always guaranteed, especially in the high-dimensional parameter space of large language models. The practical implications of this assumption need further investigation, as the behavior of GELU in these models may deviate from its theoretical properties.
2. The paper assumes that the optimization space of the loss function is a river and uses a toy model from Allen-Zhu's paper to verify this. However, neither the model assumptions in Zhu's paper nor the toy model in this paper are reflective of natural language situations, making it somewhat far-fetched to use such models to verify the existence of a river. The toy model's simplicity may not capture the complex interactions and non-linearities present in real-world language models, thus limiting the generalizability of the findings. The claim that the loss landscape resembles a river requires more robust empirical evidence using models trained on actual natural language data.
3. Compared to WSD, WSD-S does not offer any substantial innovative improvements, neither in terms of computational complexity savings nor in the final performance. The computational savings achieved by reusing checkpoint weights are not significant enough to justify the introduction of a new method. The performance gains are also marginal, raising questions about the practical utility of WSD-S over the original WSD method.

### Questions
1. Could the authors provide more evidence that the optimization space might be a river? 
2. Regarding the valley optimization space, do the authors have any ideas for developing more optimizers? For instance, how can more steps be focused on progressing along the river rather than crossing the river? Does Adam offer better descent speed compared to SGD in such a river valley? Additionally, I did not find the optimizer used by the authors mentioned, which should be specified in section 4.1.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
In this paper, the authors explore a learning rate schedule named WSD-S, an enhancement of the previously introduced WSD model, which consists of three phases: Warm-up, Stable, and Decay. They provide a robust theoretical and empirical analysis supporting the effectiveness of WSD and propose its simplification in the new WSD-S variant.

The theoretical analysis presented in the study sets the mathematical definition of what the authors refer to as the "river valley" loss landscape. They demonstrate (Theorems 2.2 and 2.3) that in such landscapes, a higher learning rate yields greater progress over the same number of gradient descent steps. For stochastic gradient descent scenarios, while progress along the 'river' remains constant, an additional 'hill' component of loss emerges. The rapidly decaying learning rate phase of WSD effectively addresses this hill component (Theorem 2.4), suggesting that WSD is particularly beneficial for river valley-type losses. The authors further argue that language modeling pre-training losses resemble these river valley losses, thereby explaining the previously observed advantages of WSD.

For continual training scenarios, the authors highlight the importance of the transition from stable to decay phases. WSD continues the the training from the pre-decay checkpoint but authors argue that the progress made during the rapid decay phase is crucial and needs to be carried over. With this hypothesis, they present a simplified WSD where the same checkpoint (instead of the pre-decay checkpoint) after the decay is continued to be trained. This approach is operationalized in the WSD-S schedule, which the empirical analysis suggests outperforms other schedules like cosine, cyclic-cosine, and WSD.

### Strengths
The paper is excellently written for the complex nature of the analysis presented in the study. The information is organized well and easy to follow. 

The authors have provided solid theoretical and empirical analysis to explain the effectiveness of the WSD and how simplification further benefits the optimization process.

### Weaknesses
None

### Questions
Minor edits:
Line 290: not sure if the eta_t is red on purpose
Line 399: missed a \ for textbf
Line 491: Figure 10 is difficult to read


Questions:
Line 236: What does it mean by “starting point w lies on the course of the river”? Does it mean that the starting point is on the manifold M or in some neighborhood of M?

Figure 8: Right bottom figure: The decay period is extended as the training progresses. If yes, why? Were there any experiments done to observe the effect of minimum LR (after the decay)? 

I wonder, if more decay phases can consistently keep the hill component smaller and ultimately make more progress?  Or is there any sweet spot of number decays that helps WSD-S to achieve the best results?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The purpose of the paper is two-fold, 1) understand the success of WSD by postulating that the loss plane is analogous to a river-valley. 2) They attempt to provide more theoretical justification and empirical support to this hypothesis, resulting in optimizing WSD to WSD-S under their assumptions.

### Strengths
They clearly articulate their idea of a river loss landscape and provide some theoretical guidance to establish it. They provide some benchmarks with various smaller models and evaluate the loss trajectories. They also provide an attempt to try and leverage their knowledge to propose WSD-S.

### Weaknesses
The main weaknesses observed are the following:
1. The assumption of a river valley isn't guaranteed and is not strongly supported. Additional theoretical or experimental results supporting this conclusion are necessary. Specifically, the paper lacks a rigorous exploration of the conditions under which this river-valley structure emerges. It's unclear if the observed loss landscape is a general property or an artifact of specific model architectures or training procedures. The theoretical justification should delve deeper into the properties of the Hessian and the optimization dynamics that lead to this structure, rather than just stating its existence under certain conditions. The empirical evidence should also be more comprehensive, including visualizations of the loss landscape under different conditions and for different models, to show the robustness of the river-valley structure.
2. Results are demonstrated on very small models, with identical architectures, identical batch-sizes, and relatively small corresponding datasets. All of which could influence the loss region. The use of small models limits the generalizability of the findings to larger, more complex models that are commonly used in practice. The identical architectures and batch sizes also raise concerns about whether the observed phenomena are specific to these settings. Furthermore, the relatively small datasets may not fully capture the complexity of real-world data, potentially leading to biased results that do not generalize to larger datasets.

### Questions
Have the authors examined different architectures, datasets, learning rates, or attempted to examine other possible explanations for the loss curve region?

Did you evaluate the models on benchmarks post-training?

Provided the hypothesis, why do we have divergence randomly during training of large models on stable plains?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper is composed of three main sections.  In the first section, they derive some analytical results for a specific type of loss landscape, which they call the “river valley landscape.”  The river valley landscape corresponds to a kind of loss function where the loss is reduced by moving in the direction of lowest curvature (the river direction), and there are steep hills on both sides of the river.  In such a situation, with a number of assumptions, it can be shown for gradient flow (continuous time), gradient descent (full batch gradients) and stochastic gradient descent (with approximate gradients), that the parameters will follow the river within a given bound.  Moreover, in the stochastic case, the loss is also bound by a term related to the variance of the gradients multiplied by the learning rate (which they associate with movement of the parameters up the hills).  A Warmup-Stable-Decay (WSD)-style schedule that has a decay at the end can, in theory, move along the river during the constant phases, and subsequently move down the hill directions during LR annealing.  The next section describes a bigram model where different initial tokens have different amounts of uncertainty in their following token.  The degree of uncertainty is shown (at an optimum) to correspond to the degree of curvature in the loss, suggesting that the “river” direction corresponds to learning more deterministic relationships, while the hill direction corresponds to more uncertain predictions.  Decayed LRs are shown to do relatively better on the uncertain bigrams in a small experiment.  Finally, the paper considers the case where multiple checkpoints are desired at intervals during training at a given model scale (e.g., to make a data-size-based scaling law).  If using the WSD schedule, the decaying happens in separate branches off the main sequence of checkpoints.  The paper makes the observation that even during these decaying phase, progress is made along the river direction.  This motivates the WSD-Simplified schedule (WSD-S), where rather than moving back to the pre-decay checkpoint in the main branch, we continue training directly after the decay phase.  This amounts to running cycles of WSD-style training.  Some experimental results dig into whether WSD-S is effective compared to WSD and to traditional schedules like Cosine decay or cyclic Cosine decay.

### Strengths
The WSD learning rate schedule has recently drawn a lot of attention in LLM training.  WSD allows us to obtain high-quality intermediate models by decaying in “branches” from checkpoints in the main training process.  Perhaps the key insight of the paper is that if using WSD, we must acknowledge that the decay portions are “wasting” a significant amount of compute in that the compute spent during these decay portions does not contribute toward the training of future checkpoints.  Prior work has recommended up to 20% of total steps in decaying, so decaying 5 times (e.g., to obtain a scaling law) could double the total compute spent training a model.  We can think of the proposed WSD-S approach as a philosophy: if you do decay, you should resume from *after* the decay, rather than from before it.  In this way, we seem to have the same amount of flexibility as WSD (with the exception that with WSD-S, we can’t run the decay in parallel with continuing training in the main branch, as you can with WSD).  Testing this philosophy is well-motivated, and of solid interest to the community.

The idea of specifying a loss landscape of a certain type (river-valley), and deriving different bounds on optimization given that landscape, and then determining whether different real-world training scenarios fit such landscapes, also seems well-motivated.
In terms of clarity, I found the figures fairly helpful in most cases.  For work like this, pictures of the LR schedules can tell the whole story and so Figure 2 was good, and the little arrows in Figure 2(b) (and even littler ones in Figure 10) were very helpful.  Figure 3 was helpful as well.  I also realized that after reading the paper, I wasn’t really confused about anything, so the work must have been explained somewhat clearly.

I thought the material on decay after loss spikes was interesting and fairly important.

### Weaknesses
The paper in its current form seems incomplete in many ways. For one, the paper has not undergone a proper proofreading/editing/review process. This makes it much harder for the reviewers to assess the quality of the work – I felt like I was being asked to help prepare an early draft of a paper written by my co-author, rather than reviewing a paper that is already ready for submission. Some typos are probably just honest mistakes, e.g., repeatedly spelling “decaying” as “decayping” – but if you pasted the paper text into ChatGPT, or ran a simple spell checker, it would find many of these typos! It’s unsettling to see typos in the abstract (!) “one can branch out from the main branch at a proper at any time”, in main theorems “with the learning decaying learning rate schedule”, in Figure captions ‘Figure 7: textbfReproducing [sic] the Nontraditional Loss Curve.” There are missing LaTeX references (I assume) “We will first motivate the decaying function we choose ?? [sic] using a simple example”. Figure 7 is blocking part of the caption of Figure 6. I feel like all of these would have been picked up if a co-author had simply reviewed the paper prior to submission (and writing could have been improved in general with such review).

Moreover, the paper has a very non-traditional style: the main body of the paper is missing Related Work, Discussion, and Conclusion sections (although there is Related Work in the appendix, which reviewers are not required to read). This makes it difficult to contextualize these results compared to prior work (missing the Related Work), and understand the key insights that we draw from the experiments and theoretical sections (missing Discussion/Conclusion). For example, does this paper present a negative result? I.e., is WSD just as good as WSD-S, even if we count the decay portions as part of the overall compute? This seems to be what Figure 10 is showing. It would be interesting to learn (from a conclusion) whether the authors feel the same way.

There is also some missing discussion of related work. E.g., consider the following passage: “We find that the loss interpolation between parameters before and after each training iteration’s update is roughly convex with a minimum (valley floor) in between for most of the training. Based on this and other metrics, we deduce that for most of the training update steps, SGD moves in valley like regions of the loss surface by jumping from one valley wall to another at a height above the valley floor. This ’bouncing between walls at a height’ mechanism helps SGD traverse larger distance … this exploration above the valley floor allows SGD to quickly travel far away from the initialization point”. Actually, this passage is not from the current paper, but from Xing et al., “A walk with SGD” (2018) (arXiv: 1802.08770v4), which is not cited here. Contextualizing the findings of Xing et al (and other works) within the main body of the paper is essential.

I think another weakness is that, of the three main sections of the paper, none of them really went into enough depth to convince me of the main arguments.

For the theoretical section, it’s not clear, of all the many assumptions, which apply to modern LLM training. Like, is the 4x “eigengap” commonly found? How important is it? Also, what is the point of departure here from other theoretical work in SGD, for example from Bottou et al, “Optimization methods for large-scale machine learning”. SIAM review, 60(2):223–311, 2018? The benefits of decaying LRs has a long history in optimization, and decay has previosly been motivated by similar considerations to those used here (moving from initial conditions early, reducing stochastic noise later on). If you frame your findings in terms of this earlier work, the contrast can help us understand the benefits of your analysis. Like, maybe the stochastic noise plays a greater role if the loss landscape has a river-valley form (motivating greater decay than we would use otherwise), and we can see this in contrast to what we’d see without all the river valley assumptions. These other works often derive a bound from the global optimum, but here we seem to be bounded from a point x “further down the river” – what is the significance of this? This could indeed be a paper all in itself.

Moreover, I am not convinced by the probes in Figure 5, given that the two points are sampled 5 *billion* tokens apart. Does this mean that the river has no bends? Like, if you interpolated between two points in Figure 3, you can clearly see that you would typically travel up the hill and back down the other side. Does this invalidate the river analogy? If not, how does Figure 5 “validate” it? Figure 2(a) says the iterate will “oscillate” between the hillsides – why not check this over fewer than 5 billion tokens? Plotting Figure 5(a) at a single pair of checkpoints is not sufficiently rigorous, from my perspective.

The empirical verification in Section 3 lacks a lot of details – “we first train a toy model” – but what is this model? A neural network? Next we fine-tune a pre-trained GPT2 model, but of what size? Why is it pre-trained? What are the objectives of doing this? There are no ablations here, nothing is varied and repeated, there are no error bars. Basically, it’s not clear why the design choices were made for these experiments, and what the objectives were, and what the implications of these results really are.

For Section 4, my main objection is that I suspect the average learning rate to be a confounder. Think of your Theorem 5: progress throughout training is partly controlled by the sum of the step sizes (this theorem is for decay, but it’s true during the stable phase as well). Then look at Figure 9: WSD-S has a higher average LR than Cyclic-Cosine. Would cyclic cosine work better than WSD-S if we simply increased the LR slightly? The paper says, “We hypothesize that a model trained with a small learning rate for too long, as with Cosine, is implicitly hurt compared to a model trained with a large learning rate for the majority of the run, as with WSD or WSD-S.” Exactly! So why not train Cosine with a higher LR?

### Questions
Why doesn’t the blue line go as far as the red line in the “0.3B Parameters” plot in Figure 10?  The red line seems to stop short of 50,000.

The introduction says, “WSD-S leads to a better validation loss than WSD under the same compute budgets due to the re-use of the decay period”.  Is Figure 10 validation loss? (it doesn’t say).  For the 0.6B parameter model trained to 50,000 steps, don’t they obtain basically the same loss at the end?  And by definition, they always have the same loss on the first checkpoint, right?  I mean, with the loss spikes seeming to affect the intermediate results, can we really conclude that WSD-S gets better validation loss under the same compute budgets?  Do we need to soften this statement in the introduction?

Do you think WSD-S, since it has a slightly lower summed LR than WSD (lower total LR “area”) might actually do better than WSD if we increased the peak LR slightly?  Do you think Cyclic-Cosine could also improve if we increased the peak LR?

### Soundness
2

### Presentation
2

### Contribution
2
