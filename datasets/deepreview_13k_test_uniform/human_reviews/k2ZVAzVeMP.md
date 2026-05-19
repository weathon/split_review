# Efficient Dictionary Learning with Switch Sparse Autoencoders

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Sparse autoencoders (SAEs) are a recent technique for decomposing neural network activations into human-interpretable features. However, in order for SAEs to identify all features represented in frontier models, it will be necessary to scale them up to very high width, posing a computational challenge. 
In this work, we introduce \textbf{Switch Sparse Autoencoders}, a novel SAE architecture aimed at reducing the compute cost of training SAEs.
Inspired by sparse mixture of experts models, Switch SAEs route activation vectors between smaller ``expert'' SAEs, enabling SAEs to efficiently scale to many more features.
We present experiments comparing Switch SAEs with other SAE architectures, and find that Switch SAEs deliver a substantial Pareto improvement in the reconstruction vs. sparsity frontier for a given fixed training compute budget.
We also study the geometry of features across experts, analyze features duplicated across experts, and verify that Switch SAE features are as interpretable as features found by other SAE architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Switch sparse autoencoders for learning sparse representations of neural network activations. Switch SAEs include a mixture of TopK SAEs and a router to ensure that only one expert processes each input.

### Strengths
This work presents an idea to apply a mixture-of-experts layer to sparse autoencoder training and propose Switch sparse autoencoders. However, the architecture itself and the training technique are straightforward applications of existing work. 

The author conducts experiments comparing the Pareto frontiers of proposed Switch SAEs against a single SAE baseline, showing their better reconstruction performance at similar sparsity levels. I think it is somewhat expected for the mixture model due to expert specialization and the additional router parameters. Moever, the training of this architecture is more complex and costly. 

The worse performance on the same width setting is indeed a drawback of this work, which might limit its applications.

### Weaknesses
See above.

### Questions
Even though only one expert is active, I wonder what sparsity patterns look like for other experts and how much they overlap. Would it make sense to compare using global sparsity?

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
The paper introduces switch SAE's which is a combination of switch layers with top-k SAEs. Instead of decomposing a latent directly it is forwarded to one of multiple SAE encoder decoder pairs. The authors show that given a FLOP budget the switch SAE reaches a lower reconstruction loss faster, while for a fixed number of parameters the vanilla top-k SAEs achieve lower reconstruction loss. That is for a low reconstruction loss with switch SAEs more features in total are required (but they are cheaper to train). Switch SAE features are shown to also be interpretable.

### Strengths
The authors explore a combination of methods that makes a lot of sense (switch layers and top-k SAEs) and analyze the resulting method in a rigorous and convincing way. They make the interesting findings that switch SAE's are in terms of FLOPS actually cheaper to train (for a given target reconstruction loss) and at the same time require more features in total (which will be an additional challenge for the usual subsequent automatic interpretation of the learnt features). Also they show that the switch SAE features are interpretable.

### Weaknesses
The idea maybe can be considered as a little bit incremental, but given the very good execution of the paper I don't think that's a big problem.

The switch SAEs require more features for the same reconstruction loss, which down the road: for automatic interpretability and SAE feature based interventions presents significant drawbacks. The cost of automatic annotation scales linearly with the number of features to annotate and in my opinion having a giant number of SAE features also makes them less human-compatible/interpretable.

### Questions
Do you think it is possible to set up switch SAE in a way that each SAE becomes a domain expert? E.g., there could be one SAE per language or something like that.

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
3

### Summary
This paper proposes an extension to Sparse Autoencoders (SAEs) in the form of switch SAEs. Switch SAEs reduce the memory consumption of storing the sparse activations by splitting the representation space across multiple SAE experts, of which only one is used at a time. Experiments show that switch SAEs achieve better reconstructions with the same number of FLOPs as current methods at the cost parameter efficency. The paper also explores the features learned by the experts and observe that some features cluster within experts and others are duplicated across them.

### Strengths
The strengths of the paper are its simple approach and side studies.
- The approach enables a trade-off between model parameters and computational requirements which should be useful to practitioners.
- The auxiliary experiments are well-motivated and support the author’s hypotheses. Specifically, the discussions of redundant representations accompanied by t-SNE visualizations are illuminating.
- The limitations (parameter efficiency and feature duplication) are discussed in an informative way.

### Weaknesses
The main weakness of the paper is its quantitative evaluation.
- The hyperparameter $\alpha$ is set to 3 (line 258) without further discussion. How was this value chosen? Is this a reasonable default in most settings or is tunning required based on the model and dataset?
- The abstract claims a “substantial Pareto improvement” for a fixed training budget. This corresponds to the FLOP-matched experiments shown in the bottom left plot of Figure 3. It is not directly obvious that this constitutes a substantial improvement. The difference looks small enough to warrant repeated experiments to ensure its significance. A table of improvements with confidence intervals would make the difference much clearer.
- Figure 4 could use an explanatory caption.

### Questions
- Why are the proportion of activations routed and the routing probability used in the auxiliary loss? Intuitively, both convey the same information, with one being the distribution and the other samples from it.
- A batch size of 8192 is used during training (line 269). Is a large batch size required for stable training of switch sparse autoencoders, and does this differ from the baseline methods?
- Finally a broader question about the utility of scaling SAEs. Do the learned features need to be manually interpreted? If so, how is increasing the number of parameters a useful approach to interpretability if it also increases the required manual annotation?
- The references seem biased towards recent years. Besides the Adam optimizer and GPU acceleration, no references exist from before 2016, despite sparse autoencoders, sparsity, topK, and MoEs being popular research topics much earlier than that. Are these not an important background to sparse SAEs?

**Minor suggestions that do not individually affect the score**
- Line 295: “For a wide range of sparsity (L0) values”. Specify the range.
- Line 298: Clarify what is meant by a zero-ablation.
- Line 317: “Switch SAEs can likely achieve greater acceleration on larger language models”. Expand on this.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces **Switch Sparse Autoencoders** (Switch SAEs). Switch SAEs are a new SAE variant, which is a popular area of research in interpretability. Switch SAEs are more efficiently to train and run at inference time for similar reasons to why Mixture-of-Expert (MoE) LLMs are more efficient than dense LLMs.

This paper claims that, fixing the number of FLOPs, Switch SAEs pareto dominate several leading SAE variants. Fixing the total number of features SAEs have however, Switch SAEs seem less performant. The paper then shows Switch SAEs have as interpretable metrics as dense SAEs as measured by an automated metric. There are some surface level studies into feature duplication, suggesting that this sometimes happens. All experiments are on GPT-2 Small's residual stream at layer 8.

Here are my references for all sections in this review:

[1] Switch MoE: https://arxiv.org/abs/2101.03961

[2] DeepSeek MoE: https://arxiv.org/abs/2401.06066

[3] GShard: https://arxiv.org/abs/2006.16668

[4] Expert-choice; https://arxiv.org/abs/2202.09368

[5] Ghost Grads: https://transformer-circuits.pub/2024/jan-update#dict-learning-resampling

[6] Updated Anthropic training method: https://transformer-circuits.pub/2024/april-update/index.html#training-saes

[7] Gated SAEs: https://arxiv.org/abs/2404.16014

[8] JumpReLU SAEs: https://arxiv.org/abs/2407.14435

[9] Anthropic Set Of Metrics Where JumpReLU does not reproduce: https://transformer-circuits.pub/2024/august-
update/index.html#interp-evals

[10] Scaling Monosemanticity: https://transformer-circuits.pub/2024/scaling-monosemanticity/

[11] SFC: https://arxiv.org/abs/2403.19647

### Strengths
1. **This paper addresses an important and novel direction that may be impactful for future work.** There are already several very large training runs that have trained large SAEs, and a key bottleneck is the autoencoder training (getting and potentially storing billions of activations from frontier models is also a bottleneck, however). The paper provides promising evidence for the MoE SAE approach.

2. **The evaluation is clear and relatively comprehensive**. Addressing FLOP-matched results and feature interpretability compared to baselines is very clear.

3. **The authors do sensible sanity checks of the approach.** Duplicated features could be a serious issue, and the analysis of how frequent they were showed they weren't an enormous proportion of features, but still present. I like the transparency of this section.

### Weaknesses
1. **There is no application of the Switch SAE in the paper.** Recently, SAEs have been applied to steering [10] and circuit finding [11] as well as many other applications in AI safety and capabilities. These applications rely on a sparse set of features explaining model behavior. But if there are N sets of sparse features, different sets for each of the experts, then these applications may not want to use Switch SAEs despite performance benefits. This is a deeper problem than merely "there may be duplicated features in different experts (as measured by cosine sim / t-SNE)". For example, on a given dataset of interest, such as a dataset used to generate an SFC graph [11] or the set of prompts related to e.g. the Golden Gate Bridge [10], there may be different ways the different experts reconstruct similar prompts. As a toy example, on a set of prompts where the "Queen" concept is always present, on one prompt Expert 1 may be chosen, and encode `V(Queen) = Feature(Woman) + Feature(Royalty)`. But on another prompt Expert 2 may be chosen and have a dedicated feature `Feature(Queen)`. Let me know if I need to make this explanation clearer.

2. **This paper bases their approach off of the Switch MoE architecture [1], but this is a weak MoE variant**. My understanding is that the switch MoE architecture is weaker than different MoE architectures. For example [2] benchmarks Switch MoEs against GShard [3] and their own DeepSeekMoE [2], and find that Switch MoEs are weakest.

Additionally, this paper requires an auxiliary loss to balance MoE load. While this is popular in conventional MoE work [1, 2, 3], other works propose to do this [4]. In the context of SAEs, several improvements have involved dropping auxiliary loss terms (e.g. [4] was replaced by [5] by the Anthropic group, and [7] was replaced by [8] by the Google DeepMind group). So I am also concerned that auxiliary loss terms are worse than (e.g.) expert-choice variants of MoEs in training MoE SAEs.

I would like to hear why these design choices were made, and think the paper should be edited if accepted to the conference to discuss these variants for future work, and to hedge the conclusions more.

3. **This paper only uses one Language Model**. GPT-2 Small has a specfic architecture which is unlike modern LLMs in several ways (only uses GeLU not gated MLPs, uses absolute positional embeddings, ...) which may mean the results do not generalize. (But this is unlikely since most work has found so far that SAE approaches that work on model 1 also work on model 2).

4. **The benefits of MoE SAEs are only at very large scale, and GPT-2 Small 800M token training runs are not large scale**. When scaling ML techniques it is often found that small-scale hacks perform worse in large setups. This is still a plausible issue given the results in paper.

Note that, despite how I found more strengths than weaknesses, these weaknesses are more technical and subtle. I think the paper overall is strong, and it required harder thinking to realise some issues with it.

### Questions
1. How can I calculate the FLOPs for a Switch SAE with given num experts, width, input dim and training datapoints? I did not see this in the paper, and therefore sentences like "As we scale up the number of
experts and represent more features, performance continues to increase while keeping computational
costs and memory costs (from storing the pre-activations) roughly constant" are very confusing.

(My GUESS at what that sentence is gesturing at is that fixing Switch SAE width, increasing number of experts decreases the encoder forward pass FLOP but not the backward pass FLOP. And after thinking about it for a minute, I think I see how increasing number of experts doesn't increase FLOP so long as you only route acts to 1 expert, always. But this was a non-trivial inference and I think it should be in the paper)

2. Are the authors able to open source training code and/or weights when this is deanonymized? Since there have been known cases in the SAE literature where promising work has not replicated [8, 9], open weights and training code will enable downstream validation of this technique to be much stronger.

3. Do you have any experiments on different models or different sites?

### Soundness
3

### Presentation
3

### Contribution
3
