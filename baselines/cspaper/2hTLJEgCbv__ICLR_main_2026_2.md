---
job_id: 2a7015d9-8cb5-4a22-89ba-84f936845104
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 2hTLJEgCbv.pdf
paper: When Encoders Should Stay Simple: An Empirical Analysis of Architectures for Variational Autoencoders
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies variational autoencoders, generative modeling, and representation learning.

## Minimum Quality
Pass ✅. The paper contains an abstract, introduction, background/related work, method, experimental results, and conclusion; although the contribution is weak and the empirical scope is limited, it does not fall below desk-reject threshold for incompleteness or obvious fatal procedural flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I do not detect hidden prompts, manipulative instructions, or suspicious text targeting automated review systems in the provided manuscript content.

# Expected Review Outcome:
## Summary
This paper presents an empirical study of how encoder and decoder architecture choices affect VAE behavior. The authors vary dense versus convolutional encoders/decoders, layer counts, and latent dimensionality on MNIST, then analyze reconstruction loss, KL-related behavior, and PCA projections of latent representations. The main claimed takeaway is that simple, shallow dense encoders tend to work better, while decoders benefit more from convolutional structure and greater depth.

## Strengths
The paper asks a reasonable question. Architectural asymmetry between encoder and decoder is often discussed informally in the VAE literature, but comparatively few papers isolate it in a deliberately simplified setup. Even if the scope is narrow, the question itself is relevant to practitioners who still use VAEs as representation learners.

I appreciate that the study tries to hold the probabilistic machinery fixed and vary only architecture. That design choice makes the intended message easy to understand: the authors are not proposing yet another VAE objective, prior, or regularizer, but trying to understand what the network families themselves are doing.

The main qualitative takeaway is at least consistent across several figures. In **Figure 4** on Pages 6-7, the center and right histograms support the claim that shallow dense encoders appear more frequently among the top-performing models, while convolutional decoders, especially deeper ones, appear more often on the decoding side. This figure is one of the clearer pieces of evidence in the paper because it directly aggregates the architecture frequencies in the selected best-performing subset.

The manuscript also makes an effort to connect reconstruction behavior and latent collapse rather than reporting only one scalar metric. In particular, **Figure 2** on Page 5 overlays reconstruction and generative/KL-related trends across many model configurations, and **Figure 3** on Page 6 focuses on the top 25% models. These visual summaries do help the reader see that the authors are not simply ranking models by one loss alone.

The latent-space visualizations, while limited, do provide some intuitive evidence that more aggressive compression harms separability. For example, the progression shown in **Figure 6** suggests that the lower-compression settings produce cleaner class structure under PCA than the more compressed settings.

## Weaknesses
1. **The empirical scope is far too narrow to support the general claims in the title and conclusion.**  
   The title, "When Encoders Should Stay Simple," reads like a broad architectural claim about VAEs, but all experiments are on **MNIST only** (Page 3, Section 3). MNIST is an extremely forgiving dataset with low variability and strong local spatial structure. Architectural conclusions drawn from MNIST often do not transfer to CIFAR-like images, CelebA, Omniglot, Fashion-MNIST, SVHN, or higher-resolution data. This matters because encoder/decoder asymmetry in VAEs is strongly data-dependent; on more complex data, encoder capacity can materially affect posterior quality, optimization stability, and mutual information. As written, the paper supports, at best, a narrow claim about simple VAEs on MNIST, not a general principle about when encoders should remain simple.

2. **The evaluation metrics are insufficient and in some places conceptually muddled.**  
   The paper repeatedly refers to "generative inference loss" and interprets near-zero KL as latent-space collapse, but the setup is not formalized carefully enough. On Pages 4-5, **Figure 1** and **Figure 2** appear to plot a KL-related term, but the exact quantity, sign convention, aggregation across the dataset, and normalization are not defined clearly. In Equation (1) on Page 2, the ELBO is written with a negative KL term plus an expectation of negative log-likelihood, which is already mixing optimization directions in a somewhat confusing way. If the authors optimize a loss, one would usually define something like
   \[
   \mathcal{J}(x)=\mathbb{E}_{q_\phi(z\mid x)}[-\log p_\theta(x\mid z)] + \mathbb{D}_{\mathrm{KL}}(q_\phi(z\mid x)\|p(z)),
   \]
   or define the ELBO and then explicitly state whether larger or smaller is better. Here, the terminology and plots make it difficult to know whether "better generative inference loss" means higher ELBO, lower KL, or simply nonzero KL. This matters because several conclusions, including the headline statement that "non-zero KLD loss was found to be generally beneficial" (Page 5), depend on a precise interpretation of this quantity.

3. **The core claims are not supported by standard generative-model evaluation.**  
   For a paper about VAE architecture and "generative quality," the evidence is unusually thin. There are no likelihood estimates, no bits/dim, no held-out negative ELBO decomposition beyond the vague plotted losses, and no sample-quality metrics such as FID, KID, or precision/recall for generative models. There is also no actual gallery of generated samples, only latent projections and aggregate plots. This is a major omission because the paper concludes that certain decoder types are preferable for generation, but it never measures generation quality in a standard way. Reconstruction and a KL-related term are not enough to substantiate claims about generative performance.

4. **The selection and summarization strategy around the “top 25%” and “top 50%” models is ad hoc and weakens the analysis.**  
   Much of the paper’s architectural interpretation is based on subsets such as the "top 25%" and "top 50%" of models, for example in **Figure 3**, **Figure 4**, **Figure 6**, and **Figure 7**. However, the paper never gives a rigorous criterion for what exactly defines "top." Is it lowest reconstruction loss, joint ranking over two metrics, or visual inspection? On Page 4, the text says "Visual evaluation revealed that the top 25% of models have minimal reconstruction collapse," which suggests a partially subjective selection process. This is problematic because the architectural conclusions in **Figure 4** and **Figure 5** then become highly sensitive to that unformalized filtering rule. A more scientific analysis would define a clear ranking functional, report all models in a table, and ideally test whether the observed architecture preferences remain under alternate ranking criteria.

5. **There are no proper baselines beyond the authors’ own architecture grid, and no statistical treatment of variance.**  
   The paper compares many internal configurations but does not benchmark against any established VAE architecture from the literature, not even a standard conv VAE or MLP VAE with conventional capacity. There are also no repeated runs, no standard deviations, and no confidence intervals. Given the known instability of VAE training and posterior collapse behavior, single-run conclusions about architecture preference are not very trustworthy. This matters particularly for **Figure 1** and **Figure 2**, where many models are visually close. Without repeated seeds, some of the apparent ordering may simply reflect run-to-run noise rather than a robust architectural effect.

6. **The latent-space analysis is too weak to support claims about representation quality or separability.**  
   The paper uses PCA scatter plots in **Figure 6** and **Figure 7** as evidence that some latent spaces are more meaningful or separable. But PCA of latent means is, at best, a very rough visualization. It does not quantify class separation, disentanglement, mutual information, linear probe performance, clustering quality, or downstream utility. Moreover, the text on Page 3 says PCA "helps avoid overfitting the representation," which is not a standard or well-justified claim in this context. PCA is simply a projection for visualization; it does not validate the representation. If the paper wants to argue that architecture affects latent structure, it should include quantitative latent evaluations, for example linear classification on frozen latents, clustering metrics, or mutual information proxies.

7. **The manuscript overstates novelty and practical insight relative to what is actually shown.**  
   The main conclusions, namely that overly compressed latents can hurt representation quality, that collapsed latents are undesirable, and that decoder architecture matters a lot in VAEs, are already broadly consistent with existing intuition in the VAE literature. The paper does not really move from intuition to strong evidence because the setting is so small and the metrics so limited. I do not object to incremental empirical papers per se, but for ICLR the bar is higher than confirming expected behavior on MNIST.

8. **The mathematical exposition needs tightening, and Equation (1) is presented in a confusing form.**  
   On Page 2, Equation (1) is written as
   \[
   \mathcal{L}(\theta,\phi;x^{(i)})=-\mathbb{D}_{\text{KL}}(q_\phi(z|x^{(i)})\|p_\theta(z))
   + \mathbb{E}_{q_\phi(z|x^{(i)})}[-\log p_\theta(x^{(i)}|z)].
   \]
   This is neither the usual ELBO notation nor a clearly defined minimization objective. The standard ELBO would be
   \[
   \mathrm{ELBO}(x)=\mathbb{E}_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)]-\mathbb{D}_{\mathrm{KL}}(q_\phi(z\mid x)\|p(z)),
   \]
   while the usual loss to minimize is the negative ELBO,
   \[
   -\mathrm{ELBO}(x)=\mathbb{E}_{q_\phi(z\mid x)}[-\log p_\theta(x\mid z)] + \mathbb{D}_{\mathrm{KL}}(q_\phi(z\mid x)\|p(z)).
   \]
   The paper mixes the two forms, then later reasons about "non-zero KLD loss" as if the sign convention were obvious. This is not a cosmetic issue, because the interpretation of the plots depends on it. Also, the prior is denoted \(p_{\theta^*}(z)\) in Section 2.1 but later \(p_\theta(z)\), which is inconsistent notation for a standard fixed prior.

9. **Crucial experimental details are missing, making the study hard to interpret and reproduce.**  
   The paper does not clearly specify training hyperparameters, optimizer, learning rate, batch size, epoch count, early stopping criterion, train/validation/test splits, decoder likelihood choice for MNIST, whether Bernoulli or Gaussian observation model is used, whether the KL term is annealed, and whether reported losses are train or test values. These are not minor omissions in a VAE paper. For instance, posterior collapse and reconstruction/KL tradeoffs can change substantially under KL warmup, optimizer settings, and decoder likelihood choices. Without these details, it is hard to know whether the observed effects are architectural or training-protocol artifacts.

10. **The paper lacks proper quantitative tables, which makes the experimental section much less informative than it should be.**  
    There is no results table summarizing the architecture grid, latent dimensions, reconstruction term, KL term, total objective, and ranking. Instead, the reader gets dense scatter/bar figures with many labels. This is a serious presentation and scientific issue, not just style. A compact table would let readers inspect whether the gaps are large or tiny, whether some configurations dominate consistently, and how many settings actually collapse. The absence of a table is especially noticeable because **Figure 1** and **Figure 2** contain many model labels but do not allow precise numerical comparison. For an empirical architecture paper, not having even one main results table is a major weakness.

11. **Some figure-driven claims are more assertive than the figures warrant.**  
    For example, the paper says on Page 5 that "powerful CNNs did not negatively impact encoding performance," but **Figure 4** and **Figure 5** do not convincingly establish that stronger encoders are harmless; they only show counts among a selected subset. Similarly, **Figure 5** reports counts of top-performing encoders/decoders by architecture type, but count histograms are not normalized by how many total models of each type were trained. If some architecture families have more configurations in the search space, raw counts can be misleading. A normalized win-rate or average rank per family would be much more defensible.

12. **The related-work positioning is thin relative to the paper’s stated ambition.**  
    The related work on Pages 2-3 mentions broad VAE references and NVAE, but does not adequately position this paper against empirical studies of architecture choice, encoder-decoder mismatch, posterior collapse diagnostics, or representation quality evaluation. The result is that the manuscript reads a bit like rediscovering familiar lessons without carefully stating what is already known and what exactly is newly established here.

## Questions
1. Please define precisely what is plotted as the "generative inference loss" in **Figure 1**, **Figure 2**, and **Figure 3**. Is it the KL term, the negative KL term, the ELBO contribution, or something else? Also specify the sign convention, averaging scheme, and whether values are computed on train, validation, or test data. A clear answer here would substantially improve my confidence in the interpretation of the results.

2. How exactly are the "top 25%" and "top 50%" model subsets selected? Please provide a deterministic criterion, ideally a formula. If the subset depends partly on visual inspection, I would view the current conclusions as much weaker.

3. Can the authors provide a full quantitative results table for all trained configurations, including latent size, encoder/decoder type and depth, reconstruction loss, KL term, total objective, and whether the model collapsed? This would make the empirical evidence much easier to assess.

4. Were the experiments repeated across multiple random seeds? If yes, please report mean and variance. If not, can the authors comment on how stable the architecture rankings are under reruns?

5. What decoder likelihood was used for MNIST, Bernoulli or Gaussian, and were any standard training tricks such as KL annealing, free bits, or beta weighting used? These details are necessary because they strongly affect posterior collapse and the reconstruction-KL tradeoff.

6. To support the broader architectural claim, can the authors provide evidence on at least one dataset beyond MNIST? Even Fashion-MNIST or CIFAR-10 would make the paper substantially more convincing.

7. Can the authors add standard generative-model evaluation, such as held-out NLL/ELBO, bits/dim, or sample-quality metrics, plus actual generated-sample visualizations? This would help separate "reconstructs digits adequately" from "is a better generative model."

8. In **Figure 5**, are the counts normalized by the number of tried configurations per architecture family? If not, the current count-based interpretation may be biased by the search-space composition.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns arise from the paper as presented. The experiments use MNIST and methodological analysis of VAE architectures, with no obvious issues involving sensitive data, harmful deployment, or human subjects.

## Soundness Rating
2: fair. The paper does run a systematic grid of VAE architectures and presents qualitative evidence, but the technical claims are only weakly supported because the evaluation is narrow, key metrics are underspecified, and the analysis relies heavily on subjective or ad hoc summaries.

## Presentation Rating
2: fair. The central idea is understandable, and the figures do communicate some trends, but the manuscript has important clarity problems in notation, objective definition, experimental detail, and result organization. The lack of a quantitative results table is a major presentation issue.

## Contribution Rating
1: poor. The paper studies a relevant question, but the contribution is limited by the narrow MNIST-only scope, weak quantitative evaluation, and conclusions that remain close to pre-existing intuition rather than establishing a robust new insight for the ICLR community.

## Overall Rating
2: Reject, not good enough. The paper is readable and asks a sensible question, but in its current form it does not meet ICLR standards for empirical depth, quantitative rigor, or breadth of evidence. The main message may be directionally reasonable, yet the study is too limited and under-specified to support the broad architectural claims being made.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper’s core experimental setup is straightforward to evaluate, and the main weaknesses are clear from the manuscript itself.