# Lines of Thought in Large Language Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Large Language Models achieve next-token prediction by transporting a vectorized piece of text (prompt) across an accompanying embedding space under the action of successive transformer layers.
The resulting high-dimensional trajectories realize different contextualization, or `thinking', steps, and fully determine the output probability distribution. We aim to characterize the statistical properties of ensembles of these `\emph{lines of thought}.' We observe that independent trajectories cluster along a low-dimensional, non-Euclidean manifold, and that their path can be well approximated by a stochastic equation with few parameters extracted from data.
We find it remarkable that the vast complexity of such large models can be reduced to a much simpler form, and we reflect on implications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper aims to study the statistical properties of what they call *lines of thought*; trajectories traced by the embedded tokens through the latent space while traversing successive transformer layers. The key observation is that independent trajectories cluster along a low-dimensional manifold, and that their paths can be approximated using a simple dynamics model.

### Strengths
- I find the question posed, and the consequent findings very interesting

- I really appreciate the development of a linear approximation to the distribution of trajectories.

### Weaknesses
 - One of my biggest gripes with the paper is, while I wanted to be excited about the findings, a recurring question that I had was "why should I care"? It is my opinion that the authors should invest in a motivation for why the reader should care about the presented findings. It's not clear to me what the takeaways are, or more concretely, how we can utilize the observation to develop better LLMs for instance.

- A second gripe, which perhaps goes hand-in-hand with my first one, is that I often felt the paper could have used a bit more hand holding, or even been organized better. To make this concrete, in Section 3.1, the findings are presented first and then the methodology employed to find them was presented, which to me was a bit confusing. Section 3.2 starts abruptly with the sentence "The fast decay of the singular values...". Section 3.4 is titled "Langevin Dynamics..." with no mention of Langevin Dynamics. Furthermore, I often found myself having to reference many different figures in different parts of the paper while reading a single paragraph. All of this made it harder to follow the paper closely.

- (Stylistic nitpicking) I think some of the writing maybe embellishes on details that maybe are not very important e.g. the methodology section starts with what I believe to be details that can be abstracted away. I also think the footnotes are somewhat excessively used.

- I'm not really sure what is meant by "pilot" in this context. My understanding is that a pilot is  "done as an experiment or test before introducing something more widely."

- The authors claim that the pseudo-sentences are "independent" (line 171) which is not immediately clear to me given that the pseudosentences are chunks produced from a single piece of writing.

- I find the notation used in the algorithm confusing. Why do we sometimes use parentheses and other times square brackets? Also, wouldn't indexing with t+1=25 at  the last iteration be undefined?

### Questions
In addition to the concerns raised in the weaknesses,

- I find the point being made in the paragraph between lines 195-201 very interesting, but I am then immediately confused by the following paragraph. Could you please clarify this?

- Could you please clarify the paragraph between lines 248-251?

### Soundness
3

### Presentation
2

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
This work studies the dynamics of the embedding space as the input tokens go through the layers of a transformer architecture. The authors break the input prompt into sequences of tokens and study the embeddings of the last token as it propagates through the layers. Using PCA-like projections, it's shown that these embeddings approximately lie in a low-dimensional manifold. Then, by rephrasing these trajectories using linear approximations, the authors attempt to model it via Langevin dynamics which gives rise to the standard Fokker-Planck probability flow. One of the main conclusions is that transformers can be "distilled" into few parameters. To validate their assumptions, the authors experimentally study these trajectory on non-language inputs and untrained models and show that their ideas weakly hold. The target audience are people interested in the physics and interpretability of large language models.

### Strengths
- There has been a flurry of works trying to understand the inner workings of LLMs. Therefore, this direction is relevant and interesting.

- This work studies this problem from a unique flow-based perspective by studying the dynamics of the embeddings as they evolve in the layers. The perspective is novel to the best of my knowledge and may potentially lead to a new perspective or algorithm to improve interpretability of LLMs.

### Weaknesses
 - While potentially interesting, the paper feels too vague and very high-level without any concrete theoretical or experimental contributions.

- No new theoretical contributions are made, other than standard langevin dynamics formulations of their ideas. The projection to lower dimensions and linear approximations are also somewhat too lossy, as the authors note, so it's not clear how well the observations here actually hold in real life.

- Experiments seem limited to a few models and as the authors note, the last layer seems to form an outlier for the Mistral 7B and the Llama models. While the authors suggest some reasons for this, it's not inherently clear why these happen and bring the central hypotheses into question.

### Questions
Some questions were raised above. In addition

- This work reminds me of neural ODEs. Are there any connections between them and the viewpoint this paper explores?

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
3

### Summary
This paper studies the trajectory of token embedding across layers. Inspired by dynamic system, they model the trajectories as diffusive process with a linear drift and a modified stochastic component.

### Strengths
1.The idea of this paper is kind of interesting.

### Weaknesses
1. the Gaussian assumption seems to not hold in early layers.
2. It is unclear if the same type of paths would hold for larger and more complex model as we already see problems with newer model like LLaMA-3. I think it makes sense to model the intermediate layers with diffusion process but early and last layers might not work not well.
3. The theory here does not lead to any practical predictions. For example, can you use this model to predict next token?

### Questions
1. It is unclear to me what does this sentence (”the uncertainty (or stochasticity) introduced here accounts only for the loss of information of considering the token without its prompt.”) in footnote 8 mean?
2. For figure 3, why u_2 and u_3 without u_1?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors describe a framework that allows tracing the path taken by the activations in latent space during a forward pass on some input text. They note that despite the complexity of computing a forward pass, the trajectory taken is rather simple, and the activations live on a low-dimensional manifold that moves through latent space as a function of the number of layers processed. They provide a stochastic model that describes the trajectory, with vastly fewer parameters than the network itself. The approximation closely agrees with the actual activations, and can be used to extrapolate the behavior of the model.

### Strengths
* Strong evidence provided to back up the claims made. The authors do a great job of explaining what it is they are measuring and why.
* The result is fascinating, computationally cheap to obtain, model agnostic, and is empirically backed by measuring the KL-divergence of the distribution after down-projecting the dimensionality.
* The theoretical justification on the proposed model is well motivated and explained in the appendix.
* See questions

### Weaknesses
 * Some claims on the similarity of extrapolated token positions are a bit weaker, and are primarily based on visually comparing the extrapolated and actual activations projected down to a low-dimensional space. I would have liked to have seen a more concrete metric of comparison, together with some baseline values to compare against to indicate that they really are close. The current visual comparison is insufficient to demonstrate the model's predictive power, as it relies on subjective interpretation of cluster proximity in a reduced dimensional space.
* I would have liked to have seen some applications of this discovery, or at least conjectures for what it could be used for. For example, could one project down the weight matrices into the space provided, and obtain a network that has similar performance and is much smaller, at the expense of off-distribution task degradation? Essentially, a way to distil a pre-trained network down if we only care about performance on one task? The paper lacks a discussion on the practical implications of the findings, and how they could be leveraged for model optimization or understanding.
* I would elaborate on the potential use-case for a continuous interpolation between layers. Is there any sort of intuitive meaning we can assign to this? The paper does not explore the potential of interpolating between layers, and it's unclear what insights this could provide. The authors should discuss the potential benefits and interpretations of such an operation.
* See questions

### questions:
 Questions: (annotated with line number/section)
125: The vector for every token is projected to form the logits, not just the last vector. For inference, we only care about the logits in the last token'th position, but that doesn't mean the logits must only come from there.
130: Algorithm 1 is overkill. Just saying "we cache the activations between each transformer block in the sequence position of the last token over a forward pass for each psuedo-sentence $s_i$" would be sufficient. The algorithm is not doing anything interesting that the transformer would not already do during a forward pass (other than the caching of activations).
145: It is advised for ICLR to notate the last token position for layer $t+1$ as $\mathbf{E}^{t+1}_{:, end}$ rather than $\mathbf{E}(t+1)[:, end]$ (check the ICLR formatting guide).
152: The latent space is obviously spanned by a Cartesian basis. Any such space is.
155: You then revert to the ICLR standard notation for indexing a matrix that you did not use on line 145. Pick one and be consistent.
175-176: Replace "Because the Cartesian axes, $\mathbb{e}_i$, are unlikely to align with trajectories meaningful directions," with "There is no reason a priori we would expect the Cartesian axes to align to meaningful directions for the trajectories of the activations"
177: Concatenating the $\mathbb{x}_k(t)$? Over what dimension? $k$ or $t$ or something else?
154: Does it makes sense to plot the trajectories such that at each layer we use a different basis? Seems like you'd want to use the same basis throughout the entire forward pass if possible, as then each step along the trajectory is measured in terms of something different. I guess maybe the size of the principal component, with respect to the most important eigenvector is still interesting. This was partially addressed by Fig. 2a. showing that all the dimensions are important at some point during the forward pass, and that the low-dimensional manifold "wanders around" the entire latent space.


Section 3.2: At first glance this seems a reasonable choice of metric: The KL divergence between the normal output distribution, and the output distribution after having performed dimensionality reduction via SVD. Is this a metric that is defined elsewhere in the literature? Cite if so. I wonder if SVD is the best thing to do here: Is there a better choice of low-dimensional manifold that can only be obtained via a non-linear transformation? Perhaps if an autoencoder was trained that compresses/uncompresses the latent space on forward passes, could you squeeze the activations into an even lower dimensional space while preserving the KL divergence?
However, what isn't clear to me is that how much displacement of KL divergence is a lot, and why $K_0 = 256$ was the value for which "most" of the true distribution is recovered. What is "most"? What makes a KL-divergence of ~0.7 "not much"? It would be good to have some sort of sense of scale what the downstream effects are (e.g. measure the performance on some benchmark before and after throwing away 75% of the activations, and see how much "dumber" the model gets.)

Figure 2(c): What precisely is the baseline defined as? The KL divergence between the output distributions conditioned on two unrelated inputs, or with random noise injected into the unembedding matrix, or something else?

Figure 3: It's not clear how to compare the true and extrapolated positions. If the cluster comparison is desired, maybe colour one red, and the other blue, but both have transparency? So the purple region is the overlap? It's hard to see with the grey just covering the blue. I also would have liked a more principled metric to measure how well the model suggested in Equation (1) captures the dynamics of the activations, and what component remains unexplainable.

255-256: The rotation matrix $\mathbf{R}(t)$ was substituted out for $\mathbf{U}(t)$, but $\mathbb{\Lambda}(t,\tau)$ was not substituted out for $\mathbb{\Sigma}(t+\tau)\mathbb{\Sigma}^{-1}(t)$. I think either substitute both (my preference) or neither.

619: Forgot to bold $\Lambda$

### Questions
Questions: (annotated with line number/section)
125: The vector for every token is projected to form the logits, not just the last vector. For inference, we only care about the logits in the last token'th position, but that doesn't mean the logits must only come from there.
130: Algorithm 1 is overkill. Just saying "we cache the activations between each transformer block in the sequence position of the last token over a forward pass for each psuedo-sentence $s_i$" would be sufficient. The algorithm is not doing anything interesting that the transformer would not already do during a forward pass (other than the caching of activations).
145: It is advised for ICLR to notate the last token position for layer $t+1$ as $\mathbf{E}^{t+1}_{:, end}$ rather than $\mathbf{E}(t+1)[:, end]$ (check the ICLR formatting guide).
152: The latent space is obviously spanned by a Cartesian basis. Any such space is.
155: You then revert to the ICLR standard notation for indexing a matrix that you did not use on line 145. Pick one and be consistent.
175-176: Replace "Because the Cartesian axes, $\mathbb{e}_i$, are unlikely to align with trajectories meaningful directions," with "There is no reason a priori we would expect the Cartesian axes to align to meaningful directions for the trajectories of the activations"
177: Concatenating the $\mathbb{x}_k(t)$? Over what dimension? $k$ or $t$ or something else?
154: Does it makes sense to plot the trajectories such that at each layer we use a different basis? Seems like you'd want to use the same basis throughout the entire forward pass if possible, as then each step along the trajectory is measured in terms of something different. I guess maybe the size of the principal component, with respect to the most important eigenvector is still interesting. This was partially addressed by Fig. 2a. showing that all the dimensions are important at some point during the forward pass, and that the low-dimensional manifold "wanders around" the entire latent space.


Section 3.2: At first glance this seems a reasonable choice of metric: The KL divergence between the normal output distribution, and the output distribution after having performed dimensionality reduction via SVD. Is this a metric that is defined elsewhere in the literature? Cite if so. I wonder if SVD is the best thing to do here: Is there a better choice of low-dimensional manifold that can only be obtained via a non-linear transformation? Perhaps if an autoencoder was trained that compresses/uncompresses the latent space on forward passes, could you squeeze the activations into an even lower dimensional space while preserving the KL divergence?
However, what isn't clear to me is that how much displacement of KL divergence is a lot, and why $K_0 = 256$ was the value for which "most" of the true distribution is recovered. What is "most"? What makes a KL-divergence of ~0.7 "not much"? It would be good to have some sort of sense of scale what the downstream effects are (e.g. measure the performance on some benchmark before and after throwing away 75% of the activations, and see how much "dumber" the model gets.)

Figure 2(c): What precisely is the baseline defined as? The KL divergence between the output distributions conditioned on two unrelated inputs, or with random noise injected into the unembedding matrix, or something else?

Figure 3: It's not clear how to compare the true and extrapolated positions. If the cluster comparison is desired, maybe colour one red, and the other blue, but both have transparency? So the purple region is the overlap? It's hard to see with the grey just covering the blue. I also would have liked a more principled metric to measure how well the model suggested in Equation (1) captures the dynamics of the activations, and what component remains unexplainable.

255-256: The rotation matrix $\mathbf{R}(t)$ was substituted out for $\mathbf{U}(t)$, but $\mathbb{\Lambda}(t,\tau)$ was not substituted out for $\mathbb{\Sigma}(t+\tau)\mathbb{\Sigma}^{-1}(t)$. I think either substitute both (my preference) or neither.

619: Forgot to bold $\Lambda$

### Soundness
3

### Presentation
4

### Contribution
3
