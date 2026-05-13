# Efficient Training of Sparse Autoencoders for Large Language Models via Layer Clustering

- Decision: Reject
- Scores: 3, 3, 6, 3, 6

## Abstract
\ac{saes} have recently been employed as an unsupervised approach for understanding the inner workings of \ac{llms}. They reconstruct the model's activations with a sparse linear combination of interpretable features.
However, training \ac{saes} is computationally intensive, especially as models grow in size and complexity. To address this challenge, we propose a novel training strategy that reduces the number of trained \ac{saes} from one per layer to one for a given group of contiguous layers. Our experimental results on Pythia 160M highlight a speedup of up to 6x without compromising the reconstruction quality and performance on downstream tasks. Therefore, layer clustering presents an efficient approach to train \ac{saes} in modern \ac{llms}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes to reduce the computational overhead of SAEs: instead of training a separate SAE for each layer, it groups the layers to several groups of adjacent layers and learns an SAE for each group.

### Strengths
Improving LLM interpretability is an important topic. The proposed method of speeding up SAEs is straightforward and easy to understand.

### Weaknesses
Overall I feel that the results presented in this work are quite obvious and expected, and I do not see a large contribution to the community.
1. The novelty of this work is limited. It seems to be an obvious choice for one to learn an SAE for each group of adjacent layers.
2. Based on the experimental results (on a 12 layer 160M model), the speed up provided by the method is limited. The speed up also always comes with a drop of the quality of the model. Based on Figure 3 and Figure 4, the drop seems to be almost linear to k. This is quite expected with any types of "simple" speed up such as down sampling and grouping (like this paper suggested).

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper builds on the recent line of work that relies on sparse autoencoders (SAEs) to address the interpretability of large language models (LLMs). In particular, SAEs aim to decompose LLM activations in a layer as a sparse combination of a large number of (interpretable) features. However, prior works require training one SAE per LLM layer (component), resulting in a large number of parameters and prohibitively high compute cost needed to obtain good quality SAEs to understand the inner workings of the LLM.

This paper leverages similarities among consecutive layers in an LLM to reduce the training cost for SAEs. The paper proposes to cluster LLM layers in $k$ groups and then train one SAE for each group of layers. Based on the reconstruction error of original representations; downstream performance on tasks focused on indirect object identification, greater than relationship, and subject-verb agreement; and human evaluations, the paper argues that the proposed approach results in good quality SAEs for Pythia 160M LLM.

### Strengths
1) The paper focuses on important and timely questions related to the interpretability of LLMs. 
2) The proposed method successfully improves the training efficiency of SAEs for LLMs by grouping similar layers. 
3) Empirical evaluation based on both reconstruction error and downstream performance showcases the utility of the proposed approach.

### Weaknesses
1) The main weakness of the paper is its limited technical novelty and contributions. The reviewer believes that the proposed approach of grouping multiple similar layers and training one SAE per group does not constitute a significant contribution to the field. Furthermore, the empirical evaluation in the paper is restricted to a small language model (Pythia 160M) and focuses on very simplistic tasks. This does provide strong evidence of the value of the proposed method for realistic settings involving LLMs.

2) There is a significant scope for improving the presentation of the paper. Many design choices in the paper are not well justified (see the Questions section below).

3) The authors build on many recent prior works. The reviewer believes that the authors can provide a more comprehensive background of some of these works to make the paper self-contained. It would be helpful for the reader to know how SAEs can be utilized for a particular application while studying LLMs.

### Questions
1) Please consider introducing dimensions of various vectors and matrices in Sections 2.1 and 2.2. Also, what is the relationship between $d$ and $dmodel$ (Line 112-113)? It appears that $d = dmodel$?

2) Please formally define the term "residual stream".

3) In Section 3.1, what is the justification/motivation for using *JumpReLU*? 

4) As for the hierarchical clustering strategy described in Lines 212 - 220, is it clear that one will only put consecutive layers in one group? Can non-consecutive layers be clustered into a single cluster? If yes, is this desirable?

5) Figure 3 presents multiple metrics, CE loss, $R^2$, $L_2$, $L_1$. Out of these, which one is more important? Also, looking at some of the figures, the difference in the metric value for different $k$ is very small. What is the significance of this small difference?

6) In Figure 7, Human interpretability scores appear to be *non-monotonic* with respect to $k$. Could authors comment on this?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method that will make suites of Sparse Autoencoders (SAEs) easier to use (as they will require fewer SAEs) and easier to train (large compute saving). The method is to train SAEs on the activations from contiguous blocks of layers in the model.

### Strengths
* The paper provides comprehensive analysis on the end artifact of their work, such as detailed circuit analysis evals, interpretability studies and accuracy metrics.

* The idea is easy to understand and the execution competently done.

* The results on the circuit analysis evals look strong, as there's barely any performance hit to using the strategy according to that eval.

### Weaknesses
The paper claims that there is a $(L-1) / k$ efficiency saving through using their method. But unless I misunderstand, since there are a fixed number of tokens used $T$ (1B in this case), and there will always be $LT$ total activations which all SAEs are trained on, the number of FLOPs used to train the SAEs will be **the same** using this method or not. Since language model activation saving can be amoritized (e.g.  https://arxiv.org/abs/2408.05147 or https://github.com/EleutherAI/sae) there is no theoretical benefit to saving LLM activation saving either.

The paper is titled as "Efficient Training of Sparse Autoencoders..." and hence unless I misunderstand some method, this paper does not achieve its goal and I cannot recommend it.

### Questions
Please answer whether my weakness is correct.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a more efficient method of training SAEs that groups similar layers together and trains a single SAE on each group. The grouping is done using aglommerative clustering between layers, where the layer to layer similarity is defined by the average angular distance between layer activations across 5M tokens. The authors compare their method with 5 different values of k (number of groups) against baseline sparse autoencoders on standard SAE metrics (L0, R^2, CE Loss score, and L0), and find that it is worse on these metrics. They also compare against circuit faithfulness and completeness metrics, where their method slightly improves on baselines.

### Strengths
- The clustering of layers to find the best groups for training a shared SAE on is interesting
- The evaluations of the interpretability and downstream performance of the SAEs are strong
- The problem is mostly well motivated: methods to reduce the computational bottlenecks of training large SAEs are important.

### Weaknesses
The largest weakness of this work is that it is unclear how the proposed method works. Does it concatenate the layers? Does it train on an equivalent fraction of activations from each layer? Does it take in layer i and predict all of the other layers? 
- It is also unclear what this method actually improves on or tells us about, besides simply reducing the total number of SAEs trained (L0s, losses, and interpretability are all significantly worse). Does it actually use less flops (since its plausible that training on more layers requires more flops)? Does it tell us something about how many features are shared across layers, and which layers share features? 
- Because of the lack of experimental details, it is very unclear how this differs from prior work in this area: Residual Stream Analysis with Multi-Layer SAEs, https://arxiv.org/pdf/2409.04185
- The paper contains many typos and rushed writing.
- All bar plots should have a number showing the actual value of the bar, and error bars where they make sense.
- This work only examines residual layers, which is in some sense the “easiest” setting for this idea.

### Questions
- How does the circuit analysis work with the multiple layer SAEs? Can features in the “same” layer be connected? If not, is this might be an unfair comparison to baselines, because there are less feaatures overall to choose from?
- Why do you think the L2 of the lower Ks is higher?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- When training sparse autoencoders on the residual stream, there is often one per layer. This is likely redundant, as the residual streams at two adjacent layers are often fairly similar
- The authors propose instead grouping layers by similarity of residual stream, using average angular distance, and training a single SAE for each group of layers. 
- The authors claim that grouping is a substantial speedup. However, the text implies (but does not explicitly state) that all SAEs are trained on 1B tokens. This means that an SAE for a group of eg 3 layers trains on 3e9 activations, while training 3 SAEs, one for each layer, trains on 1e9 activations, for the same total compute. This means it is not a speedup. If the grouped SAE was instead trained on 0.33B tokens, or even randomly sampled one layer's residual for each token, this would be a speedup. This is a crucial detail and needs to be clarified
- The grouped SAEs are evaluated fairly carefully against the baseline of identically training an SAE per layer. The authors use a range of evaluations:
    - Standard metrics like L0, L2, CE Loss score
    - A circuit finding eval on several previously studied circuits. Authors use attribution patching to identify key SAE latents and calculate completeness and faithfulness. It does not seem to be stated whether there is a separate forward pass when ablating at each layer, or if all layers are ablated at at once.
    - A human interpretability study with 96 features. It is not specified whether this is 96 features per SAE, per SAE family, or total.
- The overall conclusion is that quality and performance was preserved, which seems reasonable for K=4 or K=5 at least.

### Strengths
- A fairly comprehensive set of evaluations is used, more than is common in such papers. I particularly liked the circuit based eval, modulo the concerns below
- It's a fairly simple, elegant idea that I hadn't seen done before, and which could be a simple drop-in replacement to significantly save the cost of training suites of residual SAEs
- Covered some key limitations clearly in the limitations section

### Weaknesses
 - Numerous missing details, as discussed in the summary, which make it impossible to evaluate how impressive the results are
- Only studies a single model
- The faithfulness metric is problematic. Including the error term in the reconstruction when calculating faithfulness inflates the score of low-quality SAEs, as the error term will be more informative when the SAE is poor. This makes it unsuitable for comparing SAE quality. A poor SAE that outputs zeros will have excellent faithfulness when evaluated this way, as ablating all features will cause a large change in the output, which is not the desired behavior. 
- It is not explicitly stated how completeness and faithfulness are aggregated per layer. It seems that the scores are simply averaged across layers, which makes it hard to compare different SAE groups to the baseline. If the task is inherently easier at later layers, then even if the later groups are a degradation they may look better than the baseline when averaged. This makes it difficult to determine if the grouping method is actually effective or if the results are simply due to the inherent properties of the layers being evaluated.
- It is stated that JumpReLU activations are used, but also that an L1 loss is used. JumpReLU requires an L0 loss and straight-through estimators to update the threshold, otherwise the threshold will always be zero. This means that the SAE is effectively a ReLU SAE, which is misleading.

### Questions
# Major Comments
*The following are things that, if addressed, might increase my score*
- My overall assessment here is that it's quite plausible that this technique works, just on priors, and would be valuable to people training suites of SAEs on every layer's residual stream like Gemma Scope. I like the spirit of this paper, and think it has the potential to be a solid paper, but that right now there's significant room for improvement and I am not currently convinced of the core thesis based on the evidence in the paper. **If rebuttals go well, I'm open to increasing my score to a 6 or possibly 8.**
- There are several crucial missing details in the paper, that significantly alter how the results are to be interpreted. I wouldn't be comfortable accepting the paper until these are clarified positively, or follow-up experiments are done which clarify, especially re the amount of compute used. (Note: I tried to check the paper fairly hard for these details, but I apologise if I missed them somewhere)
    - Is a layer group SAE trained on the same number of tokens as a normal SAE? (and so on significantly more activations, since there's one per layer in the group) If so, the claims of a speedup is false, this should take the same about of compute. There are minor benefits, like having fewer features to care about for eg probing, and fewer SAE parameters, but these are comparatively minor I think. To get a speedup, you need to run it on num_tokens / num_layers, for the same amount of training compute as a normal SAE (and less LLM running compute). It needs to be a fair comparison, as SAEs trained for longer generally perform better on evals, so the current evals can't be trusted.
    - What does "96 features" mean in the human interpretability study? Is it per SAE, per SAE family (ie a set of SAEs covering all 12 layers, either grouped or baseline), or 96 total? 96 isn't that much, so this significantly changes how much to trust the study. 
    - With the circuit finding evaluations, when you do mean ablations to find completeness or faithfulness, do you do mean ablations to each layer one at a time, with a separate forwards pass per layer? Or to all layers at once?
        - If it's one pass per layer, then is it just averaged to form the faithfulness and completeness graphs?
        - If all layers are done at once, does N features mean per layer, or total?
        - Are you including error terms (ie the original act - reconstruction, as done in Marks et al), or not?
        - Including error terms makes comparisons harder - if an SAE is bad, its error terms are more informative, boosting performance
        - Meanwhile, if you don't include it and take ablations at every layer, I'm very skeptical that you could get the completeness results you do. In my experience, applying SAEs at every layer at once tanks model performance to the point of near randomness
- You say you use JumpReLU activations, but also that you use an L1 loss, unlike the JumpReLU paper's L0 loss + straight-through estimators. The threshold goes into a discrete function and so always has gradient zero and will never update unless straight-through estimators are used, suggesting that in this setup the thresholds are always zero? This is OK, it's just a ReLU SAE, but is misleading
- There are various things that make it messier to apply: it's not clear how many groups to make (especially on larger models!), I'm not convinced there's not a big performance degradation when done in a compute matched way, it's not clear how well these results generalise (in particular to the larger models where this is expensive enough to matter), etc. I know these are not realistic to fully address in the rebuttal, but here are some experiments that would strengthen the work:
    - Just doing the cosine sim analysis and layer grouping across several more models, including larger ones, and seeing how many groups are needed to get max angular distance below some threshold (eg whatever it took for 4 groups here). This should be fairly cheap, I think
    - Replicating these results on a larger model, eg Gemma 2 2B. Training a full suite would of course be fairly prohibitive, but eg finding an early pair of layers with low angular distance, and showing a compute matched grouped SAE performs comparably with an SAE per layer, would be compelling and should not be too expensive, especially with a low expansion factor, low number of tokens, and stopping execution of the LLM after the target layer.


# Minor Comments
*The following are unlikely to change my score, but are comments and suggestions that I hope will improve the paper, and I leave it up to the authors whether to implement them, either during rebuttals or after. No need to reply to all of them in the rebuttal*
- The distribution of residual streams in each layer is going to be different, in particular the norm and the mean will vary. I expect you could get notably better performance by pre-computing and subtracting the mean and dividing by the average norm (after mean-centering), to make layers comparable. This mean and scaling factor could even be made learnable parameters. I'd be curious to see this tried.
- Similarly, residual streams typically have significant non-zero mean (though I haven't investigated Pythia specifically) which makes cosine sim/angular distance harder to interpret, I'd be curious to see Figure 2 with mean-centered cosine sim (I don't expect major changes, but should be cleaner)
- I hypothesise that a layer grouped SAE trained on 1B tokens and acts from each layer may perform comparably to one trained on 1B tokens and a randomly chosen layer's act per token, since the acts are likely to be highly similar. This would also be a big SAE training compute reduction!
- The up to 6x speedup claim seems like an overclaim, it seems pretty clear to me that the K=1 setting performs badly enough to probably not be worth it. I'd say K=3 is the smallest that seems reasonable, so a 3x speedup (if compute matched)
- In Figure 3, I think it's pretty confusing to average your stats across all layers, especially things like L2 which are *very* different across layers. I would recommend either normalising (eg dividing by the baseline value), or ideally providing the per-layer info compactly. For example, a bar chart with layer on the x axis, and a group of 6 bars at each place (one for each K, and baseline). Or a line chart where the x axis is layer, and there's a line for each K and baseline. I appreciated these being included in the appendix, but this could be mentioned prominently in the main text
    - I also recommend displaying the raw change in cross-entropy loss, not the normalised CE score. Ablating the residual stream is extremely damaging, so normalised scores are always very high, making it hard to interpret
- Line 193: You say umpReLU is z * ReLU(z-theta), but it's actually z * H(z-theta), where H is the Heaviside function (1 if positive, 0 if negative)
- Figure 2: It would be good to clarify in the caption or line 209 that the key thing to look at is the main diagonal (and that it's about each layer to the adjacent one, not to itself!), that lower means closer, and that 0.5 means "totally perpendicular". I figured this out eventually, but it would help to clarify it
- I didn't find the discussion of MMCS on page 6 to be too informative. Without a baseline of comparing to another trained SAE on that layer, it's hard to really interpret what it should look like. I'd be fine with this being cut or moved to an appendix if you need the space
- Line 337: It would be good to clarify that you do integrated gradients by intervening and linearly interpolating the *activations* not *input tokens*. [Marks et al](https://arxiv.org/abs/2403.19647) does it your way, [Hanna et al](https://arxiv.org/abs/2403.17806) does it on input tokens (and input tokens is the standard method, though IMO less principled than your's)

### Soundness
1

### Presentation
1

### Contribution
3
