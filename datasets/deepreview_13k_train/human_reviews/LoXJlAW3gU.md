# Diffusion on language model encodings for protein sequence generation

- Decision: Reject
- Scores: 5, 6, 6, 5, 6, 3

## Abstract
Protein design necessitates a profound understanding of the intricate nature of the protein universe. While many efforts focus on conditional generation or specific protein families, the foundational task of unconditional generation remains underexplored and underappreciated.  Existing models still struggle to achieve both high quality and diversity in generated protein sequences. To address this gap, this research introduces DiMA, a novel model that leverages latent diffusion on representations derived from the protein language model, ESM-2, to generate amino acid sequences. We quantitatively investigate the impact of components of the latent diffusion model, revealing their contributions to superior protein generation performance. Extensive evaluations using multiple metrics across two protein modalities showcase DiMA's superior quality, diversity, and distribution matching capabilities compared to leading autoregressive transformer-based and discrete diffusion models, while utilizing ten times fewer parameters. Our approach consistently produces novel, diverse protein sequences that accurately reflect the inherent structural and functional diversity of the protein space. Furthermore, we demonstrate the conditional generation capabilities of our method. Our work advances the field of protein design by providing a robust framework for scalable and high-quality protein sequence generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents an approach for unconditional protein sequence generation that operates via continuous diffusion in the latent space of protein sequence embeddings derived from the encoding model ESM2. Generated latent vectors are decoded back to amino acid sequence space via a lightweight decoder. By leveraging a pre-trained encoder like ESM2, the size of the backbone network driving the latent space diffusion process is relatively small. The authors present a series of evaluations that attempt to quantify the distribution modeling capabilities of their approach and the quality of sampled generations, including relative to internal ablations and other approaches trained on the SwissProt dataset (evaluations on AFDB are not presented relative to other approaches).

Post rebuttal: The authors' rebuttal addresses my primary concerns, and the promised revision promises to correct the significant instances of imprecision in the manuscript. I will adjust my scores accordingly.

### Strengths
While many works have presented compelling approaches for unconditional protein sequence generation, including sequence-based generative models (ProGen, ProtGPT, EvoDiff, etc), and latent diffusion models (eg ProLDM), to my knowledge this is a work that leverages the pre-trained ESM to define a latent space over which to learn the diffusion process. This is a valuable idea to contribute to the field, but it must hold in terms of evaluations. It is also interesting to provide a head-to-head comparison of discrete diffusion over amino acid sequences versus continuous diffusion over the latent sequence embeddings provided by ESM.

### Weaknesses
There are several weaknesses to this work:
- The claim that “the foundational task of unconditional generation remains underexplored and underappreciated” is simply incorrect — many works (e.g., ProGen, ProtGPT, EvoDiff) have explored and evaluated performance of sequence-based unconditional generation.
- Discussion of related works on latent diffusion for proteins, such as Pro-LDM and CHEAP, is missing from the Introduction and Related Works. In general, many related works on diffusion models for protein generation are not discussed.
- The claim that “The straightforward adaptation of image-based diffusion models has not yet yielded satisfactory results in this domain,” is also unfounded. In fact, diffusion-based models for protein generation have been proven state-of-the-art in structure space; in sequence space, discrete diffusion is not at all a straightforward adaptation of image-based diffusion. This is not directly applying existing image-based diffusion, as the authors imply. This imprecision signals an underlying weakness of the work and the authors’ claims.
- The claim “most comprehensive set of metrics” is a gross overclaim and significantly weakens the credibility of the paper.
- All the distributional metrics presented seem to be computed relative to the train set — this calls into question the strength and credibility of the evaluations, since such comparisons to train will only reflect the ability of the generative models to memorize the train set. Such distributional evaluations should be computed relative to an independent test set.
- The presence of repeated amino acid subsequences is not a metric of “diversity”; similarly, the 95% sequence identity threshold as the barrier to novelty is extremely lenient. The use of a 95% sequence identity threshold for novelty detection is not rigorous, as it would still allow for significant overlap between generated and training sequences. A more stringent threshold, such as 70% or even 50% sequence identity, would be more appropriate to assess true novelty.
- The claims that DiMA performs as well or better than the benchmarked approaches is not upheld by the evaluations, where DiMA is often outperformed. The reported results often show DiMA underperforming compared to baselines across multiple metrics, suggesting that the model's performance is not as strong as claimed.
- The training and comparisons using SwissProt are not compelling, given the small (~200-300K sequences) size of SwissProt, making it easy to memorize, especially considering the use of the training set in the distributional metrics.

### Questions
1. Why were the distributional metrics computed relative to the train set? How do the authors justify the use of these metrics as an appropriate means to benchmark the learning capacity and generalizability of the tested models?
2. What was the sequence-level diversity/novelty achieved, relative to natural sequences? The repeated subsequence metric does not reflect this, and the 95% identity threshold is extremely lenient.
3. What was the reasoning behind the use of the SwissProt dataset when it is relatively so small, almost certainly represented within the ESM pretraining set, and given its size very easy to memorize?
4. What are the relative strengths, limitations, and novelties of DiMA versus another latent diffusion approach, Pro-LDM? These are not discussed. 
5. The evaluations of “biological relevance” do not demonstrate evidence of real-world utility of the approach. It is not surprising that high homology is achieved given training on SwissProt. Could the authors comment on the ability of DiMA to generate new sequences relevant to an independent downstream evaluation or task?

### Soundness
3

### Presentation
2

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
This work introduces DiMA, a protein sequence generation model by performing latent diffusion on ESM2-650M embeddings. The model is evaluated by sequence diversity, BLAST identity to known sequences, perplexity under autoregressive models, and distribution matching to embeddings of protein families. Structure sensibility is also assessed by examining the pLDDT and self-consistency perplexity. Some emphasis is also given to methodological design, including ablating the noise schedule used, self-conditioning, ESM2 encoding, time embedding information insertion into the model. When compared to several baselines that include autoregressive, energy-based, and diffusion-based sequence generation methods, trained to have the same parameter count and trained on the same datasets,

### Strengths
* Ablation results are thorough and provide insight for others venturing into generating proteins via their latent embeddings.
* Results are comprehensive. Retraining baselines on the same dataset & controlling for parameter size is a good and rigorous effort.
* On the whole, sequence generation results are quite strong against baselines.
* Focusing on distribution similarity is IMO a great standard for this community, and it's nice to see that many of these metrics perform well.

### Weaknesses
 * The encoder compression sections feels underdeveloped. At minimum, it should probably include a citation to CHEAP (https://www.biorxiv.org/content/10.1101/2024.08.06.606920v1.full.pdf). A stretch experiment would be to see how sequence diffusion performance changes when doing so in the CHEAP embedding space. ESM 3B yields better results in Table 3, but we know that larger embedding dimensions is generally harder for latent diffusion models, so all of this feels a bit counter intuitive. I think at this point it's not too much of a mystery that we can do sequence generation by diffusion on ESM embeddings, and ample literature exists on diffusion design choices, but the finer details of how information is captured in these latent embeddings is more under-explored, and including it in this paper would strengthen its utility.
* "Most comprehensive evaluation" in the introduction is a strong claim. The evaluations are indeed very impressive, but adding a qualifier like this is rather misleading, and does not promote the paper's longevity.
* I think the work has a lot of results, which is great, but they feel a bit under-analyzed. Reducing comparisons to single valued points without any examples of generated sequences (or their folded structures) feels short of convincing.  In future iterations, the work could be strengthened by more biological and qualitative analyses like those on pages 24-28, and moving that into the main text. In its current form, the captions are vague; for e.g. Figure 11, 12, 13 especially.
* I think it's productive to have figures like Appendix B.2 which demonstrate distribution comparisons in the main text. Though table space is limited, it would be nice to report the stds from the mean if possible. 
* In the main baseline tables, is it possible to also add the length distributions of baselines and generated sequences, given how important they are for many of the reported metrics?

Minor:
* Line 127: "High-generalizing" reads slightly awkwardly
* This is not critical for me to raise my score, but could I think the results section would be better organized with better subsections, such that a study is presented right before the results. Found it a bit hard to jump between the sections and find the correct \paragraph{} heading. 
* fontsize inconsistencies in tables could be polished
* noise schedule formula is duplicated between main text and Appendix D.1

### Questions
* In the data section, could authors clarify how they'd used the AFDB dataset, since it is a structural dataset? Why not just train on UniRef or another similarly sized whole-protein dataset?

Minor:
* line 237: description of "ProteinMPNN structure representations" is a bit murky. Which layer was used? Which ProteinMPNN structure? Where did the structure come from given that the generation is for sequences?

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
In this manuscript, the authors introduce a latent diffusion method that leverages representations derived from the protein language model, ESM-2, to design proteins by generating amino acid sequences. Extensive ablation studies and evaluations based on diverse matrics were performed by the authors showing the method's capacity in generating protein sequences. This study shows the latent diffusion based method shows practical benefits for protein sequence design in terms of computational efficiency and sequence diversity.

### Strengths
The authors present comprehensive ablation studies and evaluations using multiple metrics to demonstrate their method's effectiveness in generating protein sequences. Their results show the method's ability to generate diverse sequences while maintaining structural fidelity to the protein space. The inclusion of distributional similarity metrics is interesting. This evaluation framework offers valuable insights for the protein sequence design community and establishes useful benchmarking standards.

### Weaknesses
The manuscript does not sufficiently justify why latent diffusion-based sequence design methods would provide advantages over alternative approaches, particularly discrete diffusion methods, in the context of protein sequence design. The authors may provide more theoretical or practical benefits of their latent diffusion approach. To strengthen the work, the author should provide additional evaluation metrics including sequence novelty, and provide more discussion about the underlying relationships between the metrics they used, clarify how they complement or potentially contradict each other.

Several critical points require attention in the manuscript:

[Technical Motivation and Advantages]

While the manuscript identifies protein sequence design as an important problem, it lacks sufficient justification for using latent diffusion over established methods like discrete diffusion. The technical advantages and unique capabilities of latent diffusion in this specific context should be pointed out.


[Evaluation Metrics]
1. A novelty assessment comparing generated sequences with native sequences (e.g., sequence identity analysis) should be provided. One major concern is that the high-performance metrics could result from training set memorization rather than genuine generative capabilities. It is suggested to calculate sequence identity between generated sequences and their nearest neighbors in the training set. 
2. The choice of Progen perplexity (PPL) as a quality metric requires justification. The authors should provide more discussion to clarify whether PPL is reliable for protein sequence design (ref: https://arxiv.org/abs/2210.05892). 
3. Sequence length: The evaluation is limited to a narrow sequence length window (128-254 amino acids). This restriction raises important questions about method generalizability: How does performance scale with longer sequences? Could discrete diffusion methods demonstrate superior quality and diversity for longer sequences?

[Model Scaling Effects]

The observed decrease in distribution fitness scores (FD-seq, MMD-seq) when using the ESM3b encoder appears to contradict previous findings about model scaling benefits. This unexpected result warrants deeper analysis and discussion.

### Questions
Several critical points require attention in the manuscript:

[Technical Motivation and Advantages]

While the manuscript identifies protein sequence design as an important problem, it lacks sufficient justification for using latent diffusion over established methods like discrete diffusion. The technical advantages and unique capabilities of latent diffusion in this specific context should be pointed out. 


[Evaluation Metrics]
1. A novelty assessment comparing generated sequences with native sequences (e.g., sequence identity analysis) should be provided. One major concern is that the high-performance metrics could result from training set memorization rather than genuine generative capabilities. It is suggested to calculate sequence identity between generated sequences and their nearest neighbors in the training set. 
2. The choice of Progen perplexity (PPL) as a quality metric requires justification. The authors should provide more discussion to clarify whether PPL is reliable for protein sequence design (ref: https://arxiv.org/abs/2210.05892). 
3. Sequence length: The evaluation is limited to a narrow sequence length window (128-254 amino acids). This restriction raises important questions about method generalizability: How does performance scale with longer sequences? Could discrete diffusion methods demonstrate superior quality and diversity for longer sequences?

[Model Scaling Effects]

The observed decrease in distribution fitness scores (FD-seq, MMD-seq) when using the ESM3b encoder appears to contradict previous findings about model scaling benefits. This unexpected result warrants deeper analysis and discussion.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents DiMA, a model leveraging latent diffusion on protein language model encodings (in specific, ESM2) for generating protein sequences. The authors claim that DiMA achieves superior quality, diversity, and distribution matching compared to existing autoregressive and discrete diffusion protein sequence language models while using fewer parameters.

### Strengths
- The paper claims extensive evaluations using multiple metrics, which basically supports the findings.
- The idea of doing diffusion or flow matching in the latent space makes sense and is a good direction to explore. 
- DiMA’s efficiency in utilizing ten times fewer parameters than leading models is a significant advantage, suggesting potential for broader applications in protein design.

### Weaknesses
 - Firstly, the approach presented in this paper does not significantly advance the field of **generative models**(the primary area selected). While the application of latent diffusion is noted, it does not bring substantial new insights or methodologies to the existing body of research on generative models (even in the field of protein design). I agree on the experimental contribution of this paper and think the protein design problem is important and relevant. However, it is under-qualified as a top-conference paper given its presentation and methodology contribution.
- Inconsistent results presentation. In Tables 4 and 5 of the main text, the bold digits intended to denote the best results (I guess) are inconsistently labeled. This lack of clarity can lead to confusion about which results are truly the best and detracts from the paper’s credibility.
- The use of Swissprot and AFDB as sequence-based protein databases is not adequately justified. The authors should provide a clearer rationale for selecting these databases and explain how they enhance the effectiveness of the sequence generation process. Why not use Uniprot or Uniref on which ESM2 is pre-trained?
- The authors assert that they use “the most comprehensive set of metrics” to evaluate their model. However, this claim lacks substantiation within the paper, raising questions about the thoroughness of their evaluation process.
- The sections/paragraphs are badly organized and hard to follow, please consider improve the manuscript during rebuttal.

### Questions
- Can you clarify how DiMA’s approach contributes uniquely to the generative model area compared to existing methodologies?
- What specific rationale guided your choice of Swissprot and AFDB for protein sequence generation, and how do these structure-based databases specifically benefit your model? If this is the common practice in previous work, do the authors think incorporating sequence-based database like UniProt/UniRef will enhance the performance of DiMA? For example, in one of the baselines, EvoDiff, the authors there use evolutionary-scale sequence data to train their model.
- Could you provide a more detailed breakdown of the metrics used in your evaluations and other studies (eg., baselines) to support your claim of comprehensiveness of evaluation? For example, you can make a table to justify and list the necessity of some newly introduced metrics. That would be helpful for new readers to understand, ok, this is important to evaluate the protein design models and bring new insights to the community. 
- Why the authors choose ESM2-8M - a very small representation learning model as the encoder across the study. As a usual practice, most of works use 650M model. Could the author reason the necessity of using 8M model? Moreover, as a control comparison, in Table 3, 10, 11, the authors combine “DiMA-8M” with other ESM2 encoders while in the main experiment, the authors claims using DiMA-33M. How do the authors explain the discrepancy between? Or is this a typo?
- Could the author provide a illustration figure in the main text? That would be helpful for readers to quickly grasp what you have done.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces DiMA, a latent diffusion model designed for generating protein sequences using embeddings from the pre-trained protein language model ESM-2. DiMA aims to address the limitations of current models, which often struggle to achieve both high quality and diversity in unconditional protein sequence generation.

This work provides an in-depth exploration of model components and performs extensive evaluation across multiple metrics to validate DiMA’s sequence quality and diversity.

### Strengths
- **Comprehensive Evaluation Metrics**: The authors use a robust set of evaluation metrics, covering quality, distribution similarity, diversity, biological relevance, and both sequence-based and structure-based evaluations.

- **Well-Designed Ablation Study**: The study effectively demonstrates the contribution of each component, particularly the ESM encoder and self-conditioning. The authors also investigate the impact of the noise schedule and model scaling, offering valuable insights into best practices for latent diffusion models in protein generation.

- **Empirical Performance**: The authors compare DiMA against a broad range of baseline models and pretrained models for the unconditional generation task, providing a thorough analysis. DiMA achieves comparable generation quality with larger pretrained models using significantly fewer parameters.

### Weaknesses
 - **Limited to Unconditional Generation**: DiMA’s design is currently limited to unconditional generation, which poses challenges for performing tasks such as sequence inpainting, motif scaffolding, or guided design. This is a key limitation of DiMA and diffusion models in continuous embedding space. I suggest that the authors discuss and explore the potential of extending DiMA to these tasks, which could greatly enhance the versatility of this work. Specifically, the lack of explicit mechanisms for incorporating constraints or target structures during generation severely restricts its applicability in practical protein engineering scenarios.

- The authors could also consider evaluating DiMA on protein representation learning tasks, similar to those presented in DPLM. While the paper focuses on generation, assessing the quality of the learned representations would provide a more complete picture of the model's capabilities. This could involve evaluating the embeddings on downstream tasks such as protein classification or function prediction.

- In the main experiment, it is stated, “For a fair comparison, we train each method from scratch with the same parameter count (33M) as DiMA on the same dataset.” However, DiMA’s dependency on the ESM-2 encoder increases the effective parameter count, which could affect the reliability of these comparisons. The computational cost of the ESM-2 encoder during training, even if not used during inference, should be acknowledged and its impact on training efficiency discussed. This is especially relevant when comparing against models that do not rely on such pre-trained encoders.

- **Inconsistencies in Tables**: Some tables lack consistency, particularly Table 5, where the best-performing models are not consistently bolded. For example, in the Progen ppl column, DPLM-3B is bolded, even though DPLM-150M performs better. Correcting these inconsistencies would improve clarity and fairness. This lack of attention to detail undermines the credibility of the reported results.

- **Paper Structure**: Improving the structure of the paper would enhance readability. For example, Section 4 currently only has one subsection (4.1). Creating subsections for ablation studies and other experiments could provide better organization and make the results easier to follow. The current structure makes it difficult to navigate and understand the experimental setup and results.

### Questions
- Please review and correct the citation formatting for consistency.

- I suggest including the forward transition kernel in Section 3, clarifying how the noise schedule is used to determine the mean and variance.

- For the CD0.95 metric, does a higher value indicate greater diversity? In Table 2, 0.990 is bolded, suggesting it is considered the best. Please clarify this metric.

- I wonder why is the FD-seq metric not zero for the ground truth dataset, Is this due to sampling variability? Additionally, FD-STRUCT appears consistently lower than FD-seq—is this due to the lower dimensionality of the structure representation?

- What was the intuition behind choosing 320 as the hidden dimension for the diffusion backbone model? Also, have you considered using the fine-tuned ESM-2 model directly, as seen in DPLM?

- **Potential Bias in pLDDT Evaluation**: Since you use ESMFold to evaluate pLDDT and the ESM-2 encoder in DiMA, could this create a risk of biased evaluation? It may be worth considering alternative pLDDT metrics, such as those from AF2 or OmegaFold 2, to mitigate potential bias.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents DiMA (Diffusion on Language Model Encodings for Protein Sequence Generation), a framework for generating protein sequences. DiMA addresses the challenge of generating high-quality, diverse protein sequences by leveraging latent diffusion on protein language model (pLM) encodings from ESM-2. Existing protein generation models struggle to balance quality, diversity, and parameter efficiency, especially for unconditional generation, which is essential for creating novel protein structures without predefined constraints.

### Strengths
1. The combination of latent diffusion modeling with protein language model encodings is interesting.
2. The manuscript is well-organized and clearly written.
3. The experiments are extensive, with a set of rigorous evaluation metrics.

### Weaknesses
1. While latent diffusion is novel in this context, the motivation for choosing this approach over more conventional methods like sequence-based discrete diffusion or 3D-structure-based continuous diffusion is not strongly justified. The authors could strengthen their argument by highlighting specific challenges with current discrete or continuous approaches in handling the protein data structure.
2. It omits comparisons with strong baseline models like Chroma [1] and MultiFlow [2].
3. Although DiMA is designed to generate diverse sequences, the paper does not sufficiently analyze sequence variability at the biochemical or functional level.
4. The current citation format, as mentioned, should follow the convention of \citep rather than \cite for clarity and consistency.

### Questions
The paper is a valuable contribution to protein sequence generation through latent diffusion modeling. However, the work could be strengthened by deeper motivation for the latent diffusion choice and comparisons with recent models like Chroma and MultiFlow. I really admire this work for its comprehensive evaluation, but I doubt it is good enough for this top AI conference.

### Soundness
2

### Presentation
2

### Contribution
2
