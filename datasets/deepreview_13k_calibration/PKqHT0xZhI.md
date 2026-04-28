# Efficient Ensembles Improve Training Data Attribution

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 5, 8, 6, 3

## Abstract
Training data attribution (TDA) methods aim to quantify the influence of individual training data points on the model predictions, with broad applications in data-centric AI, such as mislabel detection, data selection, and copyright compensation. However, existing methods in this field, which can be categorized as \emph{retraining-based} and \emph{gradient-based}, have struggled with the trade-off between computational efficiency and attribution efficacy. Retraining-based methods can accurately attribute complex non-convex models but are computationally prohibitive, while gradient-based methods are efficient but often fail for non-convex models. Recent research has shown that augmenting gradient-based methods with ensembles of multiple independently trained models can achieve significantly better attribution efficacy. However, this approach remains impractical for very large-scale applications.

In this work, we discover that expensive, fully independent training is unnecessary for ensembling the gradient-based methods, and we propose two efficient ensemble strategies,  \methodA\ and \methodB, alternative to naive independent ensemble. These strategies significantly reduce training time (up to 80\%), serving time (up to 60\%), and space cost (up to 80\%) while maintaining similar attribution efficacy to the naive independent ensemble. Our extensive experimental results demonstrate that the proposed strategies are effective across multiple TDA methods on diverse datasets and models, including generative settings, significantly advancing the Pareto frontier of TDA methods with better computational efficiency and attribution efficacy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A number of training data attribution (TDA) methods have been developed recently to quantify how training data points influence particular model predictions. However, they have a clear trade-off between computational complexity and accuracy. The authors propose to improve the accuracy of “gradient-based methods” (that are computationally efficient) to improve this trade-off. In particular, they attempt to replace naive ensembling methods with LoRA and Dropout ensembling and show results.

### Strengths
The authors have motivated their problem well and seen the need for developing better ensembling methods based on simple techniques as opposed to naive ensembling which could be retraining or fine-tuning  models fully. They base their development on the TRAK approach which proposed ensembling after using random projections of gradients to counter the computational expense of determining attribution scores.

The authors also differentiate between training, serving and space cost. They also use some practical tricks such as in Iines 236-239 where they only use the dropout models to calculate Q values whereas their randomly projected gradients are determined based on the original models.

Improvements are seen in performances and good utility is demonstrated for the dropout case. I did not check the theory but it sounds reasonable at least in Case 1.

### Weaknesses
These are some comments that the authors may consider:
1. While the methods do improve performance, they do not help scale TRAK to larger models since TRAK approach has a huge storage cost. This also seems to lead the authors to test with smallish models. The core issue is that the method requires storing gradients or their projections for each training point, which becomes prohibitive for large datasets and models. The authors should explicitly acknowledge that their method does not address the fundamental scaling issue of TRAK regarding memory footprint.
2. It’s not clear how the LORA approach compares with the dropout approach. Is there any way to compare them with each other? Also the LORA has only been demonstrated for the Music Transformer model. A more direct comparison, perhaps using a consistent evaluation metric across both methods on the same model architectures and datasets, would be beneficial. The current presentation makes it difficult to assess the relative strengths and weaknesses of each ensembling technique. Furthermore, the limited scope of LORA experiments raises concerns about its general applicability.
3. If the authors really want to demonstrate this with large scale generative models, they should consider language transformer models (even smallish ones like 1B or so parameters). I can understand the practical infrastructure difficulties but this must be spelled out. What are the bottlenecks for a larger scale evaluation? The lack of experiments on larger language models is a significant limitation. The authors should discuss the computational bottlenecks that prevent them from evaluating their method on such models, such as memory constraints for storing gradients and the computational cost of ensembling. This discussion should include specific details regarding the hardware and software limitations they encountered.
4. The limitations of the approach must be spelled out (increase in space cost). You can consider adding this in a dedicated section on limitations of the work. The authors need to clearly state the trade-offs of their approach, particularly the increased memory overhead due to storing multiple model weights or intermediate representations for ensembling. A dedicated section would provide a more comprehensive and transparent assessment of the method.
5. Showing some qualitative examples that show the test data and attributions for the naive and the proposed ensemble methods will be useful.

### Questions
Please see weaknesses.

### Soundness
3

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
4

### Summary
The authors focus on improving gradient-based methods for data-centric learning. They propose two ensemble strategies as efficient alternatives to the naive independent ensemble approach. Experiments on public datasets are conducted to demonstrate the efficacy and efficiency of the proposed strategies.

### Strengths
1. This paper is well-organized, with a clear and logical structure that makes it easy to follow and understand.

2. The proposed strategies are technically sound and could significantly reduce the training time and space costs compared to the naive independent ensemble method.

### Weaknesses
1. The authors proposed two strategies, DROPOUT ENSEMBLE and LORA ENSEMBLE. However, it is unclear which might perform better and their respective advantages in different scenarios.
    
2. Given that the computational time of TracIn [1] is also quite low, the comparative advantages of DROPOUT ENSEMBLE over TracIn as well as the reasons are not well stated.
    
3. The idea of LORA ENSEMBLE appears similar to GEX [2]. It could be helpful to include GEX in the related work section and discuss the differences and potential advantages of LORA ENSEMBLE.
    
4. There are no experiments provided to evaluate the proposed strategies on data-centric tasks (for example, mislabel detection). Understanding their performance in this context would be valuable.

5. There are some typos. For example,

- Line 183 on Page 4: indepedently
- Line 252 on Page 5: fowrad-only
- Legends in Fig. 4: Naive Ensmeble

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
It has been previously observed that combining training data attribution scores from independently trained models produces better attributions. However, training and deploying an ensemble of models can be very expensive. In this work, the authors propose the use of dropout and fine tuning (specifically through LORAs) to create ensemble members in a way that incurs far less computation at training time.

The authors demonstrate empirically that this provides an improvement in performance and training time tradeoffs on a variety of models and tasks and over a variety of training data attribution methods. They then perform a theoretical analysis of their method to identify regimes in which their method is expected to perform well.

### Strengths
The method is straightforward to understand and implement since it relies primarily on the use of widely available modules (e.g. dropout). The method is flexible and can be applied across a wide variety of settings. The authors demonstrate that their method can perform attribution at a similar level to the naive independent ensemble method with far less training.

### Weaknesses
If I understand the method correctly, it should generally be expected that, while training time significantly improves using this method, serving time would be more expensive. If this is the case then it should be made clearer in the paper, ideally with some quantification of this cost.

While the authors perform experiments across a variety of methods, models, tasks, and metrics, the full grid of possible evaluations is not complete. For example, a comparison between the lora based and dropout based method appears to be missing from the main body of the paper.

### Questions
On line 126-127 you state that training and test sets are identical in the supervised case. However from my experience a validation split is usually excluded from the training set. Could you clarify?

You show the trade off between performance and training time between their method and independently trained ensembles. Could you also discuss the trade offs between serving-time and performance when compared with independently trained ensembles?

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
The paper is about training data attribution (TDA) and specifically gradient-based methods like influence functions and TRAK. These tend to benefit from ensembling scores across multiple models, which has the downside of requiring i) performing multiple training runs, ii) storing multiple sets of weights, and iii) performing the same computation multiple times. The authors propose two ideas to reduce these costs: 1) averaging TDA values calculated using multiple dropout-masked models, and 2) averaging scores across multiple LORA fine-tuned models. 

Both techniques offer some type of averaging effect that empirically improves the scores, similar to the standard ensembling approach, but potentially with reduced training time and storage space requirements. For the dropout idea, the authors also propose a trick to reduce computation time. The comparisons with standard ensembling are a bit mixed, but these are interesting ideas.

### Strengths
- The problem setting and related work is well written and easy to follow.
- The two main ideas presented here are reasonable and offer solid options to reduce training time and storage space, which is important for large-scale models. 
- For the dropout ensemble, the trick for TRAK of only using dropout masking for the $Q$ terms was a nice idea to further reduce computation/serving time (end of section 3.3). Based on the results in Figure 5, it seems to work well in practice (although I have a question about that below).
- The main results for the dropout ensemble show that it introduces helpful variability, which given enough masks can provide a similar effect to ensembling independently trained models (Figure 3). Although the TRAK alternatives (influence functions, grad-dot, grad-cos) are much worse in an absolute sense, it's nice to see that they benefit from the dropout ensemble as well (Figure 4).
- The LORA ensemble results mostly seem encouraging as well, reflecting that a little extra training cost + a few more parameters can yield large LDS improvements. I have a couple questions about these results as well, but this is enough to establish LORA ensembling as a viable approach.
- The theory is a nice addition, but perhaps a bit disconnected because the authors don't characterize the salient distributional properties in their experiment (e.g., how correlated scores are within a dropout ensemble vs between independent models).

### Weaknesses
Some assorted observations from throughout the paper:

- I can't tell how the authors justify the performance improvements quoted in the abstract and later in the paper. Can they make this logic explicit in the paper? It seems unlikely they generalize across settings or apply to both ensembling methods, and I don't know if the authors are controlling for accuracy (LDS) when making these claims.

- The authors mention one baseline that they fail to compare to, which is using multiple checkpoints from a single training run. I recognize that it would be cumbersome to add at this point, and that tuning that baseline might be necessary (e.g., which epochs to use), but it would have been nice to include because it reduces training time in a similar fashion. Can you explain why it was not included?

- From the abstract and introduction, I got the impression the authors might completely eliminate the need for multiple training runs. Unfortunately this is not the case, both methods still rely on multiple independently trained models to achieve similar performance to naive ensembling. Do you think your results convincingly show that we can't get good enough LDS scores with a single training run, even with a high number of dropout masks or LORA adapters? This seems implied by the asymptoting performance as the number of dropout masks/LORA fine-tunes grows, and might merit some discussion.

- The Figure 3 results seem to reflect that for a given serving cost, dropout ensembling is worse than naive ensembling: we can see this through the first orange point vs the fourth blue point. These figures are actually somewhat deceptive because their x-axis represents the number of independently trained models, rather than serving time or FLOPs. They effectively plott accuracy vs training time, which is the most favorable comparison for this method because it squeezes performance out of each independently trained model. Figure 5 shows serving time comparisons but omits a curve for naive ensembling... I believe the authors should be more transparent about this result, for example by including all the same plots shown for LORA ensembling (even if it's only in the appendix).

- In Figure 5, it looks like 3/4 plots show something quite surprising: that for a given number of dropout masks, their serving optimization for TRAK achieves not just lower serving time but *better LDS scores*? That's surprising and might merit some discussion. What does that tell us about which parts of TRAK truly requiring ensembling, and do you have intuition for why?

- For the LORA ensemble, I don't understand how it lets you reduce serving time - how would you get around having to backprop through the network for each set of adapters? The authors mention this on line 268 with no explanation, and reduced serving time seems to be reflected in Figure 6b. This seems like an important aspect of the method to describe in the main text.

- Why are most of the experiments performed on toy datasets? Would it have been harder to use CIFAR-10 instead of CIFAR-2? I noticed there are some more realistic settings in appendix K, why aren't they included in the main text? (For the results related to dropout ensembling, these last results seem to have the same issue I mentioned above with worse LDS for equal serving time.)

- Why are there no comparisons between dropout masks and LORA ensembling? This seems important to include.

- For the theory, it would have been nice to characterize the salient distributional properties in your experiments. For example, I believe the finding that you can't get arbitrarily good LDS scores with a large number of dropout masks and a single model reflects that one of the assumptions is incorrect (the one on line 483).

### Questions
While reading the paper I found it hard to reason about the relative importance of training, serving and storage costs, and I wonder if it would help to specify which setting you're targeting. For example, if it's large LMs or diffusion generate models, which costs matter most? Major LM providers are arguably more concerned about serving costs than training costs, so a discussion of your intended setting seems important. What both your methods have in common is that they reduce training and storage costs, but I'm not sure they provide a Pareto improvement in the accuracy / serving-time tradeoff.

For dropout ensembling, how important is it that the original model was trained with dropout?

For LORA ensembling, do you think you could get meaningful LDS improvements and reduced serving costs by fine-tuning only a few layers, perhaps late in the network?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes ways to efficiently simulate building ensembles of models from scratch using dropout and lora for the problem of training data attribution (TDA). Through empirical studies they show the efficacy  of their approach (lower LDS for similar time) over from scratch training. The paper also provides some theoretical analysis to justify their approach in terms of lower squared error loss.

### Strengths
+ Easy to peruse
+ Covers related work reasonably well
+ Experimental results are promising

### Weaknesses
 - Limited originality
- Small models and datasets
- Only one TDA method experimented on for LoRA
- Weak reasoning in the theoretical section to justify their approach

### Questions
In general, I do not find this paper too exciting. Application of Dropout and LoRA in this context is nice, but somewhat incremental from an originality standpoint in my opinion. Also since the main claim of the paper is efficiency I would have liked to see experiments on larger datasets and also with larger models, since they are considering generative tasks. Arguments in the theory section are also weak. Case 1 argument of within group covariance being smaller than individual predictor variances, although not completely justifiable, I could still buy. However, for Case 2 the within group covariance being not too much larger than covariance between individual predictors is hard to accept, since the whole point of the paper is efficiency and having a large K implies you have to build many independent models defeating the purpose. Hence, if one were using this method they would want to have a low K, which implies for Case 2 the performance of their proposed solutions could be considerably worse.

All in all the paper is reasonable, but limited in the above mentioned ways.

### Soundness
2

### Presentation
3

### Contribution
2
