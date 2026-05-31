## Human Reviewer 1

### Summary
The authors investigate the applications of using a compressed latent representation in the context of motion planning. Their work is motivated by prior research suggesting that a strong decoder model can reduce the required latent dimensions to reconstruct the target data. They propose a quantized latent representation that they suggest improves when learned using an adaptive noise distribution. Their experiments are on the Waymo Open Motion Dataset, where they show the re-usability of their latent features by analyzing the re-usability of the features in capturing motion meaning and reconstruction quality.

### Strengths
> The motivations for the author's research are sound. Classical motion planning algorithms do not scale well to extensive dimensional data, so using low-dimensional latent representations to enable their use makes sense

> The application of a compressed latent space is an interesting idea, and the authors' research has practical applications. 

> Figure 4 illustrates the model architecture proposed by the authors.

### Weaknesses
We found it challenging to follow the submitted paper draft. Many sections require rewriting for clarity, where even small details are not serving to communicate the author's point. The title suggests a generalist representation approach to robotics, but the authors only apply their autoencoder approach to a self-driving data set. Much of the paper discusses robotics in a general sense, but since the experiments focus only on autonomous driving, I consider this misleading to readers. It would serve the paper better to focus on this application rather than use general-sounding language (e.g., "robotics tasks" should really be "self-driving").  The author's method may have applications in other domains, but as they do not demonstrate this in the experiments, it might be better to discuss this only in the conclusion as future work. 

Furthermore, sections 2 & 3 in particular would benefit from extensive rewriting. It could be helpful to clarify how the latent codes are combined with classical motion planning in Section 2. Section 3 should be clearer that these are the experiments. Even just changing the section header to "Experiments" or clearly stating the experiments' objectives in the preamble would already be an improvement.

The writing also makes it difficult to determine the paper's significant contributions or its advantages. For example, Table 2 shows several models surpass the author's model performance (e.g., DriveGPT has 0.5240 minADE_6 vs the author's 0.6415). It is mentioned that the author's latent space is notably smaller; what about the decoder model's capacity in comparison? Do the baseline models use larger or smaller decoders?. Likewise, quantization is emphasized as necessary, but the reported metrics in Tables 1 & 5 suggest that excluding quantization leads to better performance.  Similarly, it is not clear from the discussion in Table 4 why matching Motion-LLaVA is essential, and should be clearly stated in the writing.  Given these issues, we believe the paper as a whole needs improvements not just in writing but also in its empirical evaluations to strengthen its claims. 

Comments on Method:
Section 2.1 (Line 14): the quantization scheme described should cite prior research that reports a closely related (near-identical) approach [1]. This work was not mentioned in the related work. 

[1] Mentzer, Fabian, et al. "Finite Scalar Quantization: VQ-VAE Made Simple." The Twelfth International Conference on Learning Representations.

> Figure 2: This idea of nosing latent embeddings has been considered in other research. VAEs do this with the reparameterization trick, yet this feature is prominently established throughout the author's work (e.g. Figure 1 shows how vital this regularization trick is). If this adaptive noising approach is beneficial, it would be better justified if alternative noising schemes (i.e. a stochastic latent variable such as from a VAE) were compared against.




Writing Opinions

> The introduction as a whole could be improved for clarity. We suggest restructuring the focus to the limitations of motion planning and the benefits of autoencoders to address these problems, rather than discussing autoencoders and treating motion planning as secondary. 

> Line 036:  "autoregressive" is ambiguous in this sentence; make it more specific. 

> Line 038: "autoencoder" is not set up well in this paragraph and is confusing to read about as written. 

> Line  488 - 492:  Combine content into a single paragraph

### Questions
Q1: Have the authors considered training a decoder that only relies on the latent variable for reconstruction? Is the reason the latent space can be compressed so much because of these additional inputs? 

Q2: What is the red square input to the decoder model?

Q3: Why did the author use the WOMD dataset? In what other domains could this method be employed? 

Q4: We find the results in Figure interesting. What do the authors believe explains this observed re-usable aspect of their latent representation?

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
2

---

## Human Reviewer 2

### Summary
This paper proposes a method to leverage recent deep learning advances in motion planning for robotics with traditional search and optimisation based planning algorithms. The key contribution is the ability that the method provides to optimise arbitrary objectives specified by the user without having to retrain or fine-tune these networks, simply by relying on the pretrained autoencoder. The results of this method are demonstrated on the Waymo Open Motion dataset for both motion prediction and behaviour generation.

### Strengths
- The approach aims at utilising one of the biggest insights from the past few years regarding the impact of large-scale real-world data to learn useful priors about the world, and channeling it to robotics to enable the use of traditional search algorithms in robotics.
- Claims on composability of objectives in the driving scenario and greedy search versus learned encoder are well substantiated.
- The main advantage of this work is the cheap adaptation tailored to the user’s objective, without having to perform additional training.

### Weaknesses
- One of the main weaknesses of the paper is the reliance of the empirical study on a single dataset, the Waymo Open Motion dataset. This makes it difficult to assess the generalisation of this approach to other robotics domains.
- A key advantage of this approach described in the paper is the ability to use these compact latent tokens in conjunction with search algorithms. However, the only search studied in this paper is greedy search. Again, the issue of generalisation comes up in how this method would work with other search strategies like beam search or Monte-Carlo Tree Search.
- When talking about real-world domains, a critical aspect is that of reliability and safety, which is not adequately addressed in this paper. Given that the paper attempts to provide a cheap way to achieve different user-guided behaviours, guarantees of reliability and safety, or the lack thereof, should be addressed.

### Questions
This work positions itself as one that gives a best-of-both-worlds scenario for foundation models for robotics and self-driving, and search and planning algorithms. However, since it is heavily dependent on having a high quality autoencoder, which in turn depends on having a large diverse dataset, could the authors shed some light on how such a method might be used in a low-data regime? No new results are required, just an intuitive understanding on how one might leverage the proposed method in robotics domains where large datasets are not available.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper proposes planning as search in a learned discrete latent space. A conditional transformer autoencoder is trained on WOMD to produce causally-ordered, low-dimensional, quantized tokens for trajectories; at test time, the decoder serves as a strong generative prior while a greedy tree search over tokens optimizes arbitrary user objectives (e.g., “turn left”, “slow down”). The model also explores multi-agent tokenization and shows that tokens convey semantic behaviors (token swapping, “library of behaviors”). Key ingredients include adaptive soft quantization at the bottleneck, nested dropout to enforce coarse-to-fine token order, and hard quantization during search. Experiments cover reconstruction, prediction via variance-minimizing search, guided maneuver generation, and a multi-agent VQA proxy by feeding tokens to an LLM.

### Strengths
1. Crisp conceptual unification. The paper cleanly separates objective choice at test time from trajectory realism via the decoder, and leverages an ultra-compact latent space to make tree search feasible.

2. Simple, well-motivated mechanics. Adaptive noise (“soft quantization”) and nested dropout jointly encourage discrete, ordered latents; this is elegant and empirically helpful (Fig. 2).

3. Compelling token semantics. Token swapping and “behavior libraries” show transferable high-level behaviors, not just compression (Fig. 5).

4. Test-time flexibility. Greedy token search handles different objectives without retraining (left-turn, slow-down), while the decoder enforces map-consistency (edge-contact ≈0%).

5. Multi-agent extension. Joint tokenization (up to 8 agents) plus simple goal objectives yields qualitatively consistent interactions; tokens also aid an LLM on WOMD-Reasoning.

### Weaknesses
1. Planning evidence is under-baselined. Section 3.4 reports maneuver “success rate” and edge-contact against the unmodified scenario, but no planning baselines (trajectory optimization, sampling-based planners, MPPI/IT-MPC, or diffusion planners) are included. As a result, it’s hard to judge optimality/efficiency and where search in latents sits among standard planners.

2. Scalability beyond toy latent sizes is unclear. All strong results use very small spaces (e.g., N=3 tokens, D=3 dims, Nlevels=2), where greedy cost is merely N·Nlevels^D = 3·2^3 = 24 decoder calls. The paper acknowledges this efficiency (≈115 traj/s on RTX 6000 Ada), but does not test larger N/D/Nlevels where branching explodes and greedy likely degrades. A scaling study is essential.

3. Objective realism and multi-objective tradeoffs. The showcased costs (cumulative left heading; target final speed) are simple and largely single-objective. Real planners optimize safety/comfort/progress and constraints (jerk, acceleration, distance to agents). The method’s greedy, token-by-token decisions might be myopic under competing objectives; no experiments probe this.

4. Reliance on decoder variance as a guard-rail is risky. Prediction and planning searches penalize decoder-predicted variance, but heteroscedastic NNs can be miscalibrated (the paper cites this literature). There are no calibration diagnostics (PIT, ECE, risk-coverage), so search could be steered by poorly calibrated uncertainty.

5. Limited safety metrics for interactions. Planning reports edge-contact with static map; dynamic-agent collisions, min-distance, TTC are not measured. Multi-agent results are mainly qualitative (Fig. 6) and a language metric table (Table 4) that doesn’t evaluate physical safety of generated interactions.

6. Causal ordering assumption not validated against optimization. The paper assumes nested-dropout + causal masking yields a coarse-to-fine order that aligns with greedy objective optimization. Evidence is indirect (reconstruction improves with more tokens; Fig. 3). There’s no analysis showing early tokens control “coarse” semantics relevant to downstream costs.

7. Open-loop feasibility and dynamics. The decoder produces kinematically smooth trajectories, but there’s no explicit vehicle dynamics or closed-loop execution. It’s unclear if generated plans remain feasible/stable under tracking noise or model errors.

### Questions
1. Scalability: What is planning quality/runtime as N, D, Nlevels increase? Have you tried beam search or MCTS in latent space, and how do they compare to greedy for complex objectives? (Complexity ≈ N·Nlevels^D per greedy layer.)

2. Baselines: Can you add at least one trajectory optimizer (with the same costs) and one sampling/diffusion planner on the same WOMD slices used in Table 3?

3. Safety metrics: For planning and multi-agent generation, can you report collision rate, min distance, jerk/accel, and rule/route compliance in addition to edge-contact and success rate?

4. Uncertainty calibration: How calibrated is the decoder’s variance? Any risk-coverage or PIT plots before using it to gate search?

5. Causal ordering verification: Can you intervene on individual tokens to quantify their semantic scope (e.g., MI between token i and global maneuvers vs. local kinematics), supporting the coarse-to-fine claim?

6. Closed-loop: Have you tested tracking a decoded plan with a simple controller (bicycle or PID) to measure closed-loop feasibility and regret?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4