# Scaling and evaluating sparse autoencoders

- Decision: Accept
- Avg Score: 8.20
- Scores: 3, 10, 10, 8, 10

## Abstract
Sparse autoencoders provide a promising unsupervised approach for extracting interpretable features from a language model by reconstructing activations from a sparse bottleneck layer.  Since language models learn many concepts, autoencoders need to be very large to recover all relevant features.  However, studying the properties of autoencoder scaling is difficult due to the need to balance reconstruction and sparsity objectives and the presence of dead latents.  We propose using k-sparse autoencoders \citep{makhzani2013k} to directly control sparsity, simplifying tuning and improving the reconstruction-sparsity frontier. Additionally, we find modifications that result in few dead latents, even at the largest scales we tried.  Using these techniques, we find clean scaling laws with respect to autoencoder size and sparsity.  We also introduce several new metrics for evaluating feature quality based on the recovery of hypothesized features, the explainability of activation patterns, and the sparsity of downstream effects. These metrics all generally improve with autoencoder size.  To demonstrate the scalability of our approach, we train a 16 million latent autoencoder on GPT-4 activations for 40 billion tokens.blob.core.windows.net/sparse-autoencoder/sae-viewer/index.html}{visualizer}.blob.core.windows.net/sparse-autoencoder/sae-viewer/index.html}{https://openaipublic.blob.core.windows.net/sparse-autoencoder/sae-viewer/index.html}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes the use of a k-sparse auto encoder model to  control sparsity, simplifying tuning and improving the reconstruction-sparsity frontier. The paper presents results showing better reconstruction and minimal dead latents. The authors trained a 16-million latent autoencoder on GPT-4 activations over 40 billion tokens, demonstrating clear scaling laws for the autoencoder size and sparsity. The main contribution of the paper is the use of TopK activation to limit the number of active latents and presenting metrics of latent quality.

This limiting factor seems to play a role in allowing scaling the model for larger encoders as demonstrated  experimentally on GPT2 with multiple ablation studies and an in-depth evaluation downstream loss, explainability amongst other metrics.

### Strengths
1. The adoption of k-sparse autoencoders with TopK activation is a significant improvement over traditional ReLU-based models. By directly controlling the number of active latents, TopK provides a straightforward way to balance reconstruction quality and sparsity, simplifying tuning and improving interpretability.

2. The study of scaling laws for sparse autoencoders across various dimensions—autoencoder size, language model size, and sparsity—is well-executed. This contributes valuable insights into how autoencoders behave at larger scales, especially when trained on large models like GPT-4. Clear scaling patterns provide guidelines for researchers to optimize model size and token budgets effectively.

3. The authors address the issue of "dead latents" effectively by using specific initialization and auxiliary loss techniques. This innovation minimizes computational waste and improves model efficiency, making it feasible to train much larger autoencoders while keeping most latents active, even at high scales.

4.The paper introduces thoughtful metrics that go beyond simple reconstruction errors to evaluate feature quality. Metrics like downstream loss, probe loss, explainability, and sparsity of downstream effects offer a more nuanced assessment of latent quality, highlighting the interpretability of features that the autoencoders extract. This focus on interpretability is particularly important for mechanistic understanding and applications in AI alignment.

5. The use of TopK avoids the activation shrinkage problem that commonly affects ReLU-based sparse autoencoders. This makes TopK particularly suitable for training sparse models without the need for additional regularisation to combat shrinkage, which simplifies model training and improves performance.

### Weaknesses
1. As highlighted in the limitations section, The TopK activation function might be overly restrictive. Each token must use exactly k latents, which could be suboptimal for capturing certain features that require more flexible sparsity levels based on input complexity. The fixed-k sparsity may limit the model's ability to adapt to varying information densities within the input, potentially hindering its performance on complex data where different parts of the input might require different levels of latent activation.

2. The experiments primarily use a context length of 64 tokens, which may not capture longer dependencies present in language models like GPT-4. By not exploring larger context lengths, the paper might miss behaviors and interactions that occur over more extended sequences, which could be valuable for understanding latent patterns and achieving higher interpretability. This limited context length might prevent the model from learning higher-level, more abstract features that span longer sequences of text.

3. Although the paper introduces meaningful metrics for interpretability, some, like the downstream loss and explainability evaluations, require substantial computational resources, particularly for large models like GPT-4. This computational burden makes it challenging to validate the findings across a wider range of settings and could limit the practical applicability of these metrics for researchers with limited resources.

4. The reliance on an auxiliary loss to prevent dead latents may add extra complexity to the training process. While effective, this approach could complicate optimization and might be sensitive to tuning, making it more challenging to reproduce results consistently across different datasets and architectures. The introduction of an additional loss term could also introduce new hyperparameters that need careful tuning, further complicating the training process.

5. Although the approach seem to scale on relatively smaller model, it is not clear how scalable this approach for much larger model.s

6. While the paper discusses applications like anomaly detection and mechanistic interpretability, there is limited empirical testing in these areas. Applying these sparse autoencoders to real-world tasks and evaluating their practical benefits would strengthen the claim of their utility and robustness across applications. Without empirical validation on real-world tasks, the practical relevance of the proposed method remains somewhat speculative.

7. The explainability metric, which relies on methods like Neuron to Graph (N2G), is noted to have high recall but lower precision. This can create an "illusion of interpretability," where explanations seem broad but lack specificity. The paper briefly acknowledges this, but a more in-depth exploration of how to balance recall and precision would improve confidence in these metrics.

### Questions
1. Could you elaborate on the choice of fixed-k sparsity? Do you foresee any scenarios where adaptive sparsity (varying k based on input complexity) might improve model performance or interpretability? Have you experimented with such approaches?

2. Given that TopK activation controls sparsity effectively, do you see potential limitations of this method in real-world applications, where sparsity needs may vary dynamically?

3. Could you share more about how the interpretability metrics were validated? For instance, have you found that these metrics correlate well with human judgment in terms of interpretability?

4. How sensitive is the auxiliary loss to hyperparameter changes, particularly at larger scales? Could you share any guidelines or best practices for tuning this component?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors present a well written paper which makes multiple significant contributions to the field of language interpretability. The paper does not explicitly pose a set of questions, but the subject matter implies several concerns:
1. Do sparse autoencoders scale to larger models? Does this require more latents than for larger models?
2. Can sparse autoencoder training be improved? For example, can it be made simpler via use of a top-K activation function? 
3. How should we evaluate sparse autoencoders? Are there alternatives to the sparsity-reconstruction pareto-frontier framing?

The paper makes a number of contributions. 
1. First, they propose a novel training recipe based on the use of the Top-K activation function for directly imposing sparsity in the sparse bottleneck layer. They evaluate their methods against similar proposed methods via the sparsity-reconstruction pareto-frontier framing and find their recipe is competitive with the best methods in the existing literature.
2. Second, they demonstrate scaling laws for their sparse autoencoder training recipe using the GPT4 family of models. 
3. Finally, they introduce a number of additional metrics for evaluating sparse autoencoders including loss-based metrics, metrics which rely on labeled datasets, automated interpretability and ablation sparsity. 

The strongest contribution of the paper is clearly the application of SAEs to exceptionally larger models, showing that sparse autoencoders scale to such models, but the paper also makes numerous other contributions around training and evaluation methods.

### Strengths
## Strengths by Section:

**Training Recipe**: The paper is unusually detailed with respect to the training recipe, which provides more clarity than similar publications about the training of sparse autoencoders. As noted by the authors, use of the Top-K activation function in a sparse autoencoder is not new, but it is novel in the context of sparse autoencoders trained on model activations. Importantly, it solves a previously documented issue called "shrinkage" which results in latent activations being biased towards activating less strongly than they theoretically should. 

**Scaling laws**: The paper demonstrates not only the training of sparse autoencoders on a SOTA language model, substantiating claims that this technique is scalable. Use of GPT4 provides one of the strongest possible arguments that sparse autoencoders can scale to very large LLMs. Additionally, the authors provide clear scaling laws in terms of the compute, data and number of latents. Though possibly a minor detail, we appreciate that the authors highlighted their initial incorrect prediction that there would need to be non-zero irreducible loss (as such comments help inform readers that the result was not obvious and thus increases readability and makes the significance clearer). 

**Evaluating SAEs**: Though plausibly it would be reasonable to separate work scaling sparse autoencoders from work exploring how best to evaluate them, we appreciate the attempt to rectify the current gap in the literature around how to evaluate sparse autoencoders. Contributions in this section are well motivated and varied. Section 4.3 is particularly valuable, as Neuron 2 Graph is a plausibly much cheaper way to perform automatic interpretability as opposed to the use of language models. 

## Strength by Dimension

**Originality**: While the work mostly combines existing ideas from the literature placing them in the context of sparse autoencoders trained on model activations, this hardly diminishes the contribution. Some ideas may be more clearly novel than others (such as the pre-training compute based metric that enables better interpretation of the increase in downstream loss in section 4.1). 

**Quality**: The work is generally high quality. There are no glaring issues that I can see. 

**Clarity**: Details of both the methods and reasoning are generally high quality.

**Significance**: The paper is highly significant due to contributions along multiple lines (training recipe, scaling laws and evaluation of SAEs).

### Weaknesses
 **Training Recipe:** 
- We appreciate that the proposed method eliminates the need for finetuning of the L1 coefficient (though choice of the number of activated latents is still required). We might interpret later analysis as attempting to identify a more principled way for setting the number of activations (setting K), though in the absence of better motivation, directly setting the number of activating latents isn’t clearly valuable. 
- Comparison of sparse autoencoder architectures is somewhat shallow, looking only at the sparsity-reconstruction pareto frontier. For example, the authors do not attempt to compare latents found by each method to establish whether they provide similar or distinct decompositions (is there often a 1:1 map between latents in sparse autoencoders trained via each method?). 
- The authors could have provided demonstrations that top-K sparse autoencoders work on toy models of superposition (as has been previously done to establish reason to prefer one architecture over another).
- Whilst the authors consider alternative methods for evaluating sparse autoencoders later in the work, they should have revisited the training recipe comparison in the context of their other evaluation methods. It is unclear whether Gated / topK SAEs would be comparable on all evaluation methodologies.
- The authors miss one possible issue with top-K activation functions. Use of the Top-K activation function means that the activation of a given latent cannot be calculated independently of others which is a minor but real obstacle to working with very large autoencoders (for example, when identifying max activating examples, one must first calculate all latent activations, then select the top-K latents). 
- Training on 64 token context sizes might affect the results. The models studied certainly can handle much longer prompts. The authors don’t note whether the SAEs generalize to activations produced during the process of larger numbers of consecutive tokens. 

**Scaling Laws**. We have no specific comments on the weaknesses of this section. 

**Evaluating SAEs**
- Though contributions in this section are valuable, there is an absence of discussion resolving possible metrics and identifying which are best to use in practice. Though many related papers likely deal with the current uncertainties of the field similarly (by presenting various possible motivations / metrics without meaningfully resolving which is best). We believe that devoting more of the discussion to comparing metrics and resolving insights found via each may be fruitful.
- (Repeating a point from earlier) The authors don’t evaluate non-TopK autoencoders via any of the new metrics leaving possibly valuable insights on the table. 
- Section 4.2 could have used a linear probe on the model activations as a baseline against which to compare the 1d logistic probe results. The authors also don’t perform any error analysis or raise any particular examples of latents which clearly track expected features of the input. While such qualitative analysis may not scale, it might possibly provide much better intuition about the results. The authors don’t address how sparse combinations of latents might jointly represent features.
- The authors could attempt to compare Neuron 2 Graph explanations to those produced by language models (which is the norm for automatic explanations of features in the rest of the sparse autoencoder literature).

### Questions
Some work that might improve this paper:
- Checking whether top-K sparse autoencoders find the same latents as other methods. Reliance on summary statistics when making comparisons between architectures could be misleading. 
- Establishing that top-K sparse autoencoders work well on toy models of superposition (and using this to better explain why top-K might be better than other architectures).
- Using longer prompts than 64 tokens when training sparse autoencoders (this seems rather short) or instead providing an empirical analysis showing that this hyperparameter has no meaningful impact on results. 

Since my overall impression of the paper is quite good, and most of the weaknesses, if addressed, would substantially increase the length of the paper, I don't believe addressing any given issue is essential.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper develops training methodology and scaling laws for a new sparse autoencoder (SAE) variant - TopK SAEs, which replaces the L1 penalty in the standard SAE (https://transformer-circuits.pub/2023/monosemantic-features) with a TopK filter, so that the desired sparsity of activations can be set directly. The new architecture is evaluated against other popular SAE variants along the reconstruction-sparsity frontier. The interpretability of the TopK SAE latents is also measured via several novel metrics.

In more detail:
- the TopK filter overcomes the shrinkage problem associated with the L1 penalty, allowing better reconstruction with the same sparsity;
- to minimize dead latents, the TopK training method uses a simple initialization strategy and an auxiliary loss that incentivizes the dead latents to reconstruct the error of the SAE.
- scaling laws for TopK are studied w.r.t. various parameters, such as the number of latents, the $k$ value, and the size of the model whose activations SAEs are trained on. 
- several evaluations beyond MSE/sparsity tradeoffs are performed:
	- downstream loss when SAE reconstructions are patched in
	- using individual SAE latents as probes for binary classification tasks 
	- simple autointerpretability based on Neuron to Graph (N2G)
	- evaluating how sparse the effect of ablating SAE latents is on logits of the model

### Strengths
- the paper presents a new, simpler SAE architecture and training stack that demonstrably scales to frontier models and many SAE latents. The main advantages over concurrent work are:
	- the sparsity can be set directly, making it easier to do hyperparameter tuning;
	- the training recipe is also simple and with few knobs to tune;
	- yet results on the MSE/sparsity frontier are state of the art, and there are very few dead latents
- many of the findings are quite well supported by extensive comparisons with other SAE variants
- the discussion on the limitations of autointerpretability methods in 4.3. is illuminating
- the paper proposes some new and interesting interpretability evaluations, especially probing and sparsity of downstream effects

### Weaknesses
 - as the authors are already aware, using individual SAE latents as probes for very high-level binary tasks (such as sentiment) may be too restrictive, especially in light of phenomena such as feature splitting. This limits the significance of the results
- another practical limitation of the TopK architecture is that it forces every activation to use exactly $k$ active features. In practice (at least in my experience) this may lead to many unimportant features to activate. See concurrent work https://www.alignmentforum.org/posts/Nkx6yWZNbAsfvic98/batchtopk-a-simple-improvement-for-topk-saes
- the interpretability evaluation is at times too reliant on high-level aggregate metrics. For instance, how should we interpret the "sparsity of downstream effects" numbers?
- the presentation on scaling laws would benefit from a comparison with concurrent work by Anthropic: https://transformer-circuits.pub/2024/scaling-monosemanticity/#scaling-scaling-laws
- there is some inconsistent notation (e.g., using $N$ and $n$ for the number of latents) and some missing symbols from the text

### Questions
- did you use the scaling laws to choose hyperparameters for the largest SAE training runs? Do you know how well that worked?
- Have you thought about ways to more scalably evaluate precision of SAE latent explanations?

### Soundness
4

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
In this paper, the authors scale and evaluate sparse autoencoders (SAEs) on modern large language models (LLMs) across different model sizes (up to GPT4).

The main contributions are as follows:
- SAEs are trained and evaluated across different model sizes, and scaling laws are found.
- The top-k activation function is leveraged to obtain state of the art results, and its ability to avoid activation shrinkage is explored
- An auxiliary loss is devised, and it significantly reduces the amount of dead features
- New metrics are introduced for evaluation: the explanation loss (obtained using just interpretable explanations), and the probe loss (where the authors check wether the SAE reproduces known features).

My **recommendation**: Accept, 8/10 (good paper).

### Why not lower score?

- Scaling SAEs was a very important problem in interpretability, as indicated in the seminal SAE paper.
- Top-k SAEs are a significant improvement on an important research topic. This approach is well motivated and well placed in the literature.

### Why not higher score?

- The performance of top-k SAEs is state of the art, but not beyond comparison with alternatives.
- While top-k SAEs are a significant incremental improvement, top-k SAEs are not new, and this is a new application.

### Strengths
The paper's strengths are as follows: 

## Scale:

LLMs are being used in an increasing number of fields, and research into LLM interpretability is important for ensuring their fairness and safety, especially at scale.
This paper scales up SAEs to frontier LLMs, such as GPT4, which is a ***significant improvement*** over previous work, which was limited to smaller models. Furthermore, scaling laws are found, which could be very useful to practitioners and researchers trying to predict SAE performance ex-ante.

## Top-K:

The paper's usage of top-k SAE is one of the main contributions of this work, and it is ***original*** to the extent that top-k sparse autoencoders hadn't (to the best of my knowledge) been used on LLMs before. The ***quality*** of the results of the top-k function is such that it represent the state of the art when compared to other activation functions.

## Auxiliary Loss:

The authors tackle the ***significant*** issue of dead latents (up to 90% of the total when not mitigated) by introducing an auxiliary loss to the overall loss function. This incentivises the model to use all the latents, as it also supervises the next-aux latents. The ***quality*** of the results is high, as it reduces dead latents by an order of magnitude to 7%. This is to the best of my knowledge an ***original*** contribution.

## Evaluations:

The paper introduces many new evaluations. I believe that explainable loss and known latent probing are the most ***significant***.
Explainable loss is an ***original*** metric that considers the loss from just using the explanations that the SAE generates (discarding uninterpretable latents), and it represents a ***significant*** improvement over either MSE or L0 alone since it includes both reconstruction quality and an interpretability guarantee (L0 does not). Known latent probing is interesting in that it shows that the ***quality*** of probes of the latents is 25% better than that of residual stream probes.

## Clarity:

The paper is very ***clear*** across all sections, and its presentation is of high ***quality***

### Weaknesses
 The paper's weaknesses are as follows:

## Irreducible error:
The paper notes that adding an irreducible error term to the scaling laws improves the laws. However, the explanation of why such an error term would exist in LLM activations is not clear, and an experiment showing that gaussian noise is hard to fit for SAEs is provided instead. The experiment does explain why such an error would be there in the first place, and its outcome is not surprising. Mentioning "components with different amounts of structure" is vague. It is unclear if this irreducible error is due to inherent limitations of the SAE architecture, or if it is a property of the data itself. The paper should explore whether this error term is consistent across different layers of the model, or if it varies based on the complexity of the features being learned. Furthermore, the paper should investigate if the irreducible error is correlated with the dimensionality of the latent space, or if it is independent of the number of features.

## Top-K vs penalty shrinkage experiments:
It is expected that having larger activations for top-k SAEs won't improve the loss and that it will for sparsity penalty SAEs. This is because top-k SAEs do not have any constraint on the magnitude of the k activations they use. An experiment on shrinkage does not make the top-k activation function more attractive. The paper should include experiments that directly compare the reconstruction quality of top-k SAEs with sparsity penalty SAEs when both are trained with the same level of sparsity. This would provide a more direct comparison of the two approaches and help to determine if the top-k approach is truly superior, or if it simply achieves similar results with a different mechanism. Furthermore, the paper should explore the effect of varying the magnitude of the top-k activations on the reconstruction quality and interpretability of the learned features.

## Reproducibility:
An issue with the experiments in this paper is that GPT4 is a closed source model, which makes it hard to reproduce the results of some of the experiments. This is a significant limitation, as it prevents other researchers from verifying the results and building upon them. The paper should include more details about the training process, such as the specific hyperparameters used, the size of the training dataset, and the computational resources required. It would also be beneficial to include experiments on open-source models to demonstrate the generalizability of the findings.

## Probing datasets:
A set of 61 binary classification tasks is used to train probes on the latents. It is not clear why these specific tasks have been chosen. A larger and more diverse set of tasks would have been more significant. The paper should provide a detailed justification for the choice of these specific tasks, and explain how they relate to the features that the SAEs are expected to learn. Furthermore, the paper should explore the use of more diverse probing datasets, including tasks that involve more complex reasoning and natural language understanding.

## Unclear phrasing of top-k's contributions:
In line 132 there is a missing word after: "instead of", which I assume to be L1, but it's unclear.

### Questions
How much better is the aux loss than the top-k loss? 
This is interesting as it quantifies how much reconstruction quality we are 'paying' for sparsity.

At lines 132 and 452 do you believe 'an' should be 'a' (or is it not a typo)?

The following refers to work that is contemporaneous (4 months old or less), and it does not affect my rating.
Are you aware of:
- Jumprelu SAEs?
- Mixture of Experts SAEs? I believe you hinted at this in the paper.
- Sparse feature circuits? And the possibility to do evals on known circuits not just known latents (SAE seem not to be the best at factual recall).

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper (1) introduces Top-k sparse autoencoders (SAEs), which are novel for language models; (2) trains them on language models ranging in size up to GPT-4; (3) measures the SAE's sparsity/reconstruction tradeoff, finding performance that exceeds the state-of-the-art by a small margin; (4) demonstrate scaling laws for reconstruction accuracy in terms of training FLOPS and SAE width; and (5) measures the SAEs on a range of "downstream" metrics.

### Strengths
- This paper makes multiple novel contributions to research on the application of SAEs to language models:
	- The Top-k SAE architecture has not previously been used on language models. (Though they were introduced previously by (Makhzani & Frey, 2013).)
	- Scaling SAEs to a model the size of GPT-4 is a challenge due to the increasing concentration of dead features, and the early works in this field (Cunningham et al, 2023; Bricken et al, 2023) focused on relatively small language models. The scaling done in this paper is not entirely novel, as (Templeton et al, 2024) trained SAEs on the similarly-sized Claude 3 Sonnet, but this paper likely represents contemporaneous, parallel work.
	- Similarly, this paper finds scaling laws that are novel except for (Templeton et al, 2024).
	- This paper investigates several methods for evaluating SAEs beyond sparsity and reconstruction accuracy, which are important for establishing outside validity and utility. Especially appreciated is the metric in lines 311-314, contextualizing downstream loss in terms of a fraction of pre-training compute.

- In addition to the quantitative results, Top-k SAEs provide qualitative benefits over previous SAE architectures:
	- The sparsity level of Top-k SAEs is directly set, instead of relying on an indirect hyperparameter.
	- Top-k SAEs do not suffer from "feature shrinkage" caused by L1-regularization. The authors clearly demonstrate this in the excellent Figure 8.
	- Top-k SAEs have far fewer dead features at large scales.

### Weaknesses
 - While the authors describe many results, they are not all equally justified.
	- Section 4.2 (Recovering Known Features with 1D Probes) is conceptually very exciting, but somewhat confusing in its details.
		- The magnitude of the probe loss improvement seems very low, from ~0.52 in the worst case to ~0.49 in the best case. Figures 32 and 33 indicate that a similar magnitude of improvement across various run sizes and datasets. This section would therefore benefit from more baselining: what is the best such classifier based on a residual stream neuron? On a linear  probe trained on all the residual stream neurons? On similarly-sized noise?
		- The only such baseline in the paper is that in Figure 32 the caption says that the loss on residual stream channels is 0.600. But the figure shows the loss improving from 0.46 to 0.44 over training, so it seems like almost all of the gain of the SAE occurred in the first <1% of training. It is unclear if the reported 0.600 baseline is the initial loss of the residual stream probe or the final loss after training, and if the latter, how long it was trained for.
		- The probe losses appear to be averaged across the 61 datasets. This should be clearly stated in the body of the text, and it would be helpful to see the distribution of probe losses across the datasets, as this averaging could obscure significant variance.
	- Figure 7 is hard to understand, and would benefit from more explanations of its significance. The current caption does not provide enough context to understand the implications of the results. It's unclear what "N2G" refers to, and how it relates to the autoencoder's latent space. The caption mentions that the "N2G simulated latents performs better than a baseline of bigram language modeling", but the bigram baseline is not described in the main text, and it's not clear why this is a relevant comparison.

- There are several typos in the body of the text (see below)


### Questions
If it is permitted for authors to make revisions before the final submission, there are several small changes that could improve the quality of the paper:

- The paper would benefit from a thorough proofreading for typos. Examples include:
	- Line 129 reads: "It removes the need for the penalty. is an imperfect approximation of , and it introduces a bias of shrinking all positive activations toward zero (subsection 5.1)." 
	- In line 327, the expression "min E [y log σ(wzi +b)+(1−y)log(1−σ(wzi +b))]" must be negated to get entropy.
	- Line 367-368 is missing a word after "similar": "with the same n (resulting in better F1 scores) and similar (Figure 24)."
	- Line 384 "trie" should be "tree".

- In section 2.4, it would be good to describe the provenance of the technique "we initialize the encoder to the transpose of the decoder". This is described in (Conerly, 2024) (https://transformer-circuits.pub/2024/april-update/index.html#:~:text=in%20most%20cases).-,%F0%9D%91%8A,.,-The%20rows%20of), which the authors should cite as inspiration or an independent replication. The other technique in section 2.4, auxiliary loss, is properly cited to (Jermyn & Templeton, 2024) in Appendix A.2.

- (Uncertain) The paper's introduction links to "code and autoencoders for open-source models" and a "visualizer". In the reviewer copy, these links are broken, likely to keep the authors anonymous. The authors should confirm that these links work in the final submission version.

### Soundness
4

### Presentation
3

### Contribution
4
