# Structure Language Models for Protein Conformation Generation

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Proteins adopt multiple structural conformations to perform their diverse biological functions, and understanding these conformations is crucial for advancing drug discovery.
Traditional physics-based simulation methods often struggle with sampling equilibrium conformations and are computationally expensive.
Recently, deep generative models have shown promise in generating protein conformations as a more efficient alternative.
However, these methods predominantly rely on the diffusion process within a 3D geometric space, which typically centers around the vicinity of metastable states and is often inefficient in terms of runtime.
In this paper, we introduce Structure Language Modeling (SLM) as a novel framework for efficient protein conformation generation. 
Specifically, the protein structures are first encoded into a compact latent space using a discrete variational auto-encoder, followed by conditional language modeling that effectively captures sequence-specific conformation distributions. 
This enables a more efficient and interpretable exploration of diverse ensemble modes compared to existing methods.
Based on this general framework, we instantiate SLM with various popular LM architectures as well as proposing the
ESMDiff, a novel BERT-like structure language model fine-tuned from ESM3 with masked diffusion.
We verify our approach in various scenarios, including the equilibrium dynamics of BPTI, conformational change pairs, and intrinsically disordered proteins. SLM provides a highly efficient solution, offering a 20-100x speedup than existing methods in generating diverse conformations, shedding light on promising avenues for future research.

\iffalse
Proteins adopt multiple structural conformations to perform their diverse biological functions, and understanding these conformations is essential for drug discovery. Although traditional methods employ molecular dynamics simulations to explore potential conformations, these simulations are usually computationally expensive. Recently, generative methods for conformation sampling have been introduced to address this. Existing approaches heavily focus on diffusion models in the 3D geometric space, which may favor a single conformation mode due to their denoising nature, thus limiting the exploration for the broader area. We here propose a novel and simple framework by performing generative modeling in the discrete latent space of protein structures,  allowing for a more sufficient and interpretable exploration of diverse conformational states. Our method first encodes protein structures into a compact latent space using a discrete variational auto-encoder, followed by conditional generative modeling with language model (LM) that effectively capture target-specific conformation distributions. Besides popular choices of LM architectures, we novelly propose ESMDiff, as a fine-tuned variant of a BERT-like protein language model ESM3, to gain conditional generative capabilities under a masked diffusion framework. We verify our approach across various scenarios, including the equilibrium dynamics of BPTI, conformational change pairs, and intrinsically disordered proteins. The results demonstrate that our method provides a highly scalable and effective solution for generating diverse conformations, shedding light on promising avenues for future research.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors present a novel Structure Language Modeling (SLM) framework that integrates recent advances in discrete variational autoencoders (dVAEs) to quantise the latent space and language models to learn the conditional distribution on this latent space with masked diffusion models framework. This combined approach is applied to model the conformation space of proteins. The proposed framework offers flexibility in selecting the dVAE and language model components; however, the authors introduce a specific setup, named ESMDiff, which utilizes ESM3 and BERT as its primary components. To demonstrate the effectiveness of this approach, the authors evaluate ESMDiff on several case studies, including the structural dynamics of bovine pancreatic trypsin inhibitor (BPTI), modeling conformational changes in structural proteins, and exploring the conformation space of intrinsically disordered proteins (IDPs).

### Strengths
The paper is well-structured, with a clear and comprehensive presentation of the theoretical background and framework. Although flexible learnable priors in VAEs have a substantial history of research, the idea of coupling the dVAE and language models as flexible conditional prior is fresh and novel in the area of protein conformation modeling. The selected case studies are relevant and show the potential for wide practical application.

### Weaknesses
While the overall quality of the paper is high, there are a few weaknesses and areas that could benefit from further clarification.

* [major] While the experiments compare a diverse set of baseline models, they lack a comparison with pure language models. Previous work [a] demonstrated that language models can generate molecular and protein structures with atomic coordinates represented as regular text, and other research [b] has shown that this approach is viable for molecular conformation space modeling. Given the context sizes of modern language models, it seems feasible to model protein backbone coordinates directly as text. Including a comparison with pure language models could provide a strong justification for using dVAE in this framework. Specifically, the paper should address whether the dVAE provides a significant advantage over directly modeling the coordinate sequences with a language model, especially in terms of sample quality and computational efficiency. The current experiments do not sufficiently justify the added complexity of the dVAE component.
* [minor] In reference to lines 175–186, the training of the dVAE and the language model prior happens in two separate stages. Previous research on learnable priors in VAEs [c, d] showed that the encoder, decoder, and prior can be trained simultaneously. It would be helpful to clarify, either theoretically or through an ablation study, why this work uses a multi-stage training approach rather than a joint training method, as this separation introduces additional complexity to the training process. The paper should provide a more detailed explanation of the trade-offs between the proposed multi-stage approach and joint training, particularly focusing on potential benefits in terms of training stability or convergence speed.
* [minor] The scope of this work is limited to modeling the coordinates of the protein backbone (lines 145–150). However, accurate spatial positioning of side chains is essential for many practical applications, especially when modeling interactions between the protein and other proteins or molecular structures is required [e]. Including a discussion of this limitation in the Limitations section would strengthen the paper by addressing the potential impact of excluding side chains on the model’s practical applications. The paper should explicitly discuss how the exclusion of side chains might affect the model's ability to accurately predict protein-protein or protein-ligand interactions, and suggest potential avenues for future work to address this limitation.

### Questions
* [major] While the experiments compare a diverse set of baseline models, they lack a comparison with pure language models. Previous work [a] demonstrated that language models can generate molecular and protein structures with atomic coordinates represented as regular text, and other research [b] has shown that this approach is viable for molecular conformation space modeling. Given the context sizes of modern language models, it seems feasible to model protein backbone coordinates directly as text. Including a comparison with pure language models could provide a strong justification for using dVAE in this framework.
* [minor] In reference to lines 175–186, the training of the dVAE and the language model prior happens in two separate stages. Previous research on learnable priors in VAEs [c, d] showed that the encoder, decoder, and prior can be trained simultaneously. It would be helpful to clarify, either theoretically or through an ablation study, why this work uses a multi-stage training approach rather than a joint training method, as this separation introduces additional complexity to the training process.
* [minor] The scope of this work is limited to modeling the coordinates of the protein backbone (lines 145–150). However, accurate spatial positioning of side chains is essential for many practical applications, especially when modeling interactions between the protein and other proteins or molecular structures is required [e]. Including a discussion of this limitation in the Limitations section would strengthen the paper by addressing the potential impact of excluding side chains on the model’s practical applications.

a. Language models can generate molecules, materials, and protein binding sites directly in three dimensions as XYZ, CIF, and PDB files, 2023

b. BindGPT: A Scalable Framework for 3D Molecular Design via Language Modeling and Reinforcement Learning, 2024

c. VAE with a VampPrior, 2017

d. A Prior of a Googol Gaussians: a Tensor Ring Induced Prior for Generative Models, 2019

e. Rotamer Density Estimator is an Unsupervised Learner of the Effect of Mutations on Protein-Protein Interaction, 2023

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to use protein language models, operating on structure tokens, to model protein conformation ensembles. Several variations on this idea are tried: (1) an encoder-decoder model that translates sequence-tokens to structure-tokens (2) a decoder only model supplied with sequence-token prompts (3) Gibbs sampling with the bidirectional unmasking model ESM3 (4) Gibbs sampling and ancestral sampling with ESMDiff, a version of ESM3 fine-tuned under masked diffusion. These models are evaluated on the BPTI benchmark and conformation pair datasets and compared against several existing methods.

### Strengths
* The problem addressed by the authors is important and timely. 
* The approach, although based on accessible and popular ideas, has not been explored in the literature and is likely to be of great interest to the community.
* The paper is thorough and has detailed appendices describing training, inference, and evaluation.
* The paper has a diversity of experimental results, including several that appear only in the appendices (?)

### Weaknesses
 **Novelty**
* The paper's approach is relatively straightforward and is almost an off-the-shelf application of ESM3 or any structural-token protein language model. With that said, I don't think this is a big drawback because the focus of the paper is on the novelty of application and empirical benchmarks.

**Quality**
The paper's evaluations are, however, relatively limited and could be improved in quality and rigor.
* The evaluations lean heavily on the BPTI benchmark, and do not make use of MD datasets like ATLAS and MD-CATH. It would be much more interesting to see how well the model can learn from those datasets and generalize to a larger number of new proteins. The lack of these datasets limits the assessment of the model's ability to capture realistic conformational changes, as BPTI is a relatively small and well-studied protein with limited conformational diversity compared to the broader range of proteins found in MD simulations.
* ESM3, out-of-the-box, can already be used as a sequence->structure generative model with iterative decoding. However, the authors seem to only evaluate ESM3 under Gibbs sampling. Thus a proper comparison with pretrained ESM3 is missing. Specifically, the authors should compare their fine-tuned models against the iterative decoding capabilities of the base ESM3 model to establish the true benefit of their approach, instead of only using Gibbs sampling which may not be the optimal way to use the base model.
* The results themselves are also relatively mixed, with zero-shot ESM3 outperforming ESMDiff in several instances. This raises questions about the effectiveness of the fine-tuning procedure and whether the added complexity of the diffusion model is truly beneficial, especially given the computational cost.

**Clarity**
* In all tables, the authors have bolded the best method _among the several methods they propose_, not the best method overall. This gives a very misleading impression and is a major issue that must be fixed. This makes it difficult to assess the true performance of the proposed methods compared to existing baselines.
* At times, the paper has a forced and unnecessary level of formalism. At best, this obscures what the model is actually doing, and at worst leads to misleading or incorrect statements.
    * The authors spend quite a bit of time building up a probabilistic framework for structure based on a standard variational lower bound. However, the authors universally use the ESM3 tokenizer, which is not trained with maximum-likelihood reconstruction. Indeed, "we begin by maximizing the ELBO $\mathcal{L}(\phi, \theta)$ with respect to the encoder $\psi$ and decoder $\phi$" as this is soon undercut by "We start with the pre-trained dVAE established in Hayes et al. (2024) as the structure tokenizer (frozen)." So are $psi$, $\phi$, ever trained, or not? Furthermore, the ESM3 decoder is not conditioned on sequence tokens, unlike the formally defined decoder $p_\phi(x \mid c, z)$. This discrepancy between the theoretical framework and the actual implementation needs to be addressed.
    * The exposition on general discrete diffusion takes up quite a lot of space, but ultimately the authors use masked diffusion, which could be presented much more clearly and succinctly on its own. The lengthy discussion of general discrete diffusion adds unnecessary complexity and obscures the specific method used.
    * Since ESM3 is also trained at all mask levels, it is not immediately clear what is different about the fine-tuning model. As I can currently tell, it is only that the model is explicitly time-conditioned and the unmasking is stochastic instead of a fixed number of tokens unmasked per step. But is this really a significant enough difference to merit a completely different presentation?

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces the Structure Language Modeling (SLM) framework for protein conformation generation. The frameworks consist of an auto-encoder and a conditional language model, which can be BERT-like or GPT-like. This method gets a good speedup than previous methods.

### Strengths
-  The paper is well motivated.
-  The framework is a meaningful combination of VAE and LM that take the benefits of both.
-  The 20x-100x speed up seems to be promising.

### Weaknesses
In results tables, seems all systems (including baselines and SLMs) have different model sizes and pre-training data. It would be better if these details are clearly described in the table to better understand the significance of SLM.


### Questions
In Table 2, the best SLM variant in each cluster is all different. Can authors provide more insights about these results?

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
2

### Summary
This paper aims to generate protein conformation ensembles with Structure Language Modeling (SLM), a method that first tokenizes protein 3D structure through learned autoencoding with a VQVAE, and then generates the 3D structure through language modeling and decoding. Compared to alternative methods such as equivariant diffusion models, the proposed method enjoys a significant efficiency advantage. The proposed method is applied to protein conformation ensemble generation tasks with a diverse set of evaluation metrics.

### Strengths
- The proposed method offers an interesting alternative to the task of protein conformation sampling, a task that has so far mostly been tackled with 3D-aware generative models that may suffer from poor computational efficiency. The proposed method naturally leverages pre trained ESM3 model and extends its capablities.

- The experiments validate the efficiency of the proposed method. The performance seems competitive with SOTA structure-based generative models.

### Weaknesses
 - There are many metrics being benchmarked and it is hard to evaluate the model performance. It seems that the proposed method is quite competitive with SOTA alternatives. However, this reviewer is not fully convinced about that because the results are so scattered around in different tasks and different evaluation metrics, and the proposed method sometimes works better and sometimes works worse compared to baseline methods. Can the authors explain what metrics are the most practically relevant, or propose consolidated metrics for comparing different models? Can the authors include benchmarks that were originally used in the AlphaFlow/ESMFLow paper (Jing et al, 2024), if they are solving the same task?

### Questions
Please see "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
2
