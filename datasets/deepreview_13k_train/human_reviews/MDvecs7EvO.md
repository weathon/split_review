# Mechanistic Permutability: Match Features Across Layers

- Decision: Accept
- Scores: 8, 5, 5, 8

## Abstract
Understanding how features evolve across layers in deep neural networks is a fundamental challenge in mechanistic interpretability, particularly due to polysemanticity and feature superposition. While Sparse Autoencoders (SAEs) have been used to extract interpretable features from individual layers, aligning these features across layers has remained an open problem. In this paper, we introduce SAE Match, a novel, data-free method for aligning SAE features across different layers of a neural network. Our approach involves matching features by minimizing the mean squared error between the folded parameters of SAEs, a technique that incorporates activation thresholds into the encoder and decoder weights to account for differences in feature scales. Through extensive experiments on the Gemma 2 language model, we demonstrate that our method effectively captures feature evolution across layers, improving feature matching quality. We also show that features persist over several layers and that our approach can approximate hidden states across layers. Our work advances the understanding of feature dynamics in neural networks and provides a new tool for mechanistic interpretability studies.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces SAE Match, a technique that produces a bijection from [sparse autoencoder (SAE) features in layer n] and [SAE features in layer n+1], with the objective of reducing the average squared distance (i.e., mean squared error (MSE)) between a feature and its target. They also introduce parameter folding, which seeks to augment SAE Match to work on features with different scales. The paper shows via experimentation on Gemma Scope SAEs  that features have more similar LLM-derived interpretations if they have lower MSE, and that SAE Match with parameter folding results in more similar interpretations.

### Strengths
- The paper's SAE Match technique appears to work well at finding corresponding SAE features between layers, which can contribute to the goal of mapping a "feature circuit" (as in Marks et al. (2024) https://arxiv.org/pdf/2403.19647). This technique is data-free, meaning only the SAE weights are required, and not any model or SAE activations.

- The paper also provides useful empirical evidence that SAEs find features between layers that are simultaneously 1) close in the space of parameters, and 2) interpreted to have similar meaning.

### Weaknesses
 - The authors get far worse results on layers 0-9 of the model than on layers 10-25, indicating that the technique may not fully generalize. The authors claim that this is to be expected, saying "This phenomenon aligns with findings from previous research. Gurnee et al. (2023) also reported increased polysemanticity in the early layers of neural networks." This explanation is unsatisfactory because Gurnee et al. (2023) were working with LLM neurons, not SAE features. Additionally, Cunningham et al. (2023) found that earlier layers were more interpretable (see Figure 2 in https://arxiv.org/pdf/2309.08600). The discrepancy between the authors' results and those of Cunningham et al. (2023) is particularly concerning, as it suggests the SAE Match technique may be fundamentally limited in its applicability to earlier layers, or that the SAEs themselves are not learning useful features in those layers. It is unclear if the poor performance is due to the matching algorithm itself, or to the nature of the features extracted by the SAEs in the initial layers.

- The proposed technique of parameter folding is only defined for SAEs using the JumpReLU activation function, and it is not clear how could be adapted to over activation functions like ReLU or TopK. This severely limits the applicability of the method, as many SAEs are trained with ReLU or TopK activations. The authors do not provide any theoretical justification for why parameter folding is unnecessary for ReLU or TopK, nor do they provide any empirical evidence to support this claim. Without a clear explanation or experimental validation, it is difficult to assess the generalizability of the proposed method to other common activation functions.



### Questions
Questions for the authors:

1. Parameter folding serves as a form of normalization for encoder/decoder weights (as is mentioned in lines 156-157). What happens if one instead matches feature with encoder/decoder weights normalized to be unit vectors? This would be equivalent to maximizing cosine similarity instead of minimizing MSE, as ||x-y||^2=||x||^2+||y||^2 -2 ||x||*||y||*cossim(x,y).

2. One might expect the set of features to change across layers as the model processes information. In that case, the "correct" form for a matching might not be a bijection. Could one instead define a non-bijective "matching" via P(f)=argmin_i ||f-g_i||_2 where f is a feature in layer n, and {g_i}_i=1^k is the set of features in layer n+1? How does this compare to Feature Matching?

3. In Section 5.4, Figure 8, the y-axis is labelled "GPT Score". What is that metric and how was it calculated? Previous metrics have been a "GPT Score" on a scale of Different/Maybe/Same, or Matching Score in a range of 0-1, but this does not appear to be either of those.

4. In Section 5.5, it seems Layer Pruning may introduce error in two ways: 1) feature activations in layer N do not result in perfect reconstruction of the residual stream even for layer N, and 2) features in layer N do not perfectly match features in layer N+1. Did any experiment disentangle those effects? For instance, what is the \Delta L from replacing x with \hat x? This would provide useful context for the quantities shown in Figure 10.

5. Many SAEs have "dead" features, which presumably contribute little to the matching process. Could SAE Match be modified to exclude "dead" features, and if so how?



If it is permitted for authors to make revisions before the final submission, there are several small changes that could improve the quality of the paper:

- Line 93: The loss function as written is incorrect. The L2 term is squared, and what is written as L0 should be L1. See e.g. Equation 4 in (Cunningham et al, 2023) (https://arxiv.org/pdf/2309.08600). 

- Line 132-133 (equation 3): The L2 norm in the argmin needs to be squared to get the mean *squared* distance.

- Lines 147-149 (equation 4): It appears that b_dec should be b_enc.

References:

Wes Gurnee, Neel Nanda, Matthew Pauly, Katherine Harvey, Dmitrii Troitskii, and Dimitris Bertsimas. Finding neurons in a haystack: Case studies with sparse probing. Trans. Mach. Learn. Res., 2023, 2023. URL https://openreview.net/forum?id=JYs1R9IMJr.

Hoagy Cunningham, Logan Riggs Smith, Aidan Ewart, Robert Huben, and Lee Sharkey. Sparse autoencoders find highly interpretable features in language models. In The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/forum? id=F76bwRSLeK.

Samuel Marks, Can Rager, Eric J. Michaud, Yonatan Belinkov, David Bau, Aaron Mueller. Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models. 2024. https://arxiv.org/abs/2403.19647

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors define a similarity metric between two learned encodings, based on permutations. They find that, specifically for the JumpReLU architecture, θ tracks the growing residual stream norm. Accounting for this observation by normalizing weight vectors with θ improves permutation matching. They find that W_dec MSE decreases substantially for high layers, while not making differences for early layers. They further employ an LLM to judge the semantic similarity of matched features. Interestingly, they find that feature matching works well in early layers (<10) as per MSE but show that feature descriptions do not match. Additionally, they compare matching features across multiple layers by exact match and layer-wise composition, and investigate SAE match as layer pruning technique.

### Strengths
Main finding: Cosine similarity alone is not a great proxy for late layers, as residual stream norms increase. The authors propose parameter folding, which effectively addresses this problem for JumpReLU SAEs. Current work relies on cosine similarity, and I am convinced the field should adopt this proposed technique.

### Weaknesses
### Critiques that can be addressed in this paper
- I am unsure whether the original hypothesis of permutation is answered. The term "matching" implies a binary measure of whether a feature mapping is true or false. This might require the introduction of a cutoff threshold, or applying a clustering technique. Otherwise, the framing of similarity measures might be clearer than permutation. I'm curious about the authors' opinion on whether there is a binary criterion for whether features do/don't match.
- To quantify the fraction of "true matches," the MSE over all features is too coarse; only the matching score distribution provides a clear picture of which fraction of features are "well enough" matches. It's unclear how the MSE relates to the actual alignment of features, especially given that the MSE is an average over all features, potentially masking important variations in matching quality across different feature pairs. A more granular analysis, perhaps using histograms of matching scores, would be more informative.
- Line 315: "...unfolded matching showed higher MSE in the scale of hidden state representations, supporting behaviour described with Hypothesis 2." Comment: This is not true for benc MSE.
- I'm unsure about the statistical significance of the LLM evaluation. I understand that 100 out of 16k (<0.1%) SAE latents (aka features) were chosen. Did the authors choose these features at random? Increasing the number of SAE features would increase the significance of their findings. Using an LLM to judge the coherence of max activating examples of features would be an insightful additional metric that would track the suspected polysemanticity in early layers. The current approach, relying on a small, possibly biased sample, makes it difficult to generalize the LLM's assessment to the entire feature set. Furthermore, the lack of a clear protocol for selecting these 100 features raises concerns about potential selection bias.
- I do not agree that Figure 7 right reflects the findings in Figure 7 left, where the matching score suddenly increases at layer 10. The GPT-Score and Matching Score, while related, are distinct metrics and should not be expected to show identical trends. The sudden increase in matching score at layer 10 in Figure 7 left is not clearly mirrored in the right panel, which shows a more gradual increase, suggesting that the two metrics may not be as tightly correlated as implied.
- The quantification of "too far apart" in Hypothesis 3 would be a useful improvement. The current definition of 'too far apart' lacks a clear, quantifiable threshold, making it difficult to evaluate the hypothesis rigorously. A more precise definition, potentially based on a statistical measure or a distance metric, would be necessary to validate this claim effectively.

### Questions
### Questions
- I'm curious about the takeaways of the experimental results from Section 5. How do I interpret a scale of ∆L about 1? Do the authors believe their results indicate that layers between 10 and 20 can be collectively pruned with the SAE matching method?
- I'd be interested in a discussion of why encoder matching performs worse than decoder matching.

### Further notes
- Line 154: Repetition of meaning in two following sentences.
- Why is Hypothesis 2 formatted as a hypothesis? It seems like a definition of a method to me.
- Line 234: Calling "average ℓ0" a regularization coefficient is misleading; calling it (average) sparsity is clearer.
- Line 235: Do the authors refer to Equation 3 when mentioning MSE? A reference of that equation or a different naming would be useful, since MSE is often used for the reconstruction loss in the context of SAEs.
I- 'm very curious how these results compare to findings with crosscoders (https://transformer-circuits.pub/2024/crosscoders/index.html). Matched features might share decoder vectors of a single crosscoder feature.
- Section 5.3: Gurnee operates on MLP neurons, which are not incentivized to be sparse. I expect SAE features to be (more) monosemantic, so Gurnee's results ideally shouldn't apply to SAE features.
- I'd be curious about a deeper investigation of the sharp increase in semantic feature similarity in Figure 4 left.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new method for comparing and matching features of SAEs of nearby layers in transformers. They propose scaling features according to the activation threshold $\theta$ of a JumpReLU activation function in order to match features in a more natural norm for the underlying activations.

### Strengths
- Proposes a novel and interesting strategy for pairing features between layers.
    - Studies some of the shortcomings (e.g. long tail of pairing 'failures') of this strategy.
- The presentation is very clear and understandable.

### Weaknesses
 - It would be good to spend more time justifying the hypothesies of Section 3. I do not think that the results in Figure 3 constitute much evidence for Hypothesis 2, since the reasoning here seems slightly circular - you propose parameter folding based off the observation that $\theta$ tracks the activation norms, but then evaluate feature similarity using the same objective that you are explicitly trying to minimize. Therefore, it is trivially true that 'folding+matching' outperforms 'matching'.
    - The evidence for Hypothesis 2 could be strengthened by including an analysis of how the scale of $\theta_i$ tracks with the scale of feature $i$ *on the same layer* (and similarly measuring MSE by scaling the features according to data-dependent statistics instead of $\theta$, e.g. by comparing MSE in the norm induced by some whitening transformation?); the observation in Figure 1 shows that *mean* $\theta$ tracks with *mean* activation norm, but your hypothesis rests on the assumption that $\theta_i$ is predictive of the scale of feature $i$ for features of the same layer. It is not clear that the average relationship between $\theta$ and activation norm extends to individual features, and this is a critical assumption for the method to be effective. The claim that "since the decoder features are originally unit-normalized, the absolute value of $\theta$ can be considered a proxy for the feature norm" is non-trivial and should be supported by empirical evidence, beyond the average norm across layers.
    - It would be more convincing if you backed up your claims in Figure 2 that "reconstructions of matched features are closer to each other than in the unfolded variant of the algorithm" by comparing the reconstruction loss (perhaps again under a norm induced by a whitening transformation?) of 'folded+matched' and 'matched' permutations when 'skipping' a layer, as in Section 5.5.
 - There was little analysis of the results of the experiments in Section 5.5. The loss differences resulting from using feature-matched activation reconstructions were not compared to any nontrivial baseline (e.g. perhaps something like a linear approximation of the layer?) and it was hard to see what the desired conclusion/hypothesis or suggestion at a direction for future study was here, and the paper might benifit from expanding on this a bit.
    - It might also be useful to baseline the figures in Figure 10 using the reconstructions of an SAE at layer $t+1$, i.e. substituting $x^{(t+1)}$ with $W_\mathrm{dec}^{(t+1)} \sigma ( W_\mathrm{enc}^{(t+1)} x^{(t+1)} + b_\mathrm{enc}^{(t+1)} ) + b_\mathrm{dec}^{(t+1)}$; it is known that SAEs achieve nonzero reconstruction loss and that this incurs a performance penalty when using the reconstructions in place of the original activations. Intuitively the penalty incured from using the matched activations is 'mixed' with this base reconstruction penalty.
    - As stated before, it would also be good to include the 'matched' baseline in this section as well.

### Questions
Could you provide more direct evidence for Hypothesis 2, or provide a clearer argument for why your current result provide evidence for it? Could you provide more discussion of what the takeaways for Section 5.5 were intended to be?

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a technique to match SAE latents from two SAEs across different layers called SAE Match. The technique finds permutations of latents which minimize MSE between the encoder and/or decoder representation of the feature in both SAEs. SAE Match addresses different layer norms by folding in the jumprelu threshold parameter into encoder and decoder matrices. The paper evaluates the technique on the Gemma Scope SAEs for Gemma 2.

### Strengths
Using MSE loss between SAE decoders is simple and fast. The idea of folding the jumprelu threshold parameter into weights to account for differences in layer norm is a really nice idea as well. Aligning SAE latents across layers is important for understanding how features progress throughout the foward pass of the model, so this work is useful to the field.

### Weaknesses
The paper only focused on a single model (Gemma) and a single type of SAE (JumpReLU). The paper evaluates on Gemma Scope, but uses only a single SAE per layer despite Gemma Scope containing multiple SAEs per layer with different sparsities. It would be a good check to see how the method performs comparing different SAEs trained on the same layer as well. The method seems like it does not address feature splitting, where a single latent in one SAE becomes multiple latents in a different SAE - the method seems like it will only pair latents 1-to-1. Furthermore, the evaluation of vanilla matching raises concerns about the baseline's informativeness. The low MSE achieved by vanilla matching, even without any alignment, suggests that the norms of the decoder weight vectors might be inherently small, making the MSE metric less sensitive to actual alignment quality. This could potentially mask the true effectiveness of the proposed matching techniques.

### Questions
- In Figure 3, there are different results for folder and unfolded b_enc, but b_enc is not affected by folding according to equation 4. How is b_enc different due to folding?
- In Figure 3, vanilla matching performs not much worse than the actual matching techniques. Is vanilla matching essentially equivalent to randomly pairing decoder rows? If so, why is the MSE loss so low?
- In Section 4, it says SAEs with regularization coefficient near 70 are used. Is this referring to the L0 of the SAE in Gemma Scope? Neuronpedia only supports Gemma Scope SAEs with L0 closest to 100 - if Neuronpedia is used for all SAEs, does this mean that the L0 near 100 Gemma Scope SAEs are used as well?

### Soundness
3

### Presentation
3

### Contribution
4
