# Monet: Mixture of Monosemantic Experts for Transformers

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Understanding the internal computations of large language models (LLMs) is crucial for aligning them with human values and preventing undesirable behaviors like toxic content generation. However, mechanistic interpretability is hindered by \emph{polysemanticity}—where individual neurons respond to multiple, unrelated concepts. While Sparse Autoencoders (SAEs) have attempted to disentangle these features \textcolor{rebuttal}{through sparse dictionary learning,  they have compromised LLM performance due to reliance on post-hoc} reconstruction loss. \textcolor{rebuttal}{To address this issue,} we introduce \textsc{Mixture of Monosemantic Experts for Transformers} (\textsc{Monet}) architecture, which \textcolor{rebuttal}{incorporates sparse dictionary learning directly into end-to-end Mixture-of-Experts pretraining.} \textcolor{rebuttal}{Our} novel expert decomposition method \textcolor{rebuttal}{enables scaling the expert count} to 262,144 per layer while total parameters scale proportionally to the square root of the number of experts. Our analyses demonstrate mutual exclusivity of knowledge across experts and showcase the parametric knowledge encapsulated within individual experts. Moreover, \textsc{Monet} allows knowledge manipulation over domains, languages, and toxicity mitigation without degrading general performance. \textcolor{rebuttal}{Our pursuit of transparent LLMs highlights the potential of scaling expert counts to enhance} mechanistic interpretability \textcolor{rebuttal}{and directly resect the internal knowledge to fundamentally adjust} model behavior.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new transformer architecture that replaces MLP layers in the standard decoder-only transformer architecture with a type of sparse coding layer which encourages only a small number of hidden neurons to activate on each given input. The construction is also motivated by, and borrows ideas from, the mixture of experts (MoE) literature. The primary motivation of this new architecture is to help interpretability by building something akin to a wide Sparse Autoencoder (SAE) into the MLP layers of the decoder-only transformer architecture in a scalable way, so that we can directly train for sparse (and thus hopefully interpretable) internal activations.

In more detail:
- the MLP layer is viewed as an associative memory, and replaced with a sparsely activating version inspired by the paper "Large memory layers with product keys". 
	- The MLP layer is replaced by multiple smaller MLP subnetworks ("experts") that share parameters in a specific way inspired by the product idea from "Large memory layers with product keys" to effectively represent many experts using only a few trainable parameters. 
	- A sparse subset of the experts is chosen to produce the final output as an expectation over these layers' outputs (similar to attention)
	- There are other engineering optimizations used to make the computation more efficient.
	- Finally, auxiliary loss terms are added, encouraging the experts to activate uniformly on average ("load balancing") and each token to have a highly activating expert (ambiguity loss).
- This new architecture is trained on 100B tokens sampled from the FineWeb-Edu dataset (a subset of experiments also uses a programming dataset), using LLaMA trained on the same dataset as a baseline across approx. 850M, 1.4B and 4.1B parameters. The MONET architecture uses an effective count of $2^18=262,144$ experts. Comparisons on question-answering benchmarks such as MMLU show that the architecture performs mostly on par with the LLaMA baseline. 
- As an additional baseline, SAEs for Gemma 2B are used to patch in Gemma-2B's original activations, and the performance drop due to the SAEs is measured. 
- Some qualitative analyses of the contexts that activate a given expert subnetwork are performed.
- The architecture is then applied to selectively delete model knowledge in three setups: subject-specific knowledge in MMLU (e.g. delete only knowledge of chemistry but not economics etc.), programming language-specific knowledge on a code dataset (e.g. delete only knowledge of Python but not Java), and purging toxic experts.

### Strengths
- The paper tackles an interesting and important question for the field: instead of interpreting LLMs post-hoc, can we directly train them in a way that results in interpretable weights? 
	- This adds to existing work, such as backpack LLMs https://arxiv.org/abs/2305.16765 and codebook features https://arxiv.org/abs/2310.17230
- The proposed architecture is interesting, can (in principle) represent a large number of experts, and performs on par with the LLaMA baseline of roughly the same parameter count.
- The applications to targeted erasure of knowledge are very interesting and relevant to the field.
- The writing is clear

### Weaknesses
 - The lack of detailed interpretability baselines makes it difficult to evaluate the strength of the results. 
	- For example, the only interpretability method used as a baseline is patching reconstructions from SAEs for Gemma-2B. However, it is not reported what sparsity these SAEs achieve compared to the (effective?) sparsity of MONET. This makes it difficult to make sense of the results. 
	- The only relevant baseline here is using SAEs at the MLP layers, because this matches the MONET setup; so, the residual stream SAEs seem irrelevant for this work?
	- Furthermore, SAEs are trained to reconstruct activations coming from the original model being studied, and iteratively applying the SAE reconstructions to MLP layers may take downstream activations off-distribution, leading to an accumulation of errors due to SAE composition. You may argue that this is just a drawback of the SAE paradigm that MONET avoids, and the comparison is still fair. However, from my point of view, the primary goal of SAEs is to find interesting concepts used by the model, and reconstruction is secondary to that (and being able to chain SAE reconstructions is even more secondary). So, ideally the baseline would compare the "monosemanticity" of MONET features vs SAE ones.
	- A baseline using the ordinary MLP neurons of the LLaMA model would be very valuable to make the point that MONET discovers more interpretable structure compared to the neuron basis
- The paper would benefit from a discussion of, and comparison with, related work, such as backpack language models and codebook features.
- Perhaps adding extra bells and whistles like instruction tuning or multimodality distracts from the main goal of the paper, which is to establish the usefulness of the new architecture for interpretability (which I believe can be achieved or falsified in a more basic setup)

### Questions
- How exactly were the top experts by subdomain chosen for the Gemma-2B SAEs? Note that SAEs have no notion of probability over the "experts", unlike the MONET model, and I could not find this addressed in the paper. Do you pass the hidden SAE activations through a softmax first? 
- What is the scale in figure 2?
- Have you tried running the MONET features through an automated interpretability pipeline like https://github.com/EleutherAI/sae-auto-interp?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the use of Mixture of Experts as a way to have more interpretable models in the context of polysemanticity. They change the standard MoE architecture in that they use product key retrieval technique as a router and they have experts associated with each key. They consider two strategies to create the model: horizontal expert decomposition and vertical expert decomposition, and finally explain how to train their models (Section 3). In the experiments section (Section 4), they show that the experts display monosemanticity and that removing some experts from some domain yields significant performance degradation (Sections 5.1 and 5.2). The Monet approach also allows to purge toxic experts from the model, which is interesting from a safety perspective.

### Strengths
I like the idea of the paper. Some earlier works noticed that experts display some monosemanticity [1,2] and it is great to see this work push this idea. I also think that the set of experiments is very convincing and I believe that this work may be influential for getting more interpretable neural networks.

[1] Fedus, William, Barret Zoph, and Noam Shazeer. "Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity." Journal of Machine Learning Research 23.120 (2022): 1-39.

[2] Fedus, William, Jeff Dean, and Barret Zoph. "A review of sparse expert models in deep learning." arXiv preprint arXiv:2209.01667 (2022).

### Weaknesses
I think the main weakness of the paper is the presentation + writing, especially in Section 3. I am happy to consider improving my score if much better explanations of the method are given in Section 3.

- **Section 3 should be more clear (especially the Horizontal and Vertical decomposition)**: I read the work by Lample et al. [1] for completing this review and according to my understanding, there is a unique $(u_i, v_i)$ that is associated with each key. Their approach makes sense to me.

  -- I am very confused why there is the mix and match (along the horizontal or the vertical) in this paper. And also, why is there any memory savings (compared to the PEER approach)? And why is each expert of dimension m (while in PEER, it is a single neuron).


  -- I also recommend the authors to do a complexity calculation like in [1], Section 3.2 to be fully transparent on the memory/computation complexities.

  -- I also didn’t find Figure 1 very clear, for instance it was not clear what “Top”, “bottom” or “TL”, “BL” refer to. Above all, I think that this drawing should be improved.


- **Lack of baselines**: It is also not clear to me that a whole new architecture is needed to ensure a more interpretable model. For instance, [2,3] showed that standard MoEs display monosemanticity behaviors. Therefore, I think it is important to maybe compare the Monet method with standard MoEs. Would for instance fine-grained MoEs [4] work in this case? Is it the fact that we have a lot of experts that is responsible for more “monosemantic” experts? Or the routing strategy is responsible for it? I just want to be convinced that no simpler architecture would lead to the results obtained in Section 4.

### Questions
I listed my question in the weaknesses section.

### Soundness
3

### Presentation
2

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
This paper presents a new architecture that makes large language models more interpretable with monosemanticity. The authors develop novel decomposition methods to efficiently scale to 262K experts per layer, achieving specialists that focus on single concepts through end-to-end training. The model also enables control over model knowledge (across domains, languages, and toxicity) without degrading performance, outperforming traditional Sparse Autoencoder approaches.

### Strengths
- The paper presents novel decomposition methods that scales traditional MoE to 262k experts.
- The paper delivers comprehensive experimental results on the proposed model architecture.
- The proposed method achieves good expert specialization, proven under several experimental settings

### Weaknesses
 - The intuition behind the architecture design is unclear.
- The explanation in the methodology section is poor and hard to understand.



### Questions
- What's the reason of choosing $512^2$ number of experts?
- Are there any trade-offs for adopting Monet over traditional MoE? What is the training time comparison between Monet and LLaMA baseline models?

I suggest the authors to elaborate more on the methodology section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose Monet. A new sMoE achitecture built on top of PEER. By pushing the notation of expert to the limit, Monet shows superior performance and unique ability to unlearn domain knowledge by simply masking out experts.  Further analyses demonstrate mutual exclusivity of knowledge across experts and showcase the parametric knowledge encapsulated within individual experts.

### Strengths
* Simple and straightforward idea
* The experiments on domain masking and unlearning is interesting

### Weaknesses
 * Presentation can be greatly improved. For example, figure 1 does more confusing than explaining. There is zero followup in the caption telling the readers what "E1", "BL2", "TL2" are. Because they are arbitrary abbreviation defined by the authors, they should be properly annotated, or simply just use the full name.
* No proper ablations to study different choices in the architectural design and no insight is provided. For example, can we mix Horizontal Expert Decomposition and vertical expert decomposition? Which part of the changes over PEER make it superior?
* No baseline comparison against PEER and traditional SMoE. How come these two most obvious baselines are missing?

Some other minor issues:
*  citation to PEER is missing. 
*  Incremental proposal on top of PEER, I am uncertain how significant the contributions are

### Questions
* What does the model start with in table 3?

### Soundness
3

### Presentation
2

### Contribution
2
